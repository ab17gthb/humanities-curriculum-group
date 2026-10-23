#!/usr/bin/env python3
"""Reading-only pass tooling.
Usage: reading_only_screen.py <unit-slug> [digest|screen]
Builds a digest (student text + questions + key per reading/QC doc) and a
token screen flagging key sentences with numbers/dates/names absent from the
document's own student text.
"""
import glob
import os
import re
import sys
import html as h

ROOT = os.path.expanduser("~/workspace/curriculum-planner")


def extract(path):
    s = open(path).read()
    s = re.sub(r"<script.*?</script>|<style.*?</style>", "", s, flags=re.S)
    s = re.sub(r"<[^>]+>", "\n", s)
    s = h.unescape(s)
    lines = [l.strip() for l in s.split("\n")]
    return "\n".join(l for l in lines if l)


def split_key(text):
    i = text.find("Teacher Answer Key")
    if i == -1:
        return text, ""
    return text[:i], text[i:]


NUM = re.compile(r"\$?\d[\d,\.]*%?")
NAME = re.compile(r"\b(?:[A-Z][a-z]+(?:\s+(?:of|the|de|and)\s+|\s+)[A-Z][a-z]+|[A-Z][a-z]{3,})\b")
STOP = {"The", "This", "That", "These", "Those", "One", "Two", "Three", "Four",
        "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Full", "Credit",
        "Blueprint", "Question", "Answer", "Part", "Section", "Lesson",
        "Reading", "Teacher", "Student", "Students", "First", "Second",
        "Third", "Point", "Points", "Accept", "Note", "Key"}


def screen_doc(student, key):
    flags = []
    low = student.lower()
    for sent in re.split(r"(?<=[\.\!\?])\s+", key.replace("\n", " ")):
        sent = sent.strip()
        if len(sent) < 25:
            continue
        missing = []
        for tok in NUM.findall(sent):
            t = tok.strip("$,. ")
            if t and t not in student and tok not in student:
                missing.append(tok)
        for name in NAME.findall(sent):
            if name.split()[0] in STOP:
                continue
            if name.lower() not in low:
                missing.append(name)
        if missing:
            flags.append((missing, sent[:220]))
    return flags


def main():
    slug = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else "screen"
    unit_dir = os.path.join(ROOT, slug)
    docs = []
    for n in range(1, 9):
        for kind in ("reading", "quick-check"):
            p = os.path.join(unit_dir, f"lesson-0{n}", f"lesson-0{n}-{kind}.html")
            if os.path.exists(p):
                docs.append((n, kind, p))
    if mode == "digest":
        out = []
        for n, kind, p in docs:
            student, key = split_key(extract(p))
            out.append(f"\n{'='*70}\nLESSON {n} {kind.upper()}\n{'='*70}\n"
                       f"--- STUDENT TEXT ---\n{student}\n--- KEY ---\n{key}")
        dest = f"/tmp/ro-digest-{slug}.txt"
        open(dest, "w").write("\n".join(out))
        print(f"digest: {dest} ({os.path.getsize(dest)} bytes, {len(docs)} docs)")
    else:
        total = 0
        for n, kind, p in docs:
            student, key = split_key(extract(p))
            flags = screen_doc(student, key)
            total += len(flags)
            if flags:
                print(f"\n--- L{n} {kind}: {len(flags)} flagged key sentences ---")
                for missing, sent in flags:
                    print(f"  MISSING {missing}\n    {sent}")
        print(f"\n{slug}: {total} flagged sentences across {len(docs)} docs")


if __name__ == "__main__":
    main()
