#!/usr/bin/env python3
"""Build the Founding unit test (50 points) in the four part format:
matching 15, multiple choice 20, sources 10, essay 5, with every item
tagged to the blueprint in the key. Coverage is recomputed from the
tags this script prints. Matching descriptions are read verbatim from
the shared build spec (unit-spec.md in this folder). Sources are
quoted verbatim from the audited TPSP bank records in founding.json,
with cuts marked [...] and the edition named in each Source line.
"""
import json
import os
import re

UNIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "unit-spec.md")
BANK = os.path.expanduser(
    "~/workspace/primary-source/vite-react-main/public/data/founding.json")

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
    ("Stamp Act", 1),
    ("Declaratory Act", 2),
    ("Intolerable Acts", 3),
    ("First Continental Congress", 4),
    ("Common Sense", 5),
    ("Declaration of Independence", 6),
    ("Battle of Saratoga", 7),
    ("Battle of Yorktown", 8),
    ("Dunmore's Proclamation", 9),
    ("inflation", 10),
    ("Articles of Confederation", 11),
    ("Shays's Rebellion", 12),
    ("Great Compromise", 13),
    ("Three-Fifths Compromise", 14),
    ("Bill of Rights", 15),
]
# letter order for descriptions (index into MATCH shuffled by hand, so
# the descriptions run unit wide and no match can be solved from one
# lesson's list alone)
ORDER = [7, 3, 11, 0, 13, 5, 9, 1, 14, 6, 10, 2, 12, 4, 8]

