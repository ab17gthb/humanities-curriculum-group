#!/usr/bin/env python3
"""Verify HCG Storage access rules end to end (run after the cross-service
IAM role below is granted).

Checks, through the Firebase Storage REST API, using object
hcg/gilded-age/unit-test.pdf:
  (a) anonymous download must FAIL (403)
  (b) a user whose hcgUsers doc carries the webhook-shaped entitlement
      {allAccess: true, status: "active"} must SUCCEED, byte-equal to the
      local unit-test.pdf
  (c) a signed-in user with no entitlement must FAIL (403)

Throwaway users: the deployer cannot call the Identity Platform Admin API,
so users are not pre-created. Custom tokens are signed locally with the
deployer key; signInWithCustomToken auto-creates the Auth users, and
cleanup deletes each user with its own ID token (accounts:delete) and
deletes the Firestore docs with admin credentials.

PREREQUISITE (owner action, one time): the cross-service rules role must be
granted or firestore.get() inside storage.rules fails and every entitled
read is denied:
  member: serviceAccount:service-552988749111@gcp-sa-firebasestorage.iam.gserviceaccount.com
  role:   roles/firebaserules.firestoreServiceAgent

Credentials: ~/workspace/system/secrets/rycal-deployer-key.json
Run: ~/workspace/.venvs/fs/bin/python ops/verify-storage-access.py
"""
import hashlib, json, os, re
import urllib.request, urllib.error
import firebase_admin
from firebase_admin import credentials, auth, firestore

KEY = os.path.expanduser("~/workspace/system/secrets/rycal-deployer-key.json")
LOCAL = os.path.expanduser("~/workspace/curriculum-planner/gilded-age/unit-test/unit-test.pdf")
OBJ = "hcg/gilded-age/unit-test.pdf"
DL = ("https://firebasestorage.googleapis.com/v0/b/cue-bb34b.firebasestorage.app/o/"
      + OBJ.replace("/", "%2F") + "?alt=media")

cfg = open(os.path.expanduser("~/workspace/curriculum-planner/site/public/firebase-config.js")).read()
API_KEY = re.search(r'apiKey:\s*"([^"]+)"', cfg).group(1)
REFERER = {"Referer": "https://humanitiescurriculumgroup.web.app/"}

def http(method, url, headers=None, body=None):
    data = json.dumps(body).encode() if body is not None else None
    h = dict(headers or {})
    if body is not None: h["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, method=method, headers=h)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()

st, body = http("GET", DL)
print(f"(a) anonymous GET: HTTP {st} -> {'DENIED as expected' if st in (401, 403) else 'UNEXPECTED'}")
print("    body:", body[:160].decode("utf-8", "replace").replace("\n", " "))

firebase_admin.initialize_app(credentials.Certificate(KEY), {"projectId": "cue-bb34b"})
db = firestore.client()
UID_OK, UID_NO = "hcg-verify-entitled", "hcg-verify-notentitled"
tokens = {}

def sign_in(uid):
    custom = auth.create_custom_token(uid).decode()
    st, body = http("POST",
        f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken?key={API_KEY}",
        headers=REFERER, body={"token": custom, "returnSecureToken": True})
    d = json.loads(body)
    assert st == 200, f"signInWithCustomToken({uid}) failed: {st} {body[:200]}"
    tokens[uid] = d["idToken"]

try:
    db.document(f"hcgUsers/{UID_OK}").set({
        "email": "verify-throwaway@example.invalid",
        "entitlement": {
            "allAccess": True,
            "status": "active",
            "currentPeriodEnd": firestore.SERVER_TIMESTAMP,
            "stripeCustomerId": "cus_verify_throwaway",
            "stripeSubscriptionId": "sub_verify_throwaway",
            "updatedAt": firestore.SERVER_TIMESTAMP,
        },
    })
    db.document(f"hcgUsers/{UID_NO}").set({"email": "verify-throwaway2@example.invalid"})
    sign_in(UID_OK)
    st, body = http("GET", DL, headers={"Authorization": f"Firebase {tokens[UID_OK]}"})
    local_bytes = open(LOCAL, "rb").read()
    print(f"(b) entitled GET: HTTP {st}; bytes {len(body)} vs local {len(local_bytes)}; "
          f"BYTE-EQUAL: {st == 200 and body == local_bytes}")
    sign_in(UID_NO)
    st, body = http("GET", DL, headers={"Authorization": f"Firebase {tokens[UID_NO]}"})
    print(f"(c) signed-in non-entitled GET: HTTP {st} -> {'DENIED as expected' if st in (401, 403) else 'UNEXPECTED'}")
finally:
    for uid in (UID_OK, UID_NO):
        if uid in tokens:
            st, _ = http("POST",
                f"https://identitytoolkit.googleapis.com/v1/accounts:delete?key={API_KEY}",
                headers=REFERER, body={"idToken": tokens[uid]})
            print(f"cleanup: accounts:delete {uid}: HTTP {st}")
        db.document(f"hcgUsers/{uid}").delete()
        print(f"cleanup: hcgUsers/{uid} exists after delete: "
              f"{db.document(f'hcgUsers/{uid}').get().exists}")
