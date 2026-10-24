#!/usr/bin/env python3
"""Lesson 5 deck, "The City," built to the approved Progressive Era system:
image-led slides, fragments only on screen, comprehensive speaker notes,
full lesson + vocabulary coverage. Fonts: Georgia titles, Lato body."""
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

# ---------------------------------------------------------------- 1 · TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'GILDED AGE · LESSON 5', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The City', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'How forty years of growth rebuilt daily life, and strained every system a city runs on', size=17, color=POWDER)
notes(s, "The photograph is Mulberry Street in New York, taken by the Detroit Publishing Company in about 1900. Hold it on screen for a moment before speaking. One street is doing the work of a market, a road, and a front yard at the same time, with tenements rising on both sides and hundreds of residents in a single view. That density is the subject of this lesson. Between 1860 and 1900 the American city grew faster than any institution built to run it: housing, water, transit, and government all had to be reinvented under pressure, and the reinvention was uneven. Frame the day as four systems and one question. Students should leave able to explain how growth changed each system, name the problem growth created inside it, and judge who responded and how well.")

# ------------------------------------------------- 2 · LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did rapid urban growth change daily life, health, and city government?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did industrial growth transform American life, and who gained, who paid, and who resisted?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question is the narrower one on the slide, and the unit question runs beneath it as the frame. This lesson is where the unit question gets concrete at street level. Industrial growth pulled millions into cities, and the transformation was not abstract: it was the size of a family's rooms, the safety of its drinking water, the length of its walk to work, and the honesty of its government. Keep the question's three parts visible in your teaching, because the lesson is built to answer them in order: daily life first, in the tenements and the streets; health second, in the water and waste systems; city government third, in the machine and the reform movements that answered it. The exit ticket returns to this wording, and the writing task asks students to judge the machine by it.")

# --------------------------------------------------- 3 · THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.3, 11.5, 1.0, 'Four systems, one transformation', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.42)
rows = [('A', 'A City Built in a Generation', 'two of every five Americans in a city by 1900'),
        ('B', 'Living Packed Together', 'twenty families, one tap, no windows at the back'),
        ('C', 'Water, Waste, and Disease', 'privies by the wells, and the White Wings answer'),
        ('D', 'Getting Around and Going Out', 'streetcars, suburbs, department stores, baseball'),
        ('E', 'The Machine That Ran the City', 'help by the block, graft by the contract'),
        ('F', 'Reform Begins at Home', 'Hull House and professional city government')]
yy = 2.78
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.7, n, size=24, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.03, 4.6, 0.7, t, size=20, color=CREAM, bold=True)
    text(s, 6.35, yy + 0.08, 6.1, 0.7, d, size=17, color=POWDER)
    yy += 0.74
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, A through F. The first three sections describe what growth did to the physical city: the numbers and the skyline, the housing families actually lived in, and the water and waste systems that decided whether crowding meant disease. Section D turns to the texture of a day, how people moved and how they spent the hours and money left over. Sections E and F are the political pair. The machine filled the gap between what city government was built to do and what a city of millions needed, and reformers answered with settlement houses and a demand for professional administration. Tell students the notebook page tracks exactly these systems, so notes taken in this order will already be organized for review day.")

# ------------------------------------------------- 4 · SECTION A DIVIDER
divider_photo('flatiron-port.jpg', 'Section A', 'A City Built in a Generation',
              ['Two of every five Americans', 'in a city by 1900'],
              "The photograph shows the Flatiron Building in New York under construction in 1902, its steel skeleton exposed before the stone skin went on. Note the date honestly with students: this building rose just after 1900, and it stands here for the building type the reading describes, the steel frame tower of ten stories or more that appeared downtown after the 1880s. The section itself is about scale. In one working lifetime, cities that had been large towns became metropolitan giants, and they did it because work concentrated there. Factories needed workers, railroads needed terminals and warehouses, and ports needed crews, and every arrival needed housing, water, and a way to get to a job at the same moment. Keep that simultaneity in view: the strain in every later section comes from all the needs arriving at once.",
              title_size=44)

