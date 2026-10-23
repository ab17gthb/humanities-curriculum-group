#!/usr/bin/env python3
"""Build the Early Republic and Expansion unit test (50 points) in
the four part format: matching 15, multiple choice 20, sources 10,
essay 5, with every item in Parts A to C tagged to the blueprint in
the key and the essay guidance tagged by prompt. Coverage is
recomputed from the tags this script prints. Matching descriptions
are read verbatim from the shared build spec (unit-spec.md in this
folder). Sources are quoted verbatim from the audited TPSP bank
records, the Farewell Address in founding.json, the Monroe Doctrine
in early-republic.json, and O'Sullivan's annexation essay in
jackson-reform.json, with cuts marked [...] and the edition named in
each Source line from the record's sourceNote. Every quoted segment
is asserted verbatim against its bank record at build time.
"""
import json
import os
import re

UNIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "unit-spec.md")
BANK_DIR = os.path.expanduser(
    "~/workspace/primary-source/vite-react-main/public/data")

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
    ("Bank of the United States", 1),
    ("Farewell Address", 2),
    ("Sedition Act", 3),
    ("Twelfth Amendment", 4),
    ("Louisiana Purchase", 5),
    ("judicial review", 6),
    ("Corps of Discovery", 7),
    ("Sacagawea", 8),
    ("impressment", 9),
    ("Treaty of Ghent", 10),
    ("American System", 11),
    ("McCulloch v. Maryland", 12),
    ("Monroe Doctrine", 13),
    ("Missouri Compromise", 14),
    ("Manifest Destiny", 15),
]
# letter order for descriptions (index into MATCH shuffled by hand, so
# the descriptions run unit wide and no match can be solved from one
# lesson's list alone)
ORDER = [11, 4, 14, 1, 8, 6, 13, 0, 10, 3, 12, 5, 9, 2, 7]

