#!/usr/bin/env python3
"""Lesson 1 template package builder — Progressive Era unit.
Design system: navy #1B2A4A, rust #B5502F, paper #FAF7F2, ink #23272E.
Titles Georgia, body Arial. Same cover block on every document."""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
import copy

NAVY = RGBColor(0x1B, 0x2A, 0x4A)
RUST = RGBColor(0xB5, 0x50, 0x2F)
PAPER = RGBColor(0xFA, 0xF7, 0xF2)
INK = RGBColor(0x23, 0x27, 0x2E)
GRAY = RGBColor(0x5A, 0x61, 0x6D)
LIGHT = RGBColor(0xE9, 0xE4, 0xDA)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
TITLE_FONT = "Georgia"
BODY_FONT = "Arial"

OUT = "/home/hatch/workspace/curriculum-planner/progressive-era/lesson-01"
IMG = OUT + "/assets/breaker-boys.jpg"

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
SW, SH = 13.333, 7.5

def slide():
    return prs.slides.add_slide(BLANK)

def rect(s, x, y, w, h, color):
    shp = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    shp.fill.solid(); shp.fill.fore_color.rgb = color
    shp.line.fill.background()
    shp.shadow.inherit = False
    return shp

def rect_border(s, x, y, w, h, fill, line_color, line_w=1.0):
    shp = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    shp.fill.solid(); shp.fill.fore_color.rgb = fill
    shp.line.color.rgb = line_color; shp.line.width = Pt(line_w)
    shp.shadow.inherit = False
    return shp

def text(s, x, y, w, h, runs, size=20, color=INK, bold=False, font=BODY_FONT,
         align=PP_ALIGN.LEFT, leading=1.12, space_after=8, anchor=MSO_ANCHOR.TOP):
    """runs: str, or list of paragraphs; each paragraph is str or list of (txt, dict) runs."""
    box = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    if isinstance(runs, str):
        runs = [runs]
    for i, para in enumerate(runs):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = leading
        p.space_after = Pt(space_after)
        if isinstance(para, str):
            para = [(para, {})]
        for txt, st in para:
            r = p.add_run(); r.text = txt
            r.font.size = Pt(st.get("size", size))
            r.font.bold = st.get("bold", bold)
            r.font.italic = st.get("italic", False)
            r.font.name = st.get("font", font)
            r.font.color.rgb = st.get("color", color)
    return box

def header(s, kicker, title, num):
    text(s, 0.62, 0.3, 11.5, 0.35, kicker.upper(), size=13, color=RUST, bold=True)
    text(s, 0.6, 0.62, 12.1, 0.75, title, size=32, color=NAVY, bold=True, font=TITLE_FONT)
    rect(s, 0.62, 1.44, 12.1, 0.03, RUST)
    text(s, 0.62, 7.06, 8.0, 0.3, "The Progressive Era · Lesson 1 · The Problems Progressives Faced", size=11, color=GRAY)
    text(s, 12.35, 7.06, 0.4, 0.3, str(num), size=11, color=GRAY, align=PP_ALIGN.RIGHT)

def bullets(s, items, x=0.65, y=1.75, w=12.0, size=20, gap=10, leading=1.15):
    paras = []
    for it in items:
        if isinstance(it, str):
            it = [(it, {})]
        paras.append([("▪  ", {"color": RUST, "bold": True})] + it)
    text(s, x, y, w, 5.1, paras, size=size, space_after=gap, leading=leading)

def B(t):  return [(t, {"bold": True})]
def T(t):  return [(t, {})]
def M(b, rest): return [(b, {"bold": True}), (rest, {})]

