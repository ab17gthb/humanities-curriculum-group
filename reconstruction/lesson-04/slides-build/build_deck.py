#!/usr/bin/env python3
"""Reconstruction Lesson 4 deck, The New Political Order: The Vote and Black
Officeholding, built to the approved system: image-led slides, fragments only
on screen, comprehensive speaker notes, full lesson and vocabulary coverage.
Fonts: Georgia titles, Lato body. Speaker notes live in notes_text.py."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags, photo_right,
                         divider_photo, content_photo, content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED, W, H)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches
from notes_text import NOTES

dc.IMG = os.path.join(HERE, 'img')
OUT = os.path.join(HERE, '..', 'lesson-04-slides.pptx')
N = NOTES

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

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'RECONSTRUCTION · LESSON 4', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The New Political Order', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'The vote, the coalition, and the men it carried to the Senate and a governor\u2019s chair', size=17, color=POWDER)
notes(s, N[1])

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("Who governed the reconstructed South, and what did the Fifteenth Amendment settle and leave open?", {})]],
     size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ("What did Reconstruction settle about freedom, citizenship, and the federal Union, and what did it leave open?", {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, N[2])

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'An electorate, a coalition, an amendment', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'An electorate made in a year', 'Registration, 1867; some 700,000 Black voters enrolled'),
        ('B', 'The leagues and the conventions', 'Union League organizing; constitutions of 1867 and 1868'),
        ('C', 'Who governed: the coalition', 'Carpetbaggers, scalawags, and Black voters and officeholders'),
        ('D', 'Revels takes a Senate seat', '1870; the schools argument of February 1871'),
        ('E', 'A governor and a full term', 'Pinchback, 1872 and 1873; Bruce, elected 1874'),
        ('F', 'The Fifteenth Amendment', 'Proposed 1869, ratified 1870; three grounds forbidden'),
        ('G', 'What the new order rested on', 'Federal law, federal presence, and a will to enforce')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, N[3])

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_photo('first-vote-port.jpg', 'Section A', 'An Electorate Made in a Year',
              ['Registration under the Reconstruction Acts,', 'and a line of new voters forms across the South.'],
              N[4], title_size=34)

# ------------------------------------------------------ 5 REGISTRATION
content_text('Registration: names on the rolls, 1867',
             ['Boards open across the ten unreconstructed states',
              'Army officers supervise the enrollment',
              'Black registrants a majority in several states',
              'The rolls choose the conventions of 1867',
              'No land, no wages: the vote arrives first'],
             N[5], kick='A · An electorate made in a year', size=24)

# ------------------------------------------------------ 6 STAT 700,000
stat('700,000', 'Black voters enrolled in a single year, 1867',
     'Enrolled where none had voted before, in states that had counted them as property',
     N[6], kick='A · An electorate made in a year')

# ------------------------------------------------- 7 SECTION B DIVIDER
divider_text('Section B', 'The Leagues and the Conventions',
             'The Union League organizes the new electorate in churches and schoolhouses, and the conventions write the South\u2019s most democratic charters.',
             N[7])

# ------------------------------------------------------ 8 LEAGUES AND CONVENTIONS
content_text('Organization, then constitutions',
             ['Union League chapters, under the Loyal League name',
              'Ballots, conventions, and tickets taught at night',
              'Black delegates in every convention',
              'A Black majority in South Carolina\u2019s',
              'Public schools and civil rights written into law'],
             N[8], kick='B · The leagues and the conventions', size=24)

# ------------------------------------------------- 9 SECTION B/C DIVIDER PHOTO
divider_photo('sc-legislature-port.jpg', 'Section B · The governments', 'A Legislature, Counted',
              ['The composite portrait of South Carolina\u2019s first', 'legislature after the war: a roster, not a symbol.'],
              N[9], title_size=34)

# ------------------------------------------------------ 10 THE COALITION
content_text('Three groups, two hostile names',
             ['Black voters: the largest bloc in most states',
              'Northern newcomers, called carpetbaggers',
              'White southern Republicans, called scalawags',
              'Officeholders by the hundreds in the legislatures',
              'The names are weapons; read them as evidence'],
             N[10], kick='C · Who governed: the coalition', size=24)

# ------------------------------------------------------ 11 STAT 76 OF 124
stat('76 of 124', 'delegates to South Carolina\u2019s convention of 1868 were Black men',
     'The only Black majority in any southern Reconstruction convention',
     N[11], kick='C · Who governed: the coalition')

# ------------------------------------------------- 12 SECTION D DIVIDER
divider_photo('revels-port.jpg', 'Section D', 'Revels Takes a Senate Seat',
              ['A Mississippi minister who recruited Black regiments', 'takes the seat Jefferson Davis had left.'],
              N[12], title_size=34)

# ------------------------------------------------------ 13 THE SEATING
content_text('Seated, 48 to 8, February 1870',
             ['Elected by the Mississippi legislature',
              'The first Black member of Congress',
              'Opponents cite Dred Scott and nine years of citizenship',
              'The Senate seats him on the new Constitution',
              'The seat Jefferson Davis had held'],
             N[13], kick='D · Revels takes a Senate seat', size=24)

# ------------------------------------------------------ 14 THE SPEECH
content_text('February 1871: prejudice has no justifying cause',
             ['The trustees\u2019 report: equality in the common schools',
              'They had not asked, fearing they could not obtain it',
              'Prejudice falls equally, whatever the conduct',
              'It must be admitted wicked, and wrong',
              'His side lost the vote'],
             N[14], kick='D · Revels takes a Senate seat', size=24)

# ------------------------------------------------- 15 SECTION E DIVIDER
divider_photo('pinchback-port.jpg', 'Section E', 'A Governor and a Full Term',
              ['Louisiana carries the new order to the governor\u2019s chair,', 'and Mississippi sends a senator for a full term.'],
              N[15], title_size=34)

# ------------------------------------------------------ 16 PINCHBACK
content_text('Pinchback: five weeks in the governor\u2019s chair',
             ['Freeborn in Georgia; a Union captain in the war',
              'State senate president, then lieutenant governor',
              'Acting governor, December 9, 1872, to January 13, 1873',
              'The first Black man to govern an American state',
              'A caretaker, governing in a contested state'],
             N[16], kick='E · A governor and a full term', size=24)

# ------------------------------------------------------ 17 BRUCE
content_photo('bruce-port.jpg', 'Bruce: the full term, 1875 to 1881',
             ['Born enslaved in Virginia in 1841',
              'Registrar, sheriff, superintendent of education',
              'Elected to the Senate in 1874',
              'The first Black senator to serve a full term',
              'Seated as the settlement was being dismantled'],
             N[17], kick='E · A governor and a full term')

# ------------------------------------------------- 18 SECTION F DIVIDER
divider_text('Section F', 'The Fifteenth Amendment',
             'Proposed in February 1869 and ratified in February 1870, the third and last of the Reconstruction amendments, read here word by word.',
             N[18])

# ------------------------------------------------------ 19 THE TEXT
content_text('Section 1, and the power behind it',
             ['The right of citizens to vote, protected',
              'Not denied or abridged by the United States, or any state',
              'On account of race, color, or previous condition of servitude',
              'Section 2: Congress shall have power to enforce',
              'A prohibition, not a grant'],
             N[19], kick='F · The Fifteenth Amendment', size=24)

# ------------------------------------------------------ 20 THE SILENCES
content_text('What the wording leaves standing',
             ['Literacy tests and poll taxes name no racial ground',
              'Written neutrally, aimed at the new electorate',
              'Within a generation, the polls close again',
              'The woman suffrage alliance breaks over the text',
              'An amendment protects men\u2019s votes, and says nothing of women\u2019s'],
             N[20], kick='F · The Fifteenth Amendment', size=24)

# ------------------------------------------------------ 21 STAT 3
stat('3', 'grounds of denial the amendment forbids',
     'Race · color · previous condition of servitude, and every other ground left standing',
     N[21], kick='F · The Fifteenth Amendment')

# ------------------------------------------------- 22 SECTION G DIVIDER
divider_text('Section G', 'What the New Order Rested On',
             'Federal law made it, federal presence guarded it, and its survival hung on a national will to keep enforcing it.',
             N[22])

# ------------------------------------------------------ 23 THE LEDGER
content_text('The achievement and its foundation',
             ['An electorate enrolled; constitutions written',
              'Schools founded; officeholders at every level',
              'An amendment ratified, with an enforcement clause',
              'All of it resting on federal protection',
              'Power given is not yet power used'],
             N[23], kick='G · What the new order rested on', size=24)

# ------------------------------------------------------ 24 AT A GLANCE
s = slide(NAVY)
kicker(s, 'The new order at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'An electorate, a coalition, an amendment', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Electorate and charters', 'Registration and League, 1867; conventions, 1868', 'Public schools and civil rights written into state law'),
        ('The coalition', 'Black voters; carpetbaggers; scalawags', 'Governments staffed at every level, by the hundreds'),
        ('The roster', 'Revels 1870; Pinchback 1872; Bruce 1874', 'A Senate seat, a governor\u2019s chair, a full term'),
        ('The amendment', 'Proposed 1869; ratified 1870', 'Three grounds forbidden; all others left standing')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.2, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.25, yy + 0.05, 5.1, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.55, yy + 0.05, 3.9, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, N[24])

# ------------------------------------------------------ 25 VOCAB A
vocab('Words for the amendment and the senator',
      [('Fifteenth Amendment', 'proposed 1869, ratified 1870'),
       ('Hiram Rhodes Revels', 'the first Black member of Congress, 1870')],
      N[25])

# ------------------------------------------------------ 26 VOCAB B
vocab('Words for the governor and the full term',
      [('Blanche K. Bruce', 'the first full Senate term, from 1875'),
       ('P. B. S. Pinchback', 'acting governor of Louisiana, five weeks')],
      N[26])

# ------------------------------------------------------ 27 VOCAB C
vocab('Words for the coalition and its organization',
      [('carpetbaggers', 'the hostile name for northern newcomers'),
       ('scalawags', 'the hostile name for white southern Republicans'),
       ('Union League', 'the clubs that organized the new electorate')],
      N[27])

# ------------------------------------------------------ 28 CLOSING SYNTHESIS
s = slide(NAVY)
kicker(s, 'Closing synthesis')
text(s, 0.9, 1.35, 11.5, 1.1, 'Two findings, held together', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 2.6,
     ["Between 1867 and 1870 the South built the broadest democracy the country had yet run, and wrote the vote\u2019s protection into the Constitution.",
      "The amendment forbade three grounds of denial and left the rest standing, and the governments it crowned rested on a federal protection they could not supply themselves."],
     size=23, color=POWDER, leading=1.3)
notes(s, N[28])

# ------------------------------------------------------ 29 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ["Who governed the reconstructed South, and what did the Fifteenth Amendment settle and leave open? Judge the records, account for the amendment\u2019s wording, and state what the new order rested on."],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The New Electorate Speaks and Is Pictured: the amendment, the speech, two pictures, a roster'),
        ('Notebook', 'Notebook page: the electorate, the conventions, the coalition, the roster, the amendment'),
        ('Quick check', 'The Amendment and the Senator: the text of 1870 beside the argument of 1871'),
        ('Writing', 'Settled in Text, Resting on Protection: your judgment defended from the bank')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the League and the amendment defined, the coalition in two sentences, and the lesson question answered.',
     size=15, color=POWDER)
notes(s, N[29])

dc.save(OUT)
