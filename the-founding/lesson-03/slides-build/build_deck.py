#!/usr/bin/env python3
"""The Founding Lesson 3 deck builder. Image led deck: the Dunlap broadside as the title, the Smithsonian Paine engraving, Trumbull's 1819 commemoration, and the broadside again for the adoption."""
import os, sys
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
 'Common Sense': "Paine's January 1776 pamphlet arguing that monarchy itself was corrupt and America should found a republic",
 'natural rights': 'rights belonging to all people by nature, named in the Declaration as life, liberty, and the pursuit of happiness',
 'unalienable rights': 'rights that cannot be taken away or surrendered, given to all men by their Creator',
 'consent of the governed': 'the principle that just powers come from the agreement of the people governed',
 'social contract': 'government as an agreement between rulers and ruled, obedience exchanged for protection of rights',
 'republic': 'a state governed by representatives chosen by its citizens under law, without a king',
 'Declaration of Independence': 'the document of July 4, 1776, declaring the colonies free and independent states and arguing the case',
}

# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'THE FOUNDING \u00b7 LESSON 3', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Declaring Independence', size=30, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'A king becomes the target, a pamphlet changes the question, and a congress argues a people into being.', size=17, color=POWDER)
notes(s, "Open with the document itself. The image is the top of the Dunlap broadside, the first printing of the Declaration of Independence, set in type by John Dunlap at Philadelphia on the night of July 4, 1776, from the copy held by Yale's Beinecke Library. Before this lesson ends, students will know why the words on that sheet had to exist at all. The fighting was already fourteen months old, an army stood before Boston, and yet no American government had said in public what the war was for. This lesson follows the making of the saying: how the king replaced his ministers as the target, how a pamphlet changed what ordinary readers could think, how Congress drafted, cut, and adopted the argument, and what the argument left unsettled.")
# 2 QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('What did the Declaration argue, and why did Americans need an argument at all?', {})]], size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': RUST_LT, 'italic': True}), ('Why did the colonies break with Britain, and what did Americans build in the place of the empire they rejected?', {'italic': True})]], size=17, color=POWDER, font='Georgia', leading=1.2)
notes(s, "Read the lesson question aloud and pull its two halves apart, because the exit ticket and the writing task grade them separately. The first half is about content: what the Declaration argued, its theory of rights and consent and its charges against the king. The second half is about need, and it is the half students skip. Americans in 1776 did not lack grievances or guns. They lacked a public justification that could carry a decade of protest, framed as a defense of British liberties, across the line into independence without breaking apart. The argument had audiences: wavering colonists, the colonies' own assemblies, foreign courts whose help the war required, and posterity. Keep the unit question under it in view. The Declaration is the hinge of this unit: it states why they broke, in words the builders of 1787 would claim to be putting into practice.")
# 3 MAP
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'How a rebellion learned to argue', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The King Becomes the Target', 'Proclamation, Prohibitory Act, hired German soldiers'),
        ('B', 'Common Sense Changes the Argument', 'Paine recasts the quarrel as monarchy itself'),
        ('C', 'The Colonies Turn Toward Independence', 'Instructions sent, constitutions drafted, Lee moves'),
        ('D', 'Drafting and Cutting the Declaration', 'A committee of five, Jefferson writes, Congress cuts'),
        ('E', 'The Argument: Truths and Consent', 'Equal rights, and just powers drawn from consent'),
        ('F', 'The Argument: Charges Against the King', 'A long train of abuses, charged to the king alone'),
        ('G', 'Adoption, Risk, and the Standard Left Open', 'July 2 and July 4, the pledge, the unfinished standard')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This map follows the guided notes section by section. Section A explains the turn of the target: through 1775 the resistance blamed Parliament and the king's ministers, and the king's own acts of that year ended the arrangement. Section B gives the turn its pamphlet, because Common Sense reached readers no assembly address could reach. Section C is the political mechanics, instructions and constitutions, without which the vote of July could not be taken. Section D slows down on the drafting, including the passage Congress removed. Sections E and F read the adopted argument in its own order, theory first and charges second. Section G follows the paper into the world, the broadside, the army reading, the signatures, and the standard the words set for people the document did not free. Tell students to track one question through every section: who is each text trying to persuade, and of what?")
