#!/usr/bin/env python3
"""Depression and New Deal Lesson 5 deck, "The Critics: Long, Townsend, Coughlin,
and the Court," built to the approved Twenties system: image-led slides,
fragments only on screen, comprehensive speaker notes, full lesson and
vocabulary coverage. Fonts: Georgia titles, Lato body."""
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


def cphoto(img, title, items, note, kick=None, size=24):
    s = slide(CREAM)
    photo_right(s, img)
    if kick: kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95 if kick else 0.8, 6.9, 1.2, title, size=31, color=NAVY, font='Georgia', leading=1.05)
    frags(s, items, y=2.15 if kick else 2.0, size=size)
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
text(s, 0.9, 5.32, 11.5, 0.4, 'THE DEPRESSION AND NEW DEAL · LESSON 5', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Critics: Long, Townsend, Coughlin, and the Court', size=36, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Attack from every direction, 1934 to 1936', size=17, color=POWDER)
notes(s, "The photograph shows Senator Huey Long of Louisiana leaving the Senate floor in August 1935, after a filibuster of five and a half hours, weeks before his assassination. It is the right doorway into this lesson, because Long is the first of the critics and because the picture was taken at the height of his national campaign. Set the scene before any names. By the start of 1935 the New Deal had run for two years without ending the Depression. Millions remained out of work, and the recovery was thin and uneven. A program of that size drew judgment as it went, and by 1935 the judgments arrived from opposite directions at once. Three mass movements argued the New Deal did too little. Wealthy opponents and the Supreme Court argued it did too much. This lesson follows the attacks in the order of the guided notes, and it ends where the pressure points: at the Second New Deal of 1935, which the next lesson takes up.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('Why did the New Deal draw attack from every direction by 1935, and what did the attacks reveal about the country?', {})]],
     size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the New Deal change the relationship between Americans and their federal government, and what did it leave undone?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question has two halves, and students should hear both before the lesson starts. Why did the attack come from every direction, and what did the attacks reveal about the country? The revealing half does the analytical work. An attack is evidence about the attacker and about the public behind him. Long's following revealed a country in which great fortunes had survived the crash while family incomes had not. The Townsend petitions revealed that old age, the need the first New Deal had answered least, had organized itself. The Supreme Court's decisions revealed that the constitutional limits of 1789 still governed a government trying to manage a modern economy. Hold students to the two-direction structure all hour. A summary that lists five critics without separating the charge of too little from the charge of too much has missed the lesson's argument, and the writing task is scored on exactly that distinction.")

# --------------------------------------------------- 3 THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Too little, too much: the two fronts', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'Attacked from both sides', 'Two years in, recovery thin and uneven'),
        ('B', 'Huey Long and Share Our Wealth', 'Cap fortunes, guarantee a family floor'),
        ('C', 'Townsend and the old-age pension', 'Two hundred dollars a month, spent within the month'),
        ('D', 'Coughlin and the radio audience', 'From supporter to opponent, 1934'),
        ('E', 'The American Liberty League', 'Property, debt, and the Constitution'),
        ('F', 'Schechter: the Court strikes', 'Delegation and commerce, 1935'),
        ('G', 'Butler and the two fronts', 'The farm act falls, 1936; pressure becomes law')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A sets the two-front problem. Sections B, C, and D take the three movements that charged the New Deal with doing too little: Huey Long and Share Our Wealth, Dr. Francis Townsend and the old-age pension, and Father Charles Coughlin and his radio audience. Section E crosses to the other front, the American Liberty League, wealthy men arguing the New Deal had done too much. Sections F and G give that argument its legal form: Schechter in 1935 striking the recovery act, and Butler in 1936 striking the farm act's tax. Tell students the final table in their guided notes, The Pressure at a Glance, asks them to rebuild exactly this map, critic by critic, from memory.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', 'Attacked From Both Sides',
             'Two years into the New Deal, the judgments arrived at once.',
             "Open with the condition of the country, because the attacks make no sense without it. By the start of 1935 the New Deal had run for two years without ending the Depression. Millions remained out of work. Farm prices and wages had recovered only in part, and the recovery that existed was thin and uneven. A smaller program might have escaped judgment. A program that had promised recovery, and had reorganized banking, farming, and industry in two years, invited it from everyone it had disappointed and everyone it had alarmed. Name the two directions before the details. From one side, mass movements argued the New Deal did too little, saying recovery would never come while a few men held most of the nation's wealth. From the other side, wealthy opponents and the Supreme Court argued it did too much, taking powers left to Congress and the states. Roosevelt faced both attacks in the same season.")

