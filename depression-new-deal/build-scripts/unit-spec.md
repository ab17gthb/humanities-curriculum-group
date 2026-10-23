# Depression and New Deal: shared build spec

Unit essential question: How did the New Deal change the relationship between Americans and their federal government, and what did it leave undone?

Skeleton: ~/workspace/curriculum-planner/depression-new-deal-skeleton.md (read it first).
Model unit: ~/workspace/curriculum-planner/twenties/ — before writing any document type, open the corresponding Twenties file and mirror its structure, CSS, and conventions exactly. Build PDFs with: python3 ~/workspace/curriculum-planner/templates/build_pdf.py <file.html>
Brandmark (first element in body of every document): <p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>
Deck system: ~/workspace/curriculum-planner/depression-new-deal/deck_common.py (copy of the Twenties system). Teacher notes builder: copy build_notes_doc.py from a Twenties lesson's slides-build/ and adapt. Decks keep headings.json in slides-build/.

## Hard rules (all documents, decks, notes)
- Zero em dashes and zero en dashes anywhere. Zero instances of the construction "that matters" or "that <anything> matters".
- No colon-led paragraph labels in prose, no decorative quotes, no canned transitions, no motivational closers.
- Readings: 850 to 900 words of body text (count and report the exact count), five questions, teacher key on its own page at the back with each question restated as a bold lead-in.
- Guided notes: Name/Date/Period line, lesson question, unit question frame, Key Terms list with the definitions below VERBATIM, lettered sections A to G matching the reading, numbered fill-in blanks, a closing summary table, an exit ticket (3 questions), teacher key with every blank answered. Definitions must match the list below character for character.
- Activity: locked print design from the Twenties activity (read one first): 5 stations with Source lines and questions with writing space, a closing ranking or verdict task with paragraph space, teacher key at the back.
- Notebook page: one chart organizer filled from the lesson plus one writing prompt, teacher key with the chart filled in.
- Quick check: short formative, every item tagged to the lesson's blueprint entries in the key.
- Writing task: prompt, evidence bank drawn from the lesson's documents, scaffold, teacher key or rubric.
- Every document: HTML source plus PDF of the same name, page count verified from the PDF.
- Decks: 24 to 29 slides. Slide 1 title, slide 2 the lesson question with the unit essential question as a frame line beneath it, slide 3 the lesson in one slide (lettered sections A to G), then sections in guided-notes order with dividers, content slides with 3 to 5 short fragments, at least two giant stat slides, two vocabulary slides carrying the terms (definitions shown short on screen is fine; the NOTES must carry every term AND its full definition string verbatim), a closing synthesis slide and an exit slide. Speaker notes on EVERY slide: 120 to 190 words each, floor 90, carrying the full teaching for that slide's content in guided-notes order, top to tail. Count notes words per slide and report the range.
- Images for decks and documents: public domain only. Prefer Farm Security Administration and other federal photographs from Wikimedia Commons / Library of Congress. Download real files, verify each opens as an image, crop deck images to portrait (about 1046 by 1500) for photo_right and one 16:9 title image, and write img/SOURCES.md per lesson recording title, creator, date, holder, source URL, and public domain basis as shown on the Commons file page. If a download fails, use text and stat slides instead and say so honestly. Never invent a catalog number.
- Sources quoted in documents: verbatim from the named edition, cuts marked with ellipses and disclosed in the Source line. Public domain texts only (speeches, statutes, court syllabi, pamphlets, government reports). Anything labeled a model or teaching summary must say so on its face.

## Vocabulary (use verbatim everywhere: guided notes, decks, study materials)

