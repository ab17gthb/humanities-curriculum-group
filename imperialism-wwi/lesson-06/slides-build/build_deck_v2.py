#!/usr/bin/env python3
"""Lesson 6 deck, "Americans in the War," built to the approved Progressive Era system:
image-led slides, fragments only on screen, comprehensive speaker notes,
full lesson and vocabulary coverage. Fonts: Georgia titles, Lato body."""
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

def vocab4(title, terms, note, kick='The vocabulary'):
    s = slide(CREAM)
    kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95, 11.5, 1.0, title, size=30, color=NAVY, font='Georgia')
    yy = 1.95
    for term, dfn in terms:
        text(s, 0.9, yy, 3.6, 0.9, term, size=22, color=NAVY, font='Georgia')
        text(s, 4.65, yy + 0.04, 7.8, 1.1, dfn, size=18, color=MUTED, leading=1.2)
        yy += 1.24
    notes(s, note)
    return s

def content_photo_sized(img, title, items, note, kick=None, size=23):
    s = slide(CREAM)
    photo_right(s, img)
    if kick: kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95 if kick else 0.8, 6.9, 1.2, title, size=31, color=NAVY, font='Georgia', leading=1.05)
    frags(s, items, y=2.15 if kick else 2.0, size=size)
    notes(s, note)
    return s

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'IMPERIALISM AND WORLD WAR I · LESSON 6', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Americans in the War', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'The draft, the convoy crossing, the trenches, influenza, and the armistice', size=17, color=POWDER)
notes(s, "The photograph shows a convoy of twenty-five ships nearing Brest, France, on November 1, 1918, photographed by Robert W. Neeser from the escort vessel USS Rambler. It is the right opening image for this lesson because the crossing was the middle of the whole American story in the First World War. Before the crossing came mobilization: a small regular army, a draft run by local civilian boards, and hastily built training camps. After it came France: an independent American army under Pershing, trench warfare, two great battles in the autumn of 1918, and an influenza pandemic moving along the same routes as the soldiers. Tell students the lesson follows that order, from registration card to armistice, and that the guided notes, the activity stations, and the writing task all follow the same single draftee through the system. Nothing in this lesson is quoted from a soldier, deliberately. Every document in the lesson is labeled for exactly what it is.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did the United States mobilize, and what did its soldiers meet in France?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('Why did the United States seek power overseas, and how did the First World War change the country that fought it?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question has two halves, and the lesson is built to answer both. How did the United States mobilize? In April 1917 the regular army was small, and the country had to register, classify, draft, train, and ship millions of men in about eighteen months. What did its soldiers meet in France? A kind of warfare no American army had seen: trenches, machine guns, poison gas, and heavy artillery, in a segregated army, during a worldwide influenza pandemic. Keep the unit question underneath as the frame. The first five lessons of this unit asked why the United States sought power overseas. This lesson asks what fighting a great war did to the country that sent the army, and the home front lesson that follows takes the same question up at home. The writing task at the end of this lesson uses this exact question as its title, so students should hear it as a promise about what they will be asked to do.")

# --------------------------------------------------- 3 THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.05, 11.5, 1.0, 'From registration card to armistice', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.05)
rows = [('A', 'Raising an army by draft', 'the Selective Service Act and local boards'),
        ('B', 'Crossing in convoy', 'troopships grouped under naval escort'),
        ('C', 'An independent army', 'Pershing refuses the replacement plan'),
        ('D', 'Trench warfare and weapons', "no man's land, gas, guns, and artillery"),
        ('E', 'St. Mihiel, Meuse-Argonne', 'the two great American battles of 1918'),
        ('F', 'A segregated army', 'labor assignments and the 369th Infantry'),
        ('G', 'Influenza and the cost', 'disease kills more soldiers than battle'),
        ('H', 'The armistice', 'fighting stops on November 11, 1918')]
yy = 2.42
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.3, 0.6, t, size=20, color=CREAM, bold=True)
    text(s, 6.05, yy + 0.05, 6.4, 0.6, d, size=16, color=POWDER)
    yy += 0.56
