#!/usr/bin/env python3
"""Depression and New Deal Lesson 3 deck builder. Image led deck: inauguration, bank run, fireside chat, TVA signing, and Norris Dam photographs."""
import os, sys, re
HERE = os.path.dirname(os.path.abspath(__file__))
LESSON_DIR = os.path.dirname(HERE)
UNIT_DIR = os.path.dirname(LESSON_DIR)
sys.path.insert(0, UNIT_DIR)
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags, photo_right,
                         divider_photo, content_photo, content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED, W, H)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

dc.IMG = os.path.join(HERE, 'img')
OUT = os.path.join(LESSON_DIR, 'lesson-03-slides.pptx')

spec = open(os.path.join(UNIT_DIR, 'build-scripts', 'unit-spec.md')).read()
sec = spec.split('### Lesson 3')[1].split('### Lesson 4')[0]
TERMS = []
for line in sec.splitlines():
    line = line.strip()
    if line.startswith('- '):
        t, d = line[2:].split(': ', 1)
        TERMS.append((t.strip(), d.strip()))
assert len(TERMS) == 7, TERMS
TD = dict(TERMS)

def vocab(title, terms, note, kick='The vocabulary'):
    s = slide(CREAM)
    kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95, 11.5, 1.0, title, size=30, color=NAVY, font='Georgia')
    yy = 2.1
    for term, dfn in terms:
        text(s, 0.9, yy, 4.1, 0.9, term, size=24, color=NAVY, font='Georgia')
        text(s, 5.15, yy + 0.06, 7.3, 1.1, dfn, size=18, color=MUTED, leading=1.2)
        yy += 1.52
    notes(s, note)
    return s

SHORT = {
 'bank holiday': 'all banks closed by proclamation, March 6, 1933, for inspection before reopening',
 'Emergency Banking Act': 'law of March 9, 1933, giving the president broad banking power and licensing reopenings',
 'fireside chat': 'a Roosevelt radio address to the nation in plain conversational language',
 'Hundred Days': 'March 9 to June 16, 1933, the first great New Deal legislative season',
 'Glass-Steagall Act': '1933 law separating banking kinds and creating federal deposit insurance',
 'Agricultural Adjustment Act': '1933 law paying farmers to cut production toward parity prices',
 'Tennessee Valley Authority': '1933 federal corporation for dams, flood control, and power in one river valley',
}

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
text(s, 0.9, 5.32, 11.5, 0.4, 'THE DEPRESSION AND NEW DEAL · LESSON 3', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Roosevelt and the First Hundred Days', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Banks closed on Monday. A law by Thursday. A president on the radio by Sunday.', size=17, color=POWDER)
notes(s, "Open with the week itself, because the speed of this week is the lesson in miniature. Franklin D. Roosevelt took the oath of office on Saturday, March 4, 1933. On Monday he closed every bank in the United States. On Thursday Congress passed a banking law in a single day. On Sunday night he explained the whole rescue on the radio, in language any listener could follow, and on Monday the sound banks began to reopen and the money came back. The photographs in this deck are the public record of that week: the ride to the Capitol, the closed banks, the radio address, and the first dam camps. Tell students to keep the guided notes open, because the deck follows sections A through G in order, and every date on screen is a blank in their notes. The question underneath the whole lesson is what Americans learned to expect from Washington in a crisis.")
# 2 QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did Roosevelt\'s first hundred days change what Americans expected their government to do in a crisis?', {})]], size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': RUST_LT, 'italic': True}), ('How did the New Deal change the relationship between Americans and their federal government, and what did it leave undone?', {'italic': True})]], size=17, color=POWDER, font='Georgia', leading=1.2)
notes(s, "Read the lesson question aloud and keep it on the wall standard for the hour: an answer that lists laws without answering the expectation half earns partial credit. The unit question beneath it runs across all eight lessons of this unit, and this lesson supplies its first half, the changed relationship. In 1932 most Americans still expected the federal government to stand back during hard times, lend at the top, and wait. By June 1933 the same public had watched Washington close the banks, license the reopenings, pay farmers, dam a river, code industry, and insure deposits. Something in the citizen and state relationship moved in those hundred days, and it never moved all the way back. Hold two judgments through the hour, because the reading holds both. The speed and the confidence were real achievements. The programs were also experiments, passed in days, and nobody in 1933 knew whether they would work.")
# 3 MAP
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Eight days in March, then a season of laws', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'Inauguration Day', 'March 4, 1933, fear named as the enemy'),
        ('B', 'The Bank Holiday', 'March 6, every bank closed for inspection'),
        ('C', 'The Banking Act', 'March 9, sound banks licensed to reopen'),
        ('D', 'The First Fireside Chat', 'March 12, the rescue explained on radio'),
        ('E', 'Farming and the Valley', 'The AAA and the TVA, May 1933'),
        ('F', 'Industry and Banking Rules', 'Codes, separation, deposit insurance'),
        ('G', 'A New Expectation', 'The Hundred Days close, June 16, 1933')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This map follows the guided notes section by section, so students can find their place by letter all hour. Sections A through D cover eight days in March: the inauguration, the bank holiday, the banking law, and the radio chat that made the reopening work. Sections E and F widen the lens to the rest of the Hundred Days, farm payments and a river valley authority in May, then industry codes and rebuilt banking rules in June. Section G closes the season and states the lesson claim, that the lasting change was an expectation. Warn students about one trap in advance. The Hundred Days can sound like a parade of victories, and the reading refuses that reading. Each law passed in days with little debate. Congress was voting on experiments. The map is therefore also a list of open questions, and Lesson 4 will start grading the experiments by what they did in people\'s lives.")
