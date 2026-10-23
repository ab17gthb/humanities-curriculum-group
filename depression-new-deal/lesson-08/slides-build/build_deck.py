#!/usr/bin/env python3
"""Depression and New Deal Lesson 8 deck, "What the New Deal Changed and
What It Did Not," built to the approved Twenties / Progressive Era pilot
system: image-led slides, fragments only on screen, comprehensive speaker
notes, full lesson and vocabulary coverage. Fonts: Georgia titles, Lato body."""
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
OUT = os.path.join(HERE, '..', 'lesson-08-slides.pptx')

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

# ---------------------------------------------------------------- 1 · TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'THE DEPRESSION AND NEW DEAL · LESSON 8', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'What the New Deal Changed and What It Did Not', size=34, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'The changed country, the unfinished work, and the two measures of judgment', size=17, color=POWDER)
notes(s, "This photograph, by Lewis Hine, shows a Tennessee Valley Authority power shovel at work on a roadway at the Norris Dam site on October 30, 1933, in the New Deal's first year. It is the right opening image for the unit's final lesson because the physical record is one of the two things students must weigh today: what the New Deal built, in concrete and in law, is still standing and still running. The other thing is what it did not do. The Depression was not ended by the New Deal, and the protections it built were not extended to everyone. This lesson teaches students to hold both records in one judgment and to name the measure they are judging by, against the collapse of 1933 or against full recovery and equal treatment. That discipline, naming the measure, is the skill the writing task grades.")

# ------------------------------------------------- 2 · LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("What did the New Deal change for good, what did it leave undone, and how should it be judged?", {})]],
     size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the New Deal change the relationship between Americans and their federal government, and what did it leave undone?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Notice that today's question is nearly the unit question itself, and say so: this lesson is where the whole unit is judged. It has three parts, and the exit ticket requires all three. What did the New Deal change for good: the federal role, the physical record, the political settlement. What did it leave undone: full recovery, which waited for war spending, and equal treatment, which its founding laws withheld from whole groups of Americans. And how should it be judged, which is the part students most want to skip, because a verdict requires choosing a measure. Two measures run through the lesson and through the reading's closing section: against the collapse it answered, and against full recovery and equal treatment. A student may defend either verdict. A student may not decline to have one, or hide the measure the verdict rests on.")

# --------------------------------------------------- 3 · THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'The changed country, then the unfinished work', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'A government present in daily life', 'Deposits insured; stock markets regulated'),
        ('B', 'Security for old age and unemployment', 'Social Security and the safety net'),
        ('C', 'Rights at work, a floor under wages', 'The labor board; the Fair Labor Standards Act, 1938'),
        ('D', 'The physical record', 'Dams, bridges, schools, parks, and airports'),
        ('E', 'The New Deal coalition', 'Five groups, one party, a generation in power'),
        ('F', 'What it did not do', 'Unemployment never below 14 percent; the exclusions'),
        ('G', 'Two measures of judgment', 'Against the collapse, or against full recovery')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "The map follows the guided notes section by section. Sections A through E build the changed country in order: the federal government's new presence in daily life through deposit insurance and securities regulation; the safety net of Social Security; labor rights enforced and a wage floor set in 1938; the physical record of dams and buildings; and the New Deal coalition that held power for a generation. Section F then states the limits as plainly as the record allows: unemployment never below fourteen percent in any year of the decade, full employment only with war spending, and the exclusions, agricultural and domestic workers outside Social Security, segregated camps, redlining, and repatriation. Section G closes with the two measures of judgment. Warn students now that the lesson is built in this order on purpose: the limits are taught after the achievements, at full strength, and neither half is a footnote to the other.")

# ------------------------------------------------- 4 · SECTION A DIVIDER
divider_photo('signing-port.jpg', 'Section A', 'A Government Present in Daily Life',
              ['Standing rules, run by standing agencies.', 'Not emergency measures for one season.'],
              "The photograph shows President Roosevelt signing the Social Security Act on August 14, 1935, with members of Congress standing behind him; the signing belongs to section B, and it opens this section because it is the era's emblem of the larger change treated first: a federal government that stayed. Make the contrast with 1933 concrete for students. The emergency agencies of the Hundred Days were built to be temporary, and some, like the Civil Works Administration, were shut within months. The agencies of this section were built the other way, as permanent parts of the state: a deposit insurance corporation, a securities regulator, and behind them a new expectation that the national government stood inside economic life, guaranteeing, policing, and paying, as a normal condition rather than a crisis exception. Sections A and B together cover that settlement; section A takes the two regulators of money itself.",
              title_size=36)

