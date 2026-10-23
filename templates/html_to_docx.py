#!/usr/bin/env python3
"""Convert one of the curriculum template HTML files to DOCX with the
approved design values applied directly (Arial, black, print sizes,
image caps, blank-paragraph writing space, key on a new page)."""
import sys, re
from html.parser import HTMLParser
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from PIL import Image
import os

SRC = sys.argv[1]
OUT = sys.argv[2]
BASE = os.path.dirname(os.path.abspath(SRC))

doc = Document()
# page setup: Letter, template margins
for s in doc.sections:
    s.page_width, s.page_height = Inches(8.5), Inches(11)
    s.top_margin = s.bottom_margin = Inches(0.7)
    s.left_margin = s.right_margin = Inches(0.75)

style = doc.styles['Normal']
style.font.name = 'Arial'
style.font.size = Pt(11.5)
style.font.color.rgb = RGBColor(0, 0, 0)
style.paragraph_format.line_spacing = 1.35
style.paragraph_format.space_after = Pt(7)
style.paragraph_format.space_before = Pt(0)
rpr = style.element.get_or_add_rPr()
rf = rpr.find(qn('w:rFonts'))
if rf is None:
    rf = OxmlElement('w:rFonts'); rpr.append(rf)
for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'):
    rf.set(qn(a), 'Arial')

def para(size=11.5, bold=False, italic=False, align=None, before=0, after=7,
         keep_next=False, line=1.35):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before, pf.space_after = Pt(before), Pt(after)
    pf.line_spacing = line
    pf.keep_with_next = keep_next
    if align is not None:
        p.alignment = align
    return p

def add_run(p, text, size=11.5, bold=False, italic=False):
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.bold, r.italic = bold, italic
    r.font.name = 'Arial'
    return r

def set_cell_borders(cell, sz=6):
    tcPr = cell._tc.get_or_add_tcPr()
    borders = OxmlElement('w:tcBorders')
    for edge in ('top', 'left', 'bottom', 'right'):
        e = OxmlElement(f'w:{edge}')
        e.set(qn('w:val'), 'single'); e.set(qn('w:sz'), str(sz))
        e.set(qn('w:color'), '000000'); e.set(qn('w:space'), '0')
        borders.append(e)
    tcPr.append(borders)

def set_cell_margins(cell, top=60, bottom=60, left=90, right=90):
    tcPr = cell._tc.get_or_add_tcPr()
    mar = OxmlElement('w:tcMar')
    for tag, val in (('top', top), ('bottom', bottom), ('left', left), ('right', right)):
        e = OxmlElement(f'w:{tag}'); e.set(qn('w:w'), str(val)); e.set(qn('w:type'), 'dxa')
        mar.append(e)
    tcPr.append(mar)

LINE_IN = 11.5 * 1.35 / 72.0  # one blank line of body text, inches

def blank_space(height_in):
    n = max(1, round(height_in / LINE_IN))
    for _ in range(n):
        p = para(after=0)
        add_run(p, '')

