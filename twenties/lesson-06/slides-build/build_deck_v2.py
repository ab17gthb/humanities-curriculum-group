#!/usr/bin/env python3
"""The Twenties Lesson 6 deck, "The Culture Wars," built to the approved
Progressive Era pilot system: image-led slides, fragments only on screen,
comprehensive speaker notes, full lesson + vocabulary coverage.
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
OUT = os.path.join(HERE, '..', 'lesson-06-slides.pptx')

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
text(s, 0.9, 5.32, 11.5, 0.4, 'THE TWENTIES · LESSON 6', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Culture Wars', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Immigration, religion, and science, and the fight over who belonged.', size=17, color=POWDER)
notes(s, "The photograph shows robed Ku Klux Klan members marching in formed ranks through Washington, D.C., on August 8, 1925, photographed by the National Photo Company and held by the Library of Congress. Say only what the record supports: the catalog establishes Washington, D.C., and the date, and contemporary reporting placed the parade on Pennsylvania Avenue. Some 30,000 members marched that day, in daylight, before crowds of spectators. Open the lesson on the fact that this was public and orderly, because that is the point students must sit with. The fights in this lesson were not conducted at the margins. Congress wrote one definition of the American into law, a mass organization marched another down the capital streets, and courts and legislatures fought over which account of the world a school could teach. Two questions organize everything today: who counted as a real American, and whose knowledge counted as true.")

# ------------------------------------------------- 2 · LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.55, 11.5, 3.9, [[('What were the fights over immigration, religion, and science really about: who counted as a real American, and whose knowledge counted as true?', {})]],
     size=40, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the prosperity of the 1920s change American life, and why was that prosperity weaker than it looked?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Read the lesson question slowly, because it has two halves and the exit ticket grades both. The first half is belonging: who counted as a real American. The quota laws, the eugenics testimony, and the second Ku Klux Klan each offered an answer, and each answer placed named groups outside the nation. The second half is knowledge: whose knowledge counted as true. The Butler Act, the trial at Dayton, and the Sacco and Vanzetti case each turned on which account a legislature, a court, or a jury would treat as authoritative. The unit question underneath asks why the prosperity of the 1920s was weaker than it looked. Part of that weakness is here. A decade celebrated for confidence was also deciding, by law and by intimidation, that large parts of its own population did not fully belong in it. Hold both halves of the question in view all hour.")

# --------------------------------------------------- 3 · THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Two fights, one decade', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'Restriction by numbers', 'Congress ranks nations in a quota formula'),
        ('B', 'A science claimed for the border', 'Eugenics testifies in the Capitol'),
        ('C', 'The second Klan', 'A definition of America, sold as a business'),
        ('D', 'Fundamentalism and Dayton', 'A state law decides what a school can teach'),
        ('E', 'Sacco and Vanzetti', 'A court judges two men, and two identities')]
yy = 2.72
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=23, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.6, 0.6, t, size=20, color=CREAM, bold=True)
    text(s, 6.35, yy + 0.06, 6.1, 0.6, d, size=16, color=POWDER)
    yy += 0.70
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Sections A and B cover the border: first the arithmetic of the quota laws, then the claimed science that defended the ranking. Section C takes up the second Ku Klux Klan, which pressed the same definition of the real American in public life and sold membership in it as a business. Section D moves to the schoolroom, where Tennessee law and the trial at Dayton contested whose account of human origins would be taught. Section E closes with Sacco and Vanzetti, two Italian immigrant anarchists whose case forced the country to argue about whether a court had judged evidence or identity. The final table in the guided notes, The Two Fights at a Glance, asks students to sort all five sections under the two halves of the lesson question.")

# ------------------------------------------------- 4 · SECTION A DIVIDER
divider_photo('angel-port.jpg', 'Section A', 'Restriction by Numbers',
              ['Congress closes the door', 'by arithmetic first'],
              "The photograph shows an immigration interview at the Angel Island station in San Francisco Bay in 1923, from the United States Public Health Service photograph file held by the National Archives. A young Chinese immigrant sits alone at a small table answering three officials, two of them in uniform, with papers and a record book on the table between them. Keep the composition in front of students. This is a judgment, not a conversation: one applicant, three representatives of the state, and a file being built. Angel Island enforced the exclusion laws against Chinese arrivals through detailed questioning checked against witnesses. Section A covers the parallel system built for Europeans in the same decade, the quota laws of 1921 and 1924, which decided most cases in advance by fixing how many people of each nationality could come at all.",
              title_size=40)

# ------------------------------------------------------ 5 · TWO LAWS
content_text('Two laws, one direction',
             ['Immigration rose sharply after the First World War.',
              'The Emergency Quota Act of 1921 set each nationality at 3 percent of the census of 1910.',
              'Total admissions were about 357,000 a year under the 1921 law.',
              'The Immigration Act of 1924 cut total admissions to 164,667 a year.',
              'The 1924 law barred nearly all immigration from Asia.'],
             "Give students the sequence before the formula, because section A of the guided notes tests both laws in order. Immigration rose sharply after the First World War, and Congress moved to close the door. The Emergency Quota Act of 1921 limited each nationality to 3 percent of the people born in that country and counted in the census of 1910, with total admissions of about 357,000 a year. The Immigration Act of 1924, known as the National Origins Act, cut much deeper, and total admissions fell to 164,667 a year. The same law barred nearly all immigration from Asia by excluding aliens who were ineligible for citizenship. Note the method. No official had to argue that any individual applicant was unfit. The law sorted nations first, and individuals were admitted or refused inside a ranking that had already been set. The next slide shows what the ranking did to particular countries.",
             kick='A · Restriction by numbers')

# ------------------------------------------------------ 6 · QUOTA STAT
stat('51,227', 'places a year for Germany under the 1924 law',
     'Italy received 3,845 places a year, Russia 2,248, and Greece the minimum of 100. Great Britain and Northern Ireland received 34,007.',
     "Dwell on the contrast, because these figures are the evidence the exit ticket and the writing task both require. Under the National Origins Act, Germany received 51,227 places a year and Great Britain and Northern Ireland 34,007, while Italy received 3,845, Russia 2,248, and Greece the minimum of 100. Do the division aloud: roughly thirteen Germans could enter for each Italian. Then ask where the ranking happened. It happened in one choice inside the formula. The act set each country quota at 2 percent of its foreign born counted in the census of 1890. That census reached back to a time before the great movement from southern and eastern Europe, so northern and western Europe received large quotas and the newer source countries received very small ones. The choice of 1890 was the policy. The arithmetic ranked nations before any individual was judged.",
     kick='A · Restriction by numbers')

# ------------------------------------------------------ 7 · JUDGED IN ADVANCE
content_photo('ellis-port.jpg', 'Judged in advance',
              ['European cases were decided by the formula before arrival.',
               'The quota fixed how many people of each nationality could come.',
               'Officials at the station applied a decision already made.',
               'An exhausted quota ended a case regardless of the person.'],
              "The photograph shows a group of immigrants outside a building on Ellis Island in New York Harbor, from the National Archives. Use it to make the procedural point that section A ends on. For Asian arrivals, judgment happened face to face, as the Angel Island interview showed. For Europeans, the decisive judgment happened earlier and at a distance, inside the quota formula itself. By the time an Italian, Polish, or Greek applicant reached a station like this one, Congress had already fixed how many people of that nationality could enter in a year, and an exhausted quota ended the case regardless of the person standing there. That is what the reading means by ranking nations before any individual was judged. Ask students to hold this photograph next to the quota table in the activity. The table is the decision. The people in the photograph are the ones the decision was about.",
              kick='A · Restriction by numbers')

# ------------------------------------------------- 8 · SECTION B DIVIDER
divider_text('Section B', 'A Science Claimed for the Border',
             'The ranking defended as a finding, not a preference.',
             "Pause here and name what section B adds to section A. The quota formula ranked nations, but a ranking stated as national preference could be argued with as politics. Supporters therefore defended the ranking as science. Eugenics claimed that ability and character were inherited and that human groups could be ranked by ancestry. That claim, presented by credentialed experts in congressional hearings and in a widely read book, let exclusion be described as a conclusion drawn from evidence. Two cautions belong on the record before students meet the names. Some scientists of the day disputed the eugenics findings, and later research discarded them. Neither caution was hidden then or later. The point for this lesson is narrower: in the 1920s the ranking carried the authority of expert testimony in the Capitol itself, and that authority is what the next two slides examine.")

# ------------------------------------------------------ 9 · EXPERTS IN THE CAPITOL
content_text('Experts in the Capitol',
             ['Eugenics claimed that ability and character were inherited.',
              'Harry Laughlin of the Eugenics Record Office served as expert agent to the House committee.',
              'Laughlin presented figures on immigrants in prisons and asylums.',
              'Madison Grant praised northern Europeans in The Passing of the Great Race in 1916.',
              'Grant warned against mixture with other peoples.'],
             "Two names carry this section, and the guided notes test both. Harry Laughlin of the Eugenics Record Office served the House immigration committee as an expert agent, and he presented figures arguing that the newer immigrants filled prisons and asylums at higher rates than the older stock. Madison Grant, in his 1916 book The Passing of the Great Race, praised the supposed virtues of northern Europeans and warned against mixture with other peoples. Put the guided notes definition beside both men. Eugenics is a movement that claimed ability and character were inherited and could be ranked by ancestry, and that argued government should favor the groups it ranked high and restrict the groups it ranked low. Laughlin supplied the testimony and Grant supplied the argument in print. Between them, a passport became, in the reading phrase, a measure of a person, and the quota tables wrote that treatment into federal law.",
             kick='B · A science claimed for the border')

# ------------------------------------------------------ 10 · WHY THE LABEL MATTERED
content_text('Why the science label mattered',
             ['A preference can be debated as politics.',
              'A finding arrives as expert testimony and data.',
              'Supporters could cite the finding in debate as fact.',
              'The findings were disputed at the time and discarded by later research.',
              'In the 1920s, the ranking carried authority in Congress.'],
             "This slide states the analytical point of section B, so slow down. Simple prejudice could not do what eugenics did for the quota system. A claim delivered as expert testimony and data could be cited in debate as fact, which let supporters describe exclusion as a conclusion drawn from evidence rather than as a choice about who belonged. The setting did part of the work. Laughlin did not publish pamphlets from outside the process; he served the House immigration committee itself as an expert agent, inside the room where the law was drafted. Keep the record honest in both directions. The findings were disputed by some scientists at the time, and later research discarded them. Students should not leave believing the science was settled and then overturned by fashion. It was contested when it was used, and it was used anyway, because it gave a ranking Congress already wanted the standing of a discovery.",
             kick='B · A science claimed for the border', size=25)

# ------------------------------------------------- 11 · SECTION C DIVIDER
divider_photo('klan-port.jpg', 'Section C', 'The Second Klan',
              ['Founded in 1915', 'Strong far beyond the South'],
              "The photograph is the same Washington, D.C., parade that opened the lesson, seen from above: National Photo Company, August 8, 1925, Library of Congress. The catalog supports Washington, D.C., and the date; it does not by itself name the avenue. Describe the image factually and without adornment. Robed members march in formed ranks down a wide street while crowds watch from the sidewalks. The order staged this display in the capital to present itself as part of American public life. Section C covers what the second Ku Klux Klan was as an organization: founded in 1915, sold by professional promoters, claiming to defend white Protestant America, and using parades, boycotts, intimidation, and violence against the groups it declared enemies. It also covers how the order fell, which happened from inside, through scandal rather than defeat.",
              title_size=40)

# ------------------------------------------------------ 12 · SOLD LIKE A BUSINESS
content_photo_s('klan-port.jpg', 'Sold like a business',
             ['William J. Simmons founded the second Klan on Stone Mountain in Georgia in 1915.',
              'The film The Birth of a Nation glorified the first Klan that same year.',
              'Recruiters called kleagles kept part of each ten dollar initiation fee.',
              'Members bought their robes from a Klan supplier.',
              'Growth produced income for the organization and its recruiters.'],
             "Begin with the founding and the money, because the guided notes test the mechanics. The second Ku Klux Klan was founded in 1915 by William J. Simmons on Stone Mountain in Georgia, in the same year that the film The Birth of a Nation glorified the first Klan. Professional promoters then sold it as a business. Recruiters called kleagles kept part of each ten dollar initiation fee, and members bought their robes from a Klan supplier, so recruitment paid the recruiter and growth paid the organization. Then state the definition the order gave itself, in the guided notes words. The Ku Klux Klan is the organization revived in 1915 that claimed to defend white Protestant America and used intimidation and violence against Black Americans, Catholics, Jews, immigrants, and others it declared un-American. The business model and the declared enemies belong in one breath: the definition was the product being sold.",
             kick='C · The second Klan')

# ------------------------------------------------------ 13 · DAYLIGHT, THEN COLLAPSE
content_text('Daylight, then collapse',
             ['The declared enemies included Catholics, Jews, immigrants, bootleggers, and Black Americans.',
              'The order used parades, boycotts, intimidation, and violence.',
              'Membership estimates at the peak run into the millions.',
              'The order was strong in Indiana, Ohio, and Oregon as well as in the South.',
              'Some 30,000 members marched in Washington on August 8, 1925.',
              'D. C. Stephenson was convicted of murder in 1925 and then exposed officials from prison.'],
             "Two facts correct the picture students bring in. First, the second Klan was national. Membership estimates for the peak years run into the millions, and the order was strong in Indiana, Ohio, and Oregon as well as in the South. Second, it operated in the open: on August 8, 1925, some 30,000 members paraded in Washington, D.C. The collapse came from inside. Indiana Grand Dragon D. C. Stephenson was convicted of murder in 1925 in the death of Madge Oberholtzer, and from prison he exposed the officials he had worked with. Membership fell away through the rest of the decade. Draw the conclusion plainly. The order was not defeated in argument at its peak. It was discredited by the conduct of one of its own leaders and by the corruption he documented, which is a weaker ending than students expect and the one the record supports.",
             kick='C · The second Klan', size=23)

# ------------------------------------------------- 14 · SECTION D DIVIDER
divider_photo('scopes-port.jpg', 'Section D', 'Fundamentalism and the Trial at Dayton',
              ['A law for the schoolroom', 'A trial the nation read about'],
              "The photograph shows the outdoor proceedings of the Scopes trial on July 20, 1925, taken by Watson Davis of Science Service and held by the Smithsonian Institution Archives. William Jennings Bryan sits at left center in a bow tie; Clarence Darrow stands at the right edge of this crop, questioning him, with the crowd behind the platform. The session sat outdoors because of the heat and the crowd. Section D covers the fight that produced this scene. The movement, fundamentalism, defended a literal reading of the Bible against both modern theology and modern science, and its supporters wrote that defense into Tennessee law. A young teacher agreed to test the law, two of the most famous public men in America took opposing sides, and for one afternoon the contest over whose knowledge counted as true was conducted in public, on the record, between the two of them.",
              title_size=34)

# ------------------------------------------------------ 15 · A LAW FOR THE SCHOOLROOM
content_text('A law for the schoolroom',
             ['Tennessee passed the Butler Act in March 1925.',
              'The Butler Act made teaching human descent from a lower order of animals a crime.',
              'The ACLU offered to defend a test case.',
              'John Scopes, a young Dayton teacher, agreed to stand trial.',
              'Clarence Darrow led the defense and William Jennings Bryan joined the prosecution.'],
             "Set the legal frame precisely, because the guided notes test each element. Fundamentalism is a Protestant movement that defended a literal reading of the Bible and opposed public school teaching that conflicted with it. Against it stood evolution, the scientific theory that species change over generations and that present species, including human beings, developed from earlier forms of life. Tennessee passed the Butler Act in March 1925, which made it a crime for a public school teacher to teach that human beings had descended from a lower order of animals. The American Civil Liberties Union offered to defend a test case, and John Scopes, a young teacher in Dayton, agreed to stand trial. Clarence Darrow led the defense. William Jennings Bryan, three times a candidate for president, joined the prosecution. Note what the law did: a legislature had decided, in advance, which account of human origins a public school could treat as true.",
             kick='D · Fundamentalism and Dayton', size=24)

# ------------------------------------------------------ 16 · JULY 20, OUTDOORS
content_photo('scopes-port.jpg', 'July 20, outdoors',
              ['The judge barred most scientific testimony.',
               'The session moved outdoors because of the heat and the crowd.',
               'Darrow questioned Bryan as an expert on the Bible.',
               'Bryan conceded that the days of creation could be periods.',
               'The days were not necessarily twenty four hour days.'],
              "The photograph is the session this slide describes, taken by Watson Davis on July 20, 1925, and held by the Smithsonian Institution Archives: Bryan seated at left center in his bow tie, Darrow standing at the right edge of this crop, the crowd behind the platform. Reconstruct why the exchange happened at all. The judge barred most scientific testimony, which removed the defense evidence about evolution itself. What remained was the Bible, and Darrow called Bryan as an expert on it. Under questioning about Genesis, Bryan conceded that the days of creation could be periods rather than twenty four hour days. Mark exactly what that concession did. The case rested on a literal reading of the Bible account, and the prosecution own Bible authority, on the stand, read its central word nonliterally. Newspapers across the country printed the exchange, which is why it reached further than anything else in the trial.",
              kick='D · Fundamentalism and Dayton')

# ------------------------------------------------------ 17 · AFTER DAYTON
content_text('What the verdict did not settle',
             ['The jury convicted Scopes and fined him 100 dollars.',
              'Bryan died in Dayton five days after the trial ended.',
              'The Tennessee Supreme Court upheld the law.',
              'The court reversed the conviction on a technicality in the fine.',
              'The public meaning of the trial outlasted the legal result.'],
             "Separate the legal result from the public result, because the guided notes and the quick check both turn on the difference. The jury convicted Scopes and he was fined 100 dollars. Bryan died in Dayton five days after the trial ended. The Tennessee Supreme Court later upheld the law but reversed the conviction on a technicality in the fine. Legally, the Butler Act stood and its only defendant walked away from the fine. Publicly, the trial had already done its work. The July 20 exchange fixed the meaning of Dayton in the national press as a contest over whose account of human origins would be taught, with the strict literal position weakened by its own champion. Neither side won the decade outright. The law survived, the conviction did not, and the argument about knowledge and authority in the schoolroom continued long after both famous men had left the platform.",
             kick='D · Fundamentalism and Dayton', size=24)

# ------------------------------------------------- 18 · SECTION E DIVIDER
divider_photo('sacco-port.jpg', 'Section E', 'Sacco and Vanzetti',
              ['Two men in a Massachusetts prison', 'A verdict the world argued about'],
              "The photograph shows Bartolomeo Vanzetti, at left, handcuffed to Nicola Sacco at the Superior Court in Dedham, Massachusetts, held by the Boston Public Library. Two disclosures belong with it, and students should hear both. The photograph dates from 1923, during the appeals period. It does not show the 1921 trial, and no caption in this lesson claims that it does. This crop centers on Vanzetti, the man whose words close the lesson; Sacco is present at the right edge, joined to him by the handcuffs between them. Section E covers the case itself: a payroll robbery and double murder in 1920, the arrest and conviction of two Italian immigrant anarchists on disputed evidence, six years of denied appeals, and an execution in 1927 that drew protests across Europe and Latin America.",
              title_size=40)

# ------------------------------------------------------ 19 · ARREST AND CONVICTION
content_photo_s('sacco-port.jpg', 'Arrest and conviction',
             ['A paymaster and his guard were shot in South Braintree on April 15, 1920.',
              'Nicola Sacco and Bartolomeo Vanzetti were arrested on May 5, 1920.',
              'Both men were Italian immigrants and anarchists.',
              'Both men were carrying guns and gave false answers early on.',
              'A Dedham jury convicted both men of murder on July 14, 1921.',
              'The trial before Judge Webster Thayer turned on disputed identification and firearms evidence.'],
             "Give the facts in order, including the facts that cut against the defense, because the lesson asks students to weigh them. On April 15, 1920, robbers shot and killed a paymaster and his guard during a payroll robbery in South Braintree, Massachusetts. On May 5, police arrested Nicola Sacco, a shoemaker, and Bartolomeo Vanzetti, a fish seller. Both were Italian immigrants and anarchists, and anarchism is a political belief that government and all ruling authority should be abolished and society organized without a state. Both men were carrying guns when arrested, and both gave false answers under early questioning, which they later explained as fear of arrest for their political activity. A jury at Dedham convicted both men of murder on July 14, 1921, in a trial before Judge Webster Thayer that turned on disputed identification and firearms evidence.",
             kick='E · Sacco and Vanzetti', size=19)

# ------------------------------------------------------ 20 · SIX YEARS, THEN AUGUST 23
content_text('Six years, then August 23',
             ['Appeals ran for six years and all were denied.',
              'Protests had spread across Europe and Latin America by 1927.',
              'The Lowell committee reported that the evidence supported the verdict.',
              'Governor Fuller refused clemency.',
              'Vanzetti said at sentencing that he suffered as a radical and as an Italian.',
              'Both men were executed on August 23, 1927.'],
             "Trace the review sequence as a pattern, because the activity asks students to name it. Appeals ran for six years and all were denied. By 1927 the case had drawn protests across Europe and Latin America. Governor Alvan Fuller appointed a committee headed by Harvard president A. Lawrence Lowell, which reported that the evidence supported the verdict, and Fuller refused clemency. Every reviewing body, the trial judge, the state supreme court, the Lowell committee, and the governor, confirmed the body before it. At sentencing, Vanzetti told the court that he was suffering because he was a radical and because he was an Italian. That sentence is the case in the form the lesson studies. Vanzetti named two grounds, his beliefs and his birth, and left the robbery out entirely, arguing that the court had judged who the men were rather than what the evidence showed. Both men were executed on August 23, 1927.",
             kick='E · Sacco and Vanzetti', size=23)

# ------------------------------------------------------ 21 · THE TWO FIGHTS AT A GLANCE
s = slide(NAVY)
kicker(s, 'The two fights at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'One fight over definition', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Belonging', 'Congress set quotas by the census of 1890; the Klan pressed the same definition in public', 'Southern and eastern Europeans, Asians, Catholics, Jews, and Black Americans placed outside'),
        ('Belief', 'State law and courts decided what schools could teach and what a jury would credit', 'Teachers of evolution and two anarchist defendants placed outside')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, The Two Fights at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The belonging row joins sections A, B, and C. Congress decided who could enter through the quota formula, eugenics testimony supplied the ranking with a claimed scientific basis, and the Klan pressed the same definition of the real American in public life. The people placed outside were southern and eastern Europeans, Asians, Catholics, Jews, immigrants, and Black Americans, on the claim that ancestry determined worth and loyalty. The belief row joins sections D and E. State legislatures and courts decided what could be taught and whose testimony counted, and the people placed outside were teachers of evolution and two anarchist defendants. Grade the table generously on wording and strictly on the sorting: each entry must name who decided, how, and who was placed outside.")

# ------------------------------------------------------ 22 · VOCAB A
vocab('Words for the border',
      [('quota system', 'a method of limiting immigration by setting a fixed maximum number of immigrants that may be admitted from each country in a year'),
       ('National Origins Act', 'the federal immigration law of 1924 that set each country quota at 2 percent of its people counted in the census of 1890 and barred nearly all immigration from Asia'),
       ('eugenics', 'a movement that claimed ability and character were inherited and could be ranked by ancestry, and that argued government should favor the groups it ranked high and restrict the groups it ranked low')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. A quota system: a method of limiting immigration by setting a fixed maximum number of immigrants that may be admitted from each country in a year. The definition names the mechanism, a fixed maximum per country, and section A showed the mechanism at work. The National Origins Act: the federal immigration law of 1924 that set each country quota at 2 percent of its people counted in the census of 1890 and barred nearly all immigration from Asia. Every element of that definition was tested today, the year, the rate, the census, and the Asia bar. Eugenics: a movement that claimed ability and character were inherited and could be ranked by ancestry, and that argued government should favor the groups it ranked high and restrict the groups it ranked low. Note the second half of the definition. Eugenics was not only a claim about inheritance; it was a program for government action.")

# ------------------------------------------------------ 23 · VOCAB B
vocab('Words for the street and the schoolroom',
      [('Ku Klux Klan', 'the organization revived in 1915 that claimed to defend white Protestant America and used intimidation and violence against Black Americans, Catholics, Jews, immigrants, and others it declared un-American'),
       ('fundamentalism', 'a Protestant movement that defended a literal reading of the Bible and opposed public school teaching that conflicted with it')],
      "Two more terms, again matching the guided notes exactly. The Ku Klux Klan: the organization revived in 1915 that claimed to defend white Protestant America and used intimidation and violence against Black Americans, Catholics, Jews, immigrants, and others it declared un-American. Unpack the definition in order. Revived in 1915 separates the second Klan from the organization of Reconstruction. Claimed to defend records the order self description as a claim, not as a fact this course endorses. The list of targets is part of the definition, because the breadth of that list, well beyond Black Americans, is what made the second Klan a national movement of the 1920s rather than a regional survival. Fundamentalism: a Protestant movement that defended a literal reading of the Bible and opposed public school teaching that conflicted with it. Literal is the load bearing word. The Butler Act, the Dayton trial, and Bryan concession all turn on what a literal reading required and whether its own defender could hold it on the stand.")

# ------------------------------------------------------ 24 · VOCAB C
vocab('Words for the theory and the belief',
      [('evolution', 'the scientific theory that species change over generations and that present species, including human beings, developed from earlier forms of life'),
       ('anarchism', 'a political belief that government and all ruling authority should be abolished and society organized without a state')],
      "The last two terms, again matching the guided notes word for word. Evolution: the scientific theory that species change over generations and that present species, including human beings, developed from earlier forms of life. The Butler Act was written against exactly the human clause of that definition; the Tennessee law named descent from a lower order of animals, not change in species generally, which is why a biology teacher and not a geology teacher stood trial. Anarchism: a political belief that government and all ruling authority should be abolished and society organized without a state. Students need the definition stated neutrally and precisely, because the Sacco and Vanzetti case turns on the distance between holding this belief and committing a murder. The prosecution and the defense argued about exactly that distance for six years. A belief can be unpopular, and can be named accurately, without being evidence of a crime, and Vanzetti sentencing statement asked the court to admit that the two had been merged.")

# ------------------------------------------------------ 25 · CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['What were the fights over immigration, religion, and science really about? Build the answer from both fights, belonging and belief.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Belonging Docket: work your half, teach it, then rank all six stations'),
        ('Notebook', 'Notebook page: the five fights in one chart, kept for review day'),
        ('Quick check', 'The Interview and the Verdict: Angel Island, the quotas, Dayton, Vanzetti'),
        ('Writing', 'Who Counted, and Whose Knowledge Counted: the lesson question as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the census year 1890, the Bryan concession, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Belonging Docket, is a jigsaw: half the class works the restriction case and half works the belief case, each student teaches the other half, and pairs then rank all six stations by how strongly each shows what the fights were about. The notebook page collects all five fights into one chart that returns on review day. The quick check, The Interview and the Verdict, tests the Angel Island photograph, the quota arithmetic, the Bryan concession, and the Vanzetti statement. The writing task, Who Counted, and Whose Knowledge Counted, turns the lesson question into an essay of about 300 words using at least three pieces of evidence, at least one from each half. The exit ticket has three parts: why the census year 1890 did the work of restriction, the concession Bryan made and why it weakened his position, and the lesson question answered in two or three sentences with one fact about belonging and one about belief.")

dc.save(OUT)
