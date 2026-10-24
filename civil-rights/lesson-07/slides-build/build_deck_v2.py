#!/usr/bin/env python3
"""Civil Rights Lesson 7 deck, "The Movement Turns North and Inward:
Chicago, Black Power, Memphis," built on the shared deck system:
image-led slides, fragments only on screen, comprehensive speaker
notes, full lesson + vocabulary coverage. Fonts: Georgia titles, Lato body."""
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
OUT = os.path.join(HERE, '..', 'lesson-07-slides.pptx')

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
text(s, 0.9, 5.30, 11.5, 0.4, 'THE CIVIL RIGHTS MOVEMENT · LESSON 7', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.64, 11.9, 1.0, 'The Movement Turns North and Inward', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.52, 11.5, 0.45, 'Chicago, Black Power, Memphis', size=17, color=POWDER)
text(s, 0.9, 7.02, 11.9, 0.4, 'Portrait photograph of Malcolm X in 1964, Library of Congress.', size=11, color=POWDER)
notes(s, "Open with the portrait and the dates, because this lesson begins at the movement's highest point and asks what happened next. In the summer of 1965 the movement had won the two great acts, the Civil Rights Act of 1964 and the Voting Rights Act of 1965, by methods it had spent a decade perfecting: disciplined nonviolent protest, a crisis the cameras could carry, and a federal government forced to enforce its own Constitution. Malcolm X, in the photograph, had been assassinated that February, and his argument outlived him inside the movement he had criticized. Within three years the movement had marched into Chicago and been met by mobs, had split in public over a two word slogan, had founded a party that patrolled the police, had turned toward poverty as its subject, and had lost Martin Luther King Jr. to an assassin in Memphis. The lesson follows that sequence in order and asks students to judge the argument the movement had with itself.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.7, 11.5, 3.6, [[('Why did the movement\u2019s methods stop working as it moved north, and how did its own people argue about what freedom required next?', {})]],
     size=40, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.5)
text(s, 0.92, 5.75, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the civil rights movement change American law and American life, and what did it leave unfinished?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Read the lesson question in its two halves, because the lesson answers both and the writing task grades both. The first half is about place and method. The movement's methods had been built for the South, where segregation was written into statutes, enforced by named officials, and vulnerable to court orders and federal enforcement. The North presented a different structure, and the first half of the lesson shows the methods meeting it in Watts, in the housing lines of northern cities, and in Chicago. The second half is about argument inside the movement itself. Between 1966 and 1968, Black Americans debated what freedom required next in public: integration pressed further, Black political and economic power, self-defense and community programs, or an economic campaign against poverty itself. The unit question runs beneath as the frame. This lesson is where the unit's unfinished business first gets named by the movement's own people, before the nation answers in the next lesson.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'North, inward, and economic', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'Five Days After the Vote: Watts', 'The law signed; a neighborhood rises'),
        ('B', 'The Northern Problem', 'Segregation in fact, not in law'),
        ('C', 'Chicago: The Movement Marches North', 'Open housing marches and the mobs'),
        ('D', 'The Argument Inside: Black Power', 'Greenwood, June 1966'),
        ('E', 'Malcolm X and the Panthers', 'Nationalism, patrols, and programs'),
        ('F', 'The Turn to Economics', "The Poor People's Campaign planned"),
        ('G', 'Memphis and April 4, 1968', 'A strike, a speech, an assassination')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A opens five days after the Voting Rights Act, in Watts. Section B names the northern problem, de facto segregation. Section C follows King into Chicago, where the method met mobs and an unenforced agreement. Sections D and E cover the argument inside the movement, Black Power on the Meredith March, and the inheritance of Malcolm X carried into the Black Panther Party. Section F turns to economics, King's planned Poor People's Campaign. Section G closes in Memphis, with the sanitation strike, the speech of April 3, and the assassination of April 4, 1968. The summary table at the end of the guided notes asks students to rebuild this map in their own words, and the activity sorts the argument itself from five documents.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', 'Five Days After the Vote: Watts',
             'August 6, 1965, a law signed. August 11, a neighborhood rises.',
             "Section A is placed first because its dates carry the lesson's problem in their shortest form. The Voting Rights Act, signed on August 6, 1965, was the movement's greatest legislative victory and the fruit of Selma, of Bloody Sunday, and of a president addressing Congress in the movement's own language. Five days later, the Watts neighborhood of Los Angeles rose after a traffic stop, and six days of violence left thirty four people dead. Teach the juxtaposition without flattening it. Watts was not a comment staged for the cameras, and no organization led it. It was an explosion of grievances its residents named afterward with complete consistency: police treatment, housing, jobs, and schools. The section's work is to make students hold both facts at once, that the movement had just won a genuine and enormous victory, and that the victory's instruments, statutes aimed at southern voting practices, did not reach the conditions of a northern or western city street.")