notes(s, "This is the map of the lesson, and it follows the guided notes section by section. Sections A and B cover mobilization and the crossing: the draft that raised the army, and the convoy system that carried it past the U-boats. Section C takes up Pershing's fight to keep that army independent and under American command. Section D describes what waited in France, trench warfare and its new weapons, and section E follows the army through St. Mihiel and the Meuse-Argonne. Sections F and G hold the two facts a simple battle account would miss: a segregated army that assigned most Black soldiers to labor, and a disease that killed more American soldiers than combat did. Section H ends the fighting with the armistice. Tell students the War at a Glance chart on their guided notes has three rows, mobilization, the crossing, and combat, and they will fill it in as we go.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', 'Raising an Army by Draft',
             'A small regular army, and millions of men to register, classify, and train',
             "Slow down at the starting problem, because students often assume the United States entered the war with an army ready to sail. In April 1917 the regular army was small, and volunteers alone could not fill the ranks fast enough for a war of this size. Congress answered within weeks, passing the Selective Service Act in May 1917. The system's design is the teaching point of this section. Conscription was not run by the army seizing men. It was run by local civilian boards, neighbors examining neighbors, which classified each registered man and decided who would go first. The activity's first station follows one sample draftee, a labeled teaching sample named Thomas Reed, through registration, classification, induction, and training, so students can see the system as a sequence of decisions rather than a single event. This section covers the numbers and the machinery. The next section follows the men those boards sent across the Atlantic.")

# ------------------------------------------------------ 5 THE DRAFT
content_text('The Selective Service Act, May 1917',
             ['Conscription meant compulsory enrollment for military service.',
              'Local civilian boards examined and classified each man.',
              'Single men without dependents were called first.',
              'Training camps were built in haste across the country.',
              'Trainees drilled with wooden rifles at first because real weapons were scarce.'],
             "State the mechanism plainly, because the first blanks of the guided notes test it. The Selective Service Act of May 1917 set up conscription, compulsory enrollment for military service, also called the draft, and put it in the hands of local civilian boards. The boards examined each man, classified him, and decided who would go first, with single men without dependents generally called before married men. Then describe what induction looked like on the ground. Draftees reported to hastily built training camps, where they learned to march and shoot, often with wooden rifles at first because real weapons were scarce. That detail does real work in the lesson. A country that had kept a small peacetime army was improvising the largest force in its history, and the improvisation reached from camp construction to rifles. Keep the two-step structure in view: registration put nearly every young man on a list, and classification turned the list into an order of call. One without the other raises no army.",
             kick='A · Raising an army by draft')

# ------------------------------------------------------ 6 STAT ONE DAY
stat('10 MILLION', 'men registered on a single day, June 5, 1917',
     'About 24 million men registered in all. About 2.8 million were drafted, and millions more volunteered.',
     "Dwell on the scale of that single day, because it is the clearest measure of what mobilization meant in practice. On June 5, 1917, nearly 10 million men registered, at local boards in every county and city in the country, on one day set by law. About 24 million men registered in all across the war's registrations. Of those, about 2.8 million were drafted, and millions more volunteered, so the draft should not be taught as the only door into the army. It was the system's backbone: it guaranteed the flow of men, set the order in which they went, and let the government plan training, shipping, and replacement around known numbers. Ask students to connect the figure back to section A's machinery. Ten million registrations in a day is only possible with thousands of local boards working from the same forms on the same schedule. The sample draft record in the activity is drawn from exactly those standard forms and steps.",
     kick='A · Raising an army by draft')

# ------------------------------------------------- 7 SECTION B DIVIDER
divider_photo('convoy-port.jpg', 'Section B', 'Crossing in Convoy',
              ['Troopships grouped under escort,',
               'crossing an ocean patrolled by U-boats'],
              "The photograph is the same convoy image from the title slide, seen closer: a twenty-five ship convoy nearing Brest, France, on November 1, 1918, photographed from USS Rambler by Robert W. Neeser, Naval Historical Center photograph NH 158. Name the problem this section solves. An army raised in the United States was useless unless it could cross an ocean patrolled by German submarines, called U-boats, which had been sinking Allied shipping at rates Britain could not sustain. The first small American force landed in France in June 1917, weeks after the declaration of war. Getting two million men across by November 1918, with their food, guns, and ammunition, was a naval achievement as much as a military one. The activity's second station uses this same photograph, and students will be asked what would have happened to the army in France if the convoy system had failed. Keep that dependency in mind through the section.",
              title_size=44)

