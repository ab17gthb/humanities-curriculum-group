#!/usr/bin/env python3
"""Crossword generator for the World War II review day.

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
SEED = 7  # fixed so the published grid is reproducible

# (answer, clue) -- answers are run together with no spaces, as in the pilot.
POOL = [
    ('SELECTIVETRAININGANDSERVICEACT', 'The law of 1940 that created the first peacetime draft in American history'),
    ('FAIREMPLOYMENTPRACTICESCOMMITTEE', 'The federal committee created in 1941 to investigate complaints of job discrimination in war industries'),
    ('OFFICEOFPRICEADMINISTRATION', 'The federal agency that set price ceilings and ran the rationing system during the war'),
    ('EXECUTIVEORDER8802', 'President Roosevelt\'s order of June 1941 barring racial discrimination in defense industries and federal employment'),
    ('EXECUTIVEORDER9066', 'President Roosevelt\'s order of February 19, 1942, under which Japanese Americans were removed from their homes'),
    ('WARPRODUCTIONBOARD', 'The federal agency created in 1942 to direct the conversion of industry to war production'),
    ('442NDREGIMENTALCOMBATTEAM', 'The segregated Japanese American army unit that became one of the most decorated of its size in American history'),
    ('MANHATTANPROJECT', 'The secret American program that built the first atomic bombs'),
    ('STRATEGICBOMBING', 'The use of heavy bombers against an enemy\'s industry, transportation, and cities'),
    ('ATLANTICCHARTER', 'The joint statement of aims issued by Roosevelt and Churchill in August 1941'),
    ('POTSDAMDECLARATION', 'The Allied ultimatum of July 26, 1945 demanding Japan\'s unconditional surrender'),
    ('NEUTRALITYACTS', 'The laws of the 1930s that barred arms sales and loans to nations at war'),
    ('NUREMBERGLAWS', 'The German laws of 1935 that stripped Jews of citizenship'),
    ('GRANDALLIANCE', 'The formal alliance of the United States, Great Britain, and the Soviet Union against the Axis'),
    ('BATTLEOFMIDWAY', 'The naval battle of June 1942 in which American carriers sank four Japanese carriers'),
    ('ISLANDHOPPING', 'The Pacific strategy of seizing selected islands while bypassing strong garrisons'),
    ('AMPHIBIOUSLANDING', 'An attack from the sea onto a defended shore by forces carried in ships and landing craft'),
    ('DOUBLEVCAMPAIGN', 'The campaign led by Black newspapers for victory over fascism abroad and victory over racism at home'),
    ('FINALSOLUTION', 'The Nazi program to murder every Jew in Europe, carried out from 1941 to 1945'),
    ('ROSIE THERIVETER'.replace(' ',''), 'The popular name and image for the American women who took factory and shipyard jobs during the war'),
    ('DEMOBILIZATION', 'The process of bringing armed forces back to civilian life after a war'),
    ('UNCONDITIONALSURRENDER', 'The demand that an enemy give up without negotiated conditions'),
    ('CASHANDCARRY', 'The 1939 policy that let nations at war buy American arms if they paid cash and carried them away in their own ships'),
    ('NAVALBLOCKADE', 'The use of warships, submarines, and aircraft to cut off an enemy\'s sea trade and supplies'),
    ('ANTISEMITISM', 'Prejudice against, hatred of, or discrimination against Jews'),
    ('GERMANYFIRST', 'The Allied strategy of concentrating the main effort on defeating Germany before Japan'),
    ('SECONDFRONT', 'The invasion of German-held western Europe that the Soviet Union demanded from 1942 onward'),
    ('EASTERNFRONT', 'The battlefront between Germany and the Soviet Union, where the largest land fighting of the war took place'),
    ('PEARLHARBOR', 'The naval base in Hawaii attacked on December 7, 1941'),
    ('MOBILIZATION', 'The process of preparing a nation\'s armed forces, industry, and economy for war'),
    ('INTERNMENT', 'The forced confinement of a group of people; here, the removal of Japanese Americans to guarded camps'),
    ('FIREBOMBING', 'The bombing of cities with incendiary weapons designed to start mass fires'),
    ('STALINGRAD', 'The 1942 to 1943 battle in which the Soviet army surrounded and destroyed a German army'),
    ('GUADALCANAL', 'The Solomon Islands campaign of 1942 to 1943, the first major Allied offensive of the Pacific war'),
    ('FOURFREEDOMS', 'The freedoms Roosevelt named in January 1941: speech, worship, freedom from want, and freedom from fear'),
    ('AXISPOWERS', 'The alliance of Germany, Italy, and Japan'),
    ('KAMIKAZE', 'A Japanese pilot who made a deliberate crash attack on an enemy ship'),
    ('RATIONING', 'A system limiting how much of a scarce good each person may buy, enforced with coupons'),
    ('HOLOCAUST', 'The state-sponsored persecution and murder of six million European Jews by Nazi Germany and its collaborators'),
    ('ATOMICBOMB', 'A bomb whose explosive power comes from splitting atoms'),
    ('WARCRIMES', 'Violations of the laws of war, such as the murder of prisoners and civilians'),
    ('DEATHCAMP', 'One of the camps built in occupied Poland where Jews and others were murdered on arrival'),
    ('WARBONDS', 'Government bonds sold to the public to raise money for the war, repaid with interest'),
    ('LENDLEASE', 'The law of March 1941 that let the president lend or lease arms to countries whose defense he judged vital'),
    ('ISOLATIONISM', 'A policy of avoiding political commitments and alliances with other countries'),
    ('VEDAY', 'May 8, 1945, the day victory in Europe was announced'),
    ('DDAY', 'June 6, 1944, the day Allied forces landed in Normandy'),
    ('GHETTO', 'A section of a city where Jews were forced to live under German occupation'),
    ('GIBILL', 'The 1944 law that gave veterans tuition, training, and government-backed loans'),
    ('THEATER', 'A large geographic area of military operations'),
]

DIRS = {"A": (0, 1), "D": (1, 0)}


def can_place(grid, word, r, c, d):
    dr, dc = DIRS[d]
    # cell before the first letter and after the last must be empty
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
            # no letter may sit beside a new letter across its direction,
            # or two words would run together side by side
            pr, pc = (dc, dr)  # perpendicular step
            if (cell[0] + pr, cell[1] + pc) in grid or (cell[0] - pr, cell[1] - pc) in grid:
                return False
    return crossings >= 1


def place(grid, placements, word, clue, r, c, d):
    dr, dc = DIRS[d]
    for i, ch in enumerate(word):
        grid[(r + dr * i, c + dc * i)] = ch
    placements.append({"word": word, "clue": clue, "r": r, "c": c, "d": d})


def build():
    """Seeded greedy build. Each word goes where it crosses the most
    letters already placed, breaking ties toward the placement that
    grows the grid's bounding box the least, which keeps the finished
    grid compact. The fixed seed makes the result reproducible."""
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
    """Every answer must spell correctly in the grid, and the letters a
    word shares with any crossing word must agree at every crossing."""
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
    # standard numbering: a cell is numbered if it starts an across or a down entry
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
    cell = max(0.20, min(0.325, 6.9 / max(H, W)))
    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>Crossword: World War II</title>
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
td.cell .n {{ position: absolute; top: 0; left: 1.5px; font-size: 7pt; line-height: 1; }}
td.cell .lt {{ display: block; text-align: center; font-size: 13pt; font-weight: bold; line-height: {cell:.3f}in; }}
.clue {{ margin: 0 0 2.5pt; font-size: 11pt; }}
.cols {{ display: flex; gap: 28pt; }}
.col {{ flex: 1; }}
.key {{ break-before: page; }}
.key h2:first-child {{ margin-top: 0; }}
.brandmark {{ margin: 0 0 4pt; line-height: 0; }} .brandmark img {{ width: 1.35in; }}
</style></head><body>

<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>
<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>

<h1>Crossword: World War II</h1>
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
    print(f"answers placed: {len(placements)} ({len(across)} across, {len(down)} down)")
    print(f"crossing check: PASS, {crossings} shared cells verified, every letter agrees")
    print("unplaced from pool:", ", ".join(w for w, _ in unplaced) or "none")
    print("wrote", out)


if __name__ == "__main__":
    main()
