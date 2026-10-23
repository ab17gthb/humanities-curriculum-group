# The Cold War: shared build spec

Unit essential question: How did the struggle between the United States and the Soviet Union reshape the world and American life, and why did it end the way it did?

Skeleton: ~/workspace/curriculum-planner/cold-war-skeleton.md (read it first).
Model unit: ~/workspace/curriculum-planner/world-war-ii/ and ~/workspace/curriculum-planner/depression-new-deal/ — before writing any document type, open the corresponding World War II file and mirror its structure, CSS, and conventions exactly. Build PDFs with: python3 ~/workspace/curriculum-planner/templates/build_pdf.py <file.html>
Brandmark (first element in body of every document): <p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>
Deck system: ~/workspace/curriculum-planner/cold-war/deck_common.py (copy of the World War II system). Teacher notes builder: copy build_notes_doc.py from a World War II lesson's slides-build/ and adapt. Decks keep headings.json in slides-build/.
Audited source texts: the TPSP bank file ~/workspace/primary-source/vite-react-main/public/data/cold-war.json holds verbatim audited text with the edition named in each record's sourceNote. Quote from those records, with cuts marked by ellipses and the edition named in the Source line. Never quote from memory where a bank record exists.

## Hard rules (all documents, decks, notes)
- Zero em dashes and zero en dashes anywhere. Zero instances of the construction "that matters" or "that <anything> matters".
- No colon-led paragraph labels in prose, no decorative quotes, no canned transitions, no motivational closers.
- Audience rule: student-facing files are addressed entirely to the student. No product talk, no marketing copy anywhere in the documents. Teacher keys carry pedagogy.
- Readings: 850 to 900 words of body text (count and report the exact count), five questions, teacher key on its own page at the back with each question restated as a bold lead-in.
- Guided notes: Name/Date/Period line, lesson question, unit question frame, Key Terms list with the definitions below VERBATIM, lettered sections A to G matching the reading, numbered fill-in blanks, a closing summary table, an exit ticket (3 questions), teacher key with every blank answered. Definitions must match the list below character for character.
- Activity: locked print design from the World War II activity (read one first): 5 stations with Source lines and questions with writing space, a closing ranking or verdict task with paragraph space, teacher key at the back.
- Notebook page: one chart organizer filled from the lesson plus one writing prompt, teacher key with the chart filled in.
- Quick check: short formative, every item tagged to the lesson's blueprint entries in the key.
- Writing task: prompt, evidence bank drawn from the lesson's documents, scaffold, teacher key or rubric.
- Every document: HTML source plus PDF of the same name, page count verified from the PDF. Student documents end at deliberate page boundaries (full page or clean page and a half); a page that dies a quarter of the way down with dead space after it is a defect to fix by adjusting space heights before delivery.
- Decks: 24 to 29 slides. Slide 1 title, slide 2 the lesson question with the unit essential question as a frame line beneath it, slide 3 the lesson in one slide (lettered sections A to G), then sections in guided-notes order with dividers, content slides with 3 to 5 short fragments, at least two giant stat slides, two vocabulary slides carrying the terms (definitions shown short on screen is fine; the NOTES must carry every term AND its full definition string verbatim, including the strict joined "term: definition" form), a closing synthesis slide and an exit slide. Speaker notes on EVERY slide: 120 to 190 words each, floor 90, carrying the full teaching for that slide's content in guided-notes order, top to tail. Count notes words per slide and report the range.
- Images for decks and documents: public domain only. Prefer National Archives, Library of Congress, presidential libraries (Truman, Eisenhower, Kennedy, Johnson, Nixon, Ford, Carter, Reagan), State Department, and Department of Defense photographs from Wikimedia Commons / the holding archive. Download real files, verify each opens as an image, crop deck images to portrait (about 1046 by 1500) for photo_right and one 16:9 title image, and write img/SOURCES.md per lesson recording title, creator, date, holder, source URL, and public domain basis as shown on the Commons file page. If a download fails, use text and stat slides instead and say so honestly. Never invent a catalog number.
- Sources quoted in documents: verbatim from the named edition, cuts marked with ellipses and disclosed in the Source line. Public domain texts only (speeches, statutes, executive orders, government reports and cables). Copyrighted material (magazine covers, song lyrics, editorial cartoons under copyright, later memoirs) stays within 90 quoted words or is not quoted at all. Anything labeled a model or teaching summary must say so on its face.

## Vocabulary (use verbatim everywhere: guided notes, decks, study materials)