# 4 DIVIDER A
divider_photo('ride-port.jpg', 'Section A', 'Inauguration Day, March 4, 1933', ['The banking system shut or failing, and a new president speaking to the whole country at once.'],
 "Set the scene before the famous sentence. Roosevelt took the oath on a cold Saturday with the financial system already closed by other hands. Governors had proclaimed state bank holidays to stop withdrawals, and in many cities no bank was open at all. About one worker in four had no job. The crowd in Washington heard the address in person, and millions more heard it by radio, which made this the first inauguration most Americans experienced as listeners in their own homes. Roosevelt knew his audience was frightened, and he designed the speech for that fear. He promised candor, he promised action, and he treated the fear itself as a force doing damage in the economy, draining banks and freezing decisions. Section A therefore covers one speech read as an instrument of government, the first tool the new administration used, before it had passed a single law or spent a single dollar.")
# 5 CONTENT A
content_photo_s('ride-port.jpg', 'Fear named as the enemy', ['Roosevelt was inaugurated on Saturday, March 4, 1933.', 'Banks stood shut or failing in state after state.', 'About one worker in four had no job.', 'The only thing we have to fear is fear itself.', 'He called that fear a nameless, unreasoning, unjustified terror.'],
 "Quote the sentence whole, because students know half of it and the second half carries the argument. In the Franklin D. Roosevelt Presidential Library transcript, Roosevelt said that the only thing we have to fear is fear itself, and he called that fear a nameless, unreasoning, unjustified terror which paralyzes needed efforts to convert retreat into advance. Paralyzes is the working word. Fear was not a mood in this analysis. Fear was the mechanism of the bank runs of February and March, the reason depositors drained sound banks alongside weak ones and the reason credit froze. A president who named the mechanism could promise to break it. Notice also what the address did not do. It announced no detailed program. It set the terms, action now, frankness about conditions, and a request for public support, and it left the country expecting the action to begin on Monday. It did, which is why the speech and the week belong in one lesson.")
# 6 STAT A
stat('1 in 4', 'workers had no job when Roosevelt took office', 'The banking system stood shut or failing in state after state on inauguration day, March 4, 1933',
 "Give this figure its full weight before moving to the rescue, because the rescue is only impressive against the depth of the collapse. About one worker in four had no job in March 1933, the worst unemployment of the whole Depression by contemporary estimates. The government did not yet count the unemployed the modern way, so the reading calls these figures what they are, estimates of a catastrophe nobody measured exactly. Around the jobless figure stood the closed banks, the exhausted charities of Lesson 2, and farm prices below the cost of production. Students should also place the date. This was not the start of the Depression. The collapse was three and a half years old on inauguration day, which is why patience with waiting had run out and why a hundred days of speed could change what the public expected. The next section opens on Monday morning, with the new president holding emergency power and a country holding its breath.")
