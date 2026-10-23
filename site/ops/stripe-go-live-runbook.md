# Stripe go-live runbook — HCG All-Access

Purpose: take HCG checkout from Stripe TEST mode to live billing in one sitting.
State today (2026-10-22): checkout runs in test mode on the Stripe account
"The Primary Source Project" (acct_1URDiBJil0sQFH0u). HCG product
prod_VTxkV1lPymIZ2r, $9.99/mo price_1USzonJil0sQFH0usCBhekux (test).
The subscribe page carries a plain test-mode note; no real charge is possible.

## Alex's steps (his Stripe login; ~15 minutes)
1. In Stripe, complete account activation for live payments if not already
   done for TPSP (business details, tax ID, bank account for payouts).
2. Flip the account to Live mode and open the HCG product: create the live
   product "Humanities Curriculum Group All-Access" with TWO recurring
   prices: $9.99/month and the annual price: $59/year (Alex, 2026-10-22 — matches TPSP All-Access annual).
   Send Muse both live price IDs (price_...).
3. Add the live webhook endpoint: Developers > Webhooks > Add endpoint,
   URL = the stripeWebhook Cloud Function URL (same URL as the test endpoint;
   Muse confirms it on request), events = checkout.session.completed,
   customer.subscription.updated, customer.subscription.deleted,
   invoice.payment_failed. Send Muse the live signing secret (whsec_...)
   through a secure channel, not chat text if avoidable.
4. Tell Muse "live IDs sent." Everything below is Muse's side.

## Muse's steps (after Alex's IDs arrive)
1. Store the live secret key + webhook secret in Secret Manager (never in
   code, chat, or memory).
2. Point createHcgCheckout at the live price ID; redeploy functions via
   site/ops/deploy-functions.py.
3. Remove the test-mode note from subscribe.html (and the static test
   payment link if the per-user flow has fully replaced it); deploy hosting;
   md5-verify.
4. Verify with a real $9.99 charge on Alex's own card, confirm the webhook
   writes entitlement, confirm downloads unlock, then refund the charge in
   Stripe and cancel the subscription.
5. Update site/ops/entitlement-status.md and the memory log; report to Alex.

5. In Stripe settings, confirm "email customers for successful payments"
   is ON so every buyer is emailed a receipt, and check the invoice/receipt
   public details (business name, support email) — school offices read the
   invoice PDF when reimbursing teachers. Note: receipts brand with the
   account's public name, currently "The Primary Source Project."

## Notes
- KNOWETHCOMP is a TEST-mode promo; recreate it in live mode only if Alex
  wants a live comp code.
- TPSP runs on the same Stripe account; its products/prices are separate and
  untouched by this switch.
