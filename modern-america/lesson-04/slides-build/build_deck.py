#!/usr/bin/env python3
"""Modern America Lesson 4 deck, "The Digital Transformation," built to the
approved system: image-led slides, fragments only on screen, comprehensive
speaker notes, full lesson and vocabulary coverage.
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

# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'MODERN AMERICA · LESSON 4', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Digital Transformation', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'The machine, the network, and the fractured news world, 1980 to 2010', size=17, color=POWDER)
notes(s, "The photograph shows operators at a UNIVAC I computer at the United States Census Bureau, a work of Census Bureau employees and public domain as stated on its Wikimedia Commons file page. Open with what the photograph proves. In the era it shows, a computer filled a room, cost more than a house, and belonged to a government agency, a university, or a large company, and ordinary people met computing only through specialists. This lesson covers the thirty years in which that machine shrank onto a desk, learned to talk to other machines, remade shopping and investing, broke the common news day into competing channels, and divided the country by who could get online. Tell students the lesson follows their guided notes, sections A through G, and that no bank record in the Primary Source Project carries this lesson. It is built from federal law and federal statistics, and the activity file says so on its face.")

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("How did the computer and the Internet remake American work, commerce, and news between 1980 and 2010?", {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the United States remake itself after 1980, in its economy, its population, and its place in the world, and what did the remaking settle and what did it leave open?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Read the question slowly and take its three nouns one at a time. Work: the personal computer rewrote office tasks, and the smartphone later thinned the boundary between office hours and the rest of the day. Commerce: buying and selling moved online from almost nothing in the middle 1990s, while investors bid the new companies to a peak in March 2000 and lost about 78 percent of that value by October 2002. News: cable channels, talk radio, and then social media replaced one common news day with a continuous flow a citizen could select by tendency. Keep the dates in front of the class all hour. The machine belongs chiefly to the 1980s, the network to the 1990s, and the fractured news world runs on a separate track that begins with CNN in 1980 and completes itself in the 2000s. The writing task will ask which of the three changes reached furthest.")

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Seven steps in thirty years', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The machine on the desk', 'Computing leaves the institution'),
        ('B', 'The network opens', '18 percent online in 1997, 42 in 2000'),
        ('C', 'The law that framed it', 'The 1996 act and Section 230'),
        ('D', 'Commerce, boom, and bust', 'Peak 5,048, then a fall of 78 percent'),
        ('E', 'The news world fractures', 'CNN 1980, the Fairness Doctrine ends 1987'),
        ('F', 'Publication in every pocket', 'Social media and the smartphone'),
        ('G', 'The divide', 'Access follows income, schooling, age, place')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This slide is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A is the personal computer carrying computing out of institutions. Section B is the Internet opening to the public, counted household by household by the Census Bureau. Section C is the Telecommunications Act of 1996 and the liability shield in its Section 230. Section D is commerce online, the boom, and the crash of 2000 to 2002. Section E is the news world fracturing, from CNN in 1980 through the repeal of the Fairness Doctrine to the drain of newspaper advertising. Section F is social media and the smartphone. Section G is the digital divide and the country the transformation made. Tell students the summary table at the end of their guided notes asks them to rebuild this map stage by stage, with the evidence attached to every stage.")

# 4 SECTION A DIVIDER
divider_photo('univac-port.jpg', 'Section A', 'The Machine on the Desk',
              ['Operators at a UNIVAC I, U.S. Census Bureau.', 'Computing begins in institutions like this one.'],
              "The photograph shows operators at a UNIVAC I computer at the Census Bureau, the institutional world this section leaves behind. Set the opening contrast carefully, because students often assume computers were always personal. In 1975 a computer filled a room, cost more than a house, and belonged to a government agency, a university, or a large company. A person who needed computing done handed the job to specialists and waited for printouts. The Census Bureau itself is a good example to name: it had used a UNIVAC to count the country since the early 1950s, and no census clerk imagined owning the machine. Section A covers the fifteen years in which a machine moved onto an office desk and then a kitchen table, sold as kits and then as finished products in the late 1970s and standardized for business after 1981. Ask the class to watch for the second change inside the first, because software became an industry of its own at the same time, and the two changes together rewrote office work.",
              title_size=40)

# 5 THE WORKPLACE REWRITTEN
content_text('Work changed task by task',
             ['Software becomes an industry of its own',
              'Typing pools give way to workers drafting their own letters',
              'Drafting tables give way to screens',
              'Filing cabinets give way to disks',
              'Skills of whole departments sit in one pair of hands'],
             "Teach the personal computer through the tasks it absorbed, because the transformation was practical before it was dramatic. The key term belongs here in full. A personal computer is a computer built for one person's desk and home, sold in large numbers from the late 1970s onward, which carried computing out of institutions and into daily life. Word processing ended the typing pool as a separate department: the person who composed a letter now typed, corrected, and printed it. Spreadsheets ended the long hand calculation of budgets, and a change in one figure recalculated the whole sheet in seconds. Drafting programs moved drawing from the table to the screen. Employers began to expect these skills of nearly every office applicant, which is the quiet measure of the change. A skill that had belonged to a department, with its own staff and its own room, now sat in one person's hands at one desk, and the offices of the country were rebuilt around that fact across the 1980s and early 1990s.",
             kick='A · The machine', size=23)

# 6 STAT COMPUTERS
stat('51%', 'of households had a computer in 2000',
     'Census Bureau, August 2000 · Up from about 8 percent of households in 1984',
     "Let the two numbers carry the section. In 1984 about 8 percent of American households had a computer, a hobbyist and professional machine at the edge of ordinary life. By August 2000 the Census Bureau counted 54 million households, about 51 percent, with one or more computers in the home. That is more than a fivefold rise in the share of households in sixteen years, measured by the federal government's own survey, the Current Population Survey. Pair the figure with the workplace record from the last slide. The machine entered the home and the office in the same decades, so a generation learned the same keyboard in both places, and children met at school the machine their parents used at work. Also mark what the figure does not say. A household with a computer in 2000 was not yet necessarily a household online, and the gap between having the machine and having the connection is where the next section begins. The network figures will rise faster than these did, because the machines were already waiting on the desks.",
     kick='A · The machine')

# 7 SECTION B DIVIDER
divider_photo('arpanet-port.jpg', 'Section B', 'The Network Opens',
              ['The ARPANET logical map, March 1977.', 'The whole network, drawn on one page.'],
              "The image is the logical map of the ARPANET in March 1977, marked public domain on its Wikimedia Commons file page, and it shows the network the Internet grew from, small enough to draw whole on one page. Its nodes were government and university machines, joined by a defense research program begun in 1969. A university network of the 1980s, built by the National Science Foundation, carried the design forward. Section B covers what happened when that research system opened to the public and to commerce in the middle 1990s. Browser software is the hinge to stress. Before it, using the network took training in its commands, and its users were researchers. After it, anyone who could point and click could read, write, buy, and publish there. The Census Bureau then counted the arrival household by household, and its figures, 18 percent of households online in 1997 and about 42 percent in 2000, are the fastest adoption figures in this lesson.",
              title_size=40)

# 8 THE NETWORK OPENS
content_text('A network of networks, opened to everyone',
             ['Roots in a defense research network begun in 1969',
              'A university network carries the design through the 1980s',
              'The system opens to the public and to business in the middle 1990s',
              'Browser software makes it usable by anyone',
              'Mail, the Web, and search arrive on one screen'],
             "State the definition in full, because the test draws on it. The Internet is the network of computer networks that grew out of government and university systems into a public means of communication, commerce, and publication in the 1990s. Hold on the phrase network of networks. No single company built or owned the system; separate networks agreed to speak the same technical language, so a message could cross from one to another without asking a central office. That design came from its government and university makers, and it shaped everything that followed, including the difficulty of governing the system later. When the system opened to commerce in the middle 1990s, electronic mail was the first use most households met, then the World Wide Web, then search tools that made the Web's growing mass findable. Each use arrived on the same screen, which is why the network absorbed the post office, the library, the store, and the newspaper stand into one piece of furniture in under a decade.",
             kick='B · The network', size=22)

# 9 STAT ONLINE
stat('42%', 'of households were online in 2000',
     'Census Bureau · Up from about 18 percent in 1997 · About half of households by 2001',
     "Use this figure to teach speed. The Census Bureau first collected data on household Internet use in 1997 and found about 18 percent of households online at home. Three years later, in August 2000, it counted 44 million households, about 42 percent, with at least one member using the Internet at home. By 2001 about half of households were online and a majority had a computer. Compare the pace with the last stat slide. The computer took sixteen years to move from about 8 percent of households to about half. The connection took about four years to cover similar ground, because it arrived as a service sold to machines already sitting in the home. Ask students what a change moving at this speed does to the industries standing in its path, and hold their answers for section D, where commerce follows the crowd online, and section E, where the advertising that paid for newspapers begins to drain toward the screen.",
     kick='B · The network')

# 10 SECTION C DIVIDER
divider_text('Section C', 'The Law That Framed It',
             'The Telecommunications Act of 1996, and twenty six words that shielded the platforms.',
             "Section C is the lesson's legal hinge, and it should be taught as law, in the statute's words, not as background color. The Telecommunications Act of 1996, Public Law 104-104, was the first full rewriting of federal communications law since the Communications Act of 1934, a frame sixty two years old. Most of the act concerned ownership: it loosened the rules across broadcasting, cable, and telephone service, letting companies own more stations and enter each other's markets. The passage that shaped the Internet sat inside the act's decency title, as Section 230 of the Communications Act. Its operative sentence is short enough to read aloud, and the next slide does. Tell students the sentence was written when the online services of the day carried discussion boards and early web pages, and that the giant platforms of the next decade grew up behind the shield it created. The activity file opens with this statute, and students will be asked to state the shield in their own words there.")

# 11 SECTION 230
content_text('No provider shall be treated as the publisher',
             ['The 1996 act rewrites communications law for the first time since 1934',
              'Ownership rules loosen across broadcasting, cable, and telephones',
              'Section 230: a service is not the speaker of its users\u2019 words',
              'Platforms grow behind the shield in the next decade'],
             "Quote the sentence whole, slowly, because the activity, the quick check, and the exit ticket all return to it. No provider or user of an interactive computer service shall be treated as the publisher or speaker of any information provided by another information content provider. Then translate it. A newspaper is legally the publisher of what it prints and can be sued for it. An online service carrying other people's words, under this sentence, is not their speaker in law. The practical consequence followed over the next decade. A company could host millions of posts, photographs, reviews, and listings without reviewing each one as a publisher reviews a page, and the social media platforms of section F, the auction and review sites of section D, and the comment and search services in between all grew behind that shield. Students do not need to judge the shield today. They need to be able to state it, date it to 1996, and name what grew behind it.",
             kick='C · The law', size=23)

# 12 SECTION D DIVIDER
divider_text('Section D', 'Commerce, Boom, and Bust',
             'Shopping moves online, prices run ahead of it, and the network outlives the crash.',
             "Section D joins two stories that students often merge, and the lesson's point is to keep them apart. The first story is commerce: the buying and selling of goods and services over the Internet, growing from almost nothing in the middle 1990s into a central part of American retail. That growth was steady, year by year, and it never reversed. The second story is speculation: investors bidding the shares of Internet companies, many with no profit, to prices that assumed the commerce of a generation would arrive in a few years. That story rose to a peak on March 10, 2000 and then collapsed, erasing trillions of dollars in paper wealth by 2002. The activity file gives students the index record itself, stripped of any company's advertising, so they can see the shape of the boom in four numbers. Teach the section's closing comparison explicitly: contemporaries reached for the railroad booms of the nineteenth century, when speculation also collapsed and the network it paid to build also remained in use.")

# 13 COMMERCE AND BUBBLE
content_text('The store and the stock price part company',
             ['E-commerce grows from almost nothing in the middle 1990s',
              'Books, auctions, then nearly everything, sold on a screen',
              'Investors buy companies with a web address and no profit',
              'The bubble ends in the crash of 2000 and 2001'],
             "Give the two definitions in full, side by side, so students can hold them apart. E-commerce is the buying and selling of goods and services over the Internet, which grew from almost nothing in the middle 1990s into a central part of American retail. The dot-com bubble is the speculative boom in Internet company stocks in the late 1990s, ending in a crash in 2000 and 2001 that erased trillions of dollars in paper wealth. The teaching difficulty is that the same names appear in both stories. An online bookseller was at once a real store teaching millions of Americans to enter a card number on a screen, and a stock priced as if every store in the country would soon close. The store was real. The price was not, and the crash sorted the two. Hundreds of firms failed, and their workers and investors paid the bill the speculation had run up. The commerce itself, the habit of buying on a screen, kept growing every year through the crash, which is the evidence students should carry into the writing task.",
             kick='D · Commerce', size=23)

# 14 STAT NASDAQ
stat('5,048', 'the NASDAQ Composite at its peak',
     'March 10, 2000 · Down about 78 percent by October 2002, to about 1,114',
     "Let the number and its fall do the teaching, in the record's own terms. The NASDAQ Composite, the index heavy with technology and Internet stocks, closed at its peak of 5,048 on March 10, 2000, having first closed above 1,000 less than five years earlier, on July 17, 1995. By October 9, 2002 it closed at about 1,114, a fall of about 78 percent from the peak. Teach what a fall of that size means in a household. A retirement account or a college fund invested at the peak held about twenty two cents of every dollar by the bottom, and the index did not return to its peak for fifteen years. Then make the distinction the last slide built. These are paper prices for shares, not measures of the network's use. In the same thirty months that the index lost about 78 percent, the Census Bureau's figures showed household Internet access still rising, and online shopping still growing. Prices collapsed; the transformation did not.",
     kick='D · The bust')

# 15 SECTION E DIVIDER
divider_text('Section E', 'The News World Fractures',
             'News runs all day from 1980, the other side becomes optional in 1987, and the audience sorts itself.',
             "Section E runs on its own track, and students should notice it begins before the public Internet exists. Cable news starts in 1980, the Fairness Doctrine falls in 1987, and national talk radio grows in the late 1980s, all before a browser sat in an ordinary home. The Internet then deepened a fracture it did not start, draining the advertising that paid for newspaper reporting and giving every tendency its own online edition. Teach the section's factual discipline explicitly, following the reading. The fragmentation is stated as a measured fact of audience data: how many channels existed, when they launched, who listened and watched, and where the advertising went. It is not taught as an accusation against any channel, host, or audience, and students' verdicts in this lesson are graded on evidence, never on which news world they prefer. That discipline is the same one the unit applies to every contested subject, and this is a good hour to say so plainly.")

# 16 CABLE AND RADIO
content_text('All day news, and the end of the other side',
             ['CNN goes on the air June 1, 1980',
              'News becomes a continuous flow, not a nightly report',
              'The Fairness Doctrine is repealed in 1987',
              'National talk radio grows in the space that opens',
              'Rival cable channels launch in 1996'],
             "Give the definition in full first. Cable news is television news carried by cable channels around the clock, beginning with CNN in 1980, which replaced the nightly broadcast as many Americans' main source of news. Work through the machinery in order. A channel filling twenty four hours cannot wait for the day's events to settle; it reports the flow itself, returns to the strongest story for hours, and treats every development as urgent. In 1987 the Federal Communications Commission repealed the Fairness Doctrine, the rule that had required broadcasters to present contrasting views on public issues. National talk radio, carried from a single studio to stations across the country, grew quickly from 1988 in the space that opened, and its hosts spoke to their listeners as a side, not as neutral reporters. In 1996 two rival cable channels, MSNBC and Fox News, launched with distinct audiences and outlooks. The common news day, built on three networks and a local paper, now had machinery working against it from several directions at once.",
             kick='E · The news', size=22)

# 17 NEWSPAPERS AND SORTING
content_text('The advertising leaves, the audience sorts',
             ['Classified advertising drains toward free online listings',
              'Wider advertising follows the audience to the screen',
              'The reporting that advertising paid for shrinks with it',
              'A citizen can live inside a news world of one tendency'],
             "Teach this slide as an economics lesson before it is a media lesson. A metropolitan newspaper of the old model was paid for less by its readers than by its advertisers, and its classified pages, jobs, cars, apartments, and personals, were among the most profitable pages ever printed. Free and cheap online listings took the classifieds first, because a searchable listing is simply better for a buyer than a column of small print. The wider advertising then followed the audience to the screen, and the reporting staffs the money had supported shrank, bureau by bureau, across the 2000s. State the result in the audience surveys' terms. Where a generation earlier most households drew on the same few broadcasts and the same local paper, a citizen could now spend the day inside a news world of one tendency, hearing chiefly the accounts that fitted it. Hold the discipline of the last divider: this is a statement about audiences and money, measured in surveys and accounts, and it sets up the political argument of the unit's last lesson.",
             kick='E · The news', size=23)

# 18 SECTION F DIVIDER
divider_text('Section F', 'Publication in Every Pocket',
             'From the middle 2000s, anyone with an account is a publisher, and the network joins the person.',
             "Section F covers the second transformation, and it begins from the middle 2000s, after the crash and after broadband reached the home. The first transformation had put a connected machine on the desk. The second put publication into the hands of the machine's user and then put the machine into the user's pocket. Stress the word publication, because it is the section's hinge. For five centuries, publishing required a press, a transmitter, or a studio, and the people who owned those tools decided what the public read and heard. The older media in this course, from the pamphlet to the network broadcast, all ran through such gatekeepers. Social media removed the gate: a photograph taken on a street corner and an official statement from a government now traveled the same channels at the same speed, and readers sorted out which to trust. The smartphone, sold in large numbers after 2007, then joined the network to the person, so the transformation stopped being a place a person visited and became a condition of the day.")

# 19 SOCIAL MEDIA AND SMARTPHONE
content_photo('univac1108-port.jpg', 'Everyone a publisher, everywhere',
             ['Social media grows from the middle 2000s',
              'Users publish their own words, photographs, and video',
              'The smartphone after 2007 joins the network to the person',
              'Work follows onto the same small screen'],
             "Give the definition in full. Social media is the Internet platforms, growing from the middle 2000s, on which users publish their own words, photographs, and video and build networks of followers and friends. The photograph beside the fragments shows a UNIVAC 1108 installation at the Census Bureau, public domain on its Commons file page, and its distance from the subject is the point: within one working lifetime, computing went from a room a specialist tended to a screen in every pocket. Work through the smartphone's effect on work carefully, because it completes the lesson question's first noun. Mail and documents moved onto the same small screen as news and shopping, so the boundary between office hours and the rest of the day thinned for millions of workers. By 2010 an American could shop, bank, argue, publish, and answer an employer without sitting down at a desk, and the desk machine of section A had become the ancestor of a device carried against the body all day.",
             kick='F · The second transformation')

# 20 SECTION G DIVIDER
divider_text('Section G', 'The Divide and the Country It Made',
             'The transformation reached everyone at a different speed, and the federal surveys measured the difference.',
             "Section G closes the lesson with the limit on every claim made in it, and it rests on federal surveys students can name. The National Telecommunications and Information Administration, in the Department of Commerce, published its Falling Through the Net surveys in 1998, 1999, and 2000, built on Census Bureau data, and gave the gap its working name, the digital divide. Teach the section's shape: the same reports record rapid growth in every group they measured and wide gaps between those groups in the same tables. Both halves are the record, and a student who keeps only one has not read the surveys. The gaps followed the lines the vocabulary names: income, education, age, and place. Access bought at a school or a library, valuable as it was, was not the same as access at home, where homework, job applications, government services, and commerce increasingly assumed a connection. The writing task requires this section's evidence, so teach it as an argument students must answer, not as a footnote to a story of progress.")

# 21 THE DIVIDE MEASURED
content_text('Growth everywhere, gaps in the same tables',
             ['Household access: 26.2 percent in 1998, 41.5 in 2000',
              'Top income households about twenty times as likely to be online',
              'Access rises steeply with education',
              'Rural households trail city households at every income'],
             "Give the definition in full to close the vocabulary. The digital divide is the gap between Americans with ready access to computers and the Internet and those without, which followed lines of income, education, age, and place. Then work the station's figures in pairs. The growth figures: the NTIA surveys counted household Internet access at 26.2 percent in December 1998 and 41.5 percent in August 2000, with computer ownership passing half of households in the same span. The gap figures, from the same survey series: households earning 75,000 dollars or more were about twenty times as likely to have Internet access, and about nine times as likely to have a computer, as households at the lowest income level, and access rose steeply with education while rural households trailed at every income. Ask the class to state, in one sentence, how both sets of figures can be true at once. That sentence, growth and division together, is the honest summary of the whole transformation, and it is the sentence the writing task will reward.",
             kick='G · The divide', size=23)

# 22 STAT DIVIDE
stat('20 to 1', 'the income gap in Internet access, 1998 data',
     'NTIA Falling Through the Net · Households at $75,000 or more against the lowest income households',
     "Use this number to correct the simplest version of the lesson's story, in which a technology arrives and everyone gets it. The NTIA surveys found that in the 1998 data, households earning 75,000 dollars or more were about twenty times as likely to have Internet access at home as households at the lowest income level, and about nine times as likely to have a computer. Twenty to one is not a lag of a season; at the speed the network was spreading, it meant whole communities meeting the transformation years after others, on shared machines in schools and libraries, while connected households banked, applied, studied, and shopped from home. Cost was the reason the surveys heard most often, which is why the gap follows income so closely. Pair this stat with the growth figure from the last slide before moving on. The divide is not evidence that the transformation was small. It is evidence about its shape: fastest where money and schooling already stood, slowest where they did not, in the same years and the same country.",
     kick='G · The divide')

# 23 GLANCE
s = slide(NAVY)
kicker(s, 'The digital transformation at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Five stages, one divide', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The machine', 'PCs in about 51 percent of households, 2000', 'Work rewritten task by task'),
        ('The network', 'Online: 18 percent in 1997, about half by 2001', 'Commerce and publication move in'),
        ('The boom', 'NASDAQ 5,048 in 2000, down 78 percent by 2002', 'Prices fell; the network remained'),
        ('The news', 'CNN 1980 to social media in the 2000s', 'One common edition gives way'),
        ('The divide', 'Twenty to one by income in the 1998 data', 'Reach stops at the survey lines')]
yy = 2.62
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=21, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.6, 0.9, d, size=15, color=POWDER, leading=1.2)
    text(s, 8.75, yy + 0.05, 3.7, 0.9, why, size=15, color=POWDER, leading=1.2)
    yy += 0.92
notes(s, "This slide mirrors the final table in the guided notes, The Digital Transformation at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The rows compress the arc with an evidence figure and a consequence attached to each stage. The machine row pairs the Census figure, about 51 percent of households with a computer in 2000, with the rewriting of office work. The network row runs household access from about 18 percent in 1997 to about half by 2001. The boom row holds the NASDAQ peak of 5,048 in March 2000 against the fall of about 78 percent by October 2002 and the network's survival. The news row runs from CNN in 1980 to social media in the 2000s. The divide row is the limit, twenty to one by income in the 1998 survey data. Grade the table generously on wording and strictly on the figures and dates.")

# 24 SYNTHESIS
content_text('What the thirty years changed',
             ['Work: the desk machine, then the pocket screen',
              'Commerce: the store on a screen, surviving its own bubble',
              'News: a common edition gives way to chosen channels',
              'Publication: from gatekeepers to every account holder',
              'The limit: access followed income, schooling, age, place'],
             "Draw the lesson together around the question's three nouns, because the exit ticket and the writing task both return to them. Work: computing began in institutions, moved to the desk with the personal computer, and left the desk for the pocket with the smartphone, thinning the boundary of the working day. Commerce: e-commerce grew steadily from almost nothing into a central part of retail, and it is essential that students separate that steady line from the bubble's prices, which rose to 5,048 and fell about 78 percent while the shopping continued. News: the common edition built on three networks and a local paper gave way to cable channels running all day, talk radio without an obligation to carry the other side, and platforms on which every citizen publishes. Over all three stands the divide, measured by the federal government's own surveys: the transformation's reach was real, rapid, and uneven, and its unevenness is part of its history, not an exception to it.",
             kick='Synthesis', size=24)

# 25 VOCAB A
vocab('Words for the machine, the network, and the boom',
      [('personal computer', 'a computer for one desk and home'),
       ('Internet', 'the network of computer networks'),
       ('e-commerce', 'buying and selling over the Internet'),
       ('dot-com bubble', 'the late 1990s stock boom and its crash')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. The first term is personal computer: a computer built for one person's desk and home, sold in large numbers from the late 1970s onward, which carried computing out of institutions and into daily life. The second is Internet: the network of computer networks that grew out of government and university systems into a public means of communication, commerce, and publication in the 1990s. The third is e-commerce: the buying and selling of goods and services over the Internet, which grew from almost nothing in the middle 1990s into a central part of American retail. The fourth is dot-com bubble: the speculative boom in Internet company stocks in the late 1990s, ending in a crash in 2000 and 2001 that erased trillions of dollars in paper wealth. Test the pair students most often merge: e-commerce kept growing through the crash that ended the bubble.")

# 26 VOCAB B
vocab('Words for the news world and the divide',
      [('cable news', 'news by cable, around the clock, from CNN in 1980'),
       ('social media', 'platforms where users publish for themselves'),
       ('digital divide', 'the access gap, by income, schooling, age, place')],
      "Three more terms, again matching the guided notes exactly. The first term is cable news: television news carried by cable channels around the clock, beginning with CNN in 1980, which replaced the nightly broadcast as many Americans' main source of news. Students should anchor the term to its date, June 1, 1980, which places the fracture's start before the public Internet. The next term is social media: the Internet platforms, growing from the middle 2000s, on which users publish their own words, photographs, and video and build networks of followers and friends. The last term is digital divide: the gap between Americans with ready access to computers and the Internet and those without, which followed lines of income, education, age, and place. Anchor that term to its measuring instruments, the Census Bureau counts and the NTIA Falling Through the Net surveys. With these three terms the full set of seven is complete, in the guided notes, in these slides, and in the review materials for the unit test.")

# 27 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did the computer and the Internet remake American work, commerce, and news between 1980 and 2010? Argue it from the record, with dates and figures.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Transformation File: five stations from the 1996 act to the NTIA surveys, and a verdict on which change reached furthest by 2010'),
        ('Notebook', 'Notebook page: the five stages charted by what changed, the evidence, and who was reached or missed'),
        ('Quick check', 'The Machine, the Network, and the News: the Census table, the Section 230 line, and the news sequence'),
        ('Writing', 'Which Change Reached Furthest: the machine, the network, or the fractured news world, argued from the Transformation File')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: Section 230 in one sentence, the Census figures and the NASDAQ peak, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Transformation File, runs five stations through the record: the Telecommunications Act passage with Section 230, the Census Bureau computer and Internet use record, the dot-com peak and crash record, the cable news record, and the digital divide record from the NTIA surveys, ending in a verdict on which change reached furthest into ordinary life by 2010. The notebook page charts the five stages by what changed, the evidence, and who was reached or missed. The quick check tests the Census table, the statute line, and the news sequence against blueprint entries 7 and 8. The writing task requires the divide used as evidence and a rival change answered from the record. The exit ticket has three parts: Section 230 stated in one sentence, the Census figures for 1997 and 2000 with the NASDAQ peak and its date, and the lesson question in two or three sentences with one fact about work and one about news.")

dc.save(OUT)
