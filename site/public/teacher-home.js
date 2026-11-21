// Humanities Curriculum Group — the My Day engine, shared.
// Computes, from the teacher's own saved plans, what lands on any date
// (unit layouts, test days, days off, homework) and renders a day's
// materials with the site's link rules: public links for the free sample,
// per-click Storage downloads for All-Access files on entitled accounts,
// plain filenames for everyone else. Loaded by home.html (the My Day page). Plans are read from localStorage exactly
// as the planners save them; nothing here talks to the network.
(function () {
  "use strict";

  // ---------- date helpers (same conventions as the planners) ----------
  function P(iso) {
    if (typeof iso !== "string" || !/^\d{4}-\d{2}-\d{2}$/.test(iso)) return new Date(NaN);
    var p = iso.split("-"), date = new Date(0);
    date.setFullYear(+p[0], +p[1] - 1, +p[2]);
    date.setHours(0, 0, 0, 0);
    return ISO(date) === iso ? date : new Date(NaN);
  }
  function ISO(d) {
    function z(n) { return (n < 10 ? "0" : "") + n; }
    return String(d.getFullYear()).padStart(4, "0") + "-" + z(d.getMonth() + 1) + "-" + z(d.getDate());
  }
  function fmtLong(iso) { return P(iso).toLocaleDateString("en-US", { weekday: "long", month: "long", day: "numeric" }); }
  function fmtShort(iso) { return P(iso).toLocaleDateString("en-US", { weekday: "short", month: "short", day: "numeric" }); }
  function addDays(iso, n) { var d = P(iso); d.setDate(d.getDate() + n); return ISO(d); }
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function load(key) {
    try { return JSON.parse(localStorage.getItem(key)); } catch (e) { return null; }
  }

  function paidAccess() {
    try { return !!(window.HCGAuth && window.HCGAuth.entitlement && window.HCGAuth.entitlement().paid); }
    catch (e) { return false; }
  }

  function buildView() {
    var yearPlan = load("hcg_year_v1");
    var unitDefs = window.HCG_UNITS || {};
    var yearUnitMap = { u1:"ca", u2:"fd", u3:"er", u4:"jr", u5:"sc", u6:"rc", u7:"ga",
      pe:"pe", wwi:"wwi", u9:"tw", u10:"dp", u11:"ww2", u12:"cw", u13:"cr", u14:"ma",
      u15:"rv", u16:"re", u17:"rm" };
    var savedUnits = {};
    Object.keys(unitDefs).forEach(function (id) { savedUnits[id] = load(unitDefs[id].key); });
    function yearUnitDays(id, fallback) {
      var override = yearPlan.unitDays && yearPlan.unitDays[id];
      var plan = savedUnits[yearUnitMap[id]];
      var value = override != null ? override : plan && plan.totalDays || fallback;
      return typeof value === "number" && Number.isFinite(value) && value > 0 ? value : fallback;
    }

    // ======================================================================
    // Year plan: which unit band covers a date.
    // Compact copy of the assignment math in year-planner.js: instructional
    // days are Mon-Fri inside [start, end] minus days off; the plan's class
    // schedule turns those into meeting days (every day, or every other day
    // on an A/B rotation, anchored on the first instructional day) and the
    // unit lengths, stated in lesson-days, into meeting counts at
    // ceil(lesson-days / lessons-per-meeting); pinned starts and exam
    // review reserves are honored the same way.
    // ======================================================================
    var UNITS = [
      { id: "u1", name: "Colonial America", days: 18 }, { id: "u2", name: "The Founding", days: 18 },
      { id: "u3", name: "Early Republic and Expansion", days: 18 }, { id: "u4", name: "Jackson and Reform", days: 18 },
      { id: "u5", name: "Sectional Crisis and Civil War", days: 18 }, { id: "u6", name: "Reconstruction", days: 18 },
      { id: "u7", name: "The Gilded Age", days: 18 }, { id: "pe", name: "The Progressive Era", days: 18 },
      { id: "wwi", name: "Imperialism and World War I", days: 18 },
      { id: "u9", name: "The Twenties", days: 18 }, { id: "u10", name: "Depression and New Deal", days: 18 },
      { id: "u11", name: "World War II", days: 18 }, { id: "u12", name: "The Cold War", days: 18 },
      { id: "u13", name: "Civil Rights", days: 18 }, { id: "u14", name: "Modern America", days: 18 },
      { id: "u15", name: "Course Review", days: 10 }, { id: "u16", name: "Early Course Review", days: 5 },
      { id: "u17", name: "Modern Course Review", days: 7 }
    ];
    var COURSES = {
      full: ["u1", "u2", "u3", "u4", "u5", "u6", "u7", "pe", "wwi", "u9", "u10", "u11", "u12", "u13", "u14", "u15"],
      early: ["u1", "u2", "u3", "u4", "u5", "u6", "u16"],
      modern: ["u7", "pe", "wwi", "u9", "u10", "u11", "u12", "u13", "u14", "u17"]
    };

    var yearOff = {};   // iso -> label, from the year plan's days off
    var yearByDate = {}; // iso -> { id, name }
    var yearTestByUnit = {}; // unit id -> last iso only if the whole unit fits
    var yearReserved = {};  // iso -> true (exam review)
    if (yearPlan && typeof yearPlan.start === "string" && typeof yearPlan.end === "string") {
      var off = Array.isArray(yearPlan.daysOff) ? yearPlan.daysOff.slice(0, 300) : [];
      var days = [], d0 = P(yearPlan.start), dEnd = P(yearPlan.end);
      // Walk the saved year, not the full extent of each off-date range.
      // Check ranges in the same order as the year planner when they overlap.
      var nDates = 0;
      while (d0 <= dEnd && nDates++ < 732) {
        var dow = d0.getDay(), iso = ISO(d0);
        var entry = off.find(function (o) { return o && iso >= o.from && iso <= o.to; });
        if (entry) yearOff[iso] = entry.label || "day off";
        else if (dow >= 1 && dow <= 5) days.push(iso);
        d0.setDate(d0.getDate() + 1);
      }
      if (yearPlan.exam) {
        var before = days.filter(function (x) { return x < yearPlan.exam; });
        var take = Math.min(yearPlan.reviewDays || 0, before.length);
        for (var i = 0; i < take; i++) yearReserved[before[before.length - 1 - i]] = true;
      }
      var ids = Object.prototype.hasOwnProperty.call(COURSES, yearPlan.course) ? COURSES[yearPlan.course] : COURSES.full;
      if (yearPlan.course === "modern" && ["u1", "u2", "u3", "u4", "u5", "u6"].indexOf(yearPlan.openingUnit) !== -1) {
        ids = [yearPlan.openingUnit].concat(ids);
      }
      var pins = yearPlan.pinnedStarts || {}, idx = 0;
      // Class schedule, normalized the way year-planner.js normSchedule does.
      var schedY = yearPlan.schedule;
      if (!schedY || (schedY.period !== 45 && schedY.period !== 90) ||
          (schedY.pattern !== "daily" && schedY.pattern !== "ab")) {
        schedY = { period: 45, pattern: "daily" };
      }
      var lpmY = schedY.period === 90 ? 2 : 1;
      var meets = schedY.pattern === "ab"
        ? days.filter(function (x, i2) { return i2 % 2 === 0; })
        : days;
      // A review unit in the course is itself the held review time (the
      // year planner's rule): shrink the blank reserve by its meetings,
      // un-reserving the days furthest from the exam first.
      (function () {
        var rid = ["u15", "u16", "u17"].filter(function (x) { return ids.indexOf(x) !== -1; })[0];
        if (!rid) return;
        var rdef = UNITS.filter(function (u) { return u.id === rid; })[0];
        var rdays = yearUnitDays(rid, rdef.days);
        var keep = Math.max(0, Object.keys(yearReserved).length - Math.ceil(rdays / lpmY));
        Object.keys(yearReserved).sort().slice(0, Object.keys(yearReserved).length - keep)
          .forEach(function (iso) { delete yearReserved[iso]; });
      })();
      UNITS.filter(function (u) { return ids.indexOf(u.id) !== -1; }).forEach(function (u) {
        var lessonDays = yearUnitDays(u.id, u.days);
        var need = Math.ceil(lessonDays / lpmY);
        var pin = pins[u.id];
        if (pin) {
          if (!(idx < meets.length && meets[idx] > pin)) {
            while (idx < meets.length && meets[idx] < pin) idx++;
          }
        }
        var got = [];
        while (need > 0 && idx < meets.length) {
          var dd = meets[idx++];
          if (yearReserved[dd]) continue;
          got.push(dd);
          yearByDate[dd] = u;
          need--;
        }
        if (!need && got.length) yearTestByUnit[u.id] = got[got.length - 1];
      });
    }

    // ======================================================================
    // Unit plans: which lesson items land on a date, for each plannable
    // unit (the Progressive Era, the Gilded Age, and Imperialism and
    // World War I).
    // Uses the shared unit scheduler for each plan's ACTIVE
    // section: candidate days are weekdays from the section start to the
    // day before its test, minus year-plan days off; each meeting date has
    // a capacity in lesson-days set by the section's period (1 for a
    // 45-minute period, about 2 for a 90-minute block), and entries pack
    // onto meeting dates in order around pins, day types, and A/B
    // rotation exactly as the planner lays them out. The test sits on its
    // own date after the last meeting.
    // ======================================================================
    function buildUnitLayout(plan, def) {
      // One unit plan laid out on dates: def carries the unit's name, its
      // plate items, and how its test shows (a public file for the free
      // sample; a plain filename for All-Access units, never a public URL).
      if (!plan || !plan.selected || !window.HCGUnitSchedule) return null;
      var byIdU = Object.create(null);
      var customItems = Array.isArray(plan.customItems) ? plan.customItems.filter(function (c) {
        return c && typeof c.id === "string" && typeof c.title === "string" && [0, 0.5, 1, 2].indexOf(c.days) !== -1;
      }) : [];
      def.items.forEach(function (it) { byIdU[it.id] = it; });
      customItems.forEach(function (ci) {
        byIdU[ci.id] = {
          id: ci.id, lesson: 0, custom: true, ck: ci.kind,
          kind: ci.kind === "tpsp" ? "TPSP" : "Your resource",
          name: ci.title, days: ci.days, tags: ci.bp || [], file: "",
          link: ci.link || "", note: ci.note || ""
        };
      });
      var sections = (Array.isArray(plan.sections) && plan.sections.length) ? plan.sections : [plan];
      var sec = sections[Math.max(0, Math.min(Number.isInteger(plan.active) ? plan.active : 0, sections.length - 1))];
      if (!sec || typeof sec.start !== "string" || typeof sec.test !== "string") return null;
      var dc = P(sec.start), testD = P(sec.test), maxEnd = P(sec.start);
      maxEnd.setDate(maxEnd.getDate() + 366);
      if (ISO(dc) !== sec.start || ISO(testD) !== sec.test || testD <= dc || testD > maxEnd) return null;
      var out = {
        id: def.id, name: def.name, shortName: def.shortName, testHref: def.testFile,
        testName: def.testName, testStorage: def.testStorage, unitPage: def.unitPage,
        sectionName: sec.name || "Period 1", testIso: sec.test, homework: sec.homework || {},
        span: { from: sec.start, to: sec.test }, byDate: {}, dayKind: {}, noMeet: {}
      };
      var dayTypes = sec.dayTypes || {}, pinsU = sec.pins || {};
      var splits = plan.splits || {};

      // Rebuild the entry order the way planner.js syncOrder does.
      var want = [];
      def.items.forEach(function (it) {
        if (!plan.selected[it.id]) return;
        if (splits[it.id]) { want.push(it.id + "#a"); want.push(it.id + "#b"); }
        else want.push(it.id);
      });
      customItems.forEach(function (ci) {
        if (!plan.selected[ci.id]) return;
        if (splits[ci.id]) { want.push(ci.id + "#a"); want.push(ci.id + "#b"); }
        else want.push(ci.id);
      });
      var order = want.slice();
      if (Array.isArray(plan.order)) {
        var have = {};
        plan.order.forEach(function (k) { have[k] = true; });
        order = plan.order.filter(function (k, i) { return want.indexOf(k) !== -1 && plan.order.indexOf(k) === i; });
        want.forEach(function (k) { if (!have[k]) order.push(k); });
      }
      function entryFor(key) {
        var base = key.replace(/#[ab]$/, ""), it = byIdU[base];
        if (!it) return null;
        var part = /#a$/.test(key) ? 1 : (/#b$/.test(key) ? 2 : 0);
        if (part) return { key: key, item: it, days: it.days / 2, name: it.name + " (part " + part + ")" };
        return { key: key, item: it, days: it.days, name: it.name };
      }

      var cand = [];
      function isSubDay(iso) { return Object.prototype.hasOwnProperty.call(sec.subDays || {}, iso); }
      while (dc < testD) {
        var dowC = dc.getDay(), isoC = ISO(dc);
        if (dowC >= 1 && dowC <= 5 && !yearOff[isoC]) cand.push({ date: new Date(dc), iso: isoC, meet: true });
        dc.setDate(dc.getDate() + 1);
      }
      if (sec.rotation === "ab") cand.forEach(function (c, i2) { c.meet = i2 % 2 === 0; });
      cand.forEach(function (c) {
        if (dayTypes[c.iso]) out.dayKind[c.iso] = dayTypes[c.iso];
        else if (!c.meet) out.noMeet[c.iso] = true;
      });
      Object.keys(dayTypes).forEach(function (isoK) { out.dayKind[isoK] = dayTypes[isoK]; });
      Object.keys(sec.subDays || {}).forEach(function (isoK) { out.dayKind[isoK] = "Sub day"; });
      if (testD.getDay() === 0 || testD.getDay() === 6 || yearOff[sec.test] || dayTypes[sec.test] || isSubDay(sec.test) ||
          (sec.rotation === "ab" && cand.length % 2)) out.testIso = "";

      var cap = sec.period === 90 ? 2 : 1;
      var usable = cand.filter(function (c) { return c.meet && !dayTypes[c.iso] && !isSubDay(c.iso); });
      var allocation = window.HCGUnitSchedule.allocate(usable, order.map(entryFor).filter(Boolean), pinsU, cap);
      allocation.buckets.forEach(function (b) {
        if (!b.entries.length && !b.continuations.length) return;
        out.byDate[b.iso] = b.continuations.map(function (e) {
          return Object.assign({}, e, { name: e.name + " (continued)" });
        }).concat(b.entries);
      });
      return out;
    }

    var layouts = Object.keys(unitDefs).map(function (id) {
      return buildUnitLayout(savedUnits[id], unitDefs[id]);
    }).filter(Boolean);
    var hasYear = !!(yearPlan && typeof yearPlan.start === "string" && typeof yearPlan.end === "string" &&
      Number.isFinite(P(yearPlan.start).getTime()) && Number.isFinite(P(yearPlan.end).getTime()) &&
      ISO(P(yearPlan.start)) === yearPlan.start && ISO(P(yearPlan.end)) === yearPlan.end && yearPlan.start <= yearPlan.end);

    // ======================================================================
    // What a single date shows.
    // ======================================================================
    function dayInfo(iso) {
      var dow = P(iso).getDay();
      if (dow === 0 || dow === 6) return { kind: "noschool", text: "No school (weekend)" };
      if (yearOff[iso]) return { kind: "noschool", text: "No school: " + yearOff[iso] };
      var li, L;
      var tests = [];
      var blocks = [];
      layouts.forEach(function (L2) {
        var entries = L2.byDate[iso];
        var hw = L2.homework[iso];
        if (L2.testIso === iso) tests.push(L2);
        if (entries || (hw && L2.span.from <= iso && iso < L2.span.to)) blocks.push({ layout: L2, entries: entries || [], hw: hw || "" });
      });
      if (blocks.length || tests.length) return { kind: "unit-day", blocks: blocks, tests: tests };
      for (li = 0; li < layouts.length; li++) {
        L = layouts[li];
        if (L.dayKind[iso] && L.span && iso >= L.span.from && iso < L.span.to) {
          return { kind: "noschool", text: "No lesson: " + L.dayKind[iso] + " (from your unit plan)" };
        }
      }
      for (li = 0; li < layouts.length; li++) {
        if (layouts[li].noMeet[iso]) {
          return { kind: "noschool", text: "This section does not meet today (A/B rotation)" };
        }
      }
      if (yearReserved[iso]) return { kind: "other", unit: "Held for exam review" };
      var u = yearByDate[iso];
      if (u) return { kind: "other", unit: u.name, test: yearTestByUnit[u.id] === iso && !layouts.some(function (L2) { return L2.id === yearUnitMap[u.id]; }) };
      if (yearPlan && yearPlan.start && iso >= yearPlan.start && iso <= yearPlan.end) {
        return { kind: "open", text: "Open day: nothing scheduled in your year plan" };
      }
      for (li = 0; li < layouts.length; li++) {
        L = layouts[li];
        if (L.span && iso >= L.span.from && iso <= L.span.to) {
          return { kind: "open", text: L.shortName + " unit plan: nothing laid out for this day" };
        }
      }
      return { kind: "open", text: "Nothing planned for this date" };
    }

    // All-Access files live in Firebase Storage, never at public URLs.
    // Entitled accounts (subscribers and the owner accounts) get a working
    // download link on My Day too, minted per click through HCGFiles
    // exactly as on the unit pages; everyone else keeps the plain filename.
    function storageLink(path, label) {
      return "<button type='button' class='my-day-download' data-storage='" + esc(path) + "'>" + esc(label) + "</button>";
    }
    function gatedName(name) {
      return esc(name) + " <span class='my-day-badge'>All-Access</span>";
    }
    function testBit(L) {
      if (!L.testName) return "Assessment file not listed";
      if (L.testHref) return "<a href='" + esc(L.testHref) + "'>" + esc(L.testName) + "</a>";
      if (L.testStorage) return paidAccess() ? storageLink(L.testStorage, L.testName) : gatedName(L.testName);
      return "Assessment file not listed";
    }

    function safeResourceLink(value) {
      if (typeof value !== "string" || !/^https?:\/\//i.test(value.trim())) return "";
      try {
        var url = new URL(value.trim());
        return url.protocol === "http:" || url.protocol === "https:" ? url.href : "";
      } catch (e) { return ""; }
    }

    function materialsList(entries) {
      if (!entries.length) return "";
      var lis = entries.map(function (e) {
        if (e.item.custom) {
          var label = e.item.ck === "tpsp" ? "TPSP" : "Your resource";
          var url = safeResourceLink(e.item.link);
          var nm = url ? "<a href='" + esc(url) + "'>" + esc(e.name) + "</a>" : esc(e.name);
          return "<li>" + label + ": " + nm + "</li>";
        }
        var f = e.item.file || "";
        var base = f.split("/").pop();
        var st = e.item.storage ? e.item.storage.split("/").pop() : "";
        return "<li>" + esc(e.item.kind) + ": " + esc(e.name) +
          (f ? " · <a href='" + esc(f) + "'>" + esc(base) + "</a>" : (st ? " · " + (paidAccess() ? storageLink(e.item.storage, st) : gatedName(st)) : "")) + "</li>";
      }).join("");
      return "<ul class='materials'>" + lis + "</ul>";
    }
    function unitLabel(L) {
      return esc(L.name) + (L.sectionName ? " <span class='my-day-section'>" + esc(L.sectionName) + "</span>" : "");
    }
    function lessonBit(b) {
      return "<div class='my-day-entry'><p class='unitname'>" + unitLabel(b.layout) + "</p>" + materialsList(b.entries) +
        (b.hw ? "<p class='hwline'>Homework: " + esc(b.hw) + "</p>" : "") + "</div>";
    }
    function assessmentBit(L) {
      return "<div class='my-day-entry'><p class='unitname'>" + unitLabel(L) + "</p>" +
        "<p class='testday'>Unit assessment</p><p>" + testBit(L) + "</p></div>";
    }
    function dateLabel(iso) {
      return "<time datetime='" + esc(iso) + "'>" + esc(fmtLong(iso)) + "</time>";
    }
    function dayHTML(iso, heading) {
      var info = dayInfo(iso);
      var h = "<h2>" + esc(heading) + "</h2><p class='when'>" + dateLabel(iso) + "</p>";
      if (info.kind === "noschool" || info.kind === "open") {
        return h + "<p class='" + (info.kind === "noschool" ? "noschool" : "") + "'>" + esc(info.text) + "</p>";
      }
      if (info.kind === "unit-day") return h + info.tests.map(assessmentBit).join("") + info.blocks.map(lessonBit).join("");
      return h + "<p class='unitname'>" + esc(info.unit) + "</p>" +
        (info.test ? "<p class='testday'>Projected assessment · Year Planner</p>" : "");
    }
    function weekCell(iso) {
      var info = dayInfo(iso);
      if (info.kind === "noschool" || info.kind === "open") return esc(info.text);
      if (info.kind === "unit-day") {
        var tests = info.tests.map(function (L) { return unitLabel(L) + " · Assessment (" + testBit(L) + ")"; });
        var lessons = info.blocks.map(function (b) {
          var names = b.entries.map(function (e) { return esc(e.name); });
          if (b.hw) names.push("Homework: " + esc(b.hw));
          return unitLabel(b.layout) + (names.length ? ": " + names.join("; ") : "");
        });
        return tests.concat(lessons).join("<br>");
      }
      return esc(info.unit) + (info.test ? " · Unit test (projected)" : "");
    }
    function upcomingHTML(today) {
      var dates = new Set();
      layouts.forEach(function (L) {
        Object.keys(L.byDate).forEach(function (iso) { if (iso >= today) dates.add(iso); });
        if (L.testIso && L.testIso >= today) dates.add(L.testIso);
      });
      var nextLesson = null, nextAssessment = null;
      Array.from(dates).sort().some(function (iso) {
        var day = dayInfo(iso);
        if (day.kind !== "unit-day") return false;
        var teaching = day.blocks.filter(function (b) { return b.entries.length; });
        if (!nextLesson && teaching.length) nextLesson = "<p class='when'>" + dateLabel(iso) + "</p>" + teaching.map(lessonBit).join("");
        if (!nextAssessment && day.tests.length) nextAssessment = "<p class='when'>" + dateLabel(iso) + "</p>" + day.tests.map(assessmentBit).join("");
        return nextLesson && nextAssessment;
      });
      if (!nextLesson || !nextAssessment) {
        Object.keys(yearByDate).sort().some(function (iso) {
          if (iso < today) return false;
          var u = yearByDate[iso];
          // Detailed unit plans supersede the year estimate for that unit.
          if (layouts.some(function (L) { return L.id === yearUnitMap[u.id]; })) return false;
          var projectedTest = yearTestByUnit[u.id] === iso;
          var preview = "<p class='when'>" + dateLabel(iso) + "</p><p class='unitname'>" + esc(u.name) + "</p>";
          if (!nextLesson && !projectedTest) nextLesson = preview +
            "<p>Year Planner only. Choose lessons in the <a href='planner.html" +
            (yearUnitMap[u.id] === "pe" ? "" : "?unit=" + encodeURIComponent(yearUnitMap[u.id])) + "'>Unit Planner</a> to see materials here.</p>";
          if (!nextAssessment && projectedTest) nextAssessment = preview + "<p>Projected by the Year Planner. Set a test date in the Unit Planner to confirm it.</p>";
          return nextLesson && nextAssessment;
        });
      }
      return {
        lesson: nextLesson || "<p>No upcoming lessons in your saved plans. <a href='planner.html'>Open Unit Planner</a></p>",
        assessment: nextAssessment || "<p>No upcoming assessments in your saved plans.</p>"
      };
    }
    function sourceNote() {
      var sources = [];
      if (hasYear) sources.push(yearPlan.starter ? "starter year" : "Year Planner");
      layouts.forEach(function (L) { sources.push(L.shortName + " (" + L.sectionName + ")"); });
      return sources.length ? "Loaded for this device: " + sources.join("; ") + "." : "";
    }
    return {
      hasData: hasYear || !!layouts.length, dayHTML: dayHTML, weekCell: weekCell, upcomingHTML: upcomingHTML, sourceNote: sourceNote,
      todayIso: function () { return ISO(new Date()); }, addDays: addDays, fmtShort: fmtShort,
      weekday: function (iso) { return P(iso).getDay(); }
    };
  }

  window.HCGTeacherHome = buildView();
  if (window.addEventListener) window.addEventListener("storage", function (event) {
    var isPlan = event.key === null || event.key === "hcg_year_v1" ||
      Object.keys(window.HCG_UNITS || {}).some(function (id) { return window.HCG_UNITS[id].key === event.key; });
    if (!isPlan) return;
    window.HCGTeacherHome = buildView();
    if (typeof window.HCGHomeRender === "function") window.HCGHomeRender();
  });

  // One delegated handler for every All-Access download link on the page:
  // mint the Storage URL per click, exactly as the unit pages do.
  document.addEventListener("click", function (ev) {
    var a = ev.target && ev.target.closest ? ev.target.closest("button.my-day-download[data-storage]") : null;
    if (!a) return;
    ev.preventDefault();
    var status = document.getElementById("home-download-status");
    function say(message) { if (status) status.textContent = message; }
    if (!paidAccess() || !window.HCGFiles) { say("This file requires All-Access. The download did not start."); return; }
    a.disabled = true;
    say("Preparing " + a.textContent + "…");
    window.HCGFiles.url(a.getAttribute("data-storage")).then(function (url) {
      a.disabled = false;
      if (url) {
        say("Opening " + a.textContent + ".");
        window.location.href = url;
      } else say("This file is not currently available on this account.");
    }).catch(function () { a.disabled = false; say("The file could not be opened. Try again."); });
  });
})();