# ------------------------------------------------------ 5 · THE NUMBERS
content_text('Drawn by work',
             ['Factories, railroads, and ports drew the newcomers.',
              'Some came from American farms and the rural South.',
              'Others crossed oceans from Ireland, Germany, Italy, eastern Europe, and China.',
              'All of them needed housing, water, and work at once.',
              'New York passed 3.4 million after joining Brooklyn in 1898.'],
             "Give students the human arithmetic behind the guided notes blanks. Chicago held about 112,000 people in 1860, a sizable town, and about 1.7 million in 1900, one of the largest cities on earth. New York passed 3.4 million after it joined with Brooklyn in 1898. Between 1860 and 1900, two of every five Americans came to live in a city. The pull was work: factories, railroads, and ports, the three answers question one of the reading asks for. The newcomers were not one group. Some came from American farms, many crossed oceans from Ireland, Germany, Italy, eastern Europe, and China, and others moved from the rural South. Stress the reading's closing sentence in this section, because it organizes the whole lesson. All of them needed housing, water, and work at once, and a city that could house them slowly or supply them one neighborhood at a time would still fail.",
             kick='A · A city built in a generation')

# ------------------------------------------------------ 6 · CHICAGO STAT
stat('1.7 MILLION', 'people in Chicago in 1900, up from about 112,000 in 1860',
     'One city multiplied roughly fifteen times in forty years. Every system in this lesson, housing, water, transit, and government, had to multiply with it.',
     "Dwell on this number, because it converts an abstraction into a workload. In 1860 Chicago held about 112,000 people. Forty years later it held about 1.7 million. Nothing in the city was designed for the second figure: not the wells, not the housing stock, not the street plan, not the form of government, which still resembled the government of a town. When students picture urbanization as a trend line, the line looks smooth. At street level it was a queue: for rooms, for water, for jobs, for a seat on a streetcar. The statistic also sets the fairness question the unit keeps asking. The growth made Chicago rich and made its port, rail yards, and stockyards nationally essential. It also concentrated the costs on the families who arrived last and could pay least, which is where the next section begins.",
     kick='A · A city built in a generation')

# ------------------------------------------------------ 7 · SKYSCRAPERS
content_photo_s('flatiron2-port.jpg', 'The city goes vertical',
              ['Steel frames and elevators made the skyscraper possible.',
               'Office buildings of ten stories or more rose after the 1880s.',
               'Land near the center was too valuable to leave uncovered.',
               'Builders covered nearly every foot of a lot.'],
              "The second construction view of the Flatiron Building shows the same steel frame from another side, and the frame is the teaching point. Two inventions made the skyscraper possible, and the guided notes test both: steel frames, which carried the building's weight so walls no longer had to, and elevators, which made the upper floors reachable and therefore rentable. After the 1880s, office buildings of ten stories or more rose downtown. The economics underneath matter as much as the engineering. Land near the center became so valuable that builders covered nearly every foot of a lot, and that sentence explains more than offices. The same land pressure that pushed offices upward pushed housing inward, into divided houses and purpose built tenement blocks on narrow lots. Section B is this slide's shadow: the lot economics of downtown applied to the homes of the poor.",
              kick='A · A city built in a generation')

# ------------------------------------------------- 8 · SECTION B DIVIDER
divider_photo('riis-port.jpg', 'Section B', 'Living Packed Together',
              ['Twenty families in one building,', 'and the camera that showed it'],
              "The photograph is Jacob Riis's lodgers in a crowded Bayard Street tenement in New York, taken in 1889 and published in How the Other Half Lives in 1890. Men and women are sleeping in a single small room, on bunks and on the floor, at five cents a spot. Riis himself appears in this lesson twice, as a source and as an argument, and students will work with this photograph directly in the first station of the activity. Set the section plainly. The tenement was where the city's growth was actually lived, and its conditions were not an accident of poverty alone. They were produced by lot sizes, building economics, and the absence of enforced housing rules. What families endured inside these rooms, the crowding, the shared water, the fire risk, is the next slide.",
              title_size=44)

