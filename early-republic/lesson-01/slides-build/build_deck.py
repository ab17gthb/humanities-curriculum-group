#!/usr/bin/env python3
"""Early Republic Lesson 1 deck, "Washington's Republic: Hamilton, Parties, and the Farewell,"
built to the approved system: image-led slides, fragments only on screen,
comprehensive speaker notes, full lesson + vocabulary coverage.
Fonts: Georgia titles, Lato body."""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags, photo_right,
                         divider_photo, content_photo, content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED, W, H)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

dc.IMG = os.path.join(HERE, 'img')
OUT = os.path.join(HERE, '..', 'lesson-01-slides.pptx')
N = {
1: "The image is Frederick Kemmelmeyer's painting of Washington reviewing the western army at Fort Cumberland, Maryland, painted after 1795 and held by the Metropolitan Museum of Art. Hold it in front of students before any content and ask why a president is drawn reviewing an army raised inside his own country. The answer is the lesson. Between 1789 and 1796 Washington's administration had to invent the machinery of a government the Constitution had only outlined, fund it through Alexander Hamilton's financial program, enforce its tax law against armed resistance in Pennsylvania, hold the country out of a European war, and then leave office by choice, warning as it left against parties and permanent foreign alliances. Every section of the guided notes follows those tasks in order.",
2: "The question has two halves and students should hear both before the lesson begins. The first half is about invention. The Constitution named offices and listed powers, but it did not build a cabinet, courts at work, a funded debt, or a way to enforce a tax. Washington's administration built that machinery while governing, and every first act became a precedent. The second half is about warning. In the Farewell Address of September 1796 Washington warned against the spirit of party he had watched form inside his own cabinet and against permanent alliances with foreign nations. Teach the tension between the halves early: the program that made the government real also created the parties the address warned against, and students will judge that tension in the writing task.",
3: "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A gives the invention problem of 1789, a cabinet and courts built where the Constitution had drawn only an outline. Section B gives Hamilton's program in four parts, funding, assumption, the Bank, and the excise. Section C gives the strict reading answer and the first parties. Section D follows the excise to western Pennsylvania and the army Washington sent. Section E pauses on the cotton gin and the expansion of slavery it powered. Section F takes up neutrality and the two treaties. Section G closes with the Farewell Address and its two warnings.",
4: 'Begin where the Founding unit closed. The Constitution was ratified, the Bill of Rights would follow in 1791, and yet in April 1789 there was no working government to point at. There was no cabinet room, no federal courtroom in session, no treasury collecting a revenue, no agreed form for receiving an ambassador or touring a state. Teach students to feel the blankness of the start. Washington was the most trusted man in the country, and his administration used that trust to give every new practice the weight of his example. A precedent set by Washington was hard for a later president to argue against, which is why this lesson treats invention itself as a form of power. The machine his administration built is the subject of the next slide.',
5: 'Work the fragments as machinery, because machinery is the right word for what 1789 produced. Congress created three executive departments in a single summer, State, Treasury, and War, and their heads became the advisers Washington gathered as his cabinet, a body the Constitution nowhere creates. The Judiciary Act of the same year organized a Supreme Court of six justices and a ladder of lower federal courts, so federal law could be heard in a federal room rather than borrowed state courts. Washington was received as head of state, met foreign ministers, and signed and vetoed bills as the Constitution directed. None of this was automatic. Each act answered a question the document had left open, and the answers hardened into the practices later presidents inherited. Students should copy the fragment list into their notes beside section A.',
6: 'Pause on the date, because holding a year in mind is how this lesson stays organized. In 1789 the new government did not merely begin; it was assembled. The same Congress that wrote the Bill of Rights also created the departments and the courts, in the same months Washington was learning how to be a president when no president had existed before. Teach the number as a count of firsts: first cabinet, first federal courts, first revenue laws, first presidential tour. Then make the limit plain. The machinery of 1789 was small, a few hundred officials in a capital that moved from New York to Philadelphia, governing a country of some four million people. Its importance was never its size. It was that the practices set in that year were still being followed when the country had grown a hundred times larger.',
7: "The portrait is John Trumbull's Alexander Hamilton, painted in 1806 after Hamilton's death from an earlier likeness, showing the first Secretary of the Treasury as a civilian statesman among his papers. Section B gives the financial design Hamilton laid before Congress in a series of reports. Teach it as one design, not four separate bills, because Hamilton built it as one design and the opposition answered it as one design. A government that cannot pay its debts cannot borrow in an emergency, cannot pay an army, and cannot ask its citizens to treat its promises as money. The four parts on the next slide are the four legs of a single table: credit, union, a bank, and a revenue. Remove any leg and Hamilton's table falls, which is exactly the counterargument the opposition tried in reverse.",
8: "Teach the four parts in Hamilton's order, because the order is the argument. Funding at full value comes first: the union pays its Revolutionary War debt whole, including certificates that had changed hands for pennies, so that anyone lending to the United States in the future trusts its word. Assumption comes second: the federal government takes over the states' war debts, so creditors who once looked to thirteen treasuries now look to one union. The Bank comes third, an institution to hold the funds and issue a currency the whole country accepts. The excise comes fourth, a revenue of the government's own, laid on distilled whiskey. Ask students which part a lender, a state creditor, a merchant, and a frontier farmer would each notice first. The four answers together are the program.",
9: "The number is the Bank's first charter, twenty years, granted in 1791 and running to 1811. Teach the charter length as a fact with an argument inside it. Hamilton wanted a bank long lived enough for merchants and lenders to build their business on its notes, so its paper would circulate as a uniform currency from New Hampshire to Georgia. Opponents heard the same twenty years as a monopoly granted for a generation, a corporation with public power that no election could touch. Both readings were available in 1791, and the fight over renewing the charter in 1811, and again under Jackson, shows the question never closed. Students should note the deeper point for their essays: the Bank was the one part of the program a citizen could walk into, hold in paper, and use at a counter.",
10: "Section C follows the argument out of the cabinet room. Jefferson and Madison did not merely dislike Hamilton's measures; they held a different reading of the Constitution, and the difference is the content of this section. Under a strict reading, the federal government holds the powers the document names and little more, so a bank the document never named stood outside the grant. Under Hamilton's broad reading, powers could be implied from the listed ends. Teach students that both readings claimed the Constitution itself as their ground, which is why the argument could not be settled by pointing at the text. It was settled, for a time, by organizing: newspapers, committees, and voting blocs gathered behind each reading until the readings had become parties with names.",
11: "Name the parties plainly and date their forming to the argument itself, not to a founding convention nobody held. Federalists gathered around Hamilton's program: a funded debt, a national bank, commerce with Britain, and a government energetic enough to use implied powers. Democratic-Republicans gathered around Jefferson and Madison: strict construction, suspicion of corporations and standing financial interests, sympathy for France, and a fear that Hamilton's design rebuilt the British system Americans had just fought. Washington deplored both camps and said so, yet he signed Hamilton's measures and kept Hamilton in office, and the country read his administration as Federalist in practice. Students often ask when parties were invented. The honest answer this lesson gives is that they were not invented at all. They accumulated out of one argument that would not end.",
12: "The painting on the next slides shows Washington reviewing the western army at Fort Cumberland before the march into Pennsylvania. Section D is the lesson's enforcement story, and it begins far from any army, in a farm economy where corn rotted before it could cross the mountains. Whiskey was the frontier's cash crop in liquid form, and the excise of 1791 taxed the one product a western farm could sell. Teach the farmers' case in its own terms first: a distant legislature, in which the West was thinly represented, had taxed them to fund a debt held largely in the East, and many said the parallel with 1765 was exact. Only after that case is standing should the government's case enter: a law obeyed only where it is popular is not a law, and the union of 1789 had been built to replace a confederation that could not enforce anything.",
13: 'Work the sequence from tax book to army camp. Through 1791 and 1793 most western counties paid late, evaded, or intimidated collectors one farm at a time. In the summer of 1794 the resistance turned open in western Pennsylvania: collectors tarred and feathered, the mail robbed, the home of a federal marshal attacked, and armed men gathered in thousands. Washington first sent commissioners and required submission by a deadline, and only when the deadline failed did he call the militia. That order of moves is part of the precedent: negotiation attempted, law stated, force raised as a stated last step. The army that followed, some thirteen thousand men from four states, was larger than most armies Washington had commanded in the Revolution, and it was raised to collect a tax. Students should sit with that proportion.',
14: 'Let the figure carry the section. Thirteen thousand is the standard rounded count of the militia Washington called from Pennsylvania, Virginia, Maryland, and New Jersey in the fall of 1794, and he rode west with the army as far as Bedford, Pennsylvania, the only time a sitting president has led troops toward a field of operations. The size was the message. The government did not send a posse to arrest a few distillers; it sent an army no county could mistake for a bluff, and the rebellion dissolved without a battle as the columns approached. Two men were convicted of treason and Washington pardoned both, pairing the largest show of force of the decade with a deliberate act of mercy. Force proved the law could be enforced; the pardons showed enforcement was a choice, not an appetite.',
15: "The image is Eli Whitney's patent drawing for the cotton gin, filed March 14, 1794, shown here from the restored copy the Patent Office made in 1845 after the original burned. Section E is short in the reading and large in the unit, and teachers should say why. The gin sits inside a lesson about building a government because the machine changed the country that government had to govern. Short staple cotton grew across the inland South, far from the coast, but its seeds clung to the fiber and hand cleaning was slow. A machine that multiplied the cleaning multiplied the value of the land, and of the enslaved labor that planted and picked the crop. The next slide works the mechanism first and the consequence second, in that order, so students meet the consequence as a fact about a machine and not as a slogan.",
16: "Teach the mechanism from the drawing before the consequence, as the activity Station 4 requires. Wire teeth on a turning cylinder catch the cotton fiber and drag it through the narrow slots of the breastwork. The seeds, too large for the slots, are held back and fall away. A brush wheel sweeps the cleaned fiber off the teeth so the cylinder can take the next mouthful. The whole machine is small enough for a table and simple enough for a plantation workshop to copy, which is why it spread faster than Whitney could defend his patent. Then state the consequence in the reading's plain terms: a crop that had been limited by hand labor became profitable across a region, planters demanded more enslaved workers to grow it, and slavery, which many founders had expected to fade, expanded instead.",
17: "The portrait is Gilbert Stuart's John Jay of 1794, painted the year Jay sailed for London, showing the Chief Justice in his judicial robes. Section F moves the lesson abroad. In 1793 the war between revolutionary France and Britain put the young republic between its old ally and its largest trading partner, with a party at home leaning each way. Washington's answer across the whole section is consistency: a declared neutrality in 1793, a negotiated settlement with Britain in 1794, and a second treaty with Spain in 1795 that opened the Mississippi. Teach the section as a government learning to act as one country in foreign affairs, speaking through a president and envoys, while its own citizens argued in newspapers about which foreign cause was America's cause. That argument, foreign sympathy as party identity, is the one the Farewell Address takes up.",
18: "Slow down on the proclamation's two describing words, friendly and impartial, because students will quote them on the quick check. Washington declared that the United States would pursue that conduct toward the belligerent powers and warned citizens that aiding either side, or carrying contraband to one, would cost them their government's protection and expose them to prosecution. Note what the document never does: it never uses the word neutrality, and it speaks to American citizens rather than to France or Britain. The government was inventing foreign policy and domestic enforcement in the same act. Jefferson sympathized with France, Hamilton leaned toward Britain, and the proclamation held the country between them for the two years the treaties on the next slide required.",
19: "Give the Jay Treaty its price in full, because the price is the lesson. Britain evacuated the frontier posts it had held since 1783, with the withdrawal complete by June 1796, and trade and old debts were settled on paper. In return the United States compensated British creditors for prewar debts its own courts had failed to collect and accepted British limits on its trade with France. Federalists called it the best settlement a weak country could win without a war. Democratic-Republicans called it surrender dressed as diplomacy, burned Jay in effigy, and watched the Senate approve it by exactly the two thirds the Constitution required. Pinckney's Treaty with Spain, opening the Mississippi and settling the Florida boundary, calmed the West in the same years. Students should leave able to state one gain, one price, and the Senate margin.",
20: "The image returns to the lesson's anchor visual, Gilbert Stuart's Lansdowne portrait of Washington, painted in 1796, the year of the address: a president in a plain black suit and a dress sword, with the Federalist and the Journal of Congress on the table and a rainbow opening behind storm clouds. Section G closes the administration in print. Washington published his Farewell Address in a Philadelphia newspaper in September 1796 and went home to Mount Vernon after two terms, setting the two term practice presidents followed until the twentieth century. The address is a summing up by the man who had signed the bank bill, proclaimed neutrality, and sent the militia west, and it warns against the two forces his own years in office had called into being: party spirit at home and foreign entanglement abroad.",
21: "Teach the two warnings as a pair and quote the phrases students must carry. Against party: Washington warns in the most solemn manner against the baneful effects of the spirit of party generally, which distracts the public councils, weakens the administration, and kindles the animosity of one part against another, until it foments riot and insurrection. Against permanent alliances: the great rule of conduct toward foreign nations is to extend commercial relations while having as little political connection as possible, and it is our true policy to steer clear of permanent alliances with any portion of the foreign world. Then put the hard question to the room. Washington's cabinet had contained both party founders, and his treaties had divided the country he was addressing. Was he warning against dangers he had watched, or against dangers his own program had made?",
22: "Build the synthesis as the answer to the lesson question, in the question's own order. What the government had to invent was the working layer of the republic: a cabinet and courts in 1789, a financial program that funded the debt, assumed the state debts, chartered a bank, and laid an excise, a tax law enforced by an army when resisted, and a foreign posture of declared neutrality carried into treaties. What it warned against, as Washington left, was the spirit of party and permanent foreign alliances, the two forces his Farewell Address named in September 1796. Hold the third fact beside both halves: in the same years the cotton gin gave slavery a new economic engine, so the government being invented was also the government that would inherit the expansion of enslavement. The rest of the unit follows all three inheritances.",
23: "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. cabinet: the heads of the executive departments who advise the president, an office the Constitution nowhere creates, which Washington formed from the departments Congress established in 1789. assumption: the federal government's taking over of debts owed by others, the policy by which Hamilton's funding plan had the United States assume the states' Revolutionary War debts. excise tax: a tax on the manufacture or sale of a product inside the country, such as the 1791 tax on distilled whiskey that paid part of Hamilton's program and fell hardest on frontier farmers. Read the chain aloud: a cabinet invented, state debts assumed by the union, and a tax laid inside the country to pay for the program.",
24: "Four more terms, again matching the guided notes exactly. Bank of the United States: the national bank chartered by Congress in 1791 for twenty years, holding the government's money, issuing currency, and lending, which Hamilton defended under Congress's implied powers and Jefferson opposed. Whiskey Rebellion: the uprising of 1794 in western Pennsylvania against the federal excise tax on whiskey, which Washington answered by calling out the militia and leading it west, proving the government could enforce its laws. cotton gin: the machine patented by Eli Whitney in 1794 that separated cotton fiber from seed by machine, which made short-staple cotton profitable across the inland South and deepened the region's dependence on enslaved labor. Farewell Address: Washington's published letter of September 1796 announcing he would not seek a third term, which warned against permanent foreign alliances and against political parties, and set the two-term precedent presidents followed.",
25: "Close by returning to the lesson question and handing the lesson to the work. The activity, Building the Republic in Five Records, runs five stations through the evidence: Hamilton's bank opinion and the Neutrality Proclamation, the Jay Treaty and the cotton gin patent drawing, and the Farewell Address, ending in a ledger of problems solved and created and a verdict on which of Hamilton's four measures did the most to make the government real. The notebook page asks students to rebuild six pieces of the republic with evidence. The quick check tests the Neutrality Proclamation against its background. The writing task weighs the four measures against each other and closes on the Farewell Address. The exit ticket has three parts: Hamilton's four measures named in order; the Whiskey Rebellion answer explained; and the lesson question answered with two inventions and both warnings."
}

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

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'EARLY REPUBLIC AND EXPANSION · LESSON 1', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, "Washington's Republic: Hamilton, Parties, and the Farewell", size=36, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'What the first administration had to invent, 1789 to 1796', size=17, color=POWDER)
notes(s, N[1])

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("What did Washington's government have to invent, and what did it warn against as it left?", {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the United States turn its Constitution into a working government, and what did continental expansion do to the republic that government served?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, N[2])

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'The republic built, in seven stretches', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'A government to invent', 'Cabinet, courts, and first precedents'),
        ('B', "Hamilton's program in four parts", 'Funding, assumption, the Bank, the excise'),
        ('C', 'Strict reading and the first parties', 'Newspapers, Federalists, Democratic-Republicans'),
        ('D', 'The excise answered on the frontier', 'Whiskey, resistance, and an army of 13,000'),
        ('E', 'The cotton gin', 'A machine, and slavery given a new engine'),
        ('F', 'Neutrality and two treaties', 'A proclamation, Jay to London, the Mississippi opened'),
        ('G', 'The Farewell', 'Two warnings, and a president goes home')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, N[3])

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', 'A Government to Invent',
             'Offices named in the Constitution. Machinery still to build.',
             N[4])

