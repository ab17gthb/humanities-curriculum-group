#!/usr/bin/env python3
"""Assemble the three Course Review study guides from course data.

Per variant: band timelines (parsed from the band packets), each unit's
essential question (planner-data.js) and term list (audited staging JSON),
the bands' Carry Three review questions (parsed from the packets), the
authored unit arguments and question key answers (guide-data.py), and a
full teacher key with every term's guided-notes definition.

Run: python3 gen_study_guides.py
"""
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from guide_data import UNIT_ARGUMENTS, BAND_KEY_ANSWERS  # noqa: E402

STAGING = "/home/hatch/workspace/rycal/course-staging"

UNITS = {  # id -> (name, staging slug)
    "ca": ("Colonial America", "hcg-colonial-america"),
    "fd": ("The Founding", "hcg-the-founding"),
    "er": ("Early Republic and Expansion", "hcg-early-republic"),
    "jr": ("Jackson and Reform", "hcg-jackson-reform"),
    "sc": ("Sectional Crisis and Civil War", "hcg-sectional-crisis"),
    "rc": ("Reconstruction", "hcg-reconstruction"),
    "ga": ("The Gilded Age", "hcg-gilded-age"),
    "pe": ("Progressive Era", "hcg-progressive-era"),
    "wwi": ("Imperialism and World War I", "hcg-imperialism-wwi"),
    "tw": ("The Twenties", "hcg-twenties"),
    "dp": ("Depression and New Deal", "hcg-depression-new-deal"),
    "ww2": ("World War II", "hcg-world-war-ii"),
    "cw": ("The Cold War", "hcg-cold-war"),
    "cr": ("Civil Rights", "hcg-civil-rights"),
    "ma": ("Modern America", "hcg-modern-america"),
}

BAND_UNITS = {
    1: ["ca", "fd"], 2: ["er", "jr"], 3: ["sc", "rc"], 4: ["ga", "pe"],
    5: ["wwi", "tw"], 6: ["dp", "ww2"], 7: ["cw", "cr"], 8: ["ma"],
}

VARIANTS = {
    "early": ("Early Course Review", [1, 2, 3]),
    "modern": ("Modern Course Review", [4, 5, 6, 7, 8]),
    "combined": ("Course Review", [1, 2, 3, 4, 5, 6, 7, 8]),
}

CSS = """
@page { size: letter; margin: 0.55in 0.75in 0.7in; }
* { box-sizing: border-box; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 11.5pt; color: #000; line-height: 1.35; margin: 0; }
.nameline { display: flex; justify-content: space-between; gap: 1em; }
h1 { font-family: Georgia, serif; font-size: 19pt; margin: 12pt 0 4pt; line-height: 1.2; color: #1b2a4a; }
h2 { font-family: Georgia, serif; font-size: 14.5pt; margin: 16pt 0 6pt; color: #1b2a4a; }
h3 { font-size: 12.5pt; margin: 14pt 0 4pt; break-after: avoid; color: #1b2a4a; }
h4 { font-size: 11.5pt; margin: 10pt 0 3pt; break-after: avoid; }
p { margin: 0 0 7pt; }
.brandmark { margin: 0 0 4pt; line-height: 0; } .brandmark img { width: 1.35in; }
.rule { border-top: 1.6pt solid #b3543f; margin: 6pt 0 10pt; }
.eq { border-left: 2.5pt solid #b3543f; padding: 2pt 0 2pt 10pt; margin: 6pt 0 8pt; }
table.tl { border-collapse: collapse; width: 100%; margin: 4pt 0 10pt; font-size: 10.2pt; }
table.tl th { text-align: left; font-family: Georgia, serif; color: #1b2a4a; border-bottom: 1.2pt solid #1b2a4a; padding: 2pt 5pt; }
table.tl td { padding: 2pt 5pt; border-bottom: 0.5pt solid #999; vertical-align: top; }
td.dt { width: 1.3in; }
table.terms { border-collapse: collapse; width: 100%; margin: 4pt 0 10pt; }
table.terms td { border: 0.6pt solid #000; padding: 4pt 6pt; text-align: left; font-size: 11pt; vertical-align: top; }
table.terms td.row { height: 0.42in; }
table.terms td.filled { font-size: 10.5pt; line-height: 1.3; }
.q { margin: 10pt 0 0; }
.sp { height: 1.1in; border-bottom: 0.5pt solid #bbb; }
.part { break-before: page; }
.part h2:first-child { margin-top: 0; }
"""


def load_eqs():
    src = open(os.path.join(ROOT, "site/public/planner-data.js")).read()
    eqs = {}
    for uid in UNITS:
        i = src.find(f'id: "{uid}"')
        m = re.search(r'essentialQuestion: "([^"]+)"', src[i:i + 4000])
        assert m, uid
        eqs[uid] = m.group(1)
    return eqs


def load_terms(slug):
    rows = json.load(open(os.path.join(STAGING, slug, "vocab-audited.json")))
    lessons = {}
    for r in rows:
        lessons.setdefault(r["unit"], []).append(r)
    return lessons


