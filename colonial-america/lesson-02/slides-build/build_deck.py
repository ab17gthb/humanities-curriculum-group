#!/usr/bin/env python3
"""Colonial America Lesson 2 deck, "The Spanish and French Americas,"
built to the approved system: image-led slides, fragments only on
screen, comprehensive speaker notes, full lesson + vocabulary
coverage. Fonts: Georgia titles, Lato body."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags, photo_right,
                         divider_photo, content_photo, content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED, W, H)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

dc.IMG = os.path.join(HERE, 'img')
OUT = os.path.join(HERE, '..', 'lesson-02-slides.pptx')

spec = open(os.path.join(HERE, '..', '..', 'build-scripts', 'unit-spec.md')).read()
l2 = spec.split('### Lesson 2')[1].split('### Lesson 3')[0]
DEFS = {}
for line in l2.splitlines():
    m = re.match(r'- (.+?): (.*)$', line.strip())
    if m: DEFS[m.group(1)] = m.group(2)
assert len(DEFS) == 7, DEFS.keys()

def joined(term):
    return f"{term}: {DEFS[term]}"

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

LQ = 'How did Spain build an empire on conquest, and how did France build one on trade?'
UQ = "How did the meeting of Europe, Africa, and the Americas remake all three worlds, and what kind of society grew up in England's colonies?"

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'COLONIAL AMERICA · LESSON 2', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Spanish and French Americas', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Spain rules an empire of millions, France trades across a continent', size=17, color=POWDER)
notes(s, "The image is the map of Tenochtitlan published at Nuremberg in 1524, three years after the city fell, the first printed picture of the Aztec capital most Europeans ever saw. Open by placing this lesson after the last one. Lesson 1 ended with a hemisphere shattered by epidemic disease, its peoples rebuilding and resisting from inside the loss. This lesson follows the two empires that moved into that world first and deepest. Spain conquered the great empires of Mexico and Peru and built the largest colonial system in the Americas, ruling millions of people through law, labor drafts, and ranked birth. France built something almost opposite in the north, a thin line of posts held together by trade and alliance, while running slave plantations in the Caribbean. Students should leave able to compare the two systems and to state the base both of them rested on.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[(LQ, {})]], size=40, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                (UQ, {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question sets two ways of holding a hemisphere side by side, and students will need both halves for the exit ticket and the writing task. The first half asks how Spain built an empire on conquest. The answer runs through Cortes and Tenochtitlan in 1521, the silver of Potosi, the encomienda labor system, and a society ranked by birth from peninsulares down to the enslaved. The second half asks how France built one on trade. That answer runs through Quebec in 1608, the fur trade, and alliances with Indigenous nations strong enough to set their own terms. Warn students now against the easy version of the contrast, in which Spain is violent and France is gentle. The lesson ends in the French sugar islands, under a written slave code, and the contrast has to survive that ending to be worth anything.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Conquest, silver, rank, trade, and the code', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The Conquistadores', 'Tenochtitlan falls in 1521, to allies and disease as much as to Spain'),
        ('B', 'Mines and Estates', 'Potosi silver, the royal fifth, and the hacienda'),
        ('C', 'The Encomienda and Las Casas', 'Forced labor, and the friar who put it on the record'),
        ('D', 'The Society New Spain Made', 'A ranked order of birth, and missions on the borders'),
        ('E', 'France on the St. Lawrence', 'Quebec, the fur trade, and alliances'),
        ('F', 'The Dutch, Louisiana, the Islands', 'New Netherland taken, and slavery written into French law'),
        ('G', 'Two Ways of Holding America', 'Rule against alliance, on one shared base')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A covers the conquest of Tenochtitlan and the forces that actually won it. Section B covers the empire Spain built on the conquests, its silver, its royal fifth, and its great estates. Section C covers the encomienda and Bartolome de las Casas. Section D covers the ranked society of New Spain and the missions. Section E covers France on the St. Lawrence and the fur trade. Section F covers the Dutch, Louisiana, and the sugar islands under the Code Noir. Section G draws the comparison the whole lesson builds toward. The summary table at the end of the guided notes is titled Two Empires at a Glance, and students will complete it from these seven sections.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', 'The Conquistadores',
             'A few hundred Spaniards march on the richest city in the Americas, and do not win alone.',
             "Set up the conquest as the lesson's first correction, because students usually arrive with a picture of Spanish soldiers defeating the Aztec empire by superior weapons. The weapons were real, and so were the horses and steel, but the numbers never worked. Cortes entered Tenochtitlan with about five hundred men, in a city of perhaps two hundred thousand people, the capital of an empire that collected tribute across central Mexico. What made the conquest possible was the politics of that empire itself. Peoples taxed and raided by the Aztecs, the Tlaxcalans above all, saw the newcomers as a weapon against their rulers and supplied the army that besieged the city. Epidemic smallpox, arriving with the Europeans, did the rest inside the walls. Teach the conquest as an Indigenous war as well as a Spanish one, because every later section depends on students seeing Indigenous peoples as actors with reasons of their own.")

# ------------------------------------------------------ 5 DIAZ ENTRY
content_photo('tenochtitlan-port.jpg', 'November 8, 1519: the entry',
              ['Bernal Diaz counts his company at 450 men',
               'Towns along the lake, canoes without number',
               'A great city rising from the water',
               'Warnings from Tlaxcala fill their minds'],
              "The image is the 1524 Nuremberg map of Tenochtitlan, drawn from a map sent home by the conquerors. Bernal Diaz del Castillo was a foot soldier on the causeway that morning, and he wrote his account decades later because official histories, he said, ignored the ordinary soldiers who had done the fighting. Read his numbers against his description. The city before him held large towns along the lake, still larger ones rising from the waters, bridges, temples, and crowds of canoes beyond counting. His own company, gazing at all of it, was a mere handful of men, in all 450. Ask students what a force that size can and cannot do to such a city. It cannot storm it. It can only enter it as guests, allies, or prisoners, and the warnings Diaz records, from the peoples of Huexotzinco, Tlaxcala, and Tlalmanalco, tell the class that Indigenous states were already recruiting the Spanish into their own quarrels with the Mexica empire.",
              kick='A · The Conquistadores')

# ------------------------------------------------------ 6 STAT 450
stat('450', 'Spaniards in the company Diaz counted',
     'Against a capital of perhaps 200,000 people · The siege of 1521 was carried by tens of thousands of Indigenous allies · Smallpox worked inside the city',
     "Hold this number in front of the class until its meaning settles. Four hundred and fifty is a large village or a small school. It is not an army capable of conquering an empire, and Diaz, who was there, gives the figure himself. When Tenochtitlan fell in August 1521, after a siege of three months, the besieging force was overwhelmingly Indigenous: Tlaxcalan and other allied warriors in the tens of thousands, fighting an empire whose tribute and captive taking they resented, for reasons the record gives in their own diplomacy. Inside the city, smallpox, carried in during the fighting, killed defenders and leaders, including the emperor Cuitlahuac, at the moment the city most needed them. Cortes then rebuilt Tenochtitlan as Mexico City, capital of the empire Spain would govern from the same streets. In Peru a decade later, Francisco Pizarro seized a second empire on the same pattern: Indigenous allies, an Inca civil war, and disease running ahead of the Spanish.",
     kick='A · The Conquistadores')

# ------------------------------------------------- 7 SECTION B DIVIDER
divider_photo('potosi-port.jpg', 'Section B', 'Mines and Estates',
              ['The woodcut shows Potosi and its', 'silver mountain, from the Chronicle', 'of Peru, printed in 1553.'],
              "The image is the first printed view of Potosi, a woodcut from Pedro Cieza de Leon's Chronicle of Peru of 1553, showing the silver mountain, the Cerro Rico, above the town that grew at its foot. What Spain built on its conquests was not a string of trading posts but a governed empire of cities, courts, treasuries, and mines, the largest colonial system in the Americas. Its engine was silver. The mountain at Potosi, in present day Bolivia, was found to be rich in silver in 1545, and within a generation the town beneath it held more than one hundred thousand people, one of the largest cities in the world, fed and supplied from a wide countryside because nothing grows at that altitude. Section B teaches the two institutions that carried the empire: the mine, taxed by the Crown before any owner was paid, and the hacienda, the great estate that fed the mining world and anchored Spanish power in the countryside.",
              title_size=40)

# ------------------------------------------------------ 8 SILVER AND HACIENDA
content_text('Silver out, food in: the working empire',
             ['New Spain governed from Mexico City',
              'Potosi and the Mexican mines drive the system',
              'The Crown takes its fifth of every mine',
              'Haciendas feed the towns and mines',
              'Silver flows to Europe, and onward to China'],
             "Walk the system as a circuit, because students remember circuits. New Spain, the viceroyalty governed from Mexico City, stretched from Panama to the present day American Southwest, and a second viceroyalty ruled Peru. At Potosi and in the Mexican silver districts around Zacatecas, drafted Indigenous laborers worked the mines in conditions that killed many of them. The Crown took its fifth, twenty percent of all silver, at the mine mouth, which made the Spanish state a partner in every shaft and gave it a direct interest in the labor supply. Around the mines stood the hacienda, the large estate worked by Indigenous or enslaved labor, raising wheat, cattle, and sheep for the mining towns, since mining camps at altitude could not feed themselves. Silver then moved outward: across the Atlantic to pay Spain's armies and creditors in Europe, and across the Pacific from Acapulco to Manila, where Chinese merchants traded silk and porcelain for the metal their economy prized.",
             kick='B · Mines and Estates', size=24)

# ------------------------------------------------------ 9 STAT 100,000
stat('100,000', 'people at Potosi within a generation of 1545',
     'A city larger than most in Spain, at 13,000 feet in the Andes · Built on one mountain of silver · Fed entirely from the countryside below',
     "Give students the scale of the mining city, because it overturns the picture of Spanish America as a frontier. Potosi in its great years held more than one hundred thousand people, by some counts more than London held in the same decades, and it sat nearly thirteen thousand feet up in the Andes, where frost rules every night and no grain ripens. Every loaf, hide, and timber in the city arrived by llama train and mule from valleys days away, which is why the hacienda economy of section B existed: the mine created a market that reorganized farming across half a continent. The labor that dug the silver was drafted. Under the mita, adapted from an Inca labor tax, Indigenous communities were required to send a share of their men to the mines for set terms, and many did not return. When students ask what the empire rested on, Potosi is the concrete answer: Indigenous labor, organized by the state, producing the metal the whole system ran on.",
     kick='B · Mines and Estates')

# ------------------------------------------------- 10 SECTION C DIVIDER
divider_text('Section C', 'The Encomienda and Las Casas',
             'The labor system at the base of the empire, and the Spaniard who put its cost on the record.',
             "This section teaches the encomienda twice, once as the system's defenders described it and once as its greatest Spanish critic recorded it, and students should hold the two descriptions apart. In law, the encomienda was a grant of trust: a colonist received the tribute and labor of the Indigenous people of a district, and in return he owed them protection and Christian teaching. In practice, as the reading states plainly, the grants were worked as forced labor, and communities already shattered by epidemic disease died under the demands. Into that gap stepped Bartolome de las Casas, a settler turned Dominican friar who had held an encomienda himself before renouncing it. For fifty years he argued at the Spanish court that Indigenous peoples were rational men and women whose rights bound the Crown, and in 1552 he published the account students will read in the activity. Teach him neither as a hero outside his world nor as a hypocrite inside it, but as evidence that the empire argued with itself, in its own courts, about what it was doing.")

# ------------------------------------------------------ 11 ENCOMIENDA
content_photo('mendoza-port.jpg', 'Tribute and labor, owed by law',
              ['A grant of a district and its people',
               'Tribute in goods and gold, labor on demand',
               'Protection and Christian teaching owed in return',
               'In practice, forced labor on a dying population'],
              "The image is a page of the Codex Mendoza, the tribute record painted by Indigenous artists for the Spanish Crown around 1541, listing what the Aztec empire's provinces had owed their rulers. Spain inherited that tribute machinery and redirected it. Under the encomienda, the Crown granted a colonist the Indigenous people of a named district. The grant did not give him their land in law. It gave him their tribute and their labor, in mines, fields, workshops, and building yards, and in return he was to protect them and have them taught the Christian faith. The bargain's terms were set entirely by the granting power, and the people bound by it had no seat at the making. Communities ordered to deliver goods, gold, and workers were the same communities epidemic disease was reducing year by year, so demands fixed in one decade fell on a fraction of the people a decade later. That arithmetic, more than any single cruelty, is what Las Casas carried to court, and it is why the encomienda became the empire's central argument with itself.",
              kick='C · The Encomienda and Las Casas')

# ------------------------------------------------------ 12 STAT 12 MILLION
stat('12 million', 'deaths Las Casas claimed in forty years',
     'His figure for the Indies as a whole, printed in 1552 · Three million on Hispaniola, he wrote, reduced to scarce three hundred · Historians read his counts as claims, and the collapse itself as beyond dispute',
     "Teach this figure with its label attached, because the label is part of the history. Las Casas wrote that of three million people on Hispaniola, scarce three hundred remained, and he dared to affirm that above twelve million people had perished in forty years of Spanish tyranny in the Indies. His numbers were arguments, built to force a king to act, and modern historians hold that he exaggerated them and simplified a catastrophe driven chiefly by epidemic disease. What is not in dispute is the direction and the scale: across the Caribbean and the mainland, Indigenous populations fell by half, by three quarters, in many regions by nine in ten, within a century of contact. Las Casas's advocacy helped push the Crown to the New Laws of 1542, which limited the encomienda. Colonists resisted, the harshest clauses were withdrawn, and labor drafts continued in new forms. Las Casas also, early on, suggested African labor as a substitute for Indigenous labor, a position he later repented and condemned, and students should hear that turn stated plainly, because it connects this lesson to the slave systems the unit takes up next.",
     kick='C · The Encomienda and Las Casas')

# ------------------------------------------------- 13 SECTION D DIVIDER
divider_text('Section D', 'The Society New Spain Made',
             'A ranked order of birth, carried in law and custom, and missions on the empire\'s edges.',
             "Spain did not only extract from its American empire. It built a society there, with cities, universities, cathedrals, and a social order as deliberate as its tax system, and section D teaches that order as its builders designed it. Every person in Spanish America held a rank fixed largely at birth. Spaniards born in Spain stood at the top and held the great offices. Spaniards born in America, the creoles, owned most of the land and wealth and resented a ceiling they could see but not pass. Between Spaniards and Indigenous peoples stood the growing mestizo population, and at the bottom stood Indigenous communities and enslaved Africans, whose labor carried the whole structure. On the empire's borders, where settlers were few, the mission did the work of expansion, gathering Indigenous peoples into supervised towns. Teach the order as a system with daily consequences: rank decided office, dress, marriage, tax, and the court a person could appeal to.")

# ------------------------------------------------------ 14 RANKED ORDER
content_text('Ranked by birth',
             ['Peninsulares: born in Spain, holding the high offices',
              'Creoles: born in America, owning the land',
              'Mestizos: between Spaniards and Indigenous peoples',
              'Indigenous communities and enslaved Africans at the base',
              'Wealth and favor sometimes moved a family across the lines'],
             "Take the four ranks in order and give each its grievance, because the grievances explain the politics of the next two centuries. The peninsulares, officials born in Spain, arrived with royal appointments and answered to Madrid, and American born Spaniards watched them take the viceroyalties, judgeships, and bishoprics. The creoles owned the haciendas and mines and filled the city councils, and their resentment at exclusion from high office is the seed of the independence movements students will meet in a later course. The mestizo population, people of mixed Spanish and Indigenous ancestry, grew every generation and fit the order's categories worst, ranked between Spaniards and Indigenous peoples and pressing against both. At the base stood Indigenous communities, taxed and drafted as corporate bodies, and enslaved Africans, held as property. The lines were policed in law and custom, in marriage registers and tax lists, and they were also crossed, by wealth, by royal favor, and by the simple arithmetic of generations, which is why the order needed constant defending.",
             kick='D · The Society New Spain Made', size=24)

# ------------------------------------------------------ 15 MISSIONS
content_text('Missions on the borders',
             ['Religious settlements among Indigenous peoples',
              'From Florida and Texas to California',
              'Farming, crafts, and doctrine taught together',
              'Towns gathered, and disease followed the gathering',
              'Languages and kin ties kept alive inside the walls'],
             "Place the mission where it belongs, on the edges of the empire, in Florida, Texas, New Mexico, and eventually California, in country Spain claimed but could not garrison. A mission was a religious settlement founded by Catholic orders, Franciscans above all, among Indigenous peoples, to convert them and remake their way of life. Families were gathered into a supervised town around a church, taught farming and crafts alongside doctrine, and governed by a daily round of bells, work, and worship. The missions extended Spanish language, livestock, and authority hundreds of miles beyond the settler towns at a cost in soldiers the Crown never had to pay. Their human cost fell on the gathered. Crowded towns raised epidemic disease to a killing rhythm, and mission populations fell at grievous rates even as new families were brought in. Teach the second half of the story too: Indigenous residents used the missions on their own terms, kept languages, kin ties, and older practices alive inside them, fled when they could, and sometimes rose against them.",
             kick='D · The Society New Spain Made', size=24)

# ------------------------------------------------- 16 SECTION E DIVIDER
divider_photo('quebec-port.jpg', 'Section E', 'France on the St. Lawrence',
              ['Champlain\'s drawing of his habitation', 'at Quebec, the post he founded', 'in 1608.'],
              "The image is Samuel de Champlain's own drawing of the habitation at Quebec, the fortified warehouse, dwellings, and garden he raised in 1608 on the St. Lawrence River. Everything about the French empire in the north follows from the size of this picture. The post held a few dozen men. The colony it anchored held, for most of the century, a few thousand settlers strung along one river, in a country whose winters closed the river for half the year. Such a colony could not conquer, tax, or draft the Indigenous nations around it, and it did not try. It traded. Beaver pelts, gathered by Indigenous hunters across half a continent and carried to the French posts by Indigenous canoes, paid for the whole enterprise, and the trade's terms were set in council, with peoples who had other buyers and armies of their own. Section E teaches the alliance system the fur trade required, and the two generations of war with the Haudenosaunee that the trade's rivalries produced.",
              title_size=40)

# ------------------------------------------------------ 17 FUR TRADE
content_text('The exchange neither side could run alone',
             ['Beaver pelts down the rivers to Quebec',
              'Axes, kettles, knives, cloth, and firearms in return',
              'Prices set in council, sealed with gifts',
              'The hunting country stayed in Indigenous hands'],
             "Break the exchange down to its two columns, as the activity asks students to do. Down the rivers came beaver pelts, the raw material of the felt hats all Europe wore, gathered by Montagnais, Algonquin, and Huron hunters in country the French had never seen and could not enter uninvited. Up the rivers went manufactured goods: iron axes and kettles that outworked stone and clay, knives, cloth, and, increasingly, firearms. Neither column could be supplied by the other side, which is the structure's whole meaning. France had no hunters, no canoes, and no knowledge of the interior. Its partners had no ironworks. Prices were not posted but negotiated, in councils that opened with gifts and speeches and the renewal of the alliance itself, because in the diplomacy of the woodlands a trade agreement and a political alliance were the same document. When beaver grew scarce in one district, the trade moved west, and France had to win new partners in new country, on terms those peoples accepted.",
             kick='E · France on the St. Lawrence', size=24)

# ------------------------------------------------------ 18 ALLIANCES
content_text('Allies, marriages, and a two generation war',
             ['Traders live in Indigenous towns and learn the languages',
              'Intermarriage binds the trade to kinship',
              'Shared war against the Haudenosaunee',
              'Missions travel the same routes as the trade'],
             "The alliance system ran on people, not paper. French traders wintered in Indigenous towns, learned the languages, and married into the nations, so that trade partnerships became kinship, the strongest bond the woodlands recognized. Champlain set the pattern early by joining his partners' wars, and the enemy that choice made was the Haudenosaunee, the Five Nations south of Lake Ontario, whose own trade ambitions ran through Dutch posts on the Hudson and whose hunting country the beaver wars of the middle century were fought over. France and the Haudenosaunee remained enemies, with truces, for two generations. Jesuit missionaries traveled the traders' routes to the same towns, learned the same languages, and built missions among the Huron and other nations, with results the next unit of the course will meet again: converts, divisions inside nations, and records written in Indigenous languages. Through all of it, French survival was renewed annually, in councils where Indigenous leaders set terms a governor could accept or refuse but not dictate.",
             kick='E · France on the St. Lawrence', size=24)

# ------------------------------------------------- 19 SECTION F DIVIDER
divider_text('Section F', 'The Dutch, Louisiana, and the Sugar Islands',
             'A second fur colony falls to England, and France\'s richest America turns out to run on enslaved labor.',
             "This section widens the map and then breaks the lesson's easy contrast, deliberately. The Dutch built their own fur colony on the Hudson, New Netherland, with its capital at New Amsterdam, and held it for forty years before an English fleet took it in 1664 and renamed it New York. France answered England's growing presence by planting Louisiana in 1699 at the mouth of the Mississippi, a colony meant to hold the river, the Gulf, and the road west. Both stories belong to the northern pattern of posts and trade. The section then turns south to the America that paid France's colonial bills: the sugar islands of the Caribbean, Saint Domingue above all, where plantations worked by enslaved Africans produced wealth the fur trade never approached. There France did not ally and negotiate. It legislated slavery, in the Code Noir of 1685, and students will read the code's own articles in the activity.")

# ------------------------------------------------------ 20 DUTCH AND LOUISIANA
content_text('New Netherland falls, Louisiana planted',
             ['The Dutch on the Hudson from the 1620s',
              'Furs through Iroquois country, farms along the river',
              'England seizes the colony in 1664: New York',
              'France plants Louisiana in 1699 to hold the Mississippi'],
             "The Dutch West India Company planted New Netherland in the 1620s for the same beaver that built New France, trading through Iroquois country at Fort Orange and farming the Hudson valley from New Amsterdam at the river's mouth. The colony was always thinly peopled, and in 1664 an English fleet took it without a battle the settlers were willing to fight. Renamed New York for the king's brother, it kept its Dutch families, churches, and place names, a reminder that empires changed flags faster than they changed populations. France watched England consolidate the coast and answered at the continent's other door. In 1699 French colonists planted Louisiana at the mouth of the Mississippi, claiming the river system Champlain's successors had explored, checking Spain's Gulf settlements, and giving the fur trade a southern outlet. Louisiana stayed poor, garrisoned, and dependent on enslaved African labor and Indigenous alliances at once, a colony that belonged to both of the lesson's patterns and prospered at neither.",
             kick='F · The Dutch, Louisiana, the Islands', size=24)

# ------------------------------------------------------ 21 CODE NOIR
content_text('The Code Noir, 1685: slavery in French law',
             ['Article II: baptism and Catholic instruction for the enslaved',
              'Article XII: children of enslaved parents are enslaved',
              'Article XXXVIII: flight punished with mutilation and branding',
              'Article LIX: freed slaves granted the rights of the freeborn'],
             "Read the four articles as a system, the way the activity sets them in front of students. Article II required every enslaved person in the French islands to be baptized and instructed in the Roman Catholic faith, bringing the church inside the slave system as its registrar. Article XII made the system hereditary: children born from marriages between slaves were slaves, so status passed through birth and no generation could age out of it. Article XXXVIII policed the system's edge: an enslaved person on the run for one month was to have his ears cut off and be branded with a fleur de lys on one shoulder, with worse for a second flight. Article LIX then held out the system's one door: freed slaves were granted the same rights, privileges, and immunities as the freeborn. On Saint Domingue, the richest sugar colony in the world, this code was working law, and the empire of alliances in the north and the empire of the code in the islands were the same French empire, flying the same flag.",
             kick='F · The Dutch, Louisiana, the Islands', size=23)

# ------------------------------------------------- 22 SECTION G DIVIDER
divider_text('Section G', 'Two Ways of Holding America',
             'Rule against alliance, and the base both empires shared.',
             "Close the lesson by making the comparison do its full work, in both directions. By 1700 Spain had built the stronger holding by every measure of permanence: millions of subjects, cities larger than Spain's own, a revenue in silver, and a society that reproduced itself across generations. France had built the wider holding at the smaller cost: a few thousand settlers, a web of alliances reaching to the Mississippi and the Great Lakes, and an empire that survived because it served the interests of the nations inside it. Then set both holdings on the record's base. Spain's conquests were made by Indigenous armies and its wealth dug by Indigenous and African labor. France's trade was gathered and defended by Indigenous partners, and its richest colonies ran on enslaved Africans under a written code. The forms differed completely, and students should be able to describe the difference exactly. The dependence did not differ, and students should be able to state that exactly too.")

# ------------------------------------------------------ 23 GLANCE
s = slide(NAVY)
kicker(s, 'Two empires at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Rule and alliance, side by side', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('How it came', 'Conquest, 1519 to 1521 and after', 'Settlement for trade, Quebec 1608'),
        ('What it lived by', 'Silver, tribute, hacienda produce', 'Furs in the north, sugar in the islands'),
        ('Whose labor', 'Indigenous drafts and enslaved Africans', 'Indigenous partners; enslaved Africans in the islands'),
        ('Indigenous nations', 'Subjects, ranked and missionized', 'Allies, courted and fought beside')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, Two Empires at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The four rows are the lesson's argument in order. How it came: Spain by conquest in 1519 to 1521, carried by Indigenous allies and disease; France by settlement for trade, Quebec in 1608. What it lived by: Spain by silver, tribute, and hacienda produce; France by furs in the north and sugar in the islands. Whose labor: Spain commanded Indigenous drafts and enslaved Africans; France traded with Indigenous partners and enslaved Africans on the plantations. How it treated Indigenous nations: Spain ruled them as ranked subjects and gathered them into missions; France courted them as allies because it could not rule them. Grade the table generously on wording and strictly on the last column of the labor row: an entry that leaves enslaved labor out of the French column has missed section F, and with it the lesson's closing judgment.")

# ------------------------------------------------------ 24 VOCAB A
vocab('Words for the Spanish empire',
      [('conquistador', 'a Spanish conqueror of the 1500s'),
       ('encomienda', 'the grant of Indigenous tribute and labor'),
       ('mestizo', 'of mixed Spanish and Indigenous ancestry'),
       ('New Spain', "Spain's viceroyalty, governed from Mexico City")],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. " + joined('conquistador') + ". " + joined('encomienda') + ". " + joined('mestizo') + ". " + joined('New Spain') + ". Teach the four as one system's parts. The conquistador made the conquest, the encomienda organized the labor the conquest delivered, the mestizo population grew inside the ranked society the system built, and New Spain was the government that held it all, from Mexico City to the borders of the present day Southwest.")

# ------------------------------------------------------ 25 VOCAB B
vocab('Words for the borderlands and the trade',
      [('mission', 'a religious settlement among Indigenous peoples'),
       ('fur trade', 'manufactured goods exchanged for beaver pelts'),
       ('hacienda', 'a large estate worked by Indigenous or enslaved labor')],
      "Three more terms, again matching the guided notes exactly. " + joined('mission') + ". " + joined('fur trade') + ". " + joined('hacienda') + ". Keep the geography in view for review. The mission stood on the borders of the Spanish and French colonies alike, the fur trade ran the French and Dutch north, and the hacienda anchored the Spanish countryside, so the three terms together map the two empires' working institutions.")

# ------------------------------------------------------ 26 SYNTHESIS
s = slide(NAVY)
kicker(s, 'The lesson in one view')
text(s, 0.9, 1.28, 11.5, 1.0, 'Two empires, one shared base', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Conquered', 'Tenochtitlan falls in 1521, to allies and smallpox as much as to Spain'),
        ('Ruled', 'Silver, the fifth, the encomienda, and a society ranked by birth'),
        ('Traded', 'Quebec lives by pelts it cannot gather, on terms set in council'),
        ('Enslaved', 'The Code Noir of 1685 writes slavery into French law')]
yy = 2.78
for t, d in rows:
    text(s, 0.9, yy, 2.4, 0.7, t, size=24, color=RUST_LT, font='Georgia')
    text(s, 3.45, yy + 0.05, 9.0, 0.9, d, size=19, color=CREAM, leading=1.2)
    yy += 1.05
notes(s, "Use this slide to close the argument before the work begins, and make students say the four rows aloud in order, because the sequence is the lesson. Conquered: Tenochtitlan fell in 1521 to a siege carried by Indigenous allies and smallpox as much as by the five hundred Spaniards who entered it. Ruled: Spain governed its prize through silver and the royal fifth, the encomienda and the drafts that followed it, missions on the borders, and a society ranked by birth from peninsulares to the enslaved. Traded: France held the north with a few thousand settlers because the fur trade let it grow rich on pelts gathered by Indigenous partners, at prices set in councils it did not control. Enslaved: the same France wrote the Code Noir in 1685 and ran its richest colonies on enslaved African labor. Two empires, opposite in form, and one shared base in land taken and labor coerced.")

# ------------------------------------------------------ 27 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did Spain build an empire on conquest, and how did France build one on trade? Complete the comparison before you judge which holding was stronger.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'Two Empires, One Hemisphere: five stations and a verdict for 1700'),
        ('Notebook', 'Notebook page: the two empires in five rows, and the difference that counted most'),
        ('Quick check', 'The Causeway and the Code: the 1524 map, the conquest, and the Code Noir'),
        ('Writing', 'Two Ways of Holding a Hemisphere: the lesson question as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the encomienda defined with its critic named, the fur trade explained with its numbers, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, Two Empires, One Hemisphere, puts five stations in front of students: Diaz entering Tenochtitlan, Las Casas on the destruction, summaries of the encomienda and the New Laws and of the fur trade, and the Code Noir's own articles, and it ends with a comparison table and a verdict on which empire's way of holding America proved stronger by 1700. The notebook page charts the two empires across five questions. The quick check, The Causeway and the Code, tests the 1524 map, the forces that took Tenochtitlan, the governor who could not command his partners, and the code's three rules. The writing task turns the lesson question into an essay argued from the evidence bank, closing with the student's judgment on whether the contrast between the empires survives the sugar islands. The exit ticket has three parts: the encomienda with Las Casas, the fur trade with its numbers, and the lesson question in two or three sentences. Next lesson turns to the English, and to a starving outpost on the James River.")

dc.save(OUT)
