#!/usr/bin/env python3
"""Reconstruction Lesson 3 deck builder. Image led deck: Johnson title, Stevens, Sumner, Waud First Vote, Stanton portraits."""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
LESSON_DIR = os.path.dirname(HERE)
UNIT_DIR = os.path.dirname(LESSON_DIR)
sys.path.insert(0, UNIT_DIR)
sys.path.insert(0, HERE)
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags, photo_right,
                         divider_photo, content_photo, content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED, W, H)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches
from notes_text import NOTES

dc.IMG = os.path.join(HERE, 'img')
OUT = os.path.join(LESSON_DIR, 'lesson-03-slides.pptx')

spec = open(os.path.join(UNIT_DIR, 'build-scripts', 'unit-spec.md')).read()
sec = spec.split('### Lesson 3')[1].split('### Lesson 4')[0]
TERMS = []
for line in sec.splitlines():
    line = line.strip()
    if line.startswith('- '):
        t, d = line[2:].split(': ', 1)
        TERMS.append((t.strip(), d.strip()))
assert len(TERMS) == 7, TERMS
TD = dict(TERMS)
def joined(term): return f"{term}: {TD[term]}"
def N(i):
    t = NOTES[i]
    for term in TD:
        t = t.replace("{J:" + term + "}", joined(term))
    assert "{J:" not in t, (i, t)
    return t

def vocab(title, terms, note, kick='The vocabulary'):
    s = slide(CREAM)
    kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95, 11.5, 1.0, title, size=30, color=NAVY, font='Georgia')
    n = len(terms); step = 1.52 if n <= 3 else 1.08
    yy = 2.1
    for term, dfn in terms:
        text(s, 0.9, yy, 4.1, 0.9, term, size=23 if n <= 3 else 21, color=NAVY, font='Georgia')
        text(s, 5.15, yy + 0.06, 7.3, 1.1, dfn, size=18 if n <= 3 else 15, color=MUTED, leading=1.2)
        yy += step
    notes(s, note)
    return s

SHORT = {
 'Fourteenth Amendment': "Congress's 1866 amendment: birthright citizenship, and no state to abridge privileges or immunities, due process, or equal protection",
 'Reconstruction Acts': "the March 1867 laws: ten governments set aside, five military districts, readmission on Congress's terms",
 'military districts': "the five command zones over the ten unreconstructed states, each under a Union general",
 'Joint Committee on Reconstruction': "the fifteen member committee of 1865 and 1866 whose testimony built the case for congressional terms",
 'Tenure of Office Act': "the March 1867 law barring removal of Senate confirmed officials without the Senate's consent",
 'Edwin M. Stanton': "Lincoln's secretary of war, whose removal in February 1868 triggered the impeachment",
 'impeachment': "the House charges and the Senate tries; Johnson's conviction vote fell one short in 1868",
}
LQ = "How did Congress rewrite the Constitution and the South's governments between 1866 and 1868, and at what cost?"
UQ = 'What did Reconstruction settle about freedom, citizenship, and the federal Union, and what did it leave open?'

def content_photo_s(img, title, items, note, kick=None, size=21):
    s = slide(CREAM)
    if kick: kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95 if kick else 0.8, 7.0, 1.0, title, size=30, color=NAVY, font='Georgia')
    photo_right(s, img)
    frags(s, items, y=2.35, w=6.9, size=size)
    notes(s, note)
    return s

# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY); rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'RECONSTRUCTION \u00b7 LESSON 3', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Congress Takes Charge', size=34, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'An amendment refused, ten governments rebuilt, and a president tried by one vote.', size=17, color=POWDER)
notes(s, N(1))
# 2 QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[(LQ, {})]], size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': RUST_LT, 'italic': True}), (UQ, {'italic': True})]], size=17, color=POWDER, font='Georgia', leading=1.2)
notes(s, N(2))
# 3 MAP
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'A committee, an amendment, an army of paper, a trial', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The Committee Hears the South', 'Fifteen members take the South\u2019s testimony'),
        ('B', 'Section 1: Citizenship Defined', 'Birthright citizenship written into the Constitution'),
        ('C', "The Amendment's Machinery and the Refusal", 'Tennessee returns; ten states refuse'),
        ('D', 'Violence and the Elections of 1866', 'Memphis, New Orleans, and a veto proof Congress'),
        ('E', 'The Reconstruction Acts', 'Five districts and a new electorate'),
        ('F', 'The Collision Over Stanton', 'A tenure law and a removal'),
        ('G', 'Impeachment, Acquittal, and the Summer of 1868', 'One vote short, and seven states back')]
yy = 2.62
for letter, head, sub in rows:
    text(s, 0.92, yy, 0.5, 0.5, letter, size=20, color=RUST_LT, font='Georgia', bold=True)
    text(s, 1.45, yy, 6.6, 0.5, head, size=19, color=CREAM, font='Georgia')
    text(s, 8.2, yy + 0.03, 4.3, 0.5, sub, size=15, color=POWDER)
    yy += 0.62
