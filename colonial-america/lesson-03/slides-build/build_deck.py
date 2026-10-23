#!/usr/bin/env python3
"""Colonial America Lesson 3 deck builder. Image led deck: Smith's 1612 map of Virginia as the title, the Powhatan detail and the van de Passe Pocahontas engraving, the de Bry and White town view, and the English arrival plate."""
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
 'joint-stock company': 'a business owned by investors who pool their money and share its costs, risks, and profits',
 'Jamestown': 'the first permanent English settlement in North America, founded in 1607 on the James River',
 'cash crop': 'a crop grown for sale and profit rather than for the grower\u2019s own use, as tobacco was in the Chesapeake',
 'headright system': 'fifty acres of land for any person who paid for an immigrant\u2019s passage to Virginia',
 'indentured servant': 'a laborer bound to work four to seven years for passage to America and freedom dues at the end',
 'House of Burgesses': 'the first elected assembly in English America, meeting at Jamestown in 1619',
 "Bacon's Rebellion": 'the Virginia uprising of 1676 led by Nathaniel Bacon, which burned Jamestown',
}

# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'COLONIAL AMERICA \u00b7 LESSON 3', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Jamestown and the Chesapeake', size=30, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'A company venture, a starving winter, a chief\u2019s corn, and the crop that remade a colony.', size=17, color=POWDER)
notes(s, "Open with the map. It is John Smith\u2019s map of Virginia, drawn from his surveys of the Chesapeake in 1608, engraved by William Hole, and first published in 1612, the most accurate map of the bay made in its century. Everything this lesson tells happened inside the country the map charts, and the map carries the lesson\u2019s first correction. The rivers are lined with the towns of the Powhatan peoples. Jamestown, founded in 1607, was a small English fort planted inside another ruler\u2019s country, and it survived its first years on that ruler\u2019s decisions. The lesson then follows the crop that ended the dependence. Tobacco made the colony pay, and tobacco demanded land and labor on terms that built the Chesapeake.")
# 2 QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did a starving outpost become a tobacco colony, and what did tobacco demand?', {})]], size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': RUST_LT, 'italic': True}), ('How did the meeting of Europe, Africa, and the Americas remake all three worlds, and what kind of society grew up in England\u2019s colonies?', {'italic': True})]], size=17, color=POWDER, font='Georgia', leading=1.2)
notes(s, "Read the lesson question aloud and separate its two halves, because the exit ticket and the writing task grade them separately. The first half is about survival and transformation: how a fort that nearly starved in the winter of 1609 and 1610 became, within a few years, a colony organized around one export crop. The second half is about consequences, and it is the harder half: what the crop demanded. Tobacco demanded fresh land as it wore out the soil, and that land belonged to the Powhatan peoples. It demanded labor in every season, and the search for that labor runs from indentured servants to the first Africans of 1619 to the decisive turn toward enslaved labor after 1676. Connect the question to the unit question beneath it. The society that grew up in the Chesapeake was built by those two demands.")
# 3 MAP
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'From a starving fort to a tobacco colony', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'A Company of Investors', 'The Virginia Company, its charter, and its ships'),
        ('B', 'A Peninsula, and the Starving Time', 'A bad site, and the winter of 1609 and 1610'),
        ('C', 'The Powhatan Paramount Chiefdom', 'Wahunsenacawh weighs how to handle the English'),
        ('D', 'John Smith and His Two Stories', 'The 1608 account, and the rescue that appears later'),
        ('E', 'Tobacco Remakes the Colony', 'Rolfe\u2019s crop, and its hunger for land and labor'),
        ('F', '1619: An Assembly and a Ship', 'The House of Burgesses, and the first Africans'),
        ('G', 'Land, Labor, and Rebellion', 'Headrights, servants, and Bacon\u2019s Rebellion')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This map follows the guided notes section by section. Sections A and B tell the founding as a business failure nearly completed: a joint-stock company\u2019s fort, planted for defense on a sickly peninsula, reduced by the starving time from some five hundred people to about sixty. Section C restores the other government in the story, Wahunsenacawh\u2019s paramount chiefdom, whose corn and whose diplomacy kept the fort alive. Section D slows down on the evidence itself, because the most famous story of these years, the rescue of John Smith, changes across Smith\u2019s own books. Sections E and F tell the transformation and its hinge year, 1619. Section G follows the labor system to its crisis in Bacon\u2019s Rebellion and the planters\u2019 turn afterward. Tell students to track one question through every section: who paid the cost of each stage, and in what coin?")
