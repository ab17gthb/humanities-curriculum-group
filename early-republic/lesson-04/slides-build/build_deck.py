#!/usr/bin/env python3
"""Early Republic Lesson 4 deck, Lewis and Clark and the Peoples of the West,
built to the approved system: image-led slides, fragments only on screen,
comprehensive speaker notes, full lesson and vocabulary coverage.
Fonts: Georgia titles, Lato body."""
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
OUT = os.path.join(HERE, '..', 'lesson-04-slides.pptx')

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
text(s, 0.9, 5.32, 11.5, 0.4, 'THE EARLY REPUBLIC AND EXPANSION · LESSON 4', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Lewis and Clark and the Peoples of the West', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'The Corps of Discovery among the nations whose country it crossed, 1804 to 1806', size=17, color=POWDER)
notes(s, "The image is Charles Marion Russell's Lewis and Clark on the Lower Columbia, painted in 1905, a century after the expedition it imagines, and students should hear that date whenever expedition art appears in this lesson: almost no image of the journey was made during it, and the famous ones are later imaginings. The lesson asks two joined questions. What did the Corps of Discovery actually find in the West, and whose country was it? The finding comes first in the hour: no single water route, ranges of mountains, and a record of maps and journals. The ownership runs underneath every stage of it: Mandan and Hidatsa towns, Shoshone horses, Nez Perce guides, and a treaty system that had been taking the West since 1795.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("What did the Corps of Discovery actually find in the West, and whose country was it?", {})]],
     size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the United States turn its Constitution into a working government, and what did continental expansion do to the republic that government served?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "The lesson question joins a geography question to an ownership question, and the joining is the lesson. Actually find presses students past the celebration version: the corps was sent to find a water communication across the continent for commerce, and it found that no such single route existed, that the Rocky Mountains were ranges rather than a single ridge, and that the country between the Missouri and the Pacific was governed, farmed, hunted, and traded over by Native nations whose help the journey required at every stage. Whose country asks students to keep those nations in the frame as actors with purposes of their own, feeding, horsing, guiding, refusing, and trading, rather than as scenery the expedition passed. Both halves are graded in the writing task, and neither half earns credit alone.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'An inhabited country, surveyed', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'An errand of the purchase', 'Jefferson orders commerce, knowledge, friendship, 1803'),
        ('B', 'A river country already inhabited', 'Mandan and Hidatsa towns; passage negotiated'),
        ('C', 'The winter hire', 'Charbonneau engaged; Sacagawea interprets'),
        ('D', 'The mountains and the kinship', 'Great Falls; Cameahwait recognized, August 1805'),
        ('E', 'The crossing and the winter vote', 'Bitterroots in snow; York and Sacagawea vote'),
        ('F', 'The return and the uses of the record', 'St. Louis, September 1806; maps and the fur trade'),
        ('G', 'The treaty system behind the story', 'Greenville, 1795; cession before the corps')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "The map follows the guided notes section by section. Section A reads Jefferson's instructions of June 20, 1803 as the expedition's design: commerce, geography, a census of nations, and friendly treatment ordered in one document. Section B places the corps in an inhabited river country, wintering beside Mandan and Hidatsa towns larger than St. Louis. Section C hires Charbonneau for Sacagawea's interpreting. Section D crosses the Great Falls portage to the Shoshone meeting of August 1805. Section E crosses the Bitterroots, reaches the Pacific, and records the Fort Clatsop vote. Section F returns in September 1806 and follows the record into the fur trade. Section G steps back to the Treaty of Greenville of 1795, the system behind the whole story.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_photo('lewis-port.jpg', 'Section A', 'An Errand of the Purchase',
              ['Jefferson writes the orders in June 1803, and the purchase', "sends a small Army party walking into other peoples' country."],
              "The portrait is Charles Willson Peale's Meriwether Lewis, painted about 1807, after the expedition's return, and it shows the captain as the republic wanted him remembered: a uniformed officer of a successful errand. Teach the orders before the journey, because the journey was the orders executed. Jefferson's instructions of June 20, 1803, read at Station 2 in the Library of Congress transcription, name the object without decoration: the most direct and practicable water communication across the continent for the purposes of commerce. Around that object the president built a census, a geography, and a diplomacy. Students who start with the keelboat start with adventure. Students who start with the instructions start with a government, which is where this unit insists the story begins.",
              title_size=34)

# ------------------------------------------------------ 5 THE ORDERS
content_text('What Jefferson ordered, June 20, 1803',
             ['Explore the Missouri; find a water route for commerce',
              'Fix the geography by observation, point by point',
              'Learn the nations: names, numbers, lands, trade',
              'Treat them in the most friendly, conciliatory manner',
              'Report everything to the government that sent you'],
             "Read the three orders as one design rather than a list. The commerce order explains the geography: a water communication was wanted because furs and goods move cheaply by water, and Jefferson hoped the Missouri and a Pacific river nearly met. The census order explains the diplomacy: a party of some forty men could not fight its way through a continent of nations, so friendly and conciliatory treatment, and satisfying the nations of the journey's innocence, were working instructions for survival. The reporting order explains the journals: observations were to be taken with great pains and accuracy and rendered to the government, in copies, on birch paper if needed against damp. Knowledge was the cargo. The expedition carried trade goods west; what it was built to carry home was information, and every later section of this lesson is that design meeting a country that had its own designs.",
             kick='A · An errand of the purchase', size=24)

# ------------------------------------------------------ 6 THE PARTY
content_photo('clark-port.jpg', 'The party that set out, May 1804',
             ['Some forty men: soldiers, interpreters, boatmen',
              'Clark journal, May 14: 4.5 miles, rain, high spirits',
              'York crosses with the corps, enslaved by Clark',
              'No roster of the first day names him'],
             "The portrait is Charles Willson Peale's William Clark, painted in 1810, four years after the return. Set the party's makeup from Clark's own first entry, read at Station 3: a boat of twenty oars with 22 men, a sergeant and seven Frenchmen in one large pirogue, a corporal and six soldiers in another, four and a half miles made under sail in the rain, the men in high spirits. The roster teaches two lessons at once. The expedition depended from its first afternoon on French boatmen whose river craft the Army did not possess, a dependence that only deepened upriver. And the roster omits by name the man who would cross the whole continent in it: York, enslaved by Clark since boyhood, appears in the journals at work for two years and appears in no first day accounting of the party he served.",
             kick='A · An errand of the purchase')

# ------------------------------------------------------ 7 STAT 40
stat('40', 'men, about, in the party that set out in May 1804',
     'Soldiers, interpreters, French boatmen, and York · An Army detachment, not a multitude',
     "State this figure as the reading states it: some forty men, an approximation the lesson keeps because the party's count shifts with hires, detachments, and the permanent party that formed at Fort Mandan. The number's teaching value is its smallness. Forty men, fewer than a modern school bus carries twice over, were sent to cross a continent held by nations that could field hundreds of warriors within a day's ride of the river, and to come back with its geography. Everything the expedition achieved by way of passage was therefore achieved by negotiation, gift, interpreting, and Native hospitality rather than by force, which the record confirms: in more than two years the corps fought once. When students picture the expedition as an army conquering distance, correct the picture with this slide: it was a detachment asking its way through other peoples' country, and mostly being answered.",
     kick='A · An errand of the purchase')

# ------------------------------------------------- 8 SECTION B DIVIDER
divider_photo('mandan-port.jpg', 'Section B', 'A River Country Already Inhabited',
              ['The Missouri the corps ascended was a lived in river,', 'its towns larger than the city the corps had left.'],
              "The image is George Catlin's bird's eye view of a Mandan village, painted between 1837 and 1839, a generation after the corps wintered beside villages of this kind, and it is used in the activity with that date stated: it records the village form, the earth lodges above the river, not the winter of 1804 itself. Open the section with the towns, because the reading does. The Mandan and Hidatsa villages near the Knife River were trading centers older than St. Louis, farming corn, beans, and squash and exchanging with peoples across the northern plains. The Corps of Discovery did not carry civilization up an empty river. It arrived, hungry and late in the season, at somebody else's city, and asked to winter there.",
              title_size=34)

# ------------------------------------------------------ 9 INHABITED RIVER
content_text('Towns larger than St. Louis',
             ['The Mandan and Hidatsa villages feed and house the corps',
              'Fort Mandan winter, 1804 to 1805: survival by hospitality',
              'The Teton Sioux confrontation stops short of violence',
              'Passage is negotiated, never simply taken',
              'The journals name, count, and describe it all for Washington'],
             "Teach the winter as a transaction between peoples, not a bivouac. The villages supplied corn through the winter, information about the river above, and the expedition's link to the Shoshone country it had to reach, and the corps supplied smith work, medicine, and trade in return, with Clark treating Native patients at the fort. The Teton Sioux meeting of the previous September belongs in the same lecture as the hospitality's other face: a nation that controlled the river demanded terms for passage, the meeting stopped at the edge of violence, and the corps went on because the confrontation was talked down, not won. The journals ran through both kinds of meeting as an instrument of possession, naming rivers and counting nations for the government. Hospitality kept the expedition alive; the record it kept was already converting the hosts' country into American information.",
             kick='B · A river country already inhabited', size=24)

# ------------------------------------------------- 10 SECTION C DIVIDER
divider_text('Section C', 'The Winter Hire',
             'The corps engages a trader for his wife: a Shoshone interpreter, a mother, and the party of peace her presence announced.',
             "Frame the hire precisely, because the familiar version reverses it. At Fort Mandan in November 1804 the captains engaged Toussaint Charbonneau, a French Canadian trader living among the Hidatsa, and the journals give the reason in the hiring itself: his wives were Snake, or Shoshone, women, and he was to take one of them to interpret the Snake language. The wife chosen was Sacagawea, about sixteen or seventeen years old (stated as an estimate in most accounts, and best taught that way), pregnant with her first child, and a captive: the Hidatsa had taken her from her Shoshone people as a girl in a raid years before. The expedition's most famous member joined it as another man's wife, another people's prisoner, and its best hope of speaking to the nation whose horses it had to have.")

# ------------------------------------------------------ 11 SACAGAWEA
content_photo('russell-port.jpg', 'Sacagawea, interpreter and sign of peace',
             ['Taken captive by the Hidatsa as a girl; carried east',
              'Interprets between her people and the villages',
              'A woman and an infant read as a party of peace',
              'Jean Baptiste born at Fort Mandan, February 1805'],
             "The image is Russell's 1905 painting of the expedition on the Lower Columbia, a later imagining used throughout this lesson with its date attached; no portrait of Sacagawea was made in her lifetime, and students should be told plainly that every picture of her is an artist's invention. Her documented work needs no invention. She interpreted, gathered and identified foods, recognized the country of her childhood as the corps neared the Shoshone, and on May 14, 1805, a year to the day after the start, she recovered the captains' instruments and papers from a pirogue that had swamped, an act the journals praise in their own pages. Her presence also spoke before she did: a war party does not travel with a woman and a newborn, and nation after nation read the corps accordingly. Presence, kinship, and language were her contributions, and the expedition could not have bought any of them.",
             kick='C · The winter hire')

# ------------------------------------------------- 12 SECTION D DIVIDER
divider_text('Section D', 'The Mountains and the Kinship',
             'A month at the Great Falls, a hungry road to the divide, and a council that turns on a sister recognizing her brother.',
             "Set the section's stakes before its famous scene. By the summer of 1805 the expedition's design had met its first hard fact: the Missouri was not a road to the sea but a river that climbed into mountains, and the portage around the Great Falls consumed about a month of carrying boats and baggage overland. Beyond the falls the party was short of food and entirely dependent on reaching the Shoshone, whose horse herds were the only known way over the ranges ahead. Lewis went forward with a small party and met the Shoshone in August, on ground Sacagawea had been carried away from as a girl. What the corps needed from that meeting was not information. It was transport, permission, and time, all held by a people who owed the strangers nothing.")

# ------------------------------------------------------ 13 FALLS AND HORSES
content_text('The falls, the hunger, the horses',
             ['The Great Falls portage consumes about a month',
              'Beyond the falls, the party works toward the divide, short of food',
              'Shoshone horses are the only way over the mountains',
              'Lewis meets the Shoshone first, in August 1805',
              'Everything now waits on one council'],
             "Follow the logistics, because the recognition scene lands harder when students know what rode on it. The Great Falls of the Missouri were not one fall but a staircase of them, and the portage, some eighteen miles of hauling the boats and baggage around them on improvised wagons, took about a month of the short mountain summer. The corps reached the Three Forks and the Beaverhead country hungry, its canoes useless beyond the divide, its baggage far beyond what men could carry over snow passes. Horses were not a convenience in this calculation. They were the expedition itself, continued or ended, and the only herds within reach belonged to the Shoshone. Lewis's advance meeting was therefore a negotiation conducted from weakness, by a captain whose party numbered a handful, in a country where his hosts could have ended the enterprise by leaving. That they did not leave is Section D's second slide.",
             kick='D · The mountains and the kinship', size=24)

# ------------------------------------------------------ 14 THE COUNCIL
content_text('August 17, 1805: the recognition',
             ['Sacagawea is called in to interpret',
              'In the chief Cameahwait, she recognizes her brother',
              'Four languages carry every word of the council',
              'The objects of the journey are stated in full',
              'Horses, and passage west, follow from the meeting'],
             "Read Lewis's journal entry at Station 4 before summarizing it here, in the Moulton edition's text: shortly after Clark arrived, the Indian woman proved to be a sister of the chief Cameahwait, and the meeting of those people was really affecting. Lewis records her reunion with a woman captured in the same raid who had escaped and rejoined the nation, a reminder that the council sat inside Sacagawea's own history of loss. Then trace the interpreting chain aloud: English to French by Labiche, French to Hidatsa by Charbonneau, Hidatsa to Shoshone by Sacagawea, every sentence of American policy reaching the Shoshone through the voice of their own stolen daughter, now returned with a child in her arms. The trade that followed, horses for goods, was a transaction between peoples. It was also a family reunion doing diplomatic work no medal or speech could have done.",
             kick='D · The mountains and the kinship', size=24)

# ------------------------------------------------------ 15 STAT 4
stat('4', 'languages in the chain that carried the Shoshone council',
     'English, French, Hidatsa, Shoshone · Every word of the expedition passed through Sacagawea',
     "Count the chain slowly, because this small number carries the lesson's argument in miniature. At the council of August 1805, Lewis spoke English. Labiche rendered it into French. Charbonneau rendered the French into Hidatsa, the language of the villages where Sacagawea had been held. Sacagawea rendered the Hidatsa into Shoshone, her first language, for her brother's people. Four languages, three interpreters, and one indispensable person: remove Sacagawea and the chain breaks at its final link, the captains are reduced to signs, and the objects of the journey Jefferson had ordered stated in full cannot be stated at all. The same structure ran all the way up the river in smaller chains, through French boatmen, village interpreters, and sign talk. An expedition remembered as two captains and a wilderness was in practice a traveling exercise in other peoples' languages.",
     kick='D · The mountains and the kinship')

# ------------------------------------------------- 16 SECTION E DIVIDER
divider_text('Section E', 'The Crossing and the Winter Vote',
             'Snow in the Bitterroots, Nez Perce food and guidance, the Columbia reached, and a vote in the rain at the rivers mouth.',
             "Introduce the crossing as the expedition's hardest labor performed on other peoples' knowledge. Shoshone guides, and then the Nez Perce, who fed the starving party as it came out of the Bitterroot Mountains in September 1805 and guided it to the Clearwater, knew the trails, the seasons, and the foods of the country the corps was crossing for the first time. The descent of the Columbia that followed was the journey's fastest water, and it ended in a wet winter camp near the river's mouth among the Clatsop. Hold the section's two halves together for students: the divide was crossed, which was the errand's geographic test, and at the far side of it the party did something no order had foreseen, which is the next slide's subject.")

# ------------------------------------------------------ 17 THE VOTE
content_text('Fort Clatsop and the vote, November 1805',
             ['The divide is crossed; no single water route lies beyond it',
              'The Nez Perce feed and guide the party out of the snow',
              'Down the Columbia to a winter at Fort Clatsop, in the rain',
              'The camp site is polled, and the journals record every vote',
              'York votes. Sacagawea votes. Neither could vote at home'],
             "Teach the vote with its exact setting, because its meaning lives in the details. In late November 1805, choosing between wintering grounds near the Columbia's mouth, the captains polled the whole party and Clark recorded the preferences in his journal, name by name: the enlisted men, Charbonneau, Sacagawea, who is recorded favoring a place with plenty of potas, or wapato, and York. It was an expedient of a small command at the edge of the continent, not a constitutional act, and students should not inflate it into one. Its weight is documentary: the expedition's own book shows an enslaved man and a Native woman counted in a decision, without comment, by the same record that elsewhere counts York as Clark's property and Sacagawea as an interpreter's wife. The journals hold the vote and the unfreedom together, which is why this lesson reads them together.",
             kick='E · The crossing and the winter vote', size=24)

# ------------------------------------------------- 18 SECTION F DIVIDER
divider_photo('map-port.jpg', 'Section F', 'The Return and the Uses of the Record',
              ['Home in September 1806, with maps that redrew a continent', 'and journals that opened a trade up the same river.'],
              "The image is a detail of the map of the expedition's track published in 1814, copied by Samuel Lewis from Clark's drawing and engraved by Samuel Harrison, the expedition's own cartographic monument and the reading's figure. Use it to frame the return as a delivery: the party that reached St. Louis in September 1806 carried home journals, specimens, and the makings of this map, and the map is the errand's product made visible, a continent redrawn for the government that had bought a claim on paper in 1803. Its honest finding is written across the Rockies: not one water passage but range after range, correcting the geography of hope Jefferson had sent the corps to test. What the government, and then the fur trade, did with the delivered record is this section's second half.",
              title_size=34)

# ------------------------------------------------------ 19 THE RETURN
content_text('St. Louis, September 1806, and after',
             ['One man lost to illness: Sergeant Floyd, August 1804',
              'Two Blackfeet killed in the journeys only violent encounter',
              'The maps correct the hope of an easy water passage',
              'The journals open a fur trade up the Missouri',
              'Smallpox destroys the Mandan villages a generation later'],
             "State the return's accounting in the reading's own terms. The corps lost one man, Sergeant Charles Floyd, to illness in August 1804, a death no discipline on the journey could have prevented, and its single killing of Native people came on the return, in July 1806, when a party under Lewis fought with Blackfeet men over attempted theft of guns and horses and two Blackfeet died. The delivered record then went to work: Clark's maps replaced conjecture with surveyed rivers and real mountain ranges, and traders followed the journals up the Missouri within a few years, building the fur trade on the expedition's geography and its Native relationships. The Mandan villages stood in that trade's path, as entrepots and then as victims: in 1837 smallpox reached them by steamboat and destroyed them as a people in their old towns, the costliest single line in the record's long ledger.",
             kick='F · The return and the uses of the record', size=24)

# ------------------------------------------------- 20 SECTION G DIVIDER
divider_text('Section G', 'The Treaty System Behind the Story',
             'Nine years before the keelboat, a treaty at Greenville took most of Ohio. The corps extended a system; it did not begin one.',
             "Open the closing section by moving the camera back nine years and fifteen hundred miles east, to Greenville in the Ohio country in August 1795. There the Western Confederacy of Native nations, defeated by Anthony Wayne's army at Fallen Timbers the year before, signed the treaty read at Station 1: prisoners restored, peace declared perpetual in its first article, and in its third the cession, forever, of the tribes' claims to the lands east and south of the boundary line, most of present day Ohio. That instrument, not the keelboat, is the decade's characteristic American document in the West: a treaty made after a defeat, exchanging goods and promises for land, and opening the ceded country to settlement. The expedition belongs inside that sequence, and students grade better verdicts when they can say what the sequence was.")

# ------------------------------------------------------ 21 GREENVILLE SYSTEM
content_text('Purchase, pressure, and cession lines',
             ['1795: Greenville cedes most of present day Ohio',
              'Its first article promises peace shall be perpetual',
              'Goods and yearly payments stand against the cession',
              'The pattern repeats across the West for a century',
              'The corps surveys the next country in line'],
             "Teach the treaty as a system with parts, because the pattern is the point. Military pressure came first, Fallen Timbers in 1794. The council followed at the victor's headquarters, with named nations on both sides of the document. The written instrument then converted the defeat into title: a boundary line, a cession stated to run forever, goods delivered and yearly payments promised, and protection accepted in language that later treaties would shrink again. Settlement followed the line, and the line moved west in the next negotiation. Jefferson's government knew this machinery from the inside when it wrote the instructions of 1803, and the corps's census of names, numbers, and lands was compiled by the same state that had drawn the Greenville line. The expedition read as exploration alone misses the office it belonged to. Read with Greenville behind it, it is the survey party of a system already at work.",
             kick='G · The treaty system behind the story', size=24)

# ------------------------------------------------------ 22 AT A GLANCE
s = slide(NAVY)
kicker(s, 'The journey at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Carried, and carrying', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The orders and the river', 'Instructions, 1803; out May 1804', 'A water route for commerce; the nations counted'),
        ('The peoples who carried it', 'Mandan winter; the August 1805 council', 'Hospitality, horses, interpreting, guidance'),
        ('The mountains and the vote', 'Bitterroots; Fort Clatsop, November 1805', 'The divide crossed; York and Sacagawea vote'),
        ('The return and the system', 'St. Louis, 1806; Greenville behind it, 1795', 'Maps, the fur trade, and the cession pattern')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.2, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.25, yy + 0.05, 5.1, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.55, yy + 0.05, 3.9, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the closing table of the guided notes, The Journey at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The orders and the river: Jefferson's instructions of June 20, 1803, the Missouri explored for a water communication for commerce, the corps out in May 1804, some forty men including York. The peoples who carried it: the Mandan and Hidatsa villages feeding and housing the corps at Fort Mandan, and the Shoshone horses obtained through Sacagawea's recognition of Cameahwait in August 1805. The mountains and the vote: the Bitterroots crossed in snow with Nez Perce help, and the Fort Clatsop vote of November 1805. The return and the system: St. Louis in September 1806, the maps and the fur trade, and Greenville in 1795 behind the whole story. Grade the table on dates, actors, and whose country each stage crossed.")

# ------------------------------------------------------ 23 VOCAB A
vocab('Words for the expedition and its captains',
      [('Corps of Discovery', 'the Army expedition of 1804 to 1806'),
       ('Meriwether Lewis', 'co-commander; kept the scientific record'),
       ('William Clark', 'co-commander; drew the maps'),
       ('Sacagawea', 'Shoshone interpreter; carried her son across')],
      "These definitions match the guided notes, and the notes carry them in full, word for word. Corps of Discovery: the Army expedition of 1804 to 1806, commanded by Meriwether Lewis and William Clark, sent by President Jefferson to explore the Louisiana Purchase, find a water route toward the Pacific, and establish an American presence among the West's peoples. Meriwether Lewis: the Army captain and former secretary to President Jefferson who co-commanded the Corps of Discovery, kept its scientific record, and governed Louisiana Territory after the expedition's return. William Clark: the Army officer who co-commanded the Corps of Discovery with Lewis, drew its maps, and negotiated much of its diplomacy with Native nations, treating the expedition's enslaved member, York, as his property throughout. Sacagawea: the Shoshone woman who joined the Corps of Discovery as an interpreter with her husband in 1804, carried her infant son across the continent, and whose presence and kinship opened doors, including her own people's, that the expedition could not have opened alone.")

# ------------------------------------------------------ 24 VOCAB B
vocab('Words for the peoples and the divide',
      [('York', 'enslaved by Clark; voted; refused his freedom'),
       ('Shoshone', "Sacagawea's people; holders of the horses"),
       ('continental divide', 'the high ground between two oceans of rivers')],
      "Three more terms, in the guided notes wording, carried in these notes in full, word for word. York: the enslaved man held by William Clark who crossed the continent with the Corps of Discovery, hunted, scouted, and voted in the expedition's decisions, and who asked for his freedom on the return and was refused for years. Shoshone: the Native nation of the northern Rockies and Great Basin, Sacagawea's people, whose horses the Corps of Discovery needed to cross the mountains in 1805 and obtained through the meeting between Sacagawea and her brother Cameahwait. continental divide: the high ground of the Rocky Mountains separating the rivers that flow toward the Atlantic from those that flow toward the Pacific, which the Corps of Discovery crossed in 1805 and found no single water route beyond. Notice what the three terms hold together: a man denied his freedom, a nation holding the crossing, and a geography that refused the errand's hope.")

# ------------------------------------------------------ 25 CLOSING SYNTHESIS
s = slide(NAVY)
kicker(s, 'Closing synthesis')
text(s, 0.9, 1.35, 11.5, 1.1, 'Two facts, held together', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 2.6,
     ["The expedition was a triumph of endurance and record keeping, carried out by soldiers and by the peoples who fed, guided, horsed, and interpreted for them.",
      "It was also the first page of a dispossession, a survey of other peoples' countries by a republic that had already decided what the survey was for."],
     size=23, color=POWDER, leading=1.3)
notes(s, "Close the lesson by refusing to let either closing fact absorb the other, because the reading's discipline is exactly that refusal. The triumph is real and documented: a party of some forty crossed a continent and back in twenty eight months, lost one man, fought once, and delivered maps and journals that corrected the geography of half a continent. The dispossession is equally documented and begins earlier than the triumph: Greenville took most of Ohio in 1795, Jefferson's census of nations was compiled for the government that drew that line, the fur trade followed the journals up the Missouri within years, and smallpox destroyed the Mandan towns that had wintered the corps. Students who hold only the first fact repeat the expedition's own account of itself. Students who hold only the second cannot explain why the record still repays reading. The verdict work in the activity is graded on holding both, with stations cited.")

# ------------------------------------------------------ 26 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ["What did the Corps of Discovery actually find in the West, and whose country was it? Keep the geography and the ownership joined, account for York, and defend your label against its strongest rival."],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Expedition File: the treaty, the orders, the journal, the council, York'),
        ('Notebook', 'Notebook page: the journey stage by stage, whose country at each stage'),
        ("Quick check", "The Orders and the First Day: Jefferson instructions beside Clark's first entry"),
        ('Writing', 'Explorers, Diplomats, or Surveyors: your verdict defended from the file')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the corps and the divide defined, the council in two sentences, and the lesson question in two or three.',
     size=15, color=POWDER)
notes(s, "Close the lesson by handing the verdict to the students, which is what this lesson exists to do. The activity, The Expedition File, gives them the Treaty of Greenville from the audited bank record, Jefferson's instructions in the Library of Congress transcription, Clark's first journal entry from the bank record, the Shoshone meeting from the Moulton edition of the journals, and a labeled teaching summary of York's service and refused petition, and asks them to judge whether the corps was chiefly explorers, diplomats, or surveyors for settlement. The notebook page charts the journey stage by stage with the country named at each stage. The quick check sets the orders beside the first day's entry. The writing task asks for the verdict defended against its strongest rival label, with the dependence and York's record carried at full strength. The exit ticket has three parts: the Corps of Discovery and the continental divide defined, the August 1805 council stated in two sentences, and the lesson question answered with the two closing facts held together.")

dc.save(OUT)
