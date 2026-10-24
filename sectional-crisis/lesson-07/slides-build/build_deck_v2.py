#!/usr/bin/env python3
"""Sectional Crisis and Civil War Lesson 7 deck: Emancipation and the War Transformed, 1863.
Vocabulary definitions are parsed verbatim from the unit spec at build time."""
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
OUT = os.path.join(HERE, '..', 'lesson-07-slides.pptx')

SPEC = open(os.path.join(HERE, '..', '..', 'build-scripts', 'unit-spec.md')).read()
_sec = SPEC.split('### Lesson 7')[1].split('### Lesson 8')[0]
DEFS = {}
for line in _sec.splitlines():
    m = re.match(r'- (.+?): (.+)$', line.strip())
    if m: DEFS[m.group(1)] = m.group(2)
assert len(DEFS) == 7, DEFS.keys()

def vocab_join(terms):
    return ' '.join(f"{t}: {DEFS[t]}" for t in terms)

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

def content_photo_s(img, title, items, note, kick=None, size=23):
    s = slide(CREAM)
    photo_right(s, img)
    if kick: kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95 if kick else 0.8, 6.9, 1.2, title, size=31, color=NAVY, font='Georgia', leading=1.05)
    frags(s, items, y=2.15 if kick else 2.0, size=size)
    notes(s, note)
    return s

# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'SECTIONAL CRISIS AND CIVIL WAR \u00b7 LESSON 7', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Emancipation and the War Transformed', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Contraband, the Proclamation, Black soldiers, and the turning of 1863', size=17, color=POWDER)
notes(s, "The image is the gateway of the cemetery at Gettysburg, photographed in 1863 by Timothy O'Sullivan and printed by Alexander Gardner, held by the Library of Congress and in the public domain. It is a gate, not a battlefield scene, and this lesson uses no photograph of the dead anywhere, following the discipline this unit applied at Antietam. Open by placing the lesson in the unit. Lesson 6 ended on September 22, 1862, with the preliminary Emancipation Proclamation in Lincoln's desk and the war still officially a war for Union alone. This lesson follows the year that followed that paper: the proclamation in force, enslaved people reaching the lines in numbers no order created, Black men in Union uniform, and the twin victories of July 1863 that remade the war's meaning while New York burned its draft offices.")

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("How did emancipation change what the war was for, and for whom?", {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ("How did compromise over slavery finally fail, and what did the war it caused settle about slavery and the Union, and what did it leave open?", {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Read the question's two halves and keep both alive all hour. The first half asks what emancipation did to the war's purpose: a war begun in 1861 to restore the Union as it was had, by the end of 1863, a government committed to maintaining the freedom of millions and a president rededicating it to the proposition that all men are created equal. The second half asks for whom: for the enslaved people who freed themselves by reaching the lines, for the Black men who enlisted and fought for equal pay as well as for the Union, and also for the people the proclamation deliberately did not reach, in the loyal border states and the exempted districts. Warn students that the documents will argue both sides. The proclamation calls itself a war measure, and its limits are printed on its face. The lesson's work is to weigh those limits against what the measure set in motion, not to recite either the celebration or the dismissal.")

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Freedom enters the war, and the war changes', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'Freedom walked to the lines first', 'Contraband at Fort Monroe, Congress follows, Antietam'),
        ('B', 'The Proclamation and its limits', 'January 1, 1863, and the states it did not touch'),
        ('C', 'Freedom as the enslaved executed it', 'Half a million reach the lines, labor withdrawn'),
        ('D', 'Black soldiers under arms', '180,000 serve, the pay fight, Fort Pillow'),
        ('E', 'The 54th Massachusetts at Fort Wagner', 'July 18, 1863, Shaw and nearly half the regiment'),
        ('F', 'Gettysburg, Vicksburg, and the Address', 'July 1 to 4, and November 19, 1863'),
        ('G', "The draft riots, Robinson's defense, the new arithmetic", 'New York in July, slavery defended in print')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This slide is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A begins before the proclamation, with the enslaved people whose arrival at Fort Monroe forced the government's hand in 1861. Section B reads the proclamation closely, promises and limits together. Section C follows freedom as the enslaved themselves executed it. Sections D and E take up the Black soldiers: the regiments, the recruiting broadside, the unequal pay, and the 54th Massachusetts at Fort Wagner. Section F holds the military turning of July 1863 and the Address that restated the war in November. Section G refuses a clean ending, setting the draft riots and Robinson's defense of slavery beside the new arithmetic the year left behind.")

# 4 A DIVIDER
divider_text('Section A', 'Freedom Walked to the Lines First',
             'Contraband at Fort Monroe, a Congress following, and a president waiting for a victory.',
             "Section A insists on the order of events, because the order is the argument. Emancipation did not begin in Washington. It began in May 1861 at Fort Monroe, Virginia, where enslaved people escaped to the Union fort and General Benjamin Butler, a lawyer in uniform, refused to return them. His word for them, contraband of war, treated them as property seized from the enemy, a legal fiction everyone involved understood: it let the army shelter and employ people the law still called slaves while the government insisted the war was for Union only. Congress followed the fugitives with a Confiscation Act and, in April 1862, emancipation in the District of Columbia, paying loyal owners. Lincoln waited longer, for reasons this section states fairly: border states to hold and a victory to speak from. Antietam supplied the second, and the preliminary proclamation followed on September 22, 1862.")

# 5 A CONTENT
content_text('Contraband, Congress, and a waiting president',
             ['In May 1861 came Fort Monroe, Butler, and contraband of war.',
              'In 1861 Congress passed a first Confiscation Act.',
              'In April 1862 came freedom in the District of Columbia.',
              'Loyal owners were paid in the capital.',
              'On September 22, 1862, came the preliminary proclamation.'],
             "Teach each step as a ratification of the step before it, because that is how emancipation actually entered this war. The fugitives acted first, at risk, without any promise that the army would keep them. Butler's ruling kept them, on a theory borrowed from the law of captured property, and students should notice the strangeness without mocking it: the fiction protected real people, and the men and women at Fort Monroe put their labor at the army's service under its cover. Congress then legislated at the edges, confiscation for the disloyal and compensated emancipation in the one jurisdiction it governed directly, the capital. Lincoln's waiting belongs in the same ledger. He had drafted his proclamation by the summer of 1862 and held it on Secretary Seward's advice until a victory made it read as strength rather than desperation. Antietam, a draw on the field and a strategic check to Lee, was enough, and on September 22 the country learned what January 1 would bring.",
             kick='A \u00b7 Freedom walked first', size=23)

# 6 B DIVIDER
divider_photo('lincoln-port.jpg', 'Section B', 'The Proclamation and Its Limits',
              ['Abraham Lincoln, photographed by Alexander Gardner,', 'August 9, 1863. Public domain.'],
              "The portrait is Alexander Gardner's Lincoln of August 9, 1863, taken in Washington five weeks after Gettysburg and a month after the draft riots, in the middle of the year this lesson studies. Section B reads the Emancipation Proclamation the way the activity's first station prints it, from the audited bank record: its declaration, its promises, and its limits, all in the document's own words. Insist that students hold both halves in one reading. The proclamation declared forever free the enslaved people in the states and parts of states in rebellion, and ordered the whole Executive Government, army and navy included, to recognize and maintain that freedom. It also, deliberately, did not touch Delaware, Maryland, Kentucky, or Missouri, and it exempted Tennessee and the occupied districts of Louisiana and Virginia. Both facts are in the text, and any account that keeps only one of them is a slogan, not a reading.")

# 7 B CONTENT
content_photo_s('lincoln-port.jpg', 'Declared free, and deliberately not declared',
             ['On January 1, 1863, they were declared then, thenceforward, and forever free.',
              'The government would recognize and maintain that freedom.',
              'Delaware, Maryland, Kentucky, and Missouri stood untouched.',
              'Tennessee and occupied Louisiana and Virginia were exempted.',
              'The ranks were opened to Black enlistment.'],
             "Work the critics' charge and the supporters' answer as a pair, because the station questions ask for both. The charge: the proclamation freed people where the Union could not yet enforce freedom, in the rebellious states, and stood aside where it could, in the loyal slave states and the occupied districts. The answer, also from the document: freedom in the rebellious states struck at the labor system the Confederacy fought with; the order to maintain that freedom bound every Union commander who advanced; the invitation into the armed service turned the freed into soldiers of their own liberation; and a war openly against slavery made British or French recognition of the Confederacy a defense of slavery in the eyes of their own publics. Add the constitutional frame students need: Lincoln acted as commander in chief under his war powers, which is why the measure reaches only where rebellion gave it reach, a limit Lesson 8 will revisit when an amendment becomes necessary.",
             kick='B \u00b7 The Proclamation', size=23)

# 8 STAT JAN 1
stat('January 1, 1863', 'the Emancipation Proclamation in final form',
     'Preliminary form September 22, 1862, after Antietam; one hundred days of warning',
     "Give this date its full weight as a hinge and then complicate it in the same breath, which is the lesson's method throughout. On this date the United States government committed itself, in a public instrument, to the freedom of some three and a half million people in the rebellious states and to maintaining that freedom with its army and navy. No earlier act of the government had done anything like it. And on this same date, slavery remained entirely legal in four states that had stayed in the Union, and in districts under Union occupation where federal power was absolute. Both statements belong on the board together. Students who can hold them together, commitment and limit in one date, are ready for the verdict the activity will ask them to write. Students who can hold only one will write the slogan version, and the grading guide prices exactly that difference.",
     kick='B \u00b7 The Proclamation')

# 9 C DIVIDER
divider_text('Section C', 'Freedom as the Enslaved Executed It',
             'The news traveled, the labor withdrew, and the armies gained guides, workers, and intelligence.',
             "Section C names the lesson's central historical actors, and teachers should give them the section's full time. A proclamation is paper. What turned this one into fact was the movement of enslaved people toward Union lines, a movement already two years old when the proclamation took effect and vastly widened by it. The news of January 1 traveled through the enslaved community by word of mouth, along the same networks that had carried word of Fort Monroe in 1861. Families timed their leaving to the armies' approach, and their leaving did double work: it withdrew labor from the Confederacy's fields, fortifications, and wagon trains, and it delivered labor, local knowledge, and intelligence to the Union. The section also teaches a habit of honesty about numbers. No census counted the people who reached the lines, and the reading states the figure as an estimate, some half a million by the war's end, and students should learn to say estimated when the record estimates.")

# 10 C CONTENT
content_text('Half a million decisions',
             ['News of January 1 was carried by word of mouth.',
              'Families left as the armies approached.',
              'Their labor was offered to the Union armies.',
              'They brought information about roads, rivers, and supplies.',
              'The estimates run to some half a million by 1865.'],
             "Slow down on the word executed in the section title, because it carries the section's claim. In law a proclamation is executed by officers. Here it was executed, carried into effect, by the people it named, most of whom never saw the document. Each departure was a decision made with incomplete information and real danger: patrols, punishment for those caught, families divided by who could travel and who could not. Union commanders' reports from these years are full of the consequences, camps of newcomers needing food and shelter behind the lines, work crews on the fortifications, guides who knew the fords and the back roads. Set the Confederacy's side of the ledger beside it. Every field hand who reached the lines was a hand the rebellion's agriculture and engineering no longer had, and the loss compounded monthly. This is why the reading calls emancipation a military fact however narrowly the measure was drawn: by 1864 no settlement of the war could put these people back, and everyone at the negotiating tables knew it.",
             kick='C \u00b7 The enslaved execute it', size=23)

# 11 D DIVIDER
divider_photo('douglass-port.jpg', 'Section D', 'Black Soldiers Under Arms',
              ['Frederick Douglass, by Samuel J. Miller,', 'between 1847 and 1852. Art Institute of Chicago.'],
              "The photograph is Samuel J. Miller's daguerreotype of Frederick Douglass, made between 1847 and 1852 and held by the Art Institute of Chicago. Douglass sat for portraits deliberately and often, and by 1863 he was the recruiting drive's most famous voice, his broadside 'Men of Color, To Arms!' of March 1863 printed at the activity's second station as the bank record presents it. Section D follows the men the broadside called. Congress had authorized Black enlistment in July 1862; the proclamation made it policy; the United States Colored Troops organized it. Teach Douglass's own stake honestly: two of his sons served, one of them in the 54th Massachusetts of the next section, and Douglass pressed the pay injustice on the president in person in August 1863. The broadside promised that rising to arms would silence the tongue of calumny, prejudice, and hate, and that the men who rose would be regarded as men. Section D prices that promise against the service actually offered.")

# 12 D CONTENT
content_photo_s('douglass-port.jpg', 'Ten dollars against thirteen',
             ['The Militia Act of July 1862 authorized enlistment.',
              'The United States Colored Troops were organized in 1863.',
              'Black soldiers were paid ten dollars a month, and white soldiers thirteen.',
              'Clothing was charged against the smaller sum.',
              'Equal pay was won in June 1864.'],
             "Teach the pay figures exactly, because the vocabulary and the quick check both price them. A Black private was offered ten dollars a month, with three dollars of it chargeable for clothing; a white private received thirteen dollars and a clothing allowance beyond it. Black soldiers and their allies argued the point as one of standing, not only of money: a government that paid a man less for the same risk had written his inferiority into its own pay tables. Protests ran from camp petitions to the 54th Massachusetts's refusal, in the next section, to take any pay at all until it was equal. Congress equalized pay in June 1864, with back pay fought over after. Then state Fort Pillow plainly and stop: in April 1864, after the Tennessee fort was taken and resistance had ended, Confederate troops killed many of its Black defenders. The fact belongs in any honest account of what Black service risked, and it needs no decoration.",
             kick='D \u00b7 Black soldiers', size=23)

# 13 STAT 180000
stat('180,000', 'Black men served in the Union army by the war\u2019s end',
     'Some 180,000, roughly a tenth of the Union army, most of them formerly enslaved',
     "Let this number stand against the broadside's promise and the pay table's insult at once, because it answers both. Roughly a tenth of the Union army, by the war's end, was made up of Black soldiers, the great majority of them men who had been enslaved when the war began. They garrisoned forts, guarded supply lines, dug, marched, and fought in some one hundred and seventy-five engagements, and their presence freed white regiments for the field armies while their service withdrew labor from the Confederacy a second time. Douglass had argued that once a Black man wore the brass letters of the United States and carried a musket, no power could deny he had earned citizenship. The number on this slide is that argument made demographic. Students should also hear the navy's share in the same story: Black sailors had served from the war's first year, before any proclamation, in an integrated service the army took two more years to imitate.",
     kick='D \u00b7 Black soldiers')

# 14 E DIVIDER
divider_text('Section E', 'The 54th Massachusetts at Fort Wagner',
             'A regiment recruited from across the North, an assault on July 18, 1863, and an eighteen month refusal of unequal pay.',
             "Section E concentrates the last section's abstractions into one regiment, and the concentration is the teaching method. The 54th Massachusetts was the first Black regiment raised in the North, recruited in the spring of 1863 under Governor John Andrew of Massachusetts and commanded by Colonel Robert Gould Shaw, a young officer from an abolitionist family. Its ranks filled with free Black men from across the North, barbers, sailors, farmers, and waiters who traveled to Boston to enlist, among them Lewis and Charles Douglass, the broadside writer's sons. Two facts about the regiment carry the section: what it did on July 18, 1863, in front of Fort Wagner, and what it refused for eighteen months afterward in the matter of its pay. Keep both in view. The assault answers the question of courage. The refusal answers the question of dignity, and the regiment's own officers stood with the men in it, declining their pay as well.")

# 15 E CONTENT
content_photo_s('usct-port.jpg', 'Across the sand at Fort Wagner',
             ['It was recruited in the spring of 1863, under Colonel Robert Gould Shaw.',
              'On July 18, 1863, it made the assault on Fort Wagner.',
              'Shaw was killed on the parapet.',
              'Nearly half the regiment was lost.',
              'Then came eighteen months refusing unequal pay.'],
             "The photograph is Company E of the 4th United States Colored Infantry at Fort Lincoln, in Washington, photographed during the war years and held by the Library of Congress; it is not the 54th Massachusetts, and students should hear the caption read honestly, as an image of the United States Colored Troops generally. Fort Wagner guarded Charleston harbor, and on the evening of July 18, 1863, the 54th led the assault across open sand against its guns. Shaw was killed on the parapet, and nearly half the regiment was killed, wounded, or missing before the survivors fell back; the fort itself was not taken that night and fell later to siege. What the assault settled was said at the time by men who had opposed Black enlistment: the claim that Black men would not fight could no longer be printed with a straight face. Sergeant William Carney, wounded, carried the regiment's flag back and is remembered for reporting that the old flag never touched the ground. The regiment then refused its pay, month after month, rather than accept the lesser rate, until Congress acted in June 1864.",
             kick='E \u00b7 The 54th Massachusetts')

# 16 F DIVIDER
divider_photo('gate-port.jpg', 'Section F', 'Gettysburg, Vicksburg, and the Address',
              ['The cemetery gateway at Gettysburg, 1863,', 'by O\u2019Sullivan and Gardner. Library of Congress.'],
              "The image is the gateway of the cemetery at Gettysburg, photographed in 1863 by Timothy O'Sullivan and printed by Alexander Gardner, held by the Library of Congress. Section F holds the year's military turning and its restatement together, because Lincoln himself joined them in November. First the field: in May 1863 Lee beat the Army of the Potomac at Chancellorsville and lost Stonewall Jackson, mortally wounded by his own men in the dusk. In June Lee invaded the North a second time, hunting supplies, a victory on northern soil, and the European recognition emancipation had made so much harder. What he found was Meade's army at a Pennsylvania crossroads town. Teach the section's two July dates as one event in two theaters: Gettysburg ending on July 3, Vicksburg surrendering on July 4, and a country reading both telegrams on the same Independence Day.")

# 17 F CONTENT
content_photo_s('gate-port.jpg', 'Three days, and a river',
             ['In May 1863 came Chancellorsville, and Jackson was lost.',
              'From July 1 to 3, Gettysburg stopped the invasion.',
              'The cost was some fifty thousand casualties, both armies together.',
              'On July 4, Vicksburg surrendered to Grant.',
              'The Mississippi was held, and the Confederacy split.'],
             "Work the arithmetic of the turning without inflating it, because students will meet claims that Gettysburg alone won the war. Gettysburg stopped Lee's second invasion and ended the Confederacy's realistic hope of winning the war on northern soil or convincing Europe to intervene. It did not destroy Lee's army, which escaped across the Potomac while Meade, his own army mauled, did not press the pursuit, to Lincoln's open frustration. Vicksburg was the heavier strategic blow: after a six week siege the fortress surrendered on July 4, and with Port Hudson's fall days later the Union held the whole Mississippi River. Texas, Arkansas, and Louisiana were cut off from the rest of the Confederacy, and Grant's reputation was made. Falling together, the two victories also did political work at home: they steadied northern opinion in the very month New York rioted, and they gave Lincoln the ground from which, in November, he could say what the war now meant.",
             kick='F \u00b7 The turning of 1863', size=23)

# 18 STAT 50000
stat('about 50,000', 'casualties at Gettysburg, both armies together',
     'July 1 to 3, 1863: killed, wounded, and missing in the war\u2019s greatest battle',
     "State the figure's composition before its size, because students hear fifty thousand as fifty thousand dead, and it is not. Casualties means killed, wounded, captured, and missing together; the dead at Gettysburg numbered roughly seven thousand of the total, the wounded many times that, and thousands of the wounded died later in the hospitals whose work the cemetery dedication acknowledged. November is where the precision pays. When Lincoln stood in that cemetery on November 19, the ground he was dedicating held the buried of both armies' worst three days, and the town around him was still a hospital. His two minutes answered this number. The address does not mention slavery, the proclamation, or any battle by name; it reaches under the casualty list to the founding proposition and asks whether the dead men's unfinished work will be taken up. Students should be able to state the figure, its dates, and the distinction between casualties and dead, and the quick check prices all three.",
     kick='F \u00b7 Gettysburg')

# 19 STAT JULY4
stat('July 4, 1863', 'Vicksburg surrenders, the day after Gettysburg ended',
     'A six week siege closed; the Union held the whole Mississippi River',
     "Hold this date up as the lesson's second hinge, the western answer to Gettysburg's eastern one. Grant had spent the spring maneuvering below Vicksburg, crossing the Mississippi, winning battles in the interior, and finally sealing the fortress in a siege of six weeks, during which its soldiers and civilians starved on shrinking rations. The surrender on July 4 gave the Union the river entire once Port Hudson followed, split the Confederacy in two, and freed Grant's army for the work Lesson 8 follows to Chattanooga and beyond. Note the coincidence the country felt at the time and did not invent later: the two victories arrived together on Independence Day, one day after the Pennsylvania battle ended and one day before its news had finished spreading. Lincoln, who had pressed his generals for exactly this kind of simultaneous pressure, now had a war that was visibly turning, and the Address of November is written from that ground.",
     kick='F \u00b7 Vicksburg')

# 20 G DIVIDER
divider_text('Section G', "The Draft Riots, Robinson's Defense, and the New Arithmetic",
             'Four days in New York, a book in Philadelphia, and a war whose labor and soldiers had changed sides.',
             "Section G is the lesson's honesty section, and it should be taught at the same pace as the victories, not hurried past on the way to the Address. In July 1863, in the same month as Gettysburg and Vicksburg, New York City gave the war its worst home front violence: four days of rioting against the draft in which the mobs turned on Black New Yorkers, who had nothing to do with the draft law, and lynched men in the streets. In the same year a Philadelphia writer, John Bell Robinson, published a book length defense of slavery as an institution imposed by God, excerpted at the activity's fourth station as the bank record presents it. Neither fact reverses the year's turning. Both facts belong in the verdict students write about it, and the grading guide for the activity prices whether they are carried or quietly dropped.")

# 21 G CONTENT
content_text('The war\u2019s other face, in its largest city',
             ['Under the draft, three hundred dollars hired a substitute.',
              'From July 13 to 16 came four days of rioting in New York.',
              'Black New Yorkers were attacked, and the orphan asylum burned.',
              'The dead were estimated at about one hundred twenty.',
              'Order was restored by troops from Gettysburg.'],
             "Teach the riots with the same plainness as Fort Pillow: the grievance stated fairly, the violence stated exactly, and no lingering. The grievance was real. The Enrollment Act's three hundred dollar commutation let a man with money buy his way out of the draft for a working man's yearly wages, and the lottery's resumption on July 13 lit the city's anger. What the mobs did with that anger is the record's center: they burned draft offices, then turned on Black residents, beating and lynching men in the streets and burning the Colored Orphan Asylum after its children were got out to safety. Estimates of the dead usually run to about one hundred twenty. Federal regiments, some marched straight from the Gettysburg campaign, restored order at cannon point, and the draft resumed under guard in August. Then set Robinson beside the riots: slavery's defense, in the emancipation year, was being argued in print in the North as well as resisted in the street, from Noah's curse, by a writer who admitted in his own text that he could not say why God had imposed it.",
             kick='G \u00b7 The strain and the arithmetic', size=23)

# 22 GLANCE
s = slide(NAVY)
kicker(s, 'Emancipation at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Four rows, one transformation', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The road', 'Contraband 1861, Congress 1862', 'Freedom a fact before it was policy'),
        ('The proclamation', 'January 1, 1863, limits printed on it', 'The Union committed, four states untouched'),
        ('Black soldiers', '180,000, pay won June 1864', 'Citizenship argued from the ranks'),
        ('Turning and strain', 'Gettysburg, Vicksburg, the Address', 'Riots and Robinson in the same year')]
yy = 2.72
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 0.88
notes(s, "This slide mirrors the final table in the guided notes, Emancipation at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The rows compress the arc the lesson has built, and each row pairs a change with what it left standing, because that pairing is the lesson's habit. The road row credits the enslaved with the first move and Congress and the president with following it. The proclamation row holds the commitment and the four untouched states in one breath, as the document itself does. The soldiers row runs from the recruiting broadside to the pay victory of June 1864, a claim to citizenship argued in uniform. The turning row refuses to separate Gettysburg, Vicksburg, and the Address from the riots and Robinson's book, all in the same twelve months. Grade the table generously on wording and strictly on the pairing: every row must show the change and the remainder together.")

# 23 SYNTHESIS
content_text('Purpose, instrument, and the people who decided',
             ['The war\u2019s stated terms changed, with Union and freedom joined.',
              'The army changed, a tenth of it Black by 1865.',
              'The Confederacy changed, its labor leaving the field.',
              'Slavery in the loyal border states stood unchanged.',
              'What freedom would mean after the war was left open.'],
             "Draw the lesson together around the activity's verdict question, because the exit ticket and the writing task both return to it. The instrument case is honest and students should be able to make it: the proclamation was a war measure, drawn to reach only where rebellion gave it reach, and slavery survived the whole war in the states that had stayed loyal. The purpose case is also in the record: a government that bound itself to maintain a freedom declared forever, armed the freed, won its great twin victory in the emancipation summer, and heard its president restate the war as a test of human equality had changed what it was fighting for. What tips the record, and what strong verdicts notice, is who executed the change: the enslaved people and Black soldiers who made emancipation irreversible on the ground. What freedom would mean in land, safety, and the vote, this war did not settle, and the unit's last lesson leaves those questions standing where 1865 left them.",
             kick='Synthesis', size=23)

# 24 VOCAB A
vocab('Words for emancipation',
      [('contraband', 'Butler at Fort Monroe, May 1861'),
       ('Emancipation Proclamation', 'January 1, 1863, and its printed limits')],
      "These definitions match the guided notes word for word. Copy them exactly, and notice how much of the lesson each one carries: the first names the legal fiction that let freedom begin before any law allowed it, and the second names the measure itself, with the areas it reached and the areas it deliberately did not, stated in the definition's own terms. " + vocab_join(['contraband', 'Emancipation Proclamation']))

# 25 VOCAB B
vocab('Words for the soldiers',
      [('United States Colored Troops', 'some 180,000 men, equal pay June 1864'),
       ('54th Massachusetts', 'Fort Wagner, July 18, 1863')],
      "Two more terms, again matching the guided notes exactly. The first names the regiments collectively, with the number who served and the battles the definition itself chooses as its evidence. The second names the one regiment this lesson followed in detail, and its definition carries the assault on Fort Wagner and the argument that assault answered, that Black men would not fight, in a single sentence students should be able to reproduce. " + vocab_join(['United States Colored Troops', '54th Massachusetts']))

# 26 VOCAB C
vocab('Words for the turning',
      [('Gettysburg', 'July 1 to 3, 1863, the invasion stopped'),
       ('Vicksburg', 'surrendered July 4, 1863, the river held'),
       ('Gettysburg Address', 'November 19, 1863, two minutes')],
      "Three more terms, again matching the guided notes exactly, and the set of seven is complete with these. " + vocab_join(['Gettysburg', 'Vicksburg', 'Gettysburg Address']))

# 27 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did emancipation change what the war was for, and for whom? Argue it from the records, with the proclamation\u2019s terms and limits, the soldiers\u2019 record, and the year\u2019s resistance.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Emancipation File: the Proclamation, the broadside, the Address, Robinson, and the draft riots summary, with a verdict on purpose or instrument'),
        ('Notebook', 'Notebook page: the transformation charted by record, actor, and change'),
        ('Quick check', 'Freedom Declared, Freedom Fought For: the proclamation read closely, its limits, and the turning of 1863'),
        ('Writing', 'Purpose or Instrument: the verdict argued in about 300 words, with the limits carried, not footnoted')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the proclamation in one sentence with its limits, the Colored Troops\u2019 record and pay, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Emancipation File, runs five stations: the Emancipation Proclamation and the Gettysburg Address from the audited bank records, Douglass's 'Men of Color, To Arms!' broadside as the bank record presents it, Robinson's Pictures of Slavery and Anti-Slavery as the bank presents it, a defense of slavery published in Philadelphia in 1863, and the draft riots record as a labeled teaching summary built from the public record, ending in a verdict on whether emancipation had become the war's purpose or its instrument. The notebook page charts the transformation by record, actor, and change. The quick check tests the proclamation read in its own words, its limits, and the turning of 1863, tagged to blueprint entries 13 and 14. The writing task requires the same verdict argued at essay length. The exit ticket has three parts: the proclamation defined in one sentence including its limits, the Colored Troops' record with the pay figures, and the lesson question in two or three sentences using one fact of the change and one of the strain.")

dc.save(OUT)