# (question, options[4], correct index, blueprint entry)
# Blueprint order by design: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
# 14, 15, 3, 8, 11, 13, 15.
MC = [
    ("Britain's ministers designed the revenue program of 1764 and 1765 chiefly because",
     ["the colonies had refused to send soldiers to fight in the French and Indian War",
      "Britain's national debt had nearly doubled in the war, and its ministers resolved that the colonies should pay for their own defense",
      "Parliament wanted to punish Boston for destroying the tea",
      "the king needed money to pay for a war with Spain"], 1, 1),
    ("The Declaratory Act of 1766, passed the same day Parliament repealed the Stamp Act, declared that",
     ["the colonies owed no taxes to Britain of any kind",
      "only the colonial assemblies could tax the colonies",
      "Parliament had power to make laws for the colonies in all cases whatsoever",
      "the Townshend duties would be repealed within the year"], 2, 2),
    ("The Tea Act of 1773 angered colonial merchants and protesters chiefly because it",
     ["raised the price of tea in the colonies",
      "banned the import of tea from every port but London",
      "required colonists to buy their tea only in Boston",
      "let the East India Company sell tea directly in the colonies, cutting out colonial merchants, while keeping the Townshend tax on tea in place"], 3, 3),
    ("The fighting at Lexington and Concord on April 19, 1775 began when",
     ["British regulars marched out of Boston to seize colonial military stores at Concord and met armed militia on Lexington green",
      "the Continental Congress voted for independence",
      "colonists boarded the tea ships in Boston Harbor",
      "Washington crossed the Delaware to attack Trenton"], 0, 4),
    ("In Common Sense, Thomas Paine argued that",
     ["the colonies should petition the king one final time before resisting",
      "Parliament alone, and not the king, was the colonies' true enemy",
      "monarchy and hereditary succession themselves were corrupt, and America should declare independence and found a republic",
      "the colonies should accept Parliament's claim to represent them"], 2, 5),
    ("Before adopting the Declaration of Independence, Congress cut from Jefferson's draft a passage that",
     ["listed life, liberty, and the pursuit of happiness as unalienable rights",
      "charged the king with waging cruel war against human nature itself in the slave trade and with blocking colonial attempts to end it",
      "named the grievances against Parliament",
      "pledged the signers' lives, fortunes, and sacred honor"], 1, 6),
    ("The American victory at Saratoga in the fall of 1777 changed the war most because it",
     ["captured New York City from the British",
      "forced General Cornwallis to surrender his army",
      "ended the fighting in the South",
      "persuaded France that the Americans could beat a British army in the field, bringing the French alliance"], 3, 7),
    ("Cornwallis surrendered at Yorktown in October 1781 because",
     ["his army had been destroyed at Camden the year before",
      "Washington and Rochambeau's armies closed around him on land while a French fleet sealed the Chesapeake against rescue or escape",
      "Congress had offered him generous terms in 1778",
      "the Loyalist forces in Virginia had already surrendered"], 1, 8),
    ("Dunmore's Proclamation of November 1775 offered freedom to",
     ["every enslaved person in all thirteen colonies",
      "Black soldiers who enlisted in the Continental Army",
      "enslaved people and indentured servants held by rebels who would leave their masters and bear arms for the king",
      "Native nations that allied with Britain against the colonies"], 2, 9),
    ("The Loyalist exodus at the war's end carried some sixty thousand or more people out of the United States, among them",
     ["the entire population of Boston",
      "General Cornwallis and his army",
      "no one of African descent",
      "some three thousand Black Loyalists whose names, ages, and former owners the British recorded in the Book of Negroes at New York in 1783"], 3, 10),
    ("The Northwest Ordinance of 1787 provided that the territory north of the Ohio River would",
     ["remain a colony of the original thirteen states permanently",
      "bar slavery and become states on equal terms with the original states in time",
      "be sold to Britain to pay the Confederation's war debts",
      "be governed directly by the Continental Army"], 1, 11),
    ("Shays's Rebellion of 1786 and 1787 began when indebted farmers in western Massachusetts",
     ["marched on Philadelphia to demand a stronger Congress",
      "attacked the British forts still held on the frontier",
      "closed the courts to stop foreclosure judgments against farmers who could not pay their debts and taxes",
      "refused to ratify the Constitution in their state convention"], 2, 12),
    ("The Virginia Plan, proposed at the Constitutional Convention, called for",
     ["a one house legislature with equal votes for every state",
      "a strong national government with a legislature apportioned by population",
      "the Articles of Confederation kept exactly as they stood",
      "a president chosen by the state governors for a life term"], 1, 13),
    ("Under the Constitution as framed in 1787, Congress could not prohibit the Atlantic slave trade before the year",
     ["1791",
      "1800",
      "1808",
      "1820"], 2, 14),
    ("The Massachusetts compromise of February 1788, which saved ratification in that state, settled that Massachusetts would",
     ["ratify only after every other state had ratified",
      "refuse ratification until a bill of rights was written into the document",
      "be exempt from the Constitution's tax powers",
      "ratify unconditionally while recommending amendments that the first Congress should take up"], 3, 15),
    ("Parliament answered the Boston Tea Party with the acts colonists called Intolerable, which included",
     ["the Stamp Act and the Declaratory Act",
      "closing Boston's port to trade until the destroyed tea was paid for",
      "repealing the Townshend tax on tea",
      "disbanding the Massachusetts assembly by name in the act itself"], 1, 3),
    ("The Treaty of Paris of September 3, 1783 settled the war by providing that Britain",
     ["kept Canada and all the lands east of the Mississippi River",
      "paid the colonies' war debts in full",
      "recognized the United States as free, sovereign, and independent, with a boundary at the Mississippi and the Great Lakes",
      "withdrew its armies from every part of North America, including Canada"], 2, 8),
    ("Under the Articles of Confederation, Congress could not",
     ["declare war or make treaties",
      "coin money or run a post office",
      "levy a tax, regulate commerce, or compel a state to obey",
      "admit territories as new states"], 2, 11),
    ("The Great Compromise settled the Convention's deadlock over representation by providing",
     ["a House of Representatives apportioned by population and a Senate of two members from every state",
      "equal votes for every state in both houses of Congress",
      "representation by wealth in both houses of Congress",
      "a single house chosen by the state legislatures"], 0, 13),
    ("In Federalist No. 51, Madison argued that the Constitution's structure would oblige the government to control itself because",
     ["officeholders could be trusted to act as angels once elected",
      "the states would keep all real power and the national government almost none",
      "a bill of rights alone would restrain every branch",
      "ambition in one branch would be made to counteract ambition in another, each branch given the means and the motive to resist the rest"], 3, 15),
]


def bank_record(record_id):
    data = json.load(open(BANK))
    for record in data["sources"]:
        if record["id"] == record_id:
            return record
    raise SystemExit("bank record not found: " + record_id)


def quoted_passage(record):
    """Rebuild the bank record's text as one flowing passage. Every
    segment between the record's own cut markers must occur verbatim
    in the record; the segments are rejoined with the marked cut, and
    a cut the record marks at the end of the text is preserved."""
    text = record["text"]
    trailing = text.rstrip().endswith("[...]")
    segments = [s.strip().replace("\n", " ") for s in text.split("[...]")]
    segments = [s for s in segments if s]
    for segment in segments:
        if segment.replace("  ", " ") not in text.replace("\n", " "):
            raise SystemExit("segment not verbatim in bank record "
                             + record["id"] + ": " + segment[:60])
    passage = " [...] ".join(segments)
    if trailing:
        passage += " [...]"
    return passage