# ------------------------------------------------------ 9 · TENEMENT CONDITIONS
content_photo_s('bandits-port.jpg', 'Inside the tenement',
              ['A single tenement might hold twenty families.',
               'Back rooms often had no outside window.',
               'Whole floors shared one or two toilets.',
               'Water came from a single tap or pump.',
               'Fire spread through wooden stairs and air shafts.'],
              "The photograph is another of Riis's, Bandit's Roost, an alley at 59 and a half Mulberry Street, photographed in 1888 and published in 1890. Use it to make the guided notes blanks physical. Owners divided older houses into small apartments or built cheap new blocks shaped to squeeze more rooms onto a narrow lot, and a single tenement might hold twenty families. Back rooms often had no outside window, so air and light stopped at the hallway. Whole floors shared one or two toilets, sometimes in the yard, and water came from a single tap or pump. Then name the dangers in the reading's order. Fires spread quickly through wooden stairs and air shafts, and coal stoves filled rooms with smoke. Crowding was dangerous as well as uncomfortable, and the next section follows the danger into the water supply.",
              kick='B · Living packed together')

# ------------------------------------------------------ 10 · RIIS
content_text("Riis and a new argument",
             ['Jacob Riis was an immigrant from Denmark.',
              'How the Other Half Lives appeared in 1890.',
              'The camera carried the evidence indoors.',
              'Poverty was a condition of housing and health.',
              'It was not simply a failure of character.'],
             "Jacob Riis matters to this lesson for his argument, not only his photographs. Riis, himself an immigrant from Denmark, worked as a police reporter and recorded tenement conditions in his 1890 book How the Other Half Lives. His photographs showed middle class readers that tenement poverty was a condition of housing and health, not simply a failure of character. That sentence is blank five in the guided notes, and it is the intellectual hinge of the section, so slow down for it. If poverty came from bad character, the remedy was moral advice and charity. If it came from windowless rooms, shared toilets, and contaminated water, the remedy was building codes, inspection, and public systems, which are government remedies. Riis was moving his readers from one diagnosis to the other, and every reform in sections C and F depends on readers making that move.",
             kick='B · Living packed together')

# ------------------------------------------------- 11 · SECTION C DIVIDER
divider_text('Section C', 'Water, Waste, and Disease',
             'A city of millions produced waste on a scale no town had faced, and sanitation lagged far behind population.',
             "Open the section with the scale problem stated in the reading. Horses left manure in the streets by the ton. Households threw ashes, garbage, and dirty water into yards and gutters. Privies stood close to wells, so waste could seep into drinking water. None of these practices was new; what was new was doing them at the density of a tenement district, where one yard served twenty families and one well sat within feet of several privies. The vocabulary word for this section names the counter system: the public measures that keep water, waste, and streets clean enough to protect health. Hold the definition for the vocabulary slide, but use the idea now. Sanitation is a system, not a household habit, and a system needs an organization that can plan, tax, build, and inspect year after year.")

# ------------------------------------------------------ 12 · DISEASE
content_text('Disease followed the water',
             ['Typhoid fever and cholera spread through contaminated water and milk.',
              'Tuberculosis spread through crowded, unventilated rooms.',
              'The answer was built: aqueducts and sewer lines.',
              'Paved roads could be washed.',
              'The systems worked only if government kept working.'],
             "Teach the transmission chains explicitly, because question three of the reading and station two of the activity both test them. Typhoid fever and cholera spread through contaminated water and milk: waste from a privy seeped into a well, or washed into a supply, and the next family drank it. Tuberculosis spread through crowded, unventilated rooms, the back rooms of section B with no outside window. Cities responded by building on a new scale: aqueducts for clean water, sewer lines under the streets, and paved roads that could be washed. Then give students the reading's condition, which is the section's real thesis. These systems worked only when a city government could plan, tax, build, and inspect, year after year. A sewer is not an event; it is a permanent department. That is why a health problem becomes a government problem by the end of this section.",
             kick='C · Water, waste, and disease')

# ------------------------------------------------------ 13 · WARING
content_text('The White Wings',
             ['In New York in 1895, George E. Waring took over street cleaning.',
              'Sweepers wore white uniforms and worked required regular routes.',
              'Garbage was separated from ashes for collection.',
              'Streets were visibly cleaner within months.',
              'A disciplined department could change a city.'],
             "No period photograph of Waring's crews is used in this deck; none with a clear public domain record surfaced in the curriculum image bank, so the slide teaches from the record instead. In New York in 1895, street cleaning commissioner George E. Waring put his sweepers in white uniforms, required regular routes, and separated garbage from ashes for collection. His crews, nicknamed the White Wings, showed that a disciplined public department could change a city within months. Both the name and the nickname are guided notes blanks, so say them slowly and spell Waring. The white uniform was a management tool, not a costume: a sweeper in white could be seen, his route could be checked, and dirt on the uniform showed whether the work was done. Waring is the bridge to sections E and F. New York already had a machine government skilled at favors; Waring showed the alternative, a department run on professional lines.",
             kick='C · Water, waste, and disease')