# ---------- S1 TITLE ----------
s = slide()
rect(s, 0, 4.62, SW, 0.045, RUST)
text(s, 0.9, 1.45, 11.5, 0.5, "U.S. HISTORY  ·  UNIT: THE PROGRESSIVE ERA", size=16, color=RUST, bold=True)
text(s, 0.88, 2.0, 11.8, 1.75, "The Problems Progressives Faced", size=48, color=NAVY, bold=True, font=TITLE_FONT, leading=1.05)
text(s, 0.9, 3.95, 11.5, 0.6, "Lesson 1 · Why a reform movement, and why then?", size=22, color=GRAY)
text(s, 0.9, 5.05, 11.6, 1.4, [
    [("Essential question:  ", {"bold": True, "color": RUST})],
    [("How did Americans respond to the problems created by industrialization, urbanization, and political corruption?", {"color": INK, "italic": True, "font": TITLE_FONT, "size": 21})],
], size=19, leading=1.25, space_after=4)
text(s, 0.9, 6.85, 11.5, 0.35, "Name ______________________________________     Date ______________     Period _______", size=13, color=GRAY)

# ---------- S2 OBJECTIVES ----------
s = slide()
header(s, "Lesson 1", "Today's Lesson", 2)
text(s, 0.65, 1.7, 7.6, 0.5, "By the end of this lesson you will be able to:", size=21, bold=True, color=NAVY, font=TITLE_FONT)
bullets(s, [
    "Describe the conditions facing American workers and city residents around 1900.",
    "Explain why government at every level did so little about those conditions.",
    "Identify the forces that made a national reform movement possible.",
], x=0.65, y=2.3, w=7.4, size=20, gap=14)
rect_border(s, 8.5, 1.75, 4.15, 4.6, WHITE, RGBColor(0xD8, 0xD2, 0xC4))
rect(s, 8.5, 1.75, 4.15, 0.06, RUST)
text(s, 8.8, 1.95, 3.6, 0.45, "KEY TERMS", size=14, bold=True, color=RUST)
terms = ["laissez-faire", "tenement", "political machine", "graft", "trust", "Social Gospel", "settlement house"]
text(s, 8.8, 2.45, 3.6, 3.7, [[(t, {})] for t in terms], size=19, space_after=9)

# ---------- S3 WARM-UP PHOTO ----------
s = slide()
header(s, "Warm-Up", "Look Closely", 3)
s.shapes.add_picture(IMG, Inches(7.05), Inches(1.7), width=Inches(5.6))
text(s, 7.05, 6.18, 5.6, 0.75, "Breaker boys in a Pennsylvania coal mine. National Child Labor Committee collection, Library of Congress.", size=11.5, color=GRAY, leading=1.15)
text(s, 0.65, 1.75, 6.0, 4.9, [
    [("These boys sorted coal in a Pennsylvania mine, picking slate out of the coal with their fingers, ten hours a day.", {})],
    [("Write for three minutes:", {"bold": True, "color": NAVY})],
    [("1.  What do you see in this photograph? List details.", {})],
    [("2.  What does it tell you about American life in 1900?", {})],
    [("3.  What can it not tell you? What would you need to know more?", {})],
], size=20, space_after=13, leading=1.2)

# ---------- S4 BY THE NUMBERS ----------
s = slide()
header(s, "Setting the Scene", "America in 1900, by the Numbers", 4)
stats = [
    ("76 million", "people lived in the United States"),
    ("40%", "lived in cities, up from 20% in 1860"),
    ("200,000", "miles of railroad track crossed the country"),
    ("1.75 million", "children ages 10 to 15 held jobs, counted by the 1900 census"),
]
for i, (big, small) in enumerate(stats):
    x = 0.65 + i * 3.13
    rect_border(s, x, 2.0, 2.9, 3.3, WHITE, RGBColor(0xD8, 0xD2, 0xC4))
    rect(s, x, 2.0, 2.9, 0.06, RUST)
    text(s, x + 0.25, 2.35, 2.55, 1.0, big, size=27, bold=True, color=NAVY, font=TITLE_FONT)
    text(s, x + 0.25, 3.35, 2.4, 1.8, small, size=16.5, color=INK, leading=1.2)
text(s, 0.65, 5.7, 12.0, 0.8, "A bigger, richer, more industrial country than ever before. The problems below grew just as fast.", size=19, color=INK)