# (question, options[4], correct index, blueprint entry)
# Blueprint order by design: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
# 13, 14, 15, 1, 5, 9, 11, 14.
MC = [
    ("Hamilton's financial program was a single design whose four parts were",
     ["a protective tariff, a national mint, a system of post roads, and a standing army",
      "selling the western lands, taxing imports only, borrowing from France, and paying the soldiers in land warrants",
      "funding the national debt at full value, assuming the states' war debts, chartering a national bank, and laying an excise tax on distilled whiskey",
      "a national university, a canal fund, a patent office, and a census of manufactures"], 2, 1),
    ("Washington's answer to the Whiskey Rebellion of 1794 showed that the new government would",
     ["enforce its laws itself, calling out a militia army of some thirteen thousand men and leading it part of the way west",
      "watch its laws go unenforced, as Congress had watched under the Articles of Confederation",
      "repeal the excise tax at the first sign of armed resistance",
      "ask the British army on the frontier to police western Pennsylvania"], 0, 2),
    ("The Sedition Act of 1798 made it a crime to",
     ["refuse militia service during the war scare with France",
      "trade with France while the undeclared naval war continued",
      "vote for a Republican candidate in a federal election",
      "publish false, scandalous, or malicious writing against the government, Congress, or the president"], 3, 3),
    ("The election of 1800 went to the House of Representatives because",
     ["Adams refused to leave office until Congress acted",
      "Jefferson and Burr tied at seventy three electoral votes because every Republican elector had voted for both men",
      "the Supreme Court ordered the House to choose the president",
      "no candidate had won a majority of the states' popular votes"], 1, 4),
    ("The Louisiana Purchase of 1803 changed the United States by",
     ["roughly doubling the nation's territory for fifteen million dollars in a single treaty with France",
      "adding Florida and Texas to the Union at the same stroke",
      "ending the wars with the Barbary states of North Africa",
      "giving the United States the Oregon Country as far as the Pacific"], 0, 5),
    ("In Marbury v. Madison, Chief Justice Marshall's opinion held that",
     ["Marbury had no right to his commission and the suit should never have been filed",
      "the Court must order Madison to deliver every commission Adams had signed",
      "Congress could abolish the federal courts whenever a president objected to a ruling",
      "the law granting the Court original jurisdiction in the case was itself unconstitutional, so the commission could not be ordered, while the Court claimed the power of judicial review"], 3, 6),
    ("Jefferson's instructions to Lewis named as the objects of the expedition",
     ["a military road to California and a survey of its gold fields",
      "a water communication across the continent for commerce, knowledge of the country and its peoples, and relations with the Native nations",
      "the capture of Santa Fe and the mapping of the Rio Grande",
      "a census of the French and Spanish settlers of Louisiana"], 1, 7),
    ("The meeting with the Shoshone in August 1805 gave the Corps its horses and its passage west after",
     ["Clark paid the Shoshone the full price they asked in gold coin",
      "the Corps defeated the Shoshone in a short battle on the river",
      "Sacagawea, interpreting for the Corps, recognized the chief Cameahwait as her brother",
      "a treaty signed at Fort Clatsop opened the mountains to the expedition"], 2, 8),
    ("Impressment, as Madison's war message laid the grievance before Congress in 1812, was",
     ["the tax Britain laid on American goods landed at British ports",
      "the French practice of seizing American ships in the Caribbean",
      "the drafting of American militiamen into state service on the frontier",
      "the British practice of stopping American ships at sea and forcing sailors, including American citizens, into service in the Royal Navy"], 3, 9),
    ("The Treaty of Ghent, signed December 24, 1814, ended the War of 1812 by",
     ["restoring the boundaries and possessions of 1811 and settling none of the questions of impressment or neutral rights over which the war had been declared",
      "ending impressment and guaranteeing American neutral rights by treaty",
      "ceding Canada to the United States in return for Florida",
      "paying the United States for the ships seized during the war"], 0, 10),
    ("Henry Clay's American System joined three parts, which were",
     ["free trade, a larger navy, and the sale of western lands",
      "state banks, no tariff at all, and canals built by the states alone",
      "a national bank, a protective tariff, and federally funded internal improvements",
      "a national mint, a patent system, and a university for the whole union"], 2, 11),
    ("In McCulloch v. Maryland in 1819, the Supreme Court held that",
     ["Maryland could tax the Bank because the states had kept the whole power of taxation",
      "Congress could charter a bank under its implied powers, and Maryland could not tax it, because the power to tax involves the power to destroy",
      "the Bank was unconstitutional and Maryland's tax was void for other reasons",
      "commerce among the states meant traffic alone and never navigation"], 1, 12),
    ("The Monroe Doctrine, declared in the president's annual message of December 2, 1823, held that",
     ["the United States would colonize the Pacific coast of South America itself",
      "Britain and the United States would govern the hemisphere together under the joint declaration Canning had proposed",
      "Spain could keep Florida if it surrendered its claims in Texas",
      "the American continents were no longer subjects for future colonization by any European power, and any attempt to extend the European system to this hemisphere would be viewed as dangerous to the United States"], 3, 13),
    ("The Missouri Compromise of 1820 settled the crisis in three parts, which were",
     ["Maine admitted as a free state, Missouri admitted as a slave state, and a line at 36 degrees 30 minutes drawn across the Louisiana Purchase lands, slavery barred north of it and permitted south",
      "Missouri admitted as a free state, Maine kept a district of Massachusetts, and no line drawn anywhere",
      "Missouri admitted with the Tallmadge Amendment in full force, and Maine admitted as a slave state",
      "both Maine and Missouri kept out of the Union until the question could be revisited in 1824"], 0, 14),
    ("Texas joined the United States in 1845 by",
     ["a treaty of annexation ratified by two thirds of the Senate",
      "purchase from Mexico for fifteen million dollars and the assumption of claims",
      "annexation by joint resolution of Congress, a simple majority of both houses doing what a treaty needing two thirds of the Senate could not",
      "a Supreme Court decision settling the Adams-Onís boundary in Texas's favor"], 2, 15),
    ("Jefferson and Madison opposed Hamilton's Bank chiefly on the ground that",
     ["a national bank would end slavery in the South too quickly",
      "the Constitution nowhere named a power to charter a bank, and they read the document's powers strictly",
      "the Bank's notes were printed in Britain and could be counterfeited",
      "Hamilton had chartered the Bank without asking Washington's leave"], 1, 1),
    ("Jefferson's constitutional scruple over the Louisiana Purchase was that",
     ["the price was larger than the sum Congress had appropriated for New Orleans",
      "France had no right to sell Louisiana because Spain had objected to the sale",
      "the Senate had already rejected an identical treaty the year before",
      "the Constitution gave no express power to acquire territory or govern it, and he drafted an amendment to supply the power before abandoning the draft as the Senate pressed for speed"], 3, 5),
    ("Tecumseh built his confederacy of Native nations on the claim that",
     ["the land was held by all the nations in common, so no single nation could sell it to the United States",
      "each nation was free to sell its own hunting grounds to the highest bidder",
      "Britain had promised the confederacy the whole of Canada after the war",
      "Prophetstown should be recognized as the capital of a separate state"], 0, 9),
    ("The Second Bank of the United States was chartered in 1816 chiefly because",
     ["the Panic of 1819 had already ruined the state banks and their notes",
      "Britain had required a national bank as a term of the Treaty of Ghent",
      "the war had exposed the disorder of a currency issued by hundreds of state banks",
      "Henry Clay needed the Bank's charter to carry Kentucky for Monroe"], 2, 11),
    ("Jefferson's letter to John Holmes of April 1820 called the Missouri question",
     ["a settled matter that required no further thought from anyone",
      "a fire bell in the night and the knell of the Union, a geographical line coinciding with a marked principle, moral and political, that would deepen with every new irritation",
      "proof that the line of thirty-six thirty would hold for a century",
      "a question the Supreme Court would settle in its next term"], 1, 14),
]


