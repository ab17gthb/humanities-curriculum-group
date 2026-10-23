#!/usr/bin/env python3
"""Civil Rights Lesson 3 deck builder. Image led deck: 101st Airborne escort title, Parks fingerprint photograph, Eisenhower portrait, Little Rock escort crops. The Till photographs are not reproduced anywhere in this deck; section D is text only, by the unit rule."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
LESSON_DIR = os.path.dirname(HERE)
UNIT_DIR = os.path.dirname(LESSON_DIR)
sys.path.insert(0, UNIT_DIR)
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags,
                         divider_photo, content_photo, content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED, W, H)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

dc.IMG = os.path.join(HERE, 'img')
OUT = os.path.join(LESSON_DIR, 'lesson-03-slides.pptx')

spec = open(os.path.join(UNIT_DIR, 'build-scripts', 'unit-spec.md')).read()
sec = spec.split('### Lesson 3')[1].split('### Lesson 4')[0]
TERMS = []
for line in sec.splitlines():
    line = line.strip()
    if line.startswith('- '):
        t, d = line[2:].split(': ', 1)
        TERMS.append((t.strip(), d.strip()))
assert len(TERMS) == 7, TERMS
TD = dict(TERMS)

def vocab(title, terms, note, kick='The vocabulary'):
    s = slide(CREAM)
    kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95, 11.5, 1.0, title, size=30, color=NAVY, font='Georgia')
    yy = 2.1
    for term, dfn in terms:
        text(s, 0.9, yy, 4.1, 0.9, term, size=24, color=NAVY, font='Georgia')
        text(s, 5.15, yy + 0.06, 7.3, 1.1, dfn, size=18, color=MUTED, leading=1.2)
        yy += 1.52
    notes(s, note)
    return s

SHORT = {
 'boycott': 'a refusal to buy or use services as protest, withdrawing the money an institution depends on',
 'Montgomery bus boycott': '381 days off the buses in 1955 and 1956, ending when the Supreme Court ordered the buses desegregated',
 'nonviolent direct action': 'protest that confronts an unjust practice openly and without violence, accepting arrest to expose it',
 'Southern Christian Leadership Conference': 'founded in 1957 by King and other Black ministers to coordinate protest campaigns across the South',
 'Emmett Till': 'the fourteen-year-old murdered in Mississippi in 1955, whose published photographs showed the nation the violence',
 'Little Rock Nine': 'the nine Black students who desegregated Central High in 1957 under federal troop protection',
 'Executive Order 10730': "Eisenhower's order of September 24, 1957 federalizing the Arkansas Guard and directing troops to Little Rock",
}

# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'THE CIVIL RIGHTS MOVEMENT · LESSON 3', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Montgomery and Little Rock', size=30, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'A warning letter, 381 days on foot, a record the nation had to face, and soldiers at a schoolhouse door.', size=17, color=POWDER)
notes(s, "Open with the photograph. It shows soldiers of the 101st Airborne Division escorting Black students to Central High School in Little Rock, Arkansas, in September 1957, near the end of the story this lesson tells. Lessons 1 and 2 built the ground: the institutions Black Americans had raised under Jim Crow, and the Brown decision that declared school segregation unconstitutional without setting a deadline for ending it. This lesson asks what happened when ordinary people tried to use that ruling. The answer runs through two cities. In Montgomery, Alabama, a boycott taught the movement how to sustain pressure for more than a year. In Little Rock, nine students and a court order met a governor's soldiers, and the federal government was forced to decide whether its own courts would be obeyed.")
# 2 QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did a bus boycott and nine schoolchildren teach the movement its methods, and force the federal government to act?', {})]], size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': RUST_LT, 'italic': True}), ('How did the civil rights movement change American law and American life, and what did it leave unfinished?', {'italic': True})]], size=17, color=POWDER, font='Georgia', leading=1.2)
notes(s, "Read the lesson question aloud and separate its two halves, because the exit ticket and the writing task grade them separately. The first half is about methods, and it is answered from Montgomery and from the Till record: a boycott that withdrew the money a bus company depended on, an organization built to run the campaign, and the deliberate publication of evidence so the nation had to look at a killing. The second half is about compulsion, and it is answered from Little Rock: a governor defied a federal court with his own soldiers, and that defiance, not the president's agreement with Brown, forced the federal government to act. Connect the question to the unit question beneath it. The methods learned here are the tools the rest of the unit will watch the movement use, and test, for a decade.")
# 3 MAP
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Two cities, and the methods between them', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'A Warning Before the Arrest', "Robinson's 1954 letter and the boycott it prepared"),
        ('B', 'December 1, 1955: The Arrest', 'Rosa Parks, the charge, and the leaflets that night'),
        ('C', 'The Boycott Holds: 381 Days', 'The MIA, the car pool, mass meetings, and Browder'),
        ('D', "The Summer's Wound: Emmett Till", 'A murder, an acquittal, and a published record'),
        ('E', 'Little Rock: A Governor Bars the Door', 'Faubus, the Guard, and nine students turned away'),
        ('F', 'The President Acts', 'The address, Executive Order 10730, and the 101st'),
        ('G', 'The Answer, and the Method', "Faubus replies, the Lost Year, and the lessons carried forward")]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This map follows the guided notes section by section. Sections A, B, and C tell Montgomery in order: the warning letter of 1954 that proves the boycott was prepared, the arrest of December 1, 1955 that gave it an occasion, and the 381 days that show what organization could sustain. Section D steps back to the summer of 1955 and the murder of Emmett Till, taught here as the bank carries the record, described rather than shown, because the Jet photographs are copyrighted magazine images. Sections E and F tell Little Rock as a contest of authority: a governor barring a schoolhouse door, and a president answering with an address, an executive order, and paratroopers. Section G closes with Faubus's reply, the Lost Year, and the method the two cities together taught. Tell students to track one question through every section: where did the power sit, and what moved it?")
# 4 DIVIDER A
divider_text('Section A', 'A Warning Before the Arrest', "May 21, 1954: a professor writes to the mayor, lists three requests, and names the riders' power.",
 "Teach this section as the correction to the easiest version of the Montgomery story, in which a tired seamstress acted alone and a movement appeared from nowhere. Jo Ann Robinson was an English professor at Alabama State College and president of the Women's Political Council, an organization of Black professional women that had been pressing the city on bus treatment for years. Her letter of May 21, 1954 followed a hearing the council had won that March, and its three requests were specific: seating from back toward front and front toward back, an end to paying at the front and boarding at the rear, and stops at every corner in Black neighborhoods. Around those requests sits the fact the whole boycott would rest on. Three-fourths of the riders were Black. The letter is a negotiation document carrying a threat, and students should read it that way.")
# 5 CONTENT A
content_text('Three-fourths of the riders', ["Robinson's letter to Mayor Gayle, May 21, 1954", 'Three requests: seating, boarding, and bus stops', 'Three-fourths of the riders were Black', 'The buses could not operate without their fares', 'More than twenty-five organizations talking boycott'],
 "Carry the definition exactly as the guided notes print it. A boycott is this: " + "boycott: " + TD['boycott'] + ". Then work the letter's arithmetic aloud, because it is the boycott's whole theory in one sentence. A bus company in Montgomery sold rides, and three of every four rides were sold to Black passengers who were insulted on board as a condition of the purchase. Withdraw those fares for long enough and the company, not the riders, faces the crisis. Robinson's letter states that power politely, as a plea, and dates it: May 1954, the same month as the Brown decision, a year and a half before the arrest that made Montgomery famous. When students later call the boycott spontaneous, send them back to this letter. The network, the grievances, and the tactic were all on paper before Rosa Parks was arrested.")
# 6 DIVIDER B
divider_photo('parks-port.jpg', 'Section B', 'December 1, 1955: The Arrest', ['Rosa Parks refuses the order, is fingerprinted and charged, and the leaflets go out that night.'],
 "Introduce the arrest through the photograph, which needs its date stated exactly. It shows Rosa Parks being fingerprinted by Lieutenant D. H. Lackey on February 22, 1956, during the mass indictments of boycott leaders, not on the day of her arrest. The arrest itself, on December 1, 1955, produced a paper record the bank carries: a fingerprint card signed Rosa L. Parks, dated 12-1-55, and a police report charging her with refusing to obey an order of the bus driver under the city code. Parks was secretary of the Montgomery branch of the NAACP and a trained activist, and her own written reflection, carried in the bank, says she had been pushed around all her life and could not take it anymore. Teach the arrest as the act of a prepared person inside a prepared network, because that is what the records show.")
# 7 CONTENT B
content_photo('parks-port.jpg', 'The charge, and the leaflets', ["Parks refuses the driver's order, December 1, 1955", "Charged with refusing to obey the bus driver", "Secretary of the local NAACP branch", "The council prints leaflets through the night", 'A one-day boycott called for Monday, December 5'],
 "Walk the night of December 1 in sequence, because the speed of it is the evidence of preparation. Parks was arrested in the early evening, booked, fingerprinted, and released on bond. Jo Ann Robinson and the Women's Political Council then worked through the night at Alabama State College mimeographing tens of thousands of leaflets, and students and couriers carried them across Black Montgomery the next day. The leaflet called for one day off the buses, Monday, December 5, the day of Parks's trial. Note what the council did not do: it did not call an open-ended campaign it could not yet sustain. It proposed a single day, a test of whether the ridership Robinson had counted in 1954 would in fact stay home. The answer to that test fills the next section, and it changed the one day into 381.")
# 8 DIVIDER C
divider_text('Section C', 'The Boycott Holds: 381 Days', 'An association to run it, a car pool to replace the buses, and mass meetings to hold the line.',
 "Frame the boycott as an organizational achievement before it is a moral one, because the organization is what students can transfer to later campaigns. Within days of December 5, Montgomery's Black residents had formed the Montgomery Improvement Association, an organization of their own, and elected as its president a twenty-six-year-old pastor new to the city, Martin Luther King Jr. The association had to solve a transport problem for some 42,000 people, absorb the arrests of its leaders, survive the bombing of its president's house, and keep a weekly rhythm of decision and encouragement running for more than a year. Bayard Rustin, the veteran organizer who visited in February 1956 and whose diary is Station 2 of the activity, recorded the system at work. His diary is the section's best evidence, and the next slide reads it closely.")
# 9 CONTENT C
content_text('The system that replaced the buses', ['The Montgomery Improvement Association runs the boycott', '42,000 riders stay off the buses', 'Police harass and arrest taxi drivers', 'A car pool with 23 dispatch centers', 'Weekly mass meetings in Black churches'],
 "Carry both definitions exactly. The Montgomery bus boycott is this: " + "Montgomery bus boycott: " + TD['Montgomery bus boycott'] + ". Nonviolent direct action is this: " + "nonviolent direct action: " + TD['nonviolent direct action'] + ". Then read Rustin's diary as an operations report. When police harassed, intimidated, and arrested the Black taxi drivers who had carried boycotters at bus fare, the association built the car pool: 23 dispatch centers where riders gathered for free transportation, hundreds of private cars, and church stations across the city. Rustin met men who had walked 7 miles and 14 miles every day since December 5. That is the texture to teach: a tactic is a leaflet for one day, but a campaign is dispatch centers, mass meetings, bail funds, and walkers, held together for 381 days until a court ended the practice the boycott had already defeated in fact.")
# 10 STAT C
stat('381 days', 'of boycott in Montgomery, December 1955 to December 1956', 'Ended when the Supreme Court ruled in Browder v. Gayle that bus segregation was unconstitutional',
 "Stop on this number and make the class price it. Three hundred eighty-one days is not a demonstration; it is a second transport system run by volunteers through a winter and a summer, under indictments of its leaders, with King's house bombed in January 1956 while the boycott held. The boycott's ending deserves the same precision. The boycott did not persuade Montgomery to relent. A federal case, Browder v. Gayle, brought by Black plaintiffs through the courts, was affirmed by the Supreme Court in November 1956, and when the written order reached Montgomery in December the association voted to end the boycott and ride the desegregated buses. Teach the pairing honestly: protest created the pressure and the record, and litigation delivered the legal result. The movement carried both tools out of Montgomery, and the rest of this unit is partly the story of learning when each one worked.")
# 11 DIVIDER D
divider_text('Section D', "The Summer's Wound: Emmett Till", 'August 1955: a fourteen-year-old murdered, his killers acquitted, and a mother who made the nation look.',
 "Set the handling rule for this section before the content, and state it the way the student materials state it. The Jet photographs of Emmett Till are copyrighted magazine images. They are not reproduced in this lesson, in the documents, or in this deck, following the bank record, which describes them without reproducing them. What is taught is the record: what happened in Mississippi in August 1955, what a jury did, what Mamie Till-Mobley decided, and what the publication of David Jackson's photographs did to the country. The chronology matters. Till was killed three months before the Montgomery boycott began, and for many of the young people who would staff the movement's next decade, the published photographs were a formative fact. Handle the section at documentary weight: exact dates, exact sequence, no embellishment, and let the record carry the effect.")
# 12 CONTENT D
content_text('Described, not shown', ['Emmett Till, fourteen, visiting Mississippi from Chicago', 'Murdered in August 1955 after an accusation', 'An all-white jury acquits in about an hour', 'The men confess to a magazine for money', "His mother publishes the photographs in Jet"],
 "Carry the definition exactly. Emmett Till is this: " + "Emmett Till: " + TD['Emmett Till'] + ". Then teach the bank record's description as the document it is, in the record's own sequence. In September 1955 Jet magazine published photographs by David Jackson showing the open casket of Emmett Till. His mother insisted the world see what had been done to her son. The bank record's verdict is measured and students should quote it rather than inflate it: the images shocked the nation and helped galvanize the civil rights movement. Connect the record forward. The boycott that began that December drew on a generation that had seen those pages, and the tactic at work, witness, the deliberate making of a public record that cannot be unseen, stands beside boycott in the movement's ledger for the rest of the unit.")
# 13 DIVIDER E
divider_photo('littlerock-port.jpg', 'Section E', 'Little Rock: A Governor Bars the Door', ['September 1957: the Arkansas National Guard posted at Central High to keep nine students out.'],
 "Introduce Little Rock through the photograph's reversal, which students will meet again in the next section. The soldiers in this photograph are escorting the students into Central High under federal orders. Three weeks earlier, soldiers of a different command, the Arkansas National Guard answering to Governor Orval Faubus, stood at the same school to keep the same students out. The nine students, remembered as the Little Rock Nine, had been selected to desegregate Central High under a federal court order following Brown. Faubus claimed he acted to prevent violence. On September 4 the students were turned away, and Elizabeth Eckford, fifteen, who had not received word of the group's meeting plan, walked toward the school alone through a hostile crowd. The photograph of her walk, taken by a press photographer, is copyrighted and is not used in this lesson; the Army photograph on this slide is the federal record of the answer.")
# 14 CONTENT E
content_photo('littlerock-port.jpg', 'Turned away at the door', ['A federal court orders nine students admitted', 'Faubus posts the Arkansas National Guard', 'Elizabeth Eckford walks alone, September 4', 'The Nine enter September 23, withdrawn within hours', "A governor's soldiers stop a federal court order"],
 "Carry the definition exactly. The Little Rock Nine are these: " + "Little Rock Nine: " + TD['Little Rock Nine'] + ". Then slow down on the legal shape of the confrontation, because it explains everything Eisenhower does next. This was not a protest against a local custom. A federal district court had ordered the students admitted under a desegregation plan the school board itself had drawn. The governor interposed his state's military force between the court's order and its execution. On September 23 the students entered through a side door while a crowd gathered outside, and police withdrew them within hours, judging that their safety could not be guaranteed. At that point every ordinary agency had failed in public: the court had ordered, the governor had obstructed, and the city could not protect nine teenagers. The question the reading ends the section with is the right one: what would the federal government do?")
# 15 DIVIDER F
divider_text('Section F', 'The President Acts', 'September 24, 1957: an address to the nation, an executive order, and the 101st Airborne.',
 "Introduce Eisenhower with the fact students find hardest to hold: he had never publicly endorsed Brown, and his address does not endorse it. His public case was narrower and, for his purpose, stronger. Disorderly mobs had prevented the carrying out of proper orders from a federal court, local authorities had not eliminated the opposition, and the responsibility of the president to uphold the federal courts was, in his word, inescapable. Teach the address and the order as one instrument in two parts. The address, delivered on radio and television on September 24, explained the duty to the nation. The order, signed the same day, performed the legal act: it took the Arkansas Guard out of the governor's hands and put federal troops at the Secretary of Defense's disposal. Words and mechanism together are the section's subject.")
# 16 CONTENT F
content_photo('eisenhower-port.jpg', 'The order behind the troops', ['Eisenhower addresses the nation, September 24, 1957', '"Mob rule cannot override the decisions of our courts"', 'Executive Order 10730 signed the same day', 'The Arkansas Guard placed under federal command', 'The 101st Airborne escorts the Nine, September 25'],
 "Carry the definition exactly. Executive Order 10730 is this: " + "Executive Order 10730: " + TD['Executive Order 10730'] + ". Then read the order's mechanism from the bank text, because its plainness is the point. Section 1 authorizes the Secretary of Defense to call the Arkansas National Guard into federal service for an indefinite period and until relieved by appropriate orders. Section 3 authorizes him to use such of the armed forces of the United States as he may deem necessary. The same Guard that had barred the door now answered to Washington, and paratroopers of the 101st Airborne Division, a federal force with no local chain of command, escorted the nine students into Central High on September 25. The students finished the school year under military protection. A court order, defied, had acquired an army.")
# 17 STAT F
stat('101st', 'Airborne Division sent to Little Rock, September 1957', 'Federal paratroopers escorted nine students to class after a governor defied a federal court',
 "Use this slide to mark the scale of the precedent, with the facts kept exact. The 101st Airborne was an elite combat division, and its soldiers were sent to an American high school to walk nine teenagers past a crowd to their classes. The Archives account of the order records that Eisenhower sent 1,000 paratroopers to Little Rock, and the order itself placed the Arkansas National Guard under federal command for an indefinite period. Tell students what this was in constitutional terms rather than in spectacle. For the first time since Reconstruction, a president had used federal troops to enforce the civil rights of Black citizens against a state government. The precedent, not the headcount, is the figure to remember: defiance of a federal court by a governor would be answered with federal force.")
# 18 DIVIDER G
divider_text('Section G', 'The Answer, and the Method', "Faubus calls Arkansas occupied territory, closes the schools, and the movement counts its lessons.",
 "Close the lesson by giving the resistance its own voice before summarizing the method, because students judge Faubus better from his words than from a summary of them. His statement of September 26, 1957, carried in the bank from the Eyes on the Prize transcript, opens with the claim that Arkansas was now an occupied territory and appeals to God, liberty, and decency against the federal action. It commanded no soldiers after September 24, and its power was political rather than military: it kept resistance respectable for the voters who returned Faubus to office, and it framed the following year, in which he closed Little Rock's high schools entirely rather than operate them desegregated. The Lost Year is the honest ending to the Little Rock story. The troops won the schoolhouse door. They did not win the school system, and the difference between those two results is a fact the rest of the unit keeps meeting.")
# 19 CONTENT G
content_text('What the two cities taught', ["Faubus: Arkansas is 'an occupied territory'", "Little Rock's high schools closed for the Lost Year", 'Boycott: withdraw the money an institution needs', 'Witness: publish the record the nation must face', 'Court order defied: federal power follows'],
 "Carry the definition exactly. The Southern Christian Leadership Conference is this: " + "Southern Christian Leadership Conference: " + TD['Southern Christian Leadership Conference'] + ". Its founding in 1957, weeks after the boycott ended, is the institutional proof that Montgomery's method was meant to travel: King and other Black ministers built a regional organization to coordinate campaigns like the one the Montgomery Improvement Association had improvised locally. Then assemble the lesson's ledger with the class. Montgomery contributed the boycott and the sustaining organization. The Till record contributed witness. Little Rock contributed the federal lever and its limit: a court order could summon troops, and a governor could still close the schools. The campaigns of the next lessons, the sit-ins, the Freedom Rides, and Birmingham, were designed by people who had studied exactly this ledger.")
# 20 GLANCE
s = slide(NAVY)
kicker(s, 'The tactics at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Boycott, witness, and troops', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Montgomery', '381 days off the buses, the MIA and the car pool', 'Browder v. Gayle desegregates the buses'),
        ('The Till record', 'Open casket, photographs published in Jet', 'The nation sees what a jury excused'),
        ('Little Rock', "A governor bars the door with his Guard", 'Order 10730, the federalized Guard, the 101st'),
        ('The reply', "Faubus: 'occupied territory,' then closed schools", 'The Lost Year, 1958 and 1959')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the closing table of the guided notes, The Tactics at a Glance, and students should complete that table now from memory where they can. Check the table with the two questions that expose shallow answers. First, which rows show power the movement generated itself, and which show power it borrowed? Montgomery and the Till record are the movement's own work, fares withdrawn and evidence published. The Little Rock row is borrowed power, federal troops the movement did not command, summoned by a court order and a governor's defiance. Second, which row is unfinished? The reply row: the Lost Year shows a victory at the schoolhouse door answered by the closing of the schools themselves. The table is the lesson in miniature: methods learned, federal power compelled, and resistance adapting in reply.")
# 21 VOCAB A
vocab('Words for the boycott', [(t, SHORT[t]) for t in ['boycott', 'Montgomery bus boycott', 'nonviolent direct action', 'Southern Christian Leadership Conference']],
 "Four terms, matching the guided notes word for word, and students should copy the definitions because the unit test draws on them. boycott: " + TD['boycott'] + ". Montgomery bus boycott: " + TD['Montgomery bus boycott'] + ". nonviolent direct action: " + TD['nonviolent direct action'] + ". Southern Christian Leadership Conference: " + TD['Southern Christian Leadership Conference'] + ". Press the pairing of the first two terms. The general term names the lever, withdrawn money and cooperation. The specific term names the campaign that taught the movement the lever could be held for 381 days, and its definition ends where the campaign ended, in a Supreme Court order.")
# 22 VOCAB B
vocab('Words for the wound and the door', [(t, SHORT[t]) for t in ['Emmett Till', 'Little Rock Nine', 'Executive Order 10730']],
 "Three more terms, again matching the guided notes exactly. Emmett Till: " + TD['Emmett Till'] + ". Little Rock Nine: " + TD['Little Rock Nine'] + ". Executive Order 10730: " + TD['Executive Order 10730'] + ". Two details in these definitions earn emphasis before the exit ticket. The Till definition joins the funeral to the publication, because the choice to publish is the tactic this lesson teaches under the name of witness. The order's definition names both of its actions, federalizing the Guard and directing federal troops, and a student who can state only one of the two has half the instrument Eisenhower actually used.")
# 23 SYNTHESIS
content_text('Answering the question', ['The methods: boycott, organization, and witness', 'The occasion: an arrest, a murder, a barred door', 'The compulsion: defiance leaves the president no exit', 'The limit: troops open a school; a governor closes it'],
 "Run the synthesis as the writing task rehearsal, and build it from the class's own answers before summarizing. Strong answers hold the lesson's two halves together and refuse to drop either. The first half is capacity: by the end of 1957 the movement possessed a tested boycott method, an organization built to sustain it, and a hard education in what published evidence could do to national opinion. The second half is compulsion: at Little Rock the movement's own tools could not open the school, because the opposing force was a state's military under a governor's orders. What forced the federal government to act was the defiance itself, a court order publicly stopped by soldiers, which no president could let stand without surrendering the authority of every federal court. Test the synthesis against its rival before closing: the federal government was not persuaded in 1957. It was cornered, and the difference explains the decade that followed.")
# 24 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4, ['How did a bus boycott and nine schoolchildren teach the movement its methods, and force the federal government to act?'], size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Tactics Ledger: five records, the tactic or power in each, then a verdict'),
        ('Notebook', 'Notebook page: the tactics chart, from the warning letter to the federal answer'),
        ('Quick check', 'Soldiers at the Schoolhouse Door: the Army photograph, sourced and connected to Montgomery'),
        ('Writing', 'The Methods and the Federal Answer: the methods and the compulsion in one essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: boycott defined with the MIA and King named, the two actions of Executive Order 10730, and the lesson question in two or three sentences.', size=15, color=POWDER)
notes(s, "Close by handing the lesson to the work. In the activity, The Tactics Ledger, each group works five records, the Robinson letter, the Rustin diary, the Till photograph record as the bank describes it, the Eisenhower address, and the Faubus statement read beside Executive Order 10730, enters the tactic or power each record shows, and judges which of the five moved the country most. The notebook page rebuilds the lesson as a chart of what happened, the tactic or power shown, and the result. The quick check, Soldiers at the Schoolhouse Door, sources the Army photograph of the 101st Airborne escort and tests whether students can connect it back to Montgomery's method. The writing task, The Methods and the Federal Answer, requires the lesson's double answer in essay form. The exit ticket has three parts: a boycott defined with the Montgomery Improvement Association and King named, the two actions of Executive Order 10730 stated, and the lesson question answered in two or three sentences.")

dc.save(OUT)
