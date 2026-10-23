#!/usr/bin/env python3
"""Cold War Lesson 6 deck, "Vietnam: The War Containment Built,"
built on the shared deck system: image-led slides, fragments only on screen,
comprehensive speaker notes, full lesson and vocabulary coverage."""
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

# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'THE COLD WAR · LESSON 6', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Vietnam: The War Containment Built', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'How a strategy for holding a line produced America\'s longest war of the Cold War, 1954 to 1975', size=17, color=POWDER)
notes(s, "The photograph shows boatloads of Vietnamese refugees approaching the United States fleet in the South China Sea on April 30, 1975, in a United States Navy photograph by PH3 Harold Brown. It is the last day of the war this lesson covers, and it belongs at the front of the lesson because the whole hour runs toward it. Students will trace how the United States arrived at that harbor by steps, each one defended at the time as necessary and limited: a divided country in 1954, a resolution in 1964, a force past half a million by 1968, an offensive that broke public belief, a slower exit that widened the war, and a settlement that settled nothing. Keep the mood documentary. The records in this lesson are strong enough without heightening.")

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did containment lead the United States into Vietnam, and why did the war fail on its own terms?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the struggle between the United States and the Soviet Union reshape the world and American life, and why did it end the way it did?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "The lesson question has two halves, and students should hear both before the first section begins. The first half asks how containment led the United States into Vietnam, which is a question about a strategy becoming a sequence of steps: a theory about dominoes, a divided country, a planned resolution, and a force that grew by increments no single decision announced. The second half asks why the war failed on its own terms, which sets the standard for judgment. The war's own terms were a standing non-Communist South Vietnam and neighbors kept from falling in sequence. Students will be asked at the end to measure the ending against those terms, not against their general view of the war. The unit question runs beneath as the frame for all eight lessons.")

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Seven steps into a war, and out again', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The road in', 'A divided country, a theory of dominoes'),
        ('B', 'The Gulf of Tonkin Resolution', 'A planned step, an open ended authority'),
        ('C', 'Escalation', 'From advisers to half a million troops'),
        ('D', 'The Tet Offensive', 'A defeat on the ground, a turn at home'),
        ('E', 'Vietnamization and the wider war', 'Troops home, bombing wider, a lottery'),
        ('F', 'The accords and the fall of Saigon', 'A settlement, then April 30, 1975'),
        ('G', 'The costs and the reckoning', '58,000 dead, a war power reclaimed')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Sections A and B build the road in: the Geneva division and the domino theory, then the resolution that supplied the war's legal basis. Section C gives the buildup in figures. Section D is the turn, the Tet Offensive and what it did to American belief. Section E follows the exit that widened the war even as it shrank the American part of it. Section F gives the settlement and the ending of April 1975. Section G counts the costs and records what Congress took back. Tell students the summary table at the end of their guided notes, The Ledger at a Glance, asks them to rebuild exactly this map.")

# 4 A DIVIDER
divider_text('Section A', 'The Road In: Division and the Dominoes',
             'A country divided at Geneva, and the theory that made the division permanent.',
             "Set the starting point precisely. Vietnam enters this unit as a French colonial war that France lost. At Dien Bien Phu in May 1954 French forces surrendered to Ho Chi Minh's Viet Minh, and the Geneva settlement that summer drew a line at the seventeenth parallel: Communist north, and a south under Ngo Dinh Diem backed by the United States. The settlement expected the line to be temporary, with elections in 1956 to reunify the country. This section asks students to hold two facts together: the division was meant to be brief, and the refusal of those elections, backed by Washington, made it the foundation of a twenty year commitment. Everything later in the lesson is built on that foundation. The guided notes open with the same two facts, so students should date the division and the refusal separately in section A and keep both dates, 1954 and 1956, visible in their notes all hour, because the test of the whole lesson is how a two year arrangement became a twenty year war.")

