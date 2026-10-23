# Curriculum + Planner Site — Concept

_Status: Alex's call made 2026-10-20. New site under the Knoweth parent brand. TPSP stays as it is. V1 BUILT AND LIVE 2026-10-20 evening: https://humanitiescurriculumgroup.web.app (Firebase hosting site on cue-bb34b; source ~/workspace/curriculum-planner/site/). Pages: home, US History course map, Progressive Era unit page (all 36 PDFs downloadable as the free sample), About, and the planner prototype (dates → pacing proposal → plate picker → schedule → live coverage meter against the 15-entry blueprint; browser-local, no accounts). Brand on site: Humanities Curriculum Group (navy/rust/powder-blue). Still open: custom domain (humanitiescurriculumgroup.org looks unregistered; .com check inconclusive from sandbox), pricing/payments, accounts._

## The idea

A social studies curriculum site and TpT presence in the mold of Students of History and Lessons in Humanities: full courses (US History, World History, Civics/Government, Geography) with lessons, activities, and tests. The differentiator neither competitor has: a built-in unit and year planner with a calendar.

Competitors sell a fixed plan or a pile of files. This sells the content plus the system that turns it into a teacher's actual year.

## The planner (the differentiator)

1. The teacher enters their frame: school year, quarter, or semester start and end dates, plus their state test date or AP exam date.
2. The planner works backward from the exam date and proposes a pacing timeline: how many instructional days each unit gets, with review days reserved before the exam.
3. For each unit, the teacher browses a plate of assignment options (readings, primary source work, activities, projects, quick checks, writing) and adds the ones they want to their calendar.
4. The end-of-unit test is added automatically at the end of each unit.
5. A coverage indicator checks the teacher's selections against the test: every test item is tagged to the topics and skills it assesses, every assignment is tagged to what it teaches. The indicator shows what is covered and names the gaps, with one-click assignment suggestions that fill them.
6. The teacher can drag days, swap assignments, and re-balance units. The coverage indicator updates live.

## Why this can win

- Students of History's plan is fixed: their sequence, their pacing. Ours adapts to the teacher's actual calendar, breaks, and exam date.
- The coverage indicator is only possible with rigorous tagging of every assignment and test item. The TPSP audit and tagging discipline is the enabling asset. It is slow for a competitor to copy because the tagging has to be built into the content from the start.
- Knoweth already owns the adjacent pieces: TPSP (source bank and builder), Rycal (study side), Crossroads History Lab (TpT storefront).

## Business shape (draft, undecided)

- Website: subscription for the planner plus full curriculum access (the planner only works as software, so it lives on the site, not on TpT).
- TpT (Crossroads History Lab): unit bundles and individual resources as static purchases, which double as discovery and as the printable form of what the planner assembles.
- Free layer: sample unit plus planner demo, mirroring how Students of History gives away the first unit.

## Content reality

- Students of History's moat is volume: hundreds of lessons across four courses, built over years. We do not match that at launch.
- Wedge: one course done completely before any second course starts. The planner makes a right-sized library feel complete because the teacher sees coverage, not a pile of files.
- Reuse where honest: TPSP sources and premium DBQ material can anchor the primary-source assignments in US units. Net-new content needed per unit: lecture/reading core, activities, unit test built to a tagged blueprint.

## Data model (the part everything hangs on)

- Every unit has a test blueprint: a list of assessable topics and skills with weights.
- Every test item maps to one or more blueprint entries.
- Every assignment maps to the blueprint entries it teaches or practices.
- Coverage = weighted share of blueprint entries taught by at least one selected assignment before the test date.
- Pacing engine: instructional days = calendar days minus weekends, breaks, and non-instructional days; units allocated days proportional to blueprint weight, adjustable by the teacher.

## Decisions queue (one at a time)

1. DONE 2026-10-20: new site under Knoweth; TPSP unchanged.
2. DONE 2026-10-20: launch scope is US History only, done completely.
3. Product name.
4. DONE 2026-10-20: build order is one unit end to end first (content + blueprint + planner on real material), then scale. The pilot unit also sets the design template/aesthetic for the course. Alex's existing materials are scattered and stylistically inconsistent; first work item is gathering and inventorying what he has for the pilot unit.
5. Pricing shape: subscription tiers, TpT bundle pricing.
6. How much TPSP material carries over at launch.
7. DONE 2026-10-20: pilot unit is the Progressive Era. Existing TPSP assets for it: 50 audited sources in the progressive-era file (1898-1920, domestic reform core plus immigration and imperialism/WWI) and premium DBQ 11 "Progressive Era Promises." Missing: reading/lecture core, activities, study guide, tagged unit test, and Alex's own scattered unit materials (not yet handed over).

## Distribution: TpT posting (REVISED 2026-10-20 — AI ban)

Original plan (superseded same day): Muse posts finished resources to TpT via the seller dashboard, one at a time, template from the first listing. That still describes the mechanics (no seller API; browser flow; first listing must be free), BUT on Oct 15, 2026 Chalkbeat reported TpT is banning AI-generated resources: announced at the Oct 8 seller town hall, sellers told to stop using AI-generated text and images in resources and listings and to replace AI content in existing products; detection/removal tools in development. Exact scope (AI-assisted vs AI-generated) and enforcement dates not yet published. CONSEQUENCE: no automated or high-volume posting of Claude-built resources to TpT — that is precisely the pattern the ban targets, and evading detection is off the table. The Knoweth website is the primary channel; TpT is demoted to an optional later channel for genuinely Alex-authored resources at a normal pace, pending TpT's published policy line on AI-assisted work. Also announced: Premium seller tier closed Oct 1, 2026, replaced by an Exclusive tier ($60/yr, exclusivity on digital resources); payout rates change Jan 1, 2027.

## Open questions
- Does the planner need class-period awareness (block schedules, multiple preps) at launch, or is one calendar per teacher enough for v1?
- Export: Google Calendar sync and printable year-at-a-glance are likely expected. Which is v1?
- State standards alignment: Students of History leads with TEKS, SOL, NGSSS, Regents. Which frameworks do we tag to at launch, beyond AP?
