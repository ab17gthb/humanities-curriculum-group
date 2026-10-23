#!/usr/bin/env python3
"""Build the Colonial America unit test (50 points) in the four part
format: matching 15, multiple choice 20, sources 10, essay 5, with every
item tagged to the blueprint in the key. Coverage is recomputed from
the tags this script prints. Matching descriptions are read verbatim
from the shared build spec (unit-spec.md in this folder). Sources are
quoted verbatim from the audited TPSP bank records in colonial.json,
with cuts marked [...] and the edition named in each Source line. The
Join, or Die cartoon is presented from the bank record's description
and is not reproduced.
"""
import json
import os
import re

UNIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "unit-spec.md")
BANK = os.path.expanduser(
    "~/workspace/primary-source/vite-react-main/public/data/colonial.json")

CSS = """
@page { size: letter; margin: 0.55in 0.75in 0.7in; }
* { box-sizing: border-box; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 11.5pt; color: #000; line-height: 1.35; margin: 0; }
.nameline { display: flex; justify-content: space-between; gap: 1em; }
h1 { font-size: 19pt; margin: 12pt 0 4pt; line-height: 1.2; }
h2 { font-size: 14.5pt; margin: 16pt 0 6pt; }
h3 { font-size: 12.5pt; margin: 14pt 0 4pt; break-after: avoid; }
p { margin: 0 0 7pt; }
.directions { margin-bottom: 4pt; }
.q { margin: 10pt 0 0; }
.qa { break-inside: avoid; }
.sp-a { height: 0.8in; }
.sp-b { height: 1.3in; }
.sp-c { height: 7.3in; }
.essay { break-before: page; }
.essay h2:first-child { margin-top: 0; }
.opts { margin: 2pt 0 0 16pt; }
.opts span { display: block; }
table.match { border-collapse: collapse; width: 100%; margin: 4pt 0 10pt; }
table.match td { padding: 3.5pt 6pt; font-size: 11.5pt; vertical-align: top; }
table.match td.n { width: 4%; }
table.match td.t { width: 30%; }
.source { border: 1.5px solid #000; padding: 8pt 11pt; margin: 8pt 0; break-inside: avoid; }
.source .srclabel { font-weight: bold; margin-bottom: 4pt; }
.source img { display: block; max-width: 3.4in; max-height: 3.2in; margin: 2pt auto 4pt; }
.caption { font-size: 9pt; font-style: italic; text-align: center; margin: 0 0 2pt; }
.key { break-before: page; }
.key h2:first-child { margin-top: 0; }
.brandmark { margin: 0 0 4pt; line-height: 0; } .brandmark img { width: 1.35in; }
"""


def spec_definition(spec_text, term):
    m = re.search(r"^- " + re.escape(term) + r": (.+)$", spec_text, re.M)
    if not m:
        raise SystemExit("definition not found in spec for: " + term)
    return m.group(1)


# (term, blueprint entry) one term per blueprint entry; the description
# printed is the spec definition for the term, verbatim
MATCH_TERMS = [
    ("Iroquois Confederacy", 1),
    ("Columbian Exchange", 2),
    ("encomienda", 3),
    ("fur trade", 4),
    ("Jamestown", 5),
    ("Bacon's Rebellion", 6),
    ("Mayflower Compact", 7),
    ("Salem witch trials", 8),
    ("William Penn", 9),
    ("Navigation Acts", 10),
    ("Middle Passage", 11),
    ("Stono Rebellion", 12),
    ("salutary neglect", 13),
    ("Great Awakening", 14),
    ("Treaty of Paris (1763)", 15),
]
# letter order for descriptions (index into MATCH shuffled by hand, so
# the descriptions run unit wide and no match can be solved from one
# lesson's list alone)
ORDER = [4, 12, 1, 9, 6, 14, 2, 10, 0, 7, 13, 3, 11, 5, 8]

