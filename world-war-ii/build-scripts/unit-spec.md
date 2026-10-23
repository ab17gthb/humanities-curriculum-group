# World War II: shared build spec

Unit essential question: How did the Second World War transform the United States, and how far did the country live up to the democracy it claimed to defend?

Skeleton: ~/workspace/curriculum-planner/world-war-ii-skeleton.md (read it first).
Model unit: ~/workspace/curriculum-planner/depression-new-deal/ — before writing any document type, open the corresponding Depression and New Deal file and mirror its structure, CSS, and conventions exactly. Build PDFs with: python3 ~/workspace/curriculum-planner/templates/build_pdf.py <file.html>
Brandmark (first element in body of every document): <p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>
Deck system: ~/workspace/curriculum-planner/world-war-ii/deck_common.py (copy of the Depression and New Deal system). Teacher notes builder: copy build_notes_doc.py from a Depression and New Deal lesson's slides-build/ and adapt. Decks keep headings.json in slides-build/.
Audited source texts: the TPSP bank files ~/workspace/primary-source/vite-react-main/public/data/wwii.json and (for the four carried records) depression.json hold verbatim audited text with the edition named in each record's sourceNote. Quote from those records, with cuts marked by ellipses and the edition named in the Source line. Never quote from memory where a bank record exists.

## Hard rules (all documents, decks, notes)
- Zero em dashes and zero en dashes anywhere. Zero instances of the construction "that matters" or "that <anything> matters".
- No colon-led paragraph labels in prose, no decorative quotes, no canned transitions, no motivational closers.
- Audience rule: student-facing files are addressed entirely to the student. No product talk, no marketing copy anywhere in the documents. Teacher keys carry pedagogy.
- Readings: 850 to 900 words of body text (count and report the exact count), five questions, teacher key on its own page at the back with each question restated as a bold lead-in.
- Guided notes: Name/Date/Period line, lesson question, unit question frame, Key Terms list with the definitions below VERBATIM, lettered sections A to G matching the reading, numbered fill-in blanks, a closing summary table, an exit ticket (3 questions), teacher key with every blank answered. Definitions must match the list below character for character.
- Activity: locked print design from the Depression and New Deal activity (read one first): 5 stations with Source lines and questions with writing space, a closing ranking or verdict task with paragraph space, teacher key at the back.
- Notebook page: one chart organizer filled from the lesson plus one writing prompt, teacher key with the chart filled in.
- Quick check: short formative, every item tagged to the lesson's blueprint entries in the key.
- Writing task: prompt, evidence bank drawn from the lesson's documents, scaffold, teacher key or rubric.
- Every document: HTML source plus PDF of the same name, page count verified from the PDF.
- Decks: 24 to 29 slides. Slide 1 title, slide 2 the lesson question with the unit essential question as a frame line beneath it, slide 3 the lesson in one slide (lettered sections A to G), then sections in guided-notes order with dividers, content slides with 3 to 5 short fragments, at least two giant stat slides, two vocabulary slides carrying the terms (definitions shown short on screen is fine; the NOTES must carry every term AND its full definition string verbatim), a closing synthesis slide and an exit slide. Speaker notes on EVERY slide: 120 to 190 words each, floor 90, carrying the full teaching for that slide's content in guided-notes order, top to tail. Count notes words per slide and report the range.
- Images for decks and documents: public domain only. Prefer National Archives, Naval History and Heritage Command, Library of Congress, FDR Library, and United States Holocaust Memorial Museum photographs from Wikimedia Commons / the holding archive. Download real files, verify each opens as an image, crop deck images to portrait (about 1046 by 1500) for photo_right and one 16:9 title image, and write img/SOURCES.md per lesson recording title, creator, date, holder, source URL, and public domain basis as shown on the Commons file page. If a download fails, use text and stat slides instead and say so honestly. Never invent a catalog number.
- Sources quoted in documents: verbatim from the named edition, cuts marked with ellipses and disclosed in the Source line. Public domain texts only (speeches, statutes, executive orders, court opinions, government reports). Anything labeled a model or teaching summary must say so on its face.
- Lesson 7 (the Holocaust) is taught with documentary sobriety: verified sources, no sensationalism, photographs chosen for evidentiary value and captioned exactly, no atrocity photograph used as decoration.

