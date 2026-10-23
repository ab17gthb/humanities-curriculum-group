#!/usr/bin/env python3
"""Lesson 1 test deck, built to Alex's slide model:
image-led slides, fragments only on screen, comprehensive speaker notes,
full lesson + vocabulary coverage. Fonts: Georgia titles, Lato body."""
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

# ---------------------------------------------------------------- 1 · TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(IMG, 'title-169.jpg'), 0, 0, prs.slide_width, prs.slide_height)
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'PROGRESSIVE ERA · LESSON 1', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Problems Progressives Faced', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'How a rich, growing country produced a movement to reform itself', size=17, color=POWDER)
notes(s, "Welcome to the Progressive Era unit. Set the frame before the details: between about 1890 and 1920 the United States tried to fix problems that its own growth had created. That is the puzzle of the whole unit. The country was not poor or failing. It was the richest industrial nation on earth, and reform grew out of that success. Today's lesson is the foundation for everything that follows. We look at four problems (work, the city, corruption, and corporate power), then ask why government did so little about them for so long, and why reform finally came when it did. The unit question, which students have on their guided notes beneath today's lesson question: How did Americans respond to the problems created by industrialization, urbanization, and political corruption? The photograph is Mulberry Street in New York, about 1900, from the Detroit Publishing Company. Nearly everything in this lesson is visible in that one street: crowding, street markets, pushcarts, children everywhere, and a city straining to hold the people arriving in it.")

# ------------------------------------------------- 2 · ESSENTIAL QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('Why did industrial America produce a reform movement?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': RUST_LT, 'italic': True}),
                                ('How did Americans respond to the problems created by industrialization, urbanization, and political corruption?', {'italic': True})]],
     size=17, color=POWDER, font='Georgia', leading=1.2)
notes(s, "Put the lesson question up and leave it up while students settle; the unit question runs beneath it as the frame for the whole unit. Three vocabulary words inside the unit question matter and will recur all unit: industrialization (the shift to factory production), urbanization (the growth of cities), and corruption (the use of public office for private gain). A useful cold-open: ask students which of the three forces they think caused the most damage, and have them commit to an answer in one sentence. They will revisit that judgment at the exit ticket. Emphasize the word respond. This unit is not mainly a catalogue of misery. It is about what people did once the problems became impossible to ignore, and the response is the story of the next eight lessons: muckrakers, political reforms, Roosevelt, Taft, Wilson, suffrage, and finally the limits of what reform achieved.")

# ------------------------------------------------------------ 3 · STAT 1900
stat('76 MILLION', 'people in the United States in 1900',
     'Two of every five lived in a city. A generation earlier, four of five Americans lived on farms or in small towns.',
     "Start with scale, because students underestimate how fast this country changed. In 1900 the United States held about 76 million people and was the richest industrial nation on earth. Its factories produced more steel than Britain and Germany combined, and its railroads ran for some 200,000 miles. The deeper change was where people lived. About two of every five Americans now lived in a city; a generation earlier four of five had lived on farms or in small towns. The wealth was real, but it was unevenly shared, and the speed of the change had outrun the country's ability to manage it. Cities had grown faster than their water systems and sewers. Factories had grown faster than any rules about safety. Corporations had grown larger than the governments meant to oversee them. That gap, between the size of the problems and the size of the response, is what the Progressive movement grew out of.",
     kick='A country transformed')

# --------------------------------------------------------- 4 · FOUR PROBLEMS
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.35, 11.5, 1.0, 'Four problems', size=46, color=CREAM, font='Georgia')
rule(s, 0.92, 2.5)
rows = [('1', 'Work', 'long hours, low pay, dangerous machines'),
        ('2', 'The city', 'crowding, disease, and housing unfit to live in'),
        ('3', 'Corruption', 'governments traded for favors and run for profit'),
        ('4', 'Corporate power', 'trusts larger than the governments watching them')]
