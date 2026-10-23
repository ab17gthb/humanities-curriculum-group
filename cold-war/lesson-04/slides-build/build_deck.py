#!/usr/bin/env python3
"""Cold War Lesson 4 deck, "Brinkmanship and the Nuclear Shadow,"
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

# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'THE COLD WAR · LESSON 4', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Brinkmanship and the Nuclear Shadow', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Megaton weapons, threats at the edge, and a warning from inside', size=17, color=POWDER)
notes(s, "The photograph shows the Castle Bravo thermonuclear test at Bikini Atoll on March 1, 1954, a United States Department of Energy photograph. Its yield is estimated at 15 megatons, far more than its designers predicted, and that gap between prediction and result is a fair emblem for the whole lesson. Between 1952 and 1961 the United States and the Soviet Union built weapons hundreds of times more powerful than the bombs of 1945, wrote a doctrine that threatened to use them in answer to far smaller attacks, taught schoolchildren to duck under desks, removed two elected governments in secret, faced each other in two armed alliances, and raced into space. The lesson follows that order. At every stage students will ask what new power or fear appeared, and what it cost or risked, because the activity file is built on exactly those two questions.")

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did nuclear weapons change the rules of the rivalry, and how close did brinkmanship bring the world to war?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the struggle between the United States and the Soviet Union reshape the world and American life, and why did it end the way it did?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "The question has two halves and students should hear both. The first asks how the rules changed once both sides held weapons that could destroy the other's society. Open war between the superpowers became the one outcome policy had to avoid, so the rivalry moved into threats, alliances, secret operations, and contests in other people's countries. The second half asks about distance. How close did the practice of pushing confrontations to the edge bring the world to a war neither side wanted? That distance cannot be measured exactly, and students should be told so plainly. What the record gives is the machinery that kept confrontations at the edge and the moments, a test that ran beyond prediction among them, when control proved thinner than the plans assumed. The unit question runs beneath the lesson as its frame, and the home front sections answer its American life half directly.")

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Seven steps into the shadow', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'An arsenal that could end societies', 'Kiloton bombs give way to megaton weapons'),
        ('B', 'Massive retaliation and brinkmanship', 'A full nuclear strike threatened at the edge'),
        ('C', 'The shadow at home', 'Duck and cover, drills, and fallout shelters'),
        ('D', 'Covert action: Iran and Guatemala', 'The secret weapon, used twice in two years'),
        ('E', 'Two alliances and the wider contest', 'Warsaw Pact, and new nations courted and armed'),
        ('F', 'Sputnik and the space race', 'A beeping sphere and a national shock'),
        ('G', 'The warning from inside', 'Eisenhower names the military-industrial complex')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This slide is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A covers the hydrogen bomb and the new scale of the arsenal. Section B takes up the doctrine built on that arsenal, massive retaliation and brinkmanship. Section C moves home, to drills, shelters, and a film for schoolchildren. Section D covers covert action in Iran and Guatemala. Section E widens the frame to the Warsaw Pact and the contest for newly independent nations. Section F is the Sputnik shock of 1957. Section G closes with Eisenhower's farewell warning of 1961. Tell students the summary table at the end of their guided notes, The Nuclear Shadow at a Glance, asks them to rebuild this map in their own words, stage by stage, with a cost or risk attached to every stage.")

# 4 SECTION A DIVIDER
divider_text('Section A', 'An Arsenal That Could End Societies',
             'The bombs of 1945 were measured in kilotons. The new weapons were measured in megatons.',
             "Start with units, because the whole lesson turns on a change of scale that students can easily slide past. A kiloton is a thousand tons of TNT. A megaton is a million tons. The atomic bombs that destroyed Hiroshima and Nagasaki in 1945 were kiloton weapons. The hydrogen weapons tested from 1952 onward were megaton weapons, hundreds of times more powerful, and they worked by fusion, joining atoms, rather than by the fission, splitting atoms, of the first bombs. Students do not need the physics beyond that distinction. What they need is the strategic consequence. A weapon that can erase a city in one strike, delivered first by bombers and then by missiles that cross oceans in minutes, changes what war between its owners can mean. By the middle of the decade each side held the power to destroy the other's society in an afternoon. Every doctrine and fear in this lesson is an answer to that single fact.")

# 5 ARSENAL
content_text('From kilotons to megatons in nine years',
             ['Ivy Mike, November 1952: estimated 10.4 megatons',
              'The island of Elugelab is erased at Enewetak Atoll',
              'The Soviet Union answers with a thermonuclear test, August 1953',
              'Castle Bravo, March 1954: estimated 15 megatons',
              'Bombers first, then missiles built to cross oceans'],
             "Walk the three tests as a sequence and insist on the word estimated every time a yield is stated. Ivy Mike, in November 1952, was a device rather than a deliverable weapon, a building sized machine, and it still released an estimated 10.4 megatons and erased the island it stood on. The Soviet test of August 1953 ended any hope that the new weapon would stay an American monopoly; it arrived in under a year. Castle Bravo, in March 1954, is the test students should remember for a second reason. Its estimated 15 megatons ran far beyond what its designers predicted, and its fallout spread beyond the test area over inhabited islands and a Japanese fishing boat. The men running the program could build the weapon and still misjudge it. Hold that fact in reserve, because it returns when students judge whether the threats built on these weapons were ever fully under anyone's control.",
             kick='A · The arsenal', size=23)

# 6 STAT IVY MIKE
stat('10.4 megatons', 'estimated yield of Ivy Mike, the first hydrogen bomb test',
     'November 1952 · Hundreds of times the power of the bombs of 1945, stated as the estimate the record supports',
     "Let the figure sit on the wall before explaining it. Ten point four megatons is ten million, four hundred thousand tons of TNT in a single device, against the kiloton scale, thousands of tons, of the 1945 bombs. Students should repeat the figure as an estimate, because yields of atmospheric tests were reconstructed from instruments and sampling after the fact, and the record states them as estimates. The comparison is the teaching point, and it should be made carefully. Hundreds of times more powerful does not mean hundreds of times the same kind of war. It means a different category of event, in which one aircraft or one missile can do what whole fleets of bombers did in the Second World War. That is why the strategists of the 1950s spoke of destroying societies rather than defeating armies. The next section shows the doctrine they built to keep such weapons from ever being used, by threatening to use them.",
     kick='A · The arsenal')

# 7 SECTION B DIVIDER
divider_text('Section B', 'Massive Retaliation and Brinkmanship',
             'Security promised at a bearable cost, paid for with a threat held at the edge of war.',
             "Section B is the lesson's doctrinal center, and it belongs to one administration and one spokesman. President Eisenhower came to office in 1953 determined to hold defense spending at a level the economy could sustain for a long contest. His Secretary of State, John Foster Dulles, turned that determination into a declared policy in January 1954. The bargain at its heart should be stated plainly for students. Conventional armies large enough to meet every Communist advance at its own location would cost more than the country could bear indefinitely. Nuclear threats were, by comparison, cheap. A great capacity to retaliate, held ready, might deter advances everywhere at once. Whether that bargain was prudent statecraft or a bluff with civilization as the stake is the question the writing task will put to students, so teach the doctrine in its strongest form here, in Dulles's own words, before anyone judges it.")

# 8 MASSIVE RETALIATION
content_text('A great capacity to retaliate, instantly',
             ['Dulles announces the doctrine, January 1954',
              'Local defenses reinforced by massive retaliatory power',
              'Retaliate instantly, by means and at places of our choosing',
              'A maximum deterrent at a bearable cost',
              'An attack answered with a threat of a full nuclear strike'],
             "Quote Dulles directly, because the activity file tests students on his phrases. Local defenses, he said, must be reinforced by the further deterrent of massive retaliatory power. The basic decision was to depend primarily upon a great capacity to retaliate, instantly, by means and at places of our choosing. Unpack the choosing, because it is the doctrine's novelty. Under the older practice, aggression was met where it happened, with matching force, as in Korea. Under massive retaliation, the United States reserved the right to answer a local advance somewhere else, with far greater force, up to a full nuclear strike. That reservation was meant to make any advance too dangerous to attempt. Note also what Dulles did not say in the address. He never named nuclear weapons, though no listener doubted the means he meant. The economy of the policy is its other half, maximum deterrent at a bearable cost, and students should write both halves into section B of their notes.",
             kick='B · Massive retaliation', size=23)

# 9 BRINKMANSHIP
content_text('Walking to the edge on purpose',
             ['Brinkmanship: pushing a confrontation to the edge of war',
              'The other side must believe the threat might be carried out',
              'Carrying it out would mean catastrophe for both sides',
              'The doctrine saves money on conventional forces',
              'Its danger: error, misreading, or pride at the edge'],
             "Define the term from the vocabulary list and then slow down on its logic. Brinkmanship is the practice of pushing a dangerous confrontation to the edge of war in order to force the other side to back down. For the push to work, the other side has to believe the threat behind it is real, which means the side making the threat has to accept a genuine risk of the catastrophe it is threatening. That is the paradox students must hold. The safer the threat maker tries to be, the less the threat deters. The more convincing the threat, the closer the confrontation runs to a war neither side wants. Add the human factors the reading names, error and pride, and the machinery of the period, bombers on alert and, soon, missiles that shortened decision time to minutes. Ask the class to keep one question open through the rest of the lesson: who, in this system, is actually in control at the edge?",
             kick='B · Brinkmanship', size=23)

# 10 SECTION C DIVIDER
divider_photo('duck-port.jpg', 'Section C', 'The Shadow at Home',
              ['A frame from Duck and Cover,', 'the Federal Civil Defense film of 1951.'],
              "The image is a frame from Duck and Cover, the Federal Civil Defense Administration film of 1951, showing its animated teacher, Bert the Turtle. Section C brings the arsenal home. The same government that was building megaton weapons also had to tell its citizens, including its youngest citizens, what to do if those weapons were used against them. Its answer was civil defense, drills in schools, shelters in backyards, and a nine minute film with a cheerful song, made for children. Teach this section with respect for both sides of the record. The advice in the film was not worthless. Dropping and covering genuinely protects against flying glass and debris at a distance from a blast. But the film was made in 1951, in the atomic age's terms, and the weapons grew past its promises within three years. Students should leave this section able to hold the routine and its limits in one thought.",
              title_size=40)

# 11 HOME FRONT
content_text('Duck, cover, and practice for the end of the world',
             ['The film teaches: see the flash, duck and cover',
              'Cover the back of your neck and your face',
              'Under a desk, against a wall, fast, wherever you are',
              'Schools run drills; families build fallout shelters',
              'A desk protects against glass, not against a hydrogen bomb'],
             "Run the film's own sequence so students hear how it teaches. First the flash, brighter than the sun. Then duck, then cover, tightly, the back of the neck and the face, under a desk or anything close by, and do it fast, because the bomb might come without warning. The narrator compares the flash to a sunburn, which tells students how the film scales the danger down to a size a child can act on. Then set the routine beside Station 1 of the activity file. At a distance from a kiloton blast, the drill saves eyes, skin, and lives. Near a megaton weapon, the building itself is inside the destruction the drill imagines sheltering from. Historians treat the film as evidence of a government trying to make an unmanageable danger feel manageable, and of a generation that practiced for the end of the world between ordinary lessons.",
             kick='C · The shadow at home', size=23)

# 12 SECTION D DIVIDER
divider_text('Section D', 'Covert Action: Iran and Guatemala',
             'Where threats were too dangerous and war too costly, a quieter weapon was used twice in two years.',
             "This divider carries no photograph, and students can be told why. The operations in this section were secret, and the photographic record that survives in public archives with a clear public domain status does not cover them the way it covers the tests. Section D covers covert action, the middle weapon of the Eisenhower years. Massive retaliation threatened too much for small contests, and another Korea cost too much in money and lives. A secret operation promised a third option, influence abroad with the sponsor's hand hidden, run chiefly by the Central Intelligence Agency, founded in 1947 and seasoned by 1953. Two operations in thirteen months, in Iran and then in Guatemala, were counted in Washington as clean successes. The section's work is to follow both operations past their first reports, to 1979 in one case and to decades of civil war in the other, and to ask what the full record does to the word cheap.")

# 13 COVERT ACTION
content_text('Two elected governments, removed in secret',
             ['Iran, August 1953: Mossadegh overthrown, the Shah restored',
              'His offense in Western eyes: nationalizing British controlled oil',
              'Guatemala, June 1954: Arbenz overthrown by a CIA backed force',
              'His land reform had taken land from the United Fruit Company',
              'The long record: revolution in 1979, civil war in Guatemala'],
             "Teach the two operations as a pattern, not a pair of anecdotes. In Iran, Prime Minister Mohammad Mossadegh had nationalized the oil industry that a British company controlled, and in August 1953 a covert operation helped drive him from power and restore the Shah to full authority. In Guatemala, President Jacobo Arbenz had taken uncultivated land from the United Fruit Company for redistribution, and in June 1954 a small CIA backed force and a campaign of pressure forced him out. Both governments were elected. Both operations were fast and cost the United States little at the time. Then require the second half of the record. The Shah's rule hardened, and in 1979 a revolution overthrew him and made Iran an adversary. Guatemala entered decades of civil war and military rule. Covert action hid the sponsor's hand in the moment. It could not hide the consequences, and students should write both halves into section D.",
             kick='D · Covert action', size=22)

# 14 SECTION E DIVIDER
divider_photo('warsaw-port.jpg', 'Section E', 'Two Alliances and the Wider Contest',
              ['The Warsaw conference at which the', 'Warsaw Pact was signed, May 1955.'],
              "The photograph shows the conference in Warsaw in May 1955 at which the Warsaw Pact was signed, joining the Soviet Union and the Communist states of Eastern Europe in a military alliance. Section E widens the lesson's map. Until now the rivalry has been a matter of weapons, doctrines, drills, and secret operations, most of them American decisions. Here it becomes a structure, two alliance systems armed against each other in Europe, and a competition that reaches into the newly independent nations of Asia and Africa. The trigger for the Pact belongs in the record. West Germany had just been admitted to NATO and allowed to rearm, ten years after the war, and Moscow answered with an alliance of its own. Students should notice the symmetry and its limit. NATO and the Warsaw Pact looked alike on an organization chart. The consent behind them was not the same on both sides of the line.",
              title_size=36)

# 15 ALLIANCES
content_text('Alliance against alliance, and a world courted',
             ['Warsaw Pact formed in May 1955, in answer to NATO',
              'West Germany inside NATO is the immediate trigger',
              'Two armed alliances face each other across Europe',
              'New nations emerge as the European empires collapse',
              'Both superpowers court and arm them, and locals pay'],
             "Set the European structure first. By 1955 the division of Europe that the Second World War left had hardened into two systems, NATO in the west, formed in 1949, and the Warsaw Pact in the east, each pledged to defend its members and each backed by nuclear weapons. A local crisis in Europe therefore carried an alliance risk from its first hour, which is one reason the superpowers so often fought their contests elsewhere. Then move the map. The collapse of the British, French, Dutch, and Belgian empires produced dozens of new states in Asia and Africa in the two decades after 1945. Both superpowers courted them with aid, arms, and attention, reading local struggles as squares on a global board. The peoples of those states had aims of their own, often local ones, and they paid the price when the rivalry turned their countries into battlegrounds, as the covert operations of section D already showed in smaller form.",
             kick='E · The wider contest', size=22)

# 16 SECTION F DIVIDER
divider_photo('sputnik-port.jpg', 'Section F', 'Sputnik and the Space Race',
              ['Sputnik 1 on exhibit at the National Museum', 'of the United States Air Force.'],
              "The photograph shows Sputnik 1, the first artificial satellite, as it appears on exhibit in the Missile and Space Gallery at the National Museum of the United States Air Force, a United States Air Force photograph. The object itself is unprepossessing, a polished metal sphere a little under two feet across with four antenna rods, and students should be told its size before its story, because the disproportion between the object and its effect is the story. Section F covers October 4, 1957, when the Soviet Union put this sphere into orbit and its simple beeping was heard by radio listeners around the world. No weapon was fired and no territory changed hands. Yet Americans across the political range heard the beeping as an alarm about their schools, their science, and their missiles. The section asks why a beeping sphere could do what a decade of Soviet armies had not, shake American confidence in American leadership of the contest.",
              title_size=40)

# 17 SPUTNIK
content_text('A beeping sphere, heard as an alarm',
             ['Sputnik launched October 4, 1957, the first artificial satellite',
              'It carried no weapon; its rocket was the proof',
              'Americans hear it as evidence the country fell behind',
              'NASA created in 1958; new money for science education',
              'The space race runs on the rockets of the arms race'],
             "Separate the satellite from its meaning, as the activity file requires. The satellite itself weighed about 83.6 kilograms, carried instruments and a transmitter, and beeped until its batteries died. It threatened no one directly. What it proved was the rocket beneath it, a machine of the same kind that could carry a nuclear warhead across an ocean, and it proved that Soviet science and engineering had achieved a first that American programs had promised and not yet delivered. The American response was institutional and fast. Congress created the National Aeronautics and Space Administration in 1958, poured new federal money into science and mathematics education, and pressed the missile program forward. Note the pattern for students. Sputnik widened the contest again, from battlefields and alliances into laboratories, classrooms, and prestige, and it did so without a shot. Fear, in this rivalry, was itself a force that moved budgets and laws.",
             kick='F · Sputnik', size=23)

# 18 STAT SPUTNIK
stat('83.6 kilograms', 'the weight of Sputnik 1, the first artificial satellite',
     'About 58 centimeters across · Launched October 4, 1957 · Its beeps were heard around the world',
     "Use the smallness of the number as the teaching device. Eighty three point six kilograms is roughly the weight of a large man, in a sphere about 58 centimeters across, about the size of a beach ball. Set that beside the megaton figure from section A and ask students to explain how the lighter object produced the larger political shock in the United States. The answer runs through proof and prestige. The hydrogen bomb tests were conducted by both sides in remote atolls, reported in figures the public could file away. Sputnik passed over American cities and farms on a schedule anyone could look up, beeping, visible at dawn and dusk, unmistakably Soviet and unmistakably first. It also stood for the missile that launched it, so the classroom shock and the military shock were the same shock wearing two faces. That is why the response ran from a new space agency to new money for school science in a single year.",
     kick='F · Sputnik')

# 19 SECTION G DIVIDER
divider_photo('eisenhower-port.jpg', 'Section G', 'The Warning from Inside',
              ['President Eisenhower delivering his', 'farewell address, January 17, 1961.'],
              "The photograph shows President Dwight D. Eisenhower delivering his farewell address on January 17, 1961, from the record held by the Eisenhower Library and the National Archives. Section G closes the lesson with a judgment from the man who presided over most of it. Eisenhower had been supreme commander of the Allied armies in Europe in the Second World War. As president he had approved the hydrogen bomb buildup, announced massive retaliation through his Secretary of State, and authorized the covert operations in Iran and Guatemala. Three days before leaving office, on television, he used his last address to warn the country about the permanent machinery those decisions had built. Students should be alert to how unusual that is. Farewell addresses usually claim vindication. This one assigns homework to the republic, and its central phrase, the military-industrial complex, entered the language from this single speech.",
              title_size=40)

# 20 FAREWELL
content_photo('eisenhower-port.jpg', 'Guard against unwarranted influence',
              ['A permanent armaments industry of vast proportions',
               'Joined to an immense military establishment',
               'Its influence felt in every city and office',
               'Guard against unwarranted influence, sought or unsought',
               'Security and liberty must prosper together, he insists'],
              "Read the warning in its own order. Eisenhower begins by granting the necessity: the United States had been compelled to create a permanent armaments industry, because the emergency improvisation of earlier wars would no longer serve. Then he names the new fact, a conjunction of an immense military establishment and a large arms industry, felt in every city, every state house, and every federal office. Then the warning itself, that the nation must guard against the acquisition of unwarranted influence, whether sought or unsought, by the military-industrial complex. Pause on the phrase whether sought or unsought, because it rules out the easy reading. Eisenhower is not accusing generals or contractors of a plot. He is describing a weight built into the system, the potential for the disastrous rise of misplaced power, which an alert and knowledgeable citizenry alone could keep in its proper place beside peaceful goals. That is the note the lesson ends on, a warning from inside the machine.",
              kick='G · The warning from inside')

# 21 GLANCE
s = slide(NAVY)
kicker(s, 'The nuclear shadow at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Four stages, one shadow', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The arsenal', 'Megaton weapons on both sides by 1953', 'Tests that ran beyond prediction'),
        ('The doctrine', 'Massive retaliation, January 1954', 'Confrontations held at the edge'),
        ('Home and secret war', 'Duck and cover; Iran and Guatemala', 'Fear at home; consequences abroad'),
        ('The wider contest', 'Warsaw Pact 1955; Sputnik 1957', 'Eisenhower warns the republic, 1961')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, The Nuclear Shadow at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The rows compress the arc. The arsenal row pairs the megaton scale, reached by both sides by 1953, with the risk carried by Castle Bravo's unpredicted yield. The doctrine row pairs the January 1954 promise of massive retaliation with its method, confrontations held deliberately at the edge of war. The home and secret war row joins the two middle weapons, a film that taught children a routine and operations that removed governments in Iran and Guatemala, with fear as the cost at home and consequences as the cost abroad. The wider contest row runs from the Warsaw Pact through Sputnik to the farewell warning of 1961. Grade the table generously on wording and strictly on pairing: each stage must show what changed and what it cost or risked.")

# 22 SYNTHESIS
content_text('What the shadow shows',
             ['Total war became the outcome every policy had to avoid',
              'So the rivalry moved: threats, secrets, clients, prestige',
              'Each substitute carried its own cost and its own risk',
              'The home front absorbed the fear as routine',
              'The builder of the machine named its danger last'],
             "Draw the lesson together before the vocabulary, because the writing task depends on this shape. Once both sides held megaton weapons, total war stopped being an instrument of policy and became the disaster every policy existed to prevent. The rivalry did not end. It moved, into threats held at the edge under massive retaliation, into secret operations where threats could not be used, into alliances that spread the risk across continents, into other people's countries, and into a race for prestige that Sputnik opened in the sky. Each substitute for open war carried its own bill. Brinkmanship risked error at the edge. Covert action bought quick results and long consequences. The home front absorbed the fear as a school routine. And the final word belongs to the structure of the lesson itself. The president who built the machine closed his service by warning the republic about its weight. Students who can explain why he did that are ready to write.",
             kick='Synthesis', size=24)

# 23 VOCAB A
vocab('Words for the arsenal and the doctrine',
      [('arms race', 'the competition to build more and more powerful weapons, each side answering the other'),
       ('hydrogen bomb', 'a thermonuclear weapon far more powerful than the atomic bombs of 1945'),
       ('massive retaliation', 'answering aggression with the threat of a full nuclear strike'),
       ('brinkmanship', 'pushing a confrontation to the edge of war to force the other side to back down')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. The first term is arms race: the competition between the United States and the Soviet Union to build more and more powerful weapons, each side answering the other's advances. The second is hydrogen bomb: a thermonuclear weapon far more powerful than the atomic bombs of 1945, first tested by the United States in 1952 and by the Soviet Union in 1953. The third is massive retaliation: the Eisenhower administration's declared policy of answering Communist aggression with the threat of a full nuclear strike, rather than matching force at the point of attack. The fourth is brinkmanship: the practice of pushing a dangerous confrontation to the edge of war in order to force the other side to back down, described by Secretary of State John Foster Dulles.")

# 24 VOCAB B
vocab('Words for the wider contest',
      [('Warsaw Pact', 'the Soviet led alliance of 1955, formed in answer to NATO'),
       ("covert action", "a secret operation abroad that hides the sponsor's hand"),
       ('Sputnik', 'the first artificial satellite, launched by the Soviet Union in 1957')],
      "Three more terms, again matching the guided notes exactly. Warsaw Pact: the military alliance formed in 1955 joining the Soviet Union and the Communist states of Eastern Europe, created in answer to NATO and West Germany's place in it. Students should anchor the term to its trigger, West Germany's admission to NATO in the same month. The next term is covert action: a secret government operation meant to influence events abroad while hiding the sponsor's hand, carried out in the Cold War chiefly by the Central Intelligence Agency. The definition's last clause names the institution, and the lesson's two cases, Iran in 1953 and Guatemala in 1954, are the examples the test will expect behind it. Sputnik: the first artificial satellite, launched by the Soviet Union in October 1957, whose success shocked the United States and opened the space race. With these three terms the full set of seven is complete, in the guided notes, in these slides, and in the review materials.")

# 25 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did nuclear weapons change the rules of the rivalry, and how close did brinkmanship bring the world to war? Argue it from the record, with dates.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Brink File: six stations from the test record to the farewell, and a verdict on which changed the contest most'),
        ('Notebook', 'Notebook page: the five stages charted by date, change, evidence, and cost or risk'),
        ('Quick check', 'The Cloud over Enewetak: the Ivy Mike photograph, the doctrine, the drill, and the wider contest in sequence'),
        ('Writing', "Peace at the Edge: massive retaliation defended or condemned, with Eisenhower's warning used directly")]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the doctrine in one sentence, one covert action with its long record, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Brink File, runs six stations through the record: the hydrogen bomb test record of 1952 to 1954, the massive retaliation address of January 1954, the Duck and Cover home front record of 1951, the covert action records for Iran and Guatemala, the Sputnik record of 1957, and the Eisenhower farewell passage of 1961 as the closing station, ending in a verdict on which station changed the contest most. The notebook page charts five stages by date, change, evidence, and cost or risk. The quick check, The Cloud over Enewetak, tests the Ivy Mike photograph, the doctrine and the drill, and the wider contest in sequence against the blueprint. The writing task, Peace at the Edge, requires Eisenhower's farewell warning to be used directly on either side. The exit ticket has three parts: the doctrine of massive retaliation in one sentence, one covert action with its date, result, and longer record, and the lesson question answered in two or three sentences with at least two facts from the notes.")

dc.save(OUT)