# ------------------------------------------------------ 5 MACHINERY OF 1789
content_text('Machinery built in a single year',
             ['Departments of State, Treasury, and War',
              'Department heads become the cabinet',
              'Judiciary Act: a Supreme Court, lower courts',
              'The president received as head of state'],
             N[5],
             kick='A · A government to invent')

# ------------------------------------------------------ 6 1789 STAT
stat('1789', 'the year the government was assembled, not merely begun',
     'First cabinet · First federal courts · First revenue laws',
     N[6],
     kick='A · A government to invent')

# ------------------------------------------------- 7 SECTION B DIVIDER
divider_photo('hamilton-port.jpg', 'Section B', "Hamilton's Program in Four Parts",
              ['John Trumbull portrait of Alexander Hamilton,', 'first Secretary of the Treasury.'],
              N[7])

# ------------------------------------------------------ 8 FOUR PARTS
content_text('One design, four moving parts',
             ['Fund the war debt at full value',
              'Assume the war debts of the states',
              'Charter a national bank',
              'Lay an excise tax on distilled whiskey',
              'Each part rests on implied powers'],
             N[8],
             kick="B · Hamilton's program", size=24)

# ------------------------------------------------------ 9 TWENTY YEARS STAT
stat('20 years', 'the first charter of the Bank of the United States, 1791 to 1811',
     'Long enough for the country to build its credit on the Bank paper',
     N[9],
     kick="B · Hamilton's program")

