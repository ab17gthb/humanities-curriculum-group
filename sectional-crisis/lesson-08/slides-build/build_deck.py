#!/usr/bin/env python3
"""Sectional Crisis and Civil War Lesson 8 deck, "Total War and Appomattox,"
built to the approved system: image-led slides, fragments only on screen,
comprehensive speaker notes, full lesson + vocabulary coverage."""
import os, sys, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags, photo_right,
                         divider_photo, content_photo, content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED, W, H)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

dc.IMG = os.path.join(HERE, 'img')
OUT = os.path.join(HERE, '..', 'lesson-08-slides.pptx')

SPEC = open(os.path.join(HERE, '..', '..', 'build-scripts', 'unit-spec.md')).read()
sec = SPEC.split('### Lesson 8 (blueprint 15)')[1]
DEFS = []
for line in sec.splitlines():
    m = re.match(r'- (.+?): (.+)', line.strip())
    if m:
        DEFS.append((m.group(1), m.group(2).strip()))
DEFS = DEFS[:7]
D = dict(DEFS)
def joined(term):
    return term + ': ' + D[term]

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

LQ = 'How did the war end, and what did its ending settle?'
EQ = 'How did compromise over slavery finally fail, and what did the war it caused settle about slavery and the Union, and what did it leave open?'

# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'SECTIONAL CRISIS AND CIVIL WAR · LESSON 8', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Total War and Appomattox', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'How the war ended, and what its ending settled', size=17, color=POWDER)
text(s, 0.9, 7.02, 11.9, 0.4, 'The McLean house, Appomattox Court House, photographed by Timothy H. O\'Sullivan, April 1865. Library of Congress.', size=11, color=POWDER)
notes(s, "The image is the McLean house at Appomattox Court House, Virginia, photographed by Timothy H. O'Sullivan in April 1865, the month of the surrender that took place in its parlor. Open with the house rather than a battle scene, because this lesson is about an ending, not a battle. The unit closes here. Grant's coordinated campaigns of 1864 fixed the Confederate armies in place while Sherman destroyed the resources behind them, the North voted to finish the war, Congress and the petitioning women carried slavery's end into the Constitution, and on April 9, 1865, Lee surrendered in this house. Five days later Lincoln was dead. The lesson stops at April 1865, where the unit stops, with the freed people's future standing exactly where the war left it, unanswered on purpose.")

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[(LQ, {})]], size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                (EQ, {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "The question has two halves and the lesson grades both. The first half is mechanical: how did the war end? Not by one battle or one surrender paper, but by coordinated pressure applied for a year, an election that refused an armistice, and a retreat cut off at a Virginia crossroads village. The second half is the unit's closing argument: what did the ending settle? The Union's indivisibility and slavery's destruction, say the documents. What it left standing, the freed people's claims to land, safety, and the vote, is stated as plainly as what it settled, because the next unit opens exactly there. Keep both halves in view all hour. Every document in the lesson answers one of them, and the exit ticket grades both.")

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'The ending, in seven stretches', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'Grant takes command', 'Armies, not cities, and all at once'),
        ('B', 'Sherman and total war', 'Atlanta, the letter, the March to the Sea'),
        ('C', 'The election of 1864', 'An armistice on the ballot, and refused'),
        ('D', "The Union's other wartime work", 'Homesteads, colleges, petitions, an amendment'),
        ('E', 'Appomattox', 'Richmond falls, and a surrender in a parlor'),
        ('F', 'The verdict of the Second Inaugural', 'Slavery the offense, the war its woe'),
        ('G', 'April 1865, and what stood open', 'Assassination, and the unanswered claims')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A gives Grant command and his doctrine. Section B follows Sherman through Atlanta and Georgia. Section C puts the war to a vote in 1864. Section D reads the wartime work of Congress and of the women who petitioned. Section E ends the fighting at Appomattox. Section F reads Lincoln's verdict on the war's cause. Section G closes in April 1865, on the assassination and on the claims the war left unanswered. Students will meet this same map again on the synthesis slide near the end of the deck.")

