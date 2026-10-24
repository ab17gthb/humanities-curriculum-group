#!/usr/bin/env python3
"""Modern America Lesson 6 deck, "September 11 and the War on Terror,"
built on the shared deck system: image-led slides, fragments only on screen,
comprehensive speaker notes, full lesson and vocabulary coverage."""
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
OUT = os.path.join(HERE, '..', 'lesson-06-slides.pptx')

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

# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'MODERN AMERICA · LESSON 6', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'September 11 and the War on Terror', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'The attacks, the doctrine, two wars, and the state built at home', size=17, color=POWDER)
notes(s, "The photograph is an aerial view of the World Trade Center site after the attacks, with the ruins of 6 World Trade Center, the United States Custom House, in the foreground, photographed by James Tourtellotte of the United States Customs and Border Protection. Open with the register this lesson requires: documentary and plain, with nothing heightened. Nineteen hijackers, four planes, 2,977 people killed, and then a government that rebuilt its powers at home and went to war twice abroad. Students will work from documents all hour: a commission report, a presidential address, two statutes, and the findings of the government's own weapons inspectors. State the rule of the lesson now. Every claim is attached to its maker, the administration said, the Commission found, critics charged, because these events are recent and the argument over them is still running.")

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did the attacks of September 11, 2001 change what the American government did abroad and at home, and what did Americans argue about the changes?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the United States remake itself after 1980, in its economy, its population, and its place in the world, and what did the remaking settle and what did it leave open?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Read the lesson question aloud and separate its two halves before the first section begins. The first half asks what changed. Abroad, the government announced a doctrine within nine days, won from Congress the broadest war authorization in its history, and fought two wars, one of which ran for twenty years. At home, it built a new cabinet department out of twenty two agencies, federalized airport security, and widened its powers of surveillance, search, and detention. The second half asks what Americans argued about the changes, and that argument never closed. Officials who built the new machinery called the powers necessary. Critics answered that one war rested on a claim the record did not support and that the powers reached further than safety required. The unit question runs beneath as the frame for the whole unit.")

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'One day, and the decade it made', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The day: September 11, 2001', 'Nineteen hijackers, 2,977 killed'),
        ('B', 'The president\u2019s answer', 'A rule that night, a doctrine in nine days'),
        ('C', 'The legal architecture', 'The AUMF and the PATRIOT Act in five weeks'),
        ('D', 'Afghanistan: the first war', 'A regime falls in weeks, a war runs for years'),
        ('E', 'Iraq: the second war', 'A claim made, and no stockpiles found'),
        ('F', 'The state built at home', 'A new department, wider powers'),
        ('G', 'The judgment and the argument', 'Failures named in 2004, an argument still running')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A states the day in the Commission's terms. Section B gives the president's answer, the sentence of September 11 and the doctrine of September 20. Section C covers the legal architecture Congress built in five weeks. Sections D and E take the two wars in sequence, the first following the doctrine directly, the second resting on a claim. Section F covers the state built at home, the department and the powers. Section G delivers the Commission's judgment and states the standing argument with both sides documented. Tell students the summary table at the end of their guided notes, The Response at a Glance, asks them to rebuild exactly this map.")

# 4 A DIVIDER
divider_photo('pentagon-port.jpg', 'Section A', 'The Day: September 11, 2001',
              ['The collapsed section of the Pentagon,', 'photographed on the day of the attack.'],
              "The photograph shows the collapsed western section of the Pentagon on September 11, 2001, in a United States Navy photograph by Photographer's Mate 2nd Class Bob Houlihan. Section A states the day plainly, in the terms the 9/11 Commission set, because everything else in the lesson is an answer to this morning. Four airliners were hijacked by nineteen men of the al Qaeda network. Two were flown into the twin towers of the World Trade Center, and both towers collapsed. One struck the Pentagon, the building in this photograph. The fourth crashed in a field near Shanksville, Pennsylvania, after its passengers fought the hijackers for the controls. Teach the facts in that order and at that pace. The lesson will not use images of the attacks themselves or of victims, and it does not need them; the documented record carries the weight.",
              title_size=38)

