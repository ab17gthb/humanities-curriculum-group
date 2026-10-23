# HCG entitlement and delivery: status (built 2026-10-21)

## What is live and verified (Stripe TEST mode)

- Functions (codebase "hcg", us-central1), deployed via ops/deploy-functions.py
  (the firebase CLI deploy fails in the sandbox: the egress proxy strips the
  Content-Length on the generateUploadUrl POST and Google returns 411; the
  Python script performs the same flow with a Content-Length set):
  - hcgPing: https://us-central1-cue-bb34b.cloudfunctions.net/hcgPing
  - createHcgCheckout (callable): auth required (verified 401 anonymous);
    creates a subscription Checkout Session for
    price_1USzonJil0sQFH0usCBhekux with client_reference_id = uid and
    metadata {uid, product: "hcg-all-access"} on session and subscription.
  - stripeWebhook: verifies signatures (verified 400 on bad signature) and is
    the only writer of hcgUsers/{uid}.entitlement
    {allAccess, status, currentPeriodEnd, stripeCustomerId,
    stripeSubscriptionId, updatedAt}. Verified end to end with a signed
    customer.subscription.deleted test event: Firestore write matched the
    shape exactly; the throwaway test doc was deleted after.
- Stripe webhook endpoint we_1UT3xwJil0sQFH0un3eWWsDh (test mode, enabled)
  points at the stripeWebhook URL for checkout.session.completed,
  customer.subscription.updated, customer.subscription.deleted. Its signing
  secret is Secret Manager secret HCG_STRIPE_WEBHOOK_SECRET (version 2).
  The Stripe API key the functions use is the project's existing
  STRIPE_SECRET_KEY secret (shared with TPSP; the Stripe API has no
  create-key operation, so no separate restricted key could be minted
  through the connector).
- Site wiring deployed: auth.js exposes HCGAuth.entitlement() on the real
  webhook shape, HCGAuth.startCheckout(), and HCGFiles.url(path) (Storage
  download URLs for entitled users). gilded-era.html carries data-file on all
  51 plate items and shows download controls (51 documents + 8 decks + 8
  teacher notes) only when entitled. subscribe.html uses the function
  checkout when signed in and keeps the payment link as the signed-out
  fallback; copy now states activation is automatic for signed-in checkout.
  subscribe-success.html polls the entitlement for ~30 seconds and reports
  the actual state. 14/14 local Playwright checks passed; live files
  verified byte-for-byte after deploy.

## Firebase Storage: provisioned and uploaded (2026-10-21, second session)

Alex granted the deployer roles/storage.admin on top of
firebasestorage.admin and storage.objectAdmin. After a short propagation
wait (first create attempt 403, second succeeded):

- Default bucket CREATED: cue-bb34b.firebasestorage.app, US-CENTRAL1,
  STANDARD — matches the storageBucket in firebase-config.js.
- Storage rules DEPLOYED from site/storage.rules via
  `firebase deploy --only storage`. Verified active: release
  projects/cue-bb34b/releases/firebase.storage/cue-bb34b.firebasestorage.app
  points at ruleset a883bfbb-e006-4a0f-837a-9c3502e70f55 whose source
  matches site/storage.rules byte for byte (createTime
  2026-10-21T18:57:12Z).
- All 67 Gilded Age files UPLOADED to the flat prefix hcg/gilded-age/
  (59 PDFs as application/pdf, 8 PPTX decks as the presentationml MIME
  type): remote object count 67, remote total 37,522,907 bytes equal to
  the local total, and every object's MD5 matches its local file.

## Entitled reads: RESOLVED (cross-service IAM grant landed 2026-10-21)

Access verification through the Firebase Storage REST API
(object hcg/gilded-age/unit-test.pdf), script saved at
ops/verify-storage-access.py:

- (a) Anonymous GET: HTTP 403 {"code": 403, "message": "Permission denied."}
  — PASS, denied as required.
- (c) Signed-in user with an hcgUsers doc but NO entitlement: HTTP 403 —
  PASS, denied as required.
- (b) Signed-in user whose hcgUsers doc carries the webhook-shaped
  entitlement {allAccess: true, status: "active", ...}: initially
  HTTP 403 — FAIL. The denial came from the rules engine: storage.rules
  calls firestore.get(), and cross-service rules need an IAM role the
  project did not have:
    member: serviceAccount:service-552988749111@gcp-sa-firebasestorage.iam.gserviceaccount.com
    role:   "Firebase Rules Firestore Service Agent"
            (roles/firebaserules.firestoreServiceAgent)

  Alex granted that role on 2026-10-21. After it propagated,
  ops/verify-storage-access.py passed all three checks: (a) anonymous
  403, (b) entitled HTTP 200 with bytes equal to the local file,
  (c) signed-in non-entitled 403. All three were re-verified again on
  2026-10-21 under the current admin ruleset (see below).

