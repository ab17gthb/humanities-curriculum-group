#!/usr/bin/env python3
"""Colonial America Lesson 4 deck, "New England: Covenant and
Community," built to the approved system: image-led slides, fragments
only on screen, comprehensive speaker notes, full lesson + vocabulary
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


def content_photo_s(img, title, items, note, kick=None, size=23):
    s = slide(CREAM)
    photo_right(s, img)
    if kick: kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95 if kick else 0.8, 6.9, 1.2, title, size=31, color=NAVY, font='Georgia', leading=1.05)
    frags(s, items, y=2.15 if kick else 2.0, size=size)
    notes(s, note)
    return s

# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'COLONIAL AMERICA · LESSON 4', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'New England: Covenant and Community', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Plymouth, Massachusetts Bay, and Salem, 1620 to 1692', size=17, color=POWDER)
notes(s, "The painting shows the Mayflower at anchor in Plymouth Harbor in 1620, by William Halsall, painted in 1882 and held by the Pilgrim Hall Museum; it is a later artist's view, and students should be told so at the start, because this lesson works from records, not from pictures made centuries later. Open with the two foundings, kept distinct all hour. Plymouth in 1620 was a small Separatist colony that made its government by a compact signed aboard ship. Massachusetts Bay from 1630 was a far larger Puritan migration that meant to build a model godly commonwealth. The lesson follows the guided notes, sections A through G, from the compact to Connecticut's written frame of 1639, through the wars with Native nations, and ends at Salem in 1692, where the community's own habits of watching turned inward.")

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("What kind of community did New England's settlers mean to build, and who could belong to it?", {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the meeting of Europe, Africa, and the Americas remake all three worlds, and what kind of society grew up in England\u2019s colonies?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Read the question in its two halves and keep both halves alive all hour. The first half asks about design: the settlers of Plymouth and Massachusetts Bay were unusually deliberate founders who wrote down, in a compact, a sermon, and a frame of government, exactly what kind of community they meant to build. Students can therefore answer the first half from documents rather than from guesses. The second half asks about the boundary: who could belong, on what terms, and who stood outside however long they lived inside the town lines. Every section of the lesson presses that second question. Settlers signed or did not sign, were examined or not examined, voted as freemen or lived unrepresented, dissented and were banished, or, at Salem, belonged in good standing and were hanged anyway.")

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Two foundings, one boundary, seventy years', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'Plymouth: a compact signed aboard ship', '1620, government by consent, men signing'),
        ('B', 'Massachusetts Bay: a city upon a hill', "1630, Winthrop's Modell of Christian Charitie"),
        ('C', 'The town they built', 'Meetinghouse towns, schools, long lived families'),
        ('D', 'Watched by their neighbors', 'Covenant discipline, freemen voting, dissent as danger'),
        ('E', 'The dissenters: Williams and Hutchinson', 'Banished 1636, tried 1637'),
        ('F', 'Widening the frame, and war', 'Fundamental Orders 1639, Mystic, King Philip\u2019s War'),
        ('G', 'Salem, 1692', 'Spectral evidence, nineteen hanged, repentance')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This slide is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A is Plymouth and the Mayflower Compact. Section B is Massachusetts Bay and Winthrop's sermon. Section C walks the town the settlers built, and section D the discipline inside it. Section E follows the two great dissenters, Roger Williams and Anne Hutchinson. Section F takes up Connecticut's Fundamental Orders and then the wars, the Pequot War and King Philip's War, stated plainly. Section G closes at Salem in 1692. Tell students the summary table at the end of their guided notes asks them to rebuild this map stage by stage, naming for every stage the rule of belonging and who stood outside it or paid for it.")

# 4 SECTION A DIVIDER
divider_photo('compact-port.jpg', 'Section A', 'Plymouth: A Compact Signed Aboard Ship',
              ['The signing of the compact as a later artist imagined it.', 'Painting by Jean Leon Gerome Ferris, Library of Congress.'],
              "The picture is Jean Leon Gerome Ferris's painting of the signing of the Mayflower Compact, printed by the Detroit Publishing Company and held by the Library of Congress. No image of the signing was made in 1620, and the painting should be introduced as an imagining, useful for the scene it sets and worthless as evidence. What survives is the document itself, a short paragraph that students will read entire at Station 1 of the activity. Set the problem the compact answered. The Mayflower had come to anchor off Cape Cod, north of the Virginia territory named in the company's patent, and some passengers, the travelers the Pilgrims called Strangers, argued openly that once ashore they would owe obedience to nobody, since no patent covered the place. The compact was written to close that gap before anyone landed.")

# 5 PLYMOUTH
content_photo_s('landing-port.jpg', 'A government made before landing',
             ['November 1620: anchored off Cape Cod',
              'Landed outside their patent',
              'Forty-one men sign before landing',
              'A civil Body Politick, by consent',
              'Half the company dies that winter'],
             "Walk the document's logic slowly, because it is the first act of self-government in the unit and students meet it again in the Founding unit. The signers call themselves loyal subjects of King James; consent here works inside loyalty, not against it. They covenant and combine themselves together into a civil Body Politick for their better ordering and preservation, and they promise all due submission and obedience to the just and equal laws the body will frame for the general good of the colony. Note who performs the act: forty-one adult men, Pilgrims and Strangers together, which makes the compact broader than a church covenant and narrower than the company aboard. Women, children, and servants would be governed by laws they had no hand in making. The engraving beside the text shows the landing at Plymouth as Joseph Andrews engraved it in 1869 after Peter Frederick Rothermel, another later imagining, held by the Library of Congress.",
             kick='A · Plymouth')

# 6 STAT 41
stat('41', 'men signed the Mayflower Compact',
     'November 1620 · Pilgrims and Strangers together, aboard the Mayflower off Cape Cod',
     "Let the number carry its two lessons at once. Forty-one is small: a shipload of men, meeting no legislature, receiving no charter for the place they stood, made a government by signing their names, and that act of consent is why the compact is remembered. Forty-one is also a boundary: the Mayflower carried about one hundred and two passengers, and the majority of the people aboard, all the women and children and the servants, did not sign. The government they would live under for the rest of their lives was made by fewer than half the adults in the company, and by none of the women. Ask students to hold both facts without letting either cancel the other, because the whole lesson runs on that double vision: New England's founders widened consent further than most governments of their century, and drew its line where their century expected it drawn.",
     kick='A · Plymouth')

# 7 SECTION B DIVIDER
divider_photo('mayflower-port.jpg', 'Section B', 'Massachusetts Bay: A City upon a Hill',
              ['The Mayflower in Plymouth Harbor, by William Halsall, 1882.', 'Pilgrim Hall Museum, via Wikimedia Commons.'],
              "Section B changes scale. Plymouth was one ship and about a hundred people. Massachusetts Bay was a fleet, a charter carried across the Atlantic in the settlers' own hands, and some twenty thousand migrants over the 1630s, the largest English migration of the century's first half. Its leaders were Puritans, English Protestants who sought to purify the Church of England of Catholic practices; unlike the Pilgrims, they had not separated from that church in name, and they said so. Their purpose was exemplary rather than separatist: build a purified church and commonwealth in New England, and let England, watching, copy the model. That watching is the section's key. John Winthrop's lay sermon aboard the Arbella in 1630, A Modell of Christian Charitie, told the settlers before they landed what the model required of them and what failure would cost.")

# 8 MODELL
content_text("Winthrop's Modell of Christian Charitie, 1630",
             ['God made some rich, some poor, and bound them together',
              'Knit together in this work, as one man',
              'Superfluities surrendered for others\u2019 necessities',
              'A city upon a hill: the eyes of all people upon us',
              'Fail, and the colony becomes a byword to the world'],
             "Teach the sermon as a social design, not as a slogan, because later centuries have worn its famous sentence smooth. Winthrop begins from inequality and calls it God's ordering: some must be rich, some poor, some high, others mean and in submission. The obligation runs across the ranks. The rich are stewards, bound to abridge themselves of their superfluities for the supply of others' necessities; the whole company must entertain each other in brotherly affection, rejoice together, mourn together, labor and suffer together. Then the warning that gives the design its enforcement: they shall be as a city upon a hill, the eyes of all people upon them, and if they deal falsely with God in the work, he will withdraw his help and make them a story and a byword through the world. Section D shows what a community does to itself when it believes the world and God are watching it.",
             kick='B · Massachusetts Bay', size=23)

# 9 STAT 4000
stat('4,000', 'souls in Massachusetts Bay by 1634',
     'Winthrop\u2019s own count in his letter to England: \u201cabout 4000 souls & upward\u201d, in good health',
     "The number comes from Winthrop himself, writing to Nathaniel Rich in England in 1634, and students should hear it as a governor's report with a governor's purpose: Winthrop was encouraging more Puritans to come, and his letter stresses health, fish, crops, and orderly government, freemen choosing magistrates every year and churches governed by their congregations. Four thousand souls in four years, against Plymouth's hundred, measures the difference between the two foundings. Then read the letter's last line about the Native peoples of the place, which the activity and the writing task both use, and read it without softening it: the natives, Winthrop wrote, are near all dead of the smallpox, so the Lord had cleared the colonists' title to what they possessed. A modern reader watches a governor convert an epidemic that emptied Native villages into a deed of title, in one sentence, and students should be asked what that sentence assumes about whose land Boston was.",
     kick='B · Massachusetts Bay')

# 10 SECTION C DIVIDER
divider_text('Section C', 'The Town They Built',
             'Tight farming towns around a meetinghouse, land to families, schools by law.',
             "Section C slows down to describe the built community, because the discipline of section D only makes sense inside the town that carried it. Compare the shape with Lesson 3's Chesapeake as you teach. Virginia scattered its settlers along rivers on tobacco plantations, and its people died young in a fever country. New England planted compact towns: a meetinghouse at the center, house lots around it, fields beyond, and land granted broadly to families rather than concentrated in great estates, so the colony filled with small freeholders. Families crossed whole, so the sex ratio balanced early, children were many, and New Englanders lived longer than Chesapeake settlers by a generation. Each town ran much of its own life through the town meeting, and each congregation chose its own minister. In 1647 Massachusetts ordered every town of fifty households to maintain a school, so that children could read Scripture, the seed of New England's famous literacy.")

# 11 TOWN
content_photo_s('hubbard-map-port.jpg', 'Towns around a meetinghouse',
             ['Families settle together',
              'Land granted broadly to households',
              'Town meeting runs town affairs',
              'Congregations choose their own ministers',
              '1647: a school in every larger town'],
             "The map beside the text is John Foster's woodcut map of New England, printed at Boston in 1677, the first map printed in English America, drawn for William Hubbard's account of the wars of 1675 and 1676. It is oriented with west at the top, so Boston and Salem stand along the lower right and Hartford and Windsor at the upper left, and students should find those names before anything else is said about it. Every labeled town on the map is the kind of community this section describes: a gathered settlement of families around a meetinghouse, its minister paid from taxes levied on everyone in the town, member or not. Point out what the town form purchased. Schools, poor relief, roads, and a militia all ran through institutions a family joined by moving in. The same closeness that delivered those goods delivered the watching of section D: in a town built this tight, a neighbor's conduct was public business by design, and anonymity was not on offer at any price.",
             kick='C · The town')

# 12 SECTION D DIVIDER
divider_text('Section D', 'Watched by Their Neighbors',
             'A covenant people under watch: by the world, by God, and by each other.',
             "Section D names the discipline inside the design, and its root idea is the covenant, the term students must carry out of this lesson word perfect. In Puritan belief a covenant was a solemn agreement with God that bound a church or a whole community to live by his laws and brought his judgment if they failed. Hold on the consequence: judgment fell on the community, not only on the sinner, so a neighbor's private sin was a public danger, like rot in a shared hull. That single belief explains the examination of church members, the admonishing of the straying, the taxing of everyone for the minister, and the courts' treatment of religious offenses as breaches of the peace. It also explains why dissent frightened magistrates out of proportion to any army a dissenter could raise. A tear anywhere threatened the whole fabric, because God read the fabric whole.")

# 13 WATCHED
content_text('The discipline inside the covenant',
             ['Churches examine members before admitting them',
              'Members admonished, the unrepentant expelled',
              'Only male church members vote as freemen',
              'Everyone pays the tax that supports the minister',
              'Dissent reads as a tear in the covenant itself'],
             "Give students the machinery concretely. A candidate for church membership stood before the congregation and gave an account of God's work on his or her soul, and the members voted. Members who strayed were admonished in stages; the unrepentant were expelled, which in a town society meant losing the community that fed, buried, and vouched for you. Political membership was narrower still: only male church members were admitted freemen, and only freemen voted for the governor and magistrates or sat in the General Court. Meanwhile the minister's salary came from a tax on every household in the town, dissenter and member alike, so a person could be required to pay for preaching he was forbidden to answer. Ask the class to state the system's own defense before criticizing it: a city upon a hill, watched by God and England, could not shrug at conduct its covenant said would bring judgment on all. Section E tests that defense against two people it expelled.",
             kick='D · The discipline', size=23)

# 14 SECTION E DIVIDER
divider_text('Section E', 'The Dissenters: Williams and Hutchinson',
             'One banished for what he said about land and worship, one tried for what she taught about grace.',
             "Section E puts the covenant's boundary under load, in the two cases the colony itself recorded most fully. Roger Williams and Anne Hutchinson did not agree with each other about much, and they were not allies; what they shared was a refusal to stop at the line the magistrates drew, and a colony that answered both with exile. Present Williams first, since his case came first and its stakes were the widest: his teaching reached beyond worship to the colony's legal existence. Then Hutchinson, whose meetings drew crowds in Boston itself and whose trial the General Court kept in its own words. In both cases students should listen for what the colony said it was defending. The magistrates' language is consistent across the two records: peace, order, and the covenant's fabric, never mere preference. The dissenters' language is also consistent: conscience, land honestly bought, and grace that no minister could mediate or withhold.")

# 15 WILLIAMS
content_text('Roger Williams: the charter itself challenged',
             ['A Salem minister questions the king\u2019s grant',
              'Native land could be bought, not granted away',
              'Government cannot compel worship',
              'Banished in 1636, he walks south in winter',
              'Providence founded on soul liberty'],
             "Williams's two teachings should be stated separately, because students habitually merge them into a general plea for tolerance and lose the sharper one. The first was legal and explosive: the king of England had no right to grant land he did not own, Native land could only be acquired by purchase from its Native owners, and therefore the Massachusetts charter, the document the whole colony stood on, rested on theft. The second was theological: civil government had no commission to compel worship, and forced worship was an offense to God rather than a service to him. Banished in the winter of 1636, Williams bought land from the Narragansett sachems Canonicus and Miantonomi, practicing the purchase his teaching required, and founded Providence. Rhode Island, the colony that grew from it, practiced the religious toleration his name now carries in the lesson's vocabulary, and it sheltered the next dissenter as well.",
             kick='E · The dissenters', size=23)

# 16 HUTCHINSON
content_text('Anne Hutchinson: tried at Newton, 1637',
             ['A Boston midwife holds meetings in her home',
              'Salvation by grace, not by a covenant of works',
              'The ministers themselves are put on trial',
              '\u201cI hear no things laid to my charge\u201d',
              'Banished; killed in New Netherland in 1643'],
             "Hutchinson's case is the lesson's closest reading exercise, because the record is a transcript and students can watch power work line by line. Governor Winthrop's opening charge names her offenses: promoting and divulging the opinions causing the colony's trouble, and keeping a meeting condemned as not tolerable nor comely in the sight of God nor fitting for your sex. Her reply refuses the proceeding's terms before answering any of it: she is called to answer, but she hears no things laid to her charge. Pressed, she demands, Name one, Sir. Behind the procedure stood the theology: Hutchinson taught that salvation came by God's grace directly to the believer, the seal of the Spirit, and that most of the colony's ministers preached a covenant of works, which made the colony's clergy, in her account, ministers of the letter rather than of the Spirit. The court banished her in 1637, the church excommunicated her in 1638, and she was killed in New Netherland in 1643.",
             kick='E · The dissenters', size=23)

# 17 SECTION F DIVIDER
divider_photo('hubbard-map-port.jpg', 'Section F', 'Widening the Frame, and War',
              ['Foster\u2019s map of New England, Boston, 1677:', 'the towns, and the wars that reached them.'],
              "Section F does two things that belong together even though they pull in opposite directions. First it follows the covenant idea west to the Connecticut River, where three towns wrote the Fundamental Orders in 1639, a frame of government made without a royal charter and often called the first written constitution in English America. Then it states, plainly and in the record's terms, what expansion cost the Native nations whose land the towns were planted on: the Pequot War of 1637 and the Mystic massacre, and a generation later King Philip's War. The map on screen is again Foster's 1677 map, and this time students should notice its numbers: Foster keyed the towns with figures marking places attacked in the wars, so the map is itself a war document, a picture of the community and of the violence at its edges in the same woodcut.",
              title_size=38)

# 18 ORDERS
content_text("Connecticut's Fundamental Orders, 1639",
             ['Three river towns act without a royal charter',
              'Freemen choose governor and magistrates yearly',
              'The governor must belong to an approved congregation',
              'The General Court holds the supreme power',
              'Its purpose: the liberty and purity of the Gospel'],
             "The Orders reward slow reading at Station 4 of the activity, so this slide sets the four facts students must be able to produce. In January 1639 the freemen of Windsor, Hartford, and Wethersfield associated and conjoined themselves as one public state or commonwealth, stating two purposes in one breath, civil order and the maintenance of the liberty and purity of the Gospel. The governor and magistrates were chosen each year by the admitted freemen, the governor could not serve two years running and had to be a member of some approved congregation, and the General Court, governor, magistrates, and town deputies together, held the supreme power of the Commonwealth, including the power to admit new freemen. The label first written constitution should be taught as a claim to test, not a title to repeat: the Orders are a written frame created by the governed, and the governed who created it were freemen, a minority of the adults living under it.",
             kick='F · Connecticut', size=23)

# 19 WARS
content_text('Mystic, 1637, and King Philip\u2019s War, 1675 to 1676',
             ['English and allied forces burn the Pequot fort at Mystic',
              'Hundreds of Pequot men, women, and children killed',
              'Fifty years of land loss follow, deed by deed',
              'Metacom builds a coalition to strike back',
              'The deadliest war per capita in the colonies\u2019 history'],
             "State this slide plainly and do not let period language decorate it. In May 1637, in the Pequot War, English soldiers under John Mason, with Mohegan and Narragansett allies who had their own quarrels with the Pequots, surrounded the fortified Pequot village at Mystic before dawn, set it on fire, and killed hundreds of Pequot men, women, and children as they tried to escape the flames. The Pequot nation was then formally dissolved by treaty, its survivors distributed among other nations or enslaved. Thirty-eight years later the pressure that produced Mystic had not relented: English deeds, fences, livestock, and courts had taken Native land season by season for fifty years. Metacom, Massasoit's son, called King Philip by the English, built a coalition of Wampanoag, Narragansett, Nipmuc, and other peoples and struck back in 1675. The war killed a larger share of the colonies' population than any later American war. Metacom was killed in 1676, and Native captives, including his wife and son, were sold into slavery in the Caribbean.",
             kick='F · The wars', size=22)

# 20 SECTION G DIVIDER
divider_photo('salem-port.jpg', 'Section G', 'Salem, 1692',
              ['A trial courtroom as an artist of 1876 imagined it.', 'The records, not the picture, are the evidence.'],
              "The engraving shows a Salem trial courtroom as William A. Crafts published it in 1876, in Pioneers in the Settlement of America; no picture of the trials was made in 1692, and the section should open by saying so, because Salem attracts decoration and this lesson refuses it. Section G teaches the crisis from the records, principally the trial record of Sarah Good, which students read entire at Station 5. Set the sequence in advance. In the winter and spring of 1692, girls in Salem Village who said they were afflicted began naming the people whose spirits tormented them. The first accused were the marginal: an enslaved woman, an elderly widow, and Sarah Good, a homeless beggar. Within months the accusations climbed to church members, a minister, and the edges of the governor's own household, and the watching community of section D found the devil on its own doorsteps.",
              title_size=40)

# 21 SALEM
content_text('The record against Sarah Good',
             ['A homeless beggar woman, among the first accused',
              'An indictment in the court\u2019s own legal language',
              'Neighbors testify: seventeen head of cattle, dead',
              'Spectral evidence the accused cannot answer',
              'Good refuses to confess; she is hanged July 19, 1692'],
             "Read the Good record the way the quick check will ask students to weigh it. The indictment charges her with detestable arts called Witchcrafts and Sorceries against a neighbor who was, in the formula, tortured, afflicted, pined, consumed, wasted, and tormented. The testimony beneath it is the Abbeys': they had taken the homeless Goods into their house out of charity, turned them out for Sarah Good's turbulent and spiteful spirit, and then lost seventeen head of cattle in two years, besides sheep and hogs, and both believed the cattle died by witchcraft. Add the spectral testimony, claims that Good's spirit had visited and tormented the afflicted in forms only they could see, and the structure of the case is complete: a settled grudge, losses after it, and evidence no accused person could ever disprove. Good refused to confess, which at Salem was the choice that led to the gallows; those who confessed were not executed. She was hanged on July 19, 1692.",
             kick='G · Salem', size=22)

# 22 STAT 19
stat('19', 'people hanged at Salem in 1692',
     'And one man, Giles Corey, pressed to death for refusing to plead · The colony then repented',
     "Nineteen is the number the vocabulary definition carries and the number students must produce exactly: nineteen people hanged, and one man, Giles Corey, pressed to death under stones because he would neither plead guilty nor not guilty, which under the law of the time stopped his trial and saved his estate for his family. Five more of the accused died in jail. The crisis did not burn itself out on its own. Increase Mather, the colony's leading minister, argued in print that spectral evidence could not be trusted, that it were better ten suspected witches escape than one innocent person be condemned; Governor Phips dissolved the special Court of Oyer and Terminer; its successor court barred spectral evidence and acquitted nearly everyone before it. Massachusetts later held a public fast of repentance, jurors signed an apology, and the colony eventually reversed the convictions and paid restitution to the families. Teach the repentance as part of the record, the community judging itself by its own standards and finding itself guilty.",
     kick='G · Salem')

# 23 GLANCE
s = slide(NAVY)
kicker(s, 'New England at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Five stages, one boundary', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The founding', 'Plymouth 1620; Massachusetts Bay 1630', 'Consent signed by men alone; Native peoples outside'),
        ('The town', 'Meetinghouse towns; schools from 1647', 'All taxed for the minister; only freemen voted'),
        ('The dissent', 'Williams 1636; Hutchinson 1637', 'Banishment for land doctrine and for grace'),
        ('The wars', 'Mystic 1637; King Philip\u2019s War 1675 to 1676', 'Native land, lives, and power broken'),
        ('Salem', '1692, spectral evidence admitted', 'Nineteen hanged, one pressed, then repentance')]
yy = 2.72
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 0.88
notes(s, "This slide mirrors the final table in the guided notes, New England at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The rows compress the arc. The founding pairs the compact's consent and Winthrop's covenant with their boundary: men signing, Native peoples never offered a signature. The town pairs the meetinghouse community and its schools with its costs: universal taxation for the minister, and a franchise held by freemen alone. The dissent pairs the two banishments with their causes, land and worship in 1636, grace in 1637. The wars row holds Mystic and King Philip's War together as one long account of land. Salem closes the table, the boundary turned inward. Grade the table generously on wording and strictly on pairing: every stage must show the rule of belonging and who stood outside it or paid.")

# 24 SYNTHESIS
content_text('What the community was, and where its line ran',
             ['The design: a covenant people, knit together, watched',
              'The widening: consent at Plymouth, a constitution in Connecticut',
              'The boundary: signature, church door, franchise, gallows',
              'The outside: women, servants, dissenters, Native nations',
              'The lesson: a community is known by who may belong to it'],
             "Draw the lesson together around the question's two halves, because the exit ticket and the writing task both return to them. The design first: New England's settlers built the most deliberate communities in English America, covenant communities of families in gathered towns, bound to God and each other, schooled, churched, and watched. The record of their intentions survives in their own words, which is why this lesson could be taught from five documents. Then the boundary, which the same documents draw with equal clarity. Belonging ran by signature at Plymouth, by examination at the church door, by admission to freemanship at the General Court, and it stopped, for Native nations, at the deed and the gun. When the boundary turned inward at Salem, the community hanged its own on evidence its own standards should have rejected, and then, to its credit and too late for the twenty dead, repented in public. The verdict students write in the activity asks whether the discipline was survival's price or a separate choice; the honest essay holds Plymouth's winter and Salem's courtroom in one argument.",
             kick='Synthesis', size=23)

# 25 VOCAB A
vocab('Words for the founding and the faith',
      [('Mayflower Compact', 'the 1620 shipboard agreement creating government by consent'),
       ('Puritans', 'English Protestants purifying the Church of England'),
       ('covenant', 'a solemn agreement with God binding a community'),
       ('Anne Hutchinson', 'the dissenter tried in 1637 and banished')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. The first term is Mayflower Compact: the agreement signed aboard the Mayflower in 1620 by the Pilgrims, creating a government by the consent of the governed for the Plymouth colony. The second is Puritans: English Protestants who sought to purify the Church of England of Catholic practices and built Massachusetts Bay as a model godly society. The third is covenant: in Puritan belief, a solemn agreement with God that bound a church or a whole community to live by his laws and brought his judgment if they failed. The fourth is Anne Hutchinson: the Massachusetts Bay religious dissenter whose teaching that faith alone brought salvation challenged the colony's ministers and led to her trial and banishment in 1637 and 1638. Test the pairing students most often blur: the compact belongs to Plymouth's Separatists in 1620, the Puritans to Massachusetts Bay from 1630.")

# 26 VOCAB B
vocab('Words for the dissent, the frame, and the crisis',
      [('Roger Williams', 'banished in 1636, founder of Rhode Island'),
       ('Fundamental Orders', 'Connecticut\u2019s written frame of 1639'),
       ('Salem witch trials', 'the crisis of 1692, nineteen hanged')],
      "Three more terms, again matching the guided notes exactly. Roger Williams: the Massachusetts minister banished in 1636 for arguing that the king had no right to grant Indigenous land and that government could not compel worship, who founded Rhode Island on religious toleration. Students should anchor the term to both of its arguments, the land argument as well as the worship argument, because the test reaches for the land argument first. The next term is Fundamental Orders of Connecticut: the document of 1639, often called the first written constitution in English America, that set up Connecticut's government by the votes of its freemen. The last term is Salem witch trials: the crisis of 1692 in Massachusetts in which accusations of witchcraft led to trials that hanged nineteen people and pressed one man to death before the colony repented. With these the full set of seven is complete, in the guided notes, in these slides, and in the review materials.")

# 27 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['What kind of community did New England\u2019s settlers mean to build, and who could belong to it? Argue it from the records, with dates.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Covenant File: five stations from the compact to Sarah Good, and a verdict on discipline, survival, or choice'),
        ('Notebook', 'Notebook page: the five stages charted by date, rule of belonging, who stood inside, and who stood outside'),
        ('Quick check', 'The Compact and the Court: the Foster map, the Plymouth and Connecticut documents, and the dissenters and Salem'),
        ('Writing', 'Who Could Belong: the boundary followed across three records, with the survival claim answered from the documents')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the covenant defined in one sentence, the Fundamental Orders and their supreme power, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Covenant File, runs five stations through the record: the Mayflower Compact, Winthrop's Modell of Christian Charitie, Hutchinson's trial examination, the Fundamental Orders of Connecticut, and Sarah Good's trial record, ending in a verdict on whether the discipline was the price of survival or a separate choice, with the counterclaim answered. The notebook page charts the five stages by date, rule of belonging, who stood inside, and who stood outside or paid. The quick check, The Compact and the Court, tests the Foster map of 1677, the Plymouth and Connecticut sequences, the two dissenters, and the Salem count against blueprint entries 7 and 8. The writing task requires the boundary followed across at least three records and the survival claim answered from the documents. The exit ticket has three parts: the covenant defined in one sentence, the Fundamental Orders with the body holding supreme power and the group alone who voted, and the lesson question in two or three sentences with two facts from the notes.")

dc.save(OUT)
