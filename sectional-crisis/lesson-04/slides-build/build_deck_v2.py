#!/usr/bin/env python3
"""Sectional Crisis and Civil War Lesson 4 deck, The Republican Party and Dred Scott,
built to the approved system: image-led slides, fragments only on screen,
comprehensive speaker notes, full lesson and vocabulary coverage.
Fonts: Georgia titles, Lato body."""
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
OUT = os.path.join(HERE, '..', 'lesson-04-slides.pptx')

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

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'SECTIONAL CRISIS AND CIVIL WAR · LESSON 4', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Republican Party and Dred Scott', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'A new party, a voided platform, and a settlement that settled nothing', size=17, color=POWDER)
notes(s, "The title image is an election poster for John C. Fremont from 1856, the Republican Party's first national campaign, held by the Library of Congress and reproduced from its public domain scan. Open with the lesson's two actors facing each other. On one side, a political party built in a single season, in 1854, out of the wreckage of the Kansas-Nebraska fight, promising one act of Congress. On the other side, the Supreme Court of the United States, which in March 1857 declared that the one act could never lawfully be done and that the people at the center of the quarrel were not citizens at all. The lesson question asks what the party promised and what the Court tried to settle, and every section that follows is one side or the other making its claim.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("What did the Republican Party promise, and what did the Supreme Court try to settle in Dred Scott?", {})]],
     size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ("How did compromise over slavery finally fail, and what did the war it caused settle about slavery and the Union, and what did it leave open?", {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "The lesson question is built in two halves, and students should keep them separate all period. What the Republican Party promised is a question about politics: a coalition of former enemies agreeing on one plank, that Congress must bar slavery from the federal territories, and running a presidential campaign on it within two years. What the Supreme Court tried to settle is a question about law used as a substitute for politics: Chief Justice Taney's opinion of March 6, 1857 attempted to remove the slavery question from elections altogether by deciding, as constitutional law, that Black people could not be citizens and that Congress had never held the power the party proposed to use. The unit question stands behind both halves, because this lesson is where compromise stops failing one act at a time and starts failing as a method.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'One plank, one lawsuit, one decree', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'A party built from a repeal', 'Anti-Nebraska meetings name a party, 1854'),
        ('B', 'The free labor creed', 'Honorable labor, rising, and its shadow'),
        ('C', 'The first campaign, 1856', 'Fremont carries eleven of sixteen free states'),
        ('D', "Dred Scott's case", 'Free soil residence; suit of 1846; eleven years'),
        ('E', 'The decision, March 6, 1857', 'No citizenship; no free soil freedom; no power'),
        ('F', 'The dissents and the answers', 'Curtis from the record; Douglass in private'),
        ('G', 'The settlement that settled nothing', 'House Divided, 1858; a president on the platform, 1860')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "The map follows the guided notes section by section. Section A builds the party from the repeal of the Missouri Compromise line in 1854. Section B gives the free labor creed under its single plank, and names the Black exclusion inside that creed. Section C runs the first campaign, Fremont in 1856, and reads the returns as both sections read them. Section D follows Dred Scott from Missouri to Illinois and Fort Snelling and into an eleven year lawsuit. Section E states Taney's three holdings of March 6, 1857. Section F carries Curtis's dissent and Douglass's answer. Section G closes with Lincoln's House Divided speech and the fate of a settlement that lasted three years before the party it voided won the presidency on the voided platform.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_photo('poster-port.jpg', 'Section A', 'A Party Built from a Repeal',
              ['The Kansas-Nebraska Act repealed a thirty four year old line,', 'and the North answered by building a party.'],
              "The image is a portrait crop of the 1856 Fremont election poster students saw on the title slide, printed in the campaign that proved the new party real. Teach the speed of the thing, because students assume parties grow slowly. The Kansas-Nebraska Act passed in May 1854, repealing the Missouri Compromise line and opening the territories to popular sovereignty. Within months, meetings across the free states were calling themselves Republican, in conscious echo of Jefferson's party, and the coalition they assembled agreed on almost nothing else: dying Whigs, Free Soilers, Democrats breaking with their own administration, temperance voters, and voters suspicious of immigrants. One plank held them together. Congress must bar slavery from the federal territories. Everything else in this lesson follows from how narrow, and how powerful, that single agreement was.",
              title_size=34)

# ------------------------------------------------------ 5 THE COALITION
content_text('One plank, and what it left alone',
             ['It was organized in 1854 from the Kansas-Nebraska fight.',
              'Ex-Whigs, Free Soilers, and anti-Nebraska Democrats joined it.',
              'Its plank held that Congress must bar slavery from the territories.',
              'Slavery stood untouched where state law protected it.',
              'Extension was barred, and slavery put toward ultimate extinction.'],
             "Read the fragments as a bargain, because that is what a coalition is. The men who founded this party had spent careers voting against one another, and the price of standing together was a platform narrow enough for all of them: nothing about slavery in the states, nothing about the Fugitive Slave Act, nothing about citizenship. The plank reached only the federal territories, where Congress plainly governed, and its defenders said the narrowness was strategy rather than timidity. Slavery barred from spreading, they argued, would be placed in the course of ultimate extinction, dying over a generation without a single state law touched. Notice also what the bargain made the party: the first successful wholly northern party in the country's history, a fact Section C's election map will make vivid.",
             kick='A · A party built from a repeal', size=24)

# ------------------------------------------------- 6 SECTION B DIVIDER
divider_text('Section B', 'The Free Labor Creed',
             'Labor honorable, the laborer free to rise, the territories as the ladder, and exclusion standing in the creed as its shadow.',
             "Introduce the creed as the party's account of why the plank mattered, because a platform sentence alone does not move voters. Free labor was the North's self image argued as economics: work was honorable, wages were a stage rather than a fate, and a laborer who saved could buy land in the territories and become independent, as could his sons. Slavery, in this telling, was not only cruel. It degraded work by marking labor as the business of the enslaved, and it let great slaveholders monopolize the common lands that should have made poor men into owners. Then name the shadow before students romanticize the creed. Free soil often meant soil kept free of Black people. Oregon and Indiana wrote Black exclusion into law, and many a Republican voter wanted the territories closed to slavery and to Black families in the same vote.")

# ------------------------------------------------------ 7 FREE LABOR
content_text('The creed and its shadow',
             ['Labor was honorable, and the laborer had a right to rise.',
              'Wages, savings, land, and independence formed the ladder.',
              'Slavery degraded work itself, the creed said.',
              'Slaveholders monopolized the common lands.',
              'The shadow was that Oregon and Indiana excluded Black settlers.'],
             "Take the fragments in two groups. The first four state the creed as its believers preached it, and it deserves to be stated at full strength, because it explains the party's energy better than antislavery conscience alone: millions of northern voters who would never call themselves abolitionists believed their own sons' chances depended on keeping the territories free for free labor. The fifth fragment is the limit, and the lesson states it without softening. The free labor argument was an argument about opportunity for white laborers, and it coexisted, in the same voters and sometimes the same speeches, with laws excluding free Black people from whole states. Students who hold both groups together understand the Republican Party of 1856 as it was, neither the abolition party of later memory nor a fraud, but a coalition whose promise and whose boundary were drawn by the same hand.",
             kick='B · The free labor creed', size=24)

# ------------------------------------------------- 8 SECTION C DIVIDER
divider_photo('fremont-port.jpg', 'Section C', 'The First Campaign, 1856',
              ['The Pathfinder runs, and a party with no southern wing', 'comes within reach of the presidency at its first attempt.'],
              "The portrait is John C. Fremont photographed by Mathew Brady, the explorer and army officer the party nominated in 1856, known across the country as the Pathfinder for his western expeditions. The nomination itself states the party's position. Fremont was famous and carried no congressional record to defend, no votes on Kansas, no speeches an opponent could quote back at him. He was a westerner for a party whose promise was about western land. What the party needed to learn from 1856 was not whether its candidate could win a debate. It was whether the electoral map would let a party that existed only in the free states win the presidency at all. The returns answered that question so clearly that both sections reorganized their politics around the answer.",
              title_size=34)

# ------------------------------------------------------ 9 THE CAMPAIGN
content_text('1856: the returns teach the arithmetic',
             ['Fremont, the Pathfinder, was the first nominee.',
              'He carried eleven of the sixteen free states.',
              'Buchanan won on Pennsylvania and the South.',
              'No southern strength was needed, only a held North.',
              'Southern editors read the same map as a warning.'],
             "Walk the returns rather than the campaign speeches, because the map is the evidence. Fremont carried eleven of the sixteen free states in the party's first national run. James Buchanan won the presidency on Pennsylvania and the South, and Democrats treated the result as relief. Read it as Republicans read it: one more large free state in their column in 1860, and a party drawing nothing from the slave states would hold the presidency, and with it the patronage, the courts' future vacancies, and the territorial question itself. Southern editors drew the identical conclusion in the opposite mood, and some began saying in print that a Republican victory in 1860 would be grounds for leaving the Union. The threat of secession as an answer to an election enters the record here, four years before it is used.",
             kick='C · The first campaign, 1856', size=24)

# ------------------------------------------------------ 10 STAT 11
stat('11 of 16', 'free states carried by Fremont in 1856',
     'A purely northern party, within reach of the presidency in its first campaign',
     "State the fraction slowly, because it is the lesson's political engine. Sixteen free states voted in 1856, and the Republican nominee, a man who had never held elective office, carried eleven of them in his party's first attempt at the presidency. He won not one slave state and was not seriously competing in any. Under the electoral college's arithmetic, that performance, repeated with Pennsylvania or one more large state added, wins. Every politician in both sections could do this sum, and the four years after 1856 are unintelligible without it: the South's increasing demand for guarantees, the Democratic split over a federal slave code, and the Republican confidence that holding the North together was a complete national strategy. A party sectionally confined had become, by arithmetic, a governing party in waiting.",
     kick='C · The first campaign, 1856')

# ------------------------------------------------- 11 SECTION D DIVIDER
divider_photo('scott-port.jpg', 'Section D', "Dred Scott's Case",
              ['Enslaved in Missouri, carried to free soil twice,', 'and suing for a family, eleven years in the courts.'],
              "The image is the portrait of Dred Scott reproduced by the New York Historical Society, the man at the center of the case students will read in the activity. Build the human itinerary before the law, because the legal claim is unintelligible without the geography. Scott was enslaved in Missouri and carried by his owner, an army surgeon named John Emerson, to a posting in Illinois, a free state, and then to Fort Snelling, in what is now Minnesota, in territory where the Missouri Compromise barred slavery. He married Harriet at Fort Snelling, and their daughters were born on free soil and in free waters. Brought back to Missouri, Scott sued for the family's freedom in 1846, arguing that residence on free soil had made them free. Owners died, lawyers maneuvered, and the case climbed for eleven years.",
              title_size=34)

# ------------------------------------------------------ 12 THE SUIT
content_photo_s('scott-port.jpg', "Scott's claim: residence had made them free",
             ['He was carried from Missouri to Illinois, a free state, on army postings.',
              'Fort Snelling stood on Missouri Compromise ground.',
              'He married there, and his daughters were born on free soil.',
              'He filed suit in 1846, for himself and his family.',
              'The case ran eleven years of courts while owners died.'],
             "State the claim in its strongest form, because students meet it again in Taney's answer and should know what was being answered. Under the doctrine many courts had applied, an owner who took an enslaved person to live where slavery was barred had, by that voluntary act, freed them, and the freedom held when they returned. Scott had lived for years on free soil, not passed through it: Illinois by its constitution, Fort Snelling by act of Congress. Missouri's own courts had honored this once free, always free reasoning in earlier cases before hardening against it in the 1850s, as the politics around slavery hardened everywhere. That is the quiet fact to leave with the class. Scott's claim was not an invention of abolitionist lawyers. It was an ordinary claim under existing doctrine, and the Supreme Court's decision to take the case, and then to reach far beyond it, is what requires explanation.",
             kick="D · Dred Scott's case", size=24)

# ------------------------------------------------------ 13 STAT 11 YEARS
stat('11', 'years from Scott filing suit to the decision',
     '1846 to 1857 · The case outlived its first owner and outgrew one family',
     "Eleven years is the second number to fix in memory. Dred Scott filed in a Missouri court in 1846, when the question of slavery in the territories was still managed by the Missouri line and the parties still straddled the sections. By the time the Supreme Court answered in March 1857, the line had been repealed, Kansas had bled, a sectional party had been built, and a president had been elected partly on that party's near victory. The delay shaped the case in two ways. First, it let the case gather meanings no single family could carry: by 1857 politicians in both sections expected the Court's answer to settle the territorial question itself. Second, it taught Scott himself the distance between law as a remedy and law as an instrument. He was freed by purchase, by the family of his original owner, in May 1857, weeks after the decision, and died the following year, a free man by transaction rather than by judgment.",
     kick="D · Dred Scott's case")

# ------------------------------------------------- 14 SECTION E DIVIDER
divider_photo('taney-port.jpg', 'Section E', 'The Decision, March 6, 1857',
              ['Two days after the inauguration, the Chief Justice', 'attempts to settle the slavery question by decree.'],
              "The portrait is Roger B. Taney photographed by Mathew Brady, the Maryland chief justice who had succeeded John Marshall in 1836 and who wrote the opinion students read at Station 1 of the activity. Set the scene with care. James Buchanan was inaugurated on March 4, 1857, and said in his address that the territorial question would be settled speedily and finally by the Supreme Court, a remark worth pausing on, since the president knew the decision was coming and said so in public. Two days later the Court delivered it. Taney was eighty years old, a former slaveholder who had freed the people he held, and by his own account he meant the opinion as a settlement: the Court would declare what the Constitution had always said, and politics would obey. The next three slides state what he declared.",
              title_size=32)

# ------------------------------------------------------ 15 THE HOLDINGS
content_photo_s('taney-port.jpg', 'Three holdings, in the order Taney made them',
             ['Black people were not, and could not be, citizens.',
              'Residence on free soil had not freed Scott.',
              'The Missouri Compromise had always been unconstitutional.',
              'Congress had never had power over slavery in the territories.',
              'The Republican platform itself stood voided.'],
             "Read the holdings as a sequence, because the order is part of the act. The citizenship holding came first and was, by itself, enough to dismiss the case: if Scott was not a citizen, no federal court could hear him. The residence holding followed, Scott remaining enslaved under Missouri law on his return. The third holding reached furthest: the Missouri Compromise had been void from 1820, because Congress possessed no power to bar slavery from the territories, enslaved people being property the Constitution protected. That holding did not decide Scott's case, which was already decided twice over. It decided the Republican Party's case, declaring its single plank unconstitutional. Justice Curtis's dissent, in Section F, objects to precisely this reach, the majority examining an act of Congress it had no need to examine after its first holding.",
             kick='E · The decision of March 6, 1857', size=24)

# ------------------------------------------------------ 16 STAT 7 TO 2
stat('7 to 2', 'the majority that signed the settlement',
     'McLean and Curtis dissenting · Curtis from the ratification record itself',
     "Seven to two is the count to hold against the word settlement. A settlement, in the sense Taney intended, requires the losing side to accept the instrument as final, and the opinion was built to compel acceptance: the majority spoke broadly, on citizenship, on the territories, on the meaning of the founding, so that no electoral result could lawfully disturb it. But two justices dissented at length, and Curtis's dissent did the one thing a settlement cannot survive. It contested the majority's facts from the same record the majority claimed to read, showing free Black citizens voting in five states at ratification. From the day of publication, therefore, the decision carried its own refutation between the same covers, and opponents did not need to defy the Court to attack it. They needed only to quote the junior document bound with it.",
     kick='E · The decision of March 6, 1857')

# ------------------------------------------------- 17 SECTION F DIVIDER
divider_text('Section F', 'The Dissents and the Answers',
             'Curtis answers from the franchise rolls of 1788, Douglass answers from his own life, and neither accepts the decree as the end.',
             "Frame this section as the decision failing in real time, because students tend to imagine Dred Scott standing unopposed until Lincoln. It did not. Inside the Court, Justice Benjamin Curtis of Massachusetts dismantled the citizenship holding with the founding generation's own record, and Justice John McLean dissented with him. Outside it, Frederick Douglass, the most famous Black man in the country and therefore a living test of the opinion's central sentence, answered in speeches that refused the despair the decision was calculated to produce, and wrote, in the same year, the private letter students read at Station 3, asking his former master for the date of his own arrival in that household as a child. The two answers are different in kind, one legal and one human, and the lesson needs both.")

# ------------------------------------------------------ 18 CURTIS
content_text("Curtis's answer: the founding record itself",
             ['Free Black men had voted in five original states.',
              'They were New Hampshire, Massachusetts, New York, New Jersey, and North Carolina.',
              'They were citizens who ordained the Constitution.',
              'Nothing in the Constitution stripped that citizenship.',
              'The majority had reached a question it need not decide.'],
             "Teach the dissent as a method, not only a conclusion. Taney's citizenship holding rested on a claim about opinion: that at the founding, Black people had been regarded as beings of an inferior order, everywhere and without exception. Curtis answered with acts rather than opinions. At ratification, free Black men possessed the elective franchise in five of the thirteen original states, which means they were citizens of those states, voters on the very instrument that created United States citizenship, and part of the people who ordained it. A Constitution ordained in part by Black citizens could not, without a clause saying so, have excluded Black people from the people forever, and Curtis wrote that he could find no such clause and no power in Congress to create the exclusion. Then his second point, jurisdictional and colder: having held Scott could not sue, the majority had no business voiding the Missouri Compromise at all.",
             kick='F · The dissents and the answers', size=24)

# ------------------------------------------------------ 19 DOUGLASS
content_photo('douglass-port.jpg', "Douglass's answer: a letter, not a brief",
             ['It was written to Hugh Auld, his former master, in 1857.',
              'It was private, and stated in the letter to be so.',
              'It asked the year he came to Aliceanna Street.',
              '"I love you, but hate Slavery" was the sentence that separated the man from the system.'],
             "The image is Frederick Douglass in a daguerreotype of the early 1850s, held by the Metropolitan Museum of Art and released under CC0. Use this slide to slow the class down. The letter at Station 3 argues nothing about the Constitution, and grading should honor that: Douglass writes to the man who once held him as property to ask a fact about his own childhood, the year he came to live on Aliceanna Street, because the records of an enslaved child's life were kept by the household that owned him. He writes with courtesy, distinguishes the man from the system in a single sentence, ran not from Auld but from slavery, and refuses to publish what he learns. Set beside Taney's description of Black people as merchandise, the letter is evidence of the plainest kind: the excluded class, writing its own history, in its own hand.",
             kick='F · The dissents and the answers')

# ------------------------------------------------- 20 SECTION G DIVIDER
divider_photo('lincoln-port.jpg', 'Section G', 'The Settlement That Settled Nothing',
              ['June 1858: Lincoln accepts a Senate nomination', 'and answers a court with a speech about a house.'],
              "The portrait is Abraham Lincoln photographed by Samuel Alschuler in 1858, beardless, as he looked when he delivered the speech this section teaches. Place Lincoln where the lesson puts him: not yet a president, not yet even a senator, an Illinois lawyer who had served one term in the House a decade earlier and had risen, on the Kansas-Nebraska fight, to lead his state's Republicans. In June 1858 the party nominated him to challenge Stephen Douglas, and his acceptance speech at Springfield opened with a sentence taken from the Gospels that named the whole crisis in a domestic image. Some of his own advisers thought the speech too radical and said so. Lincoln kept the sentence, and the decision to keep it is a fair measure of the man the party was learning it had.",
              title_size=32)

# ------------------------------------------------------ 21 HOUSE DIVIDED
content_photo_s('lincoln-port.jpg', 'House Divided: the design Lincoln charged',
             ['A house divided against itself could not stand.',
              'The government could not endure permanently half slave and half free.',
              'It would become all one thing, or all the other.',
              'Repeal, decision, and policy were parts of one design.',
              'Slavery would be made national, or placed toward extinction.'],
             "Read the speech's logic as Lincoln built it at Station 2 of the activity. He reduces the Dred Scott decision to two points, that a Black person cannot be a citizen and that neither Congress nor a territory can bar slavery from the territories, and assigns each a purpose inside a larger movement: the Kansas-Nebraska repeal opening the territories, the decision constitutionalizing slavery there, and, he warns, a next decision that could make slavery lawful in the free states themselves. Whether a coordinated design existed is a question students may argue; the documents show separate acts, not correspondence. What is beyond argument is the effect of the charge. It told Republicans that the decision was not a settlement to obey but a move to counter, and it framed the election of 1860 before that election had candidates.",
             kick='G · The settlement that settled nothing', size=19)

# ------------------------------------------------------ 22 AT A GLANCE
s = slide(NAVY)
kicker(s, 'The party and the decision at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'A promise, a decree, an answer', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A party and its creed', 'Organized 1854; Fremont, 1856', 'One plank, free labor, and exclusion inside it'),
        ('The case', 'Suit of 1846; Illinois and Fort Snelling', 'Residence on free soil claimed as freedom'),
        ('The decision', 'March 6, 1857; Taney, 7 to 2', 'No citizenship, no free soil freedom, no congressional power'),
        ('The answers', 'Curtis and Douglass, 1857; Lincoln, 1858', 'The franchise record, a private letter, one design charged')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.2, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.25, yy + 0.05, 5.1, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.55, yy + 0.05, 3.9, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the closing table of the guided notes, The Party and the Decision at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. A party and its creed: organized in 1854 on the plank that Congress must bar slavery from the territories, resting on free labor, and carrying Black exclusion within it, with Fremont carrying eleven of sixteen free states in 1856. The case: Scott's 1846 suit on his residence in Illinois and at Fort Snelling. The decision: Taney's three holdings of March 6, 1857, by seven to two. The answers: Curtis from the ratification record, Douglass from his own life, and Lincoln's House Divided charge of one design, followed in 1860 by the voided party electing a president on the voided platform.")

# ------------------------------------------------------ 23 VOCAB A
vocab('Words for the party and its creed',
      [('Republican Party', 'organized in 1854, on one plank'),
       ('free labor', 'the northern creed under the plank'),
       ('John C. Fremont', 'the Pathfinder, nominee in 1856'),
       ('Dred Scott v. Sandford', 'the decision of March 6, 1857')],
      "Four terms, in full. Republican Party: the party organized in 1854 from the wreckage of the Kansas-Nebraska fight, joining ex-Whigs, Free Soilers, and anti-Nebraska Democrats on the single plank that Congress must bar slavery from the federal territories, the first successful wholly northern party in the country's history. free labor: the northern creed that labor was honorable, that the laborer had a right to rise by his work to property and independence, and that slavery degraded work and monopolized the common lands, the economic faith under the Republican Party's promise of free soil. John C. Frémont: the explorer and army officer called the Pathfinder, the Republican Party's first presidential nominee in 1856, who carried eleven of the sixteen free states and showed both sections that a purely northern party could nearly win the presidency. Dred Scott v. Sandford: the Supreme Court decision of March 6, 1857, in which Chief Justice Taney held that Black people could not be citizens of the United States, that residence on free soil had not freed Dred Scott, and that Congress had never had power to bar slavery from the territories.")

# ------------------------------------------------------ 24 VOCAB B
vocab('Words for the judge and the answer',
      [('Roger B. Taney', 'chief justice, author of the opinion'),
       ('Abraham Lincoln', 'Illinois lawyer, nominee in 1858'),
       ('House Divided speech', "Lincoln's address of June 16, 1858")],
      "Three more terms, in the guided notes wording, carried in full. Roger B. Taney: the Maryland chief justice who succeeded John Marshall in 1836 and wrote the Dred Scott opinion, attempting to settle the slavery question by constitutional decree and instead voiding the Republican platform and deepening the crisis he meant to end. Abraham Lincoln: the Illinois lawyer and former one term congressman who rose on the Kansas-Nebraska fight to lead his state's Republicans, debated Douglas across Illinois in 1858, and was elected the sixteenth president in 1860 on the platform of barring slavery from the territories. House Divided speech: Lincoln's address of June 16, 1858, accepting the Republican nomination for the Senate, which argued that the government could not endure permanently half slave and half free and charged that the Nebraska repeal and the Dred Scott decision were parts of one design to make slavery national. Notice the arc the three terms draw: the judge who decreed, the lawyer who answered, and the speech in which the answer was made.")

# ------------------------------------------------------ 25 CLOSING SYNTHESIS
s = slide(NAVY)
kicker(s, 'Closing synthesis')
text(s, 0.9, 1.35, 11.5, 1.1, 'Two findings, held together', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 2.6,
     ["The Court spoke with finality on citizenship, on free soil, and on Congress, and a justice inside the same building answered its history from the ratification record.",
      "Within three years the party whose platform the decree voided elected a president on that platform, and the Union the decree was written to preserve had begun to dissolve."],
     size=23, color=POWDER, leading=1.3)
notes(s, "Close the lesson by holding the two findings together, because the verdict work is graded on exactly that. The first finding is legal and internal: Taney's opinion claimed to report a uniform founding settlement on Black citizenship, and Curtis's dissent, published with it, produced five states whose franchise rolls contradicted the uniformity, which is why opponents could attack the decision without defying the Court's authority in form. The second finding is political and external: a decree against a rising party's one promise did not retire the promise. It certified the party's importance, handed Lincoln the design argument of the House Divided speech, and set the terms on which the election of 1860 was fought. Students who hold only the first finding have a courtroom story. Students who hold only the second have a campaign story. The lesson's question needs both: what the Court tried to settle, and why settling it there failed.")

# ------------------------------------------------------ 26 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ["What did the Republican Party promise, and what did the Supreme Court try to settle in Dred Scott? Judge the decision from the documents, account for Curtis's dissent, and state what became of the settlement."],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Dred Scott File: the opinion, the speech, the letter, the platform, the dissent'),
        ('Notebook', 'Notebook page: the party, the case, the decision, and the answers in stages'),
        ('Quick check', 'The Platform and the Dissent: the promise of 1856 beside the record of 1788'),
        ('Writing', 'Misreading or Honest Logic: your verdict defended from the file')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the party and free labor defined, the three holdings in two sentences, and the lesson question answered.',
     size=15, color=POWDER)
notes(s, "Close the lesson by handing the verdict to the students, which is what this lesson exists to do. The activity, The Dred Scott File, gives them Taney's majority opinion and Lincoln's House Divided speech and Douglass's letter to Hugh Auld from the audited bank records, the Republican platform of 1856 in the American Presidency Project transcription, and Curtis's dissent in a transcription of the United States Reports text, and asks them to judge whether the decision was a misreading of the Constitution or its proslavery logic read honestly to its end. The notebook page charts the party, the case, the decision, and the answers in stages. The quick check sets the platform beside the dissent. The writing task asks for the verdict defended against its strongest rival, with the voided platform and Curtis's franchise record carried at full strength. The exit ticket has three parts: the party and free labor defined, the three holdings stated in two sentences, and the lesson question answered with both findings held together.")

dc.save(OUT)
