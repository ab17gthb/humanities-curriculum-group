#!/usr/bin/env python3
"""Lesson 1 slides v3 — rebuilt in Alex's model (his "Capital and Labor" deck):
image-led, one idea per slide, divider slides with short labels, short phrase
fragments instead of full sentences, Gill Sans, big titles, no footers."""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from PIL import Image

NAVY = RGBColor(0x1B, 0x2A, 0x4A)
INK = RGBColor(0x23, 0x27, 0x2E)
GRAY = RGBColor(0x5A, 0x61, 0x6D)
RUST = RGBColor(0xB5, 0x50, 0x2F)
FONT = "Gill Sans"

BASE = "/home/hatch/workspace/curriculum-planner/progressive-era/lesson-01"
A = BASE + "/assets/"

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
SW, SH = 13.333, 7.5

def slide():
    return prs.slides.add_slide(BLANK)

def text(s, x, y, w, h, paras, size=22, color=INK, bold=False, leading=1.15, space_after=14, align=PP_ALIGN.LEFT):
    box = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame; tf.word_wrap = True
    if isinstance(paras, str): paras = [paras]
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align; p.line_spacing = leading; p.space_after = Pt(space_after)
        if isinstance(para, str): para = [(para, {})]
        for txt, st in para:
            r = p.add_run(); r.text = txt
            r.font.size = Pt(st.get("size", size)); r.font.bold = st.get("bold", bold)
            r.font.name = FONT; r.font.color.rgb = st.get("color", color)
    return box

def img_cover(s, path, x, y, w, h):
    """Place image filling the box, center-cropped, no distortion."""
    iw, ih = Image.open(path).size
    box_ar = w / h; img_ar = iw / ih
    pic = s.shapes.add_picture(path, Inches(x), Inches(y), Inches(w), Inches(h))
    if img_ar > box_ar:  # image wider: crop left/right
        crop = (1 - box_ar / img_ar) / 2
        pic.crop_left = crop; pic.crop_right = crop
    else:  # image taller: crop top/bottom
        crop = (1 - img_ar / box_ar) / 2
        pic.crop_top = crop; pic.crop_bottom = crop
    pic.shadow.inherit = False
    return pic

def content(title, frags, img=None, img_w=5.5):
    s = slide()
    tw = 12.0 if not img else 12.0 - img_w - 0.4
    text(s, 0.7, 0.55, tw, 1.0, title, size=40, bold=True, color=NAVY)
    text(s, 0.72, 1.95, tw - 0.2, 5.0, frags, size=23, leading=1.2, space_after=18)
    if img:
        img_cover(s, img, SW - img_w, 0, img_w, SH)
    return s

def divider(label, img, sub=None):
    s = slide()
    img_cover(s, img, 5.3, 0, SW - 5.3, SH)
    text(s, 0.7, 2.9, 4.4, 1.4, label, size=48, bold=True, color=NAVY, leading=1.05)
    if sub:
        text(s, 0.72, 4.35, 4.3, 1.2, sub, size=20, color=GRAY, leading=1.25)
    return s

# S1 TITLE
s = slide()
img_cover(s, A + "mulberry-street.jpg", 5.3, 0, SW - 5.3, SH)
text(s, 0.7, 2.15, 4.5, 2.2, "The Problems Progressives Faced", size=40, bold=True, color=NAVY, leading=1.08)
text(s, 0.72, 4.55, 4.4, 0.6, "U.S. History · The Progressive Era", size=19, color=GRAY)

# S2 AMERICA IN 1900
content("America in 1900", [
    [("76 million", {"bold": True, "color": NAVY}), (" people", {})],
    [("40%", {"bold": True, "color": NAVY}), (" lived in cities", {})],
    [("200,000 miles", {"bold": True, "color": NAVY}), (" of railroad track", {})],
    [("The richest industrial nation on earth", {})],
    [("And a country straining under the speed of its own growth", {"color": GRAY})],
])

# S3 DIVIDER: WORK
divider("Work", A + "breaker-boys.jpg", "Breaker boys, Pennsylvania coal mine")

