#!/usr/bin/env python3
"""Early Republic Lesson 5 deck, "The War of 1812," built on the shared
deck system: image-led slides, fragments only on screen, comprehensive
speaker notes, full lesson and vocabulary coverage."""
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

def content_photo_s(img, title, items, note, kick=None, size=21):
    s = slide(CREAM)
    photo_right(s, img)
    if kick: kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95 if kick else 0.8, 6.9, 1.2, title, size=31, color=NAVY, font='Georgia', leading=1.05)
    frags(s, items, y=2.12 if kick else 2.0, size=size, gap=11, leading=1.2)
    notes(s, note)
    return s

# 1 TITLE
s = slide(NAVY)
photo_right(s, 'fortmchenry-port.jpg')
text(s, 0.9, 1.5, 6.9, 0.4, 'THE EARLY REPUBLIC · LESSON 5', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 2.0, 6.9, 2.2, 'The War of 1812', size=44, color=CREAM, font='Georgia', leading=1.1)
rule(s, 0.92, 4.15)
text(s, 0.9, 4.5, 6.8, 1.6, 'Why the United States went to war with Britain again, and what the war actually settled', size=20, color=POWDER, leading=1.3)
notes(s, "The image is John Bower's aquatint of the bombardment of Fort McHenry, published in Philadelphia about 1816, showing British bomb ships throwing shells over the fort on the morning of September 13, 1814. It opens the lesson because the flag over that fort became the war's most durable product. Set the hour's frame before any detail. The last lessons followed the republic west, into Louisiana and up the Missouri. This lesson turns back to the Atlantic, where an older quarrel had never closed. Britain and France had been at war since 1803, American trade was being seized by both, and American sailors were being taken by one. Students will follow the grievances, the peaceful weapon that failed, the western war inside the war, the declaration, the burnings, and the peace that settled none of it on paper.")

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('Why did the United States go to war with Britain again, and what did the war actually settle?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the United States turn its Constitution into a working government, and what did continental expansion do to the republic that government served?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "The lesson question has two halves, and the second half is the harder one. The first half asks for causes, and the documents state them plainly: impressment, the Orders in Council, the blockades, and in the West a fight over land that Tecumseh's confederacy was built to stop. The second half asks what the war settled, and the honest answer comes in two layers that students must keep apart. On paper the Treaty of Ghent settled none of the stated causes. In fact the war settled Canada, the western confederacies, the Federalist Party, and the country's sense of itself. Tell students now that the writing task will ask them to judge the war whole, won, lost, or merely survived, and that every section of this lesson hands them evidence for more than one verdict.")

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'A second war with Britain, and a strange peace', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'Caught between empires at sea', 'Orders in Council; impressment'),
        ('B', 'The peaceful weapon that failed', 'The embargo of 1807; repeal in 1809'),
        ('C', 'The West\u2019s war inside the war', 'Tecumseh; Prophetstown; Tippecanoe'),
        ('D', 'The declaration of 1812', 'War Hawks; Madison\u2019s message; the close vote'),
        ('E', 'Washington burned, Baltimore held', 'York; Fort McHenry; Horseshoe Bend'),
        ('F', 'Hartford, Ghent, and New Orleans', 'Amendments; the treaty; the late battle'),
        ('G', 'What the war settled', 'Nothing on paper; nearly everything in fact')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A states the grievances at sea. Section B follows Jefferson's embargo, the peaceful weapon that punished Americans and moved no one abroad. Section C takes the war west, to Tecumseh's confederacy and Tippecanoe. Section D declares the war, through the War Hawks and Madison's ranked message. Section E fights it: Canada, two burned capitals, Baltimore, and Horseshoe Bend. Section F ends it, at Hartford, at Ghent, and below New Orleans. Section G weighs the settlement. Tell students the summary table at the end of their guided notes, The War of 1812 at a Glance, asks them to rebuild exactly this map.")

