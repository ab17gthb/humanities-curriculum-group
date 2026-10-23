#!/usr/bin/env python3
"""Generic activity PDF builder (Crossroads History Studio template).

Usage: python3 build_pdf.py path/to/document.html [output.pdf]

Reads the HTML, inlines every local <img src="..."> as a base64 JPEG
(resized to at most 1000px wide), then prints to PDF with headless
Chromium next to the source file. Chromium path: the Playwright build
on this machine; override with CHROME_BIN if it moves.
"""
import base64, io, os, re, subprocess, sys, glob

def chrome_bin():
    if os.environ.get("CHROME_BIN"):
        return os.environ["CHROME_BIN"]
    hits = sorted(glob.glob(os.path.expanduser(
        "~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome")))
    if not hits:
        sys.exit("Chromium not found under ~/.cache/ms-playwright")
    return hits[-1]

def inline_images(html, base_dir):
    from PIL import Image
    def repl(m):
        src = m.group(1)
        if src.startswith(("data:", "http://", "https://")):
            return m.group(0)
        path = os.path.join(base_dir, src)
        if src.lower().endswith(".svg"):
            uri = "data:image/svg+xml;base64," + base64.b64encode(open(path, "rb").read()).decode()
            return m.group(0).replace(src, uri)
        im = Image.open(path).convert("RGB")
        if im.width > 1000:
            im = im.resize((1000, int(im.height * 1000 / im.width)))
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=82)
        uri = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
        return m.group(0).replace(src, uri)
    return re.sub(r'<img[^>]*src="([^"]+)"', lambda m: repl(m), html)

def main():
    src_path = os.path.abspath(sys.argv[1])
    out_path = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else \
        os.path.splitext(src_path)[0] + ".pdf"
    html = open(src_path).read()
    html = inline_images(html, os.path.dirname(src_path))
    tmp = src_path + ".print.html"
    with open(tmp, "w") as f:
        f.write(html)
    try:
        r = subprocess.run([chrome_bin(), "--headless=new", "--disable-gpu",
                            "--no-sandbox", "--no-pdf-header-footer",
                            "--print-to-pdf=" + out_path, "file://" + tmp],
                           capture_output=True, text=True, timeout=180)
        if r.returncode != 0 or not os.path.exists(out_path):
            sys.exit("Chromium print failed: " + (r.stderr or "")[-300:])
    finally:
        os.unlink(tmp)
    print("PDF written:", out_path)

if __name__ == "__main__":
    main()
