#!/usr/bin/env python3
"""Derive test_phase18_review.py from test_phase17_reconstruction.py:
the cumulative suite plus the Course Review integration sections.
Mechanical updates: resilient test server, switcher count 15 -> 18,
review core-id fixtures, zero-error paths. New sections are inserted
before the Zero errors section. Run once; the derived file is the suite.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "..", "site", "tests", "test_phase17_reconstruction.py")).read()


def rep(old, new, n=1):
    global src
    assert src.count(old) == n, (old[:80], src.count(old))
    src = src.replace(old, new)


rep('"""Phase 17 (Reconstruction planner integration) Playwright suite.',
    '"""Phase 18 (Course Review integration) Playwright suite.')
rep("""  TPSP picker contents (RC 24 entries led by dbq4 with dbq15 alongside; the 1879 sharecropping
  contract entry carries its postdating flag on its face)""",
    """  TPSP picker contents (RC 24 entries led by dbq4 with dbq15 alongside; the 1879 sharecropping
  contract entry carries its postdating flag on its face)
  - Course Review, Early Course Review, and Modern Course Review fresh states via ?unit=rv/re/rm
    (core plans of 10, 5, and 7 days; coverage 15 of 15, 6 of 6, 9 of 9); eighteen-unit isolation
  - review TPSP pickers hold only premium DBQs (21 combined, 11 early, 10 modern), each pre-tagged
    to the blueprint entry of its home unit
  - year planner: the review bands sit last in their shapes (Course Review in the full survey,
    Early in the to-1877 shape, Modern in the from-1877 shape), and a scheduled review unit absorbs
    the held review days before the exam instead of stacking blank days on top of it
  - the three review unit pages (43, 18, and 28 plate files, Rycal deck links, no anonymous
    download URLs), entitled-stub controls minting the three review storage prefixes, the
    practice-test path on each unit's test action, us-history rows and cards, sitemap entries""")
rep("""    server = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(PORT), "--directory", PUBLIC, "--bind", "127.0.0.1"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)""",
    """    server_log = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "serve_public.log"), "ab")
    server = subprocess.Popen(
        [sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "serve_public.py"),
         str(PORT), PUBLIC],
        stdout=subprocess.DEVNULL, stderr=server_log)""")
rep('check(S, "switcher offers 15 units",', 'check(S, "switcher offers 18 units",')
rep('"108 lesson-days" in pg.text_content("#demand-line")', '"113 lesson-days" in pg.text_content("#demand-line")')
rep('"192 lesson-days" in pg.text_content("#demand-line")', '"197 lesson-days" in pg.text_content("#demand-line")')
rep('check(S, "fit lands exactly on the year", sum(vals) == 178 and min(vals) >= 18, str(vals))',
    'check(S, "fit lands exactly on the year", vals == [50, 51, 18, 18, 18, 18, 5], str(vals))')
rep('check(S, "fit never trims below the core minimum", bool(vals) and all(v == 18 for v in vals), str(vals))',
    'check(S, "fit never trims below the core minimum", len(vals) == 16 and all(v == 18 for v in vals[:15]) and vals[15] == 7, str(vals))')
rep('"Imported:" in note and "15 units" in note', '"Imported:" in note and "16 units" in note')
rep('"2 units are scheduled after your exam" in enote', '"1 unit is scheduled after your exam" in enote')
rep('"Imperialism and World War I" in enote and "May 13" in enote', '"The Twenties" in enote and "May 28" in enote')
rep('''            wwi_row = ""
            for rowtxt in pg.eval_on_selector_all("#units tr", "els => els.map(e => e.textContent)"):
                if "Imperialism and World War I" in rowtxt:
                    wwi_row = rowtxt
            check(S, "unit row flags the late test day",
                  "is after your exam" in wwi_row and "May 13" in wwi_row, wwi_row[:200])''',
    '''            tw_row = ""
            for rowtxt in pg.eval_on_selector_all("#units tr", "els => els.map(e => e.textContent)"):
                if "The Twenties" in rowtxt:
                    tw_row = rowtxt
            check(S, "unit row flags the late test day",
                  "is after your exam" in tw_row and "May 28" in tw_row, tw_row[:200])''')
rep('pg.eval_on_selector_all("#unit-switch button", "els => els.length") == 15)',
    'pg.eval_on_selector_all("#unit-switch button", "els => els.length") == 18)')
rep('rc_core = core_ids("HCG_RC_ITEMS")',
    '''rc_core = core_ids("HCG_RC_ITEMS")
            rv_core = core_ids("HCG_RV_ITEMS")
            re_core = core_ids("HCG_RE_ITEMS")
            rm_core = core_ids("HCG_RM_ITEMS")''')
