#!/usr/bin/env python3
"""Grant a complimentary All-Access entitlement to one HCG account by email.

Usage: grant-comp.py <email>
Credentials: ~/workspace/system/secrets/rycal-deployer-key.json
Run with: ~/workspace/.venvs/fs/bin/python ops/grant-comp.py <email>

How a comp works:
  1. The person signs in once on the site, which creates their
     hcgUsers/{uid} doc (the doc appears once the account first syncs;
     if this script says no doc exists, have them sign in, open the
     planner, and save a plan, then run it again).
  2. This script finds the doc by its email field and merges in
     entitlement {allAccess: true, status: "active", source: "comp",
     updatedAt: server time}. Plans and other fields are not touched.
  3. Access works immediately: the site reads the entitlement from the
     doc, and Firebase Storage honors it through the existing entitled
     check in storage.rules.

Prints only the uid and the result. Never prints secrets. Exits nonzero
with a plain message when no hcgUsers doc exists for the email, or when
more than one doc matches (resolve the duplicate by hand in that case).
"""
import os
import sys

import firebase_admin
from firebase_admin import credentials, firestore

KEY = os.path.expanduser("~/workspace/system/secrets/rycal-deployer-key.json")


def main():
    if len(sys.argv) != 2 or "@" not in sys.argv[1]:
        print("usage: grant-comp.py <email>")
        return 2
    email = sys.argv[1].strip().lower()

    firebase_admin.initialize_app(
        credentials.Certificate(KEY), {"projectId": "cue-bb34b"})
    db = firestore.client()

    docs = list(db.collection("hcgUsers").where("email", "==", email).stream())
    if not docs:
        # Sign-in writes the email as typed by the identity provider; try a
        # case-insensitive scan before giving up.
        docs = [d for d in db.collection("hcgUsers").stream()
                if (d.to_dict() or {}).get("email", "").lower() == email]
    if not docs:
        print(f"no hcgUsers doc found for {email}; "
              "the person must sign in on the site first")
        return 1
    if len(docs) > 1:
        print(f"{len(docs)} hcgUsers docs match {email}; "
              "refusing to guess, resolve the duplicate first")
        return 1

    doc = docs[0]
    doc.reference.set({
        "entitlement": {
            "allAccess": True,
            "status": "active",
            "source": "comp",
            "updatedAt": firestore.SERVER_TIMESTAMP,
        }
    }, merge=True)
    print(f"comp granted: uid {doc.id} ({email})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
