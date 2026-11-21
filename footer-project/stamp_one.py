#!/usr/bin/env python3
"""Stamp ONE freshly built PDF with the HCG footer. Called by
templates/build_pdf.py after every print so rebuilds keep the footer.
Usage: stamp_one.py <document.html> <output.pdf>  (fs venv python)"""
import importlib.util, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))

def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def main():
    html_path, pdf_path = sys.argv[1], sys.argv[2]
    survey, stamp = load("survey"), load("stamp")
    title = survey.title_of(html_path)
    tlabel = survey.type_label(os.path.basename(pdf_path))
    label, _rule = survey.label_for(title, tlabel)
    if label is None:
        print(f"FOOTER NOT APPLIED (no label derivable): {pdf_path}")
        sys.exit(2)
    r = stamp.stamp(pdf_path, label)
    print("footer:", r["status"], "->", label)

if __name__ == "__main__":
    main()