### Lesson 1 (blueprint 1, 2)
- Great Depression: the severe economic collapse that began in the United States in 1929 and lasted through the 1930s, marked by bank failures, mass unemployment, and falling prices
- deflation: a general fall in prices across the economy, which raises the real burden of debts and rewards waiting to spend
- bank run: a rush of depositors to withdraw their money from a bank at the same time, driven by fear that the bank will fail
- unemployment: the condition of people who are able to work and seeking work but cannot find a job
- breadline: a line of people waiting for free food given out by a charity, a church, or a city agency
- Hooverville: a shantytown built by homeless people from scrap wood, tin, and cardboard during the Depression, named in bitter reference to President Hoover
- Dust Bowl: the region of the southern Great Plains where drought and poor farming practices turned topsoil to dust in the 1930s, driving many farm families from their land

### Lesson 2 (blueprint 3, 4)
- voluntarism: Hoover's policy of meeting the Depression through voluntary cooperation by business, charities, and local government rather than through federal relief programs
- rugged individualism: Hoover's belief that Americans should succeed through their own effort and that direct federal relief would weaken character and self reliance
- Reconstruction Finance Corporation: the federal agency created in 1932 that lent public money to banks, railroads, and insurance companies in the hope that stability at the top would restore jobs below
- public works: government funded construction projects such as dams, roads, and public buildings, built to provide jobs as well as lasting structures
- Hawley-Smoot Tariff: the 1930 law that raised United States tariffs to the highest level in the country's history, and drew retaliation that cut world trade
- Bonus Army: the veterans of the First World War who camped in Washington in the summer of 1932 demanding early payment of their promised service bonus, and were driven out by federal troops
- interregnum: the period between Roosevelt's election in November 1932 and his inauguration in March 1933, when the outgoing and incoming presidents shared responsibility for a deepening crisis and neither acted decisively

### Lesson 3 (blueprint 5, 6)
- bank holiday: the closing of all the nation's banks by presidential proclamation on March 6, 1933, so that examiners could sort sound banks from failed ones before reopening
- Emergency Banking Act: the law passed by Congress on March 9, 1933, that gave the president broad power over banking and allowed sound banks to reopen under federal license
- fireside chat: one of President Roosevelt's radio addresses to the nation, delivered in plain conversational language from the White House
- Hundred Days: the first phase of Roosevelt's presidency, from March 9 to June 16, 1933, in which Congress passed an exceptional volume of New Deal legislation
- Glass-Steagall Act: the 1933 law that separated commercial banking from investment banking and created federal insurance of bank deposits
- Agricultural Adjustment Act: the 1933 law that paid farmers to reduce production of basic crops and livestock in order to raise farm prices toward parity
- Tennessee Valley Authority: the federal corporation created in 1933 to build dams, control flooding, and bring electricity and development to the Tennessee River valley

### Lesson 4 (blueprint 7, 8)
- direct relief: money, food, or goods given directly to people in need without work required in return
- work relief: government paid jobs on public projects, given to unemployed people instead of direct relief payments
- Civilian Conservation Corps: the 1933 program that employed young men in camps to plant trees, fight fires, and build park roads and trails, paying thirty dollars a month, most of it sent home
- Federal Emergency Relief Administration: the 1933 agency, led by Harry Hopkins, that sent federal relief money to the states to pass on to people in need
- Civil Works Administration: the emergency program that hired about four million unemployed people for the winter of 1933 to 1934 on small public projects
- Public Works Administration: the 1933 agency, led by Harold Ickes, that funded large construction projects such as dams, bridges, schools, and courthouses, built by private contractors
- National Recovery Administration: the agency created in 1933 to write and enforce codes of fair competition for each industry, setting prices, wages, and hours and allowing workers to organize

