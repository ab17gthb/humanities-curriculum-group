#!/usr/bin/env python3
"""Phase 14 (Early Republic and Expansion planner integration) Playwright suite.

Serves site/public locally and checks, in the pattern of the Gilded Age
integration tests:
  - PE, GA, WWI, TW, DP, WW2, CW, and CR regression (the Phase 10 suites, switcher now 9 units)
  - Modern America fresh state via ?unit=ma and via the unit switcher; nine-unit isolation
  - Civil Rights fresh state via ?unit=cr and via the unit switcher
  - World War II fresh state via ?unit=ww2 and via the unit switcher
  - Cold War fresh state via ?unit=cw and via the unit switcher
  - state isolation across all nine units
  - year planner fed length and estimate label for the Twenties, Depression and New Deal, World War II, The Cold War, Civil Rights, and Modern America
  - teacher home rendering of seeded PE, GA, WWI, Twenties, Depression and New Deal, World War II, Cold War, Civil Rights, and Modern America plans
  - Twenties, Depression and New Deal, World War II, Cold War, Civil Rights, and Modern America outputs: print view, sub plan, ICS, share link, export, import refusal
  - TPSP picker contents (CW 29 entries led by dbq21; CR 39 entries led by dbq22; MA 31 entries led by dbq23;
  FD 30 entries led by dbq1 with dbq2 alongside; ER 26 entries led by dbq9 with dbq7 alongside)
  - Early Republic and Expansion fresh state via ?unit=er and via the unit switcher; twelve-unit isolation;
  year planner Early Republic band in the full and early shapes (absent in modern); ER outputs
  - anonymous state exposes no public Twenties, Depression and New Deal, World War II, Cold War, Civil Rights, or Modern America file URLs
  - entitled-stub download controls mint hcg/twenties/, hcg/depression-new-deal/, hcg/world-war-ii/, and hcg/cold-war/ URLs;
    CR checks add hcg/civil-rights/ controls and MA checks add hcg/modern-america/ controls minted from the same stub
  - zero console/page errors at 1440px and 390px

Run: python3 test_phase14_earlyrepublic.py  (playwright + chromium)
"""
import json
import os
import re
import subprocess
import sys
import time
import urllib.request

