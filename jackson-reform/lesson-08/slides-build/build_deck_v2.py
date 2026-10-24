#!/usr/bin/env python3
"""Jackson and Reform Lesson 8 deck, "Women's Rights and Seneca Falls,"
built to the approved system: image-led slides, fragments only on screen,
comprehensive speaker notes, full lesson + vocabulary coverage."""
import os, sys, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags, photo_right,
                         divider_photo, content_photo, content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED, W, H)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

dc.IMG = os.path.join(HERE, 'img')
OUT = os.path.join(HERE, '..', 'lesson-08-slides.pptx')

# Verbatim definitions parsed from the unit spec, character for character
SPEC = open(os.path.join(HERE, '..', '..', 'build-scripts', 'unit-spec.md')).read()
sec = SPEC.split('### Lesson 8 (blueprint 15)')[1]
DEFS = []
for line in sec.splitlines():
    m = re.match(r'- (.+?): (.+)', line.strip())
    if m:
        DEFS.append((m.group(1), m.group(2).strip()))
DEFS = DEFS[:7]
D = dict(DEFS)
def joined(term):
    return term + ': ' + D[term]

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

LQ = 'Where did the women of 1848 get their argument, and what did they ask for first?'
EQ = "What did democracy mean in Jackson's America, who was it for, and what did the era's reformers claim it still owed?"

def content_photo_s(img, title, items, note, kick=None, size=21):
    s = slide(CREAM)
    photo_right(s, img)
    if kick: kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95 if kick else 0.8, 6.9, 1.2, title, size=31, color=NAVY, font='Georgia', leading=1.05)
    frags(s, items, y=2.12 if kick else 2.0, size=size, gap=11, leading=1.2)
    notes(s, note)
    return s

# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'JACKSON AND REFORM · LESSON 8', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, "Women's Rights and Seneca Falls", size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Where the women of 1848 got their argument, and what they asked for first', size=17, color=POWDER)
text(s, 0.9, 7.02, 11.9, 0.4, 'The Declaration of Independence, 1776, William Stone engraving facsimile. Wikimedia Commons.', size=11, color=POWDER)
notes(s, "The image is the Declaration of Independence of 1776, in the facsimile engraving William Stone made of the signed parchment. Open with the document rather than with a portrait, because the document is the lesson. In July 1848 Elizabeth Cady Stanton sat down with this text on the table and copied it sentence by sentence, changing its most famous sentence to read that all men and women are created equal. The lesson closes the unit. It begins with the law women lived under, follows their schooling inside abolition, an exclusion in London, and an argument printed in 1837, and it ends on July 20, 1848 with a convention, a declaration, and a list of first demands. It is the last content lesson of the unit, taught before the review day and the unit test, and it stops at December 1848.")

# 2 LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[(LQ, {})]], size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                (EQ, {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "The question has two halves and the lesson grades both. The first half is about sources. The women of 1848 did not invent their argument in the Wesleyan Chapel. They built it out of scripture, as Sarah Grimké had read it in print in 1837, and out of the Declaration of Independence, whose sentences Stanton rewrote in 1848, and they learned how to argue it inside a decade of antislavery work. The second half is about sequence. What they asked for first ran from a married woman's property, which New York had partly restored in April 1848, to immediate admission to all rights of citizens, with the vote as the furthest demand. Keep both halves of the question in view all hour, because every document in the lesson answers one of them, and the exit ticket grades both.")

# 3 LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'The argument, in seven stretches', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'The condition the law made', 'Coverture, and a wife civilly dead'),
        ('B', 'The school of antislavery', 'Societies, petitions, and the Grimké sisters'),
        ('C', 'London, 1840', 'Seats refused, and a promise in the gallery'),
        ('D', 'The argument in print', "Grimké's Letters, equality from creation"),
        ('E', 'A law moves first', "New York's property act, April 7, 1848"),
        ('F', 'Seneca Falls, July 1848', 'Five organizers, three hundred people, one text'),
        ('G', 'What they asked for first', 'Grievances, resolutions, and the narrow vote')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This is the map of the lesson, and it follows the guided notes section by section, so students can use the letters on screen to find their place in their notes all hour. Section A states the legal condition, coverture. Section B follows women through the antislavery movement that trained them. Section C sits in the London gallery of 1840 where Mott and Stanton met. Section D reads Grimké's printed argument of 1837. Section E reads a New York statute of April 1848. Section F calls the convention in July. Section G closes on the grievances, the resolutions, and the suffrage vote that passed by a narrow margin. Students will meet this same map again on the synthesis slide near the end of the deck, where the rows return in a different order as a check on the hour.")

