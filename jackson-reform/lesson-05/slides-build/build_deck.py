#!/usr/bin/env python3
"""Jackson and Reform Lesson 5 deck, "The Market Revolution: Factories, Canals,
and Wires," built on the shared deck system: image-led slides, fragments only
on screen, comprehensive speaker notes, full lesson and vocabulary coverage."""
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
OUT = os.path.join(HERE, '..', 'lesson-05-slides.pptx')

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
photo_right(s, 'lowell-port.jpg')
text(s, 0.9, 1.5, 6.9, 0.4, 'JACKSON AND REFORM · LESSON 5', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 2.0, 6.9, 2.2, 'Factories, Canals, and Wires', size=44, color=CREAM, font='Georgia', leading=1.1)
rule(s, 0.92, 4.15)
text(s, 0.9, 4.5, 6.8, 1.6, 'The market revolution, and what the factory and the telegraph did to the way Americans lived and worked', size=20, color=POWDER, leading=1.3)
notes(s, "The image is a period print of Lowell, Massachusetts, its mills in a row along the Merrimack River, published between 1840 and 1860 and held by the Library of Congress. Open with the town in the picture, because Lowell is this lesson built in brick: a place that was farmland in 1820 and a factory city within the decade. Set the frame before the detail. The last four lessons were political: the vote, removal, nullification, and the bank. This lesson goes underneath the politics to the economy those men were arguing inside, an economy being rebuilt between about 1815 and 1848 by canals, steamboats, railroads, factories, and one wire. Students will end by judging whether the rebuilding handed ordinary Americans more control over their lives, or less.")

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('What did the factory and the telegraph do to the way Americans lived and worked?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ("What did democracy mean in Jackson's America, who was it for, and what did the era's reformers claim it still owed?", {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "The lesson question names two inventions, but it asks about lives, and students should hear that from the first minute. The factory is a way of organizing people: work moved out of the household, hours set by someone else's bell, wages paid in cash. The telegraph is a way of organizing knowledge: news and prices moving faster than any person could travel. Between them stands the transport that made both pay, the canals and railroads that let a factory sell to a continent and a merchant trade on same day prices. Tell students the writing task will ask for one judgment, more control or less, defended from the documents, and that the best evidence for both judgments is in this lesson, including a mill woman's own defense of the mills.")

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'A household economy becomes a market economy', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'A country of households', 'Making most of what they used, before 1815'),
        ('B', 'Water first', 'Steamboats; the Erie Canal, 1825'),
        ('C', 'Roads of iron', '23 miles in 1830; 9,000 by 1850'),
        ('D', 'The factory system', "The employer's machines; the bell; standard parts"),
        ('E', 'The Lowell system', 'Boardinghouses, rules, wages, and turn outs'),
        ('F', 'Wires', 'Morse, May 24, 1844; news leaves travel behind'),
        ('G', 'The gain and the cost', 'Cheaper goods and cash wages; the bell and the panic')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A sets the baseline, a household economy that made most of what it used. Sections B and C move goods: water first, then iron. Section D changes how things are made, gathering workers at an employer's machines under a bell, with interchangeable parts in the armories. Section E fills the factory with people, the young women of Lowell, their rules, their magazine, and their turn outs. Section F moves news off the road entirely. Section G weighs the whole change. Tell students the summary table at the end of their guided notes asks them to rebuild exactly this map.")

# 4 A DIVIDER
divider_text('Section A', 'A Country of Households',
             'In 1815 most American households made most of what they used, because moving goods was slow and dear.',
             "Begin with the baseline, and make students feel it before breaking it. A farm family in 1815 grew its food, made or bartered for its cloth, built and mended its own tools, and sold a small surplus in the nearest town. That was not backwardness; it was arithmetic. Where a wagon haul could double the price of a barrel of flour in a hundred miles, producing for a distant market made no sense, and buying from one made less. The household was therefore a workshop, a school of trades, and a welfare system at once. Section A asks students to hold that world firmly in mind, because everything after it, canal, railroad, factory, and wire, is measured against it. The change, when it came, did not move the household. It widened the household's world past the horizon.")