# 5 A CONTENT
content_text('Four planes, three targets',
             ['Nineteen hijackers seized four airliners.',
              'Two planes were flown into the World Trade Center.',
              'One plane struck the Pentagon.',
              'The fourth plane crashed in a Pennsylvania field.',
              'The attacks killed 2,977 people.'],
             "Work the sequence once, completely, and then do not return to it; the lesson is about what the day set in motion. The hijackers belonged to al Qaeda, the network led by Osama bin Laden, built from veterans of the war against the Soviet Union in Afghanistan. In New York, both towers collapsed into the streets, killing office workers, passengers, and the firefighters and police who had climbed to reach them. At the Pentagon, the attack struck the headquarters of the Department of Defense. In Pennsylvania, the passengers of the fourth plane, having learned by telephone what had happened in New York, fought the hijackers, and the plane crashed in a field near Shanksville. The bipartisan commission Congress created to investigate opened its account in two sentences students should copy: a day of unprecedented shock and suffering, and a nation unprepared.",
             kick='A · The day', size=24)

# 6 A STAT
stat('2,977', 'people killed in the attacks of September 11, 2001',
     'The worst attack on American soil in the nation\u2019s history',
     "Let the number stand before anything is built on it. The 2,977 were passengers and crew on the four planes, workers in the towers and the Pentagon, and the firefighters, police officers, and paramedics who answered the attack. The figure does not include the nineteen hijackers. Students will meet this number again in the definition of the September 11 attacks in their key terms, and it should stay attached to people rather than to strategy: every structure the lesson then describes, the doctrine, the laws, the wars, the department, was built by a government answering a morning on which 2,977 people were killed. The Commission's word for the country's condition that morning was unprepared, and section G will return to its judgment of why. For now, have the toll and the four destinations written in section A of the notes.",
     kick='A · The day')

# 7 B DIVIDER
divider_photo('bush-port.jpg', 'Section B', 'The President\u2019s Answer',
              ['President Bush greets rescue personnel', 'at the World Trade Center site, September 14, 2001.'],
              "The photograph shows President George W. Bush greeting firefighters, police, and rescue personnel at the World Trade Center site on September 14, 2001, three days after the attacks, from the Records of the White House Photo Office at the National Archives. It belongs in section B because the American answer began as presidential speech before it became law or war. On the night of September 11, the president addressed the nation from the Oval Office and stated the rule that would govern everything after. Three days later he stood at the site in this photograph and spoke to the rescue workers through a bullhorn. Section B studies the words in order: the address of the night itself, and then the address to Congress nine days later, where the doctrine was set out in full and the demands on Afghanistan's Taliban government were named.",
              title_size=40)

# 8 B CONTENT
content_text('No distinction',
             ['The president addressed the nation on the night of the attacks.',
              'He promised no distinction between the terrorists and those who harbored them.',
              'On September 20 he set out the doctrine in full.',
              'The Taliban were told to surrender al Qaeda\u2019s leaders.',
              'Every nation was told to choose.'],
             "Quote the sentence exactly and make students hear its reach: we will make no distinction between the terrorists who committed these acts and those who harbor them. In one sentence the enemy grew from nineteen hijackers and one network to any government that sheltered them. On September 20, addressing a joint session of Congress, the president demanded that Afghanistan's Taliban government hand over al Qaeda's leaders and close its camps, and told every nation it faced a choice between standing with the United States and standing with the terrorists. The campaign took the name the War on Terror. Note for students that the September 20 address survives in the source bank as an audio record and is named in this lesson, not quoted as text; the rule itself was already stated, in the words above, on the night of the attacks.",
             kick='B · The president\u2019s answer', size=24)

# 9 C DIVIDER
divider_text('Section C', 'The Legal Architecture',
             'Two laws in five weeks: one page for war, one statute for the powers at home.',
             "Between the doctrine and the wars stands the law, and Congress built it at a speed students should register as part of the evidence. The Authorization for Use of Military Force was approved on September 18, one week after the attacks, on votes of 98 to 0 and 420 to 1. The USA PATRIOT Act was signed on October 26, six weeks after the attacks, having passed the Senate 98 to 1. Between them, the two laws supplied the legal foundation for the wars abroad and the security powers at home, and lawyers and presidents argued from their texts for the next twenty years. Section C takes them one at a time: first the war authorization and the question of who decides its targets, then the powers statute and the declaration Congress wrote inside it about the rights of Arab and Muslim Americans.")

