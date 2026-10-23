(function () {
  var KEY = "hcg_year_v1";
  var UNITS = [
    { id: "u1", name: "Colonial America", days: 18, color: "#8a6d3b", planKey: "hcg_unit_ca_v1", planHref: "planner.html?unit=ca" },
    { id: "u2", name: "The Founding", days: 18, color: "#5b7553", planKey: "hcg_unit_fd_v1", planHref: "planner.html?unit=fd" },
    { id: "u3", name: "Early Republic and Expansion", days: 18, color: "#4f7a72", planKey: "hcg_unit_er_v1", planHref: "planner.html?unit=er" },
    { id: "u4", name: "Jackson and Reform", days: 18, color: "#54708c", planKey: "hcg_unit_jr_v1", planHref: "planner.html?unit=jr" },
    { id: "u5", name: "Sectional Crisis and Civil War", days: 18, color: "#6d5a7e", planKey: "hcg_unit_sc_v1", planHref: "planner.html?unit=sc" },
    { id: "u6", name: "Reconstruction", days: 18, color: "#946b54", planKey: "hcg_unit_rc_v1", planHref: "planner.html?unit=rc" },
    { id: "u7", name: "The Gilded Age", days: 18, color: "#7a7a52", planKey: "hcg_unit_ga_v1", planHref: "planner.html?unit=ga" },
    { id: "pe", name: "The Progressive Era", days: 18, color: "#b4552d", live: true, planKey: "hcg_unit_v1", planHref: "planner.html" },
    { id: "wwi", name: "Imperialism and World War I", days: 18, color: "#9c3848", planKey: "hcg_unit_wwi_v1", planHref: "planner.html?unit=wwi" },
    { id: "u9", name: "The Twenties", days: 18, color: "#4a6b8a", planKey: "hcg_unit_tw_v1", planHref: "planner.html?unit=tw" },
    { id: "u10", name: "Depression and New Deal", days: 18, color: "#767c4f", planKey: "hcg_unit_dp_v1", planHref: "planner.html?unit=dp" },
    { id: "u11", name: "World War II", days: 18, color: "#7d4f4f", planKey: "hcg_unit_ww2_v1", planHref: "planner.html?unit=ww2" },
    { id: "u12", name: "The Cold War", days: 18, color: "#4f6185", planKey: "hcg_unit_cw_v1", planHref: "planner.html?unit=cw" },
    { id: "u13", name: "Civil Rights", days: 18, color: "#5d7a5d", planKey: "hcg_unit_cr_v1", planHref: "planner.html?unit=cr" },
    { id: "u14", name: "Modern America", days: 18, color: "#83755a", planKey: "hcg_unit_ma_v1", planHref: "planner.html?unit=ma" },
    { id: "u15", name: "Course Review", days: 10, color: "#7a4a63", planKey: "hcg_unit_rv_v1", planHref: "planner.html?unit=rv" },
    { id: "u16", name: "Early Course Review", days: 5, color: "#47624a", planKey: "hcg_unit_re_v1", planHref: "planner.html?unit=re" },
    { id: "u17", name: "Modern Course Review", days: 7, color: "#33526b", planKey: "hcg_unit_rm_v1", planHref: "planner.html?unit=rm" }
  ];

  // US History runs three ways: the full survey in one year, or two parts
  // split at 1877 (the end of Reconstruction). Part 1 ends with Reconstruction;
  // Part 2 opens with the Gilded Age.
  var COURSES = {
    full: ["u1", "u2", "u3", "u4", "u5", "u6", "u7", "pe", "wwi", "u9", "u10", "u11", "u12", "u13", "u14", "u15"],
    early: ["u1", "u2", "u3", "u4", "u5", "u6", "u16"],
    modern: ["u7", "pe", "wwi", "u9", "u10", "u11", "u12", "u13", "u14", "u17"]
  };
  function activeUnits() {
    var ids = COURSES[S.course] || COURSES.full;
    return UNITS.filter(function (u) { return ids.indexOf(u.id) !== -1; });
  }

  function defaults() {
    return {
      // The starter year is Part 1 (to 1877) on purpose: the full survey
      // at full unit lengths asks for more lesson-days than a typical
      // year holds, so a first run starts with a year that fits and a
      // banner saying plainly that these are example dates.
      course: "early",
      starter: true,
      schedule: { period: 45, pattern: "daily" },
      start: "2026-08-24", end: "2027-05-28", exam: "", reviewDays: 5,
      periods: [
        { name: "Quarter 1", end: "2026-10-23" },
        { name: "Quarter 2", end: "2027-01-15" },
        { name: "Quarter 3", end: "2027-03-19" },
        { name: "Quarter 4", end: "2027-05-28" }
      ],
      daysOff: [
        { from: "2026-09-07", to: "2026-09-07", label: "Labor Day", kind: "holiday" },
        { from: "2026-11-03", to: "2026-11-03", label: "PD day (example)", kind: "pd" },
        { from: "2026-11-25", to: "2026-11-27", label: "Thanksgiving break", kind: "break" },
        { from: "2026-12-21", to: "2027-01-01", label: "Winter break", kind: "break" },
        { from: "2027-01-18", to: "2027-01-18", label: "MLK Day", kind: "holiday" },
        { from: "2027-02-15", to: "2027-02-15", label: "Presidents Day", kind: "holiday" },
        { from: "2027-04-05", to: "2027-04-09", label: "Spring break (example)", kind: "break" }
      ],
      unitDays: {},
      pinnedStarts: {}
    };
  }

  // Class schedule: content is paced in lesson-days (one 45-minute lesson).
  // A block of about 90 minutes fits about two lesson-days per meeting, and
  // on an A/B rotation the course meets every other instructional day.
  // Old saves without the field migrate to the 45-minute daily default.
  function normSchedule(s) {
    if (!s.schedule || (s.schedule.period !== 45 && s.schedule.period !== 90) ||
        (s.schedule.pattern !== "daily" && s.schedule.pattern !== "ab")) {
      s.schedule = { period: 45, pattern: "daily" };
    }
  }
  function lessonsPerMeeting() { return S.schedule && S.schedule.period === 90 ? 2 : 1; }
  function meetingDays(days) {
    if (!S.schedule || S.schedule.pattern !== "ab") return days.slice();
    return days.filter(function (d, i) { return i % 2 === 0; });
  }

  var S;
  try { S = JSON.parse(localStorage.getItem(KEY)) || defaults(); }
  catch (e) { S = defaults(); }
  if (!S.unitDays) S.unitDays = {};
  if (!S.pinnedStarts) S.pinnedStarts = {};
  normSchedule(S);

  // ---------- v4: a library of named plans (preps); hcg_year_v1 stays the active plan ----------
  var LIBKEY = "hcg_year_plans_v1";
  var lib = null, planName = "My year plan";
  try { lib = JSON.parse(localStorage.getItem(LIBKEY)); } catch (e) {}
  if (!lib || !lib.plans || !Object.keys(lib.plans).length) {
    lib = { active: planName, plans: {} };
    lib.plans[planName] = S;
  } else {
    planName = lib.active && lib.plans[lib.active] ? lib.active : Object.keys(lib.plans)[0];
    S = lib.plans[planName];
    if (!S.unitDays) S.unitDays = {};
    if (!S.pinnedStarts) S.pinnedStarts = {};
    normSchedule(S);
  }

  // A shared plan link loads as its own plan; the teacher's other plans are untouched.
  var sharedYear = false;
  try {
    if (location.hash.indexOf("#plan=") === 0) {
      var payload = JSON.parse(decodeURIComponent(escape(atob(location.hash.slice(6).replace(/-/g, "+").replace(/_/g, "/")))));
      if (payload && payload.start && payload.end) {
        if (!payload.unitDays) payload.unitDays = {};
        if (!payload.pinnedStarts) payload.pinnedStarts = {};
        normSchedule(payload);
        planName = "Shared plan";
        lib.plans[planName] = payload;
        S = payload;
        sharedYear = true;
        history.replaceState(null, "", location.pathname + location.search);
      }
    }
  } catch (e) {}

  // ---------- date helpers ----------
  function P(iso) { var p = iso.split("-"); return new Date(+p[0], +p[1] - 1, +p[2]); }
  function ISO(d) {
    function z(n) { return (n < 10 ? "0" : "") + n; }
    return d.getFullYear() + "-" + z(d.getMonth() + 1) + "-" + z(d.getDate());
  }
  function fmt(iso) { return P(iso).toLocaleDateString("en-US", { month: "short", day: "numeric" }); }
  function fmtLong(iso) { return P(iso).toLocaleDateString("en-US", { weekday: "short", month: "short", day: "numeric", year: "numeric" }); }

  function offEntry(iso) {
    for (var i = 0; i < S.daysOff.length; i++) {
      var o = S.daysOff[i];
      if (iso >= o.from && iso <= o.to) return o;
    }
    return null;
  }
  function instructionalDays() {
    var out = [], d = P(S.start), end = P(S.end);
    while (d <= end) {
      var dow = d.getDay(), iso = ISO(d);
      if (dow >= 1 && dow <= 5 && !offEntry(iso)) out.push(iso);
      d.setDate(d.getDate() + 1);
    }
    return out;
  }

  function daysFromUnitPlan(key) {
    try {
      var u = JSON.parse(localStorage.getItem(key));
      if (u && u.totalDays) return u.totalDays;
    } catch (e) {}
    return null;
  }
  // Each unit's floor for Fit to year: the lesson-days in its core picks
  // plus the test day, computed from the same registry the unit planner
  // uses. A unit never trims below its core.
  var CORE_MIN = {};
  try {
    Object.keys(window.HCG_UNITS || {}).forEach(function (k) {
      var reg = window.HCG_UNITS[k];
      var sum = 0;
      (reg.items || []).forEach(function (it) { if (it.core) sum += it.days; });
      CORE_MIN[reg.key] = reg.fitMin != null ? reg.fitMin : sum + 1;
    });
  } catch (e) {}
  function coreMin(u) {
    var v = CORE_MIN[u.planKey];
    return v != null ? v : null;
  }

  function unitDays(u) {
    if (S.unitDays[u.id] != null) return { days: S.unitDays[u.id], src: "your number" };
    if (u.planKey) {
      var fromPlan = daysFromUnitPlan(u.planKey);
      if (fromPlan) return { days: fromPlan, src: "from your unit plan" };
      if (u.live) return { days: u.days, src: "default from core picks" };
    }
    return { days: u.days, src: "estimate" };
  }

  // Assign meetings to units; reserve review days before the exam.
  // Unit lengths are lesson-days; a unit needs ceil(lesson-days /
  // lessons-per-meeting) meetings. Ranges hold meeting dates, so under a
  // 45-minute daily schedule they are exactly the instructional days a
  // unit occupies, as before. A pin sets the unit's first meeting: the
  // first meeting day on or after the pinned date.
  var REVIEW_IDS = { u15: true, u16: true, u17: true };
  function assign(days) {
    var reserved = {};
    var lpm0 = lessonsPerMeeting();
    if (S.exam) {
      var before = days.filter(function (d) { return d < S.exam; });
      var take = Math.min(S.reviewDays || 0, before.length);
      // A review unit in the course occupies the run before the exam
      // itself; do not also hold blank review days on top of it.
      activeUnits().forEach(function (u) {
        if (REVIEW_IDS[u.id]) take = Math.max(0, take - Math.ceil(unitDays(u).days / lpm0));
      });
      for (var i = 0; i < take; i++) reserved[before[before.length - 1 - i]] = true;
    }
    var lpm = lessonsPerMeeting();
    var meets = meetingDays(days);
    var byDate = {}, ranges = {}, pinStale = {}, idx = 0;
    activeUnits().forEach(function (u) {
      var need = Math.ceil(unitDays(u).days / lpm), got = [];
      var pin = S.pinnedStarts[u.id];
      if (pin) {
        if (idx < meets.length && meets[idx] > pin) {
          pinStale[u.id] = true; // earlier units already run past the pin; it cannot be honored
        } else {
          while (idx < meets.length && meets[idx] < pin) idx++; // gap meetings stay unassigned
        }
      }
      while (need > 0 && idx < meets.length) {
        var d = meets[idx++];
        if (reserved[d]) continue;
        got.push(d);
        byDate[d] = u;
        need--;
      }
      ranges[u.id] = got;
    });
    var unassigned = meets.filter(function (d) { return !byDate[d] && !reserved[d]; });
    var overflowDays = 0;
    activeUnits().forEach(function (u) {
      overflowDays += Math.max(0, unitDays(u).days - (ranges[u.id] ? ranges[u.id].length : 0) * lpm);
    });
    return { byDate: byDate, ranges: ranges, reserved: reserved, unassigned: unassigned, overflowDays: overflowDays, pinStale: pinStale };
  }

  // ---------- save ----------
  // One save line that tells the truth about sign-in state: signed out,
  // the plan lives in this browser; signed in, it syncs to the account.
  function signedIn() {
    try { return !!(window.HCGAuth && window.HCGAuth.currentUser()); } catch (e) { return false; }
  }
  function saveNoteText() {
    var t = new Date().toLocaleTimeString("en-US", { hour: "numeric", minute: "2-digit" });
    return signedIn() ? "Saved and synced to your account · " + t
                      : "Saved in this browser · " + t + ". Sign in to sync it across devices.";
  }

  function save() {
    localStorage.setItem(KEY, JSON.stringify(S));
    lib.plans[planName] = S;
    lib.active = planName;
    try { localStorage.setItem(LIBKEY, JSON.stringify(lib)); } catch (e) {}
    document.getElementById("saved-note").textContent = saveNoteText();
  }

  function renderSwitcher() {
    var sel = document.getElementById("plan-select");
    sel.innerHTML = Object.keys(lib.plans).map(function (n) {
      return "<option" + (n === planName ? " selected" : "") + ">" + n + "</option>";
    }).join("");
    document.getElementById("plan-del").disabled = Object.keys(lib.plans).length <= 1;
  }

  // ---------- editors ----------
  function renderEditors() {
    document.getElementById("y-course").value = S.course || "full";
    document.getElementById("y-schedule").value = S.schedule.period + "-" + S.schedule.pattern;
    document.getElementById("y-start").value = S.start;
    document.getElementById("y-end").value = S.end;
    document.getElementById("y-exam").value = S.exam || "";
    document.getElementById("y-review").value = S.reviewDays;

    var pe = document.getElementById("periods");
    pe.innerHTML = S.periods.slice().sort(function (a, b) { return a.end < b.end ? -1 : 1; }).map(function (p) {
      var i = S.periods.indexOf(p);
      return "<div class='editrow'><span><strong>" + p.name + "</strong></span><span class='small'>ends " + fmtLong(p.end) +
        "</span><button type='button' class='mini' data-del-period='" + i + "'>Remove</button></div>";
    }).join("") || "<p class='small'>No grading periods yet.</p>";

    var oe = document.getElementById("daysoff");
    oe.innerHTML = S.daysOff.slice().sort(function (a, b) { return a.from < b.from ? -1 : 1; }).map(function (o) {
      var i = S.daysOff.indexOf(o);
      var when = o.from === o.to ? fmtLong(o.from) : fmt(o.from) + " – " + fmtLong(o.to);
      return "<div class='editrow'><span><strong>" + o.label + "</strong> <span class='kindchip'>" + o.kind + "</span></span><span class='small'>" +
        when + "</span><button type='button' class='mini' data-del-off='" + i + "'>Remove</button></div>";
    }).join("") || "<p class='small'>No days off yet.</p>";

    pe.querySelectorAll("[data-del-period]").forEach(function (b) {
      b.addEventListener("click", function () { S.periods.splice(+b.getAttribute("data-del-period"), 1); render(); });
    });
    oe.querySelectorAll("[data-del-off]").forEach(function (b) {
      b.addEventListener("click", function () { S.daysOff.splice(+b.getAttribute("data-del-off"), 1); render(); });
    });
  }

  function renderUnits(A) {
    var el = document.getElementById("units");
    var lpm = lessonsPerMeeting();
    // Units whose test day (the last day of their band) lands after the exam
    // date. Warning only: post-exam classes are sometimes by design.
    var lateUnits = {}, postExam = [];
    if (S.exam) {
      activeUnits().forEach(function (u) {
        var r = A.ranges[u.id] || [];
        if (r.length && r[r.length - 1] > S.exam) {
          lateUnits[u.id] = r[r.length - 1];
          postExam.push({ name: u.name, testIso: r[r.length - 1] });
        }
      });
    }
    el.innerHTML = activeUnits().map(function (u) {
      var info = unitDays(u), r = A.ranges[u.id] || [];
      var when = r.length ? fmt(r[0]) + " – " + fmt(r[r.length - 1]) : "<span class='warn'>does not fit</span>";
      if (lateUnits[u.id]) {
        when += " <span class='warn'>(test day " + fmt(lateUnits[u.id]) +
          " is after your exam " + fmt(S.exam) + ")</span>";
      }
      var pin = S.pinnedStarts[u.id];
      var pinNote = pin ? "<br><span class='small'>📌 start pinned to " + fmt(pin) +
        (A.pinStale && A.pinStale[u.id] ? " (earlier units run past it, so the pin is ignored)"
          : (r.length && r[0] !== pin ? " (first meeting " + fmt(r[0]) + ")" : "")) +
        "</span> <button type='button' class='mini' data-unpin='" + u.id + "'>Unpin</button>" : "";
      var countCell = lpm === 2 ?
        "<input type='number' class='daysin' data-unit='" + u.id + "' min='1' max='60' value='" + info.days + "'> lesson-days · " +
          Math.ceil(info.days / lpm) + (Math.ceil(info.days / lpm) === 1 ? " meeting" : " meetings") :
        "<input type='number' class='daysin' data-unit='" + u.id + "' min='1' max='60' value='" + info.days + "'> days";
      return "<tr><td><span class='swatch' style='background:" + u.color + "'></span>" + u.name +
        (u.planKey ? " <a href='" + u.planHref + "' style='font-size:12.5px;'>plan it</a>" : "") +
        "<br><span class='small'>" + when + " · " + info.src + "</span>" + pinNote + "</td>" +
        "<td style='text-align:right;white-space:nowrap;'>" + countCell +
        (coreMin(u) != null ? "<br><span class='small'>core minimum " + coreMin(u) + "</span>" : "") + "</td></tr>";
    }).join("");
    el.querySelectorAll(".daysin").forEach(function (inp) {
      inp.addEventListener("change", function () {
        var v = parseInt(inp.value, 10);
        if (v > 0) { S.unitDays[inp.getAttribute("data-unit")] = v; render(); }
      });
    });
    el.querySelectorAll("[data-unpin]").forEach(function (b) {
      b.addEventListener("click", function () { delete S.pinnedStarts[b.getAttribute("data-unpin")]; render(); });
    });

    var days = instructionalDays();
    var committed = activeUnits().reduce(function (n, u) {
      return n + Math.min(unitDays(u).days, (A.ranges[u.id] || []).length * lpm);
    }, 0);
    var meetingsUsed = activeUnits().reduce(function (n, u) { return n + (A.ranges[u.id] || []).length; }, 0);
    // The reserve is taken from instructional days, but on an A/B rotation
    // only the reserved days this course actually meets on hold a meeting
    // back; count those, so the total matches what the bands flow around.
    var meetSet = {};
    meetingDays(days).forEach(function (d) { meetSet[d] = true; });
    var reservedCount = Object.keys(A.reserved).filter(function (d) { return meetSet[d]; }).length;
    var rows = [
      "<tr><td>Instructional days in the year</td><td style='text-align:right;'>" + days.length + "</td></tr>"
    ];
    if (S.schedule.pattern === "ab") {
      rows.push("<tr><td>Days this course meets (A/B rotation)</td><td style='text-align:right;'>" + meetingDays(days).length + "</td></tr>");
    }
    rows.push("<tr><td>Held for exam review</td><td style='text-align:right;'>" + reservedCount + "</td></tr>");
    rows.push("<tr><td>Committed to units" + (lpm === 2 ? " (lesson-days)" : "") + "</td><td style='text-align:right;'>" + committed + "</td></tr>");
    if (lpm === 2) {
      rows.push("<tr><td>Meetings used</td><td style='text-align:right;'>" + meetingsUsed + "</td></tr>");
    }
    rows.push("<tr><td>Buffer left" + (S.schedule.pattern === "ab" ? " (meeting days)" : "") + "</td><td style='text-align:right;'>" + A.unassigned.length + "</td></tr>");
    if (A.overflowDays > 0) {
      rows.push("<tr><td colspan='2'><span class='warn'><strong>" + A.overflowDays + " days of units do not fit</strong> in this year. Trim day counts, drop days off that do not apply, or move the last day later.</span></td></tr>");
    }
    document.getElementById("totals").innerHTML = rows.join("");
    // The demand-vs-supply arithmetic in one plain line: what the units
    // ask for against the room the year actually has.
    var demand = activeUnits().reduce(function (n, u) { return n + unitDays(u).days; }, 0);
    var capacity = (meetingDays(days).length - reservedCount) * lpm;
    document.getElementById("demand-line").textContent =
      "Your units ask for " + demand + " lesson-days; your year has " + capacity + " lesson-days of room.";
    var examHtml = S.exam ?
      "Exam on " + fmtLong(S.exam) + ", with " + reservedCount + " review day" + (reservedCount === 1 ? "" : "s") + " held in front of it. Unit bands flow around the reserve." :
      "Add a state test or AP exam date above and the planner holds review days in front of it.";
    if (postExam.length) {
      var listed = postExam.map(function (p) {
        return p.name + " (test day " + fmt(p.testIso) + ")";
      }).join("; ");
      examHtml += " <span class='warn'><strong>" + postExam.length +
        (postExam.length === 1 ? " unit is" : " units are") +
        " scheduled after your exam:</strong> " + listed +
        ". That can be by design. If it is not, move the exam later or trim days earlier in the year.</span>";
    }
    document.getElementById("exam-note").innerHTML = examHtml;

    // period summary
    var ps = document.getElementById("period-summary");
    var sorted = S.periods.slice().sort(function (a, b) { return a.end < b.end ? -1 : 1; });
    var prev = null, prows = [];
    sorted.forEach(function (p) {
      var inP = days.filter(function (d) { return d <= p.end && (prev === null || d > prev); });
      var tests = activeUnits().filter(function (u) {
        var r = A.ranges[u.id] || [];
        return r.length && r[r.length - 1] <= p.end && (prev === null || r[r.length - 1] > prev);
      }).map(function (u) { return u.name.replace("The ", ""); });
      prows.push("<tr><td>" + p.name + "<br><span class='small'>ends " + fmt(p.end) + (tests.length ? " · tests: " + tests.join(", ") : "") +
        "</span></td><td style='text-align:right;'>" + inP.length + " days</td></tr>");
      prev = p.end;
    });
    var rest = days.filter(function (d) { return prev === null || d > prev; });
    if (sorted.length && rest.length) prows.push("<tr><td>After " + sorted[sorted.length - 1].name + "</td><td style='text-align:right;'>" + rest.length + " days</td></tr>");
    ps.innerHTML = prows.join("") || "<tr><td class='small'>Add a grading period to see the year broken down by period.</td></tr>";
  }

  function renderCalendar(A, daysSet) {
    var wrap = document.getElementById("calendar");
    var periodEnds = {};
    S.periods.forEach(function (p) { periodEnds[p.end] = p.name; });
    var months = [], cur = P(S.start); cur.setDate(1);
    var lastMonth = P(S.end); lastMonth.setDate(1);
    while (cur <= lastMonth) { months.push(new Date(cur)); cur.setMonth(cur.getMonth() + 1); }

    wrap.innerHTML = months.map(function (m) {
      var year = m.getFullYear(), mon = m.getMonth();
      var firstDow = new Date(year, mon, 1).getDay();
      var count = new Date(year, mon + 1, 0).getDate();
      var cells = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"].map(function (d) { return "<div class='cal dow'>" + d + "</div>"; }).join("");
      for (var i = 0; i < firstDow; i++) cells += "<div class='cal empty'></div>";
      for (var dnum = 1; dnum <= count; dnum++) {
        var dt = new Date(year, mon, dnum), iso = ISO(dt), dow = dt.getDay();
        var cls = "cal day", title = "", label = "";
        if (dow === 0 || dow === 6) cls += " wknd";
        if (iso < S.start || iso > S.end) cls += " outside";
        var off = offEntry(iso);
        if (off && iso >= S.start && iso <= S.end) { cls += " off"; title = off.label + " (" + off.kind + ")"; }
        var u = A.byDate[iso];
        var bar = "";
        if (u && daysSet[iso]) {
          var r = A.ranges[u.id];
          var isFirst = r[0] === iso, isTest = r[r.length - 1] === iso;
          bar = "<div class='ubar' style='background:" + u.color + "'></div>";
          if (isFirst) label = "<div class='ulab'>" + u.name.replace("The ", "") + "</div>";
          if (isTest) label += "<div class='ulab test'>test</div>";
          title = u.name + (isTest ? " · unit test" : "");
        }
        if (A.reserved[iso]) { cls += " reserved"; title = "Held for exam review"; label = "<div class='ulab'>review</div>"; }
        if (periodEnds[iso]) { cls += " pend"; title = (title ? title + " · " : "") + periodEnds[iso] + " ends"; }
        if (S.exam && iso === S.exam) { cls += " exam"; title = "Exam"; }
        var dragAttrs = (u && daysSet[iso]) ? " data-unit='" + u.id + "' draggable='true'" : "";
        cells += "<div class='" + cls + "' data-iso='" + iso + "'" + dragAttrs + " title='" + title + "'><div class='dnum'>" + dnum + "</div>" + label + bar + "</div>";
      }
      return "<div class='month'><h4>" + m.toLocaleDateString("en-US", { month: "long", year: "numeric" }) + "</h4><div class='mgrid'>" + cells + "</div></div>";
    }).join("");

    // v3 drag: drag a unit's day cell onto a date to pin that unit's start there
    wrap.querySelectorAll("[data-unit]").forEach(function (cell) {
      cell.addEventListener("dragstart", function (ev) {
        ev.dataTransfer.setData("text/plain", cell.getAttribute("data-unit"));
        ev.dataTransfer.effectAllowed = "move";
      });
    });
    wrap.querySelectorAll(".cal.day[data-iso]").forEach(function (cell) {
      cell.addEventListener("dragover", function (ev) { ev.preventDefault(); ev.dataTransfer.dropEffect = "move"; cell.classList.add("dropok"); });
      cell.addEventListener("dragleave", function () { cell.classList.remove("dropok"); });
      cell.addEventListener("drop", function (ev) {
        ev.preventDefault();
        cell.classList.remove("dropok");
        var uid = ev.dataTransfer.getData("text/plain");
        var iso = cell.getAttribute("data-iso");
        if (uid && iso >= S.start && iso <= S.end) { S.pinnedStarts[uid] = iso; render(); }
      });
    });

    document.getElementById("legend").innerHTML = activeUnits().map(function (u) {
      var r = A.ranges[u.id] || [];
      var when = r.length ? fmt(r[0]) + " – " + fmt(r[r.length - 1]) : "does not fit";
      return "<span class='legitem'><span class='swatch' style='background:" + u.color + "'></span>" + u.name + " <span class='small'>" + when + "</span></span>";
    }).join("");
  }

  function render() {
    if (!S.course || !COURSES[S.course]) S.course = "full";
    if (!S.unitDays) S.unitDays = {};
    if (!S.pinnedStarts) S.pinnedStarts = {};
    normSchedule(S);
    var starterNote = document.getElementById("starter-note");
    if (starterNote) starterNote.style.display = S.starter ? "" : "none";
    renderSwitcher();
    renderEditors();
    var days = instructionalDays();
    var A = assign(days);
    var set = {};
    days.forEach(function (d) { set[d] = true; });
    renderUnits(A);
    renderCalendar(A, set);
    save();
  }

  // ---------- wiring ----------
  document.getElementById("y-course").addEventListener("change", function () {
    S.course = this.value;
    render();
  });
  document.getElementById("y-schedule").addEventListener("change", function () {
    var parts = this.value.split("-");
    S.schedule = { period: +parts[0], pattern: parts[1] };
    render();
  });
  ["y-start", "y-end", "y-exam"].forEach(function (id) {
    document.getElementById(id).addEventListener("change", function () {
      S.start = document.getElementById("y-start").value || S.start;
      S.end = document.getElementById("y-end").value || S.end;
      S.exam = document.getElementById("y-exam").value || "";
      // Real dates make the year the teacher's own, not the starter.
      S.starter = false;
      render();
    });
  });
  document.getElementById("y-review").addEventListener("change", function () {
    S.reviewDays = Math.max(0, parseInt(this.value, 10) || 0);
    render();
  });
  document.getElementById("p-add").addEventListener("click", function () {
    var name = document.getElementById("p-name").value.trim();
    var end = document.getElementById("p-end").value;
    if (name && end) { S.periods.push({ name: name, end: end }); document.getElementById("p-name").value = ""; render(); }
  });
  document.getElementById("o-add").addEventListener("click", function () {
    var from = document.getElementById("o-from").value, to = document.getElementById("o-to").value || from;
    var label = document.getElementById("o-label").value.trim();
    var kind = document.getElementById("o-kind").value;
    if (from && label) {
      if (to < from) { var t = from; from = to; to = t; }
      S.daysOff.push({ from: from, to: to, label: label, kind: kind });
      document.getElementById("o-label").value = "";
      render();
    }
  });
  document.getElementById("export").addEventListener("click", function () {
    var blob = new Blob([JSON.stringify(S, null, 2)], { type: "application/json" });
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "hcg-year-plan.json";
    a.click();
    URL.revokeObjectURL(a.href);
  });
  document.getElementById("import").addEventListener("change", function () {
    var f = this.files[0];
    if (!f) return;
    var note = document.getElementById("import-note");
    var r = new FileReader();
    r.onload = function () {
      var obj = null;
      try { obj = JSON.parse(r.result); } catch (e) {}
      if (!obj || typeof obj !== "object") {
        note.innerHTML = "<span class='warn'>That file could not be read as a year plan. " +
          "It is not in the format the Export button saves. Your current plan was not changed.</span>";
        return;
      }
      if (!obj.start || !obj.end) {
        note.innerHTML = "<span class='warn'>That file does not look like a year plan: " +
          "it has no school year start and end dates. If it is a single unit's plan file, " +
          "import it from that unit's planner page instead. Your current plan was not changed.</span>";
        return;
      }
      S = obj;
      if (!S.unitDays) S.unitDays = {};
      if (!S.pinnedStarts) S.pinnedStarts = {};
      normSchedule(S);
      render();
      var shortCourse = { full: "full survey", early: "early course (to 1877)", modern: "modern course (from 1877)" }[S.course] || "full survey";
      note.textContent = "Imported: " + shortCourse + ", " + fmtLong(S.start) + " – " + fmtLong(S.end) +
        ", " + activeUnits().length + " units.";
    };
    r.readAsText(f);
    this.value = "";
  });

  document.getElementById("plan-select").addEventListener("change", function () {
    planName = this.value;
    S = lib.plans[planName];
    render();
  });
  document.getElementById("plan-new").addEventListener("click", function () {
    var name = window.prompt("Name the new plan (it starts from the standard year setup):", "Plan " + (Object.keys(lib.plans).length + 1));
    if (!name || !name.trim() || lib.plans[name.trim()]) return;
    planName = name.trim();
    lib.plans[planName] = defaults();
    S = lib.plans[planName];
    render();
  });
  document.getElementById("plan-rename").addEventListener("click", function () {
    var name = window.prompt("Rename this plan:", planName);
    if (!name || !name.trim() || name.trim() === planName || lib.plans[name.trim()]) return;
    lib.plans[name.trim()] = S;
    delete lib.plans[planName];
    planName = name.trim();
    render();
  });
  document.getElementById("plan-del").addEventListener("click", function () {
    if (Object.keys(lib.plans).length <= 1) return;
    if (!window.confirm("Delete the plan \"" + planName + "\"? Other plans are not affected.")) return;
    delete lib.plans[planName];
    planName = Object.keys(lib.plans)[0];
    S = lib.plans[planName];
    render();
  });
  document.getElementById("share-year").addEventListener("click", function () {
    var enc = btoa(unescape(encodeURIComponent(JSON.stringify(S)))).replace(/\+/g, "-").replace(/\//g, "_");
    var url = location.origin + location.pathname + "#plan=" + enc;
    var note = document.getElementById("share-year-note");
    function done(ok) {
      note.textContent = ok ?
        "Share link copied. Whoever opens it gets this year plan loaded as its own plan in their browser; nothing is uploaded." :
        "Copy this link: " + url;
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(function () { done(true); }, function () { done(false); });
    } else done(false);
  });
  document.getElementById("starter-dismiss").addEventListener("click", function () {
    // Dismissing adopts the year: the teacher has read the banner and
    // chosen to keep these dates, so it is no longer labeled a starter.
    S.starter = false;
    render();
  });

  // Fit to year: trim unit day counts toward the room the year has,
  // proportionally across the headroom above each unit's core minimum,
  // never below that minimum. The result shows before anything changes.
  function computeFit() {
    var days = instructionalDays();
    var A = assign(days);
    var lpm = lessonsPerMeeting();
    var meetSet = {};
    meetingDays(days).forEach(function (d) { meetSet[d] = true; });
    var reservedMeetings = Object.keys(A.reserved).filter(function (d) { return meetSet[d]; }).length;
    var capacity = (meetingDays(days).length - reservedMeetings) * lpm;
    var rows = activeUnits().map(function (u) {
      var floor = coreMin(u);
      var cur = unitDays(u).days;
      return { u: u, cur: cur, floor: floor == null ? cur : floor, next: cur };
    });
    var demand = rows.reduce(function (n, r) { return n + r.cur; }, 0);
    var out = { rows: rows, demand: demand, capacity: capacity, fits: demand <= capacity, stillOver: 0, newDemand: demand };
    if (out.fits) return out;
    var excess = demand - capacity;
    var head = rows.map(function (r) { return Math.max(0, r.cur - r.floor); });
    var H = head.reduce(function (n, h) { return n + h; }, 0);
    var cuts = rows.map(function () { return 0; });
    var assigned = 0;
    if (H > 0) {
      var raw = head.map(function (h) { return excess * h / H; });
      raw.forEach(function (r, i) { cuts[i] = Math.min(head[i], Math.floor(r)); assigned += cuts[i]; });
      var order = raw.map(function (r, i) { return { i: i, frac: r - Math.floor(r) }; })
        .sort(function (a, b) { return b.frac - a.frac; });
      var guard = 0;
      while (assigned < excess && guard < 10000) {
        var progressed = false;
        for (var k = 0; k < order.length && assigned < excess; k++) {
          var oi = order[k].i;
          if (cuts[oi] < head[oi]) { cuts[oi]++; assigned++; progressed = true; }
        }
        if (!progressed) break;
        guard++;
      }
    }
    rows.forEach(function (r, i) { r.next = r.cur - cuts[i]; });
    out.stillOver = Math.max(0, excess - assigned);
    out.newDemand = rows.reduce(function (n, r) { return n + r.next; }, 0);
    return out;
  }
  document.getElementById("fit-year").addEventListener("click", function () {
    var box = document.getElementById("fit-preview");
    var F = computeFit();
    function dismiss() { box.style.display = "none"; box.innerHTML = ""; }
    if (F.fits) {
      box.innerHTML = "<p style='margin:0 0 6px;'><strong>Everything fits.</strong> Your units ask for " + F.demand +
        " lesson-days and your year has " + F.capacity + ". Nothing to trim.</p>" +
        "<button type='button' class='mini' id='fit-dismiss'>Dismiss</button>";
      box.style.display = "";
      document.getElementById("fit-dismiss").addEventListener("click", dismiss);
      return;
    }
    var changed = F.rows.filter(function (r) { return r.next !== r.cur; });
    if (!changed.length) {
      box.innerHTML = "<p style='margin:0 0 6px;'><strong>Nothing to trim.</strong> Every unit is already at its core minimum, and the year is still " +
        F.stillOver + " days short. A longer year or a shorter course is the fix.</p>" +
        "<button type='button' class='mini' id='fit-dismiss'>Dismiss</button>";
      box.style.display = "";
      document.getElementById("fit-dismiss").addEventListener("click", dismiss);
      return;
    }
    box.innerHTML = "<p style='margin:0 0 6px;'><strong>Fit to year</strong> would trim units toward your calendar. No unit goes below its core minimum, the lesson-days in its core picks plus the test day.</p>" +
      "<ul style='margin:0 0 6px;padding-left:18px;'>" + changed.map(function (r) {
        return "<li>" + r.u.name + ": " + r.cur + " → " + r.next + " days (core minimum " + r.floor + ")</li>";
      }).join("") + "</ul>" +
      "<p style='margin:0 0 6px;'>Units would ask for " + F.newDemand + " lesson-days; your year has " + F.capacity + "." +
      (F.stillOver ? " Even at every unit's core minimum the year is still " + F.stillOver + " days short, so a longer year or a shorter course is also needed." : "") + "</p>" +
      "<button type='button' class='mini' id='fit-apply'>Apply these day counts</button> " +
      "<button type='button' class='mini' id='fit-cancel'>Cancel</button>";
    box.style.display = "";
    document.getElementById("fit-apply").addEventListener("click", function () {
      F.rows.forEach(function (r) { if (r.next !== r.cur) S.unitDays[r.u.id] = r.next; });
      dismiss();
      render();
    });
    document.getElementById("fit-cancel").addEventListener("click", dismiss);
  });

  document.getElementById("ics-year").addEventListener("click", function () {
    var days = instructionalDays();
    var A = assign(days);
    // Units that do not fit are named before they are left out, never
    // dropped silently. The exam day itself is an event; the days held
    // for exam review in front of it are not separate events.
    var unfitted = activeUnits().filter(function (u) { return !(A.ranges[u.id] || []).length; });
    var note = document.getElementById("ics-note");
    if (unfitted.length) {
      var names = unfitted.map(function (u) { return u.name; }).join(", ");
      if (!window.confirm("These units do not fit in the year and will not be in the calendar file: " + names +
        ". The exam day itself is included; days held for exam review are not separate events. Export anyway?")) return;
      note.textContent = "Left out of this file because they do not fit: " + names + ".";
    } else {
      note.textContent = "Every unit is in this file." +
        (S.exam ? " Days held for exam review are not separate events; the exam day itself is." : "");
    }
    function esc(s) { return String(s).replace(/\\/g, "\\\\").replace(/;/g, "\\;").replace(/,/g, "\\,"); }
    function dnum(iso) { return iso.replace(/-/g, ""); }
    function next(iso) { var d = P(iso); d.setDate(d.getDate() + 1); return ISO(d); }
    var stamp = new Date().toISOString().replace(/[-:]/g, "").split(".")[0] + "Z";
    var lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Humanities Curriculum Group//Year Planner//EN", "CALSCALE:GREGORIAN"];
    activeUnits().forEach(function (u) {
      var r = A.ranges[u.id] || [];
      if (!r.length) return;
      lines.push("BEGIN:VEVENT", "UID:hcg-year-" + u.id + "-start@humanitiescurriculumgroup.web.app", "DTSTAMP:" + stamp,
        "DTSTART;VALUE=DATE:" + dnum(r[0]), "DTEND;VALUE=DATE:" + dnum(next(r[0])),
        "SUMMARY:" + esc("US History: " + u.name + " begins"), "END:VEVENT");
      lines.push("BEGIN:VEVENT", "UID:hcg-year-" + u.id + "-test@humanitiescurriculumgroup.web.app", "DTSTAMP:" + stamp,
        "DTSTART;VALUE=DATE:" + dnum(r[r.length - 1]), "DTEND;VALUE=DATE:" + dnum(next(r[r.length - 1])),
        "SUMMARY:" + esc("US History: " + u.name + " · unit test"), "END:VEVENT");
    });
    if (S.exam) {
      lines.push("BEGIN:VEVENT", "UID:hcg-year-exam@humanitiescurriculumgroup.web.app", "DTSTAMP:" + stamp,
        "DTSTART;VALUE=DATE:" + dnum(S.exam), "DTEND;VALUE=DATE:" + dnum(next(S.exam)),
        "SUMMARY:" + esc("US History: exam day"), "END:VEVENT");
    }
    lines.push("END:VCALENDAR");
    var blob = new Blob([lines.join("\r\n")], { type: "text/calendar" });
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "us-history-year-milestones.ics";
    a.click();
    URL.revokeObjectURL(a.href);
  });

  document.getElementById("copyfwd").addEventListener("click", function () {
    if (!window.confirm("Copy this plan forward one year? Every date moves ahead a year (holidays land on the same calendar date, so check them against next year's real calendar). Your unit day counts carry over; pinned starts are cleared. Export first if you want to keep this year's plan as a file.")) return;
    function shift(iso) {
      if (!iso) return iso;
      var p = iso.split("-"), y = +p[0] + 1, m = p[1], d = p[2];
      if (m === "02" && d === "29") d = "28";
      return y + "-" + m + "-" + d;
    }
    S.start = shift(S.start); S.end = shift(S.end); S.exam = shift(S.exam);
    S.periods.forEach(function (p) { p.end = shift(p.end); });
    S.daysOff.forEach(function (o) { o.from = shift(o.from); o.to = shift(o.to); });
    S.pinnedStarts = {};
    S.starter = false;
    render();
  });

  if (sharedYear) {
    var sn = document.getElementById("shared-note");
    if (sn) sn.style.display = "";
  }

  // Auth state changes refresh the save line through save().
  window.HCGYearRefresh = function () { save(); };

  render();
})();