# 5 A CONTENT
content_text('Making most of what they used',
             ['Food grown; cloth spun, woven, or bartered',
              'Surplus traded close to home',
              'Transport slow, and dearer than the goods',
              'About 1815 to 1848: the pattern breaks',
              'Producing for distant markets, buying from them'],
             "Work the arithmetic of distance, because it explains the whole section. Freight on bad roads cost so much per mile that low value goods could not travel far and live: wheat was worth grinding into flour, and flour into whiskey, partly because each step made the product worth more per pound it cost to haul. So the household economy was local by necessity, and its members' skills were general by necessity too; a farmer was also a carpenter, a cooper, and a mender of everything. Then, between about 1815 and 1848, canals, steamboats, railroads, and the telegraph cut the cost and time of moving goods and news so sharply that the arithmetic inverted. Historians call the change the market revolution. The Ohio farmer of the reading, selling wheat to Rochester and wearing Massachusetts cloth woven from southern cotton, is not three stories. He is one household, rewired.",
             kick='A · A country of households', size=24)

# 6 B DIVIDER
divider_text('Section B', 'Water First: Steamboats and the Erie Canal',
             'Steamboats ran against the current, and one canal cut the price of a ton of freight by nine tenths.',
             "Water moved first because water was cheap, and the two machines of this section answer two different rivers. The steamboat answered the western rivers, where flatboats had floated produce down to New Orleans and then been broken up for lumber because nothing could haul freight back up against the Mississippi current. Steam could, from 1811 on the western waters, and the valley was tied two ways to its port. The canal answered the East's geography, the Appalachian wall between the seaboard and the lakes. Section B follows the Erie Canal from Albany to Buffalo, and asks students to learn its numbers cold, because the numbers are the revolution in one line: what a ton of freight cost, and how long it took, before and after 1825.")

# 7 B CONTENT
content_text('The Erie Canal, finished 1825',
             ['363 miles, Albany to Buffalo on Lake Erie',
              'A ton of freight: about $100, to under $10',
              'The trip: about twenty days, to about eight',
              'Western wheat east; eastern goods west',
              "New York City becomes the nation's first port"],
             "Teach the canal as a price collapse with a ditch attached. Before 1825, moving a ton of goods between Buffalo and New York City cost about one hundred dollars and took about twenty days by road and lake. The canal brought the charge under ten dollars and the time to about eight days, and every farmer, miller, and merchant between the lakes and the Hudson redid his sums at once. Western wheat and flour poured east; eastern manufactures, salt, and immigrants poured west; Rochester milled the wheat, Buffalo shipped it, and New York City, collecting the ocean end of the trade, passed Philadelphia and Boston to become the nation's first port. Other states rushed to copy New York and mostly borrowed themselves into trouble doing it, a fact Lesson 4's panic makes relevant. The canal did not just move goods. It decided which cities would matter.",
             kick='B · Water first', size=24)

# 8 B STAT
stat('363', 'miles of Erie Canal, from the Hudson River at Albany to Buffalo on Lake Erie, finished in 1825',
     'Built by the State of New York in eight years, and paid for by its tolls within the decade',
     "Give the giant number its setting, because 363 miles of hand dug canal is easy to say and hard to picture. Work began in 1817, Governor DeWitt Clinton's project, derided as a ditch and a folly, and the canal opened whole in October 1825, with Clinton pouring a keg of Lake Erie water into New York harbor to marry the waters. The engineering was American and improvised: locks lifting boats over the escarpment at Lockport, an aqueduct carrying the canal itself across the Genesee River at Rochester. Tolls repaid the state's borrowing faster than its friends had promised. Students should also register who dug it: contractors' gangs, many of them Irish immigrants, at wages and in conditions the celebration prints leave out. The canal is this lesson's first proof that the market revolution was built by labor as well as by invention.",
     kick='B · Water first')

