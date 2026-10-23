# Phase 18, run 1 (2026-10-23): failures captured before /tmp was recycled

Suite died late (ERR_CONNECTION_REFUSED after the Year planner review
section) with these FAIL lines, in order:

1. [Audit top 8] demand line states the arithmetic :: "Your units ask for
   113 lesson-days; your year has 178 lesson-days of room."
2. [Audit top 8] seeded year overflows :: "...ask for 197 lesson-days;
   your year has 178 lesson-days of room."
3. [Audit top 8] fit lands exactly on the year :: [50, 51, 18, 18, 18, 18, 5]
4. [Audit top 8] fit never trims below the core minimum ::
   [18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 7]
5. [Audit quick wins] good import reports what landed :: "Imported: full
   survey, Tue, Sep 1, 2026 - Fri, Jun 4, 2027, 16 units."
6. [Audit quick wins] post-exam warning names the count :: "Exam on Fri,
   May 7, 2027, with 0 review days held in front of it. ... 1 unit is
   scheduled after your exam: The Twenties (test day May 28)..."
7. [Audit quick wins] post-exam warning names the unit and its test day
   (same caption as 6)
8. [Audit quick wins] unit row flags the late test day :: "Imperialism and
   World War I plan itApr 13 - May 6 - estimate days / core minimum 18"
9. [Year planner review] full shape: Course Review band present :: row=
10. [Year planner review] full shape: Course Review 10-day estimate :: row=

Everything through the RC switcher section passed this run, including
"switcher offers 18 units". Fixes queued: audit expectations recomputed
for the 18-unit world; exact_row must match by plan-it link; server
hardening v2 (rlimit, HTTP/1.1, stderr captured to a file).
