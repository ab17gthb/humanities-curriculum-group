#!/usr/bin/env python3
"""Lesson 7 deck, "Native Americans and the Closing Frontier," built to the
approved pilot system: image-led slides, fragments only on screen,
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

# ---------------------------------------------------------------- 1 · TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'GILDED AGE · LESSON 7', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Native Americans and the Closing Frontier', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'How land was taken, cultures were attacked, and Native nations endured', size=17, color=POWDER)
notes(s, "The photograph is a pile of American bison skulls at a Detroit works, about 1892, waiting to be ground for fertilizer. Keep it on screen while you frame the lesson. Every skull was once part of the food supply of the Plains peoples, and the pile is industrial in scale: the slaughter of the buffalo was a business, and its effect on Native independence was understood at the time. This lesson follows what happened to Native nations after the Civil War as the United States pushed west. Treaties were broken, wars were fought and lost, and then the government turned from war to a policy called assimilation, meant to end Native cultures as distinct ways of life. Students should leave able to explain that policy, count its costs in land and lives, and name what Native peoples resisted and preserved.")

# ------------------------------------------------- 2 · LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('Why did the United States pursue assimilation, and what did Native peoples lose, resist, and preserve?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did industrial growth transform American life, and who gained, who paid, and who resisted?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Read the lesson question aloud and keep it visible. It has two halves, and the lesson answers both. Why did the United States pursue assimilation? Because officials and many white reformers concluded that Native peoples could survive only by giving up tribal government, communal land, and their own languages, and becoming farmers, Christians, and English speakers. What did Native peoples lose, resist, and preserve? The losses are countable: land, food, children taken to distant schools, and lives. The resistance and the preservation are just as real, and the last section of the lesson belongs to them. Under the unit question, this lesson is the clearest case in the unit of who paid. Industrial growth wanted western land, minerals, and railroad routes, and Native nations held legal title to much of that land. The gain and the payment were connected, and students should be able to draw that connection by the exit ticket.")

# --------------------------------------------------- 3 · THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.3, 11.5, 1.0, 'War, then a policy', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.42)
rows = [('A', 'Treaties and War', 'treaty promises broken, and armed resistance ends'),
        ('B', 'Reservations and the Buffalo', 'confined on reservations, the buffalo destroyed'),
        ('C', 'Assimilation and Boarding Schools', 'a policy to end Native cultures, carried out on children'),
        ('D', 'The Dawes Act', 'allotment divides the land, and surplus land is sold'),
        ('E', 'The Ghost Dance and Wounded Knee', 'a movement of renewal, answered with troops'),
        ('F', 'Resistance and Survival', 'what was lost, and what Native peoples preserved')]
yy = 2.82
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.7, n, size=26, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.03, 4.3, 0.7, t, size=19, color=CREAM, bold=True)
    text(s, 6.05, yy + 0.08, 6.35, 0.7, d, size=17, color=POWDER)
    yy += 0.72
notes(s, "This is the map of the lesson, and it follows the guided notes section by section. Sections A and B cover the taking: treaties broken when settlers and miners wanted the land, wars that ended in surrender, confinement on reservations, and the destruction of the buffalo that made independent life on the Plains nearly impossible. Sections C and D cover the policy that replaced war: assimilation, carried out on children in boarding schools and on land through the Dawes Act. Section E covers the Ghost Dance, a religious movement of renewal, and its end at Wounded Knee. Section F closes with resistance and survival, because the story does not end in 1890. Tell students the guided notes, the activity, and the exit ticket all follow this same order, and that the numbers in sections B and D, the buffalo count and the acreage count, are the figures the test will ask about.")

# ------------------------------------------------- 4 · SECTION A DIVIDER
divider_photo('chief-joseph-port.jpg', 'Section A', 'Treaties and War',
              ['Treaty promises, and the wars', 'that followed when they broke'],
              "The portrait is Chief Joseph of the Nez Perce, photographed by Edward S. Curtis. Say the date plainly: this portrait was made in 1903, when Chief Joseph was an older man, more than twenty five years after the events of this section. It is not a picture of him as he looked in 1877, and students should not treat it as one. He is here because the reading names him: in 1877 the Nez Perce, led in part by Chief Joseph, fled toward Canada rather than leave their homeland in Oregon. Set the section's frame before the details. After the Civil War, the United States pushed west with soldiers, railroads, miners, and settlers. Native nations held legal title to much of that land under treaties the federal government had signed. The pattern of this section is what happened to those treaties when the land became valuable.",
              title_size=54)

# ------------------------------------------------------ 5 · TREATIES BROKEN
content_text('Treaties broken, land taken',
             ['Native nations held legal title under signed treaties',
              'The government broke its agreements again and again',
              '1868: the Treaty of Fort Laramie guarantees the Black Hills to the Lakota',
              'Gold is found, the government offers to buy, then seizes the hills in 1877'],
             "Work through the Black Hills case slowly, because reading question one and three guided notes blanks turn on it. The Treaty of Fort Laramie in 1868 guaranteed the Black Hills to the Lakota. That word, guaranteed, matters: the hills were not a gift the government could take back, but Lakota land confirmed by treaty. When gold was found there, the government first tried to buy the hills. The Lakota refused, as was their right. In 1877 the government seized them anyway. Ask students what a treaty is worth if one side may break it whenever the land turns out to be valuable, and let the silence do some work. Then widen the point. The Black Hills were one case of a general pattern across the West: agreements held until settlers or miners wanted the land badly enough, and then they did not. Native resistance to that pattern is the next slide.",
             kick='A · Treaties and War')

# ------------------------------------------------------ 6 · RESISTANCE AND WAR
content_text('Resistance, and the end of the wars',
             ['1876: the Lakota and Cheyenne defeat Custer at the Little Bighorn',
              'The victory does not hold: winter campaigns, hunger, surrender within a year',
              '1877: the Nez Perce flee toward Canada, captured about 40 miles from the border',
              'Apache resistance in the Southwest lasts until 1886'],
             "Give each resistance its due before explaining why it ended. At the Little Bighorn in 1876, the Lakota and their Cheyenne allies defeated George Custer outright. It was a real victory, and it changed nothing structural: the army campaigned through the winter, food ran short, and most Lakota bands surrendered within a year. In 1877 the Nez Perce chose flight over removal, traveled more than 1,000 miles, and were captured in Montana about 40 miles from Canada and safety. In the Southwest, Apache leaders including Geronimo resisted removal until 1886. The reading is careful about why large scale armed resistance ended by the late 1880s: not because Native peoples accepted the outcome, but because soldiers, supplies, and hunger made further war impossible. Students should repeat that distinction. Defeat by exhaustion is not consent, and the rest of this lesson is unintelligible if the class confuses the two.",
             kick='A · Treaties and War')

# ------------------------------------------------- 7 · SECTION B DIVIDER
divider_photo('bison-port.jpg', 'Section B', 'Reservations and the Buffalo',
              ['Confined to reservations,', 'and cut off from the buffalo'],
              "The photograph is the bison skull pile from the title slide, seen closer: one man stands on top of the pile and another at its base, and both are dwarfed by it. Two systems did the work of this section, and students often merge them, so separate them now. The reservation system was federal policy: it confined Native nations to defined areas under federal supervision and opened most of the West to settlement. The destruction of the buffalo was a commercial slaughter that the army welcomed, and it removed the food supply that could have let Plains peoples stay independent of that system. Policy confined people to a place. The slaughter removed their reason and their means to leave it. By the end of the section, students should be able to explain each half on its own and then explain how the two halves worked together.",
              title_size=40)

# ------------------------------------------------------ 8 · RESERVATION SYSTEM
content_text('Confined: the reservation system',
             ['Reservations: a fraction of a former homeland',
              'Often the land settlers wanted least',
              'Federal agents control food rations and police movement',
              'Families pressed to farm where farming is difficult'],
             "Define the system by its controls, because the guided notes test them. Under the reservation system, federal policy confined Native nations to defined areas of land under federal supervision. Reservations were usually a fraction of a nation's former homeland, and often the land settlers wanted least. Inside them, federal agents controlled food rations, policed movement, and pressed families to farm where farming was difficult. Note the dependence built into that arrangement. A nation that once fed itself now received food from an agent, and rations could be cut, as they were at Pine Ridge in 1890, with consequences this lesson reaches in section E. The system also served the government directly: it let Washington open most of the West to settlement while keeping Native peoples in fixed places under federal control. Confinement, dependence, and control are the three words students should carry out of this slide.",
             kick='B · Reservations and the Buffalo')

# ------------------------------------------------------ 9 · BUFFALO DESTROYED
content_text('A way of life destroyed in about fifteen years',
             ['Plains peoples depend on the buffalo: food, clothing, shelter, tools',
              'Early 1870s: tens of millions still roam the Plains',
              'Commercial hunters kill by the millions, hides shipped east by rail',
              'By the mid 1880s: only a few hundred wild buffalo remain'],
             "Start with dependence, because students underestimate it. For Plains peoples the buffalo were food, clothing, shelter, and tools at once, the base of an economy and a way of life built over centuries. Then run the numbers in order. In the early 1870s, tens of millions still roamed the Plains. Commercial hunters, shipping hides east by railroad, killed them by the millions. By the mid 1880s only a few hundred wild buffalo remained. A food source and a way of life had been destroyed in about fifteen years. Add the army's part plainly: officers welcomed the effect, because a people without food cannot stay independent for long. That sentence connects this slide to the last one. The reservation system worked far more easily once hunger left Plains nations no alternative to federal rations. Reading question two asks exactly this, so make sure students can answer it in their own words.",
             kick='B · Reservations and the Buffalo')

# ------------------------------------------------- 10 · SECTION C DIVIDER
divider_photo('carlisle-port.jpg', 'Section C', 'Assimilation and Boarding Schools',
              ['The plan to end Native cultures,', 'carried out on children'],
              "The photograph shows students in a classroom at the Carlisle Indian Industrial School in 1901, photographed by Frances Benjamin Johnston. Name what kind of image it is: a posed federal publicity photograph, made to show the public that the school was working. Students will read it that way again at Station 2 of the activity, set against a student's own account of the same system. Date it honestly as well: Carlisle opened in 1879, so this classroom shows the system more than twenty years in, not its first days. The section turns from war to policy. As the wars ended, officials and white reformers pursued assimilation, and its main instrument for children was the boarding school. Keep one question in front of the class through both slides: what did the policy's supporters say they were doing, and what did the policy actually do?",
              title_size=40)

# ------------------------------------------------------ 11 · ASSIMILATION
content_text('Assimilation: help, as its supporters told it',
             ['Supporters call themselves friends of Native peoples',
              'Many had documented real abuses',
              'The remedy: end Native cultures as distinct ways of life',
              'Survive as farmers, Christians, and English speakers',
              'Tribal governments and communal landholding to end'],
             "Present the supporters fairly before judging them, because the writing task grades students on exactly that fairness. Many reformers who backed assimilation described themselves as friends of Native peoples, and many had documented real abuses by agents and settlers. Their concern was not invented. Their remedy, however, was to end Native cultures as distinct ways of life. Native people would survive, in this plan, by becoming farmers, Christians, and English speakers, and tribal governments and communal landholding would end. So the goal itself, not only the methods, is what students must weigh. A policy can oppose theft and violence and still aim at the disappearance of peoples as peoples. Hold that thought for the next two sections: the boarding schools pursued this goal with children, and the Dawes Act pursued it with land. The exit ticket asks students to state the goal and one real effect side by side.",
             kick='C · Assimilation and Boarding Schools', size=24)

# ------------------------------------------------------ 12 · BOARDING SCHOOLS
s = slide(CREAM)
photo_right(s, 'torlino-port.jpg')
kicker(s, 'C · Assimilation and Boarding Schools', color=RUST)
text(s, 0.9, 0.95, 6.9, 1.2, 'Boarding schools: Carlisle and the children', size=31, color=NAVY, font='Georgia', leading=1.05)
frags(s, ['Carlisle opens in 1879, the model school',
          'Children removed hundreds of miles from home',
          'Hair cut, Native languages punished',
          'Some children die of disease far from home',
          'Some graduates later defend their nations in court and in print'],
      y=2.15, size=23, gap=13)
notes(s, "The paired portraits are Tom Torlino, a Navajo student at Carlisle, photographed by the school's photographer, John N. Choate: on top, his arrival portrait from 1882, and below, his portrait after about three years at the school, in 1885. The original pair stood side by side; the slide stacks them so both fit without distortion, and the full pair is in the quick check. The school made pairs like this as advertising, so read them as a claim, not a neutral record. Then teach the system behind the claim. Beginning with Carlisle in 1879, the government and churches ran schools that removed children from their families to suppress Native languages and cultures. Children had their hair cut and were punished for speaking their own languages. Some died of disease far from home. Others later used their English and literacy to defend their nations. Both facts belong in the record.")

# ------------------------------------------------- 13 · SECTION D DIVIDER
divider_photo('indian-land-port.jpg', 'Section D', 'The Dawes Act',
              ['Allotment divides the land,', 'and the surplus is sold'],
              "The image is a complete United States government poster from 1911, headed Indian Land for Sale. Date it plainly: it comes from inside the allotment era, twenty four years after the Dawes Act, not from 1887 itself. Read a little of it aloud. The Department of the Interior reports selling allotted Indian land across the West in 1910, state by state and price by price, and estimates that 350,000 acres will be offered for sale in 1911. This is the surplus land system of the next slide, advertised by the government itself as a benefit to buyers. The man pictured at the center is not named on the poster, and we will not name him either. Keep the poster in mind during the section: whatever supporters said allotment would teach, this is what the policy produced in practice, a standing public sale of Native land.",
              title_size=54)

# ------------------------------------------------------ 14 · HOW ALLOTMENT WORKED
content_text('How the Dawes Act worked',
             ['1887: the Dawes Act divides reservation land',
              'Individual allotments to single families or adults',
              'Remaining tribal land declared surplus',
              'Surplus land sold to non-Native buyers',
              'What remains is split into scattered parcels with many heirs'],
             "Walk the mechanism step by step, because the exit ticket asks for it in two sentences. The Dawes Act of 1887 divided reservation land into individual allotments, parcels assigned to single families or adults. Land left over after allotment was declared surplus, a word students should hear in quotation marks in their heads, since the land was surplus only because the act said so. The government then sold that surplus land to non-Native buyers. Supporters argued that private property would teach farming and independence. In practice, allotment broke up the land base that made Native self government possible, and it divided what remained into scattered parcels with many heirs, hard to use and easy to lose. Ask the class the activity's question early: why would dividing tribal land weaken a nation even if no land had been sold at all? The acreage count on the next slide shows how much land was, in fact, sold and lost.",
             kick='D · The Dawes Act')

# ------------------------------------------------------ 15 · THE LAND COUNT
stat('90 MILLION', 'acres of Native land passed out of Native hands by 1934',
     'Native nations held about 138 million acres in 1887, the year the Dawes Act passed. The losses came through surplus sales, individual sales, fraud, and tax loss.',
     "Let the number sit. In 1887, when the Dawes Act passed, Native nations held about 138 million acres. By 1934, when allotment ended, about 90 million of those acres had passed out of Native hands. That is roughly two of every three acres, gone in under fifty years, through surplus sales, individual sales, fraud, and tax loss. Connect the figure back to the promise from the last slide. Allotment was announced as a path to independence: give each family private property and farming would follow. The land record shows the opposite movement, a transfer of land from Native nations to non-Native buyers on a continental scale. Reading question three and the writing task both require this figure with its dates, so students should have 138 million in 1887 and 90 million lost by 1934 in their notes verbatim before you move on.",
     kick='D · The Dawes Act')

# ------------------------------------------------- 16 · SECTION E DIVIDER
divider_photo('ghost-dance-port.jpg', 'Section E', 'The Ghost Dance and Wounded Knee',
              ['A promise of renewal,', 'answered with troops'],
              "The image shows Oglala Lakota dancers at Pine Ridge Agency, and students must know what kind of image it is: an artist's illustration by Frederic Remington, published in Harper's Weekly in 1890 for eastern readers, not a photograph. The lesson activity asks students to weigh that distinction, because an illustration shows how the Ghost Dance was pictured for the white public, which is part of why officials feared it. There is no photograph of the Wounded Knee dead anywhere in this lesson, by design: the killing is taught through the record, not through images of bodies. The section has two movements. First, a religious movement that promised renewal to peoples who had lost land, food, and children. Second, the federal response to that movement, which ended on December 29, 1890, at Wounded Knee Creek. Teach both movements in that order.",
              title_size=40)

# ------------------------------------------------------ 17 · THE GHOST DANCE
content_text('The Ghost Dance: a promise of renewal',
             ['1889: Wovoka, a Paiute prophet, begins teaching the Ghost Dance',
              'The promise: the world restored, the buffalo and the dead return',
              'The teaching spreads across western reservations, 1889 and 1890',
              'Where rations are cut and land taken, followers gather'],
             "Introduce Wovoka accurately: a Paiute prophet who in 1889 began teaching the Ghost Dance, a religious movement that promised renewal. Dancers believed the ceremony would restore the world, bring back the buffalo and the dead, and end suffering. Nothing in the teaching called for war, and students should note that the reading describes a ceremony, not an uprising. Then explain the spread with the lesson's own logic. The teaching moved across western reservations in 1889 and 1890 and found many followers where rations had been cut and land taken. At Pine Ridge the losses named in this lesson, the Black Hills, the buffalo, the children at distant schools, were all recent and personal. A promise to restore exactly what had been lost answered exactly what people there had suffered. That is why the dance grew, and it is the fact federal agents either missed or refused to credit, with results on the next slide.",
             kick='E · The Ghost Dance and Wounded Knee')

# ------------------------------------------------------ 18 · WOUNDED KNEE
content_text('Wounded Knee, December 29, 1890',
             ['Agents at Pine Ridge fear the dance and call for troops',
              'Military police kill Sitting Bull during an arrest attempt',
              'Big Foot\u2019s band is surrounded and ordered to give up its weapons',
              'A shot is fired, and the soldiers open fire',
              'About 250 to 300 Lakota men, women, and children are killed'],
             "Slow down for this slide and keep the sequence exact. Federal agents at Pine Ridge feared the Ghost Dance and called for troops. In December 1890, military police killed the Lakota leader Sitting Bull during an arrest attempt. Two weeks later, on December 29, 1890, soldiers of the Seventh Cavalry surrounded a band of Lakota led by Big Foot at Wounded Knee Creek and ordered them to surrender their weapons. A shot was fired, and the soldiers opened fire. About 250 to 300 Lakota men, women, and children were killed. Use the reading's final sentence as the class's verdict and write it where students can copy it: for the Lakota, Wounded Knee was a massacre of people who had already surrendered and were under guard. Do not rush past the silence after this slide. The next section exists because Lakota families carried this memory and their language through everything that followed.",
             kick='E · The Ghost Dance and Wounded Knee', size=24)

# ------------------------------------------------- 19 · SECTION F DIVIDER
divider_photo('zitkala-port.jpg', 'Section F', 'Resistance and Survival',
              ['What was lost, and what', 'Native peoples preserved'],
              "The portrait is Zitkala-Sa, the Dakota writer named in the reading, photographed by Gertrude Käsebier in 1898 with her violin. Two years later her accounts of boarding school life appeared in eastern magazines, describing for white readers what the schools did to children, and challenging assimilation in print. She is the right face for this section because her life holds its whole argument. She was taken into the boarding school system the policy built, learned its language and its tools, and then used those tools in public to defend her people. Set the section's claim before the details. The story of this era does not end at Wounded Knee. Armed resistance had ended, but resistance changed form rather than disappearing, and preservation happened in homes, in courts, and in print. What Native nations lost is measured in acres, lives, and years of children taken from home. What they preserved is on the next two slides.",
              title_size=40)

# ------------------------------------------------------ 20 · RESISTANCE CHANGED FORM
content_text('Resistance changed form',
             ['Treaty claims pressed in courts and by petition',
              'Writers challenge assimilation in print',
              'Zitkala-Sa describes boarding school life for eastern readers',
              'Graduates use English and literacy to defend their nations'],
             "Make the continuity explicit: the peoples who fought in section A did not stop resisting when the wars ended; they changed instruments. Leaders pressed treaty claims in courts and by petition, using the government's own documents, including the treaties it had broken, as their evidence. Writers carried the case to the public. Zitkala-Sa, the Dakota author in the divider portrait, described boarding school life for eastern readers and challenged assimilation in print, reaching the same magazine audience that reformers wrote for. The boarding schools themselves supplied some of the tools: graduates used their English and literacy to defend their nations in court and in print, a result the schools' founders did not intend. Students sometimes read this as a silver lining that softens the policy. Correct that reading. A tool taken up by its target is resistance, not a benefit the policy planned, and the writing task rewards students who keep that distinction straight.",
             kick='F · Resistance and Survival')

# ------------------------------------------------------ 21 · WHAT WAS PRESERVED
content_text('What was preserved',
             ['Languages and ceremonies taught at home, hidden from agents',
              'Tribal governments survive on reduced land',
              'Languages and ceremonies endure',
              'Native nations still exist as peoples and governments today'],
             "End the survey where the reading ends. Families hid languages and ceremonies from agents and taught them at home, in the one place federal supervision could not reliably reach. That single fact explains much of what survived: a language spoken to children in a kitchen does not appear in an agent's report, and it can outlast a policy. Tribal governments survived on reduced land, and languages and ceremonies endured. Then give students the reading's closing judgment in full, because it reframes the whole lesson. What Native nations lost was measured in acres, lives, and years of children taken from home. What they preserved is the reason Native nations still exist as peoples and governments today. Return to the lesson question one last time. Assimilation was pursued to end Native cultures as distinct ways of life. Judged by its own goal, it failed, and the evidence of that failure is that the peoples it targeted are still here.",
             kick='F · Resistance and Survival')

# ------------------------------------------------------ 22 · VOCAB A
vocab('Words for the policy',
      [('assimilation', 'the process by which a person or group is made to adopt the customs and language of another culture'),
       ('allotment', 'the division of tribal land into individual parcels under federal policy'),
       ('Dawes Act', 'the 1887 federal law that divided reservation land into individual allotments and sold surplus land to non-Native buyers'),
       ('reservation system', 'federal policy that confined Native nations to defined areas of land under federal supervision')],
      "These four definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. Assimilation: the process by which a person or group is made to adopt the customs and language of another culture. Note the passive construction, made to adopt: assimilation here was imposed, not chosen. Allotment: the division of tribal land into individual parcels under federal policy. Dawes Act: the 1887 federal law that divided reservation land into individual allotments and sold surplus land to non-Native buyers. Reservation system: federal policy that confined Native nations to defined areas of land under federal supervision. Students confuse allotment and the Dawes Act most often. The act is the law; allotment is the process the law set running, on reservation after reservation, until 1934.")

# ------------------------------------------------------ 23 · VOCAB B
vocab('Words for the schools and the dance',
      [('boarding school', 'a school that removed Native children from their families to suppress Native languages and cultures'),
       ('Ghost Dance', 'a religious movement that promised renewal for Native peoples and spread across western reservations in 1889 and 1890'),
       ('Wounded Knee', 'the 1890 killing of Lakota men, women, and children by United States troops in South Dakota')],
      "Three more terms, again matching the guided notes exactly. Boarding school: a school that removed Native children from their families to suppress Native languages and cultures. The definition names the removal and the suppression, not education in general, and students should keep both parts when they use the term. Ghost Dance: a religious movement that promised renewal for Native peoples and spread across western reservations in 1889 and 1890. It was a religion, and the definition's word renewal is the one to underline: dancers sought the restoration of a world, not a military victory. Wounded Knee: the 1890 killing of Lakota men, women, and children by United States troops in South Dakota. Teach the term as a place name that carries an event: when students write Wounded Knee on the test, they mean December 29, 1890, Big Foot's band, and about 250 to 300 Lakota dead.")

# ------------------------------------------------------ 24 · TODAY'S WORK
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Policy and Consequence', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Work the stations. At each one, separate what officials said the policy would do from what the record shows it did.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Stations', 'The four stations, then your verdict'),
        ('Notebook', 'Loss, Resistance, and Survival: the policy chart, kept for review day'),
        ('Quick check', 'Before and After at Carlisle: read the Torlino portraits as evidence'),
        ('Writing', 'Help, Harm, or Both? Judge assimilation by its results')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.5, 0.6, d, size=19, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.8, 11.5, 0.5, 'Exit ticket: explain the Dawes Act, name two losses and two preservations, and state why assimilation was pursued.',
     size=16, color=POWDER)
notes(s, "Close by handing the lesson to its work. The activity, Policy and Consequence, runs four stations, the Dawes Act, a boarding school, the buffalo, and the Ghost Dance and Wounded Knee, then asks students to rank them by the gap between what officials said and what the record shows. The notebook page, Loss, Resistance, and Survival, collects the four policies in a chart kept for review day. The quick check, Before and After at Carlisle, returns to Tom Torlino's portraits and tests whether students can read a staged source. The writing task, Help, Harm, or Both, asks for one paragraph judged by results, with three evidence cards and one named Native nation. The exit ticket checks the spine: the Dawes Act explained, two losses and two preservations named, and assimilation's stated goal set against one real effect.")

dc.save(OUT)
