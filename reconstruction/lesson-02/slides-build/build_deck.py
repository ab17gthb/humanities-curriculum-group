#!/usr/bin/env python3
"""Reconstruction Lesson 2 deck, "The Thirteenth Amendment and the Meaning of
Freedom," built to the approved system: image-led slides, fragments only on
screen, comprehensive speaker notes, full lesson + vocabulary coverage."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags, photo_right,
                         divider_photo, content_photo, content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED, W, H)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches
from notes_text import N

dc.IMG = os.path.join(HERE, 'img')
OUT = os.path.join(HERE, '..', 'lesson-02-slides.pptx')

spec = open(os.path.join(HERE, '..', '..', 'build-scripts', 'unit-spec.md')).read()
l2 = spec.split('### Lesson 2')[1].split('### Lesson 3')[0]
DEFS = {}
for line in l2.splitlines():
    m = re.match(r'- (.+?): (.*)$', line.strip())
    if m: DEFS[m.group(1)] = m.group(2)
assert len(DEFS) == 7, DEFS.keys()

def joined(term):
    return f"{term}: {DEFS[term]}"

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

LQ = 'What did the Thirteenth Amendment settle, and why did Congress decide a statute was not enough?'
UQ = 'What did Reconstruction settle about freedom, citizenship, and the federal Union, and what did it leave open?'

# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'RECONSTRUCTION · LESSON 2', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Thirteenth Amendment and the Meaning of Freedom', size=36, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Ratification, two clauses, an exception, and a statute over a veto, 1865 to 1866', size=17, color=POWDER)
notes(s, N[1])

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[(LQ, {})]], size=38, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                (UQ, {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, N[2])

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Abolition ratified, freedom defined, citizenship written', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'Ratification Was a Fight', 'Georgia completes the count, December 6, 1865'),
        ('B', 'Two Clauses, Two Powers', 'A ban in Section 1, a commission in Section 2'),
        ('C', 'The Exception in the Text', 'Punishment for crime, and the door it opened'),
        ('D', 'Freedom Defined From Below', 'Families, marriages, and names of their own'),
        ('E', 'The Conventions State Their Terms', 'Land, wages, schools, and the ballot'),
        ('F', 'Congress Answers With a Statute', "Trumbull's act, a veto, and the override"),
        ('G', 'Settled, and Not Settled', 'Why a statute was judged a frail vessel')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, N[3])

# 4 A DIVIDER
divider_text('Section A', 'Ratification Was a Fight',
             'Proposing words is not law. Twenty seven of thirty six states had to assent.',
             N[4])

# 5 A CONTENT
content_text('The count, state by state',
             ['Passed by Congress, January 31, 1865',
              'Eight former Confederate states counted in the total',
              'Delaware rejects, Kentucky refuses',
              "Georgia assents, December 6, 1865: the twenty seventh vote",
              'Seward proclaims adoption, December 18'],
             N[5], kick='A · Ratification Was a Fight', size=24)

# 6 A CONTENT: IOWA
content_text("Iowa assents after the count closed",
             ['Georgia had already made the amendment law',
              'Iowa ratifies January 24, 1866, the thirty first state',
              'Its resolution quotes the amendment in full',
              'Ratification as commitment, not only arithmetic'],
             N[6], kick='A · Ratification Was a Fight', size=24)

# 7 STAT 27
stat('27', 'of 36 states, the three fourths the Constitution required',
     "Georgia's vote, December 6, 1865 · Proclaimed December 18 · Eight of the 27 were states lately in rebellion",
     N[7], kick='A · Ratification Was a Fight')

# 8 B DIVIDER
divider_text('Section B', 'Two Clauses, Two Powers',
             'Section 1 declares a condition abolished. Section 2 arms Congress to enforce it.',
             N[8])

# 9 B CONTENT
content_text('Section 1: a ban with a geography',
             ['Neither slavery nor involuntary servitude shall exist',
              'Within the United States, or any place under its jurisdiction',
              'No race named, no region named',
              'It does not define citizenship, land, or the vote'],
             N[9], kick='B · Two Clauses, Two Powers', size=24)

# 10 C CONTENT
content_text('The exception in the text',
             ['Except as a punishment for crime',
              'Whereof the party shall have been duly convicted',
              "Words carried from the Northwest Ordinance of 1787",
              'The doorway through which convict leasing grew'],
             N[10], kick='C · The Exception in the Text', size=24)

# 11 D DIVIDER
divider_photo('sewing-port.jpg', 'Section D', 'Freedom Defined From Below',
              ['Freedwomen earning wages in Richmond,', 'the former Confederate capital.'],
              N[11], title_size=38)

# 12 D CONTENT
content_text('Families, marriages, names',
             ['Searches for kin sold away, by notice and letter',
              'Marriages made in law, unions and children recognized',
              'Surnames chosen for the record',
              "Freedom's first test: a family made whole"],
             N[12], kick='D · Freedom Defined From Below', size=24)

# 13 STAT 4,000,000
stat('4,000,000', "freedpeople, the roughly four million the settlement concerned",
     "Stated in the lesson's vocabulary · Their demands and institution building drove the agenda from below",
     N[13], kick='D · Freedom Defined From Below')

# 14 E DIVIDER
divider_text('Section E', 'The Conventions State Their Terms',
             'Delegates elected, minutes kept, petitions sent. Most were received and left unacted on.',
             N[14])

# 15 E CONTENT
content_text("The conventions' demands",
             ['Land of their own, or fair wages on honest contracts',
              'Families protected against forced apprenticeship',
              'Schools for their children',
              'Repeal of the Black Codes, testimony, jury service',
              'The ballot, argued on service and taxes'],
             N[15], kick='E · The Conventions State Their Terms', size=24)

# 16 F DIVIDER
divider_photo('stevens-port.jpg', 'Section F', 'Congress Answers With a Statute',
              ['Thaddeus Stevens of Pennsylvania,', 'the House leader of the Radical Republicans.'],
              N[16], title_size=38)

# 17 F CONTENT PHOTO: TRUMBULL
content_photo('trumbull-port.jpg', "Trumbull and the bill",
              ['Lyman Trumbull, Judiciary chairman, a moderate',
              'All persons born in the United States are citizens',
              'The same rights as white citizens: contract, suit, testimony, property',
              'No ballot, no land, by the coalition\u2019s arithmetic'],
              N[17], kick='F · Congress Answers With a Statute')

# 18 F CONTENT: VETO
content_text("Johnson's veto, March 27, 1866",
             ['Congress cannot confer citizenship, the states govern it',
              'Eleven states unrepresented in Congress',
              'The bill said to favor the colored race over the white',
              'A stride toward centralization, in his account'],
             N[18], kick='F · Congress Answers With a Statute', size=24)

# 19 F CONTENT: OVERRIDE
content_text('The override, April 1866',
             ['Senate repasses, April 6; the House, April 9',
              'The first override of a major measure in the country\u2019s history',
              'The Bureau bill fight ends the same way in July',
              'Congress, not the president, now sets the terms'],
             N[19], kick='F · Congress Answers With a Statute', size=24)

# 20 G DIVIDER
divider_text('Section G', 'Settled, and Not Settled',
             'The override settled who could pass a law. It did not settle whether the law would stand.',
             N[20])

# 21 G CONTENT
content_text('Why a statute was not enough',
             ['A court might read Section 2 narrowly and strike the act down',
              'A hostile president would enforce it feebly',
              'The Black Code legislatures had not surrendered',
              "Congress's next answer: citizenship in the Constitution itself"],
             N[21], kick='G · Settled, and Not Settled', size=24)

# 22 GLANCE
s = slide(NAVY)
kicker(s, "Freedom's terms at a glance")
text(s, 0.9, 1.28, 11.5, 1.0, 'What each record settled, and what it left open', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The amendment', 'Ratified December 1865', 'Settled abolition · Left citizenship open'),
        ('The conventions', 'Freedpeople, 1865 and 1866', 'Stated the program · Held no power to enact it'),
        ('The Civil Rights Act', 'Over a veto, April 1866', 'Wrote citizenship in statute · Authority contested'),
        ('The veto fight', 'Veto, then override', 'Settled who governs · Left the ground unsupplied')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, N[22])

# 23 VOCAB A
vocab('Words for the amendment and the statute',
      [('Thirteenth Amendment', 'ratified December 1865, the first Reconstruction amendment'),
       ('Civil Rights Act of 1866', 'passed over a veto, April 1866')],
      N[23])

# 24 VOCAB B
vocab('Words for the faction and its leader',
      [('Radical Republicans', 'Stevens in the House, Sumner in the Senate'),
       ('Thaddeus Stevens', 'conquered provinces, and land for freed families')],
      N[24])

# 25 VOCAB C
vocab('Words for the author, the assemblies, the people',
      [('Lyman Trumbull', 'the moderate who wrote the act of 1866'),
       ("freedmen's conventions", 'the first political assemblies of the emancipated'),
       ('freedpeople', 'roughly four million, freed by emancipation and the amendment')],
      N[25])

# 26 SYNTHESIS
s = slide(NAVY)
kicker(s, 'The lesson in one view')
text(s, 0.9, 1.28, 11.5, 1.0, 'The settlement of 1866', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Settled', 'Abolition in the Constitution, Congress armed to enforce it'),
        ('Stated', "Freedpeople's terms: land, wages, family, schools, the ballot"),
        ('Written', 'Citizenship and equal rights in statute, over a veto'),
        ('Doubted', 'A contested clause, a hostile president, an unreconciled South')]
yy = 2.78
for t, d in rows:
    text(s, 0.9, yy, 2.4, 0.7, t, size=24, color=RUST_LT, font='Georgia')
    text(s, 3.45, yy + 0.05, 9.0, 0.9, d, size=19, color=CREAM, leading=1.2)
    yy += 1.05
notes(s, N[26])

# 27 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['What did the Thirteenth Amendment settle, and why did Congress decide a statute was not enough? For each record, state which of freedpeople\u2019s terms it answered and which it left standing, then deliver the verdict.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', "Freedom's Terms, Drafted Twice: five stations, a table, and a verdict"),
        ('Notebook', "Notebook page: five definers of freedom in a chart"),
        ('Quick check', "Citizenship and Its Rights: the act's text against Section 2"),
        ('Writing', 'In Law or In Life?: the lesson question as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the amendment defined with its ratification dates, Section 2 and its statute named, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, N[27])

dc.save(OUT)
