#!/usr/bin/env python3
"""Shared Course Review sprint generator. Each band folder carries a
sprint-config.json: {day, title, entries: [slugA, slugB], partA: [terms],
partC: [terms], partB: [[prompt, answerTerm], ...], seedA, seedC}.
Definitions are pulled from the audited Rycal staging JSONs so every printed
definition is byte-identical to the units' guided notes.
Usage: python3 gen_sprint.py <band-dir>"""
import json, random, os, sys

BASE = os.path.expanduser("~/workspace/rycal/course-staging")
band_dir = os.path.abspath(sys.argv[1])
cfg = json.load(open(os.path.join(band_dir, "sprint-config.json")))

ALL = {}
for slug in cfg["entries"]:
    for r in json.load(open(os.path.join(BASE, slug, "vocab-audited.json"))):
        ALL[r["term"]] = r
for t in cfg["partA"] + cfg["partC"]:
    assert t in ALL, t
for prompt, ans in cfg["partB"]:
    assert ans in ALL, ans

def matching_block(terms, start_no, seed):
    order = list(range(len(terms)))
    random.Random(seed).shuffle(order)
    letters = "abcdefghijklmnopqrst"
    letter_of, defrows = {}, []
    for pos, idx in enumerate(order):
        letter_of[terms[idx]] = letters[pos]
        defrows.append((letters[pos], ALL[terms[idx]]["definition"]))
    termrows = "".join(
        f"<tr><td class='no'>{start_no + i}</td><td class='tm'>{t}</td><td class='ans'>_____</td></tr>"
        for i, t in enumerate(terms))
    deflist = "".join(f"<p class='def'><strong>{L}.</strong> {d}</p>" for L, d in defrows)
    keylist = "; ".join(f"{start_no + i}. {letter_of[t]}" for i, t in enumerate(terms))
    return termrows, deflist, keylist

HEAD = """<!DOCTYPE html><html><head><meta charset="utf-8">
<title>Band {day} Term Sprint</title><style>
@page {{ size: letter; margin: 0.55in 0.75in 0.7in; }}
* {{ box-sizing: border-box; }}
body {{ font-family: Arial, Helvetica, sans-serif; font-size: 11.5pt; color: #000; line-height: 1.35; margin: 0; }}
.nameline {{ display: flex; justify-content: space-between; gap: 1em; }}
h1 {{ font-family: Georgia, serif; font-size: 19pt; margin: 12pt 0 4pt; line-height: 1.2; color: #1b2a4a; }}
h2 {{ font-family: Georgia, serif; font-size: 14.5pt; margin: 16pt 0 6pt; color: #1b2a4a; }}
p {{ margin: 0 0 7pt; }}
.directions {{ margin-bottom: 4pt; }}
.brandmark {{ margin: 0 0 4pt; line-height: 0; }} .brandmark img {{ width: 1.35in; }}
table.terms {{ border-collapse: collapse; width: 100%; margin: 4pt 0 10pt; }}
table.terms td {{ padding: 2.4pt 6pt; border-bottom: 0.5pt solid #999; vertical-align: top; }}
td.no {{ width: 0.35in; }} td.ans {{ width: 0.7in; text-align: center; }}
.def {{ margin: 0 0 3.5pt; font-size: 11pt; }}
.q {{ margin: 10pt 0 0; }}
.rule {{ border-top: 1.6pt solid #b3543f; margin: 6pt 0 10pt; }}
.sp-a {{ height: 0.66in; }}
</style></head><body>
<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>
<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>
<h1>Band {day} Term Sprint: {title}</h1>
<div class="rule"></div>
<p class="directions"><strong>Directions:</strong> Forty terms from the two units of this band, in two matching sets and a short-answer round. Work from memory first. The definitions are the ones printed in your guided notes, word for word, so a miss tells you exactly which lesson's notes to reopen.</p>
"""

a_terms, a_defs, a_key = matching_block(cfg["partA"], 1, cfg["seedA"])
c_terms, c_defs, c_key = matching_block(cfg["partC"], 21, cfg["seedC"])
part_b = "".join(
    f"<p class='q'><strong>{41 + i}.</strong> {p}</p><div class='sp-a'></div>"
    for i, (p, a) in enumerate(cfg["partB"]))
part_b_key = " ".join(f"{41 + i}. {a}." for i, (p, a) in enumerate(cfg["partB"]))

html = (HEAD.format(day=cfg["day"], title=cfg["title"])
    + "<h2>Part A: Matching, First Twenty</h2><table class='terms'>" + a_terms + "</table>" + a_defs
    + "<h2>Part C: Matching, Second Twenty</h2><table class='terms'>" + c_terms + "</table>" + c_defs
    + "<h2>Part B: Use the Term</h2><p>Answer in one or two sentences each. Name the term that fits, then use it correctly.</p>"
    + part_b + "</body></html>")
open(os.path.join(band_dir, f"day-{cfg['day']}-term-sprint.html"), "w").write(html)

key = ("<h3>Term sprint key</h3>\n"
       f"<p><strong>Part A:</strong> {a_key}.</p>\n"
       f"<p><strong>Part C:</strong> {c_key}.</p>\n"
       f"<p><strong>Part B:</strong> {part_b_key} "
       "Accept the term with any accurate use of it; the matching definitions are "
       "printed verbatim in the student sprint itself, so students can self-check "
       "every miss against the guided-notes wording.</p>\n")
open(os.path.join(band_dir, "sprint-key-fragment.html"), "w").write(key)
print(f"band {cfg['day']} sprint written")
