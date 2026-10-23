#!/usr/bin/env python3
"""Sectional Crisis and Civil War Lesson 1 deck, "The Compromise of 1850 and the
Fugitive Slave Act," built to the approved system: image-led slides, fragments
only on screen, comprehensive speaker notes, full lesson + vocabulary coverage."""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
sys.path.insert(0, '/tmp')
sys.path.insert(0, HERE)
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags, photo_right,
                         divider_photo, content_photo, content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED, W, H)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches
from notes_text import N

dc.IMG = os.path.join(HERE, 'img')
OUT = os.path.join(HERE, '..', 'lesson-01-slides.pptx')

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

# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'SECTIONAL CRISIS AND CIVIL WAR · LESSON 1', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Compromise of 1850 and the Fugitive Slave Act', size=36, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'A last bargain, its price, and the North commanded to enforce it, 1849 to 1850', size=17, color=POWDER)
notes(s, N[1])

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("What did the Compromise of 1850 settle, and what did its Fugitive Slave Act ask the North to do?", {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ("How did compromise over slavery finally fail, and what did the war it caused settle about slavery and the Union, and what did it leave open?", {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, N[2])

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'The last settlement and its enforcement clause, in seven stretches', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'California knocks at the door', 'A free state against a Senate balanced 15 to 15'),
        ('B', 'Two roads to a settlement', "Taylor's direct road, Clay's omnibus bargain"),
        ('C', "Calhoun's last word", 'Equality demanded, the cords snapping'),
        ('D', 'Webster speaks for the Union', 'The Seventh of March plea and \u201cIchabod\u201d'),
        ('E', 'The package fails, the pieces pass', 'Douglas bill by bill, Fillmore signing'),
        ('F', 'The terms, stated flatly', 'Five measures, each section paid'),
        ('G', 'The Act at work, and the answer', 'Commissioners, posses, and the liberty laws')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, N[3])

# 4 A DIVIDER
divider_text('Section A', 'California Knocks at the Door',
             'The gold rush state applied free, and the Senate balance broke.',
             N[4])
# 5 A CONTENT
content_text('A free constitution, written in a year',
             ['Gold peoples California overnight',
              'Settlers prohibit slavery in their constitution',
              'Statehood applied for as a free state',
              'The Wilmot fight adjourned, the question forced'],
             N[5], kick='A · California and the balance', size=24)
# 6 A STAT
stat('15 to 15', 'free states and slave states in the Senate of 1850',
     'Two senators each · The balance was the South\u2019s veto · California free makes it 16 to 15',
     N[6], kick='A · California and the balance')
# 7 B DIVIDER
divider_photo('clay-port.jpg', 'Section B', 'Two Roads to a Settlement',
              ['Mathew Brady photograph of Henry Clay,', 'taken about 1849, late in his life.'],
              N[7])
# 8 B CONTENT
content_text("Taylor's road and Clay's bargain",
             ['Taylor: admit California and New Mexico at once',
              'Their constitutions settle slavery, Congress aside',
              'Clay: every question priced inside one package',
              'Each section carries home a victory',
              'Each section swallows a defeat in the same vote'],
             N[8], kick='B · Two roads', size=24)
# 9 C DIVIDER
divider_photo('calhoun-port.jpg', 'Section C', "Calhoun's Last Word",
              ['Mathew Brady photograph of John C. Calhoun,', 'taken about 1849, in his last year.'],
              N[9])
# 10 C CONTENT
content_text('The cords snapping, one by one',
             ['Dying, his speech read aloud by Mason',
              'March 4, 1850: equality in the territories',
              'Faithful return of fugitives demanded',
              'Agitation snaps the cords successively',
              'At the end, nothing left but force'],
             N[10], kick='C · Calhoun\u2019s last word', size=24)
# 11 D DIVIDER
divider_photo('webster-port.jpg', 'Section D', 'Webster Speaks for the Union',
              ['Daniel Webster, daguerreotype by', 'Southworth and Hawes. Metropolitan Museum.'],
              N[11])
# 12 D CONTENT
content_text('The Seventh of March, and its price',
             ['Not as a Massachusetts man, but as an American',
              'The whole package, the fugitive law included',
              'Peaceable secession an impossibility',
              'Whittier answers in \u201cIchabod\u201d',
              'The glory departed, his readers judged'],
             N[12], kick='D · Webster for the Union', size=24)
# 13 E DIVIDER
divider_text('Section E', 'The Package Fails, the Pieces Pass',
             'The omnibus collapsed in July. Douglas passed the measures one at a time.',
             N[13])
# 14 E CONTENT
content_text('Five majorities do what one package could not',
             ['July 1850: the omnibus picked apart',
              'Clay, exhausted, goes home to Kentucky',
              'Douglas passes each measure separately',
              'Taylor dies, Fillmore favors the settlement',
              'September 1850: five laws, one name'],
             N[14], kick='E · Passage in pieces', size=24)
# 15 F DIVIDER
divider_text('Section F', 'The Terms, Stated Flatly',
             'Read the settlement the way a clerk would read it.',
             N[15])
# 16 F CONTENT
content_text('Five terms, each section paid',
             ['California free',
              'Utah and New Mexico, no slavery restriction',
              'Texas boundary settled, its debt assumed',
              'Slave trade ended in the District of Columbia',
              'A far stricter Fugitive Slave Act'],
             N[16], kick='F · The terms', size=24)
# 17 G DIVIDER
divider_photo('tubman-port.jpg', 'Section G', 'The Act at Work, and the Answer',
              ['Harriet Tubman, photographed by Horatio G. Squyer,', 'about 1885. National Portrait Gallery.'],
              N[17])
# 18 G CONTENT 1
content_text('Rendition at street level',
             ['Seized on an owner\u2019s affidavit',
              'A commissioner, not a judge and jury',
              'The accused cannot testify, and has no jury',
              'Bystanders summoned, all citizens commanded',
              'Aiding punished: $1,000 and six months'],
             N[18], kick='G · The Act at work', size=24)
# 19 G CONTENT 2
content_text('The North answers in law and in flight',
             ['Personal liberty laws in the statehouses',
              'State officers forbidden, state jails denied',
              'Jury trials granted that federal law withheld',
              'The Underground Railroad works on',
              'Tubman returns south, again and again'],
             N[19], kick='G · The answer', size=24)
# 20 G STAT
stat('$10 / $5', 'the commissioner paid ten dollars to remand, five to free',
     'The fee schedule of section 8, quoted by the Act\u2019s critics in the statute\u2019s own numbers',
     N[20], kick='G · The Act at work')
# 21 SYNTHESIS
content_text('Settled, and asked',
             ['Settled: statehood, territories, Texas, the District trade',
              'Passed in pieces, signed by Fillmore',
              'Asked: rendition without jury or testimony',
              'Asked: the bystander conscripted, the aider punished',
              'Answered: liberty laws and the railroad'],
             N[21], kick='Synthesis · The lesson question', size=24)
# 22 VOCAB A
vocab('The settlement, the law, the peacemaker',
      [('Compromise of 1850', 'the package of five measures of September 1850'),
       ('Fugitive Slave Act', 'the law of September 18, 1850'),
       ('Henry Clay', 'the senator who framed the last settlement')],
      N[22])
# 23 VOCAB B
vocab('The orator, the laws, the network, the conductor',
      [('Daniel Webster', 'the Seventh of March plea for the Union'),
       ('personal liberty laws', 'the northern statutes obstructing rendition'),
       ('Underground Railroad', 'the network carrying enslaved people north'),
       ('Harriet Tubman', 'the most famous conductor on the railroad')],
      N[23])
# 24 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'The compromise file', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ["For each record, state what it gives, what it takes, and who is made to act. Then judge whether the Compromise of 1850 was a settlement of the slavery question or an armistice whose terms guaranteed the fighting would resume."],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Compromise File: the resolutions, the plea, the warning, the Act, the lithograph'),
        ('Notebook', 'Notebook page: six pieces of the story, classified and evidenced'),
        ('Quick check', 'Ten Dollars and Five: the statute read against its background'),
        ('Writing', 'A Settlement, or an Armistice? The terms weighed against the enforcement')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the balance stated, the passage in pieces explained, and the lesson question answered with two settlements and two requirements of the Act.',
     size=15, color=POWDER)
notes(s, N[24])

for i, n in N.items():
    print(i, len(n.split()))
dc.save(OUT)
