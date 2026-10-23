#!/usr/bin/env python3
"""Depression and New Deal Lesson 6 deck, "The Second New Deal," built to the
approved Twenties system: image-led slides, fragments only on screen,
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


def cphoto(img, title, items, note, kick=None, size=24):
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
text(s, 0.9, 5.32, 11.5, 0.4, 'THE DEPRESSION AND NEW DEAL · LESSON 6', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Second New Deal', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'The settlement of 1935', size=17, color=POWDER)
notes(s, "The photograph shows a Works Progress Administration camp on the Mount Hood National Forest in 1936, housing the crews who built Timberline Lodge, and it belongs to the world this lesson creates. Last lesson ended with pressure from two fronts: movements demanding more than the first New Deal had given, and a Supreme Court striking down its laws. This lesson is the answer. In the legislative season of 1935, Roosevelt and Congress passed a second wave of statutes built to last: a work program that employed millions, an insurance system that still runs today, a labor law with an enforcement board, and a tax aimed at the largest fortunes. Open by naming the lesson's central contrast. The laws of 1933 were emergency measures, written in weeks to stop a collapse. The laws of 1935 were written as a settlement, permanent duties the federal government would carry in ordinary times as well as in crisis. Everything in the lesson hangs on that difference.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did the Second New Deal of 1935 move beyond the first, and who was it built to protect?', {})]],
     size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the New Deal change the relationship between Americans and their federal government, and what did it leave undone?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question has two halves again, and the second half governs the first. How did 1935 move beyond 1933, and who was it built to protect? Students will be tempted to answer the first half with a list of new agencies. Hold them to the change in kind: from emergency measures to permanent duties, from relief given by discretion to benefits owed as entitlements, from declared rights to rights with an enforcement board. The second half has a trap in it, and the lesson is built to spring it honestly. The settlement protected industrial workers, the retired, and the organized as no American law had done. It also wrote a boundary into its central statute, excluding agricultural and domestic workers, and that exclusion fell hardest on Black workers and on women. An answer that names only the protection has answered half the question. The writing task is scored on exactly that completeness.")

# --------------------------------------------------- 3 THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'From emergency measures to a settlement', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', '1935: a second season of laws', 'Permanent duties, not emergency measures'),
        ('B', 'The WPA at work', 'About 8.5 million employed across its life'),
        ('C', 'Federal One', 'Plays, guidebooks, and life histories'),
        ('D', 'The Social Security Act', 'Insurance for old age and job loss'),
        ('E', 'Who was left out', 'Agricultural and domestic workers'),
        ('F', 'The Wagner Act and the labor board', 'Organizing rights with enforcement'),
        ('G', 'The wealth tax and the settlement', 'Seventy-five percent at the top')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A states the season's purpose. Section B takes the Works Progress Administration, the largest program in daily life, and section C its arts projects, Federal One. Section D gives the season's most durable law, the Social Security Act, and section E stops at its boundary: the agricultural and domestic workers left outside the definition of employment. Section F turns to labor, the Wagner Act and the board it created. Section G closes with the Revenue Act of 1935 and with the settlement as a whole. Tell students the final table in their guided notes, The Settlement at a Glance, asks them to rebuild this map with one addition the screen does not make for them: who each measure covered, and who it left out.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', '1935: A Second Season of Laws',
             'Driven by the critics, and by recovery that had not arrived.',
             "Set up why a second season happened at all, because the fact is easy to slide past. Presidents do not usually get two legislative seasons of this size. Roosevelt got one because the first had not finished its work and was being dismantled while he watched. Recovery had not arrived: the movements of Long and Townsend were demanding security the first New Deal had not provided, and the Supreme Court was striking down its laws, as Schechter had struck the recovery act weeks before the season opened. The laws that followed were therefore written under two kinds of instruction at once. Politically, they had to answer the demand for security in old age and a curb on great fortunes. Legally, they had to be built in forms the Court could not easily strike down, as statutes of Congress resting directly on the taxing power and the commerce power. Keep both instructions visible through the whole lesson.")

# ------------------------------------------------------ 5 SETTLEMENT
content_text('Emergency measures become a settlement',
             ['1933: written in weeks to stop a collapse',
              '1935: permanent duties, carried in ordinary times too',
              'A work program, an insurance system, a labor law',
              'And a tax measure announcing who would pay'],
             "Define the lesson's key word before the programs arrive, because everything after it is an instance. A settlement, as the reading uses the word, is an arrangement meant to stand: permanent duties the federal government would carry in ordinary times as well as in crisis. The contrast is with 1933. The Hundred Days laws were emergency measures, written in weeks to stop a collapse, and several were designed to expire or were struck down within two years. The 1935 laws assume the federal government will still be doing this work in ten years and in fifty. Three of them redrew what Americans could expect from their government: a work program, an insurance system, and a labor law. A fourth, a tax measure, announced who would be asked to pay for the new order. Students should be able to state this contrast in one sentence by the exit ticket, and the guided notes ask for it directly.",
             kick='A · 1935: a second season of laws', size=24)

# ------------------------------------------------- 6 SECTION B DIVIDER
divider_photo('wpa-port.jpg', 'Section B', 'The WPA at Work',
              ['A job, a wage,', 'and something built at the end of it.'],
              "The photograph shows a street in Opelousas, Louisiana, photographed in November 1936 shortly after WPA workers paved it, from a Works Progress Administration photograph held by the Louisiana Digital Library. Choose it deliberately as the section's image: the WPA is usually pictured as men with shovels, but its own record is the finished thing, the street, the school, the airport, still in use. Introduce the agency with its full name and its chief. The Works Progress Administration was created in May 1935 and placed under Harry Hopkins, who had run the relief programs of the first New Deal and believed, as the next slides will show, that work relieved more than unemployment. Projects were proposed by states and towns and paid for by Washington, a design that put federal money behind local lists of needed work. The scale comes on the stat slide; this section's business is what the WPA was and how Hopkins defended it.",
              title_size=40)

# ------------------------------------------------------ 7 THE WPA
cphoto('wpa-port.jpg', 'Work relief, not a dole',
              ['Created May 1935, under Harry Hopkins',
               'Projects proposed by states and towns, paid for by Washington',
               'Roads, schools, courthouses, and airports',
               'Work chosen to start quickly and hire many hands',
               'Hopkins: a job, a wage, and something built'],
              "State the agency through its definition first, in the guided notes words: the Works Progress Administration is the agency created in 1935, led by Harry Hopkins, that employed about eight and a half million people over its life building roads, schools, and airports and funding arts and writing projects. Two design choices deserve attention. Projects were proposed by states and towns, which supplied materials and some costs, while Washington paid most wages; the hiring therefore followed local lists of needed work rather than a plan drawn in the capital. And the WPA wage was set below private wages for the same work, on purpose, so the program would relieve unemployment without drawing workers out of private jobs. Hopkins defended the program as work relief rather than a dole: a job, a wage, and something built at the end of it. Critics answered that some projects were make-work, and Congress argued over the cost every year of its life.",
              kick='B · The WPA at work', size=24)

# ------------------------------------------------------ 8 STAT: 8.5 MILLION
stat('8.5 million', 'people employed by the WPA across its life',
     'About three million on the payroll at its height · The agency ran from 1935 to 1943',
     "Put the two numbers together and let students feel the scale. Across its life, from 1935 to its closing in 1943, the WPA employed about eight and a half million people. At its height, in the fall of 1938, about three million people were on its payroll at once, which made the federal government, through this one agency, the employer of a workforce larger than most industries. Those workers were not an abstraction to the towns they lived in. They were the crew repaving the street in the section photograph, the men raising the school gym, the clerks in the project office. The WPA also explains why the settlement language needs care. The WPA itself was not permanent: Congress closed it in 1943, when war production had ended mass unemployment. Its place in the settlement is as the settlement's largest act of work relief, the daily-life proof that the federal government had accepted the jobless as its direct charge. The permanence of 1935 rests on the laws that follow, in sections D and F.",
     kick='B · The WPA at work')

# ------------------------------------------------- 9 SECTION C DIVIDER
divider_text('Section C', 'Federal One: Work for Artists and Writers',
             'The WPA hired for culture as well as construction.',
             "This short section covers the part of the WPA students least expect, and it should not be skipped, because it shows how far the settlement's idea of work could stretch. One part of the WPA hired not for construction but for culture. Its arts projects, grouped under the name Federal One, employed actors, musicians, artists, and writers who were out of work like everyone else on the rolls. The premise was the same as the road crews' premise: these were workers, their skill was their trade, and the government would pay them to practice it for the public. The Federal Theatre Project staged plays in cities across the country, many of them free. The Federal Writers' Project produced the guidebooks to the states that travelers still consult. The next slide gives the writers' second product, the life histories, which turned out to be the most durable thing Federal One made.")

# ------------------------------------------------------ 10 LIFE HISTORIES
content_text('Plays, guidebooks, life histories',
             ['Federal Theatre: plays across the country, many free',
              'Federal Writers: guidebooks to the states',
              'Life histories collected from ordinary Americans',
              'Congress ended the theatre project in 1939'],
             "Give the life histories their weight, because they are the part of Federal One that historians now use daily. The Federal Writers' Project collected life histories from ordinary Americans: mill workers, farmers, former slaves' children, and more than two thousand interviews with formerly enslaved people themselves, recorded in the late 1930s while living memory of slavery remained. No private publisher would have paid for that archive in a depression. It exists because a relief agency treated interviewing and writing as work worth a wage. Then mark the politics honestly. The arts projects were the smallest part of the WPA and drew the sharpest attacks in Congress, which ended the theatre project in 1939 amid charges about the politics of its plays. The section's closing judgment is the reading's: a jobless actor now counted as out of work in the same sense as a jobless carpenter, and the country's culture had become a public charge. That sentence widens the settlement's definition of the public itself.",
             kick='C · Federal One', size=24)

# ------------------------------------------------------ 11 STAT: 2,000
stat('2,000+', 'interviews with formerly enslaved people',
     'Recorded by the Federal Writers\' Project in the late 1930s, while living memory of slavery remained',
     "Pause on this number, because it is the rare statistic in the unit whose importance grows rather than shrinks with time. More than two thousand interviews with formerly enslaved people were recorded by the Federal Writers' Project. The men and women interviewed were in their eighties and nineties; within a few years most of that testimony would have been lost permanently. Historians of slavery now build on this archive constantly, and students will meet these narratives again in other courses. Connect the number back to the settlement argument. The interviews were not a charity and not a university project. They were relief work: writers on the WPA rolls, paid a federal wage to do the work they were trained for. When students judge Federal One, they should hold both facts together, the small size and sharp controversy of the arts projects in their own decade, and the permanence of the record those projects left behind. Permanence is this lesson's standard, and by that standard the smallest WPA project scores high.",
     kick='C · Federal One')

# ------------------------------------------------- 12 SECTION D DIVIDER
divider_photo('signing-port.jpg', 'Section D', 'The Social Security Act',
              ['Signed August 14, 1935.', 'The season\'s most durable law.'],
              "The photograph shows President Roosevelt signing the Social Security Act on August 14, 1935, with Secretary of Labor Frances Perkins standing behind him in the dark dress at the right of the frame. Perkins had chaired the committee that designed the act, and her presence in the photograph is the correct credit: this law has her authorship as much as the president's signature. Introduce the act through its definition, from the guided notes: the Social Security Act is the law of August 1935 that created old-age insurance, unemployment insurance with the states, and aid to dependent children and other vulnerable groups. Three protections in one statute, and the lesson takes them in order: old-age insurance at the center, unemployment insurance run with the states, and federal aid to dependent children and others the insurance did not reach. The next slide reads the center in the act's own words.",
              title_size=40)

# ------------------------------------------------------ 13 ENTITLED BY LAW
cphoto('signing-port.jpg', 'Entitled by law',
              ['Old-age insurance at the center',
               '"Shall be entitled to receive" an old-age benefit',
               'Payable in equal monthly installments, from age sixty-five',
               'Funded by a payroll tax, paid by workers, matched by employers',
               'Monthly benefits under the original text: from 1942'],
              "Read the statute's own words, because the activity and the quick check both return to them. Every qualified individual shall be entitled to receive, with respect to the period beginning on the date he attains the age of sixty-five, or on January 1, 1942, whichever is the later, an old-age benefit, payable as nearly as practicable in equal monthly installments. The verb carries the settlement. Entitled means the benefit is owed: a qualified retired worker claims it as a right, not as charity and not at an agency's discretion. In the guided notes, old-age insurance is the part of Social Security that pays a monthly benefit to retired workers, funded by payroll taxes on workers and their employers, and a payroll tax is a tax taken from workers' wages and matched by employers, used to fund Social Security. Note the dates without apology: the tax began in 1937, monthly benefits in 1942, because the fund was built from the contributions first.",
              kick='D · The Social Security Act', size=24)

# ------------------------------------------------------ 14 THREE PROTECTIONS
content_text('Three protections, one idea',
             ['Old-age insurance: a monthly benefit as a matter of right',
              'Unemployment insurance: run jointly with the states',
              'Aid: federal grants for dependent children, the blind, the old without insurance',
              'One idea: these risks no longer fall on a family alone'],
             "Lay out the whole act before the section on its boundary, so the boundary lands on a complete picture. Old-age insurance paid a monthly benefit to retired workers as a matter of right. Unemployment insurance, in the guided notes definition, is the joint federal and state system, created in 1935, that pays temporary benefits to workers who lose their jobs: Washington set the framework and the tax, the states ran the systems and set the payments. Federal grants helped the states pay aid to dependent children, to the blind, and to the old who had no insurance. The three parts shared one idea, and students should be able to say it: the risks of old age, job loss, and a father's death were no longer to fall on a family alone. What had been private misfortune, answered by family savings and local charity, became a standing charge on the whole working population, collected through the payroll. That is the relationship between Americans and their federal government changing in a single statute.",
             kick='D · The Social Security Act', size=24)

# ------------------------------------------------- 15 SECTION E DIVIDER
divider_text('Section E', 'Who Was Left Out',
             'The boundary was written into the definition of employment.',
             "Slow the lesson down here, because this section is the second half of the lesson question and students will underweight it if it passes quickly. The Social Security Act's protections attached to employment: covered work created the wage record, paid the tax, and earned the benefit. The act's definition of employment therefore decided, in advance, whose old age would be insured. That definition left out two fields of work, agricultural labor and domestic service in a private home. The exclusion was defended at the time as a matter of administration: reporting and taxing farm and household wages, paid in cash, in kind, and at irregular intervals. Teach the reason and the effect together, as the activity insists. The reason explains how the line was defended. The effect is who stood on the far side of it, and the next slide names them.")

# ------------------------------------------------------ 16 OUTSIDE THE DEFINITION
content_text('Outside the definition',
             ['Excluded: agricultural labor',
              'Excluded: domestic service in a private home',
              'Those fields held a large share of all Black workers',
              'And a large share of working women',
              'Brought inside only by later amendments, in the 1950s'],
             "Name the people plainly. The two excluded fields held a large share of all Black workers in the United States, above all in the South, where most Black Americans still lived and worked the land, and a large share of working women, since domestic service was among the largest employers of women in the country. A sharecropper and a cook therefore stood outside the new insurance at its founding, not because the act named them, but because it defined their work away. The workers most exposed to poverty were the ones the settlement reached last. Later amendments widened the system, bringing most farm and domestic workers inside during the 1950s, which is worth stating so students do not freeze the system at its founding shape. But in 1935 the boundary was part of the settlement itself, drawn where southern committee power in Congress was strongest. Any account of who the Second New Deal was built to protect has to name the people it left outside.",
             kick='E · Who was left out', size=24)

# ------------------------------------------------- 17 SECTION F DIVIDER
divider_text('Section F', 'The Wagner Act and the Labor Board',
             'A right to organize, with an agency behind it.',
             "The third of the season's great laws concerns not benefits but power inside the workplace. The National Labor Relations Act, in the guided notes definition, is the 1935 law, called the Wagner Act, that guaranteed workers the right to organize unions and bargain collectively and created a board to enforce those rights. It was signed on July 5, 1935, a month before the Social Security Act, and it took its common name from its sponsor, Senator Robert Wagner of New York. Frame the problem it answered. American law had declared workers' right to organize before, most recently in the fallen recovery act, and employers had mostly ignored the declarations, firing organizers and refusing to meet unions at all. A declaration without enforcement had been tested and had failed. The Wagner Act's contribution was machinery: a list of forbidden employer practices, a federal board, and a procedure. The next slide walks the machinery.")

# ------------------------------------------------------ 18 A RIGHT WITH AN AGENCY
content_text('A right with an agency behind it',
             ['Guaranteed: organize unions of their own choosing',
              'Guaranteed: bargain collectively with the employer',
              'Forbidden: firing a worker for union activity',
              'The National Labor Relations Board: elections and charges',
              'Remedies: reinstatement with back pay'],
             "Define the central phrase first, from the guided notes: collective bargaining is negotiation between an employer and a union chosen by the workers over wages, hours, and working conditions. Chosen by the workers is the load-bearing phrase; the act let the workers, not the employer, decide who spoke for them. The board made the choice real. It checked a union's showing of support, ran a secret ballot election, and certified the winner, whom the employer then had to meet and bargain with. It also heard charges. Firing a worker for union activity was an unfair labor practice forbidden by law, and the board could order the worker reinstated with back pay. Compare that to the position of a fired organizer in 1932, whose remedies were the strike and the street. The Wagner Act moved the contest from the street into a federal procedure, which is why the organizing drives of the next lesson start from this law.",
             kick='F · The Wagner Act and the labor board', size=24)

# ------------------------------------------------------ 19 ELECTIONS AND PRACTICES
content_text('Elections and unfair practices',
             ['A majority on cards could claim an election',
              'A secret ballot decided who spoke for the workers',
              'Refusing to bargain: itself an unfair labor practice',
              'Workers used the act at once'],
             "Fill in the procedure once more in working order, because the activity's board case tests it step by step. Organizers sign up workers; a sufficient showing lets the union ask the board for an election; the board runs a secret ballot; the winner is certified as the workers' bargaining agent; the employer must then bargain with that agent over wages, hours, and working conditions, and refusing to bargain is itself an unfair labor practice. Each step replaces force with a count. Before the act, recognition was won by strikes and held by strength. After it, recognition could be won by a vote supervised by the federal government. That substitution is the deepest sense in which the Wagner Act belongs to a settlement rather than to an emergency program: it did not relieve a crisis, it built a standing way of deciding who speaks for workers, meant to operate in ordinary times. Workers used it at once, and union membership began the climb the next lesson traces.",
             kick='F · The Wagner Act and the labor board', size=24)

# ------------------------------------------------- 20 SECTION G DIVIDER
divider_text('Section G', 'The Wealth Tax and the Settlement',
             'Who would pay, and what the season added up to.',
             "The season's fourth measure was its smallest in money and its loudest in politics. The Revenue Act of 1935, which newspapers called the wealth tax, raised income tax rates at the very top and raised taxes on large estates and corporations. It arrived in the same summer as Long's movement reached its height, and its supporters presented it as an answer to the charge that the New Deal had left great fortunes untouched. Treat it as the reading does: it paid for only part of the new programs, and its larger purpose was political. A settlement, though, needs a revenue side as well as a program side, and the wealth tax is where students should practice judging a law by its thresholds and yield rather than by its headline rate. The stat slide gives them the figures to do it with.")

# ------------------------------------------------------ 21 STAT: 75 PERCENT
stat('75 percent', 'the top income tax rate under the Revenue Act of 1935',
     'The rate applied only to income above $5,000,000, reached by a handful of taxpayers',
     "Make students read the threshold with the rate, because the act is misjudged whenever the two are separated. Seventy-five percent was the top rate of the individual income tax, and it applied only to income above five million dollars, a level reached in those years by a handful of taxpayers. The estate tax reached seventy percent above fifty million dollars. As revenue, the act was modest: it raised far less than the new programs cost, and its schedules touched ordinary prosperity not at all. As politics, it was the administration's public answer to Share Our Wealth, a demonstration that the president, and not only his critics, would tax great fortunes. Neither reading cancels the other. The strongest student answers hold both: a real rise in the tax burden at the very top of the income scale, designed at least as much to answer a movement as to fund a government. That double character is typical of the whole 1935 season.",
     kick='G · The wealth tax and the settlement')

# ------------------------------------------------------ 22 THE SETTLEMENT IN ONE VIEW
content_text('The settlement in one view',
             ['Before 1935: old age, job loss, organizing were private troubles',
              'After 1935: permanent federal responsibility for each',
              'Funded by taxes written into law',
              'Administered by standing agencies',
              'With the exclusion written beside the acceptance'],
             "Close the content where the reading closes, with the standing question of American government changed. Before 1935, a worker's old age, a lost job, and a fight to organize were treated as private troubles, answered by family, charity, and the strike. After 1935, the federal government had accepted permanent responsibility for each: a payroll tax funding an entitlement to old-age benefits, an insurance system for the jobless run with the states, a board enforcing the right to bargain, and a work program that employed millions directly in the meantime. Funded by taxes written into law and administered by standing agencies, the settlement was built to operate in ordinary times. End with the sentence the lesson has earned twice over. That acceptance, with the exclusion written beside it, is the settlement the rest of the unit will judge. Students who can defend both halves of that sentence have the lesson.",
             kick='G · The wealth tax and the settlement', size=24)

# ------------------------------------------------------ 23 SETTLEMENT AT A GLANCE
s = slide(NAVY)
kicker(s, 'The settlement at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Four measures of 1935', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('WPA', 'Direct federal employment of the jobless', 'About 8.5 million over its life; ended 1943'),
        ('Social Security', 'Insurance for old age and job loss', 'Farm and domestic workers outside at first'),
        ('Wagner Act', 'Organizing rights with a federal board', 'Depended on board and court enforcement'),
        ('Revenue Act', 'Financing from the top of the income scale', '75 percent above $5,000,000; modest yield')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=20, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, The Settlement at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. Read the rows as the season's balance sheet. The WPA accepted direct federal employment of the jobless and covered about eight and a half million people, but it was a program with an end, closed in 1943. Social Security accepted standing insurance for old age and job loss, and its limit stands in the third column: agricultural and domestic workers outside the founding definition. The Wagner Act accepted federal protection of organizing and bargaining, dependent for its force on the board and the courts. The Revenue Act accepted financing from the top of the income scale, at seventy-five percent above five million dollars, with a modest yield. Grade the table generously on wording and strictly on the covered and excluded columns: each entry must say who the measure reached and where its boundary ran.")

# ------------------------------------------------------ 24 VOCAB A
vocab('Words for the insurance state',
      [('Works Progress Administration', 'the agency created in 1935, led by Harry Hopkins, that employed about eight and a half million people over its life building roads, schools, and airports and funding arts and writing projects'),
       ('Social Security Act', 'the law of August 1935 that created old-age insurance, unemployment insurance with the states, and aid to dependent children and other vulnerable groups'),
       ('old-age insurance', 'the part of Social Security that pays a monthly benefit to retired workers, funded by payroll taxes on workers and their employers'),
       ('unemployment insurance', 'the joint federal and state system, created in 1935, that pays temporary benefits to workers who lose their jobs')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. Works Progress Administration: the agency created in 1935, led by Harry Hopkins, that employed about eight and a half million people over its life building roads, schools, and airports and funding arts and writing projects. Social Security Act: the law of August 1935 that created old-age insurance, unemployment insurance with the states, and aid to dependent children and other vulnerable groups. Old-age insurance: the part of Social Security that pays a monthly benefit to retired workers, funded by payroll taxes on workers and their employers. Unemployment insurance: the joint federal and state system, created in 1935, that pays temporary benefits to workers who lose their jobs. Stress the pair of phrases students confuse: old-age insurance is contributory and paid as a right, while the aid programs in the same act were grants to the states for people the insurance did not reach.")

# ------------------------------------------------------ 25 VOCAB B
vocab('Words for taxes and labor',
      [('payroll tax', "a tax taken from workers' wages and matched by employers, used to fund Social Security"),
       ('National Labor Relations Act', 'the 1935 law, called the Wagner Act, that guaranteed workers the right to organize unions and bargain collectively and created a board to enforce those rights'),
       ('collective bargaining', 'negotiation between an employer and a union chosen by the workers over wages, hours, and working conditions')],
      "Three more terms, again matching the guided notes exactly. Payroll tax: a tax taken from workers' wages and matched by employers, used to fund Social Security. The matching is the point to underline: the employer's half made the benefit a contribution from both sides of the wage bargain, which is why Roosevelt treated the tax as the benefit's political protection. National Labor Relations Act: the 1935 law, called the Wagner Act, that guaranteed workers the right to organize unions and bargain collectively and created a board to enforce those rights. Collective bargaining: negotiation between an employer and a union chosen by the workers over wages, hours, and working conditions. Students should be able to name the three subjects in the definition without prompting: wages, hours, and working conditions. These seven terms, with the five from the first vocabulary slide, are the whole vocabulary of the settlement.")

# ------------------------------------------------------ 26 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did the Second New Deal of 1935 move beyond the first, and who was it built to protect? Name the boundary in your answer.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Settlement Chart: the WPA record, the act, the boundary, a board case, the wealth tax'),
        ('Notebook', 'Notebook page: the four measures of 1935 in one chart'),
        ('Quick check', 'The Signing and the Statute: the entitlement, the dates, the exclusion, the board'),
        ('Writing', 'The Settlement of 1935: the lesson question as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: emergency measure against settlement in one sentence, the founding exclusion and who it fell on, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Settlement Chart, runs five stations through the season: the WPA record as a labeled summary, the Social Security Act in its own words, the boundary inside its definition of employment, a typical case before the labor board labeled as a teaching summary, and the wealth tax rate schedules, ending in a completed settlement chart and a judgment about which element changed the federal role most. The quick check, The Signing and the Statute, tests the entitlement language, the exclusion applied to two workers, and the board's remedy for a fired organizer. The writing task, The Settlement of 1935, turns the lesson question into an essay scored on both halves, the change in kind and the boundary. The exit ticket has three parts: emergency measure against settlement in one sentence; the founding exclusion and the two groups it fell on hardest; and the lesson question in two or three sentences with at least two facts. Next lesson puts the Wagner Act in workers' hands: the sit-down strikes, Flint, and the hard year of 1937.")

dc.save(OUT)