# ------------------------------------------------------ 5 A WATTS
content_text('Watts, August 1965',
             ['Six days of violence left thirty four people dead.',
              'No organization planned or directed the uprising.',
              'Residents named grievances over police, housing, pay, and schools.',
              'Victories in Washington were measured against conditions on one street.'],
             "Work through the four fragments in order and keep the account plain. The rising began on August 11, 1965, with a highway patrol traffic stop and a gathering crowd, in a district of Los Angeles where Black residents had been concentrated by the same housing practices this lesson takes up next. It spread for six days. Thirty four people died, more than a thousand were injured, and hundreds of buildings were burned or damaged before National Guard troops restored order. The second fragment does analytical work: Watts was not a movement protest, it had no demands presented to an authority, no negotiation, and no leadership able to call it off, which is part of why it unsettled movement leaders as much as it unsettled city officials. The grievances named afterward are the curriculum of the rest of the lesson. Every one of them, police treatment, housing, employment, and schools, reappears in Chicago, in the Panthers' program, and in King's economic turn.",
             kick='A · Five days after the vote')

# ------------------------------------------------------ 6 STAT 34
stat('34', 'people died in the Watts uprising',
     'Los Angeles, August 11 to 17, 1965 · Five days after the Voting Rights Act was signed',
     "Let the number stand without decoration, because it is a count of the dead and the lesson treats it in that form. Thirty four people died in Watts in August 1965, most of them Black residents of the district itself, which is a fact students should register about urban uprisings generally: their heaviest costs fell on the neighborhoods that rose, in lives, in burned housing and stores, and in the services that did not return. The date underneath is the lesson's hinge. The Voting Rights Act had been signed five days before the rising began, with the movement's leaders present at the ceremony and a quarter of a million new voters about to register in the South. Nothing in this slide argues that the act failed. It argues that the act, aimed at the South's voting statutes, answered a different question from the one Watts was asking, and the distance between those two questions is the distance the rest of the lesson travels.",
     kick='A · Five days after the vote')

# ------------------------------------------------- 7 SECTION B DIVIDER
divider_text('Section B', 'The Northern Problem',
             'No statute to strike down: covenants, redlining, and lines on a map.',
             "Section B supplies the analytical core of the lesson, the concept on which the quick check and the writing task both depend. In the South, segregation was de jure, imposed by law, and that legal form was also its weakness. A statute can be sued, a court can strike it, and a governor who defies the order creates the crisis that moves a president. Northern segregation was de facto, in fact rather than in law, and it was built from thousands of decisions that each claimed to be private or neutral: a covenant in a deed, a lender's risk map, a family's move to a suburb, a school board's attendance line. No one decision carried the system, and no court order against one decision could dismantle it. Teach students to say this precisely. The northern problem was not that racism was hidden, since the mobs of the next section were visible enough. The problem was that its legal address was missing.")