# 5 A CONTENT
content_text('Elections promised, elections refused',
             ['Dien Bien Phu, May 1954: France surrenders',
              'Geneva divides Vietnam at the 17th parallel',
              'Reunification elections set for 1956, never held',
              'Diem refuses, expecting Ho to win',
              'The Viet Cong open an insurgency in the south'],
             "Washington's stated reason for refusing the elections was the domino theory, and students should learn it as a theory with a prediction inside it. If South Vietnam fell, the prediction ran, its neighbors would fall after it in sequence, the way a row of dominoes falls. A prediction can be tested, and the end of this lesson tests it. Note also who opened fire first in the south: the Viet Cong, supplied and directed from the north, began an insurgency against Diem's government, which gave Washington a war to answer as well as a line to hold. Both halves belong in section A of the notes: the division with its dates, and the refusal with its stated reason. The reading's first question returns to exactly these facts, so have them written carefully.",
             kick='A · The road in')

# 6 B DIVIDER
divider_photo('lbj-port.jpg', 'Section B', 'The Gulf of Tonkin Resolution',
              ['President Johnson in the Fish Room,', 'the night of August 4, 1964.'],
              "The photograph shows President Johnson in the Fish Room of the White House on the night of August 4, 1964, photographed by Cecil Stoughton of the Johnson Library, as he prepared to announce air strikes and ask Congress for authority after the reported second attack in the Gulf of Tonkin. Teach the night honestly. The August 2 attack on the destroyer Maddox was real. The second attack, reported on August 4 in bad weather on the basis of radar and sonar contacts, almost certainly never happened, which is how the record is now understood on the signals evidence. The administration acted on the reports it had, and Congress acted within days. Section B then does the lesson's central piece of work: it shows students that the resolution Congress passed had been planned months before that night.",
              title_size=38)

# 7 B CONTENT
content_text('The plan came before the crisis',
             ['May 25, 1964: Bundy sends a draft memorandum',
              'Ten steps toward wider war, in order',
              'A congressional resolution stands eighth',
              'An initial strike against the north stands tenth',
              'The stated aim carries a stated limit'],
             "McGeorge Bundy was the president's national security adviser, and his draft memorandum of May 25, 1964 summarized the thinking of the secretaries of state and defense. Read its structure aloud, because the structure is the evidence. The steps run from communications with Hanoi through allied consultations and large deployments to a congressional resolution at step eight and an initial strike at step ten. Note the timing rule inside step eight: no resolution until civil rights legislation cleared the Senate calendar. Note also the limit stated in step two: Communism shall not take over Southeast Asia, and the United States did not intend the destruction of the Hanoi regime. The plan was graduated on paper. The activity works this memorandum as Station 2, beside the resolution it produced.",
             kick='B · The Tonkin Resolution')

# 8 B CONTENT 2
content_text('Authority without a declaration',
             ['August 2: the Maddox is attacked',
              'August 4: a second attack reported, almost certainly never happened',
              'August 7: Congress passes the resolution',
              'All necessary measures, as the president determines',
              'It expires when the president says the area is secure'],
             "In the guided notes definition, the Gulf of Tonkin Resolution is the resolution Congress passed in August 1964 giving the president authority to take all necessary measures to repel attacks on American forces and prevent further aggression in Southeast Asia. Teach the definition whole, then add the vote and the expiry clause, because both are tested. The House voted unanimously and two senators dissented. The resolution carried no list of permitted actions and no date. It expired when the president determined the area's peace and security were reasonably assured, or when Congress ended it, which Congress finally did in 1971. Johnson had privately told Bundy that May that getting out would prove far harder than getting in. The authority he asked for and received had no exit built into it.",
             kick='B · The Tonkin Resolution', size=24)

