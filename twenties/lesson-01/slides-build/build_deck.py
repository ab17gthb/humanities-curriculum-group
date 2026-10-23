#!/usr/bin/env python3
"""The Twenties Lesson 1 deck, "The Business of America," built to the approved
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

# ---------------------------------------------------------------- 1 · TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'THE TWENTIES · LESSON 1', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Business of America', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'How making goods by the million created buying by the million', size=17, color=POWDER)
notes(s, "This photograph shows the moving assembly line inside the Ford Motor Company plant at Highland Park, outside Detroit, in 1913, and its date needs saying plainly at the start: the picture belongs to 1913, before the decade this unit studies, because the system the lesson describes was built just before the Twenties and then filled the Twenties. Chassis stand at successive stages of completion while the workers stay in one place. Open the unit here. The decade is often remembered for music and parties, but its deepest change was economic. A new way of making goods joined a new way of selling and buying them, and together they remade daily life. This lesson follows that joining part by part: the line, wages, electricity, advertising, credit, chain stores, and radio, in the order of the guided notes. Students should leave able to answer the lesson question as one system, with prices and figures, not as two separate lists.")

# ------------------------------------------------- 2 · LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did mass production and mass consumption remake American economic life in the 1920s?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the prosperity of the 1920s change American life, and why was that prosperity weaker than it looked?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question is the narrower one on the slide, and the unit question runs beneath it as the frame for the whole Twenties unit. Notice the last clause of that unit question, about prosperity being weaker than it looked. Keep it in reserve today. This lesson builds the strong side of the story first: output rose, prices fell, wages at Ford doubled on paper, and goods spread into ordinary homes. The weaknesses are already visible inside the success, and students should be asked to spot them as they appear. The five dollars came with conditions and home inspections. Installment buying committed wages before they were earned. Chain store prices rested on squeezing out the independent merchant. Later lessons take up the farm economy, uneven income, and the crash. For today, hold students to the system standard at the exit ticket: an answer about factories alone, or about shopping alone, earns only partial credit, because the reading's claim is that the two sides fed each other.")

# --------------------------------------------------- 3 · THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Making and buying become one system', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The line at Highland Park', 'A moving line, one task per worker, 1913'),
        ('B', 'Five dollars a day', 'Pay roughly doubled, with conditions, 1914'),
        ('C', 'Electricity and appliances', 'Motors in the factory, wiring in the home'),
        ('D', 'Selling the goods', 'Advertising teaches desire, nationally'),
        ('E', 'Buying on time', 'Part down, the rest in weekly or monthly payments'),
        ('F', 'Chain stores', 'One company, one plan, thousands of outlets'),
        ('G', 'Radio and one system', 'Sponsored programs carry brands into the parlor')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Sections A and B cover production and the wage that production made necessary: the moving line at Highland Park and the five-dollar day that followed it by a few months. Section C follows electric power out of the factory and into the home, where wiring created a market for appliances. Sections D, E, and F cover the selling side in order: advertising that taught desire, installment buying that supplied credit, and chain stores that cut the cost of getting goods to buyers. Section G closes with radio and with the reading's final claim, that production and consumption were one system in which each part fed the others. Tell students the table at the end of their guided notes, The System at a Glance, asks them to rebuild exactly this map from memory.")

# ------------------------------------------------- 4 · SECTION A DIVIDER
divider_photo('highland-port.jpg', 'Section A', 'The Line at Highland Park',
              ['The work came to the worker.', 'The car moved. The man stayed.'],
              "The photograph is the Library of Congress picture of the Highland Park plant in 1913, the same image as the title slide in a tighter crop, and the date deserves one sentence: it was taken in 1913, before the Twenties, in the first year of the moving line itself. Look at what the frame actually shows. Chassis stand at successive stages of completion, each one further built than the last, inside a plant built around the line's path. Nothing in the picture is decorative. The building, the spacing, and the men's positions all serve one arrangement, in which a partly built car travels and a worker repeats a single task as it passes. Section A covers that arrangement and its two measurable results: the collapse in the time needed to build a chassis, and the fall in the price of the finished car. Both results are in the guided notes as blanks, so students should have pencils ready for numbers from here on.",
              title_size=40)

# ------------------------------------------------------ 5 · THE WORK CAME TO THE WORKER
content_photo('modelt-port.jpg', 'One design, no fitting',
              ['1913: Ford began moving chassis on a powered line at Highland Park',
               'Before the line: a crew built one chassis where it stood',
               'On the line: each worker stayed in one place, one task on every car',
               'Every Model T built to one design, with interchangeable parts',
               'No fitting needed at any station'],
              "The photograph shows an early Model T touring car on display, from a Library of Congress glass negative dated 1908 in the catalog listing. The early date is the point: the car predates the moving line by five years. Ford first fixed the product, then rebuilt the factory around it. In the guided notes definition, the Model T is the low priced automobile built by the Ford Motor Company from 1908 to 1927 and sold to millions of ordinary buyers. Because every car was built to one design with interchangeable parts, no fitting was needed at any station. An assembly line, in the guided notes definition, is a factory arrangement in which a product moves past workers who each add one part or perform one task until the product is finished. Before the line, a crew gathered around one chassis and built it where it stood. On the line, the work came to the worker instead, and the same motion repeated on every chassis that passed.",
              kick='A · The line at Highland Park')

# ------------------------------------------------------ 6 · PRICE STAT
stat('$260', 'the price of a Ford runabout in 1925, the cheapest Model T',
     'Touring car: about $850 in 1909, about $360 in 1916 · Chassis time: twelve and a half hours of labor down to an hour and a half',
     "Dwell on the price series, all of it from the reading, because it converts a factory arrangement into something a family could feel. A touring car that sold for about $850 in 1909 sold for about $360 in 1916, and the runabout, the cheapest model, reached $260 in 1925. Behind the prices sits the time figure, and students should connect the two aloud. Building a chassis had taken about twelve and a half hours of labor in the fall of 1913. By the spring of 1914 the line had cut the time to about an hour and a half. That gain is productivity, in the guided notes sense of output for each hour of labor, and Ford passed much of the saving to buyers instead of keeping it all as profit. The result was scale: Ford built more than a million cars a year by the early 1920s, and mass production became the normal way American factories worked. Cheapness and volume were not two facts. Each one caused the other.",
     kick='A · The line at Highland Park')

# ------------------------------------------------- 7 · SECTION B DIVIDER
divider_text('Section B', 'Five Dollars a Day',
             'The line solved a production problem and created a labor problem.',
             "Set up the puzzle of this section before any figures. The line made each car far cheaper to build, but it did so by making the work fast, fixed in pace, and endlessly repeated. A worker performed the same motion on every chassis, at the line's speed, all shift long. Men who had built whole cars now tightened the same part hundreds of times a day, and they responded in the simplest way available to them: they quit. Turnover on that scale threatened the whole gain, because a line staffed by constant beginners cannot hold its pace or its quality. Ford's answer, announced at the start of 1914, became the most famous wage in American industry: five dollars a day. This section gives the announcement, the arithmetic behind it, and then the fine print, because the fine print is where the lesson's argument lives. The exit ticket's first question turns entirely on the difference between the headline and the fine print.")

# ------------------------------------------------------ 8 · THE TURNOVER PROBLEM
content_photo('workers-port.jpg', 'The line drove workers away',
              ['Fast work, fixed in pace, endlessly repeated',
               'Workers quit in large numbers',
               '1913: about 53,000 men hired to keep about 14,000 jobs filled',
               'January 5, 1914: Ford announced the five-dollar day',
               'Pay roughly doubled; the shift fell from nine hours to eight'],
              "The photograph shows Ford assembly line workers in 1913, the very year of the turnover figures in the reading, and its date should be stated: 1913, before the Twenties, in the year Ford had to hire about 53,000 men to keep about 14,000 jobs filled. Do that arithmetic aloud. The company hired nearly four men for every job it kept filled, which means most new hires left within months. Training replacements cost money, and a line missing experienced hands slows or stops. On January 5, 1914, the company announced the five-dollar day. Pay roughly doubled, the shift fell from nine hours to eight, and a worker could earn in about two months what the cheapest car cost. That last comparison is the one Ford wanted printed, and it was true as far as it went: the men who built the cars could now plausibly buy one. The plan cut turnover sharply. What the five dollars actually was, and who could actually get it, is the next slide.",
              kick='B · Five dollars a day')

# ------------------------------------------------------ 9 · NOT A SIMPLE RAISE
content_text('Not a simple raise',
             ['Base wage: about $2.34 a day',
              'The rest: a share of company profits, paid only under company conditions',
              'Excluded at first: most women, men under twenty-two, new hires',
              'The Sociological Department visited workers at home',
              'The profit share could be lost: drinking, gambling, a dirty house, boarders, failing to save'],
             "This slide is the fine print, and the exit ticket tests it directly, so walk through it slowly. The five dollars was not a simple wage. A worker kept a base wage of about $2.34 a day, and the rest came as a share of company profits, paid only to workers who met company conditions. Most women were excluded at first, as were men under twenty-two and new hires, so the famous wage did not cover the whole workforce even inside Ford. Ford created a Sociological Department whose investigators visited workers at home. A man could lose his profit share for drinking, gambling, a dirty house, taking in boarders, or failing to save. Name the exchange plainly. In return for higher pay, the company claimed authority inside the worker's home, over his habits, his housekeeping, and his savings. The plan worked on its own terms: turnover fell sharply, and the line kept its experienced men. Whether it was generosity, labor policy, or social control is a judgment students can defend either way, with these facts.",
             kick='B · Five dollars a day', size=24)

# ------------------------------------------------- 10 · SECTION C DIVIDER
divider_text('Section C', 'Electricity and Appliances',
             'Electric power carried the new system beyond the automobile plant.',
             "The automobile plant is where the lesson starts, but the system did not stay there, and this short section is the bridge from production to the home. Electric power did two kinds of work in the 1920s. Inside factories, it changed how machines were driven, freeing each machine from the central steam engine and the overhead shafts that had dictated the layout of the older plant. Inside homes, wiring spread from a minority of dwellings to about half of them, and every newly wired house became a market for goods that had not existed a generation earlier. Keep the direction of causation in front of students. The appliances were not a separate story about comfort. Each one was a standardized factory product, made by mass production, sold under a national brand name, and bought, very often, on installments. Section C therefore sets up everything after it: advertising, credit, and chain stores all presuppose a wired home full of branded goods to sell.")

# ------------------------------------------------------ 11 · POWER TO EACH MACHINE
content_text('Power to each machine',
             ['Individual electric motors replaced central steam engines and overhead shafts',
              'Each machine ran on its own power',
              'Homes wired for electricity: about one in six in 1912',
              'By the middle of the 1920s: about half of dwellings'],
             "Two changes sit on this slide, one in the factory and one in the home, and the reading treats them as one development. In factories, individual electric motors replaced central steam engines and overhead shafts, so each machine ran on its own power. A plant no longer had to arrange every machine along a line of shafts, and a single machine could run without turning the whole system. In the home, the share of dwellings wired for electricity rose from about one in six in 1912 to about half by the middle of the 1920s. Students should register how fast that is: within roughly a dozen years, electric light and power went from a minority convenience to the condition of a normal house. Wiring by itself sold nothing except current. What it created was a market, a house by house demand for machines that ran on the new power. The next slide names those machines, and the guided notes ask students to name three of them from memory.",
             kick='C · Electricity and appliances')

# ------------------------------------------------------ 12 · THE WIRED HOME
content_text('The wired home',
             ['Washing machines, vacuum cleaners, electric irons',
              'Toasters, and refrigerators that cooled themselves',
              'The refrigerator ended the daily visit of the iceman',
              'Each appliance: a standardized factory product, a national brand name',
              'Each raised the standard of what a normal home was expected to contain'],
             "Read the appliance list slowly, because the guided notes ask for any three of these five: washing machines, vacuum cleaners, electric irons, toasters, and refrigerators that cooled themselves and ended the daily visit of the iceman. Then make the analytical point, which is the sentence students most often miss. Each appliance was a standardized factory product sold under a national brand name. The same system that built the Model T built the toaster: one design, interchangeable parts, enormous quantities, a falling price. And each appliance raised the standard of what a normal home was expected to contain. That rising standard is the hinge between this section and the next. A refrigerator could only become something a family felt it needed if somebody taught the family to feel the lack of one. Teaching that feeling, at national scale, was the work of advertising, and it is the subject of section D. Ask students to hold one question into the next section: who decided what a normal home contained, the family or the advertiser?",
             kick='C · Electricity and appliances', size=24)

# ------------------------------------------------- 13 · SECTION D DIVIDER
divider_photo('frigidaire-port.jpg', 'Section D', 'Selling the Goods',
              ['Factories making millions of goods', 'needed buyers by the million.'],
              "The image is a full newspaper advertisement for the Frigidaire electric refrigerator from 1922, placed by its distributors Cox and Dance, and students will work with this same advertisement in the activity. Read its two headline claims aloud before explaining anything. The top line says a home is no longer modern without Frigidaire. The large headline says No More Ice. Neither line describes how the machine works in any detail. Both lines sell a standard of life: modernity, cleanliness, and freedom from the iceman's dirt and uncertainty. That is the whole argument of section D in one artifact. Factories that could produce goods by the million needed buyers by the million, and advertising became the tool for finding and teaching them. This advertisement is dated 1922, squarely inside the decade, and it shows the teaching in progress: a machine most families had never owned is presented as something a modern home could no longer be without.",
              title_size=40)

# ------------------------------------------------------ 14 · SOLD MORE THAN THE PRODUCT
content_text('Sold more than the product',
             ['National brands advertised in magazines, on billboards, in newspapers',
              'The copy rarely stopped at describing a product',
              'Advertisements sold cleanliness, health, status, and modern life itself',
              'The family without the product was presented as behind the times',
              'A refrigerator: from a good never owned to a good felt as needed'],
             "In the guided notes definition, advertising is paid public messages that present a product to potential buyers and seek to create a desire to buy it, and the creating of desire is the load bearing phrase. National brands advertised in magazines, on billboards, and in newspapers across the country, so the same message reached every region at once. The copy rarely stopped at describing a product. Advertisements sold cleanliness, health, status, and modern life itself, and presented the family without the product as behind the times. The guided notes ask students to name two of those four things besides the goods themselves, so give them a moment to fix the list: cleanliness, health, status, modern life itself. The result, in the reading's summary, is that advertising turned goods most families had never owned, such as a refrigerator, into goods that families felt they needed. Desire, however, does not pay a bill. The gap between wanting a refrigerator and having its price in hand is the subject of the next section.",
             kick='D · Selling the goods', size=24)

# ------------------------------------------------- 15 · SECTION E DIVIDER
divider_text('Section E', 'Buying on Time',
             'Installment buying closed the gap between desire and price.',
             "Advertising could teach a family to want a car, a radio, or a refrigerator, but wanting did not produce the purchase price, and most of the new goods cost weeks or months of wages. This section covers the financial tool that closed that gap. Installment buying was not invented in the 1920s, but in this decade it spread from a few trades to the center of the consumer economy, covering automobiles, radios, appliances, furniture, and clothing. Treat it even handedly, because the reading does. On one side, it genuinely widened access: families used goods while paying for them, instead of saving for years first, and sales rose at once, which kept factories running at the volume their prices depended on. On the other side, it committed future wages before they were earned and put repossession behind every missed payment. Students who see both sides now will understand, in a later lesson, why a downturn in 1929 turned so quickly into lost cars, lost furniture, and lost homes.")

# ------------------------------------------------------ 16 · PART DOWN, THE REST ON TIME
content_text('Part down, the rest on time',
             ['Part of the price down, the goods taken home at once',
              'The rest in weekly or monthly installments',
              'Interest or a carrying charge added to the price',
              'The plan spread: automobiles, radios, appliances, furniture, clothing',
              'By the middle of the decade: about three quarters of new cars, by some reckonings'],
             "State the mechanism first, in the guided notes definition: installment buying is purchasing a good by paying part of the price at the time of purchase and the rest in regular payments over time, usually with interest or fees added. In the language of the reading, the buyer paid part of the price down, took the goods home, and paid the rest in weekly or monthly installments, with interest or a carrying charge added. In the 1920s the plan spread to automobiles, radios, appliances, furniture, and clothing. Its scale in the largest market is the figure to remember: contemporary estimates held that a large share of new cars, by some reckonings three quarters, were sold on installments by the middle of the decade. Teach the caution in that sentence as well. These were contemporary estimates, not a census, and the reading says so; the honest claim is that installment selling had become the normal way to buy a car, not that the fraction is known exactly.",
             kick='E · Buying on time', size=24)

# ------------------------------------------------------ 17 · FUTURE WAGES, SPENT EARLY
content_text('Future wages, spent early',
             ['A family no longer had to save the full price first',
              'Sales rose at once, and factories kept their volume',
              'The buyer committed future wages before they were earned',
              'Falling behind meant repossession of the goods'],
             "This slide weighs the tool, and students should be able to state both sides in the reading's own terms. Buying on time raised sales at once, since a family no longer had to save the full price first. Payments spread across weeks or months fit a wage earner's income, which brought cars, radios, and appliances within reach of buyers who could never have paid cash. That was not a small thing: it is part of how the goods of the new economy reached beyond the wealthy in this decade. The risk ran alongside the gain from the first payment. The buyer committed future wages before they were earned, paid interest or a carrying charge on top of the price, and faced repossession if payments fell behind: the seller could take the goods back, and the payments already made went with them. Connect this forward, briefly. A system that sells against next year's wages works while wages keep coming. Students should store that sentence for the lessons on 1929, when the wages stopped and the commitments remained.",
             kick='E · Buying on time')

# ------------------------------------------------- 18 · SECTION F DIVIDER
divider_photo('piggly-port.jpg', 'Section F', 'Chain Stores',
              ['Stores reorganized on factory principles.', 'One company, one plan, every town.'],
              "The photograph shows the interior of the original Piggly Wiggly store in Memphis, Tennessee, and its date must be stated plainly: the picture is from 1918, before the 1920s. It is used because it shows the self service chain store form that the 1920s adopted at scale: customers walking the aisles, selecting packaged goods themselves, in a store run to one company's plan. Piggly Wiggly had opened in 1916 as the first self service grocery store. The reading's subject in this section is broader than one company. The goods of the new factories reached buyers through stores reorganized on factory principles, standardized, centrally supplied, and repeated town after town under the same name. The example the guided notes test is the Great Atlantic and Pacific Tea Company, the A and P, whose growth across the decade is the next slide's subject after the reasons for its prices. Shoppers, merchants, and students should all be able to answer one question by the end of the section: why was the chain cheaper?",
              title_size=44)

# ------------------------------------------------------ 19 · WHY THE CHAIN CHARGED LESS
content_text('Why the chain charged less',
             ['Chains bought in carload lots at wholesale prices',
              'They sold for cash, and offered no delivery and little credit',
              'Each store was small, standardized, and cheap to run',
              'The independent merchant bought in small lots and carried customers on credit',
              'Shoppers followed the lower prices; independents organized in protest'],
             "In the guided notes definition, a chain store is one of a group of retail stores owned by a single company, carrying the same name, goods, and prices across many locations. The guided notes ask for two practices that let a chain charge less, and the reading supplies a full list, so give students the whole of it. Chains bought in carload lots from company warehouses and paid wholesale prices an independent buying in small lots could not match. They sold for cash, and offered no delivery and little credit, which removed the cost of those services from the price. Each store was small, standardized, and cheap to run. The independent merchant stood on the other side of every point: he bought in small lots, delivered, and carried his customers on credit, and each service raised his costs. Shoppers followed the lower prices, which is why the chain won, and independent merchants organized in protest, which is the first organized resistance this unit meets. Neither side of that fight was imaginary.",
             kick='F · Chain stores', size=24)

# ------------------------------------------------------ 20 · A AND P STAT
stat('15,000', 'A and P stores by the end of the 1920s',
     'About 4,300 stores in 1920 · The Great Atlantic and Pacific Tea Company, the A and P',
     "Put the two figures together and do the arithmetic aloud. The Great Atlantic and Pacific Tea Company, the A and P, grew from about 4,300 stores in 1920 to about 15,000 by the end of the decade. The chain more than tripled in ten years, opening, on average, close to three new stores a day, every day, for a decade. Numbers on that scale change what a store is. The corner grocer was a neighbor who knew his customers, extended them credit, and answered for his goods personally. The chain store was one outlet of a distant company, run to a plan written elsewhere, competing on price alone. Both descriptions are accurate, and contemporaries argued about which mattered more, which is why the protests of independent merchants belong in this lesson and not only in a later one. For the guided notes, the two blanks are the two numbers on this slide: about 4,300 stores in 1920, about 15,000 by the end of the decade. Students should leave this slide able to pair the growth with the price practices from the slide before it.",
     kick='F · Chain stores')

# ------------------------------------------------- 21 · SECTION G DIVIDER
divider_photo('radio-port.jpg', 'Section G', 'Radio and One System',
              ['Commercial broadcasting began in 1920.', 'Within the decade, millions of families owned sets.'],
              "The photograph, by Harris and Ewing in 1921, shows a family gathered around a radio receiver with a horn speaker, while one boy listens through headphones. Its date is worth stating because it falls inside the decade and at the very start of broadcasting: commercial broadcasting had begun only in 1920, and the horn and headphones in the picture are what home listening looked like in its first years. Radio is the right place to end the lesson, because it did in the home what the telegraph had done for business in an earlier unit: it carried the same content everywhere at once. Sponsored programs carried advertising into the parlor and taught the same brand names to listeners in every region, so the selling system of sections D, E, and F gained a voice inside the house itself. Section G therefore has two jobs: radio as a product of the system, sold on installments and advertised nationally, and radio as the place where the reading states its whole argument in one paragraph.",
              title_size=38)

# ------------------------------------------------------ 22 · ONE SYSTEM
content_text('One system, not two stories',
             ['Standardized goods were cheap because factories made them in enormous quantities',
              'Factories could sell enormous quantities because the selling system moved them',
              'Advertising taught desire; installment plans supplied credit',
              'Chain stores cut distribution costs; higher wages put cash in some hands',
              'Each part fed the others'],
             "Close the content where the reading closes, with its central claim stated as a loop, and ask students to trace the loop around the slide once before anyone writes. Production and consumption were not two separate stories. Standardized goods were cheap because factories made them in enormous quantities, and factories could sell enormous quantities because advertising taught desire, installment plans supplied credit, chain stores cut distribution costs, and higher wages put cash in some workers' hands. Radio then carried the advertising into the home and taught the same brand names in every region. Each part fed the others, and together they remade American economic life. Test the loop by removing parts, as a question: take away installment buying, and who can pay even $260 for a car out of weekly wages? Take away advertising, and why would a family want a refrigerator it had lived without for generations? A system is exactly this: a set of parts each of which makes the others work. That sentence is the standard for the exit ticket's final answer.",
             kick='G · Radio and one system', size=24)

# ------------------------------------------------------ 23 · THE SYSTEM AT A GLANCE
s = slide(NAVY)
kicker(s, 'The system at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Four sides, one system', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Production', 'The line, interchangeable parts, falling prices', 'Cheap goods in enormous quantities to sell'),
        ('Wages', 'Five dollars a day, doubled pay with conditions', 'Cash in some workers hands for cars and goods'),
        ('Consumption', 'Advertising, installment buying, radio', 'Desire taught, credit supplied, brands nationwide'),
        ('Distribution', 'Chain stores buying by the carload', 'Lower prices that independents could not match')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, The System at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The four rows are the system's sides. Production covers the line at Highland Park, interchangeable parts, and the falling price series, and what it fed the other side was cheap goods in enormous quantities. Wages covers the five-dollar day, doubled pay carrying conditions and inspections, and what it fed was cash in some workers' hands, enough in about two months to cover the cheapest car. Consumption covers advertising, installment buying, and radio: desire taught nationally, credit supplied against future wages, and brand names carried into the parlor. Distribution covers the chain stores, buying by the carload and selling for cash, which fed consumption lower prices and fed production a national outlet. Grade the table generously on wording and strictly on logic: each entry must say what changed and what it fed on the other side, in the student's own words.")

# ------------------------------------------------------ 24 · VOCAB A
vocab('Words for the factory',
      [('assembly line', 'a factory arrangement in which a product moves past workers who each add one part or perform one task until the product is finished'),
       ('mass production', 'the making of goods in very large quantities using standardized parts and machinery, so that each item costs less to produce'),
       ('Model T', 'the low priced automobile built by the Ford Motor Company from 1908 to 1927 and sold to millions of ordinary buyers'),
       ('productivity', 'the amount of goods or work produced for each hour of labor or for each unit of input')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. An assembly line: a factory arrangement in which a product moves past workers who each add one part or perform one task until the product is finished. The moving product is the definition's heart; the workers stay, the work travels. Mass production: the making of goods in very large quantities using standardized parts and machinery, so that each item costs less to produce. Note that the definition ends with the result, cheapness per item, not just with size. The Model T: the low priced automobile built by the Ford Motor Company from 1908 to 1927 and sold to millions of ordinary buyers. Ordinary buyers is the phrase to underline; earlier cars had been rich men's goods. Productivity: the amount of goods or work produced for each hour of labor or for each unit of input. The chassis figures, twelve and a half hours down to an hour and a half, are this definition measured.")

# ------------------------------------------------------ 25 · VOCAB B
vocab('Words for the marketplace',
      [('installment buying', 'purchasing a good by paying part of the price at the time of purchase and the rest in regular payments over time, usually with interest or fees added'),
       ('advertising', 'paid public messages that present a product to potential buyers and seek to create a desire to buy it'),
       ('chain store', 'one of a group of retail stores owned by a single company, carrying the same name, goods, and prices across many locations')],
      "Three more terms, again matching the guided notes exactly. Installment buying: purchasing a good by paying part of the price at the time of purchase and the rest in regular payments over time, usually with interest or fees added. Students often forget the last clause, and it is the one that made the tool profitable to sellers and risky to buyers. Advertising: paid public messages that present a product to potential buyers and seek to create a desire to buy it. Paid and create are the two words to stress: the messages cost the seller money, and their purpose was not to inform but to create a desire that had not existed. A chain store: one of a group of retail stores owned by a single company, carrying the same name, goods, and prices across many locations. Sameness is the definition's point. The same name, goods, and prices in every town is what let one company spread its costs across thousands of outlets and undercut the merchant who stood alone.")

# ------------------------------------------------------ 26 · CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did mass production and mass consumption remake American economic life in the 1920s? Build the answer as a system, not a list.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'Consumer Culture Stations: the falling price, five dollars a day, No More Ice, buying on time, the chain store'),
        ('Notebook', 'Notebook page: rebuild the system at a glance in your own words'),
        ('Quick check', 'The Line and the Advertisement: the line, the wage, and the Frigidaire advertisement'),
        ('Writing', 'One System: the lesson question as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: why the five-dollar day was not a simple raise, two parts of the consumption side, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, Consumer Culture Stations, runs five stations through the system: the falling price of the Model T, five dollars a day, the Frigidaire advertisement under its headline No More Ice, a model installment contract for buying on time, and the chain store against the corner store, ending in a verdict on which side of the system did more to remake economic life. The notebook page asks students to rebuild the system at a glance themselves. The quick check, The Line and the Advertisement, tests the line, the wage, and the advertisement. The writing task, One System, turns the lesson question into an essay. The exit ticket has three parts: in one sentence, why the five-dollar day was not a simple raise; two parts of the consumption side of the system, with what each one contributed; and the lesson question answered in two or three sentences with at least two facts from the notes. Next lesson takes up the consumer culture this system created, and the new media and heroes that filled it.")

dc.save(OUT)
