#!/usr/bin/env python3
"""Lesson 7 deck: The Fight for Women's Suffrage.
Built on the approved Lesson 1 system via deck_common: image-led slides,
fragments only on screen, comprehensive speaker notes, full lesson and
vocabulary coverage. Fonts: Georgia titles, Lato body."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(HERE, '..', '..')))
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags, photo_right,
                         divider_photo, content_photo, content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED)
from pptx.util import Inches

dc.IMG = os.path.join(HERE, 'img')
prs = dc.prs
W = 13.333
OUT = os.path.normpath(os.path.join(HERE, '..', 'lesson-07-slides.pptx'))

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
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, prs.slide_width, prs.slide_height)
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'PROGRESSIVE ERA · LESSON 7', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Fight for Women\u2019s Suffrage', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Seventy-two years from Seneca Falls to the Nineteenth Amendment', size=17, color=POWDER)
notes(s, "This lesson tells the longest story in the unit. The suffrage movement began in 1848, before the Civil War, before the Progressive Era had a name, and it did not finish until 1920. Nearly every other reform in this unit was won in a decade or two; this one took seventy-two years, and the reasons it took so long are the lesson. Frame the day around the unit question printed beneath today's lesson question, on the slide and on their guided notes: How did Americans respond to the problems created by industrialization, urbanization, and political corruption? The photograph shows the head of the great suffrage procession in Washington on March 3, 1913, with a herald on a white horse and the lead wagon carrying the movement's demand: an amendment to the Constitution enfranchising the women of this country. Keep that wagon in mind. The whole lesson is an argument about how to reach the sentence on it.")

# ------------------------------------------------- 2 · ESSENTIAL QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('Why did the suffrage movement win in 1920 after seventy years of losing?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did Americans respond to the problems created by industrialization, urbanization, and political corruption?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "The unit question beneath today's lesson question is the same one the class has carried all unit, and this lesson bends it in an instructive way. In earlier lessons the problem was something industrial growth produced: dangerous work, crowded housing, corrupt government. Here the problem is political exclusion itself, the fact that half the adult population could be governed, taxed, and tried without any voice in choosing the government. The response also differs. Nobody handed women the vote as a remedy; women organized for it across three generations, against an opposition that was itself organized and funded. Ask students to hold one question through the hour: the movement agreed completely on the goal for seventy-two years, so why did the fight last that long? The answer the lesson builds is that agreement on a goal is not a strategy, and the movement spent decades arguing about strategy. That argument is what they will judge in the writing task.")

# ------------------------------------------------------------ 3 · STAT 72
stat('72 YEARS', 'from Seneca Falls in 1848 to ratification in 1920',
     'Three generations of organizers worked for one sentence in the Constitution.',
     "Give the span its own moment before any details, because the length of the fight is the first fact of the lesson. Elizabeth Cady Stanton, who wrote the call for suffrage in 1848, died in 1902. Susan B. Anthony, the movement's organizer for half a century, died in 1906. Neither lived to cast a legal vote in a national election. The women who finished the fight, Carrie Chapman Catt and Alice Paul, inherited it the way an institution is inherited: with its arguments already drafted, its organizations already built, and its defeats already catalogued. A useful way to make the span concrete for students: a girl who attended Seneca Falls as a teenager could have watched ratification as a woman of eighty-nine. Movements that survive that long survive because they build structures that outlast their founders, and students should watch for those structures, the associations, the state campaigns, the trained organizers, as the lesson proceeds.",
     kick='A movement older than the era')

# --------------------------------------------------------- 4 · THE ROAD MAP
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.35, 11.5, 1.0, 'One amendment, five acts', size=46, color=CREAM, font='Georgia')
rule(s, 0.92, 2.5)
rows = [('A', 'The Early Movement', 'Seneca Falls, a twenty-year split, and a closed courthouse door'),
        ('B', 'Two Roads', 'win the states one by one, or amend the Constitution'),
        ('C', 'The Opposition', 'organized, funded, and often led by women'),
        ('D', 'The Final Push', 'Catt\u2019s plan and Paul\u2019s pickets, inside and outside'),
        ('E', 'Ratification', 'thirty-six states, decided by one vote in Tennessee')]
yy = 2.95
for n, t, d in rows:
    text(s, 0.9, yy, 0.7, 0.7, n, size=30, color=RUST_LT, font='Georgia')
    text(s, 1.65, yy + 0.04, 3.6, 0.7, t, size=27, color=CREAM, bold=True)
    text(s, 5.35, yy + 0.10, 7.1, 0.7, d, size=20, color=POWDER)
    yy += 1.02
notes(s, "This map matches the reading and the guided notes exactly, section for section, so students can use it as a checklist while they work. Act A is the early movement: the founding at Seneca Falls, the split after the Civil War, and the Supreme Court closing the courthouse door in 1875. Act B is the strategic argument that organized the next forty years, state road against federal road. Act C takes the opposition seriously, its public argument and the money behind it. Act D is the final push of 1913 to 1918, when the two roads were finally run at the same time by two different organizations. Act E is ratification, which came down to a single legislator in Tennessee. Tell students plainly: the exit ticket and the writing task both live in Act B. Everything else in the lesson is evidence for the judgment those two assignments ask them to make.")

# ------------------------------------------------- 5 · SECTION A DIVIDER
divider_photo('stanton-port.jpg', 'Section A', 'The Early Movement',
              ['It began in 1848,', 'decades before the Progressive Era had a name'],
              "The photograph is a daguerreotype of Elizabeth Cady Stanton with her daughter Harriot, from 1856, eight years after Seneca Falls. Stanton is the right face for this section. She was the movement's writer and theorist, the one who put its demands into documents, while Susan B. Anthony became its organizer and traveler. Stanton came to the cause through abolition: at the World Anti-Slavery Convention in London in 1840, women delegates were barred from the floor and made to sit behind a curtain, and she and Lucretia Mott resolved there that women needed a convention of their own. Section A covers three things students must be able to narrate in order: the founding at Seneca Falls in 1848, the movement's split over the Fifteenth Amendment after the Civil War, and the legal defeat of 1875 that closed the courthouse road for good. The section ends with the movement reunited in 1890 and the argument turning from whether women should vote to how the vote could possibly be won.")

# ------------------------------------------------------ 6 · SENECA FALLS
content_photo_s('mott-port.jpg', 'Seneca Falls, 1848',
              ['Stanton and Lucretia Mott called the first women\u2019s rights convention.',
               'The Declaration of Sentiments was modeled on the Declaration of Independence.',
               'Its boldest demand was the vote for women.'],
              "The portrait is Lucretia Mott, painted by Joseph Kyle in 1841. Mott was a Quaker preacher and veteran abolitionist, and her standing gave the young movement a respectability it badly needed. In July 1848 she and Stanton called a convention in Seneca Falls, New York, and about three hundred people came. Stanton drafted the Declaration of Sentiments by taking the Declaration of Independence as her template, grievance for grievance, and changing its most famous sentence to declare that all men and women are created equal. The strategy of that borrowing deserves attention: the movement did not import a foreign idea. It indicted America out of America's own founding text. Of all the resolutions, the demand for the vote was the most controversial, and even some organizers feared it would make the movement ridiculous. Frederick Douglass, attending as an abolitionist ally, spoke for it, and it passed. Every later argument in this lesson is an attempt to make that one resolution real.",
              kick='A · The Early Movement')

# ------------------------------------------------------- 7 · DIVIDED
content_photo_s('anthony-port.jpg', 'A movement divided',
              ['After the Civil War, the movement split over the Fifteenth Amendment.',
               'Anthony and Stanton opposed it because it enfranchised Black men and excluded all women.',
               'Lucy Stone\u2019s wing supported it as one step.',
               'Anthony voted in 1872 and was arrested, tried, and fined $100 she never paid.'],
              "The photograph shows Stanton seated and Anthony standing over a document, the partnership that ran the movement for fifty years. The split came over the Fifteenth Amendment, which barred denying the vote on account of race but said nothing about sex. Anthony and Stanton refused to support an amendment that enfranchised Black men while excluding all women, and they campaigned against it. Lucy Stone's wing supported the amendment as one step and trusted that women's turn would follow. Neither side forgave the other quickly; the movement ran as two rival organizations for twenty years. Anthony also tested the courts directly. In 1872 she persuaded Rochester election officials to register her and cast a ballot in the presidential election. She was arrested, tried, and fined one hundred dollars. She refused to pay, announced she never would, and the government quietly let the matter drop rather than jail her and make her a martyr. The legal theory behind the test, that the Fourteenth Amendment's citizenship already carried the vote, gets its hearing on the next slide.",
              kick='A · The Early Movement')

# ------------------------------------------------------------ 8 · MINOR
content_text('The courts say no',
             ['Minor v. Happersett (1875) held that voting is not a right of citizenship.',
              'The judicial road closed for good.',
              'In 1890 the two wings reunited as NAWSA.',
              'The argument turned from whether to how.'],
             "Virginia Minor of Missouri supplied the test case Anthony's strategy needed. When a registrar refused to register her, she sued, arguing that as a citizen she held a constitutional right to vote. In Minor v. Happersett in 1875 the Supreme Court ruled against her: citizenship did not carry the vote, and the Constitution protected no such right for women. The teacher key puts the consequence in one sentence students should be able to reproduce: no lawsuit could win the vote, so the movement's history after 1875 is a history of campaigns, not cases. Only two roads remained, amending the Constitution or winning state by state, and Act B is the argument between them. The first step toward either was reunion. In 1890 the two wings merged as the National American Woman Suffrage Association, usually shortened to NAWSA, and the movement's internal argument turned from whether women should vote to how the vote could be won. Hold students to that shift, because the writing task asks them to enter the argument at exactly that point.",
             kick='A · The Early Movement')

# ------------------------------------------------- 9 · SECTION B DIVIDER
divider_photo('west-port.jpg', 'Section B', 'Two Roads',
              ['Win state after state across the West,', 'or change the Constitution itself'],
              "The image is a 1916 broadside of the Congressional Union, mapping the route of envoys sent from the East to appeal to the voting women of the West. Read its headline with the class, because it states this section's geography in one line: by 1916, the women of the West could vote, and the women of the East were sending organizers to ask for their help. That map was the product of a strategic choice. The state road argued that suffrage would spread state by state, each win producing women voters, women officeholders' constituents, and proof that the republic survived. The federal road argued that state campaigns would take a century and never reach the South, and that only an amendment settled the question everywhere at once. Notice what the argument was not about. Both roads led to the same destination, and most suffragists supported both at different moments. The argument was about where scarce money, organizers, and years should go, which is what makes it a genuine strategy problem rather than a disagreement over goals.")

# ----------------------------------------------------- 10 · STATE ROAD
content_text('The state road runs through the West',
             ['Wyoming entered the Union with suffrage in 1890 and refused to drop it.',
              'Colorado followed in 1893.',
              'Utah and Idaho followed in 1896.'],
             "Wyoming is the state road's founding exhibit. Wyoming Territory had let women vote as early as 1869, and when statehood came in 1890, Congress pressed Wyoming to drop women's suffrage from its constitution as the price of admission. Wyoming refused, in the era's most quoted telegram on the subject: it would stay out of the Union a hundred years rather than come in without its women voters. It entered with suffrage intact, the first state to do so. Colorado followed in 1893, the first state where male voters approved suffrage by referendum, and Utah and Idaho followed in 1896. Do not let the short list look small. Each win did triple work. It enfranchised that state's women immediately. It created members of Congress who answered to women voters. And it produced evidence, election after election, that women voting changed nothing the antis predicted: families did not dissolve, and politics was not coarsened. The state road's real product was proof, and the federal road would eventually spend that proof in Washington.",
             kick='B · Two Roads')

# ----------------------------------------------------- 11 · WHY WEST
content_text('Why the West, and why it stalled',
             ['Western legislatures had fewer entrenched machines to defend.',
              'Territories wanted settlers, and said so openly.',
              'Populist farmers often backed the cause.',
              'New York voted no in 1915, then yes in 1917, after decades of spending.'],
             "The reading gives three western advantages, and the answer key accepts any two, so make sure students can state all three cleanly. First, western states and territories had weaker, less entrenched political machines, so the organizations that blocked suffrage in the East barely existed. Second, territories wanted settlers, and granting women the vote advertised a territory as a civilized place for families; the argument was demographic, not only moral. Third, Populist and farming constituencies often backed the cause, carrying suffrage into party platforms. Smaller legislatures were also simply cheaper to lobby and persuade. Then show the stall. In the big eastern states the state road ran into strong machines, large populations, and well funded opposition. New York, the movement's richest target, voted no in 1915 despite an enormous campaign, then yes in 1917. Two years and a fortune for one state, with forty-seven to go, is the arithmetic that made the federal road look less hopeless than its critics claimed.",
             kick='B · Two Roads')

# ----------------------------------------------------- 12 · FEDERAL ROAD
content_text('The federal road',
             ['A suffrage amendment first reached Congress in 1878.',
              'The Senate voted it down in 1887, then ignored it for a generation.',
              'An amendment needs two-thirds of Congress and three-fourths of the states.',
              'Only an amendment settles the question everywhere at once.'],
             "The federal road is older than students expect. A women's suffrage amendment was first introduced in Congress in 1878, written in language that would survive nearly unchanged into the Nineteenth Amendment. The Senate debated and voted it down in 1887, and then simply declined to vote again for a generation. The reason critics called the road hopeless is arithmetic, and students should copy the numbers: an amendment needs two-thirds of both houses of Congress and then ratification by three-fourths of the states, the highest bar in American politics, designed to be nearly impassable. The federalists' answer, which the reading states and the writing task tests, is that the difficulty was the point. State-by-state victory would never reach the South or the big eastern states at all, where machines and one-party rule could block referendums indefinitely. One amendment, passed once, settled the question everywhere at once, including in states whose own legislatures would never have conceded it. Ask which logic students find stronger now; they will need a position in the memo.",
             kick='B · Two Roads')

# ------------------------------------------------- 13 · SECTION C DIVIDER
divider_photo('anti-port.jpg', 'Section C', 'The Opposition',
              ['Organized, funded,', 'and often led by women'],
              "The photograph, by Harris and Ewing, shows the headquarters of the National Association Opposed to Woman Suffrage in 1911, with passersby reading the material posted in its windows. Use it to correct the easiest misconception students bring to this lesson: that suffrage was delayed by apathy, or by men in general, or by nobody in particular. The antis were an organization, with headquarters, chapters, newspapers, and lobbyists, and much of their leadership was female, which gave their central claim its force: they said they spoke for the majority of women who did not want the vote. A fight against an organized opponent explains seventy-two years in a way that prejudice alone cannot. This section has two slides. The first takes the antis' public argument seriously, because it was effective and students should be able to state it fairly. The second follows the money behind the argument, and then turns to the harder subject of the suffrage movement's own compromises.")

# ----------------------------------------------------- 14 · ANTIS' CASE
content_text('The antis make their case',
             ['The National Association Opposed to Woman Suffrage was founded in 1911.',
              'Its claim was that most women do not want the vote.',
              'The home is women\u2019s sphere.',
              'Politics would coarsen women without cleansing politics.'],
             "The National Association Opposed to Woman Suffrage, founded in 1911, consolidated state-level anti organizations into a national operation, and its public argument had three parts that the guided notes ask students to recover. First, most women do not want the vote. This was the load-bearing claim, and it was shrewd: it recast suffragists as a loud minority imposing an unwanted burden on their own sex, and it put the burden of proof on the movement to demonstrate demand. Second, the home is women's sphere, an argument built from the era's own values rather than against them: women exercised influence through family and church, and the ballot would trade that influence for a lesser, partisan power. Third, politics would coarsen women without cleansing politics, a claim that conceded the machines were dirty and asked why anyone would want women near them. Students do not have to find these arguments persuasive. They should understand why they worked, especially on the male legislators and voters who decided referendums, and why defeating them took organization rather than merely being right.",
             kick='C · The Opposition')

# ----------------------------------------------------- 15 · THE MONEY
content_text('The money behind the argument',
             ['Brewers and distillers feared women voters would advance Prohibition.',
              'Urban machines feared voters they could not control.',
              'The movement\u2019s own compromise was courting the South with white supremacy arguments.',
              'Black suffragists were asked to march at the back, or not at all.'],
             "Behind the public argument stood interested money, and the answer key names two backers with two distinct motives. The liquor industry, brewers and distillers, feared correctly that women voters would advance Prohibition; exit ticket question two tests exactly this, since the suffrage amendment said nothing about alcohol. Urban political machines feared a large new bloc of voters outside their ward organizations, voters whose ballots no boss could deliver or monitor. Then turn the slide's second half on the suffrage movement itself, because the reading insists on it and Lesson 8 will build on it. Some suffrage leaders courted southern support by arguing that white women's votes would protect white supremacy, and Black suffragists were repeatedly asked to march at the back of parades or not at all. Name this plainly as a compromise the movement made for advantage. It bought southern tolerance at the price of betraying the principle the movement claimed to stand for, and the cost came due after 1920, when the amendment's promise reached Black women in the Jim Crow South only on paper.",
             kick='C · The Opposition')

# ------------------------------------------------- 16 · SECTION D DIVIDER
divider_photo('sentinels-port.jpg', 'Section D', 'The Final Push',
              ['From January 1917, pickets stand at the White House gates,', 'the first ever to picket a wartime president'],
              "The photograph shows Alice Paul leading the picket line out of National Woman's Party headquarters on October 20, 1917, carrying a banner that quotes President Wilson's own words back at him: the time has come to conquer or submit. Paul was arrested that same day. Section D explains how a forty-year stalemate broke in under four years, and the reading's answer is the section's thesis: victory came from running both roads at once. Carrie Chapman Catt's NAWSA worked the inside, coordinating state campaigns with the federal drive and holding the party in power responsible. Alice Paul's party worked the outside, with a parade that seized the capital's attention in 1913 and then the Silent Sentinels, whose arrests and imprisonment turned public opinion. Neither organization liked the other much. The results neither could have produced alone is the point students should carry into the reading's fourth question, which asks what each strategy contributed that the other could not.")

# ----------------------------------------------------- 17 · WINNING PLAN
content_text('The inside strategy: Catt\u2019s Winning Plan',
             ['Carrie Chapman Catt led NAWSA from 1915.',
              'State campaigns were coordinated with a federal amendment drive.',
              'The party in power was held responsible for the result.',
              'The plan ran organization on a scale the movement had never run before.'],
             "Carrie Chapman Catt took over NAWSA in 1915 and gave the inside strategy a name students need verbatim: the Winning Plan, Carrie Chapman Catt's strategy of coordinating state campaigns with a federal amendment drive. Before Catt, state campaigns and the federal campaign had competed for the same money and often worked at cross purposes. The Winning Plan subordinated both to one timetable. State campaigns were chosen for federal effect: each new suffrage state sent members of Congress to Washington who answered to women voters, and each referendum demonstrated demand in language politicians could count. The plan's political engine was accountability. The party in power was held responsible for the amendment's progress, which meant Democrats in 1916 and after faced organized punishment in the states where women already voted. This is what the answer key calls making the amendment plausible: Catt did not merely ask Congress for a vote, she spent four years changing the composition and incentives of Congress until a yes vote was the safer choice for hundreds of members.",
             kick='D · The Final Push')

# ----------------------------------------------------- 18 · SENTINELS
content_photo_s('paul-port.jpg', 'Paul and the Silent Sentinels',
              ['A suffrage parade marched in Washington on March 3, 1913, the day before Wilson\u2019s inauguration.',
               'From January 1917, the Sentinels stood silent at the White House gates.',
               'Their banners quoted the president\u2019s own words back to him.'],
              "The portrait shows Alice Paul at her desk in 1915, photographed by Harris and Ewing, and she looks exactly like what she was: an organizer of formidable discipline. Paul had worked with the militant suffragettes in England and came home convinced that American suffragists were too polite to be feared. Her Congressional Union staged its announcement on March 3, 1913, a suffrage parade down Pennsylvania Avenue the day before Woodrow Wilson's inauguration, chosen so the incoming president's crowds and press would belong to the suffragists instead. Then, from January 1917, her National Woman's Party stationed the Silent Sentinels at the White House gates: Alice Paul's pickets who stood at the White House gates from January 1917, in the guided notes' definition. The silence was the discipline. Respectable women stood without speaking, in all weather, holding banners that quoted Wilson's speeches about democracy, and they were the first group ever to picket a wartime president. Every arrest the government made against that tableau cost the government more than it cost the pickets.",
              kick='D · The Final Push')

# ----------------------------------------------------- 19 · OCCOQUAN
content_text('Occoquan and the Night of Terror',
             ['Arrested for obstructing the sidewalk, pickets were sent to the Occoquan Workhouse.',
              'November 14, 1917 was the Night of Terror.',
               'Hunger strikes were answered with force-feeding.',
               'Wilson announced support in January 1918, as a war measure.'],
             "The government answered the pickets with arrests on the charge of obstructing the sidewalk, a charge that required the women to be blocking traffic they were demonstrably not blocking. Sentences lengthened from fines to months at the Occoquan Workhouse in Virginia. On the Night of Terror, November 14, 1917, guards beat the imprisoned pickets and left some chained and injured; when the women hunger-struck in protest, officials force-fed them. The administration expected the arrests to end the embarrassment. They achieved the opposite. Released prisoners described their treatment to reporters, lawyers took the cases, and the spectacle of the government imprisoning women for standing silently with the president's own words became indefensible in the middle of a war fought, in Wilson's phrase, for democracy. The reading's causal chain is short and students should copy it: the publicity turned public opinion, and Wilson announced his support for the amendment in January 1918, framing suffrage as a war measure. Paul's outside pressure had moved the one man whose party controlled the outcome.",
             kick='D · The Final Push')

# ------------------------------------------------- 20 · SECTION E DIVIDER
divider_photo('banner-port.jpg', 'Section E', 'Ratification',
              ['Thirty-six states had to say yes.', 'By the summer of 1920, thirty-five had.'],
              "The photograph shows Alice Paul on the balcony of National Woman's Party headquarters in August 1920, unfurling the ratification banner as her members watch from below. The banner carried a star for every state that had ratified, sewn on one at a time as the victories came in, and it waited most of that summer with thirty-five stars on it. Section E is short because the story narrows to arithmetic and then to a single room. Congress finished its work in June 1919, and ratification moved to the states, where it became what the reading calls a state-by-state trench war: quick wins first, then a wall of states that refused to act at all. The amendment needed thirty-six of forty-eight. What follows is how the thirty-sixth was found, and how close the entire seventy-two year campaign came to failing one state short.")

# ----------------------------------------------------- 21 · STAT 36
stat('36 OF 48', 'states had to ratify the amendment',
     'By the summer of 1920, thirty-five had. The remaining legislatures were refusing to act.',
     "Pause on the arithmetic, because it is the whole section. Three-fourths of forty-eight states is thirty-six, and by the summer of 1920 the suffragists had exactly thirty-five. The states that remained were not undecided in any ordinary sense: most had rejected the amendment outright or refused to call their legislatures into session to consider it, and southern opposition, where the race question ran hottest, was firm. That is what made the count a trench war rather than a formality. Every avenue had been tried for a year. This is also the setup for the reading's fifth question, why Tennessee could matter at all. A single state legislator's vote can only decide a national question when the count stands at exactly thirty-five and every other door is closed. Tennessee's governor agreed to call a special session in August 1920, where other holdout governors had refused. Both sides understood what that meant, and both sides descended on Nashville.",
     kick='E · Ratification')

# ----------------------------------------------------- 22 · TENNESSEE
content_text('Tennessee, and one mother\u2019s letter',
             ['Congress finished: the House passed in 1918, and the Senate on June 4, 1919.',
              'In Tennessee the state house vote tied.',
              'Harry Burn switched after a letter from his mother.',
              'Tennessee ratified on August 18, 1920, and the amendment was certified on August 26.',
              'The vote shall not be denied or abridged on account of sex.'],
             "The sequence belongs on the board in order. The House passed the amendment in 1918. The Senate failed once, then passed it on June 4, 1919, and the ratification fight began. Through the following year thirty-five states ratified. In Nashville in August 1920, suffragists and antis lobbied the Tennessee legislature in what reporters treated as a second war, and the state house vote tied. The tie broke on Harry Burn, a young legislator who had been counted with the opposition. He had received a letter from his mother urging him to vote for suffrage, and he switched. Tennessee ratified on August 18, 1920, and the Nineteenth Amendment was certified on August 26. Read the operative sentence aloud, because one sentence was the entire object of the seventy-two years: the right of citizens to vote shall not be denied or abridged on account of sex. Stanton had demanded that sentence's substance in 1848. She had been dead for eighteen years when it became law.",
             kick='E · Ratification')

# ------------------------------------------------------------- 23 · VOCAB A
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

vocab('Words for the movement',
      [('suffrage', 'the right to vote'),
       ('NAWSA', 'the National American Woman Suffrage Association, formed in 1890 by the reunited wings of the movement'),
       ('Silent Sentinels', "Alice Paul's pickets who stood at the White House gates from January 1917")],
      "These definitions match the guided notes word for word, so students can copy them directly into their notes. Suffrage is the right to vote, a general word that in this era's headlines almost always meant women's voting rights specifically; when a 1910 newspaper says the suffrage question, it means this fight. NAWSA is the National American Woman Suffrage Association, formed in 1890 by the reunited wings of the movement, and it was the movement's mainstream giant, the organization Catt led and the one most state campaigns ran through. The Silent Sentinels were Alice Paul's pickets who stood at the White House gates from January 1917. Note the division these three terms map: one names the goal, one names the inside organization, and one names the outside tactic. Students who can attach each term to its act in the lesson, suffrage to the whole fight, NAWSA to Catt's strategy, Sentinels to Paul's, have the lesson's structure in miniature, and the unit test's matching section uses these definitions nearly verbatim.")

# ------------------------------------------------------------- 24 · VOCAB B
vocab('Words for the finish',
      [('Winning Plan', "Carrie Chapman Catt's strategy of coordinating state campaigns with a federal amendment drive"),
       ('Nineteenth Amendment (1920)', 'amendment barring denial of the vote on account of sex')],
      "Two terms carry the endgame, and again the wording matches the guided notes exactly. The Winning Plan was Carrie Chapman Catt's strategy of coordinating state campaigns with a federal amendment drive, with the party in power held responsible for the result; it is the inside strategy of Act D in a single phrase. The Nineteenth Amendment (1920) is the amendment barring denial of the vote on account of sex, certified on August 26, 1920, after Tennessee became the thirty-sixth state to ratify. Two precision points are worth thirty seconds. First, the amendment's date: Congress passed it in 1919, but it belongs to 1920 because ratification is what made it law. Second, the amendment's limit, which Lesson 8 examines in full: the amendment barred denial on account of sex, but it did not by itself put ballots in the hands of Black women across the Jim Crow South, where the same machinery that disfranchised Black men was turned on them. The sentence was universal. Its enforcement was not, and that gap is where the unit goes next.")

# --------------------------------------------------------- 25 · TODAY'S WORK
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'The Strategy Memo', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 2.6,
     ['Judge the argument the movement argued for forty years. Which road deserved its money, its organizers, and its years?'],
     size=23, color=POWDER, leading=1.3)
rows = [('The task', 'Write the strategy memo: state road or federal amendment'),
        ('The evidence', 'The western map, the stalled Congress, and New York in 1915 and 1917'),
        ('The standard', 'The memo that hedges loses. Pick a road, fund it, and answer the other side')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.5, 0.6, d, size=19, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.8, 11.5, 0.5, 'Exit ticket: each road\u2019s strongest argument; the liquor industry\u2019s money; why Wilson\u2019s own words were hard to answer.',
     size=16, color=POWDER)
notes(s, "Close by handing the lesson to its writing task, the strategy memo, which students have in the lesson's writing handout. The assignment: write to the movement's leadership as an adviser, and commit its resources to one road, the state campaigns or the federal amendment. The evidence base is Act B, and strong memos use the map concretely: the western states won early and cheaply, New York cost two campaigns in three years, Congress ignored the amendment for a generation, and the supermajority arithmetic cuts both ways, brutal to reach and total once reached. Require the memo to answer the other road's best argument, since the historical actors had to. Then the exit ticket from the guided notes, three questions: state each road's strongest argument in one sentence; explain why the liquor industry spent against suffrage though the amendment said nothing about alcohol, because women voters were expected to advance Prohibition; and explain why banners quoting Wilson's own democracy words were hard for him to answer during a war fought in democracy's name. Next lesson takes up what the amendment did not finish.")

dc.save(OUT)