# 9 C DIVIDER
divider_text('Section C', 'Escalation',
             'Bombing from March 1965, and a force that grew by steps past half a million.',
             "Escalation is the section where the lesson's figures do the arguing, so teach the figures as a sequence and have students write each one down. Sixteen thousand advisers at the end of 1963. More than 184,000 troops by the end of 1965, the year Rolling Thunder bombing began and the first ground combat troops came ashore at Da Nang. More than half a million by 1968. No single announcement ever presented the country with the whole number at once. Each increase was defended as the amount the situation required, and each increase raised the cost of admitting the step before it had failed. That ratchet, step by step enlargement that makes retreat harder than advance, is what the vocabulary word names, and section C of the notes is built to hold it.")

# 10 C CONTENT
content_text('A war measured in body counts',
             ['Rolling Thunder bombing begins, March 1965',
              'First ground combat troops ashore at Da Nang',
              'Search and destroy sweeps through villages',
              'Progress measured by body counts',
              'The draft falls hardest on the poor and the young'],
             "In the guided notes definition, escalation is the steady enlargement of a military commitment step by step, as the American ground force in Vietnam grew from advisers to more than half a million troops. Now fill in how the enlarged war was fought and measured. American units swept villages in search and destroy operations, looking for an enemy who chose when to fight and when to disappear. Commanders, needing a number that showed progress in a war without a front line, reported body counts, the numbers of enemy dead. Students should see the weakness inside the measure without being told it is a weakness: a rising count could describe a winning war or a widening one, and the number could not tell the difference. The draft supplied the manpower, and its calls fell hardest on men without college deferments or influence with local boards.",
             kick='C · Escalation')

# 11 C STAT
stat('543,400', 'peak American troop strength in Vietnam, reached in April 1969',
     'At the end of 1963 the American presence had been about sixteen thousand advisers',
     "Let the two numbers stand next to each other before saying anything else. About sixteen thousand advisers at the end of 1963, and a peak of 543,400 American troops in April 1969. Between those numbers there was never a declaration of war and never a single vote on a force of that size. There was a resolution written in the language of repelling attacks, and a sequence of increases, each presented as limited, each building on the one before. Ask students to name the vocabulary word for growth of exactly this kind, and have them check their section C notes for the definition. Then make the connection to the Bundy memorandum explicit: the graduated sequence the planners drew in May 1964 is what a force curve like this looks like when it is drawn year by year instead of step by step.",
     kick='C · Escalation')

# 12 C PHOTO
content_photo('danang-port.jpg', 'The men the figures describe',
              ['A Marine private waits on the beach at Da Nang',
               'National Archives record 532432',
               'Most draftees were teenagers or in their early twenties',
               'A tour ran twelve months in the Army, thirteen in the Marines',
               'Units rotated men home one by one, not together'],
              "The photograph, National Archives record 532432, shows a young Marine private waiting on the beach during the Marine landing at Da Nang. Use it to return the section's numbers to the people inside them. The force that passed half a million was not a professional expeditionary army. Much of it was drafted, and the average age was far below the average of the Second World War's forces. The rotation system sent each man home on his own date, which meant units were always losing their most experienced men one at a time. None of this is decoration for the figures. It is the reason the draft's fairness became a national argument by 1969, and it prepares students for the lottery record they meet at Station 5 of the activity and again in section E.",
              kick='C · Escalation')

# 13 D DIVIDER
divider_photo('tet-port.jpg', 'Section D', 'The Tet Offensive',
              ['A deserted street in Saigon', 'during the Tet fighting, 1968.'],
              "The photograph shows a deserted street in Saigon during the Tet fighting, photographed by SP5 James Newlin of the United States Army on February 1, 1968, National Archives record 111-CCV-529-CC45843. A street in a capital city, emptied in the middle of a war the public had been told was being won: that is the right image for this section, and it needs no combat in it to make its point. Section D holds two results at once and refuses to choose between them. On the ground, the offensive was a heavy defeat for the forces that launched it. At home, it broke the public's belief in official claims of progress and ended a presidency. Students often want to keep only one of those results. The notes and the quick check both require both.",
              title_size=38)