# 4 A DIVIDER
divider_text('Section A', 'The Condition the Law Made',
             'Married, a woman was covered by her husband in law.',
             "Begin with the doctrine, because every later document in the lesson is written against it. Coverture came to America in the English common law and stood in every state in 1848. Its rule was simple to state and total in reach. A married woman's legal existence was covered by her husband's, as the definition in the guided notes puts it, so that her property, her wages, and her standing in court passed under his control. State the comparison the lesson returns to all hour. A single woman could hold property, sign a contract, and sue. Marriage, and marriage alone, removed those powers. The doctrine did not depend on any husband's cruelty. A kind husband held the same powers as a cruel one, because the powers were the law's gift.")

# 5 A CONTENT 1
content_text('Coverture: what marriage did in law',
             ['A single woman could hold property, contract, and sue.',
              'Marriage covered her legal existence with his.',
              'Her property passed under his control.',
              'Her wages belonged to him.'],
             "Work the fragments as a transfer, item by item, because students often hear coverture as an attitude when the lesson needs it as a legal mechanism. Nothing about the woman changed at the wedding except her legal person. The property she brought into the marriage, and anything she inherited during it, passed under her husband's control to use and to spend. Wages she earned belonged to him, a rule students should connect to the mill women of Lesson 5, whose pay a husband or father could claim. She could not bind herself by a contract, and she could not bring a suit in her own name. Hold the list on screen and ask what a reformer would have to change first: not manners, but statutes, which is where Sections E and G go.",
             kick='A · The condition the law made', size=24)

# 6 A CONTENT 2
content_text('Civilly dead, in the eye of the law',
             ["The Declaration's phrase called a married woman civilly dead.",
              'It stood in every state, from English common law.',
              'Kind or cruel, the powers were the same.',
              'The grievance list of 1848 was written against it.'],
             "Now give the condition its 1848 wording, because the phrase does work in the unit test and in the quick check. The Declaration of Sentiments charged that man has made woman, if married, in the eye of the law, civilly dead. The phrase is not a metaphor the convention invented for color. It is a lawyer's summary of the doctrine on the previous slide: no property, no wages, no contract, no standing in court of her own. Stanton had read law in her father's office and argued cases with his clerks as a girl, and the precision shows. Close the section by naming the habit the doctrine built. Because coverture was law everywhere, its defenders could call it nature. The rest of the lesson is the record of women answering that it was a statute, and statutes can be repealed.",
             kick='A · The condition the law made', size=24)

# 7 B DIVIDER
divider_photo('grimke-port.jpg', 'Section B', 'The School of Antislavery',
              ['Sarah Grimké, from a wood engraving', 'held by the Library of Congress.'],
              "The image is Sarah Grimké, in a wood engraving held by the Library of Congress, undated on its file page and presumed from her lifetime, 1792 to 1873. Section B answers a practical question: where did the organizers of 1848 learn to organize? They learned inside abolition. Through the 1830s women formed female antislavery societies in town after town, circulated the petitions that flooded Congress until the gag rule answered them in Lesson 7, raised the movement's money at antislavery fairs, and wrote for its newspapers. The work was public, it was skilled, and respectable opinion disapproved of all of it, which is the second lesson the school taught: the arguments ordering women silent were the same shape as the arguments defending slavery, and women noticed.")