# S4 THE FACTORY FLOOR
content("The Factory Floor", [
    "10 to 12 hour days, six days a week",
    "Average pay: $400 to $500 a year",
    "Unguarded machines, speed-ups, coal dust",
    "Tens of thousands killed on the job each year",
    "An injured worker had no compensation and no claim",
])

# S5 CHILD LABOR (statement + image)
s = slide()
img_cover(s, A + "hine-spinner.jpg", 8.1, 0, SW - 8.1, SH)
text(s, 0.7, 1.5, 7.1, 1.6, "1.75 million", size=72, bold=True, color=NAVY)
text(s, 0.72, 3.15, 7.0, 1.4, [
    [("children ages 10 to 15 worked in 1900", {"size": 26})],
], space_after=20)
text(s, 0.72, 4.35, 7.0, 2.2, [
    "Mines, mills, canneries, street trades",
    "Most left school by 12, or never went at all",
], size=22, space_after=14)

# S6 DIVIDER: THE CITY
divider("The City", A + "tenement.jpg", "Tenement courtyard, New York")

# S7 TENEMENT LIFE
content("Tenement Life", [
    "Two-thirds of New Yorkers lived in tenements",
    "One toilet for a whole floor",
    "Rooms without windows or fresh air",
    "Typhoid, cholera, tuberculosis",
    "In the worst districts, one infant in five died",
])

# S8 RIIS
content("Jacob Riis", [
    "How the Other Half Lives, 1890",
    "A police reporter with a camera",
    "Flash photography showed the slums to the middle class",
    [("His argument: ", {"bold": True}), ("the environment, not the character of the poor", {})],
], img=A + "jacob-riis.jpg", img_w=4.4)

# S9 DIVIDER: CORRUPTION
divider("Corruption", A + "tweed-nast.jpg", "Thomas Nast cartoon, Harper's Weekly")

# S10 MACHINES AND GRAFT
content("Machines and Graft", [
    "Political machines ran the cities",
    "Jobs, contracts, and favors, traded for votes",
    "Graft: kickbacks on contracts, bribes for franchises",
    "Machines also delivered: jobs, coal, help with the law",
    "Railroads bought the state legislatures that chose U.S. senators",
])

# S11 DIVIDER: CORPORATE POWER
divider("Corporate Power", A + "standard-oil-octopus.jpg", "Standard Oil, Puck magazine, 1904")

# S12 TRUSTS AND WEALTH
content("Trusts and the Wealth Gap", [
    [("318 trusts", {"bold": True, "color": NAVY}), (" by 1904", {})],
    [("Two-fifths", {"bold": True, "color": NAVY}), (" of American manufacturing", {})],
    [("Standard Oil: ", {"bold": True}), ("90% of the nation's refining at its peak", {})],
    [("The richest 1%", {"bold": True, "color": NAVY}), (" owned about half the nation's property", {})],
    [("The bottom half of families owned almost none of it", {})],
])

# S13 WHY GOVERNMENT DID SO LITTLE
content("Why Government Did So Little", [
    [("Laissez-faire: ", {"bold": True}), ("government should keep its hands off business", {})],
    "Courts struck down laws limiting hours and conditions",
    "Government was small, and much of it was for sale",
    "Poverty was widely blamed on the poor themselves",
])

# S14 WHY REFORM CAME
content("Why Reform Came", [
    "A professional middle class, trained and confident",
    "Cheap magazines and printed photographs",
    "Organized women: clubs, temperance, settlement houses",
    "The Social Gospel in the churches",
    "The Populist legacy of the 1890s",
], img=A + "jane-addams.jpg", img_w=4.2)

# S15 ESSENTIAL QUESTION
s = slide()
text(s, 0.9, 2.2, 11.5, 0.6, "ESSENTIAL QUESTION", size=16, bold=True, color=RUST)
text(s, 0.88, 2.9, 11.6, 2.4, "How did Americans respond to the problems created by industrialization, urbanization, and political corruption?", size=34, bold=True, color=NAVY, leading=1.2)
text(s, 0.9, 5.6, 11.5, 0.6, "Next lesson: The Muckrakers", size=20, color=GRAY)

prs.save(BASE + "/lesson-01-slides.pptx")
prs.save(BASE + "/lesson-01-slides-v3.pptx")
print("v3 deck saved, 15 slides")
