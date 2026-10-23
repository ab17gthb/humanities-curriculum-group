#!/usr/bin/env python3
"""Colonial America Lesson 7 deck, "Governing, Working, and Arguing
About God," built on the shared deck system: image-led slides,
fragments only on screen, comprehensive speaker notes, full lesson
plus vocabulary coverage. Fonts: Georgia titles, Lato body."""
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
OUT = os.path.join(HERE, '..', 'lesson-07-slides.pptx')

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
text(s, 0.9, 5.30, 11.5, 0.4, 'COLONIAL AMERICA · LESSON 7', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.64, 11.9, 1.0, 'Governing, Working, and Arguing About God', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.52, 11.5, 0.45, 'Assemblies, households, and the Great Awakening', size=17, color=POWDER)
text(s, 0.9, 7.02, 11.9, 0.4, 'Engraving of George Whitefield preaching in the open air, published in Harper\u2019s Weekly, 1865.', size=11, color=POWDER)
notes(s, "Open with the engraving and with the shape of the lesson, because this hour is about a society rather than an event. By the 1730s the English colonies held about a million people who had built three working systems without waiting for London to design them. They governed themselves through elected assemblies that held the power of the purse. They worked and raised children inside households ordered by law, where a father\u2019s authority covered wives, children, servants, and enslaved people. And they argued about God in churches that were about to be split by the greatest religious movement of the century. The engraving shows George Whitefield preaching in the open air, the scene the lesson ends with. The claim to carry through the hour is simple: in each of these three systems, ordinary colonists were practicing how to judge authority for themselves.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.7, 11.5, 3.6, [[('How did colonists govern themselves, raise their families, and argue about God?', {})]],
     size=40, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.5)
