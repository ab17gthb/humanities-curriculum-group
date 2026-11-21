# Explicit disk -> storage mapping for the 73 review objects (verified
# against live objects by page count + content before upload).
MAP = {}
KIND = {"packet": "review-packet", "sprint": "term-sprint",
        "practice": "practice-set", "skills": "skills-task"}
for band in range(1, 9):
    for sk, dk in KIND.items():
        disk = f"course-review/band-{band}/day-{band}-{dk}.pdf"
        MAP[f"hcg/course-review/band-{band}-{sk}.pdf"] = disk
        if band <= 3:
            MAP[f"hcg/early-review/band-{band}-{sk}.pdf"] = disk
        else:
            MAP[f"hcg/modern-review/band-{band}-{sk}.pdf"] = disk
for scope, tag in [("course-review", "combined"), ("early-review", "early"),
                   ("modern-review", "modern")]:
    MAP[f"hcg/{scope}/study-guide.pdf"] = f"course-review/study-guide-{tag}/{tag}-study-guide.pdf"
    MAP[f"hcg/{scope}/practice-test.pdf"] = f"course-review/practice-test-{tag}/{tag}-practice-test.pdf"
    MAP[f"hcg/{scope}/crossword.pdf"] = f"course-review/crossword-{tag}/{tag}-crossword.pdf"
