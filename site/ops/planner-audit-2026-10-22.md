# Planner Audit — Humanities Curriculum Group

**Date:** Thursday, October 22, 2026
**Scope:** Year planner (`planner-year.html`), unit planner (`planner.html`), teacher home (`home.html`), and the entry points into them (unit pages, homepage planner section). Audit only; no code, content, or data was changed.
**Method:** The site was served locally from `site/public/` and driven with Playwright (fs venv, headless Chromium) at 1440px desktop and 390px phone widths, signed out, with fresh browser contexts for cold starts. Every finding below comes from doing the teacher's job on the page: setting up a year, picking and cutting assignments, creating and fixing a coverage gap, pinning, splitting, marking a snow day, squeezing a test date, exporting, sharing, importing, printing, and returning cold. Print quality was judged by rendering the exact HTML the Print plan / Sub plan buttons generate. Where a claim rests on source reading rather than interaction (save-state text, import error handling), the file and line behavior are named.

**Limitations, stated plainly:** sign-in itself was not exercised with a real account in this pass, so signed-in behavior is assessed from the auth code paths and the menu strings they produce. Drag-and-drop uses standard HTML5 DnD; synthetic drag events in headless Chromium did not move a chip, so drag is assessed from the code and from the absence of any alternative control, not from a successful synthetic drag.

**Overall verdict:** The planner engine is genuinely strong — the coverage gap loop, the instant reflow around days off, the A/B and block math, and the sub plan are better than anything in the obvious comparison set. The weaknesses concentrate in three places: the first five minutes (a first-time teacher meets an example year presented as their own and a year that is already 92 days overcommitted), the integrity of outputs when a plan is in trouble (overflow quietly corrupts the last day, and prints and calendar exports hide the damage), and the mobile feedback loop. None of these needs a rebuild. All of them are fixable in place.

Grades: **P0** hurts first-run success or trust. **P1** recurring friction a teacher hits weekly. **P2** polish. Effort: S (under a day), M (a few days), L (a week-plus or a design decision first).

---

## Job 1 — First run: land cold, set up a school year

### P0 — The default year is already overcommitted, and the page never says by how much in plain terms
On a cold load the totals panel reads: Instructional days 178 · Held for exam review 0 · Committed to units 178 · Buffer left 0 · **"92 days of units do not fit in this year."** Five of the fifteen units (Depression and New Deal, World War II, The Cold War, Civil Rights, Modern America) are labeled "does not fit" before the teacher has touched anything. The arithmetic a teacher actually needs — units ask for **270 lesson-days**, the year offers **178** — appears nowhere; "Committed to units 178" is the capped figure, so the two numbers on the page (178 committed, 92 unfitted) have to be added mentally to learn the demand. A first-time teacher's first result on the flagship tool is a red failure state for a year they did not design.
**Fix:** (a) State demand vs supply in one line in Year totals: "Your units ask for 270 lesson-days; your year has 178." (b) Ship a default that fits: either trim the default estimates to a realistic spread, or default the course shape to one of the two-part shapes with a note that the full survey at full length needs a longer year or trimmed units. (c) Pair with the "Fit to year" action in Job 3. **Effort: M.**

### P0 — An example year is presented as the teacher's own year, everywhere
The cold year planner arrives pre-filled: Aug 24, 2026 – May 28, 2027, four quarters, seven days off (two literally labeled "(example)"). The panels call it "Your year" and "My year plan." Only the days-off panel admits these are examples. The teacher home then treats this seeded data as real (see Job 5), announcing a unit the teacher never chose. Nothing on either page says "starter year — replace with yours."
**Fix:** A first-run banner on the year planner ("This is a starter year with typical US dates and holidays. Set your first and last day and delete any days off that are not yours; everything reflows."), dismissed permanently after the first edit to a date field, and a matching "starter" flag honored by teacher home until the year is edited. **Effort: M.**

