#!/usr/bin/env python3
"""Build the Civil Rights unit test (50 points) in the established test
format: matching 15, multiple choice 20, source-based 15, with every
item tagged to the blueprint in the key. Coverage is recomputed from
the tags this script prints. Sources are quoted verbatim from the
audited TPSP bank records in civil-rights.json, with cuts marked and
the edition named in each Source line. The Scherman photograph is
presented from the bank record's description and is not reproduced.
No text from the Letter from Birmingham Jail, the I Have a Dream
address, or The Ballot or the Bullet is quoted anywhere in this test.
"""
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
    ("Jim Crow", 1, "the system of state and local laws and customs that enforced racial segregation in the South"),
    ("Executive Order 9981", 2, "President Truman's order of July 26, 1948 directing equality of treatment and opportunity for all persons in the armed forces, the order that desegregated the United States military"),
    ("Brown v. Board of Education", 3, "the Supreme Court decision of May 17, 1954 that declared segregation in public schools unconstitutional, ruling that separate educational facilities are inherently unequal"),
    ("Southern Manifesto", 4, "the declaration of 1956 signed by 101 southern members of Congress denouncing Brown v. Board of Education as an abuse of judicial power and pledging to resist it"),
    ("Montgomery bus boycott", 5, "the protest of 1955 and 1956 in which Black residents of Montgomery, Alabama refused to ride the city's buses for 381 days, ending when the Supreme Court ordered the buses desegregated"),
    ("Little Rock Nine", 6, "the nine Black students who desegregated Central High School in Little Rock, Arkansas in 1957 under the protection of federal troops after the state's governor tried to bar their entry"),
    ("Student Nonviolent Coordinating Committee", 7, "the organization founded by student activists in April 1960, known as SNCC, which organized sit-ins, Freedom Rides, and voter registration drives in the deepest parts of the South"),
    ("Freedom Rides", 8, "the bus journeys of 1961 in which interracial groups of activists rode through the South to test court orders desegregating interstate bus travel and bus terminals"),
    ("Birmingham campaign", 9, "the protest campaign of 1963 in Birmingham, Alabama, led by the Southern Christian Leadership Conference and the local movement, whose televised repression pushed President Kennedy to propose a national civil rights bill"),
    ("March on Washington", 10, "the demonstration of August 28, 1963 that brought about 250,000 people to the Lincoln Memorial to demand jobs and freedom and to press Congress to pass the civil rights bill"),
    ("Civil Rights Act of 1964", 11, "the federal law that banned discrimination in public accommodations and employment and allowed the government to cut off funds to segregated programs, the movement's first great legislative victory"),
    ("Voting Rights Act of 1965", 12, "the federal law that suspended literacy tests, sent federal examiners to register voters in covered states, and required those states to clear any change in voting rules with the federal government first"),
    ("de facto segregation", 13, "segregation in fact rather than in law, produced by housing patterns, economics, and custom, the form segregation took in the cities of the North"),
    ("Black Power", 14, "the call raised by Stokely Carmichael in Mississippi in June 1966 for Black Americans to build their own political and economic power and to define freedom for themselves rather than rely on white goodwill"),
    ("Fair Housing Act", 15, "the Civil Rights Act of 1968, passed in the week after Martin Luther King Jr.'s assassination, banning discrimination in the sale and rental of most housing"),
]
# letter order for descriptions (index into MATCH shuffled by hand)
ORDER = [4, 12, 1, 9, 6, 14, 2, 10, 0, 7, 13, 3, 11, 5, 8]

