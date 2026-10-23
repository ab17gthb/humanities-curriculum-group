#!/usr/bin/env python3
"""Build the Jackson and Reform review study guide from the verbatim
vocabulary in build-scripts/unit-spec.md, plus 24 review questions
with a full key, a short frame passage, and the fifteen entries of
the unit blueprint restated in student language. Mirrors the Early
Republic study guide. The teacher key carries no blueprint tags."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
UNIT = os.path.dirname(HERE)
SPEC = open(os.path.join(HERE, "unit-spec.md")).read()

LESSON_TITLES = {
    1: "The Election of 1828 and Jacksonian Democracy",
    2: "Indian Removal",
    3: "The Nullification Crisis",
    4: "The Bank War and the Panic of 1837",
    5: "The Market Revolution",
    6: "The Second Great Awakening and Reform",
    7: "Abolition",
    8: "Women's Rights and Seneca Falls",
}

def parse_terms():
    terms = {}
    current = None
    in_vocab = False
    for line in SPEC.splitlines():
        if line.startswith("## Vocabulary"):
            in_vocab = True
            continue
        if in_vocab and line.startswith("## "):
            break
        if not in_vocab:
            continue
        m = re.match(r"### Lesson (\d)", line)
        if m:
            current = int(m.group(1)); terms[current] = []
            continue
        m = re.match(r"- ([^:]+): (.+)$", line)
        if m and current:
            terms[current].append((m.group(1).strip(), m.group(2).strip()))
    return terms

QUESTIONS = [
    (1, "What happened in the election of 1824, and how did the charge of a corrupt bargain shape the campaign of 1828?",
     "In 1824 four candidates split the vote, Jackson finished first in popular and electoral votes but short of a majority, and the House of Representatives chose John Quincy Adams, who then named Henry Clay secretary of state. Jackson's supporters charged that Clay had traded his support for the office, a charge both men denied. Jacksonians carried the charge through four years of organizing, building committees, newspapers, and a party around the claim that the people's choice had been stolen, and in 1828 Jackson won decisively at the head of the first mass white electorate in the nation's politics."),
    (1, "How did the vote widen in the 1820s, and who was left outside the widening?",
     "State after state struck the property qualifications that had fenced the vote since the founding, until by 1828 suffrage belonged to nearly every white man regardless of property, and turnout became the currency of politics. The same constitutions narrowed the vote for others. Women were excluded everywhere, New Jersey having closed in 1807 a door its first constitution had left open. Free Black men were stripped of the vote in states that had let them cast it, Pennsylvania following in 1838. Native nations stood outside the polity entirely. The democracy of the era widened by race and sex at the same time, and the lesson keeps both halves of that sentence together."),
    (1, "What did Jackson mean by rotation in office, and what name did his opponents give the practice that followed?",
     "In his first annual message Jackson argued that public offices were trusts, that no man had more right to hold an office than another, and that offices should pass regularly from citizen to citizen instead of hardening into the property of a permanent officeholding class. The removals that followed were modest beside the legend, some nine hundred of nine thousand civil officers by the usual count, but they established the principle. Opponents named it from a senator's phrase, that to the victor belong the spoils, and the spoils system became their charge that office had become party pay. Jacksonians answered that rotation was democracy applied to the government itself."),
    (2, "What did the Indian Removal Act authorize, and how did Jackson defend removal in his message of December 1830?",
     "The act of May 1830, passed in the House by five votes, authorized the president to offer Native nations land west of the Mississippi in exchange for their lands inside the states, and appropriated half a million dollars to carry the exchanges out. It was the legal instrument under which the southeastern nations were driven out in the 1830s. Jackson's annual message of December 1830 defended the policy in the language of benevolence, presenting the president as a father removing his children from contact with a civilization he claimed was destroying them, and promising the nations a country of their own in the West. The Cherokee read the same message as a sentence on their farms, towns, and government."),
    (2, "How did the Cherokee resist removal through law, and what did Worcester v. Georgia decide and fail to do?",
     "The Cherokee answered pressure with law. The nation had adopted a written constitution, a syllabary and a newspaper, farms, and missions, and it carried a memorial campaign to Congress and its case to the Supreme Court under Principal Chief John Ross. In Worcester v. Georgia in 1832, Chief Justice Marshall held that Georgia's laws had no force within Cherokee country. Georgia defied the judgment, and President Jackson declined to enforce it against the state. The case therefore decided the law and changed nothing on the ground, and the lesson the Cherokee drew was that the republic's law ran where the republic chose to run it."),
    (2, "How was the Treaty of New Echota obtained, and what happened on the Trail of Tears?",
     "In December 1835 a minority of Cherokee, Major Ridge, John Ridge, Elias Boudinot, and their party, signed at New Echota a treaty ceding the nation's eastern land, acting without the authority of Ross's government. A petition carrying the names of nearly the whole nation protested it, and the Senate ratified it by a single vote. It supplied the legal cover for removal. In 1838 troops rounded up some sixteen thousand Cherokee into camps and marched them west in detachments through the winter of 1838 and 1839, roughly a quarter of them dying on the road. The other southeastern nations went by their own roads of force and negotiation, and the Seminole fought the costliest Indian war the United States ever fought and were never wholly removed."),
    (3, "Why did South Carolina call the tariff of 1828 an abomination, and what doctrine did the Exposition and Protest build against it?",
     "The Tariff of 1828 raised duties on imported goods to protect northern manufacturers. The planting states paid the higher prices on everything they bought, and the duties invited foreign retaliation against the cotton that paid for those purchases, so southerners denounced the tariff by that name. The South Carolina Exposition and Protest, adopted in December 1828 and written secretly by Vice President Calhoun, argued that the Constitution was a compact among the states, that a state as a party to the compact could declare a federal law void inside its borders, and that the law would stand nullified until the Constitution itself was amended over the state's head."),
    (3, "What did Webster and Hayne argue in the Senate in January 1830, and how did Jackson declare his own position that spring?",
     "The debate began over western land sales and rose to the nature of the Union. Robert Hayne of South Carolina defended the compact theory and nullification. Daniel Webster of Massachusetts answered that the Constitution was the people's government, not a compact of states, and closed with his defense of liberty and union as one and inseparable, words schoolchildren recited for a century. At the Jefferson Day dinner in April 1830 Jackson rose, glass in hand, and gave his toast to the federal Union, saying it must be preserved. Calhoun answered with the Union next to liberty most dear, and everyone at the table understood that the president and his vice president had declared opposite positions."),
    (3, "State the Ordinance of Nullification, and state the settlement that ended the crisis in 1833.",
     "A South Carolina convention adopted the ordinance on November 24, 1832. It declared the tariffs of 1828 and 1832 void within the state, forbade collection of their duties after February 1, 1833, and threatened secession if the federal government collected them by force. Jackson answered with a proclamation holding that the Union was a government and not a league. No other state joined South Carolina. In March 1833 Congress passed the Force Bill, authorizing Jackson to use the army and navy to collect the duties, and in the same week Clay's compromise tariff, lowering duties by stages toward the levels of 1816 by 1842. South Carolina repealed its ordinance and nullified the Force Bill in empty triumph, and each side claimed it had won."),
    (4, "How did the Bank War open, and what arguments did Jackson's veto of July 1832 make against the Second Bank?",
     "The Bank's charter ran to 1836, but Clay and Nicholas Biddle, the Bank's president, forced its recharter to a vote in 1832, four years early, meaning to make the Bank the deciding question of the election. Congress passed the recharter and Jackson vetoed it on July 10, 1832. The veto message argued that the Bank's privileges were artificial distinctions granted by law, that they made the rich richer and the powerful more powerful, and that the humble members of society, the farmers, mechanics, and laborers, had a right to complain when government showered its favors on the few. Government confined to equal protection, Jackson wrote, would be an unqualified blessing. Jackson won reelection decisively that fall."),
    (4, "How did Jackson destroy the Bank after the veto, and what did the Specie Circular try to stop?",
     "In 1833 Jackson removed the federal deposits from the Second Bank and placed them in selected state banks, which the Bank's defenders named pet banks in contempt. Biddle answered by contracting the Bank's credit, meaning to prove the nation's need of it, and the fight discredited him. The pet banks lent easily on thin reserves and fed a speculation in public lands bought with paper banknotes. In July 1836 the Treasury issued the Specie Circular, requiring gold or silver in payment for public lands, to stop speculation bought with paper. Critics blamed the order for draining specie from eastern banks on the eve of panic."),
    (4, "What happened in the Panic of 1837, and what two political answers came out of the wreckage?",
     "In May 1837 banks across the country suspended payment in specie, cotton prices and land values fell, and a depression followed that lasted into the 1840s and broke the presidency of Martin Van Buren, Jackson's successor. The first answer was a party. The Whig Party had coalesced in 1834 from National Republicans, Anti-Masons, and disaffected Democrats, named for the historic opponents of royal power and united at first chiefly by resistance to what they called executive usurpation. The second answer was Van Buren's independent treasury, enacted in 1840, under which the federal government kept its own money in its own vaults rather than in any bank, divorcing the Treasury from the banking system."),
    (5, "What changed in the American economy between about 1815 and 1848, and what did the change do to households?",
     "Canals, steamboats, railroads, and the telegraph cut the cost and time of moving goods and news across the country. Households that had made most of what they used began producing for distant markets and buying from them, so a farm family's income now depended on prices in cities it would never see, and a mill town's food arrived by canal from farms hundreds of miles away. Historians call the transformation the market revolution. It bound the sections into one market while it tied every household in that market to booms and panics it could not control, which is one reason the politics of banks and tariffs in this unit ran so hot."),
    (5, "How did the factory system differ from the older pattern of making goods, and how did the Lowell system recruit its workers?",
     "Under the factory system workers gather in one building to work set hours at machines owned by their employer, replacing the older pattern of artisans and households making goods at their own pace in their own shops and homes. At Lowell, Massachusetts, the Boston Associates built factories, boardinghouses, and churches together and recruited young women from New England farms to work the looms under rules meant to guard their morals and their hours. The mill women, the Lowell system by which they were housed and governed, and the newspaper they wrote for themselves made Lowell the showplace of the new system, and its turnouts, when hours lengthened and wages were cut, showed its workers judging the system for themselves."),
    (5, "What did interchangeable parts and the telegraph each change, and what happened to the trade unions of the 1830s?",
     "Interchangeable parts, perfected in the federal armories and spread through New England shops, meant filing and machining every part of a product to a standard pattern so that any part fits any unit and a broken one can be replaced without a craftsman's hand fitting. The telegraph, which Samuel Morse opened between Washington and Baltimore on May 24, 1844, separated the speed of news from the speed of travel for the first time. Workers in the cities answered the new economy with trade unions, organizations formed to bargain over wages and hours and to strike when bargaining failed. They spread through the 1830s until the courts, the panic of 1837, and employer resistance broke most of them."),
    (6, "What did the Second Great Awakening teach, and how did Charles Grandison Finney's preaching put the teaching to work?",
     "The evangelical revival that swept the country from the turn of the century into the 1840s taught that every person could choose salvation, against the older doctrine that salvation was fixed in advance. Finney, whose Rochester meetings of 1830 and 1831 became the model of the new evangelism, preached that conversion was an act of the sinner's own will, something a preacher could organize for and a sinner could decide. He then organized his converts into the temperance, antislavery, and moral reform societies of the age. Western and central New York, swept so often by revival and reform that preachers said it had no fuel left to burn, became the burned-over district, the seedbed of the movements in the next three lessons."),
    (6, "How did the temperance movement change its demand between the 1820s and the 1840s?",
     "The movement against drink organized nationally in the American Temperance Society of 1826. In the 1820s it asked for pledges of moderation, drinkers promising to use alcohol carefully or to give up distilled spirits while keeping beer and wine. Through the 1830s the pledge hardened into total abstinence, the teetotal pledge, and in the 1840s the movement carried its demand into law, campaigning for legal prohibition of the sale of alcohol. The path from persuasion to pledge to statute is the standard path of the era's reforms, and temperance ran it furthest first, which is why the abolitionists and the women's rights organizers of the next lessons studied its organization as a model."),
    (6, "What did Horace Mann argue schools were for, and what did Dorothea Dix's investigations expose and build?",
     "Mann, the Massachusetts education secretary whose annual reports began in 1837, argued that tax supported common schools, open to all children of a district, were the balance wheel of the social machinery, the republic's instrument for making citizens out of a diverse and mobile people. He built the first American system of public schools with trained teachers, graded classes, and state supervision. Dix, a Massachusetts teacher, investigated jails and almshouses in the 1840s and exposed the insane confined in cages, closets, and cellars, kept like animals by towns that had made no other provision for them. Her memorials to legislatures, beginning with Massachusetts in 1843, built the first generation of American public asylums."),
    (7, "What changed in the antislavery movement in the 1830s, and what did Walker and Garrison each contribute to the change?",
     "The movement turned from the gradual emancipation and colonization schemes of the founding generation to immediatism, the doctrine that slavery, being a sin against God and man, must end at once, without gradual stages, compensation, or removal of the freed people. David Walker's Appeal of 1829, published in Boston and smuggled into the South, called on enslaved people to resist their enslavement and warned white Americans that their professions of freedom stood condemned by their practice. William Lloyd Garrison founded The Liberator in 1831, renounced gradualism and colonization in its first issue, and built the American Anti-Slavery Society into the organizational engine of the new doctrine."),
    (7, "What did Nat Turner do in August 1831, and how did Virginia and the southern states answer?",
     "Nat Turner, an enslaved preacher of Southampton County, Virginia, led in August 1831 the deadliest slave rebellion in United States history, in which about sixty white people were killed before the rising was put down. Turner was captured, tried, and hanged, and his jailhouse account was published by the lawyer who questioned him. Virginia debated emancipation in its legislature one last time and rejected it. The southern states then tightened their slave codes, barred the teaching of reading to the enslaved, restricted Black preaching and assembly, and ended open debate on emancipation within the South. The rebellion and the closing that followed it stand behind the national fight over antislavery speech in the next question."),
    (7, "What was the gag rule, and how did Frederick Douglass's Narrative answer the slaveholders' argument about the enslaved?",
     "From 1836 to 1844 the House of Representatives tabled every antislavery petition without printing, reading, or debate, under a rule its supporters renewed session after session. Former president John Quincy Adams, serving in the House, fought it year after year as a violation of the right of petition until its repeal in 1844. Douglass, who escaped slavery in Maryland in 1838 and was discovered as an orator by the Massachusetts Anti-Slavery Society in 1841, published his Narrative in 1845. It was a first person account whose literacy and argument answered the slaveholders' claim that the enslaved could not speak for themselves, written by a man the law had forbidden to learn to read."),
    (8, "Where did the Seneca Falls Convention come from, and what happened there on July 19 and 20, 1848?",
     "Lucretia Mott, a Quaker minister and abolitionist of Philadelphia, and Elizabeth Cady Stanton were excluded as women from the World's Anti-Slavery Convention of 1840, and the exclusion first turned them toward organizing for women's rights. They and their associates called the convention at Seneca Falls, New York, the first convention in the United States called to discuss the social, civil, and religious condition and rights of woman. Some three hundred people attended. The convention adopted Stanton's Declaration of Sentiments and a set of resolutions, and adopted the demand for the elective franchise, which Stanton had insisted on against the advice of nearly every ally, by a narrow margin, with Frederick Douglass arguing for it from the floor."),
    (8, "How is the Declaration of Sentiments built, and what legal structure were its grievances written against?",
     "The declaration is modeled sentence by sentence on the Declaration of Independence. It holds that all men and women are created equal, and it charges man with a history of repeated injuries and usurpations toward woman as its bill of grievances: the vote never permitted, laws made without her voice, property and wages taken. The structure underneath the grievances is coverture, the common law doctrine under which a married woman's legal existence was covered by her husband's, so her property, her wages, and her standing in court passed under his control. Three months before the convention, New York's Married Women's Property Act of April 1848 had let a married woman hold property in her own name apart from her husband's debts, the first breach in that structure."),
    (8, "What had the Grimké sisters already done before Seneca Falls, and why does the unit end in 1848 with their example in view?",
     "Sarah and Angelina Grimké of Charleston left the slaveholding South and became abolitionist lecturers, first to audiences of women and then, scandalously, to audiences of men and women together. When clergy ordered women silent, Angelina answered with her Appeal to the Christian Women of the South of 1836, addressed to southern women as moral actors, and Sarah answered with her Letters on the Equality of the Sexes of 1837 and 1838, arguing from scripture that the sexes stood equal. They had therefore made the women's rights argument a decade before Seneca Falls, in public, under attack, as working abolitionists. The unit ends in 1848 because by then every argument the era had made against one hierarchy had been turned, by the people the hierarchy governed, against the rest."),
]

FRAME = [
    "Democracy in Jackson's America named, first, a widening. State after state struck the property fences from the vote until nearly every white man could cast one, the election of 1824 taught Jackson's supporters that a House of Representatives could take what the voters had given, and the campaign of 1828 built the first mass politics of committees, newspapers, and barbecues to take it back. Jackson governed in that majority's name: rotation in office against a permanent officeholding class, the veto against a bank he called a grant of privilege to the rich, and a presidency strengthened by every fight it won. The same presidency answered South Carolina's claim to nullify a federal law with a proclamation that the Union was a government and not a league, and armed itself with the Force Bill while it accepted the compromise tariff. Who the democracy was for is the other half of the record, and the unit never lets the halves separate. The widened vote widened for white men as the same constitutions stripped free Black men of ballots they had cast and kept women outside entirely, and the people's president removed the southeastern Native nations under law at every step, act, treaty, appropriation, and bayonet, after the Supreme Court had held the ground was not the states' to take.",
    "The economy the voters lived in was being remade under them. Canals, steamboats, railroads, and the telegraph bound households to distant markets, the factory system gathered workers under an employer's roof and clock, and Lowell's mill women wrote and struck inside the showplace of the new order. The Bank War and the panic that followed were this economy become politics: a national bank destroyed as privilege, its deposits scattered to pet banks, land bought on paper until the Specie Circular and the collapse of 1837 taught a generation what a credit economy does when it breaks. Revival ran through the same country at the same speed. The Second Great Awakening taught that a sinner could choose salvation the way a voter chose a candidate, and Finney's converts built the societies that carried the teaching into temperance pledges, common schools, and asylums for people the towns had kept in cages. Reform in this era was democracy's method applied to society: organize, publish, petition, pledge, and legislate, in that order or any order that worked.",
    "What the reformers claimed the democracy still owed is the unit's closing argument, made by the people it had left outside. Abolition turned from gradual schemes and colonization to immediatism because Walker, Garrison, and the enslaved themselves refused a freedom postponed, and the House answered a flood of petitions by gagging them for eight years rather than hear the claim. Douglass wrote his way out of the slaveholders' premise in a Narrative whose existence was the refutation. At Seneca Falls in 1848, women who had run abolition's local work for a decade turned its logic on their own legal condition, modeled their declaration on the founding text, charged coverture in the founders' own form, and demanded the franchise by a narrow margin in the same state that had just passed the first Married Women's Property Act. The unit closes there deliberately. Democracy in Jackson's America meant majority rule by white men, widened further than anywhere else on earth and bounded in law by race and sex, and the era's reformers, standing on its own stated principles, presented the bill for the difference.",
]

BLUEPRINT_STUDENT = [
    "Explain the election of 1828 and Jacksonian democracy, the corrupt bargain charge of 1824, the committees and newspapers of the new mass politics, and the party that formed around Jackson.",
    "Explain how suffrage widened for white men in the 1820s while women, Native Americans, and most free Black men remained or were newly excluded, and explain the spoils system and rotation in office.",
    "Explain the Indian Removal Act of 1830 and Jackson's defense of removal, and explain how the Cherokee Nation resisted through its constitution, its newspaper, petitions, and the courts under John Ross.",
    "Explain how removal was carried out, Worcester v. Georgia decided and defied, the Treaty of New Echota signed by a minority and ratified by one vote, and the Trail of Tears of 1838 and 1839.",
    "Explain the doctrine of nullification, the Tariff of Abominations, Calhoun's South Carolina Exposition and Protest, and the Webster-Hayne debate over whether the Constitution was a compact of states or the people's government.",
    "Explain the nullification crisis of 1832 and 1833, the Ordinance of Nullification, Jackson's proclamation and the Force Bill, and the compromise tariff under which South Carolina backed down.",
    "Explain the Bank War, Clay and Biddle forcing the recharter vote of 1832, Jackson's veto and its argument about privilege, and the removal of the federal deposits to the pet banks.",
    "Explain what followed the Bank War, the pet banks and land speculation, the Specie Circular, the Panic of 1837, the rise of the Whig Party, and Van Buren's independent treasury.",
    "Explain the market revolution, how canals, steamboats, railroads, and the telegraph cut the cost and time of moving goods and news, and how households began producing for distant markets and buying from them.",
    "Explain the factory system and the Lowell system, interchangeable parts, the telegraph and Samuel Morse, and the trade unions of the 1830s and what broke most of them.",
    "Explain the Second Great Awakening, Finney's preaching that conversion was an act of the sinner's own will, the burned-over district, and the temperance movement's path from pledges of moderation to campaigns for prohibition.",
    "Explain Horace Mann and the common schools, tax supported schools open to all children of a district, and Dorothea Dix's investigations and the first generation of American public asylums her memorials built.",
    "Explain abolition's turn to immediatism, Walker's Appeal of 1829, Garrison's Liberator and the American Anti-Slavery Society, and the break with gradual emancipation and colonization.",
    "Explain Nat Turner's rebellion of 1831 and the tightening of the slave codes that followed, the gag rule of 1836 to 1844 and John Quincy Adams's fight against it, and Frederick Douglass's Narrative of 1845.",
    "Explain the Seneca Falls Convention of 1848, the Declaration of Sentiments and its grievances against coverture, Stanton and Mott and the Grimké sisters, the demand for the elective franchise, and the Married Women's Property Act of April 1848.",
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
    P.append("<title>Study Guide: Jackson and Reform</title>")
    P.append(f"<style>{CSS}</style></head><body>")
    P.append('<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>')
    P.append('<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>')
    P.append("<h1>Study Guide: Jackson and Reform</h1>")
    P.append('<p class="directions"><strong>Directions:</strong> Complete Part 1 from your guided notes and readings, then answer the Part 2 questions in your own words. Part 3 tells the unit as one story and lists what the test will ask you to show. The unit test is built from this guide. Bring questions about anything you cannot answer to the review day.</p>')
    P.append("<p><strong>Unit question:</strong> What did democracy mean in Jackson's America, who was it for, and what did the era's reformers claim it still owed?</p>")
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
    P.append('<div class="arguments"><h2>Part 3: The Unit as a Whole</h2>')
    for body in FRAME:
        P.append(f"<p>{body}</p>")
    P.append("<h3>The Unit Blueprint in Student Language</h3>")
    P.append("<p>The test is built to ask whether you can do these fifteen things. If you can do each one with evidence, you are ready.</p>")
    for i, item in enumerate(BLUEPRINT_STUDENT, 1):
        P.append(f"<p><strong>{i}.</strong> {item}</p>")
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
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write("\n".join(P))
    print(f"wrote {out}: {total} terms, {len(QUESTIONS)} questions")

if __name__ == "__main__":
    main()
