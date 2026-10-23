# Course Review: registry draft

Draft for the phase-3 integration (not yet in planner-data.js). Three
registry units share the eight band days, per Alex's 2026-10-23 direction:

- Combined: registry "rv", courseId "u15", key "hcg_unit_rv_v1", storage
  hcg/course-review/, page /course-review, name "Course Review". Blueprint:
  all fifteen entries. Core 10 days, Fit-to-year minimum 7 (six bands plus
  the test).
- Early: registry "re", key "hcg_unit_re_v1", storage hcg/early-review/,
  page /early-review, name "Early Course Review". Blueprint: entries 1 to
  6. Bands 1 to 3. Core 5 days (three band days, flex, test), minimum 4.
- Modern: registry "rm", key "hcg_unit_rm_v1", storage hcg/modern-review/,
  page /modern-review, name "Modern Course Review". Blueprint: entries 7
  to 15. Bands 4 to 8. Core 7 days (five band days, flex, test), minimum 5.

Band items are defined once per band (the rX- items below, renumbered per
variant at integration so each variant's registry references its own item
copies with its own blueprint tags). Naming decision still open for the
combined page: "Course Review" or "Course Review and Exam Prep".

## Blueprint (15 entries, one per teaching unit)

1. Colonial America, 1491–1763
2. The Founding, 1763–1791
3. Early Republic and Expansion, 1789–1848
4. Jackson and Reform, 1828–1848
5. Sectional Crisis and Civil War, 1850–1865
6. Reconstruction, 1865–1877
7. The Gilded Age, 1877–1900
8. Progressive Era, 1900–1920
9. Imperialism and World War I, 1898–1919
10. The Twenties, 1919–1929
11. Depression and New Deal, 1929–1941
12. World War II, 1941–1945
13. The Cold War, 1945–1991
14. Civil Rights, 1954–1968
15. Modern America, 1978–present

Spans to be aligned to each unit's printed topicsHead at integration; the
five confirmed against the live registry during planning are entries 1, 7,
and 15, and the unit scopes confirm 3, 4, 5, and 6.

## Topics (6, the course's threads)

1. Federal power and the Constitution
2. Expansion and its costs
3. Slavery, race, and rights
4. Industrial capitalism and labor
5. America in the world
6. Reform movements

## Bands

1. Colonies and the Founding: entries 1, 2. Skill: chronology.
2. A Working Republic and Its Discontents: entries 3, 4. Skill: comparison.
3. Slavery, War, and the Unfinished Settlement: entries 5, 6. Skill:
   causation. TEMPLATE BUILT 2026-10-23 (band-3/).
4. Industry and Reform: entries 7, 8. Skill: continuity and change.
5. Power Abroad, Turmoil at Home: entries 9, 10. Skill: comparison.
6. Depression, Recovery, and Total War: entries 11, 12. Skill: causation.
7. Cold War Abroad, Rights at Home: entries 13, 14. Skill: continuity and
   change.
8. Modern America and the Long Arc: entry 15 plus cross-era threads.
   Skill: documents.

## Item model (per band, from the Band 3 template)

- rX-packet, kind "Packet", days 1, core, tags [band's two entries]: the
  day's anchor document; the sprint, practice set, and skills task anchor
  to it at days 0, the way guided notes anchor to a lesson.
- rX-sprint, kind "Term Sprint", days 0, core, tags as above.
- rX-practice, kind "Practice Set", days 0, core, tags as above.
- rX-skills, kind "Skills Task", days 0, tags as above (not core, so a
  compressed review can drop the essay before it drops questions).

## Closing items (unit level)

- rev-guide, kind "Study Guide", days 0: the variant's study guide;
  planned for the flex day beside the crossword.
- rev-cross, kind "Crossword", days 0: four answers per unit in the
  variant (early 24, modern 36, combined 60).
- The practice test is the variant's unit test (testStorage under the
  variant's own prefix), 50 points, every entry in the variant's blueprint
  assessed at least twice recomputed from its printed tags, landing on the
  last day of the variant's core plan.

Core plans and Fit-to-year minimums are stated per variant above. The
combined review's core minimum keeps six of its eight bands (1, 3, 4, 6,
7, 8) plus the test.