## Owner admin access (added 2026-10-21)

Alex's own accounts bypass the paywall. Admin emails (the same list in
both places): alexbrouhard1@gmail.com, alexbrouhardedu@gmail.com,
knowethcg@gmail.com.

- auth.js: a top-level ADMIN_EMAILS list; HCGEntitlement.current() and
  normalizeEntitlement() report {paid: true, allAccess: true,
  status: "active", source: "admin"} for a signed-in admin regardless
  of the Firestore entitlement field, so every page gate treats the
  owner as subscribed. (Patch md5s: auth.js 2b94dad54af427506fd1e033101594d2
  before, 9181782420c6d2260ef53c16fb4daea4 after; PLAN_KEYS unchanged.)
- storage.rules: an admin() function allows reads when the ID token's
  email claim is one of the three addresses, in addition to the
  existing entitled() Firestore check. Deployed via
  `firebase deploy --only storage`; active ruleset
  1371883c-7d21-470b-9b20-4f7f0b08d2d1 (source verified byte-identical
  to site/storage.rules through the Rules API). Client writes remain
  denied everywhere.
- Firestore belt and braces: checked 2026-10-21 — the hcgUsers
  collection held no documents at all, so none of the three accounts
  had a doc to grant. None was needed: the email paths above carry
  admin access on their own. If an admin doc appears later and a doc
  grant is ever wanted, merge entitlement {allAccess: true,
  status: "active", source: "admin", updatedAt: server time} into it.
- Verified for real (object hcg/gilded-age/unit-test.pdf):
  - anonymous GET: HTTP 403 — denied as required.
  - signed-in non-entitled throwaway: HTTP 403 — denied as required.
  - entitled throwaway (Firestore path): HTTP 200, byte-equal.
  - Alex's real uid for alexbrouhardedu@gmail.com (uid confirmed by
    accounts:lookup on a minted custom token): HTTP 200, 296,731
    bytes, byte-equal to the local file — with NO hcgUsers doc for
    that uid, so the read was allowed by the admin email path alone.
  Throwaway test users and docs were deleted after each check.

## Promo codes and comps (added 2026-10-21, Stripe TEST mode)

Two ways to let select individuals around the paywall:

1. Promotion code (self-serve): createHcgCheckout now sets
   allow_promotion_codes: true, so the hosted checkout shows a promo
   code field (function redeployed via ops/deploy-functions.py;
   anonymous calls still return 401 UNAUTHENTICATED).
   - Coupon: id "knoweth-comp-100", percent_off 100, duration
     "forever", valid (created via the Stripe connector and read back).
   - Promotion code: id promo_1UT8HHJil0sQFH0uJnqt5q8K, code
     KNOWETHCOMP, active, bound to that coupon (read back after
     creation). Anyone who enters KNOWETHCOMP at checkout subscribes
     at $0; the webhook then writes their entitlement as usual.
2. Direct comp (no checkout): the person signs in once on the site,
   which creates their hcgUsers/{uid} doc (it appears on first sync;
   if the script below finds no doc, have them sign in, open the
   planner, and save a plan, then run it again). Then run:
       ~/workspace/.venvs/fs/bin/python ops/grant-comp.py <email>
   The script finds the doc by its email field and merges in
   entitlement {allAccess: true, status: "active", source: "comp",
   updatedAt: server time}, leaving plans untouched. Access works
   immediately: the site reads the entitlement from the doc and
   Storage honors it through the existing entitled check. The script
   prints only the uid and result, and refuses cleanly when no doc
   exists (or when more than one doc matches the email). It is the
   one deliberate exception to the webhook-only entitlement writer
   rule, admin credentials only, and it has not been run on anyone.

## Still unverified / owner-only

- A real browser checkout with the Stripe test card (4242…) through the
  signed-in flow: all server pieces are verified individually (checkout
  session creation code path is the same shape as TPSP's live one;
  webhook fulfillment verified with a signed event), but the full
  click-to-entitlement loop needs one human-run browser pass.
- Stripe live mode, when Alex is ready: needs the live API key in
  STRIPE_SECRET_KEY (careful: shared with TPSP), a live webhook endpoint
  + HCG_STRIPE_WEBHOOK_SECRET rotation, and the live price ID in
  functions/index.js (PRICE_MONTHLY) plus the live payment link in
  firebase-config.js.
