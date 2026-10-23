// Humanities Curriculum Group paywall backend: Stripe Checkout + webhook entitlements.
// Secrets in Secret Manager: STRIPE_SECRET_KEY (shared with the project's other app),
// HCG_STRIPE_WEBHOOK_SECRET (this app's webhook endpoint signing secret).
// The webhook function is the ONLY writer of hcgUsers/{uid}.entitlement;
// Firestore rules forbid clients from creating or changing that field.

const { onCall, onRequest, HttpsError } = require('firebase-functions/v2/https');
const { defineSecret } = require('firebase-functions/params');
const admin = require('firebase-admin');
const { getFirestore, Timestamp, FieldValue } = require('firebase-admin/firestore');
const Stripe = require('stripe');

admin.initializeApp();
const db = getFirestore();

const stripeSecret = defineSecret('STRIPE_SECRET_KEY');
const webhookSecret = defineSecret('HCG_STRIPE_WEBHOOK_SECRET');

const APP_URL = 'https://humanitiescurriculumgroup.web.app';
const PRICE_MONTHLY = 'price_1USzonJil0sQFH0usCBhekux'; // HCG All-Access, $9.99/month, Stripe test mode
const PRICE_ANNUAL = 'price_1UTYsrJil0sQFH0uHCWxewqk'; // HCG All-Access, $59/year, Stripe test mode

exports.hcgPing = onRequest((req, res) => { res.json({ ok: true, app: 'hcg' }); });

// Callable: a signed-in teacher starts the All-Access subscription checkout.
// Returns { url } for the browser to redirect to.
exports.createHcgCheckout = onCall({ secrets: [stripeSecret] }, async (req) => {
  if (!req.auth) throw new HttpsError('unauthenticated', 'Sign in to subscribe');
  const uid = req.auth.uid;
  const stripe = Stripe(stripeSecret.value());
  // Optional interval: "year" selects the annual price; anything else is monthly.
  const price = (req.data && req.data.interval === 'year') ? PRICE_ANNUAL : PRICE_MONTHLY;
  const meta = { uid, product: 'hcg-all-access' };
  const session = await stripe.checkout.sessions.create({
    mode: 'subscription',
    allow_promotion_codes: true,
    line_items: [{ price, quantity: 1 }],
    metadata: meta,
    subscription_data: { metadata: meta },
    client_reference_id: uid,
    success_url: `${APP_URL}/subscribe-success?session_id={CHECKOUT_SESSION_ID}`,
    cancel_url: `${APP_URL}/subscribe`,
  });
  return { url: session.url };
});

async function uidForSubscription(sub) {
  if (sub.metadata && sub.metadata.uid) return sub.metadata.uid;
  // Fallback: find the HCG user who already carries this Stripe customer/subscription.
  const bySub = await db.collection('hcgUsers')
    .where('entitlement.stripeSubscriptionId', '==', sub.id).limit(1).get();
  if (!bySub.empty) return bySub.docs[0].id;
  if (sub.customer) {
    const byCust = await db.collection('hcgUsers')
      .where('entitlement.stripeCustomerId', '==', sub.customer).limit(1).get();
    if (!byCust.empty) return byCust.docs[0].id;
  }
  return null;
}

async function writeEntitlement(uid, sub) {
  const status = sub.status || 'canceled';
  const entitled = status === 'active' || status === 'trialing';
  await db.doc(`hcgUsers/${uid}`).set({
    entitlement: {
      allAccess: entitled,
      status,
      currentPeriodEnd: sub.current_period_end
        ? Timestamp.fromMillis(sub.current_period_end * 1000) : null,
      stripeCustomerId: sub.customer || null,
      stripeSubscriptionId: sub.id || null,
      updatedAt: FieldValue.serverTimestamp(),
    },
  }, { merge: true });
  return entitled;
}

// Webhook: Stripe -> Firestore entitlement. Registered in Stripe for this function's URL.
exports.stripeWebhook = onRequest({ secrets: [stripeSecret, webhookSecret] }, async (req, res) => {
  const stripe = Stripe(stripeSecret.value());
  let event;
  try {
    event = stripe.webhooks.constructEvent(
      req.rawBody, req.headers['stripe-signature'], webhookSecret.value());
  } catch (e) {
    console.error('webhook signature failed', e.message);
    res.status(400).send('bad signature');
    return;
  }
  try {
    if (event.type === 'checkout.session.completed') {
      const s = event.data.object;
      const uid = (s.metadata && s.metadata.uid) || s.client_reference_id;
      if (!uid) throw new Error('checkout completed without uid');
      if (s.subscription) {
        const sub = await stripe.subscriptions.retrieve(s.subscription);
        await writeEntitlement(uid, sub);
      }
    } else if (event.type === 'customer.subscription.updated'
        || event.type === 'customer.subscription.deleted') {
      const sub = event.data.object;
      const uid = await uidForSubscription(sub);
      if (uid) await writeEntitlement(uid, sub);
      else console.error('subscription event without resolvable uid', sub.id);
    }
    res.json({ received: true });
  } catch (e) {
    console.error('webhook handler error', e);
    res.status(500).send('handler error');
  }
});