# 4 A DIVIDER
divider_text('Section A', 'Grant Takes Command',
             'March 1864: the armies, not the cities, and all at once.',
             "Begin with the appointment, because the ending of the war was designed before it was fought. In March 1864 Lincoln made Grant general in chief of all Union armies, ending the war's long search for a commander who would use the whole strength of the Union at once. Grant's definition belongs to his section's teaching later in the deck, and the vocabulary slides carry it in full. His doctrine reversed the practice of his predecessors, who had chased capitals and fought one army at a time while the others rested. Grant would fight every Confederate army simultaneously, so no front could send help to another. He put his headquarters with the Army of the Potomac in Virginia, and sent Sherman west.")

# 5 A CONTENT 1
content_photo('grant-port.jpg', 'The general in chief',
             ['Command of all Union armies, March 1864',
              'The objective: the Confederate armies',
              'Every army to move at once',
              'Grant stays in Virginia; Sherman goes west'],
             "The image is Grant, from the Brady studio's wet collodion portrait, held by the Library of Congress. " + joined('Ulysses S. Grant') + " Teach the record as a qualification for the doctrine. Grant had won in the west by moving against armies and supply lines together, at Donelson on the rivers, at Vicksburg on the Mississippi, and at Chattanooga on the railroads. Lincoln's judgment in promoting him was that the man who had taken an army's surrender at Vicksburg would not stop at taking a city. Students should hold the sequence Fort Donelson, Shiloh, Vicksburg, Chattanooga as the argument Grant carried into Virginia in the spring of 1864.",
             kick='A · Grant takes command')

# 6 A CONTENT 2
content_text('The Overland ledger, and Petersburg',
             ['The Wilderness, Spotsylvania, Cold Harbor',
              'Some 65,000 Union casualties in six weeks, by the usual estimates',
              'Grant slides south after each battle',
              'Petersburg besieged, June 1864 to April 1865'],
             "Work the ledger plainly, because the cost is part of the doctrine's meaning. Grant fought Lee in May and June of 1864 in a near continuous battle, and the Union army paid casualty figures the country had never seen, by the usual estimates some sixty five thousand men in six weeks. Earlier commanders had retreated after such losses to refit. Grant slid around Lee's flank and kept going south, which is why the North's newspapers at first called him a butcher and then understood that the arithmetic had changed. Lee could not replace his men and Grant could. The siege of Petersburg, the rail center feeding Richmond, then fixed Lee in the trenches for nine months while Sherman ranged free in Georgia.",
             kick='A · Grant takes command', size=24)

# 7 B DIVIDER
divider_photo('sherman-port.jpg', 'Section B', 'Sherman and Total War',
              ['William Tecumseh Sherman, photographed', 'by Mathew Brady, circa 1865.'],
              "The image is Sherman, photographed by Mathew Brady circa 1865, from the Library of Congress copy on Wikimedia Commons. Section B gives the war its second engine. While Grant fixed Lee in Virginia, Sherman campaigned through the Confederacy's interior, first to Atlanta, the rail and manufacturing center of the Deep South, and then across Georgia itself. His theory matched Grant's and extended it. Armies were the objective, but armies ate, rode railroads, and drew their will from the society behind them, so the society's resources were military targets too. The next two slides take his own statement of that theory and then the march that carried it out, and the vocabulary slides carry his definition in full. His face in the Brady portrait, lined and unsmiling, was the face the Confederacy learned to read as resolution.")

# 8 B CONTENT 1
content_text('Atlanta, and the letter of September 12',
             ['Atlanta taken, September 1864',
              'Civilians ordered out of a military post',
              'To Mayor Calhoun: "War is cruelty"',
              '"You cannot refine it"'],
             "Sherman's definition belongs in this teaching in full. " + joined('William Tecumseh Sherman') + " The occasion of the letter carries as much weight as its sentence. Sherman had ordered Atlanta's remaining civilians to leave the city he meant to hold as a military post, and Mayor James M. Calhoun protested the order's hardship. Sherman answered that the hardship was the war itself, not his order, and that those who brought war into the country deserved its curses. Students read the letter's central paragraphs at Station 5 of the activity, in a named transcription, and judge its argument there.",
             kick='B · Sherman and total war', size=24)

