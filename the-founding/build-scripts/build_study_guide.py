#!/usr/bin/env python3
"""Build the Founding review study guide from the verbatim vocabulary
in build-scripts/unit-spec.md, plus 24 review questions with a full
key, a short frame passage, and the fifteen entries of the unit
blueprint restated in student language. Mirrors the Colonial America
study guide. The teacher key carries no blueprint tags."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
UNIT = os.path.dirname(HERE)
SPEC = open(os.path.join(HERE, "unit-spec.md")).read()

LESSON_TITLES = {
    1: "The Imperial Crisis: Taxation and Resistance", 2: "From Protest to Revolution: 1773 to 1776",
    3: "Declaring Independence", 4: "The War for Independence",
    5: "Winning and Losing: The War's Home Fronts and Its Peoples", 6: "The Confederation and the Road to Philadelphia",
    7: "The Constitution and the Great Compromises", 8: "Ratification and the Bill of Rights",
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
    (1, "Why did Britain tax the colonies after 1763, and what made the Stamp Act a break with earlier practice?",
     "Britain's national debt had nearly doubled in the French and Indian War, and its ministers resolved that the colonies should pay for their own defense, a standing army of some ten thousand soldiers in North America. Earlier British taxes touching the colonies had fallen on trade. The Stamp Act of March 1765 fell directly on the colonies themselves, taxing printed paper, newspapers, pamphlets, legal documents, licenses, and playing cards, collected through stamped paper sold by royal distributors, and so falling hardest on the printers, lawyers, and merchants who ran the colonies' newspapers and assemblies."),
    (1, "How did the colonists answer the Stamp Act in argument, in combination, and in the streets, and what did Parliament do in March 1766?",
     "In argument, Patrick Henry's Virginia Resolves of May 1765 claimed that only the colonists' own assemblies could tax them, and the Stamp Act Congress of October 1765 brought nine colonies together at New York to declare their rights and grievances in one voice. In combination, merchants organized boycotts of British goods and households made them real, women spinning and weaving homespun. In the streets, the Sons of Liberty hung tax men in effigy, wrecked the Massachusetts lieutenant governor's house, and drove every stamp distributor in America to resign before November 1. Parliament repealed the act in March 1766, pressed by the boycott and by British merchants' petitions, after Franklin testified the colonies would never submit."),
    (1, "Why did repeal in 1766 not end the quarrel, and how did the dispute end in blood at Boston in 1770?",
     "Parliament passed the Declaratory Act the same day as repeal, claiming power to legislate for the colonies in all cases whatsoever, so the principle survived the tax. The Townshend Acts of 1767 then taxed imported glass, lead, paint, paper, and tea, with the revenue assigned to pay royal governors and judges, striking at the assemblies' power of the purse, and Dickinson's Letters from a Farmer answered that a tax for revenue was a tax whatever its form. Troops sent to Boston in 1768 produced two years of street friction, and on March 5, 1770 soldiers surrounded by a taunting, icy crowd fired and killed five men, among them Crispus Attucks. John Adams defended the soldiers at trial, two were convicted of manslaughter and six acquitted, and the Townshend duties were repealed that year except the tax on tea."),
    (2, "Why was the Tea Act a trap for the colonies even though it lowered the price of tea?",
     "The East India Company, drowning in unsold tea and near bankruptcy, was licensed by the Tea Act of May 1773 to sell directly in the colonies through its own agents, cutting out colonial merchants, at a price lower than before even with the Townshend duty still on it. Every cup drunk cheap would concede Parliament's right to tax, and the colonies saw the bargain whole. Charleston let the tea rot in a warehouse, New York and Philadelphia turned the ships back, and Boston's governor Hutchinson refused to let the Dartmouth leave without unloading, which set the stage for December 16."),
    (2, "How did Parliament answer the Tea Party, and how did the colonies answer together in 1774?",
     "Parliament's acts of the spring of 1774, which colonists named Intolerable, closed Boston's port to trade until the tea was paid for, rewrote the Massachusetts charter to put its council and town meetings under royal control, let accused royal officials be tried outside the colony, and imposed a new Quartering Act, with the Quebec Act read in the colonies as a fifth blow. The colonies voted supplies to blockaded Boston from as far as South Carolina, and the First Continental Congress met at Philadelphia in September and October 1774, fifty six delegates from twelve colonies, issuing a Declaration and Resolves and adopting the Continental Association, a boycott of British imports and then exports enforced by elected committees in every county and town, which in enforcing it quietly became a second government."),
    (2, "What happened on April 19, 1775, and how do the two records the lesson carries tell it differently?",
     "On the night of April 18, 1775, General Gage sent some seven hundred regulars to seize the military stores at Concord, Paul Revere and William Dawes rode to warn the country, and the militia under Captain Parker stood on Lexington green at dawn. Lieutenant Barker's diary, a British officer's account, tells of a shot he could not assign and a volley his men fired without orders. The Massachusetts militiamen's sworn testimony, taken a week later, blames the regulars for firing first on men already dispersing. Eight Americans died at Lexington, the fight continued at Concord's North Bridge, and the march back to Boston under fire from behind walls and trees cost some 273 British casualties against about 95 American, the standard counts, and by nightfall thousands of militia had Boston besieged."),
    (3, "What did Common Sense argue that earlier colonial writing had not, and why did it reach so far?",
     "Through 1775 the resistance had framed its quarrel as a defense of British liberties against Parliament and the king's ministers. Paine's pamphlet, published at Philadelphia in January 1776, argued the case had been miscast, that the villain was not this tax or that minister but monarchy and hereditary succession themselves, corrupt in Scripture and absurd in nature, an island presuming to govern a continent. Its plain biblical and tavern language carried republican theory to readers who had never opened Locke, and it sold, by the estimates historians work from, well over one hundred thousand copies within months in a country of two and a half million."),
    (3, "How was the Declaration drafted, and what did Congress cut from Jefferson's text?",
     "On June 7, 1776, Richard Henry Lee moved that the colonies are, and of right ought to be, free and independent states. A committee of five, Adams, Franklin, Sherman, Livingston, and Jefferson, was charged with the drafting, and Jefferson did the writing at a portable desk in a rented room. Congress then cut about a quarter of his text, tightening the argument and striking, among other passages, his charge that the king had waged cruel war against human nature itself in the slave trade and had blocked every colonial attempt to end it, a passage removed at the insistence of South Carolina and Georgia, with northern delegates whose ports profited from the trade unwilling to press it. Jefferson's rough draft, with the changes visible, survives as the record of those choices."),
    (3, "State the Declaration's argument in its own order, from the preamble to the conclusion.",
     "The preamble states self evident truths, that all men are created equal and hold rights no government gives and none may rightly take, life, liberty, and the pursuit of happiness among them, that governments are instituted to secure those rights and draw their just powers from the consent of the governed, and that a people may alter or abolish a government destructive of those ends. The evidence follows, a long train of abuses charged against the king alone, because it was the king's bond that had to be dissolved, refusing assent to laws, dissolving assemblies, keeping standing armies, cutting off trade, imposing taxes without consent, hiring foreign mercenaries, exciting domestic insurrections among the colonists, and bringing on the inhabitants of the frontiers the merciless Indian Savages, a phrase the document's universal language stands against inside the same text. The conclusion absolves the colonies from all allegiance and declares them free and independent states, and Congress voted independence on July 2 and adopted the text on July 4."),
    (4, "What was Washington's strategy, and why did the arithmetic of the war require it?",
     "Britain held the world's strongest navy, a funded treasury, a professional army, and hired German auxiliaries. Against it stood a Congress that could not tax, an army enlisted by the year and often unpaid, militia who served near home and went home, and a currency already sliding. Washington's strategy followed from the arithmetic. The Americans could lose every city and still win by keeping an army in being, while Britain had to destroy that army or hold a continent, and could do neither cheaply. The strategy was tested at once, in the loss of New York in 1776 and the long retreat across New Jersey, and vindicated in the counterstrokes at Trenton on Christmas night 1776 and Princeton on January 3, 1777, which arrived when the Revolution was within weeks of dissolving."),
    (4, "Why was Saratoga the war's turning point, and what did the alliance that followed change?",
     "The British plan of 1777 was to cut New England off by taking the Hudson, Burgoyne marching south from Canada while Howe, instead of meeting him, sailed to take Philadelphia. Burgoyne, his supply line stretched and his army cut up at Bennington and Freeman's Farm, surrendered some 5,800 men at Saratoga on October 17, 1777, the standard count. The victory did the war's diplomatic work, because it proved to France that the Americans could beat a British army in the field. The Treaty of Alliance of February 6, 1778 brought France into the war with money, ships, and soldiers, Spain followed against Britain in 1779, and the war widened to the Caribbean, Gibraltar, and India, while at home the army that wintered at Valley Forge came out drilled by Baron von Steuben into a professional force."),
    (4, "How was the war finally won in the South and at Yorktown, and what did the Treaty of Paris settle?",
     "The British shifted their weight south after 1778, taking Savannah and then Charleston in May 1780 with an entire American army, the worst American defeat of the war, and destroying a second army at Camden. The backcountry answered, militia destroying a Loyalist force at King's Mountain in October 1780 and Daniel Morgan wrecking Tarleton's legion at Cowpens in January 1781, while Nathanael Greene wore Cornwallis down through Guilford Courthouse and a campaign of retreat. Cornwallis marched into Virginia to refit at Yorktown, where Washington and Rochambeau closed around him with some seventeen thousand American and French troops while the French fleet under de Grasse sealed the Chesapeake, and he surrendered his army of some eight thousand on October 19, 1781, the figures stated as the standard counts. The Treaty of Paris of September 3, 1783 recognized the United States as free, sovereign, and independent, granted a boundary at the Mississippi and the Great Lakes, and set terms on debts and Loyalist property that the states would honor unevenly."),
    (5, "What did Dunmore's Proclamation offer, who answered it, and how did Black Americans serve on the American side?",
     "Virginia's royal governor Dunmore, driven from Williamsburg to a ship, proclaimed freedom in November 1775 to enslaved people and indentured servants held by rebels who would bear arms for the king. Some hundreds reached his lines and served in an Ethiopian Regiment, most dying of smallpox and fever in the camps, and across the war thousands of enslaved people ran to British lines wherever the armies passed. On the American side, Black men were barred from the Continental Army at first on the protests of slaveholders, then enlisted as manpower ran short, some five thousand serving in all, the standard estimate, the First Rhode Island Regiment of 1778 raised substantially from enslaved men who earned freedom by enlisting, and Black sailors served in both navies."),
    (5, "How did women carry the war, in households, in camps, and in a few cases in the ranks?",
     "At the household level women ran farms and shops with husbands, sons, and laborers gone, boycotted British cloth and spun homespun as political acts, and raised money door to door, as the women of Philadelphia did in 1780 to fund shirts for the army. The camp followers, women and children numbering in the thousands with both armies, cooked, washed, nursed, sewed, and carried water and cartridges under fire for rations and little or no pay, and the armies could not have moved or fed themselves without them. A few women fought outright. Margaret Corbin was wounded manning a cannon at Fort Washington in 1776 and pensioned by Congress, and Deborah Sampson enlisted in 1782 as Robert Shurtliff, served over a year in the light infantry, was wounded, and was honorably discharged when a fever's treatment discovered her sex. Mary Ludwig Hays carried water to the guns at Monmouth in 1778, and her story hardened over the following century into the legend of Molly Pitcher."),
    (5, "How did the war divide Native nations and the Loyalists, and where did the peace leave each?",
     "The Haudenosaunee Confederacy broke on the question of the war, the Oneida and Tuscarora siding with the Americans, the Mohawk, Seneca, Cayuga, and most Onondaga with the British under leaders including Joseph Brant, who fought to use the British alliance as a shield for his people's land. Washington's Sullivan expedition of 1779 burned about forty Seneca and Cayuga towns and their stored corn and drove thousands into a starving winter at Niagara. The Loyalists, perhaps a fifth of the white population, the conventional estimate, faced test oaths, tarring and feathering, confiscation, and banishment, and some sixty thousand or more left the new United States at the peace, an estimate, among them some three thousand Black Loyalists recorded in the Book of Negroes at New York in 1783, many of whom moved on in 1792 to Sierra Leone. The reckoning at home included freedom petitions from the enslaved, Vermont's constitution of 1777 barring adult slavery, Pennsylvania's gradual emancipation act of 1780, and the Massachusetts courts ending slavery in 1783."),
    (6, "How were the Articles of Confederation designed, and why did a revolutionary generation design them so weakly?",
     "The Articles were drafted by Congress in 1777 and ratified in 1781, held up four years by Maryland's refusal until the landed states surrendered their western claims. They joined the thirteen states in a firm league of friendship, one vote per state, with a Congress that could declare war, make treaties, coin money, and run a post office, but could neither levy a tax nor regulate commerce nor compel a state, every act of consequence needing nine states and every amendment needing all thirteen. The weakness was a design with reasons. A generation that had just fought a distant legislature's taxes built a government that could not tax, and kept sovereignty where they believed it was safe, in the states."),
    (6, "What did the Confederation accomplish in the West, and why is the Northwest Ordinance called both its monument and its contradiction?",
     "The Confederation Congress won and administered the peace and negotiated the land cessions that created a national domain. The Land Ordinance of 1785 set the survey of townships and sections that still grids the Midwest and reserved a section of every township for schools. The Northwest Ordinance of July 13, 1787 built the machine by which territories became states on equal footing with the original thirteen, guaranteed their inhabitants' civil liberties, and barred slavery from the whole territory north of the Ohio. It stands as the Confederation's monument and its contradiction in one document, because freedom's territory was surveyed across land whose Native owners had never sold it. The same decade also produced Virginia's Statute for Religious Freedom, passed in 1786, disestablishing the church and protecting religious opinion from compulsion."),
    (6, "How did Shays's Rebellion grow out of the states' money troubles, and what did it set in motion?",
     "War debts were held by speculators who had bought soldiers' certificates for pennies, state taxes were levied in hard money to pay them, and farmers in the western counties faced foreclosure and debtors' prison, while Massachusetts chose the hard road of heavy taxes in specie to pay its debt in full. From August 1786 crowds of indebted farmers, many of them Continental veterans, under leaders including Daniel Shays, closed the courts at Northampton, Worcester, and Springfield to stop foreclosure judgments. A militia financed by private subscription among Boston merchants scattered the rebels at the Springfield arsenal in January 1787, where four men died, and broke the movement by February, after which the legislature eased the taxes and the voters turned the governor out. The fear the rebellion lit among the propertied gave the movement already under way its mandate, from the Annapolis Convention's call of September 1786 to the convention that met at Philadelphia in May 1787."),
    (7, "How did the Virginia and New Jersey Plans differ, and what deadlock did they produce?",
     "Congress had authorized a convention for the sole and express purpose of revising the Articles, and the Virginia delegation instead proposed, through Edmund Randolph, a wholly new national government. The Virginia Plan, drafted chiefly by Madison, set a legislature of two houses apportioned by population or wealth, choosing an executive and a judiciary, empowered to legislate wherever the states were incompetent and to strike down state laws that crossed the national ones, a big state plan that told the small states their equal votes were the price. The New Jersey Plan of June 15 kept a single house with equal votes and patched the Articles with powers to tax and to regulate trade. The weeks of deadlock that followed brought the Convention on July 2 to a tie on equal representation in the second house and near dissolution."),
    (7, "What did the Great Compromise settle, and what did the settlements on slavery settle alongside it?",
     "The Great Compromise, the Connecticut delegation's settlement adopted July 16 by a single vote's margin in a five to four division of states, set a House of Representatives apportioned by population and elected by the people for two years, originating all money bills, and a Senate of two from every state, chosen by the state legislatures for six. It fixed the union's double nature, a people in one house and states in the other, into the government's frame. Alongside it, the Convention counted each enslaved person as three fifths of a person for both representation and direct taxation, reaching back to a Confederation tax formula of 1783, so slavery, unnamed anywhere in the document, was built into the House's apportionment and through it into the electoral college and the presidency. The document further barred Congress from ending the Atlantic slave trade before 1808 and required the return of persons held to service escaping into free states."),
    (7, "What was left out of the Constitution in September 1787, and why did the omission matter?",
     "On September 12 George Mason moved that a bill of rights be prepared by committee, and the Convention, tired and holding that the states' own declarations of rights sufficed, refused without a single state in favor. Mason, Elbridge Gerry, and Edmund Randolph carried the omission into the ratification fight as the refusal that cost the document their signatures, and the missing bill of rights became the Anti-Federalists' strongest objection. What the finished document claimed instead stands in its Preamble, written last by the Committee of Style, beginning not with the states' names, as the Articles had, but with We the People of the United States. Franklin's closing speech of September 17 asked every member to doubt a little of his own infallibility and sign, thirty nine delegates signed and three refused, and the document went to the states needing nine of thirteen to take effect."),
    (8, "State Madison's argument in Federalist No. 10, and why it reversed what republican theory had taught.",
     "Madison defined a faction as a group of citizens, a majority or a minority, united by a passion or an interest harmful to the rights of others or to the whole community. Its causes could not be removed without removing liberty itself, which feeds faction as air feeds fire, so its effects had to be controlled. A small republic offered no control, because a majority faction could form and rule at once. An extended republic multiplied parties and interests until an unjust majority could rarely find itself, and representation refined the public voice through chosen citizens. The essay is a defense of bigness itself as liberty's protection, the opposite of everything republican theory had taught since Montesquieu, and Federalist No. 51 added the machinery, ambition made to counteract ambition, so a government controlling the governed would be obliged to control itself."),
    (8, "State the Anti-Federalist case as Brutus made it, and name the objection that outlasted all the others.",
     "Brutus, in No. 1, answered that history and Montesquieu agreed a free republic could survive only in a small territory of shared manners. A government of thirteen million people across a continent, armed with the necessary and proper clause and a supremacy clause that overrode state law, holding a standing army and a power to tax every article of life, would consolidate by slow degrees into the very thing the Revolution had been fought against, and its distance from the people would make it a government of strangers. With the argument about size stood the objection that outlasted all the others, that the new frame carried no bill of rights, no written fence around speech, press, religion, juries, and arms, at the moment it created the strongest government Americans had ever lived under."),
    (8, "How did ratification succeed state by state, and how did the contest end in 1791?",
     "Delaware ratified first and unanimously on December 7, 1787, Pennsylvania within the week, New Jersey and Georgia unanimously, and Connecticut in January. Massachusetts in February 1788 invented the settlement that saved the document, ratifying unconditionally while recommending amendments the first Congress should take up, carried 187 to 168. Maryland and South Carolina followed, and New Hampshire in June became the ninth and decisive state. Virginia ratified in June by 89 to 79 with amendments recommended, and New York, where the Federalist essays had been written to win, ratified 30 to 27 in July after news arrived that the Constitution was already beyond recall. North Carolina and Rhode Island waited outside, Rhode Island not ratifying until May 1790 and then by two votes. Madison, who had called a bill of rights unnecessary during ratification, steered the amendments through the First Congress, twelve went to the states, and ten were ratified by December 15, 1791."),
]

FRAME = [
    "The unit opens with the bill for victory. Britain came out of the French and Indian War holding Canada and a national debt nearly doubled, and its ministers resolved that the colonies should pay for their own defense. The Stamp Act of 1765 taxed the colonies directly for the first time, and the colonists answered in three registers at once, in argument from their assemblies and the Stamp Act Congress, in combination through boycotts that households made real, and in crowds that drove every stamp distributor to resign. Parliament repealed the act in 1766 and claimed in the Declaratory Act the power to legislate for the colonies in all cases whatsoever, so the quarrel survived its first tax. The Townshend duties, the troops at Boston, and the killings of March 5, 1770 followed, then the Tea Act's cheap trap, the tea in Boston Harbor, the Intolerable Acts, the First Continental Congress, and the shots at Lexington and Concord in April 1775.",
    "What turned a resistance into a revolution was an argument. Common Sense told ordinary readers in plain language that monarchy itself was the enemy, and the Declaration of Independence stated the standard the new nation would be judged by, government by consent for the protection of equal rights, in words capacious enough that the people it left out could and did quote them back. The war that followed was won by endurance as much as by battle, by Washington's refusal to let his army be destroyed, by Saratoga and the French alliance it won, by the backcountry's answer in the South and the trap at Yorktown, and it was fought and paid for by peoples the battle narratives leave at the edge, Black Americans who read the era's promises against their own condition and acted on both sides, women who ran the home front and in some cases the guns, Native nations who chose their sides for reasons of their own, and Loyalists who lost their country for keeping faith with the old one.",
    "The peace left the building to do. The Articles of Confederation, a league of sovereign states that could not tax, won the West its ordinances and the republic its first great statute of religious freedom, and then failed the tests of debt, trade, and order that Shays's Rebellion made visible. Fifty five men at Philadelphia answered with a frame of divided and checked power, a House of the people and a Senate of the states, and compromises that built slavery into the government's arithmetic while leaving a bill of rights out. The ratification contests of 1787 and 1788 forced the argument into the open, Madison's defense of the large republic against Brutus's warning of consolidation, and the skeptics won the settlement's final piece, the ten amendments ratified by December 1791. The government the quarrel of 1763 had made necessary stood constituted, and every question that built it stood open.",
]

BLUEPRINT_STUDENT = [
    "Explain why Britain taxed the colonies after 1763, what the Stamp Act taxed, and how the colonists resisted it in argument, in boycotts, and in the streets.",
    "Explain why repeal in 1766 did not end the quarrel, what the Townshend Acts taxed and paid for, and what happened at Boston on March 5, 1770.",
    "Explain why the Tea Act angered the colonies even though it lowered the price of tea, what happened in Boston Harbor on December 16, 1773, and how the Intolerable Acts answered it.",
    "Explain what the First Continental Congress did in 1774, what happened at Lexington and Concord on April 19, 1775, and how the two sides' records of that day differ.",
    "Explain what Common Sense argued about monarchy itself, and why a short pamphlet in plain language could move so many readers toward independence.",
    "State the Declaration of Independence's argument in its own order, name the charges it laid against the king, and explain what Congress cut from Jefferson's draft and why.",
    "Explain how the Continental Army survived the war's first years, why Saratoga was the turning point, and what the French alliance brought to the war.",
    "Explain how the southern campaign and the trap at Yorktown ended the fighting, and what the Treaty of Paris of 1783 settled.",
    "Explain what the war offered and what it cost Black Americans, women, and Native nations, using Dunmore's Proclamation, the First Rhode Island Regiment, and the Sullivan expedition as evidence.",
    "Explain how the war was paid for and carried at home, what inflation did to Continental money, and what happened to the Loyalists when the war ended.",
    "Explain how the Articles of Confederation divided power, what Congress could and could not do under them, and what the Land Ordinance of 1785 and the Northwest Ordinance built in the West.",
    "Explain how debt and hard money demands produced Shays's Rebellion, how Massachusetts answered it, and how the crisis led through Annapolis to the call for a convention at Philadelphia.",
    "Explain how the Virginia Plan and the New Jersey Plan differed, what deadlock they caused at the Convention, and how the Great Compromise settled it.",
    "Explain how the Constitution divides and checks power, and how its settlements on counting the enslaved, the slave trade, and persons held to service built slavery into the frame.",
    "Explain the Federalist and Anti-Federalist arguments of 1787 and 1788, how the Massachusetts compromise saved ratification, and what the Bill of Rights added by 1791.",
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
    P.append("<title>Study Guide: The Founding</title>")
    P.append(f"<style>{CSS}</style></head><body>")
    P.append('<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>')
    P.append('<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>')
    P.append("<h1>Study Guide: The Founding</h1>")
    P.append('<p class="directions"><strong>Directions:</strong> Complete Part 1 from your guided notes and readings, then answer the Part 2 questions in your own words. Part 3 tells the unit as one story and lists what the test will ask you to show. The unit test is built from this guide. Bring questions about anything you cannot answer to the review day.</p>')
    P.append("<p><strong>Unit question:</strong> Why did the colonies break with Britain, and what did Americans build in the place of the empire they rejected?</p>")
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
