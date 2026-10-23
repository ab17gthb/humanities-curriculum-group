#!/usr/bin/env python3
"""World War II Lesson 6 deck, "A War for Democracy? Exclusion, Internment, and Service,"
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
text(s, 0.9, 5.32, 11.5, 0.4, 'WORLD WAR II · LESSON 6', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'A War for Democracy?', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Exclusion, internment, and service: who could work, who could serve, who was imprisoned', size=17, color=POWDER)
notes(s, "The photograph shows members of the Mochida family awaiting an evacuation bus at Hayward, California, in May 1942, photographed by Dorothea Lange for the War Relocation Authority and held by the National Archives. Keep its tone in the room from the first minute. This lesson is about a contradiction, and it should be taught as one, from documents and figures rather than from slogans. The United States fought racist empires abroad while running a segregated army and a discriminating war economy at home, and it imprisoned about 120,000 people of Japanese ancestry, two thirds of them citizens, in the same years it asked the world to judge it as democracy's defender. Students will work both halves of that record today and will be asked at the end to hold them together in one judgment.")

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did a war fought in democracy\u2019s name test democracy at home, in who could work, who could serve, and who was imprisoned?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the Second World War transform the United States, and how far did the country live up to the democracy it claimed to defend?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "The lesson question names three tests, and students should hear all three before the first section begins. Who could work asks whether a worker could claim a war job without regard to race, and it is answered by Executive Order 8802 and the committee it created. Who could serve asks whether a serviceman could claim a combat role and advancement on ability, and it is answered by the segregated military and the records built inside it. Who was imprisoned asks the hardest question in the unit: whether citizenship itself protected a person from removal without a charge, and it is answered by Executive Order 9066, the camps, and Korematsu. The unit question runs beneath as the frame. By the end of the hour students should be able to give one documented fact for each of the three tests.")

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Claims gained, claims denied', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The war aims and the facts', 'Four Freedoms abroad, segregation at home'),
        ('B', 'The fight for war work', 'A threatened march, an executive order'),
        ('C', 'Double V', 'Victory abroad and victory at home'),
        ('D', 'Service in a segregated military', 'A million in uniform, units kept apart'),
        ('E', 'Removal and the camps', '120,000 removed, two thirds citizens'),
        ('F', 'Korematsu and the courts', 'The exclusion upheld, 1944'),
        ('G', 'The 442nd and the claims', 'A decorated unit, families in camps')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Sections A, B, and C build the claims: the stated aims, the order that opened war work, and the campaign that named the double demand. Section D gives the service record inside a segregated military. Sections E and F give the exclusion: the removal order and the camps, then the Supreme Court ruling that let the exclusion stand. Section G closes with the 442nd Regimental Combat Team and the open question the lesson title asks. Tell students the summary table at the end of their guided notes, Two Fronts at a Glance, asks them to rebuild exactly this map, with a gain and a limit in every row.")

# 4 A DIVIDER
divider_text('Section A', 'The War\u2019s Aims and the Country\u2019s Facts',
             'Four Freedoms on the record, and the record at home.',
             "Set the method for the whole lesson here. Students will judge the war years by comparing two documents that both belong to the United States government: the aims it announced and the arrangements it kept. The aims are on paper and dated. In January 1941 the president named four freedoms as the foundation of a just world, and in August 1941 the Atlantic Charter pledged self-determination for peoples. The arrangements are also on paper and dated: a segregated army, defense plants that refused Black applicants, and Southern elections that many Black citizens could not vote in. Neither half is a debating point. Each is a fact of the record, and the lesson's work is to keep both in view at once, because the people in the next sections lived under both at the same time.")

# 5 A CONTENT
content_photo('gothic-port.jpg', 'The aims, and the woman who cleaned the offices',
              ['Four Freedoms named, January 1941',
               'Atlantic Charter: self-determination for peoples',
               'A segregated army at home',
               'Defense jobs refused to Black workers',
               'Gordon Parks photographs Ella Watson, 1942'],
              "The photograph is Gordon Parks's American Gothic, taken in Washington in 1942 for a federal photography unit. Ella Watson cleaned offices in a federal building, and Parks posed her before a large American flag with a mop and a broom, restaging Grant Wood's famous painting with a Black working woman in place of its farm couple. Use the portrait to make section A concrete. The flag behind her is the same flag the Four Freedoms were announced under, and her job is the kind of job the federal city offered a Black woman in 1942 while its war plants argued over whether to hire Black machinists. Students should record both halves in section A of the notes: the aims with their dates, and the three facts that stood against them. The quick check returns to this photograph, so name the woman and her job aloud.",
              kick='A · The war aims and the facts')

# 6 B DIVIDER
divider_photo('randolph-port.jpg', 'Section B', 'The Fight for War Work',
              ['A. Philip Randolph, labor leader.', 'Portrait held by the National Archives.'],
              "The portrait, by Betsy Graves Reyneau and held by the National Archives, shows A. Philip Randolph, who led the Brotherhood of Sleeping Car Porters, the union of the Black men who staffed the Pullman sleeping cars. Randolph is the organizer at the center of this section, and students should understand his method before they meet the order it produced. He did not petition and wait. He set a date, the first of July 1941, and organized a march on Washington of Black workers demanding fair hiring in the defense boom, and he kept organizing while the administration asked him to call it off. The march was a claim made with numbers and a deadline. Section B follows what that pressure produced on June 25, 1941, six days before the march was to step off, and it asks students to weigh both what the order granted and what it could not enforce.",
              title_size=38)

# 7 B CONTENT
content_text('A march threatened, an order signed',
             ['Defense plants hired fast, and many refused Black applicants',
              'Randolph sets a march on Washington, summer 1941',
              'June 25, 1941: Executive Order 8802',
              'No discrimination in defense industries or government',
              'Randolph calls the march off'],
             "In the guided notes definition, Executive Order 8802 is President Roosevelt's order of June 1941 barring racial discrimination in defense industries and federal employment, issued under the threat of a protest march on Washington. Every part of that definition is tested, so teach it whole, including the cause. The order did not arrive as a gift. It arrived because an organized march with a date attached made refusal more costly than concession. Note what the order covered: defense industries and federal employment, which in 1941 meant the fastest growing jobs in the country. Note also its instrument, an executive order rather than a statute, which meant it bound federal contractors and agencies directly and could be issued without asking a Congress where Southern committee chairmen held the gates. Black employment in war plants rose through the war that followed.",
             kick='B · The fight for war work')

# 8 B CONTENT 2
content_text('A committee that could investigate, not compel',
             ['Fair Employment Practices Committee created, 1941',
              'It heard complaints of job discrimination',
              'It could investigate and publicize',
              'It could not compel a firm to hire',
              'Congress kept its funding short'],
             "In the guided notes definition, the Fair Employment Practices Committee is the federal committee created in 1941 to investigate complaints of job discrimination in war industries. Teach the committee as the lesson's first lesson in enforcement. A right on paper is worth what its machinery can do, and this machinery was deliberately light. The committee held hearings, took complaints, investigated, and published findings, and publicity did move some employers. It had no power to order a firm to hire a worker it had wronged, and Congress kept its appropriations short and its life uncertain. Students often treat Executive Order 8802 as a simple victory, and the record supports half of that reading. The other half is the limit, and the exit ticket's first question is built to check whether students carried both halves out of this section.",
             kick='B · The fight for war work', size=24)

# 9 C DIVIDER
divider_text('Section C', 'Double V',
             'Victory over fascism abroad, victory over racism at home.',
             "This section has no government document, and that is its point. The Double V campaign was a claim made by citizens through their own press, and it set the standard by which the gains in this lesson were judged at the time, by the people who had the most at stake in them. The campaign began in February 1942 in the Pittsburgh Courier, one of the leading Black newspapers in the country, after a reader's letter asked whether Black Americans should seek a double victory. The paper took the question up, printed an emblem, and other Black newspapers carried the campaign across the country. Students should hear the campaign as an argument about timing: not rights after the war as a reward for service, but rights during the war as one of its aims.")

# 10 C CONTENT
content_text('A bargain refused',
             ['Launched by the Pittsburgh Courier, February 1942',
              'Victory over fascism abroad',
              'Victory over racism at home',
              'Service given in full, at the same time',
              'Citizenship claimed as a war aim, not a reward'],
             "In the guided notes definition, the Double V campaign is the campaign led by Black newspapers from 1942 for victory over fascism abroad and victory over racism at home. Give students the slogan's structure, because the structure is the argument. The first V accepts the war and its service without reservation: Black Americans enlisted, worked the war plants, and bought the bonds. The second V names the price, stated openly rather than whispered: the defeat of racism at home, in hiring, in the services, and at the ballot box. What the campaign refused was sequence. The older bargain offered citizenship later, after service had been proven, and Double V answered that a democracy fighting for its life could not ask for the service now and date the citizenship for someday. That refusal is the standard the rest of this lesson is measured against.",
             kick='C · Double V')

# 11 D DIVIDER
divider_photo('tuskegee-port.jpg', 'Section D', 'Service in a Segregated Military',
              ['Airmen of the 332nd Fighter Group,', 'Ramitelli, Italy.'],
              "The photograph shows airmen of the 332nd Fighter Group at Ramitelli, Italy, the base from which the group escorted American heavy bombers over southern and central Europe. Section D holds a fact and a policy side by side. The policy was segregation: the armed forces kept their units separate by race, assigned most Black servicemen to service and labor units, and placed them under white officers as a rule. The fact is the record built inside that policy, by the Tuskegee Airmen in the air, by the 761st Tank Battalion on the ground in France and Germany, and by more than a million Black servicemen and women in every theater. Students should also record the wider service in this section: more than 350,000 women, Mexican American servicemen in large numbers, Native American code talkers, and more than half a million Jewish Americans.",
              title_size=38)

# 12 D CONTENT
content_text('Service given inside a segregated system',
             ['Most Black servicemen assigned to service and labor units',
              'Units segregated, officers white as a rule',
              'The 761st Tank Battalion fought across France and Germany',
              'Benjamin O. Davis Sr., first Black general, 1940',
              'Code talkers sent messages the enemy never broke'],
             "Work this slide as a roster of the whole service record, because the guided notes section D is built to hold all of it and the unit test draws on it. The system's design came first: segregation was policy, not accident, and assignment followed race before it followed ability. Against that design, set the names. Benjamin O. Davis Sr. became the first Black general in 1940, a promotion that changed one man's rank without changing the system under him. The 761st Tank Battalion landed in France in the autumn of 1944 and fought through to Germany. Native American code talkers, Choctaw in the earlier war's pattern and Navajo most famously in this one, sent radio messages in their own languages that Japanese intelligence never broke. Each record was made by people the system had rated in advance, and each record outlasted the rating.",
             kick='D · Segregated service', size=24)

# 13 D STAT
stat('1,000,000+', 'Black Americans served in uniform in the Second World War',
     'Most were assigned to service and labor units under white officers, in a military that kept its units segregated',
     "Let the figure sit before adding the condition attached to it. More than a million Black Americans served in uniform during the war, in the Army, the Navy, the Marines as that service slowly opened, and the Coast Guard. Scale alone does not tell the story, because the same sentence that carries the number carries its limit: most of those servicemen were assigned to service and labor units, unloading ships, driving trucks, and building roads, under white officers, in units kept segregated by policy. A smaller share reached combat roles, and that share built the records on the slides around this one. Ask students to write the number and the condition as one note, not two, because the lesson's argument lives in the joining. Service on this scale was a claim on citizenship that a million people had paid for in advance.",
     kick='D · Segregated service')

# 14 E DIVIDER
divider_photo('mochida-port.jpg', 'Section E', 'Removal: Executive Order 9066 and the Camps',
              ['The Mochida family awaiting the', 'evacuation bus, Hayward, May 1942.'],
              "Return to the title photograph and name it exactly: members of the Mochida family awaiting an evacuation bus at Hayward, California, in May 1942, photographed by Dorothea Lange for the War Relocation Authority, National Archives record 537505. The children wear identification tags meant to keep the family together during removal. Teach this section with the documentary sobriety the photographs themselves have. Nothing in it needs heightening. A presidential order, a set of posted exclusion notices, buses and trains, and ten guarded camps in the interior are the record, and the figures are plain: about 120,000 people removed, two thirds of them American citizens, no charges filed, no hearings held. Students should keep the legal point in view throughout: the people in this photograph were not accused of anything.",
              title_size=36)

# 15 E CONTENT
content_text('An order that named no group',
             ['Signed February 19, 1942, ten weeks after Pearl Harbor',
              'Commanders may exclude any persons from named areas',
              'The order stated no reason in its text',
              'The Army applied it to one ancestry group',
              'German and Italian ancestry brought no mass removal'],
             "In the guided notes definition, Executive Order 9066 is President Roosevelt's order of February 19, 1942 authorizing the military to exclude people from areas of the West Coast, the order under which Japanese Americans were removed from their homes. Read the operative passage in the activity closely, because its silence is the evidence. The order grants power whenever a commander deems action necessary or desirable, and it names no group, states no finding, and sets no test. The application supplied what the text omitted: the Western Defense Command used the power against people of Japanese ancestry alone, citizens and noncitizens alike, while German and Italian ancestry brought individual hearings rather than mass removal. Students should be able to say, in their own words, that the discrimination entered through the application of a neutral sounding order.",
             kick='E · Removal and the camps', size=24)

# 16 E STAT
stat('120,000', 'people of Japanese ancestry removed from the West Coast',
     'Two thirds of them were American citizens · They were held in ten guarded camps in the interior',
     "This is the figure the whole lesson turns on, and it should be spoken slowly and completely. About 120,000 people of Japanese ancestry were ordered out of their West Coast homes in the spring and summer of 1942. Two thirds of them were American citizens, most of them born in the United States, many of them children, like the children in the Mochida photograph with their identification tags. The government held them in ten guarded camps in the interior, behind barbed wire and under watchtowers, for much of the war. In the guided notes definition, internment is the forced confinement of a group of people; in this unit, the removal of about 120,000 people of Japanese ancestry, two thirds of them American citizens, to guarded camps for much of the war. Students will meet these figures again on the quick check, so have them written exactly.",
     kick='E · Removal and the camps')

# 17 E CONTENT PHOTO
content_photo('manzanar-port.jpg', 'Life inside the wire',
              ['Ten camps in the interior, behind barbed wire',
               'Families sold homes and businesses in days, at a loss',
               'No charge filed, no hearing on loyalty',
               'Schools, work crews, and camp newspapers behind the wire',
               'Ansel Adams photographed Manzanar, 1943'],
              "The photograph shows farm workers at the Manzanar camp in California with Mount Williamson behind the fields, photographed by Ansel Adams in 1943 and held by the Library of Congress. Adams came to Manzanar at the invitation of its director and photographed the camp's people at work and at school, and his pictures show the fact students find hardest to hold: ordinary life, carried on by force inside a guarded fence. Fill in the material record around the image. Families had days to sell homes, farms, and businesses, and sold at heavy losses or lost the property outright. Camp residents worked for camp wages, farmed the fields in this photograph, and sent their children to camp schools. None of it answers the legal fact from the last section: no charge was filed against the people held, and no hearing ever tested any one person's loyalty.",
              kick='E · Removal and the camps')

# 18 F DIVIDER
divider_text('Section F', 'Korematsu and the Courts',
             'The exclusion reaches the Supreme Court, 1944.',
             "Fred Korematsu was a welder in San Leandro, California, an American citizen who refused to leave his home when the exclusion orders came, and was arrested and convicted for staying. His lawyers carried the case to the Supreme Court as a test of the exclusion itself. Section F reads the Court's answer the way the activity does, from its own sentences. Students should listen for the tension inside the majority opinion, because the opinion states the strongest rule in the lesson and then declines to apply its force: restrictions on a single racial group are immediately suspect and demand the most rigid scrutiny, and this restriction survives. The dissents answer from the same record, and students will meet both voices in the Contradiction File at Station 5.")

# 19 F CONTENT
content_text('Suspect, scrutinized, and upheld',
             ['Decided December 1944, by six votes to three',
              'Restrictions on one racial group are immediately suspect',
              'The Court accepts military necessity',
              'Murphy, in dissent: the exclusion fell into racism',
              'Jackson, in dissent: a loaded weapon in the law'],
             "In the guided notes definition, Korematsu v. United States is the 1944 Supreme Court decision that upheld the exclusion of Japanese Americans from the West Coast as a military necessity. Walk the opinion in its own order. Justice Black's majority begins by calling restrictions on a single racial group immediately suspect, subject to the most rigid scrutiny, and concedes that racial antagonism can never justify them. It then accepts the military's claim of pressing public necessity at the time the order was made, and upholds the exclusion. The dissents belong in the notes with names attached: Murphy charged that the exclusion fell into racism on a record without military evidence to support it, and Jackson warned that the ruling would remain in the law like a loaded weapon for any future authority claiming urgent need. The ruling stood for the rest of the war.",
             kick='F · Korematsu and the courts', size=24)

# 20 G DIVIDER
divider_photo('rct442-port.jpg', 'Section G', 'The 442nd and the Claims',
              ['Soldiers of the 442nd Regimental', 'Combat Team in France.'],
              "The photograph shows soldiers of the 442nd Regimental Combat Team in France, in a United States Army Signal Corps photograph. Section G closes the lesson inside the contradiction rather than resolving it, and the 442nd is the reason the closing must be written carefully. The unit was segregated by the same policy that runs through this lesson, and it was recruited in part from the camps of section E: young men volunteered, and later were drafted, out of the barbed wire enclosures where their families remained. What those men did in Italy and France is a matter of record, and the record is extraordinary by the Army's own accounting. Teach the record plainly and then put the question the reading leaves open: what a country owes, and to whom, when service of this order comes from citizens it is holding behind wire.",
              title_size=38)

# 21 G CONTENT
content_text('The record from inside the contradiction',
             ['A segregated Japanese American unit',
              'Recruited in part from the camps themselves',
              'Fought in Italy and France',
              'Rescued a trapped Texas battalion, Vosges, October 1944',
              'Linguists of the Military Intelligence Service in the Pacific'],
             "In the guided notes definition, the 442nd Regimental Combat Team is the segregated Japanese American army unit that fought in Europe and became one of the most decorated units of its size and length of service in American history. Give the Vosges rescue its weight. In October 1944 the 442nd was ordered to break through German lines to a Texas battalion cut off in the mountains, and it did so at a cost in casualties that exceeded the number of men it rescued. Add the second service: Japanese American linguists of the Military Intelligence Service translated documents and interrogated prisoners across the Pacific, work the Army later credited with shortening the war. Then close the section where the reading closes. The claims and the camps stand in the same years, and what the country owed on each claim was left for later years to argue.",
             kick='G · The 442nd and the claims', size=24)

# 22 GLANCE
s = slide(NAVY)
kicker(s, 'Two fronts at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'The claim, and what stood beside it', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('War work', 'Order 8802; a committee to hear complaints', 'No power to compel a firm to hire'),
        ('The campaign', 'Double V, from February 1942', 'A demand pressed, not yet a right granted'),
        ('Service', 'A million in uniform; the Tuskegee record', 'Units segregated; most in labor roles'),
        ('Removal', '120,000 removed; Korematsu upholds it', 'The 442nd fights; families stay in camp')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, Two Fronts at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. Read the rows as pairs, because pairing is the lesson. War work pairs a real federal claim with a committee that could not compel. The campaign pairs a national demand with the standing fact that it remained a demand. Service pairs a million people in uniform and a distinguished combat record with segregation written into assignment. Removal pairs the largest denial in the lesson with the 442nd's service in the same years. Grade the table generously on wording and strictly on the pairing: every row must carry both a gain or a service and the limit or denial that stood beside it.")

# 23 VOCAB A
vocab('Words for the claims',
      [('Executive Order 8802', 'barred discrimination in defense work, June 1941'),
       ('Fair Employment Practices Committee', 'heard complaints of job discrimination'),
       ('Double V campaign', 'victory abroad, victory at home, from 1942'),
       ('Executive Order 9066', 'the removal order of February 19, 1942')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. Executive Order 8802: President Roosevelt's order of June 1941 barring racial discrimination in defense industries and federal employment, issued under the threat of a protest march on Washington. Fair Employment Practices Committee: the federal committee created in 1941 to investigate complaints of job discrimination in war industries. Double V campaign: the campaign led by Black newspapers from 1942 for victory over fascism abroad and victory over racism at home. Executive Order 9066: President Roosevelt's order of February 19, 1942 authorizing the military to exclude people from areas of the West Coast, the order under which Japanese Americans were removed from their homes. Note the pairing in this set itself: the first three terms widen claims, and the fourth removes one, eleven months apart.")

# 24 VOCAB B
vocab('Words for the exclusion and the answer',
      [('internment', 'forced confinement; 120,000 removed to camps'),
       ('Korematsu v. United States', 'the 1944 ruling upholding the exclusion'),
       ('442nd Regimental Combat Team', 'the decorated Japanese American unit')],
      "Three more terms, again matching the guided notes exactly. The first is internment: the forced confinement of a group of people; in this unit, the removal of about 120,000 people of Japanese ancestry, two thirds of them American citizens, to guarded camps for much of the war. The figures inside the definition are part of the definition, and students should learn them with it. Korematsu v. United States: the 1944 Supreme Court decision that upheld the exclusion of Japanese Americans from the West Coast as a military necessity. The last term is 442nd Regimental Combat Team: the segregated Japanese American army unit that fought in Europe and became one of the most decorated units of its size and length of service in American history. The definition's closing claim is the Army's own accounting of the unit's record, and it is stated in the definition on purpose.")

# 25 SYNTHESIS
content_text('Holding both halves at once',
             ['The claims widened: work, a campaign, a service record',
              'The exclusion stood: removal, camps, a court ruling',
              'Both records are dated, documented, and American',
              'The writing task asks for a weighing, not a tally'],
             "Close the teaching here, before the work slide, and model the judgment the writing task will ask for. The lesson's record does not sort into a simple verdict, and students should be told plainly that a one sided answer will read as unfinished work. The claims did widen: a federal order against discrimination in war work, a national campaign that made citizenship a war aim, and service records that could not later be argued away. The exclusion also stood, in law and in fact: an order, ten camps, and a Supreme Court ruling that together held about 120,000 people, most of them citizens, outside the protection the war was said to defend. The strongest student writing will weigh the halves against a stated standard, such as whether a gain arrived as an enforceable right or as a favor that had to be requested.",
             kick='Synthesis')

# 26 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did a war fought in democracy\u2019s name test democracy at home? Argue both the claims gained and the exclusion, from the documents.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Contradiction File: five stations, each with a claim, a denial, and a reason'),
        ('Notebook', 'Notebook page: the five documents charted, and the contradiction in one paragraph'),
        ('Quick check', 'The Flag and the Bus: the Parks portrait, Order 8802, the removal figures, Korematsu'),
        ('Writing', 'Did the War Years Advance Freedom at Home? Both halves weighed, from the bank')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: how the threatened march produced Order 8802, the removal figures in full, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Contradiction File, runs five stations through the documents: Executive Order 8802 quoted from the audited record, a labeled summary of the Double V campaign, a labeled summary of the Tuskegee record, Executive Order 9066 quoted from the Federal Register text, and the Korematsu majority opinion with its dissent summarized and labeled, ending in a ranking of the five by the size of the gap between aims and facts. The notebook page charts the same five documents. The quick check, The Flag and the Bus, works from the Parks portrait. The writing task turns the lesson question into an essay weighed from both halves of the bank. The exit ticket has three parts: how the threatened march produced the order, the removal figures in full, and the lesson question answered with one claim gained and one denial.")

dc.save(OUT)
