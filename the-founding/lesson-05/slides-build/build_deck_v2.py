#!/usr/bin/env python3
"""The Founding Lesson 5 deck, "Winning and Losing: The War's Home Fronts
and Its Peoples," built on the shared deck system: image-led slides,
Short complete sentences on content slides in V2 (2026-10-24 rollout);
speaker notes applied after the build from the teacher notes guide
(apply_guide_notes.py). Same 29 slides, same order."""
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

def content_photo_s(img, title, items, note, kick=None):
    s = slide(CREAM)
    photo_right(s, img)
    if kick: kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95 if kick else 0.8, 6.9, 1.2, title, size=30, color=NAVY, font='Georgia', leading=1.05)
    frags(s, items, y=2.12 if kick else 2.0, size=21, gap=11, leading=1.2)
    notes(s, note)
    return s

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

# 1 TITLE
s = slide(NAVY)
photo_right(s, 'edenton-port.jpg')
text(s, 0.9, 1.5, 6.9, 0.4, 'THE FOUNDING · LESSON 5', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 2.0, 6.9, 2.2, 'Winning and Losing', size=44, color=CREAM, font='Georgia', leading=1.1)
rule(s, 0.92, 4.15)
text(s, 0.9, 4.5, 6.8, 1.6, 'The war\u2019s home fronts and its peoples: who else fought, paid, and waited through the war, and what its promise meant to them', size=20, color=POWDER, leading=1.3)
notes(s, "The image is a London mezzotint of March 1775, A Society of Patriotic Ladies at Edenton in North Carolina, a British satire of American women signing a boycott resolve. It opens the lesson because this hour widens the war. The last lesson followed armies and campaigns: Saratoga, the French alliance, Yorktown. This lesson asks who else the war ran through. It follows the households that paid for it in depreciated money and requisitioned food, the women who worked in its camps and in a few cases in its ranks, the Black Americans who read its promises against their own condition and acted on both sides, the Native nations who chose sides to shield their land, and the Loyalists who lost the country the war made. Keep the figures labeled as the reading labels them. The numbers in this lesson are estimates, and the lesson says so wherever they appear.")

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('Who else fought, paid, and waited through the war, and what did its promise mean to them?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('Why did the colonies break with Britain, and what did Americans build in the place of the empire they rejected?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "The lesson question has three verbs, and students should hear all three before the first section begins. Fought: this lesson's soldiers include camp followers under fire, Margaret Corbin at a cannon, Deborah Sampson in the light infantry, Black soldiers in two armies, and Haudenosaunee warriors on both sides. Paid: the war was paid for by households, in paper money that wasted away, in food and wagons requisitioned, in estates confiscated, and in towns and cornfields burned. Waited: the lesson is full of people who were promised something by the era's language and then waited to see whether the promise would be kept, Abigail Adams writing to her husband, enslaved petitioners writing to a legislature, Black Loyalists trusting a British ledger at the evacuation. The second half of the question asks what the promise meant to each of them, and the documents, not the armies, carry that half.")

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'A war with more peoples in it than two armies', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'A war run by civilians', 'Paper money, requisitions, households'),
        ('B', 'The armies\u2019 own households', 'Camp followers; Corbin, Sampson, Hays'),
        ('C', 'Women thinking politically', 'Edenton 1774; Abigail Adams 1776'),
        ('D', 'Black Americans\u2019 war', 'Dunmore\u2019s offer; flight; five thousand serve'),
        ('E', 'Native nations\u2019 war', 'A confederacy divided; Sullivan 1779'),
        ('F', 'The Loyalists\u2019 war', 'Oaths, confiscation, the evacuation'),
        ('G', 'The reckoning the promises demanded', 'Petitions, courts, gradual emancipation')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A pays for the war: paper money, inflation, requisitions, and the households that carried it. Section B staffs the armies, with the camp followers and the women who fought outright. Section C takes up women claiming a political voice, at Edenton in 1774 and in Abigail Adams's letter of 1776. Section D is the lesson's center, Black Americans' war, from Dunmore's Proclamation to the five thousand who served the United States. Section E follows the Haudenosaunee split and the Sullivan expedition. Section F follows the Loyalists through confiscation to the evacuation. Section G closes with the reckoning: the petitions, the first emancipations, and Washington's letter of 1786 beside his own record. Tell students the summary table at the end of their guided notes, The War's Peoples at a Glance, asks them to rebuild exactly this map.")

