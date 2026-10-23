#!/usr/bin/env python3
"""Build the Sectional Crisis and Civil War review study guide from
the verbatim vocabulary in build-scripts/unit-spec.md, plus 24 review
questions with a full key, a plain prose frame passage answering the
unit essential question, and the fifteen entries of the unit
blueprint restated in student language. Mirrors the Jackson and
Reform study guide. The teacher key carries no blueprint tags."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
UNIT = os.path.dirname(HERE)
SPEC = open(os.path.join(HERE, "unit-spec.md")).read()

LESSON_TITLES = {
    1: "The Compromise of 1850 and the Fugitive Slave Act",
    2: "The Antislavery Argument at Full Voice",
    3: "The Kansas-Nebraska Act and Bleeding Kansas",
    4: "The Republican Party and Dred Scott",
    5: "The Debates, John Brown, the Election of 1860, and Secession",
    6: "The War Begins: Sumter to Antietam",
    7: "Emancipation and the War Transformed, 1863",
    8: "Total War and Appomattox",
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
    (1, "What question did California's application for statehood put to Congress in 1849, and what did Henry Clay propose in answer?",
     "California, peopled overnight by the gold rush, applied for statehood as a free state, which would break the Senate's balance of fifteen free states and fifteen slave states and leave the South a permanent minority in one house while its share of the other shrank. Zachary Taylor, a Louisiana slaveholder elected as a war hero, proposed admitting California and New Mexico at once and letting the territories skip the question. Henry Clay, seventy two and returned to the Senate in 1849, laid out his resolutions in January 1850, a package built to give each section a victory to carry home. The omnibus collapsed in July, Clay went home exhausted, and Stephen A. Douglas took the measures up one at a time and passed each with a different majority, Taylor's death that July putting Millard Fillmore, who would sign, in the presidency."),
    (1, "State the five terms of the Compromise of 1850 as they were finally enacted.",
     "California was admitted as a free state. Utah and New Mexico were organized as territories without a slavery restriction, their statehood constitutions to decide slavery when they came. The Texas boundary was settled and its debt assumed. The slave trade, not slavery itself, was ended in the District of Columbia. And a far stricter Fugitive Slave Act was enacted, the settlement's price and its poison. Both sections' newspapers called the package a final settlement of the slavery question, and northern statehouses began at once to pass the personal liberty laws that would make its enforcement a fight between jurisdictions."),
    (1, "How did the Fugitive Slave Act of September 18, 1850, conduct a rendition, and how did northern states answer it?",
     "A person accused of escaping slavery could be seized on an owner's affidavit and was heard before federal commissioners rather than judges. The accused was denied a jury trial and the right to testify. A commissioner was paid ten dollars when he remanded a prisoner and five when he freed one, every bystander was liable to be summoned into a posse, and aiding a fugitive, by feeding, hiding, or rescuing, was made a federal crime carrying heavy fines and prison. The northern states answered with personal liberty laws, statutes forbidding state officers to help in renditions, denying the use of state jails, and granting accused fugitives the jury trials and counsel that federal law denied them."),
    (2, "What happened to Anthony Burns in Boston in 1854, and what did the rendition show about enforcement in the North?",
     "Anthony Burns, a Virginia fugitive, was arrested in Boston in May 1854 and tried before a federal commissioner under the Fugitive Slave Act. He was remanded to slavery and marched to the ship that carried him back between lines of federal troops, while church bells tolled and buildings stood draped in mourning. The rendition was the Act's most famous northern spectacle. It showed that enforcing the law in a hostile city now required the army of the United States on its streets, and that every rendition staged the republic against itself before crowds who had come to watch slavery's officers do their work."),
    (2, "From what evidence did Harriet Beecher Stowe build Uncle Tom's Cabin, at what readers was its argument aimed, and how did the South answer the book?",
     "Stowe, who had lived eighteen years in Cincinnati across the river from Kentucky, built the novel from the slave narratives and from Josiah Henson's account in particular. Serialized in 1851 and published as a book in March 1852, it carried the narratives' evidence into northern parlors and aimed its argument at the Christian mother's conscience, showing slavery corrupting the enslaver's household as surely as it destroyed the enslaved one, with families parted at the auction block as its recurring wound. It became the best selling American novel of its century. Across the South it was banned, and southern writers answered it with a shelf of anti-Tom novels defending slavery, while translations carried it everywhere abroad."),
    (2, "Two texts survive of Sojourner Truth's speech at Akron in May 1851. Who wrote each one down, and when, and what does the difference teach about quoting the speech?",
     "Marius Robinson reported the speech for the Anti-Slavery Bugle, which printed his transcription in June 1851, weeks after Truth spoke. Frances Dana Gage, who had presided at the convention, published her version twelve years later, in 1863, and her version gave the speech its famous refrain and its dialect. The two texts are therefore not equal evidence. Robinson wrote at the time, Gage from memory in another decade and for another purpose. The lesson the unit draws is the historian's first question about any famous quotation: who wrote it down, and when. The 1851 text is the one that may be quoted with confidence as what Truth said at Akron."),
    (3, "Why did Stephen A. Douglas need Kansas and Nebraska organized in 1854, and what price did the South name for the bill?",
     "Douglas, chairman of the Senate's committee on territories, needed the two territories organized so that a transcontinental railroad could run west from Chicago. The South named its price: the Missouri Compromise line of 1820, thirty four years standing, which had barred slavery from the northern Louisiana Purchase lands, had to be repealed in so many words, so that the territories could decide slavery for themselves under Douglas's doctrine of popular sovereignty. The act of May 30, 1854, paid the price. The northern answer came in mass meetings and sermons, and the Whig Party, already strained, was dead within two years, while an anti-Nebraska coalition began gathering everyone the repeal had angered."),
    (3, "State what happened in Kansas in 1855 and 1856 that gave Bleeding Kansas its name.",
     "Free state settlers sent by New England emigrant aid societies and proslavery settlers backed from Missouri contested the territory from its opening. The territorial election of March 1855 was carried by Missourians who rode in, voted, and rode home, the border ruffians of free state naming, and the proslavery legislature they seated at Lecompton expelled its free state members. The free state settlers answered with a rival government at Topeka. In May 1856 a proslavery posse sacked Lawrence, destroying its presses and hotel, and two days later Congressman Preston Brooks beat Senator Charles Sumner nearly to death at his Senate desk for a speech against Kansas. Three nights after the sack, John Brown and his party killed five proslavery men at Pottawatomie Creek. Guerrilla war followed through 1856 and left some two hundred dead."),
    (3, "How was the Lecompton Constitution of 1857 offered to Kansas voters, and what did its fraud do to President Buchanan and to Douglas?",
     "The proslavery convention at Lecompton drafted a constitution protecting slavery and offered it in a referendum arranged so that even rejecting it protected the slavery already in the territory, so Kansas voters could not vote slavery out by voting the constitution down. President Buchanan endorsed the constitution. Douglas broke with his own president over it, because the fraud betrayed popular sovereignty itself, the doctrine on which his career stood: the people had not been left free to decide. Congress refused the constitution, the fight split the Democratic Party by section, and Kansas entered the Union at last as a free state in January 1861."),
    (4, "On what single plank was the Republican Party organized in 1854, and what did the plank leave untouched?",
     "The anti-Nebraska meetings of 1854 named themselves Republican and gathered ex-Whigs, Free Soilers, and anti-Nebraska Democrats on one plank every part of the coalition could hold: Congress must bar slavery from the federal territories. The plank left slavery untouched where state law protected it, in the fifteen slave states, and promised instead to put slavery, in the phrase Lincoln would make famous, in the course of ultimate extinction by fencing it in. The creed beneath the plank was free labor, the northern faith that labor was honorable, that the laborer had a right to rise by his work to property and independence, and that slavery degraded work and monopolized the common lands."),
    (4, "State the three holdings of the Dred Scott decision of March 6, 1857.",
     "Dred Scott had sued for his family's freedom on the ground that his owner's army postings had carried him to Illinois and to Fort Snelling, free soil both. Chief Justice Roger B. Taney, for a majority of seven, held first that Black people, enslaved or free, were not and could not be citizens of the United States. He held second that Scott's residence on free soil had not freed him. He held third that the Missouri Compromise had been unconstitutional from the start, because Congress had never had power to bar slavery from the territories. That third holding voided the Republican platform itself, the promise to do by law the very thing the Court now said no law could do."),
    (4, "What did Lincoln argue in the House Divided speech of June 16, 1858, and how did John C. Frémont's campaign of 1856 stand behind the argument?",
     "Accepting the Republican nomination for the Senate at Springfield, Lincoln argued that the government could not endure permanently half slave and half free, and charged that the Kansas-Nebraska repeal, the Dred Scott decision, and the administration's policy were parts of one design tending to make slavery national and perpetual. Frémont's campaign stood behind the warning as arithmetic. In 1856, the party's first national run, the Pathfinder had carried eleven of the sixteen free states while Buchanan won on Pennsylvania and the South. Both sections had read the same returns: a purely northern party could now come within one state of the presidency, and it would not stay short forever."),
    (5, "What question did Lincoln press on Douglas at Freeport in August 1858, and what did Douglas's answer cost him?",
     "Lincoln pressed one question through the seven debates: if the Supreme Court had held that neither Congress nor a territory could bar slavery, could a territory still keep slavery out? At Freeport, Douglas answered that it could, because slavery needed local police laws to survive, and a territory could defeat it by refusing to pass them. The Freeport Doctrine saved Douglas's Senate seat, since Illinois voters heard a territory kept free. It forfeited the South, whose leaders heard a senator teaching territories to nullify a Supreme Court decision, and who now demanded what his doctrine denied, a federal slave code for the territories, the demand on which the Democratic Party split in 1860."),
    (5, "What did John Brown do at Harpers Ferry on October 16, 1859, how did the raid end, and how did the two sections read Brown afterward?",
     "Brown and twenty one men, five of them Black, seized the federal arsenal at Harpers Ferry, Virginia, hoping to arm an enslaved rising. The rising did not come, the town's first casualty was a free Black railroad porter, Heyward Shepherd, shot by the raiders, and marines under Robert E. Lee stormed the engine house and captured Brown two days later. Virginia tried him for treason against the state and hanged him on December 2, 1859. His courtroom speech and his last written note, that the crimes of this guilty land would never be purged away but with blood, made him a martyr in northern church bells, and in southern minds the proof that abolition meant invasion, and militia companies formed across the South that winter."),
    (5, "How was Lincoln elected in 1860, and what did South Carolina's Declaration of the Immediate Causes say the break was about?",
     "Four parties contested the election. The Democrats split at Charleston and Baltimore over the southern demand for a federal slave code, nominating Douglas in the North and Breckinridge in the South, while Bell ran on the Union alone. Lincoln, nominated at Chicago on the platform of no extension, was elected with 39.8 percent of the popular vote and a majority of the electoral college, with not one electoral vote from the South and, in ten states, not even a place on the ballot. South Carolina seceded on December 20, 1860, and its declaration charged that the northern states had broken the constitutional compact by refusing their fugitive slave obligations, by nullifying the acts of Congress through their personal liberty laws, and by electing a president whose opinions and purposes were hostile to slavery. Six more states followed by February 1, the Crittenden Compromise failed, and Alexander Stephens stated the new government's cornerstone at Savannah that March: racial inequality, and slavery as the Black man's natural condition."),
    (6, "What opened the war at Fort Sumter in April 1861, and what did Lincoln's call for volunteers do to the Upper South?",
     "The federal fort in Charleston harbor was running out of provisions, and on April 12, 1861, Confederate batteries opened fire on it. The garrison surrendered on April 14. The next day Lincoln called for seventy five thousand volunteers to suppress the rebellion. The call forced the undecided slave states to choose, and Virginia, Arkansas, Tennessee, and North Carolina seceded rather than supply troops against the South, the Union's second secession. Delaware, Maryland, Kentucky, and Missouri stayed, held by occupation, political maneuver, and, in Kentucky, a neutrality both sides courted until it broke. The war the call assembled pitted the Union's twenty two million people, factories, railroads, and navy against the Confederacy's nine million, more than a third of them enslaved, and its cotton."),
    (6, "State the Anaconda Plan and the Confederacy's countering hope, and state what First Bull Run taught both governments.",
     "General Winfield Scott proposed to strangle the Confederacy: a naval blockade of its coast, proclaimed by Lincoln in April 1861, and a drive down the Mississippi that would split the Confederacy in two. Critics derided the plan as slow, but it was adopted in substance as the war became long. The Confederacy chose the defensive, hoping to outlast northern will and win European recognition on the strength of King Cotton, whose leverage collapsed as Britain turned to Indian and Egyptian cotton. On July 21, 1861, at First Bull Run near Manassas, excursion crowds from Washington watched a Confederate victory and a Union rout. The battle ended the hope of a ninety day war and taught both governments to build real armies."),
    (6, "What did Antietam settle and leave unsettled on September 17, 1862, and what did Lincoln do in the week that followed?",
     "Lee had invaded Maryland, and McClellan, holding a copy of Lee's lost orders, met him near Sharpsburg. The fighting of September 17 was the single bloodiest day in American history, some 22,700 casualties by the usual reckoning. Tactically the armies fought to a standstill, but Lee withdrew, so the first invasion of the North had ended, a strategic Union victory. It gave Lincoln the field he had waited for, and on September 22 he issued the Preliminary Emancipation Proclamation, warning that on January 1 the enslaved people in the rebellious states would be declared free. Two days later his proclamation of September 24 suspended habeas corpus along the lines of military operations, the war's cost to civil liberty stated in the same week as its new purpose."),
    (7, "How did enslaved people reach freedom before any proclamation freed them, and what legal fiction carried them?",
     "From the war's first spring, enslaved people freed themselves by walking to the Union lines. At Fort Monroe in May 1861, General Benjamin Butler refused to return three men who had escaped to his lines, holding them as contraband of war, property seized from the enemy rather than returned to him. The fiction let the Union army absorb the labor of the people who came while the government still insisted the war was only for the Union. Under it, hundreds of thousands reached freedom before any proclamation freed them, with the First Confiscation Act and the District of Columbia's compensated emancipation of April 1862 following behind the fact the fugitives had made."),
    (7, "State what the Emancipation Proclamation of January 1, 1863, did, what it left untouched, and what it changed in the war.",
     "The Proclamation, issued in preliminary form on September 22, 1862, declared free the enslaved people in the states and parts of states then in rebellion. It left slavery untouched in the loyal border states, Delaware, Maryland, Kentucky, and Missouri, and in the occupied areas it exempted. Critics charged that it freed people where the Union could not yet enforce freedom and stood aside where it could. Its supporters answered from the record: it struck at the rebellion's labor system, since every person who reached Union lines was now free by law and not by fiction, it ended any European sympathy for the South, and it opened the Union army and navy to Black enlistment, under which some 180,000 Black soldiers served by the war's end."),
    (7, "What happened at Gettysburg and Vicksburg in the first days of July 1863, and what did the 54th Massachusetts prove that same month?",
     "Lee invaded the North a second time, and the Army of the Potomac under Meade stopped him at Gettysburg, Pennsylvania, on July 1 to 3, in the war's greatest battle, at a cost of some fifty thousand casualties to the two armies. The day after the battle ended, on July 4, Vicksburg, the Mississippi River fortress, surrendered to Grant after a six week siege, giving the Union the whole river and splitting the Confederacy in two. That Independence Day stands as the war's turning point. Later in July the 54th Massachusetts, the first Black regiment raised in the North, assaulted Fort Wagner at the cost of Colonel Robert Gould Shaw and nearly half the regiment, and answered in action the claim that Black men would not fight."),
    (8, "How did Grant direct the war from March 1864, and what did Sherman's March to the Sea do?",
     "Grant, made general in chief in March 1864, directed coordinated campaigns across every theater at once, holding that the Confederacy's armies, not its cities, were the objective, and he paid the Overland campaign's ledger through the Wilderness, Spotsylvania, and Cold Harbor to the siege of Petersburg. Sherman took Atlanta in September 1864, a fall that arrived in time to save Lincoln's reelection, then cut loose from his supply lines. From November into December 1864 some sixty two thousand Union soldiers marched from Atlanta to Savannah living off the country, destroying the railroads, mills, and stores in a corridor sixty miles wide, total war carried against the resources and will that sustained the Confederate armies, and Sherman presented Savannah to Lincoln as a Christmas gift."),
    (8, "State the terms Grant gave Lee at Appomattox on April 9, 1865, and what the Thirteenth Amendment had already done that winter.",
     "Richmond was evacuated and burned on April 2 and 3, Lee's retreat was cut off at Appomattox Court House, and on April 9, 1865, Lee surrendered the Army of Northern Virginia. Grant's terms, generous by Lincoln's standing instruction, paroled the soldiers home, let officers keep their sidearms, and let the men take their horses home for the spring planting, and Grant ordered no rejoicing over a fallen foe. The surrender effectively ended the Civil War. That winter, on January 31, 1865, Congress had passed the Thirteenth Amendment, which the states ratified in December: slavery and involuntary servitude were abolished everywhere in the United States, except as punishment for a crime, the only one of the three Reconstruction amendments adopted while the war still ran."),
    (8, "What does the Second Inaugural Address of March 4, 1865, name as the war's cause and its meaning, and what does it ask the country to do at the end, and what stood unanswered when Lincoln was killed?",
     "Lincoln named American slavery as the offense, one eighth of the whole population held as slaves and making war to strengthen and perpetuate their interest, and read the war itself as the woe due to those by whom the offense came, a judgment falling on both sections, North and South alike. He closed by asking the country to bind up its wounds and to care for the soldier, his widow, and his orphan. Five weeks later, on April 14, Booth shot him at Ford's Theatre, and he died on April 15. The war had settled that the Union was indivisible and that slavery was destroyed as a system. It left standing, exactly where April 1865 left them, the freed people's claims to land, to safety, and to the vote, which the next unit takes up."),
]

FRAME = [
    "Compromise over slavery failed in stages, and each stage narrowed the ground the next settlement could stand on. The Compromise of 1850 held the Union together by enacting its terms bill by bill, but its enforcement clause, the Fugitive Slave Act, put federal commissioners, posses, and troops on northern streets and taught a generation of northerners slavery as a presence in their own towns. The antislavery writers gave that experience its argument, Stowe carrying the slave narratives' evidence into northern parlors, Truth and Jacobs bearing witness in their own persons, Douglass auditing the founding's promises against the slave's present. The Kansas-Nebraska Act then repealed the Missouri line that had bounded slavery's spread for thirty four years, and popular sovereignty, offered as a way to take the question out of Congress, produced in Kansas two governments, a sacked town, a beaten senator, and a small war. A new party rose on the single promise to bar slavery from the territories, and the Supreme Court answered by voiding that promise and denying Black citizenship outright. The debates of 1858 fixed the argument's terms, Brown's raid convinced the South that abolition meant invasion, and in 1860 a president pledged only against slavery's extension was elected without one southern electoral vote. The seceding states said in their own declarations what the break was about: the North's refusal to return fugitives, its hostility to slavery, and a government they held had been made destructive of slavery's protection, and their vice president named slavery the new government's cornerstone.",
    "The war the break caused began as a war for the Union and became a war against slavery because slavery was the rebellion's labor system and its cause. Sumter forced the choice, Bull Run ended the hope of a short war, and the rival strategies, blockade and the Mississippi against endurance and King Cotton, ran the contest toward the longer arithmetic of the North's numbers, factories, and navy. The enslaved moved first: walking to the Union lines under the contraband fiction, they made emancipation a military fact before it was a policy, and Antietam gave Lincoln the standing to make it policy. The Proclamation of January 1, 1863, freed the enslaved in the rebellious states, left the loyal border states untouched, and opened the army's ranks, and some 180,000 Black soldiers thereafter fought for the Union that had enslaved many of them, for equal pay as well as for victory. Gettysburg and Vicksburg in July 1863 ended the Confederacy's hope of winning on northern soil or holding its western half, and the Gettysburg Address restated the war as a test of the proposition that all men are created equal. Grant's coordination and Sherman's march then wore the Confederacy down by arithmetic and by destruction, until Lee's surrender at Appomattox on April 9, 1865, on terms that sent his soldiers home with their horses for the spring planting.",
    "What the war settled can be stated in two sentences, and Lincoln stated its verdict in the Second Inaugural five weeks before his death. The Union is indivisible: no state may dissolve it by its own act, and the question secession raised was answered by arms and has not been reopened by law. Slavery is destroyed as a system: the Proclamation broke it in the rebellious states as a war measure, and the Thirteenth Amendment, passed while the war still ran, abolished it everywhere in the United States. Lincoln's own accounting named American slavery as the offense and the war as its woe, a judgment on both sections, and closed by asking the country to bind up its wounds. What the war left open is the rest of freedom's content. The Proclamation and the amendment ended the legal condition of slavery and said nothing about the freed people's land, their safety in the states that had held them, or their place at the ballot box, and Annie Davis of Maryland, writing the president in August 1864 to ask whether she was free, measured the settlement at its edge, in a loyal state the Proclamation had not named. Those questions stood exactly where April 1865 left them, and answering them is the next unit's work.",
]

BLUEPRINT_STUDENT = [
    "Explain the Compromise of 1850, Clay framing the settlement in January 1850 after his earlier settlements of 1820 and 1833, the failure of his single omnibus, and Douglas passing the five measures bill by bill, California free, Utah and New Mexico organized without a slavery restriction, the Texas boundary and debt settled, the District of Columbia slave trade ended, and the stricter Fugitive Slave Act enacted.",
    "Explain the Fugitive Slave Act of September 18, 1850, rendition on an owner's affidavit before federal commissioners, the accused denied a jury trial and the right to testify, the ten dollar and five dollar fees, the crime of aiding a fugitive, and the northern answer in the personal liberty laws, the Underground Railroad, Harriet Tubman, and the rendition of Anthony Burns.",
    "Explain the antislavery argument of Uncle Tom's Cabin, Stowe building the novel from the slave narratives and Josiah Henson's account, its appeal to the conscience of its northern readers, its standing as the best selling American novel of its century, and the bans and anti-Tom novels with which the South answered it.",
    "Explain witness and resistance in the 1850s, Sojourner Truth at Akron in 1851 and the two surviving texts of her speech, Harriet Jacobs's narrative written after seven years in hiding, the slave narrative as the movement's evidence, Seward's higher law doctrine, and the fugitive rescues and renditions that made enforcement a public spectacle.",
    "Explain the Kansas-Nebraska Act of May 30, 1854, Douglas's railroad purpose, popular sovereignty as the doctrine that a territory's people should decide slavery for themselves, and the repeal of the Missouri Compromise line of 1820 that had barred slavery from the northern Louisiana Purchase lands.",
    "Explain Bleeding Kansas, the border ruffians who carried the election of March 1855, the rival governments of the Lecompton legislature and free state Topeka, the sack of Lawrence, the caning of Charles Sumner, John Brown's Pottawatomie killings, and the Lecompton Constitution whose referendum protected slavery even in rejection and split Buchanan from Douglas.",
    "Explain the Republican Party organized in 1854 from ex-Whigs, Free Soilers, and anti-Nebraska Democrats, the single plank that Congress must bar slavery from the federal territories, the free labor creed beneath the plank, and John C. Frémont carrying eleven of the sixteen free states in 1856.",
    "Explain Dred Scott v. Sandford, Chief Justice Taney's holdings that Black people could not be citizens, that residence on free soil had not freed Scott, and that Congress had never had power to bar slavery from the territories, and the answers the decision drew, the Curtis dissent, Douglass, and Lincoln's House Divided speech of June 1858.",
    "Explain the Lincoln-Douglas debates of 1858, seven open air meetings across Illinois, the question Lincoln pressed at Freeport about the Dred Scott decision, and the Freeport Doctrine, Douglas's answer that a territory could keep slavery out by refusing the local police laws slavery needed, and what that answer cost him in the South.",
    "Explain John Brown's raid on Harpers Ferry in October 1859 and his hanging on December 2, the four party election of 1860 that made Lincoln president on 39.8 percent of the popular vote with no southern electoral vote, the failure of the Crittenden Compromise, the organization of the Confederate States under Jefferson Davis, and secession defended in South Carolina's declaration.",
    "Explain the war's opening, Fort Sumter bombarded on April 12, 1861, and surrendered on April 14, the second secession that followed Lincoln's call for volunteers, First Bull Run on July 21, 1861, and the end of the short war hope, and the rival strategies, Scott's Anaconda Plan of blockade and the Mississippi against the Confederacy's hope of outlasting northern will on King Cotton.",
    "Explain the war to Antietam, McClellan building the Army of the Potomac and the caution that ended his command, the Peninsula campaign and Second Bull Run, Grant and Farragut in the West and Shiloh's price, Lincoln's suspension of habeas corpus along the military lines, and September 17, 1862, the bloodiest single day, which ended the first invasion of the North and gave Lincoln ground for the Emancipation Proclamation.",
    "Explain emancipation, Butler's contraband doctrine at Fort Monroe in May 1861 and the enslaved people who freed themselves by reaching Union lines, the Emancipation Proclamation of January 1, 1863, and what it left untouched in the loyal border states, the United States Colored Troops and their fight for equal pay, and the 54th Massachusetts at Fort Wagner.",
    "Explain 1863 as the war's turning year, Gettysburg on July 1 to 3, 1863, ending Lee's second invasion, Vicksburg surrendering to Grant on July 4 and giving the Union the whole Mississippi, and the Gettysburg Address of November 19, 1863, restating the war as a test of the proposition that all men are created equal and rededicating the living to the unfinished work.",
    "Explain total war and the end, Grant general in chief from March 1864 and the coordinated campaigns, Sherman's taking of Atlanta and the March to the Sea, the Thirteenth Amendment passed by Congress on January 31, 1865, Lee's surrender at Appomattox Court House on April 9, 1865, and the Second Inaugural Address naming American slavery as the war's offense and the war as its woe.",
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
    for lesson_terms in terms.values():
        for term, dfn in lesson_terms:
            assert "\u2014" not in dfn and "\u2013" not in dfn, term
    P = []
    P.append("<!DOCTYPE html>")
    P.append('<html lang="en"><head><meta charset="utf-8">')
    P.append("<title>Study Guide: Sectional Crisis and Civil War</title>")
    P.append(f"<style>{CSS}</style></head><body>")
    P.append('<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>')
    P.append('<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>')
    P.append("<h1>Study Guide: Sectional Crisis and Civil War</h1>")
    P.append('<p class="directions"><strong>Directions:</strong> Complete Part 1 from your guided notes and readings, then answer the Part 2 questions in your own words. Part 3 tells the unit as one story and lists what the test will ask you to show. The unit test is built from this guide. Bring questions about anything you cannot answer to the review day.</p>')
    P.append("<p><strong>Unit question:</strong> How did compromise over slavery finally fail, and what did the war it caused settle about slavery and the Union, and what did it leave open?</p>")
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
