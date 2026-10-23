#!/usr/bin/env python3
"""Lesson 3 deck, "The Workers' World," built to the approved Progressive Era
system: image-led slides, fragments only on screen, comprehensive speaker
notes, full lesson + vocabulary coverage. Fonts: Georgia titles, Lato body."""
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
OUT = os.path.join(HERE, '..', 'lesson-03-slides.pptx')

def vocab(title, terms, note, kick='The vocabulary', step=1.52):
    s = slide(CREAM)
    kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95, 11.5, 1.0, title, size=30, color=NAVY, font='Georgia')
    yy = 2.1
    for term, dfn in terms:
        text(s, 0.9, yy, 4.1, 0.9, term, size=25, color=NAVY, font='Georgia')
        text(s, 5.15, yy + 0.06, 7.3, 1.1, dfn, size=19, color=MUTED, leading=1.2)
        yy += step
    notes(s, note)
    return s

# ---------------------------------------------------------------- 1 · TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'GILDED AGE · LESSON 3', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, "The Workers' World", size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Long days, low wages, and the strikes that tested what workers could win together', size=17, color=POWDER)
notes(s, "Open on the spinning room at the Magnolia Cotton Mills in Mississippi, photographed by Lewis Hine in May 1911. Say the date plainly: this photograph comes a few years after the strikes at the heart of the lesson, and it shows the same world those strikes grew out of. Long rows of spinning frames run the length of the room, belts and wheels turn overhead, and workers stand scattered down the aisles, some of them plainly children. That room is the lesson in one image. Industrial work paid the wages that kept families alive, and it also set the terms: the hours, the pace, the danger, and the arithmetic that sent children to the frames. Today students follow the workers from that room to the unions they built, and then to the three defeats that tested what organizing could win.")

# ------------------------------------------------- 2 · LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, 'Why did workers organize, and why did collective action so often end in defeat?',
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did industrial growth transform American life, and who gained, who paid, and who resisted?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Put the lesson question at the center of the hour and keep it visible. It has two halves, and the lesson answers them in order. Why did workers organize? Sections A through D answer that: the factory day, a wage that could not feed a family, children put to work, and the two union strategies workers built in response. Why did collective action so often end in defeat? Section E answers that with three cases: Haymarket, Homestead, and Pullman. The unit question underneath frames the whole Gilded Age: how did industrial growth transform American life, and who gained, who paid, and who resisted? This lesson is the unit's clearest case of the last two groups. The workers paid, in hours, in health, and sometimes in their lives, and the workers also resisted, together. That is why their defeats, and not only their conditions, are the story today.")

# --------------------------------------------------- 3 · THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.3, 11.5, 1.0, 'A workforce organizes', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.42)
rows = [('A', 'The Factory Day', 'the clock, the machine pace, and the unguarded machine'),
        ('B', 'Wages and Child Labor', 'a few hundred dollars a year, and children at the frames'),
        ('C', 'Why Workers Combined', 'alone, replaceable; together, bargaining power'),
        ('D', 'Two Roads', "the Knights' broad reform and the AFL's narrow craft unions"),
        ('E', 'Three Defeats', 'Haymarket, Homestead, Pullman, and the pattern they share')]
yy = 2.82
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.7, n, size=26, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.03, 3.6, 0.7, t, size=21, color=CREAM, bold=True)
    text(s, 5.35, yy + 0.08, 7.1, 0.7, d, size=18, color=POWDER)
    yy += 0.9
notes(s, "This is the map of the lesson, and it follows the guided notes section by section. We start where the workers started, on the factory floor, with the clock, the machine pace, and the danger. Then the pay: wages so low that families sent children into the mills to close the gap. Then the response, because a worker alone had no power and workers together might. Section D compares the two great strategies of the period, the Knights of Labor reaching for broad reform and the American Federation of Labor narrowing its goals to wages, hours, and conditions. Section E puts both strategies, and the movement generally, to the test in three defeats between 1886 and 1894. Tell students the exit ticket draws on sections C, D, and E, so the reasons for organizing and the forces that defeated the strikes both need to land today.")

