#!/usr/bin/env python3
"""Generate the three Course Review registry blocks and insert them into
planner-data.js: per-variant BLUEPRINT, TOPICS, BP_TOPIC, LESSONS, ITEMS,
and TPSP globals, plus the HCG_UNITS registry entries (rv u15, re u16,
rm u17). Blueprint spans are aligned to the units' printed topicsHeads.
TPSP pickers collect the premium DBQ entries (dbq: true) from each
variant's units, retagged to the variant entry of the DBQ's home unit.

Run: python3 gen_registry.py  (dry output to registry-insert.js; --apply
inserts into planner-data.js after verifying anchors)
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PD = os.path.join(HERE, "..", "site", "public", "planner-data.js")

UNITS = ["ca", "fd", "er", "jr", "sc", "rc", "ga", "pe", "wwi", "tw",
         "dp", "ww2", "cw", "cr", "ma"]
BAND_UNITS = {1: ["ca", "fd"], 2: ["er", "jr"], 3: ["sc", "rc"],
              4: ["ga", "pe"], 5: ["wwi", "tw"], 6: ["dp", "ww2"],
              7: ["cw", "cr"], 8: ["ma"]}

BLUEPRINT_TEXT = {
    "ca": "Colonial America, 1491–1763: the meeting of Europe, Africa, and the Americas, and the colonial societies built from it",
    "fd": "The Founding, 1763–1791: the imperial crisis, independence, and the constitutional settlement",
    "er": "Early Republic and Expansion, 1789–1848: the working republic, its parties, its courts, and its doubling in size",
    "jr": "Jackson and Reform, 1828–1848: mass democracy's widening, its boundaries, and the reform movements it bred",
    "sc": "Sectional Crisis and Civil War, 1850–1865: the failure of compromise over slavery and the war that settled the Union",
    "rc": "Reconstruction, 1865–1877: the amendments' settlement of freedom and citizenship, and its undoing",
    "ga": "The Gilded Age, 1877–1900: industrial capitalism's transformation and the resistance it organized",
    "pe": "Progressive Era, 1877–1920: the reform answer to industrialism, in the city, the state, and the federal government",
    "wwi": "Imperialism and World War I, 1898–1920: the reach for empire, the Great War, and the peace that failed in the Senate",
    "tw": "The Twenties, 1920–1929: prosperity's transformation of American life and the weaknesses inside it",
    "dp": "Depression and New Deal, 1929–1939: the collapse, the experimentation, and the federal government's new settlement",
    "ww2": "World War II, 1935–1945: the road to war, total mobilization, the two-ocean victory, and the reckoning",
    "cw": "The Cold War, 1945–1991: containment's architecture, its wars, its home front, and its end from inside",
    "cr": "Civil Rights, 1947–1978: the movement's foundations, its legal victories, and its unfinished agenda",
    "ma": "Modern America, 1978–present: the conservative turn, globalization, the digital remaking, and the polarized present",
}
BP_TOPIC = {
    "ca": [2, 3], "fd": [1, 2], "er": [1, 2], "jr": [1, 3], "sc": [1, 3],
    "rc": [1, 3], "ga": [3, 4], "pe": [4, 6], "wwi": [1, 5], "tw": [4, 6],
    "dp": [1, 4], "ww2": [3, 5], "cw": [1, 5], "cr": [3, 6], "ma": [1, 4],
}
TOPICS = {
    1: "Federal power and the Constitution",
    2: "Expansion and its costs",
    3: "Slavery, race, and rights",
    4: "Industrial capitalism and labor",
    5: "America in the world",
    6: "Reform movements",
}
BAND_QUESTIONS = {
    1: "How did the meeting of three worlds produce colonial societies, and how did those societies become a republic?",
    2: "How did the new republic learn to govern itself, and whose democracy did Jackson's age build?",
    3: "How did compromise over slavery fail, and what did the war and its settlement settle?",
    4: "How did industrial growth transform American life, and how did reformers answer it?",
    5: "Why did the United States reach for power abroad, and what did the war and the prosperous decade do at home?",
    6: "How did depression and total war remake the federal government and the country's place in the world?",
    7: "How did the Cold War abroad and the movement at home change what the federal government protects?",
    8: "What did the remaking after 1980 settle, and what did it leave open?",
}
FLEX_Q = "Which band do the practice sets say to reopen, and can you close it today?"

VARIANTS = {
    "rv": dict(name="Course Review", course="u15", bands=[1, 2, 3, 4, 5, 6, 7, 8],
               prefix="hcg/course-review/", page="course-review.html", slug="course-review",
               fitmin=7, eq="How did the United States become what it is, and which of the course's own arguments best explains the country that resulted?",
               head="The Whole Course, 1491–present", cross_n=60),
    "re": dict(name="Early Course Review", course="u16", bands=[1, 2, 3],
               prefix="hcg/early-review/", page="early-review.html", slug="early-review",
               fitmin=4, eq="How did a fringe of British colonies become a continental republic, and what did its founding settlements settle and leave open?",
               head="America to 1877, 1491–1877", cross_n=24),
    "rm": dict(name="Modern Course Review", course="u17", bands=[4, 5, 6, 7, 8],
               prefix="hcg/modern-review/", page="modern-review.html", slug="modern-review",
               fitmin=5, eq="How did industrial America remake the nation's economy, its democracy, and its place in the world, and what did the remaking leave unsettled?",
               head="America Since 1877, 1877–present", cross_n=36),
}


def band_title(n):
    h = open(os.path.join(HERE, f"band-{n}", f"day-{n}-review-packet.html")).read()
    m = re.search(r"<h1>Band \d+ Review Packet: (.*?)</h1>", h)
    return m.group(1)


def skills_title(n):
    h = open(os.path.join(HERE, f"band-{n}", f"day-{n}-skills-task.html")).read()
    m = re.search(r"<h1>Band \d+ Skills Task: (.*?)</h1>", h)
    return m.group(1) if m else "Skills task"


def js_str(s):
    return json.dumps(s, ensure_ascii=False).replace("–", "\\u2013")


def extract_tpsp_dbqs(src):
    """Return {unit_upper: [dbq objects]} parsed from planner-data.js."""
    out = {}
    for m in re.finditer(r"window\.HCG_TPSP_([A-Z0-9]+) = \[", src):
        upper = m.group(1)
        depth, i = 0, m.end() - 1
        start = i
        while True:
            ch = src[i]
            if ch == "[":
                depth += 1
            elif ch == "]":
                depth -= 1
                if depth == 0:
                    break
            i += 1
        arr = json.loads(src[start:i + 1])
        out[upper] = [o for o in arr if o.get("dbq")]
    return out


def variant_block(vid, cfg, dbqs_by_unit):
    unit_ids = [u for b in cfg["bands"] for u in BAND_UNITS[b]]
    entry_of = {u: i + 1 for i, u in enumerate(unit_ids)}
    U = vid.upper()
    lines = []
    # Blueprint
    lines.append(f"window.HCG_{U}_BLUEPRINT = {{")
    for u in unit_ids:
        lines.append(f"  {entry_of[u]}: {js_str(BLUEPRINT_TEXT[u])},")
    lines.append("};")
    # Lessons (bands + flex)
    lines.append(f"window.HCG_{U}_LESSONS = [")
    for i, b in enumerate(cfg["bands"], 1):
        lines.append(f"  {{ n: {i}, title: {js_str('Band ' + str(b) + ': ' + band_title(b))}, question: {js_str(BAND_QUESTIONS[b])} }},")
    flex_n = len(cfg["bands"]) + 1
    lines.append(f"  {{ n: {flex_n}, title: \"Flex Day: The Study Guide and the Crossword\", question: {js_str(FLEX_Q)} }}")
    lines.append("];")
    # Items
    lines.append(f"window.HCG_{U}_ITEMS = [")
    for i, b in enumerate(cfg["bands"], 1):
        tags = [entry_of[u] for u in BAND_UNITS[b]]
        t = band_title(b)
        p = cfg["prefix"]
        lines.append(f"  // Band {b}")
        lines.append(f"  {{ id: \"{vid}{i}-packet\", lesson: {i}, kind: \"Packet\", name: {js_str(t + ' review packet')}, days: 1, tags: {tags}, storage: \"{p}band-{b}-packet.pdf\", core: true }},")
        lines.append(f"  {{ id: \"{vid}{i}-sprint\", lesson: {i}, kind: \"Term Sprint\", name: \"Band {b} term sprint\", days: 0, tags: {tags}, storage: \"{p}band-{b}-sprint.pdf\", core: true }},")
        lines.append(f"  {{ id: \"{vid}{i}-practice\", lesson: {i}, kind: \"Practice Set\", name: \"Band {b} practice set\", days: 0, tags: {tags}, storage: \"{p}band-{b}-practice.pdf\", core: true }},")
        lines.append(f"  {{ id: \"{vid}{i}-skills\", lesson: {i}, kind: \"Skills Task\", name: {js_str('Skills task: ' + skills_title(b))}, days: 0, tags: {tags}, storage: \"{p}band-{b}-skills.pdf\" }},")
    lines.append(f"  {{ id: \"{vid}-guide\", lesson: {flex_n}, kind: \"Review\", name: \"Study guide (flex day)\", days: 1, tags: [], storage: \"{cfg['prefix']}study-guide.pdf\", core: true }},")
    lines.append(f"  {{ id: \"{vid}-cross\", lesson: {flex_n}, kind: \"Review\", name: \"Crossword ({cfg['cross_n']} answers)\", days: 0.5, tags: [], storage: \"{cfg['prefix']}crossword.pdf\" }}")
    lines.append("];")
    # Topics
    lines.append(f"window.HCG_{U}_TOPICS = {{")
    for n, label in TOPICS.items():
        lines.append(f"  {n}: {{ label: {js_str(label)}, note: \"\" }},")
    lines.append("};")
    # BP topic map
    lines.append(f"window.HCG_{U}_BP_TOPIC = {{")
    for u in unit_ids:
        lines.append(f"  {entry_of[u]}: {BP_TOPIC[u]},")
    lines.append("};")
    # TPSP: premium DBQs from the variant's units, retagged
    entries = []
    for u in unit_ids:
        for o in dbqs_by_unit.get(u.upper(), []):
            e = dict(o)
            e["bp"] = [entry_of[u]]
            entries.append(e)
    lines.append(f"window.HCG_TPSP_{U} = " + json.dumps(entries, ensure_ascii=False, indent=1) + ";")
    # Registry entry
    reg = f"""  {vid}: {{
    id: "{vid}", courseId: "{cfg['course']}", key: "hcg_unit_{vid}_v1",
    fitMin: {cfg['fitmin']},
    name: "{cfg['name']}", shortName: "{cfg['name']}",
    essentialQuestion: {js_str(cfg['eq'])},
    topicsHead: {js_str(cfg['head'])},
    tpspIntro: "From The Primary Source Project's premium DBQ library. Every premium DBQ is a complete document essay on one unit of the course; click one to add it as a writing day. Each arrives pre-tagged to the unit it reviews, and you can retag any of them with Edit.",
    testFile: null, testStorage: "{cfg['prefix']}practice-test.pdf", testName: "practice-test.pdf",
    icsSlug: "{cfg['slug']}", rycalDeck: "https://rycal.web.app/hcg-{cfg['slug']}-flashcards", exportFile: "hcg-unit-plan-{cfg['slug']}.json",
    blueprint: window.HCG_{U}_BLUEPRINT, lessons: window.HCG_{U}_LESSONS, items: window.HCG_{U}_ITEMS,
    topics: window.HCG_{U}_TOPICS, bpTopic: window.HCG_{U}_BP_TOPIC, tpsp: window.HCG_TPSP_{U},
    unitPage: "{cfg['page']}"
  }}"""
    return "\n".join(lines), reg, len(entries)


def main():
    src = open(PD).read()
    dbqs = extract_tpsp_dbqs(src)
    print("DBQs per unit:", {k: len(v) for k, v in dbqs.items() if v},
          "| total:", sum(len(v) for v in dbqs.values()))
    globals_txt, regs = [], []
    for vid, cfg in VARIANTS.items():
        g, r, n = variant_block(vid, cfg, dbqs)
        globals_txt.append(g)
        regs.append(r)
        print(f"{vid}: TPSP DBQ entries: {n}")
    out = "\n\n".join(globals_txt)
    open(os.path.join(HERE, "registry-globals.js"), "w").write(out + "\n")
    open(os.path.join(HERE, "registry-entries.js"), "w").write(",\n".join(regs) + "\n")
    print("globals chars:", len(out))
    if "--apply" in sys.argv:
        anchor = "window.HCG_UNITS = {"
        assert src.count(anchor) == 1
        src = src.replace(anchor, out + "\n\n" + anchor, 1)
        # insert registry entries before the HCG_UNITS closing: the object's
        # final entry ends with the last "  }\n};" after the anchor.
        start = src.find(anchor)
        tail = src.rfind("\n};", start)
        assert tail > start
        src = src[:tail] + ",\n" + ",\n".join(regs) + src[tail:]
        open(PD, "w").write(src)
        print("APPLIED to planner-data.js")


if __name__ == "__main__":
    main()
