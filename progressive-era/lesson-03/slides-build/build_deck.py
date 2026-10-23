#!/usr/bin/env python3
"""Lesson 3 deck, built to Alex's slide model (approved Lesson 1 system):
image-led slides, fragments only on screen, comprehensive speaker notes,
full lesson + vocabulary coverage. Fonts: Georgia titles, Lato body.
Shared helpers: deck_common.py."""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags,
                         photo_right, divider_photo, content_photo,
                         content_text, stat, divider_text)
from pptx.enum.text import PP_ALIGN

dc.IMG = os.path.join(HERE, 'img')
OUT = os.path.join(HERE, '..', 'lesson-03-slides.pptx')
W = dc.W

def vocab(title, terms, note, kick='The vocabulary'):
    s = slide(dc.CREAM)
    kicker(s, kick, color=dc.RUST)
    text(s, 0.9, 0.95, 11.5, 1.0, title, size=30, color=dc.NAVY, font='Georgia')
    yy = 2.1
    for term, dfn in terms:
        text(s, 0.9, yy, 4.1, 0.9, term, size=25, color=dc.NAVY, font='Georgia')
        text(s, 5.15, yy + 0.06, 7.3, 1.1, dfn, size=19, color=dc.MUTED, leading=1.2)
        yy += 1.52
    notes(s, note)
    return s

# ---------------------------------------------------------------- 1 · TITLE
s = slide(dc.NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, dc.prs.slide_width, dc.prs.slide_height)
rect(s, 0, 5.05, W, 2.45, dc.NAVY)
rect(s, 0, 5.05, W, 0.045, dc.RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'PROGRESSIVE ERA · LESSON 3', size=14, color=dc.RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Reforming Government', size=40, color=dc.CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Moving decisions from the bosses to the voters', size=17, color=dc.POWDER)
notes(s, "Lesson 2 ended with exposure: the muckrakers showed the country who was buying its government. Lesson 3 asks the next question. Why was American government so easy to buy in the first place? The reformers in this lesson answered that the problem was not only the buyers or the bought. The problem was the machinery: the procedures that decided who held office and how decisions got made. The image behind the title is Joseph Keppler's 1889 cartoon The Bosses of the Senate, published in Puck. Giant money bags labeled with the names of trusts loom over tiny senators at their desks, and the door marked as the people's entrance stands bolted shut. Keep that picture in mind all hour, because the lesson is the story of how reformers tried to unbolt the door. By the end, students should be able to name four tools of direct democracy, explain the Wisconsin Idea, state the hidden cost of city reform, and explain how the Seventeenth Amendment finally reached Washington.")

# ------------------------------------------------- 2 · ESSENTIAL QUESTION
s = slide(dc.NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did reformers redesign the machinery of democracy?', {})]],
     size=44, color=dc.CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did Americans respond to the problems created by industrialization, urbanization, and political corruption?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's lesson question sits at the top of the guided notes, with the unit question beneath it, exactly as on this slide: How did Americans respond to the problems created by industrialization, urbanization, and political corruption? Tell students that each lesson answers it a different way. Lesson 1 answered with the problems themselves. Lesson 2 answered with exposure. Today's answer is structural: Americans rewired the machinery of government so that voters could act directly instead of begging intermediaries to act for them. A cold open that works: ask what you do when a mayor is corrupt. Most students say vote him out. Then ask what you do when the process that produces every candidate is corrupt. That gap between the two answers is the whole lesson. Six key terms today, all of them mechanisms, and an exit ticket that asks students to match each mechanism to a situation in a single town.")

# ------------------------------------------------------------ 3 · THE MAP
s = slide(dc.NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.3, 11.5, 1.0, 'Rewiring the machinery', size=42, color=dc.CREAM, font='Georgia')
rule(s, 0.92, 2.32)
rows = [('A', 'The machinery problem', 'bosses and legislatures stood between voters and decisions'),
        ('B', 'Four tools', 'initiative, referendum, recall, direct primary'),
        ('C', 'The Wisconsin Idea', 'experts and evidence inside government'),
        ('D', 'City reform and its cost', 'new plans for running cities, and who paid for them'),
        ('E', 'The 17th Amendment', 'the voters choose senators at last'),
        ('F', 'A moral cause', 'temperance used the same tools, and won')]
yy = 2.72
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=24, color=dc.RUST_LT, font='Georgia')
    text(s, 1.55, yy + 0.02, 4.0, 0.6, t, size=21, color=dc.CREAM, bold=True)
    text(s, 5.75, yy + 0.07, 6.7, 0.6, d, size=17, color=dc.POWDER)
    yy += 0.74
