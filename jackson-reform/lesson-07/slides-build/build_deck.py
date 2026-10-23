#!/usr/bin/env python3
"""Jackson and Reform Lesson 7 deck, Abolition Turns Immediate."""
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
text(s, 0.9, 5.32, 11.5, 0.4, 'JACKSON AND REFORM \u00b7 LESSON 7', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Abolition Turns Immediate', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Walker, Garrison, Southampton, and the witnesses, 1829 to 1845', size=17, color=POWDER)
notes(s, "The image is the antislavery emblem as the American Anti-Slavery Society printed it at New York in 1837, a woodcut held by the Library of Congress and in the public domain. Open by placing this lesson after Lesson 6. The Second Great Awakening taught converts that sin was a choice and that society could be reformed by organized effort, and the reform societies of that lesson supplied this one with its methods and many of its people. This lesson asks what happened when one movement applied that logic to slavery without a timetable. For two generations the respectable antislavery position had been gradual emancipation paired with colonization. In six years, from 1829 to 1835, a free Black pamphleteer, a Boston editor, and an enslaved preacher in Virginia ended that position's respectability, and the country spent the next decade answering them.")

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("What changed when abolitionists stopped asking gradually, and how did the country answer?", {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ("What did democracy mean in Jackson's America, who was it for, and what did the era's reformers claim it still owed?", {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Read the question in its two halves and keep both alive all hour. The first half is about a change inside the movement: the demand itself changed its tense, from a request that slavery end someday, by stages, with the freed people removed, to a charge that slavery was a sin requiring an ending now. The second half is about the response, and students should be warned that the response is evidence too. Governments do not gag petitions they are ignoring, and mobs do not drag editors whose papers nobody reads. By the end of the hour students should be able to name the change in the demand, Walker in 1829 and Garrison in 1831 at its head, and the country's three answers: tighter codes after Southampton, a gag in Congress from 1836, and a southern defense rebuilt to promise slavery permanence instead of an ending.")

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'The asking stops, the answers harden', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The old answer: gradual, and gone', 'Gradual emancipation and colonization, fifty years of growth'),
        ('B', 'Walker speaks first, 1829', 'A free Black voice, addressed to Black readers'),
        ('C', 'Garrison recants, 1831', 'The Liberator, a recantation, immediatism named'),
        ('D', 'Southampton, August 1831', 'Turner, about sixty killed, Virginia debates and closes'),
        ('E', 'Organization, print, and the petitions', 'A thousand societies, the mails, the gag rule'),
        ('F', 'Women and witnesses', "Grimk\u00e9 to southern women, Douglass and his literacy"),
        ('G', 'The country answers', 'Codes, mobs, and slavery defended as a positive good')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This slide is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A states the old answer fairly before pricing it. Section B gives the turn its first voice, a free Black writer speaking to Black readers in 1829. Section C names the doctrine, immediatism, through the editor who recanted gradualism in print. Section D holds the Southampton rising and Virginia's double answer, a debate held and then closed for good. Section E follows the movement's machinery, its societies, its mail, and its petitions, into the gag rule. Section F widens the witness stand, to a Charleston daughter and a Maryland fugitive. Section G collects the country's answers and the changed defense they built.")

# 4 A DIVIDER
divider_photo('emblem-port.jpg', 'Section A', 'The Old Answer: Gradual, and Gone',
              ['The antislavery emblem, printed by the American', 'Anti-Slavery Society, 1837. Library of Congress.'],
              "The image is the American Anti-Slavery Society's emblem print of 1837, held by the Library of Congress: a kneeling enslaved man asking whether he is not a man and a brother. The design was older than the republic's antislavery societies, first cut for the British abolition movement, and American printers reused it for decades because it asked slavery's question in the form slavery's defenders found hardest to refuse, a request for recognition as a man. Hold the image against this section's subject. The old antislavery worked in exactly this posture, asking. It petitioned, it proposed timetables, it asked enslavers to consent to freedom by stages and asked the freed to leave the country. Section A states that answer in its own terms, because students cannot measure the turn of 1829 until they see what was being turned from, or how reasonable its makers believed it was.")

# 5 A CONTENT
content_text('Fifty years of asking, slavery growing',
             ['Gradual emancipation: freedom by stages',
              'Colonization after 1816: removal to Liberia',
              'The freed asked to surrender their country',
              '1830: just over two million enslaved',
              'Cotton made slavery richer, not weaker'],
             "Teach the old answer with respect before teaching its failure, because its makers included men who hated slavery and its failure is the lesson's premise. Gradual emancipation freed nobody living: it freed future children, at set ages, across decades, and it asked enslavers to consent in legislatures they often controlled. Colonization, organized in the American Colonization Society from 1816, added removal: free Black people would be carried to Liberia, in Africa, a scheme that asked the people slavery had wronged to surrender their country as the price of a partial freedom. Then set the record beside the design. The census of 1830 counted just over two million enslaved people, and the cotton economy was spreading slavery southwest and enriching the men who held slaves. Fifty years of gradualism had not shrunk slavery. It had accompanied its growth, and the next sections introduce the generation that said so in print.",
             kick='A \u00b7 The old answer', size=23)

# 6 STAT TWO MILLION
stat('2 million', 'enslaved people counted in the census of 1830',
     'Just over two million, after fifty years of gradual emancipation schemes',
     "Let the number do its own work for a full minute before moving on. Two million is not an abstraction when students price it against the old answer's timetable. Gradual laws in the northern states had taken a generation to free far smaller enslaved populations, and those laws are the honest success gradualism could point to. In the South of 1830 no state was on such a timetable at all. Colonization, the plan's second half, had carried some thousands of free Black emigrants to Liberia across its whole career, against an enslaved population growing by tens of thousands a year through natural increase alone. Students do not need rhetoric to see the arithmetic failing. They need the two figures side by side, the millions held and the thousands removed, and the understanding that abolition's young radicals of the next sections began from this arithmetic, not from impatience alone.",
     kick='A \u00b7 The old answer')

# 7 B DIVIDER
divider_text('Section B', 'Walker Speaks First, 1829',
             'A free Black pamphlet, addressed to Black readers, carried south in clothing.',
             "Section B corrects the order in which this story is usually told, and the correction is the section's teaching. The turn to immediatism did not begin with a white editor in 1831. It began in September 1829 with David Walker, a free Black dealer in used clothing in Boston, born free in Wilmington, North Carolina, to an enslaved father and a free mother. His Appeal was addressed to the colored citizens of the world, and that address is its first argument: Walker did not petition white conscience, he instructed Black judgment. Teachers should also be plain about the record's limits. No likeness of Walker exists from his lifetime, and this deck shows none. He is present in this lesson the way he was present in 1829, in print that other people carried at real risk from port to port.")

# 8 B CONTENT
content_text('Are we men: the Appeal and its argument',
             ['Walker, a free Black Boston clothing dealer',
              'The Appeal, September 1829, four articles',
              'Worse than Egypt, worse than Rome',
              'No master but Jesus Christ alone',
              'Carried south, sewn into clothing'],
             "Work the Appeal's argument in its own order, as Station 1 of the activity prints it. Walker begins from condition: colored people in the United States are the most degraded, wretched, and abject set of beings that ever lived since the world began. He then runs the comparison his classical readers could not dodge, setting American slavery beside the Israelites in Egypt, the Helots in Sparta, and the slaves of Rome, and judging the ancient sufferings a cypher beside the American. The conclusion is jurisdictional. If the enslaved have no master but Jesus Christ alone, then obedience to enslavers is not a duty God imposed but a submission men enforce, and it can be withdrawn. Note the intended readers throughout. Every sentence is aimed over the heads of white gatekeepers at the people slavery claimed could not read it, which is precisely why southern ports answered it with law.",
             kick='B \u00b7 Walker speaks first', size=23)

# 9 C DIVIDER
divider_photo('garrison-port.jpg', 'Section C', 'Garrison Recants, 1831',
              ['William Lloyd Garrison, by Nathaniel Jocelyn, 1833.', 'Public domain.'],
              "The portrait is Nathaniel Jocelyn's Garrison of 1833, painted two years after the first issue of The Liberator, when its sitter was twenty seven and already the most argued about editor in the country. Section C studies the movement's most public act of self correction. On January 1, 1831, the first number of The Liberator opened with an editorial titled To the Public, and its centerpiece was not an attack on slaveholders but a confession: the editor withdrew, in print, a position he had himself preached eighteen months earlier. Students should notice what a recantation does that a change of mind does not. It names the old belief, calls it sin, asks pardon of named parties, and prints the apology where enemies can quote it back forever. Garrison built his paper's authority out of that exposure, and this section reads the editorial closely.")

# 10 C CONTENT
content_text('A recantation in the first issue',
             ['The Liberator, Boston, January 1, 1831',
              'Recants gradual abolition, assented to in 1829',
              'Timidity, injustice, and absurdity',
              'Pardon asked of God, country, and the enslaved',
              'Contends for immediate enfranchisement'],
             "Read the recantation's pieces slowly, in the bank record's words, which the quick check also uses. Garrison tells his readers that in Park-street Church on the Fourth of July, 1829, he unreflectingly assented to the popular but pernicious doctrine of gradual abolition. He seizes the first issue of his own paper to make a full and unequivocal recantation, asking pardon of his God, of his country, and of his brethren the poor slaves, for a sentiment full of timidity, injustice, and absurdity. In its place he contends strenuously for the immediate enfranchisement of the slave population, on the Declaration's ground that all men are created equal. Then close with the vow students will meet at Station 2: he will not equivocate, will not excuse, will not retreat a single inch, and he will be heard. The tone was a strategy, and its costs belong to Section G.",
             kick='C \u00b7 Garrison recants', size=23)

# 11 STAT 1833
stat('1833', 'the American Anti-Slavery Society founded at Philadelphia',
     'December 1833: immediatism given an organization, local societies, and a press',
     "Pause on the interval between the doctrine and the institution, because students tend to merge them into one event. Garrison's recantation is January 1831. The American Anti-Slavery Society is December 1833, nearly three years later, and the gap is the difference between a position and a movement. A position needs a writer. A movement needs local societies that meet in winter, agents who travel and are sometimes mobbed for it, presses, fairs, and petition tables, and a treasury. The Society supplied that machinery, and by the late 1830s more than a thousand local societies existed across the North. Note also who staffed the machinery. Women, barred from the platform in these years, ran much of the petitioning and fund raising, a fact Section F builds on when two of them take the platform anyway and change what the movement could say.",
     kick='C \u00b7 Garrison recants')

# 12 D DIVIDER
divider_text('Section D', 'Southampton, August 1831',
             'Nat Turner, the last open debate, and the codes drawn tighter.',
             "Section D requires the room's full steadiness, and it should be taught plainly and without decoration. In August 1831, eight months after The Liberator began, Nat Turner, an enslaved preacher of Southampton County, Virginia, led the deadliest slave rebellion in United States history. Turner left no writing of his own. Everything this lesson can say about his mind comes through The Confessions of Nat Turner, the pamphlet a Southampton lawyer, Thomas Gray, took down from him in jail, published, and sold, a mediation Station 3 of the activity puts on the record's face. No likeness of Turner exists from his lifetime, and this deck shows none. What the section can teach with confidence is the sequence: the rising, the retaliation, Virginia's last open debate on emancipation, and the closing of the southern codes.")

# 13 D CONTENT
content_text('The rising, and the winter after it',
             ['Turner: an enslaved preacher who could read',
              'August 21 and 22, 1831, Southampton County',
              'About sixty white people killed',
              'Retaliation killed many more Black people',
              'Virginia debates emancipation, votes it down'],
             "Teach the sequence in order and keep every number in its place. Turner believed signs in the heavens had appointed him, and on the night of August 21 and into August 22 his band killed about sixty white people before militia and armed residents crushed the rising within two days. Retaliation followed, killing many more Black people, most of whom had taken no part in the rising at all. Turner was captured in October and hanged on November 11. Then teach the winter, because it is the section's hinge. Virginia's legislature debated ending slavery openly in the winter of 1831 and 1832, the last such debate in the slaveholding South, and voted the proposals down. The ruling that followed ran the other way: southern states tightened their slave codes against preaching, assembly, and the printed word. The debate happened. Students should know it happened, and that it was ended by vote, not by silence.",
             kick='D \u00b7 Southampton', size=23)

# 14 STAT SIXTY
stat('about 60', 'white people killed in the Southampton rising',
     'August 21 and 22, 1831: the deadliest slave rebellion in United States history',
     "Give this figure its full weight without display. About sixty white people were killed in Southampton, among them women and children, in their homes, over two days, and the county's terror at the fact is part of the historical record students must hold. The record's other side must be held in the same breath: the retaliation killed many more Black people than the rising had killed white people, most of them uninvolved, and the trials that followed were conducted by the county whose residents had done the killing. Immediatists and slaveholders both built arguments on Southampton for a decade, the one side hearing slavery's violence answered, the other hearing proof that slavery had to be guarded harder. Students should be able to state the figure, the dates, and both readings, and to notice that neither reading is a justification. The unit test will price sequence and causation here, not sensation.",
     kick='D \u00b7 Southampton')

# 15 E DIVIDER
divider_text('Section E', 'Organization, Print, and the Petitions',
             'A thousand societies, a flood of mail, and a rule against being heard.',
             "Section E follows the movement's machinery into the one arena where the Constitution gave ordinary people, including women who could not vote, a formal instrument: the petition. The American Anti-Slavery Society understood print as logistics. In 1835 it sent abolitionist literature through the federal mails by the sackful, aimed at southern readers, and southern postmasters, with the Postmaster General's knowledge, let the sacks be seized and burned. Petitioning scaled the same way: signatures by the hundreds of thousands, gathered door to door, a great share of them women's, went up to Congress session after session. Section E ends where that machinery met the House of Representatives in May 1836, and where a former president, now a congressman, decided the right of petition itself was worth a decade of procedural war.")

# 16 E CONTENT
content_text('Petitions by the hundreds of thousands',
             ['Local societies: more than a thousand by 1838',
              '1835: the great postal campaign',
              'Mail sacks seized and burned in the South',
              'Petitions: hundreds of thousands of signatures',
              'Women gathered many of them, door to door'],
             "Work the machinery piece by piece, because scale is the argument. A local society was small: a town's worth of members, dues, a lending shelf of pamphlets, and a petition table after services. Multiplied past a thousand, it became a national organization without a national office doing the daily work. The postal campaign of 1835 tested whether federal channels could carry abolition into the South, and the answer, seizure and burning with official consent, told abolitionists the mails were federal only where the South allowed. The petitions tested the other channel. Signing cost little and meant something precise: it asked Congress to act against slavery where Congress constitutionally could, in the District of Columbia and the territories, and it created lists of the committed in every northern town. When the House moved against the petitions in 1836, it was answering a machinery it could count, in signatures, by the hundred thousand.",
             kick='E \u00b7 Organization and petitions', size=23)

# 17 STAT GAG
stat('1836 to 1844', 'the gag rule years in the House of Representatives',
     'Every antislavery petition tabled without printing, reading, or debate',
     "State the gag's working exactly, since the vocabulary definition at the end of this deck will ask for it. From May 1836 the House rule laid every petition touching slavery on the table automatically: not received into debate, not printed, not referred, not read aloud. Petitions kept arriving anyway, session after session, and John Quincy Adams, the former president now representing Massachusetts, made himself the rule's procedural enemy, presenting petitions through every device the rules left open and forcing the House to censure, debate, and finally, in December 1844, repeal the gag. Teach the repeal as Adams's victory and the movement's education in one. Eight years of gagging had advertised the petitions more widely than reading them would have, a lesson in how suppression certifies the importance of what it suppresses, and students will meet the same mechanism in the southern laws against Walker's pamphlet.",
     kick='E \u00b7 Organization and petitions')

# 18 F DIVIDER
divider_photo('grimke-port.jpg', 'Section F', 'Women and Witnesses',
              ['Angelina Grimk\u00e9, wood engraving, Library of Congress.', 'Public domain.'],
              "The portrait is a wood engraving of Angelina Grimké held by the Library of Congress. Section F asks who got to testify. The immediatist movement's first voices were an editor and a pamphleteer, both arguing about slavery from outside the household that practiced it. Grimké argued from inside: raised in a Charleston slaveholding family, she left the South, joined the movement, and in 1836 published her Appeal to the Christian Women of the South, asking the wives, mothers, sisters, and daughters of slaveholders to read, pray, speak, and act. The engraving's date should be stated honestly: it is a later print likeness, reproduced widely in the nineteenth century, not a sitting from 1836. With her sister Sarah, Grimké then lectured to audiences that mixed men and women, and the clergy who ordered women silent gave the next lesson, Seneca Falls, its opening argument.")

# 19 F CONTENT
content_photo_s('douglass-port.jpg', 'A narrative that answered by existing',
             ['Escaped from Maryland, 1838',
              'Discovered as an orator, 1841',
              'The Narrative, 1845, under his own name',
              "Chapter VII: bread traded for lessons",
              'Literacy itself as the argument'],
             "The photograph is Samuel J. Miller's daguerreotype of Frederick Douglass, made between 1847 and 1852, held by the Art Institute of Chicago; Douglass sat for portraits deliberately and often, understanding what a fugitive's composed likeness argued. Chapter VII of the Narrative, Station 4 of the activity, tells how the argument was built. Sent to Baltimore, Douglass was begun in the alphabet by his mistress, Sophia Auld, until her husband forbade it, teaching the household that literacy and slavery could not coexist. Douglass finished the work himself, trading bread to poor white boys for lessons in the street. His judgment on his mistress carries the chapter: slavery proved as injurious to her as to him, her tender heart became stone, and the first step in her downward course was ceasing to instruct him. Print that sentence beside the proslavery claim the vocabulary closes with, that the enslaved could not speak for themselves, and let students watch the Narrative answer it.",
             kick='F \u00b7 Women and witnesses')

# 20 G DIVIDER
divider_text('Section G', 'The Country Answers',
             'Mobs in the North, a new defense in the South, and no more promises of an ending.',
             "Section G collects the answers, and teachers should resist letting the class file them as mere backlash. Each answer taught the country something about the turn's reach. The mobs were northern as often as southern: Boston dragged Garrison in 1835, and Alton, Illinois, killed the editor Elijah Lovejoy over his press in 1837, which means immediatism frightened communities that held no slaves and profited from slavery's cotton and credit at a distance. The southern answer ran deeper than violence. A generation of southern leaders had called slavery a necessary evil their fathers had inherited and time would end. That apology required gradualism to answer to. Once abolition demanded immediacy and Southampton had happened, the apology was withdrawn, and Section G closes with the replacement doctrine southern leadership built in its place.")

# 21 G CONTENT
content_text('Necessary evil becomes positive good',
             ['1835: a Boston mob drags Garrison with a rope',
              '1837: Lovejoy killed defending his press at Alton',
              '1837: Calhoun, in the Senate, a positive good',
              'A proslavery literature grows to argue it',
              'The defenders stop promising an ending'],
             "Put the pivot sentence on the board and make students copy it whole: the defense of slavery changed its ground. John C. Calhoun, whose nullification doctrine Lesson 3 studied, told the Senate in 1837 that slavery was not a necessary evil to be apologized for but a positive good to be defended, and southern writing took up the argument in books and reviews across the following decade. Read the pivot against the turn's demands. Gradualism had always rested on a shared fiction between the sections, that slavery was temporary and everyone regretted it. Immediatism called the fiction a lie in print, weekly, for years, and after Southampton the South stopped paying for the fiction's upkeep. Abolitionists remained a minority, disliked in both sections, and students should not inflate them. But the debate after 1837 ran on ground the immediatists had cleared, between a demand for slavery's immediate end and a defense that promised it would never end at all.",
             kick='G \u00b7 The country answers', size=23)

# 22 STAT 1837
stat('1837', 'slavery defended in the Senate as a positive good',
     'The year of Calhoun and his speech, and of Lovejoy and his press at Alton',
     "Hold this year up as the lesson's verdict in a single date. In February 1837 John C. Calhoun rose in the Senate and declared the relation between the races, as southern slavery held it, a good, a positive good, the foundation, he argued, of southern wealth and stability. In November of the same year a mob at Alton, Illinois, shot Elijah Lovejoy dead as he defended his fourth press, the first three having been thrown into the Mississippi. A free state killed an editor for printing abolition in the same year the Senate heard slavery praised as a blessing, and students should sit with the pairing before judging the era's direction. Neither event freed an enslaved person. Both events are facts about what the turn had made unsayable and sayable: gradual apology unsayable in the Senate's new doctrine, and abolitionist print worth killing over on the free banks of the Mississippi.",
     kick='G \u00b7 The country answers')

# 23 GLANCE
s = slide(NAVY)
kicker(s, 'The turn at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Four rows, one turn', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The old answer', 'Gradual emancipation and colonization', 'Fifty years, and two million enslaved in 1830'),
        ('The turn in print', 'Walker 1829, Garrison 1831', 'Immediatism: end it now, as a sin'),
        ('Southampton', 'August 1831, about sixty killed', 'The last debate, then tighter codes'),
        ('The petitions', 'Mails seized 1835, gagged 1836', 'Adams wins repeal, December 1844')]
yy = 2.72
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 0.88
notes(s, "This slide mirrors the final table in the guided notes, The Turn at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The rows compress the arc the lesson has built. The old answer row pairs gradualism's fifty years against the census of 1830, refusing to let the scheme stand without its result. The print row holds the sequence Walker before Garrison, the order the unit test will price. The Southampton row states the toll and Virginia's double answer in one breath, the debate and the codes, because either fact alone distorts the winter of 1831. The petitions row ends the table on a repeal, December 1844, the one answer the country eventually withdrew. Grade the table generously on wording and strictly on pairing: every row must show the demand and the answer together, not either one alone.")

# 24 SYNTHESIS
content_text('What the turn changed, and what it could not',
             ['Changed: the demand, from someday to now',
              'Changed: the speakers, Walker to Douglass',
              'Changed: the defense, evil confessed to good proclaimed',
              'Unchanged: slavery itself, growing through the decade',
              'Left standing: the argument, on new terms'],
             "Draw the lesson together around the question's two halves, because the exit ticket and the writing task both return to them. The turn was real, and students should give it its full weight first. It changed abolition's demand from a timetable to a verdict, changed who could make the argument, from colonization societies to a free Black pamphleteer, a Charleston daughter, and a fugitive with his own name on a title page, and it changed the opposition, forcing slavery's defense off apology and onto a claim of positive good. Then price it without flinching. Slavery itself did not shrink in the 1830s; it grew, enriched its holders, and tightened its codes, and abolitionists were a hated minority at the decade's end. What the turn won was the terms. After it, no national argument about slavery could return to the gradual fiction, because both sides had publicly burned it. That is the ground the next unit inherits.",
             kick='Synthesis', size=23)

# 25 VOCAB A
vocab('Words for the turn',
      [('abolition', 'the movement, turned in the 1830s from gradual to immediate'),
       ("Walker's Appeal", "Walker's pamphlet of 1829, smuggled south"),
       ('William Lloyd Garrison', 'The Liberator, 1831, and the Society built on it'),
       ('immediatism', 'end it at once: no stages, no payment, no removal')],
      "These definitions match the guided notes word for word. Copy them exactly. abolition: the movement to end slavery in the United States, which in the 1830s turned from the gradual emancipation and colonization schemes of the founding generation to the demand that slavery, as a sin, end immediately and without compensation to the enslaver. Walker's Appeal: the pamphlet David Walker, a free Black clothing dealer of Boston, published in 1829 and smuggled into the South, which called on enslaved people to resist their enslavement and warned white Americans that their professions of freedom stood condemned by their practice. William Lloyd Garrison: the Boston editor who founded The Liberator in 1831, renounced gradualism and colonization in its first issue, and built the American Anti-Slavery Society into the organizational engine of immediatist abolition. immediatism: the abolitionist doctrine of the 1830s that slavery, being a sin against God and man, must end at once, without gradual stages, compensation, or the removal of the freed people, the doctrine that split the antislavery movement from its colonizationist past.")

# 26 VOCAB B
vocab('Words for the answer',
      [('Nat Turner', 'Southampton, August 1831, and the codes that followed'),
       ('gag rule', 'petitions tabled unread, 1836 to 1844, Adams against it'),
       ('Frederick Douglass', 'escaped 1838, orator 1841, the Narrative of 1845')],
      "Three more terms, again matching the guided notes exactly, and the set of seven is complete with these. Nat Turner: the enslaved preacher of Southampton County, Virginia, who in August 1831 led the deadliest slave rebellion in United States history, in which about sixty white people were killed, after which Virginia and the southern states tightened their slave codes and ended open debate on emancipation. gag rule: the rule by which the House of Representatives from 1836 to 1844 tabled every antislavery petition without printing, reading, or debate, which former president John Quincy Adams, serving in the House, fought year after year as a violation of the right of petition until its repeal. Frederick Douglass: the Maryland fugitive who escaped slavery in 1838, was discovered as an orator by the Massachusetts Anti-Slavery Society in 1841, and published his Narrative in 1845, a first person account whose literacy and argument answered the slaveholders' claim that the enslaved could not speak for themselves.")

# 27 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['What changed when abolitionists stopped asking gradually, and how did the country answer? Argue it from the records, with dates, audiences, and the changed defense.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', "The Immediatism File: Walker, Garrison, Turner's Confessions, Douglass, and Grimk\u00e9, with a verdict on which record ended the gradual era"),
        ('Notebook', 'Notebook page: the turn charted by demand, audience, and answer'),
        ('Quick check', 'The Asking Stops: the recantation read closely, and the turn and its answer in sequence'),
        ('Writing', 'What Changed When the Asking Stopped: one witness followed through the change that witness worked')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: immediatism in one sentence, the gag rule and its years, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Immediatism File, runs five stations: Walker's Appeal and Garrison's To the Public from the audited bank records, the Confessions of Nat Turner in the Documenting the American South transcription with Gray's mediation stated on the station's face, chapter VII of Douglass's Narrative from the same collection, and Grimké's Appeal of 1836 in the Project Gutenberg transcription, ending in a verdict on which record did most to end the era of gradual asking. The notebook page charts the turn by demand, audience, and answer. The quick check tests the recantation read in its own words and the turn in sequence, tagged to blueprint entries 13 and 14. The writing task requires one witness followed through the change that witness worked. The exit ticket has three parts: immediatism defined in one sentence, the gag rule with its years and its opponent, and the lesson question in two or three sentences using one fact of the turn and one of the answer.")

dc.save(OUT)
