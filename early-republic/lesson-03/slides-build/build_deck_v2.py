#!/usr/bin/env python3
"""Early Republic Lesson 3 deck builder. V2 (2026-10-24 rollout,
improved slide standard): content bullets are short complete sentences;
speaker notes applied after the build from the teacher notes guide
(apply_guide_notes.py). Same 25 slides, same order. Image led deck:
Decatur boarding a Tripolitan gunboat as the title, the Peale Jefferson,
the Inman Marshall, and the Carter Decatur painting for the Barbary divider."""
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
OUT = os.path.join(LESSON_DIR, 'lesson-03-slides-v2.pptx')

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
 'strict construction': 'the reading that holds the federal government to the powers the Constitution names and those necessarily implied',
 'implied powers': 'powers beyond the listed ones, drawn from the clause for laws necessary and proper to carry the listed powers out',
 'Louisiana Purchase': 'the 1803 treaty buying France\u2019s claim to Louisiana for fifteen million dollars, doubling the nation\u2019s territory',
 'midnight judges': 'the judges Adams appointed in his presidency\u2019s last days, whose undelivered commissions produced Marbury\u2019s suit',
 'Marbury v. Madison': 'the 1803 decision holding the Court could not order a commission delivered because the law granting that power was unconstitutional',
 'judicial review': 'the courts\u2019 power to declare laws and acts of the other branches unconstitutional and void, claimed in Marbury',
 'Barbary Wars': 'the wars of 1801 to 1805 and 1815 against the Barbary states rather than keep paying tribute for merchant ships\u2019 safety',
}

# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'THE EARLY REPUBLIC AND EXPANSION \u00b7 LESSON 3', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Jefferson\u2019s Republic and the Louisiana Purchase', size=30, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'A president elected to shrink the government signs the treaty that doubles it.', size=17, color=POWDER)
notes(s, "Open on the contradiction in the lesson question, because everything in this lesson hangs on it. Thomas Jefferson won the election of 1800 promising to unwind the Federalist government: fewer taxes, a smaller army and navy, a debt paid down, and a Constitution read strictly, power by power. Within three years that president had bought Louisiana from France for fifteen million dollars and doubled the territory of the United States, and he had written in a private letter that the Constitution had made no provision for what he had just done. The image is Stephen Decatur boarding a Tripolitan gunboat in 1804, from the other test of the same years, the Barbary War. This lesson follows Jefferson through the unwinding, the court case he could not unwind, the Mediterranean war, the offer from Napoleon, the scruple he recorded himself, and the territory his government then had to rule.")
# 2 QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did a president elected to shrink the government double the nation\u2019s size?', {})]], size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': RUST_LT, 'italic': True}), ('How did the United States turn its Constitution into a working government, and what did continental expansion do to the republic that government served?', {'italic': True})]], size=17, color=POWDER, font='Georgia', leading=1.2)
notes(s, "Read the lesson question aloud and name its two terms, because the exit ticket and the writing task grade them together. The first term is the program: Jefferson really was elected to shrink the government, and section A will show him doing it, tax by tax and ship by ship. The second term is the fact: the Louisiana Purchase of 1803 doubled the nation's territory in a single treaty, the largest single act of expansion in the presidency to that date and for long after. Students often reach for an easy answer, that Jefferson was simply a hypocrite, and the lesson is built to make that answer too small. His own letter to John Breckinridge records the conflict in his own words, and the documents let students judge a president who saw the problem clearly, wrote it down, and signed anyway. Keep the unit question in view: a working government is exactly what the purchase tested.")
# 3 MAP
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'The shrinking president and the doubling treaty', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'A President Elected to Shrink the Government', 'Taxes repealed, forces cut, the debt attacked'),
        ('B', 'The Judges He Could Not Unwind', 'Midnight judges, and one undelivered commission'),
        ('C', 'Marbury v. Madison', 'The Court surrenders the case and claims review'),
        ('D', 'The Mediterranean Test', 'Tribute refused, a frigate burned in Tripoli harbor'),
        ('E', 'The Offer No Ideology Survived', 'Napoleon offers the whole of Louisiana'),
        ('F', 'The Scruple, Stated Honestly', 'An act beyond the Constitution, in Jefferson\u2019s words'),
        ('G', 'The Transfer and the First Governings', 'Fifty thousand people under an appointed government')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This map follows the guided notes section by section, and students should keep it in front of them. Section A sets the standard: Jefferson's unwinding program and the strict construction it rested on. Section B introduces the inheritance he could not repeal, the Federalist judges appointed in Adams's last days. Section C reads the Supreme Court's answer in Marbury v. Madison, decided in February 1803, weeks before the Louisiana treaty was signed. Section D takes the same president overseas, where he refused tribute to Tripoli and fought a war with the small navy he was cutting. Sections E and F hold the lesson's center together: Napoleon's offer of the whole of Louisiana, and Jefferson's own recorded objection that the Constitution had made no provision for holding foreign territory. Section G follows the flag to New Orleans and asks what governing the purchase meant for the people already living under it. One question runs through every section: what did power do to the principles?")
