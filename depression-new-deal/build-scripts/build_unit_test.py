#!/usr/bin/env python3
"""Build the Depression and New Deal unit test (50 points) in the Twenties
test format: matching 15, multiple choice 20, source-based 15, with every
item tagged to the blueprint in the key. Coverage is recomputed from the
tags this script prints."""
import os

UNIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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

# (term, blueprint entry, description) descriptions are the spec definitions
MATCH = [
    ("deflation", 1, "a general fall in prices across the economy, which raises the real burden of debts and rewards waiting to spend"),
    ("Hooverville", 2, "a shantytown built by homeless people from scrap wood, tin, and cardboard during the Depression, named in bitter reference to President Hoover"),
    ("voluntarism", 3, "Hoover's policy of meeting the Depression through voluntary cooperation by business, charities, and local government rather than through federal relief programs"),
    ("Reconstruction Finance Corporation", 4, "the federal agency created in 1932 that lent public money to banks, railroads, and insurance companies in the hope that stability at the top would restore jobs below"),
    ("bank holiday", 5, "the closing of all the nation's banks by presidential proclamation on March 6, 1933, so that examiners could sort sound banks from failed ones before reopening"),
    ("Tennessee Valley Authority", 6, "the federal corporation created in 1933 to build dams, control flooding, and bring electricity and development to the Tennessee River valley"),
    ("Civilian Conservation Corps", 7, "the 1933 program that employed young men in camps to plant trees, fight fires, and build park roads and trails, paying thirty dollars a month, most of it sent home"),
    ("National Recovery Administration", 8, "the agency created in 1933 to write and enforce codes of fair competition for each industry, setting prices, wages, and hours and allowing workers to organize"),
    ("Share Our Wealth", 9, "Huey Long's program and movement, begun in 1934, which promised to cap large fortunes and guarantee every family a homestead and a minimum income"),
    ("Schechter v. United States", 10, "the 1935 Supreme Court decision that struck down the National Industrial Recovery Act, holding that Congress had given away its lawmaking power and reached business beyond its authority"),
    ("Works Progress Administration", 11, "the agency created in 1935, led by Harry Hopkins, that employed about eight and a half million people over its life building roads, schools, and airports and funding arts and writing projects"),
    ("National Labor Relations Act", 12, "the 1935 law, called the Wagner Act, that guaranteed workers the right to organize unions and bargain collectively and created a board to enforce those rights"),
    ("sit-down strike", 13, "a strike in which workers stop work and remain inside the factory, holding the plant so that replacement workers cannot be brought in"),
    ("court packing", 14, "the name opponents gave Roosevelt's 1937 proposal to add a new justice to the Supreme Court for each sitting justice over seventy, which would have let him appoint up to six"),
    ("safety net", 15, "the set of government programs that catch people who fall into poverty through old age, unemployment, disability, or the loss of a family earner"),
]
# letter order for descriptions (index into MATCH shuffled by hand)
ORDER = [7, 0, 13, 4, 10, 2, 15 - 1, 5, 1, 12, 8, 3, 11, 6, 9]