text(s, 0.92, 5.75, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the meeting of Europe, Africa, and the Americas remake all three worlds, and what kind of society grew up in England\u2019s colonies?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Read the lesson question in its three parts, because the lesson answers all three and the writing task grades the connection among them. The first part is government: assemblies, a distant Crown, and a printer\u2019s trial in New York. The second part is the household: coverture, children at work, apprentices and servants, and enslaved people building families inside an order that treated them as property. The third part is religion: settled churches, a revival that split them, and an Enlightenment arriving in the same decades through the same printing presses. The unit question runs beneath as the frame. This lesson describes the society the earlier lessons built, at the moment before the imperial wars of the next lesson tested it, and it asks what that society had already taught its people about authority.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Three schools of judgment', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'Government by Practice', 'Assemblies and the purse'),
        ('B', 'Salutary Neglect', 'The policy nobody announced'),
        ('C', 'The Zenger Trial', 'A jury, not a law'),
        ('D', 'The Household', 'Work, law, and the people inside it'),
        ('E', 'The Churches Before the Storm', 'Faith cooled, ministers worried'),
        ('F', 'The Great Awakening', 'Edwards and the fire of revival'),
        ('G', 'Whitefield, Print, and the Enlightenment', 'Two currents, one habit')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Sections A and B cover self-government: the assemblies and the British inattention that let them grow. Section C is the Zenger trial, the colonies\u2019 test case for a free press. Section D goes inside the household, the unit of work and discipline, and Section E sets the religious scene, established churches and cooling faith. Sections F and G cover the Great Awakening, Edwards preaching terror and grace at Northampton and Enfield, Whitefield touring a continent with a printing press behind him, and the Enlightenment standing beside the revival as its rival and partner. The summary table at the end of the guided notes asks students to rebuild this map in their own words.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_photo('assembly-port.jpg', 'Section A', 'Government by Practice',
             ['Elected assemblies in every colony', 'The governor appointed; the money local'],
             "Section A is placed first because it states the political fact the rest of the lesson stands on. By the early 1700s every English colony in America had an elected assembly, a body of representatives chosen by landowning colonists to vote taxes and write laws. The painting shows a colonial assembly in session, the House of Burgesses in Williamsburg as the National Archives holds the image. Above each assembly stood a governor appointed by the Crown or by a proprietor, with a council of leading colonists to advise him. On paper the governor held the stronger hand: he could veto laws, dismiss the assembly, and command the militia. The section\u2019s work is to show students why the paper overstated his power, and why the assembly\u2019s control of money outweighed the governor\u2019s commission over time.")

# ------------------------------------------------------ 5 A ASSEMBLIES
content_text('Assemblies and the power of the purse',
             ['Every colony: an elected assembly',
              'Assemblies vote taxes and write laws',
              'Assemblies vote the governor\u2019s salary',
              'Decade by decade, a larger share of governing'],
             "Work through the four fragments in order and attach the mechanism to each. The assembly was elected, which the governor was not, and its members answered to the landowning colonists who chose them. It voted the colony\u2019s taxes and wrote its laws, the two ordinary instruments of government. The decisive fragment is the third. The governor\u2019s salary, and the money for roads, forts, and officials, came to him only when the assembly voted it, so the man sent to govern began every year as a petitioner asking the governed for funds. Assemblies learned to delay salary bills, to cut them, and to attach conditions to them. Decade by decade, that yearly bargaining became a standing share of governing, and the men who sat in Williamsburg, Boston, and Philadelphia learned politics by practicing it, not by reading about it in London\u2019s instructions.",
             kick='A · Government by practice')

# ------------------------------------------------- 6 SECTION B DIVIDER
divider_text('Section B', 'Salutary Neglect',
             'The policy nobody announced, named a generation later by Edmund Burke.',
             "Section B answers the obvious question Section A raises: why did Britain allow this to happen? The answer is not a grant and not a plan. Through much of the early 1700s the British government attended to wars and politics in Europe, to party struggles at home, and to the debts those wars left behind. No minister announced a policy of leaving the colonies alone, and no law granted them self-government. Distance did the rest of the work. An ocean crossing took weeks, instructions arrived late, and royal officials in America drew salaries voted by the assemblies they were sent to oversee. Edmund Burke gave the practice its name in Parliament a generation later. Teach students to hold both halves: the neglect was real in its effects and imaginary as a policy, since nobody in London had ever voted for it.")

# ------------------------------------------------------ 7 B PRACTICE
content_text('How neglect worked in practice',
             ['Britain attends to Europe: wars, parties, debt',
              'No law grants self-government',
              'Instructions cross the ocean in weeks',
              'Officials draw salaries assemblies vote'],
             "Take the four fragments one at a time, because each one removes a possible supervisor. The first removes attention: Britain\u2019s ministers had European wars and domestic politics enough to fill every cabinet meeting, and colonial administration sank down the agenda. The second removes legal design: because no statute created the arrangement, no statute supervised it, and the assemblies\u2019 growing share of governing rested on custom rather than on a charter anyone in London reviewed. The third removes speed: a governor who wrote home for instructions waited weeks for an answer written to a situation already changed. The fourth removes independence: the royal official on the scene often held colonial property and always needed the assembly\u2019s votes for his salary. The result was a generation of colonists for whom self-government was not a theory of rights. It was the ordinary way their towns and colonies ran.",
             kick='B · Salutary neglect', size=24)

# ------------------------------------------------- 8 SECTION C DIVIDER
divider_photo('press-port.jpg', 'Section C', 'The Zenger Trial',
             ['A printer jailed in 1734', 'A jury decides in August 1735'],
             "Section C moves from practice to principle, from how colonists governed to what rights they claimed while doing it. The photograph shows a colonial printing press of the kind John Peter Zenger worked, the press Stephen Daye brought to Massachusetts in the 1630s, photographed by the Library of Congress. Zenger printed the New-York Weekly Journal, which attacked New York\u2019s royal governor, William Cosby, over his salary claims and his removal of judges. In November 1734 Zenger was jailed for seditious libel and held for about nine months awaiting trial. His newspaper kept publishing, run by his wife Anna from the jail\u2019s neighborhood, which students should register: the prosecution had already failed to silence the press it was trying. The trial came in August 1735, and it produced the colonies\u2019 most retold courtroom story.")

# ------------------------------------------------------ 9 C TRIAL
content_text('The trial of John Peter Zenger, 1735',
             ['The charge: seditious libel against Governor Cosby',
              'The law then: truth was no defense',
              'Hamilton admits the printing, argues the truth',
              'The jury acquits, against the judge\u2019s instruction'],
             "Narrate the trial through the four fragments, and use Station 1 of the activity for Hamilton\u2019s words themselves. Zenger\u2019s first lawyers were disbarred for challenging the judges\u2019 commissions, so the defense fell to Andrew Hamilton of Philadelphia, the most famous lawyer in the colonies, an old man who traveled to New York for the case. He stunned the court by confessing that Zenger had printed and published the papers, giving away the only fact the prosecution had to prove. Then he argued the principle the law denied: that true statements could not be libel, and that the jury, not the judge\u2019s instruction, should judge both the fact and the law of the case. The jury acquitted after a short deliberation. Crowds cheered the verdict in the street, and printers across the colonies printed the story.",
             kick='C · The Zenger trial', size=24)

# ------------------------------------------------------ 10 STAT 9
stat('9', 'months Zenger spent in jail awaiting trial',
     'Arrested November 1734 · Tried and acquitted August 1735',
     "Let the number stand as a measure of what the prosecution could still do, because the honest qualification of this lesson depends on it. Zenger was arrested in November 1734 and held about nine months before his trial, in part because the bail set for him was more than a printer could raise. During those months the government had its way with him completely: his shop was raided in effect, his earlier lawyers were disbarred, and he edited his newspaper through his wife from jail. The acquittal in August 1735 did not repay those nine months, and it did not change the law that had jailed him. Teach the stat as the counterweight inside the celebration. The colonies remembered the verdict as a landmark, and the same record shows a governor able to imprison a critic for three seasons on a charge a jury would not sustain.",
     kick='C · The Zenger trial')

# ------------------------------------------------- 11 SECTION D DIVIDER
divider_text('Section D', 'The Household',
             'The unit of work and discipline, where most colonists were governed.',
             "Section D goes indoors, to the institution where most colonists actually experienced authority every day. A colonial household could hold a married couple, their children, apprentices learning a trade, indentured servants working out their terms, and enslaved people held as property, all eating, working, and sleeping under one roof and one legal head. The law gave the father authority over every person in that list. This section should be taught as a description of a working order, not as a backdrop. The household produced most of the colony\u2019s food, cloth, and goods. It educated most children, nursed most of the sick, and disciplined most of the young. Its legal rules tell us who held standing in that order. Its daily work tells us who actually carried it, which was a wider set of people than the law credited.")

# ------------------------------------------------------ 12 D COVERTURE
content_text('Coverture and the working reality',
             ['A wife\u2019s legal identity covered by her husband\u2019s',
              'No property, no contracts, no suits in her own name',
              'Yet women ran farms, shops, and taverns, and taught',
              'Widows regained standing, property, and wills'],
             "Teach the legal rule first and the working reality second, and insist that both are the record. Under coverture, a married woman\u2019s legal identity was covered by her husband\u2019s: she could not hold property in her own name, sign contracts, or sue in court, and her earnings belonged in law to him. Against that rule set the work the documents show. Women ran farms during long absences, kept shops and taverns, traded in their own neighborhoods, taught children, and managed the labor of servants and the enslaved. Station 5 of the activity gives students a widow\u2019s will, Judith Johns of Goochland County in 1735, dividing her estate equally among her children. Widowhood restored the standing marriage had removed, and widows across the colonies used it to hold property, run trades, and direct their households\u2019 goods by will.",
             kick='D · The household', size=24)

# ------------------------------------------------------ 13 D PEOPLE INSIDE
content_text('The people inside the household',
             ['Children worked young; many apprenticed out',
              'Servants worked toward freedom dues and land',
              'Enslaved people: families, faiths, and skills kept',
              'New England longevity; Chesapeake early deaths'],
             "This slide names the household\u2019s other members as people working inside the order, and the notes should keep their purposes in view. Children were put to work at tasks sized to them and many left home as apprentices or servants, carrying their labor to another household and learning a trade there. Indentured servants worked out terms of four to seven years toward freedom dues and a chance at land, and their bargains were enforced in courts that also punished them. Enslaved people had no term and no dues. Inside an order that treated them as property they built families across quarters and plantations, kept African faiths, languages, and skills, taught their children, and resisted in ways from slowed work to flight. Regional contrasts close the section: New England families lived longer and schooled their children in towns, while early deaths in the Chesapeake broke families often and left orphans to the courts.",
             kick='D · The household', size=24)

# ------------------------------------------------- 14 SECTION E DIVIDER
divider_text('Section E', 'The Churches Before the Storm',
             'Established churches, tax support, and a faith ministers feared had cooled.',
             "Section E sets the religious scene the Awakening broke into, and it should be taught as a working establishment rather than a decline invented afterward. In New England, town taxes supported Congregational churches and their ministers, and attendance was expected of everyone in town. In the South, the Church of England was established by law across parishes so wide that one minister could barely serve them, and many families lived miles from any service. The middle colonies held the widest mix of faiths in the Atlantic world. By the 1730s ministers across these arrangements shared one worry: that the faith of the founding generations had cooled into habit, that sermons had grown learned and dry, and that commerce filled the week. Their disagreement was over the cure, stricter discipline or a faith felt in the heart.")

# ------------------------------------------------------ 15 E COOLED
content_text('A faith of habit, and two cures proposed',
             ['Tax supported ministers; attendance expected',
              'Wide southern parishes, one minister each',
              'The worry: members attending from habit',
              'Cure one: discipline · Cure two: a felt faith'],
             "Work through the fragments and end on the choice, because the next section is that choice exploding. The establishment was real: ministers were paid from taxes, churches stood at the center of towns, and in New England a family\u2019s standing and its churchgoing were hard to separate. The weakness was also real, and ministers themselves recorded it. Membership could be inherited, sermons could be essays read aloud, and a congregation could sit through both without anything in the hearers changing. The first cure proposed was the older one: catechize the children, discipline the wandering, and restore the practices of the founders. The second cure was new in scale if not in idea: preach for conversion, aim at the heart, and treat faith as something a person must feel and choose. In the mid 1730s that second cure found its preachers, its crowds, and its printing presses, all at once.",
             kick='E · Before the storm', size=24)

# ------------------------------------------------- 16 SECTION F DIVIDER
divider_photo('edwards-port.jpg', 'Section F', 'The Great Awakening',
             ['Northampton, 1734 and 1735', 'Enfield, July 1741'],
             "Section F takes up the revival itself, beginning with its most careful mind. The portrait is Jonathan Edwards, the Northampton minister whose preaching and writing made him the leading theologian of the Awakening in New England. Edwards was no shouting itinerant. He was a Yale educated scholar who read his sermons in a level voice and kept exact records of his congregation\u2019s spiritual state. In 1734 and 1735 a revival filled his town, as longtime churchgoers, young people first among them, came to him in distress and in joy over their souls. Edwards wrote the account of it that carried the news abroad. Teach the pairing that defines him: the most analytical preacher in the colonies produced the movement\u2019s most terrifying sermon, and he did it on purpose, from a doctrine he could state in one sentence.")

# ------------------------------------------------------ 17 F EDWARDS
content_photo('edwards-port.jpg', 'Edwards and the sermon at Enfield',
              ['Faith is not habit or membership',
               'Nothing but God\u2019s pleasure keeps sinners out of hell',
               'A spider over a fire; waters behind a dam',
               'Congregations wept and cried out'],
              "Teach the sermon from Station 2 of the activity, where students read Edwards in his own words. His claim was that nothing keeps sinners out of hell at any moment but the mere pleasure of God: not health, not careful living, not a record of religious duty, all of which he weighed together as no stronger than a spider\u2019s web against a falling rock. The images carried the doctrine into the body: God holding the sinner over the pit as a person holds a spider over a fire, wrath rising like waters behind a dam, a bow bent with its arrow aimed at the heart, the sinner hanging by a slender thread. Hearers at Enfield wept and cried out during the sermon, and the printed sermon, issued in Boston that year, became the most famous sermon in American history. Edwards\u2019s purpose was conversion, and terror was his chosen road to it.",
              kick='F · The Great Awakening')

# ------------------------------------------------------ 18 F SPLIT
content_text('Old Lights and New Lights',
             ['Revivals drew crowds across the colonies',
              'Itinerants preached beyond their own parishes',
              'Old Lights: disorder and false feeling',
              'New Lights: a faith nobody felt is no faith'],
             "The revival\u2019s spread forced every congregation to take a side, and the split is the section\u2019s institutional fact. Itinerant preachers crossed parish lines to preach where they were invited, or where they were not, which broke the settled rule that a minister\u2019s authority ran inside his own parish and no further. Hearers began traveling to hear favored preachers and staying home from their own. Defenders of the older order, called Old Lights, charged the revival with disorder, with judging ministers, and with mistaking bodily effects, fainting and crying out, for the work of God. Its supporters, the New Lights, answered that a faith nobody felt was no faith at all, and that a church of the unconverted was a worse disorder than a noisy meeting. Congregations divided, some split outright, and new churches formed. The argument taught laypeople to evaluate their ministers, which many of them continued to do.",
             kick='F · The Great Awakening', size=24)

# ------------------------------------------------- 19 SECTION G DIVIDER
divider_photo('whitefield-port.jpg', 'Section G', 'Whitefield, Print, and the Enlightenment',
             ['Tours from Georgia to New England', 'The colonies\u2019 first shared celebrity'],
             "Section G closes the lesson with the man who turned local revivals into one colonial event. The portrait is George Whitefield in 1745, painted by Joseph Badger and held by Harvard Art Museums. Whitefield was an English preacher, ordained in the Church of England, who arrived in the colonies in 1739 and toured from Georgia to New England in 1739 and 1740, returning again and again across his life. He had no American parish, no assembly\u2019s salary, and no bishop\u2019s permission for most of the pulpits he filled. What he had was a voice that carried across a field, a genius for publicity learned in the London theater world he had left, and printers happy to sell him. The section pairs him with the Enlightenment, because the two movements shared the same presses and taught the same habit by opposite roads.")

# ------------------------------------------------------ 20 G WHITEFIELD
content_photo('preaching-port.jpg', 'Whitefield on tour, 1739 and 1740',
              ['Churches when they opened; open air when they did not',
               'Crowds in the thousands, beyond any town\u2019s size',
               'His journal, New York, November 1740: fainting, weeping',
               'Franklin printed his works in Philadelphia'],
              "Teach Whitefield from his own journal, which Station 3 of the activity prints from the Oxford Text Archive transcription. In New York on November 1, 1740, he preached twice to very crowded auditories, some hearers fainted in the evening, and the next day the whole congregation was alarmed, with shrieking, crying, weeping, and wailing heard in every corner. He recorded effects the way Edwards recorded doctrine, as evidence the work was real. His method scaled because print scaled it: newspapers announced his schedule town by town, his journals and sermons were printed and sold along the route, and Benjamin Franklin, who printed his works in Philadelphia and became his friend, once measured how far the voice carried and calculated the crowd could exceed thirty thousand hearers. A farmer in Georgia and a merchant in Boston could both claim to have heard the same man, which no colonial experience had offered before.",
              kick='G · Whitefield and print')

# ------------------------------------------------------ 21 G JUDGING
content_text('What the Awakening taught beyond religion',
             ['Hearers judged rival preachers for themselves',
              'Itinerants challenged settled ministers, and survived',
              'Baptists and Methodists multiplied, in the South above all',
              'Black hearers formed churches of their own'],
             "This slide collects the consequences the reading draws, and each fragment is a transfer of judgment downward. Ordinary hearers compared preachers, followed the ones who moved them, and let the others preach to empty benches, a consumer\u2019s discipline applied to the pulpit. Itinerants who defied parish boundaries were denounced and sometimes prosecuted, and they kept preaching, which taught observers that a settled institution\u2019s disapproval was survivable. Denominations that welcomed the revival grew fastest on it: Baptists and Methodists multiplied, especially in the South, where their preachers reached people the wide Anglican parishes had barely served. Black hearers, enslaved and free, heard a message that addressed their souls directly and formed churches and faiths of their own inside the movement\u2019s openings. None of this was a political program. All of it was practice in deciding whose word to trust.",
             kick='G · Whitefield and print', size=24)

# ------------------------------------------------------ 22 STAT 18000
stat('18,000', 'sermons Whitefield preached in his lifetime',
     'An average of about 500 a year, across Britain and seven tours of the colonies',
     "The figure comes from the Christian Classics Ethereal Library\u2019s summary of Whitefield\u2019s life, which counts more than 18,000 sermons across thirty four years of preaching, an average of about five hundred a year or ten a week. Hold the number up as a fact about labor and logistics rather than about fame. Each sermon was an event his audience walked or rode to, in an age without amplification, and most were versions of sermons he had delivered hundreds of times, improving in delivery with every repetition in the way Franklin admired. Seven crossings of the Atlantic stand inside the total. The colonies did not receive a distant celebrity\u2019s reputation. They received the man himself, repeatedly, in town after town, and the repetition is why a shared colonial experience could form around one preacher before any shared politics existed.",
     kick='G · Whitefield and print')

# ------------------------------------------------------ 23 G ENLIGHTENMENT
content_text('The Enlightenment beside the revival',
             ['Reason, observation, and natural law',
              'Reaching the colonies through books, colleges, print',
              'Franklin: experiments, writings, a wider world',
              'Rivals over truth; partners in questioning authority'],
             "Close the content with the pairing the lesson insists on, stated as rivals and partners rather than as one tide. The Enlightenment prized reason, observation, and natural law over tradition and religious authority. It reached the colonies through imported books, through the colleges at Harvard, William and Mary, and Yale, and through the same newspapers and presses that carried Whitefield. Franklin is its local face: a printer who became an experimenter, testing electricity and publishing what he found for readers to judge. The rivalry was genuine. Edwards and the philosophes disagreed about where truth was found, in the awakened heart or in reasoned observation, and said so. The partnership was also genuine. Both currents told colonists that an inherited authority, a minister\u2019s, a governor\u2019s, a tradition\u2019s, had to answer to their own judgment. That is the lesson\u2019s conclusion, and the writing task argues it.",
             kick='G · Whitefield and print', size=24)

# ------------------------------------------------------ 24 VOCAB A
vocab('Words for self-government and revival',
      [('salutary neglect', 'Britain leaving the colonies to govern themselves'),
       ('Zenger trial', 'the 1735 trial; truth argued as a defense to libel'),
       ('Great Awakening', 'the revival movement of the 1730s and 1740s'),
       ('revival', 'a meeting to reawaken faith and convert sinners')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. The first term is salutary neglect: the British practice through much of the early 1700s of leaving the colonies largely to govern themselves while Britain attended to wars and politics in Europe. The second is Zenger trial: the New York trial of 1735 in which printer John Peter Zenger was acquitted of seditious libel after his lawyer argued that true statements could not be libel, a landmark for freedom of the press. The third is Great Awakening: the religious revival movement that swept the colonies in the 1730s and 1740s, emphasizing personal faith and emotional preaching over church tradition and learning. The fourth is revival: a religious meeting or series of meetings meant to reawaken faith and convert sinners, the characteristic gathering of the Great Awakening.")

# ------------------------------------------------------ 25 VOCAB B
vocab('Words for the two preachers and the other current',
      [('Jonathan Edwards', 'Northampton minister of the Enfield sermon, 1741'),
       ('George Whitefield', 'touring preacher of the open air crowds'),
       ('Enlightenment', 'reason and observation over tradition and authority')],
      "Three more terms, again matching the guided notes exactly. The first is Jonathan Edwards: the Massachusetts minister whose preaching, including the sermon Sinners in the Hands of an Angry God in 1741, helped ignite the Great Awakening in New England. The second is George Whitefield: the English preacher whose tours of the colonies during the Great Awakening drew open-air crowds in the thousands and made him the colonies' first shared celebrity. The third is Enlightenment: the European intellectual movement that prized reason, observation, and natural law over tradition and religious authority, reaching the colonies through books, colleges, and print. Keep the two preachers distinct in the notes. Edwards was the settled scholar who wrote the revival\u2019s theology from one pulpit. Whitefield was the itinerant who carried it between colonies, and the Enlightenment is neither of them: it is the rival current that shared their presses.")

# ------------------------------------------------------ 26 SYNTHESIS
s = slide(NAVY)
kicker(s, 'The record at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Governed, worked, argued', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Governed', 'Assemblies under salutary neglect', 'The purse checked the governor'),
        ('Printed', 'The Zenger verdict, 1735', 'A jury refused; the law stood'),
        ('Worked', 'The household under coverture', 'Law credited the head; many hands carried it'),
        ('Believed', 'Edwards and Whitefield, 1734 to 1741', 'Hearers judged preachers themselves'),
        ('Reasoned', 'The Enlightenment in print', 'Inherited authority had to answer')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, The Record at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The five rows compress the argument of the hour. Governed: assemblies held the purse while Britain looked to Europe, and self-government became ordinary practice. Printed: a New York jury refused to convict a printer in 1735, changing no law and changing what colonists expected a jury and a newspaper could do. Worked: the household ran the colony\u2019s production under a legal order that credited its head and subordinated wives, children, servants, and enslaved people, whose work and families filled the record anyway. Believed: revival preachers put every hearer in the position of judge. Reasoned: the Enlightenment asked the same of every reader. The next lesson takes this practiced, self-governing society into a war for the continent.")

# ------------------------------------------------------ 27 EXIT
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['How did colonists govern themselves, raise their families, and argue about God? Answer it through one practice from each of the three fields, and say what each practice trained.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Conscience File: Hamilton, Edwards, Whitefield, the purse, and a widow\u2019s will'),
        ('Notebook', 'Notebook page: the society in five stages, from assemblies to the two currents'),
        ('Quick check', 'Self-Government and Revival: Hamilton read closely, the sequence tested'),
        ('Writing', 'Ready to Judge Authority: one force, three documents, the counterclaim answered')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: salutary neglect defined, Hamilton\u2019s argument and the law unchanged, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by handing the lesson to the work. The activity, The Conscience File, runs five stations: Hamilton\u2019s summation from the audited bank record, Edwards\u2019s sermon from the same bank, Whitefield\u2019s journal from the Oxford Text Archive transcription, a teaching summary of the assembly\u2019s purse labeled as a summary on its face, and the 1735 will of Judith Johns, ending with a table of authority claimed and questioned and a defended verdict among self-government, print, and revival. The notebook page holds the five stages from assemblies to the two currents. The quick check, Self-Government and Revival, tests close reading of Hamilton against the lesson\u2019s background sequence. The writing task, Ready to Judge Authority, requires the chosen force stated in practice first, three dated pieces of evidence, and an answer to the strongest fact against it, including coverture as the standing limit on all three forces. The exit ticket has three parts, as printed at the end of the guided notes.")

dc.save(OUT)