# 4 DIVIDER A
divider_text('Section A', 'A President Elected to Shrink the Government', 'March 1801: a program of repeal, pardon, and payment, resting on a strict reading of the Constitution.',
 "Teach the program as a program, a set of acts that belong together and rest on one idea. Jefferson did not drift into smaller government. He had argued for a decade that the Federalist government of the 1790s had grown past the Constitution: a bank the document never named, a sedition law that jailed editors, an excise that fell on frontier farmers, and debts funded so that speculators and creditors would bind themselves to the new government. His election, which he called a revolution in the principles of government, was a mandate to reverse that growth by the same instruments that had built it, statute, budget, and appointment. The reading's first section lists the reversals one by one, and students should notice how concrete they are. Nothing here is a mood. Each item repeals, pardons, restores, cuts, or pays something specific, and each one can be checked against the record of the government that came before.")
# 5 CONTENT A
content_text('The unwinding, item by item', ['The Sedition Act was left to expire, and its prisoners were pardoned.', 'The citizenship wait was restored from fourteen years to five.', 'The whiskey excise was repealed.', 'The army and the navy were cut.', 'Gallatin paid down the debt on customs and land sales.'],
 "Work the list slowly, because the lesson's later sections measure Jefferson against it. The Sedition Act expired by its own terms on March 3, 1801, and Jefferson pardoned the men still serving sentences under it, carrying his inaugural promise, that error of opinion may be tolerated where reason is left free to combat it, into administration. Congress restored the naturalization wait from fourteen years to five, undoing the Alien Acts' longest barrier. The excise tax on whiskey, the tax that had produced the Whiskey Rebellion of the last unit, was repealed outright. The army and navy were cut. And Albert Gallatin at the Treasury ran the government on customs duties and land sales while retiring the national debt on a schedule, treating the debt itself as a moral burden on a republic. Underneath every item sits strict construction: the federal government holds the powers the Constitution names, and no others it cannot trace to them.")
# 6 DIVIDER B
divider_photo('marshall-port.jpg', 'Section B', 'The Judges He Could Not Unwind', ['Life tenure outlasted the election. One signed commission sat undelivered in a drawer.'],
 "The portrait is Chief Justice John Marshall, painted by Henry Inman in 1832, nearly three decades after the case this lesson reads, and held by the Library of Virginia. Set the inheritance plainly. The Federalists lost the election of 1800 and kept the judiciary. In its last weeks their Congress passed the Judiciary Act of 1801 creating new judgeships, and President Adams filled them to his final night in office, appointments remembered as the midnight judges. Federal judges hold office for life, so no repeal and no election could remove them. Among the commissions signed and sealed in those last hours, one, William Marbury's appointment as a justice of the peace, was never delivered. It sat in the secretary of state's office when Jefferson took power, and Jefferson's secretary, James Madison, refused to deliver it. Marbury sued in the Supreme Court and asked the justices to order Madison to hand it over.")
