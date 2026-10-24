#!/usr/bin/env python3
"""Gilded Age Lesson 1 deck, "The Engines of Industry," built to the approved
Progressive Era pilot system: image-led slides, fragments only on screen,
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

def content_photo_s(img, title, items, note, kick=None, size=21):
    s = slide(CREAM)
    photo_right(s, img)
    if kick: kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95 if kick else 0.8, 6.9, 1.2, title, size=31, color=NAVY, font='Georgia', leading=1.05)
    frags(s, items, y=2.15 if kick else 2.0, w=6.9, size=size)
    notes(s, note)
    return s

# ---------------------------------------------------------------- 1 · TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'GILDED AGE · LESSON 1', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Engines of Industry', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'How one railroad line became the system that remade American industry', size=17, color=POWDER)
notes(s, "This photograph is the most famous railroad image of the century: the two locomotive crews shaking hands at Promontory Summit, Utah Territory, on May 10, 1869, with the officials in the center and the workers who built the road around them. Open the unit here, because everything in the Gilded Age runs through this scene. Behind the celebration is a harder claim, and it is the claim of this lesson. The meeting in Utah mattered, but not because one line of track was dramatic. It mattered because the railroad became a system: a network of track, steel, oil, wires, and corporate money that reorganized how the whole country produced and sold goods. Students should leave today able to trace that system part by part, in order, and to answer the lesson question with facts rather than with the single word trains.")

# ------------------------------------------------- 2 · LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('Why did railroads become the engine of a national industrial economy?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did industrial growth transform American life, and who gained, who paid, and who resisted?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question is the narrower one on the slide, and the unit question runs beneath it as the frame for the whole Gilded Age unit. This lesson answers the first half of that unit question: how industrial growth happened, and what machinery, in both senses, made it possible. Later lessons take up who gained, who paid, and who resisted, and students will meet the Chinese and Irish track crews again when the unit asks who paid. For today, keep the engine metaphor in front of students. An engine does no work by itself. It powers other machines. The argument of the reading is that railroads powered steel, oil, telegraphy, and the modern corporation, and that each of those then powered the railroads in return. Hold students to that standard at the exit ticket: an answer that only says trains were fast names the transport gain and misses the system.")

# --------------------------------------------------- 3 · THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'One line becomes a system', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'One line across the continent', 'Two companies meet in Utah, May 10, 1869'),
        ('B', 'A network, not a single road', '30,000 miles becomes 193,000, and one national market'),
        ('C', 'Standards the network required', 'One gauge for the track, one time for the clocks'),
        ('D', 'Steel', 'The Bessemer process makes steel cheap, and by the ton'),
        ('E', 'Oil', 'Refineries turn crude oil into kerosene and reward size'),
        ('F', 'Wires and money', 'The telegraph coordinates, the corporation pays')]
yy = 2.72
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=23, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.6, 0.6, t, size=20, color=CREAM, bold=True)
    text(s, 6.35, yy + 0.06, 6.1, 0.6, d, size=16, color=POWDER)
    yy += 0.70
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. We start with a single event, the completion of the first transcontinental line in 1869, and then refuse to stop there. Section B shows that the line was the start of a network, and that the network created one national market. Section C shows the standards, gauge and time, that a network had to impose on the whole country to work at all. Sections D and E take up the two industries the network carried and created, steel and oil. Section F closes with the two tools that held the system together and paid for it: the telegraph and the corporation. Tell students the final table in their guided notes, The System at a Glance, asks them to rebuild exactly this map from memory.")

# ------------------------------------------------- 4 · SECTION A DIVIDER
divider_photo('promontory-port.jpg', 'Section A', 'One Line Across the Continent',
              ['Two railroads build toward each other', 'and meet in Utah Territory'],
              "The photograph is Andrew J. Russell's picture of the ceremony at Promontory Summit on May 10, 1869, taken for the Union Pacific Railroad. Point out what the image actually shows before we romanticize it. Two locomotives stand nose to nose. The men in suits in the center are officials. The men on the engines and in the foreground are the crews, and hundreds more workers stand outside the frame. One caution for students: the famous golden spike ceremony was a staged celebration of a business and government achievement, not the end of the work. Track gangs kept laying rail in every direction for thirty more years. That gap between the ceremony and the system is the subject of this lesson. Section A covers only the meeting itself and how it was paid for and built. The network, which is where the real significance sits, belongs to section B.",
              title_size=40)

# ------------------------------------------------------ 5 · THE MEETING
content_text('Two roads, one meeting point',
             ['The two roads met on May 10, 1869, at Promontory Summit, Utah Territory.',
              'The Central Pacific built east from Sacramento, across the Sierra Nevada.',
              'The Union Pacific built west from Omaha, across the Great Plains.',
              'From that day, travelers and freight could cross the continent without leaving the rails.'],
             "Give students the geography precisely, because the guided notes test the two directions and students routinely reverse them. The Central Pacific built east from Sacramento, California, across the Sierra Nevada. The Union Pacific built west from Omaha, Nebraska, across the Great Plains. They met at Promontory Summit in Utah Territory on May 10, 1869, and completed the first transcontinental railroad. In the guided notes vocabulary, a transcontinental railroad is a railroad line connecting the eastern rail network with the Pacific coast, and students will meet that definition again on the vocabulary slides. Stress what changed on that single day. Before it, a trip across the continent took months by wagon or weeks by ship around South America or across Panama. From that day, passengers and freight could cross the continent without leaving the rails. That is a transport fact. The economic consequences take the rest of the lesson to unfold.",
             kick='A · One line across the continent')

# ------------------------------------------------------ 6 · PAID FOR AND BUILT
content_text('The government paid, immigrants built',
             ['The Pacific Railway Act of 1862 gave federal loans and grants of public land.',
              'Crews graded the roadbed, blasted tunnels through granite, and laid track by hand.',
              'The Central Pacific relied mostly on Chinese immigrant workers.',
              'The Union Pacific employed many Irish immigrants and Civil War veterans.'],
             "Two facts in this section keep the celebration honest, and both are tested in the guided notes. First, the line existed because the federal government paid for much of it. The Pacific Railway Act of 1862 offered the two companies federal loans and grants of public land along the route. Private companies took the profit, but public money and public land carried much of the risk, a pattern students will see again in this unit. Second, even with that help, the work was immense and it was done by hand. Crews graded roadbed, blasted tunnels through granite, and laid track by hand. The Central Pacific relied heavily on Chinese immigrant workers, who made up most of its workforce. The Union Pacific employed many Irish immigrants and Civil War veterans. When the unit question later asks who paid for industrial growth, this slide is one answer: immigrant workers paid with their labor, and in the Sierra tunnels, often with their lives.",
             kick='A · One line across the continent', size=24)

# ------------------------------------------------- 7 · SECTION B DIVIDER
divider_photo('refrigerator-port.jpg', 'Section B', 'A Network, Not a Single Road',
              ['The 1869 line was a beginning.', 'What followed was a network.'],
              "The photograph shows a Union Refrigerator Line refrigerator car, photographed in 1895 and lettered for dairy products. Be precise with students about what they are looking at. The car in the picture carried dairy products, according to its own lettering. The reading's famous example is a Chicago packinghouse shipping dressed beef to Boston in refrigerator cars cooled with ice, and both cargoes moved in the same kind of ice cooled car shown here. The date matters too. This car belongs to 1895, late in our period, when the network the lesson describes was mature. A refrigerator car is the right emblem for section B. It only makes sense inside a system: ice harvested and stored along the route, schedules reliable enough to promise delivery, and a market a thousand miles away waiting for the cargo. One line of track explains none of that. A network explains all of it.",
              title_size=40)

# ------------------------------------------------------ 8 · ONE LINE BECOMES A NETWORK
content_text('One line became a network',
             ['New lines tied mines, farms, and cattle ranges to factories and ports.',
              'Towns on the lines became shipping points for whole regions.',
              'Towns the rails passed by often faded.',
              'Before the rails, goods moved slowly and at high cost by wagon, river, or canal.'],
             "The reading's key sentence is that the transcontinental line mattered less as a single road than as the start of a network, and this slide unpacks the network's geography. New lines tied mines, farms, and cattle ranges to factories and ports, so raw materials and food moved toward industry and finished goods moved back. The network also sorted places. Towns on the lines became shipping points for whole regions, collecting the produce of a wide countryside at one depot. Towns the rails passed by often faded, because trade followed the track. Contrast that with what came before. Most goods had moved slowly and at high cost by wagon, river, or canal, and rivers freeze, canals freeze, and wagons crawl. Railroads carried heavy loads in all seasons at a fraction of the wagon cost. The next slide puts the growth of that network into a single number students should remember.",
             kick='B · A network, not a single road')

# ------------------------------------------------------ 9 · MILEAGE STAT
stat('193,000', 'miles of railroad in the United States by 1900',
     'About 30,000 miles in 1860 and about 93,000 miles in 1880. The line completed in 1869 was the start of this growth, not the whole of it.',
     "Dwell on the three numbers, all of them from the reading, because together they convert a ceremony into a trend. Railroad mileage in the United States grew from about 30,000 miles in 1860 to about 93,000 miles in 1880 and about 193,000 miles by 1900. Do the arithmetic aloud. The network more than tripled in the twenty years after the Civil War, then more than doubled again in the next twenty. That is why the guided notes ask only for the first and last figures, 30,000 and 193,000: the exit ticket's first question asks students to explain why the transcontinental railroad was a beginning rather than an end, and these two numbers are the evidence. A beginning is something that leads somewhere. The 1869 line led to a network more than six times the size of the entire national system that had existed nine years before it was built.",
     kick='B · A network, not a single road')

# ------------------------------------------------------ 10 · ONE NATIONAL MARKET
content_text('One national market',
             ['Railroads carried heavy loads in all seasons at a fraction of the wagon cost.',
              'A Chicago packinghouse shipped dressed beef to Boston in refrigerator cars.',
              'A Pennsylvania mill drew iron ore, coal, and limestone from three states.',
              'Sellers competed nationally, and the largest scale usually won.'],
             "This slide carries the economic heart of the lesson, so slow down. A connected network changed what a business could do. Before the railroads, most manufacturers served nearby customers, because distance ate the profit. Once railroads carried heavy loads in all seasons at a fraction of the wagon cost, distance stopped protecting local producers. The reading gives two examples, and students should be able to use either one. A Chicago packinghouse could ship dressed beef to Boston in refrigerator cars cooled with ice. A Pennsylvania mill could draw iron ore, coal, and limestone from three different states. The conclusion follows, and it drives the rest of the unit: sellers now competed in one national market, and the winners in that market were usually the firms that could produce and ship at the largest scale. Keep that sentence in view. Sections D and E are both stories of scale winning.",
             kick='B · A network, not a single road')

# ------------------------------------------------- 11 · SECTION C DIVIDER
divider_photo('timezones-port.jpg', 'Section C', 'Standards the Network Required',
              ['One gauge for the track.', 'One time for the clocks.'],
              "The image is a crop from the Burlington Route map of 1892, published by the Chicago, Burlington and Quincy Railroad, and students can read the words Central Time and Mountain Time printed across the states at the top of the crop. Say the date plainly, because it is not the date in the lesson. This map was printed in 1892, nine years after the railroads adopted standard time in 1883. It does not show the moment of adoption. It shows the zone system in normal operation, as a selling point in a railroad's own advertising, which is its own kind of evidence: within a decade, railroad time had become ordinary enough to print on a poster. Section C covers the two standards the network forced on the country, the width of the track and the reading of the clock. Both look technical. Both reorganized daily life for everyone, including people who never rode a train.",
              title_size=38)

# ------------------------------------------------------ 12 · ONE GAUGE
content_text('One gauge for the track',
             ['Gauges differed from line to line in the early years.',
              'Freight was unloaded and loaded again wherever the gauge changed.',
              'Companies gradually settled on one standard gauge.',
              'In 1886, the southern railroads converted thousands of miles in days.'],
             "Gauge means the distance between the rails, and in the early years it differed from line to line, because each company had built to its own choice. The cost of that variety fell on every shipment. Wherever the gauge changed, freight had to be unloaded and loaded again, by hand, from one company's cars into another's. A network with breaks at every junction is not really a network. Companies gradually settled on one standard gauge, so cars could run through from line to line. The dramatic moment came in 1886, when the southern railroads converted thousands of miles of track to the standard gauge in a matter of days, moving one rail of each line by a few inches in a coordinated operation. Students do not need to admire the logistics for their own sake. The point is standardization itself: a national system requires shared rules, and the railroads, not Congress, set this one.",
             kick='C · Standards the network required')

# ------------------------------------------------------ 13 · ONE TIME
content_text('One time for the clocks',
             ['Every town kept local time, set by the sun.',
              'Schedules were nearly impossible to coordinate across lines.',
              'On November 18, 1883, the railroads adopted standard time.',
              'The continent was divided into four zones, with uniform time inside each zone.',
              'Cities and towns soon set their clocks by railroad time.'],
             "Time posed the same problem as gauge, and its solution is the second standard tested in the guided notes. Every town kept local time set by the sun, so noon in one town was minutes away from noon in the next, and printed schedules across lines were nearly impossible to coordinate. On November 18, 1883, the railroads adopted standard time, dividing the continent into four zones with uniform time inside each zone. In the guided notes definition, standard time is a system of uniform time zones that replaced local solar time, and students will write that definition again on the vocabulary slides. Note who acted. No law required this. The railroads imposed a national standard because their business needed one, and cities and towns soon set their clocks by railroad time. Private companies had reorganized the country's day, and almost nobody objected, because the system plainly worked.",
             kick='C · Standards the network required', size=25)

# ------------------------------------------------- 14 · SECTION D DIVIDER
divider_text('Section D', 'Steel',
             'The network ran on steel, and steel had to become cheap.',
             "Pause before the process and set the problem in one sentence. The network ran on steel, and steel had to become cheap. Iron had built the first railroads, but iron rails wore out quickly under heavy traffic, and a system carrying the traffic described in section B was consuming rails, bridges, and machines at a pace iron could not sustain economically. Steel lasted far longer, but steel had long been a costly specialty metal, made in small batches for tools and blades. The gap between what the network needed and what steel cost is the problem this section solves. The solution is a process, not a discovery of new material: a way of making the old metal so fast and so cheaply that the economics of the whole system changed. Students should watch for the feedback loop at the end of the section, because it is the lesson's clearest picture of one industry powering another.")

# ------------------------------------------------------ 15 · STEEL BY THE TON
content_photo_s('bessemer-port.jpg', 'Steel by the ton',
              ['Iron rails wore out quickly under heavy traffic.',
               'The Bessemer process blew air through molten iron.',
               'Impurities burned out in minutes.',
               'Steel was made by the ton, not by the pound.',
               'American mills took up the process in the 1870s.'],
              "The photograph shows a Bessemer converter shop floor, and its date needs saying plainly: the picture was taken between 1890 and 1908, later than the 1870s adoption described in the reading. It shows the process at mature industrial scale, not the first experimental converters. The process itself is simple to state, and the guided notes test its one mechanism. In the Bessemer process, air blown through molten iron burns out impurities in minutes, so a single converter could produce steel by the ton instead of by the pound. In the guided notes definition, the Bessemer process is a method for making steel quickly and cheaply by blowing air through molten iron. American mills took up the process in the 1870s, and output climbed steadily. The vocabulary point and the economic point are the same: minutes and tons. Speed is what made steel cheap, and cheapness is what let steel replace iron across the whole network.",
              kick='D · Steel', )

# ------------------------------------------------------ 16 · CARNEGIE LOOP
content_text('Carnegie and the feedback loop',
             ['Andrew Carnegie built his mills near Pittsburgh.',
              'He controlled every step, from ore and coke to finished rails.',
              'Cheap steel meant longer-lasting rails.',
              'Stronger bridges and bigger machines followed.',
              'Each raised the scale at which industry could operate.'],
             "Andrew Carnegie is the human face of this section, and the reading gives him one precise strategy. Carnegie built his mills near Pittsburgh and controlled every step of production, from ore and coke to finished rails. Owning each step let him cut the costs that competitors paid to middlemen, and students will meet this pattern again in the next lesson under its formal name. Then close the loop the reading draws, because it is the argument of the whole lesson in miniature. Cheap steel fed back into the whole system. It meant longer lasting rails, stronger bridges, and bigger machines, each of which raised the scale at which industry could operate. The railroads created the demand that made cheap steel profitable. Cheap steel then made the railroads, and every industry they served, bigger and cheaper to run. Neither industry explains itself alone. That interdependence is exactly what the word system means in this lesson.",
             kick='D · Steel')

# ------------------------------------------------- 17 · SECTION E DIVIDER
divider_photo('refinery-port.jpg', 'Section E', 'Oil',
              ['A novelty in 1859.', 'A system by the early 1880s.'],
              "The photograph shows the Standard Oil Company's Walworth Run refinery in Cleveland in 1870, and its modesty is the teaching point. These are wooden sheds and simple stills on a muddy creek bank, photographed a decade after the first successful oil well. Nothing in the picture looks like the master of an industry. Yet this small plant belonged to the company that, by the early 1880s, controlled most of the refining capacity in the United States. Hold that contrast for students. Section E tells the same story as section D with the materials reversed. In steel, a process made production cheap and favored the biggest mills. In oil, a product was nearly worthless until a plant processed it, processing was cheaper at large scale, and the railroads rewarded the largest shippers with lower rates. Technology and transport together pushed both industries toward a few very large firms, and students should be able to state that shared pattern in their own words.",
              title_size=54)

# ------------------------------------------------------ 18 · FROM A WELL TO A SYSTEM
content_text('From a well to a system',
             ['In 1859, Edwin Drake drilled a successful well near Titusville, Pennsylvania.',
              'Crude oil by itself was worth little.',
              'A refinery separated it into useful products.',
              'Above all, kerosene lit lamps across the country and abroad.'],
             "Oil begins as a novelty, and students should feel how small the beginning was. In 1859, Edwin Drake drilled a successful well near Titusville, Pennsylvania, and set off a rush for petroleum. The rush produced a glut of a substance nobody could use as it came from the ground. Crude oil by itself was worth little. A refinery separated it into useful products, above all kerosene, which lit lamps across the country and abroad. In the guided notes definition, a refinery is a plant where crude oil is separated into useful products such as kerosene. That definition explains the industry's economics. The value sat in the processing, not in the well. Whoever controlled the processing controlled the industry, which is why the next slide belongs to a refiner rather than to a driller. Drake found the oil. John D. Rockefeller organized the system that made oil an industry.",
             kick='E · Oil')

# ------------------------------------------------------ 19 · ROCKEFELLER
content_text('Rockefeller and the logic of size',
             ['A large refinery processed crude more cheaply than a small one.',
              'Railroads gave their largest shippers lower rates.',
              'John D. Rockefeller organized Standard Oil on that logic.',
              'By the early 1880s, Standard Oil controlled most refining capacity in the United States.',
              'Tank cars and pipelines replaced the wooden barrel.'],
             "This slide states the logic of size in its purest form in the lesson, and it is worth walking step by step. Refining rewarded size, because a large refinery processed crude oil more cheaply than a small one. The railroads then doubled the advantage, because they gave their largest shippers lower rates, so the biggest refiner also paid the least to move his product. John D. Rockefeller organized Standard Oil on that logic, and by the early 1880s the company controlled most of the refining capacity in the United States. The reading's answer key asks students to pair this story with steel, and the pairing is exact: in both industries, a technical change made large scale production cheap, and cheap production favored the largest firms. Close with the transport detail. Tank cars and pipelines then replaced the wooden barrel as the normal way to move oil, one more case of the railroad network reshaping the industry it carried.",
             kick='E · Oil', size=24)

# ------------------------------------------------- 20 · SECTION F DIVIDER
divider_text('Section F', 'Wires and Money',
             'The telegraph tied the system together. The corporation raised the money to build it.',
             "The last section holds the system together and pays for it, and the two halves belong in one section because each made the other useful. A railroad network of 193,000 miles could not be run by mail. Orders, prices, and schedules had to move faster than the trains themselves, and the telegraph supplied that speed. At the same time, none of the construction in this lesson could be paid for out of ordinary profits. A railroad was the largest business enterprise of its time, and its cost exceeded what any single owner or partnership could risk. The corporation answered that problem by pooling the savings of thousands of investors. Tell students to listen for the closing claim of the reading in this section: industrial growth was one system, in which rails carried the products of steel mills and refineries, wires coordinated the traffic, and corporations raised the money to build at continental scale.")

# ------------------------------------------------------ 21 · THE TELEGRAPH
content_photo_s('western-union-port.jpg', 'The telegraph tied it together',
              ['Telegraph lines were strung beside the tracks.',
               'The transcontinental telegraph was completed in 1861, eight years before the railroad.',
               'A Chicago manager learned New York prices within minutes.',
               'A manager could order cars and redirect a shipment still moving.',
               'Then came the telephone in 1876 and Edison lighting in 1882.'],
              "The image is a lithograph, from about 1875, of the Western Union Telegraph Building in New York, the headquarters of the company that dominated the wires; it is a print, not a photograph, and it shows how large a telegraph company had already become. The wires themselves matter more than the building. Telegraph lines were strung beside the tracks, and the transcontinental line was completed in 1861, eight years before the railroad itself, a date the guided notes ask for directly. In the guided notes definition, a telegraph is a system for sending coded messages over wires. Its business value was speed applied to decisions: a manager in Chicago could learn prices in New York within minutes, order cars where they were needed, and redirect a shipment while it was still moving. Later inventions extended the pattern: the telephone, patented in 1876, sped communication inside cities, and Edison's electric lighting system, first operated on a district scale in New York in 1882, lengthened the working day.",
              kick='F · Wires and money')

# ------------------------------------------------------ 22 · THE CORPORATION
content_text('The corporation raised the money',
             ['A railroad was the largest business enterprise of its time.',
              'Building one required capital no single owner could supply.',
              'Investors bought shares and risked only the money they put in.',
              'The law treated the corporation as distinct from its owners.',
              'Stocks and bonds sold across the United States and Europe.'],
             "End the content where the reading ends, with the money. None of this system could be paid for out of ordinary profits. A railroad was the largest business enterprise of its time, and building one required capital, money or property used to start or expand a business, on a scale no single owner could supply. The corporation answered that problem. Investors bought shares, and the law treated the corporation as distinct from its owners, so an investor risked only the money put in. In the guided notes definition, a corporation is a business owned by shareholders and treated by law as distinct from its owners. Railroads sold stocks and bonds across the United States and Europe, drawing continental savings into continental construction, and the same corporate form soon organized the steel, oil, and telegraph industries. The form outlived the building boom: it is still how the largest American businesses are owned.",
             kick='F · Wires and money', size=24)

# ------------------------------------------------------ 23 · THE SYSTEM AT A GLANCE
s = slide(NAVY)
kicker(s, 'The system at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Four parts, one system', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Steel', 'Made cheap rails, bridges, and machines', 'The network ran on it and consumed it'),
        ('Oil refining', 'Turned crude oil into kerosene and products', 'Tank cars and pipelines moved with the rails'),
        ('Telegraph', 'Moved prices and orders faster than trains', 'Lines ran beside the tracks and coordinated traffic'),
        ('Corporation', 'Pooled the savings of thousands of investors', 'It alone could raise railroad scale capital')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, The System at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The four rows are the system's working parts. Steel made the cheap rails, bridges, and machines, and the network both ran on steel and consumed it in enormous quantities. Oil refining turned a nearly worthless raw material into kerosene and other products, and its tank cars and pipelines moved inside the railroad system. The telegraph moved prices and orders faster than any train, coordinating traffic along lines strung beside the tracks. The corporation pooled the savings of thousands of investors and was the only form that could raise capital at railroad scale. Grade the table generously on wording and strictly on logic: each entry must say what the part did and why the railroads needed it, in the student's own words.")

# ------------------------------------------------------ 24 · VOCAB A
vocab('Words for the road and the works',
      [('transcontinental railroad', 'a railroad line connecting the eastern rail network with the Pacific coast'),
       ('Bessemer process', 'a method for making steel quickly and cheaply by blowing air through molten iron'),
       ('refinery', 'a plant where crude oil is separated into useful products such as kerosene'),
       ('corporation', 'a business owned by shareholders and treated by law as distinct from its owners')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. A transcontinental railroad: a railroad line connecting the eastern rail network with the Pacific coast. Note that the definition says the eastern rail network, not the East Coast in general; the feat of 1869 was joining an existing system to the Pacific. The Bessemer process: a method for making steel quickly and cheaply by blowing air through molten iron. Quickly and cheaply are the load bearing words, because speed is what produced cheapness. A refinery: a plant where crude oil is separated into useful products such as kerosene. Separated is the key verb; a refinery does not make oil, it divides crude oil into things people can use. A corporation: a business owned by shareholders and treated by law as distinct from its owners. The legal separation is the definition's point, and it is what limited an investor's risk to the money put in.")

# ------------------------------------------------------ 25 · VOCAB B
vocab('Words for the money, the wires, and the clock',
      [('capital', 'money or property used to start or expand a business'),
       ('telegraph', 'a system for sending coded messages over wires'),
       ('standard time', 'a system of uniform time zones that replaced local solar time')],
      "Three more terms, again matching the guided notes exactly. Capital: money or property used to start or expand a business. Students often reduce capital to cash, and the definition corrects them; land, equipment, and buildings committed to a business are capital too, which is why the land grants of 1862 functioned as capital for the railroads. Telegraph: a system for sending coded messages over wires. Coded is the precise word. The telegraph did not carry voices; operators translated words into electrical signals and back, which is why messages were short and why speed, not conversation, was its gift to business. Standard time: a system of uniform time zones that replaced local solar time. Local solar time meant noon arrived when the sun stood highest in each separate town. The railroads replaced hundreds of local times with four zones, and the whole country still lives on their framework.")

# ------------------------------------------------------ 26 · CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Why did railroads become the engine of a national industrial economy? Build the answer as a system, not a list.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'Network Map stations: trace a carload of beef, a steel rail, a barrel of oil, a telegram'),
        ('Notebook', 'Notebook page: rebuild the system at a glance in your own words'),
        ('Quick check', 'The Meeting at Promontory: the 1869 line and what it started'),
        ('Writing', 'The Engine of an Economy: the lesson question as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: a beginning not an end, the two standards, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, Network Map, runs four stations tracing one shipment through each part of the system: a carload of beef, a steel rail, a barrel of oil, and a telegram. Students who can follow all four traces own the system, not just the vocabulary. The notebook page asks them to rebuild the system at a glance themselves. The quick check, The Meeting at Promontory, tests the 1869 line and the standards. The writing task, The Engine of an Economy, turns the lesson question into an essay. The strongest essays will argue the system claim: railroads created the national market, set its standards, created the demand for cheap steel, carried the oil industry, coordinated business by telegraph, and spread the corporation. The exit ticket has three parts: why the 1869 line was a beginning rather than an end, the two standards and the problem each solved, and the lesson question answered in two or three sentences with at least two facts. Next lesson takes up the men who built empires out of this scale.")

dc.save(OUT)
