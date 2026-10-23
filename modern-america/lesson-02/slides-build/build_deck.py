#!/usr/bin/env python3
"""Modern America Lesson 2 deck, "The Reagan Revolution,"
built to the approved system: image-led slides, fragments only on
screen, comprehensive speaker notes, full lesson + vocabulary
coverage. Fonts: Georgia titles, Lato body."""
import os, re, sys
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

spec = open(os.path.join(HERE, '..', '..', 'build-scripts', 'unit-spec.md')).read()
l2 = spec.split('### Lesson 2')[1].split('### Lesson 3')[0]
DEFS = {}
for line in l2.splitlines():
    m = re.match(r'- (.+?): (.*)$', line.strip())
    if m: DEFS[m.group(1)] = m.group(2)
assert len(DEFS) == 7, DEFS.keys()

def joined(term):
    return f"{term}: {DEFS[term]}"

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

LQ = 'What did the Reagan administration change about what the federal government did, and what did it leave in place?'
UQ = 'How did the United States remake itself after 1980, in its economy, its population, and its place in the world, and what did the remaking settle and what did it leave open?'

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'MODERN AMERICA · LESSON 2', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Reagan Revolution', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'A president promises to curb the federal establishment, and the record keeps the receipts', size=17, color=POWDER)
notes(s, "The photograph shows Ronald Reagan delivering his first inaugural address from the west front of the United States Capitol on January 20, 1981, in a wide angle view held by the National Archives. Place the lesson before the class in one move. Lesson 1 ended with the postwar economic settlement breaking down, inflation and unemployment high together, a tax revolt organized, and a coalition assembled to answer Carter's diagnosis with a different one. This lesson takes up the answer in power. A new administration set out to change what the federal government did, in taxes, in regulation, in labor relations, and in the courts, and it governed for eight years. Students should leave able to argue both halves of the record with figures attached: what the revolution changed, and what it left standing when it ended.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[(LQ, {})]], size=40, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                (UQ, {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question is an accounting question, and students will need both columns of the ledger for the exit ticket and the writing task. The change column fills quickly: a tax code rewritten in 1981, regulation loosened, inflation broken through a hard recession, more than eleven thousand federal workers fired in a single week, and a judiciary restocked for a generation. The survival column takes longer to see, and it is where the lesson's real work sits: Social Security and Medicare untouched, a tax increase accepted in 1982, and a national debt that more than tripled under a president elected against deficits. Warn students now against the two easy answers. The government was not dismantled, and it was not left as it was found. The lesson is the discipline of holding the change and the survival in one view, with the figures for each.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'The promise, the program, and the limits', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The Mandate Stated', 'Government is the problem, January 20, 1981'),
        ('B', 'The Economic Program', 'Tax cuts, deregulation, and high interest rates'),
        ('C', 'PATCO: Labor\'s Terms Rewritten', '48 hours, and more than 11,000 fired'),
        ('D', 'The Coalition Held and Widened', 'Reagan Democrats and 49 states in 1984'),
        ('E', 'The Limits of the Revolution', 'Debt, entitlements, and the judges'),
        ('F', 'Iran-Contra: The Breach', 'Arms, the Contras, and the Tower report'),
        ('G', 'The Other Wars, and the Consoler', 'Drugs, AIDS, and the Challenger evening')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A covers the inaugural claim of January 20, 1981. Section B covers the economic program, the tax act, deregulation, and the Volcker recession. Section C covers the PATCO strike and firings of August 1981. Section D covers the recovery and the widened coalition that reelected the president in 1984. Section E covers the limits, the debt, the untouched entitlements, and the courts. Section F covers the Iran-Contra affair and the Tower Commission. Section G covers the War on Drugs, the AIDS epidemic, and the Challenger address. The summary table at the end of the guided notes is titled The Revolution at a Glance, and students will complete it from these seven sections.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', 'The Mandate Stated',
             'An inaugural address that named government itself as the problem.',
             "Set up the inaugural as a governing document, not a ceremony. Every president promises; this address is worth reading closely because the administration that followed treated its sentences as instructions. Reagan had campaigned on the diagnosis that the federal government had grown beyond the people's control and beyond the economy's capacity to carry it, and the inaugural, delivered with the Iranian hostages released the same hour and the economy in stagflation, turned the campaign claim into an official one. Tell students to listen for three things as the lesson works through the speech: the diagnosis, itemized and specific; the conclusion, which is not itemized at all; and the distance between the two, because much of the next eight years was governed inside that distance.")