# ------------------------------------------------------ 8 B DE FACTO
content_text('Segregation without a statute',
             ['Restrictive covenants barred Black buyers from many neighborhoods.',
              'Redlining steered mortgage money toward white suburbs.',
              'White flight moved families and the tax base out of changing neighborhoods.',
              'School lines followed neighborhoods that housing had already sorted.'],
             "Take the four practices one at a time and attach an actor to each, because the section's point is that the system had builders even though it had no single author. Restrictive covenants were clauses in property deeds barring sale to Black buyers, enforced for decades across whole neighborhoods. Redlining was the practice of lenders, backed by federal housing policy, treating Black neighborhoods as bad risks and directing mortgage money toward white suburbs instead, so Black families who could have bought were kept renting. White flight named the movement of white families who could afford to leave changing neighborhoods, taking the tax base with them. School boards then drew attendance lines around the neighborhoods housing had sorted, and could describe the resulting segregated schools as an accident of geography. Students should copy the four practices into section B of the notes. The writing task requires the northern problem stated in exactly these terms before any verdict about answers.",
             kick='B · The northern problem', size=24)

# ------------------------------------------------------ 9 B WHY METHODS
content_text('Why the old method found no handle',
             ['A court order needs a law to strike down.',
              'A boycott needs an institution that depends on you.',
              'A crisis needs an official who can be forced to yield.',
              'Chicago supplied none of the three in southern form.'],
             "This slide states the lesson question's first half as a piece of reasoning, and students should be able to reproduce it. Review the southern instruments quickly. Litigation worked because statutes existed to be declared unconstitutional, and Brown and its successors struck them one by one. The boycott worked because a bus company and a downtown depended on Black fares and Black customers. Direct action worked because a sheriff or a governor could be maneuvered into a public defiance that forced federal enforcement. In the northern city, each instrument met a system with no comparable handle. There was no segregation statute for a court to strike. The landlords, lenders, and school boards were numerous, private in form, and able to wait out a campaign. And when Chicago's government did sign an agreement, as the next section shows, nothing compelled it to enforce one. The methods had not lost their courage or their discipline. They had lost their target shape.",
             kick='B · The northern problem', size=24)

# ------------------------------------------------- 10 SECTION C DIVIDER
divider_text('Section C', 'Chicago: The Movement Marches North',
             'King rents a tenement flat, and the marches go into Marquette Park.',
             "Section C is the test case of the lesson, the campaign in which the movement applied its proven method to the northern problem deliberately and with full knowledge of what it was doing. King and the Southern Christian Leadership Conference joined Chicago's local movement in 1966, and King rented a flat in a West Side tenement to make the housing issue personal and visible. The campaign's demands reached housing, schools, and jobs, and its open housing marches into white neighborhoods were modeled on the marches that had worked in the South. The section should be taught as a fair test rather than a blunder. The strategy was the strongest the movement had, applied by its most experienced leadership, in a city with a large and organized Black community. What it met there, mobs as hostile as any in the South and an agreement its signers did not enforce, is therefore evidence about the problem, not only about the campaign.")

# ------------------------------------------------------ 11 C CHICAGO
content_text('The Chicago Freedom Movement, 1966',
             ['King rented a tenement flat on the West Side.',
              'Open housing marches entered white neighborhoods.',
              'At Marquette Park, mobs threw bottles and bricks and struck King.',
              'A Summit Agreement was promised and was not enforced.'],
             "Narrate the campaign through the four fragments. King moved into a tenement flat at the start of 1966 and held the building's conditions up as the campaign's first exhibit: northern slum housing maintained at high rents because its tenants had nowhere else the market would take them. The marches then carried the demand into the white neighborhoods whose covenants and customs excluded Black buyers. At Marquette Park in August 1966 the marchers were met by mobs carrying swastikas and throwing bottles and bricks, and a brick struck King himself. He said afterward, in paraphrase, that he had not seen mobs as hostile even in Mississippi or Alabama. The campaign closed with a Summit Agreement with the city, its business leadership, and its religious leadership, promising steps toward open housing. The city did not enforce it. Note the absence of a federal referee in this story. No troops came to Chicago, because no court order had been defied.",
             kick='C · Chicago', size=24)

