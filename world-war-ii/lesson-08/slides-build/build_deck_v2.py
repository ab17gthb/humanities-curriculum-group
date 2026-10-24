#!/usr/bin/env python3
"""World War II Lesson 8 deck, "Victory and the Atomic Reckoning," built to
the approved system: image-led slides, fragments only on screen,
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
OUT = os.path.join(HERE, '..', 'lesson-08-slides.pptx')

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

# ---------------------------------------------------------------- 1 · TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'WORLD WAR II · LESSON 8', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Victory and the Atomic Reckoning', size=34, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'The conferences, the bomb, the surrender, and the country that came home', size=17, color=POWDER)
notes(s, "The photograph shows the Japanese delegation standing on the deck of the battleship Missouri in Tokyo Bay on September 2, 1945, during the surrender ceremonies that formally ended the Second World War. It is the right opening image for the unit's final lesson because this lesson ends where that deck stood, and works backward and forward from it: backward to the conferences at Yalta and Potsdam that planned the peace, to the secret weapon built across the United States, and to the argument over whether to show that weapon first or use it; forward to the reckoning in figures and to the transformed country that more than twelve million Americans in uniform came home to. Teach the lesson as a file of documents, because the activity and the writing task both judge the atomic decision from those documents and from nothing else.")

# ------------------------------------------------- 2 · LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("How did the war end, what did the atomic bomb decide and leave undecided, and what country came home from the war?", {})]],
     size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the Second World War transform the United States, and how far did the country live up to the democracy it claimed to defend?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question has three parts, and the exit ticket requires all three. First, how the war ended: not in one blow but in a sequence running from the conferences through the Potsdam ultimatum, the two bombs, the Soviet entry into the war, and the emperor's intervention, to the signing on September 2. Second, what the bomb decided and left undecided: it decided the war against Japan on the Potsdam terms, and it did not decide the future of Europe, which the winning alliance was already arguing over. Third, what country came home: a country that had lost about 405,000 of its people, doubled its economy, and stood as one of two great powers, carrying veterans home into the GI Bill and into a peace whose central division the new weapon had made dangerous. Students will judge the decision itself in the writing task, from documents.")

# --------------------------------------------------- 3 · THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'The peace planned, the weapon used, the reckoning taken', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'Planning the peace at Yalta', 'Germany divided; the United Nations; Soviet entry pledged'),
        ('B', 'A new president and Potsdam', 'Truman from April 12; occupation argued; the ultimatum of July 26'),
        ('C', 'The secret weapon', 'The Manhattan Project; Trinity, July 16, 1945'),
        ('D', 'The decision argued', 'The Franck Report against the Interim Committee'),
        ('E', 'August 1945', 'Hiroshima, Soviet entry, Nagasaki, the signing on September 2'),
        ('F', 'The reckoning in figures', 'About 405,000 American dead; the world estimate, 60 to 85 million'),
        ('G', 'The country that came home', 'Demobilization, the GI Bill, one of two great powers')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "The map follows the guided notes section by section. Sections A and B cover the planning of the peace: Yalta in February 1945, where the postwar settlement was sketched while Germany still fought, and Potsdam in July, where a new president argued over the settlement with the ink barely dry. Section C introduces the secret weapon and its successful test, which sat behind everything said at Potsdam. Section D stages the argument over the weapon's use, scientists against committee, as a documentary record rather than a classroom opinion poll. Section E runs the August sequence day by day. Section F stops the narrative and counts the cost, with every figure labeled an estimate where it is one. Section G follows the country home. Warn students now that the order is deliberate: the decision is argued from the file before the outcome is allowed to argue for it.")

# ------------------------------------------------- 4 · SECTION A DIVIDER
divider_photo('yalta-port.jpg', 'Section A', 'Planning the Peace at Yalta',
              ['February 1945: three leaders, one settlement sketched,', 'and much left vague.'],
              "The photograph shows Churchill, Roosevelt, and Stalin seated together at Yalta, in the Soviet Crimea, on February 9, 1945. Set the scene precisely. Germany was near defeat but still fighting, the Red Army stood deep inside eastern Europe, and Roosevelt had traveled a long way in failing health to meet Stalin on Soviet ground. The meeting planned the peace while the war ran, which is why so much of it was drawn in outline: occupation zones for a Germany not yet surrendered, a world organization not yet founded, elections promised for countries whose governments Soviet armies would in practice choose. Teach students to hold both halves of that sentence. Yalta was a real settlement with real terms, and it was also a set of words each signer could read in his own way, above all on Poland. The argument at Potsdam five months later was built into the vagueness agreed here.",
              title_size=36)

# ------------------------------------------------------ 5 · WHAT YALTA SETTLED
content_text('What Yalta settled, and left vague',
             ['Germany was to be divided into occupation zones and disarmed.',
              'The United Nations was founded, with great powers in its Security Council.',
              'Stalin pledged free elections in eastern Europe.',
              'Stalin pledged Soviet entry against Japan after Germany fell.',
              'The price was territory and rights for the Soviet Union in Asia.',
              'The government and borders of Poland were left vague.'],
             "Work the settlement as a trade, because that is how it was made. The Western leaders got Soviet entry into the Pacific war, which in February 1945, with Okinawa still ahead, American planners wanted badly, and they got a world organization with the Soviet Union inside it rather than outside. Stalin got recognition of Soviet gains in Asia, including territory lost to Japan in 1905, and a free hand the pledges on elections did little to limit, because his armies already occupied the ground the pledges covered. The guided notes definitions run through this section and the next, and students should meet the first one here in full later in the vocabulary slides. For now, fix the method point, because the whole closing argument of the unit rests on it: a pledge is a fact about words, and an army in occupation is a fact about ground, and when the two conflicted in eastern Europe, the ground decided. Poland is the case to name. Its government and borders were the vaguest part of Yalta and the sharpest argument at Potsdam.",
             kick='A · Planning the peace at Yalta', size=24)

# ------------------------------------------------- 6 · SECTION B DIVIDER
divider_photo('potsdam-port.jpg', 'Section B', 'A New President and Potsdam',
              ['July 1945: the settlement argued over,', 'and an ultimatum sent to Japan.'],
              "The photograph shows the delegates seated around the conference table at Cecilienhof Palace in Potsdam, in occupied Germany, in July 1945. Begin with the changed cast, because students miss how much turned on it. Roosevelt died on April 12, weeks before Germany surrendered on May 8, and Harry Truman, vice president for less than three months, took his place at the table. Churchill began the conference and Clement Attlee finished it, after a British election changed governments in the middle of the meeting. Only Stalin sat in the chair he had held at Yalta. The conference set occupation policy for Germany, moved Germany's eastern border westward at Poland's expense, and argued over reparations and over eastern Europe, where the elections pledged at Yalta were producing Communist governments under Soviet protection. It was at this table, on July 26, that the ultimatum to Japan was issued, and it was here that Truman received word that the Trinity test had succeeded.",
              title_size=36)

# ------------------------------------------------------ 7 · POTSDAM AND THE ULTIMATUM
content_text('Occupation argued, ultimatum issued',
             ['Occupation policy was set for a defeated Germany.',
              'Reparations and eastern Europe were argued, not settled.',
              'On July 26, the Potsdam Declaration was sent to Japan.',
              'The demand was the unconditional surrender of the armed forces.',
              'The promise was that Japan would not be destroyed as a nation.',
              'The warning was prompt and utter destruction, with the weapon unnamed.'],
             "The Potsdam Declaration is the first station of the activity, and this slide should send students into it with its three parts already separated. The demand was total and explicitly non-negotiable: the unconditional surrender of all Japanese armed forces, on terms the Allies would not deviate from, with no alternatives and no delay. The promise was real and should not be skipped: Japan would not be enslaved as a race or destroyed as a nation, war criminals would face stern justice, and freedoms of speech, religion, and thought would be established. The warning was deliberately unspecific. Prompt and utter destruction named no weapon, ten days after Trinity, because the weapon was still secret and because its makers wanted the threat read at full size without being examined. Japan's leaders gave no acceptance, and the file's next documents, the scientists' report and the invasion planning, were already on desks in Washington when the silence came back. Note also what the declaration did not say: it never stated the future of the emperor, the question Tokyo cared about most.",
             kick='B · A new president and Potsdam', size=23)

# ------------------------------------------------- 8 · SECTION C DIVIDER
divider_photo('trinity-port.jpg', 'Section C', 'The Secret Weapon',
              ['Trinity, July 16, 1945: the first atomic explosion,', 'photographed by Los Alamos at 16 milliseconds.'],
              "The photograph is the Trinity fireball sixteen milliseconds after detonation at Alamogordo, New Mexico, on July 16, 1945, taken by Berlyn Brixner for Los Alamos National Laboratory; the top of the hemisphere shown is about two hundred meters high. Present it as a laboratory record, which is what it is: the project's own instrument reading, timed in thousandths of a second, not an image made for the public, which was not told the weapon existed for three more weeks. The chronology carries the teaching. The test succeeded while Truman sat at Potsdam, and the news reached him there by coded message, so the ultimatum of July 26 was written by men who knew the warning could be carried out by a single airplane. The scientists who built the device had already written their warning a month earlier, in June, before they knew the test would work. Sequence is the argument of this lesson: report in June, test in July, ultimatum in July, decision in August.",
              title_size=38)

# ------------------------------------------------------ 9 · BUILT IN SECRET
content_text('A weapon built in secret',
             ['The project began in 1942, at sites across the whole country.',
              'Its sites included Oak Ridge, Hanford, and Los Alamos, where the bombs were designed.',
              'More than 100,000 workers took part, and most were not told what they were making.',
              'The project cost about two billion dollars, voted without public debate.',
              'The bomb\u2019s power comes from splitting atoms.'],
             "Give the project its scale before its product, because scale explains both the secrecy and the momentum behind the decision. The Manhattan Project ran for more than two years as a small secret state inside the country: enrichment plants at Oak Ridge in Tennessee the size of a town, plutonium reactors at Hanford in Washington, and the design laboratory at Los Alamos in New Mexico under J. Robert Oppenheimer. Most of the more than 100,000 people who worked on it knew only their own task; compartmentalization was the security system. Congress voted the money, about two billion dollars, without public debate of what it was buying. The product deserves one exact sentence, which the guided notes carry as a definition: an atomic bomb draws its explosive power from splitting atoms, releasing energy on a scale no ordinary explosive can match, thousands of times the force of the largest conventional bomb from a single device carried by a single aircraft. That ratio, one plane against a fleet, is what changed the decision from a bombing question into something else.",
             kick='C · The secret weapon', size=23)

# ------------------------------------------------------ 10 · STAT 100,000+
stat('100,000+', 'people employed by the Manhattan Project at sites across the country',
     'About two billion dollars spent in secret · The peak workforce is commonly put at about 130,000',
     "Teach this figure the way the lesson teaches every figure: with its precision stated. The guided notes definition says the project employed more than 100,000 people, and that is the form students should use, because the project's own records support it without argument. The commonly cited peak figure is about 130,000, reached in 1944 as the production sites ran at full strength. Either form is honest; a single exact headcount presented as certain would not be, since the workforce turned over constantly and many workers were employed by contractors on single tasks. The money deserves the same treatment: about two billion dollars, in a war whose total American cost ran above three hundred billion, which is part of why the expenditure stayed hidden inside the larger accounts. Put the two facts together for the class: a weapon built by a city's worth of people, in total secrecy, in a democracy at war, and then ask who in that democracy had consented to its use, and in what form. The decision argued in the next section is where that question lands.",
     kick='C · The secret weapon')

# ------------------------------------------------- 11 · SECTION D DIVIDER
divider_text('Section D', 'The Decision Argued',
             'The scientists who built the bomb asked to show it first. The committee advised using it. Both arguments survive on paper.',
             "This is the lesson's center, and it should be taught as a paper record, because a paper record is what survives and what the writing task grades. Two documents were written before the decision. In June, a committee of project scientists at Chicago, chaired by James Franck, sent a report to Washington arguing that the bomb be demonstrated before it was used on a city. The government's Interim Committee, advised by its own scientific panel, recommended use against Japan without a demonstration. Neither document was a vote, and there was no single meeting at which the bombing was decided in a form students can dramatize; the decision formed as recommendations moved upward and the president accepted the one that reached him with the machinery of war already built around it. That bureaucratic shape is itself a finding of the lesson, and students who understand it write better memoranda in the activity than students waiting for a single dramatic moment of choice.")

# ------------------------------------------------------ 12 · THE FRANCK REPORT
content_text('Show it first: the Franck Report',
             ['On June 11, 1945, scientists who built the bomb wrote the report.',
              'They proposed demonstrating it on a desert or a barren island.',
              'The demonstration would be held before representatives of all nations.',
              'Sudden use would bring horror across the world.',
              'Sudden use would start an arms race no one could supervise.'],
             "Read the Franck Report's logic in its own order, because it is an argument, not a protest. The authors begin by disclaiming authority: they do not presume to speak on national policy. They claim instead a knowledge no one else had: a small group of citizens aware of a grave danger of which the rest of mankind was unaware, because they had created it. Their prediction follows. Sudden use on a city might save American lives and win military advantage, and still be outweighed by the loss of confidence and the wave of horror and repulsion sweeping the world, and by the arms race that an unsupervised weapon would start. Their proposal is constructive, and students should be required to state it whole: demonstrate the weapon before representatives of all nations, on a desert or a barren island, so America could say it had a weapon it did not use, and only then, with international sanction and a further ultimatum, use it if Japan still refused. The report reached the Interim Committee and was set aside, and it stayed classified until 1946.",
             kick='D · The decision argued', size=23)

# ------------------------------------------------------ 13 · THE RECOMMENDATION ACCEPTED
content_text('The recommendation Truman accepted',
             ['The Interim Committee advised use, without a demonstration.',
              'The argument from Okinawa was that invasion would cost heavily.',
              'Blockade and bombing had not brought surrender.',
              'Some officials hoped shock would break the deadlock in Tokyo.',
              'Truman accepted the recommendation, and no demonstration was held.'],
             "State the other side at the same full strength, because the writing task will grade students on doing exactly that. The case for use, as it was made at the time, rested on the Pacific war's recent arithmetic. Iwo Jima had cost about 6,800 American dead for eight square miles; Okinawa, just finished, about 12,500 American dead, Japanese military deaths above 100,000, and kamikaze attacks in waves. Planners were preparing landings on Kyushu for November 1945 and on Honshu for the spring, and their cost estimates varied widely and were never agreed, a distinction students must keep: the battles are record, the invasion figure is estimate. Blockade and conventional bombing had hurt Japan badly without moving its government, and the Potsdam terms had just gone unanswered. Some officials also hoped the weapon's shock, and Soviet entry, would break the deadlock inside the Japanese cabinet without an invasion. Truman accepted the Interim Committee's recommendation. No demonstration was held, no warning named the weapon, and the machinery built over three years carried the decision into August.",
             kick='D · The decision argued', size=23)

# ------------------------------------------------- 14 · SECTION E DIVIDER
divider_photo('hiroshima-port.jpg', 'Section E', 'August 1945',
              ['The cloud over Hiroshima, August 6, 1945,', 'photographed from the bombing mission. Record, not spectacle.'],
              "The photograph shows the cloud over Hiroshima on August 6, 1945, smoke rising twenty thousand feet above the city over the burst at its base, photographed from the bombing mission; the Commons record credits George Caron, tail gunner of the Enola Gay. Use it once, with its caption, and move on: it is evidence of scale, the visible form of a single weapon's effect on a city, and it is not decoration for this section. What it cannot show belongs in the teaching. Tens of thousands of people died at Hiroshima that day, and more died later of burns and radiation; the surviving records support estimates, not an exact count, and students should say so rather than recite a single figure as certain. The section then runs the sequence that the quick check and the writing task both test: August 6, Hiroshima; August 8, the Soviet Union declares war; August 9, the invasion of Manchuria and the second bomb at Nagasaki; and a Japanese government that even then split evenly, until the emperor broke the deadlock.",
              title_size=40)

# ------------------------------------------------------ 15 · THE AUGUST SEQUENCE
content_text('Nine days that ended the war',
             ['On August 6, the Enola Gay bombed Hiroshima.',
              'On August 8, the Soviet Union declared war on Japan.',
              'On August 9, Manchuria was invaded and a second bomb fell on Nagasaki.',
              'The Japanese cabinet split evenly, even then.',
              'The emperor broke the deadlock for acceptance.',
              'On August 14, Japan accepted the Potsdam terms.'],
             "Teach the sequence against the simplest version of the story, because the lesson's evidence will not carry that version. Hiroshima did not produce surrender the next morning. Japan's leaders, the Supreme War Council and the cabinet behind it, remained split between accepting the Potsdam terms and fighting on for better ones, in particular a guarantee for the imperial institution. Two further shocks landed within a day of each other: the Soviet Union, honoring the pledge made at Yalta, declared war on August 8 and invaded Manchuria on August 9, destroying Japan's hope that Moscow might mediate a settlement; and the second bomb fell on Nagasaki the same day, after the primary target, Kokura, was found under cloud. Even then the cabinet deadlocked three against three on the conditions of acceptance, and Emperor Hirohito broke the deadlock in favor of accepting Potsdam provided the emperor's position survived. Japan communicated acceptance on August 14. Students should leave able to say that the war ended through a sequence of blows and a decision in Tokyo, not through one explosion acting on its own.",
             kick='E · August 1945', size=23)

# ------------------------------------------------------ 16 · THE SIGNING
content_photo_s('surrender-port.jpg', 'Signed aboard the Missouri',
             ['The signing took place on September 2, 1945, in Tokyo Bay.',
              'Shigemitsu signed for the Emperor and the government.',
              'MacArthur accepted for the Allied Powers.',
              'The Potsdam terms were accepted in writing.',
              'The Emperor was kept, and placed under the Supreme Commander.'],
             "The photograph shows Foreign Minister Mamoru Shigemitsu signing the Instrument of Surrender aboard the Missouri on September 2, 1945, the image the activity and the quick check are built on. Read the document's double action with students, because it is the war's formal ending and it is more precise than the word surrender alone. Japan accepted the provisions of the Potsdam Declaration by name and date, proclaimed the unconditional surrender of all its armed forces wherever situated, and ordered them to cease hostilities and preserve their ships and aircraft from damage. And the authority of the Emperor and the Japanese Government to rule the state was made subject to the Supreme Commander for the Allied Powers, MacArthur, who accepted the surrender before officers of nine nations signed after him. The emperor whose retention had been Tokyo's sticking point survived, and survived subordinated, in the same sentence. The ceremony took about twenty minutes. The war that had begun at Pearl Harbor on a Sunday morning ended with signatures, on a battleship, in the harbor of the defeated capital.",
             kick='E · August 1945')

# ------------------------------------------------- 17 · SECTION F DIVIDER
divider_text('Section F', 'The Reckoning in Figures',
             'Every figure in this section is stated the way the record supports it. Where the record supports an estimate, the lesson says estimate.',
             "Slow the lesson down here. The reckoning is not a list of numbers to memorize but a discipline to practice, and it is the discipline the rest of the course assumes from here on. Some figures in the record are firm within a small margin: American deaths in the war stand at about 405,000, counted from service records. Others are constructions built after the fact from incomplete counts in ruined countries, and honest teaching labels them as the estimates they are: worldwide deaths between 60 and 85 million, Soviet deaths about 27 million. The range in the worldwide figure is not a failure of the record to be hidden from students; it is information, telling them how much of the dying happened where registration, government, and archives had themselves been destroyed. Insist on the labels in class discussion. A student who says the war killed a precise worldwide number has not learned the section, however impressive the number sounds.")

# ------------------------------------------------------ 18 · STAT 405,000
stat('405,000', 'about 405,000 American dead in the Second World War',
     'Out of more than 16 million who served · Counted from service records, and stated as about',
     "Put this number against its denominator before judging it, because both halves are the finding. More than sixteen million Americans served in uniform during the war, from an army of under two hundred thousand in 1939, and about 405,000 of them died, in combat, from wounds, in accidents, in prison camps, and at sea. The figure is stated with the word about in front of it in the reading, and it should stay there in student work; the service records behind it are strong, but wartime counting across every theater and every ship was not exact to the last name, and the lesson's rule is to claim only the precision the record carries. Then widen the comparison the next slides make. American deaths were the smallest share among the great belligerents, because the war was never fought on American soil, American cities were never bombed, and the two largest land wars, in eastern Europe and in China, were borne by other nations' armies and civilians. The 405,000 are the American count. The world count is of another order entirely, and it comes next.",
     kick='F · The reckoning in figures')

# ------------------------------------------------------ 19 · STAT WORLDWIDE (custom size)
s = slide(NAVY)
kicker(s, 'F · The reckoning in figures')
text(s, 0.9, 1.55, 11.53, 2.6, '60 to 85 million', size=84, color=CREAM, font='Georgia',
     align=PP_ALIGN.CENTER, space_after=0)
text(s, 0.9, 4.35, 11.53, 0.9, 'worldwide deaths in the Second World War, estimated', size=30, color=CREAM, align=PP_ALIGN.CENTER, space_after=0)
text(s, 1.9, 5.35, 9.53, 1.2, 'A range, not a count: the dying outran the records in much of Europe and Asia', size=20, color=POWDER, align=PP_ALIGN.CENTER, leading=1.3)
notes(s, "This number should be taught as a range and defended as one. Worldwide deaths in the war are estimated between 60 and 85 million, soldiers and civilians together, and the width of the range is the lesson: in the Soviet Union, in China, and across occupied Europe, whole systems of registration and government were destroyed along with the people, and the totals were reconstructed afterward from fragments, censuses, and graves. A death toll roughly equal to the entire population of the United States' largest states, several times over, also outruns intuition, so translate it into proportions students can hold. Well over half the dead were civilians, killed by bombing, by starvation and disease under occupation, by massacre, and in the camps taught in the last lesson. Military deaths were the smaller share of the whole. The country comparisons on the next slide, the Soviet Union first, explain where the range's weight actually sits, and why the American experience of this war, grievous as 405,000 deaths were, was not the world's experience of it.")
# ------------------------------------------------------ 20 · THE LARGEST SHARE
content_text('The largest share, and the displaced',
             ['Soviet deaths were about 27 million, an estimate.',
              'The dead were soldiers and civilians, in a war fought across Soviet land.',
              'China lost millions more, and Japan lost about three million.',
              'Millions across Europe and Asia had no homes to return to.',
              'Cities from Warsaw to Tokyo stood in ruins.'],
             "The Soviet figure needs its composition stated, because 27 million said flat can sound like a battlefield total. It joins Red Army deaths, in battle, in German captivity, and of wounds, with civilian deaths under an occupation that starved cities, burned villages, and murdered communities as policy; the Eastern Front taught in this unit carried the largest land fighting of the war, and the Soviet Union's losses are the largest of any nation by a wide margin. China's losses run into the tens of millions by some estimates and are among the least completely recorded of all. Japan's dead, about three million, join soldiers across the Pacific and China with civilians of the firebombing and the two atomic bombs. Then widen the frame past the dead. Across Europe and Asia, millions of survivors in 1945 had no homes to return to: displaced persons in camps, prisoners walking out of captivity, families separated by borders that had been moved under them. The reckoning that Potsdam argued over was not only a map and a set of reparations; it was this, a continent of the displaced, administered by armies.",
             kick='F · The reckoning in figures', size=23)

# ------------------------------------------------- 21 · SECTION G DIVIDER
divider_text('Section G', 'The Country That Came Home',
             'Twelve million in uniform, an economy doubled, and a standing among nations the country had never held.',
             "Open the last section with the demobilization's speed, because speed is its story. When Japan surrendered, more than twelve million Americans were in uniform, and the political demand to bring them home was irresistible; the armed forces shrank faster than the planners of 1945 thought safe, and by 1947 the wartime military had largely dissolved into civilian life. What caught the returning millions, and kept a demobilization of that scale from becoming the unemployment crisis many economists predicted, was a law already a year old when the war ended: the Servicemen's Readjustment Act of 1944, the GI Bill. Teach the section in the reading's order: the machinery of return first, tuition and pay and loans; then the economy that received them, doubled in output by the war; then the limits, the women pushed out of war jobs and the Black veterans returning to segregation; and finally the standing the country held, one of two great powers, which is the fact the closing synthesis will pick up.")

# ------------------------------------------------------ 22 · DEMOBILIZATION AND THE GI BILL
content_text('Demobilization, and the bill that caught it',
             ['More than 12 million Americans were in uniform when the war ended.',
              'Demobilization brought the forces home fast.',
              'The GI Bill gave unemployment pay while a veteran looked for work.',
              'It gave tuition for college and training, used by millions.',
              'Government-backed loans were offered for homes and businesses.'],
             "The GI Bill's three parts should be taught as one design, aimed at one fear: that twelve million veterans would come home to a country with no work for them, as veterans had after 1918, into a bonus march and a depression. Unemployment pay, the fifty two twenty club in veterans' shorthand, carried a veteran through the search for work. Tuition sent veterans to colleges and training schools in numbers that changed American higher education permanently, and reached men and women whose families had never sent anyone. Government backed loans for homes and businesses underwrote the suburbs and the small firms of the postwar boom. One limit belongs on this slide and not as an afterthought: the benefits were national in law and local in delivery, administered through segregated colleges, lending offices, and housing markets across much of the country, so Black veterans, who had served in a segregated army, drew on the bill through institutions that often narrowed what it could do for them. The bill transformed the country. It did not transform it equally, which is the unit question arriving in its final lesson.",
             kick='G · The country that came home', size=23)

# ------------------------------------------------------ 23 · ONE OF TWO GREAT POWERS
content_text('The country that came home',
             ['The economy had doubled its output during the war.',
              'Its cities were untouched, and its factories were intact and converted.',
              'Women were pushed toward home as veterans took the war jobs.',
              'Black veterans returned to the segregated South.',
              'The United States stood as one of two great powers in the world.'],
             "Close the section by holding the transformation and its distribution together, the way the reading does. The economic fact is plain: war production had doubled the country's output, ended mass unemployment, and left American factories the only great industrial plant in the world untouched by bombing, at the moment Europe and Japan faced rebuilding from ruins. The social facts cut across it. Women who had been recruited into shipyards and aircraft plants were pushed toward home as veterans reclaimed the jobs, though many stayed in paid work and the wartime years had changed what could be asked of them and by them. Black veterans came home with a service record, a claim, and in the South a segregated order waiting for them, and the claims they pressed belong to the next era of this course. And over everything stood the new standing: two great powers remained, the United States and the Soviet Union, allies in August and already divided over the Europe between them. That division is where the synthesis slide takes up the lesson.",
             kick='G · The country that came home', size=23)

# ------------------------------------------------------ 24 · AT A GLANCE
s = slide(NAVY)
kicker(s, 'The war\u2019s end at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Planned, decided, signed, counted', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Planned', 'Yalta, February 1945; Potsdam, July 1945', 'Germany divided; the United Nations founded; Europe argued over'),
        ('Decided', 'Trinity, July 16; the Interim Committee over the Franck Report', 'Use without a demonstration; the ultimatum unanswered'),
        ('Signed', 'Hiroshima, Soviet entry, Nagasaki; the Missouri, September 2', 'Japan accepts Potsdam; the Emperor kept, under the Supreme Commander'),
        ('Counted', 'About 405,000 American dead; the world, an estimated 60 to 85 million', 'Twelve million brought home into the GI Bill')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.2, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.25, yy + 0.05, 5.1, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.55, yy + 0.05, 3.9, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the closing table of the guided notes, The War's End at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. Planned: the conferences, Yalta in February 1945 sketching the settlement, Germany in occupation zones, the United Nations, Soviet entry pledged against Japan; Potsdam in July, occupation policy set and Europe's future already argued over. Decided: the weapon, tested at Trinity on July 16, its makers' demonstration proposal set aside for the Interim Committee's recommendation, and the ultimatum of July 26 left unanswered by Tokyo. Signed: the August sequence, Hiroshima, Soviet entry, Nagasaki, the emperor's intervention, and the Instrument of Surrender aboard the Missouri on September 2. Counted: about 405,000 American dead, worldwide deaths estimated between 60 and 85 million, and more than twelve million in uniform brought home into the GI Bill. Grade the table on the presence of the estimates stated as estimates.")

# ------------------------------------------------------ 25 · VOCAB A
vocab('Words for the conferences and the program',
      [('Yalta Conference', 'Roosevelt, Churchill, and Stalin, February 1945: the settlement planned'),
       ('Potsdam Conference', 'Truman, Churchill, and Stalin, July 1945: occupation and argument'),
       ('Potsdam Declaration', 'the ultimatum of July 26, 1945: surrender, or prompt and utter destruction'),
       ('Manhattan Project', 'the secret program that built the first atomic bombs')],
      "These definitions match the guided notes, and the notes carry them in full, word for word. Yalta Conference: the meeting of Roosevelt, Churchill, and Stalin in February 1945 that planned the postwar settlement, including the United Nations and Soviet entry into the war against Japan. Potsdam Conference: the meeting of Truman, Churchill, and Stalin in July 1945 in occupied Germany, where the leaders set occupation policy and argued over Europe's future. Potsdam Declaration: the Allied ultimatum of July 26, 1945 demanding Japan's unconditional surrender and warning of prompt and utter destruction if Japan refused. Manhattan Project: the secret American program that built the first atomic bombs, employing more than 100,000 people at sites across the country. Three of the four are conferences and a document, one is a program, and students should notice that the lesson's vocabulary is a vocabulary of decision making: men at tables, words on paper, and a weapon built in secret behind both.")

# ------------------------------------------------------ 26 · VOCAB B
vocab('Words for the weapon and the homecoming',
      [('atomic bomb', 'explosive power from splitting atoms, beyond any ordinary explosive'),
       ('demobilization', 'bringing the armed forces back to civilian life'),
       ('GI Bill', 'the Act of 1944: pay, tuition, and backed loans for veterans')],
      "Three more terms, in the guided notes wording, carried in these notes in full, word for word: atomic bomb: a bomb whose explosive power comes from splitting atoms, releasing energy on a scale no ordinary explosive can match; demobilization: the process of bringing armed forces back to civilian life and reducing a wartime military to peacetime size; GI Bill: the Servicemen's Readjustment Act of 1944, which gave veterans unemployment pay, tuition for college and training, and government-backed home and business loans. Pair the last two for memory, as the lesson taught them: demobilization is the process, the movement of more than twelve million people out of uniform in about two years; the GI Bill is the instrument that caught that movement and turned it, for millions of families, into schooling, houses, and businesses rather than into unemployment lines. The first term belongs to August; the other two belong to everything August made necessary at home.")

# ------------------------------------------------------ 27 · CLOSING SYNTHESIS
s = slide(NAVY)
kicker(s, 'Closing synthesis')
text(s, 0.9, 1.35, 11.5, 1.1, 'Where this unit ends', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 2.6,
     ["The alliance that won the war was already divided over Europe's future, and the weapon unveiled in August 1945 made that division dangerous in a new way.",
      "The policy that answered the division belongs to the Cold War unit. This unit ends at the Missouri, with the division named and the weapon on the record."],
     size=23, color=POWDER, leading=1.3)
notes(s, "Close the unit by drawing its boundary line out loud, and refuse, as the lesson has refused throughout, to teach past it. What this unit owns is the war: how it was entered, mobilized for, fought on two oceans, tested against the democracy it claimed to defend, and ended. What the ending left standing is named in the synthesis. The Grand Alliance was a wartime instrument, and by Potsdam its members were already reading their own agreements in two ways over the future of Europe. Into that division, in August 1945, came a weapon that changed what a division between great powers could do. The policy that answered it, the strategy, alliances, and aid programs of the early Cold War, belongs to the next unit, and it is not taught here, not even in outline. Students should leave able to state the boundary as a finding of this lesson rather than as a gap in it: the conferences and the bomb are this unit's closing material, and the argument they opened is the next unit's first question.")

# ------------------------------------------------------ 28 · CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ["How did the war end, what did the atomic bomb decide and leave undecided, and what country came home from the war? Judge the decision from the documents of 1945, and state the strongest argument against your own verdict."],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Decision File: the Potsdam Declaration, the Franck Report, the invasion file, the statement, the surrender'),
        ('Notebook', 'Notebook page: the questions of 1945, what the documents show, what was decided'),
        ('Quick check', 'The Signing Aboard the Missouri: the instrument, the sequence, the emperor\u2019s place'),
        ('Writing', 'Judging the Atomic Decision: a verdict from the file, the counterargument answered, the TPSP DBQ as its linked extension')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the Potsdam demand and warning, the Franck proposal and what replaced it, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close the unit by handing the judgment to the students, which is what this lesson exists to do. The activity, The Decision File, gives them the July and August file in order, the Potsdam Declaration, the Franck Report, a labeled summary of the invasion planning read against Iwo Jima and Okinawa, Truman's statement of August 6, and the Instrument of Surrender, and asks for the memorandum they would have sent on August 1, compared against the record. The notebook page charts the questions of 1945. The quick check reads the Missouri signing photograph and tests the instrument and the sequence. The writing task, Judging the Atomic Decision, requires a verdict from the file with the strongest counterargument stated and answered; teachers may extend it with The Primary Source Project premium DBQ 12, Was the U.S. Right to Drop the Atomic Bomb, a linked resource not reproduced here. The exit ticket has three parts: the Potsdam demand and warning, the Franck proposal and what was decided instead, and the lesson question answered with the reckoning figures stated as estimates. The review day and the unit test follow from here.")

dc.save(OUT)
