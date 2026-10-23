#!/usr/bin/env python3
"""Crossword generator for the Colonial America review day.

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
SEED = 58  # fixed so the published grid is reproducible; chosen for the squarest grid (43 x 43) among the seeds tried, placing all 56 terms

# (answer, clue) -- answers are run together with no spaces, as in the pilot.
# Clues are short historical identifications, not definitions.
POOL = [
    ('COLUMBIANEXCHANGE', 'Crops, animals, diseases, and people carried both ways across the Atlantic after 1492'),
    ('TENOCHTITLAN', 'Aztec capital on an island in Lake Texcoco, entered by Spanish forces in 1519'),
    ('CAHOKIA', 'Mississippian city near present day St. Louis, known for its great earthen mounds'),
    ('IROQUOISCONFEDERACY', 'League of five, later six, Native nations in present day New York, joined under the Great Law'),
    ('CARAVEL', 'Small, fast Portuguese sailing ship of the 1400s used on long ocean voyages'),
    ('RECONQUISTA', 'Centuries of campaigns that took the Iberian Peninsula from Muslim rulers, completed in 1492'),
    ('EPIDEMIC', 'Smallpox and the other sicknesses that raced through the Americas after 1492, killing on a scale no army could match'),
    ('CONQUISTADOR', 'Spanish military leader of the 1500s conquests, among them Cortes in Mexico and Pizarro in Peru'),
    ('ENCOMIENDA', 'Grant that let a Spanish colonist demand tribute and labor from Indigenous people in a set area'),
    ('MESTIZO', 'In the caste order of Spanish America, a person of mixed Spanish and Indigenous ancestry'),
    ('NEWSPAIN', 'Spanish viceroyalty governed from Mexico City, stretching at its height from Panama to the present day American Southwest'),
    ('MISSION', 'Catholic settlement founded among Indigenous peoples on the Spanish and French borderlands'),
    ('FURTRADE', 'The exchange at the center of French colonization, manufactured goods traded to Indigenous hunters for beaver pelts'),
    ('HACIENDA', 'Large Spanish American estate that produced food and goods for nearby towns and mines'),
    ('JOINTSTOCKCOMPANY', 'Business form that funded the first English colonies, with investors pooling money and sharing costs, risks, and profits'),
    ('JAMESTOWN', 'First permanent English settlement in North America, planted on the James River in 1607'),
    ('CASHCROP', 'Tobacco was the Chesapeake version, grown for sale and profit rather than for the grower\'s own use'),
    ('HEADRIGHTSYSTEM', 'Virginia grant of fifty acres to anyone who paid an immigrant\'s passage to the colony'),
    ('INDENTUREDSERVANT', 'Laborer who worked four to seven years for the master who paid the passage, then claimed freedom dues'),
    ('HOUSEOFBURGESSES', 'Elected assembly that met at Jamestown in 1619, the first in English America'),
    ('BACONSREBELLION', 'Virginia uprising of 1676 that burned Jamestown and pushed great planters toward enslaved labor'),
    ('MAYFLOWERCOMPACT', 'Agreement signed aboard ship in 1620 that set up Plymouth\'s government by consent of the governed'),
    ('PURITANS', 'English Protestants who built Massachusetts Bay as a model godly society'),
    ('COVENANT', 'In Puritan belief, a solemn agreement with God binding a church or a whole community to live by his laws'),
    ('ANNEHUTCHINSON', 'Massachusetts dissenter tried and banished in 1637 and 1638 for teaching that faith alone brought salvation'),
    ('ROGERWILLIAMS', 'Minister banished in 1636 who founded Rhode Island on religious toleration'),
    ('FUNDAMENTALORDERSOFCONNECTICUT', 'Connecticut\'s governing document of 1639, often called the first written constitution in English America'),
    ('SALEMWITCHTRIALS', 'Crisis of 1692 in Massachusetts that hanged nineteen people on accusations of witchcraft'),
    ('MIDDLECOLONIES', 'New York, New Jersey, Pennsylvania, and Delaware, known for fertile soil, busy ports, and many peoples and faiths'),
    ('QUAKERS', 'Members of the Society of Friends, persecuted in England and New England, who rejected formal ministers and oaths'),
    ('WILLIAMPENN', 'Quaker proprietor who received Pennsylvania\'s charter in 1681'),
    ('PROPRIETARYCOLONY', 'Colony the king granted to an owner who held its land, named its governor, and drew its rents and fees'),
    ('MERCANTILISM', 'Theory holding that a nation\'s power grows by exporting more than it imports and holding colonies for raw materials and markets'),
    ('NAVIGATIONACTS', 'English laws from 1651 that routed colonial trade in English or colonial ships and sent listed goods only to England'),
    ('TRIANGULARTRADE', 'Atlantic pattern linking Europe, Africa, and the Americas in manufactured goods, enslaved people, and colonial produce'),
    ('MIDDLEPASSAGE', 'Atlantic crossing that carried enslaved Africans to the Americas in crowded ships where many died'),
    ('ATLANTICSLAVETRADE', 'Forced migration that, by the Trans-Atlantic Slave Trade Database estimates, carried some 12.5 million Africans from the 1500s to the 1800s, about 10.7 million of whom survived'),
    ('CHATTELSLAVERY', 'System that treated enslaved people as property to be bought, sold, and inherited, with children born enslaved for life'),
    ('SLAVECODES', 'Laws that denied enslaved people courts, assembly, and arms and punished resistance'),
    ('TASKSYSTEM', 'Lowcountry labor system that set a daily task, after which enslaved workers had the remaining time for their own work'),
    ('STONOREBELLION', 'Uprising of September 1739 near Charleston, when enslaved Africans seized weapons and marched toward Spanish Florida'),
    ('OLAUDAHEQUIANO', 'African writer kidnapped as a boy who bought his freedom and published his narrative in 1789'),
    ('SALUTARYNEGLECT', 'British practice of the early 1700s that left the colonies largely to govern themselves'),
    ('ZENGERTRIAL', 'New York trial of 1735 that acquitted a printer of seditious libel and became a landmark for freedom of the press'),
    ('GREATAWAKENING', 'Revival movement of the 1730s and 1740s that swept the colonies with personal faith and emotional preaching'),
    ('JONATHANEDWARDS', 'Massachusetts minister whose 1741 sermon Sinners in the Hands of an Angry God helped ignite revival in New England'),
    ('GEORGEWHITEFIELD', 'English preacher whose colonial tours drew open air crowds in the thousands'),
    ('ENLIGHTENMENT', 'European movement that prized reason, observation, and natural law, reaching the colonies through books, colleges, and print'),
    ('REVIVAL', 'Open air preaching gathering at the heart of the Great Awakening, meant to reawaken faith and convert sinners'),
    ('FRENCHANDINDIANWAR', 'North American war of 1754 to 1763 between Britain and France and their Indigenous allies'),
    ('SEVENYEARSWAR', 'Worldwide war of 1756 to 1763, fought across Europe, North America, the Caribbean, and Asia'),
    ('ALBANYPLANOFUNION', 'Franklin\'s 1754 proposal for one colonial government for defense, rejected by the assemblies and the Crown alike'),
    ('WILLIAMPITT', 'British statesman who took direction of the war in 1757 and paid for victory with borrowed millions'),
    ('TREATYOFPARIS1763', 'Treaty of February 1763 that gave Britain Canada and the French lands east of the Mississippi'),
    ('PONTIACSREBELLION', 'Uprising of 1763 in which Great Lakes and Ohio Valley nations attacked British forts after the French defeat'),
    ('PROCLAMATIONOF1763', 'Royal order of October 1763 that forbade colonial settlement west of the Appalachian Mountains'),
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
<title>Crossword: Colonial America</title>
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

<h1>Crossword: Colonial America</h1>
<p class="directions"><strong>Directions:</strong> Complete the crossword using the clues. Every answer is a word or run-together phrase from this unit's vocabulary. Multi-word answers have no spaces (for example, HOUSEOFBURGESSES).</p>

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
