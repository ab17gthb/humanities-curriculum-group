#!/usr/bin/env python3
"""The Founding Lesson 2 deck, "From Protest to Revolution: 1773 to 1776,"
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

LQ = 'How did a protest over tea become a war?'
UQ = 'Why did the colonies break with Britain, and what did Americans build in the place of the empire they rejected?'

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'THE FOUNDING · LESSON 2', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'From Protest to Revolution: 1773 to 1776', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'A tax on tea, a closed port, and the first shots of a war', size=17, color=POWDER)
notes(s, "The image is Nathaniel Currier's lithograph The Destruction of Tea at Boston Harbor, published in 1846, seventy three years after the night it pictures, and students should hear that date first: no artist recorded the Tea Party in 1773, so the famous picture is a later generation imagining its own founding. Open by placing this lesson where the last one ended. Lesson 1 closed with repeal and resistance in balance, a quarrel over taxes that both sides still expected to settle. This lesson follows the three years in which the quarrel escaped settlement: a rescue act for a tea company, a disciplined destruction in Boston Harbor, a punishment that united the colonies, and a march to seize gunpowder that ended in blood. Students should leave able to trace each step to the next and to judge which step closed the door on reconciliation.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[(LQ, {})]], size=40, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                (UQ, {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question asks how a protest, a kind of argument, turned into a war, a kind of killing, and students will need the whole chain for the exit ticket and the writing task. Walk the chain in advance so the class can watch it assemble. A protest over tea became a question of who held the right to tax. The destruction of the tea became a demand for payment and a punishment. The punishment became the occasion for the colonies to act as one people, with a congress and a boycott enforced like a government. The boycott's enforcement became an armed standoff over magazines and powder, and the standoff became shooting at Lexington. Warn students against the single cause answer: every step in this lesson was chosen by people who believed the other side had left them no smaller move.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Tea, punishment, union, powder, war', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The Tea Act and the Trap of Cheap Tea', 'Direct sale, a lower price, and the tax kept in place'),
        ('B', 'The Night of December 16, 1773', '342 chests in the harbor, and nothing else harmed'),
        ('C', 'The Intolerable Acts', "Boston's port closed, its charter rewritten, Gage in command"),
        ('D', 'The Colonies Answer Together', 'Twelve colonies in Congress, and a boycott enforced'),
        ('E', 'The Winter of Powder', 'Magazines seized on both sides, and riders in the night'),
        ('F', 'April 19, 1775', 'Two records of one morning, and Boston besieged'),
        ('G', 'The First Year of War', "Washington's army, Bunker Hill, and the king's answer")]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A covers the Tea Act and why cheap tea was a trap. Section B covers the night of December 16, 1773. Section C covers the Intolerable Acts and General Gage's arrival. Section D covers the First Continental Congress, the Declaration and Resolves, and the Continental Association. Section E covers the winter of powder and the ride of April 18. Section F covers April 19, 1775 in its two disagreeing records. Section G covers the first year of war, from Washington's appointment to the king's Proclamation of Rebellion. The summary table at the end of the guided notes is titled The Road from Tea to War at a Glance, and students will complete it from these seven sections.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', 'The Tea Act and the Trap of Cheap Tea',
             'A rescue for a great company, priced so that every cup conceded a principle.',
             "Set up the Tea Act as a piece of design, because its danger lay in how reasonable it looked. The East India Company, one of Britain's greatest trading firms, was drowning in unsold tea and near bankruptcy, and its failure would shake British credit and the India trade together. Parliament's rescue let the company bypass the colonial merchants who had always handled its tea and sell directly in America through its own chosen agents. With middlemen gone, the price fell below what colonists had been paying, even though the Townshend duty of three pence a pound stayed on the tea. Teach the trap in one sentence: the tea was cheap precisely so that Americans would drink it, and every cup purchased at the new price was a quiet vote that Parliament's tax was lawful. The colonists who organized against the act were not protesting a high price. They were refusing a low one, on principle.")

# ------------------------------------------------------ 5 TEA ACT TRAP
content_photo('tea-party-port.jpg', 'Cheap tea, a costly principle',
              ['The East India Company near bankruptcy',
               'Direct sale through its own agents',
               'Colonial merchants cut out of the trade',
               'The Townshend duty stays on every pound'],
              "The image is a portrait crop of Currier's 1846 lithograph of the Tea Party, a later imagining of December 1773 rather than a record of it. Work through the act's three moving parts. First, the seller changes: the company sells through its own consignees in each port, and the established colonial tea merchants, men with warehouses, credit, and political voices, are cut out of a trade they had run for a generation. Second, the price falls: company tea undersells even smuggled Dutch tea, which is why smugglers joined the resistance alongside merchants and lawyers. Third, the duty remains: Parliament had kept the Townshend tax on tea in 1770, when it repealed the other Townshend duties, expressly to hold the principle that it could tax America. Put the parts together and the act offered Americans cheaper tea in exchange for conceding the one claim they had spent a decade denying.",
              kick='A · The Tea Act')

# ------------------------------------------------------ 6 PORTS ANSWER
content_text('Four ports answer in four ways',
             ['Charleston: the tea lands, and rots in a warehouse',
              'New York and Philadelphia: the ships are turned back',
              "Boston: Governor Hutchinson refuses the Dartmouth clearance",
              'The legal deadline runs out on December 16'],
             "The colonies answered the act port by port, and the variety is the point: there was no single American government yet, so each town improvised. At Charleston the tea was landed under guard and left to rot in a warehouse, a victory by neglect. At New York and Philadelphia, crowds and committees persuaded or forced the consignees to resign and the captains to turn back to sea. Boston was the hard case because its consignees included the sons of the royal governor, Thomas Hutchinson, and Hutchinson refused both to resign them and to let the Dartmouth leave the harbor without unloading and paying the duty. Behind him stood a legal clock: once a ship had been in port twenty days, the customs officers could seize its cargo for the unpaid duty and land it themselves. The deadline fell on December 17, which is why the crisis broke on the night of the sixteenth.",
             kick='A · The Tea Act', size=24)

# ------------------------------------------------- 7 SECTION B DIVIDER
divider_text('Section B', 'The Night of December 16, 1773',
             'A town meeting votes, a harbor fills with tea, and nothing else is touched.',
             "Teach this night as a planned operation, because the planning is the historical fact students most often miss. On December 16, 1773, thousands of people filled Old South Meeting House and the streets around it while a committee waited on Governor Hutchinson for permission for the Dartmouth to leave. His refusal came back at dusk. The meeting's moderator is reported to have said that the gathering could do nothing more to save the country, and men already prepared moved on the wharf. The disguises, thin coatings of paint and costume meant to suggest Mohawks, did two kinds of work: they hid individual faces from prosecution, and they announced that the actors stood outside ordinary politics, as Americans rather than as British subjects. What followed was destruction carried out under orders, in parties, ship by ship, which is why the participants and their defenders insisted afterward that it was not a riot.")

# ------------------------------------------------------ 8 THE NIGHT
content_text("Three hours at Griffin's Wharf",
             ['Some one hundred men board three tea ships',
              'Chests split open so the tea cannot be saved',
              '342 chests emptied into the harbor',
              'Nothing stolen, nothing else harmed, decks swept'],
             "Our fullest participant account comes from George Hewes, a Boston shoemaker who was there and whose recollection, published in 1834 when he was an old man, students will read in the activity. Hewes describes parties assigned to each ship, commanders obeyed, captains asked for the hatch keys and candles and supplying them, and the chests split with hatchets so the tea would be ruined by the water rather than salvaged. In about three hours the work was done. The discipline deserves a full stop in class. The men replaced a broken padlock, swept the decks, and punished one of their own number caught pocketing tea. They were making an argument with property: the tea alone was the offense, because the tea alone carried the tax. A mob steals. This crowd destroyed one cargo, harmed no person, and went home in silence, which is why supporters called the night a protest and why Parliament's answer had to treat it as something larger.",
             kick='B · December 16, 1773', size=24)

# ------------------------------------------------------ 9 STAT 342
stat('342', 'chests of tea emptied into Boston Harbor',
     'Destroyed in about three hours on December 16, 1773 · The cargo Parliament would demand Boston pay for · The act that turned an argument about taxes into a debt and a crime',
     "Hold this number up as the hinge of the lesson's first half. Three hundred forty two chests was the whole cargo of three ships, a loss the East India Company counted in the tens of thousands of pounds, and it converted the imperial quarrel's terms overnight. Before December 16, the argument was about rights: could Parliament tax, could it grant a monopoly, could a governor hold a port. After December 16, the argument was also about property and payment, language every merchant and lawyer in the empire understood. Parliament's answer in the spring was built directly on this figure: Boston's port would stay closed until the tea was paid for. Ask students to notice what the number did to the politics. Men who had doubts about destroying property still had to decide whether a whole town should be punished until it paid, and that second question united people the first one had divided.",
     kick='B · December 16, 1773')

# ------------------------------------------------- 10 SECTION C DIVIDER
divider_photo('exciseman-port.jpg', 'Section C', 'The Intolerable Acts',
              ['The print shows Bostonians tarring and', 'feathering a customs man beneath the', 'Liberty Tree, made for London readers.'],
              "The image is The Bostonians Paying the Excise-Man, a London print attributed to Philip Dawe and published on October 31, 1774. It squeezes two events into one scene: the tarring and feathering of customs official John Malcolm in January 1774, and the Tea Party in the background, with the Stamp Act nailed upside down to the Liberty Tree. It was made for a British audience, and it shows how London pictured Boston when Parliament legislated: a town ruled by mobs, amusing itself by torturing a tax man. Section C teaches Parliament's answer to December 16, the spring 1774 statutes the colonists named the Intolerable Acts. The print belongs beside the statutes because they argue the same case in two media: Boston is disorderly, its charter government has failed, and coercion is the remedy. Students will read the Port Act's own words in the activity and can set the picture and the statute side by side.",
              title_size=40)

# ------------------------------------------------------ 11 FOUR ACTS
content_text('Four acts, and a fifth as the colonies read it',
             ['Boston Port Act: the harbor closed until the tea is paid for',
              "Massachusetts Government Act: the charter rewritten by Parliament",
              'Administration of Justice Act: officials tried outside the colony',
              'Quartering Act: the army housed on wider powers',
              'Quebec Act: read in the colonies as a fifth blow'],
             "Take the acts one at a time, in the order colonists felt them. The Boston Port Act, in force from June 1, 1774, closed the harbor to trade and moved the customs house to Salem; it punished every Bostonian who earned a living from the water, whether or not he had stood on the wharf in December. The Massachusetts Government Act rewrote the colony's charter without its consent, making the council a royal appointment and putting town meetings under the governor's permission. The Administration of Justice Act let royal officials accused of crimes in the colony be tried in Britain, which colonists read as a license for soldiers to kill without a local jury. A new Quartering Act widened the army's power to take buildings. Colonists also folded in the Quebec Act, which tolerated Catholic worship and extended Quebec to the Ohio River, as a fifth blow against their claims and their faith's establishment.",
             kick='C · The Intolerable Acts', size=23)

# ------------------------------------------------- 12 SECTION D DIVIDER
divider_text('Section D', 'The Colonies Answer Together',
             'Relief for one blockaded town, and a congress for twelve colonies.',
             "Parliament's design assumed Boston would stand alone: other ports were expected to take Boston's trade and leave its radicals to submit. The design failed in the summer of 1774, and section D teaches the failure as the colonies' first continental act. Towns across the colonies voted supplies for the blockaded port, and food arrived from as far away as South Carolina, with Boston's own leaders taking care that the gifts were announced colony by colony. The deeper answer was political. The committees of correspondence, built in the quiet years, carried the call for a continental congress, and in September 1774 delegates chosen by assemblies and conventions gathered at Philadelphia. Teach the sequence plainly: punishment aimed at one colony produced the first institution that belonged to all of them, and everything afterward, the boycott, the army, and eventually independence, ran through that institution.")

# ------------------------------------------------------ 13 CONGRESS
content_text('Philadelphia, fall 1774: rights declared, a boycott enforced',
             ['Fifty six delegates from twelve colonies; Georgia absent',
              'Declaration and Resolves: rights held by consent, never ceded',
              'The Continental Association: imports, then exports, boycotted',
              'Elected committees enforce it in every county and town'],
             "The First Continental Congress sat from September into late October 1774, and its two great products belong together. The Declaration and Resolves of October 14 stated the colonial case at full length: the colonists were entitled to life, liberty, and property, they had never ceded to any power a right to dispose of any of the three without their consent, and taxation belonged to their own legislatures alone. Congress called its chosen weapon peaceable: the Continental Association, a boycott of British imports from December, of consumption from March, and of exports the following fall, until the acts were repealed. The enforcement is the lesson in government. Every county and town elected a committee to inspect cargoes, publish violators' names, and cut them off from trade and society. A committee that can decide what may be bought and sold is governing, whatever it calls itself, and by the spring of 1775 the Association's committees were the colonies' second government.",
             kick='D · The Colonies Answer Together', size=23)

# ------------------------------------------------------ 14 STAT 56
stat('56', 'delegates from twelve colonies at Philadelphia',
     'Georgia absent · The Suffolk Resolves, carried to Congress, urged Massachusetts to arm and drill · Relief for Boston arrived from colonies as far away as South Carolina',
     "Fifty six men in one room was a new fact in American politics, and students should feel its novelty. No institution had ever spoken for the colonies together: not the Crown's governors, who answered to London colony by colony, and not the assemblies, each jealous of its own charter. The Congress that met in September 1774 was chosen by twelve colonies through their assemblies and conventions, and it behaved from its first week like a body that expected to meet again, keeping journals, appointing committees, and issuing documents in a continental voice. Among its first acts was endorsing the Suffolk Resolves from Massachusetts, which declared the Intolerable Acts void and urged the people to arm and train. A congress that blesses arming while petitioning for redress is no longer only a protest meeting. It is a government in waiting, and London read it exactly that way when the resolves and the Association reached Britain that winter.",
     kick='D · The Colonies Answer Together')

# ------------------------------------------------- 15 SECTION E DIVIDER
divider_text('Section E', 'The Winter of Powder',
             'Two governments, one countryside, and every magazine a prize.',
             "By the winter of 1774 and 1775 the colonies held two governments on the same ground, and both of them needed gunpowder. Section E teaches the months when the argument turned into a competition for arms. Royal officials seized colonial stores where they dared, at Portsmouth, at Salem where militia faced regulars across a drawbridge, and in a dozen smaller raids; colonial forces answered by taking royal powder and cannon, including the guns of Fort William and Mary in New Hampshire. In Massachusetts the Provincial Congress organized supply, gathered stores inland at Concord and Worcester, and set the minuteman system in place, picked men from the militia companies pledged to turn out at a minute's notice. General Gage, governing Boston with a few thousand regulars and orders to act without starting a war, watched the countryside arm around him. Each side told itself it was only securing what the other would seize first, which is the classic road by which armed standoffs become battles.")

# ------------------------------------------------------ 16 THE RIDE
content_text('April 18, 1775: seven hundred men march for Concord',
             ['Gage orders the stores at Concord seized',
              'Paul Revere and William Dawes ride to warn the country',
              "Captain Parker's company waits at Lexington",
              'The regulars come up the road at dawn'],
             "Gage's expedition was planned as a police action, not a battle: some seven hundred regulars would march by night to Concord, seize or destroy the cannon, powder, and provisions gathered there, and return before the countryside could gather. Secrecy failed within hours. The Boston committee's warning system, built over the winter, sent Paul Revere across the Charles River and William Dawes out over Boston Neck, and riders carried the alarm from town to town, so that militia companies were assembling along the road hours before the column reached them. At Lexington, astride the road to Concord, Captain John Parker kept his company near the green through the night, dismissing and recalling them as reports came in. Neither Parker nor the British advance guard's commander, Major Pitcairn, had orders to start a fight. What each had was armed men, a crowd of witnesses, and no room left to step back, which is the condition the next section examines in the two records the morning left behind.",
             kick='E · The Winter of Powder', size=23)

# ------------------------------------------------- 17 SECTION F DIVIDER
divider_photo('concord-port.jpg', 'Section F', 'April 19, 1775: Lexington and Concord',
              ['Doolittle drew Concord days after', 'the fighting, from the ground and', 'from the men who had stood on it.'],
              "The image is Plate II of Amos Doolittle's engravings, a view of the town of Concord, drawn by Ralph Earl and engraved by Doolittle, who reached Massachusetts with Connecticut troops days after April 19 and walked the ground with men who had fought on it. The four Doolittle plates are the closest visual record the day has, made within the year from participants' testimony. Section F teaches the day twice over, because it survives in two records that cannot both be right. A British officer's private diary says the colonists fired first and his own men answered without orders. The militiamen's sworn testimony, taken six days later and published at once, says the regulars fired on a company already dispersing. Teach students to hold the records apart, weigh each by its maker and its moment, and notice what they agree on: a volley at dawn, eight Americans dead on the green, and a war begun before anyone had declared one.",
              title_size=36)

# ------------------------------------------------------ 18 TWO RECORDS
content_photo('lexington-port.jpg', 'One morning, two records',
              ["Barker's diary: they fired one or two shots; our men rushed in without orders",
              "The testimony: fired on while dispersing, backs turned",
              'Eight Americans dead on Lexington green',
              'The North Bridge, then the long fight back to Boston'],
              "The image is Doolittle's Plate I, the battle of Lexington, published in 1775. Set the two records side by side as the activity and the quick check do. Lieutenant John Barker wrote for himself on the day: the column advanced prepared against attack without intending to attack, the colonists fired one or two shots, and his men, without any orders, rushed in, fired, and put them to flight, afterward so wild they could hear no orders. The thirty four militiamen swore on April 25 that Parker had dismissed them to await the drum, that the company was dispersing with its backs turned when the regulars fired, and that no man in the company fired first, to their knowledge. Both records were weapons as well as memories: Massachusetts rushed its version into print to win the argument about who began the war, in the other colonies and in Britain. The day itself ended with the column fighting back to Boston under fire from behind walls and trees, and thousands of militia besieging the town by dark.",
              kick='F · April 19, 1775')

# ------------------------------------------------------ 19 STAT 273
stat('273', 'British casualties on April 19, 1775, the standard count',
     'Against about 95 American casualties, the standard count · The regulars fought back some eighteen miles to Boston · By nightfall an army of militia held the town under siege',
     "Give the day's arithmetic its weight, labeled as the lesson labels it: these are the standard counts historians work from, some 273 British casualties against about 95 American for April 19 as a whole. The distribution tells the story. At Lexington the loss was nearly all American, eight killed on the green against one British soldier wounded, which is why the morning reads as a massacre in the American record. Across the full day the balance reversed: at Concord's North Bridge the militia fired as an organized force, and on the march back the column was shot at from behind walls, trees, and houses for miles, saved from destruction only by reinforcements from Boston. A police expedition had lost more men in a day than many set piece battles of the era cost, and the regulars who reached Boston that night were besieged in it. Whatever shot began the morning, its consequences belonged to no one's plan.",
     kick='F · April 19, 1775')

# ------------------------------------------------- 20 SECTION G DIVIDER
divider_text('Section G', 'The First Year of War',
             'An army raised, a hill defended, and a petition answered with a proclamation.',
             "The shooting at Lexington did not declare anything, and section G teaches the strange year in which a war was fought by men who denied they were rebels. The Second Continental Congress, meeting in May 1775, adopted the militia besieging Boston as a Continental Army and gave its command to George Washington of Virginia, joining the South to New England's fight. In June the militia's stand on Breed's Hill taught both armies what the war would cost. In July the same Congress that was raising regiments sent the king a petition professing loyalty and begging him to interpose against his ministers. The king's answer, a Proclamation of Rebellion issued in August before the petition even arrived, and Parliament's Prohibitory Act, placing American ships outside his protection, closed the legal ground on which loyalty had stood. By the turn of 1776, royal government had collapsed across the colonies and committees governed in fact, while independence remained undeclared and unspeakable to many who were already fighting.")

# ------------------------------------------------------ 21 ARMY AND BUNKER HILL
content_photo('bunker-port.jpg', 'An army, and the price of Breed\'s Hill',
              ['Congress creates the Continental Army, May and June 1775',
              'Washington of Virginia takes command at Cambridge',
              "June 17: militia twice throw back the assaults on Breed's Hill",
              'The British take the hill, at over a thousand casualties'],
              "The image is Bernard Romans's Exact View of the battle at Charlestown, an engraving of about 1775 by a mapmaker who served on the American side. Two decisions of June 1775 fixed the war's shape. Congress adopted the New England militia before Boston as the Continental Army and appointed George Washington, a Virginia planter and former militia colonel, to command it. The choice was strategy in the form of a name: a southern commander made the siege of Boston the cause of colonies that had never seen Massachusetts. Days later, on June 17, American troops fortified Breed's Hill above Charlestown overnight, and British regulars assaulted the works head on. Twice the militia's fire threw them back. On the third assault, with American powder gone, the hill fell. Britain held the ground and counted more than a thousand casualties, officers in ruinous proportion, for a peninsula it then abandoned within the year. Both sides understood the lesson: this enemy would stand behind works and shoot, and the war would be long and expensive.",
              kick='G · The First Year of War')

# ------------------------------------------------------ 22 OLIVE BRANCH
content_text("The Olive Branch, and the king's answer",
             ['July 1775: Congress professes loyalty, blames the ministers',
              'August 1775: a Proclamation of Rebellion, issued before the petition arrives',
              "The Prohibitory Act puts American shipping outside the king's protection",
              'Turn of 1776: governments of committees, an army, no declaration'],
             "The Olive Branch Petition of July 1775 is the document students most often misread as hypocrisy, so teach its logic carefully. Congress blamed the crisis on the king's ministers, as English petitioners had blamed ministers for centuries, and begged George III to interpose, repeal the distressing statutes, and settle a lasting reconciliation. Many members meant it: they were fighting, as they said, in defense of British liberties, and a royal word could still have ended the war on terms most of them would have taken. The king refused to receive the petition and, on August 23, 1775, proclaimed the colonies in open rebellion, a step taken before the petition reached London. Parliament's Prohibitory Act then withdrew the king's protection and made American ships lawful prizes, which colonists read as the king making war on them and dissolving the bond from his side. The lesson closes there: by 1776 the empire in America had been replaced in fact, by congresses, committees, and an army, while the word independence waited for the argument of the next lesson.",
             kick='G · The First Year of War', size=23)

# ------------------------------------------------------ 23 GLANCE
s = slide(NAVY)
kicker(s, 'The road from tea to war at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Each step answered the last', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The tea', 'Destroyed in one night, December 1773', 'Parliament demands payment'),
        ('The punishment', "Port closed, charter rewritten, 1774", 'The colonies unite against it'),
        ('The answer', 'Congress, the Resolves, the Association', 'A second government in fact'),
        ('The shots', 'Lexington and Concord, April 1775', 'War before independence')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the summary table in the guided notes, The Road from Tea to War at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The four rows are the lesson's argument in order. The tea: a cargo destroyed in one disciplined night, which handed Parliament a debt to collect and a crime to punish. The punishment: the Intolerable Acts closed the port and rewrote a charter, and united the colonies that were meant to abandon Boston. The answer: twelve colonies met in Congress, declared their rights, and enforced a boycott through committees that governed in fact. The shots: the march to Concord met the militia at Lexington, and by nightfall a siege had begun. Grade the table generously on wording and strictly on sequence: a table that loses the order of the steps has lost the lesson's claim, which is that each step made the next one harder to refuse.")

# ------------------------------------------------------ 24 VOCAB A
vocab('Words for the crisis',
      [('Tea Act', 'direct sale, a lower price, the tax kept'),
       ('Boston Tea Party', '342 chests destroyed, December 16, 1773'),
       ('Intolerable Acts', "the punishment laws of 1774, closing Boston's port"),
       ('First Continental Congress', 'twelve colonies at Philadelphia, fall 1774')],
      "These definitions match the guided notes word for word, because the unit test draws on them. " + joined('Tea Act') + ". " + joined('Boston Tea Party') + ". " + joined('Intolerable Acts') + ". " + joined('First Continental Congress') + ". Teach the four as one chain. The Tea Act set the trap, the Tea Party sprang it, the Intolerable Acts were Parliament's reply, and the Congress was the colonies' reply.")

# ------------------------------------------------------ 25 VOCAB B
vocab('Words for the sides',
      [('minutemen', "Massachusetts militia, ready at a minute's notice"),
       ('Loyalist', 'loyal to Britain, opposed to independence'),
       ('Patriot', "on the rebellion's side, for independence from 1776")],
      "Three more terms, again matching the guided notes exactly. " + joined('minutemen') + ". " + joined('Loyalist') + ". " + joined('Patriot') + ". Keep the last two terms honest in class: Loyalist and Patriot are the names the winning side's vocabulary preserved, and in 1775 most colonists were neither yet, but men and women choosing under pressure, from conviction, from interest, from fear of disorder, and from loyalty to neighbors as much as to causes. The terms describe positions in a civil argument that became a civil war, and students will meet both positions again in the war lessons ahead.")

# ------------------------------------------------------ 26 SYNTHESIS
s = slide(NAVY)
kicker(s, 'The lesson in one view')
text(s, 0.9, 1.28, 11.5, 1.0, 'An argument that ran out of paper', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Trapped', 'Cheap tea priced to concede the taxing power, refused at four ports'),
        ('Punished', 'A port closed and a charter rewritten, without a trial of any offender'),
        ('United', 'Twelve colonies, one Congress, and a boycott enforced like a law'),
        ('Bloodied', 'Lexington, Concord, and Bunker Hill, before independence was declared')]
yy = 2.78
for t, d in rows:
    text(s, 0.9, yy, 2.4, 0.7, t, size=24, color=RUST_LT, font='Georgia')
    text(s, 3.45, yy + 0.05, 9.0, 0.9, d, size=19, color=CREAM, leading=1.2)
    yy += 1.05
notes(s, "Use this slide to close the argument before the work begins, and make students say the four rows aloud in order, because the sequence is the lesson. Trapped: the Tea Act offered cheap tea at the price of conceding Parliament's right to tax, and the ports refused the bargain in four different ways. Punished: Parliament answered destroyed property by closing a port and rewriting a charter, punishing a town without trying a single offender. United: the punishment built the thing it aimed to prevent, a continental Congress whose boycott committees governed the colonies in fact. Bloodied: the standoff over powder produced Lexington and Concord, and Bunker Hill proved the militia would stand against regulars at a price both sides remembered. A war was being fought by the turn of 1776 by men who still called themselves Britons, and the next lesson takes up the argument that finally gave the war a name and a purpose.")

# ------------------------------------------------------ 27 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did a protest over tea become a war? For each record, state what its makers wanted it to prove, then judge the step that closed the door.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'From Tea to War: five stations and a verdict on the decisive step'),
        ('Notebook', 'Notebook page: five steps in a chart, and the step that closed the door'),
        ('Quick check', 'Two Records of One Morning: Barker against the sworn testimony'),
        ('Writing', 'How a Protest over Tea Became a War: the lesson question as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the Intolerable Acts defined with the Port Act named, the two Lexington records set against each other, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, From Tea to War, puts five stations in front of students: Hewes remembering the Tea Party in 1834, the Boston Port Act in Parliament's own words, the Declaration and Resolves of the First Continental Congress, Barker's diary, and the militiamen's sworn testimony, and it ends with a table of what each record was made to prove and a verdict on the step that did most to make reconciliation impossible. The notebook page charts the five steps and asks for the step that closed the door. The quick check, Two Records of One Morning, tests the Concord mission, the two first shot claims, Barker's admissions, and the pamphlet war of April 1775. The writing task turns the lesson question into an essay argued from the evidence bank. The exit ticket has three parts: the Intolerable Acts with the Port Act named, the two Lexington records in a sentence each, and the lesson question in two or three sentences. Next lesson takes up the argument of 1776, and the pamphlet that made independence speakable.")

dc.save(OUT)