# 9 C DIVIDER
divider_photo('train-port.jpg', 'Section C', 'Roads of Iron',
             ['Railroads began as canal feeders, ran in winter, climbed new country, and within twenty years outran the canals entirely.'],
             "The print shows the first passenger train in New York State in 1831, the locomotive DeWitt Clinton hauling cars that are stagecoach bodies set on rails, as reproduced in a 1921 railroad history. Introduce the railroad as the canal's child and then its executioner. The first lines were built to feed canals and rivers with freight from the country behind them. Within a few years promoters saw that a road of iron was not a feeder but a rival: it ran when canals froze, it climbed where canals could not be dug, and it moved passengers at speeds that made the packet boat feel like a ferry. Section C follows the first runs, which students read as a labeled teaching summary at Station 3 of the activity, and then the mileage, which is the section's real text.")

# 10 C CONTENT
content_text('First runs, and a race with a horse',
             ['Baltimore and Ohio chartered, 1827',
              "Tom Thumb hauls the B&O directors, 1830",
              'DeWitt Clinton, Albany to Schenectady, 1831',
              'Stagecoach bodies on rails; sparks and speed',
              'Built to prove steam to investors and riders'],
             "Slow down on the demonstrations, because in 1830 a railroad was a claim, not a fact, and claims need audiences. Peter Cooper built the little Tom Thumb to show the Baltimore and Ohio's directors that a steam engine could haul a car around the road's sharp curves; the famous race with a horse drawn car, lost when a belt slipped, still proved the point his hosts cared about. A year later the DeWitt Clinton made the first passenger run in New York State, Albany to Schenectady, with respectable citizens in coach bodied cars being singed by sparks and thrilled by speed in about equal measure. What was being sold in both runs was confidence: to legislators asked for charters, to investors asked for money, and to a public asked to ride behind a boiler. The mileage in the next slide is what that confidence bought.",
             kick='C · Roads of iron', size=24)

# 11 C STAT
stat('9,000+', 'miles of railroad track in the United States by 1850, from about twenty three miles in 1830',
     'More track than any other nation on earth, laid in a single generation',
     "Put the two numbers side by side and let the class sit with them: about twenty three miles of track in all the United States in 1830, some twenty eight hundred in 1840, more than nine thousand in 1850. No other nation had laid as much. The growth was not smooth or public spirited by nature: companies fought for charters, towns bid against each other with subscriptions and bonds to be put on a line, and a town the railroad passed by could wither in a decade. Gauges differed from road to road, so freight still changed cars at breaks, and the whole web ran on borrowed money, much of it British, which is one road by which a panic in London reached an Ohio farm. For the lesson's question, note what the railroad did to time: it was the first land transport faster than a horse, and it made the timetable, and eventually standard time itself, a fact of ordinary life.",
     kick='C · Roads of iron')

# 12 D DIVIDER
divider_text('Section D', 'The Factory System',
             "Work leaves the household's pace for the employer's building, the employer's machines, and the employer's bell.",
             "Now change the subject from moving things to making them, and state the section's contrast exactly as the guided notes carry it. The older pattern: artisans and farm households making goods in their own shops and homes, at their own pace, with their own tools, selling what they finished. The new pattern: workers gathered in one building, working set hours at machines they do not own, owned by an employer who sells what they make and pays them wages for their time. That second pattern is the factory system, and cheap transport is what made it pay, because a factory that can sell to a continent can keep its looms running and its people hired in a way a village workshop never could. Section D builds the model at Waltham and Lowell, then turns to the armories, where the same logic was applied to the parts of a gun.")

