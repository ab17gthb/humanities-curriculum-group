#!/usr/bin/env python3
"""Sectional Crisis Lesson 3 deck builder. Image led deck: the Brady Douglas as the title, Douglas, Sumner, Brooks, Brown, and Buchanan portraits for the sections."""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
LESSON_DIR = os.path.dirname(HERE)
UNIT_DIR = os.path.dirname(LESSON_DIR)
sys.path.insert(0, UNIT_DIR)
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags,
                         divider_photo, content_photo, content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED, W, H)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

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

def vocab(title, terms, note, kick='The vocabulary'):
    s = slide(CREAM)
    kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95, 11.5, 1.0, title, size=30, color=NAVY, font='Georgia')
    n=len(terms); step = 1.52 if n<=3 else 1.08
    yy = 2.1
    for term, dfn in terms:
        text(s, 0.9, yy, 4.1, 0.9, term, size=23 if n<=3 else 21, color=NAVY, font='Georgia')
        text(s, 5.15, yy + 0.06, 7.3, 1.1, dfn, size=18 if n<=3 else 15, color=MUTED, leading=1.2)
        yy += step
    notes(s, note)
    return s

SHORT = {
 'Kansas-Nebraska Act': "Douglas's law of May 30, 1854, organizing Kansas and Nebraska, leaving slavery to popular sovereignty, and repealing the Missouri line",
 'popular sovereignty': "Douglas's doctrine that a territory's people should decide slavery for themselves",
 'Bleeding Kansas': "the newspapers' name for the Kansas guerrilla war of 1855 and 1856, some two hundred dead",
 'border ruffians': "the free state name for the Missourians who crossed to vote, intimidate, and sack Lawrence",
 'Lecompton Constitution': "the proslavery constitution of 1857, offered in a referendum rigged to protect slavery either way",
 'John Brown': "the abolitionist of Pottawatomie in 1856 and Harpers Ferry in 1859, hanged December 2, 1859",
 'Charles Sumner': "the Massachusetts senator beaten nearly to death at his desk for the Crime Against Kansas speech",
}
LQ = 'What did the Kansas-Nebraska Act repeal, and what did popular sovereignty look like when settlers tried it?'
UQ = 'How did compromise over slavery finally fail, and what did the war it caused settle about slavery and the Union, and what did it leave open?'
N = {}
# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY); rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'SECTIONAL CRISIS AND CIVIL WAR \u00b7 LESSON 3', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Kansas-Nebraska Act and Bleeding Kansas', size=34, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'A railroad bargain repeals a 34 year old line, and a territory tests the doctrine that replaced it.', size=17, color=POWDER)
N[1] = "Open with the portrait and the bargain it carries. Stephen A. Douglas of Illinois, photographed by Mathew Brady about 1860, was the Senate's manager of western expansion, and in 1854 he traded away the Missouri Compromise to organize two territories and advance a railroad. Set the lesson's shape for students. First the price of the repeal and the doctrine offered in its place. Then the doctrine shipped west to Kansas, where settlers, voters from another state, and armed bands tested it in order. Then the violence of one week in May 1856. The lesson ends at Lecompton, where the doctrine's own author disowned its Kansas result, and students must judge whether the doctrine failed or simply showed what it was."
notes(s, N[1])
# 2 QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[(LQ, {})]], size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': RUST_LT, 'italic': True}), (UQ, {'italic': True})]], size=17, color=POWDER, font='Georgia', leading=1.2)
N[2] = "Read the lesson question aloud and split it into its two halves, because the writing task grades both. The first half is documentary: what did the act repeal, answered from the act's own text, which students will read at Station 1. The second half is the lesson's real work: what did popular sovereignty look like in practice, not in Douglas's speeches but in an election carried by riders from Missouri, in two governments claiming one territory, and in a referendum that offered no way to say no. Warn the class against answering the second half from the doctrine's promises. The question asks what settlers produced when they tried it, and Kansas kept the receipts."
notes(s, N[2])
# 3 MAP
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'A repeal, a doctrine, a territory, a verdict', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The Railroad Behind the Repeal', "The South's price for organizing the territories"),
        ('B', 'The Act and Popular Sovereignty', 'The Missouri line declared void'),
        ('C', 'The Storm and the Broken Parties', 'The Appeal, the Whigs dead, a coalition gathering'),
        ('D', "Kansas, the Doctrine's Laboratory", 'Two governments claim one territory'),
        ('E', 'Violence in Sequence', 'Lawrence, the Senate floor, Pottawatomie'),
        ('F', 'A Small War and an Armed Truce', 'Bleeding Kansas, near two hundred dead'),
        ('G', 'Lecompton and the Balance Sheet', 'The rigged referendum and the doctrine judged')]
