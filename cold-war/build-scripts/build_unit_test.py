#!/usr/bin/env python3
"""Build the Cold War unit test (50 points) in the established test
format: matching 15, multiple choice 20, source-based 15, with every
item tagged to the blueprint in the key. Coverage is recomputed from
the tags this script prints. Sources are quoted verbatim from the
audited TPSP bank records in cold-war.json, with cuts marked by
ellipses and the edition named in each Source line."""
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

# (term, blueprint entry, description) descriptions are the spec definitions, verbatim
MATCH = [
    ("Iron Curtain", 1, "the boundary Winston Churchill named in 1946 between the Soviet-dominated states of Eastern Europe and the free states of the West, and the division of Europe it described"),
    ("Truman Doctrine", 2, "the policy President Truman declared in 1947, that the United States would support free peoples resisting attempted subjugation by armed minorities or outside pressures"),
    ("NSC-68", 3, "the secret American planning paper of 1950 that described the Cold War as a global struggle and called for a large buildup of American military strength"),
    ("Korean War", 4, "the war of 1950 to 1953 in which the United States and United Nations forces fought North Korea and China to preserve a non-Communist South Korea"),
    ("House Un-American Activities Committee", 5, "the House of Representatives committee that investigated alleged Communist influence in American life, most famously in its hearings on the film industry in 1947"),
    ("McCarthyism", 6, "the practice of making public accusations of Communist disloyalty without firm evidence, named for Senator Joseph McCarthy, who made his charges the center of a national campaign from 1950 to 1954"),
    ("hydrogen bomb", 7, "a thermonuclear weapon far more powerful than the atomic bombs of 1945, first tested by the United States in 1952 and by the Soviet Union in 1953"),
    ("Sputnik", 8, "the first artificial satellite, launched by the Soviet Union in October 1957, whose success shocked the United States and opened the space race"),
    ("Bay of Pigs invasion", 9, "the failed invasion of Cuba in April 1961 by Cuban exiles trained and supplied by the United States, defeated on the beach within three days"),
    ("Cuban Missile Crisis", 10, "the confrontation of October 1962 in which the United States discovered Soviet nuclear missiles being installed in Cuba and forced their withdrawal short of war"),
    ("Gulf of Tonkin Resolution", 11, "the resolution Congress passed in August 1964 giving the president authority to take all necessary measures to repel attacks on American forces and prevent further aggression in Southeast Asia"),
    ("Tet Offensive", 12, "the coordinated attacks by North Vietnamese and Viet Cong forces across South Vietnam in January 1968, a military defeat for the attackers that shook American confidence in official claims of progress"),
    ("détente", 13, "the easing of tension between the United States and the Soviet Union pursued in the 1970s, built on arms agreements, trade, and regular summit meetings"),
    ("Strategic Defense Initiative", 14, "President Reagan's 1983 proposal to build a defense in space against nuclear missiles, called Star Wars by its critics, which promised protection deterrence could not"),
    ("glasnost", 15, "Mikhail Gorbachev's policy of openness in the Soviet Union from 1985, allowing public discussion, criticism of officials, and a freer press"),
]
# letter order for descriptions (index into MATCH shuffled by hand)
ORDER = [4, 12, 1, 9, 6, 14, 2, 10, 0, 7, 13, 3, 11, 5, 8]

