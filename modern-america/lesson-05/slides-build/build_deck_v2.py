#!/usr/bin/env python3
"""Modern America Lesson 5 deck, "A Changing America: Immigration, Cities,
and the Sun Belt," built to the approved system: image-led slides, fragments
only on screen, comprehensive speaker notes, full lesson + vocabulary
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
OUT = os.path.join(HERE, '..', 'lesson-05-slides.pptx')

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

def content_photo_s(img, title, items, note, kick=None, size=21):
    s = slide(CREAM)
    photo_right(s, img)
    if kick: kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95 if kick else 0.8, 6.9, 1.2, title, size=31, color=NAVY, font='Georgia', leading=1.05)
    frags(s, items, y=2.15 if kick else 2.0, w=6.9, size=size)
    notes(s, note)
    return s

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'MODERN AMERICA · LESSON 5', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'A Changing America', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Immigration, cities, and the Sun Belt, 1965 to 2020', size=17, color=POWDER)
notes(s, "The photograph shows President Lyndon B. Johnson signing the Immigration Act of 1965 on Liberty Island on October 3, 1965, photographed by Yoichi Okamoto for the Johnson Library, with the Statue of Liberty behind the signing party. It opens a lesson about how the United States remade its population and its map in the half century after 1965. Two movements did the work. The law of 1965 reopened immigration and changed its sources from Europe toward Latin America and Asia, raising the foreign born population from under five percent of the country to about thirteen percent. At the same time Americans themselves moved, from the older industrial cities of the North and Midwest toward the South and West, hollowing some cities, filling others, and carrying congressional seats with them in every census. Students should leave able to give the size of each movement in Census Bureau figures and to judge which force did most to redraw the map.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("How did the immigration opened in 1965 and the movement of Americans themselves remake the country's population and map by the twenty first century?", {})]],
     size=40, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the United States remake itself after 1980, in its economy, its population, and its place in the world, and what did the remaking settle and what did it leave open?', {'italic': True})]],
     size=16, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "The lesson question has two halves, and students should keep both in view all hour. The first half asks about immigration: a law passed in 1965, whose makers expected little change, admitted a new immigration that transformed the country's sources of newcomers and raised the foreign born share of the population to levels not seen since the early twentieth century. The second half asks about Americans in motion: the long movement from the industrial North and Midwest to the South and West, the hollowing of older cities as factories closed and families left for suburbs, and the partial revival of the strongest city centers from the 1990s. The two halves meet on the map. The unit question runs beneath as the frame: this lesson is the unit's account of a population remade, and the writing task at the end asks students to judge which of its three forces, the law, the Sun Belt economy, or the factories leaving, did most of the redrawing.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'A door reopened, a country in motion', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The door reopened', 'The 1965 act ends the quotas, builds preferences'),
        ('B', 'The transformation in the numbers', '4.7 percent in 1970, about 13 percent by 2010'),
        ('C', 'The settlement of 1986', 'Legalization joined to an employer ban'),
        ('D', 'A reckoning with an older wrong', 'Personal Justice Denied and redress, 1988'),
        ('E', 'Americans on the move', 'The Sun Belt rises, seats follow the movers'),
        ('F', 'The older cities hollowed', 'Detroit: 1.85 million to about 714,000'),
        ('G', 'Revival at the center', 'Gentrification, unevenly, from the 1990s')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Sections A through D cover immigration and its settlements: the 1965 act that ended the national origins quotas, the transformation of the foreign born population in the Census Bureau numbers, the 1986 act that legalized about three million people while banning the knowing hire of unauthorized workers, and the reckoning with the wartime internment of Japanese Americans that produced an apology and payments in 1988. Sections E through G cover the internal movement: the Sun Belt's rise and the reapportionment that followed it, the hollowing of the older industrial cities, with Detroit's two census figures as the record, and the partial revival of strong city centers through gentrification from the 1990s. Tell students the summary table at the end of their guided notes, The Map at a Glance, asks them to rebuild this map in their own words.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_photo('lbj-port.jpg', 'Section A', 'The Door Reopened',
              ['President Johnson signs the immigration act', 'at the foot of the Statue of Liberty, October 3, 1965.'],
              "The photograph, by Yoichi Okamoto of the Johnson Library, shows the signing on Liberty Island, a setting chosen for its symbolism. Open with the system the act replaced, because students cannot measure a change without its starting point. For four decades the national origins quota system had sorted immigrants by the country of their birth, with quotas computed from the national origins of the American population of an earlier census. It gave large quotas to northern and western Europe, small ones to most of the rest of the world, and almost none to Asia, and it held immigration low by design. By 1965 that sorting sat badly beside the civil rights argument the country had just settled at home, and Congress, with President Johnson's support, voted to end it. Note the date for the class: the quotas were phased out through a transition that ran to June 30, 1968, which is why the census of 1970 still shows the old system's low numbers.",
              title_size=40)

# ------------------------------------------------------ 5 SECTION A CONTENT
content_photo_s('lbj-port.jpg', 'What the 1965 act built',
             ['Quotas by national origin were abolished.',
              'A preference system took their place.',
              'Family reunification came first, then needed skills.',
              'Ceilings were set per hemisphere, at 20,000 per country.',
              'Immediate relatives were admitted outside the ceilings.',
              'Its supporters predicted little change.'],
             "Use the full guided notes definition here and have students check it in their notes: the Immigration and Nationality Act of 1965 is the law that ended the national origins quota system in place since the 1920s and opened American immigration chiefly to family reunification and needed skills, transforming the sources of immigration. Station 1 of the activity carries this act as a labeled summary record, and students should know why: the lesson summarizes the statute's operative provisions from the public record of Public Law 89-236 rather than quoting its text. Walk the machinery slowly. The act set ceilings, 170,000 a year for the Eastern Hemisphere with no more than 20,000 from any one country, and 120,000 for the Western Hemisphere from 1968. Inside the ceilings, preferences ran to family first and skills second. Outside the ceilings stood the category that decided everything: spouses, minor children, and parents of citizens, admitted without numerical limit.",
             kick='A · The door reopened')

# ------------------------------------------------- 6 SECTION B DIVIDER
divider_text('Section B', 'The Transformation in the Numbers',
             'The act\u2019s makers predicted a modest change. The census recorded a transformation.',
             "Section B is the numbers section, and its source should be named every time a figure is used: the United States Census Bureau, in its decennial censuses and the American Community Survey. In 1970, five years after the act and two years after the quotas fully ended, the foreign born share of the population stood at 4.7 percent, the lowest the bureau had recorded, because the quota system had restricted entry for four decades. Then the new system began to compound. Family reunification meant that each settled immigrant could sponsor relatives, and the sponsored relatives could in time sponsor their own, so admissions grew by connection rather than by quota. Refugees admitted under separate programs, from Cuba, Southeast Asia, and the Soviet Union, added to the flow, and workers recruited for needed skills added more. By 2010 the bureau counted about forty million foreign born residents. The next slides give the transformation its two measures, size and source.")

# ------------------------------------------------------ 7 SECTION B CONTENT
content_text('The sources changed with the size',
             ['In 1960 the largest groups came from Europe and Canada.',
              'By the 2000s the largest groups came from Mexico, the Philippines, India, China, and Vietnam.',
              'Family sponsorship compounded across decades.',
              'Refugees came from Cuba, Southeast Asia, and the Soviet Union.',
              'The United States held the largest immigrant population in absolute terms.'],
             "Teach the shift of sources as the act's deepest effect, deeper than the rise in numbers itself. In 1960, at the end of the quota era, the largest immigrant groups in the United States came from Europe and Canada, the countries the old system had favored. The preference system did not name new favored countries. It named relationships and skills, and relationships ran where earlier migration, war, and labor recruitment had already planted communities: to Mexico and the Philippines, to India and China, and to Vietnam after the war in Southeast Asia ended in 1975. By the 2000s the five largest immigrant groups came from those countries. One caution belongs in the lesson and on the record: the act's supporters had predicted that the ethnic mixture of immigration would stay much as it was, because they expected Europeans to use the family preferences most. The prediction failed because the family networks that grew fastest were not European. The documents, not the intentions, carry the result.",
             kick='B · The transformation in the numbers', size=24)

# ------------------------------------------------------ 8 SECTION B STAT
stat('13%', 'foreign born share of the population by 2010',
     'Up from 4.7 percent in 1970 · About 40 million people, the largest immigrant population in the nation\u2019s history in absolute terms · Census Bureau',
     "Stop on the pair of figures, because the lesson's first claim lives in the distance between them. In 1970 the Census Bureau counted about 9.6 million foreign born residents, 4.7 percent of the population. In 2010 it counted about 40 million, about 13 percent. The population itself had grown across those forty years, so the share nearly tripling means the foreign born population grew about four times over while the country grew by about half. Then give the figure its honest limit, the way Station 4 of the activity teaches it: a share and a total cannot show where newcomers came from, under what status they arrived, or why they came. The reading supplies the sources and the mechanism beside the numbers. Students who quote 13 percent without the 1965 preference system beside it are quoting a result without its cause, and the quick check is built to catch exactly that gap.",
     kick='B · The transformation in the numbers')

# ------------------------------------------------- 9 SECTION C DIVIDER
divider_text('Section C', 'The Settlement of 1986',
             'Legalization for the population already here, joined to the first ban on hiring unauthorized workers.',
             "Section C covers the bargain Congress built once the new immigration had produced a second question beside the legal one. By the 1980s several million people lived in the United States without legal authorization, many of them at work in plain sight, and the argument over that population ran through workplaces, border enforcement, and the status of families. The Immigration Reform and Control Act of 1986 was written as a settlement with two halves, and students should learn it as a settlement, with a give on each side. One half looked backward and regularized the population already present. The other half looked forward and tried to close the workplace door that had drawn unauthorized workers. The reading reports the judgment later made of the act, attributed to its critics: that the legalization was carried out and the workplace enforcement was not. Keep that attribution in view all section. The lesson states the claim as a claim, with its makers named, and the activity gives students the statute's own words to test it against.")

# ------------------------------------------------------ 10 SECTION C CONTENT
content_text('Two halves in one statute',
             ['Legalization covered those who arrived before 1982.',
              'About three million people gained legal status.',
              'Hiring an unauthorized worker knowingly was made unlawful.',
              'Paperwork checks were required at hiring for every worker.',
              'Critics later said one half was kept and one half was not.'],
             "Use both guided notes definitions in full here. The Immigration Reform and Control Act of 1986 is the law that granted legal status to about three million unauthorized immigrants already in the country and made it illegal for employers knowingly to hire unauthorized workers. And amnesty, in the sense this act uses the idea, is in immigration law, a grant of legal status to people who entered or remained in the country without authorization, as the 1986 act gave to those who had arrived before 1982. Station 2 of the activity quotes the statute itself, and the word to slow down on is knowingly: the ban reached an employer who hired knowing the worker was unauthorized, so every enforcement case turned on proof of what an employer knew. The legalization half ran once, on applications the immigrants filed. The hiring half had to be enforced workplace by workplace, year after year. That difference in machinery is in the documents, and students can argue from it.",
             kick='C · The settlement of 1986', size=24)

# ------------------------------------------------------ 11 SECTION C STAT
stat('3 million', 'people granted legal status under the 1986 act',
     'Covering those who had arrived before January 1, 1982 and resided continuously in the country · Immigration Reform and Control Act of 1986',
     "Give the number its date line, because the date line is the settlement's shape. The legalization covered people who had entered the United States before January 1, 1982 and had resided continuously in the country in an unlawful status from that date to the filing of the application, in the statute's own words, which Station 2 of the activity quotes. About three million people applied and gained legal status, moving from unauthorized residence to temporary residence and then toward permanent residence and citizenship. Teach the pairing once more: the same Congress that legalized three million people also made the knowing hire of an unauthorized worker unlawful for the first time. Supporters presented the two halves as one settlement, a closed account behind and a closed door ahead. The argument since, stated in the reading with its makers named, is that the account was closed and the door was not, and students will meet that argument again in the unit's later lessons on the polarized present.",
     kick='C · The settlement of 1986')

# ------------------------------------------------- 12 SECTION D DIVIDER
divider_text('Section D', 'A Reckoning with an Older Wrong',
             'A federal commission reopened the wartime internment, and Congress answered with an apology and payments.',
             "Section D turns from new arrivals to an older population and an older wrong, and the turn is deliberate in the lesson's design. During the Second World War, under Executive Order 9066, the federal government forced about 120,000 people of Japanese ancestry from their West Coast homes into camps. Most of them were American citizens. The World War II unit taught the removal itself. This lesson teaches what the country did about it four decades later, because the reckoning belongs to the same decades as the immigration settlement and rests on the same question: who counts as wronged by the nation's membership rules, and what is owed. In 1980 Congress created a commission to investigate. Its report, Personal Justice Denied, issued in 1983, is Station 3 of the activity, quoted from the audited record. The next slide teaches its findings in the commission's own conclusions.")

# ------------------------------------------------------ 13 SECTION D CONTENT
content_photo_s('naturalization-port.jpg', 'Findings, then redress',
              ['The removal was not justified by military necessity.',
              'The causes named were race prejudice, war hysteria, and failed leadership.',
              'The Civil Liberties Act of 1988 apologized.',
              'Each surviving person removed received 20,000 dollars.',
              'The first payments were made in 1990, to the oldest survivors.'],
             "The photograph shows new citizens taking the Oath of Allegiance at a naturalization ceremony in Baltimore held by United States Citizenship and Immigration Services, a Department of Homeland Security photograph. Use it to mark the section's pairing: the same federal government that naturalizes new members also settled an old account with members it had wronged. Teach the report's language exactly. The commission concluded that the promulgation of Executive Order 9066 was not justified by military necessity, and it named the broad historical causes of the decisions as race prejudice, war hysteria, and a failure of political leadership. It recommended an apology of the nation and a one time payment of 20,000 dollars to each of the approximately 60,000 surviving persons. Congress enacted both in the Civil Liberties Act of 1988, which President Reagan signed, and the first checks went out in 1990, beginning with the oldest survivors. Grade the three causes exactly wherever this lesson tests them.",
             kick='D · A reckoning with an older wrong')

# ------------------------------------------------- 14 SECTION E DIVIDER
divider_text('Section E', 'Americans on the Move',
             'The second remaking was internal: jobs, families, and whole regions shifting south and west.',
             "Section E opens the lesson's second movement, and students should feel the subject change: from who entered the country to where the country's own people chose to live. Across the decades after 1970, Americans moved in large numbers from the older industrial North and Midwest toward the South and the West, one of the largest internal migrations in the nation's history. Use the guided notes definition in full: the Sun Belt is the fast-growing region of the South and Southwest, whose population, jobs, and political weight rose from the 1970s onward on air conditioning, defense and technology work, and lower costs. Each element of that definition gets a slide's attention in this section, because the definition is a causal claim in compressed form. Air conditioning made the region's summers workable for year round industry and office work. Defense spending and then technology employment supplied jobs that did not depend on the old industrial geography. And lower land, housing, and tax costs let families and firms buy more room for less money.")

# ------------------------------------------------------ 15 SECTION E CONTENT
content_text('Why the Sun Belt grew',
             ['Air conditioning made its summers workable.',
              'Defense plants, bases, and technology firms supplied jobs.',
              'Land and housing cost less than in the older states.',
              'Texas, Florida, Arizona, and the Carolinas grew decade after decade.',
              'Michigan, Ohio, and West Virginia grew slowly or lost people.'],
             "Build the section on contrast, because the census records the movement as a pair, gains in one set of states and stagnation or loss in another. The Sun Belt's growth was not a single boom. It ran decade after decade, through the censuses of 1970, 1980, 1990, 2000, and 2010, and it drew on several streams at once: retirees moving for climate and cost, families moving with employers, defense workers following contracts, and, connecting this section to the lesson's first half, immigrants settling increasingly in the South and West as well as in the older gateway cities. The sending states tell the other half in the same record. Michigan, Ohio, and West Virginia grew slowly or lost population across the same decades, as the factory economy that had drawn their grandparents contracted. Students should state the movement whole: the country's center of population, which the Census Bureau tracks each decade, moved steadily southwest across the entire period this lesson covers.",
             kick='E · Americans on the move', size=24)

# ------------------------------------------------------ 16 SECTION E STAT
stat('1.45 million', 'people in Phoenix in 2010',
     'Up from about 107,000 in 1950 · Census Bureau, decennial censuses of 1950 and 2010',
     "Phoenix is the Sun Belt's growth stated in a single city, and the figures are Census Bureau figures from the decennial censuses of 1950 and 2010, rounded as Station 5 of the activity presents them. In 1950 Phoenix was a small desert city of about 107,000 people. By 2010 it held about 1.45 million, roughly thirteen times larger, and stood among the largest cities in the country. Have students do the proportion themselves, because this lesson grades proportions, not admiration: about 107,000 multiplied by thirteen is about 1.4 million. Then set Phoenix beside the fact that the same census counted the state of Arizona gaining congressional seats across the period while states in the Northeast and Midwest lost them. A city's growth of this size is never only a local story. In a system that apportions representation by population, growth of this size is a transfer of political weight, which the next slide takes up directly.",
     kick='E · Americans on the move')

# ------------------------------------------------------ 17 SECTION E CONTENT 2
content_text('Seats follow the moving vans',
             ['Every ten years, the census counts people where they live.',
              'House seats are apportioned by that count.',
              'The South and West gained seats in every reapportionment since 1970.',
              'Electoral votes moved with the seats.',
              'Population movement became political weight.'],
             "This slide carries the mechanism that converts the lesson's movements into power, and Station 5 of the activity closes on it. The Constitution apportions House seats among the states by population, counted in the census every ten years, and each state's electoral votes follow its seats. So a family that moves from Michigan to Arizona changes two states' counts, and when millions of families make similar moves across a decade, the reapportionment that follows the census transfers seats from the states they left to the states they joined. The record is unbroken across this lesson's period: in the reapportionments after the censuses of 1970, 1980, 1990, 2000, and 2010, the South and West gained seats and the Northeast and Midwest lost them. Immigrants count in the same census, so the lesson's two movements meet in this machinery: both the newcomers of Sections A through D and the movers of this section redrew the map that elects Congress and presidents.",
             kick='E · Americans on the move', size=24)

# ------------------------------------------------- 18 SECTION F DIVIDER
divider_text('Section F', 'The Older Cities Hollowed',
             'At the other end of the moving vans stood the factory cities that had drawn earlier generations north.',
             "Section F teaches the sending end of the internal migration, and it should be taught with the perpetrators named precisely, because this lesson's vocabulary carries two distinct causes that students often merge. The first is deindustrialization: the long decline of manufacturing employment in the United States from the 1970s onward, as factories closed, automated, or moved abroad, in the guided notes definition. Note that the definition names three different processes, closing, automating, and moving, which cost jobs in different ways and hit different towns. The second cause is older: white flight, the movement of white families from cities to suburbs in the decades after the Second World War, which had already carried much of the urban middle class, and its tax payments, beyond the city line before the factories closed. A hollowed city in this lesson is a city struck by both: its employment base contracted while its tax base suburbanized, and its government was left serving a poorer population with shrinking revenue.")

# ------------------------------------------------------ 19 SECTION F CONTENT
content_text('Detroit as the record',
             ['In 1950 Detroit had about 1.85 million people.',
              'Factories closed, automated, or moved abroad.',
              'Families and tax base moved to the suburbs.',
              'Neighborhoods emptied across whole districts.',
              'In 2010 Detroit had about 714,000 people.'],
             "Use both guided notes definitions in full here, because this slide is where they do their work together. Deindustrialization is the long decline of manufacturing employment in the United States from the 1970s onward, as factories closed, automated, or moved abroad. White flight is the movement of white families from cities to suburbs in the decades after the Second World War, accelerated by school desegregation orders and changing neighborhoods, which shrank city tax bases. Detroit records the two together in one set of Census Bureau numbers. In 1950 the bureau counted about 1.85 million people in Detroit, which stood among the largest cities in the country, built on the automobile industry. By 2010 it counted about 714,000. Whole neighborhoods emptied, and the city government shrank with the tax base that remained. Detroit is the extreme case, not the only one: the same pattern, at smaller scale, ran through the factory cities of the Northeast and Midwest.",
             kick='F · The older cities hollowed', size=24)

# ------------------------------------------------------ 20 SECTION F STAT
stat('714,000', 'people in Detroit in 2010',
     'Down from about 1.85 million in 1950, a loss of more than half · Census Bureau, decennial censuses of 1950 and 2010',
     "Have students state the loss as a proportion before anything else is said about it: about 714,000 against about 1.85 million is roughly two fifths remaining, a loss of more than half the city's people across sixty years. The figures are Census Bureau figures, presented rounded in Station 5 of the activity. Then place the number in the lesson's argument. Detroit's fall and Phoenix's rise, from the previous section, are the same decades read at the two ends of the moving vans: jobs and families gathered in the South and West while the older industrial cities lost both. One limit must be stated with the number, and the reading states it: Detroit is the largest loss among big American cities in this period, not the typical one. Using the extreme case is honest teaching when the extreme is named as extreme, and students should hear the teacher name it. The statistic shows the scale of the hollowing at its deepest, not its average depth.",
     kick='F · The older cities hollowed')

# ------------------------------------------------------ 21 SECTION G CONTENT
content_text('Revival at the center, unevenly',
             ['From the 1990s, investment returned to strong city centers.',
              'Wealthier residents moved into poorer neighborhoods.',
              'Prices and rents rose, and longtime residents were pushed out.',
              'Many older industrial cities saw little of the revival.',
              'By 2000 the map had been redrawn twice over.'],
             "Close the lesson's content with the second city story, taught beside the first and never as its cancellation. Use the guided notes definition in full: gentrification is the movement of wealthier residents and new investment into poorer city neighborhoods, raising prices and rents and often pushing out the people who lived there. From the 1990s, parts of New York, Washington, and other prosperous cities rebuilt housing and storefronts that the earlier decades had let decline, as workers and returning families sought the center again. The same process raised rents on the same blocks and displaced poorer residents, many of them the families of the immigrants and migrants who had kept those neighborhoods through the hard decades. And the revival was uneven by city: the strongest metropolitan economies drew the investment, while many older industrial cities, Detroit among them, saw little of it by 2000. The map that resulted is therefore layered: new immigration at the gates, a population shifted south and west, hollowed factory cities, and reviving centers inside a few of them.",
             kick='G · Revival at the center', size=24)

# ------------------------------------------------------ 22 GLANCE
s = slide(NAVY)
kicker(s, 'The Map at a Glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Two movements, one map', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The door reopened', 'Quotas ended, preferences built, 1965', 'Family and skills in place of national origin'),
        ('The numbers', '9.6 million and 4.7 percent, then 40 million and 13 percent', 'Sources shift to Latin America and Asia'),
        ('The settlement and reckoning', '1986 legalization and hiring ban; redress in 1988', 'About 3 million legalized; 20,000 dollars each'),
        ('The moving country', 'Sun Belt gains, Detroit falls, seats follow', 'Phoenix up thirteen fold; seats south and west')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, The Map at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The four rows are the lesson's argument in miniature. The door row must carry the mechanism, not only the date: quotas ended and a preference system built on family reunification and needed skills replaced them, signed on October 3, 1965. The numbers row carries the Census Bureau pair, about 9.6 million and 4.7 percent in 1970 against about 40 million and about 13 percent in 2010, with the sources shifted toward Latin America and Asia. The settlement row pairs the 1986 act's two halves with the reckoning of Personal Justice Denied and the Civil Liberties Act of 1988. The moving country row holds the internal map whole: the Sun Belt's growth, Detroit's fall, Phoenix's rise, and House seats following the movers in every reapportionment from 1970 onward. Grade the table generously on wording and strictly on its figures.")

# ------------------------------------------------------ 23 VOCAB A
vocab('Words for the laws',
      [('Immigration and Nationality Act of 1965', '1965: quotas ended, family and skills preferences built'),
       ('Immigration Reform and Control Act of 1986', '1986: legal status for about 3 million, hiring ban'),
       ('amnesty', 'Legal status for those present without authorization'),
       ('Sun Belt', 'The fast-growing South and Southwest')],
      "These definitions match the guided notes word for word, and students copy them exactly. Immigration and Nationality Act of 1965: the law that ended the national origins quota system in place since the 1920s and opened American immigration chiefly to family reunification and needed skills, transforming the sources of immigration. Immigration Reform and Control Act of 1986: the law that granted legal status to about three million unauthorized immigrants already in the country and made it illegal for employers knowingly to hire unauthorized workers. amnesty: in immigration law, a grant of legal status to people who entered or remained in the country without authorization, as the 1986 act gave to those who had arrived before 1982. Sun Belt: the fast-growing region of the South and Southwest, whose population, jobs, and political weight rose from the 1970s onward on air conditioning, defense and technology work, and lower costs.")

# ------------------------------------------------------ 24 VOCAB B
vocab('Words for the cities',
      [('deindustrialization', 'The long decline of factory employment'),
       ('gentrification', 'Wealthier residents and investment into poorer neighborhoods'),
       ('white flight', 'White families from cities to suburbs after the war')],
      "Three more terms, again matching the guided notes exactly, and students copy them as written. deindustrialization: the long decline of manufacturing employment in the United States from the 1970s onward, as factories closed, automated, or moved abroad. gentrification: the movement of wealthier residents and new investment into poorer city neighborhoods, raising prices and rents and often pushing out the people who lived there. white flight: the movement of white families from cities to suburbs in the decades after the Second World War, accelerated by school desegregation orders and changing neighborhoods, which shrank city tax bases. End the vocabulary on the pairing this lesson keeps returning to: deindustrialization and white flight are the two causes of the hollowing in Section F, one taking the jobs and the other taking the tax base, and gentrification is the partial and uneven answer of Section G, which rebuilt the strongest centers while pushing poorer residents out of them.")

# ------------------------------------------------------ 25 SYNTHESIS
s = slide(NAVY)
kicker(s, 'Synthesis')
text(s, 0.9, 1.35, 11.5, 1.1, 'What the remaking settled, and what it left open', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 3.4,
     ['The law of 1965 settled the question of sorting by national origin, and its preference system then remade the sources of immigration across fifty years.',
      'The settlement of 1986 legalized a population and banned a hiring practice, and the country argued for decades over whether both halves were kept.',
      'Americans in motion redrew the internal map on the same schedule, and the census carried the new map into Congress every ten years.'],
     size=21, color=POWDER, leading=1.3)
notes(s, "Draw the lesson together before the exit work, and do it by answering the lesson question in full sentences students can borrow. How did the immigration opened in 1965 remake the population? A preference system built on family and skills, working through sponsorship across decades, raised the foreign born population from about 9.6 million and 4.7 percent in 1970 to about 40 million and about 13 percent in 2010, shifted its largest sources from Europe to Latin America and Asia, and produced the settlements that followed: legalization and a hiring ban in 1986, and, in the same decades, a national apology and redress for the internment the wartime government had carried out. How did the movement of Americans themselves remake the map? Jobs, air conditioning, and lower costs drew millions south and west, the older industrial cities lost factories, families, and tax base together, the strongest centers partly revived from the 1990s at the price of displacement, and every census moved House seats toward the growth. What the remaking left open, the argument over the new variety of origin, language, and faith, is carried into the unit's remaining lessons.")

# ------------------------------------------------------ 26 CLOSING / EXIT
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did the immigration opened in 1965 and the movement of Americans themselves remake the country\u2019s population and map by the twenty first century? Build from the documents, and keep every figure with its source.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Changing Map File: five records, a ledger, and a verdict'),
        ('Notebook', 'Notebook page: six streams in a chart, and two movements in one paragraph'),
        ('Quick check', 'The Table and the Two Cities: the figures, the laws, and the seats'),
        ('Writing', 'Which Force Redrew the Map? The law, the Sun Belt, or the factories leaving')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: what the 1965 act ended and built, the foreign born figures for 1970 and 2010, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Changing Map File, runs five records: a labeled summary of the Immigration and Nationality Act of 1965 from the public record of Public Law 89-236; the Immigration Reform and Control Act of 1986 and Personal Justice Denied, quoted from the audited records; and Census Bureau data records on the foreign born and on Detroit, Phoenix, and reapportionment. Students keep a ledger of change, cause, and size across the file and close with a verdict on which single document best explains the changed map of 2020, answering the strongest rival. The quick check tests the figures, the two acts, and the reapportionment mechanism. The writing task widens the activity's verdict into the lesson's three forces: the law of 1965, the economy's movement south and west, or the factories leaving. The exit ticket has three parts: what the 1965 act ended and built, the foreign born figures for both census years, and the lesson question answered with a Sun Belt cause and both of Detroit's figures.")

dc.save(OUT)