### P1 — The explainer load lands before any success
The year page asks a new teacher to absorb two long small-print paragraphs (lesson-days math; the three course shapes) plus panel intros before doing anything. "Lesson-days" is the system's key unit and it is defined only inside that paragraph. The unit planner's intro is likewise a nine-line paragraph covering five features at once.
**Fix:** Cut both intros to two lines and move the math into a "How the counts work" disclosure; put the definition where the number is ("18 lesson-days ≈ 18 class periods" as the first unit row's caption). **Effort: S.**

### P2 — Small copy and ordering nits
- The course select's first option reads "Full survey · founding to modern day," but the survey starts with Colonial America. (S)
- The unit switcher on `planner.html` lists units in build order (Progressive Era, Gilded Age, …, Modern America, then Colonial America … Reconstruction), not course order. The year planner's table is in course order, so the two pages disagree about the course's shape, and a teacher scanning the pills for Reconstruction finds it last. Order the switcher by course position and keep Progressive Era flagged as the sample. (S)
- Credit where due: the unit planner's cold state is a first-run *success* — sensible default dates, core picks pre-checked, 15 of 15 covered, a full schedule on screen immediately. The year planner should borrow that pattern.

---

## Job 2 — Plan a unit: pick, reorder, pin, split, fix coverage

### Strength to keep — the coverage gap loop
Cutting all three Lesson 8 items dropped coverage to 14 of 15 and the panel answered with exactly what a teacher needs: **"Not covered yet — Entry 14 · Progressivism and race. Fills it: The Limits of Progressivism (Lesson 8)"** with an Add button; one click restored 15 of 15. This is the best single interaction in the system. The findings below are about everything around it.

### P1 — The picker never shows what an item covers
Picker rows show kind, name, a PDF link, a Split button, and a day cost — but not the blueprint entries the item teaches. Tags become visible only after a gap exists, and the gap panel suggests only the *first* unpicked item that fills it. A teacher who cut that item on purpose (too long, wrong reading level) has no on-screen way to find an alternative covering item short of re-checking items and watching the meter.
**Fix:** Show coverage on the row (small "covers 14 · 15" text or tag chips on expand), and in the gap panel list *all* unpicked items that fill the entry, each with its own Add button. **Effort: M.**

### P1 — Coverage counts picks, not what is actually scheduled
With the test date squeezed to four usable days, thirteen items overflowed — and the coverage panel still read "15 of 15 blueprint entries covered" over a green "Every blueprint entry is covered by at least one of your picks," while a separate line said "Your picks fill 4 of 4 usable meeting days." Both statements are technically about picks; together they tell a teacher in trouble that coverage is complete when half the unit never reaches a day. Coverage that ignores the calendar overstates readiness exactly when the plan is failing.
**Fix:** When overflow is non-empty, add a second coverage line computed from *placed* items ("Scheduled before the test: 9 of 15 entries") and let the meter show the placed figure until the overflow clears. **Effort: M.**

### P1 — The two coverage lenses contradict each other without labeling
Cold state: "15 of 15 blueprint entries covered" beside "Your picks touch 5 of the 6 topics." Topic 4 (The West and Native Americans) is structurally impossible in this unit — the panel itself notes "Not part of this unit" — yet it sits in the 5-of-6 denominator, so a perfect unit permanently reads as one short. After cutting Lesson 8, Topic 5 flagged "Not covered by your current picks" with no suggested fix, while the parallel blueprint gap had an Add button. A teacher cannot tell which lens is the score and which is context, nor which gaps are fixable inside the unit.
**Fix:** Count only topics the unit can teach in the denominator; retitle the panel's summary line "For reference — the blueprint check above is the score"; where a topic gap *is* fixable in-unit, name the fixing pick the way the blueprint panel does. **Effort: S–M.**

### P2 — Picker density and unexplained controls
- A "Split" button repeats on every one-day row (~20 per unit) and the word is never explained in the picker; its only explanation sits in the schedule section's intro paragraph, below the picker. Add one clause to the picker intro ("Split divides a one-day item into two half days that can pair with other halves") and consider moving the button into a row menu. (S)
- No lesson collapse, no "hide unchecked," no search on a 35–51-item plate. The TPSP picker (below the plate) *has* search; the plate itself should get collapse-by-lesson at minimum. (M)
- Adding your own resource asks for name, days, link, note, and then a coverage decision across 15 blueprint checkboxes — honest, but a steep toll next to the one-click plate items, and self-tagged coverage is marked only by a † footnote in the results. Pre-suggest tags from the lesson the item lands in, with "tag later" allowed. (S)

### P2 — Block-period status wording
At 90 minutes the day-use line reads: "Your picks fill 9 of 19 usable meetings for Period 1: 18 lesson-days · 9 meetings, with the test day counted in the lesson-days." Accurate, and nearly unreadable. Split into two short lines (meetings used; lesson-days used). (S)

---

## Job 3 — Adjust reality: snow days, estimates, pins, overflow

### P0 — When picks overflow, their guided notes pile onto the last day and lie about it
Reproduced twice. Squeeze the Progressive Era test to a 10-teaching-day window and the final day (Fri, Nov 6 in the test run; Thu, Oct 29 in the print run) shows **"Campaign poster or speech" plus the guided notes for Lessons 6, 7, and 8** — while those lessons' readings are unscheduled entirely. The overflow message names 7 spilled items and never mentions any guided notes (zero-day "same day" items are excluded from the overflow list by construction, so the layout engine parks them on the last bucket). On screen this reads as a bizarre but plausible day; on paper (Job 4) it is worse. A teacher behind schedule — the exact user of the overflow path — gets a day plan that is quietly wrong.
**Fix:** In the layout engine, a zero-day rider whose parent item is unplaced must overflow with it (and be named in the overflow note as "and their guided notes"). Add a regression test to the phase suite: squeeze a unit, assert no orphaned notes on the final day and that the overflow text names them. **Effort: S–M.**

### P1 — No "make it fit" help anywhere
The system's answer to a 92-day overcommit is a warning sentence ("Trim day counts, drop days off that do not apply, or move the last day later") and fifteen number inputs. There is no proportional trim, no per-unit floor to guide cuts (each unit's count from core picks exists — the year table even shows "default from core picks" for Progressive Era — but never as a "don't go below" reference), and no computed suggestion ("teaching to 1877 only would fit with 12 days to spare").
**Fix:** A "Fit to year" action: scales all estimates toward the available days, never below each unit's core-picks count, shows the result before applying, and says what it changed. Show each unit's core minimum beside its estimate input permanently. **Effort: M–L.**