- The firestore-stripe-payments extension was NOT needed: custom functions
  cover checkout + webhook, and the extension would not have solved the
  storage provisioning block anyway (it manages Firestore data only).

## End-to-end checkout verification (2026-10-22 evening)
The full customer chain was run in a real browser for the first time:
throwaway non-entitled account -> createHcgCheckout minted a session ->
Stripe hosted page showed "Subscribe to Humanities Curriculum Group
All-Access", $9.99/month, merchant "The Primary Source Project" ->
test card 4242 paid -> redirect to /subscribe-success ("Checkout
finished", "All-Access is active on your account") -> webhook wrote
hcgUsers/{uid}.entitlement {allAccess: true, status: "active",
stripeCustomerId cus_VUTaX2gPz5qkDu, stripeSubscriptionId
sub_1UTUdBJil0sQFH0uKgJOhxt0} within seconds. The test Auth user and its
Firestore doc were deleted afterward. RESIDUE: the TEST-mode subscription
sub_1UTUdBJil0sQFH0uKgJOhxt0 is still "active" in Stripe's sandbox (the
connector exposes no cancel tool and Secret Manager access from the
sandbox stalled); it bills only a test card. Cancel it in one click from
the Stripe dashboard in test mode (Subscriptions) whenever convenient.
Notes: admin accounts cannot start checkout (the subscribe page shows
"All-Access is active" with the button disabled) — intended behavior.
Also observed: hcgUsers stays empty until a signed-in user first syncs a
plan; the doc is created by plan sync, not by sign-in alone.

## Annual price created (test mode, 2026-10-22)
Alex set the annual All-Access price at $59/year (matches TPSP All-Access).
Test price created on product prod_VTxkV1lPymIZ2r:
price_1UTYsrJil0sQFH0uHCWxewqk ($59.00, recurring year, active, livemode
false). Remaining build: createHcgCheckout learns an interval argument,
subscribe.html presents both plans, annual checkout verified end to end
like the monthly was. At go-live, create the matching live $59 price.

## Annual option LIVE (2026-10-22 night)
createHcgCheckout accepts {interval: "year"} and selects the $59 annual
test price; subscribe.html presents Monthly $9.99 and Annual $59 with the
single-receipt framing; the annual option hides for entitled accounts.
Functions redeployed (createHcgCheckout only); hosting deployed and
md5-verified. Annual end-to-end proof: throwaway user and session created
(session cs_test_b1Vz..., verified server-side as the annual price);
CORRECTION (2026-10-23 ~3:00am ET): the first payment browser run
errored without completing. A direct Stripe read of the session showed
status open / payment_status unpaid, no subscription, no customer — no
charge ever happened. A second payment run on the same still-open session
was started ~3:00am ET; entitlement confirmation and throwaway cleanup
follow its result.

## Annual proof: closed by Alex's decline (2026-10-23)
Alex declined the payment approval on 2026-10-23 (~6:52am ET) after
asking what the prompt was. That ends the annual end-to-end proof: the
Subscribe click never happened and nothing was charged. What stands
proven: the function mints a correct $59 annual session server-side, and
the entitlement webhook is the same handler the completed monthly
payment already proved. The one unrun hop is an annual payment itself.
Residue: the throwaway Auth user hcg-annual-test@example.com still
exists (no Firestore doc, no entitlement); the sandbox cleanup route
returned 403 and the state file was shredded, so removal is a one-click
console delete whenever convenient. The unpaid test session expires on
its own.

## Annual proof COMPLETED (2026-10-23 ~6:55am ET, supersedes the decline note above)
Alex reconsidered, approved the payment, and the same session completed:
Subscribe clicked once, landed on /subscribe-success reading "All-Access
is active on your account." The webhook wrote the entitlement within
seconds: hcgUsers/GnVz7hdEVbPW3DGZSpnKRtNUjor1 {allAccess: true,
status: "active", stripeSubscriptionId sub_1UTg7wJil0sQFH0uD5m0aanE}.
Stripe confirms that subscription is active on price
price_1UTYsrJil0sQFH0uHCWxewqk (5900, interval year). Annual billing is
proven end to end. Cleanup: the throwaway Firestore doc is deleted. The
throwaway Auth user still exists (deployer account lacks Auth delete
permission; console one-click whenever). The test subscription
sub_1UTg7wJil0sQFH0uD5m0aanE remains active in the Stripe sandbox,
bills only the test card; cancel from the test dashboard alongside
sub_1UTUdBJil0sQFH0uKgJOhxt0 whenever convenient.