notes(s, N(3))
# 4 DIVIDER A
divider_photo('stevens-port.jpg', 'Section A', 'The Committee Hears the South', ['Congress refuses the delegations, and builds a committee to hear the South itself.'], N(4))
# 5 A CONTENT
content_photo_s('stevens-port.jpg', 'Testimony and two conclusions', ['Congress refused to seat the restored delegations.', 'Governors, generals, planters, and freedpeople testified.', 'The old order survived in statute and in practice.', 'The states had no claim to representation until Congress set the terms.'], N(5), kick='Section A', size=21)
# 6 STAT 15
stat('15', 'members of the Joint Committee on Reconstruction', 'Nine representatives and six senators, hearing the South through the winter and spring of 1866 and drafting the Fourteenth Amendment.', N(6), kick='Section A')
# 7 DIVIDER B
divider_photo('stevens-port.jpg', 'Section B', 'Section 1: Citizenship Defined', ['June 1866: the committee\u2019s amendment goes to the states.'], N(7))
# 8 B CONTENT
content_text('Born or naturalized', ['All persons born or naturalized in the United States are citizens.', 'They were citizens of the nation and of their state at once.', "Dred Scott's exclusion was overturned in the text.", 'Citizenship was placed beyond any legislature\u2019s repeal.'], N(8), kick='Section B')
# 9 B CONTENT PHOTO SUMNER
content_photo_s('sumner-port.jpg', 'Three bindings on the states', ["No state shall abridge citizens' privileges or immunities.", 'No person shall be deprived of life, liberty, or property without due process.', 'No person shall be denied the equal protection of the laws.', 'The first clause speaks to citizens, and the other two speak to any person.'], N(9), kick='Section B', size=21)
# 10 VOCAB 1
vocab('Words for the amendment and its author', [(t, SHORT[t]) for t in ['Fourteenth Amendment', 'Joint Committee on Reconstruction', 'Reconstruction Acts']], N(10))
# 11 DIVIDER C
divider_text('Section C', "The Amendment's Machinery and the Refusal", 'Representation priced, leaders disabled, debts settled, and ten states say no.', N(11))
# 12 C CONTENT
content_text('Machinery, then refusal', ['Section 2 cut representation where male voters were denied the vote.', 'Section 3 barred leading former Confederates from office.', 'Section 4 honored the Union debt and voided Confederate debts.', 'Tennessee ratified the amendment and returned, and the other ten states refused it.'], N(12), kick='Section C')
# 13 DIVIDER D
divider_text('Section D', 'Violence and the Elections of 1866', 'Two attacks stated plainly, and a Congress returned able to govern over a veto.', N(13))
# 14 D CONTENT
content_text('Memphis and New Orleans', ['In Memphis in May 1866, mobs and police attacked Black residents.', 'The attacks killed 46 people, and schools and churches were burned.', 'In New Orleans in July 1866, police attacked a Unionist convention.', 'More than 30 people were killed, and neither city offered local protection.'], N(14), kick='Section D')
# 15 D CONTENT 2
content_text('The elections of 1866', ['Congressional investigations printed the testimony.', 'Northern newspapers carried the reports into the campaign.', 'Republicans held more than two thirds of both houses.', 'Two thirds was the number that could override a veto.'], N(15), kick='Section D')
# 16 DIVIDER E
divider_photo('firstvote-port.jpg', 'Section E', 'The Reconstruction Acts', ['March 1867: the amendment plus new governments, under generals until the work is done.'], N(16))
# 17 E CONTENT
content_text('The Acts at working level', ['The ten governments were declared provisional.', 'Five military districts stood under Union generals.', 'Registration came first and built an electorate that included Black men.', "Return was priced at new constitutions, ratification, and Congress's approval."], N(17), kick='Section E')
# 18 E CONTENT PHOTO FIRST VOTE
content_photo_s('firstvote-port.jpg', 'The electorate the Acts created', ['The rolls opened to adult male citizens of a year\u2019s residence, Black and white.', 'Leading former Confederates were barred from the rolls.', 'Conventions were elected to write new constitutions.', "Waud's First Vote showed the new electorate at the polls in 1867."], N(18), kick='Section E', size=21)
# 19 STAT 700000
stat('700,000', 'Black voters entered on the rolls', 'Registered under the Reconstruction Acts in 1867, the electorate that chose the conventions and ratified the amendment.', N(19), kick='Section E')
# 20 DIVIDER F
divider_photo('stanton-port.jpg', 'Section F', 'The Collision Over Stanton', ['A tenure law, a guarded chair, and a removal in defiance of both.'], N(20))
# 21 F CONTENT PHOTO STANTON
content_photo_s('stanton-port.jpg', 'The Tenure of Office Act', ['The act passed on March 2, 1867, over Johnson\u2019s veto.', "The act barred removal of a Senate-confirmed official without the Senate's consent.", 'Stanton held the War Department, and the districts with it.', 'A removal without consent was void under the act.'], N(21), kick='Section F', size=21)
# 22 F CONTENT
content_text('February 21, 1868', ['Stanton was suspended in August 1867, during the recess.', 'The Senate refused to concur in January 1868, and Stanton resumed his office.', 'Johnson removed him outright and named Lorenzo Thomas.', 'Stanton held his office, and the House had its dated act.'], N(22), kick='Section F')
# 23 DIVIDER G
divider_photo('johnson-port.jpg', 'Section G', 'Impeachment, Acquittal, and the Summer of 1868', ['Eleven articles, a spring trial, and a settlement that survives its builder\u2019s enemy.'], N(23))
# 24 G CONTENT
content_text('The trial', ['The House impeached Johnson on February 24, 1868, and eleven articles followed.', 'Article I charged the Stanton removal itself.', 'The Senate tried the charges, with the Chief Justice presiding.', 'Seven Republicans broke with their party on the doubts.'], N(24), kick='Section G')
# 25 STAT 1
stat('1', 'vote short of conviction', 'The Senate voted 35 to convict and 19 to acquit on May 16, 1868, one short of the two thirds the Constitution requires.', N(25), kick='Section G')
# 26 VOCAB 2
vocab('Words for the machinery and the crisis', [(t, SHORT[t]) for t in ['military districts', 'Tenure of Office Act', 'Edwin M. Stanton', 'impeachment']], N(26))
# 27 GLANCE
content_text('The lesson at a glance', ['Testimony became a constitutional text.', 'The text was refused, and violence returned a veto proof Congress.', 'Ten governments were rebuilt on 700,000 new Black voters.', 'A removal and a trial ended in acquittal by one vote.', 'By the summer of 1868, the amendment was ratified and seven states were back.'], N(27), kick='Synthesis')
# 28 ANSWERING
content_text('Answering the question', ['Take a position: conqueror, constitution maker, or both.', 'Test your position against the refusal, the districts, and the trial.', 'Quote Station 1 and Station 4, the amendment and the article.', 'End on what the settlement rested on and what it cost.'], N(28), kick='Synthesis')
# 29 EXIT
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.7, 11.5, 2.2, 'Answer the question, and exit', size=44, color=CREAM, font='Georgia', leading=1.1)
rule(s, 0.92, 3.5)
text(s, 0.9, 3.85, 11.0, 2.6, ['Exit ticket: the three questions at the end of your guided notes.', 'Writing task: judge Congress\u2019s power from the amendment and two of its tests.'], size=22, color=POWDER, space_after=10, leading=1.3)
notes(s, N(29))

