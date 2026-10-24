#!/usr/bin/env python3
"""Colonial America Lesson 6 deck, "Slavery and the Slave Trade,"
built on the shared deck system. V2 (2026-10-24 rollout, improved slide
standard): content bullets are short complete sentences; speaker notes
applied after the build from the teacher notes guide (apply_guide_notes.py).
Same 27 slides, same order."""
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
OUT = os.path.join(HERE, '..', 'lesson-06-slides-v2.pptx')

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

# 1 TITLE
s = slide(NAVY)
photo_right(s, 'equiano-port.jpg')
text(s, 0.9, 1.5, 6.9, 0.4, 'COLONIAL AMERICA · LESSON 6', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 2.0, 6.9, 2.2, 'Slavery and the Slave Trade', size=44, color=CREAM, font='Georgia', leading=1.1)
rule(s, 0.92, 4.15)
text(s, 0.9, 4.5, 6.8, 1.6, 'How the trade was organized, and what enslaved people endured, built, and resisted', size=20, color=POWDER, leading=1.3)
notes(s, "The portrait is the frontispiece to Olaudah Equiano's Interesting Narrative, published in London in 1789, engraved by Daniel Orme. It opens the lesson because Equiano is its best witness: a man kidnapped as a boy in West Africa, carried across the Atlantic in a slave ship's hold, who bought his freedom and wrote the account that British abolitionists carried into Parliament. This hour teaches the Atlantic slave trade as a system, its ships, markets, statutes, and codes, and it teaches the people inside that system as actors: families held together against sale, rice knowledge that built a region's wealth, day to day defiance, flight, open revolt, and a published poem. Keep the tone documentary throughout. The numbers and the documents carry the weight, stated plainly and without heightening.")

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How was the Atlantic slave trade organized, and what did enslaved people endure, build, and resist?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the meeting of Europe, Africa, and the Americas remake all three worlds, and what kind of society grew up in England\'s colonies?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "The lesson question has two halves, and students should hear both before the first section begins. The first half asks how the trade was organized, which is a question about machinery: ships and coastal markets, colonial demand, and the statutes and codes the assemblies wrote to make enslavement permanent. The second half asks what enslaved people endured, built, and resisted, which is a question about people acting inside that machinery: enduring the crossing, building families, languages, and skills, and resisting at every scale from a slowed work gang to an armed march. Neither half answers the question alone. A system with no people in it is an abstraction, and people with no system around them cannot be understood. The unit question runs beneath as the frame: this lesson is where the meeting of the three worlds shows its hardest face.")

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'A system, and the people inside it', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'A trade built on captives', 'Ships, coasts, and colonial demand'),
        ('B', 'The Middle Passage in Equiano\'s words', 'The hold, described by a survivor'),
        ('C', 'The law that made slavery hereditary', 'Virginia, 1662 and 1667; the codes'),
        ('D', 'The Chesapeake: tobacco and families', 'Gang labor, and kin held against sale'),
        ('E', 'The lowcountry: rice, tasks, a Black majority', 'African knowledge, Gullah formed'),
        ('F', 'The North, and resistance every day', 'No region outside it; defiance daily'),
        ('G', 'Stono, the Negro Act, and Wheatley\'s voice', 'Revolt, the code, and a poem of 1773')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A sets out the trade's organization and its scale. Section B puts students inside the crossing with the one witness whose account the record keeps whole. Section C reads the two Virginia statutes that made slavery hereditary and the codes that followed. Sections D and E compare the two great regional worlds slavery made, the Chesapeake and the lowcountry. Section F states the North's part plainly and takes up everyday resistance and flight. Section G closes with open revolt, the law that answered it, and Phillis Wheatley's poem of 1773, read entire in the activity. Tell students the summary table at the end of their guided notes, The System at a Glance, asks them to rebuild exactly this map.")

