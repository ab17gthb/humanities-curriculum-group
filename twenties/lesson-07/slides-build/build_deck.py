#!/usr/bin/env python3
"""Twenties Lesson 7 deck, "The Great Migration and the Harlem Renaissance,"
built to the approved Gilded Age / Progressive Era pilot system: image-led
slides, fragments only on screen, comprehensive speaker notes, full lesson
and vocabulary coverage. Fonts: Georgia titles, Lato body."""
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
OUT = os.path.join(HERE, '..', 'lesson-07-slides.pptx')

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
text(s, 0.9, 5.32, 11.5, 0.4, 'THE TWENTIES · LESSON 7', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Great Migration and the Harlem Renaissance', size=36, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'What Black Americans built in the cities of the North', size=17, color=POWDER)
notes(s, "This photograph shows a Universal Negro Improvement Association parade in Harlem on August 2, 1920, photographed by James Van Der Zee at 135th Street and Lenox Avenue. Read the sign on the car at the left aloud before anything else: The New Negro Has No Fear. That sign is this lesson in five words. Hundreds of thousands of Black southerners left the South during and after the war years, and in Chicago, Detroit, Cleveland, and New York they did not simply find new addresses. They built neighborhoods, newspapers, businesses, a literature, a music the whole country would hear, and the largest Black mass movement of the era. Students should leave today able to name what was built, city by city and form by form, and to explain how that building answered a country that had assigned Black Americans a lower place and tried to keep them in it.")

# ------------------------------------------------- 2 · LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('What did Black Americans build in the cities of the North, and how did that building answer the country that had excluded them?', {})]],
     size=40, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the prosperity of the 1920s change American life, and why was that prosperity weaker than it looked?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question has two halves, and students should hear both before we start. The first half is an inventory: what did Black Americans build in the cities of the North? Neighborhoods, churches, newspapers, businesses, poems, records, and organizations all count, and the lesson will name them with dates. The second half is the argument, and it is the half weak answers skip. How did that building answer the country that had excluded them? Every act of building in this lesson was also a statement, made to a nation that had taken the vote, segregated the schools, and enforced the arrangement with violence. The unit question underneath frames the whole Twenties unit: this migration is one place where the prosperity of the decade was real, wages several times farm pay, and also weaker than it looked, because the North answered new arrivals with covenants, bombs, and a whites only club door even in Harlem itself.")

# --------------------------------------------------- 3 · THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'They left, they built, they answered', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'Leaving the South', 'Jim Crow pushed, northern wages and the vote pulled'),
        ('B', 'The paper that spread the news', 'The Chicago Defender, carried south by Pullman porters'),
        ('C', 'New ground and the housing fight', 'The Black Belt, Black Bottom, Harlem, and the bombs'),
        ('D', 'Harlem and the Renaissance', 'Hughes, Hurston, Locke, Bessie Smith, Ellington'),
        ('E', 'The New Negro', 'Dignity claimed, not granted: vote, organize, speak'),
        ('F', 'Garvey and the UNIA', 'A mass movement, a shipping line, a collapse'),
        ('G', 'The fight in law, and Tulsa', 'The Dyer bill dies, and Greenwood burns')]
yy = 2.62
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.4, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.15, yy + 0.05, 6.3, 0.6, d, size=15, color=POWDER)
    yy += 0.63
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A covers the leaving itself, the pushes out of the South and the pulls toward the North. Section B follows the newspaper that spread the news and organized the leaving. Section C lands in the northern neighborhoods and in the housing fight that met the migrants there. Sections D and E take up what was built in Harlem, first the art and music of the Renaissance, then the claim behind it, the New Negro. Section F covers Marcus Garvey and the UNIA, the largest organization of the era. Section G closes with the NAACP's fight in law and with Tulsa, the warning that runs under the whole lesson. The final table in the guided notes, The Account at a Glance, asks students to rebuild this map as push, pull, built, and answer.")