# ------------------------------------------------- 14 · SECTION D DIVIDER
divider_photo('mulberry-port.jpg', 'Section D', 'Getting Around and Going Out',
              ['The fare decided where', 'a family could live'],
              "The photograph is the portrait crop of the Mulberry Street view from the title slide, the same Detroit Publishing photograph of about 1900, seen closer. Look at what the street is carrying: pushcarts and market stalls, horse drawn wagons, shoppers, and residents using the roadway as open space, because their rooms had none to spare. The activity's third station works with this same photograph, so students who study it now will arrive at the station ahead. This section is about movement and its price. New transit let workers live farther from their jobs than feet could carry them, and that possibility rearranged the city, pulling riders who could pay toward new suburbs at the edge and leaving the poorest in the center. It also changed the city's pleasures: downtown became a destination for shopping and entertainment, sold by the ticket.",
              title_size=44)

# ------------------------------------------------------ 15 · TRANSIT
content_photo_s('bowery-port.jpg', 'Move farther, live farther',
              ['Horse drawn streetcars came first, then cable cars.',
               'Electric trolleys and elevated railways followed.',
               'Riders who could pay settled in streetcar suburbs.',
               'The poorest stayed in the center, and walked.'],
              "The photograph shows the Bowery in New York with elevated railway tracks running above the street and streetcars below. It is one half of a stereograph copyrighted in 1903, just after the period this lesson covers; the elevated lines themselves had carried New Yorkers since the 1870s, so the scene is the period's own, photographed at its edge. Walk the guided notes list in order: horse drawn streetcars, then cable cars, electric trolleys, and elevated railways; any three earn blank eight. Each step raised speed and distance. The social result is the point to land. Riders who could pay the fare settled in new streetcar suburbs at the edge of the city, while the poorest families stayed in the crowded center, close to work they reached on foot. Transit did not simply move the city; it sorted it by income, street by street.",
              kick='D · Getting around and going out')

# ------------------------------------------------------ 16 · GOING OUT
content_photo_s('marshall-port.jpg', 'The city sells the evening',
              ['Department stores filled whole downtown blocks.',
               'Theaters and dance halls sold leisure by the ticket.',
               'Baseball parks drew crowds by the thousand.',
               'The city was harsher than the town, and faster and brighter.'],
              "The photograph is a stereoscopic view inside Marshall Field's store in Chicago, showing a department of decorative goods behind a long counter. Be plain about its date: the Commons record carries no date, and the view shows an early, modest department, well before the full block stores the reading describes. It stands here as the seed of the department store, not its final scale. By the period's end, department stores filled whole downtown blocks, with many departments under one roof and fixed prices, and theaters, dance halls, and baseball parks sold leisure by the ticket. End the section with the reading's balanced sentence, because it keeps students from flattening the city into misery. The city was harsher than the town, and also faster and brighter, and both halves of that judgment are evidence in the exit ticket's third question.",
              kick='D · Getting around and going out')

# ------------------------------------------------- 17 · SECTION E DIVIDER
divider_photo('tweed-port.jpg', 'Section E', 'The Machine That Ran the City',
              ['Help by the block,', 'graft by the contract'],
              "The portrait is William M. Tweed of New York, head and shoulders, from the Library of Congress; the caption card carries no date, and Tweed died in 1878, so treat it as a portrait from his years of power. City governments were not built for the scale this lesson has described, and into the gap stepped an organization that was built for it: the political machine, run ward by ward and block by block by men who knew their neighborhoods by name. This section must be taught as a genuine two sided record, because the writing task asks students to judge it. The machine's help was real, and for many poor families it was the only help available. Its theft was also real, and it raised taxes and rewarded loyalty over competence. Students who can hold both sentences at once are ready for the writing task; students who keep only one are not.",
              title_size=40)