# 10 C CONTENT
content_text('The Authorization for Use of Military Force',
             ['Congress passed the authorization on September 18, 2001.',
              'It granted all necessary and appropriate force.',
              'Its targets were nations, organizations, or persons.',
              'The president determines the connection to the attacks.',
              'The Senate voted 98 to 0 and the House 420 to 1.'],
             "Read the operative sentence the way the activity will ask students to read it. The president is authorized to use all necessary and appropriate force against those nations, organizations, or persons he determines planned, authorized, committed, or aided the terrorist attacks of September 11, 2001, or harbored such organizations or persons. Two words carry the breadth: he determines. Congress did not list the targets; it described them and handed the determination to the president, in order to prevent future attacks by those responsible. The same text carries the limit its writers pointed to: the force is tied to the September 11 attacks, and the resolution expressly preserves the requirements of the War Powers Resolution. Every later argument over the law's reach, including its use against groups that did not exist in 2001, is an argument between those two features of this one page.",
             kick='C · The legal architecture', size=24)

# 11 C STAT
stat('1', 'vote against the Authorization for Use of Military Force in either house of Congress',
     'House 420 to 1 · Senate 98 to 0 · Representative Barbara Lee of California cast the opposing vote',
     "Five hundred eighteen members of Congress voted on the authorization, and one voted no. Representative Barbara Lee of California explained her vote on the floor by warning against an open ended war granted in grief and haste, and she was answered at the time by colleagues who held that the country could not wait to name its enemy more narrowly. Have students hold the two numbers together, because the near unanimity is itself evidence about the weeks after the attacks: a Congress of two parties, which agreed on little else that year, agreed on this text almost without dissent. The statute's later critics did not claim it was smuggled through; they argued about what so broad a grant, passed so fast, had actually authorized. That argument is section G's inheritance, and question writers ever since have used these votes as the measure of the moment.",
     kick='C · The legal architecture')

# 12 C CONTENT 2
content_text('The PATRIOT Act, and the section inside it',
             ['The act was signed on October 26, 2001.',
              'Surveillance, search, and detention powers were widened.',
              'The Senate approved it 98 to 1.',
              'Section 102 stands inside the same statute.',
              'It declares that civil rights and civil liberties must be protected.'],
             "The second law worked at home. The USA PATRIOT Act widened the government's powers of surveillance, search, and detention in terrorism investigations, and it moved at the same speed as the authorization: Senator Russ Feingold of Wisconsin cast the Senate's only vote against it. Then slow down on the feature students least expect. The same statute carries Section 102, a sense of Congress condemning discrimination against Arab and Muslim Americans. Its findings state that Arab Americans, Muslim Americans, and Americans from South Asia are entitled to the full rights of every American, that individual responsibility for wrongdoing is sacrosanct, and that the civil rights and civil liberties of all Americans must be protected. A sense of Congress enforces nothing, and the activity will ask students to weigh exactly that: a declared standard, written into a statute of real powers, by the same hands, in the same weeks.",
             kick='C · The legal architecture', size=24)

# 13 D DIVIDER
divider_photo('afghan-port.jpg', 'Section D', 'Afghanistan: The First War',
              ['American special forces ride with Afghan allies,', 'Dari-a-Souf Valley, October 2001.'],
              "The photograph shows United States special operations forces of Task Force Dagger riding on horseback with Afghan commander Abdul Rashid Dostum in the Dari-a-Souf Valley in October 2001, in a United States Army photograph by Master Sergeant Chris Spence. It is the right image for the first war's opening form. The Taliban government had refused to surrender bin Laden, and the war that began on October 7, 2001 was fought by American air power and small teams of special forces joined to the Afghan fighters of the Northern Alliance, men who had been fighting the Taliban for years and who moved, in that country, on horses. Kabul fell in November and the regime collapsed within weeks. Section D holds the two halves of the Afghanistan story together: the quick fall of the regime, and the long war that followed it.",
              title_size=36)

