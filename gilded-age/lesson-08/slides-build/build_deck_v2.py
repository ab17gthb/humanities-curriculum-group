#!/usr/bin/env python3
"""Lesson 8 deck, "Race, Politics, and Protest," built to the approved
Progressive Era pilot system: image-led slides, fragments only on screen,
comprehensive speaker notes, full lesson + vocabulary coverage.
Fonts: Georgia titles, Lato body."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags, photo_right,
                         divider_photo, content_photo, content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED, W, H)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

HERE = os.path.dirname(os.path.abspath(__file__))
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

# ---------------------------------------------------------------- 1 · TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'GILDED AGE · LESSON 8', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Race, Politics, and Protest', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Two protest fronts of the 1890s, and the politics the next era inherited', size=17, color=POWDER)
notes(s, "This lesson closes the Gilded Age unit, and it runs on two tracks that students must keep separate. The first is the Jim Crow South: segregation written into law, the vote taken away, and Black Americans arguing over how to fight back. The second is the farm protest of the South and West: farmers in debt, organizing against railroads and deflation, building a third party that lost its final election and won much of its program anyway. One disclosure belongs with the title photograph. The photograph is from 1939, showing the Jim Crow system this lesson describes still in force decades later: a man drinking from a water cooler labeled for Black use in an Oklahoma City streetcar terminal, photographed by Russell Lee for the Farm Security Administration. By 1896 the two tracks met in one national election. Together they set the problems the Progressive movement would inherit, and judging that inheritance is the work of the lesson.")

# ------------------------------------------------- 2 · LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did Jim Crow and economic protest shape the politics that Progressives inherited?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did industrial growth transform American life, and who gained, who paid, and who resisted?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Read the lesson question aloud, then the unit question beneath it, because this lesson answers the unit question from its hardest angle. Who paid? Black southerners paid with their citizenship, stripped away in law and practice within a generation of emancipation. Indebted farmers paid with crops that bought less every year while their debts stayed fixed. Who resisted? Both groups resisted, in organized, documented, political ways, and this lesson follows their resistance rather than their suffering alone. Who gained? The white Democratic governments that rebuilt racial control in the South, and the creditors and railroads the farm movement named as its opponents. The narrower question on top asks what all of this handed to the Progressives after 1900. The short answer, which the lesson will complicate, is two inheritances at once: a tested reform program against concentrated economic power, and a segregated political order that most white reformers left standing.")

# --------------------------------------------------- 3 · THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.25, 11.5, 1.0, 'Two protests, one inheritance', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.32)
rows = [('A', 'The Retreat from Reconstruction', 'troops leave in 1877, and enforcement ends with them'),
        ('B', 'Jim Crow and Plessy', 'segregation written into law, and upheld in 1896'),
        ('C', 'Disfranchisement', 'the vote taken away, device by device'),
        ('D', 'Black Protest and Leadership', 'Wells documents lynching; Washington proposes a bargain'),
        ('E', 'Farmers, Grangers, and Populists', 'debt, deflation, and a third party'),
        ('F', '1896', 'free silver, Bryan, and a defeat that kept the ideas')]
yy = 2.68
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.7, n, size=24, color=RUST_LT, font='Georgia')
    text(s, 1.55, yy + 0.02, 4.6, 0.7, t, size=20, color=CREAM, bold=True)
    text(s, 6.3, yy + 0.06, 6.2, 0.7, d, size=17, color=POWDER)
    yy += 0.76
notes(s, "This map follows the guided notes section by section, and it also shows the lesson's architecture. Sections A through D tell the Jim Crow story in order: Reconstruction retreats, segregation becomes law, the vote is taken away, and Black leaders debate the response in public. Sections E and F then change fronts entirely. The farmers' grievance was economic, their organizations were the Grange, the Alliances, and a national third party, and their climax was a presidential election rather than a court case. Warn students against merging the two fronts into a single movement against the powerful. They named different problems, sought different remedies, and mostly moved separately, and the guided notes end with a Two Fronts at a Glance chart that grades exactly that distinction. The fronts meet only at the end, in 1896 and in the inheritance question, where students must say what each one handed to the Progressive Era.")

# ------------------------------------------------- 4 · SECTION A DIVIDER
divider_photo('first-vote-port.jpg', 'Section A', 'The Retreat from Reconstruction',
              ['Rights written into the Constitution,', 'and the enforcement withdrawn'],
              "The engraving is The First Vote, drawn by A. R. Waud for the cover of Harper's Weekly in November 1867. Three Black men are casting ballots for the first time: an older laborer, a younger man in a fine coat, and a veteran still in uniform. Hold this image in reserve, because the whole lesson is the story of what happened to the act it celebrates. After the Civil War, the Constitution itself had been amended to protect Black citizenship and Black men's voting. But amendments do not enforce themselves. They depended on federal troops, federal courts, and a northern public willing to sustain them, and by the 1870s that willingness was failing. Section A of the guided notes is short, three blanks, but it is the hinge of the lesson: when enforcement ended, everything in sections B and C became possible, and the voters in this engraving lost the protection the picture assumes.",
              title_size=40)

# ------------------------------------------------------ 5 · 1877
content_text('Rights on paper, enforcement ending',
             ['In 1877 Reconstruction ended, and federal troops left the South.',
              'White Democratic governments took control of the southern states.',
              'The Fourteenth Amendment protected citizenship.',
              'The Fifteenth Amendment protected Black men’s voting.',
              'Both protections depended on enforcement.'],
             "Give students the precise mechanics, because the guided notes test them in order. When Reconstruction ended in 1877, federal troops left the South and white Democratic governments took control of the southern states. That is blank one. Black southerners still held citizenship under the Fourteenth Amendment, blank two, and Black men held the vote under the Fifteenth Amendment, blank three. Nothing in the Constitution was repealed. What ended was enforcement: the soldiers who guarded polling places, the federal officials who prosecuted violence, the political will in Washington to intervene when a state government turned hostile. The distinction between rights on paper and rights in practice is the analytical key to the next three sections. Over the following twenty years, southern states built a new system of racial control in law, in politics, and in daily life, and they built it without ever formally amending the amendments away. Ask students to keep one question running: if the rights are still written down, what exactly does it take to nullify them?",
             kick='A · The retreat from Reconstruction', size=24)

# ------------------------------------------------- 6 · SECTION B DIVIDER
divider_photo('fountain-port.jpg', 'Section B', 'Jim Crow and Plessy',
              ['Segregation in law, in politics,', 'and in daily life'],
              "This portrait crop comes from the same photograph as the title slide, and the disclosure travels with it. The photograph is from 1939, showing the Jim Crow system this lesson describes still in force decades later: Russell Lee photographed a man drinking at a segregated water cooler in an Oklahoma City streetcar terminal, with the signs for white and Black restrooms behind him. Use the date deliberately. Students sometimes file Jim Crow away as a brief episode between slavery and the civil rights movement. A 1939 photograph of an ordinary man taking an ordinary drink of water corrects that: the system built in the 1890s was still governing daily life within living memory of people their grandparents knew. Section B now explains how that system became law, and how the Supreme Court placed it under constitutional protection in the same year as the election that ends the lesson.",
              title_size=46)

# ------------------------------------------------------ 7 · SEPARATION IN LAW
content_text('Separation written into law',
             ['State laws required separation by race.',
              'The laws covered schools, parks, hotels, theaters, and transportation.',
              'Separation was never equal in practice.',
              'Black schools received far less public money than white schools.',
              'Black rail cars were older and dirtier, and protest risked arrest.'],
             "Name the system first. State legislatures passed laws that required separation by race in schools, parks, hotels, theaters, and transportation, and the system took the name Jim Crow. The vocabulary definition arrives later in the lesson, but students can work with the mechanics now. Two facts keep the phrase separate but equal from sounding plausible. First, separation was never equal in practice: Black schools received far less public money than white schools, which is a budget decision, not an accident of prejudice. Second, the inequality was physical and daily: Black railroad cars were older and dirtier, and a Black passenger who protested the arrangement faced arrest, not an apology. Push students to see that Jim Crow was a legal system before it was a set of attitudes. Legislatures wrote it, appropriations funded it unequally, and police enforced it. That legal character is exactly why a court test came next, and why its result mattered so much.",
             kick='B · Jim Crow and Plessy', size=24)

# ------------------------------------------------------ 8 · PLESSY
content_text('Homer Plessy tests the law',
             ['In 1892, Plessy sat in a railroad car reserved for white passengers.',
              'His ride was a deliberate test of Louisiana’s separate car law.',
              'He was arrested, and his case rose through the courts.',
              'The Supreme Court decided the case on May 18, 1896, as Plessy v. Ferguson.'],
             "Slow down on the deliberateness, because it makes Plessy a protester and not only a victim. In 1892 Homer Plessy, a Black man from Louisiana, deliberately sat in a railroad car reserved for white passengers to test the state law that required separate cars. The arrest was the plan: only an arrest creates a case, and only a case can reach the Supreme Court. Students should recognize the strategy, because it is the legal version of what Wells was doing with evidence in the same years: force the system to state its rule in the open, in a record that cannot be denied. The case took four years to climb. It reached the Supreme Court at the end of a decade in which state after state had written segregation into law, and the question before the Court was whether the Fourteenth Amendment, the same amendment from section A, permitted a state to separate its citizens by race. The next slide gives the answer and the vote.",
             kick='B · Jim Crow and Plessy')

# ------------------------------------------------------ 9 · SEVEN TO ONE
stat('7 TO 1', 'the Supreme Court vote in Plessy v. Ferguson',
     'May 18, 1896. Upholding Louisiana segregation under separate but equal gave constitutional protection to segregation across the South.',
     "Dwell on the lopsidedness, because students assume landmark injustices were close calls. On May 18, 1896, the Supreme Court decided Plessy v. Ferguson by a vote of seven to one, upholding Louisiana segregation under the doctrine of separate but equal. One justice dissented, alone. The holding said, in effect, that a state could separate the races so long as the facilities were claimed to be equal, and that such separation did not violate the Fourteenth Amendment. Connect the ruling back to the reading's evidence: everyone in the courtroom knew the cars and schools were not equal, and the doctrine survived anyway, because the Court treated the claim of equality as enough. The decision gave constitutional protection to segregation across the South, which meant that challenging any single Jim Crow law now meant challenging a Supreme Court precedent as well. That is why 1896 matters twice in this lesson: the Court settled segregation in May, and the voters settled the money question in November.",
     kick='B · Jim Crow and Plessy')

# ------------------------------------------------- 10 · SECTION C DIVIDER
divider_text('Section C', 'Disfranchisement',
             'Segregation told Black southerners where they could sit. Disfranchisement took away the tool they could have used to answer.',
             "Set up the pairing before the mechanics, because the exit ticket tests the pairing directly. Plessy and disfranchisement reinforced each other. Segregation needed political protection: as long as Black men voted in large numbers, segregationist governments had to win elections against them. Disfranchisement removed that obstacle. Beginning with Mississippi in 1890, state conventions rewrote constitutions to remove Black men from the voter rolls. Note the venue: not legislatures passing ordinary laws, which courts and Congress might review, but constitutional conventions writing the barriers into the fundamental law of each state. And note the constraint the conventions worked under. The Fifteenth Amendment forbade denying the vote on account of race, so the devices they invented could not name race at all. The next slide takes the three devices from the guided notes in order, and students should be able to explain, for each one, how it fell on Black voters while protecting white ones.")

# ------------------------------------------------------ 11 · THREE DEVICES
content_text('Three devices, one result',
             ['Poll taxes were a fee voters had to pay before voting.',
              'Literacy tests were graded unfairly by white officials.',
              'Grandfather clauses protected white voters from the new barriers.',
              'Registration rules, white only primaries, fraud, and intimidation added more barriers.',
              'None of the devices had to name race.'],
             "Take the devices one at a time, with the answer key's explanations. Poll taxes priced poor voters out: a fee, often cumulative across years, stood between a poor Black farmer and the ballot box. Literacy tests handed white officials a grading pen: the same reading passage could pass a white applicant and fail a Black one, and the official's judgment was nearly impossible to appeal. Grandfather clauses were the safety valve for whites, exempting men whose grandfathers had voted before the Civil War, which in practice meant white voters, from the barriers that caught Black voters. Around the three named devices stood registration rules, white only primaries, fraud, and intimidation, and the reading is blunt that they did the rest. The design principle is the point to land: because the Fifteenth Amendment barred naming race, the system named money, literacy, and ancestry instead, and reached the same result. Black registration fell sharply in state after state.",
             kick='C · Disfranchisement', size=24)

# ------------------------------------------------------ 12 · WITHOUT THE VOTE
content_text('Politics without protection',
             ['Black registration fell sharply, state after state.',
              'Without the vote, Black southerners had no defense of their schools through politics.',
              'They had no defense of their juries and no defense of their personal safety.',
              'Plessy guarded segregation, and disfranchisement guarded Plessy.'],
             "Now draw the consequence the reading draws, in its own sequence. Without the vote, Black southerners could not defend their schools, their juries, or their safety through politics. Unpack each noun. Schools: school boards and legislatures answer to voters, and an disfranchised community cannot punish a board that starves its schools, which connects this section back to the unequal funding of section B. Juries: officials who run elections also shape jury pools, and a community without votes faces courts staffed entirely by the other side. Safety: sheriffs and prosecutors are elected, and the violence of the next section flourished partly because no officeholder feared Black voters at the next election. Then close with the formulation on the slide, which is also the exit ticket's first question: Plessy made segregation constitutional while disfranchisement removed the Black vote that might have challenged segregationist governments. Each half of the system protected the other. That closed loop is what Black protest, next, was up against.",
             kick='C · Disfranchisement')

# ------------------------------------------------- 13 · SECTION D DIVIDER
divider_photo('wells-port.jpg', 'Section D', 'Black Protest and Leadership',
              ['Two public strategies against', 'lynching and disfranchisement'],
              "The portrait is Ida B. Wells in about 1893, photographed by Mary Garrity in Chicago, one year after the pamphlet that made her name and drove her out of Memphis. Section D is a study in strategy under terrible constraints. The system described in sections B and C was closed: the courts had upheld it, the ballot was being taken away, and violence stood behind both. Black leaders agreed on the diagnosis and disagreed, in public, on the remedy. Wells chose confrontation: document the crime so exactly that denial fails, and carry the evidence to audiences with power. Booker T. Washington chose a bargain: accept segregation for the present and build the economic strength that might protect a future claim to rights. Students must be able to state both strategies in one sentence each, and to state the strongest criticism of Washington, because the guided notes, the quick check, and the writing task all return to this argument. Neither speaker is a hero or a villain in this lesson; both are strategists.",
              title_size=38)

# ------------------------------------------------------ 14 · WELLS
content_text('Ida B. Wells: evidence against lynching',
             ['In 1892, three of her friends were lynched in Memphis.',
              'Southern Horrors documented lynching with names, dates, and newspaper records.',
              'Many victims had committed no crime.',
              'The drivers were economic competition and racial control, not justice.',
              'A mob destroyed her office, and she campaigned on from the North and Britain.'],
             "Violence enforced what law began, and Wells is the lesson's witness to it. Lynch mobs killed Black people in public, often after accusations that were never tried in court, and local officials rarely punished the killers. Wells investigated lynching after three of her friends were lynched in Memphis in 1892, and her method is the point students must retain: in Southern Horrors, published that year, she used names, dates, and newspaper records, much of it from white southern newspapers, to show that many victims had committed no crime and that economic competition and racial control, not justice, drove the killings. Her friends had run a successful grocery competing with a white store, which is why the economic point is not abstract. A mob destroyed her newspaper office while she was away, and she continued her campaign from the North and in Britain, recruiting foreign opinion as leverage. Evidence, publicity, and outside pressure: hold the method up, because students will meet it again in the activity.",
             kick='D · Black protest and leadership', size=23)

# ------------------------------------------------------ 15 · WASHINGTON
content_photo_s('washington-port.jpg', 'Booker T. Washington and the Atlanta Compromise',
              ['Washington headed Tuskegee Institute in Alabama.',
               'In 1895 he delivered the speech called the Atlanta Compromise.',
               'Black southerners should accept segregation for the present.',
               'They should build economic strength first, through farming, trades, and business.'],
              "The portrait shows Washington later in life: C. M. Battey photographed him in about 1917, roughly twenty years after the speech this slide teaches, so students should picture a younger man in 1895. Washington, born enslaved, had built Tuskegee Institute in Alabama into a leading Black school for farming, trades, and teaching. In 1895 he delivered the speech later called the Atlanta Compromise. His proposal, in the reading's words, was that Black southerners accept segregation for the present and build economic strength first, through farming, trades, and business. He asked white southerners, in return, to employ and respect Black labor. White audiences praised the speech, and it made Washington the most recognized Black leader in America, with real influence over white philanthropy and Republican patronage. Teach the logic before the criticism, next slide: in a South where the vote was disappearing and violence went unpunished, Washington argued that property, skills, and institutions could be accumulated now and might be defended later. Whether that sequence could work is the argument.",
              kick='D · Black protest and leadership')

# ------------------------------------------------------ 16 · THE ARGUMENT
content_text('The argument over strategy',
             ['Black critics, including Wells, answered Washington.',
              'Giving up the vote and civil rights left gains unprotected.',
              'There was no way to protect schools, property, or personal safety.',
              'The debate between confrontation and accommodation outlived them both.'],
             "Give the criticism its full strength, as the guided notes do with blank fifteen. Black critics, including Wells, argued that giving up the vote and civil rights left Black people with no way to protect the gains Washington hoped to build. The argument is structural, and it reuses this lesson's own evidence. A school built by Tuskegee graduates is funded by a county board their parents cannot vote against. A farm bought with years of savings is taxed, zoned, or seized under laws made by legislatures they cannot reach. A prosperous Black businessman was, on Wells's evidence from Memphis, more exposed to a mob, not less, and no elected sheriff answered to him. Washington's defenders answered that demanding rights that could not yet be won might cost the institutions that existed. Do not settle the argument for the class. The exit ticket asks for one point of disagreement, stated fairly, and the writing task later asks students to judge which protest front left the deeper mark. Fair statement of both strategies is the skill being built.",
             kick='D · Black protest and leadership')

# ------------------------------------------------- 17 · SECTION E DIVIDER
divider_text('Section E', 'Farmers, Grangers, and Populists',
             'Change fronts now. The problem here is not the color line. It is the price of wheat, the interest on a loan, and the cost of a rail car.',
             "Mark the turn explicitly, because the lesson's discipline is keeping the fronts distinct. Farmers in the South and West had their own grievances, separate from Jim Crow, though the two stories will collide at the end of this section. After the Civil War, prices for cotton and wheat fell for decades while the costs of seed, equipment, and railroad shipping stayed high. A farmer could work harder, grow more, and fall further behind, and millions of them concluded that the game itself was rigged: by railroads that set rates without competition, by banks that lent dear and collected in appreciating dollars, by grain elevators that graded and stored the crop, and by a gold standard that limited the money supply. Their response was organizational, and it escalated in stages over twenty five years: a fraternal order in the 1870s, state laws, regional alliances in the 1880s, and a national political party in 1892. Follow the escalation, because each stage taught farmers skills the next one needed.")

# ------------------------------------------------------ 18 · DEBT AND DEFLATION
content_text('The farmers\u2019 grievance: debt and deflation',
             ['Crop prices fell for decades after the Civil War.',
              'The costs of seed, equipment, and shipping stayed high.',
              'Farmers borrowed at high interest.',
              'Deflation made each repaid dollar worth more than the one borrowed.',
              'Farmers blamed railroads, banks, elevators, and the gold standard.'],
             "Make the arithmetic physical, because question four of the reading and question four of the quick check both test it. A farmer borrows a fixed sum, say the quick check's thousand dollars, to plant a crop. Prices then fall by half, but the debt does not fall at all: it stays a thousand dollars, and the farmer must now sell roughly twice as many bushels to raise them. That squeeze has a name students need for blank sixteen: deflation, the process by which dollars grow more valuable as prices fall, so debts repaid later cost more in crops than when they were borrowed. Farmers borrowed at high interest and repaid in those appreciating dollars, while the prices of what they sold kept sliding and the prices of what they bought, seed, equipment, and railroad shipping, stayed high. Out of that arithmetic came a list of culprits: railroads, banks, grain elevators, and the gold standard, which limited the money supply and, in the farmers' account, kept dollars scarce and dear on purpose.",
             kick='E · Farmers, Grangers, and Populists', size=23)

# ------------------------------------------------------ 19 · GRANGER LAWS
content_text('The Grange and the Granger laws',
             ['In the 1870s, farmers organized through the Grange.',
              'Granger laws regulated railroad and warehouse rates.',
              'Courts at first upheld some of the regulation.',
              'The campaign taught farmers to act together in politics.'],
             "The first stage of escalation was the Grange, a farmers' organization that spread through the 1870s, part social order and part political school. Its achievement gives blank seventeen: farmers pushed states to pass Granger laws that regulated railroad and warehouse rates, the first serious attempt in the industrial era to say that a private business charging the public could be governed in the public interest. Courts at first upheld some regulation, which mattered beyond the rate schedules themselves: it established that regulation was constitutional territory a legislature could occupy. The deeper result was educational. Farmers who had competed against each other at the elevator learned to write a platform, lobby a legislature, and count votes, and the campaign taught farmers to act together in politics. When the Grange faded, its members and its habits moved into the Farmers' Alliances of the next decade, which is the bridge to the Omaha Platform. Students sometimes ask why a lesson on protest spends time on rate laws; the answer is that the Populist Party was built by people who had already won something once.",
             kick='E · Farmers, Grangers, and Populists')

# ------------------------------------------------------ 20 · OMAHA PLATFORM
content_text('Alliances and the Omaha Platform, 1892',
             ['In the 1880s, Farmers’ Alliances spread across the South and Plains.',
              'The Alliances built cooperatives and drafted demands together.',
              'In 1892, the Omaha Platform launched the Populist Party.',
              'The platform demanded railroad regulation, a graduated income tax, and more money in circulation.',
              'It also called for government ownership of railroads and the direct election of senators.'],
             "In the 1880s Farmers' Alliances spread across the South and Plains, building cooperatives that tried to bypass the merchants and elevators, and drafting demands together: railroad regulation, a graduated income tax, and more money in circulation. In 1892 those demands became the Omaha Platform of the new Populist Party, blank eighteen's answer, which also called for government ownership of railroads and the direct election of senators. Read the platform as the farmers' diagnosis turned into a program. Each plank answers a named grievance from the previous slides: regulation and ownership answer the railroads, the income tax answers concentrated wealth, direct election answers legislatures captured by corporate money, and more money answers deflation itself. Students will meet the last plank again as free silver, the demand that swallowed the rest in 1896. Note for later comparison that the platform was national and, at its founding, attempted something the next slide complicates: an alliance of producing classes across the color line, in the very years when disfranchisement was dismantling Black voting in the South.",
             kick='E · Farmers, Grangers, and Populists', size=23)

# ------------------------------------------------------ 21 · DIVIDED BY RACE
content_text('One movement, divided by race',
             ['The Populists won votes across regions.',
              'Holding Black and white farmers in one movement proved hard.',
              'Southern Democrats used race to divide them.',
              'Race divided what debt had united.'],
             "This short slide carries the lesson's most important connection between the two fronts, so do not rush it. The Populists won votes across regions, and in the South their movement required Black and white farmers to vote together against the Democratic governments that were, in those same years, building Jim Crow. Keeping Black and white farmers in one movement proved difficult, especially as southern Democrats used race to divide them: a white farmer could be told that his Populist vote endangered white supremacy, and a Black farmer could be promised protection, then disfranchised by the very men who promised it. The timing was fatal. Disfranchisement, section C, shrank the Black electorate the coalition needed at exactly the moment the coalition formed. When students reach the writing task and must rank the two fronts, this slide is the evidence that the fronts were not simply parallel: the Jim Crow system actively weakened the farm movement, and the politics Progressives inherited carried both the Populist program and the racial division that had broken it.",
             kick='E · Farmers, Grangers, and Populists')

# ------------------------------------------------- 22 · SECTION F DIVIDER
divider_photo('bryan-port.jpg', 'Section F', '1896',
              ['Free silver, Bryan, and the election', 'that ended a party and kept its ideas'],
              "The photograph shows William Jennings Bryan on stage beside an American flag during the 1896 campaign itself, on October 3, 1896, and Bryan did something no major nominee had done: he took his case on the road, speaking to enormous crowds across the country, because the newspapers and the money were mostly against him. He was thirty six years old, and he had won the Democratic nomination with a single convention speech on the money question. Section F is the climax both fronts have been building toward. For the farmers, 1896 was the Omaha Platform's one national test, fought on the single issue of free silver. For the Jim Crow story, 1896 was the year the arrangement hardened: the Supreme Court blessed segregation in May, and in November the election confirmed a Republican president who would not disturb it. Bryan lost, the Populist Party collapsed, and the demands survived him. Students should listen for all three outcomes: the defeat, the collapse, and the survival.",
              title_size=54)

# ------------------------------------------------------ 23 · CROSS OF GOLD
content_photo_s('cross-of-gold-port.jpg', 'A cross of gold',
              ['The Democrats nominated Bryan in 1896.',
               'His convention speech closed with an attack on the gold standard.',
               'He warned against pressing a crown of thorns on labor and crucifying mankind on a cross of gold.',
               'Judge magazine answered by calling him the sacrilegious candidate.'],
              "Teach the cartoon as hostile evidence, and say so. Judge magazine opposed Bryan, and its 1896 cover shows him trampling a Bible, carrying a wooden cross tagged as the cross of gold from his Chicago speech, and holding up a crown of thorns his campaign speeches used, under the caption calling him the sacrilegious candidate. The hostility is the historical point: Bryan's closing words at the Democratic convention, rejecting the gold standard by declaring that labor should not be pressed down with a crown of thorns nor mankind crucified on a cross of gold, were heard by supporters as prophecy and by opponents as blasphemy, and both reactions filled halls. The exact wording is documented and quoted in the activity; in class, the paraphrase in the reading is the safe form. Bryan campaigned for free silver across the country, and the Populists, facing a choice between their own ticket and fusion with the Democrats, endorsed him. That endorsement is the trap the next slides spring: it made Bryan stronger and the Populist Party unnecessary.",
              kick='F · 1896')

# ------------------------------------------------------ 24 · SIXTEEN TO ONE
stat('16 TO 1', 'the ratio at the heart of free silver',
     'Coin silver without limit at sixteen to one with gold, expanding the money supply and easing the squeeze of deflation.',
     "Give the number its full definition now, because it is a key term and the test will ask for it cold. Free silver meant minting silver dollars without limit at a ratio of sixteen ounces of silver to one ounce of gold. Because silver was cheaper than that ratio on the open market, coining it freely would have put far more money into circulation, raised prices, and lightened every farmer's debt in exactly the way deflation had raised it: a loan repaid in cheaper dollars costs fewer bushels. That is why a ratio on a slide deserves this size. To debtors, sixteen to one was not metallurgy; it was relief. To creditors and to urban workers who feared that inflation would raise the price of bread faster than wages, it was a threat, and that fear is part of why Bryan's coalition stopped at the city line. The gold standard's defenders called their position sound money. The election, next, decided between the two moneys, and with it the fate of the party that had made money a moral question.",
     kick='F · 1896')

# ------------------------------------------------------ 25 · MCKINLEY WINS
content_photo_s('mckinley-port.jpg', 'McKinley wins, and the ideas stay',
              ['William McKinley won the election of 1896.',
               'He was backed by business money and by workers who feared inflation.',
               'The Populist Party collapsed after the defeat.',
               'Many of its demands later became Progressive reforms.'],
              "The poster is the winning side's own argument, printed in 1896 by Gillespie, Metzgar and Kelley: William McKinley and Garret Hobart as home defenders, protection against free trade, factories smoking under the flag. McKinley, the Republican, won the election of 1896, blank twenty one, backed by business money on a scale Bryan could not match and by urban workers who feared inflation more than they hated the railroads. The Populists' endorsement of Bryan dissolved their separate identity, and the Populist Party collapsed. Then insist on the sentence students most need for the inheritance question. The party died and the program did not: many of its demands later became Progressive reforms, blank twenty two, including railroad regulation, a graduated income tax, and the direct election of senators. Progressives inherited both legacies from the 1890s, and the lesson ends where it began: a bold program against concentrated power, and a nation that had accepted segregation and disfranchisement as settled law. Hold both halves in view during the closing work.",
              kick='F · 1896')

# ------------------------------------------------------ 26 · VOCAB A
vocab('Words for the Jim Crow order',
      [('Jim Crow', 'the system of state and local laws and customs that enforced racial segregation in the South'),
       ('segregation', 'the separation of people by race in public facilities, schools, and transportation'),
       ('disfranchisement', 'the denial of the right to vote through law or practice')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. Jim Crow: the system of state and local laws and customs that enforced racial segregation in the South. Note that the definition includes customs as well as laws, which is why the system survived individual court challenges. Segregation: the separation of people by race in public facilities, schools, and transportation. Segregation is the practice; Jim Crow is the whole order that imposed it. Disfranchisement: the denial of the right to vote through law or practice. The last three words do the analytical work of section C: a poll tax is law, an unfairly graded test is practice, and the definition covers both, which is exactly how the southern conventions designed it. When students confuse the first two terms, send them to the definitions: one names a system, the other names an act of separating.")

# ------------------------------------------------------ 27 · VOCAB B
vocab('A ruling and a bargain',
      [('Plessy v. Ferguson', 'the 1896 Supreme Court decision that upheld segregation under the doctrine of separate but equal'),
       ('Atlanta Compromise', "Booker T. Washington's 1895 speech proposing that Black southerners accept segregation for the present and build economic strength first")],
      "Two more terms, again matching the guided notes exactly, and these two anchor sections B and D. Plessy v. Ferguson: the 1896 Supreme Court decision that upheld segregation under the doctrine of separate but equal. Students should attach the date, 1896, and the vote, seven to one, to the term whenever they use it, because the ruling's authority came from being constitutional law and not merely a southern statute. Atlanta Compromise: Booker T. Washington's 1895 speech proposing that Black southerners accept segregation for the present and build economic strength first. Every qualifier in that definition matters. For the present marks the acceptance as temporary in Washington's framing, and first marks economic strength as a sequence rather than a surrender: rights later, built on property and skill. Wells and the other critics answered that the sequence had the order wrong, because unprotected gains could be taken. Both vocabulary terms, ruling and bargain, are really arguments, and the test expects students to know who made each one and what it claimed.")

# ------------------------------------------------------ 28 · VOCAB C
vocab('Words for the farm revolt',
      [('Populist Party', "the People's Party, founded in 1892 to represent farmers and laborers against banks, railroads, and corporations"),
       ('free silver', 'the proposal to coin silver without limit at a ratio of 16 to 1 with gold, expanding the money supply')],
      "The last two terms carry section E and the election of 1896. Populist Party: the People's Party, founded in 1892 to represent farmers and laborers against banks, railroads, and corporations. The definition names the enemies as the party named them, and students should notice that the list is economic from end to end; the party's program, the Omaha Platform, followed from exactly this diagnosis. Free silver: the proposal to coin silver without limit at a ratio of 16 to 1 with gold, expanding the money supply. Without limit and expanding the money supply are the phrases to underline, because they separate free silver from ordinary silver coinage and connect it to deflation, the farmers' core grievance. A useful check before the closing work: ask a student to explain, using only these two definitions, why a party founded in 1892 ended up staking everything on a monetary ratio in 1896. The answer rehearses the whole second front in one move.")

# ------------------------------------------------------ 29 · TODAY'S WORK
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Two Fronts, One Inheritance', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Return to the lesson question. Keep the two fronts distinct: they named different problems, sought different remedies, and left different inheritances.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'Two-Front Protest Jigsaw: work one front, then teach the other'),
        ('Notebook', 'Two Fronts at a Glance: the chart that returns on review day'),
        ('Quick check', 'The 1939 photograph and five questions on the whole lesson'),
        ('Writing', 'Argue which front left the deeper mark on what Progressives inherited')]
yy = 4.35
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=19, color=CREAM)
    yy += 0.58
text(s, 0.9, 6.85, 11.5, 0.5, 'Next: the unit review and test, then the Progressive Era opens with this inheritance.',
     size=16, color=POWDER)
notes(s, "Close by handing the lesson to its work, which is built to keep the two fronts distinct. In the Two-Front Protest Jigsaw, each group works one front through three stations, then teaches the other front: Front A works the 1939 segregation photograph, Wells and lynching, and Washington's Atlanta Compromise; Front B works farm debt and the Granger laws, the Omaha Platform, and Bryan and free silver. Part 3 is completed together, and its instruction is the lesson's discipline: the fronts named different problems and sought different remedies. The notebook page, Two Fronts at a Glance, becomes the review day's study chart, so require complete rows today. The quick check returns to the 1939 photograph and asks five questions across both fronts, including the farmer's thousand dollar debt. The writing task, Two Fronts, One Inheritance, asks which front left the deeper mark on the politics Progressives inherited, and a both mattered equally answer does not meet the prompt. Next comes the unit review and test; the Progressive Era unit then opens with reformers holding the Populist program in one hand and a segregated nation in the other.")

dc.save(OUT)