# ------------------------------------------------------ 18 · THE HELP
content_text('Help that arrived in person',
             ['Precinct workers knew their neighborhoods by name.',
              'The machine found jobs, and rent and coal in a hard month.',
              'New immigrants were naturalized, and families were stood by in trouble.',
              'In return, the machine expected votes, and got them.'],
             "Describe the machine from the sidewalk up, as the reading does. At its head stood the boss, whose full definition waits for the vocabulary slide. Below him, precinct workers knew their neighborhoods by name. The machine found supporters jobs, helped families with rent or coal, naturalized new immigrants, and stood by a man arrested or a widow in trouble. In New York, William M. Tweed led the Tammany Hall machine in the late 1860s and early 1870s. Then ask the analytical question the exit ticket will ask: why would voters stay loyal? Because the help was personal, fast, and certain, while the city's formal services were slow, distant, or absent. A family facing eviction did not need a theory of government; it needed coal this week. The machine understood that need and organized it, and in return it expected votes, and it usually got them.",
             kick='E · The machine that ran the city')

# ------------------------------------------------------ 19 · GRAFT
content_photo_s('nast-port.jpg', 'The bill the city paid',
              ['Contractors padded the cost of paving and buildings.',
               'The extra was shared with the politicians who approved it.',
               "The Tweed Ring's theft ran into the tens of millions.",
               'Taxes rose, and loyalty was rewarded over competence.'],
              "The image is the center of a Thomas Nast cartoon from Harper's Weekly in the 1870s, the lesson's own cartoon, cropped to the figure of Columbia standing between the politicians. The full print hangs in the activity's fourth station, where students read its caption and its schoolhouse doors. Now the other side of the ledger. The same system that delivered help also stole. Contractors padded the cost of paving, buildings, and supplies and shared the extra money with the politicians who approved the bills. The Tweed Ring was charged with stealing sums that contemporary estimates placed in the tens of millions of dollars, which is blank twelve in the guided notes. Nast drew for readers who might not read an editorial but could read a picture, and his target was exactly this arrangement. Close honestly, in the reading's own balance: the theft raised taxes and rewarded loyalty over competence, and it coexisted with the help on the previous slide.",
              kick='E · The machine that ran the city')

# ------------------------------------------------- 20 · SECTION F DIVIDER
divider_photo('addams-port.jpg', 'Section F', 'Reform Begins at Home',
              ['Live in the neighborhood,', 'study it, and press the city'],
              "The portrait is Jane Addams of Hull House in Chicago, photographed in 1913 for the National Child Labor Committee collection at the Library of Congress. Note the date plainly: the photograph comes from 1913, after Hull House had been open for more than twenty years, and it stands here for the woman who opened it in 1889. The first reformers in this lesson often started inside the neighborhood itself, and Addams is their model. Where the machine worked a neighborhood for votes, the settlement house worked it for knowledge: live there, learn conditions at first hand, and convert what you learn into demands the whole city must answer. This closing section pairs that neighborhood method with the wider demand it fed, for professional city administration, and students should watch the pair work together on the next two slides.",
              title_size=44)

# ------------------------------------------------------ 21 · HULL HOUSE
content_text('Hull House, 1889',
             ['Jane Addams and Ellen Gates Starr opened Hull House in Chicago in 1889.',
              'Workers lived in the neighborhood they served.',
              'Hull House ran a kindergarten, classes, and childcare.',
              'Its workers studied local conditions, then pressed the city.',
              'They demanded playgrounds, bathhouses, factory inspection, and honest garbage collection.'],
             "Give the facts in the reading's order, because blank thirteen tests three of them. Jane Addams and Ellen Gates Starr opened Hull House in Chicago in 1889. Its workers lived in the neighborhood, ran a kindergarten and classes, studied local conditions, and pressed the city for playgrounds, bathhouses, factory inspection, and honest garbage collection. The definition of the institution waits for the vocabulary slide. The method is what students should carry away. A settlement worker knew which yard held the privy beside the well, which landlord never repaired the stairs, and which factory hired children, because she walked past all three daily. That knowledge made the settlement's demands specific, and specific demands are harder for a city government to wave away than general sympathy. Question five of the reading asks students to judge whether living in the neighborhood made reformers more effective; this slide is their evidence for yes.",
             kick='F · Reform begins at home', size=24)

