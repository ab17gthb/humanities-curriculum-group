#!/usr/bin/env python3
"""Crossword generator for the Modern America review day.

Places answers greedily on a shared letter grid so that every word
crosses at least one word already placed, checks the finished grid
programmatically (every answer must spell correctly in the grid and
every crossing letter must agree), then writes review-crossword.html
with an empty student grid, Across and Down clue lists, and a filled
teacher key on its own page. Run: python3 crossword-build.py
"""
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 13  # fixed so the published grid is reproducible; chosen after a seed search (seeds 0 to 30 all placed all 56 answers) for the compact, near square 49 x 51 grid with the smallest maximum dimension, so the cells stay as large as the page allows

# (answer, clue) -- answers are run together with no spaces, as in the pilot.
# The pool is this unit's 56 vocabulary terms from build-scripts/unit-spec.md;
# clues are shortened forms of the spec definitions or factual clues.
POOL = [
    ('CITIZENSUNITEDVFEDERALELECTIONCOMMISSION', 'The Supreme Court decision of 2010 holding that the government may not limit independent political spending by corporations and unions'),
    ('IMMIGRATIONREFORMANDCONTROLACTOF1986', 'The law that granted legal status to about three million unauthorized immigrants already in the country and made it illegal for employers knowingly to hire unauthorized workers'),
    ('IMMIGRATIONANDNATIONALITYACTOF1965', 'The law that ended the national origins quota system and opened American immigration chiefly to family reunification and needed skills'),
    ('AUTHORIZATIONFORUSEOFMILITARYFORCE', 'The law Congress passed on September 18, 2001 authorizing the president to use force against those responsible for the September 11 attacks'),
    ('NORTHAMERICANFREETRADEAGREEMENT', 'The agreement among the United States, Canada, and Mexico that took effect in 1994 and removed most tariffs and trade barriers among the three'),
    ('DEPARTMENTOFHOMELANDSECURITY', 'The cabinet department created in 2002 that merged twenty two federal agencies and offices charged with protecting the country against terrorist attack'),
    ('TROUBLEDASSETRELIEFPROGRAM', 'The program of October 2008, known as TARP, in which the federal government was authorized to spend up to seven hundred billion dollars to steady the banking system'),
    ('WEAPONSOFMASSDESTRUCTION', 'Chemical, biological, and nuclear weapons; no Iraqi stockpiles of them were found after the invasion of 2003'),
    ('DISTRICTOFCOLUMBIAVHELLER', 'The Supreme Court decision of 2008 holding that the Second Amendment protects an individual right to keep a handgun in the home for self-defense'),
    ('SUPPLYSIDEECONOMICS', 'The economic theory behind the Reagan program, holding that cutting tax rates and reducing regulation would grow the whole economy'),
    ('POLITICALPOLARIZATION', 'The sorting of Americans into two hostile political camps with fewer voters in the middle'),
    ('DEINDUSTRIALIZATION', 'The long decline of manufacturing employment in the United States as factories closed, automated, or moved abroad'),
    ('SEPTEMBER11ATTACKS', 'The terrorist attacks of 2001 in which al Qaeda hijackers flew passenger planes into the World Trade Center and the Pentagon, killing 2,977 people'),
    ('AFFIRMATIVEACTION', 'Government policies that take race into account in hiring, contracting, and college admissions in order to remedy the effects of past discrimination'),
    ('OBERGEFELLVHODGES', 'The Supreme Court decision of 2015 holding that the Fourteenth Amendment requires every state to license marriages between two people of the same sex'),
    ('PERSONALCOMPUTER', 'A computer built for one person\'s desk and home, sold in large numbers from the late 1970s onward'),
    ('SUBPRIMEMORTGAGE', 'A home loan made to a borrower with weak credit at a higher interest rate, issued in large numbers during the housing boom of the 2000s'),
    ('GREATRECESSION', 'The economic collapse of 2007 to 2009, the deepest since the Great Depression, in which unemployment reached ten percent'),
    ('AFFORDABLECAREACT', 'The health care law of 2010 that barred insurers from denying coverage for prior illness and expanded Medicaid'),
    ('SOUTHERNSTRATEGY', 'The Republican electoral strategy of the Nixon years that sought white southern voters by opposing federal civil rights enforcement, busing, and the pace of change'),
    ('IRANCONTRAAFFAIR', 'The scandal of 1985 to 1987 in which officials secretly sold arms to Iran and diverted the proceeds to the Contra rebels in Nicaragua'),
    ('MORALMAJORITY', 'The political organization founded by the Reverend Jerry Falwell in 1979 to mobilize evangelical Christian voters'),
    ('PERSIANGULFWAR', 'The war of January and February 1991 in which an American-led coalition drove Iraq\'s army out of Kuwait in six weeks'),
    ('GENTRIFICATION', 'The movement of wealthier residents and new investment into poorer city neighborhoods, raising prices and rents'),
    ('PEACEDIVIDEND', 'The money and attention Americans expected to redirect from military spending to needs at home once the Cold War ended in 1991'),
    ('COVID19PANDEMIC', 'The worldwide spread of the coronavirus disease first identified in 2019, which reached the United States in 2020 and killed more than a million Americans'),
    ('TEAPARTYMOVEMENT', 'The conservative protest movement that rose in 2009 against the bank bailouts, the stimulus, and the health care law'),
    ('OCCUPYWALLSTREET', 'The protest movement that began in New York in September 2011, camping in financial districts to protest economic inequality in the name of the ninety nine percent'),
    ('ENERGYCRISIS', 'The shortages and sharp price rises in oil and gasoline that struck the United States in 1973 and again in 1979'),
    ('REAGANDEMOCRAT', 'A traditionally Democratic voter, often a white working class or union voter, who voted for Ronald Reagan in 1980 and 1984'),
    ('FEDERALDEFICIT', 'The amount by which a year\'s federal spending exceeds the year\'s revenue, added each year to the national debt'),
    ('DIGITALDIVIDE', 'The gap between Americans with ready access to computers and the Internet and those without'),
    ('GLOBALIZATION', 'The deepening connection of the world\'s economies through trade, investment, and production spread across borders'),
    ('SERVICECONOMY', 'An economy in which most jobs produce services, such as health care, retail, finance, and food, rather than goods'),
    ('DOTCOMBUBBLE', 'The speculative boom in Internet company stocks in the late 1990s, ending in a crash in 2000 and 2001 that erased trillions in paper wealth'),
    ('PROPOSITION13', 'The California ballot measure of 1978 that cut property taxes sharply and capped their future growth, the opening victory of the national tax revolt'),
    ('DEREGULATION', 'The removal or loosening of government rules on an industry, pursued in airlines, trucking, banking, and communications'),
    ('USAPATRIOTACT', 'The law of October 2001 that widened the government\'s powers of surveillance, search, and detention in terrorism investigations'),
    ('STAGFLATION', 'The combination of stagnant economic growth, high unemployment, and high inflation that afflicted the American economy in the 1970s'),
    ('WARONTERROR', 'The worldwide campaign of military action, intelligence work, and security measures the United States declared after September 11, 2001'),
    ('PATCOSTRIKE', 'The strike of August 1981 in which President Reagan fired more than eleven thousand federal air traffic controllers who had struck illegally'),
    ('BUSHVGORE', 'The Supreme Court decision of December 2000 that stopped the recount of Florida\'s presidential ballots and settled the election of 2000'),
    ('SOCIALMEDIA', 'The Internet platforms, growing from the middle 2000s, on which users publish their own words, photographs, and video'),
    ('WHITEFLIGHT', 'The movement of white families from cities to suburbs in the decades after the Second World War, which shrank city tax bases'),
    ('OUTSOURCING', 'The practice of moving work, especially factory production and later office and service jobs, to lower-cost workers in other countries'),
    ('TAXREVOLT', 'The movement of the late 1970s in which voters demanded lower taxes and limits on government spending, beginning with California\'s Proposition 13 in 1978'),
    ('WARONDRUGS', 'The campaign of intensified drug enforcement and mandatory sentences greatly expanded in the 1980s, which raised prison populations across the country'),
    ('CABLENEWS', 'Television news carried by cable channels around the clock, beginning with CNN in 1980'),
    ('NEWRIGHT', 'The coalition of conservative activists, organizations, and voters that rose in the 1970s around lower taxes, a stronger military, and resistance to the social changes of the 1960s'),
    ('RUSTBELT', 'The name given to the industrial region of the Northeast and Midwest where factory closings emptied mills and cost whole cities much of their population'),
    ('ECOMMERCE', 'The buying and selling of goods and services over the Internet, which grew from almost nothing in the middle 1990s into a central part of American retail'),
    ('STIMULUS', 'Government spending and tax cuts meant to restart a stalled economy by putting money in consumers\' hands, as in the American Recovery and Reinvestment Act of 2009'),
    ('INTERNET', 'The network of computer networks that grew out of government and university systems into a public means of communication, commerce, and publication in the 1990s'),
    ('ALQAEDA', 'The terrorist network led by Osama bin Laden that carried out the September 11 attacks'),
    ('SUNBELT', 'The fast-growing region of the South and Southwest, whose population, jobs, and political weight rose from the 1970s onward'),
    ('AMNESTY', 'In immigration law, a grant of legal status to people who entered or remained in the country without authorization, as the 1986 act gave to those who had arrived before 1982'),
]