# ------------------------------------------------------ 5 TWO CHARGES
content_text('Two charges at once',
             ['The too little charge said recovery would never come while a few men held most of the wealth.',
              'The too much charge said the New Deal took powers left to Congress and the states.',
              'The first charge came with clubs, petitions, and radio audiences.',
              'The second charge came with money, lawyers, and finally the Court.'],
             "Put the two charges in their strongest form, because students will spend the lesson testing them. The first charge said the Depression was a crisis of distribution: the country produced enough, but a few men held most of the wealth, the old had no income of their own, and no program that left that arrangement untouched could restore prosperity. The second charge said the New Deal was a crisis of the Constitution: Congress had handed its lawmaking power to the president, federal agencies regulated business the Constitution left to the states, and the debt climbed every year. Notice what each charge presupposes. The first treats economic security as the federal government's business and faults it for doing the business timidly. The second denies that the business belongs to the federal government at all. A president could answer one charge only by deepening the other, which is why 1935 was such a difficult year, and why the answer, when it came, took the shape it did.",
             kick='A · Attacked from both sides', size=24)

# ------------------------------------------------- 6 SECTION B DIVIDER
divider_photo('long-port.jpg', 'Section B', 'Huey Long and Share Our Wealth',
              ['A senator, a radio audience,', 'and a club in every state.'],
              "The photograph shows Long speaking in 1935, gesturing with both arms, and it comes from the Library of Congress. Introduce the man before the program. Long had been governor of Louisiana, where he built roads, schools, and hospitals and concentrated power in his own hands to do it, and he now sat in the United States Senate. He was the loudest voice on the too little side, and the only critic in this lesson who held national office while he attacked. On February 23, 1934, in a national radio address, he announced the Share Our Wealth Society. Local clubs spread across the country, and the organization soon claimed millions of members. Radio did for Long what it did for Roosevelt: it carried one voice into millions of homes at the same hour. The difference is that Roosevelt spoke as president, and Long spoke as the president's rival in waiting.",
              title_size=40)

# ------------------------------------------------------ 7 EVERY MAN A KING
content_photo_s('long-port.jpg', 'Every Man a King',
              ['Long announced the Share Our Wealth Society on February 23, 1934.',
               'His promise was to limit poverty, not to divide wealth equally.',
               'He guaranteed a family floor of around $5,000 in wealth.',
               'He said $5,000 was enough for a home, an automobile, and a radio.',
               'He also promised an old-age pension of thirty dollars a month.'],
              "Read the plan through Long's own distinction, because it is the part students most often get backwards. Long did not propose to divide the nation's wealth equally, and he said so in the address itself: We do not propose to divide it up equally. We do not propose a division of wealth, but we propose to limit poverty that we will allow to be inflicted upon any man's family. The guarantee, as he gave it, was family wealth of around $5,000, enough for a home, an automobile, and a radio, with a pension of thirty dollars a month beside it. In the guided notes definition, Share Our Wealth is Huey Long's program and movement, begun in 1934, which promised to cap large fortunes and guarantee every family a homestead and a minimum income. The next slide takes up where the money was to come from: the cap on fortunes itself.",
              kick='B · Huey Long and Share Our Wealth', size=19)

