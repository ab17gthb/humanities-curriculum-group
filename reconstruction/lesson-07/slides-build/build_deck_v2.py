#!/usr/bin/env python3
"""Reconstruction Lesson 7 deck, "The Retreat: Courts, Panic, and the Leagues,"
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
OUT = os.path.join(HERE, '..', 'lesson-07-slides.pptx')

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
    photo_right(s, img)
    if kick: kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95 if kick else 0.8, 6.9, 1.2, title, size=31, color=NAVY, font='Georgia', leading=1.05)
    frags(s, items, y=2.15 if kick else 2.0, w=6.9, size=size)
    notes(s, note)
    return s

# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'RECONSTRUCTION · LESSON 7', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Retreat: Courts, Panic, and the Leagues', size=36, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Amnesty, a narrowed amendment, hard times, daylight terror, and one last act, 1872 to 1876', size=17, color=POWDER)
notes(s, N[1])

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("By what steps, legal, economic, and violent, did the country retreat from the settlement between 1872 and 1876?", {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ("What did Reconstruction settle about freedom, citizenship, and the federal Union, and what did it leave open?", {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, N[2])

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'A settlement dismantled by inches, in seven stretches', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'Amnesty and the Liberal Republican revolt', 'The old leaders eligible again, 1872'),
        ('B', 'The Court reads the amendment narrowly', 'Slaughter-House, April 1873, 5 to 4'),
        ('C', 'The Panic of 1873', "Cooke fails, six years of depression, the House lost"),
        ('D', 'The White League by daylight', 'Coushatta and Liberty Place, 1874'),
        ('E', 'The last Civil Rights Act', "Sumner's cause, Hays's defense, March 1875"),
        ('F', "Nast's two mirrors", 'Worse Than Slavery and Colored Rule, 1874'),
        ('G', '1876 approaches', 'Three Republican states still standing')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, N[3])

# 4 A DIVIDER
divider_text('Section A', 'Amnesty and the Liberal Republican Revolt',
             'The disability removed in May 1872, and retreat made respectable in the same year.',
             N[4])
# 5 A CONTENT
content_text('The disability removed at a stroke',
             ['The Fourteenth Amendment barred the old leaders from office.',
              'Removal once took two thirds of Congress, case by case.',
              'In May 1872, nearly all were restored at once.',
              'Seven years after Appomattox, the old class was eligible again.'],
             N[5], kick='A · The Amnesty Act', size=24)
# 6 A PHOTO
content_photo_s('greeley-port.jpg', 'Retreat, dressed as reform',
              ['Reform Republicans broke with Grant in 1872.',
               'The Liberal Republicans nominated Greeley, and the Democrats endorsed him.',
               'The platform called for amnesty, civil service reform, and an end to protection.',
               'Grant won, and the vocabulary stayed.'],
              N[6], kick='A · The Liberal Republicans')
# 7 B DIVIDER PHOTO
divider_photo('miller-port.jpg', 'Section B', 'The Court Reads the Amendment Narrowly',
              ['Samuel Freeman Miller, who wrote', 'the opinion, by Mathew Brady.'],
              N[7])
# 8 B CONTENT
content_text('A concession, and then a line',
             ["The amendments' purpose was conceded in full.",
              'Two citizenships, national and state, were held distinct.',
              'The amendment protected only the narrow rights of national citizenship.',
              'The great body of civil rights was left to the states.'],
             N[8], kick='B · Slaughter-House', size=24)
# 9 B STAT
stat('5 to 4', 'the Slaughter-House decision, April 1873',
     'The first reading of the Fourteenth Amendment · The privileges or immunities clause read down to a short list',
     N[9], kick='B · Slaughter-House')
# 10 C DIVIDER
divider_text('Section C', 'The Panic of 1873',
             'Hard times at home outbid the South for the North\'s attention, for six years.',
             N[10])
# 11 C PHOTO
content_photo_s('cooke-port.jpg', "The war's financier falls",
              ['Jay Cooke\'s banking house failed in September 1873.',
               'Railroad loans failed, banks closed, and mills shut.',
               'Protection had to compete with empty tables.',
               'In 1874, the House went Democratic.'],
              N[11], kick='C · The panic')
# 12 C STAT
stat('6 years', 'of depression after the Panic of 1873',
     'Longer than the war · It covered the League, the act of 1875, and the election of 1876',
     N[12], kick='C · The panic')
# 13 D DIVIDER
divider_text('Section D', 'The White League by Daylight',
             'No disguises and no denials: a platform in print, and a parish establishment in arms.',
             N[13])
# 14 D CONTENT
content_text('Coushatta and Liberty Place',
             ['In Louisiana in 1874, the League stated its object in print.',
              'A white man\'s government was openly pledged.',
              'At Coushatta, officeholders were murdered in August 1874.',
              'At Liberty Place, the League held the statehouse for three days.'],
             N[14], kick='D · The League', size=24)
# 15 D CONTENT 2
content_text('Answered, and resented',
             ['Federal troops restored the governor.',
              'Each rescue read worse in the North.',
              'The protected were recast as the provocation.',
              'Weariness was manufactured and spent.'],
             N[15], kick='D · The second victory', size=24)
# 16 E DIVIDER PHOTO
divider_photo('sumner-port.jpg', 'Section E', 'The Last Civil Rights Act',
              ['Charles Sumner of Massachusetts,', 'by Mathew Brady. Library of Congress.'],
              N[16])
# 17 E CONTENT
content_text('The broadest statute, the thinnest enforcement',
             ['The act of March 1875 covered inns, conveyances, and theaters.',
              'Juries were opened, and denial was made a misdemeanor.',
              'The person aggrieved could claim $500.',
              'Prosecutors were few, marshals were exposed, and the act went largely unenforced.'],
             N[17], kick='E · The act of 1875', size=24)
# 18 E CONTENT 2
content_text('Hays on the floor',
             ['Hays was an Alabama congressman and a former enslaver.',
              'He counted his cost before he spoke.',
              'He offered freedpeople\'s conduct as the evidence.',
              'He answered "social equality" as a manufactured fancy.'],
             N[18], kick='E · The defense', size=24)
# 19 F DIVIDER PHOTO
divider_photo('nast-port.jpg', 'Section F', "Nast's Two Mirrors",
              ['Thomas Nast, by Napoleon Sarony,', 'about 1870. National Portrait Gallery.'],
              N[19])
# 20 F CONTENT
content_text('Worse Than Slavery, described',
             ['In October 1874, a White Leaguer and a Klansman shook hands over a shield.',
              'A Black family stood between a skull and an alphabet book.',
              'A schoolhouse burned in the background.',
              'Nast named the partnership between daylight politics and night terror.'],
             N[20], kick='F · The indictment', size=24)
# 21 F CONTENT 2
content_text('Colored Rule, described',
             ['In March 1874, Black legislators were drawn in uproar.',
              'Columbia scolded them and told them to take back seats.',
              'The drawing carried the era\'s caricature in its faces and mockery.',
              'The cartoon taught northern readers to picture Black government as disorder.'],
             N[21], kick='F · The caricature', size=24)
# 22 G CONTENT
content_text('The map at the opening of 1876',
             ['The old leaders were restored, and the amendment was narrowed.',
              'Northern attention was spent, and the House was lost.',
              'Violence was answered late and wearily.',
              'One asset was left: the amendments themselves.'],
             N[22], kick='G · 1876 approaches', size=24)
# 23 G STAT
stat('3', 'southern states still Republican in 1876',
     'South Carolina, Florida, and Louisiana · Each resting on federal troops near its statehouse',
     N[23], kick='G · 1876 approaches')
# 24 SYNTHESIS
content_text('The steps, ranked in the open',
             ['Law came first, and the court road closed in 1873.',
              'Money came second, and the one road left went unfunded.',
              'Violence came third, through the opening, in daylight.',
              'The act of 1875 was passed, and not enforced.'],
             N[24], kick='Synthesis · The lesson question', size=24)
# 25 VOCAB A
vocab('The pardon, the revolt, the panic, the league',
      [('Amnesty Act of 1872', 'the law of May 1872'),
       ('Liberal Republicans', 'the reform Republicans who broke with Grant in 1872'),
       ('Panic of 1873', 'the financial collapse that opened in September 1873'),
       ('White League', 'the paramilitary organization formed in Louisiana in 1874')],
      N[25])
# 26 VOCAB B
vocab('The case, the act, the cartoonist',
      [('Slaughter-House Cases', "the Supreme Court's 5 to 4 decision of April 1873"),
       ('Civil Rights Act of 1875', "Charles Sumner's last cause, enacted in March 1875"),
       ('Thomas Nast', "the Harper's Weekly cartoonist")],
      N[26])
# 27 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'The retreat in five records', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ["For each record, state which pillar of the settlement it raised or struck. Then rank the retreat's causes, law, money, violence, and weariness, and defend your ranking from the documents."],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Retreat in Five Records: the syllabus, the platform, the speech, the act, the cartoon'),
        ('Notebook', 'Notebook page: six pieces of the retreat, classified and evidenced'),
        ('Quick check', 'Two Citizenships: the syllabus read against its background'),
        ('Writing', 'Ranking the Retreat: the four causes ordered and defended')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, "Exit ticket: the ruling stated, the panic and the elections explained together, and the lesson question answered with one step of each kind.",
     size=15, color=POWDER)
notes(s, N[27])

for i, n in N.items():
    print(i, len(n.split()))
dc.save(OUT)
