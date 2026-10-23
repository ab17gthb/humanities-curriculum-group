# Knoweth Curriculum: Design Template
Set by Lesson 1 (Progressive Era), October 20, 2026. Every resource in every unit follows this standard unless Alex changes it.

## Visual system (print-first; Alex's correction, Oct 20, 2026)
- Teachers print these materials, so the design is simple on purpose. White pages, black or near-black text, generous margins and line space for writing. Anything that works on screen must also work on a school copier.
- No filled color blocks, no shaded tables, no background panels. A full-bleed or solid-fill element does not ship.
- Color appears only as text and thin rules, which cost almost no ink and survive grayscale copying: navy #1B2A4A for titles and headings, rust #B5502F for kickers, labels, and rules, ink #23272E body text, gray #5A616D for captions.
- Fonts: Georgia for titles and headings, Arial for body. Both ship with Office and Google Workspace, so files render identically for buyers.
- Slides (Alex's model, set Oct 20, 2026 from his "Capital and Labor" deck, https://docs.google.com/presentation/d/1taJ7YXQ1Oh5mkTJxn6x0AZLhuNyxGTkTgcFDh4N3y8g): image-led, one idea per slide. Nearly every slide carries a large public-domain photo or cartoon; section dividers are a big image with a short label and a one-line caption. Content slides are a large Gill Sans title plus three to five short phrase fragments, not full sentences; the teaching detail lives in the guided notes, not on the slide. Key statistics get a giant statement slide (oversized number, one line). No header bands, footers, slide numbers, objectives slides, or key-terms boxes in the deck. 16:9, white background, navy titles. Speaker notes carry the comprehensive teaching (Alex, Oct 20, 2026: full lesson and vocabulary top to tail, never highlights only). Every deck also ships a printable teacher notes document (lesson-NN-teacher-notes, HTML source + PDF) generated from the deck's speaker notes: one headed section per slide, with a short "On the slide" locator line, so teachers can print the notes and teach from paper (added Oct 21, 2026 at Alex's request after he approved the Lesson 1 test deck; builder: slides-build/build_notes_doc.py).
- Documents: no cover block. Page 1 opens with Name / Date / Period spread across a single top line, then the document title in black, then directions. All text black, including headings; teacher keys print in bold, not color. No ruled lines for answers anywhere: questions and prompts get open blank space to write in. Fill-in blanks inside guided-notes sentences are the only underscores allowed. (Reading format approved by Alex, Oct 20, 2026.)
- Build and delivery format (Alex, Oct 20, 2026): build documents in HTML and deliver as PDF. Not Google Docs, not Word; the Word render looked bad to him twice. HTML gives exact control over spacing, image placement, and page breaks, and the PDF prints identically anywhere. Keep the HTML source alongside the PDF as the working copy.
- Branding (Alex, Oct 20, 2026; REVISED twice same evening, superseding the no-logo call and then the multi-variant set): ONE brand mark only, the Humanities Curriculum Group wordmark (master: ~/workspace/curriculum-planner/assets/hcg-logo/hcg-wordmark.svg). Alex's words: "too many different hcg branding things. Stick with just the words." The badge and monogram variants are retired from use everywhere (files stay in assets/hcg-logo-store/ but do not ship). On documents (REVISED Oct 21, 2026 at Alex's direction, superseding the end-of-section placement): black wordmark, 1.35in wide, at the very top of page 1 in the upper left corner (the .brandmark element, first thing in the body, above the name line), and nowhere else; there is no closing credit at the end of the document. The @page top margin is 0.55in (bottom stays 0.7in) so the mark does not push page 1 content down. Nothing else: no badge, no footer. On the website and store: the same wordmark, cream on navy for dark headers, navy and rust on light backgrounds. His supplied Crossroads badge and the drawn X logo (~/workspace/curriculum-planner/assets/) stay on file for other uses.

## Activity design (approved by Alex, Oct 20, 2026; reference build: Lesson 1 Reformer's Notebook)
The exact spec, so every worksheet activity in the line matches. Master files: starter HTML at ~/workspace/curriculum-planner/templates/activity-template.html; generic PDF builder at ~/workspace/curriculum-planner/templates/build_pdf.py (inlines local images, prints via headless Chromium). The lesson-01 build script is the reference implementation.

- Page: US Letter, margins 0.55in top / 0.7in bottom, 0.75in sides. Arial/Helvetica throughout, all black. Body 11.5pt, line height 1.35. Title (H1) 19pt, part headings (H2) 14.5pt, station headings (H3) 12.5pt.
- Page 1: name line first (Name / Date / Period spread across one line), then the title, then a directions paragraph. No logo or wordmark on page 1; the only brand element in the document is the closing wordmark (see the last bullet of this section).
- Station pattern: H3 "Station N: Title," a "Source:" line, the source image centered (max 3.9in wide, 2.3in tall) with a 9pt italic caption, the source text or labeled summary, then each question followed by 0.72in of blank writing space.
- Closing section: a ranking or verdict task, then a prompt with 1.9in of blank paragraph space.
- Brand mark: the Humanities Curriculum Group wordmark (hcg-wordmark.svg), 1.35in wide, upper left at the very top of page 1 (the .brandmark element, before the name line). No closing credit and no other branding (rule revised Oct 21, 2026).
- Teacher key: starts on its own page; each answer in body text with the question restated as a bold lead-in; a rubric as a short bullet list where the task needs one.
- Pagination check before delivery: no station heading stranded at a page bottom, no figure split across pages, and no page that is only writing space. Tighten image height caps and space heights before adding pages.

## The plate (every lesson, same ten types)
1. Core lesson: slide deck + guided notes keyed to it, blanks numbered to match the teacher key.
2. Reading: 750 to 900 words, textbook register, subheadings, five questions (comprehension through argument), teacher key.
3. Source analysis: drawn from the TPSP audited bank wherever possible; sources carry the TPSP citation standard.
4. Stations or jigsaw activity.
5. Notebook page: a single organizer students keep.
6. Activity: simulation, debate, role play, or structured game.
7. Quick check: short formative, photo- or source-based where possible.
8. Writing task: paragraph or essay with a scaffold.
9. Review: game or structured review for the unit test.
10. Assessment: drawn from the unit test bank, tagged to the unit blueprint.

## Content standards
- Every test and quick-check item is tagged to the unit test blueprint at build time. Coverage checking in the planner depends on this; untagged items do not ship.
- Facts are stated at the precision the evidence supports. Contemporary estimates are labeled as estimates.
- Prose register: direct, teacher-to-student, formal academic. No em dashes in student-facing text. No decorative quotes, no canned transitions, no motivational closers.
- Teacher keys are part of every file that needs one, on separate pages at the back, with each question restated as a bold lead-in.
- History content follows the TPSP audit posture for anything quoted: verbatim against a named edition, cuts marked.

## Build and file conventions
- One folder per lesson: curriculum-planner/<unit>/lesson-NN/, files named lesson-NN-<plate-type> (slides .pptx; documents kept as .html source with a .pdf deliverable of the same name).
- Build scripts live in <unit>/build-scripts/ so the template is reproducible, not hand-copied.
- No resource is final until Alex has approved the lesson template once; after that, later lessons follow the template without per-piece approval, and he reviews the unit as a whole.
