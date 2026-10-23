#!/usr/bin/env python3
"""Lesson 6 deck, "The West," built to the approved Progressive Era system:
image-led slides, fragments only on screen, comprehensive speaker notes,
full lesson and vocabulary coverage. Fonts: Georgia titles, Lato body."""
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
OUT = os.path.join(HERE, '..', 'lesson-06-slides.pptx')

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

def content_photo_sized(img, title, items, note, kick=None, size=23):
    s = slide(CREAM)
    photo_right(s, img)
    if kick: kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95 if kick else 0.8, 6.9, 1.2, title, size=31, color=NAVY, font='Georgia', leading=1.05)
    frags(s, items, y=2.15 if kick else 2.0, size=size)
    notes(s, note)
    return s

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'GILDED AGE · LESSON 6', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The West', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Railroads, land grants, homesteads, and the fight over land, water, and grass', size=17, color=POWDER)
notes(s, "The photograph shows cowboys branding calves on a roundup in South Dakota in 1888, photographed by John C. H. Grabill. It is a good opening image for this lesson because branding only made sense inside a whole system: cattle raised on open public grass, gathered at a roundup, marked by owner, and driven to a railhead for shipment east. That system, and the mining and farming systems beside it, were all built by the two forces in the lesson question. After the Civil War, railroads tied western places to national markets, and federal land policy decided how public land passed into private hands. Tell students to watch for both forces in every section. Mining, cattle, and farming look like three separate stories, and the lesson argues they are one story told three ways, with a fourth story underneath: the Native nations who held this land under treaties and were pressed onto reservations as the other three advanced.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did railroads and federal land policy remake the West?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did industrial growth transform American life, and who gained, who paid, and who resisted?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question is the narrower one on the slide, and the unit question runs beneath it as the frame. How did railroads and federal land policy remake the West? Push students to hear the verb. Remake means the West of 1890 was not simply the West of 1860 with more people in it. Its economy, its map of ownership, and its connections to the rest of the country had all been rebuilt. Railroads supplied the connections: after 1869 a trip that took months by wagon took about a week by train, and mines, ranches, and farms could sell into national markets. Land policy supplied the ownership: land grants to railroads, homestead claims to families, and reservations imposed on Native nations divided the region into companies, claims, fences, and reservations. The lesson answers the unit question directly. Industrial growth transformed the West, and who gained, who paid, and who resisted depended on where a person stood on that new map. Students will take that position themselves in the writing task.")

# --------------------------------------------------- 3 THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.3, 11.5, 1.0, 'A West tied to the East', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.42)
rows = [('A', 'Two forces of change', 'railroads and federal land policy drive everything'),
        ('B', 'Mining booms', 'gold and silver pull people, capital, and conflict'),
        ('C', 'Cattle and the open range', 'Texas herds walk to Kansas railheads'),
        ('D', 'Farming the Plains', 'homesteads, sod houses, and dry farming'),
        ('E', 'Land grants and reservations', 'the checkerboard and the shrinking map')]
yy = 2.82
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.7, n, size=26, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.03, 3.4, 0.7, t, size=23, color=CREAM, bold=True)
    text(s, 5.15, yy + 0.08, 7.3, 0.7, d, size=18, color=POWDER)
    yy += 0.9
