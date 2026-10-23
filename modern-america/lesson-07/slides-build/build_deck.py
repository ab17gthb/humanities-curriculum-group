#!/usr/bin/env python3
"""Modern America Lesson 7 deck, "The Great Recession and Its Long
Aftermath," built on the shared deck system: image-led title, fragments
only on screen, comprehensive speaker notes, full lesson and vocabulary
coverage. Fonts: Georgia titles, Lato body."""
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

def bigstat(number, label, sub, note, kick=None, size=84):
    s = slide(NAVY)
    if kick: kicker(s, kick)
    text(s, 0.9, 1.7, 11.53, 2.2, number, size=size, color=CREAM, font='Georgia',
         align=PP_ALIGN.CENTER, space_after=0)
    text(s, 0.9, 4.35, 11.53, 0.9, label, size=30, color=CREAM, align=PP_ALIGN.CENTER, space_after=0)
    if sub:
        text(s, 1.9, 5.35, 9.53, 1.2, sub, size=20, color=POWDER, align=PP_ALIGN.CENTER, leading=1.3)
    notes(s, note)
    return s

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.30, 11.5, 0.4, 'MODERN AMERICA · LESSON 7', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.64, 11.9, 1.0, 'The Great Recession and Its Long Aftermath', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.52, 11.5, 0.45, 'The near failure of 2008, the rescue, and the argument after', size=17, color=POWDER)
text(s, 0.9, 7.02, 11.9, 0.4, 'President Barack Obama signs the Lilly Ledbetter Fair Pay Act, January 29, 2009. Joyce N. Boghosian, White House photograph.', size=11, color=POWDER)
notes(s, "Open with the photograph and the date, because this lesson is about a rescue and the long argument over its terms. The photograph shows President Barack Obama signing the Lilly Ledbetter Fair Pay Act on January 29, 2009, the first bill he signed, nine days into his presidency and in the middle of the worst economic collapse since the Great Depression. Lilly Ledbetter stands at his side. Her own case, a pay discrimination claim the Supreme Court had barred as filed too late, is one of the recovery's smaller records, and this lesson will reach it in its place. The larger record runs from a housing boom built on easy credit, through the near failure of the financial system in September 2008, to the rescue, the household bill, and the two protest movements that read the same wreckage in opposite directions. Teach the lesson as a record, with the figures and their sources named.")

# ---------------------------------------------------------------- 2 QUESTION
s = slide(NAVY)
kicker(s, 'The lesson question')
text(s, 0.9, 1.6, 11.5, 2.6, 'How did the financial system nearly fail in 2008, what did the government do, and why did the recovery leave so many Americans unconvinced?', size=36, color=CREAM, font='Georgia', leading=1.2)
text(s, 0.9, 4.6, 11.5, 0.6, 'Unit question: How did the United States remake itself after 1980, in its economy, its population, and its place in the world, and what did the remaking settle and what did it leave open?', size=16, color=POWDER, leading=1.3)
notes(s, "Frame the lesson with its question, which has three parts and should be answered in order. First, the failure: how a housing boom built on subprime lending and securities became a threat to the whole financial system in September 2008. Second, the answer: what the government did, the rescue of the banks, the Federal Reserve's lending, the stimulus, and the laws of the recovery, each with its size and its stated purpose from the public record. Third, the aftermath: why a recovery that returned output and jobs still left so many Americans unconvinced, a question the Tea Party and Occupy Wall Street answered in opposite directions from the same facts. The unit question above it asks what the remaking of America after 1980 settled and what it left open. This lesson is one of the places where the honest answer is that the argument is still running, and the documents show why.")

# ---------------------------------------------------------------- 3 ONE SLIDE
s = slide(CREAM)
kicker(s, 'The lesson in one slide', color=RUST)
text(s, 0.9, 0.95, 11.5, 1.0, 'The lesson in one slide', size=30, color=NAVY, font='Georgia')
rows = [
    ('A', 'The boom that built the collapse: subprime loans, securities, one assumption'),
    ('B', 'The failure in sequence: prices fall, Lehman fails, credit freezes'),
    ('C', 'The rescue and its terms: TARP, the Federal Reserve, the stimulus'),
    ('D', 'The bill as households paid it: 10.0 percent, 8.7 million jobs, foreclosures'),
    ('E', 'The first bill signed: the Lilly Ledbetter Fair Pay Act, 2009'),
    ('F', 'Health coverage remade: the Affordable Care Act, 2010'),
    ('G', 'Two answers and a slow recovery: the Tea Party and Occupy'),
]
yy = 2.0
for letter, line in rows:
    text(s, 0.9, yy, 0.7, 0.6, letter, size=24, color=RUST, font='Georgia', bold=True)
    text(s, 1.7, yy + 0.04, 10.7, 0.6, line, size=21, color=INK)
    yy += 0.72
