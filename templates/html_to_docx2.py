#!/usr/bin/env python3
"""Convert a curriculum template HTML file to DOCX, v2.

Fork of html_to_docx.py aimed at pixel-faithful replication of the
canonical Chrome-printed PDF:

- page margins, sizes, and spacing are read from the file's own CSS
- the wordmark image is embedded (PNG sibling of the SVG master)
- the Name/Date/Period line is laid out with measured tab stops
  (flex space-between emulated with PIL-measured span widths)
- CSS margin collapsing between sibling blocks is emulated by
  subtracting the previous block's bottom spacing (DOCX spacing adds)
- writing-space divs become chunked empty paragraphs (one body line
  each plus an exact-height remainder) so a space can straddle a page
  break the way the CSS block does in Chrome
- figures stay whole: photo paragraph is keep-with-next to its caption

Usage: html_to_docx2.py in.html out.docx
"""
import sys, os, re, base64, hashlib, tempfile
from html.parser import HTMLParser
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn
from PIL import Image

SRC = sys.argv[1]
OUT = sys.argv[2]
BASE = os.path.dirname(os.path.abspath(SRC))
SRC_TEXT = open(SRC, encoding='utf-8').read()

# ---------------------------------------------------------------- CSS model
def css_block(selector):
    m = re.search(re.escape(selector) + r'\s*\{([^}]*)\}', SRC_TEXT)
    return m.group(1) if m else ''

def css_val(block, prop):
    m = re.search(re.escape(prop) + r'\s*:\s*([^;]+)', block)
    return m.group(1).strip() if m else None

def to_pt(v):
    v = v.strip()
    if v.endswith('pt'):
        return float(v[:-2])
    if v.endswith('in'):
        return float(v[:-2]) * 72.0
    if v.endswith('px'):
        return float(v[:-2]) * 0.75
    return float(v)

def margin_trbl(block):
    v = css_val(block, 'margin')
    if v is None:
        parts = [0.0, 0.0, 0.0, 0.0]
        out = list(parts)
        for i, prop in enumerate(('margin-top', 'margin-right',
                                  'margin-bottom', 'margin-left')):
            lv = css_val(block, prop)
            if lv:
                out[i] = to_pt(lv)
        return tuple(out)
    parts = [to_pt(x) for x in v.split()]
    if len(parts) == 1:
        parts = parts * 4
    elif len(parts) == 2:
        parts = [parts[0], parts[1], parts[0], parts[1]]
    elif len(parts) == 3:
        parts = [parts[0], parts[1], parts[2], parts[1]]
    out = list(parts)  # top, right, bottom, left
    for i, prop in enumerate(('margin-top', 'margin-right',
                              'margin-bottom', 'margin-left')):
        lv = css_val(block, prop)
        if lv:
            out[i] = to_pt(lv)
    return tuple(out)

PAGE = css_block('@page')
pm = re.search(r'margin:\s*([^;]+)', PAGE)
_page_m = [to_pt(x) for x in pm.group(1).split()] if pm else [39.6, 54, 50.4]
if len(_page_m) == 3:
    PG_TOP, PG_SIDE, PG_BOT = _page_m
else:
    PG_TOP, PG_SIDE, PG_BOT = _page_m[0], _page_m[1], _page_m[2]

BODY = css_block('body')
BODY_PT = to_pt(css_val(BODY, 'font-size') or '11.5pt')
LINE = float(css_val(BODY, 'line-height') or '1.35')
LINE_PT = BODY_PT * LINE
TEXT_W = 612.0 - 2 * PG_SIDE  # letter width minus side margins, pt

def h_style(tag, default_size):
    b = css_block(tag)
    return {
        'size': to_pt(css_val(b, 'font-size')) if css_val(b, 'font-size') else default_size,
        'margin': margin_trbl(b),
        'line': float(css_val(b, 'line-height')) if css_val(b, 'line-height') else LINE,
    }

H1 = h_style('h1', 19.0)
H2 = h_style('h2', 14.5)
H3 = h_style('h3', 12.5)
P_AFTER = margin_trbl(css_block('p'))[2]
FIG = css_block('figure')
FIG_M = margin_trbl(FIG)
FIGIMG = css_block('figure img')
CAP_W = to_pt(css_val(FIGIMG, 'max-width')) / 72.0 if css_val(FIGIMG, 'max-width') else 3.9
CAP_H = to_pt(css_val(FIGIMG, 'max-height')) / 72.0 if css_val(FIGIMG, 'max-height') else 2.3
CAPTION_PT = to_pt(css_val(css_block('figcaption'), 'font-size') or '9pt')
CAPTION_MT = margin_trbl(css_block('figcaption'))[0]
Q_BEFORE = margin_trbl(css_block('.q'))[0]
RANK_AFTER = margin_trbl(css_block('.rank p'))[2]
UL_M = margin_trbl(css_block('ul'))
LI_AFTER = margin_trbl(css_block('li'))[2]
BRAND_W = to_pt(css_val(css_block('.brandmark img'), 'width')) / 72.0 \
    if css_val(css_block('.brandmark img'), 'width') else 1.35
