#!/usr/bin/env python3
"""Re-render every unit/review cover from its HTML master in this folder.

For each cover-<slug>.html (plus cover.html = the Progressive Era sample):
  1. print the HTML to covers/<slug>-cover.pdf via templates/build_pdf.py
  2. rasterize page 1 at 192 dpi to covers/<slug>-cover.png (1632x2112)
  3. copy the PNG to site/public/assets/<slug>-cover.png
The Progressive Era cover PDF is also copied to
site/public/files/progressive-era-cover.pdf (the free downloadable copy).

Run with a python that has PIL (build_pdf.py needs it):
  ~/workspace/.venvs/pptx/bin/python rerender_covers.py
"""
import glob
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BUILD = os.path.join(ROOT, "templates", "build_pdf.py")
ASSETS = os.path.join(ROOT, "site", "public", "assets")
FILES = os.path.join(ROOT, "site", "public", "files")


def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.returncode != 0:
        print("FAILED:", cmd, (r.stderr or "")[-400:])
        sys.exit(1)


def main():
    jobs = []
    for hp in sorted(glob.glob(os.path.join(HERE, "cover-*.html"))):
        slug = os.path.basename(hp)[len("cover-"):-len(".html")]
        jobs.append((hp, slug))
    jobs.append((os.path.join(HERE, "cover.html"), "progressive-era"))
    for hp, slug in jobs:
        pdf = os.path.join(HERE, slug + "-cover.pdf")
        png_base = os.path.join(HERE, slug + "-cover")
        run(f"{sys.executable} {BUILD} {hp} {pdf}")
        run(f"pdftoppm -png -r 192 -singlefile {pdf} {png_base}")
        shutil.copyfile(png_base + ".png", os.path.join(ASSETS, slug + "-cover.png"))
        if slug == "progressive-era":
            shutil.copyfile(pdf, os.path.join(FILES, "progressive-era-cover.pdf"))
        print("rendered:", slug)
    print(f"done: {len(jobs)} covers")


if __name__ == "__main__":
    main()