# ------------------------------------------------- 4 · SECTION A DIVIDER
divider_photo('mill-port.jpg', 'Section A', 'The Factory Day',
              ['Work set by the clock,', 'paced by the machine'],
              "The photograph is the interior of a cotton mill, taken by Lewis Hine for the National Child Labor Committee in 1908. Name the date honestly: it comes just after the years this lesson covers, and it shows the same machinery, the same belts and spinning frames, and the same machine-set pace the reading describes. Look at what fills the frame. There are almost no people in it, and that is the point. A spinning room was a system of machines arranged in rows, and the workers fitted themselves into the spaces the machines left. Before unions, before strikes, students need to feel the basic fact of this section: industrial work was not the worker's craft slowed down or sped up. It was a new kind of work entirely, run on the employer's clock, at the machine's pace, and the rest of the lesson grows out of that change.",
              title_size=54)

# ------------------------------------------------------ 5 · THE CLOCK
content_text('The clock set the day',
             ['Ten to twelve hours a day, six days a week',
              'A factory whistle set the start of the day',
              'Bells marked the breaks; foremen watched the pace',
              'The pace was set by machines, not by the worker',
              'Some steelworkers worked periodic 24-hour turns'],
             "Work the guided notes blanks in order. A normal industrial schedule was ten to twelve hours a day, six days a week, and the reading adds a fact students remember: some steelworkers worked periodic 24-hour turns, a full day and night at the furnace when the shift changed. The day was bounded by the employer's signals, a whistle to start and bells for breaks, not by daylight or by the task at hand. Inside those hours, the pace belonged to the machine. A spinner or a molder did not decide how fast to work; the frames and the line decided, and foremen enforced the pace the machines set. Contrast this with the farm and craft work most students' ancestors, and many of these workers themselves, had known, where the worker set the rhythm and the seasons set the hours. The clock discipline came first, historically and in this lesson, because it explains why the wage bargain felt so one-sided.",
             kick='A · The factory day', size=24)

# ------------------------------------------------------ 6 · DANGER
content_text('Danger was part of the job',
             ['Unguarded belts and gears, mine gas, molten metal',
              'Workers killed and maimed in large numbers each year',
              "No workers' compensation system",
              'Courts held that taking the job meant accepting its risks'],
             "The reading's second paragraph is short, and its legal point is the one students must carry out of section A. The hazards were physical and constant: unguarded belts and gears that caught sleeves and hair, gas in the mines, molten metal in the mills. Workers were killed and maimed in large numbers each year. What turned injury into catastrophe was the law around it. There was no workers' compensation system, no insurance fund that paid a hurt worker or a dead worker's family as a matter of course. Courts commonly held that a worker who accepted a dangerous job had accepted its risks, a doctrine lawyers called assumption of risk. Put the consequence plainly. An injured worker could lose the family's main wage, have no claim on the employer, and face the poorhouse. Danger was not an accident of the system. Under the rules of the time, its cost was assigned, in advance, to the worker.",
             kick='A · The factory day')

# ------------------------------------------------- 7 · SECTION B DIVIDER
divider_photo('hine-port.jpg', 'Section B', 'Wages and Child Labor',
              ['A wage that could not feed a family,', 'and the children who closed the gap'],
              "Students already know this photograph: it is the quick check image, Lewis Hine's little spinner in a Georgia cotton mill, photographed about 1909 for the National Child Labor Committee. Use the familiarity. In the quick check they read the photograph for scale, the small girl beside frames as tall as she is. Now give them the economics behind it. Hine captioned photographs of this kind with the observation that some girls were so small they had to climb onto the frame to reach the threads. She is barefoot, she wears an apron with pockets for her tools, and she stands in an aisle built for machinery, not for children. This section answers the question her presence raises: why was a child standing there at all? The answer is arithmetic, and it starts with what her parents earned.",
              title_size=44)