# ------------------------------------------------------ 5 · TWO GUARANTEES
content_text('Two guarantees over money',
             ['FDIC, 1933: bank deposits insured by the federal government',
              'A failed bank no longer wiped out a family\u2019s savings',
              'SEC, 1934: stock markets regulated, honest reporting required',
              'Companies selling stock answer for their published figures',
              'Both still operate, a lifetime after the emergency'],
             "Teach the two agencies as a pair, because a working family met them as a pair: one guarded what the family saved, the other policed what the family might buy. The guided notes definitions, in full. The Federal Deposit Insurance Corporation: the federal agency created in 1933 that insures bank deposits, so that depositors are repaid by the government if their bank fails. Deposit insurance ended the bank run as a rational act: with the guarantee behind the deposit, a rumor no longer required a run to the teller. The Securities and Exchange Commission: the federal agency created in 1934 to regulate the stock markets and require honest public reporting by companies selling stock. Its weapon was disclosure: a company could sell risky stock, but not on false figures. Students should register the common form: in both cases the government did not take over the business; it set the floor of honesty and solvency beneath it, permanently.",
             kick='A · A government present in daily life', size=24)

# ------------------------------------------------- 6 · SECTION B DIVIDER
divider_text('Section B', 'Security for Old Age and Unemployment',
             'The largest piece of the new presence, and the start of the safety net.',
             "If deposit insurance is the New Deal's quietest permanence, Social Security is its largest. Set out what the Act of August 1935 actually built, because students often shrink it to a pension: old-age insurance for retired workers, funded by payroll taxes on workers and employers; unemployment insurance run jointly with the states; and aid to dependent children and other vulnerable groups. Then name the principle, which the reading states and the guided notes test. Before 1935, old age without savings, or a lost job in a slack season, was a private misfortune met by family, charity, or the county poor farm. After 1935, the federal government accepted these as standing risks of a working life and insured against them as a matter of law. That acceptance, more than any single benefit check, is the change in the relationship between Americans and their government that the unit question asks about. The exclusions written into the Act belong to section F; here, build the structure first.")

# ------------------------------------------------------ 7 · THE SAFETY NET
content_text('The safety net',
             ['Old-age insurance: a monthly benefit at retirement',
              'Unemployment insurance: pay between jobs, run with the states',
              'Aid to dependent children and other vulnerable people',
              'Funded by payroll taxes, earned as a right of work',
              'A net with edges: some stood outside it from the start'],
             "Read the guided notes definition aloud, because it is the term in its most useful form: a safety net is the set of government programs that catch people who fall into poverty through old age, unemployment, disability, or the loss of a family earner. Note the four falls the definition names: old age, unemployment, disability, and the loss of a family earner, and have students match each to a program from the lesson before it: old-age insurance, unemployment insurance, and aid to dependent children. The funding deserves one clear sentence: the net was paid for by payroll taxes, contributions from wages and employers, which is why its benefits were understood as earned, a right of work rather than a gift of relief, and why they proved politically durable when relief programs were repealed. End on the definition's limit, stated in the reading and developed in section F: a net has edges, and in 1935 the edges were drawn so that agricultural and domestic workers fell outside them.",
             kick='B · Security for old age and unemployment', size=24)

# ------------------------------------------------------ 8 · A CARD IN EVERY WALLET
content_text('A card in every wallet',
             ['Workers registered for Social Security numbers from 1936',
              'The wage record followed the worker, job to job',
              'Monthly benefits began in 1940',
              'The number became a piece of American identity',
              'An unemployed worker of 1939 carried his number tattooed on his arm'],
             "This slide makes the abstraction physical, and it previews the quick check. From late 1936, workers across the country registered for Social Security numbers, tens of millions of them, in one of the largest administrative undertakings the federal government had ever attempted; employers reported wages against those numbers, and the worker's benefit account followed him from job to job for life. Monthly benefits began in 1940. The quick check photograph, by Dorothea Lange in Oregon in August 1939, shows an unemployed lumber worker with his Social Security number tattooed on his arm, and students should be asked what the tattoo proves before they are told: a man tattoos a number on his skin only if he expects the number, and the program behind it, to be permanent and valuable for the rest of his life. The same photograph shows the decade's other truth, a man still migrant and unemployed in 1939, which is section F arriving early; let students notice it and hold the thought.",
             kick='B · Security for old age and unemployment', size=24)

