#!/usr/bin/env python3
"""Lesson 7 deck, "The Home Front," Imperialism and World War I unit.
Built to the approved system: image-led slides, fragments only on screen,
comprehensive speaker notes, full lesson and vocabulary coverage.
Fonts: Georgia titles, Lato body. Kicker: IMPERIALISM AND WORLD WAR I."""
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
OUT = os.path.join(HERE, '..', 'lesson-07-slides.pptx')
KICK = 'IMPERIALISM AND WORLD WAR I \u00b7 LESSON 7'

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
photo_right(s, 'flagg-port.jpg')
text(s, 0.9, 0.75, 6.9, 0.4, KICK, size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 1.55, 6.9, 2.2, 'The Home Front', size=54, color=CREAM, font='Georgia', leading=1.05)
rule(s, 0.92, 3.55)
text(s, 0.9, 3.9, 6.6, 2.4, ['A war fought overseas,', 'and a country remade at home'], size=22, color=POWDER, space_after=8, leading=1.25)
notes(s, "The poster is James Montgomery Flagg and his Uncle Sam, the most recognizable American recruiting image ever printed. Give students the dates plainly, because the quick check tests them: Flagg drew Uncle Sam in 1916 and the drawing first appeared on the cover of Leslie\u2019s Weekly that July, before the United States entered the war. The Army reused the drawing as a recruiting poster in 1917. So the image predates the American war it came to stand for, and no student should treat 1917 as the year it was drawn. Frame the lesson from it. The armies fought in Europe, but the war was also fought in American factories, theaters, courtrooms, and neighborhoods. This lesson follows the home front: how the government raised money and goods, how it sold the war, how it punished dissent, and which Americans gained ground while others lost it.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did the war change American life at home, and who gained and who lost by the change?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('Why did the United States seek power overseas, and how did the First World War change the country that fought it?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Read the lesson question aloud and keep both halves in view all period. How did the war change American life at home? The federal government directed industry, borrowed billions from its own citizens, ran a national persuasion campaign, and prosecuted speech. Who gained and who lost by the change? Women gained war jobs and then the vote. Black southerners gained a path north to wages and ballots. German Americans lost language classes, music, and in one case a life. Dissenters lost their liberty for leaflets and speeches. Tell students the exit ticket asks for one gaining group and one losing group with evidence for each, so they should keep a running tally as the sections move. Under the unit question, this lesson answers how the war changed the country that fought it: the change ran in two directions at once, toward wider opportunity and toward narrower rights.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.3, 11.5, 1.0, 'Money, persuasion, law, and movement', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.42)
rows = [('A', 'Managing Production and Money', 'a civilian economy turned to war in months'),
        ('B', 'Selling the War', 'a federal campaign to make a divided country act as one'),
        ('C', 'The Law Against Dissent', 'two statutes, two thousand cases, one Supreme Court test'),
        ('D', 'Fear at Home', 'suspicion aimed at German Americans and their neighbors'),
        ('E', 'Women, Work, and the Vote', 'war work becomes an argument for the ballot'),
        ('F', 'The Great Migration', 'hundreds of thousands move north for jobs and rights')]
yy = 2.82
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.7, n, size=26, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.03, 4.9, 0.7, t, size=19, color=CREAM, bold=True)
    text(s, 6.6, yy + 0.08, 5.8, 0.7, d, size=17, color=POWDER)
    yy += 0.72
notes(s, "This is the map of the lesson, and it follows the guided notes section by section. Section A covers the managed economy: the War Industries Board directing production and Liberty Bonds paying for roughly two thirds of the war. Section B covers the Committee on Public Information and its persuasion campaign. Section C covers the Espionage and Sedition Acts, the prosecutions under them, and the Schenck decision. Section D steps outside the courts to the fear aimed at German Americans. Sections E and F cover the two great movements of people: women into war work and toward the vote, and Black southerners north in the Great Migration. The reading closes with the strikes of 1919, and the deck closes there too. Tell students the activity stations, the notebook, and the exit ticket all follow this same order, so the map on this slide is also their study map for the unit test.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_photo('christy-port.jpg', 'Section A', 'Managing Production and Money',
              ['A civilian economy,', 'turned to war in months'],
              "The poster is Howard Chandler Christy and his Fight or Buy Bonds, printed for the Third Liberty Loan in 1917 and held by the Library of Congress. Read its structure before its art: a soldier and a flag on one side, and an either or choice with no third position. Fight, or lend. Students will meet this same poster at Station 4 of the activity, paired with a sentence from the Treasury, and will be asked to separate a financial appeal from a loyalty test. Set the section frame now. In April 1917 the American army was small and American factories served peacetime customers. Within months the federal government was setting production priorities, fixing prices, running the railroads, pressing families to save food, and borrowing billions from the public. Section A asks how a government does that, and what it asks of ordinary people in the process.",
              title_size=40)

