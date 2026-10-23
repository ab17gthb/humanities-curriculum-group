#!/usr/bin/env python3
"""Build the three Course Review covers and preview sheets on the units'
construction: cover HTML (navy, cream wordmark, rust rule, one period
image, contents lines, Knoweth footer) rendered to a letter PDF and a
1632x2112 PNG; preview 1 is the plate overview, previews 2 and 3 compose
real rendered pages from the built PDFs. Outputs land in
site/public/assets/ as <slug>-cover.png and <slug>-preview-N.png, with the
cover HTML and PDF kept in covers/ alongside the units' covers.

Run: python3 gen_covers.py
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))          # covers/
ROOT = os.path.dirname(HERE)                               # curriculum-planner/
CR = os.path.join(ROOT, "course-review")
ASSETS = os.path.join(ROOT, "site", "public", "assets")
BUILD = os.path.join(ROOT, "templates", "build_pdf.py")

COVER_CSS = """
  @page { size: letter; margin: 0; }
  * { margin: 0; box-sizing: border-box; }
  body { width: 8.5in; height: 11in; background: #1f3350; font-family: Arial, sans-serif; color: #f7f2e7; overflow: hidden; }
  .wm { text-align: center; padding-top: 0.5in; }
  .wm img { width: 3.1in; }
  .kick { text-align: center; margin-top: 0.4in; font-size: 12.5pt; letter-spacing: 6px; color: #d98a63; }
  h1 { font-family: Georgia, serif; font-weight: normal; text-align: center; font-size: 37pt; line-height: 1.12; letter-spacing: 2px; margin-top: 0.12in; padding: 0 0.5in; }
  .sub { text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 15.5pt; color: #a8bfd4; margin-top: 0.14in; padding: 0 0.6in; }
  .rule { width: 1.6in; height: 3px; background: #b4552d; margin: 0.28in auto 0; }
  .photo { margin: 0.3in 0.75in 0; border: 1px solid #a8bfd4; height: 3.9in; overflow: hidden; }
  .photo img { width: 100%; height: 100%; object-fit: cover; object-position: center 30%; display: block; }
  .cap { margin: 0.08in 0.75in 0; font-size: 9pt; font-style: italic; color: #a8bfd4; text-align: right; }
  .inside { margin: 0.3in 0.75in 0; text-align: center; font-size: 12.5pt; line-height: 1.6; }
  .inside .n { color: #d98a63; font-weight: bold; }
  .plan { margin: 0.2in 0.75in 0; text-align: center; font-size: 11pt; color: #cfd8e4; line-height: 1.5; }
  .foot { margin-top: 0.32in; text-align: center; font-size: 9.5pt; letter-spacing: 3.5px; color: #8fa5bd; }
"""

COVERS = {
    "course-review": dict(
        title="COURSE REVIEW",
        sub="The Whole Course in Eight Band Days, 1491 to the Present",
        photo="mitchell-map-1755.jpg",
        alt="Mitchell's map of North America, 1755",
        cap="A Map of the British and French Dominions in North America, by John Mitchell, published in London in 1755. Library of Congress, Geography and Map Division.",
        inside='<span class="n">8</span> band days &nbsp;·&nbsp; <span class="n">40</span> documents &nbsp;·&nbsp; study guide &amp; crossword<br><span class="n">840</span> terms reviewed &nbsp;·&nbsp; <span class="n">50</span>-point practice test',
    ),
    "early-review": dict(
        title="EARLY COURSE REVIEW",
        sub="Colonial America Through Reconstruction, 1491–1877",
        photo="first-vote-waud-1867.jpg",
        alt="The first vote, wood engraving after A. R. Waud, 1867",
        cap="The first vote. Wood engraving drawn by A. R. Waud, published in Harper's Weekly, November 16, 1867. Library of Congress.",
        inside='<span class="n">3</span> band days &nbsp;·&nbsp; <span class="n">15</span> documents &nbsp;·&nbsp; study guide &amp; crossword<br><span class="n">336</span> terms reviewed &nbsp;·&nbsp; <span class="n">50</span>-point practice test',
    ),
    "modern-review": dict(
        title="MODERN COURSE REVIEW",
        sub="The Gilded Age to the Present, 1877 to Today",
        photo="mulberry-street.jpg",
        alt="Mulberry Street, New York City, about 1900",
        cap="Mulberry Street, New York City, about 1900. Detroit Photographic Company. Library of Congress.",
        inside='<span class="n">5</span> band days &nbsp;·&nbsp; <span class="n">25</span> documents &nbsp;·&nbsp; study guide &amp; crossword<br><span class="n">504</span> terms reviewed &nbsp;·&nbsp; <span class="n">50</span>-point practice test',
    ),
}

SHEET_CSS = """
  @page { size: 12in 9in; margin: 0; }
  * { margin: 0; box-sizing: border-box; }
  body { width: 12in; height: 9in; background: #f7f2e7; font-family: Arial, sans-serif; color: #1f3350; overflow: hidden; padding: 0.45in 0.55in; }
  h1 { font-family: Georgia, serif; font-weight: normal; font-size: 23pt; margin-bottom: 4pt; }
  .sub { font-size: 11.5pt; color: #5a6a7e; margin-bottom: 14pt; }
  table { border-collapse: collapse; width: 100%; font-size: 11pt; }
  th { text-align: left; font-family: Georgia, serif; border-bottom: 2px solid #b4552d; padding: 3pt 6pt; }
  td { border-bottom: 0.6pt solid #c9bfa5; padding: 3.5pt 6pt; vertical-align: top; }
  td.b { font-weight: bold; white-space: nowrap; width: 2.5in; }
  .pages { display: flex; gap: 0.4in; }
  .pg { flex: 1; }
  .pg img { width: 100%; border: 1px solid #c9bfa5; box-shadow: 0 2px 8px rgba(31,51,80,.18); display: block; }
  .cap { font-size: 10pt; font-style: italic; color: #5a6a7e; margin-top: 6pt; text-align: center; }
"""

BANDS = {
    1: ("Band 1 · Colonies and the Founding", "Colonial America and The Founding"),
    2: ("Band 2 · A Working Republic and Its Discontents", "Early Republic and Expansion and Jackson and Reform"),
    3: ("Band 3 · Slavery, War, and the Unfinished Settlement", "Sectional Crisis and Civil War and Reconstruction"),
    4: ("Band 4 · Industry and Reform", "The Gilded Age and Progressive Era"),
    5: ("Band 5 · Power Abroad, Turmoil at Home", "Imperialism and World War I and The Twenties"),
    6: ("Band 6 · Depression, Recovery, and Total War", "Depression and New Deal and World War II"),
    7: ("Band 7 · Cold War Abroad, Rights at Home", "The Cold War and Civil Rights"),
    8: ("Band 8 · Modern America and the Long Arc", "Modern America and the course's six threads"),
}
VARIANT_BANDS = {"course-review": [1, 2, 3, 4, 5, 6, 7, 8],
                 "early-review": [1, 2, 3], "modern-review": [4, 5, 6, 7, 8]}
VARIANT_NAME = {"course-review": "Course Review", "early-review": "Early Course Review",
                "modern-review": "Modern Course Review"}
VARIANT_KEY = {"course-review": "combined", "early-review": "early", "modern-review": "modern"}
# (pdf, page) pairs for previews 2 and 3 per variant
PREV2 = {"course-review": [("band-1/day-1-review-packet.pdf", 1), ("band-6/day-6-practice-set.pdf", 1)],
         "early-review": [("band-1/day-1-review-packet.pdf", 1), ("band-3/day-3-skills-task.pdf", 1)],
         "modern-review": [("band-4/day-4-review-packet.pdf", 1), ("band-7/day-7-practice-set.pdf", 1)]}
PREV2_CAP = {"course-review": ("Band 1 review packet, page 1", "Band 6 practice set, page 1"),
             "early-review": ("Band 1 review packet, page 1", "Band 3 skills task, page 1"),
             "modern-review": ("Band 4 review packet, page 1", "Band 7 practice set, page 1")}
PREV3 = {"course-review": [("practice-test-combined/combined-practice-test.pdf", 3), ("practice-test-combined/combined-practice-test.pdf", 9)],
         "early-review": [("practice-test-early/early-practice-test.pdf", 3), ("practice-test-early/early-practice-test.pdf", 9)],
         "modern-review": [("practice-test-modern/modern-practice-test.pdf", 3), ("practice-test-modern/modern-practice-test.pdf", 9)]}
PREV3_CAP = ("Practice test: multiple choice, with the review tag under every item",
             "Practice test: the teacher key, every answer tagged to its blueprint entry")


def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.returncode != 0:
        print("FAILED:", cmd, r.stderr[-400:])
        sys.exit(1)


def render_page(pdf_rel, page, out_png, dpi=130):
    src = os.path.join(CR, pdf_rel)
    base = out_png[:-4]
    run(f"pdftoppm -png -r {dpi} -f {page} -l {page} -singlefile {src} {base}")


def sheet_to_png(html_path, out_png):
    pdf = html_path.replace(".html", ".pdf")
    run(f"python3 {BUILD} {html_path}")
    run(f"pdftoppm -png -r 150 -singlefile {pdf} {out_png[:-4]}")


def main():
    tmp = os.path.join(HERE, "review-build")
    os.makedirs(tmp, exist_ok=True)
    for slug, c in COVERS.items():
        cover_html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><style>{COVER_CSS}</style></head><body>
  <div class="wm"><img src="store-wordmark-cream.svg" alt="Humanities Curriculum Group"></div>
  <div class="kick">US HISTORY · COURSE REVIEW</div>
  <h1>{c['title']}</h1>
  <div class="sub">{c['sub']}</div>
  <div class="rule"></div>
  <div class="photo"><img src="{c['photo']}" alt="{c['alt']}"></div>
  <div class="cap">{c['cap']}</div>
  <div class="inside">{c['inside']}</div>
  <div class="plan">Every document includes the teacher key. Every practice item is tagged to the course blueprint,<br>so the Humanities Curriculum Group planner can check your review against the test.</div>
  <div class="foot">A KNOWETH PRODUCT</div>
</body></html>"""
        hp = os.path.join(HERE, f"cover-{slug}.html")
        open(hp, "w").write(cover_html)
        run(f"python3 {BUILD} {hp}")
        run(f"pdftoppm -png -r 192 -singlefile {hp.replace('.html', '.pdf')} {os.path.join(ASSETS, slug + '-cover')}")
        print("cover:", slug)

        # Preview 1: the plate
        rows = ""
        for b in VARIANT_BANDS[slug]:
            t, units = BANDS[b]
            rows += (f"<tr><td class='b'>{t}</td><td>Review packet · term sprint · practice set · skills task · teacher guide</td>"
                     f"<td>{units}</td></tr>")
        rows += ("<tr><td class='b'>Flex day</td><td>Study guide with full key · crossword</td><td>The variant's whole span</td></tr>"
                 "<tr><td class='b'>Practice test</td><td>50 points: matching, multiple choice, sources, with a tagged key</td><td>Every unit in the blueprint, at least twice</td></tr>")
        p1 = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{SHEET_CSS}</style></head><body>
<h1>{VARIANT_NAME[slug]}: the full plate</h1>
<p class="sub">Every band day runs the same four student pieces on one packet. Teacher guides carry the front matter and every key.</p>
<table><tr><th>Day</th><th>Documents</th><th>Reviews</th></tr>{rows}</table>
</body></html>"""
        p1p = os.path.join(tmp, f"{slug}-preview-1.html")
        open(p1p, "w").write(p1)
        sheet_to_png(p1p, os.path.join(ASSETS, f"{slug}-preview-1.png"))
        # Previews 2 and 3: real pages
        for num, spec, caps in ((2, PREV2[slug], PREV2_CAP[slug]), (3, PREV3[slug], PREV3_CAP)):
            imgs = []
            for k, (rel, page) in enumerate(spec):
                ip = os.path.join(tmp, f"{slug}-p{num}-{k}.png")
                render_page(rel, page, ip)
                imgs.append(ip)
            body = "".join(
                f'<div class="pg"><img src="{os.path.basename(im)}"><p class="cap">{cap}</p></div>'
                for im, cap in zip(imgs, caps))
            ttl = "Inside the band days" if num == 2 else "The practice test and its key"
            ph = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{SHEET_CSS}</style></head><body>
<h1>{VARIANT_NAME[slug]}: {ttl}</h1>
<p class="sub">Real pages from the built documents, unretouched.</p>
<div class="pages">{body}</div>
</body></html>"""
            php = os.path.join(tmp, f"{slug}-preview-{num}.html")
            open(php, "w").write(ph)
            sheet_to_png(php, os.path.join(ASSETS, f"{slug}-preview-{num}.png"))
        print("previews:", slug)


if __name__ == "__main__":
    main()