# ------------------------------------------------- 4 · SECTION A DIVIDER
divider_text('Section A', 'Leaving the South',
             'Jim Crow pushed. Wages, the vote, and schools pulled.',
             "Set the movement in the guided notes definition before the details, because the definition is tested and because it is precise. The Great Migration is the movement of hundreds of thousands of Black southerners to northern cities for jobs and greater rights during and after the war years. Note the two motives the definition itself names: jobs and greater rights. Students who remember only the jobs miss half the lesson, and the half the lesson question is about. The movement began in the war years and ran through the 1920s, and it was not drift. People weighed a known South against a reported North, read letters and newspapers, saved for tickets, and often left in groups on set dates. Section A takes the two sides in order: first what the South did to drive people out, then what the North offered that made leaving rational, and between them the single pair of numbers, Chicago in 1910 and Chicago in 1930, that measures the scale of the decision.")

# ------------------------------------------------------ 5 · THE PUSH
content_text('What pushed people out',
             ['Jim Crow law: segregated schools, a lower place fixed by law',
              'The vote taken away: poll taxes, literacy tests, and fraud',
              'Landlords kept the sharecroppers\' account books, and often the crop',
              'Lynching enforced the order',
              'The boll weevil ruined cotton harvests',
              'The Mississippi flood of 1927: families in guarded levee camps'],
             "Walk the pushes in the reading's order, because each one closes a different door. Jim Crow law fixed Black southerners in a lower place: segregated schools, and a vote taken away by poll taxes, literacy tests, and fraud, so the ballot could not be used to change any of the rest. Sharecropping closed the economic door. Landlords kept the sharecroppers\' account books, and often the crop, so a family's year of work could end in debt by the landlord's arithmetic alone. Lynching enforced the order, which is the reading's exact and careful phrasing: violence was not random, it was the punishment standing behind the rules. Then nature added two blows. The boll weevil ruined cotton harvests across the South, and the great Mississippi flood of 1927 drove families into guarded levee camps, where Black men were held and put to work on the levees. A push, in the guided notes, needs a fact attached, and students should collect one fact per item on this slide.",
             kick='A · Leaving the South', size=24)

# ------------------------------------------------------ 6 · CHICAGO STAT
stat('234,000', 'Black residents of Chicago in 1930',
     'About 44,000 in 1910. One city, twenty years, more than five times as many Black residents.',
     "Dwell on these two numbers, both from the reading, because together they convert individual decisions into a historical event. Chicago counted about 44,000 Black residents in 1910 and about 234,000 in 1930. Do the arithmetic aloud: the 1930 figure is more than five times the 1910 figure, in a single city, in twenty years. Every one of those added residents is a person who weighed the pushes on the last slide against the pulls on the next one and chose to move, usually by train, usually with help from family, letters, or a newspaper. The guided notes ask for these two figures directly, blanks one and two, and the exit ticket's first question asks for one push and one pull, each with a fact. Tell students that a city growing this fast is not absorbing newcomers quietly. It is being remade by them, and sections C and D show what the newcomers made of Chicago, Detroit, Cleveland, and Harlem once they arrived.",
     kick='A · Leaving the South')

# ------------------------------------------------------ 7 · THE PULL
content_text('What pulled people north',
             ['War production, and the cutoff of European immigration',
              'Mills, stockyards, auto plants, and railroads hiring',
              'Wages several times farm pay',
              'A Black man could vote in most northern states',
              'Schools the law did not split by race'],
             "The North pulled as hard as the South pushed, and the reading is specific about why the jobs existed. Mills, stockyards, auto plants, and railroads were short of workers after war production and the cutoff of European immigration, the two labor shortages that opened factory gates to Black workers who had been shut out of them before. The wages were several times farm pay, a comparison students should hold against the sharecropper's account book from the last section: the same hands, a multiple of the money, and the money actually paid. The other two pulls are political, and they matter as much to this lesson. A Black man could vote in most northern states, the very right the South had taken away. His children attended schools the law did not split by race. Say the limit honestly, because section C will prove it: the law did not split the schools, but custom, covenants, and violence drew plenty of lines the law did not have to draw.",
             kick='A · Leaving the South')