# (question, options[4], correct index, blueprint entry)
MC = [
    ("In the Long Telegram of February 1946, George Kennan argued that Soviet expansion",
     ["would end as soon as the United States offered trade concessions",
      "was driven by ideology and insecurity and could be contained by firm resistance",
      "posed no threat beyond the Soviet Union's own borders",
      "could be reversed by an immediate American invasion"], 1, 1),
    ("The Marshall Plan, in operation from 1948 to 1952, was chiefly",
     ["a program that gave about thirteen billion dollars in aid to rebuild the economies of Western Europe",
      "a lend of weapons to the Greek and Turkish armies",
      "the treaty that created the North Atlantic Treaty Organization",
      "a loan program for the rebuilding of Japan"], 0, 2),
    ("NSC-68, the secret planning paper of April 1950, called for",
     ["an immediate withdrawal from Asia",
      "a negotiated division of Korea",
      "a large buildup of American military strength for a global struggle against Soviet expansion",
      "the abolition of nuclear weapons by both sides"], 2, 3),
    ("President Truman dismissed General MacArthur in April 1951 chiefly because MacArthur",
     ["had lost the battle for Seoul",
      "had publicly defied the president's policy and demanded a wider war, and Truman defended civilian control and keeping the war limited",
      "asked to retire after the Inchon landing",
      "refused to serve under the United Nations flag"], 1, 4),
    ("The Hollywood Ten were",
     ["ten senators who censured Joseph McCarthy",
      "ten studio owners who created the blacklist",
      "ten accused spies inside the State Department",
      "ten screenwriters and directors who refused to answer the House Un-American Activities Committee's questions in 1947, were cited for contempt, and went to prison"], 3, 5),
    ("The Army-McCarthy hearings of 1954 weakened Senator McCarthy chiefly because",
     ["millions of Americans watched the televised hearings and the Senate censured him later that year",
      "the Army proved that he had been a Communist",
      "President Eisenhower removed him from the Senate",
      "the Supreme Court ordered the hearings stopped"], 0, 6),
    ("Massive retaliation, as the Eisenhower administration declared it, meant answering Communist aggression with",
     ["a matching force at the exact point of attack",
      "economic sanctions alone",
      "the threat of a full nuclear strike, rather than matching force at the point of attack",
      "a covert operation in every case"], 2, 7),
    ("Sputnik, launched in October 1957, shocked the United States chiefly because it",
     ["was the first Soviet hydrogen bomb",
      "was the first artificial satellite, and its success was heard as proof the country had fallen behind and opened the space race",
      "photographed American missile sites from orbit",
      "carried the first person into space"], 1, 8),
    ("The Bay of Pigs invasion of April 1961 ended with",
     ["Castro's government overthrown in three days",
      "a negotiated American occupation of Havana",
      "Soviet troops landing in Cuba",
      "Cuban exiles trained and supplied by the United States defeated on the beach within three days"], 3, 9),
    ("The Cuban Missile Crisis of October 1962 was settled by",
     ["Soviet missiles withdrawn from Cuba for an American promise not to invade Cuba, with American Jupiter missiles secretly removed from Turkey months later",
      "an American invasion that destroyed the missile sites",
      "a United Nations vote expelling the Soviet Union",
      "Cuba joining the North Atlantic Treaty Organization"], 0, 10),
    ("The Gulf of Tonkin Resolution of August 1964",
     ["ordered American ground troops home from Vietnam",
      "declared war on North Vietnam",
      "gave the president authority to take all necessary measures to repel attacks on American forces and prevent further aggression in Southeast Asia",
      "divided Vietnam at the 17th parallel"], 2, 11),
    ("The Tet Offensive of January 1968 was a turning point chiefly because it",
     ["destroyed the North Vietnamese army in the field",
      "was a military defeat for the attackers that shook American confidence in official claims of progress",
      "brought China into the Vietnam War",
      "ended the draft in the United States"], 1, 12),
    ("The Helsinki Accords of 1975 gave the Soviet Union and its allies",
     ["control of West Berlin",
      "membership in the North Atlantic Treaty Organization",
      "a promise of American grain sales only",
      "recognition of Europe's postwar borders, in an agreement in which they also pledged respect for human rights, a pledge dissidents later used against their own governments"], 3, 13),
    ("The Reagan Doctrine of the 1980s was the policy under which the United States",
     ["aided anti-Communist insurgencies fighting Soviet-backed governments, in Afghanistan, Nicaragua, and elsewhere",
      "recognized the Soviet Union's postwar borders in Europe",
      "withdrew from the North Atlantic Treaty Organization",
      "ended all covert action abroad"], 0, 14),
    ("The dissolution of the Soviet Union in December 1991 was",
     ["the signing of the INF Treaty in Washington",
      "the breach of the Berlin Wall by crowds",
      "the ending of the Soviet Union, when its republics declared independence and the state that had stood since 1922 ceased to exist",
      "the reunification of Germany in October 1990"], 2, 15),
    ("NATO, formed in 1949, pledged its members to",
     ["divide Germany into two states",
      "treat an attack on one member as an attack on all",
      "rebuild the economies of Western Europe",
      "ban nuclear weapons tests in the atmosphere"], 1, 2),
    ("The Korean armistice of 1953",
     ["unified Korea under one government",
      "gave South Korea control of the whole peninsula",
      "was a peace treaty signed in Washington",
      "ended the shooting without a peace treaty or a political settlement"], 3, 4),
    ("President Kennedy called the naval blockade of Cuba in 1962 a quarantine chiefly because",
     ["a blockade is legally an act of war and quarantine was not",
      "the Navy had no ships for a blockade",
      "the Soviet Union requested the word",
      "a quarantine required a declaration of war"], 0, 10),
    ("Vietnamization, under President Nixon, was the policy of",
     ["sending more American ground troops each year",
      "dividing Vietnam permanently into two states",
      "withdrawing American troops while building up South Vietnam's forces to carry the fighting themselves",
      "turning the war over to the United Nations"], 2, 12),
    ("The Berlin Wall, breached by crowds on November 9, 1989, had been",
     ["built in 1945 by the four occupying powers",
      "the wall the East German government built in 1961 to stop its citizens fleeing to the West, and the central symbol of the divided Europe",
      "a wall around the Soviet embassy in Berlin",
      "demolished by treaty in 1987"], 1, 15),
]

