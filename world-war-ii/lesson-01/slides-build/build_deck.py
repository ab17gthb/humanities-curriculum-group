#!/usr/bin/env python3
"""World War II Lesson 1 deck, "The Road to War: Neutrality and Its Critics,"
built to the approved system: image-led slides, fragments only on screen,
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
OUT = os.path.join(HERE, '..', 'lesson-01-slides.pptx')

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

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'WORLD WAR II · LESSON 1', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Road to War: Neutrality and Its Critics', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'How a neutral country armed an ally and fought at sea, 1935 to 1941', size=17, color=POWDER)
notes(s, "The photograph shows President Roosevelt and Prime Minister Churchill seated on the quarterdeck of HMS Prince of Wales during the Atlantic Conference of August 1941, from the Imperial War Museums Admiralty Official Collection. Hold the date in front of students. This is four months before Pearl Harbor, and the United States is still legally at peace, yet its president is meeting a belligerent leader aboard a warship to issue a joint statement of aims. That gap between law and fact is the whole lesson. The unit opens in 1935 rather than 1939 or 1941 because the neutrality debate is the argument the war answers. Students will walk the road step by step, from the laws that barred aid to any nation at war to the autumn of 1941, when American destroyers were fighting German submarines and an American destroyer had been sunk. At every step they will be asked to judge the direction of travel.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('Between 1935 and 1941, how did the United States move from legislated neutrality toward war without declaring it?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the Second World War transform the United States, and how far did the country live up to the democracy it claimed to defend?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question is built from two phrases students should unpack before the lesson begins. Legislated neutrality means neutrality written into law, voted by Congress and binding on the president, which is what the Neutrality Acts did in the 1930s. Toward war without declaring it means the movement happened in practice while the legal state of peace stayed in place, and the lesson ends in the autumn of 1941 with that contradiction at its sharpest. The unit question runs beneath it as the frame for all eight lessons. Notice that today's lesson ends before any declaration and before Pearl Harbor. What it explains is how the country arrived at December 1941 already armed, already committed to one side's survival, and already fighting at sea, so that the declaration, when it came, settled a debate the country had been having for six years.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'A road in seven stretches', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The memory of the First War', '116,000 dead, and the Nye charge'),
        ('B', 'The Neutrality Acts', 'Arms, loans, and travel barred by law'),
        ('C', 'Wars Americans watched', 'China, Ethiopia, Spain, then Poland'),
        ('D', 'A president pushes', 'Quarantine, the arsenal, the Four Freedoms'),
        ('E', 'The fall of France and the turn to aid', 'Destroyers, the draft, Lend-Lease'),
        ('F', 'The case for staying out', 'America First and the two oceans'),
        ('G', 'The Charter and the shots at sea', 'Common aims, convoys, the Reuben James')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Sections A and B give the starting point: a country whose memory of 1917 produced laws meant to make another entry impossible. Section C shows the wars that tested those laws from outside. Section D follows a president testing them from inside, by speech rather than by statute. Section E is the turn, when France fell and aid replaced embargo step by step. Section F states the opposition case fairly, because the argument was real and the country was divided. Section G closes at sea, where the neutrality the laws described no longer existed. Tell students the summary table at the end of their guided notes, The Road at a Glance, asks them to rebuild exactly this map in their own words.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', 'The Memory of the First War',
             'The war that ended in 1918 governed the arguments of the 1930s.',
             "Begin with the point that the First World War was not ancient history in 1935. It had ended seventeen years earlier, within the living memory of every voter and every member of Congress, and many of the men who would vote on the Neutrality Acts had served in it or had buried friends from it. The figures in this section are the ones the reading opens with, and students should copy them exactly: two million men sent to France, about 116,000 dead, and 200,000 more wounded. Then add the interpretive layer. In the 1930s Americans argued not only about what the war had cost but about why the country had entered it at all. That second argument, carried by the Nye Committee hearings, is what turned a memory into legislation. Keep the two apart in the notes: the cost is a figure, the charge is an argument about the figure.")

# ------------------------------------------------------ 5 MEMORY AND NYE
content_text('A memory, and a charge that sharpened it',
             ['Two million men sent to France in 1917 and 1918',
              'About 116,000 dead; 200,000 more wounded',
              'The Nye Committee investigated arms makers and bankers, 1934 to 1936',
              'The charge: profits and loans pulled the country into war',
              'Congress drew the lesson: cut the ties first'],
             "Give the committee its full setting, because students tend to hear the Nye charge as a footnote and it was a national event. The Senate Special Committee on Investigation of the Munitions Industry, chaired by Gerald Nye of North Dakota, held hearings from 1934 to 1936 on arms makers and on the banks that had lent to Britain and France before 1917. Witnesses described wartime profits, and the committee's supporters drew the conclusion the reading states: firms fearing for their profits and their loans had pulled the United States into the war. Say plainly, as the reading does, that historians dispute the charge. Germany's submarine campaign and the Zimmermann telegram sit awkwardly inside it. Yet the charge persuaded millions in a Depression decade already suspicious of bankers, and it supplied the Neutrality Acts with their logic. If commerce caused entry, law would police commerce.",
             kick='A · The memory of the First War')

# ------------------------------------------------------ 6 WWI DEAD STAT
stat('116,000', 'American dead in the First World War',
     'Two million men sent to France · More than 200,000 came home wounded',
     "Let this figure stand for a moment before explaining it, because it does more work than any other number in the lesson. About 116,000 American dead is the human ground on which the neutrality laws were built. When members of Congress in 1935 spoke of keeping the country out of another world war, this is the bill they were picturing, town by town and family by family. The wounded figure belongs beside it in the notes: more than 200,000 men came home wounded, so the war stayed visible in American streets for decades in a way a casualty total alone does not capture. Ask students to hold the figure against the politics that follow. A nation that had paid this price within living memory did not need to be cowardly or selfish to fear paying it again. The isolationist case in this lesson begins from a real cost, and students judge it better when they feel the weight of the number first.",
     kick='A · The memory of the First War')

# ------------------------------------------------- 7 SECTION B DIVIDER
divider_text('Section B', 'The Neutrality Acts',
             'The lesson of 1917, written into law.',
             "This section covers the laws themselves, and students should learn them as a list with a purpose, not as a blur of dates. The act of 1935 barred arms exports to any nation at war once the president proclaimed a state of war. The acts of 1936 and 1937 added the ban on loans to nations at war and barred American travel on belligerent ships. Each provision answers a specific memory of 1917: arms sales that tied American industry to one side, loans that tied American banks to an Allied victory, and passengers on belligerent ships whose deaths had pulled the country toward war. Name the design choice at the center of the acts and keep returning to it. The laws treated attacker and attacked alike, because their purpose was not to judge foreign quarrels. Their purpose was to keep American ships, goods, and credit out of the quarrel altogether.")

# ------------------------------------------------------ 8 THE ACTS
content_text('Bars on arms, loans, and travel',
             ['1935: arms exports to nations at war barred',
              'Later acts: loans to nations at war banned',
              'Americans barred from travel on belligerent ships',
              'Attacker and attacked treated alike',
              'The policy behind the acts: isolationism'],
             "In the guided notes definition, the Neutrality Acts are the laws passed by Congress in the 1930s that barred arms sales and loans to nations at war, written to keep the United States out of another world war. Work the definition in its two halves: the bars, and the purpose. The bars fell on commerce, because the Nye lesson said commerce was the road in. The purpose was prevention, and it was pursued by evenhandedness: an embargo that fell on both sides could not be called favoritism, and it kept American ships out of war zones. The cost of evenhandedness belongs in the notes too. A law that barred arms to Germany and Britain alike barred them in practice to the side that needed to buy and could not make enough at home. Students will meet that cost in Section C, when the acts meet real wars. The word behind the policy is isolationism, which the vocabulary slides take up in full at the end of the lesson.",
             kick='B · The Neutrality Acts', size=24)

# ------------------------------------------------- 9 SECTION C DIVIDER
divider_photo('shanghai-port.jpg', 'Section C', 'Wars Americans Watched',
              ['Japanese forces in Shanghai,', 'China, in 1937.'],
              "The photograph shows Japanese Special Naval Landing Forces during the Battle of Shanghai in 1937, from the public domain record of the period. Use it to set the section's problem. The wars of the 1930s were not rumors from far away. Americans watched them in newsreels, in newspaper photographs, and on the radio, and the wars arrived in a sequence students should be able to recite by the end of the section: Japan in Manchuria in 1931 and in China from 1937, Italy in Ethiopia in 1935 and 1936, civil war in Spain with German and Italian bombers on Franco's side, and Germany absorbing Austria, taking the Sudetenland, seizing the rest of Czechoslovakia, and invading Poland on September 1, 1939. Each war posed the same question to the neutrality laws, and the laws answered each one the same way, by standing aside. Whether standing aside was wisdom or surrender is the argument students are being equipped to judge.",
              title_size=38)

# ------------------------------------------------------ 10 WARS WATCHED
content_text('Aggression in sequence, and the laws standing aside',
             ['Japan: Manchuria 1931, China 1937',
              'Italy conquered Ethiopia, 1935 to 1936',
              'Spain: German and Italian bombers for Franco',
              'Germany: Austria, the Sudetenland, Czechoslovakia',
              'Poland, September 1, 1939; Britain and France declare war'],
             "Walk the sequence slowly, because the order is the argument. No single one of these wars forced an American decision, and that is exactly why the road ran the way it did: each act of aggression was met by the neutrality framework doing what it was built to do. Two details deserve emphasis in the notes. First, because Japan and China never formally declared war, Roosevelt did not invoke the Neutrality Acts against them, and American goods still reached China, a gap between the law's words and the war's reality that previews the whole lesson. Second, in Europe the acts worked as written, and their working exposed the flaw their authors had accepted. An embargo falling on both sides fell hardest on the side that needed to buy. Britain and France needed American arms. Germany, preparing for years, needed them less. Evenhanded law, uneven effect: students should write that pairing down.",
             kick='C · Wars Americans watched', size=24)

# ------------------------------------------------- 11 SECTION D DIVIDER
divider_photo('fdr-port.jpg', 'Section D', 'A President Pushes Against the Current',
              ['President Franklin D. Roosevelt,', 'photographed in 1940.'],
              "The portrait is Franklin D. Roosevelt in 1940, from the National Archives record, number 195776. Section D turns from Congress to the president, and the turn is the lesson's hinge. Roosevelt doubted the Neutrality Acts from the start, yet he had signed them, and he governed a country that kept electing the Congress that passed them. His method in this period was not confrontation but pressure by speech: testing opinion, retreating when the test failed, and returning with smaller steps that each moved policy a little. Students should watch for the pattern across the section, because it explains the road's shape. The Quarantine speech of 1937 is the test that failed. The fireside chats are the smaller steps, explaining danger in plain language to a radio audience. The Arsenal of Democracy address and the Four Freedoms are the steps that held, because by late 1940 France had fallen and the country was ready to hear them.",
              title_size=34)

# ------------------------------------------------------ 12 QUARANTINE
content_text('The Quarantine speech, and its cold reception',
             ['Chicago, October 5, 1937',
              'Aggression compared to an epidemic of disease',
              'Peace loving nations should quarantine aggressors',
              'No country named; no measure proposed',
              'Attacked as a step toward war; the idea dropped'],
             "Teach the speech from its comparison, because the comparison is the proposal. In the passage students read at Station 3 of the activity, Roosevelt calls world lawlessness an epidemic and war a contagion that can engulf peoples far from the fighting, and he says a community approves and joins in a quarantine of the patients. Translated out of metaphor, the proposal is collective pressure by peace loving nations to isolate aggressors, short of war and short of naming one. Then teach the reception with equal care. He named no country, with Japan three months into its invasion of China, and proposed no measure at all, and still newspapers and members of Congress attacked the speech as a step toward war and isolationist organizations flooded the White House with protests. Roosevelt let the idea drop and did not return to it. The episode measures the strength of the neutrality case in 1937 better than any vote: even a metaphor was too much.",
             kick='D · A president pushes against the current', size=24)

# ------------------------------------------------------ 13 ARSENAL AND FREEDOMS
content_text('The arsenal, and the aims named',
             ['Fireside chats: the danger explained in plain language',
              'December 29, 1940: the great arsenal of democracy',
              'Arm Britain; stay out of the fighting itself',
              'January 6, 1941: the Four Freedoms named',
              'Speech, worship, freedom from want, freedom from fear'],
             "Two speeches carry this slide, and students should keep them distinct. The Arsenal of Democracy fireside chat of December 29, 1940, which the quick check quotes, assigns the United States a role: producer and supplier to the nations fighting aggression, with the effort treated as an emergency as serious as war itself, while America stays out of the fighting. A fireside chat, in the guided notes definition, is one of President Roosevelt's radio addresses to the nation, delivered in plain conversational language from the White House, and the format is part of the persuasion: a president in the living room, not a lecturer at a podium. The Four Freedoms address of January 6, 1941, then names what the aid defends: freedom of speech, freedom of worship, freedom from want, and freedom from fear, everywhere in the world. Note the geography in that phrase. These are not offered as American possessions but as the foundations of a just world, which is a claim about why a neutral country should care who wins.",
             kick='D · A president pushes against the current', size=24)

# ------------------------------------------------- 14 SECTION E DIVIDER
divider_photo('lendlease-port.jpg', 'Section E', 'The Fall of France and the Turn to Aid',
              ['American machine guns arrived in England', 'under Lend-Lease, checked at an ordnance depot.'],
              "The photograph shows water cooled machine guns just arrived from the United States under Lend-Lease, checked at an ordnance depot in England, from the National Archives record, number 196325. It belongs to 1941, and it shows the end of the process this section teaches: American weapons in British hands, delivered under a law that did not exist eighteen months earlier. Section E is the turn of the lesson, and it is driven by an event, not a speech. Germany overran France in six weeks in the spring of 1940, and Britain stood alone, short of ships, short of weapons, and running short of money. Every step in the section answers that emergency: cash-and-carry already in place from November 1939, destroyers for bases in September 1940, the first peacetime draft the same month, and Lend-Lease in March 1941 when the cash ran out. Teach the steps as a sequence with dates, because the activity asks students to judge each one separately.",
              title_size=34)

# ------------------------------------------------------ 15 FALL AND DESTROYERS
content_text('France falls, and the steps quicken',
             ['Germany overran France in six weeks, 1940',
              'Britain stood alone, short of ships and money',
              'September 1940: fifty destroyers for base leases',
              'The same month: the first peacetime draft',
              'A neutral country, raising an army'],
             "Slow down on the destroyers deal, because it was the boldest step yet and it was taken without Congress. In September 1940 Roosevelt transferred fifty aging American destroyers to Britain in exchange for leases on British bases from Newfoundland to South America, acting by executive agreement. The destroyers were old, and Britain needed them for convoy escort more than for battle, but the principle was new: American warships passed directly into a belligerent navy. The same month, Congress did act, passing the Selective Training and Service Act, the first peacetime draft in American history, so the country began building a mass army while formally at peace. Put the two steps together in the notes and ask the question the lesson keeps asking. A country does not raise a mass army and hand warships to a belligerent because it expects the quarrel to stay foreign. By the autumn of 1940 the United States was preparing for a war it still said it would not join.",
             kick='E · The fall of France and the turn to aid', size=24)

# ------------------------------------------------------ 16 DESTROYERS STAT
stat('50', 'aging American destroyers sent to Britain, September 1940',
     'Paid for in leases on British bases across the Atlantic · The first peacetime draft passed the same month',
     "Fifty is a small number beside the fleets of 1944, and students should understand why it carries a whole slide. The destroyers were a down payment measured in warships, and warships are not surplus goods: they were commissioned vessels of the United States Navy, crewed until transfer by American sailors, handed to a nation at war in the middle of its fight for survival at sea. The payment tells the same story from the other side. Britain paid not in cash it no longer had but in leases on bases from Newfoundland to South America, which tied American defense geography to British territory across the Atlantic and the Caribbean. Churchill called the deal a long step toward war, and the America First Committee agreed with the description while condemning the step. When both a policy's author and its sharpest critics describe it the same way, students should take the description seriously.",
     kick='E · The fall of France and the turn to aid')

# ------------------------------------------------------ 17 CASH TO LEND-LEASE
content_text('Cash-and-carry gives way to Lend-Lease',
             ['1939: pay cash, carry it in your own ships',
              'Only Britain, ruling the Atlantic, could use it',
              'By 1941 the cash was gone',
              'March 1941: lend or lease arms by presidential judgment',
              'The neutrality bars set aside for countries named vital'],
             "This slide is the legal hinge of the lesson, and the vocabulary definition carries it, so read the definition aloud: Lend-Lease is the law of March 1941 that let the president lend or lease arms and supplies to any country whose defense he judged vital to the defense of the United States. Compare it with the policy it replaced. Cash-and-carry, the policy adopted in 1939 that let nations at war buy American arms and goods if they paid cash and carried them away in their own ships, kept two conditions: money up front, and the buyer's own ships. Both conditions protected American neutrality in form. Lend-Lease removed both. The test was no longer cash but the president's judgment of what American defense required, and the act's operative section opens by setting other law aside: notwithstanding the provisions of any other law. Students read that language at Station 5. The Neutrality Acts were never repealed in a single dramatic vote. They were bypassed, by name, for any country the president chose.",
             kick='E · The fall of France and the turn to aid', size=24)

# ------------------------------------------------- 18 SECTION F DIVIDER
divider_photo('lindbergh-port.jpg', 'Section F', 'The Case for Staying Out',
              ['Charles Lindbergh, the America First', "Committee's best known speaker."],
              "The portrait of Charles Lindbergh is by Harris and Ewing, from the Library of Congress record. Section F states the opposition case, and the instruction for this section is fairness. The America First Committee, founded in September 1940, counted hundreds of thousands of members and included students, farmers, business leaders, and members of both parties. Its argument was not that Hitler was admirable. Its argument was about the United States: that two oceans made the country defensible at home, that aid short of war was a fiction that would end in convoys and shooting, and that a war entered step by step, without a vote on war itself, would be a democratic failure as well as a strategic one. Lindbergh, the most famous aviator alive after his 1927 Atlantic flight, was its best known speaker, and his charge that the administration moved toward war step by step deserves to be tested against the road students have just walked, not waved away.",
              title_size=38)

# ------------------------------------------------------ 19 AMERICA FIRST
content_text('Safe behind two oceans, and warned about the steps',
             ['Founded September 1940; hundreds of thousands of members',
              'The duty of the United States: defense at home',
              'Aid leads to convoys; convoys lead to shooting',
              'Shooting leads to a war the people never chose',
              'Lindbergh: each step presented as short of war'],
             "State the committee's case as a chain, because that is how the quick check and the writing task ask for it. First link: aid to Britain, however it is labeled, makes American ships and ports part of Britain's supply line. Second link: supplies worth sending are worth protecting, so aid leads to American convoys. Third link: convoys in a war zone lead to shooting, as any escort commander ordered to protect his charges will fire on the submarines hunting them. Fourth link: shooting leads to incidents, incidents to dead sailors, and dead sailors to a full war, entered without the country ever voting on war itself. Then note what the autumn of 1941 did to this argument, without crowing about it. The chain the committee predicted is close to the sequence the country lived: aid, escort duty toward Iceland, the Greer, the Kearny, and the Reuben James. Being right about the steps did not settle whether the steps should have been taken, and students should hold those two judgments apart.",
             kick='F · The case for staying out', size=24)

# ------------------------------------------------- 20 SECTION G DIVIDER
divider_photo('atlantic-port.jpg', 'Section G', 'The Charter and the Shots at Sea',
              ['Roosevelt and Churchill aboard', 'HMS Prince of Wales, August 1941.'],
              "The photograph is the title image in portrait form: Roosevelt and Churchill seated on the quarterdeck of HMS Prince of Wales during the Atlantic Conference of August 1941, Imperial War Museums, Admiralty Official Collection, A4816. Section G closes the lesson at the point where law and fact came furthest apart. In August 1941 the president of a neutral country crossed a war zone in secret, met the leader of a belligerent power aboard a battleship, and issued with him a joint statement of the aims the two countries would seek in the peace to come. No alliance was signed and no war was declared, and both facts belong in the notes. Then the section goes to sea, where American destroyers were already escorting convoys partway across the Atlantic and German submarines were already hunting them. The lesson ends there deliberately, with American sailors dead in an undeclared war, five weeks and more before Pearl Harbor.",
              title_size=38)

# ------------------------------------------------------ 21 CHARTER
content_text('A neutral president signs common aims',
             ['August 1941: the meeting off Newfoundland',
              'The Atlantic Charter: a joint statement of aims',
              'Self-determination for peoples',
              'Freer trade, and freedom of the seas',
              'No alliance signed; no war declared'],
             "Read the definition as the slide's core: the Atlantic Charter is the joint statement of aims issued by Roosevelt and Churchill in August 1941, pledging self-determination for peoples, freer trade, and freedom of the seas. Each pledge answers a piece of the war. Self-determination denied that conquest could redraw maps by force, which was Germany's program in Europe and Japan's in Asia. Freer trade named the closed economic blocs of the 1930s as one of the war's causes. Freedom of the seas restated the neutral trading right over which the United States had fought Britain in 1812 and argued with Germany in 1917. Then put the document in its odd legal position, which students should be able to state. It was not a treaty, it was not ratified, and the United States was not at war. It was a declaration of shared purposes between a belligerent and a neutral, and after August 1941 the word neutral described American law far better than it described American policy.",
             kick='G · The Charter and the shots at sea', size=24)

# ------------------------------------------------------ 22 SHOTS AT SEA
content_photo('reuben-port.jpg', 'Escorts, submarines, and a destroyer lost',
              ['American destroyers escorted convoys toward Iceland',
               'The Greer, September 1941: shots exchanged',
               'The Kearny, October: torpedoed, eleven killed',
               'October 31: the Reuben James sunk',
               '115 of her crew killed, in an undeclared war'],
              "The photograph shows the destroyer USS Reuben James on the Hudson River in April 1939, an official United States Navy photograph, NH 66333, from the Naval History and Heritage Command. Work the three incidents as an escalation, with dates. In September 1941 the Greer exchanged shots with a German submarine while carrying mail toward Iceland, and Roosevelt answered with a shoot on sight order for American escort vessels in waters he defined as defensive. In October the Kearny was torpedoed while defending a convoy and lost eleven men, the first American naval dead of a war the country had not declared. On October 31 the Reuben James was sunk while escorting a convoy, with 115 of her crew killed, the first United States warship lost in the Second World War, lost before the war in law had begun. Students should end the section able to state the lesson's closing sentence from the reading in their own words: the United States was arming one side and taking losses, while its laws still called it neutral.",
              kick='G · The Charter and the shots at sea')

# ------------------------------------------------------ 23 SYNTHESIS
content_text('Neutral in law, at war in fact',
             ['The laws of 1935 still stood on paper',
              'The practice of 1941 had left them behind',
              'Arms lent, aims shared, convoys escorted, sailors lost',
              'Next: December 7, 1941 settles the argument in a day'],
             "Close the teaching where the reading closes, with the two records held together. In law, the United States in November 1941 was a neutral nation: no declaration of war, no alliance, a neutrality framework built in the 1930s still standing. In fact, it was the arsenal of one side, bound to that side by a signed statement of aims, escorting its supply ships across half an ocean, and burying sailors killed by a navy it was not at war with. Neither half cancels the other, and strong student writing, which the writing task demands, keeps both in view and argues about which describes the country better. The next lesson begins on December 7, 1941, when Japan's attack on Pearl Harbor ended the argument in a day and Germany's declaration of war four days later settled the question of a one ocean war. Students should leave today able to explain why, by then, the country was debating entry into a war it was already half inside.",
             kick='G · The Charter and the shots at sea')

# ------------------------------------------------------ 24 VOCAB A
vocab('Words for the starting point',
      [('isolationism', 'a policy of avoiding political commitments and alliances with other countries'),
       ('Neutrality Acts', 'the 1930s laws that barred arms sales and loans to nations at war'),
       ('fireside chat', "one of Roosevelt's radio addresses to the nation, in plain conversational language"),
       ('cash-and-carry', 'the 1939 policy: pay cash, and carry purchases away in your own ships')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. isolationism: a policy of avoiding political commitments and alliances with other countries while keeping a country free to act on its own. Note that the definition describes freedom of action, not indifference: an isolationist country kept its hands free. Neutrality Acts: the laws passed by Congress in the 1930s that barred arms sales and loans to nations at war, written to keep the United States out of another world war. The purpose clause at the end is part of the definition and part of the test. fireside chat: one of President Roosevelt's radio addresses to the nation, delivered in plain conversational language from the White House. cash-and-carry: the policy adopted in 1939 that let nations at war buy American arms and goods if they paid cash and carried them away in their own ships. Both conditions belong in the definition, because both conditions did the policy's work.")

# ------------------------------------------------------ 25 VOCAB B
vocab('Words for the turn to aid',
      [('Lend-Lease', 'the March 1941 law letting the president lend or lease arms to countries vital to American defense'),
       ('Four Freedoms', 'speech, worship, freedom from want, and freedom from fear'),
       ('Atlantic Charter', 'the August 1941 joint statement of aims with Churchill')],
      "Three more terms, again matching the guided notes exactly. Lend-Lease: the law of March 1941 that let the president lend or lease arms and supplies to any country whose defense he judged vital to the defense of the United States. The judging phrase is the heart of it: Congress handed the choice of recipients to the president, country by country. Four Freedoms: the four freedoms Roosevelt named in his annual message of January 6, 1941 as the foundations of a just world: freedom of speech, freedom of worship, freedom from want, and freedom from fear. Students should be able to list the four in order and say where each one points: speech and worship to political liberty, want to economic security, and fear to a disarmed peace. Atlantic Charter: the joint statement of aims issued by Roosevelt and Churchill in August 1941, pledging self-determination for peoples, freer trade, and freedom of the seas. Three pledges, three answers to the war's causes, and students should pair them that way in the notes.")

# ------------------------------------------------------ 26 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Judge the road', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Between 1935 and 1941, how did the United States move from legislated neutrality toward war without declaring it? Walk the road in order, then mark the decisive step.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Road in Ten Steps: a neutrality law, the Nye charge, the Quarantine speech, the turn to aid, Lend-Lease and its critics'),
        ('Notebook', 'Notebook page: six steps of the road, judged and evidenced'),
        ('Quick check', 'The Arsenal and the Law: the fireside chat against the neutrality framework'),
        ('Writing', 'Neutral in Law, at War in Fact?: the closing question of the lesson as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: what the Neutrality Acts were written to do, cash-and-carry against Lend-Lease, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Road in Ten Steps, runs five stations through the evidence: the 1935 act's own text, a labeled summary of the Nye charge, the Quarantine passage from the audited record, a labeled summary of the fall of France and destroyers for bases, and the Lend-Lease text answered by the America First case, ending in a ten step table where students judge each step toward war, holding back, or both, and mark the decisive one. The notebook page asks students to rebuild six steps of the road with their evidence. The quick check, The Arsenal and the Law, tests the fireside chat passage against the neutrality framework and tags every item to the blueprint. The writing task, Neutral in Law, at War in Fact?, turns the closing question into an essay. The exit ticket has three parts: what the acts were written to do with two bars named; the difference between cash-and-carry and Lend-Lease; and the lesson question in two or three sentences with two facts. Next lesson takes up Pearl Harbor.")

dc.save(OUT)
