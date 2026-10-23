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

  /* ---------------- Planner sequence ---------------- */
  (function plannerSequence() {
    var box = document.getElementById("panim");
    if (!box || reduceMotion) return;
    var chips = Array.prototype.slice.call(box.querySelectorAll(".pick-chip"));
    var bar = document.getElementById("panim-bar");
    var count = document.getElementById("panim-count");
    var note = document.getElementById("panim-note");
    // Coverage after each pick lands, ending where the real planner's
    // fresh core plan ends: 15 of 15 blueprint entries.
    var steps = [6, 10, 13, 15];
    var timers = [];
    var running = false;

    function later(fn, ms) { timers.push(window.setTimeout(fn, ms)); }
    function clearTimers() {
      timers.forEach(function (t) { window.clearTimeout(t); });
      timers = [];
    }
    function setCoverage(n) {
      if (bar) bar.style.width = (n / 15 * 100) + "%";
      if (count) count.textContent = n + " of 15";
    }
    function reset() {
      chips.forEach(function (c) { c.classList.remove("in"); });
      setCoverage(0);
      if (note) note.textContent = "Picks land on real school days. The test is already waiting at the end of the unit.";
    }
    function play() {
      clearTimers();
      reset();
      chips.forEach(function (chip, i) {
        later(function () {
          chip.classList.add("in");
          setCoverage(steps[i]);
          if (i === chips.length - 1 && note) {
            note.textContent = "Every blueprint entry covered, before the test arrives.";
          }
        }, 700 + i * 950);
      });
      later(play, 700 + chips.length * 950 + 3000); // hold the finished week, then loop
    }
    function start() {
      if (running) return;
      running = true;
      play();
    }
    function stop() {
      running = false;
      clearTimers();
    }
    box.classList.add("live");
    reset();
    whenVisible(box, function (vis) { if (vis) start(); else stop(); });
  })();
})();