# 4 A DIVIDER
divider_text('Section A', 'A Trade Built on Captives',
             'Guns, cloth, and metal to the Guinea coast; captives to the plantations of the Americas.',
             "Set the chain out in order before any numbers are introduced. European ships carried guns, cloth, and metal goods to the Guinea coast of West Africa. There, African rulers and merchants sold war captives and kidnapped people to the traders, and students should hear that fact stated plainly, along with its limit: the scale of the trade, the ships waiting offshore, and the American plantations at the end of the route were the buyers' creation, and demand from the Americas set the price that made the selling grow. Captives were held in coastal forts and barracoons and carried below deck. At the far end stood the demand: sugar plantations in Brazil and the Caribbean took the largest share of the captives, and tobacco and rice plantations in England's colonies took much of the rest. Section A of the guided notes holds this sequence, and the next slide puts the Database's figures on it.")

# 5 A CONTENT
content_text('The chain, link by link',
             ['European merchants financed voyages and insured cargoes of human beings.',
              'African rulers and merchants sold war captives and the kidnapped, into a commerce European and colonial demand had built.',
              'Captives were held in coastal forts and barracoons and carried below deck.',
              'Sugar plantations in Brazil and the Caribbean took the largest share.',
              'Tobacco and rice plantations in England\'s colonies took much of the rest.'],
             "Work the chain slowly, because students often compress it into ships appearing on a coast. Each link had people making decisions. European merchants financed voyages and insured cargoes of human beings. African rulers and merchants sold war captives and the kidnapped, a participation the reading states without letting it soften what the buyers built, because it was European and colonial demand that turned older forms of captivity into an Atlantic commerce of millions. Planters in the Americas placed the orders that set the whole chain in motion, buying bound labor for life because it returned more than servants who went free. Colonial assemblies then protected the purchase in law, which is where Section C will pick the story up. Have students keep the destinations in order in section A of the notes: Brazil and the Caribbean first, the mainland colonies after, because the mainland's share, large as it was, was not the trade's center.",
             kick='A · A trade built on captives')

# 6 A STAT
stat('12.5 million', 'people forced aboard slave ships, by the Trans-Atlantic Slave Trade Database\'s estimates',
     'About 10.7 million survived the crossing, between the 1500s and the 1800s',
     "Let the two figures stand together and name their source every time they are used: they are estimates from the Trans-Atlantic Slave Trade Database, which has reconstructed the trade voyage by voyage from shipping records. About 12.5 million Africans were forced aboard slave ships between the 1500s and the 1800s. About 10.7 million survived the crossing to be sold in the Americas. The difference, about 1.8 million people, died aboard, and Section B is about the conditions that killed them. Students should also register the span: this was not one generation's crime but a commerce sustained across three centuries, outliving the colonies that built it, the Revolution, and the founding of the United States. When students cite these numbers in the writing task, the Database's name goes with them, because an estimate with a source can be checked and an unattributed number cannot.",
     kick='A · A trade built on captives')

# 7 B DIVIDER
divider_text('Section B', 'The Middle Passage in Equiano\'s Words',
             'The crossing lasted from about six weeks to three months. One survivor described it.',
             "Introduce the witness before the account. Olaudah Equiano was kidnapped in Igboland at about eleven years old, carried first to Barbados and then to Virginia, sold again to a naval officer and a merchant, and bought his freedom in 1766. In London in 1789 he published The Interesting Narrative, which became the abolition movement's central first person evidence against the trade. The passage students will read in the activity comes from that narrative as the audited TPSP bank carries it, from the London 1789 first edition by way of Documenting the American South. Section B teaches the crossing from his sentences: the crowding, the air, the sickness, and his own verdict on who was responsible. Tell students why a single witness carries this section: for most voyages, the only written records are the traders' own logs and accounts, and Equiano is the crossing's best known survivor author.")

# 8 B CONTENT PHOTO (Brookes plate)
content_photo_s('brookes-port.jpg', 'Stowed under a regulation act',
             ['The Brookes plate was printed in 1788 by abolitionists, drawn to persuade.',
              'After the act of 1788 the ship was allowed 454 people.',
              'On an earlier voyage she had carried 609, stowed spoonwise.',
              'The plate allows each man six feet by one foot four inches.'],
             "The image is a portrait crop of the plate whose printed title is Stowage of the British Slave Ship Brookes under the Regulated Slave Trade Act of 1788, printed in 1788 by the Society for Effecting the Abolition of the Slave Trade and held by the Library of Congress. Teach it as an argument, not as a neutral diagram: abolitionists drew the stowage plans to show the British public, in measured feet and inches, what the trade did with human beings. The plate's own note states that after the act the Brookes was allowed 454 people, allowing six feet by one foot four inches to each man, and that before the act she had carried as many as 609, stowed spoonwise. Set the plate beside Equiano's account deliberately. The plate gives the space; Equiano gives what the space felt like, the heat, the foul air, and the sickness. Neither replaces the other, and the activity's first station asks students to say why.",
             kick='B · The Middle Passage')

