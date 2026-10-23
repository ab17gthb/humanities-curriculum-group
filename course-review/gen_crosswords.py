#!/usr/bin/env python3
"""Course Review crosswords: four answers per unit (early 24, modern 36,
combined 60), built on the unit crosswords' engine: greedy placement with
every word crossing a placed word, programmatic verification of every
spelling and crossing, a student grid with Across and Down clues, and a
filled teacher key. Seeds are searched for the placement that fits all
answers in the smallest grid.

Run: python3 gen_crosswords.py
"""
import json
import os
import random
import re

HERE = os.path.dirname(os.path.abspath(__file__))
STAGING = "/home/hatch/workspace/rycal/course-staging"
SLUGS = {
    "ca": "hcg-colonial-america", "fd": "hcg-the-founding",
    "er": "hcg-early-republic", "jr": "hcg-jackson-reform",
    "sc": "hcg-sectional-crisis", "rc": "hcg-reconstruction",
    "ga": "hcg-gilded-age", "pe": "hcg-progressive-era",
    "wwi": "hcg-imperialism-wwi", "tw": "hcg-twenties",
    "dp": "hcg-depression-new-deal", "ww2": "hcg-world-war-ii",
    "cw": "hcg-cold-war", "cr": "hcg-civil-rights", "ma": "hcg-modern-america",
}