# ------------------------------------------------- 8 · SECTION B DIVIDER
divider_text('Section B', 'The Paper That Spread the News',
             'One newspaper, carried south in Pullman porters\' bags.',
             "Migration on this scale needs information, and section B is about the machine that supplied it. A family in Mississippi considering Chicago needed to know that jobs were real, what the train cost, where to sleep the first night, and whether the letters home were telling the truth. The Chicago Defender supplied all of it, and it did so deliberately, as a campaign and not only as a newspaper. Keep the vocabulary definition in view through this section. The Chicago Defender is the Black newspaper founded in Chicago in 1905 by Robert S. Abbott, which urged Black southerners to move north and printed the news of lynching and discrimination that white papers ignored. Both halves of that definition do work in this section: the urging, which the next slide details, and the reporting, because a paper that printed the lynching news the white press ignored was itself evidence that the North allowed a Black press to speak.")

# ------------------------------------------------------ 9 · THE DEFENDER
content_text('The Defender spread the word',
             ['Founded in Chicago in 1905 by Robert S. Abbott',
              'Pullman porters carried the paper south',
              'Train schedules, job notices, and migrants\' letters in print',
              'May 15, 1917: the Great Northern Drive',
              'News of lynching and discrimination that white papers ignored'],
             "Give students the mechanics, because the mechanics are the history here. The Defender was founded in Chicago in 1905 by Robert S. Abbott, and Pullman porters carried the paper south in their bags, distributing it along the rail lines into towns where it was sometimes confiscated. Once there it passed hand to hand, reaching far more readers than its sales figures suggest. Inside, the paper printed practical help alongside news: train schedules, job notices, and letters from migrants already north, which let a reader check the promise against a named person from a known place. Then the Defender went further and campaigned. It set May 15, 1917, as a Great Northern Drive, urging readers to leave together on that date, turning private decisions into a collective act. And all through the paper ran the reporting the white press refused: lynching and discrimination, printed plainly, which both pushed readers out of the South and proved that a Black institution in the North could say in print what could not be said at home.",
             kick='B · The paper that spread the news', size=24)

# ------------------------------------------------------ 10 · CIRCULATION STAT
stat('125,000', 'Defender circulation in 1918, in Emmett J. Scott\'s count',
     'From about 50,000. A newspaper more than doubling in wartime was a migration organizing itself in print.',
     "This figure comes with its source attached, and students should notice that, because it is how careful history is written. Circulation rose, in Emmett J. Scott\'s count, from about 50,000 to about 125,000 in 1918. Scott studied the migration as it happened, in his 1920 book Negro Migration During the War, and the reading takes the number from him rather than from the Defender's own advertising, which had every reason to inflate it. Even the counted figure understates the paper's reach, because copies carried south were shared, read aloud, and passed hand to hand in barbershops, churches, and lodge halls. The guided notes ask for the 125,000 figure directly. The teaching point is the pairing of the two stat slides in this lesson. Chicago's Black population more than quintupled in twenty years, and the paper urging the move more than doubled in a single wartime year. Print and people moved together, and each one's growth helps explain the other's.",
     kick='B · The paper that spread the news')

# ------------------------------------------------- 11 · SECTION C DIVIDER
divider_text('Section C', 'New Ground and the Housing Fight',
             'Neighborhoods built, and lines drawn against them.',
             "Section C follows the migrants off the train, and it holds the lesson's two truths side by side on purpose. The first truth is construction. Migrants arrived in neighborhoods earlier Black residents had built, and filled them with churches, businesses, newspapers, and Urban League offices, the institutions of a self supporting city inside the city. The second truth is resistance. Housing was the sharpest fight, sharper even than the job fight, because a job could be shared across a factory floor while a house on the wrong street could not be shared at all. Rents, covenants, and bombs are the three weapons of that fight, and the next two slides take them in order: first the ground and what was built on it, then the fight over who was allowed to live on it. Warn students now that the Detroit story at the end of the section involves a killing and a murder trial, and that its ending, an acquittal and a kept house, is one of the few courtroom victories in this lesson.")