# ------------------------------------------------------ 5 WAR INDUSTRIES BOARD
content_text('Directed: the War Industries Board',
             ['The board was created in 1917, and it was led from 1918 by Bernard Baruch.',
              'The board set priorities for raw materials.',
              'The board told factories what to produce.',
              'The board fixed prices on key goods.',
              'The railroads came under federal control, and families saved food for the armies.'],
             "Teach the board as a system of direction, not a suggestion box, because guided notes blanks one and two test exactly this. The War Industries Board was created in 1917 and led from 1918 by the financier Bernard Baruch. It set priorities for raw materials, told factories what to produce, and fixed prices on key goods. Around it stood companion measures: the railroads came under federal control, and a Food Administration pressed families to save food for the armies. Production rose sharply, and students should name the reason accurately. A peacetime market, left alone, makes goods for whoever pays most. A war economy makes goods in the order the army needs them, and that ordering is a government act. Ask the class what Baruch could do to a factory owner who refused a priority order, and let them reason about the power behind the paperwork before you confirm how much of it rested on pressure and patriotism.",
             kick='A \u00b7 Managing Production and Money')

# ------------------------------------------------------ 6 LIBERTY BONDS
content_text('Borrowed from the public: Liberty Bonds',
             ['Liberty Bonds were government bonds sold to the public, and they were repaid with interest.',
              'The Treasury ran five great loan drives, with rallies and quotas in nearly every town.',
              'Americans bought about 17 billion dollars in bonds.',
              'Bond sales covered about two thirds of the cost of the war.',
              'Buying a bond became a public test of loyalty.'],
             "Define the instrument first, in the guided notes wording: Liberty Bonds were government bonds sold to the public to raise money for the war, repaid with interest. A buyer was a lender, not a donor, and the Treasury ran five great loan drives, with rallies and sales quotas reaching nearly every town. Americans bought roughly 17 billion dollars in bonds, about two thirds of the cost of the war. Then teach the second half of the slide, because the reading insists on it. Buying a bond became a public test of loyalty as well as a loan. Quotas were posted, names were known, and a neighbor who bought nothing had explaining to do. That pressure is the bridge to the Christy poster from the divider: fight or buy leaves no respectable third choice. Reading question one asks students to explain both the board and the bonds together, so keep the money and the production in one frame.",
             kick='A \u00b7 Managing Production and Money')

# ------------------------------------------------------ 7 STAT: 17 BILLION
stat('$17 BILLION', 'in Liberty Bonds bought by the American public',
     'Bond sales covered about two thirds of the cost of the war. The rest came from taxes and other borrowing.',
     "Let the number sit before you explain it. Seventeen billion dollars, in the money of 1917 and 1918, lent to the government by its own citizens in five loan drives. Bond sales covered about two thirds of the cost of the war, a share students should copy with its dates and its source, the Treasury drives themselves. Put the figure next to the board from the last section and the pairing becomes the section in one line: the board decided what the economy would make, and the bonds decided who would pay for it, which turned out to be the public itself, repaid later with interest. Note the voluntariness carefully for the activity verdict. No law required a citizen to buy a bond. The pressure was social and organized, applied by rallies, quotas, and posters, and students will have to judge at Station 4 whether organized social pressure counts as the government asking or the government compelling.",
     kick='A \u00b7 Managing Production and Money')