# 4 A DIVIDER
divider_text('Section A', 'Caught Between Empires at Sea',
             'Two empires at war made American trade a prize and American sailors a recruiting ground.',
             "Begin with the world the young republic had to trade in. France and Britain had been at war, with one short pause, since 1793, and at full pitch since 1803. Britain ruled the seas and France held much of the continent, and each power tried to starve the other by closing its ports to neutral ships. The United States was the largest neutral carrier, which made American ships, American cargoes, and American sailors worth seizing. Students should grasp that the grievances of this section were not insults on a list. They were a system: decrees and orders that made the same cargo illegal in both directions, and a manpower hunger in the Royal Navy that reached onto American decks. Section A of the guided notes asks for the parts in order: the war since 1803, the Orders in Council, the seizures, and impressment.")

# 5 A CONTENT
content_text('Two empires, one ocean',
             ['Britain ruled the seas, and France held the continent.',
              'The Orders in Council and the French decrees answered each other.',
              'The same American cargo was illegal both ways.',
              'Ships and cargoes were seized by both nations.',
              'Neutral rights were claimed, and not respected.'],
             "Work the system before the grievance, because students tend to file this war under a single insult. Britain's Orders in Council barred neutral trade with French held ports unless it passed through Britain first. Napoleon's decrees answered by barring trade with Britain and threatening any neutral that submitted to British search. An American captain sailing to Europe could thus be seized by the French for obeying Britain and by the British for obeying France, and both navies took prizes by the hundred. The United States claimed the neutral rights of a trading nation: to carry goods between ports at peace with it, under its own flag, with its own crews. Neither empire, fighting what each regarded as a war for survival, had much use for the claim. That deadlock, not a single incident, is the ground the war grew from.",
             kick='A · Caught between empires at sea', size=24)

# 6 A CONTENT 2
content_text('Impressment: men taken off American decks',
             ['Royal Navy officers stopped American vessels at sea.',
              'Sailors claimed as British subjects were taken by force.',
              'American citizens were taken with them, papers and all.',
              'Thousands were taken across the years.',
              'Madison ranked the grievance first in 1812.'],
             "Define the practice from the deck out. A British warship stopped an American merchant vessel at sea, mustered its crew, and took off any man the officer judged to be British born, to serve in the Royal Navy for the war's duration. Britain, fighting France with a navy that swallowed men, claimed its subjects owed it service wherever they were found, and it did not recognize American naturalization as an escape. The claim swept up American citizens in large numbers: men with citizenship papers in their chests were taken anyway, since officers on the spot decided who sounded British. The standard accounts count the impressed American seamen in the thousands across the years before 1812. Madison placed this grievance first in his war message, ahead of trade, because it took not cargo but citizens, and students meet his exact words at Station 2 of the activity.",
             kick='A · Caught between empires at sea', size=24)

# 7 B DIVIDER
divider_text('Section B', 'The Peaceful Weapon That Failed',
             'Jefferson closed every American port, to win neutral rights without firing a shot. The ports paid for it.',
             "Introduce the embargo as an idea before it is a failure, because it was a serious idea from a serious theory of the republic. Jefferson believed war would corrupt the government he was trying to keep small: armies, debts, and taxes were the machinery of the monarchies the republic had rejected. His alternative was economic pressure. The United States fed Britain's West Indian colonies and supplied both empires; cut off that supply, and London and Paris would respect American neutral rights to get it back. Section B follows the wager and its wreck: the act of December 1807, the collapse of exports, the smugglers, the enforcement turned inward, and the repeal of 1809. Students should leave the section able to say why the weapon failed, not only that it failed: it hurt the country that aimed it faster than the empires it was aimed at.")

# 8 B CONTENT
content_text('Jefferson\u2019s wager',
             ['The Embargo Act came in December 1807.',
              'Every American port was closed to foreign trade.',
              'Britain and France were to feel the loss, then yield.',
              'Exports collapsed by about four fifths.',
              'The act was repealed in 1809, the grievances untouched.'],
             "Teach the act's machinery from Station 1 of the activity, where students read its text. No clearance for any vessel bound to a foreign port, with one exception for vessels under the president's immediate direction. Coastwise trade, port to port inside the country, could sail only under a bond of double the value of vessel and cargo, so a captain who ran for a foreign port instead forfeited a fortune. The results came fast. Exports fell by about four fifths within a year, by the standard trade figures. Ships idled, sailors and dockworkers lost their work, and New England, which lived by the carrying trade, bore the worst of a law passed in its name as much as anyone's. Smugglers ran goods over the Canadian line and out of the coves of the coast, and federal enforcement followed them. In 1809 Congress repealed the act, and impressment and the Orders in Council stood exactly where they had stood.",
             kick='B · The peaceful weapon that failed', size=24)

