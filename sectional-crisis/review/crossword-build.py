#!/usr/bin/env python3
"""Crossword generator for the Sectional Crisis and Civil War review
day.

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
    ('Compromise of 1850', 'Five measure settlement of September 1850, passed bill by bill after the omnibus failed'),
    ('Fugitive Slave Act', 'September 18, 1850 law paying commissioners ten dollars to remand a prisoner and five to free one'),
    ('Henry Clay', 'Kentucky senator, builder of the 1820 and 1833 settlements, who framed the last one at seventy two'),
    ('Daniel Webster', "Massachusetts orator of the Seventh of March speech, mourned in Whittier's poem Ichabod"),
    ('personal liberty laws', 'Northern statutes denying state jails and state officers to federal rendition'),
    ('Underground Railroad', 'Informal network of safe houses and guides carrying enslaved people north to the free states and Canada'),
    ('Harriet Tubman', 'Maryland conductor born Araminta Ross who guided some seventy enslaved people to freedom'),
    ("Uncle Tom's Cabin", "Stowe's antislavery novel of 1852, the best selling American novel of its century"),
    ('Harriet Beecher Stowe', 'Cincinnati writer, daughter of Lyman Beecher, who later published a documentary key defending her novel'),
    ('Sojourner Truth', 'New York preacher born Isabella Baumfree who spoke at Akron in 1851'),
    ('Harriet Jacobs', 'Author of Incidents in the Life of a Slave Girl, hidden seven years above a storeroom'),
    ('slave narrative', 'First person account by a formerly enslaved person, published with authenticating documents'),
    ('higher law', "Seward's 1850 doctrine of a law of God and nature above the Constitution"),
    ('Anthony Burns', 'Virginia fugitive whose Boston rendition of 1854 filled the city with federal troops and mourning crowds'),
    ('Kansas-Nebraska Act', "Douglas's law of May 30, 1854 that repealed the Missouri line of 1820"),
    ('popular sovereignty', "Douglas's doctrine leaving a territory's slavery question to its own people"),
    ('Bleeding Kansas', "Newspaper name for the Kansas Territory's guerrilla war of 1855 and 1856"),
    ('border ruffians', "Free state settlers' name for the Missourians who rode in to vote and to sack Lawrence"),
    ('Lecompton Constitution', 'Proslavery Kansas constitution whose referendum protected slavery even in rejection'),
    ('John Brown', 'Abolitionist of Pottawatomie and Harpers Ferry, hanged by Virginia on December 2, 1859'),
    ('Charles Sumner', "Massachusetts senator beaten at his Senate desk after the speech called The Crime Against Kansas"),
    ('Republican Party', 'Party organized in 1854 on the single plank of barring slavery from the federal territories'),
    ('free labor', 'Northern creed holding that the laborer had a right to rise by his work to property and independence'),
    ('John C. Frémont', "The Pathfinder, the new party's first presidential nominee in 1856"),
    ('Dred Scott v. Sandford', 'March 6, 1857 decision denying Black citizenship and the power of Congress over territorial slavery'),
    ('Roger B. Taney', 'Chief justice from 1836 who wrote the 1857 opinion meant to settle the slavery question'),
    ('Abraham Lincoln', 'Illinois lawyer who debated Douglas in 1858 and won the presidency in 1860'),
    ('House Divided speech', "Lincoln's June 16, 1858 address on a government half slave and half free"),
    ('Lincoln-Douglas debates', 'Seven open air Illinois debates of 1858, three hours each'),
    ('Freeport Doctrine', "Douglas's 1858 answer that a territory could starve slavery by withholding its police laws"),
    ('Harpers Ferry', 'Virginia arsenal town seized by Brown on October 16, 1859'),
    ('secession', 'Doctrine and act by which eleven states declared the Union dissolved, beginning December 20, 1860'),
    ('Crittenden Compromise', 'December 1860 proposal to write the Missouri line into the Constitution as an unamendable amendment'),
    ('Confederate States of America', 'Government organized at Montgomery in February 1861 by the first seven seceded states'),
    ('Jefferson Davis', 'Mississippi senator chosen president of the new southern government in February 1861'),
    ('Fort Sumter', 'Charleston harbor fort bombarded on April 12, 1861 and surrendered on April 14'),
    ('First Bull Run', 'July 21, 1861 battle near Manassas that ended the hope of a short war'),
    ('Anaconda Plan', "Scott's 1861 strategy of blockade and a drive down the Mississippi"),
    ('blockade', 'Naval closure of Confederate ports, enforced by a navy grown to some six hundred vessels'),
    ('habeas corpus', 'Constitutional writ Lincoln suspended along the military lines from 1861'),
    ('George B. McClellan', 'Organizer of the Army of the Potomac, removed in November 1862'),
    ('Antietam', 'September 17, 1862 battle near Sharpsburg, the single bloodiest day in American history'),
    ('contraband', "Butler's Fort Monroe name of May 1861 for enslaved people who reached the Union lines"),
    ('Emancipation Proclamation', 'Executive order in final form on January 1, 1863 freeing the enslaved in the rebellious states'),
    ('United States Colored Troops', 'Black regiments, some 180,000 men, who won equal pay in June 1864'),
    ('54th Massachusetts', 'Black regiment whose July 1863 assault on Fort Wagner cost its colonel and nearly half its men'),
    ('Gettysburg', "Pennsylvania battle of July 1 to 3, 1863 that stopped Lee's second invasion of the North"),
    ('Vicksburg', 'Mississippi River fortress surrendered to Grant on July 4, 1863 after a six week siege'),
    ('Gettysburg Address', 'Two minute dedication of November 19, 1863 on the proposition that all men are created equal'),
    ('Ulysses S. Grant', "General in chief from March 1864 who accepted Lee's surrender at Appomattox"),
    ('total war', "Strategy of war on the enemy's resources and will, carried fullest in Georgia and the Carolinas"),
    ('William Tecumseh Sherman', 'Ohio general who took Atlanta in September 1864 and marched to the sea'),
    ('March to the Sea', 'November and December 1864 march from Atlanta to Savannah in a corridor sixty miles wide'),
    ('Thirteenth Amendment', 'Amendment passed by Congress on January 31, 1865 abolishing slavery everywhere in the United States'),
    ('Appomattox Court House', "Virginia village of Lee's surrender on April 9, 1865"),
    ('Second Inaugural Address', 'March 4, 1865 address naming American slavery as the offense and the war as its woe'),
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
<title>Crossword: Sectional Crisis and Civil War</title>
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

<h1>Crossword: Sectional Crisis and Civil War</h1>
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