# 8 B CONTENT 1
content_text('Societies, petitions, and fairs',
             ['Female antislavery societies formed from the 1830s.',
              'Petitions were signed by thousands.',
              "Fairs raised the movement's money.",
              'They gave a decade of practice in running a campaign.'],
             "Teach the 1830s as an apprenticeship with a curriculum. A female antislavery society had officers, a treasury, a correspondence, and a lecture program, all run by women who were told public business was not theirs. The petition campaigns taught canvassing at scale: signatures gathered door to door, rolls carried to Congress, and a right, petition, that women could exercise when they could not vote. The fairs taught finance and publicity. When five women sat down in Waterloo in July 1848 and called a convention on ten days of preparation, nothing in the work was new to them except the subject. Students who grasp this slide can answer the first half of the lesson question before the convention even appears: the argument came with an organization already trained to carry it.",
             kick='B · The school of antislavery', size=24)

# 9 B CONTENT 2
content_text('The Grimké sisters lecture, and are answered',
             ['They were Charleston daughters of a slaveholding judge.',
              'They lectured to men and women together in 1837.',
              'A pastoral letter ordered women to their sphere.',
              'The sisters answered in print, not in silence.'],
             "Sarah and Angelina Grimké carried the school's lesson furthest, and their definition belongs in this teaching in full. " + joined('Grimké sisters') + ". Add the sequence students must hold. The sisters' lectures to mixed audiences in 1837 were the first by American women on a public platform, and the Massachusetts clergy's pastoral letter answered them by ordering women back to dependence and silence. The sisters refused the order in writing. Angelina's Appeal had come first, in 1836, addressed to southern Christian women. Sarah's Letters followed, and Section D reads them. The pattern set here, a public act, a clerical rebuke, and a printed answer, is the pattern of the whole movement that follows.",
             kick='B · The school of antislavery', size=24)

# 10 C DIVIDER
divider_photo('mott-port.jpg', 'Section C', 'London, 1840',
              ['Lucretia Mott, photographed by', 'Frederick Gutekunst, circa 1870 to 1880.'],
              "The image is Lucretia Mott, photographed by Frederick Gutekunst of Philadelphia circa 1870 to 1880, from the Library of Congress copy: Mott in later life, in the plain Quaker dress she wore in 1840. Her definition anchors this section. " + joined('Lucretia Mott') + ". Section C tells the meeting behind that definition. In June 1840 the World's Anti-Slavery Convention gathered in London, the movement's world congress, and American societies that had named women as delegates expected them to sit. What happened on the first day turned two women's lives, and it is told at the next two slides from the lesson's teaching summary, which is built from the public record of the meeting.")

# 11 C CONTENT 1
content_text('The seats refused',
             ['Women were named as delegates by American societies.',
              'The convention voted to refuse their seats.',
              'A curtained gallery let them watch, and not speak.',
              'Garrison gave up his floor seat and joined them.'],
             "Work the sequence in order, because the order is the grievance. The women did not arrive as spectators hoping for a favor. Their societies had elected them delegates, with credentials like the men's. The convention debated their admission and voted to exclude them, and the hall then seated them in a gallery section set apart behind a curtain, present and silenced at once. William Lloyd Garrison, whose Liberator students met in Lesson 7, reached London after the vote, learned what had been done, and refused his own place on the floor to sit with the women in the gallery. Name what the vote taught the women in it. The movement that preached universal freedom had drawn its own line at sex, in public, by ballot, and the line could be answered only by a movement of their own.",
             kick='C · London, 1840', size=24)

# 12 C CONTENT 2
content_text('The promise in the gallery',
             ['Stanton was twenty-four, on her honeymoon.',
              'Mott was the veteran minister and abolitionist.',
              'They talked for days through the insult.',
              'They agreed on a convention on the rights of woman.'],
             "Introduce Stanton here, in the gallery, because Seneca Falls starts in this conversation and her definition is the lesson's. " + joined('Elizabeth Cady Stanton') + ". In 1840 she was twenty four, newly married to the abolitionist Henry Stanton, and in the gallery because wives watched. Mott took her up, preached where Stanton could hear her, the first sermon by a woman Stanton had ever heard, and the two talked through the exclusion day after day. Their conclusion was practical. Someday they would call a convention to discuss the rights of woman. Stanton remembered the promise as made in London. It waited eight years, for a move to Seneca Falls and a July visit, and Section F keeps it.",
             kick='C · London, 1840', size=24)

