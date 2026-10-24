#!/usr/bin/env python3
"""Lesson 4 deck, "Open Doors and the Big Stick," built to the approved pilot system:
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
text(s, 0.9, 5.32, 11.5, 0.4, 'IMPERIALISM AND WORLD WAR I · LESSON 4', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Open Doors and the Big Stick', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Notes, warships, a bargain, and bank loans across two oceans', size=17, color=POWDER)
notes(s, "The image is Putting His Foot Down, a chromolithograph cartoon by J. S. Pughe from Puck in 1899, now held by the Library of Congress. Uncle Sam stands on a map of China holding a paper marked Trade Treaty China while rulers of the European powers cut at the map with shears. Open with the puzzle the cartoon poses. The United States wanted the trade and the influence the other powers were carving out for themselves, yet in China it took no colony and held no sphere of its own. This lesson follows the instruments it used instead, across two oceans: diplomatic notes in China, a quiet bargain with Japan, a revolution backed by warships in Panama, a claimed police power in the Caribbean, and bank loans under President Taft. Each instrument projected power without a formal colony. Each one also sent a cost to the people on the receiving end, and students should track both sides of that ledger from the first slide to the exit ticket.")

# ------------------------------------------------- 2 ESSENTIAL QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did the United States project power in Asia and Latin America without ruling formal colonies there?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('Why did the United States seek power overseas, and how did the First World War change the country that fought it?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Read the lesson question slowly, because its wording does analytical work. Project power is the verb: the United States found ways to shape what other governments and peoples could do. Without ruling formal colonies is the limit that defines the lesson, and it separates this lesson from the last two. In the Philippines and Puerto Rico the United States ruled territory directly. In China, Japan, Panama, and the Caribbean it mostly did not, and the question is what it used instead. Students should finish the hour able to name five instruments, the note, armed force, control of a route, a claim to police power, and loans backed by force, and to give one fact for each. The unit question runs underneath, and this lesson is its clearest case of seeking power overseas short of annexation. Keep the lesson question visible, return to its exact wording at the end, and note that the third exit ticket question asks students to name the cost of one instrument to the people who received it.")

# --------------------------------------------------- 3 THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.3, 11.5, 1.0, 'Five instruments, two oceans', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.42)
rows = [('A', 'Notes instead of a colony in China', 'Hay, the spheres, and equal trade'),
        ('B', 'The Boxer Rebellion', 'an uprising, a siege, and an eight-nation force'),
        ('C', 'A bargain with Japan', 'a school order withdrawn, passports limited'),
        ('D', 'Panama: a revolution and a canal', 'independence, a zone ten miles wide, a canal by 1914'),
        ('E', 'The Roosevelt Corollary', 'order and debts, policed by the United States'),
        ('F', 'Dollar diplomacy in Nicaragua', 'loans, a customs collector, and Marines in 1912')]
yy = 2.72
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.7, n, size=24, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.03, 3.6, 0.7, t, size=20, color=CREAM, bold=True)
    text(s, 5.35, yy + 0.08, 7.1, 0.7, d, size=17, color=POWDER)
    yy += 0.78
notes(s, "This is the map of the lesson, and it follows the guided notes section by section. Sections A and B are set in China: first the diplomatic notes Secretary of State John Hay sent in 1899, then the Boxer Rebellion of 1900, which showed the armed force standing behind the paper. Section C stays in Asia but changes method, a negotiated bargain with Japan. Sections D, E, and F cross the Pacific to Latin America: the Panama Canal and the revolution that cleared its path, the Roosevelt Corollary that claimed a police power over the Caribbean, and dollar diplomacy in Nicaragua, where loans replaced troops until troops landed anyway. Tell students to keep the two oceans separate in their notes and to attach one named place and one date to every instrument. The activity asks them to classify all five stations by instrument, so the names used on this slide are the names they will need there.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_photo('foot-port.jpg', 'Section A', 'Notes Instead of a Colony in China',
              ['Paper promises stood in place of a province.'],
              "The image is a portrait crop of the same 1899 Puck cartoon that opened the lesson, J. S. Pughe's Putting His Foot Down, held by the Library of Congress. Uncle Sam fills the frame, one hand on his sword, holding the trade treaty, while two kneeling rulers trim the edge of the map of China with shears. Use the crop to fix the American position before the facts begin. Every other power in the cartoon is cutting off a piece. The United States is standing on the map with a piece of paper. That paper is the subject of this section. By 1899 the great powers had divided coastal China into spheres of influence, and the United States held none. Secretary of State John Hay had to protect American trade in a country his country did not rule and could not partition. His answer was a set of notes, and section A takes the division of China first, then the notes themselves, promise by promise.",
              title_size=40)

# ------------------------------------------------------ 5 SPHERES
content_photo_s('foot-port.jpg', 'A coast divided into spheres',
             ['Germany held privileges in Shandong.',
              'Russia held ports and railways in Manchuria.',
              'Britain held the lead in the Yangtze valley.',
              'The United States held no sphere of its own.',
              'Hay feared the spheres would harden into colonies and shut American trade out.'],
             "Start with the key term in its full guided notes form. A sphere of influence is a region in which one outside power holds dominant trading and investment privileges over the others. By 1899 the great powers had divided coastal China into such spheres. Germany held privileges in Shandong, Russia held ports and railways in Manchuria, and Britain led in the Yangtze valley. The United States held no sphere, and that absence drove everything Secretary of State John Hay did next. His fear was practical, not abstract. If each sphere hardened into a formal colony, its holder could favor its own merchants, charge foreign goods more, and in time shut American trade out of the largest market in Asia. Point out what a sphere was not. It was not yet annexation, and China still had its own government. The whole lesson turns on that middle ground, power exercised inside another country's borders without ruling the country outright, and China in 1899 is the first example.",
             kick='A · Notes instead of a colony in China')

# ------------------------------------------------------ 6 HAY NOTES
content_text("Hay's Open Door notes, 1899",
             ['On September 6, 1899, Hay sent notes to the powers.',
              'He asked for equal treatment for the trade of all nations.',
              'Chinese officials would still collect the duties.',
              'The powers answered with conditions.',
              'In March 1900, Hay treated the answers as acceptance.'],
             "Give students the policy in its full guided notes form first. The Open Door is the 1899 and 1900 United States policy calling for equal trading rights for all nations in China and for China to remain one country. On September 6, 1899, Hay sent notes to the powers asking each to promise equal treatment for the trade of all nations inside its sphere. The activity reads the note itself, and its three promises are worth naming here: no interference with treaty ports or vested interests, the Chinese treaty tariff applied to the goods of all nations with the duties collected by the Chinese government, and no higher harbor dues or railroad rates charged to foreigners than to the sphere holder's own people. The collector detail carries the policy. Revenue stayed Chinese, so the note claimed access for everyone's trade while leaving China's government formally in charge of its own ports. The powers answered with conditions, each making its promise depend on the others, and in March 1900 Hay simply treated the answers as acceptance and announced the policy as settled.",
             kick='A · Notes instead of a colony in China', size=24)

# ------------------------------------------------- 7 SECTION B DIVIDER
divider_photo('pekin-port.jpg', 'Section B', 'The Boxer Rebellion',
              ['An uprising against foreign influence led to a siege in Beijing.'],
              "The image is by Kasai Torajiro, a Japanese artist, and it is a chromolithograph print from 1900, not a photograph. It shows allied troops attacking a gate in Beijing during the Boxer Rebellion, with Japanese and American flags visible among the attackers, and it is held by the Library of Congress. Tell students plainly that it is a print, made to be sold and admired, because the distinction between a print and a photograph is part of reading any image from this lesson honestly. The scene shows the moment the paper policy of section A met armed force. Many Chinese blamed foreigners for their country's weakness, and a Qing government that failed to resist them. In 1900 that anger turned into an uprising, foreign troops marched on the capital, and the Open Door survived because an eight-nation army, including Americans, fought its way to Beijing. Section B traces the rebellion from its targets to its price.",
              title_size=54)

# ------------------------------------------------------ 8 BOXER REBELLION
content_photo_s('pekin-port.jpg', 'Attack, siege, and relief',
             ['The Boxers were the Society of Righteous and Harmonious Fists.',
              'They targeted missionaries, Chinese Christians, railroads, and telegraph lines.',
              'In June 1900, the Beijing legations were besieged for about eight weeks.',
              'Eight nations sent the force that lifted the siege in August.',
              "During the siege, Hay's second note called for keeping China one country."],
             "Give the term in full first. The Boxer Rebellion is the 1900 uprising in China by the Boxers, a society opposed to foreign influence, put down by an eight-nation force that included United States troops. The Boxers, members of a society whose name translates as the Society of Righteous and Harmonious Fists, attacked missionaries, Chinese Christians, railroads, and telegraph lines, the people and the hardware carrying foreign influence into the countryside. In June 1900 the Boxers and Qing government troops besieged the foreign legations in Beijing for about eight weeks. An alliance of eight nations sent an expedition that fought its way to Beijing in August and lifted the siege. During the siege, on July 3, 1900, Hay sent his second Open Door note, asking the powers to preserve China as one country. Hold the two facts together for students: the same government that asked for a whole and open China in July had soldiers marching on its capital in August.",
             kick='B · The Boxer Rebellion')

# ------------------------------------------------------ 9 STAT
stat('333 MILLION', 'dollars: the indemnity the Boxer Protocol charged China',
     'Payable over 39 years. Foreign deaths numbered in the hundreds; Chinese Christians died in the tens of thousands.',
     "Dwell on the bill, because it is the cost side of the Open Door made countable. The Boxer Protocol of 1901 forced China to pay an indemnity of about 333 million dollars over 39 years, a debt hung on the Chinese government by the same powers whose trade the Open Door kept open. Put the human figures beside the financial one, as the reading does. Foreign deaths during the rebellion numbered in the hundreds. Chinese Christians died in the tens of thousands, and Boxers and Chinese soldiers died in large numbers during the fighting and the occupation that followed. Students should see the asymmetry without being pushed to a slogan. The preserved China of Hay's second note was also a China billed for its own invasion, and its people paid in lives first and in silver for two generations after. When the exit ticket asks for the cost of one instrument to the people on the receiving end, this slide is the richest source of an answer in the whole lesson.",
     kick='B · The Boxer Rebellion')

# ------------------------------------------------- 10 SECTION C DIVIDER
divider_text('Section C', 'A Bargain with Japan',
             'No notes to six powers this time: a protest, a withdrawn order, and an agreement.',
             "This section has no divider photograph, and the reason is the state of the record rather than an oversight. The lesson's verified images cover China, Panama, and the Caribbean. The bargain with Japan was conducted in protests, meetings, and withheld passports, and no verified period image of it sits in the lesson set. The contrast with China is the place to start. In China the United States dealt with European powers over the head of a weakening Qing government. Japan was a rising power in Asia, a treaty partner that expected to be treated as an equal and said so when it was not. So the method changed. There were no notes demanding promises from six governments. There was a local school board order in San Francisco, a formal Japanese protest, a president who intervened in a city decision, and a reciprocal understanding in 1907 and 1908. Section C takes the order first, then the bargain it produced, then the discrimination the bargain left standing.")

# ------------------------------------------------------ 11 SCHOOL ORDER
content_text('A school order and a protest, 1906',
             ['In October 1906, San Francisco ordered Japanese and Korean students segregated.',
              'Japan protested that the order insulted a treaty partner.',
              'Roosevelt stepped in and persuaded the board.',
              'The board withdrew the order.'],
             "Slow down on how small the trigger was and how large the response became. In October 1906 the San Francisco school board ordered Japanese and Korean students into a segregated school. Japan protested the order as an insult to a treaty partner, which is the phrase students should keep. Tokyo was not asking for a favor. It was claiming the respect owed to one government by another under treaty, and it expected Washington to answer for a California city's decision. President Theodore Roosevelt persuaded the board to withdraw the order. Ask students why a president would spend his authority on one school board. The reading's framing supplies the answer: with Japan, the rising power in Asia, the United States bargained instead of dictating. A humiliated Japan was a strategic problem in the Pacific, where American trade, the Philippines, and the new canal route all depended on calm relations. The withdrawal was the American half of a trade, and the next slide gives the Japanese half.",
             kick='C · A bargain with Japan', size=24)

# ------------------------------------------------------ 12 GENTLEMEN'S AGREEMENT
content_text("The Gentlemen's Agreement, 1907 and 1908",
             ['Japan stopped issuing passports to laborers bound for the mainland.',
              'The United States ended the San Francisco segregation.',
              'The agreement was no law and no treaty: it was an understanding between governments.',
              'In 1913, California barred Japanese immigrants from owning farmland.'],
             "Give the term in its full guided notes form. The Gentlemen's Agreement is the 1907 and 1908 understanding in which Japan limited the emigration of its laborers to the United States and the United States ended the segregation of Japanese students in San Francisco schools. Note the form of the instrument, because the lesson is a catalogue of forms. This was not a statute and not a ratified treaty. It was an exchange of commitments between two governments, each giving the other a face saving way to step back: Tokyo limited the departure of its own laborers, and Washington delivered the withdrawal of the school order. Then give the limit the reading insists on. The bargain did not end discrimination. California barred Japanese immigrants from owning farmland in 1913, six years after the agreement. Students should leave this section able to say both things at once: the United States treated Japan as a power to bargain with, and Japanese people in America still faced laws aimed at them by name.",
             kick='C · A bargain with Japan', size=24)

# ------------------------------------------------- 13 SECTION D DIVIDER
divider_photo('gatun-port.jpg', 'Section D', 'Panama: A Revolution and a Canal',
              ['A province broke away, and a canal zone was born.'],
              "The photograph shows the Gatun Locks of the Panama Canal looking toward the Atlantic entrance, photographed for the Byron Company and held by the Library of Congress. Date it carefully for students: it is about 1913, during construction, a year before the canal opened, which is why barges and work crews fill the lock chamber instead of ocean shipping. A canal across Central America would move the United States Navy between the oceans in weeks instead of a voyage around South America, and the best route crossed Panama, then a province of Colombia. This section has two halves that students must not merge. The first is acquisition: a rejected treaty, a revolution, American warships, and a canal zone granted within days. The second is construction: a decade of digging, thousands of dead workers, and an opening in August 1914. One more caution belongs here. The route map in the lesson documents is a diagram drawn for the activity, not a historical source, and its caption says so.",
              title_size=40)

# ------------------------------------------------------ 14 PANAMA REVOLUTION
content_text('Revolution on the isthmus, 1903',
             ['The best canal route crossed Panama, a province of Colombia.',
              "Colombia's senate rejected the canal treaty.",
              'On November 3, 1903, Panama declared independence.',
              'United States warships kept Colombian troops from the isthmus.',
              'The United States recognized Panama within days and signed a treaty for a zone ten miles wide.',
              'The terms were 10 million dollars, plus an annual payment.'],
             "Walk the sequence in order, because the guided notes test it step by step and the order is the argument. A canal across Central America would move the United States Navy between the oceans in weeks, and the best route crossed Panama, then a province of Colombia. When Colombia's senate rejected the canal treaty in 1903, Panamanian leaders declared independence on November 3. United States warships kept Colombian troops from reaching the isthmus, so the revolution succeeded without Colombia being able to contest it on the ground. The United States recognized Panama within days, and the new republic signed a treaty giving the United States a canal zone ten miles wide for 10 million dollars and an annual payment. Ask students to name the instrument precisely. It was not annexation of Panama, and Panama remained a country. It was a revolution protected by American sea power, followed immediately by a treaty with the government that sea power had made possible. Control of a route was obtained without ruling the nation the route crossed.",
             kick='D · Panama: a revolution and a canal', size=24)

# ------------------------------------------------------ 15 CANAL BUILDING
content_photo_s('ancon-port.jpg', 'Building the canal, 1904 to 1914',
              ['The canal took a decade of digging across the isthmus.',
               'About 5,600 workers died, most of them West Indian laborers.',
               'On August 15, 1914, the SS Ancon made the first official transit.',
               'In 1921, Colombia received 25 million dollars.'],
              "The photograph shows the SS Ancon in the canal channel on August 15, 1914, the day of the first official transit, from the records of the Panama Canal at the National Archives. Give the term in full here. The Panama Canal is the ship canal across the Isthmus of Panama, built by the United States between 1904 and 1914, linking the Atlantic and Pacific Oceans. The route students traced in the activity diagram runs from Colon through the Gatun Locks and Gatun Lake, across the Culebra Cut, and down to Panama City, about 50 miles inside the ten mile wide zone. Remember that the diagram is a teaching drawing, not a source. The costs belong on this slide in plain numbers. Construction killed about 5,600 workers by the official count, most of them West Indian laborers. Colombia received 25 million dollars in 1921, in what many Colombians read as payment for a lost province. The canal was a triumph of engineering and a transfer of other people's land, labor, and lives, and the lesson keeps both sentences.",
              kick='D · Panama: a revolution and a canal')

# ------------------------------------------------- 16 SECTION E DIVIDER
divider_photo('bigstick-port.jpg', 'Section E', 'The Roosevelt Corollary',
              ['The big stick was written into doctrine.'],
              "The image is The Big Stick in the Caribbean Sea, a cartoon by William Allen Rogers from 1904, held by the Library of Congress. Roosevelt wades barefoot through the Caribbean carrying a large club and towing a line of warships behind him. Read the ship labels with students, because they state the policy in three words: The Receiver, The Sheriff, and Debt Collector. The shores are labeled Santo Domingo, Cuba, Mexico, and Panama. The cartoon appeared the same year Roosevelt announced the Corollary, and it understood him. His argument began with a real event. Britain, Germany, and Italy had blockaded Venezuela in 1902 and 1903 to collect debts, landing European warships in the hemisphere the Monroe Doctrine claimed to guard. Roosevelt's answer was to claim the collecting for the United States. Section E gives the doctrine in his own terms, then its first test in the Dominican Republic a year later.",
              title_size=44)

# ------------------------------------------------------ 17 COROLLARY
content_photo_s('bigstick-port.jpg', 'The Corollary, December 6, 1904',
             ['The Corollary was an addition to the Monroe Doctrine of 1823.',
              'A country that kept order and paid its obligations had no interference to fear.',
              'Chronic wrongdoing could bring a United States international police power.',
              'The stated aim was to leave Europe no reason to intervene.'],
             "Give the term in its full guided notes form first. The Roosevelt Corollary is Theodore Roosevelt's 1904 addition to the Monroe Doctrine claiming a United States right to intervene in Latin American countries guilty of chronic wrongdoing or unable to pay their debts. Roosevelt announced it in his Annual Message of December 6, 1904, and the activity reads his passage whole. His test had two sides. A country that kept order and paid its obligations, he said, need fear no interference. One that did not could face a United States international police power, so that Europe had no reason to intervene. Students should hear the move the Corollary makes. The Monroe Doctrine of 1823 told European powers to stay out of the Americas. The Corollary turned that warning outward into a warrant inward: to keep Europeans from intervening, the United States claimed the right to intervene first, and to decide for itself which governments counted as orderly. Later presidents cited it to justify occupations of Cuba, Nicaragua, Haiti, and the Dominican Republic.",
             kick='E · The Roosevelt Corollary')

# ------------------------------------------------------ 18 DOMINICAN TEST
content_text('First test: the Dominican Republic, 1905',
             ['American officials took over the customhouses.',
              'They collected the import taxes themselves.',
              'Foreign creditors received a fixed share of the revenue.',
              'The canal route gained a guarded approach.'],
             "The first test came quickly, and it shows what the police power looked like in practice. Roosevelt argued that the canal made Caribbean order an American duty, and he feared European warships returning to the Dominican Republic, on the route to Panama, as they had gone to Venezuela. In 1905 the United States took over the Dominican customhouses, collected the import taxes, and paid foreign creditors a fixed share of the revenue. Pause on the choice of target. Customs duties were the income a Caribbean government lived on, so collecting them was governing in everything but name, while the country kept its flag, its president, and its formal independence. That is the lesson question in miniature: power projected, colony avoided. It also removed the excuse for European intervention, which was the purpose Roosevelt stated. When students reach section F, ask them to remember this arrangement, because dollar diplomacy in Nicaragua used the same customs house, reached by loans instead of a doctrine.",
             kick='E · The Roosevelt Corollary')

# ------------------------------------------------- 19 SECTION F DIVIDER
divider_photo('taft-port.jpg', 'Section F', 'Dollar Diplomacy in Nicaragua',
              ['Taft promised dollars in place of bullets, with force held in reserve.'],
              "The image is the cover of Puck for February 24, 1909, by Samuel D. Ehrhart, held by the Library of Congress. Outgoing President Theodore Roosevelt, dressed as a cowboy, hands a baby labeled My Policies to incoming President William Howard Taft, who wears a nursemaid's apron and bonnet, while Roosevelt's secretary William Loeb, dressed as a bellboy, carries the big stick out behind them. Students must be told exactly what this cartoon is and is not. It documents the 1909 transfer of Roosevelt's policies to Taft. It does not depict dollar diplomacy itself, and no period cartoon specifically about dollar diplomacy could be verified for this lesson, so the policy is carried by Taft's own words and the Nicaragua account. Taft's claim was that his diplomacy substituted dollars for bullets. Section F states the policy, then follows it into Nicaragua, where the claim met its test in 1912.",
              title_size=36)

# ------------------------------------------------------ 20 DOLLAR DIPLOMACY
content_text('Dollars in place of bullets',
             ["Taft's instrument was American loans and investment.",
              'The loans were backed by government pressure, not by annexation.',
              'Customs revenue secured the loans.',
              'Nicaragua became the test case.'],
             "Give the term in its full guided notes form. Dollar diplomacy is President Taft's policy of using American loans and investment, backed by government pressure, to extend United States influence abroad. Taft said his diplomacy substituted dollars for bullets, a phrase from his Fourth Annual Message of December 3, 1912, which the activity quotes. Explain the mechanism in plain steps, because students often hear the slogan and miss the machinery. The government encouraged American bankers to lend to Caribbean governments Washington wanted to steady. The loans were secured by the borrower's customs revenue, the same revenue the United States had collected directly in the Dominican Republic. A government that owed American banks, and whose customs were watched by an American collector, had strong reasons to keep Washington satisfied, all without annexation, a governor, or a flag change. The instrument was finance, and its enforcement clause was written in customs receipts. Whether it could work without soldiers behind it is the question Nicaragua answered.",
             kick='F · Dollar diplomacy in Nicaragua')

# ------------------------------------------------------ 21 NICARAGUA
content_text('Nicaragua, 1909 to 1912',
             ['In 1909, Washington backed the overthrow of President Zelaya.',
              'Then came American bank loans and an American customs collector.',
              'In 1912, a revolt rose against the government the loans supported.',
              'About 2,500 Marines and sailors landed.',
              'A Marine guard stayed for years.'],
             "List the steps in the guided notes order, because section F asks students to reproduce them. In Nicaragua, the United States backed the overthrow of President Jose Santos Zelaya in 1909. It then arranged American bank loans to the new government and set an American collector over Nicaraguan customs, the revenue that secured the loans. When Nicaraguans revolted in 1912 against the government those arrangements supported, about 2,500 Marines and sailors landed to protect it, and a Marine guard stayed for years afterward. Draw the conclusion the reading draws, in its own careful terms. Each instrument in this lesson projected power without a formal colony, and each sent its bill to someone else: to China in indemnity payments, to Colombia in a lost province, to canal workers in lives, and to Caribbean peoples in customs revenue and governments they did not choose. Nicaragua adds a sharper point. The dollars had not replaced the bullets. They had only decided where the bullets would be aimed, and in 1912 they were fired in defense of a loan.",
             kick='F · Dollar diplomacy in Nicaragua', size=24)

# ------------------------------------------------------ 22 VOCAB A
vocab('Words for China',
      [('Open Door', 'the 1899 and 1900 United States policy calling for equal trading rights for all nations in China and for China to remain one country'),
       ('sphere of influence', 'a region in which one outside power holds dominant trading and investment privileges over the others'),
       ('Boxer Rebellion', 'the 1900 uprising in China by the Boxers, a society opposed to foreign influence, put down by an eight-nation force that included United States troops')],
      "These definitions match the guided notes word for word, and students should copy them exactly. Open Door: the 1899 and 1900 United States policy calling for equal trading rights for all nations in China and for China to remain one country. Both halves belong in the definition, access and preservation, because Hay's second note in July 1900 added the second half while the legations were under siege. Sphere of influence: a region in which one outside power holds dominant trading and investment privileges over the others. Stress the word privileges. A sphere was influence inside another country's territory, short of owning it. Boxer Rebellion: the 1900 uprising in China by the Boxers, a society opposed to foreign influence, put down by an eight-nation force that included United States troops. The definition names the suppressors as carefully as the rebels, and students should notice that the force, not any single nation, ended the uprising.")

# ------------------------------------------------------ 23 VOCAB B
vocab('Words for the Caribbean claim',
      [('Roosevelt Corollary', "Theodore Roosevelt's 1904 addition to the Monroe Doctrine claiming a United States right to intervene in Latin American countries guilty of chronic wrongdoing or unable to pay their debts"),
       ('dollar diplomacy', "President Taft's policy of using American loans and investment, backed by government pressure, to extend United States influence abroad")],
      "Two more definitions, in guided notes order, and together they name the two Caribbean instruments. Roosevelt Corollary: Theodore Roosevelt's 1904 addition to the Monroe Doctrine claiming a United States right to intervene in Latin American countries guilty of chronic wrongdoing or unable to pay their debts. Both triggers in the definition deserve attention, wrongdoing and unpaid debts, because the second one turned a financial problem into grounds for intervention and produced the Dominican customs takeover within a year. Dollar diplomacy: President Taft's policy of using American loans and investment, backed by government pressure, to extend United States influence abroad. The phrase backed by government pressure is the honest core of the term. Without it, loans are just banking. With it, a loan becomes an instrument of state, and Nicaragua in 1912 showed how short the distance was between the pressure and the Marines who finally supplied it.")

# ------------------------------------------------------ 24 VOCAB C
vocab('Words for the route and the bargain',
      [('Panama Canal', 'the ship canal across the Isthmus of Panama, built by the United States between 1904 and 1914, linking the Atlantic and Pacific Oceans'),
       ("Gentlemen's Agreement", 'the 1907 and 1908 understanding in which Japan limited the emigration of its laborers to the United States and the United States ended the segregation of Japanese students in San Francisco schools')],
      "The last two terms, again matching the guided notes exactly, and they return students to the two halves of the lesson. Panama Canal: the ship canal across the Isthmus of Panama, built by the United States between 1904 and 1914, linking the Atlantic and Pacific Oceans. The dates in the definition are the building years, and students should attach the human figures to them: about 5,600 workers dead, most of them West Indian laborers, and a zone ten miles wide held under a treaty signed days after independence. Gentlemen's Agreement: the 1907 and 1908 understanding in which Japan limited the emigration of its laborers to the United States and the United States ended the segregation of Japanese students in San Francisco schools. Point out the word understanding. It was neither a law nor a treaty, and its informality was the point, letting two governments trade concessions without either one backing down in public.")

# ------------------------------------------------------ 25 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Power without colonies?', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Return to the lesson question, then test it at the stations. Keep the note, the force, the route, the doctrine, and the loans separate.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'Instruments of Power stations: five stations, five instruments'),
        ('Notebook', 'The instrument chart: two oceans, compared'),
        ('Quick check', 'The Big Stick in the Caribbean Sea, Rogers, 1904'),
        ('Writing', 'Power Without Colonies? Judge one instrument and its cost')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.5, 0.6, d, size=19, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.8, 11.5, 0.5, "Exit ticket: name the instruments used in China and Nicaragua, apply the Corollary to a debt default, and name one instrument's cost.",
     size=16, color=POWDER)
notes(s, "Close by returning to the lesson question: how did the United States project power in Asia and Latin America without ruling formal colonies there. The answer the lesson has built is a list of instruments, each with a place, a date, and a price. Notes in China in 1899, backed by an eight-nation force in 1900. A bargain with Japan in 1907 and 1908. A protected revolution and a canal in Panama between 1903 and 1914. A police claim in 1904, tested in Dominican customhouses in 1905. Loans in Nicaragua after 1909, defended by Marines in 1912. Now hand the question to the work. In the Instruments of Power stations, groups classify all five stations by instrument and judge which one changed the most on the ground. The notebook page compares the instruments across the two oceans. The quick check returns to the Rogers cartoon from section E, and the writing task asks the closing question at full length: power without colonies, judged with one instrument and its cost. Next lesson turns to 1914, a European war, and an America trying to stay neutral.")

dc.save(OUT)