# 4 DIVIDER A
divider_text('Section A', 'A Company of Investors', 'London, 1606: merchants pool their money, share the risk, and charter a colony as a business.',
 "Teach the founding as a financial instrument before it is an adventure, because the instrument explains the colony\u2019s later choices. Spain\u2019s kings had paid for empire out of royal treasuries. England\u2019s Virginia Company of London was a joint-stock company, chartered by King James I in 1606. Investors bought shares, pooled their money, and shared the costs, the risk of losing everything, and any profit. That structure set the colony\u2019s clock. Investors who had risked money expected a return, and a colony that produced no return would lose its supply ships. The orders given the first fleet show the expectation plainly: find gold, find a passage to the Pacific, and find the Roanoke colonists lost twenty years before. Three ships carrying 144 men and boys sailed in December 1606 to execute a business plan on a shore none of the investors had seen.")
# 5 CONTENT A
content_text('Shares, risk, and three ships', ['The Virginia Company of London, chartered 1606', 'Investors pool money and share costs, risks, profits', 'Orders: gold, a Pacific passage, the lost Roanoke colony', 'Three ships, 144 men and boys, December 1606'],
 "Carry both definitions exactly as the guided notes print them. A joint-stock company is this: " + "joint-stock company: " + TD['joint-stock company'] + ". Jamestown is this: " + "Jamestown: " + TD['Jamestown'] + ". Then make the class sit with the passenger list\u2019s shape, because the reading insists on it. The company of settlers held many gentlemen unaccustomed to labor and few farmers, carpenters, and fishermen in proportion to the work waiting. The venture had been stocked, in part, for the quick strike its investors imagined, gold and a passage west, rather than for the slow work of feeding a town through a winter. When students ask later why the colony starved with a river full of fish beside it, this slide is part of the answer. The plan, the site, and the company of men were all fitted to a colony that existed first on paper in London.")
# 6 DIVIDER B
divider_photo('arrival-port.jpg', 'Section B', 'A Peninsula, and the Starving Time', ['May 1607: a fort chosen against Spanish ships, on brackish water, in another ruler\u2019s country.'],
 "The plate on this slide is Theodor de Bry\u2019s engraving of the English arrival in Virginia, made after John White\u2019s drawings and published in 1590, a generation before Jamestown, for Raleigh\u2019s Roanoke voyages. Use it to fix the geography before the disaster. The settlers of 1607 built their fort on a low peninsula in the James River, far enough upriver to spot Spanish ships and near enough to deep water to moor their own. The same site gave them brackish drinking water, swamp air and disease, and soil and hunting grounds already used by the Paspahegh people, whose town stood nearby. Defense they had considered. Water, food, and neighbors they had not, or not enough. The section\u2019s subject is what those choices cost in the colony\u2019s third winter, and the numbers on the next slides should be taught without softening.")
# 7 CONTENT B
content_text('The winter of 1609 and 1610', ['A site defensible against ships, poor for living', 'Brackish water, disease, few farmers among gentlemen', 'Trade and supply fail together', 'The starving time: winter 1609 and 1610', 'The survivors prepare to abandon Jamestown'],
 "Teach the starving time from the colony\u2019s own accounts, at documentary weight. By the autumn of 1609 some five hundred colonists were in Virginia, swollen by a supply fleet whose flagship had wrecked on Bermuda. Through that winter the Powhatan trade that had fed the town was cut off, the settlers were penned inside their fort, and the accounts record what followed without flinching: horses, dogs, and rats eaten, and in documented cases the dead. In June 1610 the roughly sixty survivors boarded ships to abandon Jamestown altogether and met a relief fleet coming up the river, which turned them back. Precision is the point here, because legend prefers a rescue story. What saved Jamestown in 1610 was not a hero. It was a supply fleet that arrived days after the colony had given itself up.")
# 8 STAT B
stat('about 60', 'survivors of the starving time, spring 1610', 'Of some five hundred colonists in the autumn of 1609, after a winter the colony\u2019s accounts record in full',
 "Stop on this number and make the class price it. A loss of nearly nine colonists in ten, in a single winter, in a settlement that had been reinforced that same year. The causes stack, and students should be able to stack them: a site chosen for defense with brackish water, a company of settlers short of farmers and laborers, a supply system broken by wreck and distance, and a trade lifeline with the Powhatan chiefdom cut at the moment of greatest need. Hold the number against the founding slide. The investors of 1606 had bought shares in a venture that by 1610 had consumed most of the people sent to run it. The colony\u2019s continuation was a decision made in London to spend more, and in Virginia a fleet\u2019s arrival, not a recovery the survivors had achieved on their own.")