# ------------------------------------------------------ 8 HOW A CONVOY WORKED
content_text('How a convoy worked',
             ['Troopships and supply ships sailed together in groups.',
              'Destroyers and escort vessels guarded the group.',
              'One torpedo could sink only one ship in the group.',
              'Convoys zigzagged, and ran without lights at night.',
              'Shipping losses fell sharply after convoys were adopted in 1917.'],
             "Work through the logic of the system, because the exit ticket tests it in one sentence. Under the convoy system, troopships and supply ships sailed together in groups under the protection of destroyers and other escort vessels. A U-boat captain who found one convoy faced many guns at once, and one torpedo could sink only one ship in the group, so grouping ships limited the damage any single attack could do. Convoys zigzagged to spoil a submarine's aim and ran without lights at night, and the activity adds radio silence to the list of habits students should notice in the photograph's account of a crossing. The system worked. Shipping losses fell sharply after convoys were adopted in 1917. Then give the payoff figure for the section: the first small American force had landed in June 1917, and by November 1918 about 2 million American soldiers were in France. The army Pershing commanded in the next section exists because this system held.",
             kick='B · Crossing in convoy')

# ------------------------------------------------- 9 SECTION C DIVIDER
divider_photo('pershing-port.jpg', 'Section C', 'An Independent Army',
              ['Pershing and the American',
               'Expeditionary Forces'],
              "The photograph shows General John J. Pershing, at left in the foreground, inspecting the Guard of Honor of the 3rd Battalion, 7th Infantry Regiment, 3rd Division, at Vaucouleurs, France, in 1918, with Major General Beaumont B. Buck and Brigadier General Fred W. Sladen. It is a United States Army Signal Corps photograph, number 111-SC-23759, held by the National Archives. Use it to introduce the man before the argument. Pershing commanded the American Expeditionary Forces, the United States forces sent to fight in Europe, and he arrived in France in June 1917 with firm instructions and a firmer temperament. The question of this section is organizational, and students sometimes underrate it: would American soldiers fight inside British and French units, or as their own army? Pershing's answer shaped the battles of 1918 and the American voice at the peace that followed, so treat the argument as strategy, not pride.",
              title_size=44)

# ------------------------------------------------------ 10 PERSHING'S INSISTENCE
content_text('What Pershing insisted on',
             ['The Allies wanted Americans as replacements in their units.',
              'Pershing refused, and insisted on an independent American army.',
              'The army would have American officers and an American sector of the front.',
              'The cost was time, and friction with the Allies.',
              'The gain was an American army, and a voice in the peace.'],
             "Set the two positions side by side, as the guided notes do. British and French commanders, whose armies had been bled for three years, wanted American soldiers fed into their own units as replacements, a few thousand at a time, where the need was immediate. Pershing refused. He insisted that Americans would fight as an independent army, under American officers, in their own sector, once trained and present in strength. Be honest about both sides of the bargain. The argument cost time, while Allied armies waited for help they could see arriving in port, and it caused real friction between allies. But it gave the United States its own army on the ground and a stronger voice in any peace that followed. While the argument went on, American divisions trained behind the lines and served quiet stretches in French trenches beside veteran units, which is how most Doughboys first met the warfare of the next section.",
             kick='C · An independent army')

# ------------------------------------------------- 11 SECTION D DIVIDER
divider_text('Section D', 'Trench Warfare and New Weapons',
             'Two lines of trenches, open ground between them, and weapons that made attack costly',
             "This section answers the second half of the lesson question directly: what did American soldiers meet in France? They met trench warfare on a scale no American army had seen. The reading's picture is systematic, and students should build it in order: two lines of trenches facing each other, dugouts below ground, and between the lines an open space called no man's land, cut by shell craters and tangled with wire. Life in the line meant mud, rats, and lice, in trenches that could be shelled at any hour. The next slide takes up the weapons that made this system so hard to break. After that, students will study the lesson's trench diagram, the same teaching diagram used in the activity, and trace an attack across it step by step. Keep the distinction ready from the start: the diagram is a drawing made for this lesson, not a historical document, and it is labeled that way wherever it appears.")

