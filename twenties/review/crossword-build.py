#!/usr/bin/env python3
"""Crossword generator for the Twenties review day.

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
SEED = 10  # fixed so the published grid is reproducible

# (answer, clue) -- answers are run together with no spaces, as in the pilot.
POOL = [
    ('HARLEMRENAISSANCE', 'The flowering of Black writing, music, and art in the 1920s, centered in Harlem in New York City'),
    ('WELFARECAPITALISM', "An employer's policy of providing benefits such as pensions, paid vacations, and recreation in order to keep workers satisfied and to keep unions out"),
    ('KELLOGBRIANDPACT', 'The agreement signed in Paris in 1928 in which the signing nations renounced war as an instrument of national policy'),
    ('GREATMIGRATION', 'The movement of hundreds of thousands of Black southerners to northern cities for jobs and greater rights'),
    ('MASSPRODUCTION', 'The making of goods in very large quantities using standardized parts and machinery, so that each item costs less to produce'),
    ('ORGANIZEDCRIME', 'Criminal activity carried out by a structured group that operates like a business, with leaders, ranks, territory, and regular sources of income'),
    ('FUNDAMENTALISM', 'A Protestant movement that defended a literal reading of the Bible and opposed public school teaching that conflicted with it'),
    ('CHICAGODEFENDER', 'The Black newspaper founded in Chicago in 1905 by Robert S. Abbott, which urged Black southerners to move north'),
    ('OVERPRODUCTION', 'Production of more of a good than buyers will purchase at prices that cover the cost of producing it'),
    ('ASSEMBLYLINE', 'A factory arrangement in which a product moves past workers who each add one part or perform one task until the product is finished'),
    ('BUYINGONMARGIN', 'Buying stock by paying only part of the price and borrowing the rest from a broker, with the stock pledged as security for the loan'),
    ('RADIONETWORK', 'A group of stations linked by wire that carry the same programs at the same time under one company'),
    ('QUOTASYSTEM', 'A method of limiting immigration by setting a fixed maximum number of immigrants that may be admitted from each country in a year'),
    ('BLACKTUESDAY', 'October 29, 1929, the day of the heaviest selling in the stock market crash of 1929'),
    ('VOLSTEADACT', 'The National Prohibition Act of 1919, the federal law that enforced the Eighteenth Amendment'),
    ('TEAPOTDOME', 'The scandal in which Secretary of the Interior Albert B. Fall secretly leased federal naval oil reserves to private oil companies'),
    ('ISOLATIONISM', 'A policy of avoiding political commitments and alliances with other countries while keeping a country free to act on its own'),
    ('SPECULATION', 'Buying an asset in the hope of selling it soon at a higher price, rather than for the income the asset produces'),
    ('ADVERTISING', 'Paid public messages that present a product to potential buyers and seek to create a desire to buy it'),
    ('CHAINSTORE', 'One of a group of retail stores owned by a single company, carrying the same name, goods, and prices across many locations'),
    ('MASSMEDIA', 'Forms of communication that reach very large audiences at the same time, including radio, film, and newspapers'),
    ('NEWNEGRO', 'A Black American of the 1920s who claimed dignity and equal rights and refused a second class place'),
    ('EUGENICS', 'A movement that claimed ability and character were inherited and could be ranked by ancestry'),
    ('KUKLUXKLAN', 'The organization revived in 1915 that claimed to defend white Protestant America and used intimidation and violence against those it declared un-American'),
    ('BOOTLEGGER', 'A person who illegally made, transported, or sold liquor during Prohibition'),
    ('SPEAKEASY', 'An illegal bar or club that sold liquor during Prohibition, often hidden behind a locked door'),
    ('PROHIBITION', 'The nationwide ban on the manufacture, sale, and transportation of intoxicating liquor for beverage purposes, from 1920 to 1933'),
    ('EVOLUTION', 'The scientific theory that species change over generations and that present species developed from earlier forms of life'),
    ('CELEBRITY', 'A person who is widely known and followed by the public because the media cover his or her life and work'),
    ('LINDBERGH', 'Charles, the pilot who flew alone from New York to Paris in May 1927'),
    ('COMMUTER', 'A person who travels regularly between home in one place and work in another, usually each day'),
    ('OPENSHOP', 'A workplace in which workers are not required to join a union in order to hold their jobs'),
    ('SUBURB', 'A residential area on the edge of a city, outside the center, where people live and travel into the city for work'),
    ('TALKIE', 'A motion picture with recorded dialogue and sound, which replaced silent film after 1927'),
    ('JAZZ', 'Music formed in Black communities of New Orleans from ragtime, blues, and brass band traditions'),
    ('UNIA', "The Universal Negro Improvement Association, Marcus Garvey's mass organization"),
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
<title>Crossword: The Twenties</title>
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

<h1>Crossword: The Twenties</h1>
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