# ------------------------------------------------------ 8 · WAGES
content_text('A few hundred dollars a year',
             ['Average yearly earnings: on the order of a few hundred dollars',
              'Pay was low, and layoffs could cut it away without warning',
              'One adult wage often could not cover rent, food, and clothing',
              'Families closed the gap by sending more members to work'],
             "Slow down on the reading's careful wording, because the guided notes test it. Average yearly earnings for manufacturing workers were on the order of a few hundred dollars. That phrase, on the order of, tells students the figure is a scale, not a precise salary: a few hundred dollars for a full year of ten and twelve hour days. The wage was also unsteady. Layoffs could cut even that away without warning, in a period with no unemployment insurance. Set the wage against the family's bills. A single adult wage often could not cover rent, food, and clothing, the three necessities the reading names. Families closed the gap the only way open to them: more members went to work, wives taking in laundry or boarders, older children leaving school for the mill. Child labor, the subject of the next two slides, was not a separate scandal pasted onto the system. It was how the system's wage arithmetic balanced at the kitchen table.",
             kick='B · Wages and child labor')

# ------------------------------------------------------ 9 · STAT
stat('1.75 MILLION', 'children ages 10 to 15 in paid work, census of 1900',
     'Roughly one child in five. The count is the wage system made visible: pay adults less than a family needs to live, and children take up the difference.',
     "Dwell on this number, because it is the census, not a reformer's pamphlet. The census of 1900 counted about 1.75 million children ages 10 to 15 in paid work, roughly one child in five in that age group. Have students picture their own school scaled up: in a school of a thousand children in those grades, about two hundred would be at work instead, on any given day, in the year 1900. The reading is precise about where they worked. They tended spinning frames in the textile mills, sorted slate from coal in the mines, and worked in glass factories, canneries, and street trades, selling papers and running errands in the cities. Emphasize that the figure counts only ages 10 to 15 and only paid work, so it understates children's labor in the home and on family farms. It is a floor, not a ceiling, and it was the official count of the United States government.",
     kick='B · Wages and child labor')

# ------------------------------------------------------ 10 · CHILDREN AT WORK
content_photo('breaker-port.jpg', 'Children the system could use',
              ['Spinners tended the frames; breaker boys sorted slate from coal',
               'Cheap, able to reach into small spaces, slow to protest',
               'Most left school early'],
              "The photograph shows breaker boys at a coal breaker near South Pittston, Pennsylvania, photographed by Lewis Hine in 1911. Give the date plainly: it falls a decade after the census count on the previous slide, and the boys are doing the exact work the reading names, sitting astride the coal chutes and picking slate and rock out of the coal as it rushes beneath them, hour after hour. The reading gives the employer's reasons in one line, and the guided notes test two of them. Children were cheap. They could reach into small spaces around machinery that adult hands could not. And they rarely protested. Add the family's reason from the last slide: their wages were needed at home. The cost landed on the children themselves. Most left school early, which fixed them in the worst paid work for life, the point the quick check asks students to argue from Hine's spinner photograph.",
              kick='B · Wages and child labor')

# ------------------------------------------------- 11 · SECTION C DIVIDER
divider_text('Section C', 'Why Workers Combined',
             'Alone, a worker could be replaced. Together, workers had something an employer had to reckon with.',
             "Pause at the turn in the lesson. Sections A and B described conditions: the hours, the danger, the wage, the children. Conditions alone, however bad, do not produce a labor movement. Plenty of workers endured them without organizing, because organizing was risky and often illegal in effect if not in name. This section gives the logic that turned endurance into combination. It is an argument about power, and students should be able to state it in one sentence by the end of the slide after next: one worker has nothing to bargain with, because one worker can be replaced; workers acting together control the one thing the employer needs, the labor itself, and stopping it together is what gives their demands weight. Everything in sections D and E, both union strategies and all three defeats, is a test of that single idea against employers, courts, and troops.")