notes(s, "This is the map of the lesson, and it follows the guided notes section by section. Section A names the two forces, railroads and federal land policy, that drive everything after it. Section B takes mining, usually the first arrival in a region, from the Comstock Lode to the Black Hills. Section C follows cattle on the open range, from Texas herds to Kansas railheads and then to the wire and winters that ended the long drives. Section D turns to farming: the Homestead Act, sod houses, and dry farming on a dry plain. Section E goes underneath the other sections to the land decisions themselves, the railroad checkerboard and the reservation system. Tell students the exit ticket asks for one change and its gainer and payer, so they should keep that question running in every section, not save it for the end. The notebook page chart has a row for each economy, and students will fill it in as we go.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_photo('railroad-port.jpg', 'Section A', 'Two Forces of Change',
              ['Railroads tied the West to national markets.',
               'Land policy decided who would own it.'],
              "The photograph is the most famous railroad image of the century: the two locomotives meeting at Promontory Summit, Utah, on May 10, 1869, photographed by Andrew J. Russell. At the center, the chief engineers of the Central Pacific and the Union Pacific shake hands at the laying of the last rail. Use the image to make the section's claim concrete. A completed transcontinental line was not just a faster trip. It was a machine for moving everything this lesson studies: miners and mining machinery inward, silver and gold outward, cattle from railheads to eastern packing houses, wheat from Plains farms to distant buyers. The second force rides along with the first. The railroad in this photograph exists because the federal government helped pay for it, in part with land. Keep both forces in view from the first minute, because the guided notes open by asking students to name them.",
              title_size=44)

# ------------------------------------------------------ 5 TWO FORCES
content_text('Two forces remade the West',
             ['Railroads: the West tied to national markets',
              'Federal land policy: who gets the public land',
              '1869: the first transcontinental line is completed',
              'The land was not empty: Native nations held it under treaties'],
             "State the two forces plainly, because the first blanks of the guided notes test them. Railroads connected western places to national markets. Federal land policy decided how public land would pass into private hands. Neither force worked alone. Railroads needed land grants and loans tied to land to finance construction across country that at first held few paying customers. Settlers needed railroads to reach a claim and to ship anything they produced. Then correct the oldest misconception in the unit before it forms. The land those settlers occupied was not empty. Native nations lived across the Plains and the mountain West, hunted and farmed there, and held the land under treaties with the United States. Every railroad line, mine, ranch, and homestead in this lesson therefore tells two stories at once: a story of new economic opportunity, and a story of conflict over land that other people already claimed as their own. That double story is the lesson in one sentence.",
             kick='A · Two forces of change')

# ------------------------------------------------------ 6 STAT 1869
stat('1869', 'the first transcontinental railroad is completed',
     'A journey that had taken months by wagon could now be made in about a week by train.',
     "Dwell on what the date changed. Before 1869, a journey from the East to the Pacific took months by wagon, at real risk, and freight moved no faster than a team could walk. After the last rail was laid at Promontory Summit, the same journey took about a week by train. Mining camps, cattle towns, and farm settlements that had once stood far from any market now sat within reach of Chicago and the cities of the East. Distance had been the West's protection and its limit. A mine too far from a railroad shipped only what a wagon could carry, which meant only rich ore paid. A ranch too far from a railhead sold cattle at local prices. The completed line collapsed that distance for every section that follows, which is why this lesson begins with a railroad rather than with a prospector, a cowboy, or a farmer. Each of them was working inside a market the railroad created.",
     kick='A · Two forces of change')

# ------------------------------------------------- 7 SECTION B DIVIDER
divider_photo('mining-port.jpg', 'Section B', 'Mining Booms',
              ['Gold and silver strikes pull people,',
               'capital, and conflict west'],
              "The photograph shows three prospectors washing and panning gold at Rockerville, in Dakota Territory, in 1889, photographed by John C. H. Grabill. Name the date honestly for students. The picture comes late in the story this section tells, a decade and more after the Black Hills strikes of the 1870s, and it shows the hand method of the earliest stage of a boom, men working a stream with a pan and simple tools. Mining usually came first in a region, before ranches or farms, because a strike needed no growing season and no permission slip from a land office. Word of gold or silver traveled fast, and people followed it faster. This section follows that sequence twice, in Nevada and in the Black Hills, and then asks what happened when the easy surface deposits ran out, because the answer, company mining and wage labor, is the pattern of the whole Gilded Age in miniature.",
              title_size=54)

