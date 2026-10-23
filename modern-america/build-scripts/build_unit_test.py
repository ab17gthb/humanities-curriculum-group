#!/usr/bin/env python3
"""Build the Modern America unit test (50 points) in the established test
format: matching 15, multiple choice 20, source-based 15, with every
item tagged to the blueprint in the key. Coverage is recomputed from
the tags this script prints. Matching definitions are read verbatim
from the shared build spec (unit-spec.md in this folder). Sources are
quoted verbatim from the audited TPSP bank records in modern.json,
with cuts marked and the edition named in each Source line.
"""
import json
import os
import re

UNIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "unit-spec.md")
BANK = os.path.expanduser(
    "~/workspace/primary-source/vite-react-main/public/data/modern.json")

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
    ("stagflation", 1),
    ("tax revolt", 2),
    ("supply-side economics", 3),
    ("PATCO strike", 4),
    ("peace dividend", 5),
    ("globalization", 6),
    ("personal computer", 7),
    ("cable news", 8),
    ("Immigration and Nationality Act of 1965", 9),
    ("Sun Belt", 10),
    ("September 11 attacks", 11),
    ("USA PATRIOT Act", 12),
    ("subprime mortgage", 13),
    ("Affordable Care Act", 14),
    ("political polarization", 15),
]
# letter order for descriptions (index into MATCH shuffled by hand)
ORDER = [4, 12, 1, 9, 6, 14, 2, 10, 0, 7, 13, 3, 11, 5, 8]

