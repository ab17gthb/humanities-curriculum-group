#!/usr/bin/env python3
"""Lesson 4 deck, built to the approved Lesson 1 system (2026-10-21):
image-led slides, fragments only on screen, comprehensive speaker notes,
full lesson + vocabulary coverage. Fonts: Georgia titles, Lato body."""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags,
                         photo_right, divider_photo, content_photo,
                         content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED)
from pptx.util import Inches
from pptx.enum.text import PP_ALIGN

dc.IMG = os.path.join(HERE, 'img')
OUT = os.path.join(HERE, '..', 'lesson-04-slides.pptx')
W = 13.333

# ---------------------------------------------------------------- 1 · TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, dc.prs.slide_width, dc.prs.slide_height)
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'PROGRESSIVE ERA · LESSON 4', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Roosevelt and the Square Deal', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'A new president makes the federal government a referee', size=17, color=POWDER)
notes(s, "The photograph shows Theodore Roosevelt at Glacier Point in Yosemite in 1903, standing with the naturalist John Muir. Keep it in mind, because that camping trip becomes evidence later in the lesson: Muir pressed Roosevelt to protect Yosemite, and the conservation side of the Square Deal grows out of encounters like this one. Set the frame before the details. Roosevelt is the first president in this unit whom students actually watch doing things. He did not win the office on a reform platform. An assassin handed it to him, and he then used it more aggressively than any president since Lincoln. His domestic program, the Square Deal, had three sides: controlling corporations, protecting consumers, and conserving natural resources. Each side put the federal government somewhere voters could watch it work. The deck and the guided notes follow the same three-part structure, so students can always tell where they are.")

# ------------------------------------------------- 2 · ESSENTIAL QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did Roosevelt use the presidency to referee between business, labor, and the public?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did Americans respond to the problems created by industrialization, urbanization, and political corruption?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's lesson question is new. The unit question beneath it is unchanged: How did Americans respond to the problems created by industrialization, urbanization, and political corruption? Lessons 1 through 3 have supplied the problems and the first responses, the muckrakers who exposed them and the political reforms that attacked corrupt machinery. Today the response acquires a president. Roosevelt matters to the question because he moved the response into the federal government itself, and he did it across all three problem areas of Lesson 1 at once: corporate power, unsafe products, and wasted land. A useful way to open discussion is to ask students what a president in 1901 was normally expected to do about a coal strike or a railroad merger. The honest answer is very little. Measuring Roosevelt against that low expectation is how students grasp why contemporaries found him startling, and why his own party's leaders found him alarming.")

# ------------------------------------------------- 3 · THE DEAL IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.35, 11.5, 1.0, 'Three sides of the Square Deal', size=46, color=CREAM, font='Georgia')
rule(s, 0.92, 2.5)
rows = [('1', 'Controlling corporations', 'Northern Securities, rates, forty cases'),
        ('2', 'Protecting consumers', 'meat inspection and pure food laws, 1906'),
        ('3', 'Conservation', '230 million acres under federal care')]
yy = 2.95
for n, t, d in rows:
    text(s, 0.9, yy, 0.7, 0.7, n, size=30, color=RUST_LT, font='Georgia')
    text(s, 1.65, yy + 0.04, 5.0, 0.7, t, size=27, color=CREAM, bold=True)
    text(s, 6.85, yy + 0.10, 5.7, 0.7, d, size=20, color=POWDER)
    yy += 1.02
notes(s, "This is the map of the lesson, and it matches the reading and the guided notes exactly. Side one is controlling the corporations: the Northern Securities case, railroad rate regulation, and a run of antitrust suits. Side two is protecting the consumer: federal meat inspection and the Pure Food and Drug Act, both passed in 1906 after a novel did the persuading. Side three is conservation: about 230 million acres of public land placed under federal management, the largest conservation record of any president. Between sides one and two sits the coal strike of 1902, which the guided notes treat as its own section because it shows the whole program in a single episode. Tell students that the exit ticket asks them to name all three sides with one Roosevelt action on each, so they should collect one concrete action per side as the lesson proceeds.")