# 4 A DIVIDER
divider_text('Section A', 'A War Run by Civilians',
             'Congress could not tax. It printed money, and the money wasted away in the country\u2019s hands.',
             "Begin with the war's missing machinery. The Continental Congress could declare war, raise an army, and borrow, but it could not tax, because taxation without representation was the grievance the war was being fought over. So it paid in paper: bills of credit printed in growing quantities, which every holder watched sink in value. Students should connect this to their own experience of prices before the vocabulary slide gives them the word inflation. The states filled the gap with requisitions, demands for food, wagons, and horses laid on particular farms and towns, which fell hardest on the country the armies had already marched through and stripped. Armies of both sides also took what they needed directly. Section A of the guided notes asks for the chain in order: no power to tax, printed paper, hundreds in paper for a dollar in coin, requisitions, and at the end of the chain a household, usually run by a woman, making the arithmetic work.")

# 5 A CONTENT
content_text('Paying for a war without taxes',
             ['Congress printed paper money to pay and supply the army.',
              'The bills sank: hundreds in paper for a dollar in coin.',
              'Not worth a Continental entered the language.',
              'States requisitioned food, wagons, and horses.',
              'Prices were fixed by law, and evaded in practice.'],
             "Work the depreciation slowly, because students tend to hear inflation as a modern abstraction. A soldier was paid in paper, a farmer was paid in paper for requisitioned grain, and by the time either man spent it, the paper bought less than it had when he took it. The phrase not worth a Continental survives because everyone who handled the money learned it. Prices fixed by law did not stop the slide: sellers withheld goods, sold quietly at market prices, or refused paper where they dared, and enforcement set neighbors against each other in town meetings and committees. Do not let the section become a story about a worthless currency alone. Behind every requisition receipt stood a farm that had already given sons, horses, and harvests to one army or the other. The household end of that chain is the next slide, and it is where Section A does its real work.",
             kick='A · A war run by civilians')

# 6 A CONTENT 2
content_text('Households carried the war',
             ['Wives ran farms and shops with the men gone.',
              'Boycotts and homespun worked as political acts.',
              'Food, fuel, and nursing were supplied at home.',
              'In Philadelphia in 1780 money was raised door to door.',
              'The money bought shirts for soldiers who had none.'],
             "Name the labor precisely. With husbands, sons, and hired hands gone, women ran farms through planting and harvest, kept shops and trades open, managed debts and hired help, and decided what a family could spare when a requisition party or a foraging party came to the door. The boycott, which students met in Lesson 1 as a merchant's instrument, was made real in households: refusing British cloth and wearing homespun were political acts performed at the spinning wheel and the loom, mostly by women. The Philadelphia campaign of 1780 makes the scale visible. Women organized a door to door subscription across the city and raised money to buy shirts for soldiers who had gone without them, one of the war's clearest cases of civilian organization doing what Congress's finances could not. Section A of the notes ends with Philadelphia for exactly this reason.",
             kick='A · A war run by civilians', size=24)

# 7 B DIVIDER
divider_text('Section B', 'The Armies\u2019 Own Households',
             'The camp followers, in the thousands, cooked, washed, nursed, and carried, for rations and little or no pay.',
             "Introduce the armies' other population. Every army in this war traveled with a tail of women and children, wives, widows, laundresses, cooks, nurses, and sutlers' families, who were issued rations because the army expected their work. Students often picture the camp follower as a camp rumor; the record is drier and stronger. Muster rolls and ration returns list them, officers' orders regulate them, and the reading states the conclusion plainly: neither army could have moved or fed itself without them. They were present in danger as well as in camp, carrying water and cartridges toward the guns under fire. Section B then follows three named women out of that population and into the line of battle itself. Keep Margaret Corbin, Deborah Sampson, and Mary Ludwig Hays distinct in students' minds, because the next slides turn on the difference between their records.")