# ------------------------------------------------------ 22 · PROFESSIONAL GOVERNMENT
content_text('The demand widens',
             ['Trained health officers served, and tenements were inspected.',
              'Civil service hiring replaced patronage jobs.',
              'Mayors were elected on reform tickets: William Strong in New York, 1894.',
              'Reform did not end machine politics.',
              'The argument had changed.'],
             "By the 1890s the settlement houses' pressure joined a wider demand for professional city administration, and blank fourteen asks for any two parts of it, so name all four. Trained health officers. Inspected tenements. Civil service hiring instead of patronage jobs. And mayors elected on reform tickets, as New York elected William Strong in 1894. Each item answers a machine practice directly: the health officer answers the uninspected tenement and the contaminated well; the civil service answers the job given for loyalty. Then end with the reading's honest close. Reform did not end machine politics. But the argument had changed. A growing city needed services that no ward organization, however helpful to its friends, could supply fairly to everyone. That sentence is the lesson's verdict, and it points forward: the demand for professional, inspectable government is one root of the reform era this course takes up next.",
             kick='F · Reform begins at home')

# ------------------------------------------------------ 23 · VOCAB A
vocab('Words for the city itself',
      [('tenement', 'a crowded, often unsafe multi-family apartment building in a city'),
       ('urbanization', 'the growth of cities as people move to them for work and services'),
       ('sanitation', 'public measures that keep water, waste, and streets clean enough to protect health'),
       ('political machine', 'an organization that controls a city or state government through favors, jobs, and votes')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. A tenement is a crowded, often unsafe multi-family apartment building in a city: note that the definition names the building, not the family, which is Riis's whole argument in one line. Urbanization is the growth of cities as people move to them for work and services, the process sections A through D described. Sanitation is public measures that keep water, waste, and streets clean enough to protect health; the word public does the work, because sanitation names what a city does, not what a household does. And a political machine is an organization that controls a city or state government through favors, jobs, and votes, the three currencies section E traced in both directions.")

# ------------------------------------------------------ 24 · VOCAB B
vocab('Words for the machine and the answer',
      [('boss', 'the leader of a political machine who directs its workers and rewards'),
       ('graft', 'the illegal use of political power for personal profit, such as kickbacks and bribes'),
       ('settlement house', 'a community center in a poor neighborhood offering classes, childcare, and help to residents')],
      "Three more terms, again matching the guided notes exactly. The boss is the leader of a political machine who directs its workers and rewards: William M. Tweed is the lesson's example, and the definition's second half, the rewards, is what held the machine together between elections. Graft is the illegal use of political power for personal profit, such as kickbacks and bribes. Keep the definition narrow in students' minds: graft is not corruption in the abstract and not every favor the machine did; it is the specific crime of converting public decisions into private money, the padded contract being the lesson's case. A settlement house is a community center in a poor neighborhood offering classes, childcare, and help to residents. Hull House is the example, and the definition's plainness is the point: the reform that answered both the tenement and the machine began as a building on a poor street, with its workers living inside it.")

# ------------------------------------------------------ 25 · TODAY'S WORK
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'City Systems', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Return to the lesson question: how did rapid urban growth change daily life, health, and city government? Work the four systems, then judge the machine.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'City Systems stations: housing, water, transit, and the machine'),
        ('Notebook', 'The City at a Glance: one chart for all four systems'),
        ('Quick check', 'One Street, Whole City: read Mulberry Street closely'),
        ('Writing', "The Machine, Judged by Its Street: help weighed against harm")]
yy = 4.35
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=19, color=CREAM)
    yy += 0.58
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: define urbanization and sanitation, explain machine loyalty, and choose, tenement or streetcar.',
     size=16, color=POWDER)
notes(s, "Close by handing the lesson to its work, in the order students will meet it. The activity, City Systems, runs four stations, one per system: the Riis lodgers photograph for housing, the water and waste summary and Waring's reorganization for sanitation, the Mulberry Street photograph for transit, and the Nast cartoon with the Tammany record for the machine. At each station students name the problem, assign it to a cause, and record the evidence, then decide who was best placed to fix each system in 1890. The notebook page, The City at a Glance, collects the same four systems into the chart they will reuse on review day, so require it complete before the quick check. The quick check, One Street, Whole City, returns to Mulberry Street and tests transfer. The writing task, The Machine, Judged by Its Street, asks for the two sided judgment section E built toward, using at least two evidence cards and answering the strongest point on the other side.")

dc.save(OUT)
