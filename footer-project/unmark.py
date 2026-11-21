#!/usr/bin/env python3
"""Remove the top wordmark from page 1 of every catalog PDF that shows it.

Alex's call (2026-10-28): documents carry the footer only; the wordmark at
the top comes off. Method: pixel-gate page 1 — the wordmark occupies a fixed
zone (x 54-151pt, 39.6-62.4pt from the top, per the uniform .brandmark CSS).
If dark pixels appear in that zone, paint a white rectangle over exactly the
brandmark box (x 50-156pt, 34-65pt from top). Content and pagination are
untouched (the rect stays inside the header gap, above the nameline).
Post-checks per treated file: wordmark zone empty afterwards, and the
nameline band's dark-pixel count unchanged (no collateral coverage).
Writes unmark-report.jsonl; prints a summary.
"""
import io, json, os, subprocess, sys, tempfile
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.expanduser("~/workspace/curriculum-planner")
DPI = 150
SCALE = DPI / 72.0
# gate zone (points): x 51-154.7, from-top 37.4-64.4 (the wordmark's box)
GATE = (int(51 * SCALE), int(37.4 * SCALE), int(154.7 * SCALE), int(64.4 * SCALE))
# wide zone: same rows, x 160-570. The wordmark never reaches it; teacher
# docs' big titles do. Any ink here means this is not a brandmark header.
WIDE = (int(160 * SCALE), int(37.4 * SCALE), int(570 * SCALE), int(64.4 * SCALE))
# nameline band (points): x 40-570, from-top 72-98 -> collateral check
BAND = (int(40 * SCALE), int(72 * SCALE), int(570 * SCALE), int(98 * SCALE))
# white rect (points, PDF bottom-origin): x 50-156, y 727-758
RECT = (50.0, 727.0, 156.0, 758.0)

def render_p1(pdf):
    with tempfile.TemporaryDirectory() as td:
        out = os.path.join(td, "p")
        subprocess.run(["pdftoppm", "-png", "-r", str(DPI), "-f", "1", "-l", "1",
                        pdf, out], check=True, capture_output=True)
        png = [f for f in os.listdir(td) if f.endswith(".png")][0]
        return Image.open(os.path.join(td, png)).convert("L").copy()

def dark_in(im, box):
    x0, y0, x1, y1 = box
    px = im.load()
    return sum(1 for y in range(y0, min(y1, im.height))
               for x in range(x0, min(x1, im.width)) if px[x, y] < 90)

def whiteout(path):
    reader = PdfReader(path)
    page = reader.pages[0]
    w, h = float(page.mediabox.width), float(page.mediabox.height)
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(w, h))
    c.setFillColorRGB(1, 1, 1)
    x0, y0, x1, y1 = RECT
    c.rect(x0, y0, x1 - x0, y1 - y0, stroke=0, fill=1)
    c.save()
    buf.seek(0)
    page.merge_page(PdfReader(buf).pages[0])
    writer = PdfWriter()
    writer.add_page(page)
    for p in reader.pages[1:]:
        writer.add_page(p)
    if reader.metadata:
        writer.add_metadata({k: str(v) for k, v in reader.metadata.items() if v})
    tmp = path + ".unmark.tmp"
    with open(tmp, "wb") as fh:
        writer.write(fh)
    os.replace(tmp, path)

def main():
    mapping = json.load(open(os.path.join(HERE, "mapping.json")))
    report = open(os.path.join(HERE, "unmark-report.jsonl"), "a")
    counts = {}
    for rel in sorted(mapping):
        path = os.path.join(ROOT, rel)
        rec = {"file": rel}
        try:
            im = render_p1(path)
            gate = dark_in(im, GATE)
            wide = dark_in(im, WIDE)
            rec["wide_px"] = wide
            if gate == 0:
                rec["status"] = "no-wordmark"
            elif wide > 0:
                rec["status"] = "skipped-wide-header"
            elif abs(float(PdfReader(path).pages[0].mediabox.height) - 792.0) > 1:
                rec["status"] = "CHECK-ME"
                rec["error"] = "non-letter page height; rect not applied"
            else:
                band_before = dark_in(im, BAND)
                whiteout(path)
                im2 = render_p1(path)
                gate_after = dark_in(im2, GATE)
                band_after = dark_in(im2, BAND)
                rec.update(gate_before=gate, gate_after=gate_after,
                           band_before=band_before, band_after=band_after)
                rec["status"] = ("whited" if gate_after == 0 and band_after == band_before
                                 else "CHECK-ME")
        except Exception as e:
            rec["status"] = "FAILED"
            rec["error"] = f"{type(e).__name__}: {e}"
        counts[rec["status"]] = counts.get(rec["status"], 0) + 1
        report.write(json.dumps(rec) + "\n")
        report.flush()
        if rec["status"] not in ("whited", "no-wordmark", "skipped-wide-header"):
            print("ATTENTION:", json.dumps(rec))
    report.close()
    print("done:", counts)

if __name__ == "__main__":
    main()