# ------------------------------------------------------ 12 · NEW GROUND
content_text('Neighborhoods earlier residents had built',
             ['Chicago: the Black Belt',
              'Detroit: Black Bottom and Paradise Valley',
              'Cleveland: the Central Avenue district',
              'New York: Harlem',
              'Each filled with churches, businesses, newspapers, Urban League offices'],
             "The guided notes test these four place names as a set, so say them slowly and have students write them as a set. In Chicago, the Black Belt. In Detroit, Black Bottom and Paradise Valley. In Cleveland, the Central Avenue district. In New York, Harlem. Then correct the picture students may be forming, that migrants arrived in empty space and built from nothing. The reading's sentence is that migrants arrived in neighborhoods earlier Black residents had built. Each generation of arrivals landed on ground prepared by the generation before, found a church, a newspaper, a lodge, and an Urban League office set up to help newcomers find work and housing, and then enlarged all of it. That is what the word built means in the lesson question. It does not mean only new construction. It means institutions dense enough that a stranger off a train could be housed, hired, informed, and buried by his own community. The scale of section A's numbers made that density possible, and the density made the culture of section D possible.",
             kick='C · New ground and the housing fight', size=24)

# ------------------------------------------------------ 13 · THE HOUSING FIGHT
content_text('The housing fight',
             ['High rents for subdivided, worn buildings',
              'Restrictive covenants: agreements barring sales or rentals to Black families',
              'Chicago: dozens of bombings of Black homes, 1917 to 1921',
              'Detroit, 1925: a crowd attacked Dr. Ossian Sweet\'s new house',
              'Sweet tried for murder, defended by Clarence Darrow, acquitted'],
             "Housing was the sharpest fight, and each fragment on this slide is a different weapon, so take them one at a time. First, price: Black tenants paid high rents for subdivided, worn buildings, because the districts open to them were limited and landlords knew the tenants had nowhere else to go. Second, law by private contract: restrictive covenants, agreements among white owners barring sales or rentals to Black families, which kept whole districts closed without any statute. Third, terror: Chicago saw dozens of bombings of Black families' homes between 1917 and 1921, aimed at families who crossed the line. Fourth, the mob, and the one case students must know whole. In Detroit in 1925 a crowd attacked Dr. Ossian Sweet\'s new house. Shots from the house killed a white man. Sweet, defended by Clarence Darrow, was tried for murder and acquitted. End on the reading's sentence, because it is the section in miniature: the house stayed his. Ground, once taken, was held.",
             kick='C · New ground and the housing fight', size=23)

# ------------------------------------------------- 14 · SECTION D DIVIDER
divider_photo('hughes-port.jpg', 'Section D', 'Harlem and the Renaissance',
              ['Poems, stories, records, and an orchestra', 'heard across the whole country'],
              "The portrait is Langston Hughes, and its date must be stated plainly: Carl Van Vechten photographed Hughes in 1936, a full decade after the years this section covers. The portrait is not a 1920s photograph, and students should never cite it as one. It is here because Hughes is the section's central writer and because this is the portrait the lesson documents use, with the 1936 date in their captions. What Hughes looked like in 1921, when he published The Negro Speaks of Rivers at nineteen, no photograph on this slide claims to show. Hold that standard for every image in this deck: the date of the picture and the date of the events are both facts, and they are different facts. Section D now takes up what the migrants built that reached furthest. The neighborhoods of section C housed tens of thousands. The writing and music of Harlem reached millions, carried by print, records, and radio into homes the migrants themselves would never enter.",
              title_size=40)

# ------------------------------------------------------ 15 · THE WRITERS
content_text('The writers of Harlem',
             ['Langston Hughes: The Negro Speaks of Rivers, 1921',
              'The Weary Blues, his first book, 1926',
              'Writing in the rhythms of jazz and the blues',
              'Zora Neale Hurston arrived in New York in 1925',
              'Stories drawn from Black southern speech and folklore',
              'Alain Locke, The New Negro, 1925: the anthology that named the movement'],
             "Three names carry this slide, and the guided notes test a date or a work for each, so attach them firmly. Langston Hughes published The Negro Speaks of Rivers in 1921 and his first book, The Weary Blues, in 1926, writing in the rhythms of jazz and the blues, so the music on the next slide is inside the poetry and not beside it. Zora Neale Hurston, who arrived in New York in 1925, wrote stories drawn from Black southern speech and folklore, treating the talk of Eatonville, Florida, as material for serious literature at a moment when most editors treated it as dialect comedy. Alain Locke's anthology The New Negro, published in 1925, gave the movement its name, and students will meet that phrase again as a vocabulary term and as the whole of section E. Now connect the slide to the lesson question. These writers took the speech, music, and memory the migrants carried north and presented them in books the whole country could buy. The culture of the excluded had become a national literature, on paper, with names on the covers.",
             kick='D · Harlem and the Renaissance', size=23)