### Lesson 1 (blueprint 1, 2)
- superpower: a nation with power and influence far beyond that of other states, able to project military and political strength across the world
- Iron Curtain: the boundary Winston Churchill named in 1946 between the Soviet-dominated states of Eastern Europe and the free states of the West, and the division of Europe it described
- containment: the American strategy of blocking the further expansion of Soviet power and communism, first argued by George Kennan and adopted as the guiding policy of the early Cold War
- Truman Doctrine: the policy President Truman declared in 1947, that the United States would support free peoples resisting attempted subjugation by armed minorities or outside pressures
- Marshall Plan: the American program of 1948 to 1952 that gave about thirteen billion dollars in aid to rebuild the economies of Western Europe after the Second World War
- Berlin Airlift: the American and British air supply of West Berlin in 1948 and 1949, flown around the Soviet blockade of the city's land routes
- NATO: the North Atlantic Treaty Organization, the alliance formed in 1949 in which the United States, Canada, and Western European nations pledged to treat an attack on one member as an attack on all

### Lesson 2 (blueprint 3, 4)
- NSC-68: the secret American planning paper of 1950 that described the Cold War as a global struggle and called for a large buildup of American military strength
- People's Republic of China: the Communist state Mao Zedong proclaimed in 1949 after his forces won the Chinese civil war, recognized by the Soviet Union and not by the United States
- Korean War: the war of 1950 to 1953 in which the United States and United Nations forces fought North Korea and China to preserve a non-Communist South Korea
- 38th parallel: the line of latitude chosen in 1945 to divide Soviet and American occupation zones in Korea, which became the border between North and South Korea
- limited war: a war fought for limited aims with some weapons and targets deliberately left unused, rather than for the enemy's total defeat
- stalemate: a condition in fighting in which neither side can gain ground or force a decision, however long the fighting continues
- armistice: an agreement to stop fighting; the Korean armistice of 1953 ended the shooting without a peace treaty or a political settlement

### Lesson 3 (blueprint 5, 6)
- Second Red Scare: the fear from the late 1940s through the 1950s that Communists had infiltrated American government and institutions, and the investigations, loyalty tests, and blacklists the fear produced
- House Un-American Activities Committee: the House of Representatives committee that investigated alleged Communist influence in American life, most famously in its hearings on the film industry in 1947
- loyalty oath: a sworn statement of loyalty to the government and denial of Communist membership, required of federal employees and many other workers during the Second Red Scare
- Hollywood Ten: the ten screenwriters and directors who refused to answer the House Un-American Activities Committee's questions in 1947, were cited for contempt of Congress, and went to prison
- blacklist: a list of people barred from employment in an industry because of suspected Communist ties or refusal to cooperate with investigators, circulated in film and broadcasting during the Second Red Scare
- McCarthyism: the practice of making public accusations of Communist disloyalty without firm evidence, named for Senator Joseph McCarthy, who made his charges the center of a national campaign from 1950 to 1954
- Army-McCarthy hearings: the televised Senate hearings of 1954 in which the Army and Senator McCarthy accused each other of improper conduct, watched by millions, after which the Senate censured McCarthy

### Lesson 4 (blueprint 7, 8)
- arms race: the competition between the United States and the Soviet Union to build more and more powerful weapons, each side answering the other's advances
- hydrogen bomb: a thermonuclear weapon far more powerful than the atomic bombs of 1945, first tested by the United States in 1952 and by the Soviet Union in 1953
- massive retaliation: the Eisenhower administration's declared policy of answering Communist aggression with the threat of a full nuclear strike, rather than matching force at the point of attack
- brinkmanship: the practice of pushing a dangerous confrontation to the edge of war in order to force the other side to back down, described by Secretary of State John Foster Dulles
- Warsaw Pact: the military alliance formed in 1955 joining the Soviet Union and the Communist states of Eastern Europe, created in answer to NATO and West Germany's place in it
- covert action: a secret government operation meant to influence events abroad while hiding the sponsor's hand, carried out in the Cold War chiefly by the Central Intelligence Agency
- Sputnik: the first artificial satellite, launched by the Soviet Union in October 1957, whose success shocked the United States and opened the space race

