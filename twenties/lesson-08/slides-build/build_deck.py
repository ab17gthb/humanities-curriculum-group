#!/usr/bin/env python3
"""The Twenties Lesson 8 deck, "The Weak Spots and the Crash," built to the
approved system mirrored from Gilded Age Lesson 1: image-led slides, fragments
only on screen, comprehensive speaker notes, full lesson + vocabulary coverage.
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
text(s, 0.9, 5.32, 11.5, 0.4, 'THE TWENTIES · LESSON 8', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Weak Spots and the Crash', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Uneven prosperity, borrowed money, and the break in October 1929', size=17, color=POWDER)
notes(s, "The photograph shows the crowd that filled Broad Street outside the New York Stock Exchange on October 29, 1929, the day this lesson ends with. Open by resisting the simple story. The simple story says a rich decade ended in one bad week on Wall Street. This lesson argues something more precise. The prosperity of the 1920s was real, and factory output, cars, radios, and appliances prove it. But it was uneven from the start. Farmers, coal miners, and textile workers spent much of the decade in a depression of their own, ordinary families bought on installment debt, and income at the top flowed into speculation. The market that broke in October 1929 broke over those weak places. Students should leave able to name each weak place with evidence, and to say exactly what broke, in what order, on which days.")

# ------------------------------------------------- 2 · LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('Why was the prosperity of the 1920s uneven from the start, and what exactly broke in October 1929?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the prosperity of the 1920s change American life, and why was that prosperity weaker than it looked?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question has two halves, and students must answer both to earn the lesson. The first half looks backward across the whole decade: why was prosperity uneven from the start, not merely at the end? The evidence runs from farm prices to sick industries to falling union membership to income concentrated at the top. The second half is narrow and factual: what exactly broke in October 1929? That answer is a stock market built on speculation and borrowed money, and it has dates, share counts, and an index number attached to it. The unit question runs beneath as the frame for the whole Twenties unit. Earlier lessons showed how prosperity changed American life. This closing lesson answers why that prosperity was weaker than it looked, and the exit ticket will hold students to the distinction the reading ends on: a crash is not yet a depression.")

# --------------------------------------------------- 3 · THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Weak places first, then the break', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The farm problem', 'Overproduction, low prices, wartime debts all decade'),
        ('B', 'Sick industries', 'Coal and textiles could produce more than buyers wanted'),
        ('C', 'Labor loses ground', 'The open shop drive and welfare capitalism'),
        ('D', 'Paid at the top, borrowed at the bottom', 'Income concentrated, consumption on installment credit'),
        ('E', 'Florida gave the warning', 'A land boom built on resale collapsed in 1926'),
        ('F', 'A market built on borrowed money', 'Speculation and buying on margin'),
        ('G', 'October 1929', 'The break, and what the crash was not')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=21, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.6, yy + 0.06, 5.9, 0.6, d, size=15, color=POWDER)
    yy += 0.62
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Sections A through D are the weak places, and they all date from early in the decade, not from 1929. Farms were depressed from 1921 onward. Coal and textiles were sick industries with too much capacity. Organized labor shrank under employer pressure. Income concentrated at the top while ordinary consumption ran on installment plans. Section E is the rehearsal: the Florida land boom collapsed in 1926 and showed exactly how speculation on credit ends. Section F builds the machine that broke, a stock market lifted by margin loans. Section G runs the five days in October when it broke, and closes with what the crash was not. Tell students the final table in their guided notes, The Weak Places at a Glance, asks them to rebuild this map from memory.")

# ------------------------------------------------- 4 · SECTION A DIVIDER
divider_photo('beltsville-port.jpg', 'Section A', 'The Farm Problem',
              ['A depression on the farm', 'that ran all decade'],
              "The photograph shows farm buildings and fields at Beltsville, Maryland, photographed on August 18, 1924, in the middle of the decade this lesson covers. Say the date plainly, because it carries the argument. This is not a photograph of the Great Depression. It is a prosperous looking American farm in 1924, and by then American farmers had already been in trouble for three years. Section A explains why. Wartime demand had pushed farmers to expand and to borrow, and when the war ended the demand fell away while the expanded production stayed. Hold the scale in view throughout the section: roughly a quarter of the American population still lived on farms in the 1920s, so a farm depression was never only a farm problem. What happened to farm income happened to a quarter of the country's customers.",
              title_size=40)

# ------------------------------------------------------ 5 · THE WARTIME BOOM
content_text('Borrowed to plant every acre',
             ['First World War: government urged farmers to plant every acre',
              'High wartime prices rewarded expansion',
              'Borrowing for land, machinery, and tractors',
              'War ends: European farms recover, demand falls',
              'American production stays high'],
             "Start with the trap, because the farm problem was set by success, not by failure. During the First World War, the government urged farmers to plant every acre, and high prices rewarded them for doing it. Many borrowed to buy land, machinery, and tractors, taking on debts sized for wartime prices. When the war ended, European farms recovered and demand fell, but American production stayed high, because the new acreage and the new tractors did not go away. The result was overproduction. In the guided notes definition, overproduction is production of more of a good than buyers will purchase at prices that cover the cost of producing it. Stress the last clause. Farmers could sell their crops. They could not sell them at prices that covered their costs and their debts. That gap, repeated across a quarter of the population for ten years, is the first weak place in the decade's prosperity.",
             kick='A · The farm problem')

# ------------------------------------------------------ 6 · PRICES AND MCNARY-HAUGEN
content_text('Prices halved, debts did not',
             ['Wheat: about $2.16 a bushel in 1919, about $1.04 in 1929',
              'Farm debts stayed at wartime levels',
              'McNary-Haugen bills: support crop prices at home',
              'Surplus sold abroad at world prices',
              'Passed Congress in 1927 and 1928, vetoed both times'],
             "Put the two wheat figures side by side and do the arithmetic aloud. Wheat averaged about $2.16 a bushel in 1919, fell to about $1.03 in 1921, and stood at about $1.04 in 1929. One disclosure belongs with these numbers: the farm prices in the reading are USDA season averages, rounded, so treat them as reliable guides to the size of the fall, not as a price quoted on any single day. The debt side of the ledger never fell at all; loans taken out at wartime prices stayed at wartime levels. Farm organizations backed the McNary-Haugen bills, which proposed federal support for crop prices at home while surplus crops were sold abroad at world prices. Congress passed the bill in 1927 and again in 1928, and President Calvin Coolidge vetoed it both times. Farmers asked for help for most of a decade and were refused, twice, by veto.",
             kick='A · The farm problem', size=25)

# ------------------------------------------------- 7 · SECTION B DIVIDER
divider_photo('mine-port.jpg', 'Section B', 'Sick Industries: Coal and Textiles',
              ['Too much capacity.', 'Too few buyers.'],
              "The photograph shows miners beside an electric hauling motor and loaded coal cars at the New Black Diamond Mine in Washington, taken about 1927. The machinery is modern, and that is part of the problem this section teaches. Coal was a sick industry not because its mines were backward but because the country had built more mining capacity than its fuel market could support, at the very moment oil and natural gas began taking its customers. Textiles were sick in a different way, and students should keep the two sicknesses separate, because the reading and the test both ask for the difference. In coal, the market itself shrank. In textiles, the market remained but capacity outran it, and production moved toward lower wages. In both industries, owners protected themselves at workers' expense, through closures, wage cuts, and resistance to unions.",
              title_size=36)

# ------------------------------------------------------ 8 · COAL
content_text('Coal lost its customers',
             ['Oil and natural gas took heating customers away',
              'Mines could produce more coal than the country would buy',
              'Operators closed mines and cut wages',
              'Operators fought the miners union',
              'Mine employment fell by about a quarter, 1923 to 1929'],
             "Coal's problem began on the demand side. Oil and natural gas took heating customers away, one boiler and one furnace at a time, while the mines already built could produce more coal than the country would buy. An industry with too much capacity and a shrinking market has few good choices, and operators chose the ones that cost workers most: they closed mines, cut wages, and fought the miners' union. The employment figure needs its label said aloud. Contemporary estimates put the fall in mine employment at roughly a quarter between 1923 and 1929. It is a contemporary estimate, not a modern census count, and students should repeat it with the word estimate attached. Even as an estimate, it describes tens of thousands of mining families losing work in the middle of a supposedly prosperous decade, in regions that had no replacement industry waiting.",
             kick='B · Sick industries')

# ------------------------------------------------------ 9 · TEXTILES
content_photo('silk-port.jpg', 'Textiles: too much cloth',
              ['New England mills faced newer southern mills',
               'Southern mills paid lower wages',
               'The industry could weave more cloth than customers wanted',
               'Owners cut wages, closed, or moved south'],
              "The photograph is by Lewis Hine and shows a young woman at work among racks of silk thread spools at the Cheney Silk Mills in South Manchester, Connecticut, in 1924. Hine photographed for the National Child Labor Committee, and the mill's own caption called these favorable working conditions, which students may weigh for themselves. Textiles were sick differently from coal. The industry could weave more cloth than customers wanted, so mills competed by cutting costs, and the sharpest competition came from inside the industry itself. Older mills in New England faced newer southern mills paying lower wages, and owners responded by cutting wages, closing, or moving production south. The pattern to name for students is the same one coal showed: when an industry carries more capacity than its market supports, the adjustment lands on workers first, in pay, in hours, and in jobs, while the owners' problem is described as the industry's sickness.",
              kick='B · Sick industries', )

# ------------------------------------------------- 10 · SECTION C DIVIDER
divider_text('Section C', 'Labor Loses Ground',
             'Fewer members, and two employer strategies working toward the same result.',
             "Section C turns from sick industries to the workers inside all industries, and its claim is that labor lost ground all decade, in numbers and in power. Union membership fell from about five million in 1920 to about three and a half million in 1929, a loss of nearly a third. That did not happen by accident. Employers organized a deliberate open shop drive, which they branded the American Plan, and courts backed them with injunctions against strikes. Other employers chose a softer looking strategy, welfare capitalism, offering benefits in place of independent organization. The section's analytical point, and the one the reading's third question tests, is that the hard strategy and the soft strategy worked toward the same result: workers without an independent union of their own. Keep the two strategies side by side in students' minds as the next two slides take them in turn.")

# ------------------------------------------------------ 11 · THE OPEN SHOP DRIVE
content_text('The open shop drive',
             ['Union membership: about 5 million in 1920, about 3.5 million in 1929',
              'The American Plan: the open shop drive, renamed',
              'Hired without joining a union',
              'In many shops, hired only by promising not to join',
              'Courts backed employers with injunctions against strikes'],
             "The open shop drive was a campaign, and students should hear it as one. Employers organized to keep union membership from being a condition of getting or keeping a job, and they called the drive the American Plan, a name chosen to make union membership itself sound unpatriotic. In the guided notes definition, an open shop is a workplace in which workers are not required to join a union in order to hold their jobs. The practice often went further than the definition's neutral wording: in many shops a worker could be hired only by promising not to join a union at all. Courts backed employers with injunctions against strikes, which meant a judge could forbid a strike before it began. The result is in the membership figures on screen. About five million union members in 1920 became about three and a half million in 1929, in a decade when the workforce itself was growing.",
             kick='C · Labor loses ground', size=25)

# ------------------------------------------------------ 12 · WELFARE CAPITALISM
content_text('Benefits instead of a union',
             ['Welfare capitalism: pensions, paid vacations, stock plans, housing',
              'Benefits offered so workers would see no need for a union',
              'Company unions discussed grievances with management',
              'Set up and financed by the employer',
              'No independent bargaining, no real strike strength'],
             "Some large employers took a second approach, and it looked generous. Under welfare capitalism, employers offered pensions, paid vacations, stock purchase plans, and company housing, hoping workers who received these benefits would see no need for a union. In the guided notes definition, welfare capitalism is an employer's policy of providing benefits such as pensions, paid vacations, and recreation in order to keep workers satisfied and to keep unions out. The definition's final clause is the point: the benefits had a purpose beyond generosity. Many of the same firms set up company unions. In the guided notes definition, a company union is an organization for discussing workers' grievances that is set up and financed by the employer rather than by an independent union. An organization the employer creates and funds cannot bargain from an independent position or strike with real strength, and the benefits themselves reached only a minority of workers.",
             kick='C · Labor loses ground', size=25)

# ------------------------------------------------- 13 · SECTION D DIVIDER
divider_text('Section D', 'Paid at the Top, Borrowed at the Bottom',
             'Income concentrated where it could not be spent. Consumption ran on credit.',
             "Section D is the quiet weak place, and in some ways the most important one, because it explains why the prosperity depended on borrowing. Factory output kept climbing through the decade, and someone had to buy what factories made. But income concentrated at the top, where families already owned what they needed and could not spend fast enough to absorb national output. Consumption therefore depended on everyone else, the workers and farmers whose incomes this lesson has already shown to be flat, falling, or insecure. Credit filled the gap between what ordinary families earned and what the economy needed them to spend. That arrangement can run for years. It cannot run forever, because installment payments are fixed even when income is not. Introduce the next slide as an estimate and keep that label on it, because precision about evidence is part of what this lesson teaches.")

# ------------------------------------------------------ 14 · INCOME STAT
stat('30%', 'of 1929 personal income went to the richest 5 percent',
     'A Brookings Institution estimate for 1929. The figure is an estimate, and it is taught as one.',
     "Dwell on what this number does and does not claim. A Brookings Institution study estimated that in 1929 the richest five percent of Americans received about thirty percent of the nation's personal income. Say the label every time: this is an estimate, produced by a respected research institution from the tax and income data then available, not an exact count. The economic problem follows from the shape of the distribution, not from envy of it. The wealthy could not spend fast enough to absorb factory output; a family can only use so many cars and radios. So consumption depended on everyone else, on the farmers with halved wheat prices, the miners losing jobs, and the mill hands taking wage cuts. Their wages rose slowly through the decade. When a nation's output depends on buyers whose incomes are not keeping pace, the difference has to come from somewhere. The next slide shows where it came from: borrowing.",
     kick='D · Paid at the top, borrowed at the bottom')

# ------------------------------------------------------ 15 · INSTALLMENT CREDIT
content_text('Bought now, paid monthly',
             ['Cars, furniture, and radios sold on installment plans',
              'A small payment at purchase, the rest monthly',
              'By 1929, most durable goods bought this way, by contemporary estimates',
              'Credit filled the gap between wages and output'],
             "Installment buying was the ordinary family's share of the decade's credit system, and students should understand its mechanics before they judge it. An installment plan meant a small payment at purchase and the rest in monthly payments, which put a car, a furniture set, or a radio within reach of a family that could never have saved the full price in advance. By contemporary estimates, most durable goods were bought this way by 1929; keep the estimate label on that claim too. Credit filled the gap described on the previous slide, between slow rising wages and fast rising factory output. Name the fragility plainly. An installment contract does not shrink when a mill cuts wages or a mine closes. A decade of consumption resting on monthly payments is a decade in which any fall in income becomes a fall in buying at once, because the payments compete with the purchases. That is a weak place whether or not a stock market ever crashes.",
             kick='D · Paid at the top, borrowed at the bottom', size=25)

# ------------------------------------------------- 16 · SECTION E DIVIDER
divider_photo('biltmore-port.jpg', 'Section E', 'Florida Gave the Warning',
              ['The first boom of the decade to collapse,', 'three years early'],
              "The photograph shows the newly opened Miami Biltmore Hotel in Coral Gables, Florida, on January 18, 1926, with automobiles parked in front. Coral Gables was a planned city created by the Florida land boom itself, and this grand hotel opened at the boom's very peak. Section E is the lesson's rehearsal for 1929, and students should be told to watch for the pattern rather than the place. Through 1925, buyers purchased Florida lots, often on a small binder payment, expecting to resell within weeks at a higher price. Prices rose because the next buyer was expected, not because the land had changed. Nothing about the lots justified the prices except the belief that someone else would pay more. That is the definition of a speculative boom, and Florida ran the full cycle, rise, stall, collapse, bank failures, three years before the stock market repeated it at national scale.",
              title_size=40)

# ------------------------------------------------------ 17 · FLORIDA COLLAPSE
content_photo('hurricane-port.jpg', '1926: the buyers stopped coming',
              ['Prices collapsed when the next buyer failed to appear',
               'Banks that had lent on land failed',
               'September 1926: a hurricane struck Miami',
               'An estimated 370 people killed'],
              "The photograph shows felled pine trees and damaged houses in the Riviera section of Coral Gables after the September 1926 hurricane, photographed on October 4, 1926. Teach it in order, because the sequence is the story. In 1926 the buyers stopped coming. Prices collapsed first, because a price held up only by expected resale falls the moment the resale fails. Banks that had lent on land then failed, because their loans rested on the same inflated values. Only after the financial collapse did the hurricane strike Miami in September 1926, killing an estimated 370 people and exposing how much of the boom had been built cheaply and sold on promotion. Students often reverse the order and blame the storm. Correct that firmly: the boom was already dead when the hurricane arrived. The lesson available to stock buyers in 1929 was written here in 1926, and the reading's fourth question asks why they did not learn it.",
              kick='E · Florida gave the warning')

# ------------------------------------------------- 18 · SECTION F DIVIDER
divider_text('Section F', 'A Market Built on Borrowed Money',
             'Rising prices, bought with borrowed money, pledged against themselves.',
             "Section F builds the machine that broke in October. Stock prices climbed through 1928 and 1929, and the climb itself became the reason to buy. Speculators bought not for dividends, the income a stock pays its owner, but to resell at a higher price, and most of them bought with borrowed money. That single fact changes the character of a fall. An owner who bought with savings can wait out a decline. A buyer who borrowed against the stock cannot wait at all, because the lender controls the timetable. By the fall of 1929, brokers' loans stood at an estimated $8.5 billion, a figure the next slides return to with its estimate label attached. Tell students this section has the lesson's two most important vocabulary terms in it, speculation and buying on margin, and that the exit ticket will ask them to explain the second one in their own words.")

# ------------------------------------------------------ 19 · SPECULATION AND MARGIN
content_text('Buying on margin',
             ['Speculation: buying to resell higher, not for dividends',
              'Margin: pay part of the price, borrow the rest from a broker',
              'Sometimes an estimated ten percent down',
              'The stock itself pledged as security for the loan',
              'Prices fall: brokers demand cash, or sell the buyer out at once'],
             "Define both terms exactly as the guided notes do, because the unit test draws on these definitions. Speculation is buying an asset in the hope of selling it soon at a higher price, rather than for the income the asset produces. Buying on margin is buying stock by paying only part of the price and borrowing the rest from a broker, with the stock pledged as security for the loan. Work a simple example. A buyer puts down an estimated ten percent and borrows the rest; if the stock rises, the gain on the whole position belongs to the buyer. But margin magnified a fall as well as a rise. When prices dropped, brokers demanded more cash to protect their loans, and buyers who could not pay were sold out immediately, at whatever price the falling market offered. Estimates put brokers' loans at about $8.5 billion by the fall of 1929; that figure is an estimate, and it measures how much forced selling was waiting inside the market.",
             kick='F · A market built on borrowed money', size=24)

# ------------------------------------------------------ 20 · DOW STAT
stat('381', 'the Dow Jones Industrial Average peak, September 3, 1929',
     'Roughly triple its level of five years earlier. By mid November it stood near 199.',
     "This number marks the top of the climb, and students should fix its date: the Dow Jones Industrial Average reached 381 on September 3, 1929, roughly triple its level five years earlier. A tripling in five years, in an index of established industrial companies, is not a return on dividends. It is a price built on the expectation of resale, the speculation defined on the previous slide, financed by the margin borrowing that put an estimated $8.5 billion of brokers' loans underneath it. Note also how close the peak stands to the break: less than eight weeks separate September 3 from Black Tuesday. Nothing in the real economy changed in those eight weeks to make American industry worth half as much. What changed was the willingness of buyers to pay, and of lenders to lend. Keep the second figure from the subheading in view as well: by mid November the average stood near 199, about half its September peak.",
     kick='F · A market built on borrowed money')

# ------------------------------------------------- 21 · SECTION G DIVIDER
divider_photo('nyse-port.jpg', 'Section G', 'October 1929',
              ['Five days that broke the market,', 'and what the crash was not'],
              "The photograph is the same crowd outside the New York Stock Exchange on October 29, 1929 that opened the lesson, now shown in full. Most of the people in it owned no stock at all. They gathered because the exchange had become the symbol of the decade's prosperity, and they wanted news. Section G runs the break in order, day by day, because the order is the explanation. The break began on Thursday, October 24. Bankers intervened and steadied prices for two days, which taught many buyers that the danger had passed. It had not. Prices fell sharply again on Monday, and on Tuesday the heaviest selling in the exchange's history overwhelmed every attempt to stop it. The section then closes with the distinction the whole lesson has been building toward: what this crash was, and what it was not yet.",
              title_size=44)

# ------------------------------------------------------ 22 · THE BREAK, DAY BY DAY
content_text('Black Thursday to Black Tuesday',
             ['Thursday, October 24: nearly 13 million shares change hands',
              'The ticker tape runs hours behind the trading',
              'A bankers pool buys to steady prices, and steadies them for two days',
              'Monday, October 28: prices fall sharply again',
              'Tuesday, October 29: the heaviest selling yet recorded'],
             "Run the five days slowly, because each day explains the next. The break began on Thursday, October 24, Black Thursday, when nearly thirteen million shares changed hands and the ticker tape reporting prices ran hours behind, so brokers across the country were selling blind. A bankers' pool bought to steady prices, and Richard Whitney placed a large order for U.S. Steel on the exchange floor. The buying steadied the market for two days, and that pause did real harm: it persuaded margin buyers to hold positions they should have sold. On Monday, October 28, prices fell sharply again. On Tuesday, October 29, the selling became the heaviest the exchange had ever recorded, and leading stocks lost roughly an eighth of their remaining value in one day. Margin buyers who could not meet the brokers' demands for cash were sold out into that fall, and their forced selling pushed prices lower still.",
             kick='G · October 1929', size=25)

# ------------------------------------------------------ 23 · BLACK TUESDAY STAT
stat('16.4 million', 'shares traded on Black Tuesday, October 29, 1929',
     'The heaviest selling the exchange had ever recorded. Leading stocks lost about an eighth of their remaining value that day.',
     "This is the figure the lesson is remembered by, and it belongs to a single day. On Black Tuesday, about 16.4 million shares were traded, the heaviest selling the exchange had ever recorded. In the guided notes definition, Black Tuesday is October 29, 1929, the day of the heaviest selling in the stock market crash of 1929, when about 16.4 million shares were traded. Help students feel the scale: Black Thursday's nearly thirteen million shares had itself been a record, and five days later the market exceeded it by more than a quarter. Volume at that level is not ordinary investors calmly revaluing companies. It is forced selling, margin accounts being liquidated by brokers protecting an estimated $8.5 billion in loans, meeting almost no buyers. By mid November the average stood near 199, about half its September peak of 381, and the market that had tripled in five years had surrendered half its value in about ten weeks.",
     kick='G · October 1929')

# ------------------------------------------------------ 24 · CRASH IS NOT DEPRESSION
content_text('A crash is not yet a depression',
             ['Only a small minority of Americans owned stock',
              'By most estimates, a few percent of the population',
              "The crash did not wipe out most families' savings",
              'A decade of mass unemployment required more',
              'Bank failures, collapsing demand, and later policy choices'],
             "End the content with the distinction the reading ends on, and teach it as a correction to the most common error students bring into this lesson. Only a small minority of Americans owned stock, by most estimates a few percent of the population, so the crash did not wipe out most families' savings. Most families had no savings in the market to lose. Their danger came from the weak places this lesson catalogued: farm prices already low, industries already sick, unions already shrinking, and consumption already resting on installment debt. Turning the October blow into a decade of mass unemployment required more: bank failures that destroyed deposits and credit, collapsing demand as frightened families stopped buying, and later policy choices that deepened or prolonged the fall. That bridge from crash to Depression is the subject of the next unit. Students who merge the two events into one cannot explain either of them.",
             kick='G · October 1929', size=25)

# ------------------------------------------------------ 25 · THE WEAK PLACES AT A GLANCE
s = slide(NAVY)
kicker(s, 'The weak places at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Five sectors, one verdict', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Farms', 'In depression all decade', 'Wheat about $1.04 in 1929, debts at wartime levels'),
        ('Coal and textiles', 'Sick industries, excess capacity', 'Mine jobs down about a quarter; mills moved south'),
        ('Labor', 'In decline', 'Membership 5 million to 3.5 million, 1920 to 1929'),
        ('Income and credit', 'Concentrated and borrowed', 'Top 5 percent held an estimated 30 percent of income'),
        ('The stock market', 'Lifted by speculation and margin', "Dow 381 at the peak; brokers' loans an estimated $8.5 billion")]
yy = 2.72
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=21, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 0.88
notes(s, "This slide mirrors the final table in the guided notes, The Weak Places at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The five rows are the lesson's whole argument in one screen. Farms spent the decade in depression, with wheat near a dollar against wartime debts. Coal and textiles were sick industries whose owners shifted the cost of excess capacity onto workers. Labor declined under the open shop drive, from about five million members to about three and a half million. Income and credit formed one weak place together: income concentrated at the top, an estimated thirty percent with the richest five percent, while consumption ran on installment borrowing. The stock market was lifted by speculation and an estimated $8.5 billion in brokers' loans. Grade the table generously on wording and strictly on evidence: each row needs a condition and a fact.")

# ------------------------------------------------------ 26 · VOCAB A
vocab('Words for the weak places',
      [('overproduction', 'production of more of a good than buyers will purchase at prices that cover the cost of producing it'),
       ('open shop', 'a workplace in which workers are not required to join a union in order to hold their jobs'),
       ('welfare capitalism', "an employer's policy of providing benefits such as pensions, paid vacations, and recreation in order to keep workers satisfied and to keep unions out"),
       ('company union', "an organization for discussing workers' grievances that is set up and financed by the employer rather than by an independent union")],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. Overproduction: production of more of a good than buyers will purchase at prices that cover the cost of producing it. The covering of costs is the load bearing clause; farms produced too much for profitable prices, not too much for hungry people. Open shop: a workplace in which workers are not required to join a union in order to hold their jobs. Welfare capitalism: an employer's policy of providing benefits such as pensions, paid vacations, and recreation in order to keep workers satisfied and to keep unions out. Company union: an organization for discussing workers' grievances that is set up and financed by the employer rather than by an independent union. The last two terms belong together: one bought contentment, the other simulated representation, and both stood in place of an independent union.")

# ------------------------------------------------------ 27 · VOCAB B
vocab('Words for the break',
      [('speculation', 'buying an asset in the hope of selling it soon at a higher price, rather than for the income the asset produces'),
       ('buying on margin', 'buying stock by paying only part of the price and borrowing the rest from a broker, with the stock pledged as security for the loan'),
       ('Black Tuesday', 'October 29, 1929, the day of the heaviest selling in the stock market crash of 1929, when about 16.4 million shares were traded')],
      "Three more terms, again matching the guided notes exactly. Speculation: buying an asset in the hope of selling it soon at a higher price, rather than for the income the asset produces. The contrast in the definition is the lesson: a dividend is income an asset produces, and a speculator does not care about it. Buying on margin: buying stock by paying only part of the price and borrowing the rest from a broker, with the stock pledged as security for the loan. Pledged as security means the broker can sell the stock to protect the loan, which is why a fall became forced selling. Black Tuesday: October 29, 1929, the day of the heaviest selling in the stock market crash of 1929, when about 16.4 million shares were traded. Students should keep Black Thursday, October 24, and Black Tuesday five days later, distinct.")

# ------------------------------------------------------ 28 · CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Why was the prosperity of the 1920s uneven from the start, and what exactly broke in October 1929?'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Boom Audit: test each sector of the boom against the evidence'),
        ('Notebook', 'Notebook page: rebuild the weak places at a glance in your own words'),
        ('Quick check', 'Quick Check: farms, sick industries, Florida, and the October break'),
        ('Writing', 'Uneven From the Start: the lesson question as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the farm problem and the whole economy, margin and the speed of the fall, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Boom Audit, asks students to test each sector of the supposed boom against the evidence and deliver a verdict, which is the lesson's argument performed as an investigation. The notebook page asks them to rebuild the weak places at a glance themselves. The quick check covers farms, sick industries, Florida, and the October break. The writing task, Uneven From the Start, turns the lesson question into an essay, and the strongest essays will close with the crash and Depression distinction rather than merging the two. The exit ticket has three parts: why the farm problem weakened the whole economy and not only farmers, why buying on margin made a falling market fall faster, and the lesson question answered in two or three sentences with at least two facts. This closes the unit; the next unit takes up the bridge from crash to Depression.")

dc.save(OUT)