# 7 DIVIDER B
divider_photo('bank-port.jpg', 'Section B', 'The Bank Holiday', ['On March 6 every bank in the country closed, so examiners could sort the sound from the failed.'],
 "Explain the gamble at the center of this section, because the holiday looks obvious only in hindsight. Closing every bank at once stopped the withdrawals that were killing sound banks, and state holidays already in force had shown that a closing could stop a local run. A national closing was a larger bet. If the public treated the holiday as proof that all banks were ruined, the reopening would fail and take the presidency down with it in its first week. Roosevelt acted under an old wartime trading law, stretched to a peacetime emergency, and he knew Congress had to confirm and widen his authority within days. The holiday therefore had a clock inside it. Doors were shut so that examiners could work fast, bank by bank, building the list of banks that could safely open again. Section B covers the closing itself. Section C covers the law that turned a proclamation into a rescue.")
# 8 CONTENT B
content_photo_s('bank-port.jpg', 'Closed so they could be sorted', ['On March 6, Roosevelt proclaimed the bank holiday.', 'Every bank in the country closed at once.', 'Withdrawals stopped for sound and weak banks alike.', 'Federal examiners inspected the banks one by one.', 'Congress was called into special session for March 9.'],
 "Walk the mechanics slowly, because the guided notes test them in order. A bank holiday, in the guided notes definition, is " + "bank holiday: " + TD['bank holiday'] + ". The proclamation of March 6 closed every bank, which ended the perverse contest in which the first depositors to reach a bank saved their money and the last lost theirs. With the doors shut, examiners could read each bank\'s loans and reserves without a line at the counter forcing a fire sale. Sorting was the whole design. A bank with sound loans and enough reserves would reopen. A bank hollowed out by bad loans would stay closed, and its depositors faced loss, a hard fact the administration did not hide. Tell students to hold that honesty in mind. The rescue that follows worked in part because the government inspected before it promised, instead of declaring every bank sound and being caught in the lie.")
# 9 DIVIDER C
divider_text('Section C', 'The Emergency Banking Act and the Reopening', 'A law in a single day, March 9, and then the doors opened in stages.',
 "Introduce this section as the legislative half of the rescue, and stress how unusual the day was. Congress met in special session on March 9, received the banking bill, debated it for hours rather than weeks, and passed it the same day, with many members voting on a bill they had heard read aloud rather than studied in print. In normal times that speed would be a scandal about process. In March 1933 the majority in both parties treated the speed as the point. Every day the banks stayed closed without a law behind the closing cost confidence the holiday could not spare. The act did three things students must separate: it confirmed what the president had already done, it widened his power over banking, and it created the licensing system for reopening. The reopening then proceeded in stages, the largest city banks first, so that success in the biggest markets could teach depositors elsewhere what to do when their own bank opened.")
# 10 CONTENT C
content_text('Licensed to reopen', ['Congress passed the act on March 9, in one day.', 'Broad presidential power over banking was confirmed.', 'Sound banks reopened under federal license.', 'Unsound banks stayed closed.', 'At the first reopenings, deposits exceeded withdrawals.'],
 "State the definition exactly as the guided notes carry it. The Emergency Banking Act is this: " + "Emergency Banking Act: " + TD['Emergency Banking Act'] + ". The licensing clause is the heart of the law. A license told a town that federal examiners had read its bank\'s books and judged it sound, which converted a rumor driven system into an inspected one. The staged reopening did the persuading that no speech could do alone. When the great city banks opened and the lines formed to deposit rather than withdraw, newspapers carried the fact nationwide within the day. Students should note the limits inside the success. Banks that stayed closed held the savings of thousands of families, and those losses were real and uncompensated in March 1933. Deposit insurance, which would change that fact for the future, does not arrive until June, in section F. The March rescue saved the system. It did not make every depositor whole.")