# 9 B CONTENT 2
content_text('The March to the Sea',
             ['Cut loose from supplies, November 1864',
              'Some 62,000 soldiers living off the country',
              'Railroads, mills, and stores destroyed',
              'Savannah reached in December'],
             "The doctrine's definition belongs here in full. " + joined('total war') + " Add the human accounting the reading insists on. The march fed the army and broke Georgia's capacity to supply Lee, and it also stripped farms whose owners were mostly women, children, old men, and enslaved people, thousands of whom followed the columns seeking freedom and food the army could not always give. Sherman then turned north through the Carolinas in 1865, where Columbia burned as his army passed, a fire whose authors the record still argues over. Total war shortened the war. The lesson does not ask students to call it clean.",
             kick='B · Sherman and total war', size=24)

# 10 STAT 60
stat('60', 'miles wide, the corridor of destruction',
     'Sherman\'s march across Georgia, November and December 1864',
     "Pause on the width, because it converts a march into a strategy. A column on one road consumes the farms along it. Sherman marched in parallel columns spread across a front some sixty miles wide, foraging parties working the farms between the roads, so that a band of Georgia from Atlanta to the sea was eaten out and its railroads wrecked beyond quick repair. The figure is the march's own measure in the reports and the histories, stated as the usual figure rather than a surveyed line. Ask students what a corridor that wide was meant to prove to the people inside it. The answer Sherman intended was that the Confederate government could not protect its own heartland, and that continuing the war would bring this to every state that sustained it.",
     kick='B · Sherman and total war')

# 11 C DIVIDER
divider_text('Section C', 'The Election of 1864',
             'An armistice on the ballot, in the middle of a war.',
             "Section C states the war's political fact. The Union held a presidential election on schedule in the fourth year of a civil war, and the war itself was the issue. The Democratic convention at Chicago in August 1864 wrote a platform declaring the war a failure and demanding an immediate armistice, a ceasefire that would have left the Confederacy in possession of its territory while commissioners negotiated. The party then nominated George B. McClellan, the general Lincoln had removed from command in 1862, who accepted the nomination while distancing himself from the armistice plank. Through the summer of Petersburg's trenches and the casualty lists, Lincoln privately expected defeat and prepared to cooperate with a successor he believed would lose the war at the table.")

# 12 C CONTENT
content_text("Atlanta votes, and the soldiers vote",
             ['Lincoln reelected, November 1864',
              'A clear popular majority, an overwhelming electoral margin',
              'Soldiers in the field vote to finish the war',
              'The armistice refused by the voters themselves'],
             "Work the timing before the result, because the result turned on six weeks. Atlanta fell on September 2, and Union victories in the Shenandoah Valley followed, and the northern public that had counted the Overland campaign's cost all summer could suddenly see the war being won. Lincoln carried every northern state but three and won the electoral college by a margin no one had predicted in August. The soldiers' vote, cast in the field under state laws arranged for it, ran heavily for the commander in chief. Teach the consequence rather than the celebration. An armistice government would have negotiated with the Confederacy as a fact. The electorate refused it, and the Confederacy's last strategy, outlasting northern will, died in November rather than April.",
             kick='C · The election of 1864', size=24)

# 13 D DIVIDER
divider_text('Section D', "The Union's Other Wartime Work",
             'Farms and colleges chartered, and an amendment carried, while armies fought.',
             "Section D widens the frame on purpose, because the war's settlement was not made only by armies. With the seceded states' members absent, the wartime Congress passed in 1862 the program the South had blocked for a generation, land for settlers and land grant colleges among it, and the records of that work sit in the activity beside the generals' letters. The section's second campaign belongs to women who held no vote and no office. The Women's Loyal National League turned the right of petition into an engine for a constitutional amendment, and the House answered on January 31, 1865. That passage is named here as a wartime event, and no further, by the unit's design. The Homestead Act and the Morrill Land-Grant Act are the two statutes the reading names, and the activity prints the Homestead text itself at Station 4.")

# 14 D CONTENT 1
content_text('Homesteads and colleges, 1862',
             ['The Homestead Act: 160 acres to a settler',
              'Five years of farming, and the land was yours',
              'The Morrill Act: land to fund state colleges',
              'Passed by a Congress the South had left'],
             "Read the statute's terms at Station 4 of the activity, where section 1 of the Homestead Act is printed from the audited bank record. Any head of a family or adult citizen, or an immigrant who had declared an intention to become one, who had never borne arms against the United States, could enter a quarter section of public land. State the record's own shadow plainly. The public land the act gave away was Native land, taken through treaties and war, a point the bank record's headnote makes and the lesson keeps. The Morrill Land-Grant Act of the same summer granted federal land to fund colleges of agriculture and the mechanical arts. Together the two acts chartered the farms and the universities of the postwar country while the war for the Union was still undecided.",
             kick="D · The Union's other wartime work", size=24)

