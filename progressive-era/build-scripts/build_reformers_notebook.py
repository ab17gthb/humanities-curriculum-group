#!/usr/bin/env python3
"""Reformer's Notebook activity: Gemini's text (Alex's Google Doc, Oct 20, 2026)
with the real public-domain images set in, in Alex's print format."""
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT

BLACK = RGBColor(0, 0, 0)
BASE = "/home/hatch/workspace/curriculum-planner/progressive-era/lesson-01"
A = BASE + "/assets/"

doc = Document()
for sec in doc.sections:
    sec.top_margin = Inches(0.6); sec.bottom_margin = Inches(0.6)
    sec.left_margin = Inches(0.75); sec.right_margin = Inches(0.75)
st = doc.styles["Normal"]
st.font.name = "Arial"; st.font.size = Pt(11.5); st.font.color.rgb = BLACK
st.paragraph_format.space_after = Pt(6); st.paragraph_format.line_spacing = 1.12

def p(text="", size=11.5, bold=False, italic=False, before=0, after=6, font="Arial", align=None):
    par = doc.add_paragraph()
    par.paragraph_format.space_before = Pt(before); par.paragraph_format.space_after = Pt(after)
    if align: par.alignment = align
    if text:
        r = par.add_run(text); r.font.size = Pt(size); r.bold = bold; r.italic = italic
        r.font.color.rgb = BLACK; r.font.name = font
    return par

def h(text, size=14, before=12):
    return p(text, size=size, bold=True, before=before, after=4, font="Georgia")

def blank(n=2):
    for _ in range(n):
        par = doc.add_paragraph()
        r = par.add_run(" "); r.font.size = Pt(14)
        par.paragraph_format.space_after = Pt(9)

def image(path, width, caption):
    par = doc.add_paragraph(); par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    par.paragraph_format.space_before = Pt(4); par.paragraph_format.space_after = Pt(2)
    par.add_run().add_picture(path, width=Inches(width))
    p(caption, size=9.5, italic=True, after=8, align=WD_ALIGN_PARAGRAPH.CENTER)

# ---- Header (Alex's standard) ----
par = doc.add_paragraph()
par.paragraph_format.space_after = Pt(2)
par.paragraph_format.tab_stops.add_tab_stop(Inches(3.1), WD_TAB_ALIGNMENT.LEFT)
par.paragraph_format.tab_stops.add_tab_stop(Inches(5.3), WD_TAB_ALIGNMENT.LEFT)
r = par.add_run("Name ____________________\tDate ____________\tPeriod __________")
r.font.size = Pt(11.5); r.font.color.rgb = BLACK; r.font.name = "Arial"

p("Reformer's Notebook: The Problems Progressives Faced", size=19, bold=True, before=10, after=2, font="Georgia")
direc = doc.add_paragraph(); direc.paragraph_format.space_after = Pt(6)
r = direc.add_run("Directions: "); r.bold = True; r.font.size = Pt(11.5)
r = direc.add_run("Read the sources at all four stations to understand the crises that sparked the Progressive movement, then answer the questions for each stop. After reviewing all four problems, complete the final verdict section to rank their urgency.")
r.font.size = Pt(11.5)

h("Part 1: Four Stops", size=15, before=8)

# ---- Station 1 ----
h("Station 1: Dangerous Industrial Work and Child Labor", size=13)
p('Source: Description of a photograph by Lewis Hine, "Breaker Boys inside the Coal Breaker," 1911.', after=2)
image(A + "breaker-boys-interior.jpg", 3.6, "The photograph itself: breaker boys at work inside the Ewen Breaker, South Pittston, Pennsylvania, 1911. Lewis Hine, Library of Congress.")
p("The photograph shows a row of young boys, some appearing as young as nine or ten years old, sitting on wooden planks over coal chutes. Their faces, clothes, and arms are completely covered in thick black coal dust. They are hunched forward in a dark, cramped room, picking sharp pieces of slate out of the rough coal with their bare, calloused hands.")
p("What does this source show about the nature of industrial work during this period?", after=2)
blank(2)
p("Who was primarily hurt by these conditions, and what were the physical or developmental costs to them?", after=2)
blank(2)

# ---- Station 2 ----
h("Station 2: Tenement Life in Crowded Cities", size=13)
p("Source: Summary of Jacob Riis, How the Other Half Lives, 1890.", after=2)
image(A + "riis-lodgers.jpg", 3.6, "Lodgers in a crowded Bayard Street tenement. Jacob Riis, from How the Other Half Lives.")
p("Riis describes a tenement hallway so dark that a visitor might stumble over children playing in the shadows. He notes that the air inside is foul and the buildings are packed tightly with immigrant families. In one small, unventilated room, he observes multiple people sleeping on the bare floor, breathing stale air filled with the overwhelming smell of summer heat and garbage from the alley below.")
p("What does this description reveal about the housing conditions for the urban poor?", after=2)
blank(2)
p("Who suffered the most in these environments, and how did it affect their daily health and safety?", after=2)
blank(2)