# ------------------------------------------------- 4 · SECTION A DIVIDER
divider_photo('tr-port.jpg', 'Section A', 'An Accidental President',
              ['An assassin\u2019s bullet in September 1901', 'A 42-year-old in the White House'],
              "The portrait is Roosevelt in 1904, photographed by the Pach brothers, and it is worth saying plainly how he got the job. President William McKinley was shot by an assassin in September 1901 and died days later. Roosevelt, his vice president, succeeded him at age 42, the youngest man ever to hold the office. The party leaders who had maneuvered him into the vice presidency had done it to bury him. He had been an inconveniently honest and energetic governor of New York, and the vice presidency looked like a shelf. Instead it became a launching pad. Students sometimes treat the assassination as a trivia fact. Slow down on it: the Square Deal was never voted on as a program in 1900. It is what one energetic man did with an office he was never supposed to reach, which is why the next slide, his theory of the presidency itself, matters so much.",
              title_size=40)

# ------------------------------------------------------- 5 · THE STEWARD
content_text('A steward of the people',
             ['President in September 1901, at 42, the youngest ever',
              'Party leaders had parked him as vice president to bury him',
              'The president as steward of the people',
              'Free to act on anything the Constitution does not forbid'],
             "Roosevelt's theory of the office is the engine of everything in this lesson, and the guided notes ask students to fill in the word steward. He believed the president should act as a steward of the people, doing anything the Constitution did not forbid, rather than waiting for Congress to grant permission item by item. That sounds modest. In practice it reversed the era's default, under which presidents mostly administered what Congress passed and kept out of economic life. Connect the theory backward to Lesson 1: the problems of industrial America had sat unanswered partly because nobody in Washington believed answering them was the president's job. Roosevelt believed it was precisely his job. One caution for students: the steward theory is a claim about power, not a guarantee of wisdom, and later lessons test it. Taft, who follows in Lesson 5, read the same Constitution far more narrowly, and the difference between the two readings splits the Republican Party.",
             kick='Section A · An accidental president')

# ------------------------------------------------- 6 · SECTION B DIVIDER
divider_photo('hill-port.jpg', 'Side one', 'Controlling the Corporations',
              ['The first test: the railroads of the Northwest',
               'James J. Hill built the combination Roosevelt sued'],
              "The portrait is James J. Hill, the railroad builder whose lines dominate this story, drawn in 1903. Side one of the Square Deal is corporate control, and Roosevelt chose his first target carefully. The railroads were the era's most hated corporations, the ones farmers and small shippers dealt with directly, and the Northwest combination was assembled by financiers at the very top of American business. Taking it on told every other boardroom in the country that no combination was too large or too well connected to be reached. The section's deeper point, which students should carry into the reading's first question, is method. Roosevelt's aim was regulation more than destruction: gather facts through a federal agency, then act on the facts in court or in Congress. That pattern, agency first and enforcement second, repeats on every side of the Square Deal and becomes the permanent machinery of the modern federal government.",
              title_size=36)

# ------------------------------------------------- 7 · NORTHERN SECURITIES
content_photo('railroad-port.jpg', 'Northern Securities, 1904',
              ['A holding company joined the competing Northwest railroads',
               'The Supreme Court ordered the combination dissolved',
               'Decided under the Sherman Antitrust Act',
               'No trust stood above federal reach'],
              "The photograph shows an Illinois Central locomotive, the kind of machine at stake in every railroad fight of the era. The case: the Northern Securities Company was a holding company, a corporation whose business was owning other corporations, and it controlled the competing railroads of the Northwest, lines that were supposed to compete with each other. Roosevelt's Justice Department sued under the Sherman Antitrust Act, a law passed in 1890 that presidents had rarely used and never against a combination this size. In 1904, in Northern Securities Co. v. United States, the Supreme Court ordered the combination dissolved. The reading's first question asks why this tested more than one railroad company, and the key gives the answer students should reach: the case tested whether the Sherman Act reached holding companies and the largest combinations at all. A government win meant no trust was beyond federal power, and the administration proved the point by filing more than forty further antitrust cases.",
              kick='Side one · Corporations')

# ------------------------------------------------------- 8 · REGULATION
content_text('Regulation more than destruction',
             ['Fair giants could stay; cheats could not',
              'The Bureau of Corporations (1903) gathered the facts',
              'More than forty antitrust cases followed',
              'The pattern: investigate first, then act'],
             "Correct the nickname before it hardens. Roosevelt became famous as a trust-buster, but his stated aim was regulation more than destruction. He distinguished large companies that competed fairly from those that cheated, and he preferred supervising the first kind to smashing them. Bigness alone was not the offense; dishonest conduct was. The machinery matched the philosophy. The Bureau of Corporations, created in 1903, investigated business conduct and published the facts, giving the government something it had never had: its own information about what corporations were actually doing. Armed with facts, the administration could sue, prosecute, or go to Congress for new law. This is worth a minute of class time because it explains the exit ticket's third question, whether trust-buster is the wrong nickname. A student who answers with the Bureau of Corporations and the forty cases, weighed against Northern Securities as the famous dissolution, has exactly the evidence the question is fishing for.",
             kick='Side one · Corporations')

