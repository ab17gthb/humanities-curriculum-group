#!/usr/bin/env python3
"""Lesson 1 documents: guided notes (student + teacher key) and reading (+ key).
Same design system as the slides: navy/rust/paper, Georgia titles, Arial body."""
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAVY = RGBColor(0x1B, 0x2A, 0x4A)
RUST = RGBColor(0xB5, 0x50, 0x2F)
INK = RGBColor(0x23, 0x27, 0x2E)
GRAY = RGBColor(0x5A, 0x61, 0x6D)
KEYRED = RGBColor(0x00, 0x00, 0x00)  # teacher key prints in bold black
BLACK = RGBColor(0x00, 0x00, 0x00)
OUT = "/home/hatch/workspace/curriculum-planner/progressive-era/lesson-01"

def base_doc():
    doc = Document()
    for sec in doc.sections:
        sec.top_margin = Inches(0.6); sec.bottom_margin = Inches(0.6)
        sec.left_margin = Inches(0.75); sec.right_margin = Inches(0.75)
    st = doc.styles["Normal"]
    st.font.name = "Arial"; st.font.size = Pt(11.5); st.font.color.rgb = INK
    st.paragraph_format.space_after = Pt(6); st.paragraph_format.line_spacing = 1.12
    return doc

def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), hexcolor); tcPr.append(shd)

def rule(doc):
    p = doc.add_paragraph()
    pPr = p._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr"); bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single"); bottom.set(qn("w:sz"), "8")
    bottom.set(qn("w:space"), "1"); bottom.set(qn("w:color"), "B5502F")
    pbdr.append(bottom); pPr.append(pbdr)
    p.paragraph_format.space_after = Pt(6)

def cover(doc, plate, title, subtitle=None):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(2)
    r = p.add_run("U.S. HISTORY  ·  THE PROGRESSIVE ERA"); r.font.size = Pt(9.5)
    r.bold = True; r.font.color.rgb = GRAY
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(2)
    r = p.add_run(title); r.font.size = Pt(20); r.bold = True
    r.font.color.rgb = NAVY; r.font.name = "Georgia"
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(2)
    r = p.add_run(plate.upper()); r.font.size = Pt(10.5); r.bold = True
    r.font.color.rgb = RUST
    if subtitle:
        p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(2)
        r = p.add_run(subtitle); r.font.size = Pt(10.5); r.italic = True
        r.font.color.rgb = GRAY
    rule(doc)
    p = doc.add_paragraph()
    r = p.add_run("Name ______________________________________     Date ______________     Period _______")
    r.font.size = Pt(10.5); r.font.color.rgb = GRAY

def h(doc, text_, size=14, color=NAVY, before=12, after=4):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(before); p.paragraph_format.space_after = Pt(after)
    r = p.add_run(text_); r.bold = True; r.font.size = Pt(size)
    r.font.color.rgb = color; r.font.name = "Georgia"
    return p

def para(doc, text_, size=11.5, after=6, italic=False, color=INK):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(after)
    r = p.add_run(text_); r.font.size = Pt(size); r.italic = italic; r.font.color.rgb = color
    return p

def rich(doc, parts, after=6, size=11.5):
    """parts: list of (text, style) where style in '', 'b', 'key'"""
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    for t, st in parts:
        r = p.add_run(t); r.font.size = Pt(size)
        if st == "b": r.bold = True
        if st == "key": r.font.color.rgb = KEYRED; r.bold = True
    return p

def lines(doc, n=2, color=GRAY):
    for _ in range(n):
        p = doc.add_paragraph()
        r = p.add_run("_" * 96); r.font.color.rgb = color; r.font.size = Pt(10)
        p.paragraph_format.space_after = Pt(10)

def blank(doc, n=3):
    """Open writing space instead of ruled lines (Alex, Oct 20, 2026)."""
    for _ in range(n):
        p = doc.add_paragraph()
        r = p.add_run(" "); r.font.size = Pt(14)
        p.paragraph_format.space_after = Pt(9)

def reading_header(doc):
    """Alex's header (Oct 20, 2026): name/date/period spread across the top
    on one line via tab stops, then directions only. All black."""
    from docx.enum.text import WD_TAB_ALIGNMENT
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.tab_stops.add_tab_stop(Inches(3.1), WD_TAB_ALIGNMENT.LEFT)
    p.paragraph_format.tab_stops.add_tab_stop(Inches(5.3), WD_TAB_ALIGNMENT.LEFT)
    r = p.add_run("Name ____________________\tDate ____________\tPeriod __________")
    r.font.size = Pt(11.5); r.font.color.rgb = BLACK; r.font.name = "Arial"
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10); p.paragraph_format.space_after = Pt(2)
    r = p.add_run("The Problems Progressives Faced")
    r.bold = True; r.font.size = Pt(19); r.font.color.rgb = BLACK; r.font.name = "Georgia"
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(2)
    r = p.add_run("Directions: "); r.bold = True; r.font.size = Pt(11.5); r.font.color.rgb = BLACK
    r = p.add_run("Read the full text, then answer the questions at the end.")
    r.font.size = Pt(11.5); r.font.color.rgb = BLACK