notes(s, "Walk the whole lesson in one pass before taking any part of it slowly. Section A builds the boom: a decade of rising house prices, subprime mortgages issued in large numbers, the loans bundled into securities and sold worldwide, all of it resting on the assumption that house prices would not fall across the whole country at once. Section B runs the failure in sequence, from prices falling in 2006 to Lehman Brothers failing on September 15, 2008 and credit freezing within days. Section C states the rescue and its terms, TARP at seven hundred billion dollars, Federal Reserve lending, the automobile bankruptcies, and the stimulus. Section D presents the household bill in numbers. Section E takes the Ledbetter Act as the recovery government's first statement. Section F covers the Affordable Care Act. Section G sets the Tea Party and Occupy against each other and closes on the recovery's uneven arithmetic.")

# ---------------------------------------------------------------- 4 DIVIDER A
divider_text('Section A', 'The Boom That Built the Collapse', 'A decade of rising prices, easy credit, and one assumption underneath it all', "Introduce Section A as the building of a structure, because the reading's point is that the collapse of 2008 was assembled in plain sight during a boom most Americans experienced as prosperity. House prices rose for a decade after the middle 1990s. Lenders competed to make loans, including subprime mortgages to borrowers with weak credit. The loans were bundled into securities and sold around the world, so the risk left the lender's books the day the loan was made. Rating agencies graded many bundles as safe, and financial firms borrowed heavily against them. Every participant in the chain could point to a reason the arrangement was sound, and every reason rested on the same assumption about house prices. Teach the section as machinery, not as villainy: the Financial Crisis Inquiry Commission's later verdict, that the crisis was avoidable, is the judgment students will test against this machinery in the activity.")

# ---------------------------------------------------------------- 5 A CONTENT
content_text('Easy credit, bundled risk', [
    'House prices rise for a decade after the middle 1990s',
    'Subprime mortgages issued in large numbers',
    'Loans bundled into securities, sold worldwide',
    'Rating agencies grade many bundles as safe',
], "Teach the four fragments as a chain, in order, because each link explains the next. First, the prices: for a decade after the middle 1990s American house prices rose almost without pause, and rising prices made every loan look safer than it was, since a borrower who could not pay could sell or refinance into a higher price. Second, the lending: lenders issued subprime mortgages in large numbers, home loans made to borrowers with weak credit at higher interest rates, often with payments set to rise after the first years. Third, the bundling: the loans did not stay with the lenders who made them, but were bundled by the thousands into securities and sold to investors around the world, so the link between the borrower's ability to pay and the holder of the risk grew long and hard to trace. Fourth, the grading: rating agencies graded many of the bundles as safe, and buyers around the world relied on the grades. Each step paid a fee to the firm that passed the risk along, so volume grew even as the borrowers' ability to carry the loans grew weaker.", kick='Section A')

# ---------------------------------------------------------------- 6 A CONTENT 2
content_text('Leverage and the one assumption', [
    'Firms borrow heavily against the securities',
    'A small fall in value can erase a firm\'s own money',
    'The assumption: prices would not fall nationwide',
], "Add the two facts that turned a housing downturn into a threat to the whole system. The first is leverage. Financial firms borrowed heavily against the securities they held, in some cases thirty dollars of borrowed money for every dollar of their own. Leverage magnifies gains while prices rise, and it magnifies losses in the other direction, so a small fall in the value of the holdings could wipe out a firm's own money entirely and leave it unable to pay its lenders. The second fact is the assumption, stated everywhere in the era's own record: house prices would not fall across the whole country at once. Regional falls had happened before and the system had absorbed them, because losses in one region were offset by gains in another. A national fall broke the offset. Every security, every grade, and every loan rested in the end on that one expectation, and Section B begins at the moment the expectation failed, when prices began falling in 2006.", kick='Section A')