# 14 D CONTENT
content_text('Attacks everywhere at once',
             ['January 30 and 31, 1968, during the Tet holiday',
              'More than one hundred cities and towns struck',
              'The American embassy grounds in Saigon breached',
              'Hue held by the attackers for about twenty five days',
              'Attacker losses heavy; the Viet Cong never fully recovered'],
             "In the guided notes definition, the Tet Offensive is the coordinated attacks by North Vietnamese and Viet Cong forces across South Vietnam in January 1968, a military defeat for the attackers that shook American confidence in official claims of progress. Walk the geography slowly. The attacks were coordinated to the hour across the whole country, which is what made them news: not one battle but a hundred, including the grounds of the American embassy in the capital. Then give the military result its full weight, because the lesson's honesty depends on it. American and South Vietnamese forces retook every position. Attacker losses were very heavy, and the Viet Cong, who had carried much of the fighting, never regained their former strength as an independent force.",
             kick='D · The Tet Offensive', size=24)

# 15 D CONTENT 2
content_text('The defeat that ran the other way',
             ['Officials had described the enemy as weakening',
              'Television showed an enemy attacking everywhere',
              'Johnson limits the bombing, March 31, 1968',
              'Johnson announces he will not seek reelection',
              'Kennedy, 1967: candor, not easy answers'],
             "The last fragment reaches back four months before Tet. Senator Robert Kennedy, writing to Professor John Bayliss in September 1967, argued that the American people had a right to expect not easy answers but candid evaluation of the war. After Tet, that argument described the country's mood. The administration had spent the autumn of 1967 presenting progress, and the offensive refuted the presentation in public, whatever the battlefield result. Johnson's two decisions of March 31, limiting the bombing and leaving the election, were the political price. Use this slide to set up the writing task's seventh bank item, the Kennedy letter, which is quoted only at the short length the audited record carries it. Students should understand why a two sentence fragment can still be evidence: it dates the credibility problem before the offensive exposed it.",
             kick='D · The Tet Offensive', size=24)

# 16 E DIVIDER
divider_text('Section E', 'Vietnamization and the Wider War',
             'American troops coming home, the war widening past Vietnam\'s borders, and a draft run by lottery.',
             "Richard Nixon won the presidency in 1968 with the war as the central fact of American politics, and he chose a slower exit rather than a fast one. Section E follows his policy in its three parts, and students should keep the parts separate in their notes because they point in different directions. The American ground force shrank year by year under Vietnamization. The air war and the ground war widened into Cambodia and Laos. And the draft, the war's most resented institution at home, was rebuilt as a lottery in December 1969. A section that contains withdrawal and widening at the same time is the honest shape of these years, and the summary table at the end of the guided notes gives this stretch its own row for that reason.")

# 17 E PHOTO
content_photo('nixon-port.jpg', 'Vietnamizing the search for peace',
              ['Nixon address, November 3, 1969',
              'The threatened people supply the manpower',
              'Training and equipment for South Vietnam increased',
              'American troops enable, then hand over',
              'The aim stated in 1964 does not change'],
              "The portrait is President Nixon's official presidential portrait of July 8, 1971, held by the National Archives. In the guided notes definition, Vietnamization is President Nixon's policy of withdrawing American troops while building up South Vietnam's forces to carry the fighting themselves. Teach the November 3, 1969 address from its own sentences, which the activity quotes at Station 4. The defense of freedom, Nixon argued, is particularly the responsibility of the people whose freedom is threatened. Under the plan he ordered a substantial increase in the training and equipment of South Vietnamese forces, and the primary mission of American troops became enabling those forces to assume full responsibility. Then name what did not change: the aim was still an independent non-Communist South Vietnam, the aim Bundy had written in 1964. Vietnamization changed who carried the fighting. It did not change what the fighting was for.",
              kick='E · Vietnamization')