# ------------------------------------------------- 8 SECTION B DIVIDER
divider_photo('hopps-port.jpg', 'Section B', 'Selling the War',
              ['Posters, pamphlets, films,', 'and 75,000 speakers'],
              "The poster is Harry R. Hopps and his Destroy This Mad Brute, printed in 1917: a drooling ape in a spiked helmet, a club labeled with German culture in his hand, a woman in his arm, and American ruins behind him. Now the disclosure students must carry into the activity: this is an Army recruiting poster, not a Committee on Public Information product, and the lesson source line says so. The distinction is the section in miniature. Many agencies sold this war, in many voices, and students who credit every poster to the committee have not read closely. What the committee did produce, posters, pamphlets, films, and speakers, fills the next two slides. Teach this image as the emotional register of the campaign: an enemy drawn as an animal, a threat drawn as personal, and enlistment drawn as the only answer. Station 1 of the activity asks students to test the committee claim of education against imagery in this register.",
              title_size=54)

# ------------------------------------------------------ 9 COMMITTEE ON PUBLIC INFORMATION
content_text('The Committee on Public Information',
             ['President Wilson created the committee in April 1917, and the journalist George Creel led it.',
              'The committee printed millions of pamphlets, and it supplied news releases to newspapers.',
              'The committee made films, and its posters covered walls across the country.',
              'The committee called its work education.',
              'Its purpose was persuasion.'],
             "Give the committee its full name and its definition in the guided notes wording: the federal agency that promoted support for the war through posters, pamphlets, films, and speakers. President Wilson created it in April 1917 under the journalist George Creel. Its output was industrial in scale: millions of pamphlets, a steady supply of news releases to newspapers, films, and posters covering walls across the country. Then draw the reading distinction slowly, because reading question two grades it. The committee presented its work as education, and much of what it published was factual. Its purpose, however, was persuasion: to make a divided country act and think as one. A fact can be accurate and still be selected, timed, and framed to move a reader in one direction. Students who can hold both halves, factual material and persuasive purpose, are ready for the stations. Students who pick one half only will misjudge either the poster or the prosecutions.",
             kick='B \u00b7 Selling the War')

# ------------------------------------------------------ 10 FOUR MINUTE MEN
content_text('Four minutes in the theater',
             ['About 75,000 volunteers served as speakers.',
              'They gave short patriotic talks while the film reels changed.',
              'One message was repeated in nearly every town.',
              'The message was to enlist, buy bonds, save food, and suspect spies.'],
             "The Four Minute Men are the committee at its most inventive, and students remember them when they forget the pamphlets. About 75,000 volunteers gave short patriotic talks in movie theaters in the minutes while the reels were changed, a captive audience in the dark with nowhere else to look. The name joined the Revolutionary minuteman to the length of the reel change. Their topics came from Washington bulletins: enlist, buy bonds, save food, report spies. Consider the reach with the class. A poster can be walked past. A newspaper can be left unopened. A speaker in a theater, a respected local man in most cases, speaks to a whole town at leisure, in person, in a voice the audience knows. That is persuasion with a local face, and it helps explain how national campaigns become neighborhood pressure, the same pressure that sold the bonds in section A and watched the neighbors in section D. Keep the number, about 75,000, in the notes for the At a Glance table.",
             kick='B \u00b7 Selling the War', size=24)

# ------------------------------------------------- 11 SECTION C DIVIDER
divider_text('Section C', 'The Law Against Dissent',
              'Two statutes, more than two thousand prosecutions, and a Supreme Court test for wartime speech',
              "Move the class from persuasion to compulsion, and mark the change of instrument. In section B the government asked, argued, and advertised. In this section it prosecuted. Congress gave the government legal weapons against opposition in two steps: the Espionage Act of 1917 and the Sedition Act of 1918, broader and aimed directly at speech. Prosecutors brought more than two thousand cases under the two laws. Two of those cases carry this section. Charles Schenck mailed leaflets against the draft and carried his conviction to the Supreme Court, which answered with the clear and present danger test. Eugene Debs gave a speech in Ohio and ran for president from a prison cell. Tell students the activity places the statutes at Station 2 and Schenck at Station 3, side by side on purpose: first the law as written, then the law as the Court allowed it to be used.")