### Lesson 5 (blueprint 9, 10)
- Cuban Revolution: the revolution that brought Fidel Castro to power in Cuba in 1959, overthrowing the government of Fulgencio Batista and turning toward alliance with the Soviet Union
- Bay of Pigs invasion: the failed invasion of Cuba in April 1961 by Cuban exiles trained and supplied by the United States, defeated on the beach within three days
- deterrence: the policy of preventing an enemy attack by holding a threat of retaliation so destructive that the attack would cost more than it could gain
- Cuban Missile Crisis: the confrontation of October 1962 in which the United States discovered Soviet nuclear missiles being installed in Cuba and forced their withdrawal short of war
- naval quarantine: President Kennedy's name for the naval blockade of Cuba in 1962, chosen because a blockade is legally an act of war and quarantine was not
- hotline: the direct communications link between Washington and Moscow established in 1963 so the two leaders could reach each other at once in a crisis
- Limited Test Ban Treaty: the treaty of 1963 in which the United States, the Soviet Union, and Britain banned nuclear weapons tests in the atmosphere, in space, and under water

### Lesson 6 (blueprint 11, 12)
- domino theory: the belief, stated publicly by President Eisenhower in 1954, that if one country fell to communism its neighbors would fall one after another like a row of dominoes
- Viet Cong: the Communist guerrilla forces and political organization in South Vietnam, supplied and directed from North Vietnam, that fought the South Vietnamese government and its American allies
- Gulf of Tonkin Resolution: the resolution Congress passed in August 1964 giving the president authority to take all necessary measures to repel attacks on American forces and prevent further aggression in Southeast Asia
- escalation: the steady enlargement of a military commitment step by step, as the American ground force in Vietnam grew from advisers to more than half a million troops
- Tet Offensive: the coordinated attacks by North Vietnamese and Viet Cong forces across South Vietnam in January 1968, a military defeat for the attackers that shook American confidence in official claims of progress
- Vietnamization: President Nixon's policy of withdrawing American troops while building up South Vietnam's forces to carry the fighting themselves
- draft lottery: the system begun in 1969 that chose the order in which young men were called for the draft by a random drawing of birth dates

### Lesson 7 (blueprint 13, 14)
- détente: the easing of tension between the United States and the Soviet Union pursued in the 1970s, built on arms agreements, trade, and regular summit meetings
- arms control: negotiated limits on the weapons the superpowers could build or deploy, agreed in treaties rather than won in competition
- SALT: the Strategic Arms Limitation Talks between the United States and the Soviet Union, and the agreements they produced in 1972 and 1979 limiting nuclear delivery vehicles
- Helsinki Accords: the 1975 agreement in which Western nations recognized Europe's postwar borders and the Soviet Union and its allies pledged respect for human rights, a pledge dissidents used against their own governments
- Reagan Doctrine: the policy of the 1980s under which the United States aided anti-Communist insurgencies fighting Soviet-backed governments, in Afghanistan, Nicaragua, and elsewhere
- Strategic Defense Initiative: President Reagan's 1983 proposal to build a defense in space against nuclear missiles, called Star Wars by its critics, which promised protection deterrence could not
- Evil Empire: President Reagan's name for the Soviet Union in a speech of March 1983, declaring it the focus of evil in the modern world and rejecting the idea that the two systems were morally equal

### Lesson 8 (blueprint 15)
- glasnost: Mikhail Gorbachev's policy of openness in the Soviet Union from 1985, allowing public discussion, criticism of officials, and a freer press
- perestroika: Gorbachev's program of restructuring the Soviet economy and political system, meant to make a failing system work and ending by loosening the party's control of both
- Solidarity: the Polish labor movement founded in 1980 at the Gdansk shipyard, the first independent union in the Communist bloc, which survived martial law to lead Poland's turn from Communist rule in 1989
- INF Treaty: the treaty of 1987 in which the United States and the Soviet Union agreed to destroy all their land-based missiles with ranges between about 300 and 3,400 miles, the first agreement to eliminate a class of nuclear weapons
- Berlin Wall: the wall the East German government built in 1961 to stop its citizens fleeing to the West, which became the central symbol of the divided Europe, and which crowds breached on November 9, 1989
- German reunification: the joining of East and West Germany into one state in October 1990, ending the division imposed after the Second World War
- dissolution of the Soviet Union: the ending of the Soviet Union in December 1991, when its republics declared independence and the state that had stood since 1922 ceased to exist

## Per-lesson file set (folder cold-war/lesson-NN/)
lesson-NN-reading.html/.pdf, lesson-NN-guided-notes.html/.pdf, lesson-NN-activity.html/.pdf, lesson-NN-notebook.html/.pdf, lesson-NN-quick-check.html/.pdf, lesson-NN-writing.html/.pdf, lesson-NN-slides.pptx, lesson-NN-teacher-notes.html/.pdf, img/SOURCES.md, slides-build/ (build_deck.py, build_notes_doc.py, headings.json, img/)
