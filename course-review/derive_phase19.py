#!/usr/bin/env python3
"""Derive test_phase19_homework.py from test_phase18_review.py: retitle,
and insert two sections before the zero-errors sweep: unit-page plates
(slides and teacher notes as real plate rows, Rycal vocab row in the
review block, no 'Also included' anywhere) and homework (per-day
homework lines in the unit planner: list input, persistence, week view,
print plan, sub plan)."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "site", "tests", "test_phase18_review.py")
DST = os.path.join(HERE, "..", "site", "tests", "test_phase19_homework.py")
src = open(SRC).read()

def rep(old, new, n=1):
    global src
    assert src.count(old) == n, (old[:80], src.count(old))
    src = src.replace(old, new)

rep('"""Phase 18 (Course Review integration) Playwright suite.',
    '"""Phase 19 (cumulative): everything in phase 18, plus the October 23 fixes round:\n'
    '  - slides and teacher notes are plate rows on every unit page (the old script-appended\n'
    '    "Also included" line is gone), and the Progressive Era decks and teacher notes are\n'
    '    public files beside the unit\'s PDFs\n'
    '  - a Vocab Review row in each unit\'s review block links the unit\'s Rycal deck\n'
    '  - homework: a per-day homework line in the unit planner, saved with the plan, shown\n'
    '    in the week view, and carried into the print plan and the sub plan.\n'
    'Phase 18 summary:')

NEW_SECTIONS = '''
            # ---------------- Unit page plates ----------------
            S = "Unit page plates"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/progressive-era.html"); settle(pg)
            pe_html = pg.content()
            n_pe_slides = sum(pe_html.count("files/lesson-%02d-slides.pptx" % n) for n in range(1, 9))
            check(S, "PE: eight public slide deck links", n_pe_slides == 8, str(n_pe_slides))
            check(S, "PE: eight public teacher notes links",
                  sum(pe_html.count("files/lesson-%02d-teacher-notes.pdf" % n) for n in range(1, 9)) == 8)
            check(S, "PE: no Also included line", "Also included" not in pe_html)
            check(S, "PE: Rycal vocab row in the review block",
                  "Vocab Review" in pe_html and pe_html.count("hcg-progressive-era-flashcards") >= 2)
            pg.goto(BASE + "/modern-america.html"); settle(pg)
            n_slides = pg.eval_on_selector_all("li[data-file$='slides.pptx']", "els => els.length")
            n_tn = pg.eval_on_selector_all("li[data-file$='teacher-notes.pdf']", "els => els.length")
            check(S, "MA: eight slides plate rows", n_slides == 8, str(n_slides))
            check(S, "MA: eight teacher-notes plate rows", n_tn == 8, str(n_tn))
            ma_html = pg.content()
            check(S, "MA: no Also included line", "Also included" not in ma_html)
            check(S, "MA: Rycal vocab row in the review block",
                  "Vocab Review" in ma_html and ma_html.count("hcg-modern-america-flashcards") >= 2)
            ctx.close()

            # ---------------- Homework ----------------
            S = "Homework"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html"); settle(pg)
            isos = pg.eval_on_selector_all("input[data-hw]", "els => els.map(e => e.getAttribute('data-hw'))")
            check(S, "homework inputs on meeting days", len(isos) >= 5, str(len(isos)))
            iso0 = isos[0]
            HW = "Read pages 41-47 and finish question 2"
            pg.fill("input[data-hw='" + iso0 + "']", HW)
            pg.dispatch_event("input[data-hw='" + iso0 + "']", "change")
            pg.wait_for_timeout(500)
            saved = ls_json(pg, "hcg_unit_v1")
            secs = saved.get("sections") or [saved]
            sec0 = secs[saved.get("active", 0)] if secs else {}
            hwmap = sec0.get("homework") or {}
            check(S, "homework saved into the plan", hwmap.get(iso0) == HW, str(hwmap)[:160])
            pg.reload(); settle(pg)
            check(S, "homework persists across reload",
                  pg.input_value("input[data-hw='" + iso0 + "']") == HW)
            pg.click("button.viewbtn[data-view='week']"); settle(pg)
            wtxt = pg.text_content("#weekview") or ""
            check(S, "week view shows the homework", "Homework:" in wtxt and "pages 41-47" in wtxt, wtxt[:200])
            pg.click("button.viewbtn[data-view='list']"); settle(pg)
            pg.click("#print-week"); pg.wait_for_timeout(300)
            pa = pg.eval_on_selector("#printArea", "e => e.innerHTML")
            check(S, "print plan carries the homework", "Homework:" in pa and "pages 41-47" in pa, pa[:200])
            pg.click("#print-sub"); pg.wait_for_timeout(300)
            pa = pg.eval_on_selector("#printArea", "e => e.innerHTML")
            check(S, "sub plan carries the homework", "Homework:" in pa and "pages 41-47" in pa, pa[:200])
            pg.fill("input[data-hw='" + iso0 + "']", "")
            pg.dispatch_event("input[data-hw='" + iso0 + "']", "change")
            pg.wait_for_timeout(500)
            saved = ls_json(pg, "hcg_unit_v1")
            secs = saved.get("sections") or [saved]
            sec0 = secs[saved.get("active", 0)] if secs else {}
            check(S, "clearing the input removes the homework",
                  iso0 not in (sec0.get("homework") or {}), str(sec0.get("homework"))[:120])
            ctx.close()

'''
rep("\n            # ---------------- Zero errors, two widths ----------------",
    NEW_SECTIONS + "            # ---------------- Zero errors, two widths ----------------")

open(DST, "w").write(src)
print("derived test_phase19_homework.py:", len(src), "chars")
