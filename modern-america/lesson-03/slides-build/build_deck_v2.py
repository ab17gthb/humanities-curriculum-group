#!/usr/bin/env python3
"""Modern America Lesson 3 deck builder. Images: ADA signing (Bush Library, PD) and Gulf War coalition (DoD, PD). No PD steel mill image was verified, so the factory sections are text and stat led, recorded in img/SOURCES.md."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
LESSON_DIR = os.path.dirname(HERE)
UNIT_DIR = os.path.dirname(LESSON_DIR)
sys.path.insert(0, UNIT_DIR)
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags, photo_right,
                         divider_photo, content_photo, content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED, W, H)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

dc.IMG = os.path.join(HERE, 'img')
OUT = os.path.join(LESSON_DIR, 'lesson-03-slides.pptx')

spec = open(os.path.join(UNIT_DIR, 'build-scripts', 'unit-spec.md')).read()
sec = spec.split('### Lesson 3')[1].split('### Lesson 4')[0]
TERMS = []
for line in sec.splitlines():
    line = line.strip()
    if line.startswith('- '):
        t, d = line[2:].split(': ', 1)
        TERMS.append((t.strip(), d.strip()))
assert len(TERMS) == 7, TERMS
TD = dict(TERMS)

def vocab(title, terms, note, kick='The vocabulary'):
    s = slide(CREAM)
    kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95, 11.5, 1.0, title, size=30, color=NAVY, font='Georgia')
    yy = 2.1
    for term, dfn in terms:
        text(s, 0.9, yy, 4.1, 0.9, term, size=24, color=NAVY, font='Georgia')
        text(s, 5.15, yy + 0.06, 7.3, 1.1, dfn, size=18, color=MUTED, leading=1.2)
        yy += 1.52
    notes(s, note)
    return s

SHORT = {
 'peace dividend': 'the saving Americans expected to redirect from military spending to needs at home after 1991',
 'Persian Gulf War': 'January and February 1991: a coalition with United Nations authorization drove Iraq out of Kuwait in six weeks',
 'globalization': 'the deepening connection of world economies through trade, investment, and production across borders',
 'North American Free Trade Agreement': 'the 1994 agreement among the United States, Canada, and Mexico removing most tariffs among the three',
 'outsourcing': 'moving work, especially factory production, to lower cost workers in other countries',
 'Rust Belt': 'the industrial Northeast and Midwest, where closings emptied mills and cities lost population',
 'service economy': 'an economy where most jobs produce services rather than goods, the form America took as factories shrank',
}

def content_photo_s(img, title, items, note, kick=None, size=21):
    s = slide(CREAM)
    photo_right(s, img)
    if kick: kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95 if kick else 0.8, 6.9, 1.2, title, size=31, color=NAVY, font='Georgia', leading=1.05)
    frags(s, items, y=2.15 if kick else 2.0, w=6.9, size=size)
    notes(s, note)
    return s

# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'MODERN AMERICA \u00b7 LESSON 3', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'After the Cold War', size=30, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'A six week war, a promised dividend, a rights law, and an economy rebuilt around trade.', size=17, color=POWDER)
notes(s, "Open with the photograph and state its limits honestly. It shows coalition forces in the Persian Gulf War of 1991, a Department of Defense photograph in the public domain. The Cold War unit owns the diplomacy of 1989 to 1991, the summits, the fall of the Berlin Wall, and the dissolution of the Soviet Union in December 1991. This lesson takes those same years at home, as a domestic event with domestic consequences. Three questions organize the hour. What did the United States do first with its sole superpower standing? What did Americans expect the end of the rivalry to pay them? And when the economy rebuilt itself around trade, who gained and who paid? Tell students that every figure used today names its federal source, because the argument of this lesson is an argument about figures and who they describe.")
# 2 QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('What did the end of the Cold War make possible at home, and who gained and who paid in the economy that followed?', {})]], size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': RUST_LT, 'italic': True}), ('How did the United States remake itself after 1980, in its economy, its population, and its place in the world, and what did the remaking settle and what did it leave open?', {'italic': True})]], size=17, color=POWDER, font='Georgia', leading=1.2)
notes(s, "Read the lesson question aloud and split it into its two halves, because the exit ticket and the writing task grade the halves separately. The first half asks about possibility. The Cold War ending freed money, attention, and confidence, and the records show three early uses of that freedom: a coalition war in the Gulf, a debate over a peace dividend, and a civil rights law for Americans with disabilities. The second half asks about distribution. The economy that followed grew, and the growth was real, with a long expansion, full employment, and budget surpluses. The same decades cut manufacturing employment by about a third. A strong student answer holds both halves in one paragraph and attributes each figure to its source, the Bureau of Labor Statistics, the Bureau of Economic Analysis, or the Congressional Budget Office.")
# 3 MAP
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'The hinge years, then the boom', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The First War of the Sole Superpower', 'Iraq invades Kuwait, the coalition answers in six weeks'),
        ('B', 'The Peace Dividend Debate', 'Deficits, taxes, or needs at home: three claims on one saving'),
        ('C', 'A Rights Settlement in the Same Years', 'The ADA of 1990 and the signing statement'),
        ('D', 'An Economy Rebuilt Around Trade', 'Globalization measured, NAFTA, the WTO, and China'),
        ('E', 'The Factory Economy Gives Its Answer', 'Outsourcing, the Rust Belt, and the service economy'),
        ('F', 'The Boom, the Surplus, and Welfare', '3.9 percent unemployment, surpluses, and the 1996 law'),
        ('G', 'Shadows Inside the Boom', 'The cleanup, the 1993 bombing, Seattle 1999, the open question')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This map follows the guided notes section by section, and students should keep it open as the route for the hour. Sections A, B, and C stay inside the hinge years of 1990 and 1991: the Gulf War abroad, the peace dividend argument at home, and the Americans with Disabilities Act as the rights settlement of the same moment. Sections D and E carry the economic story of the decade: trade opened by agreement and measured as a rising share of the economy, while factory employment fell through the same years. Section F reads the boom at the top, the expansion, the surplus, and the welfare law of 1996. Section G closes with the shadows the boom carried and the distributional question the numbers frame but do not settle. That question, who gained and who paid, is the thread to pull through every section.")
# 4 DIVIDER A
divider_photo('gulf-port.jpg', 'Section A', 'The First War of the Sole Superpower', ['August 1990: Iraq invades Kuwait. January 1991: the coalition answers.'],
 "Set the boundary of this lesson before the war itself, in one sentence. The diplomacy of 1989 to 1991, the summits and the Soviet dissolution, belongs to the Cold War unit, and this lesson names that diplomacy rather than reteaching it. What this lesson owns is the domestic register of the same years. Iraq invaded Kuwait on August 2, 1990, and the United States assembled a coalition of twenty eight countries under United Nations resolutions, with the consent of Congress. For Americans watching at home, this was the first war of a new condition: the United States acted as the world's sole superpower, without a rival able to answer in kind. Ask the class to hold that condition in mind, because the peace dividend debate in the next section is unintelligible without it. The rivalry that had organized American budgets and strategy for four decades was ending, and its ending had a price and a possible payment.")
# 5 CONTENT A
content_photo_s('gulf-port.jpg', 'Six weeks in the Gulf', ['Iraq invaded Kuwait on August 2, 1990.', 'Bush announced air attacks on January 16, 1991.', 'The coalition acted with United Nations authorization and the consent of Congress.', 'Twenty-eight countries had forces in the Gulf.', 'Iraq was driven from Kuwait by late February.'],
 "Carry the definition exactly as the guided notes print it. The Persian Gulf War is this: " + "Persian Gulf War: " + TD['Persian Gulf War'] + ". Then read the president's address at Station 3 of the activity as the section's core document. Bush opens with a time stamp: just two hours ago, allied air forces began an attack on military targets in Iraq and Kuwait, and ground forces were not yet engaged. He grounds the action in two authorities, United Nations resolutions and the consent of the United States Congress, and in a diplomatic record he says was exhausted. The ground campaign in late February lasted one hundred hours. Teach the war's brevity and its televised character plainly: Americans watched it live, and its quick success shaped what they expected the new era to feel like, competent, limited, and victorious at low American cost.", kick='A · The First War of the Sole Superpower')
# 6 STAT A
stat('6 weeks', 'from air campaign to ceasefire, January and February 1991', 'An American led coalition drove Iraq out of Kuwait, acting with United Nations authorization',
 "Stop on the brevity and make students price what it taught. Six weeks is short for a war that reversed an invasion and destroyed much of an army, and the coalition's casualties were low beside the wars Americans remembered from Vietnam. That experience fed a confidence that the post Cold War order could be managed by coalition, law, and overwhelming technology. It also set up the domestic question of the next section with unusual clarity. If wars could now be this brief and rivals were gone, why should the federal government keep spending as if the Soviet Union still existed? Defense budgets, bases, shipyards, and contractors across the country rested on the old rivalry's arithmetic. The peace dividend was the name Americans gave to the difference between that arithmetic and the new one, and the fight over who would receive it began before the troops came home.")
# 7 DIVIDER B
divider_text('Section B', 'The Peace Dividend Debate', 'If the rivalry is over, who receives the saving: the deficit, the taxpayer, or the town that needs work?',
 "Introduce the peace dividend as an argument, not a payment, because no check was ever written under that name. For four decades, competition with the Soviet Union had justified the largest peacetime military establishment in American history, and its spending reached into congressional districts in every state. When the rivalry ended, three claims were made on the expected saving at once. One claim said the money should retire debt, since the federal government had borrowed heavily through the 1980s. A second said it should return to taxpayers. A third said it should meet needs at home that the rivalry had crowded out, roads, schools, and health care. Standing against all three claims were the people whose livelihoods the old spending had supported. A dividend for the country was a lost contract for a defense town, and students should be able to state both sides of that sentence before judging either.")
# 8 CONTENT B
content_text('Three claims on one saving', ['One claim said the saving should retire the federal deficit.', 'A second claim said it should cut taxes and return the money.', 'A third claim said it should be spent on needs at home.', 'The cost side fell on bases, shipyards, and contractors.', 'No single payment was ever made.'],
 "Carry the definition exactly. The peace dividend is this: " + "peace dividend: " + TD['peace dividend'] + ". The definition's last phrase does quiet work: the dividend was debated through the 1990s, which means the debate itself is the historical fact to teach, not a sum that arrived. Defense spending did fall as a share of the economy during the decade, and bases closed under commissions Congress created to spread that pain. But the saving was absorbed piece by piece into budgets rather than delivered as a visible transfer, which is why the writing task can honestly ask whether the dividend was ever really paid. Foreshadow the strongest candidate answer now and let students test it in Section F: the budget surpluses of 1998 to 2001 are the closest thing to a paid dividend in this record, and they arrived alongside factory losses that complicate the receipt.", kick='B · The Peace Dividend Debate', size=24)
# 9 DIVIDER C
divider_photo('ada-port.jpg', 'Section C', 'A Rights Settlement in the Same Years', ['July 26, 1990: the Americans with Disabilities Act is signed on the South Lawn.'],
 "Use the photograph to open this section: President George H. W. Bush signing the Americans with Disabilities Act on the South Lawn of the White House on July 26, 1990, a George Bush Presidential Library photograph in the public domain. Place the law in the hinge years deliberately. The same president who led the Gulf coalition signed, six months before the war, the most extensive extension of federal civil rights law since the 1960s. Disability activists had built the campaign over decades, including the Capitol Crawl of March 1990, when protesters left their wheelchairs and climbed the Capitol steps. Congress wrote its case into the statute itself, in findings that open the act, and those findings are Station 1 of the activity. Teach the law as the domestic face of the new era: while Americans debated what the country would do abroad without a rival, Congress settled a long domestic claim at home.")
# 10 CONTENT C
content_photo_s('ada-port.jpg', 'What Congress found', ['Congress found 43,000,000 Americans with disabilities.', 'Discrimination persisted in jobs, housing, transit, and voting.', 'People with disabilities often had no legal recourse before 1990.', 'The act set goals of equality, participation, and independence.', 'Congress priced discrimination itself in billions of dollars.'],
 "Read the findings as an argument in two registers, because Congress built both into the text. The first register is rights. Congress found that society had tended to isolate and segregate individuals with disabilities, that discrimination persisted across employment, housing, public accommodations, education, and transportation, and that, unlike other groups, people with disabilities had often had no legal recourse. The second register is cost. Finding nine states that discrimination denies people the chance to compete on an equal basis and costs the United States billions of dollars in unnecessary expenses from dependency and nonproductivity. That pairing let the act pass with broad support in 1990: it was argued as justice and as economics at once. Students meet this pairing again in the welfare law of Section F, argued from the other direction, and naming it here prepares that comparison.", kick='C · A Rights Settlement in the Same Years')
# 11 CONTENT C2
content_photo_s('bush-port.jpg', 'The signing statement', ['Bush promised to open up all aspects of American life.', 'The promise covered jobs, services, accommodations, transport, and phones.', 'He called for an end to segregation and exclusion.', 'The law included cost limits and phase-in periods for business.', 'Its standards were borrowed from the 1973 Rehabilitation Act.'],
 "Read the signing statement beside the findings, because the pair teaches the difference between what a statute finds and what a president promises. Bush, in the bank record, says the act promises to open up all aspects of American life to individuals with disabilities, and he lists employment opportunities, government services, public accommodations, transportation, and telecommunications. He closes by calling the act the end of the unjustified segregation and exclusion of persons with disabilities from the mainstream of American life. The same statement answers business fears directly: costs could be weighed in deciding what accommodation was reasonable, the strictest access rules fell on new construction, and employment coverage phased in over two and then four years. A strong discussion holds both documents at once: a promise stated in full, and a law written with limits, which is the ordinary shape of a settlement.", kick='C · A Rights Settlement in the Same Years')
# 12 DIVIDER D
divider_text('Section D', 'An Economy Rebuilt Around Trade', 'Production spread across borders, and governments chose the rules that let it spread.',
 "Frame globalization as a set of choices before it is a force of weather, because the documents in this section are agreements that governments negotiated, signed, and defended in votes. Trade had been growing for decades, but the end of the Cold War widened the field: markets that had stood outside the American led trading system joined it, container shipping and computing cut the cost of coordinating production across oceans, and firms learned to design in one country, build parts in a second, and assemble in a third. Each step of opening in this lesson has a date and a vote attached. NAFTA was fought through Congress in 1993. The World Trade Organization was created in 1995. Permanent normal trade relations with China passed in 2000. Teaching the dates matters, because an outcome with dates and votes can be argued about as policy, while an outcome described as inevitable cannot be argued about at all.")
# 13 CONTENT D
content_text('The agreements, in order', ['NAFTA was approved in 1993 and took effect on January 1, 1994.', 'Article 102 called for eliminating barriers to trade.', 'Article 102 called for increasing investment opportunities.', 'The World Trade Organization followed in 1995.', 'Permanent normal trade relations with China passed in 2000.'],
 "Carry both definitions exactly. Globalization is this: " + "globalization: " + TD['globalization'] + ". The North American Free Trade Agreement is this: " + "North American Free Trade Agreement: " + TD['North American Free Trade Agreement'] + ". Then read Article 102 at Station 2 closely, because its plain list is the agreement's own account of itself: eliminate barriers to trade, promote fair competition, increase investment opportunities substantially, protect intellectual property, and build procedures for disputes. Set beside it the 1993 opposition in its makers' own terms. Organized labor argued the agreement would pull production toward lower wages in Mexico. Ross Perot, the independent candidate of 1992, warned of jobs moving south. President Clinton, who signed the implementing law, argued it would create export jobs. All three claims are attributed here to their makers, and the figures of the next section are what students use to test them.", kick='D · An Economy Rebuilt Around Trade', size=24)
# 14 STAT D
stat('30 percent', 'of the American economy: imports plus exports by 2010, about', 'Up from about one quarter in 1990. Bureau of Economic Analysis figures, as labeled in the activity data record',
 "Teach this figure as a measure of connection, not of victory or loss by itself. Imports plus exports rising from about one quarter of gross domestic product in 1990 toward three tenths by 2010, per the Bureau of Economic Analysis, means that a growing share of what Americans bought and sold crossed a border. A car assembled in Michigan might carry parts made in Ontario and electronics made in Shenzhen, and a shirt in an American store was likelier each year to have been sewn abroad. Students sometimes read a trade share as a grade. It is not one. The same growth in connection carried the gains named by the agreements' supporters, cheaper goods and export markets, and the losses named by their critics, exposed factory towns. The next two sections separate those two readings and give each its own figures, which is the only honest way to hold a number this large.")
# 15 DIVIDER E
divider_text('Section E', 'The Factory Economy Gives Its Answer', 'The mills kept closing inside the boom. The question is what replaced them, and on what terms.',
 "State plainly what image is not on this slide and why, the way the student materials state their own limits. No public domain photograph of a closed American mill was verified for this build, so this section is taught from figures and text rather than from an unverified image, and the gap is recorded in the lesson's source file. The facts need no photograph. Manufacturing employment fell in every decade from the 1970s onward, through recessions and through expansions alike, and the 1990s boom was no exception. Two engines drove the fall, and students must keep them separate because they imply different judgments. Outsourcing moved production to lower cost workers abroad, a choice firms made under rules governments wrote. Automation raised output per worker at home, so factories produced more with fewer hands. Both engines shrank the goods workforce while the service economy grew around it.")
# 16 CONTENT E
content_text('Where the jobs went', ['Outsourcing moved production to lower-cost workers abroad.', 'Automation produced more output with fewer hands at home.', 'The Rust Belt saw emptied mills and shrinking cities.', 'Service jobs grew in health, retail, finance, and food.', 'Productivity rose while median wages rose slowly.'],
 "Carry all three definitions exactly. Outsourcing is this: " + "outsourcing: " + TD['outsourcing'] + ". Rust Belt is this: " + "Rust Belt: " + TD['Rust Belt'] + ". Service economy is this: " + "service economy: " + TD['service economy'] + ". Then run the distributional argument in its documented form. Supporters pointed to lower prices, export jobs, and rising productivity. Critics pointed to closed plants and median wages rising slowly while productivity rose faster. Both sides argued from federal figures, chiefly the Bureau of Labor Statistics and the Census Bureau. Require students to state each side's figures before judging.", kick='E · The Factory Economy Gives Its Answer', size=24)
# 17 STAT E
stat('11.5 million', 'manufacturing jobs in 2010, down from about 17.3 million in 1990', 'Bureau of Labor Statistics figures, as labeled on the face of the activity data record',
 "Do the subtraction aloud and then refuse the easy reading of it. About 5.8 million manufacturing jobs disappeared across twenty years that included the longest peacetime expansion in American history to that date. The easy reading says trade took the jobs, full stop. The record is narrower: outsourcing, automation, and two recessions all contributed, and the Bureau of Labor Statistics figures alone do not divide the loss among its causes. What the figures do settle is the direction and the scale, and the fact that the loss was structural rather than a bad year. A town built on one mill did not experience 5.8 million as a statistic. It experienced it as the mill gate locked, the school enrollment falling, and the young leaving for service work in a city. Teach the number at both scales, national and local, because the distributional argument lives in the distance between them.")
# 18 DIVIDER F
divider_text('Section F', 'The Boom, the Surplus, and a New Welfare Law', 'The top line decade: full employment, a surplus, and assistance rewritten with clocks attached.',
 "Introduce this section as the boom read at the top, the way its own decade reported it, before Section G reads the same years from underneath. The expansion that began in 1991 ran for ten years. Unemployment fell below four percent, a level economists of the period treated as effectively full employment. Federal receipts rose with the boom and with the tax increases of 1990 and 1993, spending restraint held, and from 1998 to 2001 the federal budget ran surpluses for the first time in a generation. Into that prosperity, Congress and President Clinton rewrote the welfare law in 1996, replacing a federal entitlement dating to 1935 with a block grant carrying work requirements and time limits. The pairing is the section's subject: a country rich enough to run surpluses chose to time limit its cash assistance, and argued about the choice in the open, with supporters and critics named in the reading.")
# 19 CONTENT F
content_text('1996: welfare rewritten', ['AFDC ended after six decades as an entitlement.', 'TANF replaced it with a capped block grant to the states.', 'Work was required after two years of benefits.', 'Federal funds carried a five-year lifetime limit.', 'Clinton signed the law over opposition from his own party\u2019s left.'],
 "Teach the welfare station the way it is labeled in the activity: a labeled summary resting on the public record of Public Law 104-193, with the statute's stated purposes quoted in its own words. Those purposes pull in two directions inside one section of law. The first promises assistance so that children may be cared for in their own homes or in the homes of relatives. The second promises to end the dependence of needy parents on government benefits by promoting job preparation, work, and marriage. The two limits operationalize the second purpose: work after two years, and no federally funded benefits after five years in a lifetime. President Clinton signed the act in August 1996 after vetoing two earlier versions, over the opposition of many in his own party. Caseloads then fell sharply in a full employment economy. How much of that fall the law caused, and how much the boom caused, was argued then and remains a live example of an attribution problem for students to name.", kick='F · The Boom, the Surplus, and a New Welfare Law', size=24)
# 20 STAT F
stat('3.9 percent', 'unemployment in 2000, the boom at full stretch', 'Bureau of Labor Statistics. The federal budget ran surpluses from 1998 to 2001, per the Congressional Budget Office',
 "Hold this slide next to the manufacturing slide in memory and make the class do the same. Both figures are true, both are federal, and they describe the same country in the same decade. Unemployment of 3.9 percent in 2000, per the Bureau of Labor Statistics, means nearly everyone who wanted work and was counted as seeking it had found it, including many workers leaving welfare under the 1996 law. Surpluses from 1998 to 2001, per the Congressional Budget Office, mean the federal government took in more than it spent four years running. Yet the factory economy shrank through those same years. The lesson's distributional question is precisely this coexistence: aggregate success and concentrated loss, measured by the same statistical system. A student who can state both figures with both sources has the boom understood at the level this unit requires, which is the level at which a verdict can begin.")
# 21 DIVIDER G
divider_text('Section G', 'Shadows Inside the Boom', 'A cleanup bill, a bomb that warned, a protest that named the argument, and the question left open.',
 "Close the lesson by returning the shadows to the record in chronological order, briefly, the way the reading carries them. The decade opened with the savings and loan cleanup, the resolution of the thrift failures of the 1980s, which cost taxpayers well over one hundred billion dollars and was an early charge against the era's promised dividend. In February 1993 a truck bomb exploded in the garage beneath the World Trade Center, killing six people; the reading names it as a warning little heard, and the next unit lessons take up what followed from such warnings. In December 1999, tens of thousands of protesters filled Seattle during a World Trade Organization meeting, arguing that globalization served corporations over workers and the environment. None of these shadows cancels the boom. Together they mark its edges, and they hand the unit its next questions in the order Americans actually met them.")
# 22 CONTENT G
content_text('The question the numbers frame', ['A tide that lifted all boats?', 'Or a sorting that lifted some?', 'The gains included prices, exports, the surplus, and full employment.', 'The costs included mills closed, wages rising slowly, and limits met.', 'The figures frame the question, and they do not settle it.'],
 "End the teaching on the open question and resist closing it for the class, because the writing task grades students on closing it themselves with evidence. State the two readings one last time in their strongest documented forms. The tide reading rests on the aggregate record: a ten year expansion, 3.9 percent unemployment, four surplus years, cheaper goods, and a rights settlement that opened public life to millions. The sorting reading rests on the distribution inside that record: about 5.8 million manufacturing jobs gone, Rust Belt cities hollowed, median wages rising slowly against productivity, defense towns charged for the peace, and welfare families meeting time limits inside a boom. Both readings cite true figures from named federal sources. What separates a strong answer from a weak one is not the side chosen. It is whether the student states the other side's best figure and explains why the verdict survives it.", kick='G · Shadows Inside the Boom', size=24)
# 23 GLANCE
s = slide(NAVY)
kicker(s, 'The ledger at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Built, paid, and charged', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The hinge', 'Gulf victory, the ADA, the dividend debated', 'Defense towns await the bill'),
        ('Trade opens', 'NAFTA 1994, WTO 1995, China 2000', 'Production moves, prices fall'),
        ('Factories shrink', '17.3 million to 11.5 million by 2010', 'The Rust Belt pays in place'),
        ('The boom', '3.9 percent unemployment, surpluses 1998 to 2001', 'Welfare clocks run inside it')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the closing table of the guided notes, The Ledger at a Glance, and students should complete that table now from memory where they can. Check it with the two questions that expose shallow answers. First, which rows show gains that arrived as cash or its equivalent, and which show gains that arrived as rights or prices? The surplus years and lower prices are one kind of receipt; the ADA's access is another, and a ledger that counts only cash will undervalue the hinge years. Second, which row is unfinished? The trade row: its costs and gains kept accumulating past 2000, into the China shock debates of the following decade, which later lessons inherit. The table is the lesson in miniature: a settlement built, its payments uneven, and its argument carried forward into the rest of the unit.")
# 24 VOCAB A
vocab('Words for the hinge', [(t, SHORT[t]) for t in ['peace dividend', 'Persian Gulf War', 'globalization', 'North American Free Trade Agreement']],
 "Four terms, matching the guided notes word for word, and students should copy the definitions because the unit test draws on them. peace dividend: " + TD['peace dividend'] + ". Persian Gulf War: " + TD['Persian Gulf War'] + ". globalization: " + TD['globalization'] + ". North American Free Trade Agreement: " + TD['North American Free Trade Agreement'] + ". Press two details. The peace dividend definition uses the language of expectation, because the expectation is the documented fact. The NAFTA definition states what the agreement removed. Effects are argued in the lesson; the definition states the instrument.")
# 25 VOCAB B
vocab('Words for the new economy', [(t, SHORT[t]) for t in ['outsourcing', 'Rust Belt', 'service economy']],
 "Three more terms, again matching the guided notes exactly. outsourcing: " + TD['outsourcing'] + ". Rust Belt: " + TD['Rust Belt'] + ". service economy: " + TD['service economy'] + ". One pairing in these definitions earns emphasis before the exit ticket. Outsourcing names a practice by firms, moving work to lower cost workers in other countries, and its definition reaches beyond factories to the office and service jobs that followed in the next decade. The service economy names the result at home: most jobs producing services rather than goods. A student who can move between those two terms, practice and result, with the Rust Belt as the place where the exchange was hardest, has the vocabulary doing the work it was chosen to do.")
# 26 SYNTHESIS
content_text('Answering the question', ['What became possible included a coalition war, a rights law, and open trade.', 'Those who gained included consumers, exporters, and workers in 2000.', 'Those who paid included factory towns, defense towns, and families timed out.', 'The verdict needs both columns of the ledger.'],
 "Run the synthesis as the writing task rehearsal and build it from the class's own answers before summarizing. Strong answers refuse both single column verdicts. The boom only answer fails on the manufacturing figures, which are federal and cover the whole period. The betrayal only answer fails on the surplus, the unemployment rate, and the ADA, which are equally documented. The defensible verdicts all share one shape: they name what the Cold War's end made possible, they assign the gains and the costs to the people the documents name, and they attribute every figure to its source. Test the synthesis against the prompt's hardest version before closing. If the peace dividend means a payment every American could see, was anything in this record such a payment? Let students argue that question with the surplus and the ADA as the two candidate receipts, because that argument is the essay.", size=24)
# 27 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4, ['What did the end of the Cold War make possible at home, and who gained and who paid in the economy that followed?'], size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Ledger of the Boom: five stations, the sorting table, then the verdict'),
        ('Notebook', 'Notebook page: the ledger chart, from the Gulf War to the boom and welfare'),
        ('Quick check', 'The Signing and the Figures: the ADA statement sourced, the data line used'),
        ('Writing', 'Was the Peace Dividend Ever Really Paid: the ledger judged in one essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the peace dividend defined, the manufacturing figures with their source, and the lesson question in two or three sentences.', size=15, color=POWDER)
notes(s, "Close by handing the lesson to the work. In the activity, The Ledger of the Boom, each group works five records, the ADA findings, NAFTA's Article 102, President Bush's Gulf War address of January 16, 1991, a data record built from federal statistics, and the welfare law of 1996 as a labeled summary with the statute's purposes quoted, then sorts each under what the settlement built, who it paid, and who it cost. The notebook page rebuilds the lesson as a chart of what happened, who gained, and who paid. The quick check, The Signing and the Figures, sources the Bush ADA signing statement and tests whether students can use the manufacturing data line beside the surplus. The writing task asks the lesson's closing question directly: was the peace dividend ever really paid? The exit ticket has three parts: the peace dividend defined with one claimed use, the manufacturing figures for 1990 and 2010 with the Bureau of Labor Statistics named, and the lesson question answered in two or three sentences with one gain and one cost.")

dc.save(OUT)