# 8 B CONTENT PHOTO
content_photo_s('sampson-port.jpg', 'A workforce the armies depended on',
             ['Women and children traveled with the armies in the thousands.',
              'They cooked, washed, nursed, and sewed.',
              'Water and cartridges were carried under fire.',
              'Rations were issued; pay was little or nothing.',
              'They were present with both armies, all war long.'],
             "The portrait is Deborah Sampson, from the frontispiece engraving of Herman Mann's biography, The Female Review, published in 1797, held by the Library of Congress. Use her face to introduce the population this slide counts, because she began her war inside it: the work listed here, cooking, washing, nursing, and carrying, was the ordinary work of the thousands of women who traveled with the Continental and British armies. Teach the rations point carefully. Camp followers drew rations from the army's stores, which means the army formally counted on their labor and fed it, while paying little or nothing for it in wages. Some were soldiers' wives following one man; many were workers following an army because the army was where the food and the wages of any kind were. When students reach the quick check and the writing task, the phrase to listen for is the guided notes' own: a workforce the armies depended on and paid little or nothing.",
             kick='B · The armies\u2019 own households')

# 9 B CONTENT
content_text('Women who fought outright',
             ['Margaret Corbin stood at a cannon at Fort Washington in 1776.',
              'Wounded there, she was pensioned by Congress.',
              'Deborah Sampson enlisted in 1782 as Robert Shurtliff.',
              'She served in the light infantry, was wounded, and was honorably discharged in 1783.',
              'Mary Ludwig Hays was at Monmouth in 1778: record and legend.'],
             "Take the three women one at a time and keep their evidence separate. Margaret Corbin took her husband's place at his cannon when he was killed at Fort Washington in 1776, was wounded, and was pensioned by Congress, the best documented case of a woman in the line. Deborah Sampson enlisted in 1782 as Robert Shurtliff, served more than a year in the light infantry, was wounded, and was honorably discharged in 1783 when a fever's treatment discovered her sex; the activity reads her record as a labeled summary and marks the one detail that rests on her biographer's account. Mary Ludwig Hays carried water at Monmouth in 1778, and her story hardened over the following century into Molly Pitcher. Teach the seam openly: the water carrier is documented, the pitcher is tradition, and holding the two apart is the historical skill this lesson is practicing.",
             kick='B · The armies\u2019 own households', size=24)

# 10 C DIVIDER
divider_text('Section C', 'Women Thinking Politically',
             'Edenton, October 1774: fifty one women sign a public boycott resolve. London answers with a cartoon.',
             "No period record of women's organized politics in this era is easier to teach than Edenton, because both sides of the record survive: the women's public resolve of October 1774, signed by fifty one women under Penelope Barker's lead, and the British cartoon that mocked it, which students will study up close on the next slide. Frame the pairing before it appears. A boycott resolve signed by women, in public, with their names attached, was a political act in a world that gave women no vote and no office, and London printmakers understood exactly what was threatening about it, which is why the satire works so hard to make the women ridiculous. The mockery is evidence of the act's weight, since no one caricatures what carries none. Section C then moves from the public resolve to the private letter, from Edenton's fifty one signatures to Abigail Adams writing alone to her husband in March 1776.")

# 11 C CONTENT PHOTO
content_photo_s('edenton-port.jpg', 'A Society of Patriotic Ladies, 1775',
             ['This is a British mezzotint, printed in London in March 1775.',
              'The women sign their boycott resolve.',
              'Tea caddies are emptied at the left.',
              'The satire mocks women acting in public.',
              'The mockery is evidence the act carried weight.'],
             "The image is the title slide's print in full: A Society of Patriotic Ladies at Edenton in North Carolina, a mezzotint attributed to Philip Dawe, printed in London for R. Sayer and J. Bennett on March 25, 1775, and held by the Library of Congress. Read it as satire, not as a portrait of the meeting. The women are drawn signing their resolve not to drink tea or promote English manufactures until the acts against America are repealed, and the print crowds the scene with jokes at their expense: drink on the table, a child neglected on the floor, tea caddies emptied by women who cannot be trusted with politics. A London audience was meant to laugh, and the laughter was the argument, that women in public action were absurd. Set the record beside the joke: the Edenton resolve was real, the names were published, and the women signed knowing the names would travel. Students meet this print again on the notebook page.",
             kick='C · Women thinking politically')