# 18 E PHOTO 2
content_photo('lottery-port.jpg', 'Chance, televised',
              ['Cambodia operation announced, April 1970',
              'Four students killed at Kent State, May 4',
              'December 1, 1969: the first draft lottery',
              '366 birth dates drawn in order',
              'First date drawn: September 14, number 1'],
              "The photograph shows Representative Alexander Pirnie drawing the first capsule of the first draft lottery at Selective Service headquarters on December 1, 1969, in a photograph credited to the Selective Service System. In the guided notes definition, the draft lottery is the system begun in 1969 that chose the order in which young men were called for the draft by a random drawing of birth dates. President Nixon's proclamation gave the reason in one word's worth of argument: random selection would provide the most equitable basis for selection. One drawing fixed the standing of every man born from 1944 through 1950. September 14 stood first, and the men born on that date knew that night they would almost certainly be called. Put the lottery beside Kent State in the notes: both belong to a home front living inside the war's costs.",
              kick='E · The wider war at home')

# 19 F DIVIDER
divider_text('Section F', 'The Accords and the Fall of Saigon',
             'A ceasefire that left the central question open, and the ending of April 30, 1975.',
             "The Paris talks ran beside the fighting for years, through the widening into Cambodia, the mining of Haiphong harbor, and the bombing of December 1972. Section F covers the settlement those talks produced and then the ending the settlement did not prevent. Teach the two halves as cause and consequence. The Paris Peace Accords of January 1973 were a real agreement with real terms, and students should be able to list them. The terms also left North Vietnamese troops in place inside South Vietnam and left the political question untouched. Two years later that question was answered by an offensive. Students who can explain why a signed peace and a fallen capital belong in the same section have understood the section.")

# 20 F CONTENT
content_text('What Paris settled, and what it left',
             ['Paris Peace Accords, January 1973',
              'Ceasefire; American prisoners freed',
              'Last American combat troops leave in March',
              'North Vietnamese troops stay in the south',
              'Who governs South Vietnam left to Vietnamese arms'],
             "List the terms as a ledger, because the section's argument lives in the list's shape. Settled at Paris: a ceasefire in place, the release of American prisoners, and the withdrawal of the last American combat troops, completed in March 1973. Not settled at Paris: the presence of North Vietnamese forces inside South Vietnam, who stayed where they stood, and the question the war had been fought over since 1954, who would govern the south. Congress also cut the legal ground from under any return: the Tonkin Resolution had been repealed in 1971, and bombing in Cambodia was halted by law in 1973. When the final offensive came in 1975, the United States watched it happen. Students should write both columns of this ledger in section F of the notes, settled and left open, in those words. Have them copy both columns before moving on, since the fall of Saigon two slides from now is unintelligible without the left open column written beside the settled one.",
             kick='F · The accords and the fall')

# 21 F PHOTO
content_photo('refugees-port.jpg', 'April 30, 1975',
              ['North Vietnamese offensive, spring 1975',
              'South Vietnamese units fall back, then collapse',
              'Helicopters lift out the last embassy staff',
              'Tanks enter Saigon, April 30, 1975',
              'Vietnam reunified under Hanoi'],
              "Return to the title photograph and name it exactly: boatloads of Vietnamese refugees approaching the United States fleet on April 30, 1975, United States Navy photograph K108971 by PH3 Harold Brown. The famous rooftop helicopter photograph of the evacuation is a press photograph and is not public domain, so this lesson documents the day with the Navy's own record instead, and students should hear that choice stated plainly. On the last day, helicopters lifted the last embassy staff and thousands of Vietnamese out of Saigon while North Vietnamese tanks entered the city. The government the United States had backed since 1954 ceased to exist. The war that began with a temporary division ended with reunification under the government in Hanoi, the outcome the commitment had been built to prevent.",
              kick='F · The accords and the fall')

