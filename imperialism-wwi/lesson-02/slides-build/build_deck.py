#!/usr/bin/env python3
"""Imperialism and World War I Lesson 2 deck, "The Spanish-American War,"
built to the approved Gilded Age system: image-led slides, fragments only
on screen, comprehensive speaker notes, full lesson + vocabulary coverage.
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
OUT = os.path.join(HERE, '..', 'lesson-02-slides.pptx')
KICK = 'IMPERIALISM AND WORLD WAR I \u00b7 LESSON 2'

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
text(s, 0.9, 5.32, 11.5, 0.4, KICK, size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Spanish-American War', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'A war of less than four months that ended Spanish rule in Cuba and left the United States holding an island empire', size=17, color=POWDER)
notes(s, "The print is Our Victorious Fleets in Cuban Waters, published by Currier and Ives in 1898 and held by the Library of Congress. It shows American warships under a bright sky and names the battleship Iowa and the cruiser New Orleans in the scene. Prints like this one were made for a public following the war as news, and the confidence in the picture is part of the story. In less than four months in 1898 the United States defeated Spain on two oceans, ended Spanish rule in Cuba, and took Puerto Rico, Guam, and the Philippines for itself. Frame the day as a verdict students must reach and defend. The war plainly freed Cuba from Spain. It also left the United States ruling millions of people overseas who had not chosen American rule. Both statements rest on the same documents, and the lesson question asks which one, or both together, explains why the war was fought.")

# ------------------------------------------------- 2 · LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('Was the war with Spain fought to free Cuba, to take an empire, or both?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('Why did the United States seek power overseas, and how did the First World War change the country that fought it?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question is the narrower one on the slide, and the unit question runs beneath it as the frame. This lesson answers the unit question through a single short war. The United States sought power overseas in 1898 in the name of a colony in rebellion ninety miles from Florida, and it came out of the fighting holding territory in the Caribbean and across the Pacific. Keep the three choices in the question visible all hour: free Cuba, take an empire, or both. Tell students that a choice is not an answer until it is defended with facts. Every section that follows hands them evidence for one side or the other: a promise Congress wrote into law before the fighting, battlefields on two oceans, and a peace treaty signed by Spain and the United States over peoples who were not in the room. By the closing slide each student must pick one choice and support it with two facts from the reading.")

# --------------------------------------------------- 3 · THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.3, 11.5, 1.0, 'From rebellion to empire in one year', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.42)
rows = [('A', 'Cuba in rebellion', 'an island in revolt since 1895, and Spain\u2019s harsh answer'),
        ('B', 'The Maine and the yellow press', 'an explosion in Havana harbor, and newspapers racing to blame Spain'),
        ('C', 'A promise attached to the war', 'the Teller Amendment: no annexation of Cuba'),
        ('D', 'War on two oceans', 'Dewey at Manila Bay, and the Rough Riders at Santiago'),
        ('E', 'The treaty and the cost', 'three cessions, a protected Cuba, and a death toll set by disease')]
yy = 2.82
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.7, n, size=26, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.03, 3.4, 0.7, t, size=23, color=CREAM, bold=True)
    text(s, 5.15, yy + 0.08, 7.3, 0.7, d, size=18, color=POWDER)
    yy += 0.9
notes(s, "This is the map of the lesson, and it follows the guided notes section by section. Section A sets the cause: Cuba in rebellion since 1895 and Spain's policy of reconcentration, which killed large numbers of Cuban civilians. Section B covers the spark, the destruction of the battleship Maine in Havana harbor and the yellow press campaign that followed it. Section C is the promise Congress attached to the war before it began, the Teller Amendment. Section D follows the fighting on two oceans, in the Philippines and in Cuba, a fact students should notice early because a war fought only for Cuba did not need a Pacific battlefield. Section E closes with the Treaty of Paris, the Platt Amendment, and the real cost of the war, which disease set far more than battle did. Tell students the settlement chart and the exit ticket both draw on sections C and E, so the promises, the treaty terms, and the numbers need to land today.")

# ------------------------------------------------- 4 · SECTION A DIVIDER
divider_photo('gillam-port.jpg', 'Section A', 'Cuba in Rebellion',
              ['An island in revolt since 1895', 'Spain answers with reconcentration'],
              "The cartoon is Remember the Maine! And Don't Forget the Starving Cubans!, drawn by Victor Gillam and published in Judge magazine on May 7, 1898, after the war had begun. A mourning Uncle Sam stands before an open album. One page pairs the Maine as it was with the wreck as it is, and the facing page shows starving Cubans drawn from photographs. Gillam is looking backward at this section's subject and forward to the next one in a single image. The rebellion he expects readers to remember began in 1895, three years before the cartoon, when Cubans rose against four centuries of Spanish rule. Spain's answer, General Weyler's reconcentration, drove civilians into fortified towns where disease and hunger killed them in large numbers. Hold the cartoon for section B as well. Here, use it for the second page of the album: the starving Cubans were the human cause Americans cited before any battleship exploded.",
              title_size=44)

# ------------------------------------------------------ 5 · CUBA IN REBELLION
content_text('Cuba in rebellion',
             ['A Spanish colony for four centuries',
              'Cubans rose in rebellion in 1895',
              'General Weyler ordered civilians into fortified towns',
              'Reconcentration: disease and hunger in the crowded towns',
              'Contemporary estimates put the deaths in the tens of thousands',
              'McKinley pressed Spain, and Spain recalled Weyler'],
             "Teach this section as the war's cause, in the reading's own order. Cuba had been a Spanish colony for four centuries when Cubans rose in rebellion in 1895 to win independence. Spain sent General Valeriano Weyler to crush the revolt. Weyler ordered Cuban civilians in rebellious districts to move into fortified towns, a policy called reconcentration. In the crowded towns, disease and hunger killed large numbers of Cubans. Contemporary estimates put the deaths in the tens of thousands, and some ran far higher, so give students the range rather than a single settled figure. Americans also held sugar investments in Cuba, ninety miles from Florida, which gave the United States a material interest beside the humanitarian one. President William McKinley pressed Spain to end reconcentration, and Spain recalled Weyler, but the rebellion continued. End on the reading's last line of the section. In January 1898 the battleship Maine arrived in Havana harbor on a friendly visit.",
             kick='A \u00b7 Cuba in rebellion', size=25)

# ------------------------------------------------- 6 · SECTION B DIVIDER
divider_photo('maine-port.jpg', 'Section B', 'The Maine and the Yellow Press',
              ['February 15, 1898, in Havana harbor', '266 officers and men killed'],
              "The photograph shows the wreck of the USS Maine in Havana harbor, photographed at about 1898 and held by the National Archives. The forward part of the ship was destroyed and the wreck settled into the harbor mud, where it stayed in view while the country argued about what had happened. This section has two subjects, and students should keep them separate. The first is an event: a battleship exploded at 9:40 on the night of February 15, 1898, killing 266 officers and men. The second is a contest: two New York newspapers fighting for readers, and an official inquiry that refused to say who was responsible. The event was a fact. What Americans were told the event meant arrived through the contest, and the gap between the two is where this war came from. The slogan that crossed the country, Remember the Maine, named the ship and not the evidence, which is exactly the point to teach.",
              title_size=40)

# ------------------------------------------------------ 7 · FEBRUARY 15
content_text('The night of February 15, 1898',
             ['The Maine arrived in Havana in January, on a friendly visit',
              'On February 15 the battleship exploded and sank',
              '266 officers and men were killed',
              'The slogan spread: Remember the Maine'],
             "Set the scene from the reading before any argument about causes. The battleship Maine had arrived in Havana harbor in January 1898 on a friendly visit, while Cuba's rebellion continued around it. On February 15, 1898, the ship exploded and sank. Use the key term in its full form here, because the unit test draws on it. The USS Maine was the American battleship that exploded and sank in Havana harbor on February 15, 1898, killing 266 officers and men and becoming the rallying cause of the war. Pause on the size of the loss. Two hundred sixty-six deaths in one night, in a harbor Americans could picture, gave the explosion a weight no report from the Cuban countryside had carried. The slogan Remember the Maine spread across the country in the days that followed. Notice what the slogan does and does not say. It commands memory and anger. It does not name a culprit, because no culprit had been established. The next slide shows who filled that silence, and why.",
             kick='B \u00b7 The Maine and the yellow press', size=25)

# ------------------------------------------------------ 8 · YELLOW PRESS
content_photo('gillam-port.jpg', 'Two newspapers, racing for readers',
              ['Hearst\u2019s Journal against Pulitzer\u2019s World',
               'Dramatic accounts of the disaster, day after day',
               'Spanish guilt treated as settled fact',
               'No evidence connected Spain to the explosion'],
              "This is the Gillam cartoon again, from Judge, May 7, 1898, and here its work is different: it shows the mood the yellow press built. Two New York newspapers, William Randolph Hearst's Journal and Joseph Pulitzer's World, were fighting each other for readers, and both filled their pages with dramatic accounts of the disaster. Their style of reporting had a name: yellow journalism, sensational newspaper reporting that stretched or invented facts to sell papers and stir public feeling. Headlines in the yellow press treated Spanish guilt as settled fact, although no evidence connected Spain to the explosion. A cooler voice shows the contrast. Harper's Weekly, writing on February 26, 1898, called the fate of the Maine an unsolved mystery and counted 246 killed. That early count differs from the final toll of 266, which includes men who later died of their wounds. Early reporting after a disaster is a first count, not the settled record, and students should hold both lessons: the yellow press overstated certainty, and even careful reporting started from incomplete figures.",
              kick='B \u00b7 The Maine and the yellow press')

# ------------------------------------------------------ 9 · THE INQUIRY
content_text('What the inquiry found, and what it did not',
             ['A naval court of inquiry examined the wreck',
              'Its finding: a submarine mine outside the ship',
              'The mine set off part of her ammunition',
              'No evidence fixing responsibility on any person',
              'Later investigations disagreed, and the cause is still debated'],
             "Read the inquiry's two findings as two separate sentences, because the war argument depended on blurring them. A naval court of inquiry concluded that a submarine mine outside the ship had set off part of her ammunition. That is a finding about a cause, and even it did not settle the question for good: later investigations disagreed, and the cause is still debated. The same report stated that it had obtained no evidence fixing responsibility on any person. That is a finding about blame, and it points at no one, Spain included. Put the two side by side and ask what a headline writer could honestly claim. A mine, on the court's word. A culprit, on nobody's evidence. In the spring of 1898, however, the public argument moved faster than the evidence. Within weeks Congress was writing war resolutions. Section C begins with the promise those resolutions carried, offered before the first shot, by a senator who wanted the war's purpose fixed in law while it could still be fixed.",
             kick='B \u00b7 The Maine and the yellow press', size=24)

# ------------------------------------------------- 10 · SECTION C DIVIDER
divider_photo('mckinley-port.jpg', 'Section C', 'A Promise Attached to the War',
              ['Congress declares Cuba free', 'and promises not to take it'],
              "The portrait shows President William McKinley, photographed before his death in 1901. McKinley had pressed Spain to end reconcentration, received the Maine inquiry's report in March 1898, and signed the war resolutions that April. His signature sits at the center of this short section, but the promise in it was not his. Senator Henry M. Teller of Colorado offered the fourth resolution, and Congress adopted it, so the war began with a renunciation attached to it in law. That sequence is the teaching point. The promise was not made after the fighting, as an excuse or a decoration. It was made in April 1898, before the fighting, by men who knew the charge it answered: that a war against Spain's empire would become a war to build an American one. Every later document in this lesson, above all the Platt Amendment, gets judged against this promise. Students should learn it today as a standard to measure with, not as a slogan to repeat.",
              title_size=38)

# ------------------------------------------------------ 11 · TELLER AMENDMENT
content_text('April 1898: resolutions and a promise',
             ['Congress declared Cuba free and independent',
              'Spain was demanded to withdraw its forces',
              'The president was authorized to use the army and navy',
              'The Teller Amendment: the United States would not annex Cuba',
              'McKinley signed on April 20; war was declared April 25'],
             "Walk the April resolutions in order, as the guided notes do. In April 1898 Congress adopted resolutions declaring Cuba free and independent, demanding that Spain withdraw its forces, and authorizing the president to use the army and navy to carry the resolutions out. A fourth resolution, offered by Senator Henry M. Teller of Colorado, was the Teller Amendment: the 1898 congressional provision promising that the United States would not annex Cuba and would leave its government to the Cuban people. Say plainly why it was offered. It answered in advance the charge that the war meant annexation. McKinley signed the resolutions on April 20, and on April 25 Congress declared war, dating the start of the conflict to April 21. Note the discipline the amendment imposed and the silence inside it. It limited American claims on Cuba by name. It said nothing about Spain's other colonies, in the Caribbean or the Pacific. The next section opens in one of those colonies, and the silence starts to do work.",
             kick='C \u00b7 A promise attached to the war', size=24)

# ------------------------------------------------- 12 · SECTION D DIVIDER
divider_photo('dewey-port.jpg', 'Section D', 'War on Two Oceans',
              ['First at Manila Bay, in the Pacific', 'Then at Santiago, in Cuba'],
              "The print is Admiral Dewey at the Battle of Manila, a contemporary colored print held by the Naval History and Heritage Command as photograph NH 84510-KN. It depicts Commodore George Dewey on the bridge of his flagship, USS Olympia, during the Battle of Manila Bay on May 1, 1898, and it comes courtesy of the Naval Historical Foundation. Section D is the fighting, and its geography is its argument. The war's first battle was not fought off Cuba at all. It was fought in the Philippines, Spain's colony in the Pacific, thousands of miles from the island the war was declared to free. Only after Dewey's morning at Manila Bay does the section turn to Cuba, to the landings near Santiago, the San Juan Heights, and the destruction of the Spanish fleet on July 3. Teach the two campaigns as a pair. Together they took less than three months, and together they decided what the peace would have to dispose of: not one island, but an empire's remains on two oceans.",
              title_size=44)

# ------------------------------------------------------ 13 · MANILA BAY
content_text('May 1, 1898: Manila Bay',
             ['The first battle was fought in the Philippines, not Cuba',
              'Commodore George Dewey led the squadron into Manila Bay',
              'The Spanish Pacific fleet was destroyed in a single morning',
              'No American sailor was killed by Spanish fire',
              'Manila surrendered to American forces in August'],
             "Slow down on the first fragment, because it carries the section's surprise. The first battle of the war took place not in Cuba but in the Philippines, Spain's colony in the Pacific. On May 1, 1898, Commodore George Dewey led an American squadron into Manila Bay and destroyed the Spanish Pacific fleet in a single morning. No American sailor was killed by Spanish fire, a fact students should weigh carefully. A fleet was destroyed, a colonial capital was cut off, and the attacking force lost no one to enemy fire. Manila surrendered to American forces in August. Now connect the battle back to section C. The Teller Amendment limited American claims on Cuba. It said nothing about the Philippines. Nothing in the promise Congress made in April prevented an American squadron from taking a Spanish colony in Asia, or prevented the peace from keeping it. Whether that silence was an oversight or an opening is a question students can argue from the documents, and the treaty in section E will give them the material to argue with.",
             kick='D \u00b7 War on two oceans', size=24)

# ------------------------------------------------------ 14 · ROUGH RIDERS
content_photo('rough-port.jpg', 'July 1: the San Juan Heights',
              ['American troops landed east of Santiago in June',
               'July 1: attacks at El Caney and on the San Juan Heights',
               'On Kettle Hill, the Rough Riders charged',
               'Beside them, the Black troopers of the 9th and 10th Cavalry',
               'Roosevelt had resigned a navy post to serve'],
              "The photograph is Colonel Roosevelt and his Rough Riders at the top of the hill which they captured, taken by William Dinwiddie in 1898 and held by the Library of Congress. Carry its disclosure into the open, as the printed lesson does: this is a posed group photograph taken on the hilltop after the capture, commonly dated to about July 3, 1898, two days after the charge. It proves who held the hill and who stood together on it, including troopers of the 3rd and 10th Cavalry beside the Rough Riders. It cannot show the charge itself. The campaign it caps ran as the reading gives it. American troops landed east of Santiago in June and attacked on July 1 at El Caney and on the San Juan Heights. On Kettle Hill the Rough Riders charged alongside regular regiments, including the Black troopers of the 9th and 10th Cavalry. The Rough Riders were the First United States Volunteer Cavalry, the regiment led by Theodore Roosevelt that won fame in the fighting around Santiago, Cuba. Roosevelt had resigned a navy post to serve.",
              kick='D \u00b7 War on two oceans')

# ------------------------------------------------------ 15 · SANTIAGO FALLS
content_text('July and August: the war ends',
             ['July 3: the Spanish fleet destroyed as it tried to escape',
              'July 17: Santiago surrendered',
              'American forces occupied Puerto Rico',
              'August 12: Spain signed an armistice'],
             "Close the fighting in the reading's order. On July 3, two days after the San Juan Heights, the Spanish fleet at Santiago tried to escape and American warships destroyed it. With the fleet gone, the city had no relief coming, and Santiago surrendered on July 17. American forces occupied Puerto Rico, one more Spanish colony taken in a war declared for Cuba alone, and Spain signed an armistice on August 12. Stand back and take the measure of the campaign with students. From the declaration of war in late April to the armistice in mid August ran less than four months. In that span the United States destroyed two Spanish fleets, took Manila, took Santiago, and occupied Puerto Rico. Spain's four-century American empire was finished, and its Pacific colony was in American hands. Nothing in the armistice itself decided who would keep any of it. Armistices stop fighting; treaties dispose of territory. Section E is the treaty, and it is where the lesson question stops being about intentions and becomes a question about a signed document.",
             kick='D \u00b7 War on two oceans', size=25)

# ------------------------------------------------- 16 · SECTION E DIVIDER
divider_photo('manila-port.jpg', 'Section E', 'The Treaty of Paris and the Cost',
              ['December 10, 1898: Spain signs', 'The fighting was the short part'],
              "The painting is the Battle of Manila Bay by James Gale Tyler, painted in 1898, the year of the battle it shows. Dewey's squadron is back on screen because the treaty in this section kept what that morning won. Section E holds the two halves of the war's ending, and they pull in opposite directions. The first half is a document: the Treaty of Paris, signed on December 10, 1898, which disposed of Cuba, Puerto Rico, Guam, and the Philippines in three articles. The second half is a count: fewer than 400 Americans killed in battle, against about 2,400 dead in all, most of them killed by disease in camps and in Cuba. Teach the section in that order, as the guided notes do, treaty first and cost second. Students who meet the cessions before the death toll can weigh the settlement coolly. Students who then meet the toll understand the price at which the settlement was bought, and by whom it was mostly paid: enlisted men in typhoid camps who never faced Spanish fire.",
              title_size=38)

# ------------------------------------------------------ 17 · TREATY OF PARIS
content_text('The Treaty of Paris, December 10, 1898',
             ['Spain gave up its claim to Cuba',
              'Cuba: independent, under a temporary American occupation',
              'Puerto Rico and Guam passed outright',
              'The Philippines were ceded for twenty million dollars',
              'The Senate ratified by one vote above two thirds'],
             "Give the treaty in its full key-term form first. The Treaty of Paris was the December 1898 treaty that ended the war and transferred Puerto Rico, Guam, and the Philippines from Spain to the United States. It was signed on December 10, 1898, and its terms divide by a verb students must learn here. Spain gave up its claim to Cuba, which was to be independent under a temporary American occupation; Cuba was relinquished, not transferred. The other three places changed hands by cession: the formal transfer of territory from one country to another by treaty. Puerto Rico and Guam passed to the United States outright, and Spain ceded the Philippine Islands in return for a payment of twenty million dollars. Filipino leaders had declared their own republic. They were not parties to the treaty and had not consented to the transfer. The Senate ratified the treaty on February 6, 1899, one vote above the two-thirds majority required. One vote is the margin between the settlement students are reading and a different history.",
             kick='E \u00b7 The treaty of Paris and the cost', size=24)

# ------------------------------------------------------ 18 · THE COST STAT
stat('2,400', 'American servicemen died during the war, in all',
     'Fewer than 400 were killed in battle or died of wounds. Disease, in the training camps and in Cuba, killed the great majority.',
     "Dwell on the gap between the two numbers, because it corrects the picture the prints and cartoons leave behind. The fighting lasted less than four months, and fewer than 400 American servicemen were killed in battle or died of wounds. In all, about 2,400 American servicemen died during the war, the great majority from illness rather than Spanish fire. Name the killers from the reading. Typhoid spread through training camps in the United States, before many soldiers ever sailed. Malaria and yellow fever struck troops in Cuba. A soldier was far more likely to die in a camp hospital than on the San Juan Heights. Ask students why the famous images of this war show charges and fleets rather than hospital wards. The posed photograph, the victorious print, and the mourning cartoon all had subjects a camera or an artist could frame. Disease in a camp had no single scene, so the war's largest cost is also its least pictured, and students should learn to ask what a record leaves out.",
     kick='E \u00b7 The treaty of Paris and the cost')

# ------------------------------------------------------ 19 · PLATT AMENDMENT
content_text('Cuba after independence: the Platt Amendment',
             ['Cuba became formally independent in 1902',
              'First, the Platt Amendment went into Cuba\u2019s constitution',
              'The United States kept a right to intervene in Cuba',
              'And a right to hold naval stations there',
              'Guantanamo Bay was leased as a naval station in 1903'],
             "End the lesson's narrative with the measure that tests the Teller promise. Cuba became formally independent in 1902, but before American troops withdrew, Congress passed the Platt Amendment in 1901 and required Cuba to write it into its constitution. Use the full definition, which the exit ticket assumes. The Platt Amendment was the 1901 congressional provision, written into Cuba's constitution, that gave the United States the right to intervene in Cuba and to hold naval stations there. Under it, the United States leased Guantanamo Bay as a naval station in 1903. Now set the two amendments side by side and let students do the judging. The Teller Amendment promised no annexation and government left to the Cuban people, and Cuba was not annexed. The Platt Amendment kept an American right to intervene and American naval stations on Cuban soil, inside the constitution of the independent republic itself. The reading's verdict is exact, and worth reading aloud: Cuba was independent in form and a protectorate in practice.",
             kick='E \u00b7 The treaty of Paris and the cost', size=24)

# ------------------------------------------------------ 20 · VOCAB A
vocab('Words for the spark and the fighting',
      [('yellow journalism', 'sensational newspaper reporting that stretched or invented facts to sell papers and stir public feeling'),
       ('USS Maine', 'the American battleship that exploded and sank in Havana harbor on February 15, 1898, killing 266 officers and men and becoming the rallying cause of the war'),
       ('Teller Amendment', 'the 1898 congressional provision promising that the United States would not annex Cuba and would leave its government to the Cuban people'),
       ('Rough Riders', 'the First United States Volunteer Cavalry, the regiment led by Theodore Roosevelt that won fame in the fighting around Santiago, Cuba')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. Yellow journalism names the reporting style of the Hearst and Pulitzer contest, and it explains how an explosion with no established culprit became a case for war in print. The USS Maine definition fixes the date, the place, and the toll of 266 in one sentence, and it calls the ship the rallying cause, which is a claim about politics rather than about the explosion itself. The Teller Amendment definition holds the promise of April 1898 in the form students will need when they judge the Platt Amendment against it. The Rough Riders definition fixes the regiment's formal name and its commander, so the famous nickname never floats free of the First United States Volunteer Cavalry. One memory hook links the four: a press style, a ship, a promise, and a regiment carried the country from February to July of 1898.")

# ------------------------------------------------------ 21 · VOCAB B
vocab('Words for the settlement',
      [('Treaty of Paris', 'the December 1898 treaty that ended the war and transferred Puerto Rico, Guam, and the Philippines from Spain to the United States'),
       ('cession', 'the formal transfer of territory from one country to another by treaty'),
       ('Platt Amendment', "the 1901 congressional provision, written into Cuba's constitution, that gave the United States the right to intervene in Cuba and to hold naval stations there")],
      "Three more terms, again matching the guided notes exactly, and these three carry the settlement between them. The Treaty of Paris is the December 1898 treaty that ended the war and transferred Puerto Rico, Guam, and the Philippines from Spain to the United States; note that Cuba is absent from that list of transfers, which is the treaty's most instructive silence. A cession is the formal transfer of territory from one country to another by treaty, and students need the word used precisely: Puerto Rico, Guam, and the Philippines were ceded, and Cuba was not. The Platt Amendment, from 1901, gave the United States the right to intervene in Cuba and to hold naval stations there, inside Cuba's own constitution. Put the three in a row and the lesson question nearly answers itself in vocabulary form. A treaty, three cessions, and a protectorate written into a neighbor's founding document describe an ending larger than the liberation the war was declared to win.")

# ------------------------------------------------------ 22 · SETTLEMENT AT A GLANCE
content_text('The settlement at a glance',
             ['Cuba: claim relinquished, not ceded',
              'Independent in 1902, a protectorate in practice under Platt',
              'Puerto Rico and Guam: ceded outright',
              'Held as American territory',
              'The Philippines: ceded for twenty million dollars',
              'A declared Filipino republic, never consulted'],
             "Use this slide to fill in the settlement chart at the end of the guided notes, row by row, and make students attach the right verb to each place. Cuba: Spain relinquished all claim, the island was not ceded, and it became independent in 1902 after a temporary American occupation, but a protectorate in practice under the Platt Amendment, with a United States naval station leased at Guantanamo Bay in 1903. Puerto Rico and Guam: ceded to the United States by the Treaty of Paris and held as American territory. The Philippines: ceded in return for twenty million dollars and held as an American possession, although Filipino leaders had declared a republic and had not consented to the transfer. Press students on why the verbs matter to the argument. Relinquish, cede, and protect describe three different relationships between the United States and three peoples in a single treaty. A verdict on the lesson question that uses only one verb for all three rows has not read the settlement closely.",
             kick='The settlement at a glance', size=24)

# ------------------------------------------------------ 23 · THE EVIDENCE, SORTED
content_text('Free Cuba, take an empire, or both?',
             ['For liberation: the Teller promise, kept in form',
              'For liberation: Spanish rule and reconcentration ended',
              'For empire: three cessions in one treaty',
              'For empire: the Philippines bought, without Filipino consent',
              'Both at once: one settlement did all of it'],
             "Sort the evidence aloud before the closing work, and model the strongest form of each side. For liberation: Congress promised in the Teller Amendment that the United States would not annex Cuba, Cuba was not annexed, and American arms ended a Spanish rule whose reconcentration policy had killed Cuban civilians in large numbers. For empire: the same war's treaty transferred Puerto Rico, Guam, and the Philippines to the United States, the Philippines for twenty million dollars paid to Spain, with no Filipino signature and no Filipino consent. For both at once: a single settlement contains the kept promise and the three cessions, the independent republic and the intervention right written into its constitution. Warn students against the easy error on each side. A liberation verdict that never mentions Manila has read half the war. An empire verdict that never mentions the Teller Amendment has read half the record. The reading question allows any of the three verdicts, defended with two facts, one of which must concern the Platt Amendment.",
             kick='The verdict', size=24)

# ------------------------------------------------------ 24 · CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Headline and Evidence Lab', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Return to the lesson question: was the war with Spain fought to free Cuba, to take an empire, or both? The lab is where you judge it from the documents.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'Headline and Evidence Lab: six stations, from the Gillam cartoon to the treaty'),
        ('Notebook', 'Weigh the rallying cry against the inquiry, and the promise against the Platt Amendment'),
        ('Quick check', 'Our Victorious Fleets: read the 1898 print against the record'),
        ('Writing', 'Free Cuba, take an empire, or both, with two facts, one on the Platt Amendment')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.5, 0.6, d, size=19, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.8, 11.5, 0.5, 'Exit ticket: define cession, sort the territories, and answer the lesson question with one fact.',
     size=16, color=POWDER)
notes(s, "Close by handing the lesson to its work. The activity is the Headline and Evidence Lab. Students move through six stations in order: the Gillam cartoon, the Harper's Weekly report with its early count of 246 killed against the final toll of 266, the inquiry conclusions, the Teller Amendment, the Dinwiddie photograph with its posed character stated on its face, and the treaty with the Platt articles. At the end they sort six claims as liberation, conquest, or both, and deliver a verdict. The notebook page then asks students to weigh the rallying cry against the inquiry and the promise against the Platt Amendment in writing. The quick check works from the Currier and Ives fleet print from today's title slide. The writing task returns to the lesson question, with two facts required and one of them on the Platt Amendment. Next lesson, the empire taken at Paris meets the people it was taken from, in the Philippines.")

dc.save(OUT)
