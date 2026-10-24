#!/usr/bin/env python3
"""Sectional Crisis Lesson 5 deck, "The Debates, John Brown, the Election of
1860, and Secession," built on the unit's shared deck system."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags, photo_right,
                         divider_photo, content_photo, content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED, W, H)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

dc.IMG = os.path.join(HERE, 'img')
OUT = os.path.join(HERE, '..', 'lesson-05-slides.pptx')
HAS_LINCOLN = os.path.exists(os.path.join(dc.IMG, 'lincoln-port.jpg'))
HAS_BROWN = os.path.exists(os.path.join(dc.IMG, 'brown-port.jpg'))
HAS_DOUGLAS = os.path.exists(os.path.join(dc.IMG, 'douglas-port.jpg'))

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
    frags(s, items, y=2.12 if kick else 2.0, size=size, gap=11, leading=1.2)
    notes(s, note)
    return s

# 1 TITLE
s = slide(NAVY)
if HAS_LINCOLN: photo_right(s, 'lincoln-port.jpg')
text(s, 0.9, 1.5, 6.9, 0.4, 'SECTIONAL CRISIS AND CIVIL WAR · LESSON 5', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 2.0, 6.9, 2.2, 'The Debates, John Brown, and Secession', size=44, color=CREAM, font='Georgia', leading=1.1)
rule(s, 0.92, 4.15)
text(s, 0.9, 4.5, 6.8, 1.6, 'How the argument of 1858 became the break of 1860 and 1861', size=20, color=POWDER, leading=1.3)
notes(s, "Open with the names in the title, because this lesson is a chain with four links and every link is a person speaking or acting in public. In 1858 Abraham Lincoln and Stephen A. Douglas debated across Illinois and fixed the terms of the slavery argument. In 1859 John Brown acted on the argument with a rifle and then explained himself to a court. In 1860 the argument elected a president it could not contain. In 1861 the states that lost that election explained their departure in documents students will read word for word. Tell the class the lesson question now, and tell them the writing task will ask which single turn closed the road to compromise, defended from these records alone and from no later story about them.")

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did the argument of 1858 become the break of 1860 and 1861?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ("How did compromise over slavery finally fail, and what did the war it caused settle about slavery and the Union, and what did it leave open?", {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Read the question slowly, because its dates are its argument. The argument of 1858 is the Lincoln-Douglas debates, seven meetings that settled nothing and decided the terms of everything after. The break of 1860 and 1861 is the election, the secessions, and the founding of a rival government, all inside fourteen months. Between the argument and the break stand two events students must weigh as causes: the Freeport Doctrine, which split a national party over a sentence, and John Brown's raid, which split the sections' pictures of each other over a night. The unit question behind it asks how compromise over slavery finally failed. This lesson is where it failed, in public, in documents the class can hold. Keep both questions in view all hour, because every section of the lesson answers the first and feeds the second.")

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'An argument becomes a break', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'Seven meetings on the prairie', 'Seven towns; three hours each; 1858'),
        ('B', 'Freeport and the Doctrine', "Douglas's answer; the South forfeited"),
        ('C', 'The racial ground', "Charleston and Peoria, held together"),
        ('D', 'The raid on Harpers Ferry', 'October 16, 1859; twenty two men'),
        ('E', 'The trial and the gallows', 'A martyr, and an invasion'),
        ('F', 'Four parties and an election', '39.8 percent; no southern state'),
        ('G', 'Secession in its own words', 'The declaration; the cornerstone; the fort')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A sets the debates and their scale. Section B isolates the Freeport question and Douglas's answer. Section C states the racial ground of the debates plainly, with both of Lincoln's positions held together. Section D follows Brown into Harpers Ferry. Section E follows him to the gallows and weighs the two verdicts the sections passed on him. Section F counts the election of 1860. Section G reads secession in the seceding states' own words and ends on the fort in Charleston harbor, where the next lesson begins.")

# 4 A DIVIDER
divider_text('Section A', 'Seven Meetings on the Prairie',
             'Seven towns, three hours each, and a question crowds stood in fields to hear argued.',
             "Begin with scale, because the debates are easy to shrink into two men talking and they were a national season. Seven meetings, one in each congressional district but two, spread across Illinois from August 21 to October 15, 1858. Each lasted three hours, with crowds standing in the open air, sometimes in rain, and the speeches were printed whole in newspapers across the country and read far beyond Illinois. Douglas was the incumbent, the Senate's leading Democrat, the author of the Kansas-Nebraska Act and of popular sovereignty. Lincoln was a former one term congressman who had never won a statewide race, leading a party organized only in 1854. Section A asks what such meetings could decide when the office itself was filled by the legislature, not by the crowds.")

# 5 A CONTENT
content_photo_s('lincoln-port.jpg', 'Seven towns, three hours each',
             ['They met at Ottawa, Freeport, Jonesboro, and Charleston.',
              'They met at Galesburg, Quincy, and Alton.',
              'The format ran an hour, an hour and a half, and half an hour.',
              'The debates were printed whole in newspapers nationwide.',
              'Douglas kept the seat, and Lincoln won the audience.'],
             "Work the mechanics first. The format was set by agreement: Douglas spoke an hour, Lincoln answered for an hour and a half, Douglas closed for half an hour, alternating who opened. Stenographers took every word, and partisan newspapers printed rival texts, which is why the debates survive entire. The crowds were not decoration. Tens of thousands stood for three hours because the question under the speeches, whether slavery would spread into the territories and become national, decided what kind of country their farms and towns would sit in. Note the result honestly: Douglas kept the seat, because the legislature's districts favored his party. Lincoln lost the office and won the argument's audience, and in 1860 the same two men met again for a larger prize.",
             kick='A · Seven meetings', size=24)

# 6 B DIVIDER
if HAS_DOUGLAS:
    divider_photo('douglas-port.jpg', 'Section B', 'Freeport and the Doctrine',
             ['One question, prepared in advance, and an answer that saved a seat and forfeited a section.'],
             "Now narrow the whole campaign to one exchange, because one exchange is what history kept. At Freeport, the second debate, on August 27, Lincoln put to Douglas a question prepared with his advisers and aimed past Illinois. The Supreme Court had held in Dred Scott that Congress could not bar slavery from a territory, and the logic of the decision reached territorial legislatures too. Lincoln asked whether the people of a territory could still lawfully exclude slavery, against the wishes of a slaveholder who settled there, before the territory became a state. Everyone in the crowd understood the trap. An answer of no would destroy Douglas in Illinois. An answer of yes would destroy him in the South. Section B is the answer he chose.")
else:
    divider_text('Section B', 'Freeport and the Doctrine',
             'One question, prepared in advance, and an answer that saved a seat and forfeited a section.',
             "Now narrow the whole campaign to one exchange, because one exchange is what history kept. At Freeport, the second debate, on August 27, Lincoln put to Douglas a question prepared with his advisers and aimed past Illinois. The Supreme Court had held in Dred Scott that Congress could not bar slavery from a territory, and the logic of the decision reached territorial legislatures too. Lincoln asked whether the people of a territory could still lawfully exclude slavery, against the wishes of a slaveholder who settled there, before the territory became a state. Everyone in the crowd understood the trap. An answer of no would destroy Douglas in Illinois. An answer of yes would destroy him in the South. Section B is the answer he chose.")

# 7 B CONTENT
content_photo_s('douglas-port.jpg', 'The Freeport Doctrine',
             ['The Court had spoken in Dred Scott.',
              'Could a territory still keep slavery out?',
              'Slavery needed local police laws to live.',
              'Refuse the laws, and slavery stayed out.',
              'Illinois approved, and the South demanded a code.'],
             "State the doctrine exactly as the Key Terms carry it, because the unit test will ask for it as a definition. Douglas answered that slavery cannot exist anywhere unless it is supported by local police regulations, and that a territorial legislature could therefore keep it out, in effect, by refusing to pass the laws it needed, whatever the Supreme Court had decided about the right. Unfriendly legislation, he said, would keep slavery out as surely as a constitutional ban. The answer was clever, popular in Illinois, and fatal elsewhere. Southern leaders read it as nullification of their constitutional victory, and within two years they were demanding the opposite doctrine in their platform, a federal slave code that would protect slavery in the territories by national law against local refusal.",
             kick='B · Freeport', size=24)

# 8 B STAT
stat('7', 'open air debates across Illinois, August to October 1858',
     'Three hours each, before crowds in the tens of thousands, and printed whole for the nation',
     "Give the number its weight. Seven debates in nine weeks is a campaign form the country had never seen at this scale, two candidates for the Senate arguing one question in the open air for three hours at a time while the nation read along. The form mattered as much as the content. Because every word was printed, a Senate race in Illinois became a national seminar on the territories, and arguments built for Freeport and Charleston were weighed in Charleston, South Carolina, and in Washington. When students ask why a state campaign belongs in a unit about the Union breaking, the answer is on this slide: the debates nationalized the argument, made Lincoln a national figure, and gave the South a text, the Freeport Doctrine above all, to answer in 1860.",
     kick='B · Freeport')

# 9 C DIVIDER
divider_text('Section C', 'The Racial Ground of the Debates',
             "Both men's words on race, stated plainly, because the record holds them and this lesson does not soften them.",
             "This section states the debates' racial ground without softening, and the class should hear why. Lincoln and Douglas argued before white voters in a state that barred Black settlement by law and denied Black men the vote. Both men spoke to that audience's assumptions. Douglas built his campaign on the open claim that the government was made for white men and that Black people were permanently inferior. Lincoln denied any purpose of social and political equality and assigned the superior position to the white race, and in the same speeches called slavery a moral wrong and defended the Black man's natural rights. Section C holds both halves of that record together, because quoting either half alone is how this campaign is misread.")

# 10 C CONTENT
content_text('Charleston, stated plainly',
             ['He had no purpose of social and political equality.',
              'A physical difference would stand forever.',
              'The superior position belonged to the white race.',
              'Douglas charged Lincoln with preaching equality.',
              'The audience was white voters in a free state.'],
             "Teach the Charleston statements in Lincoln's own sequence, as the reading states them. He had no purpose to bring about social and political equality between the races. He believed a physical difference between them would forever forbid their living together on a footing of perfect equality. And since some difference must exist, he said, he favored having the superior position assigned to the white race, as Douglas did. Do not hurry past this slide or apologize for it. Students who meet these sentences first in this lesson will not be ambushed by them in a document later, and they will understand Douglas's strategy, which was to make Lincoln answer for an equality Lincoln had publicly disavowed, because Douglas's voters feared that equality more than they feared slavery's extension.",
             kick='C · The racial ground', size=24)

# 11 C CONTENT 2
content_text('Peoria, held beside it',
             ['Slavery was a moral, social, and political wrong.',
              'The nation had no right to spread it.',
              'Stopping the spread was the road to its final end.',
              'Every man held the right to the bread his own hand earned.',
              "Both statements were Lincoln's."],
             "Now set beside Charleston the position Lincoln had argued at Peoria in October 1854, when the Kansas-Nebraska Act brought him back into politics, and which he never withdrew. Slavery, he held, was a moral, social, and political wrong. The nation had no right to extend it. The policy of his party was to restore the Missouri restriction, stop the spread, and place slavery where the public mind could rest in the belief that it was in the course of ultimate extinction. At Ottawa he gave the claim its smallest form: the Black man is not his equal in color or endowment, but in the right to eat the bread his own hand earns, he is the equal of every living man. The debates live in the space between this slide and the last one.",
             kick='C · The racial ground', size=24)

# 12 D DIVIDER
if HAS_BROWN:
    divider_photo('brown-port.jpg', 'Section D', 'The Raid on Harpers Ferry',
             ['Twenty two men, a federal arsenal, and a rising that did not come, October 16 to 18, 1859.'],
             "John Brown enters the lesson out of Lesson 3, where the class met him at Pottawatomie in 1856, and out of the conviction he had carried for years, that slavery would end only in blood. By 1859 he had money from northern abolitionist backers, a plan drafted at a convention in Canada, and a target chosen with care. Harpers Ferry, in Virginia where the Potomac and Shenandoah meet, held a federal arsenal and armory, rifles in storehouses a short march from enslaved communities, with mountains behind it for a campaign of liberation. On the night of Sunday, October 16, 1859, Brown led twenty one men across the bridge from Maryland, five of them Black, and seized the town and the arsenal before morning. Section D is what the plan met.")
else:
    divider_text('Section D', 'The Raid on Harpers Ferry',
             'Twenty two men, a federal arsenal, and a rising that did not come, October 16 to 18, 1859.',
             "John Brown enters the lesson out of Lesson 3, where the class met him at Pottawatomie in 1856, and out of the conviction he had carried for years, that slavery would end only in blood. By 1859 he had money from northern abolitionist backers, a plan drafted at a convention in Canada, and a target chosen with care. Harpers Ferry, in Virginia where the Potomac and Shenandoah meet, held a federal arsenal and armory, rifles in storehouses a short march from enslaved communities, with mountains behind it for a campaign of liberation. On the night of Sunday, October 16, 1859, Brown led twenty one men across the bridge from Maryland, five of them Black, and seized the town and the arsenal before morning. Section D is what the plan met.")

# 13 D CONTENT
content_photo_s('brown-port.jpg', 'The night of October 16',
             ['The arsenal was seized before morning.',
              'The telegraph was cut, and a train let through.',
              'Heyward Shepherd was the first man killed.',
              'No rising came.',
              'Militia came by daylight, and marines to storm it.'],
             "Walk the night in order. The raiders cut the telegraph, seized the watchmen, and took the arsenal and rifle works without a fight. A party under John Cook captured Colonel Lewis Washington at his nearby estate and freed the people he enslaved. Then the plan stalled on its own mercy and confusion. Brown let an eastbound train pass, and the train carried the alarm down the line. The first man killed was Heyward Shepherd, a free Black railroad porter shot on the bridge by the raiders, a fact students should sit with, because the rising's first victim was a free Black worker. By daylight the town was armed, militia companies were arriving by rail, and enslaved people had not risen, because no rising had been told to expect them.",
             kick='D · Harpers Ferry', size=24)

# 14 D STAT
stat('22', 'men in John Brown\'s party at Harpers Ferry, Brown among them, five of them Black',
     'Ten were killed in the raid; seven more, Brown among them, were hanged after trial',
     "Count the party, because its size is the plan's confession. Twenty two men, counting Brown, five of them Black, among them a formerly enslaved man, Shields Green, and men who had followed Brown from Kansas and Canada. Against them stood a town, then militia from two states, then the United States Marines. Brown expected the enslaved of the surrounding country to multiply his twenty two into an army once the arsenal's rifles were in their hands, and he had brought pikes for men who could not handle rifles. The arithmetic never began. Ten of the twenty two were killed in the raid, and seven more were hanged after trial, Brown among them, while five escaped. The number teaches what the raid was: not an army beaten in the field, but a summons almost no one heard in time.",
     kick='D · Harpers Ferry')

# 15 E DIVIDER
divider_text('Section E', 'The Trial, the Gallows, and the Note',
             'The courtroom made Brown louder than the raid had, and the two sections judged him in opposite words.',
             "Capture made Brown more dangerous to the Union than the raid had, because Virginia gave him a courtroom, a trial the newspapers covered line by line, and a month between sentence and execution in which to write letters. He had been carried into court on a cot, wounded in the storming of the engine house, and tried for treason against the Commonwealth of Virginia, conspiracy, and first degree murder. The trial's speed, a week from indictment to verdict, troubled northern opinion, and Brown's conduct through it, calm, direct, and without self pity, did the rest. Section E centers on November 2, when the court asked the formal question whether he had anything to say why sentence should not be pronounced, and Brown rose and answered in the speech students read at Station 3.")

# 16 E CONTENT
content_text('Brown to the court, November 2',
             ['He admitted one design, to free the enslaved.',
              'He denied murder and insurrection.',
              'The same act, done for the rich, would be called reward.',
              "He rested on the Bible's two teachings.",
              'He submitted, and let it be done.'],
             "Teach the address as an argument, not as a prophecy. Brown admits one design, to free enslaved people, as he had done in Missouri the winter before, and denies murder, treason, and insurrection. He then turns the court's own standard on it: had he interfered for the rich, the powerful, the intelligent, the so called great, the same act would have been deemed worthy of reward rather than punishment. He rests on the book kissed in the courtroom, the Bible, its Golden Rule and its command to remember them that are in bonds. And he closes by submitting to the sentence as a furtherance of the ends of justice, mingling his blood with the blood of millions whose rights are disregarded. The speech is in the activity entire, in a named transcription, because its force is in its sentences.",
             kick='E · The trial', size=24)

# 17 E CONTENT 2
content_text('A martyr, and an invasion',
             ['Northern bells tolled on December 2.',
              'Republican leaders condemned the raid.',
              'The South read proof of invasion.',
              'Militia companies formed that winter.',
              "They became secession's first regiments."],
             "The two verdicts arrived before the body was buried. In the North, on December 2, church bells tolled, shops closed in some towns, and Brown was mourned as a martyr and a saint of the antislavery cause, though Republican leaders, Lincoln among them, condemned the raid itself as wrong and futile. In the South the same weeks brought the opposite reading: Brown was proof that abolition meant invasion, that northern money and northern sympathy stood behind the rifle, and that the Union now sheltered the South's enemies. Militia companies formed across the South that winter, drilling for the next raid, and those companies were still organized when secession came a year later. Section E's point is causal: the raid settled nothing about slavery and everything about what each section believed the other intended.",
             kick='E · The trial', size=24)

# 18 F DIVIDER
divider_text('Section F', 'Four Parties and an Election',
             'The argument of 1858, counted in November 1860, and answered the next month.',
             "The election of 1860 was decided by the argument of 1858 before a vote was cast, and Section F shows the mechanism. The Democratic Party met at Charleston in April 1860 and split when southern delegates demanded that the platform pledge a federal slave code for the territories, the direct answer to the Freeport Doctrine. The convention adjourned without a nominee, met again at Baltimore, split again, and produced two Democratic candidates, Douglas for the North and Vice President John C. Breckinridge for the South. John Bell ran on the Union alone for a fourth party. The Republicans at Chicago nominated Lincoln on the single plank the whole crisis had built, no extension of slavery into the territories. Four candidates, and only one question under all of them.")

# 19 F CONTENT
content_text('Four candidates, one question',
             ['Lincoln stood for no extension of slavery.',
              'Douglas stood for popular sovereignty.',
              'Breckinridge stood for a federal slave code.',
              'Bell stood for the Union alone.',
              'Lincoln won 180 electoral votes on 39.8 percent.'],
             "Count the result as the sections counted it. Lincoln won 180 electoral votes, a clear majority, with 39.8 percent of the popular vote, carrying every free state but one, which he split with Douglas. Breckinridge carried the deep South, Bell the border states of Virginia, Kentucky, and Tennessee, and Douglas, second in popular votes, won only Missouri outright. Lincoln received no electoral vote from the South and was not even on the ballot in ten slave states, where Republican organizations barely existed. Southern readers did the same arithmetic as northern ones: a party with no southern wing, no southern votes, and no southern obligations had won the government on a platform that named slavery a wrong and barred its spread. The election was constitutional in form and sectional in fact, and both halves of that sentence drove what followed.",
             kick='F · The election', size=24)

# 20 F STAT
stat('39.8%', 'of the popular vote elected Abraham Lincoln president in 1860',
     'A clear majority of the electoral college, no southern state, and no ballot place in ten slave states',
     "Hold this number up because it is the break in one figure. Thirty nine point eight percent is a minority of the nation's votes, and it was enough, because the majority was divided among three candidates and because Lincoln's votes stood exactly where electoral votes were thickest, in the free states. No fraud, no accident, and no technicality made Lincoln president. The rules of the Constitution, applied to a party system the slavery argument had shattered, produced a sectional president lawfully. That is why the number belongs beside the secession documents. South Carolina's declaration does not claim the election was stolen. It claims that a sectional party, observing the forms of the Constitution, had found the means of subverting it, which is a more dangerous charge, and students should be made to find it in the text.",
     kick='F · The election')

# 21 G DIVIDER
divider_text('Section G', 'Secession Answers in Its Own Words',
             "South Carolina's declaration, the failed compromise, the new government, and its cornerstone.",
             "The last section reads secession in the seceding states' own words, because the unit's central question, what the war was about, must be answered first from what those states said when they left. South Carolina went first, on December 20, 1860, by a unanimous convention vote, and published its Declaration of the Immediate Causes four days later. Mississippi, Florida, Alabama, Georgia, Louisiana, and Texas followed by February 1. The documents are not shy, and this lesson does not summarize them into safer language. Students read South Carolina's declaration at Station 4 and Stephens's cornerstone at Station 5, verbatim from the audited bank records. Section G follows the sequence: the declaration, the last compromise, the new government, and its own explanation of itself.")

# 22 G CONTENT
content_text("South Carolina's case",
             ['The Union was a compact among states.',
              'The fugitive clause had been broken for years.',
              'Fourteen states were named.',
              'A president hostile to slavery had been elected.',
              'South Carolina was therefore released from her obligation.'],
             "State South Carolina's case as the declaration states it, in its own order. The Constitution was a compact among sovereign states. Its fourth article promised that persons held to service or labor, escaping into another state, would be delivered up on claim. Fourteen northern states had deliberately refused that obligation for years, passing personal liberty laws that nullified the federal acts. The northern states had denounced slavery as sinful, sheltered abolition societies, and assisted thousands of enslaved people to escape. And now a sectional party had elected a president hostile to slavery, who would take the government on March 4 announcing the South's exclusion from the common territory. Therefore the compact was broken by the North, and South Carolina was released from her obligation. The argument is legal in form and entirely about slavery in content.",
             kick='G · Secession', size=24)

# 23 G CONTENT 2
content_text('The last compromise fails',
             ['Crittenden offered the Missouri line, unamendable.',
              'Lincoln instructed that there be no compromise on extension.',
              'The plan failed in January.',
              'Montgomery produced a constitution and a president.',
              'Jefferson Davis was chosen on February 9.'],
             "Two attempts to stop the sequence failed inside these same weeks, and students should name both. The Crittenden Compromise, offered by Senator John J. Crittenden of Kentucky in December, would have written the Missouri line into the Constitution as an unamendable amendment, protecting slavery south of 36 degrees 30 minutes forever and forbidding Congress to touch it. Lincoln, still a private citizen in Springfield, instructed Republican senators in writing to entertain no proposition for a compromise on the extension of slavery, and the plan failed in January. The Washington peace conference of February failed likewise. Meanwhile the seven seceded states met at Montgomery, Alabama, adopted a constitution modeled on the federal one, and on February 9 chose Jefferson Davis of Mississippi, a former secretary of war, as their president.",
             kick='G · Secession', size=24)

# 24 G CONTENT 3
content_text('The cornerstone, and the oath',
             ['Stephens spoke at Savannah on March 21.',
              'The question had been put at rest forever.',
              'Inequality was named the foundation.',
              'Lincoln held the Union perpetual.',
              "Fort Sumter's provisions were running out."],
             "End where the lesson's documents end, with the new government explaining itself. On March 21, 1861, at Savannah, Vice President Alexander H. Stephens told his audience that the Confederate constitution had put the slavery question at rest forever, that slavery had been the immediate cause of the rupture, and that the government's cornerstone rests on the great truth that the Black man is not equal to the white man and that slavery is his natural and normal condition. Eleven days earlier Lincoln had taken the oath in Washington, pledged not to interfere with slavery in the states, denied that any state could lawfully leave, and promised to hold federal property. In Charleston harbor the federal garrison of Fort Sumter was counting its provisions. The next lesson opens with the guns.",
             kick='G · Secession', size=24)

# 25 GLANCE
s = slide(NAVY)
kicker(s, 'The argument becomes the break at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Argument, raid, election, departure', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The debates', '1858, seven towns', 'Lincoln made national'),
        ('Freeport', 'One answer', 'A party split in two'),
        ('The racial ground', 'Charleston and Peoria', 'Both statements stand'),
        ('Harpers Ferry', 'October 1859', 'Martyr and invasion'),
        ('The break', '1860 to 1861', 'Departure, in its own words')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=20, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 0.85
notes(s, "This slide mirrors the summary table at the end of the guided notes, The Argument Becomes the Break at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. Read the rows as one chain rather than five summaries. The debates fixed the terms and made Lincoln national. Freeport split the Democracy's future over a single answer. The racial ground row is the chain's honest center: the argument was conducted by both men on white supremacist ground, and the difference between them, containment against extension, was still large enough to break a union over. Harpers Ferry armed the argument. The election counted it, and secession answered the count in its own words.")

# 26 VOCAB A
vocab('Words for the argument',
      [('Lincoln-Douglas debates', 'seven meetings; Lincoln made national'),
       ('Freeport Doctrine', 'refuse the police laws; the seat saved, the South lost'),
       ('Harpers Ferry', 'the arsenal seized, October 16, 1859'),
       ('secession', 'the compact withdrawn from, state by state')],
      "Definitions, verbatim from the guided notes. Lincoln-Douglas debates: the seven open air debates between Abraham Lincoln and Stephen A. Douglas across Illinois in the Senate campaign of 1858, three hours each before crowds in the tens of thousands, which made Lincoln a national figure and fixed the terms of the slavery argument. Freeport Doctrine: Douglas's answer at Freeport in August 1858, that a territory could keep slavery out despite the Dred Scott decision by refusing to pass the local police laws slavery needed to survive, the answer that saved his Senate seat and forfeited the South. Harpers Ferry: the Virginia town at the meeting of the Potomac and Shenandoah rivers, site of the federal arsenal John Brown seized on October 16, 1859, hoping to arm an enslaved rising, and of the engine house where marines under Robert E. Lee captured him two days later. secession: the doctrine and act by which eleven slaveholding states, beginning with South Carolina on December 20, 1860, declared their union with the United States dissolved and withdrew, holding that the Union was a compact from which a state could withdraw as it had entered.")

# 27 VOCAB B
vocab('Words for the break',
      [('Crittenden Compromise', "the last terms, December 1860; failed in January"),
       ('Confederate States of America', 'Montgomery, February 1861; seven states, then eleven'),
       ('Jefferson Davis', 'its president, chosen February 1861')],
      "Three more terms, again matching the guided notes exactly. Crittenden Compromise: Senator John J. Crittenden's last settlement proposal of December 1860, which would have written the Missouri line into the Constitution as an unamendable amendment protecting slavery south of it forever, rejected by the Republicans on Lincoln's instruction and failing in January 1861. Confederate States of America: the government organized at Montgomery, Alabama, in February 1861 by the first seven seceded states, later eleven, with a constitution modeled on the federal one that named slavery's protection in its text where the original had not. Jefferson Davis: the Mississippi senator and former secretary of war chosen president of the Confederate States in February 1861, who directed the Confederacy's war for four years and was captured in Georgia in May 1865 after Richmond fell. Read the set as the lesson's last sequence in three stops: the compromise that failed, the government that replaced the Union in seven states, and the man chosen to lead it.")

# 28 SYNTHESIS
content_text('Judging the chain whole',
             ['Freeport split a national party.',
              "Brown armed the argument's fears.",
              'The declarations stated the grounds.',
              'Every road but departure had closed.',
              'The writing task asks for one turn, defended.'],
             "Close the teaching here, before the work slide, and model the judgment the writing task will ask for. Three turns are on the table. Freeport: a doctrine that saved a Senate seat and split a national party, the mechanism by which a debate answer became an election no compromise candidate could win. Brown: a raid that freed no one and taught each section that the other meant violence, the mechanism by which argument became fear. The declarations: secession defended in the seceders' own words as slavery's defense, the mechanism by which the losing side of an election chose departure over terms. The strongest student writing picks one turn, builds it from at least three of the activity's records, and answers the best case for another turn instead of pretending it is not there.",
             kick='Synthesis', size=24)

# 29 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did the argument of 1858 become the break of 1860 and 1861? Build the file first, then judge from it.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Break File: five stations, a file, and a verdict on 1861'),
        ('Notebook', 'Notebook page: the chain charted in five rows, and the break in one paragraph'),
        ('Quick check', 'Ottawa to Savannah: the debates, the doctrine, the raid, the cornerstone'),
        ('Writing', 'Which Turn Closed the Road: one turn defended from both halves of the bank')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the Freeport Doctrine defined, Lincoln\'s two positions stated together, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Break File, runs five stations: Lincoln's Ottawa reply and Douglas's Ottawa speech, both verbatim from the audited bank records; Brown's address to the court from the named transcription, read for his admission, his objection, and his submission; South Carolina's declaration, read for its fugitive clause case; and Stephens's Cornerstone Speech, read for the foundation he claims. Students build the file in Part 2 and defend a verdict on which record 1861 proved right. The notebook page charts the same five steps. The quick check works from the Ottawa record and the cornerstone. The writing task turns the lesson question into an essay on which turn closed the road to compromise.")

dc.save(OUT)
