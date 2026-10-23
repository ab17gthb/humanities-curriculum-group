#!/usr/bin/env python3
"""Build the Modern America review study guide from the verbatim
vocabulary in build-scripts/unit-spec.md, plus 24 review questions with a
full key and the arguments of the era. Mirrors the Civil Rights study guide."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
UNIT = os.path.dirname(HERE)
SPEC = open(os.path.join(HERE, "unit-spec.md")).read()

LESSON_TITLES = {
    1: "The Conservative Turn: Stagflation and the Tax Revolt", 2: "The Reagan Revolution",
    3: "After the Cold War: Globalization and the New Economy", 4: "The Digital Transformation",
    5: "A Changing America: Immigration, Cities, and the Sun Belt", 6: "September 11 and the War on Terror",
    7: "The Great Recession and Its Long Aftermath", 8: "A Polarized Nation: America in the Twenty-First Century",
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
    (1, "What was stagflation, and why did it break the expectations Americans had carried since 1945?",
     "The generation after 1945 had expected rising wages, cheap energy, and a federal government able to manage the economy. By the middle 1970s all three expectations failed at once. Inflation rose through the decade while growth stalled and unemployment stayed high, the combination named stagflation. The standard economics of the day held that inflation and unemployment moved in opposite directions, so the two arriving together left the managers of the economy without a working answer, and voters without the rising standard of living they had been promised."),
    (1, "How did the tax revolt begin, and what did Proposition 13 do?",
     "Voters who felt squeezed by inflation and by rising property tax bills demanded lower taxes and limits on government spending. The revolt opened in California in June 1978, when voters passed Proposition 13, a ballot measure that cut property taxes sharply, by more than half for many owners, and capped their future growth. The measure became the opening victory of a national tax revolt, and limits on taxes and spending spread across the states in the years that followed."),
    (1, "Who organized the politics that replaced the postwar settlement, and what coalition did they build?",
     "The New Right was the coalition of conservative activists, organizations, and voters that rose in the 1970s around lower taxes, a stronger military, and resistance to the social changes of the 1960s. Its machinery included direct mail, single issue groups, and think tanks. The Moral Majority, founded by the Reverend Jerry Falwell in 1979, carried evangelical Christian voters into politics behind conservative candidates. In the South, the voters the Republican southern strategy had courted since the Nixon years were now joined by suburban taxpayers, and that joined coalition was the electoral arithmetic behind the election of 1980."),
    (2, "What did the Reagan program do in its first years, and how was inflation broken?",
     "President Reagan stated the mandate in his first inaugural address of January 20, 1981, declaring that government was the problem and promising to curb the size and influence of the federal establishment. The Economic Recovery Tax Act of 1981 cut income tax rates by a quarter over three years and cut the top rate from seventy percent to fifty percent, spending cuts were aimed at domestic programs, and deregulation continued and extended in banking, transport, and communications. The theory behind the program, supply-side economics, held that cutting tax rates and reducing regulation would free investment and production and grow the whole economy. Inflation itself was broken by Paul Volcker's Federal Reserve, which raised interest rates above nineteen percent at the cost of the deep recession of 1981 and 1982, when unemployment reached 10.8 percent."),
    (2, "What did the PATCO strike settle about the era's terms for labor?",
     "In August 1981 the federal air traffic controllers struck, although federal law barred them from striking. President Reagan fired more than eleven thousand of them and barred them from federal service. Unions and employers alike read the act as a signal of the era's terms. The government itself, as an employer, would break a strike by a public union and replace its members, and private employers drew the lesson that replacement workers and hard bargaining carried less risk than they once had."),
    (2, "What were the limits of the Reagan Revolution, and what was the Iran-Contra affair?",
     "The revolution left the core of the older order standing. Social Security and Medicare were untouched, a tax increase in 1982 quietly reclaimed part of the 1981 cut, and the federal deficit grew, with the national debt rising from about nine hundred billion dollars in 1981 toward three trillion dollars by 1989. The courts became the revolution's longest instrument through judicial appointments. The breach inside the administration was the Iran-Contra affair of 1985 to 1987, in which officials secretly sold arms to Iran and diverted the proceeds to the Contra rebels in Nicaragua, against stated policy and a congressional ban. The Tower Commission and congressional committees investigated, and the affair stood as the era's largest scandal."),
    (3, "What was the peace dividend debate, and how did the Persian Gulf War open the post Cold War decade?",
     "When the Cold War ended in 1991, Americans debated where the money and attention the rivalry had consumed should go. That expected redirection, toward deficits, tax cuts, or needs at home, was called the peace dividend. The Persian Gulf War of January and February 1991 was the sole superpower's first war of the new era. An American-led coalition, acting with United Nations authorization, drove Iraq's army out of Kuwait in six weeks, in a brief war carried live on television."),
    (3, "How did globalization rebuild the American economy in the 1990s, and how was NAFTA argued over?",
     "Trade and investment tied the world's economies closer together, production spread across borders, and imports and exports rose as a share of the American economy. The North American Free Trade Agreement removed most tariffs and trade barriers among the United States, Canada, and Mexico from January 1, 1994. Supporters in both parties argued the agreement would lower prices, widen markets for American goods, and bind Mexico to the United States. Organized labor and Ross Perot argued against it, Perot warning of jobs moving south to lower wage workers. The World Trade Organization followed in 1995 and permanent normal trade relations with China in 2000."),
    (3, "What did the boom of the 1990s look like in jobs and budgets, and what ran underneath it?",
     "The long expansion of the 1990s brought unemployment under four percent by 2000 and a federal budget in surplus from 1998 to 2001, the first sustained surpluses in a generation. Welfare law was rewritten in 1996 with work requirements and time limits. Underneath the boom, the older factory economy kept shrinking. Deindustrialization emptied mills across the Rust Belt, outsourcing moved production to lower cost workers abroad, and the service economy of health care, retail, finance, and food service supplied most new jobs. Productivity rose while median wages rose slowly, and that gap was the distributional argument of the decade."),
    (4, "How did the personal computer and the Internet remake work and commerce between 1980 and 2010?",
     "The personal computer carried computing out of institutions and onto desks and into homes from the late 1970s onward, software became an industry of its own, and the workplace was rewritten task by task as typing pools and drafting tables gave way to screens. The Internet grew out of government and university systems, opened to the public and to commerce in the middle 1990s, and reached a majority of American homes by 2001, according to Census Bureau figures. E-commerce grew from almost nothing in the middle 1990s into a central part of American retail."),
    (4, "What was the dot-com bubble, and how did it end?",
     "In the late 1990s investors bid Internet company stocks to heights their earnings did not support, on the claim that the network had rewritten the rules of business. The boom peaked in March 2000 and then collapsed. By 2002 the crash had erased trillions of dollars in paper wealth, and companies built on the boom's prices closed or were sold for a fraction of their value. Contemporaries reached for the railroads' older boom as the comparison, a real technology oversold in its first decade."),
    (4, "How did the news world fracture, and what was the digital divide?",
     "Cable news ran around the clock from CNN's founding in 1980, talk radio went national after the Fairness Doctrine was repealed in 1987, and the newspaper's advertising base drained toward free online listings. By the 2000s an American could live inside a news world of one tendency, a fragmentation visible in audience data. From the middle 2000s, social media put publication in every pocket, and the smartphone after 2007 joined the network to the person. The digital divide ran through all of it, the gap between Americans with ready access to computers and the Internet and those without, following lines of income, education, age, and place in the Census and NTIA surveys."),
    (5, "What did the Immigration and Nationality Act of 1965 change, and what followed from it?",
     "The act of 1965 ended the national origins quota system in place since the 1920s and built the new system on family reunification and needed skills. Its makers expected a modest change. Across the following half century the sources of immigration shifted from Europe toward Latin America and Asia, and the foreign born share of the population rose from under five percent in 1970 to about thirteen percent by the 2010s, the largest immigrant population in the nation's history in absolute terms, according to the Census Bureau."),
    (5, "What two halves did the Immigration Reform and Control Act of 1986 join, and what has been argued about each?",
     "The act of 1986 joined legal status for about three million unauthorized immigrants already in the country, the amnesty for those who had arrived before 1982, to the first federal ban on employers knowingly hiring unauthorized workers. The argument since has run over whether each half was carried out. Defenders of the settlement point to the millions who gained legal status. Critics charge that the employer ban was weakly enforced and that unauthorized immigration continued, and supporters of the ban answer that enforcement was never given the tools its authors promised."),
    (5, "How was the map of the country redrawn between 1970 and 2020?",
     "Americans moved as well as arrived. The Sun Belt of the South and Southwest grew fast on air conditioning, defense and technology work, and lower costs, while older industrial cities hollowed out under deindustrialization and white flight, the movement of white families to the suburbs that had accelerated with school desegregation orders. Detroit lost more than half its peak population. Congressional seats and electoral votes followed the moving population in each census reapportionment. From the 1990s, a partial urban revival and gentrification raised prices and rents in the strongest cities and pushed poorer residents out of neighborhoods they had lived in."),
    (6, "What happened on September 11, 2001, stated in the Commission's terms?",
     "Nineteen men of the al Qaeda network, the terrorist organization led by Osama bin Laden, hijacked four airliners. Two were flown into the World Trade Center in New York, one into the Pentagon, and the fourth crashed in Pennsylvania after its passengers fought the hijackers. The attacks killed 2,977 people and were the worst attack on American soil in the nation's history. The 9/11 Commission later found failures of imagination, policy, capabilities, and management behind the day."),
    (6, "What legal architecture did the government build in the weeks after the attacks?",
     "Congress passed the Authorization for Use of Military Force on September 18, 2001, by all but one vote, authorizing the president to use all necessary and appropriate force against those responsible for the attacks and those who harbored them. The USA PATRIOT Act of October 2001 widened the government's powers of surveillance, search, and detention in terrorism investigations, passing by overwhelming margins, while its own Section 102 condemned discrimination against Arab and Muslim Americans. In 2002 the Department of Homeland Security merged twenty two federal agencies and offices, and airport security was federalized."),
    (6, "How did the Iraq War's stated ground hold up, and how was the security state argued over?",
     "The United States invaded Iraq in March 2003. The stated ground, presented to the public and to the United Nations, was the claim that Iraq possessed stockpiles of weapons of mass destruction. No such stockpiles were found, as the Iraq Survey Group's final report recorded. The war became an insurgency and a long occupation, and the two wars in Afghanistan and Iraq together cost more than seven thousand American dead and sums counted in the trillions. Officials of the administrations that built the security state argued its powers and wars kept the country safe from a second mass attack. Critics charged that the wars and the surveillance powers, including programs revealed in 2013, cost more than they bought and reached past the Constitution's limits. The unit's documents carry both claims as claims."),
    (7, "How did the financial system nearly fail in 2008?",
     "House prices rose for a decade on easy credit. Subprime mortgages, home loans made to borrowers with weak credit at higher rates, were issued in large numbers and bundled into securities sold around the world, on the assumption that house prices would not fall nationwide. Prices fell from 2006, the securities soured, and Lehman Brothers failed on September 15, 2008. Money market funds and credit markets froze, and the officials who answered stated in their own record that the system itself was days from collapse. The Great Recession that followed was the deepest collapse since the Great Depression."),
    (7, "What did the government do in the rescue, and what did households pay?",
     "The Troubled Asset Relief Program of October 2008 authorized up to seven hundred billion dollars to steady the banking system, the Federal Reserve lent widely and cut interest rates to near zero, the automobile industry was carried through managed bankruptcies, and the stimulus of February 2009 put about eight hundred billion dollars of spending and tax cuts into the economy. Households paid the bill on a different schedule. Unemployment reached ten percent in October 2009, about nine million jobs were lost, millions of homes were foreclosed, and household wealth fell by trillions, in figures from the Bureau of Labor Statistics and the Federal Reserve."),
    (7, "What two protest movements answered the aftermath, and what did each claim?",
     "The Tea Party movement rose in 2009 against the bank bailouts, the stimulus, and the Affordable Care Act of 2010, the health law that required most Americans to carry insurance, barred denial of coverage for prior illness, and expanded Medicaid. Tea Party supporters described all three as one government grown too large and demanded smaller government and lower taxes. Occupy Wall Street began in New York in September 2011 and spread to cities across the country, camping in financial districts to protest economic inequality in the name of the ninety nine percent against the one percent, and its supporters described the rescue as proof that losses were shared while gains stayed private. The recovery's arithmetic framed the argument between them. Output and jobs returned while wealth and trust did not return on the same schedule."),
    (8, "What is political polarization, and what did the election of 2000 show about it?",
     "Political polarization is the sorting of Americans into two hostile political camps with fewer voters in the middle, visible from the 1990s onward in congressional roll call records, in county level landslides, in shrinking split ticket voting, and in survey measures of party identity, the sources the lesson names. The election of 2000 showed how narrow the country's margins had become. The result turned on Florida, and the Supreme Court stopped the recount of Florida's ballots in Bush v. Gore, decided by five votes to four, settling the election for George W. Bush."),
    (8, "What did the courts decide in Heller, Citizens United, and Obergefell, and how did the affirmative action argument close?",
     "In District of Columbia v. Heller in 2008, the Court held that the Second Amendment protects an individual's right to keep a handgun in the home for self-defense. In Citizens United in 2010, the Court held that the government may not limit independent political spending by corporations and unions, and the decision opened the way to super PACs and large outside spending in elections. In Obergefell v. Hodges in 2015, the Court held that the Fourteenth Amendment requires every state to license marriages between two people of the same sex. The affirmative action argument ran from the revised Philadelphia Plan of 1969 through Bakke in 1978, which allowed race as one factor among others in admissions, and closed for college admissions in 2023, when the Court ended race conscious admissions in Students for Fair Admissions."),
    (8, "How did the COVID-19 pandemic test the system, and what did the unit leave open at the close of the course?",
     "The pandemic reached the United States in 2020 and killed more than a million Americans. Schools and businesses were closed by state order, Congress passed a federal rescue of more than two trillion dollars in the CARES Act, and vaccines were developed in under a year by a government backed crash program. The argument over mandates and closures divided along the partisan lines the lesson had already drawn, with each side's claims attributed to their makers in the documents. The course closes where the unit closes. The arguments of the present, over the size of government, the reach of rights, the terms of membership in the nation, and the country's place in the world, are the same arguments the course met in 1776, 1861, 1933, 1954, and 1968, and the documents present them as still unsettled."),
]

ARGUMENTS = [
    ("The size of government", "One side of the era's central argument held that the federal government had grown past its competence and its constitutional place. President Reagan stated the claim in his first inaugural address in 1981, and the tax revolt, the Tea Party movement of 2009, and critics of the Affordable Care Act restated it in their own terms across four decades. The other side held that only the federal government could answer the era's largest problems, and pointed to the deposit guarantees and rescue programs of 2008, the stimulus of 2009, the health law of 2010, and the pandemic rescue of 2020 as its evidence. Defenders of the rescue programs argued that government action kept a bad collapse from becoming a second Great Depression. Critics of the same programs answered that each rescue enlarged the state permanently and rewarded the institutions whose failures had made the rescue necessary."),
    ("The gains and costs of globalization", "Supporters of open trade, in both parties, argued that globalization lowered prices for consumers, opened foreign markets to American goods and services, and raised living standards in the countries that joined the trading system. Presidents of both parties made versions of that case for NAFTA in 1993, for the World Trade Organization, and for permanent normal trade relations with China in 2000. Organized labor and Ross Perot argued the other side during the NAFTA fight, warning that production would move to lower wage workers abroad. Workers and officials in the Rust Belt later pointed to closed mills, emptied cities, and the long fall of factory employment as the cost side of the ledger, while economists who defended the trade agreements answered that technology and automation, more than trade, had shrunk factory employment."),
    ("The reach of rights", "The era extended rights by statute and by court decision, and argued over each extension. Congress passed the Americans with Disabilities Act in 1990, extending the civil rights method to disability, and the Lilly Ledbetter Fair Pay Act in 2009. The Supreme Court held in Heller that the Second Amendment protects an individual right to a handgun in the home, and in Obergefell that the Fourteenth Amendment requires every state to license same sex marriage. Supporters of each decision described it as the Constitution's promises reaching people or claims they had not covered before. Critics of particular decisions answered, in the terms each case supplied, that the Court had read rights into the Constitution that its text and history did not hold, or that a decision had settled by judicial vote a question the political process should have decided."),
    ("The terms of membership", "The immigration settlement of 1965 and the settlement of 1986 set the era's terms for who could join the nation, and the argument over those terms never closed. Defenders of the 1986 act pointed to the legal status it gave about three million people already living in the country. Critics charged that its ban on hiring unauthorized workers was weakly enforced and that unauthorized immigration continued after it. The Civil Liberties Act of 1988, in which Congress apologized and paid redress to Japanese Americans interned during the Second World War, showed the country revising an older judgment about who had been wronged and what was owed. In the unit's last lessons the same argument appears in new forms, over enforcement at the border, over legal status for people brought to the country as children, and over what schools and ballots should require, with the claims on each side attributed to their makers in the documents."),
    ("The price of the security state", "After September 11, 2001, officials of the administrations that built the new security state argued that the Authorization for Use of Military Force, the PATRIOT Act, the Department of Homeland Security, and the wars in Afghanistan and Iraq were necessary answers to an enemy that had killed 2,977 people in one morning, and that the absence of a second attack on that scale was evidence the measures worked. Critics in Congress, in the press, and in the courts charged that the Iraq War rested on a claim about weapons of mass destruction that proved false, that surveillance programs revealed in 2013 reached past the limits the Constitution sets, and that detention and interrogation practices broke the country's own law and stated values. The 9/11 Commission's findings stand in the documents between the two claims, recording failures of imagination, policy, capabilities, and management before the attacks."),
    ("What the present settled and left open", "Some questions the era opened have documented answers. The Cold War ended, inflation was broken in the early 1980s, the Internet remade commerce and news within a generation, and the courts settled the counting of Florida's ballots in 2000, the individual right in Heller, and the licensing of same sex marriage in Obergefell, each settlement stated in the opinion that made it. Other arguments the documents leave running. The two parties sorted into hostile camps with narrow margins, the election of 2020 was certified after the attack on the Capitol of January 6, 2021, and the argument over that election's legitimacy is recorded in the unit as a documented division, with the official record stated as the record and the claims of each side attributed. The unit takes no side in that division. It closes by naming the older arguments the present is still having, over the size of government, the reach of rights, the terms of membership, and the country's place in the world."),
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
    P.append("<title>Study Guide: Modern America</title>")
    P.append(f"<style>{CSS}</style></head><body>")
    P.append('<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>')
    P.append('<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>')
    P.append("<h1>Study Guide: Modern America</h1>")
    P.append('<p class="directions"><strong>Directions:</strong> Complete Part 1 from your guided notes and readings, then answer the Part 2 questions in your own words. Part 3 summarizes the arguments that run through the whole unit. The unit test is built from this guide. Bring questions about anything you cannot answer to the review day.</p>')
    P.append("<p><strong>Unit question:</strong> How did the United States remake itself after 1980, in its economy, its population, and its place in the world, and what did the remaking settle and what did it leave open?</p>")
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
            P.append(f'<tr><td class="filled"><strong>{term}:</strong> {dfn}</td></tr>')
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
