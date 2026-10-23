#!/usr/bin/env python3
"""Build the Depression and New Deal review study guide from the verbatim
vocabulary in build-scripts/unit-spec.md, plus 24 review questions with a
full key and the arguments of the era. Mirrors the Twenties study guide."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
UNIT = os.path.dirname(HERE)
SPEC = open(os.path.join(HERE, "unit-spec.md")).read()

LESSON_TITLES = {
    1: "The Human Cost of the Depression", 2: "Hoover and the Limits of Voluntarism",
    3: "Roosevelt and the First Hundred Days", 4: "Relief, Recovery, and the Alphabet Agencies at Work",
    5: "The Critics: Long, Townsend, Coughlin, and the Court", 6: "The Second New Deal",
    7: "Labor Rising and the Recession of 1937", 8: "What the New Deal Changed and What It Did Not",
}

def parse_terms():
    terms = {}
    current = None
    for line in SPEC.splitlines():
        m = re.match(r"### Lesson (\d)", line)
        if m:
            current = int(m.group(1)); terms[current] = []
            continue
        m = re.match(r"- ([^:]+): (.+)$", line)
        if m and current:
            terms[current].append((m.group(1).strip(), m.group(2).strip()))
    return terms

QUESTIONS = [
    (1, "How deep did the collapse run by 1933? Give three measures.",
     "By the standard historical estimates, unemployment reached about one worker in four in 1933, industrial production fell by roughly half from 1929, and thousands of banks failed, with farm prices falling so far that many crops returned less than the cost of growing them. Any three accurate measures from the reading earn credit."),
    (1, "Why did deflation make the Depression worse for debtors?",
     "Debts stay fixed in dollars while prices and incomes fall, so each payment costs more in real terms. Farmers and homeowners owed the same mortgage on smaller earnings, which pushed foreclosures and bank losses higher in a circle."),
    (1, "Name three forms the human cost took in everyday life, and the evidence for each from Lesson 1.",
     "Breadlines and soup kitchens, as charities and cities fed lines of unemployed people. Hoovervilles, the scrap built shantytowns where homeless families lived. Dust Bowl migration, as drought and dust drove Plains farm families west. Eviction, doubled up households, and postponed marriages and births also earn credit."),
    (2, "What did voluntarism ask of business, charity, and local government, and what did it refuse?",
     "It asked business to hold wages and keep workers, charities to feed the hungry, and cities and states to run relief, all by cooperation and pledge rather than law. It refused direct federal relief payments to individuals, which Hoover held would weaken character and unbalance the budget."),
    (2, "Hoover did more than the caricature of him allows. Name three federal actions he took.",
     "Any three: the Federal Farm Board supporting farm prices, expanded public works spending, the Reconstruction Finance Corporation lending to banks and railroads in 1932, the Emergency Relief and Construction Act authorizing federal relief loans to states, and federal action on drought relief. The Hawley-Smoot Tariff also counts as an action, though its effects cut the other way."),
    (2, "Why did the Bonus Army episode damage Hoover beyond its size?",
     "Veterans asking early payment of a promised bonus were driven from Washington by federal troops under his command in the summer of an election year. The photographs and reports fixed the public image of a president using soldiers against hungry veterans while refusing relief."),
    (3, "How did the bank holiday and the Emergency Banking Act work as a pair?",
     "The holiday closed every bank on March 6, 1933, stopping the runs. The Act of March 9 let examiners sort the banks and licensed only sound ones to reopen, with federal lending behind them, so reopening itself became evidence of soundness."),
    (3, "What did the first fireside chat do that no law could do?",
     "It explained the banking system in plain language to a national radio audience and asked people to trust the reopened banks. Deposits flowed back in the days after, supplying the confidence the rescue depended on."),
    (3, "Name four laws of the Hundred Days and the problem each one answered.",
     "Any four: the Emergency Banking Act for the bank runs, the Agricultural Adjustment Act for farm prices, the Tennessee Valley Authority for a flooded and unpowered river region, the National Industrial Recovery Act for industrial collapse and codes, the Glass-Steagall Act for banking structure and deposit insurance. The Civilian Conservation Corps, created in the same season, answers unemployment."),
    (4, "State the difference between direct relief and work relief, and give one agency of each kind.",
     "Direct relief gives money, food, or goods to people in need with no work required; the Federal Emergency Relief Administration worked this way through the states. Work relief pays wages for jobs on public projects; the Civilian Conservation Corps, Civil Works Administration, and Public Works Administration are the lesson's examples."),
    (4, "Why was the Civil Works Administration shut down after one winter?",
     "It hired about four million people quickly in the winter of 1933 to 1934, and the administration judged its cost too high and its make-work reputation a political risk as spring came. Hopkins himself wound it down while warning that need remained."),
    (4, "In what ways did the agencies' help reach Americans unevenly?",
     "CCC camps were segregated, relief payments varied by state and locality and were often lower for Black families, women were channeled into a narrow set of sewing and canning projects, and some local administrators used relief to discipline farm labor. The programs were federal in funding and local in delivery, and the local customs came with them."),
    (5, "What did Long, Townsend, and Coughlin each say the New Deal had failed to do?",
     "Long said it had left great fortunes untouched and promised through Share Our Wealth to cap them and guarantee every family a homestead and income. Townsend said it had left the old without support and promised two hundred dollars a month to every citizen over sixty. Coughlin said it had failed to break the power of bankers and money interests. All three charged the New Deal with doing too little."),
    (5, "What did the Liberty League and the Supreme Court charge from the other direction?",
     "They charged that the New Deal did too much, going beyond the Constitution. The League organized wealthy opposition. The Court struck down the National Industrial Recovery Act in Schechter in 1935 and the Agricultural Adjustment Act in Butler in 1936."),
    (5, "Why did pressure from both directions push Roosevelt toward a Second New Deal?",
     "The mass movements showed him millions of voters ready to follow more sweeping promises, and the Court showed him his first program being dismantled. Answering the first group and outlasting the second both required a larger, more durable settlement in 1935."),
    (6, "What three permanent systems did the Social Security Act set running?",
     "Old-age insurance paying retired workers from payroll taxes, unemployment insurance run jointly with the states paying temporary benefits to job losers, and aid to dependent children and other vulnerable groups. The old-age insurance system is the one still at the center of American retirement."),
    (6, "Who was left out of Social Security at the start, and why does the exclusion matter for judging the law?",
     "Agricultural and domestic workers were excluded, an exclusion that left out a large share of Black workers and many women workers. The exclusion counts in judging the law because its universality, the quality that made it durable, was partial from its first day, and the missing workers were those with the least bargaining power."),
    (6, "What did the Wagner Act guarantee, and what machinery did it create to make the guarantee real?",
     "It guaranteed workers the right to organize unions of their own choosing and to bargain collectively, and it created the National Labor Relations Board to run elections and police unfair labor practices. The board is what turned a stated right into an enforceable one."),
    (7, "Why did the sit-down strike work at Flint when ordinary strikes had failed in the auto industry?",
     "By staying inside the plant, the strikers kept replacement workers out and kept the company from running its machines with other hands, and the governor refused to clear the plant by force. After forty-four days General Motors recognized the United Auto Workers."),
    (7, "What did Roosevelt propose in February 1937, and how did the fight end?",
     "He proposed adding a new Supreme Court justice for each sitting justice over seventy, up to six new seats. The Senate defeated the plan as an attack on the Court. In the same season the Court upheld the Wagner Act and Social Security and began sustaining New Deal laws, and retirements soon let him appoint justices by the ordinary route."),
    (7, "What caused the Roosevelt recession, in the administration's own later judgment?",
     "The government pulled support away too soon. Federal spending was cut and the new Social Security payroll taxes began collecting before benefits flowed, taking money out of a weak economy, and production and employment fell sharply into 1938."),
    (8, "Name four changes from the New Deal that are still operating today.",
     "Any four: federal insurance of bank deposits through the FDIC, regulation of stock markets by the SEC, Social Security, unemployment insurance, federal minimum wage and overtime law under the Fair Labor Standards Act, the Tennessee Valley Authority's power system, and federal protection of the right to organize."),
    (8, "What is the strongest evidence that the New Deal did not end the Depression?",
     "Unemployment never fell below fourteen percent in any year of the 1930s and stood near nineteen percent again in 1938. Full employment arrived only with the enormous spending of the Second World War."),
    (8, "State the two measures by which Lesson 8 says the New Deal should be judged, and give a verdict under each.",
     "Against the collapse it answered, it was relief and reform on a scale the country had never attempted, and it kept a democratic government standing through a collapse that broke governments elsewhere. Against full recovery and equal treatment, it stopped short: the Depression outlasted it, and its benefits were written with exclusions. A verdict that uses both measures and evidence from the unit earns full credit."),
]

ARGUMENTS = [
    ("Emergency or misfortune", "The unit's first argument is about what a depression is. Hoover treated the collapse as a misfortune to be weathered by private effort with limited federal help. Roosevelt treated it as a public emergency that licensed federal action. Every later fight in the unit, over agencies, critics, courts, and budgets, is this argument returning in a new form."),
    ("Experiment and settlement", "The first New Deal of 1933 was a season of experiments, many of them temporary and some of them struck down. The second, in 1935, built permanent systems for old age, unemployment, and labor rights. Judging the New Deal means keeping the two seasons separate, because they were built for different purposes."),
    ("Who was inside the settlement", "The New Deal's benefits ran through local delivery and founding exclusions, so its reach differed by race, sex, region, and occupation. The unit treats that unevenness as part of the record, not an exception to it, and the test asks about it directly."),
    ("The recovery that waited", "The New Deal relieved, employed, and reformed, and the Depression still outlasted it. Full employment came with war spending. The honest verdict the unit builds toward is that the New Deal changed the country permanently and ended the Depression only in part, and both halves of that sentence are required."),
]

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
.q { margin: 8pt 0 0; }
.qa { break-inside: avoid; }
.sp-a { height: 0.62in; }
table.terms { border-collapse: collapse; width: 100%; margin: 4pt 0 10pt; }
table.terms th, table.terms td { border: 1px solid #000; padding: 5pt 6pt; text-align: left; font-size: 11pt; vertical-align: top; }
table.terms td.row { height: 0.52in; }
table.terms td.filled { font-size: 10.5pt; line-height: 1.3; }
.arguments { break-before: page; }
.arguments h2:first-child { margin-top: 0; }
.key { break-before: page; }
.key h2:first-child { margin-top: 0; }
.brandmark { margin: 0 0 4pt; line-height: 0; } .brandmark img { width: 1.35in; }
"""

