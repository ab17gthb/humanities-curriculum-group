#!/usr/bin/env python3
"""The Founding Lesson 7 deck, "The Constitution and the Great
Compromises," built to the approved system: image-led slides, fragments
only on screen, comprehensive speaker notes, full lesson + vocabulary
coverage. Fonts: Georgia titles, Lato body."""
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

def content_photo_s(img, title, items, note, kick=None, size=23):
    s = slide(CREAM)
    photo_right(s, img)
    if kick: kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95 if kick else 0.8, 6.9, 1.2, title, size=31, color=NAVY, font='Georgia', leading=1.05)
    frags(s, items, y=2.15 if kick else 2.0, size=size)
    notes(s, note)
    return s

# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'THE FOUNDING · LESSON 7', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Constitution and the Great Compromises', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Philadelphia, May 25 to September 17, 1787', size=17, color=POWDER)
notes(s, "The image is the first page of the engrossed Constitution, the parchment signed on September 17, 1787 and held by the National Archives. Open by placing this lesson after Lesson 6. The Confederation government could not tax, could not make the states obey the peace treaty, and had watched Massachusetts farmers close the courts. Congress answered by calling a convention to revise the Articles. What happened in Philadelphia instead is this lesson: fifty five delegates from twelve states, Rhode Island absent, spent one summer building a new government. Tell students the lesson runs on documents they will handle themselves, the Preamble, Madison\u2019s notes, the text of Article I, and Franklin\u2019s last speech, and that every compromise in the lesson gets priced as well as praised.")

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("How did fifty five men in one room design a government strong enough to act and limited enough to trust?", {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('Why did the colonies break with Britain, and what did Americans build in the place of the empire they rejected?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Read the question in its two halves and keep both alive all hour. Strong enough to act answers the Confederation\u2019s failure, a government that could declare war and sign treaties but could not raise a dollar or compel a state. Limited enough to trust answers the Revolution\u2019s own fear, because these men had fought a king and a Parliament they called tyrannical, and their constituents would not ratify a new tyranny with an American address. Every section of the lesson presses one half or the other. The Virginia Plan is strength. The deadlock is the small states pricing that strength. The compromises are the two halves being forced into one document, and the closing argument, in the writing task, asks students to judge whether the limits were built in or merely claimed afterward.")

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'One room, two plans, a document and its prices', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The room in Philadelphia', 'May 25, 1787, secrecy, Washington presiding, Madison recording'),
        ('B', 'The Virginia Plan', 'A new national government, apportioned by population'),
        ('C', 'The New Jersey Plan and the deadlock', 'One vote per state, and the tie of July 2'),
        ('D', 'The Great Compromise', 'July 16, the House by population, the Senate equal'),
        ('E', 'Counting the enslaved', 'Three fifths, the trade protected to 1808, return on claim'),
        ('F', 'The design assembled', 'Federalism, separated powers, checks, electors'),
        ('G', 'What was left out, and the close', 'No bill of rights, We the People, thirty nine sign')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This slide is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A sets the room, its secrecy rule, its presiding officer, and its record keeper. Section B is the Virginia Plan, and section C the small states\u2019 answer and the deadlock it produced. Section D is the Great Compromise of July 16. Section E states the count of the enslaved plainly, in the document\u2019s own arithmetic, with its two companion protections. Section F assembles the design, federalism, separated powers, checks, and the electoral college. Section G closes with the refused bill of rights, the Preamble\u2019s opening words, Franklin\u2019s speech, and the signing. The summary table at the end of the guided notes asks students to rebuild this map stage by stage.")

# 4 SECTION A DIVIDER
divider_photo('washington-port.jpg', 'Section A', 'The Room in Philadelphia',
              ['George Washington, by Gilbert Stuart, begun 1795.', 'The Metropolitan Museum of Art, Open Access.'],
              "The portrait is Gilbert Stuart\u2019s Washington, begun in 1795 and held by the Metropolitan Museum of Art, which releases the image under Open Access. Washington\u2019s role this summer was silence. Elected to preside on the first day, he sat in a chair at the front of the room, put questions, kept order, and offered no argument on any clause until the final day, when he spoke once in favor of widening the ratio of representation. His silence was the office working as intended, and his known presence did other work besides: the country trusted the chair because of the man in it, and the delegates knew the presidency they were designing would first be held by him. Section A also names the room\u2019s second fixture, Madison in his seat near the front, taking the notes that make this the best documented founding of the age.")

# 5 THE ROOM
content_photo_s('hall-port.jpg', 'A government argued in secret',
             ['The Pennsylvania State House, May 25, 1787',
              'Fifty five delegates, twelve states',
              'Rhode Island sends no one',
              'Washington presides, in silence',
              'Madison writes the debates each night'],
             "The engraving shows the Pennsylvania State House from Birch\u2019s Views of Philadelphia, drawn in 1798 and 1799, a dozen years after the Convention but the same building, in the same form. Teach the secrecy rule as a working tool rather than a scandal. Members were barred from publishing anything spoken in the house, the windows stayed shut against the summer heat, and sentries kept the curious away. The rule let a delegate test an argument in June and abandon it in August without a newspaper at home holding him to it, and the great compromises of July are hard to imagine without that shelter. Against the shelter, set the cost students will meet at Station 2 of the activity: the public got a finished document and almost no record, and the fullest account of the debates is one man\u2019s private notebook, published when every delegate was dead.",
             kick='A · The room')

# 6 STAT 55
stat('55', 'delegates from twelve states attended the Convention',
     'Rhode Island sent none · The Convention organized on May 25, 1787, once seven states were present',
     "Let the number correct two habits at once. Fifty five is small enough that students should picture a room, not a congress: a single chamber in the State House, men who had soldiered, practiced law, planted, and traded together for a decade, arguing face to face for four months. It is also a chosen company, not a sample of the country. No women sat in it, no enslaved or free Black American sat in it, no Native nation was represented in it, and the poorest farmers, the men who had closed the courts in Massachusetts the winter before, were present only as the problem the room had been called to solve. Keep the double fact in view all lesson, because the document\u2019s authority claim, We the People, was written by these fifty five men, and the ratification fight in the next lesson is the country answering them.",
     kick='A · The room')

# 7 SECTION B DIVIDER
divider_text('Section B', 'The Virginia Plan',
             'A new national government in place of a revised league.',
             "Section B is the Convention\u2019s founding act of disobedience, and students should feel its audacity in the record\u2019s own terms. Congress had authorized a convention for the sole and express purpose of revising the Articles of Confederation. Virginia\u2019s delegation arrived with a replacement already drafted, chiefly by Madison during the days he waited in Philadelphia for a quorum, and Edmund Randolph, Virginia\u2019s governor, presented it in the first week. The plan did not patch the league. It proposed a national government of the kind the Revolution had been fought, in part, to prevent: a legislature empowered against the states themselves, choosing the executive and the judiciary. Everything after this section is the Convention deciding how much of the Virginia Plan it dared to keep, and at what price in small state votes.")

# 8 VIRGINIA PLAN
content_photo_s('madison-port.jpg', 'A new government, not a revision',
             ['Presented by Edmund Randolph',
              'Drafted chiefly by James Madison',
              'Two houses, both apportioned by population',
              'Power to strike down state laws',
              'The legislature chooses executive and judiciary'],
             "The portrait is John Vanderlyn\u2019s Madison of 1816, in the White House collection, the standard likeness of the man who did more than any other delegate to shape this document. Walk the plan\u2019s logic slowly. Apportionment by population or wealth makes representation follow numbers, which is a democratic principle and a regional fact in the same breath: Virginia, Pennsylvania, and Massachusetts together held a large share of the union\u2019s people, and a population legislature hands them the government. The negative on state laws, Madison\u2019s cherished clause, would have let Congress veto any state law it judged contrary to the union, a power beyond anything the finished Constitution contains. Note what the plan assumes about sovereignty. Under the Articles the states are the parties and Congress their agent. Under this plan the people are the party and the states are districts with governments. That reversal, more than any single clause, is what the small states heard in the first week.",
             kick='B · The Virginia Plan')

# 9 SECTION C DIVIDER
divider_text('Section C', 'The New Jersey Plan and the Deadlock',
             'One house, one vote per state, and a tie that nearly ended the Convention.',
             "Section C gives the small states their full argument before the deadlock, because students who meet the New Jersey Plan only as an obstacle miss what it defended. Delaware\u2019s delegates had instructions from home forbidding them to surrender the equal vote, and the small states\u2019 fear was concrete rather than proud: in a population legislature, three large states could outvote the other ten on any question, tax them, and govern them as provinces. William Paterson\u2019s plan of June 15 kept the Articles\u2019 frame, one house and equal votes, and repaired its known failures by adding the powers to tax and to regulate trade. The Convention then spent the rest of June discovering that neither side could carry the room, which is what a deadlock between principles, each half right, looks like from inside.")

# 10 NEW JERSEY PLAN
content_text('One house, one vote per state',
             ['Paterson answers for the small states, June 15',
              'The Articles\u2019 frame, kept and patched',
              'New powers to tax and to regulate trade',
              'Representation consumes the rest of June',
              'July 2: the vote ties, state against state'],
             "Teach the tie of July 2 as the Convention\u2019s nearest approach to failure. The question was equal representation in the second house, the Senate that did not yet exist, and the states divided evenly, with Georgia\u2019s delegation split and Massachusetts divided in its vote as the records report the day. Delegates said in the room what the reading repeats: the Convention might break up, and the union with it. The rescue was procedural, and students should learn to respect procedure as a historical force. A committee of one member from each state, the grand committee, took the question out of the full room over the July 4 recess and returned with terms neither plan contained: one house by population, one house equal. Section D takes up those terms. Ask the class, before moving on, what each side would have to surrender to accept them, because the answer is the definition of a compromise they will use all unit.",
             kick='C · The deadlock', size=23)

# 11 SECTION D DIVIDER
divider_photo('constitution-port.jpg', 'Section D', 'The Great Compromise',
              ['The engrossed Constitution, page one, 1787.', 'National Archives.'],
              "The parchment on screen is the engrossed Constitution\u2019s first page, the text as Jacob Shallus wrote it out for the signing, held by the National Archives. Section D reaches the settlement the whole document stands on. Connecticut\u2019s delegates, Roger Sherman and Oliver Ellsworth, had carried the two house formula into the grand committee, and on July 16 the Convention adopted it by five states to four, with Massachusetts divided, the narrowest consequential margin of the summer. Teach the date and the margin as facts students must produce exactly, because the unit test reaches for them: a government for three million people turned on one state\u2019s vote in a committee report. Then slow down on the settlement\u2019s shape, because its two halves answer to two different theories of what the union is, and both theories were left standing in the finished frame.")

# 12 GREAT COMPROMISE
content_text('Two houses, two opposite rules',
             ['The House: apportioned by population',
              'Chosen by the people, two year terms',
              'Every revenue bill begins in the House',
              'The Senate: two from every state',
              'Chosen by state legislatures, six year terms'],
             "Set the two rules side by side and make students state what each one says about the union. The House is the Virginia Plan\u2019s child: representation by population, members chosen directly by the people, short terms to keep them answerable, and the power of the purse begun in the people\u2019s house, a deliberate inheritance from the colonial assemblies\u2019 long fight over money bills. The Senate is the New Jersey Plan\u2019s child: the states as equals, two voices each, chosen by the state legislatures rather than by voters, with long terms meant to cool the House\u2019s heat. Delaware counts exactly as Virginia did, and the reading\u2019s sentence is the one to hold: the union carries a double nature in its frame, a people in one house and states in the other. Every later argument about the Senate\u2019s fairness begins in this room and this vote, and students should be able to run the argument in both directions before the hour ends.",
             kick='D · The Great Compromise', size=23)

# 13 STAT 5 TO 4
stat('5 to 4', 'states adopted the Great Compromise on July 16, 1787',
     'The settlement that made the rest of the document possible, carried by a single state\u2019s margin',
     "Stand on the margin for a full minute, because students raised on the document\u2019s permanence underrate how close it came to not existing. Five states for the committee\u2019s terms, four against, Massachusetts divided and so counted on neither side. Had one delegation changed its vote, the report fails, the Convention returns to the July 2 tie with its tempers spent, and the most likely sequel is adjournment and a union dissolving into regional confederacies, the outcome the delegates themselves named in debate. The lesson question asks how fifty five men designed a government. Part of the honest answer is that the design survived by one vote in the middle of July, and that the delegates who lost that vote, the large state men who had written the Virginia Plan, accepted the loss and stayed in the room. Institutions, students should hear, are built by losers who stay.",
     kick='D · The Great Compromise')

# 14 SECTION E DIVIDER
divider_text('Section E', 'Counting the Enslaved',
             'Three fifths, in the document\u2019s own arithmetic, and slavery protected without its name.',
             "Section E is the lesson\u2019s center of gravity, and it should be taught at the reading\u2019s pace, in plain words. The Great Compromise apportioned the House by population, which forced the question the Articles had dodged since 1783: how does the count treat people who are held as property, who cannot vote, hold office, or leave? The southern position in the room was stated without embarrassment in the debates Madison recorded: enslaved people should count as people when seats were divided and as property when wealth and taxes were counted. The settlement the Convention reached was not invented in 1787. It was borrowed from a Confederation tax formula of 1783, which had set the same fraction for requisitions the states never paid. Name the section for what it is before the first slide of content: this is where the Constitution priced enslaved people into the republic\u2019s arithmetic.")

# 15 THREE FIFTHS
content_text('Three fifths of a person',
             ['Counted as people for seats, as property for taxes',
              'The fraction borrowed from a tax formula of 1783',
              'Five enslaved people add three to a state\u2019s count',
              '100,000 held adds 60,000 to the count',
              'Not one of those counted could cast a ballot'],
             "Work the arithmetic on the board exactly as the quick check and the unit test will ask for it, because the fraction is easy to recite and easy to misunderstand. The clause adds to the whole number of free persons three fifths of all other persons. One hundred thousand multiplied by three fifths is sixty thousand: a state\u2019s delegation grows by the count of sixty thousand people who do not exist as voters anywhere in the system. Then state whose interest the number served, in the record\u2019s terms. The tie between representation and direct taxes was the northern answer, the same count that raised a state\u2019s seats would raise its share of direct taxes, and students should give that answer its weight. Then set it down again: direct taxes were rare and hard to levy, while House seats voted on every law, every year, and the advantage compounded for as long as slavery lasted, which is the honest completion of the sentence.",
             kick='E · The count', size=23)

# 16 STAT 3/5
stat('3/5', 'of a person: the fraction the Constitution counted for each enslaved person',
     'Applied to House seats and to direct taxes alike, and carried through the House count into the electoral college',
     "This is the slide to teach slowly and without decoration. The word slavery appears nowhere in the Constitution, and students should be asked to find the institution anyway, the way the lesson has taught them to find it: in the arithmetic. Because a state\u2019s presidential electors equal its members of Congress, the three fifths count raised the slave states\u2019 weight in choosing every president, an advantage that ran through the republic\u2019s first seven decades and shaped its politics on slavery itself. Madison recorded the discomfort in the room, in the delegates\u2019 own words, at Station exercises later in the hour, and he wrote in his later years that the Convention had not confronted the thing by its right name. Hold both facts together for the class: men in that room knew what the clause did, said so in debate, and adopted it anyway, because the union they were building was priced in this currency. That is the settlement the writing task will ask students to judge.",
     kick='E · The count')

# 17 GUARDED LANGUAGE
content_text('Guarded in careful language',
             ['The Atlantic slave trade protected until 1808',
              'Congress barred from prohibiting it before that year',
              'Escape into a free state: delivered up on claim',
              'The word slavery appears nowhere in the document',
              'Madison: not confronted by its right name'],
             "Take the two companion clauses in turn, in the document\u2019s own wording, because the wording is the evidence. The trade clause does not say slave trade. It bars Congress from prohibiting the migration or importation of such persons as any of the states shall think proper to admit, before the year 1808, a date twenty years out that let delegates tell themselves and their constituents that the trade had been given an end. The return clause does not say enslaved or fugitive. It speaks of a person held to service or labour, escaping into another state, to be delivered up on claim of the party to whom the service is due, which made every free state\u2019s soil an errand route for slave catchers and wrote the obligation into the Constitution itself. Ask students why men who could write We the People with such economy chose fog here. The record answers plainly: a named institution would have cost votes in the North and confessions in the South, and the union was being held together, in this section, by what the text refused to say.",
             kick='E · The count', size=22)

# 18 SECTION F DIVIDER
divider_text('Section F', 'The Design Assembled',
             'Power divided between nation and states, then divided again inside the nation.',
             "Section F assembles what the compromises left standing, and its organizing thought is division twice over. The first division is federalism, the settlement between the national government the Virginia Plan demanded and the states the New Jersey Plan defended: each level acts directly on the people within its own sphere, and the states keep the ordinary business of life. The second division is the separation of powers inside the federal government, legislature, executive, and judiciary, each armed against the others by the checks the delegates laced between them. Present the section as engineering with a theory of human nature inside it. The framers had read their history and their own summer: power concentrated invites abuse, so the design assumes ambition in every officeholder and sets the ambitions against one another. Students met the theory\u2019s plain version in the vocabulary, and the slides now walk its machinery part by part.")

# 19 DESIGN
content_photo_s('broadside-port.jpg', 'Divided, then laced together',
             ['Federalism: nation and states, each in its sphere',
              'Enumerated powers, listed one by one',
              'Necessary and proper, toward unforeseen cases',
              'A veto, and an override to answer it',
              'Judges holding office during good behavior'],
             "The image is the first printed edition of the Constitution, run off by Dunlap and Claypoole in September 1787 so the delegates could read the finished text entire, the ancestor of Washington\u2019s annotated draft at Station 3. Walk the machinery in the order a law travels. Congress, holding the enumerated powers of Article I, passes a bill. The president signs or vetoes it; Congress may override by two thirds of both houses. The Senate consents to the treaties the president negotiates and the appointments he makes. The courts, their judges holding office during good behavior rather than at any politician\u2019s pleasure, judge cases under the laws, and judicial review, the power to void a law against the Constitution, stands nowhere written in the text and everywhere implied by a written constitution that calls itself supreme law. End on the enumeration\u2019s double edge: a list limits, and the necessary and proper clause stretches the list, and the argument between those two facts is the next two centuries of American politics in embryo.",
             kick='F · The design')

# 20 ELECTORS
content_text('Chosen by electors, for tangled reasons',
             ['Not by Congress, not by direct national vote',
              'Slow news: voters could not know distant men',
              'A single national contest invited cabal',
              'The three fifths count raised slave state weight',
              'Washington\u2019s expected occupancy did the persuading'],
             "Teach the electoral college with the care the reading uses, because this is where a single cause is most often sold as the whole story. The debates state several reasons in the delegates\u2019 own voices. Election by Congress, the Virginia Plan\u2019s method, would make the president the legislature\u2019s creature, bargaining for his office and his reelection. Direct election faced a continent of slow news, where voters in Georgia could not know a candidate from New Hampshire, and a single national pool for votes invited cabal and foreign intrigue in the framers\u2019 telling. Electors, meeting separately in their own states, answered both objections. Alongside the stated reasons, state the effect without inflating it into the sole cause: because electors equal a state\u2019s members of Congress, the three fifths count raised the slave states\u2019 weight in choosing presidents, an advantage the design carried whether or not every delegate named it aloud. Scholars argue over how heavily that effect weighed in the room. The documents in this lesson let students see both the stated reasons and the arithmetic, and the honest sentence holds the two together.",
             kick='F · The design', size=22)

# 21 SECTION G DIVIDER
divider_photo('hall-port.jpg', 'Section G', 'What Was Left Out, and the Close',
              ['The State House from Birch\u2019s Views, 1800:', 'the room emptied, the document gone out to the states.'],
              "Section G closes the summer on two facts that pull against each other, and the lesson ends by holding them together rather than choosing. The first is an omission: on September 12, with the text nearly finished, George Mason moved for a committee to prepare a bill of rights, and the Convention refused without a single state voting in favor, on the stated ground that the states\u2019 own declarations of rights were protection enough. The second is an opening: the Committee of Style began the document not with the states\u2019 names, as the Articles had, but with We the People of the United States. Mason, Gerry, and Randolph carried the omission into the open and refused to sign. The Preamble\u2019s claim went out to the states in the same envelope. Students should leave the section able to state both facts in one breath, because the ratification contest of the next lesson is nothing but those two facts argued at full length.")

# 22 LEFT OUT
content_text('No bill of rights; We the People',
             ['September 12: Mason moves for a bill of rights',
              'Refused, with no state voting in favor',
              'The states\u2019 declarations held protection enough',
              'The Preamble written last, by the Committee of Style',
              'We the People, in place of the states\u2019 names'],
             "Slow down on the refusal\u2019s reasoning before judging it, because the delegates were not careless men having a tired afternoon, though they were tired and said so. Their argument ran that the federal government held only enumerated powers, that a bill of rights against a government of listed powers was unnecessary, and that listing some rights might endanger others by implying the list was complete. The states\u2019 declarations, meanwhile, bound state governments, which held the general police power over daily life, and the new federal government was not, in this telling, the danger the declarations guarded against. The argument was coherent and it failed politically within the year, as the next lesson shows: state after state demanded amendments as the price of ratification, and Mason\u2019s refusal became the Anti-Federalists\u2019 strongest card. Then turn to the opening. We the People was Gouverneur Morris\u2019s penmanship in the Committee of Style, and its claim, that the people and not the states ordained the government, was the boldest sentence in the document and the one its opponents attacked first.",
             kick='G · The close', size=22)

# 23 STAT 39
stat('39', 'delegates signed the Constitution on September 17, 1787',
     'Three refused: George Mason, Elbridge Gerry, and Edmund Randolph · Nine of thirteen states would make it law among those that ratified',
     "Close the count honestly. Thirty nine signatures stand on the engrossed parchment, and the attestation above them claims the unanimous consent of the states present, a form of words Gouverneur Morris devised so that signing attested the Convention\u2019s act without pledging every signer\u2019s approval of every clause, the formula Franklin\u2019s speech had pleaded for. Three men who had sat all summer refused: Randolph, who had presented the Virginia Plan on the Convention\u2019s first working days; Mason, the bill of rights\u2019 author of five days before; and Gerry of Massachusetts. Their refusals were not defections from the founding. They were the founding\u2019s first opposition, and each man carried his reasons home to the ratification fight, where the document\u2019s fate would be decided by conventions of the people in the states, nine of thirteen required, exactly as Article VII provided. Franklin\u2019s rising sun belongs to this slide\u2019s story: watching the last signatures, he told the men near him that the sun carved on Washington\u2019s chair, which had puzzled him all summer, was rising.",
     kick='G · The close')

# 24 GLANCE
s = slide(NAVY)
kicker(s, 'The Convention at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Five stages, one summer', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The room', 'May 25 to September 17, 1787', 'Secrecy, Washington silent, Madison recording'),
        ('The deadlock', 'Virginia Plan against New Jersey Plan', 'July 2: the vote on equality ties'),
        ('The settlement', 'The Great Compromise, July 16', 'Adopted five states to four'),
        ('The count', 'Three fifths, trade to 1808', 'Seats and electors built on the enslaved'),
        ('The close', 'No bill of rights; thirty nine sign', 'We the People goes out to the states')]
yy = 2.72
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 0.88
notes(s, "This slide mirrors the final table in the guided notes, The Convention at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The rows compress the arc. The room pairs the Convention\u2019s working conditions, secrecy and a silent chair, with the record those conditions produced. The deadlock pairs the two plans with the July 2 tie that nearly dissolved the Convention. The settlement holds July 16 and its five to four margin. The count row refuses euphemism, in the table as in the reading: seats and electors built on people held as property. The close pairs the refused bill of rights with the thirty nine signatures and the Preamble\u2019s claim. Grade the table generously on wording and strictly on pairing: every stage must show what was settled and what it cost or left open, because that pairing is the lesson\u2019s whole habit of mind.")

# 25 SYNTHESIS
content_text('What the room built, and what it charged',
             ['The strength: a national government that could act',
              'The limit: divided powers, checked at every joint',
              'The settlement: people in one house, states in the other',
              'The price: the enslaved, counted and unnamed',
              'The test ahead: nine states, and a people asked to judge'],
             "Draw the lesson together around the question\u2019s two halves, because the exit ticket and the writing task both return to them. The strength is real and students should be able to inventory it: enumerated national powers with a taxing power the Confederation never held, a House resting on the people, an executive with energy, courts independent of annual politics. The limits are real in the same inventory: two houses that must agree, a veto with its override, consent and impeachment, judges beyond reach, and an amendment rule that denies any bare majority the power to remake the frame. Then state the price in the plain words the lesson has used all hour. The union\u2019s arithmetic rested on enslaved people counted at three fifths toward other men\u2019s power, the trade in them protected for twenty years, their escape made a constitutional errand, and the whole arrangement carried in language that never names it. The delegates knew, and signed, and Franklin called the sun rising. Students now judge that sentence for themselves in the verdict.",
             kick='Synthesis', size=23)

# 26 VOCAB A
vocab('Words for the meeting and the plans',
      [('Constitutional Convention', 'the Philadelphia meeting of 1787 that wrote the Constitution'),
       ('Virginia Plan', 'Madison\u2019s plan: a legislature apportioned by population'),
       ('New Jersey Plan', 'the small states\u2019 plan: one house, equal votes'),
       ('Great Compromise', 'the House by population, the Senate equal')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. The first term is Constitutional Convention: the meeting at Philadelphia from May to September 1787, called to revise the Articles of Confederation, which instead wrote the Constitution of the United States. The second is Virginia Plan: the plan proposed at the Convention by Virginia's delegation, drafted chiefly by James Madison, for a strong national government with a legislature apportioned by population. The third is New Jersey Plan: the plan proposed at the Convention by the small states, which kept a one house legislature with equal votes for every state under a strengthened Articles of Confederation. The fourth is Great Compromise: the Convention's settlement, also called the Connecticut Compromise, which apportioned the House of Representatives by population and gave every state two senators in the Senate.")

# 27 VOCAB B
vocab('Words for the count and the design',
      [('Three-Fifths Compromise', 'each enslaved person counted as three fifths of a person'),
       ('federalism', 'power divided between nation and states'),
       ('separation of powers', 'three branches, each able to check the others')],
      "Three more terms, again matching the guided notes exactly, and the set of seven is complete with these. The first is Three-Fifths Compromise: the Convention's settlement that counted each enslaved person as three fifths of a person when apportioning representatives and direct taxes among the states. Students should anchor the term to both of its applications, seats and taxes, because the test reaches for the pairing. The second is federalism: the division of power between a national government and state governments, each supreme in its own sphere, which the Constitution established in place of the Confederation. The third is separation of powers: the division of the federal government into legislative, executive, and judicial branches, each with its own powers and the means to check the others, so no single branch could rule alone. Test the pairing students most often blur: federalism divides power between levels of government, while separation of powers divides it among branches at the same level.")

# 28 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did fifty five men in one room design a government strong enough to act and limited enough to trust? Argue it from the records, with dates, votes, and the count.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'Philadelphia in Five Records: the Preamble, Madison\u2019s Notes, Washington\u2019s draft, Article I, and Franklin\u2019s speech, with a verdict on the compromises'),
        ('Notebook', 'Notebook page: the Convention\u2019s questions charted by proposal, settlement, and price'),
        ('Quick check', 'We the People and the Count: the Preamble read closely, the three fifths arithmetic, and the summer in sequence'),
        ('Writing', 'Strong Enough to Act, Limited Enough to Trust: one compromise followed through its settlement and its price')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the Great Compromise in one sentence, the count worked for a state of 340,000, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, Philadelphia in Five Records, runs five stations through the summer: the Preamble entire, Madison\u2019s Notes for September 17 with Franklin\u2019s speech inside them, Washington\u2019s annotated draft, Article I, Section 2 in the National Archives transcription, and Franklin\u2019s closing speech in the Avalon Project text of Madison\u2019s Notes, ending in a verdict on which compromise was most necessary and which cost the republic most. The notebook page charts the Convention\u2019s four great questions by proposal, settlement, and price. The quick check tests the Preamble\u2019s claim and its six purposes, the three fifths arithmetic, and the summer\u2019s sequence of dates against blueprint entries 13 and 14. The writing task requires one compromise followed through both its settlement and its price. The exit ticket has three parts: the Great Compromise defined in one sentence, the count worked for a state holding 240,000 free people and 100,000 enslaved people, and the lesson question in two or three sentences.")

dc.save(OUT)
