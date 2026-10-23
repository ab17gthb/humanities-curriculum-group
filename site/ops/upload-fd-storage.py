#!/usr/bin/env python3
"""Upload the The Founding unit files to Firebase Storage
under the flat prefix hcg/the-founding/ and verify count, total bytes,
and per-object MD5 against the local files.

Pattern follows the Gilded Age upload recorded in entitlement-status.md.
Run with the fs venv python and the deployer key:
  GOOGLE_APPLICATION_CREDENTIALS=~/workspace/system/secrets/rycal-deployer-key.json \
  ~/workspace/.venvs/fs/bin/python ops/upload-ca-storage.py
"""
import base64
import hashlib
import os
import sys

from google.cloud import storage

BUCKET = "cue-bb34b.firebasestorage.app"
PREFIX = "hcg/the-founding/"
BASE = os.path.expanduser("~/workspace/curriculum-planner/the-founding")

PPTX_MIME = (
    "application/vnd.openxmlformats-officedocument."
    "presentationml.presentation"
)


def local_files():
    files = []
    for n in range(1, 9):
        d = os.path.join(BASE, "lesson-%02d" % n)
        for kind in ("reading", "guided-notes", "activity", "notebook",
                     "quick-check", "writing", "teacher-notes"):
            name = "lesson-%02d-%s.pdf" % (n, kind)
            files.append((os.path.join(d, name), name, "application/pdf"))
        name = "lesson-%02d-slides.pptx" % n
        files.append((os.path.join(d, name), name, PPTX_MIME))
    files.append((os.path.join(BASE, "review", "review-study-guide.pdf"),
                  "review-study-guide.pdf", "application/pdf"))
    files.append((os.path.join(BASE, "review", "review-crossword.pdf"),
                  "review-crossword.pdf", "application/pdf"))
    files.append((os.path.join(BASE, "unit-test", "unit-test.pdf"),
                  "unit-test.pdf", "application/pdf"))
    return files


def md5_hex(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    files = local_files()
    assert len(files) == 67, len(files)
    for path, _name, _mime in files:
        if not os.path.isfile(path):
            print("MISSING LOCAL:", path)
            sys.exit(1)

    client = storage.Client()
    bucket = client.bucket(BUCKET)

    for path, name, mime in files:
        blob = bucket.blob(PREFIX + name)
        blob.upload_from_filename(path, content_type=mime)
        print("uploaded", PREFIX + name)

    # Verification pass: reload every remote object fresh.
    remote = {b.name: b for b in bucket.list_blobs(prefix=PREFIX)}
    expected = {PREFIX + name: (path, mime) for path, name, mime in files}
    errors = []
    if set(remote) != set(expected):
        errors.append("name set mismatch: remote-only %s local-only %s" % (
            sorted(set(remote) - set(expected)),
            sorted(set(expected) - set(remote))))
    total_remote = 0
    total_local = 0
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
        remote_md5 = base64.b64decode(blob.md5_hash).hex()
        if remote_md5 != md5_hex(path):
            errors.append("%s MD5 mismatch" % obj_name)
        if blob.content_type != mime:
            errors.append("%s content_type %r != %r" % (obj_name, blob.content_type, mime))
    print("remote count:", len(remote))
    print("remote total bytes:", total_remote)
    print("local total bytes:", total_local)
    if errors:
        print("VERIFY FAILED:")
        for e in errors:
            print(" -", e)
        sys.exit(1)
    print("VERIFY PASS: count, total bytes, per-object MD5, content types all match.")


if __name__ == "__main__":
    main()
