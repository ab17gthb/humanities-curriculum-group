#!/usr/bin/env python3
"""Sectional Crisis Lesson 2 deck, "The Antislavery Argument at Full Voice,"
built to the approved system: image-led slides, fragments only on screen,
comprehensive speaker notes, full lesson + vocabulary coverage."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags, photo_right,
                         divider_photo, content_photo, content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED, W, H)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

dc.IMG = os.path.join(HERE, 'img')
OUT = os.path.join(HERE, '..', 'lesson-02-slides.pptx')

spec = open(os.path.join(HERE, '..', '..', 'build-scripts', 'unit-spec.md')).read()
l2 = spec.split('### Lesson 2')[1].split('### Lesson 3')[0]
DEFS = {}
for line in l2.splitlines():
    m = re.match(r'- (.+?): (.*)$', line.strip())
    if m: DEFS[m.group(1)] = m.group(2)
assert len(DEFS) == 7, DEFS.keys()

def joined(term):
    return f"{term}: {DEFS[term]}"

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

LQ = 'What did the antislavery writers of 1851 and 1852 ask their readers to feel, to judge, and to do?'
UQ = 'How did compromise over slavery finally fail, and what did the war it caused settle about slavery and the Union, and what did it leave open?'

# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'SECTIONAL CRISIS AND CIVIL WAR · LESSON 2', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Antislavery Argument at Full Voice', size=36, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'A novel, an oration, a speech in two texts, and a narrative', size=17, color=POWDER)
notes(s, "The image is Frederick Douglass in the daguerreotype Samuel J. Miller made between 1847 and 1852, held by the Art Institute of Chicago. Open with the writers, not the politicians: Lesson 1 closed with a compromise whose enforcement clause put federal officers on northern streets, and this lesson follows the answer those streets produced. Between 1851 and 1861 a novelist, an orator, a preacher, and a woman writing under a changed name built an argument in four forms, and each form asked something different of its reader. Students should leave able to name each form, state its ask, and handle the lesson's source problem, two surviving texts of Sojourner Truth's Akron speech, with care about who wrote each one down and when.")

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[(LQ, {})]], size=38, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                (UQ, {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Today's question has three verbs, and students will need all three for the exit ticket and the writing task: feel, judge, and do. Preview the mapping without giving the lesson away. The novel worked on feeling, carrying slavery into homes that had never seen it. The oration worked on judgment, reading the nation's own promises back to the people celebrating them. The narrative worked as witness, and the rescues demanded action with the body. Then add the caution the lesson builds in: an argument at full voice still has to be checked. One of its most famous speeches survives in two texts that do not match, and one of its most repeated stories, Lincoln greeting Stowe, cannot be verified at all. Full voice and full care go together in this lesson.")

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'A spectacle, a novel, an oration, a witness', size=40, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'Rendition Becomes a Spectacle', 'Sims, Jerry, Christiana, and Burns marched through Boston'),
        ('B', 'The Novel That Answered', 'Stowe builds a household argument from the narratives'),
        ('C', 'Banned, Answered, and Carried Everywhere', 'Anti-Tom novels, a documentary Key, one anecdote'),
        ('D', 'Douglass at Rochester', 'The Fourth audited against the slave\u2019s present'),
        ('E', 'Two Texts of One Speech', 'Robinson in 1851 against Gage in 1863'),
        ('F', 'The Enslaved Woman\u2019s Own Book', 'Jacobs writes what the men could not write for her'),
        ('G', 'Feeling, Judgment, Witness, Action', 'Four instruments assembled by 1852')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A covers the Fugitive Slave Act at work and the rendition spectacle, ending with Anthony Burns. Section B covers Stowe and the novel's construction. Section C covers the South's answer, Stowe's documentary Key, and the Lincoln anecdote handled as an anecdote. Section D covers Douglass at Rochester. Section E sets the two Truth texts side by side. Section F covers Harriet Jacobs and her 1861 narrative. Section G assembles the four instruments. The summary table at the end of the guided notes is titled The Argument at a Glance.")

# 4 SECTION A DIVIDER
divider_photo('burns-port.jpg', 'Section A', 'Rendition Becomes a Spectacle',
              ['Anthony Burns, whose 1854 rendition', 'filled Boston with troops and', 'mourning crowds.'],
              "The image is Anthony Burns in the portrait engraving published in Boston in 1855, held by the Library of Congress. Keep Burns in view while section A is introduced, because his case is the section's proof. The Fugitive Slave Act of 1850 was written as procedure: an affidavit, a commissioner, a certificate. In practice it became theater. Each rendition put marshals, troops, chains, and crowds into northern streets, and each crowd went home having seen slavery's officers at work in a free state. Section A follows four cases in three years: Sims, Jerry, Christiana, and Burns, rising in scale until a whole city turned out in mourning dress to watch one man marched to a ship. Keep that pairing of law and theater in mind all hour.",
              title_size=38)

# 5 FOUR CASES
content_text('Four renditions, 1851 to 1854',
             ['Sims: carried through Boston in chains, April 1851',
              'Jerry: rescued by a Syracuse crowd, October 1851',
              'Christiana: Gorsuch killed at Parker\u2019s door, September 1851',
              'Burns: marched to a cutter between troops, 1854'],
             "Work the four cases as a rising sequence, since students should feel the escalation the reading builds. Thomas Sims was seized in Boston in April 1851, held in a courthouse wrapped in chains, and shipped back to Savannah, the city's first rendition under the new law. That September, at Christiana in Pennsylvania, Edward Gorsuch arrived with a federal warrant for men he claimed as his property and was killed at William Parker's door, where Black families had gathered to defend their homes. In October a Syracuse crowd broke William Henry, called Jerry, out of custody during his hearing and sent him to Canada. Close with Burns, whose full case gets the next slide. The pattern to name: the law's enforcement kept producing the movement's evidence, in public, on northern ground.",
             kick='A · Rendition Becomes a Spectacle', size=24)

# 6 BURNS AND HIGHER LAW
content_text('Burns, and the higher law answer',
             ['Arrested in Boston, May 1854, tried before a commissioner',
              'Church bells tolled, buildings draped in black',
              'Resisters invoke a higher law above the statute',
              'Rendition becomes a spectacle staged against itself'],
             "Give Burns his full weight, because the vocabulary list carries him. Anthony Burns, escaped from Virginia, was arrested in Boston in May 1854 and tried before a federal commissioner while the courthouse stood draped in black and church bells tolled. A rescue attempt failed, and on June 2 he was marched to a revenue cutter between lines of federal troops and marines, with tens of thousands watching in silence. He was remanded to slavery, and Boston later raised money to purchase his freedom. Teach the resisters' doctrine beside the spectacle: the higher law, named by Senator William H. Seward in 1850, held that a law of God and nature above the Constitution condemned slavery and the Fugitive Slave Act, and northern resisters used it to justify disobeying a law they held no legislature could rightfully make.",
             kick='A · Rendition Becomes a Spectacle', size=24)

# 7 SECTION B DIVIDER
divider_photo('stowe-port.jpg', 'Section B', 'The Novel That Answered',
              ['Harriet Beecher Stowe, painted', 'by Alanson Fisher in 1850.'],
              "The image is Alanson Fisher's 1850 portrait of Harriet Beecher Stowe, held by the National Portrait Gallery. Section B turns from the street to the parlor. Stowe had lived eighteen years in Cincinnati, across the Ohio River from a slave state, teaching, raising a family, listening to fugitives and travelers, and reading the slave narratives the movement published, Josiah Henson's account among them. When the Fugitive Slave Act made her northern neighbors into slavery's potential officers, she answered with the form she commanded: a novel, serialized in an antislavery newspaper and built, scene by scene, out of the narratives' evidence. Teach the construction before the plot: this book was an argument assembled from testimony. The portrait dates from 1850, the year the Fugitive Slave Act passed into law.",
              title_size=38)

# 8 THE NOVEL
content_text("Uncle Tom's Cabin, 1851 and 1852",
             ['Serialized in the National Era in 1851',
              'Published as a book in March 1852',
              'Built from the slave narratives, Henson among them',
              'Its recurring wound: families parted at the block',
              'Aimed at the Christian mother\u2019s conscience'],
             "Read the novel as an instrument, the way the reading presents it. Its serialization in the National Era through 1851 built an audience week by week, and the book of March 1852 reached readers no pamphlet could. Stowe's method did as much work as her story: she took the slave narrative's evidence, its separations, auctions, and pursuits, and set it inside a domestic novel northern families already knew how to read. The recurring wound is separation, a mother sold from her child, a husband sold down the river, a family scattered by a master's debts. She also aimed the argument inward at the enslaver's household, showing slavery corrupting the people who ran it as surely as it destroyed the people under it. The ask was feeling first, because feeling was the door her readers had left open.",
             kick='B · The Novel That Answered', size=23)

# 9 STAT 300,000
stat('300,000', 'copies in the first American year, by the usual estimates',
     'The best selling American novel of its century · Serialized 1851, a book in March 1852 · Estimates are stated as estimates',
     "Hold this number up as an estimate, because the lesson models how to handle figures. No complete sales ledger survives; the usual estimates put the first year near three hundred thousand copies in the United States, with British and translated sales far larger, many of them pirated. Even discounted, the scale is the fact: no American novel had reached so many readers so fast, and it reached them in their homes, read aloud in parlors and kitchens. Stowe understood what the number meant. The argument had not been voted on or preached at a crowd; it had been bought, borrowed, and wept over at the hearth, which is why the South answered it as a political act and why this lesson counts the novel as an instrument, not a diversion.",
     kick='B · The Novel That Answered')

# 10 SECTION C DIVIDER
divider_text('Section C', 'Banned, Answered, and Carried Everywhere',
             'A shelf of anti-Tom novels, a documentary Key, and one story that cannot be checked.',
             "Section C follows the book into the world and teaches students to sort its effects by their evidence. The South's answer is documented: the novel was banned, its sellers prosecuted in places, and southern writers produced a shelf of anti-Tom novels arguing that slavery was kind and northern wage labor cruel. Stowe's counter answer is also documented: A Key to Uncle Tom's Cabin in 1853, a documentary volume setting out the narratives, cases, and newspaper reports behind her scenes. The third item is different in kind. The story that Lincoln greeted Stowe as the little woman who made the great war was printed decades later, with no contemporary record, and this lesson states it as an anecdote, unverifiable, on its face.")

# 11 ANSWER AND ANECDOTE
content_text('The answer, the Key, and the anecdote',
             ['Banned across the South, answered by anti-Tom novels',
              '1853: A Key to Uncle Tom\u2019s Cabin defends the facts',
              'Translated into language after language',
              'The Lincoln greeting: an anecdote, printed decades later'],
             "Teach the three responses as three grades of evidence. The anti-Tom shelf, novels like Aunt Phillis's Cabin of 1852, is real and readable; its existence measures the wound Stowe had opened, since a book that changed nothing needs no answer. The Key of 1853 is Stowe's own method turned outward: she cited Josiah Henson's narrative for Tom's fidelity and set case beside scene, inviting critics to check her, which students should recognize as the same discipline this unit asks of them. Then the anecdote. It was first printed long after 1862, it flatters everyone's sense of the book's power, and precisely because it is satisfying it must be labeled: a story everyone repeats, not a fact anyone can check. Students will meet this sorting again with the Truth texts.",
             kick='C · Banned, Answered, and Carried Everywhere', size=23)

# 12 SECTION D DIVIDER
divider_photo('douglass-port.jpg', 'Section D', 'Douglass at Rochester',
              ['Frederick Douglass, in Samuel', 'J. Miller\u2019s daguerreotype.'],
              "The image is Frederick Douglass in Samuel J. Miller's daguerreotype, made between 1847 and 1852. Section D moves from the parlor to the platform. Douglass, who had escaped slavery in Maryland in 1838 and built the movement's leading Black newspaper in Rochester, was invited by the Rochester Ladies' Anti-Slavery Society to give the city's Independence Day address. He spoke on July 5, 1852, in Corinthian Hall, before an audience that had celebrated the Fourth the day before. What he did with their celebration is the section's subject: he accepted their premises, praised their founders' principles, and then audited the republic's practice against them in the hearing of the people who claimed to own both. By 1852 he had also broken with the Garrisonian abolitionists over the Constitution, a fight this lesson names and does not teach.",
              title_size=38)

# 13 THE ORATION
content_text('What to the Slave Is the Fourth of July?',
             ['Rochester, July 5, 1852',
              'The Fourth is yours, not mine: you rejoice, I must mourn',
              'Your celebration is a sham, your liberty hollow mockery',
              'The founding\u2019s promises audited against the slave\u2019s present'],
             "Set the oration's opening move plainly. Douglass divides the holiday before he judges it: this Fourth of July is yours, not mine, and to the slave it reveals, more than all other days in the year, the gross injustice and cruelty to which he is the constant victim. From there the speech reads the celebration item by item from the slave's side, its boasted liberty an unholy license, its prayers and hymns and thanksgivings a thin veil over crimes that would disgrace a nation of savages. Note the discipline in the attack: Douglass does not reject the founding. He praises the signers as statesmen and patriots and claims their principles as the slave's inheritance, which is what makes the audit unbearable for hearers who agreed with every premise he started from.",
             kick='D · Douglass at Rochester', size=23)

# 14 SCORCHING IRONY
content_text('Scorching irony, not convincing argument',
             ['Not light, but fire; not the shower, but thunder',
              'The nation\u2019s conscience must be roused',
              'Its hypocrisy must be exposed',
              'And the speech closes in hope, on the Declaration'],
             "Douglass tells his audience what instrument he is using and why, and students should catch the reasoning. At a time like this, he says, scorching irony, not convincing argument, is needed; the nation needs not the gentle shower but thunder, its feeling quickened, its conscience roused, its hypocrisy exposed. Argument assumes missing information. Douglass judged that his hearers lacked nothing but the will to apply what they knew, so he aimed at conscience rather than information. Then mark the ending, because students often miss it: the speech closes in hope. Douglass draws encouragement from the Declaration's principles and from the antislavery movement's rise, holding that the same ideals his audience celebrated would yet be turned against slavery itself. Judgment first, then hope, in that order.",
             kick='D · Douglass at Rochester', size=23)

# 15 SECTION E DIVIDER
divider_photo('truth-port.jpg', 'Section E', 'Two Texts of One Speech',
              ['Sojourner Truth, photographed', 'about 1870.'],
              "The image is Sojourner Truth in the photograph of about 1870 that she sold at her lectures to support her work. Section E is the lesson's deliberate source problem, and it should be taught slowly. Truth spoke at the women's rights convention at Akron, Ohio, in May 1851, arguing from her own enslaved labor that women deserved equal rights. No recording and no manuscript in her hand exist, because Truth could not write. What exists are two men's and women's texts made by other hands: a secretary's report printed within weeks, and a presiding officer's recollection published twelve years later. Everything students think they know about this speech depends on which text they are reading, and the sections' two slides take them in order.",
              title_size=38)

# 16 ROBINSON 1851
content_text('Robinson\u2019s text, printed June 21, 1851',
             ['Marius Robinson, the convention\u2019s secretary',
              'Printed in the Anti-Slavery Bugle within weeks',
              'The pint and the quart: let her pint be filled full',
              'Eve, Lazarus, and woman setting the world right'],
             "Read Robinson's report as the near contemporary record it is. Robinson edited the Anti-Slavery Bugle and served as the convention's secretary, and his account appeared on June 21, 1851, weeks after the speech. In it Truth argues from her body: she has plowed and reaped and husked and chopped and mowed, can carry and eat as much as any man, and answers the intellect objection with the pint and the quart, that a woman's smaller measure should still be filled full. She argues from the Bible her hearers cited against her: Eve turned the world upside down, so let woman set it right side up again, and Jesus never spurned woman from him. There is no repeated refrain in this text, and its plainness is part of its credibility. This is the text a historian may quote with confidence.",
             kick='E · Two Texts of One Speech', size=23)

# 17 GAGE 1863
content_text('Gage\u2019s version, published in 1863',
             ['Frances Dana Gage, who had presided at Akron',
              'Adds the repeated refrain the world remembers',
              'Renders Truth in a southern dialect',
              'Truth was born in New York and spoke Dutch as a child'],
             "Now set Gage beside Robinson, document against document, as the activity's Stations 3 and 4 require. Frances Dana Gage, who had presided over the Akron convention, published her recollection in 1863, twelve years after the speech. Her version is more dramatic, and it gave the speech its famous repeated refrain and its southern dialect. Both additions fail the biographical test: Truth was born enslaved in New York as Isabella Baumfree, grew up speaking Dutch, and never lived in the South. Gage's text is not worthless; it is evidence of how the speech was remembered and remade, and its refrain has inspired generations. But fame is not provenance. Teach the verdict directly: quote Robinson for what Truth said, and cite Gage, when cited at all, as Gage's 1863 version.",
             kick='E · Two Texts of One Speech', size=23)

# 18 SECTION F DIVIDER
divider_photo('jacobs-port.jpg', 'Section F', 'The Enslaved Woman\u2019s Own Book',
              ['Harriet Jacobs, in the Gilbert', 'Studios photograph of 1894.'],
              "The image is Harriet Jacobs in the Gilbert Studios photograph of 1894, the only known photograph of her, taken in her eighties. Section F closes the sequence of forms with the witness who paid most for her testimony. Jacobs was enslaved in Edenton, North Carolina. To resist her enslaver's pursuit she hid for seven years in a crawl space above her grandmother's storeroom, a space nine feet by seven and three feet high at its peak, drilling small holes to watch her children play below, unable to speak to them. She escaped to the North in 1842, worked as a nursemaid, and spent years writing the book this section reads, published in 1861 as the war began. The photograph is dated wherever it appears in this lesson, following the unit's practice with late portraits.",
              title_size=36)

# 19 JACOBS
content_text('Incidents in the Life of a Slave Girl, 1861',
             ['Published under the name Linda Brent',
              'The first slave narrative by an American woman published in the United States',
              'A child learns at six that she is merchandise',
              'What slavery did to women, in the subject\u2019s own voice'],
             "Open the narrative where Jacobs opens it, with the discovery. She was born a slave and did not know it until six years of happy childhood had passed; at her mother's death she learned by the talk around her that she was a slave, and that she had all along been a piece of merchandise, trusted to her parents for safe keeping and liable to be demanded back at any moment. Her father, a skilled carpenter, had several times offered his earnings to purchase his children and never succeeded. Teach the book's standing: it is the first slave narrative by an American woman published in the United States, written for northern women readers in particular, and it makes the argument about slavery and womanhood that the movement's male speakers could not make for her, because she alone could testify to it.",
             kick='F · The Enslaved Woman\u2019s Own Book', size=22)

# 20 STAT 7
stat('7', 'years hidden in a crawl space above a storeroom',
     'Harriet Jacobs, within earshot of her children · Escaped north in 1842 · Published her narrative in 1861',
     "Spend the silence this number earns. Seven years is most of a childhood: Jacobs's son and daughter grew from small children toward adolescence below a ceiling their mother watched through a bored hole, and she could not speak to them, cough freely, or stand upright in her hiding place. She chose the space over the alternatives her enslaver offered, and her choice is the narrative's credential: no reader could call her testimony secondhand. When the book appeared in 1861, under the name Linda Brent and with an abolitionist editor's sponsorship, it carried that credential into northern homes as the war began. Students should hold the number beside the novel's sales figure from section B: Stowe reached the most readers, and Jacobs had paid the most to testify. The writing task asks them to weigh reach against witness.",
     kick='F · The Enslaved Woman\u2019s Own Book')

# 21 SECTION G DIVIDER
divider_text('Section G', 'Feeling, Judgment, Witness, Action',
             'Four instruments, assembled by 1852, and the parties still promising to manage the question.',
             "Section G assembles the lesson, and students should be able to run the four instruments in order without their notes by its end. The novel asked for feeling: slavery carried into the parlor and judged at the hearth, by a writer who built fiction from testimony and defended her facts in a documentary key. The oration asked for judgment: the nation's promises read back to it by a man it had enslaved. The narrative asked for witness: a life set down in the first person, authenticated by sponsors because polite readers doubted the teller. The rescues asked for action: crowds and committees on northern streets. Over all four, the parties still promised that the slavery question could be managed by compromise. The next lesson tests that promise in Kansas.")

# 22 FOUR INSTRUMENTS
content_text('What each form asks',
             ['The novel: feel what separation does inside a home',
              'The oration: judge the celebration against the chains',
              'The narrative: witness a life in the first person',
              'The rescue: act, on the ground of a higher law'],
             "Land the lesson in this four line balance, and make students copy it into the summary table. Each form also carries its own standard of proof, which is the lesson's hidden curriculum. The novel proved itself by documentation, Stowe's Key answering charge with citation. The oration proved itself by the audience's own premises, the Declaration turned against its celebrants. The narrative proved itself by sponsorship and detail, a named woman writing under a changed name for safety. The speech at Akron proves the rule by its exception: when the recorder is late and inventive, confidence falls. Feeling, judgment, and witness each ask for trust, and this lesson has taught students how to grant it carefully, text by text, rather than all at once.",
             kick='G · Feeling, Judgment, Witness, Action', size=23)

# 23 GLANCE
s = slide(NAVY)
kicker(s, 'The argument at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'What each instrument asks of its reader', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The novel', 'Uncle Tom\u2019s Cabin, 1851 and 1852', 'Feel: families parted, households corrupted'),
        ('The oration', 'Douglass at Rochester, July 5, 1852', 'Judge: the Fourth audited from the slave\u2019s side'),
        ('The narrative', 'Jacobs, Incidents, 1861', 'Witness: a life told by its subject'),
        ('The speech', 'Truth at Akron, two texts', 'Act, and ask who wrote the words down')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the summary table in the guided notes, The Argument at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The four rows are the lesson in order. The novel: Stowe's book of 1852, built from the narratives and aimed at the mother's conscience, asking for feeling. The oration: Douglass at Rochester, turning the Fourth against its celebrants, asking for judgment. The narrative: Jacobs in 1861, after seven years in hiding, asking for witness. The speech and the rescue stand behind the table's fourth row: Truth's argument surviving in two unequal texts, and the crowds who acted on the higher law. Grade the table generously on wording and strictly on the asks: feeling, judgment, witness, and action are the lesson's vocabulary of purpose.")

# 24 VOCAB A
vocab('Words for the book and its maker',
      [("Uncle Tom's Cabin", 'the novel of 1852 that outsold its century'),
       ('Harriet Beecher Stowe', 'Cincinnati teacher, of the Beecher family'),
       ('slave narrative', 'the first person account that supplied the evidence'),
       ('higher law', 'Seward\u2019s doctrine, and the resisters\u2019 ground')],
      "Definitions match the guided notes word for word. " + joined("Uncle Tom's Cabin") + ". " + joined('Harriet Beecher Stowe') + ". " + joined('slave narrative') + ". " + joined('higher law') + ".")

# 25 VOCAB B
vocab('Words for the witnesses',
      [('Sojourner Truth', 'Isabella Baumfree, renamed in 1843'),
       ('Harriet Jacobs', 'seven years hidden, writing as Linda Brent'),
       ('Anthony Burns', 'Boston, 1854: the Act\u2019s most famous spectacle')],
      "Three more terms, again matching the guided notes exactly. " + joined('Sojourner Truth') + ". " + joined('Harriet Jacobs') + ". " + joined('Anthony Burns') + ". Keep the measures in view: Truth renamed herself and traveled on foot to lecture; Jacobs hid seven years within earshot of her children; Burns was one man, and his rendition required an army in the streets of Boston to complete it.")

# 26 SYNTHESIS
s = slide(NAVY)
kicker(s, 'The lesson in one view')
text(s, 0.9, 1.28, 11.5, 1.0, 'The argument assembled', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Felt', 'Stowe carried slavery into the parlor and made it a household argument'),
        ('Judged', 'Douglass read the founding\u2019s promises back to their celebrants'),
        ('Witnessed', 'Jacobs set down a life the movement\u2019s men could not testify to'),
        ('Checked', 'Robinson against Gage, an anecdote labeled an anecdote')]
yy = 2.78
for t, d in rows:
    text(s, 0.9, yy, 2.4, 0.7, t, size=24, color=RUST_LT, font='Georgia')
    text(s, 3.45, yy + 0.05, 9.0, 0.9, d, size=19, color=CREAM, leading=1.2)
    yy += 1.05
notes(s, "Use this slide to close the argument before the work begins, and make students say the four rows aloud in order, because the sequence is the lesson. Felt: a novelist in Cincinnati built slavery's evidence into a domestic novel, and the country bought it by the hundreds of thousands. Judged: an orator in Rochester refused the role of grateful guest and audited the nation's birthday from the slave's side of it. Witnessed: a woman who had hidden seven years in a crawl space published her own account in her own changed name. Checked: the same lesson that amplifies these voices refuses to repeat a presidential anecdote as fact and refuses a famous refrain as a certain quotation. Full voice and full care are the same standard, applied to friends of the cause as strictly as to its enemies.")

# 27 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['What did the antislavery writers of 1851 and 1852 ask their readers to feel, to judge, and to do? For each record, state what it asks of its reader, then deliver both verdicts.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Antislavery File: five stations, a table, and two verdicts'),
        ('Notebook', 'Notebook page: five forms in a chart, and two texts of one speech'),
        ('Quick check', 'Two Texts of One Speech: Robinson against Gage'),
        ('Writing', 'Feeling, Judgment, Witness: the lesson question as an essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the novel defined with its dates, the two Truth texts with the quotable one named, and the lesson question in two or three sentences.',
     size=15, color=POWDER)
notes(s, "Close by returning to the lesson question and handing the lesson to the work. The activity, The Antislavery File, sets out five stations: Stowe's concluding remarks from the 1852 first edition, Douglass's oration from the audited bank record, Truth at Akron in Robinson's 1851 transcription, the same address in Gage's 1863 version, and Jacobs's Incidents from the audited bank record, and it ends with a table and two verdicts, on which form reached furthest by 1861 and on which Truth text a historian may quote. The notebook page charts the five forms. The quick check, Two Texts of One Speech, tests the pint and quart argument, the refrain, and the choice between the records. The writing task turns the three asks into an essay from the evidence bank. The exit ticket has three parts. Next lesson opens with a repealed line on a map and a territory bleeding.")

dc.save(OUT)
