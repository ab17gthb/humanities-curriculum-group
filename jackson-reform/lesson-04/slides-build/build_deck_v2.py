#!/usr/bin/env python3
"""Jackson and Reform Lesson 4 deck, The Bank War and the Panic,
built to the approved system: image-led slides, fragments only on screen,
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

def content_photo_s(img, title, items, note, kick=None, size=21):
    s = slide(CREAM)
    photo_right(s, img)
    if kick: kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95 if kick else 0.8, 6.9, 1.2, title, size=31, color=NAVY, font='Georgia', leading=1.05)
    frags(s, items, y=2.12 if kick else 2.0, size=size, gap=11, leading=1.2)
    notes(s, note)
    return s

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'JACKSON AND REFORM · LESSON 4', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Bank War and the Panic', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'A veto, a removal, a boom, and the bill, 1832 to 1840', size=17, color=POWDER)
notes(s, "The title image is a five dollar note of the Bank of the United States dated 1829, the paper currency at the center of this lesson, held by the Baker Library at Harvard Business School and reproduced from its public domain scan. Open by holding the two halves of the lesson together. The first half is a political fight between named men, Andrew Jackson, Nicholas Biddle, and Henry Clay, over one chartered corporation. The second half is what that fight did to people who appear in none of its portraits: the borrowers of the pet bank boom and the workers of the Panic of 1837. The lesson question asks whether the Bank was a public good or a private monster, and who paid when it fell, and students should hear both halves of that question in the first minute.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("Was the Bank a public good or a private monster, and who paid when it fell?", {})]],
     size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ("What did democracy mean in Jackson's America, who was it for, and what did the era's reformers claim it still owed?", {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "The lesson question is built in two parts, and the grading follows the build. Public good or private monster asks students to judge the Second Bank from its conduct, not from its reputation: the same institution that kept the currency sound also contracted the nation's credit as a political weapon, and both facts are in the documents at Stations 1 and 3. Who paid when it fell turns the judgment toward consequences: the Bank's charter expired in 1836, the panic arrived in May 1837, and its costs landed on indebted farmers, failed merchants, and wage workers who had never held a Bank share. The unit question stands behind both parts, because Jackson made the Bank War democracy's own argument, the people's president against a privileged corporation, and the lesson tests what that argument included and what it cost.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'A regulator destroyed, a boom unleashed', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The Bank and what it did', 'Chartered 1816; Biddle regulates the currency'),
        ('B', 'The question forced early', 'Clay and Biddle seek recharter in 1832'),
        ('C', 'The veto', 'July 10, 1832; equal protection against privilege'),
        ('D', 'The deposits removed', 'Pet banks, 1833; censure; King Andrew; Whigs'),
        ('E', "Biddle's answer and the boom", 'Contraction, 1833 to 1834; land bought on paper'),
        ('F', 'The Specie Circular and the turn', 'Gold and silver for land, July 1836'),
        ('G', 'The Panic of 1837 and who paid', 'Suspension, May 1837; independent treasury, 1840')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "The map follows the guided notes section by section. Section A sets out what the Second Bank did: the federal deposits, a national currency, and regulation of the state banks by demanding specie for their notes. Section B shows Clay and Biddle forcing the recharter question four years early in 1832. Section C reads the veto of July 10, 1832. Section D follows the removal of the deposits to the pet banks in 1833, the Senate censure, the King Andrew cartoon, and the Whig Party forming in 1834. Section E covers Biddle's contraction of 1833 and 1834 and the land boom that followed the Bank's fall. Section F reads the Specie Circular of July 1836. Section G closes with the Panic of 1837, its payers, and Van Buren's independent treasury of 1840.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_photo('jackson-port.jpg', 'Section A', 'The Bank and What It Did',
              ['Chartered in 1816, directed from Philadelphia, the Bank', "stood over every borrower in the republic."],
              "The portrait is Andrew Jackson by Ralph Eleaser Whiteside Earl, painted in 1837, the year Jackson left office, and it shows the president as his own side wished him seen: plain, erect, and civilian. Teach the Bank before the fight, because students who meet the institution only through Jackson's charges cannot judge the charges. The Second Bank of the United States was chartered in 1816 for twenty years, held the government's deposits, issued notes that passed everywhere as a national currency, and kept the hundreds of state banks in check by one plain device: it presented their notes for payment in gold and silver, so a bank that lent too freely had to pull in its loans. That is the whole machine. Everything in this lesson is an argument about who should hold it, and whether anyone should.",
              title_size=34)

# ------------------------------------------------------ 5 THE BANK'S WORK
content_text('What the Bank did, 1816 to 1832',
             ['It held the federal deposits and moved the government money.',
              'It issued banknotes that passed as a national currency.',
              'It presented state bank notes for payment in specie.',
              'It forced loose banks to pull in their loans.',
              'It was answerable to stockholders, not to voters.'],
             "Read the five fragments as one institution described twice. The first four are the public work: a single depository for the government's money, a currency a traveler could spend in any state, and a regulator whose discipline no legislature had to vote on because the specie demand did the work automatically. Defenders called that the soundness of the currency, and they were describing something real. The fifth fragment is the democratic objection, and it is equally factual: the officers who ran the machine were chosen by its stockholders, its president served from 1823 without facing an electorate, and its loans and printing contracts could reward friends. Both descriptions were true in 1832. The Bank War happened because the country had to choose which description would govern, and Section B shows who chose the moment of decision.",
             kick='A · The Bank and what it did', size=24)

# ------------------------------------------------------ 6 BIDDLE
content_photo_s('biddle-port.jpg', 'Nicholas Biddle, the regulator',
             ['He was president of the Bank from 1823.',
              'He was a Philadelphia financier of the first rank.',
              'He ran the Bank as manager of the national currency.',
              'He fought for its life with loans and contracts.'],
             "The portrait is Nicholas Biddle by Charles Willson Peale, painted in the sitter's lifetime, and students should note the contrast the two portraits in this lesson set up: Jackson painted plain in 1837, Biddle painted as a gentleman of finance. Biddle was no cartoon villain, and the lesson fails if he becomes one. He was a former diplomat and editor, chosen to head the Bank at thirty seven, and by most accounts a genuinely able central banker before central banking had a name. Under him the Bank's notes were as good as specie and its regulation was steady. His flaw was constitutional rather than financial: he believed the Bank's usefulness placed it beyond the reach of electoral politics, and he was willing to use its economic power, its loans, its contracts, and in 1833 its credit itself, as political weapons. Jackson's veto made exactly that charge. Section E tests it.",
             kick='A · The Bank and what it did')

# ------------------------------------------------------ 7 STAT 20
stat('20', 'years in the charter Congress granted in 1816',
     'The charter ran to 1836 · No decision was required in 1832',
     "State the arithmetic plainly, because the whole crisis turns on it. Congress chartered the Second Bank in 1816 for twenty years, so the charter expired in 1836 and the institution could have been debated then, in an ordinary year, by an ordinary Congress. Nothing required a decision in 1832. The decision came in 1832 because two men wanted it then: Henry Clay, who needed an issue for his presidential campaign, and Nicholas Biddle, who believed an election year protected the Bank. When students ask why the fight happened when it did, the answer is never that the charter ran out. The answer is that the Bank's friends chose the ground, chose it four years early, and lost on it. Keep that sequence in front of the class whenever the veto is described as Jackson picking a fight: on timing, the record runs the other way.",
     kick='A · The Bank and what it did')

# ------------------------------------------------- 8 SECTION B DIVIDER
divider_text('Section B', 'The Question Forced Early',
             'Clay needs an issue, Biddle needs a charter, and both men agree on 1832, four years before any answer is due.',
             "Introduce the trap as a piece of political engineering, because its design explains everything that follows. In 1831 and 1832 Henry Clay was assembling his run for the presidency against Jackson, and the Bank was his strongest ground: popular with merchants, admired by editors, and hated by the president. Clay persuaded Biddle to apply for recharter at once rather than wait for 1836. Their calculation had two horns, and either was supposed to gore Jackson. If he signed, he surrendered his convictions and split his own coalition. If he vetoed, Clay would carry the veto into the election as proof that one man's prejudice had destroyed the nation's finances. Biddle accepted the plan because election years had always protected the Bank. What neither man priced in was Jackson campaigning on the veto itself, which is Section C.")

# ------------------------------------------------------ 9 THE TRAP
content_photo_s('clay-port.jpg', "Clay's calculation, 1832",
             ['The charter had four years left to run.',
              'Clay persuaded Biddle to apply at once.',
              'If Jackson signed, he surrendered his convictions.',
              'If he vetoed, Clay campaigned on the veto.',
              'Congress passed the recharter in summer 1832.'],
             "The image is an engraved portrait of Henry Clay, the Bank's champion in Congress and Jackson's opponent in the election of 1832. Walk the class through the trap's logic slowly, because students tend to remember the veto as the opening move and it was the answer to one. The bill passed Congress in the summer of 1832 and arrived on the president's desk with the campaign already running. Biddle supported the timing with the Bank's resources, including loans that kept friendly newspapers friendly, a fact Jackson's message would not let the country forget. Notice what the design assumed: that the Bank was too useful to attack and its president too respectable to caricature. Both assumptions were reasonable in the politics of 1828. The election of 1832 was a different politics, mass electorate politics, and the next section shows Jackson fighting on the new ground.",
             kick='B · The question forced early')

# ------------------------------------------------- 10 SECTION C DIVIDER
divider_text('Section C', 'The Veto',
             'July 10, 1832. Jackson answers the trap with a message written for the voters, and the election becomes the referendum his enemies designed, with the sides reversed.',
             "Frame the veto as a document before it is an act, because students will read it at Station 1 and its wording does the lesson's analytical work. A veto is ordinarily a short constitutional objection sent back to Congress. Jackson's message of July 10, 1832 was a campaign address in veto form, published in every newspaper in the country, and its audience was the electorate Clay and Biddle had tried to frighten. It made three arguments: that the Bank was unconstitutional despite the Supreme Court's ruling a generation earlier, that its stock and privileges made it a monopoly, and that government granting exclusive privileges made the rich richer at the expense of farmers, mechanics, and laborers. The third argument is the one the country remembered, and it is the one this lesson's question is built from.")

# ------------------------------------------------------ 11 VETO CHARGES
content_text('What the veto charged',
             ['It was unconstitutional, the Court notwithstanding.',
              'Foreign stockholders held much of its stock.',
              'Exclusive privileges made the rich richer.',
              'Farmers, mechanics, and laborers may complain.',
              'Its favors, like the rains, fell on all alike.'],
             "Read the charges in the message's own order of strength. The constitutional charge was the weakest legally, since the Supreme Court had upheld the first Bank's charter in 1819, and Jackson's answer, that each branch must judge the Constitution for itself, was a doctrine students met in the nullification lesson wearing a different uniform. The monopoly charge was the argument with a future: when laws grant titles, gratuities, and exclusive privileges, Jackson wrote, the humble members of society have a right to complain of the injustice of their government. Hold the rains sentence for last and read it aloud. Government confining itself to equal protection, showering its favors alike on the high and the low, the rich and the poor, as Heaven does its rains, would be an unqualified blessing. That sentence, not the banking details, is why the veto survived its decade.",
             kick='C · The veto', size=24)

# ------------------------------------------------- 12 SECTION D DIVIDER
divider_photo('king-port.jpg', 'Section D', 'The Deposits Removed',
              ['The veto was a power the Constitution grants. The removal', "was Jackson's own, and his opponents drew him crowned for it."],
              "The image is King Andrew the First, the anonymous print of 1833 that students read as an argument at Station 2, printed by the Library of Congress from its own impression. Use it to mark the lesson's hinge. The veto of 1832 was fierce but constitutional, and it was ratified by an election. The removal of the deposits in the fall of 1833 was something else: the president ordered the government's money taken out of the bank Congress had chosen to hold it, while Congress was away, over the refusal of his own secretary of the Treasury, whom he dismissed for refusing. That sequence is what moved the opposition's charge from a bad veto to kingship, crown, robes, scepter, and the torn Constitution under the royal feet. The Whig Party, formed the following year, took its very name from the enemies of kings.",
              title_size=34)

# ------------------------------------------------------ 13 REMOVAL
content_text('Removal, censure, and a new party, 1833 to 1834',
             ['In fall 1833 the deposits went to selected state banks.',
              'One secretary refused and was removed; Taney obeyed.',
              "The Bank's defenders named them the pet banks.",
              'The Senate censured the president.',
              'In 1834 the Whig Party coalesced against King Andrew.'],
             "Teach the removal as Jackson refused to accept the veto's limits, because that refusal is the factual core under the cartoon. The veto killed the recharter, but the Bank still held the public money and four years of charter, and Jackson read his reelection as a mandate not to wait. The removal required a compliant Treasury: the secretary who refused was dismissed, and Roger Taney carried the order out. The political answers came in pairs. In the Senate, Clay carried a censure resolution declaring the president had assumed power the Constitution had not granted him. In the country, National Republicans, Anti-Masons, and disaffected Democrats began joining in 1834 as Whigs, named for the historic opponents of royal power, united at first chiefly by resistance to what they called executive usurpation. A president who claimed to fight concentrated power had concentrated a new opposition into existence.",
             kick='D · The deposits removed', size=24)

# ------------------------------------------------------ 14 BIDDLE'S ANSWER
content_text("Biddle's answer: the contraction, 1833 to 1834",
             ['The Bank cut its loans and refused renewals.',
              'State banks were pressed to settle what they owed.',
              'Credit tightened, merchants failed, and petitions flooded Congress.',
              'The distress was meant to force the deposits back.',
              'The public blamed the Bank, and Biddle relented.'],
             "Present the contraction from the labeled teaching summary at Station 3, and tell students that is what it is: no single Biddle document carries the whole episode, so the station summarizes the record and says so. The facts are these. Through the winter of 1833 and 1834 the Bank contracted its loans sharply, and distress followed in the ports and the interior, and petitions for relief arrived in Congress by the hundred. Biddle's design was to make the country feel the Bank's absence until it demanded the Bank's restoration. The design failed in the one way he had not planned: the country blamed the hand it could see, and the hand was his. In demonstrating that one officer could tighten the whole nation's credit as a political instrument, Biddle supplied the proof of Jackson's central charge, from his own counting room.",
             kick="E · Biddle's answer and the boom", size=24)

# ------------------------------------------------------ 15 THE BOOM
content_photo_s('note-port.jpg', 'The boom the removal fed',
             ['The federal charter expired in 1836.',
              'Pet banks lent federal money on thin reserves.',
              'Western land was bought with borrowed paper.',
              'Land sales climbed year by year to 1836.'],
             "The image is a portrait crop of the Bank's five dollar note of 1829, and the contrast to carry is between the note on screen, issued under the regulator's discipline, and the flood of state bank paper that replaced it. Follow the incentives rather than the morals. The pet banks held the government's deposits, which swelled their reserves on paper, and every deposit bank competed to lend, because lending was profit and the federal balance cost nothing to hold. Western land was the era's great speculation, its price rising, its buyers borrowing the purchase money from the same banks whose notes the land office accepted. Settlers with real farms stood inside the same credit web as pure speculators, which is why Section G's collapse reaches so far down. By 1836 the boom's paper rested on reserves of gold and silver far thinner than the notes promised, and the administration that hated paper most had built the loosest paper system of the era.",
             kick="E · Biddle's answer and the boom")

# ------------------------------------------------- 16 SECTION F DIVIDER
divider_text('Section F', 'The Specie Circular and the Turn',
             'July 1836: the Treasury orders gold and silver for the public lands, aiming at the speculators, and the order lands on an economy already turning.',
             "Introduce the circular as the rare document in this unit whose text students can read entire at Station 5, a working Treasury order rather than a state paper. Its author on paper is Secretary Levi Woodbury, its direction is President Jackson's, and its occasion is stated in its own first sentence: complaints of frauds, speculations, and monopolies in the purchase of the public lands, aided by excessive bank credits. The administration's diagnosis was sincere and partly right. The boom was being bought with paper of doubtful backing, and the Treasury itself was accumulating that paper for the nation's land. The remedy was hard money orthodoxy: after August 15, 1836, the land offices would take gold and silver only. What the remedy would do to the banks that held the nation's thin stock of specie is the section's second half.")

# ------------------------------------------------------ 17 THE ORDER
content_text('What the circular ordered, July 11, 1836',
             ['Complaints were named first: frauds, speculations, monopolies.',
              'After August 15, only gold and silver bought public lands.',
              'Virginia land scrip was accepted in the proper cases.',
              'Settlers were protected to December 15, up to 320 acres.',
              'Specie began moving west to the land offices.'],
             "Read the order's mechanics with the class, because its exception tells students the target was speculation rather than settlement. An actual settler or bona fide resident could still pay in the old kinds of money until December 15, for up to 320 acres. The speculator buying thousands of acres on bank credit could not. As policy the design is coherent. As timing it was dangerous, and the danger is a matter of geography: specie was concentrated in the eastern banks, land was being sold in the West, and every land payment in coin now had to travel westward out of the reserves of banks whose notes still promised coin on demand at home. Teach that movement as the order's unintended consequence, stated in the reading, and keep it separate from the order's stated purpose. Documents prove their purposes. Their consequences have to be traced, which is what Section G does.",
             kick='F · The Specie Circular and the turn', size=24)

# ------------------------------------------------------ 18 STAT 320
stat('320', 'acres, the settler exception in the Specie Circular',
     'Actual settlers could pay in paper until December 15, 1836 · Speculators could not',
     "This small number is the circular read closely. Three hundred twenty acres is a half section, a large family farm by the standards of the public land states, and the exception tells us the administration knew the difference between a settler and a speculator and tried to write it into the order: the settler keeps the old indulgences as to the kind of money received, up to that acreage, until December 15, 1836; the large buyer must produce gold and silver after August 15. When critics called the circular a blunt instrument, this clause is the answer and the admission at once. The order's authors aimed at the paper speculation, and they aimed carefully. What they could not aim at was the state of British credit and the cotton market in the same winter, which turned a careful order into one strand of a general tightening.",
     kick='F · The Specie Circular and the turn')

# ------------------------------------------------- 19 SECTION G DIVIDER
divider_photo('vanburen-port.jpg', 'Section G', 'The Panic of 1837 and Who Paid',
              ['May 1837: the banks suspend. The president who inherits', "the collapse is not the president who fought the Bank."],
              "The portrait is Martin Van Buren, Jackson's chosen successor, photographed late in his life; the face students see is an old man's, and the presidency it belongs to was broken in its first season. Set the section's chronology hard, because causation is the lesson's final skill. Jackson retired to the Hermitage in March 1837, publishing a farewell address that warned the country against paper money and the money power. In May the banks of New York suspended payment in specie and banks across the country followed, since a note no bank would redeem in coin was a promise suspended everywhere at once. Cotton and land values collapsed, debtors failed, and workers lost wages and work. The depression that followed lasted, with brief relief, into the 1840s, and it consumed the presidency of the man in this portrait, who had cast no veto and signed no circular.",
              title_size=32)

# ------------------------------------------------------ 20 THE PANIC
content_text('May 1837: the suspension and the fall',
             ['New York banks suspended payment in specie.',
              'Banks across the country followed within weeks.',
              'Cotton prices and land values collapsed.',
              'Indebted farmers and merchants failed together.',
              'Workers lost wages and work, and depression lasted to the 1840s.'],
             "Teach the suspension as a mechanism, not a mood. A bank's note was a promise to pay gold or silver on demand. When the strongest banks in New York announced in May 1837 that they would not redeem their notes for a time, every holder of every bank's paper learned the promise was suspended, credit froze, and merchants who owed money they could no longer borrow failed in chains, each failure pulling down the next house's paper. Cotton, the export that earned the country's specie, fell in price as British buyers contracted, and western land bought at boom prices would not sell at any price. Notice who is absent from the fragments: neither Jackson nor Biddle appears, because by the spring of 1837 both men were private citizens. The panic had the Bank War's cast nowhere in it and the Bank War's consequences everywhere in it.",
             kick='G · The Panic of 1837 and who paid', size=24)

# ------------------------------------------------------ 21 VAN BUREN'S ANSWER
content_text("Van Buren's answer: the independent treasury",
             ['There would be no new national bank and no return to the pet banks.',
              'The government divorced itself from banking.',
              'In 1840 federal money was kept in federal vaults.',
              'The Bank was dead, and the currency question was not settled.'],
             "Close the narrative with the institutional answer, because the unit test asks for it by name. Van Buren refused both restorations on offer: he would not charter a third national bank, which his party's hard money men would not forgive, and he would not put the government's money back into state banks, which the panic had just discredited. His proposal was separation. Under the independent treasury, enacted in 1840, the federal government kept its money in its own vaults, in the hands of its own officers, divorcing the Treasury from the banking system until the Civil War era rebuilt the connection. Students should see the irony whole: the democracy that destroyed a bank to free the people's money from private power ended by locking the people's money in government strongboxes, outside the credit system entirely, while the country's actual currency went on being the notes of state banks.",
             kick='G · The Panic of 1837 and who paid', size=24)

# ------------------------------------------------------ 22 AT A GLANCE
s = slide(NAVY)
kicker(s, 'The Bank War at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Privilege, power, and the bill', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The Bank and the trap', 'Charter, 1816; recharter forced, 1832', 'A regulator, and a corporation answerable to no voter'),
        ('The veto and the removal', 'Veto, July 1832; deposits removed, 1833', 'Equal protection against privilege; censure and the Whigs'),
        ('The boom and the circular', 'Contraction, 1833 to 1834; circular, July 1836', 'Credit as a weapon; land on paper; specie ordered west'),
        ('The panic and the answer', 'Suspension, May 1837; treasury, 1840', 'Debtors and workers pay; the government keeps its own vaults')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.2, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.25, yy + 0.05, 5.1, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.55, yy + 0.05, 3.9, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the closing table of the guided notes, The Bank War at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The Bank and the trap: chartered in 1816, Biddle regulating by the specie demand, and Clay persuading him to force the vote in 1832. The veto and the removal: the message of July 10, 1832, the reelection, the deposits to the pet banks in 1833, the censure, and the Whigs from 1834. The boom and the circular: the contraction, pet bank lending, the charter expiring in 1836, and gold and silver ordered for land that July. The panic and the answer: suspension in May 1837, depression into the 1840s, and the independent treasury of 1840. Grade the table on dates, actors, and who bore each stage's cost.")

# ------------------------------------------------------ 23 VOCAB A
vocab('Words for the struggle and its men',
      [('Bank War', 'the struggle of 1832 to 1836'),
       ('Nicholas Biddle', 'president of the Bank from 1823'),
       ('pet banks', 'state banks holding the removed deposits'),
       ('Specie Circular', 'gold and silver for public lands, July 1836')],
      "Four terms, in full, in the guided notes wording. Bank War: the political struggle of 1832 to 1836 in which Jackson vetoed the Second Bank's recharter, removed the federal deposits to state banks, and destroyed the institution, which Clay and Biddle had forced to a vote four years early meaning to make it the election's deciding question. Nicholas Biddle: the president of the Second Bank of the United States from 1823, a Philadelphia financier who ran the Bank as the regulator of the nation's currency and fought Jackson for its life with its loans, its contracts, and a deliberate contraction of credit. pet banks: the state banks chosen by the Jackson administration to hold the federal deposits removed from the Second Bank in 1833, named in contempt by the Bank's defenders, whose easy lending on thin reserves fed the land speculation of the middle 1830s. Specie Circular: the Treasury order of July 1836 requiring gold or silver, specie, in payment for public lands, issued to stop speculation bought with paper banknotes and blamed by critics for draining specie from eastern banks on the eve of panic.")

# ------------------------------------------------------ 24 VOCAB B
vocab('Words for the fall and the settlement',
      [('Panic of 1837', 'suspension in May 1837; depression follows'),
       ('Whig Party', "coalesced in 1834 against executive usurpation"),
       ('independent treasury', "Van Buren's vaults, enacted in 1840")],
      "Three more terms, in the guided notes wording, carried in full. Panic of 1837: the financial collapse of May 1837, when banks across the country suspended payment in specie, cotton prices and land values fell, and a depression followed that lasted into the 1840s and broke the presidency of Martin Van Buren. Whig Party: the party that coalesced in 1834 from Jackson's opponents, National Republicans, Anti-Masons, and disaffected Democrats among them, named for the historic opponents of royal power and united at first chiefly by resistance to what they called executive usurpation. independent treasury: President Van Buren's system, enacted in 1840, under which the federal government kept its money in its own vaults rather than in any bank, divorcing the Treasury from the banking system until the Civil War era rebuilt the connection. Notice the arc the three terms draw: the collapse, the party the collapse's politics built, and the institution the collapse's president built in answer.")

# ------------------------------------------------------ 25 CLOSING SYNTHESIS
s = slide(NAVY)
kicker(s, 'Closing synthesis')
text(s, 0.9, 1.35, 11.5, 1.1, 'Two findings, held together', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 2.6,
     ["The Bank did the public's work, holding its money and keeping its currency sound, and its president could tighten the nation's credit as a weapon, and did.",
      "When the Bank fell, the boom and the panic that followed were paid for by debtors and workers who had been parties to neither man's quarrel."],
     size=23, color=POWDER, leading=1.3)
notes(s, "Close the lesson by refusing to let either finding absorb the other, because the documents support both and the verdict work is graded on holding them together. The Bank's public work is documented at Station 1's other side and in the reading's first section: a national currency, the public money kept, and state banks disciplined into honesty by the specie demand. The private power is documented by the Bank's own president: Biddle's contraction of 1833 and 1834, run from a Philadelphia counting room to coerce an elected government, is the veto's abstract charge demonstrated in fact. And the payment is documented in Section G's accounting: suspension in May 1837, cotton and land collapsed, debtors failed, workers idle, a depression into the 1840s, and a successor president broken by a crisis he did not make. Students who hold only the first finding repeat the Bank's defense of itself. Students who hold only the second cannot explain the panic.")

# ------------------------------------------------------ 26 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ["Was the Bank a public good or a private monster, and who paid when it fell? Judge from the Bank's conduct, account for Biddle's contraction, and name the payers of 1837."],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Bank File: the veto, the cartoon, the contraction, the farewell, the circular'),
        ('Notebook', 'Notebook page: the struggle stage by stage, power and cost at each stage'),
        ('Quick check', 'The Veto and the Circular: the charge of 1832 beside the order of 1836'),
        ('Writing', 'Public Good or Private Power: your verdict defended from the file')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the Bank War and the pet banks defined, the circular in two sentences, and the lesson question in two or three.',
     size=15, color=POWDER)
notes(s, "Close the lesson by handing the verdict to the students, which is what this lesson exists to do. The activity, The Bank File, gives them the veto message from the audited bank record, the King Andrew the First print read as an argument, a labeled teaching summary of Biddle's contraction, Jackson's farewell address in its Wikisource transcription, and the Specie Circular in the American Presidency Project transcription, and asks them to judge whether the Bank was a public good or a private power and who paid when it fell. The notebook page charts the struggle stage by stage with power and cost at each stage. The quick check sets the veto beside the circular. The writing task asks for the verdict defended against its strongest rival, with the contraction and the payers of 1837 carried at full strength. The exit ticket has three parts: the Bank War and the pet banks defined, the Specie Circular stated in two sentences, and the lesson question answered with both findings held together.")

dc.save(OUT)
