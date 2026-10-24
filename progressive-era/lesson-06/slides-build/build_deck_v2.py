#!/usr/bin/env python3
"""Lesson 6 deck: Wilson and the New Freedom.
Built on the shared system in deck_common.py, replicating the approved
Lesson 1 deck: image-led slides, fragments only on screen, comprehensive
speaker notes, full lesson and vocabulary coverage.
Fonts: Georgia titles, Lato body."""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags,
                         photo_right, divider_photo, content_photo,
                         content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED, W)

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

# ---------------------------------------------------------------- 1 · TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, dc.prs.slide_width, dc.prs.slide_height)
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'PROGRESSIVE ERA · LESSON 6', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Wilson and the New Freedom', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'How a campaign promise met the machinery of governing', size=17, color=POWDER)
notes(s, "Open with the man and the moment. Woodrow Wilson took the oath in March 1913, the first Democratic president in sixteen years, and he arrived with something neither Roosevelt nor Taft had enjoyed in their fights with Congress: a legislature controlled by his party. The photograph shows Wilson delivering his first inaugural address at the Capitol, with outgoing President Taft seated at the side of the stand, an orderly handoff that hides how sharp the argument of 1912 had been. Wilson had campaigned on the New Freedom, a promise to restore competition by tearing down what he called the triple wall of privilege. Today's lesson follows that promise wall by wall: the tariff, the banking system, and the trusts. But tell students to watch for the twist the reading ends on. Governing kept pushing Wilson toward the tools of Theodore Roosevelt, the man he had just beaten, and the most interesting question of the lesson is why. The unit question on the guided notes sits beneath today's lesson question: How did Americans respond to the problems created by industrialization, urbanization, and political corruption? Wilson's presidency is one of the largest answers.")

# ------------------------------------------------- 2 · ESSENTIAL QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did Wilson\'s New Freedom differ from Roosevelt\'s New Nationalism, and how far did the difference actually go?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did Americans respond to the problems created by industrialization, urbanization, and political corruption?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Put the lesson question up and keep the focus narrow. This lesson is the unit question answered at the level of the presidency: faced with the problems created by industrialization, one president responded with the most productive legislative first term of the Progressive Era. Students have met the problems in Lesson 1 and the political machinery in Lesson 3, and they have just spent two lessons on Roosevelt and Taft. Wilson is the third president in that sequence, and the comparison is the engine of the lesson. A useful cold open: ask students what they would attack first if they inherited the problems of 1900, prices, banks, or monopolies, and have them commit to an answer. Wilson attacked all three at once, in a single Congress, which almost no president attempts. Also flag the phrase students will hear within minutes, the triple wall of privilege. It is Wilson's own framing from his first annual message, and the whole lesson is organized by it, section by section in the guided notes.")

# ------------------------------------------------------ 3 · THREE WALLS MAP
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.35, 11.5, 1.0, 'The triple wall of privilege', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.5)
rows = [('1', 'The tariff', 'duties near 40 percent sheltered the trusts and raised prices'),
        ('2', 'The banks', 'a currency and credit system no public authority controlled'),
        ('3', 'The trusts', 'monopoly practices the law reached slowly, case by case')]
yy = 2.95
for n, t, d in rows:
    text(s, 0.9, yy, 0.7, 0.7, n, size=30, color=RUST_LT, font='Georgia')
    text(s, 1.65, yy + 0.04, 3.3, 0.7, t, size=27, color=CREAM, bold=True)
    text(s, 5.1, yy + 0.10, 7.4, 0.7, d, size=20, color=POWDER)
    yy += 1.02
text(s, 0.9, 6.15, 11.5, 0.6, 'Watch for the drift: the promise bends as he governs.',
     size=20, color=RUST_LT, leading=1.25)
notes(s, "This slide is the map of the lesson, and it matches the guided notes exactly. In his first annual message Wilson named the enemy as a triple wall of privilege. The first wall was the tariff, import duties averaging about 40 percent that sheltered big combinations from foreign competition and raised prices at home. The second wall was the banking system, a currency and credit structure no public authority controlled, as the panic of 1907 had proved. The third wall was the trusts, monopoly practices that existing law reached only slowly and case by case. The New Freedom promised to tear down all three walls and restore competition. Underneath the map sits the lesson's real question, which the line at the bottom names: the drift. What Wilson actually built, especially in 1914 and 1916, often resembled Roosevelt's New Nationalism more than his own campaign. Students should finish able to argue both readings, with a named law for each wall.")

