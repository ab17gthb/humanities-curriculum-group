#!/usr/bin/env python3
"""Cold War Lesson 7 deck, "Détente, Human Rights, and the Evil Empire,"
built on the shared deck system: image-led slides, fragments only on
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

def content_photo_s(img, title, items, note, kick=None, size=21):
    s = slide(CREAM)
    photo_right(s, img)
    if kick: kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95 if kick else 0.8, 6.9, 1.2, title, size=31, color=NAVY, font='Georgia', leading=1.05)
    frags(s, items, y=2.15 if kick else 2.0, w=6.9, size=size)
    notes(s, note)
    return s

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.30, 11.5, 0.4, 'THE COLD WAR · LESSON 7', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.64, 11.9, 1.0, 'Détente, Human Rights, and the Evil Empire', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.52, 11.5, 0.45, 'Why the rivals stepped back, and why the confrontation returned', size=17, color=POWDER)
text(s, 0.9, 7.02, 11.9, 0.4, 'President Nixon and General Secretary Brezhnev signing the SALT agreements in Moscow, May 26, 1972.', size=11, color=POWDER)
notes(s, "Open with the photograph, because it is the lesson in a single frame. President Richard Nixon and Soviet General Secretary Leonid Brezhnev are signing the first Strategic Arms Limitation agreements in Moscow on May 26, 1972, two leaders whose governments had armed against each other for a quarter century, seated at one table with pens in hand. The lesson asks how that table was reached and why it was abandoned within the decade. The arc runs in three movements. First, the easing of the 1970s, built by presidents who had reasons to step back: arms agreements, an opening to China, trade, and the Helsinki settlement of 1975. Second, the strain and collapse, as critics at home attacked the bargain from two directions and the Soviet invasion of Afghanistan ended it in December 1979. Third, the return of confrontation under President Reagan, in spending, in aid to insurgencies, in language, and in a proposed defense in space, closing with the dangerous autumn of 1983.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.7, 11.5, 3.6, [[('Why did the rivals try to ease the Cold War in the 1970s, and why did the confrontation return in the 1980s?', {})]],
     size=40, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.5)
text(s, 0.92, 5.75, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the struggle between the United States and the Soviet Union reshape the world and American life, and why did it end the way it did?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Read the lesson question in its two halves, because the lesson is built to answer both and students lose credit when they answer only one. The first half asks why the rivals tried to ease the contest, and its answer is structural, not sentimental. Neither president nor general secretary acted from goodwill alone. Each side faced costs the easing could reduce: nuclear parity, a Soviet split with China, and an American war in Vietnam. The second half asks why the confrontation returned, and its answer is a sequence of dated events rather than a change of mood: criticism at home through the 1970s, an invasion in December 1979, an election in 1980, and two announcements in March 1983. The unit question runs beneath as the frame. This lesson is where the unit's arc bends: containment partially suspended by agreement, then resumed at higher pressure, a decade before the ending the next lesson takes up.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Easing, collapse, and return', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'Why the Rivals Stepped Back', 'Parity, the China split, and Vietnam'),
        ('B', 'The Architecture of Détente', 'The China opening, SALT I, and trade'),
        ('C', 'Helsinki and Human Rights', 'Borders recognized; rights pledged and used'),
        ('D', 'The Critics at Home', 'Attacked from the right and on human rights'),
        ('E', 'The Collapse in Afghanistan', 'Invasion in December 1979; the bargain ends'),
        ('F', 'The Return of Confrontation', 'Buildup, the Reagan Doctrine, the evil empire'),
        ('G', 'A Dangerous Year', 'SDI, the airliner, and Able Archer in 1983')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Sections A and B build the easing: the reasons both sides had to step back by 1969, then the structure Nixon and Kissinger raised on those reasons, the China opening, the SALT agreements, and trade. Section C covers Helsinki, the settlement whose human rights clause outlasted the bargain that produced it. Section D turns home, to the critics who weakened détente from the right and from the human rights side at once. Section E is the collapse, dated to December 1979. Sections F and G cover the renewed confrontation: the buildup and the Reagan Doctrine, the evil empire speech and the Strategic Defense Initiative of March 1983, and the autumn when misreading became the central danger. The summary table at the end of the guided notes asks students to rebuild this map in their own words.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_text('Section A', 'Why the Rivals Stepped Back',
             'By 1969, both sides were paying more for the contest than it returned.',
             "Section A states the conditions that made easing rational, and it should be taught as calculation on both sides, not as a warming of feeling. On the Soviet side, the arsenal had drawn near the American one in nuclear strength, which removed the prospect of a cheap advantage from further building, and the split with China had become open fighting on the border in 1969, leaving Moscow with rivals on two fronts. On the American side, the war in Vietnam held more than half a million troops, consumed money and lives each week, and divided the country whose government would have to sustain any harder line. One caution belongs in the teaching. Easing the contest at its nuclear edge did not end the contest. Both governments continued to compete for influence across Asia, Africa, and Latin America throughout the decade of détente. What changed was the method at the top: negotiation and agreement where the weapons were most dangerous, while the rivalry ran on underneath.")

# ------------------------------------------------------ 5 A CONDITIONS
content_text('Three pressures toward the table',
             ['The two sides had reached near parity in nuclear strength by 1969.',
              'Soviet and Chinese forces clashed on the border in 1969.',
              'More than 500,000 American troops were in Vietnam.',
              'Nixon and Kissinger built détente on those facts.'],
             "Work through the three pressures in order and attach each one to the side it pressed. Near parity pressed both. By 1969 the Soviet Union had drawn close to the United States in nuclear strength, so each side held an arsenal the other could not disarm, and another round of building bought expense without advantage. The China split pressed Moscow. Soviet and Chinese forces fought border clashes in 1969 between two Communist states that had been allies twenty years earlier, and the Soviet Union now had to reckon with hostility in the east as well as the west. Vietnam pressed Washington. More than half a million American troops were committed to a war that showed no decision, and the country was divided over it in the streets and in Congress. From those facts Nixon and his adviser Henry Kissinger built détente, a structure of agreements, trade, and summits meant to give Moscow rewards it would lose by pushing too hard, so that restraint paid.",
             kick='A · Why the rivals stepped back')

# ------------------------------------------------------ 6 STAT VIETNAM
stat('More than 500,000', 'American troops in Vietnam in 1969',
     'The commitment the United States was carrying when détente was designed · The war also divided the country at home',
     "Let this figure carry its full weight before moving on. More than half a million American troops were in Vietnam in 1969, the year Richard Nixon took office promising a way out of the war. The commitment shaped every calculation behind détente. A government fighting an unpopular ground war in Asia could not also press the Soviet Union at full strength on every front at once, and it needed Moscow's cooperation, or at least Moscow's restraint, while it withdrew. The figure also explains the domestic half of the policy. Détente was presented to the American public as the diplomacy of a country getting its commitments back within its means: summits and agreements abroad, troops coming home from Vietnam, and defense held at levels a divided country would fund. Students should write the figure into section A of the notes beside the other two pressures, parity and the China split, because the three together form the answer to the first half of the lesson question. No one of them explains the easing alone.",
     kick='A · Why the rivals stepped back')

# ------------------------------------------------- 7 SECTION B DIVIDER
divider_text('Section B', 'The Architecture of Détente',
             'China first, then Moscow: agreements, trade, and summits.',
             "Section B covers the structure itself, built in a deliberate order that students should be able to reproduce. The opening to China came first, in February 1972, because it changed Moscow's position before Nixon ever sat down with Brezhnev. The Moscow summit followed in May, producing the SALT agreements, the first negotiated limits on the nuclear arsenals. Trade and summit meetings then gave the structure its routine: grain and technology moving one way, regular meetings at the top, and a standing negotiation on arms that continued through the decade. Teach the architecture as a design with a logic, because the writing task in this lesson asks students to judge whether the design failed on its own terms. A design can only fail on its terms if the class first states what its terms were. The terms here were linkage and restraint for reward: behave within the settlement, and the trade, the summits, and the agreements continue.")

# ------------------------------------------------------ 8 B CHINA
content_photo_s('china-port.jpg', 'The opening to China, February 1972',
              ['Nixon was in Beijing as the first American president to visit China.',
               'Relations opened after 23 years of nonrecognition.',
               'One Communist power was used against the other.',
               'Moscow gained a reason to settle with Washington.'],
              "The photograph shows President Nixon shaking hands with Premier Chou En-lai on his arrival in Peking, as the Chinese capital was then spelled in American reporting, on February 21, 1972. No American president had visited the People's Republic of China, and the United States had refused to recognize its government since its founding in 1949, treating the Nationalist government on Taiwan as the government of China instead. The visit reversed that position in a week of banquets, communiqués, and televised ceremony. Its strategic purpose was plain and was understood in Moscow at once. The United States had opened a relationship with the Soviet Union's Communist rival, the state Soviet forces had fought on the border three years earlier. A Soviet leadership facing an American opening to China had fresh reason to reach its own agreements with Washington before the triangle settled against it. That is why the China visit belongs inside the architecture of détente and not in a separate lesson on Asia. It was the first move, and the Moscow summit was the second.",
              kick='B · The architecture of détente')

# ------------------------------------------------------ 9 B SALT
content_photo_s('salt-port.jpg', 'SALT I: the first negotiated limits, May 1972',
              ['The agreements were signed at the Moscow summit on May 26, 1972.',
               'Missile launcher numbers were frozen.',
               'Modernization of existing launchers was allowed.',
               'Trade in grain and technology followed.'],
              "The photograph shows the signing in Moscow on May 26, 1972, and this is Station 1 of the activity, where students read the agreement's own text. Article I of the interim agreement froze construction of additional fixed land based intercontinental ballistic missile launchers after July 1, 1972, and a companion agreement capped submarine launched launchers as well. State the limit precisely, because the lesson's argument turns on it. The freeze counted launchers, not warheads, and Article IV of the same agreement expressly allowed each side to modernize and replace the missiles and launchers it already held. Both halves belong in section B of the notes. The first half is the achievement: rival governments accepting a negotiated ceiling on the most dangerous weapons in the world. The second half is the weakness the critics later named: inside the frozen number of launchers, each side could and did build newer missiles carrying several warheads apiece. The agreements also opened the routine of détente, summits, grain sales, and technology trade that ran through the decade.",
              kick='B · The architecture of détente')

# ------------------------------------------------- 10 SECTION C DIVIDER
divider_text('Section C', 'Helsinki and Human Rights',
             'Borders settled in 1975, and a pledge that outlasted the bargain.',
             "Section C covers the Helsinki Accords of August 1975, the widest settlement of the détente years and the one with the longest consequences. Thirty five nations signed the Final Act in the Finnish capital, including the United States, Canada, the Soviet Union, and nearly every European state. The document had two halves, and the class should hold them apart from the start. One half settled the map: Western nations recognized the postwar borders of Europe, including the division of Germany and the Soviet Union's western frontier as drawn in 1945, the settlement Moscow had sought for thirty years. The other half stated principles for conduct inside states, including respect for human rights and fundamental freedoms. Moscow signed the second half to obtain the first and expected it to cost little, since the document carried no enforcement machinery. The rest of the section is the story of that expectation failing, as dissidents converted a diplomatic formula into an instrument against their own governments.")

# ------------------------------------------------------ 11 C HELSINKI
content_photo_s('helsinki-port.jpg', 'Helsinki, August 1, 1975',
              ['Thirty five nations signed the Final Act.',
               'The West recognized Europe\u2019s postwar borders.',
               'The Soviet bloc pledged respect for human rights.',
               'Dissidents quoted the pledge back to their governments.'],
              "The photograph shows President Gerald Ford, who succeeded Nixon in 1974, signing the Final Act at Finlandia Hall in Helsinki as the document passed among the European leaders for signature. This is Station 2 of the activity, where students read Principle VII in the document's own words: the participating states will respect human rights and fundamental freedoms, including the freedom of thought, conscience, religion or belief, for all without distinction. The same principle confirmed the right of the individual to know and act upon his rights and duties. Dissidents in the Soviet Union and Eastern Europe acted on that sentence. In Moscow in 1976 and in Prague in 1977, citizens formed watch groups that measured their governments against the pledge, documented arrests and trials, and sent the record abroad, where it reached Western governments and newspapers. The pledge had no court behind it. What it had was a signature, and the dissidents' work showed that a signature, quoted persistently and in public, could itself become a form of pressure.",
              kick='C · Helsinki and human rights')

# ------------------------------------------------------ 12 STAT 35
stat('35', 'nations signed the Helsinki Final Act',
     'Helsinki, August 1, 1975 · The United States, Canada, the Soviet Union, and nearly every European state',
     "Thirty five is a small number to carry a large point, and the point is the breadth of the signature. The Helsinki Final Act was not a bilateral bargain between Washington and Moscow alone. It was signed by thirty five states, East and West, which is why its human rights language could not later be dismissed in Moscow as an American invention imposed on the Soviet Union. The Soviet government had signed it in a room with its own allies, in exchange for the recognition of borders it had wanted since 1945, and the dissidents who quoted Principle VII were quoting a text their own head of state had accepted before the whole continent. Students sometimes treat Helsinki as a footnote to the arms agreements. The sequence of the lesson argues otherwise. The SALT freeze expired and was renegotiated. The grain trade rose and fell with politics. The Helsinki pledge kept working inside the Soviet bloc for the rest of the Cold War, and the next lesson's account of 1989 runs partly through the watch groups this section describes.",
     kick='C · Helsinki and human rights')

# ------------------------------------------------------ 13 C DISSIDENTS CARTER
content_text('A pledge used, and a president who pressed it',
             ['Watch groups formed in Moscow and Prague.',
              'Arrests and trials were documented and sent abroad.',
              'Carter made human rights a test of policy in 1977.',
              'Moscow read protest as interference.'],
             "Close section C with the two forces the Helsinki pledge set moving. The first was private citizens acting on a public text. The Moscow Helsinki Group formed in 1976 to report on Soviet compliance, and Charter 77 in Czechoslovakia followed in 1977, naming itself for a January petition. Their members were watched, arrested, and in some cases imprisoned, and the documentation continued through other hands, which is the record the pledge made possible. The second force was a president. Jimmy Carter, elected in 1976, made human rights a stated test of American foreign policy, protested the treatment of named Soviet dissidents, and pressed friendly governments as well as adversaries. Soviet leaders read the protests as interference in their internal affairs, exactly the charge Principle VI of the same Helsinki document, on nonintervention, could be quoted to support. Teach that tension honestly. The Final Act armed both arguments, and the working relationship between the two governments thinned as each side quoted its half of the document.",
             kick='C · Helsinki and human rights', size=24)

# ------------------------------------------------- 14 SECTION D DIVIDER
divider_text('Section D', 'The Critics at Home',
             'Attacked from the right, and pressed on human rights, at the same time.',
             "Section D explains why détente lost its political base in the United States before it lost its structure abroad, and the section has two fronts that students often merge into one. The first front was the right. Senators and former officials charged that the agreements let the Soviet Union keep building modern weapons inside the frozen launcher counts while American programs were held back, and that grain and technology sales rewarded a government whose conduct had not changed. Senator Henry Jackson of Washington pressed the point into law, tying trade benefits to the Soviet Union's willingness to let its Jewish citizens emigrate. The second front was human rights politics, which cut across party lines: the argument that a policy of summits and trade with a government that imprisoned its critics was a bargain struck over the heads of the people living under it. Carter carried that argument into the presidency itself. A policy attacked as too soft by one side and too cynical by the other had few defenders left when the shock of 1979 arrived.")

# ------------------------------------------------------ 15 D CRITICS
content_text('Two charges against the bargain',
             ['The right charged that Moscow built while America held back.',
              'Trade rewarded conduct that had not changed.',
              'Jackson tied trade to Jewish emigration.',
              'Human rights critics said the summits were held over the heads of dissidents.'],
             "Give each charge its strongest form, because the writing task requires students to answer arguments rather than labels. The right's charge was technical before it was rhetorical, and it rested on the text students read at Station 1. Article IV of the SALT interim agreement allowed modernization without limit inside the launcher freeze, and Soviet forces used those years to field new generations of missiles. Critics concluded that the agreements limited the side that observed them in spirit and not the side that observed them only in letter. The emigration fight made the same point in human terms: Jackson's amendment denied trade benefits to a state that blocked its citizens from leaving, and Moscow, rather than accept the condition, gave up the trade agreement, which showed both governments that linkage could cut against the bargainer as well. The human rights charge came from the other direction and held that the summits themselves were the problem, conferring standing on a government while its critics sat in prison. By 1979 the policy had critics everywhere and a constituency almost nowhere.",
             kick='D · The critics at home', size=23)

# ------------------------------------------------- 16 SECTION E DIVIDER
divider_text('Section E', 'The Collapse in Afghanistan',
             'December 1979: the invasion that ended the decade\u2019s bargain in weeks.',
             "Section E is the turning point of the lesson, and it should be taught at the speed the events themselves moved. In late December 1979, Soviet forces entered Afghanistan, seized the capital, killed the country's leader, and installed a replacement who would take Moscow's direction. The Soviet government described an invitation and a limited stay. What followed instead was a guerrilla war the Soviet army could not finish, which lasted the rest of the decade. The stated Soviet purpose was defensive in its own terms: to hold a friendly Communist government in place on the Soviet Union's southern border rather than watch it fall to a rebellion. The effect in Washington was immediate and total. Whatever remained of détente's political standing collapsed, and President Carter, who had entered office as the policy's human rights critic, became the president who dismantled its remaining structure in reply. The next two slides take the invasion's consequences in order: the American answer of January 1980, and the treaty signed six months earlier that the invasion killed.")

# ------------------------------------------------------ 17 E AFGHANISTAN
content_text('The invasion and the American answer',
             ['Soviet forces entered Afghanistan in December 1979.',
              'Kabul was seized and the Afghan leader was killed.',
              'Carter answered with a grain embargo and an Olympic boycott.',
              'The Carter Doctrine warned against threats to the Persian Gulf.'],
             "This record is Station 3 of the activity, a labeled summary, and students should note that it is marked as a summary on its face, unlike the verbatim stations around it. The facts are these. Soviet troops seized Kabul in late December 1979, the Afghan leader Hafizullah Amin was killed, and Babrak Karmal was installed in his place. Carter answered in January 1980 on three levels. Economically, the United States embargoed grain sales, striking at a trade that détente itself had built. Symbolically, it led a boycott of the Moscow Olympics of that summer, so the games the Soviet Union had meant as a display went ahead with much of the West absent. Strategically, the Carter Doctrine of January 23 declared that an attempt by any outside force to gain control of the Persian Gulf region would be repelled by any means necessary, including military force. The declaration reached beyond Afghanistan to the oil region behind it, and it announced that the era of rewards for restraint was closed.",
             kick='E · The collapse in Afghanistan', size=24)

# ------------------------------------------------------ 18 E SALT II
content_photo_s('salt2-port.jpg', 'SALT II: signed in June, dead by January',
              ['Carter and Brezhnev signed at Vienna in June 1979.',
               'The second SALT treaty limited delivery vehicles.',
               'The treaty was withdrawn from the Senate after the invasion.',
               'The treaty was never ratified.'],
              "The photograph shows President Carter and General Secretary Brezhnev signing the second SALT treaty at Vienna on June 18, 1979, six months before the invasion of Afghanistan. Hold the date in front of the class, because it is the strongest single fact for one side of the lesson's argument. The structure of détente, for all the criticism it had absorbed, was still producing signed agreements on the central weapons in the summer of 1979. The treaty's fate then shows how quickly the ground moved. Ratification was already doubtful in a Senate full of the policy's critics. After December, Carter withdrew the treaty from consideration rather than lose the vote, and it was never ratified, though both sides largely observed its terms for some years afterward. Students writing the lesson's essay will use this slide's two dates, June 1979 and January 1980, whichever side they take. One side reads a working structure destroyed by a shock. The other reads a treaty already too weak to win its own Senate.",
              kick='E · The collapse in Afghanistan')

# ------------------------------------------------- 19 SECTION F DIVIDER
divider_text('Section F', 'The Return of Confrontation',
             'A new president, a buildup, aid to insurgencies, and a name for the adversary.',
             "Section F covers the change of policy that followed the election of 1980, and its argument is that the confrontation returned as a deliberate program rather than as drift. Ronald Reagan had campaigned on the charge that the United States had grown weak while the Soviet Union had grown strong, the critics' case of Section D carried into a winning platform. In office, his administration raised defense spending sharply, pressed ahead with new missiles, and aided anti-Communist insurgencies fighting Soviet backed governments, the policy that took the name Reagan Doctrine. The photograph work in this section shows the doctrine's largest theater, Afghanistan, where American aid raised the cost of the occupation the Soviet Union had begun in 1979. The section then turns from capability to language, because in March 1983 the president named the adversary in moral terms no summit document had used. The two March announcements, the speech and the defense proposal that followed it by fifteen days, are the material of Section G's dangerous year.")

# ------------------------------------------------------ 20 F DOCTRINE
content_photo_s('reagan-port.jpg', 'The Reagan Doctrine in Afghanistan',
              ['Defense spending was raised sharply from 1981.',
               'The United States aided insurgencies fighting Soviet backed governments.',
               'The aid went to Afghanistan, Nicaragua, and elsewhere.',
               'Shoulder fired antiaircraft missiles reached the Afghan fighters.'],
              "The photograph shows President Reagan meeting Afghan resistance leaders in the Oval Office on February 2, 1983, a meeting held to discuss Soviet conduct in Afghanistan. The image states the Reagan Doctrine in one scene: the fighters of an insurgency against a Soviet backed government received at the center of American power. The doctrine's logic answered the limited war problem of earlier lessons. Rather than commit American troops against Soviet clients, the United States would supply the local forces already fighting them, raising the price of occupation until it exceeded its value. In Afghanistan the aid grew through the decade and included shoulder fired antiaircraft missiles that reduced the Soviet army's freedom to use helicopters, its chief weapon against guerrillas in mountain country. In Nicaragua the same policy aided insurgents against a government Washington opposed, and it divided American politics sharply. Both judgments belong in the teaching: the doctrine raised Soviet costs in Afghanistan by design, and its means were contested at home on evidence as well as on principle.",
              kick='F · The return of confrontation')

# ------------------------------------------------------ 21 F EVIL EMPIRE
content_text('Naming the adversary, March 8, 1983',
             ['Reagan addressed the National Association of Evangelicals.',
              'He called the Soviet Union the focus of evil in the modern world.',
              'He rejected by name the idea that both sides were equally at fault.',
              'He predicted in the same speech that communism\u2019s last pages were being written.'],
             "Read the speech's central lines aloud from Station 4 of the activity, because the passage is the document and paraphrase loses its force. Reagan told the evangelical convention that while Soviet leaders preached the supremacy of the state and predicted its eventual domination of all peoples on Earth, they were the focus of evil in the modern world. He warned his audience against declaring both sides equally at fault in the arms race, calling that a temptation of pride that ignored the facts of history and the aggressive impulses of an evil empire. And he predicted that communism was another sad, bizarre chapter in human history whose last pages were even then being written. Set the register against the documents of Sections B and C. The agreements were written in the neutral vocabulary of parties and participating states, negotiated and signed by both sides. The speech was a moral verdict delivered by one side about the other, to a domestic religious audience. Critics called the language reckless. Supporters called it the first honest description. The lesson keeps both readings and tests the text.",
             kick='F · The return of confrontation', size=23)

# ------------------------------------------------- 22 SECTION G DIVIDER
divider_text('Section G', 'A Dangerous Year',
             '1983: a shield proposed, an airliner destroyed, an exercise misread.',
             "Section G closes the lesson with the year the renewed confrontation carried its greatest risk, and it must be taught with the evidence stated at its own strength. Three events compose it. In March, fifteen days after the evil empire speech, Reagan announced the Strategic Defense Initiative, a research program toward a defense in space against nuclear missiles, which Soviet leaders read as an attempt to make their arsenal useless. In September, a Soviet fighter shot down a Korean passenger airliner that had strayed into Soviet airspace, killing all 269 people aboard. In November, NATO's Able Archer exercise rehearsed the procedures of a nuclear release in the most realistic form the alliance had used. How far some in Moscow took the exercise for preparation of a real attack is a debated reading of the evidence, and this lesson states it in exactly those terms and no stronger. What is not debated is the condition the three events shared: the two governments were barely speaking, and each was reading the other's moves without the summit contact the previous decade had supplied.")

# ------------------------------------------------------ 23 G SDI
content_text('The Strategic Defense Initiative, March 23, 1983',
             ['The proposal was a defense in space against nuclear missiles.',
              'The proposal was called Star Wars by its critics.',
              'The stated goal was to render nuclear weapons impotent and obsolete.',
              'Soviet leaders read it as an attempt to make their arsenal useless.'],
             "This proposal is Station 5 of the activity, and students read Reagan's own words there: a call to the scientific community that gave the country nuclear weapons to turn its talents to giving the United States the means of rendering those weapons impotent and obsolete, and a directed research program toward eliminating the threat posed by strategic nuclear missiles. Teach why a defensive proposal raised pressure, because students often file defense under easing by reflex. Deterrence, the bargain the arsenals had rested on since the 1950s, held each side safe because an attack would bring a destroying reply. A shield that worked would protect its holder against that reply, and the side behind it could then strike, or threaten, with less to fear. Soviet leaders read the announcement in those terms, as a bid to undo their deterrent after the buildup had already pressed it, whatever the protective purpose the address declared. Whether the technology could ever have worked as promised was, and remains, a separate argument from the one Moscow had to answer in 1983.",
             kick='G · A dangerous year', size=23)

# ------------------------------------------------------ 24 STAT 269
stat('269', 'people killed aboard Korean Air Lines Flight 007',
     'Shot down by a Soviet fighter after straying into Soviet airspace, September 1, 1983 · All aboard were killed',
     "State the facts of September 1, 1983 plainly and in order. Korean Air Lines Flight 007, a passenger flight from New York to Seoul by way of Anchorage, strayed far off course and entered Soviet airspace over Sakhalin Island. A Soviet fighter intercepted it and shot it down. All 269 people aboard, passengers and crew, were killed, among them a sitting member of the United States Congress. The Soviet government at first denied the act, then defended it as the stopping of an intruder, while the United States charged that a civilian airliner had been destroyed with knowledge of what it was. For this lesson the shootdown's place is in the sequence of 1983. It fell between the March announcements and the November exercise, it confirmed each capital's worst account of the other at the moment relations were thinnest, and it brought public anger into a crisis that governments were conducting without summit contact or a working channel of explanation. Two hundred sixty nine is a count of the dead, and the slide keeps it in that form.",
     kick='G · A dangerous year')

# ------------------------------------------------------ 25 G ABLE ARCHER
content_text('Able Archer and the problem of reading an exercise',
             ['The NATO exercise rehearsed nuclear release steps in November 1983.',
              'The exercise was conducted in an unusually realistic form.',
              'Some in Moscow may have read it as cover for an attack.',
              'That reading of the evidence is debated and is stated as such.'],
             "End the content with the lesson's exercise in precision, because this slide is where students learn to state a danger at the strength the evidence supports. Able Archer was a NATO command exercise in November 1983 that rehearsed the procedures leading to a nuclear release, with realistic communications and participation at senior levels. Soviet intelligence had been directed for two years to watch for signs of a surprise attack, and reporting from that period shows genuine alarm in parts of the Soviet system as the exercise ran. Later accounts, including a 1990 American intelligence review, treated the episode as a war scare in which misreading was possible. Other historians weigh the same record and judge that Soviet leaders, while alarmed, did not expect an attack and took no steps toward launching one. The guided notes therefore say that some in Moscow may have taken the exercise for cover for a real attack, by a debated reading of the evidence. Students should copy that caution exactly. It is the form a hard claim takes when the record is real and incomplete at once.",
             kick='G · A dangerous year', size=23)

# ------------------------------------------------------ 26 VOCAB A
vocab('Words for the easing',
      [('détente', 'the easing of tension pursued in the 1970s, built on agreements, trade, and summits'),
       ('arms control', 'negotiated limits on weapons, agreed in treaties'),
       ('SALT', 'the talks, and the 1972 and 1979 agreements limiting delivery vehicles'),
       ('Helsinki Accords', 'the 1975 agreement on borders and human rights')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. The first term is détente: the easing of tension between the United States and the Soviet Union pursued in the 1970s, built on arms agreements, trade, and regular summit meetings. The second is arms control: negotiated limits on the weapons the superpowers could build or deploy, agreed in treaties rather than won in competition. The third is SALT: the Strategic Arms Limitation Talks between the United States and the Soviet Union, and the agreements they produced in 1972 and 1979 limiting nuclear delivery vehicles. The fourth is Helsinki Accords: the 1975 agreement in which Western nations recognized Europe's postwar borders and the Soviet Union and its allies pledged respect for human rights, a pledge dissidents used against their own governments. Note how much of the lesson each definition carries: the first names the structure of the easing, the third names its two treaty years, and the fourth contains the dissidents inside the definition itself, which is where the section placed them.")

# ------------------------------------------------------ 27 VOCAB B
vocab('Words for the return',
      [('Reagan Doctrine', 'aid to anti-Communist insurgencies, in Afghanistan, Nicaragua, and elsewhere'),
       ('Strategic Defense Initiative', 'the 1983 proposal for a defense in space against nuclear missiles'),
       ('Evil Empire', 'Reagan\u2019s March 1983 name for the Soviet Union')],
      "Three more terms, again matching the guided notes exactly. The first is Reagan Doctrine: the policy of the 1980s under which the United States aided anti-Communist insurgencies fighting Soviet-backed governments, in Afghanistan, Nicaragua, and elsewhere. The second is Strategic Defense Initiative: President Reagan's 1983 proposal to build a defense in space against nuclear missiles, called Star Wars by its critics, which promised protection deterrence could not. Students should note the nickname's place inside the definition: it belongs to the critics, and it has outlasted the program's official name in common use. The third is Evil Empire: President Reagan's name for the Soviet Union in a speech of March 1983, declaring it the focus of evil in the modern world and rejecting the idea that the two systems were morally equal. That last clause is the term's argument in miniature. The name did its work by refusing the equal fault framing that the freeze movement, in Reagan's charge, had accepted.")

# ------------------------------------------------------ 28 SYNTHESIS
s = slide(NAVY)
kicker(s, 'The record at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Easing, collapse, return', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Built', 'China opening, SALT I, Helsinki, 1972 to 1975', 'Agreements, trade, and summits'),
        ('Strained', 'Critics on the right and on human rights', 'The bargain loses its base at home'),
        ('Collapsed', 'Afghanistan, December 1979', 'Embargo, boycott, SALT II withdrawn'),
        ('Returned', 'Buildup, doctrine, evil empire, SDI, 1981 to 1983', 'Pressure in spending, aid, language, capability'),
        ('Risked', 'Airliner, Able Archer, autumn 1983', 'Misreading without summit contact')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the final table in the guided notes, The Record at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The five rows compress the argument of the hour. Built: between 1972 and 1975 the rivals constructed a working structure of agreements, trade, and summits on reasons both sides could state. Strained: the structure lost its political base at home to critics arguing from the right and from human rights at once. Collapsed: a single invasion in December 1979 ended the bargain and brought the embargo, the boycott, and the withdrawal of a signed treaty. Returned: from 1981 the confrontation resumed as a program, in spending, in aid to insurgencies, in moral language, and in a proposed shield. Risked: the autumn of 1983 showed the cost of conducting that confrontation without contact, a destroyed airliner and an exercise that each side had to read in the dark. Grade the table generously on wording and strictly on dates and sequence.")

# ------------------------------------------------------ 29 EXIT
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Why did the rivals step back in the 1970s, and why did the confrontation return in the 1980s? Argue it from the documents, and state the danger of 1983 no more strongly than its evidence supports.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Summit File: SALT I, Helsinki, Afghanistan, the evil empire speech, and SDI'),
        ('Notebook', 'Notebook page: the turn from easing to pressure in five stages'),
        ('Quick check', 'Naming the Adversary: the evil empire passage read closely'),
        ('Writing', 'Why Détente Ended: tried and failed, or abandoned, argued from the texts')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: what SALT I froze and left free, the two sides of the Helsinki bargain, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by handing the lesson to the work. The activity, The Summit File, runs five stations in the order of the record: the SALT I agreement text, the Helsinki human rights principle, a labeled summary of the Afghanistan invasion and the American answer, the evil empire speech from the audited bank record, and the Strategic Defense Initiative announcement, ending with a sorting of the five records by direction and a verdict on why détente ended. The notebook page holds the five stages with direction as its own column, so the turn from easing to pressure stays visible. The quick check, Naming the Adversary, tests close reading of the speech against the détente documents behind it. The writing task, Why Détente Ended, requires one side, three dated pieces of evidence, and an answer to the strongest fact against the side chosen, with the Able Archer danger stated as the debated reading it is. The exit ticket has three parts: what the SALT freeze covered and left free, the two sides of the Helsinki bargain, and the lesson question in two or three sentences.")

dc.save(OUT)