# unit -> [(term as printed in the unit, clue)]
PICKS = {
"ca": [("Columbian Exchange", "The transfer of plants, animals, diseases, and peoples between the Eastern and Western Hemispheres after 1492"),
       ("mercantilism", "The economic doctrine that a nation's wealth is its stock of precious metal, gained by exporting more than it imports and ruling colonies for the mother country's benefit"),
       ("Mayflower Compact", "The 1620 agreement by which the Pilgrims formed a civil body politic and pledged to obey laws made for the general good"),
       ("Great Awakening", "The religious revival of the 1730s and 1740s that swept the colonies and challenged established church authority")],
"fd": [("Common Sense", "Thomas Paine's 1776 pamphlet arguing, in plain language, that the colonies should declare independence"),
       ("Federalist Papers", "The essays of Hamilton, Madison, and Jay arguing for ratification of the Constitution"),
       ("Shays's Rebellion", "The 1786 rising of indebted Massachusetts farmers that convinced many leaders the Confederation was too weak"),
       ("Bill of Rights", "The first ten amendments to the Constitution, added in 1791 as the price of ratification")],
"er": [("Louisiana Purchase", "The 1803 purchase from France that doubled the territory of the United States for about fifteen million dollars"),
       ("Monroe Doctrine", "The 1823 statement that the Americas were closed to new European colonization and that the United States would stay out of Europe's wars"),
       ("Missouri Compromise", "The 1820 settlement admitting Maine and Missouri as a pair and drawing the 36°30' line across the Louisiana Purchase"),
       ("embargo", "Jefferson's 1807 law forbidding American ships to sail for foreign ports, meant to punish Britain and France without war")],
"jr": [("Trail of Tears", "The forced removal of the Cherokee and the other southeastern nations to Indian Territory in the 1830s, on which thousands died"),
       ("Seneca Falls Convention", "The 1848 convention whose Declaration of Sentiments opened the organized women's rights movement"),
       ("nullification", "The doctrine that a state may declare a federal law void within its borders, pressed by South Carolina in 1832"),
       ("spoils system", "The practice of filling government offices with the winning party's supporters, defended by Jackson as rotation in office")],
"sc": [("Fugitive Slave Act", "The 1850 law requiring the return of escaped enslaved people and compelling citizens to assist, which radicalized northern opinion"),
       ("Dred Scott v. Sandford", "The 1857 decision, in the case of an enslaved man who had lived in free territory, denying Black citizenship and Congress's power over slavery in the territories"),
       ("Gettysburg Address", "Lincoln's 1863 dedication speech restating the war's purpose as the nation's rebirth in freedom"),
       ("secession", "The claimed right of a state to leave the Union, exercised by eleven states in 1860 and 1861")],
"rc": [("Freedmen's Bureau", "The federal agency of 1865 charged with aiding the formerly enslaved and refugees with food, schools, contracts, and courts"),
       ("sharecropping", "The system in which a landless family worked a plot for a share of the crop, settling accounts with the landowner at year's end"),
       ("Black Codes", "The laws of 1865 and 1866 by which southern states restricted the freedom of the formerly enslaved and bound them to labor"),
       ("Fourteenth Amendment", "The 1868 amendment establishing birthright citizenship and promising due process and equal protection against the states")],
"ga": [("laissez-faire", "The doctrine that government should leave business alone, the Gilded Age's reigning economic faith"),
       ("Sherman Antitrust Act", "The 1890 law against combinations in restraint of trade, little enforced against trusts in its first decade and often used against unions"),
       ("Jim Crow", "The system of laws and customs that segregated the South and disfranchised its Black citizens from the 1890s"),
       ("political machine", "The urban organization, run by a boss, that traded jobs, services, and favors for the votes of the immigrant city")],
"pe": [("muckraker", "The investigative journalists who exposed corruption, adulterated food, and corporate abuse to a mass magazine readership"),
       ("settlement house", "The neighborhood institution, Hull House the model, where reformers lived and offered classes, clinics, and advocacy"),
       ("Silent Sentinels", "The suffragists who picketed the White House from 1917 and were arrested, imprisoned, and force-fed for it"),
       ("Square Deal", "Theodore Roosevelt's program of balanced dealing among capital, labor, and the public, with the federal government as referee")],
"wwi": [("Fourteen Points", "Wilson's 1918 program for the peace, from open covenants to a league of nations"),
        ("Zimmermann Telegram", "The intercepted 1917 German proposal of an alliance with Mexico against the United States, whose publication helped close the neutrality argument"),
        ("Lusitania", "The British liner sunk by a German submarine in 1915 with 128 Americans aboard, the incident that opened the submarine crisis"),
        ("Espionage Act", "The 1917 law punishing interference with the war effort, under which Schenck and Debs were prosecuted")],
"tw": [("Prohibition", "The constitutional experiment, 1920 to 1933, banning the manufacture and sale of alcohol"),
       ("Harlem Renaissance", "The flowering of Black art, literature, and music centered in Harlem in the 1920s"),
       ("speakeasy", "An illegal bar of the Prohibition years, known to the police it paid and entered by password"),
       ("Black Tuesday", "October 29, 1929, the day the stock market's collapse became a rout")],
"dp": [("bank holiday", "Roosevelt's closing of every bank in the country in March 1933, until federal inspection let the sound ones reopen"),
       ("Hooverville", "The name the homeless gave their shantytowns of scrap and packing crates, assigning the blame for them"),
       ("Social Security Act", "The 1935 law creating old-age insurance, unemployment insurance, and aid to dependent children, funded by a payroll tax"),
       ("Dust Bowl", "The drought and wind erosion that stripped the southern Plains' topsoil through the 1930s")],
"ww2": [("Lend-Lease", "The 1941 program by which the United States supplied the Allies with war materiel before and after it became a belligerent"),
        ("island hopping", "The Pacific strategy of seizing selected islands as stepping stones and bypassing Japanese strongholds"),
        ("kamikaze", "The Japanese suicide pilots who dove their planes into American ships in the war's last year"),
        ("Manhattan Project", "The secret program, centered at Los Alamos, that built the atomic bombs used in 1945")],
"cw": [("containment", "The doctrine of resisting Soviet expansion with firm, patient counter-pressure until the Soviet system changed or broke"),
       ("Iron Curtain", "Churchill's 1946 phrase for the line dividing Soviet-dominated Eastern Europe from the West"),
       ("McCarthyism", "The practice of public accusation without proof in the early 1950s, named for the senator broken by the televised Army hearings"),
       ("Cuban Missile Crisis", "The thirteen days of October 1962 when Soviet missiles in Cuba brought the superpowers to the edge of war")],
"cr": [("Freedom Rides", "The 1961 interracial bus rides that tested desegregation rulings in interstate travel and were met with burnings and beatings"),
       ("Little Rock Nine", "The nine Black students who integrated Central High School in 1957 under the protection of the 101st Airborne"),
       ("Montgomery bus boycott", "The 381-day boycott of 1955 and 1956 that ended bus segregation in Montgomery and raised King to national leadership"),
       ("March on Washington", "The August 1963 gathering of a quarter million people at the Lincoln Memorial for jobs and freedom")],
"ma": [("stagflation", "The combination of stagnant growth, high unemployment, and high inflation that afflicted the economy in the 1970s"),
       ("globalization", "The deepening connection of the world's economies through trade, investment, and production spread across borders"),
       ("PATCO strike", "The 1981 strike in which President Reagan fired more than eleven thousand federal air traffic controllers"),
       ("War on Terror", "The worldwide campaign of military action, intelligence work, and security measures declared after September 11, 2001")],
}