# ---- Station 3 ----
h("Station 3: Corrupt Political Machines", size=13)
p("Source: Summary of George Washington Plunkitt's interviews in William L. Riordon's Plunkitt of Tammany Hall, 1905.", after=2)
image(A + "tweed-nast.jpg", 3.6, "Thomas Nast cartoon on corruption, Harper's Weekly, 1872.")
p('Plunkitt proudly explains his system of "honest graft." When he learns the city plans to build a new public park, he secretly buys the targeted land in advance. He then sells it back to the city at a massive profit. He claims he is just seeing opportunities and taking them, arguing this is exactly how political leaders should reward themselves and their loyal voters.')
p("What does this source demonstrate about how political machines operated in major cities?", after=2)
blank(2)
p("Who was ultimately cheated by this system, and how did it damage the democratic process?", after=2)
blank(2)

# ---- Station 4 ----
h("Station 4: The Power of Trusts", size=13)
p("Source: Summary of Ida Tarbell, The History of the Standard Oil Company, 1904.", after=2)
image(A + "standard-oil-octopus.jpg", 3.8, "The Standard Oil octopus. Puck magazine, 1904.")
p("Tarbell details how John D. Rockefeller's company used its massive wealth and size to force railroads into giving them secret, illegal discounts on shipping oil. By cutting his transportation costs, Rockefeller could drop his oil prices so low that small, independent oil refiners were driven into bankruptcy. Once the local competitors were destroyed, Standard Oil controlled the entire market and raised prices again.")
p("What does this summary reveal about the business tactics used by large trusts to gain power?", after=2)
blank(2)
p("Who was financially hurt by these monopolies, and how did it affect the broader economy?", after=2)
blank(2)

# ---- Part 2 ----
h("Part 2: Your Verdict", size=15)
p("Rank the four problems from 1 to 4 based on how urgently they needed to be fixed in the year 1900. (1 = Most Urgent, 4 = Least Urgent).")
for item in ["Dangerous Industrial Work and Child Labor", "Tenement Life in Crowded Cities",
             "Corrupt Political Machines", "The Power of Trusts"]:
    p("______  " + item, after=3)
p("Defend your top choice (your number 1 ranking) in a short paragraph. You must use specific evidence from your top choice's station and compare it to evidence from at least one other station to prove why your choice was the most urgent threat to the nation.", after=2)
blank(6)

# ---- Teacher key ----
doc.add_page_break()
p("Teacher Answer Key", size=17, bold=True, after=6, font="Georgia")
key = [
    ("Station 1: Dangerous Industrial Work and Child Labor", [
        ("What does this source show about the nature of industrial work? ",
         "It shows that industrial labor was highly unregulated, physically grueling, dirty, and dangerous. Workplaces lacked basic safety equipment, forcing workers to use their bare hands on rough materials in dark, hazardous environments."),
        ("Who was primarily hurt and how? ",
         "Young children were primarily hurt. The physical costs included stunted growth, lung diseases from coal dust, and injuries to their hands. Developmentally, they were robbed of an education and a normal childhood."),
    ]),
    ("Station 2: Tenement Life in Crowded Cities", [
        ("What does this description reveal about housing conditions? ",
         "It reveals that urban housing was severely overcrowded, unsanitary, and lacking basic infrastructure like light and ventilation. Landlords prioritized packing in as many tenants as possible over basic living standards."),
        ("Who suffered the most and how? ",
         "The urban poor, particularly immigrants and children, suffered the most. The lack of sanitation and fresh air caused rampant spread of diseases, while the physical environment offered no safe spaces for daily life or play."),
    ]),
    ("Station 3: Corrupt Political Machines", [
        ("What does this source demonstrate about political machines? ",
         "It demonstrates that political bosses used insider knowledge and public tax money to enrich themselves. They viewed public office as a business opportunity for personal profit rather than a public service."),
        ("Who was ultimately cheated and how? ",
         "The taxpayers and regular citizens were cheated. It damaged democracy by ensuring that city planning and public funds served the interests of corrupt politicians and their loyal insiders rather than the actual needs of the community."),
    ]),
    ("Station 4: The Power of Trusts", [
        ("What does this summary reveal about business tactics? ",
         "It reveals that monopolies used unethical and illegal alliances with other industries (like railroads) to crush competition. They relied on predatory pricing to bankrupt rivals rather than competing fairly."),
        ("Who was financially hurt and how? ",
         "Small business owners and independent refiners were financially ruined. Ultimately, consumers were also hurt because once the trust secured a monopoly, they could artificially inflate prices, harming the broader free market economy."),
    ]),
]
for title, pairs in key:
    h(title, size=13)
    for q, a in pairs:
        par = doc.add_paragraph(); par.paragraph_format.space_after = Pt(6)
        r = par.add_run(q); r.bold = True; r.font.size = Pt(11.5)
        r = par.add_run(a); r.font.size = Pt(11.5)

h("Part 2: Your Verdict (Grading Rubric)", size=13)
p("Student paragraphs will vary based on their ranking. Full credit should be awarded if the student:")
for b in ["Clearly states their number one choice.",
          "Accurately cites evidence from the station corresponding to their top choice (for example, mentioning the coal dust or bare hands from Station 1).",
          "Accurately cites evidence from a second station to serve as a point of comparison (for example, arguing that child labor was a more immediate matter of life and death than the financial graft of political bosses in Station 3)."]:
    par = doc.add_paragraph(style="List Bullet")
    r = par.add_run(b); r.font.size = Pt(11.5); r.font.color.rgb = BLACK

doc.save(BASE + "/lesson-01-activity.docx")
print("activity saved")