# ------------------------------------------------- 12 SECTION D DIVIDER
divider_text('Section D', 'The Argument Inside: Black Power',
             'Greenwood, Mississippi, June 1966: a slogan replaces a word.',
             "Section D turns from place to argument, and it should be introduced as a debate among people who had shared jails and marches, not as a split between strangers. In June 1966 James Meredith, the man who had desegregated the University of Mississippi in 1962, set out alone on a March Against Fear to encourage Black voter registration, and he was shot and wounded on the second day. The movement's organizations continued the march together, King beside the younger leaders of SNCC and CORE, and the disagreements that had been growing in private were argued in public along the road. The setting matters for judging the slogan that came out of Greenwood. This was Mississippi, the state of Chaney, Goodman, and Schwerner two summers earlier, and the marchers were registering voters under the protection of a voting act whose promises local officials were already working to narrow. The call for Black Power was raised in that place, by a man coming out of jail.")

# ------------------------------------------------------ 13 D BLACK POWER
content_text('Black Power, June 1966',
             ['Carmichael was arrested for the twenty seventh time.',
              'Freedom had been said for six years and, in his words, answered with nothing.',
              'SNCC and CORE moved toward Black leadership.',
              'King refused the slogan and understood its source.'],
             "Use the activity's Station 2 text for the quotation itself, and teach this slide as the argument around it. Stokely Carmichael had become chairman of the Student Nonviolent Coordinating Committee in May 1966, displacing John Lewis in an internal vote that itself announced the organization's turn. At Greenwood he was arrested for setting up tents for the marchers, his twenty seventh arrest, and he came to the night rally announcing that he would go to jail no more. The slogan he raised named a shift from asking to building: Black political organization, Black economic strength, and freedom defined by Black people themselves. King refused the slogan, fearing it would be heard as a call to violence and would cost the movement its allies, and he said so on the march. He also understood its source, and students should hold both halves. A decade of nonviolence had been answered with bombs, beatings, and acquittals, and the slogan was raised by the people who had absorbed that answer.",
             kick='D · The argument inside', size=24)

# ------------------------------------------------- 14 SECTION E DIVIDER
divider_text('Section E', 'Malcolm X and the Panthers',
             'The earlier voice behind the argument, and the party it helped shape.',
             "Section E gives the argument its genealogy and its organization. The genealogy runs through Malcolm X, assassinated in February 1965, fifteen months before Greenwood, whose nationalism had been formed in a Garvey household and sharpened through a decade as the Nation of Islam's most effective voice before his break with it in 1964. Students sometimes meet the Black Power turn as a sudden invention of 1966. This section corrects the date. The case for Black control of Black communities' politics and economics had been argued for years, in speeches and in an autobiography published after Malcolm's death, and the younger organizers of SNCC had read and heard it. The organization is the Black Panther Party, founded in Oakland in October 1966, which converted that case into a program, a uniform, a set of patrols, and a set of services, and which the federal government then worked to destroy. The section holds the party's two faces together throughout: arms and breakfasts, patrols and clinics.")

# ------------------------------------------------------ 15 E MALCOLM
content_photo_s('malcolm-port.jpg', 'Malcolm X: the nationalist case',
              ['Malcolm X grew up in a Garvey household and rose through the Nation of Islam before his break in 1964.',
               'He argued that the Black vote should be used as a weapon, not given as a gift.',
               'He called for control of community politics and economics.',
               'He was assassinated in February 1965, and his argument outlived him.'],
              "The photograph is a portrait of Malcolm X in 1964, from the New York World Telegram and Sun collection at the Library of Congress, and the activity's first station is his argument in his own words, quoted within the unit's cap and counted there. Teach the paraphrase on this slide from the reading. Malcolm had inherited Marcus Garvey's nationalism from his father, an organizer for Garvey's movement, including the belief, quoted once in the student reading from his Autobiography, that freedom and self respect could never be won inside the American arrangement as it stood. After breaking with the Nation of Islam in 1964 he founded his own organizations and argued that Black people should control the politics and the economy of their own communities, use their votes as a bloc rather than a loyalty, and defend themselves when the state would not. He was assassinated in February 1965. The organizers who raised Black Power in 1966 had absorbed his case while he lived and carried it after his death.",
              kick='E · Malcolm X and the Panthers')

