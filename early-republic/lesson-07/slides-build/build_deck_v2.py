#!/usr/bin/env python3
"""Early Republic Lesson 7 deck, The Monroe Doctrine and the Missouri Compromise."""
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
text(s, 0.9, 5.32, 11.5, 0.4, 'THE EARLY REPUBLIC AND EXPANSION · LESSON 7', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Monroe Doctrine and the Missouri Compromise', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Two settlements, 1820 and 1823', size=17, color=POWDER)
notes(s, "The image is a map of the Missouri Compromise published by the McConnell Map Company in 1919 from Library of Congress materials, drawing the line of 1820 as later Americans studied it. Open by placing this lesson after Lesson 6. The Era of Good Feelings built a bank, a tariff, and a nationalist Court, and it left one question waiting for a territory to ask it. This lesson holds two settlements from the same season of Monroe's presidency. One faced outward, telling Europe a hemisphere was closed. One faced inward, drawing a line across the Louisiana Purchase and calling the drawing a settlement of slavery's expansion. Tell students both settlements will be priced as well as praised, in the words of the men who made them and of one man who heard a fire bell in them.")

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("What did the settlements of 1820 settle, and what did they only postpone?", {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the United States turn its Constitution into a working government, and what did continental expansion do to the republic that government served?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Read the question in its two halves and keep both alive all hour. Settle is a strong word, and the men of 1820 used settlements to end arguments they could not win outright. The Missouri Compromise settled an admission crisis in Congress. The Monroe Doctrine settled the words in which the republic would address Europe. Postpone is the question's second half, and it asks what each settlement left for later Americans to fight over. A line drawn across a map leaves the next territory undecided. A declaration backed by another nation's fleet leaves its enforcement to a later generation. By the end of the hour students should be able to name what each settlement decided, what each one deferred, and whose warning, written in April 1820, predicted the deferral in advance.")

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'A hemisphere declared, a line drawn', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'Two settlements in one season', 'Outward and inward at once, answered by declaring'),
        ('B', 'An empire dissolving', 'New republics, Florida taken, Russia claiming, Britain proposing'),
        ('C', 'The Doctrine declared', 'December 2, 1823: closed to colonization, interference dangerous'),
        ('D', 'What the Doctrine could and could not do', 'Confidence ahead of force, sheltered by the British navy'),
        ('E', 'Missouri applies', 'Eleven and eleven, the Tallmadge Amendment, a sectional vote'),
        ('F', 'The settlement of 1820', 'Maine free, Missouri slaveholding, the line at thirty six thirty'),
        ('G', 'The fire bell', 'Jefferson to Holmes, April 22, 1820: a reprieve only')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This slide is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A frames the two settlements together. Section B builds the outward situation, a dissolving Spanish empire, the treaty of 1819, a Russian claim, and a British proposal. Section C states the Doctrine in Monroe's own words, and section D weighs it honestly against the sea power of 1823. Section E opens the Missouri crisis and the Tallmadge Amendment. Section F gives the settlement of 1820 in its three parts, including the exception inside its own line. Section G closes with Jefferson's letter to John Holmes, the warning the whole lesson is judged against in the writing task.")

# 4 A DIVIDER
divider_photo('monroe-port.jpg', 'Section A', 'Two Settlements in One Season',
              ['James Monroe, by Samuel Morse, about 1819.', 'White House collection, public domain.'],
              "The portrait shows James Monroe about 1819, painted by Samuel Morse, the inventor, who painted presidents before he built telegraphs, and it hangs in the White House collection. Monroe presides over both settlements in this lesson, and students should notice how different his two roles are. In the Missouri crisis he is a signer, approving an act Congress built on March 6, 1820, after months of sectional argument he did not control. In the Doctrine he is a voice, delivering words his secretary of state drafted, in a message no Congress voted on at all. One settlement is a law with votes behind it. The other is a declaration with a navy it did not own behind it. Keep that contrast in front of the class from this slide forward, because the closing verdict asks which ground was firmer, and the forms of the two acts are part of the evidence.")

# 5 A CONTENT
content_text('Facing outward and inward at once',
             ['Abroad, an empire was dissolving in revolution.',
              'At home, a territory was asking to enter.',
              'The question underneath was slavery in new lands.',
              'The method, both times, was to declare a line.',
              'The test was what a declaration could hold.'],
             "Teach the frame before the facts, because the frame is the lesson's argument. The republic in 1820 had learned to settle by declaring. It declared principles to Europe and drew lines at home, and both acts carried the confidence of a government whose machinery, built across this unit, now ran. But a declaration settles only what other people accept or cannot challenge. Europe could challenge the Doctrine and chose, for reasons of its own, not to sail against the British fleet. The sections could challenge the Missouri line, and for a generation they chose the map over a renewed fight. Students should watch acceptance, not announcement, as the measure of each settlement. When a settlement rests on other people's choices, its ground is exactly as firm as those choices, and no firmer. That sentence is the hour in one line, and the records at the stations will test it twice.",
             kick='A · Two settlements', size=23)

# 6 B DIVIDER
divider_text('Section B', 'An Empire Dissolving',
             'New republics, a treaty line to the Pacific, and a British proposal.',
             "Section B builds the outward situation piece by piece, and each piece carries a date students must hold. Spain's American empire broke apart in revolutions through the 1810s and 1820s, and peoples from Mexico to Chile declared republics and fought to keep them. The United States recognized the new governments in 1822, a step short of alliance and long on sympathy and trade. Behind the recognition stood an older settlement, the Adams-Onís Treaty of 1819, which had taken Florida and drawn a line of claims to the Pacific. Against that background two new pressures arrived together. Russia claimed the Pacific coast in 1821, and rumors ran that Europe's monarchies might help Spain recover its colonies by force. Britain answered the rumors with a proposal, and the proposal forced the cabinet argument the next slides take up in Adams's own image.")

# 7 B CONTENT
content_photo_s('jqa-port.jpg', 'Speak alone, or follow the fleet',
             ['Canning proposed a joint declaration.',
              'Jefferson and Madison advised accepting it.',
              'Adams argued for declaring alone.',
              'The image was a cockboat in the wake of a British man of war.',
              'Monroe adopted Adams and his course.'],
             "The portrait is George Peter Alexander Healy's John Quincy Adams of 1858, painted after Adams's death from earlier likenesses, in the White House collection. Teach the cabinet argument as a contest over what a declaration is for. Canning's proposal offered safety: Britain's fleet already opposed reconquest, and a joint statement would borrow that strength openly. Jefferson and Madison, consulted in retirement, both advised Monroe to accept. Adams argued the opposite on grounds of standing. A joint declaration would read in Europe as American policy trailing British policy, his cockboat behind the man of war, and it would bind the United States to British purposes, which were trade purposes. Declaring alone claimed the hemisphere's spokesmanship for the United States itself. Monroe chose Adams's course, and the choice, not the fleet, is what the Doctrine added to the balance of 1823.",
             kick='B · An empire dissolving')

# 8 STAT 1822
stat('1822', 'the year the United States recognized the new American republics',
     'Recognition without alliance, five years after Monroe took office and one year before the Doctrine',
     "Let the date discipline an easy exaggeration. The United States did not create Latin American independence, and it did not defend it with arms in these years. What it did in 1822 was recognize governments that had won their own wars, from Mexico to Chile, accepting them as facts and opening trade and diplomacy with them. Recognition is a legal act with real weight: it told Spain its empire was over in American eyes, and it told the new republics whose friendship Washington wanted. But it promised no soldiers and no ships. Students who keep the modesty of 1822 in view will read 1823 correctly. The Doctrine grew out of recognition's logic, sympathy and interest stated as principle, and it inherited recognition's limit as well. Words were the instrument, because words, trade, and the British fleet were the instruments the republic actually held in its hands that season.",
     kick='B · An empire dissolving')

# 9 C DIVIDER
divider_text('Section C', 'The Doctrine Declared',
             'December 2, 1823: a hemisphere closed, in the annual message.',
             "Section C slows down on the document itself, Monroe's annual message to Congress of December 2, 1823, because students meet the Monroe Doctrine as a slogan and must learn to read it as a text with three distinct positions. Annual messages are reports, not laws, and nothing in the Constitution gave this one force. Its authority came from repetition, as later presidents and Congresses chose to stand on it across two centuries. Adams drafted its central passages, and the class should hold authorship and delivery apart: the doctrine carries Monroe's name because Monroe delivered it and owned it before the country. The next slide takes the three positions in the message's own order, colonization, interference, and the American pledge in return, and students should copy the order as well as the claims.")

# 10 C CONTENT
content_text('Three positions in one message',
             ['The continents were closed to future colonization.',
              'European interference was dangerous to our peace and safety.',
              'Existing colonies faced no American interference.',
              'Europe’s own wars were to have no American part.',
              'The words were drafted by Adams and delivered by Monroe.'],
             "Work the three positions slowly, in the bank record's own words, which Station 1 of the activity quotes. First, the American continents, by the free and independent condition they have assumed and maintain, are henceforth not to be considered as subjects for future colonization by any European powers. Second, any attempt to extend the European political system to any portion of this hemisphere will be considered dangerous to the peace and safety of the United States. Third, the reciprocal pledge: the United States has never taken part in Europe's wars over European concerns, and it will not disturb existing colonies. Note the asymmetry students often miss. The message claims a whole hemisphere against future moves, and in exchange it surrenders nothing the United States was positioned to do in Europe anyway. A strong claim, cheaply insured, is still a claim whose bill comes due later.",
             kick='C · The Doctrine declared', size=23)

# 11 STAT 1823
stat('1823', 'the Doctrine declared, by a nation that could not enforce it alone',
     'Its shelter was the British navy, whose trade interest ran the same way',
     "Stand on the enforcement fact for a full minute, because the Doctrine's reputation for power was built later and students import it backward into 1823. The United States Navy of 1823 was a respectable small force, built for coastal defense and single ship actions of the kind Lesson 5 studied. It could not have barred a determined European expedition from the Caribbean or the Pacific coast, and no one in Monroe's cabinet believed otherwise. The declaration floated, in the reading's phrase, on the British navy, the strongest fleet afloat, whose government wanted the new republics open to British goods and closed to rival empires. Interest, not alliance, did the work: Britain had refused the joint declaration's counterpart terms and acted from its own ledger. When British interest later ran another way, the Doctrine would need American power behind it or stand exposed as words. Section D takes up that exposure directly.",
     kick='C · The Doctrine declared')

# 12 D DIVIDER
divider_text('Section D', 'What the Doctrine Could and Could Not Do',
             'A claim addressed to three audiences, and durable by later choice.',
             "Section D is the lesson's honesty section on the outward settlement, and it should be taught at the reading's pace. The Doctrine could do three things in 1823. It could state a principle clearly enough that Europe had to reckon with American objection. It could speak to the new republics as a promise of friendship from the hemisphere's oldest republic. And it could speak to American voters, claiming a continental standing for their government. What it could not do was stop a fleet. No European power tested it with an expedition in those years, and students should be careful about assigning the credit, since British sea power, British trade interest, and the republics' own armies all stood between Spain and reconquest. The Doctrine's durability is a separate fact: later generations kept choosing to stand on it, and a later unit studies the corollary one president added nearly a century on.")

# 13 D CONTENT
content_text('Durable because later generations chose it',
             ['Addressed to Europe, it stated a warning.',
              'Addressed to the republics, it claimed a friendship.',
              'Addressed to voters, it asserted a standing.',
              'In 1823 it was enforced by British interest.',
              'It was kept alive by later American choices.'],
             "Draw the audiences apart on the board, because conflating them produces the two standard errors about this document. The first error calls the Doctrine a bluff Europe feared. Europe's chancelleries noted the message, and several dismissed a claim unbacked by a fleet, in private correspondence students can be told exists without being quoted here. The second error calls it empty words. Words that a government repeats, teaches, and builds policy on for two centuries are a political fact in themselves, and the corollary of a later unit is unintelligible without the text of 1823 beneath it. The honest sentence holds both halves. In 1823 the Doctrine was a claim whose enforcement belonged to others. Across time it became a commitment because Americans in office kept deciding to treat their predecessors' words as binding on themselves. Institutions run on exactly that kind of decision, and students met the same mechanism in Washington's precedents in Lesson 1.",
             kick='D · The Doctrine weighed', size=23)

# 14 E DIVIDER
divider_photo('map-port.jpg', 'Section E', 'Missouri Applies',
              ['The compromise line on a later map.', 'McConnell Map Co., 1919, Library of Congress.'],
              "The map is the McConnell Map Company sheet of 1919, held by the Library of Congress, drawing the settlement of 1820 for a later century's classrooms. Section E turns from the hemisphere to a single territory's application, and the turn should feel abrupt, because it felt abrupt in Congress. In 1819 Missouri, a territory of the Louisiana Purchase where enslaved people already labored, applied for statehood as a slave state. The Senate stood at eleven free states and eleven slave states, so one admission would tip the chamber where each state votes as an equal. Population was running against the South in the House, which made the Senate balance the South's central political asset and Missouri's admission a fight over the republic's future arithmetic, not over one territory's local arrangements. Into that arithmetic stepped a first term congressman from New York with an amendment.")

# 15 E CONTENT
content_text('The Tallmadge Amendment splits Congress by section',
             ['Missouri applied as a slave state in 1819.',
              'The Senate stood eleven free and eleven slave.',
              'Tallmadge would bar bringing more enslaved people in.',
              'Children born there would be freed at twenty five.',
              'The House passed it, and the Senate killed it.'],
             "Teach the amendment's gradualism precisely, because students routinely overstate it into abolition. James Tallmadge proposed two mechanisms and no more: a bar on bringing further enslaved people into Missouri, and freedom at age twenty five for children born to enslaved parents in the state after admission. Every person already enslaved in Missouri in 1819 stayed enslaved for life under his text, which Station 5 quotes entire. The design aimed at a generation's end to slavery in one new state, achieved without freeing any living person by the act itself. Then teach the vote. The House adopted the amendment, the Senate rejected it, and the division ran by section with a clarity party loyalty could not explain, in a Congress dominated by one party in the Era of Good Feelings. That division, loyalty to section shown in a roll call, is the force the vocabulary names at the end of this deck.",
             kick='E · Missouri applies', size=23)

# 16 STAT 11 TO 11
stat('11 to 11', 'free states and slave states in the Senate, 1819',
     'One admission would tip the chamber where every state counts the same',
     "Work the arithmetic of the balance until students can run it without the slide. Twenty two states meant forty four senators, twenty two from free states and twenty two from states where slavery was legal. Admit Missouri alone and the count becomes twenty four to twenty two, a working majority for the slave states in the one chamber where population does not rule. The House told the other story: northern population growth had been widening the free state majority there for a generation, and no compromise could stop the census. Read the Compromise of the next section against this slide. Pairing admissions, Maine against Missouri, protected the Senate number while surrendering the House trend, which is why southern statesmen who accepted the settlement still wrote about the future with dread. A balance that demography erodes is a settlement with a clock inside it, and Jefferson heard the clock from Monticello.",
     kick='E · Missouri applies')

# 17 F DIVIDER
divider_text('Section F', 'The Settlement of 1820',
             'Maine, Missouri, and a line at thirty six thirty.',
             "Section F gives the settlement in its three parts, and students should learn to recite the parts as a set, because the unit test reaches for the set and not for any single piece. Jesse Thomas of Illinois supplied the line, Henry Clay worked the House, and Monroe signed the central act on March 6, 1820. Maine, long a district of Massachusetts, entered as a free state. Missouri entered as a slave state, after a second argument over its constitution that this section does not hide. And the remaining Louisiana Purchase lands received a rule drawn on the map itself, at the latitude of Missouri's southern border. The reading holds the settlement's achievement and its character together: it held for a generation because it gave both sections a map they could stop arguing over. What kind of achievement a pause is, the closing section asks through Jefferson.")

# 18 F CONTENT
content_photo_s('map-port.jpg', 'Three parts, one of them an exception',
             ['Maine entered as a free state.',
              'Missouri entered as a slave state.',
              'The line ran at 36 degrees 30 minutes.',
              'North of it, slavery was forever prohibited.',
              'Missouri stood north of the line, excepted.'],
             "Take the parts in order and then return to the exception, which is where the teaching lives. Maine's admission was ready on its own merits and was used as the pairing that kept the Senate even. Missouri's admission carried an unfinished argument: its constitution barred free Black citizens from entering the state, Congress objected, Missouri's answer fudged the objection, and admission completed only in 1821. The line itself, in Section 8's words at Station 2, bars slavery in the Louisiana cession north of thirty six degrees and thirty minutes, except as punishment for crime, and protects the reclaiming of any person escaping into that free country. Then the exception: Missouri sits north of its own line and entered with slavery regardless, because the line governed territory, and the act itself carved the new state out of the ban. A rule whose text excepts its occasion is a compromise in the strictest sense, and students should say so in those words.",
             kick='F · The settlement of 1820')

# 19 STAT 36 30
stat('36°30′', 'thirty six thirty: the line across the Louisiana Purchase',
     'Slavery barred north of it, permitted south of it, Missouri excepted',
     "Give the line its full name and its full geography. Thirty six degrees thirty minutes north latitude runs along Missouri's southern border, and Thomas's amendment extended that parallel westward across the whole Louisiana Purchase, sorting country the United States already owned into future free and future slave jurisdictions with a surveyor's instrument. North of it, in the act's words, slavery was forever prohibited. South of it, Arkansas and the Indian country included, slavery stood permitted. Students should feel the abstraction as a moral fact, not only a cartographic one: the line assigned the status of people not yet born, in states not yet organized, by latitude. It also assigned the argument's future form. After 1820, every new territory arrived in Congress with a latitude attached, and the question of slavery could be debated as geography by men who preferred not to debate it as justice. Jefferson's objection, next section, begins exactly there.",
     kick='F · The settlement of 1820')

# 20 G DIVIDER
divider_photo('jefferson-port.jpg', 'Section G', 'The Fire Bell',
              ['Thomas Jefferson, by Rembrandt Peale, 1800.', 'White House Historical Association, public domain.'],
              "The portrait is Rembrandt Peale's Jefferson of 1800, the standard likeness of Jefferson in his presidential years, and the man in it had been retired at Monticello for a decade when he wrote the letter this section studies. Section G hands the lesson's judgment to a witness with standing on every side of the question. Jefferson had bought Louisiana, doubling the territory the line now crossed. He had written the nation's founding claim about human equality. He also held enslaved people at Monticello all his life, and his letter weighs justice and self preservation in opposite scales without pretending the weighing acquits him. John Holmes, the letter's recipient, was a Massachusetts congressman who had supported the compromise and would sit in the Senate for Maine, the free state the settlement created. The warning reached, in other words, one of the settlement's own makers, from the settlement's own elder.")

# 21 G CONTENT
content_text('A reprieve only, not a final sentence',
             ['A fire bell in the night filled him with terror.',
              'The knell of the Union was hushed for a moment.',
              'A line was joined to a marked principle.',
              'It was never obliterated, and it deepened with every irritation.',
              'The wolf by the ear could not be held, and could not safely be let go.'],
             "Read the letter's sentences as Station 3 prints them, in the Founders Online transcription, with Jefferson's spelling and his lowercase openings kept, because the transcription is the evidence and students should see a founder's hand unpolished. The argument moves in three steps. First, the alarm: the momentous question woke a retired man who had stopped reading newspapers, and he heard in it the Union's death bell. Second, the verdict on the settlement: hushed for the moment, a reprieve only, not a final sentence, language borrowed from a courtroom where the condemned man still waits. Third, the mechanism of doom: a geographical line coinciding with a marked principle, moral and political, once conceived will never be obliterated, and every new irritation marks it deeper. The wolf passage then admits his own paralysis, justice against self preservation, and teachers should name whose labor and freedom that paralysis cost, in plain words, before the hour ends.",
             kick='G · The fire bell', size=23)

# 22 STAT 1820
stat('1820', 'Jefferson writes the warning, seven weeks after the act',
     'April 22, 1820, to John Holmes, a maker of the settlement itself',
     "Fix the letter in time, because its date is its authority. Monroe signed the act on March 6, 1820. Jefferson wrote on April 22, with the ink of the settlement barely dry and its celebration still sounding in Washington. This is not hindsight after the line failed, decades later, when any observer could claim foresight cheaply. It is a prediction made at the moment of triumph, by the man who had acquired the territory, addressed to a man who had voted the settlement through. Predictions in history deserve the skepticism students bring to any source: Jefferson had interests, fears, and a Virginian's stake in the question, and his letter also defends diffusion of slavery as a path to emancipation, a position the class should identify and weigh rather than absorb. But the prediction's mechanism, line plus principle deepening with irritation, can be tested against every later lesson in this course, and students will meet its test again over the Mexican cession in Lesson 8.",
     kick='G · The fire bell')

# 23 GLANCE
s = slide(NAVY)
kicker(s, 'The settlements at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Four rows, two settlements', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The Doctrine', 'Declared December 2, 1823', 'Closed the hemisphere, sheltered by British sea power'),
        ('Maine and Missouri', 'Paired admissions, 1820 and 1821', 'The Senate balance held at twelve and twelve'),
        ('The line', '36 degrees 30 minutes', 'Free north, slave south, Missouri excepted'),
        ('The warning', "Jefferson's letter, April 22, 1820", 'A reprieve only; the line deepens')]
yy = 2.72
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 0.88
notes(s, "This slide mirrors the final table in the guided notes, The Settlements at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The rows compress the arc. The Doctrine row pairs the declaration with its shelter, refusing to let the claim stand without the fleet beneath it. The pairing row holds the Senate arithmetic, twelve and twelve after Maine and Missouri, with Missouri's admission completed a year after Maine's. The line row states the rule and its exception in a single breath, the habit this lesson has practiced all hour. The warning row gives Jefferson the last entry, as the lesson does, with his two judgments side by side: a reprieve only, and a line that deepens. Grade the table generously on wording and strictly on pairing: every row must show what was settled and what the settlement rested on or left open.")

# 24 SYNTHESIS
content_text('What 1820 settled, and what it scheduled',
             ['Settled were the season’s admissions and the address to Europe.',
              'Postponed was slavery in the next territory.',
              'Postponed was the Doctrine and its enforcement.',
              'The method’s price was argument by geography.',
              'The witness was the buyer of Louisiana, hearing a bell.'],
             "Draw the lesson together around the question's two halves, because the exit ticket and the writing task both return to them. The settlements were real settlements. Congress ended a crisis that had adjourned once in failure, admitted two states, and wrote a rule for an empire of land, and the president stated a foreign policy the country still names two centuries later. Students should give that record its weight before pricing it. Then price it in the records' own terms. The Compromise scheduled the slavery question for every territory outside its map, beginning with the Mexican cession of Lesson 8. The Doctrine scheduled its own enforcement for the day American power caught up with American claims. And the method itself, settling moral questions by drawing geographical lines, taught the republic a habit Jefferson warned would deepen the division it drew. Judge the season whole: decisive in form, provisional in substance, and honest about neither until Jefferson wrote his letter.",
             kick='Synthesis', size=23)

# 25 VOCAB A
vocab('Words for the hemisphere',
      [('Monroe Doctrine', 'the continents closed to Europe, in Monroe and his message of 1823'),
       ('John Quincy Adams', "Monroe's secretary of state, the Doctrine and his draftsman"),
       ('Adams-Onís Treaty', '1819: Florida ceded, a line of claims to the Pacific'),
       ('sectionalism', 'loyalty to section above nation, exposed in 1819 and 1820')],
      "These definitions match the guided notes word for word. Copy them exactly. Monroe Doctrine: the policy declared by President Monroe in his annual message of December 2, 1823, holding that the American continents were closed to future European colonization and that European interference in the hemisphere would be viewed as dangerous to the United States. John Quincy Adams: the secretary of state under Monroe, the chief author of the Monroe Doctrine's language and of the Transcontinental Treaty of 1819, who held that the United States should speak for the hemisphere itself rather than appear as a cockboat in the wake of the British man of war. Adams-Onís Treaty: the treaty of 1819, also called the Transcontinental Treaty, by which Spain ceded Florida to the United States and drew the boundary between American and Spanish claims across the continent to the Pacific. sectionalism: loyalty to one's own section of the country above the nation as a whole, the force the Missouri crisis exposed in 1819 and 1820 when the House and Senate divided on slavery's expansion in nearly perfect sectional lines.")

# 26 VOCAB B
vocab('Words for the line',
      [('Tallmadge Amendment', 'restriction proposed in 1819: passage in the House, death in the Senate'),
       ('Missouri Compromise', 'Maine free, Missouri slaveholding, the line drawn in 1820'),
       ('thirty-six thirty', 'the parallel that sorted the Louisiana lands')],
      "Three more terms, again matching the guided notes exactly, and the set of seven is complete with these. Tallmadge Amendment: the amendment proposed by Representative James Tallmadge in 1819 that would have barred bringing more enslaved people into Missouri and freed those born there at age twenty five, whose passage in the House and death in the Senate opened the Missouri crisis. Missouri Compromise: the settlement of 1820 that admitted Maine as a free state and Missouri as a slave state and drew a line at 36 degrees 30 minutes across the Louisiana Purchase lands, barring slavery north of it and permitting it south. thirty-six thirty: the parallel of latitude, 36 degrees 30 minutes north, that the Missouri Compromise drew across the Louisiana Purchase territory as the boundary between country closed to slavery and country open to it. Test the pairing students most often blur: the amendment was a failed proposal of 1819, while the compromise was the enacted settlement of 1820 that answered the crisis the amendment opened.")

# 27 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['What did the settlements of 1820 settle, and what did they only postpone? Argue it from the records, with dates, balances, and the line.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Settlements File: the Doctrine, Section 8, Jefferson and his letter, Adams and his argument, and the Tallmadge Amendment, with a verdict on firmer ground'),
        ('Notebook', 'Notebook page: the settlements charted by proposal, settlement, and postponement'),
        ('Quick check', 'A Hemisphere Declared, A Line Drawn: Section 8 read closely, and both settlements in sequence'),
        ('Writing', 'Settled, or Only Postponed: one settlement followed through its decision and its opening')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the Doctrine in one sentence, the Compromise and its three parts, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Settlements File, runs five stations: the Monroe Doctrine in the Avalon Project text carried in the bank record, Section 8 of the Missouri act in the National Archives transcript, Jefferson's letter to John Holmes in the Founders Online transcription, Adams's cabinet argument as a labeled teaching summary, and the Tallmadge Amendment in the National Register transcription of 1819, ending in a verdict on which settlement rested on firmer ground. The notebook page charts the settlements by proposal, settlement, and postponement. The quick check tests Section 8 read in its own words and both settlements in sequence, tagged to blueprint entries 13 and 14. The writing task requires one settlement followed through both its decision and its opening. The exit ticket has three parts: the Doctrine defined in one sentence, the Compromise's three parts with its exception, and the lesson question in two or three sentences using one fact from each settlement.")

dc.save(OUT)