# 12 C CONTENT
content_text('Remember the ladies',
             ['Abigail Adams wrote to John Adams on March 31, 1776.',
              'She asked him to remember the ladies in the new code of laws.',
              "She warned against putting unlimited power in husbands' hands.",
              'All men would be tyrants if they could, she wrote.',
              'John answered with a laugh, and a refusal.'],
             "The letter is carried whole, in excerpt, at Station 2 of the activity, from the audited bank record, so teach toward that reading. Abigail Adams wrote on March 31, 1776, as independence approached, asking her husband to use the break with Britain to write a new code of laws that remembered the ladies, refused husbands unlimited power, and heard her warning: if care and attention were not paid, women would foment a rebellion and would not hold themselves bound by laws in which they had no voice or representation. Note whose argument she is borrowing. No voice, no representation, no obligation to obey: that is the colonial case against Parliament, pointed at the household. John Adams answered on April 14 that he could not but laugh, and the new codes left husbands' power standing. Students should be able to state both the request and the answer without softening either.",
             kick='C · Women thinking politically', size=24)

# 13 D DIVIDER
divider_text('Section D', 'Black Americans\u2019 War',
             'November 1775: a royal governor offers freedom for arms. The enslaved decide what the offer is worth.',
             "This is the lesson's center, and it should be taught at the pace that signals it. Set the situation first. By November 1775, Virginia's royal governor, Lord Dunmore, had been driven from Williamsburg and was holding a position afloat off Norfolk with a few hundred men. He needed soldiers, and he knew where Virginia's deepest fear and largest labor force lay. His proclamation, the subject of the quick check and of Station 1 in the activity, offered freedom to enslaved people and indentured servants held by rebels who would bear arms for the king. The offer was limited, conditional, and military in purpose, and the activity's first question makes students find those limits in the text. What the offer set in motion was larger than Dunmore: across the war, enslaved people on both sides treated the conflict as a judgment on their own condition, and acted accordingly.")

# 14 D CONTENT
content_text('Dunmore\u2019s offer, and its conditions',
             ['Freedom was offered to people held by rebels.',
              'The able and willing had to bear arms for the king.',
              'Some hundreds reached his lines.',
              'An Ethiopian Regiment formed: Liberty to Slaves.',
              'Most died of smallpox and fever in the camps.'],
             "Read the proclamation's terms as a lawyer would, because the quick check grades exactly that reading. The offer runs to enslaved people and indentured servants held by rebels, not by Loyalists, whose property Dunmore protects. It runs to those able and willing to bear arms, which leaves out everyone who cannot fight. Freedom is the pay, and the enlistment is the contract. Some hundreds of enslaved Virginians reached his lines and were formed into an Ethiopian Regiment, whose uniform reportedly bore the words Liberty to Slaves, among the most quoted phrases of the war. Then state the camp record with the same plainness: most of those men died of smallpox and fever, the diseases that moved through every crowded camp of the war and through Dunmore's fastest of all. The offer was real, and so were the graves, and the lesson does not let students keep only one of those facts.",
             kick='D · Black Americans\u2019 war', size=24)