# 9 B STAT
stat('1.8 million', 'people died aboard the ships, by the Database\'s estimates',
     'Equiano laid the deaths on the improvident avarice of their purchasers',
     "This figure is the difference between the Database's two estimates, the 12.5 million forced aboard and the about 10.7 million who survived, and students should be able to show that arithmetic rather than recite a third memorized number. Then give Equiano's interpretation of it, because he did not treat the deaths as weather. He wrote that the captives died falling victims to the improvident avarice, as he put it, of their purchasers: improvident, reckless, avarice, greed. The buyers packed ships past what air and space could sustain because each person landed alive was profit, and the deaths followed from the packing. Crews threw the dead into the sea, and survivors were sold at auction or by scramble in American ports, separated from the shipmates who had become their only family on the voyage. Section B of the guided notes asks for the crossing's length, six weeks to three months, and this figure, and both belong in the students' own words.",
     kick='B · The Middle Passage')

# 10 C DIVIDER
divider_text('Section C', 'The Law That Made Slavery Hereditary',
             'Virginia, December 1662 and September 1667: status follows the mother; baptism does not free.',
             "Frame the legal problem the assemblies faced, in their own terms. English law had no settled place for slavery for life, and the first Africans in Virginia had held a range of statuses. As tobacco planters shifted from indentured servants to enslaved Africans in the decades after Bacon's Rebellion began to loom, the assembly wrote the system's foundations in two short statutes, five years apart. The first settled the status of children. The second settled the claim of Christian conversion. Between them, they converted slavery from a condition that befell individuals into a hereditary caste that reproduced itself. Section C quotes both statutes in the activity from Hening's Statutes at Large, in their original spelling, because the students should see that this was done in ordinary legislative language, by vote, on the record. Nothing about the system's permanence was an accident or a custom that drifted in unowned.")

# 11 C CONTENT
content_text('Two statutes, two doors closed',
             ['In 1662 Virginia ruled that children were held bond or free by the condition of the mother.',
              'The rule reversed English law, which ran status through the father.',
              'In 1667 the assembly declared that baptism does not alter bondage or freedom.',
              'Conversion was closed as a road to liberty, and children were born enslaved for life.'],
             "Read the 1662 statute's opening case aloud, because the act states it without embarrassment: doubts had arisen whether children got by any Englishman upon a Negro woman should be slave or free, and the assembly answered that all children borne in this country shall be held bond or free only according to the condition of the mother. Note the reversal. English law ran status through the father; Virginia ran enslaved status through the mother, which freed English fathers of consequence and made enslaved women's children property from birth. The 1667 act then declared that the conferring of baptism does not alter the condition of the person as to bondage or freedom, in the act's own words, so that masters, freed from this doubt, might permit enslaved children to be baptized without risking their property. Together the two statutes are the legal birth certificate of hereditary racial slavery in England's colonies.",
             kick='C · The law', size=24)

# 12 C CONTENT 2
content_text('Codes on the statutes\' foundation',
             ['The codes defined enslaved people as property in law.',
              'Enslaved people were denied courts, assembly, and arms.',
              'A written pass was required to leave a plantation, enforced by patrols of white men.',
              'Resistance was punished, up to death, and the codes tightened across the late 1600s and 1700s.'],
             "On the foundation of 1662 and 1667 the colonies built the slave codes, colony by colony, tightened across the late 1600s and early 1700s after every alarm. An enslaved person could not testify against a white person in court, could not gather in groups without permission, could not carry a weapon, and could not leave the plantation without a written pass or ticket. Patrols of white men, slaveholders or not, enforced the passes, which made every white colonist an agent of the system whether he owned anyone or not. South Carolina's version, the Negro Act of 1740, is quoted in the activity and returns in Section G, because it was written in direct answer to the Stono Rebellion. Have students hold the sequence clearly: statutes first, making the caste hereditary; codes after, policing it; and each tightening traceable to enslaved people's own actions, which the codes themselves record by forbidding them.",
             kick='C · The law', size=24)