# ------------------------------------------------- 10 SECTION C DIVIDER
divider_text('Section C', 'Strict Reading and the First Parties',
             'A bank the document never named, and an argument that organized a country.',
             N[10])

# ------------------------------------------------------ 11 PARTIES FORM
content_photo('jefferson-port.jpg', 'Two readings, two parties',
             ['Jefferson and Madison: strict reading',
              'A bank is a tool the document never named',
              'The argument moves into the newspapers',
              'Federalists and Democratic-Republicans'],
             N[11],
             kick='C · Strict reading and the first parties')

# ------------------------------------------------- 12 SECTION D DIVIDER
divider_photo('army-port.jpg', 'Section D', 'The Excise Answered on the Frontier',
              ['Washington reviewing the western army', 'at Fort Cumberland, by Frederick Kemmelmeyer.'],
              N[12])

# ------------------------------------------------------ 13 ROAD TO THE ARMY
content_text('From the tax book to the army camp',
             ['Whiskey: the one load a horse could carry',
              'Collectors tarred, the mail robbed, 1794',
              'Commissioners sent, a deadline set',
              'The militia called when the deadline failed'],
             N[13],
             kick='D · The excise answered', size=24)

# ------------------------------------------------------ 14 13,000 STAT
stat('13,000', 'militiamen called from four states to enforce the excise in 1794',
     'The rebellion dissolved without a battle · Two men convicted of treason, and pardoned',
     N[14],
     kick='D · The excise answered')