# 13 D CONTENT
content_text('One building, one bell, one owner',
             ['Workers gathered in one building, set hours',
              'Machines owned by the employer, driven by water',
              'Waltham, 1814; then Lowell on the Merrimack',
              'Operatives tending looms they do not own',
              'The product sold by the company, not the maker'],
             "Walk the contrast point by point, because the unit test will ask for it as a contrast. Place: the employer's building, not the worker's home or shop. Tools: the company's power looms, driven by water through belts and shafts, not the weaver's own loom. Time: set hours, announced by bells, the same for hundreds of people at once, not the task based rhythm of a household. Pay: wages for time, not the price of a finished piece the maker owned and sold. Francis Cabot Lowell and his partners, the Boston Associates, proved the system at Waltham in 1814 with spinning and weaving under one roof, then built it at scale at the Pawtucket Falls of the Merrimack in the 1820s, in the town that took Lowell's name. Everything in Section E, the boardinghouses, the rules, the magazine, and the strikes, follows from this section's five points.",
             kick='D · The factory system', size=24)

# 14 D CONTENT 2
content_text('Interchangeable parts: any part fits any unit',
             ['Perfected in the federal armories',
              'Every part filed and machined to a pattern',
              'A broken part replaced, not refitted by hand',
              'Spread through New England machine shops',
              'Skill moves from the hand into the pattern'],
             "Use a musket to teach this, because the federal armories at Springfield and Harpers Ferry were its school. The old way: a gunsmith files each lock's parts until they fit that one gun, and a broken part in the field means a craftsman, time, and luck. The new way: gauges, jigs, and milling machines cut every part to a standard pattern so closely that any part fits any unit of the model, and a soldier or a mill mechanic swaps the broken part for a sound one in minutes. The economic meaning is the section's point. Skill that lived in one man's hands now lives in the pattern and the machine, which means the work can be divided, supervised, and hired by the hour, the factory system's logic carried into metal. New England's machine shops, many of them founded to build textile machinery, spread the method to clocks, tools, sewing machines, and everything after.",
             kick='D · The factory system', size=24)

# 15 E DIVIDER
divider_photo('lowell-port.jpg', 'Section E', 'The Lowell System and the Mill Women',
             ['Factories, boardinghouses, and churches built together, and a workforce of young women recruited from New England farms.'],
             "The print is Lowell's mills along the Merrimack again, the title slide's image, and the section now fills those buildings with people. Lowell's problem as its founders saw it was labor and reputation together. New England had no surplus of factory hands, and no respectable farm family would send a daughter to the kind of mill town the English industrial cities had made infamous. The Boston Associates' answer was a system, the Lowell system of the Key Terms: build the boardinghouses and churches with the factories, recruit young women from the farms, house them under keepers and rules, and pay cash wages high enough to make the offer worth a family's while. Section E teaches the bargain whole: what the women got, what it cost them, what they wrote, and what they did when the companies tightened the terms in the 1830s.")

# 16 E CONTENT
content_text('The bargain at Lowell',
             ['Boardinghouses under keepers, beside the mills',
              "A ten o'clock curfew; church expected",
              'Cash wages, high for work open to women',
              'Savings, money sent home, a brother schooled',
              'More than 8,000 at Lowell by 1840'],
             "State the bargain as both sides understood it in the 1820s and 1830s, because students judge it better whole. The company offered cash wages that beat domestic service, sewing, and school teaching, the employments open to women, paid to the woman herself. It offered housing in company boardinghouses under a keeper, meals, a curfew, and churches built with the mills, the whole apparatus certifying to a farm family in Vermont or New Hampshire that a daughter's good name was safe in a factory town. The woman offered her labor at the loom for long days at the machine's pace, and her conduct, in the house as well as the mill, to the company's judgment. Many women came for a few years, saved, helped their families, read and borrowed books, and left. The system's defenders, including the women at Station 1 of the activity, made exactly this case, in print, and meant it.",
             kick='E · The Lowell system', size=24)

