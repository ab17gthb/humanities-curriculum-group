#!/usr/bin/env python3
"""Early Republic Lesson 2 deck, "The Alien and Sedition Acts and the
Revolution of 1800," in V2 (2026-10-24 rollout, improved slide
standard): content bullets are short complete sentences; speaker notes
applied after the build from the teacher notes guide
(apply_guide_notes.py). Same 27 slides, same order."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags, photo_right,
                         divider_photo, content_photo, content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED, W, H)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

dc.IMG = os.path.join(HERE, 'img')
OUT = os.path.join(HERE, '..', 'lesson-02-slides-v2.pptx')

spec = open(os.path.join(HERE, '..', '..', 'build-scripts', 'unit-spec.md')).read()
l2 = spec.split('### Lesson 2')[1].split('### Lesson 3')[0]
DEFS = {}
for line in l2.splitlines():
    m = re.match(r'- (.+?): (.*)$', line.strip())
    if m: DEFS[m.group(1)] = m.group(2)
assert len(DEFS) == 7, DEFS.keys()

def joined(term):
    return f"{term}: {DEFS[term]}"

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

LQ = 'When the government called its critics traitors, who answered, and what did the election of 1800 prove?'
UQ = 'How did the United States turn its Constitution into a working government, and what did continental expansion do to the republic that government served?'

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'THE EARLY REPUBLIC AND EXPANSION · LESSON 2', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Alien and Sedition Acts and the Revolution of 1800', size=38, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'A government jails its critics, and the critics win the next election', size=17, color=POWDER)
notes(s, "The image is Congressional Pugilists, an anonymous American print published at Philadelphia in 1798, showing Representative Roger Griswold attacking Representative Matthew Lyon with a cane on the floor of Congress while Lyon defends himself with fireplace tongs. Lyon is the congressman this lesson follows into a jail cell, so introduce him here, in February 1798, months before his prosecution. Place the lesson in the unit. Lesson 1 closed with Washington's Farewell Address warning against parties and foreign entanglements. Within two years the country had both at full strength: an undeclared naval war with France, a party fight carried into statute, an opposition answering from the state legislatures, and an election that deadlocked the House of Representatives for a February week. Students should leave able to argue both sides of the Sedition Act and able to say exactly how the transfer of 1801 was completed.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[(LQ, {})]], size=38, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                (UQ, {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question has two halves, and students will need both for the exit ticket and the writing task. First, who answered when the government treated criticism as treason? The answers came in layers: state legislatures speaking through resolutions their authors would not sign in public, a congressman campaigning from a jail cell, newspaper editors, and finally the voters themselves. Second, what did the election of 1800 prove? It proved the hardest thing a young republic can prove, that a ruling party will count the ballots that remove it and go home. Preview the caution built into the lesson: the states' constitutional answer, the Virginia and Kentucky Resolutions, failed in its own season, rejected by ten states and joined by none. The answer that worked was slower, electoral, and nearly broke down in the House before it held.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'War scare, laws, courts, resolutions, deadlock, transfer', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'A War Scare and a Party Fight', 'The XYZ Affair, an undeclared naval war, immigrant voters'),
        ('B', 'Four Laws of 1798', 'Citizenship at fourteen years, and criticism made a crime'),
        ('C', 'The Sedition Act in Court', 'Lyon jailed and reelected, editors tried, judges at midnight'),
        ('D', 'Virginia and Kentucky Answer', 'Compact, interposition, and the word nullification'),
        ('E', 'The Deadlock of 1800', 'A tie at seventy three, and thirty five deadlocked ballots'),
        ('F', 'The Transfer of Power', "Adams gone before dawn, and Jefferson's promise to the minority"),
        ('G', 'The Twelfth Amendment and the Precedent', 'Separate ballots in 1804, and a party surrendering power')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A covers the XYZ Affair and the war scare of 1798. Section B covers the four laws Congress passed that summer. Section C covers the Sedition Act in court, Matthew Lyon's case above all, and the Judiciary Act of 1801. Section D covers the Virginia and Kentucky Resolutions and the doctrine of nullification. Section E covers the electoral tie of 1800 and the House deadlock. Section F covers the transfer of March 4, 1801 and the First Inaugural Address. Section G covers the Twelfth Amendment and the precedent the transfer set. The summary table at the end of the guided notes is titled The Crisis and the Transfer at a Glance, and students will complete it from these seven sections.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', 'A War Scare and a Party Fight',
             'France demands a bribe, ships fight without a declaration, and each party calls the other a traitor.',
             "Set the scene as a foreign crisis arriving inside a domestic party fight, because neither half explains 1798 alone. The French Revolution had become a general European war, France against Britain, and American opinion had sorted itself by party: Federalists leaned toward Britain and order, Democratic-Republicans toward France and popular rights. President Adams had sent envoys to Paris to settle French seizures of American shipping, hoping negotiation would keep the young republic out of the war. In the spring of 1798 he published their dispatches, and the country read that French agents had demanded money before talks could even begin. The rage that followed was genuine and national, and the Federalist majorities in Congress converted it, within months, into armies, taxes, and the four laws of section B. Teach students to hold both facts: the danger was real, and the use made of the danger was partisan.")

# ------------------------------------------------------ 5 XYZ AFFAIR
content_photo_s('adams-port.jpg', 'The XYZ Affair, 1798',
              ['Adams sent envoys to negotiate with France.',
               'French agents, named X, Y, and Z, demanded a bribe and a loan.',
               'The published dispatches enraged the country.',
               'An undeclared naval war began in the Caribbean.'],
              "The image is Gilbert Stuart's portrait of John Adams, painted about 1800 to 1815 and held by the National Gallery of Art. Walk the affair in order. The envoys, Charles Cotesworth Pinckney, John Marshall, and Elbridge Gerry, reached Paris in 1797 and were met not by Foreign Minister Talleyrand but by intermediaries who demanded a large loan to France and a personal bribe before negotiations could open. The envoys refused and reported home. Adams printed the dispatches with the agents' names replaced by the letters X, Y, and Z, which gave the scandal its name. Publication was itself a political act: the documents made France look corrupt and grasping, rallied the country behind the Federalist administration, and put Jefferson's party, with its French sympathies, on the defensive in an election season. American and French warships were soon fighting in the Caribbean without any declaration of war.",
              kick='A · A War Scare')

# ------------------------------------------------------ 6 THE PARTY LENS
content_text('The war scare, read through party',
             ['Federalists saw France as revolution and disorder.',
              "Democratic-Republicans saw France as the republic's old ally.",
              'Irish and French immigrants voted overwhelmingly Republican.',
              'Each party read the other as a foreign agent at home.'],
             "The war scare frightened the Federalists twice over, once about France and once about the electorate. Immigrants arriving in the 1790s, Irish fleeing British rule and French fleeing the revolution's turns, settled in American ports and voted, once citizens, overwhelmingly for Jefferson's Democratic-Republicans. Federalist newspapers described the pattern as a foreign vote being imported, and Federalist congressmen described Republican editors, several of them immigrants, as French agents in print. The Republican answer named the Federalists British agents in return, bought by London banks and trade. Teach the vocabulary of the season carefully: in 1798 treason was a word each party threw at the other weekly, in newspapers their readers trusted completely. That atmosphere is the soil of the Sedition Act. A government that believes its critics are the advance guard of an invader will write laws a calmer government would be ashamed of, and it will find juries to enforce them.",
             kick='A · A War Scare', size=24)

# ------------------------------------------------- 7 SECTION B DIVIDER
divider_photo('lyon-port.jpg', 'Section B', 'Four Laws of 1798',
              ['The Lyon and Griswold print again: the party', 'fight in Congress, in the season the laws passed.'],
              "The image is the center of the 1798 Congressional Pugilists print, cropped for this divider, Griswold's cane against Lyon's fireplace tongs on the floor of Congress Hall in February 1798. Keep the print in view while the laws are introduced, because it shows the temper in which they were written: the majority and the opposition had already come to blows in the chamber months before the Sedition Act passed. Section B reads the four laws of the summer of 1798 as one program with one logic. The Naturalization Act attacked the opposition's future voters. The two Alien Acts armed the president against immigrants in peace and in war. The Sedition Act attacked the opposition's present voice, its newspapers. Federalists defended the package as war preparation, and parts of it, the Alien Enemies Act above all, followed the ordinary practice of nations at war. Students should learn the four laws separately, with dates and penalties, and then judge the package as a whole in the activity.",
              title_size=40)

# ------------------------------------------------------ 8 FOUR LAWS
content_text('Four laws, one program',
             ['The Naturalization Act stretched the wait for citizenship from five years to fourteen.',
              'The Alien Friends Act let the president remove immigrants he judged dangerous.',
              'The Alien Enemies Act reached enemy subjects in a declared war.',
              'The Sedition Act made false, scandalous, or malicious writing against the government a crime.'],
             "Take the laws one at a time, as the reading does. The Naturalization Act of June 1798 stretched the residence required for citizenship from five years to fourteen, which postponed the immigrant vote by nearly a decade in one stroke. The Alien Friends Act let the president order out of the country any alien he judged dangerous, on his own finding, with no trial specified. The Alien Enemies Act, the most conventional of the four, applied only after a declared war or invasion and a public proclamation, and reached male enemy subjects of fourteen and upward who were not naturalized. The Sedition Act of July 1798 made it a federal crime to write, print, utter, or publish false, scandalous, or malicious matter against the government, Congress, or the president, with a fine of up to two thousand dollars and up to two years in prison. Note for students what the act protected and what it omitted: the vice president, Thomas Jefferson, leader of the opposition, was not named in it.",
             kick='B · Four Laws of 1798', size=23)

# ------------------------------------------------------ 9 STAT 14
stat('14', 'years an immigrant now waited for citizenship',
     'Up from five years under the old law · The wait decided when an immigrant could vote · Jefferson\'s Congress restored five years in 1802',
     "Hold this number up as the quiet half of the 1798 program, because the Sedition Act's noise has covered it ever since. Naturalization is where immigration policy becomes election policy: a resident who cannot become a citizen cannot vote, and a fourteen year wait meant that the immigrant arrivals of the 1790s, who leaned heavily Republican, would miss election after election of the new century. Federalists said a long apprenticeship in republican habits made safer citizens, and fourteen years had precedents in the state laws of the Confederation era. Republicans answered that the timing gave the game away, a law passed in a war scare, by the party the immigrants voted against, in the season that party also criminalized criticism of itself. The repeal tells students how the winners judged it: in 1802 the Republican Congress restored the five year wait, where it has essentially remained.",
     kick='B · Four Laws of 1798')

# ------------------------------------------------- 10 SECTION C DIVIDER
divider_text('Section C', 'The Sedition Act in Court',
             'Some ten convictions, nearly all Republicans, and a congressman reelected from his cell.',
             "Laws argue in the abstract, and prosecutions argue in particulars, so section C teaches the Sedition Act by its cases. About twenty five people were arrested under the act and some ten convicted, a small number that students should weigh in both directions: small enough that defenders called the act restrained, and pointed enough that every name on the list belonged to the opposition. The defendants were Republican newspaper editors, the men who ran the only national voice Jefferson's party had, and one sitting congressman, Matthew Lyon of Vermont. No Federalist editor was prosecuted for the savage attacks Federalist papers printed on Jefferson in the same years. The section closes with the season's second use of institutional power, the Judiciary Act of 1801, by which the outgoing Federalist Congress created new judgeships and President Adams filled them to his last night in office, setting the problem the next lesson inherits in Marbury v. Madison.")

# ------------------------------------------------------ 11 LYON
content_photo_s('lyon-port.jpg', 'A congressman in a cell',
              ['Matthew Lyon of Vermont was jailed for criticizing Adams.',
               'His sentence was a fine of one thousand dollars and four months in jail.',
               'Vermont voters reelected him from his cell in December 1798.',
               'His supporters paid his fine, and the House seated him.'],
              "The image is the Congressional Pugilists print cropped to Lyon, who will appear in the activity as the subject of a labeled teaching summary built from the public record. Give the case its documented outline. Lyon, an Irish immigrant, a veteran, and the most combative man in the House, was indicted in Vermont for a letter criticizing President Adams and for words of his read aloud by others. A federal court convicted him in October 1798, fined him one thousand dollars, and jailed him for four months at Vergennes. He conducted his reelection campaign from the cell, writing letters his allies printed, and Vermont's voters returned him to Congress in December while he was still serving the sentence. His supporters paid the fine. Teach the political arithmetic carefully: the prosecution meant to remove a voice and instead manufactured a martyr, a campaign story, and proof, repeated in every Republican paper, that the act was a party weapon. The activity asks students to judge exactly that question from the documents.",
              kick='C · The Sedition Act in Court')

# ------------------------------------------------------ 12 SAFEGUARDS AND MIDNIGHT JUDGES
content_text('Safeguards on paper, and the last use of the season',
             ['Truth was allowed as a defense, and juries judged law and fact.',
              'In practice, the convictions fell on one party only.',
              'The act expired by its own terms on March 3, 1801.',
              'The Judiciary Act of 1801 created new judgeships, filled to the last night.'],
             "Give the Federalist defense its full strength before judging it, because students will meet this pattern again. The Sedition Act was, on paper, more protective than the English common law of seditious libel it replaced: truth could be pleaded as a defense, and the jury was expressly given the right to judge both the law and the fact of the case. Its authors set it to expire on March 3, 1801, the last day of Adams's term, which they cited as proof it was a war measure and not a permanent gag. The practice is the reply. Editors were convicted for opinion the juries of a Federalist district disliked, and the protected list in the statute named the president and Congress while leaving the vice president exposed. Then, in the administration's final weeks, the Federalist Congress passed the Judiciary Act of 1801 creating new circuit judgeships, and Adams signed commissions to his last evening, the midnight judges whose undelivered paperwork opens the next lesson.",
             kick='C · The Sedition Act in Court', size=23)

# ------------------------------------------------- 13 SECTION D DIVIDER
divider_photo('madison-port.jpg', 'Section D', 'Virginia and Kentucky Answer',
              ['Madison, painted by John Vanderlyn, who', 'wrote Virginia\'s answer in secret.'],
              "The image is John Vanderlyn's portrait of James Madison, held in the White House collection. Madison's portrait belongs on this divider because the answer of section D was his and Jefferson's, and both men hid their authorship: Jefferson was vice president of the government he was answering, and Madison was its former congressional leader, so the resolutions went to Kentucky and Virginia as the work of state legislatures, not of the opposition's chiefs. Section D teaches the compact theory at the center of both documents: the states created the federal government by an agreement among themselves, delegated definite powers, and kept the right to judge when the agreement was broken. Virginia's verb was interpose. Kentucky's second set of resolutions, in 1799, supplied the stronger noun, nullification. Teach the doctrine's 1799 reception as part of the doctrine's meaning: ten states formally rejected the resolutions, and not one state joined the two that passed them.",
              title_size=38)

# ------------------------------------------------------ 14 COMPACT
content_text('Compact, interposition, nullification',
             ['The Constitution stood as a compact among the states.',
              'The federal government held delegated powers only.',
              'Virginia held the states duty bound to interpose.',
              'Kentucky, in 1799, named nullification as the rightful remedy.'],
             "Work the argument as a chain, because students will quote it in the quick check and writing task. First, origin: the Constitution is a compact, an agreement, and its parties are the states. Second, grant: the agreement delegated certain definite powers to a general government and reserved everything else to the states. Third, judgment: the government the compact created cannot be the final judge of its own powers, since that would make its discretion, not the Constitution, the measure of them, so each party judges infractions for itself. Fourth, remedy: Madison's Virginia Resolutions say the states are in duty bound to interpose, to step between the federal government and their citizens, against a deliberate, palpable, and dangerous exercise of undelegated power. Jefferson's Kentucky draft and Kentucky's 1799 resolutions go the final step and name it: nullification, a state's declaration that the act is void within its borders. Underline the limit in Jefferson's own framing: the claim reaches undelegated powers, powers never given, not any law a state happens to dislike.",
             kick='D · Virginia and Kentucky Answer', size=23)

# ------------------------------------------------------ 15 STAT 10
stat('10', 'states answered back rejecting the resolutions',
     'And no state joined Virginia and Kentucky · The doctrine\'s authors would not sign it in public · The argument lost in the legislatures of 1799',
     "This statistic is the lesson's built in correction to any romantic reading of the resolutions, and students should write it beside the doctrine in their notes. Virginia and Kentucky asked their fellow states to declare the Alien and Sedition Acts unconstitutional and to stand with them. The other states answered through the winter and spring of 1799, and the answers were refusals: ten states sent resolutions rejecting the compact claim, several of them stating plainly that the federal courts, not state legislatures, judged the constitutionality of federal laws. Not one state joined the protest. Two of the refusals carry an irony worth a full stop in class: the idea that the states could judge federal law was itself judged, by the states, and lost. The doctrine survived anyway, carried forward by its authors' party, and it returned in later decades in hands its 1798 authors did not control, which is why the guided notes definition ends by looking forward.",
     kick='D · Virginia and Kentucky Answer')

# ------------------------------------------------- 16 SECTION E DIVIDER
divider_text('Section E', 'The Deadlock of 1800',
             'Seventy three votes for Jefferson, seventy three for Burr, and a House that could not move.',
             "Section E teaches the election of 1800 as two elections, a victory and a breakdown, in that order. The victory was clear: Jefferson's Democratic-Republicans beat John Adams and took Congress, the verdict the Sedition Act prosecutions had tried to prevent. The breakdown followed from the Constitution's original machinery, under which each elector cast two undifferentiated votes and the runner up became vice president. Every Republican elector voted for both Jefferson and Aaron Burr, as the party intended, and the two men therefore tied at seventy three votes at the head of the poll, which threw the choice between them into the outgoing House of Representatives, voting by state delegations, where Federalists still held the majority. There the breakdown became a crisis, through thirty five ballots in February 1801, with rumors of Burr bargains, of Federalist plans to install an officer of their own, and of Republican governors preparing militia. Hold the tension honestly: for a week the republic did not know who its next president was.")

# ------------------------------------------------------ 17 THE TIE
content_text('How a victory became a tie',
             ['Every Republican elector voted for Jefferson and Burr.',
              'The Constitution had one ballot, with no separate vote for vice president.',
              'The poll stood at seventy-three and seventy-three.',
              'The choice fell to the Federalist-held House, voting by states.'],
             "Explain the mechanical point slowly, since the whole crisis is a machine failure before it is a drama. Under the Constitution as written, an elector voted for two persons without designating which vote was for president and which for vice president; the highest total became president and the second became vice president. Parties, which the framers had not planned for, broke the machine: a party's electors, voting a straight ticket, produced an exact tie between the party's intended president and its intended vice president. Democratic-Republican electors all voted Jefferson and Burr, seventy three votes each, one elector having failed to withhold a second vote as some earlier tickets had arranged. Adams finished behind them, so the old president was beaten, but the Constitution sent the tie to the House, and the House that received it was the lame duck Federalist House the voters had just repudiated, voting not by members but by state delegations, nine states needed to choose.",
             kick='E · The Deadlock of 1800', size=23)

# ------------------------------------------------------ 18 STAT 36
stat('36', 'ballots in the House before Jefferson was chosen',
     'Thirty five deadlocked ballots in February 1801 · Hamilton argued Jefferson was the lesser danger · Burr never withdrew, and never won',
     "Thirty six ballots across the week of February 11 to 17, 1801, and the first thirty five changed almost nothing: Jefferson held eight states, one short of the nine required, Burr held six, and two sat divided and silent. The movement, when it came, ran through the Federalists' own divisions. Alexander Hamilton, who despised Jefferson's politics, spent the winter writing to Federalist congressmen that Burr was the dangerous man, unprincipled and hungry, and that Jefferson, whatever his errors, had principles a government could survive. Burr, for his part, refused every invitation to withdraw, which deepened the suspicion that he would take the presidency from his own party's voters if the House handed it to him. On the thirty sixth ballot, Federalists in the divided and blocking delegations abstained or cast blanks, Maryland and Vermont tipped to Jefferson, and the count reached ten states. The machine had worked at the last moment, operated by men voting against their preference to keep it working.",
     kick='E · The Deadlock of 1800')

# ------------------------------------------------- 19 SECTION F DIVIDER
divider_photo('jefferson-port.jpg', 'Section F', 'The Transfer of Power',
              ['Jefferson, painted by Rembrandt Peale in', '1800, the year of the tie and the deadlock.'],
              "The image is Rembrandt Peale's 1800 portrait of Thomas Jefferson, painted in Philadelphia in the year of the election, and held in the White House collection. Section F teaches March 4, 1801 as a choreography of restraint. President Adams left the capital before dawn, riding out of Washington on the morning his successor took the oath, a departure students should read without melodrama: he had also spent his last night signing judicial commissions, which the next lesson examines, but he made no move to hold power, call troops, or dispute the count. Jefferson walked from his lodgings to the Capitol, took the oath from Chief Justice John Marshall, his own political opponent and cousin, and delivered an inaugural address addressed as much to the beaten party as to his own. The reading and the activity both take the address as the settlement's text: majority rule, minority rights, and error of opinion answered by reason rather than prosecution. A government had changed parties, and the day was, by design, almost ordinary.",
              title_size=40)

# ------------------------------------------------------ 20 INAUGURAL
content_text('Every difference of opinion is not a difference of principle',
             ['The majority will prevail, and its will must be reasonable.',
              'The minority possess equal rights, which equal law must protect.',
              'Error of opinion may be tolerated where reason is free to combat it.',
              'Jefferson summed up good government as wise and frugal.'],
             "Read the address as the anti Sedition Act, sentence by sentence, because Jefferson wrote it for the men who had passed and enforced that act and for the men it had jailed, who now sat in his audience together. The majority principle comes first and is unconditional, the will of the majority is in all cases to prevail, and then it is bounded in the same breath: that will, to be rightful, must be reasonable, and the minority possess their equal rights, which equal law must protect, and to violate would be oppression. Political intolerance is named as a despotism equal to the religious intolerance the country had escaped. The famous sentence follows: every difference of opinion is not a difference of principle, so the two parties, called by different names, were brethren of the same principle, all Republicans, all Federalists. And the practical program closes the address: a wise and frugal government that restrains men from injuring one another and otherwise leaves them free. On March 3 the Sedition Act had expired. On March 4 its replacement was announced, reason left free to combat error.",
             kick='F · The Transfer of Power', size=22)

# ------------------------------------------------- 21 SECTION G DIVIDER
divider_text('Section G', 'The Twelfth Amendment and the Precedent',
             'The machine is repaired, and the ground every later transfer stands on is cleared.',
             "Section G closes the lesson with the repair and the precedent, in that order, and students should learn to distinguish them. The repair was constitutional housekeeping made necessary by the deadlock: the Twelfth Amendment, proposed by the Republican Congress and ratified in June 1804, in time for that year's election. It separated the electoral ballots, one list for president and one for vice president, so that a party ticket could never again tie its own two candidates at the head of the poll, and it set procedures for the House and Senate if no majority emerged. The precedent was larger and could not be amended into existence. In 1801 a party that had prosecuted its opponents counted the votes that removed it, survived a week in which its own House members could have stolen the succession, and went home, while the winners pardoned the prisoners and let the gag law stay expired. Jefferson named his victory a revolution, and section G asks students to judge the name.")

# ------------------------------------------------------ 22 PRECEDENT
content_text('What 1801 proved, and what it left open',
             ['Separate ballots for president and vice president followed from 1804.',
              'Jefferson pardoned those still held under the Sedition Act.',
              'No soldier stood in the street, and the government changed hands.',
              'Nullification was left unanswered, to return in later units.'],
             "Land the lesson's two legacies separately. The settled legacy is the transfer itself: from 1801 forward, American parties that lose presidential elections leave office, a habit so deep now that students must be reminded it was invented here, under strain, by the losing side's restraint and the winning side's inaugural promise to the minority. The naturalization wait went back to five years in 1802, the Sedition Act was never renewed, and its prisoners were pardoned. The unsettled legacy is the doctrine the crisis produced. The Virginia and Kentucky Resolutions were defeated as politics in 1799 and never withdrawn as theory, and their claim that a state may judge and even nullify a federal law sat in the record waiting for later generations to pick it up over tariffs and over slavery, carrying, in the guided notes' phrase, far heavier loads than its authors did in print. The next lesson turns from words to territory: Jefferson, the strict constructionist who doubted any federal power not named, is offered an empire for fifteen million dollars.",
             kick='G · The Twelfth Amendment and the Precedent', size=23)

# ------------------------------------------------------ 23 GLANCE
s = slide(NAVY)
kicker(s, 'The crisis and the transfer at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Who answered, and how', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The war scare', 'XYZ and the naval war, 1798', 'The laws are written'),
        ('The prosecutions', 'Lyon jailed, and reelected from his cell', 'The states answer on paper'),
        ('The resolutions', 'Compact, interpose, nullify; ten states refuse', 'The voters answer in 1800'),
        ('The transfer', 'Thirty six ballots, and power surrendered', 'The Twelfth Amendment repairs the machine')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the summary table in the guided notes, The Crisis and the Transfer at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The four rows are the lesson's argument in order. The war scare: the XYZ Affair and the undeclared naval war made France an enemy and dissent look like treason. The laws and the prosecutions: Congress criminalized criticism, and the courts jailed the opposition's editors and one of its congressmen. The states answer: Virginia and Kentucky argued compact, interposition, and nullification, and were refused by ten states and joined by none. The transfer: the voters defeated the governing party, the House finished its work on the thirty sixth ballot, and power changed hands on ballots alone. Grade the table generously on wording and strictly on sequence: the order of the answers is the lesson.")

# ------------------------------------------------------ 24 VOCAB A
vocab('Words for the crisis',
      [('XYZ Affair', 'a bribe demanded in Paris, 1798'),
       ('Alien Acts', 'citizenship at fourteen years, deportation by decree'),
       ('Sedition Act', 'criticism of the government made a crime'),
       ('Virginia and Kentucky Resolutions', 'the states answer, written in secret')],
      "These definitions match the guided notes word for word, because the unit test draws on them. " + joined('XYZ Affair') + ". " + joined('Alien Acts') + ". " + joined('Sedition Act') + ". " + joined('Virginia and Kentucky Resolutions') + ". Teach the four in sequence: scandal, fear, laws aimed at voters and at voices, and the states' answer.")

# ------------------------------------------------------ 25 VOCAB B
vocab('Words for the settlement',
      [('nullification', 'a state declares a federal law void at home'),
       ('Twelfth Amendment', 'separate ballots, ratified in 1804'),
       ('Revolution of 1800', "Jefferson's name for the transfer of 1801")],
      "Three more terms, again matching the guided notes exactly. " + joined('nullification') + ". " + joined('Twelfth Amendment') + ". " + joined('Revolution of 1800') + ". Keep the first term's warning in class: later generations carried the doctrine far beyond its authors, as students will see in later units. The other two terms belong together: the election changed the government without violence, and the amendment kept the machinery from jamming the same way twice.")

# ------------------------------------------------------ 26 SYNTHESIS
s = slide(NAVY)
kicker(s, 'The lesson in one view')
text(s, 0.9, 1.28, 11.5, 1.0, 'Criticism answered three ways', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Prosecuted', 'The Sedition Act jailed editors and a congressman, nearly all Republicans'),
        ('Answered', 'Two states argued compact and nullification, and ten states refused them'),
        ('Voted', 'The governing party lost the election its laws were built to win'),
        ('Transferred', 'Thirty six ballots, an expired gag law, and a promise to the minority')]
yy = 2.78
for t, d in rows:
    text(s, 0.9, yy, 2.4, 0.7, t, size=24, color=RUST_LT, font='Georgia')
    text(s, 3.45, yy + 0.05, 9.0, 0.9, d, size=19, color=CREAM, leading=1.2)
    yy += 1.05
notes(s, "Use this slide to close the argument before the work begins, and make students say the four rows aloud in order, because the sequence is the lesson. Prosecuted: in a war scare the government made criticism a crime and used the law against the opposition's press and one of its congressmen. Answered: the opposition replied with a constitutional doctrine, that the states as parties to a compact could judge federal law, and in 1799 that doctrine was rejected by the states themselves. Voted: the argument was settled instead by the electorate, which removed the party of the prosecutions. Transferred: after a tie and thirty six ballots, the losers went home, the Sedition Act stayed expired, and the new president promised the minority its equal rights in his first address. The republic had held its enemies inside the law, which is the claim the next lessons test against territory, courts, and war.")

# ------------------------------------------------------ 27 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['When the government called its critics traitors, who answered, and what did the election of 1800 prove? For each record, state whether it defends the government\'s power or the citizen\'s speech, then deliver the verdict.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Sedition File: five stations and a verdict on the act'),
        ('Notebook', 'Notebook page: five steps in a chart, and the answer that held'),
        ('Quick check', 'A Law and Its Answer: the Sedition Act against the Kentucky draft'),
        ('Writing', 'Necessary Law or Party Weapon: the lesson question as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the Sedition Act defined with its penalties, the compact claim with its 1799 remedy, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Sedition File, sets out five stations: the Alien and Sedition Acts in Congress's own words, Jefferson's draft of the Kentucky Resolutions, Madison's Virginia Resolutions, a labeled teaching summary of Matthew Lyon's prosecution and reelection, and Jefferson's First Inaugural Address, and it ends with a table sorting the records by the power or the speech they defend and a verdict on whether the act was a wartime necessity or a party weapon. The notebook page charts the five steps of the crisis and asks for the answer that held. The quick check, A Law and Its Answer, tests the Sedition Act's penalties, the compact claim, nullification, and the election's numbers. The writing task turns the verdict into an essay argued from the evidence bank. The exit ticket has three parts: the Sedition Act with its maximum fine and prison term, the compact claim with the remedy Kentucky added in 1799, and the lesson question in two or three sentences. Next lesson opens with the judges Adams signed on his last night.")

dc.save(OUT)
