#!/usr/bin/env python3
"""Civil Rights Lesson 8 deck, "Victory, Backlash, and the Unfinished Agenda,"
built to the approved system: image-led slides, fragments only on screen,
comprehensive speaker notes, full lesson and vocabulary coverage.
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
text(s, 0.9, 5.32, 11.5, 0.4, 'THE CIVIL RIGHTS MOVEMENT · LESSON 8', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Victory, Backlash, and the Unfinished Agenda', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'The last statute, the shelved diagnosis, the courts, and Bakke, 1968 to 1978', size=17, color=POWDER)
notes(s, "The photograph shows President Lyndon B. Johnson signing the Civil Rights Act of 1968 in the East Room of the White House on April 11, 1968, photographed by Yoichi Okamoto, the president's official photographer, in a Johnson Library record. It opens the unit's final lesson because a signing is both an ending and a question. The statute on the desk completed the movement's legislative work, three great acts in four years, and it was signed one week after the assassination of Martin Luther King Jr., in a capital still smelling of smoke from the uprisings. Teach this lesson as a reckoning rather than a celebration or a lament. The reading, the activity, and the writing task all ask students to sort the same record three ways: what the movement won, what answered it, and what was still undone when the famous decade ended in 1978.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("What did the movement win, what answered it, and what was still undone when its famous decade ended?", {})]],
     size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the civil rights movement change American law and American life, and what did it leave unfinished?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question is the unit's question brought down to one decade's end, and it has three parts that students must keep separate, because the lesson fails when they blur. What did the movement win is a question about the record of law and office: the Fair Housing Act of 1968, the thousands of Black officials the voting law produced, and a Supreme Court still willing in 1971 to order busing. What answered it is a question about reaction: a shelved commission report, George Wallace carrying five states, a southern strategy in the White House, and a court that by 1974 stopped a remedy at a city line. What was still undone is a question about the distance between a right announced and a result delivered, the distance President Johnson named at Howard University in 1965. The writing task grades the sorting and the weighing together.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Won, answered, decided, left undone', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The last statute', 'Fair Housing Act signed April 11, 1968'),
        ('B', 'The diagnosis', 'Kerner: two societies, separate and unequal'),
        ('C', 'The harvest in office', 'A few hundred officials to past five thousand'),
        ('D', 'The backlash organized', 'Wallace, the southern strategy, 1968'),
        ('E', 'The courts become the ground', 'Swann 1971; Milliken stops at the city line, 1974'),
        ('F', 'The movement widens', 'Delano; the methods and tools borrowed'),
        ('G', 'The argument over remedy', 'Philadelphia Plan 1969; Bakke 1978')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "The map follows the guided notes section by section. Section A covers the last statute, the Fair Housing Act signed in the week after the assassination with the weakest enforcement of the three great acts. Section B sets the Kerner Commission's diagnosis beside it, two societies moving apart, with its remedies shelved. Section C counts the harvest in office, Black officials rising from a few hundred toward five thousand and beyond, with mayors in Cleveland, Gary, Atlanta, and Detroit. Section D organizes the backlash, Wallace in 1968 and the southern strategy that won the presidency. Section E moves the argument into the courts, Swann upholding busing in 1971 and Milliken stopping Detroit's remedy at the city line in 1974. Section F follows the movement's tools into other hands, with Delano as the bridge. Section G closes on remedy, from the Philadelphia Plan to the Bakke settlement of 1978.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_photo('signing-port.jpg', 'Section A', 'The Last Statute',
              ['April 11, 1968: the Fair Housing Act signed,', 'one week after the assassination in Memphis.'],
              "The photograph is the signing itself, President Johnson in the East Room on April 11, 1968, from the Johnson Library record by Yoichi Okamoto. Begin with the bill's history, because the date is unintelligible without it. An open housing bill had been debated in Congress for two years and had gone nowhere; fair housing was the demand the movement's northern campaigns, above all Chicago in 1966, had failed to win by protest. What changed was not the argument but the week. King was assassinated in Memphis on April 4 while supporting the sanitation workers' strike. Uprisings followed in more than a hundred cities, troops guarded the Capitol, and Congress completed the bill within days. The lesson's first finding is about how the last statute passed: the movement's legislative monument was finished by crisis, and the terms on which it passed, above all its enforcement, bear the marks of that hurry.",
              title_size=34)

# ------------------------------------------------------ 5 THE LAST STATUTE
content_photo_s('signing-port.jpg', 'A right announced, weakly armed',
             ['It was the third great act, after the acts of 1964 and 1965.',
              'Discrimination in the sale and rental of housing was banned.',
              'The housing department could investigate complaints and use persuasion.',
              'It could not order a violator to stop.',
              'The other route was a private lawsuit, brought at personal expense.'],
             "Read the enforcement clauses slowly, because students assume a ban enforces itself and this act is the unit's standing correction. The Civil Rights Act of 1968 made it unlawful to refuse to sell or rent, to refuse to negotiate, or to discriminate in the terms of a sale or rental because of race, color, religion, or national origin, in the statute's own words, which students meet at Station 1 of the activity. Against a violation, the Department of Housing and Urban Development could receive a complaint, investigate it, and use conference and persuasion. It held no power to issue an order. A family turned away from a house could also sue, paying a lawyer to enforce a federal right. Compare the machinery of the earlier acts, federal examiners under the Voting Rights Act and fund cutoffs under the act of 1964, and let students name the difference themselves: this right was announced to the whole country and armed for the households who could afford to use it.",
             kick='A · The last statute', size=19)

# ------------------------------------------------- 6 SECTION B DIVIDER
divider_text('Section B', 'The Diagnosis',
             'March 1, 1968: the president is told his nation is moving toward two societies, and shelves the prescription.',
             "Set the commission's origin before its verdict, because its authority came from who appointed it and what it was asked. After the uprisings of the summer of 1967, in Newark and Detroit above all, President Johnson appointed the National Advisory Commission on Civil Disorders, chaired by Governor Otto Kerner of Illinois, and directed it to answer three questions: what happened, why it happened, and what could be done to prevent it from happening again. Johnson expected, on the record his aides kept, a report that would blame a small band of agitators and praise his administration's programs. The commission instead investigated for seven months and reported on March 1, 1968, five weeks before the signing on the previous slides. Its conclusion indicted the country that had commissioned it. Johnson received the report coldly and never acted on its program. Students should hold both facts: the diagnosis was official, and it was refused by the official who ordered it.")

# ------------------------------------------------------ 7 TWO SOCIETIES
content_text('Two societies, separate and unequal',
             ['Its basic conclusion was stated in the report\u2019s own words.',
              'White institutions created the ghetto.',
              'White institutions maintain it, and white society condones it.',
              'The remedy proposed jobs, housing, and education at scale.',
              'Its remedies were shelved rather than delivered.'],
             "Take the conclusion in its three movements, quoting the bank record as the activity does. First the prediction: the nation is moving toward two societies, one black, one white, separate and unequal, and reaction to the disorders was quickening the movement apart. Second the responsibility, stated in three verbs students will be asked to reproduce: white institutions created the ghetto, white institutions maintain it, and white society condones it. Third the prescription: large federal programs in employment, housing, and education, on a scale the commission compared to the nation's other great undertakings. Then the fate. The president who had signed the two earlier acts declined this one; the recommendations were shelved, and the report reached the country as a paperback bestseller rather than as policy. A diagnosis read by hundreds of thousands and enacted by no one is this lesson's clearest specimen of the unfinished agenda, dated five weeks before the last statute was signed.",
             kick='B · The diagnosis', size=24)

# ------------------------------------------------- 8 SECTION C DIVIDER
divider_text('Section C', 'The Harvest in Office',
             'The ballot the movement protected begins to staff the government it had petitioned.',
             "Turn from paper to people, because this section counts what the statutes produced in personnel, and the count is the strongest single evidence on the winning side of the ledger. The Voting Rights Act of 1965 sent federal examiners into the covered South and suspended the literacy tests that had kept Black registration in Mississippi under seven percent. Registration rose, and office followed registration with a short lag, first in the courthouse offices of the Black Belt and then in the mayor's offices of the great cities. Teach the sequence as cause and effect, with dates attached at each step, because students who meet the numbers as a celebration miss the mechanism: a federal law changed who could vote, the changed electorate changed who could win, and the winners changed what city governments defended. The backlash of the next section is unintelligible unless students first see how much had actually been won, and how visibly.")

# ------------------------------------------------------ 9 OFFICEHOLDERS
content_text('From petitioners to officeholders',
             ['In 1965, a few hundred Black elected officials served nationwide.',
              'In 1967, Stokes won in Cleveland and Hatcher won in Gary.',
              'By 1970, the count stood near fifteen hundred.',
              'In 1971, the Congressional Black Caucus was founded.',
              'In 1973, Jackson won in Atlanta and Young won in Detroit.'],
             "Work the dates as a rising line and name what each rung meant. In 1965, the year of the Voting Rights Act, a few hundred Black Americans held elected office in the entire country, most of them in small southern towns. The mayoral victories of 1967, Carl Stokes in Cleveland and Richard Hatcher in Gary, Indiana, proved the new electorate could carry industrial cities, not only counties. By 1970 the national count stood near fifteen hundred. In 1971 the Black members of the House organized the Congressional Black Caucus, converting individual seats into an institution with a staff, an agenda, and a vote presidents had to count. In 1973 Maynard Jackson took Atlanta and Coleman Young took Detroit. Behind the offices stood a second harvest the reading names: an enlarged Black middle class, admitted by the opened professions and the federal service to incomes and home ownership that the movement's laws had made possible for the first time.",
             kick='C · The harvest in office', size=24)

# ------------------------------------------------------ 10 STAT 5000
stat('5,000', 'Black elected officials, passed within the decade after 1970',
     'From a few hundred in 1965 · The Voting Rights Act counted in officeholders',
     "Teach this figure as the movement's institutional harvest stated in one number, and make students supply the mechanism before admiring the size. Five thousand officeholders did not arrive by persuasion. They arrived because the Voting Rights Act of 1965 suspended literacy tests, sent federal examiners to register voters in the covered states, and required those states to clear voting changes with Washington first, so the electorate itself changed and could not quietly be changed back. The count begins at a few hundred in 1965, reaches near fifteen hundred by 1970, and passes five thousand within the following decade, on its way to many thousands more. Set the number beside the lesson's other arithmetic: five states for Wallace in 1968, sixteen seats struck down in Bakke, two societies in the Kerner verdict. The harvest and the backlash grew in the same soil and the same years, and any verdict that reports only one of the numbers has not read the decade whole.",
     kick='C · The harvest in office')

# ------------------------------------------------- 11 SECTION D DIVIDER
divider_text('Section D', 'The Backlash Organized',
             'Wallace carries five states in 1968, and the winning candidate learns to court the same voters in quieter words.',
             "Define the section's term before its candidates, using the guided notes wording students will reproduce: the white backlash is the political reaction among white voters against the pace and reach of civil rights change. It was not a mood; it was an electorate, and 1968 was the year politicians learned to count it. George Wallace, who as governor of Alabama had stood in a schoolhouse doorway in 1963 and declared for segregation, ran nationally in 1968 outside the two major parties and built his campaign on resistance to federal enforcement, to busing before busing had a court order behind it, and to the disorder of the uprising years. Richard Nixon, the Republican nominee, drew the lesson Wallace taught and applied it inside a major party: the same voters could be courted with promises of law and order and slower enforcement, without a defense of segregation spoken aloud. The section asks which of the two men did more to shape the decades after, and the honest answer runs through both.")

# ------------------------------------------------------ 12 WALLACE AND NIXON
content_text('Five states and a strategy',
             ['Wallace carried five southern states in 1968.',
              'Nearly ten million votes were cast against the pace of change.',
              'Nixon\u2019s southern strategy courted the same voters.',
              'Its promises were law and order and slower enforcement.',
              'Segregation was defended by no one by name, while the pace of change was opposed by all.'],
             "Separate the two campaigns by method, since their voters overlapped and their legacies differ. Wallace spoke the backlash plainly and carried five states of the Deep South, winning nearly ten million votes, a showing no third party segregationist had approached, and he demonstrated that resistance to the movement's pace was a national constituency and not a regional embarrassment. Nixon spoke it carefully. The southern strategy, the Republican electoral strategy of the Nixon years as the guided notes define it, sought white southern voters by opposing federal civil rights enforcement, busing, and the pace of change the movement had set, while promising order in the cities after the uprising years. Nixon won the presidency in November 1968. The finding for students is procedural as much as moral: from 1968 forward, every national politician priced the backlash into every civil rights question, and the courts, whose members presidents appoint, became the ground where the priced argument was settled.",
             kick='D · The backlash organized', size=24)

# ------------------------------------------------------ 13 STAT FIVE STATES
stat('5 states', 'carried by George Wallace in the election of 1968',
     'Nearly ten million votes · A third party candidacy built on resistance',
     "Give this figure its context, because five states understates the showing and the showing is the point. Wallace ran in 1968 as an independent, without a party organization, a convention, or a single electoral vote promised in advance, on a platform of resistance to federal enforcement and to the movement's pace, and he carried Alabama, Georgia, Louisiana, Mississippi, and Arkansas outright while taking nearly ten million popular votes across the country, about one vote in seven cast. A protest candidacy of that size is a measurement, and both major parties read it as one. The Democrats read the loss of the Deep South, held since Reconstruction, as a generational realignment beginning. The Republicans read an available electorate. The southern strategy of the following years, and the judicial appointments that eventually decided Milliken and Bakke, are downstream of the arithmetic on this slide. Numbers in this lesson are arguments; this one argues that the backlash was organized, counted, and courted, in that order.",
     kick='D · The backlash organized')

# ------------------------------------------------- 14 SECTION E DIVIDER
divider_text('Section E', 'The Courts Become the Ground',
             'Swann opens a whole district in 1971; Milliken closes the suburbs in 1974, and the district line becomes the era\u2019s hardest border.',
             "Explain why the argument moved into courtrooms, because students should not treat the judicial turn as natural. After 1968 the presidency belonged to a coalition that had promised slower enforcement, and Congress had finished its statute writing with the act of that year. The movement's unfinished business, above all the schools, therefore stood before the one branch still holding orders from the heroic years: the federal courts, enforcing Brown against districts that had never dismantled their dual systems. The two decisions of this section, three years apart, mark the high point of that enforcement and its limit. Swann in 1971 told a unanimous court's answer to the school question inside one district. Milliken in 1974, decided five to four by a court whose membership presidents had begun to change, told where the answer stopped. Teach them as a pair with a border between them, because the border, the school district line, is the section's whole subject.")

# ------------------------------------------------------ 15 SWANN
content_text('Swann, 1971: the remedy runs',
             ['Charlotte had one combined city and county school system.',
              'Busing was upheld as one tool of desegregation.',
              'Desegregation plans could not be limited to the walk-in school.',
              'The Court was unanimous, seventeen years after Brown.'],
             "State Swann's holding in the opinion's own words, which the activity quotes at Station 3, because the phrasing carries the doctrine. The Court found no basis for holding that local school authorities may not be required to employ bus transportation as one tool of school desegregation, and it ruled that desegregation plans cannot be limited to the walk-in school. Charlotte mattered as the test case because its district joined city and suburbs in a single system, so a remedy drawn inside the district could reach across the residential pattern segregation had built. The decision was unanimous, and it stood for the proposition that a district which had run a dual system could be ordered to dismantle it root and branch, with ratios, redrawn zones, and buses as lawful instruments. For three years Swann was the law's furthest reach. Students should date what happened to it precisely: it was not reversed. It was fenced, by the case on the next slide, at the boundary Swann itself never had to cross.",
             kick='E · The courts become the ground', size=24)

# ------------------------------------------------------ 16 MILLIKEN
content_text('Milliken, 1974: the remedy stops',
             ['Detroit\u2019s schools were majority Black, and its suburbs were white.',
              'A metropolitan plan reached fifty-three districts.',
              'The Court found no interdistrict violation and allowed no interdistrict remedy.',
              'By five to four, the remedy stopped at the city line.'],
             "Run Milliken's logic step by step, in the sentence the activity quotes: without an interdistrict violation and interdistrict effect, there is no constitutional wrong calling for an interdistrict remedy. The lower court in Detroit had found the city's schools segregated by official action and had concluded that a remedy inside the city alone, whose schools were already majority Black, would leave a Black district ringed by white ones, so it ordered a metropolitan plan reaching fifty three suburban districts. The Supreme Court, five to four, set the metropolitan plan aside: the suburban districts had committed no proven violation, and their pupils could not be conscripted into another district's remedy. The consequence was structural and permanent. Where families could cross a district line by moving house, desegregation inside the line sorted schools by address instead, and the metropolitan resegregation that followed is the factual backdrop of every school argument since. Swann governed the district; Milliken governed the map.",
             kick='E · The courts become the ground', size=24)

# ------------------------------------------------- 17 SECTION F DIVIDER
divider_text('Section F', 'The Movement Widens',
             'The methods, the language, and the legal tools pass into other hands, from Delano\u2019s fields to movements the founders never led.',
             "Widen the lens deliberately at this point in the lesson, because a reckoning that counts only the movement's own institutions understates what it changed. The famous decade's deepest export was method. The sit in, the boycott, the mass march, the federal lawsuit, and the language of rights claims stated in the Constitution's own vocabulary were all, by 1968, a public curriculum that other Americans had studied at close range. Mexican American farmworkers in California, Native American activists occupying federal land and offices, Asian American students striking for their own studies programs, the women's movement organizing in the movement's own meeting rooms, and gay Americans after the Stonewall uprising of 1969 all drew on the curriculum openly and said so. This unit's bank carries the bridge in two records from a single March day in Delano, where the farmworkers' leader ended a fast for nonviolence and a United States senator came to honor him. The next slide teaches that day as the emblem of the widening.")

# ------------------------------------------------------ 18 DELANO
content_text('Delano, March 10, 1968',
             ['Cesar Chavez ended a twenty-five-day fast for nonviolence.',
              'The grape strike, running since 1965, held to King\u2019s method.',
              'Robert F. Kennedy came to Delano for the end of the fast.',
              'He called it a struggle for justice for the farmworker.',
              'The boycott carried the Montgomery method into another field.'],
             "Teach the Delano records as the bank carries them, a pair that also teaches sourcing. The United Farm Workers' own account reports Kennedy's visit; Kennedy's Senate office issued his statement the same day, and the two records agree on the sentence at their center, that he had come out of respect for one of the heroic figures of our time. His issued statement congratulates the strikers as people locked with Cesar in the struggle for justice for the farmworker and for the Spanish speaking American. Chavez's debt was declared, not hidden: the grape strike's boycott, its marches, its fasts, and its church based organizing were the southern movement's methods carried into California fields, and Chavez said his movement had learned from King. Twenty five days of fasting to hold a strike to nonviolence, three weeks before King was killed preaching the same discipline, is the widening in its purest form: the tactic outlived the campaign that invented it.",
             kick='F · The movement widens', size=24)

# ------------------------------------------------- 19 SECTION G DIVIDER
divider_text('Section G', 'The Argument Over Remedy',
             'Howard posed the question in 1965; the Philadelphia Plan tried it in 1969; Bakke settled its terms, narrowly, in 1978.',
             "Close the lesson where its argument began, at Howard University in June 1965, because the remedy debate of the 1970s is a footnote to a paragraph Johnson spoke that day. Fresh from the Civil Rights Act and weeks from the Voting Rights Act, Johnson told the graduates of the nation's leading Black university that freedom was not enough, that a person hobbled by chains and then set at a starting line had not been treated fairly, and that the nation should seek equality as a fact and equality as a result. Every later fight over affirmative action is an argument about whether policy may aim at the result or only police the starting line. The Philadelphia Plan of 1969 aimed at results for federal contractors. Bakke, in 1978, redrew the permission: results could inform a file, but a seat could not be set aside to reach them. The final slides state that settlement and ask students to judge the decade against the standard Howard set.")

# ------------------------------------------------------ 20 BAKKE
content_text('Bakke, 1978: the settlement',
             ['The Davis medical school set aside sixteen of its one hundred seats.',
              'The set-aside was struck down, and Allan Bakke was admitted.',
              'Racial classifications were inherently suspect and drew exacting scrutiny.',
              'Race survived as a plus in an applicant\u2019s file.',
              'Race was one factor among others, never a separate track.'],
             "Present Bakke as two holdings in one document, because either half alone misstates the law the decade left behind, and the activity tests the pair. The restrictive half: the University of California medical school at Davis reserved sixteen of its one hundred seats for minority applicants under a special admissions program, and the Court, through Justice Powell's controlling opinion, struck the set aside down as unnecessary to the goal of a diverse student body and invalid under the Equal Protection Clause, ordering Bakke admitted; racial classifications of any sort, Powell wrote, are inherently suspect and call for the most exacting judicial scrutiny. The preserving half: the same opinion held that a diverse student body is a compelling goal and that race or ethnic background may be deemed a plus in a particular applicant's file, weighed with all other qualifications and insulating no one from comparison. The quota died and the factor survived, and American admissions, hiring, and contracting argued inside that settlement for the rest of the century.",
             kick='G · The argument over remedy', size=24)

# ------------------------------------------------------ 21 AT A GLANCE
s = slide(NAVY)
kicker(s, 'The reckoning at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Won, answered, decided, left undone', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Won', 'Fair Housing Act, 1968; officials past 5,000', 'Statute book completed; the vote staffs the state'),
        ('Answered', 'Kerner shelved; Wallace; the southern strategy', 'The diagnosis refused; the backlash takes the presidency'),
        ('Decided', 'Swann 1971; Milliken 1974; Bakke 1978', 'The remedy runs to the district line, and the quota falls'),
        ('Undone', 'Housing, wealth, and schools in fact', 'Equality as a result, still owed in 1978')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.2, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.25, yy + 0.05, 5.1, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.55, yy + 0.05, 3.9, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the closing table of the guided notes, The Reckoning at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. Won: the Fair Housing Act of April 11, 1968 completing the three great statutes, and Black elected officials rising from a few hundred in 1965 to near fifteen hundred by 1970 and past five thousand within the decade after. Answered: the Kerner recommendations shelved in 1968, Wallace carrying five states that year, and the southern strategy taking the presidency that November. Decided: Swann upholding busing within a district in 1971, Milliken stopping Detroit's remedy at the district line in 1974, and Bakke striking the quota while preserving the factor in 1978. Undone: housing enforced by persuasion, schools resegregating by address, and the equality as a result that Howard had demanded in 1965. Grade the table on dates and actors named, not on adjectives.")

# ------------------------------------------------------ 22 VOCAB A
vocab('Words for the statute and the reaction',
      [('Kerner Commission', 'the 1968 report: two societies, separate and unequal'),
       ('Fair Housing Act', 'the Civil Rights Act of 1968, on housing'),
       ('white backlash', 'the reaction against the pace of change'),
       ('southern strategy', 'the Nixon era courtship of white southern voters')],
      "These definitions match the guided notes, and the notes carry them in full, word for word. Kerner Commission: the federal commission appointed by President Johnson whose 1968 report concluded that the nation was moving toward two societies, one black, one white, separate and unequal, and charged white racism with building the conditions of the urban uprisings. Fair Housing Act: the Civil Rights Act of 1968, passed in the week after Martin Luther King Jr.'s assassination, banning discrimination in the sale and rental of most housing. white backlash: the political reaction among white voters against the pace and reach of civil rights change, visible in the Wallace campaigns of the 1960s and the law and order politics that followed. southern strategy: the Republican electoral strategy of the Nixon years that sought white southern voters by opposing federal civil rights enforcement, busing, and the pace of change the movement had set.")

# ------------------------------------------------------ 23 VOCAB B
vocab('Words for the schools and the remedy',
      [('busing', 'court ordered transport to desegregate schools'),
       ('affirmative action', 'race taken into account to remedy past discrimination'),
       ('Bakke decision', '1978: the quota struck down, the factor kept')],
      "Three more terms, in the guided notes wording, carried in these notes in full, word for word. busing: the court-ordered transportation of students across neighborhood lines to desegregate schools, upheld by the Supreme Court in Swann in 1971 and resisted in cities across the country. affirmative action: government policies that take race into account in hiring, contracting, and college admissions in order to remedy the effects of past discrimination, ordered for federal contractors in the revised Philadelphia Plan of 1969. Bakke decision: the Supreme Court decision of 1978 in Regents of the University of California v. Bakke, which struck down a set-aside of seats by race in admissions and allowed race to be used as one factor among others. Notice the arc inside the three definitions: a remedy ordered at full strength in 1971, a policy built to reach results, and a settlement in 1978 that narrowed the second while citing the first era's amendment as its limit.")

# ------------------------------------------------------ 24 CLOSING SYNTHESIS
s = slide(NAVY)
kicker(s, 'Closing synthesis')
text(s, 0.9, 1.35, 11.5, 1.1, 'Where this unit ends', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 2.6,
     ["The movement destroyed a legal system of racial caste in a decade, the fastest moral transformation in the nation's history, and no statute it won has been repealed.",
      "It left wealth, housing, and schools substantially where law alone could not move them, which is the agenda the next era inherited."],
     size=23, color=POWDER, leading=1.3)
notes(s, "Close the unit by stating its ending as a finding in the terms the lesson has used throughout, sorted rather than summed. What the movement won can be listed and has not been unlisted: a legal system of racial caste dismantled, three great statutes standing unrepealed, the ballot protected by federal power, and thousands of Black officeholders governing cities and sitting in Congress. What answered it can also be listed: a commission's program shelved, a backlash organized into a governing coalition, a court's remedy fenced at the district line, and a quota struck down in the decade's last settlement. What it left undone is the list the next unit inherits: housing sorted by a market the statute could only police at the edges, schools resegregating inside metropolitan lines, and a wealth gap that formal equality never reached. Students should leave able to say which list any given fact of 1968 to 1978 belongs on, and to defend the placement from a document.")

# ------------------------------------------------------ 25 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ["What did the movement win, what answered it, and what was still undone when its famous decade ended? Sort the record, weigh the three strands, and answer the strongest counterclaim to your own verdict."],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Reckoning File: the statute, the report, two school decisions, Bakke, Howard revisited'),
        ('Notebook', 'Notebook page: the questions of the reckoning, what the documents show, what was decided'),
        ('Quick check', 'The Signing, April 11, 1968: the photograph, the sequence, the April claim weighed'),
        ('Writing', 'The Reckoning: the unit\u2019s closing verdict on its essential question')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the last act and the commission defined, Swann against Milliken, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close the unit by handing the reckoning to the students, which is what this lesson exists to do. The activity, The Reckoning File, gives them the Fair Housing Act from the statute as enacted, the Kerner conclusion from the audited bank record, the Swann and Milliken holdings from the opinions, the Bakke settlement from the syllabus and Justice Powell's opinion, and the Howard University address revisited, and asks for a sorting and the unit's closing verdict with the strongest counterclaim answered. The notebook page charts the questions of the reckoning. The quick check reads the signing photograph of April 11, 1968 and tests the decade's sequence against the claim that the signing finished the work. The writing task, The Reckoning, is the unit's closing writing task: a verdict on the essential question, drawn from the evidence bank, with the Howard standard engaged by name. The exit ticket has three parts: the act and the commission defined, Swann contrasted with Milliken, and the lesson question with the won, the answered, and the undone kept separate. The review day and the unit test follow from here.")

dc.save(OUT)