yy = 2.62
for letter, head, sub in rows:
    text(s, 0.92, yy, 0.5, 0.5, letter, size=20, color=RUST_LT, font='Georgia', bold=True)
    text(s, 1.45, yy, 6.6, 0.5, head, size=19, color=CREAM, font='Georgia')
    text(s, 8.2, yy + 0.03, 4.3, 0.5, sub, size=15, color=POWDER)
    yy += 0.62
N[3] = "Walk the map once, slowly, because it is the lesson's whole argument in seven lines. A railroad bargain comes first, and the repeal is its price. The act replaces a congressional rule with a doctrine and sends the question west. The North answers with an appeal and a party system breaks. Kansas then runs the experiment in public: immigration organized by both sections, an election imported from Missouri, and two governments. The experiment turns violent in a single week of May 1856, settles into a small war, and ends at a referendum table in Lecompton. Students should copy the seven section titles into their notes now, because the guided notes follow this order exactly."
notes(s, N[3])
# 4 DIVIDER A
divider_text('Section A', 'The Railroad Behind the Repeal', 'Douglas needs Kansas organized, and the South names its price.', "Section A is about motive, and students should hold it plainly. Douglas chaired the Senate committee on territories and wanted a transcontinental railroad west from Chicago. A railroad needed organized territory, and organizing Kansas and Nebraska needed southern votes that a rival southern route could draw away. The land in question lay north of the Missouri Compromise line of 1820, where slavery had been barred for thirty four years. Southern senators would not vote to organize free territory on the railroad's path. Their price was the line itself. Teach the sequence in that order, bargain first and principle second, because the Appeal at Station 2 makes exactly that accusation.")
# 5 A CONTENT
content_photo('douglas-port.jpg', 'The price of organization', ['A railroad west from Chicago needs territories organized', 'Southern votes can be withheld for a southern route', 'The land lies north of the line of 1820', "The South's price: the bar on slavery must go"], "Give Douglas his due before the class judges him, because he was no marginal figure. He was the Senate's leading expansionist, a national Democrat with presidential ambitions, and he believed western settlement was the country's future. His problem was arithmetic. Every session, bills to organize Nebraska died because southern senators saw a free territory closing around slavery and a northern railroad enriching Chicago. The repeal was the coin that could buy the votes. Students should also hear what Douglas said the coin was: not a surrender, he insisted, but a principle, the right of a territory's people to govern their own domestic institutions, which is where section B begins.", kick='Section A')
# 6 STAT LINE
stat("36\u00b030'", 'the Missouri Compromise line of 1820', 'North of this line, in the Louisiana Purchase lands, slavery had been barred for 34 years when the act declared the bar inoperative and void.', "Linger on the line, because the whole lesson is the story of removing it. The Missouri Compromise of 1820 admitted Missouri as a slave state and Maine as a free state and drew this parallel across the Louisiana Purchase: slavery barred north of it, permitted south of it. For thirty four years both sections treated the line as settled law, and the Appeal of the Independent Democrats called it a solemn compact and inviolable American law. Kansas and Nebraska both lay north of it. Organizing them under any rule that admitted slavery required Congress to break its own settlement in so many words, and the act did so, using the words inoperative and void that students will read at Station 1.", kick='Section A')
# 7 DIVIDER B
divider_photo('douglas-port.jpg', 'Section B', 'The Act and Popular Sovereignty', ['May 30, 1854: the line is void, and the people are left perfectly free.'], "Introduce the act as a text before it becomes an argument, because students meet its exact words at Station 1. The Kansas-Nebraska Act passed on May 30, 1854, after months of debate that filled the northern press. Its fourteenth section carried the repeal and the doctrine in a single passage, which is why this lesson quotes that section whole. Douglas argued the act was neutral: Congress would neither plant slavery nor bar it, and each territory would decide. His critics answered that neutrality between a pledged freedom and slavery was itself a decision, and that a settler majority could now vote human bondage into land Congress had consecrated to freedom in 1820.")
# 8 B CONTENT
content_text('Inoperative and void', ['The eighth section of the Missouri act declared void', 'Ground given: non-intervention, as recognized in 1850', 'Not to legislate slavery in, nor to exclude it', 'The people left perfectly free to regulate their domestic institutions'], "Put the act's full definition on the board in its joined form, because the test quotes its language. " + joined('Kansas-Nebraska Act') + " Walk the section's logic slowly. First the repeal, stated as a correction: the old bar is inconsistent with non-intervention and therefore void. Then the claim of neutrality in both directions at once, neither legislating slavery in nor excluding it. Then the operative sentence, leaving the people perfectly free, subject only to the Constitution. Ask the class who counts as the people of a territory in its first year, and hold their answers for section D, where Kansas answers the question in practice.", kick='Section B')
# 9 B CONTENT 2
content_text("The doctrine and its silence", ['Popular sovereignty: the territory decides for itself', 'Offered as the democratic answer to congressional rule', 'No word on when the decision may be made', 'No rule for who votes, and no umpire for a disputed count'], "Name the doctrine whole for the notes, because everything after this slide is its test. " + joined('popular sovereignty') + " The silences in the second half of this slide are the lesson's hinge, so teach them as facts about the statute, not as hindsight. The act did not say whether slavery could be decided by the first territorial legislature or only in a state constitution. It set no residency period for voters. It named no authority to settle a disputed election. Douglas treated those silences as freedom. Kansas treated them as openings, and organized men on both sides walked through every one of them.", kick='Section B')
# 10 VOCAB 1
vocab('Words for the act and the doctrine', [(t, SHORT[t]) for t in ['Kansas-Nebraska Act', 'popular sovereignty', 'Bleeding Kansas']], "Run this vocabulary slide as a first check, and read the third term's full form aloud even though Kansas has not burned yet on the map. " + joined('Bleeding Kansas') + " Students should notice that the name comes from newspapers, not from a statute or a speech: the country's press named the territory's war while it was happening, and the name did political work, carrying Kansas into every northern parlor as evidence about the doctrine. When the class reaches section F, return to this slide and ask whether the name describes a failure of popular sovereignty or its natural result, and make them answer from the election record, not from the name's drama.")
# 11 DIVIDER C
divider_text('Section C', 'The Storm and the Broken Parties', 'An appeal in January, two parties broken by the repeal.', "Section C follows the repeal home to the party system, because Kansas was fought in Washington and in the newspapers before it was fought on the creeks. The Appeal of the Independent Democrats appeared in January 1854, while the bill was still in committee, signed by six members of Congress led by Chase and Sumner. It was a campaign document as much as a protest, designed to organize the North against the bill and to name its author a conspirator. Its language, sacred pledge, criminal betrayal, atrocious plot, shows students how quickly the repeal escaped legislative language and became a sectional indictment that no later compromise language could call back.")
# 12 C CONTENT
content_text('A gross violation of a sacred pledge', ['The Appeal of the Independent Democrats, January 1854', 'Chase, Sumner, Giddings, and three others sign', 'The Missouri prohibition called a solemn compact', 'Protest called for through press, memorials, and meetings'], "Teach the Appeal as the North's founding document for the fight, and slow down on its legal claim, because it is the mirror of the act. Where the act called the Missouri bar inconsistent and void, the Appeal called the same bar a solemn compact accepted by the whole country and inviolable American law for more than thirty years. Both documents agreed on the fact, that Congress in 1820 had barred slavery north of the line. They disagreed on whether a later Congress could honorably unbar it. Then note the Appeal's methods: correspondence, the press, memorials, public meetings. This is politics organizing itself, and within two years it would have a party, which is the next slide's subject.", kick='Section C')
# 13 C CONTENT 2
content_text('The party system breaks', ['The Whig Party collapses within two years', 'The Democrats survive, split by section', 'Ex-Whigs, Free Soilers, anti-Nebraska Democrats gather', 'The next lesson names the party they built'], "Explain why the Whigs died of this act and the Democrats did not. The Whig Party held together by evading slavery, and the repeal made evasion impossible: northern Whigs had to oppose the act their southern wing had helped pass, and no platform could be written that both could sign. The Democrats, Douglas's party, held the presidency and the machinery, but every Kansas news cycle split their northern voters from their southern leadership. Into the Whig vacancy stepped the anti-Nebraska coalition, the strangest alliance of the decade, men who agreed on one sentence only: Congress should never have repealed the line. Lesson 4 names what they built from that sentence.", kick='Section C')
# 14 DIVIDER D
divider_text('Section D', "Kansas, the Doctrine's Laboratory", 'Both sections organize the settlement, and Missouri votes first.', "Frame Kansas as an experiment with no controls, because that is what the doctrine built. The territory opened in 1854 with a few thousand actual settlers and a national audience. New England emigrant aid societies raised money, bought rifles in some cases, and sent free state families west in organized companies. Missouri, a slave state sharing a long border, needed no societies: its citizens could ride in for an election and ride home the same week. The territorial governor's own count showed the imbalance early. Every institution the doctrine needed, an honest registry, a resident electorate, a trusted count, had to be invented on the ground by men who already knew what result they needed.")
# 15 D CONTENT
content_text("The settlers' race", ['Emigrant aid societies send free state settlers west', 'Missourians cross the border in organized thousands', 'Land, votes, and the legislature are the prizes', 'The territory fills with men sent to decide it'], "Teach the migration as politics by other means, openly practiced by both sides. The New England Emigrant Aid Company and its imitators made no secret of their purpose: to settle Kansas with free labor voters faster than slavery could arrive. Missouri's answer was geography and numbers, thousands of men within a day's ride of the polls, organized in lodges and companies. Neither side treated settlement as private choice alone, which is the first crack in the doctrine's picture of neighbors quietly regulating their own institutions. The neighbors were being shipped, funded, and counted by national movements that understood Kansas as the Senate's balance of power wearing a settler's coat.", kick='Section D')
# 16 D CONTENT 2
content_text('March 1855: an imported election', ['Missourians ride in, vote, and ride home', "The name border ruffians is earned in this season", 'The proslavery legislature expels its free state members', 'Topeka answers with a rival government; Pierce recognizes Lecompton\'s side'], "Put the election's name and date into the notes through its actors. " + joined('border ruffians') + " The count told the story in numbers students should hear: thousands more votes than the territory had resident voters, cast at polls ringed by armed Missourians. The legislature chosen that day expelled the few free state men elected and wrote a slave code. The free state answer was constitutional in form: a convention at Topeka, a constitution, a governor. President Pierce then recognized the imported legislature as lawful and called the Topeka government revolutionary, so Washington's recognition, not Kansas's residence, decided which government was real. The doctrine had promised the opposite order of things.", kick='Section D')
# 17 DIVIDER E
divider_photo('brooks-port.jpg', 'Section E', 'Violence in Sequence', ['One week in May 1856: a town sacked, a senator beaten, five men killed.'], "Set the week's chronology on the board before any single event, because the sequence is the teaching. Preston Brooks of South Carolina, photographed in 1856, is this section's face because his act joined the territory's war to the Senate's floor. On May 21 a proslavery posse sacked Lawrence. On May 22 Brooks beat Charles Sumner at his desk. On May 24 and 25 John Brown's party killed five men at Pottawatomie. Each act was defended by its side as an answer to the one before. Teach the three with the same plainness and the same brevity, and refuse the classroom instinct to grade them by sympathy, because that grading is the habit the week itself teaches against.")
# 18 E CONTENT
content_photo('brooks-port.jpg', 'Lawrence sacked, Sumner beaten', ['May 21: a posse destroys the presses and burns the hotel at Lawrence', "Sumner's Crime Against Kansas speech concludes the same days", 'May 22: Brooks beats Sumner nearly to death at his Senate desk', "Massachusetts keeps the seat empty; the South honors Brooks"], "State the two events as one sequence. The sack of Lawrence was carried out under legal forms, a marshal's posse enforcing territorial law, which is itself a lesson datum: the proslavery government's law and its violence were the same instrument. Sumner's speech, delivered May 19 and 20, had attacked slavery and named southern senators in personal terms, and Brooks, a kinsman of one of them, answered it with a cane in the chamber after the Senate had adjourned. Sumner could not return to his seat for years. The empty chair became the North's most reproduced argument, and Brooks's reelection became the South's, each section exhibiting its victim and its hero from the same afternoon.", kick='Section E')
# 19 E CONTENT 2
content_photo('brown-port.jpg', 'Pottawatomie, May 24 and 25', ['John Brown rides with four sons and two others', 'Five proslavery settlers taken from their cabins and killed', 'Brown calls it an answer to Lawrence and the caning', 'The killings open the territory\'s guerrilla summer'], "Give Brown his full definition here, read aloud once, because the class will meet him again at Harpers Ferry in Lesson 5 and must carry the whole record, not half of it. " + joined('John Brown') + " Then state Pottawatomie in the same flat terms as Lawrence and the caning: five men, none of them slaveholders of any scale, taken at night and killed, in retaliation for a sack in which no one had died. Brown never stood trial for it and defended it as war. Students should sit with the asymmetry the week leaves: the doctrine had no court, no count, and no constable that both sides accepted, so retaliation became the territory's only working institution.", kick='Section E')
# 20 DIVIDER F
divider_text('Section F', 'A Small War and an Armed Truce', 'Guerrilla fighting through 1856, and a governor restores quiet at gunpoint.', "Section F is short in the reading and should be short in the teaching, a ledger rather than a narrative. Through the summer and fall of 1856, free state and proslavery bands raided, burned, and ambushed across eastern Kansas, prisoners were taken, and small actions were fought along the border. Federal authority arrived late and thin: a new governor, John Geary, with troops at his back, disbanded the rival militias in September and imposed quiet. Name what the truce proves. Order in Kansas was restored not by the doctrine's local decision but by federal force applied to both sides, the intervention popular sovereignty existed to prevent, arriving a year and a half after the act.")
# 21 STAT 200
stat('200', 'dead, by the usual estimate, in Bleeding Kansas', 'The newspapers\' name for the territory\'s guerrilla war of 1855 and 1856, counted in farms burned, prisoners taken, and some two hundred killed.', "Use the number to discipline the lesson's language, because Bleeding Kansas can sound like a slogan until it is counted. Two hundred dead is a small war's toll, not a metaphor: men shot at polls and on roads, killed in raids and in reprisals like Pottawatomie, across two years in a territory whose entire population was still in the tens of thousands. The estimate is an estimate, and students should hear it called one. What is not in doubt is the structure the number measures: a territory with two governments, two militias, and no authority both sides obeyed, where every killing recruited for the next one. That structure, not any single outrage, is the doctrine's Kansas product.", kick='Section F')
# 22 DIVIDER G
divider_photo('buchanan-port.jpg', 'Section G', 'Lecompton and the Balance Sheet', ['A referendum with no way to say no, and a president and a doctrine part company.'], "Introduce James Buchanan, painted by George Peter Alexander Healy in 1859, as the doctrine's unlikely executioner. Buchanan became president in 1857 pledged to let Kansas decide, and the Lecompton convention gave him a result his southern supporters wanted. When he endorsed it, he forced the question the whole lesson has been building: was a vote still the people's decision when the ballot had been arranged so the people could not reject the constitution at all. Douglas's answer to that question broke the Democratic Party's last bridge between its sections, and it did so in popular sovereignty's own name, which is why this section closes the lesson.")
# 23 G CONTENT
content_photo('buchanan-port.jpg', 'The Lecompton referendum', ['A proslavery convention drafts the constitution at Lecompton', 'With slavery or without it: slavery already present protected either way', 'No choice to reject the constitution itself', 'Free state voters boycott the referendum as a fraud'], "Read the referendum's design as a document, the way students read it at Station 5, which is a labeled teaching summary of the record. " + joined('Lecompton Constitution') + " Two features deserve the class's full attention. The boycott came first: free state voters had refused the delegate election because they distrusted the registry, so the convention spoke for a minority of settlers. The ballot came second, and it is the cleaner evidence, because it needs no testimony: a voter could choose slavery's future arrivals or not, but the constitution, and the slavery already in Kansas, stood beyond his reach either way.", kick='Section G')
# 24 G CONTENT 2
content_text("Douglas breaks with Buchanan", ['Buchanan endorses Lecompton and asks Congress to admit Kansas under it', "Douglas: a rigged vote betrays popular sovereignty itself", 'Congress refuses admission under Lecompton', 'January 1861: Kansas enters the Union a free state'], "Close the section on the break, because it is the doctrine's verdict on itself. Douglas did not oppose Lecompton as an antislavery man; he opposed it as popular sovereignty's author, arguing that Kansas must be allowed a fair vote on the whole constitution, and he spent his alliance with a Democratic president to say so. Congress refused the admission, Kansas voters later rejected Lecompton outright under Congress's terms, and the territory finally entered the Union free in January 1861, days after secession had begun emptying the Senate that had fought over it for seven years. The question the doctrine was built to remove from national politics had consumed national politics for the whole of its life.", kick='Section G')
# 25 VOCAB 2
vocab('Words for the war and the fraud', [(t, SHORT[t]) for t in ['border ruffians', 'Lecompton Constitution', 'John Brown', 'Charles Sumner']], "Run the second vocabulary slide backward through the lesson, attaching each term to its section. The senator belongs in the notes in full at least once in this lesson's teaching. " + joined('Charles Sumner') + " Ask students to place the four terms in the order the territory met them: the ruffians at the election of 1855, Sumner's speech and beating in May 1856, Brown's answer three nights later, and Lecompton's paper settlement in 1857. A student who can run that order without notes owns the lesson's chronology, and chronology, in this lesson, is most of the argument.")
# 26 GLANCE
content_text('The lesson at a glance', ['A railroad bargain repeals a 34 year old settlement', 'The act replaces a rule with a doctrine and names no umpire', 'An imported election produces two governments', 'One week of May 1856 joins a town, a Senate desk, and a creek', 'Lecompton rigs the vote, and the doctrine\'s author disowns it'], "Synthesize in the lesson's own order before the exit work. The repeal began as a bargain, not a theory, and the theory offered for it contained the silences Kansas exploited: no resident electorate defined, no timetable, no umpire. The first election was imported, the second government was unrecognized, the argument moved to presses, canes, and broadswords within a single week, and the final settlement attempt arranged its ballot so the question could not be lost. Hold the last point longest, because it converts the lesson from a story about violence into an argument about design: at Lecompton nobody needed a weapon, because the paper had already decided.", kick='Synthesis')
# 27 ANSWERING
content_text('Answering the question', ['What did the act repeal? The Missouri line, in the act\'s own words', 'Failing, or working as designed? Take the position', 'Strongest test cases: March 1855 and Lecompton', 'Use the act at Station 1 and Sumner at Station 4 as your documents'], "Model the two verdicts without confiscating either. Failing: the doctrine promised a territory's own people deciding and was decided instead by imported voters, armed bands, and a rigged ballot, which is failure measured by its own standard. Working as designed: the act set no residency rule, no timetable, and no umpire, so every Kansas abuse was a move the design left open, and the design therefore produced exactly what it was built to allow. Students may take either side, but the rubric requires the rejected side stated at its strongest first, and it requires the act's text, not impressions of Douglas, as the first exhibit.", kick='Synthesis')
# 28 EXIT
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.7, 11.5, 2.2, 'Answer the question, and exit', size=44, color=CREAM, font='Georgia', leading=1.1)
rule(s, 0.92, 3.5)
text(s, 0.9, 3.85, 11.0, 2.6, ['Exit ticket: the three questions at the end of your guided notes.', 'Writing task: judge the doctrine from the act and two Kansas tests.'], size=22, color=POWDER, space_after=10, leading=1.3)
N[28] = "Close by sending students to the two pieces of written work and naming what each one checks. The exit ticket checks the definition whole, the repeal and the act's date, and the failing or as designed judgment argued from both sides. The writing task checks the larger verdict, and it should be introduced now, while the stations are fresh: claim first, the act's own words, two Kansas tests, the strongest fact against the position faced directly, and an ending on the doctrine's balance sheet. Tell the class the standard plainly. A verdict on Kansas that never quotes the act or the Lecompton ballot is an opinion about documents it has not used, and the rubric will grade it as one."
notes(s, N[28])

