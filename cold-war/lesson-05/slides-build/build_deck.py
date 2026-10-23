#!/usr/bin/env python3
"""Cold War Lesson 5 deck, "Cuba: Revolution and the Missile Crisis,"
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

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'THE COLD WAR · LESSON 5', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Cuba: Revolution and the Missile Crisis', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Ninety miles from Florida, thirteen days in October', size=17, color=POWDER)
notes(s, "The photograph shows President Kennedy meeting with the Executive Committee of the National Security Council in the Cabinet Room on October 29, 1962, photographed by Cecil Stoughton of the White House staff. It was taken the day after the missile crisis ended, and it opens a lesson that runs backward and forward from that room. Backward: a revolution in Cuba in 1959, a failed invasion in 1961, and a secret Soviet decision to place nuclear missiles ninety miles from Florida. Forward: thirteen days in October 1962 that brought the two superpowers closer to nuclear war than any other episode of the Cold War, and the safeguards those thirteen days produced. Students should leave able to explain why the missiles went in, how the crisis was settled in two parts, one public and one secret, and what the settlement built.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('Why did the Soviet Union put missiles in Cuba, and how did thirteen days in October 1962 change the Cold War?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the struggle between the United States and the Soviet Union reshape the world and American life, and why did it end the way it did?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "The lesson question has two halves, and students should keep both in view all hour. The first half asks why the missiles went in, which is a question about motives on three sides: Castro wanted protection against another American invasion, Khrushchev wanted to answer American missiles in Turkey and narrow the missile gap cheaply, and both men had read the Bay of Pigs failure as evidence about President Kennedy. The second half asks what thirteen days changed, which is a question about results: a two part settlement, a direct communications link between Washington and Moscow, and a treaty banning nuclear tests in the atmosphere, in space, and under water. The unit question runs beneath as the frame. This lesson is the Cold War at its most dangerous, and its ending taught both sides a rule they carried for the rest of the contest.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'From revolution to the brink, and back', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'An island ninety miles away', 'Batista, American ties, and resentment'),
        ('B', 'The turn toward Moscow', 'Land reform, seizures, and the 1960 trade deal'),
        ('C', 'The Bay of Pigs', 'Defeated in three days; two lessons learned'),
        ('D', 'Why missiles, and the photograph', 'Turkey, deterrence, and the U-2 of October 14'),
        ('E', 'Thirteen days: the quarantine', 'Secret deliberation, then the October 22 address'),
        ('F', 'October 27: the closest day', 'Two letters, a shootdown, and a secret meeting'),
        ('G', 'The settlement and what it built', 'A public part, a secret part, the hotline, the test ban')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Sections A through C build the road to the crisis: the revolution of 1959, the break with Washington and the turn to Moscow by 1961, and the failed invasion that taught Havana and Moscow opposite lessons from the same event. Section D gives the motives for the missile deployment and the photograph that exposed it. Sections E and F cover the thirteen days themselves, the secret deliberation and public quarantine, then the single closest day, October 27. Section G separates the settlement into its public and secret parts and closes with the hotline and the Limited Test Ban Treaty of 1963. Tell students the summary table at the end of their guided notes, The Crisis at a Glance, asks them to rebuild this map with dates attached.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', 'An Island Ninety Miles Away',
             'Sugar, American property, and a strongman kept by American support.',
             "Open with geography and dependence together, because the crisis of 1962 grew out of both. Cuba sits ninety miles from Florida. Its sugar economy was tied to the United States, American companies held large Cuban properties, and its government under Fulgencio Batista rested on American support. Batista jailed opponents, and resentment of his regime and of American influence ran deep on the island. Students sometimes treat the revolution as a Cold War event from its first day. It was not. It began as a Cuban revolt against a Cuban dictatorship with deep American ties, and the Cold War entered through the quarrel that followed, over land, property, and who would buy Cuban sugar. Keep that order straight today, because the sequence explains why Castro could present every later American action, including the missile crisis itself, to Cubans as one more chapter of an old story about subordination.")

# ------------------------------------------------------ 5 SECTION A CONTENT
content_text('January 1, 1959: the old order ends',
             ['Batista flees; Castro takes Havana',
              'The United States recognizes the new government within days',
              'A revolution against a dictatorship with American ties',
              'The open question: could recognition survive what came next?'],
             "On January 1, 1959, Batista fled the country and Fidel Castro and his guerrilla army entered Havana. Use the full guided notes definition here and have students check it in their notes: the Cuban Revolution is the revolution that brought Fidel Castro to power in Cuba in 1959, overthrowing the government of Fulgencio Batista and turning toward alliance with the Soviet Union. Note that the definition itself contains the whole arc of sections A and B: a revolution first, and a turn toward Moscow second, as a result of what happened between Havana and Washington. The United States recognized the new government within days, which students often find surprising. Recognition was not the problem. The problem was the program Castro began to carry out in his first two years, and the American answer to it, which is where section B begins. Ask students to hold one question through the next section: at each step, who moved first, and who was answering whom?",
             kick='A · An island ninety miles away')

# ------------------------------------------------- 6 SECTION B DIVIDER
divider_text('Section B', 'The Turn Toward Moscow',
             'Land reform, seized property, Soviet oil, and a broken relationship by 1961.',
             "Section B covers two years of action and reaction, and it should be taught as a sequence rather than as a list of grievances. Castro's government broke up large estates, including American owned sugar land. It seized American property without payment Washington would accept, and it narrowed the space for political opposition at home. Washington protested each step. Then, in February 1960, Cuba signed a trade agreement with the Soviet Union, exchanging Cuban sugar for Soviet oil, credits, and aid. Washington answered by cutting off Cuban sugar sales to the United States, Cuba answered by taking more American property, and in January 1961 the two countries broke diplomatic relations. By the time President Kennedy took office, Cuba had a patron across the ocean and the Soviet Union had an ally in the Western Hemisphere for the first time. Neither side had planned that outcome in January 1959. Both sides had produced it by answering each other.")

# ------------------------------------------------------ 7 SECTION B CONTENT
content_text('Action and reaction, 1959 to 1961',
             ['Land reform breaks up large estates, including American sugar land',
              'American property seized without payment Washington would accept',
              'February 1960: sugar for Soviet oil, credits, and aid',
              'Washington cuts off Cuban sugar sales',
              'January 1961: diplomatic relations broken'],
             "Walk the sequence slowly and make students name the direction of each move. The land reform and the seizures were Cuban decisions aimed at the structure of the old economy, and they struck American companies directly, which is why the reading says American interests were hit first and hardest. The February 1960 trade agreement was the turn in the section title: Cuban sugar would now go east, and Soviet oil, credits, and aid would come west. Washington's sugar cutoff was meant as pressure to reverse the turn. It had the opposite effect, pushing Havana to take more American property and lean harder on Moscow. By January 1961 the break was formal. The teaching point is the mechanism, because students will meet it again in this unit: pressure applied to force a small state away from a rival patron can deepen the dependence it was meant to break, when the patron is willing to pay the bill the pressure creates.",
             kick='B · The turn toward Moscow', size=24)

# ------------------------------------------------- 8 SECTION C DIVIDER
divider_text('Section C', 'The Bay of Pigs and What It Taught',
             'An invasion defeated in three days, and two lessons that pointed to 1962.',
             "Section C covers the event that connects the Cuban quarrel to the missile crisis, and it is short enough to teach whole. President Kennedy inherited a secret plan to overthrow Castro, drawn up under President Eisenhower, and in April 1961 he let it go forward. About 1,400 Cuban exiles, trained and supplied by the United States, landed at the Bay of Pigs on Cuba's southern coast on April 17. The expected Cuban uprising never came. Kennedy refused to commit American air power directly, and the landing force was defeated on the beach within three days. A failed invasion of a small island by a superpower's clients might look like a side episode. Teach it instead as the hinge of the lesson. Havana and Moscow both studied the failure, drew opposite lessons from it, and acted on those lessons in ways that produced October 1962. The next two slides take the event and then the lessons in order.")

# ------------------------------------------------------ 9 SECTION C CONTENT
content_text('April 1961: defeated on the beach',
             ['A secret plan inherited from the Eisenhower administration',
              'April 17: about 1,400 Cuban exiles land at the Bay of Pigs',
              'The expected uprising never came',
              'Kennedy refused direct American air power',
              'Defeated within three days'],
             "Use the guided notes definition and have students copy it exactly: the Bay of Pigs invasion is the failed invasion of Cuba in April 1961 by Cuban exiles trained and supplied by the United States, defeated on the beach within three days. Every phrase carries a fact the test can ask for. Cuban exiles: the landing force was not the American military, which is why the operation could be disowned and why it could also be abandoned. Trained and supplied by the United States: the American role was real, organized by the Central Intelligence Agency from a plan Kennedy inherited and approved. Defeated within three days: the speed is the fact students should remember, because it shaped what both audiences concluded. Castro's forces, fighting on their own ground with the population not rising, destroyed the landing before Washington had to decide whether to rescue it with American power. Kennedy chose not to, and that choice, as much as the landing itself, is what Havana and Moscow remembered.",
             kick='C · The Bay of Pigs and what it taught', size=24)

# ------------------------------------------------------ 10 SECTION C STAT
stat('3', 'days from landing to defeat at the Bay of Pigs',
     'About 1,400 exiles landed on April 17, 1961 · The lessons of those three days produced October 1962',
     "Stop on the two lessons, because they are the bridge from this section to the missile deployment, and blueprint entry 9 tests them directly. Castro's lesson was about the future: the United States had tried once with a small force and would, he concluded, try again with a larger one. A Cuban leader who believed that needed a guarantee stronger than his own army, and he went looking for one in Moscow. Khrushchev's lesson was about Kennedy: the young president had approved an invasion and then declined to save it, and the Soviet leader read him as inexperienced and pushable. Both lessons were readings of the same three days, and both were plausible, which is worth saying aloud. The missile decision of 1962 rested on the two together. Without Castro's fear, there is no Cuban request for protection. Without Khrushchev's reading of Kennedy, there is no Soviet willingness to run the risk of placing nuclear missiles ninety miles from Florida in secret.",
     kick='C · The Bay of Pigs and what it taught')

# ------------------------------------------------- 11 SECTION D DIVIDER
divider_photo('u2-sites-port.jpg', 'Section D', 'Why Missiles, and the Photograph',
              ['A Soviet missile site at San Cristobal,', 'photographed from the air and marked by analysts.'],
              "The photograph is an American reconnaissance photograph of a Soviet missile site at San Cristobal, Cuba, with the analysts' markings drawn on the frame: launch positions, a missile ready tent, and fuel trailers identified by the men who read the film. One caution belongs in the teaching and in the lesson's source record. The frame as downloaded carries its own label dating it November 1, 1962 and marking former launch positions, while the audited source record dates the U-2 reconnaissance photograph of the sites to October 14. Show students both facts rather than smoothing them over: the discovery photographs of October 14 established the sites, and reconnaissance kept photographing them through the crisis and into the withdrawal. Section D covers why the missiles were sent and how they were found. The motives come first, because a photograph of a missile site cannot explain itself. Students need Khrushchev's reasons in hand before they can judge what Kennedy was looking at on October 16.",
              title_size=38)

# ------------------------------------------------------ 12 SECTION D MOTIVES
content_text('Three reasons for the missiles',
             ['Protect Cuba: deter another American invasion',
              'Answer the Jupiter missiles in Turkey, in range of Soviet cities',
              'Narrow the missile gap cheaply',
              'Soviet missiles could reach America from Cuba, not yet in numbers from home',
              'Castro accepted them as a shield'],
             "Take the three reasons in order and flag the reading's own caution, that historians weigh them differently and students should not present any single one as settled. The first is deterrence, in the guided notes wording: the policy of preventing an enemy attack by holding a threat of retaliation so destructive that the attack would cost more than it could gain. Missiles in Cuba would raise the price of the invasion Castro expected. The second is symmetry: American Jupiter missiles stood in Turkey, within range of Soviet cities, and Khrushchev's public letter of October 27 would make exactly that comparison. The third is arithmetic. The Soviet Union had few missiles that could reach the United States from Soviet soil in 1962. Missiles already built for shorter ranges could reach American cities from Cuba at once, which made the deployment a cheap way to multiply Soviet striking power while new long range missiles were still coming.",
             kick='D · Why missiles, and the photograph', size=24)

# ------------------------------------------------------ 13 SECTION D PHOTO
content_photo('u2-tents-port.jpg', 'October 14: a camera finds the sites',
              ['A U-2 photographs the countryside near San Cristobal',
               'Analysts identify medium range missile sites under construction',
               'The missiles could strike much of the eastern United States',
               'Little warning time for American cities',
               'Kennedy is told on the morning of October 16'],
              "The photograph, credited to the Central Intelligence Agency on its file page, shows missile transporters and missile ready tents in Cuba in 1962. Teach discovery as a two step process, because the quick check tests it. First, the U-2, a high altitude reconnaissance aircraft, photographed the Cuban countryside near San Cristobal on October 14. The film by itself showed cleared ground, shapes, and equipment. Second, photo analysts identified what the shapes were: Soviet medium range missile sites under construction. That identification, not the photograph alone, is what advisers carried to the president on October 16. Then give the reason the identification produced an emergency rather than a diplomatic note. The missiles being installed could strike much of the eastern United States with little warning. Geography had always given the United States time. Sites ninety miles away took the time away, and every choice Kennedy made in the next six days was made against a construction clock, because unfinished sites were becoming operational ones while he deliberated.",
              kick='D · Why missiles, and the photograph')

# ------------------------------------------------- 14 SECTION E DIVIDER
divider_photo('kennedy-signs-port.jpg', 'Section E', 'Thirteen Days: The Quarantine',
              ['Kennedy signs the quarantine proclamation,', 'October 23, 1962. Photograph by Cecil Stoughton.'],
              "The photograph, by White House photographer Cecil Stoughton, shows President Kennedy signing Proclamation 3504 on October 23, 1962, the formal order authorizing the naval quarantine of Cuba. Section E covers the crisis in public: six days of secret deliberation, a televised address that told the world, and a line drawn at sea that Soviet ships had to choose whether to cross. The heart of the section is a decision among three options, and students should be able to name all three and explain the choice. An air strike on the sites would destroy the missiles but kill Soviet personnel and invite retaliation, perhaps against Berlin. An invasion of Cuba would be war at full scale. Pressure at sea was slower and might fail, but it held steps in reserve and gave Khrushchev time and a choice. Kennedy chose the sea, and the word he chose for the action, quarantine, was part of the choice itself.",
              title_size=38)

# ------------------------------------------------------ 15 SECTION E CONTENT
content_text('The choice, and the name he gave it',
             ['Six days of secret Executive Committee deliberation',
              'The options: air strike, invasion, or pressure at sea',
              'October 22: Kennedy announces the discovery on television',
              'A naval quarantine, not a blockade',
              'A missile from Cuba means a full retaliatory response'],
             "Have students state the vocabulary definition precisely, because it explains the central decision of the crisis: a naval quarantine is President Kennedy's name for the naval blockade of Cuba in 1962, chosen because a blockade is legally an act of war and quarantine was not. The naming was policy, not cosmetics. Calling the action a quarantine let the United States stop offensive weapons at sea without declaring that a state of war existed, and it left Khrushchev a retreat that was not surrender under a formal act of war. In the same October 22 address, Kennedy added the threat that completed the position: any nuclear missile launched from Cuba against any nation in the Western Hemisphere would be regarded as a Soviet attack on the United States, requiring a full retaliatory response upon the Soviet Union. The address is Station 2 of the activity, and its three passages map exactly onto this slide: the evidence, the quarantine, and the warning.",
             kick='E · Thirteen days: the quarantine', size=24)

# ------------------------------------------------------ 16 SECTION E PHOTO
content_photo('excomm-port.jpg', 'At the line, October 24',
              ['The quarantine takes effect on October 24',
               'Some Soviet ships turn back rather than be searched',
               'Work on the missile sites goes on at full speed',
               'American forces prepare the invasion in case pressure fails',
               'Both clocks run at once: construction and deliberation'],
              "The photograph shows the Executive Committee in the Cabinet Room on October 29, 1962, the day after the settlement, photographed by Cecil Stoughton. The committee in the photograph is the same body that deliberated in secret from October 16. By October 24 its chosen policy was being tested at sea. The quarantine took effect that morning, and the first Soviet ships approaching the line turned back rather than submit to search, which told Washington the pressure was being felt. Nothing else slowed down. Construction crews in Cuba worked at full speed to make the sites operational, and American forces in Florida and at sea prepared the air strike and invasion that would follow if the quarantine failed. Students should hold both clocks together, because the crisis's pressure came from their running at once. Every day of successful quarantine diplomacy was also a day in which the missiles Kennedy was demanding out of Cuba came closer to being able to fire.",
              kick='E · Thirteen days: the quarantine')

# ------------------------------------------------- 17 SECTION F DIVIDER
divider_text('Section F', 'October 27: The Closest Day',
             'Two letters, a U-2 shot down, a second U-2 lost over Siberia, and a secret meeting at night.',
             "Section F covers one day, Saturday, October 27, 1962, and it earns a full section because more happened on it, and more nearly went wrong, than on any other day of the crisis. The morning brought a second letter from Khrushchev, public and harder than the first, adding a public demand about Turkey to the private offer of the day before. In Cuba, a Soviet surface to air missile shot down an American U-2 and killed its pilot. Over the Soviet Union, another American U-2 strayed off course. By nightfall the president's brother was sitting across from the Soviet ambassador with a secret assurance and a request for an answer within a day. Teach the day in that order, documents first and accidents second, because the documents are what students can argue from, and the accidents explain why everyone in the documents was in such a hurry. The two letters and the cable are Stations 3, 4, and 5 of the activity.")

# ------------------------------------------------------ 18 SECTION F LETTERS
content_text('Two letters in two days',
             ['October 26: missiles out, for a pledge not to invade Cuba',
              'October 27, public: the same offer, plus the Jupiter missiles in Turkey',
              'Khrushchev\u2019s argument: Cuba is 90 miles from America; Turkey adjoins us',
              'Kennedy answers the first letter and sets the second aside'],
             "Set the two letters side by side, because the writing task asks students to judge between them and the distinction has to be exact. The October 26 letter, which students meet in the activity as Kennedy's reply carries it, offered a clean exchange: the weapons systems would leave Cuba under United Nations observation, no more would be introduced, and in return the United States would lift the quarantine and give assurances against an invasion of Cuba. It never mentioned Turkey. The October 27 letter, broadcast publicly, kept that offer and added a condition: the United States would remove its analogous means, the Jupiter missiles, from Turkey. Its argument was geographical symmetry, and it was a strong argument, which is why it was dangerous. Kennedy's advisers chose to answer the first letter as if the second had not arrived. That choice, sometimes called the Trollope ploy in later accounts, let Washington close on terms it could announce, while the Turkey question moved into a secret channel the same night.",
             kick='F · October 27: the closest day', size=24)

# ------------------------------------------------------ 19 SECTION F STAT
stat('27', 'October 1962: the day the crisis nearly escaped both leaders',
     'A U-2 shot down over Cuba, its pilot killed · Another U-2 strayed over Siberia · A secret meeting that night',
     "Slow down on the two air incidents, and state them at the precision the record supports. A Soviet surface to air missile battery in Cuba shot down an American U-2 on a reconnaissance flight, killing its pilot, Major Rudolf Anderson. He was the only American killed by hostile fire during the crisis. The firing was a local military act, not an order Kennedy had provoked or Khrushchev had personally given that morning, and both leaders understood that such acts could start the war neither was choosing. The second incident ran the other way: an American U-2 on an air sampling mission strayed over Soviet territory in Siberia before turning back, on the same day, giving Moscow its own reason to wonder whether an attack was beginning. This is the day's real lesson about nuclear crises. The danger did not come only from decisions at the top. It came from machines, orders written earlier, and men far from both capitals, moving faster than the letters crossing between the two leaders.",
     kick='F · October 27: the closest day')

# ------------------------------------------------- 20 SECTION G DIVIDER
divider_text('Section G', 'The Settlement and What It Built',
             'Announced on October 28, completed in secret, and followed in 1963 by the hotline and the test ban.',
             "Section G closes the crisis and opens its consequences, and the section's first duty is separation: what was announced, what was secretly agreed, and what was built afterward are three different things, and students who merge them will repeat the public story of 1962 instead of the documented one. On Sunday, October 28, Khrushchev announced over Moscow radio that the missiles would be withdrawn. The public settlement had two parts, Soviet missiles out of Cuba and an American pledge not to invade the island. The secret part, the removal of the American Jupiter missiles from Turkey months later, was denied by both governments at the time and established by later evidence, including the Dobrynin cable students read in the activity. Then, in 1963, came the safeguards: a direct link between the capitals and a treaty limiting nuclear tests. Teach the section as an ending with a long tail, because the tail is what the lesson question's second half asks about.")

# ------------------------------------------------------ 21 SECTION G SETTLEMENT
content_text('Two parts: one announced, one denied',
             ['October 28: Khrushchev announces the withdrawal',
              'Public: missiles out of Cuba; an American pledge not to invade',
              'Secret: the Jupiter missiles quietly leave Turkey months later',
              'The Turkey part was denied at the time, established by later evidence',
              'The Dobrynin cable records the assurance: 4 to 5 months, nothing public'],
             "Use the full definition once here, in the guided notes wording: the Cuban Missile Crisis is the confrontation of October 1962 in which the United States discovered Soviet nuclear missiles being installed in Cuba and forced their withdrawal short of war. Then separate the settlement. The public part was announced on October 28 and could be announced, because it cost Kennedy nothing he had not offered in his October 27 letter and it gave Khrushchev a pledge he could present at home. The secret part could not be announced. The Jupiter missiles had been placed in Turkey by a decision of the NATO Council, and Robert Kennedy told Dobrynin plainly that a public withdrawal under Soviet pressure would tear at the alliance, which is why the assurance came with its two conditions: four to five months to carry it out, and nothing said in public. The missiles did leave Turkey, quietly, the following spring. Both governments denied a trade at the time, and the record that later established it is a document students hold in this lesson, the Soviet ambassador's own cable to Moscow.",
             kick='G · The settlement and what it built', size=24)

# ------------------------------------------------------ 22 SECTION G SAFEGUARDS
content_text('What thirteen days built',
             ['1963: a direct link between Washington and Moscow',
              '1963: nuclear tests banned in the air, in space, and under water',
              'A shared rule: never lose control of a direct confrontation',
              'The arsenals remained; the conduct around them changed'],
             "Give both definitions in full, as the guided notes carry them. The hotline is the direct communications link between Washington and Moscow established in 1963 so the two leaders could reach each other at once in a crisis. It was a teletype link, not the red telephone of popular imagination, and it answered the crisis's plainest failure: in October 1962 the two leaders had exchanged letters that took hours to deliver, translate, and answer, while events in Cuba moved in minutes. The Limited Test Ban Treaty is the treaty of 1963 in which the United States, the Soviet Union, and Britain banned nuclear weapons tests in the atmosphere, in space, and under water. Underground tests continued, and the arms race continued with them, which students should hear plainly. What changed was conduct at the edge: both sides had looked into a crisis neither could fully control, and both spent 1963 building ways to keep the next one slower, better informed, and further from the point of no return.",
             kick='G · The settlement and what it built', size=24)

# ------------------------------------------------------ 23 GLANCE
s = slide(NAVY)
kicker(s, 'The Crisis at a Glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'How it began, broke, and settled', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Before the crisis', 'Revolution, the break, the Bay of Pigs', 'The motives both sides carried into 1962'),
        ('Discovery and choice', 'October 14 photograph; quarantine chosen', 'Pressure at sea, with war held in reserve'),
        ('The closest day', 'October 27: two letters, two air incidents', 'A secret channel opened that night'),
        ('Settlement', 'Public terms, secret Turkey removal', 'The hotline and the test ban of 1963')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, The Crisis at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The four rows are the lesson's argument in miniature. Before the crisis, the revolution, the break with Washington, and the Bay of Pigs supplied every motive the crisis ran on. Discovery and choice turned a photograph into a policy: the quarantine, with air strike and invasion held in reserve. The closest day, October 27, showed how thin the leaders' control had become and pushed the real bargaining into a secret channel. The settlement row must be completed in two parts or it is wrong: the public terms announced on October 28 and the secret Turkey removal, followed in 1963 by the hotline and the test ban. Grade the table generously on wording and strictly on that separation, because the two part settlement is the lesson's central documented fact.")

# ------------------------------------------------------ 24 VOCAB A
vocab('Words for the road to the crisis',
      [('Cuban Revolution', 'brought Castro to power in 1959, overthrowing Batista'),
       ('Bay of Pigs invasion', 'exiles trained and supplied by the United States, defeated in three days'),
       ('deterrence', 'preventing attack by a threat of retaliation too costly to risk'),
       ('Cuban Missile Crisis', 'October 1962: Soviet missiles found in Cuba, withdrawn short of war')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. Cuban Revolution: the revolution that brought Fidel Castro to power in Cuba in 1959, overthrowing the government of Fulgencio Batista and turning toward alliance with the Soviet Union. Bay of Pigs invasion: the failed invasion of Cuba in April 1961 by Cuban exiles trained and supplied by the United States, defeated on the beach within three days. The third term is deterrence: the policy of preventing an enemy attack by holding a threat of retaliation so destructive that the attack would cost more than it could gain. The fourth term is Cuban Missile Crisis: the confrontation of October 1962 in which the United States discovered Soviet nuclear missiles being installed in Cuba and forced their withdrawal short of war. Note the order: two events in Cuba, then the doctrine, then the crisis the doctrine failed to prevent and finally helped to end.")

# ------------------------------------------------------ 25 VOCAB B
vocab('Words for the settlement',
      [('naval quarantine', "Kennedy's name for the blockade, because a blockade is an act of war"),
       ('hotline', 'the direct Washington to Moscow link built in 1963'),
       ('Limited Test Ban Treaty', '1963: no tests in the atmosphere, in space, or under water')],
      "Three more terms, again matching the guided notes exactly. The first is naval quarantine: President Kennedy's name for the naval blockade of Cuba in 1962, chosen because a blockade is legally an act of war and quarantine was not. Students should be able to explain the choice, not only recite it: the word held the action short of a legal state of war. The second is hotline: the direct communications link between Washington and Moscow established in 1963 so the two leaders could reach each other at once in a crisis. The third is Limited Test Ban Treaty: the treaty of 1963 in which the United States, the Soviet Union, and Britain banned nuclear weapons tests in the atmosphere, in space, and under water. End the vocabulary on the treaty's limits, which its own name carries. The ban was limited: underground testing continued, and so did the arms race. The crisis had changed the conduct of the rivalry, not ended the rivalry itself, and the next lesson takes up the war the rivalry produced in Vietnam.")

# ------------------------------------------------------ 26 SYNTHESIS
s = slide(NAVY)
kicker(s, 'Synthesis')
text(s, 0.9, 1.35, 11.5, 1.1, 'What thirteen days settled', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 3.4,
     ['The missiles went in because a failed invasion had taught Castro to fear another one and taught Khrushchev to discount Kennedy, and because Cuba answered the missiles already standing in Turkey.',
      'They came out through a settlement in two parts, one announced and one secret, reached on the day the crisis nearly escaped both leaders.',
      'What the thirteen days built was a way to slow the next crisis down: a direct link, a test ban, and a rule both sides had learned at the edge.'],
     size=21, color=POWDER, leading=1.3)
notes(s, "Draw the lesson together before the exit work, and do it by answering the lesson question in full sentences students can borrow. Why did the Soviet Union put missiles in Cuba? Because the Bay of Pigs had given Castro reason to expect a larger invasion and given Khrushchev reason to think Kennedy could be pushed, because American Jupiter missiles already stood in Turkey within range of Soviet cities, and because missiles in Cuba narrowed the missile gap at once and cheaply. How did thirteen days change the Cold War? The crisis ended in a settlement with a public part and a secret part, and the near loss of control on October 27 convinced both governments to build safeguards: the hotline and the Limited Test Ban Treaty of 1963. Nothing about the arsenals shrank. What changed was the machinery for keeping a confrontation from running faster than the men responsible for ending it, and students should be able to say so in those terms.")

# ------------------------------------------------------ 27 CLOSING / EXIT
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Why did the Soviet Union put missiles in Cuba, and how did thirteen days in October 1962 change the Cold War? Build from the documents, and keep the settlement in two parts.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Thirteen Days File: five records, a day by day ledger, and a verdict on the two letters'),
        ('Notebook', 'Notebook page: six stages in a chart, and the two parts in one paragraph'),
        ('Quick check', 'The Photograph and the Line: the U-2 evidence, the quarantine, and the secret part'),
        ('Writing', 'Which Letter Mattered More? Argued from the file, the cable included')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: why Castro accepted the missiles, the two parts of the settlement, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Thirteen Days File, runs five records in order: the U-2 photograph and its caption record, Kennedy's October 22 address, the October 26 letter as Kennedy's reply carries it, the October 27 letter in Khrushchev's own words, and the Dobrynin cable on the secret meeting that night. Students keep a day by day ledger across the file and close with a verdict on which letter mattered more, having first found the settlement's two parts in the documents. The quick check, The Photograph and the Line, tests the U-2 evidence and the analysts' role in producing it, then the road from the revolution to the quarantine, then the two part settlement. The writing task asks the activity's verdict question as an essay, argued from an evidence bank drawn from the file. The exit ticket has three parts: why Castro accepted the missiles, the two parts of the settlement with the public one identified, and the lesson question answered with at least two dates.")

dc.save(OUT)
