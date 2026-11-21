# HCG Stripe LIVE objects (created 2026-10-25 via the custom.hcg-stripe connector)

Account: acct_1URDiBJil0sQFH0u — business name "Humanities Curriculum Group",
charges_enabled true, details_submitted true, statement descriptor
"HUMANITIES CURRICULUM". Payouts: USAA bank account ••••9887 attached
2026-10-25; payouts_enabled was still false at creation time with no
requirements due — expected to flip once Stripe finishes activating the
new account. Recheck before announcing sales.

- Product: prod_VVRA1YXjhrEjTz (Humanities Curriculum Group All-Access)
- Price monthly $9.99: price_1UUQHwJil0sQFH0umlztb3X3
- Price annual $59: price_1UUQHxJil0sQFH0u5MpXmjSj
- Payment link (monthly, signed-out fallback): plink_1UUQI2Jil0sQFH0uYC7OeEIF
  https://buy.stripe.com/9B6cN69KXa7h3iobFScV200
  → redirects to https://humanitiescurriculumgroup.web.app/subscribe-success
- Webhook endpoint: we_1UUQI2Jil0sQFH0uMWi7bR3I
  url https://stripewebhook-yh5summz4a-uc.a.run.app
  events: checkout.session.completed, customer.subscription.updated,
  customer.subscription.deleted. Signing secret stored in Secret Manager
  as HCG_STRIPE_WEBHOOK_SECRET (live version 3, added 2026-10-25). The
  raw creation response file was trashed 2026-10-25 once the secret was
  safely stored (trash id 20261025-123607-1c9e033a81ac45ee9639bc3ae584abae,
  expires 2026-11-24) — never commit it to git.
- Functions use secret HCG_STRIPE_SECRET_KEY (the live secret key), kept
  separate from the shared STRIPE_SECRET_KEY that PSP still uses.

## Proof purchase and cleanup (2026-10-26, complete)

- The 99-cent proof (Alex, sub_1UUn6mJil0sQFH0uxsx65XTE on temp price
  price_1UUSAtJil0sQFH0uWrCHKTB3, temp payment link
  plink_1UUTQdJil0sQFH0uDB996pHu) verified the live checkout and the
  entitlement flip on his account. Cleanup ran the same morning:
  subscription cancelled, 99c charge refunded
  (re_3UUn6kJil0sQFH0u0YI0WaXP), PRICE_MONTHLY in functions/index.js
  restored to price_1UUQHwJil0sQFH0umlztb3X3 and createHcgCheckout
  redeployed, firebase-config monthlyLink restored to the live link
  above, subscribe.html price restored to $9.99, and the temp price and
  temp payment link deactivated. The webhook flipped his hcgUsers
  entitlement to canceled / allAccess false on the cancellation. Known
  cosmetic gap: the entitlement's currentPeriodEnd writes as null (the
  current Stripe API puts period end on the subscription item); status
  handling is unaffected.

Test-mode predecessors (do not reuse): product prod_VTxkV1lPymIZ2r, prices
price_1USzonJil0sQFH0usCBhekux / price_1UTYsrJil0sQFH0uHCWxewqk, payment
link plink_1USzozJil0sQFH0ubyJ3A3XQ.
