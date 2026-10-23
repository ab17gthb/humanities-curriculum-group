#!/usr/bin/env python3
"""The Twenties Lesson 5 deck, "The Noble Experiment," built to the approved
Gilded Age and Progressive Era pilot system: image-led slides, fragments only
on screen, comprehensive speaker notes, full lesson + vocabulary coverage.
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
OUT = os.path.join(HERE, '..', 'lesson-05-slides.pptx')

def vocab(title, terms, note, kick='The vocabulary'):
    s = slide(CREAM)
    kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95, 11.5, 1.0, title, size=30, color=NAVY, font='Georgia')
    yy = 2.05
    for term, dfn in terms:
        text(s, 0.9, yy, 3.9, 0.9, term, size=24, color=NAVY, font='Georgia')
        text(s, 5.0, yy + 0.04, 7.5, 1.3, dfn, size=17, color=MUTED, leading=1.18)
        yy += 1.48
    notes(s, note)
    return s

# ---------------------------------------------------------------- 1 · TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'THE TWENTIES · LESSON 5', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Noble Experiment', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Why a constitutional ban on liquor built an illegal industry instead', size=17, color=POWDER)
notes(s, "The photograph, taken about 1921 in New York City, shows agents pouring a barrel of seized liquor into a street sewer while Deputy Police Commissioner John A. Leach, in the suit and straw hat at the right, watches beside a uniformed officer. Hold the class on that scene for a moment, because it contains the whole lesson in one frame. The government could find liquor, seize it, and destroy it in public. What it could not do, at any point in thirteen years, was make the next barrel stop coming. President Herbert Hoover would later call Prohibition a noble experiment, and the title of this lesson keeps his phrase while testing it. Students should leave today able to explain, with numbers, why enforcement failed, and to name what the law built in place of the saloon: speakeasies, supply chains, syndicates, corrupted officials, and finally a coalition strong enough to repeal a constitutional amendment.")

# ------------------------------------------------- 2 · LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('Why did Prohibition fail to stop drinking, and what did it build instead?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the prosperity of the 1920s change American life, and why was that prosperity weaker than it looked?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question has two halves, and students must answer both to earn the point. The first half asks why the ban failed on its own terms: the law aimed at a permanent end to the liquor traffic, and drinking continued. The second half is the Twenties question underneath the first. What did the law build instead? The answer is an industry, with capital, workers, territory, and protection, plus a new social institution, the speakeasy, and a new politics, the repeal coalition. Keep both halves visible all hour. A student who says only that people kept drinking has named the failure and missed the construction, which is where this lesson connects to the unit question. The prosperity of the 1920s looked solid from a distance. This lesson studies one place where it rested on an illegal economy that the Constitution itself had created, staffed, and made profitable for thirteen years.")

# --------------------------------------------------- 3 · THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'A ban, a gap, an industry', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'A law inherited from the war years', 'An amendment, an act, and a 0.5 percent line'),
        ('B', 'Too much ground, too few agents', 'About 1,500 agents for 110 million people'),
        ('C', 'Drinking moved. It did not stop.', 'The saloon closed, the speakeasy opened'),
        ('D', 'The supply business', 'Smugglers, stills, trucks, and Capone'),
        ('E', 'Violence and corruption as costs', 'No courts, so guns and bribes did the work'),
        ('F', 'A divided verdict, a repeal coalition', 'Wickersham hesitates, Sabin organizes')]
yy = 2.72
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=23, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=20, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=16, color=POWDER)
    yy += 0.70
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A states the law itself: an amendment ratified in 1919, an enforcement act, and a definition that banned beer and wine along with whiskey. Section B does the arithmetic of enforcement, and its numbers are the spine of the lesson. Section C follows the drinkers, who changed address rather than habits. Section D follows the sellers, who built supply chains and, in Chicago, a syndicate. Section E prices the system in violence and bribery. Section F records the verdict: a federal commission that documented the failure and still hesitated, and a repeal coalition that did not. The final table in the guided notes, The Ledger at a Glance, asks students to sort the whole lesson into what the law achieved, what it cost, and what it built.")

# ------------------------------------------------- 4 · SECTION A DIVIDER
divider_photo('volstead-port.jpg', 'Section A', 'A Law Inherited from the War Years',
              ['Prohibition arrived in the 1920s', 'as a finished law, not a proposal'],
              "The image is the first page of the enrolled National Prohibition Act, the Volstead Act, passed on October 28, 1919, held by the National Archives. Point out to students that they are looking at the machinery, not the idea. The Eighteenth Amendment stated the ban in a few lines and defined nothing. This act, hundreds of clauses long, supplied the definition, the permits, the penalties, and the exceptions, and it is where the real shape of Prohibition was decided. Two facts frame the section. First, the timing: the amendment was ratified in January 1919, in the closing months of the First World War era, and the ban took effect in January 1920, so the Twenties inherited a law they had not debated as a decade. Second, the politics: Congress passed this act over the veto of President Woodrow Wilson, which tells students the dry coalition in Congress was strong enough to override a president of its own wartime government.",
              title_size=40)

# ------------------------------------------------------ 5 · A FINISHED LAW
content_text('The ban arrived finished',
             ['Eighteenth Amendment ratified January 1919',
              'Manufacture, sale, and transportation banned for beverage purposes',
              'The ban took effect in January 1920',
              'Volstead Act of 1919: the enforcement machinery, passed over Wilson\u2019s veto'],
             "Give students the sequence slowly, because the guided notes test the order and the dates. The Eighteenth Amendment, ratified in January 1919, declared that after one year the manufacture, sale, and transportation of intoxicating liquors for beverage purposes would be prohibited across the United States. In January 1920, the ban took effect. Congress supplied the enforcement machinery in the Volstead Act of 1919, passed over President Woodrow Wilson's veto. In the guided notes definition, Prohibition is the nationwide ban on the manufacture, sale, and transportation of intoxicating liquor for beverage purposes, in force under the Eighteenth Amendment from 1920 to 1933, and students will meet that definition again on the vocabulary slides. Stress the word finished. Nobody in 1920 was voting on whether to try this. The argument of the decade was never whether the law should exist in theory. It was what the law, as actually written and actually staffed, did to the country that lived under it.",
             kick='A · A law inherited from the war years')

# ------------------------------------------------------ 6 · THE 0.5 PERCENT LINE
content_text('The 0.5 percent line',
             ['Intoxicating liquor: 0.5 percent or more alcohol by volume',
              'Beer and light wine banned along with whiskey and gin',
              'Many voters had not expected that reach',
              'Exceptions by permit: medicine, religious wine, industrial alcohol',
              'Each permit opened a channel illegal sellers learned to use'],
             "This slide carries the drafting decision that shaped the whole decade, so take it step by step. The act defined intoxicating liquor as any beverage containing 0.5 percent or more alcohol by volume. That low line banned beer and light wine along with whiskey and gin, which many voters had not expected. A law sold as a weapon against the saloon and hard liquor now covered the beer of working class and immigrant drinkers, and the enforcement problem grew by millions of ordinary customers. Then note the other side of the drafting. The act allowed narrow exceptions, including liquor prescribed by a doctor, wine for religious services, and alcohol for industrial use. Each exception required permits, and each permit opened a channel that illegal sellers soon learned to use. The law therefore did two things at once: it widened the ban beyond its stated target, and it punched legal holes through which the illegal trade would later flow.",
             kick='A · A law inherited from the war years', size=24)

# ------------------------------------------------- 7 · SECTION B DIVIDER
divider_photo('pouring-port.jpg', 'Section B', 'Too Much Ground, Too Few Agents',
              ['One truck, one boat, or one still', 'could supply hundreds of customers'],
              "The photograph is a portrait crop of the title image: agents pouring seized liquor into a New York City sewer, about 1921, while Deputy Police Commissioner John A. Leach watches at the right. Use it to pose the section's problem before any numbers appear. A public destruction like this one was enforcement at its most visible and its most honest: the liquor in that barrel would never be sold. But destruction photographs answer the wrong question. The question is not whether agents could seize liquor. They seized it constantly, all decade, in every city. The question is whether seizures could outrun supply, and section B answers with arithmetic. One truck crossing from Canada, one boat waiting offshore, or one hidden still could supply hundreds of customers, while each seizure required agents, warrants, raids, and prosecutions that moved at government speed. The arithmetic favored the lawbreaker from the first day, and the next three slides prove it with the bureau's own figures.",
              title_size=38)

# ------------------------------------------------------ 8 · A SMALL FORCE
content_photo('raid-port.jpg', 'A small force, a huge map',
              ['Prohibition Bureau: roughly 1,500 agents at the start, an estimate',
               'More than 110 million people to police',
               'Thousands of miles of border and coastline',
               'Permit holders to inspect, breweries and stills to raid'],
              "The photograph shows three Indianapolis police officers posed with a seized copper still, its pipe, rows of stoneware jugs, and a sack of sugar after a raid on December 9, 1920, in the first year of the ban. Everything in the picture had to be found, carried out, and cataloged by hand, which is the daily reality behind the numbers on this slide. Enforcement fell to a small federal force. At the start, the Prohibition Bureau had roughly 1,500 agents, an estimate that grew only slowly, to police more than 110 million people. Agents guarded thousands of miles of border and coastline, inspected permit holders, and raided breweries and stills. Teach the ratio as the fact of the section: one agent for roughly every seventy thousand people, before a single sick day, transfer, or bribe is counted. Students should write the two guided notes figures, 1,500 and 110 million, and keep the word estimate attached to the first one, because the reading attaches it.",
              kick='B · Too much ground, too few agents')

# ------------------------------------------------------ 9 · AGENT STAT
stat('1,500', 'federal agents at the start, by estimate',
     'To police more than 110 million people, thousands of miles of border and coastline, and every permit, brewery, and still in between. The force grew only slowly.',
     "Dwell on the two numbers together, because their relationship is the argument. The reading gives the Prohibition Bureau roughly 1,500 agents at the start and a national population of more than 110 million people, and it labels the agent figure an estimate that grew only slowly. Keep that label on the number whenever students use it: the bureau's early records do not support a false precision, and honest estimates are a habit this course grades. Now run the comparison that makes the ratio real. A single city police department of the era fielded thousands of officers for one city. The federal government assigned a force of that order to the entire country, its Canadian and Mexican borders, both coastlines, its permit system, and its courts. No increase in effort could close a gap written at that scale. The next slide shows what filled the gap instead: state governments that walked away, and agents whose pay invited the bribes the trade could easily afford.",
     kick='B · Too much ground, too few agents')

# ------------------------------------------------------ 10 · STATES WALK AWAY
content_photo('destroying-port.jpg', 'States walk away, agents sell out',
              ['State help varied widely from the start',
               '1923: New York repealed its state enforcement act',
               'Federal agents left to work alone there',
               'Pay was low beside the money offering bribes',
               'The bureau dismissed hundreds of agents for corruption'],
              "The photograph, dated November 20, 1923, shows liquor being destroyed, one of a series the Library of Congress holds from that year. Use its date, because 1923 is the hinge of this slide. Enforcement had been designed as a partnership, with states passing their own acts behind the federal one. State help varied widely. Some states funded their own enforcement laws. New York repealed its state act in 1923 and left the federal government to work alone in the largest market in the country. Inside the bureau, a second failure compounded the first. Agents were poorly paid, and the work placed them beside people who could pay far more for cooperation than the government paid for honesty. The bureau dismissed hundreds of agents for corruption, and dismissals removed only the cases it could prove. Students should see the system, not a few bad men: low pay, huge temptation, and a small force made corruption a predictable cost of the design, priced into the trade from the start.",
              kick='B · Too much ground, too few agents', )

# ------------------------------------------------- 11 · SECTION C DIVIDER
divider_text('Section C', 'Drinking Moved. It Did Not Stop.',
             'The legal saloon closed, and drinking changed its address.',
             "Pause on the section title, because it is the reading's own sentence and the exit ticket rewards students who can defend it. The legal saloon closed: that part of the law worked exactly as written, and the licensed, inspected, taxable saloon of 1919 never came back in its old form. What the law could not close was demand. Drinking changed its address. It moved behind locked doors, into back rooms and basements, into private homes and hip flasks, and each new address came with worse oversight than the saloon had ever had. A saloon kept hours, answered to a license, and could be inspected. A speakeasy answered to whoever protected it. Tell students to watch section C for the honest complication the reading insists on: drinking did fall, sharply, at first, above all among drinkers who could not pay illegal prices, and a serious answer to the lesson question has to hold that fall and the later climb in the same paragraph.")

# ------------------------------------------------------ 12 · THE SPEAKEASY
content_text('The saloon closed, the speakeasy opened',
             ['An illegal bar behind a locked door or a back room',
              'Men and women drank together in public',
              'The old saloon had served mostly men',
              'Drinking became fashion and defiance for young city residents'],
             "Define the replacement institution precisely. In the guided notes definition, a speakeasy is an illegal bar or club that sold liquor during Prohibition, often hidden behind a locked door or a legitimate business, and students will write that definition again on the vocabulary slides. In its place, the speakeasy stood where the saloon had stood, reached through a locked door or a back room, admitted by a password, a card, or a known face. Then teach the social change inside the room, because the reading treats it as one of the decade's real transformations. Inside, men and women drank together in public in a way the old saloon, which had served mostly men, had rarely allowed. Illegality had a glamour the license never gave it. Drinking became a mark of fashion and defiance for many young city residents, the opposite of the respect for law the amendment was supposed to teach the young.",
             kick='C · Drinking moved. It did not stop.')

# ------------------------------------------------------ 13 · SPEAKEASY STAT (CUSTOM)
s = slide(NAVY)
kicker(s, 'C · Drinking moved. It did not stop.')
text(s, 0.9, 1.55, 11.53, 2.2, 'Tens of thousands', size=64, color=CREAM, font='Georgia',
     align=PP_ALIGN.CENTER, space_after=0)
text(s, 0.9, 3.55, 11.53, 0.9, 'speakeasies said to fill New York City alone', size=30, color=CREAM, align=PP_ALIGN.CENTER, space_after=0)
text(s, 1.9, 4.75, 9.53, 1.4, 'An estimate, and the estimates vary widely. The reading gives no exact count, because no exact count exists for businesses built to stay uncounted.',
     size=20, color=POWDER, align=PP_ALIGN.CENTER, leading=1.3)
notes(s, "This slide is a lesson in handling numbers honestly, and it should be taught as one. Estimates vary widely: New York City alone was commonly said to hold tens of thousands of speakeasies. Note the grammar of that sentence and make students copy it. Commonly said is not counted. Nobody licensed these businesses, nobody taxed them, and their owners worked to keep them invisible, so no census of speakeasies exists and none can be constructed now. What the estimate still proves, even at its lowest retellings, is scale: a retail network large enough to replace the saloon in the largest city in the country, built within a few years of the ban, and stable enough that raided rooms reopened under new names within weeks. Pair this figure with the agent estimate from section B. One side of the contest can be estimated only loosely because it was illegal and uncounted. The other side was a federal bureau, and it still numbered only in the low thousands.")

# ------------------------------------------------------ 14 · IT FELL FIRST
content_text('It fell first, then climbed',
             ['Drinking fell sharply in the first years',
              'Working class drinkers priced out of the illegal market',
              'Deaths from cirrhosis of the liver dropped',
              'By mid-decade, consumption climbing again in the cities',
              'Home cider and juice, grape concentrate, doctors\u2019 prescriptions'],
             "This slide holds the fact that makes careless answers wrong, so slow down. Drinking fell sharply in the first years, above all among working class drinkers who could not pay illegal prices, and deaths from cirrhosis of the liver dropped. That is a real public health gain, and the reading states it without flinching. Students arguing for repeal must still answer it, and students arguing the law worked must then answer the second half. By mid-decade, consumption was climbing again in the cities. The supply had organized, prices had found their level, and the legal channels helped. The act permitted families to make fermented cider and fruit juices at home, and stores sold grape concentrate with warnings that read as instructions. Doctors wrote medicinal prescriptions in large numbers. The pattern to name is adaptation: the ban raised the price and changed the seller, and over time both drinkers and sellers adjusted to the new conditions faster than the bureau could adjust to them.",
             kick='C · Drinking moved. It did not stop.', size=24)

# ------------------------------------------------- 15 · SECTION D DIVIDER
divider_photo('still-port.jpg', 'Section D', 'The Supply Business',
              ['Smuggled, distilled, and trucked:', 'three routes to one glass'],
              "The photograph, dated October 6, 1922, shows four officials standing beside the kettles, condensing coils, jugs, and barrel of a confiscated still, with the equipment loaded behind them. Read the image as a business inventory rather than a trophy. A still like this one could be hidden in a barn or a basement, moved in a night, and rebuilt for a small sum, and the reading's point is that thousands of them ran at once. Section D follows the money through the trade the ban created. A bootlegger, in the term students will write at the end of the lesson, is a person who illegally made, transported, or sold liquor during Prohibition, and the section shows that single word splitting into an industry: smugglers at the borders, distillers in the countryside and the warehouse districts, distributors on the roads, and, at the top of the largest market in the Midwest, a Chicago organization run like the corporations this course studied in the Gilded Age unit.",
              title_size=44)

# ------------------------------------------------------ 16 · THREE ROUTES
content_text('Three routes to a glass',
             ['Smugglers: Canadian whiskey, the Detroit River, ships offshore',
              'Distillers: hidden stills in barns, basements, warehouses',
              'Distributors: trucks to speakeasies and buyers',
              'The price rose at every step',
              'Profit paid for trucks, bribes, and protection'],
             "Illegal liquor reached a glass by three main routes, and students should be able to walk a bottle through all three. Smugglers brought Canadian whiskey across the border and the Detroit River, and landed liquor from ships waiting offshore, beyond the reach of the law and rowed in at night. Distillers inside the country ran hidden stills in barns, basements, and warehouses. Distributors moved the product by truck to speakeasies and buyers. At every step the price rose, and the profit paid for trucks, bribes, and protection. Name what that structure is, because it prepares the next slide. A supply chain with specialized roles, rising margins, and overhead costs for transport and security is a business, whatever its legal standing. Prohibition did not abolish the liquor industry. It removed the industry's legal firms, its taxes, and its inspectors, and rebuilt the same functions underground, where the profit margin was higher because the risk and the ban itself had raised the price of every glass.",
             kick='D · The supply business')

# ------------------------------------------------------ 17 · CAPONE
content_photo('capone-port.jpg', 'Capone and the Outfit',
              ['Took over the organization Johnny Torrio built',
               'Territories across Chicago, breweries and stills',
               'Speakeasies, gambling, and racketeering income',
               'Contemporary income estimates: tens of millions a year, not verified'],
              "Say the dates of this photograph plainly, exactly as the lesson documents do. Wikimedia Commons dates this photograph to 1930, which is outside the 1920 to 1929 span of the lesson's main story, and the news bureau caption attached to the print is dated February 26, 1931. The photograph therefore shows Capone at the start of the federal prosecutions that ended his career, not during the 1920s years in which he built his organization. The organization itself is the subject. In Chicago, Al Capone turned the trade into a corporation in all but name. Capone took control of the organization built by Johnny Torrio, kept its division of the city into territories, and enlarged it. His organization, often called the Outfit, ran breweries and stills, managed speakeasies, and collected income from gambling and from racketeering. Contemporary estimates credited Capone with income in the tens of millions of dollars a year, a figure that cannot be verified, and students must keep that warning attached to the number.",
              kick='D · The supply business')

# ------------------------------------------------- 18 · SECTION E DIVIDER
divider_text('Section E', 'Violence and Corruption as Business Costs',
             'Illegal businesses cannot use courts, so they settle disputes with threats and guns.',
             "Frame this section with an accounting claim, because the reading makes one and the activity grades it. Violence and corruption in this story were not a breakdown of the illegal market. They were among its regular costs, budgeted like trucks and rent. A legal brewer whose shipment is stolen calls the police, sues the carrier, and collects insurance. An illegal brewer can do none of those things. His contracts cannot be enforced, his territory cannot be defended in court, and his merchandise is itself contraband, so every dispute his business meets has exactly two instruments available: payment or force. Corruption is the payment instrument, buying tolerance from the officials who could close him. Violence is the force instrument, used against rivals, hijackers, and witnesses. Students who grasp that logic can explain the decade's worst crime without treating it as a mystery, and the next slide gives them that crime in its full, documented form.")

# ------------------------------------------------------ 19 · NO COURTS, SO GUNS
content_text('No courts, so guns',
             ['Rival gangs fought over territory',
              'Competitors and witnesses killed',
              'February 14, 1929: seven men murdered in a Chicago garage',
              'The St. Valentine\u2019s Day Massacre',
              'No one was convicted; the public blamed Capone\u2019s organization'],
             "Illegal businesses cannot use courts to settle disputes, so they settle them with threats and guns. Rival gangs fought over territory and killed competitors and witnesses, and the reading asks students to see that violence as function, not frenzy: it performed the work courts perform for legal business. The example is the crime the decade is remembered for. On February 14, 1929, gunmen murdered seven men connected to the rival North Side gang in a Chicago garage, in the crime remembered as the St. Valentine's Day Massacre. No one was convicted, and the public widely attributed the killings to Capone's organization. Hold students to the precision of those two sentences. Attribution is not conviction, and the lesson keeps them separate on purpose. What is certain is the setting: a territorial war inside an illegal market, fought in a city where the largest liquor organization had divided the trade into territories and defended them the only way an outlaw business can.",
             kick='E · Violence and corruption as business costs', size=24)

# ------------------------------------------------------ 20 · CORRUPTION
content_text('Corruption was a share of the profit',
             ['An officer who ignored a speakeasy',
              'An agent who warned a brewer before a raid',
              'A politician who protected a distributor',
              'Honest citizens bought illegal liquor and served it to guests',
              'A constitutional amendment treated as a suggestion'],
             "Corruption worked the same way as violence, as a line in the budget rather than a failure of character in a few men. An officer who ignored a speakeasy, an agent who warned a brewer before a raid, or a politician who protected a distributor received a share of the profit the law had created. Follow the money one step further than the bribe itself. The profit existed because the ban had raised prices and outlawed the competition's legal rivals, so the law was, in effect, minting the money that bought its own enforcers. Then widen the lens to the customers, because the reading ends this section with them. Citizens who considered themselves honest bought illegal liquor and served it to guests, and showed their children that a constitutional amendment could be treated as a suggestion. That quiet lesson, taught at respectable dinner tables for thirteen years, is the cost the repeal movement would put at the center of its case in the next section.",
             kick='E · Violence and corruption as business costs')

# ------------------------------------------------- 21 · SECTION F DIVIDER
divider_text('Section F', 'A Divided Verdict and a Coalition for Repeal',
             'A commission documented the failure and hesitated. A coalition organized.',
             "By the end of the decade the argument had changed its subject. In 1920 the country argued about drink. By 1929 it argued about the law itself: whether a constitutional amendment that millions obeyed only in public could command respect, and what its enforcement was doing to police, courts, and city government. Section F holds the two answers the country produced, side by side, and students should feel how strange the pairing is. The official answer came from a presidential commission that gathered the evidence of failure in one report and then declined to act on it. The political answer came from the voters the dry coalition least expected to lose, organized women led by a former supporter of the ban. Teach the section as a study in evidence and courage: the commission had the facts and split. The coalition had the facts, a founder, and a membership, and it moved the country toward the only repeal of a constitutional amendment in American history.")

# ------------------------------------------------------ 22 · WICKERSHAM
content_text('Wickersham: the divided verdict',
             ['1929: Hoover appointed the Wickersham Commission',
              '1931 report: widespread evasion, corruption, contempt for the law',
              'Then it declined to recommend repeal',
              'Stronger enforcement instead, members disagreeing in separate statements',
              'One member: no alternative but repeal'],
             "In 1929 President Herbert Hoover appointed a commission chaired by George W. Wickersham to study the problem, and its 1931 report is the closest thing the era produced to an official verdict. The report documented widespread evasion, corruption, and contempt for the law, and then declined to recommend repeal, calling instead for stronger enforcement. Members filed separate statements that disagreed with one another, and one member concluded that there was no alternative but repeal. Walk students through the comedy and the seriousness of that outcome. The evidence chapters and the conclusion point in opposite directions, and newspapers of the day noticed. A government that had been shown, by its own commission, that a law was evaded, corrupting, and held in contempt answered that the law should be enforced harder, with the same bureau, the same borders, and the same arithmetic that sections B through E of this lesson have already examined. Ask students to hold the report beside their ledger before the next slide introduces the people who drew the other conclusion.",
             kick='F · A divided verdict and a coalition for repeal', size=24)

# ------------------------------------------------------ 23 · THE REPEAL COALITION
content_text('The repeal coalition',
             ['City voters, many of them immigrants, opposed the law from the start',
              'Business leaders: legal liquor would restore tax revenue',
              '1929: Pauline Sabin founded the Women\u2019s Organization for National Prohibition Reform',
              'Women expected to defend the dry cause argued hypocrisy and crime instead'],
             "By the early 1930s a repeal coalition had formed, and its membership is the news. City voters, many of them immigrants, had opposed the law from the start, and business leaders argued that legal liquor would restore tax revenue. Most striking of all, Pauline Sabin founded the Women's Organization for National Prohibition Reform in 1929. Women expected to defend the dry cause as home protection now argued that the law had produced hypocrisy and crime. Explain why Sabin's organization changed the politics rather than merely adding to them. The dry movement's strongest claim had been that women, as defenders of the home, stood behind Prohibition, and that repeal was the cause of brewers and saloon interests. An organization of women, founded by a former supporter, removed that claim. Close the lesson's argument here: Prohibition had reduced drinking at first. On its own stated terms, a permanent end to the liquor traffic, it had failed, and in place of the saloon it had built an illegal industry with its own capital, workforce, and hold on public officials.",
             kick='F · A divided verdict and a coalition for repeal', size=23)

# ------------------------------------------------------ 24 · THE LEDGER
s = slide(NAVY)
kicker(s, 'The ledger at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Achieved, cost, built', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Achieved', 'Drinking fell sharply at first', 'Cirrhosis deaths dropped'),
        ('Cost', 'Gang violence, seven dead in 1929', 'Routine corruption of officials'),
        ('Built', 'Speakeasies and supply chains', 'Syndicates and a repeal coalition')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.4, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.5, yy + 0.05, 4.6, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.3, yy + 0.05, 4.1, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, The Ledger at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The three rows are the lesson question cut into columns. What the law achieved is real and belongs in any honest answer: drinking fell sharply in the first years, and deaths from cirrhosis of the liver dropped. What the law cost is documented in section E: gang violence, including the seven murders of February 14, 1929, and the routine corruption of police, agents, and politicians. What the law built is the longest list: a speakeasy network counted in the tens of thousands in one city, smuggling and distilling supply chains, organized crime in syndicate organizations such as the Outfit, and the repeal coalition itself. Grade the table generously on wording and strictly on placement. An entry in the wrong column reveals a misunderstanding that the exit ticket will otherwise carry out of the room uncorrected.")

# ------------------------------------------------------ 25 · VOCAB A
vocab('Words for the law and the room it built',
      [('Prohibition', 'the nationwide ban on the manufacture, sale, and transportation of intoxicating liquor for beverage purposes, in force under the Eighteenth Amendment from 1920 to 1933'),
       ('Volstead Act', 'the National Prohibition Act of 1919, the federal law that enforced the Eighteenth Amendment and defined intoxicating liquor as any beverage containing 0.5 percent or more alcohol by volume'),
       ('bootlegger', 'a person who illegally made, transported, or sold liquor during Prohibition'),
       ('speakeasy', 'an illegal bar or club that sold liquor during Prohibition, often hidden behind a locked door or a legitimate business')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. Prohibition: the nationwide ban on the manufacture, sale, and transportation of intoxicating liquor for beverage purposes, in force under the Eighteenth Amendment from 1920 to 1933. Note the three verbs; the amendment banned a trade, not the act of drinking itself. The Volstead Act: the National Prohibition Act of 1919, the federal law that enforced the Eighteenth Amendment and defined intoxicating liquor as any beverage containing 0.5 percent or more alcohol by volume. The definition clause is the load bearing part. A bootlegger: a person who illegally made, transported, or sold liquor during Prohibition. One word covers the maker, the driver, and the seller of section D. A speakeasy: an illegal bar or club that sold liquor during Prohibition, often hidden behind a locked door or a legitimate business. The hiding is inside the definition, and it is why no count of speakeasies can ever be exact.")

# ------------------------------------------------------ 26 · VOCAB B
vocab('Words for the business and the ending',
      [('organized crime', 'criminal activity carried out by a structured group that operates like a business, with leaders, ranks, territory, and regular sources of income'),
       ('racketeering', 'the use of threats, violence, or a front business to extract money from businesses or workers, including forcing them to pay for protection or services they did not choose'),
       ('repeal', 'the cancellation of a law or constitutional amendment; the Twenty-first Amendment repealed the Eighteenth in 1933')],
      "Three more terms, again matching the guided notes exactly. Organized crime: criminal activity carried out by a structured group that operates like a business, with leaders, ranks, territory, and regular sources of income. Every element of that definition names something in the Outfit of section D, which is why the term fits Capone and a lone still operator does not earn it. Racketeering: the use of threats, violence, or a front business to extract money from businesses or workers, including forcing them to pay for protection or services they did not choose. The protection payment is the heart of it: the victim buys safety from the same organization that threatens him. Repeal: the cancellation of a law or constitutional amendment; the Twenty-first Amendment repealed the Eighteenth in 1933. Students should note the semicolon structure. The definition gives the general act first, then the single famous case, the only time one amendment has canceled another in American history.")

# ------------------------------------------------------ 27 · CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Why did Prohibition fail to stop drinking, and what did it build instead? Answer both halves, and include the early fall in drinking.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Enforcement Ledger: five stations, then build the ledger'),
        ('Notebook', 'Notebook page: rebuild the ledger at a glance in your own words'),
        ('Quick check', 'After the Raid: the law, the raid, and the numbers'),
        ('Writing', 'What the Law Built: the lesson question as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: why the 0.5 percent line widened the problem, two things the law built, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Enforcement Ledger, runs five stations in order: the law on paper, a raid, the business the law built, the dry appeal in Billy Sunday's own words, and the repeal pamphlet of the Women's Organization for National Prohibition Reform. Students then build the ledger the Wickersham Commission faced, two entries per column, each traced to its station. The notebook page asks them to rebuild the ledger at a glance themselves. The quick check, After the Raid, tests the law, the enforcement numbers, and the supply routes. The writing task, What the Law Built, turns the lesson question into an essay. The strongest essays will hold the whole arc: a ban wider than its target, a force too small and too exposed to enforce it, drinkers who moved rather than stopped, sellers who organized, and officials who were bought with the law's own profit. The exit ticket has three parts, ending with the lesson question answered in two or three sentences that include the early fall in drinking.")

dc.save(OUT)