# 9 B STAT
stat('80%', 'the fall in American exports in the first year of the embargo, by the standard trade figures',
     'From about 108 million dollars of exports in 1807 to about 22 million in 1808, while Britain and France held their course',
     "Give the number its context, because a giant figure can mislead if students take it as the embargo's whole effect. The trade figures are the standard ones historians cite: American exports of about 108 million dollars in 1807 fell to about 22 million in 1808, a fall of roughly four fifths, which is how the reading states it. The fall was the policy working as designed at home: the law stopped the trade it was written to stop. The failure lay abroad. Britain found other sources of supply, opened new markets in South America, and waited, while the American ports that lived by trade emptied. Ask students to hold the two halves together: the embargo was not a gesture, it was a total stop, enforced hard, and it still moved neither empire. That is why, by 1812, the men arguing for war could say the peaceful weapon had been tried at full strength and had failed.",
     kick='B · The peaceful weapon that failed')

# 10 C DIVIDER
divider_text('Section C', 'The West\u2019s War Inside the War',
             'Tecumseh built a confederacy on one claim: the land belonged to all the nations in common, and no one nation could sell it.',
             "Move the lesson west, and change the question. At sea the quarrel was over ships and sailors. In the Ohio and Indiana country the quarrel was over the land itself, and it had been running since the Treaty of Greenville in 1795, which students met in Lesson 4. The United States took the West treaty by treaty, buying cessions from individual nations, each signature real in American law and each one read by many Native people as a few chiefs selling what was not theirs alone to sell. Tecumseh's confederacy was built to end that system, and his brother's preaching gave the movement its spiritual fire. Section C follows the claim, the town built to hold it, and the battle fought there in November 1811, while Tecumseh was hundreds of miles away. Keep both leaders in view: this section has a Harrison in it as surely as it has a Tecumseh.")

# 11 C CONTENT
content_text('The land held in common',
             ['Tecumseh, a Shawnee leader, was building a confederacy.',
              'No single nation could sell the common land.',
              'Tenskwatawa, the Prophet, preached renewal.',
              'Prophetstown stood on the Tippecanoe River.',
              'Harrison answered the claim at Vincennes in 1810.'],
             "State the claim as Tecumseh made it at the Vincennes council of August 1810, which students read as a labeled teaching summary at Station 3, because the surviving English accounts of his Shawnee speech differ and this lesson prints none of them as his exact words. The land of the West, he argued, belonged to all Native nations in common; it had never been divided; therefore the Treaty of Fort Wayne of 1809, in which Harrison bought some three million acres from three nations, was void, and the land should be given back. Harrison refused the claim and the demand together. Around the argument stood the movement: his brother Tenskwatawa, called the Prophet, preaching purification and renewal at Prophetstown, and emissaries carrying the confederacy's message as far south as the Creek country. The confederacy was diplomacy, religion, and military preparation at once.",
             kick='C · The West\u2019s war inside the war', size=24)

# 12 C CONTENT 2
content_text('Tippecanoe, November 1811',
             ['Tecumseh was away in the South, seeking allies.',
              'Harrison marched on Prophetstown.',
              'The battle was fought at dawn on November 7, 1811.',
              'The town was burned, and the confederacy scattered for a season.',
              'Tecumseh turned openly to the British in Canada.'],
             "Tell the battle plainly, with its odd shape. In the autumn of 1811 Tecumseh traveled south to bring the Creeks, Choctaws, and others into the confederacy, leaving Prophetstown under Tenskwatawa's charge with orders to keep the peace. Governor William Henry Harrison marched a force of about a thousand men to the town's edge and camped. Before dawn on November 7 the confederacy's warriors attacked the camp; Harrison's army held, and the next day his men burned Prophetstown and its stores. Both sides claimed the day. Harrison's claim traveled farther: the victory made his reputation, and a generation later a presidential campaign would run on the name Tippecanoe. The strategic result was the opposite of Washington's hope. The confederacy, its town burned, turned openly to the British in Canada, and the frontier war merged into the war Madison was about to declare.",
             kick='C · The West\u2019s war inside the war', size=24)