# ------------------------------------------------------ 16 · THE MUSIC
content_photo('bessie-port.jpg', 'The music reached further',
              ['Jazz carried north by the migration: Chicago clubs',
               'King Oliver\'s band trained Louis Armstrong',
               'Bessie Smith: blues records sold by the hundreds of thousands',
               'Down Hearted Blues, a best seller of 1923',
               'Duke Ellington at the Cotton Club, 1927, broadcast nationwide',
               'The club admitted only white customers'],
              "The portrait is Bessie Smith, photographed by Carl Van Vechten on February 3, 1936, and that date must be stated plainly: it is a 1936 portrait, made after the decade of this lesson, not a photograph of Smith in her 1923 prime. What the portrait shows is the woman whose records did the work this slide describes. In the guided notes, jazz is music formed in Black communities of New Orleans from ragtime, blues, and brass band traditions, built on syncopation and improvisation, and the migration carried it north, filling Chicago clubs where King Oliver\'s band trained Louis Armstrong. The blues is a Black musical form built on a repeating pattern of chords, with verses that name hardship, work, and endurance in plain language, and Smith's blues records sold by the hundreds of thousands, with Down Hearted Blues a best seller of 1923. Close on the contradiction the reading refuses to soften. Duke Ellington's orchestra became the Cotton Club's house band in 1927 and was broadcast nationwide by radio, in a club that admitted only white customers. Black art, national audience, closed door.",
              kick='D · Harlem and the Renaissance')

# ------------------------------------------------- 17 · SECTION E DIVIDER
divider_text('Section E', 'The New Negro',
             'Dignity would not arrive as a favor. It had to be asserted.',
             "Section E is the shortest in the reading and the one the whole lesson turns on, because it names the idea that the building expressed. The Renaissance writers called what they claimed the New Negro. Use the vocabulary definition here, in full, because the guided notes test the term and because every clause of it is a refusal. A New Negro is a Black American of the 1920s who claimed dignity and equal rights, took pride in Black history and culture, and refused a second class place. Claimed, not requested. Took pride, in a history the country's textbooks had mocked or erased. Refused, the second class place that Jim Crow law, the covenant, and the bomb were all built to enforce. The photograph on the title slide belongs to this section as much as to any: a Harlem crowd in 1920 behind a car carrying the sign The New Negro Has No Fear. Section E asks what that claim looked like as conduct, what the New Negro would do, and what he would present to the country. The next slide answers from the reading, in its own order.")

# ------------------------------------------------------ 18 · THE CLAIM
content_text('What the New Negro claimed',
             ['Refused the place assigned to him',
              'Would vote, and organize',
              'Would speak in his own voice',
              'Took pride in African and Black American history',
              'Presented Black life as a subject worthy of serious art'],
             "The guided notes section E is written in the students' own words, so teach this slide as a sorting exercise against the reading's single dense paragraph. The New Negro refused the place assigned to him, which is the negative claim, the rejection. Then come the positive acts, and any two earn the guided notes blank: he would vote, using the northern ballot the South had taken away. He would organize, which is section F and the NAACP campaign in section G stated as a habit. He would speak in his own voice, which is Hughes's poems, Hurston's stories, and the Defender's columns all at once. And the one thing he would present to the country, the second guided notes blank, is Black life as a subject worthy of serious art. The reading's closing lines on this section are the ones to quote here: dignity would not arrive as a favor. It had to be asserted. Everything built in sections C, D, and F is that assertion in brick, print, music, and membership cards.",
             kick='E · The New Negro')

