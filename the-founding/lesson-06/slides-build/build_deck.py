#!/usr/bin/env python3
"""The Founding Lesson 6 deck, "The Confederation and the Road to
Philadelphia," built to the approved system: image-led slides, fragments
only on screen, comprehensive speaker notes, full lesson + vocabulary
coverage. Fonts: Georgia titles, Lato body."""
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
text(s, 0.9, 5.32, 11.5, 0.4, 'THE FOUNDING · LESSON 6', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Confederation and the Road to Philadelphia', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'A league that could not tax, and the laws it left behind', size=17, color=POWDER)
notes(s, "The image is a detail of Thomas Hutchins's 1778 map of the western parts of Virginia, Pennsylvania, Maryland, and North Carolina, held by the Library of Congress and in the public domain. It shows the Ohio country, the land the Confederation Congress had to govern and the ground of its greatest achievement. The war is won and the peace is signed. What the United States has, in 1783, is a first constitution, the Articles of Confederation, and this lesson teaches that government whole: its deliberate design, its empty treasury, its failures abroad, and then, at full weight, its achievements, the land ordinances of 1785 and 1787 and a decade in which even a weak Congress and the state legislatures legislated like founders. The lesson ends where the next one begins, on the road to Philadelphia in the summer of 1787.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("Why did the government the Revolution built first fail to hold the union together?", {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ("Why did the colonies break with Britain, and what did Americans build in the place of the empire they rejected?", {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Read the lesson question slowly, because its wording carries the lesson's fairness rule. It does not ask why the Articles were badly designed. It asks why the government the Revolution built first failed to hold the union together, which leaves room for the answer the documents support: the design withheld the powers a union needs, and the decade kept handing the government jobs those missing powers were meant for. Students should also register what the question does not claim. A government can fail at holding a union together and still write laws that outlast it, and this one did both, in the same years, sometimes in the same month. Keep both halves in view all hour: the failure is real, and so is the Northwest Ordinance. Every section feeds one side of that double record, and the closing synthesis joins them into a verdict students must defend.")

# ------------------------------------------------- 3 ONE SLIDE
s = slide(CREAM)
kicker(s, 'The lesson in one slide', color=RUST)
text(s, 0.9, 0.95, 11.5, 1.0, 'Seven parts, in order', size=31, color=NAVY, font='Georgia')
frags(s, ['A. A league of friendship, by design',
          'B. An empty treasury',
          'C. A union that could not act',
          'D. The land ordinances: the great achievement begins',
          "E. The Northwest Ordinance and Virginia's Statute",
          "F. Debt, taxes, and Shays's Rebellion",
          'G. The road to Philadelphia'], y=2.0, size=25, gap=10)
notes(s, "Use this slide as the map of the hour, and point students to the same seven letters in their guided notes. Section A takes the Articles on their own terms, as a design with reasons a revolutionary generation found convincing. Section B follows the money, or rather its absence: requisitions, an unpaid army, and Newburgh. Section C goes abroad and home again, to the held frontier posts, the closed Mississippi, and the states taxing each other's goods. Sections D and E give the achievements their full weight, the survey of 1785, the Northwest Ordinance of 1787, and Virginia's Statute for Religious Freedom of 1786. Section F brings the crisis, war debt, hard money taxes, and Shays's Rebellion. Section G walks the road from Mount Vernon in 1785 through Annapolis in 1786 to the fifty five delegates who reached Philadelphia in 1787.")

# ------------------------------------------------- 4 DIVIDER A
divider_photo('articles-port.jpg', 'Section A', 'A League of Friendship, by Design',
    ['Drafted 1777, ratified 1781', 'Sovereign states, one vote each'],
    "The image is the first page of the Articles of Confederation as printed, a United States government printing in the public domain. Hold it up as the lesson's founding text before it becomes the lesson's problem. Congress adopted the Articles in November 1777, in the middle of a war against a king and a Parliament that had taxed Americans without their consent. Ratification then took until March 1781, because Maryland refused to sign until the states with western land claims surrendered them to the union, a holdout students should remember when Section D turns those cessions into a national domain. The men who wrote this document were not careless. They built the government their experience told them was safe, and Section A reads the design in the document's own terms before anyone is allowed to judge it.")

# ------------------------------------------------- 5 CONTENT A
content_photo('articles-port.jpg', 'What Congress could do, and could not',
    ['Declare war and make treaties', 'Coin money, run a post office', 'No power to levy a tax', 'No power over commerce', 'No power to compel a state'],
    "State the design plainly, in the Articles' own logic. Article II reserves to each state its sovereignty, freedom, and independence, and every power not expressly delegated. Article III names the result a firm league of friendship, a league of governments, not a government over citizens. Inside that league, Congress held real but narrow powers: it could declare war, make treaties and alliances, coin money, borrow, and run a post office. What it could not do defines the era. It could not levy a tax on anyone. It could not regulate commerce between the states or with foreign nations. It had no executive to enforce its decisions and no court to judge disputes under them, and it could not compel a state that chose to ignore it. Each state, large or small, held one vote. Ask the class to say the design back in one sentence before moving on: a union of sovereign states that had armed its center for war and peace and disarmed it for everything else.",
    kick='Section A · The design')

# ------------------------------------------------- 6 STAT A
stat('13 of 13', 'states had to confirm any change to the Articles',
    'Major measures needed nine states. One refusal could block any repair, including a tax power',
    "Use this count to make Article XIII concrete, because it is the clause that turns the Articles from a weak design into a locked one. Ordinary major measures, war, treaties, borrowing, needed the agreement of nine of the thirteen states. An amendment needed more: agreement in Congress, then confirmation by the legislature of every state, thirteen of thirteen. A single small state could veto a repair all the others wanted, and in the 1780s single states did exactly that to proposals giving Congress a duty on imports, the closest the Confederation came to an independent revenue. Teach the consequence now, while it is fresh: a defect written into this document could not reliably be removed by the document's own method. That is why the story of reform in Section G runs outside the Articles, through conferences and conventions, and why the Philadelphia meeting of 1787 arrived instructed to revise and ended by replacing.",
    kick='Section A · The lock')

# ------------------------------------------------- 7 DIVIDER B
divider_text('Section B', 'An Empty Treasury',
    'Revenue by request, and an army unpaid',
    "Now follow the money, because the Articles' first failure was arithmetic. A government that makes war, services a war debt, pays diplomats, and runs a post office needs revenue every year, in peace as in war. The Articles gave Congress exactly one way to get it: ask the states. Section B takes that mechanism apart, the requisition, and then shows where an empty treasury leads, to an unpaid army whose officers came within one speech of defying Congress at Newburgh in March 1783. Teach the section without melodrama. Nobody in it is a villain. The state legislatures that paid late or paid nothing were answering to their own taxed and indebted voters, under a document that had made payment voluntary in everything but name. The system's flaw was that it made good behavior optional and then depended on it entirely.")

# ------------------------------------------------- 8 CONTENT B
content_text('Paid by requisition',
    ['Congress set each state a share', 'State legislatures laid the taxes', 'Each state paid what it chose', 'By the mid 1780s, a small fraction of what was asked'],
    "Walk the chain of a requisition slowly, from the document. Under Article VIII, the common treasury was to be supplied by the several states in proportion to the value of their land, and the taxes for paying each proportion were to be laid and levied by the state legislatures themselves. Congress computed and requested; only a state could tax. Define the vocabulary term here as the guided notes carry it, a request a state could lawfully refuse or ignore, and then give the record. Through the early 1780s the states paid late and in part. By the middle of the decade they were sending a small fraction of what Congress asked, and this lesson states no percentage, because the surviving accounts do not support one honest figure for all thirteen states. The results were concrete: interest on the foreign debt went unpaid, diplomats borrowed to cover their own salaries, and the army, the subject of the next slide, waited for pay that a request could not produce.",
    kick='Section B · The mechanism')

# ------------------------------------------------- 9 CONTENT B2
content_text('Newburgh, March 1783',
    ['Officers unpaid, pensions promised and unfunded', 'Discontent close to defiance of Congress', 'Washington met his officers in person', 'Persuasion did the work of power'],
    "Tell Newburgh as the empty treasury arriving at a person. The war was effectively won, and the Continental Army sat at Newburgh, New York, unpaid for months, its officers holding Congress's promise of pensions that Congress had no revenue to fund. In March 1783 anonymous addresses circulated among the officers hinting that the army might refuse to disband, or worse, until it was paid. Washington called a meeting, spoke against any threat of force, and reminded his officers of his own service and sacrifices beside theirs. The discontent collapsed. Students should name exactly what settled the crisis: not a payment, which Congress could not make, and not a power, which the Articles had not granted, but the personal authority of one commander over men who trusted him. A government that depends on that is a government one retirement away from a different ending, and Washington's planned retirement made the point urgent for everyone watching.",
    kick='Section B · The warning')

# ------------------------------------------------- 10 DIVIDER C
divider_photo('map-port.jpg', 'Section C', 'A Union That Could Not Act',
    ['Posts held, a river closed', 'States taxing each other'],
    "The image is a detail of Thomas Hutchins's 1778 map of the western country, held by the Library of Congress and in the public domain. Use it to set the geography of this section: the frontier posts at Niagara, Detroit, and Michilimackinac sat on the lakes and rivers of this map, and the Mississippi, the western farmers' road to the sea, runs along its edge. Section C tests the Confederation where a union most needs to act as one: abroad, in treaty enforcement and trade, and at home, in commerce among its own members. The pattern students should watch for is consistent. Congress could speak for the United States. It could sign, promise, and protest. What it could not do was make its own members keep the promises it had signed, and foreign governments priced that weakness accurately and quickly.")

# ------------------------------------------------- 11 CONTENT C
content_photo('map-port.jpg', 'The posts and the river',
    ['Britain held Niagara, Detroit, Michilimackinac', 'The treaty terms on debts went unenforced', 'Spain closed the Mississippi in 1784', 'Congress could answer neither'],
    "Take the two foreign failures in order. The Treaty of Paris of 1783 granted the United States the land to the Mississippi and required British evacuation of the frontier posts, while American negotiators promised that British creditors could collect prewar debts and that Loyalist property would be treated fairly. State laws and courts blocked both promises, and Congress had no power to make a state honor a treaty it had signed for all of them. Britain answered by keeping its garrisons at Niagara, Detroit, and Michilimackinac, on American soil, controlling the fur trade and the alliances of the lakes. Then, in 1784, Spain closed the Mississippi at New Orleans to American trade, cutting western farmers off from the only practical outlet for their produce. Answering Madrid required trade concessions Congress could not deliver or force it could not pay for. Two empires, one lesson: the union's word abroad was worth what thirteen separate legislatures chose to make it worth.",
    kick='Section C · Abroad')

# ------------------------------------------------- 12 CONTENT C2
content_text('Trade wars at home',
    ['British goods flooded American ports', 'American merchants barred from the British West Indies', 'New York taxed New Jersey firewood', 'And Connecticut produce'],
    "Bring the weakness home, where students can feel it in a woodpile. After the peace, British merchants returned to American ports with goods on easy credit and took the market the war had cleared, while American ships were barred from the British West Indies, the carrying trade colonial merchants had once lived on. Congress could not answer, because the Articles gave it no power over commerce at all: it could not set a common duty, could not bargain with London as one market, could not retaliate. The states filled the vacuum against each other. New York taxed firewood coming in from New Jersey and farm produce from Connecticut for its own revenue, and its neighbors answered with duties of their own. A union whose members tax each other's firewood has a commerce problem no requisition can fix. Hold this slide's example for Section G, because trade, not abstract theory, is what brought the states to Mount Vernon in 1785 and Annapolis in 1786.",
    kick='Section C · At home')

# ------------------------------------------------- 13 DIVIDER D
divider_text('Section D', 'The Land Ordinances',
    'The achievement, given its full weight',
    "Stop here and change the register deliberately, because this section and the next carry the lesson's standing instruction: the achievements get their full weight before the crisis resumes. The Confederation Congress governed one thing directly and completely, the national domain that Maryland's holdout had forced the landed states to create by ceding their western claims. On that domain it legislated with an imagination and a permanence nothing else in the decade matches. The Land Ordinance of 1785 decided how a continent would be measured, divided, and sold, and its grid is still the landscape of the Midwest. Section D teaches the survey; Section E teaches the greater ordinance of 1787 that decided what kind of states would rise on the surveyed land, and pairs it with Virginia's Statute, the decade's other founding text. Students who skip these two sections will write the verdict wrong.")

# ------------------------------------------------- 14 CONTENT D
content_photo('map-port.jpg', 'The survey of 1785',
    ['A national domain from the state cessions', 'Townships of six miles square', 'Thirty six sections to a township', 'One section in each for public schools'],
    "The image is the Hutchins map again, the country before the grid. Teach the Land Ordinance of 1785 as an act of design. Congress ordered the domain surveyed before sale: surveyors would run lines due north and south and east and west, dividing the land into townships of six miles square, and each township into thirty six sections of one square mile each. Land would then be sold to raise the revenue Congress could not tax for, with one section in every township, the sixteenth by the ordinance's numbering, reserved for the support of public schools. Notice what kind of act this is. It is rational, uniform, and permanent: the straight roads and square fields of Ohio, Indiana, and Illinois still follow these lines, and a traveler flying over the Midwest today is looking down on a Confederation Congress ordinance. Define the term from the guided notes here: the law set the grid still visible across the Midwest. A government this deliberate was not a nullity, whatever its treasury said.",
    kick='Section D · The grid')

# ------------------------------------------------- 15 STAT D
stat('36', 'sections in every township under the survey of 1785',
    'Townships of six miles square, one section of each township reserved for public schools',
    "Use the number to fix the survey's scale in students' minds. One township under the Land Ordinance of 1785 held thirty six sections, each of one square mile, six hundred forty acres. Run the multiplication with the class: a township was thirty six square miles of surveyed, numbered, sellable land, identical in form from the Ohio River to the lakes. That uniformity was the point. A buyer in New York could purchase a described section he had never seen, a clerk could record it, a court could settle its boundaries, and the school section sat in the same place in every township, so a settler knew where the community's school land lay before a single family arrived. The ordinance turned land, the one asset the union actually held, into a system. Compare it quietly with the requisition: where Congress governed directly, it governed well. Where it had to ask thirteen governments, it waited. That contrast is the whole lesson in one comparison.",
    kick='Section D · The scale')

# ------------------------------------------------- 16 DIVIDER E
divider_photo('jefferson-port.jpg', 'Section E', "The Northwest Ordinance and Virginia's Statute",
    ['July 13, 1787, and January 16, 1786', 'The decade legislating like a founding age'],
    "The image is Rembrandt Peale's 1800 portrait of Thomas Jefferson, held by the White House Historical Association and in the public domain. Jefferson belongs on this divider because he authored one of this section's two texts, Virginia's Statute for Religious Freedom, and had drafted the territorial plan of 1784 from which the other grew. Section E teaches the two documents together, deliberately: the Northwest Ordinance, passed by the Confederation Congress on July 13, 1787, while the Philadelphia convention sat, and the Statute, passed by Virginia's legislature on January 16, 1786. Between them they guaranteed worship, promised equal statehood, encouraged schools, barred slavery from a territory larger than the original states' seaboard, and disestablished a church. Teach them at full value, and teach their seams too: the fugitive proviso inside the slavery bar, and the Native land beneath the free territory.")

# ------------------------------------------------- 17 CONTENT E
content_photo('map-port.jpg', 'The Ordinance of 1787',
    ['States on an equal footing', 'Trial by jury, freedom of worship', 'Schools encouraged', 'Slavery barred north of the Ohio'],
    "The image is the Hutchins map once more, the territory the ordinance governed. Read the Northwest Ordinance as the Confederation's monument, because later generations have: Congress itself, under the new Constitution, reenacted it in 1789. Its machine ran in stages, appointed government first, then an elected assembly, then, at sixty thousand free inhabitants, statehood, and the promise that made it revolutionary was equality: new states would enter on an equal footing with the original thirteen in all respects, not as colonies of the seaboard. Its articles of compact guaranteed the territory's inhabitants freedom of worship, trial by jury, and the writ of habeas corpus, and declared that schools and the means of education shall forever be encouraged. Then its sixth article: there shall be neither slavery nor involuntary servitude in the said territory. One Congress, which could not collect a tax, drew the boundary between free and slave territory along the Ohio River for the next seventy years.",
    kick='Section E · The monument')

# ------------------------------------------------- 18 STAT E
stat('60,000', 'free inhabitants made a territory a state',
    'Article 5 of the Northwest Ordinance, admission on an equal footing with the original states',
    "Slow down on the threshold, because the number carries the promise. Under Article 5 of the Northwest Ordinance, whenever a state formed in the territory reached sixty thousand free inhabitants, it would be admitted into Congress on an equal footing with the original states in all respects whatever, free to form its own permanent constitution and government, provided that government was republican. Compare that with every older empire students have studied in this course: colonies stayed colonies, taxed and governed from a capital across the water. The Confederation instead wrote its western lands a dated, numbered path out of territorial status and into full membership, and then honored it, for Ohio in 1803 and for the states that followed across the map on the previous slides. Note also the word free in the count, and connect it to Article 6: in this territory, the inhabitants who counted toward statehood were, by the ordinance's own design, free people.",
    kick='Section E · The promise')

# ------------------------------------------------- 19 CONTENT E2
content_photo('jefferson-port.jpg', "Virginia's Statute, 1786",
    ['Written by Jefferson in 1777', 'Carried by Madison in 1786', 'The church disestablished', 'No man compelled to support any worship'],
    "The image is Peale's Jefferson of 1800. Teach the Statute as the Confederation era legislating at founding level in a statehouse, because that is where the Articles left the power to do it. Jefferson drafted the bill in 1777; it slept in Virginia's legislature for years; James Madison steered it through in the winter of 1785 and 1786, and the Assembly passed it on January 16, 1786. Its enacted clause is the cleanest sentence of the decade: no man shall be compelled to frequent or support any religious worship, place or ministry whatsoever, nor shall otherwise suffer on account of his religious opinions or belief, and those opinions shall in no wise diminish, enlarge, or affect his civil capacities. The Anglican establishment in Virginia ended, religious taxes ended, and Jefferson ranked the statute with the Declaration among his life's works. Congress could not have passed this law for Virginia. Under the Articles, founding was something states still did.",
    kick='Section E · The statute')

# ------------------------------------------------- 20 DIVIDER F
divider_photo('shays-port.jpg', 'Section F', "Debt, Taxes, and Shays's Rebellion",
    ['Hard money taxes on indebted farms', 'Courts closed from August 1786'],
    "The image is the woodcut of Daniel Shays from the cover of Bickerstaff's Boston Almanack for 1787, held by the National Portrait Gallery and in the public domain; the crop shows Shays alone from the paired print. Section F returns to the crisis, at ground level, in the farm towns of western Massachusetts. The chain students must be able to recite runs from policy to violence: a state determined to pay its war debt in full, taxes levied in hard money that farmers did not have, certificates bought cheap by speculators now honored at full value by those taxes, foreclosures and debtors' prison at the end of the chain. The men who closed the courts in 1786 were, many of them, the same men who had filled the Continental Army's ranks, led by officers of Bunker Hill and Saratoga. Teach them as creditors' and debtors' politics turning armed, not as a mob.")

# ------------------------------------------------- 21 CONTENT F
content_photo('shays-port.jpg', 'The squeeze in Massachusetts',
    ['Debts paid in full, in specie', "Soldiers' certificates in speculators' hands", 'Foreclosure and debtors\u2019 prison', 'Petitions first, then the courts closed'],
    "The image is the 1787 almanac woodcut of Shays again. Build the squeeze step by step. Massachusetts chose the honorable road on its war debt: pay it in full, on time, in hard money. Honorable for the state's credit meant crushing at the farm gate, because the western counties ran on barter and scarce coin, and the taxes fell due in specie. Worse, much of the debt had migrated: soldiers, unpaid in the war, had sold their pay certificates for pennies to speculators, who would now receive full value from taxes levied on the very men who had sold cheap. Some states answered such pressure with paper money and laws delaying collection. Massachusetts refused both. Farmers petitioned the legislature for relief and got little. From late August 1786 they changed methods: organized crowds, calling themselves Regulators after an older American tradition, closed the courts at Northampton, Worcester, and Springfield, so no judge could enter a foreclosure while the courts sat shut.",
    kick='Section F · The chain')

# ------------------------------------------------- 22 CONTENT F2
content_text('Springfield, and what followed',
    ['A militia financed by private subscription', 'Four men died at the arsenal, January 1787', 'The movement broken by February', 'Then the taxes eased, and the governor fell'],
    "Finish the rebellion with its most instructive detail first: when Massachusetts moved against the Regulators, the state financed its militia by private subscription among Boston merchants, because neither the state treasury nor Congress could produce an army's pay on demand. General Shepard's militia guarded the federal arsenal at Springfield, and on January 25, 1787, it fired on Shays's advancing column; four men died, and the rebellion broke within weeks, scattered by a winter march in February. Then teach the ending students rarely hear: the political system answered part of the grievance itself. The legislature eased the tax burden, and Massachusetts voters turned Governor Bowdoin out of office in the next election. The state had governed, harshly and then responsively, entirely on its own. Congress's part in the union's worst domestic crisis had been to watch it, unable to supply a soldier or a dollar. Every delegate who traveled to Philadelphia that spring carried Springfield with him.",
    kick='Section F · The ending')

# ------------------------------------------------- 23 DIVIDER G
divider_text('Section G', 'The Road to Philadelphia',
    'Mount Vernon 1785, Annapolis 1786, Philadelphia 1787',
    "Close the lesson on the road the reformers actually traveled, because it did not begin with Shays's Rebellion and it did not begin in Congress. It began with two states settling a river dispute at George Washington's house in 1785 and liking the method enough to propose more of it. It continued through a convention at Annapolis in September 1786 that failed at its stated business, trade, with only five states present, and used its failure to call for something larger. Shays's Rebellion, breaking that winter, gave the call its audience among men of property who had begun to fear the republic itself was dissolving. And in February 1787 Congress, the institution being repaired, endorsed the meeting for one stated purpose: revising the Articles. Section G assembles the fifty five men who answered, and hands the story to the next lesson.")

# ------------------------------------------------- 24 CONTENT G
content_text('Fifty five delegates, twelve states',
    ['Mount Vernon Conference, 1785', 'Annapolis calls for Philadelphia, 1786', 'Congress endorses revision, February 1787', 'Rhode Island sent none'],
    "Assemble the road in its order. In March 1785, commissioners from Virginia and Maryland met at Mount Vernon, settled their dispute over navigation of the Potomac, and suggested a wider conference on trade. Virginia invited all the states to Annapolis in September 1786; five states came, too few to settle the trade of thirteen, and the delegates, in a report drafted by Alexander Hamilton, declared the defects of the federal government too many for a trade meeting and called for a convention at Philadelphia in May 1787 to render the federal government adequate to the exigencies of the union. Congress endorsed the call on February 21, 1787, for the sole and express purpose of revising the Articles of Confederation. That summer fifty five delegates from twelve states reached Philadelphia; Rhode Island, satisfied with the Articles as they were, sent none. They were, on average, younger than the Congress of 1776, veterans, lawyers, merchants, and planters of the Revolution itself, and the next lesson opens inside their room.",
    kick='Section G · The call answered')

# ------------------------------------------------- 25 AT A GLANCE
content_text('The lesson at a glance',
    ['The design: sovereign states, a center without a tax',
     'The treasury: requisitions answered with a fraction',
     'Abroad: posts held, the Mississippi closed',
     'The achievement: 1785 and 1787, the survey and the Ordinance',
     'The road out: Annapolis to Philadelphia'],
    "This slide mirrors the closing table in the guided notes, The Confederation at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The five lines are the lesson's double argument in miniature. The Articles built a league of sovereign states around a Congress armed for war and treaties and disarmed for revenue, commerce, and enforcement. The predictable results followed: requisitions answered with a fraction, an unpaid army calmed by one man's authority, a treaty unenforced, a river closed, and states taxing each other's firewood. And the same decade, on the one ground where Congress governed directly and in the statehouses where the Articles left the power, produced the survey grid of 1785, the Northwest Ordinance of 1787, and Virginia's Statute of 1786. Failure and founding, in the same government, in the same years.",
    kick='Review')

# ------------------------------------------------- 26 VOCAB 1
vocab('Words for the league and its land', [
    ('Articles of Confederation', 'the first constitution of the United States, adopted by Congress in 1777 and ratified in 1781, which joined the thirteen states in a league that left most power with the states'),
    ('confederation', 'a league of independent states that keep their sovereignty and join for limited common purposes, the form of union the Articles of Confederation created'),
    ('requisition', 'a request by Congress under the Articles of Confederation asking a state to supply money or troops, which the state could lawfully refuse or ignore'),
    ('Land Ordinance of 1785', "the Confederation Congress's law for surveying the western lands into townships and lots and selling them to raise revenue, which set the grid still visible across the Midwest")],
    "These definitions match the guided notes word for word, and students copy them exactly. Articles of Confederation: the first constitution of the United States, adopted by Congress in 1777 and ratified in 1781, which joined the thirteen states in a league that left most power with the states. confederation: a league of independent states that keep their sovereignty and join for limited common purposes, the form of union the Articles of Confederation created. requisition: a request by Congress under the Articles of Confederation asking a state to supply money or troops, which the state could lawfully refuse or ignore. Land Ordinance of 1785: the Confederation Congress's law for surveying the western lands into townships and lots and selling them to raise revenue, which set the grid still visible across the Midwest. Point out how the first three terms describe a machine for asking, and the fourth describes the machine at its best.")

# ------------------------------------------------- 27 VOCAB 2
vocab('Words for the crisis and the call', [
    ('Northwest Ordinance', "the Confederation Congress's law of 1787 for governing the territory north of the Ohio River, which barred slavery there and promised its territories statehood on equal terms with the original states"),
    ("Shays's Rebellion", 'the uprising of 1786 and 1787 in western Massachusetts, led in part by the former captain Daniel Shays, in which indebted farmers closed courts to stop foreclosures before the state militia put them down'),
    ('Annapolis Convention', 'the meeting of September 1786, attended by five states, called to discuss trade among the states, which instead called for a convention at Philadelphia to repair the federal government')],
    "Three more terms, again matching the guided notes exactly, and students copy them as written. Northwest Ordinance: the Confederation Congress's law of 1787 for governing the territory north of the Ohio River, which barred slavery there and promised its territories statehood on equal terms with the original states. Shays's Rebellion: the uprising of 1786 and 1787 in western Massachusetts, led in part by the former captain Daniel Shays, in which indebted farmers closed courts to stop foreclosures before the state militia put them down. Annapolis Convention: the meeting of September 1786, attended by five states, called to discuss trade among the states, which instead called for a convention at Philadelphia to repair the federal government. Have the class notice the order the terms fall in: the era's greatest law, its sharpest crisis, and the meeting that turned the crisis into a convention.")

# ------------------------------------------------- 28 SYNTHESIS
content_text('Synthesis: weak at governing, strong at lawmaking',
    ['The design withheld the tools of compulsion',
     'The failures ran through the states',
     'The achievements ran where Congress governed directly',
     'Repair required unanimity, so reform went around',
     'Philadelphia inherited both records'],
    "Draw the lesson together by answering the lesson question in full sentences students can borrow. Why did the government the Revolution built first fail to hold the union together? Because its design withheld the tools a union runs on: no tax, no commerce power, no executive, no way to compel a state, and no way to amend itself short of unanimity. Its failures all ran through that design, from the fraction the states sent against requisitions to the treaty clauses state courts blocked and the Mississippi Congress could not reopen. Its achievements ran on the other track, where Congress governed directly, in the ordinances of 1785 and 1787, and where the Articles left founding work to the states, in Virginia's Statute of 1786. Philadelphia inherited both records at once: a union that had to be rebuilt, and proof, in its own laws, of what an American government could write when it held the power to act.",
    kick='Synthesis')

# ------------------------------------------------- 29 EXIT
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.15, 11.5, 1.6, 'Answer the question, from the records',
     size=36, color=CREAM, font='Georgia', leading=1.15)
text(s, 0.9, 2.55, 11.5, 1.1, ['Why did the government the Revolution built first fail',
                               'to hold the union together? Build from the documents.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Confederation File: five records, a ledger, and a verdict'),
        ('Notebook', 'Notebook page: could do, could not do, achieved, and one paragraph'),
        ('Quick check', 'A League and Its Limits: Articles II, VIII, and XIII at work'),
        ('Writing', 'Failure, Draft, or a Job Without Tools? Argued from the file')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the design choice and the fear behind it, one achievement and one failure with dates, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Confederation File, runs five records: the Articles of Confederation, quoted from the audited record; the Northwest Ordinance, quoted from the Avalon Project transcription; Virginia's Statute for Religious Freedom, quoted from the audited record; Washington's letter to John Francis Mercer of September 9, 1786, quoted from the Founders Online text the record carries; and a labeled teaching summary of Shays's Rebellion. Students keep a ledger of what the era could and could not do, and close with a verdict: failure, unfinished draft, or a government overtaken by a job it was never given the tools for. The quick check works Articles II, VIII, and XIII directly. The writing task argues the verdict as an essay. The exit ticket asks for the design choice and its fear, one achievement and one failure with dates, and the lesson question answered in two or three sentences.")

dc.save(OUT)
