# The Civil Rights Movement: shared build spec

Unit essential question: How did the civil rights movement change American law and American life, and what did it leave unfinished?

Skeleton: ~/workspace/curriculum-planner/civil-rights-skeleton.md (read it first).
Model units: ~/workspace/curriculum-planner/cold-war/ and ~/workspace/curriculum-planner/world-war-ii/ — before writing any document type, open the corresponding Cold War file and mirror its structure, CSS, and conventions exactly. Build PDFs with: python3 ~/workspace/curriculum-planner/templates/build_pdf.py <file.html>
Brandmark (first element in body of every document): <p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>
Deck system: ~/workspace/curriculum-planner/civil-rights/deck_common.py (copy of the Cold War system). Teacher notes builder: copy build_notes_doc.py from a Cold War lesson's slides-build/ and adapt. Decks keep headings.json in slides-build/.
Audited source texts: the TPSP bank file ~/workspace/primary-source/vite-react-main/public/data/civil-rights.json holds verbatim audited text with the edition named in each record's sourceNote; the Little Rock and Till records and Executive Order 9981 are in ~/workspace/primary-source/vite-react-main/public/data/cold-war.json. Quote from those records, with cuts marked by ellipses and the edition named in the Source line. Never quote from memory where a bank record exists.

## Copyright discipline (binding, this unit above all)
Martin Luther King Jr.'s Letter from Birmingham Jail, King's I Have a Dream address, and Malcolm X's The Ballot or the Bullet are under copyright. Each of the three works may be quoted at NO MORE THAN 90 WORDS IN TOTAL across the entire unit, all documents, decks, notes, review, and test combined. Count every quoted word when you place it, choose the shortest passage that carries the point, and log the exact count in the lesson's img/SOURCES.md or source notes so the manifest can disclose the running totals. Where the famous wording would break the cap, paraphrase and let the document say the words are paraphrased. King's MIA mass meeting speech (bank record) and the Autobiography of Malcolm X excerpt (bank record) are also copyrighted: quote them only at the lengths the bank records carry as short excerpts and keep them inside the same conservative accounting; prefer paraphrase. Presidential addresses (Kennedy, Johnson, Eisenhower, Truman documents), statutes, executive orders, court opinions, and commission reports are public documents and may be quoted from the bank records at the lengths the records carry, cuts marked.