print('part 1 slides done')
# ------------------------------------------------------ 5 INAUGURAL
content_photo('inaugural-port.jpg', 'Government is the problem',
              ['January 20, 1981, the west front of the Capitol',
               'Inflation named an affliction of great proportions',
               'Deficit piled upon deficit for decades',
               'The federal establishment to be curbed'],
              "The photograph shows President Reagan at the podium delivering the address on the west front of the Capitol, in a National Archives photograph; former President Carter sits at the right of the frame. Read the claim in the speech's own build. The address first itemizes: an economic affliction of great proportions, the longest and one of the worst sustained inflations in the national history, a tax system that penalizes successful achievement, and public spending that has outrun even that tax burden, piling deficit upon deficit and mortgaging the future. Only after the items does the conclusion arrive, in the sentence students will meet in the reading, the activity, and the quick check: in this present crisis, government is not the solution to our problem; government is the problem. Have students notice what the sentence does not say. It does not name a program, a bureau, or a tax. It names government, whole, and the program that followed had to be built out of that whole cloth.",
              kick='A · The Mandate Stated')

# ------------------------------------------------------ 6 PROMISE IN DETAIL
content_text('What the address promised',
             ['Curb the size and influence of the federal establishment',
              'Lighten a tax system called a penalty on achievement',
              'End the long trend of deficit upon deficit',
              'Act today in order to preserve tomorrow'],
             "Walk the promises as a checklist the lesson will grade at the end, because section E is this slide read backward. The first promise is institutional: curb the size and influence of the federal establishment, the standing apparatus built since the New Deal. The second is fiscal in the taxpayer's direction: lighten a tax system the speech describes as penalizing successful achievement and keeping the country from full productivity. The third is fiscal in the government's direction: end the long trend of deficit piled upon deficit, which the address calls mortgaging the future for the temporary convenience of the present. The fourth is timing: we must act today in order to preserve tomorrow. Keep the list visible in students' minds. By 1989 the record will show the second promise kept in law, the first kept only in direction and staffing, and the third not kept at all, which is the puzzle the limits section sets out to explain.",
             kick='A · The Mandate Stated', size=24)

# ------------------------------------------------- 7 SECTION B DIVIDER
divider_photo('ranch-port.jpg', 'Section B', 'The Economic Program',
              ['The president at Rancho del Cielo,', 'August 13, 1981, the tax act signed there.'],
              "The photograph shows President Reagan laughing at Rancho del Cielo, his ranch in the Santa Ynez Mountains of California, on August 13, 1981, in a White House photograph by Michael Evans: the day he signed the Economic Recovery Tax Act there, in shirtsleeves, the bill stacked on the table beside him. Use the setting to make a teaching point about the program's self image. Its authors presented the tax cut not as a favor to the wealthy but as a restoration, returning decisions about money from the government to the people who earned it, and they expected the restored incentives to do the work that government programs had failed to do. Whether the program's results matched that account is the argument students will conduct from the figures in this section, and both sides of the argument belong on the record.",
              title_size=40)

# ------------------------------------------------------ 8 SUPPLY SIDE
content_text('Supply-side economics',
             ['Cut tax rates to free work, saving, and investment',
              'Loosen regulation on industry',
              'Growth would follow production, not spending',
              'The Economic Recovery Tax Act of 1981 carries it'],
             "Teach the theory as its makers stated it, because the guided notes definition is built from their claim. The older Keynesian management of the economy worked on demand, putting money in consumers' hands so they would spend it. Supply-side economics worked on the other side of the transaction: it held that high tax rates discouraged the activities the economy needed, work, saving, and investment, and that cutting rates and loosening regulation would free production and so grow the whole economy. The Economic Recovery Tax Act of 1981 carried the theory into law, cutting individual income tax rates by about a quarter over three years: a rate reduction credit against 1981 taxes, then new rate tables for 1982, 1983, and after, each lower than the last. A companion budget act cut domestic programs while military spending rose, and deregulation, begun under President Carter in airlines and trucking, was continued and extended in banking, communications, and energy. The next slide takes the theory's most famous figure.",
             kick='B · The Economic Program', size=24)