# 22 F STAT
stat('58,000+', 'American dead in the Vietnam War',
     'Vietnamese dead, soldiers and civilians on all sides, numbered in the millions',
     "Speak this figure slowly and completely, the way the reading states it. More than 58,000 Americans died in the war, across the years from the advisers of the early 1960s to the last troops of 1973. Beside it, the second figure must be spoken with it: Vietnamese dead, soldiers and civilians on all sides, numbered in the millions, and the bombing and fighting left deep damage across Vietnam, Laos, and Cambodia. Students sometimes treat the American figure as the war's whole cost because it is the figure with a memorial wall in Washington. The lesson's ledger counts both. Have the two figures written in section G of the notes as a pair, because the guided notes summary and the unit test both draw on them together.",
     kick='F · The accords and the fall')

# 23 G DIVIDER
divider_text('Section G', 'The Costs and the Reckoning',
             'Inflation, a broken presidency, distrust that outlasted the war, and a war power taken back.',
             "Close the narrative with the reckoning at home, because the unit question asks how the Cold War reshaped American life and Vietnam reshaped it directly. The war's spending fed inflation through the late 1960s. It broke Lyndon Johnson's presidency, consuming the domestic program he had wanted as his legacy along with his standing. It left a distrust of official statements, the credibility gap named in these years, that outlasted the fighting and shadowed every later war debate. And it moved Congress to reclaim authority it had handed over in 1964: the Tonkin Resolution repealed in 1971, and the War Powers Resolution passed over a veto in 1973. Section G is short in the reading and should be taught at full weight. It is where the lesson's two halves, the strategy abroad and the country at home, are added together.")

# 24 G CONTENT
content_text('What the strategy cost the strategists',
             ['The dominoes did not fall in sequence',
              'Laos and Cambodia fell; Thailand and Malaysia did not',
              'Congress repeals the Tonkin Resolution, 1971',
              'War Powers Resolution passed, 1973',
              'Veterans came home to a country that wanted to forget'],
             "End the evidence with the prediction the war began with, because the lesson question asks for judgment on the war's own terms. Laos and Cambodia did fall to Communist governments in 1975, and honesty requires saying so. Thailand, Malaysia, Singapore, and Indonesia did not, and the sequence of falling dominoes across Southeast Asia and beyond, which the theory had predicted and the commitment had been built to stop, did not happen. The theory's defenders answer that the war bought those countries time, and students will meet that argument in the writing task's grading, where it can earn credit when argued from the record. Close the section with the veterans, whose return the reading names last on purpose: men and women who had served as ordered, in a war their country had decided to forget, carrying claims the country was slow to honor.",
             kick='G · Costs and reckoning', size=24)