# 15 D CONTENT 2
content_text('The petition campaign, and January 31, 1865',
             ["The Women's Loyal National League, 1863",
              'Petitions for an amendment abolishing slavery',
              'Some 400,000 signatures, by the usual count',
              'The House passes the Thirteenth Amendment, January 31, 1865'],
             "Its definition belongs in this teaching in full, exactly as the guided notes carry it. " + joined('Thirteenth Amendment') + " Teach the boundary the unit draws around that definition. The League, founded by Elizabeth Cady Stanton and Susan B. Anthony, made the petition the weapon of women who could neither vote nor fight, and its address is Station 3 of the activity. The amendment's passage is taught here as a wartime event, one date inside the war's last winter. Its ratification fight, and the settlement built on it after the war, belong to the next unit, and this lesson does not open them.",
             kick="D · The Union's other wartime work", size=24)

# 16 STAT 400,000
stat('400,000', 'signatures for abolition, by the usual count',
     'The Women\'s Loyal National League petition campaign, 1863 to 1865',
     "Pause on the number, stated as the campaign's usual count, because it measures a form of power the Constitution left open to the voteless. The League set out to gather a million names and presented its rolls to Congress in installments, Senator Charles Sumner carrying the first great roll into the Senate in February 1864. Four hundred thousand signatures represented canvassing in every loyal state, organized by women who could not cast a ballot for any member they petitioned. When the House passed the Thirteenth Amendment in January 1865, members on both sides credited the petitions with stiffening the vote. Students should connect the figure to Station 3, where the League's own address argues that while slavery exists anywhere there can be freedom nowhere.",
     kick="D · The Union's other wartime work")

# 17 E DIVIDER
divider_photo('mclean-port.jpg', 'Section E', 'Appomattox',
              ['The McLean house, photographed by', "Timothy H. O'Sullivan, April 1865."],
              "The image is the McLean house at Appomattox Court House, photographed by Timothy H. O'Sullivan in April 1865, from the Library of Congress copy. Section E runs the war's last week. Wilmer McLean, in whose parlor the surrender was signed, had moved to Appomattox to escape the war after its first great battle was fought across his earlier farm at Manassas, a coincidence the record documents and students may hear as the war's bookend, provided it is taught as coincidence and not as fate. The surrender's own definition sits in the vocabulary, and the next two slides take the retreat and then the terms, in that order, because the terms were written for an army that had been run to ground, not for one that had been talked into stopping.")

# 18 E CONTENT 1
content_text("Richmond falls, and Lee's way runs out",
             ['Petersburg lines break, April 2, 1865',
              'Richmond evacuated and burning, entered April 3',
              "Lee marches west, hoping for supplies",
              'Union cavalry and infantry close the retreat'],
             "Work the week as a closing trap, day by day. Grant's spring offensive finally broke the Petersburg lines on April 2, and Lee told Jefferson Davis the capital must be evacuated that night. Richmond's departing authorities set fires to warehouses and arsenals, and the fires spread through the business district before Union troops entered on April 3 and put them out. Lee marched west along the Appomattox River expecting rations waiting at Amelia Court House that were not there, losing a day his army did not have. Union cavalry got across his front near Appomattox Court House while infantry closed behind him. On the morning of April 9 Lee's last attack failed to break the cavalry line, and infantry stood behind it. He sent word to Grant that he would meet him.",
             kick='E · Appomattox', size=24)

# 19 E CONTENT 2
content_text('The terms in the McLean parlor, April 9',
             ['Soldiers paroled home, not imprisoned',
              "Officers keep their sidearms",
              'Horses taken home for the spring planting',
              'Grant stops the celebrating salutes'],
             "Its definition belongs in this teaching in full. " + joined('Appomattox Court House') + " Teach the terms as Lincoln's policy executed, not as improvisation. Lincoln had instructed his commanders at City Point in March to let the Confederates down easy, and Grant's terms did exactly that: no treason trials implied, no prison camps, and an army sent home to plant. Grant also ordered rations issued to Lee's starving men from Union stores. When Union guns began a victory salute, Grant stopped it, holding that the Confederates were fellow countrymen again and there would be no rejoicing over a fallen foe. The other Confederate armies surrendered in the weeks that followed, on the Appomattox model.",
             kick='E · Appomattox', size=24)