# ------------------------------------------------------ 9 STAT 70 TO 50
stat('70 to 50', 'the top income tax rate, percent, under the 1981 act',
     'Rates cut by about a quarter over three years · A 1.25 percent rate reduction credit for 1981, then new tables for 1982 and after · The highest bracket fell from 70 percent to 50 percent',
     "Give students this figure as the program in one pair of numbers. Before the act, the highest federal income tax rate stood at 70 percent, where it had stood, with brief changes, since the Second World War; a dollar earned at the top margin kept thirty cents. The Economic Recovery Tax Act brought the top rate to 50 percent in its new rate tables, the last line of the 1982 table for joint returns taxing income over $85,600 at 50 percent of the excess. The cut was phased in: a rate reduction credit of 1.25 percent against taxes for 1981, then the new tables for 1982, 1983, and after 1983, each lower than the last. Supply-side theorists argued the rate itself was the policy: at 70 percent, effort and investment fled into shelters; at 50 percent, they would return to productive use. Critics answered at the time that the cut delivered its largest dollar amounts to the highest earners and that the revenue it surrendered would return as deficits. Both arguments are on the record of 1981, and section E weighs the second one against the debt figures.",
     kick='B · The Economic Program')

# ------------------------------------------------------ 10 VOLCKER
content_text("The other half: Volcker's Federal Reserve",
             ['Interest rates held above 19 percent',
              'The recession of 1981 to 1982',
              'Unemployment reaches 10.8 percent',
              'Inflation falls below 4 percent by 1983'],
             "The tax cut was only half the economic story of the first term, and the other half was not the president's to command. The Federal Reserve, under Chairman Paul Volcker, an appointee of President Carter whom Reagan kept, set out to break inflation by holding interest rates above 19 percent, a level at which borrowing for houses, cars, and plant nearly stopped. The cost was the deepest recession since the 1930s, running from the summer of 1981 to November 1982, with unemployment reaching 10.8 percent in the autumn of 1982, the highest rate since the Great Depression, on the figures of the Bureau of Labor Statistics. The administration held its course and its chairman through the recession, taking the political damage in the midterm elections of 1982. The reward came in the figures that followed: inflation, above 13 percent in 1980, fell below 4 percent by 1983, and the long recovery began.",
             kick='B · The Economic Program', size=24)

# ------------------------------------------------------ 11 STAT 10.8
stat('10.8%', 'unemployment at the depth of the recession, autumn 1982',
     'Bureau of Labor Statistics · The highest rate since the Great Depression · Inflation fell from above 13 percent in 1980 to below 4 percent by 1983',
     "Pause on this figure, because it is the price tag of the era's central economic achievement, and students should be able to say who paid it. In the autumn of 1982, at the depth of the recession the Federal Reserve's interest rates had induced, 10.8 percent of the American work force was unemployed, about twelve million people, concentrated in the industrial states whose factory towns Lesson 1 described. The rate is the Bureau of Labor Statistics figure, and it was the highest since the Great Depression. The administration's political position fell with the economy in 1982, when its party lost seats in the House. What the high rates bought was the end of the inflation that had defined the 1970s: from above 13 percent in 1980 to below 4 percent by 1983. The recovery that began in November 1982 ran for the rest of the decade, and the coalition of the next section was built on its first two years.",
     kick='B · The Economic Program')
print('part 2 slides done')
# ------------------------------------------------- 12 SECTION C DIVIDER
divider_text('Section C', 'PATCO: Labor\'s Terms Rewritten',
             'One week in August 1981 that unions and employers both remembered.',
             "This section covers the single most retold week of the administration's first year, and its facts are short enough to state whole. The Professional Air Traffic Controllers Organization, the union of the federal controllers who staffed the nation's towers and control centers, had negotiated through the spring of 1981 and rejected the administration's contract offer. Its demands, a ten thousand dollar raise, a shorter work week, and a better retirement package, went far beyond what other federal workers were offered. On the morning of August 3, 1981, about thirteen thousand controllers struck. Federal law forbade the strike, and the president, himself a former union president from his years leading the Screen Actors Guild, answered within hours. What he did, and the terms on which he did it, occupy the next two slides.")