### Lesson 5 (blueprint 9, 10)
- Share Our Wealth: Huey Long's program and movement, begun in 1934, which promised to cap large fortunes and guarantee every family a homestead and a minimum income
- Townsend Plan: Dr. Francis Townsend's proposal that the federal government pay two hundred dollars a month to every citizen over sixty, on condition the money be spent within the month
- old-age pension: a regular payment made by a government to people who have reached a set age and left regular work
- demagogue: a leader who gains power by arousing popular fears, prejudices, and hopes with simple promises, rather than by answering arguments
- American Liberty League: the organization founded in 1934 by wealthy businessmen and conservative Democrats to oppose the New Deal as a threat to property and the Constitution
- Schechter v. United States: the 1935 Supreme Court decision that struck down the National Industrial Recovery Act, holding that Congress had given away its lawmaking power and reached business beyond its authority
- United States v. Butler: the 1936 Supreme Court decision that struck down the Agricultural Adjustment Act's processing tax as an unconstitutional use of federal power over farm production

### Lesson 6 (blueprint 11, 12)
- Works Progress Administration: the agency created in 1935, led by Harry Hopkins, that employed about eight and a half million people over its life building roads, schools, and airports and funding arts and writing projects
- Social Security Act: the law of August 1935 that created old-age insurance, unemployment insurance with the states, and aid to dependent children and other vulnerable groups
- old-age insurance: the part of Social Security that pays a monthly benefit to retired workers, funded by payroll taxes on workers and their employers
- unemployment insurance: the joint federal and state system, created in 1935, that pays temporary benefits to workers who lose their jobs
- payroll tax: a tax taken from workers' wages and matched by employers, used to fund Social Security
- National Labor Relations Act: the 1935 law, called the Wagner Act, that guaranteed workers the right to organize unions and bargain collectively and created a board to enforce those rights
- collective bargaining: negotiation between an employer and a union chosen by the workers over wages, hours, and working conditions

### Lesson 7 (blueprint 13, 14; new terms six, collective bargaining carried verbatim from Lesson 6)
- sit-down strike: a strike in which workers stop work and remain inside the factory, holding the plant so that replacement workers cannot be brought in
- Congress of Industrial Organizations: the federation formed in 1935 to organize workers by whole industry, including the unskilled, rather than by craft
- United Auto Workers: the union of automobile workers, recognized by General Motors in February 1937 after the Flint sit-down strike
- court packing: the name opponents gave Roosevelt's 1937 proposal to add a new justice to the Supreme Court for each sitting justice over seventy, which would have let him appoint up to six
- Roosevelt recession: the sharp economic downturn of 1937 to 1938, caused in part by federal spending cuts and new payroll taxes pulling money out of a weak economy
- deficit spending: government spending beyond the revenue it collects, financed by borrowing, used to put money into an economy in a slump

### Lesson 8 (blueprint 15)
- New Deal coalition: the alliance of white southerners, northern city voters, union members, farmers, and increasingly Black voters that kept the Democratic Party in national power for a generation after 1932
- Fair Labor Standards Act: the 1938 law that set a federal minimum wage, required overtime pay past forty hours a week, and restricted child labor
- safety net: the set of government programs that catch people who fall into poverty through old age, unemployment, disability, or the loss of a family earner
- redlining: the practice by which federal housing officials and lenders marked minority neighborhoods as risky on maps and denied loans there, keeping Black families from buying homes on equal terms
- repatriation: the removal of people of Mexican descent, including many United States citizens, to Mexico during the Depression, carried out by local and federal authorities under economic pressure
- Securities and Exchange Commission: the federal agency created in 1934 to regulate the stock markets and require honest public reporting by companies selling stock
- Federal Deposit Insurance Corporation: the federal agency created in 1933 that insures bank deposits, so that depositors are repaid by the government if their bank fails

## Per-lesson file set (folder depression-new-deal/lesson-NN/)
lesson-NN-reading.html/.pdf, lesson-NN-guided-notes.html/.pdf, lesson-NN-activity.html/.pdf, lesson-NN-notebook.html/.pdf, lesson-NN-quick-check.html/.pdf, lesson-NN-writing.html/.pdf, lesson-NN-slides.pptx, lesson-NN-teacher-notes.html/.pdf, img/SOURCES.md, slides-build/ (build_deck.py, build_notes_doc.py, headings.json, img/)