# ---------------------------------------------------------------- 7 DIVIDER B
divider_text('Section B', 'The Failure in Sequence', 'Prices fall from 2006, and in September 2008 the system comes within days of collapse', "Introduce Section B as a sequence, and keep the dates in order, because the speed of September 2008 is itself one of the lesson's facts. The fall began slowly: house prices began falling in 2006, borrowers who owed more than their houses were worth stopped paying, and the securities built on their loans lost value through 2007. In March 2008 the Federal Reserve helped rescue the investment bank Bear Stearns, an early warning that a major firm could not stand on its own. September brought the sequence to its crisis. The government took over Fannie Mae and Freddie Mac, the two mortgage companies at the center of the housing market. Lehman Brothers failed outright on September 15. A money market fund broke under its losses, and ordinary short term credit, the borrowing businesses use to meet payrolls and stock shelves, began to freeze. Officials told Congress the system itself stood days from collapse, in their own record of those weeks.")

# ---------------------------------------------------------------- 8 B CONTENT
content_text('September 2008', [
    'Fannie Mae and Freddie Mac taken over',
    'Lehman Brothers fails, September 15, 2008',
    'A money market fund breaks; credit freezes',
    'Officials: the system stood days from collapse',
], "Teach September 2008 day by day in outline. The takeover of Fannie Mae and Freddie Mac placed the two companies that stood behind half the country's mortgages under direct government control, an admission that the housing market's center could not hold itself up. The failure of Lehman Brothers on September 15, 2008 was the largest bankruptcy in American history, and it was allowed to happen, which is why it shocked the markets: firms that had assumed a rescue learned in one morning that no rescue was guaranteed. Within days a major money market fund, the kind of account businesses and savers treated as cash, broke under its Lehman losses, and lenders who could not tell which partners were sound stopped lending to all of them. That freeze is the crisis in its practical form. Credit is the economy's plumbing, and when it froze, officials at the Treasury and the Federal Reserve told Congress that the financial system itself stood days from collapse.", kick='Section B')

# ---------------------------------------------------------------- 9 STAT HOUSE PRICES
bigstat('About one third', 'the fall in national house prices from the 2006 peak', 'Measured by the Case Shiller index of house prices, as reported in the lesson reading. Prices fell by roughly a quarter to a third from peak to trough.', "Give the class the scale of the fall before returning to the narrative, and name the measure, because house price figures vary by index and students should learn to ask which measure a number comes from. The reading uses the Case Shiller measure, an index built from repeat sales of the same houses, and by that measure national prices fell by roughly a quarter to a third from the 2006 peak to the bottom of the fall. Translate the fraction into a household's position. A family that bought near the peak with a small down payment owed more than the house was worth within a few years, a position lenders call being underwater. A family that kept its income could keep paying and wait. A family that lost work faced a loan it could not pay on a house it could not sell for the amount owed, which is the human arithmetic behind the foreclosure figures in Section D.", kick='The bill in numbers')

# ---------------------------------------------------------------- 10 DIVIDER C
divider_text('Section C', 'The Rescue and Its Terms', 'TARP, the Federal Reserve, the automobile bankruptcies, and the stimulus', "Introduce Section C as the government's answer, stated with its terms attached, because the argument of the next decade was an argument about those terms. Congress passed the Emergency Economic Stabilization Act in October 2008, creating the Troubled Asset Relief Program, TARP, with up to seven hundred billion dollars authorized to steady the banking system. The Federal Reserve cut its main interest rate nearly to zero and lent on a scale not seen before. In 2009 the government carried the automobile industry through managed bankruptcies, and the new president signed a stimulus of about eight hundred billion dollars. Supporters in both the Bush and Obama administrations said the alternative was a second Great Depression. Critics charged that the rescue saved the firms whose lending had built the collapse while their executives kept their pay. Teach both statements as part of the record, attributed to their makers, and let the activity's documents carry the argument.")