### P1 — Pinning and day-marking collide silently
Pinning Lesson 1 to Mon, Oct 26 and then marking Oct 26 "No class" moved the pinned item to Oct 27 with only a small parenthetical: "(pinned to Mon, Oct 26, not a meeting day)." No warning appears when the day is marked. The behavior (float the pin) is defensible; the silence is not — the teacher's one deliberate act of fixing something to a date was undone by a different control with no notice at the point of action.
**Fix:** When a day holding a pin is marked, say so in the row as it happens ("This day held a pinned item; it moved to Tue, Oct 27") and consider listing floated pins in the overflow note area until acknowledged. **Effort: S.**

### P1 — Nothing warns that units are scheduled after the exam
With the exam set to Fri, May 7, 2027 and five review days held (the reserve renders correctly — shaded days labeled "review," the exam ringed in rust), the plan still runs Imperialism and World War I's test on May 13 and The Twenties through May 28, with no flag anywhere that three units land after the test the year is aimed at. For an AP or state-test teacher this is the most valuable warning the year planner does not give.
**Fix:** When an exam date is set, flag any unit whose band crosses or follows it in the unit list and totals ("2 units are scheduled after your May 7 exam — by design, or move the exam?"). **Effort: S.**

### P2 — A test date on a non-meeting day is accepted without a nudge
Setting the unit test to Sunday, Nov 8 placed "Unit test" on a Sunday with no comment. Teachers do pick dates by misclick; one line ("Nov 8 is a Sunday; the test will sit on the date you picked") costs nothing. **Effort: S.**

### Strengths to keep
Snow-day handling is exemplary: one added day off cut instructional days 178 → 177, re-dated every unit, and adjusted committed days, instantly and consistently. Estimate edits reflow the whole year the same way. A/B totals show meetings and lesson-days side by side ("Days this course meets (A/B rotation) 89 · Meetings used 89"), the clearest presentation of that math in the product.

---

## Job 4 — Use the outputs

