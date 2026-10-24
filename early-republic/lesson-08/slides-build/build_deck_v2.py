#!/usr/bin/env python3
"""Early Republic Lesson 8 deck, "Manifest Destiny and the War with Mexico,"
built to the approved system: image-led slides, fragments only on screen,
comprehensive speaker notes, full lesson + vocabulary coverage."""
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
    frags(s, items, y=2.12 if kick else 2.0, size=size, gap=11, leading=1.2)
    notes(s, note)
    return s

# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'THE EARLY REPUBLIC AND EXPANSION · LESSON 8', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Manifest Destiny and the War with Mexico', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'What Americans told themselves expansion was, and what the war left unsettled', size=17, color=POWDER)
text(s, 0.9, 7.02, 11.9, 0.4, 'Battle of Palo Alto, lithograph by Bayot after Nebel, 1851. Wikimedia Commons.', size=11, color=POWDER)
notes(s, "The image is the Battle of Palo Alto, fought on May 8, 1846, drawn by Carl Nebel, who accompanied the American army, and lithographed by Adolphe Jean-Baptiste Bayot for the 1851 volume The War between the United States and Mexico Illustrated. Show students the print as evidence before it is anything else: this is how the war was pictured for American readers after the fighting, in a book sold to a public that had followed the campaigns in newspapers. The lesson closes the unit. It begins with a story Americans told themselves in 1845, follows Texas, Oregon, and a war with Mexico, and ends in February 1848 with a treaty that added an immense country and a question no settlement in the unit had answered, whether slavery would enter the new lands.")

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('What did Americans tell themselves expansion was, and what did the war with Mexico leave unsettled?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the United States turn its Constitution into a working government, and what did continental expansion do to the republic that government served?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "The question has two halves and the lesson grades both. The first half is about a story. In 1845 an editor gave expansion a name and a theology, a manifest destiny to overspread a continent allotted by Providence, and that story did real work: it turned annexation into fulfillment, made a war read as defense, and made the continent's Native nations and its Mexican republic hard to see. The second half is about a remainder. The war settled a boundary and transferred a cession, and it settled nothing about slavery in the new country. David Wilmot asked that question in 1846, while the war still ran, and the Senate's refusal to answer it is where this unit ends and the next era of the course begins.")

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'The expansion, in seven stretches', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The lull and the acceleration', 'The 1820 line holds, settlement fills the East'),
        ('B', 'Texas as the first test', 'A republic for nine years, annexed in 1845'),
        ('C', 'The name the expansion took', "O'Sullivan and a destiny allotted by Providence"),
        ('D', 'Oregon divided', 'A claim halved at the 49th parallel, 1846'),
        ('E', 'The war with Mexico', 'American blood on disputed soil, three roads of war'),
        ('F', 'Opposition and the settlement', 'Whigs, abolitionists, and the treaty of 1848'),
        ('G', 'The proviso', 'Wilmot asks what the winnings are for')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A sets the pace, a settlement line holding while population doubles. Section B takes Texas from revolt in 1836 through nine years outside the Union to annexation in 1845. Section C names the story, manifest destiny, and states what the name hid. Section D divides Oregon by treaty. Section E fights the war on three roads. Section F hears the opposition at home and reads the treaty of 1848, including its eighth article. Section G closes on Wilmot's proviso and the question left standing on the table.")

# 4 A DIVIDER
divider_text('Section A', 'The Lull and the Acceleration',
             'The line of 1820 held, while the filling of the East gathered speed.',
             "Begin with the quiet decades, because the speed of the 1840s is unintelligible without them. Through the 1820s the Missouri line held across the Louisiana Purchase lands, and settlement filled the country east of the Mississippi behind it. The population of the republic doubled and doubled again across the first half of the century, and steamboats and canals moved that population and its goods west in growing volume. Every new state entered under a standing agreement about where slavery could go in the lands the union already held. Name the habit this built. Americans came to expect that expansion questions came with a settlement attached, a line or a pairing of states, and that expectation is exactly what the Mexican cession would break in the next decade.")

# 5 A CONTENT
content_text('A line that held, and a country filling behind it',
             ['The 1820 line held through the 1820s.',
              'The population doubled, and doubled again.',
              'Steamboats and canals carried settlement west.',
              'By the 1840s, the argument was about the story.'],
             "Work the fragments as a change of question. In 1820 the argument was whether slavery would enter Missouri, and Congress answered with a line. By the 1840s the lands east of the Mississippi were filling, new country lay beyond them in Texas, in Oregon, and in Mexico's north, and the argument had moved. Few Americans of either party argued about whether more of the continent would be taken. They argued about the story the taking would be told in, whether it was a destiny allotted by Providence or a set of choices made by presidents and Congresses, and about the rules for slavery in whatever country was taken next. Put the two questions on the board in that order, because the lesson answers the story question first and the slavery question last, and the second answer is no answer at all.",
             kick='A · The lull and the acceleration', size=24)

# 6 B DIVIDER
divider_photo('polk-port.jpg', 'Section B', 'Texas as the First Test',
              ['James K. Polk, elected in 1844', 'on a promise of expansion.'],
              "The image is James K. Polk, painted by George Peter Alexander Healy in a portrait dated October 7, 1858, held in the White House Collection. Polk enters the lesson early because he was elected on expansion in 1844, but Section B begins two decades before him. American settlers entered Mexican Texas in the 1820s under conditions Mexico set in its colonization laws, including limits tied to slavery and to Catholic profession, and the settlers increasingly ignored the conditions while slavery spread among them. Texas revolted in 1836 and won independence at San Jacinto. What followed was not immediate annexation but a nine year wait, and the wait is the evidence students should carry out of this section, because it shows the sectional balance, not destiny, setting the timetable.")

# 7 B CONTENT 1
content_text('A revolt, and a republic outside the Union',
             ['Settlers entered Mexican Texas in the 1820s.',
              'The conditions Mexico set were increasingly ignored.',
              'Texas revolted in 1836 and won at San Jacinto that April.',
              'It was a recognized republic, courted by Britain and France.',
              'It was kept out for nine years, because admission meant a slave state.'],
             "Teach the nine years as the section's central fact. The Republic of Texas was recognized by the United States, and Britain and France courted it for trade and for a counterweight to American power on the continent. It stayed outside the Union because every president from Jackson to Tyler could count. A Texas admitted was a slave state admitted, the Senate balance of free and slave states would tilt, and northern opposition in the House and among voters stood ready. Annexation was offered and withdrawn more than once in those years. When students later hear that destiny carried Texas into the Union in 1845, this slide is the correction: destiny waited nine years on arithmetic, and entered only when the method changed from a treaty to a joint resolution.",
             kick='B · Texas as the first test', size=24)

# 8 B CONTENT 2
content_text('1845: annexation by joint resolution',
             ['A treaty needed two thirds of the Senate, and it failed.',
              'A joint resolution needed a simple majority, and it passed.',
              'It came in Tyler’s last days, with Polk elected on expansion.',
              'Mexico never recognized the loss of Texas.'],
             "Work the method, because the method is the history here. The Constitution gives the Senate a two thirds voice in treaties, and a treaty of annexation had failed to reach that count in 1844. In 1845 Congress used a joint resolution instead, a law like any other, needing a simple majority of both houses, and Texas entered on those terms in the final days of John Tyler's presidency, with James K. Polk already elected on an expansion platform. Students should state the contrast without prompting by the end of the hour: the same admission that could not win two thirds of the Senate won a majority of Congress when the instrument changed. Then add the fact the resolution could not change. Mexico had never recognized Texas independence, so annexation took in a boundary dispute along with a state, the dispute between the Nueces and the Rio Grande that Section E fights over.",
             kick='B · Texas as the first test', size=24)

# 9 C DIVIDER
divider_text('Section C', 'The Name the Expansion Took',
             "O'Sullivan, 1845: a continent allotted by Providence.",
             "Section C slows down on a single phrase, because the phrase is the lesson's title idea and the activity's first station. In the summer of 1845 an unsigned editorial in the United States Magazine and Democratic Review, traditionally attributed to its editor John L. O'Sullivan, argued for the annexation of Texas against British and French opposition. In it the writer reached for a larger claim than Texas, a manifest destiny to overspread the continent allotted by Providence for the free development of the nation's yearly multiplying millions. The phrase survived its editorial. Within a few years politicians and newspapers used manifest destiny as the name of the whole expansion, and students meet the words here at their birth, attached to a specific annexation argument in a specific magazine.")

# 10 C CONTENT 1
content_photo_s('palo-port.jpg', 'A gift already given',
             ['Manifest destiny was named in 1845.',
              'The continent was allotted by Providence.',
              'American institutions stood as the proof of the gift.',
              'Expansion was told as fulfillment, not as taking.'],
             "State the claim in the editorial's own structure before criticizing it, so students answer the strongest version. The continent, in this telling, was not a prize to be won but an allotment already made, given by Providence for the free development of a growing American people. American institutions, republican government and free settlement, stood as the evidence that the allotment was deserved. Foreign objection, from Britain and France, could then be told as interference with a gift rather than as a defense of other titles. Hold the Palo Alto print beside the claim and ask what kind of book this argument later filled: a war pictured plate by plate for the same reading public, the story and the pictures reinforcing each other for American buyers.",
             kick='C · The name the expansion took')

# 11 C CONTENT 2
content_text('What the phrase made hard to see',
             ['The continent was inhabited, governed, and claimed.',
              'Native nations held the country the survey lines crossed.',
              'Mexico’s northern provinces were thinly settled and sovereign.',
              'Mexican citizens lived under Mexican law, from Texas to California.'],
             "Now state plainly what the phrase was built to make hard to see, in the reading's own terms, because this correction is half the lesson question. The continent was inhabited, governed, and claimed. Native nations held country across every route the expansion took, and American survey lines crossed that country as if the lines settled the question. To the southwest stood a Mexican republic, independent since 1821, whose northern provinces were thinly settled but sovereign, with Mexican citizens living under Mexican law in towns, missions turned secular, and ranchos from Texas to California. Their claims rested on law, on residence, and on governments of their own. A story about an empty continent allotted by Providence required not seeing any of this, and students should be able to name both holders, Native nations and Mexico, without help.",
             kick='C · The name the expansion took')

# 12 D DIVIDER
divider_text('Section D', 'Oregon, the Expansion That Ended in Division',
             'A claim demanded whole, and settled at the 49th parallel.',
             "Section D is the lesson's built in comparison, and it should be taught as one. The Oregon Country, the Pacific Northwest between California and Russian Alaska, had been jointly occupied by the United States and Britain since 1818, an arrangement renewed rather than settled for nearly thirty years. American settlers reached it overland in growing numbers in the early 1840s, and the Democratic campaign of 1844 demanded the whole country up to the line of 54 degrees 40 minutes, the cry remembered as fifty-four forty or fight. Polk carried that demand into office. What he did with it, while a war opened against Mexico, is the comparison the reading asks students to state: the difference between the two negotiations is part of the lesson, and the next two slides build it.")

# 13 D CONTENT
content_text('Joint occupation, and a slogan',
             ['Oregon was jointly occupied with Britain from 1818.',
              'American settlers arrived overland in the 1840s.',
              'The 1844 cry claimed the whole country to 54 degrees 40 minutes.',
              'The cry was fifty-four forty or fight.'],
             "Work the slogan as a campaign artifact before it becomes diplomacy. Fifty-four forty named a latitude, the southern boundary of Russian Alaska, and claimed the entire Oregon Country for the United States, ending the joint occupation by assertion. It helped elect Polk in 1844 alongside the promise of Texas. Once in office Polk had to govern with the slogan rather than merely run on it. Britain held real power in the Pacific Northwest, a navy, the Hudson's Bay Company posts, and settlers of its own, and a war with Britain over Oregon while Texas stood disputed carried risks no cabinet wanted. Ask students to hold the slogan in mind through the next slide, where the settlement arrives at a line far south of fifty-four forty, and to ask what changed between the cry and the treaty: not the claim, but the opponent.",
             kick='D · Oregon divided', size=24)

# 14 STAT 49
stat('49th', 'parallel, the Oregon settlement line of 1846',
     'Polk accepted half his claim against Britain, by treaty',
     "Let the number carry the comparison, because one latitude explains two policies. In June 1846 the United States and Britain divided the Oregon Country at the 49th parallel, the line that already marked much of the northern boundary farther east, with Vancouver Island left British. Polk, the president elected on fifty-four forty or fight, accepted roughly half of the claim his campaign had demanded whole. He did so by treaty, through the Senate, while American troops stood on the Rio Grande and a war with Mexico was beginning. Teach the pairing without softening it. Against Britain, a power that could fight back at sea and in Canada, the expansion ended in negotiation and division. Against Mexico, divided and far weaker, the same president's expansion proceeded by war. Students who can state that difference have the section.",
     kick='D · Oregon divided')

# 15 E DIVIDER
divider_photo('palo-port.jpg', 'Section E', 'The War with Mexico',
              ['Palo Alto, May 8, 1846: the first', 'pitched battle of the war.'],
              "The image is the Palo Alto lithograph again, now as the record of a battle rather than a title image: May 8, 1846, the first pitched battle of the war, fought north of the Rio Grande in the ground this section is about. Section E begins with an order. Polk directed General Zachary Taylor to move from the Nueces River, where his army had waited, down to the left bank of the Rio Grande, opposite the Mexican town of Matamoros. The ground between the two rivers was claimed by Texas as its boundary inheritance and held by Mexico as its own, and Mexican citizens lived in settlements within it. In April 1846 a Mexican force crossed the river and attacked a party of American dragoons under Captain Seth Thornton. The clash gave Polk his sentence for Congress, and its location gave his opponents theirs.")

# 16 E CONTENT 1
content_text('American blood, and the question of the soil',
             ['Troops were ordered between the Nueces and the Rio Grande.',
              'The Thornton affair came in April 1846.',
              'Polk, on May 11, claimed blood shed on American soil.',
              'Lincoln’s spot resolutions demanded the exact spot.'],
             "Teach the two documents as a claim and a question about one fact. Polk's message of May 11, 1846, which Station 2 prints from the Avalon Project transcription, holds that Mexico refused his envoy, threatened reconquest of Texas, and at last passed the boundary, invaded American territory, and shed American blood upon American soil, so war existed by Mexico's act and Congress need only recognize it. The whole claim rests on the soil: if the ground between the rivers was American, Mexico invaded. In December 1847 Abraham Lincoln, a first term Whig congressman, offered his spot resolutions demanding that the president inform the House whether the particular spot where blood was shed was or was not American soil at that time. The House never adopted them. The question outlived the resolutions, and students will meet both texts in the quick check.",
             kick='E · The war with Mexico', size=24)

# 17 E CONTENT 2
content_text('Three roads of war',
             ['Taylor fought in northern Mexico.',
              'Scott marched from Veracruz to Mexico City.',
              'Kearny and Fremont took New Mexico and California.',
              'The Bear Flag revolt rose in California in 1846.',
              'The United States won against a divided Mexico.'],
             "Map the war on three roads so students hold its geography before its politics. In the north, Zachary Taylor won at Palo Alto and Resaca de la Palma in May 1846, took Monterrey that fall, and held at Buena Vista in February 1847. On the Gulf coast, Winfield Scott landed near Veracruz in March 1847, took the city, and marched inland on the old conqueror's road, winning at Cerro Gordo and entering Mexico City in September. In the far west, Stephen Kearny marched to New Mexico and on to California, where American settlers had raised a Bear Flag in revolt in June 1846 and John C. Fremont's party joined them. Mexico, whose government changed hands repeatedly during the war, lost every campaign. State the cost soberly and move on: the war's dead numbered in the thousands on both sides, most by disease.",
             kick='E · The war with Mexico', size=24)

# 18 E CONTENT 3
content_text('The opposition at home',
             ['Whigs voted the supplies and doubted the cause.',
              'Abolitionists called it a slave power war for new slave states.',
              'Thoreau was jailed over a tax in 1846.',
              'Lincoln pressed the question in the House in December 1847.'],
             "Give the opposition its full weight, because a war opposed at home is a different fact from a war merely won abroad. The Whig Party, Polk's opposition, voted the men and money the army needed while doubting the cause in speech after speech, an uncomfortable position its members defended as supporting soldiers while contesting a president. Abolitionists named the war a slave power war, fought, in their telling, to win new territory in which slavery could expand, a charge the Wilmot Proviso turned into a parliamentary fight in Section G. Henry David Thoreau spent a night in a Massachusetts jail in July 1846 for refusing a poll tax he tied to the war and to slavery, a refusal he later wrote up in the essay Americans now read as Civil Disobedience. Opposition here was print, votes, and one man's tax bill: the republic argued with itself while its armies advanced.",
             kick='E · The war with Mexico', size=24)

# 19 F DIVIDER
divider_photo('scott-port.jpg', 'Section F', 'Opposition and the Settlement of 1848',
              ["Scott's entrance into Mexico City,", 'September 1847, printed in 1851.'],
              "The image is General Scott's entrance into Mexico City in September 1847, from the same Nebel and Bayot volume as the Palo Alto print. The occupation of the capital is the military fact behind the treaty that follows: Mexico negotiated with an American army in its capital and an American diplomat, Nicholas Trist, sent to make peace. Section F reads the settlement the war produced, the Treaty of Guadalupe Hidalgo of February 2, 1848, and it reads the treaty whole, including the article students most often skip. The eighth article spoke to the Mexican citizens who woke up inside the United States when the boundary moved, and what it promised them belongs in any honest account of what the settlement settled.")

# 20 F CONTENT
content_text('The Treaty of Guadalupe Hidalgo',
             ['It was signed on February 2, 1848.',
              'The Rio Grande was confirmed as the Texas boundary.',
              'California, New Mexico, and the country between were ceded.',
              'The United States paid fifteen million dollars and assumed American claims.'],
             "Work the terms as a list students must reproduce, because the unit test draws on this treaty by name. The treaty confirmed the Rio Grande as the boundary of Texas, settling by cession the dispute the war had opened between the Nueces and the Rio Grande. Mexico ceded California, New Mexico, and the country between them, the lands that became the American Southwest and more. The United States paid fifteen million dollars and assumed the claims of American citizens against Mexico, a form that let the settlement be told as a purchase as well as a conquest. The Senate ratified with amendments, Mexico ratified, and the treaty reached Washington nearly unopposed, the reading notes, because opposing the treaty meant opposing the peace. Some five hundred thousand square miles changed hands, as the cession is usually estimated.",
             kick='F · The settlement of 1848', size=24)

# 21 STAT 500000
stat('500,000', 'square miles in the Mexican cession, by the usual estimate',
     'Added by one treaty signature, February 2, 1848',
     "Pause on the scale, and on the word estimate, because precision here is a habit the unit has practiced since the Louisiana Purchase. The Mexican cession is usually reckoned at about five hundred thousand square miles, not counting Texas, whose annexation three years earlier had already added its own vast claim. Together with Texas and the Oregon settlement, the acquisitions of Polk's single term carried the United States to the Pacific across the whole Southwest. Ask students to set the number beside the story from Section C. A continent allotted by Providence arrived, on paper, in a treaty negotiated after an occupation, signed by commissioners of a defeated republic, and paid for in dollars and assumed claims. Both sentences are true. The lesson asks which one describes the event and which one disguises it, and the writing task collects their verdicts.",
     kick='F · The settlement of 1848')

# 22 F CONTENT 2
content_photo_s('scott-port.jpg', 'Article VIII: the people the boundary moved over',
             ['Mexican citizens in the ceded lands could choose.',
              'They could keep Mexican citizenship or become citizens of the United States.',
              'The election came within one year, and silence counted as choosing.',
              'Their property was to be inviolably respected.'],
             "Teach the eighth article slowly, from the treaty text Station 5 prints out of the audited bank record. Mexicans established in the ceded territories could stay where they lived or remove to Mexico, keeping their property or selling it and taking the proceeds, without tax or charge on that account. Those who stayed could retain Mexican citizenship or acquire citizenship of the United States, but they had to make their election within one year of the exchange of ratifications, and anyone still there after the year, without a declaration, was considered to have elected American citizenship. Property of Mexicans, present or absent, was to be inviolably respected, with guarantees equally ample as for citizens of the United States. Note what the article concedes by existing: the continent of Section C was somebody's home, in law, on the treaty's own page.",
             kick='F · The settlement of 1848')

# 23 G DIVIDER
divider_text('Section G', 'The Proviso and the Question Left Open',
             'Wilmot, 1846: no slavery in any territory taken from Mexico.',
             "Section G returns to August 1846, while the war still ran, because the question that closes the unit was asked at the war's beginning, not at its end. President Polk asked Congress for two million dollars to negotiate a peace and, it was understood, to pay for ceded territory. Representative David Wilmot of Pennsylvania, a Democrat of the president's own party, rose with an amendment, modeled on the Northwest Ordinance of 1787, that attached a condition to any acquisition: neither slavery nor involuntary servitude shall ever exist in any part of the territory taken from Mexico, except as punishment for a crime. The amendment was one sentence. Its career, passed by one house and blocked by the other for years, is the ground on which this unit ends.")

# 24 G CONTENT 1
content_text("The Wilmot Proviso's career",
             ['It was offered on August 8, 1846, while the war still ran.',
              'It barred slavery in any territory taken from Mexico.',
              'It passed the House again and again, by section.',
              'It died in the Senate every time.'],
             "Work the career as a map of the country that was winning the war. The House of Representatives, apportioned by population and therefore held by the more populous free states, passed the proviso repeatedly, and the votes divided by section more than by party, northern Democrats joining Whigs against southern members of both parties. The Senate, where free and slave states stood equal, blocked it every time. So the proviso never became law, and students should state all three facts together: what it would have done, where it passed, and where it died. Wilmot himself insisted he held no extreme views on slavery where it existed; his object was the new territory. That narrowness is the point to teach: even a bar limited to lands not yet taken, offered by a loyal Democrat, could not pass the Senate of the republic that was taking them.",
             kick='G · The proviso', size=24)

# 25 G CONTENT 2
content_text('The question left standing',
             ['The Missouri line had answered for the Louisiana lands.',
              'No line answered for the Mexican cession.',
              'The republic had doubled again, and its government had proved workable.',
              'Slavery in the new country stood unanswered.'],
             "Close the lesson by holding the two settlements of the unit's last decade side by side. For the Louisiana Purchase lands, the Missouri Compromise of 1820 had drawn its line at 36 degrees 30 minutes, and the line held for a generation. For the Mexican cession no line was drawn, because the proviso that would have barred slavery outright died in the Senate and no substitute commanded both houses. The unit closes where the treaty left it. In one lifetime the republic had doubled and doubled again, its Constitution had been turned into a working government, its doctrines had been declared, and its armies had won on three roads. The question every settlement since 1787 had deferred, whether slavery would follow the flag into new country, stood alone on the table of the enlarged house, awaiting the units that follow.",
             kick='G · The proviso', size=24)

# 26 VOCAB A
vocab('Words for the expansion',
      [('Manifest Destiny', 'a destiny to expand across the continent, named in 1845'),
       ('annexation', 'formal addition of territory, as Texas in 1845'),
       ('Republic of Texas', 'independent from 1836, outside the Union nine years'),
       ('Oregon Country', 'jointly occupied, divided at the 49th parallel in 1846')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. Manifest Destiny: the name given in 1845 to the belief that the United States was destined, by providence and by the superiority of its institutions, to expand across the continent to the Pacific, a belief its holders used to justify annexation and war. annexation: the formal addition of territory to a country, the method by which Texas joined the United States in 1845 by joint resolution of Congress after a treaty of annexation had failed in the Senate. Republic of Texas: the independent nation Texans declared in 1836 after revolting against Mexico, recognized by the United States but kept outside the Union for nine years because its admission as a slave state threatened the sectional balance. Oregon Country: the Pacific Northwest territory jointly occupied by the United States and Britain from 1818, claimed by American expansionists to the line of 54 degrees 40 minutes and divided at the 49th parallel by treaty in 1846.")

# 27 VOCAB B
vocab('Words for the war and the settlement',
      [('Mexican-American War', '1846 to 1848, ended by the treaty of 1848'),
       ('Wilmot Proviso', 'a bar on slavery in territory taken from Mexico'),
       ('Treaty of Guadalupe Hidalgo', 'February 2, 1848, the Rio Grande and the cession')],
      "Three more terms, again matching the guided notes exactly. Mexican-American War: the war of 1846 to 1848 between the United States and Mexico, begun over the Texas boundary after American annexation and ended by the Treaty of Guadalupe Hidalgo with Mexico ceding half its territory. Wilmot Proviso: the amendment proposed by Representative David Wilmot in 1846, passed repeatedly by the House and blocked in the Senate, that would have barred slavery in any territory taken from Mexico, forcing the slavery question onto the nation's table three years before the gold rush. Treaty of Guadalupe Hidalgo: the treaty of February 2, 1848, that ended the Mexican-American War, confirmed the Rio Grande as Texas's boundary, and transferred California, New Mexico, and the country between to the United States for fifteen million dollars. Keep the chain in view as the terms accumulate: a belief named, a republic annexed, a country divided, a war fought, a question asked, and a treaty that answered everything except that question.")

# 28 SYNTHESIS
s = slide(NAVY)
kicker(s, 'The expansion at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Named, chosen, fought, left open', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Named', "O'Sullivan's phrase, 1845", 'A continent allotted by Providence'),
        ('Chosen', 'Texas by joint resolution, 1845', 'A majority doing what a treaty could not'),
        ('Divided', 'Oregon at the 49th parallel, 1846', 'Half a claim, by treaty with Britain'),
        ('Fought', 'War with Mexico, 1846 to 1848', 'Three roads, and opposition at home'),
        ('Left open', 'The proviso unpassed, 1848', 'Slavery in the cession, unanswered')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, The Expansion at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The five rows compress the argument of the hour and of the unit's closing movement. Named: an editor's phrase of 1845 told the expansion as a destiny allotted by Providence. Chosen: Texas entered in 1845 because Congress changed the instrument, a joint resolution for a failed treaty. Divided: Oregon was split at the 49th parallel by negotiation with a strong power. Fought: Mexico's north was taken by a war that a congressman questioned and a proviso tried to condition. Left open: the treaty of February 1848 settled boundary, cession, and citizenship choices, and left slavery in the new country standing unanswered for the next units of this course.")

# 29 EXIT
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Work the expansion file', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Did Manifest Destiny describe what the United States did in the 1840s, or disguise it? Work the five records in order, then judge the story against the record.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Expansion File: the editorial, the war message, the spot resolutions, the proviso, and the treaty'),
        ('Notebook', 'Notebook page: what happened, the story told about it, and what each record left unsettled'),
        ('Quick check', 'Blood on Which Soil: Polk against Lincoln on one spot of ground'),
        ('Writing', 'Describe or Disguise: a verdict weighed from at least three bank documents')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: annexation stated, the spot question stated, and the lesson question answered with the proviso as evidence.',
     size=15, color=POWDER)
notes(s, "Close by handing the lesson to the work. The activity, The Expansion File, runs five stations: the annexation editorial of 1845 from the audited bank record, Polk's war message of May 11, 1846 from the Avalon Project transcription, Lincoln's spot resolutions from the Papers of Abraham Lincoln transcription, the Wilmot Proviso from the Congressional Globe printing, and the Treaty of Guadalupe Hidalgo from the audited bank record, ending in a table of versions told and a defended verdict on whether destiny described or disguised the expansion. The notebook page holds what happened, the story told, and what each record left unsettled. The quick check, Blood on Which Soil, tests Polk against Lincoln on one spot of ground. The writing task requires a verdict from at least three bank documents and an answer to the strongest claim of the other side. The exit ticket has three parts, as printed at the end of the guided notes.")

dc.save(OUT)

# notes audit
from pptx import Presentation
prs2 = Presentation(OUT)
counts = []
for i, sl in enumerate(prs2.slides, 1):
    t = sl.notes_slide.notes_text_frame.text if sl.has_notes_slide else ""
    counts.append(len(t.split()))
print("slides:", len(counts), "notes min:", min(counts), "max:", max(counts), "total:", sum(counts))
print(counts)