# 7 CONTENT B
content_text('A commission in a drawer', ['The Judiciary Act of 1801 created new judgeships.', 'Adams filled them to his final night in office.', 'The midnight judges held their places for life.', 'Marbury\u2019s commission sat signed, sealed, and undelivered.', 'Madison refused delivery, and Marbury sued.'],
 "Slow down on the smallness of the object, because the largest doctrine in American law grew out of a justice of the peace commission for the District of Columbia, a minor office with a five year term. What Marbury wanted was delivery of a piece of paper that would complete an appointment the last Federalist president had made. What Jefferson wanted was just as plain: not one more Federalist officeholder seated by his administration's hand. Teach the legal posture exactly. Marbury went directly to the Supreme Court under a section of the Judiciary Act of 1789 that said the Court could issue orders of this kind, and he asked for a writ of mandamus ordering Madison to deliver the commission. Then introduce the man who would decide it. John Marshall, the chief justice, had been John Adams's secretary of state. His own office had failed to deliver the commission. He was now to judge the refusal, as a Federalist holding office for life, against a Republican president who controlled the executive branch and its officers.")
# 8 DIVIDER C
divider_text('Section C', 'Marbury v. Madison: The Maneuver and the Doctrine', 'February 1803: the Court gives Jefferson the case and takes the Constitution.',
 "Frame this section as a trap with three exits, two of them ruinous. Marshall's Court was the weakest of the three branches in 1803: it had no army, no budget of its own, and a recent memory of Federalist judges enforcing the Sedition Act, which had made the judiciary itself a party question. If the Court ordered Madison to deliver Marbury's commission, Jefferson could simply refuse, and a Supreme Court order publicly defied and unenforced would advertise the Court's weakness to the whole republic. If the Court declined the case and sent Marbury away without a word about his rights, it would confirm that the judiciary bends whenever the executive pushes. Students should hold both dangers in mind before the next slide states what Marshall did instead, because the opinion only looks inevitable afterward. In February 1803, with the Louisiana negotiation running in Paris at the same moment, it was a gamble taken by a judge who could not know how it would be received.")
# 9 CONTENT C
content_text('Surrender the case, claim the power', ['The Court held that Marbury deserved his commission.', 'The Judiciary Act section behind the suit granted too much.', 'That section was unconstitutional, and therefore void.', 'No order could issue, and the commission stayed undelivered.', 'In the same opinion, the Court claimed the power to say what the law is.'],
 "Teach the opinion in its own order, because the order is the maneuver. First, Marshall held that Marbury had a legal right to his commission: the appointment was complete when Adams signed it, and Madison's refusal to deliver it violated a vested legal right. Jefferson's administration is told, in print, that it broke the law. Second, Marshall held that the laws of the United States would ordinarily give Marbury a remedy. Third, and here the opinion turns, he held that the section of the Judiciary Act of 1789 under which Marbury had sued in the Supreme Court granted the Court an original jurisdiction the Constitution does not give it. That section therefore conflicted with the Constitution and was void, and the Court could not issue the order. The commission stayed in the drawer. Jefferson won everything he could touch, and the instrument of his victory was the Court striking down an act of Congress for the first time.")
# 10 CONTENT C2
content_text('A government of laws, and not of men', ['It is the province and duty of the courts to say what the law is.', 'A law repugnant to the Constitution is void.', 'Courts, like other departments, are bound by the instrument.', 'Judicial review was claimed while ruling for the president.'],
 "Read the opinion's own sentences aloud from the activity text before summarizing them. Marshall writes that the government of the United States has been emphatically termed a government of laws, and not of men, and that it would cease to deserve the name if the laws furnished no remedy for a violated right. He writes that it is emphatically the province and duty of the judicial department to say what the law is, and that when a statute and the Constitution conflict in a case, the court must follow the Constitution, because a law repugnant to the Constitution is void. That is judicial review, stated as a duty so plain it barely needed arguing. Then make the political point students must carry out of the section. Jefferson could not attack the ruling without demanding delivery of a Federalist commission. The Court had enlarged its own power permanently by deciding the one case in front of it against the party that had appointed its chief justice.")
