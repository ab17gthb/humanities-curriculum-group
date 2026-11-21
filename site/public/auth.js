// Humanities Curriculum Group — accounts, cloud plan sync, entitlement.
//
// Phase 1 (Oct 2026): teachers can sign in with Google or with an email
// address and password, and can create an account from the same dialog.
// Their planner data (the same localStorage keys the planners already use) is mirrored to
// Firestore at hcgUsers/{uid} so it follows them across devices. Everything
// fails soft: if Firebase or Firestore is unreachable, the site behaves
// exactly as it did before accounts existed, and plans stay on the device.
//
// Sync model:
//  - On sign-in we read hcgUsers/{uid}. If the account has no plans yet, the
//    plans on this device are uploaded. If the device has no plans and the
//    account does, the account plans are applied here and the page reloads
//    once so the planners boot from them. If both have plans and they
//    differ, you can download backups, keep both unchanged, or select a copy.
//  - While signed in, writes to the plan keys are debounce-uploaded
//    (localStorage.setItem is wrapped; the wrapper also stamps a local
//    last-saved date used by the conflict prompt).
//  - Writes use merge and never touch the doc's `entitlement` field.
//
// Entitlement: hcgUsers/{uid}.entitlement, written ONLY by the
// stripeWebhook function ({ allAccess: bool, status, currentPeriodEnd,
// stripeCustomerId, stripeSubscriptionId, updatedAt }). Paid pages gate
// downloads on HCGAuth.entitlement().paid === true after HCGAuth.onChange
// fires (it fires again once the account doc has been read). The free
// Progressive Era sample is never gated.

