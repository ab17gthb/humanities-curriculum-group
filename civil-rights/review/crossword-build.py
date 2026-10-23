#!/usr/bin/env python3
"""Crossword generator for the Civil Rights review day.

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
SEED = 6  # fixed so the published grid is reproducible; chosen over 7 for a squarer grid (51 x 53) that fits the page better

# (answer, clue) -- answers are run together with no spaces, as in the pilot.
POOL = [
    ('SOUTHERNCHRISTIANLEADERSHIPCONFERENCE', 'The organization founded in 1957 by Martin Luther King Jr. and other Black ministers to coordinate nonviolent protest across the South'),
    ('STUDENTNONVIOLENTCOORDINATINGCOMMITTEE', 'The organization founded by student activists in April 1960, known as SNCC, which organized sit-ins, Freedom Rides, and voter registration drives'),
    ('MISSISSIPPIFREEDOMDEMOCRATICPARTY', 'The integrated political party organized in Mississippi in 1964 that challenged the seating of the state\'s all-white regular delegation at Atlantic City'),
    ('16THSTREETBAPTISTCHURCHBOMBING', 'The bombing of a Birmingham church on September 15, 1963, which killed four Black girls as they prepared for Sunday services'),
    ('LETTERFROMBIRMINGHAMJAIL', 'Martin Luther King Jr.\'s letter of April 1963, written from a Birmingham jail cell, defending nonviolent direct action'),
    ('BROWNVBOARDOFEDUCATION', 'The Supreme Court decision of May 17, 1954 that declared segregation in public schools unconstitutional'),
    ('KENNEDYSCIVILRIGHTSADDRESS', 'President Kennedy\'s televised address of June 11, 1963 calling civil rights a moral issue and announcing a comprehensive civil rights bill'),
    ('TOSECURETHESERIGHTS', 'The 1947 report of President Truman\'s Committee on Civil Rights, which called for federal laws against lynching and disfranchisement'),
    ('CONGRESSOFRACIALEQUALITY', 'The civil rights organization founded in 1942, known as CORE, which pioneered nonviolent direct action and organized the Freedom Rides'),
    ('EXECUTIVEORDER9981', 'President Truman\'s order of July 26, 1948 directing equality of treatment and opportunity for all persons in the armed forces'),
    ('EXECUTIVEORDER10730', 'President Eisenhower\'s order of September 24, 1957 federalizing the Arkansas National Guard to enforce school desegregation at Little Rock'),
    ('MONTGOMERYBUSBOYCOTT', 'The protest of 1955 and 1956 in which Black residents of Montgomery, Alabama refused to ride the city\'s buses for 381 days'),
    ('NONVIOLENTDIRECTACTION', 'Protest that confronts an unjust law or practice openly and without violence, accepting arrest in order to expose the injustice'),
    ('CHICAGOFREEDOMMOVEMENT', 'Martin Luther King Jr.\'s campaign of 1966 against housing and school segregation in Chicago'),
    ('CIVILRIGHTSACTOF1964', 'The federal law that banned discrimination in public accommodations and employment and allowed the government to cut off funds to segregated programs'),
    ('VOTINGRIGHTSACTOF1965', 'The federal law that suspended literacy tests, sent federal examiners to register voters in covered states, and required preclearance of voting changes'),
    ('POORPEOPLESCAMPAIGN', 'Martin Luther King Jr.\'s planned campaign of 1968 to bring an interracial army of the poor to Washington to demand federal action on poverty'),
    ('MEMPHISSANITATIONSTRIKE', 'The strike of 1968 by Black sanitation workers in Memphis, Tennessee, whose signs read I Am a Man'),
    ('BIRMINGHAMCAMPAIGN', 'The protest campaign of 1963 in Birmingham, Alabama, whose televised repression pushed President Kennedy to propose a national civil rights bill'),
    ('MASSIVERESISTANCE', 'The campaign by southern state governments after Brown to prevent school desegregation, using new laws, defiance, and school closings'),
    ('MARCHONWASHINGTON', 'The demonstration of August 28, 1963 that brought about 250,000 people to the Lincoln Memorial to demand jobs and freedom'),
    ('DEFACTOSEGREGATION', 'Segregation in fact rather than in law, produced by housing patterns, economics, and custom, the form segregation took in the North'),
    ('DEJURESEGREGATION', 'Segregation imposed and enforced by law, as under the southern statutes the courts struck down one by one'),
    ('CHILDRENSCRUSADE', 'The marches of May 1963 in Birmingham in which thousands of Black schoolchildren were met with fire hoses, police dogs, and jail'),
    ('GREENSBOROSITIN', 'The protest of February 1, 1960 in which four Black college students sat at a segregated Woolworth lunch counter in North Carolina'),
    ('AFFIRMATIVEACTION', 'Government policies that take race into account in hiring, contracting, and college admissions in order to remedy past discrimination'),
    ('DISFRANCHISEMENT', 'The denial of the right to vote through law or practice'),
    ('KERNERCOMMISSION', 'The federal commission whose 1968 report concluded that the nation was moving toward two societies, one black, one white, separate and unequal'),
    ('BLACKPANTHERPARTY', 'The organization founded in Oakland, California in 1966 by Huey Newton and Bobby Seale'),
    ('SEPARATEBUTEQUAL', 'The doctrine set in Plessy v. Ferguson in 1896, holding segregation constitutional as long as facilities for each race were equal'),
    ('SOUTHERNMANIFESTO', 'The declaration of 1956 signed by 101 southern members of Congress denouncing Brown as an abuse of judicial power'),
    ('SOUTHERNSTRATEGY', 'The Republican electoral strategy of the Nixon years that sought white southern voters by opposing federal civil rights enforcement and busing'),
    ('PLESSYVFERGUSON', 'The 1896 Supreme Court decision that upheld segregation under the doctrine of separate but equal'),
    ('DOUBLEVCAMPAIGN', 'The campaign led by Black newspapers from 1942 for victory over fascism abroad and victory over racism at home'),
    ('FAIRHOUSINGACT', 'The Civil Rights Act of 1968, passed in the week after Martin Luther King Jr.\'s assassination, banning discrimination in most housing'),
    ('ALBANYMOVEMENT', 'The campaign of 1961 and 1962 in Albany, Georgia, where polite mass arrests denied the movement a televised crisis'),
    ('LITTLEROCKNINE', 'The nine Black students who desegregated Central High School in Little Rock, Arkansas in 1957 under federal troops'),
    ('COOPERVAARON', 'The Supreme Court decision of 1958, arising from Little Rock, holding that state officials are bound by the Court\'s interpretation of the Constitution'),
    ('FREEDOMSUMMER', 'The campaign of 1964 that brought about a thousand mostly northern student volunteers to Mississippi to register Black voters'),
    ('WHITEBACKLASH', 'The political reaction among white voters against the pace and reach of civil rights change'),
    ('WATTSUPRISING', 'The six days of violence in the Watts neighborhood of Los Angeles in August 1965, in which thirty four people died'),
    ('FREEDOMRIDES', 'The bus journeys of 1961 in which interracial groups rode through the South to test court orders desegregating interstate travel'),
    ('BAKKEDECISION', 'The Supreme Court decision of 1978 which struck down a set-aside of seats by race in admissions and allowed race as one factor among others'),
    ('BLOODYSUNDAY', 'The attack of March 7, 1965 on voting rights marchers at the Edmund Pettus Bridge in Selma, televised to the nation'),
    ('IHAVEADREAM', 'Martin Luther King Jr.\'s address closing the March on Washington on August 28, 1963'),
    ('BLACKPOWER', 'The call raised by Stokely Carmichael in Mississippi in June 1966 for Black Americans to build their own political and economic power'),
    ('SEGREGATION', 'The separation of people by race in public facilities, schools, and transportation'),
    ('EMMETTTILL', 'The fourteen-year-old Chicago boy murdered in Mississippi in August 1955, whose open-casket funeral showed the nation southern racial violence'),
    ('FILIBUSTER', 'The Senate practice of extending debate to block a bill from coming to a vote, broken on the civil rights bill of 1964 by cloture'),
    ('TITLEVII', 'The section of the Civil Rights Act of 1964 that banned discrimination in employment on the basis of race, color, religion, sex, or national origin'),
    ('JIMCROW', 'The system of state and local laws and customs that enforced racial segregation in the South'),
    ('BOYCOTT', 'A refusal to buy goods or use services as a form of protest, meant to pressure an institution by withdrawing the money it depends on'),
    ('BROWNII', 'The Supreme Court\'s 1955 decision ordering school desegregation to proceed with all deliberate speed'),
    ('SITIN', 'A protest in which demonstrators seat themselves at a segregated facility and refuse to leave until they are served on equal terms or arrested'),
    ('BUSING', 'Court-ordered transportation of students across neighborhood lines to desegregate schools, upheld by the Supreme Court in Swann in 1971'),
    ('NAACP', 'The National Association for the Advancement of Colored People, founded in 1909, which fought segregation through the courts'),
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
<title>Crossword: The Civil Rights Movement</title>
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

<h1>Crossword: The Civil Rights Movement</h1>
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
    rows = [r for r, _ in grid]; cols = [c for _, c in grid]
    print(f"grid: {max(rows)-min(rows)+1} rows x {max(cols)-min(cols)+1} cols")
    print(f"answers placed: {len(placements)} ({len(across)} across, {len(down)} down)")
    print(f"crossing check: PASS, {crossings} shared cells verified, every letter agrees")
    print("unplaced from pool:", ", ".join(w for w, _ in unplaced) or "none")
    print("wrote", out)


if __name__ == "__main__":
    main()