class Conv(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []          # (tag, class)
        self.cur_p = None        # current paragraph being filled
        self.cur_size = 11.5
        self.bold = 0
        self.italic = 0
        self.pending_space = None
        self.in_key = False
        self.key_started = False
        self.table = None
        self.row = None
        self.cell_p = None
        self.in_figure = False
        self.skip = 0            # inside head/style/script

    # ---------- helpers
    def classes(self):
        for tag, cls in reversed(self.stack):
            if cls:
                return cls
        return ''

    def flush_space(self):
        if self.pending_space:
            blank_space(self.pending_space)
            self.pending_space = None

    # ---------- parser events
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get('class', '')
        if tag in ('head', 'style', 'script', 'title'):
            self.skip += 1
            return
        if self.skip:
            return
        self.stack.append((tag, cls))
        if tag == 'div' and 'nameline' in cls.split():
            p = para(after=7)
            tabs = p.paragraph_format.tab_stops
            tabs.add_tab_stop(Inches(3.1))
            tabs.add_tab_stop(Inches(5.3))
            self.cur_p = p
            self.in_nameline = True
            self.nameline_parts = 0
            return
        if tag == 'span' and getattr(self, 'in_nameline', False):
            if self.nameline_parts > 0 and self.cur_p is not None:
                self.cur_p.add_run().add_tab()
            self.nameline_parts += 1
            return
        if tag == 'div' and 'key' in cls.split():
            self.in_key = True
        if tag == 'div':
            toks = cls.split()
            hit = [t for t in toks if t in HEIGHTS]
            if hit:
                self.pending_space = HEIGHTS[hit[0]]
                return
        if tag == 'h1':
            self.flush_space()
            self.cur_p = para(size=19, before=12, after=4, line=1.2, keep_next=True)
            self.cur_size = 19
        elif tag == 'h2':
            if self.in_key and not self.key_started:
                self.key_started = True
                self.cur_p = doc.add_paragraph()
                self.cur_p.add_run().add_break(WD_BREAK.PAGE)
                self.cur_p = para(size=14.5, before=0, after=6, keep_next=True)
            else:
                self.cur_p = para(size=14.5, before=16, after=6, keep_next=True)
            self.cur_size = 14.5
        elif tag == 'h3':
            self.cur_p = para(size=12.5, before=14, after=4, keep_next=True)
            self.cur_size = 12.5
        elif tag == 'p':
            if self.table is not None:
                return
            self.flush_space()
            if 'nameline' in self.classes() or 'nameline' in cls:
                self.cur_p = para(after=7)
            elif 'credit' in cls:
                self.cur_p = para(size=9, align=WD_ALIGN_PARAGRAPH.CENTER, before=18, after=0)
                self.cur_size = 9
            elif 'eq' in cls:
                self.cur_p = para(after=10); self.italic += 1
            else:
                self.cur_p = para(after=7)
        elif tag == 'span':
            if self.table is not None:
                pass
        elif tag == 'strong' or tag == 'b':
            self.bold += 1
        elif tag in ('i', 'em'):
            self.italic += 1
        elif tag == 'figure':
            self.in_figure = True
        elif tag == 'img':
            path = self.img_path(a.get('src', ''))
            if path:
                with Image.open(path) as im:
                    w, h = im.size
                # CSS cap: max-width 3.9in, max-height 2.3in (map activity wider)
                maxw, maxh = 3.9, 2.3
                if 'map' in a.get('src', ''):
                    maxw, maxh = 6.6, 3.4
                scale = min(maxw / (w / 96.0), maxh / (h / 96.0), 1.0)
                # images in our assets are ~150-300 dpi; treat px at 150dpi baseline
                disp_w = (w / 150.0)
                disp_h = (h / 150.0)
                scale = min(maxw / disp_w, maxh / disp_h)
                p = para(align=WD_ALIGN_PARAGRAPH.CENTER, before=6, after=2)
                p.add_run().add_picture(path, width=Inches(disp_w * scale))
                self.cur_p = None
        elif tag == 'figcaption':
            self.cur_p = para(size=9, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=8)
            self.cur_size = 9
        elif tag == 'table':
            self.flush_space()
            self.table_data = []
        elif tag == 'tr':
            self.row = []
        elif tag in ('td', 'th'):
            self.cell = {'text': [], 'bold': tag == 'th', 'cls': cls}
            self.row.append(self.cell)
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
        if tag == 'div' and getattr(self, 'in_nameline', False):
            self.in_nameline = False
            self.cur_p = None
        if tag in ('h1', 'h2', 'h3'):
            self.cur_p = None; self.cur_size = 11.5
        elif tag == 'p':
            if 'eq' in self.classes():
                pass
            self.cur_p = None; self.cur_size = 11.5
            if self.italic and 'eq' in (self.stack[-1][1] if self.stack else ''):
                self.italic -= 1
        elif tag in ('strong', 'b'):
            self.bold = max(0, self.bold - 1)
        elif tag in ('i', 'em'):
            self.italic = max(0, self.italic - 1)
        elif tag == 'figure':
            self.in_figure = False
        elif tag == 'figcaption':
            self.cur_p = None; self.cur_size = 11.5
        elif tag == 'tr':
            if hasattr(self, 'table_data') and self.row is not None:
                self.table_data.append(self.row)
            self.row = None
        elif tag == 'table':
            data = self.table_data
            if data:
                ncols = max(len(r) for r in data)
                t = doc.add_table(rows=0, cols=ncols)
                t.alignment = WD_TABLE_ALIGNMENT.CENTER
                for ri, rowdata in enumerate(data):
                    cells = t.add_row().cells
                    for ci, cell in enumerate(rowdata):
                        c = cells[ci]
                        set_cell_borders(c); set_cell_margins(c)
                        p = c.paragraphs[0]
                        p.paragraph_format.line_spacing = 1.3
                        p.paragraph_format.space_after = Pt(2)
                        p.paragraph_format.space_before = Pt(2)
                        txt = ''.join(cell['text']).strip()
                        r = p.add_run(txt)
                        r.font.size = Pt(11)
                        r.font.name = 'Arial'
                        r.bold = cell['bold']
                        if 'row' in cell['cls']:
                            tr = t.rows[ri]._tr
                            trPr = tr.get_or_add_trPr()
                            h = OxmlElement('w:trHeight')
                            h.set(qn('w:val'), '1900'); h.set(qn('w:hRule'), 'atLeast')
                            trPr.append(h)
                doc.add_paragraph().paragraph_format.space_after = Pt(4)
            self.table_data = None

    def handle_data(self, data):
        if self.skip:
            return
        if hasattr(self, 'cell') and self.cell is not None and self.row is not None and self.table_data is not None:
            self.cell['text'].append(data)
            return
        if self.cur_p is None:
            return
        # nameline: the template uses spans; keep text with wide spacing
        if data.strip() == '' and len(data) < 3:
            if data.strip() == '':
                return
        add_run(self.cur_p, data, size=self.cur_size,
                bold=self.bold > 0, italic=self.italic > 0)

src = open(SRC, encoding='utf-8').read()

# Space heights come from the file's own CSS (classes vary by build date:
# .space/.space-lg in early lessons, .sp-a/.sp-b/.sp-c in later ones).
HEIGHTS = {'sp-a': 0.85, 'sp-b': 1.35, 'sp-c': 2.3}
for m in re.finditer(r'\.([a-zA-Z0-9\-]+)\s*\{[^}]*?height:\s*([0-9.]+)in', src):
    HEIGHTS[m.group(1)] = float(m.group(2))

conv = Conv()
# data-URI images: decode once to temp files so python-docx can embed them
import base64, hashlib, tempfile
def _img_path(srcval):
    if srcval.startswith('data:'):
        h = hashlib.md5(srcval.encode()).hexdigest()[:12]
        ext = 'png' if 'image/png' in srcval[:30] else 'jpg'
        p = os.path.join(tempfile.gettempdir(), f'conv-img-{h}.{ext}')
        if not os.path.exists(p):
            with open(p, 'wb') as f:
                f.write(base64.b64decode(srcval.split(',', 1)[1]))
        return p
    p = os.path.join(BASE, srcval)
    return p if os.path.exists(p) else None
Conv.img_path = staticmethod(_img_path)
conv.feed(src)
doc.save(OUT)
print('saved', OUT)