# 15 D STAT
stat('about 5,000', 'Black men served in the armed forces of the United States, by the standard estimate',
     'Among them the First Rhode Island Regiment of 1778, raised substantially from enslaved men who earned freedom by enlisting',
     "Hold the estimate label in view: about five thousand Black men served in American forces during the war, the standard estimate historians work from, in the Continental Army and the state forces and as sailors in both navies. The number stands against the policy that began the war, when Black men were barred from the Continental Army on the protests of slaveholders, a ban that held through the crisis of 1775 and gave way as manpower ran short and recruiting officers took the men who presented themselves. Rhode Island's answer was the most direct: its regiment of 1778 was raised substantially from enslaved men, whose enlistment itself earned their freedom, paid for by the state to their former owners. Black soldiers thus served the republic in arms while the republic's law still held their families in slavery, a contradiction the men themselves were in the best position to name, and some did, in the petitions of Section G.",
     kick='D · Black Americans\u2019 war')

# 16 D CONTENT 2
content_text('Flight, the war\u2019s largest self liberation',
             ['Thousands ran to British lines, all war long.',
              'The flight was taken person by person, family by family.',
              'Black sailors crewed both navies.',
              'At the evacuation, freedom was entered in a written record.',
              'Some 3,000 Black Loyalists stand in the Book of Negroes.'],
             "Widen the frame from Dunmore's lines to the whole war. Wherever British armies passed, in Virginia, the Carolinas, Georgia, and around New York, enslaved people ran to them, in numbers that historians count in the thousands across the war, the largest act of self liberation of the era, conducted without proclamations of their own because the running was the statement. It cost families separation, pursuit, and disease in the camps, and it won freedom for those who survived to the evacuation. At New York in 1783, the British recorded some three thousand Black Loyalists by name, age, and former owner in the Book of Negroes, so that their freedom would hold against American claims, and many of those families sailed again in 1792 for Sierra Leone. Section F returns to the evacuation as a whole; here, keep the focus on the decision the record shows enslaved people making, war after war year, with their feet.",
             kick='D · Black Americans\u2019 war', size=24)

# 17 E DIVIDER
divider_text('Section E', 'Native Nations\u2019 War',
             'The Haudenosaunee Confederacy had kept its internal peace for centuries. The war broke it.',
             "Open with what was broken. The Haudenosaunee Confederacy, the Six Nations of the Iroquois, had kept peace among its member nations under its Great Law since before Columbus, one of the oldest continuing governments in North America. The Revolution forced a choice on it that the Confederacy could not settle as one body, because the war was not, from the council fire, a quarrel between Britain and America. It was a contest between two expanding powers at the edges of Haudenosaunee land, and each nation weighed which power threatened that land more. The Oneida and Tuscarora judged for the Americans. The Mohawk, Seneca, Cayuga, and most Onondaga judged for the British. Section E follows the choice, the leader who made the British case most fully, the war of raids that came of it, and the American answer of 1779, whose target was not an army but the towns and corn that fed one.")

# 18 E CONTENT
content_text('A confederacy divided',
             ['The Oneida and Tuscarora stood with the Americans.',
              'The Mohawk, Seneca, Cayuga, and most Onondaga stood with Britain.',
              'Joseph Brant, Thayendanegea, led on the British side.',
              'He was educated in Connecticut and presented at court in London.',
              "He used the alliance as a shield for his people's land."],
             "Give Joseph Brant his full introduction, because the vocabulary test draws on it and because he explains the British choice better than any abstraction. Brant, Thayendanegea, was a Mohawk leader educated in Connecticut, fluent in English and in the diplomacy of both worlds, and presented at court in London, where he pressed his people's claims in person. He fought to use the British alliance as a shield: the king had drawn a line against settler expansion in 1763, British forts supplied the alliance, and the king was an ocean away, while American settlers pressed on Haudenosaunee land every year and an American government would be those settlers' own. From the council fire, distance itself was a defense. The Oneida and Tuscarora weighed the same facts and answered the other way, trusting their nearer ties to American neighbors and missions. Neither side of the split was a mistake to be corrected in class: both were strategies for the same object, the survival of their nations on their land.",
             kick='E · Native nations\u2019 war', size=24)