# 13 D DIVIDER
divider_text('Section D', 'The Declaration of 1812',
             'A young Congress voted for war by the closest margin in the nation\u2019s history, and the country went to war divided.',
             "Bring the two wars together in one vote. By the spring of 1812 the maritime grievances had run for nearly a decade, the embargo had failed, and on the frontier the fighting at Tippecanoe had already happened. What changed was the Congress. The elections of 1810 sent a young generation of western and southern members to Washington who were done with submission as a policy and who said so in those terms. Section D names them, reads Madison's message in the order he ranked it, and then looks honestly at the vote: a declaration carried narrowly, against the united opposition of the Federalist Party and most of the commercial Northeast, the very region whose ships and sailors the war was declared to defend. Students should carry that division into Section F, where it hardens into the Hartford Convention.")

# 14 D CONTENT
content_text('War Hawks, and a message ranked in order',
             ['Henry Clay of Kentucky and John C. Calhoun of South Carolina led them.',
              'Canada could be taken, they argued, by marching.',
              'National honor was named as a cause in itself.',
              'Madison, on June 1, 1812, ranked impressment first.',
              'Then came the Orders in Council and the blockades.'],
             "Give the War Hawks their argument at full strength before testing it. Clay, the new Speaker of the House, and Calhoun, on the Foreign Relations Committee, held that a decade of decrees and seizures had made submission a habit other nations counted on, that Canada lay open and its conquest would end both the British pressure on the frontier and the British alliance with the western nations, and that national honor was not a decoration but a working asset a young republic could not spend down. Madison's message of June 1, 1812, which students read at Station 2, is a lawyer's document: impressment first, then the Orders in Council and the pretended blockades, then the frontier warfare he connected to British influence. Congress declared war on June 18. Note the timing students rarely hear: Britain repealed the Orders in Council that same month, too late and too slowly known to stop the vote.",
             kick='D · The declaration of 1812', size=24)

# 15 E DIVIDER
divider_photo('capitol-port.jpg', 'Section E', 'Washington Burned, Baltimore Held',
             ['The war on land went badly, the war at sea better, and the largest land transfer of the war fell on a Native nation.'],
             "The image is George Munger's watercolor of the Capitol after its burning in August 1814, drawn that year and now held by the Library of Congress. Open the section with the war's uneven shape. The United States had declared war to conquer Canada and could not do it: expedition after expedition crossed the border and came back, at Detroit, on the Niagara, and toward Montreal. At sea the republic's few frigates won single ship victories that the country celebrated out of all proportion to their weight, and on Lake Erie Perry's squadron won a real strategic prize in 1813. Section E also holds the war in the South, where the Creek War ran inside the larger war and ended with a cession larger than any the fighting with Britain produced. Teach the burnings in sequence: York first, then Washington in answer, then Baltimore, where the sequence stopped.")

# 16 E CONTENT
content_text('Canada held, and the capitals burned',
             ['Invasions of Canada failed year after year.',
              'The frigate Constitution won at sea, and Perry won on Lake Erie in 1813.',
              'American troops burned York in 1813.',
              'A British army burned Washington in August 1814.',
              'Dolley Madison saved the Lansdowne portrait.'],
             "Take the items in the order students will be tested on them. The Canada invasions failed for the reasons the War Hawks had discounted: distance, supply, divided command, and a population that did not rise to join the invaders. The frigate Constitution's victories over Guerriere and Java, and Perry's capture of a British squadron on Lake Erie in September 1813, were the war's clean successes, and the reading calls the lake and sea war the better fought half. In April 1813 American troops took York, the capital of Upper Canada, and burned its public buildings. In August 1814 a British force routed the militia at Bladensburg and burned Washington, the Capitol and the President's House among the buildings fired, in stated answer for York. Dolley Madison, overseeing the President's House evacuation, carried out the Lansdowne portrait of Washington, the full length Stuart portrait students met in Lesson 1.",
             kick='E · Washington burned, Baltimore held', size=24)