yy = 2.95
for n, t, d in rows:
    text(s, 0.9, yy, 0.7, 0.7, n, size=30, color=RUST_LT, font='Georgia')
    text(s, 1.65, yy + 0.04, 3.3, 0.7, t, size=27, color=CREAM, bold=True)
    text(s, 5.1, yy + 0.10, 7.4, 0.7, d, size=20, color=POWDER)
    yy += 1.02
notes(s, "This is the map of the lesson, and it matches the reading and the guided notes exactly. Problem one is work: the hours, pay, and dangers of the industrial job. Problem two is the city: what happened when millions of people crowded into housing and sanitation systems built for far fewer. Problem three is corruption: the governments closest to these problems were often part of them. Problem four is corporate power: combinations of companies so large that neither competitors nor governments could easily check them. Tell students to listen for one specific fact per problem, because the exit ticket asks them to name all four problems with one fact each. The four-part structure also previews the unit test blueprint, where the first entry is simply the problems of industrial America.")

# ------------------------------------------------- 5 · PROBLEM ONE DIVIDER
divider_photo('spinner-port.jpg', 'Problem one', 'Work',
              ['The basic facts of a factory life:', 'long hours, low pay, real danger'],
              "The photograph is a young spinner in a cotton mill, taken by Lewis Hine. Keep the introduction to the problem simple: for the industrial worker, the basic facts of life were long hours and low pay, and the work itself could kill or maim. Everything else in this section is evidence for those three claims. A teaching note: students often assume bad conditions were a secret that reformers uncovered. They were not secret. They were visible on every factory floor and in every mill town. What changed later was not the visibility of the problems but the political willingness to treat them as public business rather than private misfortune. That distinction sets up the end of the lesson, when we ask why government did so little for so long.",
              title_size=54)

# ------------------------------------------------------ 6 · WORK CONDITIONS
content_photo('work-port.jpg', 'The factory floor',
              ['10 to 12 hours a day, six days a week',
               '$400 to $500 a year for the average factory hand',
               'Machines ran without guards',
               'No workers\u2019 compensation if you were hurt'],
              "The photograph shows breaker boys inside a Pennsylvania coal breaker in 1911, photographed by Lewis Hine. Now the numbers. Ten to twelve hours a day, six days a week, was a standard schedule in factories, mills, and mines. The average factory wage ran between 400 and 500 dollars a year, barely enough to keep a family fed and housed. Hold that figure, because it explains the child labor statistic on the next slide: families did not send children to work out of indifference, they sent them because the arithmetic of rent and food required it. The work was dangerous in routine ways. Machines ran without guards, mines filled with explosive dust, and employers pushed for speed. Tens of thousands of workers were killed on the job each year and many more were injured. An injured worker had almost no protection. There was no workers' compensation system, and courts usually held that a worker who took a dangerous job had accepted its risks. A family that lost its breadwinner absorbed the loss alone.",
              kick='Problem one · Work')

# ------------------------------------------------------- 7 · CHILD LABOR STAT
s = slide(NAVY)
photo_right(s, 'breaker-port.jpg')
kicker(s, 'Problem one · Work')
text(s, 0.9, 1.5, 6.9, 2.4, '1.75 MILLION', size=64, color=CREAM, font='Georgia', leading=1.05)
text(s, 0.9, 3.15, 6.7, 1.0, 'children ages 10 to 15 held jobs in 1900', size=25, color=CREAM, leading=1.25)
rule(s, 0.92, 4.35)
text(s, 0.9, 4.65, 6.6, 1.8, 'One child in five. Most had left school by twelve, and many never went at all.',
     size=20, color=POWDER, leading=1.3)