notes(s, "This slide is the map of the lesson, and it matches the guided notes section for section. Section A states the diagnosis: the machinery problem. Section B unpacks the toolkit: initiative, referendum, recall, and the direct primary. Section C shows the proof of concept, the Wisconsin Idea, where one state ran the reforms as a working model. Section D moves to the cities, where reformers invented commission government and the city manager, and where the hidden cost of reform shows up. Section E takes the toolkit to Washington and the Seventeenth Amendment. Section F closes with the temperance movement, a moral cause that picked up the same tools and carried them to the Eighteenth Amendment. Three entries on the unit test blueprint live in this lesson: political reforms, the Seventeenth Amendment, and Prohibition. Tell students to keep the map open on their notes; every heading they fill in sits on this slide.")

# ------------------------------------------------- 4 · SECTION A DIVIDER
divider_photo('tweed-port.jpg', 'Section A', 'The Machinery Problem',
              ['Every decision had a man in the middle,', 'and the man in the middle could be bought'],
              "The cartoon is Thomas Nast's portrait of Boss Tweed, drawn for Harper's Weekly in 1871. Tweed's head is a money bag with a dollar sign on it, and the caption called him the brains that achieved the Tammany victory. Nast meant it literally: in the machine system, money did the thinking. Open section A by returning to Tweed, whom students met in Lesson 1 as the type of the city boss. Today's question is narrower and more useful than whether Tweed was wicked. It is why the system kept producing Tweeds. The reformers' answer was that between the voter and every decision stood a small group of intermediaries: bosses, convention delegates, legislators, ward men. Small groups can be reached, pressured, or bought, and as long as they stood there, exposure changed faces without changing outcomes.",
              title_size=46)

# ------------------------------------------------------ 5 · INTERMEDIARIES
content_text('The people in between',
             ['Party bosses and conventions chose the candidates',
              'State legislatures chose United States senators',
              'City councils answered to ward organizations',
              'At every level, a few people stood between the voter and the decision'],
             "Work through the chain of intermediaries slowly, because reading question 1 and the first guided notes blanks rest on it. Candidates were chosen by party bosses and convention delegates, so on election day voters picked between men the machine had already approved. Senators were chosen by state legislatures, so a corporation that wanted a friendly senator did not need to persuade a state's voters; it needed to purchase a few dozen legislators. City councils answered to ward organizations, which delivered the votes that kept councilmen in office. At every level, a small number of people stood between the voter and the decision, and those people could be reached, pressured, or bought. The reformers' conclusion, in the teacher key's phrasing, was that exposure alone could not fix a selection process that kept purchasable people in charge. The machinery itself had to change. Have students complete section A of the notes before moving on.",
             kick='Section A · The machinery problem')

# ----------------------------------------------------- 6 · DIRECT DEMOCRACY
content_text('The reformers\u2019 answer',
             ['Direct democracy: move decisions to the voters themselves',
              'Between 1898 and 1918, most states adopted at least one tool',
              'The states became laboratories, testing tools for the nation'],
             "The reformers' solution was direct democracy: move decisions from intermediaries to voters themselves. Between 1898 and 1918, most states adopted at least one of the new tools, and the states became, in the phrase of the era, laboratories where the tools were tested before the nation used them. Two points deserve emphasis. First, the reform was additive, not revolutionary. None of the tools removed legislatures or abolished representative government. They gave voters a way to act when legislatures would not, and a way to threaten legislators who were considering not acting. Second, the spread was fast because it was state by state. A reform that failed in one legislature could win in another state the next year, and each success became evidence for the next campaign. The four tools themselves are the next section, and students should be ready to distinguish them, because the exit ticket depends on the distinctions.",
             kick='Section A · The machinery problem')

# ------------------------------------------------- 7 · SECTION B DIVIDER
divider_text('Section B', 'Four Tools',
             'Four ways for voters to act when legislatures would not.',
             "This section is the toolkit, and it is the most heavily tested part of the lesson. Four tools: initiative, referendum, recall, and direct primary. Give students a shape for remembering them before the details land. The initiative creates law. The referendum decides law. The recall removes an official. The direct primary chooses the candidates. Two of the tools move lawmaking to the voters, one moves removal to the voters, and one moves nominations to the voters. What unites all four is the bypass: each one routes around a body the reformers no longer trusted. The next two slides take the tools in pairs, exactly as the guided notes present them, and the slide after that covers where each tool first appeared. Students should fill the lettered blanks in section B as each tool is introduced, not afterward.")

