#!/usr/bin/env python3
"""Depression and New Deal Lesson 2 deck, "Hoover and the Limits of
Voluntarism," built to the approved Twenties system: image-led slides,
fragments only on screen, comprehensive speaker notes, full lesson +
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

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'THE DEPRESSION AND NEW DEAL · LESSON 2', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Hoover and the Limits of Voluntarism', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'What the president did, and why it fell short of the collapse', size=17, color=POWDER)
notes(s, "The photograph shows the Bonus Army camp at Anacostia in Washington in 1932, photographed by Harris and Ewing and held by the Library of Congress. It is a hard image to open a lesson about a president with, and that is the point: by the summer of 1932, the argument over Herbert Hoover's program was being held in camps and breadlines, not only in newspapers. The last lesson measured the collapse and closed with a question: private misfortune or public emergency. Hoover was the first president who had to answer that question, and he answered it from beliefs he had held all his life. This lesson takes his program seriously in three moves: what he believed, what he actually did, and where the program met its limits. Students should leave able to correct the do nothing caricature and still explain, from the record, why the voters of 1932 delivered their verdict.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('What did President Hoover do about the Depression, and why did his program fall short of the collapse?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the New Deal change the relationship between Americans and their federal government, and what did it leave undone?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question has two halves and the exit ticket tests both. The first half asks what Hoover did, and it must be answered from the record, which is fuller than the famous caricature: a farm board, wage pledges, expanded public works, a tariff, a lending corporation, and a late step toward relief loans. The second half asks why that program fell short, and it must be answered from design and scale, not from the president's character or effort. The unit question runs beneath as the frame. Hoover's answer to the crisis kept the federal government's relationship with ordinary citizens at arm's length: Washington encouraged, coordinated, and lent to institutions, and citizens in need dealt with charities, cities, and states. The New Deal lessons that follow are the story of that relationship changing. Keep the contrast in reserve today and let students build it themselves from the relief desk activity.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'A real program, measured against a larger collapse', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', "Hoover's beliefs", 'Rugged individualism and voluntarism'),
        ('B', 'What Hoover did first', 'Farm Board, pledges, public works'),
        ('C', 'The Hawley-Smoot Tariff', 'Protection answered by retaliation, 1930'),
        ('D', 'Lending at the top', 'The RFC, and one step toward relief, 1932'),
        ('E', 'The Bonus Army', 'Veterans camped in Washington, cleared by troops'),
        ('F', 'The election of 1932', 'A verdict on conditions, 57 percent for Roosevelt'),
        ('G', 'The interregnum', 'Four months, and the banks closed state by state')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A covers the beliefs, because Hoover's policy followed from them and cannot be understood without them. Sections B, C, and D cover the record in chronological order: the early measures of 1929 and 1930, the tariff, and the lending programs of 1932. Section E covers the Bonus Army, the moment the argument became visible in the capital itself. Sections F and G cover the election and the long winter that followed it, when the banking system shut down while two presidents shared a crisis. Tell students the summary table at the end of their guided notes, Hoover's Program at a Glance, asks them to rebuild this map as beliefs, actions, limits, and verdict.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_photo('hoover-port.jpg', 'Section A', "Hoover's Beliefs",
              ['A relief organizer who believed', 'relief was not Washington\'s work.'],
              "The portrait is by Douglas Granville Chandor and is held by the National Portrait Gallery; the Commons file page marks it CC0. Begin with the biographical fact students least expect. Hoover was the most experienced relief administrator ever to hold the presidency. During the First World War he had organized food relief for occupied Belgium and later directed relief across Europe, feeding millions of people. He was not a man indifferent to hunger, and he was not a man who had never run a large program. His refusal of direct federal relief was a considered position, argued from principle and from his reading of the Constitution, and students should be able to state it in its strong form before they judge it. Section A covers that position in its two parts: the belief, rugged individualism, and the method built on it, voluntarism. Both are vocabulary terms, and both are tested.",
              title_size=40)

# ------------------------------------------------------ 5 RUGGED INDIVIDUALISM
content_text('What Hoover believed about relief',
             ['Americans should succeed through their own effort',
              'Direct federal relief would weaken character',
              'It would unbalance the federal budget',
              'It would expand Washington into local duties',
              'His standard came from a lifetime in relief work'],
             "In the guided notes definition, rugged individualism is Hoover's belief that Americans should succeed through their own effort and that direct federal relief would weaken character and self reliance. Unpack the belief rather than mocking it, because students will meet its descendants all their lives. Hoover held that a citizen paid by Washington in hard times was being trained out of the habits that made citizens: work, saving, mutual aid among neighbors, and local responsibility. He added a fiscal argument, that relief spending would unbalance the budget and shake confidence in the government's credit, and a constitutional argument, that relief had always belonged to communities and states. Teachers should note where his own career cut against the caricature: nobody in the country had fed more people than Hoover had, through voluntary and cooperative organizations. His claim was that the method was the point: relief organized voluntarily preserved the citizen, and relief paid by the federal government diminished him. The next slide gives the method.",
             kick='A · Hoover\'s beliefs', size=24)

# ------------------------------------------------------ 6 VOLUNTARISM
content_text('Cooperation instead of compulsion',
             ['Business: hold wages, keep building',
              'Charities and cities: feed the hungry',
              'The president: summon leaders, win pledges, publicize them',
              'The federal government: encourage and coordinate',
              'What it would not do: pay relief itself'],
             "In the guided notes definition, voluntarism is Hoover's policy of meeting the Depression through voluntary cooperation by business, charities, and local government rather than through federal relief programs. Walk the division of labor on the slide, because the exit ticket asks students to name the carriers. Business would maintain wages and construction. Charities, churches, and city governments would feed and shelter the unemployed. The president would summon leaders to Washington, extract pledges, and publicize them, using the office as a coordinator and a spotlight. The federal government would set the example with its own building program and would balance its budget. What the design never contained was a federal payment to a family. Students should notice the design's hidden assumption while it is still on the screen: every carrier in the system, business profits, donations, and city tax revenue, shrank as the Depression deepened. A system funded by prosperity was asked to operate in a collapse.",
             kick='A · Hoover\'s beliefs', size=24)

# ------------------------------------------------- 7 SECTION B DIVIDER
divider_photo('dam-port.jpg', 'Section B', 'What Hoover Did First',
              ['Workers high on the canyon wall', 'at the Colorado River dam, 1932.'],
              "The photograph is a National Archives record from October 1932, showing workers employed as high scalers on the construction of the great dam on the Colorado River, the dam that later carried Hoover's name. It opens the section that corrects the record. Hoover acted earlier and more broadly than the later caricature of a do nothing president allows, and this section is the evidence: a farm board in 1929, pledges extracted from business, and an expanding federal building program. Students should be asked to hold two judgments separately from here on. The first is factual: did the president act? He did, repeatedly, and by the standards of earlier presidents in earlier downturns, aggressively. The second is evaluative: was the action built to the scale of this collapse? That question stays open through the tariff and the lending sections, and the activity will make students answer it case by case.",
              title_size=40)

# ------------------------------------------------------ 8 FARM BOARD AND PLEDGES
content_text('1929: farms, pledges, and building',
             ['Federal Farm Board: loans to farm cooperatives',
              'Cooperatives would hold crops and steady prices',
              'Business leaders pledged to hold wages and construction',
              'For a time, many held to their pledges',
              'The pledges had no force of law behind them'],
             "The Federal Farm Board came first, in 1929, before the crash had finished becoming a depression. It lent money to farm cooperatives so they could hold crops off the market and steady prices, on the theory that farm prices, which had been weak all through the 1920s, were the economy's first ailment. Alongside it, Hoover summoned business leaders and won pledges to maintain wages and keep construction going, and for a time many held to their pledges. Teach the structural point inside the chronology: a pledge is a promise, not a law, and it holds only while the promiser can afford it. When prices and orders kept falling through 1931, the wage pledges broke across industry, one firm at a time, each firm able to say truthfully that it could not pay 1929 wages on 1931 orders. Voluntarism had no answer to that arithmetic, because its whole design refused compulsion. The farm tool had a matching limit, which the relief desk activity tests: a loan against a crop helps a farmer who has one.",
             kick='B · What Hoover did first', size=24)

# ------------------------------------------------------ 9 PUBLIC WORKS
content_photo('dam-port.jpg', 'Building as policy',
              ['Dams, roads, and public buildings',
               'Jobs now, and structures that last',
               'Federal spending rose as revenue fell',
               'The Colorado River dam: the largest project',
               'Real jobs, against millions out of work'],
              "In the guided notes definition, public works are government funded construction projects such as dams, roads, and public buildings, built to provide jobs as well as lasting structures. Hoover expanded federal public works and increased spending on them as tax revenue fell, which students should register as a genuine departure: the federal government was building against the downturn on purpose. The photograph shows the scale of the largest project, the great dam on the Colorado River, with workers suspended on the canyon wall in 1932. Dams and courthouses had the double virtue the definition names: wages this winter and structures for a generation. The limit was arithmetic. A building program employs thousands, in particular places, on particular skills. The collapse had put millions out of work in every trade and county at once. Public works under Hoover were a real instrument used at an unreal scale, and students will need that distinction again when they reach the far larger building programs of the New Deal lessons.",
              kick='B · What Hoover did first')

# ------------------------------------------------- 10 SECTION C DIVIDER
divider_text('Section C', 'The Hawley-Smoot Tariff',
             'The one measure that worked against recovery from the start.',
             "Every program has a measure its defenders stop mentioning, and for Hoover's program it is the tariff of 1930. Set the scene accurately. Farmers and manufacturers had demanded protection from foreign goods through the 1920s, Congress obliged with the highest tariff in the country's history, and more than a thousand economists petitioned the president to veto the bill. He signed it. This section is short, and its lesson is about connection: an economy in collapse was selling to the world, and a policy that shrank world trade shrank the markets of the very workers it claimed to protect. Students should watch for the word retaliation, because it is the mechanism. Tariffs are answered by tariffs. The guided notes ask for the signing date, the economists' petition, and the export result, so give all three plainly in the next slide.")

# ------------------------------------------------------ 11 TARIFF
content_text('Protection, answered by retaliation',
             ['Signed June 1930, over a petition from economists',
              'Tariffs raised to the highest level in the country\'s history',
              'Trading partners raised their own tariffs in return',
              'American exports fell further',
              'Farmers lost foreign buyers they could not replace'],
             "In the guided notes definition, the Hawley-Smoot Tariff is the 1930 law that raised United States tariffs to the highest level in the country's history, and drew retaliation that cut world trade. Walk the sequence as cause and effect. Protection was meant to reserve the American market for American producers. Abroad, the law read as the largest economy closing its doors, and trading partners raised their own tariffs in return, some within the year. American exports, already falling with the collapse, fell further. The cruelest incidence fell on farmers, the group the tariff was sold to help: American agriculture grew far more than the home market could eat, and the foreign buyers lost to retaliation could not be replaced at home. A tariff can redistribute a market. It cannot enlarge one, and in 1930 the world's markets were the thing in shortest supply. Students should file this measure under limits of the program even though it was an action, because it is the clearest case of the administration's tools working against its aims.",
             kick='C · The Hawley-Smoot Tariff', size=24)

# ------------------------------------------------- 12 SECTION D DIVIDER
divider_text('Section D', 'Lending at the Top',
             'In 1932 Hoover went further than his beliefs had once allowed.',
             "By the winter of 1931 to 1932, banks were failing by the thousand and the voluntary machinery was visibly exhausted. This section covers Hoover's furthest steps, and students should mark how far he traveled: the president who refused federal relief created a federal corporation to lend public money, and then authorized it to lend to states for relief itself. The movement is part of the unit's argument. The line between Hoover and the New Deal that followed him was real, but it was a line of scale and directness, not a line between action and inaction. The two instruments of 1932 are the Reconstruction Finance Corporation of January and the Emergency Relief and Construction Act of July. Teach them as one design with one hope, stability at the top restoring jobs below, and then teach why the hope failed at the bottom, which is where the families were.")

# ------------------------------------------------------ 13 RFC
content_text('The Reconstruction Finance Corporation',
             ['Created in January 1932',
              'Federal loans to banks, railroads, and insurance companies',
              'A saved bank would lend again',
              'A saved railroad would keep its crews',
              'Credit would reach families at the bottom, in time'],
             "In the guided notes definition, the Reconstruction Finance Corporation is the federal agency created in 1932 that lent public money to banks, railroads, and insurance companies in the hope that stability at the top would restore jobs below. State the hope as a chain, because students judge chains link by link. Lend to a bank and the bank survives; a surviving bank lends to farmers and merchants; borrowers hire and spend; jobs return at the bottom. Lend to a railroad and its crews stay on payroll. The design was not foolish, and parts of it worked: the RFC did keep institutions alive, and a version of it operated for years. Its flaw was the chain's middle link. Banks that had watched loans fail for two years used federal money to repair their own balance sheets and were too weak or too frightened to lend. Stability at the top pooled there, and the bottom, where families waited for wages and credit, stayed dry through 1932.",
             kick='D · Lending at the top', size=24)

# ------------------------------------------------------ 14 ERCA AND THE BOTTOM
content_text('One step toward relief, taken as loans',
             ['July 1932: the Emergency Relief and Construction Act',
              'The RFC could lend to states for relief',
              'Loans, not grants, under strict conditions',
              'States already in debt could borrow only so much',
              'Pledged wages were cut anyway; charity funds ran out'],
             "The Emergency Relief and Construction Act of July 1932 was Hoover's one step toward federal relief, and its design tells the whole story of his limits in a single statute. For the first time, a federal agency could put money into relief, but the money traveled as loans to states, which had to apply, qualify, and repay. A state already in debt, with its tax revenue collapsing, could borrow only so much, and the relief then had to pass through state and city machinery before it reached a family. Set beside it the rest of the 1932 record from the reading: wages pledged in 1929 were cut across industry, banks used federal loans to repair their balance sheets rather than lend, and charities and city relief funds were exhausted in front of growing lines. The program was not nothing. Measured against a collapse with about one worker in four out of work, it was not enough, and it arrived in the wrong order: help for institutions first, and relief for families last.",
             kick='D · Lending at the top', size=24)

# ------------------------------------------------- 15 SECTION E DIVIDER
divider_photo('bonus-port.jpg', 'Section E', 'The Bonus Army',
              ['Veterans on the Capitol lawn,', 'July 13, 1932.'],
              "The photograph, by Underwood and Underwood, shows members of the Bonus Army on the United States Capitol lawn on July 13, 1932, two weeks before the camps were cleared. Section E covers the episode that fixed Hoover's image for the voters who judged him that November. Teach it as a case in the difference between a claim and a gift. The veterans were not asking for charity. Congress had voted them a service bonus in 1924, payable in 1945, and they were asking to collect a debt early, in a year when collecting it could mean food and rent. A government can refuse a gift and be called hard. Refusing creditors who had fought in the country's war, and then clearing their camps with troops, read to the country as something worse. The photographs did the rest, and students should be ready to explain how.",
              title_size=40)

# ------------------------------------------------------ 16 THE CAMPS
content_photo('camp-port.jpg', 'A bonus asked for thirteen years early',
              ['Veterans of the First World War, out of work',
               'A bonus voted in 1924, due in 1945',
               'Thousands camped across Washington',
               'The largest camp stood on the Anacostia flats',
               'Many brought their families with them'],
              "In the guided notes definition, the Bonus Army is the veterans of the First World War who camped in Washington in the summer of 1932 demanding early payment of their promised service bonus, and were driven out by federal troops. Give the camp its human scale before the politics. Thousands of veterans, many with wives and children, built camps across the capital in the summer of 1932, the largest on the flats across the Anacostia River, with streets, kitchens, and its own order. They were, in the main, orderly, and the city lived beside them for weeks. Congress considered the early payment and refused it, holding to the 1945 date and to the budget. Most veterans accepted the answer and drifted home on borrowed fare. A few thousand stayed, in camps the administration now wanted emptied before the political conventions and the autumn campaign. What happened next is the next slide, and its date, July 28, belongs in the notes.",
              kick='E · The Bonus Army')

# ------------------------------------------------------ 17 JULY 28
content_text('Cleared by the army they had served in',
             ['July 28, 1932: clashes with police in the city',
              'Hoover ordered the army to clear the camps',
              'Troops under General Douglas MacArthur',
              'Tanks, cavalry, and tear gas',
              'The Anacostia camp was burned'],
             "Narrate July 28 in order and without decoration. After clashes between veterans and police in the city, in which veterans were shot, Hoover ordered the army to clear the camps. Federal troops under General Douglas MacArthur drove the veterans out with tanks, cavalry, and tear gas, crossed to Anacostia, and the camp there burned, whether set by troops or in the confusion was argued then and since. The reading's summary is the one students should keep: photographs of the burning camp fixed the president's image for the voters who would judge him in November. Ask the class to test that sentence rather than accept it. A president's image rests on the pictures the country sees of his choices, and the picture of 1932 was soldiers against veterans and a burning camp, set against breadlines in every city. No speech about the budget could outrun it. The election section now gives the verdict the image helped write.",
             kick='E · The Bonus Army', size=24)

# ------------------------------------------------- 18 SECTION F DIVIDER
divider_photo('fdr-port.jpg', 'Section F', 'The Election of 1932',
              ['Franklin D. Roosevelt, photographed', 'by Elias Goldensky in 1933.'],
              "The portrait shows Franklin Delano Roosevelt, photographed by Elias Goldensky in December 1933, already president; the Library of Congress holds it, and its date after the election is worth one honest sentence. Section F covers the verdict. The Democrats had nominated the governor of New York, who promised a new deal for the American people and campaigned as a man willing to experiment. Hoover defended his record and warned that Roosevelt's promises would unbalance the budget and shake confidence. Students should be pressed on what an election measures in a collapse. The voters of 1932 were not grading a seminar paper on voluntarism. They were voting in a country where about one worker in four was out of a job, banks were closing, and troops had cleared veterans from the capital. The result, on the next slides, was one of the largest defeats ever handed to a sitting president.",
              title_size=38)

# ------------------------------------------------------ 19 THE VERDICT
content_text('A verdict on conditions',
             ['Roosevelt: a new deal, and a promise to act',
              'Hoover: the record defended, the budget warned over',
              'Voters were not voting on a theory',
              'One worker in four stood out of work',
              'The defeat reached across the whole map'],
             "The election of 1932 was less a contest of programs than a verdict on conditions, and students should be able to defend that sentence from the reading. Roosevelt offered a phrase, a new deal, a temperament, energy and willingness to experiment, and very little in the way of a detailed program that a voter could price. Hoover offered a record and a warning. In an ordinary year the record and the warning might have carried. In 1932 the electorate contained millions of families for whom the existing arrangement had already failed at the level of food, rent, and savings, and they voted accordingly. Teach the result as evidence about the program, not as a popularity score: when an incumbent's defense is that his measures are working, and the country answers with one of its largest defeats, the country is reporting its experience of the measures. The exact size of the answer is the next slide's figure, and it belongs in the guided notes.",
             kick='F · The election of 1932', size=24)

# ------------------------------------------------------ 20 ELECTION STAT
stat('57%', "Roosevelt's share of the popular vote in 1932",
     'Forty-two of the forty-eight states · One of the largest defeats ever handed to a sitting president',
     "Put the two figures together, because the guided notes test both. Roosevelt won about 57 percent of the popular vote and carried forty-two of the forty-eight states. A sitting president was not merely beaten; he was beaten nearly everywhere, in farm states and industrial states, in cities and in counties, which is what a verdict on conditions looks like on a map. Hoover carried six states. Students who want to argue that the election turned on personality or on one episode, the Bonus Army above all, should be asked to explain a margin of this size with it. The plainer reading is the reading's own: voters in a country with about one worker in four out of work were not voting on a theory. The inauguration, however, was still four months away under the Constitution of the day, and those four months became the worst winter of the Depression. That winter has its own vocabulary word, and it is the last section of the lesson.",
     kick='F · The election of 1932')

# ------------------------------------------------- 21 SECTION G DIVIDER
divider_photo('bank-port.jpg', 'Section G', 'The Interregnum',
              ['A crowd outside a Michigan bank,', 'February 1933.'],
              "The photograph shows a crowd outside a bank during the Michigan banking crisis of February 1933; Michigan's governor had closed the state's banks that month in an effort to stop the runs, and other states were following. The photographer is not credited in the holding record. Section G covers the four months between the election and the inauguration, and it is the bleakest section of the lesson because its subject is a failure of the calendar as much as of any man. The outgoing president had been repudiated and could not command the country. The incoming president had been elected and could not yet govern. Between them, responsibility for a deepening banking collapse belonged to both and therefore, in practice, to neither. Students should learn the word for the period precisely, because the unit test uses it, and they should understand why the country later changed its Constitution to shorten the gap.",
              title_size=40)

# ------------------------------------------------------ 22 NEITHER ACTED
content_text('Two presidents, and the banks closing',
             ['Hoover urged joint statements to steady the banks',
              'He asked commitments on the budget',
              'Roosevelt refused to bind himself before taking office',
              'Governors closed banks, state by state',
              'By inauguration morning, the system had shut down'],
             "In the guided notes definition, the interregnum is the period between Roosevelt's election in November 1932 and his inauguration in March 1933, when the outgoing and incoming presidents shared responsibility for a deepening crisis and neither acted decisively. Present both men's positions fairly, because each had an argument. Hoover wanted Roosevelt to join in public statements that would steady the banks and to commit the incoming administration to a balanced budget, which would have made the new president a partner in the old one's policies before he held any power. Roosevelt refused to bind himself before taking office, or to share responsibility for decisions he could not control, which preserved his freedom and left the crisis unowned. Meanwhile the banking system failed in the open: governor after governor closed the banks of a state to stop runs, until by inauguration morning the banking system of the United States had effectively shut down. The emergency Roosevelt inherited is the next lesson's starting point.",
             kick='G · The interregnum', size=24)

# ------------------------------------------------------ 23 INTERREGNUM STAT
stat('4 months', 'between the election and the inauguration of 1932 to 1933',
     'November to March, under the Constitution of the day · The inauguration later moved to January',
     "The figure on this slide is a length of time, and it did more damage than most laws in this unit. Four months separated Roosevelt's election in November 1932 from his inauguration in March 1933, because the Constitution of the day set the presidential term to begin on March 4. In an ordinary transition, four months is a courtesy. In the winter of 1932 to 1933 it was a vacuum at the center of a banking collapse, and the collapse filled it: bank closings spread from state to state until the system shut down entirely. The country drew the institutional conclusion afterward. The Twentieth Amendment, ratified in 1933, moved the inauguration to January, shortening every future transition, which is why modern presidents take office about ten weeks after election day. Students should connect the amendment to the winter without being told to: it is the Constitution recording the lesson of the interregnum in its own text.",
     kick='G · The interregnum')

# ------------------------------------------------------ 24 GLANCE
s = slide(NAVY)
kicker(s, "Hoover's program at a glance")
text(s, 0.9, 1.28, 11.5, 1.0, 'Beliefs, actions, limits, verdict', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Beliefs', 'Rugged individualism; voluntarism', 'Relief kept local and voluntary'),
        ('Actions', 'Farm Board, works, tariff, RFC, relief loans', 'A real record, mostly loans and pledges'),
        ('Limits', 'Pledges broke; lending pooled at the top', 'Funds fell as the need rose'),
        ('Verdict', '57 percent against; banks closed all winter', 'The country answered in November')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, Hoover's Program at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The four rows are the lesson's argument in order. Beliefs covers rugged individualism and voluntarism, the design that kept relief local and voluntary. Actions covers the record the caricature leaves out: the Farm Board, public works, the tariff, the RFC, and the relief loans of July 1932. Limits covers the failures of transmission, pledges breaking, lending pooling at the top, and local funds falling as the need rose. Verdict covers the election figures and the interregnum winter. Grade the table generously on wording and strictly on fairness: an entry that omits the actions, or omits the limits, has missed the lesson, whichever direction it leans.")

# ------------------------------------------------------ 25 VOCAB A
vocab('Words for the program',
      [('voluntarism', "Hoover's policy of meeting the Depression through voluntary cooperation by business, charities, and local government rather than through federal relief programs"),
       ('rugged individualism', "Hoover's belief that Americans should succeed through their own effort and that direct federal relief would weaken character and self reliance"),
       ('Reconstruction Finance Corporation', 'the federal agency created in 1932 that lent public money to banks, railroads, and insurance companies in the hope that stability at the top would restore jobs below'),
       ('public works', 'government funded construction projects such as dams, roads, and public buildings, built to provide jobs as well as lasting structures')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. The first term is voluntarism: Hoover's policy of meeting the Depression through voluntary cooperation by business, charities, and local government rather than through federal relief programs. The second is rugged individualism: Hoover's belief that Americans should succeed through their own effort and that direct federal relief would weaken character and self reliance. Keep the pair straight: individualism is the belief, voluntarism the method built on it. The Reconstruction Finance Corporation: the federal agency created in 1932 that lent public money to banks, railroads, and insurance companies in the hope that stability at the top would restore jobs below. The last term on this slide is public works: government funded construction projects such as dams, roads, and public buildings, built to provide jobs as well as lasting structures.")

# ------------------------------------------------------ 26 VOCAB B
vocab('Words for the limits',
      [('Hawley-Smoot Tariff', "the 1930 law that raised United States tariffs to the highest level in the country's history, and drew retaliation that cut world trade"),
       ('Bonus Army', 'the veterans of the First World War who camped in Washington in the summer of 1932 demanding early payment of their promised service bonus, and were driven out by federal troops'),
       ('interregnum', "the period between Roosevelt's election in November 1932 and his inauguration in March 1933, when the outgoing and incoming presidents shared responsibility for a deepening crisis and neither acted decisively")],
      "Three more terms, again matching the guided notes exactly. The Hawley-Smoot Tariff: the 1930 law that raised United States tariffs to the highest level in the country's history, and drew retaliation that cut world trade. Retaliation is the load bearing word; the tariff's damage came home through it. The Bonus Army: the veterans of the First World War who camped in Washington in the summer of 1932 demanding early payment of their promised service bonus, and were driven out by federal troops. Note that the definition ends with the clearing, because the clearing is what the country remembered. The last term is interregnum: the period between Roosevelt's election in November 1932 and his inauguration in March 1933, when the outgoing and incoming presidents shared responsibility for a deepening crisis and neither acted decisively. Students should hear the judgment inside that definition: shared responsibility, decisive action from neither.")

# ------------------------------------------------------ 27 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['What did President Hoover do about the Depression, and why did his program fall short of the collapse? State the record fairly, then measure it.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Voluntarism Test: a 1931 relief desk, five cases, and a judgment on the program'),
        ('Notebook', "Notebook page: rebuild Hoover's program at a glance in your own words"),
        ('Quick check', 'The Camp on the Anacostia: voluntarism, the RFC, the Bonus Army, and the interregnum'),
        ('Writing', "Judging Hoover's Program: the lesson question as an essay")]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: why the do nothing description fails, two reasons help stopped at the top, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Voluntarism Test, puts students behind a relief desk in 1931 with five cases drawn from the documents: a laid-off machinist, a failed bank depositor, a drought county, a city relief office out of funds, and a Bonus Army veteran, and asks for each one what the program offered, what it refused, and what happened. The notebook page asks students to rebuild Hoover's program at a glance themselves. The quick check, The Camp on the Anacostia, tests voluntarism, the RFC, the Bonus Army, and the interregnum against the Capitol lawn photograph. The writing task turns the lesson question into an essay that must state the record fairly before judging it. The exit ticket has three parts: why the do nothing description is inaccurate; two reasons help lent at the top did not reach families at the bottom; and the lesson question in two or three sentences with at least two facts. Next lesson opens on inauguration morning, with the banks shut.")

dc.save(OUT)
