#!/usr/bin/env python3
"""Crossword generator for the Progressive Era review day.

Places answers greedily on a shared letter grid so that every word
crosses at least one word already placed, following the Founding
model, as adapted for the Reconstruction unit. Seeds are tried in a fixed order until enough complete grids
are found, and the most compact complete grid is published, so the
published grid is reproducible. Two checks run on the finished grid.
The first spells every placed answer in the grid and confirms every
crossing letter agrees. The second is independent of the placement
record: it re-derives every run of two or more filled cells from the
finished key grid alone and requires the derived runs to match the
term pool exactly, so no answer can be lost, added, or corrupted
without the build failing. Clues are short historical
identifications, none a fill-in-the-blank of a definition.
Run: python3 crossword-build.py
"""
import os
import random
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))

# (term, clue) -- answers are the terms run together with no spaces,
# punctuation dropped and digits kept, as in the model pool.
TERMS = [
    ('laissez-faire', 'Economic doctrine that kept the federal government out of business before the reform era'),
    ('tenement', 'Crowded city apartment building Jacob Riis photographed for How the Other Half Lives'),
    ('political machine', 'Organization that ran city government through favors, jobs, and delivered votes'),
    ('graft', 'Kickbacks and bribes, taken as profit from political power'),
    ('trust', "Standard Oil was the era's most famous one"),
    ('Social Gospel', 'Teaching that pushed churches into fighting poverty and bad housing'),
    ('settlement house', 'Hull House in Chicago was the most famous, run by Jane Addams'),
    ('muckraker', "Name Roosevelt took from Bunyan's Pilgrim's Progress for critical journalists"),
    ('exposé', 'A published investigation that brings hidden wrongdoing into the open'),
    ('mass-circulation magazine', "McClure's, sold for ten or fifteen cents and paid for by advertising"),
    ('serialized', "How Tarbell's Standard Oil history reached readers, installment by installment"),
    ('The Jungle (1906)', "Sinclair's novel of immigrant life in Chicago's Packingtown"),
    ('Meat Inspection Act (1906)', 'One of the two 1906 food laws, this one covering meat'),
    ('public opinion', 'What an exposé had to move before Congress would act'),
    ('initiative', 'Device first adopted statewide by South Dakota in 1898'),
    ('referendum', 'Device that sends a law to the voters for a final decision'),
    ('recall', 'Device for removing an elected official before the term expires'),
    ('direct primary', 'Wisconsin wrote the first statewide one into law in 1903'),
    ('Wisconsin Idea', "La Follette's practice of running government with university experts"),
    ('commission government', 'Plan Galveston adopted after the hurricane of 1900'),
    ('city manager', 'Professional administrator hired under the council-manager plan'),
    ('Square Deal', "Roosevelt's program, drawn as three sides: corporations, consumers, conservation"),
    ('Sherman Antitrust Act', 'Law under which the Northern Securities holding company was dissolved in 1904'),
    ('arbitration', "Settlement method the coal owners accepted in 1902 under Roosevelt's pressure"),
    ('Hepburn Act (1906)', 'Law that gave the ICC power to set maximum railroad rates'),
    ('Pure Food and Drug Act (1906)', 'The other 1906 food law, this one aimed at impure and mislabeled products'),
    ('conservation', "Pinchot's wise-use doctrine for forests, water, and land"),
    ('Antiquities Act (1906)', 'Law Roosevelt used first at Devils Tower, Wyoming'),
    ('Mann-Elkins Act (1910)', 'Taft-era law that widened federal railroad regulation'),
    ('Payne-Aldrich Tariff (1909)', 'Tariff Taft praised in a speech, angering progressives who expected cuts'),
    ('Ballinger-Pinchot affair', 'Fight over Alaskan coal claims that ended with Pinchot fired'),
    ('Progressive Party', 'Party organized in August 1912 after the Republican convention fight'),
    ('Eugene V. Debs', 'Socialist candidate who took about 6 percent of the 1912 vote'),
    ('New Nationalism', "Roosevelt's 1912 program: accept the corporations and regulate them"),
    ('New Freedom', "Wilson's 1912 program: break up monopoly and restore competition"),
    ('triple wall of privilege', "Wilson's three targets: the tariff, the banks, and the trusts"),
    ('Underwood Tariff (1913)', 'Law that cut average import duties from about 40 percent to about 25'),
    ('Sixteenth Amendment (1913)', 'Amendment that reversed the Pollock decision'),
    ('Federal Reserve Act (1913)', 'Law creating twelve regional reserve banks under a federal board'),
    ('Clayton Antitrust Act (1914)', "1914 law Gompers called labor's Magna Carta"),
    ('Federal Trade Commission (1914)', 'Permanent expert body Wilson created to stop unfair competition'),
    ('Adamson Act (1916)', '1916 law fixing an eight-hour day for railroad workers'),
    ('suffrage', 'What Seneca Falls demanded and the Nineteenth Amendment finally secured'),
    ('Seneca Falls (1848)', 'Convention where Stanton and Mott issued the Declaration of Sentiments'),
    ('NAWSA', "Organization formed in 1890 when the movement's two wings reunited"),
    ('Silent Sentinels', "Alice Paul's pickets at the White House gates, beginning January 1917"),
    ('Night of Terror (1917)', 'November 1917 night of beatings at the Occoquan Workhouse'),
    ('Winning Plan', "Catt's strategy joining state campaigns to a federal amendment drive"),
    ('Nineteenth Amendment (1920)', 'Amendment certified in August 1920, after Tennessee ratified'),
    ('Jim Crow', "Name for the South's system of segregation laws"),
    ('poll tax', 'Fee at the polls that kept poor and Black voters away'),
    ('grandfather clause', 'Voting rule struck down by the Supreme Court in Guinn, 1915'),
    ('NAACP (1909)', 'Organization founded after the Springfield riot of 1908'),
    ('Immigration Act of 1917', "Restriction law Congress passed over Wilson's veto"),
    ('Eighteenth Amendment (1919)', 'The only amendment ever repealed'),
    ('Volstead Act (1919)', "Prohibition's enforcement law"),
]