# --------------------------------------------------------- 9 · HEPBURN ACT
content_text('The Hepburn Act, 1906',
             ['Railroads answered to the Interstate Commerce Commission',
              'The ICC could set maximum railroad rates',
              'Real power, not advice',
              'The shipper finally had somewhere to appeal'],
             "The Hepburn Act of 1906 completes side one, and it is one of the five vocabulary terms, so teach the definition here in full: the Hepburn Act (1906) is the law giving the Interstate Commerce Commission power to set maximum railroad rates. The italic point for students is the word maximum. The ICC had existed since 1887, but courts had stripped it of the power to actually fix rates; it could investigate and recommend, and railroads could ignore it. The Hepburn Act let the commission set a ceiling on what a railroad could charge, and the ceiling held unless a court overturned it. For the farmer or small shipper of Lesson 1, who had shipped at whatever rate the railroad posted, this was the federal government arriving in his freight bill. It is also the cleanest example of Roosevelt's method: an old, weak agency, given real power by new law, staffed by experts, acting continuously rather than case by case.",
             kick='Side one · Corporations')

# ------------------------------------------------- 10 · COAL STRIKE DIVIDER
divider_photo('mitchell-port.jpg', 'The coal strike', 'A Square Deal in Action',
              ['Pennsylvania anthracite country, 1902',
               'John Mitchell leads the miners; the owners refuse to meet him'],
              "The photograph shows John Mitchell, president of the United Mine Workers, arriving in the coal region during the strike, with local boys pulling his carriage. The guided notes give the coal strike its own section, between the corporations and the consumer, because it is the episode where the Square Deal stops being a list and becomes a scene. In May 1902 the anthracite miners of Pennsylvania walked out, and the owners' refusal to bargain turned a wage dispute into a national emergency as the country's winter coal supply ran down. Everything Roosevelt believed about the presidency gets tested here at once: an industry that will not talk, a union demanding recognition, and a public about to heat its homes with whatever coal remains. Tell students to watch for one thing above all: what the president threatens, and whom he threatens it against.",
              title_size=40)

# ------------------------------------------------------ 11 · THE WALKOUT
content_photo('driver-port.jpg', '140,000 miners walk out',
              ['May 1902: anthracite miners strike in Pennsylvania',
               'Demands: higher pay, shorter hours',
               'The owners refused even to meet the union',
               'Coal prices climbed as winter approached'],
              "The photograph is Lewis Hine's young driver in a coal mine, taken in West Virginia in 1908: a boy working ten hours a day underground beside his mule. It gives students the human setting of the industry that struck. The facts of the dispute are simple to state. In May 1902, some 140,000 anthracite coal miners in Pennsylvania struck for higher pay and shorter hours. Anthracite was the hard coal that heated homes and offices across the Northeast, so this was not an obscure industrial quarrel. The mine owners refused even to meet the union, treating recognition itself as the unacceptable demand. By fall, with the strike unbroken and the owners unbending, the price of coal was climbing and winter was coming. The guided notes ask for the number, 140,000, and students should also register the owners' strategy: say nothing, meet nobody, and wait for cold weather and public anger to break the strike for them. It nearly worked. It failed because the president changed the script.",
              kick='The coal strike')

# --------------------------------------------------------- 12 · THE THREAT
content_text('The referee\u2019s threat',
             ['Earlier presidents had sent troops against strikers',
              'Roosevelt invited both sides to the White House',
              'The owners still refused arbitration',
              'His answer: the Army would seize the mines and run them'],
             "Set the contrast first, because it is the whole point. Earlier presidents had sent troops against strikers; federal power in a labor dispute had always arrived on the owners' side of the line. Roosevelt instead invited both sides to the White House and pressed them to accept arbitration, one of the vocabulary terms: settling a dispute through a neutral third party whose decision both sides accept. When the owners still refused, he prepared the threat no owner could ignore: the Army would seize the mines and run them, with the government mining coal itself until the dispute settled. Notice whom the threat targeted. For the first time, a president aimed federal force at the owners rather than the strikers, and aimed it to compel talking rather than to break the strike. The owners accepted arbitration within days. Whether Roosevelt would actually have carried the threat out is a fine question for strong students; its credibility, not its execution, did the work.",
             kick='The coal strike')