# ------------------------------------------------- 9 · SECTION C DIVIDER
divider_text('Section C', 'Rights at Work and a Floor Under Wages',
             'The board behind the union, and a national minimum beneath the wage.',
             "Section C joins the two labor settlements of the unit: the right to organize, taught in the last two lessons, and the wage and hour floor, which arrives here because its law is the New Deal's last. The Wagner Act's labor board had been enforcing workers' choice of a union since 1935, and the Supreme Court secured it in April 1937; by 1938 the right to organize was a standing fact of industrial life. What workers could not yet claim was any national standard for the wage itself or the length of the week. The Fair Labor Standards Act of June 1938 supplied it, and it is the right closing statute for the New Deal's legislative record: minimum wage, overtime, and child labor limits, set in Washington for the whole country. Teach the section as the completion of a structure: the Act of 1935 protected the worker's organization; the Act of 1938 protected the worker's pay envelope.")

# ------------------------------------------------------ 10 · 25 CENTS STAT
stat('25 cents', 'the first federal minimum wage, set by the Fair Labor Standards Act of 1938',
     'Overtime pay required past forty hours a week · Child labor restricted · The last major law of the New Deal',
     "Put the figure in a worker's terms before judging it. Twenty-five cents an hour, for a forty hour week, is ten dollars a week, in a decade when millions had worked for less or not at all; the Act scheduled the minimum to rise to forty cents within seven years. The guided notes definition, in full: the Fair Labor Standards Act, the 1938 law that set a federal minimum wage, required overtime pay past forty hours a week, and restricted child labor. Each of its three provisions reversed an older settlement: the wage had been set by each employer's market, the week had run past sixty hours in many trades, and children had worked in mills and canneries within living memory. Note also what the Act excluded, because it previews section F: farm labor and domestic service were left outside the wage floor too, so the same exclusions that mark Social Security mark the New Deal's final statute.",
     kick='C · Rights at work')

# ------------------------------------------------------ 11 · THE BOARD BEHIND THE RIGHT
content_text('The board behind the right',
             ['The labor board ran union elections and policed coercion',
             'Employers bound to bargain with the workers\u2019 chosen union',
             'The Supreme Court secured the Act in April 1937',
             'By 1939: nine million union members stood behind the settlement',
             'Rights at work had become a standing part of the federal role'],
             "This slide closes section C by following the enforcement, because a right with a board behind it is a different thing from a right in a speech. The National Labor Relations Board conducted representation elections, investigated charges that employers had fired or spied on union members, and ordered remedies; after the Supreme Court upheld the Wagner Act in April 1937, in the Jones and Laughlin case from the last lesson, compliance spread through industries that had sworn never to bargain. The membership figure belongs here rather than in the last lesson's notes alone: from under three million members in 1933 toward nine million by the end of the decade. Connect that growth to the coalition of the next sections: organized labor was no longer a pressure group outside politics but a constituency inside the governing party, and its presence in the New Deal coalition is one reason the settlement survived its maker. Students should leave the section able to say what the federal government did at work by 1939: it insured the election, enforced the contract table, and set the floor under the wage.",
             kick='C · Rights at work', size=24)

# ------------------------------------------------- 12 · SECTION D DIVIDER
divider_photo('norris-port.jpg', 'Section D', 'The Physical Record',
              ['Dams, bridges, schools, parks, and airports,', 'in daily use for generations.'],
              "The photograph is Lewis Hine's power shovel at the Norris Dam site in October 1933, the same image as the title slide in a portrait crop, and it introduces the most durable evidence in the lesson: the built country. Relief checks were spent and gone; a dam is an argument that renews itself every year it stands. Teach the inventory wide, because students underrate its range: the great river dams, Norris and Grand Coulee and Boulder among them; electrification carried into farm country; bridges, schools, courthouses, post offices, and airports in nearly every county in the nation; roads paved; park lodges and trails built by the CCC and the WPA's workers. The Tennessee Valley Authority is the type case: one federal corporation remaking a whole river region's floods, power, and fertilizer. The verdict relevance comes at the end of the section and in the activity's second file: construction spending is the one kind of Depression expenditure whose return is still being collected.",
              title_size=40)

