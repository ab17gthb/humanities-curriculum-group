#!/usr/bin/env python3
"""Upload every stamped catalog PDF to its live destination, MD5-verified.

Destinations:
  - Firebase Storage objects referenced by the site (hcg/<unit>/<file>),
    resolved to disk masters by unit + basename.
  - The free Progressive Era PDFs in site/public/files/ (copied locally;
    they go live on the next hosting deploy).
Run with the fs venv python + deployer credentials. Prints a summary and
writes upload-report.jsonl. Aborts a file (never the run) on MD5 mismatch.
"""
import base64, hashlib, json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.expanduser("~/workspace/curriculum-planner")
SITE_PUBLIC = os.path.join(ROOT, "site", "public")
BUCKET = "cue-bb34b.firebasestorage.app"
REVIEW_UNITS = {"course-review", "early-review", "modern-review"}

def md5_hex(path):
    return hashlib.md5(open(path, "rb").read()).hexdigest()

def disk_index():
    """basename -> [disk paths] for every stamped master, by search unit."""
    mapping = json.load(open(os.path.join(HERE, "mapping.json")))
    idx = {}
    for rel in mapping:
        idx.setdefault(os.path.basename(rel), []).append(rel)
    return idx

def storage_paths():
    pat = re.compile(r"hcg/[a-z0-9\-]+/[a-z0-9\-]+\.pdf")
    found = set()
    for dirpath, _d, files in os.walk(SITE_PUBLIC):
        for f in files:
            if f.endswith((".js", ".html")):
                try:
                    found |= set(pat.findall(open(os.path.join(dirpath, f),
                                                  encoding="utf-8", errors="replace").read()))
                except OSError:
                    pass
    return sorted(found)

def resolve(unit, base, idx):
    cands = idx.get(base, [])
    if unit in REVIEW_UNITS:
        hits = [c for c in cands if c.startswith("course-review/")]
    else:
        hits = [c for c in cands if c.startswith(unit + "/")]
    return hits

def main():
    from google.cloud import storage
    idx = disk_index()
    report = open(os.path.join(HERE, "upload-report.jsonl"), "a")
    counts = {"uploaded": 0, "copied": 0, "failed": 0, "unresolved": 0}
    def log(rec):
        report.write(json.dumps(rec) + "\n"); report.flush()
        if rec["status"] not in ("uploaded", "copied"):
            print("ATTENTION:", json.dumps(rec))

    client = storage.Client()
    bucket = client.bucket(BUCKET)
    for obj in storage_paths():
        _h, unit, base = obj.split("/")
        hits = resolve(unit, base, idx)
        if len(hits) != 1:
            counts["unresolved"] += 1
            log({"obj": obj, "status": "unresolved", "hits": hits})
            continue
        local = os.path.join(ROOT, hits[0])
        blob = bucket.blob(obj)
        blob.upload_from_filename(local, content_type="application/pdf")
        blob.reload()
        ok = base64.b64decode(blob.md5_hash).hex() == md5_hex(local)
        counts["uploaded" if ok else "failed"] += 1
        log({"obj": obj, "src": hits[0], "status": "uploaded" if ok else "MD5-MISMATCH"})

    files_dir = os.path.join(SITE_PUBLIC, "files")
    mapping = json.load(open(os.path.join(HERE, "mapping.json")))
    for f in sorted(os.listdir(files_dir)):
        if not f.endswith(".pdf"):
            continue
        hits = [c for c in idx.get(f, []) if c.startswith("progressive-era/")
                and "/tpt/" not in c]
        if len(hits) != 1:
            print("public file not a stamped master (skipped):", f, hits)
            continue
        dst = os.path.join(files_dir, f)
        shutil.copyfile(os.path.join(ROOT, hits[0]), dst)
        ok = md5_hex(dst) == md5_hex(os.path.join(ROOT, hits[0]))
        counts["copied" if ok else "failed"] += 1
        log({"obj": "site/files/" + f, "src": hits[0],
             "status": "copied" if ok else "MD5-MISMATCH"})
    report.close()
    print("done:", counts)

if __name__ == "__main__":
    main()