# 13 D DIVIDER
divider_text('Section D', 'The Chesapeake: Tobacco and Families',
             'Gang labor in the tobacco fields, and a population that grew by birth from the early 1700s.',
             "Move from law to lived worlds, and keep the two regions of Sections D and E distinct, because the unit test asks students to contrast them. The Chesapeake, Virginia and Maryland, worked tobacco. Enslaved people labored in gangs from sunup to sundown through the crop's year, planting, weeding, worming, cutting, and curing, and skilled men and women worked beside the fields as carpenters, coopers, blacksmiths, and cooks, whose labor planters rented out for profit. The region's defining fact is demographic: by the early 1700s its enslaved population grew by birth more than by new arrivals from Africa, one of the few places in the Americas where that was true. Growth by birth changed what enslaved life could build, and the next slide takes up what it built: families, maintained deliberately, under a threat that never lifted.")

# 14 D CONTENT
content_text('Families, held against sale',
             ['Enslaved parents named their children for grandparents and kin, in Africa and in Virginia.',
              'Couples held marriages the law refused to recognize.',
              'Family lines ran across neighboring plantations, joined by pass and by stealth.',
              'An owner\'s death, debts, or divided estate could sell anyone away at any time.',
              'Holding a family together was itself work.'],
             "Teach the family as an achievement, not as a background condition. Enslaved parents named their children for grandparents and kin, in Africa and in Virginia, carrying memory across the crossing in the names themselves. Couples held marriages that the law refused to recognize, which meant no marriage they made could bind an owner, and built family lines across neighboring plantations, visiting by pass and by stealth. Against all of it stood the market: an owner's death, his debts, or an estate divided among heirs could sell a husband, a wife, or a child away at any time, and sales broke families in every generation. Students should be able to state both halves in section D of the notes, the building and the threat, because the writing task's evidence bank carries this row of the lesson and rewards answers that hold the two together.",
             kick='D · The Chesapeake', size=24)

# 15 E DIVIDER
divider_text('Section E', 'The Lowcountry: Rice, Tasks, and a Black Majority',
             'South Carolina and Georgia: rice wealth built on African knowledge, in a country where the enslaved were the majority.',
             "No period image of lowcountry rice work that this lesson could verify in the public domain is used in this deck, so the section is taught in words and in the documents, and the sources file says so plainly. Set the region's foundations. South Carolina and Georgia grew rich on rice, a crop English planters did not know how to grow. Enslaved people from West Africa's rice coasts knew it entire: how to dike tidal marshes, build the banks and floodgates, flood and drain fields on the tide, and time the crop to the water. Planters paid higher prices for captives from those regions for exactly that knowledge, which means the lowcountry's wealth rested on skills the buyers themselves recorded in their prices. White owners often left the malarial lowcountry in the sickly season, and enslaved drivers and workers ran the plantations for long stretches. The next slide takes up the labor system that ordered the day.")

# 16 E CONTENT
content_text('The task system',
             ['Each worker was assigned a measured daily task.',
              'When the task was finished, the remaining hours were the worker\'s own.',
              'Those hours went to gardens, poultry, hunting, fishing, and produce sold in Charleston\'s markets.',
              'The hours were a customary claim enslaved people defended in practice, year after year.'],
             "Define the task system precisely, because the unit test draws the definition from the guided notes: a worker was assigned a daily task, a measured piece of ground or a set amount of labor, and when it was finished, the remaining time was the worker's own. A fast, skilled worker could finish by mid afternoon. Those hours were used, for garden plots and poultry of their own, for hunting and fishing, and for produce sold in Charleston's markets, where enslaved sellers were a fixture the town's ordinances kept trying to regulate. Do not let students mistake the arrangement for generosity. The task was set by the driver, the pace was enforced, and the hours after the task were a customary claim enslaved people defended in practice, year after year, until custom gave it the force of a right they could invoke. It is one of the clearest places in the lesson where enslaved people converted a labor system into ground of their own.",
             kick='E · The lowcountry', size=24)