# ------------------------------------------------- 19 · SECTION F DIVIDER
divider_photo('garvey-parade-port.jpg', 'Section F', 'Garvey and the UNIA',
              ['The largest assertion of the era', 'marched through Harlem in uniform'],
              "The photograph shows Marcus Garvey in a plumed uniform and medal, seated in an open car during a UNIA parade in Harlem in 1922, and unlike the two Van Vechten portraits in this deck, it is a photograph of the decade itself, taken at the movement's height. Look at what Garvey understood about presentation. The uniform, the medal, the open car, the aide beside him: this is the visual language of heads of state, claimed by a Jamaican born organizer for a people the United States treated as a problem to be managed. At the UNIA's 1920 New York convention, delegates marched through Harlem in uniformed ranks, thousands of Black Americans moving through their own neighborhood in formation, under their own officers, behind their own flag. Whether students admire Garvey or judge him by the collapse that ends this section, they should first grasp the scale. No other Black organization of the era put that many people in the street, in uniform, on purpose. Section F takes the rise first, then the fall, and asks students to hold both.",
              title_size=40)

# ------------------------------------------------------ 20 · A MASS MOVEMENT
content_text('A mass movement, built on pride',
             ['Marcus Garvey, Jamaican born, built the UNIA',
              '1920 convention: delegates marched through Harlem in uniformed ranks',
              'The UNIA ran Harlem businesses',
              'Race pride as the organizing idea',
              'The largest Black mass movement of the era'],
             "State the vocabulary term in its full guided notes form, because this slide is where it belongs. The UNIA is the Universal Negro Improvement Association, Marcus Garvey\'s mass organization, founded to unite Black people worldwide and to build Black owned businesses and political power. Worldwide is the word that sets Garvey apart from every other figure in this lesson: his imagined constituency was not a neighborhood or a nation but a race, on every continent, and the UNIA enrolled members by the hundreds of thousands on that claim. The methods matched the claim. At its 1920 New York convention, delegates marched through Harlem in uniformed ranks. The UNIA ran Harlem businesses, putting the pride into shops and payrolls, not only speeches. The reading's verdict, which students should be able to repeat, is measured: its pride marked every Black movement after it. That sentence survives the collapse on the next slide, and the exit ticket rewards students who can hold the achievement and the failure in one answer, as the reading does.",
             kick='F · Garvey and the UNIA')

# ------------------------------------------------------ 21 · THE BLACK STAR LINE AND THE FALL
content_photo('garvey-desk-port.jpg', 'The Black Star Line, and the fall',
              ['A shipping line to carry Black trade across the Atlantic',
               'Financed by five dollar shares sold to Black buyers',
               'Old ships, in poor condition, losing money',
               '1923: Garvey convicted of mail fraud',
               '1925: Atlanta federal prison. 1927: commuted, deported to Jamaica'],
              "The photograph shows Garvey seated at a paper covered desk in 1924, gavel in hand, photographed on August 5 of that year by the Bain News Service: a working portrait from between the conviction and the prison term on this slide. The Black Star Line was the UNIA's boldest enterprise and its ruin. Financed by five dollar shares sold to Black buyers, a price set so that working people could own a piece of it, the line was meant to carry Black trade across the Atlantic. Instead it bought old ships in poor condition and lost money. In 1923 Garvey was convicted of mail fraud for selling stock in a ship the line did not yet own. He entered Atlanta federal prison in 1925. In 1927 President Coolidge commuted his sentence and he was deported to Jamaica. The guided notes test that sequence in order, blanks twenty four through twenty eight, so drill the dates as a chain: organization, line, fraud, prison, deportation. Then give the reading's balance in full: the UNIA never recovered its size, but its pride marked every Black movement after it.",
              kick='F · Garvey and the UNIA')

# ------------------------------------------------- 22 · SECTION G DIVIDER
divider_text('Section G', 'The Fight in Law, and the Warning of Tulsa',
             'The NAACP pressed Congress. A mob burned Greenwood.',
             "The last section sets two methods and two outcomes side by side, and it ends the lesson on a warning rather than a triumph, which is a deliberate choice students should notice. The NAACP fought the same exclusion Garvey fought, but by investigation, publicity, and law rather than by mass membership and enterprise. It documented each lynching and pressed Congress for a federal anti lynching law, the Dyer bill. That campaign is the first half of the section, and its outcome, a House victory undone in the Senate, is the honest measure of what law could and could not do in 1922. The second half is Tulsa, where a white mob destroyed a prosperous Black business district in two days and no one was punished. Teach the pairing directly: the decade that built Harlem also destroyed Greenwood, in the reading's closing sentence. Students who can hold both halves of that sentence, the building and the burning, have understood the lesson. Students who keep only the building have understood the cheerier half of it.")

