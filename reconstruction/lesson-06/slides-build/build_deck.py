#!/usr/bin/env python3
"""Reconstruction Lesson 6 deck, The Counterrevolution: The Klan and the
Enforcement Acts, built to the approved system: image-led slides, fragments
only on screen, comprehensive speaker notes, full lesson and vocabulary
coverage. Fonts: Georgia titles, Lato body. Speaker notes live in
notes_text.py. Image discipline: portraits and government buildings only;
no image of the Klan, of riders, of victims, or of violence anywhere."""
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
OUT = os.path.join(HERE, '..', 'lesson-06-slides.pptx')
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
text(s, 0.9, 5.32, 11.5, 0.4, 'RECONSTRUCTION \u00b7 LESSON 6', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Counterrevolution', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'The Klan\u2019s terror, the testimony against it, and the federal answer of 1870 and 1871', size=17, color=POWDER)
notes(s, N[1])

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("What did the Klan\u2019s terror aim at, and what did it take to break the first Klan?", {})]],
     size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ("What did Reconstruction settle about freedom, citizenship, and the federal Union, and what did it leave open?", {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, N[2])

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Terror organized, testimony given, law answered', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'Terror organized as politics', 'Pulaski 1866; the Invisible Empire, 1867; Forrest'),
        ('B', 'Night riding and its targets', 'Voters, organizers, teachers, officeholders'),
        ('C', 'Abram Colby tells Congress', 'The offers, the attack of 1869, the testimony of 1872'),
        ('D', 'Forrest: dissolution and denial', 'The order of 1869; the denials of 1871'),
        ('E', 'Congress arms the federal government', 'Three Enforcement Acts, 1870 and 1871'),
        ('F', 'The Klan Act and South Carolina', 'April 1871; the proclamation; nine counties'),
        ('G', 'Broken, and what it depended on', 'Broken by 1872; resting on a northern will')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, N[3])

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', 'Terror Organized as Politics',
             'Founded at Pulaski in 1866 and organized as the Invisible Empire in 1867, with disguise as its first instrument.',
             N[4])

# ------------------------------------------------------ 5 THE ORGANIZATION
content_text('A club becomes an empire',
             ['Six former Confederate soldiers, Pulaski, 1866',
              'Nashville, 1867: the Invisible Empire',
              'Dens, rituals, and officers under borrowed titles',
              'Forrest elected the first Grand Wizard',
              'The disguise hides the man, and defeats the law'],
             N[5], kick='A \u00b7 Terror organized as politics', size=24)

# ------------------------------------------------- 6 SECTION B DIVIDER
divider_text('Section B', 'Night Riding and Its Targets',
             'The method taught in testimony and text, stated plainly. No image of the riders or their work appears in this lesson.',
             N[6])

# ------------------------------------------------------ 7 THE METHOD
content_text('The method and the message',
             ['Mounted men in disguises, after dark',
              'Targets called out by name, at their houses',
              'Black voters and Republican organizers first',
              'Teachers, officeholders, and their allies',
              'One whipping, addressed to a whole community'],
             N[7], kick='B \u00b7 Night riding and its targets', size=24)

# ------------------------------------------------------ 8 STAT 3
stat('3', 'appointments the raids kept',
     'Before elections \u00b7 at the opening of school terms \u00b7 at contract settlements',
     N[8], kick='B \u00b7 Night riding and its targets')

# ------------------------------------------------- 9 SECTION C DIVIDER
divider_text('Section C', 'Abram Colby Tells Congress',
             'A Georgia legislator, whipped in 1869 for refusing to sell his seat, carries the account to Congress in 1872.',
             N[9])

# ------------------------------------------------------ 10 THE OFFERS AND THE ATTACK
content_text('Purchase first, violence second',
             ['$5,000 to change sides; $2,500 for his seat',
              'Refused at both prices, in his own words',
              'October 29, 1869: the door broken open',
              'Three hours in the woods, left for dead',
              'Under the whipping: the Radical ticket, tomorrow'],
             N[10], kick='C \u00b7 Abram Colby tells Congress', size=24)

# ------------------------------------------------------ 11 THE TESTIMONY
content_text('1872: the refusal goes on the record',
             ['A congressional committee hears the account',
              'Attackers named by standing: lawyer, doctor, farmers',
              'First class men of the town, in disguise',
              'No free speech in his county, or in Georgia',
              'Testimony becomes the acts\u2019 foundation'],
             N[11], kick='C \u00b7 Abram Colby tells Congress', size=24)

# ------------------------------------------------- 12 SECTION D DIVIDER
divider_photo('forrest-port.jpg', 'Section D', 'Forrest: Dissolution and Denial',
              ['The Grand Wizard who ordered the Klan dissolved', 'in 1869, and denied directing it in 1871.'],
              N[12], title_size=34)

# ------------------------------------------------------ 13 THE ACCOUNT WEIGHED
content_text('Admissions and denials',
             ['Elected Grand Wizard, 1867, by his own account',
              'January 1869: the organization ordered dissolved',
              'Its violence, he said, had escaped his control',
              '1871: no direction given, no policy known',
              'The committee weighed the man against the record'],
             N[13], kick='D \u00b7 Forrest: dissolution and denial', size=24)

# ------------------------------------------------- 14 SECTION E DIVIDER
divider_text('Section E', 'Congress Arms the Federal Government',
             'Three Enforcement Acts, 1870 and 1871: rights given officers, courts, and a reach past the states.',
             N[14])