notes(s, "This is the statistic students remember, so give it room. The census of 1900 counted about 1.75 million children between the ages of 10 and 15 holding jobs, roughly one child in five. They worked in coal mines, textile mills, canneries, and glass factories, usually in the hardest and worst-paid jobs, and most left school by age twelve or never went at all. Two points keep this from becoming a simple villain story. First, the cause was arithmetic: with adult wages at 400 to 500 dollars a year, a family often could not survive without a child's wages, which is exactly what the reading's first test question asks about. Second, employers had their own reasons to hire children: they were cheap, they could fit into small spaces, and they rarely organized. The photograph shows breaker boys outside the Ewen Breaker in South Pittston, Pennsylvania, 1911, by Lewis Hine, whose camera becomes a reform weapon in Lesson 2. Ask students: if you were a parent in 1900 making 450 dollars a year, what would you do? The discomfort of that question is the lesson.")

# ------------------------------------------------------------ 8 · THE DANGER
content_text('Danger was part of the job',
             ['Tens of thousands of workers killed on the job each year',
              'Explosive dust underground, unguarded belts and gears above it',
              'Courts called it assumed risk: you took the job, you took the danger',
              'A family that lost its earner absorbed the loss alone'],
             "Expand the last slide's danger point, because it explains why workplace safety became a reform issue rather than a private one. The hazards were ordinary, not exceptional: unguarded machinery, coal dust that could explode, and a production system that rewarded speed. When accidents happened, the legal system mostly sided with employers. Under the doctrine students will see phrased in the reading, a worker who accepted a dangerous job was treated as having accepted its risks, and fellow-servant rules often blocked claims even when a coworker's error caused the injury. There was no workers' compensation, no disability system, and no pension for a widow. The cost of industrial accidents was real; it was simply billed to the families least able to pay it. This is a good place to plant a flag for later in the unit: the Triangle Shirtwaist fire of 1911, which students meet in this lesson's quick check, turned exactly these abstractions into 146 deaths behind locked doors, and it changed New York law within a few years.",
             kick='Problem one · Work')

# ------------------------------------------------- 9 · PROBLEM TWO DIVIDER
divider_photo('tenement-port.jpg', 'Problem two', 'The City',
              ['Millions of people, housing built for far fewer'],
              "Turn from the workplace to the home. Housing in the industrial city was as harsh as the work, and for the same underlying reason: growth outran every system meant to manage it. New York is the extreme case and the one the reading uses, but the pattern held in Chicago, Boston, Pittsburgh, and every other industrial city. Immigrants arriving from overseas and migrants arriving from American farms landed in the same few districts, because that was where the cheap housing and the jobs were. Landlords responded to demand by subdividing: buildings were split into ever smaller apartments and rented to ever more people. Nothing in the arrangement rewarded ventilation, plumbing, or light, and for years almost nothing in the law required them.",
              title_size=54)

# ----------------------------------------------------- 10 · TENEMENT CONDITIONS
content_photo('lodgers-port.jpg', 'Life in the tenements',
              ['Two-thirds of New York City lived in tenements',
               'A whole floor might share a single toilet',
               'Rooms without windows or ventilation',
               'Water from pumps and taps, often contaminated'],
              "The photograph is a police photograph of lodgers in a Bayard Street tenement, about 1890, associated with Jacob Riis's reporting. The key figure: about two-thirds of New York City's 3.4 million people lived in tenements, tall buildings divided into small apartments. Conditions inside followed from crowding and cost-cutting. A whole floor might share a single toilet. Many rooms had no windows and no ventilation. Buildings packed families into spaces meant for half their number. Water came from pumps or taps that were often contaminated, and garbage collection in poor districts was irregular or absent. When students picture a tenement, they often picture poverty in the abstract. Push them to picture logistics instead: hundreds of people, one toilet, no clean water, no airflow, no garbage pickup. Disease was not a mystery in that environment. It was the predictable output of the inputs, which is precisely the argument Riis makes two slides from now.",
              kick='Problem two · The city')