# ------------------------------------------------- 15 SECTION E DIVIDER
divider_photo('gin-port.jpg', 'Section E', 'The Cotton Gin',
              ["Whitney's patent drawing of 1794,", 'from the restored copy of 1845.'],
              N[15])

# ------------------------------------------------------ 16 HOW THE GIN WORKED
content_text('Teeth, slots, and a new engine for slavery',
             ['Wire teeth drag the fiber through slots',
              'Seeds, too large to pass, are held back',
              'A brush wheel sweeps the teeth clean',
              'Short staple cotton becomes profitable',
              'Planters demand more enslaved labor'],
             N[16],
             kick='E · The cotton gin', size=24)

# ------------------------------------------------- 17 SECTION F DIVIDER
divider_photo('jay-port.jpg', 'Section F', 'Neutrality and Two Treaties',
              ['Gilbert Stuart portrait of John Jay, 1794,', 'the year Jay sailed for London.'],
              N[17])

# ------------------------------------------------------ 18 NEUTRALITY
content_text('Friendly and impartial, declared in 1793',
             ['France at war with Britain, February 1793',
              'A conduct friendly and impartial',
              'Citizens warned: aid either side, lose protection',
              'The word neutrality never appears'],
             N[18],
             kick='F · Neutrality and two treaties', size=24)