# ------------------------------------------------------ 16 E PANTHERS
content_text('The Black Panther Party, Oakland, 1966',
             ['Newton and Seale founded the party in October 1966.',
              'Members patrolled the police with law books and rifles.',
              'The Ten Point Program demanded freedom, jobs, housing, and an end to brutality.',
              'Breakfast programs and health clinics served neighborhoods while the FBI answered.'],
             "Teach the party from its program outward, using Station 3 of the activity, where students read four of the ten points in the program's own short form. Huey Newton and Bobby Seale founded the party in Oakland in October 1966, in a northern city whose Black neighborhoods had been built by wartime migration and were policed as the Watts grievances described. The patrols came first in public attention: members observing police stops, carrying law books and rifles where California law then allowed, on the stated ground that the community had a right to defend itself. The program joined that stance to demands for full employment, decent housing, and an end to police brutality. The services made the party an institution in its neighborhoods: free breakfasts for children and health clinics, run by the same organization the newspapers described only by its arms. The Federal Bureau of Investigation treated the party as a threat and worked through surveillance and raids against it.",
             kick='E · Malcolm X and the Panthers', size=23)

# ------------------------------------------------- 17 SECTION F DIVIDER
divider_text('Section F', 'The Turn to Economics',
             "King's last campaign aimed the movement at poverty itself.",
             "Section F returns to King, because his answer to the northern problem was neither the slogan he refused nor a retreat to the South. Through the winter of 1967 and 1968 he planned the Poor People's Campaign, an attempt to bring an interracial army of the poor to Washington and to stay there until the federal government acted on poverty. Teach the reasoning in his own terms as the reading states them. The movement had won legal equality at lunch counters and voting booths at a price the nation could call cheap, since a court order and a statute cost most white Americans nothing they held. Equality in wages, housing, and schools would cost far more, in money and in neighborhood arrangements, and that was why it had not come and why only federal economic action could carry it. The campaign divided his advisers and drew little support from the old coalition. It was the supporting work for this campaign that took King to Memphis.")

# ------------------------------------------------------ 18 F POOR PEOPLES
content_text("The Poor People's Campaign, planned 1967 to 1968",
             ['An interracial army of the poor would come to Washington.',
              'The campaign demanded jobs, income, and housing.',
              'King proposed an economic bill of rights.',
              'The old coalition withheld its support.'],
             "Work through the design before its fate, because students often meet this campaign only as the thing King was doing when he died. The design was a camp in the capital, an interracial army of the poor, Black, white, Mexican American, Puerto Rican, and Native American, brought to Washington to demand federal action on poverty and to remain until it came. The demands were jobs or income, decent housing, and the means to live, stated as an economic bill of rights, on the theory that the first bill of rights had secured legal standing and the second would secure material standing. State the opposition honestly. The coalition that had passed the acts of 1964 and 1965, labor, churches, liberal organizations, and the Johnson administration in its stronger years, gave the plan little support, and King's own organization was divided over it. The campaign went forward anyway, carried on after his death as Resurrection City, and its reception is part of the next lesson's account of the unfinished agenda.",
             kick='F · The turn to economics', size=24)

# ------------------------------------------------- 19 SECTION G DIVIDER
divider_text('Section G', 'Memphis and April 4, 1968',
             'A sanitation strike, a claim of dignity, and the shot at the Lorraine Motel.',
             "Section G closes the lesson, and it is taught at documentary pace, plainly and in order. In February 1968, two Black sanitation workers in Memphis were killed by a malfunctioning garbage truck, in a department where Black workers were sent home without pay in bad weather while white workers were not, and 1,300 workers struck for union recognition, safer conditions, and fair treatment. King came to Memphis to support them, as a supporting action of the economic campaign the previous section describes. His first march in the city broke into violence. He returned at the start of April determined to lead a peaceful march, spoke to the strikers at Mason Temple on April 3, and was assassinated the next day on the balcony of the Lorraine Motel. The section's last slide follows the week after, when uprisings rose in more than a hundred cities and the statute and the verdict that answered them waited in the next lesson.")