# ---------------------------------------------------------- 11 · DISEASE STAT
stat('1 IN 5', 'infants died before their first birthday in the worst districts',
     'Typhoid, cholera, and tuberculosis moved through the crowded wards.',
     "Disease was the predictable result of the conditions on the previous slide. Typhoid spread through contaminated water, cholera through water and food, and tuberculosis through the air of crowded, unventilated rooms. In the worst districts, as many as one infant in five died before reaching a first birthday. Pause on what that number meant inside a family: in the hardest neighborhoods, losing a baby was a common experience rather than a rare tragedy. It also shaped how reformers argued. They did not have to persuade middle-class readers that tenement families were virtuous. They only had to show that the conditions themselves manufactured sickness, and that sickness did not respect the boundary between the tenement district and the rest of the city. Epidemics were one of the forces that made the problems of the poor into problems for everyone, which is a theme the muckrakers in Lesson 2 exploit deliberately.",
     kick='Problem two · The city')

# --------------------------------------------------------------- 12 · RIIS
content_photo('riis-port.jpg', 'Jacob Riis and a new argument',
              ['How the Other Half Lives, 1890',
               'Flash photography carried the tenements to middle-class readers',
               'His claim: conditions make the poor, not character'],
              "Jacob Riis was a police reporter who documented tenement conditions in his 1890 book How the Other Half Lives, using the new technology of flash photography to show middle-class readers what tenement life actually looked like. The technology mattered: magnesium flash powder let him photograph dark interiors that had never been photographed before, and readers who could dismiss a written description found the photographs harder to wave away. But the book's lasting contribution was an argument. Riis held that the cause of tenement poverty was the environment, not the character of the poor. Crowding, disease, and darkness produced the behavior that comfortable Americans blamed on laziness or drink. If conditions made people sick and desperate, then changing conditions could change outcomes. That single move, from character to environment, is the intellectual hinge of the entire Progressive movement, and the reading's second test question targets it directly. Students should be able to state both sides by the end of the lesson: the common view blamed poverty on personal flaws such as laziness or drink; Riis blamed the environment that poverty lived in.",
              kick='Problem two · The city')

# ----------------------------------------------- 13 · PROBLEM THREE DIVIDER
divider_photo('nast-port.jpg', 'Problem three', 'Corruption',
              ['The governments closest to the problems', 'were often part of them'],
              "The cartoon is Thomas Nast's work against the Tweed Ring, which students analyze in today's activity. The third problem is that the governments closest to these conditions were often part of them. Many cities were controlled by political machines, disciplined organizations that traded jobs, contracts, and favors for votes. State governments could be worse. Railroad and mining companies bought legislatures outright, and because state legislatures chose United States senators, corporate money reached into the Senate itself. Frame the section honestly for students: this is the problem that made the other three so durable. Dangerous factories and lethal housing persisted partly because the officials who might have regulated them were profiting from the arrangement, or owed their jobs to the people who did.",
              title_size=54)

# -------------------------------------------------------------- 14 · MACHINES
content_text('Government for sale',
             ['Machines traded jobs, contracts, and favors for votes',
              'Profit came from graft: kickbacks on contracts, bribes for franchises',
              'Railroads and mines bought state legislatures outright',
              'Legislatures chose US senators, so the money reached the Senate'],
             "Define the machine precisely, because the vocabulary slide returns to it. A political machine was an organization that controlled a city or state government through favors, jobs, and votes, run by a boss who disciplined the organization like a business. Its profit came from graft, the illegal use of political power for personal profit: kickbacks on paving and construction contracts, bribes from businesses that wanted a franchise or wanted an inspector to look away. William Tweed's ring in New York, the target of the Nast cartoon, looted the city treasury on a scale that still anchors the era's reputation. At the state level the buyers were usually corporations rather than bosses. Railroad and mining companies bought legislatures outright, and since legislatures chose United States senators until the Seventeenth Amendment changed the rule in 1913, corporate money reached into the Senate itself. That amendment is Lesson 3's story; plant it here so students hear the payoff coming.",
             kick='Problem three · Corruption')

