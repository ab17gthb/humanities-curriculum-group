#!/usr/bin/env python3
"""Upload ONE file to Firebase Storage and verify its MD5.
Usage: upload-one.py <local-path> <object-name> [content-type]
Run with the fs venv python and the deployer key."""
import base64, hashlib, os, sys
from google.cloud import storage

path, obj = sys.argv[1], sys.argv[2]
mime = sys.argv[3] if len(sys.argv) > 3 else "application/pdf"
client = storage.Client()
bucket = client.bucket("cue-bb34b.firebasestorage.app")
blob = bucket.blob(obj)
blob.upload_from_filename(path, content_type=mime)
blob.reload()
local = hashlib.md5(open(path, "rb").read()).hexdigest()
remote = base64.b64decode(blob.md5_hash).hex()
print("uploaded", obj, "| md5 match:", local == remote)
assert local == remote
