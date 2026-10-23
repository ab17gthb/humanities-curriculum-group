#!/usr/bin/env python3
"""Jackson and Reform Lesson 3 deck builder. Image led deck: the Sully Jackson as the title, the Healy Calhoun, the Alexander Webster, and the Appletons Hayne for the section dividers."""
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

def joined(term):
    return f"{term}: {TD[term]}"

def vocab(title, terms, note, kick='The vocabulary'):
    s = slide(CREAM)
    kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95, 11.5, 1.0, title, size=30, color=NAVY, font='Georgia')
    yy = 2.1
    for term, dfn in terms:
        text(s, 0.9, yy, 4.1, 0.9, term, size=24, color=NAVY, font='Georgia')
        text(s, 5.15, yy + 0.06, 7.3, 1.1, dfn, size=18, color=MUTED, leading=1.2)
        yy += 1.52
    notes(s, note)
    return s

SHORT = {
 'Tariff of Abominations': 'the southern name for the Tariff of 1828, whose duties protected northern factories and raised planting state prices',
 'nullification': 'the claim that a state may declare a federal law void and of no force inside its borders',
 'John C. Calhoun': 'the South Carolina vice president who secretly wrote the Exposition and later resigned to defend nullification in the Senate',
 'South Carolina Exposition and Protest': "Calhoun's secret 1828 pamphlet arguing a state could nullify a federal law inside its borders",
 'Ordinance of Nullification': "South Carolina's ordinance of November 24, 1832, declaring the tariffs of 1828 and 1832 void in the state",
 'Webster-Hayne debate': "the Senate debate of January 1830, Hayne for the compact of states, Webster for the people's government",
 'Force Bill': 'the law of March 2, 1833, authorizing Jackson to use the army and navy to collect the duties',
}

N = {}
# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'JACKSON AND REFORM \u00b7 LESSON 3', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Nullification Crisis', size=34, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'A state claims a veto over federal law, and the president answers.', size=17, color=POWDER)
N[1] = "Open with the portrait and the standoff it promises. Andrew Jackson, painted by Thomas Sully before 1829, is the president who will tell South Carolina that disunion by armed force is treason. The state facing him is not rebelling in this lesson. It is doing something quieter and, for the Union, harder to answer: it is passing a law, in a convention, with a constitutional argument attached, claiming that a federal law simply does not exist inside its borders. Set the lesson's shape for students. First a tariff grievance, then the doctrine built to answer it, then the doctrine debated, personalized, and enacted, then a proclamation, and finally a settlement in which force and compromise arrive in the same week."
notes(s, N[1])
# 2 QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('Could a state veto the Union, and what made South Carolina back down?', {})]], size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': RUST_LT, 'italic': True}), ("What did democracy mean in Jackson's America, who was it for, and what did the era's reformers claim it still owed?", {'italic': True})]], size=17, color=POWDER, font='Georgia', leading=1.2)
N[2] = "Read the lesson question aloud and split it into its two halves, because the writing task grades both. The first half is constitutional: could a state veto the Union, meaning could one state declare a federal law void inside its borders and stay in the Union while doing it. The second half is practical and historical: whatever the theory said, something made South Carolina repeal its ordinance in March 1833, and students must rank the candidates, isolation, the threat of force, and the offer of lower duties. Warn the class against the easy answer that the state simply lost the argument. South Carolina's leaders believed they had won the argument and repealed anyway, which is exactly why the second half of the question carries the lesson."
notes(s, N[2])
# 3 MAP
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'A grievance, a doctrine, a deadline, a settlement', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The Tariff South Carolina Paid For', 'Duties that taxed the planting states'),
        ('B', 'Calhoun Builds the Doctrine in Secret', 'The Exposition and the compact theory'),
        ('C', 'Webster Answers Hayne in the Senate', "The people's government against the compact"),
        ('D', 'A Toast, a Breach, and a Resignation', 'Jackson and Calhoun divide in public'),
        ('E', 'The Ordinance and the Deadline', 'Nullification enacted, February 1, 1833'),
        ('F', 'Jackson Answers with a Proclamation', 'A government, not a league'),
        ('G', 'Force, Compromise, and a Rehearsal', 'The settlement and what it rehearsed')]