# (question, options[4], correct index, blueprint entry)
MC = [
    ("By 1933, the depth of the collapse was visible in all of these measures EXCEPT",
     ["about one worker in four unemployed", "industrial production cut by roughly half from 1929",
      "thousands of bank failures", "a rapid rise in consumer prices across the economy"], 3, 1),
    ("Farm families left the southern Plains in large numbers in the 1930s chiefly because",
     ["federal law ordered the region evacuated", "drought and dust storms destroyed the farming the land had supported",
      "railroads offered free passage west", "California growers seized their land"], 1, 2),
    ("Hoover's voluntarism asked which groups to carry relief for the unemployed?",
     ["the federal government, through direct payments", "business, charities, and local government, by cooperation",
      "the army and the national guard", "foreign governments, through loans"], 1, 3),
    ("The Bonus Army episode of 1932 ended when",
     ["Congress paid the bonus in full", "the veterans voted to go home on their own",
      "federal troops drove the veterans out of their Washington camps", "Roosevelt promised payment after the election"], 2, 4),
    ("The Emergency Banking Act of March 9, 1933 worked together with the bank holiday by",
     ["creating the Federal Reserve", "letting examiners sort the banks and licensing only sound ones to reopen",
      "guaranteeing every deposit in full on its first day", "closing the banks for the rest of 1933"], 1, 5),
    ("The Agricultural Adjustment Act tried to raise farm prices by",
     ["ordering farmers to grow more", "paying farmers to reduce production of basic crops and livestock",
      "banning imported food", "setting one national price for wheat by decree"], 1, 6),
    ("A young man enrolled in the Civilian Conservation Corps could expect",
     ["a college scholarship", "camp work planting trees and building park roads for thirty dollars a month, most of it sent home",
      "a permanent job in a national park", "training as a bank examiner"], 1, 7),
    ("Which statement about the New Deal's reach by 1934 is accurate?",
     ["unemployment had returned to its 1929 level", "every agency delivered its benefits on equal terms in every state",
      "millions had been helped and hired, and unemployment still stood far above any level known before 1929",
      "the Supreme Court had upheld every major program"], 2, 8),
    ("Dr. Francis Townsend's plan promised",
     ["a homestead for every family, paid for by capping fortunes", "two hundred dollars a month to every citizen over sixty, to be spent within the month",
      "a government job for every unemployed worker", "free radio broadcasts exposing the banks"], 1, 9),
    ("In United States v. Butler (1936), the Supreme Court struck down",
     ["the Social Security Act", "the Wagner Act",
      "the Agricultural Adjustment Act's processing tax", "the Tennessee Valley Authority"], 2, 10),
    ("The Social Security Act of 1935 created all of these EXCEPT",
     ["old-age insurance for retired workers", "unemployment insurance run with the states",
      "aid to dependent children", "a national system of free hospitals"], 3, 11),
    ("The National Labor Relations Board was created to",
     ["set the national minimum wage", "run union elections and police unfair labor practices",
      "assign unemployed workers to WPA jobs", "approve every strike before it could begin"], 1, 12),
    ("The Flint sit-down strike of 1936 to 1937 ended when",
     ["the governor sent troops to clear the plants", "General Motors recognized the United Auto Workers",
      "the Supreme Court ordered the workers out", "the strikers accepted a small wage increase and no union"], 1, 13),
    ("The Roosevelt recession of 1937 to 1938 followed",
     ["a new round of bank failures in the South", "federal spending cuts and new payroll taxes pulling money out of a weak economy",
      "a decision by the Federal Reserve to end deposit insurance", "the outbreak of war in Europe"], 1, 14),
    ("The clearest measure of what the New Deal left undone is that",
     ["no New Deal program survived past 1939", "unemployment never fell below fourteen percent in any year of the decade and full employment came only with war spending",
      "the federal government withdrew from economic life after 1938", "voters removed the Democratic Party from power in 1936"], 1, 15),
    ("Deflation deepened the Depression chiefly because",
     ["it made imported goods cheaper than American goods", "debts stayed fixed in dollars while prices and incomes fell, raising the real burden of every payment",
      "it raised wages faster than prices", "it persuaded depositors that banks were sound"], 1, 1),
    ("In the first fireside chat, Roosevelt's main purpose was to",
     ["announce the court packing plan", "explain the banking rescue in plain language so depositors would trust the reopened banks",
      "ask Congress for a declaration of war", "introduce the Social Security bill"], 1, 5),
    ("Huey Long's Share Our Wealth movement pressured Roosevelt chiefly by",
     ["winning seats in the Senate", "building a national network of clubs behind a promise to cap fortunes and guarantee family incomes",
      "persuading the Supreme Court to hear his case", "organizing a general strike"], 1, 9),
    ("The Works Progress Administration differed from the Social Security Act in that the WPA",
     ["was a permanent insurance system", "put people to work on public projects and ended when its appropriations ended",
      "was funded by a payroll tax", "covered only retired workers"], 1, 11),
    ("Which founding exclusion most limited the New Deal settlement's claim to cover all Americans?",
     ["the exclusion of bankers from deposit insurance", "the exclusion of agricultural and domestic workers from Social Security at the start",
      "the exclusion of veterans from the CCC", "the exclusion of southern states from the TVA"], 1, 15),
]