# 4 DIVIDER A
divider_text('Section A', 'The King Becomes the Target', 'Through 1775 the resistance blamed the ministers. In one year, the king made himself the argument.',
 "Teach the starting position honestly, because students assume independence was always the goal. Through 1775 the resistance described itself as a defense of British liberties against Parliament and the king's ministers. Colonists petitioned, boycotted, and finally fought while calling themselves loyal subjects of a king misled by bad advisers, and the Olive Branch Petition of July 1775, which this lesson reads in the activity, professes devotion to the king's person in so many words. Independence was widely called ruinous and treasonous in the same newspapers that cheered the militia. What dissolved that position was not an American pamphlet. It was the king's own conduct across the second half of 1775, three acts that colonists read together as the sovereign making war on his subjects. Once the king is the aggressor, the old frame, loyal subjects against wicked ministers, cannot hold, and the argument of 1776 becomes possible.")
# 5 CONTENT A
content_text('The king closes the middle ground', ['The resistance claims British liberties, not independence', 'August 1775: the colonies proclaimed in open rebellion', 'The Prohibitory Act puts American trade outside his protection', 'German soldiers hired to fight in America', 'Colonists read the three acts as the king making war'],
 "Work the three acts as one sequence, in the order colonists met them. First, the Proclamation of Rebellion of August 23, 1775: the king declared the colonies in open and avowed rebellion, ordered every officer and loyal subject to suppress it, and refused to receive the Olive Branch Petition when it reached London. Second, the Prohibitory Act of December 1775, by which Parliament, with the king's assent, placed American ships and goods outside the king's protection, to be seized as an enemy's property in a war the king's government was now waging in form. Third, the hiring of German soldiers, regiments from the German states contracted to fight in America, which colonists read as a king importing foreign swords against his own subjects. State the reading colonists put on the sequence, because the Declaration depends on it: a king who declares his subjects rebels, strips them of his protection, and hires strangers to subdue them has dissolved the bond of allegiance from his own side.")
# 6 STAT A
stat('30,000', 'German soldiers hired across the war', 'The standard count of auxiliaries Britain hired from the German states, stated here as the record\u2019s figure',
 "Stop on this figure and label it the way the lesson labels it: some thirty thousand German soldiers hired across the whole war, the standard count historians work from, not a muster roll anyone counted on one day. The number did political work in 1776 out of proportion to any single landing. News that the king had contracted for foreign regiments reached the colonies through the winter and spring, and it landed on readers already holding the Proclamation of Rebellion and the Prohibitory Act. A tax dispute does not require hired armies. Colonists who had blamed ministers now asked what kind of king sends strangers to fight his own subjects, and the Declaration answers by listing the mercenaries among its closing charges, a king transporting large armies of foreign mercenaries to complete works of death and desolation. Teach the figure with its label every time: an estimate and a standard count, not a slogan.")
# 7 DIVIDER B
divider_photo('paine-port.jpg', 'Section B', 'Common Sense Changes the Argument', ['Philadelphia, January 1776: fewer than fifty pages that refused the old question.'],
 "The portrait on this slide is Thomas Paine as an engraving of 1791, made after Charles Willson Peale and held by the Smithsonian's National Portrait Gallery, a likeness from fifteen years after the pamphlet. Paine himself was an unlikely author of a founding: an English immigrant who reached Philadelphia in 1774 with a letter from Benjamin Franklin, a failed staymaker and dismissed excise officer who had been in America fourteen months when Common Sense appeared in January 1776. That outsider standing is part of the pamphlet's force. Paine owed the colonial gentry nothing and wrote past them, to readers of taverns and workshops, in the plain language of the Bible they knew. Introduce the section's claim now: before Paine, the quarrel was about which Britons had broken the constitution. After Paine, the quarrel could be about whether kings should exist at all.")
# 8 CONTENT B
content_text('Not a tax. A system.', ['Common Sense appears in January 1776', 'The problem is monarchy itself, not one minister', 'Corrupt in Scripture, absurd in nature', 'Hereditary succession passes power to children and fools', 'A continent should not be governed by an island'],
 "State the reframing as a change of defendant. Every earlier protest had indicted a measure or a ministry: the stamp tax, the Townshend duties, Lord North. Paine indicted the institution. Monarchy, he argued, was corrupt in Scripture, where the demand for a king is recorded as a rejection of God's rule, and absurd in nature, since no family is born entitled to rule the rest. Hereditary succession, his sharpest practical point, guarantees nothing about the successor: power passes to children and fools as readily as to the able, and the system's admirers must pretend otherwise every generation. The island and continent line does the geographic work: a great continent permanently governed by a small island off Europe violates the plain proportions of things. Then make the formal point. Paine wrote in short biblical sentences and tavern arguments, and readers who had never opened Locke could follow him to conclusions Locke's readers had reached by study.")