# 17 E CONTENT PHOTO
content_photo_s('fortmchenry-port.jpg', 'Baltimore held, and a song came out of it',
             ['Fort McHenry was bombarded through the night.',
              'Rockets and bursting shells lit the night of September 1814.',
              'The flag was still flying at dawn.',
              'Francis Scott Key watched from a British ship.',
              'The verses became the Star-Spangled Banner.'],
             "The print is Bower's aquatint again, the title slide's image, showing the bomb ships at their work. Teach the night as Key experienced it, because Station 5 of the activity reads all four of his stanzas and asks what he could and could not know. Key had gone out under a flag of truce to negotiate the release of a prisoner and was held aboard a British vessel through the attack. Through the night of September 13 and 14, the fleet threw shells and rockets at Fort McHenry; by their glare Key could see the flag at intervals, and in the dark between, nothing. The first stanza is therefore a question, asked twice. At dawn the great garrison flag still flew, the fort had held, the land attack had already failed at North Point, and the fleet withdrew. The verses Key drafted became the Star-Spangled Banner, and the third stanza's promise about the hireling and slave deserves the class's attention in the activity.",
             kick='E · Washington burned, Baltimore held')

# 18 E STAT
stat('23 million', 'acres of Creek land taken by the Treaty of Fort Jackson in 1814',
     'The war\u2019s largest single land transfer, taken from a nation some of whose people had fought beside Jackson',
     "Put the war's largest number where it belongs, in the South. The Creek War began as a civil war inside the Creek nation, between the Red Stick towns that had taken up the movement Tecumseh carried south in 1811 and the towns allied with the United States. Andrew Jackson, commanding Tennessee militia and regulars with Creek and Cherokee allies, destroyed the Red Stick force at Horseshoe Bend in March 1814, in fighting that killed some eight hundred Red Stick warriors, the standard count. The Treaty of Fort Jackson that August took about twenty three million acres, roughly half the Creek country, including land of the Creek towns that had fought beside him. No battlefield against Britain moved a boundary at all; the war's map was redrawn here, at a Native nation's expense, and students should weigh that fact in their verdicts.",
     kick='E · Washington burned, Baltimore held')

# 19 F DIVIDER
divider_text('Section F', 'Hartford, Ghent, and New Orleans',
             'The opposition met, the peace was signed, and the war\u2019s most famous battle was fought after the war had ended on paper.',
             "Close the fighting with the war's strangest month. By December 1814 the war had run two and a half years, the Treasury was empty, the coast was blockaded, and New England's opposition had deepened from grumbling into organization: governors who would not release their militia, merchants trading with the enemy under license, banks that would not lend to Washington. Section F follows the Federalists to Hartford, the peace commissioners to Ghent, and Jackson to New Orleans, in that order, and then asks students to notice the calendar, because the calendar is the lesson. The Hartford report, the treaty, and the battle all landed within weeks of each other, and which of them the public remembered was decided by the order in which the news arrived. Armistead's flag and Jackson's riflemen won the memory; the commissioners' document won almost none.")

# 20 F CONTENT
content_text('Hartford: amendments, not secession',
             ['New England Federalists met in December 1814.',
              'Governors had refused the militia calls.',
              'Moderates carried amendments over secession.',
              'Embargoes were capped at sixty days, and war required two thirds.',
              'The report traveled south into the peace news.'],
             "Teach Hartford from its own text, which students read at Station 4, and resist the shorthand that the convention voted to leave the Union. The radicals wanted more; the moderates who ran the meeting produced a report of proposed constitutional amendments: no embargo longer than sixty days, no declaration of war without two thirds of both houses, no new state admitted without two thirds, no president twice from the same state in succession, and more of the same kind. Read as a program, it was New England's bill of grievances against a war that had closed its ports, drafted into constitutional language. Its delivery was its disaster. The commissioners carrying the report reached Washington just as the news of Ghent and New Orleans did, and a document meant as a wartime protest read, beside a victory and a peace, as treason that had missed its moment.",
             kick='F · Hartford, Ghent, and New Orleans', size=24)

