# Reading-Only Pass (started 2026-10-23, Alex's call)

## Rule (stricter than the course-wide alignment audit)

Every question in a reading document and a quick check must be answerable from that document alone: the reading text, and the sources, passages, background notes, data, and captions printed on that same document. No fallback to the rest of the lesson set (guided notes, activity stations, notebook, slides, teacher notes).

Scope: all 15 teaching units, Lessons 1-8, reading + quick check = 240 documents.

## Method

1. Machine screen per document: split student text from the teacher key at the Teacher Answer Key heading; flag key sentences carrying a number, date, or proper name that appears nowhere in the document's own student text.
2. Full read of every flagged item in context, plus a read of each document's questions and key against its student text.
3. Fix direction, same as the alignment audit: add the missing context to the document when the question targets core content; trim or reword the key when it reaches past the document.
4. Every fix applied with an asserted replacement, PDF rebuilt, uploaded (paid units: Firebase Storage `hcg/<unit>/`; Progressive Era: site files + hosting deploy), MD5 verified.
5. Log each unit here as it completes.

## Log

### Colonial America readings: COMPLETE (2026-10-23)
All 8 reading keys read against their own reading text. Two fixes, both additions to the reading:
- L1: the key located the Iroquois Confederacy "in present day New York"; the reading said only "the northeast woodlands." Reading Section C now reads "the northeast woodlands of present day New York."
- L5: the key listed the Maryland act's fine for reproachful speeches about the Virgin Mary and the apostles; the reading's account of the act omitted that penalty. Added to the reading's summary of the act.
Both rebuilt, uploaded to hcg/colonial-america/, MD5 verified. All other flagged items adjudicated as false positives (name-token variants like "Governor Cosby" vs "Governor William Cosby" in the text; source-citation lines in keys) or grading guidance.

### Quick check design finding (2026-10-23, DECIDED by Alex 2026-10-23)
Quick checks follow one design across the unit: Q1 works the printed source/background on the page; Q2-Q4 test the lesson just taught (recall and synthesis), and their keys state lesson facts that are not printed on the QC page. Under a strict page-only rule nearly every QC fails the same way by design, not by error. Audit 1 verified every one of those facts against the lesson record. Options put to Alex: (A) hold QCs to the lesson standard; (B) keep the lesson standard and rewrite QC directions so the page no longer implies page-only answering; (C) expand QC backgrounds to carry every needed fact.

Alex's decision (2026-10-23): leave quick checks on the lesson standard as they are. No QC changes in this pass; QC keys remain graded against the lesson record, which audit 1 verified. The pass proceeds on readings only.

### The Founding readings: COMPLETE (2026-10-23)
All 8 reading keys read against their own reading text. No fixes. Flagged items adjudicated: the key's conventional names for events the reading describes in full (the Virginia Resolves, the Stamp Act Congress, Bunker Hill) and its calendar date for the Lexington testimony the reading places "a week later" (April 25, 1775) carry the reading's own substance, not new facts. L7's three-fifths worked example (100,000 counted as 60,000) is printed in the reading itself.

### Early Republic readings: COMPLETE (2026-10-23)
All 8 reading keys read against their own reading text. Five fixes in three lessons, all grounding the key in the reading:
- L1: the key dates the whiskey excise to 1791; the reading now dates it ("an excise tax on distilled whiskey in 1791").
- L5 (three fixes): the key has Tecumseh dying at the Thames in 1813, the Capitol and President's House fired in the burning of Washington, and the Treaty of Fort Jackson named; the reading narrated the first two without those facts and left the treaty unnamed. All three now in the reading (Sections C and E and the Horseshoe Bend passage).
- L8: the key dates Polk's war message May 11, 1846 and Lincoln's spot resolutions December 1847; both dates now in the reading.
All rebuilt, uploaded to hcg/early-republic/, MD5 verified. L3's "Article III" is the conventional label for the treaty promise the reading states in full; adjudicated grounded. L2, L4, L6, L7 clean.

### Jackson and Reform readings: COMPLETE (2026-10-23)
All 8 reading keys read against their own reading text. Two fixes, both trims in the Lesson 1 key:
- Q2's parenthetical "(the reading also notes Pennsylvania followed the same course in 1838)" removed: the reading notes no such thing, and Pennsylvania 1838 appears nowhere in the reading.
- Q4's "her first marriage and divorce" trimmed to the reading's own words, "her first marriage."
Rebuilt, uploaded to hcg/jackson-reform/lesson-01-reading.pdf, MD5 verified. Lessons 2-8 clean (New Echota signers, Quatie Ross, the Whig coalescence, Mann, Walker, and the London gallery all verified present in their readings).

### Sectional Crisis and Civil War readings: COMPLETE (2026-10-23)
All 8 reading keys read against their own reading text. Two fixes, both additions to readings:
- L2: the key names Josiah Henson's account as Stowe's particular source; the reading credited only "the slave narratives" generally. Henson now named in the reading.
- L6: the key dates Lincoln's nationwide habeas suspension September 24, 1862; the reading narrated it under "In September 1862." The reading now carries the date.
Both rebuilt, uploaded to hcg/sectional-crisis/, MD5 verified. Adjudicated grounded: Gage's 1863 (the reading's "twelve years later" from 1851), Lincoln's April 15 call (the reading's "the next day" after the April 14 surrender), the Proclamation's "Executive Government" wording (the reading's own paraphrase of the same order), and the Pierce/Sumner/Freeport/Charleston items, all verified present in their readings.

### Reconstruction readings: COMPLETE (2026-10-23)
All 8 reading keys read against their own reading text. No fixes: the cleanest unit of this pass, matching its audit 1 result. The two screen candidates resolved in the text: Lincoln's death date is the reading's "shot five days later [after April 9], died the next morning," and Anderson's $11,680 is the reading's own "eleven thousand six hundred eighty dollars" in numeral form. The governing coalition, Pinchback, the Amnesty Act of May 1872, and Justice Miller items all verified present.