# ------------------------------------------------------ 13 · WHAT THEY WON
content_text('What the miners won',
             ['A 10 percent raise',
              'A nine-hour day',
              'No formal recognition of their union',
              'A president as referee, not as capital\u2019s agent'],
             "The arbitration settlement gave the miners a 10 percent raise and a nine-hour day, real gains that students should record exactly, since the guided notes ask for both. What the miners did not win matters just as much: formal recognition of their union. The owners never had to concede that the union spoke for the men, and that question stayed open in American labor law for another generation. The episode gave the Square Deal its meaning, in the reading's phrase: the president had acted as a referee between capital and labor rather than as capital's agent, and both sides left with part of what they wanted. Labor leaders noticed. So did every corporation that might face the next dispute, which is the point of the exit ticket's second question: the strike belongs in a lesson about the presidency because it reset what every later president would be expected to do when a strike threatened the public.",
             kick='The coal strike')

# ------------------------------------------------- 14 · SECTION D DIVIDER
divider_photo('stockyards-port.jpg', 'Side two', 'Protecting the Consumer',
              ['The fight began with a novel',
               'Armour\u2019s Chicago plant: the industry on trial'],
              "The image is Armour and Company's Chicago packing plant, billed as the largest in the world, and it anchors side two of the Square Deal, protecting the consumer. The chain of events here runs from Lesson 2, and students should feel the connection click: the muckrakers exposed, the public reacted, and now a president converts exposure into law. The exposer this time is a novelist. Upton Sinclair wrote The Jungle to indict the wage slavery of the packinghouse workers, and instead his descriptions of what went into the sausage made the whole country queasy about its dinner. Sinclair later joked that he aimed at the public's heart and hit it in the stomach. For teaching purposes the accident is the lesson: reform in 1906 moved at the speed of public disgust, and Roosevelt knew how to spend disgust while it lasted.",
              title_size=40)

# ------------------------------------------------------- 15 · THE JUNGLE
content_text('The Jungle reaches Washington',
             ['Upton Sinclair\u2019s novel disgusted the nation in 1906',
              'Its subject was meatpacking; its readers felt it at breakfast',
              'Roosevelt sent his own investigators to check the claims',
              'They confirmed the book'],
             "Tell the story in its exact chain, because reading question three asks students to trace it link by link. First link: Upton Sinclair's The Jungle, published in 1906, disgusted readers with its account of the meatpacking industry, the rats, waste, and worse that allegedly reached the public's table. Second link: public disgust created political pressure that Congress could not comfortably ignore. Third link: Roosevelt, who trusted neither hysteria nor the packers, had the book verified by his own investigators; the guided notes phrase it as Roosevelt's own investigators verifying the claims, and their report confirmed the worst of it. Fourth link: armed with verified evidence, Roosevelt pushed Congress to act, and Congress passed two laws in a single year. The pattern is the Bureau of Corporations method again, this time with a novel doing the investigating in public. Facts gathered, then law. Students who can narrate all four links in order have answered the reading question before they ever see it.",
             kick='Side two · Consumers')

# -------------------------------------------------------- 16 · TWO LAWS
content_text('Two laws in one year',
             ['Meat Inspection Act: federal inspection of meat crossing state lines',
              'Pure Food and Drug Act: no impure or falsely labeled food and drugs',
              'Both became law in 1906',
              'A permanent inspector between the producer and the public'],
             "Name both laws precisely; the guided notes test the pair and the year. The Meat Inspection Act required federal inspection of meat crossing state lines, putting government inspectors inside the packing plants rather than relying on the companies to police themselves. The Pure Food and Drug Act banned impure and falsely labeled food and drugs, attacking the era's patent medicines and doctored products as well as its sausage. Both became law in 1906. The reading's summary line deserves emphasis: both laws put a permanent federal inspector between the producer and the public's table. Permanent is the operative word. A scandal produces a headline; an inspectorate produces a routine, and routines outlast headlines. When students reach reading question five, which side of the Square Deal reaches furthest into American life today, consumer protection makes a strong case precisely here: federal food and drug inspection is now so assumed that most students have never thought about it at all.",
             kick='Side two · Consumers')