# ------------------------------------------------------ 8 BOOMTOWNS
content_photo_sized('deadwood-port.jpg', 'Gold, silver, and boomtowns',
              ['Comstock Lode, Nevada, 1859: vast silver, Virginia City booms',
               'Black Hills gold, 1870s: Deadwood rises on Lakota treaty land',
               'Leadville, Colorado: a silver town almost overnight',
               'Merchants, saloons, freight, and banks follow the prospectors'],
              "Take the three strikes in order. The Comstock Lode in Nevada, discovered in 1859, produced vast amounts of silver and turned Virginia City into a busy industrial town with deep mines financed by companies in San Francisco. Gold found in the Black Hills in the 1870s drew thousands of miners to camps such as Deadwood, on land the Lakota held under treaty, and the photograph on this slide shows Deadwood in 1876, already a street of stores a year or two into the rush. Leadville, Colorado, grew almost overnight around silver mines. Stress the order of arrival in the reading, because it explains a boomtown economy. Prospectors rushed in first, followed by merchants, saloon keepers, freight companies, and banks. Most of the steady money in a boom was made selling things to miners, not mining. And flag the conflict built into the second example: the Black Hills strike was not a discovery on empty land. It was an invasion of treaty land, and section E returns to it.",
              kick='B · Mining booms')

# ------------------------------------------------------ 9 BOOM TO BUST
content_text('When the boom went bust',
             ['Surface deposits run out fast',
              'Deep mining takes expensive machinery',
              'Only large companies can afford it',
              'Prospectors sell out, or become wage workers',
              'Empty camps become ghost towns'],
             "Boomtowns could empty almost overnight, and students should understand the mechanism rather than picture simple bad luck. Surface deposits, the gold in streambeds and the silver near the surface, ran out quickly, often within a few seasons. What remained lay deep, and deep mining required expensive machinery that only large companies could afford. At that point the individual prospector faced two choices, and both ended the independent miner. He sold his claim to a company, or he stayed and became a wage worker in a company mine, doing the same work for a daily wage instead of a prospector's hope. Many camps simply became ghost towns. Mining still left a permanent mark on a region even when it left. It pulled railroads, capital, and settlers in, and it left behind wage labor and disputed claims on land and water. Hold that phrase, disputed claims, for the map exercise at the end of the lesson.",
             kick='B · Mining booms', size=24)

# ------------------------------------------------- 10 SECTION C DIVIDER
divider_photo('cowboy-port.jpg', 'Section C', 'Cattle and the Open Range',
              ['Texas herds, Kansas railheads,',
               'and twenty years of long drives'],
              "The photograph is the lesson's most famous cowboy image, John C. H. Grabill's portrait of a mounted cowboy in Dakota Territory, made about 1888. Tell students what it is and what it is not. It is a posed portrait, taken in Dakota Territory near the end of the cattle drive era, not a photograph of a Texas herd on the trail in the 1870s. No camera rode the drives. The portrait still teaches the work honestly: the rope, the chaps, the saddle, and the working horse are the tools of a man whose job was to move other men's cattle across open country. That job existed because of a price gap. At the end of the Civil War, Texas held large herds of longhorn cattle worth little locally and much more in northern and eastern markets. The cattle drive was the bridge across that gap, and this section follows herds from Texas ranches to Kansas railheads, then asks why the bridge was needed for only about twenty years.",
              title_size=40)

# ------------------------------------------------------ 11 THE DRIVE
content_photo_sized('branding-port.jpg', 'The cattle drive',
              ['Texas longhorns: worth little at home, much more in the North',
               'Cowboys walk herds to Abilene and Dodge City, Kansas',
               'At the railhead, cattle load onto trains for eastern markets',
               'Two or three months on the trail, dangerous and poorly paid',
               'Many cowboys were Mexican American or Black'],
              "Work through the economics first. The problem the drive solved was distance, not supply. Texas had the cattle and the East had the buyers, and until railroads reached Texas there was no way to connect them except to walk the product to the train. Cowboys moved herds on foot from Texas ranches to railheads in Kansas towns such as Abilene and Dodge City, where the animals were loaded onto trains. A drive could take two or three months. Then describe the work itself, because the romance hides it. The work was dangerous and poorly paid, crossing rivers, storms, and stampedes, and it was done by a workforce that included many Mexican American and Black cowboys, a fact the guided notes and the notebook chart both carry. The photograph shows the roundup work at the end of the system, branding calves in South Dakota in 1888 so that cattle raised on shared public grass could be sorted by owner. Brands only make sense where herds mix, and herds only mixed on an unfenced range.",
              kick='C · Cattle and the open range', size=21)

