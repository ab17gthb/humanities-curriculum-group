# Modern America: shared build spec

Unit essential question: How did the United States remake itself after 1980, in its economy, its population, and its place in the world, and what did the remaking settle and what did it leave open?

Skeleton: ~/workspace/curriculum-planner/modern-america-skeleton.md (read it first, in full, plus your lesson's section twice).
Model units: ~/workspace/curriculum-planner/civil-rights/ and ~/workspace/curriculum-planner/cold-war/ — before writing any document type, open the corresponding Civil Rights file (same lesson number where possible, otherwise Civil Rights Lesson 1 or Cold War Lesson 1) and mirror its structure, CSS, and conventions exactly. Build PDFs with: python3 ~/workspace/curriculum-planner/templates/build_pdf.py <file.html>
Brandmark (first element in body of every document): <p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>
Deck system: ~/workspace/curriculum-planner/modern-america/deck_common.py (copy of the Civil Rights system). Teacher notes builder: copy build_notes_doc.py from a Civil Rights lesson's slides-build/ and adapt. Decks keep headings.json in slides-build/.
Audited source texts: the TPSP bank file ~/workspace/primary-source/vite-react-main/public/data/modern.json holds verbatim audited text with the edition named in each record's sourceNote. Quote from those records, with cuts marked by ellipses and the edition named in the Source line. Never quote from memory where a bank record exists. For public documents not in the bank (statutes, court opinions, commission reports), fetch the named edition from its official source (GovInfo, Congress.gov, supremecourt.gov, the presidential libraries, Census, BLS) and name the edition in the Source line; if you cannot fetch and verify the text, teach that station as a labeled summary resting on the public record instead of quoting.

## Copyright and evidence discipline (binding, this unit above all)
- Public documents may be quoted at the lengths the bank records or named editions carry: works of the federal government, presidential addresses and statements, statutes, executive orders, court opinions, commission reports, federal statistics.
- Copyrighted works (Barbara Jordan's 1976 convention keynote, the memoirs Warriors Don't Cry and Paul Fussell's essay, journalism, editorial cartoons, magazine writing) may be quoted ONLY at the short lengths the audited bank records themselves carry, never more than 90 quoted words from any one work across the whole unit, and every use is logged in the lesson's img/SOURCES.md so the manifest can disclose totals.
- The Herblock "Mugging" cartoon and the UFW poster exist in the bank as descriptions only. Teach them as described records. Do not reproduce the images.
- No editorial verdicts in any material. Contested and recent events are taught from documents and data, with claims attributed to their makers ("critics charged," "the administration answered"). Teacher keys grade the use of evidence, never the side a student takes. This applies with full force to Lessons 6, 7, and 8.
- Facts are stated at the precision the evidence supports; figures drawn from federal statistics name their source (Bureau of Labor Statistics, Census Bureau, Federal Reserve, Congressional Budget Office) in the document.

## Hard rules (all documents, decks, notes)
- Zero em dashes and zero en dashes anywhere. Zero instances of the construction "that matters" or "that <anything> matters".
- No colon-led paragraph labels in prose, no decorative quotes, no canned transitions, no motivational closers.
- Audience rule: student-facing files are addressed entirely to the student. No product talk, no marketing copy anywhere in the documents. Teacher keys carry pedagogy.
- Readings: 850 to 900 words of body text (count and report the exact count), five questions, teacher key on its own page at the back with each question restated as a bold lead-in.
- Guided notes: Name/Date/Period line, lesson question, unit question frame, Key Terms list with the definitions below VERBATIM, lettered sections A to G matching the reading, numbered fill-in blanks, a closing summary table, an exit ticket (3 questions), teacher key with every blank answered. Definitions must match the list below character for character.
- Activity: locked print design from the Civil Rights activity (read one first): 5 stations with Source lines and questions with writing space, a closing ranking or verdict task with paragraph space, teacher key at the back.
- Notebook page: one chart organizer filled from the lesson plus one writing prompt, teacher key with the chart filled in.
- Quick check: short formative, source-based where the lesson's records allow, every item tagged to the lesson's blueprint entries in the key.
- Writing task: prompt, evidence bank drawn from the lesson's documents, scaffold, teacher key or rubric with blueprint tags. Lesson 8's writing task names TPSP premium DBQ number 23 ("Evaluate the extent to which Americans' debate since 1968 over what the country should be has been about its moral condition rather than its policies") as a linked extension; it is not reproduced.
- Every document: HTML source plus PDF of the same name, page count verified from the PDF. Student documents end at deliberate page boundaries (full page or clean page and a half); a page that dies a quarter of the way down with dead space after it is a defect to fix by adjusting space heights before delivery.
- Decks: 24 to 29 slides. Slide 1 title, slide 2 the lesson question with the unit essential question as a frame line beneath it, slide 3 the lesson in one slide (lettered sections A to G), then sections in guided-notes order with dividers, content slides with 3 to 5 short fragments, at least two giant stat slides, two vocabulary slides carrying the terms (definitions shown short on screen is fine; the NOTES must carry every term AND its full definition string verbatim, including the strict joined "term: definition" form), a closing synthesis slide and an exit slide. Speaker notes on EVERY slide: 120 to 190 words each, floor 90, carrying the full teaching for that slide's content in guided-notes order, top to tail. Count notes words per slide and report the range.
- Images for decks and documents: public domain only. Prefer National Archives, Library of Congress, presidential libraries (Carter, Reagan, George H. W. Bush, Clinton, George W. Bush, Obama White House archives), FEMA, NASA, the Census Bureau, and other federal photographers from Wikimedia Commons / the holding archive. Many famous recent photographs are press photographs under copyright (the flag raising at Ground Zero, the Situation Room photograph is federal and public domain, most newspaper photography is not): do not use any image whose Commons file page does not state a public domain basis you can read and record. Download real files, verify each opens as an image, crop deck images to portrait (about 1046 by 1500) for photo_right and one 16:9 title image, and write img/SOURCES.md per lesson recording title, creator, date, holder, source URL, and public domain basis as shown on the Commons file page. If a download fails or no public domain image exists for a subject, use text and stat slides instead and say so honestly in SOURCES.md. Never invent a catalog number.
- Sources quoted in documents: verbatim from the named edition, cuts marked with ellipses and disclosed in the Source line. Anything labeled a model or teaching summary must say so on its face.

## Vocabulary (use verbatim everywhere: guided notes, decks, study materials)

### Lesson 1 (blueprint 1, 2; the southern strategy term carried verbatim from the Civil Rights unit, marked)
- stagflation: the combination of stagnant economic growth, high unemployment, and high inflation that afflicted the American economy in the 1970s, defying the usual rule that inflation and unemployment moved in opposite directions
- energy crisis: the shortages and sharp price rises in oil and gasoline that struck the United States in 1973 and again in 1979, when oil-producing states cut exports and revolution in Iran halted production
- tax revolt: the movement of the late 1970s in which voters demanded lower taxes and limits on government spending, beginning with California's Proposition 13 in 1978 and spreading across the country
- Proposition 13: the California ballot measure of 1978 that cut property taxes sharply and capped their future growth, the opening victory of the national tax revolt
- New Right: the coalition of conservative activists, organizations, and voters that rose in the 1970s around lower taxes, a stronger military, and resistance to the social changes of the 1960s
- Moral Majority: the political organization founded by the Reverend Jerry Falwell in 1979 to mobilize evangelical Christian voters behind conservative candidates and causes
- southern strategy: the Republican electoral strategy of the Nixon years that sought white southern voters by opposing federal civil rights enforcement, busing, and the pace of change the movement had set [carried from the Civil Rights unit]

### Lesson 2 (blueprint 3, 4)
- supply-side economics: the economic theory behind the Reagan program, holding that cutting tax rates and reducing regulation would free investment and production and so grow the whole economy
- deregulation: the removal or loosening of government rules on an industry, pursued from the late 1970s onward in airlines, trucking, banking, and communications
- Reagan Democrat: a traditionally Democratic voter, often a white working class or union voter, who voted for Ronald Reagan in 1980 and 1984 while often remaining a Democrat
- PATCO strike: the strike of August 1981 in which President Reagan fired more than eleven thousand federal air traffic controllers who had struck illegally, a blow unions took as a signal of the era's terms
- federal deficit: the amount by which a year's federal spending exceeds the year's revenue, added each year to the national debt
- Iran-Contra affair: the scandal of 1985 to 1987 in which officials of the Reagan administration secretly sold arms to Iran and diverted the proceeds to the Contra rebels in Nicaragua, against stated policy and a congressional ban
- War on Drugs: the campaign of intensified drug enforcement and mandatory sentences pursued by the federal government from the 1970s onward and greatly expanded in the 1980s, which raised prison populations across the country

### Lesson 3 (blueprint 5, 6)
- peace dividend: the money and attention Americans expected to redirect from military spending to needs at home once the Cold War ended in 1991, debated through the 1990s
- Persian Gulf War: the war of January and February 1991 in which an American-led coalition, acting with United Nations authorization, drove Iraq's army out of Kuwait in six weeks
- globalization: the deepening connection of the world's economies through trade, investment, and production spread across borders, which accelerated after the Cold War
- North American Free Trade Agreement: the agreement among the United States, Canada, and Mexico that took effect in 1994 and removed most tariffs and trade barriers among the three countries
- outsourcing: the practice of moving work, especially factory production and later office and service jobs, to lower-cost workers in other countries
- Rust Belt: the name given to the industrial region of the Northeast and Midwest where factory closings from the 1970s onward emptied mills and cost whole cities much of their population
- service economy: an economy in which most jobs produce services, such as health care, retail, finance, and food, rather than goods, the form the American economy took as factory employment shrank

### Lesson 4 (blueprint 7, 8)
- personal computer: a computer built for one person's desk and home, sold in large numbers from the late 1970s onward, which carried computing out of institutions and into daily life
- Internet: the network of computer networks that grew out of government and university systems into a public means of communication, commerce, and publication in the 1990s
- e-commerce: the buying and selling of goods and services over the Internet, which grew from almost nothing in the middle 1990s into a central part of American retail
- dot-com bubble: the speculative boom in Internet company stocks in the late 1990s, ending in a crash in 2000 and 2001 that erased trillions of dollars in paper wealth
- cable news: television news carried by cable channels around the clock, beginning with CNN in 1980, which replaced the nightly broadcast as many Americans' main source of news
- social media: the Internet platforms, growing from the middle 2000s, on which users publish their own words, photographs, and video and build networks of followers and friends
- digital divide: the gap between Americans with ready access to computers and the Internet and those without, which followed lines of income, education, age, and place

### Lesson 5 (blueprint 9, 10)
- Immigration and Nationality Act of 1965: the law that ended the national origins quota system in place since the 1920s and opened American immigration chiefly to family reunification and needed skills, transforming the sources of immigration
- Immigration Reform and Control Act of 1986: the law that granted legal status to about three million unauthorized immigrants already in the country and made it illegal for employers knowingly to hire unauthorized workers
- amnesty: in immigration law, a grant of legal status to people who entered or remained in the country without authorization, as the 1986 act gave to those who had arrived before 1982
- Sun Belt: the fast-growing region of the South and Southwest, whose population, jobs, and political weight rose from the 1970s onward on air conditioning, defense and technology work, and lower costs
- deindustrialization: the long decline of manufacturing employment in the United States from the 1970s onward, as factories closed, automated, or moved abroad
- gentrification: the movement of wealthier residents and new investment into poorer city neighborhoods, raising prices and rents and often pushing out the people who lived there
- white flight: the movement of white families from cities to suburbs in the decades after the Second World War, accelerated by school desegregation orders and changing neighborhoods, which shrank city tax bases

### Lesson 6 (blueprint 11, 12)
- September 11 attacks: the terrorist attacks of September 11, 2001, in which hijackers of the al Qaeda network flew passenger planes into the World Trade Center and the Pentagon and crashed a fourth plane in Pennsylvania, killing 2,977 people
- al Qaeda: the terrorist network led by Osama bin Laden that carried out the September 11 attacks, built from veterans of the war against the Soviet Union in Afghanistan
- War on Terror: the worldwide campaign of military action, intelligence work, and security measures the United States declared after September 11, 2001, against al Qaeda and the groups and states said to shelter it
- Authorization for Use of Military Force: the law Congress passed on September 18, 2001 authorizing the president to use all necessary and appropriate force against those responsible for the September 11 attacks and those who harbored them
- USA PATRIOT Act: the law of October 2001 that widened the government's powers of surveillance, search, and detention in terrorism investigations, passed by overwhelming margins in the weeks after September 11
- Department of Homeland Security: the cabinet department created in 2002 that merged twenty two federal agencies and offices charged with protecting the country against terrorist attack and disaster
- weapons of mass destruction: chemical, biological, and nuclear weapons; the claim that Iraq possessed stockpiles of them was the stated ground for the American invasion of Iraq in 2003, and no such stockpiles were found

### Lesson 7 (blueprint 13, 14)
- subprime mortgage: a home loan made to a borrower with weak credit at a higher interest rate, issued in large numbers during the housing boom of the 2000s and central to the financial crisis when house prices fell
- Great Recession: the economic collapse of 2007 to 2009, the deepest since the Great Depression, in which the financial system nearly failed, unemployment reached ten percent, and millions of families lost their homes
- Troubled Asset Relief Program: the program of October 2008, known as TARP, in which the federal government was authorized to spend up to seven hundred billion dollars to steady the banking system by buying troubled assets and investing in banks
- stimulus: government spending and tax cuts meant to restart a stalled economy by putting money in consumers' hands, as in the American Recovery and Reinvestment Act of 2009, at about eight hundred billion dollars
- Affordable Care Act: the health care law of 2010 that required most Americans to carry health insurance, barred insurers from denying coverage for prior illness, and expanded Medicaid, the largest change to American health policy since the 1960s
- Tea Party movement: the conservative protest movement that rose in 2009 against the bank bailouts, the stimulus, and the health care law, demanding smaller government and lower taxes, and that reshaped Republican politics
- Occupy Wall Street: the protest movement that began in New York in September 2011 and spread to cities across the country, camping in financial districts to protest economic inequality in the name of the ninety nine percent against the one percent

### Lesson 8 (blueprint 15; the affirmative action term carried verbatim from the Civil Rights unit, marked)
- political polarization: the sorting of Americans into two hostile political camps with fewer voters in the middle, visible from the 1990s onward in voting records, media habits, and measures of party identity
- Bush v. Gore: the Supreme Court decision of December 2000 that stopped the recount of Florida's presidential ballots and settled the election of 2000 for George W. Bush, decided by five votes to four
- Citizens United v. Federal Election Commission: the Supreme Court decision of 2010 holding that the government may not limit independent political spending by corporations and unions, which opened the way to super PACs and large outside spending in elections
- District of Columbia v. Heller: the Supreme Court decision of 2008 holding that the Second Amendment protects an individual's right to keep a handgun in the home for self-defense
- Obergefell v. Hodges: the Supreme Court decision of 2015 holding that the Fourteenth Amendment requires every state to license marriages between two people of the same sex and to recognize such marriages licensed in other states
- affirmative action: government policies that take race into account in hiring, contracting, and college admissions in order to remedy the effects of past discrimination, ordered for federal contractors in the revised Philadelphia Plan of 1969 [carried from the Civil Rights unit]
- COVID-19 pandemic: the worldwide spread of the coronavirus disease first identified in 2019, which reached the United States in 2020, killed more than a million Americans, and closed schools, businesses, and public life for months

## Per-lesson file set (folder modern-america/lesson-NN/)
lesson-NN-reading.html/.pdf, lesson-NN-guided-notes.html/.pdf, lesson-NN-activity.html/.pdf, lesson-NN-notebook.html/.pdf, lesson-NN-quick-check.html/.pdf, lesson-NN-writing.html/.pdf, lesson-NN-slides.pptx, lesson-NN-teacher-notes.html/.pdf, img/SOURCES.md, slides-build/ (build_deck.py, build_notes_doc.py, headings.json, img/)
