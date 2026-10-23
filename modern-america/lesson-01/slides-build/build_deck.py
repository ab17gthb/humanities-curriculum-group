#!/usr/bin/env python3
"""Modern America Lesson 1 deck, "The Conservative Turn: Stagflation and the Tax Revolt,"
built to the approved system: image-led slides, fragments only on screen,
comprehensive speaker notes, full lesson + vocabulary coverage.
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
OUT = os.path.join(HERE, '..', 'lesson-01-slides.pptx')

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
text(s, 0.9, 5.32, 11.5, 0.4, 'MODERN AMERICA · LESSON 1', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Conservative Turn: Stagflation and the Tax Revolt', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Why the postwar settlement broke down in the 1970s, and who organized what replaced it', size=17, color=POWDER)
notes(s, "The photograph shows cars lined up at a gasoline station on June 15, 1979, photographed by Warren K. Leffler and held by the Library of Congress. Hold the image in front of students before any content. A country built on cheap gasoline and the open road is standing still in line for fuel, in the second energy shock of one decade. This lesson explains how the country got into that line. It begins with the settlement Americans had expected after 1945, counts the breakdown in the government's own figures, follows the trust crisis that ran beside the economics, reads the two diagnoses offered by 1979, and ends with the coalition organized to replace the settlement, assembled in time for the election of 1980.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('Why did the postwar economic settlement break down in the 1970s, and who organized the politics that replaced it?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the United States remake itself after 1980, in its economy, its population, and its place in the world, and what did the remaking settle and what did it leave open?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question has two halves, and students should hear both verbs before the lesson begins. Broke down asks about causes: what failed, in wages, in energy, and in the government's management of the economy, and what failed beside the economics, in public trust. Organized asks about builders: the politics that replaced the settlement did not assemble itself, and it was not invented in a single campaign. By the end of the hour students should be able to name the tax revolt that proved the new politics at the ballot box in 1978, the New Right machinery of direct mail and single issue groups, and the Moral Majority that carried evangelical voters into elections, and to state the voter arithmetic those builders joined together. The unit question runs beneath this one as the frame for all eight lessons.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'The breakdown and the answer, in seven stretches', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The settlement that was expected', 'Rising wages, cheap energy, managed growth'),
        ('B', 'Stagflation, counted', 'Prices and joblessness high together'),
        ('C', 'Oil as the accelerant', 'The embargo of 1973, Iran in 1979'),
        ('D', 'Trust broken', 'Resignation, pardon, Saigon, New York'),
        ('E', 'A crisis of confidence named', "Carter's diagnosis, July 15, 1979"),
        ('F', 'The tax revolt opens', 'Proposition 13, California, June 1978'),
        ('G', 'The coalition assembled', 'New Right, Moral Majority, the hinge of 1980')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Sections A and B state the expectation and its failure in numbers: a settlement of rising wages, cheap energy, and managed growth, answered by stagflation. Section C names the accelerant, the two oil shocks of 1973 and 1979. Section D gives the trust crisis that ran beside the economics: a resignation, a pardon, a lost war's end, and a great city near default. Section E gives the president's diagnosis of 1979. Sections F and G give the organized answer: the tax revolt opened by Proposition 13, and the coalition of the New Right and the Moral Majority that stood ready for 1980. Tell students the summary table at the end of their guided notes asks them to rebuild exactly this map.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', 'The Settlement That Was Expected',
             'Rising wages, cheap energy, and a government expected to manage the economy.',
             "Begin with the expectation, because the breakdown of the 1970s is only measurable against what Americans thought was normal. For the generation after 1945, three facts held together. Wages rose with productivity, so steady work carried families into home ownership and the middle class. Energy was cheap, so gasoline, heating oil, and electricity took a small share of a household budget and rarely entered political argument. And the federal government managed the economy openly, through spending, taxes, and interest rates, with voters of both parties expecting it to keep growth steady and unemployment low. Presidents were judged against that standard, and for a quarter century the country mostly met it. Students should hold the settlement as a set of promises the government made about itself, because the politics of this lesson begins when all three promises failed in the same decade.")

# ------------------------------------------------------ 5 SETTLEMENT
content_text('Three promises the postwar country made to itself',
             ['Wages rose with productivity',
              'Energy was cheap and unargued',
              'Washington managed growth and jobs',
              'Presidents were judged on all three',
              'By the mid 1970s, all three had failed'],
             "Work the fragments as promises rather than as conditions, because that is how voters experienced them. Rising wages were not luck in the postwar telling; they were the system's output, the reward steady work was supposed to produce. Cheap energy was built into the country's design, its suburbs, its highways, and its factories, which is why an oil shock later reached so far into daily life. Managed growth was a claim of competence: the government said it possessed tools that could keep the economy between inflation and unemployment, and both parties governed inside that claim. When the three failed together, the failure was therefore political and not only economic. A voter in 1978 was not simply poorer than expected. She held a broken promise, and she was listening for someone to name who had broken it.",
             kick='A · The settlement that was expected')

# ------------------------------------------------------ 6 INFLATION STAT
stat('13.5%', 'consumer price inflation in 1980, the decade counted by the Bureau of Labor Statistics',
     '6.2 percent in 1973 · 11.0 percent in 1974 · 11.3 percent in 1979 · 13.5 percent in 1980',
     "Let the climb carry the section, because a single bad year can be blamed on weather or war and a decade's climb cannot. Inflation stood at 6.2 percent in 1973, already high by postwar standards, then 11.0 percent in 1974 after the first oil shock. It eased in the middle of the decade, which let officials hope the problem had passed, and then it climbed again through the second shock to 11.3 percent in 1979 and 13.5 percent in 1980, the highest rate in the Bureau of Labor Statistics series for the postwar era. Read the figures for what a household heard in them. A savings account lost ground every year. A wage raise negotiated in January bought less by December. A family business could not price its own work six months ahead. Inflation at this pace is not an abstraction in a textbook. It is a tax no legislature voted for, collected daily, and voters in the late 1970s said so in those words.",
     kick='B · Stagflation, counted')

# ------------------------------------------------- 7 SECTION B DIVIDER
divider_photo('gas-port.jpg', 'Section B', 'Stagflation, Counted',
              ['Cars at a gasoline station,', 'June 15, 1979.'],
              "The photograph shows the line at a gasoline station on June 15, 1979, by Warren K. Leffler, held by the Library of Congress. Section B counts the breakdown, and the photograph holds its daily form: the queue. Stagflation is the lesson's first key term, and students should learn it as a definition with three parts that stand or fall together: stagnant economic growth, high unemployment, and high inflation, afflicting the American economy in the 1970s. The definition's last clause does the analytic work. The combination defied the usual rule that inflation and unemployment moved in opposite directions, which meant the government's standing tools pointed the wrong way: spending to cut unemployment fed prices, and tightening to cut prices cost jobs. A government that had promised to manage the economy was holding instruments that made each half of the problem worse when aimed at the other.")

# ------------------------------------------------------ 8 MECHANICS
content_text('Both halves of the problem, at the same time',
             ['Growth stalled while prices climbed',
              'Unemployment reached 8.5 percent in 1975',
              'Fighting one half worsened the other',
              'The standard economics said it could not happen',
              'The settlement promise failed on its own terms'],
             "Take the mechanics slowly, because the unit test asks for the combination and not for a mood of decline. Unemployment reached 8.5 percent in 1975, the highest rate since the Depression era, and it was still 7.2 percent in 1980. In a normal postwar downturn, prices eased as jobs disappeared, and the government could spend against the joblessness without fearing inflation. In the 1970s the easing never came: prices rose at double digit rates in years when millions were out of work. That is why economists reached for a new word, stagflation, built from stagnation and inflation. The word named an admission. The model inside the settlement, in which the government traded a little inflation for fewer unemployed and called the trade management, no longer described the economy the country actually had.",
             kick='B · Stagflation, counted', size=24)

# ------------------------------------------------------ 9 UNEMPLOYMENT STAT
stat('8.5%', 'unemployment in 1975, the highest rate of the postwar era to that year',
     'Still 7.2 percent in 1980, with inflation at 13.5 percent · Bureau of Labor Statistics annual averages',
     "Pair this figure with the inflation figure two slides back, because the lesson's point lives between them. Unemployment at 8.5 percent in 1975 meant roughly eight million Americans out of work in a country that had promised full employment as a policy goal. The rate fell back in the later 1970s and then rose again to 7.2 percent in 1980, in the same year prices climbed 13.5 percent. Students should practice stating the pair in one sentence, since that sentence is stagflation with its evidence attached: in 1980 the economy delivered double digit inflation and unemployment above seven percent at once. Neither party's postwar program had a ready answer to the pair, and the admitting of that fact, by officials of both parties across the decade, is what opened the political space the second half of this lesson describes.",
     kick='B · Stagflation, counted')

# ------------------------------------------------- 10 SECTION C DIVIDER
divider_text('Section C', 'Oil as the Accelerant',
             'Two shocks, 1973 and 1979, and a dependence stated as a fact of the era.',
             "Section C names what turned a hard decade into a crisis of daily life. The energy crisis, in the lesson's definition, is the shortages and sharp price rises in oil and gasoline that struck the United States in 1973 and again in 1979, when oil-producing states cut exports and revolution in Iran halted production. Note the two different triggers inside one definition, because students habitually merge them. The 1973 shock was a deliberate act of policy: Arab oil producing states cut exports to the United States during a war between Israel and its neighbors, and prices quadrupled. The 1979 shock was a revolution's side effect: Iran's upheaval halted its production and world prices rose sharply again. What the shocks shared was the exposure they revealed. The United States had built its growth on imported oil, and twice in six years the supply could be interrupted from abroad.")

# ------------------------------------------------------ 11 LINES
content_text('The queue at the pump was the crisis made visible',
             ['1973: exports cut, prices quadrupled',
              'Lines formed at gasoline stations',
              '1979: revolution in Iran halted production',
              'Rationing and driving days by plate number',
              'Dependence on imported oil, exposed twice'],
             "Work the section through the household, because the queue is where the decade's geopolitics entered ordinary life. In 1973 and 1974 drivers waited for gasoline that stations might not have, and some stations closed for days. In 1979 the lines returned, longer in the public memory because they came as a second offense: stations rationed sales to a few gallons, and states assigned driving days by the last number of a license plate, odd and even. A president's energy program could be debated in Washington, but the line could not be debated at all; a driver was either in it or watching it. Students should connect the visibility to the politics. Inflation could be argued over as a statistic. The gasoline line was a photograph every voter had personally stood inside, and it made national decline feel like a witnessed fact rather than a claim.",
             kick='C · Oil as the accelerant', size=24)

# ------------------------------------------------- 12 SECTION D DIVIDER
divider_text('Section D', 'Trust Broken',
             'A resignation, a pardon, a war closed in defeat, and a great city near default.',
             "Section D steps back from prices to trust, because the economics alone does not explain the politics that followed. The decade opened with Watergate, and its ending is a document this class reads in the activity: on August 9, 1974, Richard Nixon resigned the presidency in a letter of one sentence. A month later President Ford pardoned him, and the argument over that pardon, whether it closed a wound or placed a president beyond the law, ran for the rest of the decade. In April 1975 Saigon fell, closing the Vietnam account the Cold War unit taught. That autumn New York City came within hours of defaulting on its debts, and the federal government at first refused the loan the city asked for. Each episode carried the same teaching for voters: the institutions claiming competence, the presidency, the war makers, the managers of the largest city, could not deliver what they had promised.")

# ------------------------------------------------------ 13 PARDON
content_photo('ford-port.jpg', 'A pardon granted, and argued over for a decade',
             ['Nixon resigned August 9, 1974',
              'Ford issued Proclamation 4311 a month later',
              'A full, free, and absolute pardon',
              'Ford argued a trial would reopen the wound',
              'Critics charged a president placed beyond the law'],
             "The portrait shows President Gerald Ford in 1974, photographed by David Hume Kennerly, a work of the federal government held by the National Archives. Teach the pardon from its own text, because students read Proclamation 4311 at Station 3 of the activity and should arrive there knowing its logic. Ford granted a full, free, and absolute pardon for all offenses Nixon had committed or may have committed between January 20, 1969 and August 9, 1974. His stated reasoning was about time and tranquility: a trial could not fairly begin for a year or more, and the prospect of it would prolong divisive debate over a man who had already paid the unprecedented penalty of resigning the office. Critics answered that the scandal had been about whether a president stood under the law, and that the pardon answered the question the wrong way. Hold both readings up without settling them; the keys in this lesson grade the reading of the document, and the distrust the argument fed is the historical fact either way.",
             kick='D · Trust broken')

# ------------------------------------------------------ 14 SECTION E DIVIDER
divider_text('Section E', "A President Names a Crisis of Confidence",
             "Carter's address of July 15, 1979, and the answer it drew.",
             "Section E gives the decade its most famous diagnosis, and students read it at Station 1 of the activity. On July 15, 1979, with inflation climbing and the gasoline lines of the second shock still fresh, President Jimmy Carter addressed the country on television. He had spent days at Camp David hearing criticism of his presidency, and the speech he delivered reached past his own record to the country's condition. Carter said the fundamental threat to American democracy was not an attack on civil liberties and not a failure of outward strength, since the nation stood at peace with unmatched economic and military power. The threat was a crisis of confidence, a loss of faith that the future would be better than the past. This section reads that diagnosis closely, including the evidence Carter himself offered for it, before the lesson sets the rival diagnosis beside it.")

# ------------------------------------------------------ 15 CARTER
content_photo('carter-port.jpg', "Carter's diagnosis: the spirit, not the statistics",
             ['A crisis of confidence, striking at the national will',
              'Identity defined by what one owns',
              'Consumption charged against hard work',
              'A majority expecting worse years ahead',
              'Energy offered as a common effort'],
             "The portrait shows President Jimmy Carter in 1977, photographed by the Naval Photographic Center, held by the National Archives. Read Carter's evidence as carefully as his claim. He said a majority of Americans, for the first time in the country's history, believed the next five years would be worse than the past five. He said the productivity of American workers was actually dropping. And he named a cultural turn as the crisis's cause: in a nation proud of hard work, strong families, close-knit communities, and faith in God, too many now worshipped self-indulgence and consumption, so that human identity was no longer defined by what one does, but by what one owns. Students should notice what the diagnosis does not contain. It names no tax rate, no regulation, and no program as the problem. The failure, in Carter's account, sat inside the citizens, and the remedy he offered was a rebuilt confidence and a common national effort on energy.",
             kick='E · A crisis of confidence named')

# ------------------------------------------------------ 16 VOTE STAT
stat('2 of 3', 'Americans did not even vote, in Carter\u2019s count in the 1979 address',
     '\u201cTwo-thirds of our people do not even vote\u201d \u00b7 A symptom of the crisis of confidence, as Carter listed it',
     "Pause on this figure because Carter chose it himself, and it shows what kind of evidence his diagnosis ran on. Two thirds of the people do not even vote, he said, in the same passage that listed falling productivity and falling saving. A president measuring a spiritual crisis reached for civic numbers: citizens who had stopped participating in the democracy he was asking to rally. The figure also carried an irony the next sections expose. While Carter counted the citizens who had withdrawn, organizers on the right were counting the citizens who could be mobilized: taxpayers angry at their assessments, and church members who had never been asked to vote as a bloc. The politics of 1980 was built by the side that treated nonvoting as a resource to be organized rather than only as a symptom to be mourned. Students should carry that contrast into the tax revolt.",
     kick='E · A crisis of confidence named')

# ------------------------------------------------- 17 SECTION F DIVIDER
divider_text('Section F', 'The Tax Revolt Opens',
             "Proposition 13, June 1978: the answer proven at the ballot box.",
             "Section F turns from diagnosis to organization, and it begins a full year before Carter spoke. California property values had risen fast through the 1970s, and because property taxes followed assessed values, tax bills climbed with them, in some cases faster than the incomes of the retired and working homeowners who owed them. Campaigners gathered signatures to put a limit on the ballot itself, and in June 1978 California voters passed Proposition 13 by a wide margin. The tax revolt, as the lesson defines it, is the movement of the late 1970s in which voters demanded lower taxes and limits on government spending, beginning with California's Proposition 13 in 1978 and spreading across the country. Note the sequence students must keep straight: the revolt's first victory predates the Crisis of Confidence speech by thirteen months. The answer was organized before the president finished stating the question.")

# ------------------------------------------------------ 18 PROP 13
content_text('A cap written into a constitution',
             ['Property taxes cut sharply in June 1978',
              'The tax capped at one percent of value',
              'Assessed values limited until a sale',
              'Two thirds votes required for many new taxes',
              'The model carried state to state'],
             "Teach Proposition 13 from the document students read at Station 2, Article XIII A of the California Constitution. Its first section caps the property tax: the maximum amount of any ad valorem tax on real property shall not exceed one percent of the full cash value of the property, collected by the counties. Around that cap the measure rolled assessments back and limited their growth to two percent a year until a property changed hands, and it required two thirds votes of the electorate for many new special taxes. Property tax bills fell by more than half on average. Students should name what kind of victory this was. A legislature can repeal a statute in a bad year; a constitutional cap binds future governments, which is why the tax revolt's leaders treated California as a proof and not only as a prize. The diagnosis inside the document is plain: government revenue, left uncapped, was itself the problem.",
             kick='F · The tax revolt opens', size=24)

# ------------------------------------------------------ 19 ONE PERCENT STAT
stat('1%', 'the cap Proposition 13 wrote on California property taxes',
     'Of the full cash value of the property \u00b7 California Constitution, Article XIII A, Section 1(a)',
     "Let the small number carry the section's argument, the way the reading's large numbers carried the breakdown. One percent is a limit a homeowner could hold in her head while paying a bill, and that portability is part of why the tax revolt spread. The Bureau of Labor Statistics figures in Section B required a table and an explanation; the Proposition 13 figure required neither, and it arrived as a rule already enacted rather than as a promise to be trusted. Students should also state what the cap did over time, since the unit test can ask it: because assessed values could rise only two percent a year until a sale, two neighboring houses of equal market value could owe very different taxes, and local governments across California lost revenue they had planned on, which supporters counted as the discipline intended and critics counted as services cut. The lesson records both counts without settling between them.",
     kick='F · The tax revolt opens')

# ------------------------------------------------- 20 SECTION G DIVIDER
divider_text('Section G', 'The Coalition Assembled',
             'Machinery, a church network, and the voters they joined, with Bakke beside them.',
             "Section G assembles the replacement politics in full. The New Right, in the lesson's definition, is the coalition of conservative activists, organizations, and voters that rose in the 1970s around lower taxes, a stronger military, and resistance to the social changes of the 1960s. Its organizers built the machinery this section names: direct mail lists that raised money from small donors by the millions of letters, single issue groups that scored and pressured officeholders, and research institutes that drafted the program in advance. In 1979 the Reverend Jerry Falwell founded the Moral Majority to mobilize evangelical Christian voters behind conservative candidates and causes, adding church networks to the coalition's reach. Beside the organizing ran the courts: in June 1978, the same month as Proposition 13, the Supreme Court decided Bakke, ending a fixed racial quota in admissions while allowing race as one factor, so the argument over remedy was being refereed even as the new coalition formed.")

# ------------------------------------------------------ 21 MACHINERY
content_text('Built before it was led',
             ['Direct mail raised money at national scale',
              'Single issue groups pressured officeholders',
              'Research institutes drafted the program',
              'The Moral Majority founded in 1979',
              'Evangelical voters carried into elections'],
             "Give each piece of machinery its function, because the writing task asks students to prove organization rather than merely assert enthusiasm. Direct mail solved the money problem: a conservative cause could reach sympathetic households without passing through party committees or television networks, and small checks arrived steadily between elections. Single issue groups solved the pressure problem: an officeholder's votes on taxes, defense, abortion, or gun rights could be scored, published, and campaigned on by an organization devoted to that one question. Research institutes solved the program problem, holding drafted bills and budget studies ready for the day their side governed. The Moral Majority solved the turnout problem for one large constituency, registering and mobilizing evangelical voters through churches. The Equal Rights Amendment fight of the same years taught the same lesson from both sides: its supporters and its organized opponents each built state by state campaigns, and the amendment fell short of ratification inside its seven year clock.",
             kick='G · The coalition assembled', size=24)

# ------------------------------------------------------ 22 ARITHMETIC
content_text('The voters the coalition joined',
             ['Southern strategy voters, courted since Nixon',
              'Suburban taxpayers of the West and North',
              'Evangelical voters, mobilized in 1979',
              'Bakke decided the same month as Proposition 13',
              'The election of 1980 stood as the hinge'],
             "Close the teaching with the arithmetic, because a coalition is a sum and students should be able to add this one. The southern strategy of the Nixon years had sought white southern voters by opposing federal civil rights enforcement, busing, and the pace of change the movement had set, and those voters were now joined by suburban taxpayers whose grievance was the assessment notice rather than the court order, and by evangelical voters entering politics as an organized bloc in 1979. Add the setting: the Supreme Court in Bakke had just shown that the argument over remedy would be refereed case by case, and the old settlement's parties had no answer to stagflation that both halves of their coalitions could accept. The election of 1980 is the hinge of the unit, and the next lesson opens with the government this coalition elected and the program it carried into office.",
             kick='G · The coalition assembled', size=24)

# ------------------------------------------------------ 23 VOCAB A
vocab('Words for the breakdown',
      [('stagflation', 'stagnant growth, high unemployment, high inflation together'),
       ('energy crisis', 'oil and gasoline shortages and price rises, 1973 and 1979'),
       ('tax revolt', 'voters demanding lower taxes and spending limits, from 1978'),
       ('Proposition 13', "California's 1978 cap on property taxes")],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. stagflation: the combination of stagnant economic growth, high unemployment, and high inflation that afflicted the American economy in the 1970s, defying the usual rule that inflation and unemployment moved in opposite directions. energy crisis: the shortages and sharp price rises in oil and gasoline that struck the United States in 1973 and again in 1979, when oil-producing states cut exports and revolution in Iran halted production. tax revolt: the movement of the late 1970s in which voters demanded lower taxes and limits on government spending, beginning with California's Proposition 13 in 1978 and spreading across the country. Proposition 13: the California ballot measure of 1978 that cut property taxes sharply and capped their future growth, the opening victory of the national tax revolt.")

# ------------------------------------------------------ 24 VOCAB B
vocab('Words for the coalition',
      [('New Right', 'the conservative coalition built in the 1970s'),
       ('Moral Majority', "Falwell's 1979 organization of evangelical voters"),
       ('southern strategy', "the Nixon era appeal to white southern voters")],
      "Three more terms, again matching the guided notes exactly. New Right: the coalition of conservative activists, organizations, and voters that rose in the 1970s around lower taxes, a stronger military, and resistance to the social changes of the 1960s. Moral Majority: the political organization founded by the Reverend Jerry Falwell in 1979 to mobilize evangelical Christian voters behind conservative candidates and causes. southern strategy: the Republican electoral strategy of the Nixon years that sought white southern voters by opposing federal civil rights enforcement, busing, and the pace of change the movement had set. Students should hold the chain these definitions make when read with the first vocabulary set: a breakdown named by two terms, a revolt named by two more, and a coalition named by three, in the order the decade produced them.")

# ------------------------------------------------------ 25 SYNTHESIS
content_text('Broken down, diagnosed, and answered',
             ['The settlement failed on all three promises',
              'Stagflation defied the standing tools',
              'Trust broke beside the economics',
              'Two diagnoses competed in 1979',
              'The organized one stood ready for 1980'],
             "Close the teaching where the lesson question points, with the whole sequence in one view. The settlement promised rising wages, cheap energy, and managed growth, and by the late 1970s it had delivered stagnant wages against 13.5 percent inflation, gasoline lines in two separate shocks, and unemployment that stayed high beside the prices. Trust broke on the same schedule: a resignation, a pardon argued over for a decade, a war closed in defeat, and a great city near default. Two diagnoses competed to explain the wreck. Carter named a crisis of confidence in the country's spirit; the tax revolt named government itself and proved the naming at the ballot box in June 1978. Behind the second diagnosis stood machinery, direct mail, single issue groups, research institutes, and a Moral Majority founded in 1979, joining southern, suburban, and evangelical voters into one coalition. The election of 1980 rewarded the organized diagnosis, and the next lesson tests what its government did with the victory.",
             kick='G · The coalition assembled')

# ------------------------------------------------------ 26 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Work the diagnosis file', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Why did the postwar economic settlement break down in the 1970s, and who organized the politics that replaced it? Work the five records in order, then judge which diagnosis the election of 1980 rewarded.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Diagnosis File: the Carter passage, Proposition 13, the pardon, the BLS record, and the ERA'),
        ('Notebook', 'Notebook page: six pieces of the story, classified and evidenced'),
        ('Quick check', 'The Diagnosis and the Numbers: the Carter passage against the BLS figures'),
        ('Writing', 'Which Diagnosis Did 1980 Reward?: the two diagnoses of 1979 weighed from the evidence bank')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: stagflation defined in full, Proposition 13 explained as a national politics, and the lesson question answered with one cause and one organization.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Diagnosis File, runs five stations through the evidence: a Crisis of Confidence passage from the audited bank record, the Proposition 13 text from the California Constitution with its assessment rules taught as a labeled summary, a Proclamation 4311 passage, a Bureau of Labor Statistics data record of inflation and unemployment, and the Equal Rights Amendment passage, ending in a verdict on which diagnosis the election of 1980 rewarded. The notebook page asks students to rebuild six pieces of the story with evidence and a classification. The quick check, The Diagnosis and the Numbers, tests the Carter passage against the background figures, tagged to blueprint entries 1 and 2. The writing task weighs the two diagnoses of 1979 from a six item evidence bank. The exit ticket has three parts: stagflation defined with all three parts; Proposition 13 explained as the opening of a national movement; and the lesson question answered with one cause of breakdown and one organization that built the replacement. Next lesson takes up the Reagan program.")

dc.save(OUT)