# ------------------------------------------------------ 12 THE WEAPONS
content_text('Why attack was so costly',
             ['Machine guns swept the open ground.',
              'Heavy artillery tore the trenches apart.',
              'Poison gas forced men to fight in masks.',
              'Tanks and aircraft appeared, but they did not yet break the deadlock.',
              'An attack opened with a barrage, then infantry crossed open ground.'],
             "Take the weapons in the order the guided notes test them. Machine guns swept open ground and could stop an attack in the wire. Heavy artillery tore the trenches apart and did most of the killing on the Western Front. Poison gas forced men to fight in masks and made even a quiet sector dangerous. Then make the balanced point about the new machines, because students often arrive believing tanks and airplanes ended trench warfare. Tanks and aircraft were appearing in 1918, but they had not yet broken the deadlock by themselves. An attack usually began with an artillery barrage, after which infantry crossed open ground against wire, machine guns, and shell fire, which is the sequence students will trace on the diagram next. The Doughboys, the nickname for American infantry soldiers in the First World War, learned this system in quiet sectors beside French veteran units before they were asked to attack inside it in the autumn battles.",
             kick='D · Trench warfare and new weapons')

# ------------------------------------------------------ 13 THE DIAGRAM
s = slide(CREAM)
kicker(s, 'D · Trench warfare and new weapons', color=RUST)
text(s, 0.9, 0.95, 11.5, 1.0, 'One sector of the front', size=31, color=NAVY, font='Georgia')
s.shapes.add_picture(os.path.join(dc.IMG, 'trench-diagram.png'), Inches(2.42), Inches(1.62), Inches(8.5), Inches(5.28))
text(s, 0.9, 6.98, 11.53, 0.5, 'Teaching diagram drawn for this lesson, simplified and not to scale. The same diagram you will work in the activity.',
     size=15, color=MUTED, align=PP_ALIGN.CENTER)
notes(s, "Be explicit about what this image is, because the lesson's honesty about sources is part of the teaching. This trench image is an original diagram drawn for this lesson, not a historical source, not a map of a real place, and not to scale. It is captioned as a diagram in the activity, and students should describe it the same way. Used as a model, it shows the parts of one sector that in real sectors varied in depth and distance: front trench, support trench, wire, and no man's land between the lines. Walk an attack across it slowly, as the activity's third station requires. The attacking unit crosses no man's land after a barrage, passes through gaps in the wire, and takes the front trench before reserves in the support trench counterattack. Ask where the danger is greatest. The front trench is drawn as a zigzag so that a shell burst, or an enemy inside the trench, cannot send blast or fire down a long straight length of it.")

# ------------------------------------------------- 14 SECTION E DIVIDER
divider_text('Section E', 'St. Mihiel and the Meuse-Argonne',
             'September to November 1918: the independent army fights its two great battles',
             "By September 1918 the army Pershing had insisted on building was present in strength, and this section follows its two great tests. The contrast between them is the teaching structure, and the reading question asks students to make the comparison themselves in scale, difficulty, and cost. St. Mihiel came first: a bulge in the German line south of Verdun, attacked on September 12 and pinched out in about four days. The Meuse-Argonne followed two weeks later and ran until the end of the war: about six weeks of fighting through forested, hilly ground against deep defenses, at the highest cost of any American battle of the war. Tell students to keep three numbers attached to each battle as we go: how many Americans fought, how long it lasted, and what it cost. The influenza section that follows will ask them to compare those battle costs with a cost no battle produced.")

# ------------------------------------------------------ 15 ST. MIHIEL
content_text('St. Mihiel, September 1918',
             ['St. Mihiel was the first great independent American battle.',
              'About 550,000 American soldiers took part.',
              'French troops, tanks, and aircraft supported the attack.',
              'The attack opened on September 12, 1918.',
              'The bulge was pinched out in about four days.'],
             "Give St. Mihiel its full weight as a first test. In September 1918 the American army fought its first great independent battle at St. Mihiel, a bulge, or salient, in the German line south of Verdun. About 550,000 American soldiers took part, supported by French troops, tanks, and aircraft. The attack began on September 12 and pinched out the bulge in about four days. Add the honest qualification the reading carries, because students should learn to weigh a victory accurately: the German force in the salient was already pulling back when the attack came, which shortened the fight. St. Mihiel still proved the point Pershing had argued for a year. An American army, under American command, could plan and carry out a large operation of its own. Pershing then moved that army at once to a harder task, and the speed of the move, changing fronts in days, strained the roads and supply lines in ways the next battle exposed.",
             kick='E · St. Mihiel and the Meuse-Argonne')