PUBLIC = os.path.expanduser("~/workspace/curriculum-planner/site/public")
PORT = 8946
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
            ww2_core = core_ids("HCG_WW2_ITEMS")
            cw_core = core_ids("HCG_CW_ITEMS")
            cr_core = core_ids("HCG_CR_ITEMS")
            ma_core = core_ids("HCG_MA_ITEMS")
            ca_core = core_ids("HCG_CA_ITEMS")
            fd_core = core_ids("HCG_FD_ITEMS")
            er_core = core_ids("HCG_ER_ITEMS")

            # ---------------- PE regression ----------------
            S = "PE regression"
            ctx = browser.new_context()
            errs = []
            pg = ctx.new_page(); attach_errors(pg, errs)
            pg.goto(BASE + "/planner.html"); settle(pg)
            check(S, "unit name PE", pg.text_content("#unit-name").strip() == "The Progressive Era",
                  pg.text_content("#unit-name"))
            check(S, "switcher offers 12 units",
                  pg.eval_on_selector_all("#unit-switch button", "els => els.length") == 12)
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


            # ---------------- World War II fresh via ?unit=ww2 ----------------
            S = "WW2 fresh (?unit=ww2)"
            ctx = browser.new_context()
            errs = []
            pg = ctx.new_page(); attach_errors(pg, errs)
            pg.goto(BASE + "/planner.html?unit=ww2"); settle(pg)
            check(S, "unit name WW2", pg.text_content("#unit-name").strip() == "World War II",
                  pg.text_content("#unit-name"))
            check(S, "essential question", "live up to the democracy" in pg.text_content("#unit-eq"),
                  pg.text_content("#unit-eq")[:100])
            check(S, "blueprint 15", pg.evaluate("Object.keys(window.HCG_WW2_BLUEPRINT).length") == 15)
            check(S, "lessons 8 with questions",
                  pg.evaluate("window.HCG_WW2_LESSONS.length === 8 && window.HCG_WW2_LESSONS.every(l => !!l.question)"))
            check(S, "items 50", pg.evaluate("window.HCG_WW2_ITEMS.length") == 50)
            n_boxes = pg.eval_on_selector_all("#picker input[type=checkbox]", "els => els.length")
            check(S, "picker shows 50 items", n_boxes == 50, str(n_boxes))
            check(S, "coverage 15 of 15 on fresh core plan", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            st = ls_json(pg, "hcg_unit_ww2_v1")
            check(S, "core totalDays 18", st and st.get("totalDays") == 18, json.dumps(st)[:160])
            topics_txt = pg.text_content("#standards")
            for label in ["The road to war and American entry",
                          "Mobilization and the home front",
                          "The global war: Europe and the Pacific",
                          "Democracy tested at home",
                          "Atrocity, the Holocaust, and war crimes",
                          "Victory, cost, and transformation"]:
                check(S, f"topic panel shows: {label[:40]}", label in topics_txt)
            ta = pg.text_content("#test-action").strip()
            href = pg.get_attribute("#test-action a", "href")
            check(S, "WW2 test panel points at its own unit page",
                  ta == "World War II unit test is part of All-Access. Subscribers download it from the World War II unit page." and href == "world-war-ii.html",
                  f"{ta} | {href}")
            pg.click("#btn-add-tpsp"); pg.wait_for_timeout(300)
            n_tpsp = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.length")
            check(S, "TPSP picker has 30 entries", n_tpsp == 30, str(n_tpsp))
            first = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.length ? els[0].textContent : ''")
            check(S, "picker leads with dbq20", "Did World War II Advance Freedom at Home as Well as Abroad?" in first, first[:100])
            pg.fill("#tpsp-q", "Quarantine"); pg.wait_for_timeout(300)
            filt = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.map(e => e.textContent).join(' ')")
            check(S, "picker search finds the carried Quarantine speech", "Quarantine" in filt, filt[:160])
            pg.fill("#tpsp-q", "Jaws"); pg.wait_for_timeout(300)
            filt = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.map(e => e.textContent).join(' ')")
            check(S, "picker search finds Into the Jaws of Death", "Into the Jaws of Death" in filt, filt[:160])
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


            # ---------------- WW2 switcher + six-unit isolation ----------------
            S = "WW2 switcher + six-unit isolation"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html"); settle(pg)
            pg.click("#unit-switch button[data-unit='ww2']")
            pg.wait_for_url("**unit=ww2**"); settle(pg)
            check(S, "switcher boots WW2", pg.text_content("#unit-name").strip() == "World War II")
            st = ls_json(pg, "hcg_unit_ww2_v1")
            check(S, "switcher fresh totalDays 18", st and st.get("totalDays") == 18)
            check(S, "switcher coverage 15 of 15", "15 of 15" in pg.text_content("#covtext"))
            # Edit WW2: drop Lesson 1's core (entries 1 and 2 lose their core coverage)
            for iid in ["v1-reading", "v1-notes", "v1-activity"]:
                pg.click(f"#picker input[type=checkbox][data-id='{iid}']")
                pg.wait_for_timeout(150)
            check(S, "WW2 edit drops coverage to 13 of 15", "13 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=dp"); settle(pg)
            check(S, "DP untouched by WW2 edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            dp_st = ls_json(pg, "hcg_unit_dp_v1")
            check(S, "DP saved state intact", dp_st and dp_st["selected"].get("d1-reading") is True
                  and dp_st.get("totalDays") == 18)
            pg.goto(BASE + "/planner.html?unit=wwi"); settle(pg)
            check(S, "WWI untouched by WW2 edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=ga"); settle(pg)
            check(S, "GA untouched by WW2 edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=tw"); settle(pg)
            check(S, "TW untouched by WW2 edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html"); settle(pg)
            check(S, "PE untouched by WW2 edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pe_st = ls_json(pg, "hcg_unit_v1")
            check(S, "PE saved state intact", pe_st and pe_st["selected"].get("l1-reading") is True)
            pg.goto(BASE + "/planner.html?unit=ww2"); settle(pg)
            check(S, "WW2 edit persisted in its own key", "13 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            check(S, "each unit key intact after switching",
                  all(ls_get(pg, k) for k in ["hcg_unit_v1", "hcg_unit_ga_v1", "hcg_unit_wwi_v1", "hcg_unit_tw_v1", "hcg_unit_dp_v1", "hcg_unit_ww2_v1"]))
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
            row = year_row("World War II")
            check(S, "WW2 band present with 18-day estimate label",
                  year_days("World War II") == "18" and "estimate" in row, f"row={row[:120]}")
            link = pg.eval_on_selector_all("#units tr a",
                                           "els => els.map(a => a.getAttribute('href')).filter(h => h && h.includes('unit=ww2'))")
            check(S, "WW2 plan-it link", link == ["planner.html?unit=ww2"], str(link))
            pg.goto(BASE + "/planner.html?unit=ww2"); settle(pg)
            pg.click("#picker input[type=checkbox][data-id='v1-activity']"); pg.wait_for_timeout(200)
            st = ls_json(pg, "hcg_unit_ww2_v1")
            check(S, "edited WW2 plan saves totalDays 17", st and st.get("totalDays") == 17,
                  json.dumps(st)[:120])
            pg.goto(BASE + "/planner-year.html"); settle(pg)
            row = year_row("World War II")
            check(S, "year planner shows WW2 fed length 17 from unit plan",
                  year_days("World War II") == "17" and "from your unit plan" in row, f"row={row[:120]}")
            row = year_row("The Cold War")
            check(S, "CW band present with 18-day estimate label",
                  year_days("The Cold War") == "18" and "estimate" in row, f"row={row[:120]}")
            link = pg.eval_on_selector_all("#units tr a",
                                           "els => els.map(a => a.getAttribute('href')).filter(h => h && h.includes('unit=cw'))")
            check(S, "CW plan-it link", link == ["planner.html?unit=cw"], str(link))
            pg.goto(BASE + "/planner.html?unit=cw"); settle(pg)
            pg.click("#picker input[type=checkbox][data-id='c1-activity']"); pg.wait_for_timeout(200)
            st = ls_json(pg, "hcg_unit_cw_v1")
            check(S, "edited CW plan saves totalDays 17", st and st.get("totalDays") == 17,
                  json.dumps(st)[:120])
            pg.goto(BASE + "/planner-year.html"); settle(pg)
            row = year_row("The Cold War")
            check(S, "year planner shows CW fed length 17 from unit plan",
                  year_days("The Cold War") == "17" and "from your unit plan" in row, f"row={row[:120]}")
            row = year_row("Civil Rights")
            check(S, "CR band present with 18-day estimate label",
                  year_days("Civil Rights") == "18" and "estimate" in row, f"row={row[:120]}")
            link = pg.eval_on_selector_all("#units tr a",
                                           "els => els.map(a => a.getAttribute('href')).filter(h => h && h.includes('unit=cr'))")
            check(S, "CR plan-it link", link == ["planner.html?unit=cr"], str(link))
            pg.goto(BASE + "/planner.html?unit=cr"); settle(pg)
            pg.click("#picker input[type=checkbox][data-id='r1-activity']"); pg.wait_for_timeout(200)
            st = ls_json(pg, "hcg_unit_cr_v1")
            check(S, "edited CR plan saves totalDays 17", st and st.get("totalDays") == 17,
                  json.dumps(st)[:120])
            pg.goto(BASE + "/planner-year.html"); settle(pg)
            row = year_row("Civil Rights")
            check(S, "year planner shows CR fed length 17 from unit plan",
                  year_days("Civil Rights") == "17" and "from your unit plan" in row, f"row={row[:120]}")
            row = year_row("Modern America")
            check(S, "MA band present with 18-day estimate label",
                  year_days("Modern America") == "18" and "estimate" in row, f"row={row[:120]}")
            link = pg.eval_on_selector_all("#units tr a",
                                           "els => els.map(a => a.getAttribute('href')).filter(h => h && h.includes('unit=ma'))")
            check(S, "MA plan-it link", link == ["planner.html?unit=ma"], str(link))
            pg.goto(BASE + "/planner.html?unit=ma"); settle(pg)
            pg.click("#picker input[type=checkbox][data-id='m1-activity']"); pg.wait_for_timeout(200)
            st = ls_json(pg, "hcg_unit_ma_v1")
            check(S, "edited MA plan saves totalDays 17", st and st.get("totalDays") == 17,
                  json.dumps(st)[:120])
            pg.goto(BASE + "/planner-year.html"); settle(pg)
            row = year_row("Modern America")
            check(S, "year planner shows MA fed length 17 from unit plan",
                  year_days("Modern America") == "17" and "from your unit plan" in row, f"row={row[:120]}")
            row = year_row("Colonial America")
            check(S, "CA band present with 18-day estimate label",
                  year_days("Colonial America") == "18" and "estimate" in row, f"row={row[:120]}")
            link = pg.eval_on_selector_all("#units tr a",
                                           "els => els.map(a => a.getAttribute('href')).filter(h => h && h.includes('unit=ca'))")
            check(S, "CA plan-it link", link == ["planner.html?unit=ca"], str(link))
            pg.goto(BASE + "/planner.html?unit=ca"); settle(pg)
            pg.click("#picker input[type=checkbox][data-id='a1-activity']"); pg.wait_for_timeout(200)
            st = ls_json(pg, "hcg_unit_ca_v1")
            check(S, "edited CA plan saves totalDays 17", st and st.get("totalDays") == 17,
                  json.dumps(st)[:120])
            pg.goto(BASE + "/planner-year.html"); settle(pg)
            row = year_row("Colonial America")
            check(S, "year planner shows CA fed length 17 from unit plan",
                  year_days("Colonial America") == "17" and "from your unit plan" in row, f"row={row[:120]}")
            row = year_row("The Founding")
            check(S, "FD band present with 18-day estimate label",
                  year_days("The Founding") == "18" and "estimate" in row, f"row={row[:120]}")
            link = pg.eval_on_selector_all("#units tr a",
                                           "els => els.map(a => a.getAttribute('href')).filter(h => h && h.includes('unit=fd'))")
            check(S, "FD plan-it link", link == ["planner.html?unit=fd"], str(link))
            pg.goto(BASE + "/planner.html?unit=fd"); settle(pg)
            pg.click("#picker input[type=checkbox][data-id='f1-activity']"); pg.wait_for_timeout(200)
            st = ls_json(pg, "hcg_unit_fd_v1")
            check(S, "edited FD plan saves totalDays 17", st and st.get("totalDays") == 17,
                  json.dumps(st)[:120])
            pg.goto(BASE + "/planner-year.html"); settle(pg)
            row = year_row("The Founding")
            check(S, "year planner shows FD fed length 17 from unit plan",
                  year_days("The Founding") == "17" and "from your unit plan" in row, f"row={row[:120]}")
            row = year_row("Early Republic and Expansion")
            check(S, "ER band present with 18-day estimate label",
                  year_days("Early Republic and Expansion") == "18" and "estimate" in row, f"row={row[:120]}")
            link = pg.eval_on_selector_all("#units tr a",
                                           "els => els.map(a => a.getAttribute('href')).filter(h => h && h.includes('unit=er'))")
            check(S, "ER plan-it link", link == ["planner.html?unit=er"], str(link))
            pg.goto(BASE + "/planner.html?unit=er"); settle(pg)
            pg.click("#picker input[type=checkbox][data-id='e1-activity']"); pg.wait_for_timeout(200)
            st = ls_json(pg, "hcg_unit_er_v1")
            check(S, "edited ER plan saves totalDays 17", st and st.get("totalDays") == 17,
                  json.dumps(st)[:120])
            pg.goto(BASE + "/planner-year.html"); settle(pg)
            row = year_row("Early Republic and Expansion")
            check(S, "year planner shows ER fed length 17 from unit plan",
                  year_days("Early Republic and Expansion") == "17" and "from your unit plan" in row, f"row={row[:120]}")
            # Early shape (to 1877): the CA band is present, modern units are not
            pg.select_option("#y-course", "early"); pg.wait_for_timeout(400)
            row = year_row("Colonial America")
            check(S, "early shape: CA band present", row != "" and "Colonial America" in row,
                  f"row={row[:120]}")
            check(S, "early shape: CA fed length 17 still read",
                  year_days("Colonial America") == "17", str(year_days("Colonial America")))
            check(S, "early shape: Reconstruction band present",
                  year_row("Reconstruction") != "")
            row = year_row("The Founding")
            check(S, "early shape: FD band present", row != "" and "The Founding" in row,
                  f"row={row[:120]}")
            check(S, "early shape: FD fed length 17 still read",
                  year_days("The Founding") == "17", str(year_days("The Founding")))
            row = year_row("Early Republic and Expansion")
            check(S, "early shape: ER band present", row != "" and "Early Republic and Expansion" in row,
                  f"row={row[:120]}")
            check(S, "early shape: ER fed length 17 still read",
                  year_days("Early Republic and Expansion") == "17", str(year_days("Early Republic and Expansion")))
            check(S, "early shape: Gilded Age band absent",
                  year_row("The Gilded Age") == "")
            check(S, "early shape: Modern America band absent",
                  year_row("Modern America") == "")
            pg.select_option("#y-course", "modern"); pg.wait_for_timeout(400)
            check(S, "modern shape: FD band absent",
                  year_row("The Founding") == "")
            check(S, "modern shape: ER band absent",
                  year_row("Early Republic and Expansion") == "")
            check(S, "modern shape: CA band absent",
                  year_row("Colonial America") == "")
            check(S, "modern shape: Gilded Age band present",
                  year_row("The Gilded Age") != "")
            pg.select_option("#y-course", "full"); pg.wait_for_timeout(400)
            check(S, "full shape restored: Modern America band back",
                  year_row("Modern America") != "")
            ctx.close()

            # ---------------- Home rendering ----------------
            S = "Home"
            for label, key, ids, name, pdf_as_link in [
                    ("ER", "hcg_unit_er_v1", er_core, "Early Republic and Expansion", False),
                    ("FD", "hcg_unit_fd_v1", fd_core, "The Founding", False),
                    ("CA", "hcg_unit_ca_v1", ca_core, "Colonial America", False),
                    ("MA", "hcg_unit_ma_v1", ma_core, "Modern America", False),
                    ("CR", "hcg_unit_cr_v1", cr_core, "Civil Rights", False),
                    ("CW", "hcg_unit_cw_v1", cw_core, "The Cold War", False),
                    ("WW2", "hcg_unit_ww2_v1", ww2_core, "World War II", False),
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


            # ---------------- World War II outputs ----------------
            S = "WW2 outputs"
            ctx = browser.new_context(accept_downloads=True)
            try:
                ctx.grant_permissions(["clipboard-read", "clipboard-write"], origin=BASE)
            except Exception:
                pass
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html?unit=ww2"); settle(pg)
            pg.evaluate("window.print = function () {};")
            pg.click("#print-week"); pg.wait_for_timeout(200)
            pa = pg.eval_on_selector("#printArea", "e => e.innerHTML")
            check(S, "print plan renders WW2", "World War II" in pa and "Unit test" in pa, pa[:150])
            pg.click("#print-sub"); pg.wait_for_timeout(200)
            pa = pg.eval_on_selector("#printArea", "e => e.innerHTML")
            check(S, "sub plan renders filenames as text",
                  "Substitute Plan" in pa and "lesson-01-reading.pdf" in pa and "unit-test.pdf" in pa, pa[:200])
            with pg.expect_download() as dl:
                pg.click("#export-ics")
            d = dl.value
            check(S, "ICS filename uses world-war-ii slug",
                  d.suggested_filename.startswith("world-war-ii-") and d.suggested_filename.endswith(".ics"),
                  d.suggested_filename)
            pth = "/tmp/ww2-test.ics"; d.save_as(pth)
            ics = open(pth).read()
            check(S, "ICS content names the unit",
                  "World War II" in ics and "UID:hcg-ww2-" in ics, ics[:200])
            with pg.expect_download() as dl2:
                pg.click("#export-plan")
            d2 = dl2.value
            check(S, "export filename", d2.suggested_filename == "hcg-unit-plan-world-war-ii.json",
                  d2.suggested_filename)
            pth2 = "/tmp/ww2-plan.json"; d2.save_as(pth2)
            exp = json.load(open(pth2))
            check(S, "export JSON carries unit ww2", exp.get("unit") == "ww2", str(exp.get("unit")))
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
            check(S, "share link carries unit ww2", bool(url) and "?unit=ww2#plan=" in url, str(url)[:120])
            if url:
                pg2 = ctx.new_page(); attach_errors(pg2, [])
                pg2.goto(BASE + "/planner.html"); settle(pg2)
                pg2.goto(url); settle(pg2)
                check(S, "share link boots the WW2 unit",
                      pg2.text_content("#unit-name").strip() == "World War II",
                      pg2.text_content("#unit-name"))
                pg2.close()
            before = ls_get(pg, "hcg_unit_ww2_v1")
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
            check(S, "WW2 state unchanged after refused import", ls_get(pg, "hcg_unit_ww2_v1") == before)
            ctx.close()

            # ---------------- Cold War fresh via ?unit=cw ----------------
            S = "CW fresh (?unit=cw)"
            ctx = browser.new_context()
            errs = []
            pg = ctx.new_page(); attach_errors(pg, errs)
            pg.goto(BASE + "/planner.html?unit=cw"); settle(pg)
            check(S, "unit name CW", pg.text_content("#unit-name").strip() == "The Cold War",
                  pg.text_content("#unit-name"))
            check(S, "essential question", "end the way it did" in pg.text_content("#unit-eq"),
                  pg.text_content("#unit-eq")[:100])
            check(S, "blueprint 15", pg.evaluate("Object.keys(window.HCG_CW_BLUEPRINT).length") == 15)
            check(S, "lessons 8 with questions",
                  pg.evaluate("window.HCG_CW_LESSONS.length === 8 && window.HCG_CW_LESSONS.every(l => !!l.question)"))
            check(S, "items 50", pg.evaluate("window.HCG_CW_ITEMS.length") == 50)
            n_boxes = pg.eval_on_selector_all("#picker input[type=checkbox]", "els => els.length")
            check(S, "picker shows 50 items", n_boxes == 50, str(n_boxes))
            check(S, "coverage 15 of 15 on fresh core plan", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            st = ls_json(pg, "hcg_unit_cw_v1")
            check(S, "core totalDays 18", st and st.get("totalDays") == 18, json.dumps(st)[:160])
            topics_txt = pg.text_content("#standards")
            for label in ["Origins and containment: the strategy takes shape",
                          "Asia and the wars of containment",
                          "Fear at home: anticommunism and American freedom",
                          "The nuclear arms race and the shadow it cast",
                          "Challenge and response: Cuba, Vietnam, détente, and the renewed confrontation",
                          "The Cold War ends: reform, collapse, and legacy",
                          "The Cold War, 1945\u20131991"]:
                check(S, f"topic panel shows: {label[:40]}", label in topics_txt)
            ta = pg.text_content("#test-action").strip()
            href = pg.get_attribute("#test-action a", "href")
            check(S, "CW test panel points at its own unit page",
                  ta == "The Cold War unit test is part of All-Access. Subscribers download it from the Cold War unit page." and href == "cold-war.html",
                  f"{ta} | {href}")
            pg.click("#btn-add-tpsp"); pg.wait_for_timeout(300)
            n_tpsp = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.length")
            check(S, "TPSP picker has 29 entries", n_tpsp == 29, str(n_tpsp))
            first = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.length ? els[0].textContent : ''")
            check(S, "picker leads with dbq21", "Did Containment Serve American Interests?" in first, first[:100])
            pg.fill("#tpsp-q", "Wheeling"); pg.wait_for_timeout(300)
            filt = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.map(e => e.textContent).join(' ')")
            check(S, "picker search finds the Wheeling speech", "Wheeling Speech" in filt, filt[:160])
            pg.fill("#tpsp-q", "Brandenburg"); pg.wait_for_timeout(300)
            filt = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.map(e => e.textContent).join(' ')")
            check(S, "picker search finds the Brandenburg Gate records", "Brandenburg Gate" in filt, filt[:160])
            pg.fill("#tpsp-q", ""); pg.wait_for_timeout(200)
            pg.click("#tpsp-close")
            check(S, "no page errors", not real_errors(errs), "; ".join(real_errors(errs))[:300])
            ctx.close()


            # ---------------- CW switcher + seven-unit isolation ----------------
            S = "CW switcher + seven-unit isolation"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html"); settle(pg)
            pg.click("#unit-switch button[data-unit='cw']")
            pg.wait_for_url("**unit=cw**"); settle(pg)
            check(S, "switcher boots CW", pg.text_content("#unit-name").strip() == "The Cold War")
            st = ls_json(pg, "hcg_unit_cw_v1")
            check(S, "switcher fresh totalDays 18", st and st.get("totalDays") == 18)
            check(S, "switcher coverage 15 of 15", "15 of 15" in pg.text_content("#covtext"))
            # Edit CW: drop Lesson 1's core (entries 1 and 2 lose their core coverage)
            for iid in ["c1-reading", "c1-notes", "c1-activity"]:
                pg.click(f"#picker input[type=checkbox][data-id='{iid}']")
                pg.wait_for_timeout(150)
            check(S, "CW edit drops coverage to 13 of 15", "13 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=ww2"); settle(pg)
            check(S, "WW2 untouched by CW edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            ww2_st = ls_json(pg, "hcg_unit_ww2_v1")
            check(S, "WW2 saved state intact", ww2_st and ww2_st["selected"].get("v1-reading") is True
                  and ww2_st.get("totalDays") == 18)
            pg.goto(BASE + "/planner.html?unit=dp"); settle(pg)
            check(S, "DP untouched by CW edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=wwi"); settle(pg)
            check(S, "WWI untouched by CW edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=ga"); settle(pg)
            check(S, "GA untouched by CW edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=tw"); settle(pg)
            check(S, "TW untouched by CW edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html"); settle(pg)
            check(S, "PE untouched by CW edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pe_st = ls_json(pg, "hcg_unit_v1")
            check(S, "PE saved state intact", pe_st and pe_st["selected"].get("l1-reading") is True)
            pg.goto(BASE + "/planner.html?unit=cw"); settle(pg)
            check(S, "CW edit persisted in its own key", "13 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            check(S, "each unit key intact after switching",
                  all(ls_get(pg, k) for k in ["hcg_unit_v1", "hcg_unit_ga_v1", "hcg_unit_wwi_v1", "hcg_unit_tw_v1", "hcg_unit_dp_v1", "hcg_unit_ww2_v1", "hcg_unit_cw_v1"]))
            ctx.close()


            # ---------------- Cold War outputs ----------------
            S = "CW outputs"
            ctx = browser.new_context(accept_downloads=True)
            try:
                ctx.grant_permissions(["clipboard-read", "clipboard-write"], origin=BASE)
            except Exception:
                pass
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html?unit=cw"); settle(pg)
            pg.evaluate("window.print = function () {};")
            pg.click("#print-week"); pg.wait_for_timeout(200)
            pa = pg.eval_on_selector("#printArea", "e => e.innerHTML")
            check(S, "print plan renders CW", "The Cold War" in pa and "Unit test" in pa, pa[:150])
            pg.click("#print-sub"); pg.wait_for_timeout(200)
            pa = pg.eval_on_selector("#printArea", "e => e.innerHTML")
            check(S, "sub plan renders filenames as text",
                  "Substitute Plan" in pa and "lesson-01-reading.pdf" in pa and "unit-test.pdf" in pa, pa[:200])
            with pg.expect_download() as dl:
                pg.click("#export-ics")
            d = dl.value
            check(S, "ICS filename uses cold-war slug",
                  d.suggested_filename.startswith("cold-war-") and d.suggested_filename.endswith(".ics"),
                  d.suggested_filename)
            pth = "/tmp/cw-test.ics"; d.save_as(pth)
            ics = open(pth).read()
            check(S, "ICS content names the unit",
                  "Cold War" in ics and "UID:hcg-cw-" in ics, ics[:200])
            with pg.expect_download() as dl2:
                pg.click("#export-plan")
            d2 = dl2.value
            check(S, "export filename", d2.suggested_filename == "hcg-unit-plan-cold-war.json",
                  d2.suggested_filename)
            pth2 = "/tmp/cw-plan.json"; d2.save_as(pth2)
            exp = json.load(open(pth2))
            check(S, "export JSON carries unit cw", exp.get("unit") == "cw", str(exp.get("unit")))
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
            check(S, "share link carries unit cw", bool(url) and "?unit=cw#plan=" in url, str(url)[:120])
            if url:
                pg2 = ctx.new_page(); attach_errors(pg2, [])
                pg2.goto(BASE + "/planner.html"); settle(pg2)
                pg2.goto(url); settle(pg2)
                check(S, "share link boots the CW unit",
                      pg2.text_content("#unit-name").strip() == "The Cold War",
                      pg2.text_content("#unit-name"))
                pg2.close()
            before = ls_get(pg, "hcg_unit_cw_v1")
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
            check(S, "CW state unchanged after refused import", ls_get(pg, "hcg_unit_cw_v1") == before)
            ctx.close()



            # ---------------- Civil Rights fresh via ?unit=cr ----------------
            S = "CR fresh (?unit=cr)"
            ctx = browser.new_context()
            errs = []
            pg = ctx.new_page(); attach_errors(pg, errs)
            pg.goto(BASE + "/planner.html?unit=cr"); settle(pg)
            check(S, "unit name CR", pg.text_content("#unit-name").strip() == "Civil Rights",
                  pg.text_content("#unit-name"))
            check(S, "essential question", "leave unfinished" in pg.text_content("#unit-eq"),
                  pg.text_content("#unit-eq")[:100])
            check(S, "blueprint 15", pg.evaluate("Object.keys(window.HCG_CR_BLUEPRINT).length") == 15)
            check(S, "lessons 8 with questions",
                  pg.evaluate("window.HCG_CR_LESSONS.length === 8 && window.HCG_CR_LESSONS.every(l => !!l.question)"))
            check(S, "items 50", pg.evaluate("window.HCG_CR_ITEMS.length") == 50)
            n_boxes = pg.eval_on_selector_all("#picker input[type=checkbox]", "els => els.length")
            check(S, "picker shows 50 items", n_boxes == 50, str(n_boxes))
            check(S, "coverage 15 of 15 on fresh core plan", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            st = ls_json(pg, "hcg_unit_cr_v1")
            check(S, "core totalDays 18", st and st.get("totalDays") == 18, json.dumps(st)[:160])
            topics_txt = pg.text_content("#standards")
            for label in ["The long groundwork: Jim Crow and the institutions that fought it",
                          "The courts and the Constitution: law as a movement weapon",
                          "Mass protest: nonviolent direct action and its makers",
                          "The federal government: ally, referee, and reluctant enforcer",
                          "The movement divides and widens: region, class, and visions of freedom",
                          "Legacy: what changed, what endured, what was left undone",
                          "Civil Rights, 1947\u20131978"]:
                check(S, f"topic panel shows: {label[:40]}", label in topics_txt)
            ta = pg.text_content("#test-action").strip()
            href = pg.get_attribute("#test-action a", "href")
            check(S, "CR test panel points at its own unit page",
                  ta == "Civil Rights unit test is part of All-Access. Subscribers download it from the Civil Rights unit page." and href == "civil-rights.html",
                  f"{ta} | {href}")
            pg.click("#btn-add-tpsp"); pg.wait_for_timeout(300)
            n_tpsp = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.length")
            check(S, "TPSP picker has 39 entries", n_tpsp == 39, str(n_tpsp))
            first = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.length ? els[0].textContent : ''")
            check(S, "picker leads with dbq22", "Did Black Americans in the 1960s Share One Vision of Freedom?" in first, first[:100])
            pg.fill("#tpsp-q", "Birmingham Jail"); pg.wait_for_timeout(300)
            filt = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.map(e => e.textContent).join(' ')")
            check(S, "picker search finds the Letter from Birmingham Jail", "Letter from Birmingham Jail" in filt, filt[:160])
            pg.fill("#tpsp-q", "9981"); pg.wait_for_timeout(300)
            filt = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.map(e => e.textContent).join(' ')")
            check(S, "picker search finds the carried Executive Order 9981", "Executive Order 9981" in filt, filt[:160])
            pg.fill("#tpsp-q", ""); pg.wait_for_timeout(200)
            pg.click("#tpsp-close")
            check(S, "no page errors", not real_errors(errs), "; ".join(real_errors(errs))[:300])
            ctx.close()


            # ---------------- CR switcher + eight-unit isolation ----------------
            S = "CR switcher + eight-unit isolation"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html"); settle(pg)
            pg.click("#unit-switch button[data-unit='cr']")
            pg.wait_for_url("**unit=cr**"); settle(pg)
            check(S, "switcher boots CR", pg.text_content("#unit-name").strip() == "Civil Rights")
            st = ls_json(pg, "hcg_unit_cr_v1")
            check(S, "switcher fresh totalDays 18", st and st.get("totalDays") == 18)
            check(S, "switcher coverage 15 of 15", "15 of 15" in pg.text_content("#covtext"))
            # Edit CR: drop Lesson 1's core (entries 1 and 2 lose their core coverage)
            for iid in ["r1-reading", "r1-notes", "r1-activity"]:
                pg.click(f"#picker input[type=checkbox][data-id='{iid}']")
                pg.wait_for_timeout(150)
            check(S, "CR edit drops coverage to 13 of 15", "13 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=cw"); settle(pg)
            check(S, "CW untouched by CR edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            cw_st = ls_json(pg, "hcg_unit_cw_v1")
            check(S, "CW saved state intact", cw_st and cw_st["selected"].get("c1-reading") is True
                  and cw_st.get("totalDays") == 18)
            pg.goto(BASE + "/planner.html?unit=ww2"); settle(pg)
            check(S, "WW2 untouched by CR edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=dp"); settle(pg)
            check(S, "DP untouched by CR edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=wwi"); settle(pg)
            check(S, "WWI untouched by CR edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=ga"); settle(pg)
            check(S, "GA untouched by CR edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=tw"); settle(pg)
            check(S, "TW untouched by CR edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html"); settle(pg)
            check(S, "PE untouched by CR edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pe_st = ls_json(pg, "hcg_unit_v1")
            check(S, "PE saved state intact", pe_st and pe_st["selected"].get("l1-reading") is True)
            pg.goto(BASE + "/planner.html?unit=cr"); settle(pg)
            check(S, "CR edit persisted in its own key", "13 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            check(S, "each unit key intact after switching",
                  all(ls_get(pg, k) for k in ["hcg_unit_v1", "hcg_unit_ga_v1", "hcg_unit_wwi_v1", "hcg_unit_tw_v1", "hcg_unit_dp_v1", "hcg_unit_ww2_v1", "hcg_unit_cw_v1", "hcg_unit_cr_v1"]))
            ctx.close()


            # ---------------- Civil Rights outputs ----------------
            S = "CR outputs"
            ctx = browser.new_context(accept_downloads=True)
            try:
                ctx.grant_permissions(["clipboard-read", "clipboard-write"], origin=BASE)
            except Exception:
                pass
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html?unit=cr"); settle(pg)
            pg.evaluate("window.print = function () {};")
            pg.click("#print-week"); pg.wait_for_timeout(200)
            pa = pg.eval_on_selector("#printArea", "e => e.innerHTML")
            check(S, "print plan renders CR", "Civil Rights" in pa and "Unit test" in pa, pa[:150])
            pg.click("#print-sub"); pg.wait_for_timeout(200)
            pa = pg.eval_on_selector("#printArea", "e => e.innerHTML")
            check(S, "sub plan renders filenames as text",
                  "Substitute Plan" in pa and "lesson-01-reading.pdf" in pa and "unit-test.pdf" in pa, pa[:200])
            with pg.expect_download() as dl:
                pg.click("#export-ics")
            d = dl.value
            check(S, "ICS filename uses civil-rights slug",
                  d.suggested_filename.startswith("civil-rights-") and d.suggested_filename.endswith(".ics"),
                  d.suggested_filename)
            pth = "/tmp/cr-test.ics"; d.save_as(pth)
            ics = open(pth).read()
            check(S, "ICS content names the unit",
                  "Civil Rights" in ics and "UID:hcg-cr-" in ics, ics[:200])
            with pg.expect_download() as dl2:
                pg.click("#export-plan")
            d2 = dl2.value
            check(S, "export filename", d2.suggested_filename == "hcg-unit-plan-civil-rights.json",
                  d2.suggested_filename)
            pth2 = "/tmp/cr-plan.json"; d2.save_as(pth2)
            exp = json.load(open(pth2))
            check(S, "export JSON carries unit cr", exp.get("unit") == "cr", str(exp.get("unit")))
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
            check(S, "share link carries unit cr", bool(url) and "?unit=cr#plan=" in url, str(url)[:120])
            if url:
                pg2 = ctx.new_page(); attach_errors(pg2, [])
                pg2.goto(BASE + "/planner.html"); settle(pg2)
                pg2.goto(url); settle(pg2)
                check(S, "share link boots the CR unit",
                      pg2.text_content("#unit-name").strip() == "Civil Rights",
                      pg2.text_content("#unit-name"))
                pg2.close()
            before = ls_get(pg, "hcg_unit_cr_v1")
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
            check(S, "CR state unchanged after refused import", ls_get(pg, "hcg_unit_cr_v1") == before)
            ctx.close()

            # ---------------- Modern America fresh via ?unit=ma ----------------
            S = "MA fresh (?unit=ma)"
            ctx = browser.new_context()
            errs = []
            pg = ctx.new_page(); attach_errors(pg, errs)
            pg.goto(BASE + "/planner.html?unit=ma"); settle(pg)
            check(S, "unit name MA", pg.text_content("#unit-name").strip() == "Modern America",
                  pg.text_content("#unit-name"))
            check(S, "essential question", "leave open" in pg.text_content("#unit-eq"),
                  pg.text_content("#unit-eq")[:100])
            check(S, "blueprint 15", pg.evaluate("Object.keys(window.HCG_MA_BLUEPRINT).length") == 15)
            check(S, "lessons 8 with questions",
                  pg.evaluate("window.HCG_MA_LESSONS.length === 8 && window.HCG_MA_LESSONS.every(l => !!l.question)"))
            check(S, "items 50", pg.evaluate("window.HCG_MA_ITEMS.length") == 50)
            n_boxes = pg.eval_on_selector_all("#picker input[type=checkbox]", "els => els.length")
            check(S, "picker shows 50 items", n_boxes == 50, str(n_boxes))
            check(S, "coverage 15 of 15 on fresh core plan", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            st = ls_json(pg, "hcg_unit_ma_v1")
            check(S, "core totalDays 18", st and st.get("totalDays") == 18, json.dumps(st)[:160])
            topics_txt = pg.text_content("#standards")
            for label in ["The conservative turn: small government and the market ascendancy",
                          "A new economy: globalization, technology, and the service age",
                          "A changing people: immigration, region, and the diversifying nation",
                          "America in the world after the Cold War: sole superpower to war on terror",
                          "Crisis and response: terror, financial collapse, and the tests of government",
                          "The unsettled present: polarization, rights, and the argument over the country's direction",
                          "Modern America, 1978\u2013present"]:
                check(S, f"topic panel shows: {label[:40]}", label in topics_txt)
            ta = pg.text_content("#test-action").strip()
            href = pg.get_attribute("#test-action a", "href")
            check(S, "MA test panel points at its own unit page",
                  ta == "Modern America unit test is part of All-Access. Subscribers download it from the Modern America unit page." and href == "modern-america.html",
                  f"{ta} | {href}")
            pg.click("#btn-add-tpsp"); pg.wait_for_timeout(300)
            n_tpsp = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.length")
            check(S, "TPSP picker has 31 entries", n_tpsp == 31, str(n_tpsp))
            first = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.length ? els[0].textContent : ''")
            check(S, "picker leads with dbq23", "Debated What the Country Should Be" in first, first[:120])
            pg.fill("#tpsp-q", "Crisis"); pg.wait_for_timeout(300)
            filt = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.map(e => e.textContent).join(' ')")
            check(S, "picker search finds the Crisis of Confidence address", "Crisis of Confidence" in filt, filt[:160])
            pg.fill("#tpsp-q", "Obergefell"); pg.wait_for_timeout(300)
            filt = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.map(e => e.textContent).join(' ')")
            check(S, "picker search finds Obergefell v. Hodges", "Obergefell v. Hodges" in filt, filt[:160])
            pg.fill("#tpsp-q", ""); pg.wait_for_timeout(200)
            pg.click("#tpsp-close")
            check(S, "no page errors", not real_errors(errs), "; ".join(real_errors(errs))[:300])
            ctx.close()


            # ---------------- MA switcher + nine-unit isolation ----------------
            S = "MA switcher + nine-unit isolation"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html"); settle(pg)
            pg.click("#unit-switch button[data-unit='ma']")
            pg.wait_for_url("**unit=ma**"); settle(pg)
            check(S, "switcher boots MA", pg.text_content("#unit-name").strip() == "Modern America")
            st = ls_json(pg, "hcg_unit_ma_v1")
            check(S, "switcher fresh totalDays 18", st and st.get("totalDays") == 18)
            check(S, "switcher coverage 15 of 15", "15 of 15" in pg.text_content("#covtext"))
            # Edit MA: drop Lesson 1's core (entries 1 and 2 lose their core coverage)
            for iid in ["m1-reading", "m1-notes", "m1-activity"]:
                pg.click(f"#picker input[type=checkbox][data-id='{iid}']")
                pg.wait_for_timeout(150)
            check(S, "MA edit drops coverage to 13 of 15", "13 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=cr"); settle(pg)
            check(S, "CR untouched by MA edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            cr_st = ls_json(pg, "hcg_unit_cr_v1")
            check(S, "CR saved state intact", cr_st and cr_st["selected"].get("r1-reading") is True
                  and cr_st.get("totalDays") == 18)
            pg.goto(BASE + "/planner.html?unit=cw"); settle(pg)
            check(S, "CW untouched by MA edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=ww2"); settle(pg)
            check(S, "WW2 untouched by MA edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=dp"); settle(pg)
            check(S, "DP untouched by MA edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=wwi"); settle(pg)
            check(S, "WWI untouched by MA edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=ga"); settle(pg)
            check(S, "GA untouched by MA edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=tw"); settle(pg)
            check(S, "TW untouched by MA edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html"); settle(pg)
            check(S, "PE untouched by MA edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pe_st = ls_json(pg, "hcg_unit_v1")
            check(S, "PE saved state intact", pe_st and pe_st["selected"].get("l1-reading") is True)
            pg.goto(BASE + "/planner.html?unit=ma"); settle(pg)
            check(S, "MA edit persisted in its own key", "13 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            check(S, "each unit key intact after switching",
                  all(ls_get(pg, k) for k in ["hcg_unit_v1", "hcg_unit_ga_v1", "hcg_unit_wwi_v1", "hcg_unit_tw_v1", "hcg_unit_dp_v1", "hcg_unit_ww2_v1", "hcg_unit_cw_v1", "hcg_unit_cr_v1", "hcg_unit_ma_v1"]))
            ctx.close()


            # ---------------- Modern America outputs ----------------
            S = "MA outputs"
            ctx = browser.new_context(accept_downloads=True)
            try:
                ctx.grant_permissions(["clipboard-read", "clipboard-write"], origin=BASE)
            except Exception:
                pass
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html?unit=ma"); settle(pg)
            pg.evaluate("window.print = function () {};")
            pg.click("#print-week"); pg.wait_for_timeout(200)
            pa = pg.eval_on_selector("#printArea", "e => e.innerHTML")
            check(S, "print plan renders MA", "Modern America" in pa and "Unit test" in pa, pa[:150])
            pg.click("#print-sub"); pg.wait_for_timeout(200)
            pa = pg.eval_on_selector("#printArea", "e => e.innerHTML")
            check(S, "sub plan renders filenames as text",
                  "Substitute Plan" in pa and "lesson-01-reading.pdf" in pa and "unit-test.pdf" in pa, pa[:200])
            with pg.expect_download() as dl:
                pg.click("#export-ics")
            d = dl.value
            check(S, "ICS filename uses modern-america slug",
                  d.suggested_filename.startswith("modern-america-") and d.suggested_filename.endswith(".ics"),
                  d.suggested_filename)
            pth = "/tmp/ma-test.ics"; d.save_as(pth)
            ics = open(pth).read()
            check(S, "ICS content names the unit",
                  "Modern America" in ics and "UID:hcg-ma-" in ics, ics[:200])
            with pg.expect_download() as dl2:
                pg.click("#export-plan")
            d2 = dl2.value
            check(S, "export filename", d2.suggested_filename == "hcg-unit-plan-modern-america.json",
                  d2.suggested_filename)
            pth2 = "/tmp/ma-plan.json"; d2.save_as(pth2)
            exp = json.load(open(pth2))
            check(S, "export JSON carries unit ma", exp.get("unit") == "ma", str(exp.get("unit")))
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
            check(S, "share link carries unit ma", bool(url) and "?unit=ma#plan=" in url, str(url)[:120])
            if url:
                pg2 = ctx.new_page(); attach_errors(pg2, [])
                pg2.goto(BASE + "/planner.html"); settle(pg2)
                pg2.goto(url); settle(pg2)
                check(S, "share link boots the MA unit",
                      pg2.text_content("#unit-name").strip() == "Modern America",
                      pg2.text_content("#unit-name"))
                pg2.close()
            before = ls_get(pg, "hcg_unit_ma_v1")
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
            check(S, "MA state unchanged after refused import", ls_get(pg, "hcg_unit_ma_v1") == before)
            ctx.close()


            # ---------------- Colonial America fresh via ?unit=ca ----------------
            S = "CA fresh (?unit=ca)"
            ctx = browser.new_context()
            errs = []
            pg = ctx.new_page(); attach_errors(pg, errs)
            pg.goto(BASE + "/planner.html?unit=ca"); settle(pg)
            check(S, "unit name CA", pg.text_content("#unit-name").strip() == "Colonial America",
                  pg.text_content("#unit-name"))
            check(S, "essential question", "remake all three worlds" in pg.text_content("#unit-eq"),
                  pg.text_content("#unit-eq")[:100])
            check(S, "blueprint 15", pg.evaluate("Object.keys(window.HCG_CA_BLUEPRINT).length") == 15)
            check(S, "lessons 8 with questions",
                  pg.evaluate("window.HCG_CA_LESSONS.length === 8 && window.HCG_CA_LESSONS.every(l => !!l.question)"))
            check(S, "items 50", pg.evaluate("window.HCG_CA_ITEMS.length") == 50)
            n_boxes = pg.eval_on_selector_all("#picker input[type=checkbox]", "els => els.length")
            check(S, "picker shows 50 items", n_boxes == 50, str(n_boxes))
            check(S, "coverage 15 of 15 on fresh core plan", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            st = ls_json(pg, "hcg_unit_ca_v1")
            check(S, "core totalDays 18", st and st.get("totalDays") == 18, json.dumps(st)[:160])
            topics_txt = pg.text_content("#standards")
            for label in ["Two worlds meet: the Americas and Europe before and at contact",
                          "Empires in America: Spain, France, and England compete",
                          "Regional colonial societies: Chesapeake, New England, and the Middle Colonies",
                          "The Atlantic system: trade, mercantilism, and enslaved labor",
                          "Colonial life: government, religion, and family",
                          "Empire tested: the imperial wars and the hinge of 1763",
                          "Colonial America, 1491\u20131763"]:
                check(S, f"topic panel shows: {label[:40]}", label in topics_txt)
            ta = pg.text_content("#test-action").strip()
            href = pg.get_attribute("#test-action a", "href")
            check(S, "CA test panel points at its own unit page",
                  ta == "Colonial America unit test is part of All-Access. Subscribers download it from the Colonial America unit page." and href == "colonial-america.html",
                  f"{ta} | {href}")
            pg.click("#btn-add-tpsp"); pg.wait_for_timeout(300)
            n_tpsp = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.length")
            check(S, "TPSP picker has 23 entries", n_tpsp == 23, str(n_tpsp))
            first = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.length ? els[0].textContent : ''")
            check(S, "picker leads with dbq13", "Did Colonial America Offer Liberty and Opportunity?" in first, first[:120])
            pg.fill("#tpsp-q", "Equiano"); pg.wait_for_timeout(300)
            filt = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.map(e => e.textContent).join(' ')")
            check(S, "picker search finds the Equiano Middle Passage record", "Middle Passage" in filt, filt[:160])
            pg.fill("#tpsp-q", "Join, or Die"); pg.wait_for_timeout(300)
            filt = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.map(e => e.textContent).join(' ')")
            check(S, "picker search finds Join, or Die", "Join, or Die" in filt, filt[:160])
            pg.fill("#tpsp-q", "Code Noir"); pg.wait_for_timeout(300)
            filt = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.map(e => e.textContent).join(' ')")
            check(S, "picker search finds the carried Code Noir", "Code Noir" in filt, filt[:160])
            pg.fill("#tpsp-q", ""); pg.wait_for_timeout(200)
            pg.click("#tpsp-close")
            check(S, "no page errors", not real_errors(errs), "; ".join(real_errors(errs))[:300])
            ctx.close()


            # ---------------- CA switcher + ten-unit isolation ----------------
            S = "CA switcher + ten-unit isolation"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html"); settle(pg)
            pg.click("#unit-switch button[data-unit='ca']")
            pg.wait_for_url("**unit=ca**"); settle(pg)
            check(S, "switcher boots CA", pg.text_content("#unit-name").strip() == "Colonial America")
            st = ls_json(pg, "hcg_unit_ca_v1")
            check(S, "switcher fresh totalDays 18", st and st.get("totalDays") == 18)
            check(S, "switcher coverage 15 of 15", "15 of 15" in pg.text_content("#covtext"))
            # Edit CA: drop Lesson 1's core (entries 1 and 2 lose their core coverage)
            for iid in ["a1-reading", "a1-notes", "a1-activity"]:
                pg.click(f"#picker input[type=checkbox][data-id='{iid}']")
                pg.wait_for_timeout(150)
            check(S, "CA edit drops coverage to 13 of 15", "13 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=ma"); settle(pg)
            check(S, "MA untouched by CA edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            ma_st = ls_json(pg, "hcg_unit_ma_v1")
            check(S, "MA saved state intact", ma_st and ma_st["selected"].get("m1-reading") is True
                  and ma_st.get("totalDays") == 18)
            pg.goto(BASE + "/planner.html?unit=cr"); settle(pg)
            check(S, "CR untouched by CA edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=cw"); settle(pg)
            check(S, "CW untouched by CA edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=ww2"); settle(pg)
            check(S, "WW2 untouched by CA edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=dp"); settle(pg)
            check(S, "DP untouched by CA edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=wwi"); settle(pg)
            check(S, "WWI untouched by CA edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=ga"); settle(pg)
            check(S, "GA untouched by CA edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=tw"); settle(pg)
            check(S, "TW untouched by CA edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html"); settle(pg)
            check(S, "PE untouched by CA edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pe_st = ls_json(pg, "hcg_unit_v1")
            check(S, "PE saved state intact", pe_st and pe_st["selected"].get("l1-reading") is True)
            pg.goto(BASE + "/planner.html?unit=ca"); settle(pg)
            check(S, "CA edit persisted in its own key", "13 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            check(S, "each unit key intact after switching",
                  all(ls_get(pg, k) for k in ["hcg_unit_v1", "hcg_unit_ga_v1", "hcg_unit_wwi_v1", "hcg_unit_tw_v1", "hcg_unit_dp_v1", "hcg_unit_ww2_v1", "hcg_unit_cw_v1", "hcg_unit_cr_v1", "hcg_unit_ma_v1", "hcg_unit_ca_v1"]))
            ctx.close()


            # ---------------- Colonial America outputs ----------------
            S = "CA outputs"
            ctx = browser.new_context(accept_downloads=True)
            try:
                ctx.grant_permissions(["clipboard-read", "clipboard-write"], origin=BASE)
            except Exception:
                pass
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html?unit=ca"); settle(pg)
            pg.evaluate("window.print = function () {};")
            pg.click("#print-week"); pg.wait_for_timeout(200)
            pa = pg.eval_on_selector("#printArea", "e => e.innerHTML")
            check(S, "print plan renders CA", "Colonial America" in pa and "Unit test" in pa, pa[:150])
            pg.click("#print-sub"); pg.wait_for_timeout(200)
            pa = pg.eval_on_selector("#printArea", "e => e.innerHTML")
            check(S, "sub plan renders filenames as text",
                  "Substitute Plan" in pa and "lesson-01-reading.pdf" in pa and "unit-test.pdf" in pa, pa[:200])
            with pg.expect_download() as dl:
                pg.click("#export-ics")
            d = dl.value
            check(S, "ICS filename uses colonial-america slug",
                  d.suggested_filename.startswith("colonial-america-") and d.suggested_filename.endswith(".ics"),
                  d.suggested_filename)
            pth = "/tmp/ca-test.ics"; d.save_as(pth)
            ics = open(pth).read()
            check(S, "ICS content names the unit",
                  "Colonial America" in ics and "UID:hcg-ca-" in ics, ics[:200])
            with pg.expect_download() as dl2:
                pg.click("#export-plan")
            d2 = dl2.value
            check(S, "export filename", d2.suggested_filename == "hcg-unit-plan-colonial-america.json",
                  d2.suggested_filename)
            pth2 = "/tmp/ca-plan.json"; d2.save_as(pth2)
            exp = json.load(open(pth2))
            check(S, "export JSON carries unit ca", exp.get("unit") == "ca", str(exp.get("unit")))
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
            check(S, "share link carries unit ca", bool(url) and "?unit=ca#plan=" in url, str(url)[:120])
            if url:
                pg2 = ctx.new_page(); attach_errors(pg2, [])
                pg2.goto(BASE + "/planner.html"); settle(pg2)
                pg2.goto(url); settle(pg2)
                check(S, "share link boots the CA unit",
                      pg2.text_content("#unit-name").strip() == "Colonial America",
                      pg2.text_content("#unit-name"))
                pg2.close()
            before = ls_get(pg, "hcg_unit_ca_v1")
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
            check(S, "CA state unchanged after refused import", ls_get(pg, "hcg_unit_ca_v1") == before)
            ctx.close()



            # ---------------- The Founding fresh via ?unit=fd ----------------
            S = "FD fresh (?unit=fd)"
            ctx = browser.new_context()
            errs = []
            pg = ctx.new_page(); attach_errors(pg, errs)
            pg.goto(BASE + "/planner.html?unit=fd"); settle(pg)
            check(S, "unit name FD", pg.text_content("#unit-name").strip() == "The Founding",
                  pg.text_content("#unit-name"))
            check(S, "essential question", "break with Britain" in pg.text_content("#unit-eq"),
                  pg.text_content("#unit-eq")[:100])
            check(S, "blueprint 15", pg.evaluate("Object.keys(window.HCG_FD_BLUEPRINT).length") == 15)
            check(S, "lessons 8 with questions",
                  pg.evaluate("window.HCG_FD_LESSONS.length === 8 && window.HCG_FD_LESSONS.every(l => !!l.question)"))
            check(S, "items 50", pg.evaluate("window.HCG_FD_ITEMS.length") == 50)
            n_boxes = pg.eval_on_selector_all("#picker input[type=checkbox]", "els => els.length")
            check(S, "picker shows 50 items", n_boxes == 50, str(n_boxes))
            check(S, "coverage 15 of 15 on fresh core plan", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            st = ls_json(pg, "hcg_unit_fd_v1")
            check(S, "core totalDays 18", st and st.get("totalDays") == 18, json.dumps(st)[:160])
            topics_txt = pg.text_content("#standards")
            for label in ["The empire after 1763: revenue, reform, and resistance",
                          "The road to revolution: protest becomes rebellion, 1773 to 1776",
                          "Independence declared: the ideas and the decision of 1776",
                          "The war for independence: campaigns, allies, and home fronts",
                          "The Confederation tested: governing the new republic in the 1780s",
                          "The Constitution: framing, ratifying, and the Bill of Rights",
                          "The Founding, 1763\u20131791"]:
                check(S, f"topic panel shows: {label[:40]}", label in topics_txt)
            ta = pg.text_content("#test-action").strip()
            href = pg.get_attribute("#test-action a", "href")
            check(S, "FD test panel points at its own unit page",
                  ta == "The Founding unit test is part of All-Access. Subscribers download it from the Founding unit page." and href == "the-founding.html",
                  f"{ta} | {href}")
            pg.click("#btn-add-tpsp"); pg.wait_for_timeout(300)
            n_tpsp = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.length")
            check(S, "TPSP picker has 30 entries", n_tpsp == 30, str(n_tpsp))
            first = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.length ? els[0].textContent : ''")
            check(S, "picker leads with dbq1", "Why Did the Colonies Break with Britain?" in first, first[:120])
            second = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.length > 1 ? els[1].textContent : ''")
            check(S, "picker has dbq2 alongside", "Whose Voices Counted in the Founding?" in second, second[:120])
            pg.fill("#tpsp-q", "Dunmore"); pg.wait_for_timeout(300)
            filt = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.map(e => e.textContent).join(' ')")
            check(S, "picker search finds Dunmore's Proclamation", "Dunmore" in filt, filt[:160])
            pg.fill("#tpsp-q", "stamped paper"); pg.wait_for_timeout(300)
            filt = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.map(e => e.textContent).join(' ')")
            check(S, "picker search finds the Stamp Act broadside", "stamped paper" in filt, filt[:160])
            pg.fill("#tpsp-q", ""); pg.wait_for_timeout(200)
            pg.click("#tpsp-close")
            check(S, "no page errors", not real_errors(errs), "; ".join(real_errors(errs))[:300])
            ctx.close()


            # ---------------- ER fresh ----------------
            S = "ER fresh (?unit=er)"
            ctx = browser.new_context()
            errs = []
            pg = ctx.new_page(); attach_errors(pg, errs)
            pg.goto(BASE + "/planner.html?unit=er"); settle(pg)
            check(S, "unit name ER", pg.text_content("#unit-name").strip() == "Early Republic and Expansion",
                  pg.text_content("#unit-name"))
            check(S, "essential question", "turn its Constitution into a working government" in pg.text_content("#unit-eq"),
                  pg.text_content("#unit-eq")[:100])
            check(S, "blueprint 15", pg.evaluate("Object.keys(window.HCG_ER_BLUEPRINT).length") == 15)
            check(S, "lessons 8 with questions",
                  pg.evaluate("window.HCG_ER_LESSONS.length === 8 && window.HCG_ER_LESSONS.every(l => !!l.question)"))
            check(S, "items 50", pg.evaluate("window.HCG_ER_ITEMS.length") == 50)
            n_boxes = pg.eval_on_selector_all("#picker input[type=checkbox]", "els => els.length")
            check(S, "picker shows 50 items", n_boxes == 50, str(n_boxes))
            check(S, "coverage 15 of 15 on fresh core plan", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            st = ls_json(pg, "hcg_unit_er_v1")
            check(S, "core totalDays 18", st and st.get("totalDays") == 18, json.dumps(st)[:160])
            topics_txt = pg.text_content("#standards")
            for label in ["Inventing a government: precedent, finance, and the first parties",
                          "The republic tested: dissent, succession, and the courts",
                          "A continental republic: purchase, exploration, and the peoples of the West",
                          "The second war and the nationalist turn",
                          "The Marshall Court and the national economy",
                          "Expansion and the question deferred: Monroe, Missouri, and Mexico",
                          "Early Republic and Expansion, 1789\u20131848"]:
                check(S, f"topic panel shows: {label[:40]}", label in topics_txt)
            ta = pg.text_content("#test-action").strip()
            href = pg.get_attribute("#test-action a", "href")
            check(S, "ER test panel points at its own unit page",
                  ta == "Early Republic and Expansion unit test is part of All-Access. Subscribers download it from the Early Republic unit page." and href == "early-republic.html",
                  f"{ta} | {href}")
            pg.click("#btn-add-tpsp"); pg.wait_for_timeout(300)
            n_tpsp = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.length")
            check(S, "TPSP picker has 26 entries", n_tpsp == 26, str(n_tpsp))
            first = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.length ? els[0].textContent : ''")
            check(S, "picker leads with dbq9", "Was Westward Expansion a Story of Opportunity or Conquest?" in first, first[:120])
            second = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.length > 1 ? els[1].textContent : ''")
            check(S, "picker has dbq7 alongside", "Did the Constitution Create a Democratic Government?" in second, second[:120])
            pg.fill("#tpsp-q", "Guadalupe"); pg.wait_for_timeout(300)
            filt = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.map(e => e.textContent).join(' ')")
            check(S, "picker search finds the Treaty of Guadalupe Hidalgo", "Guadalupe" in filt, filt[:160])
            pg.fill("#tpsp-q", "Farewell"); pg.wait_for_timeout(300)
            filt = pg.eval_on_selector_all("#tpsp-list .tpspitem", "els => els.map(e => e.textContent).join(' ')")
            check(S, "picker search finds the Farewell Address", "Farewell" in filt, filt[:160])
            pg.fill("#tpsp-q", ""); pg.wait_for_timeout(200)
            pg.click("#tpsp-close")
            check(S, "no page errors", not real_errors(errs), "; ".join(real_errors(errs))[:300])
            ctx.close()


            # ---------------- FD switcher + eleven-unit isolation ----------------
            S = "FD switcher + eleven-unit isolation"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html"); settle(pg)
            pg.click("#unit-switch button[data-unit='fd']")
            pg.wait_for_url("**unit=fd**"); settle(pg)
            check(S, "switcher boots FD", pg.text_content("#unit-name").strip() == "The Founding")
            st = ls_json(pg, "hcg_unit_fd_v1")
            check(S, "switcher fresh totalDays 18", st and st.get("totalDays") == 18)
            check(S, "switcher coverage 15 of 15", "15 of 15" in pg.text_content("#covtext"))
            # Edit FD: drop Lesson 1's core (entries 1 and 2 lose their core coverage)
            for iid in ["f1-reading", "f1-notes", "f1-activity"]:
                pg.click(f"#picker input[type=checkbox][data-id='{iid}']")
                pg.wait_for_timeout(150)
            check(S, "FD edit drops coverage to 13 of 15", "13 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=ca"); settle(pg)
            check(S, "CA untouched by FD edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            ca_st = ls_json(pg, "hcg_unit_ca_v1")
            check(S, "CA saved state intact", ca_st and ca_st["selected"].get("a1-reading") is True
                  and ca_st.get("totalDays") == 18)
            pg.goto(BASE + "/planner.html?unit=ma"); settle(pg)
            check(S, "MA untouched by FD edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=cr"); settle(pg)
            check(S, "CR untouched by FD edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=cw"); settle(pg)
            check(S, "CW untouched by FD edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=ww2"); settle(pg)
            check(S, "WW2 untouched by FD edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=dp"); settle(pg)
            check(S, "DP untouched by FD edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=wwi"); settle(pg)
            check(S, "WWI untouched by FD edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=ga"); settle(pg)
            check(S, "GA untouched by FD edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=tw"); settle(pg)
            check(S, "TW untouched by FD edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html"); settle(pg)
            check(S, "PE untouched by FD edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pe_st = ls_json(pg, "hcg_unit_v1")
            check(S, "PE saved state intact", pe_st and pe_st["selected"].get("l1-reading") is True)
            pg.goto(BASE + "/planner.html?unit=fd"); settle(pg)
            check(S, "FD edit persisted in its own key", "13 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            check(S, "each unit key intact after switching",
                  all(ls_get(pg, k) for k in ["hcg_unit_v1", "hcg_unit_ga_v1", "hcg_unit_wwi_v1", "hcg_unit_tw_v1", "hcg_unit_dp_v1", "hcg_unit_ww2_v1", "hcg_unit_cw_v1", "hcg_unit_cr_v1", "hcg_unit_ma_v1", "hcg_unit_ca_v1", "hcg_unit_fd_v1"]))
            ctx.close()


            # ---------------- ER switcher + twelve-unit isolation ----------------
            S = "ER switcher + twelve-unit isolation"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html"); settle(pg)
            pg.click("#unit-switch button[data-unit='er']")
            pg.wait_for_url("**unit=er**"); settle(pg)
            check(S, "switcher boots ER", pg.text_content("#unit-name").strip() == "Early Republic and Expansion")
            st = ls_json(pg, "hcg_unit_er_v1")
            check(S, "switcher fresh totalDays 18", st and st.get("totalDays") == 18)
            check(S, "switcher coverage 15 of 15", "15 of 15" in pg.text_content("#covtext"))
            # Edit ER: drop Lesson 1's core (entries 1 and 2 lose their core coverage)
            for iid in ["e1-reading", "e1-notes", "e1-activity"]:
                pg.click(f"#picker input[type=checkbox][data-id='{iid}']")
                pg.wait_for_timeout(150)
            check(S, "ER edit drops coverage to 13 of 15", "13 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=fd"); settle(pg)
            check(S, "FD untouched by ER edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=ca"); settle(pg)
            check(S, "CA untouched by ER edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=ma"); settle(pg)
            check(S, "MA untouched by ER edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=cr"); settle(pg)
            check(S, "CR untouched by ER edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=cw"); settle(pg)
            check(S, "CW untouched by ER edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=ww2"); settle(pg)
            check(S, "WW2 untouched by ER edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=dp"); settle(pg)
            check(S, "DP untouched by ER edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=wwi"); settle(pg)
            check(S, "WWI untouched by ER edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=ga"); settle(pg)
            check(S, "GA untouched by ER edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html?unit=tw"); settle(pg)
            check(S, "TW untouched by ER edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pg.goto(BASE + "/planner.html"); settle(pg)
            check(S, "PE untouched by ER edit", "15 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            pe_st = ls_json(pg, "hcg_unit_v1")
            check(S, "PE saved state intact", pe_st and pe_st["selected"].get("l1-reading") is True)
            pg.goto(BASE + "/planner.html?unit=er"); settle(pg)
            check(S, "ER edit persisted in its own key", "13 of 15" in pg.text_content("#covtext"),
                  pg.text_content("#covtext"))
            check(S, "each unit key intact after switching",
                  all(ls_get(pg, k) for k in ["hcg_unit_v1", "hcg_unit_ga_v1", "hcg_unit_wwi_v1", "hcg_unit_tw_v1", "hcg_unit_dp_v1", "hcg_unit_ww2_v1", "hcg_unit_cw_v1", "hcg_unit_cr_v1", "hcg_unit_ma_v1", "hcg_unit_ca_v1", "hcg_unit_fd_v1", "hcg_unit_er_v1"]))
            ctx.close()


            # ---------------- The Founding outputs ----------------
            S = "FD outputs"
            ctx = browser.new_context(accept_downloads=True)
            try:
                ctx.grant_permissions(["clipboard-read", "clipboard-write"], origin=BASE)
            except Exception:
                pass
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html?unit=fd"); settle(pg)
            pg.evaluate("window.print = function () {};")
            pg.click("#print-week"); pg.wait_for_timeout(200)
            pa = pg.eval_on_selector("#printArea", "e => e.innerHTML")
            check(S, "print plan renders FD", "The Founding" in pa and "Unit test" in pa, pa[:150])
            pg.click("#print-sub"); pg.wait_for_timeout(200)
            pa = pg.eval_on_selector("#printArea", "e => e.innerHTML")
            check(S, "sub plan renders filenames as text",
                  "Substitute Plan" in pa and "lesson-01-reading.pdf" in pa and "unit-test.pdf" in pa, pa[:200])
            with pg.expect_download() as dl:
                pg.click("#export-ics")
            d = dl.value
            check(S, "ICS filename uses the-founding slug",
                  d.suggested_filename.startswith("the-founding-") and d.suggested_filename.endswith(".ics"),
                  d.suggested_filename)
            pth = "/tmp/fd-test.ics"; d.save_as(pth)
            ics = open(pth).read()
            check(S, "ICS content names the unit",
                  "Founding" in ics and "UID:hcg-fd-" in ics, ics[:200])
            with pg.expect_download() as dl2:
                pg.click("#export-plan")
            d2 = dl2.value
            check(S, "export filename", d2.suggested_filename == "hcg-unit-plan-the-founding.json",
                  d2.suggested_filename)
            pth2 = "/tmp/fd-plan.json"; d2.save_as(pth2)
            exp = json.load(open(pth2))
            check(S, "export JSON carries unit fd", exp.get("unit") == "fd", str(exp.get("unit")))
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
            check(S, "share link carries unit fd", bool(url) and "?unit=fd#plan=" in url, str(url)[:120])
            if url:
                pg2 = ctx.new_page(); attach_errors(pg2, [])
                pg2.goto(BASE + "/planner.html"); settle(pg2)
                pg2.goto(url); settle(pg2)
                check(S, "share link boots the FD unit",
                      pg2.text_content("#unit-name").strip() == "The Founding",
                      pg2.text_content("#unit-name"))
                pg2.close()
            before = ls_get(pg, "hcg_unit_fd_v1")
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
            check(S, "FD state unchanged after refused import", ls_get(pg, "hcg_unit_fd_v1") == before)
            ctx.close()

            # ---------------- Early Republic and Expansion outputs ----------------
            S = "ER outputs"
            ctx = browser.new_context(accept_downloads=True)
            try:
                ctx.grant_permissions(["clipboard-read", "clipboard-write"], origin=BASE)
            except Exception:
                pass
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html?unit=er"); settle(pg)
            pg.evaluate("window.print = function () {};")
            pg.click("#print-week"); pg.wait_for_timeout(200)
            pa = pg.eval_on_selector("#printArea", "e => e.innerHTML")
            check(S, "print plan renders ER", "Early Republic and Expansion" in pa and "Unit test" in pa, pa[:150])
            pg.click("#print-sub"); pg.wait_for_timeout(200)
            pa = pg.eval_on_selector("#printArea", "e => e.innerHTML")
            check(S, "sub plan renders filenames as text",
                  "Substitute Plan" in pa and "lesson-01-reading.pdf" in pa and "unit-test.pdf" in pa, pa[:200])
            with pg.expect_download() as dl:
                pg.click("#export-ics")
            d = dl.value
            check(S, "ICS filename uses the early-republic slug",
                  d.suggested_filename.startswith("early-republic-") and d.suggested_filename.endswith(".ics"),
                  d.suggested_filename)
            pth = "/tmp/er-test.ics"; d.save_as(pth)
            ics = open(pth).read()
            check(S, "ICS content names the unit",
                  "Early Republic" in ics and "UID:hcg-er-" in ics, ics[:200])
            with pg.expect_download() as dl2:
                pg.click("#export-plan")
            d2 = dl2.value
            check(S, "export filename", d2.suggested_filename == "hcg-unit-plan-early-republic.json",
                  d2.suggested_filename)
            pth2 = "/tmp/er-plan.json"; d2.save_as(pth2)
            exp = json.load(open(pth2))
            check(S, "export JSON carries unit er", exp.get("unit") == "er", str(exp.get("unit")))
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
            check(S, "share link carries unit er", bool(url) and "?unit=er#plan=" in url, str(url)[:120])
            if url:
                pg2 = ctx.new_page(); attach_errors(pg2, [])
                pg2.goto(BASE + "/planner.html"); settle(pg2)
                pg2.goto(url); settle(pg2)
                check(S, "share link boots the ER unit",
                      pg2.text_content("#unit-name").strip() == "Early Republic and Expansion",
                      pg2.text_content("#unit-name"))
                pg2.close()
            before = ls_get(pg, "hcg_unit_er_v1")
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
            check(S, "ER state unchanged after refused import", ls_get(pg, "hcg_unit_er_v1") == before)
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


            # ---------------- Anonymous: no public WW2 URLs ----------------
            S = "Anonymous WW2 exposure"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html?unit=ww2"); settle(pg)
            pdf_hrefs = pg.eval_on_selector_all(
                "a", "els => els.map(a => a.getAttribute('href') || '').filter(h => h.endsWith('.pdf'))")
            check(S, "planner: zero pdf anchors", pdf_hrefs == [], str(pdf_hrefs)[:200])
            html = pg.content()
            check(S, "planner: no storage download URLs minted",
                  "firebasestorage" not in html and "storage.googleapis" not in html
                  and "data-storage" not in html)
            check(S, "planner: filenames show as text", "lesson-01-reading.pdf" in pg.text_content("body"))
            pg.goto(BASE + "/world-war-ii.html"); settle(pg)
            pdf_hrefs = pg.eval_on_selector_all(
                "a", "els => els.map(a => a.getAttribute('href') || '').filter(h => h.endsWith('.pdf'))")
            check(S, "unit page: zero pdf anchors for anonymous", pdf_hrefs == [], str(pdf_hrefs)[:200])
            ctx.close()

            # ---------------- Entitled stub (World War II) ----------------
            S = "Entitled stub (WW2)"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.route("https://stub.example/**",
                     lambda route: route.fulfill(status=200, content_type="text/html", body="stub download"))
            pg.goto(BASE + "/planner.html?unit=ww2"); settle(pg)
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
            check(S, "all controls mint hcg/world-war-ii/ paths",
                  bool(stor) and all(s and s.startswith("hcg/world-war-ii/") for s in stor),
                  str(stor)[:200])
            test_storage = pg.get_attribute("#test-action a.ga-dl", "data-storage")
            check(S, "test download uses the WW2 test path",
                  test_storage == "hcg/world-war-ii/unit-test.pdf", str(test_storage))
            pg.click("#test-action a.ga-dl")
            pg.wait_for_timeout(800)
            check(S, "clicking mints the stub URL for the WW2 test",
                  pg.url.startswith("https://stub.example/hcg/world-war-ii/unit-test.pdf"), pg.url)
            ctx.close()

            # ---------------- Anonymous: no public CW URLs ----------------
            S = "Anonymous CW exposure"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html?unit=cw"); settle(pg)
            pdf_hrefs = pg.eval_on_selector_all(
                "a", "els => els.map(a => a.getAttribute('href') || '').filter(h => h.endsWith('.pdf'))")
            check(S, "planner: zero pdf anchors", pdf_hrefs == [], str(pdf_hrefs)[:200])
            html = pg.content()
            check(S, "planner: no storage download URLs minted",
                  "firebasestorage" not in html and "storage.googleapis" not in html
                  and "data-storage" not in html)
            check(S, "planner: filenames show as text", "lesson-01-reading.pdf" in pg.text_content("body"))
            pg.goto(BASE + "/cold-war.html"); settle(pg)
            pdf_hrefs = pg.eval_on_selector_all(
                "a", "els => els.map(a => a.getAttribute('href') || '').filter(h => h.endsWith('.pdf'))")
            check(S, "unit page: zero pdf anchors for anonymous", pdf_hrefs == [], str(pdf_hrefs)[:200])
            ctx.close()

            # ---------------- Entitled stub (Cold War) ----------------
            S = "Entitled stub (CW)"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.route("https://stub.example/**",
                     lambda route: route.fulfill(status=200, content_type="text/html", body="stub download"))
            pg.goto(BASE + "/planner.html?unit=cw"); settle(pg)
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
            check(S, "all controls mint hcg/cold-war/ paths",
                  bool(stor) and all(s and s.startswith("hcg/cold-war/") for s in stor),
                  str(stor)[:200])
            test_storage = pg.get_attribute("#test-action a.ga-dl", "data-storage")
            check(S, "test download uses the CW test path",
                  test_storage == "hcg/cold-war/unit-test.pdf", str(test_storage))
            pg.click("#test-action a.ga-dl")
            pg.wait_for_timeout(800)
            check(S, "clicking mints the stub URL for the CW test",
                  pg.url.startswith("https://stub.example/hcg/cold-war/unit-test.pdf"), pg.url)
            ctx.close()
            # ---------------- Anonymous: no public CR URLs ----------------
            S = "Anonymous CR exposure"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html?unit=cr"); settle(pg)
            pdf_hrefs = pg.eval_on_selector_all(
                "a", "els => els.map(a => a.getAttribute('href') || '').filter(h => h.endsWith('.pdf'))")
            check(S, "planner: zero pdf anchors", pdf_hrefs == [], str(pdf_hrefs)[:200])
            html = pg.content()
            check(S, "planner: no storage download URLs minted",
                  "firebasestorage" not in html and "storage.googleapis" not in html
                  and "data-storage" not in html)
            check(S, "planner: filenames show as text", "lesson-01-reading.pdf" in pg.text_content("body"))
            pg.goto(BASE + "/civil-rights.html"); settle(pg)
            pdf_hrefs = pg.eval_on_selector_all(
                "a", "els => els.map(a => a.getAttribute('href') || '').filter(h => h.endsWith('.pdf'))")
            check(S, "unit page: zero pdf anchors for anonymous", pdf_hrefs == [], str(pdf_hrefs)[:200])
            ctx.close()

            # ---------------- Entitled stub (Civil Rights) ----------------
            S = "Entitled stub (CR)"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.route("https://stub.example/**",
                     lambda route: route.fulfill(status=200, content_type="text/html", body="stub download"))
            pg.goto(BASE + "/planner.html?unit=cr"); settle(pg)
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
            check(S, "all controls mint hcg/civil-rights/ paths",
                  bool(stor) and all(s and s.startswith("hcg/civil-rights/") for s in stor),
                  str(stor)[:200])
            test_storage = pg.get_attribute("#test-action a.ga-dl", "data-storage")
            check(S, "test download uses the CR test path",
                  test_storage == "hcg/civil-rights/unit-test.pdf", str(test_storage))
            pg.click("#test-action a.ga-dl")
            pg.wait_for_timeout(800)
            check(S, "clicking mints the stub URL for the CR test",
                  pg.url.startswith("https://stub.example/hcg/civil-rights/unit-test.pdf"), pg.url)
            ctx.close()

            # ---------------- Anonymous: no public MA URLs ----------------
            S = "Anonymous MA exposure"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html?unit=ma"); settle(pg)
            pdf_hrefs = pg.eval_on_selector_all(
                "a", "els => els.map(a => a.getAttribute('href') || '').filter(h => h.endsWith('.pdf'))")
            check(S, "planner: zero pdf anchors", pdf_hrefs == [], str(pdf_hrefs)[:200])
            html = pg.content()
            check(S, "planner: no storage download URLs minted",
                  "firebasestorage" not in html and "storage.googleapis" not in html
                  and "data-storage" not in html)
            check(S, "planner: filenames show as text", "lesson-01-reading.pdf" in pg.text_content("body"))
            pg.goto(BASE + "/modern-america.html"); settle(pg)
            pdf_hrefs = pg.eval_on_selector_all(
                "a", "els => els.map(a => a.getAttribute('href') || '').filter(h => h.endsWith('.pdf'))")
            check(S, "unit page: zero pdf anchors for anonymous", pdf_hrefs == [], str(pdf_hrefs)[:200])
            ctx.close()

            # ---------------- Entitled stub (Modern America) ----------------
            S = "Entitled stub (MA)"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.route("https://stub.example/**",
                     lambda route: route.fulfill(status=200, content_type="text/html", body="stub download"))
            pg.goto(BASE + "/planner.html?unit=ma"); settle(pg)
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
            check(S, "all controls mint hcg/modern-america/ paths",
                  bool(stor) and all(s and s.startswith("hcg/modern-america/") for s in stor),
                  str(stor)[:200])
            test_storage = pg.get_attribute("#test-action a.ga-dl", "data-storage")
            check(S, "test download uses the MA test path",
                  test_storage == "hcg/modern-america/unit-test.pdf", str(test_storage))
            pg.click("#test-action a.ga-dl")
            pg.wait_for_timeout(800)
            check(S, "clicking mints the stub URL for the MA test",
                  pg.url.startswith("https://stub.example/hcg/modern-america/unit-test.pdf"), pg.url)
            ctx.close()



            # ---------------- Anonymous: no public CA URLs ----------------
            S = "Anonymous CA exposure"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html?unit=ca"); settle(pg)
            pdf_hrefs = pg.eval_on_selector_all(
                "a", "els => els.map(a => a.getAttribute('href') || '').filter(h => h.endsWith('.pdf'))")
            check(S, "planner: zero pdf anchors", pdf_hrefs == [], str(pdf_hrefs)[:200])
            html = pg.content()
            check(S, "planner: no storage download URLs minted",
                  "firebasestorage" not in html and "storage.googleapis" not in html
                  and "data-storage" not in html)
            check(S, "planner: filenames show as text", "lesson-01-reading.pdf" in pg.text_content("body"))
            pg.goto(BASE + "/colonial-america.html"); settle(pg)
            pdf_hrefs = pg.eval_on_selector_all(
                "a", "els => els.map(a => a.getAttribute('href') || '').filter(h => h.endsWith('.pdf'))")
            check(S, "unit page: zero pdf anchors for anonymous", pdf_hrefs == [], str(pdf_hrefs)[:200])
            ctx.close()

            # ---------------- Entitled stub (Colonial America) ----------------
            S = "Entitled stub (CA)"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.route("https://stub.example/**",
                     lambda route: route.fulfill(status=200, content_type="text/html", body="stub download"))
            pg.goto(BASE + "/planner.html?unit=ca"); settle(pg)
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
            check(S, "all controls mint hcg/colonial-america/ paths",
                  bool(stor) and all(s and s.startswith("hcg/colonial-america/") for s in stor),
                  str(stor)[:200])
            test_storage = pg.get_attribute("#test-action a.ga-dl", "data-storage")
            check(S, "test download uses the CA test path",
                  test_storage == "hcg/colonial-america/unit-test.pdf", str(test_storage))
            pg.click("#test-action a.ga-dl")
            pg.wait_for_timeout(800)
            check(S, "clicking mints the stub URL for the CA test",
                  pg.url.startswith("https://stub.example/hcg/colonial-america/unit-test.pdf"), pg.url)
            ctx.close()



            # ---------------- Anonymous: no public FD URLs ----------------
            S = "Anonymous FD exposure"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html?unit=fd"); settle(pg)
            pdf_hrefs = pg.eval_on_selector_all(
                "a", "els => els.map(a => a.getAttribute('href') || '').filter(h => h.endsWith('.pdf'))")
            check(S, "planner: zero pdf anchors", pdf_hrefs == [], str(pdf_hrefs)[:200])
            html = pg.content()
            check(S, "planner: no storage download URLs minted",
                  "firebasestorage" not in html and "storage.googleapis" not in html
                  and "data-storage" not in html)
            check(S, "planner: filenames show as text", "lesson-01-reading.pdf" in pg.text_content("body"))
            pg.goto(BASE + "/the-founding.html"); settle(pg)
            pdf_hrefs = pg.eval_on_selector_all(
                "a", "els => els.map(a => a.getAttribute('href') || '').filter(h => h.endsWith('.pdf'))")
            check(S, "unit page: zero pdf anchors for anonymous", pdf_hrefs == [], str(pdf_hrefs)[:200])
            ctx.close()

            # ---------------- Entitled stub (The Founding) ----------------
            S = "Entitled stub (FD)"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.route("https://stub.example/**",
                     lambda route: route.fulfill(status=200, content_type="text/html", body="stub download"))
            pg.goto(BASE + "/planner.html?unit=fd"); settle(pg)
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
            check(S, "all controls mint hcg/the-founding/ paths",
                  bool(stor) and all(s and s.startswith("hcg/the-founding/") for s in stor),
                  str(stor)[:200])
            test_storage = pg.get_attribute("#test-action a.ga-dl", "data-storage")
            check(S, "test download uses the FD test path",
                  test_storage == "hcg/the-founding/unit-test.pdf", str(test_storage))
            pg.click("#test-action a.ga-dl")
            pg.wait_for_timeout(800)
            check(S, "clicking mints the stub URL for the FD test",
                  pg.url.startswith("https://stub.example/hcg/the-founding/unit-test.pdf"), pg.url)
            ctx.close()

            # ---------------- Anonymous: no public ER URLs ----------------
            S = "Anonymous ER exposure"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.goto(BASE + "/planner.html?unit=er"); settle(pg)
            pdf_hrefs = pg.eval_on_selector_all(
                "a", "els => els.map(a => a.getAttribute('href') || '').filter(h => h.endsWith('.pdf'))")
            check(S, "planner: zero pdf anchors", pdf_hrefs == [], str(pdf_hrefs)[:200])
            html = pg.content()
            check(S, "planner: no storage download URLs minted",
                  "firebasestorage" not in html and "storage.googleapis" not in html
                  and "data-storage" not in html)
            check(S, "planner: filenames show as text", "lesson-01-reading.pdf" in pg.text_content("body"))
            pg.goto(BASE + "/early-republic.html"); settle(pg)
            pdf_hrefs = pg.eval_on_selector_all(
                "a", "els => els.map(a => a.getAttribute('href') || '').filter(h => h.endsWith('.pdf'))")
            check(S, "unit page: zero pdf anchors for anonymous", pdf_hrefs == [], str(pdf_hrefs)[:200])
            ctx.close()

            # ---------------- Entitled stub (Early Republic and Expansion) ----------------
            S = "Entitled stub (ER)"
            ctx = browser.new_context()
            pg = ctx.new_page(); attach_errors(pg, [])
            pg.route("https://stub.example/**",
                     lambda route: route.fulfill(status=200, content_type="text/html", body="stub download"))
            pg.goto(BASE + "/planner.html?unit=er"); settle(pg)
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
            check(S, "all controls mint hcg/early-republic/ paths",
                  bool(stor) and all(s and s.startswith("hcg/early-republic/") for s in stor),
                  str(stor)[:200])
            test_storage = pg.get_attribute("#test-action a.ga-dl", "data-storage")
            check(S, "test download uses the ER test path",
                  test_storage == "hcg/early-republic/unit-test.pdf", str(test_storage))
            pg.click("#test-action a.ga-dl")
            pg.wait_for_timeout(800)
            check(S, "clicking mints the stub URL for the ER test",
                  pg.url.startswith("https://stub.example/hcg/early-republic/unit-test.pdf"), pg.url)
            ctx.close()

            # ---------------- Zero errors, two widths ----------------
            S = "Zero errors / responsive"
            for width in (1440, 390):
                ctx = browser.new_context(viewport={"width": width, "height": 900})
                errs = []
                pg = ctx.new_page(); attach_errors(pg, errs)
                for path in ["/planner.html?unit=er", "/planner.html?unit=fd", "/planner.html?unit=ca", "/planner.html?unit=ma", "/planner.html?unit=cr", "/planner.html?unit=cw", "/planner.html?unit=ww2", "/planner.html?unit=dp", "/planner.html?unit=tw", "/planner.html?unit=wwi", "/planner.html?unit=ga",
                             "/planner.html", "/planner-year.html", "/home.html"]:
                    pg.goto(BASE + path); settle(pg)
                pg.add_init_script(seed_plan_script("hcg_unit_wwi_v1", wwi_core))
                pg.goto(BASE + "/home.html"); settle(pg)
                pg.add_init_script(seed_plan_script("hcg_unit_tw_v1", tw_core))
                pg.goto(BASE + "/home.html"); settle(pg)
                pg.add_init_script(seed_plan_script("hcg_unit_dp_v1", dp_core))
                pg.goto(BASE + "/home.html"); settle(pg)
                pg.add_init_script(seed_plan_script("hcg_unit_ww2_v1", ww2_core))
                pg.goto(BASE + "/home.html"); settle(pg)
                pg.add_init_script(seed_plan_script("hcg_unit_cw_v1", cw_core))
                pg.goto(BASE + "/home.html"); settle(pg)
                pg.add_init_script(seed_plan_script("hcg_unit_cr_v1", cr_core))
                pg.goto(BASE + "/home.html"); settle(pg)
                pg.add_init_script(seed_plan_script("hcg_unit_ma_v1", ma_core))
                pg.goto(BASE + "/home.html"); settle(pg)
                pg.add_init_script(seed_plan_script("hcg_unit_ca_v1", ca_core))
                pg.goto(BASE + "/home.html"); settle(pg)
                pg.add_init_script(seed_plan_script("hcg_unit_fd_v1", fd_core))
                pg.goto(BASE + "/home.html"); settle(pg)
                pg.add_init_script(seed_plan_script("hcg_unit_er_v1", er_core))
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