# 13 D DIVIDER
divider_text('Section D', 'The Argument in Print',
             "Grimké's Letters, 1837 and 1838: equality from creation.",
             "Section D slows down on a book, because the book is the first foundation of the 1848 argument and the activity's third station. Sarah Grimké wrote her Letters on the Equality of the Sexes as letters to Mary S. Parker, president of the Boston Female Anti-Slavery Society, in the summer and fall of 1837, and they were published as a book at Boston in 1838. Their occasion was the pastoral letter of that summer, in which the Congregational clergy of Massachusetts had answered the sisters' lecturing by fixing woman's sphere at dependence and silence, with scripture as the warrant. Grimké's answer met the clergy on their own ground. She went to the creation account in Genesis and argued the whole question from it, text by text, in print.")

# 14 D CONTENT 1
content_photo_s('grimke-port.jpg', 'Letter I: created equal',
             ['The Fall took innocence, and happiness.',
              'It did not take equality.',
              'Adam showed as much weakness as Eve.',
              "Subjection is man's doing, not God's design."],
             "Read Letter I closely, since the activity prints its central passage. Grimké examines the Fall, the text her opponents used to ground woman's subjection, and reverses its lesson. Had Adam reproved his wife instead of sharing her guilt, she writes, she might accord man the superiority he claims. As the record stands, Adam showed as much weakness as Eve. They both fell from innocence, and consequently from happiness, but not from equality. The sentence is built like a verdict, and students should hear its logic: the one event said to establish man's rule establishes no such thing. What followed the Fall, the dominion men exercise, is therefore a human arrangement, enlarged by men over centuries, and a human arrangement can be argued with, printed against, and changed.",
             kick='D · The argument in print')

# 15 D CONTENT 2
content_text('Two foundations, one claim',
             ['Grimké argued from creation, read in scripture, in 1837.',
              'Stanton argued from self-evident truths, 1776 copied in 1848.',
              'Each answered an opponent in his own book.',
              'Equality was an origin, not an invention.'],
             "Set the two foundations side by side before the lesson moves to statutes, because the writing task grades the comparison. Grimké argues from creation as scripture records it: the sexes were made equal, so subjection is man's usurpation. Stanton argues from the founding text of the republic: all are created equal and governments rest on consent, so she copies the Declaration of Independence and adds women to its sentence. The strategy is shared. Each writer takes the authority her audience already accepts, the Bible for the clergy's readers in 1837, the Declaration for citizens in 1848, and shows that the authority condemns the condition it is used to defend. Neither woman asks her audience to adopt a new principle. Each charges the audience with betraying its own.",
             kick='D · The argument in print', size=24)

# 16 E DIVIDER
divider_text('Section E', 'A Law Moves First',
             "New York, April 7, 1848: a wife's property, her own again.",
             "Section E changes the kind of evidence, from argument to statute, and the date deserves emphasis before the text. On April 7, 1848, three months before the Seneca Falls Convention met in the same state, New York enacted its Married Women's Property Act as chapter 200 of its session laws, titled an act for the more effectual protection of the property of married women. The law was not a gift dropped by legislators. Women and their allies, Ernestine Rose prominent among the petitioners from 1836 onward, had asked the legislature for it for more than a decade, and the state constitutional convention of 1846 had debated the subject and let it pass. The statute is short, four sections, and the activity prints two of them.")

# 17 E CONTENT
content_text('The property act, and its limits',
             ['Her property was sole and separate, as if single.',
              "It was not subject to her husband's disposal.",
              'It was not liable for his debts.',
              'It covered property only, not wages, contract, or the vote.'],
             "Its definition first, in the form the guided notes carry. " + joined("Married Women's Property Act") + ". Then work the limits as firmly as the gain, because the sequence of April and July is the lesson's closing argument. The act secured what a married woman owned and what came to her by gift or inheritance. It did not secure her wages, which waited for the amendment of 1860. It gave her no general power to make contracts or to sue in her own name, and it touched no man's vote and created no woman's. What it proved stood larger than its sections. Coverture, defended as the law of nature, had been amended by an ordinary statute, in the convention's own state, one season before the convention met. The women of July knew the law could move because it had just moved.",
             kick='E · A law moves first', size=24)