# ------------------------------------------------------ 12 THE TWO ACTS
content_text('Two laws against opposition',
             ['The Espionage Act of 1917 punished spying, and it made obstructing recruiting a crime.',
              'The act also made insubordination in the armed forces a crime.',
              'The Sedition Act of 1918 punished disloyal or abusive language.',
              'It punished speech about the government, the Constitution, the flag, and the armed forces.',
              'Prosecutors brought more than two thousand cases under the two laws.'],
             "Teach the two acts as a widening circle, using the guided notes definitions word for word. The Espionage Act was the 1917 federal law that punished spying and acts intended to interfere with the military or obstruct recruiting. Its center was conduct close to the war machine: spies, sabotage, blocked recruiting, insubordination in the ranks. The Sedition Act of 1918 went further: the 1918 federal law that punished disloyal or abusive speech about the government, the Constitution, the flag, and the armed forces. Its center was words. A citizen could now be prosecuted for language itself, with no spy ring and no blocked recruiting station anywhere in the case. Prosecutors brought more than two thousand cases under the two laws together. Ask students where they would draw the line between the two statutes, and hold their answers for the Schenck slide, where the Supreme Court drew its own line and the country lived with it for fifty years.",
             kick='C \u00b7 The Law Against Dissent', size=24)

# ------------------------------------------------------ 13 SCHENCK
s = slide(CREAM)
photo_right(s, 'flagg-port.jpg')
kicker(s, 'C \u00b7 The Law Against Dissent', color=RUST)
text(s, 0.9, 0.95, 6.9, 1.2, 'Schenck and the clear and present danger test', size=31, color=NAVY, font='Georgia', leading=1.05)
frags(s, ['Charles Schenck was an officer of the Socialist Party.',
          'He mailed leaflets that urged men to resist the draft.',
          'He was convicted under the Espionage Act.',
          'In 1919, a unanimous Supreme Court upheld the conviction.',
          'Justice Holmes held that speech could be punished when it created a clear and present danger.'],
      y=2.15, size=19, gap=13)
notes(s, "The poster beside the text is the recruiting appeal Schenck was convicted of obstructing, Flagg and his Uncle Sam, drawn in 1916 and reused by the Army in 1917. Now the case. Charles Schenck, an officer of the Socialist Party, was convicted for mailing leaflets that urged men to resist the draft. In Schenck v. United States in 1919, a unanimous Supreme Court upheld the conviction. Justice Oliver Wendell Holmes wrote that speech could be punished when it created a clear and present danger of an evil Congress had the power to prevent. Teach the test in the guided notes wording: the 1919 Supreme Court case that upheld an Espionage Act conviction and stated the clear and present danger test for wartime speech. Then press on the facts. Schenck mailed paper. No recruit is shown to have refused because of his leaflets. Students must decide whether danger on paper met the test, which is exactly the judgment Station 3 demands.")

# ------------------------------------------------------ 14 DEBS
content_text('Debs: a speech, a prison cell',
             ['Eugene V. Debs was the leading American socialist.',
              'He gave a speech at Canton, Ohio, in 1918, and he praised draft resisters.',
              'He received a ten year sentence for the speech.',
              'He ran for president in 1920 from a federal prison cell.'],
             "Debs is the human scale of the two acts, and the reading gives him one paragraph on purpose. Eugene V. Debs, the leading American socialist and a four time candidate for president, spoke at Canton, Ohio, in 1918 and praised men who had resisted the draft. For that speech he received a ten year sentence. In 1920 he ran for president from a federal prison cell and drew close to a million votes, ballots cast for a man the government held behind bars for words spoken at a picnic ground. Set Debs beside Schenck and the section argument completes itself. Schenck shows the doctrine: the Court announced when speech may be punished. Debs shows the practice: the country\u2019s best known opposition voice spent the election in prison. Guided notes blanks thirteen and fourteen test the ten years and the prison cell. Exit ticket question two tests the Schenck test itself, in the student\u2019s own words, so both cases must stay distinct in the notes.",
             kick='C \u00b7 The Law Against Dissent')

# ------------------------------------------------- 15 SECTION D DIVIDER
divider_text('Section D', 'Fear at Home',
              'Suspicion aimed at German Americans, enforced by neighbors as much as by law',
              "This short section steps outside the courts, and students should feel the change of venue. Sections B and C described the federal government: a committee, two statutes, a Supreme Court. Section D describes the public itself. War feeling ran outside the law, in school boards that dropped German classes, orchestras that stopped playing German music, and grocers who renamed sauerkraut. It also ran through organized watching: loyalty leagues and the American Protective League observed neighbors and reported suspected disloyalty to the Justice Department. The reading closes the section with the case students must not forget: in April 1918 a mob in Illinois lynched Robert Prager, a German born immigrant who had applied for American citizenship. Frame the question the section leaves open. The government did not order the mob. It had spent a year teaching the country to see disloyalty everywhere, and students will judge in the activity how far official persuasion answers for private violence.")

