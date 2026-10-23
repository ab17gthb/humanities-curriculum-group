#!/usr/bin/env python3
"""Reconstruction Lesson 1 deck, "After Appomattox: Presidential Reconstruction,"
built to the approved system: image-led slides, fragments only on screen,
comprehensive speaker notes, full lesson + vocabulary coverage."""
import os, sys, json
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
text(s, 0.9, 5.32, 11.5, 0.4, 'RECONSTRUCTION · LESSON 1', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'After Appomattox: Presidential Reconstruction', size=36, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Pardons, a bureau, the Black Codes, and freedpeople stating their terms, 1865', size=17, color=POWDER)
notes(s, N[1])

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("What did Johnson's restoration give back to the South, and what did it leave freedpeople to fight for?", {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ("What did Reconstruction settle about freedom, citizenship, and the federal Union, and what did it leave open?", {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, N[2])

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'A settlement built in one fall, in seven stretches', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The president the war left behind', 'Johnson succeeds Lincoln, April 1865'),
        ('B', 'The Amnesty Proclamation', 'Pardons, property, fourteen classes excepted'),
        ('C', 'Three acts and a claim', 'Void, abolish, repudiate; the states never left'),
        ('D', "The Freedmen's Bureau at work", 'Rations, contracts, courts, marriages, schools'),
        ('E', 'Freedom reaches Texas', 'General Orders No. 3, Galveston, June 19'),
        ('F', 'The Black Codes', "Mississippi's Vagrant Law and the fifty dollar fine"),
        ('G', 'Freedpeople answer', 'The Edisto petition and Anderson\'s letter')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, N[3])

# 4 A DIVIDER
divider_text('Section A', 'The President the War Left Behind',
             'Appomattox on April 9, Lincoln dead on April 15, and every question about the peace open.',
             N[4])
# 5 A CONTENT
content_text('A successor nobody had voted on for the peace',
             ['A tailor turned senator from Tennessee',
              'Stayed loyal when his state seceded',
              "Lincoln's War Democrat on the 1864 ticket",
              'Terms, meaning, enforcement: all undecided'],
             N[5], kick='A · The succession', size=24)
# 6 B DIVIDER
divider_photo('johnson-port.jpg', 'Section B', 'The Amnesty Proclamation',
              ['Andrew Johnson, photographed', 'about 1870 to 1880.'],
              N[6])
# 7 B CONTENT
content_text('Pardon first, terms after',
             ['May 29, 1865: swear loyalty, recover property',
              'No one recovers the people he enslaved',
              'Provisional governors, conventions called',
              'The electorate: the white South of before the war'],
             N[7], kick='B · The proclamation', size=24)
# 8 B STAT
stat('14', 'classes excepted from the general pardon',
     'High officers and the wealthy applied to Johnson personally · He pardoned freely, by the thousands',
     N[8], kick='B · The proclamation')
# 9 B/C CONTENT on classes (slide 9 in notes is classes discussion; use stat-adjacent content)
content_text('The exception that restored the leaders',
             ['The leadership and the wealth, excepted by name',
              'Each man applies to the president personally',
              'The asking acknowledges federal authority',
              'The granting restores land, standing, eligibility'],
             N[9], kick='B · The fourteen classes', size=24)
# 10 C DIVIDER
divider_text('Section C', 'Three Acts and a Claim',
             'Void secession, abolish slavery, repudiate the debts. Nothing else was required.',
             N[10])
# 11 C CONTENT
content_text('Three acts, and a long list of absences',
             ['Void the secession ordinance',
              'Abolish slavery in the state',
              'Repudiate the war debts',
              'Not required: the ballot, testimony, land'],
             N[11], kick='C · The three acts', size=24)
# 12 D DIVIDER
divider_photo('howard-port.jpg', 'Section D', "The Freedmen's Bureau at Work",
              ['Oliver Otis Howard, the Bureau\'s', 'commissioner, by Mathew Brady.'],
              N[12])
# 13 D CONTENT
content_text('Relief, and then the hard work',
             ['Created March 3, 1865, in the War Department',
              'Rations and hospitals, for both races',
              'Contracts supervised, Bureau courts sitting',
              'Marriages legalized, schools built'],
             N[13], kick='D · The Bureau', size=24)
# 14 D CONTENT 2 (agent's position) -- notes 14 is Texas; adjust: notes[14] is E intro. Keep deck order: this slide uses N[13] already; merge: skip extra D content, go E divider
divider_photo('granger-port.jpg', 'Section E', 'Freedom Reaches Texas',
              ['Gordon Granger, from the Brady Handy', 'collection, Library of Congress.'],
              N[14])
# 15 E CONTENT
content_text('An order with two halves',
             ['Galveston, June 19, 1865: all slaves are free',
              'Absolute equality of personal rights',
              'Employer and hired labor, the new connection',
              'Remain home, work for wages, no idleness'],
             N[15], kick='E · General Orders No. 3', size=24)
# 16 E STAT
stat('June 19, 1865', 'freedom enforced in Texas, two years after it was proclaimed',
     'Black Texans marked the day as Emancipation Day, later Juneteenth',
     N[16], kick='E · General Orders No. 3')
# 17 F DIVIDER
divider_text('Section F', 'The Black Codes',
             'The restored legislatures rebuilt labor control in statute form, in public, in print.',
             N[17])
# 18 F CONTENT
content_text("Mississippi's Vagrant Law, at working level",
             ['Over eighteen, no lawful employment: a vagrant',
              'Assembly and association reached as well',
              'Fine, jail, and hiring out by the sheriff',
              'Black children apprenticed without consent'],
             N[18], kick='F · The Codes', size=24)
# 19 F STAT
stat('$50', 'the fine for a freedman convicted of vagrancy in Mississippi',
     'A sum a contract laborer rarely held in cash · Unpaid, he was hired out by the sheriff',
     N[19], kick='F · The Codes')
# 20 G DIVIDER
divider_photo('bureau-port.jpg', 'Section G', 'Freedpeople Answer',
              ["A. R. Waud's drawing of the Freedmen's Bureau,", "Harper's Weekly, 1868. Library of Congress."],
              N[20])
# 21 G CONTENT 1
content_text('Edisto Island: labor and loyalty',
             ['Settled land, certificates in hand',
              'Restoration returns it to pardoned owners',
              '"We have made these lands what they are"',
              'The ask: purchase land, hold it as his own'],
             N[21], kick='G · The petition', size=24)
# 22 G CONTENT 2
content_text("Anderson's arithmetic",
             ['Dayton, Ohio: $25 a month, children in school',
              'The test of sincerity: pay the back wages',
              '$11,680 for 32 years and 20',
              'Safety for his daughters, schools for his children'],
             N[22], kick='G · The letter', size=24)
# 23 SYNTHESIS
content_text('Given back, and left to fight for',
             ['Given back: pardons, property, land, governments',
              'Left to fight for: land, wages, the ballot',
              'Left to fight for: safety, schools, equal rights',
              'December 1865: Congress returns'],
             N[23], kick='Synthesis · The lesson question', size=24)
# 24 VOCAB A
vocab('The period, the president, the plan, the pardon',
      [('Reconstruction', 'the period from 1865 to 1877'),
       ('Andrew Johnson', 'the Tennessee tailor and Unionist Democrat'),
       ('presidential Reconstruction', "the restoration program Johnson ran from April 1865"),
       ('Amnesty Proclamation', "Johnson's proclamation of May 29, 1865")],
      N[24])
# 25 VOCAB B
vocab('The bureau, the codes, the freedman',
      [("Freedmen's Bureau", 'the federal agency Congress created in March 1865'),
       ('Black Codes', 'the laws the restored southern governments passed in 1865 and 1866'),
       ('Jourdon Anderson', 'the Tennessee freedman who in August 1865 answered his former enslaver')],
      N[25])
# 26 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'The settlement on paper', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ["For each record, state whose freedom it enlarged or narrowed and by what instrument. Then judge which record a freed family in December 1865 would have felt most in its daily life, and defend your judgment from the documents."],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Settlement on Paper: the terms, the Vagrant Law, the petition, the letter, the order'),
        ('Notebook', 'Notebook page: six pieces of the story, classified and evidenced'),
        ('Quick check', 'Fifty Dollars: the statute read against its background'),
        ('Writing', 'Given Back, and Left to Fight For: the terms weighed against the Codes')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, "Exit ticket: the three acts stated, the Bureau's position explained, and the lesson question answered with two restorations and two fights.",
     size=15, color=POWDER)
notes(s, N[26])

for i, n in N.items():
    print(i, len(n.split()))
dc.save(OUT)
