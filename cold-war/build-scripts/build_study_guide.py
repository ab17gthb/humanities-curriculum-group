#!/usr/bin/env python3
"""Build the Cold War review study guide from the verbatim
vocabulary in build-scripts/unit-spec.md, plus 24 review questions with a
full key and the arguments of the era. Mirrors the World War II study guide."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
UNIT = os.path.dirname(HERE)
SPEC = open(os.path.join(HERE, "unit-spec.md")).read()

LESSON_TITLES = {
    1: "Allies to Adversaries: Containment Takes Shape", 2: "The Cold War in Asia: China and Korea",
    3: "The Red Scare at Home", 4: "Brinkmanship and the Nuclear Shadow",
    5: "Cuba: Revolution and the Missile Crisis", 6: "Vietnam: The War Containment Built",
    7: "Détente, Human Rights, and the Evil Empire", 8: "The Wall Falls: The Cold War Ends",
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
    (1, "What did Kennan argue in the Long Telegram about the source of Soviet expansion and the answer to it?",
     "Kennan argued that Soviet expansion was driven by ideology and by a deep and instinctive Russian sense of insecurity, and that Soviet power was highly sensitive to the logic of force and withdrew when it met strong resistance. The answer he proposed was firm resistance that blocked further expansion, the policy Washington soon named containment, carried out chiefly by political and economic means rather than by direct war."),
    (1, "State the Truman Doctrine as Truman declared it in March 1947, and name the immediate request it framed.",
     "Truman declared that it must be the policy of the United States to support free peoples who are resisting attempted subjugation by armed minorities or by outside pressures, and that American help should be primarily economic and financial aid. The universal statement framed an immediate and specific request, aid to Greece and Turkey, whose governments Washington said were under Communist pressure in 1947."),
    (1, "How did the Berlin Blockade test containment, and how did the airlift answer it?",
     "In 1948 the Soviet Union closed the land routes to West Berlin, testing whether the Western allies would abandon a city deep inside the Soviet occupation zone. The United States and Britain supplied a city of about two million people by air for eleven months, in 1948 and 1949, until the blockade was lifted. The line held without a shot fired, and NATO followed in 1949 as the strategy took permanent military form."),
    (2, "What two shocks of 1949 set up NSC-68, and what did NSC-68 call for?",
     "The two shocks were the Communist victory in the Chinese civil war, proclaimed as the People's Republic of China on October 1, 1949, and the first Soviet atomic bomb test weeks earlier. NSC-68, the secret planning paper of April 1950, described the Cold War as a global struggle and called for a large buildup of American military strength. Shelved as too costly when written, it became policy when the Korean War began."),
    (2, "Trace the Korean War from the invasion of June 1950 to the Chinese intervention.",
     "North Korea invaded South Korea on June 25, 1950. President Truman committed American forces under the United Nations flag without a declaration of war, and after a retreat to the Pusan Perimeter, General MacArthur's landing at Inchon in September 1950 reversed the war. The drive north toward the Yalu River brought China into the war in November with hundreds of thousands of troops, drove the United Nations forces back, and settled the fighting near the 38th parallel."),
    (2, "Why did Truman dismiss MacArthur, and what did the armistice of 1953 settle and leave unsettled?",
     "MacArthur demanded a wider war against China and defied the president's policy in public, and Truman dismissed him in April 1951, defended as the price of civilian control of the military and of keeping a limited war limited. The armistice of July 1953 ended the shooting roughly where the war had begun, after more than 36,000 American dead and Korean dead in the millions. It settled no political question and signed no peace treaty, and Korea remains divided at the 38th parallel."),
    (3, "What fuel did the Second Red Scare have that was real?",
     "The scare ran on real events as well as fear. The Soviet atomic bomb of 1949 and the Communist victory in China the same year suggested a shifting balance, the Korean War from 1950 put Americans in combat against Communist forces, and Soviet espionage was real, including spies who passed atomic secrets to Moscow. The lesson's reckoning keeps the fuel and the machinery separate, because the existence of spies did not by itself prove the charges the machinery made against thousands of others."),
    (3, "How did the House Un-American Activities Committee's Hollywood hearings produce the blacklist?",
     "In its 1947 hearings on the film industry, the committee heard friendly witnesses name names and called unfriendly witnesses to answer whether they were Communists. The Hollywood Ten refused to answer, were cited for contempt of Congress, and went to prison. The studios then barred people suspected of Communist ties or of refusing to cooperate from employment, and the blacklist circulated through film and broadcasting for years, ending careers on suspicion and association rather than on proof in court."),
    (3, "What brought Senator McCarthy down in 1954?",
     "McCarthy had built a national campaign from 1950 on public accusations of Communist disloyalty without firm evidence, beginning with his Wheeling speech claim of Communists inside the State Department, a number that changed as he repeated it. In the Army-McCarthy hearings of 1954, televised for thirty six days and watched by millions, Americans saw the method at work against the Army itself. The Senate censured him that December, and his influence collapsed, though the wider scare's machinery outlasted him in places."),
    (4, "What were massive retaliation and brinkmanship as the Eisenhower administration described them?",
     "Massive retaliation was the declared policy of answering Communist aggression with the threat of a full nuclear strike, rather than matching force at the point of attack. Brinkmanship, as Secretary of State John Foster Dulles described the practice, was pushing a dangerous confrontation to the edge of war in order to force the other side to back down. Both doctrines rested on the hydrogen bomb, first tested by the United States in 1952 and by the Soviet Union in 1953, and both assumed the other side would step back first."),
    (4, "What did covert action do in Iran in 1953 and Guatemala in 1954, and what justification was given for it?",
     "The Central Intelligence Agency helped overthrow elected governments in Iran in 1953 and Guatemala in 1954, in secret operations meant to influence events abroad while hiding the sponsor's hand. The justification given was containment, that each government was opening its country to Communist influence. The operations were cheap and quick by the measure of the time, and the lesson records that they were answered by decades of consequences in both countries."),
    (4, "Why did Sputnik shock the United States, and what did the country build in answer?",
     "Sputnik, the first artificial satellite, launched by the Soviet Union in October 1957, was heard in the United States as proof the country had fallen behind in science, missiles, and education, because the rocket that orbited a satellite could in principle carry a warhead across an ocean. The answers included the National Aeronautics and Space Administration, new federal money for science education, and a missile program pressed into overdrive, opening the space race as a public test of the two systems."),
    (5, "How did Cuba move toward the Soviet Union between 1959 and 1961?",
     "Fidel Castro's revolution took power in Cuba on January 1, 1959, overthrowing the government of Fulgencio Batista. Land reform and the seizure of American property broke relations with Washington, and a trade deal with Moscow turned Cuba toward alliance with the Soviet Union. An island ninety miles from Florida aligned with the Soviet camp changed the map of the rivalry, which had until then kept Soviet military power an ocean away from the United States."),
    (5, "What did the failure of the Bay of Pigs invasion teach Castro and Khrushchev?",
     "The invasion of April 1961 landed Cuban exiles trained and supplied by the United States and was defeated on the beach within three days. The failure taught Castro that Washington would try again and that Cuba needed a stronger guarantee, which he sought from Moscow. It taught Khrushchev to read President Kennedy as young and open to pressure. Both lessons stand directly behind the decision to place Soviet nuclear missiles in Cuba the following year."),
    (5, "State the two parts of the Cuban Missile Crisis settlement, public and secret.",
     "The public part, announced in October 1962, was that the Soviet Union withdrew its missiles from Cuba in return for an American promise not to invade Cuba. The secret part, denied by both governments at the time, was that American Jupiter missiles were quietly removed from Turkey months later. The crisis that produced the settlement also produced its safeguards, the direct hotline between Washington and Moscow in 1963 and the Limited Test Ban Treaty the same year."),
    (6, "How did the domino theory and the Gulf of Tonkin Resolution together bring the United States into the ground war in Vietnam?",
     "The domino theory, stated publicly by President Eisenhower in 1954, held that if one country fell to communism its neighbors would fall one after another, which made South Vietnam a test the United States said it could not fail. The Gulf of Tonkin Resolution of August 1964, passed on reports of attacks on American destroyers, the second of which almost certainly never happened, gave the president authority to take all necessary measures in Southeast Asia. The belief supplied the reason and the resolution supplied the legal authority, and escalation followed from 1965."),
    (6, "Describe the escalation of the Vietnam War by 1968 in numbers and in methods.",
     "The American ground force grew step by step from advisers to more than half a million troops by 1968. The methods were the Rolling Thunder bombing campaign from 1965, search and destroy operations in the villages, and body counts offered as the measure of progress, while the draft fell hardest on the poor and the young. Official statements promised progress throughout, which is the gap the next question turns on, because the Tet Offensive broke public belief in those statements."),
    (6, "Why was the Tet Offensive a turning point although the attackers lost, and how did the war then end?",
     "In January 1968 North Vietnamese and Viet Cong forces attacked across South Vietnam, including the grounds of the American embassy in Saigon. The attacks were a military defeat for the attackers and a strategic defeat for the Johnson administration, because they showed a war official statements had described as being won could still open everywhere at once. President Nixon's Vietnamization withdrew American troops while widening the bombing into Cambodia and Laos, the Paris Peace Accords of January 1973 took the last American troops out, and Saigon fell on April 30, 1975."),
    (7, "What reasons did both sides have by 1969 to try détente?",
     "The Soviet Union had reached rough nuclear parity and had split with China, and the United States was bleeding in Vietnam and needed room to leave it. President Nixon and Henry Kissinger built détente as a structure of agreements, arms limits, trade, and summit meetings, that would give Moscow a stake in restraint. The opening to China in 1972 used one Communist power against the other, and SALT I the same year capped missile launchers for the first time."),
    (7, "What did the Helsinki Accords promise each side, and why did the human rights language matter afterward?",
     "Western nations recognized Europe's postwar borders in 1975, which was the settlement Moscow had sought since 1945. In return the Soviet Union and its allies pledged respect for human rights. Soviet and East European dissidents then quoted the pledge back to their own governments, using a document signed for diplomatic advantage as a legal and moral claim at home. The Accords were a slow fuse inside the settlement they appeared to freeze."),
    (7, "How did the confrontation return between 1979 and 1983?",
     "The Soviet invasion of Afghanistan in December 1979 ended the bargain of the 1970s, bringing an American grain embargo, a boycott of the Moscow Olympics, and the death of SALT II in the Senate. President Reagan, elected on the charge that America had grown weak, ordered a defense buildup, aided anti-Communist insurgencies under the Reagan Doctrine, named the Soviet Union the focus of evil in the modern world in his March 1983 Evil Empire speech, and announced the Strategic Defense Initiative the same month."),
    (8, "What were glasnost and perestroika meant to do, and what did each one loosen?",
     "Mikhail Gorbachev, who took power in 1985 over a stagnating Soviet economy, meant glasnost, openness, to let Soviet citizens discuss and criticize what had failed, and perestroika, restructuring, to make the economy and political system work. Glasnost loosened the party's control of public speech and of the Soviet past, and perestroika loosened its control of the economy and of the republics. Reform meant to save the system ended by loosening the party's control of both speech and power."),
    (8, "Trace the year 1989 from Poland to the night of November 9 in Berlin.",
     "Poland voted the Solidarity movement into government in 1989, Hungary opened its border and let East Germans leave through it, and crowds in Leipzig grew by the week. On November 9, 1989 an East German spokesman garbled a travel announcement on live television, crowds gathered at the Berlin Wall, and Berliners climbed it with hammers while the guards stood aside. The step that made the rest possible was Gorbachev's refusal, all that autumn, to use the Soviet army to hold Eastern Europe by force."),
    (8, "How did the Cold War end between 1990 and December 1991, and what did the ending leave open?",
     "East and West Germany joined in one state inside NATO in October 1990, the Warsaw Pact dissolved, and the Baltic states recovered their independence. A failed hard line coup in August 1991 broke the Communist Party's remaining authority, Ukraine voted to leave the union, and on December 25, 1991 Gorbachev resigned an office whose country no longer existed, as the Soviet Union dissolved and its republics declared independence. The ending left the United States the world's only superpower over a map of new states, old nuclear weapons, and questions no settlement had answered."),
]

ARGUMENTS = [
    ("Containment and its costs", "The unit's through line is a strategy. Read Kennan's way in 1946 and 1947, containment was chiefly political and economic, firm resistance at the points of Soviet pressure, aid that kept free peoples from being subjugated, and patience. Events made it military and global, in NSC-68's call for a worldwide buildup, in Korea as its first shooting application, and in Vietnam as the war it built and the failure it could not escape. Judging containment means judging both versions from the same documents, the strategy as argued and the strategy as applied."),
    ("Fear at home", "The Second Red Scare had real fuel, a Soviet bomb, a Communist China, a war in Korea, and genuine espionage, and the machinery built to answer it still punished association as if it were proof. Loyalty oaths, committee hearings, and blacklists cost thousands of people their work, and the scare fell not when the fuel ran out but when television showed the method to the country and the Senate censured its leading practitioner. The unit keeps the fuel and the machinery in the same lesson so neither can be used to excuse the other."),
    ("Living under the arsenals", "From 1952 both superpowers held weapons able to destroy the other's society in an afternoon, and the doctrines built on them, massive retaliation, brinkmanship, and deterrence, promised safety by threatening destruction. The record includes the days the system nearly failed, October 1962 above all, and the partial answers the failures produced, a hotline, a test ban, and negotiated arms limits. The arms race is therefore taught as a condition Americans lived inside, in school drills and fallout shelters, and not only as a contest between governments."),
    ("An ending no one predicted", "The Cold War ended without the direct war both sides had armed against for forty five years, and it ended quickly, between the Berlin Wall's breach in November 1989 and the dissolution of the Soviet Union in December 1991. The documents give the causes in combination, a reformer who loosened his own system and refused to hold it by force, crowds who tested that refusal, and a state whose economy and legitimacy had run out. The last lesson leaves the weighting of those causes to the evidence, because historians still argue it from the same record."),
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
    total = sum(len(v) for v in terms.values())
    assert total == 56, f"expected 56 terms, parsed {total}"
    P = []
    P.append("<!DOCTYPE html>")
    P.append('<html lang="en"><head><meta charset="utf-8">')
    P.append("<title>Study Guide: The Cold War</title>")
    P.append(f"<style>{CSS}</style></head><body>")
    P.append('<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>')
    P.append('<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>')
    P.append("<h1>Study Guide: The Cold War</h1>")
    P.append('<p class="directions"><strong>Directions:</strong> Complete Part 1 from your guided notes and readings, then answer the Part 2 questions in your own words. Part 3 summarizes the arguments that run through the whole unit. The unit test is built from this guide. Bring questions about anything you cannot answer to the review day.</p>')
    P.append("<p><strong>Unit question:</strong> How did the struggle between the United States and the Soviet Union reshape the world and American life, and why did it end the way it did?</p>")
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