# ------------------------------------------------------ 13 · WHAT THE TRAVELER OF 1940 USED
content_text('What the traveler of 1940 used',
             ['River dams on the Tennessee, the Columbia, the Colorado',
              'Power lines into farm country private companies had passed over',
              'Bridges, schools, courthouses, and airports in every region',
              'Park trails and lodges built by relief workers',
              'The structures outlasted the arguments that built them'],
             "Run the inventory as a journey, following the reading. A traveler crossing the United States in 1940 drove on roads the New Deal's programs had paved, crossed bridges they had built, landed at airports they had laid out, passed schools and courthouses they had raised in towns that could not have bonded them in 1933, and at night saw farmhouses lit by power lines the rural electrification program had strung into country the private utilities had judged unprofitable. The Tennessee Valley Authority's dams held back the Tennessee River's floods and sold current at rates the private companies then had to meet. Two teaching points. First, scale: this was not a scattering of monuments but a national building program carried out as relief, employing millions, which is why its remains are everywhere rather than somewhere. Second, judgment: in the activity's Verdict Brief, the physical record is the file that weighs by time, since every decade of use adds to the return on money spent in the worst years of the century.",
             kick='D · The physical record', size=24)

# ------------------------------------------------- 14 · SECTION E DIVIDER
divider_text('Section E', 'The New Deal Coalition',
             'The settlement had a political foundation, and the foundation lasted a generation.',
             "Every structure in sections A through D rested on votes, and this section names them. Roosevelt's achievement as a politician was not only winning in 1932 but assembling a majority broad enough to govern through the decade and beyond it: the New Deal coalition. Teach the coalition as a bargain among groups that agreed on little except the party that delivered to them. White southerners supplied the congressional seniority that chaired the committees. Northern city voters supplied the electoral votes of the great states. Union members, newly organized by the millions, supplied organization and turnout. Farmers supplied the heartland. And Black voters in the northern cities, heirs of the party of Lincoln, moved toward the Democrats in this decade and stayed. The bargain had a price, and the price was charged to Black southerners, who remained disfranchised inside the coalition's own stronghold. Name that here, before section F, so students meet the exclusions as a cost of the settlement and not as an unrelated scandal.")

# ------------------------------------------------------ 15 · FIVE GROUPS, ONE PARTY
content_text('Five groups, one party',
             ['White southerners: committee power in Congress',
              'Northern city voters: the great states\u2019 electoral votes',
              'Union members: organization, turnout, and members by the million',
              'Farmers: supports for prices and credit',
              'Black voters in the North: moving toward the Democratic Party'],
             "Work the list as the guided notes definition gives it, in full: the New Deal coalition, the alliance of white southerners, northern city voters, union members, farmers, and increasingly Black voters that kept the Democratic Party in national power for a generation after 1932. A generation is the operative measure: five straight presidential elections, from 1932 through 1948, and congressional majorities that long outlasted Roosevelt himself. Ask students to identify what each group received, because delivery is what held an alliance of groups with opposed interests together: farm supports and rural power for the farmers and the South; labor rights and relief for the cities and the unions; growing federal attention for Black northern voters. Then put the contradiction plainly, because it is the coalition's central fact: the same alliance included the white South, whose price was federal restraint toward segregation and disfranchisement. The exclusions of section F were not accidents that befell the settlement from outside; several of them were terms on which the coalition itself was held together.",
             kick='E · The New Deal coalition', size=24)

# ------------------------------------------------- 16 · SECTION F DIVIDER
divider_photo('lange-port.jpg', 'Section F', 'What It Did Not Do',
              ['Unemployment never below fourteen percent.', 'The protections did not reach everyone.'],
              "The photograph is Dorothea Lange's unemployed lumber worker of August 1939, the quick check image, shown here first so its argument can frame the section: in the decade's last summer, ten years after the crash, a skilled woods worker was still following the bean harvest out of a migrant camp, with his Social Security number tattooed on his arm. Permanence and insufficiency stand in the same frame, which is section F in one image. State the section's two charges in order and without softening either. The recovery charge is numerical: unemployment never fell below fourteen percent in any year of the 1930s, and full employment arrived only with war spending. The treatment charge is documentary: the settlement's exclusions were written into its founding laws, its camp rosters, its housing maps, and its removal drives, and they fell on identifiable Americans by name and category. Students who want to acquit the New Deal must answer this section, not skip it.",
              title_size=38)