## Hard rules (all documents, decks, notes)
- Zero em dashes and zero en dashes anywhere. Zero instances of the construction "that matters" or "that <anything> matters".
- No colon-led paragraph labels in prose, no decorative quotes, no canned transitions, no motivational closers.
- Audience rule: student-facing files are addressed entirely to the student. No product talk, no marketing copy anywhere in the documents. Teacher keys carry pedagogy.
- Readings: 850 to 900 words of body text (count and report the exact count), five questions, teacher key on its own page at the back with each question restated as a bold lead-in.
- Guided notes: Name/Date/Period line, lesson question, unit question frame, Key Terms list with the definitions below VERBATIM, lettered sections A to G matching the reading, numbered fill-in blanks, a closing summary table, an exit ticket (3 questions), teacher key with every blank answered. Definitions must match the list below character for character.
- Activity: locked print design from the Cold War activity (read one first): 5 stations with Source lines and questions with writing space, a closing ranking or verdict task with paragraph space, teacher key at the back.
- Notebook page: one chart organizer filled from the lesson plus one writing prompt, teacher key with the chart filled in.
- Quick check: short formative, every item tagged to the lesson's blueprint entries in the key.
- Writing task: prompt, evidence bank drawn from the lesson's documents, scaffold, teacher key or rubric. Lesson 7's writing task names TPSP premium DBQ number 22 ("Evaluate the extent to which Black Americans in the 1960s shared one vision of freedom") as a linked extension; it is not reproduced.
- Every document: HTML source plus PDF of the same name, page count verified from the PDF. Student documents end at deliberate page boundaries (full page or clean page and a half); a page that dies a quarter of the way down with dead space after it is a defect to fix by adjusting space heights before delivery.
- Decks: 24 to 29 slides. Slide 1 title, slide 2 the lesson question with the unit essential question as a frame line beneath it, slide 3 the lesson in one slide (lettered sections A to G), then sections in guided-notes order with dividers, content slides with 3 to 5 short fragments, at least two giant stat slides, two vocabulary slides carrying the terms (definitions shown short on screen is fine; the NOTES must carry every term AND its full definition string verbatim, including the strict joined "term: definition" form), a closing synthesis slide and an exit slide. Speaker notes on EVERY slide: 120 to 190 words each, floor 90, carrying the full teaching for that slide's content in guided-notes order, top to tail. Count notes words per slide and report the range.
- Images for decks and documents: public domain only. Prefer National Archives, Library of Congress, presidential libraries (Truman, Eisenhower, Kennedy, Johnson), the United States Information Agency and other federal photographers, and federal records (police and FBI records, government commissions) from Wikimedia Commons / the holding archive. Many famous movement photographs are press photographs under copyright (the Eckford and Hazel Bryan photograph, the Birmingham fire hose and dog photographs, the Bloody Sunday press photographs): do not use any image whose Commons file page does not state a public domain basis you can read and record. Download real files, verify each opens as an image, crop deck images to portrait (about 1046 by 1500) for photo_right and one 16:9 title image, and write img/SOURCES.md per lesson recording title, creator, date, holder, source URL, and public domain basis as shown on the Commons file page. If a download fails or no public domain image exists for a subject, use text and stat slides instead and say so honestly in SOURCES.md. Never invent a catalog number.
- The Emmett Till photographs are NOT reproduced anywhere in this unit. The bank record (cold-war.json, id emmett-till-jet-photographs-1955) describes them; teach from the description, and let the student materials state plainly that the photographs are copyrighted magazine images described rather than shown. No atrocity or corpse photograph is used in any lesson as decoration or otherwise; images of violence are chosen for evidentiary value and captioned exactly, following the World War II unit's Lesson 7 sobriety rule.
- Sources quoted in documents: verbatim from the named edition, cuts marked with ellipses and disclosed in the Source line. Anything labeled a model or teaching summary must say so on its face.

## Vocabulary (use verbatim everywhere: guided notes, decks, study materials)

### Lesson 1 (blueprint 1, 2; five terms carried verbatim from earlier units, marked)
- Jim Crow: the system of state and local laws and customs that enforced racial segregation in the South [carried from the Gilded Age unit]
- segregation: the separation of people by race in public facilities, schools, and transportation [carried from the Gilded Age unit]
- disfranchisement: the denial of the right to vote through law or practice [carried from the Gilded Age unit]
- NAACP: the National Association for the Advancement of Colored People, founded in 1909, which fought segregation through the courts, through lobbying, and through its magazine The Crisis
- Double V campaign: the campaign led by Black newspapers from 1942 for victory over fascism abroad and victory over racism at home [carried from the World War II unit]
- To Secure These Rights: the 1947 report of President Truman's Committee on Civil Rights, which called for federal laws against lynching and disfranchisement and for the end of segregation in American life
- Executive Order 9981: President Truman's order of July 26, 1948 directing equality of treatment and opportunity for all persons in the armed forces, the order that desegregated the United States military

### Lesson 2 (blueprint 3, 4; the Plessy term carried verbatim from the Gilded Age unit)
- Plessy v. Ferguson: the 1896 Supreme Court decision that upheld segregation under the doctrine of separate but equal [carried from the Gilded Age unit]
- separate but equal: the doctrine set by the Supreme Court in Plessy v. Ferguson in 1896, holding that segregation was constitutional as long as the facilities provided for each race were equal
- Brown v. Board of Education: the Supreme Court decision of May 17, 1954 that declared segregation in public schools unconstitutional, ruling that separate educational facilities are inherently unequal
- Brown II: the Supreme Court's 1955 decision ordering school desegregation to proceed with all deliberate speed, a phrase southern officials used to justify years of delay
- massive resistance: the campaign by southern state governments after Brown to prevent school desegregation, using new laws, defiance of federal courts, and in some places the closing of public schools
- Southern Manifesto: the declaration of 1956 signed by 101 southern members of Congress denouncing Brown v. Board of Education as an abuse of judicial power and pledging to resist it
- Cooper v. Aaron: the Supreme Court decision of 1958, arising from Little Rock, holding that state officials are bound by the Court's interpretation of the Constitution and cannot nullify its rulings

