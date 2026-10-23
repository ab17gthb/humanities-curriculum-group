#!/usr/bin/env python3
"""The Twenties Lesson 4 deck, "The Politics of Prosperity," built to the approved
Progressive Era pilot system: image-led slides, fragments only on screen,
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
OUT = os.path.join(HERE, '..', 'lesson-04-slides.pptx')

def vocab(title, terms, note, kick='The vocabulary', row_gap=1.52, dfn_size=19):
    s = slide(CREAM)
    kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95, 11.5, 1.0, title, size=30, color=NAVY, font='Georgia')
    yy = 2.1
    for term, dfn in terms:
        text(s, 0.9, yy, 4.1, 0.9, term, size=25, color=NAVY, font='Georgia')
        text(s, 5.15, yy + 0.06, 7.3, 1.1, dfn, size=dfn_size, color=MUTED, leading=1.2)
        yy += row_gap
    notes(s, note)
    return s

# ---------------------------------------------------------------- 1 · TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'THE TWENTIES · LESSON 4', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Politics of Prosperity', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'What three Republican governments did, and what they refused to do', size=17, color=POWDER)
notes(s, "The photograph shows the Washington Conference in session at Memorial Continental Hall in Washington, D.C., in a Keystone View Company stereograph dated November 21, 1921. Delegates of nine nations sit at tables arranged in a square while the galleries watch. One disclosure: the original is a stereograph card with two near identical frames, and this slide uses one frame only. Open the lesson with the puzzle this image poses. In the 1920s the United States would host the largest diplomatic gathering of the decade, cut taxes, raise tariffs, and sign a pact renouncing war, yet it refused to join the League of Nations and promised to enforce nothing. Doing and refusing are both policy. This lesson tracks both sides of that record, at home and abroad, through three Republican administrations.")

# ------------------------------------------------- 2 · LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('What did the Republican governments of the 1920s do at home and abroad, and what did they deliberately leave undone?', {})]],
     size=40, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the prosperity of the 1920s change American life, and why was that prosperity weaker than it looked?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Read the lesson question slowly, because its second half does the real work. Students can list what these governments did: cut taxes, raised the tariff, limited navies, signed a peace pact. The harder half asks what they deliberately left undone, and the word deliberately carries the weight. The refusals in this lesson were not oversights or failures to get around to things. Coolidge vetoed farm price support twice. Senators refused the League of Nations and the World Court on stated grounds. The administration insisted on war debts while blocking the trade that could have paid them. Each refusal was a decision, defended at the time as principle. Hold students to that standard at the exit ticket: a strong answer names actions and refusals side by side, with facts for each, instead of treating the decade as a government that simply did nothing.")

# --------------------------------------------------- 3 · THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.15, 11.5, 1.0, 'Action and refusal, at home and abroad', size=38, color=CREAM, font='Georgia')
rule(s, 0.92, 2.05)
rows = [('A', 'Normalcy takes office', 'Harding, strong appointments, and the Ohio Gang'),
        ('B', 'Teapot Dome', 'Secret oil leases, cash and gifts, prison for a cabinet secretary'),
        ('C', 'Coolidge and the business doctrine', 'Tax lightly, spend less, leave business to business'),
        ('D', 'Mellon and the tax cuts', 'The top rate falls from 73 percent to 25 percent'),
        ('E', 'The tariff', 'Duties rise, and the war debt contradiction follows'),
        ('F', 'The Washington Conference', 'Battle fleets fixed at 5 to 5 to 3'),
        ('G', 'War debts and the circle of loans', 'American credit keeps the payments turning'),
        ('H', 'A pact against war, and 1928', 'War renounced, nothing enforced, Hoover elected')]
yy = 2.38
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.55, n, size=20, color=RUST_LT, font='Georgia')
    text(s, 1.55, yy + 0.02, 4.9, 0.55, t, size=18, color=CREAM, bold=True)
    text(s, 6.6, yy + 0.05, 5.9, 0.55, d, size=15, color=POWDER)
    yy += 0.60
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Sections A through E are the home record: a president who trusted the wrong friends, the scandal that followed, a doctrine of limited government, tax cuts, and a high tariff. Sections F through H are the record abroad: naval limits agreed at Washington, war debts collected through a circle of American loans, and a pact that renounced war while providing nothing to stop one. Tell students the final table in their guided notes, The Record at a Glance, has two columns for a reason. One column asks what the government did. The other asks what it left undone or refused. By the end of the hour they should be able to fill both columns from memory.")

# ------------------------------------------------- 4 · SECTION A DIVIDER
divider_photo('harding-port.jpg', 'Section A', 'Normalcy Takes Office',
              ['A promise to end war and reform politics', 'and return to normalcy'],
              "The portrait is Warren G. Harding photographed by Harris and Ewing, dated circa 1920, the year he won the presidency; say circa plainly, because the photograph may date from just before his term began. Harding won the election of 1920 promising a return to normalcy after war and reform, a word students should hear as a program, not a mood. The country had been through a world war, a pandemic, strikes, and a reform era, and Harding offered quiet: lower spending, lower taxes, and government that interfered less. He took office in March 1921 and cut wartime spending. What decided the character of his administration was not the program but the people. Section A covers his two kinds of appointments, and the difference between them explains almost everything that follows in this lesson, including its largest scandal.",
              title_size=40)

# ------------------------------------------------------ 5 · TWO KINDS OF APPOINTMENTS
content_text('Two kinds of appointments',
             ['Excellent: Hughes at State, Mellon at the Treasury, Hoover at Commerce',
              'Friends from Ohio, valued for loyalty over honesty',
              'The Ohio Gang: public office as a route to private profit',
              'Harding took no bribe, and asked no hard questions'],
             "Name the strong appointments first, because students should not leave thinking this administration was simply corrupt. Charles Evans Hughes at State, Andrew W. Mellon at the Treasury, and Herbert Hoover at Commerce were able men, and two of them anchor later sections of this lesson: Mellon directs tax policy through all three Republican presidencies, and Hoover ends the lesson as president elect. Then set the second kind beside them. Harding also appointed friends from Ohio whose loyalty he valued over honesty. These friends, the Ohio Gang, treated public office as a route to private profit. The guided notes ask students for the gang by name and for Mellon at the Treasury, so check both blanks. Close on the precise judgment the reading makes. Harding was never shown to have taken a bribe. He never asked hard questions of the men he trusted. Corruption grew in that inattention, not in orders from the president.",
             kick='A · Normalcy takes office')

# ------------------------------------------------- 6 · SECTION B DIVIDER
divider_photo('teapot-port.jpg', 'Section B', 'Teapot Dome',
              ['Oil reserved for a naval emergency', 'leased in secret, for cash'],
              "The image is a center crop of Bargain Day in Washington, a cartoon by Ellison Hoover published in Life magazine in 1924. In the full cartoon the Washington Monument and the White House carry Sold signs and are being hauled away, and sale bills offer honor and ethics as remnants practically given away. That is how the public judged this scandal once the facts came out, and students meet the same cartoon in the activity. Use it to set the stakes before the details. No foreign enemy and no election produced this damage. A cabinet secretary leased public oil land to private companies and took their money, and the president who appointed him had built an administration in which nobody asked hard questions. Section B covers the leases, the payments, the Senate investigation, and the prison sentence that followed.",
              title_size=48)

# ------------------------------------------------------ 7 · LEASES IN SECRET
content_photo('coolidge-port.jpg', 'Leases in secret, money in return',
              ['Navy oil reserves: Teapot Dome, Wyoming, and Elk Hills, California',
               '1921: the reserves pass to Secretary of the Interior Albert B. Fall',
               'Secret leases to Sinclair and to Doheny, without competitive bidding',
               '$100,000 in cash from Doheny; large loans and gifts from Sinclair'],
              "The photograph is President Calvin Coolidge, photographed by Harris and Ewing about 1924; Coolidge inherited this scandal, and his portrait belongs here because the exposure unfolded on his watch. First, what the reserves were. The Navy held oil bearing land at Teapot Dome, Wyoming, and Elk Hills, California, as a reserve for emergencies, oil kept in the ground against a future war. In 1921 the reserves passed to Secretary of the Interior Albert B. Fall, a Harding friend. Fall secretly leased Teapot Dome to Harry F. Sinclair's company and Elk Hills to Edward L. Doheny's, without the competitive bidding the law expected. In return he took $100,000 in cash from Doheny and large loans and gifts from Sinclair. The exit ticket asks what made the leases corrupt rather than merely unwise, and the answer is exactly these two features: secrecy without bidding, and payment to the official who granted them.",
              kick='B · Teapot Dome', )

# ------------------------------------------------------ 8 · EXPOSURE AND PRISON
content_text('Exposure, resignation, prison',
             ['A Senate investigation, led by Thomas J. Walsh of Montana',
              'The leases exposed in 1923 and 1924',
              'Fall resigned',
              '1929: the first cabinet officer imprisoned for a crime in office',
              'Harding died in August 1923; the scandal kept his name'],
             "Follow the consequences in order, because the sequence is the accountability story. A Senate investigation led by Thomas J. Walsh of Montana exposed the leases in 1923 and 1924. Fall resigned. Then the legal ending, which the guided notes test directly: in 1929 Fall became the first cabinet officer imprisoned for a crime committed in office. No cabinet secretary before him had gone to prison for official corruption, and students should register how new that was. Place Harding in the timeline accurately. He died in August 1923, before the worst of the exposure, and he was never shown to have taken a bribe himself. But the scandal attached to his memory and to his party, because the men who profited were his appointments and his inattention had sheltered them. In the vocabulary of this lesson, the whole affair is Teapot Dome, the first of the seven key terms students will review at the end of the deck.",
             kick='B · Teapot Dome')

# ------------------------------------------------- 9 · SECTION C DIVIDER
divider_photo('coolidge-port.jpg', 'Section C', 'Coolidge and the Business Doctrine',
              ['The government does a short list well', 'and stays out of the way'],
              "This is the same Coolidge portrait used earlier, by Harris and Ewing about 1924, and repeating it is deliberate: the man who cleaned up after Harding is the subject now. Vice President Calvin Coolidge succeeded Harding in 1923 and won a term of his own in 1924. Where Harding's administration was defined by the men around him, Coolidge had a doctrine, and students should be able to state it as a list. The federal government should do a short list of things well: tax lightly, spend less than it collected, pay down the war debt, and leave business decisions to business. Section C states that doctrine and then tests it against the one group it refused to help, the farmers, because a doctrine is clearest at the point where it says no.",
              title_size=36)

# ------------------------------------------------------ 10 · THE BUSINESS DOCTRINE
content_text('The business doctrine',
             ['Tax lightly; spend less than the government collects',
              'Pay down the war debt',
              'Regulation stayed light',
              'Twice vetoed: bills to support farm prices',
              'The test of policy: rising prosperity'],
             "Walk the doctrine as Coolidge himself would have listed it. Tax lightly. Spend less than the government collected, which meant budgets that ran surpluses. Pay down the war debt. Leave business decisions to business, which meant regulation stayed light. The guided notes reduce this to three blanks students must fill: tax lightly, business decisions, and vetoed, so pause on each. Then the refusal, stated twice so no one can call it an accident. Coolidge twice vetoed bills that would have committed the government to supporting farm prices. Farmers were struggling through the whole decade, and the doctrine still said no, because supporting prices meant the government deciding what crops were worth. Close with Coolidge's own test of the policy. For Coolidge, rising prosperity was the test. If business was expanding and budgets were balanced, government was doing its work by staying out of the way. Ask students to hold that test in mind for the last lesson of the unit, which asks why the prosperity was weaker than it looked.",
             kick='C · Coolidge and the business doctrine')

# ------------------------------------------------- 11 · SECTION D DIVIDER
divider_text('Section D', 'Mellon and the Tax Cuts',
             'The Treasury secretary under all three Republican presidents.',
             "Andrew W. Mellon directed tax policy under all three Republican presidents, Harding, Coolidge, and Hoover, which makes him the most continuous figure in this lesson. Presidents changed; the tax policy did not. Mellon was a Pittsburgh banker, one of the richest men in the country, and he brought a banker's argument to the Treasury: the wartime tax law, in his view, was defeating itself. This section states that argument fairly before it states the criticism, and students should be able to give both sides in the exit work and the quick check. The facts are few and exact. A wartime top rate of 73 percent. An argument about tax exempt bonds. Three cuts, in 1921, 1924, and 1926. A top rate of 25 percent by mid decade. Budget surpluses. And a criticism that never went away.")

# ------------------------------------------------------ 12 · MELLON'S ARGUMENT
content_text("Mellon's argument",
             ['Wartime law: as much as 73 percent at the highest bracket',
              'High rates push the wealthy into tax exempt bonds',
              'Sheltered money builds no factories and pays no tax',
              'Lower rates put capital to work, and the Treasury still collects',
              'Congress cut rates in 1921, 1924, and 1926'],
             "State Mellon's argument in his own logic before judging it, because the reading question and the quick check both ask students to reproduce it accurately. Wartime law had taken as much as 73 percent of income at the highest bracket. Mellon argued that rates that high pushed wealthy investors to shelter money in tax exempt bonds instead of putting it into factories and railroads, so the Treasury collected less, not more. Money parked in those bonds built nothing and paid no tax. Cut the rate, and the same investors would move capital into productive business, where its profits could be taxed at the lower rate. Congress followed the argument in stages, cutting rates in 1921, 1924, and 1926. In the vocabulary of this lesson, each step was a tax cut, a reduction in the rates at which a tax is charged. The next slide puts the result in one number.",
             kick='D · Mellon and the tax cuts')

# ------------------------------------------------------ 13 · TAX STAT
stat('25%', 'the top income tax rate by mid decade',
     'Down from a wartime top rate of 73 percent, in cuts passed in 1921, 1924, and 1926. Budgets ran surpluses.',
     "Dwell on the two numbers, both from the reading, because together they measure what this government most wanted to do. The wartime top rate had reached 73 percent. After the cuts of 1921, 1924, and 1926, the top rate stood at 25 percent. That is a fall of forty eight points, and it was the centerpiece of Republican domestic policy: the state taking a much smaller share of the largest incomes. Pair the figure with its two companions from the reading. Budgets ran surpluses, which Mellon counted as proof the policy worked. And the criticism, which students must be able to state as readily as the argument: critics answered that the cuts gave most of their benefit to the wealthy, while farmers and wage earners saw little change. The guided notes test the two rates directly, seventy three and twenty five, so make sure both numbers land before moving on.",
     kick='D · Mellon and the tax cuts')

# ------------------------------------------------- 14 · SECTION E DIVIDER
divider_photo('capitol-port.jpg', 'Section E', 'The Tariff',
              ['Taxes cut at home', 'raised at the border'],
              "The photograph shows the United States Capitol from the air in November 1924, photographed by the National Photo Company, with the Navy airship USS Los Angeles crossing in front of it. The Capitol is the right emblem for this section because the tariff was Congress's work, not a president's. Set up the contradiction in the section title before the details. The same governments that cut taxes at home raised them at the border. A tariff is a tax; it is simply charged on goods brought into the country rather than on income earned inside it. So the Republican record is not low taxes in general. It is low taxes on income, especially high income, and high taxes on imports. Section E names the law, states whom it protected, and then follows the money across the Atlantic to the problem the administration never solved.",
              title_size=48)

# ------------------------------------------------------ 15 · HIGH DUTIES
content_text('High duties, and a contradiction',
             ['The Fordney-McCumber Tariff of 1922',
              'Duties on farm products and manufactured goods',
              'Some of the highest levels in American history',
              'American producers shielded from foreign competition',
              'Europe left short of the dollars its debts required'],
             "Give the law its full name and date, because the guided notes test both: the Fordney-McCumber Tariff of 1922. It raised duties on farm products and manufactured goods to some of the highest levels in American history, shielding American producers from foreign competition. The tariff pleased the industries it protected, and students should say plainly who gained: American manufacturers and farmers selling in the home market. Then turn to the contradiction, which is the analytical heart of the section and one of the reading questions. The Allies owed the United States about ten billion dollars in war debts, and Washington insisted the debts be paid. But Europeans earned dollars by selling goods in the United States, and the tariff made that harder. The administration demanded payment while closing the market through which payment could be earned, a contradiction the administration never resolved. Section G returns to those debts directly.",
             kick='E · The tariff')

# ------------------------------------------------- 16 · SECTION F DIVIDER
divider_photo('washington-port.jpg', 'Section F', 'The Washington Conference',
              ['Out of the League of Nations', 'at the head of the table in Washington'],
              "The photograph is a portrait crop from the same 1921 stereograph of the conference in session that opened the deck, with delegates seated around the square of tables in Memorial Continental Hall. Abroad, Republican policy is often called isolationism, but the label fits only in part, and this section is the evidence. The United States refused to join the League of Nations, yet in November 1921 it led the decade's largest diplomatic gathering in its own capital. In the vocabulary of this lesson, isolationism means avoiding political commitments and alliances while keeping a country free to act on its own, and students will get that definition in full on the vocabulary slides. The Washington Conference fits the definition precisely: agreements negotiated by the United States itself, limited in scope, with no standing obligation to anyone.",
              title_size=36)

# ------------------------------------------------------ 17 · HUGHES OPENS
content_text('Hughes opens, fleets are fixed',
             ['November 1921: Secretary Hughes proposes a stop to battleship building',
              'The Five-Power Treaty of 1922',
              'Battle fleets fixed at 5 to 5 to 3: the United States, Britain, Japan',
              'New battleship construction paused for ten years',
              'Warships scrapped; Pacific possessions and China trade pledged'],
             "Secretary of State Charles Evans Hughes opened the Washington Conference in November 1921 by proposing that the naval powers stop building battleships, and the proposal became the Five-Power Treaty of 1922. Give students its three working parts, all tested in the guided notes. It fixed the battle fleets of the United States, Britain, and Japan in a ratio of 5 to 5 to 3. It paused new battleship construction for ten years. And it ordered warships scrapped, ships already built sent to be broken up. Companion treaties pledged respect for Pacific possessions and open trade with China. Name what kind of event this was, because it complicates the decade's reputation. The United States had called the powers together, proposed the boldest terms in the room, and gotten them accepted. On naval arms, this government acted abroad with more ambition than any other government of the decade, and it did so entirely outside the League of Nations.",
             kick='F · The Washington Conference')

# ------------------------------------------------------ 18 · WHY THE SENATE COULD SAY YES
content_text('Why the Senate could say yes',
             ['The treaties limited arms without joining the League',
              'Limited, specific agreements, negotiated by the United States itself',
              'No standing obligation to act in a future crisis',
              'The pattern for the decade: agree, but promise nothing in advance'],
             "This slide answers the second half of the reading's fourth question, and it is the key to the whole foreign policy of the decade. The Senate approved the Washington agreements because they limited arms without joining the League of Nations. Draw the distinction exactly. These were limited, specific treaties, negotiated by the United States itself, about named ships and named ratios. They carried no standing obligation to act if trouble came. League membership, as senators saw it, was the opposite: a promise made in advance to respond to crises nobody could foresee, in places most Americans could not find. So the same Senate that refused the League could scrap battleships by treaty. Tell students to keep the pattern sentence from the reading in view for the rest of the lesson: sign agreements, lend money, and sell goods abroad, but promise nothing in advance. The war debts and the peace pact both follow it.",
             kick='F · The Washington Conference')

# ------------------------------------------------- 19 · SECTION G DIVIDER
divider_text('Section G', 'War Debts and the Circle of Loans',
             'Ten billion dollars owed, and a circle that turned only while American credit flowed.',
             "Money tied the United States to Europe even where politics did not, and this section follows the money. Start with the fixed fact. The Allies owed the United States about ten billion dollars borrowed during the war, and Washington insisted the debts be paid in full. The Allies answered that they could pay only what Germany paid them in reparations, and Germany could not pay at that scale out of its own economy. Three claims, each pointing at the next, and no obvious way for the circle to close. The Dawes Plan of 1924 closed it with American credit. Section G lays out the circle step by step, because the guided notes ask students to number its three steps in order, and then asks the question students should ask of every arrangement in this lesson: what happens when the flow that keeps it turning stops?")

# ------------------------------------------------------ 20 · THE CIRCLE
content_text('Ten billion dollars, and a circle',
             ['The Allies owed about ten billion dollars',
              'Washington insisted the debts be paid',
              'Step 1: American banks lend money to Germany',
              'Step 2: Germany pays reparations to the Allies',
              'Step 3: the Allies pay their debts to the United States',
              'The circle turned while American credit flowed'],
             "Work the circle slowly; the guided notes ask students to number its three steps, and the order is the whole mechanism. The Dawes Plan of 1924 loosened the knot this way. American banks lent money to Germany. Germany paid reparations to the Allies. The Allies paid their debts to the United States. Round and round, and on paper everyone was paying everyone. Now name the weakness, which the reading states in one conditional sentence: the circle turned while American credit flowed, and if American lending stopped, every payment in the circle stood at risk. Connect it back to section E. The tariff had already cut off the honest way for Europe to earn dollars, through trade. So the debts were serviced by new American loans instead, an arrangement that worked only so long as Americans kept lending. In the vocabulary of this lesson, the ten billion is war debt, money one government owes another for wartime loans.",
             kick='G · War debts and the circle of loans', size=24)

# ------------------------------------------------- 21 · SECTION H DIVIDER
divider_photo('kellogg-port.jpg', 'Section H', 'A Pact Against War, and the Election of 1928',
              ['War renounced in Paris', 'and a third Republican victory at home'],
              "The photograph shows German foreign minister Gustav Stresemann signing the Kellogg-Briand Pact at the French Foreign Ministry in Paris on August 27, 1928, from the Nationaal Archief, the Dutch National Archives. Two disclosures belong here. The Commons original is small, so this crop prints softer than the other images in the deck. And it shows the German signer, not an American; the pact was an act of fifteen governments, which is the point. Section H pairs the decade's grandest promise with its clearest refusal. Fifteen nations renounced war, and the pact gave no one any power to stop one. The same section closes the lesson at home, with the election of 1928, where the politics of prosperity won a third straight national victory.",
              title_size=30)

# ------------------------------------------------------ 22 · RENUNCING WAR
content_text('Renouncing war, with nothing behind it',
             ['Paris, August 1928: fifteen nations sign the Kellogg-Briand Pact',
              'War renounced as an instrument of national policy',
              'All disputes to be settled by pacific means only',
              'No army, no court, no penalty for breaking it'],
             "Quote the pact itself here, in the text as printed in the League of Nations Treaty Series, volume 94, which is the text students read in the lesson activity. Article I declares that the signing nations condemn recourse to war for the solution of international controversies and renounce it as an instrument of national policy in their relations with one another. Article II promises that the settlement of all disputes shall never be sought except by pacific means. As promises, those sentences are total. Now set beside them what the pact did not contain, because the guided notes test the gap directly. The pact created no army, no court, and no penalty for breaking it. Nobody was empowered to judge a breach, punish one, or stop a war. In the vocabulary of this lesson, the Kellogg-Briand Pact is the agreement signed in Paris in 1928 in which the signing nations renounced war as an instrument of national policy. Students should be able to hold both halves at once: the promise was real, and so was the emptiness behind it.",
             kick='H · A pact against war')

# ------------------------------------------------------ 23 · 85 TO 1
content_photo('kellogg-ratify-port.jpg', '85 to 1, and the doors left closed',
              ['The Senate approved the pact 85 to 1',
               'Stated: no limit on self-defense, no duty to enforce',
               'The World Court: kept out on the same terms',
               'The pattern held to the end of the decade'],
              "The photograph shows President Coolidge signing the document of ratification of the Kellogg treaty in the East Room of the White House in 1929, photographed by Harris and Ewing; note that this is the American ratification, not the Paris ceremony on the previous slides. The Senate approved the pact 85 to 1, a near unanimous vote, after stating that it did not limit self-defense and did not require the United States to enforce it. Those two statements are not footnotes. They are the conditions that made the vote possible, and the quick check asks students to explain why they fit the foreign policy pattern of the decade. The same caution kept the United States out of the World Court, which senators would join only on reservations no president accepted. So the decade ends as it began. Agreements signed, money lent, goods sold, and nothing promised in advance. The refusal was not drift. It was the policy.",
              kick='H · A pact against war')

# ------------------------------------------------------ 24 · HOOVER AND 1928
content_photo('hoover-port.jpg', 'Hoover and the election of 1928',
              ['Herbert Hoover: Commerce secretary, then the nominee',
               'Associational cooperation: trade groups setting standards, light guidance',
               'Al Smith of New York: the first Roman Catholic major party nominee',
               'Smith opposed Prohibition and spoke for the immigrant city',
               'A Hoover landslide, carrying even parts of the Democratic South'],
              "The portrait is Herbert Hoover photographed by Underwood and Underwood in 1928, the year he ran. As Secretary of Commerce, Hoover had spent the decade encouraging trade associations to set standards and share information under light guidance, a method called associational cooperation, which fit the doctrine of this lesson exactly: organization without compulsion. In 1928 he faced Governor Al Smith of New York, the first Roman Catholic nominated for president by a major party. Smith opposed Prohibition and spoke for the immigrant city. Hoover won in a landslide, carrying even states of the normally Democratic South where many Protestant voters refused a Catholic candidate, a fact students should record without flinching, because it is part of how the victory was assembled. The result closed the lesson's arc: low taxes, high tariffs, and limited government had won a third straight national victory, in 1920, 1924, and now 1928.",
              kick='H · The election of 1928', )

# ------------------------------------------------------ 25 · THE RECORD AT A GLANCE
s = slide(NAVY)
kicker(s, 'The record at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Did, and deliberately did not', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Taxes and spending', 'Top rate cut from 73 to 25 percent; surpluses', 'No farm relief, no new federal programs'),
        ('Business and farms', 'The 1922 tariff; regulation stayed light', 'Farm price support refused, vetoed twice'),
        ('Foreign agreements', 'Washington treaties; the Kellogg-Briand Pact', 'No League, no World Court, no enforcement'),
        ('Money across the Atlantic', 'Debts insisted on; the Dawes circle accepted', 'No debt cancellation, no lower tariff')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=21, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, The Record at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. Read it down the two columns rather than across. The did column: the top income tax rate cut from 73 percent to 25 percent with budget surpluses, the Fordney-McCumber Tariff of 1922 with regulation kept light, the Washington Conference treaties and the Kellogg-Briand Pact, and the war debts insisted on through the Dawes Plan circle. The refused column is just as full: no farm relief and no new federal programs, farm price support vetoed twice, no League of Nations membership, no World Court, no enforcement behind the pact, no cancellation of the debts, and no lower tariff so debtors could earn dollars. Grade the table strictly on the pairing: each row needs one action and one refusal.")

# ------------------------------------------------------ 26 · VOCAB A
vocab('Words for the record at home',
      [('Teapot Dome', 'the scandal in which Secretary of the Interior Albert B. Fall secretly leased federal naval oil reserves in Wyoming and California to private oil companies and accepted money from the oilmen in return; Fall was convicted and imprisoned'),
       ('tax cut', 'a reduction in the rates at which a tax is charged, here the cuts in federal income tax rates during the 1920s'),
       ('tariff', 'a tax charged on goods brought into a country from abroad')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. Teapot Dome: the scandal in which Secretary of the Interior Albert B. Fall secretly leased federal naval oil reserves in Wyoming and California to private oil companies and accepted money from the oilmen in return; Fall was convicted and imprisoned. Every clause of that definition carries a fact from section B: secret leases, federal reserves, two states, money in return, prison. A tax cut: a reduction in the rates at which a tax is charged, here the cuts in federal income tax rates during the 1920s. Note the definition is about rates, not amounts collected; Mellon argued the Treasury could collect as much at lower rates. A tariff: a tax charged on goods brought into a country from abroad. Students who call the tariff a ban or a limit should be corrected; it is a tax, and its price is paid inside the country that charges it.", row_gap=1.72, dfn_size=17)

# ------------------------------------------------------ 27 · VOCAB B
vocab('Words for the record abroad',
      [('isolationism', 'a policy of avoiding political commitments and alliances with other countries while keeping a country free to act on its own'),
       ('Washington Conference', 'the conference held in Washington, D.C., from November 1921 to February 1922, where the major naval powers agreed to limit the size of their battle fleets'),
       ('war debt', 'money one government owes another for wartime loans, here the debts the Allied governments owed the United States from the First World War'),
       ('Kellogg-Briand Pact', 'the agreement signed in Paris in 1928 in which the signing nations renounced war as an instrument of national policy')],
      "Four more terms, again matching the guided notes exactly. Isolationism: a policy of avoiding political commitments and alliances with other countries while keeping a country free to act on its own. Freedom to act on its own is the load bearing phrase; the policy was about preserving choice, not about ignoring the world, as the Washington Conference proves. Washington Conference: the conference held in Washington, D.C., from November 1921 to February 1922, where the major naval powers agreed to limit the size of their battle fleets. War debt: money one government owes another for wartime loans, here the debts the Allied governments owed the United States from the First World War. Kellogg-Briand Pact: the agreement signed in Paris in 1928 in which the signing nations renounced war as an instrument of national policy. Renounced is the precise verb, and students should pair it with what the pact lacked: any penalty, court, or force behind the renunciation.")

# ------------------------------------------------------ 28 · CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['What did the Republican governments of the 1920s do at home and abroad, and what did they deliberately leave undone? Answer with both halves.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Business of Government: staff a decision desk, then judge the real record'),
        ('Notebook', 'Notebook page: the politics of prosperity in your own words'),
        ('Quick check', 'Signing Away War: the pact, the leases, and the tax argument'),
        ('Writing', 'Done and Deliberately Undone: the lesson question as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: what made the leases corrupt, two acts and two refusals abroad, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Business of Government, staffs five decision desks, oil leases, tax policy, the tariff, the naval conference, and the peace pact, and then asks students to compare their decisions with what the administrations actually did. Desks whose decisions differ from the record have to judge which choice better served the country, from the documents. The notebook page restates the record in the student's own words. The quick check, Signing Away War, tests the pact, the Teapot Dome leases, and Mellon's tax argument together. The writing task, Done and Deliberately Undone, turns the lesson question into an essay. The exit ticket has three parts: what made the leases corrupt rather than merely unwise, two things done abroad and two commitments refused, and the lesson question answered in two or three sentences with at least two facts. Next lesson takes up the consumer economy this politics protected.")

dc.save(OUT)