# 11 DIVIDER D
divider_photo('decatur-port.jpg', 'Section D', 'The Mediterranean Test', ['Tribute or frigates: Jefferson refused the payment and sent the navy he was cutting.'],
 "The image is Stephen Decatur boarding a Tripolitan gunboat during the bombardment of Tripoli in August 1804, a painting by Dennis Malone Carter held by the Naval History and Heritage Command. Set the system Jefferson inherited. For centuries the Barbary states of North Africa, Morocco, Algiers, Tunis, and Tripoli, had taken tribute from trading nations in exchange for leaving their merchant ships alone, and the young United States, with no navy worth the name, had paid like everyone else. Payments and ransoms were a standing charge on the Treasury Jefferson was trying to empty of debt. In 1801 the ruler of Tripoli demanded an increased payment. Jefferson refused to pay more, and Tripoli declared war. The president who was cutting the navy now had to use it, in a war three thousand miles from home, against an enemy whose whole revenue system depended on the payments he had stopped.")
# 12 CONTENT D
content_text('The Philadelphia, and the raid that burned it', ['Tripoli declared war in 1801 over refused tribute.', 'A small navy was sent to blockade and bombard.', 'In 1803 the frigate Philadelphia was captured in Tripoli harbor.', 'In February 1804 Decatur boarded her by night and burned her.', 'In 1805 the war closed, and tribute to Tripoli ended.'],
 "Teach the episode with its limits attached, because this record is a labeled teaching summary in the activity and the lesson models honest labeling. The frigate Philadelphia, chasing a Tripolitan vessel in October 1803, ran aground outside Tripoli harbor and was captured with more than three hundred officers and men, who spent the rest of the war as prisoners. On the night of February 16, 1804, Lieutenant Stephen Decatur took a captured local vessel into the harbor with a volunteer party, boarded the Philadelphia where she lay under the harbor guns, and burned her so completely that Tripoli gained nothing from its prize. Commodore Preble bombarded Tripoli that summer, and in 1805 Tripoli signed a treaty ending the war and ending tribute. The same settlement paid sixty thousand dollars for the prisoners' release, a ransom in all but name, and the United States kept paying other Barbary rulers until 1815. The republic defended its commerce with frigates instead of bribes, and paid one last bill on the way out.")
# 13 DIVIDER E
divider_text('Section E', 'The Offer No Ideology Survived', 'Paris, spring 1803: the envoys asked for a city. Napoleon offered a continent.',
 "Set Napoleon's position before Jefferson's, because the offer is unintelligible without it. France had taken Louisiana back from Spain in 1800 and meant to rebuild an American empire on it, fed by the sugar colony of Saint-Domingue in the Caribbean. That foundation collapsed. The enslaved people of Saint-Domingue had risen in 1791 and defeated every army sent against them, including the French expedition of 1802 and 1803, which disease and resistance destroyed; the colony would declare itself the independent republic of Haiti on January 1, 1804. At the same moment Napoleon's wars in Europe were resuming, and Britain's navy stood between France and any American colony France might try to hold. Louisiana, indefensible and unfed, had become a liability that could at least be sold, and sold to the one buyer whose gain would injure Britain. Jefferson's envoys, Robert Livingston and James Monroe, had instructions to buy New Orleans and the Floridas for up to ten million dollars. The French minister offered them the whole of Louisiana instead.")