# ------------------------------------------------ 8 · INITIATIVE, REFERENDUM
content_text('Initiative and referendum',
             ['Initiative: citizens propose a law and put it on the ballot',
              'Referendum: a law goes to the voters for the final word',
              'Both let voters make law without waiting for a legislature'],
             "Two tools put lawmaking itself in voters' hands. The definition on the guided notes runs: initiative, citizens propose a law by petition and place it directly before the voters. Citizens write the law themselves, gather signatures on a petition, and place it directly on the ballot, where voters approve or reject it. The definition for the second tool runs: referendum, a law is sent to the voters for final approval or rejection. A referendum can begin with a petition against a law the legislature passed, or the legislature itself can send a law down for a final decision. The distinction students must hold is who starts the process and what is being decided. The initiative starts with citizens and produces a new law. The referendum is a yes or no verdict on a law that already exists or has been proposed. Reading question 2 asks for exactly this distinction, tool by tool.",
             kick='Section B · Four tools')

# ------------------------------------------------- 9 · RECALL, PRIMARY
content_text('Recall and the direct primary',
             ['Recall: voters remove an official before the term expires',
              'A petition, then a special vote on a single question',
              'Direct primary: the party\u2019s voters choose its candidates',
              'Nominations leave the convention hall'],
             "The other two tools concern people rather than laws. The guided notes define the first this way: recall, voters remove an elected official before the term expires, by petition and special vote. Citizens who collect enough signatures force a special election on a single question: does this official finish the term? The second definition runs: direct primary, an election in which a party's voters, not its bosses, choose the party's candidates. Of the four tools, the primary may have cut deepest, because the convention was where the machine's power lived. A boss who cannot choose the nominees has little left to sell. Note the order on the guided notes: the recall is blank 3 and the direct primary is blank 4, and the first statewide primary law belongs to Wisconsin in 1903 under Governor Robert M. La Follette, whose state is the subject of the next section.",
             kick='Section B · Four tools')

# ------------------------------------------------------ 10 · FIRST PLACES
content_text('Where the tools came from',
             ['South Dakota first: initiative and referendum, 1898',
              'Oregon built the fullest system after 1902, the Oregon System',
              'Wisconsin passed the first statewide direct primary, 1903',
              'The tools also worked as a threat over legislatures'],
             "The tools have birthplaces, and the guided notes test them. South Dakota adopted the statewide initiative and referendum first, in 1898. Oregon built the most complete system after 1902 and gave the tools their common name, the Oregon System. Wisconsin, under Governor Robert M. La Follette, passed the first statewide direct primary law in 1903. Give students the pattern rather than three isolated facts: the innovations came from the states, especially the West and upper Midwest, and they spread state to state as each success was reported in the national press. Close with the function that is easy to miss. The tools worked even when nobody used them. A legislature weighing a corrupt bargain now had to consider that angry voters could write their own law, reject the legislature's law, or end a career early. The threat disciplined legislators who were considering not acting, which is how the reading puts it.",
             kick='Section B · Four tools')

# ------------------------------------------------- 11 · SECTION C DIVIDER
divider_photo('lafollette-port.jpg', 'Section C', 'The Wisconsin Idea',
              ['One state showed the country', 'how reform actually worked'],
              "The photograph is Robert M. La Follette of Wisconsin, the central figure of this section. Wisconsin under La Follette became the model state of the reform era, and the reading insists that his method mattered as much as his laws. The Wisconsin Idea, the name his program carried, held that government should use trained experts the way a business used engineers. Where the machine staffed government with loyalists collecting payment for votes delivered, La Follette staffed it with professors. Set up the contrast plainly for students: two theories of who should run a modern state. One says government is a prize to be distributed among the faithful. The other says government is a technical problem to be solved by people who know how. The next two slides give the method and then the record it produced.",
              title_size=46)