DIRS = {"A": (0, 1), "D": (1, 0)}


def can_place(grid, word, r, c, d):
    dr, dc = DIRS[d]
    if (r - dr, c - dc) in grid or (r + dr * len(word), c + dc * len(word)) in grid:
        return False
    crossings = 0
    for i, ch in enumerate(word):
        cell = (r + dr * i, c + dc * i)
        if cell in grid:
            if grid[cell] != ch:
                return False
            crossings += 1
        else:
            pr, pc = (dc, dr)
            if (cell[0] + pr, cell[1] + pc) in grid or (cell[0] - pr, cell[1] - pc) in grid:
                return False
    return crossings >= 1


def place(grid, placements, word, clue, r, c, d):
    dr, dc = DIRS[d]
    for i, ch in enumerate(word):
        grid[(r + dr * i, c + dc * i)] = ch
    placements.append({"word": word, "clue": clue, "r": r, "c": c, "d": d})


def build():
    rng = random.Random(SEED)
    grid = {}
    placements = []
    ordered = sorted(POOL, key=lambda x: -len(x[0]))
    first_w, first_c = ordered[rng.randrange(0, 3)]
    place(grid, placements, first_w, first_c, 0, 0, "A")
    remaining = [x for x in ordered if x[0] != first_w]
    for _ in range(8):
        nxt = []
        rng.shuffle(remaining)
        remaining.sort(key=lambda x: -len(x[0]) + rng.uniform(0, 4))
        for word, clue in remaining:
            rows = [r for r, _ in grid]
            cols = [c for _, c in grid]
            cur = (max(rows) - min(rows) + 1) * (max(cols) - min(cols) + 1)
            best = None
            for (r, c), ch in list(grid.items()):
                for i, wch in enumerate(word):
                    if wch != ch:
                        continue
                    for d in ("A", "D"):
                        dr, dc = DIRS[d]
                        sr, sc = r - dr * i, c - dc * i
                        if can_place(grid, word, sr, sc, d):
                            cells = [(sr + dr * j, sc + dc * j) for j in range(len(word))]
                            allr = [x for x, _ in grid] + [x for x, _ in cells]
                            allc = [y for _, y in grid] + [y for _, y in cells]
                            area = (max(allr) - min(allr) + 1) * (max(allc) - min(allc) + 1)
                            cross = sum(1 for cell in cells if cell in grid)
                            score = (-cross, area - cur)
                            if best is None or score < best[0]:
                                best = (score, sr, sc, d)
            if best:
                _, sr, sc, d = best
                place(grid, placements, word, clue, sr, sc, d)
            else:
                nxt.append((word, clue))
        remaining = nxt
        if not remaining:
            break
    return grid, placements, remaining