# ---------------------------------------------------------------- 11 C CONTENT
content_text('Steadying the banks', [
    'October 2008: the Stabilization Act creates TARP',
    'Up to $700 billion authorized, released in stages',
    'The Federal Reserve cuts rates nearly to zero',
    'The statute\'s purposes name taxpayers and accountability',
], "Teach the rescue's design from the statute itself, which the activity reads at Station 2. The Emergency Economic Stabilization Act of October 2008 states two purposes: to give the Secretary of the Treasury authority to restore liquidity and stability to the financial system, and to ensure the authority is used in a manner that protects home values, college funds, retirement accounts, and life savings, preserves homeownership, maximizes returns to taxpayers, and provides public accountability. Section 115 released the money in stages, from 250 billion dollars outstanding at any one time to the full 700 billion, with a presidential certification and a report to Congress required along the way. In practice TARP was used chiefly to invest in banks rather than to buy the troubled assets its name described, a change of method students should note. Beside the statute stood the Federal Reserve, cutting its main rate nearly to zero and lending against collateral no private lender would take.", kick='Section C')

# ---------------------------------------------------------------- 12 STAT TARP
bigstat('$700 billion', 'authorized for the Troubled Asset Relief Program', 'Emergency Economic Stabilization Act of October 2008. The authority was released in stages under Section 115, beginning at $250 billion outstanding at any one time.', "Put the size of the authorization in front of the class and then qualify it, because the figure was argued over for a decade in forms that confused authorization with spending. Seven hundred billion dollars was the ceiling Congress authorized in October 2008, released in stages under Section 115 of the act: 250 billion dollars at enactment, more on a presidential certification to Congress, and the full amount only after a report and a chance for Congress to disapprove. The amount actually spent under TARP came in well under the ceiling, and much of the bank investment was later repaid, facts the Congressional Budget Office reported in its accounts of the program. None of that settled the political argument, because the charge against TARP was never only about the final account. It was about order and desert: the firms steadied first were the firms whose lending the Commission later examined, and households waited for a recovery that arrived on a slower schedule.", kick='The rescue in numbers')

# ---------------------------------------------------------------- 13 C CONTENT 2
content_text('The stimulus and the car companies', [
    'Automobile industry carried through managed bankruptcies, 2009',
    'February 2009: the Recovery Act, about $800 billion',
    'Spending and tax cuts to put money in consumers\' hands',
    'Critics: the rescue saved the firms that built the collapse',
], "Complete the rescue with its second half, the part aimed at the economy beyond the banks. The automobile industry was carried through managed bankruptcies in 2009, with the government supplying the financing private markets would not, and the companies emerged under new ownership with their workforces much reduced. In February 2009 President Obama signed the American Recovery and Reinvestment Act, the stimulus, at about eight hundred billion dollars of spending and tax cuts meant to restart a stalled economy by putting money in consumers' hands: road and school construction, aid to states, extended unemployment benefits, and a tax cut delivered through paychecks. The theory was the one the vocabulary entry states: when private spending collapses, public spending can carry demand until private spending returns. The critics' charge belongs on this slide as well, stated as its makers stated it: the rescue saved the firms whose lending had built the collapse, on terms their executives survived comfortably, while the households in Section D paid in full.", kick='Section C')

# ---------------------------------------------------------------- 14 DIVIDER D
divider_text('Section D', 'The Bill as Households Paid It', 'Unemployment at 10.0 percent, 8.7 million jobs lost, millions of homes foreclosed', "Introduce Section D as the same years read from the household side of the ledger, because the lesson's central tension is that both ledgers are accurate. The financial system was steadied by the spring of 2009, and the recession officially ended in June of that year by the National Bureau of Economic Research count. The household figures kept worsening after the official end. Unemployment reached its peak in October 2009, months after the recession's formal close, and stayed near the peak into 2010. Jobs lost across the downturn totaled about 8.7 million by the Bureau of Labor Statistics count. Foreclosures ran into the millions, and household wealth fell by trillions of dollars in housing and retirement accounts by the Federal Reserve's accounting. Teach the distinction the recovery debate turns on: an economy can be growing again while the families in it are still losing ground, and both things were true at once in 2009 and 2010.")

