# Planner v1 — the concrete choices

The pilot unit gives the planner its data on day one. Every finished item in `progressive-era/unit-manifest.md` is tagged to the 15-entry test blueprint, and the unit test key carries the full coverage table. The planner does not need new content to start. It needs a reader for the manifest and the six steps from the concept doc.

## What v1 proves

The smallest thing that shows the differentiator working, on the Progressive Era unit only:

1. The teacher enters start and end dates for the unit plus the test date.
2. The planner proposes a pacing timeline from the blueprint weights, with the test auto-landing at the end.
3. The teacher picks assignments from the unit's plate into the calendar.
4. The coverage indicator shows, live, which blueprint entries are taught by the picks and names the gaps, with one-click suggestions that fill them.

That is the whole demo. Everything else in the concept (full-year scope and sequence, state exam dates, drag-to-rebalance, exports) waits for v2.

## The choices

**1. Build vehicle.** A single-page interactive prototype that runs the four steps above on the pilot unit, or the full site scaffold now. My recommendation is the prototype. It is the same logic you applied to the content: prove the loop on one unit before committing to the engine. The prototype can live as a static page, no backend.

**2. Saving.** v1 does not need teacher accounts. The prototype keeps the calendar in the browser (the same local-first pattern Rycal uses for guests). Accounts come when the planner becomes the product, not before.

**3. Scope.** Planner demo covers the Progressive Era unit only. Its plate is complete: readings, guided notes, activities, notebook pages, quick checks, writing tasks, review, and the tagged test. TPSP-held items (source analyses, photo stations) are linked in the manifest, so the planner can reference them without rebuilding them.

**4. Sequencing.** Planner prototype now, or unit 2 content first. The tradeoff is real: the prototype is what you would show a teacher, but unit 2 is what makes the site a course. My read is that the prototype comes first because it answers the only open product question, whether the coverage indicator feels right in a teacher's hands. But if your instinct is content momentum, say so.

**5. Product name.** The name gates the domain and the site build. It does not gate the prototype. When you are ready, the name sits under Knoweth and should signal the planner, since that is the thing neither competitor has.

## What I build first

Once you pick the vehicle: the pacing proposal and the plate picker with the live coverage meter, reading the manifest as-is. No content changes needed. The open questions from the concept (block schedules, exports, standards tagging) stay parked for v2.