# ------------------------------------------------------ 16 FEAR AT HOME
content_text('Patriotism, and persecution',
             ['Schools dropped German language classes.',
              'Orchestras stopped playing German music.',
              'Sauerkraut became liberty cabbage.',
              'The American Protective League watched neighbors.',
              'In April 1918, a mob lynched Robert Prager in Illinois.'],
             "Work down the slide in order, from the petty to the lethal, because the order is the argument. Schools dropped German language classes. Orchestras stopped playing German music. Sauerkraut became liberty cabbage, a renaming students laugh at, until the next lines land. Loyalty leagues and the American Protective League watched neighbors and reported suspected disloyalty to the Justice Department, turning suspicion into a civic duty performed on the people next door. In April 1918 a mob in Illinois lynched Robert Prager, a German born immigrant who had applied for American citizenship. He had sought the status his killers claimed he lacked. Use the reading sentence as the slide verdict: the line between patriotism and persecution was crossed often, usually against people with no power to answer back. Guided notes blanks fifteen through seventeen test liberty cabbage, Prager, and the American Protective League by name, so read all three aloud as you close the slide.",
             kick='D \u00b7 Fear at Home')

# ------------------------------------------------- 17 SECTION E DIVIDER
divider_text('Section E', 'Women, Work, and the Vote',
              'War work opens factory gates, and the service becomes an argument for the ballot',
              "Turn from loss to gain, and say so. The two sections before this one recorded what the war took from Americans at home: speech, safety, in one case a life. This section records what the war opened. With millions of men in uniform and immigration from Europe cut off, the labor shortage reached into workplaces that had been closed to women for generations. About a million women entered war industries and related work for the first time, in factories, on railroads, and in offices. Then the second movement of the section: suffrage leaders converted that service into a constitutional argument, and the argument won. President Wilson endorsed the amendment in 1918 as a war measure, Congress passed it in 1919, and the states ratified the Nineteenth Amendment in 1920. Students should track the chain, work, argument, amendment, because the writing task card on women and the vote grades exactly that chain and nothing looser.")

# ------------------------------------------------------ 18 WOMEN AT WORK
content_text('A million women into war work',
             ['Millions of men were in uniform, and immigration was cut off.',
              'Factories, railroads, and offices hired women.',
              'Jobs long closed to women opened.',
              'About a million women entered war industries for the first time.'],
             "Start with the shortage, because the reading does and because it keeps the section honest. The gates opened for two reasons at once: millions of men were in uniform, and immigration from Europe, the usual source of new industrial labor, was cut off by the war. Factories, railroads, and offices hired women for jobs that had been closed to them. About a million women entered war industries and related work for the first time. Students should hear both halves of that fact. It was real work at real wages in places women had been told they did not belong, and it was also wartime expedient hiring that employers expected to reverse when the men came home, as in large part it did. Guided notes blank eighteen tests the million figure. Hold the reversal for the closing slide, where the strikes and the returning soldiers end the wartime labor truce, and let this slide stand for the opening itself.",
             kick='E \u00b7 Women, Work, and the Vote')

# ------------------------------------------------------ 19 THE VOTE
content_text('Service becomes an argument: the Nineteenth Amendment',
             ['Suffrage leaders pointed to women\u2019s war work.',
              'The nation fought for democracy abroad, and it denied women the vote at home.',
              'Wilson endorsed the amendment in 1918, as a war measure.',
              'Congress passed it in 1919, and the states ratified it in 1920.'],
             "Teach this slide as an argument being won, step by step. Suffrage leaders pointed to women\u2019s war work and asked how a nation fighting for democracy abroad could deny women the vote at home. The war had handed them the strongest version of their claim: the government itself had asked women to sustain the war economy, and the service was public, counted, and praised. President Wilson endorsed a federal amendment in 1918 as a war measure, his own framing, which students should quote accurately. Congress passed the Nineteenth Amendment in 1919, and the states ratified it in 1920. Guided notes blanks nineteen and twenty test the 1918 endorsement and the 1920 ratification. Close by returning to the lesson question. Here is the clearest gain of the home front: a constitutional right, won in part because the war made the old refusal impossible to defend in public. The next section follows the second great gain, and its harder landing in the North.",
             kick='E \u00b7 Women, Work, and the Vote', size=24)

