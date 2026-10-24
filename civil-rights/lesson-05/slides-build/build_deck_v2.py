#!/usr/bin/env python3
"""Civil Rights Lesson 5 deck, "Birmingham and the March on Washington,"
built to the approved system: image-led slides, fragments only on
screen, comprehensive speaker notes, full lesson + vocabulary coverage.
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
OUT = os.path.join(HERE, '..', 'lesson-05-slides.pptx')

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
    frags(s, items, y=2.15 if kick else 2.0, size=size)
    notes(s, note)
    return s

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'THE CIVIL RIGHTS MOVEMENT · LESSON 5', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Birmingham and the March on Washington', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'One spring in Alabama, one day in Washington, 1963', size=17, color=POWDER)
notes(s, "The photograph shows the leaders of the March on Washington marching from the Washington Monument toward the Lincoln Memorial on August 28, 1963, photographed by Rowland Scherman for the United States Information Agency. It opens a lesson that runs through a single year in two cities. In Birmingham, Alabama, a spring campaign chose a deeply segregated city on purpose, produced the movement's most famous letter from a jail cell, and sent schoolchildren into the streets to meet fire hoses and police dogs on television. In Washington, that pressure produced a presidential address, a promised civil rights bill, and a march of a quarter of a million people. Then, eighteen days after the march, a bomb in a Birmingham church killed four girls. Students should leave able to trace the chain of pressure event by event, and to state what the federal government had done, and had not done, by December 1963.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("How did Birmingham force the nation's hand, and what did the March on Washington ask the nation to become?", {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the civil rights movement change American law and American life, and what did it leave unfinished?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "The lesson question has two halves, and students should keep both in view all hour. The first half asks how Birmingham forced the nation's hand, which is a question about mechanism: a chosen city, a jailed letter writer, children in the streets, a settlement signed by merchants, and a president who announced a civil rights bill in June that he had not announced in April. The second half asks what the march asked the nation to become, which is a question about the demand itself: ten demands for jobs and freedom read aloud at the Lincoln Memorial, and a closing address that presented the founding documents as a promise the country had signed and not yet honored. The unit question runs beneath as the frame. This lesson is the movement's strongest year, and its clearest test of what protest could move, and what it could not move yet.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Pressure, a promise, and a price', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The city chosen on purpose', 'Segregation, Connor, and Project C'),
        ('B', 'The letter from the cell', 'King answers eight clergymen, in paraphrase'),
        ('C', 'The children march', 'May 2 and 3, the settlement within a week'),
        ('D', 'The president moved', 'June 11: a moral issue, a bill announced'),
        ('E', 'A march older than the summer', 'Randolph, Rustin, and ten demands'),
        ('F', 'August 28 at the Lincoln Memorial', 'A quarter of a million people, King last'),
        ('G', 'The answer from Birmingham', 'September 15, and a bill still stalled')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Sections A through C build the pressure in Birmingham: the chosen city and its Project C, the letter King wrote from his cell in April, and the children's marches of May that ended in a settlement within a week. Section D follows the pressure to Washington, where President Kennedy addressed the nation on June 11 and announced the bill, on the night Medgar Evers was assassinated in Mississippi. Sections E and F build the march, its organizers, its ten demands, and the day itself, August 28. Section G returns to Birmingham for September 15 and closes with the bill still stalled in Congress. Tell students the summary table at the end of their guided notes, The Year at a Glance, asks them to rebuild this map with dates attached.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', 'The City Chosen on Purpose',
             'Total segregation, a commissioner who defended it in public, and a local movement already built.',
             "Open with the choice itself, because Birmingham was not an accident of geography. The movement chose the city for three reasons students should be able to list. Its segregation was total, covering lunch counters, fitting rooms, restrooms, drinking fountains, and jobs, and enforced as a point of civic pride. Its commissioner of public safety, Eugene Connor, called Bull, had built his power on open defiance of the federal courts, and could be counted on to answer protest in ways the country would see. And its local movement, the Alabama movement led by the Reverend Fred Shuttlesworth, had been fighting that segregation for years, through bombings of homes and churches, and had the churches, the mass meetings, and the organization a campaign needs on the day it arrives. The Southern Christian Leadership Conference joined that local movement in the spring of 1963. Neither partner was complete without the other: the national organization brought King and attention, and the local movement brought Birmingham.")

# ------------------------------------------------------ 5 SECTION A CONTENT
content_text('Project C: confrontation on a schedule',
             ['Protesters held sit-ins at downtown lunch counters.',
              'Marchers moved on city hall in organized waves.',
              'Shoppers boycotted downtown stores at the Easter season.',
              'Demonstrators accepted arrests in numbers to fill the jails.',
              'The aim was to force the city to bargain.'],
             "Use the full guided notes definition here and have students check it in their notes: the Birmingham campaign is the protest campaign of 1963 in Birmingham, Alabama, led by the Southern Christian Leadership Conference and the local movement, whose televised repression pushed President Kennedy to propose a national civil rights bill. Note that the definition already contains the lesson's verdict, and students will spend the hour testing it. The plan's name was Project C, for confrontation, and its logic came straight from the Albany lesson of the previous lesson in this unit. Protest that produced no crisis could be absorbed. So the campaign ran on a schedule designed to produce one: sit-ins that closed counters, marches that drew arrests, and a boycott timed to the Easter shopping season, when downtown stores could least afford empty aisles. The arrests were not a byproduct of the plan. They were the plan, accepted in numbers meant to fill the city's jails and make segregation more expensive to defend than to bargain away.",
             kick='A · The city chosen on purpose')

# ------------------------------------------------- 6 SECTION B DIVIDER
divider_text('Section B', 'The Letter from the Cell',
             'Arrested on Good Friday, answering eight clergymen who had urged patience.',
             "Section B covers four days in a jail cell and the document they produced. On Good Friday, April 12, 1963, King marched without a permit and was arrested, and he was held alone in a cell in the Birmingham city jail. In the newspaper he found a statement by eight white Alabama clergymen, ministers and rabbis of the state, who called the demonstrations unwise and untimely and urged Black Birmingham to wait and to work through the courts. His answer began in the margins of that newspaper, continued on scraps his lawyers brought in, and was finished on a legal pad. One teaching rule governs this whole section, and students should hear it plainly. The letter is under copyright. This lesson quotes it only in the activity, in two short passages totaling sixteen words, counted exactly. Everywhere else, including this deck, its argument is paraphrased, and the paraphrase is labeled as paraphrase.")

# ------------------------------------------------------ 7 SECTION B CONTENT
content_text("The letter's argument, in paraphrase",
             ['Injustice in one city endangered fairness in every city.',
              'Delay was itself a decision, after three centuries of waiting.',
              "An unjust law bound no one's conscience.",
              'The white moderate preferred order to justice.',
              "King's exact words are quoted only in the activity."],
             "Teach the argument in the paraphrase the reading carries, and name the paraphrase as paraphrase as you go. King answered the outsider charge first: he had been invited to Birmingham by the local movement, and beyond the invitation, wrong in one city endangered fairness in every city, so no American could be treated as a stranger inside his own country. He answered the call to wait next: delay was itself a decision, made by people who had not spent three centuries waiting for rights the Constitution already promised. He answered the charge of lawbreaking with a distinction: a law that degraded human personality, or that was imposed on a people denied the vote by which laws are made, was unjust, and an unjust law bound no one's conscience. And he named the obstacle his audience least expected: not the open segregationist, but the white moderate who agreed with the goal, rejected the method, preferred order to justice, and kept setting the timetable for another people's freedom. The eight clergymen were that audience, which is why the letter addresses fellow ministers.",
             kick='B · The letter from the cell', size=24)

# ------------------------------------------------- 8 SECTION C DIVIDER
divider_text('Section C', 'The Children March',
             'The adult campaign stalled. The students of Birmingham walked out of school.',
             "Section C covers the turn that saved the campaign and the week that followed it. By the first days of May, the adult movement had a problem of arithmetic. Hundreds had been arrested since April, bail money was running short, and a movement that could not get its people out of jail could not keep marching them into it. The downtown boycott hurt the stores, but the merchants had not yet settled. James Bevel, a young organizer formed in the Nashville student movement, proposed the marchers Birmingham had in reserve: its Black schoolchildren, thousands of them, trained in nonviolence in the movement churches. The proposal was debated hard, and students should hear the debate rather than a clean story. Sending children toward Connor's police was a risk taken with open eyes, by organizers who knew exactly what the city had done to adults. The movement agreed, and set the date for May 2.")

# ------------------------------------------------------ 9 SECTION C CONTENT
content_text('May 2 and May 3, 1963',
             ['Students gathered at the 16th Street Baptist Church on May 2.',
              'Police arrested more than 900 students on the first day.',
              'Fire hoses and police dogs met marchers on May 3, on television.',
              'Birmingham business leaders settled within a week.',
              'Counters desegregated and Black clerks were hired.'],
             "Walk the two days separately, because they did different work. May 2 was numbers: students left classrooms across the city, gathered at the 16th Street Baptist Church, and came out in trained groups, wave after wave, until the police had arrested more than nine hundred of them and filled the cells and a fairground stockade. May 3 was sight: with the jails full, Connor answered the next waves with high pressure fire hoses and with police dogs, and television cameras recorded it for the nation that night. Use the guided notes definition and have students copy it exactly: the Children's Crusade is the marches of May 1963 in Birmingham in which thousands of Black schoolchildren left their classes to demonstrate and were met with fire hoses, police dogs, and jail, producing the images that turned national opinion. Then give the result its date. Within a week, on May 10, Birmingham's business leaders settled: lunch counters and fitting rooms would desegregate, and Black clerks would be hired in downtown stores.",
             kick='C · The children march', size=24)

# ------------------------------------------------------ 10 SECTION C STAT
stat('900+', 'students arrested on May 2, 1963, the first day',
     'The jails and a fairground stockade filled in one afternoon · The next day brought the hoses and the dogs',
     "Stop on the number and on what produced it. More than nine hundred arrests in a single day was not a police achievement; it was the movement's arithmetic working in public. The students came out of the church in groups all afternoon, trained, singing, and willing to be arrested, and the city ran out of jail before the movement ran out of marchers. That is the fact to hold beside May 3. When Connor turned the hoses and the dogs on the next day's waves, he was answering a demonstration he had already failed to absorb quietly, and he answered it in front of cameras. The famous photographs of those days are copyrighted press photographs, and this lesson does not reproduce them, which is worth one sentence to the class: students are learning these events from written records and from the settlement they produced, and the activity's third station describes the photographs and says plainly why they are not shown. The images turned national opinion in 1963 whether or not a classroom reprints them in 1963's terms today.",
     kick='C · The children march')

# ------------------------------------------------- 11 SECTION D DIVIDER
divider_text('Section D', 'The President Moved',
             'June 11, 1963: an address in the evening, an assassination in the night.',
             "Section D follows the pressure out of Birmingham and into the White House. Through April and May, the Kennedy administration had worked the Birmingham crisis the way it preferred to work civil rights questions: with court orders, with quiet negotiation, and with officials sent south to press businessmen toward a settlement Washington could welcome without sponsoring. No civil rights bill had been announced. The president's brother ran the Justice Department's effort, and the president kept his distance from legislation his advisers believed Congress would not pass. Birmingham changed that calculation in about five weeks. The section therefore turns on a single evening, June 11, 1963, and students should learn it as a day in three parts: a governor faced down at a university door in the afternoon, a president on television in the evening, and a murder in a driveway in Jackson, Mississippi, before the night was out.")

# ------------------------------------------------------ 12 SECTION D CONTENT
content_text('June 11: a moral issue, a bill announced',
             ['Governor Wallace was faced down at the University of Alabama that afternoon.',
              'President Kennedy addressed the nation that evening.',
              'Kennedy named civil rights a moral issue.',
              'Kennedy announced a comprehensive civil rights bill.',
              'An assassin killed Medgar Evers in Jackson that night.'],
             "Use the guided notes definition in full: Kennedy's civil rights address is President Kennedy's televised address of June 11, 1963, after the Birmingham crisis, calling civil rights a moral issue and announcing that he would send Congress a comprehensive civil rights bill. The address is Station 2 of the activity, quoted from the audited record, and its order is the teaching point. Kennedy called the question moral before he called it legislative, as old as the scriptures and as clear as the Constitution, and he asked his white audience whether they would accept for themselves the treatment Black Americans received at lunch counters, at schools, and at the registrar's office. Only then did he promise the bill, asking Congress to act on the proposition that race has no place in American life or law. Teach the promise at its exact size. A president announcing a bill is not a law. The address moved the presidency into the fight. Congress, where the bill would spend the rest of the year, is the subject the march took up next.",
             kick='D · The president moved', size=24)

# ------------------------------------------------------ 13 SECTION D CONTENT 2
content_text('The same night, in Jackson',
             ['Medgar Evers served as NAACP field secretary for Mississippi.',
              'An assassin shot Evers in his driveway on June 11.',
              'The bill went to Congress and stalled there.',
              'Pressure had produced a promise, not a law.'],
             "Close the section with the night's second event, stated plainly and without decoration. Medgar Evers was the NAACP's field secretary for Mississippi, a veteran who had investigated lynchings, organized boycotts, and applied to the University of Mississippi law school and been turned away for his race. He came home late on June 11 from a rally, and an assassin shot him in the driveway of his home in Jackson. He died that night. His murder belongs in this lesson beside the address, not after it, because the two events measure each other: on the same day the federal government committed its voice to the movement's central demand, the movement's Mississippi organizer was killed at his own door. Then state the legislative position exactly, because the writing task tests it. Kennedy sent the bill to Congress in June. The southern bloc opposed it, the committees held it, and it was still unpassed when 1963 ended. Everything the march did in August was done in support of a bill that existed and was stuck.",
             kick='D · The president moved', size=24)

# ------------------------------------------------- 14 SECTION E DIVIDER
divider_photo('leaders-port.jpg', 'Section E', 'A March Older Than the Summer',
              ['The march leaders on August 28, 1963,', 'photographed by Rowland Scherman for the USIA.'],
              "The photograph, by Rowland Scherman of the United States Information Agency, shows the leaders of the march on August 28, 1963, among them A. Philip Randolph, the elder at the center of this section. Section E explains why the march had a history before Birmingham made it necessary. Randolph had threatened a march on Washington once before, in 1941, demanding jobs in the defense industries, and President Roosevelt had answered the threat with a fair employment order rather than face the march itself. The march of 1941 never had to happen. In 1963 Randolph returned, in his seventies, as the new march's elder leader, and Bayard Rustin, who had organized for him in 1941, ran the logistics of this one: the buses and trains, the trained marshals, the water and first aid, the reviewed program. Teach the pairing on purpose. Randolph carried the demand for jobs across twenty two years. Rustin carried the machinery. The march students picture as a single August day was the second use of an old weapon, rebuilt by the two men who had first built it.",
              title_size=38)

# ------------------------------------------------------ 15 SECTION E CONTENT
content_text('Ten demands, for jobs and freedom',
             ['The march demanded a comprehensive civil rights law in that session.',
              'The march demanded desegregation of the public schools within the year.',
              'The march demanded a federal law against discrimination in employment.',
              'The march demanded a two dollar minimum wage.',
              'The march demanded federal funds be withheld from programs that discriminate.'],
             "Take the demands as a document, because the activity's fourth station works from the march's own printed program and organizing plans. The plans state the march's purpose in the organizers' words: to redress old grievances and resolve a crisis born of twin evils, racism and economic deprivation, which together denied the vote, closed public accommodations, delivered inferior education and substandard housing, and left Black unemployment at nearly three times the white rate. The ten demands answer that diagnosis item by item, and their addressee is the lesson inside the list. Nearly every demand asks the federal government to act: Congress to pass the civil rights law and the fair employment law and the minimum wage, the executive to withhold federal funds from discriminatory programs and to enforce the Fourteenth Amendment. After Birmingham, the movement had won what one city's merchants could give. The demands record its conclusion about where the rest had to be won. Rustin read the full list aloud at the Lincoln Memorial, and the crowd answered each demand with its approval, which made the program a vote as well as a speech.",
             kick='E · A march older than the summer', size=24)

# ------------------------------------------------- 16 SECTION F DIVIDER
divider_photo('crowd-port.jpg', 'Section F', 'August 28 at the Lincoln Memorial',
              ['The crowd along the Reflecting Pool,', 'August 28, 1963. National Archives photograph.'],
              "The photograph is a National Archives photograph of the crowd at the Lincoln Memorial on August 28, 1963, marchers filling the ground along the Reflecting Pool farther than the camera reaches. Section F covers the day itself, and it should be taught as a program, in order, the way the quarter of a million people in this photograph experienced it. Randolph, the elder, opened it. The organizations that had argued all summer stood on one platform. John Lewis, twenty three years old and the chairman of the Student Nonviolent Coordinating Committee, spoke after cutting his sharpest criticisms of the administration's bill under pressure from the march's other leaders, a censorship students should know about rather than discover later, because it shows the discipline the day cost. Singers performed between the speeches. Rustin read the ten demands to the crowd's shouted answers. And King, the last speaker, closed the program with the address this unit's vocabulary names, and which the next slides take up in paraphrase, with one short passage quoted in the reading only.",
              title_size=38)

# ------------------------------------------------------ 17 SECTION F PHOTO
content_photo_s('payne-port.jpg', 'The program, hour by hour',
              ['Randolph opened the program by stating its purpose.',
              'Lewis spoke after cutting his sharpest lines.',
              'Rustin read the ten demands aloud.',
              'The crowd answered each demand with its approval.',
              'King spoke last and closed the day.'],
              "The photograph, by Rowland Scherman for the United States Information Agency, shows Edith Lee-Payne of Detroit, who turned twelve on the day of the march, holding a banner for jobs and freedom. Hold her in view while the program runs, because she is the day's scale made personal: the march was not only its platform. It was a twelve year old from Detroit standing in the heat with a hand lettered banner, one of about a quarter of a million people who had come by chartered bus and train and gone home the same night. The organizers had promised a disciplined day and delivered it: trained marshals, reviewed speeches, a program that ended on time, and a city emptied by nightfall, which was itself an argument, that the movement could assemble the largest demonstration in the capital's history and conduct it in order. The Kennedy administration, which had first tried to prevent the march, ended the day relieved. The bill's supporters ended it able to say, with a photograph to prove it, that the country behind the bill could be seen.",
              kick='F · August 28 at the Lincoln Memorial', size=19)

# ------------------------------------------------------ 18 SECTION F STAT
stat('250,000', 'people at the Lincoln Memorial, August 28, 1963',
     'About a quarter of a million, by the organizers\u2019 and the press count · For jobs and freedom',
     "Give the number its evidence and its limits together. About 250,000 is the figure the march's own record and the press count of the day support, and the vocabulary definition students copy uses it: about 250,000 people at the Lincoln Memorial. From the air and from the ground the crowd filled the Reflecting Pool grounds between the Washington Monument and the memorial, as the photographs in this lesson show. Then say what the number was for. It was not decoration on the day. It was the march's central exhibit, a constituency made visible in one place, assembled to be counted by Congress and by the television audience at home. A rally in a southern city could be described as local. A quarter of a million people in the capital, drawn from every state, arriving in order and leaving in order, could not. Students should also hear the honest limit the writing task will press on: the crowd's size did not change the Senate's arithmetic that summer, and the bill it backed was still unpassed in December.",
     kick='F · August 28 at the Lincoln Memorial')

# ------------------------------------------------------ 19 SECTION F CONTENT 2
content_text("King's closing address, in paraphrase",
             ['King read the founding documents as a promise.',
              'The promise had been made to every American and not yet honored.',
              'King described the country beyond the bill.',
              'One passage of 35 words is quoted in the reading.',
              "King's words are paraphrased everywhere else in this lesson."],
             "Teach the closing address the way this lesson is required to teach it: in paraphrase, with the single quoted passage living in the reading. Paraphrased, King's argument ran as a claim on a debt. The Declaration of Independence and the Constitution, he argued, had promised liberty and equality to every American when they were signed, and the nation had honored that promise for some of its citizens and not for others, and the marchers had come to the capital to collect what was owed rather than to ask for something new. Then, in the address's best known movement, he set the pending bill aside and described the country on the far side of it, a country in which his own children would be judged as persons in full, by who they were rather than by their race. The crowd answered the address the way a congregation answers, and the day closed on it. Name the discipline once more for the class: the address is under copyright, this unit quotes thirty five words of it in total, and those words are in the reading, not on this screen.",
             kick='F · August 28 at the Lincoln Memorial', size=24)

# ------------------------------------------------- 20 SECTION G DIVIDER
divider_text('Section G', 'The Answer from Birmingham',
             'September 15, 1963. Four girls, named in this lesson every time they are counted.',
             "Teach this section at a level voice, with the facts in order and nothing added for effect. Eighteen days after the march, on Sunday, September 15, 1963, Birmingham answered the summer in the movement's own gathering place. The 16th Street Baptist Church had been the spring campaign's meeting ground, and it was the church the schoolchildren had marched from in May. That morning the congregation was preparing for Youth Day, the Sunday when its young people took part in the adult service. During the night, members of the Ku Klux Klan had planted dynamite beneath the church's side steps. It exploded at 10:22 in the morning. There is no photograph in this section, by decision, and students can be told why in one sentence: this lesson states the bombing in words and names, and does not use pictures of its damage as teaching decoration. What the record requires is accuracy about who was killed, and the next two slides carry it.")

# ------------------------------------------------------ 21 SECTION G CONTENT
content_text('September 15: the four girls',
             ['Addie Mae Collins was fourteen years old.',
              'Cynthia Wesley was fourteen years old.',
              'Carole Robertson was fourteen years old.',
              'Carol Denise McNair was eleven years old.',
              'The blast injured more than twenty other people.'],
             "Use the guided notes definition in full, and then stop and let it stand: the 16th Street Baptist Church bombing is the bombing of a Birmingham church by Ku Klux Klan members on September 15, 1963, which killed four Black girls, Addie Mae Collins, Cynthia Wesley, Carole Robertson, and Carol Denise McNair, as they prepared for Sunday services. The girls had been in a basement restroom, in their Sunday dresses, preparing for the Youth Day service. Addie Mae Collins, Cynthia Wesley, and Carole Robertson were fourteen years old. Carol Denise McNair was eleven. A fifth girl, Sarah Collins, Addie Mae's sister, survived the blast and lost the sight of one eye. More than twenty other people in the church were injured. A joint funeral for three of the girls drew thousands of mourners, and King preached the eulogy. No Birmingham city official attended. Grade the names exactly wherever this lesson tests them, in the quick check, in the notebook, and on the unit test. The names are not detail around the record. In this section they are the record.",
             kick='G · The answer from Birmingham', size=24)

# ------------------------------------------------------ 22 SECTION G CONTENT 2
content_text('What had not moved by December',
             ['The civil rights bill was still stalled in Congress.',
              'The first bombing conviction came in 1977.',
              'The last bombing convictions came in 2001 and 2002.',
              'The year had moved a president, and not yet a law.'],
             "Close the year's account with its two unfinished items side by side, because their pairing is the lesson's last fact. The first is the bill. Kennedy had announced it on June 11 and sent it to Congress, the march had backed it with a quarter of a million people on August 28, and after the bombing it remained where the southern bloc and the committees had held it all autumn: unpassed at the year's end. It would pass in the next year, under a new president, and that story belongs to the next lesson. The second item is justice for the bombing itself. The federal investigation identified the bombers, and the state of Alabama did not convict the first of them, Robert Chambliss, until 1977, fourteen years later. Thomas Blanton was convicted in 2001 and Bobby Frank Cherry in 2002. A fourth suspect died before he could be tried. Students should leave with the year's shape whole: the fastest movement of public pressure in the century, and, beside it, a law and a set of verdicts that arrived years late or not within the year at all.",
             kick='G · The answer from Birmingham', size=24)

# ------------------------------------------------------ 23 GLANCE
s = slide(NAVY)
kicker(s, 'The Year at a Glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Pressure, promise, and price', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Birmingham', 'Project C, the Letter, the children', 'A local settlement, and a national audience'),
        ('The president', 'June 11 address, the bill announced', 'The presidency moved; Congress did not, yet'),
        ('The march', 'August 28, ten demands, 250,000 people', 'A national constituency, made visible'),
        ('September 15', 'The church bombing, four girls killed', 'The bill still stalled at the year\u2019s end')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, The Year at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The four rows are the lesson's argument in miniature. Birmingham supplied the pressure in its three forms: a campaign built to create a crisis, a letter that gave the crisis its fullest argument, and children whose treatment on television gave it a national audience, ending in a settlement one city signed. The president's row must be completed in two parts or it is wrong: the address and the announced bill of June 11 belong there, and so does the stall that followed. The march row carries the constituency, a quarter of a million people behind ten demands. The last row carries the price and the limit together: four girls killed on September 15, named in full, and a bill still unpassed in December. Grade the table generously on wording and strictly on that last row's two facts.")

# ------------------------------------------------------ 24 VOCAB A
vocab('Words for Birmingham and the president',
      [('Birmingham campaign', '1963: SCLC and the local movement; repression televised'),
       ('Letter from Birmingham Jail', "King's April 1963 answer to eight clergymen"),
       ("Children's Crusade", 'May 1963: students met hoses, dogs, and jail'),
       ("Kennedy's civil rights address", 'June 11, 1963: a moral issue, a bill announced')],
      "These definitions match the guided notes word for word, and students copy them exactly. Birmingham campaign: the protest campaign of 1963 in Birmingham, Alabama, led by the Southern Christian Leadership Conference and the local movement, whose televised repression pushed President Kennedy to propose a national civil rights bill. Letter from Birmingham Jail: Martin Luther King Jr.'s letter of April 1963, written from a Birmingham jail cell, defending nonviolent direct action against white clergymen who had called his protests unwise and untimely. Children's Crusade: the marches of May 1963 in Birmingham in which thousands of Black schoolchildren left their classes to demonstrate and were met with fire hoses, police dogs, and jail, producing the images that turned national opinion. Kennedy's civil rights address: President Kennedy's televised address of June 11, 1963, after the Birmingham crisis, calling civil rights a moral issue and announcing that he would send Congress a comprehensive civil rights bill.")

# ------------------------------------------------------ 25 VOCAB B
vocab('Words for the march and September',
      [('March on Washington', 'August 28, 1963: about 250,000 people, jobs and freedom'),
       ('I Have a Dream', "King's closing address: a claim on the founding promises"),
       ('16th Street Baptist Church bombing', 'September 15, 1963: four girls killed')],
      "Three more terms, again matching the guided notes exactly, and students copy them as written. March on Washington: the demonstration of August 28, 1963 that brought about 250,000 people to the Lincoln Memorial to demand jobs and freedom and to press Congress to pass the civil rights bill. I Have a Dream: Martin Luther King Jr.'s address closing the March on Washington on August 28, 1963, casting the movement's demands as a claim on the promises of the Declaration of Independence and the Constitution. 16th Street Baptist Church bombing: the bombing of a Birmingham church by Ku Klux Klan members on September 15, 1963, which killed four Black girls, Addie Mae Collins, Cynthia Wesley, Carole Robertson, and Carol Denise McNair, as they prepared for Sunday services. End the vocabulary on the discipline this lesson keeps for the second term: the address is quoted once in this lesson, thirty five words in the reading, and paraphrased everywhere else.")

# ------------------------------------------------------ 26 SYNTHESIS
s = slide(NAVY)
kicker(s, 'Synthesis')
text(s, 0.9, 1.35, 11.5, 1.1, 'What 1963 proved, and what it left', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 3.4,
     ['Birmingham forced the hand by stages: a campaign built for crisis, a letter that argued the case, children on television, and merchants who settled within a week.',
      'The president answered in June with a moral claim and a bill, and the march answered in August with ten demands and a quarter of a million people behind them.',
      'By December the bill was still unpassed and four girls were dead in Birmingham, which is the measure of what pressure had won and what it had not.'],
     size=21, color=POWDER, leading=1.3)
notes(s, "Draw the lesson together before the exit work, and do it by answering the lesson question in full sentences students can borrow. How did Birmingham force the nation's hand? By stages that each added what the last one lacked: Project C created the confrontation, the Letter from Birmingham Jail gave the confrontation its argument in a document the country read, the Children's Crusade gave it a national audience on television, and the merchants' settlement proved the pressure could win, until a president who had announced no bill in April announced one on June 11. What did the march ask the nation to become? The country its founding documents had already described on paper: the ten demands named the work, jobs and freedom together, and King's closing address, paraphrased in this lesson and quoted once in the reading, presented those demands as a claim on promises signed at the founding and not yet honored. Close on the limit, because the unit question asks what was left unfinished: in December 1963 the bill was unpassed, and the unfinished business is the next lesson's subject.")

# ------------------------------------------------------ 27 CLOSING / EXIT
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did Birmingham force the nation\u2019s hand, and what did the March on Washington ask the nation to become? Build from the documents, and keep the year in order.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Pressure File: five records, a chain of pressure, and a verdict'),
        ('Notebook', 'Notebook page: six stages in a chart, and pressure and its price in one paragraph'),
        ('Quick check', 'The Photograph and the Promise: the march, the Letter, and September 15'),
        ('Writing', 'Which Did More, Birmingham or the March? Argued from the file')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: why Birmingham was chosen, two demands and the unhonored promise, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Pressure File, runs five records in order: the Letter from Birmingham Jail, quoted in two short passages totaling sixteen words with the rest of its argument in labeled paraphrase; Kennedy's address of June 11, quoted from the audited record; a labeled summary record of the Children's Crusade; the march's organizing plans and its ten demands, summarized from the printed program; and a labeled summary record of the church bombing. Students keep a chain of pressure across the file and close with a verdict on whether Birmingham or the march did more to move the federal government, answering the strongest counterclaim. The quick check tests the chain from May to June, the march's demands, and the names and ages of September 15. The writing task asks the activity's verdict question as an essay, argued from an evidence bank drawn from the file. The exit ticket has three parts: why Birmingham was chosen, two demands with the founding promise King named, and the lesson question answered with at least two dates.")

dc.save(OUT)