# 18 F DIVIDER
divider_photo('stanton-port.jpg', 'Section F', 'Seneca Falls, July 1848',
              ['Elizabeth Cady Stanton, from a', 'photographic print, Library of Congress.'],
              "The image is Elizabeth Cady Stanton, from a photographic print held by the Library of Congress. Section F keeps the London promise, and its facts are quickly told. Stanton had moved to Seneca Falls in 1847, to a house her father bought, and found the town quiet after Boston's abolitionist circles. In July 1848 Lucretia Mott came visiting her sister Martha Coffin Wright at nearby Waterloo. On Sunday, July 9, five women, Mott, Stanton, Wright, Mary Ann M'Clintock, and Jane Hunt, took tea at the Hunt house in Waterloo, and Stanton poured out, in her later account, the torrent of her indignation at the condition of women. Before the tea ended they had resolved to call the convention Mott and Stanton had promised in 1840, and to call it within the week, while Mott was still in the neighborhood.")

# 19 F CONTENT 1
content_text('Five organizers, ten days, one notice',
             ['They took tea at the Hunt house in Waterloo on July 9.',
              'A notice ran in the Seneca County Courier on July 11.',
              'It called them to discuss the condition and rights of woman.',
              'They met at the Wesleyan Chapel on July 19 and 20.'],
             "Work the speed of the call, because it shows the school of Section B in action. The notice in the Seneca County Courier of July 11 announced a convention to discuss the social, civil, and religious condition and rights of woman, the words the definition in the guided notes preserves, to be held at the Wesleyan Chapel in Seneca Falls on July 19 and 20. The chapel was the town's reform meeting place, an antislavery church whose doors stood open to unpopular causes. The convention's own definition belongs here in full. " + joined('Seneca Falls Convention') + ". Between the notice and the meeting the five women had a document to draft, and they drafted it at the M'Clintock house in Waterloo, around a mahogany table the family kept, with the Declaration of Independence open as the model.",
             kick='F · Seneca Falls, July 1848', size=24)

# 20 F CONTENT 2
content_photo_s('declaration-port.jpg', 'Copied from 1776',
             ['The Declaration of Sentiments was modeled sentence by sentence.',
              '"All men and women are created equal," it declared.',
              'Its grievances ran against man, as 1776 against a king.',
              'It was read aloud by Stanton on July 19.'],
             "Its definition belongs in this teaching in full, as the notes carry the vocabulary. " + joined('Declaration of Sentiments') + ". Teach the copying as a deliberate craft, not an imitation. Stanton kept the structure of 1776 whole: a preamble on why the causes must be declared, a statement of self-evident truths, a bill of grievances in a single repeated subject, he has, and a conclusion demanding a new station. She changed the subject of the tyranny from a king to man, and the plaintiffs from colonies to one portion of the family of man. The grievances then run the lesson's own order: the franchise refused, laws made without her voice, the married woman civilly dead, property and wages taken, employments monopolized, colleges closed. Students meet the full text at Station 1 of the activity, quoted from the audited bank record.",
             kick='F · Seneca Falls, July 1848')

# 21 STAT 300
stat('300', 'people at Seneca Falls, women and men',
     'About three hundred, in the Wesleyan Chapel, July 19 and 20, 1848',
     "Pause on the crowd, because its size and its composition both carry the lesson. About three hundred people came to a convention announced ten days earlier in a county newspaper, in a small canal town, in haying season. Many were local, Quaker families from the Waterloo and Seneca Falls meetings among them, and the abolitionist network of the burned-over district supplied the rest. Men were present from the first hour, some forty of them among the signers to come, and the convention needed one of them in the chair: James Mott presided on the first day because no woman present had ever chaired a mixed assembly, a fact the minutes record without embarrassment. The number rebukes two easy stories at once, that Seneca Falls was a handful of radicals in a parlor, and that it spoke for women alone. It was a public meeting of a community, called in the open and reported in the press.",
     kick='F · Seneca Falls, July 1848')