# ------------------------------------------------------ 12 DRIVES END
content_photo_sized('barbedwire-port.jpg', 'Why the drives ended',
              ['Railroads build directly into Texas',
               'Barbed wire, patented in 1874, fences the open range',
               'Wire blocks the trails and the water',
               'Severe winters in the middle 1880s kill herds',
               'Ranching survives, fenced and smaller'],
              "The open range system depended on two conditions, unfenced public grass and open trails, and in the 1880s both conditions failed at once. Give students the three causes in the order the guided notes test them. First, railroads built directly into Texas, which removed the need for the long drive: the train now came to the cattle. Second, farmers and ranchers fenced land with barbed wire, patented in 1874, and the drawing on this slide is Joseph Glidden's patent drawing of that year. Wire enclosed the open range cheaply and blocked trails and water. Third, severe winters in the middle 1880s killed cattle by the hundreds of thousands on the open range, where herds could not be fed or sheltered. Ranching did not end. It changed into a fenced, smaller scale business based on owned or leased land, which is to say it became farming with cattle, subject to the same land rules as everything else in this lesson.",
              kick='C · Cattle and the open range', size=23)

# ------------------------------------------------- 13 SECTION D DIVIDER
divider_photo('sodhouse-port.jpg', 'Section D', 'Farming the Plains',
              ['Homesteads, sod houses,',
               'and farming without rain'],
              "The photograph shows the Sylvester Rawding family in front of their sod house north of Sargent, in Custer County, Nebraska, in 1886, photographed by Solomon D. Butcher. It is the best single image in the lesson, and it rewards a slow look. The house is built of the prairie itself because timber was rare on the Plains. A cow stands on the sod roof, which tells students how thick and how earthen that roof was. The family has posed with its table, its team, and its dog, the capital of a homestead claim displayed for the camera. Farmers followed the railroads onto the Plains, encouraged by the Homestead Act of 1862, and this section takes the act apart: what a claimant had to do, what Plains farming demanded, and why a run of wet years persuaded families to settle farther west than the rainfall could support when drought returned.",
              title_size=44)

# ------------------------------------------------------ 14 HOMESTEAD ACT
content_text('The Homestead Act, 1862',
             ['A homestead: a claim of up to 160 acres of public land',
              'Pay a filing fee',
              'Live on the claim and improve it for five years',
              'Then, and only then, full title',
              'Railroads also sold land, often on credit, and recruited settlers'],
             "Correct the phrase free land directly, because the exit ticket tests the correction. The Homestead Act of 1862 offered a homestead, a claim of up to 160 acres of public land, but it was not free land with no conditions. A claimant paid a filing fee and had to live on the claim and improve it for five years before receiving full title. Improvement meant work with a cash value in a place with little cash: a house, a well, broken sod, fences. Many families spent heavily on tools, seed, and survival in the meantime, which is why the sample writing answer treats the fee as the smallest of the three conditions. Note the railroad's parallel land business. Railroad companies also sold land, often on credit, and recruited settlers in the East and in Europe, because settlers meant freight business for the line. A farm beside a railroad was a customer for a generation, shipping crops out and manufactured goods in.",
             kick='D · Farming the Plains', size=24)

