#!/usr/bin/env python3
"""Jackson and Reform Lesson 2 deck, "Indian Removal," built to the
approved system: image-led slides, fragments only on screen,
comprehensive speaker notes, full lesson + vocabulary coverage.
Fonts: Georgia titles, Lato body."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags, photo_right,
                         divider_photo, content_photo, content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED, W, H)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

dc.IMG = os.path.join(HERE, 'img')
OUT = os.path.join(HERE, '..', 'lesson-02-slides.pptx')

spec = open(os.path.join(HERE, '..', '..', 'build-scripts', 'unit-spec.md')).read()
l2 = spec.split('### Lesson 2')[1].split('### Lesson 3')[0]
DEFS = {}
for line in l2.splitlines():
    m = re.match(r'- (.+?): (.*)$', line.strip())
    if m: DEFS[m.group(1)] = m.group(2)
assert len(DEFS) == 7, DEFS.keys()

def joined(term):
    return f"{term}: {DEFS[term]}"

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

LQ = 'How did the United States take the Southeast, and what did the Cherokee do to stop it?'
UQ = "What did democracy mean in Jackson's America, who was it for, and what did the era's reformers claim it still owed?"

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'JACKSON AND REFORM · LESSON 2', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Indian Removal', size=38, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'A nation answers with law, and the law is not enforced', size=17, color=POWDER)
notes(s, "The image is George Catlin's Ball-play of the Choctaw, Ball Up, a version the artist painted between 1846 and 1850 of a game he had watched in Indian Territory in the 1830s, held by the Smithsonian American Art Museum. Open with the people, not the policy: the nations in this lesson were societies with governments, schools, farms, and games of their own, and the Choctaw in the picture had already been removed once when Catlin saw them play. Place the lesson in the unit. Lesson 1 closed with a democracy widened for white men and a president governing energetically in the majority's name. This lesson tests that democracy against the people it excluded, and students should leave able to follow removal step by step and to judge whether it was a policy of law or of force.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[(LQ, {})]], size=38, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                (UQ, {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question also has two halves, and students will need both for the exit ticket and the writing task. First, what did the Cherokee do to stop removal? They answered in the republic's own instruments: a constitution and a newspaper that made their nationhood visible, memorials and delegations to Congress, and two cases carried to the Supreme Court, the second of which they won outright. Second, how did the United States take the Southeast anyway? By law's forms used in sequence: a state extending its laws, an act of Congress, a presidential defense, a treaty signed by a minority and ratified by one vote, and finally soldiers. Preview the distinction the whole lesson turns on, between winning an argument about the law and obtaining its enforcement.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'A nation, a law, a court, a treaty, a march', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The Ground of the Question', 'Five nations, a syllabary, a constitution, a newspaper'),
        ('B', 'Georgia Presses, and the Cherokee Answer with Law', 'The 1802 compact, extension laws, and lawyers instead of war'),
        ('C', "The Removal Act and the President's Defense", 'Exchange in the act, benevolence in the message'),
        ('D', 'The Court Answers, and Is Not Obeyed', 'Dismissed in 1831, vindicated in 1832, unenforced'),
        ('E', 'A Treaty Signed by a Minority', 'New Echota, fifteen thousand protesters, one vote'),
        ('F', 'The March, and the Other Nations', 'Sixteen thousand rounded up, a quarter dead on the road'),
        ('G', 'Law at Every Step', 'Act, treaty, appropriation, and bayonet, in that order')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A covers the southeastern nations and the Cherokee achievement by 1828. Section B covers Georgia's pressure and the Cherokee decision to answer with law. Section C covers the Indian Removal Act and Jackson's defense of it. Section D covers the two Supreme Court cases and the fate of the judgment. Section E covers the Treaty of New Echota and Ross's protest. Section F covers the march of 1838 and 1839 and the other nations' removals. Section G holds the lesson's two statements together. The summary table at the end of the guided notes is titled Removal at a Glance.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_photo('phoenix-port.jpg', 'Section A', 'The Ground of the Question',
              ['The Cherokee Phoenix, first printed at', 'New Echota in February 1828, in Cherokee', 'and English.'],
              "The image is the first issue of the Cherokee Phoenix, printed at New Echota on February 21, 1828, held by the American Antiquarian Society. Keep the newspaper in view while section A is introduced, because it is the section's argument in a single object: a Native nation publishing its laws and its case in two languages, in type cast from characters one of its own citizens had invented. Section A establishes the ground of the whole question. East of the Mississippi in 1828 lived some 125,000 Native people. In the Southeast the Cherokee, Choctaw, Chickasaw, Creek, and Seminole had built the farms, schools, written laws, and printing that led white Americans to call them the Five Civilized Tribes. None of it, the lesson will show, protected their land.",
              title_size=40)

# ------------------------------------------------------ 5 THE CHEROKEE BY 1828
content_photo('sequoyah-port.jpg', 'A nation in print by 1828',
              ['Sequoyah completes the syllabary in 1821',
               'A written constitution adopted in 1827',
               'The Cherokee Phoenix begins in February 1828',
               'Farms, schools, mills, and a capital at New Echota'],
              "The image is Sequoyah holding the tablet of his syllabary, from the nineteenth century lithograph by Lehman and Duval after Henry Inman's copy of Charles Bird King's portrait. Walk the achievement in order, because students must feel its weight before Georgia's pressure makes sense. Sequoyah, a Cherokee silversmith who could not read English, spent years building written characters for the sounds of Cherokee and completed the syllabary in 1821; within a few years most Cherokee could read it, a literacy few American communities could match. The nation adopted a written constitution in 1827, modeled in part on the republic pressing against it, and in February 1828 the Cherokee Phoenix issued from New Echota, the first Native American newspaper, printed in Cherokee and English and edited by Elias Boudinot.",
              kick='A · The Ground of the Question')

# ------------------------------------------------------ 6 WHY THE LAND WAS WANTED
content_text('Why Cherokee country was coveted',
             ['Cotton: the soil of the Southeast grew the crop that made land into wealth',
              'Gold: found on Cherokee land in Georgia in 1828',
              'Some 125,000 Native people still lived east of the Mississippi',
              'Georgia had demanded the land since the compact of 1802'],
             "Desire came before doctrine in this lesson, so teach the motives plainly before any law is read. The Cherokee country sat on deep soil in the cotton belt at the moment cotton prices made southeastern land the most valuable farmland in the republic, and every acre a Native nation held was an acre a planter could not work with enslaved labor. In 1828 gold was found on Cherokee land in north Georgia, near Dahlonega, and prospectors crossed the nation's borders in defiance of federal law, which Georgia declined to stop. Georgia's legal claim was older: the compact of 1802, in which the federal government promised to extinguish Native title inside Georgia as soon as it could be done peaceably and on reasonable terms. A generation of Georgians read that promise as a debt overdue, and their state government set out to collect it.",
             kick='A · The Ground of the Question', size=24)

# ------------------------------------------------------ 7 STAT 125,000
stat('125,000', 'Native people east of the Mississippi in 1828',
     'The usual estimate for the year Jackson was elected · Five southeastern nations among them · Their land was the question the new democracy answered first',
     "Hold this number up before any statute is read, because removal can shrink in students' minds into a Cherokee story alone. One hundred twenty five thousand people is the population of a fair sized American city of the day, distributed across nations with governments, towns, farms, and treaty relations with the United States reaching back to Washington's administration. In the Southeast the five nations white Americans called civilized held millions of acres under treaties that guaranteed their land. The policy this lesson follows did not address a remnant. It addressed nations at the height of their adaptation to the republic's stated terms, which is exactly why their case is the test of those terms. The next sections narrow from this whole population to Georgia and the Cherokee, where every instrument of removal was tried in turn.",
     kick='A · The Ground of the Question')

# ------------------------------------------------- 8 SECTION B DIVIDER
divider_text('Section B', 'Georgia Presses, and the Cherokee Answer with Law',
             'A state abolishes a government on paper, and the nation hires lawyers.',
             "Section B teaches the confrontation before Congress acted, in a shape students should mark: pressure from a state, answered by a nation that chose law over war. Georgia's claim ran back to the compact of 1802, and by the late 1820s the state had run out of patience with the pace of federal treaty making. In 1829 and 1830 Georgia extended its own laws over Cherokee country, declared the Cherokee government abolished, voided Cherokee law, and moved to survey the nation's land and distribute it to white Georgians by lottery. Cherokee found mining gold, trading, or testifying against a white man were exposed to state prosecution in courts where Cherokee testimony did not count. The Cherokee answer, organized by Principal Chief John Ross, was delegations, memorials, counsel, and a lawsuit. Teach students to mark the choice: Ross's government believed the republic could be held to its own paper, and it spent a decade proving the belief half right.")

# ------------------------------------------------------ 9 GEORGIA EXTENDS ITS LAWS
content_text("Georgia's program, 1829 and 1830",
             ['State laws extended over Cherokee country',
              'The Cherokee government declared abolished',
              'Cherokee land surveyed for a lottery to white Georgians',
              'Gold miners and settlers cross the line, unpoliced'],
             "Take Georgia's acts as a program with one object, the transfer of the land. First, jurisdiction: Georgia extended its laws over the Cherokee country in 1829 and 1830, which meant Cherokee law ceased, on Georgia's paper, to exist inside Georgia's claimed borders. Second, government: acts of the Cherokee council were declared void, and Cherokee officials who enforced their own nation's law faced Georgia prosecution. Third, distribution: surveyors were sent to divide the country into lots, to be given to white Georgians in a land lottery, the same device Georgia had used for earlier cessions. Fourth, facts on the ground: miners after the 1828 gold discovery and settlers squatting on Cherokee farms were left alone by the state that claimed to govern them. Note the sequence for the activity: Georgia acted first, and every later federal instrument was built on ground Georgia had already papered over.",
             kick='B · Georgia Presses', size=24)

# ------------------------------------------------------ 10 ROSS AND THE ANSWER WITH LAW
content_photo('ross-port.jpg', 'John Ross and the answer with law',
              ['Principal chief from 1828 to 1866',
               'Memorials and delegations to Congress, year after year',
               'Lawyers hired, including former attorney general William Wirt',
               'The case carried to the Supreme Court'],
              "The image is John Ross in the hand colored lithograph published in 1843 in McKenney and Hall's History of the Indian Tribes of North America, after Charles Bird King's portrait, held by the Library of Congress. Give Ross his standing in the nation: principal chief from 1828 until his death in 1866, a merchant and planter of Cherokee and Scottish descent, educated in English, and the organizer of a resistance conducted entirely in the republic's forms. The Cherokee National Council resolved against any cession, funded delegations to Washington, flooded Congress with memorials, and retained William Wirt, a former attorney general of the United States, to carry the nation's case to the Supreme Court. Ross also used print: the Phoenix argued the case at home, and sympathetic northern papers argued it abroad. Teach the wager explicitly. Ross bet that treaties, courts, and public opinion could hold the United States to its word. The bet very nearly won.",
              kick='B · The Cherokee Answer')

# ------------------------------------------------- 11 SECTION C DIVIDER
divider_photo('jackson-port.jpg', 'Section C', "The Removal Act and the President's Defense",
              ['Jackson, painted by Ralph Eleaser', 'Whiteside Earl, about 1836, in the', "Smithsonian's collection."],
              "The image is Ralph Eleaser Whiteside Earl's portrait of Andrew Jackson, painted about 1836 and held by the Smithsonian American Art Museum. Earl was Jackson's own portraitist, living in the White House for much of the presidency, and the painting shows the president as he wished to be seen: erect, white haired, and certain. Section C moves the question from Georgia to Washington. Removal had been federal policy in some form since Jefferson, pressed by the states and resisted by the nations, but Jackson made it a program with a statute behind it. His first annual message asked Congress for the law, Congress debated it through the spring of 1830 against petitions and a serious opposition, and the Indian Removal Act became law on May 28, 1830. The section then reads Jackson's defense of the finished policy in his message of December 1830, which students will meet again as Station 2 of the activity, in the bank's audited text.",
              title_size=34)

# ------------------------------------------------------ 12 THE REMOVAL ACT
content_text('The Indian Removal Act, May 28, 1830',
             ['Authorizes exchanges: eastern land for districts west of the Mississippi',
              'Appropriates five hundred thousand dollars to carry them out',
              'Section 7 promises no existing treaty will be violated',
              'Passes the House by five votes, 102 to 97'],
             "Read the act by its moving parts, as Station 1 of the activity will. Its language is the language of contract: the president may lay off districts west of the Mississippi and exchange them with nations residing inside the states for the land those nations claim and occupy. Nothing in the text orders a single family from its home, and its defenders said so on the floor. Its seventh section promises that nothing in the act authorizes violating any existing treaty, which students should hold in memory against Station 5. But an exchange program run by the stronger party, funded with five hundred thousand dollars and pressed by states already surveying the land, carried its own momentum. The vote is the tell: 102 to 97 in the House, five votes, against the opposition of most northern members and a memorial campaign that reached every desk. Removal was national policy by the narrowest of margins.",
             kick='C · The Removal Act', size=23)

# ------------------------------------------------------ 13 STAT 102 TO 97
stat('102 to 97', 'the House vote for the Indian Removal Act',
     'A margin of five votes, May 1830 · The Senate had passed it 28 to 19 · Opposition came from the North, the missions, and the Cherokee memorial campaign',
     "This is the statistic that rescues the lesson from inevitability, and students should write it beside the act in their notes. Removal was contested at every step by people whose arguments students can still read: congressmen who called it a breach of national faith, missionaries who organized petitions by the thousand, newspaper editors, and the Cherokee delegation itself, lobbying in Washington through the debate. The bill passed the Senate 28 to 19 and the House 102 to 97, a margin of five votes in a chamber of more than two hundred. Five changed votes would have killed it. Teach the consequence honestly: because the margin was small, the administration's defenders worked to present removal as settled, generous, and already succeeding, which is the work Jackson's December message performs. Policy made by five votes was defended as the nation's benevolent consensus. The activity asks students to see the join between the vote and the selling.",
     kick='C · The Removal Act')

# ------------------------------------------------- 14 SECTION D DIVIDER
divider_photo('marshall-port.jpg', 'Section D', 'The Court Answers, and Is Not Obeyed',
              ['Marshall, painted by Henry Inman', 'in 1832, the year of the judgment.'],
              "The image is Henry Inman's 1832 portrait of Chief Justice John Marshall, painted the year he decided Worcester v. Georgia. Section D teaches the Cherokee case in its two arrivals at the Court, because the pair is the lesson in miniature. In 1831 the nation sued Georgia in its own name, and Marshall, for a Court that feared a confrontation it could not win, called the Cherokee a domestic dependent nation and dismissed the case. In 1832 the case returned wearing a missionary's name: Samuel Worcester, imprisoned by Georgia for living in Cherokee country without Georgia's license, appealed his conviction, and this time the Court decided the merits. Marshall's holding gave the Cherokee everything their lawyers had asked. What the section then follows is the holding's fate in the hands of a defiant state and an unwilling president, the gap between the law as declared and the law as done.",
              title_size=36)

# ------------------------------------------------------ 15 TWO CASES
content_text('Two cases, two answers, 1831 and 1832',
             ['1831: a domestic dependent nation, and the suit dismissed',
              'Worcester: a missionary jailed under Georgia law appeals',
              '1832: Georgia law has no force in Cherokee country',
              'The Georgia act is void, and the judgment a nullity'],
             "Work the two cases as a sequence, since students routinely merge them. Cherokee Nation v. Georgia, 1831, asked whether the nation, as a foreign state, could sue Georgia in the Supreme Court. Marshall's answer threaded a needle: the Cherokee were a distinct political society, but a domestic dependent nation, not a foreign state, so the suit was dismissed without reaching the land. The holding named dependence and nationhood in the same phrase, and both halves lived on. Worcester v. Georgia, decided March 3, 1832, reached the merits through Samuel Worcester's criminal appeal. Marshall held that the Cherokee nation was a distinct community occupying its own territory, in which the laws of Georgia could have no force, that intercourse with it was vested in the federal government, and that the act under which Worcester was convicted was void. The Cherokee had won the law. Section D's last slide asks what the win was worth.",
             kick='D · The Court Answers', size=23)

# ------------------------------------------------------ 16 THE JUDGMENT'S FATE
content_text("The judgment's fate",
             ['Georgia refuses to obey, and Worcester stays at hard labor',
              'Jackson declines to enforce the ruling against the state',
              'Worcester is pardoned by Georgia in January 1833',
              'The holding stands, and nothing on the ground changes'],
             "Give the aftermath its documented shape and resist the famous quotation. The line that Jackson said Marshall had made his decision and could enforce it himself appears in print decades later and is not in the record of 1832; what is in the record is quieter and sufficient. Georgia's legislature denounced the decision, its governor refused the Court's process, and Worcester and his fellow missionary Elizur Butler remained at hard labor in the state penitentiary. The Jackson administration made no move to execute the judgment against Georgia, and its allies pressed the missionaries to drop the case for the sake of the Union during the nullification winter. In January 1833 Governor Wilson Lumpkin pardoned the missionaries, who had agreed to petition no further, and the case died with the question formally decided and practically abandoned. The Cherokee lesson was exact: a judgment is a claim on other men's power, and theirs declined to pay.",
             kick='D · The Court Answers', size=23)

# ------------------------------------------------- 17 SECTION E DIVIDER
divider_text('Section E', 'A Treaty Signed by a Minority',
             'Cherokee law made the sale a capital crime. A minority signed anyway, and the Senate ratified by one vote.',
             "Section E teaches how the ground the Court had closed was opened by a different instrument. With Georgia's lottery distributing Cherokee farms and the administration determined on a cession, federal commissioners turned to the Cherokee who believed resistance was hopeless: Major Ridge, his son John Ridge, and Elias Boudinot, the former editor of the Phoenix, men of standing who had concluded that the nation must trade its land while a trade could still be had. Cherokee law, enacted in 1829, made ceding the nation's land without its government's authority a capital offense, and the Ridge party knew it; Major Ridge is reported to have said he had signed his death warrant. Ross and the national delegation were in Washington negotiating when the treaty was concluded at New Echota on December 29, 1835. Teach the section as a collision between two claims to speak for one nation, which is how the activity's stations frame it.")

# ------------------------------------------------------ 18 NEW ECHOTA
content_text('New Echota, December 29, 1835',
             ['Signed by Major Ridge, John Ridge, Elias Boudinot, and their party',
              'All Cherokee land east of the Mississippi for five million dollars',
              'Ross protests: upwards of fifteen thousand Cherokee against it',
              'Ratified by the Senate in May 1836, by a single vote'],
             "Set the instrument beside the protest, document against document, because students will do the same work in Stations 4 and 5. The Treaty of New Echota, concluded December 29, 1835, ceded in its first article all the lands owned, claimed, or possessed by the Cherokee east of the Mississippi, in consideration of five million dollars, with western land, removal assistance, and two years for the nation to emigrate. Its preamble performs consent, describing the Cherokees as anxious to make arrangements. Ross answered with a memorial and a petition: the instrument, his delegation averred, was fraudulent, made by unauthorized individuals, and upwards of fifteen thousand Cherokee, nearly the whole nation, had signed protests against it. Congress received the papers and ratified anyway. In May 1836 the Senate approved the treaty by a single vote above the two thirds required, and the cession the Court had refused Georgia now stood in treaty form.",
             kick='E · A Treaty Signed by a Minority', size=23)

# ------------------------------------------------------ 19 STAT 1
stat('1', 'vote to spare in the Senate, May 1836',
     'The Treaty of New Echota ratified by a single vote above two thirds · Against it, a protest signed by upwards of fifteen thousand Cherokee',
     "One vote is the smallest statistic in the unit and the one students remember, so spend the time its size earns. Treaties require two thirds of the Senate, and the Treaty of New Echota cleared that bar by a single vote in May 1836, after a debate in which senators read Ross's memorial and the protest petition into the argument against it. Set the two numbers side by side on the board: one, the margin by which the cession became the supreme law of the land, and fifteen thousand, the Cherokee who had put their names against it in a nation of about sixteen thousand. The forms were observed. The Senate voted, the president proclaimed, the deadline ran. What the memorial asked the country to weigh was whether a form observed over a documented refusal deserves the name of consent. That question, and not the march alone, is what the writing task puts to students.",
     kick='E · A Treaty Signed by a Minority')

# ------------------------------------------------- 20 SECTION F DIVIDER
divider_photo('osceola-port.jpg', 'Section F', 'The March, and the Other Nations',
              ['Osceola, the Seminole leader, painted', 'by George Catlin in 1838.'],
              "The image is George Catlin's 1838 portrait of Osceola, the Seminole leader who resisted removal in Florida and died in federal custody that year, held by the Smithsonian American Art Museum. Section F follows the paper into the world. The treaty's two years expired in May 1838, under President Van Buren, and some sixteen thousand Cherokee who had not emigrated were rounded up by federal troops under General Winfield Scott, held in stockade camps through a summer of drought and sickness, and sent west in detachments, most of them marching overland through the winter of 1838 and 1839. Roughly a quarter of the people died. The section also widens, as the reading does, to the other southeastern nations, whose removals ran on parallel tracks: the Choctaw first, the Creek in chains, the Chickasaw on negotiated terms, the Seminole at war, and the Eastern Band of Cherokee remaining in North Carolina. Teach the section with restraint: the record is plain, and it needs no decoration.",
              title_size=36)

# ------------------------------------------------------ 21 THE MARCH
content_text('The roundup and the march, 1838 and 1839',
             ['Some sixteen thousand Cherokee rounded up into camps',
              'Detachments marched west through the winter',
              'Roughly a quarter died, about four thousand people',
              "Among the dead was Quatie, John Ross's wife"],
             "Teach the march from the record, in the order the record gives it. In May and June 1838, Scott's soldiers, with Georgia and state volunteers, entered Cherokee homes across Georgia, Tennessee, Alabama, and North Carolina and moved families at bayonet point to stockade camps, often with the clothes they stood in; property left behind was looted in their absence, a fact Cherokee claims documented for decades afterward. Summer detachments sent by river suffered heavily in heat and drought, and Ross, negotiating for his nation to conduct its own removal, organized the remaining detachments under Cherokee conductors for the overland march. They crossed Tennessee, Kentucky, Illinois, Missouri, and Arkansas through the winter of 1838 and 1839, waiting on ice and ferries, burying their dead along the road. The count most often given is about four thousand dead of sixteen thousand removed, and Quatie Ross, who had given her blanket to a sick child on the river journey, died on February 1, 1839.",
             kick='F · The March', size=23)

# ------------------------------------------------------ 22 THE OTHER NATIONS
content_text('The others, and the ones who stayed',
             ['Choctaw: removed first, 1831, in disorder and suffering',
              'Creek: after resistance in 1836, marched in chains',
              'Chickasaw: negotiated terms, removed with more order',
              'Seminole: a long war, and a remnant never removed',
              'Eastern Band: remained in North Carolina'],
             "Widen the lens as the reading does, because the Cherokee case is the best documented of five removals, not the only one. The Choctaw, pressed by Mississippi's extension laws, signed at Dancing Rabbit Creek in 1830 and removed first, in the winter of 1831, in disorder that their own leaders described in print. The Creek resisted in 1836 and were marched west in chains, thousands of them, after their land was taken lot by lot in frauds federal investigators themselves documented. The Chickasaw negotiated longer, sold their land, and removed with more order and more of their property intact. The Seminole fought the Second Seminole War from 1835 to 1842, the costliest Indian war in American history, and a remnant in the Florida swamps was never removed at all. In North Carolina, the Eastern Band of Cherokee remained on land bought back for them by William Holland Thomas, their agent and adopted citizen.",
             kick='F · The March, and the Other Nations', size=22)

# ------------------------------------------------- 23 SECTION G DIVIDER
divider_text('Section G', 'Law at Every Step',
             'An act, a message, a treaty, an appropriation, and soldiers: the taking was documented at every step.',
             "Section G closes the lesson by holding its two statements together, and students should be able to state both without flinching from either. The first statement is documentary: removal was carried out under law at every step, and a teacher can lay the instruments end to end, Georgia's extension acts, the Removal Act of 1830 with its appropriation, Jackson's message defending the policy, Worcester's judgment against it, the Treaty of New Echota ratified by the Senate, and the army's orders of 1838. The second statement is about what those forms contained: a judgment left unenforced, a treaty signed by unauthorized men over the protest of nearly the whole nation, and a proviso in the act itself promising that no treaty would be violated. The Cherokee had answered in the republic's own language, with a constitution, a newspaper, petitions, and lawsuits, and they won in its court. What they could not obtain was a government willing to enforce what it had declared.")

# ------------------------------------------------------ 24 TWO STATEMENTS
content_text('What the Cherokee won, and what it bought',
             ['Won: the law, declared by the highest court in 1832',
              'Won: the record, a protest signed by nearly the whole nation',
              'Not won: enforcement, in 1832 or after',
              'The Southeast: taken under forms the holding had answered'],
             "Land the lesson here, in the balance the reading strikes. The Cherokee resistance was not futile in the ways students may assume: it delayed removal for most of a decade, it forced the taking into the open where every step had to be justified, and it left a record, Marshall's holding, Ross's memorial, the treaty's own preamble, against which the policy can be judged in its own era's terms. Students should hear that clearly, because the documents in the activity are that record. But the resistance's object was the land, and the land was taken: by 1839 the southeastern nations were removed or, in Florida and North Carolina, reduced to remnants, and the cotton frontier moved onto their farms. The next lesson turns to the other great test of Jackson's majority, a state claiming the power to nullify a federal law, where the president who would not enforce a judgment for the Cherokee threatened war for the tariff.",
             kick='G · Law at Every Step', size=23)

# ------------------------------------------------------ 25 GLANCE
s = slide(NAVY)
kicker(s, 'Removal at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Who claimed the Southeast, and on what ground', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The nation', 'Constitution 1827, Phoenix 1828, treaties in hand', 'Georgia claims the 1802 compact'),
        ('The law', 'Removal Act 1830, House 102 to 97', 'Jackson defends it as benevolence'),
        ('The court', 'Worcester won in 1832, and unenforced', 'New Echota signed by a minority, 1835'),
        ('The march', 'Sixteen thousand marched, a quarter dead', 'Law at every step, force at the end')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the summary table in the guided notes, Removal at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The four rows are the lesson's argument in order. The nation: a constitutional government with a newspaper, pressed by a state claiming an old compact. The law: Congress authorizes exchange by five votes, and the president defends the program as benevolence. The court: the Cherokee win the holding in 1832, receive no enforcement, and lose the ground to a treaty signed by a minority in 1835. The march: the treaty is executed by troops in 1838 and 1839, at the cost of roughly a quarter of the people. Grade the table generously on wording and strictly on sequence: the order of the instruments is the lesson.")

# ------------------------------------------------------ 26 VOCAB A
vocab('Words for the taking',
      [('Indian Removal Act', 'the law of May 1830, and the $500,000 behind it'),
       ('Cherokee Nation', 'a constitution, a syllabary, a newspaper, a lawsuit'),
       ('Worcester v. Georgia', "Marshall's holding of 1832, defied and unenforced"),
       ('Five Civilized Tribes', 'five nations, and a name that protected none of them')],
      "Definitions match the guided notes word for word. " + joined('Indian Removal Act') + ". " + joined('Cherokee Nation') + ". " + joined('Worcester v. Georgia') + ". " + joined('Five Civilized Tribes') + ". Teach the four in sequence: the instrument, the nation, the judgment, and the group.")

# ------------------------------------------------------ 27 VOCAB B
vocab('Words for the instrument and the cost',
      [('Treaty of New Echota', 'signed by a minority, ratified by one vote'),
       ('Trail of Tears', 'sixteen thousand marched, a quarter dead'),
       ('John Ross', 'principal chief, and leader of the resistance')],
      "Three more terms, again matching the guided notes exactly. " + joined('Treaty of New Echota') + ". " + joined('Trail of Tears') + ". " + joined('John Ross') + ". Keep the second term's measure in class: the name belongs first to the Cherokee removal, and memory has extended it to the southeastern removals as a whole. Ross's definition ends where the lesson ends, with the chief forced west with his own people.")

# ------------------------------------------------------ 28 SYNTHESIS
s = slide(NAVY)
kicker(s, 'The lesson in one view')
text(s, 0.9, 1.28, 11.5, 1.0, 'Resistance answered four ways', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Pressed', "Georgia extended its laws, and Congress funded exchange by five votes"),
        ('Answered', 'The Cherokee replied with a constitution, a press, petitions, and lawsuits'),
        ('Vindicated', "The Supreme Court held Georgia's laws void in Cherokee country"),
        ('Removed', 'A minority treaty, ratified by one vote, was executed by the army')]
yy = 2.78
for t, d in rows:
    text(s, 0.9, yy, 2.4, 0.7, t, size=24, color=RUST_LT, font='Georgia')
    text(s, 3.45, yy + 0.05, 9.0, 0.9, d, size=19, color=CREAM, leading=1.2)
    yy += 1.05
notes(s, "Use this slide to close the argument before the work begins, and make students say the four rows aloud in order, because the sequence is the lesson. Pressed: a state claimed the land under an old compact, and Congress made removal national policy by the narrowest of margins. Answered: the Cherokee resisted without war, in print, in petitions, and in court, under a chief who spent a decade in Washington's lobbies and courtrooms. Vindicated: the nation's highest court declared Georgia's laws void on Cherokee ground, and the declaration was left to stand alone. Removed: the taking was completed by a treaty the nation had refused, ratified by one vote and executed by soldiers. The republic had held its promise where its court could see it, and broken it where only its victims could. The next lessons test the same majority against a bank and a tariff.")

# ------------------------------------------------------ 29 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did the United States take the Southeast, and what did the Cherokee do to stop it? For each record, state whose law it claims to speak and what power stands behind the claim, then deliver the verdict.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Removal File: five stations and a verdict on law or force'),
        ('Notebook', 'Notebook page: five steps in a chart, and the judgment that stood alone'),
        ('Quick check', 'A Judgment and a Treaty: Worcester against New Echota'),
        ('Writing', 'A Policy of Law or of Force: the lesson question as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the Removal Act defined with its vote and appropriation, the Worcester holding with its fate, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Removal File, sets out five stations: the Indian Removal Act in Congress's own words, Jackson's message on Indian removal from the audited bank record, Worcester v. Georgia from the audited bank record, Ross's memorial and protest of 1836, and the Treaty of New Echota, and it ends with a table sorting the records by the law they claim and the power behind it, and a verdict on whether removal was a policy of law or of force. The notebook page charts the five steps of the taking. The quick check, A Judgment and a Treaty, tests the Worcester holding, its fate, and the treaty's margin. The writing task turns the verdict into an essay from the evidence bank. The exit ticket has three parts: the Removal Act with its vote and appropriation, the Worcester holding with its fate, and the lesson question in two or three sentences. Next lesson opens with a tariff and a doctrine.")

dc.save(OUT)