# ------------------------------------------------------ 12 · ALONE AND TOGETHER
content_text('Alone, replaceable; together, leverage',
             ['One worker asking alone could simply be replaced',
              'A union let workers negotiate as a group',
              'Collective bargaining: the group negotiates at once',
              'A strike stopped production, and that was the leverage'],
             "Teach the three vocabulary words here in use, because the definitions on the vocabulary slides will then land as summaries. A union is an organization of workers formed to bargain with employers as a group. Its whole premise is the first fragment: a single worker who asked for higher wages or a shorter day could simply be replaced, so alone, workers had no bargaining power. Together they might. Collective bargaining is negotiation between an employer and workers organized as a group, and it changes the employer's calculation, because refusing the group means losing the whole workforce at once. The strike is the enforcement behind the negotiation: a work stoppage meant to pressure an employer to meet workers' demands. If all the spinners stopped at once, production stopped with them. Hold students to the logic. The union did not ask the employer to be kind. It made refusal expensive, which is a different and more durable kind of argument.",
             kick='C · Why workers combined')

# ------------------------------------------------------ 13 · EMPLOYERS ANSWER
content_text('How employers answered organization',
             ['Union members fired',
              'Blacklists circulated the names of organizers',
               'Workers made to pledge they would not join a union',
               'Replacement workers hired during strikes'],
             "Employers understood the logic on the previous slide as clearly as the workers did, and they resisted organization itself, before any particular demand was on the table. Walk the four answers in the reading's order. Companies fired union members, which made joining itself a risk to the family's rent. They circulated blacklists of organizers, shared lists that kept a known union man from being hired anywhere in an industry or a town. They required pledges not to join a union as a condition of employment, contracts workers signed because the alternative was no job. And during strikes they hired replacement workers, which is why a strike was always a race between the union's funds and the employer's ability to restart production without it. This slide is the seed of section E. In the three defeats, students will watch these private weapons joined by public ones: militia, troops, and court orders.",
             kick='C · Why workers combined')

# ------------------------------------------------- 14 · SECTION D DIVIDER
divider_photo('powderly-port.jpg', 'Section D', 'Two Roads',
              ['The Knights reached for broad reform.', 'The AFL narrowed the fight to win it.'],
              "The portrait is Terence Powderly, who led the Knights of Labor through their great surge in the 1880s; the print is a colorized version of the standard likeness from his years in office. Two organizations dominate this section, and they disagreed about almost everything except the need to organize. The Knights of Labor took the broad road: one order for many kinds of workers, and a program that reached past wages to reforming the industrial system itself. The American Federation of Labor took the narrow road: skilled workers organized craft by craft, pursuing wages, hours, and conditions, with treasuries built to last. Frame the comparison as a genuine strategic argument, not a right answer and a wrong one. In 1886 the Knights were enormous and the AFL was a handful of unions. By the mid 1890s the positions had reversed, and section E explains much of why.",
              title_size=54)

# ------------------------------------------------------ 15 · KNIGHTS
content_text('The Knights of Labor: the broad road',
             ['Founded 1869; led in the 1880s by Terence Powderly',
              'One order: skilled and unskilled, factory hands and farmers',
              'Many women and Black workers, unusual for the time',
              'Goals: the eight-hour day, an end to child labor, worker ownership',
              'About 700,000 members by 1886'],
             "Give the Knights their full due before their fall, because the guided notes ask for both their reach and their numbers. The Knights of Labor, in the definition students will copy, are a national labor organization of the 1870s and 1880s that sought broad reform and organized many kinds of workers. Founded in 1869 and led in the 1880s by Terence Powderly, the Knights organized skilled and unskilled workers in the same order, factory hands and farmers together, and, unusually for the time, many women and Black workers. Their program reached beyond wages to broad reform: the eight-hour day, the end of child labor, and eventual worker ownership of industry. Membership surged after successful railroad strikes in 1885, to roughly 700,000 by some contemporary estimates in 1886. Hold the phrase contemporary estimates; the Knights kept loose records, and honest numbers for them are always approximate.",
             kick='D · Two roads', size=24)