# 19 E STAT
stat('about 40', 'Seneca and Cayuga towns burned by the Sullivan expedition in 1779',
     'Their stored corn destroyed with them; thousands driven toward Niagara and a starving winter',
     "Teach the number as a count of towns, not of battles. In 1779, on Washington's orders, some four thousand American soldiers under Generals Sullivan and Clinton marched through the Seneca and Cayuga country, met and defeated the force against them at Newtown, and then did the expedition's real work: burning about forty towns, cutting down orchards, and destroying the stored corn that would have fed those towns through the winter. Thousands of people fled to the British post at Niagara, where the winter of 1779 and 1780, one of the coldest of the century, brought severe hunger to the refugees crowded there. The strategy was deliberate and stated in the orders: end the frontier raids by removing the base that fed the raiders. It did not end the raids, and Station 5 of the activity asks students to hold the strategy and its cost in one account, including the peace of 1783, where Haudenosaunee land was ceded by Britain without Haudenosaunee consent.",
     kick='E · Native nations\u2019 war')

# 20 F DIVIDER
divider_text('Section F', 'The Loyalists\u2019 War',
             'Perhaps a fifth of the white population, the conventional estimate, stood with the king, and lost.',
             "Restore the Loyalists to the lesson as people with a position, not as scenery. Perhaps a fifth of the white population remained loyal, the conventional estimate: officeholders and merchants tied to Britain, farmers who feared the rebellion's disorder, people in every colony who judged that the king's order, whatever its faults, protected their property, their faith, or their safety better than a revolution would. The war asked them to prove it, under test oaths administered by their Patriot neighbors, and it punished refusal with confiscation of estates under state laws, banishment, and the rough violence of tarring and feathering that Patriot crowds used against the stubborn. Many fought, in Loyalist regiments that served beside the British, and in the South the Revolution was in part a civil war of neighbors, with scores settled under the war's cover. Section F ends where their war ended: at the water's edge, in the evacuation of 1783.")

# 21 F CONTENT
content_text('Oaths, confiscation, and civil war',
             ['Test oaths were required of the suspected.',
              'Estates were confiscated under state laws.',
              'Tarring and feathering and banishment punished the stubborn.',
              'Loyalist regiments served in British service.',
              'In the South the war was a civil war between neighbors.'],
             "Work the machinery of loyalty in order. A test oath required a man to swear to the new state and renounce the king; refusal marked him. State confiscation laws then took the estates of those who left or fought, selling farms and houses to pay the war's bills and to reward the committed, so disloyalty was punished in property as the tax had never been. Crowd violence did the informal work: tarring and feathering punished Loyalist printers, officials, and stubborn neighbors, stated plainly here as the reading states it, a public and painful humiliation meant to drive a man out. Loyalist regiments gave the committed a military answer, and some of the war's hardest fighting, above all in the southern backcountry, was American against American. When students judge the Revolution's costs in the writing task, this section is the evidence that independence divided the country it created, household by household.",
             kick='F · The Loyalists\u2019 war', size=24)

# 22 F STAT
stat('60,000+', 'Loyalists left the new United States at the peace, by estimate',
     'For Nova Scotia, New Brunswick, Quebec, Britain, Florida, and the Caribbean; among them some 3,000 Black Loyalists',
     "The evacuation was one of the war's largest movements of people, and its figure is an estimate, as the reading marks it: some sixty thousand or more Loyalists left the new United States in 1783 and the months around it, for Nova Scotia and the new province of New Brunswick, for Quebec, Britain, Florida, and the Caribbean. They left from New York, Charleston, and Savannah in fleets the British organized, many of them carrying little more than certificates of service and claims for losses they would press on Parliament for years. Among them were the Black Loyalists of Section D, recorded in the Book of Negroes at New York so their freedom would hold, some three thousand people whose names the ledger kept. Hold the two populations together for students: the evacuation was at once a defeat's exile for the king's white supporters and, for thousands of Black families, the war's promise kept, in a ledger, at the dock.",
     kick='F · The Loyalists\u2019 war')

