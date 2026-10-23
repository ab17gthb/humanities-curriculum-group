#!/usr/bin/env python3
"""Build the Early Republic and Expansion review study guide from the
verbatim vocabulary in build-scripts/unit-spec.md, plus 24 review
questions with a full key, a short frame passage, and the fifteen
entries of the unit blueprint restated in student language. Mirrors
the Founding study guide. The teacher key carries no blueprint tags."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
UNIT = os.path.dirname(HERE)
SPEC = open(os.path.join(HERE, "unit-spec.md")).read()

LESSON_TITLES = {
    1: "Washington's Republic: Hamilton, Parties, and the Farewell",
    2: "The Alien and Sedition Acts and the Revolution of 1800",
    3: "Jefferson's Republic and the Louisiana Purchase",
    4: "Lewis and Clark and the Peoples of the West",
    5: "The War of 1812",
    6: "The Era of Good Feelings: The American System and the Marshall Court",
    7: "The Monroe Doctrine and the Missouri Compromise",
    8: "Manifest Destiny and the War with Mexico",
}

def parse_terms():
    terms = {}
    current = None
    in_vocab = False
    for line in SPEC.splitlines():
        if line.startswith("## Vocabulary"):
            in_vocab = True
            continue
        if in_vocab and line.startswith("## "):
            break
        if not in_vocab:
            continue
        m = re.match(r"### Lesson (\d)", line)
        if m:
            current = int(m.group(1)); terms[current] = []
            continue
        m = re.match(r"- ([^:]+): (.+)$", line)
        if m and current:
            terms[current].append((m.group(1).strip(), m.group(2).strip()))
    return terms

QUESTIONS = [
    (1, "What did Washington's first administration have to invent, and how did the cabinet and the federal courts take shape?",
     "The Constitution named offices and powers but not the machinery for using them, so the first administration built the machinery while the government was already running. Congress created the executive departments in 1789, and Washington formed his cabinet from the heads of those departments, an office the Constitution nowhere creates. Congress organized the federal courts in the same season, the president was received as head of state, and every act stood as a precedent because everything was being done for the first time. The government students meet in this lesson is an invention, assembled piece by piece by the men who had to operate it."),
    (1, "State Hamilton's financial program in its four parts, and name the constitutional ground the whole design rested on.",
     "Hamilton's program was one design with four moving parts. The national debt would be funded at full value so the government's credit would stand. The federal government would assume the states' war debts so the creditors of the union would look to the union. Congress would charter a national bank to hold the government's money, issue a uniform currency, and make credit move. An excise tax on distilled whiskey would help pay for it all, and it fell hardest on the frontier farmers for whom whiskey was the only form in which their corn could reach a market. Each part rested on a broad reading of the Constitution's powers, the necessary and proper clause above all, and Jefferson and Madison answered with a strict reading, which is how the argument inside the cabinet became the first parties."),
    (1, "How did the Whiskey Rebellion test Washington's enforcement precedent, and what did the Farewell Address warn against?",
     "Western Pennsylvania farmers resisted the excise in 1794, tarring tax men, robbing the mail, and attacking a federal marshal's house. Washington answered by calling a militia army of some thirteen thousand men from four states and leading it part of the way west himself. The rebellion dissolved before the army arrived, two men were convicted of treason and pardoned, and the point stood that the new government's laws would be enforced by the government itself rather than watched helplessly, as Congress had watched under the Articles. Retiring in 1796 after two terms, a precedent in itself, Washington published his Farewell Address warning against permanent alliances with foreign nations and against the spirit of party he had watched form inside his own cabinet."),
    (2, "What war scare produced the laws of 1798, and what did the four laws do as one program?",
     "The French Revolution's wars reached American politics as a party question. In the XYZ Affair of 1798, French agents demanded a bribe and a loan before they would negotiate, the published dispatches inflamed opinion, and an undeclared naval war with France followed in the Caribbean while Federalist majorities prepared for a war they half expected to come ashore. The four laws of 1798 read as one program. The Naturalization Act stretched the wait for citizenship from five years to fourteen. The Alien Friends Act and the Alien Enemies Act armed the president against immigrants by decree. The Sedition Act made it a crime to write or publish false, scandalous, or malicious matter against the government, Congress, or the president, and its prosecutions fell on Republican editors and on a sitting congressman, Matthew Lyon of Vermont, who was jailed for criticizing President Adams and reelected from his cell."),
    (2, "How did the Virginia and Kentucky Resolutions answer the acts, and what limit did their reception show?",
     "Jefferson wrote the Kentucky Resolutions and Madison the Virginia Resolutions in secret in 1798 and 1799. They argued that the Constitution was a compact among the states, that the federal government held only delegated powers, and that the states retained the right to judge when those powers had been exceeded. Kentucky's second set of resolutions went further and named the remedy nullification, the claim that a state may declare a federal law void inside its borders. The doctrine would outgrow its authors and return in later years carrying far heavier loads. The limit stands in the record too. Ten states answered back rejecting the resolutions, and no state joined them, so in 1799 the doctrine persuaded almost no one beyond its authors."),
    (2, "How did the election of 1800 deadlock, how was the transfer secured, and what did the Twelfth Amendment change?",
     "Every Republican elector voted for both Jefferson and Burr, so the two men tied at seventy three electoral votes and the election went to the Federalist House of Representatives. The House deadlocked through thirty five ballots in February 1801 while some Federalists schemed to install Burr, and Hamilton argued for Jefferson as the lesser danger. On the thirty sixth ballot the transfer was secured. Adams left Washington before dawn on inauguration day and Jefferson walked to his swearing in, and in his First Inaugural he said that every difference of opinion is not a difference of principle. A party that had jailed its opponents surrendered power to them on the strength of ballots, with no soldier in the street. The Twelfth Amendment, ratified in 1804, separated the ballots for president and vice president so the tie of 1800 could not happen again."),
    (3, "What did Jefferson's program unwind, and what inheritance from Adams could he not unwind?",
     "Jefferson let the Sedition Act expire and pardoned its prisoners, restored the naturalization wait to five years, repealed the whiskey excise, and cut the army and the navy. At the Treasury, Gallatin ran the government on customs duties and land sales while paying down the national debt Hamilton had funded, treating the debt as a moral burden. The whole program rested on the strict reading of the Constitution Jefferson had wielded against the Bank. The inheritance he could not unwind was Adams's Judiciary Act of 1801 and its midnight judges, commissions signed and sealed in the presidency's last days. One commission, William Marbury's, sat undelivered in the secretary of state's office, and Marbury's suit over it reached the Supreme Court in 1803."),
    (3, "How did Marbury v. Madison surrender the case and claim judicial review in the same opinion?",
     "Chief Justice Marshall, Adams's own secretary of state and a Federalist holding office for life, faced a trap. Ordering Secretary of State Madison to deliver the commission would invite refusal and weaken the Court, while surrendering openly would weaken it further. The opinion of February 1803 held that Marbury deserved his commission, then held that the law granting the Supreme Court original jurisdiction in such cases was itself unconstitutional, so the commission could not be ordered after all. The Court gave up the case in front of it and claimed in the same opinion the power of judicial review, the authority to declare acts of Congress void. No president dared attack the claim, because the decision had given Jefferson the only outcome he wanted, which was keeping Marbury off the bench."),
    (3, "Why did Jefferson sign the Louisiana Purchase despite his constitutional scruples, and what did the treaty do?",
     "Napoleon, his American empire broken in Haiti and war with Britain resuming, offered not New Orleans alone but the whole of Louisiana. Jefferson stated his scruple honestly. The Constitution gave no express power to acquire territory or to govern it, and he drafted an amendment to supply the power, then abandoned the draft as the Senate pressed for speed, because delay risked the offer itself. The treaty was signed in April 1803 for fifteen million dollars and roughly doubled the national territory in a single signature. The parties traded readings as they crossed. The Federalists who had preached broad construction discovered strictness, and Jefferson, who had built a career on strictness, signed anyway. The flag went up at New Orleans in December 1803 over a territory of some fifty thousand people, many of them enslaved, governed by appointment from Washington."),
    (4, "What did Jefferson's instructions order the Corps of Discovery to seek, and how were the Native nations described in them?",
     "Jefferson's instructions to Lewis of June 1803 named the objects plainly. The Corps was to find a water communication across the continent for commerce, to gain knowledge of the country and its peoples, and to establish relations with the Native nations whose land it all was. The president wrote of those nations as sovereigns to be treated with, in the same years his government measured their country for sale. The Corps of Discovery left St. Louis in May 1804, some forty men, soldiers and interpreters and Clark's enslaved man York among them, ascending the Missouri against the current. Its journals were kept as an instrument of the errand, every river named, every nation counted, every plant and animal described for a government that meant to use the record."),
    (4, "How did Sacagawea and York each change what the expedition could do, and how was their service answered?",
     "The Corps hired the trader Toussaint Charbonneau largely because his young wife Sacagawea, a Shoshone woman taken captive by the Hidatsa as a girl, could interpret, and because a party traveling with a woman and an infant read to the nations it met as a party of peace rather than war. In August 1805, interpreting at the meeting with the Shoshone, Sacagawea recognized the chief Cameahwait as her brother, and the expedition's horses and its passage west were obtained in the space of that recognition. York hunted, scouted, and labored through the whole crossing, and at the vote on the winter camp at Fort Clatsop both York and Sacagawea voted, a ballot the journals record without comment in a nation where neither could vote. On the return York asked Clark for his freedom and was refused for years."),
    (4, "Why does the lesson read the expedition as a survey of other peoples' countries, and what does the Treaty of Greenville show about the decade before it?",
     "The river country was inhabited country. The Mandan and Hidatsa villages where the Corps wintered in 1804 and 1805 were towns larger than St. Louis, farmers and traders whose hospitality the expedition's survival depended on, and the Teton Sioux confrontation on the river showed diplomacy running at the edge of violence. Behind the whole story stood the treaty system. By the Treaty of Greenville of 1795, the Western Confederacy, defeated at Fallen Timbers, ceded most of present Ohio, and that instrument, purchase and pressure and cession lines, was how the United States had been taking the West for a decade before the Corps set out. The expedition therefore reads as a survey of other peoples' countries by a republic that had already decided what the survey was for, and its maps redrew the continent's geography for the government that had bought a claim on paper."),
    (5, "What grievances made the war party's case, and why did the embargo fail as a peaceful weapon?",
     "Britain ruled the seas and France the continent, American ships were seized by both sides, and the Royal Navy practiced impressment, stopping American vessels and carrying off seamen it claimed as British subjects, some of them American citizens, thousands taken across the years. Jefferson's answer was the Embargo Act of 1807, closing every American port in the hope of starving Britain and France into respecting neutral rights without a shot. The exports of the United States collapsed by four fifths, New England's harbors sat idle while its smugglers worked, and the law was enforced with a coercion at home that sat strangely on a republic of limited government. The embargo was repealed in 1809 with the grievances untouched, and its failure is the ground the war argument of 1812 stands on."),
    (5, "How did the West's war join the maritime grievances in the declaration of 1812?",
     "Settlers pressed into Indiana and Ohio against treaties the Native nations read as frauds. Tecumseh built a confederacy on the claim that no single nation could sell land held by all in common, while his brother Tenskwatawa, the Prophet, preached renewal at Prophetstown. Governor William Henry Harrison marched on the town in Tecumseh's absence and fought the Battle of Tippecanoe in November 1811, after which the confederacy turned openly to the British in Canada. In Congress the War Hawks, young congressmen led by Henry Clay of Kentucky and John C. Calhoun of South Carolina, argued that Canada could be taken by marching and that national honor was itself a cause. Madison's war message of June 1, 1812 laid impressment, the Orders in Council, and the blockades before Congress, and the vote was the closest war vote in the nation's history, every Federalist and the commercial Northeast against."),
    (5, "What did the Treaty of Ghent settle, and why did the timing of Hartford and New Orleans ruin the Federalists?",
     "The war's invasions of Canada failed year after year, York was burned and Washington was burned in answer, and the fighting at sea and on the lakes went better than the fighting on land. New England's Federalists met at Hartford through December 1814, where the moderates carried amendments instead of secession, and the convention's report traveled south at exactly the wrong moment. The Treaty of Ghent, signed December 24, 1814, restored the boundaries of 1811 and said nothing about impressment or neutral rights, because Napoleon was beaten and the grievances had died with his wars. Andrew Jackson, not knowing of the peace, destroyed a British army below New Orleans on January 8, 1815. Peace and victory arriving together destroyed the Hartford report's authors, and the Federalist Party never recovered its standing."),
    (6, "What did the nationalist program of 1816 enact, and what did Clay's American System add to it?",
     "The war had taught that a government without a bank, a tariff, or roads had nearly lost a winnable war. In 1816 President Madison, a Republican, signed the charter of the Second Bank of the United States for twenty years and the Tariff of 1816, the first tariff laid avowedly for protection, enacting a generation late the program Hamilton had built. Henry Clay's American System stated the program in full. A national bank would give the currency order. A protective tariff would shelter manufactures until they could stand, and its revenue would be spent on internal improvements, roads and canals binding the sections into one market, the West's food feeding the East's mill towns and the South's cotton clothing both, each section prospering by the others' demand, an economic union offered as the answer to the political union's fragility."),
    (6, "How did the presidential vetoes and the Erie Canal together show the constitutional brake on internal improvements?",
     "Madison vetoed the Bonus Bill on his last day in office in 1817, holding that the power to build roads and canals was nowhere granted to Congress and would require a constitutional amendment, for all his agreement that the roads were needed. Monroe vetoed in the same line in 1822. The brake came from the program's own friends, and it held at the federal level for the whole era. The states built what the federal government would not. New York broke ground on the Erie Canal in 1817 with the state treasury's money, and the era's greatest internal improvement arrived by state action while the constitutional argument stood unresolved. The lesson's point is the split itself, a nation agreed on the need and divided on which government the Constitution allowed to meet it."),
    (6, "What did the Panic of 1819 teach westerners, and how did McCulloch and Gibbons widen the national government's reach?",
     "Land had been bought on credit at prices the cotton boom floated, and in 1819 the Second Bank under new management called in loans to save itself. State banks failed, western farms were foreclosed by the national bank its debtors now cursed, and a generation of westerners learned to hear the word bank as an enemy's name. In the same years the Marshall Court built the nationalist reading into law. McCulloch v. Maryland in 1819 struck down Maryland's tax on the Bank's Baltimore branch, held the Bank constitutional under powers implied from the great ends of the document, and ruled that the power to tax involves the power to destroy. Gibbons v. Ogden in 1824 read commerce among the states to include navigation and intercourse, not traffic alone, and struck down a state steamboat monopoly on New York's waters."),
    (7, "Why did John Quincy Adams argue that the United States should declare its principles alone rather than jointly with Britain?",
     "Spain's American empire was dissolving in revolution, the United States recognized the new republics in 1822, the Adams-Onís Treaty of 1819 had already taken Florida and drawn a line of claims to the Pacific, and Russia's ukase of 1821 claimed the Pacific coast down to the 51st parallel. Britain, whose trade wanted the new republics open and the old empires shut out, proposed through Foreign Secretary Canning a joint declaration with the United States. Adams argued in cabinet that his country should declare its principles itself rather than come in, in his phrase, as a cockboat in the wake of the British man of war. Monroe took the advice, and the declaration went out in the president's annual message of December 2, 1823 as an American statement, not a British partnership."),
    (7, "State the Monroe Doctrine's declarations, and state honestly what weight the declaration carried in 1823.",
     "Monroe declared that the American continents, by the free and independent condition they had assumed and maintain, were no longer subjects for future colonization by any European power. He declared that any attempt by the European powers to extend their system to any portion of this hemisphere would be viewed as dangerous to the peace and safety of the United States. In the other direction, he declared that the United States would not interfere with Europe's existing colonies or with its internal concerns. The weight in 1823 was smaller than the words. The United States could not have enforced the declaration alone, and it floated on the British navy, whose interest ran the same way. It endured because later generations kept choosing to stand on it."),
    (7, "State the Missouri Compromise in its three parts, and give the warning Jefferson sent with it.",
     "Missouri applied for statehood in 1819 as a slave state with the Senate balanced at eleven free and eleven slave, and Representative Tallmadge's amendment barring more enslaved people from Missouri and freeing those born there at twenty five passed the House on sectional lines and died in the Senate. The settlement of 1820 had three parts. Maine entered as a free state. Missouri entered as a slave state, its constitution's bar on free Black citizens noted and fudged rather than settled. Thomas's amendment drew the line of thirty-six thirty across the Louisiana Purchase lands, slavery barred north of it and permitted south, and the line held for a generation because it gave both sections a map they could stop arguing over. Jefferson, writing to John Holmes from Monticello in April 1820, called the question a fire bell in the night and the knell of the Union, a geographical line coinciding with a marked principle, moral and political, that once conceived would never be obliterated."),
    (8, "Why did Texas stand outside the Union for nine years, and how did annexation finally arrive in 1845?",
     "American settlers invited into Mexican Texas in the 1820s increasingly ignored the conditions Mexico had set, slavery among them, and Texas revolted in 1836 and won its independence at San Jacinto. The Republic of Texas then stood outside the Union for nine years, recognized and courted by Britain and France, and unadmitted because every president from Jackson to Tyler could count. A Texas admitted was a slave state admitted, and the Senate's balance and the northern House stood in the way. Annexation arrived in 1845 by joint resolution, a simple majority of both houses doing what a treaty needing two thirds of the Senate could not, in the last days of Tyler's presidency and with Polk elected on expansion. The method is part of the lesson, because it showed how a determined majority could widen the Union around the Constitution's treaty gate."),
    (8, "How did Polk's handling of Oregon differ from his handling of Mexico, and what did his war message claim?",
     "The Oregon Country had been jointly occupied with Britain since 1818, and American expansionists campaigned on the cry of fifty-four forty or fight. Polk, with a war opening against Mexico, settled Oregon at the 49th parallel by treaty in 1846, halving his claim against Britain while taking half of Mexico by war, and the difference between the two negotiations is part of the lesson. Against Mexico, Polk ordered American troops into the ground between the Nueces and the Rio Grande that both nations claimed, and after the Thornton affair's bloodshed on the Rio Grande in April 1846 his message told Congress that Mexico had shed American blood on American soil. A young congressman named Abraham Lincoln answered later with his spot resolutions, demanding that the president name the exact spot where the blood had been shed."),
    (8, "What did the Treaty of Guadalupe Hidalgo settle, and what question did the Wilmot Proviso leave standing?",
     "The Treaty of Guadalupe Hidalgo of February 2, 1848 confirmed the Rio Grande as Texas's boundary and transferred California, New Mexico, and the country between to the United States for fifteen million dollars and the assumption of claims, some five hundred thousand square miles added in a signature. The war behind it had been won in every campaign, by Taylor in the north, Scott from Veracruz to Mexico City, and Kearny and Frémont in New Mexico and California. David Wilmot's amendment of 1846, offered while the war still ran, would have barred slavery in any territory taken from Mexico. It passed the House again and again on sectional votes and died in the Senate every time. The question the Missouri line had answered for the Louisiana lands therefore stood unanswered for the Mexican cession, and the unit closes with it standing alone on the table of the enlarged house."),
]

FRAME = [
    "The unit opens in 1789 with a government on paper. The Constitution named offices and powers, and Washington's first administration had to invent the machinery, a cabinet the document nowhere creates, federal courts, a funded debt, a national bank, and precedents set by everything done for the first time. Hamilton's program made the federal government real and manufactured its opposition in the same motion, Jefferson and Madison reading the Constitution strictly against his broad construction, until the argument left the cabinet and became the first parties. Washington enforced the excise on the Pennsylvania frontier with a militia army and retired in 1796 warning against the spirit of party and permanent foreign alliances. His successors tested the settlement at once. The Federalists of 1798, frightened by France and by immigrant voters, jailed their critics under the Sedition Act, and the answer came from the states in the Virginia and Kentucky Resolutions and then from the voters, who deadlocked the election of 1800 in the House and still transferred power by ballot, the first ruling party in the new republic surrendering the government to its opponents without a soldier in the street.",
    "Jefferson governed as a strict constructionist who doubled the nation. He shrank the government Hamilton had built, pardoned the Sedition Act's prisoners, and paid down the debt, and in the same season he faced Marshall's Court claiming judicial review in Marbury while surrendering the case in front of it, and Napoleon's offer of the whole of Louisiana, which his principles gave him no power to accept and his judgment would not let him refuse. The purchase sent the Corps of Discovery up the Missouri into country that was not empty, Mandan and Hidatsa towns larger than St. Louis, Shoshone horse country, Nez Perce guides, and a ballot at Fort Clatsop where Sacagawea and York both voted in a nation where neither could. The republic that came home from that crossing went to war with Britain in 1812 over impressment, honor, and Canada, fought it divided, and settled it at Ghent with the boundaries of 1811 restored and every stated cause left off the paper, while the war broke the Native confederacies of the West, ruined the Federalist Party, and taught the nationalist generation of 1816 to build the bank, the tariff, and the roads the war had shown wanting.",
    "The settlements of the 1820s declared more than the republic could yet enforce. Clay's American System bound the sections into one market on paper, Madison and Monroe vetoed its roads on constitutional grounds, the Panic of 1819 taught the West to hate the bank that saved itself by ruining its debtors, and the Marshall Court read the Constitution as a frame meant to endure, implied powers in McCulloch and a commerce of intercourse in Gibbons. In December 1823 Monroe declared the hemisphere closed to future European colonization, a declaration that floated on the British navy. Three years earlier the Missouri crisis had drawn the line of thirty-six thirty across the Louisiana lands, Maine against Missouri, slavery barred north of it, and Jefferson heard in the question a fire bell in the night and the knell of the Union. The 1840s closed the unit where the line could not follow. Texas came in by joint resolution, Oregon was halved by treaty, Mexico was beaten in every campaign and ceded half its territory at Guadalupe Hidalgo for fifteen million dollars, and the Wilmot Proviso, barring slavery from the cession, passed the House and died in the Senate until the question every settlement since 1787 had deferred stood alone, unanswered, on the table of the enlarged house.",
]

BLUEPRINT_STUDENT = [
    "Explain Hamilton's financial program in its four parts, funding the debt at full value, assuming the states' war debts, chartering the Bank of the United States, and laying the excise, and explain how the argument over the program produced the first parties.",
    "Explain Washington's precedents, neutrality in Europe's war, the enforcement of federal law against the Whiskey Rebellion, and the Farewell Address warnings against parties and permanent alliances.",
    "Explain how the XYZ Affair and the war scare of 1798 produced the Alien and Sedition Acts, what the Sedition Act made a crime, and how its prosecutions fell on Republican editors and a congressman.",
    "Explain how the election of 1800 deadlocked in the House of Representatives, how the transfer of power was secured without violence, and what the Twelfth Amendment changed.",
    "Explain Jefferson's program of smaller government, and explain how the Louisiana Purchase doubled the nation's territory while testing the strict construction he had built his career on.",
    "Explain how Marbury v. Madison arose from Adams's midnight judges, and how Chief Justice Marshall claimed judicial review for the Court while surrendering the case in front of it.",
    "Explain the Corps of Discovery's journey of 1804 to 1806, the orders Jefferson gave it, the country it crossed, and what its journals and maps did for the government that sent it.",
    "Explain the parts played by Native nations, by Sacagawea, and by York in the expedition, including the vote at Fort Clatsop and York's refused petition for freedom.",
    "Explain the road to the War of 1812, impressment, the failure of the embargo, the War Hawks in Congress, and Tecumseh's confederacy and the Battle of Tippecanoe in the West.",
    "Explain how the War of 1812 was fought and settled, the failed invasions of Canada, the terms of the Treaty of Ghent, the Hartford Convention's timing, and the Battle of New Orleans.",
    "Explain the American System, the Second Bank, the protective tariff, and internal improvements, and explain the constitutional vetoes that limited what the federal government would build.",
    "Explain the Marshall Court's nationalism in McCulloch v. Maryland and Gibbons v. Ogden, implied powers, the power to tax as the power to destroy, and commerce read to include navigation.",
    "Explain the Monroe Doctrine's declarations of December 2, 1823, the hemisphere closed to future colonization and European interference viewed as dangerous, and what the United States could and could not enforce in 1823.",
    "Explain the Missouri Compromise in its three parts, Maine free and Missouri slave and the line of thirty-six thirty, the Tallmadge Amendment crisis that forced it, and Jefferson's fire bell warning.",
    "Explain Manifest Destiny and the war with Mexico, the annexation of Texas, the division of Oregon at the 49th parallel, the war of 1846 to 1848, the cession at Guadalupe Hidalgo, and the question the Wilmot Proviso left open.",
]

CSS = """
@page { size: letter; margin: 0.55in 0.75in 0.7in; }
* { box-sizing: border-box; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 11.5pt; color: #000; line-height: 1.35; margin: 0; }
.nameline { display: flex; justify-content: space-between; gap: 1em; }
h1 { font-size: 19pt; margin: 12pt 0 4pt; line-height: 1.2; }
h2 { font-size: 14.5pt; margin: 16pt 0 6pt; }
h3 { font-size: 12.5pt; margin: 14pt 0 4pt; break-after: avoid; }
p { margin: 0 0 7pt; }
.directions { margin-bottom: 4pt; }
.q { margin: 8pt 0 0; }
.qa { break-inside: avoid; }
.sp-a { height: 0.62in; }
table.terms { border-collapse: collapse; width: 100%; margin: 4pt 0 10pt; }
table.terms th, table.terms td { border: 1px solid #000; padding: 5pt 6pt; text-align: left; font-size: 11pt; vertical-align: top; }
table.terms td.row { height: 0.52in; }
table.terms td.filled { font-size: 10.5pt; line-height: 1.3; }
.arguments { break-before: page; }
.arguments h2:first-child { margin-top: 0; }
.key { break-before: page; }
.key h2:first-child { margin-top: 0; }
.brandmark { margin: 0 0 4pt; line-height: 0; } .brandmark img { width: 1.35in; }
"""

def main():
    terms = parse_terms()
    total = sum(len(v) for v in terms.values())
    assert total == 56, f"expected 56 terms, parsed {total}"
    P = []
    P.append("<!DOCTYPE html>")
    P.append('<html lang="en"><head><meta charset="utf-8">')
    P.append("<title>Study Guide: The Early Republic and Expansion</title>")
    P.append(f"<style>{CSS}</style></head><body>")
    P.append('<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>')
    P.append('<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>')
    P.append("<h1>Study Guide: The Early Republic and Expansion</h1>")
    P.append('<p class="directions"><strong>Directions:</strong> Complete Part 1 from your guided notes and readings, then answer the Part 2 questions in your own words. Part 3 tells the unit as one story and lists what the test will ask you to show. The unit test is built from this guide. Bring questions about anything you cannot answer to the review day.</p>')
    P.append("<p><strong>Unit question:</strong> How did the United States turn its Constitution into a working government, and what did continental expansion do to the republic that government served?</p>")
    P.append("<h2>Part 1: Key Terms</h2>")
    P.append("<p>Write the definition of each term in your own notebook wording, then check it against your guided notes.</p>")
    for n in range(1, 9):
        P.append(f"<h3>Lesson {n}: {LESSON_TITLES[n]}</h3>")
        P.append('<table class="terms">')
        for term, _ in terms[n]:
            P.append(f'<tr><td style="width:30%">{term}</td><td class="row"></td></tr>')
        P.append("</table>")
    P.append("<h2>Part 2: Review Questions</h2>")
    for i, (_, q, _) in enumerate(QUESTIONS, 1):
        P.append(f'<div class="qa"><p class="q"><strong>{i}.</strong> {q}</p><div class="sp-a"></div></div>')
    P.append('<div class="arguments"><h2>Part 3: The Unit as a Whole</h2>')
    for body in FRAME:
        P.append(f"<p>{body}</p>")
    P.append("<h3>The Unit Blueprint in Student Language</h3>")
    P.append("<p>The test is built to ask whether you can do these fifteen things. If you can do each one with evidence, you are ready.</p>")
    for i, item in enumerate(BLUEPRINT_STUDENT, 1):
        P.append(f"<p><strong>{i}.</strong> {item}</p>")
    P.append("</div>")
    P.append('<div class="key"><h2>Teacher Answer Key</h2>')
    P.append("<h3>Part 1: Key Terms</h3>")
    for n in range(1, 9):
        P.append(f"<h3>Lesson {n}: {LESSON_TITLES[n]}</h3>")
        P.append('<table class="terms">')
        for term, dfn in terms[n]:
            P.append(f'<tr><td style="width:30%">{term}</td><td class="filled">{dfn}</td></tr>')
        P.append("</table>")
    P.append("<h3>Part 2: Review Questions</h3>")
    for i, (_, q, a) in enumerate(QUESTIONS, 1):
        P.append(f"<p><strong>{i}. {q}</strong> {a}</p>")
    P.append("</div></body></html>")
    out = os.path.join(UNIT, "review", "review-study-guide.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write("\n".join(P))
    print(f"wrote {out}: {total} terms, {len(QUESTIONS)} questions")

if __name__ == "__main__":
    main()