# ------------------------------------------------------ 15 THE MACHINERY
content_text('Law built for the emergency',
             ['Conspiracy against constitutional rights, a federal crime',
              'The disguised rider named in the statute',
              'Federal supervisors at the polls',
              'Marshals to guard, arrest, and summon posses',
              'Cases moved to federal court'],
             N[15], kick='E \u00b7 Congress arms the federal government', size=24)

# ------------------------------------------------------ 16 TWO OFFICERS
content_text('Supervisors watch; marshals act',
             ['Supervisors: registration, polling, the count',
              'Marshals: guards, arrests, and posses',
              'Each officer answers a named local failure',
              'Sheriffs who would not arrest; juries who would not convict',
              'Federal authority, standing in the county'],
             N[16], kick='E \u00b7 Congress arms the federal government', size=24)

# ------------------------------------------------- 17 SECTION F DIVIDER
divider_photo('grant-port.jpg', 'Section F', 'The Klan Act and South Carolina',
              ['The act of April 1871, used at full strength', 'in nine South Carolina counties that fall.'],
              N[17], title_size=34)

# ------------------------------------------------------ 18 TWO REACHES
content_text('One act, two reaches',
             ['Under color of state law, a federal offense',
              'Section 1: the injured party sues in federal court',
              'The president may use the army',
              'Combinations may be proclaimed insurrection',
              'A rights statute with a campaign inside it'],
             N[18], kick='F \u00b7 The Klan Act and South Carolina', size=24)

# ------------------------------------------------------ 19 THE CAMPAIGN
content_text('South Carolina, October 1871 to 1872',
             ['Proclamation, October 17, 1871: disperse',
              'Habeas corpus suspended in nine counties',
              'Marshals and troops: hundreds arrested',
              'Hundreds indicted; pleas, convictions, flight',
              'By 1872, the first Klan there was broken'],
             N[19], kick='F \u00b7 The Klan Act and South Carolina', size=24)

# ------------------------------------------------------ 20 STAT 9
stat('9', 'counties under the proclamation',
     'Spartanburg \u00b7 York \u00b7 Union \u00b7 Chester \u00b7 Laurens \u00b7 Newberry \u00b7 Fairfield \u00b7 Lancaster \u00b7 Chesterfield',
     N[20], kick='F \u00b7 The Klan Act and South Carolina')

# ------------------------------------------------- 21 SECTION G DIVIDER
divider_text('Section G', 'Broken, and What the Breaking Depended On',
             'Federal power, used whole, worked. The power rested on a will the statute could not supply.',
             N[21])

# ------------------------------------------------------ 22 THE LEDGER
content_text('Capacity, and dependence',
             ['Marshals, troops, prosecutors, courts, together',
              'The Invisible Empire collapsed within a year',
              'The proof: the first Klan was breakable, and broken',
              'The premise: a president, a Congress, a public',
              'The method survived, and changed its clothes'],
             N[22], kick='G \u00b7 Broken, and what it depended on', size=24)

# ------------------------------------------------------ 23 AT A GLANCE
s = slide(NAVY)
kicker(s, 'Terror and answer at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'An organization, a method, a testimony, an answer', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The organization', 'Pulaski 1866; the Empire, 1867', 'Forrest its Grand Wizard; dissolved by his order, 1869'),
        ('The method', 'Night riding, timed and targeted', 'Elections, school terms, contract settlements'),
        ('The testimony', 'Colby to Congress, 1872', 'The sums refused; the respectable men named'),
        ('The answer', 'Three acts; the Klan Act, April 1871', 'Nine counties, 1871; the first Klan broken, 1872')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.2, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.25, yy + 0.05, 5.1, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.55, yy + 0.05, 3.9, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, N[23])

# ------------------------------------------------------ 24 VOCAB A
vocab('Words for the organization and its chief',
      [('Ku Klux Klan', 'the Invisible Empire, from 1866'),
       ('Nathan Bedford Forrest', 'its first Grand Wizard, 1867')],
      N[24])

# ------------------------------------------------------ 25 VOCAB B
vocab('Words for the testimony and the method',
      [('Abram Colby', 'the legislator who refused, and testified'),
       ('night riding', 'the Klan\u2019s characteristic method')],
      N[25])

# ------------------------------------------------------ 26 VOCAB C
vocab('Words for the federal answer',
      [('Enforcement Acts', 'the three laws of 1870 and 1871'),
       ('Ku Klux Klan Act', 'the third act, April 1871'),
       ('federal marshals', 'the settlement\u2019s enforcement arm')],
      N[26])

# ------------------------------------------------------ 27 CLOSING SYNTHESIS
s = slide(NAVY)
kicker(s, 'Closing synthesis')
text(s, 0.9, 1.35, 11.5, 1.1, 'Two findings, held together', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 2.6,
     ["The terror aimed at the electorate the Reconstruction Acts had made, and it was broken, where the federal government used its full power, within a year.",
      "The breaking rested on a president, a Congress, and a northern public willing to sustain it. The statute supplied the machinery. It could not supply the will."],
     size=23, color=POWDER, leading=1.3)
notes(s, N[27])

# ------------------------------------------------------ 28 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ["What did the Klan\u2019s terror aim at, and what did it take to break the first Klan? Judge the testimony and the statute, and state what the answer depended on."],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'Testimony and Answer: the testimony, the statute, three summaries, a verdict'),
        ('Notebook', 'Notebook page: the organization, the method, the testimony, the answer'),
        ('Quick check', 'Testimony and Statute: the two quoted records tested against each other'),
        ('Writing', 'Civil Rights Law, Counterinsurgency, or Both: your verdict defended from the bank')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: night riding and the acts defined, the aim in two sentences, and the lesson question answered.',
     size=15, color=POWDER)
notes(s, N[28])

dc.save(OUT)