# 9 DIVIDER C
divider_photo('secotan-port.jpg', 'Section C', 'The Powhatan Paramount Chiefdom', ['Some thirty peoples under Wahunsenacawh, farming towns along the rivers of Tsenacommacah.'],
 "The plate on this slide is Theodor de Bry\u2019s engraving of a Virginia town, made after John White\u2019s watercolor and published with Thomas Hariot\u2019s report of 1590. It shows the kind of settled farming country the English entered in 1607: houses in order, fields under cultivation, ceremony and work in their places. Teach this section as the restoration of the story\u2019s second government. The Powhatan paramount chiefdom joined some thirty peoples of the Chesapeake under Wahunsenacawh, the leader the English called Powhatan, who had built his power by inheritance and conquest and ruled from Werowocomoco, on the York River. His people farmed corn, beans, and squash, hunted and fished, and traded across the bay. The English were a few hundred hungry strangers in his country, and everything that follows in this section is his statecraft toward them.")
# 10 CONTENT C
content_photo('powhatan-port.jpg', 'A chief weighs the English', ['Corn traded, and corn withheld, as policy', 'English strength tested season by season', 'Tools and copper valued; Smith kept alive to make them', 'Use them against his enemies, or drive them out'],
 "The detail on this slide comes from Smith\u2019s own map: Wahunsenacawh in state at Werowocomoco, as Smith was brought before him in the winter of 1607 and 1608. Read the meeting as diplomacy from the chief\u2019s side. He feasted his prisoner, promised him liberty within four days, promised corn and venison for the colony, and asked in return that the English make him hatchets and copper. He wanted English metal goods and, possibly, English guns and numbers against his enemies. He also withheld corn when withholding served him, and the colony\u2019s hunger rose and fell with his decisions. State the section\u2019s judgment plainly, because the documents support it: Jamestown survived its first years because Wahunsenacawh allowed it to, while he weighed whether the strangers were worth more as clients than as a memory.")
# 11 DIVIDER D
divider_photo('pocahontas-port.jpg', 'Section D', 'John Smith and His Two Stories', ['The portrait is Pocahontas in London in 1616, the year the rescue first enters Smith\u2019s writing.'],
 "The engraving on this slide is Simon van de Passe\u2019s portrait of Pocahontas, made in London in 1616, the only portrait of her from her lifetime. She had come to England as Rebecca Rolfe, wife of John Rolfe, and the Virginia Company presented her as proof that colonization and conversion worked. That same year Smith wrote his letter to Queen Anne introducing her at court, and in that letter, written to win royal favor for Pocahontas and for the company, the rescue story appears in his writing for the first time, eight years after the meeting it describes. Set the section\u2019s rule before the texts. Smith is taught in this lesson as a source with an author selling himself, and the class will read his two tellings of the same winter side by side and decide what the difference between them is evidence of.")
# 12 CONTENT D
content_photo('pocahontas-port.jpg', '1608 against 1624', ['1608, A True Relation: a feast, a bargain, a friendly release', 'No rescue in the first account', '1616, letter to Queen Anne: the rescue first appears', '1624, General History: the rescue in full, on the stones', 'A ritual misunderstood, or a story improved'],
 "Work the comparison slowly, because it is the lesson\u2019s exercise in reading a source against itself. In the General History of 1624 Smith tells the scene in full: two great stones brought before Powhatan, his head laid on them, clubs raised, and Pocahontas laying her own head on his to save him. In A True Relation of 1608, published within months of the meeting, the same visit ends with a feast, promises of corn, and a friendly send home, and Pocahontas does not appear in it at all. Between the two stand the letter of 1616, written for a queen, in a year when the company was displaying Pocahontas in London. Historians cannot settle whether Smith survived a ritual of adoption he misunderstood or improved his story as his audience grew. Students can settle the method: the later and more useful a story is to its teller, the harder it must be checked.")
# 13 STAT D
stat('1608', 'the account with no rescue in it', 'The rescue first appears in Smith\u2019s writing in 1616 and in full in 1624, sixteen years after the meeting',
 "Use this slide to fix the chronology in memory, because the whole argument of section D is three dates. Sixteen oh eight: the meeting, and the account written within months, feast and release, no rescue. Sixteen sixteen: the letter to Queen Anne, presenting Pocahontas at court, first written mention of her saving his life. Sixteen twenty-four: the General History, the full scene, stones, clubs, and the princess\u2019s head laid on his. Then ask the corroboration question the bank record asks: what other kinds of evidence could test the scene, records from the Powhatan side, or other colonists\u2019 accounts of the same weeks? There are none for this meeting, which is itself a finding. A claim resting on one author, told three ways across sixteen years, must be carried in the mind at exactly that weight, no more and no less.")
