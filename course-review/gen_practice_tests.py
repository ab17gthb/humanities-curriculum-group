#!/usr/bin/env python3
"""Assemble the three Course Review practice tests (50 points each) in the
unit-test format: Matching 15, Multiple Choice 20, Sources 15, with a full
teacher key. Every item carries its entry tag; coverage of every entry in
the variant's blueprint at least twice is recomputed from the item data
and asserted before anything is written.

Run: python3 gen_practice_tests.py
"""
import html
import json
import os
import random
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from test_data import ENTRY, UNAME, MATCHING, MC, SOURCES, TEST_SOURCES  # noqa: E402

STAGING = "/home/hatch/workspace/rycal/course-staging"
SLUGS = {
    "ca": "hcg-colonial-america", "fd": "hcg-the-founding",
    "er": "hcg-early-republic", "jr": "hcg-jackson-reform",
    "sc": "hcg-sectional-crisis", "rc": "hcg-reconstruction",
    "ga": "hcg-gilded-age", "pe": "hcg-progressive-era",
    "wwi": "hcg-imperialism-wwi", "tw": "hcg-twenties",
    "dp": "hcg-depression-new-deal", "ww2": "hcg-world-war-ii",
    "cw": "hcg-cold-war", "cr": "hcg-civil-rights", "ma": "hcg-modern-america",
}
VARIANTS = {
    "early": ("Early Course Review", ["ca", "fd", "er", "jr", "sc", "rc"], 101),
    "modern": ("Modern Course Review", ["ga", "pe", "wwi", "tw", "dp", "ww2", "cw", "cr", "ma"], 202),
    "combined": ("Course Review", ["ca", "fd", "er", "jr", "sc", "rc", "ga", "pe", "wwi", "tw", "dp", "ww2", "cw", "cr", "ma"], 303),
}

CSS = """
@page { size: letter; margin: 0.55in 0.75in 0.7in; }
* { box-sizing: border-box; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 11.5pt; color: #000; line-height: 1.35; margin: 0; }
.nameline { display: flex; justify-content: space-between; gap: 1em; }
h1 { font-family: Georgia, serif; font-size: 19pt; margin: 12pt 0 4pt; line-height: 1.2; color: #1b2a4a; }
h2 { font-family: Georgia, serif; font-size: 14.5pt; margin: 16pt 0 6pt; color: #1b2a4a; }
h3 { font-size: 12.5pt; margin: 14pt 0 4pt; break-after: avoid; }
p { margin: 0 0 7pt; }
.directions { margin-bottom: 4pt; }
.q { margin: 10pt 0 0; }
.qa { break-inside: avoid; }
.sp-a { height: 0.8in; }
.sp-b { height: 1.3in; }
.opts { margin: 2pt 0 0 16pt; }
.opts span { display: block; }
.look { font-size: 10pt; color: #444; margin: 2pt 0 0; }
table.match { border-collapse: collapse; width: 100%; margin: 4pt 0 10pt; }
table.match td { padding: 3.5pt 6pt; font-size: 11.5pt; vertical-align: top; }
table.match td.n { width: 4%; }
table.match td.t { width: 30%; }
table.match .tag { display: block; font-size: 9.5pt; color: #444; }
.source { border: 1.5px solid #000; padding: 8pt 11pt; margin: 8pt 0; break-inside: avoid; }
.source .srclabel { font-weight: bold; margin-bottom: 4pt; }
.key { break-before: page; }
.key h2:first-child { margin-top: 0; }
.brandmark { margin: 0 0 4pt; line-height: 0; } .brandmark img { width: 1.35in; }
"""


def esc(t):
    return html.escape(t, quote=False)


def definitions(uid):
    rows = json.load(open(os.path.join(STAGING, SLUGS[uid], "vocab-audited.json")))
    return {r["term"]: r["definition"] for r in rows}