### P0 — The printed plan and sub plan inherit the overflow corruption, with no warning on the paper
Rendered exactly as the buttons generate them: in the squeezed unit, the print plan's final day lists four guided-notes sets and none of their readings, and the sub plan does the same. Neither document carries any line like "3 items did not fit before the test and are not shown." The sub plan is the one artifact guaranteed to be read by someone who cannot ask the teacher what happened.
**Fix:** Fix the engine defect (Job 3, P0) and, independent of it, print an unplaced-items banner on any plan or sub plan with overflow, listing what is missing. A plan with problems should say so on its face. **Effort: M (banner S once the engine reports unplaced items cleanly).**

### P0 — The year calendar (.ics) export silently drops every unit that does not fit
With the default (overcommitted) year and an exam set, the exported file held **21 events**: begins + unit test for the ten units that fit, plus one "exam day." The five unfitted units — a third of the course — are absent with no event, no note in the file, and no message at export time. A teacher importing this believes the whole course is on their calendar.
**Fix:** At export, if any unit does not fit, say so before the download ("Depression and New Deal, World War II, The Cold War, Civil Rights, and Modern America do not fit and will not be in this file") and include the exam's review block as events or state that it is excluded too. Never let an export be silently partial. **Effort: S.**

### P1 — The two share links behave differently, and the unit one explains nothing
Year planner: the button copies the link and confirms, "Share link copied. Whoever opens it gets this year plan loaded as its own plan in their browser; nothing is uploaded." Unit planner: the button prints the raw base64 URL into the page — "Copy this link: http://…/planner.html#plan=eyJ2Ijo0…" — for the teacher to select by hand, with no sentence about what the recipient gets. Same product, same gesture, two standards; the worse one is on the page teachers share most.
**Fix:** Give the unit share the year pattern verbatim (copy to clipboard, the same explanatory sentence, the URL in a readonly field as fallback). While there, let the recipient banner name what arrived ("A shared plan was loaded: Progressive Era, Period 1, Oct 26 – Nov 20") — the payload knows all three. **Effort: S.**

### P1 — Home day blocks dead-end when the unit has no day-by-day plan
See Job 5, P1 (teacher home). The output-side fix is a "Plan this unit day by day" link inside the day block whenever the band's unit lacks a unit plan.

### Strengths to keep
The sub plan's prose is genuinely substitute-proof: the date range, "Every material is a PDF named below," and per-day items with lesson, kind, and filename. The unit .ics summaries are clean ("Progressive Era (Period 1): The Problems Progressives Faced + Lesson 1 guided notes"). Teacher home's print CSS is properly paper-adapted (black borders, no color dependence, blocks kept whole). The print plan's table itself — date, items, test bolded — is exactly right when the plan fits.

---

## Job 5 — Return visit: saving, sync, and the free/paid boundary

### P1 — The save story contradicts itself for signed-in users
Both planner intros state, as static copy: your work "saves in this browser…; nothing is uploaded." For a signed-in teacher that is false — plans sync to the account (the account menu reports "Synced Oct 22, 2026, 6:19 PM"). Meanwhile the year planner's own saved line hardcodes "Saved in this browser · 12:47 AM" (written verbatim by its save function) regardless of sign-in, so a signed-in teacher gets two different answers on the same screen, and a signed-out teacher never sees, at the point of work, the one sentence that matters: "Sign in and this follows you to any computer."
**Fix:** One auth-aware status line in both planners, driven by the same sync state the account menu uses: signed out — "Saved in this browser · 12:47 PM — sign in to sync across devices"; signed in — "Saved and synced to your account · 12:47 PM." Delete "nothing is uploaded" from the intros or gate it to the signed-out state. **Effort: S.**

### P1 — Teacher home presents the seeded example as today's teaching
Truly cold, home shows the correct pitch ("No plan here yet…"). But merely opening the year planner once writes the default plan, and home then renders Today as **"Early Republic and Expansion"** — the default band for the date — with no materials, no indication this is starter data, and no link to do anything about it. The footer even certifies it: "Drawn from your year plan and your Progressive Era unit plan (Period 1)."
**Fix:** Two parts. (a) Until the year plan's dates are edited, home labels the source ("from your starter year — set your real dates in the Year Planner"). (b) When today's band unit has no unit plan, the day block says so and offers "Plan Early Republic and Expansion day by day" (deep link with the unit set). With a real unit plan in place, home is excellent — today and tomorrow with filenames, test days flagged — so this is about the on-ramp, not the room. **Effort: M.**