# ------------------------------------------------- 20 SECTION F DIVIDER
divider_text('Section F', 'The Great Migration',
              'Hundreds of thousands of Black southerners move north for jobs and greater rights',
              "Use the guided notes definition to open the section, word for word: the Great Migration was the movement of hundreds of thousands of Black southerners to northern cities for jobs and greater rights during and after the war years. The same labor shortage that opened factory gates to women in section E opened them here. Northern factories, cut off from European immigrant labor, sent labor agents south, and Black newspapers such as the Chicago Defender carried word of jobs and higher wages north along the rail lines. Beginning in 1916 the movement reshaped both regions: southern counties lost the workers their economy rested on, and Chicago, Detroit, and Cleveland gained new Black neighborhoods, churches, newspapers, and voters. Tell students the section runs on one investigator\u2019s count and one set of named causes, both tested in the guided notes, and that the reading holds the gain and the hardship together to the last line.")

# ------------------------------------------------------ 21 PUSH AND PULL
content_text('Pushed out, pulled north',
             ['Northern factories sent labor agents south.',
              'The Chicago Defender carried word of jobs and wages north.',
              'Low wages, the crop lien system, and disenfranchisement pushed people out.',
              'The convict lease system, lynching, and violence also pushed people out.',
              'Wages, schools, and the right to vote pulled people north.'],
             "Teach the migration as a decision made under pressure from both directions, because guided notes section F grades one push and one pull from every student. The federal investigator Emmett J. Scott named the forces pushing people out: low wages and cheating in the crop lien system, disenfranchisement, the convict lease system, and violence, including lynching. The pull was concrete: northern war industry jobs at higher wages, schools for children, and the right to vote, which most Black southerners had been stripped of at home. Migrants sought wages, schools, and voting rights, and relief from the system Scott cataloged. Then the landing, which the reading refuses to soften. Migrants found real opportunity and also crowded housing, high rents, and white hostility that would turn violent in the riots of 1919. A strong answer to reading question four holds both halves at once: pulled north by jobs, pushed out by oppression, and met in the North by both wages and violence.",
             kick='F \u00b7 The Great Migration', size=24)

# ------------------------------------------------------ 22 STAT: 400,000
stat('400,000+', 'Black southerners moved north in three years, by Scott\u2019s count',
     'Emmett J. Scott, the federal investigator, published these figures in 1920. They are his reported count, not a census.',
     "Attribute this number every time you say it, because the attribution is part of the lesson. The federal investigator Emmett J. Scott reported that more than 400,000 Black people had moved north in the three years after the war began in Europe. These are Scott\u2019s figures, published in his 1920 study of wartime migration, and students should present them as his reported count, gathered from agents, railroads, and correspondents, not as a census enumeration. The number still does its work. Four hundred thousand people in three years is a movement no one directed and no law ordered: families deciding, one household at a time, that the South Scott described, its crop liens, its disenfranchisement, its convict leases, its lynching, was no longer bearable beside northern wages. Guided notes blanks twenty one and twenty two test Scott\u2019s name and his 400,000 together. Keep them paired in your own speech all period, name and number, so students copy them paired.",
     kick='F \u00b7 The Great Migration')

# ------------------------------------------------------ 23 WHAT THE WAR LEFT BEHIND
content_text('1919: the home front comes apart',
             ['Wartime strike limits came off, and prices were still high.',
              'More than four million workers struck in 1919.',
              'After revolution in Russia, the strikes were read as revolution.',
              'Women kept the vote, and migrants kept moving.',
              'Dissenters kept the lesson that wartime rights could be withdrawn.'],
             "Close the survey where the reading closes, with the settlement of 1919. Unions had accepted limits on strikes while the war lasted, and workers had watched prices rise faster than wages. When the controls came off, more than four million workers took part in strikes. Employers and much of the public, frightened by revolution in Russia, read the strikes as revolution rather than bargaining, and most were defeated. Then give students the reading verdict in full, because it is the lesson question answered in one breath. The home front ended the war divided: women had won the vote and Black families had begun a migration that would reshape the country, while dissenters had learned that wartime rights could be withdrawn by law and by mob alike. Reading question five asks for three groups with one gain and one loss each. Any group named today qualifies, and students should now be able to build that answer without opening the reading again.",
             kick='The reading, closing section')