def bank_record(filename, record_id):
    data = json.load(open(os.path.join(BANK_DIR, filename)))
    for record in data["sources"]:
        if record["id"] == record_id:
            return record
    raise SystemExit("bank record not found: " + record_id)


def quoted_passage(record, segments):
    """Join verbatim segments of the bank record's text with marked
    cuts. Every segment is asserted verbatim against the record, a
    leading cut is marked when the passage does not begin where the
    record begins, and a trailing cut is marked when the record's own
    text ends with one or the passage stops short of the record's
    end."""
    full = " ".join(record["text"].split())
    norm = [" ".join(s.split()) for s in segments]
    for segment in norm:
        if segment not in full:
            raise SystemExit("segment not verbatim in bank record "
                             + record["id"] + ": " + segment[:60])
    passage = " [...] ".join(norm)
    if not full.startswith(norm[0]):
        passage = "[...] " + passage
    body = full[:-len("[...]")].rstrip() if full.endswith("[...]") else full
    if full.endswith("[...]") or not body.endswith(norm[-1]):
        passage += " [...]"
    return passage


FAREWELL_SEGMENTS = [
    "The name of American, which belongs to you in your national capacity, must always exalt the just pride of patriotism more than any appellation derived from local discriminations.",
    "It serves always to distract the public councils and enfeeble the public administration. It agitates the community with ill-founded jealousies and false alarms, kindles the animosity of one part against another, foments occasionally riot and insurrection.",
    "The great rule of conduct for us in regard to foreign nations is in extending our commercial relations, to have with them as little political connection as possible.",
    "It is our true policy to steer clear of permanent alliances with any portion of the foreign world; so far, I mean, as we are now at liberty to do it.",
]

MONROE_SEGMENTS = [
    "that the American continents, by the free and independent condition which they have assumed and maintain, are henceforth not to be considered as subjects for future colonization by any European powers.",
    "In the wars of the European powers in matters relating to themselves we have never taken any part, nor does it comport with our policy to do so. It is only when our rights are invaded or seriously menaced that we resent injuries or make preparation for our defense. With the movements in this hemisphere we are of necessity more immediately connected, and by causes which must be obvious to all enlightened and impartial observers.",
    "We owe it, therefore, to candor and to the amicable relations existing between the United States and those powers to declare that we should consider any attempt on their part to extend their system to any portion of this hemisphere as dangerous to our peace and safety.",
]

OSULLIVAN_SEGMENTS = [
    "It is now time for the opposition to the Annexation of Texas to cease.",
    "Texas is now ours. Already, before these words are written, her Convention has undoubtedly ratified the acceptance, by her Congress, of our proffered invitation into the Union.",
    "Why, were other reasoning wanting, in favor of now elevating this question of the reception of Texas into the Union, out of the lower region of our past party dissensions, up to its proper level of a high and broad nationality, it surely is to be found, found abundantly, in the manner in which other nations have undertaken to intrude themselves into it, between us and the proper parties to the case, in a spirit of hostile interference against us, for the avowed object of thwarting our policy and hampering our power, limiting our greatness and checking the fulfillment of our manifest destiny to overspread the continent allotted by Providence for the free development of our yearly multiplying millions.",
]