# 17 E CONTENT 2
content_text('A Black majority, a new culture',
             ['In the lowcountry, enslaved people outnumbered white colonists.',
              'Gullah, a language and culture joining African grammar to English words, took form there.',
              'African languages, faiths, foods, and crafts crossed in the ships as knowledge in people\'s heads.',
              'The Negro Act of 1740, banning assembly, drums, and horns, was aimed at this community\'s life.'],
             "In the lowcountry, enslaved people outnumbered white colonists, and in parishes along the coast the majority ran far higher. In that majority, a new language and culture took form: Gullah, joining African languages and grammar to English words, and carrying African faiths, foods, crafts, and music into new American forms. Rice work itself, the dike and floodgate knowledge, the basketry of the fields, the foodways of rice and okra and black eyed peas, all crossed in the holds of the ships as knowledge in people's heads, which no manifest recorded. Hold this slide's last fragment for Section G: the Negro Act of 1740, with its bans on assembly, drums, and horns, was aimed at exactly this community's life, at the meetings and music where its organization lived. The act is therefore evidence for the culture as well as against it, slaveholders testifying in law to what the enslaved had built.",
             kick='E · The lowcountry', size=24)

# 18 F DIVIDER
divider_text('Section F', 'The North, and Resistance Every Day',
             'Slavery in every colony, and defiance beside the work, daily, everywhere.',
             "Begin by closing the regional escape hatch. Slavery was smaller in the northern colonies and present in all of them, and no region of British America stood outside the system. Enslaved people worked farms in New England and the middle colonies, loaded ships in Boston, New York, and Newport, cooked and cleaned in households, and crewed vessels in the trade itself, including the New England rum ships that sailed for the Guinea coast. Rhode Island ports were among the trade's American centers. Students who place slavery only in the South will misread the rest of this course, from the Constitution's bargains to the sectional crisis, so Section F states the North's part in the reading's plain terms before it turns to resistance. The resistance that follows is likewise everywhere, not a southern specialty: wherever people were held, the work was contested.")

# 19 F CONTENT
content_text('Defiance, flight, and the run for Florida',
             ['Enslaved people slowed labor, broke tools, feigned sickness, and took food their labor had produced.',
              'They kept African names for their children and buried their dead by their own rites.',
              'They learned to read where they could, against laws and custom.',
              'Flight ran to swamps, to towns, and south to Spanish Florida, whose governors promised freedom.'],
             "Teach resistance as a spectrum with the daily end first, because that is where most of it lived. Enslaved people slowed the pace of labor, broke tools, feigned sickness, and took food their labor had produced, acts owners recorded in their complaints as laziness and theft, which students should learn to read as the record of a contest. They kept African names for their children, buried their dead by their own rites, and learned to read where they could, against laws and custom. Then flight: to swamps and woods near home, where kin could feed a runaway for weeks; to towns, where free Black communities might hide them; and south to Spanish Florida, whose governors promised freedom to fugitives from the English colonies who accepted Catholic baptism. Every flight cost owners and patrols time and money. The system never held quietly, and the next section shows the day it did not hold at all.",
             kick='F · Resistance every day', size=24)

# 20 G DIVIDER
divider_text('Section G', 'Stono, the Negro Act, and Wheatley\'s Voice',
             'September 1739: an armed march for Florida. 1740: the code that answered it. 1773: an enslaved poet in print.',
             "Close the lesson with the era's fullest sequence of action and answer. In September 1739, enslaved Africans near Charleston rose in the largest rebellion of the colonial mainland, seized weapons, and marched for the freedom Spanish Florida promised. South Carolina answered within the year with the Negro Act of 1740, the most complete slave code in this lesson, and the activity quotes its declarations directly. A generation later, the era produced a different kind of record: Phillis Wheatley, kidnapped from West Africa as a child and enslaved in Boston, published a book of poems in London in 1773, the first book by an African American poet, and one eight line poem in it answers the system's defenders from their own doctrine. Section G holds all three records together, revolt, code, and poem, because each explains the others: the code shows what the revolt frightened, and the poem shows what the code could not confiscate.")