# --------------------------------------------------------- 12 · EXPERTS
content_text('Government by experts',
             ['Professors from the University of Wisconsin drafted the bills',
              'Experts staffed the commissions and measured the results',
              'Knowledge treated as a public resource'],
             "La Follette brought professors from the University of Wisconsin into state service to draft bills, staff commissions, and measure results. Each verb matters. Drafting bills meant the laws were written by people who understood the industries being regulated, rather than by lobbyists handing text to friendly legislators. Staffing commissions meant the agencies that set railroad rates and supervised corporations were run by experts with tenure in their subjects. Measuring results meant a reform could be tested against evidence and adjusted, the way an engineer tests a bridge design. The guided notes reduce this to three blanks in section C: trained experts, the University of Wisconsin, and evidence. Have students notice the deeper claim underneath the method. The Progressives believed that the problems of an industrial society were complicated but solvable, and that knowledge, honestly applied, was a public resource like roads or schools.",
             kick='Section C · The Wisconsin Idea')

# --------------------------------------------------- 13 · WISCONSIN RECORD
content_text('What Wisconsin did',
             ['A railroad commission setting rates on evidence, not influence',
              'Fairer taxes on corporations',
              'The direct primary, first statewide law, 1903',
              'Delegations traveled to Madison to study the model'],
             "The record in Wisconsin is what made other states pay attention. La Follette's railroad commission set rates on evidence instead of influence, hearing testimony and examining costs rather than trading favors. Wisconsin taxed corporations more fairly, regulated railroads, and passed the direct primary in 1903, the first statewide law of its kind. Then came the reputation effect: delegations from other states traveled to Madison to study how it was done, treating Wisconsin as a working demonstration that the reforms operated in practice and not only in speeches. That phrase is nearly the teacher key's answer to reading question 3, so plant it firmly. La Follette left the governorship for the United States Senate in 1906 and carried the program national, which points the lesson toward Washington. But first the cities, where experimentation ran fastest and where the cost of reform becomes visible.",
             kick='Section C · The Wisconsin Idea')

# ------------------------------------------------- 14 · SECTION D DIVIDER
divider_photo('galveston-port.jpg', 'Section D', 'City Reform and Its Cost',
              ['Cities experimented fastest,', 'because their failures were visible'],
              "The photograph shows Galveston, Texas, at 18th and N Streets after the hurricane of 1900, from the Bain News Service collection at the Library of Congress. Cities experimented fastest because their failures were visible: bad water, uncollected garbage, bought councils, and in Galveston's case a storm that devastated the city and discredited its government in a single night. Section D covers two inventions that came out of the cities, commission government and the council-manager plan, and then a cost that attaches to both of them. Warn students to listen for the cost as the inventions are introduced. It is the part of the story the reformers themselves rarely advertised, and reading question 5 and the last blanks in section D of the guided notes both turn on it.",
              title_size=42)

# -------------------------------------------------------- 15 · GALVESTON
content_text('Galveston starts over',
             ['A hurricane devastated Galveston in 1900',
              'Mayor and council replaced by a small elected commission',
              'Each commissioner ran one department',
              'The plan spread to hundreds of cities'],
             "After the hurricane devastated Galveston in 1900, the city replaced its mayor and council with a small elected commission, and the guided notes date the change to 1901. The definition students copy runs: commission government, a city run by a small elected commission, each member heading one department. One commissioner might run police and fire, another finance, another streets and water. The appeal was accountability in a business form. Instead of a council where responsibility dissolved into committees and ward trading, a voter could name the exact official in charge of the water supply. The commission government spread to hundreds of cities within the decade, which tells students how hungry cities were for an alternative to the ward system. Note what the plan kept and what it removed. It kept elections. It removed the mayor, the council, and the ward map that came with them, and that removal is where the next slide's cost begins.",
             kick='Section D · City reform')

# ------------------------------------------------------ 16 · THE COST
content_text('The cost nobody advertised',
             ['Council-manager plan: an elected council hires a professional manager',
              'Like a school board hiring a superintendent',
              'Administration in place of politics',
              'Ward politics weakened, and with it a working-class share of power'],
             "The second invention was the council-manager plan. The council stayed elected and kept policy, but it hired a professional to run daily operations, the way a school board hires a superintendent. The definition on the guided notes runs: city manager, a professional administrator hired by an elected council to run a city's daily operations. Both plans tried to substitute administration for politics. Both also carried a cost the reformers rarely advertised. Commission and manager governments weakened ward politics, and ward politics, corrupt as it was, had been the route by which immigrant and working-class voters won jobs, services, and a share of power. At-large commissioners and appointed managers answered to the whole city's electorate and to professional standards, which in practice often meant to middle-class reformers. Reading question 5 asks students to name the cost and the group that paid it: immigrant and working-class voters. Connect this back to Lesson 1, where the machine's usefulness explained its survival.",
             kick='Section D · City reform')