# ------------------------------------------------------ 19 JAY TREATY PRICE
content_text('The Jay Treaty, and its price',
             ['Britain evacuates the frontier posts by 1796',
              'The United States pays British creditors',
              'British limits on American trade accepted',
              'Senate approves by the bare two thirds',
              "Pinckney's Treaty opens the Mississippi"],
             N[19],
             kick='F · Neutrality and two treaties', size=24)

# ------------------------------------------------- 20 SECTION G DIVIDER
divider_photo('washington-port.jpg', 'Section G', 'The Farewell',
              ['The Lansdowne portrait of Washington,', 'by Gilbert Stuart, 1796.'],
              N[20])

# ------------------------------------------------------ 21 TWO WARNINGS
content_text('Two warnings, published in a newspaper',
             ['Against the spirit of party',
              'It distracts councils, kindles animosity',
              'Extend commerce, keep political connection small',
              'Steer clear of permanent alliances',
              'No third term: the precedent of leaving'],
             N[21],
             kick='G · The Farewell', size=24)

# ------------------------------------------------------ 22 SYNTHESIS
content_text('Invented, warned, and inherited',
             ['Invented: cabinet, courts, credit, enforcement',
              'Warned: party spirit, permanent alliances',
              'Inherited: slavery expanding under the gin',
              'Two parties already campaigning'],
             N[22],
             kick='G · The Farewell')