# 11 STAT C
stat('1 day', 'from bill to law for the Emergency Banking Act, March 9, 1933', 'Debate measured in hours · The special session then ran on to June 16',
 "Use this small number to teach a large point about the season. One day is not how Congress usually writes banking law, and the departures from normal process in the Hundred Days should be named as departures, not hidden as efficiency. Committees were skipped or compressed, texts were short, and amendments were few. The defense offered at the time was emergency: the banks were closed, the holiday clock was running, and a slow law was a failed rescue. The cost of the speed appears later in the unit, when the Supreme Court reads these fast statutes closely in 1935 and 1936 and strikes two of them down. For today, students should record both halves without choosing yet. A government that could move this fast had shown a capacity nobody had seen in peacetime. A legislature that moved this fast was also bound to write laws whose edges nobody had tested. Both halves are true, and the unit test rewards answers that keep them together.")
# 12 DIVIDER D
divider_photo('fireside-port.jpg', 'Section D', 'The First Fireside Chat', ['Sunday night, March 12: the president explains banking to the nation, in plain language, on the radio.'],
 "Frame the chat as the third leg of the rescue, as necessary as the holiday and the law. The holiday stopped the runs and the act licensed the reopenings, but neither could put money back into the banks. Only depositors could do that, one household at a time, and households act on what they understand and trust. Roosevelt understood that the explanation itself was a policy tool. On Sunday evening, March 12, with the first licensed banks set to open the next morning, he sat down at a desk in the White House and spoke to tens of millions of listeners as if he were explaining the week to neighbors. The performance was deliberate and prepared, down to the plain vocabulary. Banking words were translated as he went. Nothing was hidden, including the fact that banks lend deposits out rather than vaulting them. Section D covers what he explained, what he asked, and what happened the next morning.")
# 13 CONTENT D
content_photo_s('fireside-port.jpg', 'Banking explained in plain language', ['On March 12, Roosevelt gave the first fireside chat on radio.', 'A bank does not keep deposits in a vault.', 'Deposits are put to work in loans.', 'Only a small share of deposits is held as cash.', 'Listeners were asked to keep money in reopened banks.'],
 "Give the definition in the guided notes wording first. A fireside chat is this: " + "fireside chat: " + TD['fireside chat'] + ". Then work the content of this first chat, because its teaching was the policy. Roosevelt began, in the FDR Library transcript, by saying he wanted to talk for a few minutes with the people of the United States about banking. He then explained that a bank does not put deposits into a safe deposit vault but invests them in bonds, commercial paper, mortgages, and other loans, keeping only a small part in currency. That single fact explained the whole crisis. If deposits are mostly loans, then no bank on earth can pay every depositor in cash on the same morning, and a run can kill a sound bank. Listeners who understood that sentence understood why the holiday and the inspections had been necessary, and why bringing money back was safe in a licensed bank.")
# 14 CONTENT D2
content_text('Together we cannot fail', ['He described what the government had done.', 'He explained what would happen next, step by step.', 'He closed by asking for public support.', 'The next day, deposits kept growing.', 'Explanation itself worked as policy.'],
 "Close the section with the result, and teach students to weigh it as evidence rather than as legend. Roosevelt ended the chat by saying that the machinery to restore the financial system had been provided and that it was up to the people to support and make it work, closing with the pledge that together the country could not fail. The words are quoted here in shortened form from the FDR Library transcript, and the reading prints the source line so students can check them. On Monday the licensed banks opened, and deposits exceeded withdrawals in city after city, just as they had begun to do at the first openings. Historians still credit the sequence rather than any single step: inspection first, license second, explanation third, reopening last. Reverse the order and the rescue likely fails, because a promise made before the inspections, or an opening made before the explanation, asks depositors to trust what they have no reason to trust. That sequence is the section in one sentence, and it is worth writing on the board.")