PAD = {
 4: " Keep the customhouse arithmetic in view as well: the same Congress that could not organize the territories without southern consent also could not build the railroad without the territories, which is why a transportation bill became a slavery settlement's undoing.",
 5: " A useful check is to ask who in this slide is acting on principle and who on interest, and let students discover that Douglas would have rejected the question: he believed the principle was the interest, settlement by the settlers themselves.",
 7: " Note the theater of the passage as well: the act repeals and promises inside one section, so a reader who stops after the repeal has only half the document the Senate voted on in May of 1854.",
 11: " The signers were not outsiders. Chase had governed Ohio and Sumner sat in the Senate, and their appeal reads as what it was, a founding circular for a coalition that did not yet have a party name.",
 13: " If a student asks why the coalition did not simply revive the Whigs, the answer is on this slide: the name itself had signed the Compromise and split over it, and a new banner was worth more than a repaired one.",
 14: " The first territorial governor, Andrew Reeder, arrived a Pennsylvania Democrat friendly to the act and left a free state man, a conversion worth one sentence as evidence of what the ground itself did to the doctrine's friends.",
 15: " Lawrence, founded by emigrant aid settlers in the summer of 1854, belongs in this slide's margin: the free state capital existed because an aid society planted it, town founding as campaign strategy.",
 17: " The cane Brooks used was a gutta percha walking stick, presented to him afterward by admirers, with replacement canes sent from across the South, a detail students remember and one that measures the sections' distance better than any speech.",
 20: " Geary's truce also spared Lawrence a second sack that September, when he faced down a proslavery force outside the town, the federal governor standing physically between the territory and its war.",
 22: " Buchanan's defenders deserve one fair sentence: he argued Kansas had voted under the forms of law and that rejecting the result would invite every losing side to boycott its way out of elections, an argument Douglas had to answer, not merely denounce.",
 25: " End the slide by returning to the ballot box Sumner named at Station 4, plundered in 1855 and rigged on paper in 1857, since those are the two exhibits a student must be able to cite without notes in hand.",
 26: " Resist adding new content here; the synthesis earns its place by arrangement alone, and students who followed the sections will hear their own notes reorganized into the verdict the writing task asks them to defend.",
 27: " Leave the two verdicts on the board while students begin the writing task, not as answers to copy but as the shapes of an answer, each with its strongest exhibit named out loud.",
 28: " Collect the exit tickets at the door and sort them tonight by the third question, since a student who cannot argue the rejected side is not ready for the Republican Party lesson that follows.",
 2: " Keep both halves visible on the board as you read, the repeal in the act's words on the left and the Kansas record on the right, so students see from the first minute that the lesson grades a promise against its evidence.",
 3: " Point once at the verbs as you walk it: repeals, replaces, breaks, claims, sacks, restores, rigs. The lesson is a chain of actions, and a student who can retell the chain in those verbs can rebuild the argument without notes.",
 12: " One more document skill belongs here: the Appeal was printed in newspapers across the North within days, so its audience was voters, not senators, and its charges were written to be repeated at meetings exactly as students are repeating them now.",
 18: " Sumner's own part in the provocation should be stated fairly: his speech named a senator's relative and used language his colleagues called unparliamentary, and saying so costs the lesson nothing, because a cane is not a parliamentary answer.",
 21: " Geary's truce and this count belong together in students' minds: the war ended for the season when federal troops arrived, and its cost is the number the territory paid for the doctrine's first two years of self government.",
 24: " The break also reordered Douglas's own future, costing him southern support he never recovered before 1860, which Lesson 5 will collect when the Democratic convention splits over the same ground this slide covers.",
}
for i, sl in enumerate(dc.prs.slides, 1):
    if i in PAD:
        cur = sl.notes_slide.notes_text_frame.text
        if len(cur.split()) < 120:
            sl.notes_slide.notes_text_frame.text = cur + PAD[i]