yy = 2.62
for letter, head, sub in rows:
    text(s, 0.92, yy, 0.5, 0.5, letter, size=20, color=RUST_LT, font='Georgia', bold=True)
    text(s, 1.45, yy, 6.6, 0.5, head, size=19, color=CREAM, font='Georgia')
    text(s, 8.2, yy + 0.03, 4.3, 0.5, sub, size=15, color=POWDER)
    yy += 0.62
N[3] = "Walk the map once, slowly, because it is the lesson's whole argument in seven lines. A tariff grievance comes first, and it is economic before it is constitutional. A doctrine follows, built in secret by the sitting vice president. The doctrine is then debated in the Senate, where Webster gives the national answer its lasting form. The argument turns personal at a dinner table and in a resignation. Then the doctrine becomes law in one state, with a date attached. The president answers with a proclamation and a request for force. The settlement pairs that force with a compromise tariff, and the lesson ends on what the whole episode rehearsed for 1861. Students should copy the seven section titles into their notes now."
notes(s, N[3])
# 4 DIVIDER A
divider_text('Section A', 'The Tariff South Carolina Paid For', 'Cotton out, manufactures in, and a tax on everything that arrived.', "Section A is the grievance, and it must land as arithmetic before it lands as politics. South Carolina's economy ran in one direction: cotton sailed out to Britain, and nearly everything the state used, cloth, tools, iron, finished goods, sailed back in on foreign ships. Every duty Congress laid on imports raised the price of what the planting states bought. The protection those duties bought landed in the North, where the sheltered factories stood. Teach students to hold both halves at once, because Calhoun's doctrine in section B only makes sense as an answer to a real bill that arrived every year, in prices a planter could count, from a Congress where his section expected to be outvoted permanently.")
# 5 A CONTENT
content_text('The bill, item by item', ['Cotton sold to the world, goods bought from it', 'Duties of 1816, 1824, and 1828 raised import prices', 'Protection landed on northern factories', 'Fear that Britain would buy less cotton in return', 'A permanent minority does its arithmetic'], "Put the key term on the board in its full form, because the name itself is evidence. " + joined('Tariff of Abominations') + " Notice what the southern name complains about: not taxation itself, but taxation whose benefits flowed one way. The state paid the duties at the Charleston customhouse and watched the protection shelter factories in other states, while its own staple faced a foreign market that American duties could shrink. That arithmetic, repeated across the planting South, is the raw material of the crisis.", kick='Section A')
# 6 DIVIDER B
divider_photo('calhoun-port.jpg', 'Section B', 'Calhoun Builds the Doctrine in Secret', ['The vice president writes for his state, and signs nothing.'], "Introduce the portrait before the doctrine. John C. Calhoun of South Carolina, painted by George Peter Alexander Healy about 1845, was no fringe figure in 1828. He had been a congressman, a secretary of war, and vice president under two presidents, and he had once supported the tariff and the national bank he now opposed. His turn is part of the lesson: as his state's economy stalled and his national ambitions narrowed, he rebuilt his politics around the defense of the planting South. The pamphlet in this section was adopted by the South Carolina legislature in December 1828 with no author's name on it, because the author was still the vice president of the government it argued against.")
# 7 B CONTENT
content_photo('calhoun-port.jpg', 'The Exposition and Protest, 1828', ['The Constitution as a compact of sovereign states', 'No tribunal above the parties to a compact', 'A state convention may interpose and nullify', 'The law sleeps until three fourths amend the Constitution'], "Teach the doctrine in its author's own sequence, and put the unit's central definition on the board whole. " + joined('nullification') + " Calhoun's steps matter as much as his claim. The nullifying act had to come from a convention of the state's people, the same sovereign body that had ratified the Constitution, not from an ordinary legislature. And the doctrine had an ending other than defiance: if three fourths of the states amended the Constitution to grant the disputed power, the state submitted. Calhoun called this a remedy inside the Union, and students should hear that claim fairly before they hear Webster answer it.", kick='Section B')
# 8 B CONTENT 2
content_text('A remedy, its author said, not a revolution', ['Interposition claimed from the Kentucky Resolutions of 1798', 'A veto that arrests the law inside one state', 'The amendment process as the final judge', 'Published without a name, owned at Fort Hill in 1831'], "Slow down on the pedigree Calhoun claimed, because he built his case as inheritance, not invention. The pamphlet's full title belongs in students' notes. " + joined('South Carolina Exposition and Protest') + " Its argument reached back to the Virginia and Kentucky Resolutions of 1798, written against the Alien and Sedition Acts, and read them as a standing grant of state judgment over federal overreach. Opponents answered that 1798 protested and petitioned but never claimed to void a law in force. That gap between protest and nullification is where the next section's debate will be fought.", kick='Section B')
# 9 DIVIDER C
divider_photo('webster-port.jpg', 'Section C', 'Webster Answers Hayne in the Senate', ['A debate over land sales rises to the nature of the Union.'], "Set the Senate scene. Daniel Webster of Massachusetts, painted by Francis Alexander in 1835, was the North's great constitutional lawyer, and Robert Hayne of South Carolina was Calhoun's ally and the nullifiers' voice on the floor. The debate of January 1830 began with a resolution about western land sales, a subject that touched labor, land, and the tariff all at once. Hayne used it to lay out the compact theory in full. Webster's second reply, delivered over two days, January 26 and 27, left land behind entirely and answered the theory at its root. It was printed across the North, and for generations its closing sentence was treated as a civic creed.")
# 10 C CONTENT
content_photo('webster-port.jpg', 'The people, not the states', ['Hayne defends the compact and nullification', "Webster: the people's Constitution, the people's government", 'Answerable to the people, not to state conventions', 'Liberty and union, one and inseparable'], "Give the debate its full name and date in the notes, because students meet it again on the test. " + joined('Webster-Hayne debate') + " Webster's move was to change the author of the Constitution. If the people of the United States made it, then the federal government answers to them, courts judge its laws, and amendments change it; a state convention is a party inside the system, not a judge above it. Hayne never lacked an answer on the compact's history, but Webster's version was the one the North memorized.", kick='Section C')
# 11 VOCAB 1
vocab('Words for the grievance and the doctrine', [(t, SHORT[t]) for t in ['Tariff of Abominations', 'nullification', 'John C. Calhoun', 'South Carolina Exposition and Protest']], "Run this vocabulary slide as a check on the first half of the lesson, term by term, against the short forms on screen. The author of the doctrine deserves his full description read aloud once. " + joined('John C. Calhoun') + " Students should notice how much biography the definition carries: the secret authorship, the two vice presidencies, the resignation, and the later career are all inside it, and each one is a section of this lesson in miniature.")
# 12 DIVIDER D
divider_text('Section D', 'A Toast, a Breach, and a Resignation', 'The president and his vice president take opposite sides at one table.', "Section D explains how a constitutional argument became a broken administration. The Jefferson Day dinner of April 1830 was a party ritual, a sequence of toasts to Jefferson's memory, and both men at the top of the government used it as a platform. Around the toasts stood other quarrels teachers should name plainly: the social campaign against Peggy Eaton, the wife of the secretary of war, which Jackson read as a conspiracy by Calhoun's circle; the contest over who would succeed Jackson, with Martin Van Buren rising as Calhoun fell; and Calhoun's shrinking road to the presidency. Doctrine and ambition cannot be separated in this section, and students judge better when they see both.")
# 13 D CONTENT
content_text('Our federal Union, it must be preserved', ['April 1830, the Jefferson Day dinner', "Jackson's toast looks directly at nullification", "Calhoun answers: the Union, next to our liberty most dear", 'The Eaton affair and the Van Buren succession widen the breach'], "Teach the two toasts as documents, word by word. Jackson's was eleven words of commitment with no qualification, offered while looking, the accounts say, at his vice president. Calhoun's reply placed the Union second, next to liberty, a ranking that sounded loyal and reserved everything, since the whole doctrine claimed to defend liberty against the Union's laws. Everyone at the table understood both toasts as declarations, and the newspapers printed them as such. Ask students which toast a nullifier could repeat without changing a word, and which toast a Unionist could. The exercise shows how much of this crisis was fought in sentences short enough to fit on a glass, long before it was fought in ordinances.", kick='Section D')
# 14 D CONTENT 2
content_text('Calhoun owns the doctrine, then resigns', ['Fort Hill letter, July 26, 1831, under his own name', 'The doctrine defended as the system\u2019s foundation', 'December 1832: the vice presidency given up', 'A Senate seat taken to defend the state\u2019s course'], "Close the section on the resignation, an act without precedent. No vice president had ever resigned the office, and Calhoun gave it up in December 1832 to take a seat in the Senate, trading the second office of the government for a platform to defend a doctrine the president of that government had just condemned. He arrived in Washington as the crisis peaked, so the Senate gained the doctrine's author at the moment the doctrine's state defied the law. Students should register the exchange he made: national office surrendered for sectional leadership, a choice that set the pattern of his remaining career and of the politics he built for the slaveholding South.", kick='Section D')
# 15 DIVIDER E
divider_photo('hayne-port.jpg', 'Section E', 'The Ordinance and the Deadline', ['November 24, 1832: the doctrine becomes state law.'], "Introduce Hayne's face for the section his state now dominates. Robert Y. Hayne, shown in a portrait drawing published in Appletons' Cyclopaedia of American Biography in 1889, had carried the compact argument in the Senate and now, as governor, would command the state's preparations. The trigger for this section is disappointment: the Tariff of 1832 lowered some duties but kept protection, and South Carolina's nullifiers judged half an answer worse than none. A convention elected for the single purpose met in November 1832 and did what the Exposition had only argued. The doctrine now had legal form, a deadline, and armed men behind it, which changed every calculation in Washington.")
# 16 E CONTENT
content_photo('hayne-port.jpg', 'Null, void, and no law', ['The tariffs of 1828 and 1832 declared void in the state', 'Collection forbidden after February 1, 1833', 'Appeals to federal courts barred', 'Secession threatened if duties are collected by force'], "Read the ordinance's operative words aloud, then name the document whole for the notes. " + joined('Ordinance of Nullification') + " Three features deserve the class's attention. The ordinance spoke through a convention, the sovereign form the doctrine required. It set a date, February 1, 1833, turning theory into a countdown both governments had to plan against. And it wrote its own consequence into the text: federal force would dissolve the state's obligation to the Union. The threat of secession was not an addition to nullification in 1832. It was printed inside it.", kick='Section E')
# 17 STAT 0
stat('0', 'other states joined South Carolina', 'Georgia, Alabama, and the rest of the planting South condemned or ignored the ordinance, and South Carolina\u2019s own Unionists organized against it at home.', "Linger on the zero, because isolation is the first cause students should weigh for the repeal. Calhoun's doctrine was designed for a section acting together, and in the winter of 1832 and 1833 the section declined. Other southern legislatures denounced the tariff and then denounced nullification in the same breath, Virginia going furthest in sympathy and still refusing the remedy. Inside South Carolina, Unionist meetings in Charleston and the upcountry organized a counterweight the nullifiers had to reckon with. When the convention finally voted to repeal, it voted as a state that had tested its doctrine's market and found no buyers. Isolation did not refute the argument, but it priced it.", kick='Section E')
# 18 DIVIDER F
divider_photo('jackson-port.jpg', 'Section F', 'Jackson Answers with a Proclamation', ['December 10, 1832: the Union is a government, not a league.'], "Return to the title portrait, now in its working role. Jackson's proclamation of December 10, 1832, was drafted with his secretary of state, Edward Livingston, and addressed past the convention to the people of South Carolina themselves. Its strategy is the section's subject: it refuses the doctrine completely, in the strongest constitutional language any president had used, and in the same document pleads with South Carolinians as countrymen whose fathers had made the Union. Jackson also acted while he argued, asking Congress for authority to collect the duties by force where the customhouses were blocked, and reinforcing the forts and cutters around Charleston. Students should track argument and preparation together.")
# 19 F CONTENT
content_photo('jackson-port.jpg', 'Incompatible with the existence of the Union', ['The power to annul condemned in one sentence', 'A government, not a league, whatever its origin', 'Laws operate on the people, not on the states', 'Disunion by armed force named as treason'], "Teach the proclamation's central sentence as the mirror of Webster's reply. Webster argued from the people's authorship; Jackson argued from consequences and text together, holding the annulment power contradicted expressly by the Constitution's letter, unauthorized by its spirit, and destructive of the object the Constitution was formed to achieve. Note his concession for the sake of argument: even if the Union began as a compact, he wrote, its character now is a government operating on individuals, so the compact road no longer reaches nullification. The proclamation gave Unionists across the South a presidential text to stand on, and several state replies quoted it against their own nullifiers.", kick='Section F')
# 20 F CONTENT 2
content_text('The appeal inside the warning', ['Addressed to the people, over the convention\u2019s head', 'A shared Revolution invoked against disunion', 'Execution of the laws announced as duty', 'Charleston watched, forts strengthened, cutters moved'], "End the section on the proclamation's second register, because Jackson was campaigning as well as commanding. The document asks South Carolinians whether they will destroy a Union their own state helped win, and it separates the state's people from the convention's leaders in a way the ordinance had tried to forbid. That appeal had an audience beyond the state: wavering Unionists inside South Carolina, and legislatures in other southern states deciding whether to condemn the ordinance. It worked alongside the military preparations rather than instead of them. When students reach the settlement, they should be able to say which parts of Jackson's answer were words, which were ships and soldiers, and why he believed he needed both.", kick='Section F')
# 21 DIVIDER G
divider_text('Section G', 'Force, Compromise, and a Rehearsal', 'Two bills in one week, and a state climbs down claiming victory.', "Frame the settlement as a pairing, because neither half works alone in the record. Henry Clay, who had built the protective system the South hated, now brokered its staged dismantling to save the Union he had spent his career knitting together. Jackson, who had asked for force, accepted a compromise that gave South Carolina the falling duties it had demanded since 1828. Each man supplied what the other could not: Clay gave the nullifiers a prize to carry home, and Jackson gave them a reason to take it quickly. The convention that had threatened secession in November voted for repeal in March, and both capitals announced victory in the same week.")
# 22 G CONTENT
content_text('The paired settlement of March 1833', ['The Force Bill arms the president to collect the duties', "Clay's compromise lowers duties by stages to 1842", 'The convention repeals the ordinance', 'The Force Bill is then nullified, to no effect'], "Put the second settlement term into the notes in full, since the test pairs it with the compromise. " + joined('Force Bill') + " Sequence is the teaching point. The Force Bill passed first in the Senate's order of business and the compromise beside it, so South Carolina repealed under a drawn weapon it could describe as unnecessary once the duties were falling. Its final gesture, nullifying the Force Bill itself, cost nothing and conceded nothing verbally, which is why both sides could claim the winter. Ask students which claim survives the chronology better.", kick='Section G')
# 23 STAT 1842
stat('1842', 'the year the compromise duties reach the levels of 1816', 'Nine years of staged reductions, the prize South Carolina carried home from the crisis.', "Use the date to test the victory claims students met in section G. The compromise did not repeal protection at a stroke. It stretched the reduction across nine years, in stages, which let northern manufacturers adjust and let the administration call the settlement gradual rather than surrendered. For South Carolina the schedule was still a real concession won under threat, and nullifiers said so for years: no ordinary congressional minority had ever extracted such a schedule at such speed. Unionists answered that a schedule any Congress could revise was a statute, not a right, and that the doctrine behind the demand had been denied by every other government in the country. Both readings use this date, which is why it belongs on a slide of its own.", kick='Section G')
# 24 VOCAB 2
vocab('Words for the crisis and the settlement', [(t, SHORT[t]) for t in ['Ordinance of Nullification', 'Webster-Hayne debate', 'Force Bill']], "Run the second vocabulary slide backward through the lesson, asking students to attach each term to the section where it did its work. The ordinance belongs to section E, the debate to section C, and the Force Bill to section G, and a student who can make those attachments owns the lesson's skeleton. The full definitions wait in the guided notes for the written work. Close by asking which of the three terms names an argument, which names an act, and which names a threat, and let the class hear how the crisis moved through exactly those three forms in exactly that order.")
# 25 GLANCE
content_text('The lesson at a glance', ['A minority\u2019s grievance becomes a constitutional doctrine', 'The doctrine is debated, personalized, and enacted', 'The president denies it and prepares force', 'Force and compromise together produce repeal', 'The doctrine survives its defeat, in print'], "Synthesize before the exit work, in the lesson's own order. The tariff gave a permanent minority a grievance it could count in prices. Calhoun converted the grievance into a doctrine with a procedure and an ending in amendment. Webster and Jackson answered the doctrine from its two flanks, authorship and consequence, and neither answer moved the state. What moved it was the winter's combination: isolation, an armed president, and a compromise that paid the grievance while denying the doctrine. Hold the last fragment longest. Nullification lost in 1833 and was filed away, argued, printed, and remembered, and the filing is part of American history, not a footnote to it.", kick='Synthesis')
# 26 ANSWERING
content_text('Answering the question', ['Could a state veto the Union? On the record of 1833, no state may, and none has', 'What made South Carolina back down? Rank the causes', 'Isolation first, force second, compromise last and kindest', 'Use the ordinance and the proclamation as your documents'], "Model the ranking the writing task asks for, without confiscating it. A defensible order runs isolation, force, compromise: no ally made resistance lonelier than any argument could, the Force Bill made it dangerous, and the compromise made retreat profitable. Students may rank force first if they argue the convention feared war more than loneliness, but they must argue it from the documents, the ordinance's own secession clause and the proclamation's own threats, not from general impressions of Jackson's temper. Remind the class that South Carolina's leaders left claiming victory, and that a good answer explains a repeal its authors could celebrate, not a surrender they admitted.", kick='Synthesis')
# 27 EXIT
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.7, 11.5, 2.2, 'Answer the question, and exit', size=44, color=CREAM, font='Georgia', leading=1.1)
rule(s, 0.92, 3.5)
text(s, 0.9, 3.85, 11.0, 2.6, ['Exit ticket: the three questions at the end of your guided notes.', 'Writing task: rank the causes of the repeal, from three documents.'], size=22, color=POWDER, space_after=10, leading=1.3)
N[27] = "Close by sending students to the two pieces of written work and naming what each one checks. The exit ticket checks the definition whole, the settlement's two measures, and the victory claim judged from both sides. The writing task checks the ranking, and it should be introduced now, while the documents are fresh: claim first, three pieces of evidence, the strongest fact against the ranking faced directly, and an ending on what the settlement left unsettled. Tell the class the standard plainly. A verdict on 1833 that never quotes the ordinance or the proclamation is an opinion about documents it has not used, and the rubric will grade it as one."
notes(s, N[27])