## Vocabulary (use verbatim everywhere: guided notes, decks, study materials)

### Lesson 1 (blueprint 1, 2; two terms carried verbatim from earlier units, marked)
- isolationism: a policy of avoiding political commitments and alliances with other countries while keeping a country free to act on its own
- Neutrality Acts: the laws passed by Congress in the 1930s that barred arms sales and loans to nations at war, written to keep the United States out of another world war
- fireside chat: one of President Roosevelt's radio addresses to the nation, delivered in plain conversational language from the White House
- cash-and-carry: the policy adopted in 1939 that let nations at war buy American arms and goods if they paid cash and carried them away in their own ships
- Lend-Lease: the law of March 1941 that let the president lend or lease arms and supplies to any country whose defense he judged vital to the defense of the United States
- Four Freedoms: the four freedoms Roosevelt named in his annual message of January 6, 1941 as the foundations of a just world: freedom of speech, freedom of worship, freedom from want, and freedom from fear
- Atlantic Charter: the joint statement of aims issued by Roosevelt and Churchill in August 1941, pledging self-determination for peoples, freer trade, and freedom of the seas

### Lesson 2 (blueprint 3, 4)
- Pearl Harbor: the United States naval base in Hawaii attacked by Japanese carrier aircraft on December 7, 1941, the attack that brought the United States into the Second World War
- Axis powers: the alliance of Germany, Italy, and Japan that fought the Allied nations in the Second World War
- Allies: the nations allied against the Axis in the Second World War, led by the United States, Great Britain, and the Soviet Union
- Grand Alliance: the formal alliance of the United States, Great Britain, and the Soviet Union against the Axis, joined by many other nations in the Declaration by United Nations of January 1, 1942
- Germany first: the Allied strategy of concentrating the main effort on defeating Germany before Japan, agreed by the American and British staffs and kept through the war
- second front: the Allied invasion of German-held western Europe that the Soviet Union demanded from 1942 onward to draw German strength away from the Eastern Front
- theater: a large geographic area of military operations, such as the European theater or the Pacific theater

### Lesson 3 (blueprint 5, 6)
- mobilization: the process of preparing a nation's armed forces, industry, and economy for war
- Selective Training and Service Act: the law of 1940 that created the first peacetime draft in American history, requiring men of set ages to register for military service as called
- War Production Board: the federal agency created in 1942 to direct the conversion of industry to war production and to allocate steel, rubber, and other scarce materials
- war bonds: government bonds sold to the public to raise money for the war, repaid with interest
- rationing: a system limiting how much of a scarce good each person may buy, enforced with coupons or ration stamps
- Office of Price Administration: the federal agency that set price ceilings and ran the rationing system during the war
- Rosie the Riveter: the popular name and image for the American women who took factory and shipyard jobs during the war, used in songs and posters to recruit women to war work

### Lesson 4 (blueprint 7, 8)
- amphibious landing: an attack from the sea onto a defended shore by forces carried in ships and landing craft
- Eastern Front: the battlefront between Germany and the Soviet Union after June 1941, where the largest land fighting of the war took place
- Stalingrad: the battle of August 1942 to February 1943 in which the Soviet army surrounded and destroyed a German army, the turning point of the war on the Eastern Front
- strategic bombing: the use of heavy bombers against an enemy's industry, transportation, and cities, aiming to break its capacity and will to make war
- D-Day: June 6, 1944, the day Allied forces landed in Normandy, France, in the largest seaborne invasion in history
- Battle of the Bulge: the last major German offensive in the west, launched through the Ardennes in December 1944 and beaten back by February 1945
- VE Day: May 8, 1945, the day victory in Europe was announced after Germany's unconditional surrender

