#!/usr/bin/env python3
"""Build the World War II unit test (50 points) in the established test
format: matching 15, multiple choice 20, source-based 15, with every
item tagged to the blueprint in the key. Coverage is recomputed from
the tags this script prints."""
import os

UNIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
.q { margin: 10pt 0 0; }
.qa { break-inside: avoid; }
.sp-a { height: 0.8in; }
.sp-b { height: 1.3in; }
.opts { margin: 2pt 0 0 16pt; }
.opts span { display: block; }
table.match { border-collapse: collapse; width: 100%; margin: 4pt 0 10pt; }
table.match td { padding: 3.5pt 6pt; font-size: 11.5pt; vertical-align: top; }
table.match td.n { width: 4%; }
table.match td.t { width: 30%; }
.source { border: 1.5px solid #000; padding: 8pt 11pt; margin: 8pt 0; break-inside: avoid; }
.source .srclabel { font-weight: bold; margin-bottom: 4pt; }
.source img { display: block; max-width: 3.4in; max-height: 3.2in; margin: 2pt auto 4pt; }
.caption { font-size: 9pt; font-style: italic; text-align: center; margin: 0 0 2pt; }
.key { break-before: page; }
.key h2:first-child { margin-top: 0; }
.brandmark { margin: 0 0 4pt; line-height: 0; } .brandmark img { width: 1.35in; }
"""

# (term, blueprint entry, description) descriptions are the spec definitions
MATCH = [
    ("Neutrality Acts", 1, "the laws passed by Congress in the 1930s that barred arms sales and loans to nations at war, written to keep the United States out of another world war"),
    ("Atlantic Charter", 2, "the joint statement of aims issued by Roosevelt and Churchill in August 1941, pledging self-determination for peoples, freer trade, and freedom of the seas"),
    ("Pearl Harbor", 3, "the United States naval base in Hawaii attacked by Japanese carrier aircraft on December 7, 1941, the attack that brought the United States into the Second World War"),
    ("Germany first", 4, "the Allied strategy of concentrating the main effort on defeating Germany before Japan, agreed by the American and British staffs and kept through the war"),
    ("mobilization", 5, "the process of preparing a nation's armed forces, industry, and economy for war"),
    ("rationing", 6, "a system limiting how much of a scarce good each person may buy, enforced with coupons or ration stamps"),
    ("strategic bombing", 7, "the use of heavy bombers against an enemy's industry, transportation, and cities, aiming to break its capacity and will to make war"),
    ("D-Day", 8, "June 6, 1944, the day Allied forces landed in Normandy, France, in the largest seaborne invasion in history"),
    ("Battle of Midway", 9, "the naval battle of June 1942 in which American carrier aircraft sank four Japanese carriers and ended Japan's ability to take the offensive in the Pacific"),
    ("firebombing", 10, "the bombing of cities with incendiary weapons designed to start mass fires"),
    ("Double V campaign", 11, "the campaign led by Black newspapers from 1942 for victory over fascism abroad and victory over racism at home"),
    ("Executive Order 9066", 12, "President Roosevelt's order of February 19, 1942 authorizing the military to exclude people from areas of the West Coast, the order under which Japanese Americans were removed from their homes"),
    ("Final Solution", 13, "the Nazi program to murder every Jew in Europe, carried out by shooting units, deportations, and killing centers from 1941 to 1945"),
    ("war crimes", 14, "violations of the laws of war, such as the murder of prisoners and civilians, for which individuals were tried after the war"),
    ("Manhattan Project", 15, "the secret American program that built the first atomic bombs, employing more than 100,000 people at sites across the country"),
]
# letter order for descriptions (index into MATCH shuffled by hand)
ORDER = [3, 11, 0, 7, 14, 5, 9, 1, 12, 6, 2, 10, 4, 13, 8]

# (question, options[4], correct index, blueprint entry)
MC = [
    ("The Neutrality Acts of 1935 to 1937 were written chiefly to",
     ["prepare American industry for war production", "keep the United States out of another world war by barring arms sales and loans to nations at war",
      "punish Japan for its invasion of China", "fund the British and French war efforts"], 1, 1),
    ("The Lend-Lease law of March 1941 changed American policy by",
     ["declaring war on Germany", "letting the president lend or lease arms to any country whose defense he judged vital to the United States",
      "repealing the peacetime draft", "placing American convoys under British command"], 1, 2),
    ("The Japanese attack of December 7, 1941 fell on",
     ["San Francisco and the Panama Canal", "the Pacific Fleet at Pearl Harbor and American positions across the Pacific",
      "the Philippines only", "British Malaya only"], 1, 3),
    ("The Germany first strategy meant that the Allies would",
     ["fight Japan only after the Soviet Union joined the Pacific war", "concentrate the main effort on defeating Germany while holding against Japan",
      "invade France in the spring of 1942", "leave the Pacific entirely to the Navy"], 1, 4),
    ("The Selective Training and Service Act of 1940 was significant because it",
     ["ended the Depression by itself", "created the first peacetime draft in American history",
      "integrated the armed forces", "gave the president power to set prices"], 1, 5),
    ("The Office of Price Administration ran which pair of home front systems?",
     ["the draft and war bond sales", "price ceilings and rationing",
      "censorship and propaganda", "war housing and shipbuilding"], 1, 6),
    ("Operation Torch, the first major American ground campaign of the European war, landed American and British forces in",
     ["Normandy", "Sicily", "North Africa", "Norway"], 2, 7),
    ("The Battle of the Bulge in December 1944 was",
     ["the first Allied landing in France", "Germany's last major offensive in the west, beaten back by February 1945",
      "the Soviet capture of Berlin", "the heaviest bombing raid of the war"], 1, 8),
    ("The Battle of Midway turned the Pacific war chiefly because",
     ["American submarines cut Japan's oil supply", "American carrier aircraft sank four Japanese carriers, ending Japan's ability to take the offensive",
      "Marines captured the first Japanese airfield", "the Soviet Union entered the war against Japan"], 1, 9),
    ("Iwo Jima and Okinawa mattered to the summer of 1945 chiefly because",
     ["they ended the submarine blockade", "their cost in American and civilian dead was read as a preview of invading Japan itself",
      "they brought the Soviet Union into the Pacific war", "they captured Japan's remaining aircraft carriers"], 1, 10),
    ("Executive Order 8802, issued in June 1941, barred",
     ["Japanese Americans from the West Coast", "racial discrimination in defense industries and federal employment",
      "women from factory work", "strikes in war plants"], 1, 11),
    ("In Korematsu v. United States (1944), the Supreme Court",
     ["ordered the camps closed at once", "struck down Executive Order 9066",
      "upheld the exclusion of Japanese Americans from the West Coast as a military necessity", "ruled that citizens could never be detained"], 2, 12),
    ("The Nuremberg Laws of 1935",
     ["created the ghettos of occupied Poland", "stripped Jews of German citizenship and forbade marriage between Jews and non-Jewish Germans",
      "ordered the building of the death camps", "set the quotas for Jewish refugees to the United States"], 1, 13),
    ("Eisenhower's order after visiting the Ohrdruf camp in April 1945 required that the camp be",
     ["kept secret until after the trials", "documented and witnessed by soldiers, journalists, and officials",
      "burned to prevent disease", "handed to the Soviet army"], 1, 14),
    ("The Potsdam Declaration of July 26, 1945 demanded",
     ["a negotiated peace preserving the Japanese government unchanged", "Japan's unconditional surrender, warning of prompt and utter destruction if Japan refused",
      "the division of Japan between the United States and the Soviet Union", "an immediate Allied invasion of the home islands"], 1, 15),
    ("The isolationist case against aiding Britain, made by the America First Committee, argued that",
     ["Britain had already lost and aid was wasted", "the United States should build its own defenses at home and stay out of Europe's war",
      "Germany posed no threat to any country", "the president had no power over foreign trade"], 1, 1),
    ("Which figure best states the scale of American mobilization by 1945?",
     ["about 2 million in uniform and unemployment near 10 percent", "more than 12 million in uniform and unemployment near one percent",
      "about 6 million in uniform and aircraft production of 30,000 across the war", "more than 12 million in uniform and no rationing of any good"], 1, 5),
    ("Island hopping, the Allied Pacific strategy, worked by",
     ["capturing every Japanese-held island in order", "seizing selected islands for airfields while bypassing strong garrisons and cutting them off from supply",
      "landing directly on Japan from Hawaii", "relying on submarines alone to starve Japan"], 1, 9),
    ("The Double V campaign of the Black press demanded victory over",
     ["Germany and Japan", "fascism abroad and racism at home",
      "the draft and rationing", "the Soviet Union and Germany"], 1, 11),
    ("The clearest measure of the war's worldwide cost is that",
     ["American deaths were the largest of any nation", "worldwide deaths are estimated between 60 and 85 million, with the Soviet Union's share the largest",
      "no European city survived undamaged", "Japan and Germany lost equal numbers"], 1, 15),
]

def main():
    P = []
    P.append("<!DOCTYPE html>")
    P.append('<html lang="en"><head><meta charset="utf-8">')
    P.append("<title>Unit Test: World War II</title>")
    P.append(f"<style>{CSS}</style></head><body>")
    P.append('<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>')
    P.append('<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>')
    P.append("<h1>Unit Test: World War II</h1>")
    P.append('<p class="directions"><strong>Total: 50 points.</strong> Part 1 is worth 15 points, Part 2 is worth 20 points, Part 3 is worth 15 points. Write answers on this test. For Part 3, answer in complete sentences and cite the sources by letter.</p>')

    P.append("<h2>Part 1: Matching (15 points)</h2>")
    P.append("<p>Match each term to its description. Each description is used once.</p>")
    P.append('<table class="match">')
    letters = "ABCDEFGHIJKLMNO"
    desc_by_pos = {}
    for pos, idx in enumerate(ORDER):
        desc_by_pos[idx] = letters[pos]
    rows_desc = [MATCH[idx][2] for idx in ORDER]
    for i, (term, bp, _) in enumerate(MATCH):
        P.append(f'<tr><td class="n">___</td><td class="t">{i + 1}. {term}</td><td>{letters[i]}. {rows_desc[i]}</td></tr>')
    P.append("</table>")

    P.append("<h2>Part 2: Multiple Choice (20 points)</h2>")
    P.append("<p>Choose the best answer for each question.</p>")
    for i, (q, opts, _, _) in enumerate(MC, 1):
        P.append(f'<div class="qa"><p class="q"><strong>{i}.</strong> {q}</p><p class="opts">')
        for j, o in enumerate(opts):
            P.append(f"<span>{letters[j]}. {o}</span>")
        P.append("</p></div>")

    P.append("<h2>Part 3: Sources (15 points)</h2>")
    P.append("<p>Answer each question in complete sentences, citing the sources by letter.</p>")
    P.append('<div class="source"><p class="srclabel">Source A</p>')
    P.append("<p>President Franklin D. Roosevelt, address to Congress asking for a declaration of war against Japan, December 8, 1941. From the transcript held by the Franklin D. Roosevelt Presidential Library and Museum. Cuts are marked with ellipses.</p>")
    P.append("<p>&ldquo;The United States was at peace with that Nation and, at the solicitation of Japan, was still in conversation with its Government and its Emperor looking toward the maintenance of peace in the Pacific. . . . It will be recorded that the distance of Hawaii from Japan makes it obvious that the attack was deliberately planned many days or even weeks ago. During the intervening time, the Japanese Government has deliberately sought to deceive the United States by false statements and expressions of hope for continued peace. . . . I ask that the Congress declare that since the unprovoked and dastardly attack by Japan on Sunday, December 7, 1941, a state of war has existed between the United States and the Japanese Empire.&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>A1. (2 points)</strong> According to Roosevelt, what two facts show that the attack was planned in advance and that the peace talks were used as cover?</p><div class="sp-a"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>A2. (3 points)</strong> Roosevelt delivered this address one day after the attack. Using the source and the lesson, explain what the address and the vote that followed settled, and name one question about the war they did not settle.</p><div class="sp-b"></div></div>')
    P.append('<div class="source"><p class="srclabel">Source B</p>')
    P.append("<p>Executive Order 9066, February 19, 1942. From the Federal Register, volume 7, page 1407. A cut is marked with an ellipsis.</p>")
    P.append("<p>&ldquo;I hereby authorize and direct the Secretary of War, and the Military Commanders whom he may from time to time designate, whenever he or any designated Military Commander deems such action necessary or desirable, to prescribe military areas in such places and of such extent as he or the appropriate Military Commander may determine, from which any or all persons may be excluded, and with respect to which, the right of any person to enter, remain in, or leave shall be subject to whatever restrictions the Secretary of War or the appropriate Military Commander may impose in his discretion.&rdquo;</p></div>")
    P.append('<div class="qa"><p class="q"><strong>B1. (2 points)</strong> State in your own words what power this order gives to military commanders, and over whom it can be used.</p><div class="sp-a"></div></div>')
    P.append('<div class="qa"><p class="q"><strong>B2. (3 points)</strong> The order names no ethnic or national group. Explain how it nonetheless became the legal basis for removing one group from the West Coast, and state two facts about the people removed that the order itself does not mention.</p><div class="sp-b"></div></div>')
    P.append('<div class="source"><p class="srclabel">Source C</p>')
    P.append('<img src="into-the-jaws-of-death-1944.jpg" alt="Into the Jaws of Death photograph">')
    P.append('<p class="caption">Robert F. Sargent, United States Coast Guard, photograph of troops of the First Division disembarking from a Coast Guard landing craft at Utah Beach, Normandy, the morning of June 6, 1944. National Archives.</p>')
    P.append("<p>Sargent, a chief photographer's mate, took this picture from the landing craft as the troops went down the ramp into the water. The Coast Guard and the Army Signal Corps photographed the invasion throughout the day, and newspapers printed their pictures across the country within days.</p></div>")
    P.append('<div class="qa"><p class="q"><strong>C1. (2 points)</strong> What is happening in the photograph, and where and when was it taken? Answer from the caption and the image.</p><div class="sp-a"></div></div>')
    P.append("<div class=\"qa\"><p class=\"q\"><strong>C2. (3 points)</strong> This photograph was made by a serviceman on duty and printed in newspapers within days. What does its existence show about how the government documented and presented the war to the home front, and what does the photograph not show about June 6, 1944?</p><div class=\"sp-b\"></div></div>")

    # ---------------- KEY ----------------
    from collections import Counter
    counts = Counter()
    P.append('<div class="key"><h2>Teacher Answer Key</h2>')
    P.append("<h3>Part 1: Matching</h3>")
    for i, (term, bp, _) in enumerate(MATCH):
        counts[bp] += 1
        P.append(f"<p><strong>{i + 1}. {term}: {desc_by_pos[i]}</strong> (Blueprint {bp})</p>")
    P.append("<h3>Part 2: Multiple Choice</h3>")
    for i, (q, opts, correct, bp) in enumerate(MC, 1):
        counts[bp] += 1
        P.append(f"<p><strong>{i}. {letters[correct]}</strong> (Blueprint {bp})</p>")
    P.append("<h3>Part 3: Sources</h3>")
    key3 = [
        ("A1", 3, "The distance of Hawaii from Japan makes it obvious the attack was planned many days or weeks in advance, since the carriers had to sail that distance in secret. During the same period the Japanese government continued peace conversations and delivered expressions of hope for peace, which Roosevelt names as deliberate deception. Either fact earns a point; both together earn full credit."),
        ("A2", 3, "The address and the nearly unanimous votes (one dissent in the House) settled that the United States was at war and ended the neutrality debate of 1935 to 1941 in a day; the country entered the war formally and united, unlike 1917. Not settled, any one of: how to fight a two-ocean war against three enemies, whether Germany or Japan came first (settled by agreement and by Germany's own declaration on December 11), or how the arsenal would be built. Answers must tie the settlement to the source's request for a declaration."),
        ("B1", 12, "The order lets the Secretary of War and designated military commanders create military areas of any size they choose and exclude any or all persons from them, controlling who may enter, remain in, or leave, at the commander's discretion. The power runs over any persons, citizens included; the order sets no limit by citizenship or by charge."),
        ("B2", 12, "The Western Defense Command used the order to issue exclusion orders directed in practice at all persons of Japanese ancestry on the West Coast, so a facially general power was applied to one ancestry group. Facts the order does not mention, any two: about 120,000 people were removed; two thirds of them were American citizens; they were sent to guarded camps in the interior for much of the war; families lost homes, businesses, and property sold in haste; no individual hearings or charges were held."),
        ("C1", 7, "American troops of the First Division are disembarking from a Coast Guard landing craft, down its ramp into the sea, at Utah Beach, Normandy, on the morning of June 6, 1944, D-Day. The caption supplies the place and date; the image shows the ramp, the water, and the troops in full kit moving toward the beach."),
        ("C2", 7, "The government put its own photographers in the first waves and released their pictures to newspapers within days, so documenting the invasion was official business and the home front saw the war largely through government images. The photograph does not show the cost or the scale of the day: the casualties on the beaches, the four other landing beaches, the airborne drops inland, or the thousands of ships behind the one craft in the frame. Full credit requires one point of each kind."),
    ]
    for label, bp, ans in key3:
        counts[bp] += 1
        P.append(f"<p><strong>{label}.</strong> {ans} (Blueprint {bp})</p>")
    P.append("</div></body></html>")
    out = os.path.join(UNIT, "unit-test", "unit-test.html")
    open(out, "w").write("\n".join(P))
    print("coverage from printed tags:", dict(sorted(counts.items())))
    print("min per entry:", min(counts.values()), "entries covered:", len(counts))

if __name__ == "__main__":
    main()