def main():
    spec_text = open(SPEC).read()
    MATCH = [(term, bp, spec_definition(spec_text, term))
             for term, bp in MATCH_TERMS]

    farewell = bank_record("founding.json", "washington-farewell-address")
    monroe = bank_record("early-republic.json", "monroe-doctrine")
    osullivan = bank_record("jackson-reform.json", "osullivan-annexation-1845")
    farewell_text = quoted_passage(farewell, FAREWELL_SEGMENTS)
    monroe_text = quoted_passage(monroe, MONROE_SEGMENTS)
    osullivan_text = quoted_passage(osullivan, OSULLIVAN_SEGMENTS)
    farewell_note = farewell["sourceNote"].replace('"', "'")
    monroe_note = monroe["sourceNote"].replace('"', "'")
    osullivan_note = osullivan["sourceNote"].replace('"', "'")

    P = []
    P.append("<!DOCTYPE html>")
    P.append('<html lang="en"><head><meta charset="utf-8">')
    P.append("<title>Unit Test: The Early Republic and Expansion</title>")
    P.append(f"<style>{CSS}</style></head><body>")
    P.append('<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>')
    P.append('<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>')
    P.append("<h1>Unit Test: The Early Republic and Expansion</h1>")
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
    P.append(f"<p>George Washington, the Farewell Address, a published letter of September 1796, printed as Washington retired after two terms. From {farewell_note} Cuts are marked with ellipses in brackets.</p>")
    P.append(f"<p>&ldquo;{farewell_text}&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>A1. (1 point)</strong> Washington writes that the name of American must exalt the just pride of patriotism more than any appellation derived from what?</p><div class="sp-a"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>A2. (2 points)</strong> State the great rule of conduct the passage gives for dealings with foreign nations, and state the true policy it names toward permanent alliances.</p><div class="sp-b"></div></div>')
    P.append('<div class="source"><p class="srclabel">Source B</p>')
    P.append(f"<p>President James Monroe, the annual message to Congress of December 2, 1823; the passages known as the Monroe Doctrine. From {monroe_note} Cuts are marked with ellipses in brackets.</p>")
    P.append(f"<p>&ldquo;{monroe_text}&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>B1. (2 points)</strong> State what Monroe declares about the American continents and future colonization by European powers, and state what the United States will consider any attempt by those powers to extend their system to any portion of this hemisphere.</p><div class="sp-b"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>B2. (2 points)</strong> State the only condition under which, the passage says, the United States resents injuries or makes preparation for its defense, and state how the passage says the United States stands toward movements in this hemisphere.</p><div class="sp-b"></div></div>')
    P.append('<div class="source"><p class="srclabel">Source C</p>')
    P.append(f"<p>John L. O'Sullivan, the annexation editorial of 1845, written to rally support for the annexation of Texas. From {osullivan_note} Cuts are marked with ellipses in brackets.</p>")
    P.append(f"<p>&ldquo;{osullivan_text}&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>C1. (1 point)</strong> O\'Sullivan writes that it is now time for the opposition to cease. Opposition to what?</p><div class="sp-a"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>C2. (2 points)</strong> State what other nations are accused of checking, in the passage\'s own phrase for the nation\'s destiny, and state for what the continent is said to be allotted by Providence.</p><div class="sp-b"></div></div>')

    P.append('<div class="essay"><h2>Part D: Essay (5 points)</h2>')
    P.append("<p>Choose <strong>one</strong> prompt and write a complete essay in the space below. Use specific evidence from the unit, and state the strongest point on the other side before you answer it.</p>")
    P.append('<p class="q"><strong>Prompt 1.</strong> Judge whether the Missouri Compromise of 1820 settled the question of slavery\'s expansion or only postponed it. Build your answer on the pairing of Maine and Missouri, the line of thirty-six thirty drawn across the Louisiana Purchase lands, and Jefferson\'s fire bell warning in his letter to John Holmes of April 1820.</p>')
    P.append('<p class="q"><strong>Prompt 2.</strong> Judge whether Manifest Destiny described what the United States did in the 1840s or disguised it. Build your answer on the annexation of Texas by joint resolution, the division of Oregon at the 49th parallel, the war with Mexico and the cession at Guadalupe Hidalgo, and the Wilmot Proviso.</p>')
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
        ("A1", 2, "The name of American must exalt the just pride of patriotism more than any appellation derived from local discriminations. One point for the phrase stated from the source."),
        ("A2", 2, "The great rule of conduct in regard to foreign nations is, in extending our commercial relations, to have with them as little political connection as possible. The true policy is to steer clear of permanent alliances with any portion of the foreign world. One point for the rule of conduct and one point for the policy toward permanent alliances, both stated from the passage."),
        ("B1", 13, "Monroe declares that the American continents, by the free and independent condition which they have assumed and maintain, are henceforth not to be considered as subjects for future colonization by any European powers. He declares that the United States should consider any attempt on their part to extend their system to any portion of this hemisphere as dangerous to our peace and safety. One point for the colonization declaration and one point for the danger declared."),
        ("B2", 13, "The passage says it is only when our rights are invaded or seriously menaced that we resent injuries or make preparation for our defense. Toward movements in this hemisphere, the passage says, we are of necessity more immediately connected, by causes obvious to all enlightened and impartial observers. One point for the condition stated and one point for the hemisphere connection stated."),
        ("C1", 15, "The opposition O'Sullivan says should cease is the opposition to the Annexation of Texas. One point for the annexation of Texas named."),
        ("C2", 15, "Other nations are accused of checking the fulfillment of our manifest destiny to overspread the continent. The continent is said to be allotted by Providence for the free development of our yearly multiplying millions. One point for the destiny phrase stated and one point for the free development of the yearly multiplying millions."),
    ]
    for label, bp, ans in key3:
        counts[bp] += 1
        P.append(f"<p><strong>{label}.</strong> {ans} (Blueprint {bp})</p>")
    P.append("<h3>Part D: Essay</h3>")
    P.append("<p>The essay is scored on the six part holistic scale below, whichever prompt the student chose.</p>")
    P.append("<p><strong>Score 5.</strong> A clear judgment is stated and held through the essay. At least three pieces of specific evidence from the unit are used accurately, the strongest point on the other side is stated fairly and answered, and the writing is organized in paragraphs with a conclusion that follows from the evidence.</p>")
    P.append("<p><strong>Score 4.</strong> A clear judgment is stated and mostly held. Two or three pieces of specific evidence are used accurately, the other side is stated and answered, and the organization holds, with minor lapses in precision or development.</p>")
    P.append("<p><strong>Score 3.</strong> A judgment is stated but drifts, or the evidence is specific in places and general in others. The other side is mentioned but answered thinly, or the answer to it is asserted rather than argued.</p>")
    P.append("<p><strong>Score 2.</strong> The essay retells the settlements or the expansion story without a judgment that the evidence is made to serve, or the judgment is stated but supported by only one accurate piece of evidence. The other side does not appear.</p>")
    P.append("<p><strong>Score 1.</strong> The response is a fragment, a single point restated, or evidence is used inaccurately in ways that change its meaning. Little of the prompt is answered.</p>")
    P.append("<p><strong>Score 0.</strong> The response is blank, off the prompt, or copies the prompt without answering it.</p>")
    counts[14] += 1
    P.append("<p>For Prompt 1, strong evidence includes the Senate balanced at eleven free and eleven slave states in 1819; the Tallmadge Amendment passing the House on sectional lines and dying in the Senate; Maine admitted free and Missouri admitted slave, with Missouri's constitutional bar on free Black citizens fudged rather than settled; the line at 36 degrees 30 minutes barring slavery from the Louisiana Purchase lands north of it; and Jefferson's letter to John Holmes calling the question a fire bell in the night and the knell of the Union. Evidence on the other side includes the line holding for a generation, the crisis ending in 1820 without disunion, and both sections accepting a map they could stop arguing over, while the cotton gin's economics kept enlarging the question the line had fenced. (Blueprint 14)</p>")
    counts[15] += 1
    P.append("<p>For Prompt 2, strong evidence includes O'Sullivan's language of a continent allotted by Providence, which writes the continent's inhabitants and Mexico's sovereignty out of the account; Texas kept outside the Union for nine years because its admission as a slave state threatened the balance, then annexed by joint resolution when a treaty could not pass; Oregon halved at the 49th parallel by treaty with Britain while Mexico was fought; Polk's claim of American blood on American soil in ground both nations claimed, answered by Lincoln's spot resolutions; the cession of some five hundred thousand square miles at Guadalupe Hidalgo for fifteen million dollars; and the Wilmot Proviso passing the House and dying in the Senate. Evidence on the other side includes the sincerity of the expansionist belief, the restraint shown in the Oregon settlement, and the treaty paying Mexico and winning ratification as a peace. Either prompt can earn full credit argued from either side of its question, provided the judgment is earned from the evidence and the other side is answered. (Blueprint 15)</p>")
    P.append("</div></body></html>")
    out = os.path.join(UNIT, "unit-test", "unit-test.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write("\n".join(P))
    print("coverage from printed tags:", dict(sorted(counts.items())))
    print("min per entry:", min(counts.values()), "entries covered:", len(counts))
    print("total items tagged:", sum(counts.values()))

if __name__ == "__main__":
    main()