# ------------------------------------------------------ 8 STAT: $5,000
stat('$5,000', 'the family wealth Long promised to guarantee',
     'Funded by capping large fortunes · Average family wealth, by Long\'s own figure in the address: about $15,000',
     "Dwell on where the guarantee was to come from, because the mechanism is the program. The plan capped large fortunes and spent the proceeds on the guaranteed floor for every family. In the February 1934 address Long raised the cap question directly, saying the plan would allow no one man to own more than $50,000,000, and that the limit might have to come lower as the program was worked out. Do the comparison he invited his listeners to do. A family floor of $5,000 was, by his own arithmetic, one third of the average family wealth of about $15,000 he cited in the same address: a floor far below equality, which he used to answer the charge that he proposed to divide everything evenly. Then give the ending of the story. Long was shot in the state capitol in September 1935 and died two days later. The movement lost its leader, but the administration had already taken its measure: a senator broadcasting to millions could build a national following on the charge that the New Deal had left great fortunes untouched, and the White House feared a challenge in 1936.",
     kick='B · Huey Long and Share Our Wealth')

# ------------------------------------------------- 9 SECTION C DIVIDER
divider_photo('townsend-port.jpg', 'Section C', 'Townsend and the Old-Age Pension',
              ['One plain idea, organized', 'in nearly every congressional district.'],
              "The photograph shows Dr. Francis Townsend seated at a desk before NBC microphones, in a Harris and Ewing photograph held by the Library of Congress. Townsend was a retired California physician, in his late sixties when the Depression took his own small savings and his position, and he built his movement on one plain idea that fit on an index card. Where Long offered a whole program, Townsend offered a single number, and the simplicity was the strategy: anyone could repeat it, anyone could check whether Congress had passed it, and every older American could measure it against an empty purse. The movement he built carried petitions rather than a candidate, and it aimed at Congress district by district rather than at the White House. Keep the contrast with Long in front of students as the section runs: a program with a leader against a number with a petition.",
              title_size=38)

# ------------------------------------------------------ 10 THE PLAN
content_photo_s('townsend-port.jpg', 'Retire, and spend it all',
              ['The plan paid two hundred dollars a month to every citizen over sixty.',
               'The first condition was to give up regular work for pay.',
               'The second condition was to spend the whole payment within the month.',
               'Older workers would retire, and younger workers would take their places.',
               'Townsend argued that the spending itself would end the slump.'],
              "State the plan exactly, because the guided notes test its conditions. The federal government would pay two hundred dollars a month to every citizen over sixty. Each pensioner had to retire and spend the whole payment within the month, so the money passed at once into local stores. In the guided notes definition, the Townsend Plan is Dr. Francis Townsend's proposal that the federal government pay two hundred dollars a month to every citizen over sixty, on condition the money be spent within the month. An old-age pension, in the guided notes, is a regular payment made by a government to people who have reached a set age and left regular work. Notice the economic engine inside the plan. The pensioner is not a charge on the economy but its motor: his required spending restarts demand, and his retirement opens his job. Whether the arithmetic worked is the next slide's question; that the plan was designed, and not merely generous, is this slide's point.",
              kick='C · Townsend and the old-age pension', size=19)

# ------------------------------------------------------ 11 STAT: $200
stat('$200', 'a month, to every citizen over sixty',
     'Townsend clubs in nearly every congressional district · Petitions reached Congress by the million',
     "Now weigh the plan, because contemporaries did, and students should practice the weighing on the record. Economists of the day named the weakness plainly: paying two hundred dollars a month to every older citizen would have cost a large share of the national income, and the transactions tax proposed to fund it fell on the very spending the plan hoped to create. Two hundred dollars also exceeded what many working families earned, which made the figure implausible as policy and irresistible as organizing. Then set the arithmetic aside and state the political fact, which the reading sets apart from it. Old age was where the Depression lasted longest and charity reached least. Townsend clubs organized in nearly every congressional district, and petitions reached Congress by the million. The old were now a force no member of Congress could safely ignore. When the Social Security Act arrived in August 1935, with a far smaller old-age benefit, it arrived in a country Townsend had prepared for it.",
     kick='C · Townsend and the old-age pension')

