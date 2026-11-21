(function () {
  // ---------------- active unit ----------------
  // The plannable units share this planner. Each unit's plan lives in its
  // own localStorage key with the same shape; the Progressive Era key and
  // state are exactly what they were before the second unit existed. The
  // active unit comes from a shared link's payload first, then ?unit=,
  // then the Progressive Era default.
  var UNITS = window.HCG_UNITS || {};
  var params = new URLSearchParams(location.search);
  var isSample = params.get("sample") === "progressive-era-week";
  var draftId = params.get("draft");
  var draftPrefix = "hcg_sample_progressive_week_v1:";
  var draftKey = isSample && /^[a-z0-9-]{16,60}$/.test(draftId || "") ? draftPrefix + draftId : null;
  var savedSample = null;
  if (draftKey) {
    try { savedSample = JSON.parse(localStorage.getItem(draftKey)); } catch (e) {}
    if (!savedSample || !savedSample.selected || !Array.isArray(savedSample.sections) || !savedSample.sections.length) {
      draftKey = null;
      savedSample = null;
    }
  }
  var sampleStart = "2026-11-30";
  var sampleOrder = ["l1-reading", "l1-notes", "l1-activity", "l2-reading", "l2-notes", "l2-activity", "l3-reading", "l3-notes"];
  var sharedPayload = null;
  try {
    if (!isSample && location.hash.length <= 2500000 && location.hash.indexOf("#plan=") === 0) {
      sharedPayload = JSON.parse(decodeURIComponent(escape(atob(location.hash.slice(6).replace(/-/g, "+").replace(/_/g, "/")))));
    }
  } catch (e) {}
  var unitId = "pe";
  if (sharedPayload && Object.prototype.hasOwnProperty.call(UNITS, sharedPayload.unit)) unitId = sharedPayload.unit;
  else if (!isSample) {
    var wantUnit = null;
    try { wantUnit = new URLSearchParams(location.search).get("unit"); } catch (e) {}
    if (wantUnit && Object.prototype.hasOwnProperty.call(UNITS, wantUnit)) unitId = wantUnit;
  }
  var U = UNITS[unitId] || UNITS.pe;
  var BP = U.blueprint, LESSONS = U.lessons, ITEMS = U.items;
  var TOPICS = U.topics || {}, BP_TOPIC = U.bpTopic || {};
  var TPSP_LIST = U.tpsp || [];
  var KEY = U.key;
  var byId = Object.create(null);
  ITEMS.forEach(function (it) { byId[it.id] = it; });

  function isEntitled() {
    try { return !!(window.HCGAuth && window.HCGAuth.entitlement().paid); } catch (e) { return false; }
  }
  function fileNameOf(it) {
    var f = (it && (it.file || it.storage)) || "";
    return f.split("/").pop();
  }
  // A Storage download control: the filename shows for everyone; entitled
  // accounts get a working Download that mints its URL on click, the way
  // the Gilded Age unit page does. No public URL is ever emitted. Signed
  // out, the file shows as a "PDF · All-Access" chip so the paid boundary
  // reads as a boundary, not as a broken link.
  function storageLinkHTML(it) {
    if (isEntitled()) {
      return "<a href='#' class='ga-dl' data-storage='" + it.storage + "' style='font-size:12.5px;'>Download</a>" +
        " <span style='font-size:12.5px;color:#5a616d;'>(" + fileNameOf(it) + ")</span>";
    }
    return "<span class='kindchip'>PDF · All-Access</span>" +
      " <span style='font-size:12.5px;color:#5a616d;'>" + fileNameOf(it) + "</span>";
  }
  function wireDownloads(root) {
    if (!root) return;
    root.querySelectorAll("a.ga-dl").forEach(function (a) {
      a.addEventListener("click", function (ev) {
        ev.preventDefault();
        if (!window.HCGFiles) return;
        var old = a.textContent;
        a.textContent = "Preparing…";
        window.HCGFiles.url(a.getAttribute("data-storage")).then(function (url) {
          a.textContent = old;
          if (url) window.location.href = url;
          else window.alert("That download is not available on this account. If you just subscribed, give it a few seconds and try again.");
        }).catch(function () { a.textContent = old; });
      });
    });
  }

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  // ---------------- calendar additions (teacher-added items) ----------------
  // state.customItems holds {id, title, days, kind: "own"|"tpsp", link,
  // note, bp, tpspId?}. For layout they are dressed as plate items in a
  // parallel registry, so order/pins/splits/packing treat them exactly
  // like built-ins; only rendering and coverage know they are additions.
  var custById = Object.create(null);
  function customItemLike(ci) {
    return {
      id: ci.id, lesson: 0, custom: true, ck: ci.kind,
      kind: ci.kind === "tpsp" ? "TPSP" : "Your resource",
      name: ci.title, days: ci.days, tags: ci.bp || [], file: "",
      link: ci.link || "", note: ci.note || ""
    };
  }
  function refreshCustom() {
    custById = Object.create(null);
    (state.customItems || []).forEach(function (ci) { custById[ci.id] = customItemLike(ci); });
  }
  function itemFor(id) { return byId[id] || custById[id]; }
  var customSeq = 0;
  function newCustomId() {
    var id;
    do {
      id = "x" + Date.now().toString(36) + (customSeq++).toString(36) + Math.floor(Math.random() * 46656).toString(36);
    } while (byId[id] || custById[id]);
    return id;
  }
  function customById(id) {
    return (state.customItems || []).filter(function (ci) { return ci.id === id; })[0] || null;
  }

  function newSection(name, src) {
    src = src || {};
    return {
      name: name || "Period 1",
      start: src.start || "2026-10-26",
      test: src.test || "2026-11-20",
      dayTypes: Object.assign({}, src.dayTypes),
      // Sub days: { iso: note }. The class meets and the date (and the
      // test day) holds, but the day teaches nothing from the plan; its
      // work moves later or overflows, like a lost day whose date stays
      // on the calendar. The value is the teacher's note for the sub,
      // possibly "". Old saves and shares simply lack the field.
      subDays: Object.assign({}, src.subDays),
      // Homework: { iso: text }. The teacher's homework line for a day,
      // typed in the list view, shown in the week view, and carried into
      // the printed plan, the sub plan, the calendar export, and the
      // teacher home page. Old saves and shares simply lack the field.
      homework: Object.assign({}, src.homework),
      pins: Object.assign({}, src.pins),
      rotation: src.rotation || "daily",
      // Class period length for this section: 45 (standard period) or 90
      // (block). Content is paced in lesson-days; a block meeting holds
      // about two lesson-days. Old saves without the field get 45.
      period: src.period === 90 ? 90 : 45
    };
  }

  // ---------------- state: v4 sections; v2/v3 saves migrate in place ----------------
  var state = { selected: {}, order: null, splits: {}, view: "list", active: 0, sections: [newSection()], customItems: [] };
  if (isSample) {
    state.order = sampleOrder.slice();
    sampleOrder.forEach(function (id) { state.selected[id] = true; });
    state.sections = [newSection("Sample week", { start: sampleStart, test: sampleEnd(sampleStart) })];
    state.view = "week";
  } else {
    ITEMS.forEach(function (it) { if (it.core) state.selected[it.id] = true; });
  }
  function record(value) { return value && typeof value === "object" && !Array.isArray(value); }
  function planId(id) { return typeof id === "string" && /^[a-zA-Z0-9_-]{1,90}$/.test(id) && id !== "__proto__"; }
  function orderId(id) { return typeof id === "string" && planId(baseId(id)); }
  function validDate(s) { return Number.isFinite(P(s).getTime()); }
  function mapOf(obj, keyOk, valueOk) {
    return obj == null || (record(obj) && Object.keys(obj).every(function (key) { return keyOk(key) && valueOk(obj[key]); }));
  }
  function textValue(s) { return typeof s === "string"; }
  function boolValue(v) { return typeof v === "boolean"; }
  function supportedPlan(plan, portable) {
    if (!record(plan) || !record(plan.selected) || !mapOf(plan.selected, planId, boolValue) ||
        !mapOf(plan.splits, planId, boolValue) ||
        (plan.order != null && (!Array.isArray(plan.order) || !plan.order.every(orderId)))) return false;
    if (plan.unit != null && plan.unit !== unitId) return false;
    if (plan.sections != null && (!Array.isArray(plan.sections) || !plan.sections.length)) return false;
    if (portable && !plan.sections && (!plan.start || !plan.test)) return false;
    if (!(plan.sections || [plan]).every(function (section) {
      return record(section) && (section.name == null || textValue(section.name)) &&
        (section.start == null || validDate(section.start)) && (section.test == null || validDate(section.test)) &&
        mapOf(section.pins, orderId, validDate) &&
        mapOf(section.dayTypes, validDate, function (type) { return /^(Assembly|Substitute|Field trip|Testing|No class)?$/.test(type); }) &&
        mapOf(section.subDays, validDate, textValue) && mapOf(section.homework, validDate, textValue);
    })) return false;
    if (plan.customItems == null) return true;
    var seen = Object.create(null);
    return Array.isArray(plan.customItems) && plan.customItems.every(function (item) {
      if (!record(item) || !planId(item.id) || byId[item.id] || seen[item.id] ||
          !textValue(item.title) || [0, 0.5, 1, 2].indexOf(item.days) === -1 || ["own", "tpsp"].indexOf(item.kind) === -1 ||
          (item.link != null && !textValue(item.link)) || (item.note != null && !textValue(item.note)) ||
          (item.bp != null && (!Array.isArray(item.bp) || !item.bp.every(function (t) { return Number.isInteger(t) && !!BP[t]; })))) return false;
      seen[item.id] = true;
      return true;
    });
  }
  function usePlan(plan, legacyName) {
    state.selected = Object.assign(Object.create(null), plan.selected);
    state.order = plan.order ? plan.order.slice() : null;
    state.splits = Object.assign(Object.create(null), plan.splits);
    state.customItems = plan.customItems || [];
    state.view = plan.view === "week" ? "week" : "list";
    state.sections = plan.sections ? plan.sections.map(function (s, i) { return newSection(s.name || ("Period " + (i + 1)), s); })
      : [newSection(legacyName || "Period 1", plan)];
    state.active = Math.max(0, Math.min(Number.isInteger(plan.active) ? plan.active : 0, state.sections.length - 1));
  }
  var hasStoredPlan = false, unreadableDevicePlan = false;
  try {
    var raw = isSample ? null : localStorage.getItem(KEY);
    hasStoredPlan = raw !== null;
    var saved = isSample ? savedSample : JSON.parse(raw);
    if (saved && supportedPlan(saved, false)) usePlan(saved);
    else if (isSample && draftKey) draftKey = null;
    else if (hasStoredPlan) unreadableDevicePlan = true;
  } catch (e) { if (!isSample) unreadableDevicePlan = true; }
  function SEC() { return state.sections[state.active]; }
  function subDaysOf(sec) { if (!sec.subDays) sec.subDays = {}; return sec.subDays; }
  function isSubDay(sec, iso) { return Object.prototype.hasOwnProperty.call(sec.subDays || {}, iso); }
  function subNoteOf(sec, iso) { return (sec.subDays && sec.subDays[iso]) || ""; }
  function homeworkOf(sec) { if (!sec.homework) sec.homework = {}; return sec.homework; }
  function hwTextOf(sec, iso) { return (sec.homework && sec.homework[iso]) || ""; }
  function hwRowHTML(iso) {
    return "<div class='hwrow'><span class='hwlab'>Homework</span> " +
      "<input type='text' class='hwinput' data-hw='" + iso + "' value='" + esc(hwTextOf(SEC(), iso)) +
      "' placeholder='Add homework (optional)' aria-label='Homework for this day'></div>";
  }
  function hwPrintP(sec, iso) {
    var t = hwTextOf(sec, iso);
    return t ? "<p style='margin:2px 0 0;'>Homework: " + esc(t) + "</p>" : "";
  }
  function wireHomework(root) {
    root.querySelectorAll("[data-hw]").forEach(function (inp) {
      inp.addEventListener("change", function () {
        var iso = inp.getAttribute("data-hw");
        if (inp.value.trim()) homeworkOf(SEC())[iso] = inp.value;
        else delete homeworkOf(SEC())[iso];
        render();
      });
    });
  }

  // Never replace an existing plan merely by opening a shared link.
  var sharedLoaded = false;
  if (!isSample && location.hash.indexOf("#plan=") === 0) {
    if (!supportedPlan(sharedPayload, true)) {
      window.alert("This shared link does not contain a supported unit plan. Your saved plan was not changed.");
    } else if (!hasStoredPlan && !unreadableDevicePlan ||
        window.confirm("Open this shared plan and replace this unit’s saved plan on this device? Choose Cancel to keep your plan. You can export it first.")) {
      usePlan(sharedPayload, "Shared plan");
      unreadableDevicePlan = false;
      sharedLoaded = true;
    }
    try { history.replaceState(null, "", location.pathname + (unitId === "pe" ? "" : "?unit=" + encodeURIComponent(unitId))); } catch (e) {}
  }

  function baseId(key) { return key.replace(/#[ab]$/, ""); }
  function entryFor(key) {
    var it = itemFor(baseId(key));
    if (!it) return null;
    var part = /#a$/.test(key) ? 1 : (/#b$/.test(key) ? 2 : 0);
    if (part) return { key: key, item: it, days: it.days / 2, name: it.name + " (part " + part + ")", part: part };
    return { key: key, item: it, days: it.days, name: it.name, part: 0 };
  }
  function keysFor(id) { return state.splits[id] ? [id + "#a", id + "#b"] : [id]; }

  function syncOrder() {
    refreshCustom();
    var want = [];
    ITEMS.forEach(function (it) { if (state.selected[it.id]) keysFor(it.id).forEach(function (k) { want.push(k); }); });
    (state.customItems || []).forEach(function (ci) { if (state.selected[ci.id]) keysFor(ci.id).forEach(function (k) { want.push(k); }); });
    if (!state.order) { state.order = want.slice(); return; }
    var have = {};
    state.order.forEach(function (k) { have[k] = true; });
    var out = state.order.filter(function (k, i) { return want.indexOf(k) !== -1 && state.order.indexOf(k) === i; });
    want.forEach(function (k) { if (!have[k]) out.push(k); });
    state.order = out;
    state.sections.forEach(function (s) {
      Object.keys(s.pins).forEach(function (k) { if (want.indexOf(k) === -1) delete s.pins[k]; });
    });
  }

  var startEl = document.getElementById("start");
  var testEl = document.getElementById("test");
  var rotEl = document.getElementById("rotation");
  var periodEl = document.getElementById("period");
  function lessonsPerMeeting() { return SEC().period === 90 ? 2 : 1; }

  function P(v) {
    if (typeof v !== "string" || !/^\d{4}-\d{2}-\d{2}$/.test(v)) return new Date(NaN);
    var p = v.split("-"), d = new Date(0);
    d.setFullYear(+p[0], +p[1] - 1, +p[2]);
    d.setHours(0, 0, 0, 0);
    return ISO(d) === v ? d : new Date(NaN);
  }
  function ISO(d) {
    function z(n) { return (n < 10 ? "0" : "") + n; }
    return String(d.getFullYear()).padStart(4, "0") + "-" + z(d.getMonth() + 1) + "-" + z(d.getDate());
  }
  function fmt(d) { return d.toLocaleDateString("en-US", { weekday: "short", month: "short", day: "numeric" }); }

  function sampleEnd(start) {
    var end = P(start);
    var count = 0;
    while (count < 5 && Number.isFinite(end.getTime())) {
      var day = end.getDay();
      if (day > 0 && day < 6) count++;
      end.setDate(end.getDate() + 1);
    }
    return Number.isFinite(end.getTime()) ? ISO(end) : null;
  }

  function yearOffs(first, last) {
    var set = {};
    if (isSample) return set;
    try {
      var y = JSON.parse(localStorage.getItem("hcg_year_v1"));
      if (y && y.daysOff) y.daysOff.forEach(function (o) {
        if (!o) return;
        var d = P(o.from), end = P(o.to);
        if (d < first) d = new Date(first);
        if (end > last) end = last;
        while (d <= end) { set[ISO(d)] = typeof o.label === "string" && o.label.trim() ? o.label : "Day off"; d.setDate(d.getDate() + 1); }
      });
    } catch (e) {}
    return set;
  }

  function candidateDays() {
    var sec = SEC();
    var d = P(sec.start), test = P(sec.test), out = [], rangeIssue = "";
    var maxEnd = new Date(d);
    maxEnd.setDate(maxEnd.getDate() + 366);
    if (!Number.isFinite(d.getTime()) || !Number.isFinite(test.getTime()) || test <= d) {
      rangeIssue = "Choose a valid first day and a test date after it.";
    } else if (test > maxEnd) {
      rangeIssue = "Choose unit dates no more than 366 days apart.";
    }
    var offs = rangeIssue ? {} : yearOffs(d, test);
    while (!rangeIssue && d < test) {
      var dow = d.getDay(), iso = ISO(d);
      if (dow >= 1 && dow <= 5 && !offs[iso]) out.push({ date: new Date(d), iso: iso, meet: true });
      d.setDate(d.getDate() + 1);
    }
    if (sec.rotation === "ab") out.forEach(function (c, i) { c.meet = i % 2 === 0; });
    var testIssue = rangeIssue;
    if (!isSample && !testIssue) {
      if (test.getDay() < 1 || test.getDay() > 5) testIssue = "The selected test date is a weekend.";
      else if (offs[sec.test]) testIssue = "The selected test date is a day off in your year plan.";
      else if (sec.dayTypes[sec.test] || isSubDay(sec, sec.test)) testIssue = "The selected test date is marked unavailable.";
      else if (sec.rotation === "ab" && out.length % 2) testIssue = "This section does not meet on the selected test date.";
    }
    return { days: out, offs: offs, rangeIssue: rangeIssue, testIssue: testIssue };
  }
  function lessonWeight(n) {
    var tags = {};
    ITEMS.forEach(function (it) { if (it.lesson === n) it.tags.forEach(function (t) { tags[t] = true; }); });
    return Object.keys(tags).length;
  }

  // ---------------- layout: pins first, then flow in order ----------------
  // Each bucket is one meeting date. Its capacity is the section's
  // lessons-per-meeting: 1 lesson-day for a 45-minute period, about 2 for
  // a 90-minute block, so entries pack onto shared meeting dates in block
  // mode while keeping their order. The test sits on its own date after
  // the last bucket and is never packed with an entry.
  function layout(cand) {
    var sec = SEC();
    var cap = lessonsPerMeeting();
    var usable = cand.days.filter(function (c) { return c.meet && !sec.dayTypes[c.iso] && !isSubDay(sec, c.iso); });
    return window.HCGUnitSchedule.allocate(usable, state.order.map(entryFor).filter(Boolean), sec.pins, cap);
  }

  var L = null;

  // ---------------- sections bar ----------------
  function renderSections() {
    var el = document.getElementById("sections");
    el.innerHTML = state.sections.map(function (s, i) {
      return "<button type='button' class='mini sectab" + (i === state.active ? " on" : "") + "' data-sec='" + i + "'>" + esc(s.name) + "</button>";
    }).join("") +
      "<button type='button' class='mini' id='sec-add'>+ Add section</button>" +
      "<button type='button' class='mini' id='sec-rename'>Rename</button>" +
      (state.sections.length > 1 ? "<button type='button' class='mini' id='sec-del'>Delete</button>" : "");
    el.querySelectorAll("[data-sec]").forEach(function (b) {
      b.addEventListener("click", function () { state.active = +b.getAttribute("data-sec"); render(); });
    });
    document.getElementById("sec-add").addEventListener("click", function () {
      var cur = SEC();
      var name = window.prompt("Name the new section (it starts as a copy of " + cur.name + "'s calendar):", "Period " + (state.sections.length + 1));
      if (!name) return;
      state.sections.push(newSection(name, cur));
      state.active = state.sections.length - 1;
      render();
    });
    document.getElementById("sec-rename").addEventListener("click", function () {
      var name = window.prompt("Rename this section:", SEC().name);
      if (name && name.trim()) { SEC().name = name.trim(); render(); }
    });
    var resetPins = document.getElementById("reset-pins");
    if (resetPins) resetPins.disabled = !Object.keys(SEC().pins).length;
    var del = document.getElementById("sec-del");
    if (del) del.addEventListener("click", function () {
      if (!window.confirm("Delete the section \"" + SEC().name + "\" and its calendar? Your picks and order are shared and stay.")) return;
      state.sections.splice(state.active, 1);
      inputsBound = -1;
      state.active = 0;
      render();
    });
  }

  // ---------------- pacing proposal ----------------
  function renderPacing(cand) {
    var sec = SEC();
    var el = document.getElementById("pacing");
    var dc = document.getElementById("daycount");
    var usable = cand.days.filter(function (c) { return c.meet && !sec.dayTypes[c.iso] && !isSubDay(sec, c.iso); }).length;
    if (isSample) {
      dc.textContent = usable + " of " + cand.days.length + " weekdays available for instruction.";
      return;
    }
    if (cand.rangeIssue || !cand.days.length) {
      dc.textContent = cand.rangeIssue || cand.testIssue || "There are no instructional weekdays before the test.";
      el.innerHTML = "";
      return;
    }
    dc.textContent = usable + " usable meeting days for " + sec.name + " between the first day and the test" +
      (sec.rotation === "ab" ? " (every-other-day rotation)" : "") +
      (sec.period === 90 ? ", about " + (usable * lessonsPerMeeting()) + " lesson-days of room at two lessons per meeting" : "") +
      " (weekends and year-plan days off skipped, marked and sub days excluded)." +
      (cand.testIssue ? " " + cand.testIssue + " Choose another test date." : " The test is an additional meeting.");
    // The proposal budgets lesson-days: usable meetings less one held for
    // review, times the lessons that fit in a meeting.
    var forLessons = Math.max(usable - 1, 0) * lessonsPerMeeting();
    var weights = LESSONS.map(function (l) { return lessonWeight(l.n); });
    var totalW = weights.reduce(function (a, b) { return a + b; }, 0);
    var raw = weights.map(function (w) { return forLessons * w / totalW; });
    var alloc = raw.map(Math.floor);
    var left = forLessons - alloc.reduce(function (a, b) { return a + b; }, 0);
    raw.map(function (r, i) { return { i: i, frac: r - Math.floor(r) }; })
       .sort(function (a, b) { return b.frac - a.frac; })
       .forEach(function (o) { if (left > 0) { alloc[o.i]++; left--; } });
    var block = SEC().period === 90;
    var rows = LESSONS.map(function (l, i) {
      return "<tr><td>Lesson " + l.n + " · " + l.title + "</td><td style='text-align:right;white-space:nowrap;'>" +
        alloc[i] + (block ? (alloc[i] === 1 ? " lesson-day" : " lesson-days") : (alloc[i] === 1 ? " day" : " days")) + "</td></tr>";
    });
    rows.push("<tr><td>Review day</td><td style='text-align:right;'>" + (block ? "1 meeting" : "1 day") + "</td></tr>");
    rows.push("<tr><td><strong>Unit test</strong></td><td style='text-align:right;white-space:nowrap;'>" + (cand.testIssue ? "Not scheduled" : fmt(P(sec.test))) + "</td></tr>");
    el.innerHTML = rows.join("");
  }

  function toggleSplit(id) {
    if (state.splits[id]) {
      delete state.splits[id];
      state.sections.forEach(function (s) {
        if (s.pins[id + "#a"] || s.pins[id + "#b"]) s.pins[id] = s.pins[id + "#a"] || s.pins[id + "#b"];
        delete s.pins[id + "#a"]; delete s.pins[id + "#b"];
      });
      var firstPart = state.order.findIndex(function (k) { return baseId(k) === id; });
      state.order = state.order.filter(function (k) { return baseId(k) !== id; });
      if (firstPart !== -1) state.order.splice(firstPart, 0, id);
    } else {
      state.splits[id] = true;
      var at = state.order.indexOf(id);
      if (at !== -1) state.order.splice(at, 1, id + "#a", id + "#b");
      state.sections.forEach(function (s) {
        if (s.pins[id]) { s.pins[id + "#a"] = s.pins[id]; delete s.pins[id]; }
      });
    }
    render();
  }

  function coversSpan(tags) {
    if (!tags || !tags.length) return "";
    var titles = tags.map(function (t) { return "Entry " + t + " · " + (BP[t] || ""); }).join("; ");
    return " <span class='small' style='color:#5a616d;' title='" + esc(titles) + "'>covers " + tags.join(" · ") + "</span>";
  }

  // ---------------- picker, with split toggles ----------------
  function renderPicker() {
    var el = document.getElementById("picker");
    var html = "";
    // Paid units plan in full while signed out; say once, at the top, that
    // the files themselves are the All-Access part, so the chips on each
    // row read as a boundary rather than a defect. The free sample unit
    // has no storage items and never shows this line.
    if (!isEntitled() && ITEMS.some(function (it) { return !!it.storage; })) {
      html += "<p class='small' style='margin:10px 0 2px;'>Planning is free for every unit. The files themselves open with All-Access.</p>";
    }
    LESSONS.concat([{ n: 9, title: "Review Day" }]).forEach(function (l) {
      var items = ITEMS.filter(function (it) { return it.lesson === l.n; });
      if (!items.length) return;
      html += "<h3 style='font-size:16.5px;margin:16px 0 4px;'>" + (l.n === 9 ? "Review Day" : "Lesson " + l.n + " · " + l.title) + "</h3>";
      items.forEach(function (it) {
        var dayLabel = state.splits[it.id] ? "2 half days" : (it.days === 0 ? "same day" : (it.days === 0.5 ? "half day" : "1 day"));
        var splitBtn = it.days >= 1 ?
          "<button type='button' class='mini splitbtn' data-split='" + it.id + "'>" + (state.splits[it.id] ? "Unsplit" : "Split") + "</button>" : "";
        var fileHtml = it.file ?
          "<a href='" + it.file + "' style='font-size:12.5px;'>PDF</a>" :
          (it.storage ? storageLinkHTML(it) : "");
        // The review day's study guide also carries the student vocabulary
        // deck: same definitions as the guided notes, on Rycal, for students.
        var rycalHtml = (l.n === 9 && /rev-guide$/.test(it.id) && U.rycalDeck) ?
          " <a href='" + U.rycalDeck + "' target='_blank' rel='noopener' style='font-size:12.5px;'>Rycal vocab deck</a>" : "";
        var coversHtml = coversSpan(it.tags);
        html += "<label class='pick'><input type='checkbox' data-id='" + it.id + "'" + (state.selected[it.id] ? " checked" : "") + ">" +
          "<span><span class='kind' style='font-size:10.5px;letter-spacing:1.2px;text-transform:uppercase;color:#1f3350;'>" + it.kind + "</span> · " +
          it.name + " " + fileHtml + rycalHtml + " " + splitBtn + coversHtml + "</span>" +
          "<span class='days'>" + dayLabel + "</span></label>";
      });
    });
    el.innerHTML = html;
    wireDownloads(el);
    el.querySelectorAll("input[type=checkbox]").forEach(function (cb) {
      cb.addEventListener("change", function () {
        state.selected[cb.getAttribute("data-id")] = cb.checked;
        render();
      });
    });
    el.querySelectorAll(".splitbtn").forEach(function (b) {
      b.addEventListener("click", function (ev) {
        ev.preventDefault();
        toggleSplit(b.getAttribute("data-split"));
      });
    });
  }

  function safeResourceLink(s) {
    if (typeof s !== "string" || !/^https?:\/\//i.test(s)) return "";
    try {
      var url = new URL(s);
      return url.protocol === "https:" || url.protocol === "http:" ? url.href : "";
    } catch (e) { return ""; }
  }
  // ---------------- your additions: list, form, TPSP picker ----------------
  function dayLabelFor(days, id) {
    if (state.splits[id]) return "2 half days";
    return days === 0 ? "same day" : days === 0.5 ? "half day" : days === 1 ? "1 day" : days + " days";
  }

  function renderAdditions() {
    var el = document.getElementById("additions");
    if (!el) return;
    var items = state.customItems || [];
    if (!items.length) { el.innerHTML = ""; return; }
    var html = "<h3 style='font-size:16.5px;margin:16px 0 4px;'>Your additions</h3>";
    items.forEach(function (ci) {
      var splitBtn = ci.days >= 1 ?
        "<button type='button' class='mini splitbtn' data-split='" + ci.id + "'>" + (state.splits[ci.id] ? "Unsplit" : "Split") + "</button>" : "";
      var nameHtml, safeLink = safeResourceLink(ci.link);
      if (ci.kind === "tpsp") {
        nameHtml = "<span class='tpsptag'>TPSP</span> " +
          (safeLink ? "<a href='" + esc(safeLink) + "' target='_blank' rel='noopener'>" + esc(ci.title) + "</a>" : esc(ci.title));
      } else {
        nameHtml = "<span class='kind' style='font-size:10.5px;letter-spacing:1.2px;text-transform:uppercase;color:#1f3350;'>Your resource</span> · " + esc(ci.title) +
          (safeLink ? " <a href='" + esc(safeLink) + "' target='_blank' rel='noopener' style='font-size:12.5px;'>link</a>" : "");
      }
      html += "<label class='pick'><input type='checkbox' data-cid='" + ci.id + "'" + (state.selected[ci.id] ? " checked" : "") + ">" +
        "<span>" + nameHtml + splitBtn +
        "<button type='button' class='mini editbtn' data-edit='" + ci.id + "'>Edit</button>" +
        "<button type='button' class='mini delbtn' data-del='" + ci.id + "'>Delete</button>" +
        "<button type='button' class='mini placebtn' data-place='" + ci.id + "'>Place on a day</button>" + coversSpan(ci.bp) + "</span>" +
        "<span class='days'>" + dayLabelFor(ci.days, ci.id) + "</span></label>" +
        "<select class='placepick' data-placepick='" + ci.id + "' style='display:none;' aria-label='Choose a day for this addition'>" +
        "<option value=''>Choose a day…</option></select>";
    });
    el.innerHTML = html;
    el.querySelectorAll("input[type=checkbox]").forEach(function (cb) {
      cb.addEventListener("change", function () {
        state.selected[cb.getAttribute("data-cid")] = cb.checked;
        render();
      });
    });
    el.querySelectorAll(".splitbtn").forEach(function (b) {
      b.addEventListener("click", function (ev) {
        ev.preventDefault();
        toggleSplit(b.getAttribute("data-split"));
      });
    });
    el.querySelectorAll("[data-edit]").forEach(function (b) {
      b.addEventListener("click", function (ev) {
        ev.preventDefault();
        var ci = customById(b.getAttribute("data-edit"));
        if (ci) openItemForm(ci);
      });
    });
    el.querySelectorAll("[data-del]").forEach(function (b) {
      b.addEventListener("click", function (ev) {
        ev.preventDefault();
        deleteCustom(b.getAttribute("data-del"));
      });
    });
    el.querySelectorAll("[data-place]").forEach(function (b) {
      b.addEventListener("click", function (ev) {
        ev.preventDefault();
        var sel = el.querySelector("[data-placepick='" + b.getAttribute("data-place") + "']");
        if (!sel) return;
        if (sel.style.display === "none") {
          // The day list is built when the chooser opens: dates move as
          // the plan is edited, so a list rendered earlier can be stale.
          sel.innerHTML = "<option value=''>Choose a day…</option>" + (L ? L.buckets.map(function (bk, i) {
            return "<option value='" + bk.iso + "'>Day " + (i + 1) + " · " + fmt(bk.date) + "</option>";
          }).join("") : "");
          sel.style.display = "";
          sel.focus();
        } else sel.style.display = "none";
      });
    });
    el.querySelectorAll("[data-placepick]").forEach(function (sel) {
      sel.addEventListener("change", function () {
        if (sel.value) placeAdditionOnDay(sel.getAttribute("data-placepick"), sel.value);
      });
    });
  }

  // "Place on a day": move the addition in the order to where that day's
  // work begins, and pin it to the date. The pin is what holds it there:
  // later drags and steppers move other work around a pinned item, never
  // the item itself. Placing selects the addition first, since an
  // unpicked addition has no place in the order to move.
  function placeAdditionOnDay(id, iso) {
    var ci = customById(id);
    if (!ci) return;
    state.selected[id] = true;
    syncOrder();
    var keys = keysFor(id);
    var rest = state.order.filter(function (k) { return keys.indexOf(k) === -1; });
    var lay = layout(candidateDays());
    var target = null, beforeKeys = [];
    lay.buckets.forEach(function (b) {
      if (b.iso === iso) target = b;
      else if (b.iso < iso) b.entries.forEach(function (e) { beforeKeys.push(e.key); });
    });
    var insertAt = -1;
    if (target && target.entries.length) insertAt = rest.indexOf(target.entries[0].key);
    if (insertAt === -1) {
      insertAt = 0;
      beforeKeys.forEach(function (k) {
        var i = rest.indexOf(k);
        if (i !== -1 && i + 1 > insertAt) insertAt = i + 1;
      });
    }
    keys.forEach(function (k, i) { rest.splice(insertAt + i, 0, k); });
    state.order = rest;
    SEC().pins[keys[0]] = iso;
    render();
  }

  function deleteCustom(id) {
    var ci = customById(id);
    if (!ci) return;
    if (!window.confirm("Remove \"" + ci.title + "\" from your plan? It comes off the calendar, the plate, and your coverage tags.")) return;
    state.customItems = state.customItems.filter(function (c) { return c.id !== id; });
    delete state.selected[id];
    delete state.splits[id];
    if (state.order) state.order = state.order.filter(function (k) { return baseId(k) !== id; });
    state.sections.forEach(function (s) {
      Object.keys(s.pins).forEach(function (k) { if (baseId(k) === id) delete s.pins[k]; });
    });
    if (editingId === id) closeItemForm();
    render();
  }

  // One form serves both adding your own resource and editing any addition.
  var editingId = null;
  function buildBpChecks() {
    var el = document.getElementById("own-bp");
    if (!el || el.children.length) return;
    el.innerHTML = Object.keys(BP).map(Number).sort(function (a, b) { return a - b; }).map(function (t) {
      return "<label class='bpcheck'><input type='checkbox' data-bp='" + t + "'> Entry " + t + " · " + BP[t] + "</label>";
    }).join("");
  }
  function openItemForm(ci) {
    buildBpChecks();
    editingId = ci ? ci.id : null;
    document.getElementById("own-form-title").textContent = ci ? "Edit resource" : "Add your own resource";
    document.getElementById("own-save").textContent = ci ? "Save changes" : "Add to my plan";
    document.getElementById("own-name").value = ci ? ci.title : "";
    document.getElementById("own-days").value = String(ci ? ci.days : 1);
    document.getElementById("own-link").value = ci ? (ci.link || "") : "";
    document.getElementById("own-note").value = ci ? (ci.note || "") : "";
    document.getElementById("own-err").textContent = "";
    var tagged = ci ? (ci.bp || []) : [];
    document.querySelectorAll("#own-bp input[type=checkbox]").forEach(function (cb) {
      cb.checked = tagged.indexOf(+cb.getAttribute("data-bp")) !== -1;
    });
    document.getElementById("tpsp-picker").style.display = "none";
    document.getElementById("own-form").style.display = "";
    document.getElementById("own-name").focus();
  }
  function closeItemForm() {
    editingId = null;
    document.getElementById("own-form").style.display = "none";
  }
  function saveItemForm() {
    var title = document.getElementById("own-name").value.trim();
    var err = document.getElementById("own-err");
    if (!title) { err.textContent = "Give the resource a name first."; return; }
    var days = parseFloat(document.getElementById("own-days").value);
    if ([0, 0.5, 1, 2].indexOf(days) === -1) days = 1;
    var link = document.getElementById("own-link").value.trim();
    if (link && !safeResourceLink(link)) { err.textContent = "Enter a full link starting with https:// or leave it blank."; return; }
    var note = document.getElementById("own-note").value.trim();
    var bp = [];
    document.querySelectorAll("#own-bp input[type=checkbox]").forEach(function (cb) {
      if (cb.checked) bp.push(+cb.getAttribute("data-bp"));
    });
    if (editingId) {
      var ci = customById(editingId);
      if (ci) { ci.title = title; ci.days = days; ci.link = link; ci.note = note; ci.bp = bp; }
    } else {
      var nc = { id: newCustomId(), title: title, days: days, kind: "own", link: link, note: note, bp: bp };
      state.customItems.push(nc);
      state.selected[nc.id] = true;
    }
    closeItemForm();
    render();
  }

  function renderTpspList() {
    var el = document.getElementById("tpsp-list");
    if (!el) return;
    var q = (document.getElementById("tpsp-q").value || "").trim().toLowerCase();
    var rows = TPSP_LIST.filter(function (s) {
      return !q || (s.title + " " + s.type + " " + s.meta).toLowerCase().indexOf(q) !== -1;
    });
    el.innerHTML = rows.length ? rows.map(function (s) {
      return "<button type='button' class='tpspitem' data-tpsp='" + s.id + "'><span class='kind'>" +
        (s.dbq ? "TPSP · Premium DBQ" : "TPSP") + "</span> · " + esc(s.title) +
        "<br><span class='small'>" + esc(s.type) + " · " + esc(s.meta) + "</span></button>";
    }).join("") : "<p class='small'>No sources match that search.</p>";
    el.querySelectorAll("[data-tpsp]").forEach(function (b) {
      b.addEventListener("click", function () { addTpsp(b.getAttribute("data-tpsp")); });
    });
  }
  function addTpsp(srcId) {
    var s = TPSP_LIST.filter(function (x) { return x.id === srcId; })[0];
    if (!s) return;
    var ci = {
      id: newCustomId(), title: s.title, days: s.dbq ? 2 : 1, kind: "tpsp",
      link: s.url, note: "", bp: (s.bp || []).slice(), tpspId: s.id
    };
    state.customItems.push(ci);
    state.selected[ci.id] = true;
    document.getElementById("tpsp-added").textContent = "Added: " + s.title + " — it is in Your additions above, already on your calendar.";
    render();
  }

  // ---------------- chips, drag and drop, pins ----------------
  function chipHTML(e) {
    var pinned = !!SEC().pins[e.key];
    var note = (pinned && e.pinMovedFrom) ?
      " <span class='small'>(original pin: " + fmt(P(e.pinMovedFrom)) + "; moved because that date is unavailable or full)</span>" : "";
    var oi = state.order.indexOf(e.key);
    var steppers = "<span class='stepbtns'>" +
      "<button type='button' class='movebtn' data-move='up' data-key='" + e.key + "' title='Move earlier' aria-label='Move earlier'" +
      (oi <= 0 ? " disabled" : "") + ">↑</button>" +
      "<button type='button' class='movebtn' data-move='down' data-key='" + e.key + "' title='Move later' aria-label='Move later'" +
      (oi === -1 || oi >= state.order.length - 1 ? " disabled" : "") + ">↓</button></span>";
    return "<span class='chip" + (pinned ? " pinned" : "") + "' draggable='true' data-key='" + e.key + "'>" +
      "<span class='chipname'>" + (e.item.custom ? esc(e.name) : e.name) + "</span>" + steppers +
      "<button type='button' class='pinbtn' data-pin='" + e.key + "' title='" + (pinned ? "Unpin" : "Pin to this date") + "'>" + (pinned ? "📌" : "📍") + "</button></span>" + note;
  }
  function moveEntryInOrder(key, delta) {
    var i = state.order.indexOf(key);
    var j = i + delta;
    if (i === -1 || j < 0 || j >= state.order.length) return;
    var t = state.order[i];
    state.order[i] = state.order[j];
    state.order[j] = t;
    render();
  }
  function wireChips(root) {
    root.querySelectorAll(".chip").forEach(function (chip) {
      chip.addEventListener("dragstart", function (ev) {
        ev.dataTransfer.setData("text/plain", chip.getAttribute("data-key"));
        ev.dataTransfer.effectAllowed = "move";
        chip.classList.add("dragging");
      });
      chip.addEventListener("dragend", function () { chip.classList.remove("dragging"); });
    });
    root.querySelectorAll("[data-pin]").forEach(function (b) {
      b.addEventListener("click", function () {
        var key = b.getAttribute("data-pin");
        if (SEC().pins[key]) delete SEC().pins[key];
        else if (L && L.placedOn[key]) SEC().pins[key] = L.placedOn[key];
        render();
      });
    });
    root.querySelectorAll("[data-move]").forEach(function (b) {
      b.addEventListener("click", function () {
        var key = b.getAttribute("data-key"), dir = b.getAttribute("data-move");
        moveEntryInOrder(key, dir === "up" ? -1 : 1);
        // Keep focus on the same control after the re-render so keyboard
        // and switch users can repeat the move without starting over.
        var again = document.querySelector(".chip[data-key='" + key + "'] [data-move='" + dir + "']");
        if (again && !again.disabled) { again.focus(); return; }
        var other = document.querySelector(".chip[data-key='" + key + "'] [data-move]:not([disabled])");
        if (other) other.focus();
      });
    });
  }
  function wireDropZones(root) {
    root.querySelectorAll("[data-dropday]").forEach(function (zone) {
      zone.addEventListener("dragover", function (ev) { ev.preventDefault(); ev.dataTransfer.dropEffect = "move"; zone.classList.add("dropok"); });
      zone.addEventListener("dragleave", function () { zone.classList.remove("dropok"); });
      zone.addEventListener("drop", function (ev) {
        ev.preventDefault();
        zone.classList.remove("dropok");
        var key = ev.dataTransfer.getData("text/plain");
        if (key) moveEntryToDay(key, zone.getAttribute("data-dropday"));
      });
    });
  }
  function moveEntryToDay(key, targetIso) {
    if (!L || state.order.indexOf(key) === -1 || L.placedOn[key] === targetIso) return;
    var target = L.buckets.find(function (b) { return b.iso === targetIso; });
    if (!target) return;
    var order = state.order.filter(function (k) { return k !== key; });
    var insertAt = -1;
    if (target && target.entries.length) {
      var firstKey = target.entries[0].key;
      if (firstKey !== key) insertAt = order.indexOf(firstKey);
    }
    if (insertAt === -1) {
      var lastKey = null;
      L.buckets.forEach(function (b) { if (b.iso < targetIso) b.entries.forEach(function (e) { lastKey = e.key; }); });
      insertAt = lastKey ? order.indexOf(lastKey) + 1 : 0;
    }
    order.splice(insertAt, 0, key);
    state.order = order;
    SEC().pins[key] = targetIso;
    render();
  }

  var TYPE_OPTIONS = ["", "Assembly", "Substitute", "Field trip", "Testing", "No class"];
  function dayTypeSelect(iso) {
    var kind = SEC().dayTypes[iso];
    return "<select class='daytype' data-iso='" + iso + "'><option value=''>Normal day</option>" +
      TYPE_OPTIONS.slice(1).map(function (t) {
        return "<option" + (kind === t ? " selected" : "") + ">" + t + "</option>";
      }).join("") + "</select>";
  }
  function wireDayTypes(root) {
    root.querySelectorAll(".daytype").forEach(function (s) {
      s.addEventListener("change", function () {
        var iso = s.getAttribute("data-iso");
        if (s.value) { SEC().dayTypes[iso] = s.value; delete subDaysOf(SEC())[iso]; }
        else delete SEC().dayTypes[iso];
        render();
      });
    });
  }

  // ---------------- sub days: the date holds, the plan does not teach ----------------
  function subMarkBtn(iso) {
    return "<button type='button' class='mini submark' data-submark='" + iso + "'>Mark sub day</button>";
  }
  function subControlsHTML(iso) {
    return "<span class='subctl'>" +
      "<input type='text' class='subnote' data-subnote='" + iso + "' value='" + esc(subNoteOf(SEC(), iso)) +
      "' placeholder='Note for the sub (optional)' aria-label='Note for the substitute'>" +
      "<button type='button' class='mini subunmark' data-subunmark='" + iso + "'>Undo sub day</button></span>";
  }
  function wireSubDays(root) {
    root.querySelectorAll("[data-submark]").forEach(function (b) {
      b.addEventListener("click", function () {
        var iso = b.getAttribute("data-submark");
        subDaysOf(SEC())[iso] = "";
        delete SEC().dayTypes[iso];
        render();
      });
    });
    root.querySelectorAll("[data-subunmark]").forEach(function (b) {
      b.addEventListener("click", function () {
        delete subDaysOf(SEC())[b.getAttribute("data-subunmark")];
        render();
      });
    });
    root.querySelectorAll("[data-subnote]").forEach(function (inp) {
      inp.addEventListener("change", function () {
        var iso = inp.getAttribute("data-subnote");
        if (isSubDay(SEC(), iso)) subDaysOf(SEC())[iso] = inp.value;
        render();
      });
    });
  }

  function renderScheduleList(cand) {
    var sec = SEC();
    var el = document.getElementById("schedule");
    var bucketByIso = {};
    L.buckets.forEach(function (b) { bucketByIso[b.iso] = b; });
    var rows = [];
    cand.days.forEach(function (c) {
      var kind = sec.dayTypes[c.iso];
      if (!c.meet) {
        rows.push("<tr class='marked'><td style='white-space:nowrap;'>" + fmt(c.date) + "</td><td style='color:#5a616d;'>Rotation day · " + esc(sec.name) + " does not meet</td><td></td></tr>");
        return;
      }
      var sel = dayTypeSelect(c.iso);
      if (isSubDay(sec, c.iso)) {
        var snote = subNoteOf(sec, c.iso);
        rows.push("<tr class='marked subday'><td style='white-space:nowrap;'>" + fmt(c.date) + "</td><td><strong>Sub day</strong>" +
          " · the class meets, but no lesson from the plan is taught today; that work moves to later days." +
          (snote ? "<br>Note for the sub: " + esc(snote) : "") +
          hwRowHTML(c.iso) + "</td><td>" + subControlsHTML(c.iso) + "</td></tr>");
      } else if (kind) {
        rows.push("<tr class='marked'><td style='white-space:nowrap;'>" + fmt(c.date) + "</td><td>" + kind +
          " · nothing scheduled; the day's work bumps forward" + hwRowHTML(c.iso) + "</td><td>" + sel + "</td></tr>");
      } else {
        var b = bucketByIso[c.iso];
        var cellEntries = continuationNames(b);
        if (b) cellEntries = cellEntries.concat(b.entries.map(function (e) {
            // Storage items (the Gilded Age) show their filename in the
            // day list; public-file items keep the chip-only look.
            return chipHTML(e) + (e.item.storage ? " " + storageLinkHTML(e.item) : "");
          }));
        var cell = cellEntries.length ? cellEntries.join("<br>") : "<span style='color:#5a616d;'>Flex or review</span>";
        rows.push("<tr data-dropday='" + c.iso + "'><td style='white-space:nowrap;'>" + fmt(c.date) + "</td><td>" + cell + hwRowHTML(c.iso) + "</td><td>" + sel + " " + subMarkBtn(c.iso) + "</td></tr>");
      }
    });
    if (!isSample && cand.testIssue) rows.push("<tr><td></td><td class='warn'>Unit test not scheduled. " + esc(cand.testIssue) + "</td><td></td></tr>");
    else if (!isSample) rows.push("<tr><td style='white-space:nowrap;'><strong>" + fmt(P(sec.test)) + "</strong></td><td><strong>Unit test</strong> (50 points, tagged key)</td><td></td></tr>");
    el.innerHTML = rows.join("");
    wireDayTypes(el); wireSubDays(el); wireHomework(el); wireChips(el); wireDropZones(el); wireDownloads(el);
  }

  function renderWeek(cand) {
    var sec = SEC();
    var el = document.getElementById("weekview");
    var bucketByIso = {};
    L.buckets.forEach(function (b) { bucketByIso[b.iso] = b; });
    var byIso = {};
    cand.days.forEach(function (c) { byIso[c.iso] = c; });
    var first = P(sec.start);
    var monday = new Date(first); monday.setDate(first.getDate() - ((first.getDay() + 6) % 7));
    var test = P(sec.test);
    if (cand.rangeIssue) { el.textContent = cand.rangeIssue; return; }
    var html = (cand.testIssue ? "<p class='small warn'>Unit test not scheduled. " + esc(cand.testIssue) + "</p>" : "") +
      "<div class='wgrid'><div class='whead'>Mon</div><div class='whead'>Tue</div><div class='whead'>Wed</div><div class='whead'>Thu</div><div class='whead'>Fri</div>";
    var d = new Date(monday);
    while (isSample ? d < test : d <= test) {
      var dow = d.getDay();
      if (dow >= 1 && dow <= 5) {
        var iso = ISO(d);
        var c = byIso[iso];
        var kind = sec.dayTypes[iso];
        var cls = "wday", inner = "<div class='wdate'>" + fmt(d) + "</div>";
        if (iso === sec.test && !cand.testIssue) { cls += " testday"; inner += "<div class='wtest'>Unit test</div>"; }
        else if (!c) {
          cls += " offday";
          if (cand.offs[iso]) inner += "<div class='woff'>" + esc(cand.offs[iso]) + "</div>";
        }
        else if (!c.meet) { cls += " offday"; inner += "<div class='woff'>Does not meet (rotation)</div>"; }
        else if (kind) { cls += " marked"; inner += "<div class='wkind'>" + kind + "</div>" + dayTypeSelect(iso); }
        else if (isSubDay(sec, iso)) {
          cls += " subday";
          inner += "<div class='wkind'><strong>Sub day</strong></div>" + subControlsHTML(iso);
          if (hwTextOf(sec, iso)) inner += "<div class='whw'>Homework: " + esc(hwTextOf(sec, iso)) + "</div>";
        }
        else {
          var b = bucketByIso[iso];
          var weekEntries = continuationNames(b).map(function (name) { return "<div class='wflex'>" + name + "</div>"; });
          if (b) weekEntries = weekEntries.concat(b.entries.map(chipHTML));
          inner += weekEntries.length ? weekEntries.join("") : "<div class='wflex'>Flex or review</div>";
          if (hwTextOf(sec, iso)) inner += "<div class='whw'>Homework: " + esc(hwTextOf(sec, iso)) + "</div>";
          inner += dayTypeSelect(iso) + subMarkBtn(iso);
        }
        html += "<div class='" + cls + "'" + (c && c.meet && !kind && !isSubDay(sec, iso) && iso !== sec.test ? " data-dropday='" + iso + "'" : "") + ">" + inner + "</div>";
      }
      d.setDate(d.getDate() + 1);
    }
    html += "</div>";
    el.innerHTML = html;
    wireDayTypes(el); wireSubDays(el); wireChips(el); wireDropZones(el);
  }

  function overflowLabel(e) {
    var name = e.item.custom ? esc(e.name) : e.name;
    if (e.placedIso && e.remainingDays > 0) {
      name += " (" + e.remainingDays + (e.remainingDays === 1 ? " lesson-day remaining)" : " lesson-days remaining)");
    }
    return name;
  }

  function continuationNames(bucket) {
    return (bucket ? bucket.continuations : []).map(function (e) {
      return (e.item.custom ? esc(e.name) : e.name) + " (continued)";
    });
  }

  function renderOverflowNote() {
    var ov = document.getElementById("overflow");
    if (L.overflow.length) {
      ov.innerHTML = "<span class='warn'>" + (isSample ? "These picks do not fit in the sample week" : "These picks do not fit before the test for " + esc(SEC().name)) + ": " +
        L.overflow.map(overflowLabel).join("; ") +
        (isSample ? ". Uncheck an activity or restore a class day.</span>" : ". Uncheck something, unmark a day, split a lesson across two days, or move the test date.</span>");
    } else ov.textContent = "";
  }

  // ---------------- coverage + national topics layer ----------------
  function renderCoverage() {
    var covered = {}, coveredBuiltin = {};
    ITEMS.forEach(function (it) { if (state.selected[it.id]) it.tags.forEach(function (t) { covered[t] = true; coveredBuiltin[t] = true; }); });
    // Entries an addition covers that no picked plate item covers: the
    // coverage is the teacher's own tagging, and the panel says so.
    var customOnly = [];
    (state.customItems || []).forEach(function (ci) {
      if (!state.selected[ci.id]) return;
      (ci.bp || []).forEach(function (t) {
        if (covered[t]) return;
        covered[t] = true;
      });
    });
    (state.customItems || []).forEach(function (ci) {
      if (!state.selected[ci.id]) return;
      (ci.bp || []).forEach(function (t) { if (!coveredBuiltin[t] && customOnly.indexOf(t) === -1) customOnly.push(t); });
    });
    customOnly.sort(function (a, b) { return a - b; });
    var total = Object.keys(BP).length;
    var n = Object.keys(covered).length;
    // What the work actually scheduled before the test covers. Under
    // overflow this is the honest figure for the meter, with the picks
    // figure kept as its own line; the two never blur into one number.
    var placed = {};
    if (L) L.buckets.forEach(function (b) {
      b.entries.forEach(function (e) {
        if (L.overflow.some(function (o) { return o.key === e.key; })) return;
        if (state.splits[e.item.id] && !(L.placedOn[e.item.id + "#a"] && L.placedOn[e.item.id + "#b"])) return;
        (e.item.tags || []).forEach(function (t) { placed[t] = true; });
      });
    });
    var placedN = Object.keys(placed).length;
    var over = !!(L && L.overflow.length);
    document.getElementById("meterfill").style.width = (100 * (over ? placedN : n) / total) + "%";
    document.getElementById("covtext").textContent = n + " of " + total + " blueprint entries covered by your picks";
    document.getElementById("covplaced").textContent = over ?
      (isSample ? "Scheduled this week: " : "Scheduled before the test: ") + placedN + " of " + total + " entries" : "";
    var strip = document.getElementById("covstrip");
    if (strip) strip.textContent = "Coverage: " + (over ? placedN : n) + " of " + total + " entries" +
      (over ? " scheduled · tap for the check" : " · tap for the check");
    document.getElementById("dayuse").textContent = SEC().period === 90 ?
      "Your picks fill " + L.usedDays + " of " + L.usableCount + " usable meetings for " + SEC().name +
      ": " + (L.lessonDays + 1) + " lesson-days · " + L.usedDays + " meetings, with the test day counted in the lesson-days." :
      "Your picks fill " + L.usedDays + " of " + L.usableCount + " usable meeting days for " + SEC().name + ".";
    var gaps = Object.keys(BP).map(Number).filter(function (t) { return !covered[t]; });
    var gel = document.getElementById("gaps");
    if (!gaps.length) {
      gel.innerHTML = "<p class='ok' style='font-size:14px;margin-bottom:0;'>Every blueprint entry is covered by at least one of your picks.</p>";
    } else {
      gel.innerHTML = "<p style='font-size:14px;margin:10px 0 2px;'><strong>Not covered yet</strong></p>" + gaps.map(function (t) {
        // Every unpicked item that covers the entry gets an Add button,
        // not just the first: the teacher picks which one fits.
        var fillers = [];
        ITEMS.forEach(function (it) {
          if (!state.selected[it.id] && it.tags.indexOf(t) !== -1) fillers.push({ id: it.id, name: it.name + " (Lesson " + it.lesson + ")" });
        });
        (state.customItems || []).forEach(function (ci) {
          if (!state.selected[ci.id] && (ci.bp || []).indexOf(t) !== -1) fillers.push({ id: ci.id, name: esc(ci.title) + " (your addition)" });
        });
        if (!fillers.length) return "<div class='gap'>Entry " + t + " · " + BP[t] + "</div>";
        return "<div class='gap'>Entry " + t + " · " + BP[t] + fillers.map(function (f) {
          return "<br><button data-add='" + f.id + "'>Add</button> <span class='small'>Fills it: " + f.name + "</span>";
        }).join("") + "</div>";
      }).join("");
      gel.querySelectorAll("button[data-add]").forEach(function (b) {
        b.addEventListener("click", function () {
          state.selected[b.getAttribute("data-add")] = true;
          renderPicker();
          render();
        });
      });
    }
    if (customOnly.length) {
      gel.insertAdjacentHTML("beforeend",
        "<p style='font-size:14px;margin:10px 0 2px;'><strong>Covered by your additions</strong></p>" +
        customOnly.map(function (t) {
          return "<div class='gap'>Entry " + t + " · " + BP[t] + " †</div>";
        }).join("") +
        "<p class='small' style='margin:4px 0 0;'>† Covered by an item you added and tagged yourself.</p>");
    }
    renderTopics(placed);
  }

  function renderTopics(placed) {
    var el = document.getElementById("standards");
    if (!el) return;
    // Topics count only what the scheduled work teaches, and a topic no
    // item in this unit can teach is not part of this unit's count.
    var teachable = {};
    ITEMS.forEach(function (it) {
      it.tags.forEach(function (t) { (BP_TOPIC[t] || []).forEach(function (s) { teachable[s] = true; }); });
    });
    var hit = {};
    Object.keys(placed || {}).forEach(function (t) {
      (BP_TOPIC[t] || []).forEach(function (s) { hit[s] = true; });
    });
    Object.keys(hit).forEach(function (s) { teachable[s] = true; });
    var nums = Object.keys(TOPICS).map(Number).sort(function (a, b) { return a - b; });
    var teachNums = nums.filter(function (s) { return teachable[s]; });
    var hitNums = teachNums.filter(function (s) { return hit[s]; });
    el.innerHTML = "<p style='font-size:14px;margin:0 0 4px;'><strong>" + U.topicsHead + "</strong></p>" +
      "<p class='small' style='margin:0 0 8px;'>For reference, not a second score: the blueprint check above is the score. " +
      "The themes US History courses teach for this era in every state, not tied to one state's standards. Check them against your own framework. " +
      "Your scheduled work touches " + hitNums.length + " of the " + teachNums.length + " topics this unit teaches.</p>" +
      nums.map(function (s) {
        if (!teachable[s]) {
          return "<div class='gap' style='opacity:.62;'><strong>Topic " + s + "</strong> · " + TOPICS[s].label +
            "<br><span class='small'>" + (TOPICS[s].note || "Not part of this unit.") + "</span></div>";
        }
        if (hit[s]) return "<div class='gap'><strong>Topic " + s + "</strong> · " + TOPICS[s].label + "</div>";
        var filler = ITEMS.filter(function (it) {
          return !state.selected[it.id] && it.tags.some(function (t) { return (BP_TOPIC[t] || []).indexOf(s) !== -1; });
        })[0];
        return "<div class='gap' style='opacity:.62;'><strong>Topic " + s + "</strong> · " + TOPICS[s].label +
          "<br><span class='small'>" + (TOPICS[s].note || "Not covered by your scheduled work yet.") + "</span>" +
          (filler ? " <button data-add='" + filler.id + "'>Add</button> <span class='small'>Fills it: " + filler.name + " (Lesson " + filler.lesson + ")</span>" : "") + "</div>";
      }).join("");
    el.querySelectorAll("button[data-add]").forEach(function (b) {
      b.addEventListener("click", function () {
        state.selected[b.getAttribute("data-add")] = true;
        renderPicker();
        render();
      });
    });
  }

  // ---------------- print: week view and sub plan ----------------
  function printHTML(title, body) {
    document.getElementById("printArea").innerHTML =
      "<h1 style='font-family:Georgia,serif;font-size:24px;margin:0 0 4px;'>" + title + "</h1>" + body;
    window.print();
  }
  function fileBase(f) { return f.split("/").pop(); }

  // A plan with picks that did not fit says so on its face: the banner
  // names everything unplaced, so nobody reading the paper (a substitute
  // above all) mistakes a partial plan for the whole plan.
  function unplacedBanner() {
    if (!L || !L.overflow.length) return "";
    return "<p style='border:2px solid #000;padding:8px 10px;margin:0 0 12px;'><strong>" +
      (isSample ? "Not scheduled this week" : "Not scheduled before the test") + ":</strong> " +
      L.overflow.map(overflowLabel).join("; ") +
      ". The plan below shows only the portions that fit.</p>";
  }

  function buildWeekPrint() {
    var sec = SEC();
    var bucketByIso = {};
    L.buckets.forEach(function (b) { bucketByIso[b.iso] = b; });
    var rows = ["<table class='ptable'><tr><th style='width:22%;'>Day</th><th>Plan</th></tr>"];
    var cand = candidateDays();
    cand.days.forEach(function (c) {
      var kind = sec.dayTypes[c.iso];
      var b = bucketByIso[c.iso];
      var meetingEntries = continuationNames(b).concat(b ? b.entries.map(function (e) { return e.item.custom ? esc(e.name) : e.name; }) : []);
      var cell = !c.meet ? "Rotation day · " + esc(sec.name) + " does not meet" :
        kind ? kind + " · no lessons" :
        isSubDay(sec, c.iso) ? "Sub day" + (subNoteOf(sec, c.iso) ? " · " + esc(subNoteOf(sec, c.iso)) : " · no lessons") :
        (meetingEntries.length ? meetingEntries.join("<br>") : "Flex or review");
      var hwp = c.meet ? hwTextOf(sec, c.iso) : "";
      if (hwp) cell += "<br>Homework: " + esc(hwp);
      rows.push("<tr><td>" + fmt(c.date) + "</td><td>" + cell + "</td></tr>");
    });
    if (!isSample && cand.testIssue) rows.push("<tr><td></td><td>Unit test not scheduled. " + esc(cand.testIssue) + "</td></tr>");
    else if (!isSample) rows.push("<tr><td><strong>" + fmt(P(sec.test)) + "</strong></td><td><strong>Unit test</strong> (50 points)</td></tr>");
    rows.push("</table>");
    return unplacedBanner() + rows.join("");
  }
  function buildSubPlan() {
    var sec = SEC();
    var bucketByIso = {};
    L.buckets.forEach(function (b) { bucketByIso[b.iso] = b; });
    var cand = candidateDays();
    var out = ["<p style='margin:0 0 12px;'>Substitute plan for " + U.name + " · " + esc(sec.name) + ", " + fmt(P(sec.start)) + " to " + fmt(P(sec.test)) +
      ". Every material is a PDF named below, printed with the teacher key at the back of each document. Guided notes run alongside their reading on the same day.</p>"];
    var banner = unplacedBanner();
    if (banner) out.push(banner);
    cand.days.forEach(function (c) {
      var kind = sec.dayTypes[c.iso];
      var b = bucketByIso[c.iso];
      out.push("<h2 style='font-family:Georgia,serif;font-size:17px;margin:14px 0 2px;'>" + fmt(c.date) + "</h2>");
      if (!c.meet) { out.push("<p style='margin:0;'>This section does not meet today (rotation).</p>"); return; }
      if (kind) { out.push("<p style='margin:0;'>" + kind + ". No new material scheduled.</p>"); var hk = hwPrintP(sec, c.iso); if (hk) out.push(hk); return; }
      if (isSubDay(sec, c.iso)) {
        var sn = subNoteOf(sec, c.iso);
        out.push("<p style='margin:0;'><strong>Sub day.</strong> " +
          (sn ? "Note from the teacher: " + esc(sn)
              : "Instructions for the substitute: ________________________________________") + "</p>");
        var hs = hwPrintP(sec, c.iso); if (hs) out.push(hs);
        return;
      }
      var continuations = continuationNames(b);
      if (continuations.length) out.push("<p style='margin:0;'>" + continuations.join("; ") + "</p>");
      if (!b || !b.entries.length) {
        if (!continuations.length) out.push(
          "<p style='margin:0;'>Flex or review day. Students can use the study guide.</p>");
        var hf = hwPrintP(sec, c.iso); if (hf) out.push(hf);
        return;
      }
      out.push("<ul style='margin:2px 0 0;padding-left:18px;'>" + b.entries.map(function (e) {
        if (e.item.custom) {
          var det = e.item.link || e.item.note || "";
          return "<li>" + esc(e.name) + (det ? " <span style='color:#555;'>(" + esc(det) + ")</span>" : "") + "</li>";
        }
        return "<li>" + e.name + " <span style='color:#555;'>(Lesson " + e.item.lesson + " · " + e.item.kind + " · " + fileNameOf(e.item) + ")</span></li>";
      }).join("") + "</ul>");
      var he = hwPrintP(sec, c.iso); if (he) out.push(he);
    });
    if (cand.testIssue) out.push("<p>Unit test not scheduled. " + esc(cand.testIssue) + "</p>");
    else out.push("<h2 style='font-family:Georgia,serif;font-size:17px;margin:14px 0 2px;'>" + fmt(P(sec.test)) + "</h2><p style='margin:0;'><strong>Unit test</strong>, 50 points (" + U.testName + "). Answer key with blueprint tags is at the back of the test document.</p>");
    out.push("<p style='margin-top:16px;color:#555;'>Prepared with the Humanities Curriculum Group planner.</p>");
    return out.join("");
  }

  // ---------------- calendar (.ics) export ----------------
  function icsEscape(s) { return String(s).replace(/\\/g, "\\\\").replace(/;/g, "\\;").replace(/,/g, "\\,").replace(/\n/g, "\\n"); }
  function icsDate(iso) { return iso.replace(/-/g, ""); }
  function nextDayISO(iso) { var d = P(iso); d.setDate(d.getDate() + 1); return ISO(d); }
  function exportICS() {
    var sec = SEC();
    var stamp = new Date().toISOString().replace(/[-:]/g, "").split(".")[0] + "Z";
    var lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Humanities Curriculum Group//Planner//EN", "CALSCALE:GREGORIAN"];
    L.buckets.forEach(function (b) {
      if (!b.entries.length && !b.continuations.length) return;
      var continuations = b.continuations.map(function (e) { return e.name + " (continued)"; });
      var title = continuations.concat(b.entries.map(function (e) { return e.name; })).join(" + ");
      var desc = continuations.concat(b.entries.map(function (e) {
        if (e.item.custom) {
          var parts = [e.name];
          if (e.item.link) parts.push(e.item.link);
          if (e.item.note) parts.push(e.item.note);
          return parts.join("\n");
        }
        return e.item.kind + " · Lesson " + e.item.lesson + " · " + fileNameOf(e.item);
      })).join("\n");
      var hwi = hwTextOf(sec, b.iso);
      if (hwi) desc += "\nHomework: " + hwi;
      lines.push("BEGIN:VEVENT", "UID:hcg-" + U.id + "-" + sec.name.replace(/\W+/g, "") + "-" + b.iso + "@humanitiescurriculumgroup.web.app",
        "DTSTAMP:" + stamp, "DTSTART;VALUE=DATE:" + icsDate(b.iso), "DTEND;VALUE=DATE:" + icsDate(nextDayISO(b.iso)),
        "SUMMARY:" + icsEscape(U.shortName + " (" + sec.name + "): " + title),
        "DESCRIPTION:" + icsEscape(desc), "END:VEVENT");
    });
    if (!candidateDays().testIssue) lines.push("BEGIN:VEVENT", "UID:hcg-" + U.id + "-" + sec.name.replace(/\W+/g, "") + "-test-" + sec.test + "@humanitiescurriculumgroup.web.app",
      "DTSTAMP:" + stamp, "DTSTART;VALUE=DATE:" + icsDate(sec.test), "DTEND;VALUE=DATE:" + icsDate(nextDayISO(sec.test)),
      "SUMMARY:" + icsEscape(U.shortName + " (" + sec.name + "): Unit test"),
      "DESCRIPTION:" + icsEscape("50 points. Answer key with blueprint tags at the back of " + U.testName + "."), "END:VEVENT");
    lines.push("END:VCALENDAR");
    var blob = new Blob([lines.join("\r\n")], { type: "text/calendar" });
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = U.icsSlug + "-" + sec.name.replace(/\W+/g, "-").toLowerCase() + ".ics";
    a.click();
    URL.revokeObjectURL(a.href);
  }

  // ---------------- share link + export / import ----------------
  function shareLink() {
    var payload = { v: 4, unit: unitId, selected: state.selected, order: state.order, splits: state.splits, sections: state.sections, active: state.active, customItems: state.customItems };
    var enc = btoa(unescape(encodeURIComponent(JSON.stringify(payload)))).replace(/\+/g, "-").replace(/\//g, "_");
    var url = location.origin + location.pathname + (unitId === "pe" ? "" : "?unit=" + unitId) + "#plan=" + enc;
    function done(ok) {
      var note = document.getElementById("share-note");
      note.textContent = ok ?
        "Share link copied. Anyone who opens it gets this exact plan (sections, dates, pins, picks) loaded in their browser; nothing is uploaded." :
        "Copy this link: " + url;
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(function () { done(true); }, function () { done(false); });
    } else done(false);
  }
  function exportPlan() {
    var out = Object.assign({}, state, { unit: unitId });
    var blob = new Blob([JSON.stringify(out, null, 2)], { type: "application/json" });
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = U.exportFile;
    a.click();
    URL.revokeObjectURL(a.href);
  }
  function importPlan(file) {
    function rejected() { window.alert("This file did not contain a supported " + U.shortName + " unit plan. Your existing plan was not changed."); }
    if (isSample || !file || file.size > 5000000) { rejected(); return; }
    var r = new FileReader();
    r.onerror = rejected;
    r.onload = function () {
      var obj;
      try { obj = JSON.parse(r.result); } catch (e) { rejected(); return; }
      if (!supportedPlan(obj, true)) { rejected(); return; }
      if ((hasStoredPlan || unreadableDevicePlan) &&
          !window.confirm("Replace this unit’s existing plan with the file? Choose Cancel to keep it. You can export your existing plan first.")) return;
      usePlan(obj);
      unreadableDevicePlan = false;
      inputsBound = -1; // The old date fields still show the previous plan.
      closeItemForm();
      renderPicker();
      render();
    };
    r.readAsText(file);
  }


  // ---------------- unit switcher + test panel ----------------
  function renderUnitSwitch() {
    var el = document.getElementById("unit-switch");
    if (el) {
      el.innerHTML = Object.keys(UNITS).map(function (id) {
        return "<button type='button' class='mini sectab" + (id === unitId ? " on" : "") + "' data-unit='" + id + "'>" + UNITS[id].name + "</button>";
      }).join("");
      el.querySelectorAll("[data-unit]").forEach(function (b) {
        b.addEventListener("click", function () {
          var id = b.getAttribute("data-unit");
          if (id === unitId) return;
          // A full reload keeps the two units' state handling identical:
          // the planner boots again with the other unit's key and data.
          location.search = id === "pe" ? "" : "?unit=" + id;
        });
      });
    }
    var nm = document.getElementById("unit-name");
    if (nm) nm.textContent = U.name;
    var eq = document.getElementById("unit-eq");
    if (eq) eq.textContent = "Essential question: " + U.essentialQuestion;
    var ry = document.getElementById("unit-rycal");
    if (ry) {
      ry.innerHTML = U.rycalDeck ?
        "Student vocabulary review: post the <a href='" + U.rycalDeck + "' target='_blank' rel='noopener'>Rycal deck for this unit</a> (" + U.rycalDeck + ") on day one, so students enter the test date early and Rycal paces short spaced sessions across the whole unit." : "";
    }
    var intro = document.getElementById("tpsp-intro");
    if (intro) intro.textContent = U.tpspIntro;
  }
  function renderTest() {
    var el = document.getElementById("test-action");
    if (!el) return;
    if (U.testFile) {
      el.innerHTML = "<a href='" + U.testFile + "'>Download the unit test (PDF)</a>";
      return;
    }
    // All-Access test (the Gilded Age, Imperialism and World War I): the
    // gated download appears for entitled accounts; everyone else gets
    // the honest pointer to that unit's own page.
    if (isEntitled()) {
      el.innerHTML = "<a href='#' class='ga-dl' data-storage='" + U.testStorage + "'>Download the unit test (PDF)</a>";
      wireDownloads(el);
    } else {
      el.innerHTML = U.name + " unit test is part of All-Access. Subscribers download it from the <a href='" + (U.unitPage || "gilded-era.html") + "'>" + U.shortName + " unit page</a>.";
    }
  }

  // ---------------- render root ----------------
  var deviceSaved = false;
  function paintSaveNote() {
    var note = document.getElementById("save-note");
    if (!note) return;
    if (isSample) {
      note.textContent = !draftKey ? "Changes here don’t touch your saved plans or sync online."
        : (deviceSaved ? "Sample copy saved in this browser only. Bookmark this page to return."
          : "This browser couldn't save your latest changes. Keep this tab open or print your plan.");
      return;
    }
    if (unreadableDevicePlan) {
      note.textContent = "This browser could not read your saved plan. It has not been overwritten; new edits are not saved. Check Planner backups or export these edits.";
      return;
    }
    note.textContent = deviceSaved
      ? (window.HCGAuth && window.HCGAuth.plannerSaveStatus ? window.HCGAuth.plannerSaveStatus() : "Saved in this browser. Sign in to sync across devices.")
      : "This browser couldn't save your latest changes. Export the plan before leaving.";
  }
  window.addEventListener("hcgplansync", paintSaveNote);

  function savePayload() {
    // totalDays stays in lesson-days (content plus the test day): the year
    // planner and the home page read it that way. totalMeetings is the
    // number of meeting dates the content occupies in the active section,
    // which is smaller than the lesson-day count on a block schedule.
    return { selected: state.selected, order: state.order, splits: state.splits, view: state.view,
             active: state.active, sections: state.sections, customItems: state.customItems,
             totalDays: L.lessonDays + (L.testScheduled ? 1 : 0), totalMeetings: L.usedDays };
  }
  function save() {
    if (isSample && !draftKey || unreadableDevicePlan) { paintSaveNote(); return; }
    try {
      localStorage.setItem(isSample ? draftKey : KEY, JSON.stringify(savePayload()));
      deviceSaved = true;
      if (!isSample) hasStoredPlan = true;
    }
    catch (e) { deviceSaved = false; }
    paintSaveNote();
  }
  var inputsBound = -1; // which section the date inputs currently belong to
  function render(holdSave) {
    var sec = SEC();
    if (inputsBound === state.active) {
      sec.start = startEl.value || sec.start;
      sec.test = testEl.value || sec.test;
    }
    syncOrder();
    renderSections();
    renderAdditions();
    var cand = candidateDays();
    renderPacing(cand);
    L = layout(cand);
    L.testScheduled = !isSample && !cand.testIssue;
    var listEl = document.getElementById("schedule");
    var weekEl = document.getElementById("weekview");
    if (state.view === "week") {
      listEl.style.display = "none"; weekEl.style.display = "";
      renderWeek(cand);
    } else {
      listEl.style.display = ""; weekEl.style.display = "none";
      renderScheduleList(cand);
    }
    renderOverflowNote();
    renderCoverage();
    if (isSample) {
      document.getElementById("sample-swap").value =
        state.selected["l3-reading"] && state.selected["l3-notes"] && !state.selected["l3-activity"] ? "l3-reading" :
        state.selected["l3-activity"] && !state.selected["l3-reading"] && !state.selected["l3-notes"] ? "l3-activity" : "";
    } else renderTest();
    if (holdSave !== true) save();
    else paintSaveNote();
    document.querySelectorAll("[data-view]").forEach(function (b) {
      b.classList.toggle("on", b.getAttribute("data-view") === state.view);
    });
    inputsBound = state.active;
    syncInputs();
  }

  function syncInputs() {
    startEl.value = SEC().start;
    testEl.value = SEC().test;
    rotEl.value = SEC().rotation;
    periodEl.value = String(SEC().period);
  }

  startEl.addEventListener("change", function () {
    if (isSample && startEl.value && startEl.value !== SEC().start) {
      var nextEnd = /^(19[0-9]{2}|20[0-9]{2}|2100)-/.test(startEl.value) && sampleEnd(startEl.value);
      if (nextEnd) testEl.value = nextEnd;
      else startEl.value = SEC().start;
    }
    render();
  });
  testEl.addEventListener("change", render);
  rotEl.addEventListener("change", function () { SEC().rotation = rotEl.value; render(); });
  periodEl.addEventListener("change", function () { SEC().period = +periodEl.value === 90 ? 90 : 45; render(); });
  document.querySelectorAll("[data-view]").forEach(function (b) {
    b.addEventListener("click", function () { state.view = b.getAttribute("data-view"); render(); });
  });
  document.getElementById("print-week").addEventListener("click", function () {
    printHTML(U.name + " · " + esc(SEC().name), buildWeekPrint());
  });
  document.getElementById("covstrip").addEventListener("click", function () {
    var panel = document.getElementById("covpanel");
    if (panel) panel.scrollIntoView({ behavior: "smooth", block: "start" });
  });
  document.getElementById("print-sub").addEventListener("click", function () {
    printHTML("Substitute Plan · " + U.name + " · " + esc(SEC().name), buildSubPlan());
  });
  var resetPins = document.getElementById("reset-pins");
  if (resetPins) resetPins.addEventListener("click", function () {
    if (!Object.keys(SEC().pins).length || !window.confirm("Clear the lesson pins in this section? Picks, lesson order, dates, and other sections stay the same.")) return;
    SEC().pins = {};
    render();
  });
  document.getElementById("export-ics").addEventListener("click", exportICS);
  document.getElementById("share-plan").addEventListener("click", shareLink);
  document.getElementById("export-plan").addEventListener("click", exportPlan);
  document.getElementById("btn-add-own").addEventListener("click", function () { openItemForm(null); });
  document.getElementById("own-teaser-link").addEventListener("click", function (ev) {
    ev.preventDefault();
    openItemForm(null);
    var f = document.getElementById("own-form");
    if (f && f.scrollIntoView) f.scrollIntoView({ behavior: "smooth", block: "center" });
  });
  document.getElementById("own-save").addEventListener("click", saveItemForm);
  document.getElementById("own-cancel").addEventListener("click", closeItemForm);
  document.getElementById("btn-add-tpsp").addEventListener("click", function () {
    closeItemForm();
    var pk = document.getElementById("tpsp-picker");
    var show = pk.style.display === "none";
    pk.style.display = show ? "" : "none";
    if (show) { renderTpspList(); document.getElementById("tpsp-q").focus(); }
  });
  document.getElementById("tpsp-q").addEventListener("input", renderTpspList);
  document.getElementById("tpsp-close").addEventListener("click", function () {
    document.getElementById("tpsp-picker").style.display = "none";
  });
  document.getElementById("import-plan").addEventListener("change", function () {
    var file = this.files[0];
    this.value = ""; // Allow retrying the same file after cancel or validation.
    if (file) importPlan(file);
  });
  if (sharedLoaded) {
    var sn = document.getElementById("shared-note");
    if (sn) { sn.style.display = ""; }
  }
  if (isSample) {
    document.documentElement.classList.add("planner-sample");
    document.title = (draftKey ? "Saved Progressive Era Sample Week" : "Progressive Era Sample Week") + " | Humanities Curriculum Group";
    document.getElementById("planner-heading").textContent = draftKey ? "Your Progressive Era sample copy" : "Try the Progressive Era sample week";
    document.getElementById("start-label").textContent = "First day of the sample";
    startEl.min = "1900-01-01";
    startEl.max = "2100-12-31";
    document.getElementById("sample-tools").hidden = false;
    document.getElementById("sample-lesson-controls").hidden = false;
    document.getElementById("sample-schedule-intro").hidden = false;
    document.getElementById("sample-picker-intro").hidden = false;
    document.getElementById("picker-heading").textContent = "Choose activities";
    document.getElementById("schedule-heading").textContent = "Sample calendar";
    var pickerPanel = document.getElementById("picker-panel");
    pickerPanel.parentNode.insertBefore(document.getElementById("schedule-panel"), pickerPanel);
    var copyButton = document.getElementById("sample-copy");
    if (draftKey) {
      copyButton.hidden = true;
      document.getElementById("sample-fresh").hidden = false;
      document.getElementById("sample-description").textContent = "Edit this copy or print it. It is separate from your regular unit plans and is never synced.";
    } else {
      copyButton.addEventListener("click", function () {
        try {
          var id = typeof crypto.randomUUID === "function" ? crypto.randomUUID() :
            Date.now().toString(36) + "-" + Math.random().toString(36).slice(2) + "-" + Math.random().toString(36).slice(2);
          var key = draftPrefix + id;
          if (localStorage.getItem(key) !== null) throw new Error("A copy key already exists");
          var json = JSON.stringify(savePayload());
          localStorage.setItem(key, json);
          if (localStorage.getItem(key) !== json) throw new Error("Could not verify sample copy");
          location.assign(location.pathname + "?sample=progressive-era-week&draft=" + encodeURIComponent(id));
        } catch (e) {
          document.getElementById("sample-copy-status").textContent = "This browser couldn’t save a copy. Your edits remain here; you can print the plan.";
        }
      });
    }
    document.getElementById("sample-swap").addEventListener("change", function () {
      if (this.value !== "l3-reading" && this.value !== "l3-activity") return;
      var reading = this.value === "l3-reading";
      var previous = ["l3-reading", "l3-notes", "l3-activity"];
      var index = state.order.findIndex(function (key) { return previous.indexOf(baseId(key)) !== -1; });
      state.order = state.order.filter(function (key) { return previous.indexOf(baseId(key)) === -1; });
      if (index < 0) index = state.order.length;
      var replacements = reading ? ["l3-reading", "l3-notes"] : ["l3-activity"];
      state.order.splice.apply(state.order, [index, 0].concat(replacements));
      previous.forEach(function (id) {
        state.selected[id] = replacements.indexOf(id) !== -1;
        delete state.splits[id];
        state.sections.forEach(function (sec) {
          delete sec.pins[id];
          delete sec.pins[id + "#a"];
          delete sec.pins[id + "#b"];
        });
      });
      renderPicker();
      render();
    });
  } else renderUnitSwitch();
  // auth.js loads after this script; the hook lets it re-render the
  // Storage download controls once an account's entitlement is known.
  window.HCGPlannerRefresh = function () { renderPicker(); render(true); };
  syncInputs();
  renderPicker();
  render();
})();
