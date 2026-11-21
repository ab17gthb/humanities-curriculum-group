// Humanities Curriculum Group paywall backend: Stripe Checkout + webhook entitlements.
// Secrets in Secret Manager: HCG_STRIPE_SECRET_KEY (this app's own live
// Stripe key — the shared STRIPE_SECRET_KEY stays with the project's other
// app and remains in test mode), HCG_STRIPE_WEBHOOK_SECRET (this app's
// webhook endpoint signing secret).
// The webhook function is the ONLY writer of hcgUsers/{uid}.entitlement;
// Firestore rules forbid clients from creating or changing that field.

const { onCall, onRequest, HttpsError } = require('firebase-functions/v2/https');
const { defineSecret } = require('firebase-functions/params');
const admin = require('firebase-admin');
const { getFirestore, Timestamp, FieldValue } = require('firebase-admin/firestore');
const Stripe = require('stripe');

admin.initializeApp();
const db = getFirestore();

const stripeSecret = defineSecret('HCG_STRIPE_SECRET_KEY');
const webhookSecret = defineSecret('HCG_STRIPE_WEBHOOK_SECRET');

const APP_URL = 'https://humanitiescurriculumgroup.web.app';
const PRICE_MONTHLY = 'price_1UUQHwJil0sQFH0umlztb3X3'; // HCG All-Access, $9.99/month, Stripe LIVE mode (restored 2026-10-26 after the 99-cent proof; temp price price_1UUSAtJil0sQFH0uWrCHKTB3 deactivated)
const PRICE_ANNUAL = 'price_1UUQHxJil0sQFH0u5MpXmjSj'; // HCG All-Access, $59/year, Stripe LIVE mode

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

// ---------------- Site stats (first-party, aggregate only) ----------------
// logEvent receives tiny counters from the site's stats.js: page views,
// downloads, checkout starts, and signups. It validates the payload against
// allowlists and adds increments to a daily document in hcgStats (keyed by
// America/New_York date). Nothing about the visitor is stored: no IP, no
// user agent, no identifier. Firestore rules make the collection
// admin-read-only; this function is its only writer.
const STAT_EVENTS = ['view', 'download', 'checkout', 'signup'];
const STAT_SOURCES = ['direct', 'google', 'facebook', 'tpt', 'bing', 'duckduckgo', 'other'];
const ADMIN_EMAILS = ['alexbrouhard1@gmail.com', 'alexbrouhardedu@gmail.com', 'knowethcg@gmail.com'];

exports.logEvent = onRequest(async (req, res) => {
  res.set('Access-Control-Allow-Origin', APP_URL);
  if (req.method === 'OPTIONS') {
    res.set('Access-Control-Allow-Methods', 'POST');
    res.set('Access-Control-Allow-Headers', 'Content-Type');
    return res.status(204).send('');
  }
  if (req.method !== 'POST') return res.status(405).send('');
  let data = req.body;
  if (Buffer.isBuffer(data)) data = data.toString('utf8');
  if (typeof data === 'string') {
    try { data = JSON.parse(data); } catch (e) { return res.status(400).send(''); }
  }
  if (!data || typeof data !== 'object') return res.status(400).send('');
  const e = data.e, p = data.p, s = data.s;
  if (!STAT_EVENTS.includes(e)) return res.status(400).send('');
  if (typeof p !== 'string' || !/^[a-z0-9][a-z0-9-]{0,40}$/.test(p)) return res.status(400).send('');
  const day = new Intl.DateTimeFormat('en-CA', {
    timeZone: 'America/New_York', year: 'numeric', month: '2-digit', day: '2-digit'
  }).format(new Date());
  const inc = FieldValue.increment(1);
  const update = {};
  if (e === 'view') {
    update.viewsTotal = inc;
    update.views = { [p]: inc };
    if (typeof s === 'string' && (STAT_SOURCES.includes(s) || /^[a-z0-9.-]{1,40}$/.test(s))) {
      update.sources = { [s]: inc };
    }
  } else if (e === 'download') {
    update.downloadsTotal = inc;
    update.downloads = { [p]: inc };
  } else if (e === 'checkout') {
    update.checkouts = inc;
  } else if (e === 'signup') {
    update.signups = inc;
  }
  await db.doc(`hcgStats/${day}`).set(update, { merge: true });
  return res.status(204).send('');
});

// Callable: the active All-Access subscription count for the admin stats
// page. The dashboard client cannot list hcgUsers (rules forbid it), so
// the count is computed here with the Admin SDK after checking the
// caller's email against the same admin list the Firestore rules use.
exports.hcgStatsSummary = onCall(async (req) => {
  const email = req.auth && req.auth.token && req.auth.token.email;
  if (!email || !ADMIN_EMAILS.includes(String(email).toLowerCase())) {
    throw new HttpsError('permission-denied', 'Admins only');
  }
  const snap = await db.collection('hcgUsers').where('entitlement.allAccess', '==', true).get();
  let active = 0;
  snap.forEach((doc) => {
    const st = doc.get('entitlement.status');
    if (st === 'active' || st === 'trialing') active++;
  });
  return { active };
});
