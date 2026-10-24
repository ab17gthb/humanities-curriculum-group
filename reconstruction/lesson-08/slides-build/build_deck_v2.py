#!/usr/bin/env python3
"""Reconstruction Lesson 8 deck, "1876 and the End," built to the approved
system: image-led slides, fragments only on screen, comprehensive speaker
notes, full lesson and vocabulary coverage. Speaker notes live in
notes_text.py, with the spec's definitions inserted verbatim."""
import os, sys, re
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
OUT = os.path.join(HERE, '..', 'lesson-08-slides.pptx')

SPEC = open(os.path.join(HERE, '..', '..', 'build-scripts', 'unit-spec.md')).read()
sec = SPEC.split('### Lesson 8 (blueprint 15)')[1]
DEFS = []
for line in sec.splitlines():
    m = re.match(r'- (.+?): (.+)', line.strip())
    if m: DEFS.append((m.group(1), m.group(2).strip()))
DEFS = DEFS[:7]
D = dict(DEFS)
def joined(term): return term + ': ' + D[term]

N = {}
for k, v in NOTES.items():
    v = v.replace('__HAYES2__', joined('Rutherford B. Hayes')).replace('__HAYES__', joined('Rutherford B. Hayes'))
    v = v.replace('__TILDEN2__', joined('Samuel J. Tilden')).replace('__TILDEN__', joined('Samuel J. Tilden'))
    v = v.replace('__COMMISSION2__', joined('Electoral Commission')).replace('__COMMISSION__', joined('Electoral Commission'))
    v = v.replace('__COMPROMISE2__', joined('Compromise of 1877')).replace('__COMPROMISE__', joined('Compromise of 1877'))
    v = v.replace('__REDEEMERS2__', joined('Redeemers')).replace('__REDEEMERS__', joined('Redeemers'))
    v = v.replace('__HOMERULE2__', joined('home rule')).replace('__HOMERULE__', joined('home rule'))
    v = v.replace('__REDEMPTION2__', joined('Redemption')).replace('__REDEMPTION__', joined('Redemption'))
    N[k] = v

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

LQ = 'What did Reconstruction settle, and what did its ending leave open?'
EQ = 'What did Reconstruction settle about freedom, citizenship, and the federal Union, and what did it leave open?'

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
text(s, 0.9, 5.32, 11.5, 0.4, 'RECONSTRUCTION · LESSON 8', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, '1876 and the End', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'What Reconstruction settled, and what its ending left open', size=17, color=POWDER)
text(s, 0.9, 7.02, 11.9, 0.4, 'Counting the electoral vote, 1877. Wood engraving. Library of Congress.', size=11, color=POWDER)
notes(s, N[1])

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[(LQ, {})]], size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                (EQ, {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, N[2])

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'An election, a count, a bargain, an audit', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The election of 1876', "Tilden's majority, and twenty disputed votes"),
        ('B', 'The disputed returns', 'Terror behind the returns, two sets of certificates'),
        ('C', 'The Electoral Commission', 'Fifteen members, and eight to seven'),
        ('D', 'The bargain of 1877', 'A cabinet seat, improvements, the troops'),
        ('E', 'April 1877', 'Columbia and New Orleans, and the Redeemers'),
        ('F', 'The settled account', 'Three amendments, standing in the text'),
        ('G', 'What was left open', 'Land, protection, and enforcement')]
yy = 2.66
for n_, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n_, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, N[3])

# 4 A DIVIDER
divider_text('Section A', 'The Election of 1876',
             'Two reform governors, and a vote the South contested before it was counted.', N[4])

# 5 A CONTENT HAYES
content_photo_s('hayes-port.jpg', 'The governor and the general',
             ['Rutherford B. Hayes came from Ohio.',
              'He served as a Union general and three times as governor of Ohio.',
              'He was the Republican nominee in 1876.'],
             N[5], kick='A · The election of 1876')

# 6 A CONTENT TILDEN
content_photo_s('tilden-port.jpg', "The prosecutor of the Tweed Ring",
             ['Samuel J. Tilden came from New York.',
              'He was the Democratic nominee in 1876.',
              'He won a majority of the popular vote.'],
             N[6], kick='A · The election of 1876')

# 7 STAT
stat('250,000', 'votes, Tilden\'s popular majority, by the usual figure',
     'The election of 1876: a majority that elected no one', N[7], kick='A · The election of 1876')

# 8 B DIVIDER
divider_text('Section B', 'The Disputed Returns',
             'Twenty electoral votes, from elections that had not been free.', N[8])

# 9 B CONTENT FROST
content_text("Frost's arithmetic, October 1876",
             ['Harper\'s Weekly published it on October 21, 1876.',
              'A voter stood at a southern polling place.',
              'Pistols were held to his head, with an order to say he was free.',
              'It is taught by description, as the bank presents it.'],
             N[9], kick='B · The disputed returns', size=24)

# 10 B CONTENT RETURNS
content_text('Two governments, two sets of returns',
             ['Florida, Louisiana, South Carolina, and Oregon sent disputed returns.',
              'Republican boards certified Hayes electors.',
              'Democratic claimants certified Tilden electors.',
              'Twenty electoral votes stood in dispute.'],
             N[10], kick='B · The disputed returns', size=24)

# 11 C DIVIDER
divider_photo('commission-port.jpg', 'Section C', 'The Electoral Commission',
              ['Counting the electoral vote, 1877.', 'Wood engraving. Library of Congress.'], N[11])