### Lesson 3 (blueprint 5, 6)
- boycott: a refusal to buy goods or use services as a form of protest, meant to pressure an institution by withdrawing the money and cooperation it depends on
- Montgomery bus boycott: the protest of 1955 and 1956 in which Black residents of Montgomery, Alabama refused to ride the city's buses for 381 days, ending when the Supreme Court ordered the buses desegregated
- nonviolent direct action: protest that confronts an unjust law or practice openly and without violence, accepting arrest and punishment in order to expose the injustice and force negotiation
- Southern Christian Leadership Conference: the organization founded in 1957 by Martin Luther King Jr. and other Black ministers to coordinate nonviolent protest campaigns across the South
- Emmett Till: the fourteen-year-old Chicago boy murdered in Mississippi in August 1955 after being accused of offending a white woman, whose open-casket funeral and published photographs showed the nation what southern racial violence looked like
- Little Rock Nine: the nine Black students who desegregated Central High School in Little Rock, Arkansas in 1957 under the protection of federal troops after the state's governor tried to bar their entry
- Executive Order 10730: President Eisenhower's order of September 24, 1957 federalizing the Arkansas National Guard and directing federal troops to enforce school desegregation at Little Rock

### Lesson 4 (blueprint 7, 8)
- sit-in: a protest in which demonstrators seat themselves at a segregated facility and refuse to leave until they are served on equal terms or arrested
- Greensboro sit-in: the protest of February 1, 1960 in which four Black college students sat at a segregated Woolworth lunch counter in Greensboro, North Carolina and refused to leave, sparking sit-ins in cities across the South
- Student Nonviolent Coordinating Committee: the organization founded by student activists in April 1960, known as SNCC, which organized sit-ins, Freedom Rides, and voter registration drives in the deepest parts of the South
- Congress of Racial Equality: the civil rights organization founded in 1942, known as CORE, which pioneered nonviolent direct action and organized the Freedom Rides of 1961
- Freedom Rides: the bus journeys of 1961 in which interracial groups of activists rode through the South to test court orders desegregating interstate bus travel and bus terminals
- Albany Movement: the campaign of 1961 and 1962 in Albany, Georgia, where a police chief's polite mass arrests denied the movement a televised crisis and taught it the limits of protest that moved no federal power
- de jure segregation: segregation imposed and enforced by law, as under the southern statutes the courts struck down one by one

### Lesson 5 (blueprint 9, 10)
- Birmingham campaign: the protest campaign of 1963 in Birmingham, Alabama, led by the Southern Christian Leadership Conference and the local movement, whose televised repression pushed President Kennedy to propose a national civil rights bill
- Letter from Birmingham Jail: Martin Luther King Jr.'s letter of April 1963, written from a Birmingham jail cell, defending nonviolent direct action against white clergymen who had called his protests unwise and untimely
- Children's Crusade: the marches of May 1963 in Birmingham in which thousands of Black schoolchildren left their classes to demonstrate and were met with fire hoses, police dogs, and jail, producing the images that turned national opinion
- Kennedy's civil rights address: President Kennedy's televised address of June 11, 1963, after the Birmingham crisis, calling civil rights a moral issue and announcing that he would send Congress a comprehensive civil rights bill
- March on Washington: the demonstration of August 28, 1963 that brought about 250,000 people to the Lincoln Memorial to demand jobs and freedom and to press Congress to pass the civil rights bill
- I Have a Dream: Martin Luther King Jr.'s address closing the March on Washington on August 28, 1963, casting the movement's demands as a claim on the promises of the Declaration of Independence and the Constitution
- 16th Street Baptist Church bombing: the bombing of a Birmingham church by Ku Klux Klan members on September 15, 1963, which killed four Black girls, Addie Mae Collins, Cynthia Wesley, Carole Robertson, and Carol Denise McNair, as they prepared for Sunday services

