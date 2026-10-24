#!/usr/bin/env python3
"""World War II Lesson 2 deck v2 (rollout), "Pearl Harbor and the Arsenal of
Democracy," built to the approved system: image-led slides, fragments
only on screen, comprehensive speaker notes, full lesson + vocabulary
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
text(s, 0.9, 5.32, 11.5, 0.4, 'WORLD WAR II · LESSON 2', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Pearl Harbor and the Arsenal of Democracy', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'What the attack settled, and what it left for Americans to decide', size=17, color=POWDER)
notes(s, "The photograph shows USS Arizona burning at Pearl Harbor on December 7, 1941, in a United States Navy photograph held by the National Archives. Open by placing this lesson against the last one. Lesson 1 ended with a country arming an ally, shooting at sea in the Atlantic, and still calling itself neutral under its own laws. That halfway condition lasted until this Sunday morning. In about two hours, Japanese carrier aircraft wrecked the battleship fleet at Pearl Harbor, killed more than 2,400 Americans, and answered the question the country had argued about since 1939. But the lesson question is two-sided, and students should hear both halves from the start. The attack settled a great deal, and it left the hardest questions, strategy, alliance, and production, for Americans to decide.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('What did the attack on Pearl Harbor settle, and what did it leave for Americans to decide?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the Second World War transform the United States, and how far did the country live up to the democracy it claimed to defend?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question trains a distinction students will use in every lesson of this unit, the distinction between an event and the decisions that follow it. The attack of December 7 settled the entry question completely, and it settled the two-ocean question four days later, though the enemy settled that one. It did not settle how the war would be fought, in what order the enemies would be beaten, when France would be invaded, or whether American factories could build the arsenal the strategy required. The exit ticket and the writing task both test both halves, so warn students against one-sided answers from the beginning. The unit question runs beneath as the frame: a country entering a war in democracy's name, united at entry in a way it had not been in 1917.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Settled in December, decided over years', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The Attack', 'Two waves, eight battleships, the carriers at sea'),
        ('B', 'A Date Which Will Live in Infamy', 'December 8, and a declaration in hours'),
        ('C', 'Germany Declares War', 'December 11, and a two-ocean war'),
        ('D', 'What December Settled', 'The neutrality debate ended in a day'),
        ('E', 'The Grand Alliance and Germany First', 'Germany first, and a second front demanded'),
        ('F', 'The Cost of the First Six Months', 'Bataan, and sixteen bombers over Tokyo'),
        ('G', 'An Arsenal on Paper', 'Targets set for an arsenal not yet built')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Sections A and B cover December 7 and December 8, the attack and the American declaration against Japan. Section C covers December 11, when Germany and Italy declared war and settled the two-ocean question. Section D steps back and names what December settled as a whole. Section E covers the strategy built at the Arcadia Conference, the Grand Alliance and Germany first, and the Soviet demand for a second front. Section F states the cost of the first six months, and section G closes on the arsenal that existed mostly on paper. The summary table at the end of the guided notes is titled December 1941 at a Glance.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_photo('arizona-port.jpg', 'Section A', 'The Attack',
              ['USS Arizona burning at Pearl Harbor,', 'December 7, 1941.'],
              "The photograph is a United States Navy photograph held by the National Archives, showing USS Arizona burning after the attack. Set the scene with the hour and the place. Pearl Harbor, on the island of Oahu in Hawaii, was the home base of the Pacific Fleet, and on a Sunday morning its battleships lay moored in pairs beside Ford Island, with aircraft parked wing to wing on the airfields at Hickam and Wheeler to guard against sabotage. Six Japanese carriers had crossed the northern Pacific under radio silence and launched their planes in two waves. The attack was a tactical success built on surprise, and it was aimed at one purpose: to disable the Pacific Fleet long enough for Japan to seize the resource empire it wanted in Southeast Asia and the Pacific islands. Whether it achieved that purpose is a question this lesson answers by its last section.",
              title_size=44)

# ------------------------------------------------------ 5 THE ATTACK
content_photo_s('westvirginia-port.jpg', 'Two waves on a Sunday morning',
              ['The first bombs fell just before 8 in the morning.',
               'Battleships lay moored beside Ford Island.',
               'The airfields at Hickam and Wheeler were struck.',
               '188 American aircraft were destroyed, most on the ground.',
               'The carriers were at sea, and survived.'],
              "The photograph shows USS West Virginia burning at Pearl Harbor, a United States Navy photograph of December 7, 1941. Walk the attack in order. The first bombs fell just before eight in the morning, and the two waves worked over the battleships, the airfields, and the harbor installations for about two hours. On the ground, American aircraft had been parked close together as a guard against sabotage, which made them easy targets from the air, and 188 were destroyed, most before they could move. The point students must carry forward sits in the last fragment. The Pacific Fleet aircraft carriers were at sea that morning on missions and exercises, and they survived untouched. The attack had wrecked the battle line built for the last war and left intact the carrier force the Pacific war would actually be fought with. That accident of scheduling shaped 1942.",
              kick='A · The Attack')

# ------------------------------------------------------ 6 STAT KILLED
stat('2,403', 'Americans killed at Pearl Harbor',
     'More than 2,400 dead in the standard Navy accounting · 1,178 wounded · Eight battleships damaged, four sunk',
     "Give the class the full accounting behind this number, because the activity's damage table tests it. The standard United States Navy accounting counts 2,403 Americans killed and 1,178 wounded at Pearl Harbor on December 7, 1941. More than 1,100 of the dead were crew of USS Arizona, which exploded and sank at her moorings. All eight battleships in the harbor were damaged, and four were sunk, though most of the damaged ships were later raised, repaired, and returned to service. On the airfields, 188 American aircraft were destroyed and 159 damaged. Students should hear one comparison plainly: this single morning killed more Americans than many whole campaigns of earlier American wars, and it did so on American territory, in a place most citizens had to find on a map. The political consequence follows in section B: a shocked and grieving country did not debate entry for long.",
     kick='A · The Attack')

# ------------------------------------------------- 7 SECTION B DIVIDER
divider_photo('signing-port.jpg', 'Section B', 'A Date Which Will Live in Infamy',
              ['Roosevelt signing the declaration', 'of war against Japan, December 8, 1941.'],
              "The photograph, by Abbie Rowe of the National Park Service and held by the National Archives, shows President Roosevelt signing the declaration of war against Japan on December 8, 1941. Section B covers the day after the attack, and it moves fast, because the country moved fast. Japanese forces were striking across the Pacific the same day as Pearl Harbor, against the Philippines, Guam, and Wake Island, and against British Malaya and Hong Kong, so the address Roosevelt delivered was written for a war already spreading on two sides of the ocean. He spoke to a joint session of Congress in person, in an address of a few minutes, and he built it on two claims: that the attack was deliberate and deceptive, and that a state of war had existed since the attack itself. The signing in this photograph came within hours of the speech.",
              title_size=36)

# ------------------------------------------------------ 8 THE ADDRESS AND VOTES
content_photo_s('congress-port.jpg', 'The address, and the votes',
              ['Roosevelt addressed a joint session in person.',
               'December 7 was named a date which will live in infamy.',
               'War was dated from the attack itself.',
               'The Senate voted 82 to 0, and the House voted 388 to 1.',
               'The one dissent was Jeannette Rankin of Montana.'],
              "The photograph shows Roosevelt asking Congress for the declaration on December 8, 1941, in an image held by the National Museum of the United States Navy. Teach the wording of the request, because the quick check and the activity both use it. Roosevelt did not ask Congress to begin a war. He asked it to declare that a state of war had existed since the unprovoked attack of December 7, which placed the choice of war on Japan and made Congress the body that recognized a fact. Then give the votes their full weight. The Senate voted 82 to 0 and the House 388 to 1, the single dissent cast by Representative Jeannette Rankin of Montana, who had also voted against entry in 1917. A declaration that passes within hours, with one dissent, is the statistical shape of the settlement section D describes. The debate of six years ended in an afternoon.",
              kick='B · A Date Which Will Live in Infamy')

# ------------------------------------------------- 9 SECTION C DIVIDER
divider_text('Section C', 'Germany Declares War',
             'The declaration of December 8 covered Japan alone. Four days later the enemy widened the war.',
             "Pause on the legal position before this section's fact lands, because students routinely assume the German war followed automatically from the Japanese one. It did not. Congress had declared war on Japan only. The Tripartite Pact bound Germany, Italy, and Japan to aid one another if one of them was attacked, and Japan had done the attacking, so Germany owed Japan nothing under the treaty. An American war against Germany required either a German act or a new American declaration, and through the autumn of 1941 the undeclared naval war in the Atlantic had not produced either. What produced it, on December 11, was a decision in Berlin. Teach this section as the lesson's central reversal: the largest strategic question facing the United States, one ocean or two, was settled by the enemy, for his own reasons, against his own treaty position.")

# ------------------------------------------------------ 10 DECEMBER 11
content_text('December 11: the enemy decides',
             ['Germany and Italy declared war on the United States.',
              'No treaty required Germany to follow Japan.',
              'Hitler wanted his submarines free in the Atlantic.',
              'Congress answered the same day, without dissent.',
              'The United States faced a two-ocean war against three enemies.'],
             "On December 11, 1941, Germany delivered its declaration of war and Hitler announced it in Berlin, charging that the United States had already been waging undeclared war in the Atlantic through Lend-Lease, convoy escorts, and the shoot on sight orders of that autumn. Italy declared war the same day. Congress answered within hours with declarations against both, passed without a dissenting vote. Why Hitler acted is argued from his record: he expected American entry sooner or later, he wanted the restraint lifted from his submarine captains against American shipping, and he underrated what American production would mean in Europe. Students should state the consequence without embroidery. The United States had entered the war intending to answer one attack in one ocean. It now faced Germany, Italy, and Japan at once, and every plan built since December 7 had to be rebuilt for two oceans. Section E shows the rebuilding.",
             kick='C · Germany Declares War', size=24)

# ------------------------------------------------- 11 SECTION D DIVIDER
divider_text('Section D', 'What December Settled',
             'One month closed an argument of six years, and left the strategy open.',
             "This short section is the hinge of the lesson, and it should be taught slowly even though its content is a summary. Between 1935 and December 1941 the United States had argued, in Congress, in the press, and in the America First campaign of the last lesson, about whether a European and Asian war was America's business at all. That argument had produced neutrality laws, then aid laws, then an undeclared naval war, each step contested. The attack ended the argument by changing its subject: the question was no longer whether to enter a foreign war, but how to answer an attack on American forces. Students who grasp this hinge can explain both the votes of December and why the strategy questions of section E could be debated calmly in conference rooms while the country was at war. The argument about ends was over. The argument about means was beginning.")

# ------------------------------------------------------ 12 SETTLED
content_text('The debate ended in a day',
             ['The neutrality debate ended after six years of argument.',
              'Entry was united, with one dissent across both declarations.',
              'The United States was in the war in full, by law.',
              'The question of how to fight, and in what order, was still open.',
              'The question of whether industry could build the force was still open.'],
             "Name the settlement in its three parts. First, the neutrality debate ended: the legislation, speeches, and committee campaigns that had structured American politics since the mid 1930s lost their subject in a morning. Second, the entry was united in a way 1917 had not been: the declaration of that war followed months of argument and carried a large and vocal minority, while December 1941 produced one dissenting vote on Japan and none at all on Germany and Italy. Third, the commitment was total and legal, the country's industry, manpower, and credit placed behind the war by declaration rather than by executive improvisation. Then turn the slide's last two fragments into the lesson's second half. How to fight a two-ocean war, in what order to beat three enemies, and whether the factories could build what the strategy required were all still open, and the first conferences took them up within the month.",
             kick='D · What December Settled', size=24)

# ------------------------------------------------- 13 SECTION E DIVIDER
divider_text('Section E', 'The Grand Alliance and Germany First',
             'The strategy for a two-ocean war, built in Washington in the war\'s first month.',
             "On December 22, 1941, two weeks after Pearl Harbor, Winston Churchill arrived in Washington and the Arcadia Conference opened, running into the middle of January 1942. It was the first wartime conference between the American and British leaders, and its setting carried a message students should notice: the alliance was being built face to face, at the highest level, within days of entry, because the alternative was two allies fighting parallel wars on separate plans. The conference produced the alliance's public charter, the Declaration by United Nations, and it reaffirmed the strategic judgment the two staffs had drafted together before Pearl Harbor, that Germany was the enemy to beat first. The Soviet Union was not in the room, and its absence from the strategy's making sits behind the second front argument that runs through this section and the next two years of the war.")

# ------------------------------------------------------ 14 GRAND ALLIANCE
content_text('Twenty-six nations, one declaration',
             ['The Arcadia Conference opened in Washington on December 22.',
              'The Declaration by United Nations was signed on January 1, 1942.',
              'Twenty-six nations signed, pledging their full resources.',
              'The signers pledged no separate peace with the Axis.',
              'The Grand Alliance joined the United States, Britain, and the Soviet Union.'],
             "The Grand Alliance is a vocabulary term, and its definition belongs in full in the notes of the vocabulary slides; here, teach its working parts. The alliance's core was three powers with little in common beyond the enemy: the United States, Great Britain, and the Soviet Union. Around that core, the Declaration by United Nations of January 1, 1942 gathered 26 nations in a pledge to use their full resources against the Axis and to make no separate peace, a clause aimed at the alliance's deepest fear, that one member might cut its own deal and free Germany to fight the others one at a time. The name in the declaration outlasted the war and became the name of the postwar organization, which students will meet in the Cold War unit. For this lesson, the alliance's significance is practical: strategy would now be made jointly, and joint strategy meant argument, beginning with the question of the next slide.",
             kick='E · The Grand Alliance and Germany First', size=24)

# ------------------------------------------------------ 15 GERMANY FIRST
content_text('Germany first, and the demand it created',
             ['The main effort went against Germany, while Japan was held in the Pacific.',
              'Germany was judged the stronger enemy.',
              'Britain and the Soviet Union could be knocked out, while Japan was held.',
              'The Soviet Union demanded a second front in France.',
              'France waited until June 1944.'],
             "Germany first was not an improvisation of the Arcadia Conference. The American and British staffs had agreed it in their staff talks before Pearl Harbor, and the conference held to it under the pressure of a Pacific war going badly, which is the strongest evidence of how firmly the judgment was held. The reasoning was comparative. Germany could win its war outright by knocking Britain out with submarines and bombing, or the Soviet Union out on the Eastern Front, where the largest land fighting of the war was already raging. Japan could seize an empire but could not knock the United States out of the war. The price of the strategy was paid in Soviet suspicion: from 1942 the Soviet Union demanded a second front, an invasion of France to draw German divisions west, and the western Allies, short of landing craft and trained troops, landed in North Africa instead and reached France only in June 1944.",
             kick='E · The Grand Alliance and Germany First', size=24)

# ------------------------------------------------- 16 SECTION F DIVIDER
divider_photo('bataan-port.jpg', 'Section F', 'The Cost of the First Six Months',
              ['American troops surrendering in the Philippines,', 'in a captured Japanese photograph, 1942.'],
              "The photograph is a captured Japanese photograph held by the National Archives, showing American troops surrendering in the Philippines in the spring of 1942. Section F is the lesson's accounting of what the strategy cost while the arsenal was being built, and it should be taught as record rather than drama. Between December 1941 and June 1942 Japan conquered the Philippines, Malaya, Singapore, and the Dutch East Indies, and the Allied position in the Pacific collapsed to a line running through Hawaii, Midway, and Australia. The emblem of those months in American memory was Bataan, where American and Filipino troops held a peninsula for about four months on shrinking rations until surrender became the only alternative to starvation. Against that record, the section sets one raid whose importance was out of all proportion to its damage. Both halves belong in the notes, because the writing task asks students to weigh them together.",
              title_size=36)

# ------------------------------------------------------ 17 BATAAN
content_text('Bataan: holding on empty',
             ['The Philippines were invaded within days of Pearl Harbor.',
              'Bataan held about four months, on shrinking rations.',
              'The defenders were short of medicine, ammunition, and relief.',
              'On April 9, 1942, about 75,000 troops surrendered.',
              'Corregidor fell on May 6.'],
             "Teach Bataan from its logistics, because the surrender reads wrongly without them. The defenders of Bataan were cut to half rations early in the siege and to less after that, malaria and dysentery spread through troops with almost no medicine, and no relief force existed that could fight through the Japanese fleet to reach them. The arsenal of section G is the explanation: the ships, aircraft, and trained divisions that a relief expedition required had not yet been built. On April 9, 1942, the Bataan force surrendered, about 75,000 American and Filipino troops, the largest surrender of American-led forces in the country's history, and thousands died on the march to prison camps and in the camps themselves. The island fortress of Corregidor, in Manila Bay, held until May 6. Students should keep the order straight for the test: Bataan in April, Corregidor in May, and the whole Philippine campaign lost inside the war's first six months.",
             kick='F · The Cost of the First Six Months', size=24)

# ------------------------------------------------------ 18 DOOLITTLE
content_photo_s('hornet-port.jpg', 'Sixteen bombers over Tokyo',
              ['On April 18, 1942, B-25 bombers launched off the carrier Hornet.',
               'Lieutenant Colonel James Doolittle led the raid.',
               'Tokyo and other cities were bombed.',
               'The damage was light, but the effect was not.',
               'Most crews came down in China, and survived.'],
              "The photograph, a United States Navy photograph, shows a B-25 bomber taking off from USS Hornet during the Doolittle Raid of April 18, 1942; the Commons file is small, and the deck crop is correspondingly soft. Army bombers were never designed to fly from carriers, and the raid was planned around that impossibility: sixteen B-25s, stripped and loaded with extra fuel, launched far from Japan and flew on to China because no bomber could land back on the deck. The bombs did little material damage, and teachers should say so plainly, because the raid's honest significance is in its effects. It answered Bataan in American morale nine days after that surrender, it shocked a Japanese public whose capital had been promised safety, and it pressed Japanese leaders to widen their defensive perimeter, a decision students will weigh at Midway in lesson 5. Most of the eighty raiders survived, many with Chinese help, and China paid heavily for that help in Japanese reprisals.",
              kick='F · The Cost of the First Six Months')

# ------------------------------------------------- 19 SECTION G DIVIDER
divider_text('Section G', 'An Arsenal on Paper',
             'In December 1941 the arsenal of democracy was a promise and a set of factory orders.',
             "The phrase in this section's title comes from Roosevelt's own language of the year before entry, when he had called the United States the arsenal of democracy for the nations already fighting. Section G asks what that phrase was worth in the month the country joined the fighting itself. The honest answer is that it described a program, not a stockpile. The army was growing under the draft of 1940 but was short of modern weapons, training, and transport. The navy's new ships were on slipways rather than in the water. Aircraft and tank production was climbing from a small base toward targets no industry had ever reached. Students should be ready to hold the contrast that the rest of the unit is built on: the strategy agreed in December 1941 was sound, and the means to execute it did not yet exist. Closing that gap is lesson 3, mobilization.")

# ------------------------------------------------------ 20 TARGETS
content_text('Targets set in public',
             ['The president set the targets in his annual message on January 6, 1942.',
              'The target was 60,000 warplanes to be built in 1942.',
              'The targets also called for 45,000 tanks and 20,000 antiaircraft guns.',
              'The shipping target was eight million tons of merchant shipping.',
              'Factories were still converting from peacetime work.'],
             "Roosevelt set the production targets in public, in his annual message of January 6, 1942, and the publicity was itself a decision: the figures told allies the scale of the commitment, told the enemy the scale of what was coming, and told American industry and workers the scale of what was being asked of them. Read the figures against 1941 output to give them meaning. American aircraft production in 1941 had been roughly nineteen thousand planes of all types, many of them trainers; the target for 1942 alone was sixty thousand warplanes. The tank and shipping figures were of the same order of ambition, set for factories that in January 1942 were still converting from cars and peacetime goods. Whether the targets would be met, and what meeting them would do to the country's economy and workforce, were open questions in this lesson's sense. Lesson 3 gives the answer: the targets were met and passed, by a mobilization that remade the home front.",
             kick='G · An Arsenal on Paper', size=24)

# ------------------------------------------------------ 21 STAT 1945 STRENGTH
stat('12 million', 'Americans in uniform by 1945',
     'The force the arsenal had to equip · An army of under 200,000 in 1939, grown more than sixtyfold',
     "This figure is the destination the arsenal of December 1941 had to reach, and students should connect it backward to section G's targets. By 1945 more than twelve million Americans were in uniform, in an armed force that had numbered under two hundred thousand regulars in 1939. Every one of those twelve million had to be clothed, fed, armed, trained, and carried to a theater across an ocean, most of them in ships that did not exist in December 1941. The production targets of January 1942, sixty thousand warplanes and eight million tons of shipping in a single year, were sized to this force and to the allies the United States was also supplying under Lend-Lease. Put the two stat slides of this lesson side by side in closing discussion: 2,403 dead in a morning at the war's start, and twelve million in uniform at its end. The distance between those numbers is the transformation the unit question asks about.",
     kick='G · An Arsenal on Paper')

# ------------------------------------------------------ 22 GLANCE
s = slide(NAVY)
kicker(s, 'December 1941 at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Settled, and left open', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The attack', 'December 7: the fleet struck, 2,403 killed', 'Entry decided in a morning'),
        ('The declarations', 'December 8 on Japan; December 11 from Germany and Italy', 'A two-ocean war, settled by the enemy'),
        ('The strategy', 'Grand Alliance; Germany first', 'Agreed at Arcadia, argued over for years'),
        ('The open questions', 'Second front timing; the unbuilt arsenal', 'The risks December left behind')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, December 1941 at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The four rows are the lesson's argument in order. The attack covers December 7, the damage figures, and the carriers that survived. The declarations covers December 8 and December 11 together, because the pair of them, one American and one German, fixed the war's shape. The strategy covers the Grand Alliance and Germany first, agreed in the war's first month. The open questions covers what December left behind: the timing of a second front in France, and an arsenal that existed as orders and targets rather than as weapons in soldiers' hands. Grade the table generously on wording and strictly on the sorting: an entry that places the second front among the settled items has missed the lesson.")

# ------------------------------------------------------ 23 VOCAB A
vocab('Words for the entry',
      [('Pearl Harbor', 'the naval base in Hawaii attacked on December 7, 1941'),
       ('Axis powers', 'Germany, Italy, and Japan, allied against the Allies'),
       ('Allies', 'the nations allied against the Axis, led by the United States, Britain, and the Soviet Union'),
       ('Grand Alliance', 'the formal alliance of the United States, Britain, and the Soviet Union')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. The first term is Pearl Harbor: the United States naval base in Hawaii attacked by Japanese carrier aircraft on December 7, 1941, the attack that brought the United States into the Second World War. The second is Axis powers: the alliance of Germany, Italy, and Japan that fought the Allied nations in the Second World War. The third is Allies: the nations allied against the Axis in the Second World War, led by the United States, Great Britain, and the Soviet Union. The fourth is Grand Alliance: the formal alliance of the United States, Great Britain, and the Soviet Union against the Axis, joined by many other nations in the Declaration by United Nations of January 1, 1942. Keep the two alliance terms distinct: Allies names the whole coalition, Grand Alliance its formal three-power core.")

# ------------------------------------------------------ 24 VOCAB B
vocab('Words for the strategy',
      [('Germany first', 'the strategy of defeating Germany before Japan'),
       ('second front', 'the invasion of France the Soviet Union demanded from 1942'),
       ('theater', 'a large geographic area of military operations')],
      "Three more terms, again matching the guided notes exactly. The first is Germany first: the Allied strategy of concentrating the main effort on defeating Germany before Japan, agreed by the American and British staffs and kept through the war. The second is second front: the Allied invasion of German-held western Europe that the Soviet Union demanded from 1942 onward to draw German strength away from the Eastern Front. Note the direction of the demand in the definition: it ran from the Soviet Union toward its western allies, and the Eastern Front named in it was the front the Soviet army was holding. The third term is theater: a large geographic area of military operations, such as the European theater or the Pacific theater. Students will use theater constantly in the lessons ahead, for a war fought in two oceans at once. These three terms together describe the strategy problem December left open: two theaters, one main effort, and an ally demanding that the order change.")

# ------------------------------------------------------ 25 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['What did the attack on Pearl Harbor settle, and what did it leave for Americans to decide? Sort the record before you judge it.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'Settled and Unsettled: five stations, a sorting table, and a verdict on risk'),
        ('Notebook', 'Notebook page: the opening questions, marked settled or open from the record'),
        ('Quick check', 'The Harbor on Fire: the attack, the declarations, and Germany first'),
        ('Writing', 'Settled and Undecided: the lesson question as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: two settled facts with evidence, Germany first and the Soviet demand, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, Settled and Unsettled, puts five stations in front of students: the Pearl Harbor Address in Roosevelt's own words, the damage record in figures, a summary of the German declaration, a teaching summary of the Arcadia agreements, and a summary of Bataan and the Doolittle Raid, and it ends by asking students to sort the opening facts into settled and open and to judge which open question carried the most risk. The notebook page asks students to mark the war's five opening questions settled or open from the record. The quick check, The Harbor on Fire, tests the attack figures, the December declarations, and Germany first against the photograph of West Virginia burning. The writing task turns the lesson question into an essay argued from the documents. The exit ticket has three parts: two settled facts with evidence, Germany first with the Soviet demand, and the lesson question in two or three sentences. Next lesson opens in the factories, where the arsenal on paper had to be built.")

dc.save(OUT)