# 14 CONTENT E
content_text('Asked for New Orleans, offered Louisiana', ['The envoys\u2019 errand was New Orleans and the Mississippi outlet.', 'Saint-Domingue was lost, and war with Britain was resuming.', 'Napoleon offered France\u2019s whole claim west of the Mississippi.', 'The treaty was signed in April 1803.', 'The Senate ratified it in October 1803.'],
 "Work the negotiation as the envoys lived it, in days rather than months. Livingston had been pressing the French for New Orleans for a year and getting nowhere when, in April 1803, the French finance minister asked what the United States would give for the whole of Louisiana. Monroe arrived in Paris that same week. Neither envoy had instructions for a continent, communications with Washington took months, and the offer carried an obvious expiry date: Napoleon could change his mind, or lose Louisiana to Britain without payment, at any time. They agreed to buy the whole territory and settled the price with the claims settlements at fifteen million dollars. Then bring the fact home to the lesson question. Jefferson had asked Congress and his envoys for a port. His envoys, acting past their instructions as his letter would soon say his whole government had acted past the Constitution, brought home an empire: France's claim to the country from the Mississippi to the Rockies, doubling the nation's territory in a single signature.")
# 15 STAT E
stat('$15 million', 'the price of Louisiana in the treaty of 1803', 'About three cents an acre by the usual estimate, for a claim whose western boundary nobody in Washington could draw',
 "Stop on this figure and give it its parts, because students repeat the price without knowing what it bought. The treaty and its companion conventions settled the price at fifteen million dollars in total: sixty million francs for the territory itself, roughly eleven and a quarter million dollars, plus the United States assuming its own citizens' claims against France up to a further sum that brought the whole to fifteen million. The territory was an estimated 828,000 square miles, stated here as an estimate, since its western and northern boundaries were claims on paper rather than surveyed lines. Three cents an acre is the figure Americans usually quote, and it is fair arithmetic on those estimates. Then ask the question the price raises for this lesson. Gallatin's Treasury was paying down the national debt on principle. The purchase was financed by new bonds, new debt issued by the debt paying administration, sold through London and Amsterdam bankers. The doubling was bought on credit by the president elected to free the republic from debt.")
# 16 DIVIDER F
divider_text('Section F', 'The Scruple, Stated Honestly', 'Monticello, August 12, 1803: the president records his own objection, in his own hand.',
 "Introduce the document at the center of this lesson's judgment, Jefferson's letter to Attorney General John Breckinridge of August 12, 1803, quoted at Station 3 of the activity from the Founders Online transcription. Jefferson wrote it while the treaty awaited the Senate, thinking aloud to a cabinet officer about what the government had done and what should happen next. Most presidents' constitutional doubts are reconstructed by historians from silences. Jefferson's survives in sentences, and students should register how unusual the record is before they use it. He does not minimize. The Constitution, he writes, has made no provision for our holding foreign territory, still less for incorporating foreign nations into our union, and the executive has done an act beyond the Constitution. The section's work is to read that confession slowly, to follow the repair he proposed, and to watch the repair being set aside as the government chose speed over authorization.")
# 17 CONTENT F
content_text('An act beyond the Constitution', ['The Constitution made no provision for holding foreign territory, Jefferson wrote.', 'Still less for incorporating foreign nations into the Union.', 'A draft amendment was prepared to authorize it.', 'The amendment was abandoned: delay risked the treaty.', 'The parties traded constructions, the Federalists turning strict as Jefferson signed.'],
 "Work the sequence as Jefferson lived it, because each step is documented. He first considered the honest repair under his own theory: draft a constitutional amendment authorizing the acquisition and the incorporation of its people, and submit the purchase to the nation for approval after the fact. His letter to Breckinridge imagines exactly that appeal, Congress ratifying and paying, then asking the nation for an additional article approving an act it had not previously authorised. Then the repair was abandoned. An amendment process would take months, Napoleon might withdraw, and advisers, including voices in the Senate, pressed for ratification first. The Senate ratified in October 1803, and no amendment was ever adopted. Complete the picture with the reversal students find most surprising. The Federalists, Hamilton's party of broad construction and implied powers, now discovered strict construction and warned that the purchase exceeded the Constitution. Jefferson, who had built his career on strictness, took the broad reading when the land was in front of him. Neither party's doctrine survived contact with the offer.")