EARLY_UNITS = ["ca", "fd", "er", "jr", "sc", "rc"]
MODERN_UNITS = ["ga", "pe", "wwi", "tw", "dp", "ww2", "cw", "cr", "ma"]
VARIANTS = {
    "early": ("Early Course Review", EARLY_UNITS),
    "modern": ("Modern Course Review", MODERN_UNITS),
    "combined": ("Course Review", EARLY_UNITS + MODERN_UNITS),
}

DIRS = {"A": (0, 1), "D": (1, 0)}


def validate_picks():
    for uid, picks in PICKS.items():
        rows = json.load(open(os.path.join(STAGING, SLUGS[uid], "vocab-audited.json")))
        terms = {r["term"] for r in rows}
        for term, clue in picks:
            assert term in terms, (uid, term)
    print("all 60 crossword answers verified as printed unit terms")


def rung(term):
    return re.sub(r"[^A-Z0-9]", "", term.upper())


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


def build(pool, seed):
    rng = random.Random(seed)
    grid, placements = {}, []
    ordered = sorted(pool, key=lambda x: -len(x[0]))
    first_w, first_c = ordered[rng.randrange(0, 3)]
    place(grid, placements, first_w, first_c, 0, 0, "A")
    remaining = [x for x in ordered if x[0] != first_w]
    for _ in range(10):
        nxt = []
        rng.shuffle(remaining)
        remaining.sort(key=lambda x: -len(x[0]) + rng.uniform(0, 4))
        for word, clue in remaining:
            rows = [r for r, _ in grid]; cols = [c for _, c in grid]
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
    checked, crossings = {}, 0
    for p in placements:
        dr, dc = DIRS[p["d"]]
        spelled = "".join(grid[(p["r"] + dr * i, p["c"] + dc * i)] for i in range(len(p["word"])))
        assert spelled == p["word"], (p["word"], spelled)
        for i, ch in enumerate(p["word"]):
            cell = (p["r"] + dr * i, p["c"] + dc * i)
            if cell in checked:
                assert checked[cell] == ch, ("crossing conflict", cell)
                crossings += 1
            else:
                checked[cell] = ch
    return crossings


def render(grid, placements, vname):
    rows = [r for r, _ in grid]; cols = [c for _, c in grid]
    r0, r1, c0, c1 = min(rows), max(rows), min(cols), max(cols)
    H, W = r1 - r0 + 1, c1 - c0 + 1
    numbers, num = {}, 0
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
    doc = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>Crossword: {vname}</title>
<style>
@page {{ size: letter; margin: 0.55in 0.75in 0.7in; }}
* {{ box-sizing: border-box; }}
body {{ font-family: Arial, Helvetica, sans-serif; font-size: 11.5pt; color: #000; line-height: 1.35; margin: 0; }}
.nameline {{ display: flex; justify-content: space-between; gap: 1em; }}
h1 {{ font-family: Georgia, serif; font-size: 19pt; margin: 12pt 0 4pt; line-height: 1.2; color: #1b2a4a; }}
h2 {{ font-family: Georgia, serif; font-size: 14.5pt; margin: 14pt 0 6pt; color: #1b2a4a; }}
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
<h1>Crossword: {vname}</h1>
<p class="directions"><strong>Directions:</strong> Complete the crossword using the clues. Every answer is a term from the review: four from each unit it covers. Multi-word answers run together with no spaces (for example, BLACKTUESDAY).</p>
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
    return doc, across, down, (H, W)


def main():
    validate_picks()
    for variant, (vname, unit_ids) in VARIANTS.items():
        pool = [(rung(t), c) for uid in unit_ids for t, c in PICKS[uid]]
        best = None
        for seed in range(60):
            grid, placements, unplaced = build(pool, seed)
            if unplaced:
                continue
            rows = [r for r, _ in grid]; cols = [c for _, c in grid]
            dims = (max(rows) - min(rows) + 1, max(cols) - min(cols) + 1)
            score = max(dims)
            if best is None or score < best[0]:
                best = (score, seed, grid, placements, dims)
            if score <= 34:
                break
        assert best, variant
        score, seed, grid, placements, dims = best
        crossings = verify(grid, placements)
        doc, across, down, hw = render(grid, placements, vname)
        d = os.path.join(HERE, f"crossword-{variant}")
        os.makedirs(d, exist_ok=True)
        path = os.path.join(d, f"{variant}-crossword.html")
        open(path, "w").write(doc)
        print(f"{variant}: seed {seed}, grid {dims[0]}x{dims[1]}, "
              f"{len(placements)} answers ({len(across)} across, {len(down)} down), "
              f"{crossings} crossings verified -> {path}")


if __name__ == "__main__":
    main()
