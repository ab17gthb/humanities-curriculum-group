#!/usr/bin/env python3
"""Upload the three Course Review variants' files to Firebase Storage
under hcg/course-review/, hcg/early-review/, and hcg/modern-review/, and
verify count, total bytes, and per-object MD5 against the local files.
Band PDFs are shared documents uploaded under each variant that includes
the band. Pattern follows ops/upload-ma-storage.py.

Run with the fs venv python and the deployer key:
  GOOGLE_APPLICATION_CREDENTIALS=~/workspace/system/secrets/rycal-deployer-key.json \
  ~/workspace/.venvs/fs/bin/python ops/upload-review-storage.py
"""
import base64
import hashlib
import os
import sys

from google.cloud import storage

BUCKET = "cue-bb34b.firebasestorage.app"
BASE = os.path.expanduser("~/workspace/curriculum-planner/course-review")
PDF = "application/pdf"

VARIANTS = {
    "hcg/course-review/": ([1, 2, 3, 4, 5, 6, 7, 8], "combined"),
    "hcg/early-review/": ([1, 2, 3], "early"),
    "hcg/modern-review/": ([4, 5, 6, 7, 8], "modern"),
}
BAND_KINDS = [("review-packet", "packet"), ("term-sprint", "sprint"),
              ("practice-set", "practice"), ("skills-task", "skills"),
              ("teacher-guide", "teacher-guide")]


def plan():
    """(prefix, [(local_path, remote_name, mime)]) per variant."""
    out = {}
    for prefix, (bands, vkey) in VARIANTS.items():
        files = []
        for b in bands:
            for local_kind, remote_kind in BAND_KINDS:
                files.append((os.path.join(BASE, f"band-{b}", f"day-{b}-{local_kind}.pdf"),
                              f"band-{b}-{remote_kind}.pdf", PDF))
        files.append((os.path.join(BASE, f"study-guide-{vkey}", f"{vkey}-study-guide.pdf"),
                      "study-guide.pdf", PDF))
        files.append((os.path.join(BASE, f"crossword-{vkey}", f"{vkey}-crossword.pdf"),
                      "crossword.pdf", PDF))
        files.append((os.path.join(BASE, f"practice-test-{vkey}", f"{vkey}-practice-test.pdf"),
                      "practice-test.pdf", PDF))
        out[prefix] = files
    return out


def md5_hex(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    jobs = plan()
    counts = {p: len(f) for p, f in jobs.items()}
    print("planned uploads:", counts)
    assert counts == {"hcg/course-review/": 43, "hcg/early-review/": 18,
                      "hcg/modern-review/": 28}, counts
    for files in jobs.values():
        for path, _n, _m in files:
            if not os.path.isfile(path):
                print("MISSING LOCAL:", path)
                sys.exit(1)

    client = storage.Client()
    bucket = client.bucket(BUCKET)

    for prefix, files in jobs.items():
        for path, name, mime in files:
            blob = bucket.blob(prefix + name)
            blob.upload_from_filename(path, content_type=mime)
            print("uploaded", prefix + name)

    errors = []
    for prefix, files in jobs.items():
        remote = {b.name: b for b in bucket.list_blobs(prefix=prefix)}
        expected = {prefix + name: (path, mime) for path, name, mime in files}
        if set(remote) != set(expected):
            errors.append("%s name set mismatch: remote-only %s local-only %s" % (
                prefix, sorted(set(remote) - set(expected)),
                sorted(set(expected) - set(remote))))
        total_remote = total_local = 0
        for obj_name, (path, mime) in expected.items():
            blob = remote.get(obj_name)
            if blob is None:
                continue
            blob.reload()
            local_size = os.path.getsize(path)
            total_local += local_size
            total_remote += blob.size
            if blob.size != local_size:
                errors.append("%s size %d != local %d" % (obj_name, blob.size, local_size))
            if base64.b64decode(blob.md5_hash).hex() != md5_hex(path):
                errors.append("%s MD5 mismatch" % obj_name)
            if blob.content_type != mime:
                errors.append("%s content_type %r != %r" % (obj_name, blob.content_type, mime))
        print(prefix, "remote count:", len(remote),
              "| bytes remote/local:", total_remote, total_local)
    if errors:
        print("VERIFY FAILED:")
        for e in errors:
            print(" -", e)
        sys.exit(1)
    print("VERIFY PASS: all three prefixes match on count, bytes, MD5, content type.")


if __name__ == "__main__":
    main()
