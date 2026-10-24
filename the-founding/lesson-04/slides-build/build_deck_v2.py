#!/usr/bin/env python3
"""The Founding Lesson 4 deck, "The War for Independence,"
V2 (2026-10-24 rollout, improved slide standard): content bullets are
short complete sentences; speaker notes applied after the build from the
teacher notes guide (apply_guide_notes.py). Same 29 slides, same order."""
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
OUT = os.path.join(HERE, '..', 'lesson-04-slides-v2.pptx')

def content_photo_s(img, title, items, note, kick=None):
    s = slide(CREAM)
    photo_right(s, img)
    if kick: kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95 if kick else 0.8, 6.9, 1.2, title, size=30, color=NAVY, font='Georgia', leading=1.05)
    frags(s, items, y=2.12 if kick else 2.0, size=21, gap=11, leading=1.2)
    notes(s, note)
    return s

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
text(s, 0.9, 5.32, 11.5, 0.4, 'THE FOUNDING · LESSON 4', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The War for Independence', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Survival, Saratoga, the alliance, the southern turn, and Yorktown, 1776 to 1783', size=17, color=POWDER)
notes(s, "The image is Emanuel Leutze's Washington Crossing the Delaware, painted in 1851, seventy five years after the Christmas night crossing it shows, and students should hear that date whenever the painting appears in this lesson: it is a commemoration, not a record of the night. The lesson it opens asks how the weakest side in a war against the world's strongest empire first survived and then won. Teach the two halves in that order. Survival came first, through 1776 and the Valley Forge winter, and it was Washington's strategy, keeping an army in being, that made survival a plan rather than an accident. Winning followed from what survival produced: proof at Saratoga, allies in Paris, a southern campaign that herded Cornwallis to a coast, and a fleet waiting off it.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("How did the United States survive a war against the world's strongest empire, and win it?", {})]],
     size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('Why did the colonies break with Britain, and what did Americans build in the place of the empire they rejected?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "The lesson question joins two questions students often separate, and the joining is the lesson. Survival asks how a cause with no taxing power, an army enlisted by the year, and a sliding currency kept an army in the field for eight years against the strongest navy in the world, a funded treasury, and a professional army reinforced by hired German auxiliaries. Winning asks how that survival was converted, between October 1777 and October 1781, into an alliance, a widened war Britain could not hold, a southern campaign that stripped Cornwallis of the Loyalist strength his strategy rested on, and a surrender under a French fleet. Keep both verbs visible all hour. An answer that only survives explains 1778 and cannot explain Yorktown. An answer that only wins skips the years when there was nearly nothing left to win with.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Survive first, then win', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The odds against survival', 'The strongest empire against a Congress that could not tax'),
        ('B', 'Disaster in 1776', 'Long Island, New York, Fort Washington, the retreat'),
        ('C', 'Trenton and Princeton', 'Christmas night 1776; a cause restocked'),
        ('D', 'Saratoga, the turning year', 'Burgoyne surrenders, October 17, 1777'),
        ('E', 'Alliance and endurance', 'France enters; Valley Forge; Monmouth'),
        ('F', 'The war moves South', 'Charleston and Camden; King\u2019s Mountain, Cowpens, Greene'),
        ('G', 'Yorktown and the peace', 'The surrender, 1781; the Treaty of Paris, 1783')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "The map follows the guided notes section by section. Section A states the odds and Washington's strategy of keeping an army in being. Section B spends the strategy nearly to death in 1776, at Long Island, New York, and Fort Washington. Section C restocks the cause at Trenton and Princeton. Section D turns the war in 1777, when Burgoyne's surrender at Saratoga gave France its proof. Section E joins the alliance of February 1778 to the endurance of Valley Forge and the standstill at Monmouth. Section F follows the war South, through the disasters of 1780 to King's Mountain, Cowpens, and Greene's wearing campaign. Section G closes the trap at Yorktown and writes the result into the Treaty of Paris of September 3, 1783.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_photo('faden-port.jpg', 'Section A', 'The Odds Against Survival',
              ['The strongest empire in the world, against a Congress', 'that could not tax and an army enlisted by the year.'],
              "The image is a detail of William Faden's map of the country in which Burgoyne's army acted in the campaign of 1777, published at London in 1780 and held by the Library of Congress. It is a British map of the war's northern theater, drawn by the winning side's enemy, and it opens the lesson because the odds in this section are best stated in Britain's own expectation: this was a rebellion to be marched through and finished. State the frame before any battle. Britain held the world's strongest navy, a funded treasury, a professional army, and hired German auxiliaries. The United States held a Congress that could not tax, short enlistments, militia bound to home ground, and paper money already sliding. Every later event in this lesson is arithmetic working itself out.",
              title_size=34)

# ------------------------------------------------------ 5 THE ODDS
content_text('Two armies, two tasks',
             ['Britain fielded the strongest navy, a funded treasury, and professional soldiers.',
              'German auxiliaries were hired to reinforce the army.',
              'America had a Congress that could not tax.',
              'Its army was enlisted by the year, often unpaid, with militia serving near home.',
              'Washington\u2019s answer was to keep an army in being.'],
             "Work the fragments as two different wars being fought inside one. Britain's task was conquest: destroy Washington's army outright or hold a continent of hostile ground with supply lines across an ocean, and do it at a price Parliament would keep paying. Washington's task was existence. The Americans could lose every city, and did lose New York and Philadelphia, and still win, because a rebellion with an army in the field has not been beaten, however much ground it has surrendered. That asymmetry explains his generalship, which students often misread as timidity: he refused the battle that could end the war in an afternoon unless the ground or the moment favored him, attacked in winter strokes like Trenton instead, and treated retreat as an instrument. The militia and the Continental Army divided the labor inside that strategy, part time soldiers near home for local surges, enlisted Continentals for the army that had to stay in being, a division the vocabulary slides state in the guided notes wording.",
             kick='A · The odds against survival', size=24)

# ------------------------------------------------- 6 SECTION B DIVIDER
divider_text('Section B', 'Disaster in 1776',
             'Long Island, New York City, and Fort Washington lost in one season, and the army retreats across New Jersey with its enlistments running out.',
             "Frame 1776 as the strategy tested to destruction, because students who meet Trenton first will mistake the year for a triumph with a rough start. The British descent on New York was the largest expeditionary force Britain had ever sent overseas, and it was used professionally: a flanking march at Long Island that beat the American army in the open field, a night evacuation that saved the army and surrendered the city, and the capture of Fort Washington with its whole garrison in November, the year's worst single loss. What followed was arithmetic again, enlistments expiring on schedule while the army marched away from the enemy. By December the force that had besieged Boston numbered a few thousand effectives. Paine's sentence for the season, that these were the times that tried men's souls, was written as recruitment copy in a collapsing cause.")

# ------------------------------------------------------ 7 1776
content_text('The year of losing, 1776',
             ['In August the Americans were beaten at Long Island, and the army escaped by night.',
              'New York City was lost, and the army stayed intact.',
              'In November Fort Washington fell with its whole garrison.',
              'The army retreated across New Jersey as enlistments expired.',
              'By December only a few thousand effectives remained.'],
             "Teach the escape across the East River as the year's most consequential event, ahead of any battle. On the night after Long Island, Washington ferried his army off Brooklyn Heights in boats, in fog and darkness, with the British fleet kept off by wind, and lost the city without losing the army, which is the strategy of Section A executed under fire. Fort Washington's fall in November is the counterweight: a post held against advice, surrendered with its whole garrison, men the cause could not replace as easily as ground. Then make the retreat concrete. This was not a maneuver between armies at full strength. It was a shrinking force crossing a state in early winter, its soldiers' terms expiring by the calendar, its commander writing to Congress for men who were not coming. The question Trenton answers in the next section is not how to win the war. It is whether there would be an army in January.",
             kick='B · Disaster in 1776', size=24)

# ------------------------------------------------- 8 SECTION C DIVIDER
divider_text('Section C', 'Trenton and Princeton',
             'Two small victories in nine days, won by an army that was weeks from dissolving, and worth more than the ground they took.',
             "Introduce the counterstroke as a decision made from weakness, not strength, because that is what makes it instructive. Washington's army in late December 1776 was melting on a schedule written into its enlistments. Doing nothing meant commanding a dissolving force by New Year. The Delaware crossing was a gamble taken because the alternative was certain: a night march through a storm, an ice choked river, and a dawn attack on a garrison post, chosen because Trenton's Hessian garrison was isolated, its support a day's march away, and its vigilance lowered by the season. The second stroke at Princeton was improvisation inside the first plan's success, slipping around Cornwallis's advancing army by night with campfires left burning. Neither victory retook a city or destroyed an army. Section C asks what small victories can purchase when a cause is priced in belief.")

# ------------------------------------------------------ 9 TRENTON
content_photo_s('leutze-port.jpg', 'Christmas night, and Princeton',
             ['On Christmas night 1776 the army recrossed the Delaware through ice.',
              'At dawn at Trenton the Hessian garrison was taken.',
              'Campfires were left burning while Cornwallis was slipped by night.',
              'At Princeton on January 3, 1777, a second victory came in nine days.'],
             "The painting is Leutze's Washington Crossing the Delaware of 1851, shown in the reading with its date, and its details are a commemoration's details: the flag, the boat, and the river are all wrong for 1776, and the crossing happened at night in a storm. The event underneath it needs no help. Some 2,400 men crossed in Durham boats through floating ice, marched nine miles in sleet, and took Trenton at dawn with its garrison, at a cost the returns put in single figures for American dead. Princeton followed by audacity rather than plan: Cornwallis advanced to trap the army against the Delaware, and Washington marched around him in the dark, leaving fires burning and wheel tracks muffled, to strike the British rear guard. State the yield plainly at the end: recruits reenlisted, Congress recovered its nerve, supplies and credit moved again. The victories restocked the cause. They did not yet change the war's balance, which is Section D's work.",
             kick='C · Trenton and Princeton')

# ------------------------------------------------------ 10 STAT 2400
stat('2,400', 'men who recrossed the Delaware with Washington, Christmas night 1776',
     'Trenton at dawn · Princeton nine days later · An army restocked, not a war yet won',
     "Use this number for scale, because Trenton's fame can inflate it into a great battle and it was a raid by a remnant. The 2,400 were what remained of an army that had besieged Boston the year before with several times that strength, and they were days from the end of their enlistments. That is the figure's teaching value: the Revolution's most celebrated stroke was made by the fraction of the cause that had not yet gone home. The return on the stroke was out of all proportion to its size, and students should be able to name the return precisely: captured soldiers and stores, an enemy taught that winter quarters were not safe, enlistments extended and recruits raised, and a Congress and a country persuaded to fund another campaign. When students call Trenton a turning point, require the follow up: turned what, from what, into what. The answer is morale and credit, not territory, and distinguishing the two is this section's discipline.",
     kick='C · Trenton and Princeton')

# ------------------------------------------------- 11 SECTION D DIVIDER
divider_photo('burgoyne-port.jpg', 'Section D', 'Saratoga, the Turning Year',
              ['A British army marches south from Canada to cut the states in two,', 'and surrenders whole in upper New York.'],
              "The painting is John Trumbull's Surrender of General Burgoyne, completed in 1821 for the Capitol Rotunda, a commemoration painted more than forty years after the surrender it shows, with Burgoyne offering his sword in a ceremony arranged for the canvas. The event it honors decided the war's diplomacy. Britain's plan for 1777 was sound on the map: seize the Hudson valley, cut New England off from the states that fed the rebellion's politics, and end the war by partition. Its execution split in two, Burgoyne marching south from Canada on schedule while Howe, whose orders left him discretion, sailed to take Philadelphia instead of marching north to meet him. Teach the plan's failure as a failure of coordination across an ocean's delay, not of courage: two British armies campaigned in the same season toward different wars, and only one of them was destroyed.",
              title_size=34)

# ------------------------------------------------------ 12 THE PLAN
content_text('The plan that split in two',
             ['The plan was to seize the Hudson and cut New England off.',
              'Burgoyne marched south from Canada, and Howe was to meet him.',
              'Howe sailed instead, took Philadelphia, and changed nothing.',
              "Burgoyne's line stretched thin through Bennington and Freeman's Farm.",
              'On October 17, 1777, the army surrendered at Saratoga.'],
             "Follow Burgoyne's supply line as the explanation, because the surrender was logistics completing itself. Every mile south from Canada lengthened a line of lakes, portages, and forest roads behind him, guarded by men subtracted from the army at the front, while the country he entered supplied his enemy: American militia turned out in thousands as he advanced, cut up his foraging detachments at Bennington, and fought his army to exhaustion at Freeman's Farm. Howe's capture of Philadelphia belongs in the same lecture as a null result: the rebel capital taken, Congress fled, the war unchanged, because capitals were not the rebellion's center of gravity; Washington's surviving army was, and it wintered twenty miles away at Valley Forge. When Burgoyne surrendered on October 17, 1777, an entire British army laid down its arms, the first such surrender of the war, and the news reached Paris in December. What France did with it is Section E.",
             kick='D · Saratoga, the turning year', size=24)

# ------------------------------------------------------ 13 STAT 5800
stat('5,800', 'men surrendered with Burgoyne at Saratoga, by the standard count',
     'October 17, 1777 · A British army taken whole · The proof France had been waiting for',
     "State this figure with its label, as the reading does: some 5,800 men, by the standard count, the number the lesson asserts, with the armies' returns behind it and small variations among them that students should expect in any eighteenth century count. The figure's weight is comparative. Britain could replace regiments; it could not quickly replace an army, its artillery, and its prestige in one surrender, least of all with the war about to widen. Saratoga also reversed the meaning of the American militia in European eyes: the force that had cut Burgoyne up in the woods around his line was substantially militia surging beyond its home counties, joined to Continentals who held the fortified camp he could not break. France had supplied the Americans quietly since 1776. What it had withheld was recognition and open war, and it withheld them until an American army proved it could take a British one. That proof is what 5,800 counts.",
     kick='D · Saratoga, the turning year')

# ------------------------------------------------- 14 SECTION E DIVIDER
divider_text('Section E', 'Alliance and Endurance',
             'France signs on February 6, 1778, and the same winter the army that earned the alliance nearly starves in Pennsylvania.',
             "Hold this section's two halves together, because their coincidence is the war's hinge. The Treaty of Alliance was signed at Paris on February 6, 1778, six weeks after the Saratoga news arrived, by a monarchy that had calculated the rebellion's chances for two years and now judged them worth a war with Britain. In the same months, the army whose victory had purchased the treaty was wintering at Valley Forge, short of food, clothing, and shelter, losing men to disease at a rate no battle of the war matched. Neither half cancels the other. The alliance without the endurance would have joined a dissolving army; the endurance without the alliance would have prolonged a war of survival with no road to a decision. Students should leave this section able to state what each half supplied the other, in dates.")

# ------------------------------------------------------ 15 FRANCE ENTERS
content_text('France enters, the war widens',
             ['On February 6, 1778, the Treaty of Alliance was signed.',
              'France recognized the United States and sent money, ships, and soldiers.',
              'Article 8 barred a separate peace until independence was assured.',
              'Spain followed against Britain in 1779.',
              'The war widened to the Caribbean, Gibraltar, and India.'],
             "Read the treaty's own terms at Station 2 of the activity, Articles 1, 2, and 8 in the Avalon transcription, before summarizing them here. Article 2 states the end in the treaty's words: to maintain effectually the liberty, sovereignty, and independence absolute and unlimited of the United States. Article 8 is the clause with a battlefield inside it: neither ally will lay down its arms until American independence is assured by the peace, which meant France had bound its war to the American object, and it is that clause that stands behind the French fleet off Yorktown three years later. The widening after 1779 changed Britain's arithmetic everywhere: convoys to protect, Gibraltar besieged, India and the Caribbean to defend, and a navy suddenly outnumbered in American waters at the season it mattered most. French gold also kept Congress's credit alive. None of this fired a shot for Washington in 1778, and its first American dividend was time.",
             kick='E · Alliance and endurance', size=24)

# ------------------------------------------------------ 16 VALLEY FORGE
content_photo_s('forge-port.jpg', 'Valley Forge, the winter test',
             ['Some two thousand died, the figure stated as an estimate.',
              "Waldo's diary records provisions scarce and a camp crying No Meat.",
              'Steuben drilled the survivors into one body.',
              'In June 1778 Monmouth was fought to a standstill.'],
             "The image is an 1830 engraving of the encampment, made half a century after the winter, and the lesson's record of the winter itself is a surgeon's diary, read at Station 3. Albigence Waldo, a Connecticut surgeon writing for himself in December 1777, records an army growing sickly from the campaign's fatigues and still showing, in his words, a spirit of alacrity and contentment, and a week later a camp crying No Meat, with dinner and supper answered as fire cake and water. Use his two entries to hold the winter's two truths together: the suffering was administrative, a supply system failing men who mostly did not desert, and the army's cohesion was the achievement. Steuben's drilling then converted survival into capability, one manual, one model company, one battalion at a time, and the proof came at Monmouth in June 1778, where the army that marched out fought formed British regulars to a standstill in open battle.",
             kick='E · Alliance and endurance')

# ------------------------------------------------------ 17 STAT 2000
stat('2,000', 'men died at Valley Forge, the figure stated as an estimate',
     'Disease, hunger, and exposure, not battle · The army marched out in June and fought at Monmouth',
     "Teach this figure's label before its size: an estimate, the number the lesson states for deaths from disease, hunger, and exposure in the winter encampment, drawn from the camp's returns and the record's limits, and students should repeat it with the label attached, as the reading and the writing task require. Its composition instructs more than its total. The British army twenty miles away in Philadelphia was fed by sea. The American army starved in a farming country because Congress could not tax, its currency would not buy, and its wagons and commissaries failed, the odds of Section A arriving as a body count. The winter's other fact belongs on the same slide in students' answers: the army did not dissolve. Men whose enlistments ran out reenlisted or stayed past them, the sick were nursed by the camp's own people, and the force that buried its two thousand marched out in June drilled, uniform in method if not in cloth, and fought at Monmouth within the month.",
     kick='E · Alliance and endurance')

# ------------------------------------------------- 18 SECTION F DIVIDER
divider_text('Section F', 'The War Moves South',
             'Britain shifts its weight to the South, counting on Loyalist strength, wins its two greatest victories, and loses the strategy anyway.',
             "Explain the southern turn as a rational strategy meeting a country it misread. After 1778, with France in the war and the northern war stalemated, Britain counted on the South: Loyalists believed numerous there, ports to hold, and a rolling reconquest colony by colony behind regular bayonets. The first returns justified the plan. Savannah fell in 1778, Charleston fell in May 1780 with an entire American army, the worst American defeat of the war, and Camden destroyed a second army that August. What the strategy required next was the country's submission, and the backcountry refused it. This section's story is the refusal: militia war at King's Mountain, Morgan's crafted victory at Cowpens, and Greene's campaign of losing battles at prices Cornwallis could not keep paying, until the victor of the South abandoned it and marched to the coast at Yorktown.")

# ------------------------------------------------------ 19 THE SOUTH
content_text('The South, lost and answered',
             ['Savannah fell in 1778, and Charleston fell in May 1780 with an army inside it.',
              'At Camden in August 1780 a second army was destroyed.',
              "At King's Mountain in October 1780 militia destroyed a Loyalist force.",
              "At Cowpens in January 1781 Morgan wrecked Tarleton's legion.",
              'Morgan\u2019s report counted 12 killed against more than 500 taken.'],
             "Set the sequence's rhythm before its details: two catastrophes, then two answers, each answer of a different kind. King's Mountain was the militia's war entire, backcountry riflemen surrounding and destroying the Loyalist force that screened Cornwallis's left, and its effect was recruiting: Loyalist militia could no longer be raised in safety. Cowpens was craft. Morgan, who understood his militia's limits, built the battle around them, asked two volleys and a planned retirement, and destroyed Tarleton's legion when the British charged into the Continental line and the cavalry waiting behind it. His report, read at Station 4 in the Founders Online transcription, gives the arithmetic he sent Greene: his own loss inconsiderable, 12 killed and 60 wounded, against upwards of a hundred enemy killed, two hundred wounded, and more than five hundred prisoners with the legion's guns, colors, and wagons. A detachment does not lose those numbers and remain a detachment. Cornwallis's striking arm was gone a week before Greene's campaign began.",
             kick='F · The war moves South', size=24)

# ------------------------------------------------------ 20 GREENE
content_text('Greene wears Cornwallis down',
             ['Greene took the southern command after Camden.',
              'Guilford Courthouse was a British victory at a ruinous price.',
              'He waged a campaign of retreat the British could not afford.',
              'Cornwallis abandoned the Carolinas and marched into Virginia.',
              'He refit at Yorktown, on the coast, under no fleet.'],
             "Teach Greene's campaign as the strategy of Section A practiced by Washington's chosen subordinate, with the map doing the arguing. Greene split a weak army, accepted battle only where the price favored him, and at Guilford Courthouse in March 1781 lost the field while costing Cornwallis a quarter of the army he could not reinforce, a victory its winner had to abandon the Carolinas to survive. The retreat that followed was not flight: it was the American army staying in being across a state, drawing its pursuer away from his supplies, and choosing the war's terms week by week. Cornwallis's march into Virginia was a search for a decision the South had denied him, and it ended at a tobacco port on the York River, chosen because the Royal Navy was expected to command the Chesapeake. The expectation was reasonable in every month of the war except the one that arrived. Section G is about that month.",
             kick='F · The war moves South', size=24)

# ------------------------------------------------- 21 SECTION G DIVIDER
divider_photo('bauman-port.jpg', 'Section G', 'Yorktown and the Peace',
              ['The armies march south, the French fleet seals the Chesapeake,', 'and the war\u2019s last army surrenders inside the lines on this plan.'],
              "The image is Sebastian Bauman's plan of the investment of York and Gloucester, surveyed in the week after the surrender, October 22 to 28, 1781, published at Philadelphia in 1782, and held by the Library of Congress. Bauman was the American artillery officer who laid out the siege's works, and his plan, read at Station 5, shows the trap as engineering: two parallels of trenches approaching the British lines, American works in one color, French in another, the town and the river at their backs. Set the scene from the plan outward. Cornwallis held Yorktown with the sea behind him and expected the Royal Navy through it. In September 1781 the navy that arrived was French, de Grasse's fleet out of the Caribbean, which beat the British fleet off the Chesapeake capes and closed the water. The armies on the plan then did the rest.",
              title_size=34)

# ------------------------------------------------------ 22 THE TRAP
content_photo_s('cornwallis-port.jpg', 'The trap closes, October 1781',
             ['Washington and Rochambeau marched from New York to Virginia.',
              "De Grasse's fleet sealed the Chesapeake against rescue.",
              'Some 17,000 allied troops stood around 8,000, the standard counts.',
              'The bombardment opened October 9, and the surrender came October 19.'],
             "The painting is John Trumbull's Surrender of Lord Cornwallis, completed in 1820 for the Capitol Rotunda, and students should place it as they placed Leutze and the Burgoyne canvas: a commemoration arranged decades later, with General Lincoln receiving the surrender at center because Cornwallis, pleading illness, sent his subordinate O'Hara to march the army out. The surrender's famous music belongs in the same category of care: tradition holds that the British band played The World Turned Upside Down as it marched between the French and American lines, and the lesson teaches that story as tradition, not record, a distinction stated in the reading and required in student answers. What the record carries is arithmetic and dates: allied armies converging from New York, a fleet closing the river, parallels opened in the first week of October, the bombardment from October 9, redoubts stormed on the fourteenth, and a garrison of some eight thousand surrendered on October 19, 1781, four years almost to the day after Saratoga.",
             kick='G · Yorktown and the peace')

# ------------------------------------------------------ 23 STAT 17000
stat('17,000', 'American and French troops around Cornwallis\u2019s 8,000 at Yorktown, standard counts',
     'A French fleet behind them · The surrender, October 19, 1781',
     "State both figures with their shared label, the standard counts, as the reading states them: some seventeen thousand American and French troops around Cornwallis's eight thousand. The ratio is the least interesting thing about them. The composition is the lesson: roughly half the besieging army was French, regulars under Rochambeau who had marched from Rhode Island, paid in French coin, supported by a French siege train, behind a French fleet that had sailed from the Caribbean for this one season. Yorktown is the alliance of Section E rendered as a headcount. It is equally the survival of Sections B, C, and E rendered the same way: the American half of the ring was the army that had been kept in being since 1776, drilled at Valley Forge, and marched the length of the war to be standing on this ground. Neither half closes the trap without the other, and students' rankings in the activity will be graded on keeping both in the account.",
     kick='G · Yorktown and the peace')

# ------------------------------------------------------ 24 THE TREATY
content_text('The Treaty of Paris, September 3, 1783',
             ['Article 1 has the king acknowledge free, sovereign, independent states.',
              'The boundary ran to the Mississippi River and the Great Lakes.',
              'Fishing rights off Newfoundland were kept, and the Mississippi opened.',
              'Debts were protected, and Loyalist property was recommended for return.',
              'The states would honor the terms unevenly.'],
             "Read the treaty's first article at Station 5 in the Avalon transcription, because the recognition is the document's own sentence: the king acknowledges the thirteen named states to be free sovereign and independent states and relinquishes all claims to their government and territory. The rest of the settlement distributed the winnings: a boundary at the Mississippi and through the Great Lakes, fishing rights off Newfoundland, the Mississippi's navigation opened to both countries, and creditors on either side protected in recovering their debts. Article 5's treatment of confiscated Loyalist property was a recommendation Congress could only pass to the states, and Article 7's withdrawal clause counted enslaved people among the property not to be carried away, wording written against the Black Loyalists who had reached British lines on British promises. The states honored the debt and Loyalist terms unevenly, as the reading closes by saying, and the next lessons inherit the consequences: a peace the Confederation could sign and could not enforce.",
             kick='G · Yorktown and the peace', size=24)

# ------------------------------------------------------ 25 AT A GLANCE
s = slide(NAVY)
kicker(s, 'The winning at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Survived, then won', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The army survives', 'Trenton and Princeton; Valley Forge endured', 'An army in being through 1776 and the winter of 1777 and 1778'),
        ('Proof and alliance', 'Saratoga, October 17, 1777; the alliance, February 6, 1778', 'Some 5,800 surrendered, standard count; France enters with money, ships, soldiers'),
        ('The South answers', 'King\u2019s Mountain, Cowpens, Greene\u2019s campaign', 'Charleston and Camden answered; Cornwallis driven to Virginia'),
        ('Yorktown and peace', 'The surrender, October 19, 1781; Paris, September 3, 1783', 'Some 17,000 around 8,000, standard counts; recognition and the Mississippi line')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.2, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.25, yy + 0.05, 5.1, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.55, yy + 0.05, 3.9, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the closing table of the guided notes, The Winning at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The army survives: the defeats of 1776, Trenton on Christmas night and Princeton on January 3, and the Valley Forge winter endured with some two thousand dead, the figure stated as an estimate. Proof and alliance: Burgoyne's surrender at Saratoga on October 17, 1777, some 5,800 men by the standard count, and the Treaty of Alliance of February 6, 1778. The South answers: Charleston and Camden answered at King's Mountain and Cowpens, and Greene's campaign driving Cornwallis into Virginia. Yorktown and the peace: some seventeen thousand allied troops around eight thousand, the standard counts, the surrender of October 19, 1781, and the Treaty of Paris of September 3, 1783. Grade the table on dates, actors, and labeled figures, not on adjectives.")

# ------------------------------------------------------ 26 VOCAB A
vocab('Words for the armies and the winter',
      [('Continental Army', 'the army Congress created in June 1775'),
       ('militia', 'citizen soldiers, part time, near home'),
       ('George Washington', 'the commander chosen in 1775'),
       ('Valley Forge', 'the winter camp of 1777 and 1778')],
      "These definitions match the guided notes, and the notes carry them in full, word for word. Continental Army: the army created by the Second Continental Congress in June 1775, commanded by George Washington, drawn from all thirteen colonies and enlisted for terms beyond the militia's short service. militia: the local armed force of a colony or state, made of citizen soldiers who served part time near home and could be called out in emergencies. George Washington: the Virginia planter and former militia colonel chosen in 1775 to command the Continental Army, whose strategy of keeping the army in being carried the cause through eight years of war to Yorktown. Valley Forge: the Pennsylvania camp where the Continental Army wintered in 1777 and 1778, enduring hunger and disease while Baron von Steuben drilled it into a professional force.")

# ------------------------------------------------------ 27 VOCAB B
vocab('Words for the victories and the alliance',
      [('Battle of Saratoga', 'Burgoyne surrenders, fall of 1777'),
       ('Treaty of Alliance', 'France joins the war, February 1778'),
       ('Battle of Yorktown', 'Cornwallis trapped and surrendered, fall of 1781')],
      "Three more terms, in the guided notes wording, carried in these notes in full, word for word. Battle of Saratoga: the American victory in the fall of 1777 in which a British army under General Burgoyne surrendered in upper New York, the win that persuaded France to ally openly with the United States. Treaty of Alliance: the treaty of February 1778 by which France recognized American independence and joined the war against Britain, bringing French money, ships, and soldiers to the American cause. Battle of Yorktown: the last major battle of the war, in the fall of 1781, in which Washington's army and a French fleet trapped General Cornwallis at Yorktown, Virginia, and forced his surrender. Notice the order of the three: a proof, an alliance, and a trap the alliance made possible.")

# ------------------------------------------------------ 28 CLOSING SYNTHESIS
s = slide(NAVY)
kicker(s, 'Closing synthesis')
text(s, 0.9, 1.35, 11.5, 1.1, 'What the winning left behind', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 2.6,
     ["The war ended with a recognized country reaching the Mississippi, won by an army that had nearly dissolved three times and by allies its survival had earned.",
      "The next lesson opens inside that country, where the war was also fought at home, by the peoples who paid for it and read its promises against their own condition."],
     size=23, color=POWDER, leading=1.3)
notes(s, "Close the lesson by stating what the winning consisted of, in the record's own sequence, before pointing forward. A cause that began the war without arms, ammunition, clothing, ships, money, or skilled officers, in Congress's own list at Station 1, ended it with its independence acknowledged by the king who had claimed it, a boundary at the Mississippi and the Great Lakes, and its debts and its enemies' property claims written into a treaty the states would honor unevenly. The instruments were the ones this lesson ranked: an army kept in being past every reasonable expectation, a victory large enough to purchase an alliance, an alliance large enough to close a trap, and a southern campaign that walked the last British field army into it. Nothing in today's lesson settles what independence would mean at home. The peoples who fought, paid, and waited through the war, and what its promises came to in their hands, are the next lesson's subject, and students should arrive there with the war's chronology and its labeled figures firm.")

# ------------------------------------------------------ 29 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ["How did the United States survive a war against the world's strongest empire, and win it? Keep the survival and the winning joined, carry the figures with their labels, and answer the strongest claim that any one cause won the war alone."],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The War in Five Records: the address, the alliance, the diary, the report, the peace'),
        ('Notebook', 'Notebook page: the turning points, what happened, what each one changed'),
        ('Quick check', 'Congress to a Tired Country: the address of May 1778 read against the record'),
        ('Writing', 'What Won the War: your judgment defended against the strongest rival cause')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the two armies defined, Saratoga and the alliance in two sentences, and the lesson question in two or three.',
     size=15, color=POWDER)
notes(s, "Close the lesson by handing the ranking to the students, which is what this lesson exists to do. The activity, The War in Five Records, gives them Congress's address of May 1778 from the audited bank record, the Treaty of Alliance and the Treaty of Paris in the Avalon Project transcriptions, Waldo's diary in the Pennsylvania Magazine edition, and Morgan's Cowpens report in the Founders Online transcription, and asks them to rank the five contributions and answer the claim that any one of them won the war alone. The notebook page charts the turning points. The quick check reads the May 1778 address against the record on both sides of its date. The writing task asks what won the war, with the survival carried at full strength and every figure labeled as the lesson labels it. The exit ticket has three parts: the Continental Army and the militia defined and distinguished, Saratoga and the alliance stated in two sentences, and the lesson question answered with the survival and the winning kept together.")

dc.save(OUT)