# (question, options[4], correct index, blueprint entry)
# Design: counts by entry are 1:1, 2:2, 3:1, 4:2, 5:1, 6:2, 7:1, 8:2,
# 9:1, 10:1, 11:1, 12:1, 13:1, 14:2, 15:1. With matching (one per
# entry) and the source section (two tags each on entries 1, 3, 11),
# every entry reaches at least two assessments.
MC = [
    ("Stagflation, the condition of the American economy in the 1970s, combined",
     ["rapid growth, low unemployment, and falling prices",
      "stagnant economic growth, high unemployment, and high inflation",
      "high inflation with a federal budget surplus",
      "falling oil prices and rising wages"], 1, 1),
    ("California's Proposition 13, passed in June 1978,",
     ["raised property taxes to fund new state programs",
      "ended the national origins quota system",
      "cut property taxes sharply and capped their future growth",
      "created the Moral Majority"], 2, 2),
    ("The Economic Recovery Tax Act of 1981, the center of the Reagan economic program,",
     ["cut income tax rates by about a quarter over three years and cut the top rate from seventy percent to fifty percent",
      "raised the top income tax rate to seventy percent",
      "created a national sales tax",
      "barred the Federal Reserve from raising interest rates"], 0, 3),
    ("After President Reagan fired more than eleven thousand striking air traffic controllers in August 1981, unions and employers read the PATCO decision as",
     ["a ruling that federal workers could strike at any time",
      "a signal of the terms on which labor would be treated in the era",
      "the end of the federal air traffic control system",
      "a step required by the Tower Commission"], 1, 4),
    ("The Persian Gulf War of January and February 1991 was fought when",
     ["the United States acted alone to occupy Iraq",
      "Iraq invaded Saudi Arabia and held its oil fields",
      "an American-led coalition acting with United Nations authorization drove Iraq's army out of Kuwait in six weeks",
      "the Soviet Union sent troops into Kuwait"], 2, 5),
    ("The North American Free Trade Agreement, which took effect on January 1, 1994,",
     ["ended all trade between the United States and Mexico",
      "removed most tariffs and trade barriers among the United States, Canada, and Mexico",
      "created a single currency for North America",
      "barred American factories from moving abroad"], 1, 6),
    ("The Internet reached the general public in the form taught in this unit because it",
     ["was built by a single private company in 1980",
      "grew out of government and university systems and opened to public and commercial use in the middle 1990s, with the browser making it usable by anyone",
      "began as a cable television channel",
      "replaced the personal computer in American homes"], 1, 7),
    ("Cable news changed how many Americans followed events chiefly because it",
     ["ended newspaper publication in the United States",
      "carried news around the clock from CNN's founding in 1980, replacing the nightly broadcast as the main source for many viewers",
      "was required by the Telecommunications Act of 1996",
      "broadcast only during national emergencies"], 1, 8),
    ("The Immigration and Nationality Act of 1965 built the new immigration system chiefly on",
     ["quotas assigned by national origin",
      "a lottery open to every country equally",
      "family reunification and needed skills, ending the national origins quota system in place since the 1920s",
      "employment in the defense industry"], 2, 9),
    ("The Sun Belt rose in population, jobs, and political weight from the 1970s onward chiefly on",
     ["heavy industry returning to the Northeast",
      "air conditioning, defense and technology work, and lower costs",
      "the growth of passenger rail in the South",
      "federal orders moving families to the Southwest"], 1, 10),
    ("The Authorization for Use of Military Force, passed on September 18, 2001, authorized the president to",
     ["declare war on every state named in the PATRIOT Act",
      "use all necessary and appropriate force against those responsible for the September 11 attacks and those who harbored them",
      "create the Department of Homeland Security",
      "set the date for the invasion of Iraq in 2003"], 1, 11),
    ("The Department of Homeland Security, created in 2002, was formed by",
     ["closing the Federal Bureau of Investigation",
      "moving airport security to private companies",
      "merging twenty two federal agencies and offices charged with protecting the country against terrorist attack and disaster",
      "placing the armed forces under a civilian police chief"], 2, 12),
    ("The financial collapse of 2008 followed the sequence in which",
     ["house prices rose without interruption and banks refused all new loans",
      "house prices fell from 2006, securities built on mortgages soured, Lehman Brothers failed on September 15, 2008, and credit markets froze",
      "the Federal Reserve raised interest rates above nineteen percent",
      "the federal government ended deposit insurance"], 1, 13),
    ("The American Recovery and Reinvestment Act of February 2009, the stimulus, worked through",
     ["about eight hundred billion dollars of government spending and tax cuts meant to restart a stalled economy",
      "a cut in income tax rates to a flat ten percent",
      "the sale of the automobile industry to foreign buyers",
      "new tariffs on imported goods"], 0, 14),
    ("Bush v. Gore, decided by five votes to four in December 2000,",
     ["ordered a nationwide recount of the presidential vote",
      "stopped the recount of Florida's presidential ballots and settled the election of 2000 for George W. Bush",
      "held that the Second Amendment protects a handgun in the home",
      "required every state to license marriages between two people of the same sex"], 1, 15),
    ("The Moral Majority, founded by the Reverend Jerry Falwell in 1979, was organized to",
     ["register voters only in California",
      "defend the federal tax code of the 1970s",
      "mobilize evangelical Christian voters behind conservative candidates and causes",
      "lead the campaign for the Equal Rights Amendment"], 2, 2),
    ("One limit on the Reagan revolution, stated in the record of the 1980s, is that",
     ["the 1981 tax cut was repealed in full the next year",
      "the entitlement core of Social Security and Medicare was left in place while the national debt grew from about nine hundred billion dollars in 1981 toward three trillion dollars by 1989",
      "deregulation was ended in banking and transport",
      "no conservative judges were appointed to the federal courts"], 1, 4),
    ("As factory employment shrank in the decades after the 1970s, the American economy took the form of a service economy, in which most jobs",
     ["produced steel, cars, and other goods for export",
      "were in farming and mining",
      "were held by the federal government",
      "produced services such as health care, retail, finance, and food rather than goods"], 3, 6),
    ("The digital divide, as the federal surveys of the era measured it, was the gap in access to computers and the Internet that followed lines of",
     ["party registration alone",
      "income, education, age, and place",
      "language spoken at home alone",
      "height and occupation"], 1, 8),
    ("The Tea Party movement and Occupy Wall Street answered the aftermath of the financial crisis from opposite directions, in that the Tea Party rose in 2009 against the bailouts, the stimulus, and the health care law demanding smaller government, while Occupy, beginning in 2011,",
     ["demanded lower taxes and limits on spending",
      "supported the bank rescue of 2008",
      "camped in financial districts to protest economic inequality in the name of the ninety nine percent against the one percent",
      "called for the stimulus to be doubled"], 2, 14),
]

