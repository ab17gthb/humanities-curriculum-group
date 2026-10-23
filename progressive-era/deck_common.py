#!/usr/bin/env python3
"""Shared deck-building system for the Progressive Era slide decks.
Extracted from the approved Lesson 1 build (2026-10-21). Importing scripts
set IMG (image dir) and OUT (output pptx path), build slides with the
helpers, then call save(). Design: image-led slides, fragments only on
screen, comprehensive speaker notes, full lesson + vocabulary coverage.
Fonts: Georgia titles, Lato body. 16:9, cream/navy palette."""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
import os

IMG = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img')
NAVY = RGBColor(0x1F, 0x33, 0x50)
CREAM = RGBColor(0xF7, 0xF2, 0xE7)
RUST = RGBColor(0xB4, 0x55, 0x2D)
RUST_LT = RGBColor(0xD9, 0x8A, 0x63)
POWDER = RGBColor(0xA8, 0xBF, 0xD4)
INK = RGBColor(0x23, 0x32, 0x46)
MUTED = RGBColor(0x4C, 0x5A, 0x6C)
LINE = RGBColor(0xC9, 0xBF, 0xA5)

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
W, H = 13.333, 7.5

def slide(bg=CREAM):
    s = prs.slides.add_slide(BLANK)
    r = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    r.fill.solid(); r.fill.fore_color.rgb = bg; r.line.fill.background()
    r.shadow.inherit = False
    return s

def rect(s, x, y, w, h, color):
    r = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    r.fill.solid(); r.fill.fore_color.rgb = color; r.line.fill.background()
    r.shadow.inherit = False
    return r

def text(s, x, y, w, h, runs, size=24, color=INK, font='Lato', bold=False,
         align=PP_ALIGN.LEFT, leading=1.18, space_after=10, anchor=MSO_ANCHOR.TOP):
    """runs: str, or list of paragraphs; each paragraph is str or list of (txt, dict) runs."""
    box = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame; tf.word_wrap = True
    tf.vertical_anchor = anchor
    if isinstance(runs, str): runs = [runs]
    for i, para in enumerate(runs):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align; p.line_spacing = leading; p.space_after = Pt(space_after)
        if isinstance(para, str): para = [(para, {})]
        for txt, ov in para:
            r = p.add_run(); r.text = txt
            r.font.size = Pt(ov.get('size', size)); r.font.bold = ov.get('bold', bold)
            r.font.name = ov.get('font', font); r.font.color.rgb = ov.get('color', color)
            if ov.get('italic'): r.font.italic = True
    return box

def notes(s, txt):
    s.notes_slide.notes_text_frame.text = txt

def kicker(s, txt, color=RUST_LT, x=0.9, y=0.62):
    text(s, x, y, 11.5, 0.5, txt.upper(), size=15, color=color, font='Arial', bold=True)

def rule(s, x, y, w=1.6, color=RUST):
    rect(s, x, y, w, 0.045, color)

def frags(s, items, x=0.9, y=2.2, w=6.6, size=27, color=INK, gap=16, leading=1.15):
    paras = []
    for it in items:
        paras.append([('▪  ', {'color': RUST, 'size': size - 4}), (it, {})])
    text(s, x, y, w, 4.6, paras, size=size, color=color, space_after=gap, leading=leading)

def photo_right(s, img, x=8.1, w=5.23):
    s.shapes.add_picture(os.path.join(IMG, img), Inches(x), 0, Inches(w), Inches(H))

def divider_photo(img, kick, title, lines, note, img_x=8.1, img_w=5.23, title_size=44):
    s = slide(NAVY)
    photo_right(s, img, img_x, img_w)
    kicker(s, kick)
    text(s, 0.9, 1.7, 6.9, 2.2, title, size=title_size, color=CREAM, font='Georgia', leading=1.08)
    rule(s, 0.92, 3.62)
    if lines:
        text(s, 0.9, 3.95, 6.8, 2.6, lines, size=22, color=POWDER, space_after=8, leading=1.25)
    notes(s, note)
    return s

def content_photo(img, title, items, note, kick=None):
    s = slide(CREAM)
    photo_right(s, img)
    if kick: kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95 if kick else 0.8, 6.9, 1.2, title, size=31, color=NAVY, font='Georgia', leading=1.05)
    frags(s, items, y=2.15 if kick else 2.0)
    notes(s, note)
    return s

def content_text(title, items, note, kick=None, size=27):
    s = slide(CREAM)
    if kick: kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95 if kick else 0.8, 11.5, 1.2, title, size=31, color=NAVY, font='Georgia', leading=1.05)
    frags(s, items, y=2.15 if kick else 2.0, w=11.3, size=size)
    notes(s, note)
    return s

def stat(number, label, sub, note, kick=None):
    s = slide(NAVY)
    if kick: kicker(s, kick)
    text(s, 0.9, 1.55, 11.53, 2.6, number, size=120, color=CREAM, font='Georgia',
         align=PP_ALIGN.CENTER, space_after=0)
    text(s, 0.9, 4.35, 11.53, 0.9, label, size=30, color=CREAM, align=PP_ALIGN.CENTER, space_after=0)
    if sub:
        text(s, 1.9, 5.35, 9.53, 1.2, sub, size=20, color=POWDER, align=PP_ALIGN.CENTER, leading=1.3)
    notes(s, note)
    return s

def divider_text(kick, title, sub, note):
    s = slide(NAVY)
    kicker(s, kick)
    text(s, 0.9, 2.2, 11.5, 2.4, title, size=52, color=CREAM, font='Georgia', leading=1.1)
    rule(s, 0.92, 4.35)
    if sub:
        text(s, 0.9, 4.7, 10.5, 1.6, sub, size=22, color=POWDER, leading=1.3)
    notes(s, note)
    return s



def save(path):
    prs.save(path)
    print("saved", path, "slides:", len(prs.slides.__iter__.__self__._sldIdLst))