# 15 DIVIDER E
divider_photo('signing-port.jpg', 'Section E', 'Farming and the Valley', ['May 1933: the season moves beyond banking, to farm prices and a whole river region.'],
 "Mark the widening of the lesson here, because students often remember the Hundred Days as a banking story with laws attached. By May the administration was legislating for the two great rural crises of the Depression: farm prices so low that growing food lost money, and a river valley so poor that most of its farm homes had no electric light. The two May laws also show two different New Deal methods side by side. The farm law worked through payments and production agreements with individual farmers, inside the existing economy. The valley law created a new federal corporation and handed it a whole region to develop, dams, power lines, fertilizer, and flood control together. Ask students to watch for that contrast in method as the section proceeds. Later lessons return to both laws: the farm law is the one the Supreme Court strikes down in the Butler case, and the valley authority is the one critics point to when they argue about how far the new federal power should reach.")
# 16 CONTENT E
content_photo_s('norris-port.jpg', 'Paying farmers, damming a river', ['The AAA paid farmers to cut production toward parity.', 'In its first season, cotton was plowed under and pig herds were reduced.', 'The TVA took up a whole river region.', 'The TVA built dams for flood control and electricity.', 'Private power had left most farm homes without current.'],
 "Carry both definitions exactly. The Agricultural Adjustment Act is this: " + "Agricultural Adjustment Act: " + TD['Agricultural Adjustment Act'] + ". The Tennessee Valley Authority is this: " + "Tennessee Valley Authority: " + TD['Tennessee Valley Authority'] + ". Then slow down on the farm law\'s painful first season, because students will raise it themselves. Paying farmers to plow under growing cotton and reduce pig herds, in a country where city families stood in breadlines, looked obscene to many contemporaries and still does. The administration\'s answer was arithmetic: unsold surpluses had driven prices below the cost of growing the crop, and only a smaller crop could raise the price the remaining crop would fetch. The valley law needs less defense and more scale. One federal corporation, a river hundreds of miles long, seven states, and a building program that would run for decades all begin in a single May statute.")
# 17 DIVIDER F
divider_text('Section F', 'Industry and Banking Rules', 'June 1933: codes for industry, and a rebuilt banking system so March cannot repeat.',
 "Introduce the final legislative week of the season, in which Congress passed the two laws that tried to govern the future rather than rescue the present. The industrial recovery law reached into every factory and shop in the country with codes of fair competition, an experiment in national economic planning with no peacetime precedent. The banking law did the opposite kind of work. Instead of planning an industry, it rebuilt the rules of one: commercial banks and investment banks were separated, so that deposit money could no longer be risked in the stock market operations that had ruined banks before 1933, and deposits were insured by the federal government. Congress in the same days also set the end of Prohibition in motion, proposing the repeal amendment the states ratified before the year ended, which closed the great social experiment of the previous unit. Section F therefore ends the season at its widest reach, from the price of shoes to the safety of savings.")
# 18 CONTENT F
content_text('Codes above, insurance below', ['The Recovery Act set up codes of fair competition.', 'The codes set wages, hours, and prices by industry.', 'The law protected workers\' right to organize.', 'Glass-Steagall separated commercial and investment banking.', 'The act created federal insurance of bank deposits.'],
 "Carry the remaining definition exactly. The Glass-Steagall Act is this: " + "Glass-Steagall Act: " + TD['Glass-Steagall Act'] + ". Then separate the two June laws by the kind of power each one uses. The codes law, run by the National Recovery Administration of Lesson 4, governs by agreement enforced by government: industries write their rules, Washington approves them, and the Blue Eagle marks the firms that comply. The banking law governs by structure: it forbids one kind of institution from doing another kind\'s business, and it insures deposits so that fear loses its grip on the depositor. Of everything passed in the Hundred Days, deposit insurance may prove the most durable, because it attacks the bank run at its root. A depositor who knows the government will repay her if the bank fails has no reason to stand in line at dawn. Students should test that claim against the March story, where no such promise yet existed.")