# ------------------------------------------------------ 17 · 14 PERCENT STAT
stat('14 percent', 'the lowest unemployment reached in any year of the 1930s, in 1937',
     'About 25 percent in 1933 · About 19 percent again in 1938 · Full employment only with war spending in the 1940s',
     "This is the single most important number in the lesson, and it should be taught as a boundary, not a detail. Unemployment fell impressively from its depth, about twenty-five percent in 1933, and students should credit the fall. But in the best year of the decade, 1937, it reached only about fourteen percent, roughly one worker in seven still idle in the eighth year of the emergency, and the recession then drove it back toward nineteen percent. In 1939 it stood near seventeen percent. Full employment, the condition in which anyone seeking work can find it, arrived in the 1940s, and it arrived on war spending: the federal government finally spent at the scale the slump had required all along, building an army and a war economy. The conclusion students must be able to state without prompting is the unit's boundary line: the New Deal relieved, reformed, and partially recovered the country, and the war, not the New Deal, ended the Great Depression. The World War II unit owns the mobilization itself.",
     kick='F · What it did not do')

# ------------------------------------------------------ 18 · THE EXCLUSIONS WRITTEN IN
content_text('The exclusions written in',
             ['Social Security, 1935: agricultural and domestic workers left out',
             'The exclusion fell hardest on Black workers and on women',
             'CCC camps segregated; relief uneven under local control',
             'The same exclusions marked the wage law of 1938',
             'Written into the laws at the time, not discovered later'],
             "Teach the exclusions as design, because the activity's fourth file asks students to prove design from evidence, and the habit is the lesson's discipline. The Social Security Act's omission of agricultural and domestic workers was a provision of the statute, affecting a majority of Black workers in the South and a large share of working women, and historians have long connected it to the southern committee chairmen whose votes the bill required. The Civilian Conservation Corps enrolled its young men in segregated camps as a matter of administration. Relief run through local officials varied with local prejudice, generous in one county and grudging in the next. The Fair Labor Standards Act repeated the pattern in 1938, leaving farm and domestic workers outside the wage floor. The point to fix is the one the reading makes in its last sentence on the subject: the lines the new state drew around its protections were drawn deliberately, by identifiable men, for identifiable reasons of coalition and prejudice, and the Americans outside the lines knew it at the time.",
             kick='F · What it did not do', size=24)

# ------------------------------------------------------ 19 · REDLINING ON THE MAP
content_photo('holc-port.jpg', 'Redlining, and removal',
             ['Federal housing maps graded neighborhoods by race',
             'Minority districts marked risky; loans denied there',
             'White buyers built equity; Black buyers were kept out',
             'Repatriation removed people of Mexican descent to Mexico',
             'Many removed were United States citizens'],
             "The image is a federal housing security map of 1937, from the records of the Federal Home Loan Bank Board at the National Archives: the instrument itself, a city divided into graded zones by federal appraisers. The guided notes definitions, in full. Redlining: the practice by which federal housing officials and lenders marked minority neighborhoods as risky on maps and denied loans there, keeping Black families from buying homes on equal terms. The consequence ran for generations, because the home was the ordinary family's one road to equity: denied the federally backed loan in the 1930s and 1940s, Black families were denied the asset whose appreciation financed the white suburbs. Repatriation: the removal of people of Mexican descent, including many United States citizens, to Mexico during the Depression, carried out by local and federal authorities under economic pressure. Raids, coerced departures, and county relief offices that paid for one way tickets south did the work, and the fear of the drive emptied neighborhoods far beyond those actually removed.",
             kick='F · What it did not do')

# ------------------------------------------------------ 20 · REMOVED UNDER PRESSURE
content_text('Removed under pressure',
             ['Early 1930s: jobs scarce, and scapegoats sought',
             'Local raids and county drives pushed families south',
             'Citizens of the United States among the removed',
             'Estimates of the removed run into the hundreds of thousands',
             'The new state of sections A to E was not built for them'],
             "Give repatriation its own slide, because it is the exclusion students know least and the one that most tests the lesson's argument about who the new state was for. In the early Depression years, as unemployment climbed, people of Mexican descent, immigrants and citizens alike, were pressed to leave: workplace raids in Los Angeles and other cities, county programs that chartered trains and paid fares on condition the riders not return, and relief denied to families who stayed. Large numbers of those removed were United States citizens, many of them children born in this country, carried to a Mexico they had never seen. Estimates of the total removed run into the hundreds of thousands; the surviving records do not support a single exact figure, and students should be taught to say so rather than to memorize one. The placement of this fact shapes the verdict: it happened mostly before 1933, under Hoover and local authorities, and the New Deal did not organize it; but the New Deal's settlement, which distributed protection by category and place, left the removed and their descendants outside its account as well.",
             kick='F · What it did not do', size=24)