def main():
    spec_text = open(SPEC).read()
    MATCH = [(term, bp, spec_definition(spec_text, term))
             for term, bp in MATCH_TERMS]

    paine = bank_record("paine-common-sense-1776")
    declaration = bank_record("declaration-of-independence")
    federalist = bank_record("federalist-10")
    paine_text = quoted_passage(paine)
    declaration_text = quoted_passage(declaration)
    federalist_text = quoted_passage(federalist)

    P = []
    P.append("<!DOCTYPE html>")
    P.append('<html lang="en"><head><meta charset="utf-8">')
    P.append("<title>Unit Test: The Founding</title>")
    P.append(f"<style>{CSS}</style></head><body>")
    P.append('<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>')
    P.append('<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>')
    P.append("<h1>Unit Test: The Founding</h1>")
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
    P.append("<p>Thomas Paine, Common Sense, a pamphlet published at Philadelphia in January 1776. From Thomas Paine, 'Common Sense,' 1776 (Project Gutenberg; from the February 14, 1776 Philadelphia edition). Cuts are marked with ellipses in brackets.</p>")
    P.append(f"<p>&ldquo;{paine_text}&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>A1. (1 point)</strong> Paine writes that government even in its best state is but a necessary evil. State what he says heightens the calamity when people suffer the same miseries under a government that they might expect in a country without one.</p><div class="sp-a"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>A2. (2 points)</strong> Paine calls on those who love mankind to receive the fugitive and prepare an asylum for mankind. Identify the fugitive from the passage, and state what Paine says Americans have it in their power to do.</p><div class="sp-b"></div></div>')
    P.append('<div class="source"><p class="srclabel">Source B</p>')
    P.append("<p>Thomas Jefferson (for the Continental Congress), the Declaration of Independence, adopted July 4, 1776; the preamble passage. From Thomas Jefferson (for the Continental Congress), 'Declaration of Independence,' 1776 (National Archives). Cuts are marked with ellipses in brackets.</p>")
    P.append(f"<p>&ldquo;{declaration_text}&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>B1. (2 points)</strong> According to the passage, from what do governments derive their just powers, and what may the people do whenever a form of government becomes destructive of the ends the passage names?</p><div class="sp-b"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>B2. (2 points)</strong> The passage says prudence dictates that governments long established should not be changed for light and transient causes. State the condition the passage sets for the point at which throwing off a government becomes not only a right but a duty.</p><div class="sp-b"></div></div>')
    P.append('<div class="source"><p class="srclabel">Source C</p>')
    P.append("<p>James Madison, Federalist No. 10, a newspaper essay published in New York in 1787 under the name Publius. From James Madison, 'Federalist No. 10,' 1787 (Congress.gov; spelling modernized). Cuts are marked with ellipses in brackets.</p>")
    P.append(f"<p>&ldquo;{federalist_text}&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>C1. (1 point)</strong> State Madison\'s definition of a faction as the passage gives it.</p><div class="sp-a"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>C2. (2 points)</strong> State the two things Madison says extending the sphere does to a factious majority, as the passage gives them.</p><div class="sp-b"></div></div>')

    P.append('<div class="essay"><h2>Part D: Essay (5 points)</h2>')
    P.append("<p>Choose <strong>one</strong> prompt and write a complete essay in the space below. Use specific evidence from the unit, and state the strongest point on the other side before you answer it.</p>")
    P.append('<p class="q"><strong>Prompt 1.</strong> Judge whether the Constitution of 1787, as a settlement of the founding generation\'s hardest question, protected slavery more than it limited it. Build your answer on the Three-Fifths Compromise, the clause barring Congress from ending the Atlantic slave trade before 1808, and the clause requiring the return of persons held to service who escaped into free states.</p>')
    P.append('<p class="q"><strong>Prompt 2.</strong> Judge whether the founding settlement, the Constitution as framed in 1787 and amended by 1791, struck the right balance between a government strong enough to act and one limited enough to trust. Build your answer on the Great Compromise, the division and checking of power in the frame, and the Bill of Rights the ratification contests produced.</p>')
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
        ("A1", 5, "Paine writes that when we suffer, or are exposed to the same miseries by a government, which we might expect in a country without government, our calamity is heightened by reflecting that we furnish the means by which we suffer. The point is that the sufferers themselves supply the government with the money and obedience it uses against them, and knowing it makes the suffering worse. One point for the reflection stated from the source."),
        ("A2", 5, "The fugitive is Freedom. Paine writes that freedom has been hunted round the globe, expelled by Asia and Africa, regarded as a stranger by Europe, and warned to depart by England, and he asks his readers to receive her and prepare in time an asylum for mankind. What Americans have it in their power to do, he writes, is to begin the world over again. One point for the fugitive identified and one point for the power stated."),
        ("B1", 6, "Governments derive their just powers from the consent of the governed. Whenever any form of government becomes destructive of the ends named in the passage, securing the unalienable rights of life, liberty, and the pursuit of happiness, it is the right of the people to alter or to abolish it and to institute new government. One point for the consent of the governed and one point for the right to alter or abolish and institute new government."),
        ("B2", 6, "The condition is a long train of abuses and usurpations, pursuing invariably the same object, which evinces a design to reduce the people under absolute despotism. Only when the abuses form that pattern and show that design does the passage call throwing off the government not only the people's right but their duty, and require them to provide new guards for their future security. Full credit requires the long train of abuses and the design of despotism, both stated."),
        ("C1", 15, "Madison defines a faction as a number of citizens, whether amounting to a majority or a minority of the whole, who are united and actuated by some common impulse of passion, or of interest, adverse to the rights of other citizens, or to the permanent and aggregate interests of the community. One point for the definition stated in full, the majority or minority together with the impulse and what it is adverse to."),
        ("C2", 15, "Extending the sphere takes in a greater variety of parties and interests, and Madison gives two results. First, it makes it less probable that a majority of the whole will have a common motive to invade the rights of other citizens. Second, if such a common motive exists, it makes it more difficult for all who feel it to discover their own strength and to act in unison with each other. One point for each result stated from the passage."),
    ]
    for label, bp, ans in key3:
        counts[bp] += 1
        P.append(f"<p><strong>{label}.</strong> {ans} (Blueprint {bp})</p>")
    P.append("<h3>Part D: Essay</h3>")
    counts[14] += 1
    P.append("<p>The essay is scored on the six part holistic scale below, whichever prompt the student chose. (Blueprint 14)</p>")
    P.append("<p><strong>Score 5.</strong> A clear judgment is stated and held through the essay. At least three pieces of specific evidence from the unit are used accurately, the strongest point on the other side is stated fairly and answered, and the writing is organized in paragraphs with a conclusion that follows from the evidence.</p>")
    P.append("<p><strong>Score 4.</strong> A clear judgment is stated and mostly held. Two or three pieces of specific evidence are used accurately, the other side is stated and answered, and the organization holds, with minor lapses in precision or development.</p>")
    P.append("<p><strong>Score 3.</strong> A judgment is stated but drifts, or the evidence is specific in places and general in others. The other side is mentioned but answered thinly, or the answer to it is asserted rather than argued.</p>")
    P.append("<p><strong>Score 2.</strong> The essay retells the framing or the ratification contests without a judgment that the evidence is made to serve, or the judgment is stated but supported by only one accurate piece of evidence. The other side does not appear.</p>")
    P.append("<p><strong>Score 1.</strong> The response is a fragment, a single point restated, or evidence is used inaccurately in ways that change its meaning. Little of the prompt is answered.</p>")
    P.append("<p><strong>Score 0.</strong> The response is blank, off the prompt, or copies the prompt without answering it.</p>")
    P.append("<p>For Prompt 1, strong evidence includes the three fifths count applied to both representation and direct taxation, which enlarged the slave states' weight in the House and, through the electoral college, in the presidency; the clause barring Congress from ending the Atlantic slave trade before 1808; the clause requiring the return of persons held to service escaping into free states; and the document's refusal to name slavery at all. Evidence on the other side includes the Northwest Ordinance of the same summer barring slavery north of the Ohio, the northern states' gradual emancipation acts already under way, and the argument that no union, and so no government able to act on the question later, was possible without the settlements. For Prompt 2, strong evidence includes the Great Compromise joining a people's House to a states' Senate, federalism dividing power between the nation and the states, separation of powers with the veto, advice and consent, and impeachment, the Massachusetts compromise that joined ratification to recommended amendments, and the Bill of Rights ratified by December 1791, including the Ninth and Tenth Amendments reserving undelegated powers and unlisted rights. Either prompt can earn full credit argued from either side of its question, provided the judgment is earned from the evidence and the other side is answered.</p>")
    P.append("</div></body></html>")
    out = os.path.join(UNIT, "unit-test", "unit-test.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write("\n".join(P))
    print("coverage from printed tags:", dict(sorted(counts.items())))
    print("min per entry:", min(counts.values()), "entries covered:", len(counts))
    print("total items tagged:", sum(counts.values()))

if __name__ == "__main__":
    main()