def band_title(n):
    h = open(os.path.join(HERE, f"band-{n}", f"day-{n}-review-packet.html")).read()
    m = re.search(r"<h1>Band \d+ Review Packet: (.*?)</h1>", h)
    assert m, n
    return m.group(1)


def band_timeline(n):
    h = open(os.path.join(HERE, f"band-{n}", f"day-{n}-review-packet.html")).read()
    rows = re.findall(
        r'<tr><td class="dt">(.*?)</td><td>(.*?)</td><td>.*?</td></tr>', h, re.S)
    assert len(rows) >= 15, (n, len(rows))
    return [(re.sub(r"<[^>]+>", "", d).strip(), re.sub(r"<[^>]+>", "", e).strip())
            for d, e in rows]


def band_questions(n):
    h = open(os.path.join(HERE, f"band-{n}", f"day-{n}-review-packet.html")).read()
    i = h.find("Carry Three Questions")
    qs = re.findall(r"<strong>(\d)\.</strong> (.*?)</p>", h[i:i + 1600])
    out = [re.sub(r"<[^>]+>", "", q).strip() for _, q in sorted(qs)]
    assert len(out) == 3, (n, out)
    return out


def esc(t):
    return html.escape(t, quote=False)


def build(variant, vname, bands):
    eqs = load_eqs()
    unit_ids = [u for b in bands for u in BAND_UNITS[b]]
    out = [f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<title>Study Guide: {vname}</title><style>{CSS}</style></head><body>
<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>
<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>
<h1>Study Guide: {vname}</h1>
<div class="rule"></div>
<p><strong>How to use this guide:</strong> It gathers the whole review into one place for the flex day and for your own study before the practice test. For each band: read the timeline and say aloud what changed in each row; answer the unit's essential question in your own words; then work the term lists, writing each definition from memory and checking it against your guided notes (your teacher holds the key). Finish with the review questions, three per band, written out. The arguments at the back state each unit's case in a paragraph; if you can argue with one, you know it.</p>"""]
    for b in bands:
        out.append(f"<h2>Band {b}: {esc(band_title(b))}</h2>")
        out.append('<table class="tl"><tr><th>Date</th><th>Event</th></tr>')
        for d, e in band_timeline(b):
            out.append(f'<tr><td class="dt">{esc(d)}</td><td>{esc(e)}</td></tr>')
        out.append("</table>")
        for uid in BAND_UNITS[b]:
            name, slug = UNITS[uid]
            out.append(f"<h3>{esc(name)}</h3>")
            out.append(f'<div class="eq"><p style="margin:0;"><strong>The unit asked:</strong> {esc(eqs[uid])}</p></div>')
            out.append('<table class="terms">')
            for lesson, rows in load_terms(slug).items():
                for r in rows:
                    out.append(f'<tr><td style="width:30%">{esc(r["term"])}</td><td class="row"></td></tr>')
            out.append("</table>")
    out.append('<div class="part"><h2>Review Questions</h2>'
               "<p>Write each answer out in full. These are the questions the band packets closed with; the practice test assumes you can answer every one.</p>")
    for b in bands:
        out.append(f"<h3>Band {b}: {esc(band_title(b))}</h3>")
        for i, q in enumerate(band_questions(b), 1):
            out.append(f'<p class="q"><strong>{i}.</strong> {esc(q)}</p><div class="sp"></div>')
    out.append("</div>")
    out.append('<div class="part"><h2>The Arguments</h2>'
               "<p>Each unit's case in one paragraph, in the order the units were taught. Read the paragraph, close the guide, and restate it; where your restatement thins out is where your studying goes next.</p>")
    for uid in unit_ids:
        out.append(f"<h3>{esc(UNITS[uid][0])}</h3><p>{esc(UNIT_ARGUMENTS[uid])}</p>")
    out.append("</div>")
    # Teacher key
    out.append('<div class="part"><h2>Teacher Answer Key</h2><h3>Key Terms, With the Guided-Notes Definitions</h3>')
    for uid in unit_ids:
        name, slug = UNITS[uid]
        out.append(f"<h3>{esc(name)}</h3>")
        for lesson, rows in load_terms(slug).items():
            out.append(f"<h4>{esc(lesson.replace(chr(8212), ':'))}</h4>")
            out.append('<table class="terms">')
            for r in rows:
                out.append(f'<tr><td class="filled"><strong>{esc(r["term"])}:</strong> {esc(r["definition"])}</td></tr>')
            out.append("</table>")
    out.append("<h3>Review Questions</h3>")
    for b in bands:
        out.append(f"<h4>Band {b}: {esc(band_title(b))}</h4>")
        for i, a in enumerate(BAND_KEY_ANSWERS[b], 1):
            out.append(f"<p><strong>{i}.</strong> {esc(a)}</p>")
    out.append("</div></body></html>")
    doc = "".join(out)
    d = os.path.join(HERE, f"study-guide-{variant}")
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, f"{variant}-study-guide.html")
    open(path, "w").write(doc)
    n_terms = sum(len(rows) for uid in unit_ids for rows in load_terms(UNITS[uid][1]).values())
    print(f"{variant}: {len(doc)} chars, {len(unit_ids)} units, {n_terms} terms -> {path}")


for v, (vn, bs) in VARIANTS.items():
    build(v, vn, bs)