# 21 G CONTENT
content_text('September 1739: the march south',
             ['On Sunday, September 9, 1739, enslaved men seized guns and powder near the Stono River.',
              'They marched south under banners, calling out for liberty, on the least watched day of the week.',
              'The column grew as it marched toward Spanish Florida.',
              'The militia caught it the same day; most marchers were killed or executed.'],
             "State the rebellion plainly and in order. On Sunday, September 9, 1739, enslaved men took guns and powder from a store near the Stono River, about twenty miles from Charleston, killed the storekeepers, and marched south under banners, calling out for liberty, recruiting as they went. The choices were strategy: Sunday was the day of markets, visits, and worship, the least watched day of the lowcountry week, and south led to Spanish Florida and its promised freedom. The colony's militia caught the column the same day, and most of the marchers were killed in the fighting or executed after it. Give the scale its due: this was the largest slave uprising in the British mainland colonies in the colonial period, carried out by people who knew the patrols, the distances, and the odds. Section G of the guided notes asks for the river, the year of the answering act, and the act's ban on teaching writing, and all three belong in students' answers.",
             kick='G · Stono', size=24)

# 22 G CONTENT 2
content_text('The act of 1740, and a voice of 1773',
             ['The Negro Act of 1740 banned assembly, movement without a ticket, and earnings.',
              'Teaching an enslaved person to write drew a fine of one hundred pounds.',
              'Phillis Wheatley, kidnapped as a child and enslaved in Boston, published her poems in London in 1773.',
              'Her eight-line poem holds gratitude and accusation in the same breath.'],
             "Pair the code and the poet deliberately. The Negro Act of 1740 forbade enslaved people to assemble, to move without a ticket, to earn money, or to be taught to write, fining the teacher one hundred pounds current money, and it set up separate courts for the enslaved; it governed South Carolina for generations. Its writing clause admits what the system feared, that a literate enslaved population could forge passes, read notices, and correspond. Then Wheatley: kidnapped as a child, enslaved in Boston, taught to read in the household that held her, and published in London in 1773 because Boston publishers had refused her book. Her poem On Being Brought from Africa to America, read entire in Station 5 of the activity, calls the crossing mercy for the faith it taught her and then orders her Christian readers to remember that Negros, black as Cain, may be refined and join the angelic train. The code fined writing; the poem is what writing did.",
             kick='G · Stono, the act, and Wheatley', size=24)

# 23 GLANCE
s = slide(NAVY)
kicker(s, 'The system at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Each part, and what people did inside it', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The trade', 'Ships, coasts, colonial demand', '12.5 million aboard; Equiano\'s witness'),
        ('The law', 'Hereditary status, codes, passes', 'Families and reading pressed every seam'),
        ('The regions', 'Tobacco gangs; rice tasks', 'Kin held in one; Gullah formed in the other'),
        ('Resistance and voice', 'Defiance, flight, Stono', 'A London book in 1773 answered the codes')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the summary table at the end of the guided notes, The System at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. Read the rows as a single account rather than four summaries. The trade supplied the people, organized by ships, markets, and colonial demand. The law made their condition hereditary and policed it with codes and passes. The regions gave that condition two different daily shapes, gang labor in tobacco and the task system in rice. And inside every part, enslaved people acted: holding families, keeping names and rites, turning task hours to their own uses, forming a language, running, rising, and writing. Grade the table generously on wording and strictly on completeness: every row needs the system's working and the people's answer to it.")