# 9 STAT B
stat('100,000+', 'copies of Common Sense sold within months', 'Well over one hundred thousand, by the estimates historians work from, in colonies of about two and a half million people',
 "Give this figure its label before its size: well over one hundred thousand copies within months, by the estimates historians work from. No audited sales ledger survives, pamphlets were shared, read aloud, and reprinted in newspaper extracts, and any honest teaching keeps the estimate flag flying, exactly as the reading does. Then make the class feel the proportion the estimate implies. In colonies of about two and a half million people, a sale above one hundred thousand pamphlets, each passing through many hands and many readings aloud, put Paine's argument within reach of a large share of the literate population in a single season. Printers across the colonies issued their own editions. The pamphlet's reach is the mechanism of section C: when assemblies began instructing their delegates that spring, they were answering constituents whom Paine, among others, had already persuaded that independence was thinkable.")
# 10 DIVIDER C
divider_text('Section C', 'The Colonies Turn Toward Independence', 'Spring 1776: conventions write constitutions, assemblies send instructions, and Lee moves the resolution.',
 "Slow the class down on the mechanics, because the drama of July hides them. Independence was not declared by a mood. Through the spring of 1776, colony after colony took the legal steps that made a vote possible: royal governors fled or were arrested, provincial congresses and conventions governed in fact, several colonies drafted new state constitutions as their royal charters collapsed, and assemblies instructed their delegates in Congress to vote for independence. The instructions carried weight because many delegates lacked authority from home to take the final step at all. A delegate voting independence without instructions risked repudiation by the colony that sent him. By June, enough instructions had arrived to move, and not quite enough to move unanimously, which is why the resolution and the calendar of this section belong together in students' notes.")
# 11 CONTENT C
content_text('Instructions before independence', ['Royal governments collapse or flee', 'New state constitutions drafted as charters fall', 'Assemblies instruct delegates to vote for independence', 'June 7: Lee moves that the colonies ought to be free and independent', 'Congress postpones the vote three weeks'],
 "On June 7, 1776, Richard Henry Lee of Virginia rose in Congress and moved the resolution his colony's convention had instructed him to offer: that the United Colonies are, and of right ought to be, free and independent States. Teach the sentence's shape, because the Declaration exists to defend it: Lee asserts a present right, not a request. Congress then did the most instructive thing in the whole story. It postponed the vote for three weeks, to let the remaining colonies instruct their delegations, and it used the interval to appoint the committee that would draft the public statement. The delay is the lesson's evidence that the argument was a need and not a decoration. Congress could have voted at once. It chose instead to secure its authority at home and its justification abroad before it acted, and students should be able to say why both errands were necessary.")
# 12 DIVIDER D
divider_photo('trumbull-port.jpg', 'Section D', 'Drafting and Cutting the Declaration', ['The image is John Trumbull\u2019s painting, finished in 1819, a later commemoration, not the scene itself.'],
 "Caption this image with its date every time it appears, because the lesson's honesty about images matches its honesty about texts. The painting is John Trumbull's Declaration of Independence, finished in 1819 for the United States Capitol, showing the committee of five presenting its draft to Congress. It is a commemoration made forty three years after the event, and its figures were never in one room at one time; Trumbull painted the portraits from life where he could and composed the ceremony himself. What actually happened in June 1776 was quieter. Congress appointed a committee of five, John Adams, Benjamin Franklin, Roger Sherman, Robert Livingston, and Thomas Jefferson, and Jefferson, the youngest of them and the one with the reputation for a pen, did the writing alone in a rented room. The drafting took days. The cutting, which is this section's real subject, took Congress two more.")
# 13 CONTENT D
content_text('Five men, one pen, and a hard edit', ['A committee of five: Adams, Franklin, Sherman, Livingston, Jefferson', 'Jefferson writes at a portable desk in a rented room', 'He draws on natural rights and a decade of grievance lists', 'Congress cuts about a quarter of the draft', 'Sentences tightened, whole passages struck'],
 "Give Jefferson's materials their names, because the draft was not spun from air. He drew on the language of natural rights that colonial writers had used for a decade, on the grievance lists assemblies had been writing since the Stamp Act Congress, and on his own earlier draft constitution for Virginia. Congress then edited the draft hard on July 2 and 3, cutting about a quarter of the text, tightening sentences and striking whole passages. Jefferson sat silent and took the changes hard; his rough draft, with the cuts visible, survives as this lesson's central artifact in the activity. Teach the edit as authorship, not vandalism. Congress was not polishing a poem. It was building a coalition document that thirteen colonies, and the delegates answerable to them, could sign, and everything it struck should be read against that standard before students judge it.")
