#!/usr/bin/env python3
"""Lesson 2 deck, "The Muckrakers," built to the approved Lesson 1 system:
image-led slides, fragments only on screen, comprehensive speaker notes,
full lesson + vocabulary coverage. Fonts: Georgia titles, Lato body."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags, photo_right,
                         divider_photo, content_photo, content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED, W, H)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

HERE = os.path.dirname(os.path.abspath(__file__))
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

# ---------------------------------------------------------------- 1 · TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'PROGRESSIVE ERA · LESSON 2', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Muckrakers', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'How a handful of writers made the whole country look at what it had been avoiding', size=17, color=POWDER)
notes(s, "Lesson 1 ended with five roots of reform, and the press was one of them. This lesson is that root in full. The photograph shows the press room of the New York Herald in about 1902: rows of presses turning out a metropolitan daily. Behind every exposé in this lesson stood machinery like this, plus a new kind of magazine that could carry an investigation to hundreds of thousands of readers at once. Frame the day plainly. A group of writers, most of them working for a few New York magazines, took the four problems from Lesson 1 and documented them so specifically that ignoring them became a political choice. Students should leave able to match each major writer to a target, explain why the magazine business made the work possible, and judge both the power and the limits of exposure as a strategy for reform.")

# ------------------------------------------------- 2 · ESSENTIAL QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did journalists turn exposure into reform?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did Americans respond to the problems created by industrialization, urbanization, and political corruption?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question is the narrower one on the slide, and the unit question runs beneath it as the frame. This lesson answers that unit question as directly as any in the unit. Of all the responses Americans made to the problems of industrial life, the first and most necessary was exposure: before laws could change, someone had to make the problems undeniable to people who did not live with them. A coal miner did not need a magazine to tell him the mines were dangerous. A middle-class reader in Ohio did. Keep the question visible, and return to its wording at the end of class. The muckrakers responded with evidence rather than argument, and their response created the public opinion that later reforms in this unit, from the food laws to the Seventeenth Amendment, depended on. Students will test that claim at the exit ticket, where they judge whether the evidence, the target, or the timing made one exposé effective.")

# --------------------------------------------------- 3 · THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.3, 11.5, 1.0, 'One strategy: exposure', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.42)
rows = [('A', 'The name', 'an insult from a president, worn as a badge of honor'),
        ('B', 'The magazines', 'ten cents a copy, and advertising paid for the reporting'),
        ('C', 'The exposés', 'Tarbell, Steffens, Sinclair, Phillips, and the models behind them'),
        ('D', 'Why it worked', 'voting readers, documented evidence, a national audience'),
        ('E', 'The limits', 'fatigue, sensation, exaggeration, and a world war')]
yy = 2.82
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.7, n, size=26, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.03, 2.9, 0.7, t, size=23, color=CREAM, bold=True)
    text(s, 4.65, yy + 0.08, 7.8, 0.7, d, size=18, color=POWDER)
    yy += 0.9
notes(s, "This is the map of the lesson, and it follows the guided notes section by section. A name came first, because the writers got their identity from a presidential insult they chose to wear proudly. Then the delivery system: cheap, advertising-funded magazines that could pay for months of investigation. Then the exposés themselves, the heart of the lesson, five documented attacks on Standard Oil, city corruption, the meat industry, and the United States Senate, with two earlier models behind them. Then the analytical question students must be able to answer: why did exposure work when the problems had been visible for decades? Finally the limits, because the muckraking era faded even as its laws endured. Tell students the exit ticket draws on sections C and D, so names, targets, and reasons need to land today, not in review.")

# ------------------------------------------------- 4 · SECTION A DIVIDER
divider_photo('roosevelt-port.jpg', 'Section A', 'The Name',
              ['How an insult from a president', 'became a badge of honor'],
              "The photograph is Theodore Roosevelt, photographed by the Pach brothers. Every student knows Roosevelt as the trust-busting president, which is exactly why this section surprises them: the name muckraker came from Roosevelt himself, and he meant it as a criticism. In April 1906, at the laying of a cornerstone for a House office building in Washington, Roosevelt paused in his speech to attack journalists who, in his view, did nothing but hunt for filth. His target was real. Some of the new magazine writing had turned reckless, and Roosevelt feared that indiscriminate attacks on public men would teach Americans to distrust everyone and reform nothing. The speech is the subject of the next slide. The point to set here is that the most famous label in American journalism began as a warning from the most powerful man in the country, and the writers adopted it anyway.",
              title_size=54)

# ------------------------------------------------------ 5 · THE INSULT
content_text('An insult from the president',
             ['April 1906: Roosevelt attacks the filth-hunters',
              'His image came from Pilgrim\u2019s Progress, Bunyan\u2019s allegory',
              'The man with the muck-rake raked filth and never looked up',
              'The warning: rake only, and the country stops believing anyone'],
             "Give students the scene precisely, because the guided notes test it in three blanks. In April 1906, President Theodore Roosevelt compared critical journalists to a character in Pilgrim's Progress, John Bunyan's allegory: the man with the muck-rake, who raked up filth from the floor and could not be persuaded to look up at anything higher. In Bunyan's story the figure ignores a celestial crown held out to him because he cannot stop raking. Roosevelt's point was about proportion. Exposure had its place, he said, but a writer who only raked, who attacked the honest and the corrupt alike, would corrode the public's faith in every institution. Historians note that he had specific targets in mind, including David Graham Phillips's series on the Senate, which students meet later in this lesson. The speech backfired as criticism and succeeded as naming. Within months the word muckraker was everywhere, attached to a movement rather than a complaint.",
             kick='A · The name')

# ------------------------------------------------------ 6 · BADGE OF HONOR
content_text('Worn as a badge of honor',
             ['The writers took the insult as a badge of honor',
              'Their method: dig up the dirt and document it',
              'Pile it where everyone could see it',
              'Reform needed votes, and votes needed angry readers'],
             "Ask students why a writer would accept an insult as a professional name, because the guided notes ask for the method in one line. The writers accepted muckraker because it described their method accurately and turned the insult into a public identity: dig into the dirt of American life, pile it where everyone could see it, and make looking away impossible. The name was also honest advertising. A reader picking up McClure's knew exactly what kind of writing was inside. Then connect the name backward to Lesson 1. That lesson described four problems: work, the city, corruption, and corporate power. Problems alone changed nothing for decades. Reform laws needed votes, and votes needed readers who were angry, and the muckrakers supplied the anger one documented fact at a time. That sentence is the thesis of this lesson, and students will spend the rest of the hour watching it operate on specific targets.",
             kick='A · The name')

# ------------------------------------------------- 7 · SECTION B DIVIDER
divider_photo('mcclures-port.jpg', 'Section B', 'The Magazine Revolution',
              ['The delivery system that made', 'exposure a national force'],
              "The cover is McClure's Magazine from December 1901, months before the magazine changed American journalism. Exposure needed a delivery system, and this section explains the one the muckrakers used. A magazine cover rather than a person fills the screen on purpose: the hero of this section is a business model. In the 1890s a new kind of magazine appeared, cheap, national, and fat with advertising, and it reached readers on a scale no reform pamphlet or newspaper editorial ever had. S. S. McClure founded his magazine in 1893 and cut its price when the economics of advertising allowed it. What matters for students is causation, not nostalgia. The investigations in section C were expensive, slow, and risky, and they happened because a magazine's balance sheet could carry them. Keep that causal chain in view all hour.",
              title_size=44)

# ------------------------------------------------------ 8 · CHEAP MAGAZINES
content_text('Cheap magazines, national reach',
             ['McClure\u2019s cut its price to ten or fifteen cents',
              'Printed on inexpensive paper, sold everywhere',
              'National advertising, not subscriptions, paid the bills',
              'Circulation climbed into the hundreds of thousands'],
             "Walk the arithmetic slowly, because question two of the reading turns on it. In the 1890s, magazines such as McClure's cut their price to ten or fifteen cents, printed on inexpensive paper, and paid their bills with national advertising instead of subscriptions alone. Circulation climbed into the hundreds of thousands. Each element reinforced the others. A ten-cent price put the magazine within reach of a clerk or a schoolteacher. National brands, selling soap and breakfast food to the whole country, paid for access to those readers. Advertising revenue, not the cover price, became the profit. That arithmetic mattered to journalism. A magazine earning money from half a million readers could pay a writer to spend months, even years, on one investigation, and could survive the anger of any single advertiser or target. The exposé was, among other things, a product that only this business model could manufacture.",
             kick='B · The magazine revolution')

# ------------------------------------------------------ 9 · TEN CENTS STAT
stat('10 CENTS', 'the price of McClure\u2019s after the magazine price cut',
     'Advertising paid the bills, and advertising paid for the investigations: months or years of one writer\u2019s time on a single subject.',
     "Dwell on the number, because it explains the era. Ten cents was cheap enough to be an impulse purchase at a newsstand, and the price was possible only because the reader was not the magazine's only customer. Advertisers were buying the reader's attention, and the more readers a magazine gathered, the more that attention was worth. McClure's great rival Munsey's had shown the way in 1893 by cutting to ten cents and watching circulation explode. The editorial consequence is the part students must carry forward. An investigation like Ida Tarbell's history of Standard Oil took two years, with travel, research help, and legal risk. No subscription-funded monthly of the old kind, selling to thirty thousand gentle readers at thirty-five cents, could have carried it. When students ask why muckraking happened when it did, the first answer is not courage. It is this price.",
     kick='B · The magazine revolution')

# ------------------------------------------------------ 10 · NOVEMBER 1902
content_text('One issue, three investigations',
             ['November 1902: a single run of McClure\u2019s',
              'Tarbell on Standard Oil',
              'Steffens on corruption in St. Louis',
              'Baker on the railroads',
              'Readers saw one pattern, not three scandals'],
             "The result of the new economics arrived in November 1902, when McClure's carried Ida Tarbell's history of Standard Oil, Lincoln Steffens on corruption in St. Louis, and Ray Stannard Baker on railroads in the same run of issues. The editor, S. S. McClure, had assembled three investigations at once, and the combination was the message. A reader could dismiss one corrupt city as bad luck, or one monopoly as one company's greed. Three documented investigations, running side by side, showed readers that the corruption in one city and the monopoly in one industry were parts of a single pattern: concentrated private power, buying public power, in city after city and industry after industry. Later historians sometimes call that November issue the moment muckraking announced itself. For this class it is the bridge into section C. We now take the exposés one at a time, and students should track each writer's target and result in their notes, because the exit ticket tests the matching.",
             kick='B · The magazine revolution')

# ------------------------------------------------- 11 · SECTION C DIVIDER
divider_photo('tarbell-port.jpg', 'Section C', 'The Exposés',
              ['Five documented attacks,', 'and the two models behind them'],
              "The portrait is Ida Tarbell, the most respected of the muckrakers and the writer whose work opens this section. From here the lesson becomes a sequence of cases, and students need a consistent set of questions for each one. Who was the writer? What was the target? What evidence did the writer gather? What followed? The reading gives five exposés that moved the country: Tarbell on Standard Oil, Steffens on the cities, Sinclair on the meatpackers, and Phillips on the Senate, with two earlier models, Riis and Addams, who had shown the method before the magazines existed. Warn students against treating these as five separate stories. Each exposé taught the next writer something about evidence and audience, and each result, a breakup, a book, two laws, an amendment campaign, raised the pressure the others worked under. Exposure was becoming an industry of its own.",
              title_size=54)

# ------------------------------------------------------ 12 · TARBELL
content_text('Ida Tarbell and Standard Oil',
             ['Her father, an independent oil man, was ruined by Rockefeller\u2019s combination',
              'The History of the Standard Oil Company, McClure\u2019s, 1902 to 1904',
              'Built from court records and interviews, not memory',
              'Rebates, espionage, and coerced buyouts, documented',
              '1911: the Supreme Court ordered the trust broken up'],
             "Tarbell's father had been an independent oil man ruined by Rockefeller's combination, but her History of the Standard Oil Company, serialized in McClure's from 1902 to 1904, was not a memoir. Stress that word, serialized: the work appeared in installments over many issues, building an audience the way a serial novel did, except that every chapter was documented. It was a documented account of rebates, espionage, and coerced buyouts, built from court records and interviews. She showed how Standard Oil took secret rebates from railroads, spied on competitors, and forced independent refiners to sell or be crushed. Rockefeller, who rarely answered critics, found the series impossible to ignore. In 1911 the Supreme Court ordered Standard Oil broken into separate companies. Students should not credit Tarbell alone for the ruling; the government brought the case. But her two years of reporting had made the trust's methods common knowledge, and common knowledge is what makes a court ruling politically possible.",
             kick='C · The exposés', size=24)

# ------------------------------------------------------ 13 · STEFFENS
content_photo('steffens-port.jpg', 'Lincoln Steffens and the cities',
              ['City after city, the same discovery',
               'Corruption was a system, not a few bad men',
               'Businessmen paid the bribes; officials took them',
               'The Shame of the Cities, 1904'],
              "The photograph is Lincoln Steffens, who had been a police reporter in New York before McClure's sent him out to the cities. Steffens traveled from city to city and showed that corruption was not a few bad men but a system linking businessmen who paid bribes and officials who took them. That distinction is the intellectual core of his work, and it is the point the guided notes isolate. In St. Louis, Minneapolis, Pittsburgh, and Philadelphia, the names changed and the machinery did not: a businessman wanted a franchise or a contract, an official wanted money or advancement, and the respectable citizens who deplored corruption kept electing the officials and buying from the businessmen. His articles, collected as The Shame of the Cities in 1904, made readers in honest-looking cities ask who was buying their own government. Steffens was implicating his readers, and he knew it. That is a more unsettling, and more durable, argument than any single scandal.",
              kick='C · The exposés')

# ------------------------------------------------------ 14 · SINCLAIR
content_photo('sinclair-port.jpg', 'Upton Sinclair and The Jungle',
              ['Seven weeks inside Chicago\u2019s Packingtown',
               'The Jungle, 1906: a novel of the meat industry',
               'He aimed at the public\u2019s heart and hit its stomach',
               'Readers demanded clean food, not justice for packers'],
              "The photograph is Upton Sinclair, who was twenty-seven when he went to Chicago. Sinclair spent seven weeks in Chicago's Packingtown and wrote The Jungle in 1906, a novel about an immigrant family destroyed by the meat industry. He wanted readers to demand justice for workers: the speed, the injuries, the wages that could not feed a family. Instead they fixated on the filth going into their food: rats, spoiled meat, and worse, ground into sausage. Sinclair later said he had aimed at the public's heart and hit its stomach instead. The line is funny and bitter at once, and students should sit with the bitterness. The exposé worked, but on the audience's terms, not the author's. A reformer can document a harm perfectly and still be answered only where the readers' own interests are touched. The next slide shows what the stomach produced: within months, two federal laws.",
              kick='C · The exposés')

# ------------------------------------------------------ 15 · TWO LAWS
content_text('Two laws in a single year',
             ['1906: the Meat Inspection Act',
              '1906: the Pure Food and Drug Act',
              'Federal inspectors inside the packing plants',
              'The stomach moved Congress faster than the heart'],
             "Within months of The Jungle's publication, Congress passed the Meat Inspection Act and the Pure Food and Drug Act, both in 1906. Roosevelt, who had read the novel and sent his own investigators to Chicago, pressed Congress when the meatpackers' lobby resisted, and the investigators confirmed the worst of Sinclair's account. The inspection act put federal inspectors inside packing plants and made the government, not the packer, responsible for the stamp on the meat. The pure food act attacked mislabeled and adulterated products and patent medicines across the whole food and drug market. Note the lesson inside the result before moving to section D. These are the fastest, most concrete laws any exposé in this lesson produced, and they regulated what readers ate rather than how workers lived. Exposure worked best when the documented harm landed on the reader's own table. Students will weigh that fact when they judge the strategy's limits.",
             kick='C · The exposés')

# ------------------------------------------------------ 16 · PHILLIPS
content_text('David Graham Phillips and the Senate',
             ['\u201cThe Treason of the Senate,\u201d 1906',
              'Named individual senators and their corporate ties',
              'Legislatures chose senators, so voters could not remove them',
              'The series fed the drive for direct election',
              '1913: the Seventeenth Amendment'],
             "David Graham Phillips wrote the most politically explosive series of the era, and one of the works that had provoked Roosevelt's muck-rake speech. His 1906 series, The Treason of the Senate, named individual senators and documented their ties to railroads and corporations. The charge in the title was deliberate: a senator serving a railroad while drawing a public salary was, in Phillips's framing, committing treason against the republic. The structural problem underneath the scandal is what students must retain. Because state legislatures chose senators, voters could not remove them directly, however corrupt the arrangement became. A senator bought by corporate money answered to a legislature that the same money also influenced. The series fed the campaign for direct election that produced the Seventeenth Amendment in 1913, which transferred the choice to voters themselves. Phillips is the clearest case in the lesson of an exposé aiming past a scandal at a rule of the system, and changing the rule.",
             kick='C · The exposés', size=24)

# ------------------------------------------------------ 17 · THE MODELS
content_photo('riis-port.jpg', 'The models: Riis and Addams',
              ['Riis, 1890: photography exposes the tenements',
               'Addams: reporting from inside Hull House',
               'Exposure as reporting plus residence',
               'Stay, document, publish'],
              "The muckrakers had models, and students met the first one in Lesson 1. Jacob Riis's How the Other Half Lives, from 1890, had already shown photography's power to expose: the camera carried evidence that a written description could be accused of inventing. The photograph here is Riis himself, about 1906. Jane Addams worked differently. She wrote from inside the problem, reporting on Chicago's poor from Hull House, the settlement house she ran, in Twenty Years at Hull-House in 1910. Her authority came from residence: she lived in the neighborhood she described, for decades. Exposure, in their hands, was reporting plus residence: stay, document, publish. The distinction matters for the rest of the unit. The magazine muckrakers visited their subjects for weeks or months. Addams's model, living inside the problem and building an institution there, produced a different kind of reformer, and her network of settlement workers carried Progressive ideas into statehouses and, eventually, into the suffrage fight of Lesson 7.",
              kick='C · The exposés')

# ------------------------------------------------- 18 · SECTION D DIVIDER
divider_text('Section D', 'Why Exposure Worked',
             'The problems had been visible for decades. The reading gives three reasons the exposure finally moved the country.',
             "Pause here and make students do the analysis rather than receive it. By 1902, nothing in this lesson's exposés was new in kind: tenements had been lethal for a generation, Standard Oil's methods were an open secret in the oil regions, and city graft was a music-hall joke. Yet within a decade the country had a broken trust, federal food laws, and a constitutional amendment in motion. Section D of the guided notes asks for the three reasons from the reading, and the next slide takes them in order: the readers, the evidence, and the scale of the audience. Push students to see that the three reasons are really one system. A national magazine put specific, documented evidence in front of the exact class of people whose votes and letters politicians feared. Remove any leg and the strategy wobbles, which is why section E, the limits, follows logically rather than as an afterthought.")

# ------------------------------------------------------ 19 · THREE REASONS
content_text('Three reasons it worked',
             ['The readers voted, organized, and wrote letters',
              'The evidence was specific: names, documents, counted deaths',
              'The audience was national, so Chicago pressured Washington'],
             "Take the three reasons in order and tie each to a case students already know. First, the readers were the growing professional middle class, people who voted, organized, and wrote letters: exposure landed on citizens with political weight, not on the powerless alone. Second, the evidence was specific: named companies, dated documents, counted deaths, which made denial difficult. Tarbell could be argued with, but her railroad rebates were in the court record. Third, the audience was national, so a scandal in Chicago created pressure in Washington; a St. Louis reader and a Boston reader finished Steffens angry about the same system in the same week. Together the three reasons describe a machine for converting information into public opinion, and public opinion, as the vocabulary slide will define it, is the views of the general public, which elected officials ignore at their risk. That conversion is the muckrakers' permanent contribution to American politics.",
             kick='D · Why exposure worked')

# ------------------------------------------------- 20 · SECTION E DIVIDER
divider_text('Section E', 'The Limits',
             'The era faded within a decade. The laws it produced did not.',
             "End the survey honestly, because students should learn to evaluate a strategy, not just admire it. Muckraking blazed from about 1902 to about 1912, and by the time war came in Europe in 1914 the magazines and their readers had moved on. The reading names the causes, and the next slide lists them: fatigue, competition from sensation, exaggeration, and the war. But set the frame before the list. A strategy can fade for reasons that have little to do with whether it worked. The exposés had changed what Americans expected government to do, permanently, and the agencies, laws, and amendments they produced outlived the magazines that provoked them. The fair judgment is that exposure was a beginning and not a complete politics: it could force a problem onto the agenda, and it could not by itself write the law, staff the agency, or defend either for fifty years.")

# ------------------------------------------------------ 21 · WHY IT FADED
content_text('Why the era faded',
             ['Readers tired of outrage',
              'Cheaper magazines sold sensation instead of evidence',
              'Some writers exaggerated, and targets dismissed them all',
              'After 1914, a European war took the country\u2019s attention',
              'What stayed: the laws, agencies, and amendments'],
             "The strategy had limits, and students need two of them for section E of the guided notes; any two earn the point. Readers tired of outrage: indignation is a depleting resource, and a magazine that must shock monthly eventually shocks less. Cheaper magazines competed with sensation rather than evidence, undercutting the expensive reporting that made McClure's credible. Some muckrakers drifted into exaggeration, which let their targets dismiss all of them, the careful with the careless. And by the time war came in Europe in 1914, the magazines and their readers had moved on. Then insist on the counterweight. The laws, agencies, and amendments the exposés produced stayed, and the method, document the harm, name the responsible party, demand a specific fix, remains the template for investigative reporting. When a modern student sees an investigation change a law, the choreography was invented in these years, by these writers, in these magazines.",
             kick='E · The limits', size=24)

# ------------------------------------------------------ 22 · VOCAB A
vocab('Words for the work',
      [('muckraker', 'a journalist who investigated and exposed corruption, dangerous conditions, and corporate wrongdoing'),
       ('exposé', 'a published report that reveals wrongdoing the public did not know about'),
       ('mass-circulation magazine', 'a magazine sold cheaply to hundreds of thousands of readers and funded largely by advertising')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test's matching section draws on them. A muckraker is a journalist who investigated and exposed corruption, dangerous conditions, and corporate wrongdoing. Note the active verbs: investigated and exposed. The muckraker was not a commentator with opinions about the news; the work was original reporting, documents gathered and witnesses interviewed, often over months. An exposé is a published report that reveals wrongdoing the public did not know about. The word is French, and its key element is the revelation: an exposé fails if the public already knew, which is why muckrakers guarded their findings until publication day. A mass-circulation magazine is a magazine sold cheaply to hundreds of thousands of readers and funded largely by advertising. Students have already seen why that definition is really the era's engine: cheapness created the audience, and advertising paid for the work.")

# ------------------------------------------------------ 23 · VOCAB B
vocab('Words for the form and the force',
      [('serialized', 'published in installments over many issues'),
       ('public opinion', 'the views of the general public, which elected officials ignore at their risk')],
      "Two more terms, again matching the guided notes exactly. Serialized means published in installments over many issues. Tarbell's history of Standard Oil ran that way for two years, and serialization was a strategy, not a convenience: each installment renewed the pressure, gave targets no single week in which to kill the story, and let readers follow an investigation the way they followed a serialized novel, except that the villain was a real company and the documents were real. Public opinion is the views of the general public, which elected officials ignore at their risk. That definition is the lesson in miniature. The muckrakers manufactured nothing except attention. They converted private knowledge into public opinion, and public opinion converted politicians. When students use the term later in the unit, for suffrage or for Wilson, hold them to this definition: not what everyone thinks in the abstract, but the expressed views of voters that a politician disregards at personal cost.")

# ------------------------------------------------------ 24 · TODAY'S WORK
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Be a Muckraker', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Write your own exposé. Lead with the harm, support every claim with evidence, and end with one specific demand.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Part 1', 'Test your target: hurt, responsibility, evidence'),
        ('Part 2', 'Gather the evidence: three pieces, and the other side'),
        ('Part 3', 'Write the exposé: the harm, the proof, one demand')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.5, 0.6, d, size=19, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.8, 11.5, 0.5, 'Exit ticket: match each writer to a target, explain the magazine model, and defend one exposé.',
     size=16, color=POWDER)
notes(s, "Close by handing the lesson to the activity, Be a Muckraker: write your own exposé. It follows the lesson's method in three parts. Part 1 tests the target: someone is hurt, someone is responsible, and evidence exists. Approve targets at the end of Part 1, before evidence gathering begins, and reject gossip about named students or staff; the right scale is public problems: facilities, policies, local businesses, national industries. Part 2 gathers three pieces of evidence, each with a source, and requires students to state the other side's defense fairly and answer it before writing. Part 3 writes the exposé: a headline, an opening that leads with the harm, evidence in order of strength, and a closing with one specific demand addressed to whoever can grant it. Grade against the method, not the polish: document the harm, name the responsible party, demand a specific fix. The exit ticket: match Tarbell, Steffens, and Sinclair to their targets; explain why the magazine business model mattered to reform; and pick one exposé and defend whether its evidence, its target, or its timing made it effective. Next lesson, reform moves from exposure to lawmaking.")

dc.save(OUT)