# 14 DIVIDER E
divider_text('Section E', 'Tobacco Remakes the Colony', 'From about 1612 one leaf gives the company its profit, and the colony its marching orders.',
 "Introduce tobacco as the answer to the investors\u2019 question, and keep the economics in front of the romance. For five years the colony had consumed money and people and returned nothing London could sell. John Rolfe\u2019s experiments with a milder West Indian strain of tobacco, planted from about 1612, produced a leaf English smokers wanted in quantity. The Spanish had supplied that market from their colonies. Now Virginia could supply it, and the company finally had its commodity. Teach the turn in the colony\u2019s purposes that followed. A settlement planted to find gold and a passage west became a plantation colony organized around a single crop, and every institution of Chesapeake life, its land hunger, its labor systems, its spread along the rivers, and its wars for ground, descends from that reorganization.")
# 15 CONTENT E
content_text('One leaf, two hungers', ['Rolfe plants a West Indian strain, from about 1612', 'England\u2019s market takes all Virginia can ship', 'Tobacco exhausts the soil within a few years', 'Settlement spreads along the rivers onto Powhatan land', 'Hands demanded at every stage, in every season'],
 "Carry the definition exactly. A cash crop is this: " + "cash crop: " + TD['cash crop'] + ". Then work the two hungers as mechanisms, not slogans. The soil hunger: tobacco stripped a field\u2019s fertility within a few years, so a planter needed several times the land he cropped in any year, fresh ground resting in reserve, and the colony\u2019s footprint spread along every navigable river onto land the Powhatan peoples farmed and hunted. The labor hunger: tobacco needed hands at setting, topping, weeding, cutting, hanging, and packing, across the whole year, in numbers no company of gentlemen could supply. Land and labor together are the crop\u2019s real product in this lesson. The leaf paid London. These two demands built Virginia, and the next two sections take them in order, the political year first.")
# 16 DIVIDER F
divider_text('Section F', '1619: An Assembly and a Ship', 'One summer joins the first elected assembly in English America and the first Africans in its mainland colonies.',
 "Frame 1619 as the hinge year of the colony\u2019s history, and insist on the joining, because students will meet the two events in separate textbooks if the lesson does not bind them. In the summer of 1619 the reformed Virginia Company under its new leadership sent Governor Yeardley instructions to call an assembly, part of a bid to make the colony attractive to settlers by giving landowning colonists a voice in their laws. The assembly met at Jamestown at the end of July. Within weeks of its sitting, a ship reached Virginia carrying Africans for sale. The colony gained representative government and began its history of African slavery in the same season, out of the same company\u2019s Virginia. Neither fact cancels the other, and the rest of American history is partly the working out of their coexistence.")
# 17 CONTENT F
content_text('The summer of 1619', ['The House of Burgesses meets at Jamestown', 'Landowning colonists choose representatives', 'Weeks later, a ship sells the colony some twenty Africans', 'Taken from a Portuguese slave ship in the Atlantic', 'Their legal status: the records do not say clearly'],
 "Carry the definition exactly. The House of Burgesses is this: " + "House of Burgesses: " + TD['House of Burgesses'] + ". Then teach the second event with the honesty the record requires. The Africans who arrived in late August 1619 had been taken from a Portuguese slave ship bound for Mexico and were traded to the colony for provisions. Whether they were held as servants for a term, as some early Africans in Virginia plainly were, or as enslaved for life, the surviving records do not say clearly, and historians still argue the question from thin evidence. What is not argued is the sequel: over the next two generations Virginia\u2019s assembly wrote slavery into statute, on the mother\u2019s status, on baptism, on property, until the ambiguity of 1619 had been replaced by hereditary racial slavery in law.")
