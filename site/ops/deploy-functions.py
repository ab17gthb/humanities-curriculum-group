#!/usr/bin/env python3
"""Deploy the HCG functions codebase to cue-bb34b via the Cloud Functions v2 REST API.

Why this exists: `firebase deploy` fails in the sandbox because the egress proxy
re-issues the generateUploadUrl POST without a Content-Length header and Google
returns 411. Python's http client sets Content-Length, so the same flow works here.

Usage: deploy-functions.py [functionName ...]   (default: all in SPEC)
Credentials: the deployer key at ~/workspace/system/secrets/rycal-deployer-key.json.
"""
import io, json, os, sys, time, zipfile
import urllib.request, urllib.error
import google.auth.transport.requests
from google.oauth2 import service_account

PROJECT = "cue-bb34b"
PROJECT_NUMBER = "552988749111"
LOCATION = "us-central1"
CODEBASE = "hcg"
SRC = os.path.expanduser("~/workspace/curriculum-planner/site/functions")
SA_EMAIL = f"{PROJECT_NUMBER}-compute@developer.gserviceaccount.com"

# name -> dict(entryPoint, secrets=[secret names mounted as env vars of same name], memory, timeout)
SPEC = {
    "hcgPing":           {"entryPoint": "hcgPing", "secrets": [], "memory": "256Mi", "timeout": 60},
    "createHcgCheckout": {"entryPoint": "createHcgCheckout", "secrets": ["HCG_STRIPE_SECRET_KEY"], "memory": "256Mi", "timeout": 60},
    "stripeWebhook":     {"entryPoint": "stripeWebhook", "secrets": ["HCG_STRIPE_SECRET_KEY", "HCG_STRIPE_WEBHOOK_SECRET"], "memory": "256Mi", "timeout": 60},
    "logEvent":          {"entryPoint": "logEvent", "secrets": [], "memory": "256Mi", "timeout": 60},
    "hcgStatsSummary":   {"entryPoint": "hcgStatsSummary", "secrets": [], "memory": "256Mi", "timeout": 60},
}

creds = service_account.Credentials.from_service_account_file(
    os.path.expanduser("~/workspace/system/secrets/rycal-deployer-key.json"),
    scopes=["https://www.googleapis.com/auth/cloud-platform"])
creds.refresh(google.auth.transport.requests.Request())

def call(method, url, body=None, headers_extra=None, raw=False):
    data = None
    headers = {"Authorization": f"Bearer {creds.token}"}
    if body is not None:
        data = body if isinstance(body, bytes) else json.dumps(body).encode()
        headers["Content-Type"] = "application/json"
    if headers_extra: headers.update(headers_extra)
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            b = r.read()
            return r.status, (b if raw else json.loads(b or b"{}"))
    except urllib.error.HTTPError as e:
        b = e.read()
        try: detail = json.loads(b or b"{}")
        except Exception: detail = {"raw": b[:300].decode("utf-8", "replace")}
        return e.code, detail

def poll_op(op_name, timeout_s=900):
    url = f"https://cloudfunctions.googleapis.com/v2/{op_name}"
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        st, d = call("GET", url)
        if d.get("done"):
            if "error" in d: raise RuntimeError(f"operation failed: {json.dumps(d['error'])[:500]}")
            return d
        time.sleep(10)
    raise RuntimeError("operation timed out: " + op_name)

def make_zip():
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for f in ("index.js", "package.json", "package-lock.json"):
            p = os.path.join(SRC, f)
            if os.path.exists(p): z.write(p, f)
    return buf.getvalue()

def main():
    names = sys.argv[1:] or list(SPEC)
    zip_bytes = make_zip()
    st, d = call("POST", f"https://cloudfunctions.googleapis.com/v2/projects/{PROJECT}/locations/{LOCATION}/functions:generateUploadUrl", {})
    if st != 200: raise SystemExit(f"generateUploadUrl failed {st}: {json.dumps(d)[:300]}")
    upload_url, ss = d["uploadUrl"], d["storageSource"]
    req = urllib.request.Request(upload_url, data=zip_bytes, method="PUT",
                                 headers={"Content-Type": "application/zip"})
    with urllib.request.urlopen(req, timeout=300) as r:
        print(f"zip uploaded: HTTP {r.status}, {len(zip_bytes)} bytes")

    for name in names:
        spec = SPEC[name]
        fn_name = f"projects/{PROJECT}/locations/{LOCATION}/functions/{name}"
        secret_env = [{"key": s, "projectId": PROJECT_NUMBER, "secret": s, "version": "latest"}
                      for s in spec["secrets"]]
        fn = {
            "name": fn_name,
            "buildConfig": {
                "runtime": "nodejs22", "entryPoint": spec["entryPoint"],
                "source": {"storageSource": ss},
            },
            "serviceConfig": {
                "serviceAccountEmail": SA_EMAIL, "availableMemory": spec["memory"],
                "timeoutSeconds": spec["timeout"], "ingressSettings": "ALLOW_ALL",
                "secretEnvironmentVariables": secret_env,
            },
            "labels": {"firebase-functions-codebase": CODEBASE, "deployment-tool": "api-deploy-script"},
        }
        st, existing = call("GET", f"https://cloudfunctions.googleapis.com/v2/{fn_name}")
        if st == 404:
            st, op = call("POST", f"https://cloudfunctions.googleapis.com/v2/projects/{PROJECT}/locations/{LOCATION}/functions?functionId={name}", fn)
            action = "create"
        else:
            st, op = call("PATCH", f"https://cloudfunctions.googleapis.com/v2/{fn_name}?updateMask=buildConfig,serviceConfig,labels", fn)
            action = "update"
        if st not in (200, 201) or "name" not in op:
            raise SystemExit(f"{action} {name} failed {st}: {json.dumps(op)[:400]}")
        poll_op(op["name"])
        print(f"{name}: {action} complete")
        # Public invoker (gen2 https + callable functions need this at the platform level)
        st, pol = call("POST", f"https://cloudfunctions.googleapis.com/v2/{fn_name}:setIamPolicy",
                       {"policy": {"bindings": [{"role": "roles/cloudfunctions.invoker", "members": ["allUsers"]}]}})
        print(f"{name}: functions setIamPolicy -> {st}")
        svc = f"projects/{PROJECT}/locations/{LOCATION}/services/{name.lower()}"
        st, pol = call("POST", f"https://run.googleapis.com/v2/{svc}:setIamPolicy",
                       {"policy": {"bindings": [{"role": "roles/run.invoker", "members": ["allUsers"]}]}})
        print(f"{name}: run setIamPolicy -> {st}")
        print(f"{name}: URL https://{LOCATION}-{PROJECT}.cloudfunctions.net/{name}")

if __name__ == "__main__":
    main()