# ------------------------------------------------- 17 · SECTION E DIVIDER
divider_photo('forest-port.jpg', 'Side three', 'Conservation',
              ['The Grizzly Giant, Mariposa Grove',
               'Use the land so that the land lasts'],
              "The photograph is Carleton Watkins's 1861 view of the Grizzly Giant in the Mariposa Grove, with a man standing at its base for scale. It was forty years old when Roosevelt took office, which makes its own point: Americans had been photographing wonders like this for decades while cutting, burning, and fencing the estate around them. Side three of the Square Deal is conservation, and it is the side where Roosevelt's record is least arguable. The totals, which get their own slide shortly, remain the largest in presidential history. But teach the definition before the totals, because the era's argument was about what conservation meant. Roosevelt's people said managed use under experts. John Muir, the president's Yosemite camping companion from the title slide, said some places should be left entirely alone. Both men claimed the same word, and the argument between use and preservation runs through American land policy still.",
              title_size=44)

# -------------------------------------------------------- 18 · WISE USE
content_photo('pinchot-port.jpg', 'Wise use, expert hands',
              ['Gifford Pinchot, Roosevelt\u2019s chief forester',
               'Conservation meant managed use, not locked gates',
               'Timber cut under rules; grazing regulated',
               'Rivers dammed for irrigation: the Newlands Act, 1902'],
              "The portrait is Gifford Pinchot, Roosevelt's chief forester and the man who gave conservation its working definition, which students must have exactly as the guided notes state it: conservation is the managed, expert-supervised use of natural resources so they last. Every word of that definition is a position. Managed, not abandoned. Expert-supervised, because Pinchot believed trained foresters and engineers, not speculators and not sentiment, should run the estate. Use, because the resources were meant to be used: timber could be cut under rules, grazing regulated, and rivers dammed for irrigation under the Newlands Reclamation Act of 1902. So they last, because the point of management was permanence, the greatest good for the greatest number for the longest time, in Pinchot's famous formula. Reading question four asks students to support the managed-use claim with two facts, and the answer key takes timber cut under federal rules and irrigation dams as the pair. Make sure students can produce both before the lesson ends.",
              kick='Side three · Conservation')

# --------------------------------------------------------- 19 · 230 MILLION
stat('230 MILLION', 'acres of public land set aside by Roosevelt',
     '150 national forests, five national parks, and 51 federal bird reservations. The largest conservation record of any president.',
     "Give the totals their own moment, because scale is the argument. Roosevelt set aside about 230 million acres of public land. Students have no intuition for an acre total that size, so translate it: 230 million acres is about 360,000 square miles, an area larger than Texas and Oklahoma put together, placed under federal protection or management in under eight years. The parts are in the guided notes and all three are testable: 150 national forests, five national parks, and 51 federal bird reservations. The bird reservations are the quiet innovation in the list. Pelican Island in Florida, the first of them, protected a rookery of a few acres, proof that the new machinery could work at the scale of one island as well as one forest. The totals remain the largest in presidential history, which is why conservation is the side of the Square Deal that even Roosevelt's critics usually concede.",
     kick='Side three · Conservation')

# ---------------------------------------------------- 20 · ANTIQUITIES ACT
content_text('The Antiquities Act, 1906',
             ['The president could protect landmarks as national monuments',
              'No vote in Congress required',
              'Used 18 times; the first was Devils Tower, Wyoming',
              'Muir wanted some places left entirely untouched'],
             "The last tool in the conservation kit is one of the five vocabulary terms, so give the definition in full: the Antiquities Act (1906) is the law letting the president protect landmarks as national monuments without Congress. Roosevelt used it 18 times, beginning with Devils Tower in Wyoming, and the guided notes test both the number of monuments and the first one. The without Congress clause is the significance and also the controversy. Monument designation is the steward theory with a pen: one signature, no debate, instant protection, which is why presidents still reach for it and why Congress periodically tries to take it back. It is also where the Muir argument returns. Preservationists such as John Muir wanted some places left entirely untouched, and a monument could serve preservation as readily as use, locking a canyon away rather than managing it. Students meet this tension again in today's activity, where four of the ten mapped sites are monuments Roosevelt created alone.",
             kick='Side three · Conservation')