# 19 DIVIDER G
divider_text('Section G', 'A New Expectation', 'The special session closes June 16. What changed for good was what Americans expected.',
 "Bring the lesson home to its question. The special session that opened on March 9 closed on June 16, 1933, and the season it made has a name students already carry in their vocabulary: the Hundred Days. Section G asks for the double judgment the reading ends on, and the exit ticket will grade it. On one side stand the facts of speed and restored confidence: banks reopened, deposits returned, and a legislature passed program after program while the country watched. On the other side stand the facts of haste: bills passed in days, agencies invented on the floor, and results that nobody, including the president, could predict. Both sides belong in any honest answer. What no historian disputes is the expectation shift underneath them. A public that in 1932 expected Washington to wait out a collapse had by the summer of 1933 learned to watch Washington first, and to judge a president by how fast and how far he acted.")
# 20 CONTENT G
content_text('Experiments at speed', ['The session ran from March 9 to June 16, 1933.', 'Congress passed bill after bill, with little debate.', 'Speed and confidence were real achievements.', 'Most programs were experiments, and their results were unknown.', 'Americans now expected Washington to act first.'],
 "State the last definition exactly. The Hundred Days are this: " + "Hundred Days: " + TD['Hundred Days'] + ". Then run the closing comparison the writing task will require. Against Hoover\'s record from Lesson 2, where the federal answer to collapse was loans at the top and appeals for voluntary cooperation, set this record: a closed banking system reopened by license, farm prices addressed by federal payment, a river valley taken up whole, industry coded, deposits insured, and relief money moving through the states, all inside one spring. The contrast is the changed expectation in concrete form. End by refusing the easy verdict in both directions. The Hundred Days did not end the Depression, as Lesson 4\'s unemployment figures will show next time. They also cannot be called a failure by a class that has just watched the banking system come back to life in a week. The season changed what government was for, in the public mind, and that change outlasted every single program it produced.")
# 21 STAT G
stat('100 days', 'March 9 to June 16, 1933: the first great season of New Deal lawmaking', 'Banking, farms, a river valley, industry codes, deposit insurance, and the end of Prohibition set in motion',
 "Let the number sit on screen while students copy the span into their notes: March 9 to June 16, 1933, one hundred days by the count the country settled on. The exact day count is less important than what the span contains, and students should be able to recite the contents in order by now: the banking rescue in the first week, then relief, farm payments, and the valley authority, then the industry codes and the rebuilt banking rules at the close. One caution belongs with the celebration of the number. The Hundred Days became a measuring stick that later presidents are still judged against, and the stick itself can mislead. Speed was possible in 1933 because Congress was frightened, the president\'s party held both houses, and the bills were short. A hundred days of lawmaking in a calmer season would look different, and later lessons show this same Congress slowing down, arguing, and finally pushing back. For today the number stands as the season\'s name and its fair summary.")