# ------------------------------------------------- 21 · SECTION G DIVIDER
divider_text('Section G', 'Two Measures of Judgment',
             'The verdict changes with the measure. Name the measure.',
             "Close the teaching where the reading closes, with judgment itself as the subject. Two measures have been available all lesson, and students have been using both without naming them. The first measures the New Deal against the collapse it answered: the banks of 1933, the unemployment of 1933, the helplessness of the federal government of 1933. Against that measure the record of sections A through E is overwhelming: stabilization, millions at work, permanent protections, a built country. The second measures it against full recovery and equal treatment: a normally working economy and protections extended to all Americans. Against that measure, the record of section F is decisive the other way. Neither measure is dishonest, and the choice between them is the actual content of a century of argument about the New Deal. What the lesson forbids is the unmeasured verdict, the praise or condemnation that never says what standard it is applying. The next two slides run each measure at full strength, in order.")

# ------------------------------------------------------ 22 · MEASURED AGAINST THE COLLAPSE
content_text('Measured against the collapse',
             ['1933: banks failing, a quarter of workers idle',
             'The banking system stabilized and deposits insured',
             'Millions put to work; a physical country built',
             'Permanent protections written into law',
             'A governing coalition that lasted a generation'],
             "Run the favorable measure at its strongest, because students must be able to state it before they are asked to answer it. In March 1933 the banking system was shut, a quarter of the labor force was idle, farm prices had halved, and the federal government possessed neither the machinery nor the accepted duty to answer any of it. By 1939 the banks were stable and their deposits insured by the federal government; the securities markets were policed; millions had been put to work, and their work stood in dams, schools, and parks; old age and unemployment had become insured risks; labor rights were enforced and a floor stood under wages; and the political coalition behind the settlement had won five straight presidential elections and would shape the country for a generation. Measured against where the country stood when Roosevelt took the oath, the New Deal was the largest act of relief, recovery, and reform the nation had ever attempted, and most of its structure is still in place. That is the case. The next slide is the other case, and it is also true.",
             kick='G · Two measures of judgment', size=24)

# ------------------------------------------------------ 23 · MEASURED AGAINST FULL RECOVERY
content_text('Measured against full recovery',
             ['Unemployment at or above 14 percent in every year of the decade',
             'The recession of 1937 to 1938 inside the recovery',
             'Full employment arrived only with war spending',
             'The exclusions: written into laws, rosters, and maps',
             'On this measure, the New Deal stopped short'],
             "Now run the second measure at full strength. The New Deal's own stated work was recovery, and by the plainest test it was not achieved: unemployment never fell below about fourteen percent in any year of the 1930s, the administration's own fiscal turn in 1937 produced a recession inside the recovery, and the economy did not reach full employment until the federal government spent on war at the scale the Depression had always required. The second count is equal treatment. The settlement protected Americans by category and drew its categories so that agricultural and domestic workers, Black southerners under segregation, Black home buyers facing redlined maps, and families of Mexican descent under repatriation pressure stood outside or beneath the protections their neighbors received. A student who adopts this measure and judges the New Deal a partial, bounded achievement that stopped short of its promise has read the evidence correctly; so has the student on the other measure. The writing task grades the naming of the measure and the answering of the other side, not the verdict chosen.",
             kick='G · Two measures of judgment', size=24)

