# Course Review integration checklist (phase 4)

Started 2026-10-23. Content complete: 8 band days, 3 study guides,
3 crosswords, 3 practice tests (all in course-review/).

1. [x] planner-data.js: HCG_RV/RE/RM BLUEPRINT, TOPICS, BP_TOPIC, LESSONS,
       ITEMS, TPSP globals + registry entries (rv u15, re u16, rm u17).
       Spans aligned to the units' printed topicsHeads (registry-draft
       spans superseded where they differ: entries 8, 9, 10, 11, 12, 14).
       TPSP picker per variant = the premium DBQs (dbq:true) from the
       variant's units, bp retagged to the variant's entry for the home
       unit. Item copies per variant with variant prefixes (rv1-, re1-,
       rm1- ...). Core checks: packet days sum + flex + test = 10/5/7.
2. [x] Unit pages course-review.html, early-review.html, modern-review.html
       on the modern-america.html pattern (no deck extras; review pages
       carry a "no new decks" note per the plan's scope line), covers and
       previews in assets/, us-history.html cards, sitemap.xml entries.
3. [x] Storage: upload-review-storage.py on the upload-*-storage.py
       pattern; band PDFs + closing pieces under the three prefixes;
       MD5 verification per object.
4. [x] year-planner.js: rv joins the full shape last; re joins the
       to-1877 shape last; rm joins the from-1877 shape last. Reconcile
       the review-days reserve so scheduling a review unit does not also
       reserve blank review days on top of it.
5. [x] Rycal: three merged starter decks (336/504/840 cards) from the
       staging JSON, published like the 15 unit decks, landing pages
       /hcg-early-review-flashcards, /hcg-modern-review-flashcards,
       /hcg-course-review-flashcards; registry rycalDeck fields point
       at them; unit pages carry the standard vocab block.
6. [x] Suite: tests/test_phase18_review.py on the phase-17 pattern;
       full suite run (992 + new) green before deploy.
7. [x] Deploy (hosting) + live verification: MD5 of planner-data.js and
       the three pages, storage spot-check through an entitled session,
       Rycal deck pages live.
8. [x] Manifests + memory updated; Alex told the naming question
       (Course Review vs Course Review and Exam Prep) is still open
       and currently shipping as "Course Review".
