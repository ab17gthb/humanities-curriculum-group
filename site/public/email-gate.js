// Email gate for the free Progressive Era sample unit downloads.
//
// The free unit stays free. The first time a visitor on this browser clicks
// a file link on the sample unit page, a small dialog asks for an email
// address. The address is saved once to the hcgLeads collection in
// Firestore, which is the start of the site's own email list. After that,
// every download on the page runs without asking again on this browser.
// Teachers who are signed in are never asked, because the site already has
// their email address with their account.
//
// The files themselves stay at their normal public addresses. This gate is
// the honest front door, not a paywall, and the Privacy Policy says so.
(function () {
  if (window.HCGEmailGate) return;

  var STORAGE_KEY = "hcg_email_gate_v1";
  var SOURCE = "progressive-era";
  var pendingHref = null;
  var pendingFile = "";
  var built = false;
  var busy = false;

  function $(id) { return document.getElementById(id); }

  function storedEmail() {
    try {
      var v = window.localStorage.getItem(STORAGE_KEY);
      return v && /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v) ? v : "";
    } catch (e) { return ""; }
  }

  function signedInEmail() {
    try {
      var u = window.HCGAuth && HCGAuth.currentUser ? HCGAuth.currentUser() : null;
      return u && u.email ? String(u.email) : "";
    } catch (e) { return ""; }
  }

  function unlocked() { return !!(storedEmail() || signedInEmail()); }

  function remember(email) {
    try { window.localStorage.setItem(STORAGE_KEY, email); } catch (e) {}
  }

  function loadScript(src) {
    return new Promise(function (resolve, reject) {
      var s = document.createElement("script");
      s.src = src; s.async = true; s.onload = resolve; s.onerror = reject;
      document.head.appendChild(s);
    });
  }

  async function saveLead(email, firstFile) {
    if (!window.firebase) {
      await loadScript("/vendor/firebase/firebase-app-compat.js");
      await loadScript("/vendor/firebase/firebase-firestore-compat.js");
    }
    if (!firebase.apps.length) firebase.initializeApp(window.HCG_FIREBASE_CONFIG);
    await firebase.firestore().collection("hcgLeads").add({
      email: email,
      source: SOURCE,
      firstFile: firstFile || "",
      createdAt: firebase.firestore.FieldValue.serverTimestamp()
    });
  }

  function ensureStyles() {
    if ($("hcg-gate-style")) return;
    var style = document.createElement("style");
    style.id = "hcg-gate-style";
    style.textContent =
      ".hcg-gate-overlay[hidden]{display:none!important}" +
      ".hcg-gate-overlay{position:fixed;inset:0;z-index:1000;background:rgba(23,32,48,.64);display:flex;align-items:center;justify-content:center;overflow-y:auto;padding:24px 16px;font-family:Arial,sans-serif}" +
      ".hcg-gate-panel{position:relative;background:#fff;color:#26313f;width:440px;max-width:100%;max-height:calc(100vh - 48px);overflow-y:auto;border-radius:8px;padding:28px;box-shadow:0 24px 70px rgba(0,0,0,.35)}" +
      ".hcg-gate-panel h2{font-family:Georgia,'Times New Roman',serif;font-weight:normal;font-size:27px;color:var(--navy);margin:0 38px 8px 0}" +
      ".hcg-gate-context{font-size:15.5px;line-height:1.45;color:#4b5563;margin:0 0 20px}" +
      ".hcg-gate-close{position:absolute;top:10px;right:12px;background:none;border:none;color:#5f6873;font-size:30px;line-height:1;padding:6px;cursor:pointer}" +
      ".hcg-gate-close:hover{color:var(--navy)}" +
      ".hcg-gate-field{display:block;font-size:14px;font-weight:bold;color:#374151;margin:0 0 14px}" +
      ".hcg-gate-field input{display:block;width:100%;box-sizing:border-box;margin-top:6px;border:1px solid #b9c0c9;border-radius:5px;padding:11px 12px;font:inherit;font-size:16px;font-weight:normal;color:#26313f;background:#fff}" +
      ".hcg-gate-field input:focus{outline:2px solid rgba(48,86,140,.3);border-color:var(--navy)}" +
      ".hcg-gate-error{background:#fdf0ec;border-left:3px solid #b5442c;color:#7c2d1d;padding:10px 12px;font-size:14.5px;line-height:1.4;margin:0 0 14px}" +
      ".hcg-gate-error[hidden]{display:none!important}" +
      ".hcg-gate-submit{width:100%;background:var(--rust);color:#fff;border:none;border-radius:5px;padding:12px 14px;font:inherit;font-size:16px;font-weight:bold;cursor:pointer}" +
      ".hcg-gate-submit:hover{background:#9d4f2d}" +
      ".hcg-gate-cancel{display:block;margin:8px auto 0;background:none;border:none;color:#68707a;font:inherit;font-size:14.5px;cursor:pointer;padding:4px}" +
      ".hcg-gate-note{font-size:13px;line-height:1.45;color:#6b7280;margin:18px 0 0;text-align:center}" +
      ".hcg-gate-hp{position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden}" +
      ".hcg-gate-panel button:disabled,.hcg-gate-panel input:disabled{opacity:.58;cursor:wait}" +
      "@media(max-width:520px){.hcg-gate-overlay{padding:14px 10px}.hcg-gate-panel{padding:24px 20px;max-height:calc(100vh - 28px)}}";
    document.head.appendChild(style);
  }

  function ensureUi() {
    if (built) return;
    ensureStyles();
    var overlay = document.createElement("div");
    overlay.id = "hcg-gate-overlay";
    overlay.className = "hcg-gate-overlay";
    overlay.hidden = true;
    overlay.innerHTML =
      "<div class='hcg-gate-panel' role='dialog' aria-modal='true' aria-labelledby='hcg-gate-title'>" +
        "<button type='button' class='hcg-gate-close' id='hcg-gate-close' aria-label='Close'>&times;</button>" +
        "<h2 id='hcg-gate-title'>Get the free unit</h2>" +
        "<p class='hcg-gate-context'>Enter your email address and your download starts right away. The address joins our list for new units and free resources, and entering it once unlocks every file in this unit on this browser.</p>" +
        "<form id='hcg-gate-form' novalidate>" +
          "<label class='hcg-gate-field'>Email address" +
            "<input type='email' id='hcg-gate-email' autocomplete='email' maxlength='200' required></label>" +
          "<div class='hcg-gate-hp' aria-hidden='true'><label>Leave this blank<input type='text' id='hcg-gate-website' tabindex='-1' autocomplete='off'></label></div>" +
          "<p class='hcg-gate-error' id='hcg-gate-error' role='alert' hidden></p>" +
          "<button type='submit' class='hcg-gate-submit' id='hcg-gate-submit'>Download the file</button>" +
        "</form>" +
        "<button type='button' class='hcg-gate-cancel' id='hcg-gate-cancel'>Not now</button>" +
        "<p class='hcg-gate-note'>Already have an account? Sign in at the top of the page and the downloads open without this step. We never sell email addresses. The Privacy Policy linked in the footer covers this list.</p>" +
      "</div>";
    document.body.appendChild(overlay);
    built = true;

    $("hcg-gate-close").addEventListener("click", closeGate);
    $("hcg-gate-cancel").addEventListener("click", closeGate);
    overlay.addEventListener("click", function (ev) { if (ev.target === overlay) closeGate(); });
    document.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape" && !$("hcg-gate-overlay").hidden) closeGate();
    });
    $("hcg-gate-form").addEventListener("submit", submitGate);
  }

  function openGate(href, file) {
    pendingHref = href;
    pendingFile = file || "";
    ensureUi();
    var overlay = $("hcg-gate-overlay");
    overlay.hidden = false;
    if (document.body) document.body.style.overflow = "hidden";
    var input = $("hcg-gate-email");
    if (input) setTimeout(function () { input.focus(); }, 0);
  }

  function closeGate() {
    var overlay = $("hcg-gate-overlay");
    if (overlay) overlay.hidden = true;
    if (document.body) document.body.style.overflow = "";
    pendingHref = null;
    pendingFile = "";
  }

  function startDownload(href) {
    var a = document.createElement("a");
    a.href = href;
    document.body.appendChild(a);
    a.click();
    a.remove();
  }

  function gateError(text) {
    var el = $("hcg-gate-error");
    if (el) { el.hidden = !text; el.textContent = text || ""; }
  }

  function setBusy(on) {
    busy = !!on;
    var submit = $("hcg-gate-submit");
    if (submit) {
      submit.disabled = busy;
      submit.textContent = busy ? "Please wait…" : "Download the file";
    }
    var input = $("hcg-gate-email");
    if (input) input.disabled = busy;
  }

  async function submitGate(ev) {
    ev.preventDefault();
    if (busy) return;
    var email = ($("hcg-gate-email").value || "").trim().toLowerCase();
    // Honeypot filled means a bot. Pretend it worked, save nothing.
    if ($("hcg-gate-website").value) {
      remember(email || "teacher@example.com");
      var href = pendingHref;
      closeGate();
      if (href) startDownload(href);
      return;
    }
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) {
      gateError("That email address doesn't look complete. Check it and try again.");
      return;
    }
    gateError("");
    setBusy(true);
    try {
      // The Firestore write can hang on a blocked connection instead of
      // failing, so race it against a timeout and let the teacher retry
      // rather than sit on a spinner.
      await Promise.race([
        saveLead(email, pendingFile),
        new Promise(function (resolve, reject) {
          setTimeout(function () { reject(new Error("timeout")); }, 20000);
        })
      ]);
    } catch (e) {
      setBusy(false);
      gateError("Your email address could not be saved just now. Check your connection and try again.");
      return;
    }
    setBusy(false);
    remember(email);
    var href = pendingHref;
    closeGate();
    if (href) startDownload(href);
  }

  document.addEventListener("click", function (ev) {
    var t = ev.target && ev.target.closest ? ev.target.closest("a[href]") : null;
    if (!t) return;
    var href = t.getAttribute("href") || "";
    if (!/(^|\/)files\//.test(href)) return;
    if (!/\.(pdf|pptx)(\?|$)/i.test(href)) return;
    if (unlocked()) return;
    ev.preventDefault();
    openGate(t.href, href.split("/").pop());
  }, true);

  window.HCGEmailGate = {
    unlocked: unlocked,
    storedEmail: storedEmail
  };
})();
