#!/usr/bin/env python3
"""Colonial America Lesson 5 deck, "The Middle Colonies and the Atlantic
Economy." V2 (2026-10-24 rollout, improved slide standard): content
bullets are short complete sentences; speaker notes applied after the
build from the teacher notes guide (apply_guide_notes.py). Same 28 slides."""
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
OUT = os.path.join(HERE, '..', 'lesson-05-slides-v2.pptx')

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

def content_photo_s(img, title, items, note, kick=None):
    s = slide(CREAM)
    photo_right(s, img)
    if kick: kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95 if kick else 0.8, 6.9, 1.2, title, size=30, color=NAVY, font='Georgia', leading=1.05)
    frags(s, items, y=2.12 if kick else 2.0, size=21, gap=11, leading=1.2)
    notes(s, note)
    return s

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'COLONIAL AMERICA · LESSON 5', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Middle Colonies and the Atlantic Economy', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Many peoples on the land, one system on the water', size=17, color=POWDER)
notes(s, "The image is Jean Leon Gerome Ferris's painting of William Penn landing in Pennsylvania, held by the Library of Congress and in the public domain. It opens the lesson that completes the tour of the three colonial regions. The Chesapeake grew tobacco and New England built covenant towns. Between them sat the middle colonies, New York, New Jersey, Pennsylvania, and Delaware, the most mixed society on the seaboard, where Dutch, English, German, Welsh, and Scots-Irish settlers, several churches, and enslaved Africans shared the same ports and farms. Over that mixture London laid one economic system, mercantilism, enforced by the Navigation Acts. Students should leave able to explain both halves together: how conscience and worship were settled colony by colony, often from below, while trade was routed from above, and how colonists grew rich inside rules written for someone else's benefit.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("How did the middle colonies become the colonies of many peoples, and what held the Atlantic economy together?", {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ("How did the meeting of Europe, Africa, and the Americas remake all three worlds, and what kind of society grew up in England's colonies?", {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "The lesson question has two halves, and students should keep both in view all hour. The first half asks how the middle colonies became the colonies of many peoples, which is a question about settlement: a Dutch trading colony taken over whole, a Quaker proprietor who advertised in three languages, land bought from the Lenape in council, and a Maryland law that tried to keep Catholics and Protestants from each other's throats. The second half asks what held the Atlantic economy together, which is a question about rules: mercantilism as the theory, the Navigation Acts as the law, and the triangular trade as the lived pattern of ships and cargoes. Neither half explains the lesson alone. The diversity happened inside the empire's frame, and the frame held because colonial merchants found room to profit inside it. Every section that follows feeds one half or the other, and the closing synthesis joins them.")

# ------------------------------------------------- 3 ONE SLIDE
s = slide(CREAM)
kicker(s, 'The lesson in one slide', color=RUST)
text(s, 0.9, 0.95, 11.5, 1.0, 'Seven parts, in order', size=31, color=NAVY, font='Georgia')
frags(s, ['A. A Dutch colony becomes New York',
          'B. Penn and the holy experiment',
          'C. The Lenape and the land',
          'D. Maryland: toleration with teeth',
          'E. Flushing: conscience from below',
          'F. Mercantilism and the Navigation Acts',
          'G. One Atlantic economy'], y=2.0, size=25, gap=10)
notes(s, "Use this slide as the map of the hour, and point students to the same seven letters in their guided notes. Section A takes New Netherland from Dutch fur trade colony to English New York in 1664, with its people unchanged. Section B gives Penn his charter of 1681 and his advertised holy experiment. Section C slows down on the land itself, because every acre Penn sold was Lenape land sold in council for Lenape reasons. Sections D and E are the toleration pair: Maryland's Toleration Act of 1649, protection and penalties in one law, against the Flushing Remonstrance of 1657, a petition from below. Section F states the imperial frame, mercantilism and the Navigation Acts of 1651 and 1660. Section G draws the whole Atlantic as one economy and closes with the population estimates, about 250,000 people in 1700 and about 2.5 million by 1775.")

# ------------------------------------------------- 4 DIVIDER A
divider_photo('castello-port.jpg', 'Section A', 'A Dutch Colony Becomes New York',
    ['A fur trade port on the Hudson', 'Many languages in one town'],
    "The image is the Castello Plan of 1660, the map of New Amsterdam drawn from Jacques Cortelyou's survey by Johannes Vingboons, in the public domain. Have students read it as a port before anything else: a walled town at the tip of Manhattan, a harbor full of shipping, farms and gardens behind the wall. This was the capital of New Netherland, the Dutch West India Company's colony planted for the fur trade, beaver pelts moving down the Hudson from Indigenous hunters and out to Europe. The town inside the wall held Dutch settlers, enslaved Africans, and traders of several nations, and contemporary visitors counted its languages in the teens. Section A asks what an English takeover could change in a place like this, and what it could not change overnight. The answer runs through the next two slides: the flag, the governor, and the colony's name changed in 1664. The people, their farms, their churches, and their enslaved laborers did not change at all.")

# ------------------------------------------------- 5 CONTENT A
content_photo_s('castello-port.jpg', 'New Amsterdam, a trading town',
    ['New Netherland existed to trade: the Dutch West India Company planted it for the fur trade.', 'New Amsterdam was a company town of a fort, a church, and warehouses.', 'Enslaved Africans built and fed the town from the colony\'s early decades.', 'Traders and settlers of several nations filled the port, and its taverns heard many languages.'],
    "New Netherland existed to trade. The Dutch West India Company planted it along the Hudson River because the river ran into beaver country, and Indigenous hunters supplied the pelts that paid for the colony. New Amsterdam, at the river's mouth, was a company town before it was anything else, with a fort, a church, warehouses, and enslaved Africans whose labor built and fed it from the colony's early decades. Upriver, great patroon estates lined the Hudson, worked by Dutch tenant farmers. The town's population was never simply Dutch: traders, sailors, and settlers of several nations used the port, and its churches and taverns heard many languages. Hold that mixture in mind, because it is the first source of the middle colonies' diversity. New York did not have to import its mixture. It inherited one, whole, from the Dutch colony it absorbed, and then Pennsylvania added a second, larger mixture beside it.",
    kick='Section A · New Netherland')

# ------------------------------------------------- 6 CONTENT A2
content_text('1664: a new flag, the same people',
    ['In 1664 an English fleet arrived, and Director General Stuyvesant surrendered without a battle.', 'Charles II had already granted the colony to his brother, making New York a proprietary colony.', 'Dutch farms, churches, estates, and language stayed in place for generations.', 'Enslaved Africans, who had no say in which empire held them, remained enslaved.'],
    "In 1664 an English fleet entered the harbor and Director General Peter Stuyvesant surrendered New Netherland without a battle. King Charles II had already granted the colony to his brother, the Duke of York, which made New York a proprietary colony in English hands. Define the term here as the guided notes carry it, because students meet it again in Maryland and Pennsylvania. The takeover's limits are the point of this slide. The English took the fort, the customs house, and the government. They did not and could not replace the population. Dutch farmers kept their farms and their church, Dutch remained a language of the Hudson valley for generations, the patroon estates survived, and enslaved Africans, who had no say in which empire held them, remained enslaved under new rulers. Conquest in the middle colonies meant a change of management over a society that kept its shape. That pattern, new rulers over old peoples, is the region's first lesson.",
    kick='Section A · The takeover')

# ------------------------------------------------- 7 DIVIDER B
divider_photo('birth-port.jpg', 'Section B', 'Penn and the Holy Experiment',
    ['A royal debt paid in land, 1681', 'An invitation printed in three languages'],
    "The image is Jean Leon Gerome Ferris's painting The Birth of Pennsylvania, showing Penn receiving his charter, held by the Library of Congress and in the public domain. Pennsylvania began as bookkeeping: Charles II owed a large debt to Admiral William Penn, and in 1681 he paid the admiral's son with a charter to a colony between New York and Maryland. The son, William Penn, was a Quaker, and he meant to make the payment into something larger, a holy experiment, a colony governed by the principles of a faith that England jailed. Section B follows what Penn did with the grant: he advertised across Europe in English, Dutch, and German, he promised land, an elected assembly, and liberty of worship, and he laid out Philadelphia in 1682 as the colony's port and advertisement in one. The settlers who answered made Pennsylvania the most deliberately recruited colony in English America, and the next slide names them in order.")

# ------------------------------------------------- 8 CONTENT B
content_photo_s('landing-port.jpg', "Penn's offer, and who answered",
    ['Penn offered land a family could buy, an elected assembly, and liberty of worship.', 'His invitation was printed in English, Dutch, and German.', 'English and Welsh Quakers answered first, then German families, then Scots-Irish settlers.', 'Philadelphia was laid out in 1682 as the port that turned the colony\'s wheat into exports.'],
    "Penn's invitation was a printed argument. In English in 1681 and in Dutch and German editions for continental readers, he offered three things: land that a family could buy, a government with an elected assembly, and freedom of worship for people whom England and New England punished for their faith. Define his faith here from the guided notes: the Quakers rejected formal ministers and oaths and held women and men spiritually equal, which is why their meetings drew fines, whippings, and prison at home. The answers came in waves. English and Welsh Quakers came first. German families followed, founding Germantown in 1683. Scots-Irish settlers arrived in the next century and pushed toward the backcountry. Underneath the offer sat the colony's wheat land, rich enough to feed the settlers and then to feed the Caribbean. Philadelphia, gridded in 1682 between two rivers, became the machine that turned that wheat into exports.",
    kick='Section B · The invitation')

# ------------------------------------------------- 9 STAT
stat('1750', 'Philadelphia is the largest city in British America',
    'A Quaker port built on grain and flour, seventy years after the charter of 1681',
    "Slow down on this number, because it measures how fast Penn's experiment filled. In 1750, by contemporary counts, Philadelphia passed Boston and New York to become the largest city in British America, a position it held for the rest of the colonial period. The engine was not a single cash crop like tobacco. It was grain and flour, milled in the countryside, carted to Philadelphia's wharves, and shipped to the Caribbean sugar islands and to southern Europe. Around the wharves grew the trades a port feeds: shipwrights, coopers, millers, bakers, merchants, and printers, in a city whose population mixed English, Welsh, German, Scots-Irish, and African people, free and enslaved. Students should connect the stat to Section B's invitation. Penn advertised for settlers in three languages, and the settlers came in numbers large enough to make his city first in British America within one long lifetime. The next section asks whose land made room for all of them.",
    kick='Section B · The result')

# ------------------------------------------------- 10 DIVIDER C
divider_text('Section C', 'The Lenape and the Land',
    'Parties to the sale, with reasons of their own',
    "Introduce this section plainly: every acre Penn sold was Lenape land first, and the Lenape were parties to its transfer, not scenery inside someone else's founding story. The Lenape homeland ran across the Delaware valley, and by 1682 its towns had been thinned by epidemics that arrived with European trade. Dutch and Swedish traders had competed for Lenape furs for decades, and stronger Indigenous neighbors pressed on Lenape borders. Lenape leaders therefore faced a set of hard choices, and selling land to Penn was one of them, made for Lenape reasons: trade goods, a settled buyer who paid, and settlements that could stand as a counterweight to rivals. Penn, for his part, held that a charter from a king did not by itself make land his to sell. He bought in council. In his lifetime the standard held, and the section closes with what his sons did to it in 1737.")

# ------------------------------------------------- 11 CONTENT C
content_text('Why the Lenape sold, and what Penn promised',
    ['Epidemic disease had shrunk Lenape towns, and the fur trade tied their economy to European goods.', 'Stronger neighbors, the Susquehannock and the Haudenosaunee, pressed Lenape borders.', 'A land sale brought trade goods and a numerous, well supplied neighbor as a counterweight.', 'Penn bought in council, meeting Lenape leaders at Shackamaxon in 1682.', 'In Penn\'s lifetime, Pennsylvania had no war between colonists and Native peoples.'],
    "Teach this slide as two decisions meeting. The Lenape decision came first. Epidemic disease had reduced their towns, the fur trade had tied their economy to European goods, and the Susquehannock and the Haudenosaunee pressed their borders in turn. A land sale to Penn converted land into trade goods and into a relationship with a numerous, well supplied neighbor whose presence complicated life for Lenape rivals. That is diplomacy, conducted with the tools at hand. Penn's decision matched it. He met Lenape leaders in council, in meetings remembered at Shackamaxon in 1682, under the elm that later tradition made famous, and he paid for the land his settlers occupied, treating the councils as binding sales. The result was unusual in colonial America: in Penn's lifetime, Pennsylvania had no war between colonists and Native peoples. Students should hold both halves, the Lenape strategy and Penn's rule, because the next slide shows how quickly the settlement aged once Penn was gone.",
    kick='Section C · Two decisions')

# ------------------------------------------------- 12 CONTENT C2
content_photo_s('colonists-port.jpg', '1737: the standard breaks',
    ['In 1737 the proprietors produced an old deed claiming land as far as a man could walk in a day and a half.', 'They cleared a path and hired trained runners, who covered some sixty miles.', 'The walk took far more Lenape land than any council had agreed to sell.', 'Lenape families were pushed west, toward the Susquehanna and the Ohio country.'],
    "The image is an 1893 book illustration of Penn's colonists on the Delaware, printed in a United States history of that year and free of known copyright restrictions. Use it to mark the change of era: the orderly arrival it pictures belongs to Penn's lifetime, not to his sons'. In 1737 the proprietors produced an old deed, said to date from 1686, claiming land extending as far as a man could walk in a day and a half. They cleared a path, hired trained runners, and covered some sixty miles, taking in far more Lenape land around the Lehigh valley than any council had agreed to sell. Lenape protests went to the Haudenosaunee, who, pursuing their own diplomacy, ordered the Lenape to accept the result and leave. Families moved west toward the Susquehanna and the Ohio country. The point for students is not that Penn was betrayed in the abstract. It is that his standard depended on his own observance, and nothing in the colony's law made his heirs keep it.",
    kick='Section C · After Penn')

# ------------------------------------------------- 13 DIVIDER D
divider_text('Section D', 'Maryland: Toleration with Teeth',
    'Protection and penalties in the same act, 1649',
    "Maryland, directly south of Pennsylvania, was the Calvert family's proprietary colony, founded as a refuge for English Catholics in a Protestant kingdom. By 1649 the refuge had inverted: Protestant settlers outnumbered the Catholic founders, the two sides had already fought a small civil war of raids and seizures in the 1640s, and the assembly needed a law that would keep the colony from tearing itself apart again. The Maryland Toleration Act was that law, and this section teaches it whole, as the unit insists: the famous protection clause and the death penalty clause stand in the same statute, a few paragraphs apart, because both served the same purpose of enforced peace. Students who meet only the protection half will call 1649 a birthplace of religious freedom and miss what the act actually was, a settlement between Christian camps, guarded by terror at its edges. The next two slides take the act's halves in the act's own order, penalty first.")

# ------------------------------------------------- 14 CONTENT D
content_text("The act's protection, stated exactly",
    ['The act shielded any person professing belief in Jesus Christ from being troubled for their religion.', 'No one could be compelled to another faith against their consent.', 'The shield covered Christians only, Catholic and Protestant alike.', 'It held only while the person stayed loyal to the proprietor and the civil government.'],
    "Read the protection clause with the class, slowly, because its wording carries its limits inside it. The act orders that no person within the province professing to believe in Jesus Christ shall be any ways troubled, molested, or discountenanced for or in respect of his or her religion, nor compelled to the belief or exercise of any other religion against his or her consent. In 1649, in a century when England had executed men over worship, that was a wide shield, and it covered Catholic and Protestant alike, which was the point: the Catholic proprietor's assembly protected the Protestant majority's worship alongside its own. But note the two borders drawn in the same breath. The shield covers only those professing belief in Jesus Christ. And it holds only so long as the person is not unfaithful to the Lord Proprietary or conspiring against the civil government. Worship was protected as a branch of public order, not yet as a right held against the state.",
    kick='Section D · Protection')

# ------------------------------------------------- 15 CONTENT D2
content_text("The act's penalties, in the same law",
    ['Whoever denied the Trinity faced death and confiscation of all lands and goods.', 'Reproachful speeches about the Virgin Mary or the apostles drew fines, then whipping, then banishment.', 'Calling a neighbor a religious insult, heretic, papist, puritan, or Roundhead among them, cost ten shillings an offense.', 'Protection and punishment were one policy: enforced peace between Christian camps.'],
    "Now the other half, which the act places first. Whoever denied the Holy Trinity, or the Godhead of any person of it, was to be punished with death and confiscation of all lands and goods. Reproachful speeches about the Virgin Mary or the apostles drew fines, then whipping, then banishment for repeat offences. And the act fined, at ten shillings an offence, anyone who called a neighbor a reproachful religious name, listing the vocabulary of a colony at odds with itself: heretic, schismatic, idolator, puritan, Jesuit, Lutheran, Calvinist, Anabaptist, Roundhead, separatist, and more. That list is evidence. A legislature does not ban insults nobody is shouting. Maryland in 1649 was a place where religion was the language of political violence, and the assembly answered by protecting worship between Christians and policing everything outside and between them. Protection and punishment were one policy, and students should say so in those terms.",
    kick='Section D · Penalties')

# ------------------------------------------------- 16 DIVIDER E
divider_text('Section E', 'Flushing: Conscience from Below',
    'Thirty one signatures against a governor, 1657',
    "Cross back north for the other face of toleration. Maryland's act was a grant from above, written by an assembly. The Flushing Remonstrance was a demand from below, written by farmers. Flushing, on Long Island, was an English town inside Dutch New Netherland, and Director General Peter Stuyvesant was then driving Quakers out of the colony, fining and imprisoning those who sheltered them. In 1657 he ordered Flushing not to receive or entertain any Quakers. The town's answer, dated December 27, 1657, is one of the earliest American documents of its kind: ordinary officeholders and residents telling their ruler, in writing, that an order crossed their consciences and their charter, and that they would not obey it. The next slide takes the remonstrance's arguments in the signers' own order, conscience first, then the law of love, then the patent. Ask students as you go: which of these arguments could Stuyvesant answer, and which could he only punish?")

# ------------------------------------------------- 17 CONTENT E
content_photo_s('map-port.jpg', 'The remonstrance and its grounds',
    ['The signers could not condemn the Quakers, because judgment belonged to God.', 'They claimed the law of love, peace, and liberty, extended to Jews, Turks, and Egyptians.', 'They claimed their town charter, and free coming and going in their town.', 'Stuyvesant arrested the clerk and punished signers; Amsterdam overruled him in 1663 and stopped the persecution.'],
    "The image is Visscher's map of New Netherland and New England, first issued in 1656 and reprinted in 1685, held by the Library of Congress and in the public domain; Flushing sits on Long Island, in the Dutch colony's English towns. The remonstrance rests on three grounds. First, conscience: the signers could not condemn the Quakers and could not stretch out their hands against them, because judgment belonged to God. Second, the law of love, peace and liberty, which they said extended in Holland even to Jews, Turks, and Egyptians, as sons of Adam, and condemned hatred, war, and bondage. Third, their patent: the town charter from the States General, which they were not willing to infringe. Stuyvesant arrested the town clerk, Edward Hart, and punished several signers. In 1663 the Dutch West India Company's directors overruled him from Amsterdam and ordered the persecution stopped. A petition had beaten a governor, on delay.",
    kick='Section E · The petition')

# ------------------------------------------------- 18 DIVIDER F
divider_text('Section F', 'Mercantilism and the Navigation Acts',
    'The theory, and the statutes that enforced it',
    "Now the frame that held all of these colonies, Dutch inherited, Quaker, Catholic, and petitioning alike. Mercantilism was the operating theory of every European empire in this period, and Britain's version ran on a simple measure: a nation's power grew as its stock of gold and silver grew, and colonies existed to feed that growth, sending raw materials home and buying finished goods back. What made the theory real was statute. Parliament began the Navigation Acts in 1651, in the Commonwealth period, aimed at the Dutch carrying trade that then dominated the Atlantic, and rebuilt them under Charles II in 1660 with the enumerated list. The next slide separates the two rules students must keep apart: the shipping rule, which governed whose hulls could carry colonial trade, and the enumeration rule, which governed where the best colonial goods could land. Almost everything about colonial prosperity and colonial grievance for the next century grows out of the difference between those two rules.")

# ------------------------------------------------- 19 CONTENT F
content_text('Two rules, one penalty',
    ['From 1651, colonial goods could move only in English or colonial ships.', 'The act of 1660 required English masters and crews three fourths English.', 'Enumerated goods, sugar, tobacco, cotton wool, indigo, and ginger among them, could land only in England or another English plantation.', 'Breaking either rule cost the cargo and the ship that carried it.'],
    "State the shipping rule first. From 1651, goods of Asia, Africa, and America could reach England only in ships belonging to the people of the Commonwealth or its plantations. The act of 1660 rebuilt the rule for the restored monarchy: colonial trade, in or out, moved only in English or colonial built and owned ships, with English masters and three fourths English mariners. Then the second rule. From April 1661, the enumerated goods, sugars, tobacco, cotton wool, indigo, ginger, fustic, and other dyeing wood, could be shipped from any English plantation only to another English plantation or to England, Ireland, Wales, or Berwick upon Tweed, there to be laid on shore. Both rules carried the same teeth: forfeiture of the goods and of the ship that carried them. Have students notice the word colonial inside the shipping rule. Parliament, meaning to shut out the Dutch, wrote colonial shipowners into the protected class, and that single word built an American merchant marine.",
    kick='Section F · The acts')

# ------------------------------------------------- 20 STAT
stat('3/4', 'of every crew had to be English by the act of 1660',
    'Masters English, ships English or colonial owned, or the cargo and the ship were forfeit',
    "Use this fraction to make the shipping rule concrete. Under the Navigation Act of 1660, a legal ship in the colonial trade needed an English master and a crew at least three fourths English, a category the acts defined to include colonial sailors. Bonds were posted, governors swore oaths to enforce the clauses, and warships were ordered to seize offenders and bring them into admiralty courts. On paper the system looks airtight, and students should feel its weight before they hear how practice differed. Customs houses were few, coastlines were long, governors depended on local goodwill, and merchants learned the profitable arts of false papers, quiet landings, and bribes. The practice does not cancel the law. Smugglers ran risks and paid costs precisely because the law existed, and enumerated planters who obeyed it watched Dutch and French buyers, who might have paid more, closed to them by statute. Hold both truths for Section G: a system enforced unevenly, whose unevenness was itself a colonial opportunity.",
    kick='Section F · Enforcement')

# ------------------------------------------------- 21 DIVIDER G
divider_text('Section G', 'One Atlantic Economy',
    'Cargoes in every direction, people above all in number',
    "Close the lesson by drawing the system whole, as the reading's last section does. The middle colonies sat at the crossing of three flows. Southward went their grain, flour, fish, and timber to the sugar islands, whose enslaved labor force grew sugar and grew little food. Northward came sugar and molasses to mainland ports, for sweetening, rum, and re-export. Westward from Britain came manufactured goods, cloth, tools, and guns, the cargoes the colonies were discouraged from making for themselves. And across the middle of the ocean came the flow this unit will not let the trade diagrams hide: enslaved Africans, carried by force from Africa to the Americas, the cargo on which the sugar end of the system rested. Lesson 6 takes that crossing apart from the records. This section keeps to the frame: how the flows fit together as one economy, which of them the Navigation Acts controlled, and which they left open for colonists to grow rich inside.")

# ------------------------------------------------- 22 CONTENT G
content_photo_s('holme-port.jpg', 'The grain trade: profit inside the rules',
    ['Grain was never enumerated, so colonial merchants could sell it openly in the sugar islands.', 'The islands needed food every year, because their land and labor went to cane.', 'Colonial ships counted as English under the acts, and Philadelphia grew rich on flour.', 'Smuggling ran beside the legal trade along a long coastline.'],
    "The image is Thomas Holme's Portraiture of the City of Philadelphia, printed in 1683, held by the Bibliotheque nationale de France and in the public domain: the grid Penn's port was built on, drawn the year after the city was laid out. The grain trade is the lesson's clearest case of growth inside the rules. Grain, flour, fish, and timber never appeared on the enumerated list, so a Philadelphia merchant could load them in a colonial built ship, with a legal crew, and sell them in Barbados or Jamaica at Caribbean prices, openly. The sugar islands' need was permanent, because land and labor there went to cane, not food. Add smuggling beside the legal trade, Dutch and French goods landed quietly along a long coastline, and the colonial picture completes itself: merchants were neither obedient nor simply rebellious. They were opportunists inside a system whose openings were as real as its walls, and the middle colonies, with the best farmland and two great ports, used the openings best.",
    kick='Section G · The openings')

# ------------------------------------------------- 23 STAT
stat('2.5 million', 'colonists by 1775, up from about 250,000 in 1700',
    'Both figures are estimates. The growth came mainly from births, a population doubling roughly every twenty five years',
    "End the content with the largest fact in the lesson, and label it as the reading does: both figures are estimates, drawn from contemporary counts and later demographic reconstruction, and students should repeat the word estimates whenever they use them. From about 250,000 people in 1700, the British mainland colonies grew to about 2.5 million by 1775, a tenfold rise in seventy five years, doubling roughly every twenty five years. Immigration continued, from Britain, Germany, and Africa by force, but the engine was natural increase: colonial families, marrying young on cheap land, raised more children to adulthood than families in Europe could. The middle colonies show the pattern in its richest form, farm country filling county by county while Philadelphia and New York grew into Atlantic ports. Whatever students conclude about mercantilism in the writing task, this growth is the background fact both sides must explain: it happened under the Navigation Acts, inside the empire's frame, not after an escape from it.",
    kick='Section G · The people')

# ------------------------------------------------- 24 AT A GLANCE
content_text('The lesson at a glance',
    ['New York was a Dutch colony under an English flag from 1664, its people unchanged.',
     'Pennsylvania grew from a charter and an invitation from 1681, on Lenape land bought in council.',
     'The Lenape, sellers with reasons of their own, were dispossessed by the walk of 1737.',
     'Toleration came from above in Maryland and from below at Flushing.',
     'Two trade rules fixed the richest cargoes, and the openings inside them built two great ports.'],
    "This slide mirrors the closing table in the guided notes, The Middle Colonies at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The five lines are the lesson's argument in miniature. A change of rulers in 1664 left a mixed Dutch society intact under an English proprietor. Penn's charter and printed invitation built a second mixture beside it, on land the Lenape sold in council for reasons of their own and lost, a generation later, to a fraudulent walk. Toleration came from two directions at once: an assembly's statute in Maryland, protection fenced by penalties, and a farmers' petition at Flushing that claimed conscience against a governor. And over everything, the Navigation Acts fixed the ships and the destinations of the richest cargoes, while leaving grain, timber, and colonial hulls free enough to build two great ports.",
    kick='Review')

# ------------------------------------------------- 25 VOCAB 1
vocab('Words for the colonies of many peoples', [
    ('middle colonies', 'the colonies of New York, New Jersey, Pennsylvania, and Delaware, known for fertile soil, busy ports, and peoples of many nations and faiths'),
    ('Quakers', 'members of the Society of Friends, a Protestant group that rejected formal ministers and oaths, held women and men spiritually equal, and faced persecution in England and New England'),
    ('William Penn', "the Quaker proprietor who received Pennsylvania's charter in 1681 and founded the colony as a holy experiment in government by his persecuted faith"),
    ('proprietary colony', 'a colony granted by the king to an individual or group who owned its land, appointed its governor, and drew its rents and fees')],
    "These definitions match the guided notes word for word, and students copy them exactly. middle colonies: the colonies of New York, New Jersey, Pennsylvania, and Delaware, known for fertile soil, busy ports, and peoples of many nations and faiths. Quakers: members of the Society of Friends, a Protestant group that rejected formal ministers and oaths, held women and men spiritually equal, and faced persecution in England and New England. William Penn: the Quaker proprietor who received Pennsylvania's charter in 1681 and founded the colony as a holy experiment in government by his persecuted faith. proprietary colony: a colony granted by the king to an individual or group who owned its land, appointed its governor, and drew its rents and fees. Note for the class that three of this lesson's colonies, New York, Pennsylvania, and Maryland, were proprietary in form, which is why their religious settlements took the shapes their proprietors allowed or their settlers forced.")

# ------------------------------------------------- 26 VOCAB 2
vocab('Words for the Atlantic system', [
    ('mercantilism', "the economic theory that a nation's power grows by accumulating wealth, especially gold and silver, exporting more than it imports, and holding colonies as sources of raw materials and captive markets"),
    ('Navigation Acts', 'the English laws, beginning in 1651, that required colonial trade to travel in English or colonial ships and required certain colonial goods to be sold only to England'),
    ('triangular trade', 'the pattern of trade across the Atlantic linking Europe, Africa, and the Americas, carrying manufactured goods, enslaved people, and colonial produce between them')],
    "Three more terms, again matching the guided notes exactly, and students copy them as written. mercantilism: the economic theory that a nation's power grows by accumulating wealth, especially gold and silver, exporting more than it imports, and holding colonies as sources of raw materials and captive markets. Navigation Acts: the English laws, beginning in 1651, that required colonial trade to travel in English or colonial ships and required certain colonial goods to be sold only to England. triangular trade: the pattern of trade across the Atlantic linking Europe, Africa, and the Americas, carrying manufactured goods, enslaved people, and colonial produce between them. Warn the class against using triangular trade as a neat diagram word only. Each side of the triangle was a lived route with crews, merchants, and, on the middle passage, captives, and Lesson 6 opens that leg of the pattern from the testimony of a man who survived it.")

# ------------------------------------------------- 27 SYNTHESIS
content_text('Synthesis: freest in conscience, routed in trade',
    ['Conscience was settled colony by colony, and often it was claimed from below, in petitions like Flushing\'s.',
     'Trade was ruled from London, by a theory written into statute.',
     'Colonists prospered in the openings the rules left, in grain, in timber, and in colonial hulls.',
     'The system grew the very colonies it exploited, from about 250,000 people in 1700 to about 2.5 million by 1775, both estimates.'],
    "Draw the lesson together by answering the lesson question in full sentences students can borrow. How did the middle colonies become the colonies of many peoples? By inheritance and by invitation: New York absorbed a Dutch trading society whole in 1664, and Penn's printed invitation, backed by wheat land and liberty of worship, drew Quakers, Germans, Welsh, and Scots-Irish settlers to Pennsylvania, on land bought from the Lenape in council while Penn lived. What held the Atlantic economy together? A theory, mercantilism, written into the Navigation Acts, which fixed colonial trade in English or colonial ships and reserved the enumerated goods to England, while the triangular trade bound Europe, Africa, and the Americas into one circuit of cargoes. The two halves meet in the lesson's closing judgment: the same colonies where conscience was argued out in petitions and assemblies had their richest trades routed by a parliament across the ocean, and they grew, in population from an estimated 250,000 in 1700 to an estimated 2.5 million by 1775, inside that arrangement.",
    kick='Synthesis')

# ------------------------------------------------- 28 EXIT
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.15, 11.5, 1.6, 'Answer the question, from the records',
     size=36, color=CREAM, font='Georgia', leading=1.15)