# 17 E CONTENT 2
content_text('Their magazine, and their turn outs',
             ['The Lowell Offering: their own writing, 1840',
              'Farley answers Brownson in its pages',
              'Speedups, wage cuts, and board charges',
              'Turn outs in 1834 and 1836',
              "A Factory Girls' Association of their own"],
             "Give the women the section's last word in both of their registers, print and combination. The Lowell Offering, a magazine written by the operatives themselves and edited by Harriet Farley among others, carried their essays and poems across the country and answered the reformer Orestes Brownson's 1840 charge that factory work disgraced them: students read that answer whole at Station 1, from the audited bank record. The other register is the turn out. When the corporations cut wages in 1834, about eight hundred women struck; when they raised the board charge in 1836, well over a thousand struck, and out of that defeat built the Lowell Factory Girls' Association, some two thousand five hundred strong. Neither strike won. Together they show the factory town teaching its workforce the skills of association the next lessons' reform movements run on.",
             kick='E · The Lowell system', size=24)

# 18 E STAT
stat('8,000+', 'workers in the Lowell mills by 1840, most of them young women from New England farms',
     "The largest industrial workforce in the country, gathered in a town that had been farmland twenty years before",
     "Anchor the section in the bank record's own figure, from the headnote of the Lowell mill girls record students read at Station 1: by 1840 more than eight thousand workers tended Lowell's textile machinery, most of them young women from New England farms. Consider what concentration means. Eight thousand workers eating in company houses, worshiping in company aided churches, reading the same magazine, and discovering the same grievances in the same week is a new kind of public, one no household economy could have produced. It is also a workforce the corporations had assembled for their own purposes and could not disassemble when it began to act for its own. Keep the number beside the turn outs of the last slide: strikes of eight hundred and of well over a thousand are what a concentrated workforce makes possible, and the companies' blacklist of 1834 is what they used to answer it.",
     kick='E · The Lowell system')

# 19 F DIVIDER
divider_text('Section F', 'Wires: News at the Speed of the Signal',
             'On May 24, 1844, a message crossed forty miles without a horse, a boat, or a train under it.',
             "Slow the class down for four words, because this section's event is small enough to hold in one hand and large enough to end the old world of news. Until 1844, information could move no faster than the body carrying it: the fastest dispatch was a relay of horses, a steamboat, or the new locomotive. Every price, every election return, every declaration of war in this course so far traveled at the speed of travel. Section F follows Samuel F. B. Morse, a painter turned inventor, his electromagnetic telegraph, the federal money that built his first line, and the demonstration message students read at Station 2 from the audited bank record, tape and all. Then it asks what work changed when news and travel parted company.")

# 20 F CONTENT
content_text('What hath God wrought',
             ['Morse, painter turned inventor',
              'A federal appropriation builds the line',
              'Washington to Baltimore, May 24, 1844',
              'Four words, from the Bible, return by wire',
              'The message proved the system, not the news'],
             "Tell the demonstration as theatre with a purpose, because it was one. Congress had voted thirty thousand dollars for an experimental line between Washington and Baltimore, strung beside the railroad, and Morse sent the first message from a room in the Capitol on May 24, 1844, during the Democratic convention's season. The words, What hath God wrought, from the book of Numbers, were suggested by Annie Ellsworth, a family friend. Alfred Vail in Baltimore received the dots and dashes on paper tape, the tape students see in the activity, and sent the message back. Note what the four words do not do: they report nothing, order nothing, and price nothing. Their whole content was the fact of their arrival, which was the information Congress had paid to test, and every newspaper reader in the country understood it at once.",
             kick='F · Wires', size=24)