heads = {1:'Opening frame',2:'The lesson question',3:'The lesson in one slide',4:'Section A: The Committee Hears the South (divider)',5:'Testimony and two conclusions',6:'15 members of the Joint Committee',7:'Section B: Section 1, Citizenship Defined (divider)',8:'Born or naturalized',9:'Three bindings on the states',10:'Vocabulary: words for the amendment and its author',11:"Section C: The Amendment's Machinery and the Refusal (divider)",12:'Machinery, then refusal',13:'Section D: Violence and the Elections of 1866 (divider)',14:'Memphis and New Orleans',15:'The elections of 1866',16:'Section E: The Reconstruction Acts (divider)',17:'The Acts at working level',18:'The electorate the Acts created',19:'700,000 Black voters entered on the rolls',20:'Section F: The Collision Over Stanton (divider)',21:'The Tenure of Office Act',22:'February 21, 1868',23:'Section G: Impeachment, Acquittal, and the Summer of 1868 (divider)',24:'The trial',25:'One vote short of conviction',26:'Vocabulary: words for the machinery and the crisis',27:'The lesson at a glance',28:'Answering the question',29:'Now your turn: answer the question and exit ticket'}
json.dump({str(k): v for k, v in heads.items()}, open(os.path.join(HERE, 'headings.json'), 'w'), indent=1, sort_keys=True)
dc.save(OUT)
from pptx import Presentation
prs2 = Presentation(OUT)
counts = []
for i, sl in enumerate(prs2.slides, 1):
    t = sl.notes_slide.notes_text_frame.text if sl.has_notes_slide else ''
    counts.append(len(t.split()))
print('slides:', len(prs2.slides.__iter__.__self__._sldIdLst))
print('notes counts:', counts)
print('notes range:', min(counts), max(counts), 'total:', sum(counts))
missing = [t for t, _ in TERMS if not any((t + ': ' + TD[t]) in (sl.notes_slide.notes_text_frame.text if sl.has_notes_slide else '') for sl in prs2.slides)]
print('terms missing verbatim joined in notes:', missing)