# ------------------------------------------------------ 16 THE ARGONNE
content_photo_sized('argonne-port.jpg', 'The Meuse-Argonne',
              ['The offensive ran from September 26 to the end of the war.',
               'About 1.2 million American soldiers fought in it.',
               'The ground was forested and hilly, and the roads were clogged.',
               'German defenses were deep and layered.',
               'Progress was slow, and it was bought at high cost.'],
              "The photograph is a German official photograph from the First World War, held by the National Archives, showing dugouts in the Argonne, the underground shelters both armies lived in below the trench lines. From September 26 until the end of the war, about 1.2 million American soldiers fought in the Meuse-Argonne offensive, the largest battle American forces had fought to that date. Describe the ground as the reading does. It was forested and hilly, the roads were clogged with guns, wagons, and ambulances competing for the same few routes, and German defenses were deep, built in layers over ground the German army had held for years. Progress was slow and costly, measured in ridges and villages rather than miles. An estimated 26,000 American soldiers died in the offensive, more than in any other American battle of the war, and that figure is labeled an estimate in the reading and in the guided notes, as it is here.",
              kick='E · St. Mihiel and the Meuse-Argonne', size=20)

# ------------------------------------------------------ 17 STAT 1.2 MILLION
stat('1.2 MILLION', 'American soldiers in the Meuse-Argonne offensive',
     'An estimated 26,000 American soldiers died in the offensive, more than in any other American battle of the war.',
     "Put the two Argonne numbers together and make students hold both at once. About 1.2 million American soldiers fought in the offensive between September 26 and November 11, 1918, which makes it the largest battle American forces had fought to that date, larger than any single battle of the Civil War. An estimated 26,000 of them died there, and the word estimated belongs with the figure every time it is used, in this deck, in the reading, and in student writing. The army that fought this battle had not existed eighteen months earlier. It was registered by local boards, carried across the Atlantic in convoy, trained behind the lines, and held together as an independent force by Pershing's insistence, which is why this lesson teaches mobilization and combat as one story. The next two sections complicate the victory: who was allowed to fight in this army, and what was killing its soldiers besides the enemy.",
     kick='E · St. Mihiel and the Meuse-Argonne')

# ------------------------------------------------- 18 SECTION F DIVIDER
divider_photo('hellfighters-port.jpg', 'Section F', 'A Segregated Army',
              ['About 370,000 Black Americans served,',
               'most of them assigned to labor'],
              "The photograph shows nine decorated soldiers of the 369th Infantry aboard their transport home, wearing the Croix de Guerre France awarded them. Carry the printed disclosure from the lesson documents into the room, because the quick check tests it. This photograph is dated February 12, 1919, after the armistice, and it shows the regiment coming home, not in combat. About 370,000 Black Americans served in the First World War, in an army that was segregated by policy and whose leaders doubted Black soldiers openly. Most Black soldiers were kept out of combat divisions entirely. This section tells both halves of that record: the labor the army assigned, and the combat record one regiment built when a French command, rather than an American one, gave it the chance. Students will meet this same photograph again in the quick check and be asked to read its date before they read its medals.",
              title_size=44)

# ------------------------------------------------------ 19 LABOR AND THE 369TH
content_text('Labor assignments, and the exception',
             ['Most Black soldiers were assigned to labor units.',
              'They unloaded ships, built roads, dug trenches, and buried the dead.',
              'The work was essential, and often dangerous.',
              'The 369th Infantry fought under French command.',
              'The regiment spent about 191 days in the front line, and France decorated it.'],
             "Explain the assignment policy as a decision, not a condition of nature. Most Black soldiers were kept out of combat divisions and assigned to labor units that unloaded ships, built roads, dug trenches, and buried the dead. The work was essential and often dangerous, and it was given to Black soldiers because white officers assumed they were fit for labor rather than combat. Then take the exception slowly. The 369th Infantry, a Black regiment from New York, fought under French command with French weapons and spent about 191 days in the front line, longer than any other American regiment. France decorated the whole regiment with the Croix de Guerre. The reading's sentence is worth repeating in class: the exceptions proved what the policy denied. For the writing task, this section gives students their strongest evidence that a battle-only account of the war leaves out part of the war itself, the part decided by American policy before a soldier reached France.",
             kick='F · A segregated army')