# (question, options[4], correct index, blueprint entry)
# Blueprint order by design: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
# 14, 15, 1, 6, 11, 13, 15.
MC = [
    ("The Iroquois Confederacy joined five, later six, Native nations in present-day New York in order to",
     ["trade beaver pelts to French merchants on the St. Lawrence",
      "keep peace among themselves and deal jointly with outsiders under the Great Law",
      "build earthen mounds at a center of trade and ceremony",
      "elect representatives to the House of Burgesses"], 1, 1),
    ("The deadliest part of the Columbian Exchange for the peoples of the Americas was",
     ["the arrival of horses, which changed hunting on the plains",
      "the arrival of wheat and cattle from Europe",
      "European diseases, which spread through populations that had little resistance to them and killed on a scale no army could match",
      "the printing of Columbus's letter across Europe"], 2, 2),
    ("Under the encomienda system, a Spanish colonist received",
     ["the right to demand tribute and labor from Indigenous people in a given area, in return for supposed protection and Christian teaching",
      "fifty acres of land for every immigrant whose passage he paid",
      "a charter to govern a colony and draw its rents and fees",
      "a license to trade manufactured goods for beaver pelts"], 0, 3),
    ("The exchange at the center of French colonization in North America was",
     ["tobacco grown for sale in England",
      "silver mined and shipped to Spain",
      "sugar grown on plantations in the islands",
      "manufactured goods traded to Indigenous hunters for beaver pelts and other furs"], 3, 4),
    ("Jamestown, founded in 1607, was planted by",
     ["the Pilgrims, after signing a compact aboard the Mayflower",
      "the Virginia Company, a joint-stock company whose investors pooled their money and shared its risks",
      "William Penn, as a holy experiment for his persecuted faith",
      "Catholic orders founding a religious settlement"], 1, 5),
    ("After Bacon's Rebellion of 1676, Virginia's great planters turned increasingly to enslaved African labor because",
     ["the Navigation Acts required enslaved labor on tobacco plantations",
      "indentured servants had stopped coming to Virginia altogether",
      "enslaved people were bound for life, harder to free, and easier to mark than former servants who had gained their freedom and could rebel",
      "the House of Burgesses had outlawed indentured servitude"], 2, 6),
    ("The Mayflower Compact, signed aboard ship in 1620, created",
     ["the first written constitution in English America",
      "a government by the consent of the governed for the Plymouth colony",
      "an elected assembly for the Virginia colony",
      "a league of Native nations under the Great Law"], 1, 7),
    ("Anne Hutchinson was tried and banished from Massachusetts Bay in 1637 and 1638 because",
     ["she argued that the king had no right to grant Indigenous land",
      "she was accused of witchcraft at Salem",
      "she printed attacks on the royal governor in a newspaper",
      "her teaching that faith alone brought salvation challenged the colony's ministers"], 3, 8),
    ("William Penn founded Pennsylvania, beginning with its charter of 1681, as",
     ["a tobacco colony on the James River",
      "a trading town of many languages on the Hudson",
      "a holy experiment in government by his persecuted faith, the Quakers",
      "a viceroyalty governed from Mexico City"], 2, 9),
    ("The Navigation Acts, beginning in 1651, required that",
     ["colonial trade travel in English or colonial ships and certain colonial goods be sold only to England",
      "every colony elect an assembly and vote its own taxes",
      "colonial settlement stop west of the Appalachian Mountains",
      "enslaved people's children be born free if baptized"], 0, 10),
    ("Virginia's statutes of the 1660s rebuilt slavery as hereditary property by providing that",
     ["a child's status followed the father's condition and baptism freed the enslaved",
      "a child's enslaved status followed the mother's, and baptism did not free an enslaved person",
      "enslaved people could sue in the colony's courts",
      "every enslaved person was freed after a term of seven years"], 1, 11),
    ("The Stono Rebellion of September 1739 was",
     ["a Virginia uprising of frontier settlers who burned Jamestown",
      "a march of printers demanding a free press in New York",
      "an uprising near Charleston in which enslaved Africans seized weapons and marched toward Spanish Florida, after which the colonies tightened their slave codes",
      "an attack on British forts by the nations of the Great Lakes"], 2, 12),
    ("The Zenger trial of 1735 in New York ended when",
     ["the jury acquitted printer John Peter Zenger of seditious libel after his lawyer argued that true statements could not be libel",
      "the governor pardoned Zenger before the trial began",
      "the court changed the law of libel for every colony",
      "Zenger was banished to Rhode Island"], 0, 13),
    ("George Whitefield's tours of the colonies during the Great Awakening",
     ["preached the sermon Sinners in the Hands of an Angry God at Enfield",
      "founded Rhode Island on religious toleration",
      "were held inside meetinghouses for church members only",
      "drew open-air crowds in the thousands and made him the colonies' first shared celebrity"], 3, 14),
    ("The Treaty of Paris of February 1763 gave Britain",
     ["Louisiana and the lands west of the Mississippi",
      "Canada and all French territory east of the Mississippi River except New Orleans",
      "the right to settle west of the Appalachian Mountains",
      "France's sugar islands and its fur trade posts"], 1, 15),
    ("Tenochtitlan, as the Spanish found it in 1519, was",
     ["the largest city of the Mississippian culture, known for its earthen mounds",
      "a farming town of the Haudenosaunee league",
      "the capital of the Aztec empire, built on an island in Lake Texcoco and one of the largest cities in the world in 1500",
      "a Spanish viceroyalty governed from Mexico City"], 2, 1),
    ("The headright system recruited laborers for Virginia by",
     ["granting fifty acres of land to any person who paid for an immigrant's passage to the colony",
      "paying wages in tobacco to every servant who finished a term",
      "granting a colonist the tribute and labor of Indigenous people in a given area",
      "sending prisoners to the colony for life"], 0, 6),
    ("The figures of the Trans-Atlantic Slave Trade Database, stated as its estimates, put the Atlantic slave trade at",
     ["about 1.5 million people carried from Africa, most of whom survived",
      "some 12.5 million people carried from Africa between the 1500s and the 1800s, about 10.7 million of whom survived the crossing",
      "some 25 million people carried from Africa before 1700 alone",
      "about 500,000 people carried to England's mainland colonies, and no others"], 1, 11),
    ("Salutary neglect, through much of the early 1700s, was the British practice of",
     ["taxing the colonies directly for their own defense",
      "closing the colonial assemblies and ruling by governor alone",
      "forbidding colonial trade with every port but London",
      "leaving the colonies largely to govern themselves while Britain attended to wars and politics in Europe"], 3, 13),
    ("The Proclamation of 1763, issued in October of that year,",
     ["gave Canada to Britain and ended the French and Indian War",
      "forbade colonial settlement west of the Appalachian Mountains, to reserve the land for Indigenous peoples and prevent new frontier wars",
      "united the colonies under one government for defense",
      "required colonial goods to be sold only to England"], 1, 15),
]