# 25 LEDGER GLANCE
s = slide(NAVY)
kicker(s, 'The ledger at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Each step, and what it added', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The road in', 'A divided country held as a line', 'A refusal in 1956 makes the line permanent'),
        ('The authority', 'A resolution with no list and no date', 'Granted on a second attack that almost certainly never happened'),
        ('The buildup', 'Advisers to a peak of 543,400', 'Measured in body counts, manned by a draft'),
        ('The turn and exit', 'Tet, Vietnamization, Paris, Saigon', 'The aim survives every policy; the country does not')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the summary table at the end of the guided notes, The Ledger at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. Read the rows as a single account rather than four summaries. The road in supplied the commitment. The authority supplied the legal means, granted in a week in August 1964 on reports whose central claim did not hold. The buildup supplied the scale, half a million troops and a draft to man them. The turn and the exit supplied the ending, in which the stated aim outlived every policy built to serve it and the country the aim described ceased to exist. Grade the table generously on wording and strictly on completeness: every row needs its commitment, its reason, and its cost.")

# 26 VOCAB A
vocab('Words for the road in',
      [('domino theory', 'if one country fell, its neighbors would fall after it'),
       ('Viet Cong', 'the guerrilla forces fighting in the south'),
       ('Gulf of Tonkin Resolution', 'the August 1964 grant of authority'),
       ('escalation', 'growth of a commitment step by step')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. domino theory: the belief, stated publicly by President Eisenhower in 1954, that if one country fell to communism its neighbors would fall one after another like a row of dominoes. Viet Cong: the Communist guerrilla forces and political organization in South Vietnam, supplied and directed from North Vietnam, that fought the South Vietnamese government and its American allies. Gulf of Tonkin Resolution: the resolution Congress passed in August 1964 giving the president authority to take all necessary measures to repel attacks on American forces and prevent further aggression in Southeast Asia. escalation: the steady enlargement of a military commitment step by step, as the American ground force in Vietnam grew from advisers to more than half a million troops.")

# 27 VOCAB B
vocab('Words for the turn and the exit',
      [('Tet Offensive', 'the January 1968 attacks across South Vietnam'),
       ('Vietnamization', 'withdrawal while Saigon\'s forces take over'),
       ('draft lottery', 'call order set by a drawing of birth dates')],
      "Three more terms, again matching the guided notes exactly. Tet Offensive: the coordinated attacks by North Vietnamese and Viet Cong forces across South Vietnam in January 1968, a military defeat for the attackers that shook American confidence in official claims of progress. Vietnamization: President Nixon's policy of withdrawing American troops while building up South Vietnam's forces to carry the fighting themselves. draft lottery: the system begun in 1969 that chose the order in which young men were called for the draft by a random drawing of birth dates. Note the order of this set. The first term names the moment belief broke, the second names the policy built to manage the breaking, and the third names the system that decided, in one televised evening, which young men would still be sent while the policy ran its course.")

# 28 SYNTHESIS
content_text('Judging the war on its own terms',
             ['The aim: a standing South Vietnam, neighbors held',
              'The sequence: division, resolution, buildup, turn, exit',
              'The ending: Saigon falls, the sequence of falls does not follow',
              'The writing task asks for a weighing, not a narration'],
             "Close the teaching here, before the work slide, and model the judgment the writing task will ask for. The war's own terms were stated early and stated plainly: hold South Vietnam, and by holding it keep the dominoes standing. Against those terms the record is not ambiguous in its outcome, however argued its causes remain. South Vietnam fell on April 30, 1975. Its neighbors did not fall in the predicted sequence. Between the aim and the ending stands a sequence of decisions, each documented in this lesson, and the strongest student writing will assign weight along that sequence rather than placing the whole explanation on one year or one president. Tell students the counterarguments are known and creditable: the attackers' losses at Tet, the time bought argument for Southeast Asia, and Johnson's private doubts all belong in an honest essay.",
             kick='Synthesis')

# 29 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did containment lead the United States into Vietnam, and why did the war fail on its own terms? Build the ledger first, then judge from it.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Escalation Ledger: five records, a ledger, and a verdict on the step where better terms remained'),
        ('Notebook', 'Notebook page: the five steps charted, and the war in one paragraph'),
        ('Quick check', 'The First Capsule: the lottery photograph, the resolution, the figures, Tet and Vietnamization'),
        ('Writing', 'Why Did the War Fail on Its Own Terms? The sequence weighed against the aim, from the bank')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the Bundy memorandum and the resolution, the escalation figures in full, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Escalation Ledger, runs five stations through the records: the Tonkin Resolution quoted from the audited bank record, the Bundy memorandum quoted from the Foreign Relations text, a labeled summary of the Tet Offensive built from the Army record, Nixon's Vietnamization address quoted from the Public Papers text, and the draft lottery proclamation with the drawing record of December 1, 1969. Students build the ledger in Part 2 and defend a verdict on the step at which the war could still have ended on better terms. The notebook page charts the same five steps. The quick check, The First Capsule, works from the lottery photograph. The writing task turns the lesson question into an essay weighed from both halves of the bank. The exit ticket has three parts: the memorandum's place in the resolution's story, the escalation figures in full, and the lesson question answered with one buildup fact and one ending fact.")

dc.save(OUT)
