#!/usr/bin/env python3
"""Crossword generator for the Jackson and Reform review day.

Places answers greedily on a shared letter grid so that every word
crosses at least one word already placed, following the Founding
model. Seeds are tried in a fixed order until enough complete grids
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
    ('Andrew Jackson', 'Tennessee general, hero of New Orleans, who won the elections of 1828 and 1832'),
    ('Jacksonian democracy', 'Movement of the 1820s and 1830s celebrating the common white man and an energetic presidency'),
    ('corrupt bargain', "Charge that Clay traded the House vote of 1824 to Adams for the secretary of state's office"),
    ('suffrage', 'The vote itself, extended by the states in the 1820s until nearly every white man held it'),
    ('spoils system', "Opponents' name for filling offices with the winning side's supporters after 1828"),
    ('rotation in office', "Jackson's doctrine that offices should pass regularly from citizen to citizen"),
    ('Democratic Party', 'Party formed around Jackson out of the election of 1828, joining planters, farmers, and workingmen'),
    ('Indian Removal Act', 'Law of May 1830 authorizing land exchanges west of the Mississippi for Native nations in the states'),
    ('Cherokee Nation', 'Southern Appalachian nation with a constitution, a syllabary, and a newspaper by the 1820s'),
    ('Worcester v. Georgia', '1832 decision in which Marshall held Georgia law had no force in Cherokee country'),
    ('Five Civilized Tribes', "White Americans' name for the Cherokee, Choctaw, Chickasaw, Creek, and Seminole nations"),
    ('Treaty of New Echota', 'December 1835 treaty signed by a Cherokee minority and ratified by a single Senate vote'),
    ('Trail of Tears', 'Forced Cherokee march west in the winter of 1838 and 1839, on which about a quarter died'),
    ('John Ross', 'Principal chief of the Cherokee from 1828 to 1866 who led a decade of legal resistance'),
    ('Tariff of Abominations', 'Southern name for the high protective duties Congress passed in 1828'),
    ('nullification', 'Claim drawn from the Kentucky Resolutions that a state may declare a federal law void within its borders'),
    ('John C. Calhoun', 'Vice president who secretly wrote the Exposition and resigned in 1832 to defend his doctrine in the Senate'),
    ('South Carolina Exposition and Protest', 'Pamphlet adopted in December 1828, secretly written by the sitting vice president'),
    ('Ordinance of Nullification', 'South Carolina convention act of November 24, 1832 voiding the tariffs of 1828 and 1832 in the state'),
    ('Webster-Hayne debate', 'Senate debate of January 1830 closing with a defense of liberty and union, one and inseparable'),
    ('Force Bill', 'Law of March 2, 1833 authorizing the president to collect the tariff duties with the army and navy'),
    ('Bank War', 'Struggle of 1832 to 1836 over the Second Bank, fought with a veto, deposit removal, and contracted credit'),
    ('Nicholas Biddle', 'Philadelphia financier who ran the Second Bank from 1823 and fought Jackson for its life'),
    ('pet banks', 'Contemptuous name for the state banks given the federal deposits removed in 1833'),
    ('Specie Circular', 'Treasury order of July 1836 requiring gold or silver in payment for public lands'),
    ('Panic of 1837', 'Financial collapse of May 1837, when banks suspended specie payment and a long depression followed'),
    ('Whig Party', "Party coalesced in 1834 from Jackson's opponents, named for the historic foes of royal power"),
    ('independent treasury', 'Van Buren system, enacted in 1840, keeping federal money in government vaults instead of any bank'),
    ('market revolution', 'Transformation from about 1815 to 1848 as canals, steamboats, railroads, and wires bound households to distant markets'),
    ('factory system', 'Production moved into one building, at set hours, at machines owned by the employer'),
    ('Lowell system', 'Mill order at a Massachusetts town of factories, boardinghouses, and churches built together'),
    ('interchangeable parts', 'Armory method of machining every part to a standard pattern so any part fits any unit'),
    ('telegraph', "Morse's electromagnetic system, opened between Washington and Baltimore in 1844"),
    ('Samuel F. B. Morse', 'Painter turned inventor whose code of dots and dashes carries his name'),
    ('trade union', "Workers' organization of the 1830s cities, formed to bargain over wages and hours and to strike"),
    ('Second Great Awakening', 'Evangelical revival, carried by camp meetings, teaching that every person could choose salvation'),
    ('Charles Grandison Finney', 'Preacher whose Rochester meetings of 1830 and 1831 modeled the new evangelism'),
    ('burned-over district', 'Western and central New York region preachers said had no fuel left to burn'),
    ('temperance', 'Movement organized nationally in 1826 that moved from moderation pledges toward legal prohibition'),
    ('Horace Mann', 'Massachusetts education secretary who called common schools the balance wheel of the social machinery'),
    ('common schools', 'Tax supported public schools open to all children of a district, spread across the North in this era'),
    ('Dorothea Dix', 'Massachusetts teacher whose jail and almshouse investigations built the first public asylums'),
    ('abolition', 'Movement that turned in the 1830s from gradual schemes to demanding slavery end as a sin'),
    ("Walker's Appeal", '1829 Boston pamphlet, smuggled into the South, calling on enslaved people to resist enslavement'),
    ('William Lloyd Garrison', 'Boston editor who founded The Liberator in 1831 and renounced gradualism in its first issue'),
    ('immediatism', 'Doctrine that slavery must end at once, without stages, compensation, or removal of the freed people'),
    ('Nat Turner', 'Enslaved Virginia preacher who led the deadliest slave rebellion in United States history in 1831'),
    ('gag rule', 'House rule from 1836 to 1844 tabling every antislavery petition without reading or debate'),
    ('Frederick Douglass', 'Maryland fugitive whose 1845 Narrative answered the claim that the enslaved could not speak for themselves'),
    ('Seneca Falls Convention', 'Convention of July 19 and 20, 1848, the first called to discuss the rights of woman'),
    ('Declaration of Sentiments', '1848 declaration modeled sentence by sentence on the Declaration of Independence'),
    ('Elizabeth Cady Stanton', 'Organizer who drafted the 1848 declaration and insisted its resolutions demand the franchise'),
    ('Lucretia Mott', "Quaker minister whose exclusion at London in 1840 turned her toward organizing for women's rights"),
    ('Grimké sisters', 'Charleston sisters who left the slaveholding South and lectured for abolition to mixed audiences'),
    ('coverture', "Common law doctrine placing a married woman's property, wages, and court standing under her husband"),
    ("Married Women's Property Act", 'New York law of April 1848, three months before Seneca Falls, first effective statute of its kind'),
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
<title>Crossword: Jackson and Reform</title>
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

<h1>Crossword: Jackson and Reform</h1>
<p class="directions"><strong>Directions:</strong> Complete the crossword using the clues. Every answer is a word or run-together phrase from this unit's vocabulary. Multi-word answers have no spaces (for example, TRAILOFTEARS). Punctuation is dropped (for example, WORCESTERVGEORGIA).</p>

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