# --------------------------------------------------- 15 · WHY VOTERS STAYED
content_text('Why voters stayed loyal',
             ['A ward boss could find a new immigrant a job',
              'Coal in winter, help with an eviction, a word with the law',
              'The machine met needs that nobody else was meeting',
              'Reform had to replace the machine, not just condemn it'],
             "This slide carries the lesson's most important piece of nuance, and the reading's third test question. Machines survived because they were useful. A ward boss could find a new immigrant a job, deliver coal in winter, and help a family facing eviction or a son in trouble with the law. For a poor family, the machine was not an abstraction about clean government; it was the only institution that answered the door. Reformers who attacked the machines as simply corrupt missed why voters stayed loyal. Any successful reform would have to replace what the machines provided, not just condemn them, and the settlement houses in the roots of reform did exactly that, offering the same help without the vote attached. Ask students directly: if the boss's man brought your family coal in January, what would a reformer's speech about honest government have to offer you in exchange for your vote? Let the silence do the teaching.",
             kick='Problem three · Corruption')

# ----------------------------------------------- 16 · PROBLEM FOUR DIVIDER
s = slide(NAVY)
s.shapes.add_picture(os.path.join(IMG, 'octopus-169.jpg'), 0, 0, prs.slide_width, prs.slide_height)
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'PROBLEM FOUR', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Corporate Power', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Combinations larger than the governments meant to oversee them', size=17, color=POWDER)
notes(s, "The image is the famous Puck magazine cartoon of 1904 showing Standard Oil as an octopus with its tentacles around steel, copper, shipping, the Capitol, and reaching for the White House. Students work with this cartoon in today's activity, so do not over-explain it here; let them read the tentacles themselves at the station. The fourth problem stood above the machines: by 1904, roughly 318 trusts controlled about two-fifths of American manufacturing, and Standard Oil had refined about 90 percent of the nation's oil at its peak. A trust, in the vocabulary sense students need, is a combination of companies formed to control an industry and limit competition. The point to establish is asymmetry. Farmers shipped crops on railroads whose rates they could not negotiate. Small businesses competed against firms that could afford to sell at a loss until their rivals closed. And the government that might have answered was small, laissez-faire in philosophy, and in many places for sale.")

# ------------------------------------------------------------- 17 · TRUSTS STAT
stat('318 TRUSTS', 'controlled about two-fifths of American manufacturing by 1904',
     'Standard Oil refined about 90 percent of the nation\u2019s oil at its peak. Contemporary estimates held that the richest 1 percent owned about half the country\u2019s property.',
     "Give the concentration numbers their own moment. By 1904, roughly 318 trusts controlled about two-fifths of American manufacturing. Standard Oil had refined about 90 percent of the nation's oil at its peak, a figure students can grasp instantly: one company, one essential product, almost no alternative. Contemporary estimates held that the richest 1 percent of Americans owned about half of the country's property, while the bottom half of families owned almost none of it. Students do not need to accept the era's estimates as modern econometrics; they need to understand what contemporaries believed they were looking at, because belief is what moved politics. The consequences ran downhill to ordinary people. A farmer in Kansas shipped wheat at whatever rate the railroad posted. A small refiner or grocer competed against a firm that could sell below cost in his town until he closed, then raise prices once he was gone. Monopoly was not an economics abstraction in 1900. It was a price your family paid.",
     kick='Problem four · Corporate power')

# --------------------------------------------- 18 · WHY SO LITTLE (DIVIDER)
divider_text('The harder question', 'Why did government do so little?',
             'The problems were visible for decades before the response came.',
             "Pivot the lesson here. Students now know the four problems, and the honest puzzle is the delay: tenements, child labor, graft, and trusts were all visible by the 1880s, yet serious national reform waited until after 1900. The reading gives a connected explanation rather than a single cause. An idea, laissez-faire, said government should keep its hands off business. Institutions matched the idea: courts struck down regulations, and government at every level was small. Part of government was compromised, bought by the very interests it might have regulated. And a belief about poverty, that it reflected character, told comfortable Americans the suffering they saw was earned. Each element gets a slide's worth of attention in the notes on the next slide; on screen, keep the four causes as fragments and let students sort which they think mattered most.")

