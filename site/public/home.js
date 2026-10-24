// Humanities Curriculum Group — homepage motion.
//
// Two small animations, both renderings of the product as built:
//   1. The hero crossfades between the real unit covers.
//   2. The planner illustration drops lesson picks into a school week
//      while the coverage count fills to 15 of 15, then loops.
// The HTML already carries the finished, static frames. If the visitor
// prefers reduced motion, nothing here runs and those frames stand.
// Both animations pause while their section is off-screen.
(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Run fn(true)/fn(false) as el enters/leaves the viewport.
  function whenVisible(el, fn) {
    if (!("IntersectionObserver" in window)) { fn(true); return; }
    var state = false;
    var io = new IntersectionObserver(function (entries) {
      var vis = entries[0].isIntersecting;
      if (vis !== state) { state = vis; fn(vis); }
    }, { threshold: 0.2 });
    io.observe(el);
  }

  /* ---------------- Hero cover rotation ---------------- */
  (function heroCovers() {
    var fig = document.getElementById("hero-covers");
    if (!fig) return;
    var slides = Array.prototype.slice.call(fig.querySelectorAll(".hc-slide"));
    var nameEl = document.getElementById("hc-cap-name");
    var noteEl = document.getElementById("hc-cap-note");
    if (slides.length < 2 || reduceMotion) return;

    var idx = 0;
    var timer = null;

    function ensureSrc(i) {
      var img = slides[i];
      if (img && !img.getAttribute("src") && img.getAttribute("data-src")) {
        img.setAttribute("src", img.getAttribute("data-src"));
      }
    }
    function show(i) {
      slides[idx].classList.remove("is-active");
      idx = i;
      slides[idx].classList.add("is-active");
      if (nameEl) nameEl.textContent = slides[idx].getAttribute("data-name") || "";
      if (noteEl) noteEl.textContent = slides[idx].getAttribute("data-note") || "";
      ensureSrc((idx + 1) % slides.length); // stay one cover ahead
    }
    function tick() {
      if (document.hidden) return;
      show((idx + 1) % slides.length);
    }
    function start() {
      if (timer) return;
      ensureSrc(1);
      timer = window.setInterval(tick, 5200);
    }
    function stop() {
      if (timer) { window.clearInterval(timer); timer = null; }
    }
    function resume() {
      var r = fig.getBoundingClientRect();
      if (r.bottom > 0 && r.top < window.innerHeight) start();
    }
    fig.addEventListener("mouseenter", stop);
    fig.addEventListener("mouseleave", resume);
    fig.addEventListener("focusin", stop);
    fig.addEventListener("focusout", resume);
    whenVisible(fig, function (vis) { if (vis) start(); else stop(); });
  })();

  /* ---------------- Scroll reveal ---------------- */
  (function scrollReveal() {
    var els = Array.prototype.slice.call(document.querySelectorAll(".rv"));
    if (!els.length) return;
    if (reduceMotion || !("IntersectionObserver" in window)) {
      els.forEach(function (el) { el.classList.add("in"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.1, rootMargin: "0px 0px -6% 0px" });
    els.forEach(function (el) { io.observe(el); });
  })();
})();

  // ---- planner showcase: rotating spotlight with click-to-enlarge ----
  (function plannerShowcase() {
    var stage = document.querySelector(".sc-stage");
    if (!stage) return;
    document.documentElement.classList.add("sc-on");
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var slides = Array.prototype.slice.call(stage.querySelectorAll(".sc-slide"));
    var caps = Array.prototype.slice.call(document.querySelectorAll(".sc-cap"));
    var btns = Array.prototype.slice.call(document.querySelectorAll(".sc-btn"));
    var cur = 0, timer = null, userDrove = false;
    function go(n) {
      cur = (n + slides.length) % slides.length;
      slides.forEach(function (el, i) { el.classList.toggle("is-active", i === cur); });
      caps.forEach(function (el, i) { el.classList.toggle("is-active", i === cur); });
      btns.forEach(function (el, i) { el.classList.toggle("is-active", i === cur); });
    }
    function start() {
      if (reduce || userDrove || timer) return;
      timer = window.setInterval(function () { go(cur + 1); }, 6000);
    }
    function stop() { if (timer) { window.clearInterval(timer); timer = null; } }
    btns.forEach(function (btn, i) {
      btn.addEventListener("click", function () { userDrove = true; stop(); go(i); });
    });
    var lb = document.getElementById("scLightbox");
    var lbImg = lb ? lb.querySelector("img") : null;
    slides.forEach(function (slide) {
      var frame = slide.querySelector(".sc-frame");
      if (!frame || !lb) return;
      frame.addEventListener("click", function () {
        var img = slide.querySelector("img");
        lbImg.src = img.currentSrc || img.src;
        lbImg.alt = img.alt;
        lb.hidden = false;
        document.body.style.overflow = "hidden";
      });
    });
    if (lb) {
      function closeLb() { lb.hidden = true; document.body.style.overflow = ""; }
      lb.addEventListener("click", closeLb);
      document.addEventListener("keydown", function (ev) { if (ev.key === "Escape" && !lb.hidden) closeLb(); });
    }
    start();
  })();