# ------------------------------------------------------ 13 PATCO STORY
content_text('48 hours to report back',
             ['About 13,000 controllers strike, August 3, 1981',
              'The president reads their sworn oath aloud',
              'Return within 48 hours, or forfeit their jobs',
              'August 5: more than 11,000 are fired'],
             "Read the ultimatum as a piece of argument, the way the activity asks students to do. The president's statement to reporters on August 3 built its case in steps. First, the law: Congress had passed a law forbidding strikes by government employees against the public safety. Second, the oath: each controller, on taking the job, had sworn an affidavit that he was not participating in any strike against the Government of the United States or any agency thereof, and would not so participate while an employee. Third, the consequence: those who failed to report for duty were in violation of the law, and if they did not report for work within 48 hours, they had forfeited their jobs and would be terminated. When the deadline passed on August 5, the administration fired the more than 11,000 who had not returned, barred them from federal service, and kept the air system running with supervisors, non-striking controllers, and military controllers at reduced capacity.",
             kick='C · PATCO', size=24)

# ------------------------------------------------------ 14 STAT 48
stat('48 hours', 'the ultimatum of August 3, 1981',
     'More than 11,000 controllers fired on August 5 · PATCO decertified that October · The ban on rehiring the fired controllers was lifted in 1993',
     "The number to hold is the shortness of the deadline. Forty eight hours converted a labor dispute into a test of whether the president's word was a fact, and both sides understood it in those terms. When the hours ran out, the administration carried the firings through: more than eleven thousand controllers lost their jobs and were barred from federal service, a bar that stood until President Clinton lifted it in 1993, after which only a small number of the fired controllers returned to the towers. In October 1981 the Federal Labor Relations Authority decertified PATCO, and the union that had called the strike ceased to exist. The read of the episode by the people who watched it closest is the lesson's point. Unions took the firings as a signal that strike protection had thinned; employers, public and private, took them as permission to plan for permanent replacements, and did so through the decade.",
     kick='C · PATCO')

# ------------------------------------------------- 15 SECTION D DIVIDER
divider_text('Section D', 'The Coalition Held and Widened',
             'Recovery converts the voters of the other party.',
             "The revolution's political foundation widened in the recovery, and this short section explains the electorate the rest of the unit will keep meeting. Reagan's original coalition, assembled in Lesson 1 out of the tax revolt, the New Right's organizations, and the South and West, was joined in office by voters the coalition's builders had not organized: working Democrats in the industrial states, many of them union members, who crossed party lines for the president while often keeping their party registration. Political observers named them Reagan Democrats, and the guided notes definition of the term is one of the lesson's seven. Their crossing is the human fact behind the reelection figures on the next slide, and it set the pattern both parties studied for a generation: a presidential candidate could hold a working majority that his party's congressional candidates could not.")

# ------------------------------------------------------ 16 REAGAN DEMOCRATS
content_photo('reagan-port.jpg', 'Reagan Democrats, and 49 states',
              ['Recovery runs strong through 1983 and 1984',
               'Working and union voters cross party lines',
               '1984: reelected carrying 49 states',
               'Morning in America is the campaign\'s claim'],
              "The photograph shows President Reagan taking the oath of office on the west front of the Capitol on January 20, 1981, in a National Archives photograph: Nancy Reagan stands beside him in red, Chief Justice Warren Burger administers the oath, and Vice President George H. W. Bush watches from behind the glass. The recovery that began in November 1982 ran strong through 1983 and 1984, with growth high, inflation low, and unemployment falling from the 10.8 percent of the recession's depth. The political harvest was gathered in November 1984. Reagan Democrats, the traditionally Democratic voters, often white working class or union voters, who voted for Reagan in 1980 and 1984 while often remaining Democrats, crossed in numbers large enough to carry states their party had owned, and the president was reelected carrying 49 states against former Vice President Walter Mondale, losing only Mondale's Minnesota and the District of Columbia. The campaign's best known advertisement gave the coalition its slogan, the claim that it was morning again in America.",
              kick='D · The Coalition Held and Widened')

# ------------------------------------------------- 17 SECTION E DIVIDER
divider_text('Section E', 'The Limits of the Revolution',
             'The entitlements stand, the debt triples, and the judges remain.',
             "Every revolution should be graded against its own program, and this section grades this one against the promises of section A. The administration had promised to curb the federal establishment and to end the piling of deficit upon deficit. What the record shows instead is a government redirected rather than shrunk: taxed less, regulated more loosely, staffed with its appointees, and financed by borrowing on a scale no peacetime administration had attempted. The section's three exhibits are the debt figures, the survival of Social Security and Medicare, and the quiet tax increase of 1982, and its counterweight is the judiciary, the one arena in which the administration's changes were designed from the start to outlast it. Students who can state both the exhibits and the counterweight have the lesson's argument; students who can state only one side have a slogan.")