# ------------------------------------------------- 17 · SECTION E DIVIDER
divider_photo('capitol-port.jpg', 'Section E', 'The Seventeenth Amendment',
              ['The largest machinery failure', 'sat in Washington'],
              "The photograph is the United States Capitol as it looked around 1900. The largest machinery failure sat in Washington. Under the Constitution as written, state legislatures elected United States senators, which made the Senate, the chamber designed to be insulated and deliberate, into the chamber most exposed to purchase. A corporation that wanted a senator bought the legislature that chose him, and the price of a few dozen legislators was trivial next to the value of a friendly vote on railroad or tariff policy. This section follows the same shape as section A: name the intermediaries, show why they could be bought, then watch the reformers build a bypass. The difference is that this bypass required amending the Constitution itself, the only one of today's reforms that did.",
              title_size=38)

# --------------------------------------------------------- 18 · PHILLIPS
content_photo('phillips-port.jpg', 'The Treason of the Senate',
              ['Senate seats became prizes for rich men',
               'Deadlocked legislatures left seats empty for years',
               'Phillips named the interest each senator served'],
              "The portrait is David Graham Phillips, whose 1906 magazine series The Treason of the Senate students met in Lesson 2. Phillips documented, senator by senator, the railroad and corporate interests that members of the Senate served. His reporting landed because the structure made it plausible. Senate seats became prizes for rich men, who could treat a legislature as a purchase. Deadlocked legislatures sometimes left seats empty for years, so a state could go unrepresented in one of its two Senate seats while politicians bargained. The guided notes compress this into two blanks: legislatures, and seats left empty for years. Emphasize the reformers' framing once more. The scandal was not simply that individual senators took direction from corporations. It was that the selection method guaranteed a Senate responsive to wealth, because wealth was what the method priced. Changing the men without changing the method had been tried for decades.",
              kick='Section E · The Seventeenth Amendment')

# ------------------------------------------------------------ 19 · STAT 1913
stat('1913', 'the Seventeenth Amendment makes direct election of senators the law',
     'States like Oregon had already routed around the Constitution: voters chose, and legislatures ratified the choice.',
     "States forced the issue before the Constitution moved. Oregon and others let voters choose senators in a popular vote and then pressured their legislators to ratify the choice, making legislative election a formality. The workaround spread until the formal rule was an embarrassment: state after state was electing senators in everything but name. In 1913 the Seventeenth Amendment made the workaround the law, establishing direct election of senators by the voters of each state. That last phrase is the final blank in section E of the guided notes. Reading question 4 asks how states forced the issue, and the answer is the Oregon method: popular votes plus pressure on legislators to ratify the result. Name the larger pattern for students before moving on. When formal machinery blocks reform, reformers in this era repeatedly built an informal practice first and let the law catch up to the practice.",
     kick='Section E · The Seventeenth Amendment')

# ------------------------------------------------- 20 · SECTION F DIVIDER
divider_photo('willard-port.jpg', 'Section F', 'A Moral Cause',
              ['The same tools, picked up', 'by the era\u2019s largest moral campaign'],
              "The portrait is Frances Willard, who led the Woman's Christian Temperance Union for two decades and turned it into one of the largest organizations in the country. Open the final section with the neutrality of the toolkit. Direct democracy tools were neutral; any organized cause could use them. Nothing in the initiative, the referendum, or the pressure campaign required the cause to be about government structure at all. The era's largest moral campaign, the drive to prohibit alcohol, used petitions, referenda, and pressure politics at national scale, with exactly the discipline the political reformers had taught. The temperance movement is where students see the tools escape their inventors' purposes, which is why this section exists and why the unit returns to Prohibition in Lesson 8.",
              title_size=46)

# ---------------------------------------------------------- 21 · TEMPERANCE
content_text('The drive against alcohol',
             ['The WCTU and the Anti-Saloon League built the campaign for decades',
              'Petitions and referenda, town by town and state by state',
              '1919: the Eighteenth Amendment prohibits alcohol',
              'Lesson 8 returns to what Prohibition taught'],
             "Two organizations built the prohibition campaign. The Woman's Christian Temperance Union, led for twenty years by Frances Willard, supplied the mass membership, organized town by town through churches and local unions. The Anti-Saloon League supplied the political machinery: single-issue pressure that rewarded friends and punished enemies regardless of party, applied at every level from the township to Congress. The campaign ran for decades, town by town and state by state, stacking local victories until a national amendment was possible. In 1919 the Eighteenth Amendment prohibited the manufacture and sale of alcohol across the United States, a result the guided notes record in section F. Set the closing note of the lesson carefully. Prohibition was the tools' greatest victory and, as Lesson 8 will show, the clearest demonstration of their limits, because a constitutional amendment could change the law faster than it could change behavior.",
             kick='Section F · A moral cause')

