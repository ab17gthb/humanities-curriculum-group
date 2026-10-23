#!/usr/bin/env python3
"""Phase 7 (Depression and New Deal planner integration) Playwright suite.

Serves site/public locally and checks, in the pattern of the Gilded Age
integration tests:
  - PE, GA, WWI, and TW regression (the Phase 6 suites, switcher now 5 units)
  - Depression and New Deal fresh state via ?unit=dp and via the unit switcher
  - state isolation across all five units
  - year planner fed length and estimate label for the Twenties and Depression and New Deal
  - teacher home rendering of seeded PE, GA, WWI, Twenties, and Depression and New Deal plans
  - Twenties and Depression and New Deal outputs: print view, sub plan, ICS, share link, export, import refusal
  - TPSP picker contents (25 entries led by dbq5)
  - anonymous state exposes no public Twenties or Depression and New Deal file URLs
  - entitled-stub download controls mint hcg/twenties/ and hcg/depression-new-deal/ URLs
  - zero console/page errors at 1440px and 390px

Run: python3 test_phase7_depression.py  (playwright + chromium)
"""
import json
import os
import re
import subprocess
import sys
import time
import urllib.request

PUBLIC = os.path.expanduser("~/workspace/curriculum-planner/site/public")
PORT = 8939
BASE = f"http://127.0.0.1:{PORT}"
EXE = "/home/hatch/.cache/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell"

RESULTS = {}  # suite -> [passed, failed, failures]


def check(suite, name, cond, detail=""):
    r = RESULTS.setdefault(suite, [0, 0, []])
    if cond:
        r[0] += 1
    else:
        r[1] += 1
        r[2].append(f"{name} :: {detail}")
        print(f"FAIL [{suite}] {name} :: {detail}")


def core_ids(unit_global):
    out = subprocess.run(
        ["node", "-e",
         f"global.window={{}};require('{PUBLIC}/planner-data.js');"
         f"console.log(JSON.stringify(window.{unit_global}.filter(i=>i.core).map(i=>i.id)))"],
        capture_output=True, text=True)
    return json.loads(out.stdout.strip())


def attach_errors(page, bag):
    page.on("pageerror", lambda e: bag.append(f"pageerror: {e}"))
    page.on("console", lambda m: bag.append(f"console.{m.type}: {m.text}") if m.type == "error" else None)


def real_errors(bag):
    out = []
    for e in bag:
        if "Failed to load resource" in e or "net::" in e or "favicon" in e:
            continue
        out.append(e)
    return out


def settle(page):
    page.wait_for_load_state("load")
    page.wait_for_timeout(900)


def ls_get(page, key):
    return page.evaluate(f"localStorage.getItem({json.dumps(key)})")


def ls_json(page, key):
    raw = ls_get(page, key)
    return json.loads(raw) if raw else None


def proxy_cfg():
    raw = os.environ.get("http_proxy") or os.environ.get("HTTP_PROXY")
    if not raw:
        return None
    m = re.match(r"(https?://)([^:@/]+):([^@/]+)@(.+)", raw)
    if m:
        return {"server": m.group(1) + m.group(4), "username": m.group(2), "password": m.group(3),
                "bypass": "127.0.0.1,localhost"}
    return {"server": raw, "bypass": "127.0.0.1,localhost"}


def seed_plan_script(key, ids):
    sel = {i: True for i in ids}
    payload = {"selected": sel, "order": None, "splits": {}, "view": "list", "active": 0,
               "sections": [], "customItems": [], "totalDays": 18, "totalMeetings": 17}
    js_payload = json.dumps(payload)
    return f"""
    (function () {{
      var p = {js_payload};
      function ISO(d) {{ function z(n) {{ return (n < 10 ? "0" : "") + n; }}
        return d.getFullYear() + "-" + z(d.getMonth() + 1) + "-" + z(d.getDate()); }}
      var now = new Date();
      var mon = new Date(now); mon.setDate(now.getDate() - ((now.getDay() + 6) % 7));
      var test = new Date(now); test.setDate(now.getDate() + 1);
      p.sections = [{{ name: "Period 1", start: ISO(mon), test: ISO(test),
        dayTypes: {{}}, pins: {{}}, rotation: "daily", period: 45 }}];
      localStorage.setItem({json.dumps(key)}, JSON.stringify(p));
    }})();
    """