# =====================================================================
# GUIDED NOTES
# =====================================================================
doc = base_doc()
cover(doc, "Guided Notes", "Lesson 1: The Problems Progressives Faced",
      "Essential question: How did Americans respond to the problems created by industrialization, urbanization, and political corruption?")

h(doc, "Key Terms", before=6)
terms = [
    ("laissez-faire", "the idea that government should keep its hands off business and the economy"),
    ("tenement", "a crowded, often unsafe multi-family apartment building in a city"),
    ("political machine", "an organization that controls a city or state government through favors, jobs, and votes"),
    ("graft", "the illegal use of political power for personal profit, such as kickbacks and bribes"),
    ("trust", "a combination of companies formed to control an industry and limit competition"),
    ("Social Gospel", "a movement teaching that Christian faith required improving social conditions"),
    ("settlement house", "a community center in a poor neighborhood offering classes, childcare, and help to residents"),
]
tbl = doc.add_table(rows=0, cols=2); tbl.style = "Table Grid"
for t, d in terms:
    row = tbl.add_row().cells
    r = row[0].paragraphs[0].add_run(t); r.bold = True; r.font.size = Pt(11)
    r = row[1].paragraphs[0].add_run(d); r.font.size = Pt(11)

h(doc, "A. America in 1900")
rich(doc, [("By 1900 the United States held about (1) ____________ people, and about ____________ percent of them lived in cities. The country had (2) ____________ miles of railroad track, and the census counted (3) ____________ children ages 10 to 15 holding jobs.", "")])

h(doc, "B. Problem 1: Work")
rich(doc, [("A normal factory schedule was (4) ____________ hours a day, ____________ days a week. Average factory pay was about (5) $____________ a year. A worker injured on the job had no (6) ____________ and usually no legal claim against the employer.", "")])
rich(doc, [("Child labor: about (7) ____________ of children ages 10 to 15 worked. Photographers such as (8) ____________ documented their conditions for reform organizations.", "")])

h(doc, "C. Problem 2: The City")
rich(doc, [("About ____________ of New Yorkers lived in tenements. Crowding and contaminated water spread diseases such as (9) ____________, ____________, and ____________.", "")])
rich(doc, [("Jacob Riis argued in (10) ____________ (1890) that poverty was caused by ____________, not by the character of the poor.", "")])

h(doc, "D. Problem 3: Corruption")
rich(doc, [("Political machines traded ____________, ____________, and favors for votes. Their profit came from (11) ____________, such as kickbacks on city contracts. Voters kept machines in power because machines (12) ____________.", "")])

h(doc, "E. Problem 4: Corporate Power")
rich(doc, [("By 1904, about (13) ____________ trusts controlled roughly ____________ of American manufacturing. Contemporary estimates held that the richest 1 percent owned about ____________ of the nation's property.", "")])

h(doc, "F. Why Government Did So Little")
rich(doc, [("Give three reasons from the lesson.", "")])
rich(doc, [("1. (14)", "")], after=1)
blank(doc, 1)
rich(doc, [("2.", "")], after=1)
blank(doc, 1)
rich(doc, [("3.", "")], after=1)
blank(doc, 1)

h(doc, "G. Why Reform Came When It Did")
rich(doc, [("List the five roots of reform.", "")])
for i in range(1, 6):
    rich(doc, [(f"{i}.", "")], after=1)
    blank(doc, 1)

h(doc, "The Problems at a Glance")
tbl = doc.add_table(rows=1, cols=3); tbl.style = "Table Grid"
hdr = tbl.rows[0].cells
for i, t in enumerate(["Problem", "One key fact", "Example from the lesson"]):
    r = hdr[i].paragraphs[0].add_run(t); r.bold = True; r.font.size = Pt(11)
for name in ["Work", "The city", "Corruption", "Corporate power"]:
    row = tbl.add_row().cells
    r = row[0].paragraphs[0].add_run(name); r.bold = True; r.font.size = Pt(11)
    for c in (1, 2):
        r = row[c].paragraphs[0].add_run(" "); r.font.size = Pt(16)