# Source passages: each segment must occur verbatim in the bank record;
# the builder checks that and joins segments with a marked cut where
# text is omitted between them.
COLUMBUS_SEGMENTS = [
    "I have determined to write you this letter to inform you of everything that has been done and discovered in this voyage of mine. On the thirty-third day after leaving Cadiz I came into the Indian Sea, where I discovered many islands inhabited by numerous people. I took possession of all of them for our most fortunate King by making public proclamation and unfurling his standard, no one making any resistance.",
    "Besides, this Hispana abounds in various kinds of species, gold and metals.",
    "But when they see that they are safe, and all fear is banished, they are very guileless and honest, and very liberal of all they have. No one refuses the asker anything that he possesses; on the contrary they themselves invite us to ask for it. They manifest the greatest affection towards all of us, exchanging valuable things for trifles, content with the very least thing or nothing at all.",
    "I gave them many beautiful and pleasing things, which I had brought with me, for no return whatever, in order to win their affection, and that they might become Christians and inclined to love our King and Queen and Princes and all the people of Spain; and that they might be eager to search for and gather and give to us what they abound in and we greatly need.",
]
EQUIANO_SEGMENTS = [
    "The stench of the hold while we were on the coast was so intolerably loathsome, that it was dangerous to remain there for any time, and some of us had been permitted to stay on the deck for the fresh air; but now that the whole ship's cargo were confined together, it became absolutely pestilential. The closeness of the place, and the heat of the climate, added to the number in the ship, which was so crowded that each had scarcely room to turn himself, almost suffocated us. This produced copious perspirations, so that the air soon became unfit for respiration, from a variety of loathsome smells, and brought on a sickness among the slaves, of which many died, thus falling victims to the improvident avarice, as I may call it, of their purchasers.",
    "The shrieks of the women, and the groans of the dying, rendered the whole a scene of horror almost inconceivable.",
]
JOIN_SEGMENTS = [
    "A woodcut of a snake cut into eight segments, each labeled with the initials of a colony or region: S.C., N.C., V., M., P., N.J., N.Y., and N.E. Beneath the snake is a bold caption urging the colonies to unite.",
    'Transcript: "JOIN, or DIE." Segment labels: "S.C." "N.C." "V." "M." "P." "N.J." "N.Y." "N.E."',
]