# ---------------------------------------------------------------- 15 D CONTENT
content_text('Jobs, homes, and wealth', [
    'Great Recession: December 2007 to June 2009',
    'Unemployment peaks after the official end',
    'Millions of homes lost to foreclosure',
    'Household wealth down by trillions (Federal Reserve)',
], "Teach the four fragments as the bill itself, in the order households received it. The Great Recession ran from December 2007 to June 2009, the deepest collapse since the Great Depression, and it began in the housing and credit markets of Sections A and B before it reached the wider economy. Its cruelest feature was the lag: unemployment peaked in October 2009, four months after the recession's official end, because employers who have cut staff in a collapse do not rehire until they are sure the recovery will hold. The foreclosures joined job loss to house prices: a family needed only one of the two blows, a lost job or a fallen price, to be in danger, and millions received one or both. The wealth figure completes the bill. By the Federal Reserve's accounting, household wealth fell by trillions of dollars in housing and retirement accounts, so even families who kept their jobs and their homes watched their savings shrink.", kick='Section D')

# ---------------------------------------------------------------- 16 STAT UNEMPLOYMENT
stat('10.0%', 'unemployment in October 2009', 'Bureau of Labor Statistics. The peak came four months after the recession officially ended in June 2009, and joblessness stayed near the peak into 2010.', "Slow down on this figure, because it is the number the aftermath argument is built from. The Bureau of Labor Statistics reported unemployment at 10.0 percent in October 2009, one worker in ten in the labor force without a job and looking for one, a rate the country had not seen since the early 1980s. The date carries the lesson's point about sequence: October 2009 was a full year after the rescue of the banks and four months after the recession's official end, so the worst month for jobs arrived after the headlines had declared the emergency over. Long term unemployment, workers out of work for more than six months, also reached levels the postwar record had not shown, and it is long spells without work, more than the rate itself, that exhaust savings, force the sale of a house, and turn a recession into a family's permanent loss of ground.", kick='The bill in numbers')

# ---------------------------------------------------------------- 17 STAT JOBS
bigstat('8.7 million', 'jobs lost in the Great Recession', 'Bureau of Labor Statistics count of payroll employment lost across the downturn of 2007 to 2009 and its immediate aftermath.', "Pair this figure with the unemployment peak on the previous slide, because the two numbers measure the same loss in different units and students should be able to use both. The Bureau of Labor Statistics counted about 8.7 million jobs lost across the downturn: payroll positions that existed before the collapse and were gone at the bottom, in construction and manufacturing first, then in retail, services, and state and local government as the fall spread. The skeleton of the unit states the figure as about nine million jobs lost, and the two forms agree: 8.7 million is the bureau's count, and about nine million is its round form. Jobs returned only slowly. Employment did not pass its pre-crisis level until 2014, six years after the failure, which is why the recovery could be real in the national accounts and still feel absent in the towns where the lost jobs had been concentrated.", kick='The bill in numbers')

# ---------------------------------------------------------------- 18 DIVIDER E
divider_text('Section E', 'The First Bill Signed', 'The Lilly Ledbetter Fair Pay Act, January 29, 2009', "Introduce Section E as a change of scale, from the largest sums in the lesson to one worker's paycheck, because the recovery government chose to open with the small record and the choice itself is evidence. Lilly Ledbetter supervised a Goodyear tire plant in Alabama and learned near retirement that she had been paid less than men doing the same job for years. She sued, and the Supreme Court ruled in 2007 that her claim was filed too late, because the law's filing clock ran from the original pay decision rather than from the day she learned of the gap. Congress answered with the act that bears her name, and President Obama signed it on January 29, 2009 as the first bill of his presidency, with Ledbetter at his side, the scene in this deck's title photograph. The section teaches how a statute answers a court: Congress cannot reverse a judgment, but it can rewrite the rule the judgment applied.")

# ---------------------------------------------------------------- 19 E CONTENT
content_text('Every paycheck restarts the clock', [
    'Ledbetter learns of the pay gap near retirement',
    'Supreme Court, 2007: the claim was filed too late',
    'The act of 2009: each paycheck is a new unlawful practice',
    'Signed first, January 29, 2009',
], "Teach the act through its rule, which the activity reads at Station 3 in the statute's own words. Congress found that the Ledbetter decision significantly impairs the protections against discrimination in compensation that Congress had established, and that it unduly restricts the time in which victims can challenge discriminatory decisions. The act then provides that an unlawful employment practice occurs when a discriminatory decision is adopted, when a worker becomes subject to it, and when a worker is affected by it, including each time wages, benefits, or other compensation is paid under the decision. In plain terms, every discriminatory paycheck restarts the filing clock. The rule answers the practical problem in Ledbetter's case: pay is often secret, and a gap can run for years before a worker learns of it, so a clock that starts at the first secret decision can expire before the claim exists. Note the placement of this law in the recovery's order of business: first, ahead of the stimulus itself.", kick='Section E')