# ------------------------------------------------------ 18 LIMITS
content_text('What the record shows by 1989',
             ['The deficit grows year by year',
              'Social Security and Medicare left in place',
              'A 1982 tax increase reclaims part of the 1981 cut',
              'Judges appointed across the federal courts'],
             "State the limits in the record's own terms. The tax cuts, the military buildup, and the recession together reduced federal revenue, and spending was not cut to match, so the federal deficit grew year by year. The entitlement core of the New Deal and Great Society order, Social Security and Medicare, was left in place; an early proposal to reduce Social Security benefits was withdrawn in the face of congressional opposition, and the administration did not return to it. In 1982 the administration accepted the Tax Equity and Fiscal Responsibility Act, a tax increase that quietly reclaimed part of the 1981 cut it had celebrated the year before. What the revolution changed least in the statute books it changed most durably in personnel. Reagan appointed judges across the federal courts, among them Sandra Day O'Connor in 1981, the first woman on the Supreme Court, and the courts became the revolution's longest lasting instrument, still ruling on its premises after its statutes were amended.",
             kick='E · The Limits of the Revolution', size=24)

# ------------------------------------------------------ 19 STAT DEBT
stat('$2.9 trillion', 'the national debt by 1989',
     'From about $900 billion in 1981 · The debt more than tripled under a president elected against deficits',
     "This is the figure section A promised to watch. The national debt stood at about nine hundred billion dollars when Reagan took office, the accumulated borrowing of two centuries, two world wars, a depression, and the Great Society. By 1989, when he left, it stood at about 2.9 trillion dollars, more than tripled in eight years of peace and recovery. The arithmetic behind the figure is the section's argument in miniature: the 1981 tax act reduced revenue on purpose, the military buildup raised spending on purpose, and the entitlement core that dominated domestic spending was left in place on purpose, after Congress refused the one early attempt to touch Social Security. What remained was the deficit, the amount by which each year's spending exceeded the year's revenue, added each year to the debt. Later arguments about the era begin here, with supporters crediting the borrowing with growth and defense, and critics charging that the revolution financed itself with the future it had promised to unmortgage.",
     kick='E · The Limits of the Revolution')

# ------------------------------------------------- 20 SECTION F DIVIDER
divider_text('Section F', 'Iran-Contra: The Breach',
             'A foreign policy run off the books meets its investigators.',
             "The era's largest scandal began as two policies the administration held in public and contradicted in private. Publicly, the United States would make no concessions to terrorists and enforced an arms embargo on Iran; publicly, Congress had barred American military aid to the Contra rebels fighting Nicaragua's government. Between 1985 and 1986, officials of the administration sold arms to Iran in hope of freeing American hostages held in Lebanon, and proceeds of the sales were diverted to the Contras. The affair was exposed in November 1986, first by a Lebanese magazine's account of the arms dealing and then by the Attorney General's disclosure of the diversion. This section teaches the affair through the judgment the president's own investigators delivered, the Tower Commission report of February 1987, which students read in the activity.")
print('part 3 slides done')
# ------------------------------------------------------ 21 TOWER FINDINGS
content_text('What the Tower Commission found',
             ['Case studies in the perils of policy outside orderly process',
              'Procedures ignored, reviews too infrequent',
              'Congress was never notified',
              'No evidence the president knew of the diversion'],
             "Teach the Tower findings in the report's own order, and keep its two judgments distinct, because students habitually merge them. The first judgment is about the policy: the arms transfers to Iran ran directly counter to the administration's own policies on terrorism, the Iran-Iraq war, and military support to Iran, and the Board called the affair a case study in the perils of policy pursued outside the constraints of orderly process. The second judgment is about the process: established procedures for making national security decisions were ignored, reviews by the National Security Council principals were too infrequent, and in all of this process Congress was never notified. The Board's judgment on the president was double. It found no evidence that he was aware of the diversion of proceeds to the Contras, and it held that he should have insured the system did not fail him, that he never insisted on the critical review and accountability the operation required.",
             kick='F · Iran-Contra', size=24)

