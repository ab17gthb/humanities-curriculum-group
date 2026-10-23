#!/usr/bin/env python3
"""Build the Reformer's Notebook as print-ready HTML (base64 images embedded)
and export a PDF via headless Chromium. Alex's format: PDF deliverable, all
black, name/date/period across the top, blank writing space, key at back."""
import base64, io, os, subprocess
from PIL import Image

BASE = "/home/hatch/workspace/curriculum-planner/progressive-era/lesson-01"
A = BASE + "/assets/"

def img64(path, max_w=1000):
    im = Image.open(path).convert("RGB")
    if im.width > max_w:
        im = im.resize((max_w, int(im.height * max_w / im.width)))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=82)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

IMGS = {
    "breaker": img64(A + "breaker-boys-interior.jpg"),
    "riis": img64(A + "riis-lodgers.jpg"),
    "nast": img64(A + "tweed-nast.jpg"),
    "octopus": img64(A + "standard-oil-octopus.jpg"),
}
LOGO = img64("/home/hatch/workspace/curriculum-planner/assets/crossroads-simple-logo.png", max_w=940)

CSS = """
@page { size: letter; margin: 0.7in 0.75in; }
* { box-sizing: border-box; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 11.5pt; color: #000; line-height: 1.35; margin: 0; }
.nameline { display: flex; justify-content: space-between; gap: 1em; }
h1 { font-size: 19pt; margin: 12pt 0 4pt; line-height: 1.2; }
h2 { font-size: 14.5pt; margin: 16pt 0 6pt; }
h3 { font-size: 12.5pt; margin: 14pt 0 4pt; }
p { margin: 0 0 7pt; }
.directions { margin-bottom: 4pt; }
.source { margin-bottom: 4pt; }
figure { margin: 6pt 0 8pt; text-align: center; break-inside: avoid; }
figure img { max-width: 3.9in; max-height: 2.3in; }
figcaption { font-size: 9pt; font-style: italic; margin-top: 3pt; }
.q { margin: 8pt 0 0; }
.space { height: 0.72in; }
.space-lg { height: 1.9in; }
h3 { break-after: avoid; }
.key { break-before: page; }
.key h2:first-child { margin-top: 0; }
ul { margin: 2pt 0 8pt 16pt; padding: 0; }
li { margin-bottom: 3pt; }
.rank p { margin: 0 0 5pt; }
.credit { font-size: 9pt; text-align: center; margin-top: 18pt; }
"""

def station(num, title, source, img, caption, body, q1, q2):
    return f"""
<section class="station">
<h3>Station {num}: {title}</h3>
<p class="source">{source}</p>
<figure><img src="{img}" alt=""><figcaption>{caption}</figcaption></figure>
<p>{body}</p>
<p class="q">{q1}</p><div class="space"></div>
<p class="q">{q2}</p><div class="space"></div>
</section>"""

html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>Reformer's Notebook: The Problems Progressives Faced</title>
<style>{CSS}</style></head><body>

<div class="nameline"><span>Name ______________________</span><span>Date ______________</span><span>Period __________</span></div>

<h1>Reformer's Notebook: The Problems Progressives Faced</h1>
<p class="directions"><strong>Directions:</strong> Read the sources at all four stations to understand the crises that sparked the Progressive movement, then answer the questions for each stop. After reviewing all four problems, complete the final verdict section to rank their urgency.</p>

<h2>Part 1: Four Stops</h2>

{station(1, "Dangerous Industrial Work and Child Labor",
  'Source: Description of a photograph by Lewis Hine, "Breaker Boys inside the Coal Breaker," 1911.',
  IMGS["breaker"],
  "The photograph itself: breaker boys at work inside the Ewen Breaker, South Pittston, Pennsylvania, 1911. Lewis Hine, Library of Congress.",
  "The photograph shows a row of young boys, some appearing as young as nine or ten years old, sitting on wooden planks over coal chutes. Their faces, clothes, and arms are completely covered in thick black coal dust. They are hunched forward in a dark, cramped room, picking sharp pieces of slate out of the rough coal with their bare, calloused hands.",
  "What does this source show about the nature of industrial work during this period?",
  "Who was primarily hurt by these conditions, and what were the physical or developmental costs to them?")}

{station(2, "Tenement Life in Crowded Cities",
  "Source: Summary of Jacob Riis, How the Other Half Lives, 1890.",
  IMGS["riis"],
  "Lodgers in a crowded Bayard Street tenement. Jacob Riis, from How the Other Half Lives.",
  "Riis describes a tenement hallway so dark that a visitor might stumble over children playing in the shadows. He notes that the air inside is foul and the buildings are packed tightly with immigrant families. In one small, unventilated room, he observes multiple people sleeping on the bare floor, breathing stale air filled with the overwhelming smell of summer heat and garbage from the alley below.",
  "What does this description reveal about the housing conditions for the urban poor?",
  "Who suffered the most in these environments, and how did it affect their daily health and safety?")}

{station(3, "Corrupt Political Machines",
  "Source: Summary of George Washington Plunkitt's interviews in William L. Riordon's Plunkitt of Tammany Hall, 1905.",
  IMGS["nast"],
  "Thomas Nast cartoon on corruption, Harper's Weekly, 1872.",
  'Plunkitt proudly explains his system of "honest graft." When he learns the city plans to build a new public park, he secretly buys the targeted land in advance. He then sells it back to the city at a massive profit. He claims he is just seeing opportunities and taking them, arguing this is exactly how political leaders should reward themselves and their loyal voters.',
  "What does this source demonstrate about how political machines operated in major cities?",
  "Who was ultimately cheated by this system, and how did it damage the democratic process?")}

