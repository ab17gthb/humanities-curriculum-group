#!/usr/bin/env python3
"""Gilded Age Lesson 2 deck, "Big Business and Its Critics," built to the
approved Progressive Era pilot system: image-led slides, fragments only on
screen, comprehensive speaker notes, full lesson + vocabulary coverage.
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
text(s, 0.9, 5.32, 11.5, 0.4, 'GILDED AGE · LESSON 2', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Big Business and Its Critics', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'How a few combinations came to run whole industries, and how the country argued about it', size=17, color=POWDER)
notes(s, "The photograph shows the Homestead Steel Works in Pennsylvania, photographed by the Detroit Publishing Company in about 1900 to 1910: a riverfront of mills, furnaces, and smokestacks on a scale no single workshop owner could have built. That scale is the subject of this lesson. After the Civil War, the largest American industries stopped being run by single owners and became corporations and then combinations, until in oil and steel a handful of men could set prices for the whole country. Frame the day as an argument with two honest sides. Big business plainly built much of modern America. Its critics said it had also captured the country, its prices, its railroads, and its politics. Students will weigh both claims against the evidence and answer the lesson question for themselves at the end.")

# ------------------------------------------------- 2 · LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('Did big business build modern America, capture it, or do both at once?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did industrial growth transform American life, and who gained, who paid, and who resisted?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question is the narrower one on the slide, and the unit question runs beneath it as the frame. This lesson answers the unit question through one industry-spanning argument. Industrial growth created a new kind of company, the combination, and the country then argued about who gained from it, who paid for it, and who resisted it. The gainers were real: owners of great fortunes, and also families who could suddenly afford kerosene light. The payers were real too: small refiners driven out, farmers and merchants who took prices set by others, and workers whose pay rarely rose with the efficiency gains. Keep the three choices in the question visible all hour. Built, captured, or both at once. By the closing slide students must pick one and defend it with facts, so every section should be heard as evidence for one side or the other.")

# --------------------------------------------------- 3 · THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.3, 11.5, 1.0, 'One argument over bigness', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.42)
rows = [('A', 'Why companies grew', 'industries too large for one owner, so corporations sold shares'),
        ('B', 'Two ways to take control', 'Carnegie went vertical in steel, Rockefeller horizontal in oil'),
        ('C', 'The argument over bigness', 'efficiency and philanthropy against rebates and ruined rivals'),
        ('D', 'Ideas that defended it', 'laissez-faire and Social Darwinism gave bigness a philosophy'),
        ('E', 'The Sherman Act', 'a law against trusts in 1890, and a weak first decade')]
yy = 2.82
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.7, n, size=26, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.03, 3.4, 0.7, t, size=23, color=CREAM, bold=True)
    text(s, 5.15, yy + 0.08, 7.3, 0.7, d, size=18, color=POWDER)
    yy += 0.9
notes(s, "This is the map of the lesson, and it follows the guided notes section by section. Section A explains why companies grew: the new industries cost more than any one owner held. Section B gives the two roads to control, vertical integration in steel and horizontal integration in oil, ending in the trust and, at the limit, monopoly. Section C stages the argument itself, the defenders' case from efficiency and philanthropy against the critics' case from secret rebates and destroyed rivals. Section D names the two ideas that defended the new order as a philosophy. Section E closes with the country's first legal answer, the Sherman Antitrust Act, and why it did so little for ten years. Tell students the organizers chart and the exit ticket both draw on sections B and E, so names, methods, and numbers need to land today.")

# ------------------------------------------------- 4 · SECTION A DIVIDER
divider_photo('steel-port.jpg', 'Section A', 'Why Companies Grew',
              ['Industries too large for one owner', 'to build or to run alone'],
              "The photograph is the same Homestead Steel Works image from the title slide, cropped on the mill buildings: chimneys, sheds, and rail lines running the length of the riverfront. Use it to make the opening problem concrete. A steel company did not need one furnace. It needed iron mines and coal fields, railroads and ships to move the ore, and furnaces and mills to turn it into rails and beams. An oil company needed wells, pipelines, refineries, and tank cars. No single family fortune covered costs on that scale, and no single owner could manage all of it. So the form of business itself had to change before the size of business could change. That is the one idea this short section carries: first the corporation, then the combination. Everything else in the lesson, the trusts, the arguments, and the law, grows out of that change in form.",
              title_size=44)

# ------------------------------------------------------ 5 · A NEW KIND OF COMPANY
content_text('A new kind of company',
             ['Industries after the Civil War outgrew the single owner',
              'Corporations sold shares to investors',
              'Shares raised more money than any one family held',
              'By the 1880s, the largest firms went further',
              'They began absorbing the competition itself'],
             "Teach the sequence slowly, because the guided notes test it in the first two blanks. Businessmen met the new costs by forming corporations, which sold shares to investors and could raise far more money than any single family held. A shareholder risked only the price of the shares, so thousands of strangers would put money into an enterprise none of them could have funded alone. That solved the money problem. Then, by the 1880s, the largest corporations were doing something more, and this is the turn the whole lesson hangs on. They were absorbing the competition itself, buying or crushing rival firms until in some industries only one combination was left standing. A corporation competing harder was one thing. A corporation ending competition was another, and Americans spent the rest of the century arguing about the difference. Section B names the two methods they used.",
             kick='A · Why companies grew', size=25)

# ------------------------------------------------- 6 · SECTION B DIVIDER
divider_photo('rockefeller-port.jpg', 'Section B', 'Two Ways to Take Control',
              ['Carnegie took every stage in steel', 'Rockefeller took every rival in oil'],
              "The portrait is John D. Rockefeller, painted by Eastman Johnson in 1895, when Standard Oil stood near its peak. Section B is the mechanical heart of the lesson, and students should leave it able to define both methods without hesitation. Andrew Carnegie built his steel empire mainly by owning every stage of production. John D. Rockefeller built Standard Oil mainly by combining every firm at one stage, refining. One man went up and down the chain, the other went across it. The section then introduces the legal device Rockefeller's lawyers built in 1882, the trust, and the end point both roads could reach, monopoly. The guided notes end the section with an organizers chart comparing the two men, so teach them as a pair throughout: same goal, control of an industry, reached by opposite routes.",
              title_size=40)

# ------------------------------------------------------ 7 · CARNEGIE
content_photo('carnegie-port.jpg', 'Carnegie: control every stage',
              ['Vertical integration in steel',
               'He bought iron mines and coal fields',
               'He owned the railroads and ships that carried the ore',
               'He owned the furnaces and mills that finished it',
               'Paying no middleman, his costs fell below his rivals'],
              "The portrait shows Andrew Carnegie in 1913, late in life and long after he had sold his steel company; use it as a portrait of the man, not as a picture of the 1880s. His method was vertical integration: control by one company of every stage in making and selling a product. Carnegie Steel bought iron mines and coal fields, the railroads and ships that carried the ore, and the furnaces and mills that turned it into rails and beams. Walk the chain aloud in order, mine to mill, because the order is the definition. Owning each stage, the company paid no middleman, and its costs fell below those of rivals who bought materials from others at marked-up prices. Note what vertical integration did not require: Carnegie did not have to buy every other steel firm. He could defeat them on cost, ton by ton, while they paid suppliers he owned.",
              kick='B · Two ways to take control')

# ------------------------------------------------------ 8 · ROCKEFELLER
content_photo('rockefeller-port.jpg', 'Rockefeller: control every rival',
              ['Horizontal integration in oil',
               'He persuaded, bought, or drove out rival refiners',
               'Standard Oil came to control most of the nation\u2019s refining',
               'One stage of the industry, held almost entire'],
              "This is the same Eastman Johnson portrait of Rockefeller from 1895, used again because his method is the mirror image of Carnegie's and the comparison is the point. Rockefeller built Standard Oil mainly by horizontal integration: control by one company of many firms at the same stage of an industry. He did not begin by owning wells or pipelines. He began at the refinery gate, persuading, buying, or driving out rival refiners until Standard controlled most of the nation's oil refining. Keep the three verbs distinct, because they describe three different experiences for the rivals. Some were persuaded with fair offers. Some were bought under pressure they could feel. Some were driven out by price cuts and railroad arrangements they could not match. Students often flatten this into 'he bought everyone.' He did not. The mixture of offer, pressure, and ruin is exactly what the critics in section C will describe.",
              kick='B · Two ways to take control')

# ------------------------------------------------------ 9 · THE TRUST
content_text('1882: the trust',
             ['Rockefeller\u2019s lawyers devised a new device',
              'Stockholders in about forty companies handed over their shares',
              'Trustees ran the companies as one enterprise',
              'One price, divided markets, closed plants',
              'Sugar, whiskey, lead, and farm machinery copied it'],
             "In 1882 Rockefeller's lawyers devised the trust: a combination of corporations that limits competition within an industry. Explain the mechanics plainly, because the word confuses students. Stockholders in about forty companies handed their shares to a small board of trustees and received trust certificates in return. The trustees now held the voting power of every member company, so they ran the companies as one enterprise. The trust could set one price, divide markets among its own plants, and close inefficient plants without any rival taking the business. Legally the companies still existed. In practice they no longer competed. Then widen the lens. Other industries copied the device, in sugar, whiskey, lead, and farm machinery, which is why Americans of the era spoke of 'the trusts' as a general class, not one oil company. The word trust in this lesson never means confidence; it names this specific arrangement.",
             kick='B · Two ways to take control')

# ------------------------------------------------------ 10 · 90 PERCENT STAT
stat('90 PERCENT', 'of the nation\u2019s oil refining, held by Standard Oil at its peak',
     'The end point of either road could be a monopoly: one combination, no effective competition, and the power to set the price itself.',
     "Dwell on the number, because it converts a definition into a fact students can argue with. The end point of either road, vertical or horizontal, could be a monopoly: control of an industry by one company or combination, with no effective competition. Standard Oil refined about 90 percent of the nation's oil at its peak. Ask what changes at 90 percent that has not already changed at 50. At half the market, a firm still fears the other half. At nine tenths, the remaining refiners are too small to discipline its prices. A firm with that share did not have to take the price the market offered. It could set the price itself, and every lamp in America burned at a price one board of trustees had chosen. Hold that thought. The defenders in section C will answer that Standard also made kerosene cheap. Both claims rest on the same 90 percent.",
     kick='B · Two ways to take control')

# ------------------------------------------------- 11 · SECTION C DIVIDER
divider_text('Section C', 'The Argument Over Bigness',
             'Defenders pointed to efficiency and generosity. Critics pointed to rebates and ruined rivals.',
             "This section is a debate, and it should be taught as one, with each side given its strongest form before either is judged. The defenders were not fools or villains. Large firms really were more efficient, and their owners really did give away fortunes for libraries, universities, and medical research. The critics were not jealous outsiders either. Henry Demarest Lloyd, who wrote the era's most famous attack, was a wealthy Chicago journalist arguing that combinations took wealth the whole community had helped to create. Tell students the reading question asks for two arguments on each side, so they should be collecting them as matched pairs: efficiency against secret rebates, cheap kerosene against prices raised after rivals died, philanthropy against the question of how the fortune was made. The exit ticket will force a verdict, but no verdict is worth anything until both cases have been heard at full strength.")

# ------------------------------------------------------ 12 · DEFENDERS
content_text('The case for bigness',
             ['Large firms were efficient',
              'They bought in bulk and ran the newest machinery around the clock',
              'Kerosene fell from a luxury to a household light',
              'Philanthropy: Carnegie paid for thousands of public libraries',
              'Rockefeller funded universities and medical research'],
             "Give the defenders their full case first. Large firms were efficient. They bought in bulk, ran the newest machinery around the clock, and cut waste that smaller firms carried. The result students can picture is kerosene. Once a luxury, it became cheap enough for working families to light their homes, in part because refining at scale cost less per gallon. A family reading by a cheap, bright lamp did not experience Standard Oil as an abstraction; it experienced it as light. Defenders also pointed to philanthropy. Carnegie, who wrote that the rich should use their fortunes for the public good, paid for thousands of public libraries. Rockefeller funded universities and medical research. Take the argument seriously before turning to the critics: if bigness lowered prices and built libraries, what exactly was the objection? The next slide is the objection, and it is about methods, not size alone.",
             kick='C · The argument over bigness', size=24)

# ------------------------------------------------------ 13 · CRITICS
content_photo('octopus-port.jpg', 'The case against it',
              ['Secret rebates from railroads cut Standard\u2019s shipping costs',
               'Prices cut in one town until local refiners failed',
               'Then prices raised, once competition was gone',
               'Farmers and merchants took the prices they were given',
               'Efficiency gains rarely reached workers\u2019 pay'],
              "The cartoon is 'Next!', drawn by Udo Keppler for Puck in 1904, more than twenty years after the trust was formed; it shows how the critics' image of Standard Oil hardened over time, an octopus gripping industry and government alike. Now the record behind the image. Standard Oil had won secret rebates from railroads, lowering its shipping costs below what rivals paid on the same line. It had cut prices in one town until local refiners failed, then raised them once competition was gone. A small competitor could not match a firm willing to lose money in one market while earning it in fifty others. Farmers and merchants complained that railroads and trusts together decided what their crops and goods were worth, and workers pointed out that efficiency gains rarely reached their pay. The writer Henry Demarest Lloyd argued in Wealth Against Commonwealth, in 1894, that combinations enriched a few owners by taking wealth the whole community had helped to create.",
              kick='C · The argument over bigness')

# ------------------------------------------------- 14 · SECTION D DIVIDER
divider_photo('spencer-port.jpg', 'Section D', 'Ideas That Defended the New Order',
              ['Two arguments that turned', 'a business practice into a philosophy'],
              "The photograph is Herbert Spencer in 1889, the English writer whose name anchors this section. Sections A to C described what the combinations did and how Americans argued about it. Section D goes one level deeper, to the ideas that told defenders they were not merely rich but right. Two ideas gave the defenders a philosophy, and students must keep them separate, because the exit ticket asks them to identify each one inside a single spoken sentence. The first concerns government: it should stay out. The second concerns people: wealth proves fitness. Warn students now about the most common error in this section. The second idea carries Darwin's name, but it was an argument about society made by Spencer and by the American professor William Graham Sumner. Charles Darwin's work concerned species in nature, and he did not teach a doctrine about railroads, wages, or poor relief.",
              title_size=38)

# ------------------------------------------------------ 15 · TWO IDEAS
content_text('Laissez-faire and Social Darwinism',
             ['Laissez-faire: government should not regulate business',
              'Markets correct themselves; regulation protects the inefficient',
              'Social Darwinism: wealth and power show natural fitness',
              'Spencer applied nature\u2019s competition to society',
              'Sumner popularized the argument in the United States',
              'Not Darwin: his work concerned species in nature'],
             "Define both ideas with precision, in the guided notes' own terms. The first was laissez-faire: the argument that government should not regulate business or the economy. Under this view, markets corrected themselves, regulation protected the inefficient, and a law against a successful company punished success itself. The second was Social Darwinism: the argument that wealth and power show natural fitness and that government aid distorts competition. The English writer Herbert Spencer applied ideas about competition in nature to human society, and the American professor William Graham Sumner popularized the argument in the United States. Be precise here, as the reading insists. Social Darwinism was an argument made by Spencer, Sumner, and their followers about society. It was not a doctrine taught by Charles Darwin, whose work concerned species in nature. Its defenders held that the owners of great fortunes had won a fair contest, and that helping those who lost would weaken the whole society.",
             kick='D · Ideas that defended the new order', size=24)

# ------------------------------------------------------ 16 · FAIR CONTEST
content_text('Was the contest fair?',
             ['Defenders: the winners won a fair contest',
              'Helping the losers would weaken the whole society',
              'Critics: one side received secret railroad rebates',
              'A rigged contest is not a test of fitness'],
             "End the section with the critics' reply, because it is the sharpest single sentence in the reading and it turns the defenders' strongest word against them. The defenders' claim rested on the word fair. If the owners of great fortunes had won a fair contest, then their wealth proved fitness, and government aid to the losers only distorted a natural result. Critics replied that a contest in which one side received secret railroad rebates was not a fair test of fitness at all. Make students see the structure of that answer. It does not reject the idea of a contest, or even of fitness. It attacks the evidence. A race tells you who is fastest only if both runners start at the same line, on the same track, under the same rules. Rebates moved the starting line. Once students grasp that, they can evaluate Social Darwinism as an argument rather than repeat it as a slogan, which is what the exit ticket will ask.",
             kick='D · Ideas that defended the new order', size=25)

# ------------------------------------------------- 17 · SECTION E DIVIDER
divider_photo('bosses-port.jpg', 'Section E', 'The Sherman Antitrust Act',
              ['Congress answers in 1890', 'The courts answer back for a decade'],
              "The cartoon is 'The Bosses of the Senate,' drawn by Joseph Keppler for Puck on January 23, 1889, one year before the law in this section. Giant money bags labeled for the steel, copper, oil, iron, and sugar trusts loom over small senators, and the entrance marked for the people is bolted shut. Keep that image in mind as the political setting for the Sherman Act. Congress was not acting in calm detachment; it was acting under public pressure, with cartoons like this one telling voters that the trusts already owned the Senate. The act Congress passed in 1890 was broad, angry, and vague, and Congress left its meaning to the courts. This section is the story of what the courts did with it. Students should track two facts for the reading question: how the Supreme Court treated a business combination, and how the same law was used against labor unions.",
              title_size=40)

# ------------------------------------------------------ 18 · THE ACT
content_text('A law against trusts, 1890',
             ['The Sherman Antitrust Act, 1890',
              'It banned combinations in restraint of trade',
              'Monopolizing an industry became a federal crime',
              'The language was broad',
              'Congress left the meaning to the courts'],
             "In 1890 Congress answered with the Sherman Antitrust Act: the 1890 federal law that banned combinations in restraint of trade. Read the act's two moves separately. First, it made it a federal crime to form a combination that restrained trade. Second, it made it a crime to monopolize an industry. On paper, that covered the trust exactly: the trustees of forty companies, setting one price, were a combination restraining trade if the words meant anything. But notice the weakness built into the law from the start. Its language was broad, and Congress left it to the courts to decide what the words meant in practice. Congress had named a target without defining it, in a country whose judges were largely sympathetic to the laissez-faire ideas from section D. A law is only as strong as the institution that interprets it. The next two slides show what interpretation did to this one during its first decade.",
             kick='E · The Sherman Antitrust Act', size=25)

# ------------------------------------------------------ 19 · 98 PERCENT STAT
stat('98 PERCENT', 'of sugar refining, held by a combination the Supreme Court refused to break up in 1895',
     'The Court ruled that manufacturing was not trade between the states, so the act did not reach it.',
     "Dwell on this number beside the 90 percent from section B, because together they measure the law's first decade. In 1895 the Supreme Court held that a sugar combination controlling about 98 percent of refining could not be broken up under the Sherman Act, because manufacturing was not trade between the states. Follow the logic with students. The sugar trust manufactured sugar. Manufacturing happened inside one state, at the refinery. Trade between the states began afterward, when the sugar shipped. So the combination that controlled nearly all American refining stood outside the act, even though its product crossed every state line in the country. A combination holding 98 percent was, if anything, a clearer monopoly than Standard Oil's 90. The law had been written against combinations in restraint of trade, and the Court had read the words narrowly until almost nothing was restrained. This is the first of the two facts the reading question requires.",
     kick='E · The Sherman Antitrust Act')

# ------------------------------------------------------ 20 · AGAINST UNIONS
content_text('A law used against unions',
             ['For its first decade, the act did little against big business',
              'Courts read it narrowly, case after case',
              'The same act was used against labor unions',
              'Strikes were treated as combinations restraining trade',
              'The trust question stayed open'],
             "The second fact is the bitter irony of the decade, and students should not miss it. In the same period when the act could not reach a sugar combination holding 98 percent of refining, the act was used against labor unions, whose strikes courts treated as combinations restraining trade. A strike, in this reading, was workers combining to stop work, and stopped work restrained trade. So the one combination the law reliably punished was the combination of working people, the group with the least power in the whole story. Step back and close the section. The trust question stayed open. Big business had plainly built much of modern America: its steel, its oil, its national markets. Whether it had also captured the country, its prices, its railroads, and its politics was the argument the next generation inherited, and it is the argument students now take up in the hearing simulation.",
             kick='E · The Sherman Antitrust Act', size=25)

# ------------------------------------------------------ 21 · VOCAB A
vocab('Words for control',
      [('trust', 'a combination of corporations that limits competition within an industry'),
       ('monopoly', 'control of an industry by one company or combination, with no effective competition'),
       ('vertical integration', 'control by one company of every stage in making and selling a product'),
       ('horizontal integration', 'control by one company of many firms at the same stage of an industry')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. A trust is a combination of corporations that limits competition within an industry: the device of 1882, in which stockholders handed their shares to trustees. A monopoly is control of an industry by one company or combination, with no effective competition: the end point, measured in this lesson at 90 percent of oil refining and 98 percent of sugar refining. Vertical integration is control by one company of every stage in making and selling a product, Carnegie's road through mines, transport, furnaces, and mills. Horizontal integration is control by one company of many firms at the same stage of an industry, Rockefeller's road through rival refiners. The paired memory hook is simple: vertical goes up and down the chain of production, horizontal goes across the row of competitors.")

# ------------------------------------------------------ 22 · VOCAB B
vocab('Words for the argument and the law',
      [('laissez-faire', 'the argument that government should not regulate business or the economy'),
       ('Social Darwinism', 'the argument that wealth and power show natural fitness and that government aid distorts competition'),
       ('Sherman Antitrust Act', 'the 1890 federal law that banned combinations in restraint of trade')],
      "Three more terms, again matching the guided notes exactly. Laissez-faire is the argument that government should not regulate business or the economy: the hands-off principle that told Congress to leave the combinations alone. Social Darwinism is the argument that wealth and power show natural fitness and that government aid distorts competition: the philosophy of Spencer and Sumner, which students must not attribute to Charles Darwin himself. The Sherman Antitrust Act is the 1890 federal law that banned combinations in restraint of trade: the country's first legal answer, weakened in its first decade by narrow court rulings and used instead against labor unions. Notice how the three terms form the lesson's triangle. Two ideas defended bigness, and one law opposed it, and for ten years the ideas were stronger than the law. Students who can state all three definitions cold are ready for the organizers chart and the exit ticket.")

# ------------------------------------------------------ 23 · ORGANIZERS
content_text('Two organizers at a glance',
             ['Carnegie, steel: vertical integration',
              'Owned mines, transport, furnaces, and mills',
              'Result: costs below rivals, control of steel production',
              'Rockefeller, oil: horizontal integration and the trust',
              'Combined rival refiners under trustees',
              'Result: about 90 percent of refining, and the power to set prices'],
             "Use this slide to fill in the organizers chart at the end of the guided notes, row by row, and make students say the contrasts aloud. Andrew Carnegie, in steel, used vertical integration, owning mines, transport, furnaces, and mills; the result was costs below rivals and control of steel production. John D. Rockefeller, in oil, used horizontal integration and the trust, combining rival refiners under trustees; the result was control of about 90 percent of oil refining at its peak and the power to set prices. The chart looks simple, and that is its use: it is the fastest revision tool in the lesson. But press one level deeper before moving on. Carnegie's control rested on cost; rivals could survive, they just could not match his price and live. Rockefeller's control rested on combination; rivals inside the trust stopped being rivals at all. Two different kinds of power, one industry each, and one lesson question covers both.",
             kick='Two organizers at a glance', size=24)

# ------------------------------------------------------ 24 · CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Big Business on Trial', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Return to the lesson question: did big business build modern America, capture it, or do both at once? The hearing is where you argue it.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Trust Hearing: prepare a witness, testify before the committee'),
        ('Notebook', 'Weigh the two cases, defenders and critics, side by side'),
        ('Quick check', 'Integration, the trust, and the Sherman Act'),
        ('Writing', 'Make your claim: built, captured, or both, with two facts')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.5, 0.6, d, size=19, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.8, 11.5, 0.5, 'Exit ticket: define trust and monopoly, name the two defending ideas, and answer the lesson question with one fact.',
     size=16, color=POWDER)
notes(s, "Close by handing the lesson to its work. The activity is The Trust Hearing: Big Business on Trial, 1890. Each group takes one witness card, prepares that witness from the evidence in today's lesson, and testifies before a Senate hearing committee deciding how to use the new Sherman Act. Stress that witnesses must argue from the record: rebates, prices, libraries, percentages. The notebook page then asks students to weigh the defenders' case and the critics' case side by side in writing. The quick check covers the mechanics: the two kinds of integration, the trust device, and the Sherman Act and its weak first decade. Finally the writing task returns to the lesson question, defended with two facts from the reading. Next lesson, organized labor answers bigness with a combination of its own.")

dc.save(OUT)