# ------------------------------------------------------ 15 STAT 160 ACRES
stat('160 ACRES', 'the size of a homestead claim under the Act of 1862',
     'One claim, earned with a filing fee and five years of living on the land and improving it.',
     "Put the number on the ground for students. One hundred sixty acres is a quarter of a square mile, a square about half a mile on each side. On well watered eastern land that was a generous farm. On the dry Plains it could be too little land to survive on, because rain, not acreage, set the limit on what a family could grow, and a claim could not be moved to a wetter valley when the dry years came. The size also explains the map exercise. A district of 160 acre claims fills quickly, and every claim needs the same scarce things: water, a road or a railroad, and grass until the fences go up. When students work the land claim map, have them find the homestead rectangle and count what it touches. The claim's neighbors, the railroad, the river, the open range, and the reservation boundary, are the whole lesson drawn to scale in one district.",
     kick='D · Farming the Plains')

# ------------------------------------------------------ 16 DRY PLAIN
content_text('Farming a dry plain',
             ['Houses of sod, because timber was rare',
              'Steel plows cut the tough prairie',
              'Windmills pump water; dry farming conserves soil moisture',
              'Wet years pull settlement too far west',
              'Drought returns: debt, lost claims, and commercial farming'],
             "Plains farming was hard in ways eastern farming was not, and the guided notes isolate the adaptations. Rain was scarce and uncertain. Settlers built houses of sod because timber was rare, as the Rawding photograph showed. They used steel plows to cut the tough prairie sod that broke lighter plows, windmills to pump water from below the surface, and dry farming, methods of growing crops in dry regions by conserving soil moisture, fallowing and packing the soil so one year's rain could help grow the next year's crop. Then the trap closed. A run of wet years in the 1870s and early 1880s encouraged settlement farther west than the rainfall could support in dry years. When drought returned, many families lost their claims to debt and walked away. Those who stayed became commercial farmers, growing wheat and corn for distant markets and depending on railroad rates, bank credit, and world prices they could not control. Independence was the promise. Dependence on distant markets was the result.",
             kick='D · Farming the Plains', size=24)

# ------------------------------------------------- 17 SECTION E DIVIDER
divider_text('Section E', 'Land Grants and Reservations',
             'Underneath mining, cattle, and farming sat one federal decision: whose land is this?',
             "Slow down here, because this section is the lesson's argument about causes. Sections B, C, and D described three economies. This section names the federal decisions underneath each of them. To help railroads build, the government gave companies land grants. To settle farm families, the government offered homesteads. To clear the way for both, it pressed Native nations onto reservations. The next slide uses the teaching diagram from the activity, one western district drawn to hold all five features at once: a mining camp, a cattle trail, a railroad with its land grant checkerboard, a homestead claim, and a reservation boundary. The diagram is a teaching tool, simplified and not to scale, and it combines features that in real places were spread across several states. Used honestly, as a model rather than a map of a real place, it lets students see conflicts that a list of facts hides. Features that coexist on one page could not coexist peacefully on one piece of ground.")

# ------------------------------------------------------ 18 THE MAP
s = slide(CREAM)
kicker(s, 'E · Land grants and reservations', color=RUST)
text(s, 0.9, 0.95, 11.5, 1.0, 'One western district', size=31, color=NAVY, font='Georgia')
s.shapes.add_picture(os.path.join(dc.IMG, 'west-map.png'), Inches(2.92), Inches(1.62), Inches(7.5), Inches(4.5))
text(s, 0.9, 6.3, 11.53, 0.6, 'Teaching diagram, simplified and not to scale. The same map you will work in the activity.',
     size=16, color=MUTED, align=PP_ALIGN.CENTER)
notes(s, "Walk the diagram feature by feature, in the order the activity's five stations will visit them. The mining camp sits in the mountains where the river begins, so it will want water and timber that others need below. The cattle trail runs north from Texas ranches to the railhead town, crossing open range and needing water on the way. Along the railroad runs the checkerboard of alternating sections, railroad sections marked R and government sections marked G, which the next discussion takes apart. The homestead claim, 160 acres in the southwest, sits near both the line and the river, and its family needs both to survive. The reservation boundary, dashed in the north, looks settled on paper and was not settled on the ground. Tell students this exact diagram is the activity. Every station zooms in on one feature, and the final judgment asks how one federal policy could create opportunity and conflict at the same time. The map is the lesson's argument in picture form.")

