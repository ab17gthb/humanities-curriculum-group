#!/usr/bin/env python3
"""Survey: map every catalog PDF to its proposed footer-left label.

Derives the label from the sibling HTML <title>:
  "Guided Notes: X"        -> "X · Guided Notes"   (type from filename)
  "Teacher Notes · X"      -> "X · Teacher Notes"
  "Unit — Lesson N — X — Teacher Notes Guide" -> "X · Teacher Notes Guide"
  "Quick Check: Y"         -> "Y · Quick Check"    (Y is the doc's own topic)
  "Network Map: X"         -> "X · Activity"       (activity name dropped)
  "X" (plain)              -> "X · <type from filename>"
Writes mapping.json {pdf_path: label} and prints pattern/anomaly report.
"""
import json, os, re, sys
from collections import Counter

ROOT = os.path.expanduser("~/workspace/curriculum-planner")
UNITS = ["colonial-america", "the-founding", "early-republic", "jackson-reform",
         "sectional-crisis", "reconstruction", "gilded-age", "progressive-era",
         "imperialism-wwi", "twenties", "depression-new-deal", "world-war-ii",
         "cold-war", "civil-rights", "modern-america", "course-review"]
EXCLUDE = re.compile(r"(funnel\.pdf|-v[2-9]\.pdf|-logo\.pdf|-slides-test\.pdf)$")

TYPE_LABEL = [
    ("-teacher-notes-guide", "Teacher Notes Guide"),
    ("-teacher-notes", "Teacher Notes"),
    ("-guided-notes", "Guided Notes"),
    ("-quick-check", "Quick Check"),
    ("-notebook", "Notebook Page"),
    ("-reading", "Reading"),
    ("-writing", "Writing Task"),
    ("-activity", "Activity"),
    ("unit-test", "Unit Test"),
    ("review-study-guide", "Study Guide"),
    ("-study-guide", "Study Guide"),
    ("review-crossword", "Crossword"),
    ("-crossword", "Crossword"),
    ("-practice-test", "Practice Test"),
    ("-review-packet", "Review Packet"),
    ("-skills-task", "Skills Task"),
    ("-term-sprint", "Term Sprint"),
    ("-teacher-guide", "Teacher Guide"),
    ("-practice-set", "Practice Set"),
]

def type_label(fname):
    stem = fname[:-4] if fname.endswith(".pdf") else fname
    for key, label in TYPE_LABEL:
        if stem.endswith(key) or key in stem:
            return label
    return None

def title_of(html_path):
    try:
        html = open(html_path, encoding="utf-8", errors="replace").read(6000)
    except OSError:
        return None
    m = re.search(r"<title>(.*?)</title>", html, re.S)
    if not m:
        return None
    return re.sub(r"\s+", " ", m.group(1)).strip()

def label_for(title, tlabel):
    if title is None or tlabel is None:
        return None, "missing title or type"
    # "Unit — Lesson N — Lesson Title — Teacher Notes Guide"
    m = re.match(r"^(.*?) — Lesson \d+ — (.*?) — (.*)$", title)
    if m:
        return f"{m.group(2)} · {m.group(3)}", "dash-format"
    # "Teacher Notes · Lesson Title · Teacher Notes Guide" (early-build guides)
    if title.endswith(" · Teacher Notes Guide"):
        parts = title.split(" · ")
        mid = parts[1:-1] if parts[0] == "Teacher Notes" else parts[:-1]
        if mid:
            return " · ".join(mid) + " · Teacher Notes Guide", "guide-format"
    # Early guides titled like teacher notes: "Teacher Notes · X" in a guide file
    if tlabel == "Teacher Notes Guide" and title.startswith("Teacher Notes · "):
        return title[len("Teacher Notes · "):] + " · Teacher Notes Guide", "guide-format"
    # "Teacher Notes · X"
    m = re.match(r"^(.*?) · (.*)$", title)
    if m and m.group(1) == tlabel:
        return f"{m.group(2)} · {tlabel}", "dot-swap"
    # "Prefix: Subject"
    if ": " in title:
        head, rest = title.split(": ", 1)
        return f"{rest} · {tlabel}", "colon-split"
    return f"{title} · {tlabel}", "plain"

def main():
    mapping, anomalies, rules = {}, [], Counter()
    for unit in UNITS:
        for dirpath, _dirs, files in os.walk(os.path.join(ROOT, unit)):
            for f in sorted(files):
                if not f.endswith(".pdf") or EXCLUDE.search(f):
                    continue
                pdf = os.path.join(dirpath, f)
                rel = os.path.relpath(pdf, ROOT)
                html = pdf[:-4] + ".html"
                title = title_of(html)
                tlabel = type_label(f)
                label, rule = label_for(title, tlabel)
                if label is None:
                    anomalies.append((rel, f"title={title!r} type={tlabel!r}"))
                    continue
                rules[rule] += 1
                mapping[rel] = label
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mapping.json")
    with open(out, "w") as fh:
        json.dump(mapping, fh, indent=1, ensure_ascii=False)
    print(f"mapped: {len(mapping)}  anomalies: {len(anomalies)}")
    print("rules:", dict(rules))
    for a in anomalies[:40]:
        print("ANOMALY:", a)
    labels = Counter(mapping.values())
    print("distinct labels:", len(labels))

if __name__ == "__main__":
    main()
