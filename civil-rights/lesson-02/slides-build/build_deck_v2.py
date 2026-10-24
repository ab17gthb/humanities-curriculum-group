#!/usr/bin/env python3
"""Civil Rights Lesson 2 deck, "Brown and the Massive Resistance,"
built to the approved system: image-led slides, fragments only on
screen, comprehensive speaker notes, full lesson + vocabulary
coverage. Fonts: Georgia titles, Lato body."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags, photo_right,
                         divider_photo, content_photo, content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED, W, H)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

dc.IMG = os.path.join(HERE, 'img')
OUT = os.path.join(HERE, '..', 'lesson-02-slides.pptx')

spec = open(os.path.join(HERE, '..', '..', 'build-scripts', 'unit-spec.md')).read()
l2 = spec.split('### Lesson 2')[1].split('### Lesson 3')[0]
DEFS = {}
for line in l2.splitlines():
    m = re.match(r'- (.+?): (.*)$', line.strip())
    if m: DEFS[m.group(1)] = m.group(2)
assert len(DEFS) == 7

def joined(term):
    return f"{term}: {DEFS[term]}"

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

LQ = 'How did the NAACP turn a Kansas school case into the end of legal segregation, and how did the South answer?'
UQ = 'How did the civil rights movement change American law and American life, and what did it leave unfinished?'

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'THE CIVIL RIGHTS MOVEMENT · LESSON 2', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Brown and the Massive Resistance', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'A unanimous Court ends legal segregation, and the South organizes its answer', size=17, color=POWDER)
notes(s, "The photograph shows the Supreme Court as it stood in October 1953, the Warren Court of 1953 to 1954, in the official photograph of the Court held by the United States Government. Nine men in this photograph would decide, within eight months, the most consequential education case in American history, and they would decide it together, without a single dissent. Open by placing this lesson after the last one. Lesson 1 built the ground: Jim Crow law, the institutions Black Americans built inside it, and the NAACP, which had been fighting segregation in the courts for decades before the movement's famous decade began. This lesson follows that institution's longest campaign to its victory, and then follows the victory into the decade of resistance that answered it. Students should leave able to hold both halves at once: a legal triumph that was complete on paper, and a schoolhouse reality that barely moved for ten years.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[(LQ, {})]], size=40, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                (UQ, {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question joins a victory to its answer, and students will need both halves for the exit ticket and the writing task. The first half asks how the NAACP turned a Kansas school case into the end of legal segregation. The answer runs through a strategy planned in the 1930s, two graduate school victories in 1950, five cases joined under one name, and a unanimous ruling on May 17, 1954. The second half asks how the South answered. That answer runs through a second decision that set no date, a congressional manifesto signed by 101 members, state laws built to delay and evade, and a Virginia county that closed its public schools for five years. Warn students now against treating the 1954 ruling as the end of the story. The ruling ended a doctrine. Ending the practice took another decade of conflict, and this lesson covers the law and the resistance in the same hour.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'The case, the delay, and the answer', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The Strategy', 'Attack where inequality showed, graduate schools first'),
        ('B', 'Five Cases Become One', 'Kansas, South Carolina, Virginia, Delaware, Washington'),
        ('C', 'May 17, 1954', 'Separate educational facilities are inherently unequal'),
        ('D', 'Brown II', 'All deliberate speed, and no date in it'),
        ('E', 'Massive Resistance Organizes', 'Byrd, the Manifesto, and the closing laws'),
        ('F', 'Closing the Schools', 'Prince Edward County, closed for five years'),
        ('G', 'Cooper v. Aaron, and the Gap', 'The law settled, the schools barely moved')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A covers Charles Hamilton Houston's strategy and the graduate school cases of 1950. Section B covers the five cases joined under Brown and the question posed at reargument. Section C covers the decision of May 17, 1954. Section D covers Brown II and the timetable it set. Section E covers massive resistance and the Southern Manifesto. Section F covers Prince Edward County and the school closings. Section G covers Cooper v. Aaron and the gap between settled law and actual schools ten years later. The summary table at the end of the guided notes is titled The Case and the Answer at a Glance, and students will complete it from these seven sections.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', 'The Strategy',
             'A campaign planned in the 1930s, aimed first where inequality was easiest to prove.',
             "Set up the strategy as a piece of planning, because students often imagine the Brown case as a single lawsuit that rose on its own. It was the last step of a campaign built over twenty years. Charles Hamilton Houston, dean of Howard Law School and then the NAACP's chief lawyer, trained a generation of Black lawyers and designed the sequence this lesson follows: begin where the inequality was most visible and most expensive for states to defend, win precedents there, and move step by step toward the schools attended by the youngest children. Houston died in 1950, the year his graduate school cases reached the Supreme Court, so the students he trained, led by Thurgood Marshall, carried the campaign he had drawn. Keep the word strategy in front of the class. Every later section is this plan working, and the test will ask students to describe the plan before they describe the case.")

# ------------------------------------------------------ 5 STRATEGY
content_text('Attack where inequality showed',
             ['Houston built the NAACP legal program in the 1930s.',
              'States were ordered to make separate schools truly equal.',
              'The campaign began with graduate and professional schools.',
              'Precedent came first, and elementary schools came last.'],
             "Teach the logic of the sequence in Houston's own terms. Southern states spent far more on white schools than on Black schools at every level, and the gap was widest and hardest to defend in graduate education, where several states provided Black students no law school or medical school at all. A court order requiring truly equal separate provision would force a state to build a second full university system or admit the Black applicant to the existing one. Either outcome cost the state money or broke segregation at its smallest and least visible point, before judges sympathetic to the argument because they were themselves products of professional schools. Houston also understood the audience. Graduate cases involved adult plaintiffs, small numbers, and institutions far from the emotional center of the school question. The elementary schools, where millions of children attended under law, came last, after the precedents existed.",
             kick='A · The Strategy', size=24)

# ------------------------------------------------------ 6 MARSHALL / 1950 CASES
content_photo_s('marshall-port.jpg', '1950: the graduate school victories',
              ['Sweatt v. Painter held that a makeshift law school cannot equal the university.',
               'McLaurin v. Oklahoma held that admission means equal treatment inside.',
               'Both cases were argued by Thurgood Marshall.',
               'The method was proven, and the precedent was set.'],
              "The photograph shows Thurgood Marshall in his judicial robes in 1976, from the official portraits of the Supreme Court held by the Library of Congress. In 1950 Marshall was the NAACP's chief counsel, Houston's former student, arguing the cases his teacher had designed. In Sweatt v. Painter, Texas had created a separate law school for Heman Sweatt in haste rather than admit him to the University of Texas, and the Supreme Court held that the new school could not equal the established one in faculty, standing, or the qualities that make a law school strong. In McLaurin v. Oklahoma, George McLaurin had been admitted to a doctoral program but was seated apart in the classroom, the library, and the cafeteria, and the Court ordered that he be treated like every other student. Together the cases taught that equality could not be supplied by a building thrown up for the purpose, and that admission with internal segregation was not equality either. The elementary schools were next.",
              kick='A · The Strategy')

# ------------------------------------------------- 7 SECTION B DIVIDER
divider_text('Section B', 'Five Cases Become One',
             'Five districts, one name, and a question the Court insisted on asking twice.',
             "This section covers how the case was assembled, and the assembly is itself a teaching point. The NAACP did not bring one family's complaint and hope for a national ruling. It brought cases from four states, Kansas, South Carolina, Virginia, and Delaware, joined with a companion case from the District of Columbia decided the same day, so that the Court would confront school segregation as a national system rather than a local dispute. The Kansas case gave the group its name because it was listed first. Oliver Brown was a Topeka parent, a welder and assistant pastor, whose daughter Linda was assigned to a Black school across town although a white school stood blocks from the family home. Note for students that the Virginia case in the group, Davis, began with a student strike at Moton High School in Prince Edward County in 1951. That county returns in section F, at the far end of the resistance.")

# ------------------------------------------------------ 8 FIVE CASES
content_text('Reargument: does separation itself harm?',
             ['The cases were argued in December 1952 and reargued in December 1953.',
              'The Court asked whether segregation itself does constitutional harm.',
              'The NAACP answered yes, with evidence on children.',
              'The boards answered that Plessy settled the question in 1896.'],
             "The first argument, in December 1952, left the Court divided, and the justices took an unusual step: they set the cases for reargument and posed written questions, the sharpest of which asked whether segregation itself, even where buildings and budgets were equal, deprived Black children of equal educational opportunity. That question is the hinge of the whole case, and students should be able to state it in their own words. Marshall's team answered yes, presenting testimony and research on what state enforced separation taught Black children about their standing in the community. The school boards answered that Plessy v. Ferguson, decided in 1896, had upheld segregation for two generations and that the Fourteenth Amendment had never been understood to forbid separate schools. Between the two arguments Chief Justice Fred Vinson died, and Earl Warren, the former governor of California, took the center chair. Section C takes up what Warren did with a divided Court.",
             kick='B · Five Cases Become One', size=24)

# ------------------------------------------------- 9 SECTION C DIVIDER
divider_photo('warrencourt-port.jpg', 'Section C', 'May 17, 1954',
              ['The Warren Court, in its official', 'photograph of October 1953.'],
              "The photograph is the official portrait of the Court as it stood in October 1953, held by the United States Government, the same Court that decided Brown the following May. Earl Warren understood that a divided ruling on school segregation would hand the South a reason to treat the decision as one faction's opinion, so he worked through the winter and spring of 1954 to bring all nine justices to a single, short, unanimous opinion, written in language a newspaper reader could follow. He assigned the opinion to himself and traded drafts until the last holdouts signed. Teach the unanimity as a deliberate achievement, not a natural outcome: at the first conference after argument, the Court had been split, with several justices prepared to uphold Plessy. What unanimity bought, and what it may have cost in the enforcement decision that followed, is the judgment students will make in the activity and the writing task.",
              title_size=40)

# ------------------------------------------------------ 10 DECISION
content_text('Separate is inherently unequal',
             ['Warren read a unanimous opinion.',
              'Separation generates a feeling of inferiority.',
              'The harm does not depend on equal buildings.',
              'Separate educational facilities are inherently unequal.',
              'The Fourteenth Amendment carries the holding.'],
             "Read the holding slowly, in the opinion's own sequence, because the activity puts this text in front of students verbatim. The Court first established that public education had become a central function of government and that, where a state provided it, the opportunity had to be available to all on equal terms. It then answered the reargument question: to separate children from others of similar age and qualifications solely because of their race generates a feeling of inferiority as to their status in the community that may affect their hearts and minds in a way unlikely ever to be undone. Because the harm lay in the separation itself, equalizing buildings or budgets could not cure it. The conclusion followed in one sentence: separate educational facilities are inherently unequal. Segregation in public schools therefore denied Black children the equal protection of the laws guaranteed by the Fourteenth Amendment, and the separate but equal doctrine had no place in public education.",
             kick='C · May 17, 1954', size=24)

# ------------------------------------------------------ 11 STAT 9-0
stat('9 to 0', 'a unanimous Court on May 17, 1954',
     'One opinion, no dissents, no concurrences · Every justice signed the result · Plessy displaced in public education after 58 years',
     "Give students the weight of the unanimous vote. School segregation had stood under Plessy's protection for fifty eight years, and the Court that ended it spoke in a single opinion with no dissenting or concurring opinions to qualify it. Warren's opinion was deliberately short, about eleven pages, nontechnical, and addressed to the country as much as to lawyers. Southern newspapers printed it in full the next day, and southern officials understood at once both its clarity on the principle and its silence on enforcement, because the opinion decided constitutionality only and restored the cases for a further argument on relief. That silence is the bridge to section D. Students sometimes read unanimity as strength in every direction. Teach it precisely: unanimity made the holding hard to dismiss as partisan, and it was purchased in part by postponing every hard question about timetables, districts, and remedies to a second case the following year.",
     kick='C · May 17, 1954')
print('part 1 slides done')
# ------------------------------------------------- 12 SECTION D DIVIDER
divider_text('Section D', 'Brown II: All Deliberate Speed',
             'A second decision, a year later, that set the work in motion and set no date for finishing it.',
             "Brown II is the most argued over paragraph in this lesson, and students should understand why it exists before they judge its language. The 1954 opinion decided that segregation was unconstitutional and nothing else. The cases came from districts with different school systems, transportation maps, and local laws, and the Court heard a full second round of argument, in the spring of 1955, on relief alone. The NAACP asked for desegregation by the following autumn. Several southern states asked for gradual, open ended compliance supervised locally. What the Court produced on May 31, 1955 tried to hold both the principle and the machinery: local district courts would supervise, school boards bore the burden of proof, and the work was to begin promptly. Its closing phrase, however, is the part history kept, and section D's single content slide reads the decision in full so students can weigh its strict sentences against its famous last words.")

# ------------------------------------------------------ 13 BROWN II
content_photo_s('judgment-port.jpg', 'A prompt start, and no deadline',
              ['Brown II was decided on May 31, 1955.',
               'District courts took charge, district by district.',
               'Boards had to make a prompt and reasonable start.',
               'The burden of proving delay sat on the boards.',
               'Admission was ordered with all deliberate speed.'],
              "The image shows the judgment and decree issued in Brown on May 31, 1955, the implementation decree held by the National Archives. Teach the decision as two texts in one. The strict text requires defendants to make a prompt and reasonable start toward full compliance, permits additional time only where the defendants themselves prove it necessary in the public interest and consistent with good faith compliance at the earliest practicable date, and instructs the district courts to retain jurisdiction. The loose text is the closing order, directing that the plaintiffs be admitted to public schools on a racially nondiscriminatory basis with all deliberate speed. Deliberate in ordinary use can mean slow and careful, and the phrase contains no date, no percentage, and no penalty. Southern officials quoted the closing phrase and ignored the burden language, and district courts across the South, staffed by local judges, largely let them. The delay that followed was therefore not only disobedience. Part of it was written into the order itself.",
              kick='D · Brown II')

# ------------------------------------------------- 14 SECTION E DIVIDER
divider_text('Section E', 'Massive Resistance Organizes',
             'Virginia gives the answer its name, and Congress gives it 101 signatures.',
             "The resistance that followed Brown was organized, legalistic, and proud of both qualities, and students should meet it as a program rather than as a mood. Its architects were not street crowds. They were governors, legislators, a United States senator who ran a state political machine, and members of Congress. Their method was to use the forms of law, statutes, placement boards, funding rules, and constitutional declarations, to make the Brown holding as difficult and slow to exercise as possible, while professing fidelity to the Constitution as they read it. Senator Harry Byrd of Virginia supplied the program's name in 1956: massive resistance. Within two years of Brown II, southern states had passed hundreds of measures in its spirit. This section covers the program's tools and its congressional statement, the Southern Manifesto, which students will read verbatim in the activity alongside the two court decisions it answered.")

# ------------------------------------------------------ 15 RESISTANCE TOOLS
content_text('The tools of delay',
             ['Closing laws shut any school ordered to integrate.',
              'Pupil placement assigned each child individually, with race unnamed.',
              'Tuition grants paid public money toward private fees.',
              'Interposition declared the ruling void in the state.'],
             "Walk the four tools in order and name what each one does to a Black family's practical position. Closing laws, adopted first in Virginia in 1956, required the governor to shut any public school ordered to desegregate and cut its state funds, converting a court order against one district into a threat against every district. Pupil placement laws created boards that assigned each child individually under criteria such as home environment, aptitude, and the possibility of friction, written to produce segregated results without using the word race, and nearly impossible to challenge one child at a time. Tuition grants paid public money toward fees at private schools, which sprang up across the South as segregation academies. Interposition resolutions declared Brown void within the state, a constitutional theory with no support in the courts that nonetheless gave local officials a document to cite. The shared design is delay through procedure: every tool forced the NAACP back into court, district by district and child by child.",
             kick='E · Massive Resistance Organizes', size=24)

# ------------------------------------------------------ 16 STAT 101
stat('101', 'signers of the Southern Manifesto, 1956',
     'Nineteen senators and eighty two representatives · Brown named a clear abuse of judicial power · Resistance pledged by all lawful means',
     "The Southern Manifesto, formally the Declaration of Constitutional Principles, was read into the Congressional Record in March 1956 and signed by 101 southern members of Congress: nineteen of the South's twenty two senators and eighty two of its representatives. Its text, which students read in the activity, calls the school decisions a clear abuse of judicial power, charges the Court with encroaching on rights reserved to the states and the people, commends the states that had declared their intention to resist forced integration by any lawful means, and pledges the signers to use all lawful means to bring about a reversal of the decision. Teach the word lawful as the document's hinge. It let members of Congress lead a resistance while professing constitutional fidelity, and it set the program's public limit at the same time. The two southern senators who refused to sign, Lyndon Johnson of Texas and Estes Kefauver of Tennessee, are worth naming: the document's near unanimity was a choice, not a condition of southern politics.",
     kick='E · Massive Resistance Organizes')

# ------------------------------------------------- 17 SECTION F DIVIDER
divider_text('Section F', 'Closing the Schools',
             'In Prince Edward County, resistance reached its limit: no public schools at all.',
             "Prince Edward County, Virginia is where this lesson's beginning and its resistance meet, and students should feel that connection before the facts. The county's Davis case, one of the five joined in Brown, began in April 1951 when Barbara Johns, a sixteen year old student at Moton High School, led a strike against the school's tarpaper shack classrooms and the NAACP agreed to sue, on condition that the suit attack segregation itself rather than ask for a better separate school. Eight years later the same county became the fullest test of what massive resistance would do when every delaying tool had been used and a court order still stood. Rather than admit Black and white children to the same schools, the county ended public education altogether. This section states what that meant, in years and in children, and how it finally ended in a second Supreme Court decision in 1964.")

# ------------------------------------------------------ 18 PRINCE EDWARD
content_text('Prince Edward County, 1959 to 1964',
             ['The board of supervisors refused to levy school taxes.',
              'Public schools did not open in the fall of 1959.',
              'A private academy served white children.',
              'About 1,700 Black children had no school in the county.',
              'Griffin ordered the schools reopened in 1964.'],
             "State the mechanism precisely, because it shows the resistance working through ordinary government powers. A federal court ordered the county to admit students without regard to race for the term beginning in September 1959. The county school board lacked the power to raise its own money. The board of supervisors, which levied taxes, refused to appropriate any funds for public schools, and without money the schools could not open. A private foundation opened Prince Edward Academy for white children that fall, supported at first by state tuition grants and county tax credits. No school was provided for Black children in the county. Some families sent children to live with relatives in other counties or states, churches and volunteers ran improvised classes, and many children received no formal education for years. Classes in county buildings began in 1963, and in Griffin v. County School Board of Prince Edward County in 1964 the Supreme Court ordered the supervisors to levy taxes and reopen public schools on the same terms as other Virginia counties.",
             kick='F · Closing the Schools', size=24)

# ------------------------------------------------------ 19 STAT 5 YEARS
stat('5 years', 'Prince Edward County without public schools',
     'Fall 1959 to fall 1964 · One Virginia county · About 1,700 Black children shut out of schooling',
     "Hold this figure up against the language of law that surrounds the lesson. Five school years is the whole of a child's passage from first grade to sixth, or from seventh grade to graduation. The children who lost those years in Prince Edward County were not parties to a new lawsuit by choice: their parents' case, Davis, had been won in 1954, when many of them were small children, and the county answered the victory by abolishing the institution the case was about. About 1,700 Black children were shut out of formal schooling in the county during the closing, a figure carried in the Griffin record and the standard accounts, while the white academy enrolled the county's white children with public support. When teachers discuss what a court order can and cannot do, this is the concrete case: the order of 1959 was clear, the Constitution had been settled in the county's own case, and the schools stayed closed for five years anyway, until a new order reached the county's tax levy itself.",
     kick='F · Closing the Schools')

# ------------------------------------------------- 20 SECTION G DIVIDER
divider_text('Section G', 'Cooper v. Aaron, and the Gap',
             'The Court closes every legal exit, and the lesson closes on what the law had not moved.',
             "The final section joins a legal settlement to a statistical verdict. Cooper v. Aaron grew out of Little Rock, which the next lesson studies in full: Arkansas's governor and legislature claimed that state officials were not bound by the Supreme Court's interpretation of the Constitution in Brown, and that the decision was not the law for Arkansas until Arkansas accepted it. The claim was the constitutional theory underneath all of massive resistance, stated in its purest form by a governor. The Court's answer in 1958 closed the theory completely, in an opinion every justice signed individually. Section G then sets that complete legal victory beside the enrollment figures of 1964, ten years after Brown, because the distance between the two is the lesson's last idea and the unit's recurring question in miniature: what a court can settle, and what settling the law leaves still to be done by other means.")

# ------------------------------------------------------ 21 COOPER
content_text('No official may nullify Brown',
             ['Little Rock asked whether a state was bound by Brown.',
              'Article VI makes the Constitution the supreme law of the land.',
              'Marbury, in 1803, held that the courts say what the law is.',
              'Brown is binding on every state official, by oath.',
              'Brown could be nullified neither openly nor indirectly.'],
             "Teach Cooper as a chain of three links, the way the activity asks students to trace it. The first link is Article VI: the Constitution is the supreme Law of the Land, and state officers swear an oath to support it. The second link is Marbury v. Madison of 1803, in which Chief Justice Marshall declared that it is emphatically the province and duty of the judicial department to say what the law is, a principle the Cooper opinion calls a permanent and indispensable feature of the constitutional system. The third link is the conclusion: the interpretation of the Fourteenth Amendment given in Brown is therefore itself the supreme law of the land, binding on Arkansas officials notwithstanding any state law or constitution. The opinion, signed individually by all nine justices, closed the case with a sentence students should copy: the rights declared in Brown can be nullified neither openly and directly by state officers, nor indirectly through evasive schemes for segregation, whether attempted ingeniously or ingenuously.",
             kick='G · Cooper v. Aaron, and the Gap', size=24)

# ------------------------------------------------------ 22 STAT 1 IN 100
stat('1 in 100', 'Black children in the Deep South in school with white children, 1964',
     'Ten years after Brown · The law settled since 1958 · The schools, in most of the South, still separate in fact',
     "End the content of the lesson on this figure and let it stand without softening. In the autumn of 1964, ten years after a unanimous Court held separate schools inherently unequal, and six years after Cooper closed every legal theory of resistance, barely one Black child in a hundred across the states of the Deep South attended school with white children. The figure is the lesson's verdict on the difference between declaring a right and delivering it. The courts had supplied the declaration, twice, in the strongest available language. What the declaration lacked was an enforcement instrument equal to the resistance: no deadline in 1955, district judges drawn from the communities resisting, and families forced to sue school by school and child by child. The movement's answer to that gap, mass protest that created pressure no court timetable had produced, begins with the next lesson, in Montgomery and at Little Rock itself.",
     kick='G · Cooper v. Aaron, and the Gap')

# ------------------------------------------------------ 23 GLANCE
s = slide(NAVY)
kicker(s, 'The case and the answer at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Claimed, delayed, resisted, answered', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The strategy', 'Houston, then Marshall; graduate schools in 1950', 'Precedent built before the main case'),
        ('The decision', 'May 17, 1954: separate is inherently unequal', 'Legal segregation ended on paper'),
        ('The delay and resistance', 'Brown II, the Manifesto, the closings', 'A decade organized against the ruling'),
        ('The reply and the gap', 'Cooper in 1958; one in a hundred by 1964', 'Law settled, schools barely moved')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, The Case and the Answer at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The four rows are the lesson's argument in order. The strategy covers Houston's plan and the graduate school victories of Sweatt and McLaurin in 1950. The decision covers the five joined cases, the reargument question, and the unanimous holding of May 17, 1954. The delay and resistance covers Brown II's open timetable in 1955, massive resistance and the Southern Manifesto of 1956, and the Prince Edward County closings of 1959 to 1964. The reply and the gap covers Cooper v. Aaron in 1958 and the enrollment figure of 1964. Grade the table generously on wording and strictly on the sorting: an entry that calls Brown a complete victory has missed the second half of the lesson, and an entry that calls it a failure has missed that legal segregation never recovered its constitutional standing.")
print('part 2 slides done')
# ------------------------------------------------------ 24 VOCAB A
vocab('Words for the old order and its end',
      [('Plessy v. Ferguson', 'the 1896 decision that upheld separate but equal'),
       ('separate but equal', 'segregation allowed if facilities were equal'),
       ('Brown v. Board of Education', 'the 1954 ruling: separate schools are inherently unequal'),
       ('Brown II', 'the 1955 order: proceed with all deliberate speed')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. " + joined('Plessy v. Ferguson') + ". " + joined('separate but equal') + ". " + joined('Brown v. Board of Education') + ". " + joined('Brown II') + ". Teach the four as two pairs. Plessy and its doctrine supplied the legal shelter for school segregation from 1896 to 1954. Brown removed the shelter in public education, and Brown II then determined, in practice, how fast the removal would reach actual classrooms.")

# ------------------------------------------------------ 25 VOCAB B
vocab('Words for the answer',
      [('massive resistance', 'the southern campaign to prevent desegregation'),
       ('Southern Manifesto', 'the 1956 declaration signed by 101 members of Congress'),
       ('Cooper v. Aaron', 'the 1958 ruling: state officials are bound by Brown')],
      "Three more terms, again matching the guided notes exactly. " + joined('massive resistance') + ". " + joined('Southern Manifesto') + ". " + joined('Cooper v. Aaron') + ". Keep the sequence in view for review: the resistance organized first under Byrd's name and the Manifesto's signatures, and Cooper answered it last, in 1958, by holding that the Court's reading of the Constitution binds state officials and cannot be nullified.")

# ------------------------------------------------------ 26 SYNTHESIS
s = slide(NAVY)
kicker(s, 'The lesson in one view')
text(s, 0.9, 1.28, 11.5, 1.0, 'A right declared, a decade taken', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Declared', 'Separate schools held inherently unequal, May 17, 1954'),
        ('Delayed', 'No date set in 1955; all deliberate speed instead'),
        ('Resisted', 'Manifesto, placement laws, grants, and closed schools'),
        ('Answered', 'Cooper in 1958: nullification closed, openly and indirectly')]
yy = 2.78
for t, d in rows:
    text(s, 0.9, yy, 2.4, 0.7, t, size=24, color=RUST_LT, font='Georgia')
    text(s, 3.45, yy + 0.05, 9.0, 0.9, d, size=19, color=CREAM, leading=1.2)
    yy += 1.05
notes(s, "Use this slide to close the argument before the work begins, and make students say the four rows aloud in order, because the sequence is the lesson. Declared: on May 17, 1954 a unanimous Court held separate educational facilities inherently unequal, ending the constitutional standing of legal segregation in the public schools after a campaign the NAACP had planned for two decades. Delayed: Brown II in 1955 required a prompt and reasonable start and then ordered admission with all deliberate speed, a phrase with no deadline in it. Resisted: into that open timetable stepped massive resistance, the Southern Manifesto signed by 101 members of Congress, pupil placement laws, tuition grants, and whole districts, Prince Edward County first among them, closing their public schools. Answered: Cooper v. Aaron in 1958 held state officials bound by the Court's reading of the Constitution and closed nullification in both its open and indirect forms, while the schools themselves remained almost entirely separate in 1964.")

# ------------------------------------------------------ 27 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did the NAACP turn a Kansas school case into the end of legal segregation, and how did the South answer? Build the argument chain before you judge the delay.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Case File: five stations, an argument chain, and a verdict on the delay'),
        ('Notebook', 'Notebook page: five moves in the argument, claimed to answered'),
        ('Quick check', 'The Decree: the Brown II judgment, the 1950 cases, and Cooper'),
        ('Writing', 'A Right Declared, a Decade Taken: the lesson question as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the Brown holding in one sentence, all deliberate speed with one tool of resistance, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Case File, puts five stations in front of students: the Brown opinion, Brown II, the Southern Manifesto, Cooper v. Aaron, and a labeled summary of the Prince Edward County closings, and it ends with an argument chain and a verdict on whether the delay was the price of unanimity or a separate failure. The notebook page asks students to chart the five moves of the argument. The quick check, The Decree, tests the Brown II judgment document, the two graduate school cases of 1950, the closing phrase and Prince Edward, and the Cooper answer to a defiant governor. The writing task turns the lesson question into an essay argued from the evidence bank, closing with the student's own judgment on the delay. The exit ticket has three parts: the Brown holding with the doctrine it displaced, all deliberate speed with one tool of resistance, and the lesson question in two or three sentences. Next lesson turns from the courts to the streets, in Montgomery and at Little Rock.")

dc.save(OUT)
