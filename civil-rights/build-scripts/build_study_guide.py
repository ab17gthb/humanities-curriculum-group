#!/usr/bin/env python3
"""Build the Civil Rights review study guide from the verbatim
vocabulary in build-scripts/unit-spec.md, plus 24 review questions with a
full key and the arguments of the era. Mirrors the Cold War study guide."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
UNIT = os.path.dirname(HERE)
SPEC = open(os.path.join(HERE, "unit-spec.md")).read()

LESSON_TITLES = {
    1: "Foundations: The Movement Before the Movement", 2: "Brown and the Massive Resistance",
    3: "Montgomery and Little Rock: The Movement Finds Its Tactics", 4: "Sit-Ins and Freedom Rides: The Students Take the Lead",
    5: "Birmingham and the March on Washington", 6: "The Laws Change: 1964 and 1965",
    7: "The Movement Turns North and Inward: Chicago, Black Power, Memphis", 8: "Victory, Backlash, and the Unfinished Agenda",
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
    (1, "What did the Jim Crow system do, and by what tools did it keep Black southerners from voting?",
     "Jim Crow was the system of state and local laws and customs that enforced racial segregation in the South, in schools, transport, and public life, a settlement the Supreme Court had blessed in Plessy v. Ferguson in 1896. Disfranchisement worked through the poll tax, the literacy test, and the white primary, the Democratic primary from which Black voters were barred, and behind the paper tools stood violence against anyone who tried to register or vote. The system held because law and custom enforced each other."),
    (1, "What institutions had Black Americans built under Jim Crow, and what had the NAACP already won before 1954?",
     "The institutions the system could not close were the Black church, the Black college, and the Black press, and standing over them the NAACP, founded in 1909, which had been fighting segregation in the courts for decades. Its lawyers had already won cases against the white primary and against restrictive covenants that barred Black buyers from housing. The famous decade of the movement rested on organizations, money, and legal skill built long before it began."),
    (1, "What did the Second World War leave the movement, and what were the first federal steps of 1947 and 1948?",
     "The war left a million Black servicemen, the Double V campaign's demand for victory over fascism abroad and racism at home, Executive Order 8802's fair employment precedent, and the Great Migration's second wave moving Black voters into northern cities where their ballots counted in national elections. President Truman's Committee on Civil Rights reported in 1947 in To Secure These Rights, naming lynching, disfranchisement, and segregation as federal business. His 1948 civil rights message split his party and sent the Dixiecrats out of the convention, and Executive Order 9981 of July 26, 1948 ordered equality of treatment in the armed forces."),
    (2, "How did Charles Hamilton Houston and Thurgood Marshall plan the NAACP's attack on school segregation?",
     "Houston's plan attacked segregation where it was most visibly unequal, in graduate and professional schools first, where states had built almost nothing for Black students. The strategy won Sweatt and McLaurin in 1950 without asking the Court to overturn Plessy outright. Marshall then carried the campaign to the elementary schools themselves, arguing that segregation was unequal in itself and not only in its buildings and books."),
    (2, "What did the Supreme Court hold in Brown v. Board of Education on May 17, 1954?",
     "Five cases from Kansas, South Carolina, Virginia, and Delaware were joined under the Kansas case, and a unanimous Warren Court held that segregation in public schools violated the Fourteenth Amendment. The opinion declared that separate educational facilities are inherently unequal, because separating children by race stamps them with a badge of inferiority whatever the facilities. The decision ended the legal standing of separate but equal in public education, the doctrine Plessy had set in 1896."),
    (2, "How did the South answer Brown, and what did the Court answer in Cooper v. Aaron?",
     "Brown II in 1955 ordered desegregation with all deliberate speed, a phrase with no deadline in it, and southern officials read it as permission to wait. The organized answer was massive resistance, pupil placement laws, private school schemes, and whole districts closing their public schools, Prince Edward County in Virginia first among them, while the Southern Manifesto of 1956, signed by 101 members of Congress, called the decision an abuse of judicial power. Cooper v. Aaron in 1958, arising from Little Rock, held that state officials are bound by the Court's reading of the Constitution and that no governor or legislature may nullify it. Ten years after Brown, barely one Black child in a hundred in the deep South attended school with white children."),
    (3, "How did the Montgomery bus boycott work, and how did it end?",
     "Jo Ann Robinson's letter of May 1954 had warned Montgomery's mayor that a boycott was coming. After Rosa Parks was arrested on December 1, 1955, the Women's Political Council spread leaflets overnight, and the Montgomery Improvement Association, led by a twenty six year old pastor, Martin Luther King Jr., sustained the boycott for 381 days through carpools, church networks, mass meetings, arrests, and a bombed house. It ended when the Supreme Court, in Browder v. Gayle, ordered the city's buses desegregated. Its method joined economic pressure, an institution of the movement's own to run the campaign, a moral claim stated in the language of the Constitution and the church, and cameras watching."),
    (3, "Who was Emmett Till, and how did his mother's decision change what the nation knew?",
     "Emmett Till was fourteen, visiting Mississippi from Chicago in August 1955, when he was murdered after being accused of offending a white woman. An all white jury acquitted his killers in about an hour, and the men then confessed to a magazine for money, protected from a second trial. Mamie Till-Mobley held an open casket funeral in Chicago and let Jet magazine publish the photographs, so tens of thousands of mourners filed past her son's body and the nation saw what the jury had excused. The photographs are copyrighted magazine images. This unit teaches the record as the bank carries it, described and not reproduced, and says so in the student materials."),
    (3, "Why did President Eisenhower send federal troops to Little Rock in 1957?",
     "Governor Orval Faubus posted the Arkansas National Guard to bar nine Black students from Central High School, and a mob turned Elizabeth Eckford away alone before the cameras. Eisenhower had never endorsed Brown, but he decided a governor's defiance of a federal court order was the one thing he could not let stand. His Executive Order 10730 of September 24, 1957 federalized the Arkansas Guard and sent the 101st Airborne, and the Little Rock Nine attended school that year under the protection of soldiers. Faubus then closed Little Rock's high schools entirely for the 1958 and 1959 school year, remembered as the Lost Year."),
    (4, "How did the sit-ins begin in 1960, and what happened in Nashville?",
     "On February 1, 1960 four freshmen at North Carolina A and T sat down at a segregated Woolworth lunch counter in Greensboro, were refused service, and returned with more students each day, and within weeks the tactic ran through the South. Nashville's students, trained in nonviolence workshops by James Lawson, sat in, were beaten and arrested, and filled the jails rather than posting bail. When Diane Nash asked Nashville's mayor on the courthouse steps whether he believed it was wrong to discriminate against a person by the color of his skin, his answer opened the city's lunch counters."),
    (4, "What organization did the student movement create in April 1960, and what did it commit itself to?",
     "The Student Nonviolent Coordinating Committee, known as SNCC, was founded at Shaw University in April 1960 under Ella Baker's guidance. Baker pressed the students to build an organization of local leadership rather than a following for national leaders. SNCC committed itself to staying in the hardest places in the deepest South, organizing sit-ins, Freedom Rides, and voter registration drives county by county."),
    (4, "What did the Freedom Rides test in 1961, and what lesson did Albany teach the movement afterward?",
     "CORE's Freedom Rides sent interracial teams into the deep South to test the court order desegregating interstate bus terminals. A bus was burned at Anniston and riders were beaten in Birmingham and Montgomery and arrested in Jackson and sent to Parchman prison, and that fall the Interstate Commerce Commission ordered the terminals desegregated. In Albany, Georgia, in 1961 and 1962, Police Chief Laurie Pritchett answered protest with polite mass arrests, no violence for the cameras, and jail space borrowed from every county around, and King left without a victory. The students carried the lesson forward. Protest worked when it created a crisis the federal government could not ignore, and Albany showed what happened when it did not."),
    (5, "Why was Birmingham chosen for the campaign of 1963, and what did the Children's Crusade do?",
     "Birmingham was the most segregated city in America, and the SCLC and Fred Shuttlesworth's local movement aimed Project C, for confrontation, at Commissioner Bull Connor's police in the spring of 1963. When the adult campaign stalled, James Bevel's Children's Crusade of May 1963 sent thousands of schoolchildren into the streets, and Connor answered with fire hoses and police dogs before the television cameras. Birmingham's businessmen settled within the week, and the images moved national opinion and the president."),
    (5, "What did Martin Luther King Jr. argue in his Letter from Birmingham Jail, stated in summary?",
     "King, arrested on Good Friday 1963, wrote the letter to answer eight white clergymen who had called his protests unwise and untimely. In summary, and in paraphrase rather than in his words, he argued that a community's injustice could not be sealed off from the rest of the country, that a law degrading human personality was not entitled to obedience, that freedom was never handed over by those who held power without demand, and that the white moderate who preferred quiet order to justice was a greater obstacle than the open segregationist. The letter's text is under copyright, and this unit quotes it only within a counted allowance in Lesson 5 and paraphrases it elsewhere, as here."),
    (5, "What did President Kennedy do in June 1963, what did the March on Washington demand that August, and what answered the march in September?",
     "After Birmingham, Kennedy addressed the nation on June 11, 1963, calling civil rights a moral issue and announcing he would send Congress a comprehensive civil rights bill. The same night, Medgar Evers was murdered in his driveway in Jackson, Mississippi. On August 28, 1963 about 250,000 people gathered at the Lincoln Memorial for the March on Washington for jobs and freedom, organized by Bayard Rustin and A. Philip Randolph, and King closed the day with the address that cast the movement's demands as a claim on the promises of the Declaration of Independence and the Constitution. Eighteen days later, on September 15, a bomb at Birmingham's 16th Street Baptist Church killed four girls, Addie Mae Collins, Cynthia Wesley, Carole Robertson, and Carol Denise McNair."),
    (6, "How was the Civil Rights Act of 1964 passed, and what did it reach?",
     "Kennedy's bill stalled, and after his death President Johnson staked his presidency on passing it whole. The House voted in February 1964, and the southern filibuster ran sixty working days in the Senate until two thirds of the Senate voted cloture, closing debate on a civil rights bill for the first time in the century. Signed on July 2, 1964, the act banned discrimination in public accommodations and in employment, in Title VII, and let the government cut off funds to segregated programs receiving federal money."),
    (6, "What happened during Freedom Summer in 1964, and what did the Mississippi Freedom Democratic Party do at Atlantic City?",
     "Freedom Summer brought about a thousand mostly northern student volunteers to Mississippi to register Black voters and run Freedom Schools. In June, three workers, James Chaney, Andrew Goodman, and Michael Schwerner, were murdered. That August the Mississippi Freedom Democratic Party, an integrated party organized in the state, challenged the seating of Mississippi's all white regular delegation at the Democratic National Convention, and Fannie Lou Hamer testified to the credentials committee on national television. The party was offered two seats as a compromise and refused them."),
    (6, "What happened at Selma in the winter of 1965, and what did the Voting Rights Act do?",
     "In Selma, where Sheriff Jim Clark's county had registered almost no Black voters though Black residents were half its population, Jimmie Lee Jackson was killed in Marion during the campaign. On Bloody Sunday, March 7, 1965, state troopers and a sheriff's posse attacked marchers at the Edmund Pettus Bridge before the television cameras, fracturing John Lewis's skull. Johnson answered on March 15 in an address to Congress asking for the voting bill as a matter of the American promise, and the march to Montgomery was then completed under federal protection. The Voting Rights Act of August 6, 1965 suspended literacy tests, sent federal examiners to register voters, and required covered states to clear any change in voting rules with the federal government first. A quarter of a million new Black voters were registered by the end of 1965, and Mississippi's Black registration rose from under seven percent toward sixty in three years."),
    (7, "Why did the movement's southern methods stop working in the North, and what happened in Chicago in 1966?",
     "Five days after the Voting Rights Act was signed, Watts in Los Angeles burned for six days in August 1965 and thirty four people died, a warning that the movement's southern legal targets were not the whole of American racism. Northern segregation was de facto, segregation in fact rather than in law, built from housing covenants, redlining, white flight, and school lines drawn around neighborhoods, so there was no single statute to strike down. King took the movement to Chicago in 1966, rented a tenement flat, and marched into Marquette Park, where mobs carried swastikas and threw bricks, one of which struck him. The campaign ended with a Summit Agreement on open housing that the city did not enforce."),
    (7, "What did Black Power mean when Stokely Carmichael raised the call in 1966, and where did Malcolm X stand in the argument?",
     "On the Meredith March in Mississippi in June 1966, Carmichael, jailed for the twenty seventh time, raised the call of Black Power, meaning that Black Americans should build their own political and economic power and define freedom for themselves rather than rely on white goodwill. SNCC and CORE moved toward Black leadership and away from the interracial liberal coalition, and King refused the slogan while understanding its source in a decade of nonviolence answered with bombs and acquittals. Malcolm X stood behind the argument as its earlier voice. Assassinated in February 1965 after breaking with the Nation of Islam, he had argued in The Ballot or the Bullet and in his other speeches and his Autobiography, paraphrased here because those texts are under copyright, that Black Americans should control the politics and economy of their own communities, defend themselves when government would not, and not make integration into an unjust order the measure of freedom."),
    (7, "Who were the Black Panthers, what was King's last campaign, and what happened in Memphis in 1968?",
     "Huey Newton and Bobby Seale founded the Black Panther Party in Oakland in October 1966. The Panthers patrolled the police carrying law books and rifles and then built free breakfast programs and health clinics, which the FBI worked to destroy. King's last campaign was the Poor People's Campaign, an interracial army of the poor to camp in Washington and demand an economic bill of rights. In Memphis, Black sanitation workers struck from February 1968 under signs reading I Am a Man, and King came to support them, returned after a march broke into violence, and spoke on April 3 determined to prove a peaceful march possible. He was shot on the balcony of the Lorraine Motel on April 4, 1968, and uprisings followed in more than a hundred cities."),
    (8, "What did the Fair Housing Act do, and what verdict did the Kerner Commission deliver in 1968?",
     "In the week after King's assassination, with Washington still marked by the uprisings, Congress passed the Fair Housing Act, the Civil Rights Act of 1968, banning discrimination in the sale and rental of most housing. It was the third great act, and the one whose enforcement was written weakest. The Kerner Commission, appointed by President Johnson to explain the uprisings, reported that white racism had built the ghetto and that the nation was moving toward two societies, one black, one white, separate and unequal. The president who commissioned the report could not accept its verdict, and its recommendations were shelved."),
    (8, "What did the movement win in public office, and how did the backlash and the courts answer it in the decade after?",
     "Black elected officials rose from a few hundred in 1965 toward five thousand by 1970 and beyond, with Black mayors in Cleveland and Gary and then Atlanta and Detroit, and the Congressional Black Caucus was founded in 1971. In parallel, George Wallace's campaigns carried five states in 1968, and a national politics of law and order and a southern strategy courted white voters who felt the movement had gone too far. The courts became contested ground. Swann in 1971 upheld busing to desegregate Charlotte's schools, and Milliken in 1974 stopped Detroit's desegregation at the city line, so schools could resegregate inside metropolitan borders the law would not cross."),
    (8, "How did the argument over affirmative action run from 1965 to the Bakke decision of 1978, and what is the unit's closing verdict?",
     "President Johnson had posed the question at Howard University in 1965, whether formal equality was enough after centuries of discrimination. Affirmative action followed in government policy, from the revised Philadelphia Plan of 1969, which set goals for federal contractors, to Bakke in 1978, where the Supreme Court struck down a medical school's set aside of seats by race and allowed race to stand as one factor among others in admissions. The closing verdict the documents support is double. In a decade the movement destroyed a legal system of racial caste, the fastest moral transformation in the nation's history, and it left wealth, housing, and schools substantially where law alone could not move them, which is the agenda the next era inherited."),
]

ARGUMENTS = [
    ("Law as a weapon and its limits", "The NAACP spent decades turning the Constitution against the system that claimed its protection, winning first against the white primary and restrictive covenants and then, in Brown, against school segregation itself. Cooper v. Aaron closed the legal escape hatch, holding that no state official could nullify the Court's reading of the Constitution. Yet the same record shows what a ruling alone could not move. Brown II carried no deadline, Prince Edward County closed its schools, and ten years after 1954 barely one Black child in a hundred in the deep South sat in a classroom with white children. Law opened the door. It took protest, federal enforcement, and two great statutes to push the country through it, and Milliken later showed the courts drawing a line the movement could not cross."),
    ("Protest that created a crisis", "Montgomery taught the method in sequence, economic pressure, an institution of the movement's own, a moral claim in the language of the Constitution and the church, and cameras watching. The students of 1960 sharpened the method into a test of federal power. Sit-ins and Freedom Rides worked when they created a crisis the federal government could not ignore, and Birmingham was chosen to make that crisis unavoidable, while Albany stands in the same unit as the proof of the limit, a campaign answered with polite mass arrests that moved no federal power and won nothing. Judging any single campaign means asking what crisis it created, who it moved, and what it cost, and the unit's documents let students answer all three."),
    ("The federal government in three roles", "Washington appears in this unit as ally, referee, and reluctant enforcer, sometimes in the same year. Truman named civil rights federal business in 1947 and desegregated the armed forces in 1948. Eisenhower, who never endorsed Brown, sent the 101st Airborne to Little Rock because a governor's defiance of a court was the one thing he could not let stand. Kennedy moved only after Birmingham filled the nation's screens, and Johnson, who knew the Senate, turned protest outside the Capitol into the acts of 1964 and 1965. The pattern the documents support is not a government leading the movement. It is a movement making federal action unavoidable, and then counting the cost of enforcement, in registered voters, in funds cut off, and in schools that resegregated inside lines federal law would not cross."),
    ("Visions of freedom and the unfinished agenda", "By 1966 the movement argued with itself, in the open, about what freedom required. One vision held to integration and the ballot, another called for Black political and economic power built and defined by Black Americans, the Panthers joined self defense to breakfast programs and clinics, and King's last campaign recast the whole demand as an economic bill of rights for an interracial army of the poor. Other Americans took the movement's tactics, language, and legal tools and made them their own. The Kerner Commission named the ground still unheld, housing, wealth, and the schools of the northern city, and the argument over remedy that Johnson posed at Howard University in 1965 was still running in Bakke in 1978. The unit closes there on purpose. The agenda left unfinished is part of the record, not a footnote to it."),
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
    P.append("<title>Study Guide: The Civil Rights Movement</title>")
    P.append(f"<style>{CSS}</style></head><body>")
    P.append('<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>')
    P.append('<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>')
    P.append("<h1>Study Guide: The Civil Rights Movement</h1>")
    P.append('<p class="directions"><strong>Directions:</strong> Complete Part 1 from your guided notes and readings, then answer the Part 2 questions in your own words. Part 3 summarizes the arguments that run through the whole unit. The unit test is built from this guide. Bring questions about anything you cannot answer to the review day.</p>')
    P.append("<p><strong>Unit question:</strong> How did the civil rights movement change American law and American life, and what did it leave unfinished?</p>")
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
