#!/usr/bin/env python3
"""Lesson 4 deck, "The New Immigration," built to the approved pilot system:
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
OUT = os.path.join(HERE, '..', 'lesson-04-slides.pptx')

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
text(s, 0.9, 5.32, 11.5, 0.4, 'GILDED AGE · LESSON 4', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The New Immigration', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'More than 20 million arrivals, and a country deciding who could stay', size=17, color=POWDER)
notes(s, "The photograph is Mulberry Street in New York City, about 1900, the center of Little Italy, crowded with market stalls and shoppers. It is a good place to start, because it shows the end of a journey that this lesson will trace from the beginning. Between 1880 and 1920 more than 20 million people arrived in the United States, and the arrivals changed the country as surely as the factories and railroads of the earlier lessons did. Frame the day around two movements at once. People moved, in numbers and from places that were new in American experience. And the United States, through inspectors at two island stations and through laws passed in Congress, decided which of those people belonged. Students should leave able to explain both movements, and to say where the real decision was made.")

# ------------------------------------------------- 2 ESSENTIAL QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('Who were the new immigrants, and how did the United States decide who belonged?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did industrial growth transform American life, and who gained, who paid, and who resisted?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question has two halves, and students need both. Who were the new immigrants asks about people: where they came from, why they left, and where they settled. How did the United States decide who belonged asks about power: the chalk mark on a coat at Ellis Island, the months of questioning at Angel Island, and the laws that drew the lines before any ship arrived. The unit question runs underneath. Industrial growth created the demand for labor that pulled migrants across two oceans, so immigration is not a side story to industrialization. It is one of its largest human consequences. Keep the lesson question visible, and return to its exact wording at the end of class. The exit ticket asks students to choose between the inspection station and Congress as the place where belonging was decided, and to defend the choice with facts.")

# --------------------------------------------------- 3 THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.3, 11.5, 1.0, 'Arrival, inspection, and the closing door', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.42)
rows = [('A', 'A larger and different migration', 'more than 20 million, and a shift to southern and eastern Europe'),
        ('B', 'Push and pull', 'hardship at home, work and wages across the ocean'),
        ('C', 'Ellis Island', 'steerage, the stairs, the chalk, and the manifest'),
        ('D', 'Angel Island and exclusion', 'detention, questioning, and the law of 1882'),
        ('E', 'Neighborhoods and work', 'Little Italy and Chinatown, hard jobs, two speeds of change'),
        ('F', 'Nativism and restriction', 'from one named group in 1882 to quotas in 1924')]
yy = 2.72
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.7, n, size=24, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.03, 3.6, 0.7, t, size=20, color=CREAM, bold=True)
    text(s, 5.35, yy + 0.08, 7.1, 0.7, d, size=17, color=POWDER)
    yy += 0.78
notes(s, "This is the map of the lesson, and it follows the guided notes section by section. Section A sets the scale and the change in origins. Section B explains the movement itself, the forces that pushed people out and pulled them in. Sections C and D are the heart of the lesson, a deliberate contrast. At Ellis Island most Europeans were admitted within hours. At Angel Island many Asian arrivals were detained for weeks and months. Section E follows the admitted into neighborhoods and workplaces, and section F follows the opposition, as nativism turned into law step by step between 1882 and 1924. Tell students to keep the two stations separate in their notes all hour. The lesson's central comparison, and the exit ticket, depend on that distinction never blurring into one general immigrant story.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_photo('ellis-group-port.jpg', 'Section A', 'A Larger and Different Migration',
              ['More people, and from new places'],
              "The photograph shows a group of immigrants outside a building on Ellis Island in the early twentieth century, a federal government photograph now held by the National Archives. Use it to slow students down before the numbers begin. Every person in a frame like this one had a village, a reason for leaving, and a destination, and the lesson will deal in millions. Section A makes one claim with two parts. The migration after 1880 was larger than what came before it, and it was different in origin. Earlier arrivals had come mostly from northern and western Europe. The new arrivals came mostly from southern and eastern Europe, with smaller numbers crossing the Pacific and the southern border. That change in origin, more than the numbers alone, is what later sections argue about, because the argument over who belonged was largely an argument about where a person was born.",
              title_size=40)

# ------------------------------------------------------ 5 ORIGINS SHIFT
content_text('Where they came from, before and after',
             ['Before 1880: Britain, Ireland, Germany, Scandinavia',
              'After 1880: Italy, Poland, Greece, Russia, eastern Europe',
              'Smaller numbers from Japan, China, Korea, India, Mexico',
              'Historians call the later arrivals the new immigrants',
              'By 1910, about one American in seven was foreign born'],
             "Work the contrast plainly, because section A of the guided notes tests it in three blanks. Before 1880, most immigrants came from northern and western Europe: Britain, Ireland, Germany, and Scandinavia. After 1880, the largest groups came from southern and eastern Europe, including Italians, Poles, Slovaks, Greeks, and Russian and eastern European Jews. Smaller numbers came from Japan, China, Korea, India, and Mexico, a point students often miss when they picture immigration as only an Atlantic story. The reading opens with the two paired terms students will meet again on the vocabulary slides. An immigrant is a person who comes to live permanently in a new country, and an emigrant is a person who leaves a country to live elsewhere. The same person is both, seen from opposite shores. By 1910 about one American in seven was foreign born, which means the change was visible on any city street in the industrial North.",
             kick='A · A larger and different migration', size=24)

# ------------------------------------------------------ 6 STAT
stat('20 MILLION', 'immigrants arrived between 1880 and 1920',
     'By 1910 about one American in seven was foreign born. The change was in the numbers, and in where people came from.',
     "Dwell on the number, because it disciplines everything else in the lesson. More than 20 million arrivals in forty years is an average of half a million people a year, arriving by ship, most of them through a small number of ports, and most of them settling in the industrial cities of the Northeast and Midwest. Cities, schools, workplaces, and politics all had to absorb that flow while it was happening, not in retrospect. Pair the big number with the smaller one in the subheading. One American in seven foreign born by 1910 means that immigration was not something happening at the edge of American life. In the mill towns and city neighborhoods where most arrivals settled, the share was far higher than one in seven. When later sections turn to conflict over wages, language, and religion, students should remember that the conflict ran at this scale, in daily life, block by block.",
     kick='A · A larger and different migration')

# ------------------------------------------------- 7 SECTION B DIVIDER
divider_text('Section B', 'Push and Pull',
             'Every departure had two sides: what drove people out, and what drew them in.',
             "This section has no divider photograph, and the absence is worth a quiet note to yourself rather than an apology to the class. The lesson's photographs show arrival and settlement, the American end of the journey. The villages people left, in Sicily, in Poland, in Guangdong, sit outside the lesson's image set, which is itself a small lesson in how the surviving record favors the receiving country. The framework here is simple and students will use it twice, in the guided notes and in the exit ticket. Push factors drove people out of a home country. Pull factors drew people toward a specific destination. Neither side explains a migration alone. A family needed a reason to leave and a reason to choose the United States, plus a route, a ticket, and usually a person waiting at the other end. The next two slides take the sides in order.")

# ------------------------------------------------------ 8 PUSH FACTORS
content_text('Push: what drove people out',
             ['Farmland divided into plots too small to feed a family',
              'Years of required military service for young men',
              'Landlords took much of what a harvest earned',
              'Pogroms drove Russian Jews from their homes',
              'Poverty, flooding, and disorder in Guangdong, China'],
             "Take the push factors one at a time, and keep them concrete. In southern Italy and eastern Europe, farmland had been divided by inheritance into plots too small to feed a family, so departure was often arithmetic before it was adventure. Young men faced years of required military service. Landlords took much of what a harvest earned. For Russian Jews the push was violent. Pogroms were organized attacks on Jewish communities that the government allowed or encouraged, and families fled them for safety, not only for wages. Chinese migrants left Guangdong province, where poverty, flooding, and disorder followed decades of war and rebellion. Stress the variety inside one word. Push can mean hunger, conscription, rent, persecution, or flood, and different families in the same village could be pushed by different items on this list at the same time.",
             kick='B · Push and pull')

# ------------------------------------------------------ 9 PULL FACTORS
content_text('Pull: what drew people in',
             ['Factories, mines, mills, and railroads needed labor',
              'American wages several times home pay for the same work',
              'Steamship companies sold cheap tickets and advertised abroad',
              'Letters, money, and prepaid tickets pulled kin along',
              'Many planned to return, and a substantial share did'],
             "Pull factors worked as a chain, and students should be able to trace it. Industrial employers needed labor for factories, mines, mills, and railroad crews, the same industrial growth from the unit question. American wages, though low by American standards, could be several times what the same work paid at home, and that difference paid for the ticket and then for the tickets of relatives. Steamship companies sold cheap tickets and advertised abroad, because migrants were a business. Letters and money sent home by earlier migrants, along with prepaid tickets, pulled relatives and neighbors along the same routes, which is why whole villages sometimes reappear in a single American neighborhood. End with the complication the reading insists on. Many men planned to work a few years and return home, and a substantial share did go back. Migration was a strategy, not always a farewell.",
             kick='B · Push and pull', size=24)

# ------------------------------------------------- 10 SECTION C DIVIDER
divider_photo('ellis-waiting-port.jpg', 'Section C', 'Ellis Island',
              ['Hours for most, and a ferry to a new life'],
              "The photograph shows immigrants with bundles and suitcases waiting to be transferred at Ellis Island on October 30, 1912, photographed by Underwood and Underwood and held by the Library of Congress. It shows the station's purpose exactly: a crowd in transit, waiting to move, not a crowd being housed. Ellis Island was the federal immigration station in New York Harbor that processed most European arrivals after 1892, and between 1892 and 1954 about 12 million people passed through it. Hold both facts for the contrast ahead. For most of those 12 million, the island was an afternoon, not an ordeal: a medical look, a set of questions, and a ferry ride. The small share who were excluded, about 2 percent, experienced the same rooms very differently. Section C takes the crossing first, then the inspection, step by step, in the order an arrival lived it.",
              title_size=54)

# ------------------------------------------------------ 11 STEERAGE
content_text('The crossing: steerage',
             ['Most Europeans crossed in steerage, below deck',
              'The cheapest space: crowded dormitories, one to two weeks',
              'Cabin passengers were inspected briefly on board',
              'Steerage passengers were ferried to Ellis Island'],
             "Start with the class system built into the ship, because it explains who met the island and who did not. Most Europeans crossed the Atlantic in steerage, the cheapest space on the ship, in crowded dormitories below deck. The voyage lasted one to two weeks. Cabin passengers, who had paid more for the crossing, were inspected briefly on board and landed directly. Steerage passengers were ferried to Ellis Island for the full inspection. The reading makes the point without editorializing, and students should catch it anyway. The depth of your inspection depended in part on the price of your ticket, because officials assumed that a cabin passenger was unlikely to become a public charge. That assumption, money as evidence of admissibility, will return at the manifest check on the next slide, and again at Angel Island, where no ticket price could outweigh a law aimed at a person's birthplace.",
             kick='C · Ellis Island')

# ------------------------------------------------------ 12 INSPECTION
content_text('Inspection at Ellis Island',
             ['Doctors watched the climb and chalk marked the doubtful',
              'Inspectors checked answers against the ship manifest',
              'For most, the whole process took a few hours',
              'About 2 percent were excluded and sent back',
              'Trachoma and likely public charge were common grounds'],
             "Walk the inspection in order, because the guided notes test each step. Doctors watched arrivals climb the stairs to the registry room and marked the coats of anyone who limped, breathed hard, or looked ill with a chalk letter for a closer examination. The stairs were the first test, and it took seconds. Inspectors then asked each arrival a standard set of questions and checked the answers against the ship's passenger list, called a manifest, which had been filled out at the port of departure. A mismatch raised suspicion. A match moved the line along. For most Ellis Island arrivals the whole process took a few hours, and about 2 percent of arrivals were excluded and sent back, most often for trachoma, a contagious eye disease, for other medical conditions, or because an inspector judged they were likely to become public charges. Behind that small percent stood thousands of individual reversals at the last step of a long journey.",
             kick='C · Ellis Island', size=24)

# ------------------------------------------------- 13 SECTION D DIVIDER
divider_photo('angel-arriving-port.jpg', 'Section D', 'Angel Island and Exclusion',
              ['The same ocean, a different welcome'],
              "The photograph shows immigrants arriving at the immigration station on Angel Island, a federal government photograph held by the National Archives. A caution about the image itself: the surviving source file is small, so this portrait crop reads softer than the other photographs in the deck, but the scene is real and period. Angel Island operated from 1910 to 1940 in San Francisco Bay, and its work was shaped by law in a way Ellis Island's was not. Where the New York station mostly processed arrivals for admission, the San Francisco station often detained them, above all Chinese arrivals, while officials decided whether the law allowed them in at all. Set the contrast in one sentence before moving on. Ellis Island asked, are you who the manifest says you are, and are you healthy. Angel Island asked, can you prove the law lets you enter.",
              title_size=40)

# ------------------------------------------------------ 14 ANGEL ISLAND
content_photo('angel-interview-port.jpg', 'Detention and questioning',
              ['The station in San Francisco Bay, 1910 to 1940',
               'Arrivals held in barracks for weeks, often months',
               'Questioning compared applicant and witness answers',
               'Each arrival had to prove a legal right to enter'],
              "The photograph shows officials examining an applicant at Angel Island. The Angel Island Immigration Station Foundation dates the well known interview photograph to 1923, and it is used here for exactly that scene, an applicant seated before officials. It does not show a named case or a specific interrogation, and students should not be told otherwise. The routine it illustrates was slow by design. A Chinese arrival claiming an exempt status, such as merchant or son of a citizen, had to prove it. Officials held arrivals in barracks for weeks and often months while they questioned the applicant and witnesses in detail, comparing answers about family and village for any mismatch. One inconsistent detail about a house, a road, or a relative could sink a claim built over months. Compare that directly with the few hours on the previous section's slide, and let students sit with the distance between the two stations.",
              kick='D · Angel Island and exclusion')

# ------------------------------------------------------ 15 EXCLUSION ACT
content_text('Exclusion, paper sons, and poems',
             ['The 1882 law suspended Chinese labor immigration',
              'Exempt claims: merchant, or son of a citizen',
              'After the 1906 fire, paper sons claimed citizen fathers',
              'Detainees brushed and carved poems on barrack walls',
              'Japanese, Korean, and South Asian arrivals detained too'],
             "Give students the law first, in its full guided notes form, because the vocabulary slides return to it. The Chinese Exclusion Act was the 1882 federal law that suspended Chinese labor immigration and barred Chinese residents from naturalized citizenship, and it was the first federal law to bar a named national group. Exclusion created the paperwork it then policed. Because the 1906 San Francisco earthquake and fire destroyed the city's birth and citizenship records, some Chinese migrants entered as paper sons, claiming a citizen father whose records could not be checked. Inside the barracks, detainees brushed and carved poems onto the walls recording anger, boredom, and uncertainty. Those poems are evidence of a kind no manifest can supply, and the activity returns to them. Japanese, Korean, and South Asian arrivals also passed through Angel Island and were often detained, though exclusion fell hardest on the Chinese.",
             kick='D · Angel Island and exclusion', size=24)

# ------------------------------------------------- 16 SECTION E DIVIDER
divider_photo('mulberry-port.jpg', 'Section E', 'Neighborhoods, Work, and Assimilation',
              ['Where the admitted landed, and what changed'],
              "The photograph returns to Mulberry Street, about 1900, this time in a portrait crop of the same Detroit Publishing photochrom that opened the lesson. It is the right image for this section, because admission was not the end of the story the lesson is telling. Admitted immigrants settled where the work was, and they built neighborhoods dense enough to photograph like this one. Section E covers three connected subjects. The neighborhoods themselves, named places such as Little Italy and Chinatown. The work that filled them, hard and often dangerous. And the slower, uneven change inside families, as children moved toward American customs faster than their parents did. Warn students against a tidy ending here. Settlement was not a reward ceremony after inspection. It was the beginning of a second negotiation, this one with employers, landlords, schools, and neighbors, and it ran for a generation.",
              title_size=36)

# ------------------------------------------------------ 17 NEIGHBORHOODS
content_text('Neighborhoods and mutual aid',
             ['Most settled in the Northeast and Midwest cities',
              'Little Italy, Chinatown, and blocks built by village ties',
              'Help from relatives, mutual aid societies, parishes, synagogues',
              'Foreign language newspapers explained schools and courts'],
             "Settlement followed work and kin, in that order for most families. Admitted immigrants settled where the work was, and most stayed in the industrial cities of the Northeast and Midwest, in neighborhoods that took names such as Little Italy and Chinatown. New arrivals found rooms and jobs through relatives and through mutual aid societies, parishes, and synagogues. Pause on those institutions, because they are the lesson's answer to a fair student question: how did a person with twelve dollars and no English start. The answer is that almost nobody started alone. A brother, a cousin, or a society from the home village supplied the first room, the first job lead, and the first explanations. Foreign language newspapers explained American schools, courts, and elections. The neighborhood was both a shelter from the new country and a school for it, and it was both at the same time, which is why it worked.",
             kick='E · Neighborhoods, work, and assimilation')

# ------------------------------------------------------ 18 WORK AND ASSIMILATION
content_text('Work, school, and two speeds',
             ['Garment shops, steel mills, coal mines, and docks',
              'The work was hard and often dangerous',
              'Children learned English fast in public schools',
              'Families kept home languages, foods, and holidays'],
             "Work first, because work was the reason for the address. The jobs waiting in the industrial cities were in garment shops, steel mills, coal mines, and docks, and the work was hard and often dangerous, a direct link back to the factory and mine conditions from the start of this unit. Then the family change, in the reading's exact terms. Children entered public schools and learned English quickly, which could strain families when children adopted American customs faster than their parents. The key term here is assimilation: the process by which a person or group adopts the customs and language of another culture. The reading is careful about it, and students should be too. Assimilation rarely ran at one speed, and most families kept home languages, foods, and holidays while adding American ones. It was addition and loss at once, at different rates inside the same household.",
             kick='E · Neighborhoods, work, and assimilation')

# ------------------------------------------------- 19 SECTION F DIVIDER
divider_photo('barred-port.jpg', 'Section F', 'Nativism and Restriction',
              ['Opinion first, then law, step by step'],
              "The image is a cartoon from Frank Leslie's Illustrated Newspaper of April 1, 1882, titled The Only One Barred Out, weeks before Congress passed the Chinese Exclusion Act. A Chinese man sits outside a gate labeled as the gate of liberty, while a sign welcomes groups the cartoon's readers were meant to fear and bars only him. His baggage is labeled with virtues: industry, order, peace, and sobriety. The cartoon criticizes exclusion, and the activity examines both its argument and its limits. It opens this section because it dates the argument precisely. Opposition to the new immigration was not a late reaction to the quotas of the 1920s. It was present, organized, and already winning laws in 1882, before the largest arrivals had even landed. Section F names the attitude, gives its arguments fairly, and then traces the laws that followed it.",
              title_size=44)

# ------------------------------------------------------ 20 NATIVISM
content_text('Nativism: the argument against',
             ['The charge: too different in religion, language, custom',
              'The claim: new arrivals held wages down',
              'Unions backed restriction when employers broke strikes',
              'Law followed opinion, step by step'],
             "Define the attitude in the guided notes words first. Nativism is a policy or attitude favoring native-born residents over immigrants. Then give its arguments as the reading gives them, without softening or inflating them. Many native-born Americans answered the new immigration with nativism. Critics charged that the new arrivals were too different in religion, language, and custom to become Americans, and that they held wages down. The wage argument had an organized base. Many unions supported restriction because employers used immigrant workers to break strikes and undercut pay, which put labor organizations in the painful position of opposing fellow workers in the name of protecting wages. Students do not have to accept an argument to explain it, and the guided notes only ask them to explain it. The section's last move is the important one. Law followed opinion step by step, and the next slide is that staircase.",
             kick='F · Nativism and restriction')

# ------------------------------------------------------ 21 CLOSING DOOR
content_text('The closing door, 1882 to 1924',
             ['1882: Chinese labor immigration suspended',
              '1885: contract laborers recruited abroad barred',
              '1917: a literacy test, and most of Asia barred',
              '1921 and 1924: quotas cut immigration sharply',
              'Smallest quotas went to southern and eastern Europeans'],
             "Trace the staircase slowly, because section F of the guided notes asks students to list these steps in order, and reading question five asks them to narrate the same widening. In 1882 the Chinese Exclusion Act suspended Chinese labor immigration and barred Chinese residents from naturalized citizenship, one named group. An 1885 law barred contract laborers recruited abroad. In 1917 Congress required adult immigrants to pass a literacy test and barred most immigration from Asia, a continent rather than a country. Quota laws in 1921 and 1924 cut immigration sharply and gave the smallest quotas to southern and eastern Europeans, the very groups whose arrival opened this lesson. By the 1920s, who belonged was answered more and more by law, and the answer depended heavily on where an arrival was born. The circle that began with one group in 1882 had widened to rank nearly every birthplace on earth.",
             kick='F · Nativism and restriction', size=24)

# ------------------------------------------------------ 22 VOCAB A
vocab('Words for the journey',
      [('immigrant', 'a person who comes to live permanently in a new country'),
       ('emigrant', 'a person who leaves a country to live elsewhere'),
       ('nativism', 'a policy or attitude favoring native-born residents over immigrants')],
      "These definitions match the guided notes word for word, and students should copy them exactly. Immigrant: a person who comes to live permanently in a new country. Emigrant: a person who leaves a country to live elsewhere. The pair describes one person from two directions, and the small spelling difference carries the whole distinction, in for immigrant, out for emigrant. Students mix them under test pressure, so give them the shore test: name the shore you are standing on, and the word follows. Nativism: a policy or attitude favoring native-born residents over immigrants. Note that the definition covers both a policy and an attitude, because section F showed the two feeding each other. The attitude supplied the voters, the policy supplied the laws, and the laws then taught the next generation what the attitude claimed was natural.")

# ------------------------------------------------------ 23 VOCAB B
vocab('Words for the two gates',
      [('Ellis Island', 'the federal immigration station in New York Harbor that processed most European arrivals after 1892'),
       ('Angel Island', 'the immigration station in San Francisco Bay that processed and often detained many Asian arrivals')],
      "Two more definitions, again matching the guided notes exactly, and these two carry the lesson's central contrast inside their wording. Ellis Island: the federal immigration station in New York Harbor that processed most European arrivals after 1892. The verb in the definition is processed, which is the right word for a station built to move people through in hours. Angel Island: the immigration station in San Francisco Bay that processed and often detained many Asian arrivals. The added words, and often detained, do the analytical work. Same country, same federal system, same decades, and the definitions themselves have to diverge to stay accurate. When students write the exit ticket comparison, push them to borrow this language. A one sentence contrast built from these two definitions, plus the law named on the next slide, answers the first exit ticket question in full.")

# ------------------------------------------------------ 24 VOCAB C
vocab('Words for the law and the change',
      [('Chinese Exclusion Act', 'the 1882 federal law that suspended Chinese labor immigration and barred Chinese residents from naturalized citizenship'),
       ('assimilation', 'the process by which a person or group adopts the customs and language of another culture')],
      "The last two terms, in guided notes order, and together they name the two forces the lesson question asks about. Chinese Exclusion Act: the 1882 federal law that suspended Chinese labor immigration and barred Chinese residents from naturalized citizenship. Both halves of the definition matter. The act stopped a flow of workers, and it denied the people already here a path to citizenship, which is why its effects lasted long after any single ship was turned away. Assimilation: the process by which a person or group adopts the customs and language of another culture. Hold students to the reading's caution when they use the word. It rarely ran at one speed, it ran fastest in children and slowest in grandparents, and most families added American customs while keeping home languages, foods, and holidays, rather than trading one culture cleanly for another.")

# ------------------------------------------------------ 25 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Who decided who belonged?', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Return to the lesson question, then test it against the records. Keep inspection, admission, exclusion, and settlement separate.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'Arrival record jigsaw: five stations, one account of arrival'),
        ('Notebook', 'The gateway chart: three arrival routes, compared'),
        ('Quick check', 'Questioning at Angel Island'),
        ('Writing', 'Who decided who belonged? Station or Congress, defended')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.5, 0.6, d, size=19, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.8, 11.5, 0.5, 'Exit ticket: contrast the two islands, give a push and a pull, and defend where belonging was decided.',
     size=16, color=POWDER)
notes(s, "Close by returning to the lesson question: who were the new immigrants, and how did the United States decide who belonged. The honest answer the lesson has built is layered. Inspectors decided individual cases, with chalk, manifests, and months of questioning. Congress decided the categories those inspectors applied, and by 1924 the categories did most of the deciding before a ship arrived. Now hand the question to the work. In the arrival record jigsaw, groups rotate through five stations, a passenger manifest, an Ellis Island inspection account, an Angel Island poem in summary, the 1882 cartoon, and a settlement map, then build one account that keeps inspection, admission, exclusion, and settlement separate. The notebook page compares the three arrival routes in a chart. The quick check takes up questioning at Angel Island, and the writing task asks the exit ticket's third question at full length: station or Congress, defended with facts. Next lesson turns from the people arriving to the machines and the men who owned them.")

dc.save(OUT)