{station(4, "The Power of Trusts",
  "Source: Summary of Ida Tarbell, The History of the Standard Oil Company, 1904.",
  IMGS["octopus"],
  "The Standard Oil octopus. Puck magazine, 1904.",
  "Tarbell details how John D. Rockefeller's company used its massive wealth and size to force railroads into giving them secret, illegal discounts on shipping oil. By cutting his transportation costs, Rockefeller could drop his oil prices so low that small, independent oil refiners were driven into bankruptcy. Once the local competitors were destroyed, Standard Oil controlled the entire market and raised prices again.",
  "What does this summary reveal about the business tactics used by large trusts to gain power?",
  "Who was financially hurt by these monopolies, and how did it affect the broader economy?")}

<h2>Part 2: Your Verdict</h2>
<p>Rank the four problems from 1 to 4 based on how urgently they needed to be fixed in the year 1900. (1 = Most Urgent, 4 = Least Urgent).</p>
<div class="rank">
<p>______ &nbsp;Dangerous Industrial Work and Child Labor</p>
<p>______ &nbsp;Tenement Life in Crowded Cities</p>
<p>______ &nbsp;Corrupt Political Machines</p>
<p>______ &nbsp;The Power of Trusts</p>
</div>
<p class="q">Defend your top choice (your number 1 ranking) in a short paragraph. You must use specific evidence from your top choice's station and compare it to evidence from at least one other station to prove why your choice was the most urgent threat to the nation.</p>
<div class="space-lg"></div>
<p class="credit">Created by Crossroads History Studio</p>

<div class="key">
<h2>Teacher Answer Key</h2>

<h3>Station 1: Dangerous Industrial Work and Child Labor</h3>
<p><strong>What does this source show about the nature of industrial work?</strong> It shows that industrial labor was highly unregulated, physically grueling, dirty, and dangerous. Workplaces lacked basic safety equipment, forcing workers to use their bare hands on rough materials in dark, hazardous environments.</p>
<p><strong>Who was primarily hurt and how?</strong> Young children were primarily hurt. The physical costs included stunted growth, lung diseases from coal dust, and injuries to their hands. Developmentally, they were robbed of an education and a normal childhood.</p>

<h3>Station 2: Tenement Life in Crowded Cities</h3>
<p><strong>What does this description reveal about housing conditions?</strong> It reveals that urban housing was severely overcrowded, unsanitary, and lacking basic infrastructure like light and ventilation. Landlords prioritized packing in as many tenants as possible over basic living standards.</p>
<p><strong>Who suffered the most and how?</strong> The urban poor, particularly immigrants and children, suffered the most. The lack of sanitation and fresh air caused rampant spread of diseases, while the physical environment offered no safe spaces for daily life or play.</p>

<h3>Station 3: Corrupt Political Machines</h3>
<p><strong>What does this source demonstrate about political machines?</strong> It demonstrates that political bosses used insider knowledge and public tax money to enrich themselves. They viewed public office as a business opportunity for personal profit rather than a public service.</p>
<p><strong>Who was ultimately cheated and how?</strong> The taxpayers and regular citizens were cheated. It damaged democracy by ensuring that city planning and public funds served the interests of corrupt politicians and their loyal insiders rather than the actual needs of the community.</p>

<h3>Station 4: The Power of Trusts</h3>
<p><strong>What does this summary reveal about business tactics?</strong> It reveals that monopolies used unethical and illegal alliances with other industries (like railroads) to crush competition. They relied on predatory pricing to bankrupt rivals rather than competing fairly.</p>
<p><strong>Who was financially hurt and how?</strong> Small business owners and independent refiners were financially ruined. Ultimately, consumers were also hurt because once the trust secured a monopoly, they could artificially inflate prices, harming the broader free market economy.</p>

<h3>Part 2: Your Verdict (Grading Rubric)</h3>
<p>Student paragraphs will vary based on their ranking. Full credit should be awarded if the student:</p>
<ul>
<li>Clearly states their number one choice.</li>
<li>Accurately cites evidence from the station corresponding to their top choice (for example, mentioning the coal dust or bare hands from Station 1).</li>
<li>Accurately cites evidence from a second station to serve as a point of comparison (for example, arguing that child labor was a more immediate matter of life and death than the financial graft of political bosses in Station 3).</li>
</ul>
<p class="credit">Created by Crossroads History Studio</p>
</div>

</body></html>"""

html_path = BASE + "/lesson-01-activity.html"
with open(html_path, "w") as f:
    f.write(html)
print("html written:", round(os.path.getsize(html_path) / 1024), "KB")

chrome = os.path.expanduser("~/.cache/ms-playwright/chromium-1243/chrome-linux64/chrome")
pdf_path = BASE + "/lesson-01-activity.pdf"
r = subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", "--print-to-pdf=" + pdf_path,
                    "file://" + html_path], capture_output=True, text=True, timeout=120)
print("chrome exit:", r.returncode, r.stderr[-200:] if r.stderr else "")
print("pdf exists:", os.path.exists(pdf_path))
