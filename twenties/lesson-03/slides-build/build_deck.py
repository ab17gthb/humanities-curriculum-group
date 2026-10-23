#!/usr/bin/env python3
"""The Twenties Lesson 3 deck, "America on Wheels," built to the approved
Gilded Age and Progressive Era pilot system: image-led slides, fragments only
on screen, comprehensive speaker notes, full lesson and vocabulary coverage.
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
OUT = os.path.join(HERE, '..', 'lesson-03-slides.pptx')

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
text(s, 0.9, 5.32, 11.5, 0.4, 'THE TWENTIES · LESSON 3', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'America on Wheels', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'How the car remade where Americans lived and what they expected', size=17, color=POWDER)
notes(s, "The photograph shows an auto tourists camp in Washington, D.C., on August 20, 1923, photographed by the National Photo Company and held by the Library of Congress. Automobiles stand beside rows of tents, with the Washington Monument in the distance. Open the lesson here, because the camp holds the whole argument in one view. Families had bought a machine, driven it on public roads, and stopped for the night in a place a town provided for motorists, a pattern that had barely existed a decade earlier. Today students trace that change step by step. Where a family could live, how a young couple spent an evening, where a farmer traded, and what a vacation looked like all shifted once an ordinary family could count on a car. Keep the costs in view from the start. The same spread of the car brought deaths, debt, and decline for the places and businesses it passed by.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did the automobile change where Americans lived, how they spent their time, and what they expected from life?', {})]],
     size=40, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the prosperity of the 1920s change American life, and why was that prosperity weaker than it looked?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question has three parts, and students should hear all three before the reading starts. Where Americans lived covers housing and the suburb. How they spent their time covers work, courtship, and leisure on the road. What they expected from life covers the new normal that followed, distance on demand, privacy in motion, and a house beyond the city with a machine in the garage. The unit question runs beneath it as the frame for the whole Twenties unit. This lesson answers the first half, how prosperity changed life, and it also opens the second half, because the car was bought on credit and its toll in deaths rose all decade. Hold students to the three part structure at the exit ticket. An answer that covers only housing or only freedom has answered part of the question, not the question.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'One car, five changes', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'From luxury to expectation', 'About 8 million cars in 1920, about 23 million in 1929'),
        ('B', 'Good roads and the federal highway', 'Federal aid, gasoline taxes, numbered highways in 1926'),
        ('C', 'The suburb and the commuter', 'Houses beyond the streetcar lines, a garage as standard'),
        ('D', 'What the car weakened', 'Streetcars, railroads, and bypassed small towns'),
        ('E', 'Courtship leaves the parlor', 'Dating by car replaces calling at home'),
        ('F', 'Tourism, camps, and the motel', 'Tourist camps, tourist cabins, the motel in 1925'),
        ('G', 'The costs of the car', 'About 30,000 deaths in 1929, and debt that remained')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=20, color=RUST_LT, font='Georgia')
    text(s, 1.55, yy + 0.02, 4.7, 0.6, t, size=18, color=CREAM, bold=True)
    text(s, 6.4, yy + 0.06, 6.0, 0.6, d, size=15, color=POWDER)
    yy += 0.62
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A sets the scale, from a rich man's toy in 1900 to about 23 million registrations in 1929. Section B shows the public roads that made the car usable in all weather. Section C follows the car into housing, as suburbs spread beyond the streetcar lines and the daily commute became normal. Section D names the losers the car created. Sections E and F follow the car into private life, courtship out of the parlor and family travel into camps, cabins, and motels. Section G collects the bill. Tell students the summary organizer in their guided notes, One Car, Five Changes, asks them to rebuild this map at the end.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_photo('family-port.jpg', 'Section A', 'From Luxury to Expectation',
              ['A rich man\'s toy in 1900', 'A family expectation by 1929'],
              "The photograph is S. P. Campbell and family touring the Glass House Mountains region in a motor car, about 1925, held by the State Library of Queensland. Say the disclosure plainly before students draw conclusions from it. The touring family photograph is Australian, about 1925, and the family and location are in Queensland, Australia, not the United States. It is used here only because it shows the family touring pattern plainly, a family posed beside its car on an outing taken on its own schedule. All registration figures in this lesson are United States figures. The pattern itself is the point of section A. A car outing like this one required a machine an ordinary family could buy, a price brought down by mass production, and a way to pay for it over time. Section A covers that spread of ownership, who bought, what they paid, and which industries the car pulled behind it.",
              title_size=40)

# ------------------------------------------------------ 5 LUXURY TO EXPECTATION
content_text('From a toy to an expectation',
             ['1900: expensive, unreliable, roads built for horses',
              '1920: about 8 million passenger cars registered',
              '1929: about 23 million, roughly one car for five people',
              'Model T: $850 in 1908, under $300 by the middle 1920s',
              'Most cars bought on installment credit'],
             "Give students the arc in order, because the guided notes test each step. In 1900 an automobile was a rich man's toy, expensive and unreliable on roads built for horses. By 1929 it was a normal expectation of family life. Mass production drove the change, as Lesson 1 showed. A Model T that cost $850 in 1908 sold for under $300 by the middle of the 1920s, and most cars were bought on installment credit, a payment at a time. Ownership spread from the wealthy to clerks, skilled workers, and farm families. Stress the second force as carefully as the first. A lower price alone did not put a car in a working family's yard. Credit did the rest, and that fact returns in section G, when a lost job could mean a lost car and a debt that remained. Price and credit together turned a luxury into an expectation.",
             kick='A · From luxury to expectation')

# ------------------------------------------------------ 6 STAT 23 MILLION
stat('23 million', 'passenger cars registered in the United States by 1929',
     'About 8 million in 1920. Roughly one car for every five people.',
     "Dwell on the two numbers, both from the reading, because together they convert a trend into a scale students can hold. About 8 million passenger cars were registered in 1920. By 1929 the figure was about 23 million, roughly one car for every five people. Do the arithmetic aloud. Registrations grew by nearly three times in nine years. At five people per car, the typical family could plausibly have its own machine, so not having one began to limit where a family could live, work, court, and travel. The guided notes ask for both figures, 8 million and 23 million, and the people per car figure, five. The exit ticket and the writing task both reward students who use the 1929 total accurately. A beginning luxury had become a mass possession, and every later section of this lesson follows from that spread. The car could remake daily life only once ordinary families had one.",
     kick='A · From luxury to expectation')

# ------------------------------------------------------ 7 A INDUSTRIES PULLED
content_text('The car pulled industries behind it',
             ['Most of the nation\'s rubber',
              'Much of its steel, glass, and oil',
              'Advertisers sold freedom and status',
              'Not transport alone'],
             "The car was never one industry by itself, and this short slide keeps students from treating ownership as a private purchase with no wider effects. The reading states that the car pulled other industries behind it, consuming most of the nation's rubber and much of its steel, glass, and oil. A family buying a car was also buying tires, plate glass, gasoline, and road services, and factories and refineries organized work around that demand. Advertisers understood the wider sale. They sold the car as freedom and status, not transport alone, which helps explain the third part of the lesson question. What Americans expected from life changed because the car was presented, and then experienced, as independence. A household could go where it chose, on its own schedule, without a timetable or a fare. Keep that expectation in view through the roads, suburb, and tourism sections. Each one turns a purchase into a new daily pattern.",
             kick='A · From luxury to expectation')

# ------------------------------------------------- 8 SECTION B DIVIDER
divider_photo('highway-port.jpg', 'Section B', 'Good Roads and the Federal Highway',
              ['Dirt in 1920: dust, then mud', 'Paved main routes by 1929'],
              "The photograph shows a completed paved highway in Durham County, North Carolina, a rock asphalt highway built as Federal Aid Project No. 71 and printed in the Biennial Report of the State Highway Commission of North Carolina in 1922. Be precise about what it shows. It is a finished road curving through trees with guard rails, not road construction in progress, and the caption beneath it in the original report is part of that page. The image is the right emblem for section B. A car was only as useful as the road under it, and in 1920 most rural roads were dirt, dust in summer and mud after rain. Section B covers the demand for surfaced roads, the federal acts that paid for part of them, the state gasoline tax that paid for another part, and the numbering system that tied the main routes together in 1926.",
              title_size=38)

# ------------------------------------------------------ 9 FEDERAL MONEY
content_text('Government answered with roads',
             ['Good Roads movement: surfaced roads as a public good',
              'Federal Aid Road Act of 1916: matching federal money',
              'Federal Highway Act of 1921: a connected network of main routes',
              'Mile by mile, the paved highway replaced the mud road'],
             "Walk the public money in order, because the guided notes test both act names and both dates. Drivers and farmers organized in a Good Roads movement demanding surfaced roads paid for as a public good. Government answered at two levels. The Federal Aid Road Act of 1916 offered matching federal money for state highway building, so federal dollars rewarded states that built. The Federal Highway Act of 1921 concentrated that money on a connected network of main routes, rather than scattering it across every local road. In the guided notes definition, a paved highway is a main road between places with a hard, surfaced roadway of concrete, asphalt, or brick that can be used in wet weather. That last phrase is the teaching point. A surfaced road stayed open after rain, so a long drive became a plan rather than an adventure.",
             kick='B · Good roads and the federal highway')

# ------------------------------------------------------ 10 GASOLINE TAX
content_text('The gasoline tax and one numbering system',
             ['States paid their share in part with gasoline taxes',
              'First adopted by Oregon in 1919',
              'Levied by every state by 1929',
              '1926: one numbering system, the United States highways'],
             "This slide completes the funding story and adds the standard that tied the roads together. States paid their share in part with gasoline taxes, first adopted by Oregon in 1919 and levied by every state by 1929. Note the fairness argument students often raise on their own. The tax fell on drivers, the people who used the roads, and it rose automatically as driving rose, so road building had a revenue source tied to its own demand. Then add the system step. In 1926 the main routes received one numbering system, the United States highways, so a driver could follow a numbered route across state lines instead of navigating by local road names. Connect this back to section A. Families bought cars in the millions once the cars were usable in all weather, on roads that connected, under numbers they could follow.",
             kick='B · Good roads and the federal highway')

# ------------------------------------------------- 11 SECTION C DIVIDER
divider_text('Section C', 'The Suburb and the Commuter',
             'The car redrew the map of where people lived.',
             "Pause before the comparison and set the problem in one sentence. The car redrew the map of where people lived. Earlier settlement had followed fixed lines, streetcar tracks and railroad tracks, because a family had to walk to a station and ride on a schedule. A private car removed both limits at once. Any road became a route to work, and any land a road reached became land a family could live on. Section C covers that shift in two moves. First, builders laid out subdivisions on cheap land beyond the streetcar lines, with a garage beside the house as a standard feature. Second, the head of the household settled into a new daily pattern, driving into the city each morning and back each evening. Home and work, which the streetcar had begun to separate, now separated more completely. A house and a yard in one place, a job downtown miles away, and the road between them belonged to the car.")

# ------------------------------------------------------ 12 SUBURB AND COMMUTER
content_text('Beyond the streetcar lines',
             ['Earlier suburbs: along streetcar and railroad lines',
              'Within walking distance of a station',
              'With a car: anywhere a road reached',
              'Subdivisions on cheap land, a garage as standard',
              'Head of household: a daily drive to the city'],
             "State the comparison precisely, because the reading question and the guided notes both test it. A suburb is a residential area on the edge of a city, outside the center, where people live and travel into the city for work. Earlier suburbs grew along streetcar and railroad lines, within walking distance of a station. A family with a car could live anywhere a road reached. Builders laid out subdivisions on cheap land beyond the streetcar lines, with a garage beside the house as a standard feature. The head of the household became a commuter, a person who travels regularly between home in one place and work in another, usually each day, driving into the city each morning and back each evening. Home and work separated more completely than the streetcar had separated them. That daily drive is the first clear answer to where Americans lived.",
             kick='C · The suburb and the commuter', size=25)

# ------------------------------------------------------ 13 SEATTLE PHOTO
content_photo('seattle-port.jpg', 'Two systems on one street',
              ['California Avenue SW, Seattle, October 30, 1925',
               'Streetcar tracks down the center',
               'Paved automobile lanes on each side',
               'Houses line both sides'],
              "The photograph shows California Avenue SW from SW Hill Street in Seattle on October 30, 1925, looking north, held by the Seattle Municipal Archives. Say the disclosure plainly, because it corrects the first conclusion students will draw. The Seattle photograph is a city street with streetcar tracks, not a suburb. It does not show a new automobile subdivision. It shows the older and newer systems sharing one street in 1925. Streetcar tracks of the Number 3 West Seattle line run down the center, a paved automobile lane runs on each side, automobiles are parked and driving on the lanes, and houses line both sides. Use the image as a competition picture. Every trip a family in one of these houses made in its own car, on its own schedule from its own door, was a fare the streetcar company did not collect. That loss is the subject of the next section.",
              kick='C · The suburb and the commuter')

# ------------------------------------------------- 14 SECTION D DIVIDER
divider_text('Section D', 'What the Car Weakened',
             'Every gain in reach was a loss somewhere else.',
             "Open this section with the reading's own balance sentence. Every gain in reach was a loss somewhere else. The car did not only connect places. It ranked them, rewarding the places on the paved routes at the expense of the places off them. Section D names three losers, and students should be able to give a reason for each, not just a name. Streetcar companies lost riders while their fare stayed fixed. Railroads lost short distance passengers to the new highways. Small towns lost the farm trade that had once had nowhere else to go. Keep the ranking language in front of students. A road that let a farmer drive past a small store to a larger town did not merely add a choice. It moved trade, and moved trade thinned main streets and started some railroad towns on a long decline. Gains and losses came from the same machine.")

# ------------------------------------------------------ 15 WHAT WEAKENED
content_text('The losers had names',
             ['Streetcar companies: fixed five cent fare, rising costs',
              'Many lines cut service or failed',
              'Railroads: short distance passengers lost to highways',
              'Farmers drove past the nearest store to a larger town',
              'Main streets in bypassed towns thinned out'],
             "Walk the three losers with the reason attached to each, because the exit ticket asks for two groups with a reason for each. Streetcar companies, charging a fixed five cent fare while costs rose, lost riders to private cars, and many lines cut service or failed. Railroads lost short distance passengers to the new highways, the trips where a car was most convenient. Small towns faced the sharpest problem. A farmer who once traded at the nearest store could now drive past it to a larger town with lower prices and more choice. Main streets in bypassed towns thinned out, and some railroad towns began a long decline. Close by returning to the ranking claim. The car rewarded places on the paved routes and weakened places off them, so a map of new highways in the 1920s is also a map of which towns would grow and which would shrink.",
             kick='D · What the car weakened', size=24)

# ------------------------------------------------- 16 SECTION E DIVIDER
divider_text('Section E', 'Courtship Leaves the Parlor',
             'Private life changed as plainly as the map.',
             "The car changed private life as plainly as it changed the map, and this section often draws the strongest reaction in the room, so ground it in the older pattern first. In the older pattern of courtship, a young man called on a young woman at her home, in the parlor, under the eyes of her family. The house set the hours, the place, and the supervision. A car removed all three controls at once. A couple could leave the house, travel miles, and spend an evening at a movie, a dance, or on a drive, on a schedule they chose themselves. Parents, ministers, and judges objected in print throughout the decade, and their alarm is evidence of how complete the change was. Section E covers that single shift, from calling to dating, and asks students to treat adult objection not as background color but as a measure of the change itself.")

# ------------------------------------------------------ 17 COURTSHIP
content_text('Dating replaced calling',
             ['Calling: at her home, in the parlor, family present',
              'Dating: out together, away from the house',
              'To a movie, a dance, or a drive',
              'Away from adult supervision',
              'Parents, ministers, and judges objected in print'],
             "Define the new practice in the guided notes wording, because the vocabulary slides return to it. Dating is a form of courtship in which a young man and a young woman go out together to public amusements, away from the family home and its supervision. Contrast it step by step with calling. Calling happened at the young woman's home, in the parlor, under the eyes of her family. Dating replaced calling. A young man with access to a car took a young woman out, to a movie, a dance, or a drive, away from the house and from adult supervision. A car gave young people privacy and a social life set by their own choices. What a family once supervised in its own front room now happened miles down a paved road. That sentence answers the second part of the lesson question, how Americans spent their time, in its most private form.",
             kick='E · Courtship leaves the parlor')

# ------------------------------------------------- 18 SECTION F DIVIDER
divider_photo('camp-port.jpg', 'Section F', 'Tourism, Camps, and the Motel',
              ['Travel on the family\'s own schedule', 'Stop where the family chose'],
              "The photograph is the same Washington, D.C. auto tourists camp of August 20, 1923, shown on the title slide, here cropped to the rows of tents and automobiles. More than a thousand towns provided municipal tourist camps by the middle of the decade, some free and some for a small fee, with water, cooking shelters, and a watchman, because campers bought gasoline, food, and supplies before they left in the morning. Section F follows what the car did to leisure. Tourism by automobile let a family see country that railroad tourists had seen only from a train window, and stop where it chose. Business then followed the campers, first with tourist cabins and then with the motel. Along the same roads, filling stations, diners, and billboards competed for the driver's money. A roadside economy had appeared that had no reason to exist before the car.",
              title_size=36)

# ------------------------------------------------------ 19 TOURISM AND CAMPS
content_text('A new kind of travel',
             ['Tourism by car: see the country, stop where you chose',
              'Early motorists camped beside the road',
              'Municipal tourist camps: more than a thousand towns',
              'Tin Can Tourists: founded in Florida in 1919',
              'Campers organized, towns competed for them'],
             "Define the practice first, in guided notes wording. Tourism is travel for pleasure, and the businesses that serve travelers with food, fuel, lodging, and entertainment. The car changed both halves of that definition. Travelers could now see country that railroad tourists had seen only from a train window, and stop where they chose, on their own schedule. Early motorists camped beside the road or in municipal tourist camps, which more than a thousand towns provided by the middle of the decade, some free and some for a small fee. Campers organized, most famously the Tin Can Tourists, founded in Florida in 1919. Ask students why a town would pay for a free camp. The camp was a funnel. A town that drew motorists in for the night sold them gasoline, food, and supplies in the morning, and competed with the next town down the road for the same travelers.",
             kick='F · Tourism, camps, and the motel')

# ------------------------------------------------------ 20 MOTEL AND ROADSIDE
content_photo('filling-port.jpg', 'The motel and the roadside',
              ['Tourist cabins, then one business for lodging and parking',
               'Motel: a word coined in 1925, from motor and hotel',
               'Guests park beside their rooms',
               'Filling station: gasoline, oil, and repairs'],
              "The photograph shows Clyde Mock's Hi-Speed filling station in Toledo, Ohio, in 1924, a small station building with two globe pumps in snow, held through the Digital Public Library of America. Its signs advertise hot dogs, refreshments, lunch, and coffee beside gasoline, which is the roadside economy in one building. Business followed the campers in steps. Owners built rows of tourist cabins, then combined lodging and parking in one business, the motel, a lodging built for motorists, from motor and hotel, in which guests park their cars beside or near their rooms. The word was coined in 1925. Along the same roads, the filling station, a roadside business that sells gasoline and oil and provides air, water, and basic repairs for automobiles, sold fuel and repairs, and diners and billboards competed for the driver's money. Each business existed only because drivers bought along roads.",
              kick='F · Tourism, camps, and the motel')

# ------------------------------------------------- 21 SECTION G DIVIDER
divider_text('Section G', 'The Costs of the Car',
             'The bill arrived with the benefits.',
             "Close the content where the reading closes, with the bill. The bill arrived with the benefits, and it had three parts students should keep separate. First, a human toll no earlier transport had imposed on ordinary families, in deaths that rose from about 12,000 in 1920 to about 30,000 in 1929. Second, a household cost built into the way the cars were bought, installment debt that remained even when the job or the car was gone. Third, a cost the earlier sections already counted, borne by farmers and towns whose trade the new roads carried to larger competitors. Section G gathers those costs so the lesson question is answered honestly. The automobile remade where Americans lived, how they spent their time, and what they expected from life, in distance on demand, privacy in motion, and a house beyond the city. The debts and the deaths came with it, and a full answer names both sides.")

# ------------------------------------------------------ 22 COSTS
content_text('Deaths, debt, and trade carried away',
             ['Deaths: about 12,000 in 1920, about 30,000 in 1929',
              'Millions of cars bought on credit',
              'A lost job could mean a lost car, and a debt that remained',
              'Farmers reached town, and their trade reached competitors'],
             "Take the costs one at a time, with the figures attached. Motor vehicle deaths rose from about 12,000 in 1920 to about 30,000 in 1929, a toll no earlier transport had imposed on ordinary families, and the guided notes ask for both figures. Millions of cars were bought on credit, so a lost job could mean a lost car and a debt that remained, a direct link back to the installment buying of section A and forward to the unit question about prosperity weaker than it looked. Farmers used cars to reach town and markets, yet the same roads carried their trade to larger competitors, the small town loss of section D seen from the farm side. End on the reading's summary claim. Distance on demand, privacy in motion, and a house beyond the city with a machine in the garage were the new expectations. The deaths and the debts were part of the same change.",
             kick='G · The costs of the car', size=24)

# ------------------------------------------------------ 23 SUMMARY ORGANIZER
s = slide(NAVY)
kicker(s, 'One car, five changes')
text(s, 0.9, 1.28, 11.5, 1.0, 'Rebuild the lesson in five rows', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Housing', 'Suburbs beyond the streetcar lines', 'A garage as a standard feature'),
        ('Courtship', 'Dating by car replaces parlor calling', 'Away from family supervision'),
        ('Work', 'The daily commute by car', 'Roadside and highway jobs grow'),
        ('Leisure', 'Tourism, camps, cabins, the motel', 'Travel on the family schedule'),
        ('Town business', 'Roadside economy on paved routes', 'Bypassed main streets thin out')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 0.82
notes(s, "This slide mirrors the summary organizer in the guided notes, One Car, Five Changes, and students should complete that table now, from memory where they can and from the lesson where they must. The five rows sort the whole lesson by area of life. Housing covers subdivisions beyond the streetcar lines with a garage as a standard feature. Courtship covers dating by car in place of parlor calling, away from family supervision. Work covers the daily commute and the new roadside and highway jobs. Leisure covers automobile tourism, tourist camps, tourist cabins, and the motel. Town business covers the roadside economy on paved routes and the thinning of bypassed main streets. Grade the table generously on wording and strictly on evidence. Each row needs what the car changed and one fact from the reading, such as about 23 million registrations, more than a thousand camps, or the motel in 1925.")

# ------------------------------------------------------ 24 VOCAB A
vocab('Words for where people lived and drove',
      [('suburb', 'a residential area on the edge of a city, outside the center, where people live and travel into the city for work'),
       ('commuter', 'a person who travels regularly between home in one place and work in another, usually each day'),
       ('paved highway', 'a main road between places with a hard, surfaced roadway of concrete, asphalt, or brick that can be used in wet weather'),
       ('filling station', 'a roadside business that sells gasoline and oil and provides air, water, and basic repairs for automobiles')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. A suburb: a residential area on the edge of a city, outside the center, where people live and travel into the city for work. The travel clause is part of the definition, not an extra. A commuter: a person who travels regularly between home in one place and work in another, usually each day. Regularly and each day separate a commuter from an occasional traveler. A paved highway: a main road between places with a hard, surfaced roadway of concrete, asphalt, or brick that can be used in wet weather. Wet weather is the load bearing phrase. A filling station: a roadside business that sells gasoline and oil and provides air, water, and basic repairs for automobiles. Roadside is its defining place.")

# ------------------------------------------------------ 25 VOCAB B
vocab('Words for time on the road',
      [('tourism', 'travel for pleasure, and the businesses that serve travelers with food, fuel, lodging, and entertainment'),
       ('motel', 'a lodging built for motorists, from motor and hotel, in which guests park their cars beside or near their rooms'),
       ('dating', 'a form of courtship in which a young man and a young woman go out together to public amusements, away from the family home and its supervision')],
      "Three more terms, again matching the guided notes exactly. Tourism: travel for pleasure, and the businesses that serve travelers with food, fuel, lodging, and entertainment. The definition has two halves, the travel and the businesses, and students need both. A motel: a lodging built for motorists, from motor and hotel, in which guests park their cars beside or near their rooms. The parked car beside the room is what separates a motel from a hotel or a cabin court in this lesson. Dating: a form of courtship in which a young man and a young woman go out together to public amusements, away from the family home and its supervision. Away from the family home and its supervision is the phrase that carries the change from calling, and it is the phrase the test will look for.")

# ------------------------------------------------------ 26 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did the automobile change where Americans lived, how they spent their time, and what they expected from life? Cover all three parts, and name one cost.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'One Car, Five Changes stations: numbers, the map, camps, Middletown, the roadside ledger'),
        ('Notebook', 'Notebook page: before the car, with the car, cost or loser, in five rows'),
        ('Quick check', 'Two Systems on One Street: the Seattle photograph of 1925'),
        ('Writing', 'The Car and the Shape of a Life: the lesson question as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: a highway as cause, two losers with reasons, and the lesson question in two or three sentences with one cost.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, One Car, Five Changes, runs five stations tracing one family purchase outward, through registration numbers, a county map, a tourist camp, the Middletown study of dating, and a roadside filling station, and ends by ranking the five changes by reach. The notebook page asks students to sort before the car, with the car, and cost or loser across housing, courtship, work, leisure, and town business. The quick check, Two Systems on One Street, uses the Seattle photograph of 1925. The writing task, The Car and the Shape of a Life, turns the lesson question into an essay. The exit ticket has three parts: why a paved highway was a cause of suburban growth and not only a result, two groups weakened by the car with a reason for each, and the lesson question in two or three sentences with at least two facts and one cost named.")

dc.save(OUT)