# ------------------------------------------------------ 19 CHECKERBOARD
content_text('The checkerboard',
             ['Land grants: alternating sections along the line',
              'The railroad sells its sections to settlers',
              'The land is also security for the loans that build the line',
              'The government keeps the sections in between',
              'Farms and railroad land end up interleaved'],
             "Explain the checkerboard slowly, because the exit ticket's first question tests it in one sentence. To help railroads build, the government gave companies a land grant, public land in alternating sections along the line, in a checkerboard pattern. The companies sold their sections to settlers and used the land as security for loans, while the government kept the sections in between. Both halves of the pattern mattered. For the railroad, the grant solved the builder's problem: a line through unsettled country had few customers at first, but the land beside it could be sold or borrowed against today, paying for construction before a single ticket was bought. For the government, the kept sections usually rose in value once the line was built, so the public was repaid in land value rather than cash. For settlers, the pattern meant buying from a mix of railroad, government, and private sellers, with farms and railroad land interleaved along the route, a complication the map exercise asks them to feel from inside one district.",
             kick='E · Land grants and reservations', size=24)

# ------------------------------------------------------ 20 RESERVATIONS
content_text('Reservations and the shrinking map',
             ['Reservations: land set aside by treaty or federal order',
              'Often far smaller than the land a nation used before',
              'Reduced again when miners or settlers wanted the land',
              'Conflicts over land, water, and grass run through every section'],
             "Give the reservation system the same mechanical clarity as the checkerboard, because students should see it as a policy, not a background condition. To clear the way for grants and homesteads, the government pressed Native nations onto a reservation, land set aside by treaty or federal order, often far smaller than the land a nation had used before, and often reduced again when miners or settlers wanted it. The Black Hills are the lesson's worked example: gold drew miners to camps such as Deadwood on land the Lakota held under treaty, and the boundary moved. Nor was land the only contested resource. Mining took water and fouled streams, cattle needed grass and open trails, and farms fenced both. Conflict over land, water, and grass is therefore not a separate topic at the end of the lesson. It is the friction produced whenever the other sections met on the same ground, and the notebook chart's final column, who paid or resisted, records it row by row.",
             kick='E · Land grants and reservations')

# ------------------------------------------------------ 21 BY 1890
content_text('By 1890: a West tied to the East',
             ['Mines supply national industry',
              'Ranches and farms feed eastern cities',
              'Land now sits in companies, claims, fences, and reservations',
              'Who gained, who paid, and who resisted depends on where you stand'],
             "Close the survey with the reading's conclusion. By 1890 the West was no longer a separate frontier economy. Its mines supplied national industry, its ranches and farms fed eastern cities, and its land had largely passed into a system of companies, claims, fences, and reservations. Eastern capital had financed the deep mines and the railroads, and eastern and European markets set the prices that decided whether a Plains farm survived. That is the tie back the lesson question asks for: the West was remade not by isolation but by connection, and the connections ran through railroad lines and federal land law. Return to the unit question one more time before vocabulary. Industrial growth had remade the region. Who gained, who paid, and who resisted depended on where a person stood on that map. Students have now met every group the writing task offers them: miners, ranchers, homestead farmers, railroad companies, and Native nations.",
             kick='E · Land grants and reservations')

