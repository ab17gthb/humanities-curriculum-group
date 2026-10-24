#!/usr/bin/env python3
"""Cold War Lesson 1 deck, "Allies to Adversaries: Containment Takes Shape,"
built to the approved system: image-led slides, fragments only on screen,
comprehensive speaker notes, full lesson + vocabulary coverage.
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
OUT = os.path.join(HERE, '..', 'lesson-01-slides.pptx')

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
text(s, 0.9, 5.32, 11.5, 0.4, 'THE COLD WAR · LESSON 1', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Allies to Adversaries: Containment Takes Shape', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'How wartime allies became rivals, and the strategy built to meet the Soviet Union, 1945 to 1949', size=17, color=POWDER)
notes(s, "The photograph shows President Truman signing the document implementing the North Atlantic Treaty at his desk in the Oval Office on August 24, 1949, photographed by Abbie Rowe, from the National Archives record 200163. Hold the date in front of students. Four years before this signing, the United States and the Soviet Union had been allies against Hitler. By 1949 the United States had built a strategy, an aid program, and an alliance against its former partner, and the president is signing the alliance into effect. This lesson walks the four years between those two facts. Students will follow the alliance breaking, two documents naming the new reality in 1946, the doctrine and the aid plan of 1947, the test at Berlin, and the settlement of 1949, and they will be asked at the end what held the whole build together.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did wartime allies become rivals, and what strategy did the United States adopt to meet the Soviet Union?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the struggle between the United States and the Soviet Union reshape the world and American life, and why did it end the way it did?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question has two halves, and students should hear both before the lesson begins. The first half asks how allies became rivals, which is a question about 1945 and 1946: an alliance built on a common enemy, a Europe divided by where the armies stopped, and pledges broken in the liberated states. The second half asks what strategy the United States adopted, which is a question about an answer built piece by piece between 1946 and 1949: an analysis, a doctrine, an aid program, an airlift, and an alliance. The word strategy deserves a moment. A strategy is not a single decision. It is a set of connected choices that hold together over years, and the lesson's work is to show students the connections. The unit question runs beneath this one as the frame for all eight lessons, from containment's birth to the dissolution of the Soviet Union in 1991.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'A strategy built in seven stretches', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'Partners of necessity', 'Allies against Hitler, divided by ideology'),
        ('B', 'The alliance unravels', 'Poland, Iran, and the Turkish straits'),
        ('C', 'Two documents name the new reality', 'The Long Telegram and the Iron Curtain'),
        ('D', 'A strategy takes shape', 'Containment: hold the line'),
        ('E', 'The doctrine and the plan', 'Truman Doctrine and Marshall Plan'),
        ('F', 'The test at Berlin', 'Blockade and airlift, 1948 to 1949'),
        ('G', 'An alliance and a second bomb', 'NATO, two Germanys, August 1949')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Sections A and B give the problem: partners of necessity, divided long before 1945, watching the wartime pledges break across Eastern Europe and Soviet pressure reach Iran and Turkey. Section C gives the naming, in February and March 1946, when Kennan's cable and Churchill's speech described the new reality within eleven days of each other. Section D states the strategy those documents supported. Section E gives the strategy its doctrine and its money in 1947. Section F tests it at Berlin. Section G settles the decade with an alliance, a divided Germany, and a second atomic bomb. Tell students the summary table at the end of their guided notes asks them to rebuild exactly this map in their own words.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', 'Partners of Necessity',
             'The alliance rested on a common enemy, not on trust.',
             "Begin with the partnership's terms, because students often assume the wartime alliance was a friendship that later soured. It was not. The United States and the Soviet Union had stood opposed since the Russian Revolution, and each entered the alliance expecting rivalry to resume once Hitler fell. The war hid the division without ending it, and teachers should keep that sentence in front of the class. Then set the ground of 1945. Victory left two powers standing far above a ruined field, and where their armies stopped in Europe, the new map hardened: Soviet armies in the East, American and British armies in the West. Every later event in this lesson runs along that line. The vocabulary word for the two standing powers, superpower, is defined in full on the vocabulary slides at the end of the lesson, and students copy it from their guided notes.")

# ------------------------------------------------------ 5 PARTNERS
content_text('Allies against Hitler, divided long before 1945',
             ['The United States and the Soviet Union were partners against a common enemy, not friends.',
              'The two powers had been divided by ideology since the Russian Revolution.',
              'Victory in 1945 left two superpowers standing above the rest.',
              'Soviet armies held Eastern Europe at the end of the war.',
              'Where the armies stopped, the map of Europe hardened.'],
             "Work the first fragment slowly. An alliance of necessity is a working arrangement, and both sides treated it as one. Washington supplied the Soviet Union with trucks, food, and material through the war while distrusting its system, and Moscow took the supplies while distrusting the supplier. Neither side was deceived, and students judge the later breakup better when they see that little trust existed to lose. The second half of the slide is the settlement the war produced. Europe's old great powers were ruined or occupied, and two states stood far above the rest, each able to project military and political strength across the world. The armies' stopping line ran through Germany and through Berlin itself, which is why Berlin becomes the strategy's test in Section F. Ask students to keep the map in mind: the Cold War's front line was drawn by the last advance of the Second World War.",
             kick='A · Partners of necessity')

# ------------------------------------------------------ 6 TWO SUPERPOWERS STAT
stat('2', 'superpowers stood above the rest in 1945',
     'The United States and the Soviet Union · Every other great power was ruined, occupied, or exhausted',
     "Let the small number carry the point. In 1939 the world held half a dozen great powers. In 1945 it held two. Britain had won and was broke, France had been occupied, Germany and Japan were defeated and divided or occupied, and China was sliding toward civil war. The United States held the atomic bomb, the world's largest navy, and an economy untouched by invasion. The Soviet Union held the largest army on earth and physical possession of Eastern Europe, bought at a cost in lives no Western state approached. A contest between two powers differs from a contest among many. There is no third party to balance against, no neutral ground of weight, and every local quarrel anywhere can be read as a move by one side against the other. Students will watch that reading habit form across this unit, and it begins here, with the field reduced to two.",
     kick='A · Partners of necessity')

# ------------------------------------------------- 7 SECTION B DIVIDER
divider_text('Section B', 'The Alliance Unravels',
             'Broken pledges in the East, and pressure beyond it.',
             "This section covers the breakup in sequence, and students should learn it as two movements. The first movement ran inside Eastern Europe, where the Yalta pledge of free elections in the liberated states broke first in Poland and then across the region, as coalition governments gave way to Communist rule backed by Soviet force. The second movement reached beyond the occupied zone. Soviet troops stayed in northern Iran past the date agreed for their withdrawal, and Moscow demanded joint control of the Turkish straits between the Black Sea and the Mediterranean. Each single move could be excused as security seeking by a state that had been invaded twice in a generation. Together the moves described a pattern, and it was the pattern, not any one move, that Washington answered. Keep asking students which reading the evidence supports, because both readings were honestly available in 1946.")

# ------------------------------------------------------ 8 UNRAVELING
content_text('Poland first, then pressure on Iran and Turkey',
             ['At Yalta, the Allies pledged free elections in the liberated states.',
              'That pledge broke first in Poland.',
              'Coalition governments gave way to Communist rule across the region.',
              'Soviet troops stayed in northern Iran past the agreed withdrawal date.',
              'Moscow demanded joint control of the Turkish straits.'],
             "Give Poland its full weight, because it was the case every later argument cited. Poland had been promised free elections at Yalta in February 1945, in writing. Instead Moscow installed a government of its choosing, arrested Polish leaders who objected, and stage managed the outcome it required. If the pledge could be set aside in the largest of the liberated states, no pledge in the region held. Then follow the pressure outward. Iran was a wartime supply corridor, not a Soviet possession, and the troops' refusal to leave on schedule tested whether wartime occupation would become permanent anywhere the Red Army had stood. The demand on Turkey touched the straits, the Soviet navy's exit to the Mediterranean, a Russian ambition older than the Soviet Union itself. Students should note the geography: the pressure of 1946 already pointed at the two countries, Greece's neighbor and Greece itself, that the doctrine of 1947 would name.",
             kick='B · The alliance unravels', size=24)

# ------------------------------------------------- 9 SECTION C DIVIDER
divider_photo('kennan-port.jpg', 'Section C', 'Two Documents Name the New Reality',
              ['George F. Kennan in 1947,', 'photographed by Harris and Ewing.'],
              "The portrait is George F. Kennan in 1947, by Harris and Ewing, from the Library of Congress record, digital ID hec.12925. Section C holds the two documents of February and March 1946 that named the new reality, and they belong together. Kennan wrote first, on February 22, in a cable from Moscow that ran to about eight thousand words, the longest telegram of its kind, sent in answer to a routine Washington question about Soviet intentions. Churchill spoke eleven days later, on March 5, at Fulton, Missouri, with President Truman seated on the platform behind him. One document was secret and one was public, one was analysis and one was oratory, and between them they gave Washington both a theory of Soviet conduct and a name the public could hold. Students read passages from both at the first two stations of the activity.",
              title_size=38)

# ------------------------------------------------------ 10 LONG TELEGRAM
content_text('The Long Telegram: insecurity, ideology, and force',
             ['On February 22, 1946, Kennan sent a cable of about 8,000 words from Moscow.',
              'Soviet expansion grew from Communist ideology joined to Russian insecurity.',
              'Soviet power took no unnecessary risks.',
              'Soviet power withdrew when it met strong resistance.',
              'Churchill named the division of Europe eleven days later.'],
             "Teach the telegram from its two claims, because the strategy stands on both. The first claim explains the opponent: Soviet expansion grew from Communist ideology joined to a traditional Russian sense of insecurity, a ruling group that had learned to seek security only in the total destruction of rival power, never in compacts and compromises. On that account no Western concession caused the hostility, and none would end it. The second claim limits the danger: Soviet power was cautious, took no unnecessary risks, ignored the logic of reason, and respected the logic of force, withdrawing when strong resistance was encountered at any point. Hold the two claims together for students. An opponent who cannot be persuaded and will not stop on his own, yet backs down before firmness, calls for exactly the strategy of the next section: steady resistance at every point tested, and no direct war. Churchill's Iron Curtain speech, delivered at Fulton with Truman on the platform, then named the geography in public.",
             kick='C · Two documents name the new reality', size=24)

# ------------------------------------------------------ 11 8000 STAT
stat('8,000', 'words in Kennan\'s Long Telegram, February 22, 1946',
     'A routine question from Washington, answered at the length of a book chapter · Read across the government within weeks',
     "Pause on the length, because the length is part of the document's power. A diplomatic cable answered a question; eight thousand words answered it with a complete theory of the Soviet system, its roots in Russian history, its ideology, its methods, and its limits. The telegram arrived in a Washington that had anecdotes about Soviet conduct and no framework for them, and it supplied the framework. Officials copied it, circulated it, and read it at the highest levels, and within a year its analysis had become the government's working account of the opponent. Kennan himself later objected to uses made of his argument, holding that he had meant a political and economic contest, not a military one everywhere. Students will meet that objection again in the writing task, where the doctrine's worldwide wording is weighed against the strategy's original design. For today, the point stands: one cable set the terms in which a superpower understood its rival.",
     kick='C · Two documents name the new reality')

# ------------------------------------------------- 12 SECTION D DIVIDER
divider_text('Section D', 'A Strategy Takes Shape',
             'Containment: hold the line where Soviet power has not yet reached.',
             "Section D states the strategy itself, and it is short by design, because containment in its first form was a simple idea with demanding consequences. Kennan's answer to the problem his telegram described was to block the further expansion of Soviet power and communism, point by point, for as long as blocking took. The strategy did not promise to roll Soviet power back where it already stood, which would have meant war with the Red Army in Eastern Europe. It promised to hold the line where Soviet power had not yet reached, and to hold it with political and economic strength first of all. Say plainly to students that the name came later in print, in Kennan's published argument of 1947, and that the men who adopted the strategy argued for years about what it required. The next two sections show it being built in public, in a doctrine and in an aid program.")

# ------------------------------------------------------ 13 CONTAINMENT LOGIC
content_text('Hold the line, and strengthen the states on it',
             ['Containment would block further Soviet expansion, point by point.',
              'Containment made no promise to roll Soviet power back where it already stood.',
              'Kennan read the contest as political and economic first.',
              'Soviet power fed on weakness and disorder.',
              'Strong, confident societies denied Soviet power its openings.'],
             "Work the logic as a chain, because the activity's briefing table asks students to rebuild it. Premise one, from the telegram: Soviet power expands into weakness and stops before firmness. Premise two: the weakness of 1946 was real and specific, ruined economies, hungry cities, discredited governments, and Communist parties waiting to inherit the disorder in France, Italy, and Greece. Conclusion: a strategy that repaired economies, restored confidence, and backed governments under pressure would deny Moscow its openings without a direct war between the superpowers. Note what the logic does not require. It does not require an American army in every threatened state, and it does not require the United States to approve of every government it aids, a discomfort the doctrine's text carries openly. It requires patience measured in decades, which Kennan stated and which American politics found hard. The strategy's own author thought in generations. The country that adopted it thought in election cycles, and the friction between those clocks runs through the whole unit.",
             kick='D · A strategy takes shape', size=24)

# ------------------------------------------------- 14 SECTION E DIVIDER
divider_photo('truman-port.jpg', 'Section E', 'The Doctrine and the Plan',
              ['President Harry S. Truman,', 'official portrait, 1947.'],
              "The portrait is the official presidential portrait of Harry S. Truman, painted by Greta Kempton in 1947 and held by the Truman Library. Section E turns from analysis to policy, and Truman is its central figure, because the strategy became policy when a president stated it to Congress and asked for money. The occasion came in February 1947, when Britain, broke and overstretched, told Washington it could give Greece and Turkey no further aid after March 31. Greece faced Communist guerrillas in a civil war, and Turkey faced Soviet pressure over the straits. Truman could have asked for an appropriation and stopped there. Instead, on March 12, 1947, he addressed a joint session of Congress, asked for four hundred million dollars, and framed the request as a universal rule. Three months later his secretary of state proposed the aid program that gave the rule its economic instrument. Students read both documents at Stations 3 and 4 of the activity.",
              title_size=38)

# ------------------------------------------------------ 15 TRUMAN DOCTRINE
content_text('A two country request, stated as a worldwide rule',
             ['Britain ended its aid to Greece and Turkey in 1947.',
              'On March 12, 1947, Truman addressed Congress to ask for aid.',
              'Truman asked for $400 million for Greece and Turkey.',
              'The United States would support free peoples resisting subjugation.',
              'That help would be chiefly economic and financial.'],
             "Read the doctrine's sentence aloud, because its wording is the lesson's central evidence. Truman declared that it must be the policy of the United States to support free peoples who are resisting attempted subjugation by armed minorities or by outside pressures, and that the help should be primarily through economic and financial aid. Then measure the sentence against its occasion. The request before Congress named two countries and one sum. The sentence names no country, no enemy, and no limit, and it covers pressure from inside a country, by armed minorities, as well as pressure from outside. Students should see both faces of that choice. As statecraft, a rule stated once could deter in the next case without a new debate, and it told Moscow the commitment was general. As a commitment, it promised in advance for cases no one in the room had imagined, and later governments inherited the words. The writing task asks students to judge which face mattered more.",
             kick='E · The doctrine and the plan', size=24)

# ------------------------------------------------------ 16 $400M STAT
stat('$400 million', 'asked for Greece and Turkey, March 1947',
     'The first appropriation under the Truman Doctrine · Britain had set the deadline: no further aid after March 31',
     "The sum deserves its scale. Four hundred million dollars in 1947 was a large appropriation for two small countries, and Congress voted it after a debate that ran for weeks, because members understood they were voting on more than the money. They were voting on the sentence that carried it, and Senator Vandenberg, the Republican whose support Truman needed, told the president he would have to scare the country to get it through. The deadline in the slide is the detail students should keep. Britain did not withdraw from Greece and Turkey out of indifference. It withdrew because it could no longer pay, and the handover of March 1947 is the moment the United States took up, in public and with money, a burden Britain had carried for a century: holding the eastern Mediterranean against Russian pressure. The strategy now had a doctrine, a deadline met, and a first payment made.",
     kick='E · The doctrine and the plan')

# ------------------------------------------------------ 17 MARSHALL
content_photo_s('marshall-port.jpg', 'The Marshall Plan: aid aimed at hunger and chaos',
              ['On June 5, 1947, Marshall proposed the plan at Harvard.',
               'The plan gave about $13 billion in aid from 1948 to 1952.',
               'The plan was aimed at hunger, poverty, desperation, and chaos.',
               'Moscow barred its satellites from taking part in the plan.',
               'The plan bound Western Europe to the United States.'],
              "The photograph is the official military portrait of George C. Marshall, from the Department of Defense record. Marshall, the secretary of state and the Army's wartime chief of staff, proposed the plan in a Harvard commencement address on June 5, 1947, in deliberately plain words. His diagnosis matched Kennan's premise. The visible destruction of Europe, he argued, was less serious than the dislocation of the entire fabric of its economy, and American policy should be directed not against any country or doctrine but against hunger, poverty, desperation, and chaos. Congress funded about thirteen billion dollars over four years. The offer was formally open to the Soviet Union and its sphere, and Moscow refused it and barred the states under its control from taking part, which fixed the plan's dividing line in practice. Western Europe's recovery, and its binding to the United States in trade and politics, was containment's largest single success, achieved without a soldier firing. Students should be able to pair the two instruments of 1947: the doctrine promised, the plan paid.",
              kick='E · The doctrine and the plan')

# ------------------------------------------------- 18 SECTION F DIVIDER
divider_photo('berlin-port.jpg', 'Section F', 'The Test at Berlin',
              ['A United States C-54 over Berlin, 1948,', 'watched by German children.'],
              "The photograph, by Henry Ries of the United States Air Force and held by the Library of Congress, shows a C-54 over Berlin during the airlift, watched by German children from a hillside. Section F is the strategy's first direct test, and Berlin was the place most likely to produce it. The city sat deep inside the Soviet occupation zone, held in sectors by the four victorious powers, with its western sectors supplied by road, rail, and canal through Soviet held territory. In June 1948, after the Western powers joined their zones and reformed the currency, the Soviet Union closed every land route into West Berlin. About two million people faced the loss of food and coal by land. The closure was a probe in exactly Kennan's sense: firmness would be answered, or weakness would be. The answer the West gave surprised Moscow, and students work the record at Station 5 of the activity.",
              title_size=38)

# ------------------------------------------------------ 19 AIRLIFT
content_text('A city of two million, supplied by air',
             ['In June 1948, the Soviet Union closed every land route into West Berlin.',
              'Food and coal were flown into the city around the clock.',
              'The airlift lasted eleven months, through a winter.',
              'In May 1949, the blockade was lifted and nothing had been gained.',
              'West Berlin stayed Western.'],
             "Work the airlift as the strategy performed under pressure. The Western choice was not between the airlift and nothing. The alternatives were abandonment of two million Berliners, negotiation from weakness, or an armed convoy forcing its way down the highway, which could have begun the war both sides said they did not want. The airlift refused all three. It met the blockade with a supply effort of a scale Moscow had judged impossible, planes landing at intervals measured in minutes at the peak, coal as well as food, through a Berlin winter. Seventy or so Allied airmen died in crashes during the operation, a cost students should hear stated, because the resistance was firm without being bloodless. In May 1949 the Soviet Union lifted the blockade having gained nothing, and Kennan's prediction had been borne out in the hardest case: strong resistance, short of attack, had made Soviet power withdraw. The blockade's failure also settled Berlin's status for a generation.",
             kick='F · The test at Berlin', size=24)

# ------------------------------------------------------ 20 11 MONTHS STAT
stat('11 months', 'of airlift, June 1948 to May 1949',
     'About two million West Berliners supplied by plane · Food and coal, around the clock, through the winter',
     "Eleven months is the figure that defeats the blockade's logic. A blockade works by time: the besieger waits, the besieged consume their stores, and surrender becomes arithmetic. The airlift reversed the arithmetic. Every month the planes kept landing proved the city could be held indefinitely, and every month cost the Soviet Union standing with the Germans it hoped one day to win. The tonnage figures belong in the notes as an estimate stated carefully: at the effort's peak the airlift delivered thousands of tons a day, and on its best day, in April 1949, nearly thirteen thousand tons, more than the railways had carried before the blockade. Hold the human frame beside the figures. The cargo was food and coal for about two million people, flown by young crews in winter weather, and watched daily by the children in the divider photograph. Containment here was not an abstraction. It was a supply line made of airplanes, and Berliners could set their watches by it.",
     kick='F · The test at Berlin')

# ------------------------------------------------- 21 SECTION G DIVIDER
divider_photo('nato-port.jpg', 'Section G', 'An Alliance, Two Germanys, and a Second Bomb',
              ['Truman signs the North Atlantic Treaty', 'document into effect, August 1949.'],
              "The photograph shows Truman signing the document implementing the North Atlantic Treaty in the Oval Office on August 24, 1949, by Abbie Rowe, from the National Archives record 200163. Section G settles the decade the lesson has built. In April 1949, while the airlift still flew, the United States signed the treaty creating the North Atlantic Treaty Organization with Canada and the nations of Western Europe, the first peacetime alliance in American history. Germany divided to match the continent, the Western zones becoming the Federal Republic and the Soviet zone the German Democratic Republic. And in August 1949, weeks before the treaty signing in this photograph, the Soviet Union tested its first atomic bomb, years earlier than American estimates had expected. The strategy built to hold a line in Europe now had to hold it against a nuclear armed rival, and the reading closes on the change that fact was about to force.",
              title_size=34)

# ------------------------------------------------------ 22 SETTLEMENT OF 1949
content_text('The pledge, the divided country, the ended monopoly',
             ['NATO pledged that an attack on one member is an attack on all.',
              'NATO was the first peacetime alliance in American history.',
              'Two German states were formed in 1949.',
              'In August 1949, the Soviet Union tested its first atomic bomb.',
              'The American monopoly on the atomic bomb ended.'],
             "Take the three facts of 1949 in order, and students should be able to state what each one fixed in place. The alliance fixed the commitment: American power was pledged to Europe's defense in advance of any attack, so a future president could not weigh the question fresh in a crisis, which was the treaty's purpose. The German settlement fixed the map: two states, each bound to its side, with Berlin still divided inside the Eastern one, a standing reminder that the division was unfinished. The Soviet bomb fixed the danger: from August 1949 the rivalry the strategy managed was a rivalry between nuclear powers, and every later test of containment, in Korea, Cuba, and Vietnam, ran under that shadow. Close the section by returning to Kennan's design. Containment as he argued it was political and economic, waged with aid, trade, and firmness. The bomb and the alliance were already pulling it toward the military and the global, which is where the next lesson, on China and Korea, begins.",
             kick='G · An alliance, two Germanys, and a second bomb', size=24)

# ------------------------------------------------------ 23 SYNTHESIS
content_text('A strategy built, and the question it left open',
             ['The build ran in order: analysis, doctrine, money, proof, and alliance.',
              'The strategy was built in four years, from 1946 to 1949.',
              'Kennan read the contest as political and economic.',
              'Events were about to make the contest military and global.'],
             "Close the teaching where the reading closes, with the build complete and its open question named. Between February 1946 and August 1949 the United States produced, in order, an analysis of the opponent, a public doctrine, an aid program of thirteen billion dollars, a successful act of resistance at Berlin, and a peacetime alliance, and it did all of this without a direct war with the Soviet Union. That is containment as designed, and students should be able to recite the build as a single sentence. Then state the tension the unit will spend seven lessons testing. Kennan's design was political and economic, aimed at a line in Europe. The Soviet bomb, the fall of China weeks after this lesson ends, and war in Korea were about to make the strategy military and global, applied in places its author never meant it to govern. Whether that widening served the strategy or broke it is the argument of the unit, and students now hold the original design against which to judge it.",
             kick='G · An alliance, two Germanys, and a second bomb')

# ------------------------------------------------------ 24 VOCAB A
vocab('Words for the problem and the strategy',
      [('superpower', 'a nation with power and influence far beyond that of other states'),
       ('Iron Curtain', 'the boundary Churchill named in 1946 between East and West'),
       ('containment', 'the strategy of blocking the further expansion of Soviet power'),
       ('Truman Doctrine', 'the 1947 policy of supporting free peoples resisting subjugation')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. superpower: a nation with power and influence far beyond that of other states, able to project military and political strength across the world. Iron Curtain: the boundary Winston Churchill named in 1946 between the Soviet-dominated states of Eastern Europe and the free states of the West, and the division of Europe it described. containment: the American strategy of blocking the further expansion of Soviet power and communism, first argued by George Kennan and adopted as the guiding policy of the early Cold War. Truman Doctrine: the policy President Truman declared in 1947, that the United States would support free peoples resisting attempted subjugation by armed minorities or outside pressures. Note the two definition habits worth teaching: each names a date or an author, and the doctrine's definition keeps Truman's own standard, subjugation by armed minorities or outside pressures, inside it.")

# ------------------------------------------------------ 25 VOCAB B
vocab('Words for the instruments and the test',
      [('Marshall Plan', 'the program of 1948 to 1952 that gave about $13 billion to rebuild Western Europe'),
       ('Berlin Airlift', 'the American and British air supply of West Berlin in 1948 and 1949'),
       ('NATO', 'the 1949 alliance pledging members to treat an attack on one as an attack on all')],
      "Three more terms, again matching the guided notes exactly. Marshall Plan: the American program of 1948 to 1952 that gave about thirteen billion dollars in aid to rebuild the economies of Western Europe after the Second World War. The dates and the sum are part of the definition, and students should hold both. Berlin Airlift: the American and British air supply of West Berlin in 1948 and 1949, flown around the Soviet blockade of the city's land routes. The definition's last clause does the teaching work: the airlift existed because the land routes were closed, and it ended the blockade by outlasting it. NATO: the North Atlantic Treaty Organization, the alliance formed in 1949 in which the United States, Canada, and Western European nations pledged to treat an attack on one member as an attack on all. Students should be able to expand the initials and state the pledge in the definition's own words.")

# ------------------------------------------------------ 26 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Build the briefing', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did wartime allies become rivals, and what strategy did the United States adopt to meet the Soviet Union? Work the documents in order, then judge which one fixed the policy in place.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Strategy Desk: the Long Telegram, the Iron Curtain speech, the Truman Doctrine, the Harvard address, and the Berlin Airlift record'),
        ('Notebook', 'Notebook page: six steps of the build, judged and evidenced'),
        ('Quick check', 'The Doctrine and the Line: the Truman Doctrine passage against the record of 1946 and 1947'),
        ('Writing', 'A Doctrine Without Borders?: the worldwide wording of 1947 weighed against the strategy it served')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: containment stated and its author named, the doctrine and the plan compared by their tools, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Strategy Desk, runs five stations through the evidence: the Long Telegram passage, the Iron Curtain passage with a labeled summary of the rest of the address, the Truman Doctrine passage, the Harvard address passage, and a labeled summary of the Berlin Airlift with the Air Force photograph, ending in a briefing table where students state the threat, the tools, the line, and the test, and judge which document fixed the policy in place. The notebook page asks students to rebuild six steps of the build with evidence. The quick check, The Doctrine and the Line, tests the doctrine passage against the record of 1946 and 1947, tagged to the blueprint. The writing task, A Doctrine Without Borders?, weighs the doctrine's worldwide wording against the strategy's need. The exit ticket has three parts: containment stated with its author named; the doctrine and the plan compared by their tools; and the lesson question in two or three sentences with two facts. Next lesson takes up China and Korea.")

dc.save(OUT)