# ------------------------------------------------- 4 · SECTION A DIVIDER
divider_photo('wilson-port.jpg', 'Section A', 'The Setup',
              ['A president with a Congress of his own party',
               'The program he carried in: the New Freedom'],
              "The photograph is Wilson's formal portrait by Harris and Ewing, the Washington studio that photographed the presidents of this era. Set up who this man was before the legislation starts. Wilson was a former professor and president of Princeton, then a one-term governor of New Jersey, and he governed like a lecturer: he believed arguments, clearly stated, moved legislatures. He was also a party leader in a way Roosevelt and Taft had not been while in office. The Democrats held both houses of Congress, and Wilson intended to use that majority as a single instrument, taking his program in sequence: tariff first, then banking, then the trusts. Section A of the guided notes asks for exactly these facts: he took office in 1913, with a Congress run by his own party, and he named the enemy the triple wall of privilege: the tariff, the banking system, and the trusts. Everything in the next three sections is one wall at a time, in the order Wilson himself chose to attack them.",
              title_size=54)

# ------------------------------------------------------- 5 · TWO PROGRAMS
content_text('Two programs from 1912',
             ['The New Nationalism accepted bigness and would supervise it with commissions.',
              'Under the New Freedom, bigness itself is the problem.',
              'Wilson would restore competition and let the market police itself.',
              'Roosevelt trusted commissions, and Wilson trusted competition.'],
             "Students cannot see the drift unless they remember the argument of 1912, which Lesson 5 covered and this lesson reopens. Roosevelt's New Nationalism accepted big business as permanent and proposed to supervise it: strong federal commissions, expert regulators, continuous oversight. Wilson's New Freedom, shaped by his adviser Louis Brandeis, held that bigness itself was the problem. Restore competition, break the privileges that sheltered monopoly, and the economy would police itself without a large permanent bureaucracy. That contrast is the scoring key for today's activity, Sort the Record, where students classify Wilson's laws as New Freedom or New Nationalism. Plant the distinction now in its sharpest form: Roosevelt wanted a referee standing permanently on the field; Wilson wanted the rigged fences taken down so the game would be fair on its own. By the end of the lesson students will judge which description fits the Federal Trade Commission, and the honest answer is Roosevelt's. Hold that verdict until they have seen the trust wall, where the evidence sits.",
             kick='The setup')

# ------------------------------------------------------ 6 · TRIPLE WALL
content_text('The triple wall of privilege',
             ['The triple wall joined the tariff, the banking system, and the trusts.',
              'Privilege means advantage granted and guarded by law.',
              'The three parts formed one wall, sheltering the same interests.',
              'Wilson promised to tear it down and restore competition.'],
             "Now the framing in Wilson's own words. In his first annual message, delivered in person to Congress in December 1913, the first president since John Adams to address the legislature face to face, Wilson named the enemy as a triple wall of privilege: the tariff, the banks, and the trusts. Each word did political work. Privilege said the problem was not success but advantage granted and guarded by law. Wall said the three parts formed one structure, sheltering the same interests behind it. The campaign promise attached to the framing was restoration: tear the walls down and competition, the discipline Wilson trusted, would return on its own. The Section A blanks in the guided notes come straight off this slide. One teaching point: Wilson's sequence was strategic, not accidental. The tariff came first because every faction of his party could unite against high duties, and an early win would bank the authority he needed for the harder banking fight that followed.",
             kick='The setup')

