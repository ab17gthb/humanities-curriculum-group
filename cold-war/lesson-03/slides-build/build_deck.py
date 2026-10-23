#!/usr/bin/env python3
"""Cold War Lesson 3 deck builder. Image led deck: McCarthy and Cohn title, Trumbo photograph, McCarthy portrait, Army-McCarthy hearings crops."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
LESSON_DIR = os.path.dirname(HERE)
UNIT_DIR = os.path.dirname(LESSON_DIR)
sys.path.insert(0, UNIT_DIR)
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags,
                         divider_photo, content_photo, content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED, W, H)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

dc.IMG = os.path.join(HERE, 'img')
OUT = os.path.join(LESSON_DIR, 'lesson-03-slides.pptx')

spec = open(os.path.join(UNIT_DIR, 'build-scripts', 'unit-spec.md')).read()
sec = spec.split('### Lesson 3')[1].split('### Lesson 4')[0]
TERMS = []
for line in sec.splitlines():
    line = line.strip()
    if line.startswith('- '):
        t, d = line[2:].split(': ', 1)
        TERMS.append((t.strip(), d.strip()))
assert len(TERMS) == 7, TERMS
TD = dict(TERMS)

def vocab(title, terms, note, kick='The vocabulary'):
    s = slide(CREAM)
    kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95, 11.5, 1.0, title, size=30, color=NAVY, font='Georgia')
    yy = 2.1
    for term, dfn in terms:
        text(s, 0.9, yy, 4.1, 0.9, term, size=24, color=NAVY, font='Georgia')
        text(s, 5.15, yy + 0.06, 7.3, 1.1, dfn, size=18, color=MUTED, leading=1.2)
        yy += 1.52
    notes(s, note)
    return s

SHORT = {
 'Second Red Scare': 'fear of Communist infiltration, and the investigations, tests, and blacklists it produced',
 'House Un-American Activities Committee': 'the House committee that investigated alleged Communist influence, most famously in Hollywood in 1947',
 'loyalty oath': 'a sworn statement of loyalty and denial of Communist membership, required of many workers',
 'Hollywood Ten': 'the ten who refused HUAC in 1947, were cited for contempt of Congress, and went to prison',
 'blacklist': 'a list of people barred from work in an industry over suspected Communist ties',
 'McCarthyism': 'public accusations of Communist disloyalty without firm evidence, named for Senator McCarthy',
 'Army-McCarthy hearings': 'the televised Senate hearings of 1954, watched by millions, after which the Senate censured McCarthy',
}

# 1 TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'THE COLD WAR · LESSON 3', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, 'The Red Scare at Home', size=30, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'Loyalty oaths, a blacklist, a list that changed, and 36 days on television. How fear of communism rebuilt American life.', size=17, color=POWDER)
notes(s, "Open with the photograph. It shows Senator Joseph McCarthy with his chief counsel Roy Cohn at the Army-McCarthy hearings on March 12, 1954, near the end of the story this lesson tells. Lessons 1 and 2 followed the Cold War abroad, containment in Europe and a shooting war in Korea. This lesson brings the rivalry home. Between 1947 and 1954 the United States built a machinery for testing the loyalty of its own citizens, and millions of Americans met that machinery at work, in a hearing room, or on a television screen. Set the two cautions that govern the whole lesson. Soviet espionage was real, and the fear had genuine fuel. The machinery built to answer it also punished people on suspicion and association, and students will have to hold both records at once, because the lesson question grades exactly that double judgment.")
# 2 QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('How did the fear of communism change American life at home, and what ended the scare?', {})]], size=42, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': RUST_LT, 'italic': True}), ('How did the struggle between the United States and the Soviet Union reshape the world and American life, and why did it end the way it did?', {'italic': True})]], size=17, color=POWDER, font='Georgia', leading=1.2)
notes(s, "Read the lesson question aloud and separate its two halves, because the exit ticket and the writing task grade them separately. The first half asks how American life changed, and the answer is institutional, not atmospheric. Workers were investigated, oaths were signed, witnesses were jailed for refusing questions, and careers ended on lists no court had approved. An answer that says people were frightened has named a feeling, not a change, and should not earn full credit. The second half asks what ended the scare, and the honest answer is narrower than students expect. Television and a Senate vote ended McCarthy's campaign in 1954. The wider machinery faded slowly, and some of its questions were never settled. Connect the question to the unit question beneath it. The American life half of the unit question is built here, in the loyalty office and the hearing room.")
# 3 MAP
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.28, 11.5, 1.0, 'Fuel, machinery, cases, and the turn', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('A', 'Fuel for the Fear', 'The Soviet bomb, the fall of China, Korea, and real espionage'),
        ('B', 'The Loyalty Program', 'Executive Order 9835, investigations, boards, and oaths'),
        ('C', 'HUAC Comes to Hollywood', 'Friendly and unfriendly witnesses, the Hollywood Ten'),
        ('D', 'The Blacklist and the Wider Reach', 'Careers ended on suspicion, far beyond film'),
        ('E', 'The Spy Cases', 'Hiss convicted of perjury, the Rosenbergs executed'),
        ('F', 'McCarthy and the List That Changed', 'Wheeling 1950, accusation as a national campaign'),
        ('G', 'Television, Censure, and the Reckoning', '36 days on camera, Welch, and a 67 to 22 vote')]
yy = 2.66
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.6, n, size=22, color=RUST_LT, font='Georgia')
    text(s, 1.6, yy + 0.02, 4.9, 0.6, t, size=19, color=CREAM, bold=True)
    text(s, 6.65, yy + 0.06, 5.8, 0.6, d, size=15, color=POWDER)
    yy += 0.635
notes(s, "This map follows the guided notes section by section. Section A supplies the fuel, because students who skip it judge the scare as an invention, which it was not. Sections B, C, and D build the machinery in order: a presidential loyalty program, a congressional committee at work in Hollywood, and a private blacklist that punished without a trial. Section E covers the two spy cases that kept the fear credible to millions of Americans. Section F follows the senator who turned accusation into a national campaign, and section G closes with the turn, the televised hearings, the decency exchange, and the Senate vote. Tell students to track one distinction through every section: the claim made, and the evidence shown for it. The activity, The Investigation File, grades exactly that distinction on five documents, and the writing task rewards it in essay form.")
# 4 DIVIDER A
divider_text('Section A', 'Fuel for the Fear', 'The Soviet bomb and the fall of China in 1949, war in Korea in 1950, and espionage that was real.',
 "Teach this section as the correction to the easiest version of the story, in which frightened Americans invented a danger from nothing. Three shocks landed in ten months. The Soviet atomic test of August 1949 ended the American monopoly years earlier than officials had expected. The Communist victory in China weeks later put the most populous country on earth in the opposing camp, and American politics immediately asked who had lost it. The Korean invasion of June 1950 then turned the contest into a shooting war. Behind the shocks stood genuine espionage. Soviet agents had passed atomic secrets to Moscow, and American codebreakers held evidence of spy networks that the government could not display in open court without exposing its sources. The fear that follows in this lesson grew from that soil. Its machinery still has to be judged on its own record, which is the work of sections B through D.")
# 5 CONTENT A
content_text('Three shocks in ten months', ['Soviet atomic bomb tested, August 1949', "People's Republic of China proclaimed, 1949", 'North Korea invades South Korea, June 1950', 'Soviet espionage was real, including atomic secrets', 'Fear abroad became fear at home'],
 "Carry the definition exactly as the guided notes print it. The Second Red Scare is this: " + "Second Red Scare: " + TD['Second Red Scare'] + ". Then walk the shocks as a sequence, because their order explains the politics. The bomb came first and broke the assumption that time was on the American side. China came second and gave the opposition a question with no good answer: a country of hundreds of millions had gone Communist on this administration's watch. Korea came third and made the first two feel like a pattern rather than a run of bad luck. Add the espionage carefully. The government knew more than it could prove in public, because its best evidence came from secret codebreaking. That gap between what officials suspected and what they could show is the space in which the machinery of the next sections operated.")
# 6 DIVIDER B
divider_text('Section B', 'The Loyalty Program', 'Executive Order 9835 in March 1947: an investigation for every new federal worker, and boards to judge the rest.',
 "Frame the loyalty program as the scare's foundation, laid by a Democratic president three years before McCarthy spoke at Wheeling. That date does heavy work in this lesson. When students later meet McCarthy, they should understand that he joined a system already running, with its forms, its boards, and its lists already in place. President Truman acted under real pressure. Republicans had won Congress in 1946 campaigning partly on Communist infiltration, a federal employee had been caught passing documents toward Soviet contacts in the Amerasia case, and Truman wanted the issue handled by his own administration rather than by Congress. His order promised two protections at once, protection against infiltration and protection against unfounded accusation. The section standard is whether students can state both promises and then see, in the standard the boards applied, why the second promise was the harder one to keep.")
# 7 CONTENT B
content_text('Checked by the millions', ['Executive Order 9835, March 1947', 'A loyalty investigation for every new federal worker', 'FBI files and committee files consulted', 'Association with a listed group could count against a worker', 'Loyalty oaths signed across the workforce'],
 "Carry the definition exactly. A loyalty oath is this: " + "loyalty oath: " + TD['loyalty oath'] + ". Then make the program concrete at the level of one worker. A clerk applying for a federal job in 1948 faced a check of FBI files, committee files, former employers, and schools. If investigators found derogatory information, a loyalty board heard the case, sometimes on evidence from informants the worker could not confront. The board's question was not whether the worker had committed a crime. It was whether reasonable grounds existed for believing the worker disloyal, and membership in, affiliation with, or sympathetic association with an organization the Attorney General listed as subversive could supply those grounds. Millions were checked under the program. A few hundred lost federal jobs on loyalty grounds, and many more resigned while under investigation, a figure students should keep beside the dismissal count.")
# 8 DIVIDER C
divider_photo('trumbo-port.jpg', 'Section C', 'HUAC Comes to Hollywood', ['October 1947: friendly witnesses named names, and ten witnesses refused the question.'],
 "Introduce the hearings through the man in the photograph, screenwriter Dalton Trumbo at the House Un-American Activities Committee hearings in 1947, because his exchange with the chairman is the clearest record of the collision this section teaches. The committee chose Hollywood deliberately. Film reached every town in the country, studio heads feared the publicity, and a hearing in Washington could command newspaper coverage no investigation of a school board could match. The committee's witnesses came in two kinds, and students must keep the kinds separate. Friendly witnesses answered and named colleagues. Unfriendly witnesses were called to be asked one question, whether they were now or had ever been members of the Communist Party, and to be pressed for the names of others. Ten of them had agreed together to refuse, on First Amendment grounds. What the committee did with that refusal is the section's legal core.")
# 9 CONTENT C
content_photo('trumbo-port.jpg', 'The question and the refusal', ['HUAC hearings on the film industry, October 1947', 'Friendly witnesses named colleagues', 'The question: party membership, now or ever', 'The Hollywood Ten refused on First Amendment grounds', 'Cited for contempt of Congress, and sent to prison'],
 "Carry both definitions exactly. The House Un-American Activities Committee is this: " + "House Un-American Activities Committee: " + TD['House Un-American Activities Committee'] + ". The Hollywood Ten are these: " + "Hollywood Ten: " + TD['Hollywood Ten'] + ". Then slow down on the refusal, because its legal logic is the point students miss. The Ten did not plead the Fifth Amendment protection against self incrimination. They argued that the First Amendment barred Congress from asking about beliefs and associations at all, which made their cases a direct test of the committee's right to ask. The House cited all ten for contempt of Congress in November 1947. Appeals failed, and in 1950 the ten went to prison for terms of six months to a year. Their stand was principled and it was costly, and the next section prices the second cost, the one paid at work rather than in court.")
# 10 DIVIDER D
divider_text('Section D', 'The Blacklist and the Wider Reach', 'No trial, no charge to answer, and no work: the list did what the hearing room could not.',
 "Teach the blacklist as a private punishment built on public machinery, because that partnership is what made it so hard to fight. The hearings supplied the names and the suspicion. The studios, networks, and sponsors supplied the penalty, and because the penalty came from employers rather than from a court, there was no indictment to answer, no evidence to test, and no verdict to appeal. A worker cleared in one place could stay listed in another, since the lists circulated through newsletters, consultants, and sponsor offices rather than through any single official register. The section also widens the map beyond Hollywood, which is where students tend to leave the scare. The same combination of oath, hearing, and list reached teachers who would not sign state loyalty oaths, union members expelled in anti-Communist purges, and public workers at every level of government. The scare's largest costs were paid in ordinary workplaces.")
# 11 CONTENT D
content_text('Punished without a trial', ['Studio heads barred the Ten, November 1947', 'Lists circulated in film and broadcasting', 'Named for membership, petitions, or association', 'Hundreds lost work with no charge to answer', 'Teachers and union members faced the same machinery'],
 "Carry the definition exactly. A blacklist is this: " + "blacklist: " + TD['blacklist'] + ". Then distinguish the kinds of names the lists carried, because the mixture is the injustice students should be able to describe precisely. Some listed workers had belonged to the Communist Party, which was legal membership in a legal party. Some had signed petitions or joined organizations, a peace group, a refugee relief committee, a writers league, that later appeared on the Attorney General's list. Some were named by informants whose accounts they never saw. A few worked again under false names; Dalton Trumbo wrote scripts credited to other men. Many simply left the industry. The clearance system that grew up around the lists, in which a named worker hired a lawyer and published a letter of explanation, shows the blacklist's real character: employment depended on satisfying private gatekeepers that one's past associations were acceptable.")
# 12 DIVIDER E
divider_text('Section E', 'The Spy Cases', 'Hiss and the Rosenbergs: the two cases that kept the fear credible, and argued over ever since.',
 "Introduce the two cases as the scare's strongest fuel after 1949, because each one seemed to confirm the central claim that Communists had reached inside the American government and its most secret project. Handle them at different weights, and tell students why. The Hiss case was about credibility: a polished former State Department official, accused by a confessed former courier, convicted not of espionage but of lying about it under oath. The Rosenberg case was about the atomic secret itself, and it ended at the electric chair, which raised every argument about evidence and punishment to its highest pitch. Historians still argue over both cases, and later evidence, including decrypted Soviet cables released decades later, has strengthened parts of the prosecution record while leaving the arguments over Ethel Rosenberg's role and over both sentences alive. The lesson standard is to state what each jury decided, what the cases rested on, and what remains argued.")
# 13 CONTENT E1
content_text('Hiss: convicted of lying', ['Alger Hiss, former State Department official', 'Accused of passing documents to a Soviet agent', 'Denied the charge under oath', 'Convicted of perjury, January 1950', 'His case convinced millions the threat was inside'],
 "Walk the Hiss case as a contest of credibility that the country watched like a trial of the New Deal itself. Whittaker Chambers, a former Communist courier, told the House committee in 1948 that Hiss had passed State Department documents to him in the 1930s, and he later produced copies of documents he said Hiss had given him. Hiss denied everything under oath. The espionage charge itself was barred by time, so prosecutors charged the lie. Two trials followed; the first jury could not decide, and the second convicted Hiss of perjury in January 1950. He served more than three years in prison and maintained his innocence for the rest of his life. For this lesson, the case's political effect outweighs its legal one. Weeks before McCarthy spoke at Wheeling, the conviction of a man who had stood near the center of the wartime government made the senator's larger charges sound plausible to Americans who wanted evidence that infiltration was real.")
# 14 CONTENT E2
content_text('The Rosenbergs: convicted and executed', ['Tried in 1951 for conspiracy to pass atomic secrets', "The key witness: Ethel's brother, David Greenglass", 'Greenglass described sketches passed to Julius', 'Both convicted, and sentenced to death', 'Executed in June 1953, argued over ever since'],
 "Walk the Rosenberg case from its evidence outward, because the activity asks students to separate the verdict from the argument. David Greenglass had machined parts at Los Alamos and confessed to passing information; his testimony put sketches of the bomb project in Julius Rosenberg's hands through the courier Harry Gold, and put Ethel at a typewriter preparing notes. The defense answered that Greenglass, facing his own sentence, had bought leniency by enlarging his sister's part. The jury convicted both Rosenbergs in March 1951, Judge Kaufman imposed death sentences, and appeals and clemency campaigns failed. Both were executed at Sing Sing on June 19, 1953, the first American civilians put to death for espionage in peacetime. Keep two later facts in view without letting them swallow the trial: Soviet cables released in the 1990s confirmed that Julius ran a spy network, and Greenglass late in life said he could not recall Ethel typing the notes his testimony described. The argument over her sentence continues on exactly that ground.")
# 15 DIVIDER F
divider_photo('mccarthy-port.jpg', 'Section F', 'McCarthy and the List That Changed', ['Wheeling, February 9, 1950: a senator, a list in his hand, and a number that would not stay still.'],
 "Introduce McCarthy through the precision rule this section exists to teach: his numbers were claims, and students must repeat them as claims, never as findings. The photograph shows him in February 1954, still telling reporters he would not change his tactics, four years after Wheeling. At Wheeling he was a first term senator with a weak reelection record who needed an issue, speaking to a Republican women's club on Lincoln Day. What he said there reached Washington through wire reports the next morning, and its vagueness was its strength: a list existed, he had held it, and the State Department was infested. Senators demanded he substantiate the charge, and when he read the speech into the Congressional Record eleven days later the printed number differed from the number reporters had heard. The section follows that moving number, because the lesson's central evidence skill is watching what a claim does when it is asked for proof.")
# 16 CONTENT F
content_photo('mccarthy-port.jpg', 'Accusation as evidence', ['Wheeling speech, February 9, 1950', 'Reporters heard one number at Wheeling', 'The Congressional Record text spoke of 57 cases', 'The Senate committee found no Communists in the department', 'Four years at the center of national politics'],
 "Carry the definition exactly. McCarthyism is this: " + "McCarthyism: " + TD['McCarthyism'] + ". Then trace the claim's career, because the career is the evidence lesson. The Tydings committee, assigned to check the charges, reported in 1950 that it had found no Communists in the State Department and called the charges a fraud and a hoax. McCarthy answered by accusing the committee itself, campaigned against Senator Tydings in Maryland, and helped defeat him. Other officeholders drew the intended conclusion, and for four years few challenged McCarthy directly while his committee investigated the Army, the Voice of America, and overseas libraries. Note the institutional fact students often miss: McCarthy never ran the House committee of section C and never controlled the loyalty program of section B. His power was publicity, the hearing as theater and the charge as headline, which is why television, the same medium, was able to end him.")
# 17 STAT F
stat('57 cases', 'the number in the Congressional Record text of the Wheeling claim', "Reporters at Wheeling heard a claim of 205 names. Both figures are claims by McCarthy, stated here as claims, not as findings",
 "Stop on this slide and make the class do the source work out loud. Two numbers attach to the most famous accusation of the era, and they come from two different records of the same speech. Reporters present at Wheeling on February 9, 1950 heard McCarthy claim a list of 205 names. When he read the speech into the Congressional Record on February 20, the printed text said he held 57 cases. The audited bank record used in the activity carries the Record text, and its headnote carries the reporters' figure, so students can see both in one place. Ask what a careful writer does with the pair. The answer is the lesson rule: state each figure with its source attached, call both of them claims, and record that the Senate committee assigned to check the charges found no Communists in the department. A number repeated without its source is how McCarthyism worked, and this class will not work that way.")
# 18 DIVIDER G
divider_photo('cohn-port.jpg', 'Section G', 'Television, Censure, and the Reckoning', ['The Army fought back, the cameras came in, and the country watched for 36 days.'],
 "Introduce the ending as a fight McCarthy picked with the wrong institution. The photograph shows McCarthy with Roy Cohn, his chief counsel, at the hearings in March 1954. Cohn had pressed the Army for special treatment for G. David Schine, a former committee aide drafted as a private, and the Army answered with a written chronology of the pressure. McCarthy countercharged that the Army was holding Schine hostage to stop the investigation of Communists in its ranks. The Senate subcommittee took up both sets of charges with McCarthy temporarily off the chair, and it admitted television cameras for the whole proceeding. That decision is the hinge of the section. McCarthy's power had always depended on controlling the report of a hearing after it ended. Live television removed the filter: viewers watched the interruptions, the needling, and the evasions themselves, day after day, and formed the judgment the newspapers had once formed for them.")
# 19 CONTENT G
content_text('The room turns, then the Senate votes', ['Army-McCarthy hearings, 36 days on television, 1954', 'Millions watched McCarthy bully witnesses', 'Welch answers for Fred Fisher, June 9', 'The Senate condemns his conduct, December 1954', 'His power collapses; the scare fades slowly'],
 "Carry the definition exactly. The Army-McCarthy hearings are these: " + "Army-McCarthy hearings: " + TD['Army-McCarthy hearings'] + ". Then tell the June 9 exchange as the room experienced it. McCarthy, pressed by the Army's lawyer Joseph Welch, struck at Fred Fisher, a young lawyer in Welch's firm who had once belonged to the National Lawyers Guild and had already been sent home from the Army's team. Welch answered that until that moment he had never gauged McCarthy's cruelty or recklessness, and closed by asking whether the senator had no sense of decency. The room applauded, which Senate hearing rooms do not do. In December the Senate voted 67 to 22 to condemn McCarthy's conduct, a vote the record treats as a censure. He kept his seat and lost everything else: the chairmanship, the cameras, and the fear of him.")
# 20 STAT G1
stat('36 days', 'of televised Army-McCarthy hearings in 1954', "Two networks carried the proceedings live, and millions of Americans formed their own judgment of the methods of McCarthy",
 "Teach the 36 days as a change in who judged the evidence. Before 1954, most Americans met a hearing through a headline and a summary written by someone else, and McCarthy was skilled at supplying both in advance. Across 36 days that spring, two networks carried the subcommittee live for more than 180 hours in total, and the audience watched procedure itself: the interruptions counted aloud by Chairman Mundt, the long pauses, the point of order calls, and the treatment of witnesses who had no counsel's protection. Edward R. Murrow's television report that March had already shown viewers a McCarthy assembled from his own filmed performances. The hearings completed the work at full length. Students should connect the figure to the mechanism: the scare at its height ran on accusation reported secondhand, and it broke when the accusation could be watched firsthand by the whole country at once.")
# 21 STAT G2
stat('67 to 22', "the Senate vote to condemn the conduct of McCarthy, December 1954", 'A censure in effect. He kept his seat, and lost the chairmanship, the cameras, and his power',
 "Be exact about what this vote was and was not, because students routinely overstate it. The Senate did not expel McCarthy, remove him from office, or rule on the truth of his charges against the State Department. On December 2, 1954 it voted 67 to 22 to condemn his conduct toward Senate colleagues and committees as contrary to senatorial traditions, which the institution and the press treated as a censure. The narrowness of the charge is part of its meaning: the Senate judged the method, in its own house, on its own rules. The consequences were still complete. McCarthy lost his committee chairmanship when the Senate changed hands, reporters stopped attending his hearings, and he died in 1957 with his influence long gone. The scare itself faded more slowly. Loyalty programs, oaths, and lists outlasted him by years, and the Supreme Court narrowed their legal tools only in the later 1950s.")
# 22 GLANCE
s = slide(NAVY)
kicker(s, 'The scare at a glance')
text(s, 0.9, 1.28, 11.5, 1.0, 'Machinery, cases, and the turn', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.36)
rows = [('The machinery', 'Loyalty program, HUAC, oaths, and the blacklist', 'Jobs lost on suspicion and association'),
        ('The cases', 'Hiss convicted of perjury; the Rosenbergs executed', 'Real espionage argued beside thin evidence'),
        ('The campaign', 'Wheeling 1950 and four years of accusation', 'A list whose number changed as it was repeated'),
        ('The turn', '36 televised days, Welch, and the Senate vote', 'Conduct condemned 67 to 22 in December 1954')]
yy = 2.78
for t, d, why in rows:
    text(s, 0.9, yy, 2.9, 0.7, t, size=22, color=CREAM, font='Georgia')
    text(s, 3.95, yy + 0.05, 4.3, 0.9, d, size=16, color=POWDER, leading=1.2)
    text(s, 8.45, yy + 0.05, 4.0, 0.9, why, size=16, color=POWDER, leading=1.2)
    yy += 1.05
notes(s, "This slide mirrors the closing table of the guided notes, and students should complete that table now from memory where they can. The guided notes table, The Scare at a Glance, groups the lesson into the machinery, the cases and the campaign, and the turn. Check the table with the two questions that expose shallow answers. First, which rows existed before Senator McCarthy spoke at Wheeling? The machinery row and most of the cases row, which is why a McCarthy alone account of the scare fails. Second, which row ended on evidence and which on conduct? The cases row ended in court verdicts, argued over still, while the campaign ended in a conduct vote that deliberately left the underlying charges untried. The table is a map of one system: fuel at the top, institutions in the middle, and a public judgment at the end that settled less than it seemed to settle.")
# 23 VOCAB A
vocab('Words for the machinery', [(t, SHORT[t]) for t in ['Second Red Scare', 'House Un-American Activities Committee', 'loyalty oath', 'Hollywood Ten']],
 "Four terms, matching the guided notes word for word, and students should copy the definitions because the unit test draws on them. Second Red Scare: " + TD['Second Red Scare'] + ". House Un-American Activities Committee: " + TD['House Un-American Activities Committee'] + ". Loyalty oath: " + TD['loyalty oath'] + ". Hollywood Ten: " + TD['Hollywood Ten'] + ". Press the first term hardest, because it names the whole lesson: the definition joins a fear to its products, investigations, loyalty tests, and blacklists, and an answer that keeps the fear and drops the products has cut the term in half.")
# 24 VOCAB B
vocab('Words for the campaign and the turn', [(t, SHORT[t]) for t in ['blacklist', 'McCarthyism', 'Army-McCarthy hearings']],
 "Three more terms, again matching the guided notes exactly. Blacklist: " + TD['blacklist'] + ". McCarthyism: " + TD['McCarthyism'] + ". Army-McCarthy hearings: " + TD['Army-McCarthy hearings'] + ". Two details in these definitions earn emphasis before the exit ticket. The McCarthyism definition turns on the words without firm evidence: the term judges an evidence practice, not a political position, and students should use it with that precision. The hearings definition ends with the Senate's censure, which keeps the ending institutional rather than personal: a lawyer's question turned the room, and a vote of the Senate ended the campaign.")
# 25 SYNTHESIS
content_text('Answering the question', ['The change: investigations, oaths, hearings, prison, and the blacklist', 'The fuel: the bomb, China, Korea, and real espionage', 'The method: accusation repeated, numbers stated as claims', 'The ending: 36 days on television and a 67 to 22 vote'],
 "Run the synthesis as the writing task rehearsal, and build it from the class's own answers before summarizing. Strong answers hold two records at once and refuse to drop either. The first record is the fuel: a Soviet bomb, a Communist China, a war in Korea, and espionage that decrypted cables later confirmed was real. The second record is the machinery: millions investigated, oaths required, ten men jailed for refusing a question, hundreds blacklisted without a trial, and a senator whose numbers changed as he repeated them. The ending belongs to the second record, not the first. Television showed the method, Welch named it in the room, and the Senate condemned the conduct 67 to 22. Test the synthesis once against its two rivals before closing. The scare was not invented, and it was not justified in full. An essay that cannot hold both halves has not yet answered the question.")
# 26 CLOSING
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'Answer the question', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4, ['How did the fear of communism change American life at home, and what ended the scare?'], size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'The Investigation File: five documents, claim against evidence, then a verdict'),
        ('Notebook', 'Notebook page: the scare chart, claim or charge against evidence or result'),
        ('Quick check', 'Decency on Television: the Welch photograph, sourced and placed in 1954'),
        ('Writing', 'Judging the Scare: the machinery and the ending in one essay')]
yy = 4.15
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=18, color=CREAM)
    yy += 0.62
text(s, 0.9, 6.85, 11.5, 0.5, 'Exit ticket: the Second Red Scare defined, HUAC and the Hollywood Ten, and the lesson question in two or three sentences.', size=15, color=POWDER)
notes(s, "Close by handing the lesson to the work. In the activity, The Investigation File, each group separates the claim from the evidence in five documents, the Wheeling speech, the Trumbo exchange, the loyalty order and oath, the Rosenberg case summary, and the Welch exchange, then ranks the file and defends the document that shows the scare at its most defensible and the one that shows it at its least. The notebook page rebuilds the scare as a chart of what happened, the claim or charge, and the evidence or result. The quick check, Decency on Television, sources the Senate photograph of Welch and McCarthy and tests whether students can place one famous day inside the wider machinery. The writing task, Judging the Scare, requires the double judgment of the lesson in essay form. The exit ticket has three parts: the Second Red Scare defined with Truman's 1947 program named, the Hollywood committee and the fate of the Ten, and the lesson question answered in two or three sentences.")

dc.save(OUT)