rep('''for path in ["/planner.html?unit=rc", "/planner.html?unit=sc", "/planner.html?unit=jr", "/planner.html?unit=er", "/planner.html?unit=fd", "/planner.html?unit=ca", "/planner.html?unit=ma", "/planner.html?unit=cr", "/planner.html?unit=cw", "/planner.html?unit=ww2", "/planner.html?unit=dp", "/planner.html?unit=tw", "/planner.html?unit=wwi", "/planner.html?unit=ga",
                             "/planner.html", "/planner-year.html", "/home.html"]:''',
    '''for path in ["/planner.html?unit=rv", "/planner.html?unit=re", "/planner.html?unit=rm", "/planner.html?unit=rc", "/planner.html?unit=sc", "/planner.html?unit=jr", "/planner.html?unit=er", "/planner.html?unit=fd", "/planner.html?unit=ca", "/planner.html?unit=ma", "/planner.html?unit=cr", "/planner.html?unit=cw", "/planner.html?unit=ww2", "/planner.html?unit=dp", "/planner.html?unit=tw", "/planner.html?unit=wwi", "/planner.html?unit=ga",
                             "/planner.html", "/planner-year.html", "/home.html", "/course-review.html", "/early-review.html", "/modern-review.html", "/us-history.html"]:''')

