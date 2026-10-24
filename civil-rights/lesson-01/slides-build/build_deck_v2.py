#!/usr/bin/env python3
"""Civil Rights Lesson 1 deck, "Foundations: The Movement Before the Movement,"
built to the approved system: image-led slides, fragments only on screen,
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
OUT = os.path.join(HERE, '..', 'lesson-01-slides.pptx')

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
text(s, 0.9, 5.32, 11.5, 0.4, 'THE CIVIL RIGHTS MOVEMENT · LESSON 1', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Foundations: The Movement Before the Movement', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'What Black Americans had built, and won, before the famous decade began, 1896 to 1948', size=17, color=POWDER)
notes(s, "The photograph shows President Truman addressing the closing session of the NAACP conference at the Lincoln Memorial on June 29, 1947, photographed by Abbie Rowe, National Archives record 199717. Hold the scene in front of students before any content. A president of the United States stood before the nation's oldest civil rights organization, at the memorial to the president who had signed emancipation, and pledged his administration to the cause of civil rights. That scene was possible in 1947 because of groundwork laid across the fifty years before it. This lesson walks that groundwork in order: the Jim Crow system at full strength, the institutions Black Americans built inside it, the court victories those institutions won, the war that changed the country's arithmetic, and the first federal steps of 1947 and 1948.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('What had Black Americans already built, and already won, before the movement\u2019s famous decade began?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the civil rights movement change American law and American life, and what did it leave unfinished?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question has two halves, and students should hear the verbs before the lesson begins. Built asks about institutions: what did Black Americans construct, own, and staff during the decades when the law was against them. Won asks about victories already on the record before 1950: cases decided, orders signed, ground taken. The question is aimed at a habit students bring with them, the assumption that the civil rights movement began in 1954 or 1955 with famous names and famous photographs. By the end of the hour they should be able to show that the famous decade inherited a church, a college system, a national press, a legal organization with a trained staff, two Supreme Court victories, and a federal government that had already begun, under pressure, to move. The unit question runs beneath this one as the frame for all eight lessons.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'The groundwork, in seven stretches', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The system in place', 'Jim Crow, Plessy, and the guarded ballot'),
        ('B', 'Shut out of the ballot box', 'Poll tax, literacy test, white primary'),
        ('C', 'The institutions that held', 'Church, colleges, press, and the NAACP'),
        ('D', 'Victories in court before 1950', 'Smith in 1944, Shelley in 1948'),
        ('E', 'The war and the moving north', 'A million in uniform, Double V, migration'),
        ('F', 'A committee, a report, a split party', 'To Secure These Rights, 1947'),
        ('G', 'The order of July 26, 1948', 'Executive Order 9981')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Sections A and B state the problem at full strength: a legal system of racial caste, and a ballot box locked by fees, tests, party rules, and violence. Section C gives the answer built inside that system, the institutions Black Americans owned. Section D gives the first victories those institutions won in court. Section E gives the war, which put a million Black Americans in uniform, gave the demand a two letter name, and moved voters to states where their ballots counted. Sections F and G give the federal response of 1947 and 1948, a report, a party split, and an order desegregating the armed forces. Tell students the summary table at the end of their guided notes asks them to rebuild exactly this map.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', 'The System in Place',
             'Jim Crow governed by law and by custom, and the Supreme Court had blessed it.',
             "Begin with the system's full extent, because students underestimate it when they meet it only in pieces. Jim Crow was not a set of rude customs that happened to grow up in one region. It was a legal order, written into state statutes and local ordinances, requiring separation in schools, transportation, theaters, restaurants, parks, and courthouses, and it was enforced by custom and by violence where statutes did not reach. In 1896 the Supreme Court, in Plessy v. Ferguson, upheld the arrangement under the doctrine of separate but equal, and for fifty years the facilities provided under that doctrine were separate and unequal in fact, in school funding most measurably. Students should hold two ideas together in this section. The system was oppressive, and the system was constructed, piece by piece, by identifiable laws and decisions, which is why identifiable laws and decisions could later take it apart.")

# ------------------------------------------------------ 5 SYSTEM
content_text('Separate in everything, equal in nothing the law provided',
             ['Statutes required separate schools and cars.',
              'Plessy blessed the system in 1896.',
              'Separate but equal was the doctrine.',
              'The facilities were separate and unequal.',
              'Custom enforced what law did not reach.'],
             "Work the fragments as a description of a machine with three power sources. Law came first: statutes and ordinances commanded separation in the ordinary places of life, school, train, waiting room, theater, restaurant, fountain, and a citizen met the system a dozen times a day without ever seeing a policeman. Doctrine came second: Plessy v. Ferguson in 1896 told the country that the Constitution permitted the arrangement as long as facilities were equal, and southern governments then spent fifty years providing the separation and neglecting the equality, above all in the money spent on Black schools. Custom came third, and students should not rank it last in force. Habit, expectation, and the knowledge of what happened to people who crossed the line enforced separation in places no statute named, and violence stood behind the habit whenever it was challenged.",
             kick='A · The system in place')

# ------------------------------------------------------ 6 THREE IN 100 STAT
stat('3 in 100', 'Black adults in the South were registered to vote in 1940',
     'The combined count of the poll tax, the literacy test, the white primary, and violence',
     "Let the small figure carry the weight of Sections A and B together. In 1940, after fifty years of the devices the next section names, about three in every hundred Black adults in the South appeared on the registration rolls, and in the deepest states the count stood lower still. Read the figure for what it measures. It is not a measure of apathy, and teachers should say so plainly. It is the measured output of a system designed to produce it: a fee charged for the ballot, a test graded by an interested official, a primary closed by race in the only party that won elections, and violence held in reserve behind the paperwork. A people held at three in a hundred cannot vote a system down from inside it. Everything else in this lesson, the institutions, the lawsuits, the migration, and the pressure on presidents, is an answer to the problem this number states.",
     kick='B · Shut out of the ballot box')

# ------------------------------------------------- 7 SECTION B DIVIDER
divider_text('Section B', 'Shut Out of the Ballot Box',
             'Three devices, and violence behind all three.',
             "This section names the machinery of disfranchisement, and students should learn it as machinery, each part doing work the others could not. The poll tax priced the ballot. The literacy test put admission in the hands of a white registrar who graded Black applicants by a standard he invented on the spot. The white primary closed the only election with real choices in the one party South, so that even a registered Black voter met a general election whose outcome had been settled without him. Behind the three devices stood a fourth fact, unwritten and universally understood: a Black citizen who pressed a claim to register risked his job, his credit, his home, and at the limit his life, in a region where lynching went unpunished in almost every case. The result stands on the stat slide the class has just seen, three registered voters in a hundred by 1940.")

# ------------------------------------------------------ 8 LOCKS
content_text('Three locks on the ballot box',
             ['The poll tax charged a fee for voting.',
              'The literacy test rested in a registrar\u2019s hands.',
              'The white primary closed the deciding election.',
              'Violence stood behind the paperwork.',
              'The system could not be voted down.'],
             "Take the devices one at a time and make students state how each one worked, because the unit test asks for the mechanics, not the mood. The poll tax was cumulative in several states, so a citizen who had skipped years owed years of fees before he could vote once, and the fee fell hardest on sharecroppers paid once a year. The literacy test asked applicants to read and interpret a passage of the state constitution to the registrar's satisfaction, a standard white applicants were routinely helped through and Black applicants routinely failed. The white primary was the most elegant lock of the three: in a region where the Democratic nomination was the election, barring Black voters from the primary disfranchised them while leaving the general election formally open. Close with the conclusion the reading draws. A system locked this way had to be broken from outside the ballot box, in courts, in migration, and in Washington.",
             kick='B · Shut out of the ballot box', size=24)

# ------------------------------------------------- 9 SECTION C DIVIDER
divider_text('Section C', 'The Institutions That Held',
             'A church, colleges, a press, and an association the system could not close.',
             "Turn the lesson here, from what was done to Black Americans to what Black Americans built, because the rest of the unit runs on this section's ground. The system controlled the schools, the ballot, and the courts of first resort. It did not control the Black church, which held its own buildings and budgets and answered to its own congregations. It did not control the Black colleges, which trained the teachers, lawyers, and doctors the community required. It did not control the Black press, which carried the news white papers refused to print to a national readership every week. And from 1909 it faced the NAACP, an organization built to fight the system with the system's own instruments, legislatures, courts, and print. Students should notice the common property of the four: each was owned, funded, and staffed by the people it served, so none could be closed by a governor's order or a registrar's refusal.")

# ------------------------------------------------------ 10 INSTITUTIONS
content_text('Owned outright, and beyond white control',
             ['The church held buildings and budgets.',
              'Colleges trained teachers, lawyers, and doctors.',
              'The Black press spoke to the nation.',
              'The NAACP fought on three fronts.',
              'The NAACP was founded in 1909 and funded by dues.'],
             "Give each institution its specific contribution, because the activity asks students to name what each record built. The church contributed ground and voice: meeting space that no official could revoke, and ministers whose salaries came from their congregations, so they could speak when a teacher or a government employee could be fired for speaking. The colleges contributed trained people, including the lawyers who would staff the legal campaign the next section describes. The press contributed a national conversation: the Chicago Defender and the Pittsburgh Courier moved along the rail lines with the porters who carried them, telling readers in Mississippi and Chicago the same news in the same week. The NAACP contributed continuity and craft, a national office, branch dues, a magazine, The Crisis, and a legal program that treated each case as one step in a sequence planned across decades.",
             kick='C · The institutions that held', size=24)

# ------------------------------------------------- 11 SECTION D DIVIDER
divider_text('Section D', 'Victories in Court Before 1950',
             'Twice, the Supreme Court ruled that private was state action in disguise.',
             "Section D holds the groundwork's first victories, and they were won by the institution the class just studied, which is the point to make before any case is named. In 1944 the NAACP carried the white primary to the Supreme Court in Smith v. Allwright, with Thurgood Marshall arguing. In 1948 the Court decided Shelley v. Kraemer, on the restrictive covenants that barred Black families from buying homes in white neighborhoods. In both cases the defense rested on one word: private. A party was a private club. A covenant was a private agreement. Twice the Court answered that when the state's machinery does the excluding, the exclusion is state action, and the Constitution applies to it. Neither victory desegregated a school or seated a single voter by itself. Each removed a legal prop from the system, and together they taught a generation of lawyers that the federal courts could be made to move, the lesson Brown would cash in during the next lesson.")

# ------------------------------------------------------ 12 PRIVATE FAILS
content_text('The word private fails twice',
             ['Smith ended the white primary in 1944.',
              'A primary under state law is state action.',
              'Shelley barred covenant enforcement in 1948.',
              'Courts could not do the excluding.',
              'Marshall argued Smith for the NAACP.'],
             "Teach the two holdings as one argument made twice, because students remember the pattern better than either case alone. In Smith, Texas said the Democratic Party chose its own members as any club does. The Court looked at how the primary actually ran: created by state statute, administered under state law, and producing the only ballot line that counted in November. A primary run that way, the Court held, is state action within the meaning of the Fifteenth Amendment, and it cannot exclude by race. In Shelley, homeowners said their covenants were private contracts. The Court agreed the paper was private and held that enforcement was not: when a state court evicts a Black buyer under a covenant, the state has denied the equal protection of the laws. Hold the limit up as plainly as the victory. Shelley did not outlaw the agreements. It withdrew the courts from them, and voluntary discrimination in housing sales continued for twenty more years.",
             kick='D · Victories in court before 1950', size=24)

# ------------------------------------------------------ 13 8 TO 1 STAT
stat('8 to 1', 'the vote in Smith v. Allwright, April 3, 1944',
     'The white primary struck down · Only Justice Roberts dissented',
     "Pause on the margin, because the margin is evidence about the groundwork's quality. Smith v. Allwright was not a narrow escape. Eight justices, in an opinion by Justice Reed, held that Texas could not do through a party what the Fifteenth Amendment forbade it to do directly, and the Court overruled its own nine year old precedent, Grovey v. Townsend, to reach the result. Only Justice Roberts, the author of Grovey, dissented, and his dissent complained about the Court's willingness to reverse itself rather than about the right at stake. Students should connect the margin to the preparation behind it. The NAACP's lawyers had litigated the white primary in a sequence of cases reaching back to the 1920s, losing, adjusting, and returning, and by 1944 the argument arrived at the Court fully built. Court victories in this unit are never sudden. They are the visible end of staff work done years earlier, which is what the word groundwork means in this lesson's title.",
     kick='D · Victories in court before 1950')

# ------------------------------------------------- 14 SECTION E DIVIDER
divider_photo('tuskegee-port.jpg', 'Section E', 'The War and the Moving North',
              ['Pilots of the 332nd Fighter Group,', 'photographed by Toni Frissell, 1945.'],
              "The photograph shows pilots of the 332nd Fighter Group at Ramitelli, Italy, in March 1945, photographed by Toni Frissell for the Office of War Information, held by the Library of Congress under digital ID ppmsca.13245. Section E takes up the war, and the photograph holds its central contradiction in one frame: Black Americans flew and fought for a country whose armed forces kept them in segregated units under rules that presumed their inferiority. About a million Black Americans served in the Second World War. They came home with service records, training, and a claim stated by the Black press in two letters, Double V, victory over fascism abroad and victory over racism at home. At the same time the war was moving their families north and west in the second wave of the Great Migration, to cities where their votes could not be taken from them. The war changed both the claim and the arithmetic of American politics.")

# ------------------------------------------------------ 15 WAR
content_photo_s('chicago-port.jpg', 'Service abroad, and a second victory demanded at home',
             ['About a million Black Americans served in uniform.',
              'The military kept them segregated.',
              'Double V named the contradiction.',
              'Randolph\u2019s 1941 threat won Order 8802.',
              'Migration moved voters north and west.'],
             "Work the section as cause and consequence in both directions. Service created the claim: a man who had been drafted, trained, and in many cases decorated could state his demand for equal treatment as a debt owed, and the country found the debt hard to argue with. The Black press gave the claim its form in 1942, when the Pittsburgh Courier built its Double V campaign on a reader's letter asking why he should give his life for freedoms he did not hold, and the emblem spread through the Black press nationwide. Pressure created the precedent: in 1941, before the war began for the United States, A. Philip Randolph threatened a march on Washington, and President Roosevelt answered with Executive Order 8802, barring discrimination in defense industries, the first federal fair employment order since Reconstruction. And migration created the constituency, as war jobs pulled Black southerners into northern and western cities by the hundreds of thousands.",
             kick='E · The war and the moving north')

# ------------------------------------------------------ 16 492000 STAT
stat('492,000', 'Black residents of Chicago in 1950, up from 234,000 in 1940',
     'The second Great Migration, counted by the census · A constituency presidents had to answer',
     "Use the census counts to make the migration concrete, because students hear migration as weather, something that happened, rather than as a political act performed household by household. Chicago's Black population more than doubled in a single decade, from about 234,000 in 1940 to about 492,000 in 1950, and Detroit, Cleveland, Los Angeles, and Oakland grew on the same pattern. Each arriving family changed two political facts at once. In the South, a registrar lost a subject he could intimidate. In the North, a ward gained voters whom both parties had to court in states rich in electoral votes. By 1948 the arithmetic sat on every strategist's desk in Washington: presidential elections turned on a handful of northern states, and Black voters in those states held margins larger than the gaps between the candidates. The report and the order in the next two sections were written by men who had done that arithmetic, and the writing task asks students to judge how much of the explanation the arithmetic carries.",
     kick='E · The war and the moving north')

# ------------------------------------------------- 17 SECTION F DIVIDER
divider_photo('truman-port.jpg', 'Section F', 'A Committee, a Report, and a Split Party',
              ['President Truman at the NAACP conference,', 'Lincoln Memorial, June 29, 1947.'],
              "The photograph shows President Truman addressing the closing session of the NAACP conference at the Lincoln Memorial on June 29, 1947, photographed by Abbie Rowe, National Archives record 199715. Section F gives the first federal steps, and Truman stands at their center, a border state president whose committee would name the whole system as federal business. In December 1946 Truman created the President's Committee on Civil Rights, after a year in which Black veterans had been beaten and lynched in the South and the crimes had gone unpunished. He charged the committee with saying how the nation could better protect civil rights. Its report, To Secure These Rights, appeared on October 29, 1947, and it exceeded what cautious advisers had expected. Truman then sent its program to Congress in February 1948, knowing the price inside his own party, and the party paid part of that price at its convention that summer.")

# ------------------------------------------------------ 18 REPORT
content_text('A president\u2019s committee names the system',
             ['Truman created the committee in 1946.',
              'The report appeared in October 1947.',
              'Lynching and disfranchisement were named federal business.',
              'Distinctions of race have no place in public life.',
              'Congress got the program in February 1948.'],
             "Teach the report from its own sentences, because students read this document at the first station of the activity and should arrive there knowing its logic. The committee protected private choice plainly: each person must be free to choose his friends and govern his family life. It then drew the line the whole later movement would use. In going to school, working, voting, serving in the armed forces, using public services and transportation and accommodations, and choosing where to live, distinctions of race, color, and creed have no place. Its second famous passage made lynching a national affair: the repercussions of such a crime echo from one end of the globe to the other, and the world looks to the American national government for an explanation and for remedial action. A committee report binds no one. This one fixed the agenda every later federal step in the unit follows, in the report's own order: lynching, the ballot, and segregation itself.",
             kick='F · A committee, a report, and a split party', size=24)

# ------------------------------------------------------ 19 SPLIT
content_text('The party splits over the report',
             ['Southern delegates walked out in 1948.',
              'The Dixiecrats ran their own ticket.',
              'They carried four states that fall.',
              'Truman won without them.',
              'Northern Black votes were part of the margin.'],
             "The split deserves its facts, because it is the first time in the unit that civil rights visibly rearranged national politics. At the Democratic convention in July 1948, with a strong civil rights plank adopted, delegates from the deep South walked out and formed the States' Rights Democratic Party, the Dixiecrats, running Governor Strom Thurmond of South Carolina for president. In November the ticket carried four states, South Carolina, Alabama, Mississippi, and Louisiana, and won thirty nine electoral votes. Truman won the election anyway, by margins in the northern and western states so narrow that Black voters in cities such as Chicago and Cleveland formed part of the arithmetic of victory. Students should state the lesson the year taught both parties. A national Democrat could now lose the deep South over civil rights and still win the presidency, which had not been true for a century, and every later president in this unit governed inside that new calculation.",
             kick='F · A committee, a report, and a split party', size=24)

# ------------------------------------------------- 20 SECTION G DIVIDER
divider_photo('randolph-port.jpg', 'Section G', 'The Order of July 26, 1948',
              ['A. Philip Randolph in 1963,', 'photographed by John Bottega.'],
              "The portrait shows A. Philip Randolph in 1963, photographed by John Bottega of the New York World Telegram and Sun staff, held by the Library of Congress under digital ID cph.3c19495. Randolph closes the lesson because he opens its argument twice, and students should leave able to tell both stories. In 1941 his threatened march on Washington extracted Executive Order 8802 from President Roosevelt. In 1948 he returned, telling a Senate committee that he would counsel Black young men to resist a segregated draft, a threat of mass civil disobedience aimed at the one institution the president commanded directly. On July 26, 1948, days after the Democratic convention had split over civil rights, President Truman signed Executive Order 9981. Section G reads the order closely, including the brake written into its own text, and follows it into the Korean War, where its promise was finally carried out under the pressure of a battlefield's manpower needs.")

# ------------------------------------------------------ 21 ORDER
content_text('Equality of treatment, ordered',
             ['Randolph threatened draft resistance in 1948.',
              'The order was signed on July 26, 1948.',
              'Equality was ordered without regard to race.',
              'A brake was written into the order itself.',
              'Korea carried the order into practice.'],
             "Read the order's first numbered paragraph aloud, because the quick check tests this passage word by word. Truman declared it the policy of the President that there shall be equality of treatment and opportunity for all persons in the armed services without regard to race, color, religion or national origin. Then read the brake in the same paragraph: the policy is to be put into effect as rapidly as possible, having due regard to the time required, without impairing efficiency or morale. Those qualifying words gave resisting officials their instrument, and the services moved slowly for two years. What moved them was Korea. From 1950 the Army in the field integrated units because replacements arrived as individuals and commanders needed riflemen, and by the war's end the armed forces had become the most integrated large institution in American life. The order shows students the groundwork's full circuit in one document: pressure applied, a president moved, a promise qualified, and an institution changed in practice under later pressure.",
             kick='G · The order of July 26, 1948', size=24)

# ------------------------------------------------------ 22 SYNTHESIS
content_text('Built and won, before the decade began',
             ['Institutions were owned for forty years.',
              'Two props of the system were struck down.',
              'A report, a split party, and an order followed.',
              'Mass pressure was already the central tactic.',
              'The famous decade inherited all of it.'],
             "Close the teaching where the lesson question points, with the inventory complete. Built, across four decades: a church that no official controlled, colleges that trained the movement's professionals, a press that made a national public, and an association, founded in 1909, with branches, dues, a magazine, and lawyers who planned in sequences of cases. Won, before the decade began: the white primary ended in 1944, covenant enforcement ended in 1948, a fair employment precedent set in 1941, a presidential report in 1947 naming the system as federal business, a party forced to choose in 1948, and the armed forces ordered desegregated that July. Add the tactic that produced the two orders: organized mass pressure, threatened by Randolph in 1941 and again in 1948, years before it filled the television screens of the famous decade. The next lesson begins in 1954, and students should now be unable to see Brown as a beginning. It was an inheritance being spent.",
             kick='G · The order of July 26, 1948')

# ------------------------------------------------------ 23 VOCAB A
vocab('Words for the system and the answer to it',
      [('Jim Crow', 'the laws and customs that enforced segregation in the South'),
       ('segregation', 'separation by race in schools, facilities, and transport'),
       ('disfranchisement', 'the denial of the right to vote'),
       ('NAACP', 'founded in 1909; fought in the courts, in Congress, and in print')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. Jim Crow: the system of state and local laws and customs that enforced racial segregation in the South. segregation: the separation of people by race in public facilities, schools, and transportation. disfranchisement: the denial of the right to vote through law or practice. NAACP: the National Association for the Advancement of Colored People, founded in 1909, which fought segregation through the courts, through lobbying, and through its magazine The Crisis. Note the teaching pattern in this set: the first three terms name the system and its guard on the ballot, and the fourth names the organization built to answer all three, with its founding year and its three fronts carried inside the definition itself.")

# ------------------------------------------------------ 24 VOCAB B
vocab('Words for the war and the first federal steps',
      [('Double V campaign', 'victory over fascism abroad and racism at home, from 1942'),
       ('To Secure These Rights', 'the 1947 report naming segregation federal business'),
       ('Executive Order 9981', 'the July 26, 1948 order desegregating the armed forces')],
      "Three more terms, again matching the guided notes exactly. Double V campaign: the campaign led by Black newspapers from 1942 for victory over fascism abroad and victory over racism at home. To Secure These Rights: the 1947 report of President Truman's Committee on Civil Rights, which called for federal laws against lynching and disfranchisement and for the end of segregation in American life. Executive Order 9981: President Truman's order of July 26, 1948 directing equality of treatment and opportunity for all persons in the armed forces, the order that desegregated the United States military. Students should hold the chain these three definitions make when read in order: a demand stated by a press campaign in 1942, a program stated by a president's committee in 1947, and an order signed by that president in 1948.")

# ------------------------------------------------------ 25 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Work the groundwork file', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['What had Black Americans already built, and already won, before the movement\u2019s famous decade began? Work the five records in order, then judge which piece of groundwork the later movement could least have done without.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Groundwork File: the report, the order, the Double V record, the court victories, and the migration count'),
        ('Notebook', 'Notebook page: six pieces of groundwork, classified and evidenced'),
        ('Quick check', 'The Order and the Argument: Executive Order 9981 against the record of 1941 to 1948'),
        ('Writing', 'Built, Won, or Given?: the steps of 1947 and 1948 weighed against the groundwork behind them')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the NAACP stated with its three fronts, the war\u2019s change explained, and the lesson question answered with one thing built and one thing won.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Groundwork File, runs five stations through the evidence: the To Secure These Rights passages, the Executive Order 9981 text, a labeled summary of the Double V campaign, the Smith and Shelley holdings, and a labeled summary of the migration counts, ending in a ledger where students classify each record as a law, an institution, a constituency, or a tactic, and judge which piece of groundwork the later movement could least have done without. The notebook page asks students to rebuild six pieces of the groundwork with evidence. The quick check, The Order and the Argument, tests the order's passage against the background of 1941 to 1948, tagged to the blueprint. The writing task, Built, Won, or Given?, weighs the federal steps of 1947 and 1948 against the groundwork that produced them. The exit ticket has three parts: the NAACP and its three fronts; the war's change, naming the campaign and the migration; and the lesson question with one thing built and one thing won. Next lesson takes up Brown.")

dc.save(OUT)