# ------------------------------------------------------------- 22 · VOCAB A
vocab('Words for acting directly',
      [('initiative', 'citizens propose a law by petition and place it directly before the voters'),
       ('referendum', 'a law is sent to the voters for final approval or rejection'),
       ('recall', 'voters remove an elected official before the term expires, by petition and special vote')],
      "These definitions match the guided notes word for word, so students can copy them directly and the unit test's matching section will use them nearly verbatim. Initiative: citizens propose a law by petition and place it directly before the voters. Referendum: a law is sent to the voters for final approval or rejection. Recall: voters remove an elected official before the term expires, by petition and special vote. Drill the distinctions, not just the words. Ask who starts each process and what the voters decide. The exit ticket opens with a single town using three tools at once: voters petition a park law onto the ballot, vote to remove their mayor, and choose a party's candidate for governor. The first of those is the initiative, and students who hesitate here usually fix the hesitation by remembering that the initiative is the only tool that begins with citizens writing a law.")

# ------------------------------------------------------------- 23 · VOCAB B
vocab('Words for the new machinery',
      [('direct primary', 'an election in which a party\u2019s voters, not its bosses, choose the party\u2019s candidates'),
       ('commission government', 'a city run by a small elected commission, each member heading one department'),
       ('city manager', 'a professional administrator hired by an elected council to run a city\u2019s daily operations')],
      "Three more terms, again matching the guided notes exactly. Direct primary: an election in which a party's voters, not its bosses, choose the party's candidates. Commission government: a city run by a small elected commission, each member heading one department. City manager: a professional administrator hired by an elected council to run a city's daily operations. The exit ticket's third scenario, choosing the party's candidate for governor, is the direct primary, and its second question asks why reformers distrusted legislatures to fix the Senate problem on their own. The teacher key's point is the conflict of interest: legislatures were the body whose members benefited from choosing senators and were themselves the purchasable intermediaries, so asking them to surrender the power voluntarily asked the problem to solve itself. The final exit ticket question asks which tool is strongest and which is most open to abuse; strong answers often name the initiative as strongest because it creates law, and the recall as most abusable because it can punish a single unpopular decision.")

# --------------------------------------------------------- 24 · TODAY'S WORK
s = slide(dc.NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Ballot Simulation: A 1908 Mill Town', size=40, color=dc.CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['One day at the ballot box in Millbrook. All four tools appear on the same ballot. Vote on each item, and write your reason.'],
     size=22, color=dc.POWDER, leading=1.3)
rows = [('Item 1 · Initiative', 'a factory inspection law, petitioned onto the ballot'),
        ('Item 2 · Referendum', 'the council\u2019s thirty-year streetcar franchise'),
        ('Item 3 · Recall', 'Mayor Brandt, who took the streetcar company\u2019s money'),
        ('Item 4 · Direct primary', 'a factory inspector against the bosses\u2019 candidate')]
yy = 4.3
for t, d in rows:
    text(s, 0.9, yy, 3.6, 0.6, t, size=18, color=dc.RUST_LT, bold=True)
    text(s, 4.7, yy, 7.9, 0.6, d, size=18, color=dc.CREAM)
    yy += 0.6
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: name the tool in each scenario, and judge which tool is strongest and which most open to abuse.',
     size=15, color=dc.POWDER)
notes(s, "Close by handing the lesson to the activity, the ballot simulation set in Millbrook, a fictional mill town on election day in 1908. Millbrook has adopted all four tools, and all four appear on the same ballot, which is what makes the simulation a review disguised as a vote. Item 1 is an initiative, a factory inspection law that citizens petitioned onto the ballot after a mill fire killed nine workers behind a locked door. Item 2 is a referendum on the council's thirty-year streetcar franchise. Item 3 is the recall of Mayor Brandt, who took the streetcar company's money and then voted for its franchise without breaking any law a prosecutor can prove. Item 4 is the town's first direct primary, a former factory inspector against a railroad attorney endorsed by the bosses. Students mark each vote and write a reason; the grading is in the reasons, not the choices. Then tally the class and work Part 2. Finish with the exit ticket from the guided notes.")

dc.save(OUT)