# 22 STAT 100
stat('100', 'signers of the Declaration of Sentiments',
     'Sixty eight women and thirty two men',
     "The second number is the signature count, and it has a story inside it that students should hear plainly. One hundred of those present signed the Declaration, sixty eight women and thirty two men, their names printed with the proceedings in the convention report that Station 2 of the activity prints from the audited bank record. In the weeks after the convention, under newspaper ridicule that reached across the country, some signers asked to have their names withdrawn, a fact Stanton recorded with anger in her own history of the movement. She refused to treat the withdrawals as the story. The signatures that stayed, and the report that carried them into print, made the convention a public act that could not be unheld. When students ask what a declaration does, the honest first answer is this: it gives its signers a position they must then decide, in public, whether to keep.",
     kick='F · Seneca Falls, July 1848')

# 23 G DIVIDER
divider_text('Section G', 'What They Asked For First',
             'Immediate admission to all rights of citizens, and the vote.',
             "Section G reads the convention's asks in their own order, because the lesson question's second half turns on sequence. The Declaration's grievances came first in the document, a bill of particulars against man modeled on the bill of 1776 against George the Third. The resolutions followed, a program rather than a protest: laws in conflict with woman's happiness to be void, clergy who confined women to be answered, the professions and the colleges to be opened, and over the whole list the convention's own summary demand, in the words of its report, that women have immediate admission to all the rights and privileges which belong to them as citizens of these United States. The word immediate came straight from abolition's vocabulary, the immediatism of Lesson 7, applied now to women. One resolution went beyond the rest, and the next two slides take it in order.")

# 24 G CONTENT 1
content_text('The grievances, then the program',
             ['First came the bill of grievances against man.',
              'Then came the resolutions, a program, not a protest.',
              'Laws against her were to be void, and employments opened.',
              '"Immediate admission to all rights of citizens" was the summary demand.'],
             "Distinguish the document's two halves as plainly as the convention did. The grievances prove a condition: the franchise refused, laws imposed without her voice, the wife civilly dead, wages taken, colleges closed. The resolutions propose the remedy, and their order is an argument about priority. Property stood already partly answered by the April statute in the same state, which is why the resolutions press past it to the whole standing of citizens. Admission to all rights and privileges, with the timing word immediate, is the convention's first ask stated as a principle: not a schedule of concessions granted one by one at men's convenience, but a standing to be recognized at once, from which particular statutes would then have to be rewritten, as New York had just rewritten one. The suffrage resolution tested how far that principle ran in the room itself.",
             kick='G · What they asked for first', size=24)

# 25 G CONTENT 2
content_photo_s('douglass-port.jpg', 'The resolution that nearly failed',
             ['Stanton insisted on demanding the elective franchise.',
              'Mott warned it would make them ridiculous.',
              'Douglass spoke for it on July 20.',
              'It carried by a narrow margin, alone among the resolutions.'],
             "The image is Frederick Douglass, photographed by George Kendall Warren circa 1879, three decades after he stood up at Seneca Falls. Tell the fight exactly as the record gives it. Stanton had written the suffrage demand into the resolutions before the convention met and held it there against nearly every ally's advice: Mott told her it would make the movement ridiculous, and her own husband left town rather than be present for it, as her memoir records. On the second day Douglass, the convention's famous guest, editor of the North Star at Rochester, rose and argued that the ballot was the right by which all other rights would be defended, for women as for his own people. The resolution carried by a narrow margin and was the only one not passed unanimously. It stood in the printed report, and it set the movement's furthest demand at its first meeting.",
             kick='G · What they asked for first')