# 18 DIVIDER G
divider_text('Section G', 'The Transfer and the First Governings', 'New Orleans, December 1803: the flag rises over people who were never asked.',
 "Close the narrative where the paper becomes a government. In December 1803, at New Orleans, the French flag came down and the American flag rose, France having held the colony for twenty days after taking it back from Spain, long enough to hand it over. The territory the United States now possessed held about fifty thousand people in its settled districts, stated here as the standard estimate: French and Spanish colonists, free people of color, and enslaved Africans and African Americans forming a large share of lower Louisiana's population, living under French and Spanish law, much of it in French and Spanish languages. Article III of the treaty promised these inhabitants incorporation into the Union and admission to the rights of citizens as soon as possible under the Constitution. What they received first was a territorial government appointed from Washington, a governor and council named by the president, ruling people who had elected none of them and who petitioned Congress for the rights the treaty had promised.")
# 19 CONTENT G
content_text('An empire of liberty, governed by appointment', ['Possession was taken at New Orleans in December 1803.', 'The territory held about fifty thousand inhabitants, many of them enslaved.', 'The treaty promised incorporation and citizens\u2019 rights.', 'The first reality was a governor and council appointed from Washington.', 'The inhabitants petitioned for what the treaty promised.'],
 "Hold the promise and the practice side by side, because the gap between them is this section's content. Jefferson believed the purchase served liberty: he called Louisiana ground for an empire of liberty, room enough for republics to multiply westward as states equal to the original thirteen, rather than colonies held in subjection on the European model. The treaty's third article writes that intention into law. But the Constitution's territory arrangements and the politics of 1804 delivered something else first: rule by appointment, laws in a language many inhabitants did not read, and for the enslaved majority of some districts, a change of flags that changed nothing about their condition except the government that upheld it. The petitions from Louisiana's inhabitants asking for elected government and the treaty's promised rights are the record's own verdict on the meantime. Students should end the lesson able to state the question the purchase opened rather than closed: whether a republic could acquire peoples by treaty and govern them as subjects while calling the result an empire of liberty.")
# 20 STAT G
stat('50,000', 'inhabitants of the ceded territory, about', 'The standard estimate for the settled districts in 1803, many of them enslaved, all of them promised citizens\u2019 rights by Article III',
 "Give this figure its label before its weight: about fifty thousand inhabitants, the standard estimate historians work from for the settled population of Louisiana in 1803, concentrated along the Mississippi and the Gulf settlements, with the vast interior inhabited by Native nations whom the treaty's arithmetic did not count at all. That omission belongs in the teaching. France sold, and the United States bought, a claim: the paper sovereignty of a country whose actual peoples, the Native nations of the plains and the river valleys, had signed nothing and been consulted by nobody. Within the counted fifty thousand, enslaved people made up a large share, in lower Louisiana approaching half the population. Article III promised the inhabitants incorporation and the rights of citizens as soon as possible. For the enslaved, the promise's language about liberty, property, and religion protected the property rights of the people who held them. Keep both facts in the same sentence whenever this number is used.")