# ------------------------------------------------------ 16 · AFL
content_photo('gompers-port.jpg', 'The AFL: the narrow road',
              ['Founded 1886 under Samuel Gompers',
               'A federation of craft unions, one skilled trade each',
               'Concentrated on wages, hours, and working conditions',
               'Dues and strike funds built to survive a long fight'],
              "The portrait is Samuel Gompers, photographed in 1911, late in a tenure that ran from the AFL's founding in 1886 until his death in 1924; he was younger, and the federation far smaller, in the years this lesson covers. The American Federation of Labor is, in the guided notes definition, a federation of craft unions founded in 1886 that focused on wages, hours, and working conditions. Each craft union organized one skilled trade, cigarmakers, iron molders, carpenters, and kept its own affairs. Gompers deliberately refused the Knights' broad program. No campaigns to remake the industrial system; instead, enforceable gains, won by collective bargaining and defended by money. The AFL built unions with dues and strike funds meant to survive a long fight. That unglamorous sentence is the strategic heart of the section, and the exit ticket will ask students to use it to explain why the AFL was still standing in 1900.",
              kick='D · Two roads')

# ------------------------------------------------------ 17 · SIDE BY SIDE
content_text('Two roads, side by side',
             ['Knights: many kinds of workers, one order, broad reform',
              'AFL: skilled crafts in separate unions, wages and hours first',
              'The Knights surged fast, and stretched wide',
              'The AFL grew slowly, and kept money in reserve',
              'Section E tests which road held up'],
             "Consolidate the comparison before the defeats, because students need it organized for the reading's second question and for the exit ticket. On membership: the Knights put many kinds of workers in one order, skilled beside unskilled, and welcomed groups other unions excluded; the AFL federated separate craft unions of skilled workers and left the unskilled largely outside. On goals: the Knights sought broad reform of the industrial order itself, up to worker ownership; the AFL concentrated on wages, hours, and working conditions that a contract could deliver this year. On structure: the Knights surged to perhaps 700,000 members on the strength of strike victories, with thin funds and loose control; the AFL collected dues and strike funds so a local could hold out. Neither road was foolish. Breadth gave the Knights numbers and moral reach; narrowness gave the AFL endurance. The next section shows what each quality was worth when employers, governments, and newspapers combined against them.",
             kick='D · Two roads', size=24)

# ------------------------------------------------- 18 · SECTION E DIVIDER
divider_photo('haymarket-port.jpg', 'Section E', 'Three Defeats',
              ['Haymarket, 1886. Homestead, 1892.', 'Pullman, 1894. One pattern.'],
              "The image is the famous Harper's Weekly engraving of the Haymarket bomb, published May 15, 1886, eleven days after the event. Warn students, as the activity does, that the engraving compresses the speech, the explosion, and the shooting into a single moment; it is evidence about what the public saw and feared as much as about what happened. That warning sets up the whole section. Between 1886 and 1894, three of the largest labor actions in American history ended in complete defeat, and the writing task will ask students to explain why. Take the cases in chronological order and keep the same questions for each: what did the workers want, what force was brought against them, and what broke first, their funds, their numbers, or their standing with the public? By Pullman, students should be naming the pattern before you do.",
              title_size=54)

# ------------------------------------------------------ 19 · HAYMARKET
content_text('Haymarket, Chicago, 1886',
             ['A national campaign for the eight-hour day',
              'May 4: a bomb thrown into the police ranks',
              'The thrower was never identified',
              'Eight leaders tried for their speeches; four were hanged',
              'The Knights, who had not called the meeting, were blamed'],
             "Teach Haymarket with the reading's care about what is known and what is not. On May 4, 1886, during a national campaign for the eight-hour day, a Chicago labor meeting in Haymarket Square was ending when police moved in to disperse it. Someone, never identified, threw a bomb into the police ranks. The blast and gunfire killed seven police officers and at least four civilians, by the counts most often given; totals differ across accounts. Eight anarchist leaders were tried for murder on the theory that their speeches had encouraged the act, and four were hanged. No evidence connected any of them to the bomb itself. Then the consequence that matters for the labor movement: in the public mind, labor and violence were now linked. The Knights of Labor, who had not called the meeting, were blamed too, and their membership collapsed within a few years. A movement can be defeated by association, without losing a vote or a battle.",
             kick='E · Three defeats', size=24)

