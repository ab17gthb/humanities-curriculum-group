#!/usr/bin/env python3
"""Civil Rights Lesson 4 deck, "Sit-Ins and Freedom Rides: The Students
Take the Lead," built to the approved system: image-led slides, fragments
only on screen, comprehensive speaker notes, full lesson + vocabulary
coverage. Fonts: Georgia titles, Lato body."""
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
OUT = os.path.join(HERE, '..', 'lesson-04-slides.pptx')

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

# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'THE CIVIL RIGHTS MOVEMENT · LESSON 4', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Sit-Ins and Freedom Rides', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'The students take the lead, 1960 to 1962', size=17, color=POWDER)
notes(s, "The photograph shows a traveler standing under the Colored Waiting Room sign at the bus station in Durham, North Carolina, in May 1940, photographed by Jack Delano for the Farm Security Administration and held by the Library of Congress. Open with the date. The segregated system in this photograph was twenty years old when this lesson begins, and it still governed where a traveler could wait, eat, or use a restroom across the South. Between February 1960 and the fall of 1961, students barely out of high school attacked that system at lunch counters and in bus terminals, and forced the federal government to enforce rights it had already declared. Tell students the lesson follows the order of their guided notes, sections A through G, from a Greensboro lunch counter to a Georgia city where the same methods failed, and that the activity file will ask them at every stage what crisis the students created and who answered it.")

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("How did students a decade younger than the movement's leaders change its pace, its tactics, and its demands?", {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the civil rights movement change American law and American life, and what did it leave unfinished?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Read the question slowly and take its three verbs one at a time. Pace: before February 1960 the movement moved at the speed of court cases and national organizations; after it, any student in any town could open a front in a week. Tactics: the students replaced the lawsuit and the one day boycott with the sustained occupation of segregated space, the filled jail, and the interstate bus ridden straight into the hardest counties. Demands: they stopped asking for gradual improvement and demanded service now, on equal terms, at the counter in front of them. Keep the ages in front of the class all hour. The Greensboro four were freshmen. Diane Nash was twenty one. Martin Luther King Jr. was thirty one in 1960, a full decade older, and in this lesson the older leaders repeatedly follow where students have already gone, most plainly when King comes to Albany after SNCC has been there for months.")

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Seven steps in eighteen months', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'Greensboro: four students at a lunch counter', 'February 1, 1960, and a tactic is born'),
        ('B', 'A tactic any student could copy', 'Sit-ins in more than a hundred cities'),
        ('C', "Nashville: training, jails, and a mayor's answer", 'Workshops, filled jails, counters opened'),
        ('D', 'The students organize: SNCC', 'Shaw University, April 1960, Ella Baker'),
        ('E', 'The Freedom Rides: testing Boynton', 'Thirteen riders leave Washington, May 1961'),
        ('F', 'Fire at Anniston, prison at Parchman', 'Violence, arrests, and four hundred more riders'),
        ('G', 'The federal answer and the Albany limit', 'The ICC acts; Pritchett absorbs the protest')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This slide is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A is Greensboro, where four freshmen invent the sit-in as a mass tactic. Section B follows the tactic across the South. Section C is Nashville, where training and jail filling win a major city. Section D is the founding of the Student Nonviolent Coordinating Committee at Shaw University. Sections E and F are the Freedom Rides, the court decision they tested, and the violence and imprisonment that followed. Section G closes with the Interstate Commerce Commission regulations of September 1961 and the Albany campaign, where the same methods met a police chief who had studied them. Tell students the summary table at the end of their guided notes asks them to rebuild this map stage by stage, with a cost or risk attached to every stage.")

# 4 SECTION A DIVIDER
divider_text('Section A', 'Greensboro: Four Students at a Lunch Counter',
             'February 1, 1960. Four freshmen, one store, and a refusal that would not move.',
             "Set the scene with care, because students often imagine the sit-in as a spontaneous gesture by students who had not thought it through. The four freshmen at North Carolina Agricultural and Technical College had talked for months in their dormitory rooms. Joseph McNeil had been refused service at a bus terminal lunch counter while traveling back from military reserve duty, and the four had read and argued about the Constitution and about the movement's slow pace. They chose Woolworth because a national chain was vulnerable in a way a local store was not: its northern stores served Black customers, and its name was known everywhere. They also bought small items first and kept their receipts, proof that the store was glad to take their money everywhere except at the counter. The protest was planned down to that detail, and students should register the planning, because the lesson's argument about students changing the movement begins with how deliberate they were.")

# 5 GREENSBORO
content_text('They stayed until the store closed',
             ['Four freshmen sat at the Woolworth counter on February 1, 1960.',
              'Refused service, they studied and stayed until closing.',
              'They returned each day with more students.',
              'Within a week, hundreds were sitting in across Greensboro.',
              'On July 25, 1960, the counter served Black customers.'],
             "Walk the first day slowly. The four bought school supplies and other small items, kept their receipts, and then sat at the lunch counter and asked for coffee and food. The waitress refused, an older Black employee told them they were hurting their own people, and the manager watched. The four stayed until the store closed, reading and studying, and they told a reporter they would return. Notice what did not happen on the first day: no arrest, no violence, no federal official, no national leader. The power of the event was its repeatability. Each day the crowd of students grew, the newspapers photographed rows of well dressed students at the counter, and the store faced a choice it could not escape, serve them, close the counter, or have them removed by force on camera. Woolworth held out for nearly six months and then, on July 25, 1960, quietly served its first Black customers at that counter, four store employees in their work clothes among them in some accounts. The students had won with a tactic that cost almost nothing.",
             kick='A · Greensboro', size=23)

# 6 STAT FOUR
stat('4', 'freshmen began the Greensboro sit-in',
     'February 1, 1960 · Joseph McNeil, Ezell Blair Jr., Franklin McCain, and David Richmond, all students at North Carolina A&T',
     "Let the smallness of the number do the teaching. Four students, none of them officers of any national organization, none older than eighteen or nineteen, opened the campaign that reshaped the movement. Set the four beside the institutions of the earlier lessons: the NAACP, founded in 1909, with its lawyers and its decades of litigation; the churches and colleges of Lesson 1; the Supreme Court itself, whose Brown decision was six years old. Those institutions had built the ground, and students should not be taught to dismiss them. But the decision to sit down on February 1, 1960 was taken in a dormitory, not a boardroom, and it was taken by freshmen who had concluded that the existing pace was too slow. Ask the class to hold two facts together for the rest of the lesson: the students stood on ground the older movement had built, and they moved faster than the older movement had planned to move. That tension runs through SNCC's founding in section D and through Albany in section G.",
     kick='A · Greensboro')

# 7 SECTION B DIVIDER
divider_text('Section B', 'A Tactic Any Student Could Copy',
             'No budget, no headquarters, no permission. By the end of 1960, sit-ins in more than a hundred cities.',
             "Section B explains the spread, and the explanation is the tactic's design. A lunch counter sit-in needed nothing that could be confiscated, funded, or enjoined in advance. It needed students, a segregated counter, and the discipline to stay seated. The targets stood in every southern town, and the chain stores that ran many of them answered to national offices in New York, which northern supporters could picket in sympathy. Television and the wire services did the rest: a photograph of students in coats and ties being shouted at over a counter carried the story further in a day than a pamphlet could in a year. Students should also see the limit built into the design. A sit-in could open a lunch counter. It could not by itself register a voter, desegregate a school system, or employ anyone, and the movement's later turns toward voter registration and federal legislation begin in that limit. For now, ask the class to name what the tactic required of the people who used it, because Nashville answers that question next.")

# 8 SPREAD
content_text('More than a hundred cities by the end of 1960',
             ['Students sat in at counters, libraries, theaters, and pools.',
              'They dressed in their best clothes and carried their books.',
              'Insults and blows were absorbed, never returned.',
              'Northern supporters picketed the same chain stores.',
              'Local campaigns were run by local students, city by city.'],
             "Teach the spread as a series of local decisions rather than a wave that carried people along. In each city, students at a Black college or high school chose their target, trained as well as they could, and sat in, knowing the local record of arrests and violence. The discipline was the message. Students wore their best clothes, brought books and homework, and refused to answer insults or blows, so that the only disorder in the photograph was the disorder directed at them. The economic pressure was real but modest at any single store; the political pressure was the larger weapon, because each sit-in forced a city to declare, in public, whether it would defend a lunch counter's customs with its police. By the end of 1960 students had sat in in more than a hundred southern cities. Some counters opened quickly, some only after months, and some not at all, which is why the movement needed the organization and the federal strategy built later in this lesson. The tactic spread because it was copyable; it won where preparation and pressure met, which Nashville shows in full.",
             kick='B · The tactic spreads', size=23)

# 9 SECTION C DIVIDER
divider_photo('nash-port.jpg', 'Section C', "Nashville: Training, Jails, and a Mayor's Answer",
              ['Diane Nash and the Reverend Kelly Miller Smith,', 'Nashville, April 9, 1960.'],
              "The photograph shows Diane Nash and the Reverend Kelly Miller Smith in Nashville on April 9, 1960, reviewing a statement that answered the city's biracial committee, photographed by Gerald Holly for The Tennessean and held to be public domain on its Wikimedia Commons file page because the copyright was not renewed. Section C is the lesson's study in preparation. Nashville's students came from Fisk University, Tennessee State, Meharry Medical College, and American Baptist College, and they had been training since the fall of 1959, months before Greensboro, in workshops run by the Reverend James Lawson. When their moment came, they were the best prepared sit-in students in the South, and their campaign is the one that produced the movement's first major city victory. Nash, a Fisk student of twenty one, became its public voice, and her exchange with the mayor on the courthouse steps is the section's center. Students should watch for what training purchased: the ability to keep discipline after arrests, after a bombing, and at the moment of negotiation itself.",
              title_size=36)

# 10 NASHVILLE WORKSHOPS
content_text('Trained before they sat down',
             ["James Lawson's workshops ran from the fall of 1959.",
              'Students practiced absorbing insults and blows.',
              'The rule was to meet hatred without returning it.',
              'On February 27, 1960, they were beaten, arrested, and jailed.',
              'They filled the jails rather than post bail.'],
             "Describe the workshops concretely, because students romanticize nonviolence as temperament when Nashville treated it as a skill. In Lawson's sessions, students sat on stools while their classmates shouted insults, blew smoke, shoved them, and pulled them to the floor, and the students practiced protecting their heads, keeping their hands down, and helping each other back onto the stools. Lawson, who had studied nonviolence in India, taught the theology and the strategy together: the demonstrator's task was to expose the violence inside segregation by refusing to add any of his own. The test came on February 27, 1960, when Nashville sit-in students were attacked at the counters and then arrested, the attackers left alone. The students refused bail and filled the jails, a choice that raised the city's cost of holding them and kept the campaign's initiative with the students. Expulsion threats from the colleges followed and were beaten back. By April the students, not the city, were setting the terms of the confrontation.",
             kick='C · Nashville', size=23)

# 11 NASHVILLE ANSWER
content_text("A mayor's answer on the courthouse steps",
             ['On April 19, 1960, the Looby home was bombed.',
              'Thousands marched in silence to the courthouse.',
              'Diane Nash questioned Mayor Ben West directly.',
              'West answered that discrimination by skin color was wrong.',
              'On May 10, 1960, Nashville opened its lunch counters.'],
             "Narrate April 19 in order. In the early morning a bomb wrecked the home of Z. Alexander Looby, the students' lawyer and a city councilman. No one was killed, and by midday thousands of students and residents marched to the courthouse in silence, a discipline the whole city could read. On the steps, Diane Nash confronted Mayor Ben West. She asked whether he believed it was wrong to discriminate against a person by the color of his skin. West answered that it was wrong, and when she pressed him on the counters themselves, he agreed they should be opened to everyone. The exchange took minutes, and it worked because the march behind her made evasion more costly than concession. Three weeks of negotiation followed, and on May 10, 1960, Nashville became the first major southern city to desegregate its lunch counters. Mark the shape of the victory for the class: a local crisis, aimed at a local power, answered by that power. No federal official appears in this story, which becomes an important contrast when the riders need Washington in section F.",
             kick='C · Nashville', size=23)

# 12 SECTION D DIVIDER
divider_text('Section D', 'The Students Organize: SNCC',
             'Shaw University, April 1960. Ella Baker tells the students to build their own organization.',
             "Section D is short in the reading and large in the unit. By April 1960 the sit-ins had produced something the movement had not planned: a generation of tested local leaders, most of them under twenty two, who owed their authority to arrests they had served rather than to offices they held. The question was what structure that generation would take. The Southern Christian Leadership Conference, King's organization, called the conference at Shaw University in Raleigh that Easter weekend, and a youth wing of the SCLC was the expected outcome. Ella Baker, the SCLC's acting executive director and the conference's organizer, argued against it. Baker had spent decades organizing for the NAACP, and she believed movements were built by developing local leaders, not by gathering followers around a national voice. She urged the students to found an organization of their own. They did, and the habits Baker taught it mark every campaign in the rest of this unit, including the voter registration work of Lesson 6.")

# 13 SNCC
content_text('An organization of their own',
             ['They met at Shaw University in Raleigh in April 1960.',
              'Ella Baker urged independence from the older groups.',
              'The Student Nonviolent Coordinating Committee was founded.',
              "Baker's rule was that local people lead their own fights.",
              'SNCC went to the deepest parts of the South, and stayed.'],
             "Give students the founding facts and then the operating habits, because the test asks about both. The conference met at Shaw University in Raleigh, North Carolina, in April 1960, drawing student leaders from the sit-in cities. The organization they founded took the name Student Nonviolent Coordinating Committee, known everywhere as SNCC. Its structure was deliberately loose: field secretaries went into a county, found the people already respected there, and built the campaign around them, rather than importing a program. Baker's rule, that local people lead their own fights, was both a democratic conviction and a survival strategy, since a local leader could not be transferred away or fired by a distant board. SNCC workers lived on subsistence pay, stayed in the hardest counties after the cameras and the national staff left, and accepted risks the older organizations often judged too high. In this lesson SNCC appears first as a child of the sit-ins, then as the reinforcements of the Freedom Rides, and finally as the organizer who reached Albany first. Track those appearances; they are the organization's biography in one lesson.",
             kick='D · SNCC', size=23)

# 14 SECTION E DIVIDER
divider_photo('farmer-port.jpg', 'Section E', 'The Freedom Rides: Testing Boynton',
              ['James Farmer of CORE, photographed by Jackson,', 'Mississippi police after his arrest, May 24, 1961.'],
              "The photograph is the Jackson, Mississippi police mug shot of James Farmer, taken on May 24, 1961, after his arrest as a Freedom Rider, and marked public domain on its Wikimedia Commons file page. Farmer was the national director of the Congress of Racial Equality, and at forty one he was a generation older than the students of this lesson, a founder of CORE in 1942 who had pioneered the nonviolent direct action the students now practiced. Section E sets up the Freedom Rides as a legal test before it becomes a physical ordeal. In December 1960 the Supreme Court had decided Boynton v. Virginia, reversing the trespass conviction of a Black law student who had refused to leave the white section of a bus terminal restaurant. The right existed in the United States Reports. What did not exist was southern obedience to it, and CORE designed the rides to find out whether a declared right would be honored when ordinary travelers claimed it in person.",
              title_size=38)

# 15 BOYNTON
content_text('A right declared, and unenforced',
             ['Boynton v. Virginia was decided in December 1960.',
              'A law student had been convicted of trespass in a terminal restaurant.',
              'The Court reversed the conviction.',
              'Terminal services had to be given without discrimination.',
              'Five months later, the terminals were still segregated.'],
             "State the holding in the Court's own structure, because the activity file quotes it and the quick check tests it. Bruce Boynton, a Black law student traveling by bus, sat in the white section of the restaurant in the Richmond Trailways terminal, refused to move to the section for Black customers, and was convicted of trespass under Virginia law. The Supreme Court reversed. When a bus carrier makes terminal and restaurant facilities available to its interstate passengers as a regular part of their transportation, the Court held, the terminal and restaurant must perform those services without the discriminations prohibited by the Interstate Commerce Act. Note the ground: a federal statute, not the Fourteenth Amendment, which let the Court decide for Boynton without ruling on segregation generally. Then make the enforcement gap vivid. The decision came in December 1960, and through the winter and spring the terminals kept their white and colored signs. No agency inspected them. A right that nobody enforces is a claim, and the Freedom Rides were designed to convert the claim into a test the federal government would have to grade.",
             kick='E · Boynton', size=22)

# 16 DEPARTURE
content_text('Thirteen riders leave Washington',
             ['On May 4, 1961, they rode Greyhound and Trailways buses.',
              'Seven riders were Black and six were white.',
              'CORE organized the rides, and Farmer led the first group.',
              'At each stop, they used the white waiting room and lunch counter.',
              'Their destination was New Orleans, by way of the deep South.'],
             "Walk the plan as its organizers understood it. Thirteen riders, seven Black and six white, divided between a Greyhound bus and a Trailways bus, left Washington on May 4, 1961. Black riders would sit in the front of the buses and use the white waiting rooms, restrooms, and lunch counters at each stop; white riders would use the facilities marked for Black travelers. The destination was New Orleans, reached on May 17, the seventh anniversary of Brown. The route ran through Virginia and the Carolinas into Georgia, Alabama, and Mississippi, deliberately entering the states where Boynton was most openly defied. Farmer and his colleagues expected arrests and probable violence, and the riders had trained in nonviolent discipline and made out wills before leaving. The first week passed with scattered arrests and little national notice, which is worth telling students plainly: as long as the South answered with routine arrests, the test produced no crisis. The crisis came when Alabama answered with a mob, and section F takes up that answer in plain terms.",
             kick='E · The rides begin', size=23)

# 17 SECTION F DIVIDER
divider_photo('reagon-port.jpg', 'Section F', 'Fire at Anniston, Prison at Parchman',
              ['Cordell Reagon, photographed by Jackson, Mississippi', 'police after his arrest, June 2, 1961.'],
              "The photograph is the Jackson, Mississippi police mug shot of Cordell Reagon, a Nashville student and SNCC worker, taken on June 2, 1961, and marked public domain on its Wikimedia Commons file page as a work of the Jackson police. Reagon's face belongs to section G as much as to this one, since he carried the organizing into Albany that fall. Section F covers the ordeal of May and June 1961 in the plain terms the lesson has used throughout: exact places, exact dates, no embellishment, because the documented facts need none. Teach the sequence as an escalation with a logic. Alabama's mobs tried to end the rides by terror. Mississippi's officials tried to end them by processing the riders through arrest, conviction, and imprisonment. The Kennedy administration tried to end them by negotiation, offering protection in exchange for a pause. The riders, reinforced by Nashville students when the original group could not continue, refused every ending offered to them, and that refusal is what converted a two week test into a summer long crisis the federal government finally had to settle.",
              title_size=38)

# 18 MAY 14
content_text('May 14, 1961: Anniston and Birmingham',
             ['A mob attacked the Greyhound bus outside Anniston.',
              'A firebomb was thrown, and the doors were held shut.',
              'Riders escaped the burning bus and were beaten.',
              'In Birmingham, riders were beaten at the terminal.',
              'Police had been arranged to be absent.'],
             "Teach May 14 in plain sequence, and keep the language exact. Near Anniston, Alabama, a mob surrounded the Greyhound bus, slashed its tires, and followed it out of town. When the bus stopped, a firebomb was thrown through a window and the doors were held shut while the bus burned; the riders escaped through the windows and the rear door and were beaten as they came out. Several were hospitalized. The Trailways bus reached Birmingham, where riders were beaten at the terminal by a mob that Police Commissioner Eugene Connor had arranged to face no police for its first minutes. The Federal Bureau of Investigation had been told of the Birmingham plan in advance, a fact students will meet again in later study. Pause on the design of the test: the riders had claimed facilities the Supreme Court had opened, in daylight, without weapons, and the answer was attempted murder by fire. Whatever the administration in Washington preferred, the photographs of the burning bus made the Freedom Rides a national question within the day, which is precisely the mechanism the riders had counted on.",
             kick='F · The ordeal', size=23)

# 19 JACKSON PARCHMAN
content_text('The rides continue, into Parchman',
             ['On May 20, riders were beaten at the Montgomery bus station.',
              'Federal marshals were sent to Montgomery.',
              'Nashville students replaced the injured riders.',
              'Jackson arrested riders who used the white waiting room.',
              'Refusing fines, riders were sent to Parchman prison.'],
             "Follow the crisis to Mississippi, and mark who kept it alive. After the Montgomery beating of May 20, in which a Justice Department official was knocked unconscious, the administration sent federal marshals and pressed the riders to accept a cooling off period. CORE's injured group could not continue, and the rides should have ended there. Instead, Nashville students organized by Diane Nash insisted on continuing, writing that they would not stop until the job was done, and rode from Montgomery to Jackson. Mississippi's answer was orderly: arrest in the white waiting room, a breach of peace conviction, and a choice of fine or jail. The riders chose jail, were stripped of bedding and books at Parchman, the state penitentiary, and sang freedom songs through the cellblock bars. Through the summer more than four hundred riders, most of them students, rode into the South and filled its jails. The administration's problem compounded weekly: every new busload renewed the question of whether federal law ran in interstate terminals. On May 29, Attorney General Robert Kennedy petitioned the Interstate Commerce Commission for the regulations that end this section of the story.",
             kick='F · The ordeal', size=22)

# 20 STAT RIDERS
stat('400+', 'Freedom Riders rode into the South in 1961',
     'May to November 1961 · Most of them students · Arrested in Jackson and sent to Parchman when they refused their fines',
     "Use the number to correct a common picture of the rides as a single bus and a single week. The first group numbered thirteen. By the end of the summer, more than four hundred riders had ridden into the South, the great majority of them students, Black and white, from colleges across the country, and most were arrested in Jackson, Mississippi, for using the white side of the terminal. The supply of riders was the strategy. Alabama's violence was supposed to make the price of riding higher than students would pay; instead, each attack recruited the next busload, and the jails and then Parchman prison filled with young people whose families, colleges, and home newspapers followed their cases. That arithmetic is what the Kennedy administration faced when it calculated the cost of inaction. A crisis that renews itself every week cannot be waited out, and a movement that can replace every arrested rider has changed its own bargaining power. Connect the number back to the lesson question: this is the pace the students set, a pace set by their willingness to be replaced and to return.",
     kick='F · The ordeal')

# 21 SECTION G DIVIDER
divider_photo('moskowitz-port.jpg', 'Section G', 'The Federal Answer and the Albany Limit',
              ['Ruth Moskowitz, photographed by Jackson, Mississippi', 'police after her arrest, July 21, 1961.'],
              "The photograph is the Jackson, Mississippi police mug shot of Ruth Moskowitz, a Freedom Rider arrested in the summer of 1961, marked public domain on its Wikimedia Commons file page because the copyright was not renewed. Section G holds the lesson's two endings side by side, and students should be told that the pairing is the lesson. In the first ending, the crisis the riders created reached the Interstate Commerce Commission, and the federal government issued the regulations that desegregated interstate terminals across the South, the clearest federal enforcement victory the student movement had yet won. In the second ending, in Albany, Georgia, the movement's methods met Police Chief Laurie Pritchett, who had studied those methods as carefully as any organizer, and the campaign closed without the agreement it had come for. The guided notes summary table calls this row the limit, and the writing task will require students to argue from both endings at once. Teach the ICC order first, in its own words, and Albany second, in its chief's own method.",
              title_size=34)

# 22 ICC
content_text('September 22, 1961: the Commission acts',
             ['Robert Kennedy petitioned the ICC on May 29, 1961.',
              'Regulations were adopted on September 22 and took effect on November 1.',
              'No carrier could seat passengers by race.',
              'Every ticket printed the seating notice.',
              'Segregation signs came down in the terminals.'],
             "Quote the order's operative language, because students meet it at Station 4 of the activity file and should hear it twice. No motor common carrier of passengers, the regulations provide, shall operate a vehicle in interstate commerce on which the seating of passengers is based upon race, color, creed, or national origin. Every ticket had to print the notice that seating aboard vehicles operated in interstate or foreign commerce is without regard to race, color, creed, or national origin, and terminals had to post the regulations and operate without segregation. Compare the machinery with Boynton's. The Court had declared a right that an individual passenger could sue over, one terminal at a time. The Commission's rule bound an entire industry at once, with an agency behind it. That difference, a right declared against a rule enforced, is the distinction this lesson most wants students to carry into Lesson 5 and Lesson 6, where the movement turns from protest to national legislation. The signs students saw in the title photograph began coming down that fall.",
             kick='G · The federal answer', size=23)

# 23 ALBANY
content_text('Albany: the crisis that never came',
             ['SNCC organizers reached Albany in the fall of 1961.',
              'Mass marches filled the jails in December.',
              'Pritchett ordered polite arrests, with no beatings.',
              'Jail space was borrowed from surrounding counties.',
              'In August 1962, King left without an agreement.'],
             "Teach Albany as a contest of methods, not as a failure of courage, because the record forbids the easy reading: more than a thousand Albany demonstrators were arrested, and King himself went to jail there twice. Police Chief Laurie Pritchett had read the movement's accounts of itself and understood its mechanism exactly. Protest worked by creating a crisis, televised violence or overflowing jails, that forced federal intervention or negotiation. Pritchett denied it both halves. His officers made mass arrests politely, in front of cameras, without the brutality that had shamed Birmingham and Montgomery. He borrowed jail space from every surrounding county, so Albany's cells never overflowed and the pressure never peaked. When King chose jail over a fine in July 1962, an unknown person paid the fine and the chief released him, denying the movement even its martyr. King left Albany on August 10, 1962, without a desegregation agreement. The general desegregation of Albany's facilities came only later and piecemeal. The students drew the arithmetic plainly, and Birmingham, in the next lesson, was planned with Albany open on the desk.",
             kick='G · The limit', size=23)

# 24 GLANCE
s = slide(NAVY)
kicker(s, 'The students take the lead at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Four stages, one arithmetic', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The counters', 'Greensboro, February 1960; Nashville, May 1960', 'Beatings, arrests, a bombed home'),
        ('The organization', 'SNCC founded at Shaw, April 1960', 'Subsistence pay and the hardest counties'),
        ('The buses', 'Rides from May 1961; ICC order that fall', 'A burned bus, Parchman, four hundred riders'),
        ('The limit', 'Albany, 1961 to 1962', 'A crisis absorbed quietly moved nothing')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, The Students Take the Lead at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The rows compress the arc. The counters row pairs the Greensboro opening and the Nashville victory with their price, beatings, arrests, and the bombing of the Looby home. The organization row pairs SNCC's founding at Shaw in April 1960 with its working condition, subsistence pay in the hardest counties of the South. The buses row runs from the rides of May 1961 to the ICC regulations of that fall, against a burned bus, Parchman prison, and more than four hundred riders. The limit row is Albany, where a crisis absorbed quietly moved no federal power. Grade the table generously on wording and strictly on pairing: each stage must show what changed and what it cost or risked, and the federal result, including when the honest entry is that there was none.")

# 25 SYNTHESIS
content_text('What the students changed',
             ['A front could open anywhere, in a week.',
              'The tactics were to occupy the space, fill the jail, and ride the bus.',
              'The demands were service now, on equal terms, in person.',
              'Crisis moved federal power, and quiet did not.',
              'A disciplined opponent could absorb protest.'],
             "Draw the lesson together around the question's three verbs, because the exit ticket and the writing task both return to them. Pace: the students made the movement continuous and local, no longer waiting for a national campaign to be announced. Tactics: they occupied the segregated space itself, the stool, the waiting room, the front seat, and accepted jail as an instrument rather than a defeat. Demands: they asked for the concrete thing in front of them, a cup of coffee served, a terminal opened, rather than for statements of principle, and the concreteness is part of why their claims were so hard to answer. Then state the rule the two endings prove together: protest moved the federal government when it created a crisis the government could not ignore, and Albany stands in the record to show the rule from the other side. The movement's leaders, a decade older, learned the arithmetic from the students. Birmingham in the next lesson is where King applied it deliberately, choosing the city, the opponent, and the ground in advance.",
             kick='Synthesis', size=24)

# 26 VOCAB A
vocab('Words for the counters and the organizations',
      [('sit-in', 'seating yourself at a segregated facility and refusing to leave'),
       ('Greensboro sit-in', 'the February 1, 1960 Woolworth protest that sparked the wave'),
       ('SNCC', 'the student organization founded in April 1960'),
       ('CORE', 'the 1942 organization that organized the Freedom Rides')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. The first term is sit-in: a protest in which demonstrators seat themselves at a segregated facility and refuse to leave until they are served on equal terms or arrested. The second is Greensboro sit-in: the protest of February 1, 1960 in which four Black college students sat at a segregated Woolworth lunch counter in Greensboro, North Carolina and refused to leave, sparking sit-ins in cities across the South. The third is Student Nonviolent Coordinating Committee: the organization founded by student activists in April 1960, known as SNCC, which organized sit-ins, Freedom Rides, and voter registration drives in the deepest parts of the South. The fourth is Congress of Racial Equality: the civil rights organization founded in 1942, known as CORE, which pioneered nonviolent direct action and organized the Freedom Rides of 1961. Test the distinction students most often blur: CORE is the older organization, founded in 1942, and SNCC is the students' own, founded in April 1960.")

# 27 VOCAB B
vocab('Words for the buses and the limit',
      [('Freedom Rides', 'the 1961 bus journeys testing interstate desegregation'),
       ('Albany Movement', "the 1961 to 1962 campaign Pritchett's arrests absorbed"),
       ('de jure segregation', 'segregation imposed and enforced by law')],
      "Three more terms, again matching the guided notes exactly. Freedom Rides: the bus journeys of 1961 in which interracial groups of activists rode through the South to test court orders desegregating interstate bus travel and bus terminals. Students should anchor the term to its dates, May to November 1961, and to its legal ground, the Boynton decision of December 1960. The next term is Albany Movement: the campaign of 1961 and 1962 in Albany, Georgia, where a police chief's polite mass arrests denied the movement a televised crisis and taught it the limits of protest that moved no federal power. The chief's name, Laurie Pritchett, belongs with the term in every full answer. The last term is de jure segregation: segregation imposed and enforced by law, as under the southern statutes the courts struck down one by one. Lesson 7 will set its pair beside it, de facto segregation, segregation in fact rather than in law. With these three terms the full set of seven is complete, in the guided notes, in these slides, and in the review materials.")

# 28 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did students a decade younger than the movement\'s leaders change its pace, its tactics, and its demands? Argue it from the record, with dates.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Crisis File: five stations from Greensboro to Albany, and a verdict on where the tactic worked and where it failed'),
        ('Notebook', "Notebook page: the five stages charted by date, crisis created, answer drawn, and federal result"),
        ('Quick check', 'The Counter and the Bus: the Durham photograph, the Greensboro and Nashville sequences, and the ICC and Albany dates'),
        ('Writing', "The Students' Arithmetic: the rule the victories and Albany together prove, argued from the Crisis File records")]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the sit-in defined in one sentence, the ICC dates and the protest that forced them, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Crisis File, runs five stations through the record: the Greensboro sit-in record, the Nashville workshop record, the Freedom Ride record with the Boynton holding, the ICC order record of September 1961, and the Albany record, ending in a verdict on which record shows the tactic working and which shows it failing, and why. The notebook page charts the five stages by date, crisis created, answer drawn, and federal result. The quick check, The Counter and the Bus, tests the Durham waiting room photograph, the Greensboro and Nashville sequences, and the ICC and Albany dates against blueprint entries 7 and 8. The writing task requires Albany argued as evidence and the cleared the way claim answered from the record. The exit ticket has three parts: a sit-in defined in one sentence, the ICC dates and the protest that forced them, and the lesson question in two or three sentences with two facts from the notes.")

dc.save(OUT)
