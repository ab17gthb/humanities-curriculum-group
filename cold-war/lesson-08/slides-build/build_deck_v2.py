#!/usr/bin/env python3
"""Cold War Lesson 8 deck, "The Wall Falls: The Cold War Ends," built to
the approved system: image-led slides, fragments only on screen,
comprehensive speaker notes, full lesson and vocabulary coverage.
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
    frags(s, items, y=2.15 if kick else 2.0, w=6.9, size=size)
    notes(s, note)
    return s

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'THE COLD WAR · LESSON 8', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Wall Falls: The Cold War Ends', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Reform, crowds, and collapse: how the rivalry ended, 1985 to 1991', size=17, color=POWDER)
notes(s, "The photograph shows crowds thronging around the Brandenburg Gate in Berlin on December 1, 1989, three weeks after the Berlin Wall was breached, photographed by Staff Sergeant F. Lee Corkran of the United States Air Force for the Department of Defense. It is the right opening image for the unit's final lesson because this lesson ends in crowds rather than in battle. Between 1985 and 1991 the Soviet Union was reformed by its own leader, challenged in public by an American president, and then left, piece by piece, by the peoples it ruled, until the state itself was declared dissolved in December 1991. Teach the lesson as a sequence of choices, because the activity and the writing task both ask students to weigh those choices against each other.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("Why did the Cold War end between 1989 and 1991, and what did its ending settle and leave unsettled?", {})]],
     size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the struggle between the United States and the Soviet Union reshape the world and American life, and why did it end the way it did?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question has two halves, and the exit ticket requires both. The first half asks why the Cold War ended when it did, between 1989 and 1991 rather than a decade earlier or later, which is a question about causes that students will have to weigh: a reforming leader, pressing crowds, American pressure, and a failing system. The second half asks what the ending settled and what it left open, which is a question about consequences: Germany reunified, an alliance dissolved, a superpower gone, and a map of new states holding old weapons. Warn students now that the lesson presents the causes as an argument to be weighed from documents, not as a verdict to be copied down. The writing task grades the weighing.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Reformed, breached, settled, dissolved', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The reformer takes power', 'Gorbachev, March 1985; a stagnated Soviet Union'),
        ('B', 'Glasnost and perestroika', 'Openness and restructuring loosen the party grip'),
        ('C', 'A second chance at diplomacy', 'Reykjavik, the Gate speech, the INF Treaty'),
        ('D', 'The year it broke: 1989', 'Poland votes; Hungary opens; Leipzig marches'),
        ('E', 'November 9: the wall opens', 'A garbled announcement, a crowd, guards aside'),
        ('F', 'The settlement of 1990', 'Reunification inside NATO, October 3, 1990'),
        ('G', 'The center gives way: 1991', 'The failed coup; dissolution, December 25, 1991')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "The map follows the guided notes section by section. Sections A and B cover the reformer: Gorbachev taking power in 1985 over a stagnated country, and the two policies, glasnost and perestroika, that loosened the control they were built to restore. Section C follows the diplomacy of those years, a near miss at Reykjavik, a public challenge at the Brandenburg Gate, and the first treaty to destroy a class of weapons. Sections D and E run the year 1989, from Poland's election to the night of November 9, when a garbled announcement and a crowd opened the wall. Section F settles Germany in 1990. Section G moves to Moscow in 1991, a failed coup in August and a dissolution in December. The order is the argument: reform first, then pressure, then crowds, then signatures.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', 'The Reformer Takes Power',
             'March 1985: a new Soviet leader inherits a country that has stopped working, and decides it must change to survive.',
             "Begin with what Gorbachev did not intend, because the whole lesson turns on the gap between his intention and his result. He was a product of the system he reformed, a Communist Party official who had risen through its ranks for thirty years, and he took power in March 1985 to save Soviet socialism, not to bury it. The condition he inherited made reform unavoidable in his eyes: more than a decade of stagnation under aging leaders, factories turning out goods nobody wanted, shops standing half empty, harvests falling short of feeding the country, and a war in Afghanistan consuming men and money with no victory in sight. At the same time the state still commanded an arsenal equal to America's and armies across Eastern Europe. A failing economy inside a military superpower is the combination students should hold in mind through every later section.")

# ------------------------------------------------------ 5 INHERITANCE
content_text('The inheritance of 1985',
             ['The Soviet Union had endured more than a decade of stagnation.',
              'Factories produced goods few people wanted.',
              'Shops stood half empty and harvests fell short.',
              'The war in Afghanistan was costly and unwon.',
              'The Soviet arsenal matched America weapon for weapon.',
              'Gorbachev concluded the system had to change.'],
             "Give the stagnation its texture before naming the reformer, because students who picture a thriving Soviet Union in 1985 cannot understand why anyone inside the Kremlin wanted change. Growth had slowed through the 1970s and stalled in the early 1980s. Consumer goods were shoddy and scarce, alcoholism and declining health cut into the workforce, and the country that had launched the first satellite was falling behind in computers and technology. The war in Afghanistan, begun in 1979 to hold a friendly government in Kabul, had settled into occupation and ambush. Three general secretaries had died in office between 1982 and 1985, so the system's immobility had a human face: old men repeating formulas. Gorbachev, at fifty four the youngest leader in a generation, concluded the country had to change in order to survive. His two instruments come next, and both deserve exact definitions, since the guided notes carry them as vocabulary.",
             kick='A · The reformer takes power', size=24)

# ------------------------------------------------- 6 SECTION B DIVIDER
divider_text('Section B', 'Glasnost and Perestroika',
             'Openness and restructuring: two policies built to save the party, which loosened its grip on everything it touched.',
             "Teach the two policies as a pair with a feedback loop between them, because taught separately they sound like a civics lesson and taught together they explain 1989. Glasnost, openness, came first in practice: censorship loosened, political prisoners were released, newspapers began printing what officials had hidden, and the crimes of the Stalin years could be argued about in public. Perestroika, restructuring, tried to make the economy respond by loosening central commands and letting managers and republics act on their own initiative. Each policy fed the other. Open discussion exposed how badly the economy was failing, which weakened the party's claim that only it could rule. Restructuring loosened the party's grip on the institutions it had commanded for seventy years. The result neither man nor policy had planned: citizens learned that criticism was survivable, and the peoples of the empire learned that obedience had become a choice.")

# ------------------------------------------------------ 7 TWO INSTRUMENTS
content_text('Two instruments, one result',
             ['Glasnost loosened censorship and freed political prisoners.',
              'The Soviet past itself was argued about in public.',
              'Perestroika loosened central control.',
              'Openness exposed the failure glasnost described.',
              'Restructuring loosened the party grip.',
              'Obedience became a choice.'],
             "Work the loop slowly, with one concrete example of each policy. For glasnost, use the press after the Chernobyl disaster of April 1986, when initial official silence gave way under the new policy to public argument about what the state had hidden, a pattern repeated across Soviet life from factory failures to the Afghan war's cost. For perestroika, use the factory manager or the republic government told to decide locally what Moscow had always decided, and then blamed when supplies failed to arrive. The vocabulary definitions on the later slides carry the formal wording, and students should be able to reproduce both: glasnost as openness allowing public discussion, criticism of officials, and a freer press; perestroika as restructuring meant to make a failing system work, ending by loosening the party's control of both economy and state. The unintended result is the section's finding, and it sets up everything that happened outside the Soviet Union's borders.",
             kick='B · Glasnost and perestroika', size=24)

# ------------------------------------------------- 8 SECTION C DIVIDER
divider_photo('reagan-port.jpg', 'Section C', 'A Second Chance at Diplomacy',
              ['June 12, 1987: Reagan at the Brandenburg Gate,', 'challenging Gorbachev to tear down the wall.'],
              "The photograph shows President Reagan giving his speech at the Berlin Wall, Brandenburg Gate, in West Berlin on June 12, 1987, from the National Archives record. Set the diplomatic sequence before reading the famous sentence. In October 1986, at Reykjavik in Iceland, Reagan and Gorbachev had come within reach of abolishing nuclear weapons entirely before their talks broke down over Reagan's missile defense program. Eight months later Reagan stood within sight of the wall and addressed Gorbachev by name and title, setting a public test for the reforms Moscow was advertising: if the change was real, here was one unmistakable sign. The sentence students know is in the activity as Station 1, quoted from the audited text. Resist letting the sentence swallow the sequence. The near miss came first, the challenge second, and the treaty, which comes on the next slides, third.",
              title_size=34)

# ------------------------------------------------------ 9 REYKJAVIK TO WASHINGTON
content_text('Reykjavik, the Gate, Washington',
             ['Reykjavik in October 1986 was a near miss on abolition.',
              'The talks broke down over missile defense.',
              'Reagan issued the Brandenburg Gate challenge in June 1987.',
              'The INF Treaty was signed in December 1987.',
              'The treaty was the first agreement to destroy a class of weapons.'],
             "State the sequence plainly, because its order corrects two easy errors. The first error is that pressure alone produced the treaty: in fact the deepest offer, the near abolition discussed at Reykjavik, came from negotiation and failed on the missile defense question, and the treaty that followed covered a narrower class of weapons both sides could verify. The second error is that the Berlin speech ended something: the wall stood for two more years after it, and its immediate diplomatic product was not the wall's fall but a signing ceremony in Washington. The INF Treaty of December 8, 1987 required each side to eliminate its intermediate-range and shorter-range missiles entirely, under inspection, rather than to cap them at an agreed number. That distinction, elimination rather than limitation, is the slide's teaching point, and the guided notes definition carries it in the range figures students will meet again on the vocabulary slides.",
             kick='C · A second chance at diplomacy', size=24)

# ------------------------------------------------------ 10 STAT MISSILES
stat('2,692', 'missiles destroyed under the INF Treaty by June 1991',
     '846 American and 1,846 Soviet · A class eliminated, not limited',
     "Teach this figure as the treaty's character in numbers. Earlier agreements in this unit, SALT above all, had limited how many launchers each side could hold, leaving the weapons in place under a ceiling. The INF Treaty required destruction, verified by inspectors watching missiles cut up and burned at named sites, and by June 1991 the count stood complete at 2,692 missiles in all: 846 American, including the Pershing II and the ground launched cruise missiles deployed in Europe in 1983, and 1,846 Soviet, including the SS-20 force whose deployment had started the crisis of the early 1980s. The imbalance in the count is itself instructive. The Soviet Union destroyed more than twice as many missiles, because it had deployed more of them, and Gorbachev accepted the arithmetic because the treaty's value to him lay at home: resources and attention freed for reform. A treaty both sides kept, counted to the last missile, is part of why 1989 could unfold without the superpowers reaching for their arsenals.",
     kick='C · A second chance at diplomacy')

# ------------------------------------------------- 11 SECTION D DIVIDER
divider_photo('gate-port.jpg', 'Section D', 'The Year It Broke: 1989',
              ['Poland votes, Hungary opens its border,', 'and Leipzig marches, while Moscow refuses to shoot.'],
              "The photograph is the December 1, 1989 crowd at the Brandenburg Gate, used here to open the 1989 section because the year's story ends at this gate. Work backward from it. Through 1989 the peoples of Eastern Europe tested, one country at a time, whether the Soviet guarantee behind their governments still held. In Poland the test was an election the Communists had agreed to hold. In Hungary it was a border fence cut open. In East Germany it was a weekly demonstration that grew for two months in plain sight. Each test returned the same answer: the local government stood alone, because Gorbachev had decided that holding the empire by force would destroy the reforms the empire was supposed to pay for. Earlier Soviet leaders had answered such tests with tanks, in Budapest in 1956 and in Prague in 1968. The difference in 1989 was not the crowds. Crowds had come before. The difference was the refusal in Moscow.",
              title_size=34)

# ------------------------------------------------------ 12 POLAND HUNGARY LEIPZIG
content_text('Three tests in one year',
             ['Poland voted Solidarity into government.',
              'Hungary opened its border with Austria.',
              'East Germans left through Hungary by the thousands.',
              "Leipzig's Monday crowds grew all autumn.",
              'Gorbachev refused to use the Soviet army at each step.'],
             "Take the three tests in the order their results arrived, and name what each one proved. Poland proved an election could remove a Communist government without Soviet punishment: Solidarity, the shipyard union founded in 1980 and driven underground under martial law, won the June 1989 vote so completely that by September it led the government, and Moscow accepted the result. Hungary proved a border could open: when Budapest cut its fence with Austria, East Germans on holiday drove through the gap by the thousands, and the East German state began losing its citizens faster than it could replace their obedience. Leipzig proved a crowd could grow under a police state: Monday demonstrations that began in the hundreds in September stood in the hundreds of thousands by late October, chanting for free travel and free elections, and the local authorities, denied Soviet backing, let them march. By November the pressure stood concentrated in Berlin itself.",
             kick='D · The year it broke: 1989', size=24)

# ------------------------------------------------- 13 SECTION E DIVIDER
divider_text('Section E', 'November 9: The Night the Wall Opened',
             'A concession, a garbled answer, a crowd at the crossings, and guards with no orders who stood aside.',
             "Slow down for this section, because it is the lesson's set piece and the quick check and writing task both test its sequence. No cabinet voted to open the Berlin Wall on November 9, 1989, and no army forced it open. The East German government, trying to relieve the pressure of the autumn demonstrations and the departures through Hungary, prepared looser travel rules as a controlled concession. What happened instead was produced by a chain of four links, each ordinary on its own: a spokesman sent to announce the rules without a full briefing, a question about timing answered wrong on live television, a crowd that treated the broadcast words as a fact and walked to the crossings, and border guards whose orders covered none of it. Teach the chain as a chain. Remove any link, the television answer, the crowd's decision, the guards' restraint, the Soviet silence behind them all, and the night ends differently.")

# ------------------------------------------------------ 14 THE NIGHT IN SEQUENCE
content_text('The night in sequence',
             ['The government planned a limited concession.',
              'The spokesman said the rules applied immediately.',
              'Television carried the words across both Berlins.',
              'Thousands walked to the crossings and demanded passage.',
              'Late that night, the guards stood aside.'],
             "Reconstruct the evening hour by hour as the record supports it, and mark the limits of the record as you go. The press conference ran in the early evening; the spokesman's answer on timing was an improvisation, and historians still argue over how much he understood of the rules he announced, so teach his state of briefing as imperfect rather than inventing his thoughts. What is documented is the effect: East Berliners who had watched the broadcast in their own living rooms went out to test it, first in hundreds and then in thousands, at crossing points across the city. At the Bornholmer Strasse crossing the crowd grew past the guards' ability to process or disperse it, and the officer in charge, facing a crowd his orders did not describe, opened the barrier late that night rather than fire on it. Other crossings followed. By morning, Berliners were standing on the wall at the Brandenburg Gate, and hammers were at work on its concrete.",
             kick='E · November 9', size=24)

# ------------------------------------------------------ 15 NO SHOT FIRED
content_photo_s('gate-port.jpg', 'No shot was fired',
             ['Crowds climbed the wall at the Brandenburg Gate.',
              'Hammers were at work on the concrete by morning.',
              'Soviet forces in East Germany stayed in barracks.',
              'The symbol of divided Europe was breached by a crowd.',
              'The December photograph shows the gate standing open.'],
             "Hold the negative fact up for inspection, because it is the most important fact of the night. The East German state possessed the police, the border troops, and the Soviet garrison that had enforced the division since 1961, and none of it fired. The guards at the crossings stood aside, the Soviet forces stayed in their barracks under the standing refusal from Moscow, and the crowd, which had come expecting to test a travel rule, found itself dismantling the central symbol of the Cold War order with hammers while photographers recorded it. Then direct students to the December 1 photograph in the activity and the quick check: crowds at the gate in daylight, a month later, with the gate accessible from the East and its formal opening to the West still three weeks away. The photograph's date is its lesson. November 9 was not reversed, and everyone in the picture knows it.",
             kick='E · November 9', size=19)

# ------------------------------------------------- 16 SECTION F DIVIDER
divider_text('Section F', 'The Settlement of 1990',
             'A unified Germany inside NATO, settled by negotiation while consent could still be won.',
             "Open the settlement section with its speed, because speed was its strategy. Once the wall opened, Chancellor Helmut Kohl of West Germany moved to reunify the two German states quickly, while Gorbachev's consent could still be obtained and before events in Moscow could close the window. The negotiation joined the two German governments with the four powers that had held occupation rights since 1945, the United States, the Soviet Union, Britain, and France, and it settled the external questions a unified Germany raised: its borders, its alliances, and the withdrawal of Soviet troops. The internal question was settled by East Germans themselves, at the ballot box in March 1990, in the first free election in that state's history, which returned a government committed to fast unification. On October 3, 1990 the two states joined as one. Germany had been divided by the war's outcome in 1945; it was reunified by signatures and an election forty five years later.")

# ------------------------------------------------------ 17 REUNIFICATION
content_text('Reunification inside NATO',
             ['East Germany voted freely for unity in March 1990.',
              'The two states and four powers settled the terms.',
              'One German state joined NATO on October 3, 1990.',
              'The Warsaw Pact dissolved in 1991.',
              'The Baltic states recovered their independence.'],
             "Work the settlement's two surprises, because students tend to absorb reunification as inevitable and it was not. The first surprise is the alliance: the unified Germany joined NATO, the Western alliance built against the Soviet Union, with the Soviet leader's consent, obtained through negotiation and Western assurances and aid rather than through any Soviet collapse that autumn. Moscow in 1990 still held armies in Germany and could have stalled; consent was a choice, and teachers should present it as one. The second surprise is the quiet around it: the Warsaw Pact, the Soviet alliance of 1955, dissolved itself in 1991 without a shot, and Estonia, Latvia, and Lithuania, annexed in 1940, recovered independence the same year. The postwar map of Europe, drawn by the armies of 1945 and frozen for two generations, was redrawn in about eighteen months by elections, negotiations, and withdrawals. What remained unsettled stood further east, inside the Soviet Union itself, which is the final section.",
             kick='F · The settlement of 1990', size=24)

# ------------------------------------------------------ 18 STAT 28 YEARS
stat('28 years', 'the Berlin Wall stood, from August 1961 to November 1989',
     'Built to stop a population leaving · Breached by the population it confined',
     "Give the wall its full biography in this one figure, because students meet it in this unit first as a symbol and should leave knowing it as a structure with dates. The East German government built the wall in August 1961 to stop its own citizens fleeing to the West, after millions had already left, and for twenty eight years it ringed West Berlin with concrete, guard towers, and a death strip patrolled under orders to shoot. People died at it across all twenty eight years, shot crossing, drowned in its canals, or killed in its tunnels, and the last deaths at the wall came in 1989 itself, months before the breach. Then the arithmetic reverses. The wall was breached in November 1989 by the population it had been built to confine, acting on a televised error, and the state that built it ceased to exist eleven months later, absorbed into the Federal Republic on October 3, 1990. Twenty eight years standing, eleven months from breach to the builder's disappearance: the two numbers together are the pace of the ending.",
     kick='F · The settlement of 1990')

# ------------------------------------------------- 19 SECTION G DIVIDER
divider_text('Section G', 'The Center Gives Way: 1991',
             'A coup that failed in three days, and a union dissolved by its own republics that December.',
             "Carry the lesson's method into the last section: causes stated as choices, and choices attached to named people on dated days. By the summer of 1991 the opening Gorbachev had created in 1985 had reached the center of the system itself. The Baltic states were leaving, Ukraine was claiming sovereignty, and a new union treaty meant to hold a looser federation together was scheduled for signature on August 20. The men who struck on August 19, the vice president, the prime minister, the heads of the army, the interior ministry, and the secret police, understood the treaty as the union's death certificate and acted to stop it. Their failure, and what the republics did with the failure in December, is the Cold War's last sequence, and it mirrors November 1989 at larger scale: an old command given, a crowd and a rival authority refusing it, and armed men declining to enforce it.")

# ------------------------------------------------------ 20 THE COUP FAILS
content_text('Three days in August',
             ['The emergency was announced on August 19, 1991.',
              'Gorbachev was held at his vacation home in Crimea.',
              'Yeltsin stood on a tank outside the Russian parliament.',
              'Crowds defended the building and units refused orders.',
              'The coup collapsed on August 21.'],
             "Teach the coup as a test of where authority had gone since 1985, because every asset the plotters held turned out to be the wrong kind. They held the ministries, the television stations, and tanks in the streets of Moscow. They did not hold legitimacy: Boris Yeltsin was the elected president of the Russian republic, chosen in a vote that June, and his climb onto a tank outside the Russian parliament gave resistance a face and a lawful claim. They did not hold the crowd, which built barricades and stayed through two nights. Above all they did not hold the army's obedience: key units refused orders to storm the parliament, and the single armored clash that killed three young men on the second night showed the plotters what enforcement would cost. On August 21 their authority collapsed. Gorbachev returned to Moscow as president of a country whose republics now took their lead from Yeltsin.",
             kick='G · The center gives way: 1991', size=24)

# ------------------------------------------------------ 21 DECEMBER 1991
content_text('Dissolved by declaration',
             ['Ukraine voted for independence on December 1.',
              'Three republics declared the union ended on December 8.',
              'Eleven republics joined the commonwealth on December 21.',
              'Gorbachev resigned on television on December 25.',
              'That evening, the flag came down over the Kremlin.'],
             "Run the December sequence as the record gives it, step by dated step, because its order explains the ending better than any summary. Ukraine's referendum on December 1 removed the second largest republic from any federation Gorbachev could still propose. A week later the leaders of Russia, Ukraine, and Belarus, the three Slavic republics that had founded the union in 1922, met and declared that the Soviet Union had ceased to exist, forming a Commonwealth of Independent States in its place. On December 21, eleven republics joined the commonwealth, and the union's institutions, including control of its armed forces, passed to the new arrangement. Gorbachev's resignation on December 25 was therefore a recognition, not a cause: he resigned an office whose country had already been declared out of existence, and the flag change over the Kremlin that evening closed the state that had stood since 1922.",
             kick='G · The center gives way: 1991', size=24)

# ------------------------------------------------------ 22 AT A GLANCE
s = slide(NAVY)
kicker(s, 'The ending at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Reformed, breached, settled, dissolved', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Reformed', 'Gorbachev, 1985; glasnost and perestroika', 'The party loosens its own grip; obedience becomes a choice'),
        ('Diplomacy', 'Reykjavik 1986; the Gate 1987; INF, December 1987', 'A class of weapons destroyed; the challenge set in public'),
        ('Breached', 'Poland, Leipzig, and November 9, 1989', 'The wall opens; Germany reunified inside NATO, 1990'),
        ('Dissolved', 'The failed coup, August 1991; December 1991', 'Ukraine votes; the republics declare; Gorbachev resigns')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.2, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.25, yy + 0.05, 5.1, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.55, yy + 0.05, 3.9, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the closing table of the guided notes, The Ending at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. Reformed: Gorbachev takes power in 1985 and his two policies loosen the party's control of the economy, the press, and public argument. Diplomacy: the Reykjavik near miss of 1986, the Brandenburg Gate challenge of June 1987, and the INF Treaty that December destroying a class of weapons. Breached: Poland's election, the Leipzig crowds, the night of November 9, 1989, and the settlement that reunified Germany inside NATO on October 3, 1990 and dissolved the Warsaw Pact. Dissolved: the failed coup of August 1991 and the December sequence, Ukraine's vote, the republics' declaration, and the resignation of December 25, 1991. Grade the table on sequence and on actors named, not on adjectives.")

# ------------------------------------------------------ 23 VOCAB A
vocab('Words for the reform and the treaty',
      [('glasnost', 'openness: discussion, criticism, a freer press'),
       ('perestroika', 'restructuring the economy and the political system'),
       ('Solidarity', 'the Polish union that led the turn of 1989'),
       ('INF Treaty', 'the 1987 treaty destroying a class of missiles')],
      "These definitions match the guided notes, and the notes carry them in full, word for word. glasnost: Mikhail Gorbachev's policy of openness in the Soviet Union from 1985, allowing public discussion, criticism of officials, and a freer press. perestroika: Gorbachev's program of restructuring the Soviet economy and political system, meant to make a failing system work and ending by loosening the party's control of both. Solidarity: the Polish labor movement founded in 1980 at the Gdansk shipyard, the first independent union in the Communist bloc, which survived martial law to lead Poland's turn from Communist rule in 1989. INF Treaty: the treaty of 1987 in which the United States and the Soviet Union agreed to destroy all their land-based missiles with ranges between about 300 and 3,400 miles, the first agreement to eliminate a class of nuclear weapons. Hold the four together: two policies, one movement, one treaty, which is the cast of the ending in miniature.")

# ------------------------------------------------------ 24 VOCAB B
vocab('Words for the wall and the ending',
      [('Berlin Wall', 'built 1961; breached by crowds, November 9, 1989'),
       ('German reunification', 'East and West joined in one state, October 1990'),
       ('dissolution of the Soviet Union', 'the state of 1922 ends, December 1991')],
      "Three more terms, in the guided notes wording, carried in these notes in full, word for word: Berlin Wall: the wall the East German government built in 1961 to stop its citizens fleeing to the West, which became the central symbol of the divided Europe, and which crowds breached on November 9, 1989; German reunification: the joining of East and West Germany into one state in October 1990, ending the division imposed after the Second World War; dissolution of the Soviet Union: the ending of the Soviet Union in December 1991, when its republics declared independence and the state that had stood since 1922 ceased to exist. Notice the grammar of the three definitions, because it is the lesson's argument in small: a wall built by a government, a country joined by negotiation and election, and a state ended by its own republics' declarations. No definition in this lesson names a conquering army, and students should be asked why that is.")

# ------------------------------------------------------ 25 CLOSING SYNTHESIS
s = slide(NAVY)
kicker(s, 'Closing synthesis')
text(s, 0.9, 1.35, 11.5, 1.1, 'Where this unit ends', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 2.6,
     ["The Cold War ended without the direct war both sides had armed against for forty five years, an ending no one in 1949 or 1962 or 1983 had predicted.",
      "It left the United States the world's only superpower, over a map of new states, old weapons, and unsettled questions the next unit takes up."],
     size=23, color=POWDER, leading=1.3)
notes(s, "Close the unit by stating its ending as a finding rather than a celebration, in the terms the lesson has used throughout. The rivalry that began with containment in the 1940s, ran through Korea, the missile crisis, and Vietnam, hardened again in the 1980s, and then ended, between a Polish election in the summer of 1989 and a flag change in Moscow on Christmas night 1991, without the direct superpower war that every lesson in this unit showed the two sides preparing for. What it settled can be listed: a divided Germany reunified inside the Western alliance, the Warsaw Pact dissolved, the Baltic states free, and the Soviet Union gone. What it left unsettled belongs to the next unit: the future of the new states, the control of an arsenal divided among republics, and the conduct of a world with one superpower. Students should leave able to say which list any given fact of 1989 to 1991 belongs on.")

# ------------------------------------------------------ 26 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ["Why did the Cold War end between 1989 and 1991, and what did its ending settle and leave unsettled? Weigh the causes from the documents, and answer the strongest counterclaim to your own verdict."],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The End in Sequence: the Gate speech, the treaty, Berlin, the coup, the dissolution'),
        ('Notebook', 'Notebook page: the questions of the ending, what the documents show, what was decided'),
        ('Quick check', 'Crowds at the Brandenburg Gate: the photograph, the sequence, the speech weighed'),
        ('Writing', 'Why the Cold War Ended When It Did: a verdict weighed, the TPSP DBQ as its linked extension')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the two reforms defined, the night of November 9 in sequence, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close the unit by handing the weighing to the students, which is what this lesson exists to do. The activity, The End in Sequence, gives them the five stations in order, the Brandenburg Gate speech from the audited text, the INF Treaty from the treaty record, the Berlin summary paired with the December 1989 photograph, and labeled summaries of the coup's failure and the dissolution, and asks for a verdict with the strongest counterclaim answered. The notebook page charts the questions of the ending. The quick check reads the Brandenburg Gate photograph and tests the November 9 sequence against the famous sentence of 1987. The writing task, Why the Cold War Ended When It Did, requires a weighed verdict from the evidence bank; teachers may extend it with The Primary Source Project premium DBQ 21, Did Containment Serve American Interests, a linked resource not reproduced here. The exit ticket has three parts: the two reforms defined, November 9 in sequence, and the lesson question with the settled and the unsettled separated. The review day and the unit test follow from here.")

dc.save(OUT)
