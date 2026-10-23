# The Founding: shared build spec

Unit essential question: Why did the colonies break with Britain, and what did Americans build in the place of the empire they rejected?

Skeleton: ~/workspace/curriculum-planner/the-founding-skeleton.md (read it first; your lesson's section is your assignment).
Model units: ~/workspace/curriculum-planner/colonial-america/ and ~/workspace/curriculum-planner/civil-rights/ — before writing any document type, open the corresponding Colonial America file and mirror its structure, CSS, and conventions exactly. Build PDFs with: python3 ~/workspace/curriculum-planner/templates/build_pdf.py <file.html>
Brandmark (first element in body of every document): <p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>
Deck system: ~/workspace/curriculum-planner/the-founding/deck_common.py (copy of the Colonial America system). Teacher notes builder: copy build_notes_doc.py from a Colonial America lesson's slides-build/ and adapt. Decks keep headings.json in slides-build/.
Audited source texts: the TPSP bank file ~/workspace/primary-source/vite-react-main/public/data/founding.json holds verbatim audited text with the edition named in each record's sourceNote. Quote from those records, with cuts marked by ellipses and the edition named in the Source line. Never quote a period text from memory where a bank record exists, and never quote one at all without a named edition.

## Edition discipline (binding on every document in this unit)
Period texts are public domain, but the edition still matters. Where the bank carries the text, quote the bank record and name the edition its sourceNote names. Where the bank does not carry it (the Stamp Act Congress declaration, the Declaratory Act, Dickinson's Farmer's Letters, the Boston Port Act, the Declaration and Resolves of 1774, the Hewes recollection, the Treaty of Alliance, the Treaty of Paris of 1783, the Northwest Ordinance, the Constitution's Article I, Franklin's closing speech), name the transcription or facsimile edition you actually used in the document's Source line and in the lesson's img/SOURCES.md: the Avalon Project at Yale, the National Archives' Charters of Freedom transcriptions, Founders Online, or a standard scholarly transcription. Spelling stays as the edition carries it; if the edition modernizes spelling, the Source line says so, exactly as the bank records do. Where no verbatim text from a named edition can be verified, write a teaching summary and label it a summary on its face, as the model units do.

## Hard rules (all documents, decks, notes)
- Zero em dashes and zero en dashes anywhere. Zero instances of the construction "that matters" or "that <anything> matters".
- No colon-led paragraph labels in prose, no decorative quotes, no canned transitions, no motivational closers. Ordinary colons in labels, source lines, and times are fine.
- Audience rule: student-facing files are addressed entirely to the student. No product talk, no marketing copy, no grade-band lines anywhere in the documents. Teacher keys carry pedagogy.
- Readings: 850 to 900 words of body text (count by the standard method, words in the reading's section paragraphs; count and report the exact count), five questions, teacher key on its own page at the back with each question restated as a bold lead-in. Reading sections are lettered A to G and match the guided notes sections exactly.
- Guided notes: Name/Date/Period line, lesson question, unit question frame, Key Terms list with the definitions below VERBATIM, lettered sections A to G matching the reading, numbered fill-in blanks, a closing summary table, an exit ticket (3 questions), teacher key with every blank answered. Definitions must match the list below character for character.
- Activity: locked print design from the Colonial America activity (read one first): 5 stations with Source lines and questions with writing space (0.72in), a closing ranking or verdict task with paragraph space (1.9in), teacher key at the back.
- Notebook page: one chart organizer filled from the lesson plus one writing prompt, teacher key with the chart filled in.
- Quick check: short formative, source-based where the lesson allows, every item tagged to the lesson's blueprint entries in the key.
- Writing task: prompt, evidence bank drawn from the lesson's documents, planning questions, scaffold, teacher key or rubric with blueprint tags.
- Every document: HTML source plus PDF of the same name, page count verified from the PDF. Student documents end at deliberate page boundaries (full page or clean page and a half); a page that dies a quarter of the way down with dead space after it is a defect to fix by adjusting space heights before delivery.
- Decks: 24 to 29 slides. Slide 1 title, slide 2 the lesson question with the unit essential question as a frame line beneath it, slide 3 the lesson in one slide (lettered sections A to G), then sections in guided-notes order with dividers, content slides with 3 to 5 short fragments, at least two giant stat slides, two vocabulary slides carrying the terms (definitions shown short on screen is fine; the NOTES must carry every term AND its full definition string verbatim, including the strict joined "term: definition" form), a closing synthesis slide and an exit slide. Speaker notes on EVERY slide: 120 to 190 words each, floor 90, carrying the full teaching for that slide's content in guided-notes order, top to tail. Count notes words per slide and report the range.
- Images for decks and documents: public domain only. Prefer period prints, engravings, maps, broadsides, and artifacts from the Library of Congress, the National Archives, the Metropolitan Museum Open Access, Smithsonian Open Access, and Wikimedia Commons file pages whose public domain basis you can read and record. Download real files, verify each opens as an image, crop deck images to portrait (about 1046 by 1500) for photo_right and one 16:9 title image, and write img/SOURCES.md per lesson recording title, creator, date, holder, source URL, and public domain basis as shown on the file page. Also copy the document images into the lesson's assets/ folder where the HTML documents reference them (the model units keep document images in assets/ and deck images in slides-build/img/, with img/ holding the lesson's SOURCES.md and masters). If a download fails or no public domain image exists for a subject, use text and stat slides instead and say so honestly in SOURCES.md. Never invent a catalog number. Later artists' imaginings are captioned as imaginings wherever they appear, with their dates.
- Sources quoted in documents: verbatim from the named edition, cuts marked with ellipses and disclosed in the Source line. Anything labeled a model or teaching summary must say so on its face.
- The war's peoples are historical actors throughout: name nations, persons, and their reasons as the record gives them. Enslavement is written about with documentary sobriety: people first in sentence structure, violence stated plainly and never lingered on, and no image of violence used as decoration.

## Vocabulary (use verbatim everywhere: guided notes, decks, study materials)

### Lesson 1 (blueprint 1, 2)
- Stamp Act: the British law of 1765 that taxed printed paper in the colonies, including newspapers, legal documents, and playing cards, collected through stamps sold by royal distributors
- repeal: the canceling of a law by the authority that made it, as Parliament canceled the Stamp Act in 1766 under pressure from colonial resistance and British merchants
- Declaratory Act: the British law of 1766, passed the same day as the Stamp Act's repeal, declaring that Parliament had power to make laws for the colonies in all cases whatsoever
- Townshend Acts: the British laws of 1767 that taxed imports into the colonies, including tea, glass, lead, paint, and paper, and used the revenue to pay royal governors and judges
- boycott: a refusal to buy goods or use services as a form of protest, meant to pressure an institution by withdrawing the money and cooperation it depends on
- virtual representation: the British argument that members of Parliament represented all British subjects, including the colonists, whether or not the colonists had voted for them
- Boston Massacre: the clash of March 5, 1770, in which British soldiers fired into a Boston crowd that had surrounded and taunted them, killing five colonists

Note on the boycott definition: it is carried character for character from the Civil Rights unit's spec, where the term is already defined. Do not alter a word of it.

### Lesson 2 (blueprint 3, 4)
- Tea Act: the British law of 1773 that let the East India Company sell tea directly in the colonies at a lower price while keeping the Townshend tax on tea in place
- Boston Tea Party: the protest of December 16, 1773, in which Boston men disguised as Mohawks boarded three tea ships and threw 342 chests of tea into the harbor rather than let it be landed and taxed
- Intolerable Acts: the laws Parliament passed in 1774 to punish Massachusetts for the Tea Party, closing Boston's port and rewriting the colony's charter, which the colonists called Intolerable and Britain called the Coercive Acts
- First Continental Congress: the meeting of delegates from twelve colonies at Philadelphia in the fall of 1774 that answered the Intolerable Acts with a declaration of rights and a boycott of British goods
- minutemen: the Massachusetts militiamen who promised to be ready at a minute's notice, who turned out along the road from Lexington and Concord on April 19, 1775
- Loyalist: a colonist who remained loyal to Britain during the Revolution, whether from conviction, interest, or fear of the rebellion's disorder, and who opposed independence
- Patriot: a colonist who supported resistance to Britain and, from 1776, American independence, and who took the rebellion's side in the war

### Lesson 3 (blueprint 5, 6)
- Common Sense: Thomas Paine's pamphlet of January 1776 that argued in plain language that monarchy itself was corrupt and that America should declare independence and found a republic
- natural rights: the rights held to belong to all people by nature rather than by any government's gift, which the Declaration of Independence names as life, liberty, and the pursuit of happiness
- unalienable rights: rights that cannot be taken away or surrendered, which the Declaration of Independence holds are given to all men by their Creator and stand beyond any government's reach
- consent of the governed: the principle that a government draws its just powers from the agreement of the people it governs, the ground on which the Declaration of Independence rests its case
- social contract: the theory that government rests on an agreement between rulers and ruled, in which the people obey the laws and the government protects their rights, and either side's breach can dissolve the bond
- republic: a state governed by representatives chosen by its citizens under law, without a king or hereditary ruler, the form the American states adopted after independence
- Declaration of Independence: the document adopted by the Continental Congress on July 4, 1776, written chiefly by Thomas Jefferson, that declared the thirteen colonies free and independent states and argued the case from natural rights and the king's abuses

### Lesson 4 (blueprint 7, 8)
- Continental Army: the army created by the Second Continental Congress in June 1775, commanded by George Washington, drawn from all thirteen colonies and enlisted for terms beyond the militia's short service
- militia: the local armed force of a colony or state, made of citizen soldiers who served part time near home and could be called out in emergencies
- George Washington: the Virginia planter and former militia colonel chosen in 1775 to command the Continental Army, whose strategy of keeping the army in being carried the cause through eight years of war to Yorktown
- Valley Forge: the Pennsylvania camp where the Continental Army wintered in 1777 and 1778, enduring hunger and disease while Baron von Steuben drilled it into a professional force
- Battle of Saratoga: the American victory in the fall of 1777 in which a British army under General Burgoyne surrendered in upper New York, the win that persuaded France to ally openly with the United States
- Treaty of Alliance: the treaty of February 1778 by which France recognized American independence and joined the war against Britain, bringing French money, ships, and soldiers to the American cause
- Battle of Yorktown: the last major battle of the war, in the fall of 1781, in which Washington's army and a French fleet trapped General Cornwallis at Yorktown, Virginia, and forced his surrender

### Lesson 5 (blueprint 9, 10)
- Dunmore's Proclamation: the order of November 1775 by Virginia's royal governor, Lord Dunmore, offering freedom to enslaved people and indentured servants held by rebels if they left their masters and bore arms for the king
- inflation: a general rise in prices that shrinks what money can buy, which struck the United States during the war as Congress printed paper money faster than the states could support it
- camp followers: the women and children who traveled with the Continental and British armies, cooking, washing, nursing, and carrying supplies, a workforce the armies depended on and paid little or nothing
- Deborah Sampson: the Massachusetts woman who enlisted in the Continental Army in 1782 disguised as a man named Robert Shurtliff, served more than a year, and was honorably discharged when her sex was discovered
- Joseph Brant: the Mohawk leader, known in his own language as Thayendanegea, who led Haudenosaunee forces allied with Britain during the war and afterward pressed his people's claims to their land
- Sullivan expedition: the American campaign of 1779, ordered by Washington, that burned some forty Seneca and Cayuga towns and their cornfields in answer to frontier raids, driving thousands from their homes
- gradual emancipation: the method by which northern states ended slavery after the Revolution, freeing children born to enslaved mothers only after years of service, so slavery died slowly rather than at once

### Lesson 6 (blueprint 11, 12)
- Articles of Confederation: the first constitution of the United States, adopted by Congress in 1777 and ratified in 1781, which joined the thirteen states in a league that left most power with the states
- confederation: a league of independent states that keep their sovereignty and join for limited common purposes, the form of union the Articles of Confederation created
- requisition: a request by Congress under the Articles of Confederation asking a state to supply money or troops, which the state could lawfully refuse or ignore
- Land Ordinance of 1785: the Confederation Congress's law for surveying the western lands into townships and lots and selling them to raise revenue, which set the grid still visible across the Midwest
- Northwest Ordinance: the Confederation Congress's law of 1787 for governing the territory north of the Ohio River, which barred slavery there and promised its territories statehood on equal terms with the original states
- Shays's Rebellion: the uprising of 1786 and 1787 in western Massachusetts, led in part by the former captain Daniel Shays, in which indebted farmers closed courts to stop foreclosures before the state militia put them down
- Annapolis Convention: the meeting of September 1786, attended by five states, called to discuss trade among the states, which instead called for a convention at Philadelphia to repair the federal government

### Lesson 7 (blueprint 13, 14)
- Constitutional Convention: the meeting at Philadelphia from May to September 1787, called to revise the Articles of Confederation, which instead wrote the Constitution of the United States
- Virginia Plan: the plan proposed at the Convention by Virginia's delegation, drafted chiefly by James Madison, for a strong national government with a legislature apportioned by population
- New Jersey Plan: the plan proposed at the Convention by the small states, which kept a one house legislature with equal votes for every state under a strengthened Articles of Confederation
- Great Compromise: the Convention's settlement, also called the Connecticut Compromise, which apportioned the House of Representatives by population and gave every state two senators in the Senate
- Three-Fifths Compromise: the Convention's settlement that counted each enslaved person as three fifths of a person when apportioning representatives and direct taxes among the states
- federalism: the division of power between a national government and state governments, each supreme in its own sphere, which the Constitution established in place of the Confederation
- separation of powers: the division of the federal government into legislative, executive, and judicial branches, each with its own powers and the means to check the others, so no single branch could rule alone

Note on shared terms owned by earlier units: the Colonial America unit owns definitions for Enlightenment, salutary neglect, and Great Awakening, among others. If your lesson names those ideas in prose, do not re-define them with different wording in any Key Terms list, notes, or study material; name them in text only, or carry the Colonial definition character for character. The same rule binds for any term another built unit defines: search the other units' specs and guided notes before finalizing any definition of your own.

### Lesson 8 (blueprint 15)
- ratification: the formal approval of a proposed constitution or treaty by the body empowered to accept it, which for the Constitution meant conventions in nine of the thirteen states
- Federalists: the supporters of the Constitution in the ratification contests of 1787 and 1788, who argued that the union needed a stronger national government to survive
- Anti-Federalists: the opponents of the Constitution in the ratification contests of 1787 and 1788, who argued that it gave the national government too much power and threatened liberty, above all by omitting a bill of rights
- Federalist Papers: the eighty-five essays written by Alexander Hamilton, James Madison, and John Jay under the name Publius to persuade New York to ratify the Constitution, published in newspapers in 1787 and 1788
- faction: in Madison's argument in Federalist No. 10, a group of citizens united by a passion or interest harmful to the rights of others or to the whole community, whose effects a large republic could control
- Bill of Rights: the first ten amendments to the Constitution, proposed by the First Congress in 1789 and ratified by the states by December 1791, which list rights the federal government may not violate
- amendment: a formal change or addition to a constitution, made for the Constitution of the United States by proposal of two thirds of Congress and ratification by three fourths of the states

## Per-lesson file set (folder the-founding/lesson-NN/)
lesson-NN-reading.html/.pdf, lesson-NN-guided-notes.html/.pdf, lesson-NN-activity.html/.pdf, lesson-NN-notebook.html/.pdf, lesson-NN-quick-check.html/.pdf, lesson-NN-writing.html/.pdf, lesson-NN-slides.pptx, lesson-NN-teacher-notes.html/.pdf, img/SOURCES.md, slides-build/ (build_deck.py, build_notes_doc.py, headings.json, img/)

## Per-lesson source assignments (bank record ids in founding.json)
- Lesson 1 activity stations: Stamp Act Congress Declaration of Rights and Grievances (Avalon Project), Declaratory Act (Avalon Project), Dickinson, Letters from a Farmer (Avalon Project), Preston account + Drowne testimony (bank: preston-case-1770, drowne-testimony-1770), Revere engraving (bank visual: revere-boston-massacre-1770).
- Lesson 2 activity stations: Hewes recollection (named edition, 1834 memoir printing, date stated on its face), Boston Port Act (Avalon Project), Declaration and Resolves of the First Continental Congress (Avalon Project), Barker diary (bank: barker-diary-lexington-1775), minutemen testimony (bank: minutemen-testimony-lexington-1775). Quick check draws on the Lexington records.
- Lesson 3 activity stations: Common Sense (bank: paine-common-sense-1776), Jefferson's rough draft (bank: jefferson-rough-draft-1776), Declaration as adopted (bank: declaration-of-independence), king's Proclamation of Rebellion (bank: king-proclamation-rebellion-1775), Olive Branch Petition (bank: olive-branch-petition-1775).
- Lesson 4 activity stations: Address of Congress to the Inhabitants (bank: address-congress-inhabitants-1778), Treaty of Alliance (Avalon Project), Valley Forge record (named edition or labeled teaching summary), southern campaign record (named edition or labeled teaching summary), Treaty of Paris 1783 (Avalon Project).
- Lesson 5 activity stations: Dunmore's Proclamation (bank: dunmore-proclamation-1775), Abigail Adams letter (bank: abigail-adams-remember-the-ladies), freedom petition (named transcription or labeled summary), Deborah Sampson record (labeled teaching summary from the public record), Sullivan expedition and Haudenosaunee record (named edition or labeled summary).
- Lesson 6 activity stations: Articles of Confederation (bank: articles-of-confederation-1777), Northwest Ordinance (Avalon Project), Virginia Statute for Religious Freedom (bank: virginia-statute-religious-freedom-1786), Washington to Mercer (bank: washington-mercer-slavery-1786), Shays's Rebellion (labeled teaching summary).
- Lesson 7 activity stations: Preamble (bank: constitution-preamble), Madison's Notes, September 17 (bank: madison-notes-debates-1787), Washington's annotated draft (bank visual/document: washington-annotated-draft-constitution-1787), Article I three-fifths clause (National Archives Charters of Freedom transcription), Franklin's closing speech (Avalon Project text of Madison's Notes).
- Lesson 8 activity stations: Federalist No. 10 (bank: federalist-10), Brutus No. 1 (bank: brutus-no-1-1787), Federalist No. 51 (bank: federalist-51), Looking Glass for 1787 (bank visual: looking-glass-1787), Bill of Rights (bank: bill-of-rights).