NEW_SECTIONS = '''
            # ---------------- Review fresh states ----------------
            S = "Review fresh states"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            for unit, name, key, days, cov in [
                    ("rv", "Course Review", "hcg_unit_rv_v1", 10, "15 of 15"),
                    ("re", "Early Course Review", "hcg_unit_re_v1", 5, "6 of 6"),
                    ("rm", "Modern Course Review", "hcg_unit_rm_v1", 7, "9 of 9")]:
                pg.goto(BASE + f"/planner.html?unit={unit}"); settle(pg)
                check(S, f"{unit}: boots to {name}",
                      pg.text_content("#unit-name").strip() == name)
                st = ls_json(pg, key)
                check(S, f"{unit}: fresh totalDays {days}",
                      st and st.get("totalDays") == days, json.dumps(st)[:120])
                check(S, f"{unit}: fresh coverage {cov}",
                      cov in pg.text_content("#covtext"), pg.text_content("#covtext"))
            ctx.close()

            # ---------------- Review switcher + eighteen-unit isolation ----------------
            S = "Review switcher + eighteen-unit isolation"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html"); settle(pg)
            pg.click("#unit-switch button[data-unit='rv']")
            pg.wait_for_url("**unit=rv**"); settle(pg)
            check(S, "switcher boots RV", pg.text_content("#unit-name").strip() == "Course Review")
            st = ls_json(pg, "hcg_unit_rv_v1")
            check(S, "switcher fresh totalDays 10", st and st.get("totalDays") == 10)
            check(S, "switcher coverage 15 of 15", "15 of 15" in pg.text_content("#covtext"))
            for iid in ["rv3-packet", "rv3-sprint", "rv3-practice"]:
                pg.click(f"#picker input[type=checkbox][data-id='{iid}']")
                pg.wait_for_timeout(150)
            check(S, "RV edit drops coverage to 13 of 15",
                  "13 of 15" in pg.text_content("#covtext"), pg.text_content("#covtext"))
            expect_cov = {"ca": "15 of 15", "fd": "15 of 15", "er": "15 of 15",
                          "jr": "15 of 15", "sc": "15 of 15", "rc": "15 of 15",
                          "ga": "15 of 15", "wwi": "15 of 15", "tw": "15 of 15",
                          "dp": "15 of 15", "ww2": "15 of 15", "cw": "15 of 15",
                          "cr": "15 of 15", "ma": "15 of 15",
                          "re": "6 of 6", "rm": "9 of 9"}
            for u2, cov2 in expect_cov.items():
                pg.goto(BASE + f"/planner.html?unit={u2}"); settle(pg)
                check(S, f"{u2.upper()} untouched by RV edit",
                      cov2 in pg.text_content("#covtext"), pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html"); settle(pg)
            check(S, "PE untouched by RV edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=rv"); settle(pg)
            check(S, "RV edit persisted in its own key",
                  "13 of 15" in pg.text_content("#covtext"), pg.text_content("#covtext"))
            check(S, "each unit key intact after switching",
                  all(ls_get(pg, k) for k in ["hcg_unit_v1", "hcg_unit_ga_v1", "hcg_unit_wwi_v1",
                      "hcg_unit_tw_v1", "hcg_unit_dp_v1", "hcg_unit_ww2_v1", "hcg_unit_cw_v1",
                      "hcg_unit_cr_v1", "hcg_unit_ma_v1", "hcg_unit_ca_v1", "hcg_unit_fd_v1",
                      "hcg_unit_er_v1", "hcg_unit_jr_v1", "hcg_unit_sc_v1", "hcg_unit_rc_v1",
                      "hcg_unit_rv_v1", "hcg_unit_re_v1", "hcg_unit_rm_v1"]))
            ctx.close()

            # ---------------- Review TPSP pickers ----------------
            S = "Review TPSP pickers"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            for unit, n in [("rv", 21), ("re", 11), ("rm", 10)]:
                pg.goto(BASE + f"/planner.html?unit={unit}"); settle(pg)
                pg.click("#btn-add-tpsp"); pg.wait_for_timeout(300)
                n_tpsp = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.length")
                check(S, f"{unit}: picker has {n} entries", n_tpsp == n, str(n_tpsp))
                kinds = pg.eval_on_selector_all("#tpsp-list .tpspitem",
                                                "els => els.map(e => e.textContent)")
                check(S, f"{unit}: every picker entry is a premium DBQ",
                      bool(kinds) and all("DBQ" in t for t in kinds), str(kinds)[:200])
            ctx.close()

            # ---------------- Year planner: review bands + reserve ----------------
            S = "Year planner review"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner-year.html"); settle(pg)

            ROW_UNIT = {"Course Review": "rv", "Early Course Review": "re",
                        "Modern Course Review": "rm"}

            def exact_row(name):
                uid = ROW_UNIT[name]
                return pg.eval_on_selector_all(
                    "#units tr",
                    "els => { const r = els.find(e => { const a = e.querySelector('a[href]'); "
                    "return a && a.getAttribute('href') === 'planner.html?unit=' + "
                    + json.dumps(uid) + "; }); return r ? r.textContent : ''; }")

            def held_days():
                t = pg.eval_on_selector("#totals", "e => e.textContent")
                m = re.search(r"Held for exam review\\s*(\\d+)", t)
                return int(m.group(1)) if m else None

            pg.select_option("#y-course", "full"); settle(pg)
            row = exact_row("Course Review")
            check(S, "full shape: Course Review band present, last in the course",
                  row != "" and "Course Review" in row, f"row={row[:120]}")
            check(S, "full shape: Course Review 10-day estimate",
                  year_days("Course Review") == "10" and "estimate" in row, f"row={row[:120]}")
            link = pg.eval_on_selector_all(
                "#units tr a",
                "els => els.map(a => a.getAttribute('href')).filter(h => h && h.includes('unit=rv'))")
            check(S, "Course Review plan-it link", link == ["planner.html?unit=rv"], str(link))
            pg.select_option("#y-course", "early"); settle(pg)
            check(S, "early shape: Early Course Review band present",
                  exact_row("Early Course Review") != "")
            check(S, "early shape: Early Course Review 5-day estimate",
                  year_days("Early Course Review") == "5")
            check(S, "early shape: combined Course Review absent",
                  exact_row("Course Review") == "")
            check(S, "early shape: Modern Course Review absent",
                  exact_row("Modern Course Review") == "")
            pg.select_option("#y-course", "modern"); settle(pg)
            check(S, "modern shape: Modern Course Review band present",
                  exact_row("Modern Course Review") != "")
            check(S, "modern shape: Modern Course Review 7-day estimate",
                  year_days("Modern Course Review") == "7")
            check(S, "modern shape: Early Course Review absent",
                  exact_row("Early Course Review") == "")
            check(S, "modern shape: combined Course Review absent",
                  exact_row("Course Review") == "")
            # Reserve reconciliation: the review unit is the held review time.
            pg.select_option("#y-course", "full"); settle(pg)
            pg.fill("#y-exam", "2027-05-20")
            pg.eval_on_selector("#y-exam", "e => e.dispatchEvent(new Event('change'))")
            pg.wait_for_timeout(300)
            pg.fill("#y-review", "5")
            pg.eval_on_selector("#y-review", "e => e.dispatchEvent(new Event('change'))")
            settle(pg)
            check(S, "reserve: the 10-day review absorbs 5 held days",
                  held_days() == 0, str(held_days()))
            pg.fill("#y-review", "12")
            pg.eval_on_selector("#y-review", "e => e.dispatchEvent(new Event('change'))")
            settle(pg)
            check(S, "reserve: 12 held days less the review leaves 2",
                  held_days() == 2, str(held_days()))
            pg.select_option("#y-course", "early"); settle(pg)
            check(S, "reserve: early shape leaves 12 less the 5-day review = 7",
                  held_days() == 7, str(held_days()))
            ctx.close()

            # ---------------- Review home ----------------
            S = "Review home"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.add_init_script(seed_plan_script("hcg_unit_rv_v1", rv_core))
            pg.goto(BASE + "/home.html"); settle(pg)
            blocks = pg.text_content("#home-blocks")
            check(S, "RV: blocks render", not pg.eval_on_selector("#home-blocks", "e => e.hidden"))
            check(S, "RV: unit name renders", "Course Review" in blocks, blocks[:200])
            pdf_hrefs = pg.eval_on_selector_all(
                "#home-blocks a",
                "els => els.map(a => a.getAttribute('href') || '').filter(h => h.endsWith('.pdf'))")
            check(S, "RV: no public pdf links for All-Access unit", pdf_hrefs == [],
                  str(pdf_hrefs)[:200])
            ctx.close()

            # ---------------- Entitled stub (review units) ----------------
            S = "Entitled stub (review)"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.route("https://stub.example/**",
                     lambda route: route.fulfill(status=200, content_type="text/html",
                                                 body="stub download"))
            for unit, prefix in [("rv", "hcg/course-review/"), ("re", "hcg/early-review/"),
                                 ("rm", "hcg/modern-review/")]:
                pg.goto(BASE + f"/planner.html?unit={unit}"); settle(pg)
                pg.evaluate("""
                  window.HCGAuth.entitlement = function () {
                    return { paid: true, allAccess: true, status: "active" };
                  };
                  window.HCGFiles = { url: function (p) { return Promise.resolve("https://stub.example/" + p); } };
                  window.HCGPlannerRefresh();
                """)
                pg.wait_for_timeout(400)
                stor = pg.eval_on_selector_all(
                    "a.ga-dl", "els => els.map(a => a.getAttribute('data-storage'))")
                check(S, f"{unit}: download controls appear", len(stor) > 0, str(len(stor)))
                check(S, f"{unit}: all controls mint {prefix} paths",
                      bool(stor) and all(s and s.startswith(prefix) for s in stor),
                      str(stor)[:200])
                test_storage = pg.get_attribute("#test-action a.ga-dl", "data-storage")
                check(S, f"{unit}: test download uses the practice-test path",
                      test_storage == prefix + "practice-test.pdf", str(test_storage))
            ctx.close()

            # ---------------- Review unit pages ----------------
            S = "Review unit pages"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            for slug, name, files, terms in [
                    ("course-review", "Course Review", 43, "840"),
                    ("early-review", "Early Course Review", 18, "336"),
                    ("modern-review", "Modern Course Review", 28, "504")]:
                pg.goto(BASE + f"/{slug}.html"); settle(pg)
                check(S, f"{slug}: page boots", name in pg.text_content("h1"))
                n_files = pg.eval_on_selector_all("li[data-file]", "els => els.length")
                check(S, f"{slug}: plate lists {files} files", n_files == files, str(n_files))
                pdf_hrefs = pg.eval_on_selector_all(
                    "a", "els => els.map(a => a.getAttribute('href') || '').filter(h => h.endsWith('.pdf'))")
                check(S, f"{slug}: zero pdf anchors for anonymous", pdf_hrefs == [],
                      str(pdf_hrefs)[:200])
                check(S, f"{slug}: Rycal deck link present",
                      f"https://rycal.web.app/hcg-{slug}-flashcards" in pg.content())
                check(S, f"{slug}: term count {terms} stated", terms in pg.text_content("body"))
            ctx.close()

            # ---------------- Review static files ----------------
            S = "Review static files"
            ush = open(os.path.join(PUBLIC, "us-history.html")).read()
            for slug in ("course-review", "early-review", "modern-review"):
                check(S, f"us-history links {slug} with its cover",
                      f'href="{slug}.html"' in ush and f"assets/{slug}-cover.png" in ush)
            smap = open(os.path.join(PUBLIC, "sitemap.xml")).read()
            for slug in ("course-review", "early-review", "modern-review"):
                check(S, f"sitemap lists {slug}",
                      f"humanitiescurriculumgroup.web.app/{slug}" in smap)

'''
anchor = "            # ---------------- Zero errors, two widths ----------------"
assert src.count(anchor) == 1
src = src.replace(anchor, NEW_SECTIONS + anchor)

open(os.path.join(HERE, "..", "site", "tests", "test_phase18_review.py"), "w").write(src)
print("derived test_phase18_review.py:", len(src), "chars")