# 20 F DIVIDER
divider_text('Section F', 'The Verdict of the Second Inaugural',
             "March 4, 1865: slavery the offense, and the war its woe.",
             "Section F slows down on a speech of some seven hundred words, because the speech is the war's own verdict on the unit's essential question and the activity prints it in full as its first station. Lincoln delivered it on March 4, 1865, at his second inauguration, with the war visibly ending and its cost beyond any figure his audience needed to be given. He used the occasion, the most ceremonial a president commands, not to celebrate the coming victory but to name the war's cause and apportion its guilt, and he apportioned it to his own section as well as to the enemy. The address's definition sits in the vocabulary. The next slide reads its argument in three moves.")

# 21 F CONTENT
content_photo('lincoln-port.jpg', 'The offense, the woe, the obligation',
             ['One eighth of the population were colored slaves',
              '"Somehow the cause of the war"',
              'Both read the same Bible; neither prayer answered fully',
              '"With malice toward none, with charity for all"'],
             "The image is Lincoln, photographed by Alexander Gardner on February 5, 1865, a month before the address. " + joined('Second Inaugural Address') + " Read the three moves in order. First the cause, stated as common knowledge: the slave interest was somehow the cause of the war. Second the judgment: if slavery is an offense that must needs come, the war is the woe due for it, charged to North and South together. Third the obligation, which the closing sentence lays out as work, binding wounds and caring for the soldier, his widow, and his orphan.",
             kick='F · The verdict of the Second Inaugural')

# 22 G DIVIDER
divider_text('Section G', 'April 1865, and What Stood Open',
             'The assassination, and the claims the war left unanswered.',
             "Section G closes the unit in the month the war ended, and it closes deliberately on what the ending did not do. On April 14, five days after Appomattox, John Wilkes Booth shot Lincoln at Ford's Theatre, and the president died the next morning. Jefferson Davis was captured in Georgia in May, and the remaining Confederate armies surrendered by June. The two great questions the war had been fought over stood settled, the Union indivisible and slavery destroyed as a legal system. But a settlement on paper is not a settlement in a life, and this section measures the distance between the two in one letter written by an enslaved woman in Maryland, which students read in full at Station 2 of the activity.")

# 23 G CONTENT 1
content_text("The president killed, and Annie Davis's question",
             ['Booth at Ford\'s Theatre, April 14, 1865',
              'Lincoln dead on the morning of April 15',
              'Annie Davis, August 1864: "if we are free"',
              'Maryland frees her by its own constitution, November 1864'],
             "Tell the assassination plainly and briefly, as the record gives it: a famous actor and Confederate sympathizer shot the president in his box at the theatre, and Lincoln died across the street the next morning, the war's last famous casualty. Then set beside it the letter that measures the settlement's edge. Annie Davis, enslaved at Belair, Maryland, wrote to Lincoln in August 1864 that it was her desire to be free, to go and see her people on the Eastern Shore, and asked him to let her know if we are free, and what she could do. The Emancipation Proclamation had not named loyal Maryland. Her state freed her that November by its own new constitution, a freedom no federal measure had given her when she asked.",
             kick='G · April 1865, and what stood open', size=24)

# 24 G CONTENT 2
content_text('Settled, and left standing',
             ['Settled: no state could leave the Union',
              'Settled: slavery destroyed as a legal system',
              'Left standing: land for the freed people',
              'Left standing: safety, and the vote'],
             "Close the lesson's argument in its own two columns, because the unit test and the writing task both grade the distinction. Settled beyond reopening: the Union was perpetual in fact as Lincoln had argued it was in law, and slavery as a system of property in human beings was destroyed, its destruction written into the Constitution by the amendment Congress passed in January 1865. Left standing in April 1865, exactly where the war left them: whether the freed people would hold land of their own, whether they would be safe in their homes and persons, and whether they would vote. Those questions were not answered at Appomattox, in the Second Inaugural, or in any document of this unit. They are the questions the next unit opens with, and the lesson ends by naming them rather than resolving them.",
             kick='G · April 1865, and what stood open', size=24)