# ------------------------------------------------- 20 SECTION G DIVIDER
divider_photo('flu-port.jpg', 'Section G', 'Influenza and the Cost of the War',
              ['Disease traveled the same routes',
               'as the soldiers'],
              "The photograph shows the emergency hospital during the influenza epidemic at Camp Funston, Kansas, about 1918, from the National Museum of Health and Medicine. Rows of beds fill a converted hall, which is what a training camp looked like when the pandemic arrived. Set up the section's central fact before the numbers. Disease traveled the same routes as the soldiers: the mobilization system concentrated young men from across the country in crowded camps, moved them on crowded trains, and packed them into troopships, which is close to a perfect distribution system for a respiratory disease. Influenza appeared in American camps in the spring of 1918, including Camp Funston, crossed the Atlantic in the troopships, and returned in a far deadlier wave in the autumn, at the height of the fighting in France. The activity's fifth station uses this same photograph with a labeled summary of camp conditions in the autumn of 1918.",
              title_size=40)

# ------------------------------------------------------ 21 THE COST IN NUMBERS
content_text('More deaths from disease than from battle',
             ['About 116,500 Americans died in the war.',
              'Roughly 53,000 of them died in battle.',
              'About 63,000 died from disease and other nonbattle causes.',
              'Most of those deaths came from influenza and pneumonia.',
              'The deadlier wave of influenza struck in autumn 1918.'],
             "Teach the comparison directly, because the second reading question and the exit ticket both draw on it. Of about 116,500 American deaths in the war, roughly 53,000 came in battle and about 63,000 from disease and other nonbattle causes, most of them from influenza and pneumonia. In the American forces, disease killed more soldiers than battle did. The chronology explains how. Influenza appeared in the camps in the spring of 1918, and a far deadlier wave struck in the autumn, at the height of the Meuse-Argonne fighting, filling camp hospitals at home and evacuation hospitals in France at the same time. Doctors and nurses fell sick themselves, training stopped for quarantined units, and some sailings were delayed. All of these figures in this section are the standard Army accounting, rounded, and the influenza figures that follow on the next slide are estimates and are labeled as estimates in the student documents and here.",
             kick='G · Influenza and the cost of the war')

# ------------------------------------------------------ 22 STAT 675,000
stat('675,000', 'estimated American deaths in the influenza pandemic',
     'An estimate, from the Centers for Disease Control and Prevention. Worldwide deaths are estimated at at least 50 million.',
     "Handle this number with its label attached, and teach students to do the same. An estimated 675,000 people died of influenza in the United States in 1918 and 1919. The figure is an estimate, drawn from the Centers for Disease Control and Prevention, not a count, and the reading and guided notes label it as an estimate wherever it appears. Worldwide, estimates of influenza deaths run to at least 50 million, and those estimates are especially uncertain. Compare the scale to the war itself for one sentence only: the pandemic killed several times as many Americans as the war's battlefields did, and it killed them in the same months, in the same age group, often in the same camps and ships the mobilization system had filled. That is why this lesson places influenza inside the war story rather than beside it, and why the influenza pandemic appears in the vocabulary list beside the battles.",
     kick='G · Influenza and the cost of the war')

# ------------------------------------------------- 23 SECTION H DIVIDER
divider_photo('armistice-port.jpg', 'Section H', 'The Armistice',
              ['November 11, 1918: the fighting stops,',
               'at 11 in the morning'],
              "The photograph was taken in the Forest of Compiegne on November 11, 1918, after the agreement for the armistice had been reached, outside the railway carriage Marshal Ferdinand Foch used as his headquarters. Foch, the Allied supreme commander, stands second from the right in the long coat. The photographer is unknown; the image circulated as a press photograph around the world. By November 1918 Germany was losing its allies one by one, its army was falling back along the front, and its leaders had asked for terms. The armistice was signed in that carriage in the early morning and took effect at 11 in the morning, a timing students remember easily and should also read precisely: the fighting stopped by agreement, at an hour set in advance, while soldiers were still in the line on both sides. The next slide separates what the armistice did from what it did not do.",
              title_size=44)