# --------------------------------------------------- 21 · WHAT HE CHANGED
content_text('What Roosevelt changed',
             ['Washington now inspected food and supervised railroads',
              'It sued trusts and arbitrated strikes',
              'It managed a continental estate of public land',
              'Every president since has sat in the referee\u2019s chair'],
             "Close the content where the reading closes, with the expectation Roosevelt permanently changed. He left office in 1909 having altered what Americans expected a president to do. The federal government now inspected food, supervised railroads, sued trusts, arbitrated strikes, and managed a continental estate of public land, none of which had been normal presidential business in 1900. The reading's image is the one to leave with students: the referee's chair Roosevelt built at the center of economic life has been occupied by every president since. Two honest qualifications keep the summary from becoming a celebration, and strong students should hear both. The Square Deal did not settle the argument about how far federal power should reach; that argument resumes in Lesson 5, inside Roosevelt's own party. And it left some Americans almost entirely out, a failure Lesson 8 examines in full. A program can be transformative and incomplete at the same time, and holding both judgments is the habit this unit keeps training.",
             kick='The legacy')

# ------------------------------------------------------------- 22 · VOCAB A
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

vocab('Words for the program',
      [('Square Deal', "Roosevelt's program of corporate control, consumer protection, and conservation"),
       ('arbitration', 'settling a dispute through a neutral third party whose decision both sides accept'),
       ('Hepburn Act (1906)', 'law giving the Interstate Commerce Commission power to set maximum railroad rates')],
      "These definitions match the guided notes word for word, so students can copy them directly. Square Deal: Roosevelt's program of corporate control, consumer protection, and conservation. The name itself was a promise about fairness, a square deal being the honest bargain a referee owes both sides, and Roosevelt used it as the umbrella for everything in this lesson. Arbitration: settling a dispute through a neutral third party whose decision both sides accept. Students met the practice before the term, in the coal strike, where arbitration was the thing the owners refused and the thing Roosevelt's threat finally forced on them. Hepburn Act (1906): law giving the Interstate Commerce Commission power to set maximum railroad rates. The detail that separates strong answers from weak ones is that the commission already existed; the act's contribution was power, the authority to set a maximum rate that railroads actually had to obey. The unit test's matching section draws on these definitions nearly verbatim.")

# ------------------------------------------------------------- 23 · VOCAB B
vocab('Words for the land',
      [('conservation', 'the managed, expert-supervised use of natural resources so they last'),
       ('Antiquities Act (1906)', 'law letting the president protect landmarks as national monuments without Congress')],
      "Two more terms, again matching the guided notes exactly. Conservation: the managed, expert-supervised use of natural resources so they last. Drill the contrast one final time, because the reading and the activity both turn on it: Pinchot's conservation is a working landscape, timber cut under rules and rivers dammed under plans, which is a different idea from preservation, Muir's untouched wilderness. Students who use the words interchangeably will miss the argument the whole side of the lesson is having. Antiquities Act (1906): law letting the president protect landmarks as national monuments without Congress. The without Congress ending is the part students forget and the part that matters; it is what turned the act into a standing presidential power, used by Roosevelt 18 times and by his successors ever since, most often exactly when Congress would not act. With these two terms the lesson's five key terms are complete, and every one of them appeared inside its own section before arriving on these slides.")

# --------------------------------------------------------- 24 · TODAY'S WORK
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Conservation Map Work', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['The Land Roosevelt Saved. Plot ten protected places on the outline map, each by number and category code.'],
     size=23, color=POWDER, leading=1.3)
rows = [('The map', 'Ten sites, 1902 to 1909, Pelican Island to Mount Olympus'),
        ('The codes', 'NF forest · NP park · NM monument · BR bird · GP game'),
        ('Part 2', 'Why the West, why one Florida island, Pinchot or Muir')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=19, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.8, 11.5, 0.5, 'Exit ticket: the three sides with one action each, the coal strike as a presidency story, and a verdict on the nickname trust-buster.',
     size=16, color=POWDER)
notes(s, "Close by handing the lesson to the activity, Conservation Map Work: The Land Roosevelt Saved. Students plot ten places Roosevelt protected between 1902 and 1909, writing each site's number inside the correct state with its category code beside it: NF national forest, NP national park, NM national monument, BR bird reservation, GP game preserve. The list runs from Pelican Island, the first bird reservation, to Mount Olympus, and four of the ten are monuments, the category Roosevelt could create alone. Part 2 asks students to read the pattern the map reveals: eight of the ten sites sit west of the Mississippi, because the federal government still owned most western land in 1900, and to weigh Pinchot's conservation against Muir's preservation. Before they leave, the exit ticket from the guided notes: name the three sides of the Square Deal with one action on each; explain why the coal strike belongs in a lesson about the presidency; and rule on whether trust-buster is the wrong nickname for Roosevelt, defended in two sentences. Next lesson, Taft inherits all of this and the Republican Party splits over it.")

dc.save(OUT)