# 14 D CONTENT
content_text('The quick fall, and the long war',
             ['The bombing opened on October 7, 2001.',
              'Kabul fell in November.',
              'Bin Laden escaped at Tora Bora.',
              'The quick victory opened a long war.',
              'Bin Laden was killed in Pakistan in 2011.'],
             "Teach the sequence as a contrast. The campaign opened on October 7, 2001, less than a month after the attacks, and the Taliban regime, which had sheltered al Qaeda and refused to give up its leaders, fell from Kabul in November and collapsed within weeks. At Tora Bora in December, bin Laden escaped the fighting and crossed into Pakistan, and the hunt for him ran for nearly ten more years. The victory over the regime opened the longer war: building an Afghan government and fighting a Taliban insurgency that regained ground year by year. American forces were still fighting in Afghanistan when the financial crisis arrived in 2008, which is where the next lesson picks the country up. The hunt itself ended on May 2, 2011, when American forces killed bin Laden at his compound in Abbottabad, Pakistan, in a raid ordered by President Barack Obama.",
             kick='D · Afghanistan', size=24)

# 15 E DIVIDER
divider_text('Section E', 'Iraq: The Second War',
             'A war that rested on a claim, and a search that settled what the claim was worth.',
             "The second war differed from the first in the ground it stood on, and students should have the difference stated before any detail. Afghanistan followed the doctrine: the government attacked had sheltered the network that attacked the United States. Iraq had attacked no one in 2001. The administration said that Iraq, ruled by Saddam Hussein, possessed stockpiles of weapons of mass destruction and was rebuilding the means to make more, and that claim was the stated ground for the invasion of 2003. Section E follows the claim in order: its presentation to the country and to the United Nations, the invasion, and then the search of the country by the Iraq Survey Group, whose report of 2004 is the lesson's closing document for the war. Every statement in this section is attributed, because the argument over this war is the sharpest in the lesson.")

# 16 E CONTENT
content_text('A claim, presented',
             ['The stated ground was stockpiles of weapons of mass destruction.',
              'Congress authorized force in October 2002.',
              'Powell presented the evidence at the United Nations.',
              'The invasion began on March 20, 2003.',
              'Baghdad fell in April.'],
             "Present the case as it was presented, in its makers' terms, before the record judges it. The administration said Iraq possessed chemical and biological stockpiles and was reconstituting its nuclear program, and it connected that claim to the doctrine of September 2001: after the attacks, it argued, a hostile state with such weapons could hand them to terrorists. Congress authorized force against Iraq in October 2002. In February 2003, Secretary of State Colin Powell presented the administration's evidence to the United Nations Security Council, in the administration's fullest public statement of the claim. The invasion began on March 20, 2003, and Baghdad fell in April. Students should note the forms the evidence took: intelligence assessments summarized by officials, photographs and intercepts explained to the Council, and the word of defectors the public could not examine. The search that could examine everything came after the invasion.",
             kick='E · Iraq', size=24)

# 17 E CONTENT 2
content_text('No stockpiles found',
             ['The Iraq Survey Group searched the country.',
              'The chemical stockpile was destroyed in 1991.',
              'The nuclear program ended in 1991.',
              'The Group found no evidence of a restart.',
              'Its second finding was an intent to rebuild after sanctions.'],
             "Give the findings in the report's own words, because precision is the whole point of this slide. On the nuclear program: Saddam Husayn ended the nuclear program in 1991 following the Gulf war, and the Survey Group found no evidence to suggest concerted efforts to restart the program. On chemical weapons: Iraq unilaterally destroyed its undeclared chemical weapons stockpile in 1991, and there were no credible indications that Baghdad resumed production thereafter. The Group's evidence was the country itself, sites searched, regime documents exploited, and detained officials interviewed, which is why its report settled the stockpile question in a way prewar intelligence could not. Then state the report's second half with equal care, because honest teaching requires it: the same report found that Saddam intended to recreate his capability once sanctions were removed. The regime's fall in the meantime opened an insurgency and a sectarian civil war, and the occupation ran for years.",
             kick='E · Iraq', size=24)