# ------------------------------------------------------ 24 WHAT THE ARMISTICE DID
content_text('An agreement to stop fighting',
             ['The armistice was signed on November 11, 1918.',
              'It took effect at 11 in the morning.',
              'Germany was losing its allies, and its army was falling back.',
              'No peace treaty had yet been written.',
              'Questions about empires, borders, and a league were still open.'],
             "Close the narrative with the distinction the guided notes end on. On November 11, 1918, the two sides signed an armistice, an agreement to stop fighting, which took effect at 11 in the morning. Germany came to that carriage because its allies had left the war, its army was falling back, and its leaders asked for terms. Then draw the line students most need for the lessons ahead. Fighting stopped, but no peace treaty had yet been written, and the questions the war had raised, about empires, borders, and a league to keep the peace, were still unanswered. Those questions belong to the final lesson of the unit, on Wilson's peace and the turn inward, and students should hear this ending as a pause, not a settlement. The army the lesson has followed now begins the trip home, including the men of the 369th on the transport in the photograph they will read in the quick check.",
             kick='H · The armistice')

# ------------------------------------------------------ 25 VOCAB A
vocab4('Words for the system',
      [('conscription', 'compulsory enrollment for military service, also called the draft'),
       ('American Expeditionary Forces', 'the United States forces sent to fight in Europe under General John J. Pershing'),
       ('convoy system', 'the grouping of troopships and supply ships to sail together under naval escort against submarines'),
       ('trench warfare', "fighting from lines of dug trenches facing each other across open ground called no man's land")],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. Conscription: compulsory enrollment for military service, also called the draft. The American Expeditionary Forces: the United States forces sent to fight in Europe under General John J. Pershing. The convoy system: the grouping of troopships and supply ships to sail together under naval escort against submarines. Trench warfare: fighting from lines of dug trenches facing each other across open ground called no man's land. Together the four terms are the lesson's machinery in miniature: how the men were raised, what the force was called, how it crossed, and what it met. Point out that two of the definitions carry their explanation inside them. The convoy definition names the escort and the enemy, and the trench warfare definition names no man's land, so a student who learns the definitions has already learned the system's outline.")

# ------------------------------------------------------ 26 VOCAB B
vocab('Words for the men and the ending',
      [('armistice', 'an agreement to stop fighting, signed on November 11, 1918, that ended the fighting in the First World War'),
       ('Doughboys', 'a nickname for American infantry soldiers in the First World War'),
       ('influenza pandemic', 'the worldwide outbreak of influenza in 1918 and 1919 that killed millions of people, including an estimated 675,000 in the United States')],
      "Three more terms, again matching the guided notes exactly. Armistice: an agreement to stop fighting, signed on November 11, 1918, that ended the fighting in the First World War. Note what the definition does not say. It does not call the armistice a treaty or a surrender, because it was neither; it stopped the fighting and left the peace unwritten. Doughboys: a nickname for American infantry soldiers in the First World War. The reading uses the nickname from section D onward, and students should be able to use it precisely, for infantry, the men who crossed no man's land. Influenza pandemic: the worldwide outbreak of influenza in 1918 and 1919 that killed millions of people, including an estimated 675,000 in the United States. The definition carries the word estimated, and students should keep it there in their own writing. A vocabulary term about a disease, in a war lesson, is itself an argument about what belongs in the story of the war.")

# ------------------------------------------------------ 27 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Mobilization System Stations', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Return to the lesson question: how did the United States mobilize, and what did its soldiers meet in France? Follow one draftee to your verdict.'],
     size=22, color=POWDER, leading=1.3)
rows = [('Activity', 'Mobilization System Stations: five stations, then your verdict'),
        ('Notebook', 'The War at a Glance: mobilization, the crossing, combat'),
        ('Quick check', 'The 369th Infantry Comes Home: the February 1919 photograph'),
        ('Writing', 'How Did the United States Mobilize, and What Did Its Soldiers Meet?')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=19, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.75, 11.5, 0.5, 'Exit ticket: explain the convoy system, state what Pershing refused, give one fact a battle account would miss.',
     size=16, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to its work. How did the United States mobilize, and what did its soldiers meet in France? Students now answer it four ways. In the activity, Mobilization System Stations, they follow one sample draftee through five stations, the draft record, the convoy crossing, the trench diagram, a labeled summary of a soldier's letter home, and a camp influenza report, then chart how the parts of the system depended on one another and defend a verdict about which part the system could least afford to lose. The notebook page keeps the War at a Glance chart they filled in today. The quick check, The 369th Infantry Comes Home, tests whether they can date the February 1919 photograph correctly and read it as a homecoming, not a combat scene. The writing task asks for one paragraph answering the lesson question itself. Next lesson, the focus shifts home, to bonds, posters, laws, and the country the soldiers left.")

dc.save(OUT)
