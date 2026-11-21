// Humanities Curriculum Group — site-wide Firebase + payments config.
// Same Firebase project as Rycal (cue-bb34b); values copied from the Rycal
// web app config, which already runs Google sign-in on this project.
// NOTE: humanitiescurriculumgroup.web.app must be listed under Firebase
// Console > Authentication > Settings > Authorized domains or Google
// sign-in popups will fail on the live site.
window.HCG_FIREBASE_CONFIG = {
    apiKey: "AIzaSyANv25UmX3LZBtoCqDVOu12cSfdvkoUVcM",
    authDomain: "humanitiescurriculumgroup.web.app",
    projectId: "cue-bb34b",
    storageBucket: "cue-bb34b.firebasestorage.app",
    messagingSenderId: "552988749111",
    appId: "1:552988749111:web:478c2f947f0b5d20be7eb2",
    measurementId: "G-640TS7NT1F"
  };

// Stripe — LIVE MODE (switched 2026-10-25). Signed-in checkout runs
// through the createHcgCheckout function (account-bound, so the
// stripeWebhook function can switch All-Access on automatically). This
// payment link remains only as the signed-out fallback. All-Access,
// $9.99/month or $59/year. Product prod_VVRA1YXjhrEjTz, monthly price
// price_1UUQHwJil0sQFH0umlztb3X3, annual price
// price_1UUQHxJil0sQFH0u5MpXmjSj, payment link plink_1UUQI2Jil0sQFH0uYC7OeEIF.
// After checkout both paths redirect to
// https://humanitiescurriculumgroup.web.app/subscribe-success
window.HCG_STRIPE = {
  monthlyLink: "https://buy.stripe.com/9B6cN69KXa7h3iobFScV200",
  monthlyPriceLabel: "$9.99/month"
};