def build(variant, vname, unit_ids, seed):
    rng = random.Random(seed)
    coverage = Counter()
    for uid, term in MATCHING[variant]:
        coverage[ENTRY[uid]] += 1
    for uid, stem, opts in MC[variant]:
        coverage[ENTRY[uid]] += 1
    for skey in TEST_SOURCES[variant]:
        for pts, q, a in SOURCES[skey]["qs"]:
            coverage[ENTRY[SOURCES[skey]["unit"]]] += 1
    for uid in unit_ids:
        assert coverage[ENTRY[uid]] >= 2, (variant, uid, coverage[ENTRY[uid]])

    out = [f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<title>Practice Test: {vname}</title><style>{CSS}</style></head><body>
<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>
<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>
<h1>Practice Test: {vname}</h1>
<p class="directions">Total: 50 points. Part 1 is worth 15 points, Part 2 is worth 20 points, Part 3 is worth 15 points. Write answers on this test. The small line under each item names the course unit it reviews, so that when the test is over you can see exactly which units to reopen.</p>"""]

    # Part 1: Matching
    pairs = []
    for uid, term in MATCHING[variant]:
        defs = definitions(uid)
        assert term in defs, (uid, term)
        pairs.append((uid, term, defs[term]))
    order = list(range(len(pairs)))
    rng.shuffle(order)  # description order
    desc_at_row = [pairs[j] for j in order]
    letter_of = {}
    for row, (uid, term, dfn) in enumerate(desc_at_row):
        letter_of[term] = chr(ord("A") + row)
    out.append('<h2>Part 1: Matching (15 points)</h2><p>Match each term to its description. Each description is used once. Write the letter in the blank.</p>')
    out.append('<table class="match">')
    for i, (uid, term, dfn) in enumerate(pairs):
        ruid, rterm, rdfn = desc_at_row[i]
        out.append(f'<tr><td class="n">___</td><td class="t">{i + 1}. {esc(term)}<span class="tag">Entry {ENTRY[uid]} · {esc(UNAME[uid])}</span></td><td>{chr(ord("A") + i)}. {esc(rdfn)}</td></tr>')
    out.append("</table>")

    # Part 2: Multiple choice, correct answers rotated round-robin
    mc_key = []
    out.append('<h2>Part 2: Multiple Choice (20 points)</h2><p>Choose the best answer for each question.</p>')
    for i, (uid, stem, opts) in enumerate(MC[variant]):
        correct, distractors = opts[0], opts[1:]
        slots = distractors[:]
        rng.shuffle(slots)
        pos = i % 4
        final = slots[:]
        final.insert(pos, correct)
        mc_key.append(chr(ord("A") + pos))
        spans = "".join(f"<span>{chr(ord('A') + j)}. {esc(o)}</span>" for j, o in enumerate(final))
        out.append(f'<div class="qa"><p class="q"><strong>{i + 1}.</strong> {esc(stem)}</p><p class="opts">{spans}</p><p class="look">Reviews Entry {ENTRY[uid]} · {esc(UNAME[uid])}</p></div>')
    spread = Counter(mc_key)

    # Part 3: Sources
    out.append('<h2>Part 3: Sources (15 points)</h2><p>Answer each question in complete sentences, citing the sources by letter.</p>')
    src_key = []
    for li, skey in enumerate(TEST_SOURCES[variant]):
        letter = chr(ord("A") + li)
        s = SOURCES[skey]
        out.append(f'<div class="source"><p class="srclabel">Source {letter}</p><p>{esc(s["label"])}</p><p>&ldquo;{esc(s["text"])}&rdquo;</p></div>')
        for qi, (pts, q, a) in enumerate(s["qs"]):
            sp = "sp-b" if pts == 3 else "sp-a"
            out.append(f'<div class="qa"><p class="q"><strong>{letter}{qi + 1}. ({pts} points)</strong> {esc(q)}</p><div class="{sp}"></div><p class="look">Reviews Entry {ENTRY[s["unit"]]} · {esc(UNAME[s["unit"]])}</p></div>')
            src_key.append((f"{letter}{qi + 1}", pts, a))

    # Key
    out.append('<div class="key"><h2>Teacher Answer Key</h2><h3>Part 1: Matching</h3>')
    for i, (uid, term, dfn) in enumerate(pairs):
        out.append(f"<p><strong>{i + 1}. {esc(term)}: {letter_of[term]}</strong> (Entry {ENTRY[uid]})</p>")
    out.append("<h3>Part 2: Multiple Choice</h3>")
    for i, ((uid, stem, opts), letter) in enumerate(zip(MC[variant], mc_key)):
        out.append(f"<p><strong>{i + 1}. {letter}</strong> (Entry {ENTRY[uid]} · {esc(UNAME[uid])})</p>")
    out.append("<h3>Part 3: Sources</h3>")
    for tag, pts, a in src_key:
        out.append(f"<p><strong>{tag}. ({pts} points)</strong> {esc(a)}</p>")
    out.append("</div></body></html>")
    doc = "".join(out)
    d = os.path.join(HERE, f"practice-test-{variant}")
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, f"{variant}-practice-test.html")
    open(path, "w").write(doc)
    cov = {UNAME[u]: coverage[ENTRY[u]] for u in unit_ids}
    print(f"{variant}: MC key spread {dict(sorted(spread.items()))} | coverage {cov} -> {path}")


for v, (vn, us, sd) in VARIANTS.items():
    build(v, vn, us, sd)