# 18 E STAT
stat('7,000+', 'American service members killed in the Afghanistan and Iraq wars combined',
     'The two wars\u2019 cost to the United States ran to sums measured in the trillions of dollars',
     "Read this number beside the first one in the lesson. The attacks killed 2,977 people in a morning. The wars that answered them killed more than seven thousand American service members across two decades, most of them in Iraq after its invasion and in Afghanistan after its quick victory turned long, alongside Iraqi and Afghan dead in far greater numbers, whom this lesson names as a fact of the record without a settled count. The financial accounting runs to sums measured in the trillions of dollars, in war appropriations, veterans' care, and interest, by the accounting the era's documents use. Officials who ordered the wars said the cost bought the country's safety after an attack that had shown the price of unpreparedness. Critics answered that the Iraq share of the bill rested on a claim the record retired in 2004. Both arguments are documented; the figures are what the documents agree on.",
     kick='E · Iraq')

# 19 F DIVIDER
divider_text('Section F', 'The State Built at Home',
             'A department assembled from twenty two agencies, and powers the public learned of twelve years later.',
             "While the wars ran abroad, the government rebuilt itself at home, and section F takes the building in two parts: the structure, and the powers. The structure is the Department of Homeland Security, created in 2002, the largest reorganization of the federal government in half a century, gathering border, coast guard, immigration, emergency, and transportation security agencies under one secretary. The powers are the surveillance authorities widened by the PATRIOT Act, used for years in secret programs, and revealed in 2013 when Edward Snowden's disclosures showed that the government had collected Americans' telephone records in bulk. The argument over those programs, between officials who defended them as lawful tools that had helped stop plots and critics who charged that they swept in millions with no connection to terrorism, is the domestic form of the lesson's standing argument.")

# 20 F CONTENT
content_photo_s('groundzero-port.jpg', 'A department built from the site outward',
             ['The Department of Homeland Security was created in 2002.',
              'Twenty two agencies were placed under one secretary.',
              'Airport security was federalized.',
              'It gathered border, coast guard, immigration, and emergency agencies.'],
             "The photograph shows workers clearing debris from the World Trade Center wreckage on September 14, 2001, photographed by Andrea Booher of the Federal Emergency Management Agency, an agency that would itself be folded into the new department. Work the structure plainly. Before the attacks, the work of guarding the country at home was scattered across the government: the Coast Guard in one department, customs and immigration in others, emergency management independent, airport screening in private hands. The Homeland Security Act of 2002 merged twenty two federal agencies and offices into one cabinet department charged with protecting the country against terrorist attack and disaster. Airport security was federalized under a new Transportation Security Administration, which is why the screening every student has walked through is performed by federal officers. The department was the domestic monument of the era: an institution, with a budget and a secretary, built to make the failure of September 11 structurally harder to repeat.",
             kick='F · The state built at home')

# 21 F CONTENT 2
content_text('The bulk collection revealed',
             ['Powers widened in 2001 were used in secret.',
              'The Snowden disclosures came in 2013.',
              'Telephone records were collected in bulk.',
              'Officials called them lawful tools that had stopped plots.',
              'Critics said millions were swept in with too little check.'],
             "State both cases in their makers' terms, in this order, and let neither borrow the other's language. The disclosures of 2013 showed that under authorities rooted in the PATRIOT Act, the National Security Agency had collected records of Americans' telephone calls in bulk, keeping data on millions of people with no connection to terrorism, under orders of a secret court. Officials of the Obama administration, and members of Congress briefed on the programs, defended them as lawful, court supervised tools that had helped identify and stop plots. Critics in and out of Congress charged that bulk collection reversed the principle Section 102 had stated inside the same statute, judging people as a population rather than by individual responsibility, and that a check conducted in secret was no public check at all. Congress ended the bulk telephone program in 2015 and replaced it with a narrower system, a fact that belongs to both sides' accounts.",
             kick='F · The state built at home', size=24)

