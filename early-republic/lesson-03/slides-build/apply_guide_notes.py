#!/usr/bin/env python3
"""Apply the teacher notes guide's content as the deck's speaker notes.

Reads ../lesson-03-teacher-notes-guide.html, flattens each slide section to
labeled plain text (Slide heading / On the slide / cue / Picture / labeled
blocks with bullets), and writes it into the matching slide's notes in the
given PPTX. Run after every deck build so the deck and the printed guide
carry the same notes."""
import re, sys
from html.parser import HTMLParser
from pptx import Presentation

class Guide(HTMLParser):
    def __init__(self):
        super().__init__()
        self.slides = {}; self.cur = None; self.buf = []; self.mode = None
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'h3':
            self.mode = 'h3'; self.buf = []
        elif tag == 'p':
            self.mode = 'p:' + a.get('class', ''); self.buf = []
        elif tag == 'li':
            self.mode = 'li'; self.buf = []
        elif tag == 'br' and self.mode:
            self.buf.append('\n')
    def handle_data(self, d):
        if self.mode: self.buf.append(d)
    def handle_endtag(self, tag):
        if not self.mode: return
        if tag == 'h3' and self.mode == 'h3':
            t = ''.join(self.buf).strip()
            m = re.match(r'Slide (\d+)', t)
            self.cur = int(m.group(1))
            self.slides[self.cur] = [t]
            self.mode = None
        elif tag == 'p' and self.mode.startswith('p:'):
            t = ' '.join(''.join(self.buf).split())
            if t and self.cur: self.slides[self.cur].append(t)
            self.mode = None
        elif tag == 'li' and self.mode == 'li':
            t = ' '.join(''.join(self.buf).split())
            if t and self.cur: self.slides[self.cur].append('\u2022 ' + t)
            self.mode = None

g = Guide()
g.feed(open('../lesson-03-teacher-notes-guide.html').read())
assert len(g.slides) == 25, len(g.slides)
path = sys.argv[1] if len(sys.argv) > 1 else '../lesson-03-slides-v2.pptx'
prs = Presentation(path)
assert len(prs.slides.__iter__.__self__._sldIdLst) == 25
for i, s in enumerate(prs.slides, 1):
    s.notes_slide.notes_text_frame.text = '\n'.join(g.slides[i])
prs.save(path)
print('guide notes applied to', path)