# ------------------------------------------------- 7 · SECTION B DIVIDER
divider_photo('tariff-port.jpg', 'Section B', 'The Tariff Wall',
              ['Duties near 40 percent, sheltering the trusts',
               'The first wall Wilson attacked'],
              "The cartoon is a 1908 Puck magazine image by J. Keppler Jr. on the tariff question, drawn before Wilson took office. It makes a useful point by its date alone: the tariff had been the standing argument of American politics for a generation. Every election since the Civil War had turned on it, because duties decided who paid for the federal government and whose products received protection. High tariffs sheltered American manufacturers from foreign competition, and the largest combinations hid behind them, charging what the shelter allowed. That is why a dry subject, tax rates on imports, counts as a wall of privilege in Wilson's framing: the tariff was where government favor touched every price in the country. Section B of the guided notes begins here, and its first facts are the size of the cut and the problem the cut created: average duties from about 40 percent to about 25 percent, and a hole in the revenue that had to be filled.",
              title_size=54)

# ------------------------------------------------------------ 8 · UNDERWOOD
content_text('The Underwood Tariff',
             ['The Underwood Tariff cut average duties from about 40 percent to about 25 percent.',
              'The cut was the first real reduction in a generation.',
              'Foreign competition would discipline the sheltered trusts.',
              'Wilson pressed the bill on Congress in person.'],
             "The Underwood Tariff of 1913, named for House leader Oscar Underwood of Alabama, cut average import duties from about 40 percent to about 25 percent. Wilson forced the pace personally. In April 1913 he went to Capitol Hill and addressed Congress in person to press the bill, the first president to do that since John Adams, breaking a practice that ran back to Jefferson. The cut mattered in two directions at once. For the New Freedom argument, lowering duties exposed sheltered combinations to foreign competition, using the world market as the discipline on monopoly. For consumers, it attacked the cost of living, the argument Democrats had made against high Republican tariffs for decades. But the reading slows down on the problem the cut created, and students should feel its weight before the next slides: tariffs were not a side income for the federal government. They were the main revenue, the money the government ran on. Cutting them opened a hole in the budget, and something had to plug it.",
             kick='The tariff wall')

# ------------------------------------------------------------- 9 · STAT 25%
stat('25%', 'the average import duty under the Underwood Tariff',
     'Down from about 40 percent. The first real reduction in a generation.',
     "Give this number its own moment, because it is the first kept promise of the term. Average import duties fell from about 40 percent to about 25 percent under the Underwood Tariff, the first real reduction in a generation. Two precisions matter for the test. First, the figure is an average across thousands of scheduled goods; some duties vanished entirely and others barely moved, and the fights over the sugar and wool schedules were famous. Second, 25 percent was still a substantial tariff by free-trade standards; the New Freedom lowered the wall rather than leveling it. Students sometimes hear the word tariff and tune out, so translate the percentage into a household fact: duties were a tax folded into the price of cloth, tools, and sugar, paid at the counter by people who never saw the word tariff on any receipt. Cutting the average rate by more than a third was the largest single price intervention of Wilson's first year in office.",
     kick='The tariff wall')

# --------------------------------------------------- 10 · SIXTEENTH AMENDMENT
content_text('The plug: the Sixteenth Amendment',
             ['Tariffs were the main revenue, so cutting them opened a hole.',
              'The Sixteenth Amendment was ratified in February 1913, just before Wilson took office.',
              'The amendment overturned Pollock (1895), which had killed an income tax.',
              'The first tax took 1 percent on incomes above $3,000, with surtaxes to 7 percent.'],
             "The plug for the revenue hole was ready before Wilson needed it. The Sixteenth Amendment, ratified in February 1913, just before his inauguration, authorized a federal income tax and overturned the Supreme Court's 1895 decision in Pollock v. Farmers' Loan, which had struck an earlier income tax down as unconstitutional. The Underwood Act itself carried the first tax under the amendment, and by later standards it was modest: 1 percent on incomes above 3,000 dollars, with surtaxes rising to 7 percent on the largest incomes. Few Americans paid it directly. The reading insists the importance was structural, and the exit ticket returns to exactly that word. Tariffs had made federal revenue depend on imports and on taxing consumption at the border. The income tax gave the government a revenue source that grew with the economy it was learning to regulate. A government that can tax incomes can afford to lower tariffs, fund commissions, and act in an emergency. Section B's blanks end here: revenue, Sixteenth, February 1913, Pollock, incomes, 1 percent.",
             kick='The tariff wall')

