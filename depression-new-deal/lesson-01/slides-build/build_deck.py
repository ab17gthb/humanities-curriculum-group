#!/usr/bin/env python3
"""Depression and New Deal Lesson 1 deck, "The Human Cost of the Depression,"
built to the approved Twenties system: image-led slides, fragments only on
screen, comprehensive speaker notes, full lesson + vocabulary coverage.
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
text(s, 0.9, 5.32, 11.5, 0.4, 'THE DEPRESSION AND NEW DEAL · LESSON 1', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Human Cost of the Depression', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'How deep the collapse cut, and how families lived through it', size=17, color=POWDER)
notes(s, "The photograph shows a dust storm approaching Spearman, Texas, on April 14, 1935, from the National Archives and NOAA photo collections. It opens a unit that begins with the Depression already under way. The Twenties unit closed with the crash of 1929, and this unit takes up what the crash became: not a bad season on the stock market but a decade of collapse in banks, factories, farms, and family budgets. Today's lesson measures that collapse and then follows it into homes. Students will work with figures first, because the figures are the argument. Production cut nearly in half, about one worker in four out of work, and about nine thousand banks gone are not background color. They are the evidence the whole unit rests on, and the exit ticket will ask students to use them.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How deep did the Depression cut, and how did ordinary families live through it?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the New Deal change the relationship between Americans and their federal government, and what did it leave undone?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question has two halves, and students should hear both. The first half asks for depth, which means numbers stated accurately and labeled honestly as estimates where the record is an estimate. The second half asks how families lived through it, which means the human record: breadlines, evictions, doubled up households, freight trains, and migration west. The unit question runs beneath it as the frame for the whole unit. Notice that today's lesson does not yet answer the unit question. It builds the problem the New Deal was invented to answer. By the end of the hour students should be able to pose the closing question of the reading in their own words: whether a collapse this size was a private misfortune to be waited out, or a public emergency the government had a duty to answer. The next lessons take up the men who had to answer it.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'A collapse, measured and lived', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The collapse in numbers', 'Production nearly halved, one worker in four out'),
        ('B', 'Bank failures and deflation', 'Runs, lost savings, debts growing heavier'),
        ('C', 'Breadlines and charity', 'Free food, and funds running out'),
        ('D', 'Hoovervilles and eviction', 'Scrap shacks on land families did not own'),
        ('E', 'Family strain', 'Doubled up, postponed, riding the freights'),
        ('F', 'The Dust Bowl', 'Drought, dust storms, and Route 66 west'),
        ('G', 'Private or public', 'The question the whole unit answers')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Sections A and B give the collapse in its economic form: falling production and mass unemployment, then bank failures and deflation working together. Sections C, D, and E follow the collapse into daily life: the breadline, the eviction and the Hooverville, and the rearranged family. Section F moves to the southern Plains, where drought turned an economic collapse into an ecological one and sent families west. Section G closes the lesson by posing the question the rest of the unit answers. Tell students the summary table at the end of their guided notes, The Human Cost at a Glance, asks them to rebuild exactly this map from the record, row by row, in their own words.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', 'The Collapse in Numbers',
             'More than three years of shrinking, measured plainly.',
             "Set the habit for this section before any figures: the numbers in this lesson come from the records of the period, and the government of the early 1930s counted some of them loosely. Where the reading gives a figure as an estimate, students should repeat it as an estimate. That caution does not weaken the story. It strengthens it, because the scale is not in doubt even where the last digit is. The Great Depression, in the guided notes definition, is the severe economic collapse that began in the United States in 1929 and lasted through the 1930s, marked by bank failures, mass unemployment, and falling prices. Hold that definition in view. This section covers the first two marks, falling output and mass unemployment. The bank failures belong to the next section, and the falling prices run through both.")

# ------------------------------------------------------ 5 PRODUCTION
content_text('Production cut nearly in half',
             ['Industrial production fell by nearly half, 1929 to 1932',
              'Steel mills ran at a small fraction of capacity',
              'Railroads carried far less freight',
              'The downturn deepened year after year',
              'It did not end in a season, as earlier downturns had'],
             "Give students the production figure first and let it sit. Industrial production, the output of the nation's factories and mines, had fallen by nearly half between 1929 and 1932. A fall of that size means the economy was not running slowly. It was running at about half its former size. Steel mills ran at a small fraction of their capacity, and railroads carried far less freight, which is how a factory figure becomes a national figure: mills that make less steel order less coal, railroads that carry less freight employ fewer crews, and each cut pulls the next one behind it. Earlier downturns in American history had ended in a season or a year. This one deepened year after year, which is the plainest reason contemporaries stopped calling it a depression in the older, smaller sense and began treating it as something new. Students should write the production fall and its dates into section A of the notes.",
             kick='A · The collapse in numbers')

# ------------------------------------------------------ 6 UNEMPLOYMENT STAT
stat('1 in 4', 'workers out of work in 1933, by contemporary estimate',
     'About 25 percent unemployment at the depth of the collapse · In industrial cities, the share ran higher',
     "Dwell on what this figure counts, because the guided notes test the definition. Unemployment is the condition of people who are able to work and seeking work but cannot find a job. Contemporary estimates, counted loosely by the standards of a later age, put about one worker in four out of work in 1933. The estimates do not count the farmer whose crop would not sell, the worker cut to half hours, or the man who had stopped looking, so the loss of income in the country was larger than the figure on this slide. In industrial cities the share ran higher than one in four. Behind each figure stood a wage that had stopped, and behind the stopped wage stood rent, food, and children. Ask students to say the sentence that way once, in their own words, before moving on, because the rest of the lesson is that sentence worked out in detail.",
     kick='A · The collapse in numbers')

# ------------------------------------------------- 7 SECTION B DIVIDER
divider_photo('bank-port.jpg', 'Section B', 'Bank Failures and Deflation',
              ['A crowd outside a Michigan bank,', 'February 1933.'],
              "The photograph shows a crowd outside a bank during the Michigan banking crisis of February 1933, and the photographer is not credited in the holding record, which students should hear as an honest limit on what the record says. What the crowd is doing is the subject of this section. These are not customers in the ordinary sense. They are depositors who fear their bank is about to fail, gathered to take their money out before the doors close. Section B covers the two mechanisms that turned a market collapse into a decade of ruin for families who never owned a share of stock: the bank run, which destroyed savings directly, and deflation, which quietly raised the weight of every debt in the country. Both mechanisms are in the vocabulary list, and both are tested, so students should have pencils ready for definitions as well as figures.",
              title_size=38)

# ------------------------------------------------------ 8 BANK RUN
content_text('A run could close a sound bank',
             ['A rumor: the bank held loans that could not be repaid',
              'Depositors gathered to withdraw, all at the same time',
              'No bank kept all its deposits in cash',
              'Most deposits were out on loan',
              'The doors closed, and deposits were frozen'],
             "In the guided notes definition, a bank run is a rush of depositors to withdraw their money from a bank at the same time, driven by fear that the bank will fail. Walk the mechanism slowly, because students often reverse the cause. The run did not begin because the bank had already failed. It began with a fear or a rumor, and the fear itself could do the work. No bank kept all its deposits in cash, because most deposits were out on loan to farmers, merchants, and home buyers, which is what a bank is for. A bank therefore could not pay every depositor on the same morning even if every loan it held was good. When the cash ran out, the doors closed, deposits were frozen, and most frozen deposits in failed banks were never fully repaid. About nine thousand banks failed in the decade, which is the next slide's figure.",
             kick='B · Bank failures and deflation')

# ------------------------------------------------------ 9 BANKS STAT
stat('9,000', 'banks failed in the Depression decade',
     'No federal insurance protected deposits · Families lost savings built over years',
     "Put the figure together with the mechanism from the last slide. About nine thousand banks failed in the United States during the decade. Each failure was local, a named bank on a named street, and each one took deposits with it. No federal insurance protected depositors, so a family that had saved the price of a farm, a store, or a year of schooling could lose the whole of it in one afternoon without having borrowed anything or speculated in anything. That last point does real work in the lesson's closing argument, so students should mark it. The banking collapse did not punish only the reckless. It reached careful savers through a system failure, and it destroyed the local supply of credit at the same time, because a closed bank makes no new loans to the farmers and merchants of its town. Both losses belong in section B of the notes.",
     kick='B · Bank failures and deflation')

# ------------------------------------------------------ 10 DEFLATION
content_text('Debts that grew heavier as prices fell',
             ['Prices fell across the economy, year after year',
              'Wheat and cotton could return less than the cost of growing them',
              'The dollars owed stayed the same',
              'Each payment took a larger share of a smaller income',
              'Waiting to spend paid, so buyers waited'],
             "In the guided notes definition, deflation is a general fall in prices across the economy, which raises the real burden of debts and rewards waiting to spend. Students tend to hear falling prices as good news, so work the farm example until the mechanism is plain. A farmer who borrowed at the high prices of the 1920s sold his crop at the low prices of the 1930s and owed the same number of dollars. Wheat and cotton sometimes returned less than the cost of growing them. The debt did not change on paper, and it grew heavier every year in the only terms that counted, bushels and bales. The second half of the definition belongs in the notes as well: when prices will be lower next month, a buyer who can wait has reason to wait, and waiting cuts demand, which cuts jobs, which cuts prices again. Deflation is a spiral, not a discount.",
             kick='B · Bank failures and deflation', size=24)

# ------------------------------------------------- 11 SECTION C DIVIDER
divider_photo('soup-port.jpg', 'Section C', 'Breadlines and Charity',
              ['Unemployed men outside a Chicago', 'soup kitchen, February 1931.'],
              "The photograph is a National Archives record, number 541927, showing unemployed men queued outside a depression soup kitchen opened in Chicago, in February 1931. Note its date. This is early in the collapse, before the worst of the bank failures, and already the line reaches down the sidewalk. Section C covers hunger as a public sight in the richest country in the world, and it covers the machinery that answered hunger in 1931: private charity, churches, missions, and city agencies. Students should watch for the turn inside the section. Charity was not idle and it was not stingy. It raised money, opened kitchens, and fed thousands of people a day. It failed anyway, because donations fell with incomes while the lines grew, and that failure is one of the load bearing facts in the lesson's closing question.",
              title_size=38)

# ------------------------------------------------------ 12 BREADLINES
content_photo('soup-port.jpg', 'Free food, and funds running out',
              ['A line of people waiting for free food',
               'Run by a charity, a church, or a city agency',
               'Soup kitchens fed thousands a day',
               'Donations fell as incomes fell',
               'Relief funds ran out in front of growing lines'],
              "In the guided notes definition, a breadline is a line of people waiting for free food given out by a charity, a church, or a city agency. Lines like the one in the photograph stretched along sidewalks in every large city, and the men in them were often men who had held skilled jobs a year or two earlier. Name the system that fed them accurately: it was private and local, built from donations, church kitchens, missions, and city relief funds. Then name its limit, which the reading states in one sentence students should copy. By 1931 and 1932 donations had fallen with incomes, and many charities and city relief funds were running out of money in front of lines that kept growing. A relief system funded by the incomes of the community fails exactly when the community's incomes fail. That sentence explains much of what follows in this unit, from the limits of voluntarism in the next lesson to the federal relief programs after it.",
              kick='C · Breadlines and charity')

# ------------------------------------------------- 13 SECTION D DIVIDER
divider_photo('hooverville-port.jpg', 'Section D', 'Hoovervilles and Eviction',
              ['Scrap shacks on vacant land,', 'Portland, Oregon, 1936.'],
              "The photograph is by Arthur Rothstein, working for the federal Farm Security Administration, and it shows a Hooverville in Portland, Oregon, in July 1936. The date deserves a sentence: this camp was still standing, and still being added to, more than six years after the crash. Section D covers the loss of homes in its two forms. The first is legal and quick: eviction for unpaid rent and foreclosure for an unpaid mortgage. The second is what families built afterward, on vacant land at the edges of cities, from whatever the city discarded. The guided notes ask students to name the building materials and the president whose name the camps carried, so teach both as facts of the record, not as color. A shantytown that lasts for years is a housing system, and students should be ready to describe it as one.",
              title_size=38)

# ------------------------------------------------------ 14 EVICTION AND HOOVERVILLE
content_text('Out of the apartment, onto vacant land',
             ['Eviction for rent unpaid; foreclosure on the mortgage',
              'Shacks of scrap wood, tin, packing boxes, and cardboard',
              'The largest camps held hundreds of families',
              'No running water, no sewers, no legal claim to the ground',
              'Named in bitter reference to President Hoover'],
             "In the guided notes definition, a Hooverville is a shantytown built by homeless people from scrap wood, tin, and cardboard during the Depression, named in bitter reference to President Hoover. The name was an argument addressed to the president and to voters: the man under whom the collapse deepened owned its most visible shame. The camps themselves were more organized than the word shantytown suggests. Residents laid out streets between the shacks and in the largest camps chose informal mayors. What no organization could supply was infrastructure and legal standing. The camps had no running water and no sewers, and the families had no legal claim to the ground beneath them, so a city could clear a camp whenever it chose. Students should connect this section backward: the road to the Hooverville usually ran through a stopped wage, an emptied relief fund, and an eviction notice, in that order.",
             kick='D · Hoovervilles and eviction', size=24)

# ------------------------------------------------- 15 SECTION E DIVIDER
divider_text('Section E', 'Family Strain',
             'The collapse rearranged who lived where, who worked, and who waited.',
             "This section has no single photograph and no single figure, and that is worth saying to students, because the strain it covers was recorded in smaller records: marriages postponed, births postponed, households doubled, and teenagers gone from the breakfast table. The family was the last relief system standing after wages, savings, and charity had failed, and families stretched themselves to absorb relatives and to feed extra mouths on smaller incomes. They also broke under the load in predictable ways. Men who had lost jobs rode freight trains looking for work, and hundreds of thousands of teenagers left home the same way, some hunting work and some sparing their families one more mouth to feed. Teach the section as a set of household decisions, each one rational on its own terms and each one a cost. The guided notes ask for the decisions and their causes together.")

# ------------------------------------------------------ 16 FAMILY STRAIN
content_text('Doubled up, postponed, and riding the freights',
             ['Families doubled up, taking in relatives',
              'Marriages postponed; the birth rate fell',
              'Men rode freight trains looking for work',
              'Hundreds of thousands of teenagers left home',
              'Women became the earners families depended on'],
             "Work through the list as causes and effects, because the exit ticket tests them in pairs. Families doubled up in apartments and houses, taking in relatives who had lost their own homes, which is the Hooverville's alternative and the reason the camps did not hold everyone who lost housing. Young couples postponed marriage because they could not set up a household, and the birth rate fell as couples postponed children, so the Depression is visible in the census as well as in the breadline. Men rode freight trains from town to town looking for work, and hundreds of thousands of teenagers left home the same way, some seeking work and some sparing their families one more mouth to feed. Women who found work in laundries, kitchens, and offices often became the earners their families depended on, even as many employers refused to hire married women. Each line on this slide is a plan a family gave up or remade.",
             kick='E · Family strain', size=24)

# ------------------------------------------------- 17 SECTION F DIVIDER
divider_photo('dust-port.jpg', 'Section F', 'The Dust Bowl',
              ['Dust over the Texas Panhandle,', 'photographed in March 1936.'],
              "The photograph is by Arthur Rothstein for the Farm Security Administration and shows dust over the Texas Panhandle in March 1936, from the Library of Congress FSA file. Section F moves the lesson from the cities to the southern Great Plains, where the collapse met a second disaster that no banker had caused and no bank failure could explain. Drought settled over the region in the early 1930s, and farming practices that had broken the prairie sod left the topsoil loose. Wind did the rest. Students should hold the two disasters apart in their notes, because the reading does: the farm economy had already collapsed on prices before the rain stopped, and the dust then destroyed the land itself. Families who lost both a market and a farm had one asset left, a car or a truck, and one road west.",
              title_size=40)

# ------------------------------------------------------ 18 DUST AND MIGRATION
content_photo('farmer-port.jpg', 'The fields blew away, and families drove west',
              ['Drought settled over the southern Plains',
               'Wind carried dry topsoil away in storms',
               'Storms darkened the sky at noon',
               'Families loaded cars and trucks and drove west',
               'Route 66 toward California, hoping for field work'],
              "In the guided notes definition, the Dust Bowl is the region of the southern Great Plains where drought and poor farming practices turned topsoil to dust in the 1930s, driving many farm families from their land. The photograph, also by Rothstein, shows a farmer and his sons walking in the face of a dust storm in Cimarron County, Oklahoma, in April 1936. Name the states in the reading's account: parts of Texas, Oklahoma, Kansas, Colorado, and New Mexico. Farm families who had already watched prices collapse now watched their fields blow away, and many drove west on Route 66 toward California hoping for work picking fruit and vegetables. What many found was crowded camps, low wages, and hostility from the communities they entered, which the activity takes up through the most famous FSA photograph of all, Dorothea Lange's Migrant Mother, made at Nipomo, California, in March 1936.",
              kick='F · The Dust Bowl')

# ------------------------------------------------- 19 SECTION G DIVIDER
divider_text('Section G', 'A Private Misfortune or a Public Emergency',
             'The question the whole unit follows.',
             "The lesson closes where the reading closes, with a judgment students now have the evidence to make. Set the two answers side by side and refuse, for one more slide, to settle it. On one account, hard times were a private misfortune: families endured, neighbors helped, charities fed, and better times eventually returned, as they had after earlier downturns. On the other account, a collapse that closed banks, emptied factories, and drove families from homes and land in every state at once was a public emergency, of a size that private endurance could not answer. Students have watched the private machinery work and fail in this lesson: savings destroyed by a system failure, charity funds emptied in front of growing lines, families stretched to doubling and still breaking. The writing task will make them argue the question in full, with the figures and the photographs as evidence.")

# ------------------------------------------------------ 20 THE QUESTION
content_text('A failure of the whole system at once',
             ['It reached savers, steady workers, and prudent borrowers',
              'Banks, factories, farms, and homes failed together',
              'Private charity ran out of money in front of growing lines',
              'Next: the president who had to answer it first'],
             "State the reading's closing claim plainly, because the exit ticket and the writing task both build on it. A collapse that closed banks, emptied factories, drove one worker in four from a job, and pushed families out of their homes and off their land was not a run of private bad luck. It was a failure of the whole economic system at once, reaching people who had saved carefully, worked steadily, and borrowed prudently. That is why the question at the end of the reading is a real question and not a slogan. If the failure was systemic, then a remedy at the scale of the system was at least arguable, and the argument itself is the subject of this unit. The next lesson begins with President Hoover, the man who had to answer the question first, with his own beliefs about what the federal government should and should not do. Students should leave today able to state his problem fairly, in the figures from this lesson.",
             kick='G · Private or public')

# ------------------------------------------------------ 21 GLANCE
s = slide(NAVY)
kicker(s, 'The human cost at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Four records, one cost', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The collapse', 'Production nearly halved; one worker in four out', 'Wages stopped across whole cities'),
        ('Banks and prices', 'Runs, 9,000 failures, deflation', 'Savings lost; debts grew heavier'),
        ('Food and shelter', 'Breadlines, exhausted funds, Hoovervilles', 'Hunger in public; homes lost'),
        ('Families and land', 'Doubling up, freight trains, dust and Route 66', 'Plans postponed; farms blown away')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, The Human Cost at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The four rows are the lesson's records. The collapse covers the production fall and the unemployment estimates, and what it cost was wages stopping across whole cities. Banks and prices covers the runs, the nine thousand failures, and deflation, and what it cost was savings lost in an afternoon and debts growing heavier as prices fell. Food and shelter covers the breadlines, the exhausted relief funds, eviction, and the Hoovervilles. Families and land covers doubling up, postponed marriages and births, the freight trains, and the Dust Bowl migration west. Grade the table generously on wording and strictly on pairing: each entry must say what happened and what it cost, in the student's own words.")

# ------------------------------------------------------ 22 VOCAB A
vocab('Words for the collapse',
      [('Great Depression', 'the severe economic collapse that began in the United States in 1929 and lasted through the 1930s, marked by bank failures, mass unemployment, and falling prices'),
       ('deflation', 'a general fall in prices across the economy, which raises the real burden of debts and rewards waiting to spend'),
       ('bank run', 'a rush of depositors to withdraw their money from a bank at the same time, driven by fear that the bank will fail'),
       ('unemployment', 'the condition of people who are able to work and seeking work but cannot find a job')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. Great Depression: the severe economic collapse that began in the United States in 1929 and lasted through the 1930s, marked by bank failures, mass unemployment, and falling prices. The three marks in the definition are the lesson's structure. The second term is deflation: a general fall in prices across the economy, which raises the real burden of debts and rewards waiting to spend. The third term is bank run: a rush of depositors to withdraw their money from a bank at the same time, driven by fear that the bank will fail. Note that fear, not failure, starts the run. The fourth term is unemployment: the condition of people who are able to work and seeking work but cannot find a job. Both halves count; a person who has stopped seeking work falls outside the measure, which is why the estimates understate lost income.")

# ------------------------------------------------------ 23 VOCAB B
vocab('Words for the human record',
      [('breadline', 'a line of people waiting for free food given out by a charity, a church, or a city agency'),
       ('Hooverville', 'a shantytown built by homeless people from scrap wood, tin, and cardboard during the Depression, named in bitter reference to President Hoover'),
       ('Dust Bowl', 'the region of the southern Great Plains where drought and poor farming practices turned topsoil to dust in the 1930s, driving many farm families from their land')],
      "Three more terms, again matching the guided notes exactly. The first is breadline: a line of people waiting for free food given out by a charity, a church, or a city agency. The definition names the three givers because relief in 1931 was private and local, and its limits are the lesson's argument. Hooverville: a shantytown built by homeless people from scrap wood, tin, and cardboard during the Depression, named in bitter reference to President Hoover. The materials list belongs in the definition, because scrap construction is what made the camps clearable and uninsurable as homes. Dust Bowl: the region of the southern Great Plains where drought and poor farming practices turned topsoil to dust in the 1930s, driving many farm families from their land. Note the double cause in the definition, drought and poor farming practices together, because students who blame the weather alone miss half of it.")

# ------------------------------------------------------ 24 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How deep did the Depression cut, and how did ordinary families live through it? Measure the depth first, then follow it into homes.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Cost Ledger: an unemployment series, a bank failure, a Hooverville, a migrant photograph, a family budget'),
        ('Notebook', 'Notebook page: rebuild the human cost at a glance in your own words'),
        ('Quick check', 'The Run and the Line: the bank run, deflation, the breadline, and the Hooverville'),
        ('Writing', 'A Public Emergency: the closing question of the reading as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: why a run could close a sound bank, two changes in family life with their causes, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Cost Ledger, runs five stations through the evidence: an unemployment series with its limits stated, a bank failure record with the failure counts, Rothstein's Hooverville photograph from Portland, Lange's Migrant Mother with its Library of Congress caption, and a teaching budget cut in half, ending in a ledger sorted into money lost, homes lost, and plans lost. The notebook page asks students to rebuild the human cost at a glance themselves. The quick check, The Run and the Line, tests the bank run, deflation, the breadline, and the Hooverville against the Michigan photograph. The writing task, A Public Emergency, turns the reading's closing question into an essay. The exit ticket has three parts: in one sentence, why a run could close a sound bank; two changes in family life with the economic cause of each; and the lesson question answered in two or three sentences with at least two facts from the notes. Next lesson takes up President Hoover and the limits of his answer.")

dc.save(OUT)