# ------------------------------------------------------ 20 G MEMPHIS
content_text('The Memphis sanitation strike, 1968',
             ['Two workers were killed by a malfunctioning truck.',
              'The city refused to recognize the union.',
              'The strikers carried signs that read I Am a Man.',
              'King came to Memphis, a march broke into violence, and he returned.'],
             "The facts of the strike are stated in the fragments and should be taught without addition. The strikers were the men who collected Memphis's garbage, employed by the city, and their dispute joined the ordinary subjects of a labor strike, recognition, pay, and safety, to the standing the signs assert. Read the sign as the activity's fourth station reads it. It makes no request and names no term of settlement. It asserts the manhood of the men carrying it, with the middle word underlined, against a city whose treatment of them had denied it. King came to support the strike in March, and the march he led on March 28 broke into violence, for which he was blamed in the press and by the city. He left, and he returned on April 3 determined to prove that a peaceful march in Memphis was possible. The march he returned to lead was planned for April 8. It was held after his death, in silence, led by his widow.",
             kick='G · Memphis', size=24)

# ------------------------------------------------------ 21 STAT 1300
stat('1,300', 'Black sanitation workers struck in Memphis',
     'Strike began February 12, 1968 · After two workers were killed by a malfunctioning truck',
     "The figure comes from the audited bank record for the Memphis posters, which states that 1,300 Black sanitation workers in Memphis went on strike on February 12, 1968, after two workers were crushed by a malfunctioning garbage truck, demanding union recognition, better pay, and safer conditions. Hold the composition of that sentence in front of the class. The number is a workforce, not a crowd: the entire Black sanitation force of a major American city, withholding the labor the city could not run without, over deaths on the job and over treatment that sorted workers by race in pay and in weather. The strike is the lesson's clearest joining of the movement's two late subjects. Its instrument was the oldest economic instrument there is, the strike, and its claim, printed on the signs, was the oldest claim in the movement's record, full human standing. King did not create that joining in Memphis. He recognized it, and he came.",
     kick='G · Memphis')

# ------------------------------------------------------ 22 G APRIL 4
content_text('April 3 and April 4, 1968',
             ['At Mason Temple on April 3, King addressed the strikers.',
              'In paraphrase, he said he was unafraid and glad to be in the struggle.',
              'On April 4 he was shot on the balcony of the Lorraine Motel.',
              'Uprisings rose in more than a hundred cities within a week.'],
             "Teach April 3 from the paraphrase, because King's words that night are his own copyrighted text and this lesson paraphrases them, as the reading does. He told the strikers, in substance, that he was glad to be alive in a time of struggle, that he was unafraid of what might come, and that the movement would reach its goal with or without him. The next evening, April 4, 1968, he was shot while standing on the balcony of the Lorraine Motel, where he was staying during the Memphis campaign, and he died that evening at the age of thirty nine. State the response plainly. In the week that followed, uprisings rose in more than a hundred American cities, the largest wave since Watts, and troops patrolled Washington itself. The federal commission on the urban disorders had delivered its verdict a month earlier. The next lesson takes up that verdict, the housing act passed in the assassination's shadow, and the reckoning of what the movement won and left undone.",
             kick='G · Memphis', size=24)