# ------------------------------------------------ 11 · SECTION C DIVIDER
divider_photo('morgan-port.jpg', 'Section C', 'The Banking Wall',
              ['A currency no one controlled',
               'In 1907 the rescue was a private citizen'],
              "The portrait is a 1902 studio portrait of J. P. Morgan by the Pach Brothers, showing the banker who stands for the second wall. In the panic of 1907, when banks failed and credit froze across the country, there was no public institution able to act as lender of last resort. So a private citizen did it. Morgan summoned the great bankers and trust presidents to his library in New York and organized the rescue of the financial system himself, deciding which institutions would be saved and which would be allowed to fail. It worked, which was precisely the scandal. The money supply of the United States had rested, in its worst week, on the judgment and the lifespan of one private banker, then seventy years old. Morgan died in the spring of 1913, and the argument his rescue started produced the Federal Reserve within the year. Section C of the guided notes opens with that panic: 1907, no lender of last resort, and a Congress determined to find out who actually ran the money.",
              title_size=46)

# ------------------------------------------------------------ 12 · PUJO
content_photo_s('pujo-port.jpg', 'The panic and the money trust',
              ['In 1907, banks failed with no lender of last resort.',
               'J. P. Morgan organized the rescue himself.',
               'The Pujo Committee held hearings in 1912 and 1913.',
               'The hearings documented a money trust of interlocked banks.'],
              "The photograph shows members of the Pujo Committee, the House subcommittee that investigated the money trust through 1912 and 1913 under Representative Arsène Pujo of Louisiana, with the lawyer Samuel Untermyer as its chief counsel. Morgan himself testified, along with the heads of the great banks and railroad corporations. The committee documented what critics had alleged for years: a money trust, a small web of interlocked banks and corporations whose directors sat on one another's boards and could steer the credit of the whole country. Pair the evidence with the panic for students. The banking wall was really two complaints fused together: the system was unstable, collapsing in panics with no lender of last resort, and it was privately governed, run by men no voter had chosen. Any successful reform had to answer both complaints at once, and the answers pointed in opposite directions, toward public control and away from concentrated control. That tension is the design problem of the next two slides, and reading question 3 tests it directly.",
              kick='The banking wall')

# ------------------------------------------------------- 13 · TWELVE BANKS
s = slide(NAVY)
photo_right(s, 'fedboard-port.jpg')
kicker(s, 'The banking wall')
text(s, 0.9, 1.5, 6.9, 2.4, '12', size=110, color=CREAM, font='Georgia', leading=1.05)
text(s, 0.9, 3.35, 6.7, 1.0, 'regional Reserve banks created by the Federal Reserve Act', size=25, color=CREAM, leading=1.25)
rule(s, 0.92, 4.55)
text(s, 0.9, 4.85, 6.6, 1.8, 'Owned by the member banks of each district. Supervised by a board in Washington.',
     size=20, color=POWDER, leading=1.3)
notes(s, "The answer was a dozen banks, not one. The Federal Reserve Act of December 1913 created twelve regional Federal Reserve banks in districts across the country, from Boston to San Francisco, a structure with no real parallel among the central banks of Europe. The photograph shows the first Federal Reserve Board in 1914. The number itself was the argument in institutional form: banking power would be dispersed geographically, so that credit for a farmer in the South or a merchant in the Midwest would not be allocated solely from New York. Each regional bank was owned by the member banks in its district, which kept private bankers inside the system rather than outside it, fighting it. Above the twelve sat a Federal Reserve Board in Washington, appointed by the president, so public authority held the top of the structure. Dispersed below, supervised above: after the next slide, students should be able to say which half of that formula answers which fear.")

# --------------------------------------------------------- 14 · TWO FEARS
content_text('Built to answer two fears',
             ['The first fear was Wall Street\u2019s money trust, answered by a public board.',
              'The second fear was one political bank, answered by twelve regional banks.',
              'The currency could expand or contract with the needs of business.',
              'The lender of last resort would be an institution, not a man.'],
             "Slow down on this design, because reading question 3 and the guided notes both test it. The Federal Reserve was built to answer two opposite fears at once. The first fear was Wall Street: that a private money trust, documented by the Pujo Committee, would keep control of the nation's credit. The answering feature was public supervision, a Federal Reserve Board in Washington appointed by the president, holding authority over the whole system. The second fear was the mirror image: that a single government bank in Washington would put the money supply under political control, and that the East would dominate the rest of the country. Its answering feature was the twelve regional banks, owned by the member banks and spread across the districts. Between the two halves, the system could expand or contract the currency with the needs of business, the elastic currency the old system lacked, so the next panic would meet a lender of last resort that was an institution rather than a person.",
             kick='The banking wall')

