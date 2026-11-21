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
  function P(iso) { var p = iso.split("-"); return new Date(+p[0], +p[1] - 1, +p[2]); }
  function ISO(d) {
    function z(n) { return (n < 10 ? "0" : "") + n; }
    return d.getFullYear() + "-" + z(d.getMonth() + 1) + "-" + z(d.getDate());
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

  var yearPlan = load("hcg_year_v1");
  var unitPlan = load("hcg_unit_v1");
  var gaPlan = load("hcg_unit_ga_v1");
  var wwiPlan = load("hcg_unit_wwi_v1");
  var twPlan = load("hcg_unit_tw_v1");
  var dpPlan = load("hcg_unit_dp_v1");
  var ww2Plan = load("hcg_unit_ww2_v1");
  var cwPlan = load("hcg_unit_cw_v1");
  var crPlan = load("hcg_unit_cr_v1");
  var maPlan = load("hcg_unit_ma_v1");
  var caPlan = load("hcg_unit_ca_v1");
  var fdPlan = load("hcg_unit_fd_v1");
  var erPlan = load("hcg_unit_er_v1");
  var jrPlan = load("hcg_unit_jr_v1");
  var scPlan = load("hcg_unit_sc_v1");
  var rcPlan = load("hcg_unit_rc_v1");
  var rvPlan = load("hcg_unit_rv_v1");
  var rePlan = load("hcg_unit_re_v1");
  var rmPlan = load("hcg_unit_rm_v1");
  var ITEMS = window.HCG_ITEMS || [];

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
    var overrides = yearPlan.unitDays || {}, pins = yearPlan.pinnedStarts || {}, idx = 0;
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
      var rplan = rid === "u15" ? rvPlan : rid === "u16" ? rePlan : rmPlan;
      var rdef = UNITS.filter(function (u) { return u.id === rid; })[0];
      var rdays = overrides[rid] != null ? overrides[rid]
        : (rplan && rplan.totalDays) ? rplan.totalDays : rdef.days;
      var keep = Math.max(0, Object.keys(yearReserved).length - Math.ceil(rdays / lpmY));
      Object.keys(yearReserved).sort().slice(0, Object.keys(yearReserved).length - keep)
        .forEach(function (iso) { delete yearReserved[iso]; });
    })();
    UNITS.filter(function (u) { return ids.indexOf(u.id) !== -1; }).forEach(function (u) {
      var lessonDays = overrides[u.id] != null ? overrides[u.id]
        : (u.id === "pe" && unitPlan && unitPlan.totalDays) ? unitPlan.totalDays
        : (u.id === "u7" && gaPlan && gaPlan.totalDays) ? gaPlan.totalDays
        : (u.id === "wwi" && wwiPlan && wwiPlan.totalDays) ? wwiPlan.totalDays
        : (u.id === "u9" && twPlan && twPlan.totalDays) ? twPlan.totalDays
        : (u.id === "u10" && dpPlan && dpPlan.totalDays) ? dpPlan.totalDays
        : (u.id === "u11" && ww2Plan && ww2Plan.totalDays) ? ww2Plan.totalDays
        : (u.id === "u12" && cwPlan && cwPlan.totalDays) ? cwPlan.totalDays
        : (u.id === "u13" && crPlan && crPlan.totalDays) ? crPlan.totalDays
        : (u.id === "u14" && maPlan && maPlan.totalDays) ? maPlan.totalDays
        : (u.id === "u1" && caPlan && caPlan.totalDays) ? caPlan.totalDays
        : (u.id === "u2" && fdPlan && fdPlan.totalDays) ? fdPlan.totalDays
        : (u.id === "u3" && erPlan && erPlan.totalDays) ? erPlan.totalDays
        : (u.id === "u4" && jrPlan && jrPlan.totalDays) ? jrPlan.totalDays
        : (u.id === "u5" && scPlan && scPlan.totalDays) ? scPlan.totalDays
        : (u.id === "u6" && rcPlan && rcPlan.totalDays) ? rcPlan.totalDays
        : (u.id === "u15" && rvPlan && rvPlan.totalDays) ? rvPlan.totalDays
        : (u.id === "u16" && rePlan && rePlan.totalDays) ? rePlan.totalDays
        : (u.id === "u17" && rmPlan && rmPlan.totalDays) ? rmPlan.totalDays : u.days;
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
    if (!plan || !plan.selected) return null;
    var byIdU = {};
    def.items.forEach(function (it) { byIdU[it.id] = it; });
    (plan.customItems || []).forEach(function (ci) {
      byIdU[ci.id] = {
        id: ci.id, lesson: 0, custom: true, ck: ci.kind,
        kind: ci.kind === "tpsp" ? "TPSP" : "Your resource",
        name: ci.title, days: ci.days, tags: ci.bp || [], file: "",
        link: ci.link || "", note: ci.note || ""
      };
    });
    var sections = (plan.sections && plan.sections.length) ? plan.sections : [plan];
    var sec = sections[Math.min(plan.active || 0, sections.length - 1)];
    if (!sec || typeof sec.start !== "string" || typeof sec.test !== "string") return null;
    var dc = P(sec.start), testD = P(sec.test), maxEnd = P(sec.start);
    maxEnd.setDate(maxEnd.getDate() + 366);
    if (ISO(dc) !== sec.start || ISO(testD) !== sec.test || testD <= dc || testD > maxEnd) return null;
    var storagePrefix = "";
    def.items.forEach(function (it) {
      if (!storagePrefix && it.storage) storagePrefix = it.storage.slice(0, it.storage.lastIndexOf("/") + 1);
    });
    var out = {
      name: def.name, shortName: def.shortName, testHref: def.testHref, testName: def.testName,
      testStorage: (!def.testHref && storagePrefix) ? storagePrefix + def.testName : null,
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
    (plan.customItems || []).forEach(function (ci) {
      if (!plan.selected[ci.id]) return;
      if (splits[ci.id]) { want.push(ci.id + "#a"); want.push(ci.id + "#b"); }
      else want.push(ci.id);
    });
    var order = want.slice();
    if (plan.order) {
      var have = {};
      plan.order.forEach(function (k) { have[k] = true; });
      order = plan.order.filter(function (k) { return want.indexOf(k) !== -1; });
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

  var GA_DEF = (window.HCG_UNITS && window.HCG_UNITS.ga) || null;
  var WWI_DEF = (window.HCG_UNITS && window.HCG_UNITS.wwi) || null;
  var TW_DEF = (window.HCG_UNITS && window.HCG_UNITS.tw) || null;
  var DP_DEF = (window.HCG_UNITS && window.HCG_UNITS.dp) || null;
  var WW2_DEF = (window.HCG_UNITS && window.HCG_UNITS.ww2) || null;
  var CW_DEF = (window.HCG_UNITS && window.HCG_UNITS.cw) || null;
  var CR_DEF = (window.HCG_UNITS && window.HCG_UNITS.cr) || null;
  var MA_DEF = (window.HCG_UNITS && window.HCG_UNITS.ma) || null;
  var CA_DEF = (window.HCG_UNITS && window.HCG_UNITS.ca) || null;
  var FD_DEF = (window.HCG_UNITS && window.HCG_UNITS.fd) || null;
  var ER_DEF = (window.HCG_UNITS && window.HCG_UNITS.er) || null;
  var JR_DEF = (window.HCG_UNITS && window.HCG_UNITS.jr) || null;
  var SC_DEF = (window.HCG_UNITS && window.HCG_UNITS.sc) || null;
  var RC_DEF = (window.HCG_UNITS && window.HCG_UNITS.rc) || null;
  var RV_DEF = (window.HCG_UNITS && window.HCG_UNITS.rv) || null;
  var RE_DEF = (window.HCG_UNITS && window.HCG_UNITS.re) || null;
  var RM_DEF = (window.HCG_UNITS && window.HCG_UNITS.rm) || null;
  var peLayout = buildUnitLayout(unitPlan, { name: "The Progressive Era", shortName: "Progressive Era", items: ITEMS, testHref: "files/unit-test.pdf", testName: "unit-test.pdf" });
  var gaLayout = GA_DEF ? buildUnitLayout(gaPlan, { name: GA_DEF.name, shortName: GA_DEF.shortName, items: GA_DEF.items, testHref: null, testName: "unit-test.pdf" }) : null;
  var wwiLayout = WWI_DEF ? buildUnitLayout(wwiPlan, { name: WWI_DEF.name, shortName: WWI_DEF.shortName, items: WWI_DEF.items, testHref: null, testName: "unit-test.pdf" }) : null;
  var twLayout = TW_DEF ? buildUnitLayout(twPlan, { name: TW_DEF.name, shortName: TW_DEF.shortName, items: TW_DEF.items, testHref: null, testName: "unit-test.pdf" }) : null;
  var dpLayout = DP_DEF ? buildUnitLayout(dpPlan, { name: DP_DEF.name, shortName: DP_DEF.shortName, items: DP_DEF.items, testHref: null, testName: "unit-test.pdf" }) : null;
  var ww2Layout = WW2_DEF ? buildUnitLayout(ww2Plan, { name: WW2_DEF.name, shortName: WW2_DEF.shortName, items: WW2_DEF.items, testHref: null, testName: "unit-test.pdf" }) : null;
  var cwLayout = CW_DEF ? buildUnitLayout(cwPlan, { name: CW_DEF.name, shortName: CW_DEF.shortName, items: CW_DEF.items, testHref: null, testName: "unit-test.pdf" }) : null;
  var crLayout = CR_DEF ? buildUnitLayout(crPlan, { name: CR_DEF.name, shortName: CR_DEF.shortName, items: CR_DEF.items, testHref: null, testName: "unit-test.pdf" }) : null;
  var maLayout = MA_DEF ? buildUnitLayout(maPlan, { name: MA_DEF.name, shortName: MA_DEF.shortName, items: MA_DEF.items, testHref: null, testName: "unit-test.pdf" }) : null;
  var caLayout = CA_DEF ? buildUnitLayout(caPlan, { name: CA_DEF.name, shortName: CA_DEF.shortName, items: CA_DEF.items, testHref: null, testName: "unit-test.pdf" }) : null;
  var fdLayout = FD_DEF ? buildUnitLayout(fdPlan, { name: FD_DEF.name, shortName: FD_DEF.shortName, items: FD_DEF.items, testHref: null, testName: "unit-test.pdf" }) : null;
  var erLayout = ER_DEF ? buildUnitLayout(erPlan, { name: ER_DEF.name, shortName: ER_DEF.shortName, items: ER_DEF.items, testHref: null, testName: "unit-test.pdf" }) : null;
  var jrLayout = JR_DEF ? buildUnitLayout(jrPlan, { name: JR_DEF.name, shortName: JR_DEF.shortName, items: JR_DEF.items, testHref: null, testName: "unit-test.pdf" }) : null;
  var scLayout = SC_DEF ? buildUnitLayout(scPlan, { name: SC_DEF.name, shortName: SC_DEF.shortName, items: SC_DEF.items, testHref: null, testName: "unit-test.pdf" }) : null;
  var rcLayout = RC_DEF ? buildUnitLayout(rcPlan, { name: RC_DEF.name, shortName: RC_DEF.shortName, items: RC_DEF.items, testHref: null, testName: "unit-test.pdf" }) : null;
  var rvLayout = RV_DEF ? buildUnitLayout(rvPlan, { name: RV_DEF.name, shortName: RV_DEF.shortName, items: RV_DEF.items, testHref: null, testName: "practice-test.pdf" }) : null;
  var reLayout = RE_DEF ? buildUnitLayout(rePlan, { name: RE_DEF.name, shortName: RE_DEF.shortName, items: RE_DEF.items, testHref: null, testName: "practice-test.pdf" }) : null;
  var rmLayout = RM_DEF ? buildUnitLayout(rmPlan, { name: RM_DEF.name, shortName: RM_DEF.shortName, items: RM_DEF.items, testHref: null, testName: "practice-test.pdf" }) : null;
  var layouts = [];
  if (peLayout) layouts.push(peLayout);
  if (gaLayout) layouts.push(gaLayout);
  if (wwiLayout) layouts.push(wwiLayout);
  if (twLayout) layouts.push(twLayout);
  if (dpLayout) layouts.push(dpLayout);
  if (ww2Layout) layouts.push(ww2Layout);
  if (cwLayout) layouts.push(cwLayout);
  if (crLayout) layouts.push(crLayout);
  if (maLayout) layouts.push(maLayout);
  if (caLayout) layouts.push(caLayout);
  if (fdLayout) layouts.push(fdLayout);
  if (erLayout) layouts.push(erLayout);
  if (jrLayout) layouts.push(jrLayout);
  if (scLayout) layouts.push(scLayout);
  if (rcLayout) layouts.push(rcLayout);
  if (rvLayout) layouts.push(rvLayout);
  if (reLayout) layouts.push(reLayout);
  if (rmLayout) layouts.push(rmLayout);

  // ======================================================================
  // What a single date shows.
  // ======================================================================
  function dayInfo(iso) {
    var dow = P(iso).getDay();
    if (dow === 0 || dow === 6) return { kind: "noschool", text: "No school (weekend)" };
    if (yearOff[iso]) return { kind: "noschool", text: "No school: " + yearOff[iso] };
    var li, L;
    for (li = 0; li < layouts.length; li++) {
      L = layouts[li];
      if (iso === L.testIso) return { kind: "test", layout: L };
    }
    var blocks = [];
    layouts.forEach(function (L2) {
      if (L2.byDate[iso]) blocks.push({ layout: L2, entries: L2.byDate[iso], hw: (L2.homework && L2.homework[iso]) || "" });
    });
    if (blocks.length) return { kind: "units", blocks: blocks };
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
    if (u) return { kind: "other", unit: u.name, test: yearTestByUnit[u.id] === iso };
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
  function paidAccess() {
    try { return !!(window.HCGAuth && window.HCGAuth.entitlement && window.HCGAuth.entitlement().paid); }
    catch (e) { return false; }
  }
  function storageLink(path, label) {
    return "<a href='#' class='dl' data-storage='" + esc(path) + "' data-file='" + esc(label) + "'>" + esc(label) + "</a>";
  }
  function testBit(L) {
    if (L.testHref) return "<a href='" + esc(L.testHref) + "'>" + esc(L.testName) + "</a>";
    if (L.testStorage && paidAccess()) return storageLink(L.testStorage, L.testName);
    return esc(L.testName);
  }

  function safeResourceLink(value) {
    if (typeof value !== "string" || !/^https?:\/\//i.test(value.trim())) return "";
    try {
      var url = new URL(value.trim());
      return url.protocol === "http:" || url.protocol === "https:" ? url.href : "";
    } catch (e) { return ""; }
  }

  function materialsList(entries) {
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
        (f ? " · <a href='" + esc(f) + "'>" + esc(base) + "</a>" : (st ? " · " + (paidAccess() ? storageLink(e.item.storage, st) : esc(st)) : "")) + "</li>";
    }).join("");
    return "<ul class='materials'>" + lis + "</ul>";
  }
  function dayHTML(iso, heading) {
    var info = dayInfo(iso);
    var h = "<h3>" + esc(heading) + "</h3><p class='when'>" + esc(fmtLong(iso)) + "</p>";
    if (info.kind === "noschool" || info.kind === "open") {
      return h + "<p class='" + (info.kind === "noschool" ? "noschool" : "") + "'>" + esc(info.text) + "</p>";
    }
    if (info.kind === "test") {
      var L = info.layout;
      return h + "<p class='unitname'>" + esc(L.name) + "</p>" +
        "<p class='testday'>Unit test</p><ul class='materials'><li>Test: " +
        testBit(L) + "</li></ul>";
    }
    if (info.kind === "units") {
      return h + info.blocks.map(function (b) {
        return "<p class='unitname'>" + esc(b.layout.name) + "</p>" + materialsList(b.entries) +
          (b.hw ? "<p class='hwline'>Homework: " + esc(b.hw) + "</p>" : "");
      }).join("");
    }
    var out = h + "<p class='unitname'>" + esc(info.unit) + "</p>";
    if (info.test) {
      out += "<p class='testday'>Unit test</p>";
    }
    return out;
  }
  function weekCell(iso) {
    var info = dayInfo(iso);
    if (info.kind === "noschool" || info.kind === "open") return esc(info.text);
    if (info.kind === "test") {
      var L = info.layout;
      return esc(L.name) + " · <strong>Unit test</strong> (" +
        testBit(L) + ")";
    }
    if (info.kind === "units") {
      return info.blocks.map(function (b) {
        return esc(b.layout.name) + ": " + (b.hw ? "Homework: " + esc(b.hw) + " · " : "") + b.entries.map(function (e) {
          var f = e.item.file || "";
          var st = e.item.storage ? e.item.storage.split("/").pop() : "";
          return esc(e.name) + (f ? " (<a href='" + esc(f) + "'>" + esc(f.split("/").pop()) + "</a>)" : (st ? " (" + (paidAccess() ? storageLink(e.item.storage, st) : esc(st)) + ")" : ""));
        }).join("; ");
      }).join("<br>");
    }
    var s = esc(info.unit);
    if (info.test) s += " · <strong>Unit test</strong>";
    return s;
  }

  // ---------- shared exports ----------
  var hasData = !!((yearPlan && yearPlan.start) || (unitPlan && unitPlan.selected) || (gaPlan && gaPlan.selected) || (wwiPlan && wwiPlan.selected) || (twPlan && twPlan.selected) || (dpPlan && dpPlan.selected) || (ww2Plan && ww2Plan.selected) || (cwPlan && cwPlan.selected) || (crPlan && crPlan.selected) || (maPlan && maPlan.selected) || (caPlan && caPlan.selected) || (fdPlan && fdPlan.selected) || (erPlan && erPlan.selected) || (jrPlan && jrPlan.selected) || (scPlan && scPlan.selected) || (rcPlan && rcPlan.selected) || (rvPlan && rvPlan.selected) || (rePlan && rePlan.selected) || (rmPlan && rmPlan.selected));

  function sourceNote() {
  var sources = [];
  if (yearPlan && yearPlan.start) sources.push(yearPlan.starter ? "your starter year (set your real dates in the Year Planner)" : "your year plan");
  if (unitPlan && unitPlan.selected) sources.push("your Progressive Era unit plan" + (peLayout && peLayout.sectionName ? " (" + peLayout.sectionName + ")" : ""));
  if (gaPlan && gaPlan.selected) sources.push("your Gilded Age unit plan" + (gaLayout && gaLayout.sectionName ? " (" + gaLayout.sectionName + ")" : ""));
  if (wwiPlan && wwiPlan.selected) sources.push("your Imperialism and World War I unit plan" + (wwiLayout && wwiLayout.sectionName ? " (" + wwiLayout.sectionName + ")" : ""));
  if (twPlan && twPlan.selected) sources.push("your Twenties unit plan" + (twLayout && twLayout.sectionName ? " (" + twLayout.sectionName + ")" : ""));
  if (dpPlan && dpPlan.selected) sources.push("your Depression and New Deal unit plan" + (dpLayout && dpLayout.sectionName ? " (" + dpLayout.sectionName + ")" : ""));
  if (ww2Plan && ww2Plan.selected) sources.push("your World War II unit plan" + (ww2Layout && ww2Layout.sectionName ? " (" + ww2Layout.sectionName + ")" : ""));
  if (cwPlan && cwPlan.selected) sources.push("your Cold War unit plan" + (cwLayout && cwLayout.sectionName ? " (" + cwLayout.sectionName + ")" : ""));
  if (crPlan && crPlan.selected) sources.push("your Civil Rights unit plan" + (crLayout && crLayout.sectionName ? " (" + crLayout.sectionName + ")" : ""));
  if (maPlan && maPlan.selected) sources.push("your Modern America unit plan" + (maLayout && maLayout.sectionName ? " (" + maLayout.sectionName + ")" : ""));
  if (caPlan && caPlan.selected) sources.push("your Colonial America unit plan" + (caLayout && caLayout.sectionName ? " (" + caLayout.sectionName + ")" : ""));
  if (fdPlan && fdPlan.selected) sources.push("your Founding unit plan" + (fdLayout && fdLayout.sectionName ? " (" + fdLayout.sectionName + ")" : ""));
  if (erPlan && erPlan.selected) sources.push("your Early Republic unit plan" + (erLayout && erLayout.sectionName ? " (" + erLayout.sectionName + ")" : ""));
  if (jrPlan && jrPlan.selected) sources.push("your Jackson and Reform unit plan" + (jrLayout && jrLayout.sectionName ? " (" + jrLayout.sectionName + ")" : ""));
  if (scPlan && scPlan.selected) sources.push("your Sectional Crisis and Civil War unit plan" + (scLayout && scLayout.sectionName ? " (" + scLayout.sectionName + ")" : ""));
  if (rcPlan && rcPlan.selected) sources.push("your Reconstruction unit plan" + (rcLayout && rcLayout.sectionName ? " (" + rcLayout.sectionName + ")" : ""));
  if (rvPlan && rvPlan.selected) sources.push("your Course Review plan" + (rvLayout && rvLayout.sectionName ? " (" + rvLayout.sectionName + ")" : ""));
  if (rePlan && rePlan.selected) sources.push("your Early Course Review plan" + (reLayout && reLayout.sectionName ? " (" + reLayout.sectionName + ")" : ""));
  if (rmPlan && rmPlan.selected) sources.push("your Modern Course Review plan" + (rmLayout && rmLayout.sectionName ? " (" + rmLayout.sectionName + ")" : ""));
  return "Drawn from " + sources.join(" and ") + ". Change anything in the planners and this page follows.";
  }

  window.HCGTeacherHome = {
    hasData: hasData,
    dayHTML: dayHTML,
    weekCell: weekCell,
    sourceNote: sourceNote,
    todayIso: function () { return ISO(new Date()); },
    addDays: addDays,
    fmtShort: fmtShort
  };

  // One delegated handler for every All-Access download link on the page:
  // mint the Storage URL per click, exactly as the unit pages do.
  document.addEventListener("click", function (ev) {
    var a = ev.target && ev.target.closest ? ev.target.closest("a.dl[data-storage]") : null;
    if (!a) return;
    ev.preventDefault();
    if (!window.HCGFiles) return;
    var old = a.textContent; a.textContent = "Preparing…";
    window.HCGFiles.url(a.getAttribute("data-storage")).then(function (url) {
      a.textContent = old;
      if (url) window.location.href = url;
      else window.alert("That download is not available on this account. If you just subscribed, give it a few seconds and try again.");
    }).catch(function () { a.textContent = old; });
  });
})();