# 21 F CONTENT 2
content_text('What the wire changed first',
             ['Prices learned the day they moved',
              'Newspapers print news hours old, cities away',
              'Wire services gather the news once, sell it to all',
              'Railroad dispatchers run trains by wire',
              'News and travel never move together again'],
             "Follow the wire into work, in the order the changes came. Commerce first: a merchant or a cotton factor who knows today's price in New York or Liverpool acts on knowledge that used to be a week old and a guess, and markets that had moved at the speed of ships began moving at the speed of signals. News second: papers organized cooperative wire services to share the cost of telegraphic dispatches, the Associated Press among them by 1846, and an event hundreds of miles away entered the evening edition the day it happened. Railroads third: dispatchers running single track lines by telegraphic train order made the two networks partners, wires on poles beside the rails. Underneath all three stands the section's definition, the one students must carry out verbatim in substance: the telegraph separated the speed of news from the speed of travel for the first time in human history.",
             kick='F · Wires', size=24)

# 22 G DIVIDER
divider_text('Section G', 'The Gain and the Cost Together',
             'Cheaper goods, cash wages, and same day news, against the bell, the speedup, and the panic that broke the unions.',
             "End the narrative where the reading ends, holding the gain and the cost in one frame, because holding them together is the lesson's main discipline and the writing task's whole demand. The gain is not propaganda: goods really did grow cheaper and more various, a farm daughter really could earn and keep cash wages, and a merchant's or a reader's world really did widen past the horizon. The cost is not rhetoric either: the working day was set by a bell and its pace by a speedup, households were bound to markets they could not see, the looms were fed by cotton picked by enslaved people, and the Panic of 1837, which students met in Lesson 4 as a banking collapse, here reappears breaking the young trade unions. Section G also hands the course forward: an economy of wage labor, corporations, and instant news is the ground the reformers of Lesson 6 are about to organize on.")

# 23 G CONTENT
content_text('What the change settled, and left open',
             ['Production out of the household, for good',
              'Time set by bell, clock, and timetable',
              'Wage labor and combination grow together',
              "The market's reach exceeds anyone's control",
              'Who the remaking served: still argued'],
             "Take the five results one by one and ask, of each, who decided it. Production: once a factory could sell to a continent, household making for home use could not compete on price, and the change ran one way. Time: bells, timetables, and telegraphic dispatches taught a whole people to live by the clock in place of the sun and the season. Combination: the same gathering that disciplined workers taught them to act together, in turn outs, unions, and magazines. Reach: by 1848 an Ohio farmer's income could be decided by a cotton price wired from New York and a credit decision made in London, powers no vote of his could touch. And the open question, the one the reading leaves standing and the writing task takes up: whether ordinary Americans, inside this new machinery, held more control over their lives, or less.",
             kick='G · The gain and the cost', size=24)

