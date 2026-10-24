#!/usr/bin/env python3
"""Depression and New Deal Lesson 7 deck, "Labor Rising and the Recession of
1937," built to the approved Twenties / Progressive Era pilot system:
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
text(s, 0.9, 5.32, 11.5, 0.4, 'THE DEPRESSION AND NEW DEAL · LESSON 7', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Labor Rising and the Recession of 1937', size=38, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'One year, two ledgers: what workers won, and what the New Deal lost', size=17, color=POWDER)
notes(s, "This photograph, by Sheldon Dick for the Farm Security Administration, shows sit-down strikers inside Fisher Body Plant Number Three in Flint, Michigan, in 1937, seated on car seat cushions at the window entrance they were guarding. Hold that image, because it states the whole lesson before a word of it is taught. In the winter of 1936 and 1937 American workers took the labor law of 1935 into their own hands and won victories no union had won in the mass production industries. In the same calendar year, the President lost a fight with the Senate over the Supreme Court, and the government's own decisions produced a new recession that its opponents named after him. Students should leave able to keep the two ledgers separate and then judge which one ran longer.")

# ------------------------------------------------- 2 · LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("Why did 1937 bring both labor's greatest victories and the New Deal's hardest year?", {})]],
     size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the New Deal change the relationship between Americans and their federal government, and what did it leave undone?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question has two halves that students tend to answer one at a time, and the exit ticket will require both. The first half is labor's: why did 1937 bring the greatest victories American unions had won, at Flint and across the mass production industries? The second half is the administration's: why was the same year the New Deal's hardest, with the court packing plan defeated and a recession beginning inside the recovery? The unit question underneath is the frame for the whole unit, and this lesson feeds it directly, because 1937 is the year the new relationship between workers and their government was tested in both directions at once: the government had given workers a right, and workers, senators, judges, and the economy each decided what that right and that government were worth.")

# --------------------------------------------------- 3 · THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'A law, a tactic, a victory, a defeat, a recession', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', "A law in workers' hands", 'The Wagner Act taken up by the CIO, 1935 to 1937'),
        ('B', 'The sit-down strike', 'Stop work, stay inside, hold the plant'),
        ('C', 'Flint: forty-four days', 'December 30, 1936 to February 11, 1937'),
        ('D', 'Membership, and the cost', 'Toward nine million members; ten dead at Republic Steel'),
        ('E', 'The court packing plan', 'Proposed February 5, 1937; dead in the Senate by July'),
        ('F', 'The Roosevelt recession', 'Cuts and new taxes; unemployment back toward 19 percent'),
        ('G', 'The lesson of 1937', 'Deficit spending accepted in the spring of 1938')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can find their place in their notes by the letters all hour. Sections A and B set up the victory: the Wagner Act of 1935 in the hands of a new federation, the CIO, and the new tactic it carried into the plants, the sit-down strike. Section C is the victory itself, the forty-four days at Flint and General Motors' recognition of the United Auto Workers. Section D holds the victory and its price together: membership climbing toward nine million, and ten dead at Republic Steel. Sections E and F are the administration's year: the court packing fight and the Roosevelt recession. Section G closes with what the administration learned by the spring of 1938, and the table at the end of the guided notes, The Year at a Glance, asks students to rebuild this map themselves.")

# ------------------------------------------------- 4 · SECTION A DIVIDER
divider_text('Section A', "A Law in Workers' Hands",
             'The Wagner Act promised a right. Workers still had to take it up.',
             "Begin where the last lesson ended. The National Labor Relations Act of 1935, the Wagner Act, guaranteed workers the right to organize unions and bargain collectively, and created a board to enforce those rights. A guarantee, however, is not an organization. Somebody had to sign the members, call the meetings, and face the company, and in the mass production industries the established labor movement had largely not done that work, because its unions were built for skilled craftsmen rather than for whole factories. This section covers the men who decided to do the work on a new plan: John L. Lewis and the federation he built inside, and then against, the American Federation of Labor. The distinction to fix in students' minds is one word against another, craft against industry, because everything at Flint follows from it.")

# ------------------------------------------------------ 5 · THE CIO ORGANIZES BY INDUSTRY
content_photo_s('lewis-port.jpg', 'The CIO organizes by industry',
              ['Formed in November 1935, inside the AFL at first.',
               'Chaired by John L. Lewis of the United Mine Workers.',
               'Soon the Congress of Industrial Organizations.',
               'One union for every worker in a plant.',
               'Skilled and unskilled signed the same card.'],
              "The portrait is John L. Lewis in 1937, photographed by Harris and Ewing, and 1937 is the right year to meet him: the year his federation's organizing broke the open shop in automobiles. Lewis had led the United Mine Workers and believed the future of labor lay in the great unorganized industries, steel, autos, rubber, and meatpacking, where the workforce was unskilled or semiskilled and the craft unions had made little headway. In November 1935 his allies formed the Committee for Industrial Organization inside the American Federation of Labor, soon renamed in the guided notes term: the Congress of Industrial Organizations, the federation formed in 1935 to organize workers by whole industry, including the unskilled, rather than by craft. The federation and the AFL soon split. What Lewis built was an organizing machine aimed at whole plants at once, and its first great test came within fourteen months of its founding.",
              kick='A · A law in workers\u2019 hands')

# ------------------------------------------------------ 6 · CRAFT AGAINST INDUSTRY
content_text('Craft against industry',
             ['The older unions kept one union for each skilled trade.',
              'Machinists, electricians, and carpenters sat in separate locals.',
              'Most factory hands belonged to no craft at all.',
              'The CIO put every worker in the plant in one union.',
              'One contract, one bargaining table, and one strike stopped the plant.'],
             "Slow down on this distinction, because students who miss it cannot explain Flint. The older American Federation of Labor unions organized by craft: the machinists in one union, the electricians in another, the carpenters in a third, each guarding its own skilled trade. That structure fitted a building site. It fitted a mass production plant badly, because most of the men and women on an assembly line practiced no single craft; they tended machines, moved parts, and assembled, and no craft union claimed them. Organized by industry, every worker in the plant joins one union, and the plant speaks and stops as one body. That is also what collective bargaining means in practice: negotiation between an employer and a union chosen by the workers over wages, hours, and working conditions. One union chosen by the whole plant is a party an employer cannot divide craft by craft. The next section gives that union its weapon.",
             kick='A · A law in workers\u2019 hands', size=24)

# ------------------------------------------------------ 7 · THE WAGNER ACT IN WORKERS' HANDS
content_text("The Wagner Act in workers' hands",
             ['The law of 1935 guaranteed the right to organize in federal law.',
              'A federal board enforced the right.',
              'Employers were bound to bargain with the chosen union.',
              'Company unions and blacklists were barred.',
              'The law named the right, and organizing made it real.'],
             "State the law's content plainly, from the last lesson, because this lesson is its sequel. The National Labor Relations Act guaranteed workers the right to organize and to bargain collectively through representatives of their own choosing, created the National Labor Relations Board to police elections and unfair practices, and barred employers from interfering, from running company unions, or from punishing union members. Collective bargaining, carried from Lesson 6 and tested again on this unit's test: negotiation between an employer and a union chosen by the workers over wages, hours, and working conditions. Two cautions belong with the law. First, in 1935 and 1936 nobody knew whether the Supreme Court would let it stand, which is why the Court fight later in this lesson connects to Flint. Second, a right on paper organized no one by itself. The CIO's organizers, signing cards plant by plant through 1936, are the bridge between the statute and the strike.",
             kick='A · A law in workers\u2019 hands', size=24)

# ------------------------------------------------- 8 · SECTION B DIVIDER
divider_photo('flint-port.jpg', 'Section B', 'The Sit-Down Strike',
              ['Stop the work. Stay inside.', 'Hold the plant itself.'],
              "This photograph is the title image in a tighter crop: strikers at the window entrance of Fisher Body Plant Number Three, Flint, in 1937, photographed by Sheldon Dick. Look at how unmilitary it is. Men sit on car seat cushions in work clothes, reading, talking, and watching the window they are guarding. That is the tactic in one frame, and its quietness was its strength. The guided notes definition should be read aloud here: a sit-down strike is a strike in which workers stop work and remain inside the factory, holding the plant so that replacement workers cannot be brought in. Every part of that definition does work: stop work, remain inside, hold the plant, and the purpose stated at the end, that replacement workers cannot be brought in. The next slide takes the definition apart against the ordinary strike it replaced.",
              title_size=40)

# ------------------------------------------------------ 9 · LIFE INSIDE THE HELD PLANT
content_photo_s('meal-port.jpg', 'Life inside the held plant',
              ['Committees handled food, sanitation, and defense.',
              'Meals were served in the plant cafeteria, in shifts.',
              'Beds were made beside the machines.',
              "A women's auxiliary outside provided food, pickets, and support.",
              'Discipline inside was the strike\u2019s public argument.'],
              "The photograph shows strikers eating in the cafeteria of Fisher Body Plant Number Three during the occupation, photographed by Sheldon Dick in 1937. An occupation of weeks is a logistics problem before it is anything else: hundreds of men had to be fed, kept clean, kept sober, and kept from damaging the machinery their jobs depended on. The strikers organized the plant like a small city, with committees for food, sanitation, entertainment, and defense, rules against drinking and against harming company property, and classes and boxing matches to hold morale. Outside, the Women's Auxiliary, wives, mothers, and sisters of the strikers, ran kitchens, raised money, and picketed, and when the crisis came it was the auxiliary's Emergency Brigade that stood in the street. Discipline inside was a political argument: a company that called the strikers lawless was answered by photographs of men eating in shifts and sweeping the floor of a plant they intended to work in again.",
              kick='B · The sit-down strike')

# ------------------------------------------------------ 10 · 44 DAYS STAT
stat('44 days', 'the Flint sit-down strike, December 30, 1936 to February 11, 1937',
     'Fisher Body plants in Flint, Michigan · Ended with General Motors recognizing the United Auto Workers',
     "Dwell on the length, because forty-four days is what separates Flint from a walkout. The strike began on December 30, 1936, at the Fisher Body plants, and spread until it stopped General Motors, the largest car maker in the country, because Fisher Body supplied bodies to the whole corporation: hold the body plants and the assembly lines starve. For forty-four days the men inside held the plants through winter, through a court injunction ordering them out, which they ignored, and through the fight of January 11 that the next slide covers. On February 11, 1937, General Motors signed a one page agreement recognizing the union. The guided notes term, in full: the United Auto Workers, the union of automobile workers, recognized by General Motors in February 1937 after the Flint sit-down strike. Students should pair the number on this slide with that recognition every time they use it: forty-four days bought a signature, and the signature is the fact.",
     kick='C · Flint')

# ------------------------------------------------------ 11 · THE BATTLE AND THE GOVERNOR
content_photo_s('guard-port.jpg', 'The battle, and the governor who refused',
              ['On January 11, police tried to retake Fisher Body Number Two.',
              'Fire hoses, car door hinges, and bottles answered them.',
              'The fight is remembered as the Battle of the Running Bulls.',
              'Governor Frank Murphy sent the National Guard.',
              'His order was to keep order, not to evict.'],
              "The photograph shows a National Guard machine gun position overlooking the Chevrolet plants at Flint, from Sheldon Dick's series of 1937. Two decisions decided Flint, and students should be able to name both. The first was the strikers': on January 11, when police cut off heat and tried to retake Fisher Body Number Two, the men fought back with fire hoses, hinges torn from car doors, and bottles, and women of the Emergency Brigade broke plant windows from outside so the tear gas could clear; the police retreated, and the day was named the Battle of the Running Bulls. The second decision was Governor Frank Murphy's. He sent the National Guard to Flint, as governors had sent troops to strikes for fifty years, but he ordered it to keep order and protect life, and he refused to use it to drive the men out. Deprived of eviction by the state and of replacements by the sit-down, General Motors negotiated.",
              kick='C · Flint')

# ------------------------------------------------- 12 · SECTION D DIVIDER
divider_text('Section D', 'Membership Climbs, and the Cost',
             'Flint set off a wave. The wave broke against steel.',
             "Flint was not an ending but a signal. Workers across the mass production industries read the settlement the same way: the largest corporation in America had recognized a union of its own workers, the government of Michigan had declined to break the strike, and the Supreme Court was about to uphold the law that stood behind it. Organizers who had been signing cards quietly for two years now found lines at their doors. This section holds the two facts of 1937 together, in one breath, because the lesson question requires them together: the fastest growth of union membership in the country's history, and, in Chicago five months after Flint, the bloodiest day of the organizing era. Students who carry only the first fact forward will write half an essay on the writing task; the Memorial Day Massacre is the second fact, and it belongs in the same ledger.")

# ------------------------------------------------------ 13 · 9 MILLION STAT
stat('Toward 9,000,000', 'union members by the end of the decade',
     'Under 3,000,000 in 1933 · The fastest growth in the history of American labor to that point',
     "These figures are the reading's, and they should be stated with the reading's own caution built in: from under three million union members in 1933 toward nine million by the end of the decade. The tripling is the point, not false precision about any single year. Behind the numbers sits a change in who a union member was. The labor movement of 1932 had been a movement of skilled craftsmen, miners, and railroad men. The movement of 1939 included auto workers, steelworkers, rubber workers, packers, and longshoremen, organized by industry under the CIO, together with the older federation's unions, which grew as well once organizing proved possible. Political weight followed membership: a movement of nine million members, with families, was a constituency no national politician could ignore, and it became a pillar of the coalition the final lesson examines. The next slide is the price that was still being charged for a union card in 1937, in the middle of the climb.",
     kick='D · Membership and the cost')

# ------------------------------------------------------ 14 · MEMORIAL DAY
content_text('Memorial Day at Republic Steel',
             ['On May 30, 1937, strikers and families marched to set a picket line.',
             'Chicago police blocked the field and fired into the crowd.',
             'Ten people were killed, most of them shot from behind.',
             'A Senate committee found the police violence unjustified.',
             'The newsreel film was kept out of public theaters.'],
             "Teach this slide slowly, because it is the counterweight to Flint and the lesson fails without it. Republic Steel's chairman, Tom Girdler, had refused to sign an agreement with the steelworkers' union, and on Memorial Day, May 30, 1937, strikers and their families, about a thousand people in Sunday clothes, marched across an open field in South Chicago to establish a picket line at the plant. Chicago police blocked the field; there was a brief confrontation, and the police fired into the crowd as it fell back. Ten people were killed, most of them shot in the back or the side, and dozens were wounded. A Senate committee under Robert La Follette investigated and found the violence unjustified. The newsreel film of the shooting was withheld from theaters as too disturbing, so the country largely read the police version. Organizing had the law, the numbers, and the momentum, and it still buried ten of its own that spring.",
             kick='D · Membership and the cost', size=24)

# ------------------------------------------------- 15 · SECTION E DIVIDER
divider_photo('fdr-port.jpg', 'Section E', 'The Court Packing Plan',
              ['A landslide in November.', 'A defeat by July.'],
              "The photograph shows President Roosevelt at a microphone in 1937, by Harris and Ewing, in the year he made the largest political mistake of his presidency. Set the scene in one sentence: in November 1936 Roosevelt had been reelected carrying forty-six of the forty-eight states, the greatest landslide of the era, and he read it as a mandate to settle the one institution that had blocked him, the Supreme Court, which in 1935 and 1936 had struck down the National Industrial Recovery Act and the Agricultural Adjustment Act and was expected to rule on the Wagner Act and Social Security next. On February 5, 1937, he proposed to add a justice for each sitting justice over seventy, up to six. Opponents named it in the guided notes term: court packing, the name opponents gave Roosevelt's 1937 proposal to add a new justice to the Supreme Court for each sitting justice over seventy, which would have let him appoint up to six.",
              title_size=38)

# ------------------------------------------------------ 16 · FEBRUARY 5, 1937
content_text('February 5, 1937: the proposal',
             ['The stated reason was crowded dockets and aged judges.',
              'The plan added a judge for each judge over seventy who stayed.',
              'It allowed up to six new justices on a Court of nine.',
              'The decisions of 1935 and 1936 were never mentioned.',
              'Opponents named it court packing at once.'],
             "Use the activity's third station to teach this slide, because the message's own words are the evidence. Roosevelt's message to Congress argued workload and age: the federal judiciary's personnel, he wrote, was insufficient to meet the business before them, and life tenure was not intended to create a static judiciary; younger blood would vitalize the courts. What the message never mentioned was the grievance everyone in Washington understood, the Court's destruction of New Deal statutes in 1935 and 1936 and the rulings expected on the Wagner Act and Social Security. Opponents, including much of the press and many Democrats, measured the remedy against the reasons and found the fit exact for the unstated purpose: new judges only where a judge was over seventy, and up to six appointments at once, for this president. The name they gave it, court packing, stuck, and names in politics are verdicts delivered early.",
             kick='E · The court packing plan', size=24)

# ------------------------------------------------------ 17 · THE COURT CHANGES COURSE
content_text('The Court changes course',
             ['In March 1937, a state minimum wage law was upheld.',
             'In April 1937, the Wagner Act was upheld.',
             'In May 1937, Social Security was upheld.',
             'One justice retired, and the threat of enlargement receded.',
             'The laws survived, and the plan had become unnecessary.'],
             "The chronology on this slide surprised contemporaries and still organizes the argument. While the Senate fought over the bill, the Court itself moved. In March it upheld a Washington state minimum wage law in West Coast Hotel against Parrish, reversing its earlier position, with Justice Owen Roberts changing sides, a move wits named the switch in time that saved nine. In April the Court upheld the Wagner Act in the Jones and Laughlin case, securing everything Flint had won. In May it upheld the Social Security Act. In June, Justice Van Devanter, one of the plan's targets, retired, giving Roosevelt his first appointment. Historians still argue about how much the plan pressured the Court, since Roberts had voted in conference before the plan was announced; what is not argued is the political result. The New Deal's laws were safe, and the bill to enlarge the Court had lost its reason to exist, while its costs were still being counted.",
             kick='E · The court packing plan', size=24)

# ------------------------------------------------------ 18 · DEFEAT IN THE SENATE
content_text('Defeat in the Senate',
             ['His own party\u2019s senators led the resistance.',
             'The Judiciary Committee reported against the bill.',
             'In July 1937, the Senate sent the bill back to committee.',
             'The landslide\u2019s authority was spent on one fight.',
             'The conservative coalition in Congress dates from here.'],
             "Close the court fight with its cost, because the cost is the lesson's point. Roosevelt had expected his landslide to carry the Senate; instead the Senate Judiciary Committee, with Democrats in the majority, reported the bill adversely in language calling it an invasion of judicial independence, and the administration's Senate leader, Joseph Robinson, died in the middle of the fight. In July 1937 the Senate voted to send the bill back to committee, where it died, and a modest judgeship bill took its place. Roosevelt won the substance, the Court upheld his laws, and lost the fight, and the manner of the loss had a long tail: southern Democrats and Republicans who had combined to kill the bill learned they could combine, and the conservative coalition that limited every later New Deal measure is conventionally dated from this battle. The authority of November 1936 was real, and by July 1937 much of it was spent.",
             kick='E · The court packing plan', size=24)

# ------------------------------------------------- 19 · SECTION F DIVIDER
divider_text('Section F', 'The Roosevelt Recession',
             'The recovery ran backward, and the government\u2019s own hand was on it.',
             "The second defeat of 1937 was not voted in the Senate; it appeared in the production figures. Through the middle of 1937 the administration believed the recovery had taken hold, and Roosevelt, who had never stopped worrying about the federal debt, cut spending and shrank the relief rolls to move toward a balanced budget. At the same moment, the Social Security payroll taxes that had begun in January 1937 were taking money out of millions of pay envelopes for benefits that would not be paid monthly until 1940, and the Federal Reserve, fearing inflation in a still weak economy, tightened credit. The guided notes definition holds the whole section: the Roosevelt recession, the sharp economic downturn of 1937 to 1938, caused in part by federal spending cuts and new payroll taxes pulling money out of a weak economy. Caused in part is the honest phrase, and students should keep it; the section teaches contribution, not sole cause.")

# ------------------------------------------------------ 20 · MONEY PULLED OUT
content_text('Money pulled out, twice',
             ['Federal spending was cut, and the relief rolls shrank.',
             'Payroll taxes began in January 1937.',
             'Benefits those taxes funded were not payable until 1940.',
             'Each withdrawal was defended on its own terms.',
             'Together, demand fell out of a weak economy.'],
             "Work through the two withdrawals separately before joining them, as the activity's fourth station does. The spending cut was defended as responsibility: the emergency was ending, recovery seemed real, and a balanced budget was the era's mark of sound government, believed in by Roosevelt himself. The payroll taxes were defended as insurance: workers and employers were funding a permanent system of old-age benefits, contributions today for pensions tomorrow, and the taxes were the price of making Social Security a right rather than a dole. Either defense, alone, was respectable. Together, in a single year, they withdrew money from both directions of the same weak economy: the government spent less into it, and workers took home less from it, while the pensions the taxes funded would not flow back until 1940. The production index fell from 117 in August 1937 to 76 in May 1938, about a third, and the political name for the result attached itself to the President.",
             kick='F · The Roosevelt recession', size=24)

# ------------------------------------------------------ 21 · 19 PERCENT STAT
stat('19 percent', 'unemployment in 1938, climbed back from about 14 percent in 1937',
     'Industrial production fell by about a third between the summer of 1937 and the spring of 1938',
     "Put the number against the unit's whole arc. Unemployment had stood near twenty-five percent at the depth in 1933; the New Deal's years had brought it down to about fourteen percent in 1937, still high, but a country moving. Within months of the spending cuts and the new taxes, it was climbing back toward nineteen percent, and something like two million workers who had found jobs lost them again. That reversal is why the name Roosevelt recession was so damaging: the downturns of 1930 to 1933 could be laid at Herbert Hoover's door and at the collapse itself, but this one began in the fifth year of the New Deal, under a president reelected in a landslide, with his own fiscal decisions among its causes. For the guided notes, the figures to fix are these: about fourteen percent in 1937, back toward nineteen percent in 1938, production down about a third. The next section is the administration's answer, and it amounted to admitting the mechanism of this slide.",
     kick='F · The Roosevelt recession')

# ------------------------------------------------- 22 · SECTION G: THE LESSON OF 1937
content_text('The spring of 1938: spending again',
             ['The administration reversed itself.',
             'New spending was asked of Congress, and granted.',
             'Deficit spending was accepted in practice.',
             'Production recovered, and unemployment stayed high.',
             'The argument over the lesson has run ever since.'],
             "Section G is short and should be taught as a conclusion drawn under pressure. By the spring of 1938, with the recession deepening and the midterm elections ahead, Roosevelt asked Congress for a new spending program of some three billion dollars, and Congress granted it. In doing so the administration accepted, in practice if not in doctrine, the principle its economists had urged: deficit spending, government spending beyond the revenue it collects, financed by borrowing, used to put money into an economy in a slump, stated here in the guided notes definition in full. Production turned up again within months, which contemporaries and historians both read as evidence about what had caused the fall. Unemployment stayed high, near nineteen percent for 1938 as a whole, and full recovery waited for the war spending of the next decade. The argument the recession started, about whether government spending sustains or burdens a weak economy, has never actually closed; students are meeting its first American round.",
             kick='G · The lesson of 1937', size=24)

# ------------------------------------------------------ 23 · TWO LEDGERS AT A GLANCE
s = slide(NAVY)
kicker(s, 'The year at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Two ledgers, one year', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Won', 'Flint settled; the Wagner Act upheld; membership toward nine million', 'Labor entered 1938 organized as never before'),
        ('Paid', 'Ten dead at Republic Steel; the right unevenly protected', 'Victory and its price in the same season'),
        ('Lost', 'Court packing killed in the Senate; the landslide spent', 'A limit found on presidential power'),
        ('Learned', 'Cuts and taxes together made a recession', 'Deficit spending accepted by the spring of 1938')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.2, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.25, yy + 0.05, 5.1, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.55, yy + 0.05, 3.9, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the closing table of the guided notes, The Year at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. Won: the Flint settlement, with General Motors recognizing the United Auto Workers; the Supreme Court upholding the Wagner Act in April 1937; membership climbing from under three million toward nine million. Paid: the Memorial Day Massacre at Republic Steel, ten killed on May 30, 1937, with the Senate's later finding that the violence was unjustified, the proof that the right was still unevenly protected. Lost: the court packing plan, proposed on February 5, 1937 and dead in the Senate by July, and with it much of the authority of the 1936 landslide. Learned: that cutting spending while starting payroll taxes withdrew money from a weak economy and produced the Roosevelt recession, and that the administration reversed itself into deficit spending by the spring of 1938.")

# ------------------------------------------------------ 24 · VOCAB A
vocab('Words for the organizing',
      [('sit-down strike', 'workers stop work and remain inside the factory, holding the plant'),
       ('Congress of Industrial Organizations', 'the federation that organized workers by whole industry, including the unskilled'),
       ('United Auto Workers', 'the auto workers\u2019 union, recognized by GM in February 1937 after Flint'),
       ('collective bargaining', 'negotiation between an employer and a union chosen by the workers')],
      "These definitions match the guided notes, and the notes carry them in full. A sit-down strike: a strike in which workers stop work and remain inside the factory, holding the plant so that replacement workers cannot be brought in. The Congress of Industrial Organizations: the federation formed in 1935 to organize workers by whole industry, including the unskilled, rather than by craft. The United Auto Workers: the union of automobile workers, recognized by General Motors in February 1937 after the Flint sit-down strike. Collective bargaining, the term carried from Lesson 6: negotiation between an employer and a union chosen by the workers over wages, hours, and working conditions. Note for students that three of these four terms name the victory's machinery, the tactic, the federation, and the union, while the fourth names what the machinery was for: bargaining, the ordinary work that recognition made possible every year after the strike ended.")

# ------------------------------------------------------ 25 · VOCAB B
vocab('Words for the hard year',
      [('court packing', 'the name opponents gave the plan to add a justice for each justice over seventy'),
       ('Roosevelt recession', 'the downturn of 1937 to 1938, fed by spending cuts and new payroll taxes'),
       ('deficit spending', 'government spending beyond its revenue, used to put money into a slumping economy')],
      "Three more terms, again in the guided notes wording, carried here in the notes in full. Court packing: the name opponents gave Roosevelt's 1937 proposal to add a new justice to the Supreme Court for each sitting justice over seventy, which would have let him appoint up to six. Students should notice that the vocabulary itself records a political defeat: the term in the textbook is the opponents' name for the plan, not the president's, whose phrase was reorganization of the judicial branch. The Roosevelt recession: the sharp economic downturn of 1937 to 1938, caused in part by federal spending cuts and new payroll taxes pulling money out of a weak economy. Deficit spending: government spending beyond the revenue it collects, financed by borrowing, used to put money into an economy in a slump. The three terms form a sentence when read in order: a president weakened by the court fight then met a recession his own fiscal choices had fed, and answered it by spending beyond revenue.")

# ------------------------------------------------------ 26 · CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ["Why did 1937 bring both labor's greatest victories and the New Deal's hardest year? Keep the two ledgers separate, then judge which one ran longer."],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'Two Ledgers of 1937: the Flint settlement, the Memorial Day record, the court message, the recession table'),
        ('Notebook', 'Notebook page: the year in two ledgers, in your own words'),
        ('Quick check', 'The Guard at Flint: the photograph, the governor\u2019s order, the court plan, the recession'),
        ('Writing', 'Two Ledgers of One Year: the lesson question as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: how a sit-down strike worked, the two withdrawals that made the recession, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, Two Ledgers of 1937, runs four documents of the year: a teaching summary of the Flint settlement, the Senate investigation's record of the Memorial Day killings, Roosevelt's February 5, 1937 message on the courts quoted in his own words, and a production and unemployment table, ending in two ledgers the students keep themselves and a judgment about which ledger ran longer. The notebook page asks for the year's account in chart form. The quick check, The Guard at Flint, works from Sheldon Dick's photograph of the National Guard and tests the governor's decision, the sit-down mechanism, the court plan, and the recession's causes. The writing task, Two Ledgers of One Year, turns the lesson question into an essay. The exit ticket has three parts: the sit-down mechanism explained, the two withdrawals of money named, and the lesson question answered in two or three sentences with two facts. The final lesson steps back from 1937 to judge the whole New Deal, and this lesson's two ledgers are its raw material.")

dc.save(OUT)