def main():
    terms = parse_terms()
    cb = [d for t, d in terms[6] if t == "collective bargaining"][0]
    terms[7] = [("collective bargaining (carried from Lesson 6)", cb)] + terms[7]
    total = sum(len(v) for v in terms.values())
    P = []
    P.append("<!DOCTYPE html>")
    P.append('<html lang="en"><head><meta charset="utf-8">')
    P.append("<title>Study Guide: The Depression and New Deal</title>")
    P.append(f"<style>{CSS}</style></head><body>")
    P.append('<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>')
    P.append('<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>')
    P.append("<h1>Study Guide: The Depression and New Deal</h1>")
    P.append('<p class="directions"><strong>Directions:</strong> Complete Part 1 from your guided notes and readings, then answer the Part 2 questions in your own words. Part 3 summarizes the arguments that run through the whole unit. The unit test is built from this guide. Bring questions about anything you cannot answer to the review day.</p>')
    P.append("<p><strong>Unit question:</strong> How did the New Deal change the relationship between Americans and their federal government, and what did it leave undone?</p>")
    P.append("<h2>Part 1: Key Terms</h2>")
    P.append("<p>Write the definition of each term in your own notebook wording, then check it against your guided notes.</p>")
    for n in range(1, 9):
        P.append(f"<h3>Lesson {n}: {LESSON_TITLES[n]}</h3>")
        P.append('<table class="terms">')
        for term, _ in terms[n]:
            P.append(f'<tr><td style="width:30%">{term}</td><td class="row"></td></tr>')
        P.append("</table>")
    P.append("<h2>Part 2: Review Questions</h2>")
    for i, (_, q, _) in enumerate(QUESTIONS, 1):
        P.append(f'<div class="qa"><p class="q"><strong>{i}.</strong> {q}</p><div class="sp-a"></div></div>')
    P.append('<div class="arguments"><h2>Part 3: The Arguments of the Era</h2>')
    for title, body in ARGUMENTS:
        P.append(f"<p><strong>{title}.</strong> {body}</p>")
    P.append("</div>")
    P.append('<div class="key"><h2>Teacher Answer Key</h2>')
    P.append("<h3>Part 1: Key Terms</h3>")
    for n in range(1, 9):
        P.append(f"<h3>Lesson {n}: {LESSON_TITLES[n]}</h3>")
        P.append('<table class="terms">')
        for term, dfn in terms[n]:
            P.append(f'<tr><td style="width:30%">{term}</td><td class="filled">{dfn}</td></tr>')
        P.append("</table>")
    P.append("<h3>Part 2: Review Questions</h3>")
    for i, (_, q, a) in enumerate(QUESTIONS, 1):
        P.append(f"<p><strong>{i}. {q}</strong> {a}</p>")
    P.append("</div></body></html>")
    out = os.path.join(UNIT, "review", "review-study-guide.html")
    open(out, "w").write("\n".join(P))
    print(f"wrote {out}: {total} terms, {len(QUESTIONS)} questions")

if __name__ == "__main__":
    main()