def bank_record(record_id):
    data = json.load(open(BANK))
    for record in data["sources"]:
        if record["id"] == record_id:
            return record
    raise SystemExit("bank record not found: " + record_id)


def quoted_passage(record, segments):
    text = record["text"]
    for segment in segments:
        if segment not in text:
            raise SystemExit("segment not verbatim in bank record "
                             + record["id"] + ": " + segment[:60])
    return " [...] ".join(segments)


def main():
    spec_text = open(SPEC).read()
    MATCH = [(term, bp, spec_definition(spec_text, term))
             for term, bp in MATCH_TERMS]

    columbus = bank_record("columbus-first-voyage-1493")
    equiano = bank_record("equiano-middle-passage")
    join = bank_record("join-or-die-1754")
    columbus_text = quoted_passage(columbus, COLUMBUS_SEGMENTS)
    equiano_text = quoted_passage(equiano, EQUIANO_SEGMENTS)
    for segment in JOIN_SEGMENTS:
        if segment not in join["text"]:
            raise SystemExit("segment not verbatim in bank record "
                             + join["id"] + ": " + segment[:60])

    P = []
    P.append("<!DOCTYPE html>")
    P.append('<html lang="en"><head><meta charset="utf-8">')
    P.append("<title>Unit Test: Colonial America</title>")
    P.append(f"<style>{CSS}</style></head><body>")
    P.append('<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>')
    P.append('<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>')
    P.append("<h1>Unit Test: Colonial America</h1>")
    P.append('<p class="directions"><strong>Total: 50 points.</strong> Part A is worth 15 points, Part B is worth 20 points, Part C is worth 10 points, Part D is worth 5 points. Write answers on this test. For Part C, answer in complete sentences and cite the sources by letter. For Part D, choose one prompt and write a complete essay.</p>')

    P.append("<h2>Part A: Matching (15 points)</h2>")
    P.append("<p>Match each term to its description. Each description is used once.</p>")
    P.append('<table class="match">')
    letters = "ABCDEFGHIJKLMNO"
    desc_by_pos = {}
    for pos, idx in enumerate(ORDER):
        desc_by_pos[idx] = letters[pos]
    rows_desc = [MATCH[idx][2] for idx in ORDER]
    for i, (term, bp, _) in enumerate(MATCH):
        P.append(f'<tr><td class="n">___</td><td class="t">{i + 1}. {term}</td><td>{letters[i]}. {rows_desc[i]}</td></tr>')
    P.append("</table>")

    P.append("<h2>Part B: Multiple Choice (20 points)</h2>")
    P.append("<p>Choose the best answer for each question.</p>")
    for i, (q, opts, _, _) in enumerate(MC, 1):
        P.append(f'<div class="qa"><p class="q"><strong>{i}.</strong> {q}</p><p class="opts">')
        for j, o in enumerate(opts):
            P.append(f"<span>{letters[j]}. {o}</span>")
        P.append("</p></div>")

    P.append("<h2>Part C: Sources (10 points)</h2>")
    P.append("<p>Answer each question in complete sentences, citing the sources by letter.</p>")
    P.append('<div class="source"><p class="srclabel">Source A</p>')
    P.append("<p>Christopher Columbus, letter reporting his first voyage, written on the voyage home, 1493. From Christopher Columbus, 'Columbus Reports on His First Voyage,' 1493 (Gilder Lehrman Institute). Cuts are marked with ellipses in brackets.</p>")
    P.append(f"<p>&ldquo;{columbus_text}&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>A1. (1 point)</strong> According to Columbus, what did he do with the islands he reached, and for whom did he say he did it? Name the two public acts he says he performed.</p><div class="sp-a"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>A2. (2 points)</strong> Columbus writes that he gave the islanders many pleasing things for no return whatever. State the two purposes he says those gifts were meant to serve.</p><div class="sp-b"></div></div>')
    P.append('<div class="source"><p class="srclabel">Source B</p>')
    P.append("<p>Olaudah Equiano, The Interesting Narrative, published in London, 1789. From Olaudah Equiano, 'The Interesting Narrative,' 1789 (Documenting the American South, UNC; from the London 1789 first edition; original spelling and punctuation preserved). Cuts are marked with ellipses in brackets.</p>")
    P.append(f"<p>&ldquo;{equiano_text}&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>B1. (2 points)</strong> Name two conditions in the hold that Equiano describes, and state what those conditions brought on among the enslaved people aboard.</p><div class="sp-b"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>B2. (2 points)</strong> Equiano writes that many died as victims of the improvident avarice of their purchasers. Explain what he is blaming in that phrase, and state the sounds he closes the passage with.</p><div class="sp-b"></div></div>')
    P.append('<div class="source"><p class="srclabel">Source C</p>')
    P.append("<p>Benjamin Franklin (attributed), Join, or Die, published in the Pennsylvania Gazette, May 9, 1754. From Benjamin Franklin (attributed), 'Join, or Die,' 1754 (Library of Congress; image described). The bank record describes the cartoon rather than reproducing it, and this test presents the cartoon from that description. The cartoon itself is not reproduced here.</p>")
    P.append(f"<p>The bank record describes the image in these words: &ldquo;{JOIN_SEGMENTS[0]}&rdquo;</p>")
    P.append(f"<p>{JOIN_SEGMENTS[1]}</p></div>")
    P.append('<div class="qa"><p class="q"><strong>C1. (1 point)</strong> Into how many segments is the snake cut, and what does each segment stand for?</p><div class="sp-a"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>C2. (2 points)</strong> Explain the warning the cartoon makes to the colonies in 1754, the year the French and Indian War began. What does the cut snake claim will happen to colonies that stay divided, and what does the caption order them to do instead?</p><div class="sp-b"></div></div>')

    P.append('<div class="essay"><h2>Part D: Essay (5 points)</h2>')
    P.append("<p>Choose <strong>one</strong> prompt and write a complete essay in the space below. Use specific evidence from the unit, and state the strongest point on the other side before you answer it.</p>")
    P.append('<p class="q"><strong>Prompt 1.</strong> Judge whether 1763 was a triumph or a warning. Build your answer on the Treaty of Paris, Pontiac\'s Rebellion, and the Proclamation of 1763.</p>')
    P.append('<p class="q"><strong>Prompt 2.</strong> Britain won the French and Indian War. Judge whether that victory solved the empire\'s problems or created them. Build your answer on the war\'s costs, the land settlement of 1763, and the part the colonies played in the war.</p>')
    P.append('<div class="sp-c"></div></div>')

    # ---------------- KEY ----------------
    from collections import Counter
    counts = Counter()
    P.append('<div class="key"><h2>Teacher Answer Key</h2>')
    P.append("<h3>Part A: Matching</h3>")
    for i, (term, bp, _) in enumerate(MATCH):
        counts[bp] += 1
        P.append(f"<p><strong>{i + 1}. {term}: {desc_by_pos[i]}</strong> (Blueprint {bp})</p>")
    P.append("<h3>Part B: Multiple Choice</h3>")
    for i, (q, opts, correct, bp) in enumerate(MC, 1):
        counts[bp] += 1
        P.append(f"<p><strong>{i}. {letters[correct]}</strong> (Blueprint {bp})</p>")
    P.append("<h3>Part C: Sources</h3>")
    key3 = [
        ("A1", 2, "Columbus writes that he took possession of all the islands for our most fortunate King, meaning Ferdinand of Spain, the king who had paid for the voyage. The two public acts he names are making public proclamation and unfurling his standard, with no one making any resistance. One point for the possession and the king together with both acts named."),
        ("A2", 2, "Columbus states two purposes for the gifts. The first was to win the islanders' affection, so that they might become Christians and inclined to love the King and Queen and Princes and all the people of Spain. The second was that they might be eager to search for and gather and give to the Spanish what they abound in and Spain greatly needed, the gold and goods the passage names for Hispana. One point for each purpose stated from the source."),
        ("B1", 11, "Equiano describes the hold's intolerable stench, the closeness of the place and the heat of the climate, a ship so crowded that each person had scarcely room to turn himself, copious perspirations, and air made unfit for respiration by loathsome smells. Those conditions, he writes, brought on a sickness among the slaves, of which many died. Full credit requires any two conditions from the passage and the sickness and deaths they brought on."),
        ("B2", 11, "By the improvident avarice of their purchasers Equiano blames the reckless greed of the buyers who crowded the ship, the greed that packed people into the hold without provision for their lives. He closes the passage with the shrieks of the women and the groans of the dying, which he says rendered the whole a scene of horror almost inconceivable. One point for the blame explained and one point for both sounds named."),
        ("C1", 15, "The snake is cut into eight segments. Each segment stands for a colony or region, labeled with its initials, S.C., N.C., V., M., P., N.J., N.Y., and N.E. One point for the number and what the segments stand for together."),
        ("C2", 15, "The cartoon warns the colonies that divided they are a snake in pieces, dead and unable to act, at the opening of a war with France in North America. A colony standing alone could be defeated alone, and the cut pieces claim the colonies share one body and one fate. The caption orders the remedy in its own words, JOIN, or DIE, that the colonies unite, as Franklin's Albany Plan of Union proposed that same summer, for defense and for relations with Indigenous nations. Full credit requires the fate claimed for divided colonies and the union ordered, tied to the war of 1754."),
    ]
    for label, bp, ans in key3:
        counts[bp] += 1
        P.append(f"<p><strong>{label}.</strong> {ans} (Blueprint {bp})</p>")
    P.append("<h3>Part D: Essay</h3>")
    counts[15] += 1
    P.append("<p>The essay is scored on the six part holistic scale below, whichever prompt the student chose. (Blueprint 15)</p>")
    P.append("<p><strong>Score 5.</strong> A clear judgment is stated and held through the essay. At least three pieces of specific evidence from the unit are used accurately, the strongest point on the other side is stated fairly and answered, and the writing is organized in paragraphs with a conclusion that follows from the evidence.</p>")
    P.append("<p><strong>Score 4.</strong> A clear judgment is stated and mostly held. Two or three pieces of specific evidence are used accurately, the other side is stated and answered, and the organization holds, with minor lapses in precision or development.</p>")
    P.append("<p><strong>Score 3.</strong> A judgment is stated but drifts, or the evidence is specific in places and general in others. The other side is mentioned but answered thinly, or the answer to it is asserted rather than argued.</p>")
    P.append("<p><strong>Score 2.</strong> The essay retells the events of 1763 without a judgment that the evidence is made to serve, or the judgment is stated but supported by only one accurate piece of evidence. The other side does not appear.</p>")
    P.append("<p><strong>Score 1.</strong> The response is a fragment, a single point restated, or evidence is used inaccurately in ways that change its meaning. Little of the prompt is answered.</p>")
    P.append("<p><strong>Score 0.</strong> The response is blank, off the prompt, or copies the prompt without answering it.</p>")
    P.append("<p>For Prompt 1, strong evidence includes the Treaty of Paris of February 1763 giving Britain Canada and the French lands east of the Mississippi, Pontiac's Rebellion taking British forts in the spring and summer of 1763, the Proclamation of October 1763 forbidding settlement west of the Appalachians, and settlers already crossing the line. For Prompt 2, strong evidence includes the war's cost in borrowed millions and a national debt nearly doubled, Britain's ministers resolving that the colonies should pay for their own defense, colonial soldiers serving beside regulars and meeting British contempt, and the land settlement of 1763 closing the west the colonists had expected the victory to open. Either prompt can earn full credit argued from either side of its question, provided the judgment is earned from the evidence and the other side is answered.</p>")
    P.append("</div></body></html>")
    out = os.path.join(UNIT, "unit-test", "unit-test.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write("\n".join(P))
    print("coverage from printed tags:", dict(sorted(counts.items())))
    print("min per entry:", min(counts.values()), "entries covered:", len(counts))
    print("total items tagged:", sum(counts.values()))

if __name__ == "__main__":
    main()