# 22 G DIVIDER
divider_photo('situation-port.jpg', 'Section G', 'The Judgment and the Argument',
              ['The Situation Room, May 1, 2011:', 'the hunt for bin Laden ends.'],
              "The photograph shows President Barack Obama and his national security team in the White House Situation Room on May 1, 2011, receiving updates on the raid that killed Osama bin Laden in Abbottabad, Pakistan, in an official White House photograph by Pete Souza. It closes the lesson's arc: the hunt that began on the night of September 11, 2001 ended in this room nearly ten years later. Section G is not about the raid. It is about the two judgments the era produced and left standing. The first is the 9/11 Commission's, delivered in 2004, a judgment of the government that had failed to stop the attacks. The second is the argument over everything built in answer, the wars and the powers, which the Commission did not settle and which the documents of this lesson carry in both sides' own terms.",
              title_size=36)

# 23 G CONTENT
content_text('Failures of imagination',
             ['The Commission reported in July 2004.',
              'It named failures of imagination, policy, capabilities, and management.',
              'Imagination was named the most important failure.',
              'No measure from 1998 to 2001 delayed the plot.'],
             "Teach the Commission's judgment as the lesson's standard of official self-examination. The report found that none of the measures the government had adopted from 1998 to 2001 disturbed or even delayed the progress of the al Qaeda plot, and it distributed the failure across the whole government rather than fixing it on one office or one administration: failures of imagination, policy, capabilities, and management. It then ranked them, and students should hear the ranking as the report's central claim. The most important failure was one of imagination: the Commission did not believe leaders understood the gravity of the threat. Policy, capabilities, and management failures could each be repaired with money, law, and reorganization, and much of section F's building was exactly that repair. Imagination was the failure underneath the others, the inability to picture the attack before it arrived, and the report's word for it is the one the quick check and the test will ask for.",
             kick='G · The judgment', size=24)

# 24 G CONTENT 2
content_text('The standing argument',
             ['Officials said the powers were necessary.',
              'Their evidence was that no second attack on that scale followed.',
              'Critics said Iraq\u2019s claim failed the record.',
              'Critics said the powers outran safety.',
              'The documents carry both sides.'],
             "Close the content by stating the argument as a pair of documented positions, which is the form the writing task will grade. On one side stand the officials who built the machinery of 2001 and 2002. They said the powers were necessary, that a government which had been surprised once had a duty to organize against surprise, and they pointed to their central piece of evidence: in the years after, no second attack on the scale of September 11 succeeded on American soil. On the other side stand the critics. They answered that the Iraq war, the era's largest single act, rested on a stockpile claim the government's own inspectors retired in 2004, and that the security powers, above all the bulk collection revealed in 2013, reached further into ordinary life than safety required. The lesson takes no side between these positions. It requires students to argue from the documents, and to be able to state the other side's evidence as fairly as their own.",
             kick='G · The judgment', size=24)

