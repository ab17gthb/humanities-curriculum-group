#!/usr/bin/env python3
"""Build the Colonial America review study guide from the verbatim
vocabulary in build-scripts/unit-spec.md, plus 24 review questions with a
full key, a short frame passage, and the fifteen entries of the unit
blueprint restated in student language. Mirrors the Civil Rights study
guide. The teacher key carries no blueprint tags."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
UNIT = os.path.dirname(HERE)
SPEC = open(os.path.join(HERE, "unit-spec.md")).read()

LESSON_TITLES = {
    1: "Two Worlds Before Contact", 2: "The Spanish and French Americas",
    3: "Jamestown and the Chesapeake", 4: "New England: Covenant and Community",
    5: "The Middle Colonies and the Atlantic Economy", 6: "Slavery and the Slave Trade",
    7: "Colonial Society: Religion, Family, and the Great Awakening", 8: "Empire and War: The French and Indian War",
}

def parse_terms():
    terms = {}
    current = None
    for line in SPEC.splitlines():
        m = re.match(r"### Lesson (\d)", line)
        if m:
            current = int(m.group(1)); terms[current] = []
            continue
        m = re.match(r"- ([^:]+): (.+)$", line)
        if m and current:
            terms[current].append((m.group(1).strip(), m.group(2).strip()))
    return terms

QUESTIONS = [
    (1, "What did the Americas look like in 1491, before Europeans arrived?",
     "The hemisphere held perhaps fifty million people or more, in scholarly estimates, in farming peoples and hunting peoples, cities and confederacies. Tenochtitlan stood on an island in Lake Texcoco, larger than London, with chinampas, markets, and causeways. Cahokia on the Mississippi had raised its mounds and plazas centuries before Columbus. In the northeast woodlands the Haudenosaunee league joined five nations under the Great Law to keep peace among themselves and deal jointly with outsiders, and farming villages, towns, and trade routes covered the Eastern Woodlands."),
    (1, "What did Europe bring to the meeting of 1492, in ships, skills, and motives?",
     "Europe was a continent of rival kingdoms. Spain had just been unified and had completed the Reconquista in January 1492, and Portugal was already pushing down Africa's coast in caravels. The equipment of expansion included the compass, the lateen sail, gunpowder weapons, and printing to spread the news. Columbus sailed for Ferdinand and Isabella claiming Caribbean islands for Spain while believing he had reached Asia's edge, and his 1493 letter was printed across Europe within months, advertising fertile land, gold, and peoples he described as timid and generous."),
    (1, "What moved in the Columbian Exchange, and why were diseases its deadliest cargo?",
     "Crops moved both ways, maize, potatoes, and tomatoes east and wheat, horses, and cattle west, along with animals, people, and ideas. European diseases moved west into populations with no resistance to them, smallpox first among them, killing on a scale no army could match. In many regions the loss over the following century reached nine people in ten, in estimates labeled as estimates. Empires and colonies were later built in a hemisphere whose peoples had already been shattered by disease, and Indigenous nations rebuilt, adapted, and resisted from inside that loss."),
    (2, "How did Spain conquer and organize its American empire?",
     "The conquistadores took empires with Indigenous allies who had their own quarrels with them and with smallpox doing work no sword could. Cortes took Tenochtitlan in 1521 and Pizarro took Peru, and Spain built New Spain on mines, missions, and great estates from Mexico to the silver mountain of Potosi. The encomienda stood at the base, granting a colonist the tribute and labor of Indigenous people in return for supposed protection and Christian teaching. The society it made was ranked, peninsulares, creoles, mestizos, Indigenous peoples, and enslaved Africans, and its silver flowed to Spain and onward to China."),
    (2, "What did Bartolome de las Casas put on the record, and what followed from his advocacy?",
     "Las Casas published A Brief Account of the Destruction of the Indies in 1552, putting the dying of Indigenous people under Spanish rule on the record in numbers his readers could not forget. His advocacy at court helped push the Crown toward the New Laws limiting the encomienda. It also helped push the Crown toward African enslavement as the labor answer for the colonies, a turn Las Casas himself came to regret. His record and his regret stand together in the lesson, because the empire's defenders and its sharpest critic argued inside the same system of coerced labor."),
    (2, "How did France hold an American empire, and where did slavery stand inside it?",
     "France planted itself on the St. Lawrence after 1608 as a thin line of settlers living by the fur trade. The trade made the French dependent on Indigenous hunters, guides, and allies, and bound them with diplomacy, intermarriage, and missions, while France fought the Haudenosaunee for two generations over the beaver country. The Dutch worked the same trade on the Hudson. France's other America stood in Louisiana and the sugar islands, where the Code Noir of 1685 wrote slavery into French law and Saint-Domingue's plantations ran on enslaved labor as brutally as any in the hemisphere."),
    (3, "Why did Jamestown nearly fail in its first years?",
     "The Virginia Company of London, a joint-stock company chartered in 1606, planted Jamestown in 1607 on a swampy James River peninsula chosen for defense against Spanish ships and bad for almost everything else. The settlers were heavy with gentlemen and light on farmers, the water was brackish, disease spread, and the supply system failed. In the starving time of 1609 and 1610 the colony of some five hundred ate horses and dogs and fell to about sixty survivors. Around it stood the Powhatan paramount chiefdom under Wahunsenacawh, whose corn trade kept the English alive while he weighed how to use or remove them."),
    (3, "How did tobacco remake Virginia, and what labor did the crop demand?",
     "John Rolfe planted a milder West Indian tobacco strain from about 1612, and the leaf found England's market. Tobacco became the colony's cash crop, and it wore out soil and men and made the colony hungry for land. The headright system granted fifty acres to any person who paid for an immigrant's passage, and indentured servants came by the thousands on terms of four to seven years, dying in seasoning fevers at rates the records keep. Land, labor, and the crop's demands set the pattern the Chesapeake kept for the rest of the century."),
    (3, "Why does the unit call 1619 a hinge year, and how did Bacon's Rebellion close the lesson?",
     "In 1619 the House of Burgesses met at Jamestown, the first elected assembly in English America, and weeks later a Dutch ship sold some twenty Africans to the colony, the beginning of African slavery in England's mainland colonies, whose first legal status there historians still argue over, as the lesson states. In 1676 Nathaniel Bacon led frontier settlers and former servants in an uprising that attacked Indigenous peoples and burned Jamestown. After it, Virginia's great planters shifted decisively toward enslaved African labor, harder to free, easier to mark, and bound for life."),
    (4, "What two foundings began New England, and what kind of community did each mean to build?",
     "Plymouth came first, in 1620, when Separatist Pilgrims crossed on the Mayflower and signed a compact aboard ship to govern themselves by consent, having landed outside their patent. Half of them died the first winter, and Tisquantum and the Wampanoag under Massasoit helped the rest survive. Massachusetts Bay followed from 1630, settled by Puritans building a Bible commonwealth, with John Winthrop's sermon A Modell of Christian Charitie and its city upon a hill preached as the fleet crossed. Both colonies built tight farming towns around a meetinghouse, with land spread broadly among families and schools ordered by law."),
    (4, "What did Roger Williams and Anne Hutchinson each challenge, and what happened to them?",
     "Roger Williams was banished in 1636 for teaching that the king could not grant Indigenous land he did not own and that the state could not compel worship, and he founded Rhode Island on soul liberty. Anne Hutchinson was tried in 1637 for holding that grace, not works or ministers, stood between a believer and God, and her trial examination survives as the colony's own record of its fear. She was banished to Rhode Island and killed in New Netherland in 1643. In a covenant community, dissent was treated as danger, and both cases show the colony defending its rule of belonging."),
    (4, "What did New England's wars and the Salem crisis show about the community by 1692?",
     "Connecticut's Fundamental Orders of 1639 set up government by the votes of freemen. Expansion brought war, the Pequot War of 1637 with the Mystic massacre, and a generation later King Philip's War of 1675 and 1676, when Metacom's coalition struck back at fifty years of land loss in the deadliest war per capita in the colonies' history. At Salem in 1692 a community built on watching for the devil found him in its own daughters' accusations. Nineteen people were hanged and one man was pressed to death before the colony's leaders called the trials home."),
    (5, "How did the middle colonies become the colonies of many peoples?",
     "The Dutch West India Company planted New Netherland for the fur trade, and New Amsterdam was a trading town of many languages before an English fleet took it in 1664 and renamed it New York. William Penn received Pennsylvania's charter in 1681 and advertised his holy experiment across Europe in German and Dutch, drawing Quakers, Germans, Scots-Irish, and Welsh to rich wheat land. He governed with an elected assembly and bought land from the Lenape under treaties he honored in his lifetime. By 1750 Philadelphia was the largest city in British America, and Delaware and Maryland stood beside the middle colonies with settlements of their own."),
    (5, "What did toleration promise in the middle colonies, and where did its limits show?",
     "Pennsylvania promised Quakers and other settlers room to worship under a proprietor of a persecuted faith, and Penn's frame of government rested on an elected assembly. The limits showed in the records around it. In 1657 English Quaker sympathizers at Flushing petitioned Governor Stuyvesant in the Flushing Remonstrance for the liberty he had denied them, claiming conscience against a proprietor's order. Maryland's Toleration Act of 1649 protected Christian worship and punished its disturbance in the same clauses, protecting one faith's practice while binding others. Toleration in this era was granted by rulers, and rulers set its edges."),
    (5, "How did mercantilism and the Navigation Acts work, and what grew up inside the rules?",
     "Mercantilism held that colonies existed to enrich the mother country, exporting raw materials, importing finished goods, and piling up bullion. The Navigation Acts from 1651 onward routed enumerated goods, tobacco and sugar first among them, through England in English or colonial ships, with customs houses to watch the trade. The acts invited smuggling, and a colonial carrying trade grew up inside the rules anyway, New England ships and middle colony grain feeding the sugar islands. The Atlantic worked as one economy, grain, fish, and timber moving south and east, sugar and molasses north, manufactured goods from Britain, and enslaved Africans from the Guinea coast."),
    (6, "How was the Atlantic slave trade organized, and what do its numbers rest on?",
     "European ships carried guns, cloth, and metal goods to Africa's Guinea coast, where African rulers and merchants sold war captives and the kidnapped to the traders, a fact the lesson states without letting it soften what the buyers built. The Trans-Atlantic Slave Trade Database puts the forced migration at some 12.5 million Africans carried aboard between the 1500s and the 1800s, of whom about 10.7 million survived the crossing, and the lesson states those figures as the database's estimates wherever they appear. Ships, forts, credit, insurance, and colonial law organized the trade as a system, not a series of accidents."),
    (6, "What does Equiano describe, and what did the law add to the trade in England's colonies?",
     "Olaudah Equiano, kidnapped in Igboland at about eleven and carried to Barbados and Virginia, described the Middle Passage in his Interesting Narrative of 1789 from inside the hold, its heat, filth, crowding, sickness, and the deaths of the crossing, in the first person. In England's colonies the law made the system permanent. Virginia's statutes of the 1660s made a child's status follow the mother's and declared that baptism did not free, rebuilding slavery as hereditary chattel property. Slave codes followed in colony after colony, defining enslaved people as property and denying them courts, assembly, and arms, and punishing resistance with death."),
    (6, "How did enslaved people resist, and what worlds did they build inside slavery?",
     "Resistance ran from day to day defiance, work slowed and tools broken, to flight toward swamps, Spanish Florida, and the woods. In the South Carolina and Georgia lowcountry, enslaved Africans' rice knowledge built the plantations' wealth, the task system ordered the day, a Black majority lived in something close to an African country, and the Gullah language and culture took form. At Stono in September 1739 enslaved men seized guns and marched for Florida's promised freedom, and South Carolina answered with the Negro Act of 1740. Phillis Wheatley, enslaved in Boston, published her poems in London in 1773, the first African American poet in print."),
    (7, "How did colonial assemblies gain power while Britain looked away?",
     "By the early 1700s every colony had an elected assembly voting its taxes and laws, while the governor was appointed from London or by a proprietor. Through the practice later called salutary neglect, Britain, busy with wars and politics in Europe, left the colonies largely to govern themselves, and the assemblies spent the decades quietly taking powers, above all the power of the purse, voting the money governors needed and attaching their terms to it. Colonists came to claim the rights of Englishmen as their birthright, and self-government in practice ran ahead of what Britain understood from across the Atlantic."),
    (7, "What did the Zenger trial establish, and what did it not do?",
     "John Peter Zenger, a New York printer, was jailed in 1734 for his newspaper's attacks on the royal governor and tried in 1735 for seditious libel. His lawyer Andrew Hamilton argued that true statements could not be libel, and the jury acquitted him against the judge's instruction. The verdict stands as the colonies' landmark for a free press, the claim that a printer could criticize a governor in print and answer for it before a jury of colonists. Stated honestly, it was a jury's act and not a change in the law, which is part of why the lesson keeps the qualification attached to the verdict."),
    (7, "What happened in the Great Awakening, and what did it teach beyond religion?",
     "In the 1730s and 1740s revival preaching swept the colonies. Jonathan Edwards at Northampton preached Sinners in the Hands of an Angry God at Enfield in 1741, and George Whitefield toured from Georgia to New England in 1739 and 1740 drawing open air crowds larger than any town's population. Itinerants challenged settled ministers, and congregations split into Old Lights and New Lights, while Baptists and Methodists multiplied in the South. The Awakening taught ordinary people to judge their betters' messages for themselves, and print and preaching made Whitefield one shared celebrity of thirteen colonies. Beside it the Enlightenment arrived through books, colleges, and men like Benjamin Franklin, prizing reason and observation, the two currents standing as rivals and partners."),
    (8, "Why did war come to the Ohio Valley, and how did its opening years go?",
     "By 1750 three peoples claimed the Ohio Valley at once, Virginia speculators and settlers moving west, France binding Canada to Louisiana with a chain of forts, and the Ohio nations, Delaware, Shawnee, and Mingo among them, playing the empires against each other to keep their country. George Washington, sent to order the French out in 1753, ambushed a French party in May 1754 and lost Fort Necessity that July. The Albany Congress that summer rejected Franklin's Plan of Union, whose Join, or Die snake had run in his Gazette that May. Braddock's army was destroyed on the Monongahela in 1755, and the frontier was raided for two years."),
    (8, "How did William Pitt turn the war, and what did the Treaty of Paris settle?",
     "William Pitt took the war's direction in 1757, paying for it with borrowed millions, promoting officers by merit, and sending Britain's regulars and navy to North America in force. Louisbourg and Quebec fell in 1758 and 1759, with Wolfe and Montcalm dying on the Plains of Abraham, and Montreal surrendered in 1760. The Treaty of Paris of February 1763 took France off the mainland. Britain received Canada and all French territory east of the Mississippi River except New Orleans, and Louisiana went to Spain. Colonial soldiers had served beside regulars and learned both British competence and British contempt."),
    (8, "What bills did the victory of 1763 present, and why does the unit close there?",
     "The war's bills arrived together. Britain's national debt had nearly doubled, and its ministers resolved that the colonies should pay for their own defense. The Ohio nations, shut out of the treaty's making, rose under Pontiac in the spring of 1763 and took fort after fort. London answered with the Proclamation of October 1763, drawing a line along the Appalachians and forbidding colonial settlement west of it, a line settlers were already crossing. In 1763 Britain and its colonies had never been stronger together, and every term of their partnership, money, land, and authority, was about to be renegotiated, which is where the next unit begins."),
]

FRAME = [
    "In 1491 the Americas were not empty land waiting for a history. They were a hemisphere of farmers and hunters, cities and leagues, trade routes and ceremonies, and Europe was a continent of rival kingdoms with new ships, new weapons, and old ambitions. When the two worlds met after 1492, the meeting remade both. Crops, animals, and peoples crossed the ocean in both directions, and disease crossed westward into peoples who had no resistance to it, killing on a scale that reshaped everything built afterward. Spain, France, and England each planted a different kind of America on ground that catastrophe had cleared and that Indigenous nations still contested, and every kind rested in the end on land taken and labor coerced.",
    "England's colonies grew into three regional societies with one Atlantic economy running through them. The Chesapeake lived on tobacco and moved from servant labor to enslaved labor. New England built covenant towns that watched their members closely and punished those who stepped outside the rule of belonging. The middle colonies held peoples of many nations and faiths under proprietors and assemblies. Grain, fish, timber, sugar, manufactured goods, and enslaved Africans moved around the Atlantic in a pattern the Navigation Acts tried to rule and could not contain. Inside the colonies, assemblies learned to govern, printers tested what could be said, and revival preachers and Enlightenment writers taught ordinary people, in different tongues, to judge authority for themselves.",
    "The French and Indian War tested the whole structure at once. Britain and France fought for the Ohio Valley and for North America, the Ohio nations fought to keep their country, and the colonies supplied men and money for a victory that took France off the mainland in 1763. The same year presented the victory's bills, a doubled national debt, an uprising under Pontiac in the west, and a royal line drawn along the mountains that settlers were already crossing. The unit ends at that hinge. Britain and its colonies had never been stronger together, and every term of their partnership was about to be argued over.",
]

BLUEPRINT_STUDENT = [
    "Describe the Indigenous cities, farming peoples, and leagues of the Americas before Europeans arrived, from Tenochtitlan and Cahokia to the Haudenosaunee.",
    "Explain what Columbus started, what the Columbian Exchange carried in each direction, and why disease killed so many of the Americas' peoples.",
    "Explain how Spain conquered and organized its American empire, through the encomienda, the missions, and the great estates, and who spoke against its cruelty and with what result.",
    "Explain how France and the Netherlands held on in North America through the fur trade and alliances with Indigenous nations, and where slavery stood in the French colonies.",
    "Explain why Jamestown nearly starved in its first years and how tobacco saved the colony and changed what it demanded.",
    "Explain how Virginia got its workers, first indentured servants and then enslaved Africans, and what Bacon's Rebellion had to do with the change.",
    "Explain why Plymouth and Massachusetts Bay were founded, and what kind of community New England's settlers meant to build.",
    "Explain how New England answered the people who disagreed with it, what happened at Salem in 1692, and how its wars with Indigenous nations went.",
    "Explain why the middle colonies held so many peoples and faiths, what William Penn tried in Pennsylvania, and where toleration stopped.",
    "Explain how mercantilism and the Navigation Acts were supposed to work, and how goods and people actually moved around the Atlantic.",
    "Explain how the Atlantic slave trade was organized, what the Middle Passage was like in Equiano's account, and how law made slavery pass from a mother to her children for life.",
    "Explain how slavery differed from place to place, what enslaved people built and kept alive, and how they resisted, including the rising at Stono in 1739.",
    "Explain how colonial assemblies gained power while Britain left the colonies largely alone, and what the Zenger trial showed about a free press.",
    "Explain what happened in the Great Awakening and what the Enlightenment added to it, and how both taught colonists to judge messages and authority for themselves.",
    "Explain how Britain won the French and Indian War, what the peace of 1763 gave it, and why Pontiac's rising and the Proclamation line followed in the same year.",
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
    P.append("<title>Study Guide: Colonial America</title>")
    P.append(f"<style>{CSS}</style></head><body>")
    P.append('<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>')
    P.append('<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>')
    P.append("<h1>Study Guide: Colonial America</h1>")
    P.append('<p class="directions"><strong>Directions:</strong> Complete Part 1 from your guided notes and readings, then answer the Part 2 questions in your own words. Part 3 tells the unit as one story and lists what the test will ask you to show. The unit test is built from this guide. Bring questions about anything you cannot answer to the review day.</p>')
    P.append("<p><strong>Unit question:</strong> How did the meeting of Europe, Africa, and the Americas remake all three worlds, and what kind of society grew up in England's colonies?</p>")
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