# ------------------------------------------------------ 23 VOCAB A
vocab('Words for the machinery and the money',
      [('cabinet', 'the department heads who advise the president'),
       ('assumption', 'the union takes over the debts of the states'),
       ('excise tax', 'a tax on a product made or sold inside the country')],
      N[23])

# ------------------------------------------------------ 24 VOCAB B
vocab('Words for the bank, the rising, the machine, the address',
      [('Bank of the United States', 'the national bank chartered in 1791'),
       ('Whiskey Rebellion', 'the 1794 rising against the excise'),
       ('cotton gin', "Whitney's machine of 1794"),
       ('Farewell Address', "Washington's published letter of 1796")],
      N[24])

# ------------------------------------------------------ 25 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Build the republic in five records', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ["For each record, state the problem it was solving and the new problem it created. Then judge which of Hamilton's four measures did the most to make the federal government real."],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'Building the Republic in Five Records: the bank opinion, the proclamation, the treaty, the patent, the address'),
        ('Notebook', 'Notebook page: six pieces of the republic, classified and evidenced'),
        ('Quick check', 'Hold the Country Out of the War: the proclamation read against its background'),
        ('Writing', 'Which Measure Made the Government Real? The four measures weighed, the Farewell as the cost')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the four measures in order, the Rebellion answer explained, and the lesson question answered with two inventions and both warnings.',
     size=15, color=POWDER)
notes(s, N[25])

dc.save(OUT)