# ------------------------------------------------------- 19 · LAISSEZ-FAIRE
content_text('An idea, and the machinery behind it',
             ['Laissez-faire: government keeps its hands off business',
              'Courts struck down state laws on hours and conditions',
              'Government was small, and much of it was for sale',
              'Poverty was widely blamed on the poor themselves'],
             "Walk the four causes slowly; the guided notes ask students for three reasons, and the strongest answers combine an idea with an institution. First, the reigning idea of the age was laissez-faire, the belief that government should not interfere with business. Second, courts enforced the idea, striking down state laws that regulated hours and conditions, so even legislatures willing to act often could not. Third, government itself was small, with tiny staffs and budgets, and much of it was for sale to the interests it might have regulated. Fourth, many comfortable Americans believed poverty was a character flaw, the result of laziness or drink, which made Riis's environmental argument a genuine challenge to common sense. If poverty is your fault, the state owes you nothing; if poverty is manufactured by conditions, the state might owe you new conditions. That is why a photography book from 1890 matters to a political movement twenty years later.",
             kick='Why so little response')

# ----------------------------------------------- 20 · WHY REFORM (DIVIDER)
divider_text('The turn', 'Why reform came when it did',
             'Several forces matured at the same moment. The Progressives inherited all of them.',
             "The response came when it did because several forces matured at once, and the reading names five roots. This section matters beyond today: the rest of the unit is these five roots at work. The professional middle class staffs the movement in every lesson. The press becomes the muckrakers of Lesson 2. Organized women drive the suffrage fight in Lesson 7 and much of the rest besides. The Social Gospel supplies the moral language reformers preach with. The Populist legacy supplies the argument, rehearsed through the 1890s, that concentrated power is the nation's central problem. Have students copy the five roots carefully; the guided notes and the reading's fourth question both require them, and the exit ticket asks which root mattered most.")

# ------------------------------------------------------------ 21 · FIVE ROOTS
s = slide(CREAM)
kicker(s, 'Why reform came', color=RUST)
text(s, 0.9, 0.95, 11.5, 1.0, 'Five roots of reform', size=31, color=NAVY, font='Georgia')
roots = [('The professional middle class', 'educated, organized, and numerous enough to staff a movement'),
         ('The press', 'cheap magazines and photographs carried the evidence into millions of homes'),
         ('Organized women', 'clubs, temperance campaigns, and settlement houses built trained networks'),
         ('The Social Gospel', 'faith that required repairing society, not only saving souls'),
         ('The Populist legacy', 'a decade of arguing that concentrated power was the problem')]
yy = 2.05
for t, d in roots:
    text(s, 0.9, yy, 4.6, 0.6, t, size=22, color=INK, bold=True)
    text(s, 5.6, yy + 0.05, 6.9, 0.8, d, size=18, color=MUTED, leading=1.15)
    yy += 0.98
notes(s, "Take each root in turn, with an example students can hold onto. One, an educated professional middle class had grown large enough to staff a movement: lawyers, teachers, social workers, and journalists with training and confidence. Two, cheap magazines and printed photographs carried evidence of the problems into millions of homes; this is the root that makes Lesson 2's muckrakers possible. Three, women organized through clubs, temperance campaigns, and settlement houses such as Jane Addams's Hull House in Chicago had built networks of trained reformers, and settlement houses did the machine's helping work without demanding votes. Four, churches preaching the Social Gospel taught that faith required repairing society, not just saving souls, giving reform a moral vocabulary. Five, the farmers of the Populist movement had spent the 1890s arguing that concentrated power was the nation's central problem, and the Progressives inherited the argument ready-made. If a student asks which root mattered most, that is literally exit ticket question three; the strongest answers usually pick the press, because it made the other four possible, or organized women, because they supplied the trained people.")