# 21 F CONTENT 2
content_text('Ghent, then New Orleans',
             ['The Treaty of Ghent was signed on December 24, 1814.',
              'The boundaries of 1811 were restored, and the causes went unmentioned.',
              'Napoleon was beaten, and the grievances had died with his wars.',
              'Jackson fought below New Orleans on January 8, 1815.',
              'The war\u2019s most lopsided battle was fought after the peace.'],
             "Work the two dates until students can say them without notes. At Ghent, in modern Belgium, American and British commissioners signed on Christmas Eve 1814 a treaty that restored the boundaries and possessions of 1811 and said nothing about impressment, the Orders in Council, or neutral rights. The silence was not an oversight. With Napoleon beaten and exiled, Britain had no wartime navy to man by impressment and no blockade system to defend; the causes had expired with the European war, and neither side needed them in a treaty. Jackson knew none of it. On January 8, 1815, a British army of veterans advanced on his lines below New Orleans and was destroyed in about half an hour of frontal assault, losing some two thousand men, the standard count, against a small fraction of that number on the American side. The battle changed no term of the peace. It changed the peace's meaning at home.",
             kick='F · Hartford, Ghent, and New Orleans', size=24)

# 22 G DIVIDER
divider_text('Section G', 'What the War Settled',
             'None of its stated causes on paper. Nearly everything around them in fact.',
             "End the narrative where the reading ends, with the two layers held apart, because holding them apart is the lesson's main skill. Layer one is the document: a treaty of status quo, silent on every cause named in 1812. Layer two is the country the war left behind: Canada tried and confirmed out of reach, the western confederacies broken past recovery, one national party dead, another generation of soldiers made famous, and a public persuaded that the republic had fought the world's greatest naval power to a standstill and won independence a second time. Section G also looks forward. Jackson's fame from New Orleans becomes the Jackson presidency of the next unit, and the land opened in the West becomes the settlement story the rest of this course keeps meeting. Students write their verdicts from this section's evidence, so teach it as a weighing, not a summary.")

# 23 G CONTENT
content_text('The settlement beneath the silence',
             ['Canada was confirmed beyond American reach.',
              'The western confederacies were broken for good.',
              'The Federalist Party was ruined by timing.',
              'The generation told it as a second independence.',
              'Jackson stood as the most famous soldier in the country.'],
             "Take the five results one by one and ask, of each, whether a treaty signed it or the war itself did. Canada: three years of invasion settled what no clause mentioned, that the northern border would hold. The West: Tecumseh dead at the Thames in 1813, the confederacy scattered, the Creek country halved, and settlement after the war poured across the Old Northwest on a scale the prewar years never approached. The Federalists: a party that had governed the country in the 1790s ended the war as a regional rump, ruined less by Hartford's text than by its arrival date. The national memory: out of a drawn war the country manufactured a victory story, with the Banner and New Orleans as its proofs. And Jackson: the fame made at Horseshoe Bend and New Orleans carried him toward the presidency the next unit opens with.",
             kick='G · What the war settled', size=24)