# 18 STAT F
stat('20', 'Africans brought to Virginia in 1619', 'Some twenty, taken from a Portuguese slave ship, the first recorded in England\u2019s mainland colonies; their legal status is still argued by historians',
 "Stop on this small number against the scale of what follows from it. Some twenty people, in a colony of about a thousand, arriving weeks after the first assembly sat. Teach the figure with its documentary frame: the count comes from the colony\u2019s own reporting of the ship\u2019s arrival, the people named in it had been baptized in Angola and carried across the Atlantic in a Portuguese slaver before an English privateer took them. Then state the long arc without inflating the first step. These twenty were the beginning of African slavery in England\u2019s mainland colonies, not yet its legal system. Lesson 6 of this unit takes up the trade and the statutes whole. Here the point is the year: the future of Virginia was decided twice in one summer, in the assembly house and at the wharf, and students should leave able to say why both landings belong in the same sentence.")
# 19 DIVIDER G
divider_text('Section G', 'Land, Labor, and Rebellion', 'Headrights fill the colony with servants, the servants grow free and angry, and 1676 settles the labor question.',
 "Close the lesson by following the labor supply to its crisis, because section G is where the crop\u2019s second hunger is answered in full. After tobacco, Virginia\u2019s scarce resource was people to work it, and the company answered with the headright, paying land for imported labor. For two generations the Chesapeake ran on young English servants who gambled their worst years against a start in a colony where many of them died in the first summer. The survivors who lived out their terms became the frontier population of the 1670s, land hungry, armed, and governed by men whose great estates blocked their way. The section\u2019s story is how that population rose in 1676, what it did, and what the colony\u2019s great men decided, in its ashes, about the labor they would buy afterward.")
# 20 CONTENT G
content_text('Fifty acres a head', ['The headright: fifty acres for every passage paid', 'Import twenty servants, gain a thousand acres', 'Servants bound four to seven years for passage', 'Freedom dues at the term\u2019s end', 'Many die of seasoning fevers in the first summer'],
 "Carry both definitions exactly. The headright system is this: " + "headright system: " + TD['headright system'] + ". An indentured servant is this: " + "indentured servant: " + TD['indentured servant'] + ". Then do the arithmetic aloud, because the headright is a machine and students should see it work. A passage cost a planter about the price of a servant\u2019s first crop year. The passage bought two assets, the servant\u2019s labor for the term and fifty acres forever. Import twenty servants and the estate gained a thousand acres along with twenty workers. Land, the colony\u2019s wealth, flowed to the men who could import the most people, which is one reason the great planters of the later century were great. The servants\u2019 side of the machine is the next fact: the seasoning, the first summer\u2019s fevers, killed them in numbers the London recruiting pamphlets never printed.")
# 21 CONTENT G2
content_text('1676: the colony burns its capital', ['Frontier settlers and former servants follow Bacon', 'His declaration charges Berkeley with unjust taxes', 'And with shielding Indigenous peoples from retaliation', 'Jamestown burned, September 1676', 'Bacon dies in October; the rising collapses'],
 "Carry the definition exactly. Bacon\u2019s Rebellion is this: " + "Bacon's Rebellion: " + TD["Bacon's Rebellion"] + ". Then read the declaration as the station document it is, because Bacon\u2019s own charges fix the rising\u2019s politics. He accused Governor Berkeley of great unjust taxes raised for private favorites, and of protecting and emboldening the Indigenous peoples against the king\u2019s loyal subjects, and he signed himself Generall by Consent of the people while calling the king\u2019s governor a traitor. His men attacked Indigenous peoples, including peoples at peace with the colony, marched on Jamestown, and burned it in September 1676. Bacon died of illness that October and the rebellion collapsed. The planters\u2019 lesson from the rising was about labor: servants who survived became free, armed, and land hungry. Enslaved Africans could be held for life, marked by sight, and barred from ever standing where Bacon\u2019s men had stood. The turn toward enslaved labor, already under way, became decisive.")
