// Humanities Curriculum Group — accounts, cloud plan sync, entitlement.
//
// Phase 1 (Oct 2026): teachers can sign in with Google. Their planner data
// (the same localStorage keys the planners already use) is mirrored to
// Firestore at hcgUsers/{uid} so it follows them across devices. Everything
// fails soft: if Firebase or Firestore is unreachable, the site behaves
// exactly as it did before accounts existed, and plans stay on the device.
//
// Sync model:
//  - On sign-in we read hcgUsers/{uid}. If the account has no plans yet, the
//    plans on this device are uploaded. If the device has no plans and the
//    account does, the account plans are applied here and the page reloads
//    once so the planners boot from them. If both have plans and they
//    differ, confirm() asks which copy to keep, describing each by its
//    saved date.
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
  var ADMIN_EMAILS = ["alexbrouhard1@gmail.com", "alexbrouhardedu@gmail.com", "knowethcg@gmail.com"];

  var user = null;               // firebase.User or null
  var authResolved = false;      // onAuthStateChanged has fired at least once
  var listeners = [];
  var entitlementCache = { paid: false };
  var syncState = { status: "idle", at: null }; // idle | ok | error
  var syncReady = false;         // true after the sign-in resolution finishes
  var applyingCloud = false;     // true while we write cloud plans locally
  var uploadTimer = null;
  var sdkPromise = null;
  var auth = null, db = null, st = null, fns = null;

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
    applyingCloud = true;
    try {
      PLAN_KEYS.forEach(function (k) {
        if (plans[k] == null) rawRemoveItem(k);
        else rawSetItem(k, JSON.stringify(plans[k]));
      });
      stampLocal(savedAt);
    } catch (e) { console.warn("HCG sync: could not apply account plans locally.", e); }
    applyingCloud = false;
  }

  // Watch plan writes: stamp the local saved-date always; upload while signed in.
  localStorage.setItem = function (key, value) {
    rawSetItem(key, value);
    if (PLAN_KEYS.indexOf(key) !== -1 && !applyingCloud) {
      stampLocal(new Date().toISOString());
      if (user && syncReady) scheduleUpload();
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
    if (!user) return "";
    if (syncState.status === "ok") return "Synced " + (syncState.at ? fmtDate(syncState.at) : "just now");
    if (syncState.status === "error") return "Saved on this device only";
    return "Syncing…";
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
          "<a href='home.html'>My Home</a>" +
          "<a href='subscribe.html'>Subscribe</a>" +
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

  // ---------------- cloud sync ----------------
  function docRef() { return db.collection("hcgUsers").doc(user.uid); }

  async function uploadPlans(savedAtIso) {
    if (!user || !db) return false;
    var plans = readLocalPlans();
    var at = savedAtIso || new Date().toISOString();
    try {
      await docRef().set({
        email: user.email || null,
        displayName: user.displayName || null,
        plans: plans,
        plansUpdatedAt: at
      }, { merge: true });
      syncState = { status: "ok", at: at };
      updateSyncLine();
      return true;
    } catch (e) {
      console.warn("HCG sync upload failed; plans remain on this device.", e);
      syncState = { status: "error", at: null };
      updateSyncLine();
      return false;
    }
  }
  function scheduleUpload() {
    if (uploadTimer) clearTimeout(uploadTimer);
    uploadTimer = setTimeout(function () {
      uploadTimer = null;
      if (user && syncReady) uploadPlans(localSavedAt());
    }, 1500);
  }

  async function resolveOnSignIn() {
    syncReady = false;
    var local = readLocalPlans();
    var cloud = null, cloudAt = null;
    try {
      var snap = await docRef().get();
      if (snap.exists) {
        var data = snap.data() || {};
        cloud = data.plans || null;
        cloudAt = data.plansUpdatedAt || null;
        entitlementCache = normalizeEntitlement(data.entitlement);
      }
    } catch (e) {
      console.warn("HCG sync: could not read account plans; staying device-only for this session.", e);
      syncState = { status: "error", at: null };
      updateSyncLine();
      return; // syncReady stays false: no uploads over unread cloud state
    }

    var cloudEmpty = !cloud || PLAN_KEYS.every(function (k) { return cloud[k] == null; });

    if (cloudEmpty) {
      // First sign-in (or empty account): push this device's plans up.
      if (!localIsEmpty(local)) await uploadPlans(localSavedAt() || new Date().toISOString());
      else { syncState = { status: "ok", at: new Date().toISOString() }; updateSyncLine(); }
      syncReady = true;
      return;
    }
    if (localIsEmpty(local)) {
      // Nothing on this device to lose: take the account plans and reboot.
      applyPlansToLocal(cloud, cloudAt);
      syncReady = true;
      location.reload();
      return;
    }
    var cloudSet = {};
    PLAN_KEYS.forEach(function (k) { cloudSet[k] = cloud[k] != null ? cloud[k] : null; });
    if (canonical(local) === canonical(cloudSet)) {
      syncState = { status: "ok", at: cloudAt || new Date().toISOString() };
      updateSyncLine();
      syncReady = true;
      return;
    }
    // Both sides have plans and they differ: the teacher chooses.
    var keepLocal = window.confirm(
      "Your plans on this device differ from the plans saved to your account.\n\n" +
      "On this device: saved " + fmtDate(localSavedAt()) + ".\n" +
      "In your account: saved " + fmtDate(cloudAt) + ".\n\n" +
      "OK: keep the plans on THIS DEVICE and replace the account copy.\n" +
      "Cancel: use the ACCOUNT plans and replace this device's copy."
    );
    if (keepLocal) {
      await uploadPlans(localSavedAt() || new Date().toISOString());
      syncReady = true;
    } else {
      applyPlansToLocal(cloud, cloudAt);
      syncReady = true;
      location.reload();
    }
  }

  function onAuthChanged(u) {
    var wasSignedIn = !!user;
    user = u || null;
    authResolved = true;
    renderControl();
    fireListeners();
    if (user && !wasSignedIn) {
      resolveOnSignIn()
        .then(function () { fireListeners(); }) // entitlement is readable now; let gates re-render
        .catch(function (e) { console.warn("HCG sync resolution failed:", e); });
    }
    if (!user) {
      syncReady = false;
      entitlementCache = { paid: false };
      syncState = { status: "idle", at: null };
    }
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
    entitlement: function () { return HCGEntitlement.current(); },
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
      return res.data.url;
    },
    signIn: async function () {
      try {
        await ensureFirebase();
        if (!auth) throw new Error("Auth unavailable");
        if (user) return;
        var provider = new firebase.auth.GoogleAuthProvider();
        provider.setCustomParameters({ prompt: "select_account" });
        try {
          await auth.signInWithPopup(provider);
        } catch (popupErr) {
          console.warn("HCG popup sign-in failed; falling back to redirect.", popupErr && popupErr.code, popupErr);
          await auth.signInWithRedirect(provider);
        }
      } catch (e) {
        console.warn("HCG sign-in failed:", e);
        window.alert("Sign-in could not start (" + ((e && (e.code || e.message)) || "unknown error") + "). Check your connection and try again. Your plans are still saved on this device.");
      }
    },
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
    ensureFirebase().catch(function () { /* already logged; site stays device-only */ });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
