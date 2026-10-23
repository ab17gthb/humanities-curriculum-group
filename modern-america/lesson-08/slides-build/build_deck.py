#!/usr/bin/env python3
"""Modern America Lesson 8 deck, "A Polarized Nation," built to the approved
system: image-led slides, fragments only on screen, comprehensive speaker
notes, full lesson and vocabulary coverage. Fonts: Georgia titles, Lato body."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(HERE, '..'))
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags, photo_right,
                         divider_photo, content_photo, content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED, W, H)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

dc.IMG = os.path.join(HERE, 'img')
OUT = os.path.join(HERE, '..', 'lesson-08-slides.pptx')

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
text(s, 0.9, 5.32, 11.5, 0.4, 'MODERN AMERICA · LESSON 8', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'A Polarized Nation', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'The sorting, the courts, the pandemic, and the arguments the course began with', size=17, color=POWDER)
notes(s, "The photograph shows the Supreme Court Building in Washington, west front, photographed by the Architect of the Capitol in October 2013 after a facade restoration. It opens the closing lesson of the course because the building is where this era argued its largest questions. The country this lesson describes was closely divided, its two parties sorted into hostile camps, and question after question that the political branches could not settle arrived at this Court: an election in 2000, a handgun ban in 2008, campaign spending in 2010, marriage in 2015, and college admissions in 2023. Teach the lesson as the course's closing file. Every modern record in it is paired with an older argument of the course, and the final writing task asks students to judge the whole year from the documents they have read since the founding.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("What divided Americans most deeply in the first decades of the twenty first century, and which of the course's oldest arguments were they still having?", {})]],
     size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the United States remake itself after 1980, in its economy, its population, and its place in the world, and what did the remaking settle and what did it leave open?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "The lesson question has two halves, and students must keep them separate, because the lesson fails when they blur. The first half asks what divided Americans in the years after 2000, and it is answered from the record: a sorted electorate, a presidential election settled by a court, rights and money questions decided five to four, a forty five year argument over remedy in college admissions, and a pandemic answered and argued along the same partisan lines. The second half asks which of the course's oldest arguments those divisions continued, and it reaches back across the whole year: to the founding and its amendments, to the Civil War era and the Fourteenth Amendment, to the New Deal and the federal answer to collapse, and to the movement years and their argument over remedy. The activity, the notebook page, and the writing task all grade the pairing of the two halves.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Sorted, decided, tested, unsettled', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The sorting', 'Parties pull apart; margins narrow to 537 votes'),
        ('B', 'The court settles an election', 'Bush v. Gore, 2000: the recount stops'),
        ('C', 'Two rights decisions', 'Heller 2008; Citizens United 2010'),
        ('D', 'Marriage in every state', 'Obergefell 2015: zero states in 2003, fifty after'),
        ('E', 'The forty five year argument', 'Bakke 1978 to Students for Fair Admissions 2023'),
        ('F', 'The pandemic test', 'CARES Act 2020; more than a million deaths'),
        ('G', 'The machinery tested', '2020 certified; January 6, 2021; the course closes')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "The map follows the guided notes section by section. Section A measures the sorting: parties voting as blocs, counties delivering landslides, split ticket voting shrinking, and an election decided by 537 votes in Florida. Section B states Bush v. Gore, the decision that stopped the recount and settled the election of 2000. Section C takes two rights decisions, Heller on the handgun in the home and Citizens United on independent political spending. Section D follows marriage from zero states licensing it in 2003 to every state required to license it after Obergefell in 2015. Section E runs the forty five year argument over race in admissions from Bakke in 1978 to its close in 2023. Section F tests the system with the pandemic and the CARES Act. Section G states the official record of the election of 2020 and closes the course where it began.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_photo('court-port.jpg', 'Section A', 'The Sorting',
              ['Two hostile camps, fewer voters in the middle,', 'and margins thin enough for a court to decide.'],
              "The photograph is the Supreme Court Building again, this time as a portrait, because the sorting described in this section is what delivered the era's questions to that building. Begin with the definition students will reproduce in the guided notes: political polarization is the sorting of Americans into two hostile political camps with fewer voters in the middle. Insist that the sorting be shown rather than asserted. Roll call records in Congress show the parties voting as blocs more often from the 1990s onward. Survey series show party identity hardening and hostility toward the other camp rising. Counties that once swung between the parties began delivering landslides for one side. Split ticket voting, a ballot for one party's president and the other party's congressman, shrank toward vanishing. A closely divided country is not new in this course; a country sorted so that nearly every contest is close and nearly every institution is contested is the era's own condition.",
              title_size=40)

# ------------------------------------------------------ 5 THE SORTING MEASURED
content_text('The sorting, measured',
             ['Congress: the parties vote as blocs more often',
              'Counties: landslides for one party or the other',
              'Ballots: split ticket voting shrinks',
              'Surveys: party identity hardens, hostility rises',
              '2000: a national count nearly even'],
             "Work the four measures in order and make students say what each one measures. The roll call measure is about institutions: members of Congress sorted into two disciplined parties, with the overlapping middle that once produced cross party coalitions largely gone from the voting record. The county measure is about geography: more Americans lived in counties that voted overwhelmingly for one party, so the lived experience of a contested election disappeared from much of the map, a change the public record of election results documents. The ballot measure is about individual voters, who once split tickets routinely and by this era voted one party up and down the ballot. The survey measure is about feeling: party identity became a stronger marker, and negative views of the other party rose through the series the lesson names. Together the four measures describe one fact from four sides, a country divided into camps before any single issue is named.",
             kick='A · The sorting', size=24)

# ------------------------------------------------------ 6 STAT 537
stat('537 votes', "Florida's certified margin in the election of 2000",
     'A presidency settled inside one state recount · Decided the Electoral College',
     "Give this figure its full weight, because it is the sorting stated as a single number. In November 2000 the two candidates divided the national vote almost evenly, Albert Gore winning the popular vote and George W. Bush the Electoral College, and the whole contest came down to Florida, where the state eventually certified a margin of 537 votes out of nearly six million cast. A margin that small cannot be recounted into certainty; every judgment about a hanging chad or a faint mark moves the total by more than the margin itself. That arithmetic is why the Florida fight moved so quickly from counting rooms to courtrooms, and why the Supreme Court's decision to stop the recount, on the next section's slide, settled a presidency. Teach the number beside the era's other close margins: five to four on the Court itself, in decision after decision of this lesson. The country was not divided between a majority and a minority in these years. It was divided down the middle, and its institutions were built for majorities.",
     kick='A · The sorting')

# ------------------------------------------------- 7 SECTION B DIVIDER
divider_text('Section B', 'The Court Settles an Election',
             'December 12, 2000: five justices stop a recount, and the election of 2000 is over.',
             "Set the scene before the holding, because students meet Bush v. Gore as a slogan and must instead meet it as a procedure. Florida's result was too close to call on election night. State law provided for recounts, the candidates sued over which ballots to count and how, and the Florida Supreme Court ordered a manual recount of the ballots machines had not read, judged by the intent of the voter. The question that reached the United States Supreme Court was narrow and procedural: whether a recount conducted county by county, with no uniform standard for judging intent, treated voters equally under the Constitution. The Court answered on December 12, thirty six days after the election, with the inauguration five weeks away. The holding is on the next slide, in the opinion's own terms, which is how the activity at Station 1 requires students to state it.")

# ------------------------------------------------------ 8 BUSH V GORE
content_text('Bush v. Gore: the recount stops',
             ['The right: equal weight for each vote, equal dignity for each voter',
              'The defect: no uniform standard for judging intent',
              'The holding: the recount violates equal protection',
              'Five to four; the ruling limited to the present circumstances'],
             "State the holding in the opinion's own words, which Station 1 of the activity quotes. The per curiam opinion grounds the right first: when the state legislature vests the right to vote for President in its people, that right is fundamental, and one source of its fundamental nature lies in the equal weight accorded to each vote and the equal dignity owed to each voter. It then finds the defect: the recount mechanisms did not satisfy the minimum requirement for non-arbitrary treatment of voters, because Florida's command to honor the intent of the voter had no specific standards to ensure its equal application, so the same ballot could count in one county and fail in another. The remedy followed: the recount stopped, Florida's certified result stood, and Gore conceded the next day. Close on the sentence students most often omit: our consideration is limited to the present circumstances. The Court itself declined to make the ruling a general rule for recounts, and any account that leaves that sentence out reports a larger decision than the one issued.",
             kick='B · The court settles an election', size=24)

# ------------------------------------------------- 9 SECTION C DIVIDER
divider_photo('justices-port.jpg', 'Section C', 'Two Rights Decisions',
              ['Heller reads the Second Amendment in 2008.', 'Citizens United reads the First in 2010.'],
              "The photograph shows the Roberts Court of 2010, photographed by Steve Petteway for the Collection of the Supreme Court of the United States: the Court that decided Citizens United that year, two years after Heller. Use the portrait to make the section's structure plain. With Congress sorted and legislatures closely divided, the era's ground rules for personal rights and for political money were set by this institution, reading amendments written in 1791. Heller asked what the Second Amendment protects: a right of militias, the dissent argued, or a right of individuals, the majority held. Citizens United asked what the First Amendment forbids: limits on corporate political speech, which the majority held the amendment bars when the spending is independent of a campaign. In both cases the losing side warned that the majority was removing questions from democratic politics. The majority's answer in Heller is the section's key sentence, and it is quoted at Station 2 of the activity: the enshrinement of constitutional rights necessarily takes certain policy choices off the table.",
              title_size=36)

# ------------------------------------------------------ 10 HELLER
content_text('Heller, 2008: the handgun in the home',
             ['The question: a ban on usable handguns in the home',
              'The holding: an individual right to keep a handgun at home',
              'Self-defense named as the right\u2019s core use',
              'The District\u2019s ban and its inoperable rule struck down',
              'Five to four, on the text of 1791'],
             "Teach Heller from its question, which the opinion states in its first line and the activity quotes: whether a District of Columbia prohibition on the possession of usable handguns in the home violates the Second Amendment. The holding follows in the opinion's summary: the District's ban on handgun possession in the home violates the Second Amendment, as does its prohibition against rendering any lawful firearm in the home operable for the purpose of immediate self-defense, and the District had to permit Heller to register his handgun and license it for the home. Two features deserve class time. The first is method: the majority read the amendment's words as its authors' generation used them, and treated that reading as settling a modern city's law. The second is scope: the opinion protected the handgun in the home for self-defense and acknowledged a range of other regulation as lawful, so the holding is narrower than the arguments made about it on either side. State it at the scope the text claims.",
             kick='C · Two rights decisions', size=24)

# ------------------------------------------------------ 11 CITIZENS UNITED
content_text('Citizens United, 2010: money and speech',
             ['The holding: no limits on independent spending',
              'Corporations and unions spend from their own treasuries',
              'Independent of a campaign: the line the holding draws',
              'Super PACs follow; outside spending grows large'],
             "State Citizens United from the definition students carry in the guided notes: the Supreme Court decision of 2010 holding that the government may not limit independent political spending by corporations and unions, which opened the way to super PACs and large outside spending in elections. The majority's reasoning ran through the First Amendment: spending to publish political speech is speech, and the identity of the speaker, a corporation or a union rather than a person, does not remove the protection when the spending is independent of any candidate's campaign. The dissent answered that corporate treasuries could now overwhelm the electoral debate the amendment was meant to keep open. Both positions belong in the lesson, attributed to their makers. The practical consequence is measurable and belongs on the record: committees that may raise and spend unlimited sums independently of candidates, the super PACs, became central spenders in the election cycles that followed, and the argument over money in politics moved from Congress, which had written the limits, to the Court, which had removed them.",
             kick='C · Two rights decisions', size=24)

# ------------------------------------------------- 12 SECTION D DIVIDER
divider_text('Section D', 'Marriage in Every State',
             'In 2003 no state licensed a same sex marriage. In 2015 the Fourteenth Amendment required every state to.',
             "Open the section with the speed of the change, because students who grew up after 2015 often assume the Obergefell settlement was old. In 2003, when this lesson's period was already under way, no state in the Union licensed marriages between two people of the same sex. Massachusetts became the first in 2004, under a ruling of its own supreme court. Other states followed by ruling and by statute, while still others amended their laws and constitutions to forbid such marriages, so the country's map of a basic civil status depended on which side of a state line a couple stood. The question that reached the Supreme Court was whether the Fourteenth Amendment, ratified in 1868, allowed that map to stand. Justice Kennedy's opinion answered for the whole country on June 26, 2015, the same date, two years apart, as the Heller decision in this lesson's previous section, a coincidence students enjoy noticing and a reminder of how much of the era ran through one building.")

# ------------------------------------------------------ 13 OBERGEFELL
content_text('Obergefell, 2015: equal dignity',
             ['Licensing: every state must license same sex marriages',
              'Recognition: marriages from other states must be honored',
              'The ground: the Fourteenth Amendment',
              'The close: equal dignity in the eyes of the law',
              'Five to four'],
             "State Obergefell in its two halves, because the activity at Station 3 tests both and each half does different work. The licensing half: the Court holds that same-sex couples may exercise the fundamental right to marry in all States, so every state must issue the licenses its own law had withheld. The recognition half: there is no lawful basis for a State to refuse to recognize a lawful same-sex marriage performed in another State on the ground of its same-sex character, so a marriage valid where it was celebrated remains valid when the couple crosses a state line. Then read the closing passage aloud, as the station does: the petitioners' hope is not to be condemned to live in loneliness, excluded from one of civilization's oldest institutions; they ask for equal dignity in the eyes of the law, and the Constitution grants them that right. Name the phrase's ancestry for the class: equal dignity is the Civil War era amendment's claim, argued through the movement years, stated here for marriage in 2015.",
             kick='D · Marriage in every state', size=24)

# ------------------------------------------------------ 14 STAT ZERO TO FIFTY
stat('0 to 50', 'states licensing same sex marriage, 2003 to 2015',
     'No state in 2003 · Massachusetts first in 2004 · Every state required after Obergefell',
     "Teach this pair of numbers as the era's fastest change of legal status, and make students account for both ends of it. The zero is a fact of 2003: in the year this century's argument was already raging, not one state issued a marriage license to a same sex couple, and many states had statutes or constitutional provisions against it. The fifty is a fact of June 26, 2015: after Obergefell, every state was required by the Fourteenth Amendment to license such marriages and to recognize those performed elsewhere. Between the two numbers stand twelve years of state politics, rulings, statutes, ballot measures, and reversals, which the decision ended by national ruling rather than by the fiftieth state acting on its own. Set the pair beside the lesson's other numbers: 537 votes, five to four, forty five years. This change took twelve years from none to all; the admissions argument on the next section took forty five years to run from its settlement to its close. The era moved at both speeds at once.",
     kick='D · Marriage in every state')

# ------------------------------------------------- 15 SECTION E DIVIDER
divider_text('Section E', 'The Forty Five Year Argument',
             'Bakke settles the terms in 1978. Students for Fair Admissions closes them in 2023.',
             "This section is where the course's longest thread ends, and students should feel the length of it. The argument over remedy began in this course at Howard University in 1965, where President Johnson argued that the nation should seek equality as a fact and equality as a result, not equality as a right only. Affirmative action turned that argument into policy, ordered for federal contractors in the revised Philadelphia Plan of 1969, in the definition students carry verbatim in this lesson's guided notes. The Civil Rights unit closed with Bakke in 1978, Justice Powell's opinion striking down a set aside of seats and preserving race as one factor among others. That settlement governed American college admissions for forty five years, through reaffirmations and narrowings, until June 29, 2023. The next two slides state the settlement and its close as a pair, which is how Station 4 of the activity presents them and how the key requires them to be read: together, or not at all.")

# ------------------------------------------------------ 16 BAKKE
content_text('Bakke, 1978: the settlement recalled',
             ['Struck down: sixteen of one hundred seats set aside',
              'The ground: disregard of individual rights',
              'Preserved: race as a plus in an applicant\u2019s file',
              'Weighed against all other candidates, never a separate track'],
             "Recall Bakke precisely, because the 2023 decision is unintelligible without both of its halves in view. The restrictive half, in the words Station 4 quotes: the fatal flaw in the Davis medical school's preferential program was its disregard of individual rights as guaranteed by the Fourteenth Amendment, and the set aside of sixteen of one hundred seats fell. The preserving half stands in the same opinion: in a lawful admissions program, race or ethnic background may be deemed a plus in a particular applicant's file, yet it does not insulate the individual from comparison with all other candidates for the available seats. Powell's settlement therefore did two things at once. It forbade the quota, the one remedy that counted results in seats. It preserved the factor, the tool that let admissions officers weigh race among many qualifications. American universities built their admissions systems inside that settlement for two generations of applicants. Students should name the tension the settlement carried from birth: a program aimed at results, judged by a rule stated in individual terms.",
             kick='E · The forty five year argument', size=24)

# ------------------------------------------------------ 17 SFFA
content_text('Students for Fair Admissions, 2023: the close',
             ['The syllabus: strict scrutiny, no stereotype or negative, an end point',
              'The programs fail each criterion',
              'Invalid under the Equal Protection Clause',
              'Six to three, forty five years after Bakke'],
             "State the 2023 holding from the syllabus of the slip opinion, the document Station 4 quotes. The syllabus first recites the terms on which the Court had permitted race based admissions: such programs must comply with strict scrutiny, may never use race as a stereotype or negative, and must, at some point, end. It then applies the terms: respondents' admissions systems fail each of these criteria and must therefore be invalidated under the Equal Protection Clause of the Fourteenth Amendment. The majority's reasoning filled in the three failures: the interests the universities claimed, training leaders and enriching discussion among them, were not measurable enough for a court to review; a plus for some applicants in a fixed class operates as a negative for others; and programs justified by goals without a measure have no logical end point. The dissents answered that the majority had abandoned the Fourteenth Amendment's remedial history. Present both, attributed, and grade only the accuracy with which students state the holding and its grounds.",
             kick='E · The forty five year argument', size=24)

# ------------------------------------------------- 18 SECTION F DIVIDER
divider_photo('vaccine-port.jpg', 'Section F', 'The Pandemic Test',
              ['A virus closes the country in 2020.', 'The federal answer arrives at New Deal scale.'],
              "The photograph shows officials touring the community based vaccination site at Elizabeth High School in Elizabeth, New Jersey, on March 3, 2021, photographed by Kenneth Wilsey of the Federal Emergency Management Agency. A school gymnasium converted to a vaccination center, run with federal support inside a state and city system, is the pandemic response in one image: an emergency administered through every layer of the federal structure at once. Set the scale before the politics. The COVID-19 pandemic reached the United States in 2020, and by the count of the Centers for Disease Control and Prevention it killed more than a million Americans. State orders closed schools, businesses, and public life for months. The federal rescue, the vaccines, and the argument over both are the next slide's subject. Teach the section as a stress test of everything the course has built: the New Deal's machinery, the war powers era's emergency habits, and the sorting of the previous sections, all loaded at once.",
              title_size=38)

# ------------------------------------------------------ 19 PANDEMIC AND CARES
content_photo('vaccine-port.jpg', 'The pandemic and the CARES Act',
             ['More than a million American deaths, by CDC counts',
              'Schools, businesses, and public life closed for months',
              'The CARES Act, March 27, 2020: more than two trillion dollars',
              'Vaccines authorized in under a year',
              'Closures and mandates argued along the sorting\u2019s lines'],
             "Run the section's facts in the order the reading gives them. The disease first, defined in the guided notes: the worldwide spread of the coronavirus disease first identified in 2019, which reached the United States in 2020, killed more than a million Americans, and closed schools, businesses, and public life for months. The count behind the rounded phrase is in the CDC record the activity quotes at Station 5: by April 26, 2023, more than 104 million cases and 1.1 million COVID-19-associated deaths had been reported to the Centers for Disease Control and Prevention. The federal answer came on March 27, 2020, when the CARES Act committed more than two trillion dollars in direct payments, expanded unemployment assistance, and payroll loans. Vaccines followed in under a year under a government backed crash program. The argument over closures, mandates, and emergency power then divided along the lines the sorting had drawn, with supporters crediting the measures with limiting the damage and critics charging that they cost more than they saved. Attribute both claims every time.",
             kick='F · The pandemic test')

# ------------------------------------------------------ 20 STAT DEATHS
stat('1.1 million', 'COVID-19-associated deaths reported to the CDC by April 26, 2023',
     'More than 104 million cases · The count is the Centers for Disease Control and Prevention record',
     "Teach this number as a record, not a rounded phrase, because the lesson's discipline is that even a catastrophe enters the file as a document. The figure comes from the Centers for Disease Control and Prevention, in its Morbidity and Mortality Weekly Report on surveillance after the public health emergency: by April 26, 2023, more than 104 million cases, six million related hospitalizations, and 1.1 million COVID-19-associated deaths had been reported to the CDC and summarized on its COVID Data Tracker. The count passed one million during 2022, which is why the guided notes definition, written for the whole pandemic, says the disease killed more than a million Americans. Give students the comparison the course has prepared them for: the pandemic's American dead exceed the American dead of the Civil War era's armies counted in the same cumulative way, and the federal answer, a statute moving more than two trillion dollars within weeks, was written at a scale only the New Deal and the Second World War had precedented in this course.",
     kick='F · The pandemic test')

# ------------------------------------------------- 21 SECTION G DIVIDER
divider_text('Section G', 'The Machinery Tested',
             'The election of 2020 is certified, disputed, and completed. The course closes on its first arguments.',
             "Close the lesson with the machinery itself under stress, and teach this section under the lesson's strictest discipline: claims attributed to their makers, and the official record stated as the record. The election of 2020 was held during the pandemic and produced the highest turnout in more than a century. Its results were counted, recounted in contested states, certified by officials of both parties, and defended in court, where challenges to the count were rejected in case after case. The president who lost it claimed the election had been stolen, and many of his supporters believed the claim; the official record does not support it. On January 6, 2021, the day Congress counted the electoral votes, a crowd attacked the Capitol and interrupted the count, which was completed that night. The next slide states the record in that form, and the writing task's rubric holds students to the same form: attribution for claims, the record for facts.")

# ------------------------------------------------------ 22 ELECTION 2020
content_text('2020 and January 6: the record stated',
             ['The official record: Biden wins the Electoral College and the popular vote',
              'Certified by officials of both parties; challenges rejected in court',
              'The claim: the election was stolen, made by President Trump and supporters',
              'January 6, 2021: the Capitol attacked; the count completed that night',
              'Hundreds prosecuted and convicted for their parts'],
             "State this slide's content slowly, in the exact form the reading uses, and tell the class why the form is the content. The official record of the election of 2020 is that Joseph Biden won the Electoral College and the popular vote, that state officials of both parties certified their results, and that challenges to the count were rejected in court after court. Against that record stands a claim, attributed to its makers: President Trump and many of his supporters claimed the election had been stolen, a claim the official record does not support. Both sentences belong in an honest account; neither may borrow the other's standing. On January 6, 2021, a crowd that had gathered in Washington attacked the Capitol while Congress counted the electoral votes. The count was completed that night, the transfer of power proceeded on January 20, and hundreds of participants were later prosecuted and convicted for their parts in the attack. No event after 2023 is assigned a settled meaning beyond this record anywhere in the course, and students' verdicts are graded on evidence and attribution, never on the side they take.",
             kick='G · The machinery tested', size=24)

# ------------------------------------------------------ 23 AT A GLANCE
s = slide(NAVY)
kicker(s, 'The unsettled present at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Sorted, decided, tested, unsettled', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The sorting', 'Blocs, landslides, 537 votes', 'Two camps, thin margins, contested institutions'),
        ('Decided', '2000, 2008, 2010, 2015, 2023', 'The Court reads 1791, 1868, and settles'),
        ('Tested', 'CARES Act 2020; 1.1 million deaths', 'Crisis answered at New Deal scale'),
        ('Unsettled', 'Government, rights, membership, place in the world', 'The arguments of 1776, 1861, 1933, 1954, 1968')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.2, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.25, yy + 0.05, 5.1, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.55, yy + 0.05, 3.9, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the closing table of the guided notes, The Unsettled Present at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The sorting: parties voting as blocs, counties delivering landslides, split ticket voting shrinking, and the 537 vote margin of 2000. Decided by courts: Bush v. Gore in 2000, Heller in 2008, Citizens United in 2010, Obergefell in 2015, and Students for Fair Admissions in 2023 closing the Bakke settlement of 1978. Tested by crisis: more than a million American deaths in the pandemic by the CDC count, the CARES Act of March 27, 2020 at more than two trillion dollars, and vaccines authorized in under a year. Still unsettled: the size of government, the reach of rights, the terms of membership in the nation, and the country's place in the world. Grade the table on dates, actors, and holdings stated exactly, not on adjectives.")

# ------------------------------------------------------ 24 VOCAB A
vocab('Words for the sorting and the Court',
      [('political polarization', 'two hostile camps, fewer voters in the middle'),
       ('Bush v. Gore', 'December 2000: the recount stopped, five to four'),
       ('Citizens United', '2010: independent spending may not be limited'),
       ('Heller', '2008: a handgun in the home protected')],
      "These definitions match the guided notes, and the notes carry them in full, word for word. political polarization: the sorting of Americans into two hostile political camps with fewer voters in the middle, visible from the 1990s onward in voting records, media habits, and measures of party identity. Bush v. Gore: the Supreme Court decision of December 2000 that stopped the recount of Florida's presidential ballots and settled the election of 2000 for George W. Bush, decided by five votes to four. Citizens United v. Federal Election Commission: the Supreme Court decision of 2010 holding that the government may not limit independent political spending by corporations and unions, which opened the way to super PACs and large outside spending in elections. District of Columbia v. Heller: the Supreme Court decision of 2008 holding that the Second Amendment protects an individual's right to keep a handgun in the home for self-defense.")

# ------------------------------------------------------ 25 VOCAB B
vocab('Words for marriage, remedy, and the pandemic',
      [('Obergefell v. Hodges', '2015: marriage licensed in every state'),
       ('affirmative action', 'race taken into account to remedy past discrimination'),
       ('COVID-19 pandemic', '2020: more than a million American deaths')],
      "Three more terms, in the guided notes wording, carried in these notes in full, word for word. Obergefell v. Hodges: the Supreme Court decision of 2015 holding that the Fourteenth Amendment requires every state to license marriages between two people of the same sex and to recognize such marriages licensed in other states. affirmative action: government policies that take race into account in hiring, contracting, and college admissions in order to remedy the effects of past discrimination, ordered for federal contractors in the revised Philadelphia Plan of 1969. COVID-19 pandemic: the worldwide spread of the coronavirus disease first identified in 2019, which reached the United States in 2020, killed more than a million Americans, and closed schools, businesses, and public life for months. Notice the dates inside the three definitions: a remedy ordered in 1969 and argued until 2023, a marriage settlement reached in 2015, and a pandemic that arrived in 2020 and tested every institution the other definitions name.")

# ------------------------------------------------------ 26 CLOSING SYNTHESIS
s = slide(NAVY)
kicker(s, 'Closing synthesis')
text(s, 0.9, 1.35, 11.5, 1.1, 'Where this course ends', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 2.6,
     ["The subjects changed across this course: who may vote, who may marry, what the government may spend and forbid, what the country owes to those its laws once wronged.",
      "The arguments did not change their age. They were argued in 1776, 1861, 1933, 1954, and 1968, and the documents of 2000 to 2023 argue them still."],
     size=23, color=POWDER, leading=1.3)
notes(s, "Close the course by stating its ending as a finding in the terms the lesson has used throughout, sorted rather than summed. What changed can be listed and dated: an electorate sorted into two camps, a presidency settled by a court on 537 votes, a handgun right and a spending right read out of the founding amendments, a marriage right read out of the Fourteenth Amendment for all fifty states, a forty five year admissions settlement closed, and a pandemic answered at a scale the New Deal first made thinkable. What did not change can also be listed: the texts being read, from 1791 and 1868; the questions being asked, over the size of government, the reach of rights, the terms of membership in the nation, and the country's place in the world; and the habit of settling them in court when the political branches divide too evenly to settle them themselves. Students should leave able to pair any document of this lesson with the older argument it continues, and to defend the pairing from the document's own words.")

# ------------------------------------------------------ 27 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ["What divided Americans most deeply in the first decades of the twenty first century, and which of the course's oldest arguments were they still having? Pair the modern record with the older arguments, and answer the strongest counterclaim to your own verdict."],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Continuity File: five modern records paired with the arguments they continue'),
        ('Notebook', 'Notebook page: the modern record, the older argument, the evidence for the pairing'),
        ('Quick check', 'The Recount Stops, December 12, 2000: the passage, the margin, the limited ruling'),
        ('Writing', "The Closing Verdict: the course's final claim about what changed and what did not")]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: two decisions defined with their votes, the three grounds of 2023, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close the course by handing the verdict to the students, which is what this lesson exists to do. The activity, The Continuity File, gives them Bush v. Gore from the audited bank record, Heller from the bank record, Obergefell from the bank record, Bakke beside Students for Fair Admissions so the forty five year argument can be read whole, and the CARES Act beside the CDC count, and asks for pairings with the founding, the Civil War era, the New Deal, the movement years, and the conservative turn, then the course's closing verdict with the strongest counterclaim answered. The notebook page charts the pairings. The quick check reads the Bush v. Gore passage and tests whether students can state a holding at the scope its own text claims. The writing task, The Closing Verdict, is the course's final writing task, and it names TPSP premium DBQ number 23 as the linked extension for students who continue. The exit ticket has three parts: two decisions defined with their votes, the three grounds of the 2023 holding with Bakke named, and the lesson question answered with a pairing and a date.")

dc.save(OUT)
