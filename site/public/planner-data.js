// Progressive Era unit data for the planner prototype.
// Every item's tags are the test-blueprint entries it teaches or assesses,
// taken from the unit build manifest. days = class days the item takes
// (0 = runs the same day as the item above it, e.g. guided notes with the reading).
window.HCG_BLUEPRINT = {
  1: "Problems of industrial America",
  2: "Muckrakers and exposure",
  3: "Political reforms",
  4: "Seventeenth Amendment and direct democracy",
  5: "Trust-busting and the Square Deal",
  6: "Consumer protection",
  7: "Conservation under Roosevelt",
  8: "Taft and the Republican split",
  9: "Election of 1912",
  10: "Wilson's New Freedom",
  11: "Sixteenth Amendment and the income tax",
  12: "Women's suffrage and the Nineteenth Amendment",
  13: "Opposition to suffrage",
  14: "Progressivism and race",
  15: "Eighteenth Amendment and Prohibition"
};

window.HCG_LESSONS = [
  { n: 1, title: "The Problems Progressives Faced" },
  { n: 2, title: "The Muckrakers" },
  { n: 3, title: "Reforming Government" },
  { n: 4, title: "Roosevelt and the Square Deal" },
  { n: 5, title: "Taft, the Split, and the Election of 1912" },
  { n: 6, title: "Wilson and the New Freedom" },
  { n: 7, title: "The Fight for Women's Suffrage" },
  { n: 8, title: "The Limits of Progressivism" }
];

window.HCG_ITEMS = [
  // Lesson 1
  { id: "l1-reading", lesson: 1, kind: "Reading", name: "The Problems Progressives Faced", days: 1, tags: [1], file: "files/lesson-01-reading.pdf", core: true },
  { id: "l1-notes", lesson: 1, kind: "Guided Notes", name: "Lesson 1 guided notes", days: 0, tags: [1], file: "files/lesson-01-guided-notes.pdf", core: true },
  { id: "l1-activity", lesson: 1, kind: "Activity", name: "The Reformer's Notebook (stations)", days: 1, tags: [1], file: "files/lesson-01-activity.pdf", core: true },
  { id: "l1-notebook", lesson: 1, kind: "Notebook", name: "Problems, causes, and who cared", days: 0.5, tags: [1], file: "files/lesson-01-notebook.pdf" },
  { id: "l1-quick", lesson: 1, kind: "Quick Check", name: "Triangle fire escape photograph", days: 0.5, tags: [1], file: "files/lesson-01-quick-check.pdf" },
  // Lesson 2
  { id: "l2-reading", lesson: 2, kind: "Reading", name: "The Muckrakers", days: 1, tags: [2, 6], file: "files/lesson-02-reading.pdf", core: true },
  { id: "l2-notes", lesson: 2, kind: "Guided Notes", name: "Lesson 2 guided notes", days: 0, tags: [2], file: "files/lesson-02-guided-notes.pdf", core: true },
  { id: "l2-activity", lesson: 2, kind: "Activity", name: "Be a Muckraker: write your own exposé", days: 1, tags: [2], file: "files/lesson-02-activity.pdf", core: true },
  { id: "l2-notebook", lesson: 2, kind: "Notebook", name: "Muckraker match chart", days: 0.5, tags: [2], file: "files/lesson-02-notebook.pdf" },
  // Lesson 3
  { id: "l3-reading", lesson: 3, kind: "Reading", name: "Reforming Government", days: 1, tags: [3, 4, 15], file: "files/lesson-03-reading.pdf", core: true },
  { id: "l3-notes", lesson: 3, kind: "Guided Notes", name: "Lesson 3 guided notes", days: 0, tags: [3, 4, 15], file: "files/lesson-03-guided-notes.pdf", core: true },
  { id: "l3-activity", lesson: 3, kind: "Activity", name: "Ballot simulation: a 1908 mill town", days: 1, tags: [3], file: "files/lesson-03-activity.pdf", core: true },
  { id: "l3-quick", lesson: 3, kind: "Quick Check", name: "Reform terms", days: 0.5, tags: [3, 4], file: "files/lesson-03-quick-check.pdf" },
  // Lesson 4
  { id: "l4-reading", lesson: 4, kind: "Reading", name: "Roosevelt and the Square Deal", days: 1, tags: [5, 6, 7], file: "files/lesson-04-reading.pdf", core: true },
  { id: "l4-notes", lesson: 4, kind: "Guided Notes", name: "Lesson 4 guided notes", days: 0, tags: [5, 6, 7], file: "files/lesson-04-guided-notes.pdf", core: true },
  { id: "l4-activity", lesson: 4, kind: "Activity", name: "Conservation map work", days: 1, tags: [7], file: "files/lesson-04-activity.pdf", core: true },
  { id: "l4-notebook", lesson: 4, kind: "Notebook", name: "The three-sided Square Deal organizer", days: 0.5, tags: [5, 6, 7], file: "files/lesson-04-notebook.pdf" },
  // Lesson 5
  { id: "l5-reading", lesson: 5, kind: "Reading", name: "Taft, the Split, and the Election of 1912", days: 1, tags: [8, 9], file: "files/lesson-05-reading.pdf", core: true },
  { id: "l5-notes", lesson: 5, kind: "Guided Notes", name: "Lesson 5 guided notes", days: 0, tags: [8, 9], file: "files/lesson-05-guided-notes.pdf", core: true },
  { id: "l5-chart", lesson: 5, kind: "Activity", name: "The 1912 comparison chart", days: 0.5, tags: [9], file: "files/lesson-05-activity-chart.pdf" },
  { id: "l5-campaign", lesson: 5, kind: "Activity", name: "Campaign poster or speech", days: 1, tags: [9], file: "files/lesson-05-activity-campaign.pdf", core: true },
  { id: "l5-quick", lesson: 5, kind: "Quick Check", name: "The election of 1912", days: 0.5, tags: [8, 9], file: "files/lesson-05-quick-check.pdf" },
  // Lesson 6
  { id: "l6-reading", lesson: 6, kind: "Reading", name: "Wilson and the New Freedom", days: 1, tags: [10, 11], file: "files/lesson-06-reading.pdf", core: true },
  { id: "l6-notes", lesson: 6, kind: "Guided Notes", name: "Lesson 6 guided notes", days: 0, tags: [10, 11], file: "files/lesson-06-guided-notes.pdf", core: true },
  { id: "l6-activity", lesson: 6, kind: "Activity", name: "Sort the Record: NF or NN", days: 1, tags: [10], file: "files/lesson-06-activity.pdf", core: true },
  { id: "l6-notebook", lesson: 6, kind: "Notebook", name: "Wilson reforms organizer", days: 0.5, tags: [10, 11], file: "files/lesson-06-notebook.pdf" },
  // Lesson 7
  { id: "l7-reading", lesson: 7, kind: "Reading", name: "The Fight for Women's Suffrage", days: 1, tags: [12, 13], file: "files/lesson-07-reading.pdf", core: true },
  { id: "l7-notes", lesson: 7, kind: "Guided Notes", name: "Lesson 7 guided notes", days: 0, tags: [12, 13], file: "files/lesson-07-guided-notes.pdf", core: true },
  { id: "l7-writing", lesson: 7, kind: "Writing", name: "Strategy memo: state road or federal amendment", days: 1, tags: [12, 13], file: "files/lesson-07-writing.pdf", core: true },
  { id: "l7-quick", lesson: 7, kind: "Quick Check", name: "The suffrage fight", days: 0.5, tags: [12, 13], file: "files/lesson-07-quick-check.pdf" },
  // Lesson 8
  { id: "l8-reading", lesson: 8, kind: "Reading", name: "The Limits of Progressivism", days: 1, tags: [14, 15], file: "files/lesson-08-reading.pdf", core: true },
  { id: "l8-notes", lesson: 8, kind: "Guided Notes", name: "Lesson 8 guided notes", days: 0, tags: [14, 15], file: "files/lesson-08-guided-notes.pdf", core: true },
  { id: "l8-writing", lesson: 8, kind: "Writing", name: "Seminar prep: how much changed", days: 1, tags: [14, 15], file: "files/lesson-08-writing.pdf", core: true },
  // Review day
  { id: "rev-guide", lesson: 9, kind: "Review", name: "Study guide (review day)", days: 1, tags: [], file: "files/review-study-guide.pdf", core: true },
  { id: "rev-cross", lesson: 9, kind: "Review", name: "Crossword (56 answers)", days: 0.5, tags: [], file: "files/review-crossword.pdf" }
];

// National topics for this era — the themes US History courses teach in every state,
// not tied to any one state's standards. Teachers can check these against their own
// state framework; the topics themselves are state-neutral.
window.HCG_TOPICS = {
  1: { label: "Industrial growth and big business", note: "" },
  2: { label: "Labor and the working class", note: "" },
  3: { label: "Immigration, migration, and city life", note: "" },
  4: { label: "The West and Native Americans", note: "Not part of this unit. It belongs with the Gilded Age and the West." },
  5: { label: "Race and Jim Crow after Reconstruction", note: "" },
  6: { label: "Progressive reform of government, business, and society", note: "" }
};
// Which topics each blueprint entry serves (editorial mapping, entry by entry).
window.HCG_BP_TOPIC = {
  1: [2, 3], 2: [6], 3: [6], 4: [6], 5: [1, 6], 6: [6], 7: [6], 8: [6],
  9: [6], 10: [6], 11: [6], 12: [6], 13: [6], 14: [5, 6], 15: [6]
};

// TPSP picker index: the Progressive Era sources in The Primary Source
// Project's library (50 audited sources) plus its premium DBQ. The TPSP
// app has no per-source deep link; /library?q=<title> opens the library
// pre-searched for that source, which is the closest address it has.
// bp holds conservative blueprint pre-tags (see the era build notes);
// most sources carry none and the teacher can tag them when adding.
window.HCG_TPSP_PE = [
 {
  "id": "dbq-progressive-era-promises",
  "title": "Progressive Era Promises",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true
 },
 {
  "id": "beveridge-march-of-the-flag",
  "title": "March of the Flag",
  "type": "Speech",
  "meta": "Albert J. Beveridge · 1898",
  "url": "https://tpsp.web.app/library?q=March%20of%20the%20Flag"
 },
 {
  "id": "gillam-remember-the-maine-1898",
  "title": "\"Remember the Maine! And Don't Forget the Starving Cubans!\" (cartoon)",
  "type": "Political cartoon",
  "meta": "Victor Gillam · 1898",
  "url": "https://tpsp.web.app/library?q=%22Remember%20the%20Maine%21%20And%20Don%27t%20Forget%20the%20Starving%20Cubans%21%22%20%28cartoon%29"
 },
 {
  "id": "harpers-weekly-remember-the-maine-1898",
  "title": "\"Remember the Maine,\" 1898 (Harper's Weekly)",
  "type": "Newspaper",
  "meta": "Harper's Weekly · 1898",
  "url": "https://tpsp.web.app/library?q=%22Remember%20the%20Maine%2C%22%201898%20%28Harper%27s%20Weekly%29"
 },
 {
  "id": "our-victorious-fleets-1898",
  "title": "Our Victorious Fleets in Cuban Waters, 1898 (Currier & Ives)",
  "type": "Illustration",
  "meta": "Currier & Ives · 1898",
  "url": "https://tpsp.web.app/library?q=Our%20Victorious%20Fleets%20in%20Cuban%20Waters%2C%201898%20%28Currier%20%26%20Ives%29"
 },
 {
  "id": "anti-imperialist-league-platform",
  "title": "American Anti-Imperialist League Platform",
  "type": "Platform",
  "meta": "American Anti-Imperialist League · 1899",
  "url": "https://tpsp.web.app/library?q=American%20Anti-Imperialist%20League%20Platform"
 },
 {
  "id": "to-the-colored-men-of-voting-age-1900",
  "title": "\"To the Colored Men of Voting Age in the Southern States\"",
  "type": "Pamphlet",
  "meta": "Unknown · ca. 1901",
  "url": "https://tpsp.web.app/library?q=%22To%20the%20Colored%20Men%20of%20Voting%20Age%20in%20the%20Southern%20States%22",
  "bp": [
   14
  ]
 },
 {
  "id": "jim-crow-car-poem-1900",
  "title": "\"The 'Jim Crow' Car,\" Richmond Planet, September 15, 1900",
  "type": "Newspaper",
  "meta": "Rev. Walter H. Brooks · 1900",
  "url": "https://tpsp.web.app/library?q=%22The%20%27Jim%20Crow%27%20Car%2C%22%20Richmond%20Planet%2C%20September%2015%2C%201900",
  "bp": [
   14
  ]
 },
 {
  "id": "steerage-passengers-1900",
  "title": "\"Steerage Passengers Taking Life Easy on an Ocean Liner\"",
  "type": "Photograph",
  "meta": "Unknown · ca. 1905",
  "url": "https://tpsp.web.app/library?q=%22Steerage%20Passengers%20Taking%20Life%20Easy%20on%20an%20Ocean%20Liner%22"
 },
 {
  "id": "goodbye-to-old-ireland-1900",
  "title": "\"Goodbye to old Ireland\"",
  "type": "Photograph",
  "meta": "Unknown · ca. 1903",
  "url": "https://tpsp.web.app/library?q=%22Goodbye%20to%20old%20Ireland%22"
 },
 {
  "id": "susan-b-anthony-letter-1901",
  "title": "Susan B. Anthony on Suffrage and Equal Rights, 1901",
  "type": "Letter",
  "meta": "Susan B. Anthony · 1901",
  "url": "https://tpsp.web.app/library?q=Susan%20B.%20Anthony%20on%20Suffrage%20and%20Equal%20Rights%2C%201901",
  "bp": [
   12
  ]
 },
 {
  "id": "souls-of-black-folk-1903",
  "title": "The Souls of Black Folk (excerpt)",
  "type": "Narrative",
  "meta": "W.E.B. Du Bois · 1903",
  "url": "https://tpsp.web.app/library?q=The%20Souls%20of%20Black%20Folk%20%28excerpt%29",
  "bp": [
   14
  ]
 },
 {
  "id": "sinclair-the-jungle-1906",
  "title": "The Jungle (excerpt)",
  "type": "Narrative",
  "meta": "Upton Sinclair · 1906",
  "url": "https://tpsp.web.app/library?q=The%20Jungle%20%28excerpt%29",
  "bp": [
   2,
   6
  ]
 },
 {
  "id": "cowen-report-1906",
  "title": "Cowen Report on Jewish Immigration (excerpt)",
  "type": "Government document",
  "meta": "Philip Cowen · 1906",
  "url": "https://tpsp.web.app/library?q=Cowen%20Report%20on%20Jewish%20Immigration%20%28excerpt%29"
 },
 {
  "id": "sixteenth-amendment-1909",
  "title": "Sixteenth Amendment",
  "type": "Government document",
  "meta": "U.S. Congress · 1909-1913",
  "url": "https://tpsp.web.app/library?q=Sixteenth%20Amendment",
  "bp": [
   11
  ]
 },
 {
  "id": "protest-against-child-labor-1909",
  "title": "\"Protest against child labor in a labor parade\" - two girls with 'Abolish Child Slavery' banners, May 1, 1909",
  "type": "Photograph",
  "meta": "Bain News Service · 1909",
  "url": "https://tpsp.web.app/library?q=%22Protest%20against%20child%20labor%20in%20a%20labor%20parade%22%20-%20two%20girls%20with%20%27Abolish%20Child%20Slavery%27%20banners%2C%20May%201%2C%201909",
  "bp": [
   1
  ]
 },
 {
  "id": "child-labor-canning-maryland-1909",
  "title": "\"Child Labor in the Canning Industry of Maryland\" (1909)",
  "type": "Photograph",
  "meta": "Lewis Hine · 1909",
  "url": "https://tpsp.web.app/library?q=%22Child%20Labor%20in%20the%20Canning%20Industry%20of%20Maryland%22%20%281909%29",
  "bp": [
   1
  ]
 },
 {
  "id": "election-day-cartoon-1909",
  "title": "\"Election Day!\"",
  "type": "Political cartoon",
  "meta": "E. W. Gustin · 1909",
  "url": "https://tpsp.web.app/library?q=%22Election%20Day%21%22"
 },
 {
  "id": "addams-hull-house-1910",
  "title": "Twenty Years at Hull-House (excerpt)",
  "type": "Narrative",
  "meta": "Jane Addams · 1910",
  "url": "https://tpsp.web.app/library?q=Twenty%20Years%20at%20Hull-House%20%28excerpt%29"
 },
 {
  "id": "roosevelt-man-in-the-arena-1910",
  "title": "\"The Man in the Arena\" (excerpt)",
  "type": "Speech",
  "meta": "Theodore Roosevelt · 1910",
  "url": "https://tpsp.web.app/library?q=%22The%20Man%20in%20the%20Arena%22%20%28excerpt%29"
 },
 {
  "id": "breaker-boys-1911",
  "title": "\"Breaker boys, Pennsylvania coal mine\"",
  "type": "Photograph",
  "meta": "Lewis Hine · January 1911",
  "url": "https://tpsp.web.app/library?q=%22Breaker%20boys%2C%20Pennsylvania%20coal%20mine%22",
  "bp": [
   1
  ]
 },
 {
  "id": "angel-island-immigration-station-1910",
  "title": "\"Immigration Station, Angel Island, Cal.\"",
  "type": "Photograph",
  "meta": "J. D. Givens · ca. 1915",
  "url": "https://tpsp.web.app/library?q=%22Immigration%20Station%2C%20Angel%20Island%2C%20Cal.%22"
 },
 {
  "id": "triangle-fire-escape-1911",
  "title": "Damaged Fire Escape, Triangle Shirtwaist Company",
  "type": "Photograph",
  "meta": "Brown Brothers · 1911",
  "url": "https://tpsp.web.app/library?q=Damaged%20Fire%20Escape%2C%20Triangle%20Shirtwaist%20Company",
  "bp": [
   1
  ]
 },
 {
  "id": "suffrage-parade-photo-1913",
  "title": "Suffrage Parade Photograph",
  "type": "Photograph",
  "meta": "Bain News Service (George Grantham Bain Collection; individual photographer unknown) · 1913",
  "url": "https://tpsp.web.app/library?q=Suffrage%20Parade%20Photograph",
  "bp": [
   12
  ]
 },
 {
  "id": "jim-crow-airship-cartoon-1913",
  "title": "Airship with \"Jim Crow\" trailer",
  "type": "Political cartoon",
  "meta": "Unknown · 1913",
  "url": "https://tpsp.web.app/library?q=Airship%20with%20%22Jim%20Crow%22%20trailer",
  "bp": [
   14
  ]
 },
 {
  "id": "suffrage-procession-program-1913",
  "title": "Official program - Woman suffrage procession, Washington, D.C. March 3, 1913",
  "type": "Pamphlet",
  "meta": "Benjamin M. Dale · 1913",
  "url": "https://tpsp.web.app/library?q=Official%20program%20-%20Woman%20suffrage%20procession%2C%20Washington%2C%20D.C.%20March%203%2C%201913",
  "bp": [
   12
  ]
 },
 {
  "id": "ellis-island-eye-exam-1913",
  "title": "\"U.S. inspectors examining eyes of immigrants, Ellis Island\" (c. 1913)",
  "type": "Photograph",
  "meta": "Underwood & Underwood · ca. 1913",
  "url": "https://tpsp.web.app/library?q=%22U.S.%20inspectors%20examining%20eyes%20of%20immigrants%2C%20Ellis%20Island%22%20%28c.%201913%29"
 },
 {
  "id": "ellis-island-view-1913",
  "title": "\"View of Ellis Island, N.Y.\" (c. 1913)",
  "type": "Photograph",
  "meta": "Unknown · ca. 1913",
  "url": "https://tpsp.web.app/library?q=%22View%20of%20Ellis%20Island%2C%20N.Y.%22%20%28c.%201913%29"
 },
 {
  "id": "anti-suffrage-headquarters-photo-1914",
  "title": "\"National Anti-Suffrage Association\"",
  "type": "Photograph",
  "meta": "Unknown · 1914",
  "url": "https://tpsp.web.app/library?q=%22National%20Anti-Suffrage%20Association%22",
  "bp": [
   13
  ]
 },
 {
  "id": "awful-blot-cartoon-1914",
  "title": "\"An Awful Blot\" (anti-child-labor cartoon, ca. 1914)",
  "type": "Political cartoon",
  "meta": "Lewis W. Hine (attributed) · ca. 1914",
  "url": "https://tpsp.web.app/library?q=%22An%20Awful%20Blot%22%20%28anti-child-labor%20cartoon%2C%20ca.%201914%29"
 },
 {
  "id": "awakening-suffrage-1915",
  "title": "The Awakening",
  "type": "Poster",
  "meta": "Henry \"Hy\" Mayer · 1915",
  "url": "https://tpsp.web.app/library?q=The%20Awakening",
  "bp": [
   12
  ]
 },
 {
  "id": "birth-of-a-nation-poster-1915",
  "title": "Movie poster for The Birth of a Nation",
  "type": "Poster",
  "meta": "Elliot & Sherman Film Corp. · 1915",
  "url": "https://tpsp.web.app/library?q=Movie%20poster%20for%20The%20Birth%20of%20a%20Nation",
  "bp": [
   14
  ]
 },
 {
  "id": "jim-crow-law-letter-1915",
  "title": "\"Wants 'Jim Crow' Law All Over the United States,\" Washington Times, February 22, 1915 (excerpt)",
  "type": "Newspaper",
  "meta": "W. W. J. · 1915",
  "url": "https://tpsp.web.app/library?q=%22Wants%20%27Jim%20Crow%27%20Law%20All%20Over%20the%20United%20States%2C%22%20Washington%20Times%2C%20February%2022%2C%201915%20%28excerpt%29",
  "bp": [
   14
  ]
 },
 {
  "id": "americanese-wall-1916",
  "title": "\"The Americanese wall\" (cartoon)",
  "type": "Political cartoon",
  "meta": "Raymond O. Evans · 1916",
  "url": "https://tpsp.web.app/library?q=%22The%20Americanese%20wall%22%20%28cartoon%29"
 },
 {
  "id": "keating-owen-child-labor-act-1916",
  "title": "Keating-Owen Child Labor Act (excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress · 1916",
  "url": "https://tpsp.web.app/library?q=Keating-Owen%20Child%20Labor%20Act%20%28excerpt%29"
 },
 {
  "id": "negro-exodus-article-1916",
  "title": "\"South Unable to Put Stop to Negro Exodus,\" Washington Times, October 23, 1916 (excerpt)",
  "type": "Newspaper",
  "meta": "Unknown · 1916",
  "url": "https://tpsp.web.app/library?q=%22South%20Unable%20to%20Put%20Stop%20to%20Negro%20Exodus%2C%22%20Washington%20Times%2C%20October%2023%2C%201916%20%28excerpt%29"
 },
 {
  "id": "zimmermann-telegram",
  "title": "Zimmermann Telegram (full text)",
  "type": "Government document",
  "meta": "Arthur Zimmermann · 1917",
  "url": "https://tpsp.web.app/library?q=Zimmermann%20Telegram%20%28full%20text%29"
 },
 {
  "id": "wilson-war-message-1917",
  "title": "War Message to Congress",
  "type": "Speech",
  "meta": "Woodrow Wilson · 1917",
  "url": "https://tpsp.web.app/library?q=War%20Message%20to%20Congress"
 },
 {
  "id": "flagg-i-want-you-1917",
  "title": "\"I Want You for U.S. Army\" (poster)",
  "type": "Poster",
  "meta": "James Montgomery Flagg · 1917",
  "url": "https://tpsp.web.app/library?q=%22I%20Want%20You%20for%20U.S.%20Army%22%20%28poster%29"
 },
 {
  "id": "hopps-destroy-this-mad-brute-1917",
  "title": "\"Destroy This Mad Brute\" (poster)",
  "type": "Poster",
  "meta": "Harry R. Hopps · 1917",
  "url": "https://tpsp.web.app/library?q=%22Destroy%20This%20Mad%20Brute%22%20%28poster%29"
 },
 {
  "id": "fourteen-points",
  "title": "Fourteen Points",
  "type": "Speech",
  "meta": "Woodrow Wilson · 1918",
  "url": "https://tpsp.web.app/library?q=Fourteen%20Points"
 },
 {
  "id": "hoover-memo-ridgely-1919",
  "title": "Memorandum to Special Agent Ridgely",
  "type": "Government document",
  "meta": "J. Edgar Hoover · 1919",
  "url": "https://tpsp.web.app/library?q=Memorandum%20to%20Special%20Agent%20Ridgely"
 },
 {
  "id": "nineteenth-amendment-1919",
  "title": "Nineteenth Amendment",
  "type": "Government document",
  "meta": "U.S. Congress · 1919-1920",
  "url": "https://tpsp.web.app/library?q=Nineteenth%20Amendment",
  "bp": [
   12
  ]
 },
 {
  "id": "treaty-of-versailles-1919",
  "title": "Treaty of Versailles, 1919 (Articles 231-233, excerpt)",
  "type": "Government document",
  "meta": "Paris Peace Conference (Allied and Associated Powers) · 1919",
  "url": "https://tpsp.web.app/library?q=Treaty%20of%20Versailles%2C%201919%20%28Articles%20231-233%2C%20excerpt%29"
 },
 {
  "id": "scott-negro-migration-1920",
  "title": "\"Negro Migration During the War\" (1920) (excerpt)",
  "type": "Government document",
  "meta": "Emmett J. Scott · 1920",
  "url": "https://tpsp.web.app/library?q=%22Negro%20Migration%20During%20the%20War%22%20%281920%29%20%28excerpt%29"
 },
 {
  "id": "volstead-act-1919",
  "title": "National Prohibition Act (Volstead Act, excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress · 1919",
  "url": "https://tpsp.web.app/library?q=National%20Prohibition%20Act%20%28Volstead%20Act%2C%20excerpt%29",
  "bp": [
   15
  ]
 },
 {
  "id": "eighteenth-amendment-1919",
  "title": "The Eighteenth Amendment",
  "type": "Government document",
  "meta": "U.S. Congress · 1919",
  "url": "https://tpsp.web.app/library?q=The%20Eighteenth%20Amendment",
  "bp": [
   15
  ]
 },
 {
  "id": "niagara-movement-declaration-1905",
  "title": "Declaration of Principles of the Niagara Movement (excerpt)",
  "type": "Platform",
  "meta": "W.E.B. Du Bois · 1905",
  "url": "https://tpsp.web.app/library?q=Declaration%20of%20Principles%20of%20the%20Niagara%20Movement%20%28excerpt%29",
  "bp": [
   14
  ]
 },
 {
  "id": "pure-food-and-drug-act-1906",
  "title": "The Pure Food and Drug Act (excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress · 1906",
  "url": "https://tpsp.web.app/library?q=The%20Pure%20Food%20and%20Drug%20Act%20%28excerpt%29",
  "bp": [
   6
  ]
 },
 {
  "id": "roosevelt-new-nationalism-1910",
  "title": "\"The New Nationalism\" (excerpt)",
  "type": "Speech",
  "meta": "Theodore Roosevelt · 1910",
  "url": "https://tpsp.web.app/library?q=%22The%20New%20Nationalism%22%20%28excerpt%29"
 },
 {
  "id": "seventeenth-amendment-1913",
  "title": "The Seventeenth Amendment",
  "type": "Government document",
  "meta": "U.S. Congress · 1913",
  "url": "https://tpsp.web.app/library?q=The%20Seventeenth%20Amendment",
  "bp": [
   4
  ]
 }
];

// ---------------------------------------------------------------------
// The Gilded Age: second plannable unit. Item tags, names, and files
// come from gilded-age/unit-manifest.md and gilded-age-skeleton.md.
// Files live in Firebase Storage under hcg/gilded-age/ (All-Access);
// items carry the Storage path in `storage`, never a public URL.
window.HCG_GA_BLUEPRINT = {
  1: "Railroads and the making of a national market",
  2: "Steel, oil, invention, and industrial scale",
  3: "Trusts, monopoly, and the Sherman Antitrust Act",
  4: "Laissez-faire, Social Darwinism, and their critics",
  5: "Industrial work, wages, and child labor",
  6: "Unions and the great strikes: Haymarket, Homestead, and Pullman",
  7: "New immigration, Ellis Island, Angel Island, and restriction",
  8: "Urban growth, tenements, sanitation, and daily life",
  9: "Political machines, graft, and early city reform",
  10: "Mining, cattle, farming, and the commercial West",
  11: "Native American dispossession, the Dawes Act, assimilation, and Wounded Knee",
  12: "Jim Crow, Plessy v. Ferguson, and disfranchisement",
  13: "Black protest and leadership: Ida B. Wells and Booker T. Washington",
  14: "Farmers' grievances, Granger laws, and Populism",
  15: "Free silver, Bryan, the election of 1896, and the road to Progressivism"
};

window.HCG_GA_LESSONS = [
  { n: 1, title: "The Engines of Industry", question: "Why did railroads become the engine of a national industrial economy?" },
  { n: 2, title: "Big Business and Its Critics", question: "Did big business build modern America, capture it, or do both at once?" },
  { n: 3, title: "The Workers' World", question: "Why did workers organize, and why did collective action so often end in defeat?" },
  { n: 4, title: "The New Immigration", question: "Who were the new immigrants, and how did the United States decide who belonged?" },
  { n: 5, title: "The City", question: "How did rapid urban growth change daily life, health, and city government?" },
  { n: 6, title: "The West", question: "How did railroads and federal land policy remake the West?" },
  { n: 7, title: "Native Americans and the Closing Frontier", question: "Why did the United States pursue assimilation, and what did Native peoples lose, resist, and preserve?" },
  { n: 8, title: "Race, Politics, and Protest", question: "How did Jim Crow and economic protest shape the politics that Progressives inherited?" },
];

window.HCG_GA_ITEMS = [
  // Lesson 1
  { id: "g1-reading", lesson: 1, kind: "Reading", name: "The Engines of Industry", days: 1, tags: [1, 2], storage: "hcg/gilded-age/lesson-01-reading.pdf", core: true },
  { id: "g1-notes", lesson: 1, kind: "Guided Notes", name: "Lesson 1 guided notes", days: 0, tags: [1, 2], storage: "hcg/gilded-age/lesson-01-guided-notes.pdf", core: true },
  { id: "g1-activity", lesson: 1, kind: "Activity", name: "Network map stations", days: 1, tags: [1, 2], storage: "hcg/gilded-age/lesson-01-activity.pdf", core: true },
  { id: "g1-notebook", lesson: 1, kind: "Notebook", name: "The five-part system chart", days: 0.5, tags: [1, 2], storage: "hcg/gilded-age/lesson-01-notebook.pdf" },
  { id: "g1-quick", lesson: 1, kind: "Quick Check", name: "The Promontory photograph", days: 0.5, tags: [1, 2], storage: "hcg/gilded-age/lesson-01-quick-check.pdf" },
  { id: "g1-writing", lesson: 1, kind: "Writing", name: "Essay, why railroads became the engine", days: 1, tags: [1, 2], storage: "hcg/gilded-age/lesson-01-writing.pdf" },
  // Lesson 2
  { id: "g2-reading", lesson: 2, kind: "Reading", name: "Big Business and Its Critics", days: 1, tags: [3, 4], storage: "hcg/gilded-age/lesson-02-reading.pdf", core: true },
  { id: "g2-notes", lesson: 2, kind: "Guided Notes", name: "Lesson 2 guided notes", days: 0, tags: [3, 4], storage: "hcg/gilded-age/lesson-02-guided-notes.pdf", core: true },
  { id: "g2-activity", lesson: 2, kind: "Activity", name: "Trust hearing simulation", days: 1, tags: [3, 4], storage: "hcg/gilded-age/lesson-02-activity.pdf", core: true },
  { id: "g2-notebook", lesson: 2, kind: "Notebook", name: "Integration and ideas organizer", days: 0.5, tags: [3, 4], storage: "hcg/gilded-age/lesson-02-notebook.pdf" },
  { id: "g2-quick", lesson: 2, kind: "Quick Check", name: "Political cartoon on the trusts", days: 0.5, tags: [3, 4], storage: "hcg/gilded-age/lesson-02-quick-check.pdf" },
  { id: "g2-writing", lesson: 2, kind: "Writing", name: "Paragraph, build, capture, or both", days: 1, tags: [3, 4], storage: "hcg/gilded-age/lesson-02-writing.pdf" },
  // Lesson 3
  { id: "g3-reading", lesson: 3, kind: "Reading", name: "The Workers' World", days: 1, tags: [5, 6], storage: "hcg/gilded-age/lesson-03-reading.pdf", core: true },
  { id: "g3-notes", lesson: 3, kind: "Guided Notes", name: "Lesson 3 guided notes", days: 0, tags: [5, 6], storage: "hcg/gilded-age/lesson-03-guided-notes.pdf", core: true },
  { id: "g3-activity", lesson: 3, kind: "Activity", name: "Strike evidence stations", days: 1, tags: [5, 6], storage: "hcg/gilded-age/lesson-03-activity.pdf", core: true },
  { id: "g3-notebook", lesson: 3, kind: "Notebook", name: "The three strikes chart", days: 0.5, tags: [5, 6], storage: "hcg/gilded-age/lesson-03-notebook.pdf" },
  { id: "g3-quick", lesson: 3, kind: "Quick Check", name: "The Hine spinner photograph", days: 0.5, tags: [5], storage: "hcg/gilded-age/lesson-03-quick-check.pdf" },
  { id: "g3-writing", lesson: 3, kind: "Writing", name: "Argument essay, why the strikes failed", days: 1, tags: [6], storage: "hcg/gilded-age/lesson-03-writing.pdf" },
  // Lesson 4
  { id: "g4-reading", lesson: 4, kind: "Reading", name: "The New Immigration", days: 1, tags: [7], storage: "hcg/gilded-age/lesson-04-reading.pdf", core: true },
  { id: "g4-notes", lesson: 4, kind: "Guided Notes", name: "Lesson 4 guided notes", days: 0, tags: [7], storage: "hcg/gilded-age/lesson-04-guided-notes.pdf", core: true },
  { id: "g4-activity", lesson: 4, kind: "Activity", name: "Arrival record jigsaw", days: 1, tags: [7], storage: "hcg/gilded-age/lesson-04-activity.pdf", core: true },
  { id: "g4-notebook", lesson: 4, kind: "Notebook", name: "Three arrival routes chart", days: 0.5, tags: [7], storage: "hcg/gilded-age/lesson-04-notebook.pdf" },
  { id: "g4-quick", lesson: 4, kind: "Quick Check", name: "The Angel Island photograph", days: 0.5, tags: [7], storage: "hcg/gilded-age/lesson-04-quick-check.pdf" },
  { id: "g4-writing", lesson: 4, kind: "Writing", name: "Essay, who decided who belonged", days: 1, tags: [7], storage: "hcg/gilded-age/lesson-04-writing.pdf" },
  // Lesson 5
  { id: "g5-reading", lesson: 5, kind: "Reading", name: "The City", days: 1, tags: [8, 9], storage: "hcg/gilded-age/lesson-05-reading.pdf", core: true },
  { id: "g5-notes", lesson: 5, kind: "Guided Notes", name: "Lesson 5 guided notes", days: 0, tags: [8, 9], storage: "hcg/gilded-age/lesson-05-guided-notes.pdf", core: true },
  { id: "g5-activity", lesson: 5, kind: "Activity", name: "City systems stations", days: 1, tags: [8, 9], storage: "hcg/gilded-age/lesson-05-activity.pdf", core: true },
  { id: "g5-notebook", lesson: 5, kind: "Notebook", name: "The four systems organizer", days: 0.5, tags: [8, 9], storage: "hcg/gilded-age/lesson-05-notebook.pdf" },
  { id: "g5-quick", lesson: 5, kind: "Quick Check", name: "The Mulberry Street photograph", days: 0.5, tags: [8, 9], storage: "hcg/gilded-age/lesson-05-quick-check.pdf" },
  { id: "g5-writing", lesson: 5, kind: "Writing", name: "The machine judged by its street", days: 1, tags: [8, 9], storage: "hcg/gilded-age/lesson-05-writing.pdf" },
  // Lesson 6
  { id: "g6-reading", lesson: 6, kind: "Reading", name: "The West", days: 1, tags: [10], storage: "hcg/gilded-age/lesson-06-reading.pdf", core: true },
  { id: "g6-notes", lesson: 6, kind: "Guided Notes", name: "Lesson 6 guided notes", days: 0, tags: [10], storage: "hcg/gilded-age/lesson-06-guided-notes.pdf", core: true },
  { id: "g6-activity", lesson: 6, kind: "Activity", name: "Land claim map exercise", days: 1, tags: [10], storage: "hcg/gilded-age/lesson-06-activity.pdf", core: true },
  { id: "g6-notebook", lesson: 6, kind: "Notebook", name: "Mining, cattle, farming, and railroads chart", days: 0.5, tags: [10], storage: "hcg/gilded-age/lesson-06-notebook.pdf" },
  { id: "g6-quick", lesson: 6, kind: "Quick Check", name: "The 1888 branding photograph", days: 0.5, tags: [10], storage: "hcg/gilded-age/lesson-06-quick-check.pdf" },
  { id: "g6-writing", lesson: 6, kind: "Writing", name: "Paragraph, how policy remade the West", days: 1, tags: [10], storage: "hcg/gilded-age/lesson-06-writing.pdf" },
  // Lesson 7
  { id: "g7-reading", lesson: 7, kind: "Reading", name: "Native Americans and the Closing Frontier", days: 1, tags: [11], storage: "hcg/gilded-age/lesson-07-reading.pdf", core: true },
  { id: "g7-notes", lesson: 7, kind: "Guided Notes", name: "Lesson 7 guided notes", days: 0, tags: [11], storage: "hcg/gilded-age/lesson-07-guided-notes.pdf", core: true },
  { id: "g7-activity", lesson: 7, kind: "Activity", name: "Policy and consequence stations", days: 1, tags: [11], storage: "hcg/gilded-age/lesson-07-activity.pdf", core: true },
  { id: "g7-notebook", lesson: 7, kind: "Notebook", name: "Goal, outcome, and response organizer", days: 0.5, tags: [11], storage: "hcg/gilded-age/lesson-07-notebook.pdf" },
  { id: "g7-quick", lesson: 7, kind: "Quick Check", name: "The Tom Torlino portraits", days: 0.5, tags: [11], storage: "hcg/gilded-age/lesson-07-quick-check.pdf" },
  { id: "g7-writing", lesson: 7, kind: "Writing", name: "Paragraph, help, harm, or both", days: 1, tags: [11], storage: "hcg/gilded-age/lesson-07-writing.pdf" },
  // Lesson 8
  { id: "g8-reading", lesson: 8, kind: "Reading", name: "Race, Politics, and Protest", days: 1, tags: [12, 13, 14, 15], storage: "hcg/gilded-age/lesson-08-reading.pdf", core: true },
  { id: "g8-notes", lesson: 8, kind: "Guided Notes", name: "Lesson 8 guided notes", days: 0, tags: [12, 13, 14, 15], storage: "hcg/gilded-age/lesson-08-guided-notes.pdf", core: true },
  { id: "g8-activity", lesson: 8, kind: "Activity", name: "Two-front protest jigsaw", days: 1, tags: [12, 13, 14, 15], storage: "hcg/gilded-age/lesson-08-activity.pdf", core: true },
  { id: "g8-notebook", lesson: 8, kind: "Notebook", name: "Four-part organizer with the election of 1896", days: 0.5, tags: [12, 13, 14, 15], storage: "hcg/gilded-age/lesson-08-notebook.pdf" },
  { id: "g8-quick", lesson: 8, kind: "Quick Check", name: "The segregation photograph", days: 0.5, tags: [12, 13, 14, 15], storage: "hcg/gilded-age/lesson-08-quick-check.pdf" },
  { id: "g8-writing", lesson: 8, kind: "Writing", name: "Essay, which front left the deeper mark", days: 1, tags: [12, 13, 14, 15], storage: "hcg/gilded-age/lesson-08-writing.pdf" },
  // Review day
  { id: "grev-guide", lesson: 9, kind: "Review", name: "Study guide (review day)", days: 1, tags: [], storage: "hcg/gilded-age/review-study-guide.pdf", core: true },
  { id: "grev-cross", lesson: 9, kind: "Review", name: "Crossword (36 answers)", days: 0.5, tags: [], storage: "hcg/gilded-age/review-crossword.pdf" },
];

window.HCG_GA_TOPICS = {
  1: { label: "Industrial growth and big business", note: "" },
  2: { label: "Labor and the working class", note: "" },
  3: { label: "Immigration, migration, and city life", note: "" },
  4: { label: "The West and Native Americans", note: "" },
  5: { label: "Race and Jim Crow after Reconstruction", note: "" },
  6: { label: "Politics, corruption, and protest", note: "" }
};
window.HCG_GA_BP_TOPIC = {
  1: [1], 2: [1], 3: [1, 6], 4: [1, 6], 5: [2], 6: [2, 6], 7: [3], 8: [3], 9: [3, 6], 10: [4], 11: [4, 5], 12: [5, 6], 13: [5, 6], 14: [4, 6], 15: [6]
};

// TPSP picker index for the Gilded Age, generated from the TPSP era
// file the same way as the Progressive Era list: era sources in file
// order (Audio excluded), plus the premium DBQs whose TPSP era is
// "The Gilded Age" (dbq10 and dbq16). Pre-tags are conservative:
// a source is tagged only where it names the blueprint entry.
window.HCG_TPSP_GA = [
 {
  "id": "dbq10-industrialization-american-life",
  "title": "Did Industrialization Improve American Life?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true
 },
 {
  "id": "dbq16-west-opportunity",
  "title": "For Whom Was the West a Land of Opportunity?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true
 },
 {
  "id": "nast-boss-tweed-1871",
  "title": "\"As long as I count the Votes, what are you going to do about it?\"",
  "type": "Political cartoon",
  "meta": "Thomas Nast · 1871",
  "url": "https://tpsp.web.app/library?q=%22As%20long%20as%20I%20count%20the%20Votes%2C%20what%20are%20you%20going%20to%20do%20about%20it%3F%22",
  "bp": [
   9
  ]
 },
 {
  "id": "american-progress-1872",
  "title": "American Progress",
  "type": "Painting",
  "meta": "John Gast · 1872",
  "url": "https://tpsp.web.app/library?q=American%20Progress"
 },
 {
  "id": "great-railroad-strike-1877-illustration",
  "title": "The Great Railroad Strike of July 1877",
  "type": "Illustration",
  "meta": "Unknown · 1877",
  "url": "https://tpsp.web.app/library?q=The%20Great%20Railroad%20Strike%20of%20July%201877"
 },
 {
  "id": "indian-territory-homestead-poster-1880s",
  "title": "Poster Advertising \"Indian Territory That Garden of the World, Open for Homestead and Pre-Emption\"",
  "type": "Poster",
  "meta": "Unknown railroad advertiser · 1889",
  "url": "https://tpsp.web.app/library?q=Poster%20Advertising%20%22Indian%20Territory%20That%20Garden%20of%20the%20World%2C%20Open%20for%20Homestead%20and%20Pre-Emption%22"
 },
 {
  "id": "chinese-invasion-cartoon-1880s",
  "title": "The Chinese Invasion (cartoon)",
  "type": "Political cartoon",
  "meta": "Joseph Keppler · 1880",
  "url": "https://tpsp.web.app/library?q=The%20Chinese%20Invasion%20%28cartoon%29",
  "bp": [
   7
  ]
 },
 {
  "id": "chinese-exclusion-act-1882",
  "title": "Chinese Exclusion Act (excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress · 1882",
  "url": "https://tpsp.web.app/library?q=Chinese%20Exclusion%20Act%20%28excerpt%29",
  "bp": [
   7
  ]
 },
 {
  "id": "dawes-act-1887",
  "title": "Dawes Act of 1887 (excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress · 1887",
  "url": "https://tpsp.web.app/library?q=Dawes%20Act%20of%201887%20%28excerpt%29",
  "bp": [
   11
  ]
 },
 {
  "id": "carnegie-gospel-of-wealth-1889",
  "title": "\"The Gospel of Wealth\" (excerpt)",
  "type": "Narrative",
  "meta": "Andrew Carnegie · 1889",
  "url": "https://tpsp.web.app/library?q=%22The%20Gospel%20of%20Wealth%22%20%28excerpt%29",
  "bp": [
   4
  ]
 },
 {
  "id": "colored-population-map-1890",
  "title": "Distribution of the Colored Population of the United States: 1890",
  "type": "Map",
  "meta": "U.S. Census Office · 1898",
  "url": "https://tpsp.web.app/library?q=Distribution%20of%20the%20Colored%20Population%20of%20the%20United%20States%3A%201890"
 },
 {
  "id": "omaha-platform-1892",
  "title": "Omaha Platform (excerpt)",
  "type": "Platform",
  "meta": "People's Party · 1892",
  "url": "https://tpsp.web.app/library?q=Omaha%20Platform%20%28excerpt%29",
  "bp": [
   14
  ]
 },
 {
  "id": "homestead-riot-1892",
  "title": "The Homestead Riot",
  "type": "Illustration",
  "meta": "W. P. Snyder (after a photograph by Dabbs) · 1892",
  "url": "https://tpsp.web.app/library?q=The%20Homestead%20Riot",
  "bp": [
   6
  ]
 },
 {
  "id": "columbus-day-proclamation-1892",
  "title": "Proclamation 335 (Columbus Day proclamation)",
  "type": "Government document",
  "meta": "President Benjamin Harrison · 1892",
  "url": "https://tpsp.web.app/library?q=Proclamation%20335%20%28Columbus%20Day%20proclamation%29"
 },
 {
  "id": "washington-atlanta-compromise-1895",
  "title": "Atlanta Compromise Speech (excerpt)",
  "type": "Speech",
  "meta": "Booker T. Washington · 1895",
  "url": "https://tpsp.web.app/library?q=Atlanta%20Compromise%20Speech%20%28excerpt%29",
  "bp": [
   13
  ]
 },
 {
  "id": "bryan-cross-of-gold-1896",
  "title": "\"Cross of Gold\" Speech (excerpt)",
  "type": "Speech",
  "meta": "William Jennings Bryan · 1896",
  "url": "https://tpsp.web.app/library?q=%22Cross%20of%20Gold%22%20Speech%20%28excerpt%29",
  "bp": [
   15
  ]
 },
 {
  "id": "plessy-v-ferguson-judgment-1896",
  "title": "Judgment in Plessy v. Ferguson (excerpt)",
  "type": "Court decision",
  "meta": "U.S. Supreme Court · 1896",
  "url": "https://tpsp.web.app/library?q=Judgment%20in%20Plessy%20v.%20Ferguson%20%28excerpt%29",
  "bp": [
   12
  ]
 },
 {
  "id": "sherman-antitrust-act-1890",
  "title": "Sherman Antitrust Act (excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress · 1890",
  "url": "https://tpsp.web.app/library?q=Sherman%20Antitrust%20Act%20%28excerpt%29",
  "bp": [
   3
  ]
 },
 {
  "id": "interstate-commerce-act-1887",
  "title": "Interstate Commerce Act (excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress · 1887",
  "url": "https://tpsp.web.app/library?q=Interstate%20Commerce%20Act%20%28excerpt%29",
  "bp": [
   1
  ]
 },
 {
  "id": "riis-how-the-other-half-lives-1890",
  "title": "How the Other Half Lives (excerpt)",
  "type": "Book",
  "meta": "Jacob A. Riis · 1890",
  "url": "https://tpsp.web.app/library?q=How%20the%20Other%20Half%20Lives%20%28excerpt%29",
  "bp": [
   8
  ]
 },
 {
  "id": "wells-southern-horrors-1892",
  "title": "Southern Horrors: Lynch Law in All Its Phases (excerpt)",
  "type": "Pamphlet",
  "meta": "Ida B. Wells-Barnett · 1892",
  "url": "https://tpsp.web.app/library?q=Southern%20Horrors%3A%20Lynch%20Law%20in%20All%20Its%20Phases%20%28excerpt%29",
  "bp": [
   13
  ]
 },
 {
  "id": "turner-frontier-thesis-1893",
  "title": "\"The Significance of the Frontier in American History\" (excerpt)",
  "type": "Other",
  "meta": "Frederick Jackson Turner · 1893",
  "url": "https://tpsp.web.app/library?q=%22The%20Significance%20of%20the%20Frontier%20in%20American%20History%22%20%28excerpt%29"
 },
 {
  "id": "chief-joseph-surrender-speech-1877",
  "title": "Surrender Speech (transcript)",
  "type": "Speech",
  "meta": "Chief Joseph · 1877",
  "url": "https://tpsp.web.app/library?q=Surrender%20Speech%20%28transcript%29",
  "bp": [
   11
  ]
 },
 {
  "id": "pendleton-civil-service-act-1883",
  "title": "Pendleton Civil Service Act (excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress · 1883",
  "url": "https://tpsp.web.app/library?q=Pendleton%20Civil%20Service%20Act%20%28excerpt%29"
 }
];

// ---------------------------------------------------------------------
// Imperialism and World War I: third plannable unit. Item tags, names,
// and files come from imperialism-wwi/unit-manifest.md and
// imperialism-wwi-skeleton.md. Files live in Firebase Storage under
// hcg/imperialism-wwi/ (All-Access); items carry the Storage path in
// `storage`, never a public URL.
window.HCG_WWI_BLUEPRINT = {
  1: "The causes of American expansion in the 1890s: markets, sea power, and ideas of mission",
  2: "The Spanish-American War: the Maine, the fighting, and the Treaty of Paris",
  3: "The Philippine question: the annexation debate, the Philippine-American War, and colonial rule",
  4: "The Open Door in China and the Boxer Rebellion",
  5: "Panama, the Roosevelt Corollary, and dollar diplomacy in Latin America",
  6: "The outbreak of war in Europe and American neutrality, 1914 to 1916",
  7: "The road to intervention: submarine warfare, the Zimmermann Telegram, and the declaration of war",
  8: "Mobilization: the draft, war production and finance, and the AEF",
  9: "Americans in combat: convoys, the trenches, St. Mihiel, the Meuse-Argonne, and the armistice",
  10: "The managed home front: bonds, production boards, and official persuasion",
  11: "Dissent, migration, and wartime change: the Espionage and Sedition Acts, the Great Migration, and women's war work",
  12: "The Fourteen Points and the Treaty of Versailles",
  13: "The League fight: Lodge, the reservations, and Senate rejection",
  14: "The troubled aftermath: the strikes, race violence, and Red Scare of 1919",
  15: "The election of 1920, normalcy, and the turn toward the Twenties"
};

window.HCG_WWI_LESSONS = [
  { n: 1, title: "The Turn Overseas", question: "Why did the United States look overseas for territory, markets, and influence in the 1890s?" },
  { n: 2, title: "The Spanish-American War", question: "Was the war with Spain fought to free Cuba, to take an empire, or both?" },
  { n: 3, title: "An Empire in the Philippines", question: "Did taking the Philippines extend American ideals or contradict them?" },
  { n: 4, title: "Open Doors and the Big Stick", question: "How did the United States project power in Asia and Latin America without ruling formal colonies there?" },
  { n: 5, title: "Neutrality Tested", question: "Why did the United States enter the First World War in 1917 after three years of declared neutrality?" },
  { n: 6, title: "Americans in the War", question: "How did the United States mobilize, and what did its soldiers meet in France?" },
  { n: 7, title: "The Home Front", question: "How did the war change American life at home, and who gained and who lost by the change?" },
  { n: 8, title: "Wilson's Peace and the Turn Inward", question: "Why did the United States refuse the League of Nations it had proposed, and what did the country turn toward in 1920?" }
];

window.HCG_WWI_ITEMS = [
  // Lesson 1
  { id: "w1-reading", lesson: 1, kind: "Reading", name: "The Turn Overseas", days: 1, tags: [1], storage: "hcg/imperialism-wwi/lesson-01-reading.pdf", core: true },
  { id: "w1-notes", lesson: 1, kind: "Guided Notes", name: "Lesson 1 guided notes", days: 0, tags: [1], storage: "hcg/imperialism-wwi/lesson-01-guided-notes.pdf", core: true },
  { id: "w1-activity", lesson: 1, kind: "Activity", name: "Motive Stations: The Turn Overseas", days: 1, tags: [1], storage: "hcg/imperialism-wwi/lesson-01-activity.pdf", core: true },
  { id: "w1-notebook", lesson: 1, kind: "Notebook", name: "Motive, claim, and evidence chart", days: 0.5, tags: [1], storage: "hcg/imperialism-wwi/lesson-01-notebook.pdf" },
  { id: "w1-quick", lesson: 1, kind: "Quick Check", name: "The Queen and the Argument", days: 0.5, tags: [1], storage: "hcg/imperialism-wwi/lesson-01-quick-check.pdf" },
  { id: "w1-writing", lesson: 1, kind: "Writing", name: "Essay, why the turn overseas", days: 1, tags: [1], storage: "hcg/imperialism-wwi/lesson-01-writing.pdf" },
  // Lesson 2
  { id: "w2-reading", lesson: 2, kind: "Reading", name: "The Spanish-American War", days: 1, tags: [2], storage: "hcg/imperialism-wwi/lesson-02-reading.pdf", core: true },
  { id: "w2-notes", lesson: 2, kind: "Guided Notes", name: "Lesson 2 guided notes", days: 0, tags: [2], storage: "hcg/imperialism-wwi/lesson-02-guided-notes.pdf", core: true },
  { id: "w2-activity", lesson: 2, kind: "Activity", name: "Headline and Evidence Lab: Free Cuba, Take an Empire, or Both?", days: 1, tags: [2], storage: "hcg/imperialism-wwi/lesson-02-activity.pdf", core: true },
  { id: "w2-notebook", lesson: 2, kind: "Notebook", name: "Stage chart, liberation and empire evidence", days: 0.5, tags: [2], storage: "hcg/imperialism-wwi/lesson-02-notebook.pdf" },
  { id: "w2-quick", lesson: 2, kind: "Quick Check", name: "Our Victorious Fleets", days: 0.5, tags: [2], storage: "hcg/imperialism-wwi/lesson-02-quick-check.pdf" },
  { id: "w2-writing", lesson: 2, kind: "Writing", name: "Paragraph, free Cuba, take an empire, or both", days: 1, tags: [2], storage: "hcg/imperialism-wwi/lesson-02-writing.pdf" },
  // Lesson 3
  { id: "w3-reading", lesson: 3, kind: "Reading", name: "An Empire in the Philippines", days: 1, tags: [3], storage: "hcg/imperialism-wwi/lesson-03-reading.pdf", core: true },
  { id: "w3-notes", lesson: 3, kind: "Guided Notes", name: "Lesson 3 guided notes", days: 0, tags: [3], storage: "hcg/imperialism-wwi/lesson-03-guided-notes.pdf", core: true },
  { id: "w3-activity", lesson: 3, kind: "Activity", name: "Annexation Debate Simulation: The Senate Question, 1899", days: 1, tags: [3], storage: "hcg/imperialism-wwi/lesson-03-activity.pdf", core: true },
  { id: "w3-notebook", lesson: 3, kind: "Notebook", name: "Stage chart, extend or contradict", days: 0.5, tags: [3], storage: "hcg/imperialism-wwi/lesson-03-notebook.pdf" },
  { id: "w3-quick", lesson: 3, kind: "Quick Check", name: "School Begins", days: 0.5, tags: [3], storage: "hcg/imperialism-wwi/lesson-03-quick-check.pdf" },
  { id: "w3-writing", lesson: 3, kind: "Writing", name: "Essay, extend or contradict", days: 1, tags: [3], storage: "hcg/imperialism-wwi/lesson-03-writing.pdf" },
  // Lesson 4
  { id: "w4-reading", lesson: 4, kind: "Reading", name: "Open Doors and the Big Stick", days: 1, tags: [4, 5], storage: "hcg/imperialism-wwi/lesson-04-reading.pdf", core: true },
  { id: "w4-notes", lesson: 4, kind: "Guided Notes", name: "Lesson 4 guided notes", days: 0, tags: [4, 5], storage: "hcg/imperialism-wwi/lesson-04-guided-notes.pdf", core: true },
  { id: "w4-activity", lesson: 4, kind: "Activity", name: "Instruments of Power Stations: Open Doors and the Big Stick", days: 1, tags: [4, 5], storage: "hcg/imperialism-wwi/lesson-04-activity.pdf", core: true },
  { id: "w4-notebook", lesson: 4, kind: "Notebook", name: "Instruments of power chart", days: 0.5, tags: [4, 5], storage: "hcg/imperialism-wwi/lesson-04-notebook.pdf" },
  { id: "w4-quick", lesson: 4, kind: "Quick Check", name: "The Big Stick in the Caribbean Sea", days: 0.5, tags: [4, 5], storage: "hcg/imperialism-wwi/lesson-04-quick-check.pdf" },
  { id: "w4-writing", lesson: 4, kind: "Writing", name: "Essay, power without colonies", days: 1, tags: [4, 5], storage: "hcg/imperialism-wwi/lesson-04-writing.pdf" },
  // Lesson 5
  { id: "w5-reading", lesson: 5, kind: "Reading", name: "Neutrality Tested", days: 1, tags: [6, 7], storage: "hcg/imperialism-wwi/lesson-05-reading.pdf", core: true },
  { id: "w5-notes", lesson: 5, kind: "Guided Notes", name: "Lesson 5 guided notes", days: 0, tags: [6, 7], storage: "hcg/imperialism-wwi/lesson-05-guided-notes.pdf", core: true },
  { id: "w5-activity", lesson: 5, kind: "Activity", name: "Chain to War: An Evidence Lab", days: 1, tags: [6, 7], storage: "hcg/imperialism-wwi/lesson-05-activity.pdf", core: true },
  { id: "w5-notebook", lesson: 5, kind: "Notebook", name: "The Chain to War", days: 0.5, tags: [6, 7], storage: "hcg/imperialism-wwi/lesson-05-notebook.pdf" },
  { id: "w5-quick", lesson: 5, kind: "Quick Check", name: "The Last Links", days: 0.5, tags: [6, 7], storage: "hcg/imperialism-wwi/lesson-05-quick-check.pdf" },
  { id: "w5-writing", lesson: 5, kind: "Writing", name: "Paragraph, the decisive link", days: 1, tags: [6, 7], storage: "hcg/imperialism-wwi/lesson-05-writing.pdf" },
  // Lesson 6
  { id: "w6-reading", lesson: 6, kind: "Reading", name: "Americans in the War", days: 1, tags: [8, 9], storage: "hcg/imperialism-wwi/lesson-06-reading.pdf", core: true },
  { id: "w6-notes", lesson: 6, kind: "Guided Notes", name: "Lesson 6 guided notes", days: 0, tags: [8, 9], storage: "hcg/imperialism-wwi/lesson-06-guided-notes.pdf", core: true },
  { id: "w6-activity", lesson: 6, kind: "Activity", name: "Mobilization System Stations: Americans in the War", days: 1, tags: [8, 9], storage: "hcg/imperialism-wwi/lesson-06-activity.pdf", core: true },
  { id: "w6-notebook", lesson: 6, kind: "Notebook", name: "Stage chart, the draft to the front", days: 0.5, tags: [8, 9], storage: "hcg/imperialism-wwi/lesson-06-notebook.pdf" },
  { id: "w6-quick", lesson: 6, kind: "Quick Check", name: "The 369th Infantry Comes Home", days: 0.5, tags: [8, 9], storage: "hcg/imperialism-wwi/lesson-06-quick-check.pdf" },
  { id: "w6-writing", lesson: 6, kind: "Writing", name: "Paragraph, how the United States mobilized and what its soldiers met", days: 1, tags: [8, 9], storage: "hcg/imperialism-wwi/lesson-06-writing.pdf" },
  // Lesson 7
  { id: "w7-reading", lesson: 7, kind: "Reading", name: "The Home Front", days: 1, tags: [10, 11], storage: "hcg/imperialism-wwi/lesson-07-reading.pdf", core: true },
  { id: "w7-notes", lesson: 7, kind: "Guided Notes", name: "Lesson 7 guided notes", days: 0, tags: [10, 11], storage: "hcg/imperialism-wwi/lesson-07-guided-notes.pdf", core: true },
  { id: "w7-activity", lesson: 7, kind: "Activity", name: "Liberty and Security: The Home Front on the Record", days: 1, tags: [10, 11], storage: "hcg/imperialism-wwi/lesson-07-activity.pdf", core: true },
  { id: "w7-notebook", lesson: 7, kind: "Notebook", name: "Who Gained, Who Lost", days: 0.5, tags: [10, 11], storage: "hcg/imperialism-wwi/lesson-07-notebook.pdf" },
  { id: "w7-quick", lesson: 7, kind: "Quick Check", name: "I Want You", days: 0.5, tags: [10, 11], storage: "hcg/imperialism-wwi/lesson-07-quick-check.pdf" },
  { id: "w7-writing", lesson: 7, kind: "Writing", name: "Paragraph, who gained, who lost", days: 1, tags: [10, 11], storage: "hcg/imperialism-wwi/lesson-07-writing.pdf" },
  // Lesson 8
  { id: "w8-reading", lesson: 8, kind: "Reading", name: "Wilson's Peace and the Turn Inward", days: 1, tags: [12, 13, 14, 15], storage: "hcg/imperialism-wwi/lesson-08-reading.pdf", core: true },
  { id: "w8-notes", lesson: 8, kind: "Guided Notes", name: "Lesson 8 guided notes", days: 0, tags: [12, 13, 14, 15], storage: "hcg/imperialism-wwi/lesson-08-guided-notes.pdf", core: true },
  { id: "w8-activity", lesson: 8, kind: "Activity", name: "Treaty Fight Hearing: Wilson's Peace and the Turn Inward", days: 1, tags: [12, 13, 14, 15], storage: "hcg/imperialism-wwi/lesson-08-activity.pdf", core: true },
  { id: "w8-notebook", lesson: 8, kind: "Notebook", name: "Subject, action, and result chart", days: 0.5, tags: [12, 13, 14, 15], storage: "hcg/imperialism-wwi/lesson-08-notebook.pdf" },
  { id: "w8-quick", lesson: 8, kind: "Quick Check", name: "Wilson's Peace and the Turn Inward", days: 0.5, tags: [12, 13, 14, 15], storage: "hcg/imperialism-wwi/lesson-08-quick-check.pdf" },
  { id: "w8-writing", lesson: 8, kind: "Writing", name: "Essay, the League refused", days: 1, tags: [12, 13, 14, 15], storage: "hcg/imperialism-wwi/lesson-08-writing.pdf" },
  // Review day
  { id: "wrev-guide", lesson: 9, kind: "Review", name: "Study guide (review day)", days: 1, tags: [], storage: "hcg/imperialism-wwi/review-study-guide.pdf", core: true },
  { id: "wrev-cross", lesson: 9, kind: "Review", name: "Crossword (30 answers)", days: 0.5, tags: [], storage: "hcg/imperialism-wwi/review-crossword.pdf" }
];

window.HCG_WWI_TOPICS = {
  1: { label: "Imperial expansion and its critics", note: "" },
  2: { label: "The United States in Asia and the Pacific", note: "" },
  3: { label: "The United States in the Caribbean and Latin America", note: "" },
  4: { label: "The First World War: causes, combat, and mobilization", note: "" },
  5: { label: "The home front: liberty, labor, race, and migration", note: "" },
  6: { label: "Peace, the League fight, and the turn inward", note: "" }
};
window.HCG_WWI_BP_TOPIC = {
  1: [1], 2: [1, 3], 3: [1, 2], 4: [2], 5: [3], 6: [4], 7: [4], 8: [4, 5], 9: [4], 10: [5], 11: [5], 12: [6], 13: [6], 14: [5, 6], 15: [6]
};

// TPSP picker index for Imperialism and World War I: the unit's
// premium DBQ (dbq17) first, then the era sources from the TPSP
// library files (progressive-era.json, then the three World War I
// sources in industrial-world-wars.json), each with its blueprint
// pre-tags. Duplicate records of the same source in the second
// file are not repeated. Audio excluded.
window.HCG_TPSP_WWI = [
 {
  "id": "dbq17",
  "title": "Was American Expansion Overseas a Duty or a Betrayal?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project \u00b7 premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true
 },
 {
  "id": "beveridge-march-of-the-flag",
  "title": "March of the Flag",
  "type": "Speech",
  "meta": "Albert J. Beveridge \u00b7 1898",
  "url": "https://tpsp.web.app/library?q=March%20of%20the%20Flag",
  "bp": [
   1
  ]
 },
 {
  "id": "gillam-remember-the-maine-1898",
  "title": "\"Remember the Maine! And Don't Forget the Starving Cubans!\" (cartoon)",
  "type": "Political cartoon",
  "meta": "Victor Gillam \u00b7 1898",
  "url": "https://tpsp.web.app/library?q=%22Remember%20the%20Maine%21%20And%20Don%27t%20Forget%20the%20Starving%20Cubans%21%22%20%28cartoon%29",
  "bp": [
   2
  ]
 },
 {
  "id": "harpers-weekly-remember-the-maine-1898",
  "title": "\"Remember the Maine,\" 1898 (Harper's Weekly)",
  "type": "Newspaper",
  "meta": "Harper's Weekly \u00b7 1898",
  "url": "https://tpsp.web.app/library?q=%22Remember%20the%20Maine%2C%22%201898%20%28Harper%27s%20Weekly%29",
  "bp": [
   2
  ]
 },
 {
  "id": "our-victorious-fleets-1898",
  "title": "Our Victorious Fleets in Cuban Waters, 1898 (Currier & Ives)",
  "type": "Illustration",
  "meta": "Currier & Ives \u00b7 1898",
  "url": "https://tpsp.web.app/library?q=Our%20Victorious%20Fleets%20in%20Cuban%20Waters%2C%201898%20%28Currier%20%26%20Ives%29",
  "bp": [
   2
  ]
 },
 {
  "id": "anti-imperialist-league-platform",
  "title": "American Anti-Imperialist League Platform",
  "type": "Platform",
  "meta": "American Anti-Imperialist League \u00b7 1899",
  "url": "https://tpsp.web.app/library?q=American%20Anti-Imperialist%20League%20Platform",
  "bp": [
   3
  ]
 },
 {
  "id": "zimmermann-telegram",
  "title": "Zimmermann Telegram (full text)",
  "type": "Government document",
  "meta": "Arthur Zimmermann \u00b7 1917",
  "url": "https://tpsp.web.app/library?q=Zimmermann%20Telegram%20%28full%20text%29",
  "bp": [
   7
  ]
 },
 {
  "id": "wilson-war-message-1917",
  "title": "War Message to Congress",
  "type": "Speech",
  "meta": "Woodrow Wilson \u00b7 1917",
  "url": "https://tpsp.web.app/library?q=War%20Message%20to%20Congress",
  "bp": [
   7
  ]
 },
 {
  "id": "flagg-i-want-you-1917",
  "title": "\"I Want You for U.S. Army\" (poster)",
  "type": "Poster",
  "meta": "James Montgomery Flagg \u00b7 1917",
  "url": "https://tpsp.web.app/library?q=%22I%20Want%20You%20for%20U.S.%20Army%22%20%28poster%29",
  "bp": [
   8
  ]
 },
 {
  "id": "hopps-destroy-this-mad-brute-1917",
  "title": "\"Destroy This Mad Brute\" (poster)",
  "type": "Poster",
  "meta": "Harry R. Hopps \u00b7 1917",
  "url": "https://tpsp.web.app/library?q=%22Destroy%20This%20Mad%20Brute%22%20%28poster%29",
  "bp": [
   10
  ]
 },
 {
  "id": "fourteen-points",
  "title": "Fourteen Points",
  "type": "Speech",
  "meta": "Woodrow Wilson \u00b7 1918",
  "url": "https://tpsp.web.app/library?q=Fourteen%20Points",
  "bp": [
   12
  ]
 },
 {
  "id": "hoover-memo-ridgely-1919",
  "title": "Memorandum to Special Agent Ridgely",
  "type": "Government document",
  "meta": "J. Edgar Hoover \u00b7 1919",
  "url": "https://tpsp.web.app/library?q=Memorandum%20to%20Special%20Agent%20Ridgely",
  "bp": [
   14
  ]
 },
 {
  "id": "treaty-of-versailles-1919",
  "title": "Treaty of Versailles, 1919 (Articles 231-233, excerpt)",
  "type": "Government document",
  "meta": "Paris Peace Conference (Allied and Associated Powers) \u00b7 1919",
  "url": "https://tpsp.web.app/library?q=Treaty%20of%20Versailles%2C%201919%20%28Articles%20231-233%2C%20excerpt%29",
  "bp": [
   12
  ]
 },
 {
  "id": "scott-negro-migration-1920",
  "title": "\"Negro Migration During the War\" (1920) (excerpt)",
  "type": "Government document",
  "meta": "Emmett J. Scott \u00b7 1920",
  "url": "https://tpsp.web.app/library?q=%22Negro%20Migration%20During%20the%20War%22%20%281920%29%20%28excerpt%29",
  "bp": [
   11
  ]
 },
 {
  "id": "owen-dulce-et-decorum-est-1917",
  "title": "\"Dulce et Decorum Est,\" 1917",
  "type": "Poem",
  "meta": "Wilfred Owen \u00b7 1917",
  "url": "https://tpsp.web.app/library?q=%22Dulce%20et%20Decorum%20Est%2C%22%201917",
  "bp": [
   9
  ]
 },
 {
  "id": "indian-sepoy-letter-1915",
  "title": "Letter of an Indian Sepoy from the Western Front, 1915 (excerpt)",
  "type": "Letter",
  "meta": "Anonymous Indian sepoy, Indian Expeditionary Force \u00b7 1915",
  "url": "https://tpsp.web.app/library?q=Letter%20of%20an%20Indian%20Sepoy%20from%20the%20Western%20Front%2C%201915%20%28excerpt%29",
  "bp": [
   9
  ]
 },
 {
  "id": "league-covenant-1919",
  "title": "The Covenant of the League of Nations, 1919 (excerpt)",
  "type": "Treaty",
  "meta": "The Paris Peace Conference \u00b7 1919",
  "url": "https://tpsp.web.app/library?q=The%20Covenant%20of%20the%20League%20of%20Nations%2C%201919%20%28excerpt%29",
  "bp": [
   13
  ]
 }
];

// ---------------------------------------------------------------------
// The Twenties: fourth plannable unit. Item tags, names, and files
// come from twenties/unit-manifest.md and twenties-skeleton.md. Files
// live in Firebase Storage under hcg/twenties/ (All-Access); items
// carry the Storage path in `storage`, never a public URL.
window.HCG_TW_BLUEPRINT = {
  1: "Mass production: Ford, the assembly line, and the falling price of the automobile",
  2: "Consumer culture: advertising, installment credit, chain stores, and the taught desire to buy",
  3: "Mass media and celebrity: network radio, the movies, the tabloids, sports, and the Lindbergh flight",
  4: "The automobile remakes daily life: suburbs, roads, tourism, courtship, and the costs",
  5: "Republican government at home: Harding, Coolidge, Teapot Dome, tax cuts, and the pro-business state",
  6: "Foreign policy of the decade: war debts, disarmament, the Kellogg-Briand Pact, and independence from the League",
  7: "Prohibition: the Volstead Act, enforcement, speakeasies, and organized crime",
  8: "Immigration restriction: the Emergency Quota Act, the National Origins Act, and eugenics",
  9: "The culture wars: the revived Klan, Scopes, fundamentalism, and Sacco and Vanzetti",
  10: "The Great Migration: causes, the Defender, and Black life in northern cities",
  11: "The Harlem Renaissance, the New Negro, Garvey and the UNIA, and Black organizing",
  12: "The farm problem: overproduction, falling prices, and McNary-Haugen",
  13: "Labor in decline: the open shop, welfare capitalism, and company unions",
  14: "Unequal prosperity and speculation: income concentration, installment debt, margin buying, and the bull market",
  15: "The crash of October 1929: what broke, what it did not yet mean, and the bridge to the Depression"
};

window.HCG_TW_LESSONS = [
  { n: 1, title: "The Business of America", question: "How did mass production and mass consumption remake American economic life in the 1920s?" },
  { n: 2, title: "Mass Media and the Celebrity Age", question: "How did radio, movies, and the popular press give Americans a shared national culture for the first time?" },
  { n: 3, title: "America on Wheels", question: "How did the automobile change where Americans lived, how they spent their time, and what they expected from life?" },
  { n: 4, title: "The Politics of Prosperity", question: "What did the Republican governments of the 1920s do at home and abroad, and what did they deliberately leave undone?" },
  { n: 5, title: "The Noble Experiment", question: "Why did Prohibition fail to stop drinking, and what did it build instead?" },
  { n: 6, title: "The Culture Wars", question: "What were the fights over immigration, religion, and science really about: who counted as a real American, and whose knowledge counted as true?" },
  { n: 7, title: "The Great Migration and the Harlem Renaissance", question: "What did Black Americans build in the cities of the North, and how did that building answer the country that had excluded them?" },
  { n: 8, title: "The Weak Spots and the Crash", question: "Why was the prosperity of the 1920s uneven from the start, and what exactly broke in October 1929?" }
];

window.HCG_TW_ITEMS = [
  // Lesson 1
  { id: "t1-reading", lesson: 1, kind: "Reading", name: "The Business of America", days: 1, tags: [1, 2], storage: "hcg/twenties/lesson-01-reading.pdf", core: true },
  { id: "t1-notes", lesson: 1, kind: "Guided Notes", name: "Lesson 1 guided notes", days: 0, tags: [1, 2], storage: "hcg/twenties/lesson-01-guided-notes.pdf", core: true },
  { id: "t1-activity", lesson: 1, kind: "Activity", name: "Consumer Culture Stations", days: 1, tags: [1, 2], storage: "hcg/twenties/lesson-01-activity.pdf", core: true },
  { id: "t1-notebook", lesson: 1, kind: "Notebook", name: "The system chart", days: 0.5, tags: [1, 2], storage: "hcg/twenties/lesson-01-notebook.pdf" },
  { id: "t1-quick", lesson: 1, kind: "Quick Check", name: "The Line and the Advertisement", days: 0.5, tags: [1, 2], storage: "hcg/twenties/lesson-01-quick-check.pdf" },
  { id: "t1-writing", lesson: 1, kind: "Writing", name: "One System", days: 1, tags: [1, 2], storage: "hcg/twenties/lesson-01-writing.pdf" },
  // Lesson 2
  { id: "t2-reading", lesson: 2, kind: "Reading", name: "Mass Media and the Celebrity Age", days: 1, tags: [3], storage: "hcg/twenties/lesson-02-reading.pdf", core: true },
  { id: "t2-notes", lesson: 2, kind: "Guided Notes", name: "Lesson 2 guided notes", days: 0, tags: [3], storage: "hcg/twenties/lesson-02-guided-notes.pdf", core: true },
  { id: "t2-activity", lesson: 2, kind: "Activity", name: "One Week of Media, 1927", days: 1, tags: [3], storage: "hcg/twenties/lesson-02-activity.pdf", core: true },
  { id: "t2-notebook", lesson: 2, kind: "Notebook", name: "Medium by medium chart", days: 0.5, tags: [3], storage: "hcg/twenties/lesson-02-notebook.pdf" },
  { id: "t2-quick", lesson: 2, kind: "Quick Check", name: "The Fight of the Century", days: 0.5, tags: [3], storage: "hcg/twenties/lesson-02-quick-check.pdf" },
  { id: "t2-writing", lesson: 2, kind: "Writing", name: "A Culture Heard at the Same Hour", days: 1, tags: [3], storage: "hcg/twenties/lesson-02-writing.pdf" },
  // Lesson 3
  { id: "t3-reading", lesson: 3, kind: "Reading", name: "America on Wheels", days: 1, tags: [4], storage: "hcg/twenties/lesson-03-reading.pdf", core: true },
  { id: "t3-notes", lesson: 3, kind: "Guided Notes", name: "Lesson 3 guided notes", days: 0, tags: [4], storage: "hcg/twenties/lesson-03-guided-notes.pdf", core: true },
  { id: "t3-activity", lesson: 3, kind: "Activity", name: "One Car, Five Changes", days: 1, tags: [4], storage: "hcg/twenties/lesson-03-activity.pdf", core: true },
  { id: "t3-notebook", lesson: 3, kind: "Notebook", name: "Before the car, with the car chart", days: 0.5, tags: [4], storage: "hcg/twenties/lesson-03-notebook.pdf" },
  { id: "t3-quick", lesson: 3, kind: "Quick Check", name: "Two Systems on One Street", days: 0.5, tags: [4], storage: "hcg/twenties/lesson-03-quick-check.pdf" },
  { id: "t3-writing", lesson: 3, kind: "Writing", name: "The Car and the Shape of a Life", days: 1, tags: [4], storage: "hcg/twenties/lesson-03-writing.pdf" },
  // Lesson 4
  { id: "t4-reading", lesson: 4, kind: "Reading", name: "The Politics of Prosperity", days: 1, tags: [5, 6], storage: "hcg/twenties/lesson-04-reading.pdf", core: true },
  { id: "t4-notes", lesson: 4, kind: "Guided Notes", name: "Lesson 4 guided notes", days: 0, tags: [5, 6], storage: "hcg/twenties/lesson-04-guided-notes.pdf", core: true },
  { id: "t4-activity", lesson: 4, kind: "Activity", name: "The Business of Government: A Decision Desk Simulation", days: 1, tags: [5, 6], storage: "hcg/twenties/lesson-04-activity.pdf", core: true },
  { id: "t4-notebook", lesson: 4, kind: "Notebook", name: "Did and left undone chart", days: 0.5, tags: [5, 6], storage: "hcg/twenties/lesson-04-notebook.pdf" },
  { id: "t4-quick", lesson: 4, kind: "Quick Check", name: "Signing Away War", days: 0.5, tags: [5, 6], storage: "hcg/twenties/lesson-04-quick-check.pdf" },
  { id: "t4-writing", lesson: 4, kind: "Writing", name: "Done and Deliberately Undone", days: 1, tags: [5, 6], storage: "hcg/twenties/lesson-04-writing.pdf" },
  // Lesson 5
  { id: "t5-reading", lesson: 5, kind: "Reading", name: "The Noble Experiment", days: 1, tags: [7], storage: "hcg/twenties/lesson-05-reading.pdf", core: true },
  { id: "t5-notes", lesson: 5, kind: "Guided Notes", name: "Lesson 5 guided notes", days: 0, tags: [7], storage: "hcg/twenties/lesson-05-guided-notes.pdf", core: true },
  { id: "t5-activity", lesson: 5, kind: "Activity", name: "The Enforcement Ledger", days: 1, tags: [7], storage: "hcg/twenties/lesson-05-activity.pdf", core: true },
  { id: "t5-notebook", lesson: 5, kind: "Notebook", name: "The lesson ledger", days: 0.5, tags: [7], storage: "hcg/twenties/lesson-05-notebook.pdf" },
  { id: "t5-quick", lesson: 5, kind: "Quick Check", name: "After the Raid", days: 0.5, tags: [7], storage: "hcg/twenties/lesson-05-quick-check.pdf" },
  { id: "t5-writing", lesson: 5, kind: "Writing", name: "What the Law Built", days: 1, tags: [7], storage: "hcg/twenties/lesson-05-writing.pdf" },
  // Lesson 6
  { id: "t6-reading", lesson: 6, kind: "Reading", name: "The Culture Wars", days: 1, tags: [8, 9], storage: "hcg/twenties/lesson-06-reading.pdf", core: true },
  { id: "t6-notes", lesson: 6, kind: "Guided Notes", name: "Lesson 6 guided notes", days: 0, tags: [8, 9], storage: "hcg/twenties/lesson-06-guided-notes.pdf", core: true },
  { id: "t6-activity", lesson: 6, kind: "Activity", name: "The Belonging Docket", days: 1, tags: [8, 9], storage: "hcg/twenties/lesson-06-activity.pdf", core: true },
  { id: "t6-notebook", lesson: 6, kind: "Notebook", name: "Fight, claim, and answer chart", days: 0.5, tags: [8, 9], storage: "hcg/twenties/lesson-06-notebook.pdf" },
  { id: "t6-quick", lesson: 6, kind: "Quick Check", name: "The Interview and the Verdict", days: 0.5, tags: [8, 9], storage: "hcg/twenties/lesson-06-quick-check.pdf" },
  { id: "t6-writing", lesson: 6, kind: "Writing", name: "Who Counted, and Whose Knowledge Counted", days: 1, tags: [8, 9], storage: "hcg/twenties/lesson-06-writing.pdf" },
  // Lesson 7
  { id: "t7-reading", lesson: 7, kind: "Reading", name: "The Great Migration and the Harlem Renaissance", days: 1, tags: [10, 11], storage: "hcg/twenties/lesson-07-reading.pdf", core: true },
  { id: "t7-notes", lesson: 7, kind: "Guided Notes", name: "Lesson 7 guided notes", days: 0, tags: [10, 11], storage: "hcg/twenties/lesson-07-guided-notes.pdf", core: true },
  { id: "t7-activity", lesson: 7, kind: "Activity", name: "Migration Account Jigsaw", days: 1, tags: [10, 11], storage: "hcg/twenties/lesson-07-activity.pdf", core: true },
  { id: "t7-notebook", lesson: 7, kind: "Notebook", name: "Push, pull, and built chart", days: 0.5, tags: [10, 11], storage: "hcg/twenties/lesson-07-notebook.pdf" },
  { id: "t7-quick", lesson: 7, kind: "Quick Check", name: "Garvey at His Desk", days: 0.5, tags: [10, 11], storage: "hcg/twenties/lesson-07-quick-check.pdf" },
  { id: "t7-writing", lesson: 7, kind: "Writing", name: "What They Built", days: 1, tags: [10, 11], storage: "hcg/twenties/lesson-07-writing.pdf" },
  // Lesson 8
  { id: "t8-reading", lesson: 8, kind: "Reading", name: "The Weak Spots and the Crash", days: 1, tags: [12, 13, 14, 15], storage: "hcg/twenties/lesson-08-reading.pdf", core: true },
  { id: "t8-notes", lesson: 8, kind: "Guided Notes", name: "Lesson 8 guided notes", days: 0, tags: [12, 13, 14, 15], storage: "hcg/twenties/lesson-08-guided-notes.pdf", core: true },
  { id: "t8-activity", lesson: 8, kind: "Activity", name: "The Boom Audit", days: 1, tags: [12, 13, 14, 15], storage: "hcg/twenties/lesson-08-activity.pdf", core: true },
  { id: "t8-notebook", lesson: 8, kind: "Notebook", name: "The Crash in Five Lines", days: 0.5, tags: [12, 13, 14, 15], storage: "hcg/twenties/lesson-08-notebook.pdf" },
  { id: "t8-quick", lesson: 8, kind: "Quick Check", name: "The Weak Spots and the Crash", days: 0.5, tags: [12, 13, 14, 15], storage: "hcg/twenties/lesson-08-quick-check.pdf" },
  { id: "t8-writing", lesson: 8, kind: "Writing", name: "Uneven From the Start", days: 1, tags: [12, 13, 14, 15], storage: "hcg/twenties/lesson-08-writing.pdf" },
  // Review day
  { id: "trev-guide", lesson: 9, kind: "Review", name: "Study guide (review day)", days: 1, tags: [], storage: "hcg/twenties/review-study-guide.pdf", core: true },
  { id: "trev-cross", lesson: 9, kind: "Review", name: "Crossword (36 answers)", days: 0.5, tags: [], storage: "hcg/twenties/review-crossword.pdf" }
];

window.HCG_TW_TOPICS = {
  1: { label: "The new economy: production, consumption, and credit", note: "" },
  2: { label: "Mass media and national culture", note: "" },
  3: { label: "The automobile and the reshaped map of daily life", note: "" },
  4: { label: "Politics, Prohibition, and the limited state", note: "" },
  5: { label: "Race, migration, and Black cultural and political movements", note: "" },
  6: { label: "Belonging and belief: restriction, the Klan, and the culture wars", note: "" }
};
window.HCG_TW_BP_TOPIC = {
  1: [1], 2: [1, 2], 3: [2], 4: [3, 1], 5: [4], 6: [4], 7: [4], 8: [6], 9: [6], 10: [5, 3], 11: [5, 2], 12: [1], 13: [1], 14: [1], 15: [1]
};

// TPSP picker index for the Twenties: the unit's premium DBQ (dbq18,
// era "The 1920s" in the TPSP premium catalog) first, then the era
// sources from the TPSP library file twenties.json in file order,
// each with conservative blueprint pre-tags where the source names
// the entry's content. The era file holds no Audio sources.
window.HCG_TPSP_TW = [
 {
  "id": "dbq18",
  "title": "Did the 1920s Move America Forward?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project \u00b7 premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true
 },
 {
  "id": "garvey-must-go-letter-1923",
  "title": "Letter to U.S. Attorney General Harry M. Daugherty (\"Garvey Must Go\" letter)",
  "type": "Letter",
  "meta": "Robert S. Abbott, Julia P. Coleman, William Pickens, Chandler Owen, Robert W. Bagnall, Harry H. Pace, John E. Nail, and George W. Harris \u00b7 1923",
  "url": "https://tpsp.web.app/library?q=Letter%20to%20U.S.%20Attorney%20General%20Harry%20M.%20Daugherty%20%28%22Garvey%20Must%20Go%22%20letter%29",
  "bp": [
   11
  ]
 },
 {
  "id": "garvey-negros-greatest-enemy-1923",
  "title": "The Negro's Greatest Enemy (autobiographical article, excerpt)",
  "type": "Memoir",
  "meta": "Marcus Garvey \u00b7 1923",
  "url": "https://tpsp.web.app/library?q=The%20Negro%27s%20Greatest%20Enemy%20%28autobiographical%20article%2C%20excerpt%29",
  "bp": [
   11
  ]
 },
 {
  "id": "immigration-act-1924",
  "title": "Immigration Act of 1924 (Johnson-Reed Act)",
  "type": "Government document",
  "meta": "68th U.S. Congress \u00b7 1924",
  "url": "https://tpsp.web.app/library?q=Immigration%20Act%20of%201924%20%28Johnson-Reed%20Act%29",
  "bp": [
   8
  ]
 },
 {
  "id": "butler-act-1925",
  "title": "The Butler Act",
  "type": "Government document",
  "meta": "Tennessee General Assembly \u00b7 1925",
  "url": "https://tpsp.web.app/library?q=The%20Butler%20Act",
  "bp": [
   9
  ]
 },
 {
  "id": "evans-klans-fight-for-americanism-1926",
  "title": "\"The Klan's Fight for Americanism\" (excerpt)",
  "type": "Magazine",
  "meta": "Hiram W. Evans \u00b7 1926",
  "url": "https://tpsp.web.app/library?q=%22The%20Klan%27s%20Fight%20for%20Americanism%22%20%28excerpt%29",
  "bp": [
   9
  ]
 },
 {
  "id": "hughes-i-too-1926",
  "title": "\"I, Too\"",
  "type": "Poem",
  "meta": "Langston Hughes \u00b7 1926",
  "url": "https://tpsp.web.app/library?q=%22I%2C%20Too%22",
  "bp": [
   11
  ]
 },
 {
  "id": "vanzetti-courtroom-statement-1927",
  "title": "Statement to the Court at Sentencing (Sacco and Vanzetti)",
  "type": "Speech",
  "meta": "Bartolomeo Vanzetti (with Nicola Sacco) \u00b7 1927",
  "url": "https://tpsp.web.app/library?q=Statement%20to%20the%20Court%20at%20Sentencing%20%28Sacco%20and%20Vanzetti%29",
  "bp": [
   9
  ]
 },
 {
  "id": "bryan-scopes-closing-1925",
  "title": "William Jennings Bryan's Undelivered Closing Statement at the Scopes Trial (excerpt)",
  "type": "Speech",
  "meta": "William Jennings Bryan \u00b7 1925",
  "url": "https://tpsp.web.app/library?q=William%20Jennings%20Bryan%27s%20Undelivered%20Closing%20Statement%20at%20the%20Scopes%20Trial%20%28excerpt%29",
  "bp": [
   9
  ]
 },
 {
  "id": "cable-act-1922",
  "title": "The Cable Act (excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress \u00b7 1922",
  "url": "https://tpsp.web.app/library?q=The%20Cable%20Act%20%28excerpt%29"
 },
 {
  "id": "great-gatsby-excerpt-1925",
  "title": "\"The Great Gatsby\" (novel excerpt)",
  "type": "Book",
  "meta": "F. Scott Fitzgerald \u00b7 1925",
  "url": "https://tpsp.web.app/library?q=%22The%20Great%20Gatsby%22%20%28novel%20excerpt%29",
  "bp": [
   2
  ]
 },
 {
  "id": "harding-first-inaugural-1921",
  "title": "First Inaugural Address (excerpt)",
  "type": "Speech",
  "meta": "Warren G. Harding \u00b7 1921",
  "url": "https://tpsp.web.app/library?q=First%20Inaugural%20Address%20%28excerpt%29",
  "bp": [
   5
  ]
 },
 {
  "id": "hughes-negro-artist-racial-mountain-1926",
  "title": "\"The Negro Artist and the Racial Mountain\" (excerpt)",
  "type": "Magazine",
  "meta": "Langston Hughes \u00b7 1926",
  "url": "https://tpsp.web.app/library?q=%22The%20Negro%20Artist%20and%20the%20Racial%20Mountain%22%20%28excerpt%29",
  "bp": [
   11
  ]
 },
 {
  "id": "indian-citizenship-act-1924",
  "title": "The Indian Citizenship Act",
  "type": "Government document",
  "meta": "U.S. Congress \u00b7 1924",
  "url": "https://tpsp.web.app/library?q=The%20Indian%20Citizenship%20Act"
 },
 {
  "id": "radio-act-1927",
  "title": "The Radio Act of 1927 (excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress \u00b7 1927",
  "url": "https://tpsp.web.app/library?q=The%20Radio%20Act%20of%201927%20%28excerpt%29",
  "bp": [
   3
  ]
 },
 {
  "id": "mellon-taxation-peoples-business-1924",
  "title": "Taxation: The People's Business (excerpt)",
  "type": "Book",
  "meta": "Andrew W. Mellon \u00b7 1924",
  "url": "https://tpsp.web.app/library?q=Taxation%3A%20The%20People%27s%20Business%20%28excerpt%29",
  "bp": [
   5
  ]
 },
 {
  "id": "sheppard-towner-act-1921",
  "title": "Sheppard-Towner Maternity and Infancy Protection Act (excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress \u00b7 1921",
  "url": "https://tpsp.web.app/library?q=Sheppard-Towner%20Maternity%20and%20Infancy%20Protection%20Act%20%28excerpt%29"
 },
 {
  "id": "coolidge-first-inaugural-1925",
  "title": "First Inaugural Address (excerpt)",
  "type": "Speech",
  "meta": "Calvin Coolidge \u00b7 1925",
  "url": "https://tpsp.web.app/library?q=First%20Inaugural%20Address%20%28excerpt%29",
  "bp": [
   5
  ]
 },
 {
  "id": "hoover-american-individualism-1922",
  "title": "\"American Individualism\" (excerpt)",
  "type": "Book",
  "meta": "Herbert Hoover \u00b7 1922",
  "url": "https://tpsp.web.app/library?q=%22American%20Individualism%22%20%28excerpt%29",
  "bp": [
   5
  ]
 },
 {
  "id": "coolidge-mcnary-haugen-veto-1928",
  "title": "McNary-Haugen Veto Message (second veto, excerpt)",
  "type": "Government document",
  "meta": "Calvin Coolidge \u00b7 1928",
  "url": "https://tpsp.web.app/library?q=McNary-Haugen%20Veto%20Message%20%28second%20veto%2C%20excerpt%29",
  "bp": [
   12
  ]
 },
 {
  "id": "ford-my-life-and-work-1922",
  "title": "\"My Life and Work\" (excerpt)",
  "type": "Book",
  "meta": "Henry Ford (with Samuel Crowther) \u00b7 1922",
  "url": "https://tpsp.web.app/library?q=%22My%20Life%20and%20Work%22%20%28excerpt%29",
  "bp": [
   1
  ]
 },
 {
  "id": "railway-labor-act-1926",
  "title": "The Railway Labor Act (excerpt)",
  "type": "Government document",
  "meta": "69th U.S. Congress \u00b7 1926",
  "url": "https://tpsp.web.app/library?q=The%20Railway%20Labor%20Act%20%28excerpt%29"
 },
 {
  "id": "faulkner-jazz-syncopation-1921",
  "title": "\"Does Jazz Put the Sin in Syncopation?\" (excerpt)",
  "type": "Magazine",
  "meta": "Anne Shaw Faulkner \u00b7 1921",
  "url": "https://tpsp.web.app/library?q=%22Does%20Jazz%20Put%20the%20Sin%20in%20Syncopation%3F%22%20%28excerpt%29"
 }
];

// ---------------------------------------------------------------------
// Depression and New Deal: fifth plannable unit. Item tags, names, and
// files come from depression-new-deal/unit-manifest.md and
// depression-new-deal-skeleton.md. Files live in Firebase Storage under
// hcg/depression-new-deal/ (All-Access); items carry the Storage path
// in `storage`, never a public URL.
window.HCG_DP_BLUEPRINT = {
  1: "The depth of the collapse: bank failures, deflation, falling production, and mass unemployment",
  2: "The human cost: breadlines, Hoovervilles, eviction, family strain, and Dust Bowl migration",
  3: "Hoover's program: voluntarism, the Farm Board, public works, and the Hawley-Smoot Tariff",
  4: "The limits of Hoover's response: the RFC, the Bonus Army, the election of 1932, and the interregnum",
  5: "The banking rescue: the bank holiday, the Emergency Banking Act, and the first fireside chat",
  6: "The Hundred Days: the AAA, the TVA, the NIRA, and deposit insurance in one legislative season",
  7: "Relief at work: direct relief, work relief, and the FERA, CCC, CWA, and PWA in people's lives",
  8: "The reach and the gaps: the NRA codes, uneven and segregated delivery, and unemployment still high in 1934",
  9: "The critics who said too little: Long and Share Our Wealth, the Townsend Plan, and Coughlin",
  10: "The critics who said too much: the Liberty League and the Supreme Court in Schechter and Butler",
  11: "The Second New Deal: the WPA and the Social Security Act of 1935",
  12: "Labor rights in law: the Wagner Act, collective bargaining, and the labor board",
  13: "Labor rising: the CIO, the sit-down strikes, Flint, and the cost at Republic Steel",
  14: "The hard year: the court packing fight and the Roosevelt recession of 1937 to 1938",
  15: "Legacy and limits: the changed federal role, the safety net, the exclusions, and the recovery that waited for war"
};

window.HCG_DP_LESSONS = [
  { n: 1, title: "The Human Cost of the Depression", question: "How deep did the Depression cut, and how did ordinary families live through it?" },
  { n: 2, title: "Hoover and the Limits of Voluntarism", question: "What did President Hoover do about the Depression, and why did his program fall short of the collapse?" },
  { n: 3, title: "Roosevelt and the First Hundred Days", question: "How did Roosevelt's first hundred days change what Americans expected their government to do in a crisis?" },
  { n: 4, title: "Relief, Recovery, and the Alphabet Agencies at Work", question: "What did the New Deal agencies actually do in people's lives, and how far did their help reach?" },
  { n: 5, title: "The Critics: Long, Townsend, Coughlin, and the Court", question: "Why did the New Deal draw attack from every direction by 1935, and what did the attacks reveal about the country?" },
  { n: 6, title: "The Second New Deal", question: "How did the Second New Deal of 1935 move beyond the first, and who was it built to protect?" },
  { n: 7, title: "Labor Rising and the Recession of 1937", question: "Why did 1937 bring both labor's greatest victories and the New Deal's hardest year?" },
  { n: 8, title: "What the New Deal Changed and What It Did Not", question: "What did the New Deal change for good, what did it leave undone, and how should it be judged?" }
];

window.HCG_DP_ITEMS = [
  // Lesson 1
  { id: "d1-reading", lesson: 1, kind: "Reading", name: "The Human Cost of the Depression", days: 1, tags: [1, 2], storage: "hcg/depression-new-deal/lesson-01-reading.pdf", core: true },
  { id: "d1-notes", lesson: 1, kind: "Guided Notes", name: "Lesson 1 guided notes", days: 0, tags: [1, 2], storage: "hcg/depression-new-deal/lesson-01-guided-notes.pdf", core: true },
  { id: "d1-activity", lesson: 1, kind: "Activity", name: "The Cost Ledger", days: 1, tags: [1, 2], storage: "hcg/depression-new-deal/lesson-01-activity.pdf", core: true },
  { id: "d1-notebook", lesson: 1, kind: "Notebook", name: "Part of the cost chart", days: 0.5, tags: [1, 2], storage: "hcg/depression-new-deal/lesson-01-notebook.pdf" },
  { id: "d1-quick", lesson: 1, kind: "Quick Check", name: "The Run and the Line", days: 0.5, tags: [1, 2], storage: "hcg/depression-new-deal/lesson-01-quick-check.pdf" },
  { id: "d1-writing", lesson: 1, kind: "Writing", name: "A Public Emergency", days: 1, tags: [1, 2], storage: "hcg/depression-new-deal/lesson-01-writing.pdf" },
  // Lesson 2
  { id: "d2-reading", lesson: 2, kind: "Reading", name: "Hoover and the Limits of Voluntarism", days: 1, tags: [3, 4], storage: "hcg/depression-new-deal/lesson-02-reading.pdf", core: true },
  { id: "d2-notes", lesson: 2, kind: "Guided Notes", name: "Lesson 2 guided notes", days: 0, tags: [3, 4], storage: "hcg/depression-new-deal/lesson-02-guided-notes.pdf", core: true },
  { id: "d2-activity", lesson: 2, kind: "Activity", name: "The Voluntarism Test", days: 1, tags: [3, 4], storage: "hcg/depression-new-deal/lesson-02-activity.pdf", core: true },
  { id: "d2-notebook", lesson: 2, kind: "Notebook", name: "Part of the record chart", days: 0.5, tags: [3, 4], storage: "hcg/depression-new-deal/lesson-02-notebook.pdf" },
  { id: "d2-quick", lesson: 2, kind: "Quick Check", name: "The Camp on the Anacostia", days: 0.5, tags: [3, 4], storage: "hcg/depression-new-deal/lesson-02-quick-check.pdf" },
  { id: "d2-writing", lesson: 2, kind: "Writing", name: "Judging Hoover's Program", days: 1, tags: [3, 4], storage: "hcg/depression-new-deal/lesson-02-writing.pdf" },
  // Lesson 3
  { id: "d3-reading", lesson: 3, kind: "Reading", name: "Roosevelt and the First Hundred Days", days: 1, tags: [5, 6], storage: "hcg/depression-new-deal/lesson-03-reading.pdf", core: true },
  { id: "d3-notes", lesson: 3, kind: "Guided Notes", name: "Lesson 3 guided notes", days: 0, tags: [5, 6], storage: "hcg/depression-new-deal/lesson-03-guided-notes.pdf", core: true },
  { id: "d3-activity", lesson: 3, kind: "Activity", name: "Hundred Days Drafting Desk", days: 1, tags: [5, 6], storage: "hcg/depression-new-deal/lesson-03-activity.pdf", core: true },
  { id: "d3-notebook", lesson: 3, kind: "Notebook", name: "Hundred Days chart", days: 0.5, tags: [5, 6], storage: "hcg/depression-new-deal/lesson-03-notebook.pdf" },
  { id: "d3-quick", lesson: 3, kind: "Quick Check", name: "The Banking Rescue", days: 0.5, tags: [5, 6], storage: "hcg/depression-new-deal/lesson-03-quick-check.pdf" },
  { id: "d3-writing", lesson: 3, kind: "Writing", name: "A New Expectation", days: 1, tags: [5, 6], storage: "hcg/depression-new-deal/lesson-03-writing.pdf" },
  // Lesson 4
  { id: "d4-reading", lesson: 4, kind: "Reading", name: "Relief, Recovery, and the Alphabet Agencies at Work", days: 1, tags: [7, 8], storage: "hcg/depression-new-deal/lesson-04-reading.pdf", core: true },
  { id: "d4-notes", lesson: 4, kind: "Guided Notes", name: "Lesson 4 guided notes", days: 0, tags: [7, 8], storage: "hcg/depression-new-deal/lesson-04-guided-notes.pdf", core: true },
  { id: "d4-activity", lesson: 4, kind: "Activity", name: "Agency Case Files", days: 1, tags: [7, 8], storage: "hcg/depression-new-deal/lesson-04-activity.pdf", core: true },
  { id: "d4-notebook", lesson: 4, kind: "Notebook", name: "Agency by agency chart", days: 0.5, tags: [7, 8], storage: "hcg/depression-new-deal/lesson-04-notebook.pdf" },
  { id: "d4-quick", lesson: 4, kind: "Quick Check", name: "Relief at Work", days: 0.5, tags: [7, 8], storage: "hcg/depression-new-deal/lesson-04-quick-check.pdf" },
  { id: "d4-writing", lesson: 4, kind: "Writing", name: "How Far Did Help Reach", days: 1, tags: [7, 8], storage: "hcg/depression-new-deal/lesson-04-writing.pdf" },
  // Lesson 5
  { id: "d5-reading", lesson: 5, kind: "Reading", name: "The Critics: Long, Townsend, Coughlin, and the Court", days: 1, tags: [9, 10], storage: "hcg/depression-new-deal/lesson-05-reading.pdf", core: true },
  { id: "d5-notes", lesson: 5, kind: "Guided Notes", name: "Lesson 5 guided notes", days: 0, tags: [9, 10], storage: "hcg/depression-new-deal/lesson-05-guided-notes.pdf", core: true },
  { id: "d5-activity", lesson: 5, kind: "Activity", name: "The Pressure Map", days: 1, tags: [9, 10], storage: "hcg/depression-new-deal/lesson-05-activity.pdf", core: true },
  { id: "d5-notebook", lesson: 5, kind: "Notebook", name: "Critic by critic chart", days: 0.5, tags: [9, 10], storage: "hcg/depression-new-deal/lesson-05-notebook.pdf" },
  { id: "d5-quick", lesson: 5, kind: "Quick Check", name: "The Filibuster and the Syllabus", days: 0.5, tags: [9, 10], storage: "hcg/depression-new-deal/lesson-05-quick-check.pdf" },
  { id: "d5-writing", lesson: 5, kind: "Writing", name: "Attack From Every Direction", days: 1, tags: [9, 10], storage: "hcg/depression-new-deal/lesson-05-writing.pdf" },
  // Lesson 6
  { id: "d6-reading", lesson: 6, kind: "Reading", name: "The Second New Deal", days: 1, tags: [11, 12], storage: "hcg/depression-new-deal/lesson-06-reading.pdf", core: true },
  { id: "d6-notes", lesson: 6, kind: "Guided Notes", name: "Lesson 6 guided notes", days: 0, tags: [11, 12], storage: "hcg/depression-new-deal/lesson-06-guided-notes.pdf", core: true },
  { id: "d6-activity", lesson: 6, kind: "Activity", name: "The Settlement Chart", days: 1, tags: [11, 12], storage: "hcg/depression-new-deal/lesson-06-activity.pdf", core: true },
  { id: "d6-notebook", lesson: 6, kind: "Notebook", name: "The 1935 settlement chart", days: 0.5, tags: [11, 12], storage: "hcg/depression-new-deal/lesson-06-notebook.pdf" },
  { id: "d6-quick", lesson: 6, kind: "Quick Check", name: "The Signing and the Statute", days: 0.5, tags: [11, 12], storage: "hcg/depression-new-deal/lesson-06-quick-check.pdf" },
  { id: "d6-writing", lesson: 6, kind: "Writing", name: "The Settlement of 1935", days: 1, tags: [11, 12], storage: "hcg/depression-new-deal/lesson-06-writing.pdf" },
  // Lesson 7
  { id: "d7-reading", lesson: 7, kind: "Reading", name: "Labor Rising and the Recession of 1937", days: 1, tags: [13, 14], storage: "hcg/depression-new-deal/lesson-07-reading.pdf", core: true },
  { id: "d7-notes", lesson: 7, kind: "Guided Notes", name: "Lesson 7 guided notes", days: 0, tags: [13, 14], storage: "hcg/depression-new-deal/lesson-07-guided-notes.pdf", core: true },
  { id: "d7-activity", lesson: 7, kind: "Activity", name: "Two Ledgers of 1937", days: 1, tags: [13, 14], storage: "hcg/depression-new-deal/lesson-07-activity.pdf", core: true },
  { id: "d7-notebook", lesson: 7, kind: "Notebook", name: "Two ledgers chart", days: 0.5, tags: [13, 14], storage: "hcg/depression-new-deal/lesson-07-notebook.pdf" },
  { id: "d7-quick", lesson: 7, kind: "Quick Check", name: "The Guard at Flint", days: 0.5, tags: [13, 14], storage: "hcg/depression-new-deal/lesson-07-quick-check.pdf" },
  { id: "d7-writing", lesson: 7, kind: "Writing", name: "Two Ledgers of One Year", days: 1, tags: [13, 14], storage: "hcg/depression-new-deal/lesson-07-writing.pdf" },
  // Lesson 8
  { id: "d8-reading", lesson: 8, kind: "Reading", name: "What the New Deal Changed and What It Did Not", days: 1, tags: [15], storage: "hcg/depression-new-deal/lesson-08-reading.pdf", core: true },
  { id: "d8-notes", lesson: 8, kind: "Guided Notes", name: "Lesson 8 guided notes", days: 0, tags: [15], storage: "hcg/depression-new-deal/lesson-08-guided-notes.pdf", core: true },
  { id: "d8-activity", lesson: 8, kind: "Activity", name: "The Verdict Brief", days: 1, tags: [15], storage: "hcg/depression-new-deal/lesson-08-activity.pdf", core: true },
  { id: "d8-notebook", lesson: 8, kind: "Notebook", name: "Changed and left undone chart", days: 0.5, tags: [15], storage: "hcg/depression-new-deal/lesson-08-notebook.pdf" },
  { id: "d8-quick", lesson: 8, kind: "Quick Check", name: "The Number on His Arm", days: 0.5, tags: [15], storage: "hcg/depression-new-deal/lesson-08-quick-check.pdf" },
  { id: "d8-writing", lesson: 8, kind: "Writing", name: "The Verdict", days: 1, tags: [15], storage: "hcg/depression-new-deal/lesson-08-writing.pdf" },
  // Review day
  { id: "drev-guide", lesson: 9, kind: "Review", name: "Study guide (review day)", days: 1, tags: [], storage: "hcg/depression-new-deal/review-study-guide.pdf", core: true },
  { id: "drev-cross", lesson: 9, kind: "Review", name: "Crossword (41 answers)", days: 0.5, tags: [], storage: "hcg/depression-new-deal/review-crossword.pdf" }
];

window.HCG_DP_TOPICS = {
  1: { label: "Collapse and human cost", note: "" },
  2: { label: "From Hoover to Roosevelt: the changing federal role", note: "" },
  3: { label: "Relief, recovery, and reform: the New Deal programs", note: "" },
  4: { label: "Opposition, the critics, and the courts", note: "" },
  5: { label: "Labor, exclusion, and the unfinished agenda", note: "" },
  6: { label: "Legacy: the new American state and its limits", note: "" }
};
window.HCG_DP_BP_TOPIC = {
  1: [1], 2: [1], 3: [2], 4: [2, 4], 5: [2, 3], 6: [3], 7: [3], 8: [3, 5], 9: [4], 10: [4], 11: [3, 6], 12: [5, 3], 13: [5], 14: [4, 6], 15: [6, 5]
};

// TPSP picker index for Depression and New Deal: the unit's premium
// DBQ (dbq5, era "Great Depression and New Deal" in the TPSP premium
// catalog, catalog code DBQ180) first, then the era sources from the
// TPSP library file depression.json in file order, each with
// conservative blueprint pre-tags where the source names the entry's
// content. Audio sources are excluded, as in the other units.
window.HCG_TPSP_DP = [
 {
  "id": "dbq5",
  "title": "Did the New Deal End the Great Depression?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project \u00b7 premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true
 },
 {
  "id": "hoover-depression-new-deal-1931-1933",
  "title": "Herbert Hoover on the Great Depression and New Deal, 1931-1933 (excerpt)",
  "type": "Letter",
  "meta": "Herbert Hoover \u00b7 1931-1933",
  "url": "https://tpsp.web.app/library?q=Herbert%20Hoover%20on%20the%20Great%20Depression%20and%20New%20Deal%2C%201931-1933%20%28excerpt%29",
  "bp": [
   3,
   4
  ]
 },
 {
  "id": "fdr-first-inaugural",
  "title": "First Inaugural Address",
  "type": "Speech",
  "meta": "Franklin D. Roosevelt \u00b7 1933",
  "url": "https://tpsp.web.app/library?q=First%20Inaugural%20Address",
  "bp": [
   5
  ]
 },
 {
  "id": "social-security-act-1935",
  "title": "Social Security Act (excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress \u00b7 1935",
  "url": "https://tpsp.web.app/library?q=Social%20Security%20Act%20%28excerpt%29",
  "bp": [
   11
  ]
 },
 {
  "id": "henderson-letter-wallace-1935",
  "title": "Letter to Secretary of Agriculture Henry A. Wallace (excerpt)",
  "type": "Letter",
  "meta": "Caroline Henderson \u00b7 1935",
  "url": "https://tpsp.web.app/library?q=Letter%20to%20Secretary%20of%20Agriculture%20Henry%20A.%20Wallace%20%28excerpt%29",
  "bp": [
   2
  ]
 },
 {
  "id": "lange-migrant-mother-1936",
  "title": "\"Migrant Mother\" (photograph)",
  "type": "Photograph",
  "meta": "Dorothea Lange \u00b7 March 1936",
  "url": "https://tpsp.web.app/library?q=%22Migrant%20Mother%22%20%28photograph%29",
  "bp": [
   2
  ]
 },
 {
  "id": "rothstein-dust-storm-1936",
  "title": "Farmer and sons walking in a dust storm, Cimarron County, Oklahoma (photograph)",
  "type": "Photograph",
  "meta": "Arthur Rothstein \u00b7 1936",
  "url": "https://tpsp.web.app/library?q=Farmer%20and%20sons%20walking%20in%20a%20dust%20storm%2C%20Cimarron%20County%2C%20Oklahoma%20%28photograph%29",
  "bp": [
   2
  ]
 },
 {
  "id": "cooke-drought-committee-report-1936",
  "title": "Report of the Great Plains Drought Area Committee (excerpt)",
  "type": "Government document",
  "meta": "Morris L. Cooke (for the Great Plains Drought Area Committee) \u00b7 1936",
  "url": "https://tpsp.web.app/library?q=Report%20of%20the%20Great%20Plains%20Drought%20Area%20Committee%20%28excerpt%29",
  "bp": [
   2
  ]
 },
 {
  "id": "rothstein-texas-panhandle-dust-1936",
  "title": "\"Heavy black clouds of dust rising over the Texas Panhandle, Texas\" (photograph)",
  "type": "Photograph",
  "meta": "Arthur Rothstein \u00b7 1936",
  "url": "https://tpsp.web.app/library?q=%22Heavy%20black%20clouds%20of%20dust%20rising%20over%20the%20Texas%20Panhandle%2C%20Texas%22%20%28photograph%29",
  "bp": [
   2
  ]
 },
 {
  "id": "lange-migrant-mother-sequence-1936",
  "title": "Photographs of the Migrant Mother family, Nipomo, California (sequence)",
  "type": "Photograph",
  "meta": "Dorothea Lange \u00b7 1936",
  "url": "https://tpsp.web.app/library?q=Photographs%20of%20the%20Migrant%20Mother%20family%2C%20Nipomo%2C%20California%20%28sequence%29",
  "bp": [
   2
  ]
 },
 {
  "id": "tva-pictorial-map-1939",
  "title": "\"Tennessee Valley Area: Pictorial Map\" (map)",
  "type": "Map",
  "meta": "Tennessee Valley Authority \u00b7 1939",
  "url": "https://tpsp.web.app/library?q=%22Tennessee%20Valley%20Area%3A%20Pictorial%20Map%22%20%28map%29",
  "bp": [
   6
  ]
 },
 {
  "id": "four-freedoms",
  "title": "Four Freedoms Speech (excerpt)",
  "type": "Speech",
  "meta": "Franklin D. Roosevelt \u00b7 1941",
  "url": "https://tpsp.web.app/library?q=Four%20Freedoms%20Speech%20%28excerpt%29"
 },
 {
  "id": "executive-order-8802-1941",
  "title": "Executive Order 8802 (excerpt)",
  "type": "Government document",
  "meta": "Franklin D. Roosevelt \u00b7 1941",
  "url": "https://tpsp.web.app/library?q=Executive%20Order%208802%20%28excerpt%29"
 },
 {
  "id": "agricultural-adjustment-act-1933",
  "title": "Agricultural Adjustment Act of 1933 (excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress \u00b7 1933",
  "url": "https://tpsp.web.app/library?q=Agricultural%20Adjustment%20Act%20of%201933%20%28excerpt%29",
  "bp": [
   6
  ]
 },
 {
  "id": "evans-sharecropper-bud-fields-1936",
  "title": "\"Sharecropper Bud Fields and his family at home\" (photograph)",
  "type": "Photograph",
  "meta": "Walker Evans \u00b7 1936",
  "url": "https://tpsp.web.app/library?q=%22Sharecropper%20Bud%20Fields%20and%20his%20family%20at%20home%22%20%28photograph%29",
  "bp": [
   2
  ]
 },
 {
  "id": "fdr-arsenal-of-democracy-1940",
  "title": "\"Arsenal of Democracy\" Fireside Chat (excerpt)",
  "type": "Speech",
  "meta": "Franklin D. Roosevelt \u00b7 1940",
  "url": "https://tpsp.web.app/library?q=%22Arsenal%20of%20Democracy%22%20Fireside%20Chat%20%28excerpt%29"
 },
 {
  "id": "fdr-fireside-chat-1-1933",
  "title": "Fireside Chat 1: \"On the Banking Crisis\" (excerpt)",
  "type": "Speech",
  "meta": "Franklin D. Roosevelt \u00b7 1933",
  "url": "https://tpsp.web.app/library?q=Fireside%20Chat%201%3A%20%22On%20the%20Banking%20Crisis%22%20%28excerpt%29",
  "bp": [
   5
  ]
 },
 {
  "id": "fdr-quarantine-speech-1937",
  "title": "\"Quarantine\" Speech (excerpt)",
  "type": "Speech",
  "meta": "Franklin D. Roosevelt \u00b7 1937",
  "url": "https://tpsp.web.app/library?q=%22Quarantine%22%20Speech%20%28excerpt%29"
 },
 {
  "id": "fdr-second-inaugural-1937",
  "title": "Second Inaugural Address (excerpt)",
  "type": "Speech",
  "meta": "Franklin D. Roosevelt \u00b7 1937",
  "url": "https://tpsp.web.app/library?q=Second%20Inaugural%20Address%20%28excerpt%29"
 },
 {
  "id": "huey-long-share-the-wealth-1934",
  "title": "\"Share the Wealth\" Senate Speech (excerpt)",
  "type": "Speech",
  "meta": "Huey P. Long \u00b7 1934",
  "url": "https://tpsp.web.app/library?q=%22Share%20the%20Wealth%22%20Senate%20Speech%20%28excerpt%29",
  "bp": [
   9
  ]
 },
 {
  "id": "louis-love-wpa-narrative",
  "title": "WPA Slave Narrative of Louis Love (excerpt)",
  "type": "Narrative",
  "meta": "Louis Love (interviewed by the Federal Writers' Project) \u00b7 1936-1938",
  "url": "https://tpsp.web.app/library?q=WPA%20Slave%20Narrative%20of%20Louis%20Love%20%28excerpt%29",
  "bp": [
   11
  ]
 },
 {
  "id": "nra-blue-eagle-restaurant-1933",
  "title": "NRA Blue Eagle Poster in Restaurant Window (photograph)",
  "type": "Photograph",
  "meta": "National Recovery Administration (photographer unknown) \u00b7 c. 1934",
  "url": "https://tpsp.web.app/library?q=NRA%20Blue%20Eagle%20Poster%20in%20Restaurant%20Window%20%28photograph%29",
  "bp": [
   8
  ]
 },
 {
  "id": "wagner-act-1935",
  "title": "National Labor Relations Act (\"Wagner Act\") (excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress \u00b7 1935",
  "url": "https://tpsp.web.app/library?q=National%20Labor%20Relations%20Act%20%28%22Wagner%20Act%22%29%20%28excerpt%29",
  "bp": [
   12
  ]
 },
 {
  "id": "banking-act-1933-glass-steagall",
  "title": "Banking Act of 1933 (Glass-Steagall) (excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress \u00b7 1933",
  "url": "https://tpsp.web.app/library?q=Banking%20Act%20of%201933%20%28Glass-Steagall%29%20%28excerpt%29",
  "bp": [
   6
  ]
 },
 {
  "id": "indian-reorganization-act-1934",
  "title": "Indian Reorganization Act (excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress \u00b7 1934",
  "url": "https://tpsp.web.app/library?q=Indian%20Reorganization%20Act%20%28excerpt%29"
 }
];


// ---------------------------------------------------------------------
// World War II: sixth plannable unit. Item tags, names, and files come
// from world-war-ii/unit-manifest.md and world-war-ii-skeleton.md.
// Files live in Firebase Storage under hcg/world-war-ii/ (All-Access);
// items carry the Storage path in `storage`, never a public URL.
window.HCG_WW2_BLUEPRINT = {
  1: "The neutrality laws: the Neutrality Acts, the memory of the First World War, and the isolationist case",
  2: "The turn to aid: cash-and-carry, Lend-Lease, the Four Freedoms, the Atlantic Charter, and the undeclared Atlantic war",
  3: "Pearl Harbor and entry: the attack of December 7, 1941, the declarations of war, and the end of the neutrality debate",
  4: "Strategy for a two-ocean war: the Grand Alliance, Germany first, and the second front argument",
  5: "Mobilization: the peacetime draft, the conversion of industry, and the end of mass unemployment",
  6: "The home front regime: the War Production Board, rationing, price controls, war bonds, and the migration to war work",
  7: "Into Europe: North Africa, Sicily and Italy, and the strategic bombing campaign",
  8: "The road to VE Day: D-Day, the drive across France, the Bulge, the Elbe, and the surrender of Germany",
  9: "Turning the Pacific: the Coral Sea, Midway, Guadalcanal, and the island hopping strategy",
  10: "Closing on Japan: the submarine blockade, the firebombing, Iwo Jima, and Okinawa",
  11: "The claims of democracy: Executive Order 8802, the Double V campaign, and service in a segregated military",
  12: "Internment: Executive Order 9066, the removal and the camps, Korematsu, and Japanese American service",
  13: "The Holocaust: persecution, the Nuremberg Laws, the ghettos, and the Final Solution",
  14: "Knowledge and reckoning: the refugees refused, liberation and documentation, the war's other crimes, and Nuremberg",
  15: "Victory and the atomic reckoning: Yalta and Potsdam, the atomic decision, the surrender, the costs, and the transformed nation"
};

window.HCG_WW2_LESSONS = [
  { n: 1, title: "The Road to War: Neutrality and Its Critics", question: "Between 1935 and 1941, how did the United States move from legislated neutrality toward war without declaring it?" },
  { n: 2, title: "Pearl Harbor and the Arsenal of Democracy", question: "What did the attack on Pearl Harbor settle, and what did it leave for Americans to decide?" },
  { n: 3, title: "Mobilizing the Home Front", question: "How did the United States turn a peacetime economy into the arsenal the war required, and who did the work?" },
  { n: 4, title: "The War in Europe and North Africa", question: "How did the Allies carry the war from North Africa to the surrender of Germany, and what did each stage cost?" },
  { n: 5, title: "The War in the Pacific", question: "How did the Allies cross the Pacific and close on Japan, and what did each step toward the home islands cost?" },
  { n: 6, title: "A War for Democracy? Exclusion, Internment, and Service", question: "How did a war fought in democracy's name test democracy at home, in who could work, who could serve, and who was imprisoned?" },
  { n: 7, title: "The Holocaust and the War's Crimes", question: "What did Nazi Germany do to the Jews of Europe and to others it marked for persecution and death, and what did the world know, do, and answer?" },
  { n: 8, title: "Victory and the Atomic Reckoning", question: "How did the war end, what did the atomic bomb decide and leave undecided, and what country came home from the war?" }
];

window.HCG_WW2_ITEMS = [
  // Lesson 1
  { id: "v1-reading", lesson: 1, kind: "Reading", name: "The Road to War: Neutrality and Its Critics", days: 1, tags: [1, 2], storage: "hcg/world-war-ii/lesson-01-reading.pdf", core: true },
  { id: "v1-notes", lesson: 1, kind: "Guided Notes", name: "Lesson 1 guided notes", days: 0, tags: [1, 2], storage: "hcg/world-war-ii/lesson-01-guided-notes.pdf", core: true },
  { id: "v1-activity", lesson: 1, kind: "Activity", name: "The Road in Ten Steps", days: 1, tags: [1, 2], storage: "hcg/world-war-ii/lesson-01-activity.pdf", core: true },
  { id: "v1-notebook", lesson: 1, kind: "Notebook", name: "The road chart", days: 0.5, tags: [1, 2], storage: "hcg/world-war-ii/lesson-01-notebook.pdf" },
  { id: "v1-quick", lesson: 1, kind: "Quick Check", name: "The Arsenal and the Law", days: 0.5, tags: [1, 2], storage: "hcg/world-war-ii/lesson-01-quick-check.pdf" },
  { id: "v1-writing", lesson: 1, kind: "Writing", name: "Neutral in Law, at War in Fact?", days: 1, tags: [1, 2], storage: "hcg/world-war-ii/lesson-01-writing.pdf" },
  // Lesson 2
  { id: "v2-reading", lesson: 2, kind: "Reading", name: "Pearl Harbor and the Arsenal of Democracy", days: 1, tags: [3, 4], storage: "hcg/world-war-ii/lesson-02-reading.pdf", core: true },
  { id: "v2-notes", lesson: 2, kind: "Guided Notes", name: "Lesson 2 guided notes", days: 0, tags: [3, 4], storage: "hcg/world-war-ii/lesson-02-guided-notes.pdf", core: true },
  { id: "v2-activity", lesson: 2, kind: "Activity", name: "Settled and Unsettled", days: 1, tags: [3, 4], storage: "hcg/world-war-ii/lesson-02-activity.pdf", core: true },
  { id: "v2-notebook", lesson: 2, kind: "Notebook", name: "Settled and open chart", days: 0.5, tags: [3, 4], storage: "hcg/world-war-ii/lesson-02-notebook.pdf" },
  { id: "v2-quick", lesson: 2, kind: "Quick Check", name: "The Harbor on Fire", days: 0.5, tags: [3, 4], storage: "hcg/world-war-ii/lesson-02-quick-check.pdf" },
  { id: "v2-writing", lesson: 2, kind: "Writing", name: "Settled and Undecided", days: 1, tags: [3, 4], storage: "hcg/world-war-ii/lesson-02-writing.pdf" },
  // Lesson 3
  { id: "v3-reading", lesson: 3, kind: "Reading", name: "Mobilizing the Home Front", days: 1, tags: [5, 6], storage: "hcg/world-war-ii/lesson-03-reading.pdf", core: true },
  { id: "v3-notes", lesson: 3, kind: "Guided Notes", name: "Lesson 3 guided notes", days: 0, tags: [5, 6], storage: "hcg/world-war-ii/lesson-03-guided-notes.pdf", core: true },
  { id: "v3-activity", lesson: 3, kind: "Activity", name: "The Conversion Desk", days: 1, tags: [5, 6], storage: "hcg/world-war-ii/lesson-03-activity.pdf", core: true },
  { id: "v3-notebook", lesson: 3, kind: "Notebook", name: "Part of the mobilization chart", days: 0.5, tags: [5, 6], storage: "hcg/world-war-ii/lesson-03-notebook.pdf" },
  { id: "v3-quick", lesson: 3, kind: "Quick Check", name: "The Arsenal at Work", days: 0.5, tags: [5, 6], storage: "hcg/world-war-ii/lesson-03-quick-check.pdf" },
  { id: "v3-writing", lesson: 3, kind: "Writing", name: "The Government That Ended the Depression", days: 1, tags: [5, 6], storage: "hcg/world-war-ii/lesson-03-writing.pdf" },
  // Lesson 4
  { id: "v4-reading", lesson: 4, kind: "Reading", name: "The War in Europe and North Africa", days: 1, tags: [7, 8], storage: "hcg/world-war-ii/lesson-04-reading.pdf", core: true },
  { id: "v4-notes", lesson: 4, kind: "Guided Notes", name: "Lesson 4 guided notes", days: 0, tags: [7, 8], storage: "hcg/world-war-ii/lesson-04-guided-notes.pdf", core: true },
  { id: "v4-activity", lesson: 4, kind: "Activity", name: "Five Maps, One War", days: 1, tags: [7, 8], storage: "hcg/world-war-ii/lesson-04-activity.pdf", core: true },
  { id: "v4-notebook", lesson: 4, kind: "Notebook", name: "Stage by stage chart", days: 0.5, tags: [7, 8], storage: "hcg/world-war-ii/lesson-04-notebook.pdf" },
  { id: "v4-quick", lesson: 4, kind: "Quick Check", name: "The Ramp at Omaha", days: 0.5, tags: [7, 8], storage: "hcg/world-war-ii/lesson-04-quick-check.pdf" },
  { id: "v4-writing", lesson: 4, kind: "Writing", name: "The Turning Point", days: 1, tags: [7, 8], storage: "hcg/world-war-ii/lesson-04-writing.pdf" },
  // Lesson 5
  { id: "v5-reading", lesson: 5, kind: "Reading", name: "The War in the Pacific", days: 1, tags: [9, 10], storage: "hcg/world-war-ii/lesson-05-reading.pdf", core: true },
  { id: "v5-notes", lesson: 5, kind: "Guided Notes", name: "Lesson 5 guided notes", days: 0, tags: [9, 10], storage: "hcg/world-war-ii/lesson-05-guided-notes.pdf", core: true },
  { id: "v5-activity", lesson: 5, kind: "Activity", name: "The Stepping Stone Ledger", days: 1, tags: [9, 10], storage: "hcg/world-war-ii/lesson-05-activity.pdf", core: true },
  { id: "v5-notebook", lesson: 5, kind: "Notebook", name: "The stepping stone chart", days: 0.5, tags: [9, 10], storage: "hcg/world-war-ii/lesson-05-notebook.pdf" },
  { id: "v5-quick", lesson: 5, kind: "Quick Check", name: "The Fleet Under Attack", days: 0.5, tags: [9, 10], storage: "hcg/world-war-ii/lesson-05-quick-check.pdf" },
  { id: "v5-writing", lesson: 5, kind: "Writing", name: "Another Way to End the War", days: 1, tags: [9, 10], storage: "hcg/world-war-ii/lesson-05-writing.pdf" },
  // Lesson 6
  { id: "v6-reading", lesson: 6, kind: "Reading", name: "A War for Democracy? Exclusion, Internment, and Service", days: 1, tags: [11, 12], storage: "hcg/world-war-ii/lesson-06-reading.pdf", core: true },
  { id: "v6-notes", lesson: 6, kind: "Guided Notes", name: "Lesson 6 guided notes", days: 0, tags: [11, 12], storage: "hcg/world-war-ii/lesson-06-guided-notes.pdf", core: true },
  { id: "v6-activity", lesson: 6, kind: "Activity", name: "The Contradiction File", days: 1, tags: [11, 12], storage: "hcg/world-war-ii/lesson-06-activity.pdf", core: true },
  { id: "v6-notebook", lesson: 6, kind: "Notebook", name: "Claim by claim chart", days: 0.5, tags: [11, 12], storage: "hcg/world-war-ii/lesson-06-notebook.pdf" },
  { id: "v6-quick", lesson: 6, kind: "Quick Check", name: "The Flag and the Bus", days: 0.5, tags: [11, 12], storage: "hcg/world-war-ii/lesson-06-quick-check.pdf" },
  { id: "v6-writing", lesson: 6, kind: "Writing", name: "Did the War Years Advance Freedom at Home?", days: 1, tags: [11, 12], storage: "hcg/world-war-ii/lesson-06-writing.pdf" },
  // Lesson 7
  { id: "v7-reading", lesson: 7, kind: "Reading", name: "The Holocaust and the War's Crimes", days: 1, tags: [13, 14], storage: "hcg/world-war-ii/lesson-07-reading.pdf", core: true },
  { id: "v7-notes", lesson: 7, kind: "Guided Notes", name: "Lesson 7 guided notes", days: 0, tags: [13, 14], storage: "hcg/world-war-ii/lesson-07-guided-notes.pdf", core: true },
  { id: "v7-activity", lesson: 7, kind: "Activity", name: "The Record and the Response", days: 1, tags: [13, 14], storage: "hcg/world-war-ii/lesson-07-activity.pdf", core: true },
  { id: "v7-notebook", lesson: 7, kind: "Notebook", name: "The record and response chart", days: 0.5, tags: [13, 14], storage: "hcg/world-war-ii/lesson-07-notebook.pdf" },
  { id: "v7-quick", lesson: 7, kind: "Quick Check", name: "First-Hand Evidence", days: 0.5, tags: [13, 14], storage: "hcg/world-war-ii/lesson-07-quick-check.pdf" },
  { id: "v7-writing", lesson: 7, kind: "Writing", name: "Knowledge and Response", days: 1, tags: [13, 14], storage: "hcg/world-war-ii/lesson-07-writing.pdf" },
  // Lesson 8
  { id: "v8-reading", lesson: 8, kind: "Reading", name: "Victory and the Atomic Reckoning", days: 1, tags: [15], storage: "hcg/world-war-ii/lesson-08-reading.pdf", core: true },
  { id: "v8-notes", lesson: 8, kind: "Guided Notes", name: "Lesson 8 guided notes", days: 0, tags: [15], storage: "hcg/world-war-ii/lesson-08-guided-notes.pdf", core: true },
  { id: "v8-activity", lesson: 8, kind: "Activity", name: "The Decision File", days: 1, tags: [15], storage: "hcg/world-war-ii/lesson-08-activity.pdf", core: true },
  { id: "v8-notebook", lesson: 8, kind: "Notebook", name: "The questions of 1945 chart", days: 0.5, tags: [15], storage: "hcg/world-war-ii/lesson-08-notebook.pdf" },
  { id: "v8-quick", lesson: 8, kind: "Quick Check", name: "The Signing Aboard the Missouri", days: 0.5, tags: [15], storage: "hcg/world-war-ii/lesson-08-quick-check.pdf" },
  { id: "v8-writing", lesson: 8, kind: "Writing", name: "Judging the Atomic Decision", days: 1, tags: [15], storage: "hcg/world-war-ii/lesson-08-writing.pdf" },
  // Review day
  { id: "vrev-guide", lesson: 9, kind: "Review", name: "Study guide (review day)", days: 1, tags: [], storage: "hcg/world-war-ii/review-study-guide.pdf", core: true },
  { id: "vrev-cross", lesson: 9, kind: "Review", name: "Crossword (50 answers)", days: 0.5, tags: [], storage: "hcg/world-war-ii/review-crossword.pdf" }
];

window.HCG_WW2_TOPICS = {
  1: { label: "The road to war and American entry", note: "" },
  2: { label: "Mobilization and the home front", note: "" },
  3: { label: "The global war: Europe and the Pacific", note: "" },
  4: { label: "Democracy tested at home", note: "" },
  5: { label: "Atrocity, the Holocaust, and war crimes", note: "" },
  6: { label: "Victory, cost, and transformation", note: "" }
};
window.HCG_WW2_BP_TOPIC = {
  1: [1], 2: [1], 3: [1], 4: [1, 3], 5: [2], 6: [2, 4], 7: [3], 8: [3], 9: [3], 10: [3, 6], 11: [4], 12: [4], 13: [5], 14: [5], 15: [6, 1]
};

// TPSP picker index for World War II: the unit's premium DBQ (dbq20,
// era "World War II" in the TPSP premium catalog, verified in Firestore
// with all seven of its documents present in the era file) first, then
// the four records the Depression and New Deal picker left untagged
// because they belong to this unit (the "Quarantine" speech, the Four
// Freedoms address, Executive Order 8802, and the "Arsenal of Democracy"
// fireside chat, from the TPSP depression era file, tagged here), then
// the era sources from the TPSP library file wwii.json in file order,
// each with conservative blueprint pre-tags where the source names the
// entry's content. Audio sources are excluded, as in the other units.
window.HCG_TPSP_WW2 = [
 {
  "id": "dbq20",
  "title": "Did World War II Advance Freedom at Home as Well as Abroad?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project \u00b7 premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true
 },
 {
  "id": "four-freedoms",
  "title": "Four Freedoms Speech (excerpt)",
  "type": "Speech",
  "meta": "Franklin D. Roosevelt \u00b7 1941",
  "url": "https://tpsp.web.app/library?q=Four%20Freedoms%20Speech%20%28excerpt%29",
  "bp": [
   2
  ]
 },
 {
  "id": "executive-order-8802-1941",
  "title": "Executive Order 8802 (excerpt)",
  "type": "Government document",
  "meta": "Franklin D. Roosevelt \u00b7 1941",
  "url": "https://tpsp.web.app/library?q=Executive%20Order%208802%20%28excerpt%29",
  "bp": [
   11
  ]
 },
 {
  "id": "fdr-arsenal-of-democracy-1940",
  "title": "\"Arsenal of Democracy\" Fireside Chat (excerpt)",
  "type": "Speech",
  "meta": "Franklin D. Roosevelt \u00b7 1940",
  "url": "https://tpsp.web.app/library?q=%22Arsenal%20of%20Democracy%22%20Fireside%20Chat%20%28excerpt%29",
  "bp": [
   2
  ]
 },
 {
  "id": "fdr-quarantine-speech-1937",
  "title": "\"Quarantine\" Speech (excerpt)",
  "type": "Speech",
  "meta": "Franklin D. Roosevelt \u00b7 1937",
  "url": "https://tpsp.web.app/library?q=%22Quarantine%22%20Speech%20%28excerpt%29",
  "bp": [
   1
  ]
 },
 {
  "id": "fdr-pearl-harbor-address-1941",
  "title": "Pearl Harbor Address to Congress (excerpt)",
  "type": "Speech",
  "meta": "Franklin D. Roosevelt \u00b7 1941",
  "url": "https://tpsp.web.app/library?q=Pearl%20Harbor%20Address%20to%20Congress%20%28excerpt%29",
  "bp": [
   3
  ]
 },
 {
  "id": "munson-report-1941",
  "title": "Munson Report on Japanese Americans (excerpt)",
  "type": "Government document",
  "meta": "Curtis B. Munson \u00b7 1941",
  "url": "https://tpsp.web.app/library?q=Munson%20Report%20on%20Japanese%20Americans%20%28excerpt%29",
  "bp": [
   12
  ]
 },
 {
  "id": "executive-order-9066",
  "title": "Executive Order 9066 (excerpt)",
  "type": "Government document",
  "meta": "Franklin D. Roosevelt \u00b7 1942",
  "url": "https://tpsp.web.app/library?q=Executive%20Order%209066%20%28excerpt%29",
  "bp": [
   12
  ]
 },
 {
  "id": "public-law-77-503-1942",
  "title": "An Act of March 21, 1942 (Public Law 77-503, operative provision)",
  "type": "Government document",
  "meta": "U.S. Congress \u00b7 1942",
  "url": "https://tpsp.web.app/library?q=An%20Act%20of%20March%2021%2C%201942%20%28Public%20Law%2077-503%2C%20operative%20provision%29",
  "bp": [
   12
  ]
 },
 {
  "id": "mochida-children-evacuation-bus-1942",
  "title": "\"Two children of the Mochida family . . . awaiting evacuation bus\" (photograph)",
  "type": "Photograph",
  "meta": "Dorothea Lange / War Relocation Authority \u00b7 1942",
  "url": "https://tpsp.web.app/library?q=%22Two%20children%20of%20the%20Mochida%20family%20.%20.%20.%20awaiting%20evacuation%20bus%22%20%28photograph%29",
  "bp": [
   12
  ]
 },
 {
  "id": "parks-american-gothic-1942",
  "title": "\"American Gothic\" (photograph)",
  "type": "Photograph",
  "meta": "Gordon Parks \u00b7 1942",
  "url": "https://tpsp.web.app/library?q=%22American%20Gothic%22%20%28photograph%29",
  "bp": [
   11
  ]
 },
 {
  "id": "howard-americans-in-concentration-camps-1942",
  "title": "\"Americans in Concentration Camps\" (excerpt)",
  "type": "Other",
  "meta": "Harry Paxton Howard \u00b7 1942",
  "url": "https://tpsp.web.app/library?q=%22Americans%20in%20Concentration%20Camps%22%20%28excerpt%29",
  "bp": [
   12
  ]
 },
 {
  "id": "miller-we-can-do-it-1943",
  "title": "\"We Can Do It!\" (poster)",
  "type": "Poster",
  "meta": "J. Howard Miller \u00b7 1943",
  "url": "https://tpsp.web.app/library?q=%22We%20Can%20Do%20It%21%22%20%28poster%29",
  "bp": [
   6
  ]
 },
 {
  "id": "sargent-into-the-jaws-of-death-1944",
  "title": "\"Into the Jaws of Death\" (photograph)",
  "type": "Photograph",
  "meta": "Robert F. Sargent \u00b7 1944",
  "url": "https://tpsp.web.app/library?q=%22Into%20the%20Jaws%20of%20Death%22%20%28photograph%29",
  "bp": [
   8
  ]
 },
 {
  "id": "korematsu-majority-opinion-1944",
  "title": "Korematsu v. United States, majority opinion (excerpt)",
  "type": "Court decision",
  "meta": "Justice Hugo Black \u00b7 1944",
  "url": "https://tpsp.web.app/library?q=Korematsu%20v.%20United%20States%2C%20majority%20opinion%20%28excerpt%29",
  "bp": [
   12
  ]
 },
 {
  "id": "eisenhower-in-case-of-failure-1944",
  "title": "\"In Case of Failure\" message (full text)",
  "type": "Government document",
  "meta": "Dwight D. Eisenhower \u00b7 1944",
  "url": "https://tpsp.web.app/library?q=%22In%20Case%20of%20Failure%22%20message%20%28full%20text%29",
  "bp": [
   8
  ]
 },
 {
  "id": "gi-bill-1944",
  "title": "Servicemen's Readjustment Act of 1944 (\"G.I. Bill,\" excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress \u00b7 1944",
  "url": "https://tpsp.web.app/library?q=Servicemen%27s%20Readjustment%20Act%20of%201944%20%28%22G.I.%20Bill%2C%22%20excerpt%29",
  "bp": [
   15
  ]
 },
 {
  "id": "atlantic-charter-1941",
  "title": "The Atlantic Charter",
  "type": "Government document",
  "meta": "Franklin D. Roosevelt and Winston Churchill \u00b7 1941",
  "url": "https://tpsp.web.app/library?q=The%20Atlantic%20Charter",
  "bp": [
   2
  ]
 },
 {
  "id": "eisenhower-order-of-the-day-1944",
  "title": "Order of the Day (\"Great Crusade\") (excerpt)",
  "type": "Government document",
  "meta": "Dwight D. Eisenhower \u00b7 1944",
  "url": "https://tpsp.web.app/library?q=Order%20of%20the%20Day%20%28%22Great%20Crusade%22%29%20%28excerpt%29",
  "bp": [
   8
  ]
 },
 {
  "id": "fdr-d-day-prayer-1944",
  "title": "D-Day Prayer (excerpt)",
  "type": "Speech",
  "meta": "Franklin D. Roosevelt \u00b7 1944",
  "url": "https://tpsp.web.app/library?q=D-Day%20Prayer%20%28excerpt%29",
  "bp": [
   8
  ]
 },
 {
  "id": "fdr-second-bill-of-rights-1944",
  "title": "\"Second Bill of Rights\" (State of the Union, excerpt)",
  "type": "Speech",
  "meta": "Franklin D. Roosevelt \u00b7 1944",
  "url": "https://tpsp.web.app/library?q=%22Second%20Bill%20of%20Rights%22%20%28State%20of%20the%20Union%2C%20excerpt%29",
  "bp": [
   15
  ]
 },
 {
  "id": "franck-report-1945",
  "title": "Report of the Committee on Political and Social Problems (\"Franck Report\") (excerpt)",
  "type": "Government document",
  "meta": "Committee on Political and Social Problems, Manhattan Project (chaired by James Franck) \u00b7 1945",
  "url": "https://tpsp.web.app/library?q=Report%20of%20the%20Committee%20on%20Political%20and%20Social%20Problems%20%28%22Franck%20Report%22%29%20%28excerpt%29",
  "bp": [
   15
  ]
 },
 {
  "id": "jackson-nuremberg-opening-1945",
  "title": "Opening Statement at the Nuremberg Trial (excerpt)",
  "type": "Speech",
  "meta": "Robert H. Jackson \u00b7 1945",
  "url": "https://tpsp.web.app/library?q=Opening%20Statement%20at%20the%20Nuremberg%20Trial%20%28excerpt%29",
  "bp": [
   14
  ]
 },
 {
  "id": "lend-lease-act-1941",
  "title": "Lend-Lease Act (excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress \u00b7 1941",
  "url": "https://tpsp.web.app/library?q=Lend-Lease%20Act%20%28excerpt%29",
  "bp": [
   2
  ]
 },
 {
  "id": "negroes-and-the-war-1942",
  "title": "\"Negroes and the War\" (excerpt)",
  "type": "Government document",
  "meta": "Chandler Owen \u00b7 1942",
  "url": "https://tpsp.web.app/library?q=%22Negroes%20and%20the%20War%22%20%28excerpt%29",
  "bp": [
   11
  ]
 },
 {
  "id": "potsdam-declaration-1945",
  "title": "Potsdam Declaration (excerpt)",
  "type": "Government document",
  "meta": "United States, United Kingdom, and China \u00b7 1945",
  "url": "https://tpsp.web.app/library?q=Potsdam%20Declaration%20%28excerpt%29",
  "bp": [
   15
  ]
 },
 {
  "id": "truman-hiroshima-statement-1945",
  "title": "Statement Announcing the Use of the A-Bomb at Hiroshima (excerpt)",
  "type": "Government document",
  "meta": "Harry S. Truman \u00b7 1945",
  "url": "https://tpsp.web.app/library?q=Statement%20Announcing%20the%20Use%20of%20the%20A-Bomb%20at%20Hiroshima%20%28excerpt%29",
  "bp": [
   15
  ]
 },
 {
  "id": "japanese-instrument-of-surrender-1945",
  "title": "Japanese Instrument of Surrender (excerpt)",
  "type": "Government document",
  "meta": "Empire of Japan and the Allied Powers \u00b7 1945",
  "url": "https://tpsp.web.app/library?q=Japanese%20Instrument%20of%20Surrender%20%28excerpt%29",
  "bp": [
   15
  ]
 },
 {
  "id": "eisenhower-ohrdruf-letter-1945",
  "title": "Eisenhower's Ohrdruf Cable to Marshall (excerpt)",
  "type": "Government document",
  "meta": "Dwight D. Eisenhower \u00b7 1945",
  "url": "https://tpsp.web.app/library?q=Eisenhower%27s%20Ohrdruf%20Cable%20to%20Marshall%20%28excerpt%29",
  "bp": [
   14
  ]
 },
 {
  "id": "hersey-hiroshima-1946",
  "title": "Hiroshima (excerpt)",
  "type": "Book",
  "meta": "John Hersey \u00b7 1946",
  "url": "https://tpsp.web.app/library?q=Hiroshima%20%28excerpt%29",
  "bp": [
   15
  ]
 }
];

window.HCG_CW_BLUEPRINT = {
  1: "Origins: the wartime alliance breaks, the Long Telegram, and the Iron Curtain speech",
  2: "Containment as policy: the Truman Doctrine, the Marshall Plan, the Berlin Airlift, and NATO",
  3: "The Cold War turns to Asia: Communist victory in China, the Soviet bomb, and NSC-68",
  4: "Korea: intervention under the United Nations, Inchon, Chinese intervention, MacArthur's dismissal, and the armistice",
  5: "The machinery of fear: the loyalty program, HUAC and the Hollywood Ten, the blacklist, and the spy cases",
  6: "McCarthy and his fall: the Wheeling speech, McCarthyism, the Army-McCarthy hearings, and the censure",
  7: "The nuclear arms race: the hydrogen bomb, massive retaliation, brinkmanship, and the fear at home",
  8: "The contest widens: covert action in Iran and Guatemala, the Warsaw Pact, Sputnik and the space race",
  9: "Cuba before the crisis: Castro's revolution, the turn to Moscow, and the Bay of Pigs",
  10: "Thirteen days: the missile crisis, the quarantine, the two-part settlement, the hotline, and the test ban",
  11: "Into Vietnam: the domino theory, the Gulf of Tonkin Resolution, and escalation",
  12: "The war turns: the Tet Offensive, Vietnamization, the accords, the fall of Saigon, and the costs",
  13: "Détente and its critics: China, SALT, Helsinki and human rights, and the Afghanistan shock",
  14: "The second Cold War: the buildup, the Reagan Doctrine, the \"evil empire,\" and the Strategic Defense Initiative",
  15: "The end: Gorbachev, glasnost and perestroika, 1989, reunification, and the dissolution of 1991"
};

window.HCG_CW_LESSONS = [
  { n: 1, title: "Allies to Adversaries: Containment Takes Shape", question: "How did wartime allies become rivals, and what strategy did the United States adopt to meet the Soviet Union?" },
  { n: 2, title: "The Cold War in Asia: China and Korea", question: "How did the Cold War turn into a shooting war in Asia, and why did Korea end without victory?" },
  { n: 3, title: "The Red Scare at Home", question: "How did the fear of communism change American life at home, and what ended the scare?" },
  { n: 4, title: "Brinkmanship and the Nuclear Shadow", question: "How did nuclear weapons change the rules of the rivalry, and how close did brinkmanship bring the world to war?" },
  { n: 5, title: "Cuba: Revolution and the Missile Crisis", question: "Why did the Soviet Union put missiles in Cuba, and how did thirteen days in October 1962 change the Cold War?" },
  { n: 6, title: "Vietnam: The War Containment Built", question: "How did containment lead the United States into Vietnam, and why did the war fail on its own terms?" },
  { n: 7, title: "Détente, Human Rights, and the Evil Empire", question: "Why did the rivals try to ease the Cold War in the 1970s, and why did the confrontation return in the 1980s?" },
  { n: 8, title: "The Wall Falls: The Cold War Ends", question: "Why did the Cold War end between 1989 and 1991, and what did its ending settle and leave unsettled?" }
];

window.HCG_CW_ITEMS = [
  // Lesson 1
  { id: "c1-reading", lesson: 1, kind: "Reading", name: "Allies to Adversaries: Containment Takes Shape", days: 1, tags: [1, 2], storage: "hcg/cold-war/lesson-01-reading.pdf", core: true },
  { id: "c1-notes", lesson: 1, kind: "Guided Notes", name: "Lesson 1 guided notes", days: 0, tags: [1, 2], storage: "hcg/cold-war/lesson-01-guided-notes.pdf", core: true },
  { id: "c1-activity", lesson: 1, kind: "Activity", name: "The Strategy Desk", days: 1, tags: [1, 2], storage: "hcg/cold-war/lesson-01-activity.pdf", core: true },
  { id: "c1-notebook", lesson: 1, kind: "Notebook", name: "Step by step chart", days: 0.5, tags: [1, 2], storage: "hcg/cold-war/lesson-01-notebook.pdf" },
  { id: "c1-quick", lesson: 1, kind: "Quick Check", name: "The Doctrine and the Line", days: 0.5, tags: [1, 2], storage: "hcg/cold-war/lesson-01-quick-check.pdf" },
  { id: "c1-writing", lesson: 1, kind: "Writing", name: "A Doctrine Without Borders?", days: 1, tags: [1, 2], storage: "hcg/cold-war/lesson-01-writing.pdf" },
  // Lesson 2
  { id: "c2-reading", lesson: 2, kind: "Reading", name: "The Cold War in Asia: China and Korea", days: 1, tags: [3, 4], storage: "hcg/cold-war/lesson-02-reading.pdf", core: true },
  { id: "c2-notes", lesson: 2, kind: "Guided Notes", name: "Lesson 2 guided notes", days: 0, tags: [3, 4], storage: "hcg/cold-war/lesson-02-guided-notes.pdf", core: true },
  { id: "c2-activity", lesson: 2, kind: "Activity", name: "The Limited War File", days: 1, tags: [3, 4], storage: "hcg/cold-war/lesson-02-activity.pdf", core: true },
  { id: "c2-notebook", lesson: 2, kind: "Notebook", name: "Decision point chart", days: 0.5, tags: [3, 4], storage: "hcg/cold-war/lesson-02-notebook.pdf" },
  { id: "c2-quick", lesson: 2, kind: "Quick Check", name: "The Reservoir in Winter", days: 0.5, tags: [3, 4], storage: "hcg/cold-war/lesson-02-quick-check.pdf" },
  { id: "c2-writing", lesson: 2, kind: "Writing", name: "Won, Lost, or Settled", days: 1, tags: [3, 4], storage: "hcg/cold-war/lesson-02-writing.pdf" },
  // Lesson 3
  { id: "c3-reading", lesson: 3, kind: "Reading", name: "The Red Scare at Home", days: 1, tags: [5, 6], storage: "hcg/cold-war/lesson-03-reading.pdf", core: true },
  { id: "c3-notes", lesson: 3, kind: "Guided Notes", name: "Lesson 3 guided notes", days: 0, tags: [5, 6], storage: "hcg/cold-war/lesson-03-guided-notes.pdf", core: true },
  { id: "c3-activity", lesson: 3, kind: "Activity", name: "The Investigation File", days: 1, tags: [5, 6], storage: "hcg/cold-war/lesson-03-activity.pdf", core: true },
  { id: "c3-notebook", lesson: 3, kind: "Notebook", name: "Part of the scare chart", days: 0.5, tags: [5, 6], storage: "hcg/cold-war/lesson-03-notebook.pdf" },
  { id: "c3-quick", lesson: 3, kind: "Quick Check", name: "Decency on Television", days: 0.5, tags: [5, 6], storage: "hcg/cold-war/lesson-03-quick-check.pdf" },
  { id: "c3-writing", lesson: 3, kind: "Writing", name: "Judging the Scare", days: 1, tags: [5, 6], storage: "hcg/cold-war/lesson-03-writing.pdf" },
  // Lesson 4
  { id: "c4-reading", lesson: 4, kind: "Reading", name: "Brinkmanship and the Nuclear Shadow", days: 1, tags: [7, 8], storage: "hcg/cold-war/lesson-04-reading.pdf", core: true },
  { id: "c4-notes", lesson: 4, kind: "Guided Notes", name: "Lesson 4 guided notes", days: 0, tags: [7, 8], storage: "hcg/cold-war/lesson-04-guided-notes.pdf", core: true },
  { id: "c4-activity", lesson: 4, kind: "Activity", name: "The Brink File", days: 1, tags: [7, 8], storage: "hcg/cold-war/lesson-04-activity.pdf", core: true },
  { id: "c4-notebook", lesson: 4, kind: "Notebook", name: "Stage by stage chart", days: 0.5, tags: [7, 8], storage: "hcg/cold-war/lesson-04-notebook.pdf" },
  { id: "c4-quick", lesson: 4, kind: "Quick Check", name: "The Cloud over Enewetak", days: 0.5, tags: [7, 8], storage: "hcg/cold-war/lesson-04-quick-check.pdf" },
  { id: "c4-writing", lesson: 4, kind: "Writing", name: "Peace at the Edge", days: 1, tags: [7, 8], storage: "hcg/cold-war/lesson-04-writing.pdf" },
  // Lesson 5
  { id: "c5-reading", lesson: 5, kind: "Reading", name: "Cuba: Revolution and the Missile Crisis", days: 1, tags: [9, 10], storage: "hcg/cold-war/lesson-05-reading.pdf", core: true },
  { id: "c5-notes", lesson: 5, kind: "Guided Notes", name: "Lesson 5 guided notes", days: 0, tags: [9, 10], storage: "hcg/cold-war/lesson-05-guided-notes.pdf", core: true },
  { id: "c5-activity", lesson: 5, kind: "Activity", name: "The Thirteen Days File", days: 1, tags: [9, 10], storage: "hcg/cold-war/lesson-05-activity.pdf", core: true },
  { id: "c5-notebook", lesson: 5, kind: "Notebook", name: "The thirteen days chart", days: 0.5, tags: [9, 10], storage: "hcg/cold-war/lesson-05-notebook.pdf" },
  { id: "c5-quick", lesson: 5, kind: "Quick Check", name: "The Photograph and the Line", days: 0.5, tags: [9, 10], storage: "hcg/cold-war/lesson-05-quick-check.pdf" },
  { id: "c5-writing", lesson: 5, kind: "Writing", name: "Which Letter Mattered More?", days: 1, tags: [9, 10], storage: "hcg/cold-war/lesson-05-writing.pdf" },
  // Lesson 6
  { id: "c6-reading", lesson: 6, kind: "Reading", name: "Vietnam: The War Containment Built", days: 1, tags: [11, 12], storage: "hcg/cold-war/lesson-06-reading.pdf", core: true },
  { id: "c6-notes", lesson: 6, kind: "Guided Notes", name: "Lesson 6 guided notes", days: 0, tags: [11, 12], storage: "hcg/cold-war/lesson-06-guided-notes.pdf", core: true },
  { id: "c6-activity", lesson: 6, kind: "Activity", name: "The Escalation Ledger", days: 1, tags: [11, 12], storage: "hcg/cold-war/lesson-06-activity.pdf", core: true },
  { id: "c6-notebook", lesson: 6, kind: "Notebook", name: "The escalation chart", days: 0.5, tags: [11, 12], storage: "hcg/cold-war/lesson-06-notebook.pdf" },
  { id: "c6-quick", lesson: 6, kind: "Quick Check", name: "The First Capsule", days: 0.5, tags: [11, 12], storage: "hcg/cold-war/lesson-06-quick-check.pdf" },
  { id: "c6-writing", lesson: 6, kind: "Writing", name: "Why Did the War Fail on Its Own Terms?", days: 1, tags: [11, 12], storage: "hcg/cold-war/lesson-06-writing.pdf" },
  // Lesson 7
  { id: "c7-reading", lesson: 7, kind: "Reading", name: "Détente, Human Rights, and the Evil Empire", days: 1, tags: [13, 14], storage: "hcg/cold-war/lesson-07-reading.pdf", core: true },
  { id: "c7-notes", lesson: 7, kind: "Guided Notes", name: "Lesson 7 guided notes", days: 0, tags: [13, 14], storage: "hcg/cold-war/lesson-07-guided-notes.pdf", core: true },
  { id: "c7-activity", lesson: 7, kind: "Activity", name: "The Summit File", days: 1, tags: [13, 14], storage: "hcg/cold-war/lesson-07-activity.pdf", core: true },
  { id: "c7-notebook", lesson: 7, kind: "Notebook", name: "Direction of the contest chart", days: 0.5, tags: [13, 14], storage: "hcg/cold-war/lesson-07-notebook.pdf" },
  { id: "c7-quick", lesson: 7, kind: "Quick Check", name: "Naming the Adversary", days: 0.5, tags: [13, 14], storage: "hcg/cold-war/lesson-07-quick-check.pdf" },
  { id: "c7-writing", lesson: 7, kind: "Writing", name: "Why Détente Ended", days: 1, tags: [13, 14], storage: "hcg/cold-war/lesson-07-writing.pdf" },
  // Lesson 8
  { id: "c8-reading", lesson: 8, kind: "Reading", name: "The Wall Falls: The Cold War Ends", days: 1, tags: [15], storage: "hcg/cold-war/lesson-08-reading.pdf", core: true },
  { id: "c8-notes", lesson: 8, kind: "Guided Notes", name: "Lesson 8 guided notes", days: 0, tags: [15], storage: "hcg/cold-war/lesson-08-guided-notes.pdf", core: true },
  { id: "c8-activity", lesson: 8, kind: "Activity", name: "The End in Sequence", days: 1, tags: [15], storage: "hcg/cold-war/lesson-08-activity.pdf", core: true },
  { id: "c8-notebook", lesson: 8, kind: "Notebook", name: "What was decided chart", days: 0.5, tags: [15], storage: "hcg/cold-war/lesson-08-notebook.pdf" },
  { id: "c8-quick", lesson: 8, kind: "Quick Check", name: "Crowds at the Brandenburg Gate", days: 0.5, tags: [15], storage: "hcg/cold-war/lesson-08-quick-check.pdf" },
  { id: "c8-writing", lesson: 8, kind: "Writing", name: "Why the Cold War Ended When It Did", days: 1, tags: [15], storage: "hcg/cold-war/lesson-08-writing.pdf" },
  // Review day
  { id: "crev-guide", lesson: 9, kind: "Review", name: "Study guide (review day)", days: 1, tags: [], storage: "hcg/cold-war/review-study-guide.pdf", core: true },
  { id: "crev-cross", lesson: 9, kind: "Review", name: "Crossword (56 answers)", days: 0.5, tags: [], storage: "hcg/cold-war/review-crossword.pdf" }
];

window.HCG_CW_TOPICS = {
  1: { label: "Origins and containment: the strategy takes shape", note: "" },
  2: { label: "Asia and the wars of containment", note: "" },
  3: { label: "Fear at home: anticommunism and American freedom", note: "" },
  4: { label: "The nuclear arms race and the shadow it cast", note: "" },
  5: { label: "Challenge and response: Cuba, Vietnam, détente, and the renewed confrontation", note: "" },
  6: { label: "The Cold War ends: reform, collapse, and legacy", note: "" }
};
window.HCG_CW_BP_TOPIC = {
  1: [1], 2: [1], 3: [1, 2], 4: [2], 5: [3], 6: [3], 7: [4], 8: [4, 5], 9: [5], 10: [4, 5], 11: [2, 5], 12: [2, 5], 13: [5], 14: [4, 5], 15: [6]
};

// TPSP picker index for The Cold War: the unit's premium DBQ (dbq21,
// era "The Cold War" in the TPSP premium catalog, catalog code DBQ196,
// verified in Firestore with all seven of its documents present in the
// era file) first, then the era sources from the TPSP library file
// cold-war.json in file order, each with conservative blueprint
// pre-tags where the source names the entry's content. Audio sources
// are excluded, as in the other units.
window.HCG_TPSP_CW = [
 {
  "id": "dbq21",
  "title": "Did Containment Serve American Interests?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project \u00b7 premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true
 },
 {
  "id": "truman-doctrine",
  "title": "Truman Doctrine Address",
  "type": "Speech",
  "meta": "Harry S. Truman \u00b7 1947",
  "url": "https://tpsp.web.app/library?q=Truman%20Doctrine%20Address",
  "bp": [
   2
  ]
 },
 {
  "id": "executive-order-9981-1948",
  "title": "Executive Order 9981",
  "type": "Government document",
  "meta": "Harry S. Truman \u00b7 1948",
  "url": "https://tpsp.web.app/library?q=Executive%20Order%209981"
 },
 {
  "id": "duck-and-cover-film-1951",
  "title": "\"Duck and Cover\" (Federal Civil Defense Administration film, 1951)",
  "type": "Government document",
  "meta": "Federal Civil Defense Administration \u00b7 1951",
  "url": "https://tpsp.web.app/library?q=%22Duck%20and%20Cover%22%20%28Federal%20Civil%20Defense%20Administration%20film%2C%201951%29",
  "bp": [
   7
  ]
 },
 {
  "id": "emmett-till-jet-photographs-1955",
  "title": "Jet magazine photographs of Emmett Till",
  "type": "Photograph",
  "meta": "David Jackson \u00b7 1955",
  "url": "https://tpsp.web.app/library?q=Jet%20magazine%20photographs%20of%20Emmett%20Till"
 },
 {
  "id": "eisenhower-little-rock-address-1957",
  "title": "Radio and television address on the Little Rock crisis",
  "type": "Speech",
  "meta": "Dwight D. Eisenhower \u00b7 1957",
  "url": "https://tpsp.web.app/library?q=Radio%20and%20television%20address%20on%20the%20Little%20Rock%20crisis"
 },
 {
  "id": "faubus-little-rock-statement-1957",
  "title": "Statement on the Little Rock crisis",
  "type": "Speech",
  "meta": "Orval Faubus \u00b7 1957",
  "url": "https://tpsp.web.app/library?q=Statement%20on%20the%20Little%20Rock%20crisis"
 },
 {
  "id": "executive-order-10730-1957",
  "title": "Executive Order 10730",
  "type": "Government document",
  "meta": "Dwight D. Eisenhower \u00b7 1957",
  "url": "https://tpsp.web.app/library?q=Executive%20Order%2010730"
 },
 {
  "id": "kennedy-inaugural",
  "title": "Inaugural Address",
  "type": "Speech",
  "meta": "John F. Kennedy \u00b7 1961",
  "url": "https://tpsp.web.app/library?q=Inaugural%20Address"
 },
 {
  "id": "u2-cuban-missile-sites-1962",
  "title": "U-2 reconnaissance photo of Soviet missile sites in Cuba (photograph)",
  "type": "Photograph",
  "meta": "United States Air Force \u00b7 1962",
  "url": "https://tpsp.web.app/library?q=U-2%20reconnaissance%20photo%20of%20Soviet%20missile%20sites%20in%20Cuba%20%28photograph%29",
  "bp": [
   10
  ]
 },
 {
  "id": "khrushchev-letter-kennedy-1962",
  "title": "Letter to President Kennedy",
  "type": "Letter",
  "meta": "Nikita Khrushchev \u00b7 1962",
  "url": "https://tpsp.web.app/library?q=Letter%20to%20President%20Kennedy",
  "bp": [
   10
  ]
 },
 {
  "id": "kennedy-letter-khrushchev-1962",
  "title": "Letter to Chairman Khrushchev",
  "type": "Letter",
  "meta": "John F. Kennedy \u00b7 1962",
  "url": "https://tpsp.web.app/library?q=Letter%20to%20Chairman%20Khrushchev",
  "bp": [
   10
  ]
 },
 {
  "id": "dobrynin-cable-rfk-meeting-1962",
  "title": "Cable reporting the Robert Kennedy meeting",
  "type": "Government document",
  "meta": "Anatoly Dobrynin \u00b7 1962",
  "url": "https://tpsp.web.app/library?q=Cable%20reporting%20the%20Robert%20Kennedy%20meeting",
  "bp": [
   10
  ]
 },
 {
  "id": "gulf-of-tonkin-resolution-1964",
  "title": "Gulf of Tonkin Resolution (H.J. Res. 1145)",
  "type": "Government document",
  "meta": "U.S. Congress \u00b7 1964",
  "url": "https://tpsp.web.app/library?q=Gulf%20of%20Tonkin%20Resolution%20%28H.J.%20Res.%201145%29",
  "bp": [
   11
  ]
 },
 {
  "id": "bundy-memorandum-vietnam-1964",
  "title": "Draft Memorandum from the President's Special Assistant for National Security Affairs (Bundy) to the President",
  "type": "Government document",
  "meta": "McGeorge Bundy \u00b7 1964",
  "url": "https://tpsp.web.app/library?q=Draft%20Memorandum%20from%20the%20President%27s%20Special%20Assistant%20for%20National%20Security%20Affairs%20%28Bundy%29%20to%20the%20President",
  "bp": [
   11
  ]
 },
 {
  "id": "lbj-bundy-phone-conversation-1964",
  "title": "Recording of a telephone conversation between the President and McGeorge Bundy",
  "type": "Government document",
  "meta": "Lyndon B. Johnson and McGeorge Bundy \u00b7 1964",
  "url": "https://tpsp.web.app/library?q=Recording%20of%20a%20telephone%20conversation%20between%20the%20President%20and%20McGeorge%20Bundy",
  "bp": [
   11
  ]
 },
 {
  "id": "rfk-vietnam-letter-bayliss-1967",
  "title": "Robert Kennedy's Views on Vietnam, 1967 (letter to John F. Bayliss)",
  "type": "Letter",
  "meta": "Robert F. Kennedy \u00b7 1967",
  "url": "https://tpsp.web.app/library?q=Robert%20Kennedy%27s%20Views%20on%20Vietnam%2C%201967%20%28letter%20to%20John%20F.%20Bayliss%29",
  "bp": [
   12
  ]
 },
 {
  "id": "nasa-aldrin-moon-1969",
  "title": "Buzz Aldrin on the Moon (photograph)",
  "type": "Photograph",
  "meta": "NASA (Neil Armstrong) \u00b7 1969",
  "url": "https://tpsp.web.app/library?q=Buzz%20Aldrin%20on%20the%20Moon%20%28photograph%29",
  "bp": [
   8
  ]
 },
 {
  "id": "reagan-tear-down-this-wall",
  "title": "Remarks at the Brandenburg Gate",
  "type": "Speech",
  "meta": "Ronald Reagan \u00b7 1987",
  "url": "https://tpsp.web.app/library?q=Remarks%20at%20the%20Brandenburg%20Gate",
  "bp": [
   15
  ]
 },
 {
  "id": "corkran-berlin-wall-1989",
  "title": "Crowds at the Brandenburg Gate, Berlin, December 1989 (photograph)",
  "type": "Photograph",
  "meta": "SSgt. F. Lee Corkran, U.S. Air Force \u00b7 1989",
  "url": "https://tpsp.web.app/library?q=Crowds%20at%20the%20Brandenburg%20Gate%2C%20Berlin%2C%20December%201989%20%28photograph%29",
  "bp": [
   15
  ]
 },
 {
  "id": "lange-assignment-ill-never-forget-1960",
  "title": "\"The Assignment I'll Never Forget: Migrant Mother\" (excerpt)",
  "type": "Memoir",
  "meta": "Dorothea Lange \u00b7 1960",
  "url": "https://tpsp.web.app/library?q=%22The%20Assignment%20I%27ll%20Never%20Forget%3A%20Migrant%20Mother%22%20%28excerpt%29"
 },
 {
  "id": "kennan-long-telegram-1946",
  "title": "The \"Long Telegram\" (excerpt)",
  "type": "Government document",
  "meta": "George F. Kennan \u00b7 1946",
  "url": "https://tpsp.web.app/library?q=The%20%22Long%20Telegram%22%20%28excerpt%29",
  "bp": [
   1
  ]
 },
 {
  "id": "nsc-68-1950",
  "title": "NSC-68 (excerpt)",
  "type": "Government document",
  "meta": "National Security Council \u00b7 1950",
  "url": "https://tpsp.web.app/library?q=NSC-68%20%28excerpt%29",
  "bp": [
   3
  ]
 },
 {
  "id": "marshall-plan-harvard-address-1947",
  "title": "The Marshall Plan (Harvard Address) (excerpt)",
  "type": "Speech",
  "meta": "George C. Marshall \u00b7 1947",
  "url": "https://tpsp.web.app/library?q=The%20Marshall%20Plan%20%28Harvard%20Address%29%20%28excerpt%29",
  "bp": [
   2
  ]
 },
 {
  "id": "eisenhower-farewell-address-1961",
  "title": "Farewell Address (excerpt)",
  "type": "Speech",
  "meta": "Dwight D. Eisenhower \u00b7 1961",
  "url": "https://tpsp.web.app/library?q=Farewell%20Address%20%28excerpt%29"
 },
 {
  "id": "kennedy-cuba-missile-crisis-address-1962",
  "title": "Address on the Soviet Arms Buildup in Cuba (excerpt)",
  "type": "Speech",
  "meta": "John F. Kennedy \u00b7 1962",
  "url": "https://tpsp.web.app/library?q=Address%20on%20the%20Soviet%20Arms%20Buildup%20in%20Cuba%20%28excerpt%29",
  "bp": [
   10
  ]
 },
 {
  "id": "mccarthy-wheeling-speech-1950",
  "title": "Wheeling Speech on Communists in the State Department (excerpt)",
  "type": "Speech",
  "meta": "Joseph R. McCarthy \u00b7 1950",
  "url": "https://tpsp.web.app/library?q=Wheeling%20Speech%20on%20Communists%20in%20the%20State%20Department%20%28excerpt%29",
  "bp": [
   6
  ]
 },
 {
  "id": "nixon-resignation-address-1974",
  "title": "Resignation Address (excerpt)",
  "type": "Speech",
  "meta": "Richard Nixon \u00b7 1974",
  "url": "https://tpsp.web.app/library?q=Resignation%20Address%20%28excerpt%29"
 },
 {
  "id": "reagan-evil-empire-speech-1983",
  "title": "\"Evil Empire\" Speech (excerpt)",
  "type": "Speech",
  "meta": "Ronald Reagan \u00b7 1983",
  "url": "https://tpsp.web.app/library?q=%22Evil%20Empire%22%20Speech%20%28excerpt%29",
  "bp": [
   14
  ]
 }
];

window.HCG_CR_BLUEPRINT = {
  1: "The ground before: Jim Crow, disfranchisement, and the institutions Black Americans built",
  2: "The war's inheritance and the first federal steps: Double V, To Secure These Rights, and Executive Order 9981",
  3: "The legal strategy pays off: Houston, Marshall, and the Brown decision",
  4: "Massive resistance: Brown II, the Southern Manifesto, school closings, and Cooper v. Aaron",
  5: "Montgomery: the boycott, the MIA, King, and mass nonviolent protest",
  6: "Little Rock and Till: federal power against a governor, and a murder that showed the nation",
  7: "The students move: the sit-ins, Nashville, and SNCC",
  8: "Freedom Rides and Albany: testing federal enforcement and learning its limits",
  9: "Birmingham: the Letter, the Children's Crusade, and the pressure that moved Kennedy",
  10: "The March on Washington and the movement's public case",
  11: "The Civil Rights Act of 1964: the filibuster broken and what the act reached",
  12: "Selma and the Voting Rights Act of 1965",
  13: "The northern turn: de facto segregation, Chicago, and Watts",
  14: "Black Power and the last King: Malcolm X's inheritance, Carmichael, the Panthers, Memphis, and the assassination",
  15: "The reckoning: the Kerner verdict, the Fair Housing Act, busing, affirmative action, Bakke, and the unfinished agenda"
};

window.HCG_CR_LESSONS = [
  { n: 1, title: "Foundations: The Movement Before the Movement", question: "What had Black Americans already built, and already won, before the movement's famous decade began?" },
  { n: 2, title: "Brown and the Massive Resistance", question: "How did the NAACP turn a Kansas school case into the end of legal segregation, and how did the South answer?" },
  { n: 3, title: "Montgomery and Little Rock: The Movement Finds Its Tactics", question: "How did a bus boycott and nine schoolchildren teach the movement its methods, and force the federal government to act?" },
  { n: 4, title: "Sit-Ins and Freedom Rides: The Students Take the Lead", question: "How did students a decade younger than the movement's leaders change its pace, its tactics, and its demands?" },
  { n: 5, title: "Birmingham and the March on Washington", question: "How did Birmingham force the nation's hand, and what did the March on Washington ask the nation to become?" },
  { n: 6, title: "The Laws Change: 1964 and 1965", question: "How did the movement turn protest into law, and what could the two great acts actually reach?" },
  { n: 7, title: "The Movement Turns North and Inward: Chicago, Black Power, Memphis", question: "Why did the movement's methods stop working as it moved north, and how did its own people argue about what freedom required next?" },
  { n: 8, title: "Victory, Backlash, and the Unfinished Agenda", question: "What did the movement win, what answered it, and what was still undone when its famous decade ended?" }
];

window.HCG_CR_ITEMS = [
  // Lesson 1
  { id: "r1-reading", lesson: 1, kind: "Reading", name: "Foundations: The Movement Before the Movement", days: 1, tags: [1, 2], storage: "hcg/civil-rights/lesson-01-reading.pdf", core: true },
  { id: "r1-notes", lesson: 1, kind: "Guided Notes", name: "Lesson 1 guided notes", days: 0, tags: [1, 2], storage: "hcg/civil-rights/lesson-01-guided-notes.pdf", core: true },
  { id: "r1-activity", lesson: 1, kind: "Activity", name: "The Groundwork File", days: 1, tags: [1, 2], storage: "hcg/civil-rights/lesson-01-activity.pdf", core: true },
  { id: "r1-notebook", lesson: 1, kind: "Notebook", name: "Piece of groundwork chart", days: 0.5, tags: [1, 2], storage: "hcg/civil-rights/lesson-01-notebook.pdf" },
  { id: "r1-quick", lesson: 1, kind: "Quick Check", name: "The Order and the Argument", days: 0.5, tags: [1, 2], storage: "hcg/civil-rights/lesson-01-quick-check.pdf" },
  { id: "r1-writing", lesson: 1, kind: "Writing", name: "Built, Won, or Given?", days: 1, tags: [1, 2], storage: "hcg/civil-rights/lesson-01-writing.pdf" },
  // Lesson 2
  { id: "r2-reading", lesson: 2, kind: "Reading", name: "Brown and the Massive Resistance", days: 1, tags: [3, 4], storage: "hcg/civil-rights/lesson-02-reading.pdf", core: true },
  { id: "r2-notes", lesson: 2, kind: "Guided Notes", name: "Lesson 2 guided notes", days: 0, tags: [3, 4], storage: "hcg/civil-rights/lesson-02-guided-notes.pdf", core: true },
  { id: "r2-activity", lesson: 2, kind: "Activity", name: "The Case File", days: 1, tags: [3, 4], storage: "hcg/civil-rights/lesson-02-activity.pdf", core: true },
  { id: "r2-notebook", lesson: 2, kind: "Notebook", name: "Move in the argument chart", days: 0.5, tags: [3, 4], storage: "hcg/civil-rights/lesson-02-notebook.pdf" },
  { id: "r2-quick", lesson: 2, kind: "Quick Check", name: "The Decree", days: 0.5, tags: [3, 4], storage: "hcg/civil-rights/lesson-02-quick-check.pdf" },
  { id: "r2-writing", lesson: 2, kind: "Writing", name: "A Right Declared, a Decade Taken", days: 1, tags: [3, 4], storage: "hcg/civil-rights/lesson-02-writing.pdf" },
  // Lesson 3
  { id: "r3-reading", lesson: 3, kind: "Reading", name: "Montgomery and Little Rock: The Movement Finds Its Tactics", days: 1, tags: [5, 6], storage: "hcg/civil-rights/lesson-03-reading.pdf", core: true },
  { id: "r3-notes", lesson: 3, kind: "Guided Notes", name: "Lesson 3 guided notes", days: 0, tags: [5, 6], storage: "hcg/civil-rights/lesson-03-guided-notes.pdf", core: true },
  { id: "r3-activity", lesson: 3, kind: "Activity", name: "The Tactics Ledger", days: 1, tags: [5, 6], storage: "hcg/civil-rights/lesson-03-activity.pdf", core: true },
  { id: "r3-notebook", lesson: 3, kind: "Notebook", name: "Tactic or power chart", days: 0.5, tags: [5, 6], storage: "hcg/civil-rights/lesson-03-notebook.pdf" },
  { id: "r3-quick", lesson: 3, kind: "Quick Check", name: "Soldiers at the Schoolhouse Door", days: 0.5, tags: [5, 6], storage: "hcg/civil-rights/lesson-03-quick-check.pdf" },
  { id: "r3-writing", lesson: 3, kind: "Writing", name: "The Methods and the Federal Answer", days: 1, tags: [5, 6], storage: "hcg/civil-rights/lesson-03-writing.pdf" },
  // Lesson 4
  { id: "r4-reading", lesson: 4, kind: "Reading", name: "Sit-Ins and Freedom Rides: The Students Take the Lead", days: 1, tags: [7, 8], storage: "hcg/civil-rights/lesson-04-reading.pdf", core: true },
  { id: "r4-notes", lesson: 4, kind: "Guided Notes", name: "Lesson 4 guided notes", days: 0, tags: [7, 8], storage: "hcg/civil-rights/lesson-04-guided-notes.pdf", core: true },
  { id: "r4-activity", lesson: 4, kind: "Activity", name: "The Crisis File", days: 1, tags: [7, 8], storage: "hcg/civil-rights/lesson-04-activity.pdf", core: true },
  { id: "r4-notebook", lesson: 4, kind: "Notebook", name: "Crisis and answer chart", days: 0.5, tags: [7, 8], storage: "hcg/civil-rights/lesson-04-notebook.pdf" },
  { id: "r4-quick", lesson: 4, kind: "Quick Check", name: "The Counter and the Bus", days: 0.5, tags: [7, 8], storage: "hcg/civil-rights/lesson-04-quick-check.pdf" },
  { id: "r4-writing", lesson: 4, kind: "Writing", name: "The Students' Arithmetic", days: 1, tags: [7, 8], storage: "hcg/civil-rights/lesson-04-writing.pdf" },
  // Lesson 5
  { id: "r5-reading", lesson: 5, kind: "Reading", name: "Birmingham and the March on Washington", days: 1, tags: [9, 10], storage: "hcg/civil-rights/lesson-05-reading.pdf", core: true },
  { id: "r5-notes", lesson: 5, kind: "Guided Notes", name: "Lesson 5 guided notes", days: 0, tags: [9, 10], storage: "hcg/civil-rights/lesson-05-guided-notes.pdf", core: true },
  { id: "r5-activity", lesson: 5, kind: "Activity", name: "The Pressure File", days: 1, tags: [9, 10], storage: "hcg/civil-rights/lesson-05-activity.pdf", core: true },
  { id: "r5-notebook", lesson: 5, kind: "Notebook", name: "What it cost chart", days: 0.5, tags: [9, 10], storage: "hcg/civil-rights/lesson-05-notebook.pdf" },
  { id: "r5-quick", lesson: 5, kind: "Quick Check", name: "The Photograph and the Promise", days: 0.5, tags: [9, 10], storage: "hcg/civil-rights/lesson-05-quick-check.pdf" },
  { id: "r5-writing", lesson: 5, kind: "Writing", name: "Which Did More, Birmingham or the March?", days: 1, tags: [9, 10], storage: "hcg/civil-rights/lesson-05-writing.pdf" },
  // Lesson 6
  { id: "r6-reading", lesson: 6, kind: "Reading", name: "The Laws Change: 1964 and 1965", days: 1, tags: [11, 12], storage: "hcg/civil-rights/lesson-06-reading.pdf", core: true },
  { id: "r6-notes", lesson: 6, kind: "Guided Notes", name: "Lesson 6 guided notes", days: 0, tags: [11, 12], storage: "hcg/civil-rights/lesson-06-guided-notes.pdf", core: true },
  { id: "r6-activity", lesson: 6, kind: "Activity", name: "The Statute File", days: 1, tags: [11, 12], storage: "hcg/civil-rights/lesson-06-activity.pdf", core: true },
  { id: "r6-notebook", lesson: 6, kind: "Notebook", name: "The power created chart", days: 0.5, tags: [11, 12], storage: "hcg/civil-rights/lesson-06-notebook.pdf" },
  { id: "r6-quick", lesson: 6, kind: "Quick Check", name: "The Marchers on Highway 80", days: 0.5, tags: [11, 12], storage: "hcg/civil-rights/lesson-06-quick-check.pdf" },
  { id: "r6-writing", lesson: 6, kind: "Writing", name: "What Could the Two Great Acts Actually Reach?", days: 1, tags: [11, 12], storage: "hcg/civil-rights/lesson-06-writing.pdf" },
  // Lesson 7
  { id: "r7-reading", lesson: 7, kind: "Reading", name: "The Movement Turns North and Inward: Chicago, Black Power, Memphis", days: 1, tags: [13, 14], storage: "hcg/civil-rights/lesson-07-reading.pdf", core: true },
  { id: "r7-notes", lesson: 7, kind: "Guided Notes", name: "Lesson 7 guided notes", days: 0, tags: [13, 14], storage: "hcg/civil-rights/lesson-07-guided-notes.pdf", core: true },
  { id: "r7-activity", lesson: 7, kind: "Activity", name: "The Argument File", days: 1, tags: [13, 14], storage: "hcg/civil-rights/lesson-07-activity.pdf", core: true },
  { id: "r7-notebook", lesson: 7, kind: "Notebook", name: "Stage by stage chart", days: 0.5, tags: [13, 14], storage: "hcg/civil-rights/lesson-07-notebook.pdf" },
  { id: "r7-quick", lesson: 7, kind: "Quick Check", name: "The Northern Problem", days: 0.5, tags: [13, 14], storage: "hcg/civil-rights/lesson-07-quick-check.pdf" },
  { id: "r7-writing", lesson: 7, kind: "Writing", name: "What Freedom Required Next", days: 1, tags: [13, 14], storage: "hcg/civil-rights/lesson-07-writing.pdf" },
  // Lesson 8
  { id: "r8-reading", lesson: 8, kind: "Reading", name: "Victory, Backlash, and the Unfinished Agenda", days: 1, tags: [15], storage: "hcg/civil-rights/lesson-08-reading.pdf", core: true },
  { id: "r8-notes", lesson: 8, kind: "Guided Notes", name: "Lesson 8 guided notes", days: 0, tags: [15], storage: "hcg/civil-rights/lesson-08-guided-notes.pdf", core: true },
  { id: "r8-activity", lesson: 8, kind: "Activity", name: "The Reckoning File", days: 1, tags: [15], storage: "hcg/civil-rights/lesson-08-activity.pdf", core: true },
  { id: "r8-notebook", lesson: 8, kind: "Notebook", name: "The reckoning chart", days: 0.5, tags: [15], storage: "hcg/civil-rights/lesson-08-notebook.pdf" },
  { id: "r8-quick", lesson: 8, kind: "Quick Check", name: "The Signing, April 11, 1968", days: 0.5, tags: [15], storage: "hcg/civil-rights/lesson-08-quick-check.pdf" },
  { id: "r8-writing", lesson: 8, kind: "Writing", name: "The Reckoning", days: 1, tags: [15], storage: "hcg/civil-rights/lesson-08-writing.pdf" },
  // Review day
  { id: "rrev-guide", lesson: 9, kind: "Review", name: "Study guide (review day)", days: 1, tags: [], storage: "hcg/civil-rights/review-study-guide.pdf", core: true },
  { id: "rrev-cross", lesson: 9, kind: "Review", name: "Crossword (56 answers)", days: 0.5, tags: [], storage: "hcg/civil-rights/review-crossword.pdf" }
];

window.HCG_CR_TOPICS = {
  1: { label: "The long groundwork: Jim Crow and the institutions that fought it", note: "" },
  2: { label: "The courts and the Constitution: law as a movement weapon", note: "" },
  3: { label: "Mass protest: nonviolent direct action and its makers", note: "" },
  4: { label: "The federal government: ally, referee, and reluctant enforcer", note: "" },
  5: { label: "The movement divides and widens: region, class, and visions of freedom", note: "" },
  6: { label: "Legacy: what changed, what endured, what was left undone", note: "" }
};
window.HCG_CR_BP_TOPIC = {
  1: [1], 2: [1, 4], 3: [1, 2], 4: [2, 4], 5: [3], 6: [3, 4], 7: [3], 8: [3, 4], 9: [3, 4], 10: [3, 5], 11: [2, 4], 12: [2, 4], 13: [5], 14: [5], 15: [5, 6]
};

window.HCG_MA_BLUEPRINT = {
  1: "The malaise years: stagflation, the energy shocks, and the postwar settlement breaking down",
  2: "The revolt organized: the tax revolt, the New Right, the Moral Majority, and the coalition of 1980",
  3: "The Reagan program: the inaugural's claim, the 1981 tax cuts, deregulation, and the breaking of inflation",
  4: "The revolution's terms and limits: PATCO, the deficit, Iran-Contra, and what the New Deal order kept",
  5: "The Cold War ends at home: the Gulf War, the peace dividend debate, and the ADA settlement",
  6: "Globalization and the new economy: NAFTA, China trade, deindustrialization, and the distributional argument",
  7: "The machine and the network: the personal computer, the Internet, and the remaking of work and commerce",
  8: "The fractured news world: cable news, talk radio, the Internet press, social media, and the digital divide",
  9: "The new immigration: the 1965 act, the transformation of sources, and the 1986 settlement",
  10: "The map redrawn: the Sun Belt, the hollowing and revival of the cities, and reapportionment",
  11: "September 11 and the decision for war: the attacks, the doctrine, the AUMF, Afghanistan, and Iraq",
  12: "The security state and its critics: the PATRIOT Act, homeland security, surveillance, and the civil liberties argument",
  13: "The near failure: the housing bubble, subprime securities, Lehman's fall, and the rescue of 2008",
  14: "The aftermath argued: the stimulus, the Affordable Care Act, the Tea Party, Occupy, and the slow recovery",
  15: "The unsettled present: polarization, the courts' rights decisions, the pandemic test, and the continuities of the whole course"
};

window.HCG_MA_LESSONS = [
  { n: 1, title: "The Conservative Turn: Stagflation and the Tax Revolt", question: "Why did voters who had lived under the New Deal order for two generations turn against it in the 1970s?" },
  { n: 2, title: "The Reagan Revolution", question: "What did the Reagan administration change about what the federal government does, and what did it leave standing?" },
  { n: 3, title: "After the Cold War: Globalization and the New Economy", question: "What did Americans gain and what did they give up as their economy opened to the world after the Cold War?" },
  { n: 4, title: "The Digital Transformation", question: "How did networked computers change how Americans worked, shopped, learned, and talked to each other, and who was left out of the change?" },
  { n: 5, title: "A Changing America: Immigration, Cities, and the Sun Belt", question: "How did new immigration and the move to the Sun Belt change who Americans were and where American political power sat?" },
  { n: 6, title: "September 11 and the War on Terror", question: "How did the attacks of September 11 change what the federal government could do, and how Americans judged the wars that followed?" },
  { n: 7, title: "The Great Recession and Its Long Aftermath", question: "Why did a crisis in home loans become a crisis for the whole economy, and what did the government's answer change?" },
  { n: 8, title: "A Polarized Nation: America in the Twenty-First Century", question: "What do Americans now disagree about, and how much of the disagreement is new?" }
];

window.HCG_MA_ITEMS = [
  // Lesson 1
  { id: "m1-reading", lesson: 1, kind: "Reading", name: "The Conservative Turn: Stagflation and the Tax Revolt", days: 1, tags: [1, 2], storage: "hcg/modern-america/lesson-01-reading.pdf", core: true },
  { id: "m1-notes", lesson: 1, kind: "Guided Notes", name: "Lesson 1 guided notes", days: 0, tags: [1, 2], storage: "hcg/modern-america/lesson-01-guided-notes.pdf", core: true },
  { id: "m1-activity", lesson: 1, kind: "Activity", name: "The Diagnosis File", days: 1, tags: [1, 2], storage: "hcg/modern-america/lesson-01-activity.pdf", core: true },
  { id: "m1-notebook", lesson: 1, kind: "Notebook", name: "Piece of the story chart", days: 0.5, tags: [1, 2], storage: "hcg/modern-america/lesson-01-notebook.pdf" },
  { id: "m1-quick", lesson: 1, kind: "Quick Check", name: "The Diagnosis and the Numbers", days: 0.5, tags: [1, 2], storage: "hcg/modern-america/lesson-01-quick-check.pdf" },
  { id: "m1-writing", lesson: 1, kind: "Writing", name: "Which Diagnosis Did 1980 Reward?", days: 1, tags: [1, 2], storage: "hcg/modern-america/lesson-01-writing.pdf" },
  // Lesson 2
  { id: "m2-reading", lesson: 2, kind: "Reading", name: "The Reagan Revolution", days: 1, tags: [3, 4], storage: "hcg/modern-america/lesson-02-reading.pdf", core: true },
  { id: "m2-notes", lesson: 2, kind: "Guided Notes", name: "Lesson 2 guided notes", days: 0, tags: [3, 4], storage: "hcg/modern-america/lesson-02-guided-notes.pdf", core: true },
  { id: "m2-activity", lesson: 2, kind: "Activity", name: "The Revolution Ledger", days: 1, tags: [3, 4], storage: "hcg/modern-america/lesson-02-activity.pdf", core: true },
  { id: "m2-notebook", lesson: 2, kind: "Notebook", name: "Move in the record chart", days: 0.5, tags: [3, 4], storage: "hcg/modern-america/lesson-02-notebook.pdf" },
  { id: "m2-quick", lesson: 2, kind: "Quick Check", name: "The Promise and the Ledger", days: 0.5, tags: [3, 4], storage: "hcg/modern-america/lesson-02-quick-check.pdf" },
  { id: "m2-writing", lesson: 2, kind: "Writing", name: "Changed, and Left Standing", days: 1, tags: [3, 4], storage: "hcg/modern-america/lesson-02-writing.pdf" },
  // Lesson 3
  { id: "m3-reading", lesson: 3, kind: "Reading", name: "After the Cold War: Globalization and the New Economy", days: 1, tags: [5, 6], storage: "hcg/modern-america/lesson-03-reading.pdf", core: true },
  { id: "m3-notes", lesson: 3, kind: "Guided Notes", name: "Lesson 3 guided notes", days: 0, tags: [5, 6], storage: "hcg/modern-america/lesson-03-guided-notes.pdf", core: true },
  { id: "m3-activity", lesson: 3, kind: "Activity", name: "The Ledger of the Boom", days: 1, tags: [5, 6], storage: "hcg/modern-america/lesson-03-activity.pdf", core: true },
  { id: "m3-notebook", lesson: 3, kind: "Notebook", name: "Who gained, who paid chart", days: 0.5, tags: [5, 6], storage: "hcg/modern-america/lesson-03-notebook.pdf" },
  { id: "m3-quick", lesson: 3, kind: "Quick Check", name: "The Signing and the Figures", days: 0.5, tags: [5, 6], storage: "hcg/modern-america/lesson-03-quick-check.pdf" },
  { id: "m3-writing", lesson: 3, kind: "Writing", name: "Was the Peace Dividend Ever Really Paid?", days: 1, tags: [5, 6], storage: "hcg/modern-america/lesson-03-writing.pdf" },
  // Lesson 4
  { id: "m4-reading", lesson: 4, kind: "Reading", name: "The Digital Transformation", days: 1, tags: [7, 8], storage: "hcg/modern-america/lesson-04-reading.pdf", core: true },
  { id: "m4-notes", lesson: 4, kind: "Guided Notes", name: "Lesson 4 guided notes", days: 0, tags: [7, 8], storage: "hcg/modern-america/lesson-04-guided-notes.pdf", core: true },
  { id: "m4-activity", lesson: 4, kind: "Activity", name: "The Transformation File", days: 1, tags: [7, 8], storage: "hcg/modern-america/lesson-04-activity.pdf", core: true },
  { id: "m4-notebook", lesson: 4, kind: "Notebook", name: "Stage by stage chart", days: 0.5, tags: [7, 8], storage: "hcg/modern-america/lesson-04-notebook.pdf" },
  { id: "m4-quick", lesson: 4, kind: "Quick Check", name: "The Machine, the Network, and the News", days: 0.5, tags: [7, 8], storage: "hcg/modern-america/lesson-04-quick-check.pdf" },
  { id: "m4-writing", lesson: 4, kind: "Writing", name: "Which Change Reached Furthest?", days: 1, tags: [7, 8], storage: "hcg/modern-america/lesson-04-writing.pdf" },
  // Lesson 5
  { id: "m5-reading", lesson: 5, kind: "Reading", name: "A Changing America: Immigration, Cities, and the Sun Belt", days: 1, tags: [9, 10], storage: "hcg/modern-america/lesson-05-reading.pdf", core: true },
  { id: "m5-notes", lesson: 5, kind: "Guided Notes", name: "Lesson 5 guided notes", days: 0, tags: [9, 10], storage: "hcg/modern-america/lesson-05-guided-notes.pdf", core: true },
  { id: "m5-activity", lesson: 5, kind: "Activity", name: "The Changing Map File", days: 1, tags: [9, 10], storage: "hcg/modern-america/lesson-05-activity.pdf", core: true },
  { id: "m5-notebook", lesson: 5, kind: "Notebook", name: "Region or stream chart", days: 0.5, tags: [9, 10], storage: "hcg/modern-america/lesson-05-notebook.pdf" },
  { id: "m5-quick", lesson: 5, kind: "Quick Check", name: "The Table and the Two Cities", days: 0.5, tags: [9, 10], storage: "hcg/modern-america/lesson-05-quick-check.pdf" },
  { id: "m5-writing", lesson: 5, kind: "Writing", name: "Which Force Redrew the Map?", days: 1, tags: [9, 10], storage: "hcg/modern-america/lesson-05-writing.pdf" },
  // Lesson 6
  { id: "m6-reading", lesson: 6, kind: "Reading", name: "September 11 and the War on Terror", days: 1, tags: [11, 12], storage: "hcg/modern-america/lesson-06-reading.pdf", core: true },
  { id: "m6-notes", lesson: 6, kind: "Guided Notes", name: "Lesson 6 guided notes", days: 0, tags: [11, 12], storage: "hcg/modern-america/lesson-06-guided-notes.pdf", core: true },
  { id: "m6-activity", lesson: 6, kind: "Activity", name: "The Powers File", days: 1, tags: [11, 12], storage: "hcg/modern-america/lesson-06-activity.pdf", core: true },
  { id: "m6-notebook", lesson: 6, kind: "Notebook", name: "Power and its check chart", days: 0.5, tags: [11, 12], storage: "hcg/modern-america/lesson-06-notebook.pdf" },
  { id: "m6-quick", lesson: 6, kind: "Quick Check", name: "The Situation Room, May 1, 2011", days: 0.5, tags: [11, 12], storage: "hcg/modern-america/lesson-06-quick-check.pdf" },
  { id: "m6-writing", lesson: 6, kind: "Writing", name: "The Gap Between the Evidence and the Record", days: 1, tags: [11, 12], storage: "hcg/modern-america/lesson-06-writing.pdf" },
  // Lesson 7
  { id: "m7-reading", lesson: 7, kind: "Reading", name: "The Great Recession and Its Long Aftermath", days: 1, tags: [13, 14], storage: "hcg/modern-america/lesson-07-reading.pdf", core: true },
  { id: "m7-notes", lesson: 7, kind: "Guided Notes", name: "Lesson 7 guided notes", days: 0, tags: [13, 14], storage: "hcg/modern-america/lesson-07-guided-notes.pdf", core: true },
  { id: "m7-activity", lesson: 7, kind: "Activity", name: "The Rescue File", days: 1, tags: [13, 14], storage: "hcg/modern-america/lesson-07-activity.pdf", core: true },
  { id: "m7-notebook", lesson: 7, kind: "Notebook", name: "Failure and answer chart", days: 0.5, tags: [13, 14], storage: "hcg/modern-america/lesson-07-notebook.pdf" },
  { id: "m7-quick", lesson: 7, kind: "Quick Check", name: "The Rescue and Its Terms", days: 0.5, tags: [13, 14], storage: "hcg/modern-america/lesson-07-quick-check.pdf" },
  { id: "m7-writing", lesson: 7, kind: "Writing", name: "Who Was Rescued, Who Paid", days: 1, tags: [13, 14], storage: "hcg/modern-america/lesson-07-writing.pdf" },
  // Lesson 8
  { id: "m8-reading", lesson: 8, kind: "Reading", name: "A Polarized Nation: America in the Twenty-First Century", days: 1, tags: [15], storage: "hcg/modern-america/lesson-08-reading.pdf", core: true },
  { id: "m8-notes", lesson: 8, kind: "Guided Notes", name: "Lesson 8 guided notes", days: 0, tags: [15], storage: "hcg/modern-america/lesson-08-guided-notes.pdf", core: true },
  { id: "m8-activity", lesson: 8, kind: "Activity", name: "The Continuity File", days: 1, tags: [15], storage: "hcg/modern-america/lesson-08-activity.pdf", core: true },
  { id: "m8-notebook", lesson: 8, kind: "Notebook", name: "The modern record chart", days: 0.5, tags: [15], storage: "hcg/modern-america/lesson-08-notebook.pdf" },
  { id: "m8-quick", lesson: 8, kind: "Quick Check", name: "The Recount Stops, December 12, 2000", days: 0.5, tags: [15], storage: "hcg/modern-america/lesson-08-quick-check.pdf" },
  { id: "m8-writing", lesson: 8, kind: "Writing", name: "The Closing Verdict", days: 1, tags: [15], storage: "hcg/modern-america/lesson-08-writing.pdf" },
  // Review day
  { id: "mrev-guide", lesson: 9, kind: "Review", name: "Study guide (review day)", days: 1, tags: [], storage: "hcg/modern-america/review-study-guide.pdf", core: true },
  { id: "mrev-cross", lesson: 9, kind: "Review", name: "Crossword (56 answers)", days: 0.5, tags: [], storage: "hcg/modern-america/review-crossword.pdf" }
];

window.HCG_MA_TOPICS = {
  1: { label: "The conservative turn: small government and the market ascendancy", note: "" },
  2: { label: "A new economy: globalization, technology, and the service age", note: "" },
  3: { label: "A changing people: immigration, region, and the diversifying nation", note: "" },
  4: { label: "America in the world after the Cold War: sole superpower to war on terror", note: "" },
  5: { label: "Crisis and response: terror, financial collapse, and the tests of government", note: "" },
  6: { label: "The unsettled present: polarization, rights, and the argument over the country's direction", note: "" }
};
window.HCG_MA_BP_TOPIC = {
  1: [1], 2: [1], 3: [1], 4: [1, 6], 5: [4], 6: [2], 7: [2], 8: [2, 6], 9: [3], 10: [3], 11: [4, 5], 12: [5, 6], 13: [5], 14: [5, 1], 15: [6, 3]
};

// TPSP picker index for Modern America: the unit's premium DBQ (dbq23,
// era "Modern America" in the TPSP premium catalog, catalog code DBQ198,
// verified in Firestore with all seven of its documents present in
// the era file) first, then the era sources from the TPSP library file
// modern.json in file order, each with conservative blueprint pre-tags
// where the source names the entry's content. The era file's one audio
// record (the September 20, 2001 address) is excluded, as in the
// GA/WWI/DP pickers.
window.HCG_TPSP_MA = [
 {
  "id": "dbq23",
  "title": "How Have Americans Since 1968 Debated What the Country Should Be?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true
 },
 {
  "id": "ufw-boycott-for-democracy-poster-1975",
  "title": "UFW 'Boycott for Democracy' grape poster",
  "type": "Poster",
  "meta": "United Farm Workers · 1975",
  "url": "https://tpsp.web.app/library?q=UFW%20%27Boycott%20for%20Democracy%27%20grape%20poster"
 },
 {
  "id": "barbara-jordan-dnc-keynote-1976",
  "title": "Keynote address to the Democratic National Convention",
  "type": "Speech",
  "meta": "Barbara Jordan · 1976",
  "url": "https://tpsp.web.app/library?q=Keynote%20address%20to%20the%20Democratic%20National%20Convention"
 },
 {
  "id": "personal-justice-denied-1983",
  "title": "Personal Justice Denied (report of the Commission on Wartime Relocation and Internment of Civilians)",
  "type": "Government document",
  "meta": "Commission on Wartime Relocation and Internment of Civilians · 1983",
  "url": "https://tpsp.web.app/library?q=Personal%20Justice%20Denied%20%28report%20of%20the%20Commission%20on%20Wartime%20Relocation%20and%20Internment%20of%20Civilians%29"
 },
 {
  "id": "lippitt-mill-habs-drawing-1968",
  "title": "\"Lippitt Mill, West Warwick, RI\" (Historic American Buildings Survey drawing)",
  "type": "Illustration",
  "meta": "Unknown · 1968",
  "url": "https://tpsp.web.app/library?q=%22Lippitt%20Mill%2C%20West%20Warwick%2C%20RI%22%20%28Historic%20American%20Buildings%20Survey%20drawing%29"
 },
 {
  "id": "fussell-thank-god-for-the-atom-bomb-1981",
  "title": "\"Thank God for the Atom Bomb\" (excerpt)",
  "type": "Memoir",
  "meta": "Paul Fussell · 1981",
  "url": "https://tpsp.web.app/library?q=%22Thank%20God%20for%20the%20Atom%20Bomb%22%20%28excerpt%29"
 },
 {
  "id": "warriors-dont-cry-excerpt",
  "title": "Warriors Don't Cry (excerpt)",
  "type": "Memoir",
  "meta": "Melba Pattillo Beals · 1994",
  "url": "https://tpsp.web.app/library?q=Warriors%20Don%27t%20Cry%20%28excerpt%29"
 },
 {
  "id": "nixon-resignation-letter-1974",
  "title": "Richard M. Nixon's Resignation Letter",
  "type": "Letter",
  "meta": "Richard M. Nixon · 1974",
  "url": "https://tpsp.web.app/library?q=Richard%20M.%20Nixon%27s%20Resignation%20Letter"
 },
 {
  "id": "herblock-mugging-1973",
  "title": "\"Mugging\" (political cartoon)",
  "type": "Political cartoon",
  "meta": "Herbert L. Block (Herblock) · 1973",
  "url": "https://tpsp.web.app/library?q=%22Mugging%22%20%28political%20cartoon%29"
 },
 {
  "id": "carter-crisis-of-confidence-1979",
  "title": "\"Crisis of Confidence\" Address",
  "type": "Speech",
  "meta": "Jimmy Carter · 1979",
  "url": "https://tpsp.web.app/library?q=%22Crisis%20of%20Confidence%22%20Address",
  "bp": [
   1
  ]
 },
 {
  "id": "reagan-first-inaugural-1981",
  "title": "First Inaugural Address",
  "type": "Speech",
  "meta": "Ronald Reagan · 1981",
  "url": "https://tpsp.web.app/library?q=First%20Inaugural%20Address",
  "bp": [
   3
  ]
 },
 {
  "id": "bush-911-address-2001",
  "title": "Address to the Nation on the September 11 Attacks",
  "type": "Speech",
  "meta": "George W. Bush · 2001",
  "url": "https://tpsp.web.app/library?q=Address%20to%20the%20Nation%20on%20the%20September%2011%20Attacks",
  "bp": [
   11
  ]
 },
 {
  "id": "clinton-articles-impeachment-1998",
  "title": "Articles of Impeachment against William Jefferson Clinton (H.Res. 611)",
  "type": "Government document",
  "meta": "U.S. House of Representatives · 1998",
  "url": "https://tpsp.web.app/library?q=Articles%20of%20Impeachment%20against%20William%20Jefferson%20Clinton%20%28H.Res.%20611%29"
 },
 {
  "id": "roe-v-wade-1973",
  "title": "Roe v. Wade, 410 U.S. 113 (majority opinion, excerpt)",
  "type": "Court decision",
  "meta": "Justice Harry Blackmun (U.S. Supreme Court) · 1973",
  "url": "https://tpsp.web.app/library?q=Roe%20v.%20Wade%2C%20410%20U.S.%20113%20%28majority%20opinion%2C%20excerpt%29"
 },
 {
  "id": "americans-with-disabilities-act-1990",
  "title": "Americans with Disabilities Act of 1990 (Section 2, Findings; excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress · 1990",
  "url": "https://tpsp.web.app/library?q=Americans%20with%20Disabilities%20Act%20of%201990%20%28Section%202%2C%20Findings%3B%20excerpt%29",
  "bp": [
   5
  ]
 },
 {
  "id": "dc-v-heller-2008",
  "title": "District of Columbia v. Heller, 554 U.S. 570 (Justice Scalia)",
  "type": "Court decision",
  "meta": "U.S. Supreme Court · 2008",
  "url": "https://tpsp.web.app/library?q=District%20of%20Columbia%20v.%20Heller%2C%20554%20U.S.%20570%20%28Justice%20Scalia%29",
  "bp": [
   15
  ]
 },
 {
  "id": "lilly-ledbetter-fair-pay-act-2009",
  "title": "Lilly Ledbetter Fair Pay Act of 2009",
  "type": "Government document",
  "meta": "U.S. Congress · 2009",
  "url": "https://tpsp.web.app/library?q=Lilly%20Ledbetter%20Fair%20Pay%20Act%20of%202009"
 },
 {
  "id": "immigration-reform-control-act-1986",
  "title": "Immigration Reform and Control Act of 1986",
  "type": "Government document",
  "meta": "U.S. Congress · 1986",
  "url": "https://tpsp.web.app/library?q=Immigration%20Reform%20and%20Control%20Act%20of%201986",
  "bp": [
   9
  ]
 },
 {
  "id": "911-commission-report-exec-summary-2004",
  "title": "The 9/11 Commission Report: Executive Summary",
  "type": "Government document",
  "meta": "National Commission on Terrorist Attacks Upon the United States · 2004",
  "url": "https://tpsp.web.app/library?q=The%209%2F11%20Commission%20Report%3A%20Executive%20Summary",
  "bp": [
   11
  ]
 },
 {
  "id": "title-ix-education-amendments-1972",
  "title": "Title IX, Education Amendments of 1972 (Section 901)",
  "type": "Government document",
  "meta": "U.S. Congress · 1972",
  "url": "https://tpsp.web.app/library?q=Title%20IX%2C%20Education%20Amendments%20of%201972%20%28Section%20901%29"
 },
 {
  "id": "equal-rights-amendment-1972",
  "title": "Equal Rights Amendment (H.J. Res. 208), as Passed by Congress",
  "type": "Government document",
  "meta": "U.S. Congress · 1972",
  "url": "https://tpsp.web.app/library?q=Equal%20Rights%20Amendment%20%28H.J.%20Res.%20208%29%2C%20as%20Passed%20by%20Congress"
 },
 {
  "id": "ford-proclamation-4311-1974",
  "title": "Proclamation 4311: Granting Pardon to Richard Nixon",
  "type": "Government document",
  "meta": "Gerald R. Ford · 1974",
  "url": "https://tpsp.web.app/library?q=Proclamation%204311%3A%20Granting%20Pardon%20to%20Richard%20Nixon"
 },
 {
  "id": "authorization-use-military-force-2001",
  "title": "Authorization for Use of Military Force (AUMF), 2001",
  "type": "Government document",
  "meta": "U.S. Congress · 2001",
  "url": "https://tpsp.web.app/library?q=Authorization%20for%20Use%20of%20Military%20Force%20%28AUMF%29%2C%202001",
  "bp": [
   11
  ]
 },
 {
  "id": "bush-v-gore-2000",
  "title": "Bush v. Gore, 531 U.S. 98 (per curiam)",
  "type": "Court decision",
  "meta": "U.S. Supreme Court · 2000",
  "url": "https://tpsp.web.app/library?q=Bush%20v.%20Gore%2C%20531%20U.S.%2098%20%28per%20curiam%29",
  "bp": [
   15
  ]
 },
 {
  "id": "patriot-act-section-102-2001",
  "title": "USA PATRIOT Act, Section 102: Sense of Congress Condemning Discrimination",
  "type": "Government document",
  "meta": "U.S. Congress · 2001",
  "url": "https://tpsp.web.app/library?q=USA%20PATRIOT%20Act%2C%20Section%20102%3A%20Sense%20of%20Congress%20Condemning%20Discrimination",
  "bp": [
   12
  ]
 },
 {
  "id": "war-powers-resolution-1973",
  "title": "War Powers Resolution (P.L. 93-148)",
  "type": "Government document",
  "meta": "U.S. Congress · 1973",
  "url": "https://tpsp.web.app/library?q=War%20Powers%20Resolution%20%28P.L.%2093-148%29"
 },
 {
  "id": "obergefell-v-hodges-2015",
  "title": "Obergefell v. Hodges, 576 U.S. 644 (Justice Kennedy)",
  "type": "Court decision",
  "meta": "U.S. Supreme Court · 2015",
  "url": "https://tpsp.web.app/library?q=Obergefell%20v.%20Hodges%2C%20576%20U.S.%20644%20%28Justice%20Kennedy%29",
  "bp": [
   15
  ]
 },
 {
  "id": "bush-ada-signing-statement-1990",
  "title": "Statement on Signing the Americans with Disabilities Act",
  "type": "Speech",
  "meta": "George H. W. Bush · 1990",
  "url": "https://tpsp.web.app/library?q=Statement%20on%20Signing%20the%20Americans%20with%20Disabilities%20Act",
  "bp": [
   5
  ]
 },
 {
  "id": "regents-uc-v-bakke-1978",
  "title": "Regents of the University of California v. Bakke, 438 U.S. 265 (Justice Powell)",
  "type": "Court decision",
  "meta": "U.S. Supreme Court · 1978",
  "url": "https://tpsp.web.app/library?q=Regents%20of%20the%20University%20of%20California%20v.%20Bakke%2C%20438%20U.S.%20265%20%28Justice%20Powell%29",
  "bp": [
   15
  ]
 },
 {
  "id": "reagan-challenger-address-1986",
  "title": "Address to the Nation on the Challenger Disaster",
  "type": "Speech",
  "meta": "Ronald Reagan · 1986",
  "url": "https://tpsp.web.app/library?q=Address%20to%20the%20Nation%20on%20the%20Challenger%20Disaster"
 },
 {
  "id": "carter-proclamation-4483-1977",
  "title": "Proclamation 4483: Pardon for Violations of the Selective Service Act",
  "type": "Government document",
  "meta": "Jimmy Carter · 1977",
  "url": "https://tpsp.web.app/library?q=Proclamation%204483%3A%20Pardon%20for%20Violations%20of%20the%20Selective%20Service%20Act"
 }
];

// TPSP picker index for Civil Rights: the unit's premium DBQ (dbq22,
// era "Civil Rights" in the TPSP premium catalog, catalog code DBQ197,
// verified in Firestore with all seven of its documents present in
// the era file) first, then the five records the Cold War picker left
// untagged because they belong to this unit (Executive Order 9981, the
// Till record, Eisenhower's Little Rock address, the Faubus statement,
// and Executive Order 10730, from the TPSP cold-war era file), then
// the era sources from the TPSP library file civil-rights.json in
// file order, each with conservative blueprint pre-tags where the
// source names the entry's content. The era file carries no audio
// sources, so none are excluded here.
window.HCG_TPSP_CR = [
 {
  "id": "dbq22",
  "title": "Did Black Americans in the 1960s Share One Vision of Freedom?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true
 },
 {
  "id": "executive-order-9981-1948",
  "title": "Executive Order 9981",
  "type": "Government document",
  "meta": "Harry S. Truman · 1948",
  "url": "https://tpsp.web.app/library?q=Executive%20Order%209981",
  "bp": [
   2
  ]
 },
 {
  "id": "emmett-till-jet-photographs-1955",
  "title": "Jet magazine photographs of Emmett Till",
  "type": "Photograph",
  "meta": "David Jackson · 1955",
  "url": "https://tpsp.web.app/library?q=Jet%20magazine%20photographs%20of%20Emmett%20Till",
  "bp": [
   6
  ]
 },
 {
  "id": "eisenhower-little-rock-address-1957",
  "title": "Radio and television address on the Little Rock crisis",
  "type": "Speech",
  "meta": "Dwight D. Eisenhower · 1957",
  "url": "https://tpsp.web.app/library?q=Radio%20and%20television%20address%20on%20the%20Little%20Rock%20crisis",
  "bp": [
   6
  ]
 },
 {
  "id": "faubus-little-rock-statement-1957",
  "title": "Statement on the Little Rock crisis",
  "type": "Speech",
  "meta": "Orval Faubus · 1957",
  "url": "https://tpsp.web.app/library?q=Statement%20on%20the%20Little%20Rock%20crisis",
  "bp": [
   6
  ]
 },
 {
  "id": "executive-order-10730-1957",
  "title": "Executive Order 10730",
  "type": "Government document",
  "meta": "Dwight D. Eisenhower · 1957",
  "url": "https://tpsp.web.app/library?q=Executive%20Order%2010730",
  "bp": [
   6
  ]
 },
 {
  "id": "brown-v-board",
  "title": "Brown v. Board of Education",
  "type": "Court decision",
  "meta": "U.S. Supreme Court · 1954",
  "url": "https://tpsp.web.app/library?q=Brown%20v.%20Board%20of%20Education",
  "bp": [
   3
  ]
 },
 {
  "id": "jo-ann-robinson-letter-mayor-1954",
  "title": "Letter to the Mayor (Jo Ann Robinson)",
  "type": "Letter",
  "meta": "Jo Ann Robinson · 1954",
  "url": "https://tpsp.web.app/library?q=Letter%20to%20the%20Mayor%20%28Jo%20Ann%20Robinson%29",
  "bp": [
   5
  ]
 },
 {
  "id": "rosa-parks-fingerprint-card-1955",
  "title": "Fingerprint Card of Rosa Parks",
  "type": "Government document",
  "meta": "Montgomery, Alabama police / U.S. District Court records · 1955",
  "url": "https://tpsp.web.app/library?q=Fingerprint%20Card%20of%20Rosa%20Parks",
  "bp": [
   5
  ]
 },
 {
  "id": "bayard-rustin-montgomery-diary-1956",
  "title": "Montgomery Diary (February 24, 1956)",
  "type": "Diary",
  "meta": "Bayard Rustin · 1956",
  "url": "https://tpsp.web.app/library?q=Montgomery%20Diary%20%28February%2024%2C%201956%29",
  "bp": [
   5
  ]
 },
 {
  "id": "virginia-durr-letter-hortons-1956",
  "title": "Letter to Myles and Zilphia Horton",
  "type": "Letter",
  "meta": "Virginia Foster Durr · 1956",
  "url": "https://tpsp.web.app/library?q=Letter%20to%20Myles%20and%20Zilphia%20Horton"
 },
 {
  "id": "mlk-mia-mass-meeting-1956",
  "title": "Speech at the MIA Mass Meeting (as reported by Anna Holden)",
  "type": "Speech",
  "meta": "Martin Luther King Jr. · 1956",
  "url": "https://tpsp.web.app/library?q=Speech%20at%20the%20MIA%20Mass%20Meeting%20%28as%20reported%20by%20Anna%20Holden%29",
  "bp": [
   5
  ]
 },
 {
  "id": "rosa-parks-reflections-arrest-1956",
  "title": "Rosa Parks's Reflections on Her Arrest (manuscript excerpt)",
  "type": "Memoir",
  "meta": "Rosa Parks · ca. 1956",
  "url": "https://tpsp.web.app/library?q=Rosa%20Parks%27s%20Reflections%20on%20Her%20Arrest%20%28manuscript%20excerpt%29",
  "bp": [
   5
  ]
 },
 {
  "id": "jesus-colon-little-things-are-big-1961",
  "title": "\"Little Things are Big\"",
  "type": "Memoir",
  "meta": "Jesús Colón · 1961",
  "url": "https://tpsp.web.app/library?q=%22Little%20Things%20are%20Big%22"
 },
 {
  "id": "mlk-birmingham-jail",
  "title": "Letter from Birmingham Jail (excerpt)",
  "type": "Letter",
  "meta": "Martin Luther King Jr. · 1963",
  "url": "https://tpsp.web.app/library?q=Letter%20from%20Birmingham%20Jail%20%28excerpt%29",
  "bp": [
   9
  ]
 },
 {
  "id": "mlk-i-have-a-dream",
  "title": "I Have a Dream (excerpt)",
  "type": "Speech",
  "meta": "Martin Luther King Jr. · 1963",
  "url": "https://tpsp.web.app/library?q=I%20Have%20a%20Dream%20%28excerpt%29",
  "bp": [
   10
  ]
 },
 {
  "id": "march-on-washington-1963",
  "title": "March on Washington for Jobs and Freedom (photograph)",
  "type": "Photograph",
  "meta": "Unknown photographer (National Archives) · 1963",
  "url": "https://tpsp.web.app/library?q=March%20on%20Washington%20for%20Jobs%20and%20Freedom%20%28photograph%29",
  "bp": [
   10
  ]
 },
 {
  "id": "final-plans-march-washington-1963",
  "title": "Final Plans for the March on Washington for Jobs and Freedom",
  "type": "Pamphlet",
  "meta": "Bayard Rustin and Cleveland Robinson · 1963",
  "url": "https://tpsp.web.app/library?q=Final%20Plans%20for%20the%20March%20on%20Washington%20for%20Jobs%20and%20Freedom",
  "bp": [
   10
  ]
 },
 {
  "id": "march-on-washington-scherman-1963",
  "title": "March on Washington: Edith Lee-Payne (photograph)",
  "type": "Photograph",
  "meta": "U.S. Information Agency (photographer Rowland Scherman) · 1963",
  "url": "https://tpsp.web.app/library?q=March%20on%20Washington%3A%20Edith%20Lee-Payne%20%28photograph%29",
  "bp": [
   10
  ]
 },
 {
  "id": "trikosko-aerial-march-washington-1963",
  "title": "Aerial View of the Crowds at the March on Washington (photograph)",
  "type": "Photograph",
  "meta": "Marion S. Trikosko · 1963",
  "url": "https://tpsp.web.app/library?q=Aerial%20View%20of%20the%20Crowds%20at%20the%20March%20on%20Washington%20%28photograph%29",
  "bp": [
   10
  ]
 },
 {
  "id": "civil-rights-act-1964",
  "title": "Civil Rights Act of 1964",
  "type": "Government document",
  "meta": "U.S. Congress · 1964",
  "url": "https://tpsp.web.app/library?q=Civil%20Rights%20Act%20of%201964",
  "bp": [
   11
  ]
 },
 {
  "id": "lbj-signing-civil-rights-act-1964",
  "title": "President Johnson signs the Civil Rights Act (photograph)",
  "type": "Photograph",
  "meta": "Cecil Stoughton, White House Press Office · 1964",
  "url": "https://tpsp.web.app/library?q=President%20Johnson%20signs%20the%20Civil%20Rights%20Act%20%28photograph%29",
  "bp": [
   11
  ]
 },
 {
  "id": "malcolm-x-autobiography-garvey-1964",
  "title": "The Autobiography of Malcolm X (excerpt on Marcus Garvey)",
  "type": "Memoir",
  "meta": "Malcolm X · 1964",
  "url": "https://tpsp.web.app/library?q=The%20Autobiography%20of%20Malcolm%20X%20%28excerpt%20on%20Marcus%20Garvey%29",
  "bp": [
   14
  ]
 },
 {
  "id": "civil-rights-act-title-vii-1964",
  "title": "Civil Rights Act of 1964, Title VII (excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress · 1964",
  "url": "https://tpsp.web.app/library?q=Civil%20Rights%20Act%20of%201964%2C%20Title%20VII%20%28excerpt%29",
  "bp": [
   11
  ]
 },
 {
  "id": "ballot-or-the-bullet-1964",
  "title": "\"The Ballot or the Bullet\" (excerpt)",
  "type": "Speech",
  "meta": "Malcolm X · 1964",
  "url": "https://tpsp.web.app/library?q=%22The%20Ballot%20or%20the%20Bullet%22%20%28excerpt%29",
  "bp": [
   14
  ]
 },
 {
  "id": "voting-rights-act-1965",
  "title": "Voting Rights Act of 1965 (excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress · 1965",
  "url": "https://tpsp.web.app/library?q=Voting%20Rights%20Act%20of%201965%20%28excerpt%29",
  "bp": [
   12
  ]
 },
 {
  "id": "e-jackson-voting-rights-letter-1965",
  "title": "Letter from Mrs. E. Jackson on Voting Rights",
  "type": "Letter",
  "meta": "Mrs. E. Jackson · 1965",
  "url": "https://tpsp.web.app/library?q=Letter%20from%20Mrs.%20E.%20Jackson%20on%20Voting%20Rights",
  "bp": [
   12
  ]
 },
 {
  "id": "lbj-we-shall-overcome-1965",
  "title": "\"We Shall Overcome\" Voting Rights Address",
  "type": "Speech",
  "meta": "Lyndon B. Johnson · 1965",
  "url": "https://tpsp.web.app/library?q=%22We%20Shall%20Overcome%22%20Voting%20Rights%20Address",
  "bp": [
   12
  ]
 },
 {
  "id": "rfk-delano-chavez-1968",
  "title": "Robert F. Kennedy's Remarks at Delano (as reported)",
  "type": "Speech",
  "meta": "United Farm Workers · 1968",
  "url": "https://tpsp.web.app/library?q=Robert%20F.%20Kennedy%27s%20Remarks%20at%20Delano%20%28as%20reported%29"
 },
 {
  "id": "rfk-delano-statement-1968",
  "title": "Robert F. Kennedy's Statement on Cesar Chavez at Delano",
  "type": "Speech",
  "meta": "Robert F. Kennedy · 1968",
  "url": "https://tpsp.web.app/library?q=Robert%20F.%20Kennedy%27s%20Statement%20on%20Cesar%20Chavez%20at%20Delano"
 },
 {
  "id": "civil-rights-posters-memphis-1968",
  "title": "Civil Rights Posters, 1968 (\"I AM A MAN\" and \"Honor King\")",
  "type": "Poster",
  "meta": "Various (Memphis sanitation workers' strike) · 1968",
  "url": "https://tpsp.web.app/library?q=Civil%20Rights%20Posters%2C%201968%20%28%22I%20AM%20A%20MAN%22%20and%20%22Honor%20King%22%29",
  "bp": [
   14
  ]
 },
 {
  "id": "kennedy-civil-rights-address-1963",
  "title": "Report to the American People on Civil Rights (excerpt)",
  "type": "Speech",
  "meta": "John F. Kennedy · 1963",
  "url": "https://tpsp.web.app/library?q=Report%20to%20the%20American%20People%20on%20Civil%20Rights%20%28excerpt%29",
  "bp": [
   9
  ]
 },
 {
  "id": "southern-manifesto-1956",
  "title": "The Southern Manifesto (excerpt)",
  "type": "Government document",
  "meta": "Southern Members of Congress · 1956",
  "url": "https://tpsp.web.app/library?q=The%20Southern%20Manifesto%20%28excerpt%29",
  "bp": [
   4
  ]
 },
 {
  "id": "brown-v-board-ii-1955",
  "title": "Brown v. Board of Education II (excerpt)",
  "type": "Court decision",
  "meta": "U.S. Supreme Court · 1955",
  "url": "https://tpsp.web.app/library?q=Brown%20v.%20Board%20of%20Education%20II%20%28excerpt%29",
  "bp": [
   4
  ]
 },
 {
  "id": "lbj-howard-university-address-1965",
  "title": "Howard University Commencement Address (\"To Fulfill These Rights\") (excerpt)",
  "type": "Speech",
  "meta": "Lyndon B. Johnson · 1965",
  "url": "https://tpsp.web.app/library?q=Howard%20University%20Commencement%20Address%20%28%22To%20Fulfill%20These%20Rights%22%29%20%28excerpt%29",
  "bp": [
   15
  ]
 },
 {
  "id": "cooper-v-aaron-1958",
  "title": "Cooper v. Aaron (excerpt)",
  "type": "Court decision",
  "meta": "U.S. Supreme Court · 1958",
  "url": "https://tpsp.web.app/library?q=Cooper%20v.%20Aaron%20%28excerpt%29",
  "bp": [
   4
  ]
 },
 {
  "id": "loving-v-virginia-1967",
  "title": "Loving v. Virginia (excerpt)",
  "type": "Court decision",
  "meta": "U.S. Supreme Court · 1967",
  "url": "https://tpsp.web.app/library?q=Loving%20v.%20Virginia%20%28excerpt%29"
 },
 {
  "id": "kerner-commission-report-1968",
  "title": "Kerner Commission Report, Introduction (excerpt)",
  "type": "Government document",
  "meta": "National Advisory Commission on Civil Disorders · 1968",
  "url": "https://tpsp.web.app/library?q=Kerner%20Commission%20Report%2C%20Introduction%20%28excerpt%29",
  "bp": [
   15
  ]
 },
 {
  "id": "to-secure-these-rights-1947",
  "title": "To Secure These Rights (excerpt)",
  "type": "Government document",
  "meta": "President's Committee on Civil Rights · 1947",
  "url": "https://tpsp.web.app/library?q=To%20Secure%20These%20Rights%20%28excerpt%29",
  "bp": [
   2
  ]
 }
];

window.HCG_CA_BLUEPRINT = {
  1: "The Americas before contact: Indigenous societies, cities, and confederacies",
  2: "Contact and catastrophe: Columbus, the Columbian Exchange, and the demographic collapse",
  3: "Spanish America: conquest, encomienda, Las Casas, and the colonial order",
  4: "The northern empires: France's fur trade and alliances, the Dutch, and French slavery",
  5: "Jamestown: the Virginia Company, the starving time, and tobacco's transformation",
  6: "Chesapeake labor: indenture, the turn to slavery, and Bacon's Rebellion",
  7: "New England founded: Plymouth, Massachusetts Bay, and Winthrop's commonwealth",
  8: "New England tested: dissent, Salem, and war with Indigenous nations",
  9: "The middle colonies: diversity, Penn's Pennsylvania, and toleration's limits",
  10: "Mercantilism at work: the Navigation Acts and the Atlantic economy",
  11: "The slave trade: the Middle Passage and the law that made slavery hereditary",
  12: "Slavery's worlds: regional variation, culture, resistance, and Stono",
  13: "Self-government: assemblies, salutary neglect, and the Zenger verdict",
  14: "The Great Awakening and the Enlightenment: revival, print, and judging authority",
  15: "The French and Indian War: victory, the Treaty of Paris, Pontiac, and the Proclamation"
};

window.HCG_CA_LESSONS = [
  { n: 1, title: "Two Worlds Before Contact", question: "What did the Americas and Europe each look like in 1491, and what changed when they met?" },
  { n: 2, title: "The Spanish and French Americas", question: "How did Spain build an empire on conquest, and how did France build one on trade?" },
  { n: 3, title: "Jamestown and the Chesapeake", question: "How did a starving outpost become a tobacco colony, and what did tobacco demand?" },
  { n: 4, title: "New England: Covenant and Community", question: "What kind of community did New England's settlers mean to build, and who could belong to it?" },
  { n: 5, title: "The Middle Colonies and the Atlantic Economy", question: "How did the middle colonies become the colonies of many peoples, and what held the Atlantic economy together?" },
  { n: 6, title: "Slavery and the Slave Trade", question: "How was the Atlantic slave trade organized, and what did enslaved people endure, build, and resist?" },
  { n: 7, title: "Governing, Working, and Arguing About God", question: "How did colonists govern themselves, raise their families, and argue about God?" },
  { n: 8, title: "Empire and War: The French and Indian War", question: "How did Britain win North America, and what did the victory cost everyone who fought it?" }
];

window.HCG_CA_ITEMS = [
  // Lesson 1
  { id: "a1-reading", lesson: 1, kind: "Reading", name: "Two Worlds Before Contact", days: 1, tags: [1, 2], storage: "hcg/colonial-america/lesson-01-reading.pdf", core: true },
  { id: "a1-notes", lesson: 1, kind: "Guided Notes", name: "Lesson 1 guided notes", days: 0, tags: [1, 2], storage: "hcg/colonial-america/lesson-01-guided-notes.pdf", core: true },
  { id: "a1-activity", lesson: 1, kind: "Activity", name: "Two Worlds in 1491", days: 1, tags: [1, 2], storage: "hcg/colonial-america/lesson-01-activity.pdf", core: true },
  { id: "a1-notebook", lesson: 1, kind: "Notebook", name: "Piece of the picture chart", days: 0.5, tags: [1, 2], storage: "hcg/colonial-america/lesson-01-notebook.pdf" },
  { id: "a1-quick", lesson: 1, kind: "Quick Check", name: "The Letter and the Claim", days: 0.5, tags: [1, 2], storage: "hcg/colonial-america/lesson-01-quick-check.pdf" },
  { id: "a1-writing", lesson: 1, kind: "Writing", name: "Which Change Remade the Americas?", days: 1, tags: [1, 2], storage: "hcg/colonial-america/lesson-01-writing.pdf" },
  // Lesson 2
  { id: "a2-reading", lesson: 2, kind: "Reading", name: "The Spanish and French Americas", days: 1, tags: [3, 4], storage: "hcg/colonial-america/lesson-02-reading.pdf", core: true },
  { id: "a2-notes", lesson: 2, kind: "Guided Notes", name: "Lesson 2 guided notes", days: 0, tags: [3, 4], storage: "hcg/colonial-america/lesson-02-guided-notes.pdf", core: true },
  { id: "a2-activity", lesson: 2, kind: "Activity", name: "Two Empires, One Hemisphere", days: 1, tags: [3, 4], storage: "hcg/colonial-america/lesson-02-activity.pdf", core: true },
  { id: "a2-notebook", lesson: 2, kind: "Notebook", name: "Spain and France chart", days: 0.5, tags: [3, 4], storage: "hcg/colonial-america/lesson-02-notebook.pdf" },
  { id: "a2-quick", lesson: 2, kind: "Quick Check", name: "The Causeway and the Code", days: 0.5, tags: [3, 4], storage: "hcg/colonial-america/lesson-02-quick-check.pdf" },
  { id: "a2-writing", lesson: 2, kind: "Writing", name: "Two Ways of Holding a Hemisphere", days: 1, tags: [3, 4], storage: "hcg/colonial-america/lesson-02-writing.pdf" },
  // Lesson 3
  { id: "a3-reading", lesson: 3, kind: "Reading", name: "Jamestown and the Chesapeake", days: 1, tags: [5, 6], storage: "hcg/colonial-america/lesson-03-reading.pdf", core: true },
  { id: "a3-notes", lesson: 3, kind: "Guided Notes", name: "Lesson 3 guided notes", days: 0, tags: [5, 6], storage: "hcg/colonial-america/lesson-03-guided-notes.pdf", core: true },
  { id: "a3-activity", lesson: 3, kind: "Activity", name: "The Tobacco Ledger", days: 1, tags: [5, 6], storage: "hcg/colonial-america/lesson-03-activity.pdf", core: true },
  { id: "a3-notebook", lesson: 3, kind: "Notebook", name: "Part of the lesson chart", days: 0.5, tags: [5, 6], storage: "hcg/colonial-america/lesson-03-notebook.pdf" },
  { id: "a3-quick", lesson: 3, kind: "Quick Check", name: "The Map and the Colony", days: 0.5, tags: [5, 6], storage: "hcg/colonial-america/lesson-03-quick-check.pdf" },
  { id: "a3-writing", lesson: 3, kind: "Writing", name: "What Tobacco Demanded", days: 1, tags: [5, 6], storage: "hcg/colonial-america/lesson-03-writing.pdf" },
  // Lesson 4
  { id: "a4-reading", lesson: 4, kind: "Reading", name: "New England: Covenant and Community", days: 1, tags: [7, 8], storage: "hcg/colonial-america/lesson-04-reading.pdf", core: true },
  { id: "a4-notes", lesson: 4, kind: "Guided Notes", name: "Lesson 4 guided notes", days: 0, tags: [7, 8], storage: "hcg/colonial-america/lesson-04-guided-notes.pdf", core: true },
  { id: "a4-activity", lesson: 4, kind: "Activity", name: "The Covenant File", days: 1, tags: [7, 8], storage: "hcg/colonial-america/lesson-04-activity.pdf", core: true },
  { id: "a4-notebook", lesson: 4, kind: "Notebook", name: "Rule of belonging chart", days: 0.5, tags: [7, 8], storage: "hcg/colonial-america/lesson-04-notebook.pdf" },
  { id: "a4-quick", lesson: 4, kind: "Quick Check", name: "The Compact and the Court", days: 0.5, tags: [7, 8], storage: "hcg/colonial-america/lesson-04-quick-check.pdf" },
  { id: "a4-writing", lesson: 4, kind: "Writing", name: "Who Could Belong", days: 1, tags: [7, 8], storage: "hcg/colonial-america/lesson-04-writing.pdf" },
  // Lesson 5
  { id: "a5-reading", lesson: 5, kind: "Reading", name: "The Middle Colonies and the Atlantic Economy", days: 1, tags: [9, 10], storage: "hcg/colonial-america/lesson-05-reading.pdf", core: true },
  { id: "a5-notes", lesson: 5, kind: "Guided Notes", name: "Lesson 5 guided notes", days: 0, tags: [9, 10], storage: "hcg/colonial-america/lesson-05-guided-notes.pdf", core: true },
  { id: "a5-activity", lesson: 5, kind: "Activity", name: "The Atlantic Ledger", days: 1, tags: [9, 10], storage: "hcg/colonial-america/lesson-05-activity.pdf", core: true },
  { id: "a5-notebook", lesson: 5, kind: "Notebook", name: "What it gave, what it cost chart", days: 0.5, tags: [9, 10], storage: "hcg/colonial-america/lesson-05-notebook.pdf" },
  { id: "a5-quick", lesson: 5, kind: "Quick Check", name: "Conscience and Cargo", days: 0.5, tags: [9, 10], storage: "hcg/colonial-america/lesson-05-quick-check.pdf" },
  { id: "a5-writing", lesson: 5, kind: "Writing", name: "Helped to Grow, or Held in Place?", days: 1, tags: [9, 10], storage: "hcg/colonial-america/lesson-05-writing.pdf" },
  // Lesson 6
  { id: "a6-reading", lesson: 6, kind: "Reading", name: "Slavery and the Slave Trade", days: 1, tags: [11, 12], storage: "hcg/colonial-america/lesson-06-reading.pdf", core: true },
  { id: "a6-notes", lesson: 6, kind: "Guided Notes", name: "Lesson 6 guided notes", days: 0, tags: [11, 12], storage: "hcg/colonial-america/lesson-06-guided-notes.pdf", core: true },
  { id: "a6-activity", lesson: 6, kind: "Activity", name: "The System in Five Records", days: 1, tags: [11, 12], storage: "hcg/colonial-america/lesson-06-activity.pdf", core: true },
  { id: "a6-notebook", lesson: 6, kind: "Notebook", name: "Part of the system chart", days: 0.5, tags: [11, 12], storage: "hcg/colonial-america/lesson-06-notebook.pdf" },
  { id: "a6-quick", lesson: 6, kind: "Quick Check", name: "The Brookes Plate, 1788", days: 0.5, tags: [11, 12], storage: "hcg/colonial-america/lesson-06-quick-check.pdf" },
  { id: "a6-writing", lesson: 6, kind: "Writing", name: "Endure, Build, Resist", days: 1, tags: [11, 12], storage: "hcg/colonial-america/lesson-06-writing.pdf" },
  // Lesson 7
  { id: "a7-reading", lesson: 7, kind: "Reading", name: "Governing, Working, and Arguing About God", days: 1, tags: [13, 14], storage: "hcg/colonial-america/lesson-07-reading.pdf", core: true },
  { id: "a7-notes", lesson: 7, kind: "Guided Notes", name: "Lesson 7 guided notes", days: 0, tags: [13, 14], storage: "hcg/colonial-america/lesson-07-guided-notes.pdf", core: true },
  { id: "a7-activity", lesson: 7, kind: "Activity", name: "The Conscience File", days: 1, tags: [13, 14], storage: "hcg/colonial-america/lesson-07-activity.pdf", core: true },
  { id: "a7-notebook", lesson: 7, kind: "Notebook", name: "Stage by stage chart", days: 0.5, tags: [13, 14], storage: "hcg/colonial-america/lesson-07-notebook.pdf" },
  { id: "a7-quick", lesson: 7, kind: "Quick Check", name: "Self-Government and Revival", days: 0.5, tags: [13, 14], storage: "hcg/colonial-america/lesson-07-quick-check.pdf" },
  { id: "a7-writing", lesson: 7, kind: "Writing", name: "Ready to Judge Authority", days: 1, tags: [13, 14], storage: "hcg/colonial-america/lesson-07-writing.pdf" },
  // Lesson 8
  { id: "a8-reading", lesson: 8, kind: "Reading", name: "Empire and War: The French and Indian War", days: 1, tags: [15], storage: "hcg/colonial-america/lesson-08-reading.pdf", core: true },
  { id: "a8-notes", lesson: 8, kind: "Guided Notes", name: "Lesson 8 guided notes", days: 0, tags: [15], storage: "hcg/colonial-america/lesson-08-guided-notes.pdf", core: true },
  { id: "a8-activity", lesson: 8, kind: "Activity", name: "The War in Five Records", days: 1, tags: [15], storage: "hcg/colonial-america/lesson-08-activity.pdf", core: true },
  { id: "a8-notebook", lesson: 8, kind: "Notebook", name: "Question of the war chart", days: 0.5, tags: [15], storage: "hcg/colonial-america/lesson-08-notebook.pdf" },
  { id: "a8-quick", lesson: 8, kind: "Quick Check", name: "The Map of 1763", days: 0.5, tags: [15], storage: "hcg/colonial-america/lesson-08-quick-check.pdf" },
  { id: "a8-writing", lesson: 8, kind: "Writing", name: "Triumph, Warning, or Both", days: 1, tags: [15], storage: "hcg/colonial-america/lesson-08-writing.pdf" },
  // Review day
  { id: "arev-guide", lesson: 9, kind: "Review", name: "Study guide (review day)", days: 1, tags: [], storage: "hcg/colonial-america/review-study-guide.pdf", core: true },
  { id: "arev-cross", lesson: 9, kind: "Review", name: "Crossword (56 answers)", days: 0.5, tags: [], storage: "hcg/colonial-america/review-crossword.pdf" }
];

window.HCG_CA_TOPICS = {
  1: { label: "Two worlds meet: the Americas and Europe before and at contact", note: "" },
  2: { label: "Empires in America: Spain, France, and England compete", note: "" },
  3: { label: "Regional colonial societies: Chesapeake, New England, and the Middle Colonies", note: "" },
  4: { label: "The Atlantic system: trade, mercantilism, and enslaved labor", note: "" },
  5: { label: "Colonial life: government, religion, and family", note: "" },
  6: { label: "Empire tested: the imperial wars and the hinge of 1763", note: "" }
};
window.HCG_CA_BP_TOPIC = {
  1: [1], 2: [1, 4], 3: [2, 4], 4: [2], 5: [2, 3], 6: [3, 4], 7: [3], 8: [3, 5], 9: [3, 5], 10: [4, 2], 11: [4], 12: [4, 3], 13: [5, 6], 14: [5], 15: [6, 2]
};

// TPSP picker index for Colonial America: the unit's premium DBQ (dbq13,
// era "Colonial America" in the TPSP premium catalog, catalog code DBQ188,
// verified in Firestore with all seven of its documents present in
// the era file) first, then the two records the unit draws from the
// early-modern-empire era file (the Diaz entry into Tenochtitlan and the
// Code Noir), then the era sources from the TPSP library file
// colonial.json in file order, each with conservative blueprint pre-tags
// where the source names the entry's content. The 1765 Stamp Act broadside
// is deliberately left untagged: the unit closes in 1763 and the imperial
// crisis belongs to the Founding unit.
window.HCG_TPSP_CA = [
 {
  "id": "dbq13",
  "title": "Did Colonial America Offer Liberty and Opportunity?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true
 },
 {
  "id": "diaz-entry-into-tenochtitlan",
  "title": "True History of the Conquest of New Spain: Entry into Tenochtitlan, 1519",
  "type": "Memoir",
  "meta": "Bernal Díaz del Castillo · 1568",
  "url": "https://tpsp.web.app/library?q=True%20History%20of%20the%20Conquest%20of%20New%20Spain%3A%20Entry%20into%20Tenochtitlan%2C%201519",
  "bp": [
   3
  ]
 },
 {
  "id": "code-noir-1685",
  "title": "The Code Noir (The Black Code), 1685",
  "type": "Legal code",
  "meta": "Louis XIV · 1685",
  "url": "https://tpsp.web.app/library?q=The%20Code%20Noir%20%28The%20Black%20Code%29%2C%201685",
  "bp": [
   4
  ]
 },
 {
  "id": "columbus-first-voyage-1493",
  "title": "Columbus Reports on His First Voyage, 1493",
  "type": "Letter",
  "meta": "Christopher Columbus · 1493",
  "url": "https://tpsp.web.app/library?q=Columbus%20Reports%20on%20His%20First%20Voyage%2C%201493",
  "bp": [
   2
  ]
 },
 {
  "id": "smith-true-relation-1608",
  "title": "A True Relation",
  "type": "Memoir",
  "meta": "John Smith · 1608",
  "url": "https://tpsp.web.app/library?q=A%20True%20Relation",
  "bp": [
   5
  ]
 },
 {
  "id": "smith-letter-queen-anne-1616",
  "title": "Letter to Queen Anne",
  "type": "Letter",
  "meta": "John Smith · 1616",
  "url": "https://tpsp.web.app/library?q=Letter%20to%20Queen%20Anne",
  "bp": [
   5
  ]
 },
 {
  "id": "mayflower-compact",
  "title": "Mayflower Compact (excerpt)",
  "type": "Government document",
  "meta": "Pilgrim settlers · 1620",
  "url": "https://tpsp.web.app/library?q=Mayflower%20Compact%20%28excerpt%29",
  "bp": [
   7
  ]
 },
 {
  "id": "smith-general-history-1624",
  "title": "The General History of Virginia, New England and the Summer Isles",
  "type": "Memoir",
  "meta": "John Smith · 1624",
  "url": "https://tpsp.web.app/library?q=The%20General%20History%20of%20Virginia%2C%20New%20England%20and%20the%20Summer%20Isles",
  "bp": [
   5
  ]
 },
 {
  "id": "winthrop-boston-1634",
  "title": "John Winthrop Describes Life in Boston, 1634",
  "type": "Letter",
  "meta": "John Winthrop · 1634",
  "url": "https://tpsp.web.app/library?q=John%20Winthrop%20Describes%20Life%20in%20Boston%2C%201634",
  "bp": [
   7
  ]
 },
 {
  "id": "hutchinson-trial-examination",
  "title": "Anne Hutchinson trial examination",
  "type": "Court decision",
  "meta": "Massachusetts Bay General Court · 1637",
  "url": "https://tpsp.web.app/library?q=Anne%20Hutchinson%20trial%20examination",
  "bp": [
   8
  ]
 },
 {
  "id": "join-or-die-1754",
  "title": "Join, or Die",
  "type": "Political cartoon",
  "meta": "Benjamin Franklin (attributed) · 1754",
  "url": "https://tpsp.web.app/library?q=Join%2C%20or%20Die",
  "bp": [
   15
  ]
 },
 {
  "id": "no-stamped-paper-1765",
  "title": "\"No stamped paper to be had\" (Philadelphia, 1765)",
  "type": "Broadside",
  "meta": "Hall & Franklin · 1765",
  "url": "https://tpsp.web.app/library?q=%22No%20stamped%20paper%20to%20be%20had%22%20%28Philadelphia%2C%201765%29"
 },
 {
  "id": "wheatley-on-being-brought",
  "title": "'On Being Brought from Africa to America' (full poem)",
  "type": "Poem",
  "meta": "Phillis Wheatley · 1773",
  "url": "https://tpsp.web.app/library?q=%27On%20Being%20Brought%20from%20Africa%20to%20America%27%20%28full%20poem%29",
  "bp": [
   12
  ]
 },
 {
  "id": "equiano-middle-passage",
  "title": "The Interesting Narrative (Middle Passage excerpt)",
  "type": "Narrative",
  "meta": "Olaudah Equiano · 1789",
  "url": "https://tpsp.web.app/library?q=The%20Interesting%20Narrative%20%28Middle%20Passage%20excerpt%29",
  "bp": [
   11
  ]
 },
 {
  "id": "winthrop-modell-christian-charitie-1630",
  "title": "\"A Modell of Christian Charitie\"",
  "type": "Speech",
  "meta": "John Winthrop · 1630",
  "url": "https://tpsp.web.app/library?q=%22A%20Modell%20of%20Christian%20Charitie%22",
  "bp": [
   7
  ]
 },
 {
  "id": "fundamental-orders-connecticut-1639",
  "title": "Fundamental Orders of Connecticut",
  "type": "Government document",
  "meta": "Freemen of the Connecticut River towns · 1639",
  "url": "https://tpsp.web.app/library?q=Fundamental%20Orders%20of%20Connecticut",
  "bp": [
   7
  ]
 },
 {
  "id": "bacon-declaration-1676",
  "title": "Declaration in the Name of the People",
  "type": "Pamphlet",
  "meta": "Nathaniel Bacon · 1676",
  "url": "https://tpsp.web.app/library?q=Declaration%20in%20the%20Name%20of%20the%20People",
  "bp": [
   6
  ]
 },
 {
  "id": "las-casas-destruction-indies-1552",
  "title": "A Brief Account of the Destruction of the Indies",
  "type": "Book",
  "meta": "Bartolomé de las Casas · 1552",
  "url": "https://tpsp.web.app/library?q=A%20Brief%20Account%20of%20the%20Destruction%20of%20the%20Indies",
  "bp": [
   3
  ]
 },
 {
  "id": "maryland-toleration-act-1649",
  "title": "Maryland Toleration Act",
  "type": "Government document",
  "meta": "Maryland General Assembly · 1649",
  "url": "https://tpsp.web.app/library?q=Maryland%20Toleration%20Act",
  "bp": [
   9
  ]
 },
 {
  "id": "zenger-trial-narrative-1735",
  "title": "Trial of John Peter Zenger (Hamilton's Summation)",
  "type": "Narrative",
  "meta": "Andrew Hamilton (defense summation, in Zenger's narrative of the trial) · 1735",
  "url": "https://tpsp.web.app/library?q=Trial%20of%20John%20Peter%20Zenger%20%28Hamilton%27s%20Summation%29",
  "bp": [
   13
  ]
 },
 {
  "id": "edwards-sinners-angry-god-1741",
  "title": "\"Sinners in the Hands of an Angry God\"",
  "type": "Speech",
  "meta": "Jonathan Edwards · 1741",
  "url": "https://tpsp.web.app/library?q=%22Sinners%20in%20the%20Hands%20of%20an%20Angry%20God%22",
  "bp": [
   14
  ]
 },
 {
  "id": "sarah-good-trial-records-1692",
  "title": "Records of the Trial and Execution of Sarah Good",
  "type": "Court decision",
  "meta": "Essex County Court of Oyer and Terminer · 1692",
  "url": "https://tpsp.web.app/library?q=Records%20of%20the%20Trial%20and%20Execution%20of%20Sarah%20Good",
  "bp": [
   8
  ]
 },
 {
  "id": "flushing-remonstrance-1657",
  "title": "Flushing Remonstrance",
  "type": "Petition",
  "meta": "Edward Hart and 30 residents of Flushing · 1657",
  "url": "https://tpsp.web.app/library?q=Flushing%20Remonstrance",
  "bp": [
   9
  ]
 }
];
// ---------------------------------------------------------------------
// The Founding (eleventh unit, second in course order)
window.HCG_FD_BLUEPRINT = {
  1: "The revenue program: Britain's war debt, the Stamp Act, and the first resistance",
  2: "Repeal and its limits: the Declaratory Act, the Townshend duties, and the Boston Massacre",
  3: "Tea and coercion: the Tea Act, the Boston Tea Party, and the Intolerable Acts",
  4: "Congress and the first shots: the First Continental Congress, Lexington and Concord, and the road from the Olive Branch to the Proclamation of Rebellion",
  5: "The argument for independence: Common Sense and the republican turn",
  6: "The Declaration: natural rights, the grievances against the king, and the deleted passage",
  7: "Survival and Saratoga: the Continental Army's endurance and the French alliance",
  8: "The war won: the southern campaigns, Yorktown, and the Treaty of Paris",
  9: "The peoples of the war: Black Americans, women, and Native nations",
  10: "The home front and the Loyalists: inflation, sacrifice, and the Loyalist exodus",
  11: "The Articles of Confederation: structure and the land ordinances",
  12: "The Confederation in crisis: debt, Shays's Rebellion, and the call for a convention",
  13: "Framing the Constitution: the Virginia and New Jersey Plans and the Great Compromise",
  14: "The Constitution's design: federalism, separation of powers, and slavery's compromises",
  15: "Ratification and the Bill of Rights: Federalists, Anti-Federalists, and the first amendments"
};

window.HCG_FD_LESSONS = [
  { n: 1, title: "The Imperial Crisis: Taxation and Resistance", question: "Why did Britain tax the colonies after 1763, and why did the colonists resist taxes they had never been asked to pay before?" },
  { n: 2, title: "From Protest to Revolution: 1773 to 1776", question: "How did a protest over tea become a war?" },
  { n: 3, title: "Declaring Independence", question: "What did the Declaration argue, and why did Americans need an argument at all?" },
  { n: 4, title: "The War for Independence", question: "How did the United States survive a war against the world's strongest empire, and win it?" },
  { n: 5, title: "Winning and Losing: The War's Home Fronts and Its Peoples", question: "Who else fought, paid, and waited through the war, and what did its promise mean to them?" },
  { n: 6, title: "The Confederation and the Road to Philadelphia", question: "Why did the government the Revolution built first fail to hold the union together?" },
  { n: 7, title: "The Constitution and the Great Compromises", question: "How did fifty five men in one room design a government strong enough to act and limited enough to trust?" },
  { n: 8, title: "Ratification and the Bill of Rights", question: "How was the Constitution sold to a skeptical people, and what did the skeptics win?" }
];

window.HCG_FD_ITEMS = [
  // Lesson 1
  { id: "f1-reading", lesson: 1, kind: "Reading", name: "The Imperial Crisis: Taxation and Resistance", days: 1, tags: [1, 2], storage: "hcg/the-founding/lesson-01-reading.pdf", core: true },
  { id: "f1-notes", lesson: 1, kind: "Guided Notes", name: "Lesson 1 guided notes", days: 0, tags: [1, 2], storage: "hcg/the-founding/lesson-01-guided-notes.pdf", core: true },
  { id: "f1-activity", lesson: 1, kind: "Activity", name: "The Tax File", days: 1, tags: [1, 2], storage: "hcg/the-founding/lesson-01-activity.pdf", core: true },
  { id: "f1-notebook", lesson: 1, kind: "Notebook", name: "Piece of the crisis chart", days: 0.5, tags: [1, 2], storage: "hcg/the-founding/lesson-01-notebook.pdf" },
  { id: "f1-quick", lesson: 1, kind: "Quick Check", name: "Two Accounts of One Night", days: 0.5, tags: [1, 2], storage: "hcg/the-founding/lesson-01-quick-check.pdf" },
  { id: "f1-writing", lesson: 1, kind: "Writing", name: "Why Repeal Did Not End the Quarrel", days: 1, tags: [1, 2], storage: "hcg/the-founding/lesson-01-writing.pdf" },
  // Lesson 2
  { id: "f2-reading", lesson: 2, kind: "Reading", name: "From Protest to Revolution: 1773 to 1776", days: 1, tags: [3, 4], storage: "hcg/the-founding/lesson-02-reading.pdf", core: true },
  { id: "f2-notes", lesson: 2, kind: "Guided Notes", name: "Lesson 2 guided notes", days: 0, tags: [3, 4], storage: "hcg/the-founding/lesson-02-guided-notes.pdf", core: true },
  { id: "f2-activity", lesson: 2, kind: "Activity", name: "From Tea to War", days: 1, tags: [3, 4], storage: "hcg/the-founding/lesson-02-activity.pdf", core: true },
  { id: "f2-notebook", lesson: 2, kind: "Notebook", name: "Step by step chart", days: 0.5, tags: [3, 4], storage: "hcg/the-founding/lesson-02-notebook.pdf" },
  { id: "f2-quick", lesson: 2, kind: "Quick Check", name: "Two Records of One Morning", days: 0.5, tags: [3, 4], storage: "hcg/the-founding/lesson-02-quick-check.pdf" },
  { id: "f2-writing", lesson: 2, kind: "Writing", name: "How a Protest over Tea Became a War", days: 1, tags: [3, 4], storage: "hcg/the-founding/lesson-02-writing.pdf" },
  // Lesson 3
  { id: "f3-reading", lesson: 3, kind: "Reading", name: "Declaring Independence", days: 1, tags: [5, 6], storage: "hcg/the-founding/lesson-03-reading.pdf", core: true },
  { id: "f3-notes", lesson: 3, kind: "Guided Notes", name: "Lesson 3 guided notes", days: 0, tags: [5, 6], storage: "hcg/the-founding/lesson-03-guided-notes.pdf", core: true },
  { id: "f3-activity", lesson: 3, kind: "Activity", name: "The Argument of 1776: Declaring Independence", days: 1, tags: [5, 6], storage: "hcg/the-founding/lesson-03-activity.pdf", core: true },
  { id: "f3-notebook", lesson: 3, kind: "Notebook", name: "Part of the argument chart", days: 0.5, tags: [5, 6], storage: "hcg/the-founding/lesson-03-notebook.pdf" },
  { id: "f3-quick", lesson: 3, kind: "Quick Check", name: "The Argument in the Text", days: 0.5, tags: [5, 6], storage: "hcg/the-founding/lesson-03-quick-check.pdf" },
  { id: "f3-writing", lesson: 3, kind: "Writing", name: "Why an Argument", days: 1, tags: [5, 6], storage: "hcg/the-founding/lesson-03-writing.pdf" },
  // Lesson 4
  { id: "f4-reading", lesson: 4, kind: "Reading", name: "The War for Independence", days: 1, tags: [7, 8], storage: "hcg/the-founding/lesson-04-reading.pdf", core: true },
  { id: "f4-notes", lesson: 4, kind: "Guided Notes", name: "Lesson 4 guided notes", days: 0, tags: [7, 8], storage: "hcg/the-founding/lesson-04-guided-notes.pdf", core: true },
  { id: "f4-activity", lesson: 4, kind: "Activity", name: "The War in Five Records", days: 1, tags: [7, 8], storage: "hcg/the-founding/lesson-04-activity.pdf", core: true },
  { id: "f4-notebook", lesson: 4, kind: "Notebook", name: "Turning point chart", days: 0.5, tags: [7, 8], storage: "hcg/the-founding/lesson-04-notebook.pdf" },
  { id: "f4-quick", lesson: 4, kind: "Quick Check", name: "Congress to a Tired Country, May 1778", days: 0.5, tags: [7, 8], storage: "hcg/the-founding/lesson-04-quick-check.pdf" },
  { id: "f4-writing", lesson: 4, kind: "Writing", name: "What Won the War", days: 1, tags: [7, 8], storage: "hcg/the-founding/lesson-04-writing.pdf" },
  // Lesson 5
  { id: "f5-reading", lesson: 5, kind: "Reading", name: "Winning and Losing: The War's Home Fronts and Its Peoples", days: 1, tags: [9, 10], storage: "hcg/the-founding/lesson-05-reading.pdf", core: true },
  { id: "f5-notes", lesson: 5, kind: "Guided Notes", name: "Lesson 5 guided notes", days: 0, tags: [9, 10], storage: "hcg/the-founding/lesson-05-guided-notes.pdf", core: true },
  { id: "f5-activity", lesson: 5, kind: "Activity", name: "Whose War", days: 1, tags: [9, 10], storage: "hcg/the-founding/lesson-05-activity.pdf", core: true },
  { id: "f5-notebook", lesson: 5, kind: "Notebook", name: "The war's peoples chart", days: 0.5, tags: [9, 10], storage: "hcg/the-founding/lesson-05-notebook.pdf" },
  { id: "f5-quick", lesson: 5, kind: "Quick Check", name: "Dunmore's Proclamation, 1775", days: 0.5, tags: [9, 10], storage: "hcg/the-founding/lesson-05-quick-check.pdf" },
  { id: "f5-writing", lesson: 5, kind: "Writing", name: "What Freedom Meant", days: 1, tags: [9, 10], storage: "hcg/the-founding/lesson-05-writing.pdf" },
  // Lesson 6
  { id: "f6-reading", lesson: 6, kind: "Reading", name: "The Confederation and the Road to Philadelphia", days: 1, tags: [11, 12], storage: "hcg/the-founding/lesson-06-reading.pdf", core: true },
  { id: "f6-notes", lesson: 6, kind: "Guided Notes", name: "Lesson 6 guided notes", days: 0, tags: [11, 12], storage: "hcg/the-founding/lesson-06-guided-notes.pdf", core: true },
  { id: "f6-activity", lesson: 6, kind: "Activity", name: "The Confederation File: What the First Government Could and Could Not Do", days: 1, tags: [11, 12], storage: "hcg/the-founding/lesson-06-activity.pdf", core: true },
  { id: "f6-notebook", lesson: 6, kind: "Notebook", name: "Part by part chart", days: 0.5, tags: [11, 12], storage: "hcg/the-founding/lesson-06-notebook.pdf" },
  { id: "f6-quick", lesson: 6, kind: "Quick Check", name: "A League and Its Limits", days: 0.5, tags: [11, 12], storage: "hcg/the-founding/lesson-06-quick-check.pdf" },
  { id: "f6-writing", lesson: 6, kind: "Writing", name: "Failure, Draft, or a Job Without Tools?", days: 1, tags: [11, 12], storage: "hcg/the-founding/lesson-06-writing.pdf" },
  // Lesson 7
  { id: "f7-reading", lesson: 7, kind: "Reading", name: "The Constitution and the Great Compromises", days: 1, tags: [13, 14], storage: "hcg/the-founding/lesson-07-reading.pdf", core: true },
  { id: "f7-notes", lesson: 7, kind: "Guided Notes", name: "Lesson 7 guided notes", days: 0, tags: [13, 14], storage: "hcg/the-founding/lesson-07-guided-notes.pdf", core: true },
  { id: "f7-activity", lesson: 7, kind: "Activity", name: "Philadelphia in Five Records", days: 1, tags: [13, 14], storage: "hcg/the-founding/lesson-07-activity.pdf", core: true },
  { id: "f7-notebook", lesson: 7, kind: "Notebook", name: "Question by question chart", days: 0.5, tags: [13, 14], storage: "hcg/the-founding/lesson-07-notebook.pdf" },
  { id: "f7-quick", lesson: 7, kind: "Quick Check", name: "We the People and the Count", days: 0.5, tags: [13, 14], storage: "hcg/the-founding/lesson-07-quick-check.pdf" },
  { id: "f7-writing", lesson: 7, kind: "Writing", name: "Strong Enough to Act, Limited Enough to Trust", days: 1, tags: [13, 14], storage: "hcg/the-founding/lesson-07-writing.pdf" },
  // Lesson 8
  { id: "f8-reading", lesson: 8, kind: "Reading", name: "Ratification and the Bill of Rights", days: 1, tags: [15], storage: "hcg/the-founding/lesson-08-reading.pdf", core: true },
  { id: "f8-notes", lesson: 8, kind: "Guided Notes", name: "Lesson 8 guided notes", days: 0, tags: [15], storage: "hcg/the-founding/lesson-08-guided-notes.pdf", core: true },
  { id: "f8-activity", lesson: 8, kind: "Activity", name: "The Ratification File", days: 1, tags: [15], storage: "hcg/the-founding/lesson-08-activity.pdf", core: true },
  { id: "f8-notebook", lesson: 8, kind: "Notebook", name: "Record by record chart", days: 0.5, tags: [15], storage: "hcg/the-founding/lesson-08-notebook.pdf" },
  { id: "f8-quick", lesson: 8, kind: "Quick Check", name: "Two Arguments About Size", days: 0.5, tags: [15], storage: "hcg/the-founding/lesson-08-quick-check.pdf" },
  { id: "f8-writing", lesson: 8, kind: "Writing", name: "Who Won the Argument of 1787 and 1788", days: 1, tags: [15], storage: "hcg/the-founding/lesson-08-writing.pdf" },
  // Review day
  { id: "frev-guide", lesson: 9, kind: "Review", name: "Study guide (review day)", days: 1, tags: [], storage: "hcg/the-founding/review-study-guide.pdf", core: true },
  { id: "frev-cross", lesson: 9, kind: "Review", name: "Crossword (56 answers)", days: 0.5, tags: [], storage: "hcg/the-founding/review-crossword.pdf" }
];

window.HCG_FD_TOPICS = {
  1: { label: "The empire after 1763: revenue, reform, and resistance", note: "" },
  2: { label: "The road to revolution: protest becomes rebellion, 1773 to 1776", note: "" },
  3: { label: "Independence declared: the ideas and the decision of 1776", note: "" },
  4: { label: "The war for independence: campaigns, allies, and home fronts", note: "" },
  5: { label: "The Confederation tested: governing the new republic in the 1780s", note: "" },
  6: { label: "The Constitution: framing, ratifying, and the Bill of Rights", note: "" }
};
window.HCG_FD_BP_TOPIC = {
  1: [1], 2: [1], 3: [2, 1], 4: [2], 5: [3, 2], 6: [3], 7: [4], 8: [4], 9: [4, 3], 10: [4], 11: [5], 12: [5, 6], 13: [6], 14: [6, 3], 15: [6]
};

// TPSP picker index for The Founding: the unit's two premium DBQs
// (dbq1, catalog code DBQ176, and dbq2, catalog code DBQ177, both era
// "Revolution and the Founding" in the TPSP premium catalog, verified
// in Firestore with all seven documents of each present in the era
// file) first, then the 1765 Stamp Act broadside the Colonial America
// picker deliberately left untagged (tagged here, where it belongs),
// then the era sources from the TPSP library file founding.json in
// file order, each with conservative blueprint pre-tags where the
// source names the entry's content. Four records are deliberately
// left untagged: Washington's 1786 Mercer letter and Virginia's
// Statute for Religious Freedom (Confederation-era context no single
// entry names), and the cotton gin patent and the Farewell Address,
// which belong to the Early Republic unit's ground.
window.HCG_TPSP_FD = [
 {
  "id": "dbq1",
  "title": "Why Did the Colonies Break with Britain?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project \u00b7 premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true
 },
 {
  "id": "dbq2",
  "title": "Whose Voices Counted in the Founding?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project \u00b7 premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true
 },
 {
  "id": "no-stamped-paper-1765",
  "title": "\"No stamped paper to be had\" (Philadelphia, 1765)",
  "type": "Broadside",
  "meta": "Hall & Franklin \u00b7 1765",
  "url": "https://tpsp.web.app/library?q=%22No%20stamped%20paper%20to%20be%20had%22%20%28Philadelphia%2C%201765%29",
  "bp": [
   1
  ]
 },
 {
  "id": "revere-boston-massacre-1770",
  "title": "The Bloody Massacre in King-Street",
  "type": "Political cartoon",
  "meta": "Paul Revere (after Henry Pelham) \u00b7 1770",
  "url": "https://tpsp.web.app/library?q=The%20Bloody%20Massacre%20in%20King-Street",
  "bp": [
   2
  ]
 },
 {
  "id": "preston-case-1770",
  "title": "Captain Preston's Account of the Boston Massacre",
  "type": "Newspaper",
  "meta": "Capt. Thomas Preston \u00b7 1770",
  "url": "https://tpsp.web.app/library?q=Captain%20Preston%27s%20Account%20of%20the%20Boston%20Massacre",
  "bp": [
   2
  ]
 },
 {
  "id": "drowne-testimony-1770",
  "title": "Samuel Drowne's Testimony on the Boston Massacre",
  "type": "Government document",
  "meta": "Samuel Drowne \u00b7 1770",
  "url": "https://tpsp.web.app/library?q=Samuel%20Drowne%27s%20Testimony%20on%20the%20Boston%20Massacre",
  "bp": [
   2
  ]
 },
 {
  "id": "bostonians-paying-exciseman-1774",
  "title": "The Bostonian's Paying the Excise-Man",
  "type": "Political cartoon",
  "meta": "Philip Dawe (attributed) \u00b7 1774",
  "url": "https://tpsp.web.app/library?q=The%20Bostonian%27s%20Paying%20the%20Excise-Man",
  "bp": [
   3
  ]
 },
 {
  "id": "barker-diary-lexington-1775",
  "title": "Lieutenant Barker Describes the Battle of Lexington, 1775",
  "type": "Diary",
  "meta": "Lt. John Barker \u00b7 1775",
  "url": "https://tpsp.web.app/library?q=Lieutenant%20Barker%20Describes%20the%20Battle%20of%20Lexington%2C%201775",
  "bp": [
   4
  ]
 },
 {
  "id": "minutemen-testimony-lexington-1775",
  "title": "Lexington Militiamen Give Their Account of the Battle",
  "type": "Government document",
  "meta": "Massachusetts minutemen \u00b7 1775",
  "url": "https://tpsp.web.app/library?q=Lexington%20Militiamen%20Give%20Their%20Account%20of%20the%20Battle",
  "bp": [
   4
  ]
 },
 {
  "id": "king-proclamation-rebellion-1775",
  "title": "King George III's Proclamation Suppressing Rebellion and Sedition",
  "type": "Government document",
  "meta": "King George III \u00b7 1775",
  "url": "https://tpsp.web.app/library?q=King%20George%20III%27s%20Proclamation%20Suppressing%20Rebellion%20and%20Sedition",
  "bp": [
   4
  ]
 },
 {
  "id": "dunmore-proclamation-1775",
  "title": "Lord Dunmore's Proclamation",
  "type": "Government document",
  "meta": "John Murray, Earl of Dunmore \u00b7 1775",
  "url": "https://tpsp.web.app/library?q=Lord%20Dunmore%27s%20Proclamation",
  "bp": [
   9
  ]
 },
 {
  "id": "declaration-of-independence",
  "title": "Declaration of Independence (excerpt)",
  "type": "Government document",
  "meta": "Thomas Jefferson (for the Continental Congress) \u00b7 1776",
  "url": "https://tpsp.web.app/library?q=Declaration%20of%20Independence%20%28excerpt%29",
  "bp": [
   6
  ]
 },
 {
  "id": "abigail-adams-remember-the-ladies",
  "title": "'Remember the ladies' letter (excerpt)",
  "type": "Letter",
  "meta": "Abigail Adams \u00b7 March 1776",
  "url": "https://tpsp.web.app/library?q=%27Remember%20the%20ladies%27%20letter%20%28excerpt%29",
  "bp": [
   9
  ]
 },
 {
  "id": "jefferson-rough-draft-1776",
  "title": "Jefferson's Rough Draft of the Declaration (Selected Grievances, Including the Deleted Anti-Slavery Passage)",
  "type": "Government document",
  "meta": "Thomas Jefferson \u00b7 1776",
  "url": "https://tpsp.web.app/library?q=Jefferson%27s%20Rough%20Draft%20of%20the%20Declaration%20%28Selected%20Grievances%2C%20Including%20the%20Deleted%20Anti-Slavery%20Passage%29",
  "bp": [
   6
  ]
 },
 {
  "id": "address-congress-inhabitants-1778",
  "title": "Address of the Congress to the Inhabitants of the United States",
  "type": "Broadside",
  "meta": "Continental Congress \u00b7 1778",
  "url": "https://tpsp.web.app/library?q=Address%20of%20the%20Congress%20to%20the%20Inhabitants%20of%20the%20United%20States",
  "bp": [
   7
  ]
 },
 {
  "id": "washington-mercer-slavery-1786",
  "title": "Washington to John Francis Mercer on Slavery",
  "type": "Letter",
  "meta": "George Washington \u00b7 1786",
  "url": "https://tpsp.web.app/library?q=Washington%20to%20John%20Francis%20Mercer%20on%20Slavery"
 },
 {
  "id": "constitution-preamble",
  "title": "Constitution, Preamble (full text)",
  "type": "Government document",
  "meta": "Framers of the Constitution \u00b7 1787",
  "url": "https://tpsp.web.app/library?q=Constitution%2C%20Preamble%20%28full%20text%29",
  "bp": [
   13
  ]
 },
 {
  "id": "federalist-10",
  "title": "Federalist No. 10 (excerpt)",
  "type": "Newspaper",
  "meta": "James Madison \u00b7 1787",
  "url": "https://tpsp.web.app/library?q=Federalist%20No.%2010%20%28excerpt%29",
  "bp": [
   15
  ]
 },
 {
  "id": "looking-glass-1787",
  "title": "The Looking Glass for 1787",
  "type": "Political cartoon",
  "meta": "Amos Doolittle (attributed) \u00b7 1787",
  "url": "https://tpsp.web.app/library?q=The%20Looking%20Glass%20for%201787",
  "bp": [
   15
  ]
 },
 {
  "id": "washington-annotated-draft-constitution-1787",
  "title": "Washington's Annotated Draft of the Constitution",
  "type": "Government document",
  "meta": "George Washington \u00b7 1787",
  "url": "https://tpsp.web.app/library?q=Washington%27s%20Annotated%20Draft%20of%20the%20Constitution",
  "bp": [
   13
  ]
 },
 {
  "id": "madison-notes-debates-1787",
  "title": "Madison's Notes of the Debates, September 17, 1787",
  "type": "Diary",
  "meta": "James Madison \u00b7 1787",
  "url": "https://tpsp.web.app/library?q=Madison%27s%20Notes%20of%20the%20Debates%2C%20September%2017%2C%201787",
  "bp": [
   13
  ]
 },
 {
  "id": "federalist-51",
  "title": "Federalist No. 51 (excerpt)",
  "type": "Newspaper",
  "meta": "James Madison \u00b7 1788",
  "url": "https://tpsp.web.app/library?q=Federalist%20No.%2051%20%28excerpt%29",
  "bp": [
   15
  ]
 },
 {
  "id": "bill-of-rights",
  "title": "Bill of Rights (excerpts)",
  "type": "Government document",
  "meta": "First Congress \u00b7 1791",
  "url": "https://tpsp.web.app/library?q=Bill%20of%20Rights%20%28excerpts%29",
  "bp": [
   15
  ]
 },
 {
  "id": "whitney-cotton-gin-patent-1794",
  "title": "Patent Drawing for Whitney's Cotton Gin",
  "type": "Illustration",
  "meta": "Eli Whitney \u00b7 1794",
  "url": "https://tpsp.web.app/library?q=Patent%20Drawing%20for%20Whitney%27s%20Cotton%20Gin"
 },
 {
  "id": "washington-farewell-address",
  "title": "Washington's Farewell Address (excerpt)",
  "type": "Newspaper",
  "meta": "George Washington \u00b7 1796",
  "url": "https://tpsp.web.app/library?q=Washington%27s%20Farewell%20Address%20%28excerpt%29"
 },
 {
  "id": "paine-common-sense-1776",
  "title": "Common Sense",
  "type": "Pamphlet",
  "meta": "Thomas Paine \u00b7 1776",
  "url": "https://tpsp.web.app/library?q=Common%20Sense",
  "bp": [
   5
  ]
 },
 {
  "id": "olive-branch-petition-1775",
  "title": "Olive Branch Petition",
  "type": "Petition",
  "meta": "Second Continental Congress \u00b7 1775",
  "url": "https://tpsp.web.app/library?q=Olive%20Branch%20Petition",
  "bp": [
   4
  ]
 },
 {
  "id": "articles-of-confederation-1777",
  "title": "Articles of Confederation",
  "type": "Government document",
  "meta": "Second Continental Congress \u00b7 1777",
  "url": "https://tpsp.web.app/library?q=Articles%20of%20Confederation",
  "bp": [
   11
  ]
 },
 {
  "id": "brutus-no-1-1787",
  "title": "Brutus No. 1",
  "type": "Newspaper",
  "meta": "Brutus (attributed to Robert Yates) \u00b7 1787",
  "url": "https://tpsp.web.app/library?q=Brutus%20No.%201",
  "bp": [
   15
  ]
 },
 {
  "id": "virginia-statute-religious-freedom-1786",
  "title": "Virginia Statute for Religious Freedom",
  "type": "Government document",
  "meta": "Virginia General Assembly (drafted by Thomas Jefferson) \u00b7 1786",
  "url": "https://tpsp.web.app/library?q=Virginia%20Statute%20for%20Religious%20Freedom"
 }
];
window.HCG_ER_BLUEPRINT = {
  1: "Hamilton's program: funding, assumption, the Bank, and the birth of parties",
  2: "Washington's precedents: neutrality, enforcing the laws, and the Farewell Address",
  3: "The Alien and Sedition Acts: dissent prosecuted in a war scare",
  4: "The Revolution of 1800: deadlock, the peaceful transfer, and the Twelfth Amendment",
  5: "Jefferson's republic: smaller government and the Louisiana Purchase",
  6: "Marbury and judicial review: the Court claims its power",
  7: "The Corps of Discovery: crossing the continent, 1804 to 1806",
  8: "The peoples of the West: Native nations, Sacagawea, and York",
  9: "The road to war: impressment, embargo, the War Hawks, and Tecumseh's confederacy",
  10: "The War of 1812 fought and settled: Ghent, Hartford, and New Orleans",
  11: "The American System: bank, tariff, and internal improvements",
  12: "The Marshall Court's nationalism: McCulloch and Gibbons",
  13: "The Monroe Doctrine: a hemisphere declared closed",
  14: "The Missouri Compromise: slavery's line drawn, the warning heard",
  15: "Manifest Destiny and the war with Mexico: Texas, Oregon, and the cession"
};

window.HCG_ER_LESSONS = [
  { n: 1, title: "Washington's Republic: Hamilton, Parties, and the Farewell", question: "What did Washington's government have to invent, and what did it warn against as it left?" },
  { n: 2, title: "The Alien and Sedition Acts and the Revolution of 1800", question: "When the government called its critics traitors, who answered, and what did the election of 1800 prove?" },
  { n: 3, title: "Jefferson's Republic and the Louisiana Purchase", question: "How did a president elected to shrink the government double the nation's size?" },
  { n: 4, title: "Lewis and Clark and the Peoples of the West", question: "What did the Corps of Discovery actually find in the West, and whose country was it?" },
  { n: 5, title: "The War of 1812", question: "Why did the United States go to war with Britain again, and what did the war actually settle?" },
  { n: 6, title: "The Era of Good Feelings: The American System and the Marshall Court", question: "After the war, how far would Americans let their national government build?" },
  { n: 7, title: "The Monroe Doctrine and the Missouri Compromise", question: "What did the settlements of 1820 settle, and what did they only postpone?" },
  { n: 8, title: "Manifest Destiny and the War with Mexico", question: "What did Americans tell themselves expansion was, and what did the war with Mexico leave unsettled?" }
];

window.HCG_ER_ITEMS = [
  // Lesson 1
  { id: "e1-reading", lesson: 1, kind: "Reading", name: "Washington's Republic: Hamilton, Parties, and the Farewell", days: 1, tags: [1, 2], storage: "hcg/early-republic/lesson-01-reading.pdf", core: true },
  { id: "e1-notes", lesson: 1, kind: "Guided Notes", name: "Lesson 1 guided notes", days: 0, tags: [1, 2], storage: "hcg/early-republic/lesson-01-guided-notes.pdf", core: true },
  { id: "e1-activity", lesson: 1, kind: "Activity", name: "Building the Republic in Five Records", days: 1, tags: [1, 2], storage: "hcg/early-republic/lesson-01-activity.pdf", core: true },
  { id: "e1-notebook", lesson: 1, kind: "Notebook", name: "Piece of the republic chart", days: 0.5, tags: [1, 2], storage: "hcg/early-republic/lesson-01-notebook.pdf" },
  { id: "e1-quick", lesson: 1, kind: "Quick Check", name: "Hold the Country Out of the War", days: 0.5, tags: [1, 2], storage: "hcg/early-republic/lesson-01-quick-check.pdf" },
  { id: "e1-writing", lesson: 1, kind: "Writing", name: "Which Measure Made the Government Real?", days: 1, tags: [1, 2], storage: "hcg/early-republic/lesson-01-writing.pdf" },
  // Lesson 2
  { id: "e2-reading", lesson: 2, kind: "Reading", name: "The Alien and Sedition Acts and the Revolution of 1800", days: 1, tags: [3, 4], storage: "hcg/early-republic/lesson-02-reading.pdf", core: true },
  { id: "e2-notes", lesson: 2, kind: "Guided Notes", name: "Lesson 2 guided notes", days: 0, tags: [3, 4], storage: "hcg/early-republic/lesson-02-guided-notes.pdf", core: true },
  { id: "e2-activity", lesson: 2, kind: "Activity", name: "The Sedition File", days: 1, tags: [3, 4], storage: "hcg/early-republic/lesson-02-activity.pdf", core: true },
  { id: "e2-notebook", lesson: 2, kind: "Notebook", name: "Step by step chart", days: 0.5, tags: [3, 4], storage: "hcg/early-republic/lesson-02-notebook.pdf" },
  { id: "e2-quick", lesson: 2, kind: "Quick Check", name: "A Law and Its Answer", days: 0.5, tags: [3, 4], storage: "hcg/early-republic/lesson-02-quick-check.pdf" },
  { id: "e2-writing", lesson: 2, kind: "Writing", name: "Necessary Law or Party Weapon", days: 1, tags: [3, 4], storage: "hcg/early-republic/lesson-02-writing.pdf" },
  // Lesson 3
  { id: "e3-reading", lesson: 3, kind: "Reading", name: "Jefferson's Republic and the Louisiana Purchase", days: 1, tags: [5, 6], storage: "hcg/early-republic/lesson-03-reading.pdf", core: true },
  { id: "e3-notes", lesson: 3, kind: "Guided Notes", name: "Lesson 3 guided notes", days: 0, tags: [5, 6], storage: "hcg/early-republic/lesson-03-guided-notes.pdf", core: true },
  { id: "e3-activity", lesson: 3, kind: "Activity", name: "The Purchase File: Jefferson's Republic and the Louisiana Purchase", days: 1, tags: [5, 6], storage: "hcg/early-republic/lesson-03-activity.pdf", core: true },
  { id: "e3-notebook", lesson: 3, kind: "Notebook", name: "Episode by episode chart", days: 0.5, tags: [5, 6], storage: "hcg/early-republic/lesson-03-notebook.pdf" },
  { id: "e3-quick", lesson: 3, kind: "Quick Check", name: "The Purchase and the Court", days: 0.5, tags: [5, 6], storage: "hcg/early-republic/lesson-03-quick-check.pdf" },
  { id: "e3-writing", lesson: 3, kind: "Writing", name: "Against His Principles, or For Them", days: 1, tags: [5, 6], storage: "hcg/early-republic/lesson-03-writing.pdf" },
  // Lesson 4
  { id: "e4-reading", lesson: 4, kind: "Reading", name: "Lewis and Clark and the Peoples of the West", days: 1, tags: [7, 8], storage: "hcg/early-republic/lesson-04-reading.pdf", core: true },
  { id: "e4-notes", lesson: 4, kind: "Guided Notes", name: "Lesson 4 guided notes", days: 0, tags: [7, 8], storage: "hcg/early-republic/lesson-04-guided-notes.pdf", core: true },
  { id: "e4-activity", lesson: 4, kind: "Activity", name: "The Expedition File", days: 1, tags: [7, 8], storage: "hcg/early-republic/lesson-04-activity.pdf", core: true },
  { id: "e4-notebook", lesson: 4, kind: "Notebook", name: "Stage of the journey chart", days: 0.5, tags: [7, 8], storage: "hcg/early-republic/lesson-04-notebook.pdf" },
  { id: "e4-quick", lesson: 4, kind: "Quick Check", name: "The Orders and the First Day, 1803 to 1804", days: 0.5, tags: [7, 8], storage: "hcg/early-republic/lesson-04-quick-check.pdf" },
  { id: "e4-writing", lesson: 4, kind: "Writing", name: "Explorers, Diplomats, or Surveyors", days: 1, tags: [7, 8], storage: "hcg/early-republic/lesson-04-writing.pdf" },
  // Lesson 5
  { id: "e5-reading", lesson: 5, kind: "Reading", name: "The War of 1812", days: 1, tags: [9, 10], storage: "hcg/early-republic/lesson-05-reading.pdf", core: true },
  { id: "e5-notes", lesson: 5, kind: "Guided Notes", name: "Lesson 5 guided notes", days: 0, tags: [9, 10], storage: "hcg/early-republic/lesson-05-guided-notes.pdf", core: true },
  { id: "e5-activity", lesson: 5, kind: "Activity", name: "The War File", days: 1, tags: [9, 10], storage: "hcg/early-republic/lesson-05-activity.pdf", core: true },
  { id: "e5-notebook", lesson: 5, kind: "Notebook", name: "Part of the war chart", days: 0.5, tags: [9, 10], storage: "hcg/early-republic/lesson-05-notebook.pdf" },
  { id: "e5-quick", lesson: 5, kind: "Quick Check", name: "Madison's War Message, 1812", days: 0.5, tags: [9, 10], storage: "hcg/early-republic/lesson-05-quick-check.pdf" },
  { id: "e5-writing", lesson: 5, kind: "Writing", name: "Won, Lost, or Survived", days: 1, tags: [9, 10], storage: "hcg/early-republic/lesson-05-writing.pdf" },
  // Lesson 6
  { id: "e6-reading", lesson: 6, kind: "Reading", name: "The Era of Good Feelings: The American System and the Marshall Court", days: 1, tags: [11, 12], storage: "hcg/early-republic/lesson-06-reading.pdf", core: true },
  { id: "e6-notes", lesson: 6, kind: "Guided Notes", name: "Lesson 6 guided notes", days: 0, tags: [11, 12], storage: "hcg/early-republic/lesson-06-guided-notes.pdf", core: true },
  { id: "e6-activity", lesson: 6, kind: "Activity", name: "The Nationalism File: How Far Would the National Government Build?", days: 1, tags: [11, 12], storage: "hcg/early-republic/lesson-06-activity.pdf", core: true },
  { id: "e6-notebook", lesson: 6, kind: "Notebook", name: "Part by part chart", days: 0.5, tags: [11, 12], storage: "hcg/early-republic/lesson-06-notebook.pdf" },
  { id: "e6-quick", lesson: 6, kind: "Quick Check", name: "The Reach and Its Limits", days: 0.5, tags: [11, 12], storage: "hcg/early-republic/lesson-06-quick-check.pdf" },
  { id: "e6-writing", lesson: 6, kind: "Writing", name: "Hamilton's Program Fulfilled, or a New Thing?", days: 1, tags: [11, 12], storage: "hcg/early-republic/lesson-06-writing.pdf" },
  // Lesson 7
  { id: "e7-reading", lesson: 7, kind: "Reading", name: "The Monroe Doctrine and the Missouri Compromise", days: 1, tags: [13, 14], storage: "hcg/early-republic/lesson-07-reading.pdf", core: true },
  { id: "e7-notes", lesson: 7, kind: "Guided Notes", name: "Lesson 7 guided notes", days: 0, tags: [13, 14], storage: "hcg/early-republic/lesson-07-guided-notes.pdf", core: true },
  { id: "e7-activity", lesson: 7, kind: "Activity", name: "The Settlements File", days: 1, tags: [13, 14], storage: "hcg/early-republic/lesson-07-activity.pdf", core: true },
  { id: "e7-notebook", lesson: 7, kind: "Notebook", name: "Compromise line chart", days: 0.5, tags: [13, 14], storage: "hcg/early-republic/lesson-07-notebook.pdf" },
  { id: "e7-quick", lesson: 7, kind: "Quick Check", name: "A Hemisphere Declared, A Line Drawn", days: 0.5, tags: [13, 14], storage: "hcg/early-republic/lesson-07-quick-check.pdf" },
  { id: "e7-writing", lesson: 7, kind: "Writing", name: "Settled, or Only Postponed", days: 1, tags: [13, 14], storage: "hcg/early-republic/lesson-07-writing.pdf" },
  // Lesson 8
  { id: "e8-reading", lesson: 8, kind: "Reading", name: "Manifest Destiny and the War with Mexico", days: 1, tags: [15], storage: "hcg/early-republic/lesson-08-reading.pdf", core: true },
  { id: "e8-notes", lesson: 8, kind: "Guided Notes", name: "Lesson 8 guided notes", days: 0, tags: [15], storage: "hcg/early-republic/lesson-08-guided-notes.pdf", core: true },
  { id: "e8-activity", lesson: 8, kind: "Activity", name: "The Expansion File", days: 1, tags: [15], storage: "hcg/early-republic/lesson-08-activity.pdf", core: true },
  { id: "e8-notebook", lesson: 8, kind: "Notebook", name: "Record by record chart", days: 0.5, tags: [15], storage: "hcg/early-republic/lesson-08-notebook.pdf" },
  { id: "e8-quick", lesson: 8, kind: "Quick Check", name: "Blood on Which Soil", days: 0.5, tags: [15], storage: "hcg/early-republic/lesson-08-quick-check.pdf" },
  { id: "e8-writing", lesson: 8, kind: "Writing", name: "Describe or Disguise", days: 1, tags: [15], storage: "hcg/early-republic/lesson-08-writing.pdf" },
  // Review day
  { id: "erev-guide", lesson: 9, kind: "Review", name: "Study guide (review day)", days: 1, tags: [], storage: "hcg/early-republic/review-study-guide.pdf", core: true },
  { id: "erev-cross", lesson: 9, kind: "Review", name: "Crossword (56 answers)", days: 0.5, tags: [], storage: "hcg/early-republic/review-crossword.pdf" }
];

window.HCG_ER_TOPICS = {
  1: { label: "Inventing a government: precedent, finance, and the first parties", note: "" },
  2: { label: "The republic tested: dissent, succession, and the courts", note: "" },
  3: { label: "A continental republic: purchase, exploration, and the peoples of the West", note: "" },
  4: { label: "The second war and the nationalist turn", note: "" },
  5: { label: "The Marshall Court and the national economy", note: "" },
  6: { label: "Expansion and the question deferred: Monroe, Missouri, and Mexico", note: "" }
};
window.HCG_ER_BP_TOPIC = {
  1: [1], 2: [1], 3: [1, 2], 4: [2], 5: [3], 6: [2], 7: [3], 8: [3], 9: [4], 10: [4], 11: [4, 5], 12: [5], 13: [6], 14: [6], 15: [6]
};

// TPSP picker index for Early Republic and Expansion: the unit's two
// premium DBQs first, both straddling into this unit's ground and
// verified in Firestore (collection psp_premium) for this pass, dbq9,
// "Was Westward Expansion a Story of Opportunity or Conquest?"
// (catalog code DBQ184, era "Westward Expansion"), whose first two
// documents are this unit's Lesson 8 records, leading, and dbq7,
// "Did the Constitution Create a Democratic Government?" (catalog
// code DBQ182, era "Founding and Early Republic"), whose last two
// documents are this unit's Farewell Address and Missouri
// Compromise, alongside it; then the four records the unit draws
// from other era files (the Farewell Address and the cotton gin
// patent from the founding era file, which The Founding's picker
// deliberately left untagged because they belong to this unit, and
// O'Sullivan's annexation essay and the Treaty of Guadalupe Hidalgo
// from the Jackson and reform era file), then the era sources from
// the TPSP library file early-republic.json in file order, each
// with conservative blueprint pre-tags where the source names the
// entry's content. Two source records are deliberately left
// untagged: the cotton gin patent drawing and the Lansdowne
// portrait of Washington, neither of which names any single
// blueprint entry's content.
window.HCG_TPSP_ER = [
 {
  "id": "dbq9",
  "title": "Was Westward Expansion a Story of Opportunity or Conquest?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true
 },
 {
  "id": "dbq7",
  "title": "Did the Constitution Create a Democratic Government?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true
 },
 {
  "id": "washington-farewell-address",
  "title": "Washington's Farewell Address (excerpt)",
  "type": "Newspaper",
  "meta": "George Washington · 1796",
  "url": "https://tpsp.web.app/library?q=Washington%27s%20Farewell%20Address%20%28excerpt%29",
  "bp": [
   2
  ]
 },
 {
  "id": "whitney-cotton-gin-patent-1794",
  "title": "Patent Drawing for Whitney's Cotton Gin",
  "type": "Illustration",
  "meta": "Eli Whitney · 1794",
  "url": "https://tpsp.web.app/library?q=Patent%20Drawing%20for%20Whitney%27s%20Cotton%20Gin"
 },
 {
  "id": "osullivan-annexation-1845",
  "title": "Annexation Editorial (coining \"Manifest Destiny\")",
  "type": "Magazine",
  "meta": "John L. O'Sullivan · 1845",
  "url": "https://tpsp.web.app/library?q=Annexation%20Editorial%20%28coining%20%22Manifest%20Destiny%22%29",
  "bp": [
   15
  ]
 },
 {
  "id": "treaty-guadalupe-hidalgo-1848",
  "title": "Treaty of Guadalupe Hidalgo",
  "type": "Government document",
  "meta": "United States and Mexico · 1848",
  "url": "https://tpsp.web.app/library?q=Treaty%20of%20Guadalupe%20Hidalgo",
  "bp": [
   15
  ]
 },
 {
  "id": "treaty-greenville-1795",
  "title": "Treaty of Greenville",
  "type": "Government document",
  "meta": "United States and the Western Confederacy tribes · 1795",
  "url": "https://tpsp.web.app/library?q=Treaty%20of%20Greenville",
  "bp": [
   8
  ]
 },
 {
  "id": "lansdowne-washington-1796",
  "title": "George Washington (Lansdowne Portrait)",
  "type": "Painting",
  "meta": "Gilbert Stuart · 1796",
  "url": "https://tpsp.web.app/library?q=George%20Washington%20%28Lansdowne%20Portrait%29"
 },
 {
  "id": "virginia-resolutions-1798",
  "title": "Virginia Resolutions (excerpt)",
  "type": "Government document",
  "meta": "James Madison (for the Virginia legislature) · 1798",
  "url": "https://tpsp.web.app/library?q=Virginia%20Resolutions%20%28excerpt%29",
  "bp": [
   3
  ]
 },
 {
  "id": "marbury-v-madison",
  "title": "Marbury v. Madison (excerpts)",
  "type": "Court decision",
  "meta": "Chief Justice John Marshall · 1803",
  "url": "https://tpsp.web.app/library?q=Marbury%20v.%20Madison%20%28excerpts%29",
  "bp": [
   6
  ]
 },
 {
  "id": "lewis-clark-journals-1804",
  "title": "Journals of Lewis and Clark (May 14, 1804)",
  "type": "Diary",
  "meta": "William Clark · 1804",
  "url": "https://tpsp.web.app/library?q=Journals%20of%20Lewis%20and%20Clark%20%28May%2014%2C%201804%29",
  "bp": [
   7
  ]
 },
 {
  "id": "mcculloch-v-maryland",
  "title": "McCulloch v. Maryland (excerpts)",
  "type": "Court decision",
  "meta": "Chief Justice John Marshall · 1819",
  "url": "https://tpsp.web.app/library?q=McCulloch%20v.%20Maryland%20%28excerpts%29",
  "bp": [
   12
  ]
 },
 {
  "id": "monroe-doctrine",
  "title": "Monroe Doctrine (excerpts)",
  "type": "Government document",
  "meta": "President James Monroe · 1823",
  "url": "https://tpsp.web.app/library?q=Monroe%20Doctrine%20%28excerpts%29",
  "bp": [
   13
  ]
 },
 {
  "id": "alien-and-sedition-acts-1798",
  "title": "The Alien and Sedition Acts (excerpts)",
  "type": "Government document",
  "meta": "U.S. Congress (signed by President John Adams) · 1798",
  "url": "https://tpsp.web.app/library?q=The%20Alien%20and%20Sedition%20Acts%20%28excerpts%29",
  "bp": [
   3
  ]
 },
 {
  "id": "jefferson-kentucky-resolutions-1798",
  "title": "Draft of the Kentucky Resolutions",
  "type": "Government document",
  "meta": "Thomas Jefferson · 1798",
  "url": "https://tpsp.web.app/library?q=Draft%20of%20the%20Kentucky%20Resolutions",
  "bp": [
   3
  ]
 },
 {
  "id": "louisiana-purchase-treaty-1803",
  "title": "Louisiana Purchase Treaty (excerpts)",
  "type": "Government document",
  "meta": "United States and the French Republic · 1803",
  "url": "https://tpsp.web.app/library?q=Louisiana%20Purchase%20Treaty%20%28excerpts%29",
  "bp": [
   5
  ]
 },
 {
  "id": "missouri-compromise-1820",
  "title": "The Missouri Compromise (excerpts)",
  "type": "Government document",
  "meta": "U.S. Congress (signed by President James Monroe) · 1820",
  "url": "https://tpsp.web.app/library?q=The%20Missouri%20Compromise%20%28excerpts%29",
  "bp": [
   14
  ]
 },
 {
  "id": "madison-war-message-1812",
  "title": "War Message to Congress",
  "type": "Government document",
  "meta": "James Madison · 1812",
  "url": "https://tpsp.web.app/library?q=War%20Message%20to%20Congress",
  "bp": [
   9
  ]
 },
 {
  "id": "jefferson-first-inaugural-1801",
  "title": "First Inaugural Address",
  "type": "Speech",
  "meta": "Thomas Jefferson · 1801",
  "url": "https://tpsp.web.app/library?q=First%20Inaugural%20Address",
  "bp": [
   4
  ]
 },
 {
  "id": "hamilton-bank-opinion-1791",
  "title": "Opinion on the Constitutionality of the Bank",
  "type": "Government document",
  "meta": "Alexander Hamilton · 1791",
  "url": "https://tpsp.web.app/library?q=Opinion%20on%20the%20Constitutionality%20of%20the%20Bank",
  "bp": [
   1
  ]
 },
 {
  "id": "washington-neutrality-proclamation-1793",
  "title": "Proclamation of Neutrality",
  "type": "Government document",
  "meta": "George Washington · 1793",
  "url": "https://tpsp.web.app/library?q=Proclamation%20of%20Neutrality",
  "bp": [
   2
  ]
 },
 {
  "id": "jay-treaty-1794",
  "title": "Jay Treaty",
  "type": "Government document",
  "meta": "John Jay and Lord Grenville · 1794",
  "url": "https://tpsp.web.app/library?q=Jay%20Treaty",
  "bp": [
   2
  ]
 },
 {
  "id": "embargo-act-1807",
  "title": "Embargo Act",
  "type": "Government document",
  "meta": "10th U.S. Congress · 1807",
  "url": "https://tpsp.web.app/library?q=Embargo%20Act",
  "bp": [
   9
  ]
 },
 {
  "id": "star-spangled-banner-1814",
  "title": "\"The Star-Spangled Banner\" (full four stanzas)",
  "type": "Poem",
  "meta": "Francis Scott Key · 1814",
  "url": "https://tpsp.web.app/library?q=%22The%20Star-Spangled%20Banner%22%20%28full%20four%20stanzas%29",
  "bp": [
   10
  ]
 },
 {
  "id": "gibbons-v-ogden-1824",
  "title": "Gibbons v. Ogden",
  "type": "Court decision",
  "meta": "U.S. Supreme Court (Chief Justice John Marshall) · 1824",
  "url": "https://tpsp.web.app/library?q=Gibbons%20v.%20Ogden",
  "bp": [
   12
  ]
 },
 {
  "id": "hartford-convention-resolutions-1815",
  "title": "Hartford Convention Resolutions",
  "type": "Government document",
  "meta": "Hartford Convention delegates · 1815",
  "url": "https://tpsp.web.app/library?q=Hartford%20Convention%20Resolutions",
  "bp": [
   10
  ]
 }
];

window.HCG_JR_BLUEPRINT = {
  1: "The election of 1828: the widening electorate and the people's president",
  2: "Jacksonian democracy in office: spoils, rotation, and the party",
  3: "Indian removal: the act, the message, and the southeastern nations",
  4: "The Cherokee case and the Trail of Tears: law defied and removal carried out",
  5: "Nullification: Calhoun's doctrine and South Carolina's ordinance",
  6: "The crisis settled: the Force Bill, the compromise tariff, and Jackson's Union",
  7: "The Bank War: the veto and the removal of the deposits",
  8: "Panic and party: 1837 and the rise of the Whigs",
  9: "The market revolution: transport, communication, and the factory",
  10: "Lowell and labor: the mill women and the first unions",
  11: "The Second Great Awakening: revival and the reform impulse",
  12: "Reforming institutions: temperance, common schools, and asylums",
  13: "Abolition turns immediate: Walker, Turner, and Garrison",
  14: "Abolition organized and answered: societies, petitions, and the gag rule",
  15: "Women's rights: Seneca Falls and the Declaration of Sentiments"
};

window.HCG_JR_LESSONS = [
  { n: 1, title: "The Election of 1828 and Jacksonian Democracy", question: "What changed when the common white man got the vote, and who was still left outside it?" },
  { n: 2, title: "Indian Removal", question: "How did the United States take the Southeast, and what did the Cherokee do to stop it?" },
  { n: 3, title: "The Nullification Crisis", question: "Could a state veto the Union, and what made South Carolina back down?" },
  { n: 4, title: "The Bank War and the Panic", question: "Was the Bank a public good or a private monster, and who paid when it fell?" },
  { n: 5, title: "The Market Revolution: Factories, Canals, and Wires", question: "What did the factory and the telegraph do to the way Americans lived and worked?" },
  { n: 6, title: "Revival and Reform: The Second Great Awakening", question: "Why did revival produce reformers, and what did they set out to fix first?" },
  { n: 7, title: "Abolition Turns Immediate", question: "What changed when abolitionists stopped asking gradually, and how did the country answer?" },
  { n: 8, title: "Women's Rights and Seneca Falls", question: "Where did the women of 1848 get their argument, and what did they ask for first?" }
];

window.HCG_JR_ITEMS = [
  // Lesson 1
  { id: "j1-reading", lesson: 1, kind: "Reading", name: "The Election of 1828 and Jacksonian Democracy", days: 1, tags: [1, 2], storage: "hcg/jackson-reform/lesson-01-reading.pdf", core: true },
  { id: "j1-notes", lesson: 1, kind: "Guided Notes", name: "Lesson 1 guided notes", days: 0, tags: [1, 2], storage: "hcg/jackson-reform/lesson-01-guided-notes.pdf", core: true },
  { id: "j1-activity", lesson: 1, kind: "Activity", name: "The People's President File", days: 1, tags: [1, 2], storage: "hcg/jackson-reform/lesson-01-activity.pdf", core: true },
  { id: "j1-notebook", lesson: 1, kind: "Notebook", name: "Piece of the story chart", days: 0.5, tags: [1, 2], storage: "hcg/jackson-reform/lesson-01-notebook.pdf" },
  { id: "j1-quick", lesson: 1, kind: "Quick Check", name: "Office Is Not Property", days: 0.5, tags: [1, 2], storage: "hcg/jackson-reform/lesson-01-quick-check.pdf" },
  { id: "j1-writing", lesson: 1, kind: "Writing", name: "The Birth of Democratic Politics?", days: 1, tags: [1, 2], storage: "hcg/jackson-reform/lesson-01-writing.pdf" },
  // Lesson 2
  { id: "j2-reading", lesson: 2, kind: "Reading", name: "Indian Removal", days: 1, tags: [3, 4], storage: "hcg/jackson-reform/lesson-02-reading.pdf", core: true },
  { id: "j2-notes", lesson: 2, kind: "Guided Notes", name: "Lesson 2 guided notes", days: 0, tags: [3, 4], storage: "hcg/jackson-reform/lesson-02-guided-notes.pdf", core: true },
  { id: "j2-activity", lesson: 2, kind: "Activity", name: "The Removal File", days: 1, tags: [3, 4], storage: "hcg/jackson-reform/lesson-02-activity.pdf", core: true },
  { id: "j2-notebook", lesson: 2, kind: "Notebook", name: "Step by step chart", days: 0.5, tags: [3, 4], storage: "hcg/jackson-reform/lesson-02-notebook.pdf" },
  { id: "j2-quick", lesson: 2, kind: "Quick Check", name: "A Judgment and a Treaty", days: 0.5, tags: [3, 4], storage: "hcg/jackson-reform/lesson-02-quick-check.pdf" },
  { id: "j2-writing", lesson: 2, kind: "Writing", name: "A Policy of Law or of Force", days: 1, tags: [3, 4], storage: "hcg/jackson-reform/lesson-02-writing.pdf" },
  // Lesson 3
  { id: "j3-reading", lesson: 3, kind: "Reading", name: "The Nullification Crisis", days: 1, tags: [5, 6], storage: "hcg/jackson-reform/lesson-03-reading.pdf", core: true },
  { id: "j3-notes", lesson: 3, kind: "Guided Notes", name: "Lesson 3 guided notes", days: 0, tags: [5, 6], storage: "hcg/jackson-reform/lesson-03-guided-notes.pdf", core: true },
  { id: "j3-activity", lesson: 3, kind: "Activity", name: "The Nullification File: The Nullification Crisis", days: 1, tags: [5, 6], storage: "hcg/jackson-reform/lesson-03-activity.pdf", core: true },
  { id: "j3-notebook", lesson: 3, kind: "Notebook", name: "Episode by episode chart", days: 0.5, tags: [5, 6], storage: "hcg/jackson-reform/lesson-03-notebook.pdf" },
  { id: "j3-quick", lesson: 3, kind: "Quick Check", name: "The Veto and the Answer", days: 0.5, tags: [5, 6], storage: "hcg/jackson-reform/lesson-03-quick-check.pdf" },
  { id: "j3-writing", lesson: 3, kind: "Writing", name: "What Made South Carolina Back Down?", days: 1, tags: [5, 6], storage: "hcg/jackson-reform/lesson-03-writing.pdf" },
  // Lesson 4
  { id: "j4-reading", lesson: 4, kind: "Reading", name: "The Bank War and the Panic", days: 1, tags: [7, 8], storage: "hcg/jackson-reform/lesson-04-reading.pdf", core: true },
  { id: "j4-notes", lesson: 4, kind: "Guided Notes", name: "Lesson 4 guided notes", days: 0, tags: [7, 8], storage: "hcg/jackson-reform/lesson-04-guided-notes.pdf", core: true },
  { id: "j4-activity", lesson: 4, kind: "Activity", name: "The Bank File", days: 1, tags: [7, 8], storage: "hcg/jackson-reform/lesson-04-activity.pdf", core: true },
  { id: "j4-notebook", lesson: 4, kind: "Notebook", name: "Stage of the struggle chart", days: 0.5, tags: [7, 8], storage: "hcg/jackson-reform/lesson-04-notebook.pdf" },
  { id: "j4-quick", lesson: 4, kind: "Quick Check", name: "The Veto and the Circular, 1832 to 1836", days: 0.5, tags: [7, 8], storage: "hcg/jackson-reform/lesson-04-quick-check.pdf" },
  { id: "j4-writing", lesson: 4, kind: "Writing", name: "Public Good or Private Power", days: 1, tags: [7, 8], storage: "hcg/jackson-reform/lesson-04-writing.pdf" },
  // Lesson 5
  { id: "j5-reading", lesson: 5, kind: "Reading", name: "The Market Revolution: Factories, Canals, and Wires", days: 1, tags: [9, 10], storage: "hcg/jackson-reform/lesson-05-reading.pdf", core: true },
  { id: "j5-notes", lesson: 5, kind: "Guided Notes", name: "Lesson 5 guided notes", days: 0, tags: [9, 10], storage: "hcg/jackson-reform/lesson-05-guided-notes.pdf", core: true },
  { id: "j5-activity", lesson: 5, kind: "Activity", name: "The Market Revolution File", days: 1, tags: [9, 10], storage: "hcg/jackson-reform/lesson-05-activity.pdf", core: true },
  { id: "j5-notebook", lesson: 5, kind: "Notebook", name: "Part of the change chart", days: 0.5, tags: [9, 10], storage: "hcg/jackson-reform/lesson-05-notebook.pdf" },
  { id: "j5-quick", lesson: 5, kind: "Quick Check", name: "The Mill Woman and the Wire, 1840 to 1844", days: 0.5, tags: [9, 10], storage: "hcg/jackson-reform/lesson-05-quick-check.pdf" },
  { id: "j5-writing", lesson: 5, kind: "Writing", name: "More Control, or Less", days: 1, tags: [9, 10], storage: "hcg/jackson-reform/lesson-05-writing.pdf" },
  // Lesson 6
  { id: "j6-reading", lesson: 6, kind: "Reading", name: "Revival and Reform: The Second Great Awakening", days: 1, tags: [11, 12], storage: "hcg/jackson-reform/lesson-06-reading.pdf", core: true },
  { id: "j6-notes", lesson: 6, kind: "Guided Notes", name: "Lesson 6 guided notes", days: 0, tags: [11, 12], storage: "hcg/jackson-reform/lesson-06-guided-notes.pdf", core: true },
  { id: "j6-activity", lesson: 6, kind: "Activity", name: "The Reform File: Why Did Revival Produce Reformers?", days: 1, tags: [11, 12], storage: "hcg/jackson-reform/lesson-06-activity.pdf", core: true },
  { id: "j6-notebook", lesson: 6, kind: "Notebook", name: "Part by part chart", days: 0.5, tags: [11, 12], storage: "hcg/jackson-reform/lesson-06-notebook.pdf" },
  { id: "j6-quick", lesson: 6, kind: "Quick Check", name: "The Will and the Remedy", days: 0.5, tags: [11, 12], storage: "hcg/jackson-reform/lesson-06-quick-check.pdf" },
  { id: "j6-writing", lesson: 6, kind: "Writing", name: "Why Did Revival Produce Reformers?", days: 1, tags: [11, 12], storage: "hcg/jackson-reform/lesson-06-writing.pdf" },
  // Lesson 7
  { id: "j7-reading", lesson: 7, kind: "Reading", name: "Abolition Turns Immediate", days: 1, tags: [13, 14], storage: "hcg/jackson-reform/lesson-07-reading.pdf", core: true },
  { id: "j7-notes", lesson: 7, kind: "Guided Notes", name: "Lesson 7 guided notes", days: 0, tags: [13, 14], storage: "hcg/jackson-reform/lesson-07-guided-notes.pdf", core: true },
  { id: "j7-activity", lesson: 7, kind: "Activity", name: "The Immediatism File", days: 1, tags: [13, 14], storage: "hcg/jackson-reform/lesson-07-activity.pdf", core: true },
  { id: "j7-notebook", lesson: 7, kind: "Notebook", name: "Record by record chart", days: 0.5, tags: [13, 14], storage: "hcg/jackson-reform/lesson-07-notebook.pdf" },
  { id: "j7-quick", lesson: 7, kind: "Quick Check", name: "The Asking Stops", days: 0.5, tags: [13, 14], storage: "hcg/jackson-reform/lesson-07-quick-check.pdf" },
  { id: "j7-writing", lesson: 7, kind: "Writing", name: "What Changed When the Asking Stopped", days: 1, tags: [13, 14], storage: "hcg/jackson-reform/lesson-07-writing.pdf" },
  // Lesson 8
  { id: "j8-reading", lesson: 8, kind: "Reading", name: "Women's Rights and Seneca Falls", days: 1, tags: [15], storage: "hcg/jackson-reform/lesson-08-reading.pdf", core: true },
  { id: "j8-notes", lesson: 8, kind: "Guided Notes", name: "Lesson 8 guided notes", days: 0, tags: [15], storage: "hcg/jackson-reform/lesson-08-guided-notes.pdf", core: true },
  { id: "j8-activity", lesson: 8, kind: "Activity", name: "The Seneca Falls File", days: 1, tags: [15], storage: "hcg/jackson-reform/lesson-08-activity.pdf", core: true },
  { id: "j8-notebook", lesson: 8, kind: "Notebook", name: "Piece by piece chart", days: 0.5, tags: [15], storage: "hcg/jackson-reform/lesson-08-notebook.pdf" },
  { id: "j8-quick", lesson: 8, kind: "Quick Check", name: "Civilly Dead", days: 0.5, tags: [15], storage: "hcg/jackson-reform/lesson-08-quick-check.pdf" },
  { id: "j8-writing", lesson: 8, kind: "Writing", name: "The Argument They Borrowed", days: 1, tags: [15], storage: "hcg/jackson-reform/lesson-08-writing.pdf" },
  // Review day
  { id: "jrev-guide", lesson: 9, kind: "Review", name: "Study guide (review day)", days: 1, tags: [], storage: "hcg/jackson-reform/review-study-guide.pdf", core: true },
  { id: "jrev-cross", lesson: 9, kind: "Review", name: "Crossword (56 answers)", days: 0.5, tags: [], storage: "hcg/jackson-reform/review-crossword.pdf" }
];

window.HCG_JR_TOPICS = {
  1: { label: "Democracy widened: suffrage, parties, and the people's president", note: "" },
  2: { label: "Removal: the republic and the Native nations of the Southeast", note: "" },
  3: { label: "The Union tested: nullification, the bank, and the limits of federal power", note: "" },
  4: { label: "The market remade: factories, transport, and communication", note: "" },
  5: { label: "Revival and reform: awakening, temperance, schools, and asylums", note: "" },
  6: { label: "Freedom's claims widened: abolition and women's rights", note: "" }
};

window.HCG_JR_BP_TOPIC = {
  1: [1], 2: [1], 3: [2], 4: [2], 5: [3], 6: [3], 7: [3], 8: [3, 4], 9: [4], 10: [4], 11: [5], 12: [5], 13: [6], 14: [6], 15: [6]
};

// TPSP picker index for Jackson and Reform: the unit's two premium
// DBQs first, both verified in Firestore (collection psp_premium)
// for this pass: dbq8, "Did Andrew Jackson Expand Democracy or
// Abuse Power?" (catalog code DBQ183, era "Jacksonian America"),
// whose seven documents all sit on this unit's ground and are all
// taught in its lessons, leading, and dbq14, "What Strategies Did
// Reformers Use to Force Change?" (catalog code DBQ189, era
// "Jacksonian America and Reform"), four of whose seven documents
// are taught here and three of which belong to the Sectional Crisis
// unit, alongside it; then the era sources from the TPSP library
// file jackson-reform.json in file order, each with conservative
// blueprint pre-tags where the source names the entry's content.
// Twelve of the 22 sources are pre-tagged; ten are deliberately
// left untagged: the Baptism of Pocahontas painting and the
// Washington Crossing the Delaware painting (other units'
// subjects), Lincoln's 1841 letter to Mary Speed (a private letter
// the unit does not teach), O'Sullivan's annexation essay and the
// Treaty of Guadalupe Hidalgo (the Early Republic unit's closing
// documents, prior knowledge here), and Sojourner Truth's 1851
// speech, Douglass's 1852 Fourth of July oration, the House
// Divided speech, Douglass's 1857 letter to Hugh Auld, and Dred
// Scott (all the Sectional Crisis unit's ground).
window.HCG_TPSP_JR = [
 {
  "id": "dbq8",
  "title": "Did Andrew Jackson Expand Democracy or Abuse Power?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true
 },
 {
  "id": "dbq14",
  "title": "What Strategies Did Reformers Use to Force Change?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true
 },
 {
  "id": "jackson-indian-removal-message-1830",
  "title": "Message to Congress \"On Indian Removal\"",
  "type": "Government document",
  "meta": "Andrew Jackson · 1830",
  "url": "https://tpsp.web.app/library?q=Message%20to%20Congress%20%22On%20Indian%20Removal%22",
  "bp": [
   3
  ]
 },
 {
  "id": "jackson-bank-veto-1832",
  "title": "Bank Veto Message (excerpt)",
  "type": "Government document",
  "meta": "Andrew Jackson · 1832",
  "url": "https://tpsp.web.app/library?q=Bank%20Veto%20Message%20%28excerpt%29",
  "bp": [
   7
  ]
 },
 {
  "id": "south-carolina-nullification-1832",
  "title": "Ordinance of Nullification (excerpt)",
  "type": "Government document",
  "meta": "South Carolina Convention · 1832",
  "url": "https://tpsp.web.app/library?q=Ordinance%20of%20Nullification%20%28excerpt%29",
  "bp": [
   5
  ]
 },
 {
  "id": "king-andrew-first-1833",
  "title": "King Andrew the First",
  "type": "Political cartoon",
  "meta": "Unknown artist · 1833",
  "url": "https://tpsp.web.app/library?q=King%20Andrew%20the%20First",
  "bp": [
   7
  ]
 },
 {
  "id": "baptism-of-pocahontas-1840",
  "title": "Baptism of Pocahontas",
  "type": "Painting",
  "meta": "John Gadsby Chapman · 1840",
  "url": "https://tpsp.web.app/library?q=Baptism%20of%20Pocahontas"
 },
 {
  "id": "lowell-mill-girls-1840",
  "title": "Lowell Mill Girls and the Factory System, 1840",
  "type": "Magazine",
  "meta": "Probably Harriet Jane Farley (\"A Factory Girl\"), Lowell Offering · 1840",
  "url": "https://tpsp.web.app/library?q=Lowell%20Mill%20Girls%20and%20the%20Factory%20System%2C%201840",
  "bp": [
   10
  ]
 },
 {
  "id": "lincoln-to-mary-speed-1841",
  "title": "Letter to Mary Speed",
  "type": "Letter",
  "meta": "Abraham Lincoln · 1841",
  "url": "https://tpsp.web.app/library?q=Letter%20to%20Mary%20Speed"
 },
 {
  "id": "morse-first-telegraph-message-1844",
  "title": "\"First Telegraphic Message - 24 May 1844\"",
  "type": "Other",
  "meta": "Samuel F. B. Morse · 1844",
  "url": "https://tpsp.web.app/library?q=%22First%20Telegraphic%20Message%20-%2024%20May%201844%22",
  "bp": [
   9
  ]
 },
 {
  "id": "osullivan-annexation-1845",
  "title": "Annexation Editorial (coining \"Manifest Destiny\")",
  "type": "Magazine",
  "meta": "John L. O'Sullivan · 1845",
  "url": "https://tpsp.web.app/library?q=Annexation%20Editorial%20%28coining%20%22Manifest%20Destiny%22%29"
 },
 {
  "id": "seneca-falls-declaration-1848",
  "title": "Declaration of Sentiments (excerpt)",
  "type": "Other",
  "meta": "Elizabeth Cady Stanton and the Seneca Falls Convention · 1848",
  "url": "https://tpsp.web.app/library?q=Declaration%20of%20Sentiments%20%28excerpt%29",
  "bp": [
   15
  ]
 },
 {
  "id": "treaty-guadalupe-hidalgo-1848",
  "title": "Treaty of Guadalupe Hidalgo",
  "type": "Government document",
  "meta": "United States and Mexico · 1848",
  "url": "https://tpsp.web.app/library?q=Treaty%20of%20Guadalupe%20Hidalgo"
 },
 {
  "id": "seneca-falls-report-1848",
  "title": "Report of the Woman's Rights Convention (Declaration of Sentiments), Seneca Falls, July 19-20, 1848",
  "type": "Pamphlet",
  "meta": "Elizabeth Cady Stanton · 1848",
  "url": "https://tpsp.web.app/library?q=Report%20of%20the%20Woman%27s%20Rights%20Convention%20%28Declaration%20of%20Sentiments%29%2C%20Seneca%20Falls%2C%20July%2019-20%2C%201848",
  "bp": [
   15
  ]
 },
 {
  "id": "sojourner-truth-aint-i-a-woman-1851",
  "title": "\"Ain't I a Woman?\" (excerpt)",
  "type": "Speech",
  "meta": "Sojourner Truth · 1851",
  "url": "https://tpsp.web.app/library?q=%22Ain%27t%20I%20a%20Woman%3F%22%20%28excerpt%29"
 },
 {
  "id": "douglass-fourth-of-july-1852",
  "title": "\"What to the Slave Is the Fourth of July?\" (excerpt)",
  "type": "Speech",
  "meta": "Frederick Douglass · 1852",
  "url": "https://tpsp.web.app/library?q=%22What%20to%20the%20Slave%20Is%20the%20Fourth%20of%20July%3F%22%20%28excerpt%29"
 },
 {
  "id": "house-divided-speech-1858",
  "title": "The \"House Divided\" Speech",
  "type": "Speech",
  "meta": "Abraham Lincoln · 1857-1858",
  "url": "https://tpsp.web.app/library?q=The%20%22House%20Divided%22%20Speech"
 },
 {
  "id": "douglass-to-hugh-auld-1857",
  "title": "\"I Love You But Hate Slavery\": Frederick Douglass to His Former Master, Hugh Auld",
  "type": "Letter",
  "meta": "Frederick Douglass · 1857",
  "url": "https://tpsp.web.app/library?q=%22I%20Love%20You%20But%20Hate%20Slavery%22%3A%20Frederick%20Douglass%20to%20His%20Former%20Master%2C%20Hugh%20Auld"
 },
 {
  "id": "washington-crossing-delaware-1851",
  "title": "Washington Crossing the Delaware",
  "type": "Painting",
  "meta": "Emanuel Leutze · 1851",
  "url": "https://tpsp.web.app/library?q=Washington%20Crossing%20the%20Delaware"
 },
 {
  "id": "worcester-v-georgia-1832",
  "title": "Worcester v. Georgia",
  "type": "Court decision",
  "meta": "U.S. Supreme Court (Chief Justice John Marshall) · 1832",
  "url": "https://tpsp.web.app/library?q=Worcester%20v.%20Georgia",
  "bp": [
   4
  ]
 },
 {
  "id": "south-carolina-exposition-and-protest-1828",
  "title": "South Carolina Exposition and Protest",
  "type": "Government document",
  "meta": "South Carolina Legislature (written by John C. Calhoun) · 1828",
  "url": "https://tpsp.web.app/library?q=South%20Carolina%20Exposition%20and%20Protest",
  "bp": [
   5
  ]
 },
 {
  "id": "garrison-to-the-public-1831",
  "title": "\"To the Public\"",
  "type": "Newspaper",
  "meta": "William Lloyd Garrison · 1831",
  "url": "https://tpsp.web.app/library?q=%22To%20the%20Public%22",
  "bp": [
   13
  ]
 },
 {
  "id": "walker-appeal-1829",
  "title": "Walker's Appeal",
  "type": "Pamphlet",
  "meta": "David Walker · 1829",
  "url": "https://tpsp.web.app/library?q=Walker%27s%20Appeal",
  "bp": [
   13
  ]
 },
 {
  "id": "dred-scott-v-sandford-1857",
  "title": "Dred Scott v. Sandford",
  "type": "Court decision",
  "meta": "U.S. Supreme Court (Chief Justice Roger B. Taney) · 1857",
  "url": "https://tpsp.web.app/library?q=Dred%20Scott%20v.%20Sandford"
 }
];

window.HCG_SC_BLUEPRINT = {
  1: "The Compromise of 1850: Clay's settlement and its terms",
  2: "The Fugitive Slave Act: enforcement in the North",
  3: "The antislavery argument: Uncle Tom's Cabin and the case against slavery",
  4: "Witness and resistance: Truth, Douglass, and the fugitive fights",
  5: "The Kansas-Nebraska Act: popular sovereignty and the Missouri line repealed",
  6: "Bleeding Kansas: two governments and the violence",
  7: "The Republican Party: a sectional party on free labor",
  8: "Dred Scott: the Court's settlement and its answer",
  9: "The Lincoln-Douglas debates and the Freeport Doctrine",
  10: "John Brown, the election of 1860, and secession",
  11: "The war begins: Sumter, Bull Run, and the rival strategies",
  12: "Stalemate and cost: the war to Antietam and the liberties suspended",
  13: "Emancipation: the Proclamation and Black soldiers",
  14: "1863: Gettysburg, Vicksburg, and the Address",
  15: "Total war and the end: Grant, Sherman, Appomattox, and the Second Inaugural"
};

window.HCG_SC_LESSONS = [
  { n: 1, title: "The Compromise of 1850 and the Fugitive Slave Act", question: "What did the Compromise of 1850 settle, and what did its Fugitive Slave Act ask the North to do?" },
  { n: 2, title: "The Antislavery Argument at Full Voice", question: "What did the antislavery writers of 1851 and 1852 ask their readers to feel, to judge, and to do?" },
  { n: 3, title: "The Kansas-Nebraska Act and Bleeding Kansas", question: "What did the Kansas-Nebraska Act repeal, and what did popular sovereignty look like when settlers tried it?" },
  { n: 4, title: "The Republican Party and Dred Scott", question: "What did the Republican Party promise, and what did the Supreme Court try to settle in Dred Scott?" },
  { n: 5, title: "The Debates, John Brown, the Election of 1860, and Secession", question: "How did the argument of 1858 become the break of 1860 and 1861?" },
  { n: 6, title: "The War Begins: Sumter to Antietam", question: "What did each side think would win the war, and what did the first seventeen months teach them?" },
  { n: 7, title: "Emancipation and the War Transformed, 1863", question: "How did emancipation change what the war was for, and for whom?" },
  { n: 8, title: "Total War and Appomattox", question: "How did the war end, and what did its ending settle?" }
];

window.HCG_SC_ITEMS = [
  // Lesson 1
  { id: "s1-reading", lesson: 1, kind: "Reading", name: "The Compromise of 1850 and the Fugitive Slave Act", days: 1, tags: [1, 2], storage: "hcg/sectional-crisis/lesson-01-reading.pdf", core: true },
  { id: "s1-notes", lesson: 1, kind: "Guided Notes", name: "Lesson 1 guided notes", days: 0, tags: [1, 2], storage: "hcg/sectional-crisis/lesson-01-guided-notes.pdf", core: true },
  { id: "s1-activity", lesson: 1, kind: "Activity", name: "The Compromise File", days: 1, tags: [1, 2], storage: "hcg/sectional-crisis/lesson-01-activity.pdf", core: true },
  { id: "s1-notebook", lesson: 1, kind: "Notebook", name: "Piece of the story chart", days: 0.5, tags: [1, 2], storage: "hcg/sectional-crisis/lesson-01-notebook.pdf" },
  { id: "s1-quick", lesson: 1, kind: "Quick Check", name: "Ten Dollars and Five", days: 0.5, tags: [1, 2], storage: "hcg/sectional-crisis/lesson-01-quick-check.pdf" },
  { id: "s1-writing", lesson: 1, kind: "Writing", name: "A Settlement, or an Armistice?", days: 1, tags: [1, 2], storage: "hcg/sectional-crisis/lesson-01-writing.pdf" },
  // Lesson 2
  { id: "s2-reading", lesson: 2, kind: "Reading", name: "The Antislavery Argument at Full Voice", days: 1, tags: [3, 4], storage: "hcg/sectional-crisis/lesson-02-reading.pdf", core: true },
  { id: "s2-notes", lesson: 2, kind: "Guided Notes", name: "Lesson 2 guided notes", days: 0, tags: [3, 4], storage: "hcg/sectional-crisis/lesson-02-guided-notes.pdf", core: true },
  { id: "s2-activity", lesson: 2, kind: "Activity", name: "The Antislavery File", days: 1, tags: [3, 4], storage: "hcg/sectional-crisis/lesson-02-activity.pdf", core: true },
  { id: "s2-notebook", lesson: 2, kind: "Notebook", name: "Form by form chart", days: 0.5, tags: [3, 4], storage: "hcg/sectional-crisis/lesson-02-notebook.pdf" },
  { id: "s2-quick", lesson: 2, kind: "Quick Check", name: "Two Texts of One Speech", days: 0.5, tags: [3, 4], storage: "hcg/sectional-crisis/lesson-02-quick-check.pdf" },
  { id: "s2-writing", lesson: 2, kind: "Writing", name: "Feeling, Judgment, Witness", days: 1, tags: [3, 4], storage: "hcg/sectional-crisis/lesson-02-writing.pdf" },
  // Lesson 3
  { id: "s3-reading", lesson: 3, kind: "Reading", name: "The Kansas-Nebraska Act and Bleeding Kansas", days: 1, tags: [5, 6], storage: "hcg/sectional-crisis/lesson-03-reading.pdf", core: true },
  { id: "s3-notes", lesson: 3, kind: "Guided Notes", name: "Lesson 3 guided notes", days: 0, tags: [5, 6], storage: "hcg/sectional-crisis/lesson-03-guided-notes.pdf", core: true },
  { id: "s3-activity", lesson: 3, kind: "Activity", name: "The Kansas File: The Kansas-Nebraska Act and Bleeding Kansas", days: 1, tags: [5, 6], storage: "hcg/sectional-crisis/lesson-03-activity.pdf", core: true },
  { id: "s3-notebook", lesson: 3, kind: "Notebook", name: "Episode by episode chart", days: 0.5, tags: [5, 6], storage: "hcg/sectional-crisis/lesson-03-notebook.pdf" },
  { id: "s3-quick", lesson: 3, kind: "Quick Check", name: "The Repeal and the Doctrine Tested", days: 0.5, tags: [5, 6], storage: "hcg/sectional-crisis/lesson-03-quick-check.pdf" },
  { id: "s3-writing", lesson: 3, kind: "Writing", name: "Failing, or Working as Designed?", days: 1, tags: [5, 6], storage: "hcg/sectional-crisis/lesson-03-writing.pdf" },
  // Lesson 4
  { id: "s4-reading", lesson: 4, kind: "Reading", name: "The Republican Party and Dred Scott", days: 1, tags: [7, 8], storage: "hcg/sectional-crisis/lesson-04-reading.pdf", core: true },
  { id: "s4-notes", lesson: 4, kind: "Guided Notes", name: "Lesson 4 guided notes", days: 0, tags: [7, 8], storage: "hcg/sectional-crisis/lesson-04-guided-notes.pdf", core: true },
  { id: "s4-activity", lesson: 4, kind: "Activity", name: "The Dred Scott File", days: 1, tags: [7, 8], storage: "hcg/sectional-crisis/lesson-04-activity.pdf", core: true },
  { id: "s4-notebook", lesson: 4, kind: "Notebook", name: "Stage by stage chart", days: 0.5, tags: [7, 8], storage: "hcg/sectional-crisis/lesson-04-notebook.pdf" },
  { id: "s4-quick", lesson: 4, kind: "Quick Check", name: "The Platform and the Dissent, 1856 to 1857", days: 0.5, tags: [7, 8], storage: "hcg/sectional-crisis/lesson-04-quick-check.pdf" },
  { id: "s4-writing", lesson: 4, kind: "Writing", name: "Misreading or Honest Logic", days: 1, tags: [7, 8], storage: "hcg/sectional-crisis/lesson-04-writing.pdf" },
  // Lesson 5
  { id: "s5-reading", lesson: 5, kind: "Reading", name: "The Debates, John Brown, the Election of 1860, and Secession", days: 1, tags: [9, 10], storage: "hcg/sectional-crisis/lesson-05-reading.pdf", core: true },
  { id: "s5-notes", lesson: 5, kind: "Guided Notes", name: "Lesson 5 guided notes", days: 0, tags: [9, 10], storage: "hcg/sectional-crisis/lesson-05-guided-notes.pdf", core: true },
  { id: "s5-activity", lesson: 5, kind: "Activity", name: "The Break File", days: 1, tags: [9, 10], storage: "hcg/sectional-crisis/lesson-05-activity.pdf", core: true },
  { id: "s5-notebook", lesson: 5, kind: "Notebook", name: "Part of the break chart", days: 0.5, tags: [9, 10], storage: "hcg/sectional-crisis/lesson-05-notebook.pdf" },
  { id: "s5-quick", lesson: 5, kind: "Quick Check", name: "Ottawa to Savannah, 1858 to 1861", days: 0.5, tags: [9, 10], storage: "hcg/sectional-crisis/lesson-05-quick-check.pdf" },
  { id: "s5-writing", lesson: 5, kind: "Writing", name: "Which Turn Closed the Road", days: 1, tags: [9, 10], storage: "hcg/sectional-crisis/lesson-05-writing.pdf" },
  // Lesson 6
  { id: "s6-reading", lesson: 6, kind: "Reading", name: "The War Begins: Sumter to Antietam", days: 1, tags: [11, 12], storage: "hcg/sectional-crisis/lesson-06-reading.pdf", core: true },
  { id: "s6-notes", lesson: 6, kind: "Guided Notes", name: "Lesson 6 guided notes", days: 0, tags: [11, 12], storage: "hcg/sectional-crisis/lesson-06-guided-notes.pdf", core: true },
  { id: "s6-activity", lesson: 6, kind: "Activity", name: "The First War File: What Did Each Side Think Would Win?", days: 1, tags: [11, 12], storage: "hcg/sectional-crisis/lesson-06-activity.pdf", core: true },
  { id: "s6-notebook", lesson: 6, kind: "Notebook", name: "Part by part chart", days: 0.5, tags: [11, 12], storage: "hcg/sectional-crisis/lesson-06-notebook.pdf" },
  { id: "s6-quick", lesson: 6, kind: "Quick Check", name: "Theories of Victory", days: 0.5, tags: [11, 12], storage: "hcg/sectional-crisis/lesson-06-quick-check.pdf" },
  { id: "s6-writing", lesson: 6, kind: "Writing", name: "What Did Each Side Think Would Win the War?", days: 1, tags: [11, 12], storage: "hcg/sectional-crisis/lesson-06-writing.pdf" },
  // Lesson 7
  { id: "s7-reading", lesson: 7, kind: "Reading", name: "Emancipation and the War Transformed, 1863", days: 1, tags: [13, 14], storage: "hcg/sectional-crisis/lesson-07-reading.pdf", core: true },
  { id: "s7-notes", lesson: 7, kind: "Guided Notes", name: "Lesson 7 guided notes", days: 0, tags: [13, 14], storage: "hcg/sectional-crisis/lesson-07-guided-notes.pdf", core: true },
  { id: "s7-activity", lesson: 7, kind: "Activity", name: "The Emancipation File", days: 1, tags: [13, 14], storage: "hcg/sectional-crisis/lesson-07-activity.pdf", core: true },
  { id: "s7-notebook", lesson: 7, kind: "Notebook", name: "Record by record chart", days: 0.5, tags: [13, 14], storage: "hcg/sectional-crisis/lesson-07-notebook.pdf" },
  { id: "s7-quick", lesson: 7, kind: "Quick Check", name: "Freedom Declared, Freedom Fought For", days: 0.5, tags: [13, 14], storage: "hcg/sectional-crisis/lesson-07-quick-check.pdf" },
  { id: "s7-writing", lesson: 7, kind: "Writing", name: "Purpose or Instrument?", days: 1, tags: [13, 14], storage: "hcg/sectional-crisis/lesson-07-writing.pdf" },
  // Lesson 8
  { id: "s8-reading", lesson: 8, kind: "Reading", name: "Total War and Appomattox", days: 1, tags: [15], storage: "hcg/sectional-crisis/lesson-08-reading.pdf", core: true },
  { id: "s8-notes", lesson: 8, kind: "Guided Notes", name: "Lesson 8 guided notes", days: 0, tags: [15], storage: "hcg/sectional-crisis/lesson-08-guided-notes.pdf", core: true },
  { id: "s8-activity", lesson: 8, kind: "Activity", name: "The Ending File", days: 1, tags: [15], storage: "hcg/sectional-crisis/lesson-08-activity.pdf", core: true },
  { id: "s8-notebook", lesson: 8, kind: "Notebook", name: "Piece by piece chart", days: 0.5, tags: [15], storage: "hcg/sectional-crisis/lesson-08-notebook.pdf" },
  { id: "s8-quick", lesson: 8, kind: "Quick Check", name: "The Woe Due", days: 0.5, tags: [15], storage: "hcg/sectional-crisis/lesson-08-quick-check.pdf" },
  { id: "s8-writing", lesson: 8, kind: "Writing", name: "The Verdict of the Second Inaugural", days: 1, tags: [15], storage: "hcg/sectional-crisis/lesson-08-writing.pdf" },
  // Review day
  { id: "srev-guide", lesson: 9, kind: "Review", name: "Study guide (review day)", days: 1, tags: [], storage: "hcg/sectional-crisis/review-study-guide.pdf", core: true },
  { id: "srev-cross", lesson: 9, kind: "Review", name: "Crossword (56 answers)", days: 0.5, tags: [], storage: "hcg/sectional-crisis/review-crossword.pdf" }
];

window.HCG_SC_TOPICS = {
  1: { label: "The last settlement: compromise, the fugitive law, and the antislavery answer", note: "" },
  2: { label: "Kansas and the broken parties: Nebraska, the Republicans, and the Court", note: "" },
  3: { label: "The break: argument, raid, election, and secession", note: "" },
  4: { label: "The war for the Union: strategy, stalemate, and cost to 1862", note: "" },
  5: { label: "The war remade: emancipation, 1863, and the Address", note: "" },
  6: { label: "The verdict of arms: total war, Appomattox, and the Second Inaugural", note: "" }
};

window.HCG_SC_BP_TOPIC = {
  1: [1], 2: [1], 3: [1], 4: [1], 5: [2], 6: [2], 7: [2], 8: [2], 9: [3], 10: [3], 11: [4], 12: [4], 13: [5], 14: [5], 15: [6]
};

// TPSP picker index for Sectional Crisis and Civil War: the
// unit's premium DBQ lead and its secondary first, both verified
// in Firestore (collection psp_premium) for this pass: dbq3, "Was
// Slavery the Central Cause of the Civil War?" (catalog code
// DBQ178, era "Sectional Crisis and Civil War"), whose seven
// documents all sit in the sectional era file and are all taught
// in the unit, leading, and dbq14, "What Strategies Did Reformers
// Use to Force Change?" (catalog code DBQ189, era "Jacksonian
// America and Reform"), three of whose seven documents stand on
// this unit's ground and are taught in Lessons 2 and 4, named
// alongside it as the Jackson integration established; then the
// era sources from the TPSP library file sectional-civil-war.json
// in file order, then the five records the Jackson build left
// untagged for this unit from jackson-reform.json (Truth in Gage's
// version, Douglass's Fourth of July oration, the House Divided
// speech, Douglass's letter to Hugh Auld, and the second Dred
// Scott record), each with conservative blueprint pre-tags where
// the source names the entry's content. Twenty-five of the 28
// sources are pre-tagged; three are deliberately left untagged:
// Robinson's Pictures of Slavery (the institution's defense of
// itself, which names no single entry's content) and the
// Homestead and Morrill Acts (the wartime Congress's work, taught
// inside Lesson 8's frame but naming none of entry 15's terms).
window.HCG_TPSP_SC = [
{
 "id": "dbq3",
 "title": "Was Slavery the Central Cause of the Civil War?",
 "type": "Premium DBQ",
 "meta": "The Primary Source Project · premium document-based question",
 "url": "https://tpsp.web.app/library?tab=premium",
 "dbq": true
},
{
 "id": "dbq14",
 "title": "What Strategies Did Reformers Use to Force Change?",
 "type": "Premium DBQ",
 "meta": "The Primary Source Project · premium document-based question",
 "url": "https://tpsp.web.app/library?tab=premium",
 "dbq": true
},
{
 "id": "effects-of-fugitive-slave-law-1850",
 "title": "\"Effects of the Fugitive-Slave-Law\"",
 "type": "Print",
 "meta": "Theodor Kaufmann · 1850",
 "url": "https://tpsp.web.app/library?q=%22Effects%20of%20the%20Fugitive-Slave-Law%22",
 "bp": [
  2
 ]
},
{
 "id": "kansas-nebraska-act-1854",
 "title": "Kansas-Nebraska Act",
 "type": "Government document",
 "meta": "U.S. Congress · 1854",
 "url": "https://tpsp.web.app/library?q=Kansas-Nebraska%20Act",
 "bp": [
  5
 ]
},
{
 "id": "forcing-slavery-cartoon-1856",
 "title": "\"Forcing Slavery Down the Throat of a Freesoiler\"",
 "type": "Political cartoon",
 "meta": "John L. Magee · 1856",
 "url": "https://tpsp.web.app/library?q=%22Forcing%20Slavery%20Down%20the%20Throat%20of%20a%20Freesoiler%22",
 "bp": [
  6
 ]
},
{
 "id": "dred-scott-decision-1857",
 "title": "Dred Scott v. Sandford Majority Opinion",
 "type": "Court decision",
 "meta": "Chief Justice Roger B. Taney · 1857",
 "url": "https://tpsp.web.app/library?q=Dred%20Scott%20v.%20Sandford%20Majority%20Opinion",
 "bp": [
  8
 ]
},
{
 "id": "douglas-ottawa-debate-1858",
 "title": "Speech at the Ottawa Debate",
 "type": "Speech",
 "meta": "Stephen A. Douglas · 1858",
 "url": "https://tpsp.web.app/library?q=Speech%20at%20the%20Ottawa%20Debate",
 "bp": [
  9
 ]
},
{
 "id": "lincoln-ottawa-debate-reply-1858",
 "title": "Reply at the Ottawa Debate",
 "type": "Speech",
 "meta": "Abraham Lincoln · 1858",
 "url": "https://tpsp.web.app/library?q=Reply%20at%20the%20Ottawa%20Debate",
 "bp": [
  9
 ]
},
{
 "id": "slave-population-map-1861",
 "title": "Map Showing the Distribution of the Slave Population of the Southern States",
 "type": "Map",
 "meta": "U.S. Coast Survey · 1861",
 "url": "https://tpsp.web.app/library?q=Map%20Showing%20the%20Distribution%20of%20the%20Slave%20Population%20of%20the%20Southern%20States",
 "bp": [
  11
 ]
},
{
 "id": "antietam-dead-1862",
 "title": "Dead of Antietam",
 "type": "Photograph",
 "meta": "Alexander Gardner · 1862",
 "url": "https://tpsp.web.app/library?q=Dead%20of%20Antietam",
 "bp": [
  12
 ]
},
{
 "id": "habeas-corpus-proclamation-1862",
 "title": "A Proclamation on the Suspension of Habeas Corpus, 1862",
 "type": "Government document",
 "meta": "Abraham Lincoln · 1862",
 "url": "https://tpsp.web.app/library?q=A%20Proclamation%20on%20the%20Suspension%20of%20Habeas%20Corpus%2C%201862",
 "bp": [
  12
 ]
},
{
 "id": "gettysburg-address-1863",
 "title": "Gettysburg Address (full text)",
 "type": "Speech",
 "meta": "Abraham Lincoln · 1863",
 "url": "https://tpsp.web.app/library?q=Gettysburg%20Address%20%28full%20text%29",
 "bp": [
  14
 ]
},
{
 "id": "emancipation-proclamation-1863",
 "title": "Emancipation Proclamation (excerpt)",
 "type": "Government document",
 "meta": "Abraham Lincoln · 1863",
 "url": "https://tpsp.web.app/library?q=Emancipation%20Proclamation%20%28excerpt%29",
 "bp": [
  13
 ]
},
{
 "id": "robinson-pictures-of-slavery-1863",
 "title": "Pictures of Slavery and Anti-Slavery",
 "type": "Book",
 "meta": "John Bell Robinson · 1863",
 "url": "https://tpsp.web.app/library?q=Pictures%20of%20Slavery%20and%20Anti-Slavery"
},
{
 "id": "wlnl-address-1864",
 "title": "\"To the Women of the Republic,\" Address from the Women's Loyal National League",
 "type": "Petition",
 "meta": "Women's Loyal National League · 1864",
 "url": "https://tpsp.web.app/library?q=%22To%20the%20Women%20of%20the%20Republic%2C%22%20Address%20from%20the%20Women%27s%20Loyal%20National%20League",
 "bp": [
  15
 ]
},
{
 "id": "annie-davis-letter-1864",
 "title": "Letter from Annie Davis to Abraham Lincoln",
 "type": "Letter",
 "meta": "Annie Davis · 1864",
 "url": "https://tpsp.web.app/library?q=Letter%20from%20Annie%20Davis%20to%20Abraham%20Lincoln",
 "bp": [
  15
 ]
},
{
 "id": "lincoln-second-inaugural-1865",
 "title": "Second Inaugural Address (full text)",
 "type": "Speech",
 "meta": "Abraham Lincoln · 1865",
 "url": "https://tpsp.web.app/library?q=Second%20Inaugural%20Address%20%28full%20text%29",
 "bp": [
  15
 ]
},
{
 "id": "stephens-cornerstone-speech-1861",
 "title": "Cornerstone Speech (excerpt)",
 "type": "Speech",
 "meta": "Alexander H. Stephens · 1861",
 "url": "https://tpsp.web.app/library?q=Cornerstone%20Speech%20%28excerpt%29",
 "bp": [
  10
 ]
},
{
 "id": "south-carolina-secession-declaration-1860",
 "title": "Declaration of the Immediate Causes of Secession (excerpt)",
 "type": "Government document",
 "meta": "South Carolina Secession Convention · 1860",
 "url": "https://tpsp.web.app/library?q=Declaration%20of%20the%20Immediate%20Causes%20of%20Secession%20%28excerpt%29",
 "bp": [
  10
 ]
},
{
 "id": "douglass-men-of-color-to-arms-1863",
 "title": "\"Men of Color, To Arms! To Arms!\" (recruiting broadside)",
 "type": "Poster",
 "meta": "Frederick Douglass and other African American leaders · 1863",
 "url": "https://tpsp.web.app/library?q=%22Men%20of%20Color%2C%20To%20Arms%21%20To%20Arms%21%22%20%28recruiting%20broadside%29",
 "bp": [
  13
 ]
},
{
 "id": "truth-akron-address-1851",
 "title": "Address at the Akron Women's Rights Convention (1851)",
 "type": "Speech",
 "meta": "Sojourner Truth · 1851",
 "url": "https://tpsp.web.app/library?q=Address%20at%20the%20Akron%20Women%27s%20Rights%20Convention%20%281851%29",
 "bp": [
  4
 ]
},
{
 "id": "homestead-act-1862",
 "title": "Homestead Act (Section 1)",
 "type": "Government document",
 "meta": "U.S. Congress · 1862",
 "url": "https://tpsp.web.app/library?q=Homestead%20Act%20%28Section%201%29"
},
{
 "id": "morrill-land-grant-act-1862",
 "title": "Morrill Land-Grant Act (excerpt)",
 "type": "Government document",
 "meta": "U.S. Congress · 1862",
 "url": "https://tpsp.web.app/library?q=Morrill%20Land-Grant%20Act%20%28excerpt%29"
},
{
 "id": "ballou-letter-to-sarah-1861",
 "title": "Letter to Sarah Ballou (full text)",
 "type": "Letter",
 "meta": "Sullivan Ballou · 1861",
 "url": "https://tpsp.web.app/library?q=Letter%20to%20Sarah%20Ballou%20%28full%20text%29",
 "bp": [
  11
 ]
},
{
 "id": "jacobs-incidents-slave-girl-1861",
 "title": "\"Incidents in the Life of a Slave Girl\" (excerpt)",
 "type": "Book",
 "meta": "Harriet Jacobs · 1861",
 "url": "https://tpsp.web.app/library?q=%22Incidents%20in%20the%20Life%20of%20a%20Slave%20Girl%22%20%28excerpt%29",
 "bp": [
  3
 ]
},
{
 "id": "sojourner-truth-aint-i-a-woman-1851",
 "title": "\"Ain't I a Woman?\" (excerpt)",
 "type": "Speech",
 "meta": "Sojourner Truth · 1851",
 "url": "https://tpsp.web.app/library?q=%22Ain%27t%20I%20a%20Woman%3F%22%20%28excerpt%29",
 "bp": [
  4
 ]
},
{
 "id": "douglass-fourth-of-july-1852",
 "title": "\"What to the Slave Is the Fourth of July?\" (excerpt)",
 "type": "Speech",
 "meta": "Frederick Douglass · 1852",
 "url": "https://tpsp.web.app/library?q=%22What%20to%20the%20Slave%20Is%20the%20Fourth%20of%20July%3F%22%20%28excerpt%29",
 "bp": [
  4
 ]
},
{
 "id": "house-divided-speech-1858",
 "title": "The \"House Divided\" Speech",
 "type": "Speech",
 "meta": "Abraham Lincoln · 1857-1858",
 "url": "https://tpsp.web.app/library?q=The%20%22House%20Divided%22%20Speech",
 "bp": [
  8
 ]
},
{
 "id": "douglass-to-hugh-auld-1857",
 "title": "\"I Love You But Hate Slavery\": Frederick Douglass to His Former Master, Hugh Auld",
 "type": "Letter",
 "meta": "Frederick Douglass · 1857",
 "url": "https://tpsp.web.app/library?q=%22I%20Love%20You%20But%20Hate%20Slavery%22%3A%20Frederick%20Douglass%20to%20His%20Former%20Master%2C%20Hugh%20Auld",
 "bp": [
  8
 ]
},
{
 "id": "dred-scott-v-sandford-1857",
 "title": "Dred Scott v. Sandford",
 "type": "Court decision",
 "meta": "U.S. Supreme Court (Chief Justice Roger B. Taney) · 1857",
 "url": "https://tpsp.web.app/library?q=Dred%20Scott%20v.%20Sandford",
 "bp": [
  8
 ]
}
];

window.HCG_RC_BLUEPRINT = {
  1: "Presidential Reconstruction: Johnson's restoration plan and its terms",
  2: "The Black Codes and the Freedmen's Bureau: freedom contested on the ground",
  3: "The Thirteenth Amendment: ratification and the enforcement clause",
  4: "The Civil Rights Act of 1866 and the veto fight",
  5: "The Fourteenth Amendment: citizenship written into the Constitution",
  6: "Military Reconstruction: the Reconstruction Acts and the impeachment crisis",
  7: "The Fifteenth Amendment and the vote",
  8: "Black officeholding and the Reconstruction governments",
  9: "Land and labor: the land that never came, sharecropping, and the crop lien",
  10: "Schools and churches: freedom's institutions built by freedpeople",
  11: "The Ku Klux Klan and organized terror",
  12: "The Enforcement Acts and the federal answer",
  13: "The courts narrow the amendments: Slaughter-House and the judicial retreat",
  14: "The northern retreat: amnesty, panic, the White League, and the Civil Rights Act of 1875",
  15: "1876 and the Compromise of 1877: the end of Reconstruction"
};

window.HCG_RC_LESSONS = [
  { n: 1, title: "After Appomattox: Presidential Reconstruction", question: "What did Johnson's restoration give back to the South, and what did it leave freedpeople to fight for?" },
  { n: 2, title: "The Thirteenth Amendment and the Meaning of Freedom", question: "What did the Thirteenth Amendment settle, and why did Congress decide a statute was not enough?" },
  { n: 3, title: "Congress Takes Charge: The Fourteenth Amendment and the Reconstruction Acts", question: "How did Congress rewrite the Constitution and the South's governments between 1866 and 1868, and at what cost?" },
  { n: 4, title: "The New Political Order: The Vote and Black Officeholding", question: "Who governed the reconstructed South, and what did the Fifteenth Amendment settle and leave open?" },
  { n: 5, title: "Freedom on the Ground: Land, Labor, Schools, and Churches", question: "What did freedpeople build, and what did the land settlement they never got cost what they built?" },
  { n: 6, title: "The Counterrevolution: The Klan and the Enforcement Acts", question: "What did the Klan's terror aim at, and what did it take to break the first Klan?" },
  { n: 7, title: "The Retreat: Courts, Panic, and the Leagues", question: "By what steps, legal, economic, and violent, did the country retreat from the settlement between 1872 and 1876?" },
  { n: 8, title: "1876 and the End: What Was Settled, What Was Left Open", question: "What did Reconstruction settle, and what did its ending leave open?" }
];

window.HCG_RC_ITEMS = [
  // Lesson 1
  { id: "n1-reading", lesson: 1, kind: "Reading", name: "After Appomattox: Presidential Reconstruction", days: 1, tags: [1, 2], storage: "hcg/reconstruction/lesson-01-reading.pdf", core: true },
  { id: "n1-notes", lesson: 1, kind: "Guided Notes", name: "Lesson 1 guided notes", days: 0, tags: [1, 2], storage: "hcg/reconstruction/lesson-01-guided-notes.pdf", core: true },
  { id: "n1-activity", lesson: 1, kind: "Activity", name: "The Settlement on Paper", days: 1, tags: [1, 2], storage: "hcg/reconstruction/lesson-01-activity.pdf", core: true },
  { id: "n1-notebook", lesson: 1, kind: "Notebook", name: "Piece of the story chart", days: 0.5, tags: [1, 2], storage: "hcg/reconstruction/lesson-01-notebook.pdf" },
  { id: "n1-quick", lesson: 1, kind: "Quick Check", name: "Fifty Dollars", days: 0.5, tags: [1, 2], storage: "hcg/reconstruction/lesson-01-quick-check.pdf" },
  { id: "n1-writing", lesson: 1, kind: "Writing", name: "Given Back, and Left to Fight For", days: 1, tags: [1, 2], storage: "hcg/reconstruction/lesson-01-writing.pdf" },
  // Lesson 2
  { id: "n2-reading", lesson: 2, kind: "Reading", name: "The Thirteenth Amendment and the Meaning of Freedom", days: 1, tags: [3, 4], storage: "hcg/reconstruction/lesson-02-reading.pdf", core: true },
  { id: "n2-notes", lesson: 2, kind: "Guided Notes", name: "Lesson 2 guided notes", days: 0, tags: [3, 4], storage: "hcg/reconstruction/lesson-02-guided-notes.pdf", core: true },
  { id: "n2-activity", lesson: 2, kind: "Activity", name: "Freedom's Terms, Drafted Twice", days: 1, tags: [3, 4], storage: "hcg/reconstruction/lesson-02-activity.pdf", core: true },
  { id: "n2-notebook", lesson: 2, kind: "Notebook", name: "Definer by definer chart", days: 0.5, tags: [3, 4], storage: "hcg/reconstruction/lesson-02-notebook.pdf" },
  { id: "n2-quick", lesson: 2, kind: "Quick Check", name: "Citizenship and Its Rights", days: 0.5, tags: [3, 4], storage: "hcg/reconstruction/lesson-02-quick-check.pdf" },
  { id: "n2-writing", lesson: 2, kind: "Writing", name: "In Law or In Life?", days: 1, tags: [3, 4], storage: "hcg/reconstruction/lesson-02-writing.pdf" },
  // Lesson 3
  { id: "n3-reading", lesson: 3, kind: "Reading", name: "Congress Takes Charge: The Fourteenth Amendment and the Reconstruction Acts", days: 1, tags: [5, 6], storage: "hcg/reconstruction/lesson-03-reading.pdf", core: true },
  { id: "n3-notes", lesson: 3, kind: "Guided Notes", name: "Lesson 3 guided notes", days: 0, tags: [5, 6], storage: "hcg/reconstruction/lesson-03-guided-notes.pdf", core: true },
  { id: "n3-activity", lesson: 3, kind: "Activity", name: "The Amendment and the Machinery: The Fourteenth Amendment and the Reconstruction Acts", days: 1, tags: [5, 6], storage: "hcg/reconstruction/lesson-03-activity.pdf", core: true },
  { id: "n3-notebook", lesson: 3, kind: "Notebook", name: "Step by step chart", days: 0.5, tags: [5, 6], storage: "hcg/reconstruction/lesson-03-notebook.pdf" },
  { id: "n3-quick", lesson: 3, kind: "Quick Check", name: "Citizenship Written, Governments Rebuilt", days: 0.5, tags: [5, 6], storage: "hcg/reconstruction/lesson-03-quick-check.pdf" },
  { id: "n3-writing", lesson: 3, kind: "Writing", name: "Conqueror, Constitution Maker, or Both?", days: 1, tags: [5, 6], storage: "hcg/reconstruction/lesson-03-writing.pdf" },
  // Lesson 4
  { id: "n4-reading", lesson: 4, kind: "Reading", name: "The New Political Order: The Vote and Black Officeholding", days: 1, tags: [7, 8], storage: "hcg/reconstruction/lesson-04-reading.pdf", core: true },
  { id: "n4-notes", lesson: 4, kind: "Guided Notes", name: "Lesson 4 guided notes", days: 0, tags: [7, 8], storage: "hcg/reconstruction/lesson-04-guided-notes.pdf", core: true },
  { id: "n4-activity", lesson: 4, kind: "Activity", name: "The New Electorate Speaks and Is Pictured", days: 1, tags: [7, 8], storage: "hcg/reconstruction/lesson-04-activity.pdf", core: true },
  { id: "n4-notebook", lesson: 4, kind: "Notebook", name: "Stage by stage chart", days: 0.5, tags: [7, 8], storage: "hcg/reconstruction/lesson-04-notebook.pdf" },
  { id: "n4-quick", lesson: 4, kind: "Quick Check", name: "The Amendment and the Senator, 1870 to 1871", days: 0.5, tags: [7, 8], storage: "hcg/reconstruction/lesson-04-quick-check.pdf" },
  { id: "n4-writing", lesson: 4, kind: "Writing", name: "Settled in Text, Resting on Protection", days: 1, tags: [7, 8], storage: "hcg/reconstruction/lesson-04-writing.pdf" },
  // Lesson 5
  { id: "n5-reading", lesson: 5, kind: "Reading", name: "Freedom on the Ground: Land, Labor, Schools, and Churches", days: 1, tags: [9, 10], storage: "hcg/reconstruction/lesson-05-reading.pdf", core: true },
  { id: "n5-notes", lesson: 5, kind: "Guided Notes", name: "Lesson 5 guided notes", days: 0, tags: [9, 10], storage: "hcg/reconstruction/lesson-05-guided-notes.pdf", core: true },
  { id: "n5-activity", lesson: 5, kind: "Activity", name: "Freedom's Ledger", days: 1, tags: [9, 10], storage: "hcg/reconstruction/lesson-05-activity.pdf", core: true },
  { id: "n5-notebook", lesson: 5, kind: "Notebook", name: "Stage by stage chart", days: 0.5, tags: [9, 10], storage: "hcg/reconstruction/lesson-05-notebook.pdf" },
  { id: "n5-quick", lesson: 5, kind: "Quick Check", name: "The Petition and the Settlement", days: 0.5, tags: [9, 10], storage: "hcg/reconstruction/lesson-05-quick-check.pdf" },
  { id: "n5-writing", lesson: 5, kind: "Writing", name: "Built Without Land", days: 1, tags: [9, 10], storage: "hcg/reconstruction/lesson-05-writing.pdf" },
  // Lesson 6
  { id: "n6-reading", lesson: 6, kind: "Reading", name: "The Counterrevolution: The Klan and the Enforcement Acts", days: 1, tags: [11, 12], storage: "hcg/reconstruction/lesson-06-reading.pdf", core: true },
  { id: "n6-notes", lesson: 6, kind: "Guided Notes", name: "Lesson 6 guided notes", days: 0, tags: [11, 12], storage: "hcg/reconstruction/lesson-06-guided-notes.pdf", core: true },
  { id: "n6-activity", lesson: 6, kind: "Activity", name: "Testimony and Answer", days: 1, tags: [11, 12], storage: "hcg/reconstruction/lesson-06-activity.pdf", core: true },
  { id: "n6-notebook", lesson: 6, kind: "Notebook", name: "Stage by stage chart", days: 0.5, tags: [11, 12], storage: "hcg/reconstruction/lesson-06-notebook.pdf" },
  { id: "n6-quick", lesson: 6, kind: "Quick Check", name: "Testimony and Statute, 1871 to 1872", days: 0.5, tags: [11, 12], storage: "hcg/reconstruction/lesson-06-quick-check.pdf" },
  { id: "n6-writing", lesson: 6, kind: "Writing", name: "Civil Rights Law, Counterinsurgency, or Both", days: 1, tags: [11, 12], storage: "hcg/reconstruction/lesson-06-writing.pdf" },
  // Lesson 7
  { id: "n7-reading", lesson: 7, kind: "Reading", name: "The Retreat: Courts, Panic, and the Leagues", days: 1, tags: [13, 14], storage: "hcg/reconstruction/lesson-07-reading.pdf", core: true },
  { id: "n7-notes", lesson: 7, kind: "Guided Notes", name: "Lesson 7 guided notes", days: 0, tags: [13, 14], storage: "hcg/reconstruction/lesson-07-guided-notes.pdf", core: true },
  { id: "n7-activity", lesson: 7, kind: "Activity", name: "The Retreat in Five Records", days: 1, tags: [13, 14], storage: "hcg/reconstruction/lesson-07-activity.pdf", core: true },
  { id: "n7-notebook", lesson: 7, kind: "Notebook", name: "Piece of the story chart", days: 0.5, tags: [13, 14], storage: "hcg/reconstruction/lesson-07-notebook.pdf" },
  { id: "n7-quick", lesson: 7, kind: "Quick Check", name: "Two Citizenships", days: 0.5, tags: [13, 14], storage: "hcg/reconstruction/lesson-07-quick-check.pdf" },
  { id: "n7-writing", lesson: 7, kind: "Writing", name: "Ranking the Retreat", days: 1, tags: [13, 14], storage: "hcg/reconstruction/lesson-07-writing.pdf" },
  // Lesson 8
  { id: "n8-reading", lesson: 8, kind: "Reading", name: "1876 and the End", days: 1, tags: [15], storage: "hcg/reconstruction/lesson-08-reading.pdf", core: true },
  { id: "n8-notes", lesson: 8, kind: "Guided Notes", name: "Lesson 8 guided notes", days: 0, tags: [15], storage: "hcg/reconstruction/lesson-08-guided-notes.pdf", core: true },
  { id: "n8-activity", lesson: 8, kind: "Activity", name: "The Settlement Audited", days: 1, tags: [15], storage: "hcg/reconstruction/lesson-08-activity.pdf", core: true },
  { id: "n8-notebook", lesson: 8, kind: "Notebook", name: "Piece by piece chart", days: 0.5, tags: [15], storage: "hcg/reconstruction/lesson-08-notebook.pdf" },
  { id: "n8-quick", lesson: 8, kind: "Quick Check", name: "Settled in Text", days: 0.5, tags: [15], storage: "hcg/reconstruction/lesson-08-quick-check.pdf" },
  { id: "n8-writing", lesson: 8, kind: "Writing", name: "Ended, or Only Stood Down", days: 1, tags: [15], storage: "hcg/reconstruction/lesson-08-writing.pdf" },
  // Review day
  { id: "nrev-guide", lesson: 9, kind: "Review", name: "Study guide (review day)", days: 1, tags: [], storage: "hcg/reconstruction/review-study-guide.pdf", core: true },
  { id: "nrev-cross", lesson: 9, kind: "Review", name: "Crossword (56 answers)", days: 0.5, tags: [], storage: "hcg/reconstruction/review-crossword.pdf" }
];

window.HCG_RC_TOPICS = {
  1: { label: "The postwar settlement: presidential Reconstruction, the Bureau, and the Black Codes", note: "" },
  2: { label: "Freedom in law: the Thirteenth Amendment and the Civil Rights Act", note: "" },
  3: { label: "Citizenship remade: the Fourteenth Amendment and congressional Reconstruction", note: "" },
  4: { label: "The vote and the new politics: the Fifteenth Amendment and Black officeholding", note: "" },
  5: { label: "Freedom on the ground: land, labor, schools, and churches", note: "" },
  6: { label: "The counterrevolution and the end: violence, retreat, and 1877", note: "" }
};

window.HCG_RC_BP_TOPIC = {
  1: [1], 2: [1], 3: [2], 4: [2], 5: [3], 6: [3], 7: [4], 8: [4], 9: [5], 10: [5], 11: [6], 12: [6], 13: [6], 14: [6], 15: [6]
};

// TPSP picker index for Reconstruction: the unit's twin
// premium DBQ leads first, both verified in Firestore (collection
// psp_premium) during the content build: dbq4, "Did Reconstruction
// Give Freed People Real Freedom?" (catalog code DBQ179, era
// "Reconstruction"), whose seven documents all sit in the
// reconstruction era file and whose first six are taught in this
// unit, and dbq15, "What Forces Brought Reconstruction to an End?"
// (catalog code DBQ190, era "Reconstruction"), whose seven
// documents all sit in the same era file and are all taught in
// this unit; then the 22 era sources from the TPSP library file
// reconstruction.json in file order, each with conservative
// blueprint pre-tags where the source names the entry's content.
// Twenty of the 22 sources are pre-tagged; two are deliberately
// left untagged: Nast's "Emancipation" (taught by description in
// Lesson 4, its scenes of enslavement carried in text only under
// the unit's image discipline, naming no single entry's content)
// and Nast's "Colored Rule" (taught by description in Lesson 7's
// reading as evidence of the image war, naming no single entry's
// content). The seventh document of DBQ 4, the 1879 sharecropping
// contract, postdates the unit's 1877 close: its picker entry
// carries that flag on its face, it is pre-tagged to the
// sharecropping entry it names, and the contract itself is not
// printed anywhere in the unit, which teaches its standard terms
// as a labeled summary.
window.HCG_TPSP_RC = [
 {
  "id": "dbq4",
  "title": "Did Reconstruction Give Freed People Real Freedom?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true
 },
 {
  "id": "dbq15",
  "title": "What Forces Brought Reconstruction to an End?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true
 },
 {
  "id": "thirteenth-amendment-1865",
  "title": "Thirteenth Amendment (full text)",
  "type": "Government document",
  "meta": "United States Congress · 1865",
  "url": "https://tpsp.web.app/library?q=Thirteenth%20Amendment%20%28full%20text%29",
  "bp": [
   3
  ]
 },
 {
  "id": "mississippi-black-code-1865",
  "title": "Mississippi Vagrant Law (excerpt)",
  "type": "Government document",
  "meta": "Mississippi Legislature · 1865",
  "url": "https://tpsp.web.app/library?q=Mississippi%20Vagrant%20Law%20%28excerpt%29",
  "bp": [
   2
  ]
 },
 {
  "id": "general-orders-no-3-1865",
  "title": "General Orders No. 3 (Juneteenth order)",
  "type": "Government document",
  "meta": "Gordon Granger · 1865",
  "url": "https://tpsp.web.app/library?q=General%20Orders%20No.%203%20%28Juneteenth%20order%29",
  "bp": [
   2
  ]
 },
 {
  "id": "nast-emancipation-1865",
  "title": "Emancipation (1865)",
  "type": "Political cartoon",
  "meta": "Thomas Nast · 1865",
  "url": "https://tpsp.web.app/library?q=Emancipation%20%281865%29"
 },
 {
  "id": "iowa-ratification-thirteenth-amendment-1866",
  "title": "Iowa's Ratification of the Thirteenth Amendment (excerpt)",
  "type": "Government document",
  "meta": "Iowa General Assembly · 1866",
  "url": "https://tpsp.web.app/library?q=Iowa%27s%20Ratification%20of%20the%20Thirteenth%20Amendment%20%28excerpt%29",
  "bp": [
   3
  ]
 },
 {
  "id": "first-vote-waud-1867",
  "title": "The First Vote",
  "type": "Illustration",
  "meta": "Alfred R. Waud · 1867",
  "url": "https://tpsp.web.app/library?q=The%20First%20Vote",
  "bp": [
   7
  ]
 },
 {
  "id": "fourteenth-amendment-section-1-1868",
  "title": "Fourteenth Amendment, Section 1 (excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress · 1868",
  "url": "https://tpsp.web.app/library?q=Fourteenth%20Amendment%2C%20Section%201%20%28excerpt%29",
  "bp": [
   5
  ]
 },
 {
  "id": "fifteenth-amendment-joint-resolution-1869",
  "title": "Joint Resolution Proposing the Fifteenth Amendment (excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress · 1869",
  "url": "https://tpsp.web.app/library?q=Joint%20Resolution%20Proposing%20the%20Fifteenth%20Amendment%20%28excerpt%29",
  "bp": [
   7
  ]
 },
 {
  "id": "abram-colby-kkk-testimony-1872",
  "title": "\"Klansmen Broke My Door Open\" (Abram Colby's testimony to Congress)",
  "type": "Government document",
  "meta": "Abram Colby · 1872",
  "url": "https://tpsp.web.app/library?q=%22Klansmen%20Broke%20My%20Door%20Open%22%20%28Abram%20Colby%27s%20testimony%20to%20Congress%29",
  "bp": [
   11
  ]
 },
 {
  "id": "louisiana-white-league-platform-1874",
  "title": "Louisiana White League Platform (excerpt)",
  "type": "Pamphlet",
  "meta": "Louisiana White League · 1874",
  "url": "https://tpsp.web.app/library?q=Louisiana%20White%20League%20Platform%20%28excerpt%29",
  "bp": [
   14
  ]
 },
 {
  "id": "charles-hays-civil-rights-speech-1874",
  "title": "Speech Reaffirming the Rights of African Americans (excerpt)",
  "type": "Speech",
  "meta": "Rep. Charles Hays · 1874",
  "url": "https://tpsp.web.app/library?q=Speech%20Reaffirming%20the%20Rights%20of%20African%20Americans%20%28excerpt%29",
  "bp": [
   14
  ]
 },
 {
  "id": "nast-colored-rule-1874",
  "title": "Colored Rule in a Reconstructed (?) State (1874)",
  "type": "Political cartoon",
  "meta": "Thomas Nast · 1874",
  "url": "https://tpsp.web.app/library?q=Colored%20Rule%20in%20a%20Reconstructed%20%28%3F%29%20State%20%281874%29"
 },
 {
  "id": "nast-worse-than-slavery-1874",
  "title": "Worse Than Slavery (c. 1874)",
  "type": "Political cartoon",
  "meta": "Thomas Nast · 1874",
  "url": "https://tpsp.web.app/library?q=Worse%20Than%20Slavery%20%28c.%201874%29",
  "bp": [
   14
  ]
 },
 {
  "id": "civil-rights-act-1875-sections-1-2",
  "title": "Civil Rights Act of 1875, Sections 1-2 (excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress · 1875",
  "url": "https://tpsp.web.app/library?q=Civil%20Rights%20Act%20of%201875%2C%20Sections%201-2%20%28excerpt%29",
  "bp": [
   14
  ]
 },
 {
  "id": "frost-democratic-ticket-1876",
  "title": "Of Course He Wants to Vote the Democratic Ticket (1876)",
  "type": "Political cartoon",
  "meta": "A. B. Frost · 1876",
  "url": "https://tpsp.web.app/library?q=Of%20Course%20He%20Wants%20to%20Vote%20the%20Democratic%20Ticket%20%281876%29",
  "bp": [
   15
  ]
 },
 {
  "id": "civil-rights-act-1866",
  "title": "Civil Rights Act of 1866 (Section 1)",
  "type": "Government document",
  "meta": "U.S. Congress · 1866",
  "url": "https://tpsp.web.app/library?q=Civil%20Rights%20Act%20of%201866%20%28Section%201%29",
  "bp": [
   4
  ]
 },
 {
  "id": "enforcement-act-1871",
  "title": "Enforcement Act of 1871 (\"Ku Klux Klan Act,\" excerpt)",
  "type": "Government document",
  "meta": "U.S. Congress · 1871",
  "url": "https://tpsp.web.app/library?q=Enforcement%20Act%20of%201871%20%28%22Ku%20Klux%20Klan%20Act%2C%22%20excerpt%29",
  "bp": [
   12
  ]
 },
 {
  "id": "jourdon-anderson-letter-1865",
  "title": "Letter to Colonel P. H. Anderson (full text)",
  "type": "Letter",
  "meta": "Jourdon Anderson · 1865",
  "url": "https://tpsp.web.app/library?q=Letter%20to%20Colonel%20P.%20H.%20Anderson%20%28full%20text%29",
  "bp": [
   2
  ]
 },
 {
  "id": "slaughter-house-cases-1873",
  "title": "Slaughter-House Cases (syllabus excerpt)",
  "type": "Court decision",
  "meta": "U.S. Supreme Court (Justice Samuel F. Miller) · 1873",
  "url": "https://tpsp.web.app/library?q=Slaughter-House%20Cases%20%28syllabus%20excerpt%29",
  "bp": [
   13
  ]
 },
 {
  "id": "sharecropping-contract-1879",
  "title": "Sharecropping Contract, Louisiana (full text)",
  "type": "Other",
  "meta": "Solid South and John Dawson · 1879 · Postdates the unit's 1877 close: the unit teaches sharecropping's standard terms from this contract as a labeled summary, and the contract itself is not printed in the unit",
  "url": "https://tpsp.web.app/library?q=Sharecropping%20Contract%2C%20Louisiana%20%28full%20text%29",
  "bp": [
   9
  ]
 },
 {
  "id": "edisto-island-petition-1865",
  "title": "Petition of the Freedmen of Edisto Island (excerpt)",
  "type": "Petition",
  "meta": "Committee of freedmen, Edisto Island · 1865",
  "url": "https://tpsp.web.app/library?q=Petition%20of%20the%20Freedmen%20of%20Edisto%20Island%20%28excerpt%29",
  "bp": [
   9
  ]
 },
 {
  "id": "revels-school-desegregation-speech-1871",
  "title": "Speech on School Desegregation in the District of Columbia (excerpt)",
  "type": "Speech",
  "meta": "Hiram Rhodes Revels · 1871",
  "url": "https://tpsp.web.app/library?q=Speech%20on%20School%20Desegregation%20in%20the%20District%20of%20Columbia%20%28excerpt%29",
  "bp": [
   8
  ]
 }
];

// ---------------------------------------------------------------------
// Per-unit dataset registry. The planners read the active unit from
// here; each unit plan lives in its own localStorage key, same shape.
window.HCG_RV_BLUEPRINT = {
  1: "Colonial America, 1491\u20131763: the meeting of Europe, Africa, and the Americas, and the colonial societies built from it",
  2: "The Founding, 1763\u20131791: the imperial crisis, independence, and the constitutional settlement",
  3: "Early Republic and Expansion, 1789\u20131848: the working republic, its parties, its courts, and its doubling in size",
  4: "Jackson and Reform, 1828\u20131848: mass democracy's widening, its boundaries, and the reform movements it bred",
  5: "Sectional Crisis and Civil War, 1850\u20131865: the failure of compromise over slavery and the war that settled the Union",
  6: "Reconstruction, 1865\u20131877: the amendments' settlement of freedom and citizenship, and its undoing",
  7: "The Gilded Age, 1877\u20131900: industrial capitalism's transformation and the resistance it organized",
  8: "Progressive Era, 1877\u20131920: the reform answer to industrialism, in the city, the state, and the federal government",
  9: "Imperialism and World War I, 1898\u20131920: the reach for empire, the Great War, and the peace that failed in the Senate",
  10: "The Twenties, 1920\u20131929: prosperity's transformation of American life and the weaknesses inside it",
  11: "Depression and New Deal, 1929\u20131939: the collapse, the experimentation, and the federal government's new settlement",
  12: "World War II, 1935\u20131945: the road to war, total mobilization, the two-ocean victory, and the reckoning",
  13: "The Cold War, 1945\u20131991: containment's architecture, its wars, its home front, and its end from inside",
  14: "Civil Rights, 1947\u20131978: the movement's foundations, its legal victories, and its unfinished agenda",
  15: "Modern America, 1978\u2013present: the conservative turn, globalization, the digital remaking, and the polarized present",
};
window.HCG_RV_LESSONS = [
  { n: 1, title: "Band 1: Colonies and the Founding", question: "How did the meeting of three worlds produce colonial societies, and how did those societies become a republic?" },
  { n: 2, title: "Band 2: A Working Republic and Its Discontents", question: "How did the new republic learn to govern itself, and whose democracy did Jackson's age build?" },
  { n: 3, title: "Band 3: Slavery, War, and the Unfinished Settlement", question: "How did compromise over slavery fail, and what did the war and its settlement settle?" },
  { n: 4, title: "Band 4: Industry and Reform", question: "How did industrial growth transform American life, and how did reformers answer it?" },
  { n: 5, title: "Band 5: Power Abroad, Turmoil at Home", question: "Why did the United States reach for power abroad, and what did the war and the prosperous decade do at home?" },
  { n: 6, title: "Band 6: Depression, Recovery, and Total War", question: "How did depression and total war remake the federal government and the country's place in the world?" },
  { n: 7, title: "Band 7: Cold War Abroad, Rights at Home", question: "How did the Cold War abroad and the movement at home change what the federal government protects?" },
  { n: 8, title: "Band 8: Modern America and the Long Arc", question: "What did the remaking after 1980 settle, and what did it leave open?" },
  { n: 9, title: "Flex Day: The Study Guide and the Crossword", question: "Which band do the practice sets say to reopen, and can you close it today?" }
];
window.HCG_RV_ITEMS = [
  // Band 1
  { id: "rv1-packet", lesson: 1, kind: "Packet", name: "Colonies and the Founding review packet", days: 1, tags: [1, 2], storage: "hcg/course-review/band-1-packet.pdf", core: true },
  { id: "rv1-sprint", lesson: 1, kind: "Term Sprint", name: "Band 1 term sprint", days: 0, tags: [1, 2], storage: "hcg/course-review/band-1-sprint.pdf", core: true },
  { id: "rv1-practice", lesson: 1, kind: "Practice Set", name: "Band 1 practice set", days: 0, tags: [1, 2], storage: "hcg/course-review/band-1-practice.pdf", core: true },
  { id: "rv1-skills", lesson: 1, kind: "Skills Task", name: "Skills task: Sequence and Turning Points", days: 0, tags: [1, 2], storage: "hcg/course-review/band-1-skills.pdf" },
  // Band 2
  { id: "rv2-packet", lesson: 2, kind: "Packet", name: "A Working Republic and Its Discontents review packet", days: 1, tags: [3, 4], storage: "hcg/course-review/band-2-packet.pdf", core: true },
  { id: "rv2-sprint", lesson: 2, kind: "Term Sprint", name: "Band 2 term sprint", days: 0, tags: [3, 4], storage: "hcg/course-review/band-2-sprint.pdf", core: true },
  { id: "rv2-practice", lesson: 2, kind: "Practice Set", name: "Band 2 practice set", days: 0, tags: [3, 4], storage: "hcg/course-review/band-2-practice.pdf", core: true },
  { id: "rv2-skills", lesson: 2, kind: "Skills Task", name: "Skills task: Two Republics, Compared", days: 0, tags: [3, 4], storage: "hcg/course-review/band-2-skills.pdf" },
  // Band 3
  { id: "rv3-packet", lesson: 3, kind: "Packet", name: "Slavery, War, and the Unfinished Settlement review packet", days: 1, tags: [5, 6], storage: "hcg/course-review/band-3-packet.pdf", core: true },
  { id: "rv3-sprint", lesson: 3, kind: "Term Sprint", name: "Band 3 term sprint", days: 0, tags: [5, 6], storage: "hcg/course-review/band-3-sprint.pdf", core: true },
  { id: "rv3-practice", lesson: 3, kind: "Practice Set", name: "Band 3 practice set", days: 0, tags: [5, 6], storage: "hcg/course-review/band-3-practice.pdf", core: true },
  { id: "rv3-skills", lesson: 3, kind: "Skills Task", name: "Skills task: Two Settlements, Two Failures", days: 0, tags: [5, 6], storage: "hcg/course-review/band-3-skills.pdf" },
  // Band 4
  { id: "rv4-packet", lesson: 4, kind: "Packet", name: "Industry and Reform review packet", days: 1, tags: [7, 8], storage: "hcg/course-review/band-4-packet.pdf", core: true },
  { id: "rv4-sprint", lesson: 4, kind: "Term Sprint", name: "Band 4 term sprint", days: 0, tags: [7, 8], storage: "hcg/course-review/band-4-sprint.pdf", core: true },
  { id: "rv4-practice", lesson: 4, kind: "Practice Set", name: "Band 4 practice set", days: 0, tags: [7, 8], storage: "hcg/course-review/band-4-practice.pdf", core: true },
  { id: "rv4-skills", lesson: 4, kind: "Skills Task", name: "Skills task: What Changed, What Did Not", days: 0, tags: [7, 8], storage: "hcg/course-review/band-4-skills.pdf" },
  // Band 5
  { id: "rv5-packet", lesson: 5, kind: "Packet", name: "Power Abroad, Turmoil at Home review packet", days: 1, tags: [9, 10], storage: "hcg/course-review/band-5-packet.pdf", core: true },
  { id: "rv5-sprint", lesson: 5, kind: "Term Sprint", name: "Band 5 term sprint", days: 0, tags: [9, 10], storage: "hcg/course-review/band-5-sprint.pdf", core: true },
  { id: "rv5-practice", lesson: 5, kind: "Practice Set", name: "Band 5 practice set", days: 0, tags: [9, 10], storage: "hcg/course-review/band-5-practice.pdf", core: true },
  { id: "rv5-skills", lesson: 5, kind: "Skills Task", name: "Skills task: The Argument About America in the World, Twice", days: 0, tags: [9, 10], storage: "hcg/course-review/band-5-skills.pdf" },
  // Band 6
  { id: "rv6-packet", lesson: 6, kind: "Packet", name: "Depression, Recovery, and Total War review packet", days: 1, tags: [11, 12], storage: "hcg/course-review/band-6-packet.pdf", core: true },
  { id: "rv6-sprint", lesson: 6, kind: "Term Sprint", name: "Band 6 term sprint", days: 0, tags: [11, 12], storage: "hcg/course-review/band-6-sprint.pdf", core: true },
  { id: "rv6-practice", lesson: 6, kind: "Practice Set", name: "Band 6 practice set", days: 0, tags: [11, 12], storage: "hcg/course-review/band-6-practice.pdf", core: true },
  { id: "rv6-skills", lesson: 6, kind: "Skills Task", name: "Skills task: Two Chains of Cause", days: 0, tags: [11, 12], storage: "hcg/course-review/band-6-skills.pdf" },
  // Band 7
  { id: "rv7-packet", lesson: 7, kind: "Packet", name: "Cold War Abroad, Rights at Home review packet", days: 1, tags: [13, 14], storage: "hcg/course-review/band-7-packet.pdf", core: true },
  { id: "rv7-sprint", lesson: 7, kind: "Term Sprint", name: "Band 7 term sprint", days: 0, tags: [13, 14], storage: "hcg/course-review/band-7-sprint.pdf", core: true },
  { id: "rv7-practice", lesson: 7, kind: "Practice Set", name: "Band 7 practice set", days: 0, tags: [13, 14], storage: "hcg/course-review/band-7-practice.pdf", core: true },
  { id: "rv7-skills", lesson: 7, kind: "Skills Task", name: "Skills task: What Changed, What the Camera Cannot Show", days: 0, tags: [13, 14], storage: "hcg/course-review/band-7-skills.pdf" },
  // Band 8
  { id: "rv8-packet", lesson: 8, kind: "Packet", name: "Modern America and the Long Arc review packet", days: 1, tags: [15], storage: "hcg/course-review/band-8-packet.pdf", core: true },
  { id: "rv8-sprint", lesson: 8, kind: "Term Sprint", name: "Band 8 term sprint", days: 0, tags: [15], storage: "hcg/course-review/band-8-sprint.pdf", core: true },
  { id: "rv8-practice", lesson: 8, kind: "Practice Set", name: "Band 8 practice set", days: 0, tags: [15], storage: "hcg/course-review/band-8-practice.pdf", core: true },
  { id: "rv8-skills", lesson: 8, kind: "Skills Task", name: "Skills task: The Long Arc in Four Documents", days: 0, tags: [15], storage: "hcg/course-review/band-8-skills.pdf" },
  { id: "rv-guide", lesson: 9, kind: "Review", name: "Study guide (flex day)", days: 1, tags: [], storage: "hcg/course-review/study-guide.pdf", core: true },
  { id: "rv-cross", lesson: 9, kind: "Review", name: "Crossword (60 answers)", days: 0.5, tags: [], storage: "hcg/course-review/crossword.pdf" }
];
window.HCG_RV_TOPICS = {
  1: { label: "Federal power and the Constitution", note: "" },
  2: { label: "Expansion and its costs", note: "" },
  3: { label: "Slavery, race, and rights", note: "" },
  4: { label: "Industrial capitalism and labor", note: "" },
  5: { label: "America in the world", note: "" },
  6: { label: "Reform movements", note: "" },
};
window.HCG_RV_BP_TOPIC = {
  1: [2, 3],
  2: [1, 2],
  3: [1, 2],
  4: [1, 3],
  5: [1, 3],
  6: [1, 3],
  7: [3, 4],
  8: [4, 6],
  9: [1, 5],
  10: [4, 6],
  11: [1, 4],
  12: [3, 5],
  13: [1, 5],
  14: [3, 6],
  15: [1, 4],
};
window.HCG_TPSP_RV = [
 {
  "id": "dbq13",
  "title": "Did Colonial America Offer Liberty and Opportunity?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   1
  ]
 },
 {
  "id": "dbq1",
  "title": "Why Did the Colonies Break with Britain?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   2
  ]
 },
 {
  "id": "dbq2",
  "title": "Whose Voices Counted in the Founding?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   2
  ]
 },
 {
  "id": "dbq9",
  "title": "Was Westward Expansion a Story of Opportunity or Conquest?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   3
  ]
 },
 {
  "id": "dbq7",
  "title": "Did the Constitution Create a Democratic Government?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   3
  ]
 },
 {
  "id": "dbq8",
  "title": "Did Andrew Jackson Expand Democracy or Abuse Power?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   4
  ]
 },
 {
  "id": "dbq14",
  "title": "What Strategies Did Reformers Use to Force Change?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   4
  ]
 },
 {
  "id": "dbq3",
  "title": "Was Slavery the Central Cause of the Civil War?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   5
  ]
 },
 {
  "id": "dbq14",
  "title": "What Strategies Did Reformers Use to Force Change?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   5
  ]
 },
 {
  "id": "dbq4",
  "title": "Did Reconstruction Give Freed People Real Freedom?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   6
  ]
 },
 {
  "id": "dbq15",
  "title": "What Forces Brought Reconstruction to an End?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   6
  ]
 },
 {
  "id": "dbq10-industrialization-american-life",
  "title": "Did Industrialization Improve American Life?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   7
  ]
 },
 {
  "id": "dbq16-west-opportunity",
  "title": "For Whom Was the West a Land of Opportunity?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   7
  ]
 },
 {
  "id": "dbq-progressive-era-promises",
  "title": "Progressive Era Promises",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   8
  ]
 },
 {
  "id": "dbq17",
  "title": "Was American Expansion Overseas a Duty or a Betrayal?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   9
  ]
 },
 {
  "id": "dbq18",
  "title": "Did the 1920s Move America Forward?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   10
  ]
 },
 {
  "id": "dbq5",
  "title": "Did the New Deal End the Great Depression?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   11
  ]
 },
 {
  "id": "dbq20",
  "title": "Did World War II Advance Freedom at Home as Well as Abroad?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   12
  ]
 },
 {
  "id": "dbq21",
  "title": "Did Containment Serve American Interests?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   13
  ]
 },
 {
  "id": "dbq22",
  "title": "Did Black Americans in the 1960s Share One Vision of Freedom?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   14
  ]
 },
 {
  "id": "dbq23",
  "title": "How Have Americans Since 1968 Debated What the Country Should Be?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   15
  ]
 }
];

window.HCG_RE_BLUEPRINT = {
  1: "Colonial America, 1491\u20131763: the meeting of Europe, Africa, and the Americas, and the colonial societies built from it",
  2: "The Founding, 1763\u20131791: the imperial crisis, independence, and the constitutional settlement",
  3: "Early Republic and Expansion, 1789\u20131848: the working republic, its parties, its courts, and its doubling in size",
  4: "Jackson and Reform, 1828\u20131848: mass democracy's widening, its boundaries, and the reform movements it bred",
  5: "Sectional Crisis and Civil War, 1850\u20131865: the failure of compromise over slavery and the war that settled the Union",
  6: "Reconstruction, 1865\u20131877: the amendments' settlement of freedom and citizenship, and its undoing",
};
window.HCG_RE_LESSONS = [
  { n: 1, title: "Band 1: Colonies and the Founding", question: "How did the meeting of three worlds produce colonial societies, and how did those societies become a republic?" },
  { n: 2, title: "Band 2: A Working Republic and Its Discontents", question: "How did the new republic learn to govern itself, and whose democracy did Jackson's age build?" },
  { n: 3, title: "Band 3: Slavery, War, and the Unfinished Settlement", question: "How did compromise over slavery fail, and what did the war and its settlement settle?" },
  { n: 4, title: "Flex Day: The Study Guide and the Crossword", question: "Which band do the practice sets say to reopen, and can you close it today?" }
];
window.HCG_RE_ITEMS = [
  // Band 1
  { id: "re1-packet", lesson: 1, kind: "Packet", name: "Colonies and the Founding review packet", days: 1, tags: [1, 2], storage: "hcg/early-review/band-1-packet.pdf", core: true },
  { id: "re1-sprint", lesson: 1, kind: "Term Sprint", name: "Band 1 term sprint", days: 0, tags: [1, 2], storage: "hcg/early-review/band-1-sprint.pdf", core: true },
  { id: "re1-practice", lesson: 1, kind: "Practice Set", name: "Band 1 practice set", days: 0, tags: [1, 2], storage: "hcg/early-review/band-1-practice.pdf", core: true },
  { id: "re1-skills", lesson: 1, kind: "Skills Task", name: "Skills task: Sequence and Turning Points", days: 0, tags: [1, 2], storage: "hcg/early-review/band-1-skills.pdf" },
  // Band 2
  { id: "re2-packet", lesson: 2, kind: "Packet", name: "A Working Republic and Its Discontents review packet", days: 1, tags: [3, 4], storage: "hcg/early-review/band-2-packet.pdf", core: true },
  { id: "re2-sprint", lesson: 2, kind: "Term Sprint", name: "Band 2 term sprint", days: 0, tags: [3, 4], storage: "hcg/early-review/band-2-sprint.pdf", core: true },
  { id: "re2-practice", lesson: 2, kind: "Practice Set", name: "Band 2 practice set", days: 0, tags: [3, 4], storage: "hcg/early-review/band-2-practice.pdf", core: true },
  { id: "re2-skills", lesson: 2, kind: "Skills Task", name: "Skills task: Two Republics, Compared", days: 0, tags: [3, 4], storage: "hcg/early-review/band-2-skills.pdf" },
  // Band 3
  { id: "re3-packet", lesson: 3, kind: "Packet", name: "Slavery, War, and the Unfinished Settlement review packet", days: 1, tags: [5, 6], storage: "hcg/early-review/band-3-packet.pdf", core: true },
  { id: "re3-sprint", lesson: 3, kind: "Term Sprint", name: "Band 3 term sprint", days: 0, tags: [5, 6], storage: "hcg/early-review/band-3-sprint.pdf", core: true },
  { id: "re3-practice", lesson: 3, kind: "Practice Set", name: "Band 3 practice set", days: 0, tags: [5, 6], storage: "hcg/early-review/band-3-practice.pdf", core: true },
  { id: "re3-skills", lesson: 3, kind: "Skills Task", name: "Skills task: Two Settlements, Two Failures", days: 0, tags: [5, 6], storage: "hcg/early-review/band-3-skills.pdf" },
  { id: "re-guide", lesson: 4, kind: "Review", name: "Study guide (flex day)", days: 1, tags: [], storage: "hcg/early-review/study-guide.pdf", core: true },
  { id: "re-cross", lesson: 4, kind: "Review", name: "Crossword (24 answers)", days: 0.5, tags: [], storage: "hcg/early-review/crossword.pdf" }
];
window.HCG_RE_TOPICS = {
  1: { label: "Federal power and the Constitution", note: "" },
  2: { label: "Expansion and its costs", note: "" },
  3: { label: "Slavery, race, and rights", note: "" },
  4: { label: "Industrial capitalism and labor", note: "" },
  5: { label: "America in the world", note: "" },
  6: { label: "Reform movements", note: "" },
};
window.HCG_RE_BP_TOPIC = {
  1: [2, 3],
  2: [1, 2],
  3: [1, 2],
  4: [1, 3],
  5: [1, 3],
  6: [1, 3],
};
window.HCG_TPSP_RE = [
 {
  "id": "dbq13",
  "title": "Did Colonial America Offer Liberty and Opportunity?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   1
  ]
 },
 {
  "id": "dbq1",
  "title": "Why Did the Colonies Break with Britain?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   2
  ]
 },
 {
  "id": "dbq2",
  "title": "Whose Voices Counted in the Founding?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   2
  ]
 },
 {
  "id": "dbq9",
  "title": "Was Westward Expansion a Story of Opportunity or Conquest?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   3
  ]
 },
 {
  "id": "dbq7",
  "title": "Did the Constitution Create a Democratic Government?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   3
  ]
 },
 {
  "id": "dbq8",
  "title": "Did Andrew Jackson Expand Democracy or Abuse Power?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   4
  ]
 },
 {
  "id": "dbq14",
  "title": "What Strategies Did Reformers Use to Force Change?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   4
  ]
 },
 {
  "id": "dbq3",
  "title": "Was Slavery the Central Cause of the Civil War?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   5
  ]
 },
 {
  "id": "dbq14",
  "title": "What Strategies Did Reformers Use to Force Change?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   5
  ]
 },
 {
  "id": "dbq4",
  "title": "Did Reconstruction Give Freed People Real Freedom?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   6
  ]
 },
 {
  "id": "dbq15",
  "title": "What Forces Brought Reconstruction to an End?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   6
  ]
 }
];

window.HCG_RM_BLUEPRINT = {
  1: "The Gilded Age, 1877\u20131900: industrial capitalism's transformation and the resistance it organized",
  2: "Progressive Era, 1877\u20131920: the reform answer to industrialism, in the city, the state, and the federal government",
  3: "Imperialism and World War I, 1898\u20131920: the reach for empire, the Great War, and the peace that failed in the Senate",
  4: "The Twenties, 1920\u20131929: prosperity's transformation of American life and the weaknesses inside it",
  5: "Depression and New Deal, 1929\u20131939: the collapse, the experimentation, and the federal government's new settlement",
  6: "World War II, 1935\u20131945: the road to war, total mobilization, the two-ocean victory, and the reckoning",
  7: "The Cold War, 1945\u20131991: containment's architecture, its wars, its home front, and its end from inside",
  8: "Civil Rights, 1947\u20131978: the movement's foundations, its legal victories, and its unfinished agenda",
  9: "Modern America, 1978\u2013present: the conservative turn, globalization, the digital remaking, and the polarized present",
};
window.HCG_RM_LESSONS = [
  { n: 1, title: "Band 4: Industry and Reform", question: "How did industrial growth transform American life, and how did reformers answer it?" },
  { n: 2, title: "Band 5: Power Abroad, Turmoil at Home", question: "Why did the United States reach for power abroad, and what did the war and the prosperous decade do at home?" },
  { n: 3, title: "Band 6: Depression, Recovery, and Total War", question: "How did depression and total war remake the federal government and the country's place in the world?" },
  { n: 4, title: "Band 7: Cold War Abroad, Rights at Home", question: "How did the Cold War abroad and the movement at home change what the federal government protects?" },
  { n: 5, title: "Band 8: Modern America and the Long Arc", question: "What did the remaking after 1980 settle, and what did it leave open?" },
  { n: 6, title: "Flex Day: The Study Guide and the Crossword", question: "Which band do the practice sets say to reopen, and can you close it today?" }
];
window.HCG_RM_ITEMS = [
  // Band 4
  { id: "rm1-packet", lesson: 1, kind: "Packet", name: "Industry and Reform review packet", days: 1, tags: [1, 2], storage: "hcg/modern-review/band-4-packet.pdf", core: true },
  { id: "rm1-sprint", lesson: 1, kind: "Term Sprint", name: "Band 4 term sprint", days: 0, tags: [1, 2], storage: "hcg/modern-review/band-4-sprint.pdf", core: true },
  { id: "rm1-practice", lesson: 1, kind: "Practice Set", name: "Band 4 practice set", days: 0, tags: [1, 2], storage: "hcg/modern-review/band-4-practice.pdf", core: true },
  { id: "rm1-skills", lesson: 1, kind: "Skills Task", name: "Skills task: What Changed, What Did Not", days: 0, tags: [1, 2], storage: "hcg/modern-review/band-4-skills.pdf" },
  // Band 5
  { id: "rm2-packet", lesson: 2, kind: "Packet", name: "Power Abroad, Turmoil at Home review packet", days: 1, tags: [3, 4], storage: "hcg/modern-review/band-5-packet.pdf", core: true },
  { id: "rm2-sprint", lesson: 2, kind: "Term Sprint", name: "Band 5 term sprint", days: 0, tags: [3, 4], storage: "hcg/modern-review/band-5-sprint.pdf", core: true },
  { id: "rm2-practice", lesson: 2, kind: "Practice Set", name: "Band 5 practice set", days: 0, tags: [3, 4], storage: "hcg/modern-review/band-5-practice.pdf", core: true },
  { id: "rm2-skills", lesson: 2, kind: "Skills Task", name: "Skills task: The Argument About America in the World, Twice", days: 0, tags: [3, 4], storage: "hcg/modern-review/band-5-skills.pdf" },
  // Band 6
  { id: "rm3-packet", lesson: 3, kind: "Packet", name: "Depression, Recovery, and Total War review packet", days: 1, tags: [5, 6], storage: "hcg/modern-review/band-6-packet.pdf", core: true },
  { id: "rm3-sprint", lesson: 3, kind: "Term Sprint", name: "Band 6 term sprint", days: 0, tags: [5, 6], storage: "hcg/modern-review/band-6-sprint.pdf", core: true },
  { id: "rm3-practice", lesson: 3, kind: "Practice Set", name: "Band 6 practice set", days: 0, tags: [5, 6], storage: "hcg/modern-review/band-6-practice.pdf", core: true },
  { id: "rm3-skills", lesson: 3, kind: "Skills Task", name: "Skills task: Two Chains of Cause", days: 0, tags: [5, 6], storage: "hcg/modern-review/band-6-skills.pdf" },
  // Band 7
  { id: "rm4-packet", lesson: 4, kind: "Packet", name: "Cold War Abroad, Rights at Home review packet", days: 1, tags: [7, 8], storage: "hcg/modern-review/band-7-packet.pdf", core: true },
  { id: "rm4-sprint", lesson: 4, kind: "Term Sprint", name: "Band 7 term sprint", days: 0, tags: [7, 8], storage: "hcg/modern-review/band-7-sprint.pdf", core: true },
  { id: "rm4-practice", lesson: 4, kind: "Practice Set", name: "Band 7 practice set", days: 0, tags: [7, 8], storage: "hcg/modern-review/band-7-practice.pdf", core: true },
  { id: "rm4-skills", lesson: 4, kind: "Skills Task", name: "Skills task: What Changed, What the Camera Cannot Show", days: 0, tags: [7, 8], storage: "hcg/modern-review/band-7-skills.pdf" },
  // Band 8
  { id: "rm5-packet", lesson: 5, kind: "Packet", name: "Modern America and the Long Arc review packet", days: 1, tags: [9], storage: "hcg/modern-review/band-8-packet.pdf", core: true },
  { id: "rm5-sprint", lesson: 5, kind: "Term Sprint", name: "Band 8 term sprint", days: 0, tags: [9], storage: "hcg/modern-review/band-8-sprint.pdf", core: true },
  { id: "rm5-practice", lesson: 5, kind: "Practice Set", name: "Band 8 practice set", days: 0, tags: [9], storage: "hcg/modern-review/band-8-practice.pdf", core: true },
  { id: "rm5-skills", lesson: 5, kind: "Skills Task", name: "Skills task: The Long Arc in Four Documents", days: 0, tags: [9], storage: "hcg/modern-review/band-8-skills.pdf" },
  { id: "rm-guide", lesson: 6, kind: "Review", name: "Study guide (flex day)", days: 1, tags: [], storage: "hcg/modern-review/study-guide.pdf", core: true },
  { id: "rm-cross", lesson: 6, kind: "Review", name: "Crossword (36 answers)", days: 0.5, tags: [], storage: "hcg/modern-review/crossword.pdf" }
];
window.HCG_RM_TOPICS = {
  1: { label: "Federal power and the Constitution", note: "" },
  2: { label: "Expansion and its costs", note: "" },
  3: { label: "Slavery, race, and rights", note: "" },
  4: { label: "Industrial capitalism and labor", note: "" },
  5: { label: "America in the world", note: "" },
  6: { label: "Reform movements", note: "" },
};
window.HCG_RM_BP_TOPIC = {
  1: [3, 4],
  2: [4, 6],
  3: [1, 5],
  4: [4, 6],
  5: [1, 4],
  6: [3, 5],
  7: [1, 5],
  8: [3, 6],
  9: [1, 4],
};
window.HCG_TPSP_RM = [
 {
  "id": "dbq10-industrialization-american-life",
  "title": "Did Industrialization Improve American Life?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   1
  ]
 },
 {
  "id": "dbq16-west-opportunity",
  "title": "For Whom Was the West a Land of Opportunity?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   1
  ]
 },
 {
  "id": "dbq-progressive-era-promises",
  "title": "Progressive Era Promises",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   2
  ]
 },
 {
  "id": "dbq17",
  "title": "Was American Expansion Overseas a Duty or a Betrayal?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   3
  ]
 },
 {
  "id": "dbq18",
  "title": "Did the 1920s Move America Forward?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   4
  ]
 },
 {
  "id": "dbq5",
  "title": "Did the New Deal End the Great Depression?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   5
  ]
 },
 {
  "id": "dbq20",
  "title": "Did World War II Advance Freedom at Home as Well as Abroad?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   6
  ]
 },
 {
  "id": "dbq21",
  "title": "Did Containment Serve American Interests?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   7
  ]
 },
 {
  "id": "dbq22",
  "title": "Did Black Americans in the 1960s Share One Vision of Freedom?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   8
  ]
 },
 {
  "id": "dbq23",
  "title": "How Have Americans Since 1968 Debated What the Country Should Be?",
  "type": "Premium DBQ",
  "meta": "The Primary Source Project · premium document-based question",
  "url": "https://tpsp.web.app/library?tab=premium",
  "dbq": true,
  "bp": [
   9
  ]
 }
];

window.HCG_UNITS = {
  pe: {
    id: "pe", courseId: "pe", key: "hcg_unit_v1",
    name: "The Progressive Era", shortName: "Progressive Era",
    essentialQuestion: "How did Americans respond to the problems created by industrialization, urbanization, and political corruption?",
    topicsHead: "Industrialization and Progressivism, 1877\u20131920",
    tpspIntro: "From The Primary Source Project's Progressive Era library. Click a source to add it to your plan; a few arrive pre-tagged to the blueprint where the match is clear, and you can retag any of them with Edit.",
    testFile: "files/unit-test.pdf", testStorage: null, testName: "unit-test.pdf",
    icsSlug: "progressive-era", rycalDeck: "https://rycal.web.app/hcg-progressive-era-flashcards", exportFile: "hcg-unit-plan.json",
    blueprint: window.HCG_BLUEPRINT, lessons: window.HCG_LESSONS, items: window.HCG_ITEMS,
    topics: window.HCG_TOPICS, bpTopic: window.HCG_BP_TOPIC, tpsp: window.HCG_TPSP_PE
  },
  ga: {
    id: "ga", courseId: "u7", key: "hcg_unit_ga_v1",
    name: "The Gilded Age", shortName: "Gilded Age",
    essentialQuestion: "How did industrial growth transform American life, and who gained, who paid, and who resisted?",
    topicsHead: "Industrialization and the Gilded Age, 1877\u20131900",
    tpspIntro: "From The Primary Source Project's Gilded Age library. Click a source to add it to your plan; a few arrive pre-tagged to the blueprint where the match is clear, and you can retag any of them with Edit.",
    testFile: null, testStorage: "hcg/gilded-age/unit-test.pdf", testName: "unit-test.pdf",
    icsSlug: "gilded-age", rycalDeck: "https://rycal.web.app/hcg-gilded-age-flashcards", exportFile: "hcg-unit-plan-gilded-age.json",
    blueprint: window.HCG_GA_BLUEPRINT, lessons: window.HCG_GA_LESSONS, items: window.HCG_GA_ITEMS,
    topics: window.HCG_GA_TOPICS, bpTopic: window.HCG_GA_BP_TOPIC, tpsp: window.HCG_TPSP_GA,
    unitPage: "gilded-era.html"
  },
  wwi: {
    id: "wwi", courseId: "wwi", key: "hcg_unit_wwi_v1",
    name: "Imperialism and World War I", shortName: "Imperialism and World War I",
    essentialQuestion: "Why did the United States seek power overseas, and how did the First World War change the country that fought it?",
    topicsHead: "Expansion and the Great War, 1898\u20131920",
    tpspIntro: "From The Primary Source Project's Imperialism and World War I library. Click a source to add it to your plan; a few arrive pre-tagged to the blueprint where the match is clear, and you can retag any of them with Edit.",
    testFile: null, testStorage: "hcg/imperialism-wwi/unit-test.pdf", testName: "unit-test.pdf",
    icsSlug: "imperialism-wwi", rycalDeck: "https://rycal.web.app/hcg-imperialism-wwi-flashcards", exportFile: "hcg-unit-plan-imperialism-wwi.json",
    blueprint: window.HCG_WWI_BLUEPRINT, lessons: window.HCG_WWI_LESSONS, items: window.HCG_WWI_ITEMS,
    topics: window.HCG_WWI_TOPICS, bpTopic: window.HCG_WWI_BP_TOPIC, tpsp: window.HCG_TPSP_WWI,
    unitPage: "imperialism-wwi.html"
  },
  tw: {
    id: "tw", courseId: "u9", key: "hcg_unit_tw_v1",
    name: "The Twenties", shortName: "Twenties",
    essentialQuestion: "How did the prosperity of the 1920s change American life, and why was that prosperity weaker than it looked?",
    topicsHead: "Prosperity and Its Limits, 1920\u20131929",
    tpspIntro: "From The Primary Source Project's Twenties library. Click a source to add it to your plan; a few arrive pre-tagged to the blueprint where the match is clear, and you can retag any of them with Edit.",
    testFile: null, testStorage: "hcg/twenties/unit-test.pdf", testName: "unit-test.pdf",
    icsSlug: "twenties", rycalDeck: "https://rycal.web.app/hcg-twenties-flashcards", exportFile: "hcg-unit-plan-twenties.json",
    blueprint: window.HCG_TW_BLUEPRINT, lessons: window.HCG_TW_LESSONS, items: window.HCG_TW_ITEMS,
    topics: window.HCG_TW_TOPICS, bpTopic: window.HCG_TW_BP_TOPIC, tpsp: window.HCG_TPSP_TW,
    unitPage: "twenties.html"
  },
  dp: {
    id: "dp", courseId: "u10", key: "hcg_unit_dp_v1",
    name: "Depression and New Deal", shortName: "Depression and New Deal",
    essentialQuestion: "How did the New Deal change the relationship between Americans and their federal government, and what did it leave undone?",
    topicsHead: "Depression and the New Deal, 1929\u20131939",
    tpspIntro: "From The Primary Source Project's Depression and New Deal library. Click a source to add it to your plan; a few arrive pre-tagged to the blueprint where the match is clear, and you can retag any of them with Edit.",
    testFile: null, testStorage: "hcg/depression-new-deal/unit-test.pdf", testName: "unit-test.pdf",
    icsSlug: "depression-new-deal", rycalDeck: "https://rycal.web.app/hcg-depression-new-deal-flashcards", exportFile: "hcg-unit-plan-depression-new-deal.json",
    blueprint: window.HCG_DP_BLUEPRINT, lessons: window.HCG_DP_LESSONS, items: window.HCG_DP_ITEMS,
    topics: window.HCG_DP_TOPICS, bpTopic: window.HCG_DP_BP_TOPIC, tpsp: window.HCG_TPSP_DP,
    unitPage: "depression-new-deal.html"
  },
  ww2: {
    id: "ww2", courseId: "u11", key: "hcg_unit_ww2_v1",
    name: "World War II", shortName: "World War II",
    essentialQuestion: "How did the Second World War transform the United States, and how far did the country live up to the democracy it claimed to defend?",
    topicsHead: "World War II, 1935\u20131945",
    tpspIntro: "From The Primary Source Project's World War II library. Click a source to add it to your plan; a few arrive pre-tagged to the blueprint where the match is clear, and you can retag any of them with Edit.",
    testFile: null, testStorage: "hcg/world-war-ii/unit-test.pdf", testName: "unit-test.pdf",
    icsSlug: "world-war-ii", rycalDeck: "https://rycal.web.app/hcg-world-war-ii-flashcards", exportFile: "hcg-unit-plan-world-war-ii.json",
    blueprint: window.HCG_WW2_BLUEPRINT, lessons: window.HCG_WW2_LESSONS, items: window.HCG_WW2_ITEMS,
    topics: window.HCG_WW2_TOPICS, bpTopic: window.HCG_WW2_BP_TOPIC, tpsp: window.HCG_TPSP_WW2,
    unitPage: "world-war-ii.html"
  },
  cw: {
    id: "cw", courseId: "u12", key: "hcg_unit_cw_v1",
    name: "The Cold War", shortName: "Cold War",
    essentialQuestion: "How did the struggle between the United States and the Soviet Union reshape the world and American life, and why did it end the way it did?",
    topicsHead: "The Cold War, 1945\u20131991",
    tpspIntro: "From The Primary Source Project's Cold War library. Click a source to add it to your plan; a few arrive pre-tagged to the blueprint where the match is clear, and you can retag any of them with Edit.",
    testFile: null, testStorage: "hcg/cold-war/unit-test.pdf", testName: "unit-test.pdf",
    icsSlug: "cold-war", rycalDeck: "https://rycal.web.app/hcg-cold-war-flashcards", exportFile: "hcg-unit-plan-cold-war.json",
    blueprint: window.HCG_CW_BLUEPRINT, lessons: window.HCG_CW_LESSONS, items: window.HCG_CW_ITEMS,
    topics: window.HCG_CW_TOPICS, bpTopic: window.HCG_CW_BP_TOPIC, tpsp: window.HCG_TPSP_CW,
    unitPage: "cold-war.html"
  },
  cr: {
    id: "cr", courseId: "u13", key: "hcg_unit_cr_v1",
    name: "Civil Rights", shortName: "Civil Rights",
    essentialQuestion: "How did the civil rights movement change American law and American life, and what did it leave unfinished?",
    topicsHead: "Civil Rights, 1947\u20131978",
    tpspIntro: "From The Primary Source Project's Civil Rights library. Click a source to add it to your plan; a few arrive pre-tagged to the blueprint where the match is clear, and you can retag any of them with Edit.",
    testFile: null, testStorage: "hcg/civil-rights/unit-test.pdf", testName: "unit-test.pdf",
    icsSlug: "civil-rights", rycalDeck: "https://rycal.web.app/hcg-civil-rights-flashcards", exportFile: "hcg-unit-plan-civil-rights.json",
    blueprint: window.HCG_CR_BLUEPRINT, lessons: window.HCG_CR_LESSONS, items: window.HCG_CR_ITEMS,
    topics: window.HCG_CR_TOPICS, bpTopic: window.HCG_CR_BP_TOPIC, tpsp: window.HCG_TPSP_CR,
    unitPage: "civil-rights.html"
  },
  ma: {
    id: "ma", courseId: "u14", key: "hcg_unit_ma_v1",
    name: "Modern America", shortName: "Modern America",
    essentialQuestion: "How did the United States remake itself after 1980, in its economy, its population, and its place in the world, and what did the remaking settle and what did it leave open?",
    topicsHead: "Modern America, 1978\u2013present",
    tpspIntro: "From The Primary Source Project's Modern America library. Click a source to add it to your plan; a few arrive pre-tagged to the blueprint where the match is clear, and you can retag any of them with Edit.",
    testFile: null, testStorage: "hcg/modern-america/unit-test.pdf", testName: "unit-test.pdf",
    icsSlug: "modern-america", rycalDeck: "https://rycal.web.app/hcg-modern-america-flashcards", exportFile: "hcg-unit-plan-modern-america.json",
    blueprint: window.HCG_MA_BLUEPRINT, lessons: window.HCG_MA_LESSONS, items: window.HCG_MA_ITEMS,
    topics: window.HCG_MA_TOPICS, bpTopic: window.HCG_MA_BP_TOPIC, tpsp: window.HCG_TPSP_MA,
    unitPage: "modern-america.html"
  },
  ca: {
    id: "ca", courseId: "u1", key: "hcg_unit_ca_v1",
    name: "Colonial America", shortName: "Colonial America",
    essentialQuestion: "How did the meeting of Europe, Africa, and the Americas remake all three worlds, and what kind of society grew up in England's colonies?",
    topicsHead: "Colonial America, 1491\u20131763",
    tpspIntro: "From The Primary Source Project's Colonial America library. Click a source to add it to your plan; a few arrive pre-tagged to the blueprint where the match is clear, and you can retag any of them with Edit.",
    testFile: null, testStorage: "hcg/colonial-america/unit-test.pdf", testName: "unit-test.pdf",
    icsSlug: "colonial-america", rycalDeck: "https://rycal.web.app/hcg-colonial-america-flashcards", exportFile: "hcg-unit-plan-colonial-america.json",
    blueprint: window.HCG_CA_BLUEPRINT, lessons: window.HCG_CA_LESSONS, items: window.HCG_CA_ITEMS,
    topics: window.HCG_CA_TOPICS, bpTopic: window.HCG_CA_BP_TOPIC, tpsp: window.HCG_TPSP_CA,
    unitPage: "colonial-america.html"
  },
  fd: {
    id: "fd", courseId: "u2", key: "hcg_unit_fd_v1",
    name: "The Founding", shortName: "Founding",
    essentialQuestion: "Why did the colonies break with Britain, and what did Americans build in the place of the empire they rejected?",
    topicsHead: "The Founding, 1763\u20131791",
    tpspIntro: "From The Primary Source Project's Founding library. Click a source to add it to your plan; a few arrive pre-tagged to the blueprint where the match is clear, and you can retag any of them with Edit.",
    testFile: null, testStorage: "hcg/the-founding/unit-test.pdf", testName: "unit-test.pdf",
    icsSlug: "the-founding", rycalDeck: "https://rycal.web.app/hcg-the-founding-flashcards", exportFile: "hcg-unit-plan-the-founding.json",
    blueprint: window.HCG_FD_BLUEPRINT, lessons: window.HCG_FD_LESSONS, items: window.HCG_FD_ITEMS,
    topics: window.HCG_FD_TOPICS, bpTopic: window.HCG_FD_BP_TOPIC, tpsp: window.HCG_TPSP_FD,
    unitPage: "the-founding.html"
  },
  er: {
    id: "er", courseId: "u3", key: "hcg_unit_er_v1",
    name: "Early Republic and Expansion", shortName: "Early Republic",
    essentialQuestion: "How did the United States turn its Constitution into a working government, and what did continental expansion do to the republic that government served?",
    topicsHead: "Early Republic and Expansion, 1789\u20131848",
    tpspIntro: "From The Primary Source Project's Early Republic library. Click a source to add it to your plan; a few arrive pre-tagged to the blueprint where the match is clear, and you can retag any of them with Edit.",
    testFile: null, testStorage: "hcg/early-republic/unit-test.pdf", testName: "unit-test.pdf",
    icsSlug: "early-republic", rycalDeck: "https://rycal.web.app/hcg-early-republic-flashcards", exportFile: "hcg-unit-plan-early-republic.json",
    blueprint: window.HCG_ER_BLUEPRINT, lessons: window.HCG_ER_LESSONS, items: window.HCG_ER_ITEMS,
    topics: window.HCG_ER_TOPICS, bpTopic: window.HCG_ER_BP_TOPIC, tpsp: window.HCG_TPSP_ER,
    unitPage: "early-republic.html"
  },
  jr: {
    id: "jr", courseId: "u4", key: "hcg_unit_jr_v1",
    name: "Jackson and Reform", shortName: "Jackson and Reform",
    essentialQuestion: "What did democracy mean in Jackson's America, who was it for, and what did the era's reformers claim it still owed?",
    topicsHead: "Jackson and Reform, 1828\u20131848",
    tpspIntro: "From The Primary Source Project's Jackson and Reform library. Click a source to add it to your plan; a few arrive pre-tagged to the blueprint where the match is clear, and you can retag any of them with Edit.",
    testFile: null, testStorage: "hcg/jackson-reform/unit-test.pdf", testName: "unit-test.pdf",
    icsSlug: "jackson-reform", rycalDeck: "https://rycal.web.app/hcg-jackson-reform-flashcards", exportFile: "hcg-unit-plan-jackson-reform.json",
    blueprint: window.HCG_JR_BLUEPRINT, lessons: window.HCG_JR_LESSONS, items: window.HCG_JR_ITEMS,
    topics: window.HCG_JR_TOPICS, bpTopic: window.HCG_JR_BP_TOPIC, tpsp: window.HCG_TPSP_JR,
    unitPage: "jackson-reform.html"
  },
  sc: {
    id: "sc", courseId: "u5", key: "hcg_unit_sc_v1", name: "Sectional Crisis and Civil War",
    shortName: "Sectional Crisis",
    essentialQuestion: "How did compromise over slavery finally fail, and what did the war it caused settle about slavery and the Union, and what did it leave open?",
    blueprint: window.HCG_SC_BLUEPRINT, lessons: window.HCG_SC_LESSONS, items: window.HCG_SC_ITEMS,
    topics: window.HCG_SC_TOPICS, topicsHead: "Sectional Crisis and Civil War, 1850\u20131865",
    bpTopic: window.HCG_SC_BP_TOPIC, tpsp: window.HCG_TPSP_SC,
    tpspIntro: "From The Primary Source Project's Sectional Crisis library. Click a source to add it to your plan; a few arrive pre-tagged to the blueprint where the match is clear, and you can retag any of them with Edit.",
    testFile: null, testStorage: "hcg/sectional-crisis/unit-test.pdf", testName: "unit-test.pdf",
    icsSlug: "sectional-crisis", rycalDeck: "https://rycal.web.app/hcg-sectional-crisis-flashcards", exportFile: "hcg-unit-plan-sectional-crisis.json",
    unitPage: "sectional-crisis.html"
  },
  rc: {
    id: "rc", courseId: "u6", key: "hcg_unit_rc_v1", name: "Reconstruction",
    shortName: "Reconstruction",
    essentialQuestion: "What did Reconstruction settle about freedom, citizenship, and the federal Union, and what did it leave open?",
    blueprint: window.HCG_RC_BLUEPRINT, lessons: window.HCG_RC_LESSONS, items: window.HCG_RC_ITEMS,
    topics: window.HCG_RC_TOPICS, topicsHead: "Reconstruction, 1865\u20131877",
    bpTopic: window.HCG_RC_BP_TOPIC, tpsp: window.HCG_TPSP_RC,
    tpspIntro: "From The Primary Source Project's Reconstruction library. Click a source to add it to your plan; a few arrive pre-tagged to the blueprint where the match is clear, and you can retag any of them with Edit.",
    testFile: null, testStorage: "hcg/reconstruction/unit-test.pdf", testName: "unit-test.pdf",
    icsSlug: "reconstruction", rycalDeck: "https://rycal.web.app/hcg-reconstruction-flashcards", exportFile: "hcg-unit-plan-reconstruction.json",
    unitPage: "reconstruction.html"
  },
  rv: {
    id: "rv", courseId: "u15", key: "hcg_unit_rv_v1",
    fitMin: 7,
    name: "Course Review", shortName: "Course Review",
    essentialQuestion: "How did the United States become what it is, and which of the course's own arguments best explains the country that resulted?",
    topicsHead: "The Whole Course, 1491\u2013present",
    tpspIntro: "From The Primary Source Project's premium DBQ library. Every premium DBQ is a complete document essay on one unit of the course; click one to add it as a writing day. Each arrives pre-tagged to the unit it reviews, and you can retag any of them with Edit.",
    testFile: null, testStorage: "hcg/course-review/practice-test.pdf", testName: "practice-test.pdf",
    icsSlug: "course-review", rycalDeck: "https://rycal.web.app/hcg-course-review-flashcards", exportFile: "hcg-unit-plan-course-review.json",
    blueprint: window.HCG_RV_BLUEPRINT, lessons: window.HCG_RV_LESSONS, items: window.HCG_RV_ITEMS,
    topics: window.HCG_RV_TOPICS, bpTopic: window.HCG_RV_BP_TOPIC, tpsp: window.HCG_TPSP_RV,
    unitPage: "course-review.html"
  },
  re: {
    id: "re", courseId: "u16", key: "hcg_unit_re_v1",
    fitMin: 4,
    name: "Early Course Review", shortName: "Early Course Review",
    essentialQuestion: "How did a fringe of British colonies become a continental republic, and what did its founding settlements settle and leave open?",
    topicsHead: "America to 1877, 1491\u20131877",
    tpspIntro: "From The Primary Source Project's premium DBQ library. Every premium DBQ is a complete document essay on one unit of the course; click one to add it as a writing day. Each arrives pre-tagged to the unit it reviews, and you can retag any of them with Edit.",
    testFile: null, testStorage: "hcg/early-review/practice-test.pdf", testName: "practice-test.pdf",
    icsSlug: "early-review", rycalDeck: "https://rycal.web.app/hcg-early-review-flashcards", exportFile: "hcg-unit-plan-early-review.json",
    blueprint: window.HCG_RE_BLUEPRINT, lessons: window.HCG_RE_LESSONS, items: window.HCG_RE_ITEMS,
    topics: window.HCG_RE_TOPICS, bpTopic: window.HCG_RE_BP_TOPIC, tpsp: window.HCG_TPSP_RE,
    unitPage: "early-review.html"
  },
  rm: {
    id: "rm", courseId: "u17", key: "hcg_unit_rm_v1",
    fitMin: 5,
    name: "Modern Course Review", shortName: "Modern Course Review",
    essentialQuestion: "How did industrial America remake the nation's economy, its democracy, and its place in the world, and what did the remaking leave unsettled?",
    topicsHead: "America Since 1877, 1877\u2013present",
    tpspIntro: "From The Primary Source Project's premium DBQ library. Every premium DBQ is a complete document essay on one unit of the course; click one to add it as a writing day. Each arrives pre-tagged to the unit it reviews, and you can retag any of them with Edit.",
    testFile: null, testStorage: "hcg/modern-review/practice-test.pdf", testName: "practice-test.pdf",
    icsSlug: "modern-review", rycalDeck: "https://rycal.web.app/hcg-modern-review-flashcards", exportFile: "hcg-unit-plan-modern-review.json",
    blueprint: window.HCG_RM_BLUEPRINT, lessons: window.HCG_RM_LESSONS, items: window.HCG_RM_ITEMS,
    topics: window.HCG_RM_TOPICS, bpTopic: window.HCG_RM_BP_TOPIC, tpsp: window.HCG_TPSP_RM,
    unitPage: "modern-review.html"
  }
};