# 22 GLANCE
s = slide(NAVY)
kicker(s, 'The Hundred Days at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Rescue first, then a new reach', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Banking rescue', 'Holiday, banking act, fireside chat', 'Deposits returned; licensed banks trusted'),
        ('Farms and valley', 'AAA payments; TVA dams and power', 'Farm prices addressed; a region electrified'),
        ('Industry and rules', 'Codes; Glass-Steagall; deposit insurance', 'Wages and hours set; savings protected'),
        ('The expectation', 'Action in days, across the whole economy', 'Washington watched first in every crisis after')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the closing table of the guided notes, and students should complete that table now, from memory where they can. The three action rows recapitulate the season in the order Congress lived it: the banking rescue of the first week, the farm and valley programs of May, and the industry codes and banking rules of June. The fourth row is the lesson itself, the expectation those actions created. Check the table with two questions that expose shallow answers fast. First, which row would disappear if the fireside chat had failed? The rescue row, because licenses without returning deposits are paper. Second, which rows were experiments whose results 1933 could not know? The farm, valley, and industry rows, and students should be able to say why in each case: untested payments, an unbuilt dam system, and codes never tried in peacetime. Grade the table generously on wording and strictly on that logic, because the writing task grades the same logic in prose.")
# 23 VOCAB A
vocab('Words for the rescue', [(t, SHORT[t]) for t in ['bank holiday', 'Emergency Banking Act', 'fireside chat', 'Hundred Days']],
 "Four terms, matching the guided notes word for word, and students should copy the full definitions exactly because the unit test draws on them. Bank holiday: " + TD['bank holiday'] + ". Emergency Banking Act: " + TD['Emergency Banking Act'] + ". Fireside chat: " + TD['fireside chat'] + ". Hundred Days: " + TD['Hundred Days'] + ". Press the two distinctions students blur most. The holiday was the closing itself, proclaimed March 6. The act was the law of March 9 that confirmed the closing and licensed the reopening. The chat is a form, not a nickname for any speech, and this lesson studies the first one, on banking, delivered March 12.")
# 24 VOCAB B
vocab('Words for the season', [(t, SHORT[t]) for t in ['Glass-Steagall Act', 'Agricultural Adjustment Act', 'Tennessee Valley Authority']],
 "Three more terms, again matching the guided notes exactly. Glass-Steagall Act: " + TD['Glass-Steagall Act'] + ". Agricultural Adjustment Act: " + TD['Agricultural Adjustment Act'] + ". Tennessee Valley Authority: " + TD['Tennessee Valley Authority'] + ". Two wording points deserve emphasis before the exit ticket. The farm definition ends with the goal, parity, the price level at which farm income would buy what it bought before the First World War, and students who write only that the law paid farmers have the mechanism without the purpose. The valley definition calls the authority a federal corporation, a government owned company built to run a development program like a business, and that corporate form is why the TVA could build, sell power, and hire outside the normal department structure. Both points return on the unit test, in the blueprint entries for the Hundred Days.")
# 25 SYNTHESIS
content_text('Answering the question', ['Before 1933, Washington waited, lent at the top, and appealed for calm.', 'In March 1933, Washington closed, inspected, licensed, and explained.', 'By June, farms, a valley, industry, and deposits were all federal business.', 'The expectation changed, and it did not change back.'],
 "Run the synthesis as a direct comparison with Lesson 2, because the unit is built on the contrast. Hoover facing the same collapse offered voluntarism, loans to banks and railroads through the Reconstruction Finance Corporation, and a warning that direct federal relief would weaken character. Roosevelt facing the deepened collapse closed every bank in the country in his first forty eight hours, took a banking law through Congress in a day, explained himself on the radio within the week, and spent the spring signing laws that reached farms, rivers, factories, and savings accounts. The policy difference is large. The expectation difference is larger, and it is the one the lesson question names. After the Hundred Days, an American in trouble, a farmer, a depositor, a worker, looked to Washington as a matter of course, and a president who failed to act would be judged for the failure. That habit of looking is the New Deal\'s first legacy, and the next lesson tests it against what the new agencies actually delivered at the kitchen table.")
# 26 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4, ['How did Roosevelt\'s first hundred days change what Americans expected their government to do in a crisis?'], size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'Hundred Days Drafting Desk: five crisis files, your bill against the law passed'),
        ('Notebook', 'Notebook page: the Hundred Days chart in your own words'),
        ('Quick check', 'The Banking Rescue: the address, the sequence, and deposit insurance'),
        ('Writing', 'A New Expectation: the lesson question as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: why the holiday came first, two Hundred Days laws, and the lesson question in two or three sentences.', size=15, color=POWDER)
notes(s, "Close by handing the lesson to the work. In the activity, the Hundred Days Drafting Desk, each group receives one crisis file, banking, farm prices, a river valley, industrial collapse, or unemployment, drafts the operative clauses of a one page bill, and then compares the draft with the law Congress actually passed, marking what Congress added, cut, or left out. The notebook page rebuilds the season as a chart of actions and changes. The quick check, The Banking Rescue, tests the inaugural passage, the March sequence, and deposit insurance against blueprint entries five and six. The writing task, A New Expectation, requires the double judgment this lesson has carried throughout: speed and confidence as real achievements, and the programs as experiments whose results nobody could yet know. The exit ticket has three parts: why the holiday had to come before the reopening, two Hundred Days laws with what each did, and the lesson question answered in two or three sentences with two facts. Next lesson follows the money home, into relief offices, camps, and construction sites.")

dc.save(OUT)
