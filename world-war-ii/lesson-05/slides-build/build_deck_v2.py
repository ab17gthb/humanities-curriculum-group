#!/usr/bin/env python3
"""World War II Lesson 5 deck, "The War in the Pacific,"
built to the approved system: image-led slides, fragments only on
screen, comprehensive speaker notes, full lesson + vocabulary coverage.
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
    frags(s, items, y=2.15 if kick else 2.0, w=6.9, size=size)
    notes(s, note)
    return s

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'WORLD WAR II · LESSON 5', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The War in the Pacific', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Across the ocean, one island at a time, at a rising price', size=17, color=POWDER)
notes(s, "The photograph shows United States Navy Task Group 58.1 underway in the Pacific in July 1944, an official Navy photograph held by the National Archives. It opens the Pacific half of this unit. The last lesson followed the war in Europe from North Africa to the surrender of Germany. This lesson follows the other ocean. In the spring of 1942 Japan held an empire won in six months, and the United States faced thousands of miles of open water with Japanese garrisons on the islands in between. Students will trace how the Allies crossed that ocean: a turn at sea in 1942, a strategy of island hopping on two roads, a submarine blockade, a bombing campaign flown from the Marianas, and two final battles whose cost figures frame everything the next lessons take up.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did the Allies cross the Pacific and close on Japan, and what did each step toward the home islands cost?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the Second World War transform the United States, and how far did the country live up to the democracy it claimed to defend?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question has two halves, and students should keep both in view all hour. The first half asks how the Pacific was crossed, which is a question about method: carrier battles, island hopping, submarines, and bombers based ever closer to Japan. The second half asks what each step cost, which is a question about figures: American dead, Japanese dead, and, from 1944 onward, civilian dead in growing numbers. The lesson is built as a ledger. Every step bought something the advance needed, and every step was paid for, and the price per step rose as the advance closed on the home islands. The unit question runs beneath as the frame. Keep it in reserve today. This lesson stays with the fighting and its cost, and the reckoning with the war's meaning belongs to the lessons that follow.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'An advance, measured step by step', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'An empire won in six months', 'Manchuria to the Solomons by spring 1942'),
        ('B', 'The turn at sea', 'Coral Sea, then four carriers lost at Midway'),
        ('C', 'Guadalcanal', 'The first offensive, six months for one airfield'),
        ('D', 'Island hopping on two roads', 'MacArthur and Nimitz, airfields one step at a time'),
        ('E', 'The strangling of an island empire', 'Submarines cut the sea trade Japan lived on'),
        ('F', 'Fire from the Marianas', 'The B-29, and Tokyo in March 1945'),
        ('G', 'Iwo Jima and Okinawa', 'The preview of invading Japan itself')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Sections A through C cover 1942: the empire Japan won, the carrier battles that stopped its advance, and the first Allied offensive at Guadalcanal. Sections D and E give the method of the advance, island hopping run by two commands, and the strategy underneath it, the submarine blockade that strangled an empire dependent on sea trade. Sections F and G cover the closing years: the Marianas and the firebombing they made possible, then Iwo Jima and Okinawa. Tell students the summary table at the end of their guided notes, The Pacific War at a Glance, asks them to rebuild this map from the record, with what each step bought set beside what it cost.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', 'An Empire Won in Six Months',
             'From Manchuria to the Solomons, and an ocean in the way.',
             "Open with the speed of it, because American planning in 1942 began from shock. In the six months after Pearl Harbor, Japanese forces took the Philippines, Malaya, Singapore, and the Dutch East Indies, and pushed south through the Solomon Islands toward Australia. By the spring of 1942 the empire ran from Manchuria in the north to the Solomons in the south, a chain of conquests held together by sea power. Students should also hold the limit inside the achievement. Japan had won territory faster than it could supply or defend all of it, and every garrison it planted on an island depended on ships to feed it. That dependence is the thread this whole lesson pulls. The empire looked solid on a map in 1942. Its supply lines were its weak point from the first day, and the American strategy was built to find them.")

# ------------------------------------------------------ 5 EMPIRE AND DISTANCE
content_text('An empire, and thousands of miles of ocean',
             ['Japan took the Philippines, Malaya, Singapore, and the Dutch East Indies.',
              'Japanese forces pushed south through the Solomons toward Australia.',
              'The empire ran from Manchuria to the Solomons by the spring of 1942.',
              'Germany first sent the main American effort to Europe.',
              'Every advance needed a harbor, an airfield, and a supply line.'],
             "State the American problem plainly, because the reading states it in one word: distance. Thousands of miles of ocean lay between Hawaii and Japan, and Japanese garrisons held the islands in between. A land army could not march across that. Every step of any advance would have to be carried by ship, landed on a defended shore, and supplied across open water for as long as it lasted. The Germany first strategy, agreed with Britain and kept through the war, sent the main American effort to Europe first, so Pacific commanders fought most of 1942 with what they had on hand. That shortage shaped the year. The Pacific war in 1942 was a holding war fought by carriers and one division of Marines, and it very nearly was not enough. Students should write the distance problem into section A of the notes, because every later section is an answer to it.",
             kick='A · An empire won in six months')

# ------------------------------------------------- 6 SECTION B DIVIDER
divider_photo('yorktown-port.jpg', 'Section B', 'The Turn at Sea: Coral Sea and Midway',
              ['USS Yorktown burning after the first', 'Japanese attack at Midway, June 4, 1942.'],
              "The photograph is an official United States Navy photograph, number 80-G-32300, held by the National Archives. It shows the carrier Yorktown burning after the first Japanese attack at Midway on June 4, 1942. Yorktown survived this attack, was hit again, and sank after the battle, the one American carrier lost. Section B covers the two carrier battles of May and June 1942 that stopped the Japanese advance at sea. Teach them as a pair. The Coral Sea was a check, fought entirely by aircraft whose ships never sighted each other. Midway was a decision, made possible by code breaking and paid for in the currency Japan could least afford, fleet carriers and the trained pilots who flew from them. Both battles belong to blueprint entry 9, and both are tested, so students should have the dates and the figures in their notes before the section ends.",
              title_size=38)

# ------------------------------------------------------ 7 CORAL SEA AND MIDWAY
content_text('A check in May, a decision in June',
             ['At the Coral Sea in May 1942, the Port Moresby force turned back.',
              'The Coral Sea was the first battle fought entirely by aircraft.',
              'Code breakers named the next target as Midway Island.',
              'Nimitz set an ambush with three carriers.',
              'On June 4, dive bombers caught the Japanese force in the open.'],
             "Work the two battles as cause and effect. In the Coral Sea in May 1942, American and Japanese carrier fleets fought the first naval battle in history conducted entirely by aircraft, in which the opposing ships never sighted each other. The United States lost the carrier Lexington, which students should hear as a real loss, but the Japanese invasion force bound for Port Moresby in New Guinea turned back, the first time a Japanese advance had been stopped. A month later came the decision. Code breakers had read enough of the Japanese naval code to identify Midway Island as the target, and Admiral Nimitz, instead of spreading his weaker force, concentrated his three carriers northeast of the island and waited. On the morning of June 4, American dive bombers found the Japanese carrier force with its decks crowded and its fighter cover drawn low, and in a single day the battle was decided.",
             kick='B · The turn at sea')

# ------------------------------------------------------ 8 FOUR CARRIERS STAT
stat('4', 'Japanese fleet carriers sunk in one day at Midway',
     'June 4, 1942 · With them went trained carrier pilots Japan could not replace at American speed',
     "Put the figure together with its meaning, because the number alone understates the loss. Japan began the Pacific war with the finest carrier aircrews in the world, trained over years. Four fleet carriers went down at Midway, Akagi, Kaga, Soryu, and Hiryu, and with the ships went hundreds of those pilots. A carrier can be built in a shipyard in a year or two, and American yards were already launching ships at a pace Japan could not match. A veteran carrier pilot cannot be built at all. He is accumulated, flight hour by flight hour, over years Japan no longer had. That is why the guided notes definition says what it says: the Battle of Midway ended Japan's ability to take the offensive in the Pacific. Japan still had carriers after June 1942. What it no longer had was the combination of ships, pilots, and time that an offensive requires, and it never got that combination back.",
     kick='B · The turn at sea')

# ------------------------------------------------- 9 SECTION C DIVIDER
divider_photo('guadalcanal-port.jpg', 'Section C', 'Guadalcanal: The First Offensive',
              ['Marines on patrol on Guadalcanal,', 'August 1942. Marine Corps photograph.'],
              "The photograph is an official Marine Corps photograph, number 50831 in the Marine Corps record as credited on its file page, showing Marines on patrol on Guadalcanal in August 1942, the month the campaign began. Section C covers the first major Allied offensive of the Pacific war. Two months after Midway, the United States stopped reacting and chose a place to attack: a small island in the Solomons where Japan was building an airfield that could threaten the sea route to Australia. What followed was not a landing and a victory parade. It was six months of fighting on land, at sea, and in the air, in jungle, in heat, and under nightly naval bombardment, for one island and one airstrip. Teach the campaign as a supply contest, because that is what decided it, and because the lesson it taught became the strategy of the whole Pacific war.",
              title_size=38)

# ------------------------------------------------------ 10 GUADALCANAL
content_photo_s('guadalcanal-port.jpg', 'Six months for one island and its airfield',
              ['Marines landed in August 1942 and took the airfield.',
               'Henderson Field was held against repeated attacks.',
               'The fleets fought offshore at night, again and again.',
               'Japan could not feed or reinforce its troops.',
               'In February 1943, Japan evacuated the survivors.'],
              "In the guided notes definition, Guadalcanal is the Solomon Islands campaign of August 1942 to February 1943, the first major Allied offensive of the Pacific war, fought on land, at sea, and in the air around one island and its airfield. Unpack each part of that definition with students. On land, Marines and then Army troops held Henderson Field against repeated Japanese attacks delivered through the jungle. At sea, the two fleets fought a series of night battles in the waters offshore so savage that the channel earned a grim nickname among sailors. In the air, the field's aircraft, the Cactus Air Force, flew by day while Japanese bombers came over from Rabaul. What decided the campaign was none of these alone. Japan could not feed or reinforce its troops on the island, and hunger and disease did what American firepower alone had not. In February 1943 Japan evacuated its survivors by night and conceded the island.",
              kick='C · Guadalcanal')

# ------------------------------------------------- 11 SECTION D DIVIDER
divider_text('Section D', 'Island Hopping on Two Roads',
             'Take what buys an airfield. Leave the rest to wither.',
             "Guadalcanal taught a lesson that became a strategy, and this section names it. The Pacific held far more Japanese garrisons than the Allies could ever attack one by one, and Guadalcanal had shown what attacking one cost in time, ships, and men. It had also shown something else: a garrison on an island is only as strong as the ships that feed it. Cut the supply and the garrison is a prisoner of its own island, dangerous to anyone who lands on it and harmless to everyone who sails past. Section D covers the strategy built on that insight, island hopping, and the two commands that ran it on two roads across the Pacific, MacArthur in the southwest and Nimitz in the central Pacific. Students should be able to define the strategy in the guided notes wording and to explain, in their own words, why a bypassed garrison counted as defeated.")

# ------------------------------------------------------ 12 ISLAND HOPPING
content_text('Seize the airfield, bypass the fortress',
             ['Selected islands were taken for airfields.',
              'Strong garrisons were bypassed and cut off from supply.',
              'A bypassed garrison could not be fed or moved.',
              'It waited out the war behind the advance.',
              'Strength was spent only where it bought range.'],
             "In the guided notes definition, island hopping is the Allied Pacific strategy of seizing selected islands for airfields while bypassing strong Japanese garrisons and cutting them off from supply. Every clause of that definition carries weight, so take them in order. Selected islands: the Allies chose islands for what they bought, an airfield within range of the next step, not for their size or fame. Bypassing: strong positions such as the great Japanese base at Rabaul were left alone, neutralized from the air and cut off, rather than stormed. Cutting off from supply: American sea and air power made sure nothing reached them, and a garrison that cannot be fed cannot fight, move, or matter to the outcome. The strategy traded the attacker's old problem, every fortress must be taken, for the defender's new one, every garrison must be fed. Japan had planted its strength across a hundred islands. Island hopping made that strength sit still and starve while the advance walked past it.",
             kick='D · Island hopping on two roads', size=24)

# ------------------------------------------------------ 13 TWO ROADS
content_photo_s('taskforce-port.jpg', 'Two commands, two roads, one direction',
              ['MacArthur advanced along New Guinea toward the Philippines.',
               'Nimitz advanced across the central Pacific.',
               'The Gilberts, the Marshalls, and then the Marianas fell in turn.',
               'Each landing put aircraft one step closer to Japan.',
               'Each step was measured in airfield range.'],
              "The photograph shows a Navy task group underway in July 1944, the summer the central Pacific drive reached the Marianas. Name the two roads clearly, because students mix them up. In the southwest, General MacArthur advanced along the coast of New Guinea toward the Philippines, the return he had promised when he was driven out in 1942. In the central Pacific, Admiral Nimitz drove straight across the ocean, through the Gilbert Islands and the Marshall Islands toward the Marianas. The two drives supported each other in a way a map makes plain: Japan never knew which road the next blow would come on, and it could not defend both at full strength. Each landing on either road put American aircraft one step closer to Japan. Insist on the reading's measure for those steps. They were not counted in miles conquered. They were counted in airfield range, in what the aircraft based there could now reach. That measure explains why some famous islands were taken at great cost and others, larger and stronger, were simply left behind.",
              kick='D · Island hopping on two roads')

# ------------------------------------------------- 14 SECTION E DIVIDER
divider_photo('submarine-port.jpg', 'Section E', 'The Strangling of an Island Empire',
              ['An American submarine on war patrol.', 'National Archives photograph.'],
              "The photograph shows an American submarine on war patrol in the Pacific, a National Archives record, number 520690. It suits the quietest and in tonnage the deadliest campaign of the Pacific war. Section E steps back from the landings to the strategy running underneath them. Japan was an island empire. It held oil fields, mines, and plantations across Southeast Asia and the East Indies, but none of that wealth sat in Japan itself. All of it had to travel by ship to reach a Japanese refinery, factory, or kitchen. Whoever cut the sea lanes cut the empire off from its own conquests. That is what the submarine campaign, with surface warships and aircraft, set out to do, and by 1944 it was succeeding on a scale Japanese planners had not believed possible. Students tend to remember the landings and forget this campaign. The figures argue otherwise, and the next slide gives them.",
              title_size=36)

# ------------------------------------------------------ 15 BLOCKADE
content_text('Cut the sea lanes, starve the empire',
             ['A blockade was maintained by warships, submarines, and aircraft.',
              'Submarines did most of the work.',
              'Merchant ships were sunk faster than yards could replace them.',
              'Tankers went down before their oil reached a refinery.',
              'By 1945, aircraft were mining Japan\u2019s home harbors.'],
             "In the guided notes definition, a naval blockade is the use of warships, submarines, and aircraft to cut off an enemy's sea trade and supplies. Apply the definition to Japan's particular weakness. Japan imported its oil, much of its steel, and part of its food by ship from the territories it had conquered, so the empire's wealth existed at the far end of sea lanes the United States Navy could patrol. American submarines, after early war torpedo failures were fixed, sank Japanese merchant ships faster than Japanese yards could launch replacements. Tankers from the East Indies went down before their oil reached a refinery, which meant the conquest that was supposed to make Japan self sufficient never delivered its promise. In 1945 American aircraft added mines to Japan's home harbors, closing even coastal shipping. An empire won by sea power was being strangled by sea power, and its factories slowed for want of supplies while its armies waited on islands the advance had already passed.",
             kick='E · The strangling of an island empire', size=24)

# ------------------------------------------------- 16 SECTION F DIVIDER
divider_photo('b29-port.jpg', 'Section F', 'Fire from the Marianas',
              ['A B-29 Superfortress of the 509th', 'Composite Group, 1945.'],
              "The photograph shows a B-29 Superfortress in 1945, a War Department photograph held by the National Archives. The B-29 was the largest bomber of the war, built to fly farther with a heavier load than anything before it, and for most of the war there was nowhere within its reach of Japan to base it. Section F covers the capture that changed that geometry. In June 1944 Nimitz's central Pacific road reached the Mariana Islands, Saipan, Guam, and Tinian, close enough to the home islands for the B-29 to fly there and return. What followed was first a conventional bombing campaign that disappointed its planners, and then, in March 1945, a change of method, low altitude night attacks with incendiaries against cities built largely of wood. This section carries the heaviest single figure in the lesson, and it should be taught at the pace that figure deserves, with its label kept attached: an estimate.",
              title_size=38)

# ------------------------------------------------------ 17 MARIANAS AND FIRE
content_text('Range first, then fire',
             ['Saipan, Guam, and Tinian were taken in June 1944.',
              'The prize was range, because B-29s could reach Japan and return.',
              'In March 1945, the campaign changed form.',
              'Firebombing was flown low at night.',
              'More than sixty Japanese cities burned, in whole or in part.'],
             "In the guided notes definition, firebombing is the bombing of cities with incendiary weapons designed to start mass fires. Set the sequence before the definition. The Marianas were taken in June and July 1944 after hard fighting, Saipan against a garrison that fought nearly to the last man, a fact students should file away for section G. The prize was range. From fields built on those islands, the B-29 could reach Japan's home islands and return, which no base taken earlier could offer. The first raids, flown high by day with explosive bombs, scattered their loads in high winds and did limited damage. In March 1945 the command changed the method: bombers came in low at night, stripped of guns to carry more incendiaries, against cities built largely of wood and paper. The fires did the work the bombs had not. Raid followed raid through the spring and summer, and more than sixty Japanese cities burned in whole or in part before the war ended.",
             kick='F · Fire from the Marianas', size=24)

# ------------------------------------------------------ 18 TOKYO STAT
stat('90,000+', 'people killed in one night in Tokyo, March 9 to 10, 1945, by estimate',
     'The record gives a range, on the order of 90,000 to 100,000 dead, and the lesson prints it as an estimate',
     "Stop on the labeling before the number, because how this figure is stated is part of the lesson. Nobody counted the dead of the Tokyo fire raid one by one. The figure in the record is an estimate, a range, on the order of 90,000 to 100,000 people killed in a single night, and students should repeat it with those words attached, as the reading does. What is not in doubt is the scale. On the night of March 9 to 10, 1945, hundreds of B-29s dropped incendiaries on Tokyo in a low altitude attack, and the fires joined into a single storm of flame that burned out a large share of the city. It was the deadliest air raid of the Second World War, deadlier in that one night than either atomic bomb would be in its first count. The atomic decision belongs to lesson 8. Today students need the fact and its label: by March 1945 the bombing of Japan had become a weapon against cities and the people in them, at a cost counted in six figures a night.",
     kick='F · Fire from the Marianas')

# ------------------------------------------------- 19 SECTION G DIVIDER
divider_photo('iwo-port.jpg', 'Section G', 'Iwo Jima and Okinawa: The Preview',
              ['The first flag raising on Mount Suribachi,', 'photographed by Sergeant Louis Lowery, USMC.'],
              "The photograph shows the first flag raising on Mount Suribachi, Iwo Jima, on February 23, 1945, taken by Staff Sergeant Louis Lowery of the Marine Corps. Name the photographer and the service deliberately. The famous photograph of the second flag raising, later that day, was made by Joe Rosenthal, a civilian Associated Press photographer. It is the better known image and it is not a federal work, so this lesson uses the Marine Corps photograph of the first raising instead, and students should know why the lesson draws the distinction in a course that works from the public record. Section G covers the last two steps of the advance, Iwo Jima in February and March 1945 and Okinawa from April to June. Together they changed the character of the lesson's ledger. The steps stopped buying distance and started previewing the invasion of Japan itself, and planners in Washington read them exactly that way.",
              title_size=36)

# ------------------------------------------------------ 20 IWO JIMA
content_photo_s('iwo-port.jpg', 'Eight square miles, bought position by position',
              ['The battle ran from February to March 1945, halfway to Japan.',
               'The island was wanted for a fighter base and an emergency field for B-29s.',
               'The garrison fought from tunnels and caves.',
               'About 6,800 Americans died taking the island.',
               'Nearly the whole Japanese garrison died where it stood.'],
              "Give students the island's purpose first, because Iwo Jima was taken for the bombers, not for itself. Halfway between the Marianas and Japan, its airfields let American fighters escort the B-29s all the way to the target and gave damaged bombers an emergency field to land on instead of ditching in the ocean, and by the war's end thousands of airmen owed their lives to that strip of volcanic ash. Then give the cost, and do not rush it. The Japanese garrison, about 21,000 men, had dug itself into tunnels and caves and had to be destroyed position by position with flame, explosives, and infantry assault. Taking eight square miles cost about 6,800 American dead, and nearly the whole garrison died where it stood rather than surrender. Students should mark that last fact as carefully as the first. A garrison that does not surrender, on an island of no value to anyone but the attacker, is evidence about the next island, and about the home islands behind it.",
              kick='G · Iwo Jima and Okinawa')

# ------------------------------------------------------ 21 IWO STAT
stat('6,800', 'American dead for eight square miles at Iwo Jima',
     'About 850 dead per square mile · The garrison of about 21,000 was nearly destroyed',
     "Do the arithmetic on the board, because students should see where the per mile figure comes from and check it themselves: about 6,800 American dead divided by about eight square miles of island is about 850 dead for each square mile taken. Then set the Japanese figure beside it. Of a garrison of about 21,000 men, about 18,000 died and most of the rest were wounded or captured only when they could no longer fight. There was no surrender of the position as a position. Compare this row of the ledger with the first row, Midway, where a decisive victory at sea cost about 300 American dead. The difference is the lesson in one contrast. A war fought by ships and aircraft at a distance and a war fought by infantry against dug in defenders on land are different wars in cost, and by 1945 the Pacific war had become the second kind, with the largest defended land of all still ahead.",
     kick='G · Iwo Jima and Okinawa')

# ------------------------------------------------------ 22 OKINAWA
content_photo_s('okinawa-port.jpg', 'The largest battle of the Pacific war',
              ['The battle ran from April to June 1945, on a home island sixty miles long.',
               'The island was taken as the base for invading Japan.',
               'Kamikaze attacks came in waves against the fleet.',
               'Japanese military deaths ran above 100,000.',
               'Okinawan civilians died in large numbers.'],
              "The photograph shows the carrier Bunker Hill burning after kamikaze hits off Okinawa on May 11, 1945, a Navy photograph held by the National Archives. In the guided notes definition, a kamikaze is a Japanese pilot who made a deliberate crash attack on an enemy ship; the word also names the attack itself. Okinawa was the first battle fought on a Japanese home island, sixty miles long and about 350 miles from the main islands, taken to serve as the base for the invasion of Japan. Japan defended it with a large army dug into the southern hills and with kamikaze attacks flown in organized waves against the fleet that had to stay offshore and supply the landing. About 12,500 Americans died, on land and at sea together. Japanese military deaths ran above 100,000. And Okinawa was inhabited, which the earlier stepping stones mostly were not: its civilians died in large numbers in the fighting, caught between the armies on their own island.",
              kick='G · Iwo Jima and Okinawa')

# ------------------------------------------------------ 23 OKINAWA STAT
stat('12,500', 'American dead at Okinawa, the preview of invading Japan',
     'Above 100,000 Japanese military dead · Heavy civilian deaths on one island sixty miles long',
     "Close the ledger with the reading planners did in the summer of 1945, because it is the bridge to the rest of this unit. Okinawa cost about 12,500 American dead. Set that figure in the ledger's sequence: about 300 at Midway, about 3,400 on Saipan, about 6,800 at Iwo Jima, about 12,500 at Okinawa, each step closer to Japan costing more than the step before it, against defenders who died nearly whole rather than surrender, and, from Saipan onward, among a civilian population. Japan's home islands held a far larger army and a far larger population than Okinawa's, on far larger ground. Planners preparing the invasion, set for the autumn of 1945, read Okinawa as a preview and multiplied accordingly, and their estimates of the invasion's cost ran to figures that shaped every decision of that summer. Add the final fact of the reading and leave it standing: blockade and bombing were starving Japan, and its government still had not surrendered, and the Allied demand remained unconditional surrender.",
     kick='G · Iwo Jima and Okinawa')

# ------------------------------------------------------ 24 GLANCE
s = slide(NAVY)
kicker(s, 'The Pacific War at a Glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'What each step bought, and cost', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The turn at sea', 'Coral Sea check; four carriers at Midway', 'The initiative, and the first offensive'),
        ('The advance', 'Island hopping on two roads', 'Airfields, one step of range at a time'),
        ('The closing', 'Blockade, then B-29s over Japan', 'An empire starved; cities burned'),
        ('The last steps', 'Iwo Jima and Okinawa', 'The preview of invading Japan itself')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, The Pacific War at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The four rows are the lesson's argument in miniature. The turn at sea bought the initiative, at the Coral Sea and above all at Midway. The advance bought airfields, one step of aircraft range at a time, on two roads. The closing bought pressure no island battle could: a blockade that starved the empire and a bombing campaign flown from the Marianas against Japan itself. The last steps bought the invasion's base and its preview at the highest prices in the ledger. Grade the table generously on wording and strictly on pairing: each row must say what happened and what it bought, and the last row must carry a cost figure, because cost is the point of the row.")

# ------------------------------------------------------ 25 VOCAB A
vocab('Words for the turn and the advance',
      [('Guadalcanal', 'the Solomon Islands campaign of August 1942 to February 1943, the first major Allied offensive of the Pacific war, fought on land, at sea, and in the air around one island and its airfield'),
       ('Battle of Midway', 'the naval battle of June 1942 in which American carrier aircraft sank four Japanese carriers and ended Japan\u2019s ability to take the offensive in the Pacific'),
       ('island hopping', 'the Allied Pacific strategy of seizing selected islands for airfields while bypassing strong Japanese garrisons and cutting them off from supply'),
       ('naval blockade', 'the use of warships, submarines, and aircraft to cut off an enemy\u2019s sea trade and supplies')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. Guadalcanal: the Solomon Islands campaign of August 1942 to February 1943, the first major Allied offensive of the Pacific war, fought on land, at sea, and in the air around one island and its airfield. Battle of Midway: the naval battle of June 1942 in which American carrier aircraft sank four Japanese carriers and ended Japan's ability to take the offensive in the Pacific. The third term is island hopping: the Allied Pacific strategy of seizing selected islands for airfields while bypassing strong Japanese garrisons and cutting them off from supply. The fourth term is naval blockade: the use of warships, submarines, and aircraft to cut off an enemy's sea trade and supplies. Note the order: the two battles of 1942 first, then the two strategies those battles made possible.")

# ------------------------------------------------------ 26 VOCAB B
vocab('Words for the closing',
      [('firebombing', 'the bombing of cities with incendiary weapons designed to start mass fires'),
       ('kamikaze', 'a Japanese pilot who made a deliberate crash attack on an enemy ship; also the attack itself'),
       ('unconditional surrender', 'the demand that an enemy give up without negotiated conditions, announced as Allied policy for Germany and Japan')],
      "Three more terms, again matching the guided notes exactly. The first is firebombing: the bombing of cities with incendiary weapons designed to start mass fires. The definition names the weapon type because the method, not only the target, is what changed in March 1945. The second is kamikaze: a Japanese pilot who made a deliberate crash attack on an enemy ship; also the attack itself. Note that the definition covers both the man and the act, and that the attacks were organized policy by 1945, flown in waves, not isolated acts of desperation. The last term is unconditional surrender: the demand that an enemy give up without negotiated conditions, announced as Allied policy for Germany and Japan. End the vocabulary here on purpose, on the demand itself. Germany had already met it in May 1945. Japan had not, and the gap between the demand and the refusal is where the next lessons begin, with a government in Tokyo that would not surrender and a ledger in Washington that priced the alternative.")

# ------------------------------------------------------ 27 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did the Allies cross the Pacific and close on Japan, and what did each step toward the home islands cost? Build the ledger first, then read its pattern.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Stepping Stone Ledger: five battle records, and a verdict on the invasion\u2019s expected cost'),
        ('Notebook', 'Notebook page: the five steps in a chart, bought, cost, and taught'),
        ('Quick check', 'The Fleet Under Attack: the kamikaze, Midway, island hopping, and the preview'),
        ('Writing', 'Another Way to End the War: whether the cost pattern of 1945 made the search unavoidable')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: why a bypassed garrison was defeated, what the Marianas and Iwo Jima each bought, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Stepping Stone Ledger, runs five battle records, Midway, Guadalcanal, the Marianas, Iwo Jima, and Okinawa, and at each one students enter what the step bought, what it cost in American and Japanese dead, and what it taught, then close the ledger with a verdict on what the invasion of Japan was expected to cost and who was doing the expecting. The quick check, The Fleet Under Attack, tests the kamikaze against the Bunker Hill photograph, then Midway, island hopping, and the preview argument. The writing task, Another Way to End the War, asks whether the cost pattern of 1945 made the search for another way to end the war unavoidable, argued from the ledger. The exit ticket has three parts: why a bypassed garrison was defeated, one purchase each for the Marianas and Iwo Jima, and the lesson question answered with at least two cost figures. The next lesson turns from the fighting to the home front's own reckoning with the democracy the war claimed to defend.")

dc.save(OUT)