### Lesson 5 (blueprint 9, 10)
- Guadalcanal: the Solomon Islands campaign of August 1942 to February 1943, the first major Allied offensive of the Pacific war, fought on land, at sea, and in the air around one island and its airfield
- Battle of Midway: the naval battle of June 1942 in which American carrier aircraft sank four Japanese carriers and ended Japan's ability to take the offensive in the Pacific
- island hopping: the Allied Pacific strategy of seizing selected islands for airfields while bypassing strong Japanese garrisons and cutting them off from supply
- naval blockade: the use of warships, submarines, and aircraft to cut off an enemy's sea trade and supplies
- firebombing: the bombing of cities with incendiary weapons designed to start mass fires
- kamikaze: a Japanese pilot who made a deliberate crash attack on an enemy ship; also the attack itself
- unconditional surrender: the demand that an enemy give up without negotiated conditions, announced as Allied policy for Germany and Japan

### Lesson 6 (blueprint 11, 12)
- Executive Order 8802: President Roosevelt's order of June 1941 barring racial discrimination in defense industries and federal employment, issued under the threat of a protest march on Washington
- Fair Employment Practices Committee: the federal committee created in 1941 to investigate complaints of job discrimination in war industries
- Double V campaign: the campaign led by Black newspapers from 1942 for victory over fascism abroad and victory over racism at home
- Executive Order 9066: President Roosevelt's order of February 19, 1942 authorizing the military to exclude people from areas of the West Coast, the order under which Japanese Americans were removed from their homes
- internment: the forced confinement of a group of people; in this unit, the removal of about 120,000 people of Japanese ancestry, two thirds of them American citizens, to guarded camps for much of the war
- Korematsu v. United States: the 1944 Supreme Court decision that upheld the exclusion of Japanese Americans from the West Coast as a military necessity
- 442nd Regimental Combat Team: the segregated Japanese American army unit that fought in Europe and became one of the most decorated units of its size and length of service in American history

### Lesson 7 (blueprint 13, 14)
- antisemitism: prejudice against, hatred of, or discrimination against Jews as a religious or ethnic group
- Nuremberg Laws: the German laws of 1935 that stripped Jews of citizenship and forbade marriage between Jews and non-Jewish Germans
- Holocaust: the state-sponsored persecution and murder of six million European Jews by Nazi Germany and its collaborators, together with the murder of millions of others, including Roma, people with disabilities, and Soviet prisoners of war
- ghetto: a section of a city where Jews were forced to live in crowded and starved conditions under German occupation
- Final Solution: the Nazi program to murder every Jew in Europe, carried out by shooting units, deportations, and killing centers from 1941 to 1945
- death camp: one of the camps built by Nazi Germany in occupied Poland where Jews and others were murdered, most in gas chambers on arrival
- war crimes: violations of the laws of war, such as the murder of prisoners and civilians, for which individuals were tried after the war

### Lesson 8 (blueprint 15)
- Yalta Conference: the meeting of Roosevelt, Churchill, and Stalin in February 1945 that planned the postwar settlement, including the United Nations and Soviet entry into the war against Japan
- Potsdam Conference: the meeting of Truman, Churchill, and Stalin in July 1945 in occupied Germany, where the leaders set occupation policy and argued over Europe's future
- Potsdam Declaration: the Allied ultimatum of July 26, 1945 demanding Japan's unconditional surrender and warning of prompt and utter destruction if Japan refused
- Manhattan Project: the secret American program that built the first atomic bombs, employing more than 100,000 people at sites across the country
- atomic bomb: a bomb whose explosive power comes from splitting atoms, releasing energy on a scale no ordinary explosive can match
- demobilization: the process of bringing armed forces back to civilian life and reducing a wartime military to peacetime size
- GI Bill: the Servicemen's Readjustment Act of 1944, which gave veterans unemployment pay, tuition for college and training, and government-backed home and business loans

## Per-lesson file set (folder world-war-ii/lesson-NN/)
lesson-NN-reading.html/.pdf, lesson-NN-guided-notes.html/.pdf, lesson-NN-activity.html/.pdf, lesson-NN-notebook.html/.pdf, lesson-NN-quick-check.html/.pdf, lesson-NN-writing.html/.pdf, lesson-NN-slides.pptx, lesson-NN-teacher-notes.html/.pdf, img/SOURCES.md, slides-build/ (build_deck.py, build_notes_doc.py, headings.json, img/)