(function () {
  "use strict";

  var SDK_VERSION = "10.12.2";
  var SDK_BASE = "/vendor/firebase/";
  var PLAN_KEYS = ["hcg_unit_v1", "hcg_unit_ga_v1", "hcg_unit_wwi_v1", "hcg_unit_tw_v1", "hcg_unit_dp_v1", "hcg_unit_ww2_v1", "hcg_unit_cw_v1", "hcg_unit_cr_v1", "hcg_unit_ma_v1", "hcg_unit_ca_v1", "hcg_unit_fd_v1", "hcg_unit_er_v1", "hcg_unit_jr_v1", "hcg_unit_sc_v1", "hcg_unit_rc_v1", "hcg_year_v1", "hcg_year_plans_v1"];
  var META_KEY = "hcg_sync_meta";
  // Owner/admin accounts: full access without a subscription, regardless of
  // the Firestore entitlement field. Firebase Storage rules enforce the
  // same list server-side, so downloads work for these accounts too.
  // Assembled from parts so no full address appears in the served file
  // for address harvesters (all three mailboxes are on the same domain).
  var ADMIN_EMAILS = ["alexbrouhard1", "alexbrouhardedu", "knowethcg"].map(function (u) { return u + "@" + "gmail.com"; });

  var user = null;               // firebase.User or null
  var authResolved = false;      // onAuthStateChanged has fired at least once
  var listeners = [];
  var entitlementCache = { paid: false };
  var syncState = { status: "idle", at: null };
  var syncGeneration = 0, localRevision = 0;
  var uploading = false, resolving = false;
  var confirmedCloud = null;
  var syncReady = false;         // true after the sign-in resolution finishes
  var applyingCloud = false;     // true while we write cloud plans locally
  var uploadTimer = null;
  var sdkPromise = null;
  var auth = null, db = null, st = null, fns = null;
  var PENDING_CHECKOUT_KEY = "hcg_pending_checkout";
  var authUi = {
    built: false,
    open: false,
    mode: "signin",
    busy: false,
    checkoutInterval: null,
    trigger: null,
    previousBodyOverflow: ""
  };
  var checkoutContinuing = false;

  // ---------------- small helpers ----------------
  function $(id) { return document.getElementById(id); }
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function canonical(v) {
    if (v === null || typeof v !== "object") return JSON.stringify(v);
    if (Array.isArray(v)) return "[" + v.map(canonical).join(",") + "]";
    return "{" + Object.keys(v).sort().map(function (k) {
      return JSON.stringify(k) + ":" + canonical(v[k]);
    }).join(",") + "}";
  }
  function fmtDate(iso) {
    if (!iso) return "an unknown date";
    var d = new Date(iso);
    if (isNaN(d.getTime())) return "an unknown date";
    return d.toLocaleString("en-US", { month: "short", day: "numeric", year: "numeric", hour: "numeric", minute: "2-digit" });
  }

  // ---------------- local plan set ----------------
  var rawSetItem = localStorage.setItem.bind(localStorage);
  var rawRemoveItem = localStorage.removeItem.bind(localStorage);

  function readLocalPlans() {
    var out = {};
    PLAN_KEYS.forEach(function (k) {
      var raw = null;
      try { raw = localStorage.getItem(k); } catch (e) {}
      if (!raw) { out[k] = null; return; }
      try { out[k] = JSON.parse(raw); } catch (e) { out[k] = null; }
    });
    return out;
  }
  function localIsEmpty(plans) {
    return PLAN_KEYS.every(function (k) { return plans[k] == null; });
  }
  function localSavedAt() {
    try {
      var m = JSON.parse(localStorage.getItem(META_KEY));
      return m && m.updatedAt ? m.updatedAt : null;
    } catch (e) { return null; }
  }
  function stampLocal(iso) {
    try { rawSetItem(META_KEY, JSON.stringify({ updatedAt: iso || new Date().toISOString() })); } catch (e) {}
  }
  function applyPlansToLocal(plans, savedAt) {
    var previous = {};
    try { PLAN_KEYS.forEach(function (k) { previous[k] = localStorage.getItem(k); }); }
    catch (e) { return false; }
    applyingCloud = true;
    try {
      PLAN_KEYS.forEach(function (k) {
        if (plans[k] == null) rawRemoveItem(k);
        else rawSetItem(k, JSON.stringify(plans[k]));
      });
      stampLocal(savedAt);
      return true;
    } catch (e) {
      // Best effort rollback. Conflict and restore paths also have a stored backup.
      PLAN_KEYS.forEach(function (k) {
        try {
          if (previous[k] == null) rawRemoveItem(k);
          else rawSetItem(k, previous[k]);
        } catch (ignored) {}
      });
      console.warn("HCG sync: could not apply account plans locally.", e);
      return false;
    } finally { applyingCloud = false; }
  }

  // Identical renders are not new saves and should not queue a cloud write.
  localStorage.setItem = function (key, value) {
    var plan = PLAN_KEYS.indexOf(key) !== -1;
    var changed = !plan || localStorage.getItem(key) !== String(value);
    if (!changed) return;
    rawSetItem(key, value);
    if (plan && !applyingCloud) {
      localRevision++;
      stampLocal(new Date().toISOString());
      if (user && syncReady && !syncIsPaused()) scheduleUpload();
    }
  };

  // ---------------- Firebase loading (lazy, fail-soft) ----------------
  function loadScript(src) {
    return new Promise(function (resolve, reject) {
      var s = document.createElement("script");
      s.src = src; s.async = true;
      s.onload = resolve; s.onerror = reject;
      document.head.appendChild(s);
    });
  }
  function ensureFirebase() {
    if (sdkPromise) return sdkPromise;
    sdkPromise = (async function () {
      if (!window.HCG_FIREBASE_CONFIG) throw new Error("firebase-config.js not loaded");
      await loadScript(SDK_BASE + "firebase-app-compat.js");
      await loadScript(SDK_BASE + "firebase-auth-compat.js");
      await loadScript(SDK_BASE + "firebase-firestore-compat.js");
      await loadScript(SDK_BASE + "firebase-storage-compat.js");
      await loadScript(SDK_BASE + "firebase-functions-compat.js");
      if (!window.firebase) throw new Error("Firebase SDK failed to load");
      if (!firebase.apps.length) firebase.initializeApp(window.HCG_FIREBASE_CONFIG);
      auth = firebase.auth();
      db = firebase.firestore();
      st = firebase.storage();
      fns = firebase.functions();
      auth.onAuthStateChanged(onAuthChanged, function (err) {
        console.warn("HCG auth state error:", err);
      });
      // Surface redirect sign-in results/errors (popup fallback path).
      auth.getRedirectResult().catch(function (err) {
        if (err && err.code !== "auth/no-current-user") console.warn("HCG redirect sign-in:", err);
      });
      return true;
    })();
    sdkPromise.catch(function (err) {
      console.warn("HCG accounts unavailable; continuing device-only.", err);
      sdkPromise = null; // allow a later retry from the Sign in button
    });
    return sdkPromise;
  }

  // ---------------- account control UI ----------------
  function syncLabel() {
    if (!user) return "Saved in this browser. Sign in to sync across devices.";
    if (syncState.status === "ok") return "Saved in this browser and synced to your account.";
    if (syncState.status === "empty") return "No plans to sync yet.";
    if (syncState.status === "paused") return "Saved in this browser. Account sync is paused.";
    if (syncState.status === "changed") return "Plans changed on another device or in another tab. Nothing was overwritten. Open Planner backups to resume sync.";
    if (syncState.status === "conflict") return "Saved in this browser. Choose which copy to use.";
    if (syncState.status === "waiting") return "Saved in this browser. Waiting for the account to confirm.";
    if (syncState.status === "error") return "Saved in this browser. Account sync could not finish.";
    if (syncState.status === "device-error") return "This browser couldn't load the account plans. Check Planner backups.";
    return "Saved in this browser. Syncing to your account…";
  }
  function renderControl() {
    var host = $("hcg-account");
    if (!host) return;
    if (user) {
      var name = (user.displayName || user.email || "Account").split(" ")[0].split("@")[0];
      host.innerHTML =
        "<button type='button' class='hcg-acct-btn' id='hcg-acct-toggle' aria-haspopup='true' aria-expanded='false'>" +
          esc(name) + " <span class='hcg-caret'>▾</span></button>" +
        "<div class='hcg-menu' id='hcg-menu' hidden>" +
          "<a href='home.html'>My Day</a>" +
          "<a href='subscribe.html'>Subscribe</a>" +
          (isAdminUser() ? "<a href='inbox.html'>Inbox</a><a href='leads.html'>Email list</a><a href='stats.html'>Stats</a>" : "") +
          "<div class='hcg-sync' id='hcg-sync-line'>" + esc(syncLabel()) + "</div>" +
          "<button type='button' class='hcg-signout' id='hcg-signout'>Sign out</button>" +
        "</div>";
      var toggle = $("hcg-acct-toggle"), menu = $("hcg-menu");
      toggle.addEventListener("click", function (ev) {
        ev.stopPropagation();
        var open = menu.hidden;
        menu.hidden = !open;
        toggle.setAttribute("aria-expanded", String(open));
      });
      document.addEventListener("click", function (ev) {
        if (!menu.hidden && !host.contains(ev.target)) { menu.hidden = true; toggle.setAttribute("aria-expanded", "false"); }
      });
      document.addEventListener("keydown", function (ev) {
        if (ev.key === "Escape" && !menu.hidden) { menu.hidden = true; toggle.setAttribute("aria-expanded", "false"); }
      });
      $("hcg-signout").addEventListener("click", function () { HCGAuth.signOut(); });
    } else {
      host.innerHTML = "<button type='button' class='hcg-acct-btn' id='hcg-signin'>Sign in</button>";
      $("hcg-signin").addEventListener("click", function () { HCGAuth.signIn(); });
    }
  }
  function updateSyncLine() {
    var el = $("hcg-sync-line");
    if (el) el.textContent = syncLabel();
  }

  // ---------------- sign-in / account creation dialog ----------------
  // The dialog is injected by this file so every page gets the same account
  // flow without duplicating markup. Teachers can use Google or an email
  // address and password. Email passwords are handled by Firebase
  // Authentication; this site never receives or stores them.
  function normalizeCheckoutInterval(value) {
    return value === "year" ? "year" : "month";
  }
  function getPendingCheckout() {
    try {
      var value = window.sessionStorage.getItem(PENDING_CHECKOUT_KEY);
      return value === "month" || value === "year" ? value : null;
    } catch (e) { return null; }
  }
  function setPendingCheckout(interval) {
    authUi.checkoutInterval = normalizeCheckoutInterval(interval);
    try { window.sessionStorage.setItem(PENDING_CHECKOUT_KEY, authUi.checkoutInterval); } catch (e) {}
  }
  function clearPendingCheckout() {
    authUi.checkoutInterval = null;
    try { window.sessionStorage.removeItem(PENDING_CHECKOUT_KEY); } catch (e) {}
  }

  function ensureAuthStyles() {
    if ($("hcg-auth-style")) return;
    var style = document.createElement("style");
    style.id = "hcg-auth-style";
    style.textContent =
      ".hcg-auth-overlay[hidden]{display:none!important}" +
      ".hcg-auth-panel [hidden]{display:none!important}" +
      ".hcg-auth-overlay{position:fixed;inset:0;z-index:1000;background:rgba(23,32,48,.64);display:flex;align-items:center;justify-content:center;overflow-y:auto;padding:24px 16px;font-family:Arial,sans-serif}" +
      ".hcg-auth-panel{position:relative;background:#fff;color:#26313f;width:440px;max-width:100%;max-height:calc(100vh - 48px);overflow-y:auto;border-radius:8px;padding:28px;box-shadow:0 24px 70px rgba(0,0,0,.35)}" +
      ".hcg-auth-panel h2{font-family:Georgia,'Times New Roman',serif;font-weight:normal;font-size:27px;color:var(--navy);margin:0 38px 8px 0}" +
      ".hcg-auth-context{font-size:15.5px;line-height:1.45;color:#4b5563;margin:0 0 20px}" +
      ".hcg-auth-close{position:absolute;top:10px;right:12px;background:none;border:none;color:#5f6873;font-size:30px;line-height:1;padding:6px;cursor:pointer}" +
      ".hcg-auth-close:hover{color:var(--navy)}" +
      ".hcg-auth-google{width:100%;background:#fff;color:#26313f;border:1px solid #b9c0c9;border-radius:5px;padding:11px 14px;font:inherit;font-size:15.5px;font-weight:bold;cursor:pointer}" +
      ".hcg-auth-google:hover{border-color:var(--navy);background:#faf8f2}" +
      ".hcg-auth-divider{display:flex;align-items:center;gap:12px;margin:18px 0;color:#6b7280;font-size:13px}" +
      ".hcg-auth-divider:before,.hcg-auth-divider:after{content:'';height:1px;background:#ddd6c4;flex:1}" +
      ".hcg-auth-tabs{display:grid;grid-template-columns:1fr 1fr;background:#f3efe4;border:1px solid #ddd6c4;border-radius:5px;padding:3px;margin-bottom:18px}" +
      ".hcg-auth-tabs button{background:transparent;border:none;border-radius:3px;color:#5f6259;font:inherit;font-size:14.5px;padding:8px 6px;cursor:pointer}" +
      ".hcg-auth-tabs button[aria-selected='true']{background:#fff;color:var(--navy);font-weight:bold;box-shadow:0 1px 4px rgba(31,51,80,.16)}" +
      ".hcg-auth-field{display:block;font-size:14px;font-weight:bold;color:#374151;margin:0 0 14px}" +
      ".hcg-auth-field input{display:block;width:100%;box-sizing:border-box;margin-top:6px;border:1px solid #b9c0c9;border-radius:5px;padding:11px 12px;font:inherit;font-size:16px;font-weight:normal;color:#26313f;background:#fff}" +
      ".hcg-auth-field input:focus{outline:2px solid rgba(48,86,140,.3);border-color:var(--navy)}" +
      ".hcg-auth-error{background:#fdf0ec;border-left:3px solid #b5442c;color:#7c2d1d;padding:10px 12px;font-size:14.5px;line-height:1.4;margin:0 0 14px}" +
      ".hcg-auth-success{background:#eef6ec;border-left:3px solid #39713a;color:#28512a;padding:10px 12px;font-size:14.5px;line-height:1.4;margin:0 0 14px}" +
      ".hcg-auth-submit{width:100%;background:var(--rust);color:#fff;border:none;border-radius:5px;padding:12px 14px;font:inherit;font-size:16px;font-weight:bold;cursor:pointer}" +
      ".hcg-auth-submit:hover{background:#9d4f2d}" +
      ".hcg-auth-link{display:block;margin:12px auto 0;background:none;border:none;color:var(--navy);font:inherit;font-size:14.5px;text-decoration:underline;cursor:pointer;padding:4px}" +
      ".hcg-auth-cancel{display:block;margin:8px auto 0;background:none;border:none;color:#68707a;font:inherit;font-size:14.5px;cursor:pointer;padding:4px}" +
      ".hcg-auth-note{font-size:13px;line-height:1.45;color:#6b7280;margin:18px 0 0;text-align:center}" +
      ".hcg-auth-panel button:disabled,.hcg-auth-panel input:disabled{opacity:.58;cursor:wait}" +
      "@media(max-width:520px){.hcg-auth-overlay{padding:14px 10px}.hcg-auth-panel{padding:24px 20px;max-height:calc(100vh - 28px)}}";
    document.head.appendChild(style);
  }

  function authMessage(kind, text) {
    var error = $("hcg-auth-error"), success = $("hcg-auth-success");
    if (error) { error.hidden = kind !== "error"; error.textContent = kind === "error" ? text : ""; }
    if (success) { success.hidden = kind !== "success"; success.textContent = kind === "success" ? text : ""; }
  }
  function authErrorMessage(err) {
    var code = err && err.code ? String(err.code) : "";
    if (code === "auth/invalid-credential" || code === "auth/wrong-password" || code === "auth/user-not-found") {
      return "That email address and password do not match an account. Check them and try again, or create a new account.";
    }
    if (code === "auth/email-already-in-use") {
      return "An account already uses that email address. Switch to Sign in, or reset the password if you have forgotten it.";
    }
    if (code === "auth/weak-password") return "Choose a password with at least 6 characters.";
    if (code === "auth/invalid-email") return "Enter a valid email address.";
    if (code === "auth/too-many-requests") return "Too many attempts. Wait a few minutes and try again.";
    if (code === "auth/network-request-failed") return "The connection failed. Check your internet connection and try again.";
    if (code === "auth/popup-closed-by-user" || code === "auth/cancelled-popup-request") {
      return "The Google sign-in window was closed before sign-in finished. Try again when you are ready.";
    }
    if (code === "auth/operation-not-allowed") return "Email sign-in is not available right now. Continue with Google instead.";
    return "Sign-in could not finish. Try again in a moment." + (code ? " (" + code + ")" : "");
  }
  function setAuthBusy(busy) {
    authUi.busy = !!busy;
    var overlay = $("hcg-auth-overlay");
    if (!overlay) return;
    overlay.querySelectorAll("button,input").forEach(function (el) { el.disabled = authUi.busy; });
    var submit = $("hcg-auth-submit");
    if (submit) submit.textContent = authUi.busy ? "Please wait…" : (authUi.mode === "create" ? "Create account" : "Sign in");
    var google = $("hcg-auth-google");
    if (google) google.textContent = authUi.busy ? "Please wait…" : "Continue with Google";
  }
  function setAuthMode(mode) {
    authUi.mode = mode === "create" ? "create" : "signin";
    var creating = authUi.mode === "create";
    var title = $("hcg-auth-title"), submit = $("hcg-auth-submit");
    if (title) title.textContent = creating ? "Create your account" : "Sign in";
    if (submit) submit.textContent = creating ? "Create account" : "Sign in";
    var nameWrap = $("hcg-auth-name-wrap"), forgot = $("hcg-auth-forgot"), password = $("hcg-auth-password");
    if (nameWrap) nameWrap.hidden = !creating;
    if (forgot) forgot.hidden = creating;
    if (password) password.setAttribute("autocomplete", creating ? "new-password" : "current-password");
    var signinTab = $("hcg-auth-tab-signin"), createTab = $("hcg-auth-tab-create");
    if (signinTab) signinTab.setAttribute("aria-selected", String(!creating));
    if (createTab) createTab.setAttribute("aria-selected", String(creating));
    authMessage("", "");
  }

  function ensureAuthUi() {
    if (authUi.built) return;
    ensureAuthStyles();
    var overlay = document.createElement("div");
    overlay.id = "hcg-auth-overlay";
    overlay.className = "hcg-auth-overlay";
    overlay.hidden = true;
    overlay.innerHTML =
      "<div class='hcg-auth-panel' role='dialog' aria-modal='true' aria-labelledby='hcg-auth-title'>" +
        "<button type='button' class='hcg-auth-close' id='hcg-auth-close' aria-label='Close'>&times;</button>" +
        "<h2 id='hcg-auth-title'>Sign in</h2>" +
        "<p class='hcg-auth-context' id='hcg-auth-context'>Sign in or create an account to save your plans to your account.</p>" +
        "<button type='button' class='hcg-auth-google' id='hcg-auth-google'>Continue with Google</button>" +
        "<div class='hcg-auth-divider'><span>or use email</span></div>" +
        "<div class='hcg-auth-tabs' role='tablist' aria-label='Email account options'>" +
          "<button type='button' id='hcg-auth-tab-signin' aria-selected='true'>Sign in</button>" +
          "<button type='button' id='hcg-auth-tab-create' aria-selected='false'>Create account</button>" +
        "</div>" +
        "<form id='hcg-auth-form' novalidate>" +
          "<label class='hcg-auth-field' id='hcg-auth-name-wrap' hidden>Name <span style='font-weight:normal;color:#6b7280;'>(optional)</span>" +
            "<input type='text' id='hcg-auth-name' autocomplete='name'></label>" +
          "<label class='hcg-auth-field'>Email address" +
            "<input type='email' id='hcg-auth-email' autocomplete='email' required></label>" +
          "<label class='hcg-auth-field'>Password" +
            "<input type='password' id='hcg-auth-password' autocomplete='current-password' required></label>" +
          "<p class='hcg-auth-error' id='hcg-auth-error' role='alert' hidden></p>" +
          "<p class='hcg-auth-success' id='hcg-auth-success' role='status' hidden></p>" +
          "<button type='submit' class='hcg-auth-submit' id='hcg-auth-submit'>Sign in</button>" +
          "<button type='button' class='hcg-auth-link' id='hcg-auth-forgot'>Forgot your password?</button>" +
        "</form>" +
        "<button type='button' class='hcg-auth-cancel' id='hcg-auth-cancel'>Not now</button>" +
        "<p class='hcg-auth-note'>Your password is handled by Firebase Authentication. This site never receives or stores it.</p>" +
      "</div>";
    document.body.appendChild(overlay);
    authUi.built = true;

    $("hcg-auth-close").addEventListener("click", function () { closeAuth(true); });
    $("hcg-auth-cancel").addEventListener("click", function () { closeAuth(true); });
    overlay.addEventListener("click", function (ev) { if (ev.target === overlay) closeAuth(true); });
    document.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape" && authUi.open) closeAuth(true);
    });
    $("hcg-auth-tab-signin").addEventListener("click", function () { setAuthMode("signin"); });
    $("hcg-auth-tab-create").addEventListener("click", function () { setAuthMode("create"); });
    $("hcg-auth-google").addEventListener("click", signInWithGoogle);
    $("hcg-auth-form").addEventListener("submit", submitEmailAuth);
    $("hcg-auth-forgot").addEventListener("click", sendPasswordReset);
  }

  async function openAuth(options) {
    options = options || {};
    if (user) return true;
    if (options.checkoutInterval) setPendingCheckout(options.checkoutInterval);
    else if (getPendingCheckout()) authUi.checkoutInterval = getPendingCheckout();
    ensureAuthUi();
    var context = $("hcg-auth-context");
    if (context) {
      if (authUi.checkoutInterval) {
        context.textContent = "Sign in or create an account, then we will continue to secure checkout for the " +
          (authUi.checkoutInterval === "year" ? "annual" : "monthly") + " plan.";
      } else {
        context.textContent = options.message || "Sign in or create an account to save your plans to your account and use them on any device.";
      }
    }
    setAuthMode(options.mode === "create" ? "create" : "signin");
    authUi.trigger = document.activeElement;
    authUi.previousBodyOverflow = document.body ? document.body.style.overflow : "";
    authUi.open = true;
    $("hcg-auth-overlay").hidden = false;
    if (document.body) document.body.style.overflow = "hidden";
    var email = $("hcg-auth-email");
    if (email) setTimeout(function () { email.focus(); }, 0);
    try { await ensureFirebase(); }
    catch (e) { authMessage("error", "Sign-in is temporarily unavailable. Check your connection and try again."); }
    if (user) closeAuth(false);
    return true;
  }
  function closeAuth(cancelled) {
    if (!authUi.open) return;
    authUi.open = false;
    if (authUi.busy) setAuthBusy(false);
    var overlay = $("hcg-auth-overlay");
    if (overlay) overlay.hidden = true;
    if (document.body) document.body.style.overflow = authUi.previousBodyOverflow || "";
    if (cancelled) clearPendingCheckout();
    if (authUi.trigger && typeof authUi.trigger.focus === "function") {
      try { authUi.trigger.focus(); } catch (e) {}
    }
  }

  async function signInWithGoogle() {
    if (authUi.busy) return;
    setAuthBusy(true);
    authMessage("", "");
    try {
      await ensureFirebase();
      if (!auth) throw new Error("Auth unavailable");
      if (user) { closeAuth(false); return; }
      var provider = new firebase.auth.GoogleAuthProvider();
      provider.setCustomParameters({ prompt: "select_account" });
      try {
        var gcred = await auth.signInWithPopup(provider);
        if (gcred && gcred.additionalUserInfo && gcred.additionalUserInfo.isNewUser && window.HCGStats) window.HCGStats.log("signup");
      } catch (popupErr) {
        var code = popupErr && popupErr.code ? String(popupErr.code) : "";
        if (code === "auth/popup-closed-by-user" || code === "auth/cancelled-popup-request") throw popupErr;
        console.warn("HCG popup sign-in failed; falling back to redirect.", code, popupErr);
        await auth.signInWithRedirect(provider);
        return;
      }
      closeAuth(false);
    } catch (e) {
      console.warn("HCG Google sign-in failed:", e);
      authMessage("error", authErrorMessage(e));
    } finally {
      if (authUi.open) setAuthBusy(false);
    }
  }

  async function submitEmailAuth(ev) {
    ev.preventDefault();
    if (authUi.busy) return;
    var emailEl = $("hcg-auth-email"), passwordEl = $("hcg-auth-password"), nameEl = $("hcg-auth-name");
    var email = emailEl ? emailEl.value.trim() : "";
    var password = passwordEl ? passwordEl.value : "";
    var name = nameEl ? nameEl.value.trim() : "";
    authMessage("", "");
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      authMessage("error", "Enter a valid email address.");
      if (emailEl) emailEl.focus();
      return;
    }
    if (!password || (authUi.mode === "create" && password.length < 6)) {
      authMessage("error", authUi.mode === "create" ? "Choose a password with at least 6 characters." : "Enter your password.");
      if (passwordEl) passwordEl.focus();
      return;
    }
    setAuthBusy(true);
    try {
      await ensureFirebase();
      if (!auth) throw new Error("Auth unavailable");
      if (authUi.mode === "create") {
        var cred = await auth.createUserWithEmailAndPassword(email, password);
        if (name && cred && cred.user) {
          try { await cred.user.updateProfile({ displayName: name }); } catch (e) { console.warn("HCG display name update failed:", e); }
        }
        if (window.HCGStats) window.HCGStats.log("signup");
      } else {
        await auth.signInWithEmailAndPassword(email, password);
      }
      closeAuth(false);
    } catch (e) {
      console.warn("HCG email sign-in failed:", e);
      authMessage("error", authErrorMessage(e));
    } finally {
      if (authUi.open) setAuthBusy(false);
    }
  }

  async function sendPasswordReset() {
    if (authUi.busy) return;
    var emailEl = $("hcg-auth-email");
    var email = emailEl ? emailEl.value.trim() : "";
    authMessage("", "");
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      authMessage("error", "Enter your email address above, then choose Forgot your password again.");
      if (emailEl) emailEl.focus();
      return;
    }
    setAuthBusy(true);
    try {
      await ensureFirebase();
      if (!auth) throw new Error("Auth unavailable");
      await auth.sendPasswordResetEmail(email);
      authMessage("success", "Password reset email sent to " + email + ". Follow the link in that email to choose a new password.");
    } catch (e) {
      console.warn("HCG password reset failed:", e);
      authMessage("error", authErrorMessage(e));
    } finally {
      setAuthBusy(false);
    }
  }

  async function continuePendingCheckout() {
    if (!user || checkoutContinuing) return;
    var interval = getPendingCheckout();
    if (!interval) return;
    clearPendingCheckout();
    if (HCGEntitlement.current().paid) return;
    checkoutContinuing = true;
    try {
      var url = await HCGAuth.startCheckout(interval);
      window.location.href = url;
    } catch (e) {
      checkoutContinuing = false;
      console.warn("HCG checkout continuation failed:", e);
      window.alert("You are signed in, but checkout could not start. Return to the Subscribe page and choose your plan again.");
      if (!/subscribe\.html$/.test(window.location.pathname)) window.location.href = "subscribe.html";
    }
  }

  // ---------------- entitlement ----------------
  // Paid unit pages check HCGAuth.entitlement().paid === true.
  function isAdminUser() {
    return !!user && !!user.email && ADMIN_EMAILS.indexOf(String(user.email).toLowerCase()) !== -1;
  }
  function adminEntitlement() {
    return { paid: true, allAccess: true, status: "active", currentPeriodEnd: null, stripeCustomerId: null, stripeSubscriptionId: null, source: "admin" };
  }
  var HCGEntitlement = {
    current: function () {
      if (isAdminUser()) return adminEntitlement();
      return Object.assign({}, entitlementCache);
    },
    refresh: async function () {
      if (!user || !db) return HCGEntitlement.current();
      try {
        var snap = await db.collection("hcgUsers").doc(user.uid).get();
        var data = snap.exists ? snap.data() : null;
        entitlementCache = normalizeEntitlement(data && data.entitlement);
      } catch (e) { console.warn("HCG entitlement read failed:", e); }
      return HCGEntitlement.current();
    }
  };
  function normalizeEntitlement(ent) {
    if (!ent || typeof ent !== "object") {
      if (isAdminUser()) return adminEntitlement();
      return { paid: false, allAccess: false, status: null, currentPeriodEnd: null };
    }
    var end = ent.currentPeriodEnd || null;
    if (end && typeof end.toDate === "function") { try { end = end.toDate().toISOString(); } catch (e) { end = null; } }
    else if (end && typeof end === "object" && typeof end.seconds === "number") {
      end = new Date(end.seconds * 1000).toISOString();
    }
    var status = ent.status || null;
    if (isAdminUser()) {
      var adm = adminEntitlement();
      adm.currentPeriodEnd = end;
      adm.stripeCustomerId = ent.stripeCustomerId || null;
      adm.stripeSubscriptionId = ent.stripeSubscriptionId || null;
      return adm;
    }
    return {
      paid: ent.allAccess === true && (status === "active" || status === "trialing"),
      allAccess: ent.allAccess === true,
      status: status,
      currentPeriodEnd: end,
      stripeCustomerId: ent.stripeCustomerId || null,
      stripeSubscriptionId: ent.stripeSubscriptionId || null
    };
  }
  window.HCGEntitlement = HCGEntitlement;

  // ---------------- paid file delivery ----------------
  // Download URLs come from Firebase Storage; the storage rules re-check
  // the entitlement on every read, so a URL is only minted for (and only
  // usable by) an entitled signed-in account.
  var HCGFiles = {
    url: async function (path) {
      if (!user) return null;
      try { await ensureFirebase(); } catch (e) { return null; }
      if (!st) return null;
      var ent = HCGEntitlement.current();
      if (!ent.paid) ent = await HCGEntitlement.refresh();
      if (!ent.paid) return null;
      try { return await st.ref(path).getDownloadURL(); }
      catch (e) { console.warn("HCG file URL failed:", e); return null; }
    }
  };
  window.HCGFiles = HCGFiles;

  // ---------------- planner backups ----------------
  var BACKUPS_KEY = "hcg_plan_backups_v1";
  var PAUSED_KEY = "hcg_plan_sync_paused_v1";
  var pauseInMemory = false;
  function planObject(v) { return !!v && typeof v === "object" && !Array.isArray(v); }
  function projectPlans(plans) {
    var out = {};
    PLAN_KEYS.forEach(function (k) { out[k] = plans && plans[k] != null ? plans[k] : null; });
    return out;
  }
  function pauseSync(persist) {
    pauseInMemory = true;
    syncReady = false;
    if (uploadTimer) { clearTimeout(uploadTimer); uploadTimer = null; }
    if (!persist) return true;
    try { window.sessionStorage.setItem(PAUSED_KEY, "1"); return true; }
    catch (e) { return false; }
  }
  function syncIsPaused() {
    if (pauseInMemory) return true;
    try { return window.sessionStorage.getItem(PAUSED_KEY) === "1"; }
    catch (e) { return false; }
  }
  function resumeSync() {
    if (!user || uploading || resolving) return;
    try { window.sessionStorage.removeItem(PAUSED_KEY); } catch (e) {}
    pauseInMemory = false;
    startPlanResolution();
  }
  function readBackups() {
    try {
      var stored = JSON.parse(localStorage.getItem(BACKUPS_KEY));
      return Array.isArray(stored) ? stored.filter(function (entry) { return entry && entry.device && entry.at; }) : [];
    } catch (e) { return []; }
  }
  function saveBackup(device, deviceAt, account, accountAt) {
    var backup = { at: new Date().toISOString(), owner: account && user ? user.uid : null,
      device: { savedAt: deviceAt, plans: projectPlans(device) },
      account: account ? { savedAt: accountAt, plans: projectPlans(account) } : null };
    var list = readBackups().slice(0, 2);
    list.unshift(backup);
    try { rawSetItem(BACKUPS_KEY, JSON.stringify(list)); return true; }
    catch (e) { return false; }
  }
  function downloadBackup(copy, side) {
    var data = { format: "hcg-planner-backup", version: 1, savedAt: copy.savedAt || null, plans: projectPlans(copy.plans) };
    var a = document.createElement("a");
    a.href = URL.createObjectURL(new Blob([JSON.stringify(data, null, 2)], { type: "application/json" }));
    a.download = "hcg-plans-" + side + "-" + new Date().toISOString().slice(0, 10) + ".json";
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(function () { URL.revokeObjectURL(a.href); }, 1000);
  }
  function validatePortable(data) {
    if (!planObject(data) || data.format !== "hcg-planner-backup" || data.version !== 1 || !planObject(data.plans)) return null;
    if (Object.keys(data.plans).length !== PLAN_KEYS.length ||
        !PLAN_KEYS.every(function (k) { return Object.prototype.hasOwnProperty.call(data.plans, k); })) return null;
    var seen = 0;
    function safe(v, depth) {
      if (++seen > 100000 || depth > 20) return false;
      if (typeof v === "string") return v.length <= 16000 && !/[<>]/.test(v) && !/^\s*(javascript|data|vbscript):/i.test(v);
      if (v === null || typeof v === "boolean") return true;
      if (typeof v === "number") return isFinite(v);
      if (!v || typeof v !== "object") return false;
      return Object.keys(v).every(function (k) {
        return k !== "__proto__" && k !== "prototype" && k !== "constructor" && !/[<>]/.test(k) && safe(v[k], depth + 1);
      });
    }
    function date(v) {
      if (typeof v !== "string" || !/^(19\d{2}|20\d{2}|21\d{2})-\d{2}-\d{2}$/.test(v)) return false;
      var d = new Date(v + "T00:00:00Z");
      return !isNaN(d.getTime()) && d.toISOString().slice(0, 10) === v;
    }
    function datePair(from, to) {
      return date(from) && date(to) && Math.abs(Date.parse(to) - Date.parse(from)) <= 732 * 86400000;
    }
    function year(v) {
      return planObject(v) && datePair(v.start, v.end) && Array.isArray(v.periods) &&
        Array.isArray(v.daysOff) && v.periods.every(function (p) {
          return planObject(p) && typeof p.name === "string" && date(p.end);
        }) && v.daysOff.every(function (d) {
          return planObject(d) && typeof d.label === "string" && typeof d.kind === "string" && datePair(d.from, d.to);
        });
    }
    function unit(v) {
      return planObject(v) && planObject(v.selected) &&
        (v.order == null || Array.isArray(v.order)) &&
        (v.customItems == null || (Array.isArray(v.customItems) && v.customItems.every(function (item) {
          return planObject(item) && typeof item.id === "string" && /^[a-zA-Z0-9_:-]{1,180}$/.test(item.id) &&
            (item.bp == null || Array.isArray(item.bp)) &&
            (item.link == null || item.link === "" || (typeof item.link === "string" && /^https?:\/\//i.test(item.link)));
        }))) &&
        (v.sections == null || (Array.isArray(v.sections) && v.sections.every(function (sec) {
          return planObject(sec) && datePair(sec.start, sec.test) &&
            ["dayTypes", "subDays", "homework", "pins"].every(function (field) { return sec[field] == null || planObject(sec[field]); });
        }))) && (v.active == null || (Number.isInteger(v.active) && v.active >= 0));
    }
    if (!safe(data.plans, 0) || !PLAN_KEYS.every(function (k) {
      var v = data.plans[k];
      if (v === null) return true;
      if (k === "hcg_year_v1") return year(v);
      if (k === "hcg_year_plans_v1") return planObject(v) && planObject(v.plans) && Object.values(v.plans).every(year);
      return unit(v);
    }) || localIsEmpty(data.plans)) return null;
    return { plans: projectPlans(data.plans), savedAt: typeof data.savedAt === "string" ? data.savedAt : null };
  }
  function modal(title) {
    var d = document.createElement("dialog");
    d.setAttribute("aria-label", title);
    d.style.cssText = "box-sizing:border-box;width:min(540px, calc(100% - 32px));max-height:calc(100% - 32px);overflow:auto;border:1px solid #b9c0c9;border-radius:8px;padding:22px;color:#26313f;background:#fff";
    var head = document.createElement("h2");
    head.textContent = title;
    d.appendChild(head);
    document.body.appendChild(d);
    d.addEventListener("close", function () { d.remove(); });
    return d;
  }
  function modalText(parent, value) {
    var p = document.createElement("p");
    p.textContent = value;
    parent.appendChild(p);
    return p;
  }
  function modalButton(parent, label, fn) {
    var b = document.createElement("button");
    b.className = "btn ghost";
    b.type = "button";
    b.style.margin = "0 6px 6px 0";
    b.textContent = label;
    b.addEventListener("click", fn);
    parent.appendChild(b);
    return b;
  }
  function presentModal(d) {
    if (typeof d.showModal !== "function") { d.remove(); return false; }
    d.showModal();
    return true;
  }
  function choosePlanCopy(local, localAt, cloud, cloudAt, backedUp) {
    return new Promise(function (resolve) {
      var d = modal("Two copies of your plans");
      modalText(d, "This browser and your account have different plans. Choose a copy to use, or keep both unchanged for now.");
      modalText(d, "This browser: " + fmtDate(localAt) + ". Account: " + fmtDate(cloudAt) + ".");
      modalText(d, backedUp ? "Both copies were saved in Planner backups on this browser. You can also download either copy now."
        : "This browser couldn't save a backup. Download either copy if you need it. Neither copy will be replaced.");
      modalButton(d, "Download browser copy", function () { downloadBackup({ plans: local, savedAt: localAt }, "browser"); });
      modalButton(d, "Download account copy", function () { downloadBackup({ plans: cloud, savedAt: cloudAt }, "account"); });
      var choices = document.createElement("p");
      d.appendChild(choices);
      function choose(value) { d.close(value); }
      modalButton(choices, "Keep both for now", function () { choose("pause"); }).autofocus = true;
      if (backedUp) {
        modalButton(choices, "Use browser copy in account", function () { choose("device"); });
        modalButton(choices, "Use account copy in browser", function () { choose("account"); });
      }
      d.addEventListener("close", function () { resolve(d.returnValue || "pause"); });
      if (!presentModal(d)) resolve("pause");
    });
  }
  function restoreCopy(copy, message) {
    if (uploading || resolving) { message.textContent = "Wait for the current sync check to finish, then try again."; return; }
    if (!window.confirm("Replace the plans in this browser with this backup? Your account copy will not be changed.")) return;
    if (!saveBackup(readLocalPlans(), localSavedAt(), null, null)) {
      message.textContent = "This browser couldn't back up your current plans. Nothing was replaced.";
      return;
    }
    if (!pauseSync(true)) {
      message.textContent = "This browser couldn't pause account sync across a reload. Nothing was replaced.";
      return;
    }
    setSyncState("paused");
    if (!applyPlansToLocal(copy.plans, copy.savedAt)) {
      message.textContent = "The browser couldn't finish the restore. Your prior plans are in Planner backups.";
      return;
    }
    location.reload();
  }
  function openPlannerBackups() {
    var d = modal("Planner backups");
    var message = modalText(d, "Backups stay on this browser unless you download a copy. Avoid putting student information in backup files.");
    message.setAttribute("role", "status");
    var local = readLocalPlans();
    if (!localIsEmpty(local)) modalButton(d, "Download current browser plans", function () {
      downloadBackup({ plans: readLocalPlans(), savedAt: localSavedAt() }, "browser");
    });
    if (user && !resolving && !uploading && (syncIsPaused() || syncState.status === "error")) {
      modalButton(d, syncIsPaused() ? "Resume account sync" : "Retry account sync", function () { d.close(); resumeSync(); });
    }
    readBackups().forEach(function (entry) {
      modalText(d, "Backup saved " + fmtDate(entry.at) + ".");
      [[entry.device, "browser"], [entry.owner && user && entry.owner === user.uid ? entry.account : null, "account"]]
        .forEach(function (pair) {
          if (!pair[0] || localIsEmpty(pair[0].plans)) return;
          modalButton(d, "Download " + pair[1] + " backup", function () { downloadBackup(pair[0], pair[1]); });
          modalButton(d, "Restore " + pair[1] + " backup here", function () { restoreCopy(pair[0], message); });
        });
    });
    var picker = document.createElement("input");
    picker.type = "file";
    picker.accept = ".json,application/json";
    picker.hidden = true;
    d.appendChild(picker);
    modalButton(d, "Open a backup file", function () { picker.click(); });
    picker.addEventListener("change", async function () {
      var file = picker.files[0];
      picker.value = "";
      if (!file) return;
      var copy = null;
      if (file.size <= 1500000) {
        try { copy = validatePortable(JSON.parse(await file.text())); } catch (e) {}
      }
      if (!copy) { message.textContent = "This file couldn't be restored. Choose a Planner backups JSON file with supported plan content."; return; }
      restoreCopy(copy, message);
    });
    modalButton(d, "Close", function () { d.close(); });
    if (!presentModal(d)) window.alert("Planner backups need a browser that supports dialogs. You can still use the existing plan export controls.");
  }

  // ---------------- cloud sync ----------------
  function docRef() { return db.collection("hcgUsers").doc(user.uid); }
  function setSyncState(status, at) {
    syncState = { status: status, at: at || null };
    updateSyncLine();
    window.dispatchEvent(new CustomEvent("hcgplansync"));
  }

  async function uploadPlans(savedAtIso, expectedCloud) {
    if (!user || !db || uploading || syncIsPaused() || !confirmedCloud) return false;
    var baseline = expectedCloud || confirmedCloud;
    var activeUser = user, generation = syncGeneration, revision = localRevision, plans = readLocalPlans();
    var at = savedAtIso || new Date().toISOString();
    uploading = true;
    setSyncState("pending");
    var warning = setTimeout(function () {
      if (generation === syncGeneration && uploading) setSyncState("waiting");
    }, 8000);
    try {
      var ref = docRef();
      var payload = { email: activeUser.email || null, displayName: activeUser.displayName || null,
        plans: plans, plansUpdatedAt: at };
      // Guard every upload, including an account that was empty on sign-in.
      // Other tabs or devices may have saved since our last server read/write.
      var replaced = await db.runTransaction(async function (tx) {
        var latest = await tx.get(ref);
        var current = latest.exists ? (latest.data() || {}) : {};
        if (generation !== syncGeneration || (expectedCloud && revision !== localRevision) ||
            canonical(projectPlans(current.plans)) !== canonical(projectPlans(baseline.plans)) ||
            (current.plansUpdatedAt || null) !== (baseline.savedAt || null)) return false;
        tx.set(ref, payload, { merge: true });
        return true;
      });
      if (!replaced) {
        if (generation === syncGeneration) { pauseSync(true); setSyncState("changed"); }
        return false;
      }
      if (generation !== syncGeneration) return false;
      confirmedCloud = { plans: plans, savedAt: at };
      if (revision === localRevision) setSyncState("ok", at);
      return true;
    } catch (e) {
      if (generation === syncGeneration) setSyncState("error");
      console.warn("HCG sync upload failed; plans remain on this device.", e);
      return false;
    } finally {
      clearTimeout(warning);
      if (generation === syncGeneration) {
        uploading = false;
        if (revision !== localRevision && syncReady && !syncIsPaused()) scheduleUpload();
      }
    }
  }
  function scheduleUpload() {
    if (uploadTimer) clearTimeout(uploadTimer);
    setSyncState("pending");
    if (uploading) return;
    uploadTimer = setTimeout(function () {
      uploadTimer = null;
      if (user && syncReady && !syncIsPaused()) uploadPlans(localSavedAt());
    }, 1500);
  }

  async function resolveOnSignIn(generation) {
    syncReady = false;
    var cloud = null, cloudAt = null;
    try {
      var snap = await docRef().get({ source: "server" });
      if (generation !== syncGeneration) return;
      if (snap.exists) {
        var data = snap.data() || {};
        cloud = data.plans || null;
        cloudAt = data.plansUpdatedAt || null;
        entitlementCache = normalizeEntitlement(data.entitlement);
      }
    } catch (e) {
      if (generation !== syncGeneration) return;
      // Keep the existing entitlement read path on an offline device without
      // treating a cached plan as confirmation or replacing either copy.
      try {
        var cached = await docRef().get({ source: "cache" });
        if (generation === syncGeneration && cached.exists) entitlementCache = normalizeEntitlement((cached.data() || {}).entitlement);
      } catch (ignored) {}
      if (generation === syncGeneration) setSyncState(syncIsPaused() ? "paused" : "error");
      return;
    }
    confirmedCloud = { plans: projectPlans(cloud), savedAt: cloudAt };
    if (syncIsPaused()) { setSyncState("paused"); return; }

    var local = readLocalPlans(), localAt = localSavedAt();
    var cloudEmpty = !cloud || localIsEmpty(cloud);
    if (cloudEmpty) {
      syncReady = true;
      if (!localIsEmpty(local)) await uploadPlans(localAt);
      else setSyncState("empty");
      return;
    }
    if (localIsEmpty(local)) {
      if (!applyPlansToLocal(cloud, cloudAt)) { setSyncState("device-error"); return; }
      location.reload();
      return;
    }
    if (canonical(local) === canonical(projectPlans(cloud))) {
      syncReady = true;
      setSyncState("ok", cloudAt);
      return;
    }

    // No replacement is possible without a stored snapshot of both copies.
    var backedUp = saveBackup(local, localAt, cloud, cloudAt);
    setSyncState("conflict");
    var choice = await choosePlanCopy(local, localAt, cloud, cloudAt, backedUp);
    if (generation !== syncGeneration) return;
    if (!backedUp || choice === "pause") { pauseSync(true); setSyncState("paused"); return; }
    if (canonical(local) !== canonical(readLocalPlans())) {
      // Another tab changed this browser's plan. Do not resolve an old choice.
      pauseSync(true); setSyncState("paused"); return;
    }
    if (choice === "device") {
      syncReady = true;
      if (!await uploadPlans(localAt, { plans: cloud, savedAt: cloudAt }) && generation === syncGeneration) {
        // A failed conflict upload must not make the next edit overwrite an
        // account copy that we have not matched to the backup on this device.
        if (!syncIsPaused()) pauseSync(true);
      }
    } else {
      if (!applyPlansToLocal(cloud, cloudAt)) { setSyncState("device-error"); return; }
      location.reload();
    }
  }

  function startPlanResolution() {
    if (!user || !db) return;
    var generation = syncGeneration;
    resolving = true;
    setSyncState(syncIsPaused() ? "paused" : "pending");
    resolveOnSignIn(generation).catch(function (e) {
      if (generation === syncGeneration) setSyncState("error");
      console.warn("HCG sync resolution failed:", e);
    }).finally(function () {
      if (generation !== syncGeneration) return;
      resolving = false;
      fireListeners(); // Entitlement is readable now; let download gates re-render.
      continuePendingCheckout();
    });
  }
  function onAuthChanged(u) {
    var previousUid = user && user.uid;
    var nextUid = u && u.uid;
    if (previousUid !== nextUid || !authResolved) {
      syncGeneration++;
      if (uploadTimer) clearTimeout(uploadTimer);
      uploadTimer = null;
      uploading = false;
      resolving = false;
      syncReady = false;
      confirmedCloud = null;
      entitlementCache = { paid: false };
      syncState = { status: "idle", at: null };
    }
    user = u || null;
    authResolved = true;
    if (user && authUi.open) closeAuth(false);
    renderControl();
    fireListeners();
    if (user && previousUid !== nextUid) startPlanResolution();
    else window.dispatchEvent(new CustomEvent("hcgplansync"));
  }
  function fireListeners() {
    listeners.slice().forEach(function (cb) {
      try { cb(user); } catch (e) { console.warn("HCGAuth listener error:", e); }
    });
  }

  // ---------------- public API ----------------
  var HCGAuth = {
    currentUser: function () { return user; },
    isResolved: function () { return authResolved; },
    plannerSaveStatus: syncLabel,
    openPlannerBackups: openPlannerBackups,
    entitlement: function () { return HCGEntitlement.current(); },
    isAdmin: function () { return isAdminUser(); },
    firestore: async function () { await ensureFirebase(); return db; },
    onChange: function (cb) {
      if (typeof cb === "function") {
        listeners.push(cb);
        if (authResolved) { try { cb(user); } catch (e) {} }
      }
      return function () {
        var i = listeners.indexOf(cb);
        if (i !== -1) listeners.splice(i, 1);
      };
    },
    startCheckout: async function (interval) {
      await ensureFirebase();
      if (!user) throw new Error("Sign in to subscribe");
      if (!fns) throw new Error("Payments unavailable");
      var res = await fns.httpsCallable("createHcgCheckout")({ interval: interval === "year" ? "year" : "month" });
      if (!res || !res.data || !res.data.url) throw new Error("Checkout did not return a URL");
      if (window.HCGStats) window.HCGStats.log("checkout");
      return res.data.url;
    },
    signIn: function (options) { return openAuth(options); },
    openAuth: function (options) { return openAuth(options); },
    signInWithGoogle: function () { return signInWithGoogle(); },
    signOut: async function () {
      try {
        await ensureFirebase();
        if (auth) await auth.signOut();
      } catch (e) { console.warn("HCG sign-out failed:", e); }
    }
  };
  window.HCGAuth = HCGAuth;

  // ---------------- boot ----------------
  function boot() {
    renderControl(); // immediate device-only control; updates when auth resolves
    var saveLine = $("save-note") || $("saved-note");
    if (saveLine) {
      saveLine.setAttribute("aria-live", "polite");
      var backups = document.createElement("button");
      backups.type = "button";
      backups.className = "mini";
      backups.textContent = "Planner backups";
      backups.addEventListener("click", openPlannerBackups);
      saveLine.insertAdjacentElement("afterend", backups);
    }
    ensureFirebase().catch(function () { /* already logged; site stays device-only */ });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
