#!/usr/bin/env python3
"""Build the Reconstruction unit test (50 points) in the four part
format: matching 15, multiple choice 20, sources 10, essay 5, with
every item in Parts A to C tagged to the blueprint in the key and the
essay guidance tagged by prompt. Coverage is recomputed from the
tags this script prints. Matching descriptions are read verbatim
from the shared build spec (unit-spec.md in this folder). Sources
are quoted verbatim from the audited TPSP bank records in
reconstruction.json: the Mississippi Vagrant Law, the Fourteenth
Amendment, Section 1, and Abram Colby's testimony, with cuts marked
[...] and the edition named in each Source line from the record's
sourceNote. Every quoted segment is asserted verbatim against its
bank record at build time. Segments were chosen from within the
records so that no segment carries an em dash, which the unit's hard
rules bar from every document.
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
    ("presidential Reconstruction", 1),
    ("Black Codes", 2),
    ("Thirteenth Amendment", 3),
    ("Civil Rights Act of 1866", 4),
    ("Fourteenth Amendment", 5),
    ("Reconstruction Acts", 6),
    ("Fifteenth Amendment", 7),
    ("Hiram Rhodes Revels", 8),
    ("sharecropping", 9),
    ("freedmen's schools", 10),
    ("Ku Klux Klan", 11),
    ("Enforcement Acts", 12),
    ("Slaughter-House Cases", 13),
    ("Panic of 1873", 14),
    ("Compromise of 1877", 15),
]
# letter order for descriptions (index into MATCH shuffled by hand, so
# the descriptions run unit wide and no match can be solved from one
# lesson's list alone)
ORDER = [10, 3, 13, 0, 7, 5, 12, 1, 9, 2, 11, 4, 8, 14, 6]

# (question, options[4], correct index, blueprint entry)
# Blueprint order by design: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
# 13, 14, 15, 1, 3, 7, 10, 14.
MC = [
    ("Johnson's restoration program, run from April 1865, readmitted a seceded state once its convention had",
     ["ratified the Fourteenth Amendment and guaranteed Black male suffrage",
      "abolished slavery, repudiated its secession ordinance and its Confederate debts, with the terms of Black freedom left to the government so organized",
      "elected a governor approved by the Joint Committee on Reconstruction",
      "distributed the great planters' estates to freed families in forty acre plots"], 1, 1),
    ("The Freedmen's Bureau, created in March 1865, worked across the South by",
     ["arming freedpeople and enrolling them in the Union League",
      "collecting the crop lien debts owed to furnishing merchants",
      "feeding the hungry of both races, running hospitals and courts, supervising labor contracts, legalizing marriages, and building schools",
      "registering voters and supervising elections in the five military districts"], 2, 2),
    ("The Thirteenth Amendment was proclaimed ratified in December 1865 after",
     ["Georgia's vote completed the count of ratifying states, in a ratification run through the border states and the restored South under Johnson's pressure",
      "Congress seated the southern delegations and counted their votes a second time",
      "the Supreme Court upheld the amendment against a challenge from Kentucky",
      "Johnson withdrew his veto of the amendment in return for the Bureau bill"], 0, 3),
    ("The Civil Rights Act of 1866 became law in April 1866 when Congress",
     ["accepted Johnson's amendments and passed the bill again by a simple majority",
      "waited for Trumbull to rewrite the bill as a constitutional amendment",
      "removed the citizenship clause so that the president would sign it",
      "passed the statute over Johnson's veto, the first override of a presidential veto on a major measure"], 3, 4),
    ("Section 1 of the Fourteenth Amendment forbids any state to",
     ["tax the property of citizens who had served the Confederacy",
      "abridge citizens' privileges or immunities, deprive any person of life, liberty, or property without due process of law, or deny any person equal protection of the laws",
      "set the qualifications of voters in elections for the House of Representatives",
      "maintain a state militia without the consent of Congress"], 1, 5),
    ("The Reconstruction Acts of March 1867 required each of the ten unreconstructed states to",
     ["pay its share of the Confederate debt before its delegation was seated",
      "elect a governor from among its former Union officers",
      "write a new constitution guaranteeing Black male suffrage, ratify the Fourteenth Amendment, and win Congress's approval before readmission to representation",
      "surrender its public lands to the Freedmen's Bureau for settlement by freed families"], 2, 6),
    ("The Fifteenth Amendment, ratified in February 1870, forbids denial of the vote on account of",
     ["race, color, or previous condition of servitude",
      "failure to pay a poll tax or pass a literacy test",
      "sex, age under twenty one, or residence under one year",
      "service in the Confederate army or office held under it"], 0, 7),
    ("Hiram Rhodes Revels entered the United States Senate in 1870 as",
     ["a former Confederate officer restored to office by the Amnesty Act",
      "the first Black governor of an American state",
      "the senator chosen to complete the term of Jefferson Davis's successor in Mississippi's other seat",
      "the first Black member of Congress, a Mississippi minister freeborn in North Carolina who had recruited Black regiments and served as a Union army chaplain"], 3, 8),
    ("Under the crop lien system that financed sharecropping, a furnishing merchant",
     ["bought the family's plot outright at the year's settlement",
      "advanced seed, tools, food, and clothing against a legal claim on the crop before it was planted, at prices and interest the merchant set",
      "paid the family wages monthly and took the whole crop as rent",
      "held the family's savings in an account insured by the Freedmen's Bank"], 1, 9),
    ("The schools and churches freedpeople built shared one pattern, in that both",
     ["were staffed entirely by teachers and ministers sent from the North",
      "were financed by the sale of confiscated planter estates",
      "were founded and sustained by freedpeople themselves, the schools filled by some quarter of a million students by 1870 and the meetinghouses serving as schoolhouses and league halls and as the first property Black communities owned outright",
      "were closed by the Redemption governments in the spring of 1877"], 2, 10),
    ("The Ku Klux Klan's night riding was aimed chiefly at",
     ["Black voters, Republican organizers, teachers, and officeholders, timed to elections, school terms, and contract settlements so that one attack instructed a whole community",
      "federal marshals and the troops guarding the statehouses at Columbia and New Orleans",
      "northern merchants who held crop liens against southern landowners",
      "the furnishing stores and railroad depots of the cotton towns"], 0, 11),
    ("Grant's use of the Enforcement Acts in South Carolina in 1871 ran on the authority to",
     ["remove state officials confirmed by the state senate without its consent",
      "close the freedmen's schools in counties where the Klan was active",
      "tax the great estates and distribute the proceeds to freed families",
      "suspend habeas corpus against insurrectionary combinations, under which federal marshals and troops made hundreds of arrests and the first Klan was broken by 1872"], 3, 12),
    ("In the Slaughter-House Cases of April 1873, the Supreme Court held that the Fourteenth Amendment",
     ["gave Congress power to protect every civil right against state action",
      "protected only the narrow rights of national citizenship and left the great body of civil rights under state authority",
      "had been ratified without the votes of the southern states and bound no one",
      "applied to private conspiracies such as the Klan as fully as to state laws"], 1, 13),
    ("Louisiana's White League, formed in 1874, differed from the first Klan in that it",
     ["operated only through the courts and the Democratic press",
      "pledged itself to protect Black voters against the rifle clubs",
      "stated white supremacy as an open platform, murdered Republican officeholders at Coushatta, and fought federal troops at Liberty Place in New Orleans, terror organized as politics by daylight",
      "was dissolved by Nathan Bedford Forrest before it could act"], 2, 14),
    ("The Electoral Commission of January 1877 settled the disputed election of 1876 by",
     ["awarding every disputed electoral vote to Hayes by votes of eight to seven, giving him the presidency by a single electoral vote, 185 to 184",
      "ordering new elections in Florida, Louisiana, South Carolina, and Oregon",
      "counting Tilden's popular vote majority as the deciding vote under the Twelfth Amendment",
      "dividing the disputed votes evenly and throwing the election to the House"], 0, 15),
    ("Johnson's Amnesty Proclamation of May 29, 1865, pardoned most former Confederates who swore a loyalty oath, while",
     ["restoring their enslaved people to them along with their other property",
      "requiring each pardoned man to give forty acres to a freed family",
      "excepting fourteen classes, including high officers and the wealthy, who had to apply to the president personally for pardon",
      "barring every pardoned man from office for fourteen years"], 2, 1),
    ("The Thirteenth Amendment's second section is central to the unit's argument because it",
     ["set the date of emancipation at January 1, 1866",
      "gave Congress power to enforce the abolition of slavery by appropriate legislation, the ground Congress stood on for the Civil Rights Act",
      "promised each freed family a plot of land and the loan of an army mule",
      "barred the former Confederate states from representation until 1870"], 1, 3),
    ("The Fifteenth Amendment's text left open a road to disfranchisement because it did not forbid",
     ["Congress to set the qualifications of voters in federal elections",
      "the states to require Black voters to register with the Union League",
      "a state to count only the votes cast in its capital county",
      "qualifications written without naming race, such as a literacy test or a poll tax, through which the vote could later be narrowed"], 3, 7),
    ("The African Methodist Episcopal Church served the new politics as well as worship because",
     ["its meetinghouses served as schoolhouses and league halls, its ministers doubled as organizers, and its property was often the first a Black community owned outright",
      "its bishops were elected to the state senates of six southern states",
      "it held the deposits of the Freedmen's Savings Bank in its own vaults",
      "it printed the ballots used in the elections of 1868"], 0, 10),
    ("The Civil Rights Act of 1875, the last of the Reconstruction civil rights laws, guaranteed",
     ["each freed family title to the plot it had farmed for two years",
      "Black men the vote in every state election regardless of state law",
      "all citizens equal enjoyment of inns, public conveyances, and theaters, and barred racial exclusion from juries, a guarantee left largely unenforced in its own decade",
      "federal marshals at every polling place in the former Confederate states"], 2, 14),
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
        if chr(8212) in segment or chr(8211) in segment:
            raise SystemExit("segment carries a dash the unit bars: "
                             + record["id"] + ": " + segment[:60])
    passage = " [...] ".join(norm)
    if not full.startswith(norm[0]):
        passage = "[...] " + passage
    body = full[:-len("[...]")].rstrip() if full.endswith("[...]") else full
    if full.endswith("[...]") or not body.endswith(norm[-1]):
        passage += " [...]"
    return passage


VAGRANT_SEGMENTS = [
    "That all rogues and vagabonds, idle and dissipated persons, beggars, jugglers, or persons practicing unlawful games or plays, runaways, common drunkards, common night-walkers, pilferers, lewd, wanton, or lascivious persons, in speech or behavior, common railers and brawlers, persons who neglect their calling or employment, misspend what they earn, or do not provide for the support of themselves or their families, or dependants, and all other idle and disorderly persons, including all who neglect all lawful business, or habitually misspend their time by frequenting houses of ill-fame, gaming-houses or tippling shops, shall be deemed and considered vagrants under the provisions of this act",
    "That all freedmen, free negroes and mulattoes in this State, over the age of eighteen years, found on the second Monday in January, 1866, or thereafter, with no lawful employment or business, or found unlawfully assembling themselves together either in the day or night time, and all white persons so assembling with freedmen, free negroes or mulattoes, or usually associating with freedmen, free negroes or mulattoes on terms of equality, or living in adultery or fornication with a freedwoman, free negro, or mulatto, shall be deemed vagrants, and on conviction thereof, shall be fined in the sum of not exceeding, in the case of a freedman, free negro or mulatto, fifty dollars, and a white man two hundred dollars, and imprisoned at the discretion of the court, the free negro not exceeding ten days, and the white man not exceeding six months.",
]

FOURTEENTH_SEGMENTS = [
    "Section 1. All persons born or naturalized in the United States, and subject to the jurisdiction thereof, are citizens of the United States and of the State wherein they reside. No State shall make or enforce any law which shall abridge the privileges or immunities of citizens of the United States; nor shall any State deprive any person of life, liberty, or property, without due process of law; nor deny to any person within its jurisdiction the equal protection of the laws.",
]

COLBY_SEGMENTS = [
    "On the 29th of October 1869, [the Klansmen] broke my door open, took me out of bed, took me to the woods and whipped me three hours or more and left me for dead.",
    "They said to me, \"Do you think you will ever vote another damned Radical ticket?\" I said, \"If there was an election tomorrow, I would vote the Radical ticket.\"",
    "Question: What is the character of those men who were engaged in whipping you? Colby: Some are first-class men in our town. One is a lawyer, one a doctor, and some are farmers.",
    "They said I had voted for Grant and had carried the Negroes against them.",
    "About two days before they whipped me they offered me $5,000 to go with them and said they would pay me $2,500 in cash if I would let another man go to the legislature in my place.",
    "I told them that I would not do it if they would give me all the county was worth.",
    "No man can make a free speech in my county. I do not believe it can be done anywhere in Georgia.",
]


def main():
    spec_text = open(SPEC).read()
    MATCH = [(term, bp, spec_definition(spec_text, term))
             for term, bp in MATCH_TERMS]

    vagrant = bank_record("reconstruction.json", "mississippi-black-code-1865")
    fourteenth = bank_record("reconstruction.json", "fourteenth-amendment-section-1-1868")
    colby = bank_record("reconstruction.json", "abram-colby-kkk-testimony-1872")
    vagrant_text = quoted_passage(vagrant, VAGRANT_SEGMENTS)
    fourteenth_text = quoted_passage(fourteenth, FOURTEENTH_SEGMENTS)
    colby_text = quoted_passage(colby, COLBY_SEGMENTS)
    vagrant_note = vagrant["sourceNote"].replace('"', "'")
    fourteenth_note = fourteenth["sourceNote"].replace('"', "'")
    colby_note = colby["sourceNote"].replace('"', "'")

    P = []
    P.append("<!DOCTYPE html>")
    P.append('<html lang="en"><head><meta charset="utf-8">')
    P.append("<title>Unit Test: Reconstruction</title>")
    P.append(f"<style>{CSS}</style></head><body>")
    P.append('<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>')
    P.append('<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>')
    P.append("<h1>Unit Test: Reconstruction</h1>")
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
    P.append(f"<p>The Mississippi Legislature, the Vagrant Law, from the Mississippi Black Code, 1865. From {vagrant_note} Cuts are marked with ellipses in brackets.</p>")
    P.append(f"<p>&ldquo;{vagrant_text}&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>A1. (1 point)</strong> Under the second section quoted, a freedman over the age of eighteen years found on or after the second Monday in January, 1866, with what condition is deemed a vagrant?</p><div class="sp-a"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>A2. (2 points)</strong> State the fine and the imprisonment the second section sets for a freedman, and state the fine and the imprisonment it sets for a white man convicted under the same section.</p><div class="sp-b"></div></div>')
    P.append('<div class="source"><p class="srclabel">Source B</p>')
    P.append(f"<p>The Fourteenth Amendment, Section 1, proposed by Congress in 1866 and ratified in 1868. From {fourteenth_note} Cuts are marked with ellipses in brackets.</p>")
    P.append(f"<p>&ldquo;{fourteenth_text}&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>B1. (2 points)</strong> State who the section declares to be citizens of the United States, and state of what else it declares them citizens.</p><div class="sp-b"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>B2. (2 points)</strong> State the three things the section forbids any state to do in its second sentence.</p><div class="sp-b"></div></div>')
    P.append('<div class="source"><p class="srclabel">Source C</p>')
    P.append(f"<p>Abram Colby, testimony to the Joint Select Committee on the Late Insurrectionary States, 1872. From {colby_note} Cuts are marked with ellipses in brackets.</p>")
    P.append(f"<p>&ldquo;{colby_text}&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>C1. (1 point)</strong> Colby testifies that the men who whipped him said he had done two things in the election. Name one of them.</p><div class="sp-a"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>C2. (2 points)</strong> State the offer the men made Colby about two days before the whipping, in its amounts and its condition, and state the answer Colby testifies he gave them.</p><div class="sp-b"></div></div>')

    P.append('<div class="essay"><h2>Part D: Essay (5 points)</h2>')
    P.append("<p>Choose <strong>one</strong> prompt and write a complete essay in the space below. Use specific evidence from the unit, and state the strongest point on the other side before you answer it.</p>")
    P.append('<p class="q"><strong>Prompt 1.</strong> Judge whether Reconstruction gave freed people real freedom. Build your answer on the terms freedpeople stated for themselves in the conventions, in Jourdon Anderson\'s letter, and in the Edisto Island petition, on the land settlement and the labor system that followed it, and on the institutions freedpeople built in the schools and the churches.</p>')
    P.append('<p class="q"><strong>Prompt 2.</strong> Judge whether 1877 ended Reconstruction or only ended its federal enforcement. Build your answer on the Compromise of 1877 and the April troop withdrawals, on the three amendments standing in the Constitution as ratified, and on the retreat that ran from amnesty and the Slaughter-House Cases through the Panic of 1873 and the White League.</p>')
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
        ("A1", 2, "A freedman over eighteen found on the second Monday in January, 1866, or thereafter, with no lawful employment or business is deemed a vagrant. Unlawful assembling, in the day time or the night time, is also accepted for the point, as the section names it in the same sentence."),
        ("A2", 2, "For a freedman, free negro or mulatto, the fine is not exceeding fifty dollars and imprisonment at the discretion of the court, the free negro not exceeding ten days. For a white man the fine is not exceeding two hundred dollars and imprisonment not exceeding six months. One point for the freedman's penalty stated and one point for the white man's penalty stated."),
        ("B1", 5, "All persons born or naturalized in the United States, and subject to the jurisdiction thereof, are citizens of the United States. They are also citizens of the State wherein they reside. One point for birth or naturalization under the jurisdiction stated and one point for citizenship of the state of residence stated."),
        ("B2", 5, "No State shall make or enforce any law which shall abridge the privileges or immunities of citizens of the United States. No State shall deprive any person of life, liberty, or property, without due process of law. No State shall deny to any person within its jurisdiction the equal protection of the laws. Two of the three prohibitions stated accurately earn one point, and all three earn both points."),
        ("C1", 11, "The men said Colby had voted for Grant, and that he had carried the Negroes against them. Either charge named earns the point."),
        ("C2", 11, "About two days before the whipping the men offered Colby $5,000 to go with them, and said they would pay him $2,500 in cash, if he would let another man go to the legislature in his place. Colby told them he would not do it if they would give him all the county was worth. One point for the offer stated with its amounts and condition and one point for Colby's refusal stated."),
    ]
    for label, bp, ans in key3:
        counts[bp] += 1
        P.append(f"<p><strong>{label}.</strong> {ans} (Blueprint {bp})</p>")
    P.append("<h3>Part D: Essay</h3>")
    P.append("<p>The essay is scored on the six part holistic scale below, whichever prompt the student chose.</p>")
    P.append("<p><strong>Score 5.</strong> A clear judgment is stated and held through the essay. At least three pieces of specific evidence from the unit are used accurately, the strongest point on the other side is stated fairly and answered, and the writing is organized in paragraphs with a conclusion that follows from the evidence.</p>")
    P.append("<p><strong>Score 4.</strong> A clear judgment is stated and mostly held. Two or three pieces of specific evidence are used accurately, the other side is stated and answered, and the organization holds, with minor lapses in precision or development.</p>")
    P.append("<p><strong>Score 3.</strong> A judgment is stated but drifts, or the evidence is specific in places and general in others. The other side is mentioned but answered thinly, or the answer to it is asserted rather than argued.</p>")
    P.append("<p><strong>Score 2.</strong> The essay retells the Reconstruction story without a judgment that the evidence is made to serve, or the judgment is stated but supported by only one accurate piece of evidence. The other side does not appear.</p>")
    P.append("<p><strong>Score 1.</strong> The response is a fragment, a single point restated, or evidence is used inaccurately in ways that change its meaning. Little of the prompt is answered.</p>")
    P.append("<p><strong>Score 0.</strong> The response is blank, off the prompt, or copies the prompt without answering it.</p>")
    counts[9] += 1
    P.append("<p>For Prompt 1, strong evidence includes the freedmen's conventions demanding land, fair wages, family protection, schools, and the ballot; Jourdon Anderson pricing thirty two years of his own labor and twenty of his wife's and asking after his daughters' safety and his children's schooling; the Edisto Island petitioners asking to keep and buy the land they had settled and worked; the land settlement's refusal, Field Orders No. 15 reversed and Stevens's confiscation plan rejected; sharecropping and the crop lien renewing a family's debt at every settlement; the vote exercised and office held, Revels, Bruce, and Pinchback at the top of a legislature full of Black members; and the schools and churches freedpeople built and sustained themselves. Evidence on the other side includes the legal frame itself, slavery abolished by amendment, citizenship and equal protection written into the Constitution, the vote protected in the text, and a generation that learned to read in the freedmen's schools. A strong essay weighs freedom as freedpeople themselves defined it, in land, wages, family, school, and ballot, against the freedom the law delivered and the ground it never reached. (Blueprint 9)</p>")
    counts[15] += 1
    P.append("<p>For Prompt 2, strong evidence includes the Compromise of 1877 and the April orders withdrawing the last troops from the statehouses at Columbia and New Orleans, after which the Republican governments of South Carolina and Louisiana fell and Redemption governed; the retreat that prepared the ending, the Amnesty Act of 1872, the Slaughter-House narrowing of the Fourteenth Amendment in 1873, the Panic of 1873 and the northern attention it drew home, the White League's open terror of 1874, and the Civil Rights Act of 1875 left largely unenforced; and the case that enforcement was the era's working half, since the Enforcement Acts had broken the first Klan when they were used. Evidence on the other side includes the texts that survived the withdrawal: the Thirteenth, Fourteenth, and Fifteenth Amendments stood in the Constitution unamended, defining citizenship, abolishing slavery, and protecting the vote in law, and the schools, churches, and political experience of the era stood with them. Either prompt can earn full credit argued from either side of its question, provided the judgment is earned from the evidence and the other side is answered. (Blueprint 15)</p>")
    P.append("</div></body></html>")
    out = os.path.join(UNIT, "unit-test", "unit-test.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write("\n".join(P))
    print("coverage from printed tags:", dict(sorted(counts.items())))
    print("min per entry:", min(counts.values()), "entries covered:", len(counts))
    print("total items tagged:", sum(counts.values()))

if __name__ == "__main__":
    main()