# ---------------------------------------------------------------- 20 DIVIDER F
divider_text('Section F', 'Health Coverage Remade', 'The Affordable Care Act of 2010, passed without a vote from the other party', "Introduce Section F as the recovery's largest lasting law and its most argued one, and teach it from its text and its numbers, with the claims on each side attributed. The Affordable Care Act of March 2010 required most Americans to carry health insurance, barred insurers from denying coverage for prior illness, and expanded Medicaid, the largest change to American health policy since Medicare and Medicaid in the 1960s. It passed the House and Senate without a vote from the other party, the first great social law of the modern era enacted on one party's votes alone, and opponents challenged it in court and campaigned against it in every election that followed. Supporters answered that coverage was the point of the law and pointed to the count of the newly covered. The Supreme Court upheld the law's central requirement in 2012. The section's figures, like the lesson's others, are stated with the office that counted them.")

# ---------------------------------------------------------------- 21 F CONTENT
content_text('The Affordable Care Act, 2010', [
    'Most Americans required to carry health insurance',
    'No denial of coverage for prior illness',
    'Medicaid expanded; young adults covered to age 26',
    'Upheld by the Supreme Court in 2012',
], "Teach the law in its three working parts. The requirement: Section 1501 of the act required most Americans to maintain minimum essential coverage, and Congress placed findings at its head stating that the requirement regulates economic and financial decisions about how health care is paid for, the statute's own claim about its constitutional ground, which the activity reads at Station 4. The protections: insurers were barred from denying coverage because of a prior illness, from dropping coverage when a customer fell sick, and from setting lifetime dollar limits, and young adults could stay on a parent's plan to age twenty six. The expansion: Medicaid was enlarged for people with low incomes, and marketplaces with subsidies were created for buyers without workplace coverage. By 2016 about twenty million more people held coverage than before the act, by the Department of Health and Human Services count, the figure the next slide puts on the screen. Opponents continued to charge that the requirement and the costs exceeded the federal government's proper reach.", kick='Section F')

# ---------------------------------------------------------------- 22 STAT COVERAGE
bigstat('20 million', 'more people with health coverage by 2016', 'Department of Health and Human Services count of the gain in coverage under the Affordable Care Act, comparing 2016 with the years before the law.', "Present this figure the way the lesson has presented every figure: with its source attached and its critics heard. The Department of Health and Human Services, the department that administered the law, counted about twenty million more people holding health coverage by 2016 than before the Affordable Care Act, and the uninsured rate fell to the lowest levels in the national survey record. Critics of the law answered on different ground: that premiums and deductibles rose for many buyers in the individual market, that the requirement itself was an improper use of federal power, and that a law passed without a vote from the other party lacked the standing a settlement needs. Both the count and the charges belong in the lesson, attributed to their makers. What the documents settle is the arithmetic of coverage; what they do not settle is the argument over the law's proper reach, which the elections after 2010 kept open.", kick='The aftermath in numbers')

# ---------------------------------------------------------------- 23 DIVIDER G
divider_text('Section G', 'Two Answers and a Slow Recovery', 'The Tea Party names the government; Occupy names concentrated wealth', "Introduce the closing section as the aftermath argued, because Sections C through F built a record that two movements then read in opposite directions. The Tea Party rose in 2009, within weeks of the stimulus, against the bank bailouts, the stimulus, and the health care law together, and read them as one pattern: a federal government grown too large, to be answered with smaller government and lower taxes. Occupy Wall Street began in September 2011, two years later, camping in financial districts and naming a different holder of power: concentrated wealth and the financial industry, in the name of the ninety nine percent against the one percent. Both movements began from the bailouts, a fact the activity's fifth station makes students establish from the texts. The recovery's arithmetic ran underneath both arguments: output and employment returned while wealth and trust did not return on the same schedule.")

