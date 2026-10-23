#!/usr/bin/env python3
"""Build the Sectional Crisis and Civil War unit test (50 points) in
the four part format: matching 15, multiple choice 20, sources 10,
essay 5, with every item in Parts A to C tagged to the blueprint in
the key and the essay guidance tagged by prompt. Coverage is
recomputed from the tags this script prints. Matching descriptions
are read verbatim from the shared build spec (unit-spec.md in this
folder). Sources are quoted verbatim from the audited TPSP bank
records in sectional-civil-war.json, the Kansas-Nebraska Act, South
Carolina's Declaration of the Immediate Causes of Secession, and the
Emancipation Proclamation, with cuts marked [...] and the edition
named in each Source line from the record's sourceNote. Every quoted
segment is asserted verbatim against its bank record at build time.
Segments were chosen from within the records so that no segment
carries an em dash, which the unit's hard rules bar from every
document.
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
    ("Compromise of 1850", 1),
    ("Fugitive Slave Act", 2),
    ("Uncle Tom's Cabin", 3),
    ("Anthony Burns", 4),
    ("Kansas-Nebraska Act", 5),
    ("Bleeding Kansas", 6),
    ("Republican Party", 7),
    ("Dred Scott v. Sandford", 8),
    ("Freeport Doctrine", 9),
    ("secession", 10),
    ("Anaconda Plan", 11),
    ("Antietam", 12),
    ("Emancipation Proclamation", 13),
    ("Gettysburg", 14),
    ("Second Inaugural Address", 15),
]
# letter order for descriptions (index into MATCH shuffled by hand, so
# the descriptions run unit wide and no match can be solved from one
# lesson's list alone)
ORDER = [10, 3, 13, 0, 7, 5, 12, 1, 9, 2, 11, 4, 8, 14, 6]

# (question, options[4], correct index, blueprint entry)
# Blueprint order by design: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
# 13, 14, 15, 1, 5, 8, 11, 14.
MC = [
    ("The Compromise of 1850 reached passage in September 1850 after",
     ["Clay's single omnibus bill passed the Senate as one measure",
      "Douglas took the measures up one at a time and passed each with a different majority",
      "California withdrew its application and applied again as two states",
      "the Supreme Court ordered Congress to settle the Texas boundary"], 1, 1),
    ("Under the Fugitive Slave Act of September 18, 1850, a person accused of escaping slavery was",
     ["tried by a jury in the federal district court where the seizure occurred",
      "heard by a state judge, with counsel paid by the state",
      "heard by a federal commissioner, denied a jury trial and the right to testify, with the commissioner paid ten dollars for remanding and five for freeing",
      "freed automatically unless the owner appeared in person to claim the prisoner"], 2, 2),
    ("Uncle Tom's Cabin, published as a book in March 1852, built its case against slavery chiefly from",
     ["the slave narratives, and Josiah Henson's account in particular",
      "the reports of federal commissioners under the Fugitive Slave Act",
      "Clay's and Webster's speeches in the Compromise debates",
      "British parliamentary papers on the West India emancipation"], 0, 3),
    ("The two surviving texts of Sojourner Truth's speech at Akron in 1851 differ chiefly because",
     ["Truth wrote one text herself and dictated the other to a secretary",
      "Robinson printed his report in a southern newspaper and Gage in a northern one",
      "Gage's text was printed weeks after the speech and Robinson's twelve years later",
      "Robinson reported the speech in the Anti-Slavery Bugle in June 1851, while Gage's version, published twelve years later, gave it its famous refrain and its dialect"], 3, 4),
    ("The Kansas-Nebraska Act of May 30, 1854, dealt with the Missouri Compromise line of 1820 by",
     ["extending the line westward to the Pacific Ocean",
      "declaring the eighth section of the Missouri act inoperative and void and leaving slavery in the territories to popular sovereignty",
      "moving the line north to the border of Canada",
      "submitting the line to the Supreme Court for a ruling"], 1, 5),
    ("The territorial election of March 1855 in Kansas was carried by",
     ["federal troops sent to the territory by President Pierce",
      "free state settlers sent west by the New England aid societies",
      "Missourians who crossed the border in organized bands, voted, and rode home, the border ruffians of free state naming",
      "delegates chosen by the convention that met at Lecompton"], 2, 6),
    ("The Republican Party of 1854 joined ex-Whigs, Free Soilers, and anti-Nebraska Democrats on the single plank that",
     ["Congress must bar slavery from the federal territories",
      "slavery must end at once in every state where it stood",
      "each territory should decide the slavery question by popular sovereignty",
      "the Fugitive Slave Act must be repealed before the next census"], 0, 7),
    ("In Dred Scott v. Sandford in 1857, Chief Justice Taney held that",
     ["Scott had been freed by his residence at Fort Snelling",
      "Congress could bar slavery from the territories but had chosen not to",
      "Black people could be citizens of a state but never of the United States",
      "Black people could not be citizens of the United States, Scott's residence on free soil had not freed him, and Congress had never had power to bar slavery from the territories"], 3, 8),
    ("At Freeport in August 1858, Douglas answered Lincoln by holding that a territory could keep slavery out despite the Dred Scott decision by",
     ["nullifying the decision in its first legislative session",
      "refusing to pass the local police laws slavery needed to survive",
      "petitioning Congress to admit it as a free state at once",
      "driving slaveholders from the territory by a special tax"], 1, 9),
    ("Lincoln won the presidency in 1860 with",
     ["a majority of the popular vote and every free state but one",
      "the electoral votes of four southern states added to the North",
      "39.8 percent of the popular vote, a majority of the electoral college, and not one electoral vote from the South",
      "a contingent election in the House of Representatives"], 2, 10),
    ("General Winfield Scott's Anaconda Plan of 1861 proposed to defeat the Confederacy by",
     ["a naval blockade of its coast and a drive down the Mississippi that would split it in two",
      "an immediate march on Richmond before the Confederacy could arm",
      "arming the enslaved people of the South in the war's first month",
      "holding New Orleans and abandoning the Mississippi above it"], 0, 11),
    ("Antietam, fought on September 17, 1862, is carried in the unit as",
     ["the war's first great battle, fought before excursion crowds",
      "a Confederate victory that opened Maryland to recruitment",
      "the surrender of the Army of Northern Virginia to McClellan",
      "the single bloodiest day in American history, a tactical standstill that ended Lee's first invasion of the North and gave Lincoln ground to issue the Emancipation Proclamation"], 3, 12),
    ("The Emancipation Proclamation of January 1, 1863, declared free",
     ["every enslaved person in the United States, the loyal border states included",
      "the enslaved people in the states and parts of states then in rebellion, leaving slavery untouched in the loyal border states and opening the army and navy to Black enlistment",
      "only the enslaved people who had already reached the Union lines",
      "the enslaved people of the federal territories and the District of Columbia"], 1, 13),
    ("The first days of July 1863 joined two results, when",
     ["Chancellorsville and Fredericksburg fell in the same week",
      "Atlanta was taken and Mobile Bay was closed",
      "Meade stopped Lee at Gettysburg on July 1 to 3 and Vicksburg surrendered to Grant on July 4, giving the Union the whole Mississippi",
      "Shiloh was fought and New Orleans was taken"], 2, 14),
    ("Sherman's March to the Sea of November and December 1864 carried total war by",
     ["marching some sixty two thousand men from Atlanta to Savannah living off the country and destroying the railroads, mills, and stores in a corridor sixty miles wide",
      "besieging Petersburg until its railroads were cut",
      "burning the Confederate capital on the night of the evacuation",
      "marching north to Appomattox to receive Lee's surrender"], 0, 15),
    ("Henry Clay's part in the Compromise of 1850 was to",
     ["write the Fugitive Slave Act and carry it through the House alone",
      "persuade President Taylor to admit California and New Mexico at once",
      "frame the settlement in his resolutions of January 1850, the last settlement of the career that had built the compromises of 1820 and 1833, though the omnibus failed and Douglas passed the measures separately",
      "preside over the Senate as vice president during the debates"], 2, 1),
    ("Popular sovereignty, as Douglas offered the doctrine, held that",
     ["Congress should decide the slavery question for each territory",
      "the people of a territory should decide for themselves whether to permit slavery there",
      "the Supreme Court should decide the question for the territories",
      "each state legislature should decide the question for its neighboring territories"], 1, 5),
    ("The House Divided speech of June 16, 1858, argued that",
     ["the Union would be dissolved within the year by secession",
      "Douglas and Lincoln had reached agreement on the territories",
      "slavery would end by purchase and colonization before 1860",
      "the government could not endure permanently half slave and half free, and the Nebraska repeal and the Dred Scott decision were parts of one design to make slavery national"], 3, 8),
    ("First Bull Run, fought near Manassas on July 21, 1861, taught both governments that",
     ["the war would not be short and real armies had to be built, in a Confederate victory and Union rout watched by excursion crowds from Washington",
      "the blockade had already decided the war at sea",
      "European recognition of the Confederacy was now certain",
      "McClellan would be sent west to command on the Mississippi"], 0, 11),
    ("In the Gettysburg Address of November 19, 1863, Lincoln restated the war as",
     ["a contest over the tariff and the national banking system",
      "a punishment the North alone had earned by its sins",
      "a test of the proposition that all men are created equal, rededicating the living to the unfinished work of the dead",
      "the opening campaign of his reelection the following year"], 2, 14),
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


KANSAS_SEGMENTS = [
    "That the Constitution, and all Laws of the United States which are not locally inapplicable, shall have the same force and effect within the said Territory of Nebraska as elsewhere within the United States, except the eighth section of the act preparatory to the admission of Missouri into the Union approved March sixth, eighteen hundred and twenty, which, being inconsistent with the principle of non-intervention by Congress with slaves in the States and Territories, as recognized by the legislation of eighteen hundred and fifty, commonly called the Compromise Measures, is hereby declared inoperative and void;",
    "it being the true intent and meaning of this act not to legislate slavery into any Territory or State, nor to exclude it therefrom, but to leave the people thereof perfectly free to form and regulate their domestic institutions in their own way, subject only to the Constitution of the United States",
]

SECESSION_SEGMENTS = [
    "We assert that fourteen of the States have deliberately refused, for years past, to fulfill their constitutional obligations, and we refer to their own Statutes for the proof.",
    "An increasing hostility on the part of the non-slaveholding States to the institution of slavery, has led to a disregard of their obligations, and the laws of the General Government have ceased to effect the objects of the Constitution.",
    "Thus the constituted compact has been deliberately broken and disregarded by the non-slaveholding States, and the consequence follows that South Carolina is released from her obligation.",
    "They have encouraged and assisted thousands of our slaves to leave their homes; and those who remain, have been incited by emissaries, books and pictures to servile insurrection.",
    "A geographical line has been drawn across the Union, and all the States north of that line have united in the election of a man to the high office of President of the United States, whose opinions and purposes are hostile to slavery.",
    "It has announced that the South shall be excluded from the common territory, that the judicial tribunals shall be made sectional, and that a war must be waged against slavery until it shall cease throughout the United States.",
]

EMANCIPATION_SEGMENTS = [
    "That on the first day of January, in the year of our Lord one thousand eight hundred and sixty-three, all persons held as slaves within any State or designated part of a State, the people whereof shall then be in rebellion against the United States, shall be then, thenceforward, and forever free;",
    "the Executive Government of the United States, including the military and naval authority thereof, will recognize and maintain the freedom of such persons, and will do no act or acts to repress such persons, or any of them, in any efforts they may make for their actual freedom.",
    "And I further declare and make known, that such persons of suitable condition, will be received into the armed service of the United States to garrison forts, positions, stations, and other places, and to man vessels of all sorts in said service.",
    "And upon this act, sincerely believed to be an act of justice, warranted by the Constitution, upon military necessity, I invoke the considerate judgment of mankind, and the gracious favor of Almighty God.",
]


def main():
    spec_text = open(SPEC).read()
    MATCH = [(term, bp, spec_definition(spec_text, term))
             for term, bp in MATCH_TERMS]

    kansas = bank_record("sectional-civil-war.json", "kansas-nebraska-act-1854")
    secession = bank_record("sectional-civil-war.json", "south-carolina-secession-declaration-1860")
    emancipation = bank_record("sectional-civil-war.json", "emancipation-proclamation-1863")
    kansas_text = quoted_passage(kansas, KANSAS_SEGMENTS)
    secession_text = quoted_passage(secession, SECESSION_SEGMENTS)
    emancipation_text = quoted_passage(emancipation, EMANCIPATION_SEGMENTS)
    kansas_note = kansas["sourceNote"].replace('"', "'")
    secession_note = secession["sourceNote"].replace('"', "'")
    emancipation_note = emancipation["sourceNote"].replace('"', "'")

    P = []
    P.append("<!DOCTYPE html>")
    P.append('<html lang="en"><head><meta charset="utf-8">')
    P.append("<title>Unit Test: Sectional Crisis and Civil War</title>")
    P.append(f"<style>{CSS}</style></head><body>")
    P.append('<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>')
    P.append('<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>')
    P.append("<h1>Unit Test: Sectional Crisis and Civil War</h1>")
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
    P.append(f"<p>The Congress of the United States, Section 14 of the Kansas-Nebraska Act, May 30, 1854. From {kansas_note} Cuts are marked with ellipses in brackets.</p>")
    P.append(f"<p>&ldquo;{kansas_text}&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>A1. (1 point)</strong> The act declares the eighth section of the act for the admission of Missouri inoperative and void because it is inconsistent with what principle, as the passage names the principle?</p><div class="sp-a"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>A2. (2 points)</strong> State what the act says is not its intent to do about slavery in a territory or state, and state what it leaves the people of a territory free to do instead.</p><div class="sp-b"></div></div>')
    P.append('<div class="source"><p class="srclabel">Source B</p>')
    P.append(f"<p>The South Carolina Secession Convention, the Declaration of the Immediate Causes of Secession, 1860. From {secession_note} Cuts are marked with ellipses in brackets.</p>")
    P.append(f"<p>&ldquo;{secession_text}&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>B1. (2 points)</strong> State what the declaration asserts fourteen of the states have deliberately refused to do, and state the proof the declaration points to for the charge.</p><div class="sp-b"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>B2. (2 points)</strong> State the consequence the declaration draws from the compact having been deliberately broken, and name one purpose it says the incoming sectional party has announced.</p><div class="sp-b"></div></div>')
    P.append('<div class="source"><p class="srclabel">Source C</p>')
    P.append(f"<p>President Abraham Lincoln, the Emancipation Proclamation, January 1, 1863. From {emancipation_note} Cuts are marked with ellipses in brackets.</p>")
    P.append(f"<p>&ldquo;{emancipation_text}&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>C1. (1 point)</strong> The proclamation declares free the persons held as slaves in any state whose people shall then be in what condition?</p><div class="sp-a"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>C2. (2 points)</strong> State what the Executive Government will recognize and maintain for the people declared free, and state what service such persons of suitable condition will be received into.</p><div class="sp-b"></div></div>')

    P.append('<div class="essay"><h2>Part D: Essay (5 points)</h2>')
    P.append("<p>Choose <strong>one</strong> prompt and write a complete essay in the space below. Use specific evidence from the unit, and state the strongest point on the other side before you answer it.</p>")
    P.append('<p class="q"><strong>Prompt 1.</strong> Judge whether slavery was the central cause of the Civil War. Build your answer on the seceding states\' own words in South Carolina\'s Declaration of the Immediate Causes and Stephens\'s Cornerstone Speech, on the fight over slavery\'s extension from the Kansas-Nebraska repeal through the Dred Scott decision, and on the verdict of Lincoln\'s Second Inaugural Address.</p>')
    P.append('<p class="q"><strong>Prompt 2.</strong> Judge whether the war\'s settled verdict was the destruction of slavery or the preservation of the Union. Build your answer on the Emancipation Proclamation and its limits, on the contraband record and Black enlistment, on the Thirteenth Amendment, and on the Second Inaugural\'s account of what the war settled and what it left open.</p>')
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
        ("A1", 5, "The eighth section is declared inconsistent with the principle of non-intervention by Congress with slaves in the States and Territories, as recognized by the legislation of eighteen hundred and fifty, commonly called the Compromise Measures. One point for the principle named in the passage's words."),
        ("A2", 5, "The act's true intent and meaning is not to legislate slavery into any Territory or State, nor to exclude it therefrom. It leaves the people thereof perfectly free to form and regulate their domestic institutions in their own way, subject only to the Constitution of the United States. One point for neither legislating slavery in nor excluding it, and one point for the people left free to form and regulate their domestic institutions subject only to the Constitution."),
        ("B1", 10, "The declaration asserts that fourteen of the States have deliberately refused, for years past, to fulfill their constitutional obligations. It refers to their own Statutes for the proof. One point for the refusal stated and one point for the statutes named as the proof."),
        ("B2", 10, "Because the constituted compact has been deliberately broken and disregarded by the non-slaveholding States, the consequence follows that South Carolina is released from her obligation. The incoming party has announced, in the declaration's list, that the South shall be excluded from the common territory, or that the judicial tribunals shall be made sectional, or that a war must be waged against slavery until it shall cease throughout the United States. One point for the release from obligation and one point for any one announced purpose named."),
        ("C1", 13, "The state or designated part of a state must be one whose people shall then be in rebellion against the United States. One point for rebellion named."),
        ("C2", 13, "The Executive Government of the United States, including the military and naval authority thereof, will recognize and maintain the freedom of such persons, and will do no act or acts to repress them in any efforts they may make for their actual freedom. Such persons of suitable condition will be received into the armed service of the United States, to garrison forts, positions, stations, and other places, and to man vessels of all sorts in that service. One point for the freedom recognized and maintained and one point for reception into the armed service."),
    ]
    for label, bp, ans in key3:
        counts[bp] += 1
        P.append(f"<p><strong>{label}.</strong> {ans} (Blueprint {bp})</p>")
    P.append("<h3>Part D: Essay</h3>")
    P.append("<p>The essay is scored on the six part holistic scale below, whichever prompt the student chose.</p>")
    P.append("<p><strong>Score 5.</strong> A clear judgment is stated and held through the essay. At least three pieces of specific evidence from the unit are used accurately, the strongest point on the other side is stated fairly and answered, and the writing is organized in paragraphs with a conclusion that follows from the evidence.</p>")
    P.append("<p><strong>Score 4.</strong> A clear judgment is stated and mostly held. Two or three pieces of specific evidence are used accurately, the other side is stated and answered, and the organization holds, with minor lapses in precision or development.</p>")
    P.append("<p><strong>Score 3.</strong> A judgment is stated but drifts, or the evidence is specific in places and general in others. The other side is mentioned but answered thinly, or the answer to it is asserted rather than argued.</p>")
    P.append("<p><strong>Score 2.</strong> The essay retells the secession story or the war story without a judgment that the evidence is made to serve, or the judgment is stated but supported by only one accurate piece of evidence. The other side does not appear.</p>")
    P.append("<p><strong>Score 1.</strong> The response is a fragment, a single point restated, or evidence is used inaccurately in ways that change its meaning. Little of the prompt is answered.</p>")
    P.append("<p><strong>Score 0.</strong> The response is blank, off the prompt, or copies the prompt without answering it.</p>")
    counts[10] += 1
    P.append("<p>For Prompt 1, strong evidence includes South Carolina's declaration charging the northern states with refusing their constitutional obligations on fugitives, nullifying the acts of Congress by their own statutes, encouraging enslaved people to leave their homes, and electing a president hostile to slavery; Stephens's Cornerstone Speech naming the new government's foundation as the truth of racial inequality and slavery as the Black man's natural condition; the Kansas-Nebraska repeal and the violence over slavery's extension; the Dred Scott decision voiding every political settlement of the territorial question; and Lincoln's Second Inaugural naming American slavery as the offense of which the war was the woe. Evidence on the other side includes the secession documents' own language of compact and constitutional rights, the North's stated war aim of Union in 1861, and the tariff and states rights arguments the era also carried; a strong essay weighs what the seceding states said when they left against what later memory preferred to say for them. (Blueprint 10)</p>")
    counts[15] += 1
    P.append("<p>For Prompt 2, strong evidence includes the Proclamation's limits, freedom declared in the rebellious states and slavery untouched in the loyal border states; the contraband record, in which the enslaved made emancipation a fact by reaching Union lines before any proclamation; Black enlistment, some 180,000 soldiers in the United States Colored Troops and the equal pay fight won in June 1864; the Thirteenth Amendment completing abolition in law everywhere in the United States; Appomattox and the Union preserved as one government; and the Second Inaugural naming slavery, not disunion alone, as the war's offense. Evidence on the other side includes Lincoln's opening pledge to save the Union with or without freeing the enslaved, the Proclamation framed as military necessity, and the freed people's land, safety, and vote left unsettled in April 1865. Either prompt can earn full credit argued from either side of its question, provided the judgment is earned from the evidence and the other side is answered. (Blueprint 15)</p>")
    P.append("</div></body></html>")
    out = os.path.join(UNIT, "unit-test", "unit-test.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write("\n".join(P))
    print("coverage from printed tags:", dict(sorted(counts.items())))
    print("min per entry:", min(counts.values()), "entries covered:", len(counts))
    print("total items tagged:", sum(counts.values()))

if __name__ == "__main__":
    main()