# ------------------------------------------------------ 20 · HOMESTEAD
content_photo('frick-port.jpg', 'Homestead, 1892',
              ['Frick ran the works; Carnegie was in Scotland',
               'A lockout and a wage cut, aimed at the union itself',
               'About 300 Pinkerton guards arrived by barge',
               'Workers won the battle; 8,000 militia ended the strike'],
              "The portrait is Henry Clay Frick, from a Bain News Service photograph made years after 1892; Frick directed the company's side at Homestead while Andrew Carnegie was in Scotland, and students should never write that Carnegie ran the fight in person. The issue at Homestead was union survival itself. Frick set out to break the Amalgamated Association and cut wages, locked the workers out when the contract expired, and brought in about 300 armed Pinkerton guards by barge before dawn on July 6. Workers met them in a day-long gun battle in which about ten men died, and the Pinkertons surrendered. The victory lasted days. Pennsylvania sent some 8,000 militia, the plant reopened with replacement workers under military protection, and the strike collapsed by November. Steel remained largely unorganized for a generation. Private force lost the battle; public force won the strike.",
              kick='E · Three defeats')

# ------------------------------------------------------ 21 · PULLMAN STRIKE
content_photo('pullman-port.jpg', 'Pullman, 1894: the company town',
              ['Wages cut at the car works; rents in the company town not cut',
               'Workers struck in May 1894',
               'The American Railway Union boycotted Pullman cars',
               'Rail traffic stalled across much of the country'],
              "The photograph shows troops in formation outside the Arcade Building in Pullman during the strike, with residents watching from the foreground; it is a contemporary photograph from 1894, and the orderliness of the scene is itself the lesson's point about organized public force. The strike began in a company town. George Pullman cut wages at his railroad car works near Chicago during the depression of the 1890s but did not cut the rents in the town he owned, where his workers were required to live. His workers struck in May 1894 and appealed to Eugene V. Debs and the American Railway Union. The union voted to boycott all trains carrying Pullman cars, and rail traffic tied up across much of the country. Note the scale change from Homestead. A boycott that stopped the nation's trains, and with them the mail, was no longer a local dispute, and it drew a national answer, which is the next slide.",
              kick='E · Three defeats')

# ------------------------------------------------------ 22 · DEBS
content_photo('debs-port.jpg', 'Debs and the injunction',
              ['A federal court ordered the boycott stopped',
               'President Cleveland sent federal troops to Chicago',
               'The troops came over the governor\u2019s objection',
               'Debs jailed for violating the injunction; the union destroyed'],
              "The portrait shows Eugene V. Debs in 1897, three years after the Pullman strike, already the most famous labor leader in the country because of it. The legal tool that ended the strike is a vocabulary word, so define it in use: an injunction is a court order that requires or forbids a specific action. A federal court issued an injunction ordering the American Railway Union to stop interfering with the trains and the mail. President Cleveland then sent federal troops to Chicago over the governor of Illinois's objection, a state government protesting that it had not asked for help and did not want it. About thirty people died in clashes, by the estimate most often given. Debs refused to obey the injunction and was jailed for violating it; be precise that he was jailed for defying the court order, not for leading a strike. The union was destroyed, and the strike ended in complete defeat.",
              kick='E · Three defeats')

# ------------------------------------------------------ 23 · THE PATTERN
content_text('The pattern in the defeats',
             ['Employers: private guards, replacement workers, and lawyers',
              'Governments: militia, troops, and court orders',
              'Newspapers presented strikers as dangerous radicals',
              'Unions that stretched past their members and funds broke',
              "The AFL's narrower unions survived"],
             "End the section with the reading's own synthesis, which the notebook page and the writing task both build on. Across the three defeats the combination repeats. Employers hired private guards, replacement workers, and lawyers. Governments supplied militia, troops, and court orders, state force at Homestead, federal force at Pullman, and the courts at both Haymarket and Pullman. Newspapers commonly presented strikers as dangerous radicals, turning public opinion against them, which cost the Knights their membership without any battle at all. And unions that stretched beyond what their members and funds could hold broke under the strain, while the AFL's narrower unions survived. Have students fill the Three Defeats at a Glance table from this slide before you move on: for each strike, what the workers wanted, and why it ended in defeat. The writing task then asks them to rank these causes and defend the ranking, so the pattern needs to be theirs, not yours.",
             kick='E · Three defeats', size=24)