# ------------------------------------------------ 15 · SECTION D DIVIDER
divider_photo('gompers-port.jpg', 'Section D', 'The Trust Wall',
              ['Named practices, banned in advance',
               'And a commission the campaign argued against'],
              "The portrait is Samuel Gompers, founder and longtime president of the American Federation of Labor, in a Harris and Ewing studio photograph. He stands on the divider for the trust wall because labor turns out to be one of its main battlegrounds. The third wall looked like a contest between government and big business, but the law of monopoly had repeatedly landed on unions instead: courts had treated strikes and boycotts as conspiracies in restraint of trade, and the Sherman Antitrust Act, written against trusts, had been used against workers, most famously in the Danbury Hatters case. Wilson's trust program therefore had two audiences, business and labor, and the Clayton Act addressed both inside the same statute. Keep Gompers in view for the next two slides: his verdict on the Clayton Act, that it was labor's Magna Carta, is the phrase students remember, and the guided notes test the protection behind it, the declaration that unions were not conspiracies in themselves.",
              title_size=54)

# ------------------------------------------------------------- 16 · CLAYTON
content_text('The Clayton Antitrust Act',
             ['The Sherman Act\u2019s general words left everything to judges.',
              'The Clayton Act banned price discrimination meant to destroy competitors.',
              'It banned tying contracts that forced buyers to take unwanted products.',
              'It banned interlocking directorates linking supposed rivals.'],
             "The Clayton Antitrust Act of 1914 fixed a drafting problem in the Sherman Act. The older law had banned combinations in restraint of trade in general words, which left nearly everything to judges and produced uneven results: trust prosecutions that took years, rulings that varied, and a statute that could fall on a union as easily as on a monopoly. Clayton took the New Freedom approach the campaign had promised. It named the specific practices and banned them in advance. Price discrimination meant to destroy competitors. Tying contracts that forced a buyer to take unwanted products in order to get the one product he wanted. Interlocking directorates linking supposed rivals through shared board members, the same interlocks the Pujo Committee had exposed in banking. Each practice on this slide is a Section D blank in the guided notes. The theory was pure 1912 Wilson: write the rules of competition clearly, and the market would do the rest without a standing army of regulators. Hold that theory up to the light, because within the same year Wilson built the standing regulator anyway.",
             kick='The trust wall')

# ------------------------------------------------------- 17 · MAGNA CARTA
content_text('Labor\u2019s Magna Carta',
             ['The Clayton Act declared unions not conspiracies in themselves.',
              'The act limited court injunctions against strikes.',
              'Gompers called the act labor\u2019s Magna Carta.'],
             "The Clayton Act's most celebrated sections were about labor, not trusts. The act declared that labor unions were not conspiracies in themselves, a sentence aimed at decades of court rulings, and it limited the injunctions federal courts could issue against strikes, the orders that had let a single judge halt a walkout overnight. Samuel Gompers hailed the law as labor's Magna Carta, and the phrase is worth unpacking for students. Magna Carta is the charter the English barons forced on King John in 1215, the founding symbol of rights that even a government must respect. Gompers was claiming that standing for organized workers. Teachers should add the honest footnote the reading leaves implicit: courts narrowed these labor protections in the 1920s, and labor's full statutory security did not arrive until the 1930s. For 1914, though, the direction was unmistakable, and the guided notes ask for the protected party by name: labor unions were not conspiracies in themselves. Hold the phrase; it returns in the vocabulary.",
             kick='The trust wall')