### P1 — The paid boundary reads as a broken page in the picker
Planning a paid unit signed out is (correctly, honestly) full-featured: picks, dates, coverage all work. But where the free unit's rows carry live "PDF" links, the Gilded Age's rows show bare filenames as inert text — "READING · The Engines of Industry lesson-01-reading.pdf" — which reads as a rendering bug, not a paywall. The one honest sentence lives in a different panel ("The Gilded Age unit test is part of All-Access…").
**Fix:** Render paid files as disabled chips with a consistent affordance ("PDF · All-Access") and put one line at the top of the picker for paid units: "Planning is free for every unit. The files themselves open with All-Access." The boundary is already fair; make it legible as a boundary instead of a defect. **Effort: S.**

### P2 — Native prompt()/confirm() dialogs carry core flows
Renaming plans and sections, adding sections, and deleting plans all run through `window.prompt`/`window.confirm` (two each in `planner.js` and `year-planner.js`). They work, but they are the most dated-feeling interactions in the product, they cannot be styled, and some school-managed browsers suppress them. Replace with small inline dialogs when those flows are next touched. **Effort: M.**

### P1 — Year-plan import fails silently; the unit planner proves the fix exists
Importing a wrong-shaped JSON into the year planner changed nothing and said nothing (the handler's catch is empty; a file that parses but lacks start/end is dropped on the floor). A teacher cannot tell a failed import from a successful one that looks similar. The unit planner already does this right — importing another unit's file produces "That file is a Gilded Age plan. Switch to that unit in the planner and import it there, so the two unit plans stay separate."
**Fix:** Port that pattern: validate the year file's shape and report either success ("Imported: full survey, Aug 24 – May 28, 15 units") or the specific problem and what to do. **Effort: S.**

### Strengths to keep
The round trip itself is sound: export → fresh browser → import reproduced dates, exam, and edited day counts exactly. Copy-forward's confirm dialog is a model of its kind ("…holidays land on the same calendar date, so check them against next year's real calendar… Export first if you want to keep this year's plan as a file"). Autosave is genuinely invisible — every edit persisted without a save button anywhere, verified across page loads all through this audit.

---

## Job 6 — Mobile (390px)

### P1 — Reordering, the planner's core gesture, has no touch path
Reordering exists only as HTML5 drag-and-drop on the chips. There is no move-up/move-down control on any chip, so on a phone the schedule's order is effectively read-only: a teacher can pick, split, and pin, but cannot move Tuesday's lesson to Thursday. The same absence hits keyboard users. (Drag also gives no affordance on desktop — no grip, no hint; the pin emoji is the only visible chip control.)
**Fix:** Add steppers (↑ ↓) to each chip — they serve touch, keyboard, and mouse users and make the capability discoverable — and keep drag as the fast path on desktop. **Effort: M.**

### P1 — The coverage loop breaks on mobile
On desktop the coverage panel is sticky beside the picker and the pick → meter loop is tight. On mobile the DOM order rules: sections, dates, picker, schedule, *then* coverage. A teacher checking boxes in step 2 must scroll past the entire schedule in step 3 to learn whether coverage moved — the product's signature feedback loop is severed on the device a teacher is most likely to use at a desk between classes.
**Fix:** On narrow widths, pin a compact coverage strip (mini meter + "14 of 15" + gap count, tap to jump to the full panel) at the top of the picker panel or sticky under the site header. **Effort: M.**

### P2 — Density costs
No horizontal overflow anywhere at 390px (real credit — both planners and home hold the width). The cost is vertical and visual: 31 toolbar buttons on the unit planner; a full day-type `<select>` repeated on every schedule row, taking roughly a quarter of each row's width and wrapping chip text to three lines; the intro paragraph plus the 15-pill unit switcher plus the sections panel push "1 · Your dates" about two screens down; the Rycal line prints its full deck URL as wrapped raw text. Collapse the day menu behind a per-row "⋯" on small screens, turn the switcher into a `<select>` under a width breakpoint, and truncate the displayed Rycal URL (the link already works). **Effort: M (S for the switcher and URL).**

---

## Effectiveness as a planning tool (cross-cutting)

- **Pacing math: sound.** The lesson-day model is applied consistently at 45 minutes, 90-minute block (items pair up; an 18-lesson-day unit takes 9 meetings; the test consumes a lesson-day and says so), and A/B (89 meeting days for the course; units land on meeting days only). The proposed-pacing table (days per lesson proportional to blueprint weight, last day held for review) is a sensible default a teacher can override by picks.
- **Exam handling: half done.** The review reserve is real and visible (shaded "review" days, ringed exam date, one-sentence explanation). What is missing is the post-exam flag (Job 3, P1) — the difference between "planned" and "planned in time."
- **The two coverage lenses: keep both, label them.** The blueprint lens is a score with a repair loop; the topic lens is context for a conversation with a department head. They only confuse while both present as scores (Job 2, P1).
- **Overcommitment detection: strong; follow-through: absent.** Compared with the reference points: Students of History's pacing guide is a static PDF — it cannot notice anything, and a teacher discovers the overrun in March. This planner notices in September, in numbers, per unit. TpT product pages promise outcomes with previews; this tool's promise is verifiable on its own screen. The gap is not detection, it is remedy (Job 3, P1) and honest exports (Job 4, P0 ×2). Google Calendar is the right comparison for the calendar itself: it repeats an event's title on every week segment and rings today; the year calendar does neither (unit names print only on a band's first day, across 15 earth-tone colors that sit close together — Colonial brown, Founding green, Early Republic teal are genuinely hard to tell apart at bar weight). Repeat the unit label at each week boundary and add a today ring. **Effort: S–M (P2).**

