#!/usr/bin/env python3
"""Build the World War II review study guide from the verbatim
vocabulary in build-scripts/unit-spec.md, plus 24 review questions with a
full key and the arguments of the era. Mirrors the Depression and New Deal study guide."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
UNIT = os.path.dirname(HERE)
SPEC = open(os.path.join(HERE, "unit-spec.md")).read()

LESSON_TITLES = {
    1: "The Road to War: Neutrality and Its Critics", 2: "Pearl Harbor and the Arsenal of Democracy",
    3: "Mobilizing the Home Front", 4: "The War in Europe and North Africa",
    5: "The War in the Pacific", 6: "A War for Democracy? Exclusion, Internment, and Service",
    7: "The Holocaust and the War's Crimes", 8: "Victory and the Atomic Reckoning",
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
    (1, "What did the Neutrality Acts forbid, and what memory of the First World War produced them?",
     "They barred arms sales and loans to nations at war and restricted American travel on belligerent ships. They grew out of the First World War's costs and the Nye Committee's charge that bankers and arms makers had pulled the country into that war for profit, and out of Congress's determination that law, not trade, would decide whether the country drifted in again."),
    (1, "State the isolationist case and the interventionist case as each side made them in 1940 and 1941.",
     "Isolationists, led by the America First Committee, argued that the oceans and a strong defense at home kept the country safe, that Britain's war was not America's, and that aid short of war would become war. Interventionists argued that a German victory would leave the United States facing a hostile Europe alone, that Britain's survival was American defense carried on by other hands, and that the Four Freedoms named what the country itself stood for."),
    (1, "Which steps between 1939 and 1941 most changed American policy before any declaration of war?",
     "Cash-and-carry in 1939 reopened arms sales to the side that could pay and carry, which in practice meant Britain and France. The destroyers for bases deal and the first peacetime draft followed in 1940. Lend-Lease in March 1941 made the United States the supplier of its chosen side, and by the autumn of 1941 American destroyers were convoying shipping and shooting at German submarines in an undeclared naval war. Any three, with the direction of change stated, earn credit."),
    (2, "What did the attack on Pearl Harbor settle, and what did it leave open?",
     "It settled the question of entry: Congress declared war against Japan with one dissenting vote, and Germany and Italy removed the remaining doubt by declaring war on the United States on December 11. The country entered united, unlike 1917. It left open how a two-ocean war against three enemies would be fought, which enemy came first, and how the arsenal would be built."),
    (2, "Why did the Allies choose Germany first, and who agreed to it?",
     "Germany was the stronger enemy, held the resources of Europe, and was fighting the Soviet Union, whose collapse would free those resources entirely. The American and British staffs had agreed the priority before Pearl Harbor, the Arcadia conference confirmed it after entry, and the Soviet Union's demand for a second front in France assumed the same priority from the other side."),
    (2, "Describe the cost of the war's first six months after Pearl Harbor.",
     "Japan took the Philippines, Guam, Wake Island, Hong Kong, Malaya, Singapore, and the Dutch East Indies. American and Filipino forces on Bataan surrendered in April 1942 and Corregidor in May. The Doolittle Raid of April 18, 1942 answered in morale rather than damage. The honest summary is that the arsenal of December 1941 existed as orders and appropriations, not yet as ships, planes, and trained divisions."),
    (3, "How did the United States convert its economy to war production, and what machinery ran the conversion?",
     "Automobile plants stopped making cars and turned to tanks, trucks, and aircraft engines; shipyards built cargo ships by welded sections in weeks. The War Production Board allocated steel, rubber, and machine tools and set the order of production. The Office of Price Administration held price ceilings and ran rationing. The Treasury sold war bonds and the income tax became a mass tax. Output roughly doubled across the war, and aircraft production alone approached 300,000 planes."),
    (3, "Who did the war's industrial work, and how did the workforce change?",
     "About six million women entered paid work, many in shipyards and aircraft plants, recruited under images such as Rosie the Riveter. Black workers, Mexican American workers, and Native American workers migrated in large numbers to war industry cities in a second Great Migration. Older workers returned and teenagers left school for jobs. Unemployment, the Depression's defining figure, fell to about one percent."),
    (3, "How was the war paid for, and what did civilians give up?",
     "The war was paid for by taxes raised to reach most working families and by war bonds sold in repeated national drives, with the rest borrowed. Civilians gave up new cars, tires, gasoline, sugar, meat, butter, and shoes to rationing, accepted price controls, and lived with crowded housing in the boomtowns. Private building and consumer production largely stopped for the duration."),
    (4, "Why did the western Allies land in North Africa in 1942 rather than in France?",
     "American forces were not yet built, trained, or shipped in the numbers a cross Channel invasion required, and the landing craft did not exist. North Africa put American troops into the ground war against Germany in 1942, cleared the Mediterranean route, and set up the invasion of Sicily and Italy. The Soviet Union, carrying the land war in the east, pressed for France the whole time, which is why the argument belongs in the lesson."),
    (4, "What did the strategic bombing campaign aim to do, and what did it cost?",
     "It aimed to break Germany's capacity and will to make war by destroying industry, oil, and transportation from the air. The cost ran both ways: American daylight crews took losses that at Schweinfurt in 1943 could not be sustained until long range fighters arrived, and German cities and their civilians bore the campaign on the ground, at Hamburg, Dresden, and across the Ruhr. Bombing cut German production and drew the German air force up to be destroyed, and German war production still rose into 1944, which is why historians argue its weight."),
    (4, "Trace the road from D-Day to VE Day, placing the Battle of the Bulge correctly.",
     "Allied forces landed in Normandy on June 6, 1944 and broke out in July, liberated Paris in August, and stalled at the German border in the autumn. Germany's last offensive in the west struck through the Ardennes in December 1944, the Bulge, and was beaten back by February 1945. The Rhine was crossed in March, American and Soviet forces met at the Elbe on April 25, Hitler killed himself on April 30, and Germany surrendered unconditionally, marked as VE Day on May 8, 1945."),
    (5, "Why was the Battle of Midway the turn of the Pacific war?",
     "American code breaking let the Pacific Fleet ambush the Japanese carrier force in June 1942. American carrier aircraft sank four Japanese fleet carriers and killed aircrews Japan could not replace at the same quality. Japan kept fighting for three more years, but after Midway it defended an empire it had already reached the edge of, and the initiative in the Pacific passed to the United States."),
    (5, "How did island hopping work, and what problem did it solve?",
     "The problem was distance: thousands of miles of ocean with Japanese garrisons on the islands between Hawaii and Japan. The answer was to seize selected islands for airfields and anchorages and to bypass strong garrisons such as Rabaul and Truk, cutting them off by sea and air to wither without garrisons of their own to feed. Each captured island put American aircraft in range of the next objective, and the submarine campaign cut the supply lines of everything bypassed."),
    (5, "What did Iwo Jima and Okinawa teach the planners of 1945 about invading Japan?",
     "Iwo Jima cost about 6,800 American dead for eight square miles. Okinawa, April to June 1945, was larger in every measure: about 12,500 American dead, kamikaze attacks in waves against the fleet, Japanese military deaths above 100,000, and civilian deaths on a scale that read as a rehearsal for the home islands. Planners used both battles to estimate the invasion's cost, and the estimates in the documents of the summer of 1945 are part of the atomic decision's record."),
    (6, "What did Executive Order 8802 do, and what forced it?",
     "It barred racial discrimination in defense industries and federal employment and created the Fair Employment Practices Committee to investigate complaints. It was forced by A. Philip Randolph's threatened march on Washington, set for July 1, 1941, which Roosevelt answered with the order days before the march date. Its enforcement was weak and its life temporary, and it still marks the first federal fair employment machinery since Reconstruction."),
    (6, "State the Double V argument as the Black press made it.",
     "The Pittsburgh Courier's campaign of 1942 argued for two victories in one war: victory over fascism and tyranny abroad, and victory over racism at home. If the Four Freedoms were the war's stated aims, then segregated service, discriminatory hiring, and lynching were not separate from the war but contradictions inside it. The campaign turned war service and war work into claims on citizenship that outlasted the war."),
    (6, "How did the internment of Japanese Americans happen in law, and what did the Supreme Court decide in Korematsu?",
     "Executive Order 9066 of February 19, 1942 authorized military commanders to exclude any persons from prescribed areas. The Western Defense Command applied it to all persons of Japanese ancestry on the West Coast; Congress made violating the exclusion a crime; and about 120,000 people, two thirds of them citizens, were removed to camps without individual hearings. In Korematsu v. United States in December 1944 the Court upheld the exclusion as a military necessity, over dissents that named it the legalization of racism."),
    (7, "Trace the persecution from the Nuremberg Laws to the Final Solution.",
     "The Nuremberg Laws of 1935 stripped Jews of citizenship and marked them in law. Kristallnacht in November 1938 brought open violence and mass arrests. War brought the ghettos of occupied Poland, confinement under starvation conditions. The invasion of the Soviet Union in 1941 brought the Einsatzgruppen, shooting squads that murdered more than a million people. From 1942 the deportation trains ran to killing centers built for murder, Auschwitz-Birkenau and Treblinka among them. By 1945 six million Jews had been murdered, about two thirds of Europe's Jewish population, alongside millions of others."),
    (7, "What did Allied governments know about the murder of Europe's Jews, and what did they do?",
     "Reports of mass murder reached London and Washington from 1941 and 1942, through couriers, escaped witnesses, and Polish government channels, and the Allies publicly condemned the extermination in December 1942. Action lagged the knowledge: refugee doors stayed mostly shut before the war, at Evian and with the St. Louis, and the War Refugee Board was created only in January 1944, after which it helped save tens of thousands, Raoul Wallenberg's work in Budapest among them. The debate over bombing the rail lines and the camps remains an argument historians conduct from the documents."),
    (7, "What answer did the Allies choose at Nuremberg, and what principle did Justice Jackson state for it?",
     "They chose a trial: individual defendants, documentary evidence, stated charges, and a defense, at Nuremberg from November 1945. Jackson's opening stated the principle that the record on which the defendants were judged would be the record by which history judged the tribunal, and that giving conquered men a trial the victors themselves conducted under law was the answer to vengeance. War crimes and crimes against humanity entered international law through that choice."),
    (8, "What was planned at Yalta and argued at Potsdam, and what was left divided?",
     "Yalta in February 1945 set the United Nations conference, sketched Germany's occupation in zones, took Poland's borders and government as promises the west could not enforce, and bought Soviet entry against Japan with concessions in Asia. Potsdam in July 1945 ran the occupation's first business, set reparations and the Oder-Neisse line in practice, and argued over the same Poland. What was left divided was Europe itself: two armies, two systems, and a Germany split at the line where they met."),
    (8, "State the atomic decision as the documents present it: what was argued, and what reasons were given at the time?",
     "The Franck Report of June 1945 argued for a demonstration before military use and warned of an arms race. The interim committee recommended use on a target without warning. The reasons given at the time were the expected cost of invasion read from Iwo Jima and Okinawa, the blockade's slow timetable against a government that had not surrendered after Tokyo's firebombing, and the wish to end the war before more died on every side, including Asian civilians under occupation and prisoners in Japanese hands. The Soviet entry of August 8 and 9 and the second bomb at Nagasaki on August 9 stand in the same record, and the emperor's intervention broke the deadlock in Tokyo."),
    (8, "Describe the country that came home from the war in four changes.",
     "Any four: an economy roughly doubled in output and a generation funded for college and houses by the GI Bill; a population shifted west and to the suburbs by war migration; women pressed to leave war jobs as veterans returned, with the expectation of women working changed anyway; Black veterans and war workers carrying the Double V claims into the postwar freedom struggle; a federal government permanently enlarged in taxation, science, and military reach; and the United States one of two great powers, its cities untouched, holding a monopoly of atomic weapons that would last four years."),
]

ARGUMENTS = [
    ("Neutral in law, belligerent in fact", "The unit's first argument is about what neutrality could mean after 1935. Congress wrote laws to keep trade from choosing a side, and trade chose anyway: cash-and-carry served the side with ships and cash, Lend-Lease named a side outright, and American destroyers were fighting German submarines months before any declaration. The road to war is the record of a policy failing in stages, and each stage was argued in public at the time."),
    ("The arsenal and the state", "The Depression ended when the federal government spent at war scale and directed production directly. That is a fact about the economy before it is an argument, and the unit teaches it as both: the mobilization is the New Deal's unfinished business completed by other means, and it permanently enlarged what Americans expected their government to run, tax, and guarantee."),
    ("Democracy's two fronts", "The war's stated aims were democratic, and the war widened democratic claims at home: war work opened under protest, the Double V campaign turned service into a citizenship claim, and women and migrants redrew the country's map. The same years hold the camps behind barbed wire and a Supreme Court that ratified them. The unit keeps both records in the same lessons, because the claims and the exclusion explain each other."),
    ("Victory and the reckoning", "The alliance won completely, and the victory's instruments and costs are part of the verdict: cities firebombed, a weapon built in secret and used on two cities, 60 to 85 million dead worldwide, and an alliance divided over the peace it had planned together. Judging the war requires the achievement and the reckoning in one account, and the unit's last lesson builds exactly that account from the documents."),
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
    P = []
    P.append("<!DOCTYPE html>")
    P.append('<html lang="en"><head><meta charset="utf-8">')
    P.append("<title>Study Guide: World War II</title>")
    P.append(f"<style>{CSS}</style></head><body>")
    P.append('<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>')
    P.append('<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>')
    P.append("<h1>Study Guide: World War II</h1>")
    P.append('<p class="directions"><strong>Directions:</strong> Complete Part 1 from your guided notes and readings, then answer the Part 2 questions in your own words. Part 3 summarizes the arguments that run through the whole unit. The unit test is built from this guide. Bring questions about anything you cannot answer to the review day.</p>')
    P.append("<p><strong>Unit question:</strong> How did the Second World War transform the United States, and how far did the country live up to the democracy it claimed to defend?</p>")
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