# 26 VOCAB A
vocab('Words for the texts and the law',
      [('Seneca Falls Convention', 'the convention at Seneca Falls, July 19 and 20, 1848'),
       ('Declaration of Sentiments', 'the declaration of 1848, modeled on 1776'),
       ('coverture', 'the doctrine that covered a wife in law'),
       ("Married Women's Property Act", "New York, April 1848, a wife's property her own")],
      joined('Seneca Falls Convention') + ' ' + joined('Declaration of Sentiments') + ' ' + joined('coverture') + ' ' + joined("Married Women's Property Act"))

# 27 VOCAB B
vocab('Words for the women',
      [('Elizabeth Cady Stanton', 'the organizer who drafted the Declaration'),
       ('Lucretia Mott', 'the Quaker minister excluded at London in 1840'),
       ('Grimké sisters', 'Sarah and Angelina, abolitionist lecturers and writers')],
      "Three more terms, again matching the guided notes exactly, and all three are people, because the argument of this lesson had authors before it had a convention. " + joined('Elizabeth Cady Stanton') + ' ' + joined('Lucretia Mott') + ' ' + joined('Grimké sisters'))

# 28 SYNTHESIS
s = slide(NAVY)
kicker(s, 'The argument at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Condition, school, foundations, asks', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('Condition', 'Coverture', 'A wife civilly dead in the eye of the law'),
        ('School', 'Antislavery, and London 1840', 'The method learned, the seats refused'),
        ('Foundations', "Grimké 1837, and 1776 rewritten", 'Creation, and self-evident truths'),
        ('Proof', 'The property act, April 1848', 'The law moved, in the same state'),
        ('Asks', 'Seneca Falls, July 1848', 'Immediate admission, and the franchise')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the guided notes table, The Argument at a Glance, and students should complete that table now, from memory where they can and from the lesson where they must. The five rows compress the hour and close the unit. Condition: coverture made a wife civilly dead in law. School: antislavery work trained the organizers, and London showed them their exclusion in a curtained gallery. Foundations: Grimké argued created equality from scripture in 1837, and Stanton rewrote the truths of 1776 in 1848. Proof: New York's property act of April 1848 showed the law could move. Asks: the convention demanded immediate admission to all rights of citizens and carried the franchise by a narrow margin. The guided notes table uses these same five rows, so the chart students keep in their notebooks and the summary on screen cannot drift apart.")

# 29 EXIT
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Work the Seneca Falls file', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Where did the women of 1848 get their argument, and what did they ask for first? Work the five records in order, then answer both halves of the question from the file.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Seneca Falls File: the declaration, the report, Grimké, the property act, and London'),
        ('Notebook', 'Notebook page: what each piece says, where it came from, and what it left to win'),
        ('Quick check', 'Civilly Dead: a grievance of July read against a statute of April'),
        ('Writing', 'The Argument They Borrowed: an answer weighed from at least three bank documents')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: coverture stated, London stated, and the lesson question answered from both foundations.',
     size=15, color=POWDER)
notes(s, "Close by handing the lesson to the work. The activity, The Seneca Falls File, runs five stations: the Declaration of Sentiments and the convention report, both from the audited bank records, Grimké's Letter I from the Boston edition of 1838, the New York property act from the session laws, and a labeled teaching summary of the London exclusion, ending in a table of what each record supplied and a defended answer to the lesson question. The notebook page holds what each piece says, where it came from, and what it left to win. The quick check, Civilly Dead, reads a grievance of July against a statute of April. The writing task, The Argument They Borrowed, requires an answer from at least three bank documents and a reply to the strongest claim of the other side. The exit ticket has three parts, as printed at the end of the guided notes.")

dc.save(OUT)

from pptx import Presentation
prs2 = Presentation(OUT)
counts = []
for i, sl in enumerate(prs2.slides, 1):
    t = sl.notes_slide.notes_text_frame.text if sl.has_notes_slide else ""
    counts.append(len(t.split()))
print("slides:", len(counts), "notes min:", min(counts), "max:", max(counts), "total:", sum(counts))
print(counts)
# verify every term verbatim in notes
allnotes = " ".join(sl.notes_slide.notes_text_frame.text for sl in prs2.slides)
for term, dfn in DEFS:
    print(term, "VERBATIM" if (term + ': ' + dfn) in allnotes else "MISSING")