# ------------------------------------------------- 12 SECTION D DIVIDER
divider_photo('coughlin-port.jpg', 'Section D', 'Coughlin and the Radio Audience',
              ['The largest audience of the three,', 'gathered by one voice each week.'],
              "The photograph is the portrait of Father Charles Coughlin by Craine of Detroit, dated 1933, held by the Library of Congress. Coughlin was a Catholic priest broadcasting from Royal Oak, Michigan, and he reached the largest audience of the three critics in this lesson: his weekly talks were counted in the tens of millions of listeners. Radio was the common instrument of the age. Roosevelt used it to explain the banking system. Long used it to announce a society. Coughlin used it every week, and a weekly audience is a different political fact from a single address: it is a congregation that returns. Like the other two, he began as a Roosevelt supporter. Unlike them, he built no pension plan and no wealth cap. His subject was the money system itself, and his weapon was the framing of a fight. The summaries in this section describe his program; they are not quotations from the broadcasts, and students should note the difference.",
              title_size=38)

# ------------------------------------------------------ 13 SUPPORTER TO OPPONENT
content_text('From supporter to opponent',
             ['His talks had backed Roosevelt in the early New Deal.',
              'By 1934 he was attacking bankers and the Federal Reserve.',
              'In November 1934 he founded the National Union for Social Justice.',
              'Summaries describe his program as monetary change and public control of key industries.',
              'He framed the fight as the people against a small circle of financiers.'],
             "Trace the turn carefully, because it is the evidence students will use when they test the word demagogue. Coughlin's talks had backed Roosevelt in the early New Deal. By 1934 he had turned on the administration, attacking bankers and the Federal Reserve, and in November he founded the National Union for Social Justice to organize his listeners. Summaries of the broadcasts describe a program of monetary change and public control of key industries, framed as a fight against a small circle of financiers. Now give the term, from the guided notes: a demagogue is a leader who gains power by arousing popular fears, prejudices, and hopes with simple promises, rather than by answering arguments. Do not settle the label in class. The reading treats it as a judgment to be tested man by man against what each proposed. Long stated figures and a funding mechanism. Townsend stated a figure, conditions, and a tax. Coughlin's case rests on how much of his appeal was program and how much was the framing of enemies.",
             kick='D · Coughlin and the radio audience', size=23)

# ------------------------------------------------- 14 SECTION E DIVIDER
divider_text('Section E', 'The American Liberty League',
             'Money and standing, but no mass membership.',
             "Cross now to the other front, and mark how different the crossing feels. The three movements filled clubs, petition lists, and radio audiences. The American Liberty League filled offices. In the guided notes definition, the American Liberty League is the organization founded in 1934 by wealthy businessmen and conservative Democrats to oppose the New Deal as a threat to property and the Constitution. Its leaders included former Democratic candidates for president, which gave its attack a particular sting: this was not the Republican opposition but a revolt inside Roosevelt's own party's wealthy wing. The League published pamphlets, placed statements in newspapers, and testified against administration bills. It enrolled no mass membership and ran no candidates. Everything about its method assumed that arguments move governments. The next slide states the argument; the sections after it show where the argument found its real power, in a courtroom rather than in print.")

# ------------------------------------------------------ 15 THE CHARGE OF TOO MUCH
content_text('The charge of too much',
             ['The League said the New Deal threatened property.',
              'It said spending piled up public debt.',
              'It said federal agencies regulated business beyond the Constitution.',
              'It said relief and planning moved toward government control of economic life.',
              'Its remedy was to hold federal power within narrow limits.'],
             "State the League's case at full strength before weighing it, as the activity asks students to do. The League held that the New Deal threatened property, piled up debt, and moved toward government control of business, defending a Constitution read to keep federal power narrow. Each charge had a factual root students can check: the debt did climb, the agencies did write rules for whole industries, and the codes did set prices and wages. Then weigh the League as a political force. Defending great wealth in a depression made it an easy target, and it never won a following among voters; the administration treated its pamphlets as proof that the wealthy opposed recovery itself. Its claim, though, traveled further than its organization. The claim that the New Deal had passed the Constitution's limits was also a lawyer's claim, about to be heard in the Supreme Court, where followings do not count and arguments do.",
             kick='E · The American Liberty League', size=24)