BRAND_AFTER = margin_trbl(css_block('.brandmark'))[2]

AFTER_OVERRIDE = {}
for cls in ('directions', 'source'):
    v = css_val(css_block('.' + cls), 'margin-bottom')
    if v:
        AFTER_OVERRIDE[cls] = to_pt(v)

HEIGHTS = {}
for m in re.finditer(r'\.([a-zA-Z0-9\-]+)\s*\{[^}]*?height:\s*([0-9.]+)in', SRC_TEXT):
    HEIGHTS[m.group(1)] = float(m.group(2))

# ---------------------------------------------------------------- document
doc = Document()
for s in doc.sections:
    s.page_width, s.page_height = Inches(8.5), Inches(11)
    s.top_margin = Inches(PG_TOP / 72.0)
    s.bottom_margin = Inches(PG_BOT / 72.0)
    s.left_margin = s.right_margin = Inches(PG_SIDE / 72.0)

style = doc.styles['Normal']
style.font.name = 'Arial'
style.font.size = Pt(BODY_PT)
style.font.color.rgb = RGBColor(0, 0, 0)
style.paragraph_format.line_spacing = LINE
style.paragraph_format.space_after = Pt(P_AFTER)
style.paragraph_format.space_before = Pt(0)
rpr = style.element.get_or_add_rPr()
rf = rpr.find(qn('w:rFonts'))
if rf is None:
    from docx.oxml import OxmlElement
    rf = OxmlElement('w:rFonts')
    rpr.append(rf)
for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'):
    rf.set(qn(a), 'Arial')

# prev_after: bottom spacing (pt) of the previously emitted block, used to
# emulate CSS margin collapsing (DOCX paragraph spacing simply adds).
prev_after = [0.0]
after_space = [False]

def para(size=BODY_PT, before_css=0.0, after=P_AFTER, align=None,
         keep_next=False, line=LINE, page_break_before=False):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(max(0.0, before_css - prev_after[0]))
    pf.space_after = Pt(after)
    if line == 1.0:
        pf.line_spacing = 1.0
    else:
        # CSS line-height multiplies the font size; DOCX "multiple"
        # multiplies the font's natural height (~1.15x) instead, so pin
        # every text line to an exact height in points.
        pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY
        pf.line_spacing = Pt(size * line)
    pf.keep_with_next = keep_next
    pf.page_break_before = page_break_before
    if align is not None:
        p.alignment = align
    prev_after[0] = after
    after_space[0] = False
    return p

def add_run(p, text, size=BODY_PT, bold=False, italic=False):
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.bold, r.italic = bold, italic
    r.font.name = 'Arial'
    return r