# ------------------------------------------------------ 22 VOCAB A
vocab('Words for the land',
      [('homestead', 'a farm claim of up to 160 acres of public land made under the Homestead Act'),
       ('land grant', 'public land given by the government to a railroad or other company to support construction'),
       ('reservation', 'land set aside by treaty or federal order for a Native nation')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. A homestead: a farm claim of up to 160 acres of public land made under the Homestead Act. Note that the definition says claim, not gift, which carries the whole argument of section D. A land grant: public land given by the government to a railroad or other company to support construction. The purpose clause matters: the land was payment and financing for building, not a reward after it. A reservation: land set aside by treaty or federal order for a Native nation. Set aside sounds generous until students pair it with the reading's facts: the land was far smaller than what the nation had used before and could be reduced again. Together the three terms are the federal land system in miniature: land offered to families, land granted to companies, and land assigned to the nations who already held it.")

# ------------------------------------------------------ 23 VOCAB B
vocab('Words for the work',
      [('cattle drive', 'the movement of herds on foot from Texas ranches to railheads and markets'),
       ('mining boom', 'a rapid rush of people and capital to a place where gold, silver, or another mineral was found')],
      "Two more terms, again matching the guided notes exactly. A cattle drive: the movement of herds on foot from Texas ranches to railheads and markets. Every phrase in that definition does work. On foot distinguishes the drive from shipment by rail, and railheads and markets names its destination and its purpose: the drive existed only to reach a train. A mining boom: a rapid rush of people and capital to a place where gold, silver, or another mineral was found. Students often keep the people and drop the capital, so stress the second half. A boom was money arriving as fast as men did: San Francisco companies financing Comstock mines, banks and freight firms following prospectors into Deadwood and Leadville. When the capital changed its mind or the surface deposits ran out, the boom ended just as rapidly, which is why boomtowns became ghost towns. Both terms describe movement toward money, one walking north at a cow's pace, the other rushing in at the speed of a rumor.")

# ------------------------------------------------------ 24 VOCAB C
vocab('Words for the fence and the field',
      [('barbed wire', 'fencing wire with sharp barbs that enclosed open range cheaply'),
       ('dry farming', 'methods of growing crops in dry regions by conserving soil moisture')],
      "The last two terms are the technologies that closed the open range and opened the dry Plains, and both definitions match the guided notes. Barbed wire: fencing wire with sharp barbs that enclosed open range cheaply. The final word is the definition's point. Fencing a range with timber rails was ruinously expensive where timber was scarce. Wire was cheap, and cheap fencing is what turned public grass into controlled parcels, blocked cattle trails, and guarded water. Dry farming: methods of growing crops in dry regions by conserving soil moisture. This is a definition about a system, not a single tool: fallowing, packing, and timing the soil so scarce rain was saved rather than spent. Together the terms explain the 1880s turn in the lesson. Wire ended the cattle drive's landscape, and dry farming extended the farm's landscape farther west than rainfall alone would have allowed, with the drought losses of section D as the price when the methods were pushed too far.")

# ------------------------------------------------------ 25 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'The Land Claim Map', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Return to the lesson question: how did railroads and federal land policy remake the West? Answer it with the map, the chart, and one paragraph.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'Land Claim Map Exercise: five stations, then your judgment'),
        ('Notebook', 'The West chart: mining, cattle, farming, railroads and land'),
        ('Quick check', 'Branding Calves on the Roundup: the 1888 photograph'),
        ('Writing', 'Who Gained, Who Paid: one paragraph answering the question')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=19, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.75, 11.5, 0.5, 'Exit ticket: explain a land grant, name two homestead conditions, pick a gainer and payer.',
     size=16, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to its work. How did railroads and federal land policy remake the West? Students now answer it four ways. In the activity, the Land Claim Map Exercise, they study the teaching diagram through five stations, mining camp, cattle trail, railroad grant checkerboard, homestead claim, and reservation boundary, then rank the features and judge one federal policy in a paragraph. The notebook page keeps the chart they filled in today, mining, cattle, farming, and railroads and land, with its pattern question about the federal government's role in every row, and they will use it again on review day. The quick check, Branding Calves on the Roundup, tests whether they can read the 1888 Grabill photograph as evidence about the open range system. The writing task, Who Gained, Who Paid in the West, asks for one paragraph that answers the lesson question with a claim, two facts from two different rows, and a cost side. Next lesson, the focus shifts from the land to the cities that industry built.")

dc.save(OUT)
