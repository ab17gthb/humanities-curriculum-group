# Humanities Curriculum Group

The full working tree for Humanities Curriculum Group (HCG), the US History curriculum published under Knoweth at https://humanitiescurriculumgroup.web.app

## What is here

- `site/` — the live website: static pages, the year and unit planner (`site/public/planner-data.js`, `planner.js`), Firebase config, Cloud Functions (`site/functions/`), ops runbooks (`site/ops/`), and the Playwright test suites (`site/tests/`).
- One folder per teaching unit (`colonial-america/` through `modern-america/`): HTML masters for every document (reading, guided notes, activity, notebook page, quick check, writing task, teacher notes), the review set, and the unit test, plus the source images each document uses. PDFs are rendered from the HTML masters with `templates/build_pdf.py`.
- `course-review/` — the three review variants (full course, early to 1877, modern from 1877): band packets, study guides, crosswords, and practice tests.
- `templates/` — the print template standard (`TEMPLATE.md`) and the PDF build script.
- `covers/` — cover and preview art. `assets/` — brand assets and logos.
- `reading-key-audit.md` — the 2026-10-23 audit log: every question in the course checked against the rule that an answer key may not assert a fact the student's own material does not support.

## Working notes

- HTML is the master format. Fix the HTML, rebuild the PDF, then upload. Paid-unit PDFs serve from Firebase Storage under `hcg/<unit-slug>/`; Progressive Era (the free unit) serves from `site/public/files/`.
- Deploy the site from `site/` with `firebase deploy --project cue-bb34b`, and confirm the deploy log ends with "Deploy complete!" before trusting it.
- Print standard: white pages, black text, no filled blocks or shaded tables, color only as text and thin rules. Student-facing files speak only to students; selling copy lives in listings, never in documents.

`node_modules/`, Python caches, and run logs are excluded from this repo (see `.gitignore`).