# ------------------------------------------------- 22 SECTION G DIVIDER
divider_text('Section G', 'The Other Wars, and the Consoler',
             'Drug sentences and an epidemic at home, and one evening of national mourning.',
             "The lesson closes with the parts of the Reagan record that fit neither the program nor the limits, and it teaches them under the discipline this unit applies to every contested subject: claims attributed to their makers, and the record stated at the precision the evidence supports. The War on Drugs expanded through the decade, with mandatory sentences written into the Anti-Drug Abuse Act of 1986 as crack cocaine spread, and the prison population rose steeply behind it. The AIDS epidemic, first identified in 1981, killed tens of thousands of Americans in the same years, and the argument over the administration's answer to it is stated on the next slide as an argument, with each side's evidence named. The section then turns to the presidency's other register, the consoler's, on the evening of January 28, 1986.")

# ------------------------------------------------------ 23 OTHER WARS
content_text('Drugs and AIDS: the argued record',
             ['Mandatory sentences in the Anti-Drug Abuse Act of 1986',
              'The prison population rises steeply',
              'AIDS identified in 1981; tens of thousands dead by decade\'s end',
              'Koop\'s 1986 report describes the disease plainly'],
             "Take the two subjects in turn and keep the attribution discipline in front of the class. The War on Drugs is the campaign of intensified drug enforcement and mandatory sentences pursued by the federal government from the 1970s onward and greatly expanded in the 1980s, which raised prison populations across the country. Its legislative peak in this lesson is the Anti-Drug Abuse Act of 1986, passed in the alarm over crack cocaine, which wrote long mandatory minimum sentences into federal law, with penalties for crack set far heavier than for the same weight of powder cocaine. On AIDS, the attributed record runs this way. Activists charged that the administration answered the epidemic slowly, pointing to the president's public silence on the disease in its first years. The administration pointed to rising federal spending on research and treatment and to the 1986 report of Surgeon General C. Everett Koop, which described the disease to the public in plain terms and recommended education rather than quarantine. The lesson records both charges and grades neither.",
             kick='G · The Other Wars, and the Consoler', size=23)

# ------------------------------------------------------ 24 CHALLENGER
content_photo('crew-port.jpg', 'January 28, 1986: the consoler',
              ['Ronald McNair, mission specialist, one of the seven',
               'Christa McAuliffe, a schoolteacher, among them',
               'The State of the Union postponed that evening',
               'The future belongs to the brave'],
              "The photograph is the NASA portrait of Ronald McNair, a physicist and mission specialist on the Challenger crew, in his flight suit, with a model of the shuttle behind him. The seven who died on January 28, 1986 were Commander Dick Scobee, Pilot Mike Smith, mission specialists Judy Resnik, Ellison Onizuka, and Ronald McNair, payload specialist Greg Jarvis, and Christa McAuliffe, the New Hampshire schoolteacher chosen to fly as the first teacher in space. The shuttle broke apart shortly after launch, in view of a national audience that included schoolchildren watching for McAuliffe. That evening the president postponed his State of the Union address and spoke as consoler. The address mourned the seven as pioneers, spoke to the schoolchildren who had watched, and committed the program to continue in the sentence students read in the activity: the future doesn't belong to the fainthearted; it belongs to the brave.",
              kick='G · The Other Wars, and the Consoler')

