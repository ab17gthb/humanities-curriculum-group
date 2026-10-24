#!/usr/bin/env python3
"""Lesson 8 deck, built to Alex's slide model (approved Lesson 1 system):
image-led slides, fragments only on screen, comprehensive speaker notes,
full lesson + vocabulary coverage. Fonts: Georgia titles, Lato body."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags,
                         photo_right, divider_photo, content_photo,
                         content_text, stat, divider_text)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

dc.IMG = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lesson-08-slides.pptx')
NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED = (dc.NAVY, dc.CREAM, dc.RUST,
                                                 dc.RUST_LT, dc.POWDER, dc.INK, dc.MUTED)
W = dc.W

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
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, dc.prs.slide_width, dc.prs.slide_height)
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'PROGRESSIVE ERA · LESSON 8', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Limits of Progressivism', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Reform rebuilt the government. This lesson asks who it was rebuilt for.', size=17, color=POWDER)
notes(s, "This is the last content lesson of the unit, and it changes the job. Every earlier lesson described reformers acting for the people. This lesson asks who was included in that phrase. Set the method before the details: judging Progressivism fairly means holding both records at once, the expansion of democracy and its narrowing, without letting either one erase the other. The photograph is a publicity still from The Birth of a Nation, D. W. Griffith's 1915 film glorifying the Ku Klux Klan. It appears on the first slide because the film, and the White House screening it received, is the single most damning exhibit in the lesson. The five sections follow the guided notes exactly: race and the federal government, the organized response, immigration, labor, and Prohibition. Tell students to keep the exit ticket in view all period. Its first item asks them to complete the sentence: Progressivism expanded democracy for someone, while doing something else for someone else. Everything today is evidence for that sentence.")

# ------------------------------------------------- 2 · ESSENTIAL QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('Who did progressivism leave out, and what did that cost?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': RUST_LT, 'italic': True}),
                                ('How did Americans respond to the problems created by industrialization, urbanization, and political corruption?', {'italic': True})]],
     size=17, color=POWDER, font='Georgia', leading=1.2)
notes(s, "The unit question is printed at the top of the guided notes, beneath today's lesson question, and it has carried the whole unit. Today the word Americans does the work. In earlier lessons the responders were mostly reformers inside the system: journalists, presidents, suffragists. Today the responders include the people the system shut out. Black Americans responded to disfranchisement by building the NAACP. Immigrants were responded to in two opposite directions at once. Workers won protections but not power. A useful cold-open: ask students who they picture when the unit says reformers acted for the people, and write two or three answers where the class can see them. The lesson will test every name on that list. By the exit ticket, students should be able to say for whom democracy expanded in this era, for whom it narrowed, and which piece of evidence settles the judgment for them.")

# ------------------------------------------------------------ 3 · OVERVIEW
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.35, 11.5, 1.0, 'One movement, two records', size=46, color=CREAM, font='Georgia')
rule(s, 0.92, 2.5)
rows = [('A', 'Race', 'disfranchisement in the South, segregation in Washington'),
        ('B', 'The response', 'Wells, Du Bois, and a new organization'),
        ('C', 'Immigration', 'the movement argues with itself'),
        ('D', 'Labor', 'real protections, a floor that stayed low'),
        ('E', 'Prohibition', 'the boldest reform, and the only one repealed')]
yy = 2.95
for n, t, d in rows:
    text(s, 0.9, yy, 0.7, 0.7, n, size=30, color=RUST_LT, font='Georgia')
    text(s, 1.65, yy + 0.04, 3.3, 0.7, t, size=27, color=CREAM, bold=True)
    text(s, 5.1, yy + 0.10, 7.4, 0.7, d, size=20, color=POWDER)
    yy += 0.82
notes(s, "This is the map of the lesson, and the letters match the guided notes sections A through E, so students can follow their own page as the deck moves. Section A is the hardest evidence: while reformers democratized city governments, southern states completed the legal structure of Jim Crow, and the Wilson administration segregated the federal government itself. Section B is the answer Black Americans built: documentation, organization, and litigation. Section C shows the movement divided against itself on immigration, ending in the era's darkest use of science. Section D weighs labor's genuine wins against the floor that stayed low. Section E takes up the final amendment, the boldest of the era and the only one ever repealed. Name the skill explicitly: students are not collecting horrors today. They are building a judgment they can defend with evidence, which is what the seminar prep writing task will ask for.")

# ------------------------------------------------- 4 · SECTION A DIVIDER
divider_photo('jimcrow-port.jpg', 'Section A', 'Race and the Federal Government',
              ['Jim Crow completed by law in the South', 'And a segregated government in Washington'],
              "The photograph is a Farm Security Administration image from 1940, a Colored Waiting Room sign at a Durham, North Carolina bus station. It postdates the lesson by two decades on purpose: it shows the mature system, ordinary and official, whose legal foundations were poured in the years this unit covers. While reformers were democratizing city governments and regulating the trusts, southern states were completing the legal structure of Jim Crow, and the federal government under Woodrow Wilson did not merely look away. It segregated its own departments. That is the section's two-part claim, state action and federal action, and students should hold both halves. The guided notes in section A ask for the devices of disfranchisement and the two federal acts of 1913 and 1915. The reading's first question targets exactly this material, so teach it as testable fact, not atmosphere.",
              title_size=40)

# ------------------------------------------------------ 5 · DISFRANCHISEMENT
content_text('How the vote was taken away',
             ['Poll taxes priced poor men out of the voting booth.',
              'Literacy tests were graded by the local registrar.',
              'Grandfather clauses let illiterate whites still vote.',
              'White primaries decided the real election in the one-party South.',
              'Lynching stood behind it all, and no federal law barred it.'],
             "Walk the machinery device by device, because each was designed to look neutral while landing on one race. A poll tax charged men for the right to vote, and it fell hardest on the poor. A literacy test required a voter to read and explain a passage, and the local registrar decided who had passed, which meant the test measured the registrar as much as the voter. The grandfather clause solved the obvious problem that these rules would also bar illiterate and poor whites: it exempted voters whose grandfathers could vote, a category that in the South meant white men only, since Black grandfathers had been enslaved when the clause's reference years were set. White primaries barred Black voters from the Democratic primary, the only election that mattered in the one-party South. Behind the paperwork stood lynching, which enforced the whole system with terror, while anti-lynching bills died in Congress year after year. The result: the vote the Fifteenth Amendment promised was taken back by law, without amending the Constitution.",
             kick='Section A · Race')

# ------------------------------------------------------- 6 · WILSON SEGREGATES
content_photo_s('wilson-port.jpg', 'Washington joins in',
              ['In 1913, the Treasury and Post Office were segregated.',
               'Black clerks were screened off, demoted, and pushed out.',
               'In 1915, the White House screened The Birth of a Nation.',
               'The most democratic administration of the age ran a segregated government.'],
              "Wilson is the president of Lesson 6, the New Freedom, the trust-busting and tariff reform. He is also this. In 1913 his administration segregated the Treasury and Post Office departments, separating Black federal employees in offices where they had worked alongside white colleagues for decades. Screens and separate facilities went up, Black supervisors lost their posts, and men who had built careers in federal service were demoted or driven out. In 1915 the White House screened The Birth of a Nation, Griffith's film glorifying the Ku Klux Klan, the first motion picture ever shown there, lending the presidency's prestige to a story in which the Klan rides as the hero. The NAACP, which students meet in the next section, organized protests against the film across the country. Hold the reading's judgment up plainly, because its first question asks for it: these were not omissions by an administration too busy to act. They were acts. The most democratic administration of the age, by its own description, ran a segregated government, and used federal authority to entrench the color line rather than merely tolerate it.",
              kick='Section A · Race')

# ------------------------------------------------- 7 · SECTION B DIVIDER
divider_photo('dubois-port.jpg', 'Section B', 'The Organized Response',
              ['Shut out of the coalition,', 'Black Americans built their own institutions'],
              "The portrait is W. E. B. Du Bois in 1918, by then the most important Black intellectual in America and the editor of The Crisis. The section's pivot matters as much as its facts. Section A described what was done to Black Americans. Section B describes what they did in answer, and the answer was organization: documentation first, then a movement, then a permanent institution with a legal strategy. Black Americans answered the closing of American politics by building machinery outside it. The reading ends this section with the line students should carry into the unit test and beyond: the organizations the era excluded built the machinery that would dismantle Jim Crow two generations later. Wells, Du Bois, the Niagara Movement, and the NAACP are the guided notes in section B, in that order, and each gets its moment in the next three slides.",
              title_size=44)

# ------------------------------------------------------------ 8 · IDA B WELLS
content_photo_s('wells-port.jpg', 'Ida B. Wells and the record',
              ['Ida B. Wells was a Memphis journalist driven out for telling the truth.',
               'She spent the 1890s documenting lynching, case by case.',
               'Her finding was that lynching was economic terror, not justice.'],
              "Ida B. Wells was a Memphis newspaper editor when, in 1892, three Black grocers she knew were lynched after their store competed successfully with a white rival. She investigated, and she kept investigating for the rest of the decade, compiling names, dates, and stated pretexts from white newspapers themselves, so her evidence could not be dismissed as invention. Her conclusion reversed the era's standard story. Lynching was not rough justice against crime, she showed. It was economic terror, aimed at Black success, Black property, and Black voting, and most victims had been charged with no serious crime at all. A Memphis mob destroyed her press and she was warned not to return, so she continued from the North and from Britain. Teach her method as carefully as her findings. Documentation was the first form the organized response took: an undeniable record, built case by case, that later organizations, the NAACP above all, would carry into court. The guided notes ask for Wells by name, and the reading's account of the response begins with her.",
              kick='Section B · The response')

# ------------------------------------------------------------- 9 · NIAGARA/NAACP
content_photo_s('niagara-port.jpg', 'Niagara to the NAACP',
              ['In 1905, the Niagara Movement demanded full rights now.',
               'Du Bois opposed Washington\u2019s gradualism.',
               'In 1908, a race riot struck Springfield, Illinois.',
               'In 1909, the NAACP was founded, and The Crisis carried its case.'],
              "The photograph shows the Niagara Movement's founders at Fort Erie, Canada, in 1905. They met on the Canadian side of the river because hotels in Buffalo would not house them, a detail students remember. Du Bois and William Monroe Trotter had called the meeting to reject Booker T. Washington's gradualism, the bargain that accepted segregation and disfranchisement in exchange for time to prove economic worth. Niagara demanded full rights now: the vote, enforcement of the Fourteenth and Fifteenth Amendments, and an end to segregation in public life. The movement itself was small and short-lived, but its demands became a program. In 1908 a white mob rioted in Springfield, Illinois, Abraham Lincoln's hometown, and the shock of it brought Black leaders and white allies together to found the NAACP in 1909. Du Bois became its director of publicity and research and editor of The Crisis, the magazine that carried the case to the nation. Students should note the founding coalition: the organization the era's exclusion produced was interracial from its first day, though led increasingly by the people it existed to defend.",
              kick='Section B · The response')

# ------------------------------------------------------------ 10 · LITIGATION
content_text('The weapon was litigation',
             ['The NAACP fought in the courts, case by case and precedent by precedent.',
              'Guinn v. United States (1915) struck down grandfather clauses.',
              'Buchanan v. Warley (1917) blocked a housing segregation ordinance.',
              'The wins were narrow. The machinery was the point.'],
             "Why courts? Put the strategic problem to the class first. The NAACP's constituency could not vote in the states where its rights were most abused, which closed legislatures as a remedy, and Congress had shown for decades that it would not act. Courts at least had to hear an argument and answer it on the record. So the association chose litigation as its weapon and began winning. In Guinn v. United States in 1915, the Supreme Court struck down Oklahoma's grandfather clause as a violation of the Fifteenth Amendment, the very device from section A. In Buchanan v. Warley in 1917, the court blocked Louisville's residential segregation ordinance, which had forbidden Black families to buy homes on majority-white blocks. Both decisions were unanimous. Be honest about the limits: states rewrote rules to evade Guinn, and Buchanan was decided on property rights, not equality. The wins were narrow. What endured was the method and the institution, a legal arm that filed case after case for fifty years until the structure built in section A came down. The reading's second question targets this slide directly.",
             kick='Section B · The response')

# ------------------------------------------------- 11 · SECTION C DIVIDER
divider_photo('immigrants-port.jpg', 'Section C', 'Immigration: The Split',
              ['One movement, two answers', 'Defend the newcomer, or keep him out'],
              "Lewis Hine photographed this immigrant family in the baggage room at Ellis Island, surrounded by everything it owned. Hold the image while you frame the section, because the movement in this unit argued about the people in this photograph, and it argued in both directions. Settlement workers such as Jane Addams, whom students met in Lesson 1, defended immigrant cultures and fought for the newcomers in their neighborhoods. Other progressives, trusting expertise and alarmed by the new immigration from southern and eastern Europe, joined the restriction movement and wrote it into federal law in 1917. The guided notes in section C are built as a split for a reason. Neither side was outside the movement. Both claimed the progressive mantle, one through uplift and protection, the other through expertise and national management, and the section ends where the second logic led when carried furthest: eugenics. The reading's third question asks students to name both positions with evidence for each, so keep the two columns distinct as you teach.",
              title_size=44)

# ------------------------------------------------------ 12 · TWO ANSWERS
content_text('Two answers to the newcomer',
             ['Jane Addams and the settlement houses defended immigrant cultures.',
              'The Dillingham Commission worked from 1907 to 1911 and produced volumes for restriction.',
              'In 1917, Congress imposed a literacy test on immigrants.',
              'The law was enacted over President Wilson\u2019s veto.'],
             "Teach the two columns in turn. On one side, the settlement house progressives. Jane Addams and her allies lived in immigrant neighborhoods, defended immigrant cultures against forced Americanization, and fought for the newcomers in their districts: translation, classes, legal help, and political protection. Their premise was the premise of Lesson 1, that environment, not blood, explained what they saw. On the other side, restriction. Alarmed by the scale of the new immigration from southern and eastern Europe, the federal Dillingham Commission worked from 1907 to 1911 and produced volumes of findings recommending restriction, giving the cause the era's favorite credential, an expert report. In 1917 Congress delivered: the Immigration Act of 1917, in the guided notes' definition the law imposing a literacy test on immigrants, passed over Wilson's veto. Wilson had argued that a literacy test punished the excluded rather than measuring character, and Congress overrode him. Students often assume restriction was progressivism's enemy camp. The harder truth on this slide is that it was one of progressivism's own products, built with the same faith in expertise that built the regulatory commissions of Lesson 4.",
             kick='Section C · Immigration')

# ------------------------------------------------------------ 13 · EUGENICS
content_text('The dark branch: eugenics',
             ['Eugenics turned the era\u2019s faith in science on people.',
              'Indiana passed the first eugenic sterilization law in 1907.',
              'States sterilized people officials deemed unfit.',
              'Officials called it reform.'],
             "Slow down for this slide; it is short in the reading, and it is the section's point. Eugenics was the claim, dressed in the language of biology, that society could be improved by controlling who reproduced, and that some people were unfit to have children. Beginning with Indiana in 1907, states passed eugenic sterilization laws under which officials ordered the sterilization of people they deemed unfit: the poor, the disabled, the institutionalized, disproportionately the same newcomers the restriction movement targeted. The operations were compulsory and irreversible, and they were defended in the era's own vocabulary as public health, efficiency, and reform. Draw the through line for the class explicitly. The expertise that progressives trusted to inspect meat and regulate railroads was a tool, and tools take the purposes of their users. When the experts themselves carried the era's prejudices about blood and stock, expertise did not correct the prejudice. It certified it, and gave it the force of law. This is the split mind of section C carried to its conclusion, and it belongs in students' seminar prep as the limiting case of reform by expertise.",
             kick='Section C · Immigration')

# ------------------------------------------------- 14 · SECTION D DIVIDER
divider_photo('triangle-port.jpg', 'Section D', "Labor's Floor",
              ['Real protections, written after disaster', 'A floor that stayed low'],
              "The photograph is the Triangle Shirtwaist Factory fire of March 25, 1911, which students met in Lesson 1's quick check: 146 workers, most of them young immigrant women, died behind locked doors and at broken fire escapes. It opens this section because New York's factory safety codes, the era's model labor legislation, were written in its ashes. The section's frame comes straight from the reading, and it is the distinction the fourth reading question tests. Working people gained real protections in these years. Hours limits, safety codes, and compensation systems were not nothing; they saved lives measurably. But the floor stayed low, and the courts kept cutting into it. Protection and empowerment are different things. Protection is what the state does for workers. Empowerment is what workers' own organizations can do for themselves. Progressivism delivered the first far more reliably than the second, and students should leave this section able to prove both halves.",
              title_size=44)

# ------------------------------------------------------------- 15 · LABOR WINS
content_text('What workers won',
             ['Muller v. Oregon (1908) upheld hours limits for women.',
              'Factory safety codes followed the Triangle fire.',
              'Workers\u2019 compensation spread to most states.',
              'The Clayton Act spoke up for unions, on paper.'],
             "Give the wins their full weight first; the lesson fails if students hear only the limits. In Muller v. Oregon in 1908, the Supreme Court upheld Oregon's limit on working hours for women, a landmark because the same courts had been striking down labor regulation for a generation. Louis Brandeis defended the law with a brief stuffed with data on what long hours did to women's health, and the argument by evidence, the progressive method itself, won. After Triangle, New York's Factory Investigating Commission rewrote the state's safety law: fire drills, unlocked exits, sprinklers, inspections, the code other states copied. Workers' compensation spread to most states, replacing the old assumed-risk world of Lesson 1 with insurance that paid injured workers without a lawsuit. And the Clayton Act of 1914, Wilson's antitrust law, declared that the labor of a human being is not a commodity and limited the injunctions courts used to break strikes. Samuel Gompers called it labor's Magna Carta. Keep that phrase in the air. The next slide tests whether the parchment held.",
             kick='Section D · Labor')

# ------------------------------------------------------------ 16 · FLOOR GIVES WAY
content_text('Where the floor gave way',
             ['The Keating-Owen child labor law was struck down in 1918.',
              'There was no federal minimum wage.',
              'There was no protected right to organize.',
              'Workers were protected as objects of concern, not empowered as organizations.'],
             "Now the cuts. Congress tried to reach child labor nationally with the Keating-Owen Act of 1916, which barred goods made by children from interstate commerce. In 1918 the Supreme Court struck it down, ruling that production was a state matter beyond Congress's reach, and children went back to the mills until the New Deal era. There was no federal minimum wage at any point in this period, and no protected right to organize: a worker's union existed at the sufferance of employers and judges, and the Clayton Act's fine language on labor proved weaker in court than it read on the page, as judges went on enjoining strikes under it. The reading's sentence is the one to land: the reforms protected workers as objects of concern more reliably than they empowered workers as organizations. A safety code treats a worker as someone to be shielded. A protected right to organize treats a worker as someone with power of his own. Progressivism was generous with the first and stingy with the second, and the guided notes in section D ask students to hold exactly that contrast.",
             kick='Section D · Labor')

# ------------------------------------------------- 17 · SECTION E DIVIDER
divider_photo('prohibition-port.jpg', 'Section E', 'Prohibition',
              ['The era\u2019s final amendment, and its boldest', 'A law against an ordinary habit'],
              "The photograph shows New York Deputy Police Commissioner John A. Leach, at the right, watching agents pour liquor into a sewer after a raid, in the first years of Prohibition enforcement. Students have met this movement before: the temperance campaign of Lesson 3, the WCTU and the Anti-Saloon League, the most disciplined single-issue pressure campaign in American politics to that date. In this section it reaches its goal, and passes it. The Eighteenth Amendment was the era's final amendment and its boldest, the only one aimed not at the structure of government or the conduct of business but at a personal habit shared by tens of millions of Americans. Frame the section's question now, because it is the reading's fifth question and the unit's closing argument: why was Prohibition different in kind from everything else in this unit, and what does its fate, the only repeal in constitutional history, show about the limits of reform itself?",
              title_size=44)

# ------------------------------------------------- 18 · PROHIBITION PASSES
content_text('How Prohibition passed',
             ['The Eighteenth Amendment was ratified in January 1919.',
              'The Volstead Act supplied the enforcement.',
              'Wartime grain conservation helped it through.',
              'The German names on America\u2019s breweries also helped it pass.'],
             "The instruments first, because the test and the guided notes both test them as a pair. The Eighteenth Amendment, ratified in January 1919, is defined in the notes as the amendment banning the manufacture, sale, and transportation of alcohol. The Volstead Act of 1919 is the federal enforcement law for Prohibition, the statute that defined intoxicating liquor, set penalties, and put federal agents on the street. Amendment states the rule; Volstead is the police. Then the timing, which was not accidental. The First World War delivered the amendment its final arguments: grain was needed for food and soldiers, not beer, and wartime conservation made prohibition look patriotic. The great brewing families were German American, Busch, Pabst, Schlitz, and in 1917 and 1918 German names on America's breweries read as enemy names. Add the Anti-Saloon League's decades of district-by-district pressure from Lesson 3, and a cause that had seemed utopian in 1900 was constitutional law by 1919, taking effect a year later. The drys had won everything they asked. The next slide is what winning looked like.",
             kick='Section E · Prohibition')

# ------------------------------------------------------------- 19 · REPEAL STAT
stat('1', 'amendment in American history has ever been repealed',
     'The Twenty-First Amendment repealed the Eighteenth in 1933. Fourteen years of illegal markets and overwhelmed enforcement ended with the Constitution correcting itself.',
     "This statistic is the unit's epitaph, so give it the full pause the format allows. Why did Prohibition fail where other reforms, however flawed, endured? Because it differed in kind. The unit's other reforms regulated industries, structured markets, or widened political participation. They supervised corporations and officials, a few thousand actors the state could watch. Prohibition criminalized a behavior most Americans had considered ordinary, which required policing millions of citizens in their homes, restaurants, and clubs. Enforcement overwhelmed authorities from the first year. Illegal markets enriched organized crime on a national scale, and a generation learned to treat one section of the Constitution as a joke, which corroded respect for the rest. In 1933 the Twenty-First Amendment repealed it, the only amendment ever repealed. Land the lesson in the limits frame: the era that taught Americans the federal government could fix almost anything ended by demonstrating the thing law cannot do, which is legislate a people's morality against its habits.",
     kick='Section E · Prohibition')

# ------------------------------------------------------------- 20 · VOCAB A
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

vocab('Words for the machinery',
      [('grandfather clause', 'a rule exempting voters whose grandfathers could vote, used to disfranchise Black voters while sparing illiterate whites'),
       ('NAACP (1909)', 'the National Association for the Advancement of Colored People, founded to fight segregation and disfranchisement through the courts'),
       ('Immigration Act of 1917', 'law imposing a literacy test on immigrants, passed over Wilson\u2019s veto')],
      "These definitions match the guided notes word for word, so students can copy them directly. A grandfather clause is a rule exempting voters whose grandfathers could vote, used to disfranchise Black voters while sparing illiterate whites; students know it from section A, and it is the device the Supreme Court voided in Guinn. The NAACP (1909) is the National Association for the Advancement of Colored People, founded to fight segregation and disfranchisement through the courts, and students should learn the full name exactly, since the acronym is meaningless without it and the strategy, through the courts, is built into the definition itself. The Immigration Act of 1917 is the law imposing a literacy test on immigrants, passed over Wilson's veto; the definition carries the section's whole story, the test and the override, in one line. Warn students about the confusions the test will probe: grandfather clause belongs to voting, not immigration, and the NAACP dates to 1909, before Wilson, before the war, built in the teeth of the disfranchisement era itself.")

# ------------------------------------------------------------- 21 · VOCAB B
vocab('Words for the last reform',
      [('Eighteenth Amendment (1919)', 'amendment banning the manufacture, sale, and transportation of alcohol'),
       ('Volstead Act (1919)', 'the federal enforcement law for Prohibition')],
      "Two terms only on this slide, and they arrive as a pair, again matching the guided notes exactly. The Eighteenth Amendment (1919) is the amendment banning the manufacture, sale, and transportation of alcohol. The Volstead Act (1919) is the federal enforcement law for Prohibition. Students reliably confuse the two, so give them the handle from the lecture: the amendment is the rule, the Volstead Act is the enforcement. One is in the Constitution, ratified by the states in January 1919. The other is an ordinary statute, passed by Congress the same year, which defined what counted as intoxicating liquor, set the penalties, and sent the agents out. A useful check: if a question asks what banned alcohol, the answer is the amendment. If it asks who chased the bootleggers and under what law, the answer is the Volstead Act. Both dates are 1919, and the pair closes the vocabulary of the whole unit: the last key terms of the last lesson are a ban and the law hired to enforce it.",
      )

# --------------------------------------------------------- 22 · CLOSING HANDOFF
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Seminar prep: how much changed', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Your writing task: build the seminar case for how much Progressivism actually changed, and for whom.'],
     size=23, color=POWDER, leading=1.3)
rows = [('The task', 'Seminar prep: argue a verdict on the era, with evidence'),
        ('Bring', 'One expansion of democracy, one limit, a fact for each'),
        ('Strongest cases', 'Use the distinctions: protection versus power, regulate versus criminalize')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.6, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.6, yy, 8.6, 0.6, d, size=19, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.55, 11.5, 0.7, 'Exit ticket: complete the sentence, name the most serious limit, weigh the NAACP\u2019s separate road.',
     size=16, color=POWDER)
notes(s, "Close by handing the lesson to its writing task, the seminar prep titled How Much Changed, which students hold. The assignment asks them to build a defensible verdict on the whole era, and today's deck was arranged to stock it: an expansion of democracy and a limit, with evidence for each. The strongest seminar cases steal the reading's own distinctions. Protection versus empowerment sorts the labor evidence. Regulating an industry versus criminalizing a habit sorts Prohibition. And section A's federal record answers anyone whose verdict is simply that the era meant well. Before they write, the exit ticket from the guided notes has three items. First, complete the sentence in their own words: Progressivism expanded democracy for a named group, while doing something named, for another. Second, judge which limit in this lesson is most serious and name the evidence that settles it. Third, the NAACP's founders worked largely outside the progressive coalition; students name one advantage and one disadvantage of building a separate organization. Tomorrow is review day, and the blueprint's last two entries, Progressivism and race, and the Eighteenth Amendment and Prohibition, ride on this lesson.")

dc.save(OUT)
