#!/usr/bin/env python3
"""Colonial America Lesson 8 deck, "Empire and War: The French and Indian War,"
V2 (2026-10-24 rollout, improved slide standard): content bullets are
short complete sentences; speaker notes applied after the build from the
teacher notes guide (apply_guide_notes.py). Same 28 slides, same order."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags, photo_right,
                         divider_photo, content_photo, content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED, W, H)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

dc.IMG = os.path.join(HERE, 'img')
OUT = os.path.join(HERE, '..', 'lesson-08-slides-v2.pptx')

def vocab(title, terms, note, kick='The vocabulary'):
    s = slide(CREAM)
    kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95, 11.5, 1.0, title, size=30, color=NAVY, font='Georgia')
    yy = 2.1
    for term, dfn in terms:
        text(s, 0.9, yy, 4.1, 0.9, term, size=25, color=NAVY, font='Georgia')
        text(s, 5.15, yy + 0.06, 7.3, 1.1, dfn, size=19, color=MUTED, leading=1.2)
        yy += 1.52
    notes(s, note)
    return s

def content_photo_s(img, title, items, note, kick=None):
    s = slide(CREAM)
    photo_right(s, img)
    if kick: kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95 if kick else 0.8, 6.9, 1.2, title, size=30, color=NAVY, font='Georgia', leading=1.05)
    frags(s, items, y=2.12 if kick else 2.0, size=21, gap=11, leading=1.2)
    notes(s, note)
    return s

# ---------------------------------------------------------------- 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'COLONIAL AMERICA · LESSON 8', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'Empire and War: The French and Indian War', size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'The Ohio Valley, Pitt and Quebec, the treaty, Pontiac, and the line, 1754 to 1763', size=17, color=POWDER)
notes(s, "The image is John Mitchell's map of the British and French dominions in North America, published in London in 1755, the map the empire's own diplomats used. It opens the unit's closing lesson because this war was fought over the ground the map claims, and the map claims more than either empire held. Teach the lesson as a victory studied whole: how Britain won North America, and what the victory cost everyone who fought it, Britain, the thirteen colonies, and the Ohio and Great Lakes nations who appear in this lesson as peoples with claims and strategies of their own. The unit ends at 1763 on purpose. The treaty, the rising, and the Proclamation line are the door into the next unit, and nothing past that door is opened today.")

# ------------------------------------------------- 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[("How did Britain win North America, and what did the victory cost everyone who fought it?", {})]],
     size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('How did the meeting of Europe, Africa, and the Americas remake all three worlds, and what kind of society grew up in England\u2019s colonies?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "The lesson question has two halves, and students must keep them joined, because either half alone produces a false lesson. How Britain won is a question with a documented answer: a war that opened in disaster in 1754 and 1755 was reversed after 1757 by money borrowed in unprecedented amounts, regular regiments and sea power sent across the Atlantic, officers promoted by merit, and colonial soldiers and assemblies serving and paying beside the regulars. What the victory cost is a question with three separate answers, one for each people who paid. Britain paid in a debt nearly doubled. The colonies paid in a Proclamation line that closed the west they had fought expecting to enter. The Ohio and Great Lakes nations paid most: their French counterweight destroyed, their country transferred at a table where they had no seat, and a war of their own in 1763 to keep it.")

# --------------------------------------------------- 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Three claims, one war, three bills', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'Three claims on one valley', 'Ohio nations, Virginia, and France, by 1750'),
        ('B', 'The war opens', 'Washington, Jumonville, Fort Necessity, 1754'),
        ('C', 'Albany and disaster', 'The plan rejected; Braddock destroyed, 1755'),
        ('D', 'Pitt and the turn', 'Louisbourg 1758, Quebec 1759, Montreal 1760'),
        ('E', 'One war, many wars', 'A worldwide war; the allies\u2019 fates divide'),
        ('F', 'The Treaty of Paris', 'February 10, 1763: France off the mainland'),
        ('G', 'The bills arrive', 'Debt, Pontiac\u2019s rising, the Proclamation line')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "The map follows the guided notes section by section. Section A sets three claims on the Ohio Valley: the Ohio nations who lived there, Virginia by charter and speculation, and France by its chain of forts. Section B opens the war with Washington's mission of 1753, the ambush of Jumonville's party, and the surrender of Fort Necessity in 1754. Section C holds the Albany Plan's rejection beside Braddock's destruction in 1755 and two years of frontier raids. Section D turns the war under Pitt: Louisbourg in 1758, Quebec in 1759, Montreal in 1760. Section E widens to the worldwide Seven Years' War and the allies' divided fates. Section F writes the victory into the Treaty of Paris. Section G presents the bills of 1763: the debt, Pontiac's rising, and the Proclamation line.")

# ------------------------------------------------- 4 SECTION A DIVIDER
divider_photo('mitchell-port.jpg', 'Section A', 'Three Claims on One Valley',
              ['By 1750 the Ohio Valley was claimed at once', 'by the peoples who lived there and by two empires.'],
              "The image is a detail of the Mitchell Map, drawn in London from colonial governors' reports and published in 1755, the standard map of the war's ground. Begin by correcting the picture maps like this one give: the colored imperial claims are arguments, not possessions. The Ohio Valley in 1750 was lived in, farmed, hunted, and governed by Indigenous nations, Delaware, Shawnee, and Mingo among them, whose towns and councils appear on period maps as names in a landscape European engravers otherwise filled with imperial color. France claimed the valley as the link between Canada and Louisiana. Virginia claimed it by a charter written in London a century and a half earlier. The Ohio nations claimed it by living there, and for two generations they had defended that claim with diplomacy rather than submission, playing the empires against each other. The war began when both empires decided the ground itself was worth more than the nations' friendship.",
              title_size=34)

# ------------------------------------------------------ 5 THREE CLAIMS
content_text('Three claims on one valley',
             ['The Ohio nations lived in the valley and kept it by playing empire against empire.',
              'Virginia claimed it by charter, by speculators\u2019 grants, and by settlers crossing the mountains.',
              'France claimed it as the link between Canada and Louisiana, bound by a chain of forts.',
              'The balance held while both empires still needed the nations\u2019 friendship.'],
             "Take the three claims in the order the reading gives them, nations first, because the war is unintelligible if the valley is treated as empty. The Ohio nations, Delaware, Shawnee, and Mingo among them, had kept their country for two generations by a deliberate policy: trade with both empires, ally with neither permanently, and use each as a counterweight to the other. Virginia's claim ran on paper, a sea to sea charter and grants sold by speculators like the Ohio Company to buyers who had never seen the land. France's claim ran on water and timber, a chain of forts from Lake Erie down the Allegheny to the Forks, holding the portages between Canada and the Mississippi. Ask students to name what each claimant would have to give up to accept another's claim. That exercise, done honestly, predicts the war: by 1753 neither empire would accept the nations' terms, and the nations would not accept either empire's.",
             kick='A · Three claims on one valley', size=24)

# ------------------------------------------------- 6 SECTION B DIVIDER
divider_text('Section B', 'The War Opens',
             'A twenty two year old major carries a letter to the French, ambushes a French party, and surrenders a fort, all inside eight months.',
             "Frame this section as a young man's expedition with an empire's consequences, because the scale is the lesson. George Washington in 1753 was twenty one, a Virginia militia major with surveying experience and powerful patrons, ambitious for a regular commission and for western land. Governor Dinwiddie, himself an investor in the Ohio Company, chose him to carry Virginia's ultimatum to the French commandant: withdraw from the Ohio country or answer for it. The mission made Washington's name in print on both sides of the Atlantic, since Dinwiddie published his journal in 1754 as Virginia's case against France. It also started a world war. The shots at Jumonville Glen in May 1754 are conventionally counted the first of the Seven Years' War, fired two years before the war was declared in Europe. Students should feel the disproportion and learn from it: empires drift into wars through agents on distant ground whose local quarrels they cannot control and will not disown.")

# ------------------------------------------------------ 7 WASHINGTON
content_text('Washington\u2019s mission, 1753 to 1754',
             ['In 1753 Governor Dinwiddie sent Washington to order the French out of the Ohio country.',
              'The French refused, politely, and Dinwiddie published Washington\u2019s journal as Virginia\u2019s case.',
              'In May 1754 Washington, guided by Tanacharison, ambushed a French party in a rocky glen.',
              'Jumonville was killed, and twenty-one French prisoners were taken.'],
             "Read Washington's own journal entry at Station 2 of the activity before summarizing him, because the document shows what the mission was really for. He was sent to deliver a letter, yet his journal surveys the Forks of the Ohio like an engineer: extreamly well situated for a Fort, with the absolute Command of both Rivers, in his words as the 1754 edition printed them. The published journal was Virginia's claim staked in print. The following May, guided by the Seneca leader Tanacharison, whose own quarrel with the French was older than Virginia's, Washington ambushed Jumonville's party in a rocky glen. Ten Frenchmen were killed, by Washington's own count in his report, Jumonville among them, killed after the fighting by Tanacharison, by several accounts. France called the party an embassy and its commander murdered. Washington called it a military reconnaissance. The difference between those two descriptions is the difference between a skirmish and an assassination, and it follows Washington onto the next slide.",
             kick='B · The war opens', size=24)

# ------------------------------------------------------ 8 FORT NECESSITY
content_text('Fort Necessity and the capitulation',
             ['Washington built a small stockade at Great Meadows in a matter of days.',
              'On July 3, 1754, attacked in the rain, the flooded fort surrendered.',
              'The capitulation was written in French, which Washington could not read.',
              'Its word for Jumonville\u2019s death was assassination, and France printed it across Europe.'],
             "Slow down on the capitulation, because it is this lesson's cleanest document lesson after the cartoon. Washington's position at Great Meadows was weak: a small round stockade in a meadow clearing, trenches that flooded in the rain of July 3, powder wet, and a French force under Jumonville's own brother offering terms by night. The terms were brought in French and translated aloud by an interpreter in the rain. Washington signed a document that twice framed his mission around the assassination of a French officer on what France called a diplomatic errand. He insisted for the rest of his life that the word rendered to him was death, not assassination. Both things can be true: the translation failed him, and the signature was his. France printed the capitulation across Europe as a British confession. Teach the sequence as the war's first propaganda victory, won with a dictionary rather than a regiment.",
             kick='B · The war opens', size=24)

# ------------------------------------------------- 9 SECTION C DIVIDER
divider_text('Section C', 'Albany and Disaster',
             'The colonies refuse to unite in 1754, and the unled war produces the Monongahela in 1755 and two years of frontier raids.',
             "Pair this section's two halves deliberately, because together they state the colonies' position in 1754 and its price. At Albany that summer the colonies were offered the machinery of union, drafted by their own delegates, and every assembly refused it. The refusal was not apathy: the assemblies were defending the power of the purse and their separate charters against a president general appointed in London and a council that could tax them. Those defenses were the habits of self government Lesson 7 traced. But the war did not wait for the colonies to settle their principles. Britain sent a regular army under a commander who disdained colonial and Indigenous advice, and the frontier paid for the disunion and the disdain together. Students should hold both judgments at once, since the lesson's closing verdict will ask them to weigh a union refused against a victory finally won without one.")

# ------------------------------------------------------ 10 ALBANY
content_photo_s('join-port.jpg', 'Join, or Die, and the plan it advertised',
             ['Franklin\u2019s Gazette cartoon showed a snake cut into eight segments: join, or die.',
              'His plan proposed one government for defense, Indian treaties, and western purchases.',
              'A President-General would be appointed by the Crown, and a Grand Council chosen by the assemblies.',
              'The congress adopted the plan; every assembly rejected it, and the Crown let it drop.'],
             "The cartoon on this slide is reproduced from the Library of Congress copy of the Pennsylvania Gazette of May 9, 1754, and students meet its bank description at Station 1. Teach the image before the plan: a snake cut into eight labeled segments is an argument that division is death, made for newspaper readers in the weeks before the Albany Congress. The plan the cartoon advertised proposed a President-General appointed and supported by the Crown and a Grand Council chosen by the assemblies, holding Indian treaties, defense, western purchases, and a power to lay general taxes. The congress adopted it. Every assembly then rejected it, and the Crown, which disliked a council that could tax, let it drop. Franklin wrote later that the assemblies thought the plan had too much prerogative in it, and the Crown thought it had too much of the democratic. That double rejection is the document's verdict: union in 1754 had no constituency strong enough to pay for it.",
             kick='C · Albany and disaster')

# ------------------------------------------------------ 11 STAT 48
stat('48', 'members of the Grand Council the Albany Plan proposed',
     'Chosen by the assemblies, colony by colony · Never seated',
     "Use this number to make the plan concrete, because students hear union as a slogan and the plan was a constitution with arithmetic. The Avalon transcription, quoted at Station 3, apportions the forty eight seats colony by colony: Massachusetts Bay and Virginia seven each, Pennsylvania six, Connecticut five, New York, Maryland, North Carolina, and South Carolina four each, New Jersey three, New Hampshire and Rhode Island two each. The proportions track population and expected contributions, and after three years the seats were to be reapportioned by each colony's payments into the general treasury, never fewer than two and never more than seven for any colony. It is a federal design in embryo, representation tied to taxation a generation before the phrase existed. The assemblies that refused those forty eight seats were refusing, among other things, to be outvoted in a body that could tax them, and teachers should let students argue whether they were wrong, using Braddock's defeat, one summer later, as the evidence on the other side.",
     kick='C · Albany and disaster')

# ------------------------------------------------------ 12 BRADDOCK
content_text('Braddock\u2019s defeat and the frontier war',
             ['In July 1755 two regiments marched on Fort Duquesne.',
              'Ambushed on the Monongahela, the army was destroyed and Braddock was killed.',
              'Two years of raids on the frontier settlements followed.',
              'Thousands were killed or captured, by the records\u2019 estimates.'],
             "State the disaster plainly and resist the legend in both directions. General Edward Braddock was no fool, and his column was a professional army with artillery, ambushed in wooded ground by a smaller force of French and Indigenous fighters whose method of war the ground suited. Braddock was killed, his army destroyed as an effective force, and his papers, including British plans, were captured. What followed was worse than the battle. For two years, French and Indigenous raiding parties struck the frontiers of Pennsylvania, Virginia, and Maryland, burning settlements and carrying off captives, while the colonial governments quarreled over money and Britain's war failed in Europe as well. The casualty figure on this slide is stated as what it is, an estimate drawn from the records, and students should notice the lesson's habit: where the record gives no exact count, the lesson gives none, and labels the range it uses.",
             kick='C · Albany and disaster')

# ------------------------------------------------- 13 SECTION D DIVIDER
divider_text('Section D', 'Pitt and the Turn',
             'From 1757 one minister borrows millions, sends the regulars and the navy in force, and buys colonial help with promises of repayment.',
             "Introduce William Pitt as a change of system, not a change of luck, because that is how the record reads. By 1757 Britain had lost Minorca, was losing in Germany, and had failed in North America for three campaigning seasons. Pitt, directing the war from London, reversed the method on every point. Where his predecessors had economized, he borrowed, running the national debt toward double its prewar size and treating credit as a weapon. Where they had sent regiments in driblets, he sent armies and fleets. Where London had lectured the assemblies, he promised reimbursement for colonial men and money, and the assemblies responded with troops and taxes. He also promoted by merit in a service run on purchase and seniority, which is how a thirty two year old James Wolfe came to command at Quebec. The next two slides test the system: the victories of 1758 to 1760, won by regulars, sailors, and colonial soldiers together.")

# ------------------------------------------------------ 14 PITT TURN
content_text('The turn, 1757 to 1760',
             ['Pitt borrowed millions and spent them on North America.',
              'Regulars and the navy were sent in force, and officers were promoted by merit.',
              'Assemblies were repaid for the men and money they voted, and they voted both in thousands.',
              'Louisbourg fell in 1758, Quebec in 1759, and Montreal in 1760.'],
             "Teach the sequence as a system producing results on a schedule. In 1758 the new method took Louisbourg, the fortress at the mouth of the St. Lawrence, after a siege supported by overwhelming sea power, and a British column forced the French to abandon Fort Duquesne, where Pittsburgh now stands. In 1759, the year British memory calls the year of victories, Wolfe's expedition sailed up the St. Lawrence under naval escort. In 1760 Montreal surrendered and Canada passed under British military government, three years before the diplomats signed. At every step the colonial part must be stated beside the regular part: provincial regiments served in the thousands in these campaigns, colonial assemblies voted the men and the money Pitt had promised to repay, and colonial rangers and Indigenous allies who had made their own peace with Britain opened the road to Duquesne. The victory was imperial and colonial at once, which is why its bills, in Section G, could be presented to both.",
             kick='D · Pitt and the turn')

# ------------------------------------------------------ 15 QUEBEC
content_photo_s('wolfe-port.jpg', 'Quebec, September 13, 1759',
             ['Wolfe\u2019s army landed below the cliffs by night and formed on the Plains of Abraham.',
              'British volleys broke the French advance in under an hour.',
              'Both commanders were killed: Wolfe on the field, Montcalm the next morning.',
              'Quebec surrendered five days later, and Canada fell with Montreal in 1760.'],
             "The painting on this slide is Benjamin West's Death of General Wolfe, painted in 1770, eleven years after the battle, and students should be told so: it is a commemoration, not a report, and its grouped officers and contemplative Indigenous figure are West's composition, not the field's record. The battle itself was brief and decided by discipline. After a summer of failed attempts, Wolfe landed his army by night below the cliffs west of Quebec and formed it on the Plains of Abraham. Montcalm marched out to fight before his supplies and reinforcements could be cut off, and British volleys broke the French advance in under an hour. Wolfe was hit three times and died on the field; Montcalm died the next morning. Quebec surrendered on September 18. France nearly retook the city the following spring, and only the arrival of a British fleet in May 1760 settled Canada before Montreal fell.",
             kick='D · Pitt and the turn')

# ------------------------------------------------- 16 SECTION E DIVIDER
divider_text('Section E', 'One War, Many Wars',
             'The North American war was one theater of a worldwide struggle, and inside the shared victory the allies\u2019 experiences divided sharply.',
             "Widen the lens for one section, because students who see only North America will misjudge both the winning and the bills. The Seven Years' War was fought on four continents: Prussia against Austria and France in Europe with British subsidies, Britain against France in India, in the Caribbean sugar islands, in West Africa, and at sea everywhere. North America's conquest was one prize among several, and at the peace table Britain weighed Canada against the sugar island of Guadeloupe and chose Canada. That global frame also explains the debt on the closing slides: Britain had paid for a world war, not a frontier one. Inside the North American victory, meanwhile, the allies' experiences divided. The same campaigns that taught colonial soldiers British competence taught them British contempt. The same French collapse that freed Britain's hand in the interior ended the balance the Ohio nations had built their diplomacy on. One victory, three different wars: the next slide separates them.")

# ------------------------------------------------------ 17 MANY WARS
content_text('The allies\u2019 divergent fates',
             ['France\u2019s Indigenous allies lost the counterweight their diplomacy required.',
              'British officers cut the gifts, powder, and trade credit that alliance had run on.',
              'Colonial soldiers learned British competence, and British contempt for provincials.',
              'Assemblies, courted and repaid, practiced paying for a continental war.'],
             "Work the four fragments as four separate balances being closed. France's Indigenous allies, and the Ohio nations who had traded with France while obeying no one, lost the counterweight their diplomacy required: with one empire gone, British officers no longer had to bid for their friendship, and General Amherst cut the gift giving and restricted the powder that alliance had run on. Colonial soldiers carried home a double education, respect for British professional competence and resentment at regular officers who treated provincial troops and their officers as inferiors, a grievance men like Washington kept for life. Colonial assemblies carried home a habit: courted by Pitt and repaid by London, they had voted men and money on a continental scale and had grown practiced at both. Each of these is a bill presented later. Section G collects the financial one; the nations' answer and the Proclamation arrive there too.",
             kick='E · One war, many wars', size=24)

# ------------------------------------------------- 18 SECTION F DIVIDER
divider_photo('bowen-port.jpg', 'Section F', 'The Treaty of Paris',
              ['February 10, 1763: the victory written onto the map,', 'by men who had never seen the country they divided.'],
              "The image is Emanuel Bowen's accurate map of North America drawn to the treaty, the same map students read in the quick check. Set the scene of the signing before the terms. The diplomats at Paris divided a continent none of them had crossed, working from maps like the Mitchell Map on this lesson's title slide. France, Britain, and Spain settled North America among themselves in articles that run to fisheries, sugar islands, and the Mississippi's navigation. No Indigenous diplomat was in Paris, no Indigenous signature is on the treaty, and no article asks the peoples of Canada, the Ohio Valley, or the Great Lakes whether they accepted being transferred. That absence is not a modern judgment imposed on the document; it is the document's own table of contents. The nations concerned answered the treaty in the spring of the same year, in the rising Section G teaches, and their answer is part of the treaty's history, not a footnote to it.",
              title_size=34)

# ------------------------------------------------------ 19 TREATY
content_text('The treaty\u2019s terms',
             ['Canada passed to Britain in full right, with all its dependencies.',
              'Everything east of the Mississippi passed to Britain, except New Orleans.',
              'Louisiana west of the river went to Spain, and Florida went to Britain.',
              'France\u2019s mainland empire, built since 1608, ended in a signature.'],
             "State the terms from the articles students' teacher key paraphrases, Articles IV and VII of the Avalon transcription. By Article IV France cedes Canada in full right, with all its dependencies, Cape Breton, and the islands and coasts of the Gulf and River St. Lawrence, and Britain agrees that Canada's inhabitants may profess the Catholic religion as far as British law permits. By Article VII the boundary between British and French dominions in America is fixed irrevocably along the middle of the Mississippi, and France cedes everything it possesses on the river's left side except the town of New Orleans and its island. In the treaty's other arrangements, France had already ceded Louisiana west of the river to Spain, and Spain ceded Florida to Britain. The result, in the reading's summary: Britain held North America from Hudson Bay to the Gulf, and France's mainland empire, built since 1608, was finished in a signature.",
             kick='F · The Treaty of Paris', size=24)

# ------------------------------------------------- 20 SECTION G DIVIDER
divider_text('Section G', 'The Bills Arrive',
             'In a single year, 1763: a debt nearly doubled, an interior in arms, and a line drawn down the Appalachians.',
             "Close the lesson by presenting the three bills of 1763 in the order the reading gives them, because the order is the argument. The financial bill came first in London's thinking: the national debt had nearly doubled, the war's interest alone consumed a share of revenue ministers found frightening, and a standing army in America would cost money every year of the peace. The military bill arrived in the spring, when the Ohio and Great Lakes nations rose and took most of the interior forts, showing that the conquest of Canada had not conquered the interior and that holding it would cost the very money London was trying to save. The political bill followed in October, when the Proclamation tried to stop the frontier war by fencing the colonies out of the west, and in doing so made enemies of the veterans and speculators the victory had promised land. Three bills, one year, and every later quarrel of the empire runs through them.")

# ------------------------------------------------------ 21 DEBT AND PONTIAC
content_text('The debt, and the rising of 1763',
             ['Britain\u2019s debt nearly doubled, and ministers resolved that the colonies should pay for their own defense.',
              'In the spring of 1763 the nations of the lakes and the Ohio Valley rose under Pontiac and other leaders.',
              'Most interior forts fell within weeks; Detroit and Fort Pitt were besieged.',
              'The frontier was struck again, by the peoples the treaty had ignored.'],
             "Hold the two halves of this slide together, because each explains the other's timing. The debt was real and enormous by the standards of the day, and ministers across parties resolved that Americans, defended at British expense, should contribute to the cost of their own defense; the next unit opens with the measures that resolution produced. The rising was also real, and it was not a spasm. The nations of the Great Lakes and Ohio Valley had watched Amherst end the gifts, restrict the powder, raise the prices, and refuse the credit that French alliance had carried, while settlers crossed the mountains onto land the treaty had just transferred without their consent. Under leaders including the Ottawa chief Pontiac, they struck together in the spring of 1763, took most of the interior forts within weeks, and besieged Detroit and Fort Pitt. They fought, in the summary's terms at Station 4, to keep their country or force the French terms back.",
             kick='G · The bills arrive', size=24)

# ------------------------------------------------------ 22 STAT DEBT
stat('Nearly 2x', 'Britain\u2019s national debt, after seven years of world war',
     'The interest alone frightened ministers · America\u2019s defense now had to be paid for in peacetime',
     "Teach this figure as the hinge number of the whole unit, and be precise about its status: the debt nearly doubled during the war is the standard summary, and this lesson asserts no exact pound figure, because the documents in the file do not carry one. What the number meant in practice can be stated exactly. Before the war, Britain's American establishment had been small and cheap, a few regiments and a customs service the colonies mostly evaded. After 1763, ministers intended to keep a standing force in America to hold the new continent and police the Proclamation line, and that force had to be paid every year, in peacetime, out of revenue that did not exist yet. Every part of the imperial crisis the next unit teaches begins in the gap between this slide's number and that intention. Students who understand the arithmetic do not need the later taxes explained as villainy or as justice; they can see the problem each side was solving, and why the solutions collided.",
     kick='G · The bills arrive')

# ------------------------------------------------------ 23 PROCLAMATION
content_text('The Proclamation line, October 1763',
             ['Settlement was forbidden west of the Appalachians.',
              'The country was reserved to the Indigenous nations as their hunting grounds.',
              'Settlers already seated there were ordered to remove themselves.',
              'The line was drawn in London as a temporary fence, and settlers crossed it from the year it was drawn.'],
             "Read the proclamation's own words at Station 5 before judging it, because the document is more interesting than its reputation. In its own language it is just and reasonable that the nations under British protection should not be molested or disturbed in lands not ceded or purchased, reserved to them as their hunting grounds. It forbids governors to grant the land, forbids subjects to buy or settle it without licence, and orders those already seated on it to remove themselves forthwith. Its motives, as the guided notes definition states, were to reserve the land for Indigenous peoples and prevent new frontier wars, and it was issued for the present, until the king's further pleasure: a temporary fence, not a permanent wall. None of that softened its reception. Veterans had been promised western acres for their service and speculators held paper claims to millions more, and both read the line as the victor confiscating the prize. Settlers crossed it anyway, from the year it was drawn.",
             kick='G · The bills arrive', size=24)

# ------------------------------------------------------ 24 AT A GLANCE
s = slide(NAVY)
kicker(s, 'The victory at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Won, and what it cost', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Won', 'Canada; the Mississippi line; France off the mainland', 'Pitt\u2019s system, regulars and sea power, colonial men and money'),
        ('Britain paid', 'A debt nearly doubled', 'The colonies marked to pay for their own defense'),
        ('Colonies paid', 'The Proclamation line, October 1763', 'The west closed to the veterans who had fought for it'),
        ('Nations paid', 'The counterweight gone; their country transferred', 'The rising of 1763, under Pontiac and other leaders')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.2, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.25, yy + 0.05, 5.1, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.55, yy + 0.05, 3.9, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the closing table of the guided notes, The Victory at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. Won: Canada and the lands east of the Mississippi, taken by Pitt's direction from 1757, borrowed millions, regulars and the navy in force, and colonial soldiers and assemblies beside them, sealed at Louisbourg in 1758, Quebec in 1759, and Montreal in 1760, and written into the Treaty of Paris of February 10, 1763. Britain paid with a national debt nearly doubled and the standing cost of a continent. The colonies paid with the Proclamation of October 1763, closing the western country their veterans expected to enter. The Ohio and Great Lakes nations paid with the French counterweight, with a treaty that transferred their country without them, and with the war they fought under Pontiac and other leaders in 1763 to keep it. Grade the table on dates and actors named, not on adjectives.")

# ------------------------------------------------------ 25 VOCAB A
vocab('Words for the war and the union',
      [('French and Indian War', 'the North American war, 1754 to 1763'),
       ('Seven Years\u2019 War', 'the worldwide war, 1756 to 1763'),
       ('Albany Plan of Union', 'Franklin\u2019s 1754 proposal for one government'),
       ('William Pitt', 'the minister who directed the war from 1757')],
      "These definitions match the guided notes, and the notes carry them in full, word for word. French and Indian War: the North American war of 1754 to 1763 between Britain and France and their Indigenous allies, part of the worldwide Seven Years' War, which ended with Britain taking Canada and the French lands east of the Mississippi. Seven Years' War: the worldwide war of 1756 to 1763 in which Britain and Prussia fought France, Austria, and their allies across Europe, North America, the Caribbean, and Asia. Albany Plan of Union: Benjamin Franklin's proposal of 1754 that the colonies unite under one government for defense and relations with Indigenous nations, rejected by the colonial assemblies and the Crown. William Pitt: the British statesman who took direction of the war in 1757, paid for victory with borrowed millions, and sent Britain's army and navy to North America in force.")

# ------------------------------------------------------ 26 VOCAB B
vocab('Words for the peace and its answers',
      [('Treaty of Paris (1763)', 'Canada and the east to Britain, February 1763'),
       ('Pontiac\u2019s Rebellion', 'the rising of 1763 in the lakes and Ohio country'),
       ('Proclamation of 1763', 'the October line along the Appalachians')],
      "Three more terms, in the guided notes wording, carried in these notes in full, word for word. Treaty of Paris (1763): the treaty of February 1763 that ended the French and Indian War, giving Britain Canada and all French territory east of the Mississippi River except New Orleans. Pontiac's Rebellion: the uprising of 1763 in which Indigenous nations of the Great Lakes and Ohio Valley, joined under leaders including the Ottawa chief Pontiac, attacked British forts and settlements after the French defeat. Proclamation of 1763: the royal order of October 1763 forbidding colonial settlement west of the Appalachian Mountains, meant to reserve the land for Indigenous peoples and prevent new frontier wars. Notice the order of the three: a treaty that transferred a continent, a rising by the peoples the treaty ignored, and an order by the victor fencing its own colonists out of the prize, all inside nine months of one year.")

# ------------------------------------------------------ 27 CLOSING SYNTHESIS
s = slide(NAVY)
kicker(s, 'Closing synthesis')
text(s, 0.9, 1.35, 11.5, 1.1, 'Where this unit ends', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 2.6,
     ["In 1763 Britain and its colonies had never been stronger together: Canada taken, France off the mainland, a continent east of the Mississippi under one flag.",
      "And every term of their partnership, money, land, and authority, was about to be renegotiated. The next unit takes up the renegotiation."],
     size=23, color=POWDER, leading=1.3)
notes(s, "Close the unit by stating its ending as the hinge it was built to be, in the reading's own closing terms. The victory of 1763 was complete in the way the century measured victories: an enemy empire removed from a continent, a boundary river reached, a capital and a fortress province transferred, and the winning side's soldiers, British and colonial, home with their reputations made. It was also unstable in every particular the lesson has itemized. The debt required revenue the colonies had never paid. The conquered interior required an army the treasury could not fund and its peoples had not consented to be conquered. The frontier required a line the victor's own subjects began crossing in the year it was drawn, and the assemblies that had learned to fund a war had also learned their own power in funding one. Nothing in today's lesson reaches past October 1763. What London did about money, land, and authority next is the Founding unit's subject, and students should arrive there able to say exactly which bills were already on the table.")

# ------------------------------------------------------ 28 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ["How did Britain win North America, and what did the victory cost everyone who fought it? State the winning whole, carry all three peoples who paid, and answer the strongest counterclaim to your own judgment."],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The War in Five Records: the cartoon, the journal, the plan, the rising, the proclamation'),
        ('Notebook', 'Notebook page: the questions of the war, what the documents show, what was decided'),
        ('Quick check', 'The Map of 1763: the clean division weighed against the ground'),
        ('Writing', 'Triumph, Warning, or Both: the unit\u2019s closing judgment of 1763')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the Albany Plan and the Proclamation defined, the turn of 1757 to 1760, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close the lesson by handing the judgment of 1763 to the students, which is what this lesson exists to do. The activity, The War in Five Records, gives them Franklin's cartoon from the audited bank record, Washington's journal in the 1754 edition as Founders Online transcribes it, the Albany Plan and the Proclamation in the Avalon Project transcriptions, and a labeled teaching summary for the rising of 1763, and asks for a verdict on the year with the strongest counterclaim answered. The notebook page charts the questions of the war. The quick check reads Bowen's treaty map against the ground it claims. The writing task is the unit's closing writing task: triumph, warning, or both, with all three peoples who paid carried in the evidence. The exit ticket has three parts: the plan and the proclamation defined, the turn from 1757 to 1760 stated, and the lesson question answered with the winning and the three costs kept together. The review day and the unit test follow from here.")

dc.save(OUT)