h(doc, "Exit Ticket")
para(doc, "1. Name the four problems from today's lesson, and give one specific fact for each.", after=2)
blank(doc, 4)
para(doc, "2. Why did government do so little about these problems before 1900? Give two reasons.", after=2)
blank(doc, 4)
para(doc, "3. Of the five roots of reform, which do you think mattered most? Defend your choice in two or three sentences.", after=2)
blank(doc, 4)

# ---- Teacher key ----
doc.add_page_break()
p = doc.add_paragraph(); r = p.add_run("TEACHER KEY — Guided Notes, Lesson 1")
r.bold = True; r.font.size = Pt(15); r.font.color.rgb = KEYRED; r.font.name = "Georgia"
answers = [
    ("(1)", "76 million; 40"),
    ("(2)", "200,000"),
    ("(3)", "1.75 million"),
    ("(4)", "10 to 12; six"),
    ("(5)", "400 to 500"),
    ("(6)", "workers' compensation"),
    ("(7)", "one in five (about 1.75 million)"),
    ("(8)", "Lewis Hine"),
    ("C blanks", "two-thirds; typhoid, cholera, tuberculosis (any order)"),
    ("(10)", "How the Other Half Lives; the environment (conditions)"),
    ("D blanks", "jobs, contracts; (11) graft; (12) delivered real help to immigrants and the poor (jobs, coal, assistance)"),
    ("(13)", "318; two-fifths; half"),
    ("(14) F reasons", "laissez-faire ideas dominated; courts struck down regulations; government was small and often corrupt; poverty was blamed on the poor themselves (any three)"),
    ("G five roots", "the professional middle class; the press (magazines and photographs); organized women and settlement houses; the Social Gospel; the Populist legacy"),
]
for k, v in answers:
    rich(doc, [(k + "  ", "b"), (v, "key")], after=3)
para(doc, "Exit ticket, question 3: accept any root defended with two supporting facts from the lesson. The strongest answers usually pick the press (it made the other four possible) or organized women (it supplied the trained people).", italic=True)

doc.save(OUT + "/lesson-01-guided-notes.docx")
print("guided notes saved")

# =====================================================================
# READING
# =====================================================================
doc = base_doc()
doc.styles["Normal"].font.color.rgb = BLACK
reading_header(doc)