# ------------------------------------------------- 16 SECTION F DIVIDER
divider_text('Section F', 'Schechter: The Court Strikes the Recovery Act',
             'May 27, 1935. The administration called it Black Monday.',
             "Set the case before the holdings. A Brooklyn poultry company had been prosecuted under the live poultry code, one of the codes of fair competition written under the National Industrial Recovery Act, the law at the center of the early New Deal's industrial plan. The company slaughtered chickens that had been shipped into New York from other states and sold them to local buyers. On May 27, 1935, the Supreme Court decided its case, and the decision in Schechter v. United States was unanimous: all nine justices, including the Court's liberals, held the act unconstitutional. The administration called the day Black Monday because the Court ruled against the government in two other cases the same day. In the guided notes definition, Schechter v. United States is the 1935 Supreme Court decision that struck down the National Industrial Recovery Act, holding that Congress had given away its lawmaking power and reached business beyond its authority. The next two slides take the holdings one at a time.")

# ------------------------------------------------------ 17 DELEGATION
content_text('Congress may not give its power away',
             ['The syllabus said an economic crisis cannot create or enlarge constitutional power.',
              'It said Congress may not abdicate its essential legislative functions.',
              'The president had approved codes for whole industries.',
              'Congress had set no standards of its own.',
              'The code system of the NRA fell with the act.'],
             "Read the syllabus lines aloud, because they are the primary text of this section and the activity returns to them. Extraordinary conditions, such as an economic crisis, may call for extraordinary remedies, but they cannot create or enlarge constitutional power. Congress is not permitted by the Constitution to abdicate, or to transfer to others, the essential legislative functions with which it is vested. Unpack the second sentence slowly. The Constitution vests lawmaking in Congress. Congress may let others apply its policies, but it must lay down the policies and standards itself. Under the Recovery Act, trade associations proposed codes and the president approved them, with no standard in the statute beyond fairness itself. The Court called that a transfer of the lawmaking power, and a transfer the Constitution forbids. The consequence was immediate and total: the code system, the operating machinery of the National Recovery Administration, lost its legal basis in a single decision.",
             kick='F · Schechter', size=24)

# ------------------------------------------------------ 18 STAT: 9 TO 0
stat('9 to 0', 'the Schechter decision was unanimous',
     'The second holding: local selling and slaughtering lay beyond the commerce power of Congress',
     "Use the unanimity to make the commerce holding land. Nine justices who agreed about little else agreed that the federal government had reached too far, twice over. The second holding concerned commerce. The company's chickens had crossed state lines to reach New York, but the code punished how they were sold and slaughtered inside the state, which the Court held lay beyond the commerce power of Congress and within the authority reserved to the states. Put the two holdings side by side for students. Delegation limited how Congress could share its power. Commerce limited where federal power could reach at all. A government that had built its recovery on codes written in Washington and applied in every town had lost on both grounds in one morning. After Schechter, the administration also had to assume that the farm program, built on a tax and production controls, stood in the same danger. It did, and the next section is that story.",
     kick='F · Schechter')

# ------------------------------------------------- 19 SECTION G DIVIDER
divider_text('Section G', 'Butler and the Lesson of the Two Fronts',
             'The farm program fell in January 1936.',
             "The Agricultural Adjustment Act paid farmers to produce less, funded by a tax on the companies that processed farm goods. The theory joined two powers: Congress could tax, and Congress could spend for the general welfare. In United States v. Butler, decided in January 1936, the Court struck the processing tax down, holding that Congress could not use its taxing power to regulate farm production, a field the decision left to the states. In the guided notes definition, United States v. Butler is the 1936 Supreme Court decision that struck down the Agricultural Adjustment Act's processing tax as an unconstitutional use of federal power over farm production. After the two decisions, the Court would plainly set the boundaries of the New Deal. This final section draws the lesson's balance: what the two fronts together forced, and what they produced in the legislative season of 1935.")

