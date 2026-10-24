#!/usr/bin/env python3
"""Jackson and Reform Lesson 1 deck, "The Election of 1828 and Jacksonian Democracy,"
built to the approved system: image-led slides, fragments only on screen,
comprehensive speaker notes, full lesson + vocabulary coverage.
Fonts: Georgia titles, Lato body."""
import os, sys, json
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
N = {
1: "The image is Robert Cruikshank's print of 1829, The President's Levee, or All Creation Going to the White House, held by the Library of Congress. It shows the crowd of inauguration day pressing toward the president's house, men and women of every dress and condition drawn as a satire by a hostile hand. Hold it in front of students and ask who these people thought the house belonged to. The lesson answers that question in order. The states first remade the electorate by striking down property limits on white men's voting. The election of 1824 supplied a grievance, the campaign of 1828 a mass party, and the First Annual Message a doctrine of office. The limits were drawn in the same years, and the lesson never lets them out of the frame.",
2: "Read the question slowly, because its two halves are the whole lesson. The first half asks what changed when the common white man got the vote: the vote left property behind, turnout became the test of a campaign, parties built committees and newspapers to reach men never courted before, and the president those voters chose declared that office itself should rotate among citizens. The second half asks who was still left outside: women everywhere, free Black men losing ballots they had cast, Native nations outside the polity, and the enslaved people of the president's own plantation. Students should hear both halves before any content, because every section that follows belongs to one half or holds the two together. Keep the question visible as the lesson moves, and return to it at the close.",
3: "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A gives the electorate remade before the candidate, state by state. Section B gives the doors that closed as others opened, in New Jersey, New York, and Pennsylvania. Section C gives the election of 1824 and the corrupt bargain charge. Section D gives the campaign of 1828 and the attacks on Rachel Jackson. Section E gives the inauguration in Margaret Bayard Smith's two scenes. Section F gives rotation in office and the spoils. Section G closes with the party formed and the limits stated whole. Tell students the letters are their filing system for everything that follows today.",
4: "Begin before Jackson, because the lesson's first claim is that the electorate made the candidate possible, not the other way round. In the early republic a vote was tied to a freehold or a tax receipt, on the stated theory that a man without a stake in the community could be bought or commanded by the man who employed him. Ask students what that theory assumes about the poor man's judgment, and let them say it plainly before you tell them the states abandoned it. Between the 1810s and 1828 the property tests fell in one state after another, and by the time Jackson ran his second campaign, nearly every white man in the country could cast a ballot. The section that follows names the states and the years where the change can be dated.",
5: "Work the fragments as a sequence, because sequence is the argument. New states came into the union with white manhood suffrage in their constitutions, Indiana, Illinois, Alabama among them, and voters there never knew a property test. Older states then rewrote their own rules rather than be outvoted in reputation: Connecticut in 1818, Massachusetts in 1820, and New York, the largest state, removing its property test for white men in 1821 and completing the change in 1826. Teach the direction of travel: suffrage widened from the frontier inward. By 1828 the tests survived for white men in only a few states, Rhode Island, Virginia, and Louisiana among them, and the exception had become the oddity. Students should copy the state and year pairs into section A of their notes.",
6: "A wider electorate is only paper until somebody organizes it, and organizing is the craft this section names. County committees kept lists of voters and saw them to the polls. Party newspapers, printed cheap and passed hand to hand, carried one version of events into taverns and workshops. Rallies, barbecues, and parades made politics a public season rather than a courthouse errand. Teach students to connect the machinery to the man: Jackson's fame from New Orleans gave the organization a name every voter already knew, and the organization gave the fame a way to become ballots. Neither half wins 1828 alone. The next slide puts a number on what the machinery delivered. The machinery was partisan from its first day, and both parties built it.",
7: "Let the comparison carry the section. Turnout in the presidential election of 1828 ran near three times the turnout of 1824, the standard comparison historians use for the arrival of mass politics in the United States. The figure is a ratio, not a count, because the two elections are the cleanest before and after the suffrage changes and the organizing that followed them. Ask students what had to be true on the ground for three times as many ballots to be cast: more men eligible, more men reached, more men carried to a poll. Each answer names a piece of section A. Then set the limit beside the number before leaving it: the tripled turnout was a turnout of white men, and section B begins exactly there.",
8: "Section B is the counterweight, and it should be taught at the same weight as section A, not as a footnote to it. The claim is precise: the exclusions of this era were not leftovers waiting for a later generation to clear away. They were enacted, in statutes and constitutions, by the same generation that widened the white vote, sometimes in the same document that widened it. New York's convention of 1821 freed the white man's vote and fenced the Black man's in the same settlement. Teach students to hold the two motions in one hand, widening and narrowing, because the unit's essential question cannot be answered from either motion alone. Nothing in this section is an afterthought, and it should not be taught as one.",
9: "Work the three cases in date order. New Jersey is the strangest and the most instructive: its constitution of 1776 gave the vote to all inhabitants worth fifty pounds, and for thirty years some women and some free Black men voted under it, until a disputed election gave the legislature its occasion and the law of 1807 limited the vote to free white male citizens. New York in 1821 removed the property test for white men and set a property test for free Black men alone, two hundred fifty dollars in a freehold. Pennsylvania closed the sequence in 1838, writing the word white before freemen in a new constitution. Native nations were never in the count at all: their peoples stood outside the polity as members of separate nations.",
10: "Pause on the year, because 1807 teaches the direction of the era better than any summary. This was not the founding generation's oversight surviving into a more generous age. In 1807 the age was already generous to white men, and New Jersey's legislature used a modern law to take ballots away from neighbors who had cast them within living memory, women who held property in their own names among them. The closing was deliberate, public, and contested at the time. Students sometimes ask when Americans began arguing about who the people were. This lesson's answer is that the argument was never absent: it ran alongside every widening, and the wideners and the closers were frequently the same voters in the same decade.",
11: "The portrait is Mathew Brady's photograph of Henry Clay, taken about 1849, two decades after the events of this section, and it is worth saying so to students: our clearest likeness of Clay comes from the end of his life. Section C begins with the election of 1824, in which four candidates divided the country and its electoral vote. Jackson's grievance was real in its facts and unproven in its charge, and students must learn to hold those two judgments separately. The sequence on the next slide is the documented record, established from the returns and the House journal, and no part of it depends on what any man intended. What Clay intended is unknowable, and the lesson teaches only what he did.",
12: "Teach the figures as the House saw them. Jackson took 99 electoral votes, Adams 84, Crawford 41, and Clay 37, and no man held the majority of 131 the Constitution requires. The contest moved to the House of Representatives, where each state delegation cast one vote and only the top three finishers stood, which put Clay, the Speaker of the House, out of the contest and in command of its outcome. Clay declared for Adams, whose views on government he shared and whose rival he distrusted, and on February 9, 1825, the House elected Adams with thirteen state delegations. In March, Adams named Clay secretary of state. Every step was constitutional. That is what made the charge that followed so durable: the people had watched the forms of the Constitution overturn the first place finisher.",
13: "Now separate the record from the charge, because the whole lesson turns on the separation. The charge, cried in Jackson newspapers for four years, was that Clay had sold his support in advance for the secretaryship, the office then read as the stepping stone to the presidency. Both men denied any bargain. No letter, witness, or admission has ever established one, and historians teach the episode with the charge labeled a charge. Then ask why an unproven charge outperformed the documented record. It fit what the new voters could see: a plurality winner set aside in Washington rooms. The corrupt bargain was truer to the new politics than to the facts, and it built the party that won 1828. That gap between charge and proof is the habit of mind the whole unit practices.",
14: "The portrait is Ralph Earl's Rachel Jackson, painted in the years of her husband's rise, showing the woman the campaign of 1828 would put at the center of its hardest attacks. Section D treats the campaign as the new politics practiced without restraint: organization and spectacle on one side of the ledger, personal destruction on the other. Rachel Donelson's first marriage had ended in a tangled divorce, final only after she and Jackson had married believing her free, and the couple remarried once the decree was certain. Adams newspapers revived the story in 1828 in its ugliest form. Teach the episode soberly and exactly, because its consequence belongs on the next slide. Jackson never forgave the men he blamed, and he said so for the rest of his life.",
15: "Work the campaign as two inventories. The organization: committees in counties and towns, hickory poles planted in squares for Old Hickory, barbecues and parades that made voting a festival, and a party press that printed the general as the people's candidate and the administration as a corrupt circle. The mud: coffin handbills listing men Jackson had executed or killed, attacks on his temper and his duels from the Adams side, and from both sides a willingness to print what a later age would call private. The result was a wide Jackson victory in the popular vote and the Electoral College. Then give the cost its own sentence. Rachel Jackson died in December 1828, weeks after the voting, and her husband went to Washington a widower who believed the attacks had killed her.",
16: "The image is the portrait crop of Cruikshank's President's Levee print, the crowd pressing on the White House. Section E is built on one witness, Margaret Bayard Smith, a leader of Washington society who had known every administration since Jefferson's and wrote her account in a letter of March 1829, preserved in The First Forty Years of Washington Society, published in 1906 under Gaillard Hunt's editorship. Smith gives the lesson two scenes from a single day, the crowd at the Capitol and the crowd in the president's house, and readers have quoted whichever scene suited them ever since. Teach the two scenes as one account by one observer, because the tension inside the letter is its evidence. Her letter survives because her family papers were published three generations later.",
17: "Take the scenes in Smith's order. At the Capitol she saw thousands and thousands of people, without distinction of rank, collected in an immense mass, silent, orderly and tranquil, waiting for the president in the portico, and she called the sight sublime. At the White House reception the same people pressed after Jackson through the rooms, broke cut glass and china worth thousands of dollars in the scramble for refreshments, and drove the president out a back way to his lodgings at Gadsby's. Smith's sentence for the second scene is the one students must weigh: the Majesty of the People had disappeared, and a rabble, a mob, had taken its place. Then read her closing sentence aloud: it was the People's day, and the People's President and the People would rule. Smith feared and recorded the same fact.",
18: "The portrait is Thomas Sully's Andrew Jackson, the president the First Annual Message introduces in his own words. Section F takes up the doctrine Jackson laid before Congress on December 8, 1829, and its text is in the activity as Station 1, quoted from Richardson's Messages and Papers of the Presidents. The doctrine answers a question the election had posed: if the people rule, why should the government's offices stay filled by the men of the last administration and the last generation? Jackson's answer was rotation: offices are public trusts, not property, and they should pass among citizens the way the vote itself had passed beyond the propertied few. The next slide gives the argument in its own order. The doctrine also suited the party's needs, and students may note both truths together.",
19: "Quote the argument's three steps. First, long officeholding corrupts the holder's relation to the public: few men, Jackson wrote, can enjoy office and power for long without looking with indifference on the public interest, until office is considered as a species of property. Second, the work does not require a permanent class: the duties of public officers are so plain and simple that men of intelligence may readily qualify themselves for their performance. Third, the balance favors rotation: more is lost by the long continuance of men in office than is gained by their experience. His proposal followed the argument: extend the law limiting appointments to four years. Students should notice the form: a democratic premise about office, argued as policy, addressed to Congress.",
20: "Let the count correct the legend in both directions. The removals of Jackson's first years came to some nine hundred of roughly nine thousand federal civil officers by the usual count, about one officeholder in ten, postmasters making up most of the number. That is far less than the sweeping purge the phrase spoils system suggests, and students should say so. It is also nine hundred livelihoods and nine hundred appointments, enough to establish the principle that a change of administration changes the officers. The name came from the other side: Senator William Marcy of New York, defending the practice in 1832, said the victors saw nothing wrong in the rule that to the victor belong the spoils, and opponents made the phrase the system's permanent title.",
21: "Section G gathers the lesson into its final shape. Out of the campaign of 1828 the Democratic Party took lasting form, joining southern planters, western farmers, and northern workingmen in one organization behind white manhood suffrage, strict limits on federal power, and suspicion of banks and chartered privilege. It was the first American party built to win a mass white electorate, and its machinery outlasted its founder. Set the founder inside his own limits before the synthesis: Jackson was a Tennessee cotton planter whose Hermitage wealth rested on enslaved labor, a slaveholder carried to power by a movement preaching the equality of white men. The era's democracy and its exclusions had the same address. The synthesis on the next slide answers in the same two columns as the question.",
22: "Build the synthesis as the answer to the lesson question, in the question's own order. What changed: the vote was uncoupled from property for white men, turnout and organization became the currency of politics, a plurality grievance from 1824 became a governing party, and the president that party elected declared office itself a trust to rotate among citizens rather than a property to keep. Who was left outside: women in every state, free Black men stripped of ballots in New Jersey and Pennsylvania and fenced in New York, Native nations outside the polity altogether, and the enslaved people whose labor supported the president's own house. Hold both columns up together and do not let either one fall. Neither column is the lesson alone, and students should be marked on holding both.",
23: "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. Andrew Jackson: the Tennessee general and seventh president, hero of New Orleans and victor in the elections of 1828 and 1832, whose presidency widened white men's democracy while it removed Native nations, broke the national bank, and strengthened the presidency itself. Jacksonian democracy: the political movement of the 1820s and 1830s that celebrated the common white man, widened the vote, attacked privileged institutions such as the national bank, and held that the president, chosen by the majority, should govern energetically in the people's name. corrupt bargain: the charge Jackson's supporters leveled at the election of 1824, that Henry Clay threw the House of Representatives vote to John Quincy Adams in return for appointment as secretary of state, a charge both men denied and Jacksonians rode to victory in 1828.",
24: "Four more terms, again matching the guided notes exactly, and students should copy them as written. suffrage: the right to vote, which state after state extended in the 1820s until nearly every white man could vote regardless of property, while women, Native Americans, and most free Black men remained excluded. spoils system: the practice of filling government offices with the winning side's supporters, named by Jackson's opponents for the claim that to the victor belong the spoils, and defended by Jacksonians as rotation that kept office from hardening into property. rotation in office: Jackson's doctrine that public offices should pass regularly from citizen to citizen rather than become the possession of a permanent officeholding class, which he argued no man had any more right to hold than another. Democratic Party: the party that formed around Andrew Jackson out of the election of 1828, joining southern planters, western farmers, and northern workingmen behind white manhood suffrage, strict limits on federal power, and suspicion of banks and chartered privilege.",
25: "Close by returning to the lesson question and handing the lesson to the work. The activity, The People's President File, runs five stations through the evidence: the First Annual Message, Smith's inauguration letter, the widening suffrage summary, the corrupt bargain record, and the exclusion record of 1807 and 1838, ending in a ledger of standing gained and lost and a verdict on whether 1828 deserves its name as the birth of democratic politics in America. The notebook page asks students to rebuild six pieces of the story with evidence. The quick check tests the First Annual Message passage against its background. The writing task weighs the widening against the boundary and closes on Smith's sentence. The exit ticket has three parts: the suffrage change stated in one sentence; the bargain charge explained as unproven and decisive; and the lesson question answered with the change, the doctrine, and two groups left outside."
}

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
text(s, 0.9, 5.32, 11.5, 0.4, 'JACKSON AND REFORM · LESSON 1', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Election of 1828 and Jacksonian Democracy', size=36, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'The electorate remade, the bargain charged, and the people let in, 1824 to 1829', size=17, color=POWDER)
notes(s, N[1])

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("What changed when the common white man got the vote, and who was still left outside it?", {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ("What did democracy mean in Jackson's America, who was it for, and what did the era's reformers claim it still owed?", {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, N[2])

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'A new electorate and its boundaries, in seven stretches', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The electorate remade', 'Property tests fall, white manhood suffrage rises'),
        ('B', 'The doors that closed', 'New Jersey 1807, New York 1821, Pennsylvania 1838'),
        ('C', '1824 and the corrupt bargain', 'A House decision and a four year charge'),
        ('D', 'The campaign of 1828', 'Committees, barbecues, and the attacks on Rachel'),
        ('E', 'The inauguration as portrait', "Smith's two crowds on one day"),
        ('F', 'Rotation and the spoils', 'Office is not property, the president argues'),
        ('G', 'A wider democracy, and its limits', 'A party formed, a boundary held')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, N[3])

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', 'The Electorate Remade Before the Candidate',
             'The vote changed first. The candidate came second.',
             N[4])
# ------------------------------------------------------ 5 SUFFRAGE FALLS
content_text('The property tests fall, state by state',
             ['New states entered with white manhood suffrage.',
              'Connecticut acted in 1818 and Massachusetts in 1820.',
              'New York removed its test for white men in 1821.',
              'By 1828 the tests survived in only a few states.'],
             N[5], kick='A · The electorate remade', size=24)
# ------------------------------------------------------ 6 ORGANIZING
content_text('Parties learn to organize the new voters',
             ['County committees kept the lists.',
              'Party newspapers were passed hand to hand.',
              'Barbecues, parades, and hickory poles filled the season.',
              'Turnout became the measure of a campaign.'],
             N[6], kick='A · The electorate remade', size=24)
# ------------------------------------------------------ 7 TURNOUT STAT
stat('3x', 'the turnout of 1828 measured against the turnout of 1824',
     'More men eligible · More men reached · More men carried to the polls',
     N[7], kick='A · The electorate remade')
# ------------------------------------------------- 8 SECTION B DIVIDER
divider_text('Section B', 'The Doors That Closed as Others Opened',
             'The exclusions were enacted in the same decades as the widening.',
             N[8])
# ------------------------------------------------------ 9 THREE CASES
content_text('Three closings, in date order',
             ['In 1807 New Jersey closed the vote to white men only.',
              'In 1821 New York set a property test for Black men alone.',
              'In 1838 Pennsylvania wrote white before freemen.',
              'Native nations stood outside the polity entirely.'],
             N[9], kick='B · The doors that closed', size=24)
# ------------------------------------------------------ 10 1807 STAT
stat('1807', 'the year New Jersey took the vote from people who had cast it',
     'Women and free Black men had voted under the constitution of 1776 for thirty years',
     N[10], kick='B · The doors that closed')
# ------------------------------------------------- 11 SECTION C DIVIDER
divider_photo('clay-port.jpg', 'Section C', '1824 and the Cry of Corrupt Bargain',
              ['Mathew Brady photograph of Henry Clay,', 'taken about 1849, late in his life.'],
              N[11])
# ------------------------------------------------------ 12 1824 SEQUENCE
content_text('First in the votes, short of a majority',
             ['Jackson took 99 electoral votes, and Adams took 84.',
              'With no majority, the House chose, voting by state.',
              'Clay, fourth and out, backed Adams.',
              'Adams was elected on February 9, 1825.',
              'Clay was named secretary of state in March.'],
             N[12], kick='C · 1824 and the bargain', size=24)
# ------------------------------------------------------ 13 CHARGE VS RECORD
content_text('The record and the charge are different things',
             ['Documented were the returns, the House vote, and the appointment.',
              'Charged was that the office was promised for the support.',
              'The charge was denied by both men and never proven.',
              'Jacksonians rode it to victory in 1828.'],
             N[13], kick='C · 1824 and the bargain', size=24)
# ------------------------------------------------- 14 SECTION D DIVIDER
divider_photo('rachel-port.jpg', 'Section D', 'The Campaign of 1828',
              ["Ralph Earl's portrait of Rachel Jackson,", "the campaign's hardest target."],
              N[14])
# ------------------------------------------------------ 15 CAMPAIGN
content_text('The new politics, in the open and in the mud',
             ['Committees, barbecues, and hickory poles organized the campaign.',
              'A party press praised the people’s candidate.',
              'Coffin handbills and duels came from the other side.',
              'Rachel was attacked in print over her first marriage.',
              'Jackson won wide, and Rachel died in December.'],
             N[15], kick='D · The campaign of 1828', size=24)
# ------------------------------------------------- 16 SECTION E DIVIDER
divider_photo('levee-port.jpg', 'Section E', 'The Inauguration as Portrait',
              ["Cruikshank's President's Levee print of 1829:", 'all creation going to the White House.'],
              N[16])
# ------------------------------------------------------ 17 TWO SCENES
content_text("Smith's two crowds on one day",
             ['At the Capitol the crowd was silent, orderly, and tranquil.',
              'It gathered without distinction of rank, in an immense mass.',
              'At the White House, glass and china were broken.',
              'The president was driven out a back way.',
              'Her close was that the People would rule.'],
             N[17], kick='E · The inauguration', size=24)
# ------------------------------------------------- 18 SECTION F DIVIDER
divider_photo('jackson-port.jpg', 'Section F', 'Rotation in Office and the Spoils',
              ["Thomas Sully's portrait of Andrew Jackson,", 'the seventh president.'],
              N[18])
# ------------------------------------------------------ 19 DOCTRINE
content_text('Office is not property',
             ['Long office bred indifference to the public.',
              'The duties were plain and simple to learn.',
              'More was lost by continuance than was gained.',
              'His proposal limited appointments to four years.'],
             N[19], kick='F · Rotation and the spoils', size=24)
# ------------------------------------------------------ 20 900 STAT
stat('900', 'officers removed out of some 9,000 in the first years',
     'Modest beside the legend · Enough to establish the principle of rotation',
     N[20], kick='F · Rotation and the spoils')
# ------------------------------------------------- 21 SECTION G DIVIDER
divider_text('Section G', 'A Wider Democracy, and Its Limits',
             'A party takes lasting shape, and its hero holds enslaved people.',
             N[21])
# ------------------------------------------------------ 22 SYNTHESIS
content_text('Changed, and left outside',
             ['The vote was uncoupled from property.',
              'A mass party and a doctrine of rotation took shape.',
              'Left outside were women, free Black men, and Native nations.',
              'Left outside were the enslaved people of the Hermitage.'],
             N[22], kick='G · A wider democracy, and its limits')
# ------------------------------------------------------ 23 VOCAB A
vocab('The general, the movement, the charge',
      [('Andrew Jackson', 'the Tennessee general and seventh president'),
       ('Jacksonian democracy', 'the movement of the common white man'),
       ('corrupt bargain', 'the charge carried from 1824 to 1828')],
      N[23])
# ------------------------------------------------------ 24 VOCAB B
vocab('The vote, the system, the doctrine, the party',
      [('suffrage', 'the right to vote, widened for white men'),
       ('spoils system', "the opponents' name for filling offices"),
       ('rotation in office', "Jackson's doctrine of office in turn"),
       ('Democratic Party', 'the party formed around Jackson in 1828')],
      N[24])
# ------------------------------------------------------ 25 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, "The people's president file", size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ["For each record, state who gained standing in the people's democracy and who lost it or was left outside it. Then judge whether 1828 deserves its name as the birth of democratic politics in America."],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', "The People's President File: the message, the letter, the suffrage, the bargain, the exclusion"),
        ('Notebook', 'Notebook page: six pieces of the story, classified and evidenced'),
        ('Quick check', 'Office Is Not Property: the message read against its background'),
        ('Writing', 'The Birth of Democratic Politics? The widening weighed against the boundary')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the suffrage change in one sentence, the bargain charge explained, and the lesson question answered with the doctrine and two groups outside.',
     size=15, color=POWDER)
notes(s, N[25])

for i, n in N.items():
    c = len(n.split())
    print(i, c)
dc.save(OUT)
