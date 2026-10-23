#!/usr/bin/env python3
"""Generate Band 3 term sprint HTML + teacher key fragment from the audited
Rycal staging JSONs, so every printed definition is byte-identical to the
units' guided notes. Run: python3 gen_sprint.py"""
import json, random, os

BASE = os.path.expanduser("~/workspace/rycal/course-staging")
OUT = os.path.dirname(os.path.abspath(__file__))

def load(slug):
    rows = json.load(open(os.path.join(BASE, slug, "vocab-audited.json")))
    return {r["term"]: r for r in rows}

SC = load("hcg-sectional-crisis")
RC = load("hcg-reconstruction")

PART_A = [  # matching set 1: 20 terms, mixed units
    "Compromise of 1850", "Fugitive Slave Act", "Uncle Tom's Cabin",
    "Kansas-Nebraska Act", "popular sovereignty", "Republican Party",
    "Dred Scott v. Sandford", "Freeport Doctrine", "secession",
    "Emancipation Proclamation",
    "presidential Reconstruction", "Black Codes", "Civil Rights Act of 1866",
    "Fourteenth Amendment", "Reconstruction Acts", "Fifteenth Amendment",
    "sharecropping", "Ku Klux Klan", "Enforcement Acts",
    "Compromise of 1877",
]
PART_C = [  # matching set 2: the other 20
    "personal liberty laws", "higher law", "Bleeding Kansas",
    "Confederate States of America", "Anaconda Plan", "Antietam",
    "Gettysburg", "total war", "Thirteenth Amendment",
    "Second Inaugural Address",
    "Freedmen's Bureau", "Radical Republicans", "impeachment",
    "Union League", "crop lien", "freedmen's schools",
    "Slaughter-House Cases", "Panic of 1873", "White League", "Redemption",
]
ALL = {**SC, **RC}
for t in PART_A + PART_C:
    assert t in ALL, t

def matching_block(terms, start_no, seed):
    defs = [(t, ALL[t]["definition"]) for t in terms]
    order = list(range(len(terms)))
    random.Random(seed).shuffle(order)
    letters = "abcdefghijklmnopqrst"
    letter_of = {}
    defrows = []
    for pos, idx in enumerate(order):
        letter_of[terms[idx]] = letters[pos]
        defrows.append((letters[pos], defs[idx][1]))
    termrows = "".join(
        f"<tr><td class='no'>{start_no + i}</td><td class='tm'>{t}</td>"
        f"<td class='ans'>_____</td></tr>"
        for i, t in enumerate(terms))
    deflist = "".join(f"<p class='def'><strong>{L}.</strong> {d}</p>" for L, d in defrows)
    keylist = "; ".join(f"{start_no + i}. {letter_of[t]}" for i, t in enumerate(terms))
    return termrows, deflist, keylist

HEAD = """<!DOCTYPE html><html><head><meta charset="utf-8">
<title>Band 3 Term Sprint</title><style>
@page { size: letter; margin: 0.55in 0.75in 0.7in; }
* { box-sizing: border-box; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 11.5pt; color: #000; line-height: 1.35; margin: 0; }
.nameline { display: flex; justify-content: space-between; gap: 1em; }
h1 { font-family: Georgia, serif; font-size: 19pt; margin: 12pt 0 4pt; line-height: 1.2; color: #1b2a4a; }
h2 { font-family: Georgia, serif; font-size: 14.5pt; margin: 16pt 0 6pt; color: #1b2a4a; }
h3 { font-size: 12.5pt; margin: 14pt 0 4pt; break-after: avoid; }
p { margin: 0 0 7pt; }
.directions { margin-bottom: 4pt; }
.brandmark { margin: 0 0 4pt; line-height: 0; } .brandmark img { width: 1.35in; }
table.terms { border-collapse: collapse; width: 100%; margin: 4pt 0 10pt; }
table.terms td { padding: 2.4pt 6pt; border-bottom: 0.5pt solid #999; vertical-align: top; }
td.no { width: 0.35in; } td.tm { } td.ans { width: 0.7in; text-align: center; }
.def { margin: 0 0 3.5pt; font-size: 11pt; }
.q { margin: 10pt 0 0; }
.rule { border-top: 1.6pt solid #b3543f; margin: 6pt 0 10pt; }
.sp-a { height: 0.66in; } .sp-b { height: 0.9in; }
</style></head><body>
<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>
<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>
<h1>Band 3 Term Sprint: Slavery, War, and the Unfinished Settlement</h1>
<div class="rule"></div>
<p class="directions"><strong>Directions:</strong> Forty terms from the Sectional Crisis and Reconstruction units, in two matching sets and a short-answer round. Work from memory first. The definitions are the ones printed in your guided notes, word for word, so a miss tells you exactly which lesson's notes to reopen.</p>
"""

a_terms, a_defs, a_key = matching_block(PART_A, 1, 3103)
c_terms, c_defs, c_key = matching_block(PART_C, 21, 7702)

PART_B = """
<h2>Part B: Use the Term</h2>
<p>Answer in one or two sentences each. Name the term that fits, then use it correctly.</p>
<p class="q"><strong>41.</strong> A state law passed to obstruct the federal fugitive law, by guaranteeing a jury trial the federal law denied.</p><div class="sp-a"></div>
<p class="q"><strong>42.</strong> The doctrine Stephen A. Douglas offered at Freeport to keep popular sovereignty alive after the Dred Scott decision.</p><div class="sp-a"></div>
<p class="q"><strong>43.</strong> The Union's opening strategy of blockade and control of the Mississippi River, named for the snake it resembled.</p><div class="sp-a"></div>
<p class="q"><strong>44.</strong> The system under which a family farmed another man's land for a share of the crop, settling accounts once a year.</p><div class="sp-a"></div>
<p class="q"><strong>45.</strong> The 1873 Supreme Court decision that read the Fourteenth Amendment's privileges or immunities clause down to almost nothing.</p><div class="sp-a"></div>
<p class="q"><strong>46.</strong> The president's plan of 1865 that restored the seceded states on pardons and repudiation of secession, with no federal guarantee of freedpeople's rights.</p><div class="sp-a"></div>
<p class="q"><strong>47.</strong> The September 1862 battle whose outcome let Lincoln issue the preliminary Emancipation Proclamation.</p><div class="sp-a"></div>
<p class="q"><strong>48.</strong> The secret political society freedpeople and Republicans built across the South to register voters and protect them.</p><div class="sp-a"></div>
"""

html = (HEAD
    + "<h2>Part A: Matching, First Twenty</h2><table class='terms'>" + a_terms + "</table>" + a_defs
    + "<h2>Part C: Matching, Second Twenty</h2><table class='terms'>" + c_terms + "</table>" + c_defs
    + PART_B
    + "</body></html>")
open(os.path.join(OUT, "day-3-term-sprint.html"), "w").write(html)

key = ("<h3>Term sprint key</h3>\n"
       f"<p><strong>Part A:</strong> {a_key}.</p>\n"
       f"<p><strong>Part C:</strong> {c_key}.</p>\n"
       "<p><strong>Part B:</strong> 41. personal liberty laws. 42. Freeport Doctrine. "
       "43. Anaconda Plan. 44. sharecropping. 45. Slaughter-House Cases. "
       "46. presidential Reconstruction. 47. Antietam. 48. Union League. "
       "Accept the term with any accurate use of it; the matching definitions are "
       "printed verbatim in the student sprint itself, so students can self-check "
       "every miss against the guided-notes wording.</p>\n")
open(os.path.join(OUT, "sprint-key-fragment.html"), "w").write(key)
print("sprint + key fragment written;", len(html), "bytes")