### The Gilded Age readings: COMPLETE (2026-10-23)
All 8 reading keys read against their own reading text. No fixes. The screen's candidates were sentence-initial artifacts and two identifications the readings support: the key's "Sherman Act" is the short form of the Sherman Antitrust Act the reading names, and "the Illinois governor" is the governor whose objection the reading records over troops sent to Chicago.

### Progressive Era readings: COMPLETE (2026-10-23)
All 8 reading keys read against their own reading text. No fixes. The Tennessee ratification count in the Lesson 7 key (thirty-five states by August 1920, Tennessee's the thirty-sixth) is the reading's own count plus its arithmetic. Remaining flags were grading guidance and interpretive limits the keys state openly.

### Imperialism and World War I readings: COMPLETE (2026-10-23)
All 8 reading keys read against their own reading text. One fix: L7's key states the Espionage Act's penalties (fines up to $10,000, up to twenty years) that the reading omitted; the reading now carries them. The keys in this unit carry edition citations for every quotation (teacher-facing apparatus, not answer content). Adjudicated grounded: the Treaty of Paris vote arithmetic (the reading's 57 to 27 yields the key's 84 cast and 56 required), the Hawaii missionary/plantation sequence, the Panama costs, the Lusitania and Sussex pledge record, the 370,000 Black servicemen figure, and the Scott migration figure, all verified in their readings.

### The Twenties readings: COMPLETE (2026-10-23)
All 8 reading keys read against their own reading text. No fixes. KDKA and the Harding-Cox returns, the motor vehicle death figures in the Lesson 3 key's strong-answer examples, Sacco and Vanzetti, the Dyer bill's House passage and Senate filibuster death, the Coolidge vetoes, and the Black Thursday and Tuesday share volumes all verified present in their readings.

### Depression and New Deal readings: COMPLETE (2026-10-23)
All 8 reading keys read against their own reading text. One fix: L5's key and its question require Huey Long's fortune cap figure, which the reading stated only as "capped large fortunes"; the reading now gives the February 1934 address's figure, $50,000,000, beside the $5,000 guarantee and thirty dollar pension it already carried. The March 12 fireside chat date and the Schechter record verified present.

### World War II readings: COMPLETE (2026-10-23)
All 8 reading keys read against their own reading text. No fixes. Lesson 2's key models the standard correctly on its face: it accepts the Pearl Harbor wounded figure of about 1,178 only as an optional addition from the activity record, not as a requirement. The Nye Committee record, the Omaha and Mulberry and Saint-Lo details, the Potsdam Declaration date, and the Franck Report items all verified present in their readings.

### The Cold War readings: COMPLETE (2026-10-23)
All 8 reading keys read against their own reading text. Two fixes, both naming what the reading described:
- L7: the key dates the second SALT treaty to June 1979; the reading dated the agreements only to 1979. The month is now in the reading.
- L8: the key names Reagan's missile defense program the Strategic Defense Initiative; the reading described it unnamed. Now named in the reading.
Both rebuilt, uploaded to hcg/cold-war/, MD5 verified. Adjudicated grounded: Executive Order 9835 and the loyalty program record, the Mossadegh overthrow, and the Khrushchev reasons; the Lesson 5 key's NATO gloss on the secret Turkey withdrawal is explanatory analysis of facts the reading carries, left as written.

### Civil Rights readings: COMPLETE (2026-10-23)
All 8 reading keys read against their own reading text. No fixes. The Lesson 3 key's Chapter 6, Section 11 citation carries its own provenance note (the arrest record as carried in the bank), and the charge itself is stated in the reading. The Smith v. Allwright holding, the Greensboro and Albany records, the Voting Rights Act coverage formula (stated in full in the Lesson 6 reading), the Meredith March, and the Milliken and Fair Housing items all verified present. Lesson 5's key carries the unit's copyright accounting (Letter and Dream quoted at no more than 90 words each) as teacher apparatus.

### Modern America readings: COMPLETE (2026-10-23)
All 8 reading keys read against their own reading text. Three fixes, all in the readings:
- L1: the key's stagflation sentence pairs 1979 and 1980 unemployment (5.9 and 7.2 percent); the reading carried only the 1980 figure (the 1979 figure lived in the activity data table). The reading now states both years.
- L5: the key quotes the 1983 commission's conclusion naming Executive Order 9066; the reading described the removal without naming the order. Now named where the removal is narrated.
- L8: the key gives Bakke's specifics (the University of California medical school's set aside of sixteen seats); the reading stated only "a set aside of seats." Now stated in full.
All rebuilt, uploaded to hcg/modern-america/, MD5 verified. The Gulf War coalition record, the manufacturing employment figures, the Hart-Celler signing date, and the September 11 and 20 Bush statements verified present.

## PASS COMPLETE (2026-10-23)
All 120 lesson readings across the 15 units rechecked under the document-only standard: every reading's questions and key answerable from that reading alone. 18 fixes in 13 documents across 9 units (Colonial 2, Early Republic 5, Jackson 2 key trims, Sectional Crisis 2, Imperialism/WWI 1, Depression/New Deal 1, Cold War 2, Modern America 3); six units needed none (Founding, Reconstruction, Gilded Age, Progressive Era, Twenties, World War II). Fix direction held throughout: core facts the key required were added to the reading; the two exceptions were Jackson Lesson 1 key trims where the key asserted what the reading does not contain. Every fix rebuilt, uploaded to Firebase Storage, and MD5 verified. Quick checks unchanged under the lesson standard, per Alex's decision of 2026-10-23.
