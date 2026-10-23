#!/usr/bin/env python3
"""Crossword generator for the Early Republic and Expansion review day.

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
# punctuation dropped and digits kept, as in the Founding pool.
TERMS = [
    ("cabinet", "Advisers Washington formed from the department heads Congress created in 1789, an office the Constitution never names"),
    ("assumption", "Hamilton policy that had the United States take over the states' Revolutionary War debts"),
    ("excise tax", "1791 tax on distilled whiskey that helped pay for Hamilton's program and fell hardest on frontier farmers"),
    ("Bank of the United States", "National bank chartered in 1791 for twenty years that held the government's money and issued currency"),
    ("Whiskey Rebellion", "1794 western Pennsylvania uprising Washington answered by leading a militia army west"),
    ("cotton gin", "Whitney's 1794 patented machine that made short-staple cotton profitable across the inland South"),
    ("Farewell Address", "Washington's published letter of September 1796 warning against parties and permanent foreign alliances"),
    ("XYZ Affair", "1798 scandal in which French agents demanded a bribe and a loan before France would negotiate"),
    ("Alien Acts", "1798 laws stretching the citizenship wait to fourteen years and arming the president against immigrants"),
    ("Sedition Act", "1798 law under which Republican newspaper editors were tried and jailed for criticizing the government"),
    ("Virginia and Kentucky Resolutions", "1798 and 1799 resolutions, Madison's for Virginia and Jefferson's for Kentucky, claiming states could judge federal laws"),
    ("nullification", "Claim drawn from the Kentucky Resolutions that a state may declare a federal law void within its borders"),
    ("Twelfth Amendment", "Amendment ratified in 1804 requiring separate electoral ballots for president and vice president"),
    ("Revolution of 1800", "Jefferson's name for the 1801 transfer of power from Federalists to Democratic-Republicans by election"),
    ("strict construction", "Reading of the Constitution Jefferson wielded against the Bank and doubted over the Louisiana Purchase"),
    ("implied powers", "Powers drawn from the clause letting Congress make all laws necessary and proper to execute its listed powers"),
    ("Louisiana Purchase", "1803 treaty buying France's claim for fifteen million dollars and doubling the nation's territory"),
    ("midnight judges", "Judges Adams appointed in his presidency's last days whose undelivered commissions produced a famous lawsuit"),
    ("Marbury v. Madison", "1803 decision in which Marshall's Court surrendered a commission case and claimed a larger power"),
    ("judicial review", "Power the Supreme Court claimed in 1803 to declare acts of Congress unconstitutional and void"),
    ("Barbary Wars", "Wars of 1801 to 1805 and 1815 fought rather than keep paying tribute for merchant ships in the Mediterranean"),
    ("Corps of Discovery", "Army expedition of 1804 to 1806 Jefferson sent to explore the purchase and find a water route toward the Pacific"),
    ("Meriwether Lewis", "Army captain and former secretary to Jefferson who co-commanded the expedition and kept its scientific record"),
    ("William Clark", "Officer who co-commanded the expedition, drew its maps, and held its enslaved member as his property"),
    ("Sacagawea", "Shoshone interpreter who carried her infant across the continent and recognized her brother at the mountain meeting"),
    ("York", "Enslaved man who crossed the continent with the Corps, voted at Fort Clatsop, and was refused freedom for years"),
    ("Shoshone", "Northern Rockies nation, Sacagawea's people, whose horses the Corps needed to cross the mountains in 1805"),
    ("continental divide", "Rocky Mountain high ground the Corps crossed in 1805, separating Atlantic waters from Pacific waters"),
    ("impressment", "British practice of stopping American ships and forcing sailors, citizens among them, into the Royal Navy"),
    ("embargo", "Jefferson's 1807 policy closing every American port to foreign trade without firing a shot"),
    ("War Hawks", "Young congressmen led by Clay and Calhoun who pressed for war with Britain in 1811 and 1812"),
    ("Tecumseh", "Shawnee leader who built a confederacy on the claim that no single nation could sell land held in common"),
    ("Tippecanoe", "November 1811 fight at Prophetstown that burned the town and made Harrison's reputation"),
    ("Hartford Convention", "December 1814 New England Federalist meeting whose report arrived with news of peace and victory"),
    ("Treaty of Ghent", "Treaty signed December 24, 1814 restoring the boundaries of 1811 and saying nothing about impressment"),
    ("American System", "Clay's program of a national bank, a protective tariff, and internal improvements binding the sections"),
    ("Second Bank of the United States", "National bank chartered in 1816 after the war exposed the disorder of hundreds of state bank currencies"),
    ("protective tariff", "Import tax first enacted as national policy in 1816 to shelter American manufacturers"),
    ("internal improvements", "Roads, canals, and harbors Madison and Monroe agreed the nation needed and doubted Congress could fund"),
    ("Panic of 1819", "Financial collapse of 1819 in which the Second Bank's loan calls burst a land and cotton speculation"),
    ("McCulloch v. Maryland", "1819 decision holding Congress could charter a bank and Maryland could not tax it"),
    ("Gibbons v. Ogden", "1824 decision striking a state steamboat monopoly by reading commerce to include navigation"),
    ("Monroe Doctrine", "Policy declared December 2, 1823 holding the American continents closed to future European colonization"),
    ("John Quincy Adams", "Secretary of state who argued America should not come in as a cockboat in the wake of a British man of war"),
    ("Adams-Onís Treaty", "1819 treaty by which Spain ceded Florida and a boundary was drawn across the continent to the Pacific"),
    ("sectionalism", "Loyalty to one's section above the nation, exposed when Congress divided on slavery in 1819 and 1820"),
    ("Tallmadge Amendment", "1819 proposal that would have freed Missouri's enslaved children at twenty five and barred new importations"),
    ("Missouri Compromise", "1820 settlement pairing Maine and Missouri and drawing a slavery line across the Louisiana lands"),
    ("thirty-six thirty", "Parallel of latitude the Missouri Compromise drew across the Louisiana Purchase territory"),
    ("Manifest Destiny", "Name given in 1845 to the belief that providence destined the United States to overspread the continent"),
    ("annexation", "Method by which Texas joined the Union in 1845 by joint resolution after a treaty failed in the Senate"),
    ("Republic of Texas", "Independent nation declared in 1836 that waited nine years outside the Union over the slavery balance"),
    ("Oregon Country", "Pacific Northwest jointly occupied from 1818 and divided at the 49th parallel by treaty in 1846"),
    ("Mexican-American War", "War of 1846 to 1848 begun over the Texas boundary and ended with Mexico ceding half its territory"),
    ("Wilmot Proviso", "1846 proposal, passed by the House and blocked in the Senate, to bar slavery in territory taken from Mexico"),
    ("Treaty of Guadalupe Hidalgo", "Treaty of February 2, 1848 confirming the Rio Grande boundary and transferring California and New Mexico"),
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
<title>Crossword: The Early Republic and Expansion</title>
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

<h1>Crossword: The Early Republic and Expansion</h1>
<p class="directions"><strong>Directions:</strong> Complete the crossword using the clues. Every answer is a word or run-together phrase from this unit's vocabulary. Multi-word answers have no spaces (for example, LOUISIANAPURCHASE). Punctuation is dropped (for example, MARBURYVMADISON).</p>

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
    for seed in range(1, 251):
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
        if successes >= 10:
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