# ------------------------------------------------------ 24 · AT A GLANCE
s = slide(NAVY)
kicker(s, 'The account at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Changed, built, held, undone', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Changed', 'FDIC, SEC, Social Security, labor rights, the wage floor', 'A permanent federal presence in economic life'),
        ('Built', 'Dams, bridges, schools, parks, and airports', 'Construction still in daily use generations later'),
        ('Held', 'The New Deal coalition, five straight elections', 'National power for a generation after 1932'),
        ('Undone', 'Unemployment never below 14 percent; the exclusions', 'Recovery waited for war; protection was not equal')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.2, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.25, yy + 0.05, 5.1, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.55, yy + 0.05, 3.9, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the closing table of the guided notes, The Account at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. Changed: the federal role, deposit insurance from 1933, securities regulation from 1934, Social Security from 1935, enforced labor rights, and the wage and hour floor of 1938, a permanent presence where ten years earlier there had been almost none. Built: the physical record, dams on three great rivers and buildings in every county, still in daily use. Held: the political settlement, the New Deal coalition in national power for a generation. Undone: two entries, recovery, with unemployment never below fourteen percent in any year of the decade and full employment reserved to war spending; and equal treatment, with the exclusions of the founding laws, the segregated camps, the redlined maps, and repatriation. Grade the table on the presence of both undone entries: a table with only the recovery entry has missed half of section F.")

# ------------------------------------------------------ 25 · VOCAB A
vocab('Words for the settlement',
      [('New Deal coalition', 'white southerners, city voters, unions, farmers, and increasingly Black voters'),
       ('Fair Labor Standards Act', 'the 1938 law: a minimum wage, overtime past forty hours, child labor restricted'),
       ('safety net', 'the programs that catch people who fall into poverty'),
       ('redlining', 'marking minority neighborhoods as risky on maps and denying loans there')],
      "These definitions match the guided notes, and the notes carry them in full, word for word. The New Deal coalition: the alliance of white southerners, northern city voters, union members, farmers, and increasingly Black voters that kept the Democratic Party in national power for a generation after 1932. The Fair Labor Standards Act: the 1938 law that set a federal minimum wage, required overtime pay past forty hours a week, and restricted child labor. A safety net: the set of government programs that catch people who fall into poverty through old age, unemployment, disability, or the loss of a family earner. Redlining: the practice by which federal housing officials and lenders marked minority neighborhoods as risky on maps and denied loans there, keeping Black families from buying homes on equal terms. Notice for students that this set holds the settlement and its shadow together: two terms for the coalition and its laws, one for the protection, and one for the exclusion, which is the shape of the whole lesson in four lines.")

# ------------------------------------------------------ 26 · VOCAB B
vocab('Words for the record and the removal',
      [('repatriation', 'the removal of people of Mexican descent, including many citizens, to Mexico'),
       ('Securities and Exchange Commission', 'the agency of 1934 that regulates the stock markets'),
       ('Federal Deposit Insurance Corporation', 'the agency of 1933 that insures bank deposits')],
      "Three more terms, in the guided notes wording, carried in these notes in full. Repatriation: the removal of people of Mexican descent, including many United States citizens, to Mexico during the Depression, carried out by local and federal authorities under economic pressure. The Securities and Exchange Commission: the federal agency created in 1934 to regulate the stock markets and require honest public reporting by companies selling stock. The Federal Deposit Insurance Corporation: the federal agency created in 1933 that insures bank deposits, so that depositors are repaid by the government if their bank fails. Pair the two agencies for memory, as the lesson taught them: 1933 insured what a family saved, 1934 policed what a company sold. And have students state the repatriation definition's hardest phrase aloud, including many United States citizens, because the verdict in the writing task depends on not losing it.")

# ------------------------------------------------------ 27 · CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ["What did the New Deal change for good, what did it leave undone, and how should it be judged? Name your measure before you give your verdict."],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Verdict Brief: the changed state, the physical record, the recovery numbers, the exclusions'),
        ('Notebook', 'Notebook page: the account in chart form, with your measure named'),
        ('Quick check', 'The Number on His Arm: Lange\u2019s lumber worker, the two agencies, the exclusions'),
        ('Writing', 'The Verdict: the lesson and unit questions as an essay, with the TPSP DBQ as its linked extension')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: one permanent change with its law, the recovery fact, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close the unit by handing the judgment to the students, which is what this lesson exists to do. The activity, The Verdict Brief, sorts the unit's evidence into four files, the changed state, the physical record, the recovery numbers, and the exclusions, and requires a one page brief with a claim, three pieces of evidence from three files, and the strongest counterargument stated and answered. The notebook page asks for the account in chart form. The quick check, The Number on His Arm, reads Dorothea Lange's 1939 photograph of the unemployed lumber worker and tests the two financial agencies and the exclusions. The writing task, The Verdict, takes up the lesson and unit questions; teachers may extend or replace it with The Primary Source Project premium DBQ 5, Did the New Deal end the Great Depression, DBQ180, which is a linked resource and not part of this folder's plate. The exit ticket has three parts: one permanent change with its agency or law, the strongest single recovery fact, and the lesson question answered with one fact from each side. The review day and the unit test follow from here.")

dc.save(OUT)