text(s, 0.9, 2.55, 11.5, 1.1, ['How did the middle colonies become the colonies of many peoples,',
                               'and what held the Atlantic economy together? Build from the documents.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Atlantic Ledger: five records, a ledger of interests, and a verdict'),
        ('Notebook', 'Notebook page: six parts in a chart, and two systems in one paragraph'),
        ('Quick check', 'Conscience and Cargo: the map, the act read whole, and the two cargoes'),
        ('Writing', 'Helped to Grow, or Held in Place? Argued from the ledger')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: why the middle colonies held many peoples, one protection and one penalty from 1649, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Atlantic Ledger, runs five records: the Flushing Remonstrance of 1657, quoted from the audited record; the Maryland Toleration Act of 1649, read whole with its penalty clause first; the Navigation Acts of 1651 and 1660, quoted from the Statutes of the Realm transcription named in the station; a labeled summary record of Penn's invitation and the Lenape purchase; and a teaching table of the Atlantic's cargoes. Students keep a ledger of whose interest each record served and whose it bound, and close with a verdict on whether mercantilism in practice helped the colonies grow or mainly held them in place, answering the strongest counterclaim. The quick check tests the charter and the map, Penn's land standard and its breaking in 1737, the Toleration Act read whole, and a merchant's two cargoes under the acts. The writing task asks the verdict question as an essay. The exit ticket asks why the colonies held many peoples, one protection and one penalty from 1649, and the lesson question with two dates.")

dc.save(OUT)