# ---------------------------------------------------------------- 24 G CONTENT TEA PARTY
content_text('The Tea Party, from 2009', [
    'Rises against the bailouts, the stimulus, the health law',
    'Demands smaller government and lower taxes',
    'Rallies on Tax Day, April 15, 2009',
    'Reshapes Republican politics within two cycles',
], "Teach the Tea Party in its own stated terms, as the activity's fifth station does through a labeled summary resting on the movement's public record. The movement rose in the first months of 2009, weeks after the stimulus was signed, and held rallies across the country on April 15, 2009, the day federal income taxes fall due. Its stated demands were smaller government, lower taxes, and reduced federal spending and debt. It opposed the bank bailouts begun under President George W. Bush, the stimulus of 2009, and the health care law as parts of one pattern, a federal government grown beyond its proper size, and its name invoked the Boston Tea Party of 1773, a protest against a tax imposed by a distant government. Its method was electoral: it backed candidates in primary elections, defeated sitting members of Congress, and reshaped Republican politics within two election cycles, as the vocabulary entry records.", kick='Section G')

# ---------------------------------------------------------------- 25 G CONTENT OCCUPY
content_text('Occupy Wall Street, from 2011', [
    'Begins in New York, September 2011; camps in financial districts',
    'The ninety nine percent against the one percent',
    'Declaration charges: houses taken, bailouts taken, bonuses kept',
    'A claim about corporate power, stated as a movement document',
], "Teach Occupy Wall Street from its own document, the Declaration of the Occupation of New York City, accepted by the movement's New York City General Assembly on September 29, 2011 and published by the movement, which the activity quotes at Station 5. The movement began that September with an encampment in the financial district of New York and spread to cities across the country. Its name for its constituency was the ninety nine percent, set against the one percent it held responsible for the crisis and its aftermath. The declaration's charges are specific: that corporations have taken houses through an illegal foreclosure process, have taken bailouts from taxpayers with impunity, and continue to give executives exorbitant bonuses. Where the Tea Party's account placed the power in Washington, Occupy's placed it in the corporations it said run the governments that are supposed to answer to voters. Set the two accounts side by side and stop there: the lesson presents both, in their own terms, and the writing task asks students to judge the record.", kick='Section G')

# ---------------------------------------------------------------- 26 VOCAB 1
vocab('Words for the failure and the rescue', [
    ('subprime mortgage', 'a home loan for a borrower with weak credit, at a higher rate'),
    ('Great Recession', 'the collapse of 2007 to 2009, the deepest since the Great Depression'),
    ('Troubled Asset Relief Program', 'TARP, October 2008, up to $700 billion to steady the banks'),
    ('stimulus', 'spending and tax cuts to restart a stalled economy, 2009'),
], "Carry the vocabulary at the full length of the guided notes, because the test and the writing task both use these definitions exactly. Read them joined, as they stand in the notes. subprime mortgage: a home loan made to a borrower with weak credit at a higher interest rate, issued in large numbers during the housing boom of the 2000s and central to the financial crisis when house prices fell. Great Recession: the economic collapse of 2007 to 2009, the deepest since the Great Depression, in which the financial system nearly failed, unemployment reached ten percent, and millions of families lost their homes. Troubled Asset Relief Program: the program of October 2008, known as TARP, in which the federal government was authorized to spend up to seven hundred billion dollars to steady the banking system by buying troubled assets and investing in banks. stimulus: government spending and tax cuts meant to restart a stalled economy by putting money in consumers' hands, as in the American Recovery and Reinvestment Act of 2009, at about eight hundred billion dollars.")