# (question, options[4], correct index, blueprint entry)
MC = [
    ("Under Jim Crow, Black southerners were kept from voting chiefly by",
     ["a federal law barring Black voters in every state",
      "poll taxes, literacy tests, white primaries, and violence",
      "a constitutional amendment passed in 1896",
      "the decisions of the Warren Court"], 1, 1),
    ("To Secure These Rights, the 1947 report of President Truman's Committee on Civil Rights, called for",
     ["federal laws against lynching and disfranchisement and the end of segregation in American life",
      "the armed forces to remain segregated",
      "school desegregation to wait for state action",
      "the NAACP to end its court campaign"], 0, 2),
    ("Charles Hamilton Houston's legal strategy attacked segregation first in",
     ["elementary schools in the largest southern cities",
      "interstate bus terminals",
      "graduate and professional schools, where it was most visibly unequal, winning Sweatt and McLaurin in 1950",
      "the United States Senate"], 2, 3),
    ("Brown II, decided in 1955, ordered school desegregation to proceed",
     ["within thirty days in every district",
      "only in the four states named in Brown",
      "with federal troops in every school",
      "with all deliberate speed, a phrase with no deadline in it that southern officials used to justify years of delay"], 3, 4),
    ("The Montgomery bus boycott of 1955 and 1956 ended when",
     ["the city council voted to raise bus fares",
      "the Supreme Court, in Browder v. Gayle, ordered the city's buses desegregated",
      "the governor of Alabama intervened",
      "the boycotters accepted segregated seating"], 1, 5),
    ("President Eisenhower sent federal troops to Little Rock in 1957 chiefly because",
     ["he had written the Brown decision",
      "the city's mayor asked him to close the schools",
      "Governor Faubus was defying a federal court order, and Eisenhower held that no governor could be allowed to do so",
      "the Little Rock Nine asked to leave Central High School"], 2, 6),
    ("The Nashville student sit-ins of 1960 were prepared by",
     ["training in nonviolence workshops led by James Lawson",
      "the Montgomery Improvement Association",
      "a federal court order opening the lunch counters",
      "the staff of the NAACP's national office"], 0, 7),
    ("The Albany Movement of 1961 and 1962 taught the movement that protest could fail when",
     ["students refused to take part",
      "the press covered the campaign too closely",
      "television cameras were banned from the city",
      "a police chief answered with polite mass arrests and denied the movement a televised crisis that moved federal power"], 3, 8),
    ("The Children's Crusade of May 1963 in Birmingham sent",
     ["college students to register voters in Mississippi",
      "thousands of Black schoolchildren into the streets, where they were met with fire hoses, police dogs, and jail",
      "marchers from Selma to Montgomery",
      "delegates to the Democratic National Convention"], 1, 9),
    ("The March on Washington of August 28, 1963 brought about 250,000 people to the Lincoln Memorial to",
     ["demand jobs and freedom and press Congress to pass the civil rights bill",
      "protest the Vietnam War",
      "nominate a presidential candidate",
      "celebrate the passage of the Voting Rights Act"], 0, 10),
    ("The southern filibuster against the civil rights bill of 1964 was broken when",
     ["President Johnson addressed a joint session of Congress",
      "the House of Representatives voted in February 1964",
      "the Senate voted for cloture after more than two months of debate, closing debate on a civil rights bill for the first time in the century",
      "the Supreme Court ordered the Senate to vote"], 2, 11),
    ("Bloody Sunday, March 7, 1965, was the attack by Alabama state troopers and a sheriff's posse on",
     ["Freedom Riders at a bus station in Montgomery",
      "voting rights marchers at the Edmund Pettus Bridge in Selma, televised to the nation that evening",
      "students sitting in at a Greensboro lunch counter",
      "marchers entering Chicago on an open housing march"], 1, 12),
    ("De facto segregation in the northern cities was produced chiefly by",
     ["statutes requiring separate schools by race",
      "the decisions of southern state legislatures",
      "housing patterns, economics, and custom, rather than by law",
      "Executive Order 10730"], 2, 13),
    ("Stokely Carmichael raised the call of Black Power in June 1966",
     ["at the March on Washington",
      "in Oakland, at the founding of the Black Panther Party",
      "from a jail cell in Birmingham",
      "on the Meredith March in Mississippi, calling on Black Americans to build their own political and economic power"], 3, 14),
    ("The Bakke decision of 1978 held that",
     ["a set aside of seats by race in admissions was struck down, and race could be used as one factor among others",
      "affirmative action was ended in every program",
      "busing could no longer be ordered by any court",
      "the Fair Housing Act was unconstitutional"], 0, 15),
    ("Executive Order 9981, issued by President Truman on July 26, 1948, directed",
     ["the desegregation of public schools in the District of Columbia",
      "equality of treatment and opportunity for all persons in the armed forces",
      "federal examiners to register voters in the South",
      "the end of the poll tax in federal elections"], 1, 2),
    ("Cooper v. Aaron, decided in 1958 and arising from Little Rock, held that",
     ["states could close public schools rather than desegregate them",
      "Brown applied only to the states named in the case",
      "governors could suspend federal court orders in an emergency",
      "state officials are bound by the Court's interpretation of the Constitution and cannot nullify its rulings"], 3, 4),
    ("The March on Washington was organized chiefly by",
     ["Bayard Rustin and A. Philip Randolph, who had threatened a march on Washington a generation earlier, in 1941",
      "the Southern Christian Leadership Conference alone",
      "the Kennedy administration",
      "the Student Nonviolent Coordinating Committee alone"], 0, 10),
    ("The Voting Rights Act of 1965 worked by suspending literacy tests and",
     ["ordering states to redraw their congressional districts",
      "sending federal examiners to register voters in covered states and requiring those states to clear any change in voting rules with the federal government first",
      "lowering the voting age to eighteen",
      "banning the poll tax in state elections"], 1, 12),
    ("In Swann in 1971, the Supreme Court",
     ["struck down the Civil Rights Act of 1968",
      "ended court ordered desegregation everywhere",
      "upheld busing to desegregate Charlotte's schools",
      "allowed Detroit's desegregation to cross into the suburbs"], 2, 15),
]