### Lesson 6 (blueprint 11, 12)
- Civil Rights Act of 1964: the federal law that banned discrimination in public accommodations and employment and allowed the government to cut off funds to segregated programs, the movement's first great legislative victory
- filibuster: the Senate practice of extending debate to block a bill from coming to a vote, broken on the civil rights bill of 1964 when the Senate voted for cloture after more than two months of debate
- Title VII: the section of the Civil Rights Act of 1964 that banned discrimination in employment on the basis of race, color, religion, sex, or national origin
- Freedom Summer: the campaign of 1964 that brought about a thousand mostly northern student volunteers to Mississippi to register Black voters and run Freedom Schools
- Mississippi Freedom Democratic Party: the integrated political party organized in Mississippi in 1964 that challenged the seating of the state's all-white regular delegation at the Democratic National Convention in Atlantic City
- Bloody Sunday: the attack of March 7, 1965 by Alabama state troopers and a sheriff's posse on voting rights marchers at the Edmund Pettus Bridge in Selma, televised to the nation that evening
- Voting Rights Act of 1965: the federal law that suspended literacy tests, sent federal examiners to register voters in covered states, and required those states to clear any change in voting rules with the federal government first

### Lesson 7 (blueprint 13, 14)
- de facto segregation: segregation in fact rather than in law, produced by housing patterns, economics, and custom, the form segregation took in the cities of the North
- Chicago Freedom Movement: Martin Luther King Jr.'s campaign of 1966 against housing and school segregation in Chicago, met by violent mobs on its open-housing marches and ended by an agreement the city did not enforce
- Watts uprising: the six days of violence in the Watts neighborhood of Los Angeles in August 1965, beginning five days after the Voting Rights Act was signed, in which thirty four people died
- Black Power: the call raised by Stokely Carmichael in Mississippi in June 1966 for Black Americans to build their own political and economic power and to define freedom for themselves rather than rely on white goodwill
- Black Panther Party: the organization founded in Oakland, California in 1966 by Huey Newton and Bobby Seale, which patrolled the police, carried arms in self-defense, and ran free breakfast and health programs in Black neighborhoods
- Poor People's Campaign: Martin Luther King Jr.'s planned campaign of 1968 to bring an interracial army of the poor to Washington to demand federal action on poverty, carried on after his assassination as Resurrection City
- Memphis sanitation strike: the strike of 1968 by Black sanitation workers in Memphis, Tennessee, whose signs read I Am a Man, and which brought Martin Luther King Jr. to the city where he was assassinated

### Lesson 8 (blueprint 15)
- Kerner Commission: the federal commission appointed by President Johnson whose 1968 report concluded that the nation was moving toward two societies, one black, one white, separate and unequal, and charged white racism with building the conditions of the urban uprisings
- Fair Housing Act: the Civil Rights Act of 1968, passed in the week after Martin Luther King Jr.'s assassination, banning discrimination in the sale and rental of most housing
- white backlash: the political reaction among white voters against the pace and reach of civil rights change, visible in the Wallace campaigns of the 1960s and the law and order politics that followed
- southern strategy: the Republican electoral strategy of the Nixon years that sought white southern voters by opposing federal civil rights enforcement, busing, and the pace of change the movement had set
- busing: the court-ordered transportation of students across neighborhood lines to desegregate schools, upheld by the Supreme Court in Swann in 1971 and resisted in cities across the country
- affirmative action: government policies that take race into account in hiring, contracting, and college admissions in order to remedy the effects of past discrimination, ordered for federal contractors in the revised Philadelphia Plan of 1969
- Bakke decision: the Supreme Court decision of 1978 in Regents of the University of California v. Bakke, which struck down a set-aside of seats by race in admissions and allowed race to be used as one factor among others

## Per-lesson file set (folder civil-rights/lesson-NN/)
lesson-NN-reading.html/.pdf, lesson-NN-guided-notes.html/.pdf, lesson-NN-activity.html/.pdf, lesson-NN-notebook.html/.pdf, lesson-NN-quick-check.html/.pdf, lesson-NN-writing.html/.pdf, lesson-NN-slides.pptx, lesson-NN-teacher-notes.html/.pdf, img/SOURCES.md, slides-build/ (build_deck.py, build_notes_doc.py, headings.json, img/)