# ------------------------------------------------------------ 18 · THE FTC
content_text('Wilson builds a commission',
             ['Wilson created the Federal Trade Commission in 1914.',
              'The Commission is a permanent body of experts.',
              'It holds power to investigate corporations.',
              'It holds power to stop \u201cunfair methods of competition\u201d.'],
             "Then Wilson built a commission, and this slide is the turn the whole lesson leans toward. The Federal Trade Commission Act of 1914 created the FTC, a permanent body of experts empowered to investigate corporations and stop unfair methods of competition. Compare it with the Clayton approach on the previous slides. Clayton listed offenses in advance, like a statute book, and trusted courts to apply the list. The FTC instead set a standard, unfair methods, and trusted experts to apply it continuously, business by business and year after year. That is the New Nationalism's central tool: Roosevelt's method of supervising big business continuously rather than suing it occasionally, the very program Wilson had campaigned against, reached for within two years of defeating it. Reading question 4 asks students to make exactly this identification and defend it with the commission's powers. The vocabulary definition is precise and students will meet it again: permanent expert commission empowered to stop unfair methods of competition.",
             kick='The trust wall')

# ------------------------------------------------ 19 · SECTION E DIVIDER
divider_photo('train-port.jpg', 'Section E', 'The Drift',
              ['1916: federal credit and a federal eight-hour day',
               'The promise bends toward Roosevelt'],
              "The photograph shows a Tanana Valley Railroad train crossing a trestle bridge in Alaska in 1916, the year of the two laws in this short final section. Section E of the guided notes is called The Drift, and the name is the argument: after the three walls came down, Wilson's governing did not stop at his campaign program. It drifted, steadily and by his own choice, toward federal systems and federal standards in areas the New Freedom had never promised to enter. Two laws of 1916 mark the direction. One built a federal credit system so that farmers could borrow on better terms. The other set working hours for an entire industry by national law. Neither tore down a wall of privilege; both put the federal government permanently inside a sector of the economy. That is the pattern students should name when they reach the verdict slide: the campaign of 1912 argued over whether big government or big business was the danger, and by 1916 Wilson was using the first to manage the second.",
              title_size=54)

# ---------------------------------------------------------- 20 · 1916 LAWS
content_text('Two laws of 1916',
             ['The Federal Farm Loan Act built a federal credit system for farmers.',
              'The Adamson Act set an eight-hour day for railroad workers.',
              'Congress passed the Adamson Act in days to head off a nationwide rail strike.',
              'The two laws set federal standards by law, not by the market.'],
             "The two statutes are quick to teach, and both are Section E blanks. The Federal Farm Loan Act of 1916 built a federal credit system for farmers, with land banks that could lend on farm mortgages at rates private banks had not offered, a permanent federal presence in agricultural finance modeled in part on the Federal Reserve's regional design. The Adamson Act, also 1916, set an eight-hour day for railroad workers by federal law. Its circumstances show the drift in action: facing a threatened nationwide rail strike, Wilson went to Congress and asked for the law directly, and Congress passed it within days. A president who had campaigned on limiting the government's role was setting the working hours of a national industry to keep the trains running, and calling it necessity. Students do not have to judge the choice harshly to see the pattern. Necessity, repeated often enough, becomes a governing philosophy, and by 1916 Wilson's second phase had quietly become Roosevelt's program.",
             kick='The drift')

# ------------------------------------------------------------- 21 · VERDICT
content_text('What the New Freedom became',
             ['Wilson left a central bank, an income tax, a trade commission, and clarified antitrust law.',
              'All four creations still stand.',
              'The argument of 1912 was never fully settled.',
              'Wilson\u2019s own presidency voted both ways.'],
             "Close the content with the reading's verdict, which is deliberately balanced. Wilson's first term redrew the working machinery of the federal government: a central banking system, an income tax, a trade commission, and clarified antitrust law all date from it, and all four still stand more than a century later. The campaign argument of 1912 was never fully settled, because Wilson's own presidency voted both ways. He tore down the tariff wall exactly as promised and legislated competition in the Clayton Act as promised, and then he governed the economy through boards and commissions in a manner Theodore Roosevelt would have recognized as his own. Reading question 5 asks students to argue whether that makes the campaign dishonest or simply shows the difference between campaigning and governing, and either position earns credit when it carries two specific facts. Point them forward before the vocabulary: Lesson 7 turns to the suffrage movement, which watched these victories from outside and asked when its turn would come.",
             kick='The verdict')

