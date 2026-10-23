#!/usr/bin/env python3
"""Crossword generator for the Founding review day.

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
SEED = 360  # fixed so the published grid is reproducible; chosen for the most compact grid (43 x 44) among the 400 seeds tried, placing all 56 terms

# (answer, clue) -- answers are run together with no spaces, as in the pilot.
# Clues are short historical identifications, not definitions.
POOL = [
    ("STAMPACT", "1765 British tax on newspapers, legal documents, and playing cards, collected through stamped paper"),
    ("REPEAL", "What Parliament did to the Stamp Act in March 1766 after boycotts and British merchants' petitions"),
    ("DECLARATORYACT", "1766 law passed the same day as the Stamp Act's repeal, claiming power over the colonies in all cases whatsoever"),
    ("TOWNSHENDACTS", "1767 duties on tea, glass, lead, paint, and paper imports, with the revenue paying royal governors and judges"),
    ("BOYCOTT", "Refusal to buy British goods, organized by merchants and made real by households spinning homespun"),
    ("VIRTUALREPRESENTATION", "British claim that members of Parliament spoke for colonists who had never voted for them"),
    ("BOSTONMASSACRE", "March 5, 1770 clash in which soldiers fired on a taunting crowd, killing five, Crispus Attucks among them"),
    ("TEAACT", "1773 law letting the East India Company sell tea directly in the colonies while the tea tax stayed in place"),
    ("BOSTONTEAPARTY", "December 16, 1773 protest that emptied 342 chests of tea into Boston Harbor"),
    ("INTOLERABLEACTS", "1774 laws closing Boston's port and rewriting the Massachusetts charter, passed to punish the Tea Party"),
    ("FIRSTCONTINENTALCONGRESS", "1774 Philadelphia meeting of twelve colonies that declared colonial rights and organized a boycott of British goods"),
    ("MINUTEMEN", "Massachusetts militiamen who turned out along the road from Lexington and Concord on April 19, 1775"),
    ("LOYALIST", "Colonist who stayed with Britain during the Revolution, from conviction, interest, or fear of the rebellion's disorder"),
    ("PATRIOT", "Colonist who took the rebellion's side, from the resistance of 1773 to independence in 1776"),
    ("COMMONSENSE", "Paine's January 1776 pamphlet arguing in plain language that monarchy itself was corrupt"),
    ("NATURALRIGHTS", "Rights held to belong to all people by nature, life, liberty, and the pursuit of happiness among them in the Declaration"),
    ("UNALIENABLERIGHTS", "Rights the Declaration says a Creator gives to all men and no government may rightly take away"),
    ("CONSENTOFTHEGOVERNED", "Ground of just power in the Declaration, the agreement of the people a government rules"),
    ("SOCIALCONTRACT", "Theory that rulers and ruled hold each other to an agreement, protection of rights exchanged for obedience to law"),
    ("REPUBLIC", "Form the American states adopted after independence, representatives chosen by citizens and no king"),
    ("DECLARATIONOFINDEPENDENCE", "Document adopted July 4, 1776, written chiefly by Jefferson, declaring the colonies free and independent states"),
    ("CONTINENTALARMY", "Army Congress created in June 1775 and gave to Washington, drawn from all thirteen colonies"),
    ("MILITIA", "Local citizen soldiers who served part time near home and could be called out in emergencies"),
    ("GEORGEWASHINGTON", "Virginian chosen in 1775 to command the Continental Army, whose strategy of keeping the army in being carried the cause to Yorktown"),
    ("VALLEYFORGE", "Pennsylvania winter camp of 1777 and 1778 where von Steuben drilled the army into a professional force"),
    ("BATTLEOFSARATOGA", "Fall 1777 victory in upper New York where Burgoyne surrendered, the win that brought France openly into the war"),
    ("TREATYOFALLIANCE", "February 1778 treaty by which France recognized the United States and joined the war against Britain"),
    ("BATTLEOFYORKTOWN", "Fall 1781 trap in Virginia where allied armies and a French fleet forced Cornwallis to surrender"),
    ("DUNMORESPROCLAMATION", "November 1775 order by Virginia's royal governor offering freedom to enslaved people held by rebels who bore arms for the king"),
    ("INFLATION", "Rise in prices as Congress printed paper money faster than the states could support it"),
    ("CAMPFOLLOWERS", "Women and children who cooked, washed, and nursed for the armies and were paid little or nothing"),
    ("DEBORAHSAMPSON", "Massachusetts woman who served over a year in the Continental Army as Robert Shurtliff"),
    ("JOSEPHBRANT", "Mohawk leader called Thayendanegea who led Haudenosaunee forces allied with Britain"),
    ("SULLIVANEXPEDITION", "1779 campaign ordered by Washington that burned some forty Seneca and Cayuga towns and their cornfields"),
    ("GRADUALEMANCIPATION", "Northern method of ending slavery slowly, freeing children born to enslaved mothers only after years of service"),
    ("ARTICLESOFCONFEDERATION", "First United States constitution, ratified in 1781, joining the states in a league that left most power with the states"),
    ("CONFEDERATION", "League of independent states that keep their sovereignty and join for limited common purposes"),
    ("REQUISITION", "Congressional request under the Articles asking a state for money or troops, which the state could lawfully refuse or ignore"),
    ("LANDORDINANCEOF1785", "1785 law surveying the western lands into townships and lots, setting the grid still visible across the Midwest"),
    ("NORTHWESTORDINANCE", "1787 law for the territory north of the Ohio, barring slavery there and promising statehood on equal terms"),
    ("SHAYSSREBELLION", "Uprising of indebted western Massachusetts farmers in 1786 and 1787 who closed courts to stop foreclosures"),
    ("ANNAPOLISCONVENTION", "September 1786 meeting of five states that called for a convention at Philadelphia to repair the federal government"),
    ("CONSTITUTIONALCONVENTION", "Philadelphia meeting of May to September 1787 that wrote the Constitution instead of only revising the Articles"),
    ("VIRGINIAPLAN", "Madison's plan for a strong national government with a legislature apportioned by population"),
    ("NEWJERSEYPLAN", "Small states' plan keeping a one house legislature with equal votes for every state"),
    ("GREATCOMPROMISE", "Settlement giving the House of Representatives to population and the Senate two members to every state"),
    ("THREEFIFTHSCOMPROMISE", "Settlement counting each enslaved person as three fifths of a person for representation and direct taxes"),
    ("FEDERALISM", "Division of power between a national government and state governments, each supreme in its own sphere"),
    ("SEPARATIONOFPOWERS", "Division of the federal government into legislative, executive, and judicial branches that check one another"),
    ("RATIFICATION", "Formal approval of the Constitution by conventions in nine of the thirteen states"),
    ("FEDERALISTS", "Supporters of the Constitution in the contests of 1787 and 1788 who argued the union needed a stronger national government"),
    ("ANTIFEDERALISTS", "Opponents of the Constitution who argued it threatened liberty, above all by omitting a bill of rights"),
    ("FEDERALISTPAPERS", "Eighty five essays by Hamilton, Madison, and Jay under the name Publius, written to persuade New York to ratify"),
    ("FACTION", "In Madison's argument in Federalist No. 10, citizens united by a passion or interest harmful to the rights of others"),
    ("BILLOFRIGHTS", "First ten amendments to the Constitution, ratified by the states by December 1791"),
    ("AMENDMENT", "Formal change to the Constitution, proposed by two thirds of Congress and ratified by three fourths of the states"),
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
    cell = max(0.20, min(0.325, 6.9 / max(H, W)))
    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>Crossword: The Founding</title>
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

<h1>Crossword: The Founding</h1>
<p class="directions"><strong>Directions:</strong> Complete the crossword using the clues. Every answer is a word or run-together phrase from this unit's vocabulary. Multi-word answers have no spaces (for example, BOSTONTEAPARTY). Numbers and apostrophes are dropped (for example, SHAYSSREBELLION).</p>

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