## Data consistency

### P1 — The free sample's planner mislabels its own crossword
`planner-data.js` (line 78) still names the Progressive Era review item "Crossword (22 answers)." The PE-56 rebuild replaced that crossword with a 56-answer grid; the unit page says "Crossword, 56 answers," and every other unit's planner label says 56. Only the planner — on the flagship free unit, the one every evaluator touches — kept the stale count. On a product whose entire pitch is "the definition on the card is the definition in your notes," a wrong number in the sample is a trust leak out of proportion to its size. **Fix:** correct the label to "Crossword (56 answers)" and add a suite assertion comparing planner item names against the unit pages' counts for all 15 units so the next rebuild cannot drift one surface. **Effort: S.**

---

## Top 8 recommendations, in priority order

1. **Fix the overflow layout defect** — guided notes follow their reading into overflow and are named there; add the squeeze regression test. (P0, Job 3 · S–M)
2. **Put the plan's problems on its outputs** — unplaced-items banner on print plan and sub plan; year .ics export warns before downloading when units do not fit, and never drops them silently. (P0, Job 4 · S–M)
3. **Make the first year-planner run a success** — label the starter year as a starter, state demand vs supply in one line ("Units ask for 270 lesson-days; your year has 178"), and ship defaults that fit a normal year. (P0, Job 1 · M)
4. **Add "Fit to year"** — one guided trim toward the available days with each unit's core-picks floor shown and respected. (P1, Job 3 · M–L)
5. **Make coverage honest about the calendar** — placed-vs-picked coverage line whenever overflow exists; topic panel counts only teachable topics and labels itself reference, not score. (P1, Job 2 · S–M)
6. **One auth-aware save line in both planners** — "Saved in this browser" vs "Saved and synced to your account," replacing the static "nothing is uploaded." (P1, Job 5 · S)
7. **Give reordering a touch and keyboard path, and restore the mobile coverage loop** — chip steppers plus a compact sticky coverage strip on narrow screens. (P1, Job 6 · M)
8. **Connect the picker to the blueprint** — show what each item covers on its row, and let the gap panel offer every covering item, not just the first. (P1, Job 2 · M)

**Quick wins (all S, do alongside anything above):** correct the PE crossword label to 56 and assert planner/page count parity in the suite (Data consistency); port the unit planner's import-error message to the year planner (Job 5); give the unit share link the year link's copy-to-clipboard behavior and sentence (Job 4); flag units scheduled after the exam date (Job 3); order the unit switcher by course position (Job 1); nudge when a test date lands on a non-meeting day (Job 3); add a today ring and week-boundary labels to the year calendar (Effectiveness).