# 14 CONTENT D2
content_text('The largest cut', ['Jefferson charges cruel war against human nature itself', 'The slave trade: a market where men should be bought and sold', 'Colonial laws to end the trade, blocked by the king\u2019s negative', 'Struck for South Carolina and Georgia', 'Northern delegates tied to the trade would not press it'],
 "Read the deleted passage itself in the activity, and prepare students for its double character here. Jefferson charged that the king had waged cruel war against human nature itself in the slave trade, violating the sacred rights of life and liberty of a distant people who never offended him, carrying them into slavery in another hemisphere, and blocking every colonial attempt to prohibit or restrain the commerce. The charge is real, and so are its limits: it blames the king for a trade colonial buyers sustained, and its last lines fear the enslaved as a weapon the king was exciting against their masters. The record of the cut is plain. South Carolina and Georgia would not accept it, and northern delegates whose ports profited from the trade would not press it, and the passage fell. The adopted document therefore opens by declaring all men created equal and says nothing about the trade that brought so many of them to America in chains.")
# 15 STAT D
stat('1/4', 'of Jefferson\u2019s draft, cut by Congress', 'About a quarter of the text tightened or struck, including the whole charge on the slave trade',
 "Use this slide to fix the scale of the edit in memory, because students picture Congress changing commas. About a quarter of Jefferson's text went: sentences shortened throughout, references trimmed, and at least one whole argument, the slave trade charge of the last slide, removed entire. The proportion is the reading's figure, about a quarter, and it is an approximation from comparing the rough draft with the adopted text, which students can test themselves in the activity, where the draft and the adoption sit two stations apart. Ask the class to hold two judgments at once, because the documents require both. The edit made the Declaration signable by delegations that would have refused the longer text. The edit also removed the document's one direct charge against the institution its preamble's logic condemned, and the republic was founded with that silence inside its founding text.")
# 16 DIVIDER E
divider_text('Section E', 'The Argument: Truths and Consent', 'The preamble states the theory before it names a single injury.',
 "Teach the preamble as a piece of engineering, because its order is its argument. The Declaration does not open with a crime. It opens with a theory of what government is for, then states the rule for ending one, then files its evidence, then announces the conclusion. That order was a choice with audiences in mind: a candid world, as the text says, was to be given causes, not just news. The theory itself came out of the social contract tradition students met in the Colonial unit's Enlightenment lessons, but Jefferson compressed it into sentences a newspaper reader could carry whole. Prepare the vocabulary now, because the next slide and the exit ticket both run on it: natural rights, unalienable rights, and consent of the governed are not decorations on this document. They are its load bearing claims, and each one will be defined word for word before the lesson ends.")
# 17 CONTENT E
content_text('Truths held to be self-evident', ['All men are created equal', 'Rights endowed by their Creator, not granted by government', 'Life, liberty, and the pursuit of happiness', 'Just powers from the consent of the governed', 'A destructive government may be altered or abolished'],
 "Work the sentence chain link by link, in the order the text builds it. First, equality and endowment: rights are not granted by kings or parliaments, so they cannot be withdrawn by them; they are held by nature and by the Creator's gift. Second, the purpose of government: to secure those rights, and no other commission. Third, the source of power: the consent of the governed, which makes the people, not the Crown, the fountain of just authority. Fourth, the remedy: when a government becomes destructive of those ends, the people may alter or abolish it. Then state the discipline Jefferson builds into the same paragraph, because section F depends on it. Prudence warns that long established governments should not be changed for light and transient causes. The preamble itself demands a long train of abuses before its remedy may lawfully be used, and the grievances are that demand being met.")
# 18 DIVIDER F
divider_text('Section F', 'The Argument: Charges Against the King', 'Every charge names the king alone, because the bond being dissolved ran to the Crown.',
 "Explain the defendant before the charges, because it puzzles every class. A decade of colonial protest had charged Parliament: its taxes, its acts, its claim to legislate in all cases whatsoever. The Declaration charges Parliament with almost nothing. Every grievance names the king. The reason is structural, and students should state it without prompting by the end of the section: the legal bond between the colonies and Britain ran to the Crown. Colonies held their charters from kings, their governors were the king's, and allegiance was owed to the king's person. To dissolve that bond, the indictment had to name the party to it. Parliament's acts appear in the document only as measures the king assented to or combined with others to impose. The king was also, by 1776, the defendant events had prepared: he had proclaimed the rebellion, signed the Prohibitory Act, and hired the regiments of section A.")