# ------------------------------------------------------ 20 THE FARM PROGRAM FALLS
content_text('The farm program falls',
             ['The AAA paid farmers to produce less.',
              'The payments were funded by a tax on farm processors.',
              'In Butler, in January 1936, the Court struck the tax down.',
              'The Court said Congress could not use the taxing power to regulate production.',
              'The Court left farm production as a field for the states.'],
             "Walk the Butler holding once, slowly, because it completes the legal half of the lesson. The processing tax was not attacked as a tax. Taxes on processors were common and lawful. It was attacked as a regulation wearing a tax's clothing: the money was raised for one stated purpose, to pay farmers to cut production, and production was a field the Court held belonged to the states. A power to tax that can be aimed at any activity would let Congress regulate anything by pricing it, and the Court refused to read the taxing power that widely. Then widen the lens to the whole two-front picture students now hold. By the start of 1936 the administration had been told by mass movements that its program was too small, and by the Court that central parts of it were unlawful. Both messages were true on their own terms. The response, the Second New Deal, is the next lesson; this lesson closes by judging the pressure itself.",
             kick='G · Butler and the two fronts', size=24)

# ------------------------------------------------------ 21 TWO FRONTS, ONE ANSWER
content_text('Two fronts, one answer',
             ['The movements demanded more, including security in old age and a curb on fortunes.',
              'The Court demanded less, requiring laws inside the Constitution as it read it.',
              'The 1935 answer moved toward the protections the movements demanded.',
              'It was written as statutes of Congress, in forms meant to survive the Court.'],
             "Close the content where the reading closes, with the two fronts acting on one legislative season. The movements demanded more than the New Deal had given, above all security in old age and a curb on great fortunes, and their clubs, petitions, and audiences made inaction dangerous in the run up to the 1936 election. The Court demanded less, and its demands were not requests: Schechter and Butler removed laws from the books. The Second New Deal of 1935 answered both pressures at once. It moved toward the protections the critics demanded, old-age insurance above all, which was Townsend's subject taken up at a sustainable size. And it was written as statutes of Congress resting on the taxing power used directly rather than as a lever, in forms its authors hoped the Court could not strike down. Whether the answer worked, and who it protected, is the subject of the next lesson.",
             kick='G · Butler and the two fronts', size=24)