# 23 G DIVIDER
divider_text('Section G', 'The Reckoning the Promises Demanded',
             'The era\u2019s language, quoted back: petitions, constitutions, courtrooms, and one letter of 1786.',
             "Close the lesson where its question has been pointing all hour. The Revolution's language, natural rights, consent, freedom as a birthright, did not stay in the keeping of the men who first published it. Enslaved people in Massachusetts and New Hampshire petitioned for freedom in that language, arguing a natural and unalienable right to the freedom the new states claimed, and Station 3 of the activity reads the Massachusetts petition of January 1777 in its own words. What answered them was slow, uneven, and real: a constitution in Vermont, a gradual statute in Pennsylvania, court decisions in Massachusetts, and across the South, nothing at all. Section G also sets down the lesson's hardest juxtaposition, the words of George Washington in 1786 beside the fact of Mount Vernon, and asks students to hold the letter and the record together rather than choose between them.")

# 24 G CONTENT
content_text('The first emancipations, and their pace',
             ["Vermont's constitution of 1777 barred adult slavery.",
              'Pennsylvania chose gradual emancipation in 1780.',
              'Massachusetts courts ended slavery in 1783.',
              'Elizabeth Freeman and Quock Walker won their cases.',
              'Washington wrote to Mercer in 1786: abolition was his first wish.'],
             "Take the measures in order and name their pace exactly, because gradual emancipation is a vocabulary term and its definition is the pace: freeing children born to enslaved mothers only after years of service, so slavery died slowly rather than at once. Vermont's constitution of 1777 barred adult slavery outright, the first such act in America. Pennsylvania's statute of 1780, the first legislative emancipation, chose the gradual road. In Massachusetts the end came through the courts in 1783, in the cases of Elizabeth Freeman and Quock Walker, whose suits argued that the state's own constitution, declaring all men born free and equal, had already abolished slavery. Then the letter: Washington, writing to John Francis Mercer in 1786, called it his first wish to see a plan adopted for abolishing slavery, while continuing to hold people in slavery at Mount Vernon until his death. The next lesson reads that letter entire.",
             kick='G · The reckoning', size=24)

# 25 GLANCE
s = slide(NAVY)
kicker(s, 'The war\u2019s peoples at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'What the war asked, and what it left', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Households', 'Farms, camps, boycotts, fundraising', 'The work done; the claims refused'),
        ('Black Americans', 'A choice between two causes', 'Freedom seized, earned, and recorded; camps\u2019 graves'),
        ('Native nations', 'Alliances to shield the land', 'Towns burned; land ceded without consent'),
        ('Loyalists', 'Oaths, property, and exile', '60,000 gone; Black Loyalists in the ledger'),
        ('The reckoning', 'Promises quoted back', '1777, 1780, 1783: freedom begun, slowly')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=20, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 0.85
notes(s, "This slide mirrors the summary table at the end of the guided notes, The War's Peoples at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. Read the rows as one account rather than five summaries. Households supplied the war's money, food, and labor and were refused a voice for it. Black Americans made the war's most consequential choices about their own freedom, on both sides, and paid for them in the camps and at the docks. Native nations chose alliances to shield their land and lost towns, corn, and finally the land itself at a peace table where they had no seat. Loyalists lost the country. And the reckoning row is the lesson's open end: the petitions and the first emancipations show the era's promises beginning to be collected, slowly, by the people they were not written for.")