# 25 VOCAB A
vocab('Words for the commanders',
      [('Ulysses S. Grant', 'the general in chief from March 1864'),
       ('total war', 'war on resources and will, not armies alone')],
      "Two of the lesson's seven terms, matching the guided notes exactly, and both belong to Section A and Section B. " + joined('Ulysses S. Grant') + ' ' + joined('total war') + " Students meet both terms again in the synthesis, where Grant's pressure on the armies and Sherman's war on the resources behind them stand as the first row of the ending at a glance.")

# 26 VOCAB B
vocab('Words for the march',
      [('William Tecumseh Sherman', 'Atlanta taken, and the letter of September 12'),
       ('March to the Sea', 'Atlanta to Savannah, November and December 1864')],
      "Two more terms, again matching the guided notes exactly, and both belong to Section B. " + joined('William Tecumseh Sherman') + ' ' + joined('March to the Sea') + " Together the pair states the lesson's western argument in miniature: the general who defined war as cruelty that cannot be refined, and the campaign that carried that definition across Georgia to the sea, in the war's last full season of fighting before the Carolinas and the end.")

# 27 VOCAB C
vocab('Words for the settlement',
      [('Thirteenth Amendment', 'passed January 31, 1865, ratified that December'),
       ('Appomattox Court House', 'the surrender of April 9, 1865'),
       ('Second Inaugural Address', "Lincoln's verdict, March 4, 1865")],
      joined('Thirteenth Amendment') + ' ' + joined('Appomattox Court House') + ' ' + joined('Second Inaugural Address'))

# 28 SYNTHESIS
s = slide(NAVY)
kicker(s, 'The ending at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Pressure, vote, surrender, verdict, open claims', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Pressure', 'Grant and Sherman, 1864', 'Armies fixed, resources destroyed'),
        ('Vote', 'The election and the petitions', 'No armistice; an amendment carried'),
        ('Surrender', 'Appomattox, April 9, 1865', 'Paroles, sidearms, horses for planting'),
        ('Verdict', 'The Second Inaugural', 'Slavery the offense, the war its woe'),
        ('Open', 'April 1865', 'Land, safety, and the vote unanswered')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the guided notes table, The Ending at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The five rows compress the hour and close the unit. Pressure: Grant fixed the Confederate armies while Sherman destroyed the resources behind them. Vote: the electorate refused an armistice in 1864 and the petition campaign carried an amendment through the House. Surrender: Lee's army went home on parole at Appomattox. Verdict: Lincoln named slavery the offense and the war its woe, charged to both sections. Open: the freed people's land, safety, and vote stood unanswered. The guided notes table uses these same five rows, so the chart in the notebooks and the summary on screen cannot drift apart.")

# 29 EXIT
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Work the ending file', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did the war end, and what did its ending settle? Work the five records in order, then judge the Second Inaugural\'s verdict from the file.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Ending File: the Second Inaugural, Annie Davis, the League, the Homestead Act, and Sherman'),
        ('Notebook', 'Notebook page: what each piece did, how it ended the war, and what it left unanswered'),
        ('Quick check', "The Woe Due: Lincoln's judgment read against Sherman's letter"),
        ('Writing', "The Verdict of the Second Inaugural: Lincoln's claim judged from at least three bank documents")]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: Grant\'s doctrine and the Appomattox terms, the amendment\'s date, and the lesson question answered from both settlements.',
     size=15, color=POWDER)
notes(s, "Close by handing the lesson to the work. The activity, The Ending File, runs five stations: the Second Inaugural Address in full, Annie Davis's letter, and the Women's Loyal National League address, all from the audited bank records, the Homestead Act's first section from the same bank, and Sherman's letter to Atlanta's mayor from a named transcription, ending in a table of what the war had settled and left standing and a defended judgment on Lincoln's verdict. The notebook page holds what each piece did and what it left unanswered. The quick check, The Woe Due, reads Lincoln's judgment against Sherman's explanation. The writing task, The Verdict of the Second Inaugural, requires a judgment from at least three bank documents and a reply to the strongest claim of the other side. The exit ticket has three parts, as printed at the end of the guided notes.")

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