# ------------------------------------------------------------- 22 · VOCAB A
def vocab(title, terms, note, kick='The vocabulary'):
    s = slide(CREAM)
    kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95, 11.5, 1.0, title, size=30, color=NAVY, font='Georgia')
    yy = 2.1
    for term, dfn in terms:
        text(s, 0.9, yy, 4.1, 0.9, term, size=25, color=NAVY, font='Georgia')
        text(s, 5.15, yy + 0.06, 7.3, 1.1, dfn, size=19, color=MUTED, leading=1.2)
        yy += 1.52
    notes(s, note)
    return s

vocab('Words for the problems',
      [('laissez-faire', 'the idea that government should keep its hands off business and the economy'),
       ('tenement', 'a crowded, often unsafe multi-family apartment building in a city'),
       ('political machine', 'an organization that controls a city or state government through favors, jobs, and votes')],
      "These definitions match the guided notes word for word, so students can copy them directly. Laissez-faire is French for allow to do, and in this era it named the default setting of American government rather than a fringe position; both major parties governed by it most of the time. A tenement was not simply any apartment building: the word carried the specific meaning of a crowded, subdivided urban building rented to many families, usually with shared facilities and little light or air. A political machine sounds illegal by definition, and students should understand it was usually a legal organization doing partly illegal things: it won real elections with real votes, then converted public office into jobs, contracts, and profit. The precision matters for the unit test, whose matching section uses these definitions nearly verbatim.")

# ------------------------------------------------------------- 23 · VOCAB B
vocab('Words for the system',
      [('graft', 'the illegal use of political power for personal profit, such as kickbacks and bribes'),
       ('trust', 'a combination of companies formed to control an industry and limit competition'),
       ('Social Gospel', 'a movement teaching that Christian faith required improving social conditions'),
       ('settlement house', 'a community center in a poor neighborhood offering classes, childcare, and help to residents')],
      "Four more terms, again matching the guided notes exactly. Graft is the profit of corruption: kickbacks on contracts and bribes for franchises or for inspectors to look away. A trust was originally a legal device, a board of trustees holding the stock of formerly competing companies, and it became the era's general word for a monopoly combination; students meet the word constantly from here on, including in trust-busting in Lesson 4. The Social Gospel was the religious wing of reform, preached by ministers such as Walter Rauschenbusch, holding that Christian faith required improving social conditions and not only saving individual souls. A settlement house was its most practical expression: a community center planted in a poor neighborhood, staffed largely by college-educated women, offering classes, childcare, and help to residents. Jane Addams's Hull House in Chicago, founded in 1889, was the famous model, and Addams herself becomes a recurring figure in this unit.")

# --------------------------------------------------------- 24 · TODAY'S WORK
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'The Reformer\u2019s Notebook', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 2.6,
     ['Four stations, four problems. Read each source, answer its questions, then rank the problems in the verdict section.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Station 1', 'Dangerous work and child labor'), ('Station 2', 'The tenement city'),
        ('Station 3', 'The boss and the machine'), ('Station 4', 'The octopus of Standard Oil')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.5, 0.6, d, size=19, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.8, 11.5, 0.5, 'Exit ticket: the four problems, one fact each, and the root of reform you would defend.',
     size=16, color=POWDER)
notes(s, "Close by handing the lesson to the activity, the Reformer's Notebook, which students already have. The four stations mirror the four problems in order: Hine's breaker boys photograph for work, Riis's Bayard Street tenement photograph for the city, Nast's 1872 cartoon against Boss Tweed for corruption, and the 1904 Puck cartoon of the Standard Oil octopus for corporate power. Each station asks what the source shows and who was hurt; the verdict section at the end asks students to rank the four problems by urgency and defend the ranking, which rehearses the reading's fifth question. Logistics from experience: the descriptions under each image carry the content, so students who struggle with the images themselves can still work from the text. Before they leave, the exit ticket from the guided notes: name the four problems with one specific fact each; give two reasons government did so little before 1900; and pick the root of reform that mattered most and defend it in two or three sentences. Next lesson, the muckrakers take these same problems and turn them into the most explosive journalism in American history.")

prs.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lesson-01-slides-test.pptx'))
print('slides:', len(prs.slides.__iter__.__self__._sldIdLst))
