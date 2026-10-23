#!/usr/bin/env python3
"""Generate the three Course Review unit pages on the modern-america.html
pattern: intro, entitled note, Rycal block, About, cover, per-band plate
divs with data-file download items, flex/test div, previews, blueprint
table, and the All-Access download script (no deck extras: the review
ships no new decks, and the pages say so).

Run: python3 gen_pages.py
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.join(HERE, "..", "site", "public")
sys.path.insert(0, HERE)
from gen_registry import BLUEPRINT_TEXT, BAND_UNITS  # noqa: E402

BAND_TITLES = {}
for n in range(1, 9):
    h = open(os.path.join(HERE, f"band-{n}", f"day-{n}-review-packet.html")).read()
    BAND_TITLES[n] = re.search(r"<h1>Band \d+ Review Packet: (.*?)</h1>", h).group(1)
BAND_SKILLS = {1: "chronology", 2: "comparison", 3: "causation",
               4: "continuity and change", 5: "comparison", 6: "causation",
               7: "continuity and change", 8: "working with documents"}
UNAME = {"ca": "Colonial America", "fd": "The Founding", "er": "Early Republic and Expansion",
         "jr": "Jackson and Reform", "sc": "Sectional Crisis and Civil War", "rc": "Reconstruction",
         "ga": "The Gilded Age", "pe": "Progressive Era", "wwi": "Imperialism and World War I",
         "tw": "The Twenties", "dp": "Depression and New Deal", "ww2": "World War II",
         "cw": "The Cold War", "cr": "Civil Rights", "ma": "Modern America"}

V = {
    "course-review": dict(
        vid="rv", name="Course Review", bands=[1, 2, 3, 4, 5, 6, 7, 8], docs=43, terms=840,
        cross=60, days="ten days", bands_word="eight",
        title="Course Review | Eight Band Days, Study Guide, and Practice Test | Humanities Curriculum Group",
        desc="Review the whole US History course in eight band days: packets, term sprints, practice sets, skills tasks, a study guide, a crossword, and a 50-point practice test tagged to the course blueprint.",
        sub="The capstone of the US History course, included with All-Access. Eight band days compress all fifteen units into review: each day runs a packet, a forty-term sprint, an eighteen-question practice set, and a skills task on the era's own skill, with a teacher guide carrying the keys. A flex day works the study guide and crossword, and a 50-point practice test closes the review, every item tagged to the course blueprint. Every document follows the same print standard as the rest of the course: black text, open writing space, no ink-heavy design. If you are new here, the <a href=\"progressive-era.html\">Progressive Era unit</a> is the free sample, and it runs on the same plate and the same planner.",
        about=[
            "The review is built from the course's own materials and nothing else. Every term in the sprints and the study guide prints the definition word for word as the unit's guided notes print it; every timeline row comes from the units' packets; the practice questions are new, written to the same standard as the unit tests, and each one carries a printed tag naming the unit it reviews. The eight bands pair the course's units in course order, two to a day, and each band trains the skill its era teaches best: chronology for the colonies and the Founding, comparison for the early republic and for the age of empire, causation for the road to civil war and for depression and total war, continuity and change for industry and reform and for the Cold War and civil rights, and documents for Modern America and the long arc of the whole course.",
            "The closing pieces gather the whole span. The study guide prints all 840 terms by unit and lesson with room to write the definitions from memory, then a key with every definition filled in, the eight bands' timelines, the fifteen units' essential questions, one paragraph stating each unit's argument, and the twenty-four review questions the band packets end on, with a full key. The crossword holds sixty answers, four from every unit. The practice test is fifty points in the unit tests' format, matching, multiple choice, and sources, and its blueprint is the course itself: all fifteen units, each assessed at least twice, recomputed from the printed tags.",
            "In the planner the review is a unit like any other: ten days at full length, with a Fit to year floor of seven. Its natural home is the run of days before the exam, and the year planner treats it that way, so a teacher who schedules the review is not also reserving blank review days on top of it. The writing option is the capstone: every premium DBQ from The Primary Source Project is a picker entry here, pre-tagged to the unit it reviews, so the era a practice set exposes becomes the next day's document essay. There are no new slide decks in the review, deliberately: review days are student-work days, and a teacher reteaching a band uses that unit's own decks, which stay one click away on its page.",
        ],
        cover_alt="The Course Review cover",
        cover_text="Print it for the front of the review packet, or keep it as the first page of the digital bundle. The cover ships with the unit in All-Access. The three previews further down show the full plate, two real pages from the band days, and the practice test with its tagged key.",
    ),
    "early-review": dict(
        vid="re", name="Early Course Review", bands=[1, 2, 3], docs=18, terms=336,
        cross=24, days="five days", bands_word="three",
        title="Early Course Review | Colonial America to Reconstruction | Humanities Curriculum Group",
        desc="Review the first half of US History, 1491 to 1877, in three band days: packets, term sprints, practice sets, skills tasks, a study guide, a crossword, and a 50-point practice test.",
        sub="The review for the first half of the course, 1491 to 1877, included with All-Access. Three band days cover the first six units: each day runs a packet, a forty-term sprint, an eighteen-question practice set, and a skills task, with a teacher guide carrying the keys. A flex day works the study guide and crossword, and a 50-point practice test closes the review, every item tagged to the blueprint. Every document follows the same print standard as the rest of the course: black text, open writing space, no ink-heavy design. If you are new here, the <a href=\"progressive-era.html\">Progressive Era unit</a> is the free sample, and it runs on the same plate and the same planner.",
        about=[
            "The review is built from the course's own materials and nothing else. Every term in the sprints and the study guide prints the definition word for word as the unit's guided notes print it; every timeline row comes from the units' packets; the practice questions are new, written to the same standard as the unit tests, and each one carries a printed tag naming the unit it reviews. The three bands pair the early units in course order: the colonies with the Founding, the early republic with Jackson's age, and the sectional crisis with Reconstruction. Each band trains the skill its era teaches best: chronology, comparison, and causation.",
            "The closing pieces gather the early span. The study guide prints all 336 terms by unit and lesson with room to write the definitions from memory, then a key with every definition filled in, the three bands' timelines, the six units' essential questions, one paragraph stating each unit's argument, and the nine review questions the band packets end on, with a full key. The crossword holds twenty-four answers, four from every unit. The practice test is fifty points in the unit tests' format, and its blueprint is the early course itself: all six units, each assessed at least twice, recomputed from the printed tags.",
            "In the planner the early review is a unit like any other: five days at full length, with a Fit to year floor of four, and its natural home is the end of a course that stops at 1877. The writing option is the capstone: the premium DBQs from The Primary Source Project that belong to these six units are picker entries here, pre-tagged to the unit each reviews, so the era a practice set exposes becomes the next day's document essay. There are no new slide decks in the review, deliberately: review days are student-work days, and a teacher reteaching a band uses that unit's own decks, which stay one click away on its page.",
        ],
        cover_alt="The Early Course Review cover",
        cover_text="Print it for the front of the review packet, or keep it as the first page of the digital bundle. The cover ships with the unit in All-Access. The three previews further down show the full plate, two real pages from the band days, and the practice test with its tagged key.",
    ),
    "modern-review": dict(
        vid="rm", name="Modern Course Review", bands=[4, 5, 6, 7, 8], docs=28, terms=504,
        cross=36, days="seven days", bands_word="five",
        title="Modern Course Review | The Gilded Age to the Present | Humanities Curriculum Group",
        desc="Review the modern half of US History, 1877 to the present, in five band days: packets, term sprints, practice sets, skills tasks, a study guide, a crossword, and a 50-point practice test.",
        sub="The review for the modern half of the course, 1877 to the present, included with All-Access. Five band days cover the last nine units: each day runs a packet, a forty-term sprint, an eighteen-question practice set, and a skills task, with a teacher guide carrying the keys. A flex day works the study guide and crossword, and a 50-point practice test closes the review, every item tagged to the blueprint. Every document follows the same print standard as the rest of the course: black text, open writing space, no ink-heavy design. If you are new here, the <a href=\"progressive-era.html\">Progressive Era unit</a> is the free sample, and it runs on the same plate and the same planner.",
        about=[
            "The review is built from the course's own materials and nothing else. Every term in the sprints and the study guide prints the definition word for word as the unit's guided notes print it; every timeline row comes from the units' packets; the practice questions are new, written to the same standard as the unit tests, and each one carries a printed tag naming the unit it reviews. The five bands pair the modern units in course order: the Gilded Age with the Progressive Era, empire and war with the Twenties, depression with total war, and the Cold War with civil rights, closing on Modern America and the long arc of the whole course. The bands train continuity and change, comparison, causation, and, on the last day, work with documents.",
            "The closing pieces gather the modern span. The study guide prints all 504 terms by unit and lesson with room to write the definitions from memory, then a key with every definition filled in, the five bands' timelines, the nine units' essential questions, one paragraph stating each unit's argument, and the fifteen review questions the band packets end on, with a full key. The crossword holds thirty-six answers, four from every unit. The practice test is fifty points in the unit tests' format, and its blueprint is the modern course itself: all nine units, each assessed at least twice, recomputed from the printed tags.",
            "In the planner the modern review is a unit like any other: seven days at full length, with a Fit to year floor of five, and its natural home is the run of days before the exam in a course that begins at 1877. The writing option is the capstone: the premium DBQs from The Primary Source Project that belong to these nine units are picker entries here, pre-tagged to the unit each reviews, so the era a practice set exposes becomes the next day's document essay. There are no new slide decks in the review, deliberately: review days are student-work days, and a teacher reteaching a band uses that unit's own decks, which stay one click away on its page.",
        ],
        cover_alt="The Modern Course Review cover",
        cover_text="Print it for the front of the review packet, or keep it as the first page of the digital bundle. The cover ships with the unit in All-Access. The three previews further down show the full plate, two real pages from the band days, and the practice test with its tagged key.",
    ),
}

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://humanitiescurriculumgroup.web.app/{slug}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://humanitiescurriculumgroup.web.app/{slug}">
<link rel="stylesheet" href="styles.css">
<link rel="icon" type="image/svg+xml" href="assets/store-wordmark-color.svg">
<style>
  .plate a.dl {{ font-weight: bold; white-space: nowrap; }}
  #{vid}-entitled-note {{ background: var(--cream); border-left: 3px solid var(--rust); padding: 12px 16px; max-width: 820px; margin: 16px 0 0; }}
</style>
</head>
<body>

<header class="site">
  <div class="wrap">
    <a href="index.html"><img class="wordmark" src="assets/store-wordmark-cream.svg" alt="Humanities Curriculum Group"></a>
    <nav class="main">
      <a href="index.html">Home</a>
      <a href="us-history.html" class="here">US History</a>
      <a href="progressive-era.html">Sample Unit</a>
      <a href="planner-year.html">Year Planner</a>
      <a href="planner.html">Unit Planner</a>
      <a href="about.html">About</a>
    </nav>
    <div class="hcg-account" id="hcg-account"></div>
  </div>
</header>
"""