def verify(grid, placements):
    checked = {}
    crossings = 0
    for p in placements:
        dr, dc = DIRS[p["d"]]
        spelled = "".join(grid[(p["r"] + dr * i, p["c"] + dc * i)] for i in range(len(p["word"])))
        assert spelled == p["word"], (p["word"], spelled)
        for i, ch in enumerate(p["word"]):
            cell = (p["r"] + dr * i, p["c"] + dc * i)
            if cell in checked:
                assert checked[cell] == ch, ("crossing conflict", cell, checked[cell], ch)
                crossings += 1
            else:
                checked[cell] = ch
    return crossings


def render(grid, placements):
    rows = [r for r, _ in grid]
    cols = [c for _, c in grid]
    r0, r1, c0, c1 = min(rows), max(rows), min(cols), max(cols)
    H, W = r1 - r0 + 1, c1 - c0 + 1
    starts = {}
    num = 0
    numbers = {}
    for r in range(r0, r1 + 1):
        for c in range(c0, c1 + 1):
            if (r, c) not in grid:
                continue
            sa = (r, c - 1) not in grid and (r, c + 1) in grid
            sd = (r - 1, c) not in grid and (r + 1, c) in grid
            if sa or sd:
                num += 1
                numbers[(r, c)] = num
    for p in placements:
        p["num"] = numbers[(p["r"], p["c"])]
    across = sorted([p for p in placements if p["d"] == "A"], key=lambda p: p["num"])
    down = sorted([p for p in placements if p["d"] == "D"], key=lambda p: p["num"])

    def table(filled):
        out = ['<table class="xword">']
        for r in range(r0, r1 + 1):
            out.append("<tr>")
            for c in range(c0, c1 + 1):
                if (r, c) not in grid:
                    out.append('<td class="blk"></td>')
                else:
                    n = f'<span class="n">{numbers[(r, c)]}</span>' if (r, c) in numbers else ""
                    lt = grid[(r, c)] if filled else ""
                    out.append(f'<td class="cell">{n}<span class="lt">{lt}</span></td>')
            out.append("</tr>")
        out.append("</table>")
        return "".join(out)

    def clues(lst):
        return "".join(f'<p class="clue"><strong>{p["num"]}.</strong> {p["clue"]}</p>' for p in lst)

    across_list = "; ".join(f'{p["num"]} {p["word"]}' for p in across)
    down_list = "; ".join(f'{p["num"]} {p["word"]}' for p in down)
    cell = min(0.325, 6.9 / max(H, W))
    lt_pt = max(6.5, cell * 46)
    n_pt = max(5.0, cell * 30)
    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>Crossword: Modern America</title>
