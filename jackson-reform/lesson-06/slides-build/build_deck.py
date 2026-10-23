#!/usr/bin/env python3
"""Jackson and Reform Lesson 6 deck, "Revival and Reform: The Second Great
Awakening," built to the approved system: image-led slides, fragments only
on screen, comprehensive speaker notes, full lesson and vocabulary
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

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'JACKSON AND REFORM · LESSON 6', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Revival and Reform', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'The Second Great Awakening', size=17, color=POWDER)
notes(s, "The image is a detail of J. Maze Burbank's 1839 drawing of a camp meeting, made from a sketch taken on the spot and in the public domain. It belongs on the title because the camp meeting is where this lesson begins: an outdoor crowd, a preacher at a stand, and hearers overcome where they sit. The lesson runs from that clearing in Kentucky in 1801 to a Massachusetts statehouse in 1848. Along the way it follows one chain. A revival taught that every person could choose salvation. The converts that teaching produced organized societies. The societies took up drink, schooling, and the confinement of the insane, in that order, and carried their remedies from the signature to the statute book.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("Why did revival produce reformers, and what did they set out to fix first?", {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ("What did democracy mean in Jackson's America, who was it for, and what did the era's reformers claim it still owed?", {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Read the lesson question slowly and notice that it has two halves, and the lesson answers them in that order. The first half asks for a mechanism, not a mood. Revival produced reformers for a stated reason that the preachers themselves wrote down: conversion was an act of the will, religion was work assigned to human beings, and a will trained to choose the good in the soul did not retire when the meeting ended. The second half asks for a first target, and it has a precise answer with a date: drink, in 1826, by a signed pledge. By the end of the hour students will trace the chain from a Kentucky clearing to a pledge card, a school report, and a memorial laid before a legislature.")

# ------------------------------------------------- 3 ONE SLIDE
s = slide(CREAM)
kicker(s, 'The lesson in one slide', color=RUST)
text(s, 0.9, 0.95, 11.5, 1.0, 'Seven parts, in order', size=31, color=NAVY, font='Georgia')
frags(s, ['A. A revival sweeps the country',
          'B. Finney and the new measures',
          'C. The burned-over district',
          'D. From conversion to reform',
          'E. Temperance, the first crusade',
          'F. Mann and the common schools',
          'G. Dix and the insane'], y=2.0, size=25, gap=10)
notes(s, "Use this slide as the map of the hour, and point students to the same seven letters in their guided notes. The letters are the filing system for everything that follows, in the reading, the notes, and the activity. Section A sets the scene: a revival running from about 1800 into the 1840s, carried by camp meetings and circuit riders, teaching that salvation could be chosen. Section B gives the revival its method in Finney, the Rochester meetings, and the Lectures of 1835. Section C maps the ground where revival ran hottest, the burned-over district of New York. Section D makes the lesson's central step, from conversion to reform. Sections E, F, and G then take the first three fields the reformers worked, in their order: drink, the schoolhouse, and the asylum, closing in 1848.")

# ------------------------------------------------- 4 DIVIDER A
divider_photo('camp-port.jpg', 'Section A', 'A Revival Sweeps the Country',
    ['Camp meetings, circuit riders, and a choice offered to everyone'],
    "The image is a portrait detail of Burbank's 1839 camp meeting drawing. Open the lesson with the form, because the form explains the reach. Most Americans of 1800 lived in scattered settlements, far from any settled parish, and the older churches waited for members to come to them. The revival went to the people instead. Methodist and Baptist preachers rode circuits through the backcountry, and Presbyterian ministers joined them at outdoor sacramental meetings that turned into camps. A meeting was an event in a clearing: tents and wagons around a preaching stand, services from morning into the night, and preaching aimed at a decision made in public, on the spot, before the crowd scattered back to its farms. A meeting could run through the night and into the following days when conviction took hold.")

# ------------------------------------------------- 5 CONTENT A
content_text('A choice offered to everyone',
    ['Begins about 1800, runs into the 1840s', 'Camp meetings lasting for days', 'Preachers riding circuits', 'Salvation offered to every person'],
    "Teach the definition here in its full form, because the whole unit's reform argument rests on it. Second Great Awakening: the evangelical revival that swept the United States from the turn of the century into the 1840s, carried by camp meetings and itinerant preachers, which taught that every person could choose salvation and sent millions of converts toward the work of reforming society as well as themselves. Slow down on the contrast the reading draws. The older Calvinism many of these preachers inherited taught that salvation was sealed before birth for a chosen few. The revival's preachers offered it to every person in the clearing, and made the choosing itself the center of the service. Every later section of this lesson grows out of that single offered choice.",
    kick='Section A · The teaching')

# ------------------------------------------------- 6 STAT A
stat('1801', 'the camp meeting at Cane Ridge, Kentucky',
    'Thousands gather in the woods in August for nearly a week of preaching',
    "Use the date and the gathering to fix the revival's opening scene in students' minds. At Cane Ridge, in Bourbon County, in August 1801, a sacramental meeting at Barton Stone's church drew thousands into the woods. The usual estimates put the crowd between ten and twenty thousand people, in a state whose largest towns held only a few thousand, and the meeting ran for nearly a week. Hearers wept, cried out, and fell to the ground under conviction of sin, and neighbors prayed with them where they lay. Whether every estimate is exact is not the point to press. The scale is: a crowd of that size, gathered by preaching alone, showed the preachers what their instrument could do. Cane Ridge followed a smaller sacramental meeting at Red River, in the same country, the summer before.",
    kick='Section A · The scene')

# ------------------------------------------------- 7 DIVIDER B
divider_photo('finney-port.jpg', 'Section B', 'Finney and the New Measures',
    ['Rochester, 1830 and 1831, becomes the model'],
    "The image is a painted portrait of Charles Grandison Finney, in the public domain, showing him in later life with the beard he wore at Oberlin. The Finney of this lesson is younger and clean shaven, a lawyer converted in 1821 who gave up his practice to preach, and who worked the towns of western New York through the 1820s before Rochester made him famous. Rochester mattered because it was not a frontier clearing. It was a booming canal town of merchants, millers, lawyers, and workers, and Finney's meetings there in the winter of 1830 and 1831 reached all of them at once, in nightly services that ran for months. What he built there became the template other preachers copied.")

# ------------------------------------------------- 8 CONTENT B
content_photo('finney-port.jpg', 'Religion is the work of man',
    ['A lawyer converted in 1821', 'Rochester meetings, 1830 and 1831', 'Conversion an act of the will', 'A revival follows its means, as a crop follows sowing'],
    "Teach the man through his own definition, which the guided notes carry word for word. Charles Grandison Finney: the revival preacher whose Rochester meetings of 1830 and 1831 became the model of the new evangelism, who preached that conversion was an act of the sinner's own will and organized his converts into the temperance, antislavery, and moral reform societies of the age. In the Lectures on Revivals of Religion of 1835 he wrote the doctrine down: religion is the work of man, and a revival is not a miracle but the result of the right use of the appropriate means. The crop comparison is his, and students meet it again at Station 1 of the activity. His converts were expected to keep choosing, in public, after the sermon ended.",
    kick='Section B · The doctrine')

# ------------------------------------------------- 9 CONTENT B2
content_text('The new measures',
    ['Protracted meetings, night after night', 'Plain speech aimed at a decision', 'The anxious bench, prayed for by name', 'Women praying in the meetings'],
    "List the measures as techniques, because that is what Finney said they were: means, chosen because they produced the result. A protracted meeting refused to let conviction cool, returning night after night until a decision was made. Preaching in plain, direct speech treated the hearer as a person who could act now, not as a student of doctrine. The anxious bench brought sinners under conviction to the front, where the congregation prayed for them by name, making the private struggle public and supported. Older ministers objected to all of it, including the part women took in the praying, and the argument itself advertised the method. Students should see that organization, not excitement alone, is the lesson's subject. Each measure was defended the same way Finney defended the whole system, by its fruit.",
    kick='Section B · The means')

# ------------------------------------------------- 10 DIVIDER C
divider_text('Section C', 'The Burned-Over District',
    'Western and central New York, swept again and again',
    "Now place the revival on its hottest ground. The region of western and central New York, strung along the Erie Canal from Albany to Buffalo, was settled, enriched, and unsettled again in a single generation: new farms, new canal towns, new money, and whole populations arriving and moving on. Revival came through it in wave after wave, Rochester's meetings among them, until preachers gave the region the name this section carries. Teach the name as the preachers meant it: not praise and not quite blame, but a report on fuel and fire, a district where the preaching had been so frequent that organizing anything new there meant working ground already swept by a dozen campaigns before yours. Keep the canal at the center of the map as you teach this section.")

# ------------------------------------------------- 11 CONTENT C
content_text('No fuel left to burn',
    ['The Erie Canal runs through it', 'Rochester, Utica, Syracuse', 'Abolition and temperance draw members', "New movements rise, the Mormons at Palmyra, 1830"],
    "Give the term in full as the notes carry it. burned-over district: the region of western and central New York swept so often by revival and reform that preachers said it had no fuel left to burn, the seedbed in the 1830s and 1840s of abolitionism, women's rights, temperance crusades, and new religious movements. Then make the geography do work. The canal carried preachers, printed tracts, and converts' letters along the same route it carried wheat and merchandise, so a campaign in one town became news in the next within days. That density is why the district produced movements out of proportion to its population, including Joseph Smith's new church, organized from Palmyra in 1830. The name began as a preacher's complaint and became a historian's label for the region.",
    kick='Section C · The ground')

# ------------------------------------------------- 12 DIVIDER D
divider_text('Section D', 'From Conversion to Reform',
    'The will that chose the good is set to work',
    "This section is the hinge of the lesson, and it should be taught as an argument the preachers made, not as a coincidence of dates. The convert had chosen. Choosing was the whole event: the will, addressed by preaching and supported by prayer, had turned from sin to obedience in public. The preachers then asked the obvious next question in their sermons and their societies. If a will could choose against drunkenness in a man's own life, why could a town's wills, organized, not choose against the liquor trade itself? The distance from the anxious bench to the pledge table is short, and this section walks it slowly, because the writing task is graded on whether students can walk it themselves.")

# ------------------------------------------------- 13 CONTENT D
content_text('Perfected people, improved institutions',
    ['The same will, turned outward', 'Institutions can be improved by effort', 'Leaving them unimproved becomes a sin', 'Finney organizes his converts into societies'],
    "State the logic as a sequence of three steps and have students copy the sequence, not just the conclusion. First, conversion is an act of the will: the sinner chooses the good. Second, what the will can choose in one life, organized wills can choose in a society: if people can be perfected by effort, institutions can be improved by effort. Third, the duty follows the ability: leaving a known evil unimproved becomes itself a sin, so the convert who does nothing is disobeying, not resting. Finney acted on the sequence at Rochester, organizing his converts into societies for temperance, for moral reform, and against slavery. The society, a voluntary association with officers, dues, and petitions, is the revival's lasting invention.",
    kick='Section D · The logic')

# ------------------------------------------------- 14 CONTENT D2
content_text('The societies and the women who staffed them',
    ['Converts become members, members become organizers', 'Petitions, tracts, and money raised', 'Women the majority of converts', 'Skills learned here run the later movements'],
    "Give the societies their workforce, because the record is plain about who it was. Women formed the majority of converts in town after town, and women staffed the societies those converts founded: circulating the petitions that legislatures received by the bundle, raising the money that printed the tracts, visiting the families the drink statistics described. The work taught skills in public: how to run a meeting, keep a roll, frame a petition, and hold a public standard against ridicule. When Lessons 7 and 8 reach abolition and women's rights, students should recognize the personnel and the methods, because both were trained here, in the temperance and moral reform societies of the 1830s, a full decade before Seneca Falls. Their names fill the membership rolls and petition lists the movements left behind.",
    kick='Section D · The workforce')

# ------------------------------------------------- 15 DIVIDER E
divider_text('Section E', 'Temperance, the First Crusade',
    'Drink first, by a signature',
    "Ask the class why drink came first, before schooling, before the asylum, before slavery in the societies' own order of work, and let them reason from the lesson before you confirm it. Drink was the evil a convert could reach tonight, in his own house, with a pen. It needed no legislature, no tax, and no building. It also stood visibly behind the other miseries the reformers cataloged: the spent wages, the beaten wife, the children without shoes, the worker unfit for the factory's hours. The American Temperance Society, founded at Boston in 1826, made the attack national and gave it a single instrument anyone could use the day he heard of it: the signed pledge. That order, conscience first and law last, is the pattern the whole era repeats.")

# ------------------------------------------------- 16 CONTENT E
content_text('The pledge, and how it hardened',
    ['American Temperance Society, Boston, 1826', 'At first, against ardent spirits only', 'Total abstinence in the 1830s', 'Prohibition by law in the 1840s'],
    "Carry the term in its full form here. temperance: the reform movement against the drinking of alcohol, organized nationally in the American Temperance Society of 1826, which moved from pledges of moderation in the 1820s to campaigns for total abstinence and legal prohibition in the 1840s. Then walk the hardening as a change of carrier as much as of content. The pledge of 1826 bound one conscience against distilled liquor, and left beer, wine, and cider outside it. The teetotal pledge of the 1830s bound the same conscience against every intoxicating drink, enforced by the society around the signer. The campaigns of the 1840s asked the legislature to bind everyone, signer or not, which is the revival method arriving at law.",
    kick='Section E · The remedy')

# ------------------------------------------------- 17 STAT E
stat('1,000,000+', 'members counted by the temperance movement in the 1830s',
    'The pledge becomes the first mass membership campaign of the reform era',
    "Use the size of the number to mark a first in American organizing. The temperance movement counted its members in the millions of signatures its societies claimed through the 1830s, and the Library of Congress's own account of the movement records the American Temperance Society gaining more than a million members nationwide. Treat the figure as the movement's claimed strength rather than an audited roll, and say so to the class. Even discounted, the scale is the fact: no voluntary cause in the republic had ever signed up adherents at anything like this rate. The pledge had shown reformers that a printed card, a local society, and a public signature could build a national constituency, and every later movement in this unit copies the machinery.",
    kick='Section E · The scale')

# ------------------------------------------------- 18 DIVIDER F
divider_photo('mann-port.jpg', 'Section F', 'Mann and the Common Schools',
    ['The same logic, carried into the schoolhouse'],
    "The image is the daguerreotype of Horace Mann by Southworth and Hawes, made about 1850, after the work of this section was done. Mann came to the schoolhouse from the legislature, not the pulpit: a Massachusetts lawyer and state senator who gave up a leading practice in 1837 to become secretary of the new Board of Education, at a salary his friends thought beneath him. What he carried into the office was the revival generation's confidence in a new dress. People could be improved by effort, institutions could be improved by effort, and the institution within every child's reach was the district school, which in 1837 reached most children badly, briefly, or not at all. He served eleven years in the office, and the reports outlived it.")

# ------------------------------------------------- 19 CONTENT F
content_photo('mann-port.jpg', 'The balance wheel of the social machinery',
    ['Secretary of the Board of Education, 1837', 'Annual reports as his instrument', 'Trained teachers, graded classes', 'State supervision of the districts'],
    "Two of the lesson's terms belong to this slide, and the notes carry both in full. Horace Mann: the Massachusetts education secretary whose annual reports from 1837 argued that tax supported common schools were the balance wheel of the social machinery, and who built the first American system of public schools with trained teachers, graded classes, and state supervision. common schools: the tax supported public schools open to all children of a district, which reformers of Mann's generation spread across the northern states in the 1830s and 1840s as the republic's instrument for making citizens out of a diverse and mobile people. Mann's instrument was the annual report, twelve of them, argued like briefs and read far beyond Massachusetts. The report was his pulpit, and he preached from it for eleven years.",
    kick='Section F · The system')

# ------------------------------------------------- 20 CONTENT F2
content_text('The Twelfth Report, 1848',
    ['Education the great equalizer', 'Spread evenly, it draws property after it', 'It prevents being poor', 'A republic of classes is the danger'],
    "Close the Mann argument with his own sentences, which students meet at Station 3. Mann's Massachusetts theory held that all are to have an equal chance for earning, and equal security in the enjoyment of what they earn. Against the lengthening distance between rich and poor that he saw in the manufacturing towns, he set one condition and one promise: if education be equably diffused, spread evenly, it will draw property after it, because an intelligent and practical body of men has never been permanently poor. Note the reach of the claim he is making for a school tax. He is not promising nicer citizens. He is promising that schooling, universal and complete, prevents being poor, and keeps a republic from hardening into the castes of Europe.",
    kick='Section F · The argument')

# ------------------------------------------------- 21 DIVIDER G
divider_photo('dix-port.jpg', 'Section G', 'Dix and the Insane',
    ['Inspect, record, and petition, 1841 to 1843'],
    "The image is the Library of Congress portrait of Dorothea Dix. End the lesson's chain with the reformer who took it furthest from the revival meeting and closest to the statute book. Dix was a Massachusetts teacher, not a preacher, and her instrument was not a sermon or a pledge. Teaching a Sunday school class in the East Cambridge jail in 1841, she found insane men and women locked in unheated cells among the criminals, and she spent nearly two years inspecting the jails and almshouses of her state and writing down what she found, town by town, keeper by keeper, cell by cell. The record she built became the Memorial of January 1843. She began the work at thirty eight, with a teacher's habits of order and a notebook.")

# ------------------------------------------------- 22 CONTENT G
content_photo('dix-port.jpg', 'Cages, closets, cellars',
    ['A Sunday school class in a jail, 1841', 'Two years inspecting jails and almshouses', 'The Memorial, January 1843', 'Defective legislation named as the cause'],
    "The last term, in full. Dorothea Dix: the Massachusetts teacher whose investigations of jails and almshouses in the 1840s exposed the insane confined in cages, closets, and cellars, and whose memorials to legislatures built the first generation of American public asylums. Teach her method as a sequence students can name: inspect in person, record exactly, and petition the body that can act. Her Memorial told the Massachusetts legislature that insane persons were confined in cages, closets, cellars, stalls, and pens, chained, naked, beaten with rods, and lashed into obedience, and it refused the easy blame of keepers. The cause she named was defective legislation, which is why her remedy was a law, not a collection plate. Her notebook extracts, Lincoln, Medford, and Granville among them, are quoted at Station 4 of the activity.",
    kick='Section G · The record')

# ------------------------------------------------- 23 CONTENT G2
content_text('The asylum, and the method repeated',
    ['Worcester asylum enlarged, 1843', 'State after state on the same method', 'Reform reaches people who cannot sign or choose', 'The legislature is the carrier now'],
    "Follow the result and then the reach. The Massachusetts legislature answered the Memorial by enlarging the state asylum at Worcester, and Dix carried the same method, inspect, record, and petition, to state after state for the rest of her working life, building the first generation of American public asylums. Mark what has changed along the lesson's chain. The temperance signer chose for himself. Mann's schoolchild was chosen for by his district. Dix's subjects could not sign a pledge, attend a meeting, or petition anyone, so the reformer's will had to act entirely on their behalf, and its only adequate carrier was the state itself. That is the furthest point the revival's logic reaches in this lesson, and it is reached by 1843.",
    kick='Section G · The result')

# ------------------------------------------------- 24 AT A GLANCE
content_text('The lesson at a glance',
    ['The revival: a choice offered to everyone, from 1800',
     "Finney's method: the right use of the appropriate means",
     'The burned-over district: reform grows where revival ran hottest',
     'Temperance first: the pledge of 1826, hardening toward law',
     'Schools and the asylum: Mann 1837 to 1848, Dix 1843'],
    "This slide mirrors the closing table in the guided notes, The Lesson at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The five lines are the lesson's measured answer to its question. Revival produced reformers because its teaching made the will the instrument of salvation and then of society: a choice offered to everyone at the camp meeting, a method stated by Finney in 1835, and ground in the burned-over district where the choosing never stopped. What they set out to fix first was drink, by the pledge of 1826. By 1848 the same logic had built a school argument and an asylum, and its carrier had widened from the signer to the state.",
    kick='Review')

# ------------------------------------------------- 25 VOCAB 1
vocab('Words for the revival', [
    ('Second Great Awakening', 'the revival that taught every person could choose salvation, and sent converts to reform'),
    ('Charles Grandison Finney', 'the Rochester preacher of 1830 and 1831, conversion as an act of the will'),
    ('burned-over district', 'western and central New York, swept so often it had no fuel left to burn'),
    ('temperance', 'the movement against drink, organized nationally in 1826, pledge to prohibition')],
    "These definitions match the guided notes word for word. Second Great Awakening: the evangelical revival that swept the United States from the turn of the century into the 1840s, carried by camp meetings and itinerant preachers, which taught that every person could choose salvation and sent millions of converts toward the work of reforming society as well as themselves. Charles Grandison Finney: the revival preacher whose Rochester meetings of 1830 and 1831 became the model of the new evangelism, who preached that conversion was an act of the sinner's own will and organized his converts into the temperance, antislavery, and moral reform societies of the age. burned-over district: the region of western and central New York swept so often by revival and reform that preachers said it had no fuel left to burn, the seedbed in the 1830s and 1840s of abolitionism, women's rights, temperance crusades, and new religious movements. temperance: the reform movement against the drinking of alcohol, organized nationally in the American Temperance Society of 1826, which moved from pledges of moderation in the 1820s to campaigns for total abstinence and legal prohibition in the 1840s.")

# ------------------------------------------------- 26 VOCAB 2
vocab('Words for the builders', [
    ('Horace Mann', "Massachusetts education secretary from 1837, the common school's great advocate"),
    ('common schools', "tax supported public schools open to all a district's children"),
    ('Dorothea Dix', 'the teacher whose memorials built the first public asylums')],
    "Three more terms, again matching the guided notes exactly, and students copy them as written. Horace Mann: the Massachusetts education secretary whose annual reports from 1837 argued that tax supported common schools were the balance wheel of the social machinery, and who built the first American system of public schools with trained teachers, graded classes, and state supervision. common schools: the tax supported public schools open to all children of a district, which reformers of Mann's generation spread across the northern states in the 1830s and 1840s as the republic's instrument for making citizens out of a diverse and mobile people. Dorothea Dix: the Massachusetts teacher whose investigations of jails and almshouses in the 1840s exposed the insane confined in cages, closets, and cellars, and whose memorials to legislatures built the first generation of American public asylums.")

# ------------------------------------------------- 27 SYNTHESIS
content_text('Synthesis: the will, organized',
    ['Salvation offered as a choice', 'The choice trained the will to work', 'The work organized into societies', 'Drink first, then the schoolhouse, then the asylum',
     'The carrier widened, signer to society to state'],
    "Draw the lesson together by answering the lesson question in full sentences students can borrow. Why did revival produce reformers? Because it located the power to change in the human will, announced that power to everyone in the clearing, and trained it in public decisions until standing still felt like disobedience. A movement built on that teaching does not end at the church door; it organizes, and its organizations pick up the evils within reach in order. What did they set out to fix first? Drink, in 1826, because a pledge needed nothing but a pen. Then the schoolhouse, because an ignorant republic could not stay equal. Then the asylum, because the people in the cages could wait for no one's conversion but the legislature's.",
    kick='Synthesis')

# ------------------------------------------------- 28 EXIT
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.15, 11.5, 1.6, 'Answer the question, from the records',
     size=36, color=CREAM, font='Georgia', leading=1.15)
text(s, 0.9, 2.55, 11.5, 1.1, ['Why did revival produce reformers, and what did they',
                               'set out to fix first? Build from the documents.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Reform File: five records, a ledger, and a verdict'),
        ('Notebook', 'Notebook page: broken, remedy, carrier, and one paragraph'),
        ('Quick check', "The Will and the Remedy: Finney, Mann, and Dix at work"),
        ('Writing', 'Why Did Revival Produce Reformers? Argued from the file')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, "Exit ticket: Finney's teaching in one sentence, the first evil and its 1826 organization with the remedy's two later stages, and the lesson question in two or three sentences.",
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Reform File, runs five records: Finney's Lectures on Revivals of Religion, Lecture I, quoted from the 1835 edition; a labeled teaching summary of the temperance pledge, with Currier's Drunkard's Progress print of 1846 as its picture argument; Mann's Twelfth Annual Report of 1848, quoted from the Life and Works edition; Dix's Memorial of 1843, quoted from the transcription the class packet names; and a labeled teaching summary of the camp meeting. Students keep a ledger of what must be fixed first and who is asked to carry the remedy, and close with a verdict on the lesson question. The quick check works Finney's two sentences against Mann's and Dix's. The exit ticket asks for Finney's teaching in one sentence, the first evil with its organization and stages, and the lesson question answered in two or three sentences.")

dc.save(OUT)
