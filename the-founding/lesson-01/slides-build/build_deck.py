#!/usr/bin/env python3
"""The Founding Lesson 1 deck, "The Imperial Crisis: Taxation and Resistance,"
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
text(s, 0.9, 5.32, 11.5, 0.4, 'THE FOUNDING · LESSON 1', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Imperial Crisis: Taxation and Resistance', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Why Britain taxed after 1763, and why the colonies said no', size=17, color=POWDER)
notes(s, "The image is a London print of 1766, The Repeal, or the Funeral of Miss Ame-Stamp, showing politicians carrying the Stamp Act to its grave in a mock funeral procession. Hold it in front of students before any content and ask what a funeral for a tax could mean. Britain had repealed the Stamp Act within a year of passing it, and London printmakers treated the repeal as a burial. This lesson explains how a tax on paper brought an empire to that point. It runs from the war debt of 1763 through the Stamp Act, the boycotts and crowds that killed it, the repeal that came with a warning attached, the Townshend Acts, and the night in Boston in 1770 when the quarrel turned bloody. By the end of the hour students should be able to state both claims in the quarrel, in the words the two sides used at the time.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('Why did Britain tax the colonies after 1763, and why did the colonists resist taxes they had never been asked to pay before?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('Why did the colonies break with Britain, and what did Americans build in the place of the empire they rejected?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "The question has two halves and students should hear both before the lesson begins. The first half is about money and empire. Britain won the French and Indian War and doubled its national debt winning it, kept some ten thousand soldiers in North America, and decided the colonies should help pay for their own defense. The second half is about consent. The colonists had always been taxed by assemblies they elected, and the new taxes came from a Parliament in which no colonist sat and no colonist voted. Britain answered that Parliament represented every British subject wherever he lived, the argument of virtual representation. The colonists answered that representation without a vote was no representation at all. Every document in this lesson is one side or the other stating that disagreement, and the writing task asks students to judge why repeal failed to settle it.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'The crisis, in seven stretches', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The bill for victory', 'A doubled debt, and an army to pay for'),
        ('B', 'The Stamp Act', 'A tax on paper, laid directly on the colonies'),
        ('C', 'Argument and combination', 'Resolves, a congress, boycotts, homespun'),
        ('D', 'Crowds, resignations, repeal', 'No stamps sold, and a claim kept'),
        ('E', 'The Townshend Acts', 'Duties on imports, and Dickinson answer'),
        ('F', 'Troops and blood in Boston', 'Two regiments, and five men dead'),
        ('G', 'The quiet years', 'Tea kept, and committees built')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A sets the bill: a doubled debt and a standing army. Section B gives the Stamp Act of 1765, the first tax laid directly on the colonies. Section C gives the answer in argument and combination, resolves, a congress of nine colonies, boycotts, and homespun. Section D adds the crowd, the resignations, and the repeal of 1766 with the Declaratory Act attached. Section E opens the second round, the Townshend Acts and Dickinson reply. Section F follows the troops to Boston and the killings of March 5, 1770. Section G closes in the quiet years, with the tea duty kept and the committees of correspondence wiring the colonies together.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', 'The Bill for Victory',
             'A doubled debt, and ten thousand soldiers to pay for.',
             "Begin where the Colonial America unit closed. The French and Indian War ended in 1763 with Britain holding Canada and the Ohio country, and with a national debt that had nearly doubled during the fighting. Ministers in London looked at the new empire and at the bill together. Holding North America meant keeping an army there, some ten thousand soldiers to guard the frontier posts and the new territories, and armies are paid every year, in peace as in war. The ministry of George Grenville resolved that the colonies, defended by the victory, should carry part of that charge. Teach the fairness argument in its own terms before students judge it: from London the request looked reasonable, since the war had been fought in part on American ground. The quarrel begins not with the request but with the method chosen to collect it.")

# ------------------------------------------------------ 5 THE BILL
content_text('A revenue program, designed in London',
             ['The national debt had nearly doubled',
              'An army of some 10,000 in North America',
              'Grenville ministry, 1764 and 1765',
              'Money to be raised in America itself',
              'A break with assembly taxation'],
             "Work the fragments as a design, because design is what students must be able to describe. The Grenville program of 1764 and 1765 was a system, not a single tax: tighter customs collection, new duties, and then the Stamp Act, each part meant to make the colonies yield a regular revenue for their own defense. The break inside the design is the last fragment. For generations, colonial assemblies had voted the taxes their own people paid, granting money to the Crown as a gift of the people through their representatives. A revenue raised by Parliament directly reversed the direction of that grant. London called the change efficiency and fairness. The colonies called it a new power claimed over them, and the difference between those two descriptions is the whole lesson. Students who can state the design plainly can follow every document that answers it.",
             kick='A · The bill for victory')

# ------------------------------------------------------ 6 TEN THOUSAND STAT
stat('10,000', 'soldiers in the standing army Britain kept in North America after 1763',
     'The charge the Grenville revenue program was designed to make the colonies carry',
     "Let the figure carry the weight of Section A, and teach students what kind of fact it is. Ten thousand is the standard count of the peacetime establishment Britain kept in North America after 1763, regiments posted from Canada to Florida to hold the frontier line the Proclamation of 1763 had drawn. A standing army is a permanent charge, not a wartime emergency expense: pay, food, housing, and transport, due every year whether or not a shot is fired. That permanence is why the ministry wanted a permanent revenue rather than yearly requests to thirteen assemblies, any of which might refuse or delay. It is also why the colonies heard the program as a permanent change in their government. An army paid by Parliament, posted among them, answered to London. An army paid by assemblies answered, in part, to the people it guarded. The fight over the money was always also a fight over the army.",
     kick='A · The bill for victory')

# ------------------------------------------------- 7 SECTION B DIVIDER
divider_photo('stamps-port.jpg', 'Section B', 'The Stamp Act',
              ['A proof sheet of one penny stamps,', 'submitted for approval in May 1765.'],
              "The image is the proof sheet of one penny stamps submitted to the Commissioners of Stamps in May 1765, the trial printing of the instrument the act would use. Section B takes up the tax itself, passed in March 1765 as part of the Grenville program. Students should notice the ordinariness of the sheet: rows of small embossed stamps, a penny each, bureaucratic and neat. Nothing in the picture suggests an empire about to split. That is the teaching point. The Stamp Act worked through paper and clerks rather than soldiers, and it was defeated before it collected a penny in most colonies, defeated by argument, combination, and crowd pressure of the kind Section C and Section D take up. Keep the proof sheet in mind when students reach the resignations: the stamps existed, printed and shipped, and still were never sold.")

# ------------------------------------------------------ 8 STAMP ACT
content_text('A tax on paper, inside the colonies',
             ['Passed in March 1765',
              'Newspapers, pamphlets, legal paper',
              'Licenses and playing cards',
              'Collected through stamped paper',
              'Sold by royal distributors'],
             "Teach the act through its reach, because the reach explains the resistance. Earlier British taxes touching the colonies had fallen on trade, on goods crossing at the ports. The Stamp Act fell on paper used inside the colonies, in the ordinary business of colonial life: a newspaper, a will, a deed, a license to trade, a deck of cards. Every taxed item had to be printed or written on stamped paper bought from a royal distributor appointed in each colony, so the tax was visible at the counter every single time. The men it touched most directly were printers, lawyers, and merchants, the people who ran the newspapers, the courts, and the assemblies. A tax that falls on the printing trade is a tax on the people best placed to answer it in print, and London learned that fact within the year.",
             kick='B · The Stamp Act', size=24)

# ------------------------------------------------------ 9 STAMPED PAPER
content_text('A tax you could see on every page',
             ['The stamp carried the price',
              'No stamp, no legal document',
              'Printers and lawyers hit hardest',
              'The taxed ran the newspapers'],
             "Slow down on the mechanics, because students who picture the tax as an abstraction miss why it failed. A deed written on unstamped paper was not valid in court. A newspaper printed without the stamp broke the law on every page it sold. Compliance was not a yearly payment sent away to London; it was a daily act, performed at the distributors counter, under the eyes of neighbors who had organized against the tax. Refusal was equally public. A printer who issued a paper without stamps announced his resistance to the whole town, and printers across the colonies did exactly that once the act took effect. The act design made every transaction a small referendum on Parliament claim, held in public, every day. That is a design no tax survives when the taxed have already decided the answer, and it is why November 1, 1765, the day the act took effect, became a demonstration rather than a collection day.",
             kick='B · The Stamp Act', size=24)

# ------------------------------------------------- 10 SECTION C DIVIDER
divider_text('Section C', 'Argument and Combination',
             'Resolves, a congress of nine colonies, boycotts, and homespun.',
             "Section C gives the colonial answer in its first two registers, argument and combination, and students should keep the registers separate in their notes because the activity grades them separately. The argument was constitutional: the colonists claimed the rights of Englishmen, above all the right to be taxed only by their own consent given through representatives they had chosen. The combination was economic: merchants agreed to stop importing British goods, and households agreed to stop buying them, so the argument arrived in London as a fall in trade figures as well as a stack of petitions. Neither register worked alone. The resolves without the boycott were paper. The boycott without the resolves was a trade dispute. Together they made the case that a united colonial public, speaking law and acting on it, stood behind the refusal, and that combination is what Parliament had to answer in 1766.")

# ------------------------------------------------------ 11 ARGUMENT
content_text('Only our own assemblies can tax us',
             ['Virginia Resolves, May 1765',
              'Patrick Henry claim in the House of Burgesses',
              'Stamp Act Congress, October 1765',
              'Nine colonies at New York',
              'Rights and grievances in one voice'],
             "Teach the argument as a lawyer would build it, step by step. First premise, from the Virginia Resolves of May 1765, put forward by the young Patrick Henry: the colonists hold the rights of Englishmen. Second step: Englishmen are taxed only with their own consent, given personally or by their representatives. Third step: the colonists elect no members of Parliament and cannot, from their distance, be represented there. Conclusion, stated by the Stamp Act Congress at New York in October 1765, where nine colonies sent delegates: no taxes can be constitutionally imposed on the colonies but by their respective legislatures. Britain answer was virtual representation, the claim that members of Parliament represented all British subjects wherever they lived. Students should be able to state both arguments whole, because the unit test asks for the claim, not the slogan that later shorthand made of it.",
             kick='C · Argument and combination', size=24)

# ------------------------------------------------------ 12 COMBINATION
content_text('Boycotts, homespun, and the household front',
             ['Merchants stop importing British goods',
              'Households stop buying them',
              'Women spin and weave homespun',
              'Homespun worn as a public sign'],
             "The boycott turned an argument into a cost, and this slide names who paid the cost of making it work. Merchant agreements to stop importing British goods were signed in the port cities, but an import stop fails if households keep buying what is already on the shelves, and it fails completely if families keep ordering British cloth. The work of refusal fell largely on women, who organized spinning and weaving so that homespun could replace British textiles in daily wear. Homespun then did double duty: it clothed the family and it advertised the cause, a public sign worn in the street that the wearer household stood with the resistance. Teach the sequence plainly for the notes: argument named the right, combination enforced the argument in the marketplace, and British merchants, watching their American orders collapse, carried the colonial case into Parliament as a petition from Englishmen about English jobs and debts.",
             kick='C · Argument and combination', size=24)

# ------------------------------------------------- 13 SECTION D DIVIDER
divider_photo('repeal-port.jpg', 'Section D', 'Crowds, Resignations, and Repeal',
              ['The Repeal print of 1766: the Stamp Act', 'carried to its grave in London.'],
              "The image is the London print of 1766 showing the funeral of the Stamp Act, the repeal drawn as a burial procession. Section D adds the third register of resistance, the crowd, and then follows the repeal itself. The crowd is the register students most need to handle with care. Crowd action in 1765 was organized, targeted, and political: effigies of stamp men hung from liberty trees, distributors offices threatened, and in Boston the house of Lieutenant Governor Thomas Hutchinson wrecked in a night of destruction that shocked even leaders of the resistance. It worked. Under that pressure every stamp distributor in America resigned his post before the act took effect. But the same crowds taught London a lesson the colonies would pay for later: that colonial resistance, in British eyes, could be painted as mob rule needing soldiers to answer it.")

# ------------------------------------------------------ 14 REPEAL
content_text('Repeal, with a claim attached',
             ['Every distributor resigns',
              'November 1, 1765: no stamps sold',
              'British merchants petition Parliament',
              'Franklin testifies, February 1766',
              'Repeal and Declaratory Act, same day'],
             "Work the sequence as cause and effect, and stop hard on the last fragment. The boycott hurt British merchants, British merchants petitioned, and in February 1766 Benjamin Franklin testified before Parliament that the colonies would never submit to the stamp tax, testimony that gave wavering members a colonial voice to quote. In March 1766 Parliament repealed the act. On the same day it passed the Declaratory Act, claiming full power and authority to make laws binding the colonies in all cases whatsoever, and declaring colonial resolutions that denied that power null and void. The colonies celebrated repeal with bonfires and toasts and largely looked past the claim. Students must not look past it. The act is the hinge of the lesson and of the writing task: repeal settled a tax bill and left the constitutional claim standing, in writing, waiting for its next use.",
             kick='D · Crowds, resignations, and repeal', size=24)

# ------------------------------------------------------ 15 1766 STAT
stat('1766', 'the year Parliament repealed the Stamp Act and claimed the whole power in one day',
     'Repeal in one act · Power to bind the colonies in all cases whatsoever in the other',
     "Pause on the pairing, because holding two facts in one date is the skill this lesson builds. In March 1766 the same Parliament, on the same day, canceled the Stamp Act and passed the Declaratory Act. The repeal answered the merchants petitions and Franklin testimony: the tax was unenforceable and its cost in lost trade exceeded its yield. The Declaratory Act answered the colonial argument: it denied, in statute form, the Stamp Act Congress claim that only the assemblies could tax, by asserting a power to bind the colonies in all cases whatsoever, taxation plainly included, and by voiding colonial resolutions to the contrary. London regarded the second act as the face saving price of the first. Many colonial leaders accepted the bargain and advised quiet. The record of the next four years is the argument over which of the two acts of March 1766 stated the real settlement, and students now hold both texts to judge it.",
     kick='D · Crowds, resignations, and repeal')

# ------------------------------------------------- 16 SECTION E DIVIDER
divider_text('Section E', 'The Townshend Acts and the Farmer',
             'Duties on imports, salaries for royal officials, and a farmer reply.',
             "Section E opens the second round, and its dates discipline the story: the Declaratory Act claim stood on the books for barely a year before Parliament used it. In 1767 Charles Townshend, the minister in charge of finance, proposed duties on goods imported into the colonies, a form chosen deliberately to step around the Stamp Act defeat. Colonists had seemed to distinguish between internal taxes, laid inside the colonies, which they rejected, and external taxes on trade, which they had long paid. Townshend built on that distinction. The duties were external, collected at the ports on imports, and their yield was assigned to a purpose stated in the acts themselves: paying the salaries of royal governors and judges in America. That purpose, more than the size of the duties, is what the colonial answer fastened on, and it is where the section heads next.")

# ------------------------------------------------------ 17 TOWNSHEND
content_text('External in form, a tax in purpose',
             ['Duties of 1767 on imports',
              'Glass, lead, paint, paper, and tea',
              'Collected at the ports',
              'Revenue pays governors and judges',
              'A strike at the power of the purse'],
             "Teach the salary clause as the center of the slide, because contemporaries did. Colonial assemblies had controlled royal governors in one practical way for generations: the assembly voted the governor salary each year, and a governor who fought his assembly risked his income. The power of the purse was the assemblies working check on royal power in America. The Townshend Acts removed that check by paying governors and judges from customs revenue collected under Parliament authority, independent of any assembly vote. A governor paid from London revenue owed his living to London. Students should connect the clause back to Section A: the revenue program was never only about paying for an army. It was also about governing the colonies without depending on the colonists consent, given yearly, in their own assemblies. That is the development Dickinson answered, and it is why his answer reached for first principles rather than price lists.",
             kick='E · The Townshend Acts and the Farmer', size=24)

# ------------------------------------------------------ 18 DICKINSON
content_text('A tax in any form, if revenue is the purpose',
             ['Letters from a Farmer, 1767 and 1768',
              'Written by John Dickinson of Pennsylvania',
              'A duty to levy money is a tax',
              'Massachusetts Circular Letter, 1768'],
             "Dickinson Letters gave the resistance its second argument, sharper than the first. Writing as a Pennsylvania farmer through the winter of 1767 and 1768, John Dickinson granted what the Townshend design assumed: Parliament may lay duties to regulate trade, as it had always done. He then drew the line the duties had crossed. A duty laid for the single purpose of levying money is not regulation but taxation, whatever its form and wherever it is collected, and taxation belongs to the assemblies under the argument of 1765. Apply the test and the Townshend Acts fail it on their own stated purpose, since their preamble assigns the money to salaries and defense. The Massachusetts Circular Letter of February 1768 carried the argument to the other assemblies, and London order to rescind it only spread it further. Students now have two colonial arguments, consent and purpose, and one British claim, in all cases whatsoever, still unrepealed.",
             kick='E · The Townshend Acts and the Farmer', size=24)

# ------------------------------------------------- 19 SECTION F DIVIDER
divider_photo('revere-port.jpg', 'Section F', 'Troops and Blood in Boston',
              ['Revere engraving of the Massacre,', 'printed in Boston in 1770.'],
              "The image is Paul Revere engraving of the Boston Massacre, after a drawing by Henry Pelham, printed and sold in Boston within weeks of the shooting. Section F follows the quarrel from paper to blood. In 1768 the ministry sent two regiments to Boston to back the customs men collecting the Townshend duties, and quartered them in a town of some sixteen thousand people that had not asked for them and did not want them. Soldiers took part time work from Boston laborers, customs men seized a merchant ship, and street fights between soldiers and townspeople built month by month. The engraving on screen shows where that friction ended on the night of March 5, 1770. Teach students to read it as an argument made in pictures, a line of soldiers firing in order into an unarmed crowd, and to hold it against the sworn accounts the activity sets beside it.")

# ------------------------------------------------------ 20 BOSTON NIGHT
content_text('The night of March 5, 1770',
             ['Two regiments posted since 1768',
              'A crowd outside the Custom House',
              'Taunts, ice, and debris thrown',
              'The soldiers fire',
              'Five men dead, Crispus Attucks among them'],
             "Reconstruct the night plainly and in order. A lone sentry stood guard outside the Custom House on King Street. A crowd gathered, taunting him, and a small guard under Captain Thomas Preston came to his support. The crowd pressed in, shouting for the soldiers to fire, throwing ice, snowballs, and debris, in a street lit by moonlight and full of noise from church bells rung to call people out. Shots followed, in what order and on whose word the record disputes. Three men died on the spot and two more of their wounds: Crispus Attucks, a sailor of African and Native descent, Samuel Gray, James Caldwell, Samuel Maverick, and Patrick Carr. Name all five for students. The lesson record keeps the event at the scale of a street guard overwhelmed, and the name massacre, fixed by Revere print, as the Patriot verdict on it. Both facts belong in the notes.",
             kick='F · Troops and blood in Boston', size=24)

# ------------------------------------------------------ 21 FIVE STAT
stat('5', 'men killed by the soldiers fire on King Street, March 5, 1770',
     'Three died on the spot · Two died of their wounds · Crispus Attucks among them',
     "Let the small number sit beside the large numbers elsewhere in the course, because its smallness is instructive. Five deaths is a street tragedy, not a battle, and yet the night of March 5 was remembered, named, and commemorated in Boston every year until independence, because of what the five deaths proved to the colonial public: that the Declaratory Act claim, backed by regiments quartered in a town, ended with soldiers firing on the people the revenue system taxed. Teach the commemorations as part of the record: annual Massacre Day orations kept the night in political memory through the quiet years of Section G, when little else seemed to be happening. The number also disciplines students language. The record supports a crowd that taunted and threw ice and debris, soldiers who fired without a proven order, and five dead men. Precision about a famous night is a form of respect for it.",
     kick='F · Troops and blood in Boston')

# ------------------------------------------------------ 22 TRIAL
content_text('Two accounts, and a Boston jury',
             ['Preston: no order to fire was given',
              'Drowne: the order was heard and sworn to',
              'John Adams defends the soldiers',
              'Two convicted, branded; six acquitted'],
             "Close Section F with the dispute and the verdict, in that order. Captain Preston, writing from jail for a London audience, swore he stood between his men and the crowd and ordered them not to fire, and that the men fired on hearing the word fire shouted from the crowd itself. Samuel Drowne, swearing before a Boston committee gathering depositions for London, testified that he heard Preston order the firing in so many words. The activity sets the two texts side by side and asks students to weigh them. Then give the verdict its full weight: John Adams, a leader of the resistance, defended the soldiers, and a Boston jury convicted two of manslaughter, branded on the thumb, and acquitted six. A movement that claimed British rights submitted its worst night to British justice, and the split verdict is evidence about 1770 that no engraving can supply.",
             kick='F · Troops and blood in Boston', size=24)

# ------------------------------------------------- 23 SECTION G DIVIDER
divider_text('Section G', 'The Quiet Years',
             'The duties repealed but one, the principle kept, and the wires laid.',
             "Section G closes the lesson in an apparent calm that the documents show to be a rearming. In 1770 the ministry of Lord North repealed the Townshend duties on glass, lead, paint, and paper, keeping only the duty on tea. The kept duty was small in yield and large in meaning: it held the Declaratory Act principle in force in a single article of trade, so that drinking taxed tea conceded the claim and refusing it kept the argument alive at the breakfast table. Trade revived, crowds thinned, and the imperial crisis seemed to cool. Under the calm, the colonies built the machinery of the next crisis: committees of correspondence, formed in 1772 and 1773, to share news and coordinate answers across colony lines. When the tea itself became the crisis in 1773, the committees were already standing. The next lesson begins with the ships.")

# ------------------------------------------------------ 24 QUIET YEARS
content_text('Repeal again, and the tea kept',
             ['Townshend duties repealed, 1770',
              'The tea duty kept, to hold the principle',
              'Trade revives, crowds thin',
              'Committees of correspondence, 1772 and 1773',
              'The colonies wired together'],
             "Work the fragments as a balance sheet of the whole lesson, because the writing task draws its closing evidence here. Gained by the colonies since 1765: two revenue programs repealed in large part, a stated constitutional argument tested in congresses, letters, and a courtroom, and a working system of intercolonial communication that had not existed when the Stamp Act passed. Kept by Britain: the Declaratory Act claim, unrepealed and now embodied in one small duty on tea, a standing army in America, and governors and judges whose salaries London still meant to free from assembly control. Neither side had surrendered its rule about who may tax. That is the precise sense in which repeal did not end the quarrel, and students who can state the balance sheet in those terms are ready for the activity ledger and the essay. The tea ships of the next lesson sail into exactly this unfinished settlement.",
             kick='G · The quiet years', size=24)

# ------------------------------------------------------ 25 SYNTHESIS
content_text('A tax settled, a claim left standing',
             ['Britain taxed to pay for war and an army',
              'The colonies answered: consent, or no tax',
              'Argument, combination, and the crowd',
              'Repeal removed the tax, not the claim',
              'Boston showed the price of enforcing it'],
             "Build the synthesis as the answer to the lesson question, in the question own order. Britain taxed the colonies after 1763 because the French and Indian War had nearly doubled the national debt and left a standing army of some ten thousand soldiers to pay for, and the Grenville program set out to raise that money in America. The colonists resisted because the taxes broke the standing practice of their political lives: they had been taxed by assemblies they elected, and the new taxes came from a Parliament they had no voice in choosing, laid first directly on their paper and then, after repeal, on their imports for the stated purpose of revenue. Their answer ran in three registers, argument, combination, and crowd action, and it won two repeals. It did not win the principle. The Declaratory Act claim stood, the tea duty embodied it, and Boston in 1770 showed what enforcing the claim could cost in blood.",
             kick='G · The quiet years')

# ------------------------------------------------------ 26 VOCAB A
vocab('Words for the taxes and the claim',
      [('Stamp Act', 'taxed printed paper, collected through royal stamps'),
       ('repeal', 'a law canceled by the authority that made it'),
       ('Declaratory Act', 'Parliament claim of power in all cases whatsoever'),
       ('Townshend Acts', 'duties on imports that paid royal officials')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. Stamp Act: the British law of 1765 that taxed printed paper in the colonies, including newspapers, legal documents, and playing cards, collected through stamps sold by royal distributors. repeal: the canceling of a law by the authority that made it, as Parliament canceled the Stamp Act in 1766 under pressure from colonial resistance and British merchants. Declaratory Act: the British law of 1766, passed the same day as the Stamp Act's repeal, declaring that Parliament had power to make laws for the colonies in all cases whatsoever. Townshend Acts: the British laws of 1767 that taxed imports into the colonies, including tea, glass, lead, paint, and paper, and used the revenue to pay royal governors and judges.")

# ------------------------------------------------------ 27 VOCAB B
vocab('Words for the answer and the night',
      [('boycott', 'refusal to buy, used as protest'),
       ('virtual representation', 'Parliament claim to represent all subjects'),
       ('Boston Massacre', 'five colonists killed, March 5, 1770')],
      "Three more terms, again matching the guided notes exactly. boycott: a refusal to buy goods or use services as a form of protest, meant to pressure an institution by withdrawing the money and cooperation it depends on. virtual representation: the British argument that members of Parliament represented all British subjects, including the colonists, whether or not the colonists had voted for them. Boston Massacre: the clash of March 5, 1770, in which British soldiers fired into a Boston crowd that had surrounded and taunted them, killing five colonists. Students should hold the chain these definitions make when read with the first vocabulary set: a tax on paper, answered by a boycott and repealed, a claim of unlimited power stated the same day, new duties that tested the claim, a British argument that answered the colonial one without conceding it, and a night in Boston that gave the quarrel its martyrs and its most famous picture.")

# ------------------------------------------------------ 28 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Work the tax file', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Why did repeal in 1766 not end the quarrel? Work the five records in order, then judge which document best explains the failure of repeal.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Tax File: the Congress, the Declaratory Act, Dickinson, two accounts of March 5, and the engraving'),
        ('Notebook', 'Notebook page: six pieces of the crisis, classified and evidenced'),
        ('Quick check', 'Two Accounts of One Night: Preston against Drowne, with the trial behind them'),
        ('Writing', 'Why Repeal Did Not End the Quarrel: the claims of 1765 and 1766 weighed against the record')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the Stamp Act stated, the same day pairing explained, and the lesson question answered with one event after 1766.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Tax File, runs five stations through the evidence: the Stamp Act Congress declaration of 1765 from the Avalon Project transcription, the Declaratory Act of 1766 from the same source, Dickinson Letter II in the transcription recorded in the lesson source file, the opposed accounts of Preston and Drowne from the audited bank records, and Revere engraving as the bank record describes it, ending in a ledger and a verdict on which document best explains why repeal did not end the quarrel. The notebook page asks students to rebuild six pieces of the crisis with evidence. The quick check tests Preston against Drowne. The writing task weighs the claims of 1765 and 1766 against the Townshend record and the tea duty kept in 1770. The exit ticket has three parts: the Stamp Act defined; the same day pairing of repeal and the Declaratory Act explained; and the lesson question answered with one event after 1766.")

dc.save(OUT)