# 12 C CONTENT
content_text('Fifteen members, one expected balance',
             ['Five senators, five representatives, and five justices made fifteen members.',
              'Justice Davis was expected to hold the balance.',
              'Illinois sent Davis to the Senate.',
              'Every ruling went eight to seven for Hayes.'],
             N[12], kick='C · The Electoral Commission', size=24)

# 13 STAT
stat('185 to 184', 'the electoral count, a majority of one vote',
     'Every disputed vote awarded to Hayes, February and March 1877', N[13], kick='C · The Electoral Commission')

# 14 D DIVIDER
divider_text('Section D', 'The Bargain of 1877',
             'The count finished, at a price named in assurances.', N[14])

# 15 D CONTENT TERMS
content_text('The Wormley House terms',
             ['The Democrats let the count finish.',
              'A cabinet seat went to a southerner.',
              'Federal support was pledged for southern internal improvements.',
              'The last troops were withdrawn.'],
             N[15], kick='D · The bargain of 1877', size=24)

# 16 D CONTENT INAUGURAL
content_photo_s('hayes-port.jpg', 'The public face, March 5, 1877',
             ["The inaugural address was the bargain's public face.",
              'Complete protection of all citizens was pledged.',
              'Honest local self-government was promised.',
              'The troops were not named.'],
             N[16], kick='D · The bargain of 1877')

# 17 E DIVIDER
divider_text('Section E', 'April 1877: The Troops Withdraw',
             'Two garrisons recalled, and the last governments fall.', N[17])

# 18 E CONTENT CAPITALS
content_text('Columbia, then New Orleans',
             ['The troops at the Columbia statehouse were recalled.',
              'Chamberlain yielded to Hampton.',
              'The New Orleans troops were withdrawn days later.',
              'No Reconstruction government remained.'],
             N[18], kick='E · April 1877', size=24)

# 19 E CONTENT REDEEMERS
content_text('Redemption and home rule',
             ['The Redeemers held every southern state.',
              'They governed for low taxes, cheap government, and retrenched schools.',
              'The vote remained in law, and its protection was gone.'],
             N[19], kick='E · April 1877', size=24)

# 20 F DIVIDER
divider_text('Section F', 'The Audit: What the Settlement Settled',
             'Unenforced is not unsettled: the text stood.', N[20])

# 21 F CONTENT
content_text('Settled, in the text',
             ['Slavery was abolished, and Congress was armed to enforce it.',
              'Citizenship came by birth, with due process and equal protection.',
              'The vote was protected against racial denial.',
              'No settlement of 1877 repealed any of it.'],
             N[21], kick='F · The settled account', size=24)

# 22 G DIVIDER
divider_text('Section G', 'What Was Left Open',
             'Land, protection, and enforcement, left where 1877 left them.', N[22])

# 23 G CONTENT
content_text('The open account',
             ['Land was never redistributed.',
              'Protection was withdrawn with the troops.',
              'Schools and governments passed under hostile rule.',
              'Enforcement clauses stood, unused.'],
             N[23], kick='G · What was left open', size=24)

# 24 VOCAB A
vocab('Words for the bargain',
      [('Compromise of 1877', 'the bargain that settled 1876'),
       ('Rutherford B. Hayes', 'the president it seated')], N[24])

# 25 VOCAB B
vocab('Words for the count',
      [('Samuel J. Tilden', 'winner of the popular vote'),
       ('Electoral Commission', 'fifteen members, eight to seven')], N[25])

# 26 VOCAB C
vocab('Words for the new order',
      [('Redeemers', 'the leaders who retook the South'),
       ('home rule', 'the slogan of the return'),
       ('Redemption', 'the name they gave it')], N[26])

# 27 SYNTHESIS
s = slide(NAVY)
kicker(s, 'The settlement at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Count, bargain, settled, open', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Count', 'The election and the commission', '185 to 184, on eight to seven rulings'),
        ('Bargain', 'Wormley House, February 1877', 'A seat, improvements, and the troops'),
        ('Withdrawal', 'April 1877', 'Columbia and New Orleans; the last governments fall'),
        ('Settled', 'The three amendments', 'Abolition, citizenship, the vote, in the text'),
        ('Open', 'The other column', 'Land, protection, and enforcement')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, N[27])

# 28 EXIT
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Audit the settlement', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['What did Reconstruction settle, and what did its ending leave open? Work the five records in order, then judge whether 1877 ended Reconstruction or only its enforcement.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Settlement Audited: the three amendments, Frost, and the inaugural summary'),
        ('Notebook', 'Notebook page: the count, the bargain, and both columns of the audit'),
        ('Quick check', 'Settled in Text: the Thirteenth Amendment read against Frost\'s voter'),
        ('Writing', 'Ended, or Only Stood Down: the claim of 1877 judged from the bank')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the two results of 1876, the bargain\'s three assurances, and the lesson question answered from both columns.',
     size=15, color=POWDER)
notes(s, N[28])

dc.save(OUT)

from pptx import Presentation
prs2 = Presentation(OUT)
counts = []
for i, sl in enumerate(prs2.slides, 1):
    t = sl.notes_slide.notes_text_frame.text if sl.has_notes_slide else ""
    counts.append(len(t.split()))
print("slides:", len(counts), "notes min:", min(counts), "max:", max(counts), "total:", sum(counts))
print(counts)
allnotes = " ".join(sl.notes_slide.notes_text_frame.text for sl in prs2.slides)
for term, dfn in DEFS:
    print(term, "VERBATIM" if (term + ': ' + dfn) in allnotes else "MISSING")
