#!/usr/bin/env python3
"""Early Republic Lesson 6 deck, "The Era of Good Feelings: The American
System and the Marshall Court," built to the approved system: image-led
slides, fragments only on screen, comprehensive speaker notes, full lesson
and vocabulary coverage. Fonts: Georgia titles, Lato body."""
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
OUT = os.path.join(HERE, '..', 'lesson-06-slides.pptx')

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
text(s, 0.9, 5.32, 11.5, 0.4, 'THE EARLY REPUBLIC AND EXPANSION · LESSON 6', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Era of Good Feelings', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'The American System and the Marshall Court', size=17, color=POWDER)
notes(s, "The image is a detail of Henry Inman's 1832 portrait of Chief Justice John Marshall, held by the Library of Virginia and in the public domain. Marshall belongs on the title because his Court supplied half of this lesson: the opinions of 1819 and 1824 that read the Constitution for a building nation. The other half belongs to Congress and the presidents: a bank chartered, a tariff laid for protection, roads and canals proposed and vetoed, and a panic that charged the country for all of it. The lesson runs from the peace of 1815 to the steamboat decision of 1824, and it asks students to measure, record by record, how far the national government's reach actually grew, and where it stopped.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("After the war, how far would Americans let their national government build?", {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ("How did the United States turn its Constitution into a working government, and what did continental expansion do to the republic that government served?", {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Read the lesson question slowly and notice its wording. It does not ask whether the national government grew; the charters, tariffs, and opinions settle that it did. It asks how far Americans would let it build, which makes consent and resistance part of the evidence: a president vetoing his own party's bill, a state building the canal the federal government would not, western debtors cursing the bank the Supreme Court had just sustained. Students should expect a measured answer, in miles of canal, in a twenty year charter, in a tax struck down and a monopoly dissolved. By the end of the hour they will judge the whole record in the activity's verdict: Hamilton's program fulfilled, or a new thing built from the war's lessons.")

# ------------------------------------------------- 3 ONE SLIDE
s = slide(CREAM)
kicker(s, 'The lesson in one slide', color=RUST)
text(s, 0.9, 0.95, 11.5, 1.0, 'Seven parts, in order', size=31, color=NAVY, font='Georgia')
frags(s, ['A. The peace and the mood it bought',
          'B. The program of 1816',
          "C. Clay's American System",
          'D. The constitutional brakes',
          'E. The Panic of 1819',
          'F. McCulloch and the nationalist Court',
          'G. Gibbons and the reach of commerce'], y=2.0, size=25, gap=10)
notes(s, "Use this slide as the map of the hour, and point students to the same seven letters in their guided notes. Section A sets the scene: one party, a presidential tour, and a newspaper's name for the mood, with the war's hard lessons underneath. Section B takes the building itself, the Second Bank and the protective tariff of 1816, signed by Madison. Section C gives the building its theory in Clay's American System. Section D applies the brakes: the Bonus Bill veto of 1817, Monroe's veto of 1822, and New York building the Erie Canal as a state. Section E charges the price in the Panic of 1819. Sections F and G move to the Court: McCulloch on the bank and state taxation, and Gibbons on commerce and the waterways.")

# ------------------------------------------------- 4 DIVIDER A
divider_text('Section A', 'The Peace and the Mood It Bought',
    'One party, a tour, and the lessons underneath',
    "Set the scene with precision about the famous name. The Era of Good Feelings was a newspaper phrase, printed in Boston in 1817 as Monroe toured the country and was received by crowds that included men who had been Federalists two years earlier. The Federalist Party had collapsed as a national force after the Hartford Convention, whose report reached Washington alongside the news of peace and of New Orleans. With one party holding the field, the old arguments of 1798 seemed buried. Teach students to distrust the calm as an explanation. The building of the next decade did not come from good feelings; it came from a war that had exposed an empty fiscal machinery, and the men doing the building said so at the time.")

# ------------------------------------------------- 5 CONTENT A
content_text('What the war had shown',
    ['No national bank since 1811', 'A currency of state bank notes', 'Troops delayed on poor roads', 'Governors refusing their militia'],
    "Walk the four failures as the builders themselves listed them. When the first Bank's charter expired in 1811, the Treasury lost its fiscal agent, and the war was financed on loans and on the notes of hundreds of state banks, of uneven value from place to place. Moving troops and supplies over the roads of 1812 was slow enough to shape strategy. New England's governors refused to place their militia under federal command, and the government watched a section decline to fight its war. None of this required a theory to explain in 1816; it required machinery. That is why the program of the next section was carried by Republicans who had once opposed it: experience, in Madison's later phrase for his own change, had intervened, and the war had been the experience.",
    kick='Section A · The lessons')

# ------------------------------------------------- 6 STAT A
stat('1817', 'the year Monroe toured a one party country',
    'A Boston newspaper names the moment the Era of Good Feelings',
    "Use the year to separate the mood from the machinery. Monroe's tour of 1817 was a political fact: the president of one party was cheered in Boston, the former capital of the other, and a Boston paper gave the moment its lasting name. But ask the class what a tour builds. It builds nothing that collects a tax, issues a currency, or moves a regiment. The machinery of this lesson was built in the session of 1816, before the tour, by a Congress answering the war's failures. Keep the two timelines side by side all hour: the feelings run 1817 forward at the top of politics, while underneath them the charter, the tariff, the veto, the panic, and the opinions follow their own harder chronology, and the second timeline is the one the documents record.",
    kick='Section A · The name')

# ------------------------------------------------- 7 DIVIDER B
divider_text('Section B', 'The Program of 1816',
    'A bank chartered, a tariff laid for protection',
    "One session of Congress did the building, and students should hold the date firmly: 1816, the year after the war ended. In that session Congress chartered the Second Bank of the United States for twenty years and passed the Tariff of 1816, the first tariff in the nation's history laid avowedly for protection rather than only for revenue. President Madison signed both bills. Neither measure was a Federalist survival smuggled past a Republican government; both were enacted by the party that had opposed their predecessors, on majorities built from the war's experience. This section takes the two measures in order, then pauses on the signature itself, because Madison's name on the bank charter is the single most instructive fact in the lesson: the strict constructionist of 1791, converted by a war.")

# ------------------------------------------------- 8 CONTENT B
content_text('Two measures, one session',
    ['Second Bank chartered for twenty years', "Larger than Hamilton's first Bank", "To hold the government's money", 'Tariff of 1816, the first for protection'],
    "Take the measures separately before joining them. The Second Bank of the United States was chartered in 1816 for twenty years, on a larger scale than Hamilton's first Bank, to hold the government's deposits, transfer its funds, issue a currency that would pass everywhere, and by its presence restrain the note issues of the state banks. The Tariff of 1816 laid duties on imported manufactures, above all iron and textiles, at levels meant to shelter American makers from the flood of British goods that arrived with the peace; earlier tariffs had been laid for revenue, and protection had been their side effect, while this one reversed the order openly. Together the two measures gave the federal government a fiscal machine and an industrial policy in a single session, a combination the republic had not had since the 1790s.",
    kick='Section B · The building')

# ------------------------------------------------- 9 CONTENT B2
content_text('Madison signs',
    ['He had opposed the first Bank in 1791', 'On constitutional grounds', 'The war persuaded him experience had answered', "The currency's disorder was the danger"],
    "Slow down on the signature, because it carries the lesson's fairness rule in one career. In 1791 James Madison had argued in the House that Congress held no power to charter a bank, the strict reading on which his party was built. In 1816 President Madison signed the Second Bank's charter. He explained himself on the record across his presidency: the question, he held, had been settled by the repeated recognitions of the bank's validity by every branch of the government and by the people, and the war had shown what a currency of hundreds of state bank notes cost a government trying to pay an army. Students need not decide today whether his reasoning was principle or surrender. They should be able to state it accurately: the opponent of the first Bank chartered the second, and he said experience had answered the constitutional question.",
    kick='Section B · The signature')

# ------------------------------------------------- 10 DIVIDER C
divider_text('Section C', "Clay's American System",
    'Bank, tariff, and improvements as one design',
    "Henry Clay of Kentucky, Speaker of the House, gave the program of 1816 its name, its theory, and its future. Clay had been a War Hawk in 1811 and a peace commissioner at Ghent, and he came home convinced that the republic's weakness was economic before it was military: a country that bought its manufactures abroad and moved its crops on bad roads would remain a dependency in fact whatever its flag said. His American System joined the bank and the tariff to a third part Congress had not yet enacted, federally funded internal improvements, and presented the three as one design with one purpose, a home market. Teach the system as Clay argued it, a circle of exchanges among the sections, before Section D shows which part of the circle the Constitution's own readers refused to close.")

# ------------------------------------------------- 11 CONTENT C
content_text('One market, three parts',
    ['A bank for a uniform currency', 'A tariff to shelter manufactures', 'Improvements paid from the revenue', 'Each section buying from the others'],
    "Draw Clay's circle on the board as you teach this slide, because the system is a circle or it is nothing. The national bank gives the whole country one currency and orderly credit, so a farmer's payment in Kentucky is a manufacturer's receipt in Massachusetts. The protective tariff shelters northern manufactures until they can stand, and its duties fill the Treasury. The revenue pays for roads and canals, the internal improvements that carry western food to eastern mill towns and carry manufactures back. Then the sections trade: western farmers feed the mill towns, southern cotton clothes workers in both, northern goods find buyers at home instead of competing for foreign markets. Clay's claim was political as much as economic: sections that prosper by each other's demand will not easily pull the union apart.",
    kick='Section C · The design')

# ------------------------------------------------- 12 STAT C
stat('3', 'parts to one system, argued as a single design',
    "Bank, protective tariff, and internal improvements, each one carrying the other two",
    "Use the small number to test whether students hold the system whole. Ask for the three parts in order and refuse a list without the links: the bank serves the currency, the tariff serves the manufactures and raises the revenue, the improvements serve the movement of goods the other two parts create. Then ask which part was already law in 1816 and which was not. The bank and the tariff stood enacted; the improvements bill, the Bonus Bill, was vetoed in 1817, and that failure is structural, not incidental: Clay's circle was drawn around a third part the federal government never supplied, so the system as built ran on two of its three parts, with the states, above all New York, building the third part themselves. Section D takes that failure in full.",
    kick='Section C · The count')

# ------------------------------------------------- 13 DIVIDER D
divider_text('Section D', 'The Constitutional Brakes',
    'A veto in 1817, a veto in 1822, and a canal built by a state',
    "Now apply the brakes, and insist on who applied them. The Bonus Bill of 1817 was John C. Calhoun's bill, carried by the nationalist wing of the Republican party, to set the Second Bank's bonus payment and dividends aside as a permanent fund for roads and canals. The man who vetoed it was not a Federalist and not an enemy of the program; it was James Madison, on March 3, 1817, his last full day in office, eleven months after signing the bank charter. Monroe repeated the veto in 1822. This section teaches the veto's argument in Madison's own words, from Station 4 of the activity, and then follows the work the federal government refused into the hands of the state that did it, New York, on the Erie Canal.")

# ------------------------------------------------- 14 CONTENT D
content_text('The Bonus Bill veto',
    ['Roads and canals, funded from the Bank', 'Vetoed March 3, 1817', 'The power is nowhere enumerated', 'The remedy named is an amendment'],
    "Teach the veto as an argument in Madison's own sequence, because students will meet the text at Station 4. First, the legislative powers of Congress are specified and enumerated in Article I, section 8. Second, the power to construct roads and canals does not appear among them. Third, it cannot be reached by any just interpretation of the necessary and proper power. Fourth, and this is the step students miss, Madison concedes the policy: he is not unaware of the great importance of roads and canals, and a federal power to build them might be exercised with signal advantage to the general prosperity. The concession is the argument's strength. A president who wants the roads and still vetoes their funding has isolated the constitutional ground as the entire dispute, and his remedy follows from it: grant the power by amendment, as the Constitution provides.",
    kick='Section D · The veto')

# ------------------------------------------------- 15 CONTENT D2
content_text('The states build instead',
    ['Monroe vetoes again in 1822', 'New York begins the Erie Canal in 1817', 'State money, state treasury', 'Opened 1825, Albany to Lake Erie'],
    "Follow the work into the state's hands and give the canal its full scale. While Madison's veto stood unrepaired in Washington, New York broke ground for the Erie Canal in 1817, under Governor DeWitt Clinton, and paid for the work from the state treasury, borrowing on the state's credit against the tolls to come. The canal opened in 1825, running more than 360 miles from Albany on the Hudson to Lake Erie, and it cut the cost of moving freight between the lakes and the seaboard by an order of magnitude; the standard accounts put the Buffalo to New York freight rate near a tenth of its former level. Teach the constitutional meaning plainly: the era's greatest internal improvement was not a federal work. The veto had limited the federal government, not the building, and the states entered the space the veto left.",
    kick='Section D · The canal')

# ------------------------------------------------- 16 STAT D
stat('360+', 'miles of canal from Albany to Lake Erie',
    'Begun by New York State in 1817, opened in 1825, paid from the state treasury',
    "Use the distance to make the state built alternative concrete. More than 360 miles of dug channel, locks, and aqueducts made the Erie Canal the longest artificial waterway of its age in the republic, and every mile of it was a state work, authorized by a state legislature, financed on state credit, and repaid from state tolls. Place it beside the veto the class has just read: the same political generation that produced Madison's enumerated powers argument also produced a state willing to borrow millions on its own account to do the work the federal government had declined. When students later generalize about an age of small government, this slide is the correction: government in these years was building at full scale, and the live argument was about which government, federal or state, the Constitution allowed to build.",
    kick='Section D · The scale')

# ------------------------------------------------- 17 DIVIDER E
divider_text('Section E', 'The Panic of 1819',
    'The calm breaks on credit, cotton, and foreclosures',
    "The Panic of 1819 is the era's first fracture, and it arrives from inside the new machinery, which is why this lesson places it between the veto and the Court. The land boom of the war years and after was bought on credit, at prices floated by high cotton prices, with paper borrowed from state banks and from the Second Bank's own branches. When the prices fell and the Bank reversed course to save itself, the debts remained. This section teaches the chain in order, boom, reversal, failure, foreclosure, and then asks what the panic did to the politics of the program: the institution at the center of Clay's first part survived the crisis it had helped to cause, and it emerged with its charter intact and its public standing in the West destroyed.")

# ------------------------------------------------- 18 CONTENT E
content_text('Boom, reversal, foreclosure',
    ['Land bought on credit at cotton prices', 'State banks printing notes freely', 'The Second Bank calls in its loans', 'Farms foreclosed, banks failing'],
    "Build the chain link by link, and name the Second Bank's part in both halves of it. In the boom, the Bank under its first president, William Jones, let its western and southern branches lend freely, feeding the same speculation the state banks fed. When cotton prices fell in 1818 and 1819 and the Bank's own reserves came under strain, the Bank reversed: under Jones and then Langdon Cheves it called in loans, demanded payment in specie, and pressed the state banks to redeem their notes or fail. Banks failed. Land bought at boom prices would not pay its debts at fallen prices, and the Bank foreclosed on farms and town lots across the West. In the cities, merchants failed and working people lost employment, in the first great peacetime depression the country had known. Relief laws in the states were the politics that followed.",
    kick='Section E · The chain')

# ------------------------------------------------- 19 STAT E
stat('1819', 'the first great peacetime depression of the United States',
    'The Second Bank steadied the currency and spent its standing in the West doing it',
    "Use the date to fix the panic inside the Era of Good Feelings, not after it: the collapse of 1819 sits between the bank charter of 1816 and the Missouri crisis of the next lesson, in the middle of the calm the newspapers had named. Two judgments belong together and students should be made to hold both. By the middle of the 1820s the Bank had restored a sound and uniform currency, the service its charter promised, and even many critics conceded the steadiness. And the foreclosures of 1819 and 1820 had taught a generation of western debtors to hear the word bank as the name of a distant creditor power, a lesson Andrew Jackson's presidency would later collect in full. The panic is therefore not an interruption of this lesson's story; it is the story's price, charged in the West.",
    kick='Section E · The price')

# ------------------------------------------------- 20 DIVIDER F
divider_photo('marshall-port.jpg', 'Section F', 'McCulloch and the Nationalist Court',
    ['Maryland taxes the Bank, and loses', 'The opinion of 1819'],
    "The image is Henry Inman's 1832 portrait of Chief Justice John Marshall, held by the Library of Virginia and in the public domain. Marshall had been chief justice since 1801, a Federalist appointed by John Adams, outliving his party on a court that now decided the Republican program's fate. In McCulloch v. Maryland the question reached him in its sharpest form: Maryland had taxed the notes of the Second Bank's Baltimore branch, and the branch's cashier had issued notes without paying. The case therefore asked both questions of the era at once, whether Congress could charter the bank at all, and whether a state could tax the instrument Congress had created. Marshall's opinion answered the first with the broadest statement of implied powers in the Court's history and the second with the sentence the case is remembered by.")

# ------------------------------------------------- 21 CONTENT F
content_photo('marshall-port.jpg', 'The Bank sustained',
    ['Congress may charter a bank', 'Powers implied from the great ends', 'A constitution meant to endure', 'Adapted to the crises of human affairs'],
    "The image is Inman's Marshall again. Teach the first holding as a piece of reasoning students will reproduce at Station 1. Marshall begins from the document's character: it is a constitution being expounded, intended to endure for ages to come and to be adapted to the various crises of human affairs, so it cannot enumerate every means by which its great ends will be served. From that premise the test follows: let the end be legitimate and within the scope of the Constitution, and all means which are appropriate, plainly adapted to that end, not prohibited, and consistent with the letter and spirit of the Constitution, are constitutional. Chartering a bank is such a means to the ends of taxing, borrowing, and regulating commerce. Note for the class that this is Hamilton's bank argument of 1791, adopted by a court in 1819 as the law of the Constitution.",
    kick='Section F · The holding')

# ------------------------------------------------- 22 CONTENT F2
content_text('The tax struck down',
    ['The power to tax involves the power to destroy', 'One government may not control another', 'Dartmouth College, the same year', 'Charters protected as contracts'],
    "Take the second holding with the same care. If Maryland may tax the Bank's notes at all, it may tax them at any rate, and the power to tax, exercised without a limit the taxpayer can appeal to, involves the power to destroy. A state would then hold the power to defeat and render useless a measure of the government of the whole people, which is declared supreme in its sphere; Marshall calls the repugnance in that arrangement plain and not to be denied. The tax fell. Add the companion decision of the same year for completeness: in Dartmouth College v. Woodward the Court held a corporate charter to be a contract the state that granted it could not rewrite, protecting the charters on which the era's banks, colleges, and canal companies stood. Together the two decisions of 1819 fenced the states out of the era's building instruments.",
    kick='Section F · The limit on states')

# ------------------------------------------------- 23 DIVIDER G
divider_text('Section G', 'Gibbons and the Reach of Commerce',
    'A steamboat monopoly falls, and navigation becomes commerce',
    "Close the lesson's argument where the era closed it, on the water. The steamboat was the new machine of the 1820s economy, and the states had rewarded its pioneers with monopolies: New York had granted Robert Livingston and Robert Fulton the exclusive right to navigate its waters by steam, and Aaron Ogden held that right for the route between New York and New Jersey. Thomas Gibbons ran competing boats on the same water under a license Congress had issued. In Gibbons v. Ogden, decided in 1824, Marshall used the collision to define the commerce power for the machine age. This final section teaches the definition and its reach, and then the lesson closes by reading the whole era against the question it opened with.")

# ------------------------------------------------- 24 CONTENT G
content_text('Commerce is intercourse',
    ['Commerce is traffic, and something more', 'It includes navigation', 'It does not stop at a state border', "Congress's power is complete in its sphere"],
    "Teach the definition first, in Marshall's own words from Station 2. Commerce, undoubtedly, is traffic, but it is something more: it is intercourse, the commercial intercourse between nations and parts of nations in all its branches, and a system for regulating it that excluded navigation would scarcely be conceivable. From the definition the reach follows: commerce among the several states means commerce intermingled with them, and it cannot stop at the external boundary line of each state but may be introduced into the interior, while commerce completely internal to one state remains reserved. The power to regulate that commerce is complete in itself, exercisable to its utmost extent, limited only by the Constitution. Applied to the case, the federal license prevailed and the monopoly fell, opening the nation's waterways to the competition the state grants had closed.",
    kick='Section G · The definition')

# ------------------------------------------------- 25 AT A GLANCE
content_text('The lesson at a glance',
    ['The mood: one party, and the war\u2019s lessons underneath',
     'The program: bank and protective tariff, 1816',
     "Clay's design: one home market in three parts",
     'The brakes: the veto of 1817, the canal built by a state',
     'The Court: implied powers and commerce, 1819 and 1824'],
    "This slide mirrors the closing table in the guided notes, The Era at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The five lines are the lesson's measured answer to its question. The mood of good feelings was real at the top of politics and explains none of the building; the war's lessons explain the program of 1816, bank and tariff, signed by the strict constructionist of 1791. Clay gave the building its theory of one home market. The brakes were applied by the builders themselves, a veto in 1817 and a canal raised by a state instead. And the Court, in 1819 and 1824, wrote the widest reading of federal power into law while the panic charged the program's price in the West.",
    kick='Review')

# ------------------------------------------------- 26 VOCAB 1
vocab('Words for the program', [
    ('American System', "Clay's program of bank, tariff, and improvements, binding the sections into one economy"),
    ('Second Bank of the United States', 'chartered 1816 for twenty years, to order a currency of state bank notes'),
    ('protective tariff', 'a tax on imports set to shelter American manufactures, first in the Tariff of 1816'),
    ('internal improvements', 'roads, canals, and harbors the nation needed and Congress was doubted to fund')],
    "These definitions match the guided notes word for word, and students copy them exactly. American System: Henry Clay's program of a national bank, a protective tariff, and federally funded internal improvements, meant to bind the sections into one economy in which western food, southern cotton, and northern manufactures traded with each other. Second Bank of the United States: the national bank chartered in 1816 for twenty years, larger than Hamilton's first Bank and created because the war had exposed the disorder of a currency issued by hundreds of state banks. protective tariff: a tax on imported goods set high enough to shelter American manufacturers from foreign competition rather than only to raise revenue, first enacted as national policy in the Tariff of 1816. internal improvements: roads, canals, and harbors built to move goods and people inside the country, which nearly every president of the era agreed the nation needed and many held the Constitution gave Congress no power to fund.")

# ------------------------------------------------- 27 VOCAB 2
vocab('Words for the crisis and the Court', [
    ('Panic of 1819', 'the collapse of 1819, credit contracted and the speculation burst'),
    ('McCulloch v. Maryland', "1819: the Bank sustained under implied powers, Maryland's tax struck down"),
    ('Gibbons v. Ogden', '1824: commerce read broadly, the steamboat monopoly struck down')],
    "Three more terms, again matching the guided notes exactly, and students copy them as written. Panic of 1819: the financial collapse of 1819, the first great peacetime depression of the United States, in which the Second Bank's contraction of credit helped burst a land and cotton speculation, throwing western farmers and city workers into ruin. McCulloch v. Maryland: the Supreme Court decision of 1819 in which Chief Justice Marshall held that Congress could charter a bank under its implied powers and that Maryland could not tax it, because the power to tax is the power to destroy. Gibbons v. Ogden: the Supreme Court decision of 1824 in which Chief Justice Marshall read Congress's power to regulate commerce among the states broadly, striking down a state steamboat monopoly and opening the nation's waterways to competition.")

# ------------------------------------------------- 28 SYNTHESIS
content_text('Synthesis: built by law, widened by interpretation',
    ['Congress built the machinery in 1816',
     "The builders were Hamilton's opponents",
     'The veto stopped the third part at the enumeration',
     'The Court widened what the statutes rested on',
     'The panic charged the West for the first part'],
    "Draw the lesson together by answering the lesson question in full sentences students can borrow. How far would Americans let their national government build? Far enough to charter a bank and protect manufactures by law in 1816, under a president who had opposed the first bank on constitutional grounds, because a war had taught the cost of building nothing. Not far enough to fund roads and canals from the Treasury: the program's own president vetoed that part in 1817 and named an amendment as the only road to it, and a state built the era's canal instead. Further in court than in Congress: Marshall's opinions of 1819 and 1824 sustained the bank on implied powers, barred the states from taxing it, and read commerce to the interior of every state. And the consent underneath the building thinned as it grew, in the foreclosures of 1819.",
    kick='Synthesis')

# ------------------------------------------------- 29 EXIT
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.15, 11.5, 1.6, 'Answer the question, from the records',
     size=36, color=CREAM, font='Georgia', leading=1.15)
text(s, 0.9, 2.55, 11.5, 1.1, ['After the war, how far would Americans let their',
                               'national government build? Build from the documents.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Nationalism File: five records, a ledger, and a verdict'),
        ('Notebook', 'Notebook page: built, reach, limit or cost, and one paragraph'),
        ('Quick check', 'The Reach and Its Limits: McCulloch and the veto at work'),
        ('Writing', "Hamilton's Program Fulfilled, or a New Thing? Argued from the file")]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the three parts of the system, one widening and one stopping with dates, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Nationalism File, runs five records: McCulloch v. Maryland and Gibbons v. Ogden, quoted from the audited records; Clay's tariff speech of March 1824, quoted as the House history carries it; Madison's Bonus Bill veto of March 3, 1817, quoted from the Richardson edition; and a labeled teaching summary of the Panic of 1819. Students keep a ledger of widening and narrowing, with the constitutional ground of each, and close with a verdict: Hamilton's program fulfilled, or a new thing built from the war's lessons. The quick check works Marshall's test and Madison's enumeration side by side. The writing task argues the verdict as an essay. The exit ticket asks for the system's three parts, one widening and one stopping with dates, and the lesson question answered in two or three sentences.")

dc.save(OUT)
