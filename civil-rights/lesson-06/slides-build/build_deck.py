#!/usr/bin/env python3
"""Civil Rights Lesson 6 deck, "The Laws Change: 1964 and 1965,"
built on the shared deck system: image-led slides, fragments only on screen,
comprehensive speaker notes, full lesson and vocabulary coverage."""
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

# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'THE CIVIL RIGHTS MOVEMENT · LESSON 6', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Laws Change: 1964 and 1965', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'How protest outside the Capitol and mastery inside it produced the two great acts', size=17, color=POWDER)
notes(s, "The photograph shows President Johnson signing the Civil Rights Act in the East Room of the White House on July 2, 1964, photographed by Cecil Stoughton of the White House Press Office, with Martin Luther King Jr. standing behind him. It belongs at the front of the lesson because this hour is about how a movement's demands became federal law. Students will trace two statutes in order: the Civil Rights Act of 1964, forced through a Senate filibuster, and the Voting Rights Act of 1965, carried out of Selma. Between the two signings stand a Mississippi summer, three murders, a refused compromise in Atlantic City, and an attack on a bridge. Keep the mood documentary throughout. The records carry the weight without heightening, and the lesson ends by asking what the two laws could not reach.")

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did the movement turn protest into law, and what could the two great acts actually reach?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the civil rights movement change American law and American life, and what did it leave unfinished?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "The lesson question has two halves, and students should hear both before the first section begins. The first half asks how the movement turned protest into law, which is a question about two kinds of work done at once: pressure built outside the Capitol, in registration lines, convention challenges, and marches, and mastery inside it, a president who knew the Senate and a coalition that could close a filibuster. The second half asks what the two great acts could actually reach, which sets the standard for judgment all hour. Reach will be measured title by title and county by county, and the limits will be named as precisely as the victories. The unit question runs beneath as the frame for all eight lessons, and this lesson is its legislative center.")

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Two summers, two statutes', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The fight in the Senate', 'A stalled bill, a filibuster, a cloture vote'),
        ('B', 'The Civil Rights Act: what it reached', 'Public accommodations, jobs, federal funds'),
        ('C', 'Freedom Summer', 'A thousand volunteers in Mississippi'),
        ('D', 'Atlantic City: the Freedom Democrats', 'Hamer testifies, two seats refused'),
        ('E', 'Selma: the vote denied', 'Half a county, almost no voters'),
        ('F', 'Bloody Sunday and the president answers', 'A bridge on television, a bill in Congress'),
        ('G', 'The Voting Rights Act and the arithmetic', 'Tests suspended, a quarter of a million voters')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Sections A and B cover the first statute: the Senate fight and then the act itself, title by title, with its limits stated in the same breath. Sections C and D cover the Mississippi summer of 1964 and the challenge it carried to Atlantic City. Sections E and F cover Selma, the county that showed why the first act's voting provisions had failed, and the attack and presidential answer of March 1965. Section G gives the second statute and its arithmetic. Tell students the summary table at the end of their guided notes, The Two Laws at a Glance, asks them to rebuild exactly this map.")

# 4 A DIVIDER
divider_text('Section A', 'The Fight in the Senate',
             'A bill sent in 1963, stalled at a president\'s death, and passed whole by his successor.',
             "Set the starting point precisely. President Kennedy sent Congress a civil rights bill in June 1963, after Birmingham, and the bill was still stalled when he was assassinated that November. His successor was the rarest kind of president for a Senate fight: Lyndon Johnson had run the Senate as majority leader, knew its rules, and knew its members. Johnson told Congress that no memorial could honor Kennedy better than passing the bill whole, and he refused to trade away its strength for an easier vote. The House of Representatives passed the bill in February 1964. Everything then depended on the Senate, where a determined minority had killed civil rights bills for decades with a single weapon, extended debate. Section A of the guided notes holds the sequence, so have students keep the dates separate: the bill, the assassination, the House vote, and then the long spring in the Senate.")