# 26 VOCAB A
vocab('Words for the offer and the armies',
      [('Dunmore\u2019s Proclamation', 'freedom offered for arms, November 1775'),
       ('inflation', 'prices rise; money buys less'),
       ('camp followers', 'the armies\u2019 workforce, paid little or nothing'),
       ('Deborah Sampson', 'enlisted 1782 as Robert Shurtliff')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. Dunmore's Proclamation: the order of November 1775 by Virginia's royal governor, Lord Dunmore, offering freedom to enslaved people and indentured servants held by rebels if they left their masters and bore arms for the king. inflation: a general rise in prices that shrinks what money can buy, which struck the United States during the war as Congress printed paper money faster than the states could support it. camp followers: the women and children who traveled with the Continental and British armies, cooking, washing, nursing, and carrying supplies, a workforce the armies depended on and paid little or nothing. Deborah Sampson: the Massachusetts woman who enlisted in the Continental Army in 1782 disguised as a man named Robert Shurtliff, served more than a year, and was honorably discharged when her sex was discovered. Read the set in the lesson's order: the offer, the money, the workforce, and the soldier.")

# 27 VOCAB B
vocab('Words for the nations and the reckoning',
      [('Joseph Brant', 'Thayendanegea; the alliance as a shield'),
       ('Sullivan expedition', '1779; some forty towns burned'),
       ('gradual emancipation', 'freedom by slow degrees, after years of service')],
      "Three more terms, again matching the guided notes exactly. Joseph Brant: the Mohawk leader, known in his own language as Thayendanegea, who led Haudenosaunee forces allied with Britain during the war and afterward pressed his people's claims to their land. Sullivan expedition: the American campaign of 1779, ordered by Washington, that burned some forty Seneca and Cayuga towns and their cornfields in answer to frontier raids, driving thousands from their homes. gradual emancipation: the method by which northern states ended slavery after the Revolution, freeing children born to enslaved mothers only after years of service, so slavery died slowly rather than at once. Read the set as the lesson's second half in miniature. Brant names a leader choosing an alliance to defend his people's land. The Sullivan expedition names what the United States did to that land's defenders. Gradual emancipation names the pace at which the North answered the petitions, a freedom real in law and slow in life, whose slowness is inside the definition itself and should be inside students' answers.")

# 28 SYNTHESIS
content_text('Judging the war whole',
             ['The fighting ran through camps, cannons, regiments, and lines of flight.',
              'The paying fell on households, estates, towns, and cornfields.',
              'The waiting fell to wives, petitioners, and the ledger at New York.',
              'Freedom changed most where it was seized and written down.',
              'The writing task asks for both halves in one argument.'],
             "Close the teaching here, before the work slide, and model the judgment the writing task will ask for. The Revolution's promise was not distributed evenly, and its own record shows the distribution. It changed most where people could take hold of it and fix it in a durable form: an enlistment that earned freedom, a name entered in the Book of Negroes, a court decision in Massachusetts, a pension granted in Boston. It changed least where a claim depended on the goodwill of the men it accused: Abigail Adams's argument was complete in 1776 and was answered with laughter, the Massachusetts petition of 1777 asked for an act that never passed, and the Haudenosaunee nations learned in 1783 that their land could be ceded by an ally who had never owned it. The strongest student writing holds the seizures and the refusals in one argument, and can say what each proves about what the promise was worth, and to whom.",
             kick='Synthesis', size=24)

# 29 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Who else fought, paid, and waited through the war, and what did its promise mean to them? Build the file first, then judge from it.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'Whose War: five stations, a file, and a verdict on most changed and least'),
        ('Notebook', 'Notebook page: the war\u2019s peoples charted, and the war\u2019s peoples in one paragraph'),
        ('Quick check', 'Dunmore\u2019s Proclamation, 1775: the offer, its conditions and limits, the camps, the ledger'),
        ('Writing', 'What Freedom Meant: most changed and least, argued from both halves of the bank')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: Dunmore\u2019s offer and the camps, the Haudenosaunee split and Sullivan, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, Whose War, runs five stations: Dunmore's Proclamation from the audited bank record, read for its conditions and its parenthesis; Abigail Adams's letter of March 31, 1776, from the audited bank record; the Massachusetts freedom petition of January 13, 1777, from the Massachusetts Archives transcription; a labeled teaching summary of Deborah Sampson's service with her 1797 portrait; and a labeled teaching summary of the Haudenosaunee decision and the Sullivan expedition. Students build the file in Part 2 and defend a verdict on for whom the Revolution most changed what freedom meant, and for whom it changed it least. The notebook page charts the same five peoples. The quick check works from Dunmore's Proclamation alone. The writing task turns the verdict into an essay drawn from both halves of its bank. The exit ticket has three parts: the offer and the camps, the split and the expedition, and the lesson question answered with one fact from Black Americans' war and one from the reckoning.")

dc.save(OUT)
