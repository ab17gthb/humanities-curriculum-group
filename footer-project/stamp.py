#!/usr/bin/env python3
"""Stamp the HCG footer onto catalog PDFs (in place, idempotent).

Footer (Alex's spec, 2026-10-28): small gray text at the bottom margin —
left:  "<Lesson title> · <Doc type>"   (from mapping.json)
right: "© Humanities Curriculum Group · Page X of Y"
Sits at y=25pt, inside the documents' 0.7in (50.4pt) bottom margin, so no
content or pagination changes. Skips any PDF already carrying the footer.

Usage: stamp.py PREFIX [PREFIX ...]   (e.g. stamp.py gilded-age/)
       stamp.py --all
Writes stamp-report.jsonl next to this script.
"""
import io, json, os, sys
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase.pdfmetrics import stringWidth

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.expanduser("~/workspace/curriculum-planner")
BRAND = "© Humanities Curriculum Group"
MARKER = "© Humanities Curriculum Group · Page"
FONT, SIZE, COLOR = "Helvetica", 7.5, HexColor("#595959")
X_MARGIN, Y_BASE = 54.0, 25.0  # 0.75in sides (matches @page), inside 0.7in bottom margin

def overlay(w, h, left, right):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(w, h))
    c.setFont(FONT, SIZE)
    c.setFillColor(COLOR)
    c.drawString(X_MARGIN, Y_BASE, left)
    c.drawRightString(w - X_MARGIN, Y_BASE, right)
    c.save()
    buf.seek(0)
    return PdfReader(buf).pages[0]

def stamp(path, label):
    reader = PdfReader(path)
    n = len(reader.pages)
    first_text = reader.pages[0].extract_text() or ""
    if MARKER in first_text:
        return {"file": path, "pages": n, "status": "already-stamped"}
    # overlap guard: left + right must fit the usable width on every page size
    sizes = {(float(p.mediabox.width), float(p.mediabox.height)) for p in reader.pages}
    for (w, _h) in sizes:
        right_worst = f"{BRAND} · Page {n} of {n}"
        need = stringWidth(label, FONT, SIZE) + stringWidth(right_worst, FONT, SIZE)
        if need > w - 2 * X_MARGIN - 12:
            return {"file": path, "pages": n, "status": "too-wide",
                    "need": round(need, 1), "usable": round(w - 2 * X_MARGIN, 1)}
    writer = PdfWriter()
    for i, page in enumerate(reader.pages, 1):
        w, h = float(page.mediabox.width), float(page.mediabox.height)
        right = f"{BRAND} · Page {i} of {n}"
        page.merge_page(overlay(w, h, label, right))
        writer.add_page(page)
    if reader.metadata:
        writer.add_metadata({k: str(v) for k, v in reader.metadata.items() if v})
    tmp = path + ".stamp.tmp"
    with open(tmp, "wb") as fh:
        writer.write(fh)
    os.replace(tmp, path)
    return {"file": path, "pages": n, "status": "stamped"}

def main():
    mapping = json.load(open(os.path.join(HERE, "mapping.json")))
    args = sys.argv[1:]
    if args == ["--all"]:
        keys = sorted(mapping)
    else:
        keys = sorted(k for k in mapping if any(k.startswith(a) for a in args))
    report = open(os.path.join(HERE, "stamp-report.jsonl"), "a")
    counts = {}
    for rel in keys:
        try:
            r = stamp(os.path.join(ROOT, rel), mapping[rel])
        except Exception as e:  # keep going; failures are reported, never hidden
            r = {"file": rel, "status": "FAILED", "error": f"{type(e).__name__}: {e}"}
        r["file"] = rel
        counts[r["status"]] = counts.get(r["status"], 0) + 1
        report.write(json.dumps(r, ensure_ascii=False) + "\n")
        report.flush()
        if r["status"] not in ("stamped", "already-stamped"):
            print("ATTENTION:", json.dumps(r, ensure_ascii=False))
    report.close()
    print("done:", counts)

if __name__ == "__main__":
    main()