# ------------------------------------------------------ 23 · THE DYER BILL
content_text('The NAACP and the Dyer bill',
             ['The NAACP documented each lynching',
              'A flag at headquarters: A Man Was Lynched Yesterday',
              'The Dyer bill: lynching a federal crime where states failed to act',
              'Passed the House, January 1922',
              'Southern senators filibustered it. Given up that December'],
             "The NAACP's method was evidence, patiently accumulated and publicly displayed, and students should see how different it is from Garvey's uniforms and parades. It documented each lynching, building the record case by case. It flew a flag from its headquarters reading A Man Was Lynched Yesterday, turning a Manhattan office window into a running count the press could not ignore. And it pressed Congress for the Dyer anti lynching bill, which would have made lynching a federal crime where states failed to act, answering the local sheriffs and juries who would not prosecute. The bill passed the House in January 1922. Southern senators then filibustered it, talking it to death, and it was given up that December. Every element of that sequence is tested: the exit ticket's second question asks what the Dyer bill proposed and what happened to it in 1922, word for word from this slide. Note the year against Tulsa on the next slide: the bill died the year after Greenwood burned, and the burning is part of why the bill existed.",
             kick='G · The fight in law, and the warning of Tulsa', size=23)

# ------------------------------------------------------ 24 · TULSA
content_text('Tulsa: the warning',
             ['Greenwood: a prosperous Black business district in Tulsa, Oklahoma',
              'May 31 and June 1, 1921: a white mob invaded it',
              'About thirty five blocks burned',
              'More than a thousand homes and businesses destroyed or looted',
              'The death toll never settled. No one was punished'],
             "Teach Tulsa last and teach it plainly, in the reading's own facts and in its order. Greenwood was a prosperous Black business district in Tulsa, Oklahoma, which means it was exactly the kind of building this whole lesson celebrates: Black owned shops, offices, and homes, accumulated over years. On May 31 and June 1, 1921, a white mob invaded it. About thirty five blocks burned. More than a thousand homes and businesses were destroyed or looted. The death toll was never settled; estimates run into the hundreds, and students should hear that uncertainty stated as a fact about the record, not filled in with a confident number. No one was punished. Then close the section with the reading's own final sentence, which the strongest exit tickets will echo: the decade that built Harlem also destroyed Greenwood. The building of this lesson was an answer to exclusion, and it was made while exclusion still had mobs, Senate filibusters, and impunity at its disposal. That is why the answer had to be an assertion, and not a request.",
             kick='G · The fight in law, and the warning of Tulsa', size=23)

# ------------------------------------------------------ 25 · THE ACCOUNT AT A GLANCE
s = slide(NAVY)
kicker(s, 'The account at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Push, pull, built, answer', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Push', 'What drove people out', 'Jim Crow, the landlord\'s ledger, lynching, flood'),
        ('Pull', 'What drew people north', 'Wages, the vote, schools, the Defender'),
        ('Built', 'What they made', 'Neighborhoods, a Renaissance, the UNIA, a campaign'),
        ('Answer', 'What the building said', 'Citizens, creators, organizers: not a lower place')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.0, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.05, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 7.55, yy + 0.05, 4.9, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, The Account at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The four rows are the lesson's argument in its simplest form. Push: Jim Crow law and disfranchisement, landlord controlled sharecropping, lynching, the boll weevil, and the 1927 flood drove people out of the South. Pull: industrial jobs at several times farm pay, the vote, schools not split by race in law, and the news and help carried by the Defender drew them north. Built: the Black Belt, Black Bottom and Paradise Valley, Central Avenue, and Harlem, with their churches, businesses, and newspapers, the Harlem Renaissance, and the organizations, the UNIA and the NAACP campaign. Answer: the building stated that Black Americans were citizens, creators, and organizers who would hold ground in housing, in art, and in law, rather than accept the place assigned. Grade the table generously on wording and strictly on the fourth row: an answer row that only lists achievements, without saying what they answered, has missed the lesson.")