# 5 A CONTENT
content_text('Sixty working days',
             ['Kennedy\'s bill stalls, then Johnson stakes his presidency',
              'The House passes the bill, February 1964',
              'Southern senators filibuster for sixty working days',
              'Cloture carries 71 to 29, June 10',
              'Johnson signs the act, July 2, 1964'],
             "Teach the filibuster as a mechanism before teaching it as an episode. A minority that cannot win a vote can still prevent one, by holding the floor and refusing to let debate close. The only answer the Senate's rules supply is cloture, a two-thirds vote to end debate, and on civil rights bills that vote had never been won in this century. Republican votes supplied the margin in 1964, which students should note carefully, because the coalition that passed the act crossed party lines. On June 10 the Senate voted 71 to 29 for cloture. The bill passed the Senate on June 19, and Johnson signed it on July 2. Have the three figures written in section A of the notes in order: sixty working days, 71 to 29, July 2.",
             kick='A · The fight in the Senate')

# 6 A STAT
stat('60', 'working days of filibuster against the civil rights bill',
     'Ended on June 10, 1964, when the Senate voted 71 to 29 for cloture',
     "Let the number stand before explaining it. Sixty working days means the Senate spent more than two months of its working life on a single bill, while the bill's opponents spoke in relays to keep debate alive. The length is itself the evidence of what the act faced: not majority opposition it could outvote, but a procedural wall that required two thirds of the Senate to move. When the cloture vote came, it carried 71 to 29, and the nine votes above the required two thirds came from the cross-party coalition Johnson and the bill's managers had assembled. Ask students what the filibuster's defeat changed beyond this bill. The answer is that a weapon used against civil rights bills for decades had been beaten once, in public, and could be beaten again, which the voting bill's managers remembered the next year.",
     kick='A · The fight in the Senate')

# 7 B DIVIDER
divider_photo('signing-port.jpg', 'Section B', 'The Civil Rights Act: What It Reached',
              ['Johnson signs the act,', 'East Room, July 2, 1964.'],
              "The photograph is a portrait crop of Cecil Stoughton's White House photograph of the signing on July 2, 1964, held by the Johnson Library. Johnson signed with dozens of pens, handing them to the legislators and movement leaders who had carried the bill, and Martin Luther King Jr. stood behind him. Section B now slows down over what the signature actually enacted, because students often treat the act as a general statement against discrimination. It was a set of specific legal tools, title by title, each with a defined field and a defined limit. The guided notes divide the section the same way: the three titles that did the work, and then the edges of the reach. Have students list the titles with their fields in section B before the limits are introduced, so the limits land as qualifications of real powers rather than as a general disappointment.",
              title_size=38)

# 8 B CONTENT
content_text('Three titles, three fields',
             ['Title II: public accommodations opened',
              'Hotels, restaurants, theaters, lunch counters',
              'Title VI: federal funds cut off to segregated programs',
              'Title VII: employment discrimination banned',
              'A commission created to receive job complaints'],
             "Work the titles one at a time, with the field of each stated plainly. Title II barred discrimination in places of public accommodation, the hotels, restaurants, theaters, and lunch counters whose refusal had been the daily texture of segregation for travelers and for local people alike. Title VI put the federal budget behind the Constitution: programs receiving federal money could lose it for discriminating, which gave the government a lever that did not require a lawsuit for every school or hospital. Title VII carried the ban into employment, covering hiring and firing, and the act created a commission to receive job complaints. Students should be able to match each title to its field without notes by the end of this slide, because the quick check and the unit test both ask the match in exactly this form.",
             kick='B · The Civil Rights Act')

# 9 B CONTENT 2
content_text('The edges of the reach',
             ['Genuinely private clubs stand outside Title II',
              'Housing stands outside the act altogether',
              'The jobs commission can investigate, not order',
              'Voting provisions leave registration to lawsuits',
              'County by county was too slow to work'],
             "State the limits with the same precision as the powers, because this section sets up everything that follows in the lesson. A genuinely private club stood outside Title II, a line the act's opponents had demanded and its supporters accepted. Housing, where segregation did its deepest economic work, stood outside the act altogether and waited until 1968. The new employment commission could investigate a complaint and try to settle it, but it could not order an employer to stop, a weakness Congress repaired only years later. Above all for this lesson, the voting provisions were weak: the government could sue a county over registration abuses, one county at a time, while registrars kept failing applicants. Hold that limit in view. Mississippi and Selma are about to demonstrate it.",
             kick='B · The Civil Rights Act', size=24)