# 19 CONTENT F
content_text('A long train of abuses', ['Assent refused to necessary laws', 'Assemblies dissolved, justice obstructed', 'Standing armies kept in times of peace', 'Trade cut off, taxes imposed without consent', 'Trial by jury denied, colonists sent overseas for trial'],
 "Teach the grievances as categories rather than as a chant, because the list is organized by the parts of government the king is charged with corrupting. He blocked legislation, refusing assent to wholesome laws and dissolving the assemblies that passed them. He bent justice, obstructing courts, making judges depend on his will, denying trial by jury, and transporting colonists overseas for trial. He militarized peace, keeping standing armies among the colonists without their legislatures' consent. He strangled livelihood, cutting off trade and imposing taxes without consent, the charge that folds the whole decade of tax protest into the king's indictment. Each charge answers the preamble's caution from the last section: these are not light and transient causes but a pattern pursuing invariably the same object, the establishment of absolute tyranny over the states. The next slide takes the charges where they stop being about government and become about war.")
# 20 CONTENT F2
content_text('The closing charges', ['Coasts plundered, towns burned, mercenaries hired', 'Domestic insurrections excited: Dunmore\u2019s freedom offer', 'The frontiers charge, in the document\u2019s own words', 'Both charges stand in the same document as equal creation'],
 "Teach the two closing charges plainly and in the document's own words, because this lesson does not soften its central text. The Declaration charges that the king has excited domestic insurrections amongst us: that means Lord Dunmore's proclamation of November 1775, offering freedom to enslaved people who left rebel masters and bore arms for the king, which the slaveholding signers counted among the king's crimes. It charges that he has endeavoured to bring on the inhabitants of our frontiers the merciless Indian Savages, whose known rule of warfare is an undistinguished destruction of all ages, sexes and conditions: that is the document's phrase for Native nations who allied with Britain to defend their own lands. Hold both charges up beside the preamble without commentary doing the students' work for them. The same text that declares all men created equal lists an offer of freedom to the enslaved as a grievance and denies Native peoples the standing of nations. That tension is not a footnote to the founding. It is in the founding document, in its closing charges, and the rest of this course keeps meeting it.")
# 21 DIVIDER G
divider_photo('broadside-port.jpg', 'Section G', 'Adoption, Risk, and the Standard Left Open', ['The Dunlap broadside carried the adopted words to the states within days.'],
 "The image is the Dunlap broadside again, the whole sheet this time, and its journey is this section's story in one object. Congress voted independence on July 2, 1776, adopting Lee's resolution, and adopted the Declaration's text on July 4 after two days of editing. Dunlap printed the text that night, and copies rode to the states, the armies, and the newspapers. Washington had it read to his army at New York on July 9, the day the city's crowd pulled down the lead statue of George III and melted it for bullets, a piece of political theater no curriculum should skip, because it shows the argument becoming action in the street. The engrossed parchment copy was signed by most members on August 2. What those signatures meant in law, and what the document did not do, are the two halves of this closing section.")
# 22 CONTENT G
content_text('July 2, July 4, August 2', ['July 2: Congress votes independence', 'July 4: the text adopted, printed the same night', 'July 9: read to the army as the king\u2019s statue falls', 'August 2: most signers sign the engrossed copy', 'Abigail Adams, that March: remember the ladies'],
 "Close the narrative with the pledge, because it prices the document. For the support of this Declaration, the signers mutually pledged their lives, their fortunes, and their sacred honor. In British law the text they signed was a confession of treason, and every signer knew the penalty. Then turn to the limit the reading insists on, because ending on the pledge alone teaches half the lesson. The Declaration freed no one by itself. It settled nothing about who counted as the people. That March, Abigail Adams had written to her husband in Congress asking him to remember the ladies in the new code of laws, warning that women would not hold themselves bound by laws in which they had no voice or representation. John Adams answered with a laugh. The standard stood anyway, on paper, in sentences about equality and consent wide enough that the people left outside them could, and in later years did, quote them back at the republic.")