# 24 GLANCE
s = slide(NAVY)
kicker(s, 'The market revolution at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Movement, making, and news', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Moving goods', 'Erie Canal, 1825', 'Freight $100 to under $10 a ton'),
        ('Roads of iron', '23 miles to 9,000+', '1830 to 1850, winter and summer'),
        ('Making things', 'Factory system; standard parts', "The employer's machines; the bell"),
        ('The mill women', 'Lowell system; the Offering', 'Turn outs, 1834 and 1836'),
        ('News by wire', 'Morse, May 24, 1844', 'News separated from travel')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=20, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 0.85
notes(s, "This slide mirrors the summary table at the end of the guided notes, The Market Revolution at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. Read the rows as one account rather than five summaries. Movement made the market national: a canal that cut freight by nine tenths, and railroads that multiplied track four hundred fold in twenty years. Making followed movement into the factory, where the employer owned the machines and the bell owned the hours. The mill women row is the account in persons: wages, a magazine, and two strikes. The last row is the revolution turned inward on knowledge itself, news arriving faster than any traveler, which is why 1844, and not a battle or an election, is this lesson's closing date.")

# 25 VOCAB A
vocab('Words for the change',
      [('market revolution', 'households turn to distant markets, 1815 to 1848'),
       ('factory system', "the employer's building, machines, and set hours"),
       ('Lowell system', 'mills, boardinghouses, and churches built together'),
       ('interchangeable parts', 'any part fits any unit, to a standard pattern')],
      "Definitions, verbatim from the guided notes. market revolution: the transformation of the American economy between about 1815 and 1848, when canals, steamboats, railroads, and the telegraph cut the cost and time of moving goods and news, and households that had made most of what they used began producing for distant markets and buying from them. factory system: the organization of production in which workers gather in one building to work set hours at machines owned by their employer, replacing the older pattern of artisans and households making goods at their own pace in their own shops and homes. Lowell system: the labor system of the mills at Lowell, Massachusetts, where the Boston Associates built factories, boardinghouses, and churches together and recruited young women from New England farms to work the looms under rules meant to guard their morals and their hours. interchangeable parts: the manufacturing method, perfected in the federal armories and spread through New England shops, of filing and machining every part of a product to a standard pattern so that any part fits any unit and a broken one can be replaced without a craftsman's hand fitting.")

# 26 VOCAB B
vocab('Words for the wire and the answer',
      [('telegraph', 'news separated from travel, 1844'),
       ('Samuel F. B. Morse', 'the painter who built the first line'),
       ('trade union', 'bargain over wages and hours; strike when it fails')],
      "Three more terms, again matching the guided notes exactly. telegraph: the electromagnetic signaling system Samuel Morse demonstrated to Congress and opened between Washington and Baltimore in 1844, which separated the speed of news from the speed of travel for the first time in human history. Samuel F. B. Morse: the painter turned inventor who developed the electromagnetic telegraph and the code of dots and dashes named for him, and whose first line, built with a federal appropriation, carried its first message on May 24, 1844. trade union: an organization of workers in a trade formed to bargain over wages and hours and to strike when bargaining failed, which spread through the cities in the 1830s until the courts, the panic of 1837, and employer resistance broke most of them. Read the set as the lesson's closing arc in three stops: the machine, the man the machine is named for, and the organizations of the workers the new economy made.")

# 27 SYNTHESIS
content_text('Judging the change whole',
             ['Goods cheaper; markets suddenly near',
              'Wages in cash, and a printed voice',
              'The bell, the speedup, and the blacklist',
              'Cotton picked by enslaved people fed the looms',
              'The writing task asks for one judgment, defended'],
             "Close the teaching here, before the work slide, and model the judgment the writing task will ask for. Each verdict has a record. More control: Farley's wages and her liberty to withdraw, markets brought within a farm's reach, a magazine and a union built by the workers themselves. Less control: the corporation's rules reaching into the evening, the leaders of 1834 dismissed and blacklisted, households exposed to prices and panics arriving from beyond any horizon they could see, and looms fed by slave grown cotton tying Lowell's freedom to the South's bondage. The strongest student writing picks one verdict, builds it from at least three of the activity's records, and answers the best record against it instead of pretending it is not there. Note for the class that the women of Lowell are themselves the finest arguers on both sides of this question, sometimes in the same document.",
             kick='Synthesis', size=24)

# 28 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['What did the factory and the telegraph do to the way Americans lived and worked? Build the file first, then judge from it.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Market Revolution File: five stations, a file, and a verdict on control'),
        ('Notebook', 'Notebook page: the change charted in five rows, and the change in one paragraph'),
        ('Quick check', 'The Mill Woman and the Wire: the defense, the canal numbers, and the message'),
        ('Writing', 'More Control, or Less: one judgment defended from both halves of the bank')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the factory system defined, the canal numbers stated, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Market Revolution File, runs five stations: the mill woman's defense of 1840 from the audited bank record, read for her three grounds and her one concession; Morse's first message from the audited bank record, read whole at four words with its tape; a labeled teaching summary of the railroad record, labeled because no single period text carries the mileage; a labeled teaching summary of the corporation's rules at Lowell; and a labeled teaching summary of the turn outs of 1834 and 1836. Students build the file in Part 2 and defend a verdict of more control or less. The notebook page charts the same five parts. The quick check works from the defense and the message. The writing task turns the verdict into an essay from both halves of its bank.")

dc.save(OUT)