# ------------------------------------------------------ 26 · VOCAB A
vocab('Words for the movement and the moment',
      [('Great Migration', 'the movement of hundreds of thousands of Black southerners to northern cities for jobs and greater rights during and after the war years'),
       ('New Negro', 'a Black American of the 1920s who claimed dignity and equal rights, took pride in Black history and culture, and refused a second class place'),
       ('Harlem Renaissance', 'the flowering of Black writing, music, and art in the 1920s, centered in Harlem in New York City'),
       ('jazz', 'music formed in Black communities of New Orleans from ragtime, blues, and brass band traditions, built on syncopation and improvisation')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. The Great Migration: the movement of hundreds of thousands of Black southerners to northern cities for jobs and greater rights during and after the war years. Jobs and greater rights are both in the definition, and both halves were taught. New Negro: a Black American of the 1920s who claimed dignity and equal rights, took pride in Black history and culture, and refused a second class place. Harlem Renaissance: the flowering of Black writing, music, and art in the 1920s, centered in Harlem in New York City. Flowering is the definition's own word for the sudden abundance of section D. Jazz: music formed in Black communities of New Orleans from ragtime, blues, and brass band traditions, built on syncopation and improvisation. Note the birthplace in the definition: jazz is a southern creation that the migration carried north, like the people who played it.")

# ------------------------------------------------------ 27 · VOCAB B
vocab('Words for the music, the movement, and the paper',
      [('blues', 'a Black musical form built on a repeating pattern of chords, with verses that name hardship, work, and endurance in plain language'),
       ('UNIA', 'the Universal Negro Improvement Association, Marcus Garvey\'s mass organization, founded to unite Black people worldwide and to build Black owned businesses and political power'),
       ('Chicago Defender', 'the Black newspaper founded in Chicago in 1905 by Robert S. Abbott, which urged Black southerners to move north and printed the news of lynching and discrimination that white papers ignored')],
      "Three more terms, again matching the guided notes exactly. Blues: a Black musical form built on a repeating pattern of chords, with verses that name hardship, work, and endurance in plain language. Plain language is the load bearing phrase: the blues said what the sharecropper's ledger and the lynching record contained, in verses anyone could memorize, and Bessie Smith's records carried those verses nationwide. UNIA: the Universal Negro Improvement Association, Marcus Garvey\'s mass organization, founded to unite Black people worldwide and to build Black owned businesses and political power. Students often keep only the parades from section F; the definition keeps the program, worldwide unity, Black owned business, and political power. Chicago Defender: the Black newspaper founded in Chicago in 1905 by Robert S. Abbott, which urged Black southerners to move north and printed the news of lynching and discrimination that white papers ignored. Urged and printed are the two verbs of section B, the campaign and the reporting, and an answer that names only one of them is half an answer.")

# ------------------------------------------------------ 28 · CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['What did Black Americans build in the cities of the North, and how did that building answer the country that had excluded them?'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'Migration Account Jigsaw: five stations, from Scott\'s migrants to the Garvey parade'),
        ('Notebook', 'Notebook page: the keeper chart, push, pull, built, answer'),
        ('Quick check', 'Garvey at His Desk: the 1924 photograph and what it claims'),
        ('Writing', 'What They Built: the lesson question as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: one push and one pull, the Dyer bill and its fate, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, Migration Account Jigsaw, runs five stations through the lesson's evidence, from Scott's account of the migrants to the 1922 Garvey parade photograph. Students who can work every station own the account, not just the vocabulary. The notebook page asks them to rebuild the account at a glance in the keeper chart. The quick check, Garvey at His Desk, studies the 1924 desk photograph and what its gavel, papers, and formal dress claim. The writing task, What They Built, turns the lesson question into an essay of about 300 words. The strongest essays join at least three kinds of building: the neighborhoods and their institutions, the Renaissance claim that Black life was a subject for serious art, and the organizing of the UNIA and the NAACP. The exit ticket has three parts: one push and one pull, each with a fact, the Dyer bill and its fate in 1922, and the lesson question in two or three sentences using at least two facts. Next lesson takes up the crash that ended the decade's prosperity.")

dc.save(OUT)