# ------------------------------------------------------ 23 VOCAB A
vocab('Words for the northern turn',
      [('de facto segregation', 'segregation in fact, not in law'),
       ('Chicago Freedom Movement', "King's 1966 campaign against housing and school segregation"),
       ('Watts uprising', 'six days of violence in Los Angeles, August 1965'),
       ('Black Power', "Carmichael's 1966 call to build Black political and economic power")],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. The first term is de facto segregation: segregation in fact rather than in law, produced by housing patterns, economics, and custom, the form segregation took in the cities of the North. The second is Chicago Freedom Movement: Martin Luther King Jr.'s campaign of 1966 against housing and school segregation in Chicago, met by violent mobs on its open-housing marches and ended by an agreement the city did not enforce. The third is Watts uprising: the six days of violence in the Watts neighborhood of Los Angeles in August 1965, beginning five days after the Voting Rights Act was signed, in which thirty four people died. The fourth is Black Power: the call raised by Stokely Carmichael in Mississippi in June 1966 for Black Americans to build their own political and economic power and to define freedom for themselves rather than rely on white goodwill.")

# ------------------------------------------------------ 24 VOCAB B
vocab('Words for the argument and the end',
      [('Black Panther Party', 'founded in Oakland in 1966; patrols, breakfasts, clinics'),
       ("Poor People's Campaign", "King's planned 1968 campaign against poverty"),
       ('Memphis sanitation strike', 'the 1968 strike whose signs read I Am a Man')],
      "Three more terms, again matching the guided notes exactly. The first is Black Panther Party: the organization founded in Oakland, California in 1966 by Huey Newton and Bobby Seale, which patrolled the police, carried arms in self-defense, and ran free breakfast and health programs in Black neighborhoods. The second is Poor People's Campaign: Martin Luther King Jr.'s planned campaign of 1968 to bring an interracial army of the poor to Washington to demand federal action on poverty, carried on after his assassination as Resurrection City. The third is Memphis sanitation strike: the strike of 1968 by Black sanitation workers in Memphis, Tennessee, whose signs read I Am a Man, and which brought Martin Luther King Jr. to the city where he was assassinated. Students sometimes merge the second and third terms because King was killed during the strike while planning the campaign. Keep them apart in the notes: the campaign was the national design, the strike was the local action that drew him to Memphis.")

# ------------------------------------------------------ 25 SYNTHESIS
s = slide(NAVY)
kicker(s, 'The record at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'North, inward, economic, Memphis', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Faced', 'De facto segregation; Watts, 1965', 'No statute at the center to strike'),
        ('Tested', 'Chicago, 1966', 'Mobs at Marquette Park; agreement unenforced'),
        ('Argued', 'Black Power; the Panthers, 1966', 'Power built, not requested'),
        ('Turned', "Poor People's Campaign, planned 1968", 'Poverty as the subject; coalition withheld'),
        ('Ended', 'Memphis, April 4, 1968', 'A strike supported; a leader assassinated')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, The Record at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The five rows compress the argument of the hour. Faced: the movement met a northern segregation built in fact rather than in law, and Watts announced its grievances five days after its greatest legislative victory. Tested: in Chicago the proven method was applied by its most experienced leadership and produced mobs and an agreement nobody enforced. Argued: the movement's own people answered with new positions, Black Power at Greenwood, Malcolm's nationalism behind it, and a party in Oakland joining patrols to programs. Turned: King aimed the movement at poverty itself and found the old coalition unwilling to follow. Ended: in Memphis a strike joined the dignity claim to the economic claim in one sign, and the man who had carried the movement for thirteen years was killed supporting it.")

# ------------------------------------------------------ 26 EXIT
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Why did the methods stop working in the North, and which answer, power, economics, or the promise, does the evidence support best? Argue it from the documents.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Argument File: Malcolm, Carmichael, the Ten Point Program, the Memphis posters, Kerner'),
        ('Notebook', 'Notebook page: the turn from statutes to structures in five stages'),
        ('Quick check', 'The Northern Problem: the Kerner verdict read closely'),
        ('Writing', 'What Freedom Required Next: the northern problem, then a verdict, then the counterclaim')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: de facto segregation defined, the Memphis signs and the larger campaign, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by handing the lesson to the work. The activity, The Argument File, runs five stations: Malcolm's ballot argument quoted within the unit cap, Carmichael's Greenwood call as the public record carries it, four points of the Panthers' Ten Point Program from the party newspaper, the Memphis poster record with its slogans transcribed from the audited bank record, and the Kerner Commission's verdict, ending with a sorting of the five records by vision of freedom and a defended verdict. The notebook page holds the five stages from Watts to Memphis. The quick check, The Northern Problem, tests close reading of the Kerner passage against the lesson's background sequence. The writing task, What Freedom Required Next, requires the northern problem stated first, one verdict, three dated pieces of evidence, and an answer to the strongest fact against the verdict chosen, and it names the linked TPSP premium DBQ on the visions of freedom as its extension. The exit ticket has three parts, as printed at the end of the guided notes.")

dc.save(OUT)