# ------------------------------------------------------ 25 GLANCE
s = slide(NAVY)
kicker(s, 'The revolution at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Claimed, enacted, limited, breached', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The mandate', 'Government is the problem, January 20, 1981', 'A governing claim, stated whole'),
        ('The program', 'Tax rates cut, top rate 70 to 50; inflation broken', 'Law and interest rates, 1981 to 1983'),
        ('The terms and coalition', 'PATCO fired; Reagan Democrats; 49 states', 'The era\'s terms, ratified in 1984'),
        ('The limits and breach', 'Debt to $2.9 trillion; entitlements stand; Tower report', 'The record the promise must answer')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, The Revolution at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The four rows are the lesson's argument in order. The mandate covers the inaugural claim of January 20, 1981 and its promises. The program covers the Economic Recovery Tax Act, deregulation, and the Volcker recession that broke inflation at 10.8 percent unemployment. The terms and coalition covers the PATCO firings of August 1981, the Reagan Democrats, and the 49 state reelection of 1984. The limits and breach covers the debt's rise to about 2.9 trillion dollars, the standing entitlements, the 1982 tax increase, the judicial appointments, and the Tower Commission's findings of February 1987. Grade the table generously on wording and strictly on the sorting.")

# ------------------------------------------------------ 26 VOCAB A
vocab('Words for the program',
      [('supply-side economics', 'cut rates and regulation to grow the economy'),
       ('deregulation', 'removing or loosening government rules on an industry'),
       ('Reagan Democrat', 'a Democrat who voted for Reagan in 1980 and 1984'),
       ('PATCO strike', 'August 1981: more than 11,000 controllers fired')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. " + joined('supply-side economics') + ". " + joined('deregulation') + ". " + joined('Reagan Democrat') + ". " + joined('PATCO strike') + ". Teach the four as the program's working vocabulary: the theory, the method, the voter it created, and the act that announced its terms.")

# ------------------------------------------------------ 27 VOCAB B
vocab('Words for the limits and the breach',
      [('federal deficit', 'a year\'s spending beyond the year\'s revenue'),
       ('Iran-Contra affair', 'arms to Iran, proceeds to the Contras, 1985 to 1987'),
       ('War on Drugs', 'intensified enforcement and mandatory sentences')],
      "Three more terms, again matching the guided notes exactly. " + joined('federal deficit') + ". " + joined('Iran-Contra affair') + ". " + joined('War on Drugs') + ". Keep the pairing in view for review: the deficit is the arithmetic of section E, the affair is the breach of section F, and the drug war is the domestic campaign of section G that outlasted the administration that expanded it.")

# ------------------------------------------------------ 28 SYNTHESIS
s = slide(NAVY)
kicker(s, 'The lesson in one view')
text(s, 0.9, 1.28, 11.5, 1.0, 'Changed, and left standing', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Changed', 'Tax rates, regulation, labor terms, and the courts'),
        ('Broken', 'Inflation, from above 13 percent to below 4'),
        ('Left standing', 'Social Security, Medicare, and a growing debt'),
        ('Exposed', 'A secret foreign policy, judged by its own commission')]
yy = 2.78
for t, d in rows:
    text(s, 0.9, yy, 2.4, 0.7, t, size=24, color=RUST_LT, font='Georgia')
    text(s, 3.45, yy + 0.05, 9.0, 0.9, d, size=19, color=CREAM, leading=1.2)
    yy += 1.05
notes(s, "Use this slide to close the argument before the work begins, and make students say the four rows aloud in order, because the pairing is the lesson. Changed: the direction of tax policy, with rates cut by about a quarter and the top rate brought from 70 percent to 50 percent; the regulatory stance of the government; the terms of labor conflict after August 1981; and the federal judiciary, restocked by appointment. Broken: the inflation of the 1970s, ended by the Federal Reserve's rates through a recession that put unemployment at 10.8 percent. Left standing: the entitlement core of Social Security and Medicare, and a federal establishment financed by a debt that rose from about 900 billion dollars to about 2.9 trillion. Exposed: a foreign policy run in secret against the administration's own stated policies and a congressional ban, judged in February 1987 by the commission the president himself had appointed.")

# ------------------------------------------------------ 29 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['What did the Reagan administration change about what the federal government did, and what did it leave in place? Build the ledger before you judge the revolution.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Revolution Ledger: five stations, a ledger, and a verdict'),
        ('Notebook', 'Notebook page: six moves in the record, claim to breach'),
        ('Quick check', 'The Promise and the Ledger: the inaugural against the figures'),
        ('Writing', 'Changed, and Left Standing: the lesson question as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the inaugural claim with the act of 1981, one change and one survival with figures, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Revolution Ledger, puts five stations in front of students: the first inaugural, the Economic Recovery Tax Act, a PATCO record built from the president's own statement, the Tower Commission report, and the Challenger address, and it ends with a ledger and a verdict on which single act changed the government's work most durably, defended against the strongest rival entry. The notebook page asks students to chart six moves in the record. The quick check sets the inaugural's warning against the debt figures. The writing task turns the lesson question into an essay argued from the evidence bank, closing with a judgment on the deepest change. The exit ticket has three parts: the inaugural claim with the act that carried it, one change and one survival with a figure each, and the lesson question in two or three sentences. Next lesson takes the Cold War's end as it landed at home.")

dc.save(OUT)