# 21 GLANCE
s = slide(NAVY)
kicker(s, 'The lesson at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Program, case, war, purchase, scruple', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The program', 'Repeal, pardon, restore, cut, pay down', 'Strict construction governing at home'),
        ('The case', 'Marbury decided, February 1803', 'The Court claims review, Jefferson keeps the refusal'),
        ('The war', 'Tripoli, 1801 to 1805', 'Tribute refused, a frigate burned, one ransom paid'),
        ('The purchase', 'Treaty of April 1803, fifteen million dollars', 'The territory roughly doubled in one signature'),
        ('The scruple', 'The Breckinridge letter, August 1803', 'An act beyond the Constitution, the cure abandoned')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 0.86
notes(s, "This slide mirrors the closing table of the guided notes, The Lesson at a Glance, and students should complete that table now from memory where they can. Check it with the question that exposes shallow answers: which rows describe Jefferson choosing, and which describe Jefferson being overtaken? The program row is pure choice, the unwinding he campaigned on. The case and war rows are mixed: he chose the refusal of the commission and the refusal of tribute, and other men's decisions, Marshall's opinion and Tripoli's declaration, set the terms on which those choices played out. The purchase row is an offer arriving from outside, from Napoleon's necessities, that no American program had planned. And the scruple row is Jefferson judging himself after the fact, in writing. The table is the lesson in miniature: a president whose principles were clearest at home, tested hardest abroad, and recorded most honestly in a private letter.")
# 22 VOCAB A
vocab('Words for the two readings of the Constitution', [(t, SHORT[t]) for t in ['strict construction', 'implied powers', 'Louisiana Purchase', 'midnight judges']],
 "Four terms, word for word as the guided notes print them, and the writing task cannot be done well without the first two held apart. " + "strict construction: " + TD['strict construction'] + ". " + "implied powers: " + TD['implied powers'] + ". " + "Louisiana Purchase: " + TD['Louisiana Purchase'] + ". " + "midnight judges: " + TD['midnight judges'] + ".")
# 23 VOCAB B
vocab('Words for the Court and the Mediterranean', [(t, SHORT[t]) for t in ['Marbury v. Madison', 'judicial review', 'Barbary Wars']],
 "Three more terms, again matching the guided notes exactly, and students should copy the definitions because the unit test draws on them. " + "Marbury v. Madison: " + TD['Marbury v. Madison'] + ". " + "judicial review: " + TD['judicial review'] + ". " + "Barbary Wars: " + TD['Barbary Wars'] + ". Press the connection between the first two terms before the exit ticket. The case is remembered because of the power: a single undelivered commission became the occasion on which the Court claimed the authority to void acts of Congress, and it has held that authority ever since.")
# 24 SYNTHESIS
content_text('Answering the question', ['At home, the government shrank, on strict construction.', 'In court, Jefferson\u2019s refusal stood, and the Court grew.', 'Abroad, tribute was refused, and a continent was accepted.', 'The scruple was confessed on the record, and the amendment abandoned.'],
 "Run the synthesis as the writing task rehearsal, and build it from the class's own answers before summarizing. Jefferson doubled the nation's size by accepting, in April 1803, an offer his principles had no article for: Napoleon, stripped of Saint-Domingue and facing British sea power, sold the whole of Louisiana when American envoys had asked only for New Orleans. The same president shrank the government at home on schedule, repealing the excise, cutting the forces, paying the debt, and letting the Sedition Act die. The two records are not a contradiction to be explained away but a hierarchy to be judged: when security of the Mississippi and land for republics stood on one side and a construction rule on the other, Jefferson chose, confessed the choice in the Breckinridge letter, and let the cure lapse. Test the synthesis against Marbury before closing: in the same season the Court read its own powers broadly too, and Jefferson, who benefited, let that stand as well.")
# 25 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4, ['How did a president elected to shrink the government double the nation\u2019s size?'], size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Purchase File: five records, what each shows Jefferson doing with power, then a verdict'),
        ('Notebook', 'Notebook page: the lesson as a chart, episode by episode, power by power'),
        ('Quick check', 'The Purchase and the Court: Marbury and the Breckinridge letter, read side by side'),
        ('Writing', 'Against His Principles, or For Them: the verdict in one essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: judicial review defined with its case, Jefferson\u2019s objection in his own words, and the lesson question in two or three sentences.', size=15, color=POWDER)
notes(s, "Close by handing the lesson to the work. In the activity, The Purchase File, each group works five records, the Louisiana Purchase Treaty, Marbury v. Madison, Jefferson's letter to Breckinridge, the Barbary War teaching summary, and the First Inaugural Address, states what each one shows Jefferson doing with power, and judges whether the purchase was Jefferson acting against his principles or discovering what his principles were for. The notebook page rebuilds the lesson as a chart of episode, power, and what each episode settled or left open. The quick check sets Marshall's opinion and Jefferson's letter side by side and tests whether students can hold both expansions of 1803 at once. The writing task, Against His Principles, or For Them, requires the verdict in essay form, argued from the inaugural standard and the Breckinridge confession. The exit ticket has three parts, and students should leave with all three ready.")

dc.save(OUT)