def normalize(term):
    ascii_term = unicodedata.normalize("NFKD", term).encode("ascii", "ignore").decode()
    return "".join(ch for ch in ascii_term.upper() if ch.isalnum())


POOL = [(normalize(term), clue) for term, clue in TERMS]
assert len(POOL) == 56, len(POOL)
assert len({w for w, _ in POOL}) == 56, "normalized answers are not unique"

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


def build(seed):
    rng = random.Random(seed)
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


def derive_runs(grid):
    """Re-derive every run of two or more filled cells from the grid
    alone, with no reference to the placement record."""
    runs = []
    by_row = {}
    by_col = {}
    for (r, c) in grid:
        by_row.setdefault(r, []).append(c)
        by_col.setdefault(c, []).append(r)
    for r, cols in by_row.items():
        cols.sort()
        start = prev = cols[0]
        for c in cols[1:] + [None]:
            if c is not None and c == prev + 1:
                prev = c
                continue
            if prev - start + 1 >= 2:
                runs.append("".join(grid[(r, x)] for x in range(start, prev + 1)))
            if c is not None:
                start = prev = c
    for c, rows in by_col.items():
        rows.sort()
        start = prev = rows[0]
        for r in rows[1:] + [None]:
            if r is not None and r == prev + 1:
                prev = r
                continue
            if prev - start + 1 >= 2:
                runs.append("".join(grid[(x, c)] for x in range(start, prev + 1)))
            if r is not None:
                start = prev = r
    return runs


def independent_check(grid):
    derived = sorted(derive_runs(grid))
    pool = sorted(w for w, _ in POOL)
    assert derived == pool, (
        "derived runs do not match the term pool exactly; "
        f"missing: {[w for w in pool if w not in derived]}, "
        f"extra: {[w for w in derived if w not in pool]}")
    return len(derived)


def grid_size(grid):
    rows = [r for r, _ in grid]
    cols = [c for _, c in grid]
    return max(rows) - min(rows) + 1, max(cols) - min(cols) + 1


def render(grid, placements):
    rows = [r for r, _ in grid]
    cols = [c for _, c in grid]
    r0, r1, c0, c1 = min(rows), max(rows), min(cols), max(cols)
    H, W = r1 - r0 + 1, c1 - c0 + 1
    numbers = {}
    num = 0
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
<title>Review Crossword: The Progressive Era</title>
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
.clue {{ margin: 0 0 2pt; font-size: 10.5pt; }}
.cols {{ display: flex; gap: 28pt; }}
.col {{ flex: 1; }}
.key {{ break-before: page; }}
.key h2:first-child {{ margin-top: 0; }}
.brandmark {{ margin: 0 0 4pt; line-height: 0; }} .brandmark img {{ width: 1.35in; }}
</style></head><body>

<p class="brandmark"><img src="../../assets/hcg-logo/hcg-wordmark.svg" alt="Humanities Curriculum Group"></p>
<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>

<h1>Review Crossword: The Progressive Era</h1>
<p class="directions"><strong>Directions:</strong> Complete the crossword using the clues. Every answer is a word or run-together phrase from this unit's vocabulary. Multi-word answers have no spaces (for example, SQUAREDEAL).</p>

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
    best = None
    successes = 0
    attempts = 0
    for seed in range(1, 601):
        attempts = seed
        grid, placements, remaining = build(seed)
        if remaining:
            continue
        try:
            crossings = verify(grid, placements)
            independent_check(grid)
        except AssertionError:
            continue
        successes += 1
        H, W = grid_size(grid)
        score = (H * W, max(H, W), seed)
        if best is None or score < best[0]:
            best = (score, seed, grid, placements, crossings)
        if successes >= 40:
            break
    assert best is not None, "no seed produced a complete verified grid"
    _, seed, grid, placements, crossings = best
    derived = independent_check(grid)
    html, across, down = render(grid, placements)
    out = os.path.join(HERE, "review-crossword.html")
    with open(out, "w") as f:
        f.write(html)
    H, W = grid_size(grid)
    print(f"seed: {seed} (chosen as the most compact of {successes} complete verified grids in {attempts} seeds tried)")
    print(f"grid: {H} rows x {W} cols")
    print(f"answers placed: {len(placements)} ({len(across)} across, {len(down)} down)")
    print(f"crossing check: PASS, {crossings} shared cells verified, every letter agrees")
    print(f"independent check: PASS, {derived} runs re-derived from the finished key grid match the 56 term pool exactly")
    print("unplaced from pool: none")
    print("wrote", out)


if __name__ == "__main__":
    main()