# 24 VOCAB A
vocab('Words for the trade and the crossing',
      [('Atlantic slave trade', '12.5 million carried; about 10.7 million survived'),
       ('Middle Passage', 'the crossing itself, six weeks to three months'),
       ('Olaudah Equiano', 'kidnapped, freed, author of the 1789 narrative'),
       ('chattel slavery', 'people held as property, children born enslaved')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. Atlantic slave trade: the forced migration of Africans across the Atlantic in slave ships, which carried some 12.5 million people from Africa between the 1500s and the 1800s, about 10.7 million of whom survived the crossing. Middle Passage: the voyage across the Atlantic that carried enslaved Africans to the Americas, the middle leg of the Atlantic trade, made in crowded ships where disease and abuse killed many of those aboard. Olaudah Equiano: the African writer who was kidnapped as a boy, enslaved, bought his freedom, and published in 1789 a narrative that described the Middle Passage and argued against the slave trade. chattel slavery: the system in which enslaved people were legally treated as property, bought, sold, and inherited, and in which their children were born enslaved for life. Note the order: the commerce, the voyage, the witness, and the legal condition the voyage delivered people into.")

# 25 VOCAB B
vocab('Words for the law, the labor, and the rising',
      [('slave codes', 'the laws that policed the system'),
       ('task system', 'a daily task, then time of their own'),
       ('Stono Rebellion', 'September 1739, the march for Florida')],
      "Three more terms, again matching the guided notes exactly. slave codes: the laws that defined enslaved people's legal status, denied them rights to courts, assembly, and arms, and punished resistance, tightened in the colonies across the late 1600s and early 1700s. task system: the labor system of the South Carolina and Georgia lowcountry in which enslaved workers were assigned a daily task and, when it was finished, had the remaining time for their own work. Stono Rebellion: the uprising of September 1739 near Charleston, South Carolina, in which enslaved Africans seized weapons and marched toward Spanish Florida, after which the colonies tightened their slave codes. Read the set as the lesson's second half in miniature. The codes state the law's claim. The task system names the lowcountry's daily order, inside which enslaved people carved out hours of their own. Stono names the day the claim and the order were challenged in arms, and the tightening that followed is inside the codes' definition itself.")

# 26 SYNTHESIS
content_text('Judging the system whole',
             ['The trade was organized as a system of ships, markets, statutes, and codes.',
              'Enslaved people endured the hold, the gang, and the standing threat of sale.',
              'They built rice wealth, families, the Gullah language, and a book in print.',
              'They resisted by daily defiance, by flight, and at Stono in arms.',
              'The writing task asks for both halves of the record in one argument.'],
             "Close the teaching here, before the work slide, and model the judgment the writing task will ask for. The trade was organized as a system, and systems language, tonnage, statutes, prices, is true as far as it goes. It does not go all the way. The same record that holds the statutes holds the rice knowledge in the planters' own prices, the names given to children, the language formed in the lowcountry, the column marching south under banners, and an enslaved poet published in London in 1773. The strongest student writing holds both records at full strength in one argument, and can say what each proves: the first, that enslavement was built deliberately, in law, by named assemblies; the second, that the people it was built on were never the passive material the statutes described. Dismiss either half and the lesson has been halved with it.",
             kick='Synthesis', size=24)

# 27 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How was the Atlantic slave trade organized, and what did enslaved people endure, build, and resist? Build the file first, then judge from it.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The System in Five Records: five stations, a file, and a verdict on the record no reader may skip'),
        ('Notebook', 'Notebook page: the system charted in five parts, and the system in one paragraph'),
        ('Quick check', 'The Brookes Plate, 1788: the plate and its note, the estimates, the statutes, the task system'),
        ('Writing', 'Endure, Build, Resist: the system weighed against the people inside it, from both halves of the bank')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the two statutes of the 1660s, the Database\'s arithmetic in full, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The System in Five Records, runs five stations: Equiano's Middle Passage account from the audited bank record, with the Brookes plate captioned by its own printed title and its abolitionist purpose; Virginia's statutes of 1662 and 1667 from Hening's Statutes at Large; the Negro Act of 1740 from McCord's Statutes at Large of South Carolina; a labeled teaching summary of Stono beside the act's own words on assembly; and Wheatley's poem of 1773 printed entire. Students build the file in Part 2 and defend a verdict on the record no reader may skip. The notebook page charts the same five parts. The quick check works from the Brookes plate and its printed note. The writing task turns the lesson question into an essay drawn from both halves of its bank. The exit ticket has three parts: the two statutes and what each did, the Database's arithmetic in full, and the lesson question answered with one organization fact and one building or resistance fact.")

dc.save(OUT)
