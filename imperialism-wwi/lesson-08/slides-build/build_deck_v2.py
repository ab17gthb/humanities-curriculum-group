#!/usr/bin/env python3
"""Lesson 8 deck, "Wilson's Peace and the Turn Inward," built to the approved
Progressive Era pilot system: image-led slides, fragments only on screen,
comprehensive speaker notes, full lesson + vocabulary coverage.
Fonts: Georgia titles, Lato body."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
import deck_common as dc
from deck_common import (slide, rect, text, notes, kicker, rule, frags, photo_right,
                         divider_photo, content_photo, content_text, stat, divider_text,
                         NAVY, CREAM, RUST, RUST_LT, POWDER, INK, MUTED, W, H)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

HERE = os.path.dirname(os.path.abspath(__file__))
dc.IMG = os.path.join(HERE, 'img')
OUT = os.path.join(HERE, '..', 'lesson-08-slides.pptx')

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

def content_photo_s(img, title, items, note, kick=None, size=21):
    s = slide(CREAM)
    photo_right(s, img)
    if kick: kicker(s, kick, color=RUST)
    text(s, 0.9, 0.95 if kick else 0.8, 6.9, 1.2, title, size=31, color=NAVY, font='Georgia', leading=1.05)
    frags(s, items, y=2.15 if kick else 2.0, w=6.9, size=size)
    notes(s, note)
    return s

# ---------------------------------------------------------------- 1 · TITLE
s = slide(NAVY)
s.shapes.add_picture(os.path.join(dc.IMG, 'title-169.jpg'), 0, 0, Inches(13.333), Inches(7.5))
rect(s, 0, 5.05, W, 2.45, NAVY)
rect(s, 0, 5.05, W, 0.045, RUST)
text(s, 0.9, 5.32, 11.5, 0.4, 'IMPERIALISM AND WORLD WAR I · LESSON 8', size=14, color=RUST_LT, font='Arial', bold=True)
text(s, 0.9, 5.68, 11.9, 1.1, "Wilson's Peace and the Turn Inward", size=40, color=CREAM, font='Georgia')
text(s, 0.9, 6.62, 11.5, 0.5, 'The League proposed, the treaty refused, and a country turns toward normalcy', size=17, color=POWDER)
notes(s, "This lesson closes the Imperialism and World War I unit, and it tells how the war ended twice. The fighting stopped in November 1918, but the peace was argued over for two more years, in Paris, in the Senate, and at the ballot box. The title photograph shows the men who wrote that peace. It is the Council of Four at the Paris Peace Conference, photographed by Edward N. Jackson of the United States Army Signal Corps on May 27, 1919. From left to right: David Lloyd George of Britain, Vittorio Orlando of Italy, Georges Clemenceau of France, and President Woodrow Wilson. Wilson had proposed the League of Nations. His own country refused to join it. The lesson follows that refusal step by step, then turns to the strikes, violence, and fear of 1919, and to the quiet voters demanded in 1920.")

# ------------------------------------------------- 2 · LESSON QUESTION
s = slide(NAVY)
kicker(s, 'The question for today')
text(s, 0.9, 1.9, 11.5, 3.4, [[('Why did the United States refuse the League of Nations it had proposed, and what did the country turn toward in 1920?', {})]],
     size=44, color=CREAM, font='Georgia', leading=1.25)
rule(s, 0.92, 5.6)
text(s, 0.92, 5.85, 11.5, 0.9, [[('Unit question: ', {'color': dc.RUST_LT, 'italic': True}),
                                ('Why did the United States seek power overseas, and how did the First World War change the country that fought it?', {'italic': True})]],
     size=17, color=dc.POWDER, font='Georgia', leading=1.2)
notes(s, "Read the lesson question aloud, then the unit question beneath it. The lesson question has two halves, and students must answer both. First, the refusal: the League of Nations was an American proposal, carried to Paris by an American president, and the United States Senate still would not ratify the treaty that created it. Explaining that refusal takes most of the lesson, through the bargaining at Paris, one article of the League Covenant, one Senate reservation, a speaking tour, a stroke, and three votes. Second, the turn: refusal was not drift. In 1920 the country chose something positive in place of the League, a return to ordinary life that Warren G. Harding named normalcy. Hold the unit question in view as well. A country that had sought power overseas for two decades ended the unit by declining the leading seat in the new world organization, and the war had changed the country at home as deeply as any battle had changed it abroad.")

# --------------------------------------------------- 3 · THE LESSON IN ONE SLIDE
s = slide(NAVY)
kicker(s, 'The lesson in one slide')
text(s, 0.9, 1.25, 11.5, 1.0, 'A peace proposed, refused, and replaced', size=42, color=CREAM, font='Georgia')
rule(s, 0.92, 2.32)
rows = [('A', "Wilson's Plan", 'a peace program in fourteen points, January 8, 1918'),
        ('B', 'Paris and the Treaty', 'the League won at Paris, and Germany charged'),
        ('C', 'The Fight in the Senate', 'Article 10 against Reservation 2'),
        ('D', 'The Tour, the Stroke, and the Votes', '8,000 miles, a stroke, and three failed votes'),
        ('E', '1919: Strikes, Violence, and Fear', 'strikes, the Red Summer, and the raids'),
        ('F', '1920: Normalcy', 'Harding, healing, and no League')]
yy = 2.68
for n, t, d in rows:
    text(s, 0.9, yy, 0.6, 0.7, n, size=24, color=RUST_LT, font='Georgia')
    text(s, 1.55, yy + 0.02, 4.6, 0.7, t, size=20, color=CREAM, bold=True)
    text(s, 6.3, yy + 0.06, 6.2, 0.7, d, size=17, color=POWDER)
    yy += 0.76
notes(s, "This map follows the guided notes section by section. Sections A and B build the peace: Wilson writes the program in January 1918, carries it to Paris in 1919, wins the League, and accepts a treaty that charges Germany with the war and bills it for the damage. Sections C and D stage the refusal: the Senate fight over Article 10, the speaking tour, the stroke of October 2, 1919, and the votes of November 19, 1919 and March 19, 1920. Section E widens the lens to the country behind the Senate: more than 3,600 strikes, the Red Summer, and the Palmer raids. Section F lands the turn in the election of 1920. Warn students now that the Senate fight has a chart at the end of the guided notes, the Senate Fight at a Glance, with three positions to keep distinct: Wilson and his supporters, the Lodge reservationists, and the irreconcilables. Confusing the last two is the most common error in this lesson, so name the distinction on day one.")

# ------------------------------------------------- 4 · SECTION A DIVIDER
divider_text('Section A', "Wilson's Plan",
             'A peace without victory, written in January 1918, while the war still ran',
             "Set the date before the ideas, because the date explains the document. Wilson presented the Fourteen Points to Congress on January 8, 1918, ten months before the fighting stopped. This was not a victory speech and not a treaty draft negotiated with allies. It was a public statement of what the United States was fighting for and what kind of peace could justify the fighting. The audience was triple: Congress and the American public at home, the allied governments whose secret wartime bargains the first point quietly rebuked, and the German public, who were being told that a peace on these terms would not crush them. Wilson intended a peace without victory, in the reading's phrase, enforced not by one army but by an association of nations acting together. Section A of the guided notes has four blanks, and every one is tested: the date, the seas, armaments, and the association of the fourteenth point.")

# ------------------------------------------------------ 5 · THE PRINCIPLES
content_text('A program in fourteen points',
             ['Wilson presented the program to Congress on January 8, 1918.',
              'The opening points called for open agreements, reached in public.',
              'They called for freedom of the seas and lower trade barriers.',
              'They called for reduced armaments.',
              'Colonial claims were to be adjusted fairly, with the peoples concerned weighed.'],
             "Take the opening points in the order the reading gives them, because the guided notes test them in that order. The Fourteen Points opened with general principles. First, open agreements reached in public, a direct answer to the secret treaties and private understandings of wartime diplomacy, which the activity quotes in Point I in full. Then freedom of the seas, blank two, and lower trade barriers between nations. Then reduced armaments, blank three: armies and navies cut back so that no state could restart the war on its own. Then a fair adjustment of colonial claims, one that weighed the interests of the peoples concerned alongside the claims of the governments taking territory. Underline that last phrase for students. Even in a program written by a president of an expanding republic, the peoples living in the colonies appear as a party whose interests count. What Paris did with that principle is a section B question, and students should hold Wilson to his own standard when the mandates arrive.",
             kick="A · Wilson's Plan", size=24)

# ------------------------------------------------------ 6 · POINT XIV
content_text('Territory, and a fourteenth point',
             ['German forces were to leave Russia, Belgium, and France.',
              'An independent Poland was to be created.',
              'Point XIV proposed a general association of nations.',
              'The association would guarantee independence and territory, great and small.',
              'Wilson intended a peace without victory, enforced together.'],
             "The later points applied the principles to the map. German forces were to leave Russia, Belgium, and France, restoring the countries the German army had occupied or invaded, and an independent Poland was to be created. Then comes the point the whole lesson turns on, blank four. The fourteenth point proposed a general association of nations to guarantee the independence and territory of all states, great and small. Read the guarantee slowly, because students will meet it again as Article 10 of the League Covenant, as the target of Lodge's Reservation 2, and as the first question of the quick check. The association was not a debating society in Wilson's design. Its members would promise one another protection against aggression, and the promise itself, made in advance and by all together, was supposed to stop a future aggressor before the first shot. Wilson intended a peace without victory, enforced by the association acting together. Whether the Senate would accept an advance promise of that kind is the fight ahead.",
             kick="A · Wilson's Plan", size=24)

# ------------------------------------------------- 7 · SECTION B DIVIDER
divider_photo('big-four-port.jpg', 'Section B', 'Paris and the Treaty',
              ['Four leaders, one table,', 'and a treaty with two arguments inside it'],
              "The photograph is a portrait crop of the title image, and its date and identification travel with it. Edward N. Jackson of the United States Army Signal Corps photographed the Council of Four at Paris on May 27, 1919. The full photograph shows, from left to right, David Lloyd George of Britain, Vittorio Orlando of Italy, Georges Clemenceau of France, and Woodrow Wilson; this crop centers on Clemenceau and Wilson. Wilson carried his program to Paris in person in 1919, an American president negotiating face to face with allied leaders for months. Section B is the story of a bargain with a split result. Wilson won his fourteenth point: the League of Nations entered the treaty. On most other points he compromised or lost, and the treaty that emerged also carried the war guilt clause and reparations, which shaped how Germans, and then the Senate, received the whole document.",
              title_size=44)

# ------------------------------------------------------ 8 · THE BARGAINING
content_text('The bargaining at Paris, 1919',
             ['Wilson negotiated in person with Lloyd George, Clemenceau, and Orlando.',
              'Britain and France wanted Germany weakened, and made to pay.',
              'Wilson won the League Covenant inside the treaty.',
              'Freedom of the seas was dropped.',
              'Colonies went to the victors as mandates to administer.'],
             "Name the four men first, as the guided notes do: Wilson negotiated with David Lloyd George of Britain, Georges Clemenceau of France, blank five, and Vittorio Orlando of Italy. Then state the imbalance at the table honestly. The British and French leaders spoke for countries that had borne the fighting, with losses the United States had not matched, and they wanted Germany weakened and made to pay. Wilson wanted his League and a peace that Germany could live under. The result was a trade. Wilson won his fourteenth point: the Covenant of the League of Nations became the first part of the treaty. On other points he compromised or lost. Freedom of the seas was dropped. Colonial claims were settled by giving former German and Ottoman territories to the victors as mandates to administer, a long way from weighing the interests of the peoples concerned, as section A had promised. Germany lost territory, its colonies, and most of its armed forces. Students should leave this slide able to say what Wilson bought, and what he paid.",
             kick='B · Paris and the Treaty', size=24)

# ------------------------------------------------------ 9 · THE SIGNING
content_photo_s('orpen-port.jpg', 'Signed in the Hall of Mirrors',
              ['The treaty was signed on June 28, 1919, at Versailles.',
               'The League Covenant was the first part of the treaty.',
               'Article 10 bound members to preserve territory and independence.',
               'That preservation was against external aggression.'],
              "The image is a painting, and its date belongs in the teaching. William Orpen, an official British war artist, painted The Signing of Peace in the Hall of Mirrors in 1919; the original hangs with the Imperial War Museums. The treaty was signed in that hall at Versailles on June 28, 1919, blanks seven and eight of the guided notes. Keep students on the document's structure. The Covenant of the League of Nations became the first part of the treaty, so a vote for the treaty was a vote for the League, with no way to take one without the other. Inside the Covenant sat Article 10, blank six, which bound members to preserve one another's territory and independence against external aggression. Everything in section C is an argument about that one article. Wilson treated it as the heart of the treaty, the guarantee that made the League real. Lodge treated the same sentence as a promise Congress had never agreed to make.",
              kick='B · Paris and the Treaty')

# ------------------------------------------------------ 10 · GUILT AND REPARATIONS
content_text('Guilt and reparations',
             ['Article 231 made Germany accept responsibility for the war.',
              'Germans called Article 231 the war guilt clause.',
              'Article 232 required payment for damage to civilians and property.',
              'German resources could not cover the whole loss.',
              'A Reparation Commission would fix the total.'],
             "Two articles carry the treaty's judgment on Germany, and the quick check quotes the first one in full. Article 231, blank nine, stated that Germany accepted responsibility for causing all the loss and damage of the war, which the Allies charged to German aggression. Germans called this the war guilt clause, and the name tells students how the clause was heard in Germany: not as a billing mechanism, but as a national verdict. The clause supplied the legal basis for what followed. Article 232 required Germany to compensate the Allies for damage to civilians and their property, blank ten, the payments this lesson calls reparations, while admitting that German resources could not cover the whole loss. A Reparation Commission would fix the total later, so the treaty Germany signed named no final sum. Hold two facts together for the writing task: the treaty created the League Wilson wanted, and it humiliated the Germany whose cooperation any lasting peace would need. Both facts were in the document the Senate received.",
             kick='B · Paris and the Treaty', size=24)

# ------------------------------------------------- 11 · SECTION C DIVIDER
divider_text('Section C', 'The Fight in the Senate',
             'The treaty needed two thirds of a Senate its author had not courted',
             "Explain the two handicaps Wilson carried into the fight before naming any senator. First, the arithmetic: ratification required a two thirds vote of the Senate, blank eleven, so a determined minority larger than one third could kill the treaty without ever holding a majority. Second, the politics: Wilson had asked voters in 1918 to return a Democratic Congress, and they elected Republican majorities instead. He then took no leading Republican senator to Paris, so the men who would judge the treaty had no share in making it. A note on images belongs here. The lesson documents use no portraits of Lodge or Borah, because verified period portraits could not be secured, and this divider follows that choice with text alone. What the fight lacked in pictures it made up in paper: fourteen written reservations, one of which, Reservation 2, became the ground on which the treaty lived or died.")

# ------------------------------------------------------ 12 · THREE POSITIONS
content_text('Three positions in the Senate',
             ['Wilson and his supporters wanted the treaty as written.',
              'Lodge reservationists would ratify only with reservations.',
              'Irreconcilables, led by Borah of Idaho, opposed any league, in any form.',
              'Lodge of Massachusetts chaired the Foreign Relations Committee.',
              'The committee produced fourteen reservations.'],
             "Build the chart from the guided notes now, the Senate Fight at a Glance, because every later slide assumes it. Senator Henry Cabot Lodge of Massachusetts, the Republican chairman of the Foreign Relations Committee, blank twelve, led the opposition. His followers were the reservationists: willing to ratify, but only with the fourteen reservations Lodge wrote into the committee's conditions. A smaller group stood apart from both camps. The irreconcilables, blank thirteen, led by Senator William E. Borah of Idaho, opposed joining any league in any form, with reservations or without them. Wilson and his supporters held the third position: the treaty as written, with the Covenant intact. Do the coalition arithmetic aloud, because it predicts November. Wilson's bloc plus the irreconcilables could defeat the reserved treaty. The reservationists plus the irreconcilables could defeat the unreserved treaty. Unless one bloc moved, every version lost, and the two thirds rule meant that losing by a little still counted as losing completely.",
             kick='C · The Fight in the Senate', size=23)

# ------------------------------------------------------ 13 · ARTICLE 10 AGAINST RESERVATION 2
content_text('Article 10 against Reservation 2',
             ['Article 10 bound members to act together against aggression.',
              'Reservation 2 imposed no obligation unless Congress provided for it.',
              'Congress would have to provide in each particular case.',
              'Lodge said the reservation protected the power to declare war.',
              'Wilson said it cut the heart out of the treaty.'],
             "This is the lesson's central document pair, and the activity and quick check both quote the two texts side by side. Article 10 bound League members to preserve one another's territory and independence against external aggression. Reservation 2, blank fourteen, declared that the United States assumed no obligation under Article 10 to preserve another country's territory or independence, or to use its armed forces, unless Congress so provided in each particular case, blank fifteen. State both arguments at full strength, as the exit ticket requires. Lodge argued that the reservation protected the power of Congress to declare war: no treaty, he held, could promise American soldiers in advance. Wilson answered that Reservation 2 cut the heart out of the treaty, since Article 10 was the League's promise to act together against aggression, and a promise that waited on a future vote in each crisis was no promise at all. He ordered Democrats to vote no on that version, blank sixteen, and section D follows that order to its result.",
             kick='C · The Fight in the Senate', size=24)

# ------------------------------------------------- 14 · SECTION D DIVIDER
divider_text('Section D', 'The Tour, the Stroke, and the Votes',
             'Wilson takes the treaty to the people, and his health fails in the attempt',
             "With the Senate deadlocked, Wilson chose the one weapon a president holds over senators: public opinion in their home states. In September 1919 he boarded a train to speak for the treaty as written, over the heads of the Senate and directly to the voters. Teach this section as a sequence with no wasted steps. The tour ran some 8,000 miles. The president collapsed after speaking at Pueblo, Colorado. The stroke followed on October 2, 1919. The refusal of the Lodge reservations continued from the sickroom. The votes came on November 19, 1919, and again on March 19, 1920, and each one failed. Students sometimes treat the stroke as a sad footnote to a political story. Resist that reading in class. The stroke removed the one man who might have bargained, at the exact moment when a bargain was the only road left to two thirds, and Wilson's refusal survived his collapse because it traveled by instruction to senators who still took his orders.")

# ------------------------------------------------------ 15 · 8,000 MILES
stat('8,000 MILES', "Wilson's speaking tour for the treaty, September 1919",
     'By train, town after town, for the treaty as written, until Pueblo, Colorado',
     "Give the tour its scale before its ending, because the mileage is the measure of the effort. In September 1919 Wilson traveled some 8,000 miles by train, blank seventeen, speaking for the treaty as written. He was sixty two years old, visibly exhausted, and traveling against medical advice, because he believed the country agreed with him and only the Senate stood in the way. Town after town, the argument stayed the same: the League was the purpose of the war, Article 10 was its heart, and the Lodge reservations would leave the United States inside a League it had promised nothing to. The crowds were large, and the speeches changed no Senate votes that anyone could count. Exhausted, he collapsed after a speech at Pueblo, Colorado, blank eighteen, and the tour ended there, the remaining stops canceled. The train carried him back to Washington, and on October 2, 1919, the collapse became something worse. Students should note the sequence in the guided notes, because the tour, the collapse, and the stroke are three separate facts, tested separately.",
     kick='D · The Tour, the Stroke, and the Votes')

# ------------------------------------------------------ 16 · THE STROKE
content_text('The stroke, and no compromise',
             ['Wilson collapsed after speaking at Pueblo, Colorado.',
              'On October 2, 1919, he suffered a severe stroke.',
              'The stroke left him with partial paralysis, and a sickroom presidency.',
              'Wilson still refused the Lodge reservations.',
              'He ordered Democrats to vote no.'],
             "On October 2, 1919, Wilson suffered a severe stroke, blank nineteen, that left him partially paralyzed. From his sickroom he still refused the Lodge reservations. Both halves of that sentence carry weight in this lesson. The stroke was a medical fact: the president was gravely ill during the decisive weeks of the treaty fight, cut off from the bargaining, visitors, and pressure that a healthy president uses to move senators. The refusal was a political fact: illness did not soften the position. Wilson held that Reservation 2 destroyed the collective guarantee at the center of the League, and he ordered Democrats to vote no on the treaty with the Lodge reservations attached. That order is the hinge of the first November vote. Without it, the reserved treaty might well have reached two thirds in November 1919. With it, Wilson's own party supplied the votes that killed the version of his treaty closest to passing. The exit ticket asks why the treaty failed twice on one day for two different reasons, and this slide holds the first reason.",
             kick='D · The Tour, the Stroke, and the Votes', size=24)

# ------------------------------------------------------ 17 · THREE VOTES
content_text('Three votes, no ratification',
             ['On November 19, 1919, the treaty with reservations failed, 39 to 55.',
              'That same day, the treaty without reservations failed, 38 to 53.',
              'On March 19, 1920, the treaty with reservations won 49 votes to 35.',
              'That was a majority, and still short of two thirds.',
              'There was no ratification and no League, and a separate peace followed in 1921.'],
             "Read the three votes slowly, with the dates, because the reading test and the quick check both use them at this precision. On November 19, 1919, blank twenty, the Senate voted twice. The treaty with the Lodge reservations failed, 39 to 55, as Wilson's Democrats, obeying his order, joined the irreconcilables in voting no. The treaty without reservations failed, 38 to 53, blocked by reservationists and irreconcilables together. Each version was killed by a different majority, which is the first exit ticket question exactly. A last vote on March 19, 1920, gave the treaty with reservations 49 votes to 35, a majority but short of the two thirds ratification requires. That gap, a winning count that still loses, is the fourth reading question and the third quick check question. The consequences followed in order: the United States never ratified the treaty, never joined the League it had proposed, and made a separate peace with Germany in 1921.",
             kick='D · The Tour, the Stroke, and the Votes', size=24)

# ------------------------------------------------- 18 · SECTION E DIVIDER
divider_text('Section E', '1919: Strikes, Violence, and Fear',
             'The war ends abroad, and the country comes apart at home',
             "Widen the lens now, and mark the turn for students. While the treaty fight ran in Washington, the country was turning inward in anger, and section E explains the mood that made the Senate's refusal popular rather than costly. The year 1919 was not a quiet year of homecoming. It brought a strike wave on a scale the country had never seen, a summer of race violence that earned its own name, and a fear of revolution fed by real bombs and answered by federal raids. Each strand has figures attached, and the lesson states them at a careful precision that students should copy: more than 3,600 strikes, some four million workers, 38 dead in Chicago, 23 of them Black, 249 people deported on one ship. These numbers are the evidence base for the last reading question, which asks how 1919 prepared the voters of 1920. Teach the section as the bridge between the treaty fight and the election.")

# ------------------------------------------------------ 19 · 3,600 STRIKES
stat('3,600 STRIKES', 'in 1919 alone, involving some four million workers',
     'A general strike in Seattle, and national strikes in steel and coal',
     "State the figures at the precision the reading states them, because the writing task grades students on using them honestly. The year 1919 brought more than 3,600 strikes, blank twenty one, involving some four million workers. More than, and some: the counts are large, documented, and rounded, and students should keep the qualifiers attached. The named cases show the range. A general strike in Seattle shut down a whole city, the kind of action that convinced many Americans the labor movement had turned revolutionary. National strikes in steel and coal hit the industries the war had just depended on, in the same months that soldiers were coming home to look for work. Employers, newspapers, and much of the public read the strike wave as one movement with one foreign inspiration, and that reading, fair or not, is part of the history. It connected the picket line, in the public mind, to the revolution in Russia and to the bombs of the spring, which is where the next two slides go.",
     kick='E · 1919: Strikes, Violence, and Fear')

# ------------------------------------------------------ 20 · RED SUMMER
content_text('The Red Summer of 1919',
             ['Race violence spread across the country that summer.',
              'In Chicago, a week of rioting began on July 27.',
              'The Chicago rioting left 38 dead, 23 of them Black.',
              'At Elaine, Arkansas, Black sharecroppers had organized a union.',
              'White posses and troops did the killing at Elaine.'],
             "Race violence scarred the Red Summer of 1919, blank twenty two, and the lesson names two places. In Chicago, a week of rioting that began on July 27 left 38 people dead, 23 of them Black. Give both numbers, because the second one carries the pattern: in riot after riot that summer, the dying fell heaviest on the Black communities that white mobs attacked. At Elaine, Arkansas, white posses and troops killed Black sharecroppers who had organized a union. Note what the Elaine sharecroppers were doing when they were attacked: organizing, the same act the steel and coal strikers were punished for attempting, in a country where a Black union met not injunctions but gunfire. Connect the summer back to the unit question. Black soldiers had served in the war the country just fought, and Black families had moved north in the Great Migration of the previous lesson. The Red Summer was, in part, a violent answer to both facts, delivered in the first year of peace.",
             kick='E · 1919: Strikes, Violence, and Fear', size=24)

# ------------------------------------------------------ 21 · THE RAIDS
content_text('Raids against a feared revolution',
             ['Bombs were mailed to officials in spring 1919.',
              'On November 7, 1919, raids struck radical offices in a dozen cities.',
              'In December 1919, 249 people were deported on the Buford.',
              'On January 2, 1920, several thousand people were arrested.',
              'The arrests spread across more than thirty cities.'],
             "Fear of revolution fed the conflicts of 1919, and the fear had real material to work with. The Russian Revolution of 1917 had created a Communist government, American radicals formed Communist parties in 1919, and bombs were mailed to officials that spring, one exploding outside the home of Attorney General A. Mitchell Palmer. Palmer answered with raids, blank twenty three. On November 7, 1919, federal agents raided radical offices in a dozen cities. That December the government deported 249 aliens, including the anarchist Emma Goldman, on the transport Buford. On January 2, 1920, agents arrested several thousand suspected radicals in more than thirty cities, the peak of what the country would soon call the Red Scare. Then teach the turn inside the facts: the raids swept up many with no part in any plot, and public support faded when Palmer's predicted May Day revolution did not come. The fear had overshot, and voters were left tired of emergency itself, which is the mood section F harvests.",
             kick='E · 1919: Strikes, Violence, and Fear', size=24)

# ------------------------------------------------- 22 · SECTION F DIVIDER
divider_photo('harding-port.jpg', 'Section F', '1920: Normalcy',
              ['A front porch promise:', 'healing, not heroics'],
              "The portrait carries its date in the teaching, as the quick check does. Moffett Studio of Chicago photographed Warren G. Harding on June 21, 1920, during his presidential campaign; the print is held by the Library of Congress. Harding campaigned from his front porch in Ohio while the country counted the costs of 1919: the strikes, the riots, the raids, and a treaty fight that had ended with the United States outside the League its president had designed. His promise was deliberately small. Where Wilson had offered a world organization and a moral crusade, Harding offered rest. Section F is short, one election and one word, but it answers the second half of the lesson question outright. What did the country turn toward in 1920? It turned toward ordinary life, toward less reform at home and no League abroad, and it chose that turn by one of the widest margins in American electoral history.",
              title_size=46)

# ------------------------------------------------------ 23 · 404 TO 127
stat('404 TO 127', 'electoral votes, Harding over Cox, November 1920',
     'About 60 percent of the popular vote for the Republican and normalcy',
     "Give the result at the precision the reading gives it. In November 1920, Republican Warren G. Harding defeated Democrat James M. Cox with about 60 percent of the popular vote and 404 electoral votes to 127. About 60 percent: teach students to keep the qualifier, because the lesson uses it and the test repeats it. The size of the win is the argument. Cox ran as the heir of Wilson and the defender of the League, and the country did not merely edge away from that inheritance; it repudiated it by a landslide. Read the result as a verdict on the whole era this unit has covered, not only on one treaty. The voters of 1920 had lived through war mobilization, a flu pandemic, the strike wave, the Red Summer, and the Red Scare in three crowded years. Harding's margin says the country wanted the emergency over, all of it, at home and abroad together. The next slide takes up the word he gave that wanting.",
     kick='F · 1920: Normalcy')

# ------------------------------------------------------ 24 · WHAT NORMALCY MEANT
content_text('What normalcy meant',
             ['In May 1920, Harding promised not heroics, but healing.',
              'He promised not nostrums, but normalcy.',
              'Normalcy meant ordinary life again after war.',
              'It meant less reform at home, and no League abroad.',
              'The United States made a separate peace with Germany in 1921.'],
             "Harding had supplied the word himself in May 1920, promising that the country needed not heroics, but healing; not nostrums, but normalcy. The reading quotes only those clauses, and the full passage waits on Card 5 of the writing task, where students can weigh his words directly. Normalcy meant ordinary life again: less reform at home and no League abroad. Unpack the pairing, because it closes the unit. At home, the Progressive era's appetite for reform, already strained by war, gave way to a decade of quieter government. Abroad, the refusal of 1919 became the settlement of the 1920s: the United States never ratified the Treaty of Versailles, never joined the League of Nations, and made its separate peace with Germany in 1921. Return to the lesson question for the close. The country refused the League for reasons students can now rank, Senate arithmetic, Article 10, a stroke, and exhaustion among them, and in 1920 it turned, deliberately and by landslide, toward normalcy.",
             kick='F · 1920: Normalcy', size=24)

# ------------------------------------------------------ 25 · VOCAB A
vocab('The program and its treaty',
      [('Fourteen Points', "President Woodrow Wilson's program for a just peace, presented to Congress on January 8, 1918, in fourteen numbered principles that ended with a general association of nations"),
       ('League of Nations', 'the general association of nations created by the Treaty of Versailles in 1919, whose members promised to preserve peace and protect one another against external aggression'),
       ('Treaty of Versailles', 'the treaty signed on June 28, 1919, between Germany and the Allied and Associated Powers, which created the League of Nations and imposed territorial losses, disarmament, and reparations on Germany')],
      "These definitions match the guided notes word for word, and students should copy them exactly, because the unit test draws on them. Fourteen Points: President Woodrow Wilson's program for a just peace, presented to Congress on January 8, 1918, in fourteen numbered principles that ended with a general association of nations. League of Nations: the general association of nations created by the Treaty of Versailles in 1919, whose members promised to preserve peace and protect one another against external aggression. Treaty of Versailles: the treaty signed on June 28, 1919, between Germany and the Allied and Associated Powers, which created the League of Nations and imposed territorial losses, disarmament, and reparations on Germany. Watch the chain the three definitions build: a program proposes an association, a treaty creates it, and the treaty's other terms, the losses and reparations, travel with it into the Senate.")

# ------------------------------------------------------ 26 · VOCAB B
vocab('The bill, and the conditions',
      [('reparations', 'payments imposed on a defeated nation for the loss and damage its aggression caused during a war'),
       ('Lodge reservations', 'the fourteen conditions Senator Henry Cabot Lodge and the Senate Foreign Relations Committee attached to ratification of the Treaty of Versailles, chiefly reserving to Congress the decision on any United States obligation under Article 10')],
      "Two more terms, again matching the guided notes exactly, and these two carry sections B and C. Reparations: payments imposed on a defeated nation for the loss and damage its aggression caused during a war. Students should connect the definition back to its treaty machinery: Article 231 assigned the responsibility, Article 232 required the compensation, and a Reparation Commission was left to fix the total. Lodge reservations: the fourteen conditions Senator Henry Cabot Lodge and the Senate Foreign Relations Committee attached to ratification of the Treaty of Versailles, chiefly reserving to Congress the decision on any United States obligation under Article 10. The last clause is the one to underline in class. Fourteen reservations existed, and students can name several from the activity, but the definition itself singles out the Article 10 reservation, Reservation 2, as the chief one, because that reservation was the ground of the whole fight: who decides, Congress or the Covenant, when American forces might be called on.")

# ------------------------------------------------------ 27 · VOCAB C
vocab('The fear, and the answer to it',
      [('Red Scare', 'the fear in 1919 and 1920 that Communists and other radicals were plotting revolution in the United States, and the government campaign against suspected radicals that the fear produced'),
       ('normalcy', "Warren G. Harding's word in the 1920 campaign for a return to ordinary life after war, with less government activism at home and less involvement abroad")],
      "The last two terms name the turn inward, and both definitions do double work that students should notice. Red Scare: the fear in 1919 and 1920 that Communists and other radicals were plotting revolution in the United States, and the government campaign against suspected radicals that the fear produced. The definition holds a feeling and a policy in one sentence: the fear came first, and the Palmer raids were the campaign the fear produced, so a student who knows only the raids knows half the term. Normalcy: Warren G. Harding's word in the 1920 campaign for a return to ordinary life after war, with less government activism at home and less involvement abroad. That final pairing, at home and abroad, is the lesson in miniature. Less activism at home ends the reform era. Less involvement abroad buries the League. A useful check before the closing work: ask a student to explain the election of 1920 using only these two definitions, in order.")

# ------------------------------------------------------ 28 · TODAY'S WORK
s = slide(NAVY)
kicker(s, 'Now your turn')
text(s, 0.9, 1.35, 11.5, 1.1, 'The League Refused', size=44, color=CREAM, font='Georgia')
rule(s, 0.92, 2.62)
text(s, 0.9, 2.95, 11.3, 1.4,
     ['Return to the lesson question, and rank the causes. A refusal with several causes still has a most important one, and your work today asks you to name it and defend it.'],
     size=23, color=POWDER, leading=1.3)
rows = [('Activity', 'Treaty Fight Hearing: four stations, then draft the compromise'),
        ('Notebook', 'The four subjects and the pattern, kept for review day'),
        ('Quick check', 'Two treaty excerpts, the Harding photograph, five questions'),
        ('Writing', 'The League Refused: rank the causes, answer the counterargument')]
yy = 4.35
for t, d in rows:
    text(s, 0.9, yy, 2.2, 0.6, t, size=19, color=RUST_LT, bold=True)
    text(s, 3.2, yy, 8.9, 0.6, d, size=19, color=CREAM)
    yy += 0.58
text(s, 0.9, 6.85, 11.5, 0.5, 'Next: the unit review and test.',
     size=16, color=POWDER)
notes(s, "Close by handing the lesson to its work, which is built to make students rank causes rather than list them. In the Treaty Fight Hearing, the class staffs a Senate hearing from the fall of 1919: four stations present Wilson's Fourteen Points, the treaty as signed, the Lodge reservations, and the irreconcilable case, and Part 3 asks each committee to draft the compromise it could have offered, then compare that draft with the votes the Senate actually took. The notebook page charts the lesson under four subjects, the peace terms, the League fight, the year 1919, and the election of 1920, and closes with the pattern: the United States proposed the League and then refused to join it. Keep that page, because it returns on review day. The quick check pairs Article 231 and Article 10 with the Harding photograph of June 21, 1920, and asks five questions across the lesson. The writing task, The League Refused, repeats the lesson question as its prompt and requires a ranking, at least three evidence cards, and an answer to the strongest counterargument.")

dc.save(OUT)