# Source passages: each segment must occur verbatim in the bank record;
# the builder checks that and joins segments with a marked cut.
CARTER_SEGMENTS = [
    "The threat is nearly invisible in ordinary ways. It is a crisis of confidence. It is a crisis that strikes at the very heart and soul and spirit of our national will. We can see this crisis in the growing doubt about the meaning of our own lives and in the loss of a unity of purpose for our Nation.",
    "In a nation that was proud of hard work, strong families, close-knit communities, and our faith in God, too many of us now tend to worship self-indulgence and consumption. Human identity is no longer defined by what one does, but by what one owns. But we've discovered that owning things and consuming things does not satisfy our longing for meaning.",
    "For the first time in the history of our country a majority of our people believe that the next 5 years will be worse than the past 5 years. Two-thirds of our people do not even vote.",
    "So, the solution of our energy crisis can also help us to conquer the crisis of the spirit in our country. It can rekindle our sense of unity, our confidence in the future, and give our Nation and all of us individually a new sense of purpose.",
]
REAGAN_SEGMENTS = [
    "We suffer from the longest and one of the worst sustained inflations in our national history. It distorts our economic decisions, penalizes thrift, and crushes the struggling young and the fixed-income elderly alike. It threatens to shatter the lives of millions of our people.",
    "Idle industries have cast workers into unemployment, human misery, and personal indignity. Those who do work are denied a fair return for their labor by a tax system which penalizes successful achievement and keeps us from maintaining full productivity.",
    "But great as our tax burden is, it has not kept pace with public spending. For decades we have piled deficit upon deficit, mortgaging our future and our children's future for the temporary convenience of the present.",
    "In this present crisis, government is not the solution to our problem; government is the problem.",
]
COMMISSION_SEGMENTS = [
    "We present the narrative of this report and the recommendations that flow from it to the President of the United States, the United States Congress, and the American people for their consideration. Ten Commissioners, five Republicans and five Democrats chosen by elected leaders from our nation's capital at a time of great partisan division, have come together to present this report without dissent.",
    "September 11, 2001, was a day of unprecedented shock and suffering in the history of the United States. The nation was unprepared.",
    "What we can say with confidence is that none of the measures adopted by the U.S. government from 1998 to 2001 disturbed or even delayed the progress of the al Qaeda plot. Across the government, there were failures of imagination, policy, capabilities, and management.",
    "The most important failure was one of imagination. We do not believe leaders understood the gravity of the threat. The terrorist danger from Bin Ladin and al Qaeda was not a major topic for policy debate among the public, the media, or in the Congress.",
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

    carter = bank_record("carter-crisis-of-confidence-1979")
    reagan = bank_record("reagan-first-inaugural-1981")
    commission = bank_record("911-commission-report-exec-summary-2004")
    carter_text = quoted_passage(carter, CARTER_SEGMENTS)
    reagan_text = quoted_passage(reagan, REAGAN_SEGMENTS)
    commission_text = quoted_passage(commission, COMMISSION_SEGMENTS)

    P = []
    P.append("<!DOCTYPE html>")
    P.append('<html lang="en"><head><meta charset="utf-8">')
    P.append("<title>Unit Test: Modern America</title>")
    P.append(f"<style>{CSS}</style></head><body>")
    P.append('<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>')
    P.append('<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>')
    P.append("<h1>Unit Test: Modern America</h1>")
    P.append('<p class="directions"><strong>Total: 50 points.</strong> Part 1 is worth 15 points, Part 2 is worth 20 points, Part 3 is worth 15 points. Write answers on this test. For Part 3, answer in complete sentences and cite the sources by letter.</p>')

    P.append("<h2>Part 1: Matching (15 points)</h2>")
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

    P.append("<h2>Part 2: Multiple Choice (20 points)</h2>")
    P.append("<p>Choose the best answer for each question.</p>")
    for i, (q, opts, _, _) in enumerate(MC, 1):
        P.append(f'<div class="qa"><p class="q"><strong>{i}.</strong> {q}</p><p class="opts">')
        for j, o in enumerate(opts):
            P.append(f"<span>{letters[j]}. {o}</span>")
        P.append("</p></div>")

    P.append("<h2>Part 3: Sources (15 points)</h2>")
    P.append("<p>Answer each question in complete sentences, citing the sources by letter.</p>")
    P.append('<div class="source"><p class="srclabel">Source A</p>')
    P.append("<p>Jimmy Carter, Crisis of Confidence Address, July 15, 1979. From Jimmy Carter, 'Crisis of Confidence Address,' July 15, 1979 (Miller Center). Cuts are marked with ellipses in brackets.</p>")
    P.append(f"<p>&ldquo;{carter_text}&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>A1. (2 points)</strong> According to President Carter, what crisis strikes at the heart and soul and spirit of the national will, and what two losses does he say the country can see in it?</p><div class="sp-a"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>A2. (3 points)</strong> State how Carter says human identity had changed, give the evidence he offers that a majority of Americans expected the next five years to be worse than the past five, and state how he connects the solution of the energy crisis to the crisis of the spirit.</p><div class="sp-b"></div></div>')
    P.append('<div class="source"><p class="srclabel">Source B</p>')
    P.append("<p>Ronald Reagan, First Inaugural Address, January 20, 1981. From Ronald Reagan, 'First Inaugural Address,' January 20, 1981 (Gilder Lehrman Institute). Cuts are marked with ellipses in brackets.</p>")
    P.append(f"<p>&ldquo;{reagan_text}&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>B1. (2 points)</strong> According to President Reagan, what does sustained inflation penalize and whom does it crush, naming both groups he lists?</p><div class="sp-a"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>B2. (3 points)</strong> State Reagan\'s conclusion about government in the present crisis, and explain the reasoning he gives for it from the tax burden, public spending, and the deficits piled up over decades.</p><div class="sp-b"></div></div>')
    P.append('<div class="source"><p class="srclabel">Source C</p>')
    P.append("<p>National Commission on Terrorist Attacks Upon the United States, The 9/11 Commission Report: Executive Summary, 2004. From National Commission on Terrorist Attacks Upon the United States, 'The 9/11 Commission Report: Executive Summary,' 2004 (the Commission's own edition). Cuts are marked with ellipses in brackets.</p>")
    P.append(f"<p>&ldquo;{commission_text}&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>C1. (2 points)</strong> Who produced this report, how were its ten commissioners divided between the two parties, and to whom is the report presented, as the source states its own making?</p><div class="sp-a"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>C2. (3 points)</strong> Name the four failures the Commission found across the government, state which failure it calls the most important, and state its finding about the measures the government adopted from 1998 to 2001.</p><div class="sp-b"></div></div>')

    # ---------------- KEY ----------------
    from collections import Counter
    counts = Counter()
    P.append('<div class="key"><h2>Teacher Answer Key</h2>')
    P.append("<h3>Part 1: Matching</h3>")
    for i, (term, bp, _) in enumerate(MATCH):
        counts[bp] += 1
        P.append(f"<p><strong>{i + 1}. {term}: {desc_by_pos[i]}</strong> (Blueprint {bp})</p>")
    P.append("<h3>Part 2: Multiple Choice</h3>")
    for i, (q, opts, correct, bp) in enumerate(MC, 1):
        counts[bp] += 1
        P.append(f"<p><strong>{i}. {letters[correct]}</strong> (Blueprint {bp})</p>")
    P.append("<h3>Part 3: Sources</h3>")
    key3 = [
        ("A1", 1, "Carter names a crisis of confidence. He says it strikes at the very heart and soul and spirit of the national will. The country can see it, he says, in the growing doubt about the meaning of our own lives and in the loss of a unity of purpose for the nation. One point for the crisis named in the source's words and one point for both losses."),
        ("A2", 1, "Carter says human identity is no longer defined by what one does, but by what one owns, in a nation where too many people tend to worship self-indulgence and consumption, and he adds that owning and consuming things does not satisfy the longing for meaning. His evidence is that for the first time in the country's history a majority of the people believe the next five years will be worse than the past five years. He connects the two crises directly, stating that the solution of the energy crisis can also help conquer the crisis of the spirit by rekindling a sense of unity and confidence in the future. Full credit requires the identity claim, the majority evidence, and that connection."),
        ("B1", 3, "Reagan says sustained inflation distorts economic decisions and penalizes thrift. It crushes the struggling young and the fixed-income elderly alike. One point for thrift and one point for both groups named."),
        ("B2", 3, "Reagan concludes that in this present crisis, government is not the solution to the problem; government is the problem. His reasoning in the passage is that the tax burden, great as it is, has not kept pace with public spending, and that for decades the country has piled deficit upon deficit, mortgaging the future and children's future for the temporary convenience of the present. The tax system in the passage also penalizes successful achievement and keeps the country from maintaining full productivity. Full credit requires the conclusion in the source's words and at least two parts of that reasoning."),
        ("C1", 11, "The report was produced by the National Commission on Terrorist Attacks Upon the United States. Its ten commissioners were five Republicans and five Democrats, chosen by elected leaders, and the source states that they came together to present the report without dissent. The source states that it presents its narrative and recommendations to the President of the United States, the United States Congress, and the American people. One point for the commission and the five and five division and one point for the presentation without dissent."),
        ("C2", 11, "The Commission found failures of imagination, policy, capabilities, and management across the government. It calls the failure of imagination the most important failure, stating that leaders did not understand the gravity of the threat. Its finding on the measures adopted from 1998 to 2001 is that none of them disturbed or even delayed the progress of the al Qaeda plot. Full credit requires all four failures, the most important one named, and that finding stated."),
    ]
    for label, bp, ans in key3:
        counts[bp] += 1
        P.append(f"<p><strong>{label}.</strong> {ans} (Blueprint {bp})</p>")
    P.append("</div></body></html>")
    out = os.path.join(UNIT, "unit-test", "unit-test.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write("\n".join(P))
    print("coverage from printed tags:", dict(sorted(counts.items())))
    print("min per entry:", min(counts.values()), "entries covered:", len(counts))
    print("total items tagged:", sum(counts.values()))


if __name__ == "__main__":
    main()
