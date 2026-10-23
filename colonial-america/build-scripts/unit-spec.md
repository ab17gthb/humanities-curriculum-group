# Colonial America: shared build spec

Unit essential question: How did the meeting of Europe, Africa, and the Americas remake all three worlds, and what kind of society grew up in England's colonies?

Skeleton: ~/workspace/curriculum-planner/colonial-america-skeleton.md (read it first; your lesson's section is your assignment).
Model units: ~/workspace/curriculum-planner/civil-rights/ and ~/workspace/curriculum-planner/cold-war/ — before writing any document type, open the corresponding Civil Rights file and mirror its structure, CSS, and conventions exactly. Build PDFs with: python3 ~/workspace/curriculum-planner/templates/build_pdf.py <file.html>
Brandmark (first element in body of every document): <p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>
Deck system: ~/workspace/curriculum-planner/colonial-america/deck_common.py (copy of the Civil Rights system). Teacher notes builder: copy build_notes_doc.py from a Civil Rights lesson's slides-build/ and adapt. Decks keep headings.json in slides-build/.
Audited source texts: the TPSP bank file ~/workspace/primary-source/vite-react-main/public/data/colonial.json holds verbatim audited text with the edition named in each record's sourceNote; the Díaz entry into Tenochtitlan and the Code Noir are in ~/workspace/primary-source/vite-react-main/public/data/early-modern-empire.json. Quote from those records, with cuts marked by ellipses and the edition named in the Source line. Never quote a period text from memory where a bank record exists, and never quote one at all without a named edition.

## Edition discipline (binding on every document in this unit)
Period texts are public domain, but the edition still matters. Where the bank carries the text, quote the bank record and name the edition its sourceNote names. Where the bank does not carry it (the Navigation Acts, Virginia's statutes of 1662 and 1667, the Negro Act of 1740, Whitefield's journals, Washington's 1754 journal, the Albany Plan, the Treaty of Paris of 1763, the Proclamation of 1763), name the transcription or facsimile edition you actually used in the document's Source line and in the lesson's img/SOURCES.md: a standard scholarly transcription, the holding archive's transcript (Library of Congress, National Archives, Avalon Project at Yale, Fordham's Internet History Sourcebooks, the Statutes at Large), or the session-law printing. Early modern spelling stays as the edition carries it; if you modernize spelling for student readers, the Source line says the spelling is modernized. Figures from the Trans-Atlantic Slave Trade Database are stated as its estimates wherever they appear.

## Hard rules (all documents, decks, notes)
- Zero em dashes and zero en dashes anywhere. Zero instances of the construction "that matters" or "that <anything> matters".
- No colon-led paragraph labels in prose, no decorative quotes, no canned transitions, no motivational closers. Ordinary colons in labels, source lines, and times are fine.
- Audience rule: student-facing files are addressed entirely to the student. No product talk, no marketing copy, no grade-band lines anywhere in the documents. Teacher keys carry pedagogy.
- Readings: 850 to 900 words of body text (count by the standard method, words in the reading's section paragraphs; count and report the exact count), five questions, teacher key on its own page at the back with each question restated as a bold lead-in.
- Guided notes: Name/Date/Period line, lesson question, unit question frame, Key Terms list with the definitions below VERBATIM, lettered sections A to G matching the reading, numbered fill-in blanks, a closing summary table, an exit ticket (3 questions), teacher key with every blank answered. Definitions must match the list below character for character.
- Activity: locked print design from the Civil Rights activity (read one first): 5 stations with Source lines and questions with writing space (0.72in), a closing ranking or verdict task with paragraph space (1.9in), teacher key at the back.
- Notebook page: one chart organizer filled from the lesson plus one writing prompt, teacher key with the chart filled in.
- Quick check: short formative, every item tagged to the lesson's blueprint entries in the key.
- Writing task: prompt, evidence bank drawn from the lesson's documents, scaffold, teacher key or rubric.
- Every document: HTML source plus PDF of the same name, page count verified from the PDF. Student documents end at deliberate page boundaries (full page or clean page and a half); a page that dies a quarter of the way down with dead space after it is a defect to fix by adjusting space heights before delivery.
- Decks: 24 to 29 slides. Slide 1 title, slide 2 the lesson question with the unit essential question as a frame line beneath it, slide 3 the lesson in one slide (lettered sections A to G), then sections in guided-notes order with dividers, content slides with 3 to 5 short fragments, at least two giant stat slides, two vocabulary slides carrying the terms (definitions shown short on screen is fine; the NOTES must carry every term AND its full definition string verbatim, including the strict joined "term: definition" form), a closing synthesis slide and an exit slide. Speaker notes on EVERY slide: 120 to 190 words each, floor 90, carrying the full teaching for that slide's content in guided-notes order, top to tail. Count notes words per slide and report the range.
- Images for decks and documents: public domain only. Prefer period maps, engravings, prints, and artifacts from the Library of Congress, the National Archives, the Metropolitan Museum Open Access, Smithsonian Open Access, the British Museum open access, and Wikimedia Commons file pages whose public domain basis you can read and record. Download real files, verify each opens as an image, crop deck images to portrait (about 1046 by 1500) for photo_right and one 16:9 title image, and write img/SOURCES.md per lesson recording title, creator, date, holder, source URL, and public domain basis as shown on the file page. If a download fails or no public domain image exists for a subject, use text and stat slides instead and say so honestly in SOURCES.md. Never invent a catalog number. The Brookes slave ship diagram (1788 abolitionist print) may be used in Lesson 6 only with its exact caption and abolitionist purpose stated. No image of the trade or of violence is used as decoration.
- Sources quoted in documents: verbatim from the named edition, cuts marked with ellipses and disclosed in the Source line. Anything labeled a model or teaching summary must say so on its face.
- Indigenous peoples are historical actors throughout: name nations and leaders where the record names them, state their reasons as the record gives them, and never write them as scenery. Enslavement is written about with documentary sobriety: people first in sentence structure, violence stated plainly and never lingered on.

## Vocabulary (use verbatim everywhere: guided notes, decks, study materials)

### Lesson 1 (blueprint 1, 2)
- Columbian Exchange: the transfer of plants, animals, diseases, people, and ideas between the Eastern and Western Hemispheres that began with the voyages of Columbus in 1492
- Tenochtitlan: the capital of the Aztec empire, built on an island in Lake Texcoco in present-day Mexico, one of the largest cities in the world in 1500
- Cahokia: the largest city of the Mississippian culture, near present-day St. Louis, a center of trade and ceremony known for its great earthen mounds
- Iroquois Confederacy: the league of five, later six, Native nations in present-day New York, joined under the Great Law to keep peace among themselves and deal jointly with outsiders
- caravel: a small, fast sailing ship developed by the Portuguese in the 1400s, able to sail against the wind and suited to long ocean voyages
- Reconquista: the centuries of campaigns by Christian kingdoms to take the Iberian Peninsula from Muslim rulers, completed in 1492, which shaped Spain's ambitions in the Americas
- epidemic: the rapid spread of a disease through a population that has little resistance to it

### Lesson 2 (blueprint 3, 4)
- conquistador: a Spanish military leader who conquered Indigenous peoples in the Americas in the 1500s, seeking land, gold, and glory for Spain and himself
- encomienda: the Spanish system that granted a colonist the right to demand tribute and labor from Indigenous people in a given area, in return for supposed protection and Christian teaching
- mestizo: a person of mixed Spanish and Indigenous ancestry, ranked in the caste order of Spanish America between Spaniards and Indigenous peoples
- New Spain: Spain's viceroyalty in North America and the Caribbean, governed from Mexico City, which at its height stretched from Panama to the present-day American Southwest
- mission: a religious settlement founded by Catholic orders among Indigenous peoples in the Spanish and French colonies to convert them and remake their way of life
- fur trade: the exchange central to French and Dutch colonization, in which Europeans traded manufactured goods to Indigenous hunters for beaver pelts and other furs
- hacienda: a large estate in Spanish America worked by Indigenous or enslaved labor, producing food and goods for nearby towns and mines

### Lesson 3 (blueprint 5, 6)
- joint-stock company: a business owned by investors who pool their money and share its costs, risks, and profits, the form used to fund the first English colonies
- Jamestown: the first permanent English settlement in North America, founded in 1607 on the James River in Virginia by the Virginia Company
- cash crop: a crop grown for sale and profit rather than for the grower's own use, as tobacco was grown in the Chesapeake
- headright system: the Virginia policy that granted fifty acres of land to any person who paid for an immigrant's passage to the colony, used to recruit laborers
- indentured servant: a laborer who agreed to work for a set number of years, usually four to seven, in exchange for passage to America and freedom dues at the end of the term
- House of Burgesses: the first elected assembly in English America, which met at Jamestown in 1619, where landowning colonists chose representatives to make the colony's laws
- Bacon's Rebellion: the Virginia uprising of 1676 led by Nathaniel Bacon, in which frontier settlers and former servants attacked Indigenous peoples and burned Jamestown, pushing great planters toward enslaved labor

### Lesson 4 (blueprint 7, 8)
- Mayflower Compact: the agreement signed aboard the Mayflower in 1620 by the Pilgrims, creating a government by the consent of the governed for the Plymouth colony
- Puritans: English Protestants who sought to purify the Church of England of Catholic practices and built Massachusetts Bay as a model godly society
- covenant: in Puritan belief, a solemn agreement with God that bound a church or a whole community to live by his laws and brought his judgment if they failed
- Anne Hutchinson: the Massachusetts Bay religious dissenter whose teaching that faith alone brought salvation challenged the colony's ministers and led to her trial and banishment in 1637 and 1638
- Roger Williams: the Massachusetts minister banished in 1636 for arguing that the king had no right to grant Indigenous land and that government could not compel worship, who founded Rhode Island on religious toleration
- Fundamental Orders of Connecticut: the document of 1639, often called the first written constitution in English America, that set up Connecticut's government by the votes of its freemen
- Salem witch trials: the crisis of 1692 in Massachusetts in which accusations of witchcraft led to trials that hanged nineteen people and pressed one man to death before the colony repented

### Lesson 5 (blueprint 9, 10)
- middle colonies: the colonies of New York, New Jersey, Pennsylvania, and Delaware, known for fertile soil, busy ports, and peoples of many nations and faiths
- Quakers: members of the Society of Friends, a Protestant group that rejected formal ministers and oaths, held women and men spiritually equal, and faced persecution in England and New England
- William Penn: the Quaker proprietor who received Pennsylvania's charter in 1681 and founded the colony as a holy experiment in government by his persecuted faith
- proprietary colony: a colony granted by the king to an individual or group who owned its land, appointed its governor, and drew its rents and fees
- mercantilism: the economic theory that a nation's power grows by accumulating wealth, especially gold and silver, exporting more than it imports, and holding colonies as sources of raw materials and captive markets
- Navigation Acts: the English laws, beginning in 1651, that required colonial trade to travel in English or colonial ships and required certain colonial goods to be sold only to England
- triangular trade: the pattern of trade across the Atlantic linking Europe, Africa, and the Americas, carrying manufactured goods, enslaved people, and colonial produce between them

### Lesson 6 (blueprint 11, 12)
- Middle Passage: the voyage across the Atlantic that carried enslaved Africans to the Americas, the middle leg of the Atlantic trade, made in crowded ships where disease and abuse killed many of those aboard
- Atlantic slave trade: the forced migration of Africans across the Atlantic in slave ships, which carried some 12.5 million people from Africa between the 1500s and the 1800s, about 10.7 million of whom survived the crossing
- chattel slavery: the system in which enslaved people were legally treated as property, bought, sold, and inherited, and in which their children were born enslaved for life
- slave codes: the laws that defined enslaved people's legal status, denied them rights to courts, assembly, and arms, and punished resistance, tightened in the colonies across the late 1600s and early 1700s
- task system: the labor system of the South Carolina and Georgia lowcountry in which enslaved workers were assigned a daily task and, when it was finished, had the remaining time for their own work
- Stono Rebellion: the uprising of September 1739 near Charleston, South Carolina, in which enslaved Africans seized weapons and marched toward Spanish Florida, after which the colonies tightened their slave codes
- Olaudah Equiano: the African writer who was kidnapped as a boy, enslaved, bought his freedom, and published in 1789 a narrative that described the Middle Passage and argued against the slave trade

### Lesson 7 (blueprint 13, 14)
- salutary neglect: the British practice through much of the early 1700s of leaving the colonies largely to govern themselves while Britain attended to wars and politics in Europe
- Zenger trial: the New York trial of 1735 in which printer John Peter Zenger was acquitted of seditious libel after his lawyer argued that true statements could not be libel, a landmark for freedom of the press
- Great Awakening: the religious revival movement that swept the colonies in the 1730s and 1740s, emphasizing personal faith and emotional preaching over church tradition and learning
- Jonathan Edwards: the Massachusetts minister whose preaching, including the sermon Sinners in the Hands of an Angry God in 1741, helped ignite the Great Awakening in New England
- George Whitefield: the English preacher whose tours of the colonies during the Great Awakening drew open-air crowds in the thousands and made him the colonies' first shared celebrity
- Enlightenment: the European intellectual movement that prized reason, observation, and natural law over tradition and religious authority, reaching the colonies through books, colleges, and print
- revival: a religious meeting or series of meetings meant to reawaken faith and convert sinners, the characteristic gathering of the Great Awakening

### Lesson 8 (blueprint 15)
- French and Indian War: the North American war of 1754 to 1763 between Britain and France and their Indigenous allies, part of the worldwide Seven Years' War, which ended with Britain taking Canada and the French lands east of the Mississippi
- Seven Years' War: the worldwide war of 1756 to 1763 in which Britain and Prussia fought France, Austria, and their allies across Europe, North America, the Caribbean, and Asia
- Albany Plan of Union: Benjamin Franklin's proposal of 1754 that the colonies unite under one government for defense and relations with Indigenous nations, rejected by the colonial assemblies and the Crown
- William Pitt: the British statesman who took direction of the war in 1757, paid for victory with borrowed millions, and sent Britain's army and navy to North America in force
- Treaty of Paris (1763): the treaty of February 1763 that ended the French and Indian War, giving Britain Canada and all French territory east of the Mississippi River except New Orleans
- Pontiac's Rebellion: the uprising of 1763 in which Indigenous nations of the Great Lakes and Ohio Valley, joined under leaders including the Ottawa chief Pontiac, attacked British forts and settlements after the French defeat
- Proclamation of 1763: the royal order of October 1763 forbidding colonial settlement west of the Appalachian Mountains, meant to reserve the land for Indigenous peoples and prevent new frontier wars

## Per-lesson file set (folder colonial-america/lesson-NN/)
lesson-NN-reading.html/.pdf, lesson-NN-guided-notes.html/.pdf, lesson-NN-activity.html/.pdf, lesson-NN-notebook.html/.pdf, lesson-NN-quick-check.html/.pdf, lesson-NN-writing.html/.pdf, lesson-NN-slides.pptx, lesson-NN-teacher-notes.html/.pdf, img/SOURCES.md, slides-build/ (build_deck.py, build_notes_doc.py, headings.json, img/)
