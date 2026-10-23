#!/usr/bin/env python3
"""Build the printable teacher-notes document for a lesson slide deck.

Usage: python3 build_notes_doc.py <deck.pptx> <lesson-label> <lesson-title> <headings.json> <out.html>

Reads the speaker notes out of the .pptx and lays them out in slide order
under the house print standard (US Letter, Arial body, Georgia headings,
black text, closing HCG wordmark). headings.json maps slide number (as a
string) to a short heading for that slide's notes.
Convert to PDF afterwards with templates/build_pdf.py.
"""
import html, json, sys
from pptx import Presentation

CSS = """
@page { size: letter; margin: 0.55in 0.75in 0.7in; }
* { box-sizing: border-box; }
.brandmark { margin: 0 0 4pt; line-height: 0; } .brandmark img { width: 1.35in; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 11.5pt; color: #000; line-height: 1.34; margin: 0; }
h1 { font-family: Georgia, serif; font-size: 19pt; margin: 0 0 2pt; line-height: 1.2; }
.sub { font-size: 12pt; margin: 0 0 4pt; }
.rule { border: 0; border-top: 2px solid #b4552d; margin: 8pt 0 10pt; }
.intro { margin: 0 0 6pt; }
h3 { font-family: Georgia, serif; font-size: 12.5pt; margin: 14pt 0 3pt; break-after: avoid; }
.onslide { font-size: 10pt; color: #5a616d; margin: 0 0 3pt; }
p.notes { margin: 0 0 7pt; }
"""


def slide_texts(slide):
    out = []
    for sh in slide.shapes:
        if sh.has_text_frame and sh.text_frame.text.strip():
            out.append(sh.text_frame.text.strip())
    return out


def main():
    deck_path, label, title, headings_path, out_path = sys.argv[1:6]
    headings = json.load(open(headings_path))
    prs = Presentation(deck_path)

    parts = [
        "<!DOCTYPE html>",
        '<html lang="en"><head><meta charset="utf-8">',
        f"<title>Teacher Notes · {html.escape(title)}</title>",
        f"<style>{CSS}</style></head><body>",
        '<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>',
        "<h1>Teacher Notes</h1>",
        f'<p class="sub">{html.escape(label)} · {html.escape(title)}</p>',
        '<hr class="rule">',
        '<p class="intro">These are the speaker notes from the slide deck, in slide order, '
        "set for printing. The deck itself carries the main ideas in a few fragments per slide; "
        "the teaching is here. Print this and keep it beside you while you teach. "
        "Each entry is headed by its slide number and shows what is on that slide, "
        "so you can find your place without flipping back to the screen. "
        "Vocabulary definitions match the student guided notes word for word.</p>",
    ]

    total_words = 0
    for i, slide in enumerate(prs.slides, 1):
        notes = ""
        if slide.has_notes_slide:
            notes = slide.notes_slide.notes_text_frame.text.strip()
        total_words += len(notes.split())
        texts = slide_texts(slide)
        onslide = " · ".join(t.replace("\n", " / ") for t in texts[1:]) if len(texts) > 1 else ""
        heading = headings.get(str(i), f"Slide {i}")
        parts.append(f"<h3>Slide {i} · {html.escape(heading)}</h3>")
        if onslide:
            parts.append(f'<p class="onslide">On the slide: {html.escape(onslide[:220])}</p>')
        parts.append(f'<p class="notes">{html.escape(notes)}</p>')

    parts.append("</body></html>")
    open(out_path, "w").write("\n".join(parts))
    print(f"HTML written: {out_path} ({len(prs.slides)} slides, {total_words} words of notes)")


if __name__ == "__main__":
    main()