# 10 C DIVIDER
divider_text('Section C', 'Freedom Summer',
             'A thousand volunteers join Mississippi\'s registration work, in the summer the act was signed.',
             "The act was signed on July 2, 1964, and in Mississippi that same summer the movement tested what a law on paper could do against a registrar in a courthouse. Freedom Summer brought about a thousand mostly northern student volunteers into the state to register Black voters and run Freedom Schools, joining local organizers who had been doing the work, at far greater risk and with far less attention, for years. Students should hear the structure clearly: the volunteers were new, the work and its dangers were not. Registration meant preparing residents to face tests designed to fail them, in counties where trying to register could cost a job, a home, or a life. Section C is taught plainly and without heightening. Three of the campaign's workers were murdered in its first days, and the lesson states that fact the way the reading states it.")

# 11 C CONTENT
content_text('Registration at its cost',
             ['Volunteers canvass and teach in Freedom Schools',
              'Residents prepare to face the registrar',
              'June 21: Chaney, Goodman, and Schwerner disappear',
              'August 4: their bodies are found',
              'All three had been murdered'],
             "Name the three workers and say what happened in plain words. James Chaney, a Black Mississippian, and Andrew Goodman and Michael Schwerner, white New Yorkers, disappeared on June 21 after investigating a burned church near Philadelphia, Mississippi. Their bodies were found on August 4, buried in an earthen dam. All three had been murdered. The search for them, carried on by federal agents and sailors for six weeks, found the graves of other victims as well, a fact students may raise and should hear answered honestly. Then return to the work itself, because the campaign did not stop: registration canvasses and Freedom Schools continued through the summer. The lesson's point is the contrast the summer exposed. A federal statute now banned discrimination in public accommodations, and in Mississippi the older work of the movement, the voter by voter work, went on at its established price.",
             kick='C · Freedom Summer', size=24)

# 12 C STAT
stat('1,000', 'mostly northern student volunteers joined Mississippi registration work in 1964',
     'Three of the campaign\'s workers were murdered in its first weeks',
     "Let the two facts on this slide stand together, because the campaign's meaning is in the pairing. About a thousand volunteers, most of them students, most of them northern, many of them white, came to Mississippi for one summer to do work that local Black organizers had been doing for years at the same risk. The country watched that summer with an attention it had not given the years before, and students should be asked why: the volunteers carried the nation's own children into the danger, and the murders of Chaney, Goodman, and Schwerner in June made the price undeniable on the national news. The volunteers also built something that outlasted the summer, an organized Mississippi constituency with its own political party, which is where the lesson goes next, to Atlantic City.",
     kick='C · Freedom Summer')

# 13 D DIVIDER
divider_photo('hamer-port.jpg', 'Section D', 'Atlantic City: The Freedom Democrats',
              ['Fannie Lou Hamer at the convention,', 'August 1964.'],
              "The photograph shows Fannie Lou Hamer at the Democratic National Convention in Atlantic City in August 1964, photographed by Warren K. Leffler for U.S. News and World Report and held by the Library of Congress. Hamer had been a sharecropper in Sunflower County, fired and driven from the plantation where she had lived for years after she tried to register to vote. By August 1964 she was the best known voice of the Mississippi Freedom Democratic Party, the integrated party the registration work had built. Section D follows the challenge that party carried to the convention: it asked the Democratic Party to seat its delegates in place of Mississippi's all-white regular delegation. The question underneath the credentials fight was the lesson's question in party form: who speaks for a state whose elections shut out half its people.",
              title_size=36)

# 14 D CONTENT
content_text('Two seats, refused',
             ['The Freedom Democrats hold their own open elections',
              'Hamer testifies before the credentials committee',
              'Her testimony runs on national television',
              'The convention offers two at-large seats',
              'The Freedom Democrats refuse'],
             "Walk the sequence carefully. The Mississippi Freedom Democratic Party had been chosen in its own elections, open to every resident, while the regular Mississippi delegation was chosen in a process that shut Black Mississippians out. Hamer testified before the credentials committee and described, on national television, what registration cost in Mississippi, including the beating she had survived in a jail the year before. The convention, pressed by a president who wanted no public fight, offered a compromise: two at-large seats, chosen by the national party, with the regulars keeping the rest. The Freedom Democrats refused. Their ground was the principle they had come with: a delegation elected with Black voters shut out had no claim to the seats at all. They went home without the victory, and their argument went home with the country.",
             kick='D · Atlantic City', size=24)

