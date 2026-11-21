// First-party, aggregate-only site stats for Humanities Curriculum Group.
// Sends small counters (page views, downloads, checkout starts, signups) to
// our own logEvent function, which adds them to daily totals in our own
// database. No cookies, no identifiers, no third parties, nothing about
// individual visitors. Runs only on the production host, so local test
// runs and previews stay silent. See the Privacy Policy.
(function () {
  if (window.HCGStats) return;
  var ENDPOINT = "https://logevent-yh5summz4a-uc.a.run.app/";
  if (location.hostname !== "humanitiescurriculumgroup.web.app") return;

  function pageKey() {
    var p = location.pathname.replace(/^\/+/, "").replace(/\.html$/, "");
    return p === "" ? "home" : p.split("/")[0];
  }
  function sourceBucket() {
    var r = document.referrer;
    if (!r) return "direct";
    var h;
    try { h = new URL(r).hostname; } catch (e) { return "direct"; }
    if (h === location.hostname) return null; // internal move: not an arrival
    if (/(^|\.)google\./.test(h)) return "google";
    if (h.indexOf("facebook.com") !== -1) return "facebook";
    if (h.indexOf("teacherspayteachers.com") !== -1) return "tpt";
    if (h.indexOf("bing.com") !== -1) return "bing";
    if (h.indexOf("duckduckgo.com") !== -1) return "duckduckgo";
    return h.replace(/[^a-z0-9.-]/gi, "").slice(0, 40) || "other";
  }
  function send(payload) {
    try {
      var body = JSON.stringify(payload);
      if (navigator.sendBeacon) {
        navigator.sendBeacon(ENDPOINT, body);
      } else if (window.fetch) {
        fetch(ENDPOINT, { method: "POST", body: body, keepalive: true, headers: { "Content-Type": "text/plain" } }).catch(function () {});
      }
    } catch (e) { /* stats must never break the page */ }
  }

  var key = pageKey();
  var view = { e: "view", p: key };
  var src = sourceBucket();
  if (src) view.s = src;
  send(view);

  document.addEventListener("click", function (ev) {
    var t = ev.target && ev.target.closest ? ev.target.closest("a[href], [data-file]") : null;
    if (!t || !t.getAttribute) return;
    var isFile = t.hasAttribute && t.hasAttribute("data-file");
    var href = t.getAttribute("href") || "";
    if (!isFile && !/(^|\/)files(-units)?\//.test(href) && !/\.(pdf|pptx)(\?|$)/i.test(href)) return;
    send({ e: "download", p: key });
  }, true);

  window.HCGStats = {
    log: function (event) { send({ e: event, p: key }); }
  };
})();
