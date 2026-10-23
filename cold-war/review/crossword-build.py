#!/usr/bin/env python3
"""Crossword generator for the Cold War review day.

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
    ('HOUSEUNAMERICANACTIVITIESCOMMITTEE', 'The House committee that investigated alleged Communist influence in American life, most famously in its 1947 hearings on the film industry'),
    ('PEOPLESREPUBLICOFCHINA', 'The Communist state Mao Zedong proclaimed in 1949 after his forces won the Chinese civil war'),
    ('DISSOLUTIONOFTHESOVIETUNION', 'The ending of the Soviet Union in December 1991, when its republics declared independence'),
    ('STRATEGICDEFENSEINITIATIVE', 'President Reagan\'s 1983 proposal to build a defense in space against nuclear missiles, called Star Wars by its critics'),
    ('GULFOFTONKINRESOLUTION', 'The resolution Congress passed in August 1964 giving the president authority to take all necessary measures in Southeast Asia'),
    ('GERMANREUNIFICATION', 'The joining of East and West Germany into one state in October 1990'),
    ('ARMYMCCARTHYHEARINGS', 'The televised Senate hearings of 1954 after which the Senate censured Senator McCarthy'),
    ('LIMITEDTESTBANTREATY', 'The treaty of 1963 that banned nuclear weapons tests in the atmosphere, in space, and under water'),
    ('CUBANMISSILECRISIS', 'The confrontation of October 1962 in which the United States forced the withdrawal of Soviet nuclear missiles from Cuba'),
    ('BAYOFPIGSINVASION', 'The failed invasion of Cuba in April 1961 by Cuban exiles trained and supplied by the United States'),
    ('MASSIVERETALIATION', 'The Eisenhower policy of answering Communist aggression with the threat of a full nuclear strike'),
    ('SECONDREDSCARE', 'The fear from the late 1940s through the 1950s that Communists had infiltrated American government and institutions'),
    ('CUBANREVOLUTION', 'The revolution that brought Fidel Castro to power in Cuba in 1959'),
    ('HELSINKIACCORDS', 'The 1975 agreement in which the West recognized Europe\'s postwar borders and the Soviet bloc pledged respect for human rights'),
    ('TRUMANDOCTRINE', 'The policy President Truman declared in 1947, that the United States would support free peoples resisting attempted subjugation'),
    ('REAGANDOCTRINE', 'The policy of the 1980s under which the United States aided anti-Communist insurgencies fighting Soviet-backed governments'),
    ('BERLINAIRLIFT', 'The American and British air supply of West Berlin in 1948 and 1949, flown around the Soviet blockade'),
    ('MARSHALLPLAN', 'The American program of 1948 to 1952 that gave about thirteen billion dollars in aid to rebuild Western Europe'),
    ('38THPARALLEL', 'The line of latitude chosen in 1945 to divide occupation zones in Korea, which became the border between North and South Korea'),
    ('NAVALQUARANTINE', 'President Kennedy\'s name for the naval blockade of Cuba in 1962, chosen because a blockade is legally an act of war'),
    ('DOMINOTHEORY', 'The belief, stated by President Eisenhower in 1954, that if one country fell to communism its neighbors would fall one after another'),
    ('HYDROGENBOMB', 'A thermonuclear weapon far more powerful than the atomic bombs of 1945, first tested by the United States in 1952'),
    ('TETOFFENSIVE', 'The coordinated attacks across South Vietnam in January 1968 that shook American confidence in official claims of progress'),
    ('HOLLYWOODTEN', 'The ten screenwriters and directors who refused to answer committee questions in 1947 and went to prison for contempt'),
    ('IRONCURTAIN', 'The boundary Winston Churchill named in 1946 between the Soviet-dominated states of Eastern Europe and the free states of the West'),
    ('CONTAINMENT', 'The American strategy of blocking the further expansion of Soviet power and communism'),
    ('VIETNAMIZATION', 'President Nixon\'s policy of withdrawing American troops while building up South Vietnam\'s forces to carry the fighting'),
    ('BRINKMANSHIP', 'The practice of pushing a dangerous confrontation to the edge of war in order to force the other side to back down'),
    ('COVERTACTION', 'A secret government operation meant to influence events abroad while hiding the sponsor\'s hand'),
    ('DRAFTLOTTERY', 'The system begun in 1969 that chose the order in which young men were called for the draft by a random drawing of birth dates'),
    ('SUPERPOWER', 'A nation with power and influence far beyond that of other states, able to project strength across the world'),
    ('KOREANWAR', 'The war of 1950 to 1953 in which United States and United Nations forces fought North Korea and China'),
    ('INFTREATY', 'The treaty of 1987 in which the United States and the Soviet Union agreed to destroy all their land-based missiles with ranges between about 300 and 3,400 miles'),
    ('LIMITEDWAR', 'A war fought for limited aims with some weapons and targets deliberately left unused'),
    ('ARMSCONTROL', 'Negotiated limits on the weapons the superpowers could build or deploy, agreed in treaties'),
    ('EVILEMPIRE', 'President Reagan\'s name for the Soviet Union in a speech of March 1983'),
    ('BERLINWALL', 'The wall built in 1961 to stop East Germans fleeing to the West, breached by crowds on November 9, 1989'),
    ('WARSAWPACT', 'The military alliance formed in 1955 joining the Soviet Union and the Communist states of Eastern Europe'),
    ('MCCARTHYISM', 'The practice of making public accusations of Communist disloyalty without firm evidence, named for Senator Joseph McCarthy'),
    ('LOYALTYOATH', 'A sworn statement of loyalty and denial of Communist membership, required of federal employees during the Second Red Scare'),
    ('SOLIDARITY', 'The Polish labor movement founded in 1980 at the Gdansk shipyard, the first independent union in the Communist bloc'),
    ('PERESTROIKA', 'Gorbachev\'s program of restructuring the Soviet economy and political system'),
    ('DETERRENCE', 'The policy of preventing an enemy attack by holding a threat of retaliation so destructive that the attack would cost more than it could gain'),
    ('ESCALATION', 'The steady enlargement of a military commitment step by step, as the American ground force in Vietnam grew past half a million troops'),
    ('BLACKLIST', 'A list of people barred from employment in an industry because of suspected Communist ties'),
    ('VIETCONG', 'The Communist guerrilla forces and political organization in South Vietnam'),
    ('ARMSRACE', 'The competition between the United States and the Soviet Union to build more and more powerful weapons'),
    ('GLASNOST', 'Mikhail Gorbachev\'s policy of openness in the Soviet Union from 1985'),
    ('STALEMATE', 'A condition in fighting in which neither side can gain ground or force a decision'),
    ('ARMISTICE', 'An agreement to stop fighting; the Korean one of 1953 ended the shooting without a peace treaty'),
    ('SPUTNIK', 'The first artificial satellite, launched by the Soviet Union in October 1957'),
    ('HOTLINE', 'The direct communications link between Washington and Moscow established in 1963'),
    ('DETENTE', 'The easing of tension between the United States and the Soviet Union pursued in the 1970s'),
    ('NSC68', 'The secret American planning paper of 1950 that called for a large buildup of American military strength'),
    ('NATO', 'The alliance formed in 1949 in which an attack on one member was treated as an attack on all'),
    ('SALT', 'The Strategic Arms Limitation Talks, and the agreements they produced in 1972 and 1979'),
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
<title>Crossword: The Cold War</title>
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

<h1>Crossword: The Cold War</h1>
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