# 15 E DIVIDER
divider_text('Section E', 'Selma: The Vote Denied',
             'A county where Black residents were half the population, and almost none could vote.',
             "Section E turns from what the movement built to what the 1964 act had failed to move. The act's voting provisions left registration in the hands of local officials and gave the federal government lawsuits, county by county. Selma, in Dallas County, Alabama, is the case the lesson studies, and its figures should be stated before its story. Black residents made up about half the county's population. Almost none of them were registered to vote. That was not an accident of apathy, and students should be able to describe the machinery that produced it: registrars who opened on few days, asked Black applicants questions no white applicant faced, and failed them for any error. Sheriff Jim Clark enforced the local order around the courthouse. SNCC organizers, and then the Southern Christian Leadership Conference, built a campaign there through the winter of 1965, marching to the courthouse and filling the jails.")

# 16 E CONTENT
content_text('The registrar\'s desk',
             ['Registrars open on few days',
              'Questions no white applicant faces',
              'Any error fails the application',
              'Courthouse marches through the winter of 1965',
              'February 18: Jimmie Lee Jackson is shot in Marion'],
             "End the section with the killing that turned a local campaign into a national question, stated plainly. On February 18, during a night march in nearby Marion, a state trooper shot Jimmie Lee Jackson, a twenty six year old demonstrator who had stepped in front of his mother. Jackson died on February 26. The Selma organizers answered with a plan: a march from Selma to Montgomery, the state capital, to lay the question of the vote before the governor and the nation. Note what the campaign had already established before any march began. The county's rolls were the product of a system, not of a few rude officials, and a system of that kind had survived the 1964 act's voting title intact. That is why the demand that winter was not for another lawsuit. It was for a new federal law with machinery of its own.",
             kick='E · Selma', size=24)

# 17 F DIVIDER
divider_photo('selma-port.jpg', 'Section F', 'Bloody Sunday and the President Answers',
              ['Marchers rest on the road', 'to Montgomery, March 1965.'],
              "The photograph shows marchers resting on a wall during the completed Selma to Montgomery march later in March 1965, photographed by Peter Pettus and held by the Library of Congress; one placard reads that they march together for the dignity and brotherhood of all men. Tell students plainly why this lesson shows the completed march and not the attack of March 7: the famous Bloody Sunday photographs are copyrighted press photographs, and this unit does not use them. The attack is taught from the record in words, which are exact enough. On March 7, about six hundred marchers crossed the Edmund Pettus Bridge out of Selma. Troopers ordered them back, gave them a moment, and charged. Section F covers the attack, its broadcast, and the president's answer eight days later, in that order, because the order is the argument.",
              title_size=34)

# 18 F CONTENT
content_text('March 7, 1965',
             ['About six hundred marchers cross the bridge',
              'Troopers order them back, then charge',
              'Clubs and tear gas drive the march back into Selma',
              'John Lewis suffers a fractured skull',
              'The film runs on national television that evening'],
             "State the attack plainly and completely, the way the reading states it. The marchers were unarmed and marching two by two. The troopers and Sheriff Clark's posse met them at the foot of the bridge, ordered them to disperse, and charged within about a minute, beating marchers with clubs, firing tear gas, and driving the column back across the bridge into Selma. John Lewis, the SNCC chairman marching in the front line, suffered a fractured skull. Then give the second fact its full weight: the attack was filmed, and the film ran on national television that evening, interrupting a major network broadcast, so that the country saw, in its own homes, what a registration system defended itself with. The movement had argued for years that the registrar's desk rested on violence. On March 7 the violence was televised.",
             kick='F · Bloody Sunday', size=24)