FOOT = """
<footer class="site">
  <div class="wrap">
    <img src="assets/store-wordmark-cream.svg" alt="Humanities Curriculum Group">
    <div>
      <p>Humanities Curriculum Group is a Knoweth product, built by a working social studies teacher. Sister projects: <a href="https://rycal.web.app">Rycal</a>, spaced-repetition study tools for AP courses, and <a href="https://tpsp.web.app">The Primary Source Project</a>, a primary source library and DBQ builder.</p>
      <p>Materials print on standard US Letter paper with ordinary school copiers in mind.</p>
    </div>
  </div>
</footer>
"""


def band_units_label(b):
    return " and ".join(UNAME[u] for u in BAND_UNITS[b])


def build(slug, c):
    vid = c["vid"]
    entries = []  # (num, text, bandidx) in this variant's blueprint numbering
    n = 0
    band_of_entry = {}
    for bi, b in enumerate(c["bands"], 1):
        for u in BAND_UNITS[b]:
            n += 1
            entries.append((n, BLUEPRINT_TEXT[u], bi, b))
            band_of_entry[n] = bi
    out = [HEAD.format(title=c["title"], desc=c["desc"], slug=slug, vid=vid)]
    out.append(f"""
<section class="block">
  <div class="wrap">
    <h1>{c['name']}</h1>
    <p class="sub">{c['sub']}</p>
    <p><a class="btn" href="subscribe.html">Get this unit with All-Access</a> <a class="btn secondary" href="progressive-era.html">See the free sample unit</a> <a class="btn secondary" href="planner.html?unit={vid}">Plan this unit</a></p>
    <div id="{vid}-entitled-note" hidden><strong>Your All-Access is active.</strong> Download buttons appear next to every document below.</div>

    <div class="note rycal-note" style="max-width:820px;">
      <strong>Student vocabulary review.</strong> Post this link for students on the first day of the review: <a href="https://rycal.web.app/hcg-{slug}-flashcards">https://rycal.web.app/hcg-{slug}-flashcards</a>. The deck holds all {c['terms']} key terms from this review's units, with the definitions word for word as the guided notes print them. Students need no account: they open the link, copy the deck to their own set, enter the exam date, and Rycal paces short spaced sessions across the whole review. HCG collects nothing about students; the link simply takes them to Rycal. Paste the address into your LMS so students have it from day one.
    </div>

    <h2 style="margin-top:30px;">About this unit</h2>
    <div style="max-width:820px;">
""")
    for p in c["about"]:
        out.append(f"      <p>{p}</p>\n")
    out.append(f"""    </div>

    <div style="display:flex; gap:26px; align-items:flex-start; margin:28px 0 4px; flex-wrap:wrap;">
      <img src="assets/{slug}-cover.png" alt="{c['cover_alt']}" style="width:270px; border:1px solid #c9bfa5; box-shadow:0 2px 10px rgba(31,51,80,.15); display:block;">
      <div style="flex:1; min-width:260px;">
        <h3 style="margin-top:2px;">The cover page</h3>
        <p class="sub">{c['cover_text']}</p>
      </div>
    </div>
""")
    for bi, b in enumerate(c["bands"], 1):
        b_entries = [t for (num, t, bx, bb) in entries if bb == b]
        out.append(f"""
    <div class="lesson">
      <h3>Band {b} · {BAND_TITLES[b]}</h3>
      <p class="covers">Course blueprint: {'; '.join(b_entries)}</p>
      <ul class="plate">
        <li data-file="band-{b}-packet.pdf"><span class="kind">Packet</span> {BAND_TITLES[b]} review packet</li>
        <li data-file="band-{b}-sprint.pdf"><span class="kind">Term Sprint</span> Forty terms from {band_units_label(b)}</li>
        <li data-file="band-{b}-practice.pdf"><span class="kind">Practice Set</span> Eighteen questions in the style of the course test</li>
        <li data-file="band-{b}-skills.pdf"><span class="kind">Skills Task</span> The band's skill: {BAND_SKILLS[b]}</li>
        <li data-file="band-{b}-teacher-guide.pdf"><span class="kind">Teacher Guide</span> Front matter and every key for the day</li>
      </ul>
    </div>
""")
    out.append(f"""
    <div class="lesson">
      <h3>Flex Day and Practice Test</h3>
      <p class="covers">The practice test is 50 points: matching, multiple choice, and a source-based section, with every item tagged in the key to the blueprint entry it assesses. Each entry in this review's blueprint is assessed at least twice, recomputed from the printed tags.</p>
      <ul class="plate">
        <li data-file="study-guide.pdf"><span class="kind">Review</span> Study guide with full key, all {c['terms']} terms</li>
        <li data-file="crossword.pdf"><span class="kind">Review</span> Crossword, {c['cross']} answers</li>
        <li data-file="practice-test.pdf"><span class="kind">Test</span> Practice test with tagged answer key</li>
      </ul>
    </div>

    <h3 style="margin-top:30px;">Preview the unit</h3>
    <p class="sub">Three pages from the listing, built from the actual documents.</p>
    <p style="margin:14px 0 4px;"><a href="assets/{slug}-preview-1.png"><img src="assets/{slug}-preview-1.png" alt="Preview 1: the full plate" style="width:100%; max-width:920px; border:1px solid #c9bfa5; display:block;"></a></p>
    <p style="margin:14px 0 4px;"><a href="assets/{slug}-preview-2.png"><img src="assets/{slug}-preview-2.png" alt="Preview 2: inside the band days" style="width:100%; max-width:920px; border:1px solid #c9bfa5; display:block;"></a></p>
    <p style="margin:14px 0 4px;"><a href="assets/{slug}-preview-3.png"><img src="assets/{slug}-preview-3.png" alt="Preview 3: the practice test and its key" style="width:100%; max-width:920px; border:1px solid #c9bfa5; display:block;"></a></p>

    <h3 style="margin-top:28px;">The course blueprint</h3>
    <p class="sub">The entries the practice test assesses. Every band day above is tagged to the entries it reviews, which is what the planner's coverage check reads.</p>
    <table class="course">
      <tr><th style="width:6%">#</th><th>Blueprint entry</th><th style="width:22%">Reviewed in</th></tr>
""")
    for num, text, bi, b in entries:
        out.append(f'      <tr><td>{num}</td><td>{text}</td><td>Band {b}</td></tr>\n')
    out.append(f"""    </table>

    <div class="note" style="margin-top:26px;">This unit is part of All-Access, so its documents are not posted as free downloads. The complete <a href="progressive-era.html">Progressive Era unit</a> is free if you want to see the full plate, the print standard, and a tagged test before subscribing.</div>
  </div>
</section>
{FOOT}
<script src="firebase-config.js"></script>
<script src="auth.js"></script>
<script>
  // All-Access downloads: entitled accounts get a Download control on each
  // plate item. URLs are minted per click through Firebase Storage, whose
  // rules re-check entitlement.
  (function () {{
    var PREFIX = "hcg/{slug}/";
    function makeDl(file, label) {{
      var a = document.createElement("a");
      a.href = "#"; a.className = "dl"; a.textContent = label;
      a.addEventListener("click", function (ev) {{
        ev.preventDefault();
        var old = a.textContent; a.textContent = "Preparing\\u2026";
        window.HCGFiles.url(PREFIX + file).then(function (url) {{
          a.textContent = old;
          if (url) window.location.href = url;
          else window.alert("That download is not available on this account. If you just subscribed, give it a few seconds and try again.");
        }}).catch(function () {{ a.textContent = old; }});
      }});
      return a;
    }}
    function render() {{
      var ent = window.HCGAuth.entitlement();
      var note = document.getElementById("{vid}-entitled-note");
      if (!ent.paid) {{ if (note) note.hidden = true; return; }}
      if (note) note.hidden = false;
      document.querySelectorAll("li[data-file]").forEach(function (li) {{
        if (li.querySelector("a.dl")) return;
        li.appendChild(document.createTextNode(" \\u00b7 "));
        li.appendChild(makeDl(li.getAttribute("data-file"), "Download"));
      }});
    }}
    if (window.HCGAuth) window.HCGAuth.onChange(render);
  }})();
</script>
</body>
</html>
""")
    path = os.path.join(PUB, f"{slug}.html")
    open(path, "w").write("".join(out))
    print("page:", path)


for slug, cfg in V.items():
    build(slug, cfg)