# Pad any note under 120 words into the 120 to 190 band with a slide specific sentence.
PAD = {
 4: " Keep the customhouse in view while you teach it, because every argument later in the lesson is an argument about who controls that one building and the revenue that passes through it.",
 5: " Have a student read the definition aloud once, slowly, and ask the class to find the two complaints inside it, the prices paid at home and the retaliation feared abroad, before you move on.",
 6: " Mention his earlier career once more before the doctrine, because students who meet Calhoun only as a nullifier miss how completely a national statesman rebuilt himself into a sectional theorist within a single decade.",
 9: " Tell the class that Hayne spoke first and at length, so Webster was answering a complete case, not a fragment, and his reply should be judged as a refutation with its own structure and its own peroration.",
 11: " If time runs short on this slide, protect the Calhoun definition and let the other three go to the guided notes, because his biography is the one the test items will assume students can reproduce accurately.",
 12: " The dinner was held on Jefferson's birthday, April 13, 1830, a detail worth one breath, because both men were claiming the founder's inheritance in front of the party that claimed to own it.",
 13: " A useful check at the end of this slide is to ask which man at that table could afford a public defeat, and let the silence teach how completely Jackson held the stronger hand in 1830.",
 14: " Note the destination he chose: not retirement, not a governorship, but the Senate floor, the one room where the doctrine could be defended in the Union's own chamber while the crisis unfolded outside it.",
 15: " Hayne left the Senate to become governor during this crisis, a second exchange of national office for state command that pairs with Calhoun's resignation and shows students where the nullifiers believed power now lived.",
 17: " Ask the class to name the state they expected to join first, and then sit with the empty list, because the expectation of company was built into the ordinance's timing and its failure shaped everything after.",
 18: " Livingston's hand in the drafting is worth one sentence, since the proclamation's legal architecture came from a Louisianan who knew the compact argument from inside the South and answered it as a southerner.",
 19: " Have students underline the four charges in Jackson's single sentence, incompatible, contradicted, unauthorized, destructive, and notice that he argues from the Union's existence outward, the reverse of the Exposition's road into the question.",
 20: " The reinforcement orders were deliberately quiet, and that quiet is itself a teaching point: Jackson wanted Charleston watched and supplied, not provoked, while the proclamation did its work in print across the South.",
 21: " Clay's role confuses students who filed him as the tariff's author, so name his motive plainly: he would rather lower his own system by stages than watch the Union test whether a state could leave it.",
 24: " End the slide by returning to the ordinance's three operative words, null, void, and no law, since those are the words a student must be able to attach to November 24, 1832, without notes in hand.",
 25: " Resist adding new content here; the synthesis earns its place by arrangement alone, and students who have followed the sections will hear their own notes reorganized into an argument they can now carry into writing.",
 26: " Leave the ranking on the board while students begin the writing task, not as the answer to copy but as the shape of an answer, a ranked claim defended from documents named out loud.",
 27: " Collect the exit tickets at the door and sort them tonight by the second question, since a student who cannot name both settlement measures is not ready for the Bank War lesson that follows.",
}
for i, sl in enumerate(dc.prs.slides, 1):
    if i in PAD:
        cur = sl.notes_slide.notes_text_frame.text
        if len(cur.split()) < 120:
            sl.notes_slide.notes_text_frame.text = cur + PAD[i]

heads = {1:'Opening frame',2:'The lesson question',3:'The lesson in one slide',4:'Section A: The Tariff South Carolina Paid For (divider)',5:'The bill, item by item',6:'Section B: Calhoun Builds the Doctrine in Secret (divider)',7:'The Exposition and Protest, 1828',8:'A remedy, its author said, not a revolution',9:'Section C: Webster Answers Hayne in the Senate (divider)',10:'The people, not the states',11:'Vocabulary: words for the grievance and the doctrine',12:'Section D: A Toast, a Breach, and a Resignation (divider)',13:'Our federal Union, it must be preserved',14:'Calhoun owns the doctrine, then resigns',15:'Section E: The Ordinance and the Deadline (divider)',16:'Null, void, and no law',17:'0: other states joined South Carolina',18:'Section F: Jackson Answers with a Proclamation (divider)',19:'Incompatible with the existence of the Union',20:'The appeal inside the warning',21:'Section G: Force, Compromise, and a Rehearsal (divider)',22:'The paired settlement of March 1833',23:'1842: the compromise reaches the levels of 1816',24:'Vocabulary: words for the crisis and the settlement',25:'The lesson at a glance',26:'Answering the question',27:'Now your turn: answer the question and exit ticket'}
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
