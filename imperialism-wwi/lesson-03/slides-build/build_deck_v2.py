#!/usr/bin/env python3
"""Lesson 3 deck, "An Empire in the Philippines," built to the approved
Progressive Era system: image-led slides, fragments only on screen,
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
OUT = os.path.join(HERE, '..', 'lesson-03-slides.pptx')

def vocab(title, terms, note, kick='The vocabulary', step=1.52):
    s = slide(CREAM)
    kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95, 11.5, 1.0, title, size=30, color=NAVY, font='Georgia')
    yy = 2.1
    for term, dfn in terms:
        text(s, 0.9, yy, 4.1, 0.9, term, size=25, color=NAVY, font='Georgia')
        text(s, 5.15, yy + 0.06, 7.3, 1.1, dfn, size=19, color=MUTED, leading=1.2)
        yy += step
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
text(s, 0.9, 5.32, 11.5, 0.4, 'IMPERIALISM AND WORLD WAR I · LESSON 3', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'An Empire in the Philippines', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'A treaty signed in Paris, a republic proclaimed at Malolos, and a war over consent', size=17, color=POWDER)
notes(s, "Open on Filipino prisoners of war at Pasig, photographed in 1899 and published by Underwood and Underwood as a stereograph; the Library of Congress holds the copy this crop comes from. Say what the photograph is and is not. It shows captured Filipino soldiers under guard in the opening year of the war this lesson studies, seated in rows while American soldiers stand over them. It does not show a battle, and students should not read it as one. Use it to set the puzzle of the hour. In December 1898 the United States bought the Philippine Islands from Spain for 20 million dollars. By the time this photograph was taken, American soldiers were fighting the very people who had proclaimed their own republic the year before. How a purchase in Paris became a war in Luzon, and what that war cost, is the lesson.")

# ------------------------------------------------- 2 · LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, 'Did taking the Philippines extend American ideals or contradict them?',
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('Why did the United States seek power overseas, and how did the First World War change the country that fought it?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Put the lesson question at the center of the hour and keep it visible, because the exit ticket and the writing task both answer it directly. It is a genuine two sided question, and the lesson is built to give each side its strongest evidence. The extension case rests on the promises: just government in place of arbitrary rule, schools, courts, an elected assembly. The contradiction case rests on the record: a treaty signed without Filipinos, a republic treated as an insurrection, rule without consent, and a war whose civilian deaths are estimated at as many as 200,000. The unit question underneath asks why the United States sought power overseas at all, and this lesson gives the fullest answer in the unit: markets, strategy, claimed duty, and a debate the country nearly voted the other way. Tell students their job today is not to pick a side early. It is to collect the evidence for both.")

# --------------------------------------------------- 3 · THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.3, 11.5, 1.0, 'An empire decided, debated, and fought over', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.42)
rows = [('A', 'A Treaty and a Vote', 'Paris, December 1898; the Senate decides by one vote'),
        ('B', 'The League Against Empire', 'Boston organizes the case against annexation'),
        ('C', 'The Philippine Republic', 'independence at Kawit; a constitution at Malolos'),
        ('D', 'Benevolent Assimilation and War', 'a promise of friendship, then three years of war'),
        ('E', 'Courts and Civil Government', 'the Insular Cases, Taft, and an assembly in 1907')]
yy = 2.82
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.7, n, size=26, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.03, 3.6, 0.7, t, size=21, color=CREAM, bold=True)
    text(s, 5.35, yy + 0.08, 7.1, 0.7, d, size=18, color=POWDER)
    yy += 0.9
notes(s, "This is the map of the lesson, and it follows the guided notes section by section. We start in Paris, where Spain and the United States settled the Philippines between themselves, and in Washington, where the Senate approved that settlement by the narrowest margin the Constitution allows. Then the organized opposition: the American Anti-Imperialist League and the unlikely coalition behind it. Section C turns the camera around and looks at the same months from the Filipino side: a revolt against Spain, a proclaimed independence, a written constitution, a republic. Section D puts the American promise and the American war side by side, including the methods used and the deaths that followed. Section E closes with the law and the government the United States built on the islands it kept. By the end, students hold every piece of evidence the writing task asks them to weigh.")

# ------------------------------------------------- 4 · SECTION A DIVIDER
divider_photo('prisoners-port.jpg', 'Section A', 'A Treaty and a Vote',
              ['The treaty was signed in Paris on December 10, 1898.', 'The Senate approved it by a margin of one vote.'],
              "The photograph is the same Pasig prisoners image from the title slide, cropped for this slot: Filipino prisoners of war in 1899, from the Underwood and Underwood stereograph held by the Library of Congress. It belongs at the head of this section for a reason students should hear stated plainly. The treaty and the vote came first, and the prisoners came after. Every document in this section was produced by men who never saw the Philippines: diplomats in Paris trading islands they did not live on, senators in Washington arguing about people most had never met. The Filipino envoy who traveled to both capitals to plead for independence was refused a hearing in each. Keep that sequence in front of the class through the next three slides: first the signatures, then the single vote, then the war the signatures and the vote set in motion.",
              title_size=54)

# ------------------------------------------------------ 5 · THE TREATY
content_text('A treaty signed in Paris',
             ['Spain and the United States signed the treaty on December 10, 1898.',
              'Spain gave up Cuba, Puerto Rico, and Guam.',
              'Spain ceded the Philippines for 20 million dollars.',
              'No Filipino signed the treaty, and no Filipino was heard at Paris.',
              'Officials refused envoy Felipe Agoncillo a hearing in Paris and Washington.'],
             "Work the guided notes blanks in order, because the first three answers all sit in this one paragraph of the reading. The Treaty of Paris, signed December 10, 1898, ended the Spanish American War. Spain gave up Cuba, Puerto Rico, and Guam, and ceded the Philippine Islands to the United States for 20 million dollars. Then slow down on the absence at the center of the document. No Filipino signed the treaty or was heard at Paris. The Philippine envoy Felipe Agoncillo traveled to Paris and then to Washington to argue for independence, and officials in both capitals refused to receive him. The reading closes the section with the contrast students should copy into their thinking: the treaty settled the islands between two empires, while their people were building a government of their own. Section C shows that government. First, the treaty had to survive the Senate.",
             kick='A · A treaty and a vote', size=24)

# ------------------------------------------------------ 6 · THE SENATE DEBATE
content_text('The debate in the Senate',
             ['Ratification needed two thirds of the Senate.',
              'Expansionists promised markets and a coaling station on the route to China.',
              'Expansionists claimed a duty to govern people they said could not govern themselves.',
              'Expansionists warned that Germany or Japan would seize the islands.',
              'Opponents answered that rule without consent breaks the founding principle.'],
             "Through January 1899 the outcome stayed in doubt, and students should understand both cases at full strength before they see the vote. The expansionist case had three parts. The Philippines offered markets and a coaling station on the route to China, a practical argument about trade and steamships. Supporters claimed a duty to govern people they argued could not govern themselves, a claim Section C tests against the Malolos constitution. And they warned that Germany or Japan would seize the islands if America let them go, which was a real strategic fear in 1899, not an invention. The opposition case was constitutional. Ruling millions of people without their consent broke the founding principle of the United States, the principle of the Declaration of Independence itself. Neither side was arguing about whether the islands had value. They were arguing about what the republic was allowed to do with its power.",
             kick='A · A treaty and a vote', size=24)

# ------------------------------------------------------ 7 · STAT: THE VOTE
stat('57 TO 27', 'Senate vote to ratify the Treaty of Paris, February 6, 1899',
     'One vote more than the two thirds required. One senator switching sides defeats the treaty.',
     "Dwell on the arithmetic, because the exit ticket tests it and students reliably get it wrong on first reading. Ratification required two thirds of the Senate. Eighty four votes were cast on February 6, 1899, and two thirds of 84 is 56. The treaty received 57 votes, one vote more than required. A vote that looks one sided, 57 to 27, was in fact decided by a single senator. Had one supporter switched sides, the count falls to 56 to 28, the two thirds line is missed, and the treaty fails. Everything after this slide in the lesson, the war, the court cases, the civil government, rests on that margin. Two days before the vote, on February 4, fighting had already begun outside Manila, and senators voted knowing American and Filipino soldiers were shooting at each other. The closeness of the vote is the first evidence students should log for the writing task: annexation was not a national consensus. It was a contested choice, made by the narrowest constitutional margin.",
     kick='A · A treaty and a vote')

# ------------------------------------------------- 8 · SECTION B DIVIDER
divider_photo('school-port.jpg', 'Section B', 'The League Against Empire',
              ['The opposition organized in Boston in 1898.', 'A Puck cartoon taught empire as a schoolroom.'],
              "The image is School Begins, drawn by Louis Dalrymple and published in Puck magazine on January 25, 1899, while the Senate debate was still running; the Library of Congress holds the print. Uncle Sam stands as a schoolmaster before four children labeled Philippines, Hawaii, Puerto Rico, and Cuba, while other students, including a Black child, a Native American child, and Chinese and Mexican figures, watch from the room. Name the problem in the image directly, the way the quick check does: the cartoon draws its Filipino, Hawaiian, Puerto Rican, and Cuban figures as racial caricatures, the standard style of American political cartooning in 1899. That is not a reason to look away from it. It is evidence about how annexation was sold and pictured at home, and students will analyze this same cartoon in the quick check. This section studies the Americans who fought the treaty anyway.",
              title_size=44)

# ------------------------------------------------------ 9 · THE LEAGUE
content_photo_s('school-port.jpg', 'A coalition across American life',
             ['The American Anti-Imperialist League organized in Boston in 1898.',
              'Former president Grover Cleveland and diplomat Carl Schurz led it.',
              'Industrialist Andrew Carnegie offered 20 million dollars for Philippine independence.',
              'Labor leader Samuel Gompers stood in the same coalition.',
              'Mark Twain joined its leadership from 1901.'],
             "The American Anti-Imperialist League, organized in Boston in 1898, coordinated the opposition to annexation, and its membership list is the fastest way to show students how wide that opposition ran. Its leaders ranged from former president Grover Cleveland and the diplomat Carl Schurz to the industrialist Andrew Carnegie, who offered 20 million dollars of his own money for Philippine independence, the exact sum the United States had just paid Spain. Labor leader Samuel Gompers stood in the same coalition, and Mark Twain joined its leadership from 1901. Pause on the strangeness of that lineup. A former president, a steel magnate, a union chief, and the most famous writer in the country agreed on almost nothing else in public life. They agreed on this vote, and the League made anti-imperialism a national argument. The next slide separates what they agreed on from why, because the coalition held together on the conclusion while its members reasoned from opposite premises.",
             kick='B · The league against empire')

# ------------------------------------------------------ 10 · THREE REASONS
content_text('One vote, three different reasons',
             ['Some argued from the Declaration of Independence: governments rest on the consent of the governed.',
              'Others feared competition from Filipino workers.',
              'Still others objected to governing people they deemed racially unfit for citizenship.',
              "The October 1899 platform called subjugation 'criminal aggression'."],
             "Teach the disagreement inside the League honestly, because students respect the lesson more when it refuses to tidy the past. Some members argued from the Declaration of Independence: governments rest on the consent of the governed, so ruling the Philippines without Filipino consent was wrong in principle, whatever it paid. Others feared competition from Filipino labor, an economic argument about wages at home. Still others objected to governing people they deemed racially unfit for citizenship, which means part of the anti imperialist coalition opposed empire from racial prejudice, not from respect for Filipino rights. The League's platform of October 1899 called the subjugation of any people criminal aggression, the phrase the guided notes test. Flag the date for students: the platform came eight months after the February Senate vote, so it states the League's settled position during the war, not the argument that nearly beat the treaty.",
             kick='B · The league against empire', size=24)

# ------------------------------------------------- 11 · SECTION C DIVIDER
divider_photo('aguinaldo-port.jpg', 'Section C', 'The Philippine Republic',
              ['Independence was proclaimed at Kawit on June 12, 1898.', 'A republic was inaugurated at Malolos on January 23, 1899.'],
              "The portrait shows Emilio Aguinaldo at about 1898, and students deserve the disclosure the printed documents carry: the surviving scan, published in 1899 in the book War in the Philippines and held through Wikimedia Commons, is small, 209 by 299 pixels, so the portrait prints and projects soft by design. No sharper period portrait was available to use honestly. Aguinaldo was twenty nine years old in the year of this portrait, a revolutionary who had already led one revolt against Spain, accepted exile, and returned to fight again. Everything in this section follows from taking him and his government seriously as political actors rather than as background to an American debate. While Washington argued over the treaty, Filipinos proclaimed independence, wrote a constitution, seated a congress, and inaugurated a republic. The question Section C answers is simple: what exactly did the United States refuse to recognize?",
              title_size=44)

# ------------------------------------------------------ 12 · AGUINALDO
content_photo_s('aguinaldo-port.jpg', 'Aguinaldo and the revolt',
             ['Filipinos had been fighting Spain since 1896.',
              'Aguinaldo returned from exile in May 1898 on an American naval vessel.',
              'The United States encouraged the revolt but never promised independence in writing.',
              'Aguinaldo proclaimed independence at Kawit on June 12, 1898.',
              'Filipino forces held most of Luzon outside Manila.'],
             "Give the chronology carefully, because the moral weight of the section sits inside it. Filipinos had been fighting Spain since 1896, two years before the United States entered the picture. Their leader, Emilio Aguinaldo, in the guided notes definition, is the Filipino revolutionary leader who proclaimed Philippine independence in 1898 and served as president of the Philippine Republic. He returned from exile in May 1898 on an American naval vessel and resumed the revolt with American encouragement. Hold students to the reading's exact qualification: the United States never promised independence in writing. On June 12, 1898, Aguinaldo proclaimed Philippine independence at Kawit, and Filipino forces took control of most of Luzon outside Manila. By the time Spain signed the islands away in Paris that December, the Spain being paid for them no longer controlled most of the largest island. The United States had bought a claim. The Filipinos held the ground.",
             kick='C · The Philippine Republic')

# ------------------------------------------------------ 13 · MALOLOS
content_text('A government of their own',
             ['A congress at Malolos wrote a constitution.',
              'The Philippine Republic was inaugurated on January 23, 1899.',
              'Aguinaldo served as its president.',
              'American officials called the republic an insurrection.',
              'That word claimed an authority Filipinos had never accepted.'],
             "Two weeks before the Senate ratified the treaty, the Philippine Republic already existed in working form. A congress at Malolos wrote a constitution, and on January 23, 1899, the republic was inaugurated with Aguinaldo as president. That sequence answers the expansionist claim from Section A directly. Senators had argued that Filipinos could not govern themselves; at Malolos, Filipinos were governing themselves, with a constitution, a congress, a capital, and an army in the field. American officials treated the republic as an insurrection against American authority. Have students sit with that word. An insurrection is a revolt against a government a people has accepted. Filipinos had never accepted American sovereignty; Spain had sold a title it could not deliver, and the republic's leaders said so in writing. Whether a government can be an insurrection against rulers it never consented to is the constitutional heart of the lesson question, and Aguinaldo's protest on the next section makes the argument in his own position.",
             kick='C · The Philippine Republic', size=24)

# ------------------------------------------------- 14 · SECTION D DIVIDER
divider_text('Section D', 'Benevolent Assimilation and War',
             'A proclamation promising friendship, a warning of force, and a war that ran to 1902.',
             "This section holds the lesson's central tension in a single document and a single war. On December 21, 1898, President McKinley issued the proclamation that named American policy Benevolent Assimilation. It promised friendship and just government. It also ordered military rule over the whole archipelago and warned that resistance would meet the strong arm of authority. Six weeks later the shooting started, two days before the Senate vote. The war that followed lasted, by the official American declaration, until July 4, 1902, and it changed character within its first year, from set battles between armies to a guerrilla struggle across the islands. Methods hardened as the war lengthened, and the costs fell heaviest, by a wide margin, on Filipino civilians. Teach the promise and the war together, in the same breath, because the writing task asks students to judge the distance between them.")

# ------------------------------------------------------ 15 · THE PROCLAMATION
content_text('Benevolent Assimilation',
             ['McKinley issued the proclamation on December 21, 1898.',
              'The United States came, it promised, not as invaders or conquerors, but as friends.',
              'It promised the mild sway of justice and right in place of arbitrary rule.',
              'It ordered military government extended over the whole archipelago.',
              'It warned that resistance would meet the strong arm of authority.'],
             "Read the proclamation the way the exit ticket will: one document, two voices. The first voice is the promise. Control of the islands had been ceded to the United States, McKinley announced, and the United States came not as invaders or conquerors, but as friends. He named the mission Benevolent Assimilation, in the guided notes definition, the name President McKinley gave his Philippine policy in his proclamation of December 21, 1898, claiming that American rule would substitute just government for arbitrary rule. The second voice is the order inside the same proclamation. Military government would extend over the whole archipelago, and resistance would meet the strong arm of authority. Students should hear that both voices are authentic and neither cancels the other. The promise described the intention officials stated. The order described what would happen to any Filipino who acted on the independence proclaimed at Kawit. The next slide shows how the man the proclamation was aimed at actually received it.",
             kick='D · Benevolent assimilation and war', size=24)

# ------------------------------------------------------ 16 · THE EDITED COPY
content_text('How Aguinaldo learned the terms',
             ['General Otis sent Aguinaldo a copy with the sovereignty claims removed.',
              'The unedited text reached Aguinaldo anyway.',
              'Aguinaldo protested on January 5, 1899.',
              'He had never agreed to American sovereignty.',
              'A sentry fired on February 4, 1899, and open war began.'],
             "This episode is small, documented, and worth teaching slowly. General Elwell Otis, commanding in Manila, sent Aguinaldo a copy of the proclamation with the claims of sovereignty removed, apparently hoping the softened text would keep the peace while Washington decided. The unedited text reached Aguinaldo anyway. On January 5, 1899, he protested in writing: he had never agreed to American sovereignty, and he had returned from exile to fight for independence, the cause he had been fighting since 1896. Students should weigh what the editing itself reveals. The commanding general judged that the proclamation's real terms, read plainly, would provoke the resistance it claimed to welcome as friendship. On February 4, 1899, two days before the Senate vote, an American sentry shot at Filipino soldiers near Manila, and open war began. Neither capital voted for that first shot. Both governments had spent two months making it likely.",
             kick='D · Benevolent assimilation and war', size=24)

# ------------------------------------------------------ 17 · GUERRILLA WAR
content_text('War, then guerrilla war',
             ['American forces won the early set battles and took Malolos, the capital.',
              'The United States sent about 126,000 soldiers during the war.',
              'Aguinaldo disbanded his regular army in November 1899.',
              'His forces turned to guerrilla warfare: small bands that ambush, raid, and disperse.',
              'Aguinaldo was captured in March 1901, and fighting ran to July 4, 1902.'],
             "The war had two phases, and the second explains the methods on the next slide. American forces won the early set battles and took the capital, Malolos. In November 1899 Aguinaldo disbanded his regular army and ordered guerrilla warfare, in the guided notes definition, fighting by small, mobile bands that ambush, raid, and disperse instead of meeting an enemy army in open battle. The Philippine-American War, again in the definition students copy, is the war fought from 1899 to 1902 between the United States and the Philippine Republic over American annexation of the Philippines. The United States sent about 126,000 soldiers to the islands during the war. Troops captured Aguinaldo in March 1901; he swore allegiance to the United States and called for peace. Resistance continued anyway, until President Theodore Roosevelt declared the war over on July 4, 1902. Name the date's symbolism without leaning on it: independence declared ended, on Independence Day, by the occupying power.",
             kick='D · Benevolent assimilation and war', size=24)

# ------------------------------------------------------ 18 · METHODS AND COSTS
content_photo_s('prisoners-port.jpg', 'Methods and costs',
             ['American troops burned villages and crops.',
              'Reconcentration camps in Batangas filled, and disease spread quickly.',
              'Interrogators used the water cure on prisoners.',
              'Filipino fighters killed 48 Americans at Balangiga in September 1901.',
              'General Jacob Smith ordered Samar made a howling wilderness and was court-martialed.'],
             "Do not rush this slide, and do not soften its contents. Guerrilla war blurred the line between soldier and civilian, and American methods hardened in response. Troops burned villages and crops. In Batangas, much of the population was forced into guarded reconcentration camps, where disease spread quickly among crowded people short of food and clean water. Interrogators used the water cure, forcing water into a prisoner until he talked. After Filipino fighters killed 48 Americans at Balangiga, on Samar, in September 1901, General Jacob Smith ordered his men to kill and burn and make Samar a howling wilderness. Smith was court-martialed and retired, which students should note in both directions: the order was given by a general, and the army did punish it, after it was given. Next slide puts the human total on the screen. Insist, there and everywhere, that the civilian figure is an estimate, because no one counted.",
             kick='D · Benevolent assimilation and war')

# ------------------------------------------------------ 19 · STAT: CIVILIAN DEATHS
stat('200,000', 'estimated Filipino civilian deaths',
     'An estimate, not a count. Some estimates run higher.',
     "Give this number its full weight and its full qualification, in that order. The Office of the Historian gives more than 4,200 American dead and more than 20,000 Filipino combatants dead. For civilians, it gives an estimate of as many as 200,000 Filipino civilian deaths from violence, famine, and disease. That figure is an estimate, not a count, and the reading says so in plain words; some estimates run higher. No authority registered civilian deaths during the war. The total is reconstructed from population records across hundreds of islands over three years, counting people who died in burned villages, in reconcentration camps, and in the epidemics and hunger that followed destroyed crops. Students sometimes discount a number because it is estimated. Reverse that instinct here. The uncertainty exists because the dead were Filipino villagers whom no government office was counting. The estimate is the honest form of the fact, and the writing task expects students to state it as an estimate when they use it.",
     kick='D · Benevolent assimilation and war')

# ------------------------------------------------- 20 · SECTION E DIVIDER
divider_text('Section E', 'Courts and Civil Government',
             'What the new possessions were in law, and who governed them in practice.',
             "The war answered who held the islands by force. This section answers the two questions force could not settle. The first was legal: what were Puerto Rico and the Philippines inside the American constitutional order, places the United States owned but had not made states and did not intend, in the near term, to let go? The Supreme Court took that question in the Insular Cases beginning in 1901, while the war was still being fought. The second question was practical: who would govern day to day, soldiers or civilians, and with what Filipino participation? The answer came in stages, a civil governor in 1901, an organic act in 1902, an elected assembly in 1907, and final authority kept in American hands throughout, with no date set for independence. Hold both answers against the lesson question as you teach. Each is evidence, for opposite sides of it.")

# ------------------------------------------------------ 21 · INSULAR CASES
content_text('The Insular Cases',
             ['The cases began with Downes v. Bidwell in 1901.',
              'The territories were not foreign countries, but they were not fully part of the United States.',
              'Justice White called such territory foreign to the United States in a domestic sense.',
              'The rulings created a new category: the unincorporated territory.',
              'The territory belonged to the United States, and the Constitution applied only in part.'],
             "Define the term from the guided notes first: the Insular Cases are the Supreme Court decisions beginning in 1901 that held the new island territories were not fully part of the United States and that the Constitution did not apply there in full. In the first of them, Downes v. Bidwell in 1901, the Court held that Puerto Rico and the Philippines were not foreign countries, but neither were they fully part of the United States. Justice Edward White, concurring, described such a territory as foreign to the United States in a domestic sense, a phrase students find strange until they see the category it built. The rulings created the unincorporated territory: belonging to the United States, not on the road to statehood, and under the Constitution only in part. Put the consequence plainly. The same flag now flew over two kinds of ground, ground where the Constitution followed in full, and ground where it followed only as far as Congress and the Court allowed.",
             kick='E · Courts and civil government', size=24)

# ------------------------------------------------------ 22 · CIVIL GOVERNMENT
content_text('Civil government',
             ['William Howard Taft became civil governor on July 4, 1901.',
              'His commission built schools, courts, and a civil service, with English as the language of instruction.',
              'The Philippine Organic Act of 1902 confirmed civil government.',
              'An elected Philippine assembly met in 1907.',
              'Final authority stayed American, and no date for independence was set.'],
             "Close the content with the definition in use: civil government is the rule of a territory by civilian officials acting under law, in place of direct military rule. Military rule gave way by stages. On July 4, 1901, William Howard Taft became civil governor, heading a commission building schools, courts, and a civil service, with English as the language of instruction. The Philippine Organic Act of 1902 confirmed civil government and promised an assembly, which met in 1907. Filipinos held local offices and sat in that assembly. Then give the limit its full sentence, because it is the fact the writing task turns on: an American governor general kept final authority, and no date for independence was set. The islands remained a colony, governed in the name of preparing their people for a self government they had proclaimed in 1899. Students now have the whole arc, from the Paris signatures to the 1907 assembly, and the argument is theirs to judge.",
             kick='E · Courts and civil government', size=24)

# ------------------------------------------------------ 23 · AT A GLANCE
content_text('The argument at a glance',
             ['Annex: the islands offered markets, a station on the route to China, and a claimed duty to govern.',
              'Reject: governing without consent violates the Declaration of Independence.',
              'Independence: the Filipinos had already built a republic, with a constitution and a capital.',
              'Underneath all three positions sits one question: whose consent counts?'],
             "Consolidate the three positions before the vocabulary slides, because the guided notes table, the notebook page, and the simulation all organize the lesson this way. The annexation case, at its strongest: the islands offered markets and a station on the route to China, and their rulers claimed a duty to govern people they judged unready, pointing to schools, courts, and the promised assembly as the work beginning. The rejection case, at its strongest: governing a people without its consent violates the Declaration of Independence, and the League named subjugation criminal aggression. The independence case, at its strongest: the Filipinos had already formed a republic with a constitution, an army, and a capital, so the question was never whether they could govern, but whether the United States would let them. Have students fill the Argument at a Glance table now, claim and backing document for each row, while all three cases are in front of them.",
             kick='E · Courts and civil government', size=24)

# ------------------------------------------------------ 24 · VOCAB A
vocab('Words for the war and the opposition',
      [('Philippine-American War', 'the war fought from 1899 to 1902 between the United States and the Philippine Republic over American annexation of the Philippines'),
       ('anti-imperialism', 'opposition to acquiring and ruling overseas colonies, especially on the ground that governing a people without its consent violates republican principles'),
       ('Emilio Aguinaldo', 'the Filipino revolutionary leader who proclaimed Philippine independence in 1898 and served as president of the Philippine Republic')],
      "These definitions match the guided notes word for word, and students should copy them exactly. The Philippine-American War is the war fought from 1899 to 1902 between the United States and the Philippine Republic over American annexation of the Philippines. Note the definition's naming choice: it calls the other belligerent the Philippine Republic, the government inaugurated at Malolos, which is how the Filipino side understood the war. Anti-imperialism is opposition to acquiring and ruling overseas colonies, especially on the ground that governing a people without its consent violates republican principles. That ground was the League's strongest argument, though Section B showed it was never the coalition's only motive. Emilio Aguinaldo is the Filipino revolutionary leader who proclaimed Philippine independence in 1898 and served as president of the Philippine Republic. Students have now met all three terms in use across Sections B, C, and D, before meeting them here as definitions to copy.",
      kick='The vocabulary')

# ------------------------------------------------------ 25 · VOCAB B
vocab('Words for the fighting and the rule that followed',
      [('guerrilla warfare', 'fighting by small, mobile bands that ambush, raid, and disperse instead of meeting an enemy army in open battle'),
       ('Benevolent Assimilation', 'the name President McKinley gave his Philippine policy in his proclamation of December 21, 1898, claiming that American rule would substitute just government for arbitrary rule'),
       ('Insular Cases', 'the Supreme Court decisions beginning in 1901 that held the new island territories were not fully part of the United States and that the Constitution did not apply there in full'),
       ('civil government', 'the rule of a territory by civilian officials acting under law, in place of direct military rule')],
      "Four more terms, again matching the guided notes exactly. Guerrilla warfare is fighting by small, mobile bands that ambush, raid, and disperse instead of meeting an enemy army in open battle; Aguinaldo ordered it in November 1899, and the war's hardest methods followed from it. Benevolent Assimilation is the name President McKinley gave his Philippine policy in his proclamation of December 21, 1898, claiming that American rule would substitute just government for arbitrary rule. The Insular Cases are the Supreme Court decisions beginning in 1901 that held the new island territories were not fully part of the United States and that the Constitution did not apply there in full. Civil government is the rule of a territory by civilian officials acting under law, in place of direct military rule, the system Taft headed from July 4, 1901. Together the four terms trace the lesson's second half: the fighting, the promise that named it, the law that housed it, and the government that outlasted it.",
      kick='The vocabulary', step=1.25)

# ------------------------------------------------------ 26 · TODAY'S WORK
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Argue the Senate question yourself', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Return to the lesson question: did taking the Philippines extend American ideals or contradict them?'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'Annexation Debate Simulation: five roles, five documents, then the vote'),
        ('Notebook', 'The argument chart: three positions, their claims, and the evidence behind each'),
        ('Quick check', 'School Begins: read the Puck cartoon, caricatures included, as evidence'),
        ('Writing', 'Extend or Contradict: argue the lesson question from the documents')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=19, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.8, 11.5, 0.5, 'Exit ticket: the promise and the threat, the one vote margin, and one piece of evidence for each side.',
     size=16, color=POWDER)
notes(s, "Close by handing the argument to the students, in four pieces. The activity is the Annexation Debate Simulation, The Senate Question, 1899: five roles argue from five documents, including a composite anti-imperialist senator whose part is labeled as a composite on the face of the station, then the class votes as the Senate did. The notebook page collects the argument chart they filled today: three positions, their strongest claims, and the document or fact behind each. The quick check, School Begins, asks them to read the Dalrymple cartoon as evidence, naming its racial caricatures rather than looking past them. The writing task, Extend or Contradict, states the lesson question as an argument to be settled from the documents, with the civilian death estimate stated as an estimate wherever it is used. Collect the exit ticket on the way out: McKinley's promise and his threat, why 57 to 27 was a one vote decision, and one piece of evidence for each side of the question.")

dc.save(OUT)