# ---------- S5 FOUR PROBLEMS ----------
s = slide()
header(s, "The Problems", "Four Problems, One Movement", 5)
probs = [
    ("1 · WORK", "Dangerous, exhausting, and insecure jobs"),
    ("2 · THE CITY", "Overcrowded, unsanitary housing"),
    ("3 · CORRUPTION", "Government run for private profit"),
    ("4 · CORPORATE POWER", "Trusts and a widening wealth gap"),
]
for i, (t1, t2) in enumerate(probs):
    x = 0.65 + (i % 2) * 6.15
    y = 1.85 + (i // 2) * 2.15
    rect_border(s, x, y, 5.9, 1.85, WHITE, RGBColor(0xD8, 0xD2, 0xC4))
    rect(s, x, y, 0.07, 1.85, RUST)
    text(s, x + 0.35, y + 0.22, 5.3, 0.5, t1, size=17, bold=True, color=RUST)
    text(s, x + 0.35, y + 0.72, 5.3, 1.0, t2, size=22, bold=True, color=NAVY, font=TITLE_FONT, leading=1.1)
text(s, 0.65, 6.35, 12.0, 0.6, "Progressivism was the response to all four. Today we take the problems one at a time.", size=19)

# ---------- S6 PROBLEM 1 WORK ----------
s = slide()
header(s, "Problem 1 · Work", "The Factory Floor", 6)
bullets(s, [
    M("Hours. ", "Ten to twelve hours a day, six days a week, was a normal schedule in factories, mills, and mines."),
    M("Pay. ", "The average factory worker earned roughly $400 to $500 a year, barely enough to support a family."),
    M("Danger. ", "Unguarded machines, coal dust, and speed-up systems. Tens of thousands of workers were killed on the job each year, and far more were injured."),
    M("No safety net. ", "A worker hurt on the job had no workers' compensation and usually no legal claim. The family absorbed the loss."),
])

# ---------- S7 CHILD LABOR ----------
s = slide()
header(s, "Problem 1 · Work", "Child Labor", 7)
bullets(s, [
    M("The count. ", "The 1900 census counted about 1.75 million working children between the ages of 10 and 15, roughly one child in five."),
    M("The jobs. ", "Mines, textile mills, canneries, glass factories, and street trades. Children were cheap, could fit into small spaces, and rarely organized."),
    M("The cost. ", "Most working children left school by age 12, or never attended at all. Work injuries and stunted growth followed many of them for life."),
    M("The evidence. ", "Reformers sent photographers such as Lewis Hine into mines and mills. His pictures made child labor impossible to unsee."),
])

# ---------- S8 PROBLEM 2 CITY ----------
s = slide()
header(s, "Problem 2 · The City", "Tenement Life", 8)
bullets(s, [
    M("Growth. ", "Cities grew faster than housing, water systems, or sewers could be built. New York City alone held 3.4 million people by 1900."),
    M("Tenements. ", "About two-thirds of New Yorkers lived in tenements, crowded multi-family buildings where a whole floor might share one toilet and many rooms had no windows."),
    M("Disease. ", "Contaminated water and crowding spread typhoid, cholera, and tuberculosis. In the worst districts, as many as one infant in five died before a first birthday."),
    M("Services lagged. ", "Garbage collection, street cleaning, and clean water arrived slowly, and last in the poorest neighborhoods."),
])

# ---------- S9 RIIS ----------
s = slide()
header(s, "Seeing the Problem", "Jacob Riis and the Camera", 9)
bullets(s, [
    M("The book. ", "How the Other Half Lives (1890), by police reporter Jacob Riis, took middle-class readers inside New York's tenements."),
    M("The technology. ", "Flash photography and halftone printing meant pictures of slum life could now appear in books and magazines, not just be described."),
    M("The argument. ", "Riis blamed the environment, not the character of the poor. Change the conditions, he argued, and you change the people."),
    M("The legacy. ", "That idea sits underneath nearly all Progressive reform. Remember it when we meet the muckrakers tomorrow."),
])

# ---------- S10 PROBLEM 3 CORRUPTION ----------
s = slide()
header(s, "Problem 3 · Corruption", "Government for Sale", 10)
bullets(s, [
    M("Machines. ", "Many cities were run by political machines, organizations that controlled votes and city jobs through favors and patronage."),
    M("Graft. ", "The business model was kickbacks on city contracts and bribes from companies that wanted franchises, licenses, or no inspections."),
    M("Why voters kept them. ", "Machines delivered real help to immigrants and the poor: a job, coal in winter, help with a judge. Loyalty was earned, not just bought."),
    M("States too. ", "Railroads and mining companies routinely bought state legislatures, which also chose U.S. senators. Corruption reached Washington this way."),
])

# ---------- S11 PROBLEM 4 CORPORATE POWER ----------
s = slide()
header(s, "Problem 4 · Corporate Power", "Trusts and the Wealth Gap", 11)
bullets(s, [
    M("Trusts. ", "By 1904, roughly 318 trusts controlled about two-fifths of American manufacturing. Standard Oil had refined about 90 percent of the nation's oil at its peak."),
    M("Wealth. ", "Contemporary estimates held that the richest 1 percent of Americans owned about half the nation's property, while the bottom half of families owned almost none of it."),
    M("The squeeze. ", "Farmers depended on railroads they could not bargain with. Small businesses faced competitors who could sell below cost until they folded."),
    M("The question. ", "Could a democracy survive this much concentrated private power? Progressives answered no, and that government had to act."),
])

# ---------- S12 WHY GOVERNMENT DID SO LITTLE ----------
s = slide()
header(s, "The Response Gap", "Why Government Did So Little", 12)
bullets(s, [
    M("Laissez-faire. ", "The dominant idea of the age held that government should keep its hands off business. Interference was seen as both wrong and harmful."),
    M("The courts. ", "Judges backed the idea up, striking down state laws that limited hours or set conditions in workplaces."),
    M("Small and bought. ", "Government was tiny next to the problems, and Problem 3 meant much of it was for sale anyway."),
    M("Blaming the poor. ", "Many Americans treated poverty as a character failure: laziness, drink, bad choices. Riis's environmental argument was a direct challenge to this view."),
])

# ---------- S13 WHY REFORM CAME ----------
s = slide()
header(s, "The Turn", "Why Reform Came When It Did", 13)
roots = [
    ("The middle class", "A growing class of educated professionals had the income, training, and confidence to believe problems could be managed."),
    ("The press", "Cheap magazines and printed photographs carried the evidence into millions of homes."),
    ("Organized women", "Clubs, temperance groups, and settlement houses such as Jane Addams's Hull House trained a generation of reformers."),
    ("The Social Gospel", "Churches taught that faith required fixing social conditions, not only saving individual souls."),
    ("The Populist legacy", "Farmers of the 1890s had already argued that concentrated power was the problem and that government could act."),
]
y = 1.72
for t1, t2 in roots:
    text(s, 0.65, y, 3.1, 0.9, t1, size=19, bold=True, color=NAVY, font=TITLE_FONT, leading=1.05)
    text(s, 3.95, y + 0.02, 8.75, 0.95, t2, size=17.5, leading=1.12)
    y += 1.04

# ---------- S14 EXIT TICKET ----------
s = slide()
header(s, "Check for Understanding", "Exit Ticket", 14)
bullets(s, [
    M("1. ", "Name the four problems from today's lesson, and give one specific fact for each."),
    M("2. ", "Why did government do so little about these problems before 1900? Give two reasons."),
    M("3. ", "Of the five roots of reform, which do you think mattered most? Defend your choice in two or three sentences."),
], size=21, gap=16)
text(s, 0.65, 5.6, 12.0, 0.7, "Write your answers on your guided notes sheet.", size=17, color=GRAY)

# ---------- S15 NEXT ----------
s = slide()
rect(s, 0, 3.3, SW, 0.045, RUST)
text(s, 0.9, 1.7, 11.5, 0.5, "NEXT LESSON", size=15, bold=True, color=RUST)
text(s, 0.88, 2.2, 11.8, 1.1, "The Muckrakers", size=46, bold=True, color=NAVY, font=TITLE_FONT)
text(s, 0.9, 3.7, 11.4, 1.6, "The writers and photographers who turned these problems into a national scandal, starting with a novel about a Chicago meatpacking plant that changed what America ate.", size=21, color=GRAY, leading=1.3)

prs.save(OUT + "/lesson-01-slides.pptx")
print("slides saved:", len(prs.slides.__iter__.__self__._sldIdLst), "slides")