sections = [
    ("A Country Transformed", [
        "In 1900 the United States was the richest industrial nation on earth. Its factories produced more steel than Britain and Germany combined, its railroads ran for some 200,000 miles, and its cities were filling with people from farms and from overseas. About 76 million people lived in the country, and two of every five lived in a city. A generation earlier, four of five Americans had lived on farms or in small towns.",
        "The wealth was real, but it was unevenly shared, and the speed of the change had outrun the country's ability to manage it. Cities had grown faster than their water systems and sewers. Factories had grown faster than any rules about safety. Corporations had grown larger than the governments that were supposed to oversee them. The Progressive movement, which would dominate American politics for the next twenty years, began as a response to four problems created by this growth: work, the city, corruption, and corporate power.",
    ]),
    ("The Factory Floor", [
        "For the industrial worker, the basic facts of life were long hours and low pay. Ten to twelve hours a day, six days a week, was a standard schedule in factories, mills, and mines. The average factory wage ran between $400 and $500 a year, which was barely enough to keep a family fed and housed. That arithmetic explains the era's most shocking statistic. The census of 1900 counted about 1.75 million children between the ages of 10 and 15 holding jobs, roughly one child in five. They worked in coal mines, textile mills, canneries, and glass factories, usually in the hardest and worst-paid jobs, and most left school by age twelve or never went at all.",
        "The work itself was dangerous. Machines ran without guards, mines filled with explosive dust, and employers pushed for speed. Tens of thousands of workers were killed on the job each year, and many more were injured. An injured worker had almost no protection. There was no workers' compensation, and courts usually held that a worker who took a dangerous job had accepted its risks. A family that lost its breadwinner absorbed the loss alone.",
    ]),
    ("The Crowded City", [
        "Housing in the industrial city was as harsh as the work. About two-thirds of New York City's 3.4 million people lived in tenements, tall buildings divided into small apartments. A whole floor might share a single toilet. Many rooms had no windows and no ventilation, and buildings packed families into spaces meant for half their number. Water came from pumps or taps that were often contaminated, and garbage collection in poor districts was irregular or absent.",
        "Disease was the predictable result. Typhoid, cholera, and tuberculosis moved through crowded districts, and in the worst of them, as many as one infant in five died before reaching a first birthday. The journalist Jacob Riis documented these conditions in his 1890 book How the Other Half Lives, using the new technology of flash photography to show middle-class readers what tenement life actually looked like. Riis's central argument shaped the movement that followed: the cause of tenement poverty was the environment, not the character of the poor. If conditions made people sick and desperate, then changing conditions could change outcomes.",
    ]),
    ("Government for Sale", [
        "The third problem was that the governments closest to these conditions were often part of them. Many cities were controlled by political machines, disciplined organizations that traded jobs, contracts, and favors for votes. A machine's profit came from graft: kickbacks on paving and construction contracts, bribes from businesses that wanted a franchise or wanted an inspector to look away. State governments could be worse. Railroad and mining companies bought legislatures outright, and since state legislatures chose United States senators, corporate money reached into the Senate itself.",
        "Machines survived because they were useful. A ward boss could find a new immigrant a job, deliver coal in winter, and help a family facing eviction or a son in trouble with the law. Reformers who attacked the machines as simply corrupt missed why voters stayed loyal. Any successful reform would have to replace what the machines provided, not just condemn them.",
    ]),
    ("Corporate Power and the Late Response", [
        "Above the machines stood the fourth problem. By 1904, roughly 318 trusts controlled about two-fifths of American manufacturing, and Standard Oil had refined about 90 percent of the nation's oil at its peak. Contemporary estimates held that the richest 1 percent of Americans owned about half of the country's property, while the bottom half of families owned almost none of it. Farmers shipped their crops on railroads whose rates they could not negotiate, and small businesses competed against firms that could afford to sell at a loss until their rivals closed.",
        "Why did government respond so slowly? The reigning idea of the age was laissez-faire, the belief that government should not interfere with business. Courts enforced the idea by striking down state laws that regulated hours and conditions. Government itself was small, and much of it was for sale. Many comfortable Americans also believed poverty was a character flaw, the result of laziness or drink, which made Riis's environmental argument a genuine challenge to common sense.",
        "The response came when it did because several forces matured at once. An educated professional middle class had grown large enough to staff a movement. Cheap magazines and printed photographs carried evidence of the problems into millions of homes. Women, organized through clubs, temperance campaigns, and settlement houses such as Jane Addams's Hull House in Chicago, had built networks of trained reformers. Churches preaching the Social Gospel taught that faith required repairing society, not just saving souls. And the farmers of the Populist movement had spent the 1890s arguing that concentrated power was the nation's central problem. The Progressives inherited all of it. What they did with it is the story of this unit.",
    ]),
]
for title, paras in sections:
    h(doc, title, before=10, color=BLACK)
    for t in paras:
        para(doc, t, color=BLACK)

h(doc, "Questions", color=BLACK)
qs = [
    "1. According to the reading, why did so many children work in 1900?",
    "2. What did Jacob Riis argue caused tenement poverty, and how did that differ from what many Americans believed?",
    "3. Why did political machines stay in power even though they were corrupt?",
    "4. Choose two of the five reasons the reading gives for why reform came when it did. Explain how each one helped turn problems into a movement.",
    "5. Which of the four problems do you think was most urgent in 1900? Support your answer with two facts from the reading.",
]
for q in qs:
    para(doc, q, after=3, color=BLACK)
    blank(doc, 3)

doc.add_page_break()
p = doc.add_paragraph(); r = p.add_run("TEACHER KEY — Reading, Lesson 1")
r.bold = True; r.font.size = Pt(15); r.font.color.rgb = KEYRED; r.font.name = "Georgia"
key = [
    ("1.", "Adult wages (about $400 to $500 a year) were too low to support a family, so children had to work for the family to survive. Employers also preferred children for many jobs because they were cheap and could fit into small spaces."),
    ("2.", "Riis argued the environment caused tenement poverty: crowding, disease, and lack of sanitation and opportunity. The common view held that poverty resulted from personal character flaws such as laziness or drink."),
    ("3.", "Machines provided real services to immigrants and the poor, including jobs, coal, housing help, and assistance with officials. Voters remained loyal because the machine met needs that no one else met."),
    ("4.", "Any two, explained. Middle class: supplied trained, confident reformers and voters. Press: made conditions visible nationally, creating pressure. Organized women: supplied networks and experienced activists through clubs and settlement houses. Social Gospel: gave reform a moral and religious justification. Populist legacy: supplied the argument that concentrated power was the problem and government could act."),
    ("5.", "Accept any of the four if defended with two accurate facts from the reading. Work: hours, pay, deaths, child labor. City: tenement crowding, disease, infant deaths. Corruption: graft and purchased legislatures. Corporate power: trusts' share of manufacturing and wealth concentration."),
]
for k, v in key:
    rich(doc, [(k + "  ", "b"), (v, "key")], after=5)

doc.save(OUT + "/lesson-01-reading.docx")
print("reading saved")