# 24 GLANCE
s = slide(NAVY)
kicker(s, 'The war of 1812 at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Causes, costs, and the settlement', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The causes', 'Impressment; Orders in Council', 'Ranked by Madison, June 1, 1812'),
        ('The embargo', 'Ports closed, 1807 to 1809', 'Exports down four fifths; repealed'),
        ('The western war', 'Tecumseh\u2019s claim; Tippecanoe', 'The confederacy turned to Britain'),
        ('The fighting', 'York and Washington burned', 'Baltimore held; 23 million acres taken'),
        ('The settlement', 'Ghent, December 24, 1814', 'Silent on the causes; New Orleans after')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=20, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 0.85
notes(s, "This slide mirrors the summary table at the end of the guided notes, The War of 1812 at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. Read the rows as one account rather than five summaries. The causes were stated in ranked order by the president who asked for the war. The embargo was the alternative, tried at full strength for over a year and abandoned. The western war gave the declaration its second front and its deepest cause, the land. The fighting produced the burnings, the held fort, and a cession no treaty with Britain matched. The settlement row is the lesson's open end: a treaty silent on its own war, beside a country rearranged by the fighting anyway.")

# 25 VOCAB A
vocab('Words for the causes',
      [('impressment', 'sailors taken into the Royal Navy by force'),
       ('embargo', 'a government ban on trade, 1807'),
       ('War Hawks', 'Clay and Calhoun; war for honor and Canada'),
       ('Tecumseh', 'the Shawnee confederacy\u2019s builder')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. impressment: the British practice of stopping American ships at sea and forcing sailors, including American citizens, into service in the Royal Navy, one of the grievances Madison's war message laid before Congress in 1812. embargo: a government ban on trade, the policy of the Embargo Act of 1807, which closed American ports to foreign trade entirely in the hope of forcing Britain and France to respect American neutral rights without a war. War Hawks: the young congressmen, Henry Clay and John C. Calhoun among them, who pressed for war with Britain in 1811 and 1812 to end impressment, defend national honor, and conquer Canada. Tecumseh: the Shawnee leader who built a confederacy of Native nations in the West to resist American land cessions, traveled as far south as the Creek country seeking allies, and joined Britain in the War of 1812, dying at the Thames in 1813.")

# 26 VOCAB B
vocab('Words for the fighting and the peace',
      [('Tippecanoe', 'Prophetstown, November 1811'),
       ('Hartford Convention', 'amendments proposed, the party ruined'),
       ('Treaty of Ghent', 'December 24, 1814; the causes unmentioned')],
      "Three more terms, again matching the guided notes exactly. Tippecanoe: the battle of November 1811 in which William Henry Harrison's army fought Tecumseh's confederacy at Prophetstown while Tecumseh was away, burned the town, and claimed a victory that made Harrison's reputation. Hartford Convention: the meeting of New England Federalists at Hartford in December 1814 and January 1815, which proposed constitutional amendments and hinted at a separate peace, and whose report reached Washington just as news of peace and New Orleans destroyed the party's standing. Treaty of Ghent: the treaty signed at Ghent on December 24, 1814, that ended the War of 1812 by restoring the boundaries and possessions of 1811, settling none of the questions of impressment or neutral rights over which the war had been declared. Read the set as the lesson's arc in three stops: the frontier battle that made the war two wars, the wartime opposition that the peace destroyed, and the treaty whose silence students must be able to explain.")

# 27 SYNTHESIS
content_text('Judging the war whole',
             ['The war was declared for sailors, trade, and honor.',
              'It was fought to a draw on the main front.',
              'It was decided in the West and in the Creek country.',
              'It settled in fact what it never settled on paper.',
              'The writing task asks for one verdict, defended.'],
             "Close the teaching here, before the work slide, and model the judgment the writing task will ask for. Each of the three verdicts has a record. Won: the republic took on the world's strongest naval power a second time, kept its independence, its capital rebuilt, its flag flying, and emerged with heroes and a song the country still sings. Lost: the stated causes were never won, the capital was burned, the trade the war defended was ruined by the war itself, and the treaty restored 1811 as if the fighting had not happened. Survived: Ghent's silence beside the war's rearrangements, Canada confirmed, the confederacies broken, the Federalists gone, reads to many historians as the verdict the documents support. The strongest student writing picks one verdict, builds it from at least three of the activity's records, and answers the best record against it instead of pretending it is not there.",
             kick='Synthesis', size=24)

# 28 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Why did the United States go to war with Britain again, and what did the war actually settle? Build the file first, then judge from it.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The War File: five stations, a file, and a verdict on won, lost, or survived'),
        ('Notebook', 'Notebook page: the war charted in five rows, and the war in one paragraph'),
        ('Quick check', 'Madison\u2019s War Message, 1812: the definition, the pretext, the embargo, and Ghent'),
        ('Writing', 'Won, Lost, or Survived: one verdict defended from both halves of the bank')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: impressment defined and ranked, Tecumseh\u2019s claim and Tippecanoe, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The War File, runs five stations: the Embargo Act from the audited bank record, read for what it forbids and for the bond that policed it; Madison's war message from the audited bank record, read for the ranking and the word pretext; a labeled teaching summary of Tecumseh at Vincennes, labeled because the surviving accounts of his speech differ; the Hartford Convention resolutions from the audited bank record, read for the amendments and their targets; and the Star-Spangled Banner whole, all four stanzas, from the audited bank record. Students build the file in Part 2 and defend a verdict of won, lost, or merely survived. The notebook page charts the same five parts. The quick check works from Madison's message alone. The writing task turns the verdict into an essay from both halves of its bank.")

dc.save(OUT)