# 19 F CONTENT 2
content_text('We shall overcome',
             ['March 15: Johnson addresses Congress',
              '\'Their cause must be our cause too\'',
              'He closes with the movement\'s own words',
              'A federal court clears the march to Montgomery',
              'March 25: about 25,000 reach the capital'],
             "Eight days after Bloody Sunday, President Johnson addressed a joint session of Congress and asked for a voting bill, and he framed the cause in the movement's own language: their cause must be our cause too, and we shall overcome. Students should register what that borrowing meant. A president of the United States, a southerner, took the movement's anthem as the closing of a legislative address, because Selma had made the question a national one and he chose to answer it at full strength rather than bargain it down. The practical sequence followed at once: a federal court cleared the Selma to Montgomery march, federal troops guarded the route, and about twenty five thousand people reached the capital on March 25. The bill then moved through Congress in the spring and summer, with the Selma film behind it.",
             kick='F · Bloody Sunday and the answer', size=24)

# 20 G DIVIDER
divider_photo('vra-port.jpg', 'Section G', 'The Voting Rights Act and the Arithmetic',
              ['Johnson signs the act at the Capitol,', 'August 6, 1965.'],
              "The photograph is a portrait crop of Yoichi Okamoto's photograph of President Johnson signing the Voting Rights Act at the Capitol on August 6, 1965, held by the Johnson Library, with Martin Luther King Jr. and other leaders looking on. Section G studies the act as machinery, because machinery is what separates it from everything the movement had won before. The 1964 act had stated rights and left their enforcement to lawsuits. The 1965 act, in the places where disfranchisement was systematic, removed the registrar's discretion in advance: tests suspended by the statute itself, federal examiners empowered to register voters directly, and a duty on covered states to clear any change in voting rules with Washington before the change could take effect. Have students hold those three tools separate in section G of the notes. The arithmetic that closes the lesson is unintelligible without them.",
              title_size=34)

# 21 G CONTENT
content_text('Machinery, not only rights',
             ['Section 2: no rule may deny the vote by race',
              'Coverage: a test in 1964, under half registered or voting',
              'Tests and devices suspended at once in covered places',
              'Federal examiners register voters directly',
              'Voting changes cleared with Washington first'],
             "Work the machinery in the act's own order. Section 2 states the standing ban, nationwide: no voting qualification, standard, practice, or procedure may be imposed to deny or abridge the right to vote on account of race or color. The coverage formula then identifies where stronger medicine applies, places that had kept a test or device on November 1, 1964 and where fewer than half of voting age residents had been registered or had voted. In those places the tests, literacy tests above all, were suspended by the act itself, without a lawsuit for each county. Federal examiners could register voters over the local registrar's refusal. And preclearance reversed the old sequence: instead of a discriminatory rule operating until a court struck it down years later, a covered state had to clear its change with Washington first.",
             kick='G · The Voting Rights Act', size=24)

# 22 G STAT
stat('250,000', 'new Black voters registered by the end of 1965',
     'Mississippi moved from under 7 percent Black registration in 1964 to about 60 percent within three years',
     "Read the two figures as a pair, the way the guided notes require. About a quarter of a million new Black voters were registered by the end of 1965, within five months of the signing. Mississippi, the state of Freedom Summer and the Atlantic City challenge, where under seven percent of Black voting age residents had been registered in 1964, reached about sixty percent within three years. Ask students to explain the speed with the machinery from the previous slide rather than with goodwill: the tests were already suspended, the examiners were already empowered, and a registrar who invented a new barrier found that the new rule itself needed clearance from Washington. The figures are the lesson's verdict on the difference between a right announced and a right administered. Keep both figures in section G, because the quick check asks for the Mississippi pair by name.",
     kick='G · The Voting Rights Act')

