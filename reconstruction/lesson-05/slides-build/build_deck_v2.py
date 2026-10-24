#!/usr/bin/env python3
"""Reconstruction Lesson 5 deck, Freedom on the Ground: Land, Labor, Schools,
and Churches, built to the approved system: image-led slides, fragments only
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
OUT = os.path.join(HERE, '..', 'lesson-05-slides.pptx')
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

def content_photo_s(img, title, items, note, kick=None, size=21):
    s = slide(CREAM)
    if kick:
        kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95, 7.0, 1.0, title, size=30, color=NAVY, font='Georgia')
    photo_right(s, img)
    frags(s, items, y=2.35, w=6.9, size=size)
    notes(s, note)
    return s

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'RECONSTRUCTION · LESSON 5', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Freedom on the Ground', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Land, labor, schools, and churches: what freedpeople built, and on what base', size=17, color=POWDER)
notes(s, N[1])

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("What did freedpeople build, and what did the land settlement they never got cost what they built?", {})]],
     size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ("What did Reconstruction settle about freedom, citizenship, and the federal Union, and what did it leave open?", {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, N[2])

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Land denied, institutions built', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The land reserved', 'Field Orders No. 15, 1865; some 40,000 settled'),
        ('B', 'The land taken back', 'Restoration, the Edisto petition, confiscation defeated'),
        ('C', 'Work without land', 'The gang refused; family plots demanded'),
        ('D', 'Sharecropping, the compromise', 'A family plot for a share, commonly half'),
        ('E', 'The crop lien', 'Advances against the crop; debt renewed at settlement'),
        ('F', 'Schools built, savings lost', 'A quarter of a million students by 1870; the bank fails, 1874'),
        ('G', 'The churches, a permanent address', 'AME congregations; the first property owned outright')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, N[3])

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_photo('edisto-school-port.jpg', 'Section A', 'The Land Reserved',
              ['A school on Edisto Island, where freed families first', 'settled the land this section describes.'],
              N[4], title_size=34)

# ------------------------------------------------------ 5 THE ORDER
content_photo_s('edisto-school-port.jpg', 'Special Field Orders No. 15, January 1865',
             ['The Sea Islands and a coastal strip were reserved for freed families.',
              'The reserve covered some 400,000 acres.',
              'Each family could claim a plot of not more than forty acres.',
              'Army inspectors issued possessory titles to the settlers.',
              'The settlers managed their own affairs.'],
             N[5], kick='A · The land reserved', size=19)

# ------------------------------------------------------ 6 STAT 40,000
stat('40,000', 'freedpeople settled in the Sherman reserve by the summer of 1865',
     'Whole communities, farming land they expected to keep',
     N[6], kick='A · The land reserved')

# ------------------------------------------------- 7 SECTION B DIVIDER
divider_text('Section B', 'The Land Taken Back',
             'Johnson\u2019s restoration returns the land to its pardoned owners, the Edisto petitioners answer, and Congress defeats confiscation.',
             N[7])

# ------------------------------------------------------ 8 THE RETURN
content_text('Restoration, refusal, and the roads not taken',
             ['Pardons returned the owners, and orders returned the land.',
              'Commissioner Howard carried the news to Edisto Island himself.',
              'The Edisto petition answered with labor, loyalty, and an offer to pay.',
              'Congress defeated Stevens\u2019s confiscation plan.',
              'The Southern Homestead Act offered poor acres to people with empty pockets.'],
             N[8], kick='B · The land taken back', size=24)

# ------------------------------------------------- 9 SECTION C DIVIDER
divider_text('Section C', 'Work Without Land',
             'Planters press for the gang; freed families demand the family plot, and the working day itself becomes the argument.',
             N[9])

# ------------------------------------------------------ 10 THE LABOR FIGHT
content_text('Two programs for the working day',
             ['Planters wanted squads working under an overseer, with wages paid at year\u2019s end.',
              'Freedpeople refused the gang and the overseer.',
              'Families demanded plots they could work at their own pace.',
              'Many women withdrew their labor from the fields to their own households.',
              'Bureau contracts papered over a standoff that neither side kept.'],
             N[10], kick='C · Work without land', size=24)

# ------------------------------------------------- 11 SECTION D DIVIDER
divider_photo('sc-school-port.jpg', 'Section D', 'Sharecropping, the Compromise',
              ['A freedmen\u2019s school in South Carolina: the farm family\u2019s', 'children, in the compromise\u2019s own country.'],
              N[11], title_size=34)

# ------------------------------------------------------ 12 THE TERMS
content_text('What each side received',
             ['The family received a plot of its own to farm for the year.',
              'The family worked with no overseer and no gang, at its own pace.',
              'The owner received labor settled on his land without paying cash wages.',
              'A share of the crop went to the owner as rent, commonly half.',
              'Accounts were settled once a year, when the crop was sold.'],
             N[12], kick='D · Sharecropping, the compromise', size=24)

# ------------------------------------------------------ 13 STAT ONE HALF
stat('1/2', 'of the crop, commonly, went to the landowner at settlement',
     'Half of the harvest, against the whole of the family\u2019s labor for the year',
     N[13], kick='D · Sharecropping, the compromise')

# ------------------------------------------------- 14 SECTION E DIVIDER
divider_text('Section E', 'The Crop Lien',
             'The family eats on credit from planting to harvest, and the merchant\u2019s claim on the crop is filed before the crop is planted.',
             N[14])

# ------------------------------------------------------ 15 THE CHAIN
content_text('The lien, step by step',
             ['The merchant advanced seed, tools, food, and clothing through the year.',
              'Each advance was recorded at credit prices, with interest.',
              'The lien took the first claim on the growing crop.',
              'The crop was ginned and sold through the creditor.',
              'At settlement the book was read, and the family learned how its year had ended.'],
             N[15], kick='E · The crop lien', size=24)

# ------------------------------------------------------ 16 THE RENEWAL
content_text('Why the debt renewed itself',
             ['A shortfall at settlement opened the next year\u2019s book.',
              'New advances were added at new prices and new interest.',
              'Merchants financed cotton only, the one crop they could always sell.',
              'No acres could be spared for food crops that would have cut the store bill.',
              'A poor year or a disputed account started the cycle again.'],
             N[16], kick='E · The crop lien', size=24)

# ------------------------------------------------- 17 SECTION F DIVIDER
divider_photo('cooke-school-port.jpg', 'Section F', 'Schools Built, Savings Lost',
              ['A Bureau schoolroom in Richmond, 1866: the schools', 'freed communities taxed themselves to build.'],
              N[17], title_size=34)

# ------------------------------------------------------ 18 THE SCHOOLS
content_photo_s('cooke-school-port.jpg', 'Who paid, who taught, who sat in the seats',
             ['Freed communities taxed themselves and raised the schoolhouse frames.',
              'Missionary societies sent teachers and money.',
              'The Freedmen\u2019s Bureau supplied buildings and kept the count.',
              'Black men and women and northern teachers taught in the schools.',
              'Children attended by day, and adults attended at night and on Sundays.'],
             N[18], kick='F · Schools built, savings lost', size=19)

# ------------------------------------------------------ 19 STAT 250,000
stat('250,000', 'students enrolled in the freedmen\u2019s schools by 1870',
     'Enrolled in a region that five years earlier had forbidden most of them literacy by law',
     N[19], kick='F · Schools built, savings lost')

# ------------------------------------------------------ 20 THE BANK
content_text('The Freedmen\u2019s Savings Bank, 1865 to 1874',
             ['Congress chartered the bank in March 1865.',
              'Branches spread across the South and took deposits of a few cents.',
              'Passbooks held savings toward a lot, tools, and schooling.',
              'In 1870 Congress loosened the charter, and the managers speculated.',
              'The bank failed in 1874, and depositors lost much of what they had saved.'],
             N[20], kick='F · Schools built, savings lost', size=24)

# ------------------------------------------------- 21 SECTION G DIVIDER
divider_text('Section G', 'The Churches, a Permanent Address',
             'The one institution on the lesson\u2019s chart that owned its own ground, and the doubled verdict the whole lesson builds toward.',
             N[21])

# ------------------------------------------------------ 22 THE MEETINGHOUSE
content_text('One building, the whole week',
             ['The AME Church, independent since 1816, was carried South by the thousands.',
              'The meetinghouse was often the first property a community owned outright.',
              'On weekdays the building served as a schoolhouse.',
              'On meeting nights it served as a Union League hall.',
              'Its ministers worked as teachers, organizers, and officeholders.'],
             N[22], kick='G · The churches, a permanent address', size=24)

# ------------------------------------------------------ 23 AT A GLANCE
s = slide(NAVY)
kicker(s, 'Freedom on the ground at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Land denied, institutions built', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The land, 1865', '40,000 settled; the land restored', 'A claim on an order, revoked by a policy'),
        ('Labor and credit', 'The gang refused; a share, commonly half', 'The lien financed the year and renewed the debt'),
        ('Schools and savings', '250,000 students by 1870; the bank fails, 1874', 'Literacy gained; savings lost to other men\u2019s speculation'),
        ('Churches', 'AME and Baptist congregations, by the thousands', 'The first property owned outright; schools and politics housed')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.2, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.25, yy + 0.05, 5.1, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.55, yy + 0.05, 3.9, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, N[23])

# ------------------------------------------------------ 24 VOCAB A
vocab('Words for the land',
      [('Special Field Orders No. 15', 'Sherman\u2019s order, January 16, 1865'),
       ('forty acres and a mule', 'the shorthand for land of one\u2019s own')],
      N[24])

# ------------------------------------------------------ 25 VOCAB B
vocab('Words for labor and credit',
      [('sharecropping', 'a family plot for a share of the crop'),
       ('crop lien', 'the merchant\u2019s claim on the crop before it grew')],
      N[25])

# ------------------------------------------------------ 26 VOCAB C
vocab('Words for the institutions',
      [('freedmen\u2019s schools', 'a quarter of a million students by 1870'),
       ('African Methodist Episcopal Church', 'independent since 1816'),
       ('Freedmen\u2019s Savings Bank', 'chartered 1865; failed 1874')],
      N[26])

# ------------------------------------------------------ 27 CLOSING SYNTHESIS
s = slide(NAVY)
kicker(s, 'Closing synthesis')
text(s, 0.9, 1.35, 11.5, 1.1, 'Two findings, held together', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 2.6,
     ["Refused the land they asked to buy, freedpeople built schools, churches, and savings at speed, institutions that outlasted Reconstruction itself.",
      "They built them on shares of crops grown on other men\u2019s land, at prices other men set, so the land settlement they never got taxed everything they built, every year, at every settlement."],
     size=23, color=POWDER, leading=1.3)
notes(s, N[27])

# ------------------------------------------------------ 28 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ["What did freedpeople build, and what did the land settlement they never got cost what they built? Judge the sharecropping settlement, account for the contract\u2019s terms, and state the petitioners\u2019 claim in their own grounds."],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'Freedom\u2019s Ledger: the order, the contract, the schools, the bank, the petition'),
        ('Notebook', 'Notebook page: the land, the labor fight, the lien, the schools, the churches'),
        ('Quick check', 'The Petition and the Settlement: the claim of 1865 beside the terms that followed'),
        ('Writing', 'Built Without Land: your verdict defended from the bank')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: sharecropping and the lien defined, the building in two sentences, and the lesson question answered.',
     size=15, color=POWDER)
notes(s, N[28])

dc.save(OUT)