<style>
@page {{ size: letter; margin: 0.55in 0.75in 0.7in; }}
* {{ box-sizing: border-box; }}
body {{ font-family: Arial, Helvetica, sans-serif; font-size: 11.5pt; color: #000; line-height: 1.35; margin: 0; }}
.nameline {{ display: flex; justify-content: space-between; gap: 1em; }}
h1 {{ font-size: 19pt; margin: 12pt 0 4pt; line-height: 1.2; }}
h2 {{ font-size: 14.5pt; margin: 14pt 0 6pt; }}
p {{ margin: 0 0 7pt; }}
.directions {{ margin-bottom: 8pt; }}
table.xword {{ border-collapse: collapse; margin: 0 auto; }}
table.xword td {{ width: {cell:.3f}in; height: {cell:.3f}in; padding: 0; position: relative; }}
td.cell {{ border: 1.2px solid #000; }}
td.blk {{ background: #000; border: 1.2px solid #000; }}
td.cell .n {{ position: absolute; top: 0; left: 1.5px; font-size: {n_pt:.1f}pt; line-height: 1; }}
td.cell .lt {{ display: block; text-align: center; font-size: {lt_pt:.1f}pt; font-weight: bold; line-height: {cell:.3f}in; }}
.clue {{ margin: 0 0 2pt; font-size: 10.5pt; }}
.cols {{ display: flex; gap: 28pt; }}
.col {{ flex: 1; }}
.key {{ break-before: page; }}
.key h2:first-child {{ margin-top: 0; }}
.brandmark {{ margin: 0 0 4pt; line-height: 0; }} .brandmark img {{ width: 1.35in; }}
</style></head><body>

<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>
<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>

<h1>Crossword: Modern America</h1>
<p class="directions"><strong>Directions:</strong> Complete the crossword using the clues. Every answer is a word or run-together phrase from this unit's vocabulary and test blueprint. Multi-word answers have no spaces (for example, BLACKTUESDAY).</p>

{table(False)}

<div class="cols">
<div class="col"><h2>Across</h2>{clues(across)}</div>
<div class="col"><h2>Down</h2>{clues(down)}</div>
</div>

<div class="key">
<h2>Teacher Answer Key</h2>
{table(True)}
<p style="margin-top:10pt"><strong>Across:</strong> {across_list}</p>
<p><strong>Down:</strong> {down_list}</p>
</div>

</body></html>
"""
    return html, across, down


def main():
    grid, placements, unplaced = build()
    crossings = verify(grid, placements)
    assert len(placements) >= 20, f"only {len(placements)} answers placed"
    html, across, down = render(grid, placements)
    out = os.path.join(HERE, "review-crossword.html")
    with open(out, "w") as f:
        f.write(html)
    rows = [r for r, _ in grid]; cols = [c for _, c in grid]
    print(f"grid: {max(rows)-min(rows)+1} rows x {max(cols)-min(cols)+1} cols")
    print(f"answers placed: {len(placements)} ({len(across)} across, {len(down)} down)")
    print(f"crossing check: PASS, {crossings} shared cells verified, every letter agrees")
    print("unplaced from pool:", ", ".join(w for w, _ in unplaced) or "none")
    print("wrote", out)


if __name__ == "__main__":
    main()