# ------------------------------------------------------ 22 PRESSURE AT A GLANCE
s = slide(NAVY)
kicker(s, 'The pressure at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Five critics, two directions', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Long', 'Too little: fortunes untouched', 'Cap fortunes; $5,000 floor; $30 pension'),
        ('Townsend', 'Too little: no security in old age', '$200 a month, spent within the month'),
        ('Coughlin', 'Too little: the money system protected', 'Monetary change, public control, as summarized'),
        ('Liberty League', 'Too much: property and the Constitution', 'Federal power held narrow'),
        ('Supreme Court', 'Too much: beyond the Constitution', 'Schechter and Butler void the laws')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=20, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 0.88
notes(s, "This slide mirrors the final table in the guided notes, The Pressure at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. Read it as the lesson's argument in five rows. The first three rows charge the New Deal with doing too little, and each pairs the charge with a cure: Long with a fortune cap funding a $5,000 family floor and a thirty dollar pension, Townsend with two hundred dollars a month spent within the month, Coughlin with monetary change and public control of key industries as the summaries of his broadcasts describe it. The last two rows charge it with doing too much: the Liberty League in print, demanding federal power held narrow, and the Supreme Court in law, voiding the recovery act and the farm tax. Grade the table generously on wording and strictly on direction: a student who places a critic on the wrong front has missed the lesson, whatever the details say.")

# ------------------------------------------------------ 23 VOCAB A
vocab('Words for the movements',
      [('Share Our Wealth', "Huey Long's program and movement, begun in 1934, which promised to cap large fortunes and guarantee every family a homestead and a minimum income"),
       ('Townsend Plan', "Dr. Francis Townsend's proposal that the federal government pay two hundred dollars a month to every citizen over sixty, on condition the money be spent within the month"),
       ('old-age pension', 'a regular payment made by a government to people who have reached a set age and left regular work'),
       ('demagogue', 'a leader who gains power by arousing popular fears, prejudices, and hopes with simple promises, rather than by answering arguments')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. Share Our Wealth: Huey Long's program and movement, begun in 1934, which promised to cap large fortunes and guarantee every family a homestead and a minimum income. The Townsend Plan: Dr. Francis Townsend's proposal that the federal government pay two hundred dollars a month to every citizen over sixty, on condition the money be spent within the month. The spending condition is the definition's heart, so underline it. Old-age pension: a regular payment made by a government to people who have reached a set age and left regular work. Demagogue: a leader who gains power by arousing popular fears, prejudices, and hopes with simple promises, rather than by answering arguments. Remind students the word names a method, not a side: it can be tested against any leader in the lesson, including the ones they agree with.")

# ------------------------------------------------------ 24 VOCAB B
vocab('Words for the opposition and the Court',
      [('American Liberty League', 'the organization founded in 1934 by wealthy businessmen and conservative Democrats to oppose the New Deal as a threat to property and the Constitution'),
       ('Schechter v. United States', 'the 1935 Supreme Court decision that struck down the National Industrial Recovery Act, holding that Congress had given away its lawmaking power and reached business beyond its authority'),
       ('United States v. Butler', "the 1936 Supreme Court decision that struck down the Agricultural Adjustment Act's processing tax as an unconstitutional use of federal power over farm production")],
      "Three more terms, again matching the guided notes exactly. American Liberty League: the organization founded in 1934 by wealthy businessmen and conservative Democrats to oppose the New Deal as a threat to property and the Constitution. Note the party in the definition: conservative Democrats, opponents inside the president's own coalition. Schechter v. United States: the 1935 Supreme Court decision that struck down the National Industrial Recovery Act, holding that Congress had given away its lawmaking power and reached business beyond its authority. The definition carries both holdings, delegation and commerce, in one sentence. United States v. Butler: the 1936 Supreme Court decision that struck down the Agricultural Adjustment Act's processing tax as an unconstitutional use of federal power over farm production. Pair the two cases when you review: industry in 1935, agriculture in 1936, and the early New Deal's two largest programs gone between them.")

# ------------------------------------------------------ 25 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Why did the New Deal draw attack from every direction by 1935, and what did the attacks reveal about the country? Keep the two directions separate in your answer.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Pressure Map: the address, the plan, the broadcasts, the League, the syllabus'),
        ('Notebook', 'Notebook page: the five critics in one chart'),
        ('Quick check', 'The Filibuster and the Syllabus: Long, Townsend, and the Schechter holdings'),
        ('Writing', 'Attack From Every Direction: the lesson question as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the two charges in one sentence, why the Court could do what the League could not, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Pressure Map, runs five stations through the critics: Long's Share Our Wealth address in his own words, the Townsend Plan as a labeled summary of its stated terms, Coughlin's broadcasts as a labeled summary account, the Liberty League's positions as a labeled summary, and the Schechter syllabus quoted from the United States Reports, ending in a completed pressure map and a judgment about which pressure Roosevelt had most reason to answer. The quick check, The Filibuster and the Syllabus, tests the two pension plans against each other and the two Schechter holdings. The writing task, Attack From Every Direction, turns the lesson question into an essay scored on keeping the two directions separate. The exit ticket has three parts: the two charges in one sentence; why the Court could do what the League could not, answered with the two cases; and the lesson question in two or three sentences with at least two facts. Next lesson takes up the answer the pressure produced: the Second New Deal of 1935.")

dc.save(OUT)