# ---------------------------------------------------------------- 27 VOCAB 2
vocab('Words for the aftermath', [
    ('Affordable Care Act', 'the health law of 2010: coverage required, prior illness protected'),
    ('Tea Party movement', 'from 2009, against bailouts, stimulus, and the health law'),
    ('Occupy Wall Street', 'from 2011, the ninety nine percent against the one percent'),
], "Complete the vocabulary with the three terms of the aftermath, again at full length and in the joined form of the guided notes. Affordable Care Act: the health care law of 2010 that required most Americans to carry health insurance, barred insurers from denying coverage for prior illness, and expanded Medicaid, the largest change to American health policy since the 1960s. Tea Party movement: the conservative protest movement that rose in 2009 against the bank bailouts, the stimulus, and the health care law, demanding smaller government and lower taxes, and that reshaped Republican politics. Occupy Wall Street: the protest movement that began in New York in September 2011 and spread to cities across the country, camping in financial districts to protest economic inequality in the name of the ninety nine percent against the one percent. Note for the class that the last two definitions are written to state each movement in its own terms, one by its demands and one by its name for itself, which is the same discipline the activity's fifth station follows.")

# ---------------------------------------------------------------- 28 GLANCE
s = slide(CREAM)
kicker(s, 'Synthesis', color=RUST)
text(s, 0.9, 0.95, 11.5, 1.0, 'The record at a glance', size=30, color=NAVY, font='Georgia')
rows = [
    ('Failure', 'Subprime securities on one assumption; Lehman falls; credit freezes'),
    ('Rescue', 'TARP and the Federal Reserve steady the banks; the stimulus follows'),
    ('Bill', '10.0 percent unemployment; 8.7 million jobs; millions of homes lost'),
    ('Aftermath', 'Ledbetter, the health law, and two movements reading one record'),
]
yy = 2.2
for t, d in rows:
    text(s, 0.9, yy, 2.4, 0.7, t, size=23, color=NAVY, font='Georgia', bold=True)
    text(s, 3.4, yy + 0.05, 9.0, 0.9, d, size=20, color=INK, leading=1.25)
    yy += 1.1
notes(s, "Draw the lesson together in its four movements, matching the summary table at the end of the guided notes. The failure: subprime mortgages bundled into securities on the assumption that prices would not fall nationwide, then the fall, Lehman's failure on September 15, 2008, and the freeze. The rescue: TARP authorized at up to seven hundred billion dollars and released in stages, Federal Reserve lending at near zero rates, the automobile bankruptcies, and the stimulus of February 2009. The bill: unemployment at 10.0 percent in October 2009, about 8.7 million jobs lost, millions of homes foreclosed, and household wealth down by trillions. The aftermath: the Ledbetter Act restarting the pay clock with every paycheck, the Affordable Care Act extending coverage to about twenty million more people while passing on one party's votes, and the Tea Party and Occupy reading the same record in opposite directions. Hold the four movements apart, because the writing task grades students on keeping the sequence straight.")

# ---------------------------------------------------------------- 29 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.15, 11.5, 1.6, 'Who was rescued, who paid, and who was left to the recovery?', size=32, color=CREAM, font='Georgia', leading=1.2)
text(s, 0.9, 2.95, 11.5, 1.0, ['Work from the documents. The statute states its purposes; the Commission states its verdict; the movements state their charges. Argue from them.'],
     size=20, color=POWDER, leading=1.3)
rows = [('Activity', 'The Rescue File: the Commission, the statute, the two laws, the two movements'),
        ('Notebook', 'Notebook page: failure or claim, the answer made, the cost or result'),
        ('Quick check', 'The Rescue and Its Terms: the statute\'s purposes read closely'),
        ('Writing', 'Who Was Rescued, Who Paid: the rescue, the bill, and the judgment')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the subprime mortgage and its assumption, TARP and the critics\' charge, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by handing the lesson to the work. The activity, The Rescue File, runs five stations: the Financial Crisis Inquiry Commission's conclusions with its dissents noted, the Stabilization Act's purposes and staged limits, the Ledbetter Act's findings and paycheck rule from the audited bank record, the Affordable Care Act's findings with its requirement and protections summarized and labeled, and the paired protest station, a labeled summary of the Tea Party in its stated demands beside the quoted Declaration of the Occupation of New York City, ending with a ledger and a verdict on which protest answer the following decade rewarded. The notebook page holds the record in the chart of failure or claim, the answer made, and the cost or result. The quick check tests close reading of the statute's purposes against the September 2008 background. The writing task requires the rescue stated first, the household bill in numbers, and a judgment about who was left to the recovery, answered against the strongest fact on the other side. The exit ticket has three parts, as printed at the end of the guided notes.")

dc.save(OUT)
