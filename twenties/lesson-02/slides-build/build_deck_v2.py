#!/usr/bin/env python3
"""The Twenties Lesson 2 deck, "Mass Media and the Celebrity Age," built to the
approved system: image-led slides, fragments only on screen, comprehensive
speaker notes, full lesson and vocabulary coverage.
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
OUT = os.path.join(HERE, '..', 'lesson-02-slides.pptx')

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
text(s, 0.9, 5.32, 11.5, 0.4, 'THE TWENTIES · LESSON 2', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Mass Media and the Celebrity Age', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Radio, movies, and the popular press give the country one culture', size=17, color=POWDER)
notes(s, "The photograph shows Grauman's Chinese Theatre in Hollywood in 1927, the year it opened, and it is the right doorway into this lesson. A movie palace was not just a place to watch a film. It was a machine for gathering thousands of strangers into one room to watch the same picture at the same hour, and the same picture was playing that week in cities across the country. That sameness, repeated across radio, film, and print, is the subject of the lesson. Before the 1920s, Americans mostly lived inside local cultures: local papers, local teams, local heroes. By the end of the decade, a family in Ohio and a family in Georgia could hear the same voice, watch the same film, and follow the same ballplayer in the same week. Students should leave able to explain how that happened, medium by medium, and to name who the new shared culture left at its margins.")

# ------------------------------------------------- 2 · LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did radio, movies, and the popular press give Americans a shared national culture for the first time?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the prosperity of the 1920s change American life, and why was that prosperity weaker than it looked?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question is the narrower one on the slide, and the unit question runs beneath it as the frame for the whole Twenties unit. Hold students to the two key words in the lesson question: shared and first. Shared means the same program, the same film, and the same front page photograph reaching people in different regions at the same time, not similar experiences in separate places. First means this had not happened before at national scale: earlier media were local or slow, and a newspaper took days to cross the country. The reading builds the answer in layers. Radio supplied simultaneity, one voice in many cities at one moment. Movies supplied identical pictures and, after 1927, identical voices. The tabloids supplied identical images and famous faces every morning. The exit ticket requires two facts and one limit, so keep the limit in view from the start: the shared culture was paid for by advertisers and it placed Black Americans, immigrants, and women at its margins.")

# --------------------------------------------------- 3 · THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'One country, one evening at a time', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'A Voice in the Air', 'KDKA, Pittsburgh, November 2, 1920'),
        ('B', 'Networks and the Sponsored Hour', 'NBC in 1926, CBS in 1927, one program in dozens of cities'),
        ('C', 'The Movie Palace and the Talkies', 'Palaces, fifty million admissions a week, The Jazz Singer'),
        ('D', 'The Tabloid and the Photograph', 'The Daily News, the Daily Mirror, wire photographs'),
        ('E', 'Sports as National Theater', 'Dempsey in the ring, Ruth at the plate'),
        ('F', 'The Hero of 1927', 'Lindbergh flies alone from New York to Paris'),
        ('G', 'Fads, Advertising, and the Voices Left Out', 'Shared crazes, sponsor money, and the margins')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.05, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.62
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Sections A and B cover radio: first the single station, then the network that linked stations into one national audience. Section C covers film, from the movie palace to the talkie that gave pictures a voice. Section D covers print, where tabloids and wire photographs put the same images in many cities on the same morning. Sections E and F cover what the system did with people: it turned athletes into national theater and one pilot into a national hero. Section G closes with the costs and the limits, the fads the media manufactured, the advertisers who paid, and the Americans the shared culture left out. Tell students the final table in their guided notes, The System at a Glance, asks them to rebuild exactly this map.")

# ------------------------------------------------- 4 · SECTION A DIVIDER
divider_photo('radio-port.jpg', 'Section A', 'A Voice in the Air',
              ['One station in Pittsburgh.', 'Anyone with a receiver heard the same words.'],
              "The photograph dates to 1923 and shows listeners at a home receiver wearing headphones, with onlookers gathered around them. Say plainly what the image does and does not show. It does not show a family around a cabinet set with a speaker, because in 1923 most listening still happened through headphones on crystal receivers, one or two people at a time. That detail carries the lesson's argument. Radio began as a private, almost solitary experience, and it became a shared national one only as sets gained speakers and networks linked stations. Keep that growth in view through sections A and B. Section A itself covers only the beginning: the first commercial broadcast in 1920, the engineer and the company behind it, and the sets that carried the voice into American homes. The national scale belongs to section B.",
              title_size=40)

# ------------------------------------------------------ 5 · KDKA
content_text('The first commercial broadcast',
             ['On November 2, 1920, station KDKA in Pittsburgh made the first commercial broadcast.',
              'The broadcast carried the returns of the Harding and Cox presidential election.',
              'Frank Conrad, a Westinghouse engineer, built the station.',
              'Westinghouse sold radio sets, and the sets needed programs.'],
             "Give students the scene precisely, because the guided notes test the station, the date, and the company. On November 2, 1920, station KDKA in Pittsburgh sent out the first commercial broadcast in the United States: the returns of the presidential election between Warren G. Harding and James M. Cox. In the guided notes vocabulary, to broadcast is part of the term broadcast: to send a program by radio waves to many listeners at once from a single station. The station grew out of the experimental work of Frank Conrad, an engineer for Westinghouse. Westinghouse sold radio sets, and it needed programs on the air to make the sets worth buying. That commercial logic is the seed of the whole system. Broadcasting existed because a manufacturer needed an audience, and everything in this lesson, including the sponsored hour in section B, grows from that arrangement. Anyone with a receiver heard the same words at the same moment, and that simultaneity was new in human history.",
             kick='A · A voice in the air')

# ------------------------------------------------------ 6 · SETS CHANGE
content_text('From headphones to the whole room',
             ['Stations multiplied across the country.',
              'Manufacturers sold sets by the millions.',
              'The first sets were crystal receivers, used with headphones.',
              'Cabinet sets with speakers followed, and a whole room could hear.',
              'By the middle of the decade, hundreds of stations were on the air.'],
             "This slide follows the hardware, because the hardware decided who could share the experience. Manufacturers sold radio sets by the millions. The first sets most families met were crystal receivers used with headphones, which limited listening to one or two people wearing the phones. Cabinet sets with speakers changed the social fact: a whole room could hear the same program at once, and listening became a normal evening activity for a family rather than a hobby for an enthusiast. Stations multiplied just as quickly, and by the middle of the decade hundreds of stations were on the air. Two cautions for students. First, a single station still reached only its own city and countryside; the national audience required the networks of section B. Second, the reading gives growth in sets and stations, not a single clean count of radio households, so students should describe the growth in the reading's own terms: sets by the millions, stations by the hundreds.",
             kick='A · A voice in the air', size=25)

# ------------------------------------------------- 7 · SECTION B DIVIDER
divider_text('Section B', 'Networks and the Sponsored Hour',
             'A single station reached one city. A network reached the country.',
             "Pause on the distinction in the subtitle, because it is the analytical heart of the radio story and the first exit ticket question. A stronger single station would still have reached one area at one time. A network did something different: it linked separate stations by telephone wire so that one program played in dozens of cities at the same moment, under one company's schedule. That created a single simultaneous national audience, and a simultaneous audience was something a sponsor could buy in one purchase. Section B therefore has two halves that belong together. The first is the wiring: the National Broadcasting Company in 1926 and the Columbia Broadcasting System in 1927. The second is the money: advertisers paid for the programs, which made radio free to the listener and made the listener the product being sold. Students who grasp both halves can explain the rest of the lesson, because movies and tabloids ran on versions of the same bargain.")

# ------------------------------------------------------ 8 · NETWORKS
content_text('One program, dozens of cities',
             ['In 1926, the National Broadcasting Company, NBC, was formed.',
              'Stations were linked by telephone wire.',
              'In 1927, the Columbia Broadcasting System, CBS, followed.',
              'One program played in many cities at the same time.',
              'Families planned supper around a favorite program.'],
             "Define the network in the guided notes words, because the unit test draws on them. A radio network is a group of stations linked by wire that carry the same programs at the same time under one company. The National Broadcasting Company, formed in 1926, linked stations by telephone wire so one program could play in dozens of cities at once. The Columbia Broadcasting System followed in 1927. The consequence reached into daily routine. Network schedules taught the country to keep the same hours: families planned supper around a favorite program, and a program's time slot became a national appointment. Compare that with the world before radio, when entertainment was local and each town kept its own amusements on its own schedule. The network did not just distribute programs. It synchronized the country's evenings, region by region, until millions of people were laughing, listening, and reacting at the same moment to the same voices.",
             kick='B · Networks and the sponsored hour')

# ------------------------------------------------------ 9 · SPONSORED HOUR
content_text('The listener was the product',
             ['Advertisers paid for the programs.',
              'Radio was free to the listener.',
              'A sponsor could speak to millions in a single evening.',
              'Amos and Andy, from Chicago in 1928, drew listeners in every region.',
              'Its two Black characters were played by white actors using dialect.'],
             "Follow the money carefully, because students often assume listeners paid for radio the way they paid for newspapers. They did not. Advertisers paid for the programs, so radio was free to the listener, and what the network sold to the sponsor was the audience itself, gathered at a predictable hour in predictable numbers. A sponsor could speak to millions of listeners in a single evening, something no earlier medium could offer. Then take up the period's most popular program honestly. Amos and Andy, first broadcast from Chicago in 1928, drew listeners in every region, and it is a clean example of the shared culture forming. Its two Black characters, however, were played by white actors using dialect. The most popular Black voices on network radio were not Black voices at all. That fact belongs in this section, not only in section G, because it shows the limit being built into the system at the moment of its greatest success.",
             kick='B · Networks and the sponsored hour', size=24)

# ------------------------------------------------- 10 · SECTION C DIVIDER
divider_photo('jazz-port.jpg', 'Section C', 'The Movie Palace and the Talkies',
              ['Film was national before radio.', 'In the 1920s it became grand, and then it learned to speak.'],
              "The image is the original 1927 poster for The Jazz Singer, the Warner Bros. film at the center of this section, showing Al Jolson, its star. A poster is advertising, and students should read it as such: it promises a star, a story, and a sensation, and identical posters hung outside theaters across the country. Film had been national before radio, since the same reels could ship from town to town, but in the 1920s the movies became grander in scale and then changed in kind. Section C covers both changes in order. First the movie palace, the theater built to seat thousands and to make an ordinary evening feel like an occasion. Then the talkie, the film with recorded sound that standardized what audiences heard. By the end of the section students should be able to say what a Georgian and an Ohioan now had in common on a Saturday night: the same palace ritual, the same picture, and the same spoken lines.",
              title_size=36)

# ------------------------------------------------------ 11 · MOVIE PALACES
content_photo_s('chinese-port.jpg', 'The movie palace',
              ['Palaces seated thousands, with marble lobbies and uniformed ushers.',
               'The Roxy in New York opened in 1927.',
               "Grauman's Chinese Theatre in Hollywood opened in 1927.",
               'For a quarter, a mill worker and a bank president watched the same picture.'],
              "The photograph shows Grauman's Chinese Theatre in Hollywood in 1927, the year it opened, one of the two palaces the reading names. Studios built movie palaces that seated thousands, with marble lobbies and uniformed ushers, and the setting was part of the product: a working person entered a space grander than any room in daily life. The Roxy in New York and Grauman's Chinese Theatre in Hollywood both opened in 1927, the same year as The Jazz Singer, which makes 1927 the hinge year of this whole lesson. Stress the democratic surface of the experience. For a quarter, a mill worker and a bank president watched the same picture. Class did not vanish at the door, and section G will ask who decided what appeared on the screen, but the picture itself was identical for everyone in the room, and the same picture played that week in palaces across the country.",
              kick='C · The movie palace and the talkies')

# ------------------------------------------------------ 12 · ATTENDANCE STAT
stat('50 million', 'movie admissions a week in the middle of the decade',
     'A contemporary estimate from the reading. The palaces seated thousands at a time, and the same pictures played in every region.',
     "Dwell on the scale of this number, because students underestimate it until they compare it with the country's size. Contemporary estimates put weekly attendance at about fifty million admissions in the middle of the decade, in a nation of roughly one hundred fifteen million people. Admissions are not individual people, since enthusiasts went more than once a week, but the figure still means that moviegoing touched a large share of American households every single week. No earlier entertainment had reached that many people with the same content. A stage play reached one theater at a time and changed with each cast. A film reached thousands of theaters with identical images, and after 1927, identical voices. That is why the reading treats the movies as a national culture machine rather than a local amusement. When students write about the shared culture, this estimate is strong evidence: fifty million admissions a week is a habit, and a shared habit is most of what a shared culture is.",
     kick='C · The movie palace and the talkies')

# ------------------------------------------------------ 13 · TALKIES
content_text('The picture learns to speak',
             ['On October 6, 1927, Warner Bros. released The Jazz Singer.',
              'The mostly silent film included scenes of recorded dialogue and song by Al Jolson.',
              'Audiences crowded in to hear a picture speak.',
              'Within two years, the major studios had converted to sound.',
              'Silent stars with unsuitable voices lost their careers.'],
             "This slide carries the turning point of the film story, and the guided notes test the date and the film. On October 6, 1927, Warner Bros. released The Jazz Singer, a mostly silent film with several scenes of recorded dialogue and song by Al Jolson. In the guided notes definition, a talkie is a motion picture with recorded dialogue and sound, which replaced silent film after 1927. Audiences crowded in to hear a picture speak, and within two years the major studios had converted to sound production. The change standardized the national experience further: the same actor now said the same line in Georgia and in Ohio in the same week. It also acted as a filter on people. Silent stars whose voices recorded poorly, or whose acts depended on silence, lost their careers, while performers who could speak and sing gained work. Technology created the shared culture, and it also decided whose voices that culture would carry.",
             kick='C · The movie palace and the talkies', size=24)

# ------------------------------------------------- 14 · SECTION D DIVIDER
divider_text('Section D', 'The Tabloid and the Photograph',
             'Print changed with the rest: smaller pages, larger pictures, bolder headlines.',
             "Print is the oldest medium in this lesson, and students may assume it changed least. Section D corrects that. The newspaper of the 1920s was rebuilt around the photograph, and the photograph changed what news was. A story had to be tellable in a picture, and the faces that photographed well became the faces the country knew. The tabloid format led the change: a smaller page, large photographs, short stories, and bold headlines, with crime, scandal, and sport covered closely. Wire services then carried photographs across the country, so the same front page image greeted readers in many cities on the same morning. Note the limit built into the section. No verified public domain scan of a 1927 tabloid front page is reproduced in this lesson's materials; the activity presents a front page as a labeled summary instead. The evidence here is the format and the distribution system, and students should be able to explain both without needing to see one particular page.")

# ------------------------------------------------------ 15 · TABLOIDS
content_text('A smaller page, a larger picture',
             ['In 1919, the New York Daily News was founded.',
              'It was built around photographs, and it outsold the older papers.',
              'In 1924, the Daily Mirror followed.',
              'The tabloids printed large pictures, short stories, and bold headlines.',
              'They covered crime, scandal, and sport closely.'],
             "Give the tabloid its guided notes definition first, because students often use the word loosely. A tabloid is a newspaper printed in a smaller format that used large photographs and bold headlines to report crime, scandal, and celebrity news. The New York Daily News, founded in 1919, proved that a smaller page built around photographs could outsell the older, wordier papers. The Daily Mirror followed in 1924. These papers printed large pictures, short stories, and bold headlines, and they covered crime, scandal, and sport closely, because those subjects photographed well and sold on the street. The deeper point is selection. The tabloids manufactured fame by choosing which faces readers would see every day. A face on the front page became a famous face, and fame created more coverage, which created more fame. That loop is how a celebrity, in the vocabulary sense, gets made, and sections E and F show the loop running at full speed on athletes and on one pilot.",
             kick='D · The tabloid and the photograph', size=25)

# ------------------------------------------------------ 16 · WIRE PHOTOS
content_text('The same front page, the same morning',
             ['Wire services moved photographs across the country.',
              'The same image greeted readers in many cities on the same morning.',
              'Trials, scandals, and famous faces became national stories.',
              'The papers chose which faces the country would see daily.'],
             "This short slide carries the print version of the lesson's central claim, simultaneity, so slow down on the mechanism. Wire services moved photographs across the country by wire, which meant an editor in another city could print a picture taken the day before, and readers in many cities saw the same front page image on the same morning. Before wire photographs, a distant event arrived as words, and each reader pictured it privately. Now the country pictured it identically: the same defendant's face, the same wreck, the same ballplayer's swing. That identical picturing is a large part of what a shared national culture means. Connect the three media explicitly for students. Radio synchronized the country's ears, the talkies synchronized its eyes and ears together, and the wire photograph synchronized its morning conversation. The tabloids also chose the faces, and that choosing power is why the reading says the papers manufactured fame rather than merely reporting it.",
             kick='D · The tabloid and the photograph')

# ------------------------------------------------- 17 · SECTION E DIVIDER
divider_photo('dempsey-port.jpg', 'Section E', 'Sports as National Theater',
              ['Sport gave the new media its most reliable drama.'],
              "The photograph shows Jack Dempsey and Georges Carpentier in the ring on July 2, 1921, in Jersey City, the fight this section opens with. Look at what surrounds the two men: a stadium built for the occasion and a crowd of about eighty thousand people. Sport suited the new media perfectly. A fight or a ballgame had a scheduled hour, a clear contest, a result nobody could know in advance, and heroes whose faces and records the papers could print daily. Radio could carry the event as it happened, newsreels could show it within days, and newspapers could argue about it for a week. Section E follows the two largest examples. First Dempsey, whose 1921 title defense drew the first million dollar gate and a radio audience far beyond the stadium. Then Babe Ruth, whose daily home runs gave newspapers and newsreels a serial story that renewed itself every afternoon of the season.",
              title_size=38)

# ------------------------------------------------------ 18 · DEMPSEY
content_text('The fight of July 2, 1921',
             ['Jack Dempsey defended his heavyweight title against Georges Carpentier.',
              'About eighty thousand people filled the seats in Jersey City.',
              'The gate passed one million dollars.',
              'A radio account carried the fight far beyond the ring.',
              'Dempsey won by a knockout in the fourth round.'],
             "Walk through the fight as a media event, not only as a sporting result. On July 2, 1921, Jack Dempsey defended his heavyweight title against Georges Carpentier in Jersey City before about eighty thousand people. The gate passed one million dollars, the first million dollar gate in boxing, which tells students how large a live audience sport could already draw. The newer fact is the audience beyond the stadium. A radio account carried the fight far beyond the ring, so listeners who could never have bought a ticket followed the rounds as they happened. Dempsey won by a knockout in the fourth round. For the lesson's argument, the reach counts for more than the result: one contest, at one scheduled hour, held the attention of a stadium crowd and a radio audience at once. Sport taught the media system how to gather the country, and the system repaid sport by making its champions into national figures.",
             kick='E · Sports as national theater', size=25)

# ------------------------------------------------------ 19 · RUTH
content_photo_s('ruth-port.jpg', 'Ruth, the daily serial',
              ['Babe Ruth played for the New York Yankees.',
               'He hit home runs at a rate no player had approached.',
               'Newspapers, newsreels, and radio made his performance a national routine.',
               'On September 30, 1927, he hit his sixtieth home run of the season.',
               'The Yankees swept the Pittsburgh Pirates in the World Series.'],
              "The photograph shows Babe Ruth batting in Seattle on October 19, 1924, during an exhibition appearance. Date it plainly for students: it is a 1924 photograph, not an image of the 1927 season the text describes, and the lesson documents say the same. Ruth himself supplied the raw material. He hit home runs at a rate no player had approached, and he did it on a daily schedule, which made him ideal for the new media: newspapers, newsreels, and radio turned his daily performance into a national routine. On September 30, 1927, Ruth hit his sixtieth home run of the season, a record the whole country had counted toward for weeks, and the Yankees then swept the Pittsburgh Pirates in the World Series. In the guided notes vocabulary, Ruth is the model celebrity: a person widely known and followed because the media covered his work. Without the coverage system, he would have been famous in ballparks. With it, he was famous in towns he never visited.",
              kick='E · Sports as national theater')

# ------------------------------------------------- 20 · SECTION F DIVIDER
divider_photo('lindbergh-port.jpg', 'Section F', 'The Hero of 1927',
              ['He flew alone.', 'His fame was a joint product.'],
              "The photograph shows Charles Lindbergh with his airplane, the Spirit of St. Louis, in 1927, in a Harris and Ewing photograph held by the Library of Congress. Use the subtitle to set the section's argument before the facts. Lindbergh flew alone, and no account should take the feat away from him: thirty-three and a half hours in a single engine plane, without a copilot, navigating to another continent. But his fame, the speed and scale of it, was a joint product of his skill and of a media system that could build a hero in a weekend. Newspapers had covered the contest for the prize for weeks before he took off. Radio and newsreels carried his arrival in Paris to a public already prepared to celebrate him. Section F asks students to separate the two contributions, the deed and the amplification, because that separation is exactly what the reading's fourth question tests with Ruth and Lindbergh together.",
              title_size=40)

# ------------------------------------------------------ 21 · FLIGHT STAT
stat('33.5 hours', 'alone, from Roosevelt Field to Paris, May 1927',
     'The first nonstop flight between New York and Paris. It won the twenty-five thousand dollar Orteig Prize.',
     "Dwell on what this number measures and what it does not. Thirty-three and a half hours was the time Charles Lindbergh spent alone in the Spirit of St. Louis between Roosevelt Field on Long Island and Paris in May 1927, on the first nonstop flight between New York and Paris. He won the twenty-five thousand dollar Orteig Prize, offered for exactly that flight. The number proves endurance and navigation, and students should respect it on those terms. What the number cannot explain is the fame. Other pilots had flown far and flown bravely without becoming the most celebrated man in the country. Lindbergh's flight arrived inside a system that had been preparing his story for weeks: newspapers followed the prize contest, rivals, and weather, so the public already knew his name and his plane before he landed. Radio and newsreels then delivered the arrival everywhere at once. The flight was his. The weekend of celebration that followed belonged to the media system as much as to him.",
     kick='F · The hero of 1927')

# ------------------------------------------------------ 22 · HERO BUILT
content_text('A hero built in a weekend',
             ['Newspapers had followed the prize contest for weeks.',
              'Radio and newsreels carried his arrival in Paris.',
              'On June 13, New York gave him a ticker tape parade.',
              'He had flown alone, but his fame was a joint product.',
              'Skill supplied the deed, and the media supplied the scale.'],
             "Close the section by making the comparison the reading's answer key rewards. Ruth supplied a repeatable daily performance, renewed every afternoon. Lindbergh supplied a single feat, prepared in advance by weeks of newspaper coverage of the Orteig Prize contest. In both cases the media supplied the scale: the same photographs, the same accounts, and the same parade images reached towns neither man would ever visit. New York welcomed Lindbergh home with a ticker tape parade on June 13, 1927, and the parade itself became content, photographed and filmed for the rest of the country. Students should be able to state the formula in their own words: a celebrity is made when a real deed meets a distribution system. Either half alone is not enough. A great deed without the system stays a local story, and the system without a deed has nothing durable to amplify, which is why the fads of the next section faded within months.",
             kick='F · The hero of 1927', size=25)

# ------------------------------------------------- 23 · SECTION G DIVIDER
divider_text('Section G', 'Fads, Advertising, and the Voices Left Out',
             'The shared culture had a price, a sponsor, and a margin.',
             "The final section refuses to end the lesson on celebration, and students should hear the three parts of the title as one argument. Fads show the system's power at its most trivial: it could make the whole country buy a game or watch a stunt within weeks, and drop it within months. Advertising explains the system's economics: sponsors and studios paid for nearly all of it, so the shared culture was built to address the audiences advertisers most wanted to reach. The voices left out are the consequence: Americans outside that address did not simply wait to be included. Black Americans built newspapers of their own, immigrant communities sustained their own papers and radio hours, and women filled the screens while holding few of the jobs that decided what the country saw. A complete answer to the lesson question needs all three parts, and the exit ticket requires the third.")

# ------------------------------------------------------ 24 · FADS
content_text('Crazes the media made',
             ['Mah jongg sets sold out in the early decade.',
              'In 1924, crossword puzzles became a book publishing boom.',
              'Al Shipwreck Kelly sat on a flagpole for thirteen days in 1924.',
              'Imitators followed, and each stunt was reported as news.',
              'The media that reported a fad also created it.'],
             "Define the term in the guided notes words before the examples run away with the hour. A fad is a craze that spreads quickly through the public and fades within months, such as a dance, a game, or a stunt. The decade supplied examples in every category. Mah jongg sets sold out in the early years of the decade. Crossword puzzles became a book publishing boom in 1924. Al Shipwreck Kelly sat on a flagpole in Atlantic City for thirteen days in 1924, and imitators followed, each stunt reported as news. The reading's sharpest sentence belongs here: the media that reported a fad also created it. Coverage was not a mirror held up to a craze that existed independently. Without national coverage there was no national craze, only a man on a pole in one city. Fads are the purest proof of the system's power, because the content was nearly nothing and the spread was nearly total, and they faded because nothing real held them up.",
             kick='G · Fads, advertising, and the voices left out', size=25)

# ------------------------------------------------------ 25 · VOICES LEFT OUT
content_text('Who the shared culture left out',
             ['Advertising paid for nearly all of the system.',
              'The shared culture was also a shared national market.',
              'Black Americans built media of their own, including the Chicago Defender.',
              'Immigrant communities sustained foreign language papers.',
              'Women filled screens and held few of the deciding jobs.',
              'Network radio kept Black performers at its margins.'],
             "End the content where the reading ends, with the address of the shared culture. Advertising paid for nearly all of this system: sponsors bought radio programs and newspaper space, and studios sold films together with the products placed around them. The shared national culture was therefore also a shared national market, addressed to the Americans advertisers most wanted to reach, and that address left people out. Black Americans built media of their own, including the Chicago Defender and other Black newspapers, while network radio kept Black performers at its margins and its most popular Black characters were white actors in dialect. Immigrant communities sustained foreign language papers and local radio hours the networks ignored. Women filled screens and photographs and held few of the jobs that decided what the country would see and hear. The reading's verdict is balanced and students should keep both halves: the new media gave Americans a common culture for the first time, and it did not give every American the same place inside it.",
             kick='G · Fads, advertising, and the voices left out', size=23)

# ------------------------------------------------------ 26 · THE SYSTEM AT A GLANCE
s = slide(NAVY)
kicker(s, 'The system at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Four media, one culture', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Network radio', 'One program in dozens of cities at the same hour', 'Sponsors paid; Black voices stayed at the margins'),
        ('Movies and talkies', 'The same films, then the same spoken lines, in every region', 'Studios and advertisers paid; few women decided'),
        ('Tabloids', 'The same wire photographs and famous faces each morning', 'The papers chose which faces the country saw'),
        ('Sports coverage', 'The same fights and games, followed daily nationwide', 'Promoters and papers profited from the stars they built')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, The System at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. Each row pairs what a medium shared with who paid and who was left out, because the lesson's argument needs both columns. Network radio shared one program across dozens of cities at the same hour, paid for by sponsors, with Black performers at its margins. Movies and talkies shared identical films and, after 1927, identical voices, paid for by studios and advertisers, with women holding few deciding jobs. Tabloids shared wire photographs and famous faces each morning, and the papers themselves chose the faces. Sports coverage shared the same fights and games daily, and promoters and papers profited from the stars the coverage built. Grade the table generously on wording and strictly on the pairing: every row must name a sharing mechanism and a limit.")

# ------------------------------------------------------ 27 · VOCAB A
vocab('Words for the new media',
      [('mass media', 'forms of communication that reach very large audiences at the same time, including radio, film, and newspapers sold across the country'),
       ('broadcast', 'to send a program by radio waves to many listeners at once from a single station'),
       ('radio network', 'a group of stations linked by wire that carry the same programs at the same time under one company'),
       ('talkie', 'a motion picture with recorded dialogue and sound, which replaced silent film after 1927')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. The first term is mass media: forms of communication that reach very large audiences at the same time, including radio, film, and newspapers sold across the country. The load bearing phrase is at the same time; size alone is not the point, simultaneity is. Broadcast: to send a program by radio waves to many listeners at once from a single station. One sender, many listeners, one moment: that triangle is the whole radio story. Radio network: a group of stations linked by wire that carry the same programs at the same time under one company. Linked by wire and under one company separate a network from stations merely playing similar programs. Talkie: a motion picture with recorded dialogue and sound, which replaced silent film after 1927. The date in the definition is the hinge year of the lesson.")

# ------------------------------------------------------ 28 · VOCAB B
vocab('Words for fame and crazes',
      [('tabloid', 'a newspaper printed in a smaller format that used large photographs and bold headlines to report crime, scandal, and celebrity news'),
       ('celebrity', 'a person who is widely known and followed by the public because the media cover his or her life and work'),
       ('fad', 'a craze that spreads quickly through the public and fades within months, such as a dance, a game, or a stunt')],
      "Three more terms, again matching the guided notes exactly. Tabloid: a newspaper printed in a smaller format that used large photographs and bold headlines to report crime, scandal, and celebrity news. Smaller format is the literal meaning; the photographs and headlines are what the format was for. Celebrity: a person who is widely known and followed by the public because the media cover his or her life and work. Because the media cover is the definition's engine: Ruth and Lindbergh qualify not only for what they did but for the coverage that carried it. Fad: a craze that spreads quickly through the public and fades within months, such as a dance, a game, or a stunt. Quickly and fades are the two halves to stress. Flagpole sitting spread nationally in weeks and vanished just as fast, which is what separates a fad from a lasting change in culture.")

# ------------------------------------------------------ 29 · CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did radio, movies, and the popular press give Americans a shared national culture for the first time? Answer with simultaneity, not just popularity.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'One Week of Media, 1927: stations on radio, film, print, sport, and the flight'),
        ('Notebook', 'Notebook page: rebuild the system at a glance in your own words'),
        ('Quick check', 'The Fight of the Century: Dempsey, Carpentier, and the radio audience'),
        ('Writing', 'A Culture Heard at the Same Hour: the lesson question as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the network effect, two national figures of 1927, and the lesson question with one margin named.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, One Week of Media, 1927, runs stations across the media of the lesson, so students handle the radio schedule, the film, the front page, the fight, and the flight as one week's experience. The notebook page asks them to rebuild the system at a glance themselves. The quick check, The Fight of the Century, tests the Dempsey fight and the radio audience that heard it. The writing task, A Culture Heard at the Same Hour, turns the lesson question into an essay. The strongest essays will argue simultaneity and sameness: networks put one program into dozens of cities at one hour, talkies gave every region the same voices, and wire photographs put the same faces in every city on the same morning. The exit ticket has three parts: why a network changed radio more than a stronger station would have, two national figures of 1927 with what each one did, and the lesson question answered in two or three sentences with one group at the margins named.")

dc.save(OUT)
