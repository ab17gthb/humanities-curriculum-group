#!/usr/bin/env python3
"""World War II Lesson 7 deck, "The Holocaust and the War's Crimes,"
built on the shared deck system: image-led slides, fragments only on
screen, comprehensive speaker notes, full lesson + vocabulary coverage.
Taught with documentary sobriety: photographs appear only where they are
under discussion, captioned from the holding record.
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
OUT = os.path.join(HERE, '..', 'lesson-07-slides.pptx')

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
text(s, 0.9, 5.30, 11.5, 0.4, 'WORLD WAR II · LESSON 7', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.64, 11.9, 1.0, 'The Holocaust and the War\u2019s Crimes', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.52, 11.5, 0.45, 'What was done, what was known, and what was answered', size=17, color=POWDER)
text(s, 0.9, 7.02, 11.9, 0.4, 'Prisoners in the barracks at Buchenwald, photographed by Private H. Miller, United States Army, April 16, 1945.', size=11, color=POWDER)
notes(s, "Set the standard for this lesson in the first minute. It is taught from the record: laws, cables, passenger lists, trial transcripts, and photographs that are evidence, each one captioned with what it shows, who made it, and when. The photograph on this slide shows prisoners in the barracks at Buchenwald concentration camp near Weimar, Germany, photographed by Private H. Miller of the United States Army on April 16, 1945, five days after the camp was liberated. It appears here as evidence and returns in Section F, where the class takes up liberation directly. No photograph in this lesson is used as decoration. The lesson follows a sequence students should be able to rebuild by the end of the hour: persecution carried out in law, refugees refused, murder carried out by shooting units and then by killing centers, knowledge that reached the Allied governments while the murders were happening, a rescue effort that came late, liberation documented on purpose, and a trial that answered the crimes with evidence. The figures in this lesson are stated at the precision the record supports, and estimates are labeled as estimates.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.7, 11.5, 3.6, [[('What did Nazi Germany do to the Jews of Europe and to others it marked for persecution and death, and what did the world know, do, and answer?', {})]],
     size=40, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.5)
text(s, 0.92, 5.75, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the Second World War transform the United States, and how far did the country live up to the democracy it claimed to defend?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Read the lesson question slowly, because it has four verbs and the lesson is organized by them. What did Nazi Germany do: that is the persecution, the ghettos, the shooting squads, and the Final Solution. What did the world know: that is the reports that reached London and Washington from 1942 and the public condemnation that December. What did the world do: that is the closed doors of 1938 and 1939, set against the War Refugee Board of 1944. And what did the world answer: that is liberation documented on a general's orders and a trial at Nuremberg conducted from the Germans' own records. The unit question runs beneath as the frame. A country fighting in democracy's name turned a refugee ship away in 1939 and built its rescue agency in 1944. Students should hold both of those facts at once by the end of the lesson, because the documents hold both.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Persecution, murder, knowledge, judgment', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'Persecution in Law and Violence', 'Citizenship stripped, then open violence'),
        ('B', 'The Doors That Stayed Shut', 'Evian, and the St. Louis turned away'),
        ('C', 'Ghettos and the Shooting Squads', 'Warsaw confined; more than a million shot'),
        ('D', 'The Final Solution', 'Deportations to killing centers from 1942'),
        ('E', 'Knowledge and Response', 'Reports by 1942; rescue agency in 1944'),
        ('F', 'Liberation and the Camera', 'Ohrdruf documented on Eisenhower\u2019s order'),
        ('G', 'Judgment at Nuremberg', 'A trial proved from the Germans\u2019 own records')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Sections A and B cover the years before the war in Europe: persecution written into German law, violence in November 1938, and the refusal of the world's governments to admit the people trying to escape. Sections C and D cover the murder itself, first in the ghettos and the open air shootings after the invasion of the Soviet Union, then in the killing centers from 1942. Section E asks what was known and what was done, and it is the section where the lesson slows down, because the dates in it carry the argument. Sections F and G cover the spring of 1945 and the answer that followed: documentation ordered deliberately, and a trial. The summary table at the end of the guided notes, The Record at a Glance, asks students to rebuild this map in their own words.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', 'Persecution in Law and Violence',
             'Exclusion written into law first, then violence in the open.',
             "Section A covers the years 1933 to 1938, and its point is that the persecution began in law, in public, before it became mass murder. Antisemitism, in the vocabulary definition students will copy later, is prejudice against, hatred of, or discrimination against Jews as a religious or ethnic group. In Nazi Germany it was not a private attitude. It was state doctrine, carried out by a government through statutes, decrees, and police. That distinction does real work in this lesson. Students sometimes imagine the persecution as the work of mobs alone. The record shows a legislature, a civil service, and a court system doing it in orderly steps: posts taken, businesses boycotted, students barred, citizenship removed, marriage forbidden. The violence of Kristallnacht came after five years of law, and it came with the state's forces in the street. Teach the sequence in that order, law first and violence second, because the activity's first station asks students to judge exactly that relationship.")

# ------------------------------------------------------ 5 A LAWS
content_text('Citizenship taken by statute',
             ['1933: Jews driven from public life and office',
              'Nuremberg Laws, September 1935',
              'Citizenship stripped; intermarriage forbidden',
              'Later decrees reached schools, work, and property'],
             "In the guided notes definition, the Nuremberg Laws are the German laws of 1935 that stripped Jews of citizenship and forbade marriage between Jews and non-Jewish Germans. Give students the mechanism, not only the outcome. The Reich Citizenship Law divided the population into citizens and subjects and reserved citizenship to people of German or related blood. Jews became subjects in the country where many of their families had lived for centuries. A companion law forbade marriage between Jews and non-Jewish Germans. The years around the laws belong in the notes as well: in 1933 Jewish officials lost their posts, Jewish shops faced an official boycott, and Jewish students met barriers at schools and universities. Later decrees extended the exclusion to professions and property. Nothing in this section was secret, and nothing in it required a war. It was the peacetime law of a state, published and enforced, three years before the refugee crisis of the next section and six years before the invasion of Poland.",
             kick='A · Persecution in law and violence')

# ------------------------------------------------------ 6 A KRISTALLNACHT
content_text('November 1938: violence in the open',
             ['Kristallnacht, November 9 to 10, 1938',
              'Synagogues burned across Germany',
              'Jewish shops smashed',
              'About 30,000 Jewish men arrested',
              'Many Jews now tried to leave Germany'],
             "Kristallnacht is the point where the persecution in law became persecution in the street, and students should date it precisely: the night of November 9 to 10, 1938. Nazi forces burned synagogues across Germany, smashed Jewish shops, and arrested about thirty thousand Jewish men, who were sent to concentration camps. The name comes from the broken glass of the shop windows, and teachers should say plainly that the event was organized violence by the state's forces and their supporters, not a spontaneous riot. The consequence that carries the lesson forward is in the last line on this slide. After November 1938, many German Jews tried to leave Germany. They had papers to prepare, property the state was taking, and families to move. What they met abroad is the subject of the next section, and the contrast is the lesson's first hard fact: the danger was public, reported in newspapers around the world, and the doors were still closed. Keep that sentence in view as the class moves to Section B.",
             kick='A · Persecution in law and violence')

# ------------------------------------------------- 7 SECTION B DIVIDER
divider_text('Section B', 'The Doors That Stayed Shut',
             'Evian in 1938, and a ship turned away in 1939.',
             "Section B is about the response of other governments while escape was still possible, and it should be taught as a record of decisions, each one dated and each one made by named governments. In July 1938 the democracies met at Evian in France, at the initiative of the United States, to discuss Jewish refugees. The result is stated in the reading in one sentence students should copy: nation after nation expressed sympathy and then explained why it could take few or none. The United States kept its immigration quotas fixed. Eleven months later a single ship tested those decisions, and its passenger list survives, which is why the St. Louis can be taught passenger by passenger rather than as a symbol. The section closes with a finding from later research. Teach it as research, with its source named, because the difference between what was decided in 1939 and what is known now about the outcome is itself part of the evidence.")

# ------------------------------------------------------ 8 B ST LOUIS
content_text('The St. Louis, May to June 1939',
             ['937 Jewish passengers sailed from Hamburg',
              'Cuba refused most of them entry',
              'The United States and Canada turned the ship away',
              'The ship returned to Europe',
              'About a quarter of its passengers were later murdered'],
             "Work through the record in order, because the order is the teaching. The St. Louis sailed from Hamburg in May 1939 with 937 Jewish passengers, most of them holding landing permits for Cuba. Cuba invalidated most of the permits, and only a small number of passengers were allowed to land. The ship stood off the coast of Florida, and the United States did not admit the passengers. Canada refused them as well. The ship returned to Europe, where Great Britain, France, Belgium, and the Netherlands divided the passengers among them. Then give the class the later finding, attributed as the reading attributes it: later research, conducted by the United States Holocaust Memorial Museum, established that about a quarter of the passengers were murdered in the Holocaust, most of them among those sent to countries Germany later occupied. Students should write the figure of 937 and the finding of about a quarter into section B of the notes, with the word research attached to the second one.",
             kick='B · The doors that stayed shut')

# ------------------------------------------------- 9 SECTION C DIVIDER
divider_text('Section C', 'Ghettos and the Shooting Squads',
             'Confinement in the cities of Poland, and murder in the open in the east.',
             "Section C covers the first stage of mass murder, and it has two parts that students often merge. The first is confinement: after the invasion of Poland in 1939, the Germans forced Jews into ghettos in the occupied cities. The second is the open air shootings that followed the invasion of the Soviet Union in June 1941, carried out by the Einsatzgruppen behind the advancing army. Keep the two apart in the notes, because they were different instruments used in different places, and the killing centers of Section D were a third. A note on photographs belongs here as well. This lesson uses no photograph of the ghettos. The best known ghetto photographs were taken by German personnel during the destruction of the Warsaw ghetto in 1943 and show prisoners being arrested at gunpoint. They are evidence in the historical record. They are not used as illustration in this lesson, and the ghettos are taught from the documented record of population, walls, hunger, and disease.")

# ------------------------------------------------------ 10 C GHETTOS
content_text('Confined behind walls',
             ['Ghettos imposed in occupied Poland from 1939',
              'Warsaw, the largest, held more than 400,000 people',
              'Crowded rooms, rationed food, sealed walls',
              'Hunger and disease killed tens of thousands'],
             "In the guided notes definition, a ghetto is a section of a city where Jews were forced to live in crowded and starved conditions under German occupation. Name the conditions concretely, because the definition's two adjectives carry the section. Crowded: the Warsaw ghetto, the largest, held more than four hundred thousand people in a small district of the city, sealed behind walls in November 1940. Starved: the German authorities set food rations for the ghetto far below what a person needs to live, and smuggling food became a crime punished by death. Hunger and disease killed tens of thousands of people in the Warsaw ghetto before the deportations to the killing centers began in the summer of 1942. Students should understand the ghetto as an instrument, not a backdrop. Confinement concentrated the victims, weakened them, and made the later deportations a matter of moving people from a sealed district to a railway station. The Warsaw figure, more than four hundred thousand, belongs in section C of the notes.",
             kick='C · Ghettos and the shooting squads')

# ------------------------------------------------------ 11 C SQUADS
content_text('Murder in the open, town by town',
             ['Einsatzgruppen followed the army into the Soviet Union, 1941',
              'Victims shot at pits and ravines',
              'Babi Yar, outside Kyiv: nearly 34,000 Jews in two days',
              'September 29 to 30, 1941'],
             "The Einsatzgruppen were special units that followed the German army into the Soviet Union after the invasion of June 1941, ordered to murder Jews and others in the occupied territory. Their method was the opposite of concealment. Victims were taken from their towns to pits, ravines, and forests at the edge of settlement and shot there, town by town, in operations the units reported in writing to Berlin. The largest single action of this stage took place at Babi Yar, a ravine outside Kyiv, where nearly thirty four thousand Jews were murdered in two days, September 29 and 30, 1941. The figure comes from the units' own reports, which is a point worth making in a lesson built on records: the count of the shootings rests substantially on documents the perpetrators themselves filed. The next slide gives the total for the shooting campaign as a whole. Students should attach Babi Yar's name, place, dates, and figure to section C before the total appears, so the total is understood as a sum of named places.",
             kick='C · Ghettos and the shooting squads')

# ------------------------------------------------------ 12 STAT SQUADS
stat('More than 1 million', 'people murdered by the shooting units and those who worked with them',
     'The Einsatzgruppen campaign in the occupied Soviet Union, 1941 to 1943 · Counted in part from the units\u2019 own reports',
     "Let this figure sit before explaining it. More than one million people were murdered by the shooting units and those who worked with them in the occupied Soviet Union. The victims were overwhelmingly Jews, murdered because they were Jews, together with Roma, Soviet officials, and others the units were ordered to kill. Historians built this count from the units' own situation reports, from German records, and from the graves investigated after the war, and the lesson states it as a floor: more than one million, not a rounded claim of exactly one million. Connect the figure backward to the previous slide. Babi Yar's nearly thirty four thousand in two days was one action among hundreds. A class that understands how a total like this is assembled, report by report and place by place, is better defended against the later claim that the numbers were invented. That defense is one reason this lesson teaches the documentation stage, Section F, with the same care as the murder itself.",
     kick='C · Ghettos and the shooting squads')

# ------------------------------------------------- 13 SECTION D DIVIDER
divider_text('Section D', 'The Final Solution',
             'From 1942, deportation by rail to killing centers built for murder.',
             "Section D covers the stage the Nazi government called the Final Solution, and the phrase should be introduced as the perpetrators' own term, defined precisely in the vocabulary students will copy at the end of the lesson. From 1942 the program ran on rails. Jews were deported from the ghettos and from countries across Europe to killing centers built in occupied Poland, and most arrivals were murdered within hours. The decision and coordination belong to January 1942, when officials met at Wannsee in Berlin to organize the deportations across government agencies. One caution belongs in the teaching here. The killing did not begin at Wannsee. The shootings of Section C were already six months old, and the first killing center, at Chelmno, had begun operating in December 1941. What changed in 1942 was scale and system: murder organized as a European transportation and camp program. The section closes with the full count, stated as the record supports it, and with the other peoples the murder reached.")

# ------------------------------------------------------ 14 D CENTERS
content_text('Deportation by rail to the killing centers',
             ['Coordination at Wannsee, January 1942',
              'Auschwitz-Birkenau, Treblinka, Belzec, Sobibor, Chelmno',
              'Built in occupied Poland',
              'Most arrivals murdered in gas chambers within hours'],
             "In the guided notes definition, a death camp is one of the camps built by Nazi Germany in occupied Poland where Jews and others were murdered, most in gas chambers on arrival. Walk the geography first. The centers named on this slide stood in occupied Poland, close to the largest Jewish populations of Europe and to the rail lines that crossed it. Trains arrived from the ghettos and from France, the Netherlands, Greece, Hungary, and across the continent. At most of these camps the majority of arrivals were murdered in gas chambers within hours of arrival. Treblinka, Belzec, and Sobibor existed for this purpose alone and were dismantled after their work, in 1943. Auschwitz-Birkenau was both a killing center and a vast camp complex, where some arrivals were selected for labor and the rest murdered. Students should note the distinction the reading keeps: these were not camps where people died of conditions, though conditions killed many. They were built for murder, and the trains ran on schedule until the autumn of 1944.",
             kick='D · The Final Solution', size=24)

# ------------------------------------------------------ 15 STAT SIX MILLION
stat('Six million', 'Jews murdered in the Holocaust',
     'About two thirds of the Jewish population of Europe · The count the record supports, built from German records, demographic study, and the documentation gathered after the war',
     "State the count the way the reading states it, because the wording is the lesson's standard for figures. The record supports a count of six million Jews murdered, about two thirds of the Jewish population of Europe. This is not a figure of speech. It was assembled after the war from the perpetrators' own records, including deportation lists and camp documents, from the demographic comparison of Europe's Jewish population before and after the war, and from the documentation gathered for the trials. Scholars working independently have arrived at totals in the same range, and six million is the count the evidence supports. Students will meet attempts to shrink this number, and the strongest answer is the one this lesson has been building: the number stands on records, many of them German, that can be examined. The guided notes definition of the Holocaust carries this count inside it, and students will copy it in the vocabulary section. The next slide names the millions murdered alongside the Jews of Europe.",
     kick='D · The Final Solution')

# ------------------------------------------------------ 16 D OTHERS
content_text('The murder did not stop with Jews',
             ['Roma murdered in large numbers',
              'People with disabilities murdered in the T4 program',
              'Polish and Soviet civilians killed in great numbers',
              'More than three million Soviet prisoners of war died in German custody'],
             "The guided notes definition of the Holocaust ends with the murder of millions of others, and this slide teaches that clause group by group. Roma were persecuted across Europe and murdered in large numbers, including at Auschwitz-Birkenau. People with disabilities were murdered in the program called T4, which began in 1939, before the killing centers, and in which German doctors and officials organized the killing of patients in institutions; its personnel and its methods later moved to the camps. Polish and Soviet civilians were killed in great numbers in the occupied east, in reprisals, starvation policy, and the destruction of villages. More than three million Soviet prisoners of war died in German custody, most of them deliberately starved in open air enclosures in the winter of 1941 and 1942, a crime against prisoners that belongs in the same record. Teach the distinctions along with the total. Each group was targeted under its own orders, and the lesson names them separately because the record does.",
             kick='D · The Final Solution', size=23)

# ------------------------------------------------- 17 SECTION E DIVIDER
divider_text('Section E', 'Knowledge and Response',
             'What the Allied governments knew, when they knew it, and what followed.',
             "Section E is the lesson's examination of the bystander governments, and it runs on dates, so keep the chronology on the board as you teach it. August 1942: a telegram reporting a German plan to murder the Jews of Europe reached London and Washington. December 1942: the Allied governments publicly condemned the extermination. January 1944: the United States created the War Refugee Board, the first agency whose task was rescue. The distance between the second date and the third is sixteen months, and measuring that distance from documents, without inflating it or explaining it away, is the work of the writing task. One debate belongs in this section and should be taught as a debate: whether Allied bombers should have struck the rail lines leading to the camps, or the camps themselves, in 1944. Historians argue it from the documents on both sides. The lesson states the debate and does not settle it, and students should hear that restraint as part of the method, not as an omission.")

# ------------------------------------------------------ 18 E RESPONSE
content_text('Condemnation in 1942, a rescue agency in 1944',
             ['August 1942: a telegram reported the plan to murder Europe\u2019s Jews',
              'December 1942: the Allies publicly condemned the extermination',
              'By 1944, escaped prisoners and couriers had confirmed the killing centers',
              'January 1944: the War Refugee Board created',
              'Wallenberg in Budapest: papers and safe houses saved thousands'],
             "Teach this slide as a sequence and resist summarizing it into a verdict, because the students' writing task asks them to judge it. The reports arrived while the murders were happening: the August 1942 telegram reported a plan to exterminate the Jews of Europe, and that December the Allied governments condemned the extermination in public, by name. Confirmation deepened through 1943 and 1944, brought by escaped prisoners and by Polish couriers who reached London and Washington. The rescue machinery arrived in January 1944, when the president created the War Refugee Board after Treasury officials reported that the government had blocked rescue for years. In its last year the Board funded rescue, pressed neutral countries, and supported Raoul Wallenberg in Budapest, whose protective papers and safe houses saved thousands of Hungarian Jews. The Board's own postwar estimate, tens of thousands saved, is an estimate and is taught as one. What the documents measure is the gap: condemnation in 1942, an agency in 1944, and deportations that continued between and after both dates.",
             kick='E · Knowledge and response', size=23)

# ------------------------------------------------- 19 SECTION F DIVIDER
divider_photo('buchenwald-port.jpg', 'Section F', 'Liberation and the Camera',
              ['Prisoners in the barracks at Buchenwald,', 'photographed by Private H. Miller,', 'United States Army, April 16, 1945.'],
              "The photograph on this slide is the first of two in this lesson, and it appears here because it is under discussion, not as illustration. It shows prisoners in the barracks at Buchenwald concentration camp near Weimar, Germany, in the multi-tier bunks where they slept. It was taken by Private H. Miller of the United States Army on April 16, 1945, five days after American forces liberated the camp on April 11. Photographs like this one were made deliberately, by army photographers working to a record, and they were published in newspapers and shown in newsreels within weeks. Section F covers the spring of 1945, when Allied armies overran the camps and found the dead and the starving together, and it covers the decision made at the first camp the Americans reached: to document what was found, to bring witnesses, and to place the evidence beyond later dispute. That decision, and the general who made it, are the next slide.",
              title_size=38)

# ------------------------------------------------------ 20 F OHRDORF
content_photo('ohrdruf-port.jpg', 'Eisenhower at Ohrdruf: document it',
              ['First camp reached by American forces, April 4, 1945',
               'Eisenhower toured Ohrdruf on April 12',
               'He ordered the camp documented',
               'Congress members and journalists brought to see it',
               'His cable: first-hand evidence against a future charge of propaganda'],
              "The photograph shows General Dwight D. Eisenhower and other senior United States Army officers at the Ohrdruf camp near Gotha on April 12, 1945, viewing prisoners who had been killed during the evacuation of the camp. The photographer is not credited in the holding record, which is held by the United States Holocaust Memorial Museum as Photograph 04649, and students should hear the caption stated with that limit included. Ohrdruf was the first camp American forces reached, on April 4. Eisenhower toured it eight days later and then acted as a witness on purpose. He ordered the camp documented, brought members of Congress and journalists to see it, and cabled Washington the sentence the activity prints in full: he had made the visit deliberately, in order to be in position to give first-hand evidence of these things if ever there developed a tendency to charge the allegations merely to propaganda. The cable is Station 3 of the activity, and it is the document this photograph belongs to.",
              kick='F · Liberation and the camera')

# ------------------------------------------------- 21 SECTION G DIVIDER
divider_photo('nuremberg-port.jpg', 'Section G', 'Judgment at Nuremberg',
              ['Defendants at the Nuremberg War Crimes Tribunal,', 'Palace of Justice courtroom, November 27, 1945.', 'United States military photograph.'],
              "Section G covers the reckoning. The photograph shows the defendants in the Palace of Justice courtroom at Nuremberg on November 27, 1945, in a United States military photograph held by the Harry S. Truman Library. The section's central fact is a choice. The victorious Allies held the surviving leaders of Nazi Germany prisoner in 1945 and could have punished them without process, as occupying powers have done in other wars. They chose a trial instead: an international tribunal at Nuremberg, with charges stated in advance, evidence presented in open court, and defense counsel heard. Justice Robert H. Jackson, the chief American prosecutor, opened the case on November 21, 1945, and his opening statement is Station 5 of the activity and the second verbatim document of this lesson. The trials ran through 1946. The tribunal convicted most of the defendants and sentenced twelve to death. Japanese leaders were tried in the same period for their own crimes, among them the Bataan Death March of 1942, in which thousands of American and Filipino prisoners died. The section closes the lesson's sequence: persecution, refusal, murder, knowledge, documentation, judgment.")

# ------------------------------------------------------ 22 G NUREMBERG
content_text('Proof from the Germans\u2019 own records',
             ['International tribunal at Nuremberg, 1945 to 1946',
              'Jackson opened the prosecution, November 21, 1945',
              'The case proved by books, records, photographs, and films',
              'Most defendants convicted; twelve sentenced to death'],
             "Justice Robert H. Jackson's opening statement makes two claims students should be able to separate. The first is about method. He told the tribunal that there was no count in the indictment that could not be proved by books and records, because the Germans had kept meticulous records and had arranged to be photographed and filmed in action. The prosecution's evidence was, in large part, the perpetrators' own documentation, the same habit of record keeping this lesson has relied on from the Nuremberg Laws onward. The second claim is about the choice of a trial itself. Four nations, he said, flushed with victory and stung with injury, stayed the hand of vengeance and voluntarily submitted their captive enemies to the judgment of the law, which he called one of the most significant tributes that Power has ever paid to Reason. Students read this passage in full at Station 5 of the activity, and the exit ticket asks them to use it. Teach both claims here so the station work can go deeper.",
             kick='G · Judgment at Nuremberg', size=24)

# ------------------------------------------------------ 23 G WAR CRIMES
content_text('War crimes, tried as crimes',
             ['War crimes: violations of the laws of war',
              'The murder of prisoners and civilians among them',
              'Soviet prisoners starved in German custody',
              'The Bataan Death March, 1942',
              'Individuals, not nations alone, held responsible'],
             "Close the content with the term the trials applied. In the guided notes definition, war crimes are violations of the laws of war, such as the murder of prisoners and civilians, for which individuals were tried after the war. The definition's examples reach back through this lesson and the ones before it. The murder of civilians is the record of Sections C and D. The murder of prisoners is the record of the more than three million Soviet prisoners of war who died in German custody, most of them deliberately starved, and of the Bataan Death March of April 1942, in which thousands of American and Filipino prisoners died on a forced march after the fall of the Philippines, a crime tried by an American military commission. The principle Nuremberg established, and the one students should carry out of the lesson, is that these acts were crimes committed by individuals who could be named, charged, and tried on evidence, not misfortunes of war that no one authored. That principle is the answer in the lesson question's final verb.",
             kick='G · Judgment at Nuremberg', size=24)

# ------------------------------------------------------ 24 VOCAB A
vocab('Words for the persecution',
      [('antisemitism', 'prejudice against, hatred of, or discrimination against Jews as a religious or ethnic group'),
       ('Nuremberg Laws', 'the German laws of 1935 that stripped Jews of citizenship and forbade marriage between Jews and non-Jewish Germans'),
       ('Holocaust', 'the state-sponsored persecution and murder of six million European Jews by Nazi Germany and its collaborators, together with the murder of millions of others, including Roma, people with disabilities, and Soviet prisoners of war'),
       ('ghetto', 'a section of a city where Jews were forced to live in crowded and starved conditions under German occupation')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. The first term is antisemitism: prejudice against, hatred of, or discrimination against Jews as a religious or ethnic group. Nuremberg Laws: the German laws of 1935 that stripped Jews of citizenship and forbade marriage between Jews and non-Jewish Germans. Holocaust: the state-sponsored persecution and murder of six million European Jews by Nazi Germany and its collaborators, together with the murder of millions of others, including Roma, people with disabilities, and Soviet prisoners of war. Note what the Holocaust definition carries inside it: the count of six million, the collaborators who took part, and the other peoples murdered. The fourth term is ghetto: a section of a city where Jews were forced to live in crowded and starved conditions under German occupation. The two adjectives in that definition, crowded and starved, were policy, set by ration scales and sealed boundaries, and Section C taught them as such.")

# ------------------------------------------------------ 25 VOCAB B
vocab('Words for the murder and the reckoning',
      [('Final Solution', 'the Nazi program to murder every Jew in Europe, carried out by shooting units, deportations, and killing centers from 1941 to 1945'),
       ('death camp', 'one of the camps built by Nazi Germany in occupied Poland where Jews and others were murdered, most in gas chambers on arrival'),
       ('war crimes', 'violations of the laws of war, such as the murder of prisoners and civilians, for which individuals were tried after the war')],
      "Three more terms, again matching the guided notes exactly. Final Solution: the Nazi program to murder every Jew in Europe, carried out by shooting units, deportations, and killing centers from 1941 to 1945. The definition names the program's three instruments in the order this lesson taught them, and students should notice that the phrase itself was the perpetrators' term, adopted by historians because the documents use it. The second term is death camp: one of the camps built by Nazi Germany in occupied Poland where Jews and others were murdered, most in gas chambers on arrival. The location and the method are both inside the definition, and both were tested in the reading questions. The third term is war crimes: violations of the laws of war, such as the murder of prisoners and civilians, for which individuals were tried after the war. The last clause is the Nuremberg principle from Section G: individuals were tried, by name, on evidence.")

# ------------------------------------------------------ 26 GLANCE
s = slide(NAVY)
kicker(s, 'The record at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Five stages, one record', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Persecution', 'Laws of 1935; Kristallnacht, 1938', 'Public law and public violence'),
        ('Refusal', 'Evian, 1938; the St. Louis, 1939', 'Quotas fixed; a ship turned away'),
        ('Murder', 'Ghettos, shootings, killing centers', 'Six million Jews; millions of others'),
        ('Response', 'Condemnation, 1942; War Refugee Board, 1944', 'Knowledge first; rescue late'),
        ('Judgment', 'Ohrdruf documented, 1945; Nuremberg, 1945 to 1946', 'Evidence gathered, then a trial')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, The Record at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The five rows are the lesson's stages. Persecution covers the laws of 1935 and Kristallnacht, and what defines the stage is that both were public. Refusal covers Evian and the St. Louis, with the finding that about a quarter of the ship's passengers were later murdered. Murder covers the ghettos, the shooting units, and the killing centers, and its count is six million Jews and millions of others. Response pairs the two dates students must hold together, condemnation in December 1942 and a rescue agency in January 1944. Judgment covers Ohrdruf's documentation and the Nuremberg trial. Grade the table generously on wording and strictly on dates and pairing: each row must say what the record shows and what was known or done in response.")

# ------------------------------------------------------ 27 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['What did Nazi Germany do, and what did the world know, do, and answer? Argue it from the documents, and state no claim more strongly than its evidence supports.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Record and the Response: the laws, the St. Louis, the Ohrdruf cable, the War Refugee Board, and Jackson at Nuremberg'),
        ('Notebook', 'Notebook page: the record in five stages, with what was known and what was done'),
        ('Quick check', 'First-Hand Evidence: Eisenhower\u2019s cable read closely'),
        ('Writing', 'Knowledge and Response: the distance between the two, measured in dates')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the two provisions of the Nuremberg Laws, the record of the St. Louis, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning the lesson to its documents and handing it to the work. The activity, The Record and the Response, runs the five stations in the order of the record: a labeled summary of the Nuremberg Laws, a labeled summary of the St. Louis and the refugee record, Eisenhower's Ohrdruf cable printed word for word, a labeled summary of the War Refugee Board with its estimate labeled, and Jackson's opening statement printed word for word, ending in a timeline the students build themselves. The notebook page holds the five stages with what was known and what was done in separate columns. The quick check, First-Hand Evidence, tests close reading of the Ohrdruf cable. The writing task, Knowledge and Response, asks for the distance between knowledge and response measured in dates, and its rubric refuses claims the documents cannot carry in either direction. The exit ticket has three parts: the two provisions of the Nuremberg Laws, the record of the St. Louis with its later finding, and the lesson question answered in two or three sentences. The next lesson takes up the war's end.")

dc.save(OUT)