# 25 GLANCE
s = slide(NAVY)
kicker(s, 'The response at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Each step, and what it settled', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The day and the doctrine', '2,977 killed; no distinction', 'The rule that governed two wars'),
        ('The laws of 2001', 'AUMF 518 to 1; the powers statute', 'Breadth granted in weeks, argued ever since'),
        ('The two wars', 'Afghanistan 2001; Iraq 2003', 'One ground held; one claim failed'),
        ('The judgment of 2004', 'Imagination the deepest failure', 'The argument the era left open')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the summary table at the end of the guided notes, The Response at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. Read the rows as one account rather than four summaries. The day and the doctrine supplied the rule. The laws of the fall of 2001 supplied the authority, voted almost unanimously and argued about ever since. The two wars tested the rule and the claim in sequence, one ground holding and one failing. The judgment of 2004, the Commission's on the failure and the Survey Group's on the stockpiles, supplied the record against which everything since has been argued. Grade the table generously on wording and strictly on completeness: every row needs what was done or found, and what was argued or left open.")

# 26 VOCAB A
vocab('Words for the attacks and the answer',
      [('September 11 attacks', 'the day, in the Commission\u2019s accounting'),
       ('al Qaeda', 'the network led by Osama bin Laden'),
       ('War on Terror', 'the worldwide campaign declared after the attacks'),
       ('Authorization for Use of Military Force', 'the war authorization of September 18, 2001')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. September 11 attacks: the terrorist attacks of September 11, 2001, in which hijackers of the al Qaeda network flew passenger planes into the World Trade Center and the Pentagon and crashed a fourth plane in Pennsylvania, killing 2,977 people. al Qaeda: the terrorist network led by Osama bin Laden that carried out the September 11 attacks, built from veterans of the war against the Soviet Union in Afghanistan. War on Terror: the worldwide campaign of military action, intelligence work, and security measures the United States declared after September 11, 2001, against al Qaeda and the groups and states said to shelter it. Authorization for Use of Military Force: the law Congress passed on September 18, 2001 authorizing the president to use all necessary and appropriate force against those responsible for the September 11 attacks and those who harbored them.")

# 27 VOCAB B
vocab('Words for the powers and the claim',
      [('USA PATRIOT Act', 'the powers statute of October 2001'),
       ('Department of Homeland Security', 'twenty two agencies under one secretary'),
       ('weapons of mass destruction', 'the claim at the center of the Iraq decision')],
      "Three more terms, again matching the guided notes exactly. USA PATRIOT Act: the law of October 2001 that widened the government's powers of surveillance, search, and detention in terrorism investigations, passed by overwhelming margins in the weeks after September 11. Department of Homeland Security: the cabinet department created in 2002 that merged twenty two federal agencies and offices charged with protecting the country against terrorist attack and disaster. weapons of mass destruction: chemical, biological, and nuclear weapons; the claim that Iraq possessed stockpiles of them was the stated ground for the American invasion of Iraq in 2003, and no such stockpiles were found. Note the order of this set. The first two terms name what the government built at home, a statute and a department. The third names the claim on which the second war rested, defined by what the record showed about it.")

# 28 SYNTHESIS
content_text('Judging the era from its documents',
             ['The rule was stated in a night and voted in a week.',
              'One war\u2019s ground held and one war\u2019s claim failed.',
              'Powers were built at home and then argued about.',
              'The writing task asks for a gap, measured.'],
             "Close the teaching here, before the work slide, and model the judgment the writing task will ask for. The era's machinery worked fastest where its evidence was plainest: the attacks were a fact, the doctrine answered them in a sentence, and Congress voted the authority 518 to 1. It worked worst where its evidence was a claim about a closed country: the stockpiles did not exist, and the government's own inspectors, searching the country itself, retired the claim in 2004. Between those poles stand the powers at home, granted in the same weeks as the war authorization and argued about ever since, with Section 102's declaration and the bulk collection of 2013 as the two documents that frame the argument. The strongest student writing will measure each response by the same standard: the distance between the evidence offered at the time and what the record later showed.",
             kick='Synthesis')

# 29 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did the attacks change what the government did abroad and at home, and what did Americans argue about the changes? Build the file first, then judge from it.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Powers File: five records, a file, and a verdict on the machinery at its strongest and its most questionable'),
        ('Notebook', 'Notebook page: five records charted by power, evidence, and check, and the standing argument in one paragraph'),
        ('Quick check', 'The Situation Room, May 1, 2011: the photograph, the toll, the votes, the definitions'),
        ('Writing', 'The Gap Between the Evidence and the Record: which response\u2019s evidence failed furthest, judged from the documents')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the AUMF votes and who decides its targets, the Survey Group\u2019s two findings of 2004, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Powers File, runs five stations through the records: the Commission's executive summary, the president's address of September 11, the Authorization for Use of Military Force, Section 102 of the PATRIOT Act, and the Duelfer findings, each station asking for the power claimed or the finding made, the evidence offered, and the check placed on it. Students build the file in Part 2 and defend a double verdict, the document that shows the era's machinery at its strongest and the one that shows it at its most questionable. The notebook page charts the same five records. The quick check works from Pete Souza's Situation Room photograph of May 1, 2011. The writing task asks for the largest gap between the evidence offered at the time and what the record later showed. The exit ticket has three parts: the AUMF votes and the determination, the Survey Group's two findings with their year, and the lesson question answered with one change abroad and one at home.")

dc.save(OUT)
