#!/usr/bin/env python3
"""Stable-path Secret Manager helper for the HCG site (project cue-bb34b).

Usage:
  secret_tool.py exists SECRET_ID
  secret_tool.py add-version SECRET_ID --value-from-json JSON_FILE KEY
      Reads the string at KEY from JSON_FILE and adds it as a new version of
      SECRET_ID (creating the secret if needed). The value is never printed.
Credentials: the Rycal deployer service account.
"""
import base64
import json
import sys

import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request as AuthRequest

PROJECT = "cue-bb34b"
SA = "/home/hatch/workspace/system/secrets/rycal-deployer-key.json"
SCOPES = ["https://www.googleapis.com/auth/cloud-platform"]
BASE = "https://secretmanager.googleapis.com/v1"


def token():
    creds = service_account.Credentials.from_service_account_file(SA, scopes=SCOPES)
    creds.refresh(AuthRequest())
    return creds.token


def headers():
    return {"Authorization": f"Bearer {token()}", "Content-Type": "application/json"}


def secret_exists(secret_id):
    r = requests.get(f"{BASE}/projects/{PROJECT}/secrets/{secret_id}", headers=headers())
    return r.status_code == 200


def ensure_secret(secret_id):
    if secret_exists(secret_id):
        return
    r = requests.post(
        f"{BASE}/projects/{PROJECT}/secrets?secretId={secret_id}",
        headers=headers(),
        json={"replication": {"automatic": {}}},
    )
    r.raise_for_status()


def add_version(secret_id, value):
    ensure_secret(secret_id)
    payload = base64.b64encode(value.encode()).decode()
    r = requests.post(
        f"{BASE}/projects/{PROJECT}/secrets/{secret_id}:addVersion",
        headers=headers(),
        json={"payload": {"data": payload}},
    )
    r.raise_for_status()
    return r.json().get("name")


def main():
    cmd = sys.argv[1]
    if cmd == "exists":
        print("exists" if secret_exists(sys.argv[2]) else "missing")
    elif cmd == "add-version":
        secret_id = sys.argv[2]
        assert sys.argv[3] == "--value-from-json"
        data = json.load(open(sys.argv[4]))
        value = data[sys.argv[5]]
        name = add_version(secret_id, value)
        print(f"version added: {name}")
    elif cmd == "grant-accessor":
        # grant-accessor SECRET_ID SERVICE_ACCOUNT_EMAIL
        secret_id, email = sys.argv[2], sys.argv[3]
        url = f"{BASE}/projects/552988749111/secrets/{secret_id}"
        # NOTE: in this sandbox :getIamPolicy returns an HTML 404 (proxy
        # quirk) while :setIamPolicy works. The get below is best-effort;
        # on failure we stop rather than blind-overwrite an unknown policy.
        r = requests.post(f"{url}:getIamPolicy", headers=headers(), json={})
        if r.status_code != 200:
            sys.exit(f"getIamPolicy failed ({r.status_code}); refusing blind set")
        policy = r.json()
        member = f"serviceAccount:{email}"
        role = "roles/secretmanager.secretAccessor"
        bindings = policy.get("bindings", [])
        b = next((x for x in bindings if x["role"] == role), None)
        if b is None:
            bindings.append({"role": role, "members": [member]})
        elif member not in b["members"]:
            b["members"].append(member)
        policy["bindings"] = bindings
        r = requests.post(f"{url}:setIamPolicy", headers=headers(), json={"policy": policy})
        r.raise_for_status()
        print(f"accessor granted on {secret_id} to {email}")
    elif cmd == "add-version-stdin":
        # Value arrives on stdin (never in argv, files, or output).
        value = sys.stdin.read().strip()
        if not value:
            sys.exit("empty stdin")
        name = add_version(sys.argv[2], value)
        print(f"version added: {name}")
    else:
        sys.exit(f"unknown command {cmd}")


if __name__ == "__main__":
    main()