# 23 GLANCE
s = slide(NAVY)
kicker(s, 'The two laws at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Each step, and what it added', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The Senate fight', 'Cloture after sixty working days', 'A statute where three presidents had failed to get one'),
        ('The 1964 act', 'Accommodations, jobs, federal funds', 'Housing, clubs, and registration left outside'),
        ('Mississippi and Selma', 'Pressure the government could not ignore', 'Three workers murdered; a march beaten on a bridge'),
        ('The 1965 act', 'Tests suspended, examiners, preclearance', 'A quarter of a million new voters by year\'s end')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the summary table at the end of the guided notes, The Two Laws at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. Read the rows as a single account rather than four summaries. The Senate fight supplied the first statute. The 1964 act supplied rights in public life and employment, and a map of its own limits. Mississippi and Selma supplied the evidence and the pressure, at a price the table names without decoration. The 1965 act supplied machinery aimed at the exact failure Selma had exposed. Grade the table generously on wording and strictly on completeness: every row needs its power, its holder, and its limit or its proof.")

# 24 VOCAB A
vocab('Words for the two statutes',
      [('Civil Rights Act of 1964', 'the act that opened public life and employment'),
       ('filibuster', 'extended debate used to block a vote'),
       ('Title VII', 'the act\'s ban on employment discrimination'),
       ('Freedom Summer', 'Mississippi registration work, summer 1964')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. Civil Rights Act of 1964: the federal law that banned discrimination in public accommodations and employment and allowed the government to cut off funds to segregated programs, the movement's first great legislative victory. filibuster: the Senate practice of extending debate to block a bill from coming to a vote, broken on the civil rights bill of 1964 when the Senate voted for cloture after more than two months of debate. Title VII: the section of the Civil Rights Act of 1964 that banned discrimination in employment on the basis of race, color, religion, sex, or national origin. Freedom Summer: the campaign of 1964 that brought about a thousand mostly northern student volunteers to Mississippi to register Black voters and run Freedom Schools.")

# 25 VOCAB B
vocab('Words for the challenge and the vote',
      [('Mississippi Freedom Democratic Party', 'the integrated party that challenged Atlantic City'),
       ('Bloody Sunday', 'the attack at the bridge, March 7, 1965'),
       ('Voting Rights Act of 1965', 'tests suspended, examiners, preclearance')],
      "Three more terms, again matching the guided notes exactly. Mississippi Freedom Democratic Party: the integrated political party organized in Mississippi in 1964 that challenged the seating of the state's all-white regular delegation at the Democratic National Convention in Atlantic City. Bloody Sunday: the attack of March 7, 1965 by Alabama state troopers and a sheriff's posse on voting rights marchers at the Edmund Pettus Bridge in Selma, televised to the nation that evening. Voting Rights Act of 1965: the federal law that suspended literacy tests, sent federal examiners to register voters in covered states, and required those states to clear any change in voting rules with the federal government first. Note the order of this set. The first term names the constituency the registration work built, the second names the attack that moved the presidency, and the third names the machinery the movement's decade of work finally obtained.")

# 26 SYNTHESIS
content_text('Judging the reach of the law',
             ['The making: pressure outside, mastery inside',
              'The reach: public life, the job, the ballot',
              'The limits: housing, wealth, equality as a result',
              'The writing task asks for a weighing, not a narration'],
             "Close the teaching here, before the work slide, and model the judgment the writing task will ask for. The movement turned protest into law by working both sides of the Capitol wall at once, and the proof is in the pair of years: a filibuster broken in June 1964 and a bridge in March 1965 each produced a statute within months. Against that achievement, state the limits with equal clarity, because Johnson stated them himself at Howard University in June 1965, before the second act was even signed: freedom is not enough, and equality as a right is not yet equality as a result. The strongest student writing will hold both halves in one argument, measuring the quarter of a million new voters against the housing and wealth the acts never touched, and will say which measurement should govern the verdict and why.",
             kick='Synthesis')

# 27 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did the movement turn protest into law, and what could the two great acts actually reach? Build the file first, then judge from it.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Statute File: five records, a file, and a verdict on the provision that did the most work'),
        ('Notebook', 'Notebook page: the five steps charted, and the two laws in one paragraph'),
        ('Quick check', 'The Marchers on Highway 80: the photograph, the filibuster, the titles, the arithmetic'),
        ('Writing', 'What Could the Two Great Acts Actually Reach? The sequence weighed against the Howard standard')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the cloture vote and its first, the registration arithmetic in full, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Statute File, runs five stations through the records: Title II and Title VII quoted from the audited bank records of the 1964 act, Johnson's Selma address and Howard University address quoted from the bank records of his speeches, and the Voting Rights Act quoted from its bank record, each station asking for the power created, its holder, and its limit. Students build the file in Part 2 and defend a verdict on the single provision that did the most work in the decade after. The notebook page charts the same five steps. The quick check, The Marchers on Highway 80, works from Peter Pettus's photograph of the completed march. The writing task turns the lesson question into an essay weighed from both halves of the bank. The exit ticket has three parts: the cloture vote and why it was a first, the registration arithmetic in full, and the lesson question answered with one reach fact and one limit fact.")

dc.save(OUT)