# 23 GLANCE
s = slide(NAVY)
kicker(s, 'The argument at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Target, pamphlet, theory, charges, decision', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The target', 'The king himself, by his acts of 1775', 'The bond ran to the Crown'),
        ('The pamphlet', 'Common Sense, January 1776', 'Monarchy itself put on trial'),
        ('The theory', 'Rights by nature, power by consent', 'The preamble\u2019s social contract'),
        ('The charges', 'A long train of abuses', 'Charged to the king alone'),
        ('The decision', 'July 2 and July 4, 1776', 'Argued in public, signed in August')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 0.86
notes(s, "This slide mirrors the closing table of the guided notes, The Argument at a Glance, and students should complete that table now from memory where they can. Check the table with the two questions that expose shallow answers. First, which rows describe Americans being acted on, and which describe them acting? The target row belongs to the king's initiative: proclamation, Prohibitory Act, hired regiments. The pamphlet, theory, and decision rows belong to Americans answering in print, in instructions, and in Congress. Second, which row reaches furthest past 1776? The theory: consent of the governed and equal natural rights became the standard every later American argument, including the arguments of the people the Declaration left out, would appeal to. The table is the lesson in miniature: a target imposed by events, an argument built to answer it, and a decision whose words outlasted its makers' intentions.")
# 24 VOCAB A
vocab('Words for the pamphlet and the rights', [(t, SHORT[t]) for t in ['Common Sense', 'natural rights', 'unalienable rights', 'consent of the governed']],
 "Four terms, word for word as the guided notes print them. " + "Common Sense: " + TD['Common Sense'] + ". " + "natural rights: " + TD['natural rights'] + ". " + "unalienable rights: " + TD['unalienable rights'] + ". " + "consent of the governed: " + TD['consent of the governed'] + ".")
# 25 VOCAB B
vocab('Words for the contract and the new state', [(t, SHORT[t]) for t in ['social contract', 'republic', 'Declaration of Independence']],
 "Three more terms, again matching the guided notes exactly, and students should copy the definitions because the unit test draws on them. " + "social contract: " + TD['social contract'] + ". " + "republic: " + TD['republic'] + ". " + "Declaration of Independence: " + TD['Declaration of Independence'] + ". Press the link between the first two terms before the exit ticket. The social contract explains why a government may fall; the republic names what the Americans built in the fallen government's place, representatives chosen under law in place of a hereditary king.")
# 26 SYNTHESIS
content_text('Answering the question', ['The argument: rights by nature, power by consent, a contract broken', 'The proof: a long train of abuses charged to the king alone', 'The need: loyalty, law, and foreign courts required a stated cause', 'The limit: the standard set, the slave trade charge struck'],
 "Run the synthesis as the writing task rehearsal, and build it from the class's own answers before summarizing. The Declaration argued that government rests on a contract: rights held by nature, powers drawn from consent, and a remedy of alteration or abolition when the contract is broken. It proved the breach with a long train of abuses charged to the one defendant the law of allegiance allowed, the king. And it existed because the break it announced could not survive as a mere act of arms: colonists who had called themselves loyal Britons, assemblies whose instructions ran only so far, and foreign courts deciding whether to treat with rebels all required the cause stated in a form they could judge. Test the synthesis against the document's own silences before closing: the charge Congress struck, and the peoples the closing grievances name without freeing.")
# 27 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4, ['What did the Declaration argue, and why did Americans need an argument at all?'], size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Argument of 1776: five records, the claim in each, then a verdict'),
        ('Notebook', 'Notebook page: the Declaration\u2019s argument as a chart, claim by claim'),
        ('Quick check', 'The Argument in the Text: the preamble and the grievances, sourced and read closely'),
        ('Writing', 'Why an Argument: the claim and its audiences in one essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: natural rights defined with the three rights named, the largest cut stated with its reason, and the lesson question in two or three sentences.', size=15, color=POWDER)
notes(s, "Close by handing the lesson to the work. In the activity, The Argument of 1776, each group works five records, Common Sense, Jefferson's rough draft with the passage Congress struck, the Declaration as adopted, the king's Proclamation of Rebellion, and the Olive Branch Petition, states each record's claim about where legitimate government comes from, and judges which record would most persuade a wavering colonist in June 1776 and what it would have to overcome in him. The notebook page rebuilds the Declaration as a chart of claim, evidence, and what each part settles or leaves open. The quick check, The Argument in the Text, puts the preamble and the grievances side by side and tests whether students can read the theory against its charges. The writing task, Why an Argument, requires the lesson's double answer in essay form. The exit ticket has three parts, and students should leave with all three ready.")

dc.save(OUT)