def main():
    P = []
    P.append("<!DOCTYPE html>")
    P.append('<html lang="en"><head><meta charset="utf-8">')
    P.append("<title>Unit Test: The Civil Rights Movement</title>")
    P.append(f"<style>{CSS}</style></head><body>")
    P.append('<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>')
    P.append('<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>')
    P.append("<h1>Unit Test: The Civil Rights Movement</h1>")
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
    P.append("<p>U.S. Supreme Court, Brown v. Board of Education, May 17, 1954. From U.S. Supreme Court, 'Brown v. Board of Education,' 1954 (Justia transcription of U.S. Reports, 347 U.S. 483). Cuts are marked with ellipses in brackets.</p>")
    P.append("<p>&ldquo;To separate them from others of similar age and qualifications solely because of their race generates a feeling of inferiority as to their status in the community that may affect their hearts and minds in a way unlikely ever to be undone. [...] We conclude that, in the field of public education, the doctrine of &ldquo;separate but equal&rdquo; has no place. Separate educational facilities are inherently unequal. Therefore, we hold that the plaintiffs and others similarly situated for whom the actions have been brought are, by reason of the segregation complained of, deprived of the equal protection of the laws guaranteed by the Fourteenth Amendment.&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>A1. (2 points)</strong> According to the Court, what does separating children from others of similar age and qualifications solely because of their race generate, and what may that feeling affect?</p><div class="sp-a"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>A2. (3 points)</strong> State the Court\'s conclusion about the doctrine of separate but equal in the field of public education, name the amendment the plaintiffs were held to be deprived of protection under, and explain why the conclusion held even where the physical facilities of the separate schools might be equal.</p><div class="sp-b"></div></div>')
    P.append('<div class="source"><p class="srclabel">Source B</p>')
    P.append("<p>U.S. Congress, Civil Rights Act of 1964, signed July 2, 1964. From U.S. Congress, 'Civil Rights Act of 1964,' 1964 (Statutes at Large, verified via GovInfo). Cuts are marked with ellipses in brackets.</p>")
    P.append("<p>Title II, Section 201. &ldquo;(a) All persons shall be entitled to the full and equal enjoyment of the goods, services, facilities, privileges, advantages, and accommodations of any place of public accommodation, as defined in this section, without discrimination or segregation on the ground of race, color, religion, or national origin.&rdquo; [...] Title VI, Section 601. &ldquo;No person in the United States shall, on the ground of race, color, or national origin, be excluded from participation in, be denied the benefits of, or be subjected to discrimination under any program or activity receiving Federal financial assistance.&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>B1. (2 points)</strong> Under Title II, what are all persons entitled to, and on what four grounds may they not be discriminated against or segregated in a place of public accommodation?</p><div class="sp-a"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>B2. (3 points)</strong> State the Title VI rule for programs receiving federal financial assistance, and explain what power that rule gave the federal government over a segregated program, naming the consequence the act allowed.</p><div class="sp-b"></div></div>')
    P.append('<div class="source"><p class="srclabel">Source C</p>')
    P.append("<p>U.S. Information Agency (photographer Rowland Scherman), March on Washington photograph, August 28, 1963. From U.S. Information Agency (photographer Rowland Scherman), 'March on Washington: Edith Lee-Payne,' August 28, 1963 (National Archives; image described, banner caption transcribed). The bank record describes the photograph rather than reproducing it, and this test presents the photograph from that description. The photograph itself is not reproduced here. The United States Information Agency sent photographers to document the March on Washington for audiences abroad.</p>")
    P.append("<p>The bank record describes the image in these words: &ldquo;A young Black girl, Edith Lee-Payne of Detroit, holds a banner reading &ldquo;MARCH FOR JOBS AND FREEDOM / AUGUST 28&rdquo; at the March on Washington, August 28, 1963. She had just turned twelve that day and attended the march with her mother. She had no idea she had been photographed until years later, when a cousin spotted the image in a calendar of African American history.&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>C1. (2 points)</strong> Who appears in the photograph, what does her banner read, and what two facts does the description give about her age and her knowledge of being photographed?</p><div class="sp-a"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>C2. (3 points)</strong> Explain how this photograph served the movement\'s public case on August 28, 1963, and explain why the identity of the agency that sent the photographer, and the audience it worked for, must shape how a historian reads the image as evidence.</p><div class="sp-b"></div></div>')

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
        ("A1", 3, "The Court states that separating children from others of similar age and qualifications solely because of their race generates a feeling of inferiority as to their status in the community. That feeling, the Court says, may affect their hearts and minds in a way unlikely ever to be undone. One point for the feeling named in the source's words, one point for the effect the source states."),
        ("A2", 3, "The Court concludes that in the field of public education the doctrine of separate but equal has no place, because separate educational facilities are inherently unequal. The plaintiffs were held to be deprived of the equal protection of the laws guaranteed by the Fourteenth Amendment. The conclusion held even where tangible factors such as buildings and curricula had been equalized, because the harm the opinion identifies is the effect of segregation itself on the children, not a comparison of facilities. Full credit requires the conclusion, the amendment, and that reasoning."),
        ("B1", 11, "Title II entitles all persons to the full and equal enjoyment of the goods, services, facilities, privileges, advantages, and accommodations of any place of public accommodation. The four grounds named are race, color, religion, and national origin. One point for the entitlement and one point for all four grounds."),
        ("B2", 11, "Title VI provides that no person in the United States shall, on the ground of race, color, or national origin, be excluded from participation in, be denied the benefits of, or be subjected to discrimination under any program or activity receiving federal financial assistance. The rule gave the federal government a funding lever over segregated programs. As the act is defined in the unit's vocabulary, the government could cut off funds to segregated programs, so a school, hospital, or agency that took federal money risked losing it by discriminating. Full credit requires the rule stated from the source and the funding consequence named."),
        ("C1", 10, "The photograph shows Edith Lee-Payne of Detroit, a young Black girl holding a banner reading MARCH FOR JOBS AND FREEDOM / AUGUST 28 at the March on Washington on August 28, 1963. The description states that she had just turned twelve that day and that she had no idea she had been photographed until years later, when a cousin spotted the image in a calendar of African American history. One point for the subject and the banner, one point for both facts."),
        ("C2", 10, "The photograph put a single child's face on a demonstration of about 250,000 people who came to the Lincoln Memorial to demand jobs and freedom and to press Congress to pass the civil rights bill, which is the movement's public case stated in one frame, orderly, young, and carrying its demands in plain words. A historian must also weigh its making. Rowland Scherman was sent by the United States Information Agency, the government's overseas storytelling service, to document the march for audiences abroad, so the image was framed by a federal agency with an interest in showing a peaceful and hopeful America during the Cold War. That purpose does not make the photograph false. It means the image is evidence both of the march and of what the government wanted the world to see of it. Full credit requires the march's demands, the agency and its audience, and that double reading."),
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