# ------------------------------------------------------------- 22 · VOCAB A
vocab('Words for 1913',
      [('Underwood Tariff', 'law cutting average import duties from about 40 percent to about 25 percent'),
       ('Sixteenth Amendment', 'amendment authorizing a federal income tax, overturning the Pollock decision'),
       ('Federal Reserve Act', 'law creating twelve regional Reserve banks under a federal board in Washington')],
      "These definitions match the guided notes word for word, so students can copy them directly, with the years the key terms carry: Underwood Tariff (1913): law cutting average import duties from about 40 percent to about 25 percent. Sixteenth Amendment (1913): amendment authorizing a federal income tax, overturning the Pollock decision. Federal Reserve Act (1913): law creating twelve regional Reserve banks under a federal board in Washington. Two memory hooks help. The tariff and the amendment are a matched pair, the cut and the plug, and a student who remembers the revenue problem remembers both terms at once. The Federal Reserve definition holds the whole design in one sentence: twelve and regional set against federal and Washington, the two fears answered in a single line. The unit test's matching section uses these definitions nearly verbatim, so accuracy here pays off directly. Have students say the years aloud with the terms; 1913 carries three of this lesson's five key terms, and the year is part of each term's full name in the guided notes.")

# ------------------------------------------------------------- 23 · VOCAB B
vocab('Words for 1914',
      [('Clayton Antitrust Act', 'law naming and banning specific monopoly practices and protecting unions from conspiracy charges'),
       ('Federal Trade Commission', 'permanent expert commission empowered to stop unfair methods of competition')],
      "Two terms remain, both from 1914, and both belong to the trust wall. Clayton Antitrust Act (1914): law naming and banning specific monopoly practices and protecting unions from conspiracy charges. Federal Trade Commission (1914): permanent expert commission empowered to stop unfair methods of competition. The pair is the lesson in miniature, and it is worth saying so out loud. Clayton is the New Freedom method, a list of banned practices written by Congress in advance. The Commission is the New Nationalism method, a standing body of experts trusted to judge business conduct as it happens. Wilson signed both in the same season, which is why the campaign argument of 1912 could never be settled by his record alone. One wording precision: the key term is the institution, the Federal Trade Commission, and the statute that created it is the Federal Trade Commission Act. Students who can state both definitions and then say which 1912 program each law belongs to are ready for the activity.")

# --------------------------------------------------------- 24 · TODAY'S WORK
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Sort the Record: NF or NN', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 2.6,
     ['Take Wilson\u2019s record item by item. Sort each law as New Freedom or New Nationalism, and defend the call with what the law actually does.'],
     size=23, color=POWDER, leading=1.3)
rows = [('1913', 'Underwood Tariff and the Sixteenth Amendment'), ('1913', 'The Federal Reserve Act'),
        ('1914', 'The Clayton Antitrust Act'), ('1914', 'The Federal Trade Commission'),
        ('1916', 'Farm Loan Act and Adamson Act')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.5, 0.6, d, size=19, color=CREAM)
    yy += 0.52
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the three walls and their laws, why the income tax is structural, one fact for or against the claim.',
     size=16, color=POWDER)
notes(s, "Close by handing the lesson to its activity, Sort the Record: NF or NN, which students already have. Working through Wilson's record item by item, students sort each law as New Freedom or New Nationalism and defend the call with what the law actually does. The tariff cut and Clayton's list of banned practices sort cleanly as New Freedom. The Federal Trade Commission is the clearest New Nationalism item on the table. The Federal Reserve splits most classes, because its regional structure sounds like Wilson and its standing federal board sounds like Roosevelt, which is exactly the argument the lesson was built to produce. The 1916 laws push the same way as the Commission. Then the exit ticket from the guided notes, three items: name the three walls and the law that attacked each; explain in one sentence why the income tax is called structural rather than just a new tax; and attack or defend the claim that Wilson won the argument of 1912 and then governed with the loser's tools, using one fact. Next lesson, the suffrage movement asks when its turn will come.")

dc.save(OUT)
