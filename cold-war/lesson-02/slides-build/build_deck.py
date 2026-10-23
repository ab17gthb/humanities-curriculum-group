#!/usr/bin/env python3
"""Cold War Lesson 2 deck, "The Cold War in Asia: China and Korea,"
built to the approved system: image-led slides, fragments only on
screen, comprehensive speaker notes, full lesson + vocabulary
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
OUT = os.path.join(HERE, '..', 'lesson-02-slides.pptx')

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
text(s, 0.9, 5.32, 11.5, 0.4, 'THE COLD WAR · LESSON 2', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Cold War in Asia: China and Korea', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'How a paper war became a shooting war, and why it ended without victory', size=17, color=POWDER)
notes(s, "The photograph shows a column of the United States 1st Marine Division moving through Chinese lines during its breakout from the Chosin Reservoir in December 1950, in an official United States photograph. Open by placing this lesson against the last one. Lesson 1 ended with containment written as policy for Europe: a doctrine, a recovery program, an airlift, and an alliance, all of it conducted without a shot fired between the superpowers. This lesson is where the Cold War first turned hot. Between the autumn of 1949 and the summer of 1950 the struggle moved to Asia, drew in a new Communist great power, and produced a war that killed millions and ended on the line where it had started. The lesson question is two-sided, and students should hear both halves from the start: how the shooting began, and why it could not be won outright.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did the Cold War turn into a shooting war in Asia, and why did Korea end without victory?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the struggle between the United States and the Soviet Union reshape the world and American life, and why did it end the way it did?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question joins a cause to a consequence, and students will need both halves for the exit ticket and the writing task. The first half asks how a rivalry that had stayed cold in Europe became a shooting war in Asia within a year of the shocks of 1949. The answer runs through a secret planning paper, NSC-68, and an invasion across a line drawn in 1945. The second half asks why a war the United States entered to repel invasion ended three years later without victory, on roughly its starting line. The answer runs through a changed war aim, a Chinese intervention, and a president who dismissed his most famous general rather than let the war grow. Warn students now against answers that treat the ending as a simple defeat. South Korea survived, which was the original aim. Unification, the aim added in the autumn of 1950, was given up. The lesson lives in the distance between those two aims.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'From paper war to stalemate', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The Shocks of 1949', 'A bomb in August, a revolution in October'),
        ('B', 'NSC-68: The Answer on Paper', 'A global struggle, priced in advance'),
        ('C', 'Invasion and Intervention', 'June 25, 1950, and an answer under the UN flag'),
        ('D', 'Inchon and the Drive North', 'A landing that reversed the war'),
        ('E', 'China Enters and the War Settles', 'November 25, and two years of stalemate'),
        ('F', 'MacArthur and Truman', 'Who commands a limited war'),
        ('G', 'Armistice Without Victory', 'July 27, 1953, on the starting line')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Sections A and B cover the shocks of 1949 and the answer Washington wrote on paper in the spring of 1950. Section C covers the invasion of June 25, 1950 and the American entry under the United Nations flag. Section D covers Inchon and the drive north that changed the aim of the war. Section E covers the Chinese intervention and the settling of the front. Section F covers the fight between the president and his general over the limits of the war, and section G closes on the armistice of 1953 and the template Korea set for later American wars. The summary table at the end of the guided notes is titled Korea at a Glance.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', 'The Shocks of 1949',
             'Two blows in one season, and a question Washington could not shake.',
             "Set the scene with the calendar, because the closeness of these two events did the political work. In the last months of 1949, within about five weeks of each other, the United States lost the two advantages it had counted on since 1945: its monopoly of the atomic bomb and its expectation that China, however chaotic its civil war, would not become a Soviet aligned Communist state. Neither event was an American defeat in battle. No American soldier had lost a position. Yet both were read in Washington as losses on a single scoreboard, and that reading is the first idea students need. Once the bomb and China were entered as two squares lost in one game, every later event in Asia, including a local invasion of Korea, would be scored the same way. Section B shows the document that wrote that scoreboard into policy before the invasion came.")

# ------------------------------------------------------ 5 SHOCKS
content_text('Two blows in a single season',
             ['August 29, 1949: the Soviet atomic bomb test',
              "October 1, 1949: the People's Republic of China proclaimed",
              'The Nationalists flee to Taiwan',
              "A quarter of the world's people under a Communist government",
              'Congress asks who lost China'],
             "Walk the two dates in order and keep them distinct, because students merge them. On August 29, 1949, the Soviet Union tested its first atomic bomb, years earlier than American planners had expected, ending a monopoly the United States had held since 1945. On October 1, Mao Zedong proclaimed the People's Republic of China in Beijing after his forces won the Chinese civil war, and Chiang Kai-shek and his defeated Nationalist government fled to the island of Taiwan. The Soviet Union recognized the new state at once; the United States did not, and would not for three decades. Then teach the political consequence plainly. A Communist government now ruled a quarter of the world's people, and Congress and the press asked who had lost China, as if China had been America's to lose. The Truman administration faced charges of softness toward communism that it carried into the spring of 1950, when it wrote its answer.",
             kick='A · The Shocks of 1949', size=24)

# ------------------------------------------------- 6 SECTION B DIVIDER
divider_text('Section B', 'NSC-68: The Answer on Paper',
             'A secret paper that described a global struggle and priced the answer.',
             "This section covers a document, and students should understand what kind of document it was before they hear its claims. NSC-68 was a planning paper, not a speech, a law, or an order. It was written inside the government, classified secret, and addressed to the president. It carried no authority of its own. Its power lay in the completeness of its argument: it described the enemy, named the stake, and priced the response in one chain of reasoning, so that a president who accepted its description of the threat had its buildup as the only consistent answer. It was finished in April 1950 and set aside. Hold that shelving in view through the next two slides. The paper's history is the clearest case in this unit of an event making a document into policy, because the invasion of June 1950 did in weeks what no argument had done in the spring.")

# ------------------------------------------------------ 7 NSC-68
content_text('The paper that priced the struggle',
             ['Finished in April 1950, in secret',
              'Moscow seeking absolute authority over the rest of the world',
              'The United States named the principal enemy',
              'Defense spending to rise to roughly three times its level',
              'Shelved as too costly, until war arrived'],
             "Teach NSC-68 from its own sentences, which the activity puts in front of students verbatim. The paper described the Soviet Union as animated by a fanatic faith and seeking to impose its absolute authority over the rest of the world. It named the United States, as the principal center of power in the non-Soviet world, the principal enemy whose strength had to be subverted or destroyed if the Kremlin was to succeed. From that description, the prescription followed: a rapid build-up of political, economic, and military strength, expressed in the reading as defense spending rising to roughly three times its current level, with larger forces and aid to allies on every continent. Its closing verbs are the pair students will meet in the activity, to check and to roll back the Kremlin's drive for world domination. President Truman set the paper aside as too costly, since no Congress would vote the taxes in peacetime. The paper waited for an event.",
             kick='B · NSC-68: The Answer on Paper', size=24)

# ------------------------------------------------------ 8 STAT TRIPLE
stat('3x', 'the defense buildup NSC-68 demanded',
     'Spending to rise to roughly three times its 1950 level · Larger ground, sea, and air forces · Aid to allies on every continent',
     "Give this number its context, because without context it sounds modest. American defense spending in 1950 stood at roughly thirteen billion dollars, held down by a president determined to balance the budget after the Second World War. NSC-68 argued that the country could afford far more and that its safety required it: spending rising toward three times that level, a standing army and air force far larger than the peacetime establishment, and military aid to allies across Europe and Asia. In the spring of 1950 those figures had no constituency. Congress would not vote the taxes, and the president who had commissioned the paper shelved it. Then, in June, North Korea invaded the South, and the paper's logic acquired a battlefield. Within a year, defense spending had roughly tripled, as the paper had urged. Students should state the sequence carefully for the test: the buildup was proposed before the war, rejected on cost, and adopted because of the war.",
     kick='B · NSC-68: The Answer on Paper')

# ------------------------------------------------- 9 SECTION C DIVIDER
divider_text('Section C', 'Invasion and Intervention',
             'North Korea crosses the parallel, and the United States answers under the United Nations flag.',
             "Korea enters this unit as a leftover of the last one. In 1945, American and Soviet officers divided the peninsula at the 38th parallel so that both armies could accept the Japanese surrender, and the temporary line hardened into a border between a Communist north backed by Moscow and a south backed by Washington. Each Korean government claimed the whole peninsula, and border fighting ran through 1949. What changed in June 1950 was scale and sponsorship. Kim Il Sung invaded with Soviet built tanks and aircraft, after securing Stalin's approval, expecting a quick victory before the United States could react. The American reaction is the subject of this section, and its legal shape deserves emphasis. The United States went to war on a Security Council resolution and presidential orders. Congress debated, appropriated, and never declared war. That shape became the template the reading names at its close.")

# ------------------------------------------------------ 10 INVASION
content_text('June 25, 1950',
             ['North Korea invades across the 38th parallel',
              'Seoul falls in three days',
              'The Security Council acts during a Soviet boycott',
              'Truman orders American forces in, under the UN flag',
              'No declaration of war from Congress'],
             "On June 25, 1950, North Korean troops crossed the 38th parallel in force, and Seoul, the southern capital, fell in three days. South Korean forces, lacking tanks and heavy guns, could not hold. President Truman answered within days, and the form of the answer is a test point. The United Nations Security Council, meeting while the Soviet delegate was boycotting its sessions over the seating of Communist China, condemned the invasion and called on member states to repel it. Had the Soviet delegate been present, a veto would have blocked the resolution. Truman ordered American air and sea forces, and then ground troops, into the fight under the United Nations flag, with General Douglas MacArthur in command. He did not ask Congress for a declaration of war, and Congress never voted one. The Korean War, the first American war fought under an international flag and without a declaration, had begun as containment's first shooting test.",
             kick='C · Invasion and Intervention', size=24)

# ------------------------------------------------------ 11 PUSAN
content_text('The Pusan Perimeter',
             ['The first summer goes badly',
              'Defenders driven into a corner around Pusan',
              'The perimeter holds through August',
              'MacArthur plans a landing far behind the front'],
             "The first summer of the war was a retreat, and students should feel its length before Inchon reverses it. North Korean troops drove south through July against American units rushed from occupation duty in Japan, short of training, equipment, and numbers. By August the defenders held only the Pusan Perimeter, a corner of the peninsula around the port of Pusan at its southeast tip. Through August and into September the perimeter held, supplied through the port and covered by air power, while the North Korean army at the end of its supply lines weakened. MacArthur refused to spend his reserves merely strengthening the corner. His answer, prepared through the summer against the doubts of the Joint Chiefs, was an amphibious landing deep behind the front at Inchon, the port for Seoul. The next section takes up the landing and the decision that followed it, which students will judge in the activity as the war's hinge.",
             kick='C · Invasion and Intervention', size=24)

# ------------------------------------------------- 12 SECTION D DIVIDER
divider_photo('firstwave-port.jpg', 'Section D', 'Inchon and the Drive North',
              ['First wave of Marines heads for the landing', 'beach at Inchon, September 15, 1950.'],
              "The photograph, an official United States Navy photograph from the collections of the Naval Historical Center, shows the first wave of Marines in landing craft heading for the beach at Inchon on September 15, 1950, possibly toward the Wolmi-do landings, in the judgment of the Naval Historical Center caption. Section D covers the turn of the war, and it has two movements students must keep apart. The first is the landing itself, a rescue operation that destroyed the North Korean army in the south and restored the position of June. The second is the decision that followed, to cross the 38th parallel and unify Korea by force, which changed the war from a rescue into a rollback. The first movement was MacArthur's triumph and is still studied as a model amphibious operation. The second movement brought China into the war within two months. The activity asks students to weigh the two movements separately, and the deck does the same.",
              title_size=40)

# ------------------------------------------------------ 13 INCHON
content_photo('lopez-port.jpg', 'Over the seawall at Inchon',
              ['September 15, 1950: Marines land at Inchon',
               'Seawalls climbed at high tide',
               'Seoul retaken within two weeks',
               'The parallel crossed in October',
               'The aim changes: unify Korea by force'],
              "The photograph, a United States Marine Corps photograph held by the Naval Historical Center, shows First Lieutenant Baldomero Lopez leading his platoon over the seawall on Red Beach at Inchon on September 15, 1950. Lopez was killed within minutes of this photograph, covering a grenade with his body, and received the Medal of Honor. Teach the landing from its difficulty: tides up to about thirty feet, mud flats at low water, and seawalls above the beaches, which is why the North Koreans had left the port lightly held. Marines took Wolmi-do island in the morning and the city on the evening tide, about seventy thousand troops in the operation. Seoul was retaken within two weeks, and the North Korean army in the south, cut off from supply, collapsed. Then mark the turn. In October, United Nations forces crossed the 38th parallel, and the aim of the war changed from preserving South Korea to unifying Korea by force.",
              kick='D · Inchon and the Drive North')

# ------------------------------------------------- 14 SECTION E DIVIDER
divider_photo('commandpost-port.jpg', 'Section E', 'China Enters and the War Settles',
              ['A Marine command post near the', 'Chosin Reservoir, winter 1950.'],
              "The photograph shows Marines of the 2nd Battalion, 5th Marines at a command post near the Chosin Reservoir, in an official United States photograph from the National Archives series carried on Wikimedia Commons. Section E covers the reversal that undid the triumph of section D. China had warned, in public statements and through diplomatic channels, that it would not stand aside while United Nations forces approached the Yalu River, its border with Korea. The warnings were discounted in Washington and in Tokyo, where MacArthur assured the president at Wake Island in October that the war was won and that Chinese intervention, if it came, would be small and late. Chinese soldiers were already crossing the Yalu at night and hiding by day. They struck in late October, broke contact, and were read as a bluff. On November 25 they attacked in force. What followed was a different war, fought to a standstill over the same ground for two more years.",
              title_size=38)

# ------------------------------------------------------ 15 CHINA ENTERS
content_text('November 25, 1950',
             ['Warnings from China, discounted',
              'Chinese troops cross the Yalu in secret',
              'Attack in force along the whole front',
              'The Chosin Reservoir breakout in subzero cold',
              'Seoul falls again in January 1951'],
             "About three hundred thousand Chinese troops were in Korea by late November 1950, moved at night and hidden by day from American aircraft. Their first attacks in late October, against South Korean and American units, were broken off by design, and headquarters in Tokyo read the withdrawal as evidence that China's intervention would stay small. The offensive of November 25 corrected that reading along the whole front. In the west, the Eighth Army was driven back in a long retreat. In the northeast, around the Chosin Reservoir, Marines fought their way out of encirclement in bitter cold to the port of Hungnam and evacuation by sea. Seoul fell to the Communists again in January 1951 and was retaken in March. By the summer of 1951 the front had settled near the 38th parallel. The war of movement was over. The war of position, and of negotiation, had begun, and it would run for two years without changing the map.",
             kick='E · China Enters and the War Settles', size=24)

# ------------------------------------------------------ 16 STAT CHOSIN
stat('120,000', 'Chinese troops around the Chosin Reservoir',
     'Against some 30,000 United Nations troops · A four to one balance in subzero cold · November to December 1950',
     "These figures are the estimates carried in the standard accounting of the Chosin Reservoir campaign, and the activity tests them, so give them slowly. Around the reservoir in late November 1950, about one hundred twenty thousand Chinese troops surrounded some thirty thousand United Nations troops, most of them United States Marines of the 1st Marine Division with attached Army units. The cold was a weapon in itself: temperatures fell well below zero, weapons and vehicles failed, and frostbite took men out of the line in numbers rivaling the wounded. The surrounded force fought its way south down a single mountain road to the port of Hungnam, carrying its wounded and much of its equipment, and was evacuated by sea in December. Teachers should hold both truths at once, as the activity key does. The force was driven out of the northeast in defeat, and it was not destroyed. That combination, a defeat that was not a disaster, is the shape the whole war was taking.",
     kick='E · China Enters and the War Settles')

# ------------------------------------------------- 17 SECTION F DIVIDER
divider_text('Section F', 'MacArthur and Truman',
             'A general who wanted a wider war, and a president who held the limit.',
             "This section is a constitutional argument conducted inside a war, and it should be taught as an argument, with both positions stated at their strongest. MacArthur's position was a soldier's logic: a war half fought, against an enemy granted sanctuary across a border, asked soldiers to die for an aim smaller than victory, and he proposed to end the stalemate by striking the enemy's bases, coast, and reinforcements directly. Truman's position was a strategist's logic: every widening step risked Soviet entry, and a third world war was a price no Korean outcome could justify, so the war would stay limited even at the cost of stalemate. Between those logics stood a rule older than both men, that in the American system the elected civilian decides the aims of a war and the uniformed commander carries them out. The section's climax, the dismissal of April 1951, was that rule enforced at the height of a war, against its most decorated commander.")

# ------------------------------------------------------ 18 THE GENERAL
content_photo('macarthur-port.jpg', 'The general against the limit',
              ['Blockade the Chinese coast',
               'Bomb the bases in Manchuria',
               'Bring in Nationalist troops from Taiwan',
               'Washington refuses each step',
               'April 11, 1951: relieved of command'],
              "The photograph, an official United States Navy photograph held by the National Archives, shows General MacArthur boarding USS Missouri off Inchon on September 21, 1950, during the triumph this section's argument grew out of. By the spring of 1951 MacArthur was pressing Washington for a wider war. His program had four parts students should be able to list: a naval blockade of the Chinese coast, bombing of Chinese bases and supply lines in Manchuria, air reconnaissance over Chinese territory, and the use of Chiang Kai-shek's Nationalist troops from Taiwan. Truman and the Joint Chiefs refused each step, judging that each one widened the war toward the Soviet Union, whose treaty with China was a year old. MacArthur then pressed his case in public, in statements and letters that undercut a peace move the president was preparing and told the country its commander disagreed with its policy. On April 11, 1951, Truman relieved him of all his commands and named General Matthew Ridgway in his place.",
              kick='F · MacArthur and Truman')

# ------------------------------------------------------ 19 CIVILIAN CONTROL
content_text('Civilian control, and a farewell',
             ['Truman: commanders must be governed by policy',
              'Debate is free; command is not',
              'MacArthur addresses Congress, April 19',
              'Old soldiers never die; they just fade away',
              'The policy does not change'],
             "Truman's statement of April 11, which students read verbatim in the activity, laid down the rule in his own sequence. Full and vigorous debate on national policy, he wrote, is vital in a free democracy. It is fundamental, however, that military commanders must be governed by the policies and directives issued to them under the laws and the Constitution, a consideration he called particularly compelling in a crisis. MacArthur came home to enormous crowds and addressed Congress on April 19, 1951. His closing lines, from an old barracks ballad, were that old soldiers never die; they just fade away, and the address won him the public argument of that week. It changed nothing about the war. The limited war stayed limited, Ridgway and then General Mark Clark commanded it to its end, and the administration's critics in Congress held hearings and let the policy stand. Teach the outcome plainly: the dismissal was unpopular, and it held.",
             kick='F · MacArthur and Truman', size=24)

# ------------------------------------------------- 20 SECTION G DIVIDER
divider_text('Section G', 'Armistice Without Victory',
             'Two years of talks for a line the war had started on.',
             "Section G covers the longest negotiation of the war and its deliberately incomplete ending. Armistice talks opened in July 1951, while the fighting continued, and the two sides settled most questions early: a line along the final positions, a demilitarized zone, and supervision of the truce. One question held the agreement for most of two years, and it was a question of principle disguised as procedure. The United Nations Command held about one hundred fifty thousand prisoners, thousands of whom refused to return to Communist rule, and the United States held that no prisoner would be forced home. Students should notice what kind of issue could extend a war: not territory, which had stopped moving, but the fate of individual prisoners and the propaganda value of their refusal. The agreement of July 1953 gave the refusers to a neutral commission. The shooting stopped that night. No peace conference settled Korea afterward.")

# ------------------------------------------------------ 21 TALKS
content_text('Two years of talks',
             ['Talks open July 1951, at Kaesong, then Panmunjom',
              '158 meetings over two years and seventeen days',
              'The stall: prisoners who refused to go home',
              'Signed July 27, 1953; the guns stop at 10 that night',
              'No peace treaty follows'],
             "The figures on this slide are the record of the negotiation, and the first two belong together: 158 meetings spread over two years and seventeen days, the longest negotiated armistice in history, in the National Archives' accounting. The talks fixed a Military Demarcation Line along the final line of contact, close to the 38th parallel, with a demilitarized zone about two and a half miles wide drawn along it, and a Military Armistice Commission to supervise the truce. The agreement was signed by commanders, not governments, on July 27, 1953, and the shooting stopped at ten o'clock that evening. South Korea's president, Syngman Rhee, refused to sign, because the agreement left his country divided. No peace treaty has followed, and the two Korean states remain divided along that line. Close the section with the reading's last idea: Korea set the template for later American wars, undeclared, fought for limited aims, and ended by negotiation rather than victory.",
             kick='G · Armistice Without Victory', size=24)

# ------------------------------------------------------ 22 STAT DEAD
stat('36,000+', 'Americans dead in the Korean War',
     'Korean dead in the millions, soldiers and civilians together · Chinese dead in the hundreds of thousands · The line ended close to where the war began',
     "State these costs as ranges, the way the reading states them, because exact counts for Korean and Chinese losses do not exist and honest teaching keeps the uncertainty visible. The American figure is the firmest: more than thirty six thousand dead, a count students will meet as 36,516 or a near figure in standard references depending on which categories are included. Korean losses, soldiers and civilians of both states together, are estimated in the millions, with civilian deaths from bombing, ground fighting, and massacre forming a large share. Chinese military deaths are estimated in the hundreds of thousands. Then put the cost against the map. Three years of this fighting moved the border a few miles in places and left the peninsula divided near the 38th parallel, approximately where the war began. That disproportion between cost and territorial result is why Korea is remembered as the war that ended without victory, and it is the fact the writing task asks students to explain rather than merely repeat.",
     kick='G · Armistice Without Victory')

# ------------------------------------------------------ 23 GLANCE
s = slide(NAVY)
kicker(s, 'Korea at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Won, lost, and settled', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The shocks', 'August and October 1949: the bomb and China', 'Expansion read as one design'),
        ('The paper answer', 'NSC-68, April 1950: buildup to check and roll back', 'Shelved on cost, adopted in war'),
        ('The war in motion', 'Invasion, Inchon, the Yalu, intervention', 'Rescue won, unification lost'),
        ('The settlement', 'The limit held in 1951; armistice in 1953', 'The starting line, at full price')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, Korea at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The four rows are the lesson's argument in order. The shocks covers the Soviet bomb of August 29, 1949 and the proclamation of the People's Republic of China on October 1, 1949, and the reading of both as one design. The paper answer covers NSC-68, its global description of the struggle, and its buildup shelved on cost and adopted in war. The war in motion covers the invasion of June 1950, Inchon, the crossing of the parallel, and the Chinese intervention, sorting the rescue that was won from the unification that was lost. The settlement covers the dismissal of April 1951 and the armistice of July 27, 1953. Grade the table generously on wording and strictly on the sorting: an entry that calls the war simply lost has missed the preserved South Korea in the second row.")

# ------------------------------------------------------ 24 VOCAB A
vocab('Words for the turn to Asia',
      [('NSC-68', 'the secret 1950 planning paper calling for a large buildup'),
       ("People's Republic of China", 'the Communist state Mao proclaimed in 1949'),
       ('Korean War', 'the war of 1950 to 1953, fought to preserve South Korea'),
       ('38th parallel', 'the line dividing the occupation zones, then the border')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. The first term is NSC-68: the secret American planning paper of 1950 that described the Cold War as a global struggle and called for a large buildup of American military strength. The second is People's Republic of China: the Communist state Mao Zedong proclaimed in 1949 after his forces won the Chinese civil war, recognized by the Soviet Union and not by the United States. The third is Korean War: the war of 1950 to 1953 in which the United States and United Nations forces fought North Korea and China to preserve a non-Communist South Korea. The fourth is 38th parallel: the line of latitude chosen in 1945 to divide Soviet and American occupation zones in Korea, which became the border between North and South Korea.")

# ------------------------------------------------------ 25 VOCAB B
vocab('Words for the ending',
      [('limited war', 'a war fought for limited aims, some weapons left unused'),
       ('stalemate', 'fighting in which neither side can force a decision'),
       ('armistice', 'an agreement to stop fighting, short of a peace treaty')],
      "Three more terms, again matching the guided notes exactly. The first is limited war: a war fought for limited aims with some weapons and targets deliberately left unused, rather than for the enemy's total defeat. That definition is the rule Truman enforced against MacArthur, and students should be able to apply it to the refused steps of section F, the blockade, the bombing in Manchuria, and the Nationalist troops. The second is stalemate: a condition in fighting in which neither side can gain ground or force a decision, however long the fighting continues. Korea reached it by the summer of 1951 and held it for two years. The third is armistice: an agreement to stop fighting; the Korean armistice of 1953 ended the shooting without a peace treaty or a political settlement. Keep the last two terms distinct in review: stalemate describes the fighting, armistice describes the paper that stopped it.")

# ------------------------------------------------------ 26 SYNTHESIS
s = slide(NAVY)
kicker(s, 'The lesson in one view')
text(s, 0.9, 1.28, 11.5, 1.0, 'An armistice, not a victory', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Won', 'South Korea preserved, the aim of June 1950'),
        ('Lost', 'Unification, the aim added in October 1950'),
        ('Refused', 'A wider war with China, at every step from 1950 to 1951'),
        ('Settled', 'A divided peninsula on the starting line, since 1953')]
yy = 2.78
for t, d in rows:
    text(s, 0.9, yy, 2.4, 0.7, t, size=24, color=RUST_LT, font='Georgia')
    text(s, 3.45, yy + 0.05, 9.0, 0.9, d, size=19, color=CREAM, leading=1.2)
    yy += 1.05
notes(s, "Use this slide to close the argument before the work begins, and make students say the four rows aloud in order, because the sorting is the lesson. Won: South Korea was preserved, its government survived, and the invasion of June 1950 was reversed, which was the aim the United States entered the war to achieve. Lost: unification of the peninsula by force, the aim added after Inchon, was abandoned by December 1950 and never recovered. Refused: at every decision point from the drive to the Yalu to the dismissal of MacArthur, Washington declined to widen the war against China, accepting stalemate as the price of avoiding a third world war. Settled: the armistice of July 27, 1953 froze the division near the 38th parallel, where it remains. A student who can hold all four rows at once can answer the lesson question. A student who holds only one row has a slogan, and the writing task will show it.")

# ------------------------------------------------------ 27 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did the Cold War turn into a shooting war in Asia, and why did Korea end without victory? Follow the decisions before you judge them.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Limited War File: five stations, a decision ledger, and a verdict'),
        ('Notebook', 'Notebook page: five decision points, marked won, lost, or settled'),
        ('Quick check', 'The Reservoir in Winter: Chosin, NSC-68, and the dismissal'),
        ('Writing', 'Won, Lost, or Settled: the lesson question as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the two shocks with dates, limited war and the dismissed commander, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Limited War File, puts five stations in front of students: NSC-68 in its own words, a summary of Inchon and the drive north, a summary of the Chinese intervention, Truman's dismissal statement with MacArthur's farewell closing, and the armistice terms, and it ends with a decision ledger and a verdict on where the war was decided. The notebook page asks students to mark five decision points won, lost, or settled from the record. The quick check, The Reservoir in Winter, tests the Chosin figures, the two shocks behind NSC-68, and the grounds of the dismissal against the photograph of the exhausted Marines. The writing task turns the lesson question into an essay argued from the evidence bank. The exit ticket has three parts: the two shocks of 1949 with their dates, limited war with the commander dismissed for pressing against it, and the lesson question in two or three sentences. Next lesson turns home, to the fear the war fed.")

dc.save(OUT)