def main():
    P = []
    P.append("<!DOCTYPE html>")
    P.append('<html lang="en"><head><meta charset="utf-8">')
    P.append("<title>Unit Test: The Depression and New Deal</title>")
    P.append(f"<style>{CSS}</style></head><body>")
    P.append('<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>')
    P.append('<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>')
    P.append("<h1>Unit Test: The Depression and New Deal</h1>")
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
    P.append("<p>President Franklin D. Roosevelt, first fireside chat on the banking crisis, March 12, 1933. From the transcript held by the Franklin D. Roosevelt Presidential Library and Museum.</p>")
    P.append("<p>&ldquo;First of all, let me state the simple fact that when you deposit money in a bank the bank does not put the money into a safe deposit vault. It invests your money in many different forms of credit, in bonds, in commercial paper, in mortgages and in many other kinds of loans. . . . What, then, happened during the last few days of February and the first few days of March? Because of undermined confidence on the part of the public, there was a general rush by a large portion of our population to turn bank deposits into currency or gold, a rush so great that the soundest banks could not get enough currency to meet the demand.&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>A1. (2 points)</strong> According to Roosevelt, what caused the rush that even the soundest banks could not meet?</p><div class="sp-a"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>A2. (3 points)</strong> Why did explaining the banking system on the radio serve the rescue as no statute could on its own? Answer from the source and the lesson.</p><div class="sp-b"></div></div>')
    P.append('<div class="source"><p class="srclabel">Source B</p>')
    P.append("<p>The Social Security Act, August 14, 1935, Title I, Section 1. From the United States Statutes at Large, Volume 49.</p>")
    P.append("<p>&ldquo;For the purpose of enabling each State to furnish financial assistance, as far as practicable under the conditions in such State, to aged needy individuals, there is hereby authorized to be appropriated for each fiscal year a sum sufficient to carry out the purposes of this title.&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>B1. (2 points)</strong> State in your own words what this section set the federal government to fund, and through whom the help would reach people.</p><div class="sp-a"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>B2. (3 points)</strong> The Social Security Act built three systems. Name the other two besides old-age assistance, and name one group of workers the Act left out at the start.</p><div class="sp-b"></div></div>')
    P.append('<div class="source"><p class="srclabel">Source C</p>')
    P.append('<img src="migrant-mother-1936.jpg" alt="Migrant Mother photograph">')
    P.append('<p class="caption">Dorothea Lange, photograph of Florence Owens Thompson and her children, Nipomo, California, March 1936. Farm Security Administration, Library of Congress.</p>')
    P.append("<p>Lange, a photographer working for the federal relief agencies, took this picture at a camp of migrant pea pickers and sent it to Washington. Newspapers printed it within days, and the government rushed food to the camp.</p></div>")
    P.append('<div class="qa"><p class="q"><strong>C1. (2 points)</strong> What conditions in the country produced the scene in this photograph? Name two.</p><div class="sp-a"></div></div>')
    P.append("<div class=\"qa\"><p class=\"q\"><strong>C2. (3 points)</strong> This photograph was made by a photographer paid by the federal government. What does its existence, and the response to it, show about how the federal role had changed since the breadline years?</p><div class=\"sp-b\"></div></div>")

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
        ("A1", 5, "The rush was caused by undermined public confidence. Depositors across the country tried at the same time to turn deposits into currency or gold, a demand no bank, however sound, could meet from its cash on hand."),
        ("A2", 5, "The statutes could close, examine, and license banks, but reopening would fail if depositors withdrew again at once. The chat rebuilt the confidence the system ran on by explaining in plain language where deposits go and why the reopened banks could be trusted. Deposits flowed back after the broadcast, which is the evidence the explanation did the work."),
        ("B1", 11, "The section authorizes federal money so that each state can give financial assistance to aged people in need. The help would reach people through the states, under state plans, with the federal government paying."),
        ("B2", 11, "Besides old-age assistance, the Act created old-age insurance paying retired workers from payroll taxes, and unemployment insurance run with the states. Either also earns credit: aid to dependent children. Left out at the start: agricultural workers and domestic workers, an exclusion that fell hardest on Black workers and on women."),
        ("C1", 2, "Any two: mass unemployment that left migrant families without wages, farm collapse and low crop prices, drought and the Dust Bowl driving families off the land, and the seasonal poverty of migrant field labor. The family in the photograph were migrant pea pickers living in a camp."),
        ("C2", 2, "Under Hoover the federal government had refused direct relief and left feeding people to charities and cities. By 1936 a federal agency employed the photographer, documented the need as official business, and answered publication with a federal food shipment. The government's role had changed from referee to provider, and documenting need had become part of governing."),
    ]
    for label, bp, ans in key3:
        counts[bp] += 1
        P.append(f"<p><strong>{label}.</strong> {ans} (Blueprint {bp})</p>")
    P.append("</div></body></html>")
    out = os.path.join(UNIT, "unit-test", "unit-test.html")
    open(out, "w").write("\n".join(P))
    print("coverage from printed tags:", dict(sorted(counts.items())))
    print("min per entry:", min(counts.values()), "entries covered:", len(counts))

if __name__ == "__main__":
    main()