# ------------------------------------------------------ 24 VOCAB A
vocab('Words for money, production, and persuasion',
      [('Liberty Bonds', 'government bonds sold to the public to raise money for the war, repaid with interest'),
       ('War Industries Board', 'the federal agency that coordinated war production and set priorities for industry during the war'),
       ('Committee on Public Information', 'the federal agency that promoted support for the war through posters, pamphlets, films, and speakers'),
       ('Espionage Act', 'the 1917 federal law that punished spying and acts intended to interfere with the military or obstruct recruiting')],
      "These four definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. Liberty Bonds: government bonds sold to the public to raise money for the war, repaid with interest. War Industries Board: the federal agency that coordinated war production and set priorities for industry during the war. Committee on Public Information: the federal agency that promoted support for the war through posters, pamphlets, films, and speakers. Espionage Act: the 1917 federal law that punished spying and acts intended to interfere with the military or obstruct recruiting. Students confuse the board and the committee most often. The board directed things: materials, factories, prices. The committee directed opinion: posters, pamphlets, films, speakers. One ran the economy of the war, the other ran its argument, and the Espionage Act stood behind both with prison for anyone who obstructed the first or answered the second too loudly.")

# ------------------------------------------------------ 25 VOCAB B
vocab('Words for speech and movement',
      [('Sedition Act', 'the 1918 federal law that punished disloyal or abusive speech about the government, the Constitution, the flag, and the armed forces'),
       ('Great Migration', 'the movement of hundreds of thousands of Black southerners to northern cities for jobs and greater rights during and after the war years'),
       ('Schenck v. United States', 'the 1919 Supreme Court case that upheld an Espionage Act conviction and stated the clear and present danger test for wartime speech')],
      "Three more terms, again matching the guided notes exactly. Sedition Act: the 1918 federal law that punished disloyal or abusive speech about the government, the Constitution, the flag, and the armed forces. Note the year and the target: 1918, and language itself. Great Migration: the movement of hundreds of thousands of Black southerners to northern cities for jobs and greater rights during and after the war years. The definition carries both motives, jobs and greater rights, and students should keep both when they use the term. Schenck v. United States: the 1919 Supreme Court case that upheld an Espionage Act conviction and stated the clear and present danger test for wartime speech. Students pair this case with the wrong statute often, so fix the pairing aloud: Schenck was an Espionage Act conviction, reviewed in 1919, and the test it produced governed wartime speech cases for the next fifty years.")

# ------------------------------------------------------ 26 TODAY'S WORK
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Where Did the Government Cross the Line?', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Work the stations. At each one, record what the government asked of Americans and what power it used to get it.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Stations', 'Five stations, then your verdict on where the line was crossed'),
        ('Notebook', 'The home front chart: what was asked, what power, what resulted'),
        ('Quick check', 'Flagg against Schenck: two printed appeals, judged by direction and circumstance'),
        ('Writing', 'Five evidence cards, one paragraph: who gained, who lost, and by what power')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.5, 0.6, d, size=19, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.8, 11.5, 0.5, 'Exit ticket: explain Liberty Bonds, state the clear and present danger test, and name one group that gained and one that lost.',
     size=16, color=POWDER)
notes(s, "Close by handing the lesson to its work. The activity, Where Did the Government Cross the Line, runs five stations: a Committee on Public Information poster, the Espionage and Sedition Acts, Schenck, a Liberty Bond appeal, and a Great Migration account from Scott. At each station students record what the government asked and what power it used, then render a verdict: one station where the government crossed a line, and one where it stayed within its proper wartime powers, each defended with a document. The Migration station is the control case, since the government appears there as an investigator recording a change it did not direct. The notebook collects the home front chart for review day. The quick check sets Flagg against Schenck. The writing task builds one paragraph from five evidence cards on who gained and who lost. The exit ticket checks the spine: Liberty Bonds explained, the Schenck test stated, and one gaining group and one losing group named with evidence.")

dc.save(OUT)
