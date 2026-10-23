#!/usr/bin/env python3
"""Crossword generator for the Reconstruction review day.

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
    ('Reconstruction', 'Twelve year postwar era that closed with the troop withdrawal of 1877'),
    ('Andrew Johnson', 'Tennessee tailor and Unionist who succeeded Lincoln in April 1865'),
    ('presidential Reconstruction', 'Restoration program run from the White House in 1865, before Congress took charge'),
    ("Freedmen's Bureau", 'Federal agency of March 1865 that ran hospitals, courts, and schools across the South'),
    ('Black Codes', 'Statutes of 1865 and 1866 tying freedpeople to plantations through vagrancy and apprenticeship rules'),
    ('Amnesty Proclamation', "Johnson's May 29, 1865 offer of pardon on a loyalty oath, with fourteen excepted classes"),
    ('Jourdon Anderson', 'Tennessee freedman who answered his former enslaver with a demand for thirty two years of back wages'),
    ('Thirteenth Amendment', 'Amendment ratified in December 1865 that ended slavery everywhere in the United States'),
    ('Civil Rights Act of 1866', 'First major law passed over a presidential veto, in April 1866, declaring birthright citizenship by statute'),
    ('Radical Republicans', 'Faction led by Stevens in the House and Sumner in the Senate demanding equal rights as the price of restoration'),
    ('Thaddeus Stevens', 'Pennsylvania congressman who called the seceded states conquered provinces and demanded land for freed families'),
    ('Lyman Trumbull', 'Illinois senator and Judiciary chairman who wrote the Civil Rights Act of 1866'),
    ("freedmen's conventions", 'State assemblies of 1865 and 1866 where the emancipated petitioned for land, schools, and the ballot'),
    ('freedpeople', "Historians' name for the roughly four million emancipated by the war and the Thirteenth Amendment"),
    ('Fourteenth Amendment', 'Amendment ratified in 1868 writing birthright citizenship and equal protection into the Constitution'),
    ('Reconstruction Acts', 'Laws of March 1867 that set aside ten state governments and required new constitutions with Black male suffrage'),
    ('military districts', 'Five command zones covering the ten unreconstructed states under Union generals'),
    ('Joint Committee on Reconstruction', 'Fifteen member congressional committee of December 1865 that drafted the Fourteenth Amendment'),
    ('Tenure of Office Act', 'Law of March 1867 barring removal of Senate confirmed officials without Senate consent'),
    ('Edwin M. Stanton', "Lincoln's war secretary whose February 1868 removal triggered impeachment"),
    ('impeachment', 'Process of House charges and a Senate trial, decided against Johnson by one vote short of two thirds'),
    ('Fifteenth Amendment', 'Amendment ratified in February 1870 barring denial of the vote for race, color, or previous servitude'),
    ('Hiram Rhodes Revels', 'Mississippi minister seated in the United States Senate in 1870 in the chamber Jefferson Davis had left'),
    ('Blanche K. Bruce', 'Mississippi senator of 1874, born enslaved, the first Black senator to serve a full term'),
    ('P. B. S. Pinchback', 'Louisiana leader who governed his state for five weeks in the winter of 1872 and 1873'),
    ('carpetbaggers', 'Hostile Democratic label for northern men who came South as teachers, merchants, veterans, and office seekers'),
    ('scalawags', 'Hostile Democratic label for white southerners who joined the Republican Party'),
    ('Union League', 'Patriotic clubs that organized Black voters in churches and schoolhouses from 1867'),
    ('Special Field Orders No. 15', "Sherman's January 16, 1865 order reserving a coastal strip for freed families in plots up to forty acres"),
    ('forty acres and a mule', "Freedpeople's shorthand for the land settlement expected from a Sherman order and army mules"),
    ('sharecropping', 'System in which a family farmed a plot for a share of the crop, commonly half, settling once a year'),
    ('crop lien', "Merchant's legal claim on an unplanted crop, given for seed, tools, and food advanced on credit"),
    ("freedmen's schools", 'Schools enrolling some quarter of a million students by 1870, sustained in part by freedpeople taxing themselves'),
    ('African Methodist Episcopal Church', 'Independent Black denomination of 1816 whose meetinghouses doubled as schoolhouses and league halls after the war'),
    ("Freedmen's Savings Bank", 'Bank chartered in March 1865 for Black soldiers and freed families, brought down in 1874 after the Panic'),
    ('Ku Klux Klan', 'Secret terrorist order founded at Pulaski, Tennessee, in 1866 and spread as the Invisible Empire'),
    ('Nathan Bedford Forrest', 'Former Confederate cavalry general and Memphis slave trader elected the first Grand Wizard in 1867'),
    ('Abram Colby', 'Georgia legislator whipped in October 1869 who named his attackers and refused their bribes before Congress in 1872'),
    ('night riding', 'Mounted, disguised after dark visits that whipped or shot targets as an instruction to a whole community'),
    ('Enforcement Acts', 'Three laws of 1870 and 1871 arming federal power against election violence and rights conspiracies'),
    ('Ku Klux Klan Act', 'Third Enforcement Act of April 1871 under which Grant broke the first Klan in South Carolina'),
    ('federal marshals', 'Federal court officers empowered to guard polls, arrest election offenders, and summon posses'),
    ('Slaughter-House Cases', 'Five to four decision of April 1873, the first reading of the Fourteenth Amendment, narrowing it to national citizenship rights'),
    ('Amnesty Act of 1872', 'Law of May 1872 removing officeholding disability from nearly all former Confederates'),
    ('Liberal Republicans', 'Reform faction that broke with Grant in 1872 and nominated Horace Greeley'),
    ('Panic of 1873', "Collapse opened by Jay Cooke's banking house failure in September 1873, settling into a six year depression"),
    ('White League', 'Louisiana paramilitary organization of 1874 that fought at Coushatta and at Liberty Place'),
    ('Civil Rights Act of 1875', "Sumner's last cause, enacted March 1875, guaranteeing equal enjoyment of inns, conveyances, and theaters"),
    ('Thomas Nast', "Harper's Weekly cartoonist of the Tweed Ring fight whose pen indicted the Klan and pictured Colored Rule"),
    ('Compromise of 1877', 'Informal bargain seating Hayes in return for a cabinet seat, internal improvements, and the last troop withdrawals'),
    ('Rutherford B. Hayes', 'Ohio Republican who lost the popular vote in 1876 and ordered the last troops from Columbia and New Orleans in April 1877'),
    ('Samuel J. Tilden', 'New York governor who won the 1876 popular vote by some quarter of a million'),
    ('Electoral Commission', 'Fifteen member body of January 1877 that awarded every disputed electoral vote eight to seven'),
    ('Redeemers', 'White Democratic leaders who retook southern governments promising low taxes and white supremacy'),
    ('home rule', "Redeemers' slogan for ending federal supervision of southern governments and elections"),
    ('Redemption', 'Name white Democrats gave their state by state overthrow of the Reconstruction governments, completed in spring 1877'),
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
<title>Crossword: Reconstruction</title>
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

<h1>Crossword: Reconstruction</h1>
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