heads = {1:'Opening frame',2:'The lesson question',3:'The lesson in one slide',4:'Section A: The Railroad Behind the Repeal (divider)',5:'The price of organization',6:'36 degrees 30 minutes: the Missouri line',7:'Section B: The Act and Popular Sovereignty (divider)',8:'Inoperative and void',9:'The doctrine and its silence',10:'Vocabulary: words for the act and the doctrine',11:'Section C: The Storm and the Broken Parties (divider)',12:'A gross violation of a sacred pledge',13:'The party system breaks',14:"Section D: Kansas, the Doctrine's Laboratory (divider)",15:"The settlers' race",16:'March 1855: an imported election',17:'Section E: Violence in Sequence (divider)',18:'Lawrence sacked, Sumner beaten',19:'Pottawatomie, May 24 and 25',20:'Section F: A Small War and an Armed Truce (divider)',21:'200 dead in Bleeding Kansas',22:'Section G: Lecompton and the Balance Sheet (divider)',23:'The Lecompton referendum',24:'Douglas breaks with Buchanan',25:'Vocabulary: words for the war and the fraud',26:'The lesson at a glance',27:'Answering the question',28:'Now your turn: answer the question and exit ticket'}
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
print('notes range:', min(counts), max(counts))
missing=[t for t,_ in TERMS if not any((t+': '+TD[t]) in (sl.notes_slide.notes_text_frame.text if sl.has_notes_slide else '') for sl in prs2.slides)]
print('terms missing verbatim joined in notes:', missing)