def emit_space(height_in):
    """Writing space: chunked empty paragraphs so the block can split
    across a page break like the CSS div does. Exact total height."""
    total = height_in * 72.0
    n = int(total // LINE_PT)
    rem = total - n * LINE_PT
    for _ in range(n):
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.space_before = Pt(0)
        pf.space_after = Pt(0)
        pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY
        pf.line_spacing = Pt(LINE_PT)
        add_run(p, '', size=BODY_PT)
    if rem >= 0.75:
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.space_before = Pt(0)
        pf.space_after = Pt(0)
        pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY
        pf.line_spacing = Pt(rem)
        add_run(p, '', size=2)
    prev_after[0] = 0.0
    after_space[0] = True

# ---------------------------------------------------------------- images
def img_path(srcval):
    if srcval.startswith('data:'):
        h = hashlib.md5(srcval.encode()).hexdigest()[:12]
        ext = 'png' if 'image/png' in srcval[:30] else 'jpg'
        p = os.path.join(tempfile.gettempdir(), f'conv2-img-{h}.{ext}')
        if not os.path.exists(p):
            with open(p, 'wb') as f:
                f.write(base64.b64decode(srcval.split(',', 1)[1]))
        return p
    p = os.path.normpath(os.path.join(BASE, srcval))
    if p.endswith('.svg'):
        png = p[:-4] + '.png'   # raster sibling of the SVG master
        if os.path.exists(png):
            return png
    return p if os.path.exists(p) else None

def display_height_in(path):
    with Image.open(path) as im:
        w, h = im.size
    nat_w, nat_h = w / 96.0, h / 96.0
    scale = min(1.0, CAP_W / nat_w, CAP_H / nat_h)
    return nat_h * scale

# ------------------------------------------------------- nameline measuring
def measure_pt(text, size_pt=BODY_PT, bold=False):
    """Width of text in points using the metric twin of Arial."""
    try:
        from PIL import ImageFont
        import subprocess
        name = 'LiberationSans-Bold.ttf' if bold else 'LiberationSans-Regular.ttf'
        out = subprocess.run(['fc-match', '-f', '%{file}',
                              'Liberation Sans' + (':bold' if bold else '')],
                             capture_output=True, text=True).stdout.strip()
        path = out if out and os.path.exists(out) else \
            '/usr/share/fonts/truetype/liberation/' + name
        f = ImageFont.truetype(path, 1150)  # 100x scale at 11.5pt
        return f.getlength(text) * size_pt / 1150.0
    except Exception:
        return None

# ---------------------------------------------------------------- parser
class Conv(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.cur_p = None
        self.cur_size = BODY_PT
        self.bold = 0
        self.italic = 0
        self.skip = 0
        self.in_key = False
        self.key_h2_done = False
        self.in_nameline = False
        self.nameline_spans = []
        self.span_buf = None
        self.in_figure = False
        self.in_ul = False
        self.last_li = None
        self.li_count = 0

    def classes(self):
        for tag, cls in reversed(self.stack):
            if cls:
                return cls
        return ''

    def in_class(self, name):
        return any(name in cls.split() for _, cls in self.stack)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get('class', '')
        toks = cls.split()
        if tag in ('head', 'style', 'script', 'title'):
            self.skip += 1
            return
        if self.skip:
            return
        self.stack.append((tag, cls))

        if tag == 'p' and 'brandmark' in toks:
            self.cur_p = para(after=BRAND_AFTER, line=1.0)
            self.cur_size = BODY_PT
            self.brandmark_p = self.cur_p
            return
        if tag == 'div' and 'nameline' in toks:
            self.in_nameline = True
            self.nameline_spans = []
            return
        if tag == 'span' and self.in_nameline:
            self.span_buf = []
            return
        if tag == 'div' and 'key' in toks:
            self.in_key = True
            return
        if tag == 'div':
            hit = [t for t in toks if t in HEIGHTS]
            if hit:
                # the previous block's bottom margin is absorbed into the
                # CSS block flow around the space div in Chrome; the white
                # gap measures as space height + next block's top margin.
                if self.cur_p is not None:
                    pass
                last = doc.paragraphs[-1] if doc.paragraphs else None
                if last is not None:
                    last.paragraph_format.space_after = Pt(0)
                emit_space(HEIGHTS[hit[0]])
                return
        if tag == 'h1':
            self.cur_p = para(size=H1['size'], before_css=H1['margin'][0],
                              after=H1['margin'][2], line=H1['line'],
                              keep_next=True)
            self.cur_size = H1['size']
            self.bold += 1
        elif tag == 'h2':
            if self.in_key and not self.key_h2_done:
                self.key_h2_done = True
                self.cur_p = para(size=H2['size'], before_css=0,
                                  after=H2['margin'][2], keep_next=True,
                                  page_break_before=True)
            else:
                self.cur_p = para(size=H2['size'],
                                  before_css=H2['margin'][0],
                                  after=H2['margin'][2], keep_next=True)
            self.cur_size = H2['size']
            self.bold += 1
        elif tag == 'h3':
            self.cur_p = para(size=H3['size'],
                              before_css=H3['margin'][0],
                              after=H3['margin'][2], keep_next=True)
            self.cur_size = H3['size']
            self.bold += 1
        elif tag == 'p':
            after = P_AFTER
            for t in toks:
                if t in AFTER_OVERRIDE:
                    after = AFTER_OVERRIDE[t]
            before = Q_BEFORE if 'q' in toks else 0.0
            if self.in_class('rank'):
                after = RANK_AFTER
            self.cur_p = para(before_css=before, after=after)
            self.cur_size = BODY_PT
        elif tag in ('strong', 'b'):
            self.bold += 1
        elif tag in ('i', 'em'):
            self.italic += 1
        elif tag == 'figure':
            self.in_figure = True
        elif tag == 'img':
            path = img_path(a.get('src', ''))
            if path is None:
                return
            if getattr(self, 'brandmark_p', None) is self.cur_p and self.cur_p is not None:
                run = self.cur_p.add_run()
                run.add_picture(path, width=Inches(BRAND_W))
                self.cur_p = None
                self.brandmark_p = None
                return
            h_in = display_height_in(path)
            p = para(before_css=FIG_M[0], after=0,
                     align=WD_ALIGN_PARAGRAPH.CENTER, keep_next=True, line=1.0)
            run = p.add_run()
            run.add_picture(path, height=Inches(h_in))
            self.cur_p = None
        elif tag == 'figcaption':
            self.cur_p = para(size=CAPTION_PT, before_css=CAPTION_MT,
                              after=FIG_M[2], align=WD_ALIGN_PARAGRAPH.CENTER)
            self.cur_size = CAPTION_PT
            self.italic += 1
        elif tag == 'ul':
            self.in_ul = True
            self.li_count = 0
        elif tag == 'li':
            p = para(before_css=UL_M[0] if self.li_count == 0 else 0.0,
                     after=LI_AFTER)
            pf = p.paragraph_format
            pf.left_indent = Pt(UL_M[3])
            pf.first_line_indent = Pt(-14)
            tabs = pf.tab_stops
            tabs.add_tab_stop(Pt(UL_M[3]))
            add_run(p, '•')
            r = p.add_run()
            r.add_tab()
            self.cur_p = p
            self.cur_size = BODY_PT
            self.last_li = p
            self.li_count += 1
        elif tag == 'br':
            if self.cur_p is not None:
                self.cur_p.add_run().add_break()

    def handle_endtag(self, tag):
        if tag in ('head', 'style', 'script', 'title'):
            self.skip -= 1
            return
        if self.skip:
            return
        if self.stack and self.stack[-1][0] == tag:
            self.stack.pop()
        if tag == 'span' and self.in_nameline and self.span_buf is not None:
            self.nameline_spans.append(''.join(self.span_buf))
            self.span_buf = None
        elif tag == 'div' and self.in_nameline:
            self.in_nameline = False
            self.build_nameline()
        elif tag in ('h1', 'h2', 'h3'):
            self.cur_p = None
            self.cur_size = BODY_PT
            self.bold = max(0, self.bold - 1)
        elif tag == 'p':
            self.cur_p = None
            self.cur_size = BODY_PT
        elif tag in ('strong', 'b'):
            self.bold = max(0, self.bold - 1)
        elif tag in ('i', 'em'):
            self.italic = max(0, self.italic - 1)
        elif tag == 'figure':
            self.in_figure = False
        elif tag == 'figcaption':
            self.cur_p = None
            self.cur_size = BODY_PT
            self.italic = max(0, self.italic - 1)
        elif tag == 'ul':
            self.in_ul = False
            if self.last_li is not None:
                # last item carries the list's bottom margin (collapsed max)
                self.last_li.paragraph_format.space_after = Pt(max(LI_AFTER, UL_M[2]))
                prev_after[0] = max(LI_AFTER, UL_M[2])
                self.last_li = None
        elif tag == 'li':
            self.cur_p = None

    def build_nameline(self):
        spans = [s for s in self.nameline_spans if s]
        p = para(after=P_AFTER)
        widths = [measure_pt(s) for s in spans]
        if len(spans) >= 2 and all(w is not None for w in widths):
            free = TEXT_W - sum(widths)
            gap = free / (len(spans) - 1)
            tabs = p.paragraph_format.tab_stops
            pos = 0.0
            for i in range(1, len(spans)):
                pos += widths[i - 1] + gap
                tabs.add_tab_stop(Pt(pos))
        for i, s in enumerate(spans):
            if i > 0:
                r = p.add_run()
                r.add_tab()
            add_run(p, s)
        self.cur_p = None

    def handle_data(self, data):
        if self.skip:
            return
        if self.span_buf is not None:
            self.span_buf.append(data)
            return
        if self.cur_p is None:
            return
        if data == '' :
            return
        add_run(self.cur_p, data, size=self.cur_size,
                bold=self.bold > 0, italic=self.italic > 0)

# Spacing must ADD (Word semantics). python-docx's template omits
# doNotUseHTMLParagraphAutoSpacing, and without it LibreOffice collapses
# adjacent paragraph spacing to the max (HTML style), which silently
# shrinks every gap. Add the compat flag so all renderers add.
from docx.oxml import OxmlElement as _Ox
_settings = doc.settings.element
_compat = _settings.find(qn('w:compat'))
if _compat is None:
    _compat = _Ox('w:compat')
    _settings.append(_compat)
_compat.append(_Ox('w:doNotUseHTMLParagraphAutoSpacing'))

conv = Conv()
conv.feed(SRC_TEXT)
doc.core_properties.title = 'Reformer\'s Notebook: The Problems Progressives Faced'
doc.save(OUT)
print('saved', OUT)