# 22 GLANCE
s = slide(NAVY)
kicker(s, 'The colony at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Company, crop, labor, and turn', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The company', 'Joint-stock venture, chartered 1606', 'A profit demanded; none returned for years'),
        ('The hunger', 'Starving time, 1609 and 1610', 'About 60 survive of some 500'),
        ('The chiefdom', 'Wahunsenacawh\u2019s corn and diplomacy', 'The fort lives by his leave'),
        ('The crop', 'Rolfe\u2019s tobacco, from about 1612', 'Land and labor demanded without limit'),
        ('The turn', 'Rebellion in 1676, Jamestown burned', 'Planters choose enslaved labor for life')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 0.86
notes(s, "This slide mirrors the closing table of the guided notes, The Colony at a Glance, and students should complete that table now from memory where they can. Check the table with the two questions that expose shallow answers. First, which rows show the colony being acted on, and which show it acting? The hunger and chiefdom rows belong to a colony surviving on fleets and on another ruler\u2019s corn. The crop and turn rows belong to a colony making decisions, about land, about labor, and finally about whose labor would be bound for life. Second, which row reaches furthest past 1680? The turn: the labor settlement made after Bacon\u2019s Rebellion shaped Virginia for the next two centuries. The table is the lesson in miniature: a business venture, a near death, a chief\u2019s policy, a crop, and a choice about labor that outlasted everyone who made it.")
# 23 VOCAB A
vocab('Words for the venture and the crop', [(t, SHORT[t]) for t in ['joint-stock company', 'Jamestown', 'cash crop', 'headright system']],
 "Four terms, matching the guided notes word for word, and students should copy the definitions because the unit test draws on them. joint-stock company: " + TD['joint-stock company'] + ". Jamestown: " + TD['Jamestown'] + ". cash crop: " + TD['cash crop'] + ". headright system: " + TD['headright system'] + ". Press the chain these four terms make, because the chain is the lesson\u2019s skeleton. A joint-stock company founded Jamestown. A cash crop gave the company its return. The headright system paid for the crop\u2019s labor in land, and the land it paid out was Powhatan land.")
# 24 VOCAB B
vocab('Words for the labor and the turn', [(t, SHORT[t]) for t in ['indentured servant', 'House of Burgesses', "Bacon's Rebellion"]],
 "Three more terms, again matching the guided notes exactly. indentured servant: " + TD['indentured servant'] + ". House of Burgesses: " + TD['House of Burgesses'] + ". Bacon's Rebellion: " + TD["Bacon's Rebellion"] + ". Two details in these definitions earn emphasis before the exit ticket. The servant\u2019s definition ends with freedom dues at the end of the term, and that ending is the hinge of the whole labor story: a term that ends creates free people, and free people with grievances made 1676. The rebellion\u2019s definition ends with the consequence, great planters pushed toward enslaved labor, and a student who can state only the burning has half the event.")
# 25 SYNTHESIS
content_text('Answering the question', ['Survival first: corn, discipline, and a relief fleet', 'Then the crop: Rolfe\u2019s tobacco finds England\u2019s market', 'The land demand: fresh soil, taken from Powhatan towns', 'The labor demand: servants first, then enslaved for life'],
 "Run the synthesis as the writing task rehearsal, and build it from the class\u2019s own answers before summarizing. Strong answers refuse the single hero version in both its forms. The outpost did not survive because Smith rescued it or because Pocahontas rescued Smith; it survived because Wahunsenacawh\u2019s corn policy, hard discipline inside the fort, and a relief fleet in June 1610 carried it past the starving time. Nor did the crop simply save the colony once it arrived. Tobacco remade Virginia by making two demands no one could satisfy inside the colony\u2019s own borders: fresh land every few years, which meant Powhatan land, and labor in every season, which meant people bound first for terms and after 1676 for life. Test the synthesis against its rival before closing: a colony is not only what saves it. It is also what its salvation goes on to require.")
# 26 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4, ['How did a starving outpost become a tobacco colony, and what did tobacco demand?'], size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Tobacco Ledger: five records, the problem and cost in each, then a verdict'),
        ('Notebook', 'Notebook page: the colony chart, from the venture to the rebellion'),
        ('Quick check', 'The Map and the Colony: Smith\u2019s 1612 map, sourced and connected to 1676'),
        ('Writing', 'What Tobacco Demanded: survival, the crop, and its two demands in one essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: joint-stock company defined with the Virginia Company and 1606 named, the two arrivals of 1619, and the lesson question in two or three sentences.', size=15, color=POWDER)
notes(s, "Close by handing the lesson to the work. In the activity, The Tobacco Ledger, each group works five records, Smith\u2019s True Relation, his letter to Queen Anne read beside the starving time figures, the company\u2019s headright and assembly records, the tobacco and labor record, and Bacon\u2019s Declaration of 1676, states the problem each record was answering and what it cost, and judges which single change between 1607 and 1680 mattered most to what Virginia became. The notebook page rebuilds the lesson as a chart of what happened, the problem or demand, and the result. The quick check, The Map and the Colony, sources Smith\u2019s 1612 map and tests whether students can connect it to the rebellion of 1676. The writing task, What Tobacco Demanded, requires the lesson\u2019s double answer in essay form. The exit ticket has three parts: a joint-stock company defined with the Virginia Company and its charter year named, the two arrivals of the summer of 1619 stated, and the lesson question answered in two or three sentences.")

dc.save(OUT)