# ------------------------------------------------------ 24 · VOCAB A
vocab('Words for organizing',
      [('union', 'an organization of workers formed to bargain with employers as a group'),
       ('strike', "a work stoppage meant to pressure an employer to meet workers' demands"),
       ('collective bargaining', 'negotiation between an employer and workers organized as a group')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test's vocabulary matching draws on them. A union is an organization of workers formed to bargain with employers as a group. The definition's weight sits in its last three words: the group is the invention, the thing that made refusal expensive for an employer. A strike is a work stoppage meant to pressure an employer to meet workers' demands. Note that the definition says pressure, not persuasion; a strike works by stopping production, not by winning an argument. Collective bargaining is negotiation between an employer and workers organized as a group. Students met all three terms in section C, in use, before meeting them here as definitions. That order is deliberate: the vocabulary names machinery they have already watched run, and stall, in the three defeats.")

# ------------------------------------------------------ 25 · VOCAB B
vocab('Words for the fight and the law',
      [('injunction', 'a court order that requires or forbids a specific action'),
       ('Knights of Labor', 'a national labor organization of the 1870s and 1880s that sought broad reform and organized many kinds of workers'),
       ('American Federation of Labor', 'a federation of craft unions founded in 1886 that focused on wages, hours, and working conditions'),
       ('child labor', 'paid work by children, often in factories, mines, mills, and street trades')],
      "Four more terms, again matching the guided notes exactly. An injunction is a court order that requires or forbids a specific action; at Pullman it forbade the boycott, and Debs went to jail for violating it, which makes this the rare vocabulary word with a man's imprisonment inside it. The Knights of Labor are a national labor organization of the 1870s and 1880s that sought broad reform and organized many kinds of workers. The American Federation of Labor is a federation of craft unions founded in 1886 that focused on wages, hours, and working conditions. Students should hear the contrast inside the two definitions themselves: broad reform against wages, hours, and conditions. Finally, child labor is paid work by children, often in factories, mines, mills, and street trades, the practice section B counted at 1.75 million children in the census of 1900.",
      step=1.25)

# ------------------------------------------------------ 26 · TODAY'S WORK
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Judge the pattern yourself', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Return to the lesson question: why did workers organize, and why did collective action so often end in defeat?'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'Strike evidence stations for all three defeats, then your verdict'),
        ('Notebook', 'The three defeats chart, filled in as we study each strike'),
        ('Quick check', "A Little Spinner: read Hine's photograph against the wage facts"),
        ('Writing', 'Rank the causes of defeat, and answer the strongest counterargument')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=19, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.8, 11.5, 0.5, 'Exit ticket: why workers organized, what beat one strike, and why the AFL survived.',
     size=16, color=POWDER)
notes(s, "Close by handing the lesson to the students' own judgment, in four pieces. The activity, Strike Evidence Stations, walks them through Haymarket, Homestead, and Pullman one station at a time, image first, then a summary, then questions, and ends with a verdict: rank employer force, government power, and union overreach as explanations for the defeats, and defend the ranking from at least two stations. The notebook page is the three defeats chart they fill as they go: what the workers wanted, what the other side did, and how it ended and what it proved; it returns on review day. The quick check, A Little Spinner, asks them to read Hine's photograph against the wage facts from section B. The writing task states the lesson question as an argument: which single cause best explains why collective action failed, argued from at least two defeats, with the strongest counterargument answered. Collect the exit ticket on the way out.")

dc.save(OUT)