def main():
    server = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(PORT), "--directory", PUBLIC, "--bind", "127.0.0.1"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        for _ in range(50):
            try:
                urllib.request.urlopen(BASE + "/planner.html", timeout=2)
                break
            except Exception:
                time.sleep(0.2)

        from playwright.sync_api import sync_playwright
        with sync_playwright() as pw:
            browser = pw.chromium.launch(executable_path=EXE, proxy=proxy_cfg(),
                                         args=["--no-sandbox"])
            pe_core = core_ids("HCG_ITEMS")
            ga_core = core_ids("HCG_GA_ITEMS")
            wwi_core = core_ids("HCG_WWI_ITEMS")
            tw_core = core_ids("HCG_TW_ITEMS")
            dp_core = core_ids("HCG_DP_ITEMS")

            # ---------------- PE regression ----------------
            S = "PE regression"
            ctx = browser.new_context()
            errs = []
            pg = ctx.new_page(); attach_errors(pg, errs)
            pg.goto(BASE + "/planner.html"); settle(pg)
            check(S, "unit name PE", pg.text_content("#unit-name").strip() == "The Progressive Era",
                  pg.text_content("#unit-name"))
            check(S, "switcher offers 5 units",
                  pg.eval_on_selector_all("#unit-switch button", "els => els.length") == 5)
            n_items = pg.evaluate("window.HCG_ITEMS.length")
            n_boxes = pg.eval_on_selector_all("#picker input[type=checkbox]", "els => els.length")
            check(S, "picker count = PE items", n_boxes == n_items, f"{n_boxes} vs {n_items}")
            check(S, "coverage 15 of 15", "15 of 15" in pg.text_content("#covtext"), pg.text_content("#covtext"))
            st = ls_json(pg, "hcg_unit_v1")
            check(S, "PE totalDays 18", st and st.get("totalDays") == 18, json.dumps(st)[:120])
            check(S, "PE test is a public file link",
                  "files/unit-test.pdf" in (pg.get_attribute("#test-action a", "href") or ""))
            check(S, "PE topics panel", "Progressive reform" in pg.text_content("#standards"))
            check(S, "no page errors", not real_errors(errs), "; ".join(real_errors(errs))[:300])
            ctx.close()

            # ---------------- GA regression ----------------
            S = "GA regression"
            ctx = browser.new_context()
            errs = []
            pg = ctx.new_page(); attach_errors(pg, errs)
            pg.goto(BASE + "/planner.html?unit=ga"); settle(pg)
            check(S, "unit name GA", pg.text_content("#unit-name").strip() == "The Gilded Age",
                  pg.text_content("#unit-name"))
            n_items = pg.evaluate("window.HCG_GA_ITEMS.length")
            n_boxes = pg.eval_on_selector_all("#picker input[type=checkbox]", "els => els.length")
            check(S, "GA items 50 and picker matches", n_items == 50 and n_boxes == 50, f"{n_items}/{n_boxes}")
            check(S, "coverage 15 of 15", "15 of 15" in pg.text_content("#covtext"), pg.text_content("#covtext"))
            st = ls_json(pg, "hcg_unit_ga_v1")
            check(S, "GA totalDays 18", st and st.get("totalDays") == 18, json.dumps(st)[:120])
            ta = pg.text_content("#test-action").strip()
            href = pg.get_attribute("#test-action a", "href")
            check(S, "GA test panel text unchanged",
                  ta == "The Gilded Age unit test is part of All-Access. Subscribers download it from the Gilded Age unit page." and href == "gilded-era.html",
                  f"{ta} | {href}")
            pdf_hrefs = pg.eval_on_selector_all("a", "els => els.map(a => a.getAttribute('href') || '').filter(h => h.endsWith('.pdf'))")
            check(S, "GA anonymous has no public pdf links", pdf_hrefs == [], str(pdf_hrefs)[:200])
            check(S, "GA topics panel", "Politics, corruption, and protest" in pg.text_content("#standards"))
            check(S, "no page errors", not real_errors(errs), "; ".join(real_errors(errs))[:300])
            ctx.close()

            # ---------------- WWI fresh via ?unit=wwi ----------------
            S = "WWI fresh (?unit=wwi)"
            ctx = browser.new_context()
            errs = []
            pg = ctx.new_page(); attach_errors(pg, errs)
            pg.goto(BASE + "/planner.html?unit=wwi"); settle(pg)
            check(S, "unit name WWI", pg.text_content("#unit-name").strip() == "Imperialism and World War I",
                  pg.text_content("#unit-name"))
            check(S, "essential question", "seek power overseas" in pg.text_content("#unit-eq"),
                  pg.text_content("#unit-eq")[:100])
            check(S, "blueprint 15", pg.evaluate("Object.keys(window.HCG_WWI_BLUEPRINT).length") == 15)
            check(S, "lessons 8 with questions",
                  pg.evaluate("window.HCG_WWI_LESSONS.length === 8 && window.HCG_WWI_LESSONS.every(l => !!l.question)"))
            check(S, "items 50", pg.evaluate("window.HCG_WWI_ITEMS.length") == 50)
            n_boxes = pg.eval_on_selector_all("#picker input[type=checkbox]", "els => els.length")
            check(S, "picker shows 50 items", n_boxes == 50, str(n_boxes))
            check(S, "coverage 15 of 15 on fresh core plan", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            st = ls_json(pg, "hcg_unit_wwi_v1")
            check(S, "core totalDays 18", st and st.get("totalDays") == 18, json.dumps(st)[:160])
            topics_txt = pg.text_content("#standards")
            for label in ["Imperial expansion and its critics", "The United States in Asia and the Pacific",
                          "The United States in the Caribbean and Latin America",
                          "The First World War: causes, combat, and mobilization",
                          "The home front: liberty, labor, race, and migration",
                          "Peace, the League fight, and the turn inward",
                          "Expansion and the Great War"]:
                check(S, f"topic panel shows: {label[:40]}", label in topics_txt)
            ta = pg.text_content("#test-action").strip()
            href = pg.get_attribute("#test-action a", "href")
            check(S, "WWI test panel points at its own unit page",
                  ta == "Imperialism and World War I unit test is part of All-Access. Subscribers download it from the Imperialism and World War I unit page." and href == "imperialism-wwi.html",
                  f"{ta} | {href}")
            # TPSP picker
            pg.click("#btn-add-tpsp"); pg.wait_for_timeout(300)
            n_tpsp = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.length")
            check(S, "TPSP picker has 17 entries", n_tpsp == 17, str(n_tpsp))
            first = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.length ? els[0].textContent : ''")
            check(S, "picker leads with dbq17", "Was American Expansion Overseas a Duty or a Betrayal?" in first, first[:100])
            pg.fill("#tpsp-q", "Owen"); pg.wait_for_timeout(300)
            filt = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.map(e => e.textContent).join(' ')")
            check(S, "picker search finds Owen source", "Dulce et Decorum Est" in filt, filt[:120])
            pg.fill("#tpsp-q", ""); pg.wait_for_timeout(200)
            pg.click("#tpsp-close")
            check(S, "no page errors", not real_errors(errs), "; ".join(real_errors(errs))[:300])
            ctx.close()


            # ---------------- Twenties fresh via ?unit=tw ----------------
            S = "TW fresh (?unit=tw)"
            ctx = browser.new_context()
            errs = []
            pg = ctx.new_page(); attach_errors(pg, errs)
            pg.goto(BASE + "/planner.html?unit=tw"); settle(pg)
            check(S, "unit name TW", pg.text_content("#unit-name").strip() == "The Twenties",
                  pg.text_content("#unit-name"))
            check(S, "essential question", "weaker than it looked" in pg.text_content("#unit-eq"),
                  pg.text_content("#unit-eq")[:100])
            check(S, "blueprint 15", pg.evaluate("Object.keys(window.HCG_TW_BLUEPRINT).length") == 15)
            check(S, "lessons 8 with questions",
                  pg.evaluate("window.HCG_TW_LESSONS.length === 8 && window.HCG_TW_LESSONS.every(l => !!l.question)"))
            check(S, "items 50", pg.evaluate("window.HCG_TW_ITEMS.length") == 50)
            n_boxes = pg.eval_on_selector_all("#picker input[type=checkbox]", "els => els.length")
            check(S, "picker shows 50 items", n_boxes == 50, str(n_boxes))
            check(S, "coverage 15 of 15 on fresh core plan", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            st = ls_json(pg, "hcg_unit_tw_v1")
            check(S, "core totalDays 18", st and st.get("totalDays") == 18, json.dumps(st)[:160])
            topics_txt = pg.text_content("#standards")
            for label in ["The new economy: production, consumption, and credit",
                          "Mass media and national culture",
                          "The automobile and the reshaped map of daily life",
                          "Politics, Prohibition, and the limited state",
                          "Race, migration, and Black cultural and political movements",
                          "Belonging and belief: restriction, the Klan, and the culture wars",
                          "Prosperity and Its Limits"]:
                check(S, f"topic panel shows: {label[:40]}", label in topics_txt)
            ta = pg.text_content("#test-action").strip()
            href = pg.get_attribute("#test-action a", "href")
            check(S, "TW test panel points at its own unit page",
                  ta == "The Twenties unit test is part of All-Access. Subscribers download it from the Twenties unit page." and href == "twenties.html",
                  f"{ta} | {href}")
            pg.click("#btn-add-tpsp"); pg.wait_for_timeout(300)
            n_tpsp = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.length")
            check(S, "TPSP picker has 23 entries", n_tpsp == 23, str(n_tpsp))
            first = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.length ? els[0].textContent : ''")
            check(S, "picker leads with dbq18", "Did the 1920s Move America Forward?" in first, first[:100])
            pg.fill("#tpsp-q", "Garvey"); pg.wait_for_timeout(300)
            filt = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.map(e => e.textContent).join(' ')")
            check(S, "picker search finds Garvey sources", "Garvey" in filt and "Negro" in filt, filt[:160])
            pg.fill("#tpsp-q", ""); pg.wait_for_timeout(200)
            pg.click("#tpsp-close")
            check(S, "no page errors", not real_errors(errs), "; ".join(real_errors(errs))[:300])
            ctx.close()


            # ---------------- Depression and New Deal fresh via ?unit=dp ----------------
            S = "DP fresh (?unit=dp)"
            ctx = browser.new_context()
            errs = []
            pg = ctx.new_page(); attach_errors(pg, errs)
            pg.goto(BASE + "/planner.html?unit=dp"); settle(pg)
            check(S, "unit name DP", pg.text_content("#unit-name").strip() == "Depression and New Deal",
                  pg.text_content("#unit-name"))
            check(S, "essential question", "leave undone" in pg.text_content("#unit-eq"),
                  pg.text_content("#unit-eq")[:100])
            check(S, "blueprint 15", pg.evaluate("Object.keys(window.HCG_DP_BLUEPRINT).length") == 15)
            check(S, "lessons 8 with questions",
                  pg.evaluate("window.HCG_DP_LESSONS.length === 8 && window.HCG_DP_LESSONS.every(l => !!l.question)"))
            check(S, "items 50", pg.evaluate("window.HCG_DP_ITEMS.length") == 50)
            n_boxes = pg.eval_on_selector_all("#picker input[type=checkbox]", "els => els.length")
            check(S, "picker shows 50 items", n_boxes == 50, str(n_boxes))
            check(S, "coverage 15 of 15 on fresh core plan", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            st = ls_json(pg, "hcg_unit_dp_v1")
            check(S, "core totalDays 18", st and st.get("totalDays") == 18, json.dumps(st)[:160])
            topics_txt = pg.text_content("#standards")
            for label in ["Collapse and human cost",
                          "From Hoover to Roosevelt: the changing federal role",
                          "Relief, recovery, and reform: the New Deal programs",
                          "Opposition, the critics, and the courts",
                          "Labor, exclusion, and the unfinished agenda",
                          "Legacy: the new American state and its limits"]:
                check(S, f"topic panel shows: {label[:40]}", label in topics_txt)
            ta = pg.text_content("#test-action").strip()
            href = pg.get_attribute("#test-action a", "href")
            check(S, "DP test panel points at its own unit page",
                  ta == "Depression and New Deal unit test is part of All-Access. Subscribers download it from the Depression and New Deal unit page." and href == "depression-new-deal.html",
                  f"{ta} | {href}")
            pg.click("#btn-add-tpsp"); pg.wait_for_timeout(300)
            n_tpsp = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.length")
            check(S, "TPSP picker has 25 entries", n_tpsp == 25, str(n_tpsp))
            first = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.length ? els[0].textContent : ''")
            check(S, "picker leads with dbq5", "Did the New Deal End the Great Depression?" in first, first[:100])
            pg.fill("#tpsp-q", "Migrant"); pg.wait_for_timeout(300)
            filt = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.map(e => e.textContent).join(' ')")
            check(S, "picker search finds Migrant Mother", "Migrant Mother" in filt, filt[:160])
            pg.fill("#tpsp-q", ""); pg.wait_for_timeout(200)
            pg.click("#tpsp-close")
            check(S, "no page errors", not real_errors(errs), "; ".join(real_errors(errs))[:300])
            ctx.close()

            # ---------------- TW fresh via switcher + isolation ----------------
            S = "TW switcher + five-unit isolation"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html"); settle(pg)
            pg.click("#unit-switch button[data-unit='tw']")
            pg.wait_for_url("**unit=tw**"); settle(pg)
            check(S, "switcher boots TW", pg.text_content("#unit-name").strip() == "The Twenties")
            st = ls_json(pg, "hcg_unit_tw_v1")
            check(S, "switcher fresh totalDays 18", st and st.get("totalDays") == 18)
            check(S, "switcher coverage 15 of 15", "15 of 15" in pg.text_content("#covtext"))
            # Edit TW: drop Lesson 1's core (entries 1 and 2 lose their core coverage)
            for iid in ["t1-reading", "t1-notes", "t1-activity"]:
                pg.click(f"#picker input[type=checkbox][data-id='{iid}']")
                pg.wait_for_timeout(150)
            check(S, "TW edit drops coverage to 13 of 15", "13 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=wwi"); settle(pg)
            check(S, "WWI untouched by TW edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            wwi_st = ls_json(pg, "hcg_unit_wwi_v1")
            check(S, "WWI saved state intact", wwi_st and wwi_st["selected"].get("w1-reading") is True
                  and wwi_st.get("totalDays") == 18)
            pg.goto(BASE + "/planner.html?unit=ga"); settle(pg)
            check(S, "GA untouched by TW edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            ga_st = ls_json(pg, "hcg_unit_ga_v1")
            check(S, "GA saved state intact", ga_st and ga_st["selected"].get("g1-reading") is True
                  and ga_st.get("totalDays") == 18)
            pg.goto(BASE + "/planner.html"); settle(pg)
            check(S, "PE untouched by TW edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pe_st = ls_json(pg, "hcg_unit_v1")
            check(S, "PE saved state intact", pe_st and pe_st["selected"].get("l1-reading") is True)
            pg.goto(BASE + "/planner.html?unit=tw"); settle(pg)
            check(S, "TW edit persisted in its own key", "13 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            tw_st = ls_json(pg, "hcg_unit_tw_v1")
            pg.goto(BASE + "/planner.html?unit=dp"); settle(pg)
            check(S, "DP untouched by TW edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            dp_st = ls_json(pg, "hcg_unit_dp_v1")
            check(S, "DP saved state intact", dp_st and dp_st["selected"].get("d1-reading") is True
                  and dp_st.get("totalDays") == 18)
            pg.goto(BASE + "/planner.html?unit=tw"); settle(pg)
            check(S, "TW edit still persisted after DP visit", "13 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            check(S, "each unit key intact after switching",
                  all(ls_get(pg, k) for k in ["hcg_unit_v1", "hcg_unit_ga_v1", "hcg_unit_wwi_v1", "hcg_unit_tw_v1", "hcg_unit_dp_v1"]))
            ctx.close()

            # ---------------- Year planner ----------------
            S = "Year planner"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner-year.html"); settle(pg)
            def year_row(name):
                return pg.eval_on_selector_all("#units tr",
                    "els => els.map(e => e.textContent).find(t => t.includes(" + json.dumps(name) + ")) || ''")
            def year_days(name):
                return pg.eval_on_selector_all(
                    "#units tr",
                    "els => { const r = els.find(e => e.textContent.includes(" + json.dumps(name) + ")); "
                    "const i = r ? r.querySelector('input.daysin') : null; return i ? i.value : null; }")
            row = year_row("The Twenties")
            check(S, "TW band present with 18-day estimate label",
                  year_days("The Twenties") == "18" and "estimate" in row, f"row={row[:120]}")
            link = pg.eval_on_selector_all("#units tr a",
                                           "els => els.map(a => a.getAttribute('href')).filter(h => h && h.includes('unit=tw'))")
            check(S, "TW plan-it link", link == ["planner.html?unit=tw"], str(link))
            wwi_row = year_row("Imperialism and World War I")
            check(S, "WWI band still shows its 18-day estimate (regression)",
                  year_days("Imperialism and World War I") == "18" and "estimate" in wwi_row,
                  f"row={wwi_row[:120]}")
            # Feed it a shorter saved TW plan (17 days after dropping one core day)
            pg.goto(BASE + "/planner.html?unit=tw"); settle(pg)
            pg.click("#picker input[type=checkbox][data-id='t1-activity']"); pg.wait_for_timeout(200)
            st = ls_json(pg, "hcg_unit_tw_v1")
            check(S, "edited TW plan saves totalDays 17", st and st.get("totalDays") == 17,
                  json.dumps(st)[:120])
            pg.goto(BASE + "/planner-year.html"); settle(pg)
            row = year_row("The Twenties")
            check(S, "year planner shows fed length 17 from unit plan",
                  year_days("The Twenties") == "17" and "from your unit plan" in row, f"row={row[:120]}")
            row = year_row("Depression and New Deal")
            check(S, "DP band present with 18-day estimate label",
                  year_days("Depression and New Deal") == "18" and "estimate" in row, f"row={row[:120]}")
            link = pg.eval_on_selector_all("#units tr a",
                                           "els => els.map(a => a.getAttribute('href')).filter(h => h && h.includes('unit=dp'))")
            check(S, "DP plan-it link", link == ["planner.html?unit=dp"], str(link))
            pg.goto(BASE + "/planner.html?unit=dp"); settle(pg)
            pg.click("#picker input[type=checkbox][data-id='d1-activity']"); pg.wait_for_timeout(200)
            st = ls_json(pg, "hcg_unit_dp_v1")
            check(S, "edited DP plan saves totalDays 17", st and st.get("totalDays") == 17,
                  json.dumps(st)[:120])
            pg.goto(BASE + "/planner-year.html"); settle(pg)
            row = year_row("Depression and New Deal")
            check(S, "year planner shows DP fed length 17 from unit plan",
                  year_days("Depression and New Deal") == "17" and "from your unit plan" in row, f"row={row[:120]}")
            ctx.close()

            # ---------------- Home rendering ----------------
            S = "Home"
            for label, key, ids, name, pdf_as_link in [
                    ("DP", "hcg_unit_dp_v1", dp_core, "Depression and New Deal", False),
                    ("TW", "hcg_unit_tw_v1", tw_core, "The Twenties", False),
                    ("WWI", "hcg_unit_wwi_v1", wwi_core, "Imperialism and World War I", False),
                    ("GA", "hcg_unit_ga_v1", ga_core, "The Gilded Age", False),
                    ("PE", "hcg_unit_v1", pe_core, "The Progressive Era", True)]:
                ctx = browser.new_context()
                pg = ctx.new_page(); attach_errors(pg, [])
                pg.add_init_script(seed_plan_script(key, ids))
                pg.goto(BASE + "/home.html"); settle(pg)
                blocks = pg.text_content("#home-blocks")
                check(S, f"{label}: blocks render", not pg.eval_on_selector("#home-blocks", "e => e.hidden"))
                check(S, f"{label}: unit name renders", name in blocks, blocks[:200])
                check(S, f"{label}: lesson 2 reading filename present", "lesson-02-reading.pdf" in blocks,
                      blocks[:300])
                check(S, f"{label}: tomorrow is the test day", "Unit test" in pg.text_content("#block-tomorrow"),
                      pg.text_content("#block-tomorrow")[:200])
                check(S, f"{label}: week block names the unit", name in pg.text_content("#block-week"))
                pdf_hrefs = pg.eval_on_selector_all(
                    "#home-blocks a", "els => els.map(a => a.getAttribute('href') || '').filter(h => h.endsWith('.pdf'))")
                if pdf_as_link:
                    check(S, "PE: sample files stay public links",
                          pdf_hrefs and all(h.startswith("files/") for h in pdf_hrefs), str(pdf_hrefs)[:200])
                else:
                    check(S, f"{label}: no public pdf links for All-Access unit", pdf_hrefs == [],
                          str(pdf_hrefs)[:200])
                ctx.close()

            # ---------------- WWI outputs ----------------
            S = "WWI outputs"
            ctx = browser.new_context(accept_downloads=True)
            try:
                ctx.grant_permissions(["clipboard-read", "clipboard-write"], origin=BASE)
            except Exception:
                pass
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html?unit=wwi"); settle(pg)
            pg.evaluate("window.print = function () {};")
            pg.click("#print-week"); pg.wait_for_timeout(200)
            pa = pg.eval_on_selector("#printArea", "e => e.innerHTML")
            check(S, "print plan renders WWI", "Imperialism and World War I" in pa and "Unit test" in pa, pa[:150])
            pg.click("#print-sub"); pg.wait_for_timeout(200)
            pa = pg.eval_on_selector("#printArea", "e => e.innerHTML")
            check(S, "sub plan renders filenames as text",
                  "Substitute Plan" in pa and "lesson-01-reading.pdf" in pa and "unit-test.pdf" in pa, pa[:200])
            with pg.expect_download() as dl:
                pg.click("#export-ics")
            d = dl.value
            check(S, "ICS filename uses imperialism-wwi slug",
                  d.suggested_filename.startswith("imperialism-wwi-") and d.suggested_filename.endswith(".ics"),
                  d.suggested_filename)
            pth = "/tmp/wwi-test.ics"; d.save_as(pth)
            ics = open(pth).read()
            check(S, "ICS content names the unit", "Imperialism and World War I" in ics, ics[:200])
            with pg.expect_download() as dl2:
                pg.click("#export-plan")
            d2 = dl2.value
            check(S, "export filename", d2.suggested_filename == "hcg-unit-plan-imperialism-wwi.json",
                  d2.suggested_filename)
            pth2 = "/tmp/wwi-plan.json"; d2.save_as(pth2)
            exp = json.load(open(pth2))
            check(S, "export JSON carries unit wwi", exp.get("unit") == "wwi", str(exp.get("unit")))
            # Share link
            pg.click("#share-plan"); pg.wait_for_timeout(600)
            url = None
            try:
                url = pg.evaluate("navigator.clipboard.readText()")
            except Exception:
                url = None
            if not url or "#plan=" not in str(url):
                note = pg.text_content("#share-note")
                m = re.search(r"(https?://\S+#plan=\S+)", note or "")
                url = m.group(1) if m else None
            check(S, "share link carries unit wwi", bool(url) and "?unit=wwi#plan=" in url, str(url)[:120])
            if url:
                payload = url.split("#plan=")[1]
                pg2 = ctx.new_page(); attach_errors(pg2, [])
                pg2.goto(BASE + "/planner.html"); settle(pg2)
                pg2.goto(url); settle(pg2)
                check(S, "share link boots the WWI unit",
                      pg2.text_content("#unit-name").strip() == "Imperialism and World War I",
                      pg2.text_content("#unit-name"))
                pg2.close()
            # Import refusal: a GA plan file into the WWI planner
            before = ls_get(pg, "hcg_unit_wwi_v1")
            ga_file = "/tmp/ga-plan.json"
            with open(ga_file, "w") as f:
                json.dump({"unit": "ga", "selected": {"g1-reading": True},
                           "sections": [{"name": "Period 1", "start": "2026-10-26", "test": "2026-11-20",
                                         "dayTypes": {}, "pins": {}, "rotation": "daily", "period": 45}],
                           "splits": {}, "customItems": [], "order": None, "active": 0, "view": "list"}, f)
            dialogs = []
            pg.on("dialog", lambda dlg: (dialogs.append(dlg.message), dlg.accept()))
            pg.set_input_files("#import-plan", ga_file)
            pg.wait_for_timeout(600)
            check(S, "wrong-unit import refused with pointer",
                  any("Gilded Age" in m for m in dialogs), str(dialogs)[:200])
            check(S, "WWI state unchanged after refused import", ls_get(pg, "hcg_unit_wwi_v1") == before)
            ctx.close()

            # ---------------- Twenties outputs ----------------
            S = "TW outputs"
            ctx = browser.new_context(accept_downloads=True)
            try:
                ctx.grant_permissions(["clipboard-read", "clipboard-write"], origin=BASE)
            except Exception:
                pass
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html?unit=tw"); settle(pg)
            pg.evaluate("window.print = function () {};")
            pg.click("#print-week"); pg.wait_for_timeout(200)
            pa = pg.eval_on_selector("#printArea", "e => e.innerHTML")
            check(S, "print plan renders TW", "The Twenties" in pa and "Unit test" in pa, pa[:150])
            pg.click("#print-sub"); pg.wait_for_timeout(200)
            pa = pg.eval_on_selector("#printArea", "e => e.innerHTML")
            check(S, "sub plan renders filenames as text",
                  "Substitute Plan" in pa and "lesson-01-reading.pdf" in pa and "unit-test.pdf" in pa, pa[:200])
            with pg.expect_download() as dl:
                pg.click("#export-ics")
            d = dl.value
            check(S, "ICS filename uses twenties slug",
                  d.suggested_filename.startswith("twenties-") and d.suggested_filename.endswith(".ics"),
                  d.suggested_filename)
            pth = "/tmp/tw-test.ics"; d.save_as(pth)
            ics = open(pth).read()
            check(S, "ICS content names the unit",
                  "Twenties" in ics and "UID:hcg-tw-" in ics, ics[:200])
            with pg.expect_download() as dl2:
                pg.click("#export-plan")
            d2 = dl2.value
            check(S, "export filename", d2.suggested_filename == "hcg-unit-plan-twenties.json",
                  d2.suggested_filename)
            pth2 = "/tmp/tw-plan.json"; d2.save_as(pth2)
            exp = json.load(open(pth2))
            check(S, "export JSON carries unit tw", exp.get("unit") == "tw", str(exp.get("unit")))
            pg.click("#share-plan"); pg.wait_for_timeout(600)
            url = None
            try:
                url = pg.evaluate("navigator.clipboard.readText()")
            except Exception:
                url = None
            if not url or "#plan=" not in str(url):
                note = pg.text_content("#share-note")
                m = re.search(r"(https?://\S+#plan=\S+)", note or "")
                url = m.group(1) if m else None
            check(S, "share link carries unit tw", bool(url) and "?unit=tw#plan=" in url, str(url)[:120])
            if url:
                pg2 = ctx.new_page(); attach_errors(pg2, [])
                pg2.goto(BASE + "/planner.html"); settle(pg2)
                pg2.goto(url); settle(pg2)
                check(S, "share link boots the TW unit",
                      pg2.text_content("#unit-name").strip() == "The Twenties",
                      pg2.text_content("#unit-name"))
                pg2.close()
            before = ls_get(pg, "hcg_unit_tw_v1")
            ga_file = "/tmp/ga-plan.json"
            with open(ga_file, "w") as f:
                json.dump({"unit": "ga", "selected": {"g1-reading": True},
                           "sections": [{"name": "Period 1", "start": "2026-10-26", "test": "2026-11-20",
                                         "dayTypes": {}, "pins": {}, "rotation": "daily", "period": 45}],
                           "splits": {}, "customItems": [], "order": None, "active": 0, "view": "list"}, f)
            dialogs = []
            pg.on("dialog", lambda dlg: (dialogs.append(dlg.message), dlg.accept()))
            pg.set_input_files("#import-plan", ga_file)
            pg.wait_for_timeout(600)
            check(S, "wrong-unit import refused with pointer",
                  any("Gilded Age" in m for m in dialogs), str(dialogs)[:200])
            check(S, "TW state unchanged after refused import", ls_get(pg, "hcg_unit_tw_v1") == before)
            ctx.close()


            # ---------------- Depression and New Deal outputs ----------------
            S = "DP outputs"
            ctx = browser.new_context(accept_downloads=True)
            try:
                ctx.grant_permissions(["clipboard-read", "clipboard-write"], origin=BASE)
            except Exception:
                pass
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html?unit=dp"); settle(pg)
            pg.evaluate("window.print = function () {};")
            pg.click("#print-week"); pg.wait_for_timeout(200)
            pa = pg.eval_on_selector("#printArea", "e => e.innerHTML")
            check(S, "print plan renders DP", "Depression and New Deal" in pa and "Unit test" in pa, pa[:150])
            pg.click("#print-sub"); pg.wait_for_timeout(200)
            pa = pg.eval_on_selector("#printArea", "e => e.innerHTML")
            check(S, "sub plan renders filenames as text",
                  "Substitute Plan" in pa and "lesson-01-reading.pdf" in pa and "unit-test.pdf" in pa, pa[:200])
            with pg.expect_download() as dl:
                pg.click("#export-ics")
            d = dl.value
            check(S, "ICS filename uses depression-new-deal slug",
                  d.suggested_filename.startswith("depression-new-deal-") and d.suggested_filename.endswith(".ics"),
                  d.suggested_filename)
            pth = "/tmp/dp-test.ics"; d.save_as(pth)
            ics = open(pth).read()
            check(S, "ICS content names the unit",
                  "Depression and New Deal" in ics and "UID:hcg-dp-" in ics, ics[:200])
            with pg.expect_download() as dl2:
                pg.click("#export-plan")
            d2 = dl2.value
            check(S, "export filename", d2.suggested_filename == "hcg-unit-plan-depression-new-deal.json",
                  d2.suggested_filename)
            pth2 = "/tmp/dp-plan.json"; d2.save_as(pth2)
            exp = json.load(open(pth2))
            check(S, "export JSON carries unit dp", exp.get("unit") == "dp", str(exp.get("unit")))
            pg.click("#share-plan"); pg.wait_for_timeout(600)
            url = None
            try:
                url = pg.evaluate("navigator.clipboard.readText()")
            except Exception:
                url = None
            if not url or "#plan=" not in str(url):
                note = pg.text_content("#share-note")
                m = re.search(r"(https?://\S+#plan=\S+)", note or "")
                url = m.group(1) if m else None
            check(S, "share link carries unit dp", bool(url) and "?unit=dp#plan=" in url, str(url)[:120])
            if url:
                pg2 = ctx.new_page(); attach_errors(pg2, [])
                pg2.goto(BASE + "/planner.html"); settle(pg2)
                pg2.goto(url); settle(pg2)
                check(S, "share link boots the DP unit",
                      pg2.text_content("#unit-name").strip() == "Depression and New Deal",
                      pg2.text_content("#unit-name"))
                pg2.close()
            before = ls_get(pg, "hcg_unit_dp_v1")
            ga_file = "/tmp/ga-plan.json"
            with open(ga_file, "w") as f:
                json.dump({"unit": "ga", "selected": {"g1-reading": True},
                           "sections": [{"name": "Period 1", "start": "2026-10-26", "test": "2026-11-20",
                                         "dayTypes": {}, "pins": {}, "rotation": "daily", "period": 45}],
                           "splits": {}, "customItems": [], "order": None, "active": 0, "view": "list"}, f)
            dialogs = []
            pg.on("dialog", lambda dlg: (dialogs.append(dlg.message), dlg.accept()))
            pg.set_input_files("#import-plan", ga_file)
            pg.wait_for_timeout(600)
            check(S, "wrong-unit import refused with pointer",
                  any("Gilded Age" in m for m in dialogs), str(dialogs)[:200])
            check(S, "DP state unchanged after refused import", ls_get(pg, "hcg_unit_dp_v1") == before)
            ctx.close()

            # ---------------- Anonymous: no public WWI URLs ----------------
            S = "Anonymous WWI exposure"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html?unit=wwi"); settle(pg)
            pdf_hrefs = pg.eval_on_selector_all(
                "a", "els => els.map(a => a.getAttribute('href') || '').filter(h => h.endsWith('.pdf'))")
            check(S, "planner: zero pdf anchors", pdf_hrefs == [], str(pdf_hrefs)[:200])
            html = pg.content()
            check(S, "planner: no storage download URLs minted",
                  "firebasestorage" not in html and "storage.googleapis" not in html
                  and "data-storage" not in html)
            check(S, "planner: filenames show as text", "lesson-01-reading.pdf" in pg.text_content("body"))
            pg.goto(BASE + "/imperialism-wwi.html"); settle(pg)
            pdf_hrefs = pg.eval_on_selector_all(
                "a", "els => els.map(a => a.getAttribute('href') || '').filter(h => h.endsWith('.pdf'))")
            check(S, "unit page: zero pdf anchors for anonymous", pdf_hrefs == [], str(pdf_hrefs)[:200])
            ctx.close()

            # ---------------- Entitled stub ----------------
            S = "Entitled stub"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.route("https://stub.example/**",
                     lambda route: route.fulfill(status=200, content_type="text/html", body="stub download"))
            pg.goto(BASE + "/planner.html?unit=wwi"); settle(pg)
            pg.evaluate("""
              window.HCGAuth.entitlement = function () {
                return { paid: true, allAccess: true, status: "active" };
              };
              window.HCGFiles = { url: function (p) { return Promise.resolve("https://stub.example/" + p); } };
              window.HCGPlannerRefresh();
            """)
            pg.wait_for_timeout(400)
            stor = pg.eval_on_selector_all("a.ga-dl", "els => els.map(a => a.getAttribute('data-storage'))")
            check(S, "download controls appear", len(stor) > 0, str(len(stor)))
            check(S, "all controls mint hcg/imperialism-wwi/ paths",
                  bool(stor) and all(s and s.startswith("hcg/imperialism-wwi/") for s in stor),
                  str(stor)[:200])
            test_storage = pg.get_attribute("#test-action a.ga-dl", "data-storage")
            check(S, "test download uses the WWI test path",
                  test_storage == "hcg/imperialism-wwi/unit-test.pdf", str(test_storage))
            pg.click("#test-action a.ga-dl")
            pg.wait_for_timeout(800)
            check(S, "clicking mints the stub URL for the WWI test",
                  pg.url.startswith("https://stub.example/hcg/imperialism-wwi/unit-test.pdf"), pg.url)
            ctx.close()

            # ---------------- Anonymous: no public Twenties URLs ----------------
            S = "Anonymous TW exposure"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html?unit=tw"); settle(pg)
            pdf_hrefs = pg.eval_on_selector_all(
                "a", "els => els.map(a => a.getAttribute('href') || '').filter(h => h.endsWith('.pdf'))")
            check(S, "planner: zero pdf anchors", pdf_hrefs == [], str(pdf_hrefs)[:200])
            html = pg.content()
            check(S, "planner: no storage download URLs minted",
                  "firebasestorage" not in html and "storage.googleapis" not in html
                  and "data-storage" not in html)
            check(S, "planner: filenames show as text", "lesson-01-reading.pdf" in pg.text_content("body"))
            pg.goto(BASE + "/twenties.html"); settle(pg)
            pdf_hrefs = pg.eval_on_selector_all(
                "a", "els => els.map(a => a.getAttribute('href') || '').filter(h => h.endsWith('.pdf'))")
            check(S, "unit page: zero pdf anchors for anonymous", pdf_hrefs == [], str(pdf_hrefs)[:200])
            ctx.close()

            # ---------------- Entitled stub (Twenties) ----------------
            S = "Entitled stub (TW)"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.route("https://stub.example/**",
                     lambda route: route.fulfill(status=200, content_type="text/html", body="stub download"))
            pg.goto(BASE + "/planner.html?unit=tw"); settle(pg)
            pg.evaluate("""
              window.HCGAuth.entitlement = function () {
                return { paid: true, allAccess: true, status: "active" };
              };
              window.HCGFiles = { url: function (p) { return Promise.resolve("https://stub.example/" + p); } };
              window.HCGPlannerRefresh();
            """)
            pg.wait_for_timeout(400)
            stor = pg.eval_on_selector_all("a.ga-dl", "els => els.map(a => a.getAttribute('data-storage'))")
            check(S, "download controls appear", len(stor) > 0, str(len(stor)))
            check(S, "all controls mint hcg/twenties/ paths",
                  bool(stor) and all(s and s.startswith("hcg/twenties/") for s in stor),
                  str(stor)[:200])
            test_storage = pg.get_attribute("#test-action a.ga-dl", "data-storage")
            check(S, "test download uses the Twenties test path",
                  test_storage == "hcg/twenties/unit-test.pdf", str(test_storage))
            pg.click("#test-action a.ga-dl")
            pg.wait_for_timeout(800)
            check(S, "clicking mints the stub URL for the Twenties test",
                  pg.url.startswith("https://stub.example/hcg/twenties/unit-test.pdf"), pg.url)
            ctx.close()


            # ---------------- Anonymous: no public DP URLs ----------------
            S = "Anonymous DP exposure"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html?unit=dp"); settle(pg)
            pdf_hrefs = pg.eval_on_selector_all(
                "a", "els => els.map(a => a.getAttribute('href') || '').filter(h => h.endsWith('.pdf'))")
            check(S, "planner: zero pdf anchors", pdf_hrefs == [], str(pdf_hrefs)[:200])
            html = pg.content()
            check(S, "planner: no storage download URLs minted",
                  "firebasestorage" not in html and "storage.googleapis" not in html
                  and "data-storage" not in html)
            check(S, "planner: filenames show as text", "lesson-01-reading.pdf" in pg.text_content("body"))
            pg.goto(BASE + "/depression-new-deal.html"); settle(pg)
            pdf_hrefs = pg.eval_on_selector_all(
                "a", "els => els.map(a => a.getAttribute('href') || '').filter(h => h.endsWith('.pdf'))")
            check(S, "unit page: zero pdf anchors for anonymous", pdf_hrefs == [], str(pdf_hrefs)[:200])
            ctx.close()

            # ---------------- Entitled stub (Depression and New Deal) ----------------
            S = "Entitled stub (DP)"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.route("https://stub.example/**",
                     lambda route: route.fulfill(status=200, content_type="text/html", body="stub download"))
            pg.goto(BASE + "/planner.html?unit=dp"); settle(pg)
            pg.evaluate("""
              window.HCGAuth.entitlement = function () {
                return { paid: true, allAccess: true, status: "active" };
              };
              window.HCGFiles = { url: function (p) { return Promise.resolve("https://stub.example/" + p); } };
              window.HCGPlannerRefresh();
            """)
            pg.wait_for_timeout(400)
            stor = pg.eval_on_selector_all("a.ga-dl", "els => els.map(a => a.getAttribute('data-storage'))")
            check(S, "download controls appear", len(stor) > 0, str(len(stor)))
            check(S, "all controls mint hcg/depression-new-deal/ paths",
                  bool(stor) and all(s and s.startswith("hcg/depression-new-deal/") for s in stor),
                  str(stor)[:200])
            test_storage = pg.get_attribute("#test-action a.ga-dl", "data-storage")
            check(S, "test download uses the DP test path",
                  test_storage == "hcg/depression-new-deal/unit-test.pdf", str(test_storage))
            pg.click("#test-action a.ga-dl")
            pg.wait_for_timeout(800)
            check(S, "clicking mints the stub URL for the DP test",
                  pg.url.startswith("https://stub.example/hcg/depression-new-deal/unit-test.pdf"), pg.url)
            ctx.close()

            # ---------------- Zero errors, two widths ----------------
            S = "Zero errors / responsive"
            for width in (1440, 390):
                ctx = browser.new_context(viewport={"width": width, "height": 900})
                errs = []
                pg = ctx.new_page(); attach_errors(pg, errs)
                for path in ["/planner.html?unit=dp", "/planner.html?unit=tw", "/planner.html?unit=wwi", "/planner.html?unit=ga",
                             "/planner.html", "/planner-year.html", "/home.html"]:
                    pg.goto(BASE + path); settle(pg)
                pg.add_init_script(seed_plan_script("hcg_unit_wwi_v1", wwi_core))
                pg.goto(BASE + "/home.html"); settle(pg)
                pg.add_init_script(seed_plan_script("hcg_unit_tw_v1", tw_core))
                pg.goto(BASE + "/home.html"); settle(pg)
                pg.add_init_script(seed_plan_script("hcg_unit_dp_v1", dp_core))
                pg.goto(BASE + "/home.html"); settle(pg)
                re_errs = real_errors(errs)
                check(S, f"no console/page errors at {width}px", re_errs == [], "; ".join(re_errs)[:300])
                ctx.close()

            browser.close()
    finally:
        server.terminate()

    total_p = total_f = 0
    print("\n==== RESULTS ====")
    for suite, (p, f, fails) in RESULTS.items():
        print(f"{suite}: {p} passed, {f} failed")
        total_p += p; total_f += f
    print(f"TOTAL: {total_p} passed, {total_f} failed")
    return 1 if total_f else 0


if __name__ == "__main__":
    sys.exit(main())