def main():
    P = []
    P.append("<!DOCTYPE html>")
    P.append('<html lang="en"><head><meta charset="utf-8">')
    P.append("<title>Unit Test: The Cold War</title>")
    P.append(f"<style>{CSS}</style></head><body>")
    P.append('<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>')
    P.append('<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>')
    P.append("<h1>Unit Test: The Cold War</h1>")
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
    P.append("<p>President Harry S. Truman, Truman Doctrine Address, March 12, 1947. From Harry S. Truman, 'Truman Doctrine Address,' March 12, 1947 (Harry S. Truman Library, Public Papers). A cut is marked with ellipses.</p>")
    P.append("<p>&ldquo;I believe that it must be the policy of the United States to support free peoples who are resisting attempted subjugation by armed minorities or by outside pressures. . . . I believe that our help should be primarily through economic and financial aid which is essential to economic stability and orderly political processes.&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>A1. (2 points)</strong> According to Truman, what must the policy of the United States be, and what two kinds of pressure are the free peoples in his statement resisting?</p><div class="sp-a"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>A2. (3 points)</strong> Truman says American help should be primarily of one kind. Name that kind, state the reason he gives for choosing it, and explain how the Marshall Plan carried the same idea to Western Europe.</p><div class="sp-b"></div></div>')
    P.append('<div class="source"><p class="srclabel">Source B</p>')
    P.append("<p>National Security Council, NSC-68, April 7, 1950. From National Security Council, 'NSC-68,' April 7, 1950 (declassified report; Truman Library). Cuts are marked with ellipses, as in the bank record.</p>")
    P.append("<p>&ldquo;[...] The Soviet Union, unlike previous aspirants to hegemony, is animated by a new fanatic faith, antithetical to our own, and seeks to impose its absolute authority over the rest of the world. [...] A more rapid build-up of political, economic, and military strength and thereby of confidence in the free world than is now contemplated is the only course which is consistent with progress toward achieving our fundamental purpose. [...]&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>B1. (2 points)</strong> How does NSC-68 describe the Soviet Union, and what does the paper say the Soviet Union seeks?</p><div class="sp-a"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>B2. (3 points)</strong> What course does NSC-68 call the only course consistent with its purpose, and how did the shocks of 1949 and the start of the Korean War turn that call into policy?</p><div class="sp-b"></div></div>')
    P.append('<div class="source"><p class="srclabel">Source C</p>')
    P.append('<img src="u2-cuban-missile-sites-1962.jpg" alt="U-2 reconnaissance photograph of Soviet missile sites in Cuba">')
    P.append('<p class="caption">United States Air Force, U-2 reconnaissance photograph of Soviet missile sites in Cuba, October 14, 1962. U.S. government photograph.</p>')
    P.append("<p>From United States Air Force, 'U-2 reconnaissance photo of Soviet missile sites in Cuba,' October 14, 1962 (U.S. government photograph; image described). The bank record describes the image in these words: &ldquo;Visual description: A grainy black-and-white aerial photograph taken from high altitude shows cleared sites in the Cuban countryside with long shapes identified as missile transporters and launch equipment. Military analysts marked the installations visible in the frame.&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>C1. (2 points)</strong> What does the photograph show, and where and when was it taken? Answer from the caption and the description.</p><div class="sp-a"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>C2. (3 points)</strong> Explain why this discovery produced a thirteen day confrontation in October 1962, name the measure President Kennedy announced on October 22, and state how the confrontation was settled.</p><div class="sp-b"></div></div>')

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
        ("A1", 2, "Truman states that it must be the policy of the United States to support free peoples who are resisting attempted subjugation. The two kinds of pressure he names are armed minorities and outside pressures. One point for the policy stated in the source's words, one point for both pressures named."),
        ("A2", 2, "The help should be primarily through economic and financial aid, which Truman says is essential to economic stability and orderly political processes. The Marshall Plan carried the same idea to Western Europe from 1948 to 1952, giving about thirteen billion dollars in aid to rebuild Western European economies so that hunger and chaos could not deliver them to Communist parties. Full credit requires the kind of aid, Truman's stated reason, and the Marshall Plan connection."),
        ("B1", 3, "NSC-68 describes the Soviet Union as animated by a new fanatic faith, antithetical to the American faith, unlike previous aspirants to hegemony. It says the Soviet Union seeks to impose its absolute authority over the rest of the world. Both parts must come from the source for full credit."),
        ("B2", 3, "The paper calls for a more rapid build-up of political, economic, and military strength in the free world, and names that build-up the only course consistent with progress toward achieving the American purpose. The shocks of 1949, the Communist victory in China and the first Soviet atomic bomb, had set up the paper's argument, and the Korean War, which began weeks after it was written in April 1950, turned a paper shelved as too costly into policy, as American defense spending rose sharply to fight a limited war in Asia."),
        ("C1", 10, "The photograph is a grainy black and white aerial photograph taken from high altitude over Cuba on October 14, 1962. It shows cleared sites in the Cuban countryside with long shapes identified as missile transporters and launch equipment, with the installations marked by military analysts. The caption supplies the place and date and the description supplies what the frame shows."),
        ("C2", 10, "The sites were Soviet nuclear missile installations under construction ninety miles from Florida, able to strike much of the eastern United States with little warning, which is why Kennedy treated the discovery as an emergency. On October 22 he announced a naval quarantine of offensive weapons bound for Cuba. The confrontation lasted thirteen days and was settled when the Soviet Union withdrew the missiles for an American promise not to invade Cuba, with American Jupiter missiles secretly removed from Turkey months later. Full credit requires the reason, the quarantine, and both parts of the settlement, or the public part plus one accurate consequence such as the hotline or the Limited Test Ban Treaty."),
    ]
    for label, bp, ans in key3:
        counts[bp] += 1
        P.append(f"<p><strong>{label}.</strong> {ans} (Blueprint {bp})</p>")
    P.append("</div></body></html>")
    out = os.path.join(UNIT, "unit-test", "unit-test.html")
    open(out, "w").write("\n".join(P))
    print("coverage from printed tags:", dict(sorted(counts.items())))
    print("min per entry:", min(counts.values()), "entries covered:", len(counts))
    print("total items tagged:", sum(counts.values()))

if __name__ == "__main__":
    main()
