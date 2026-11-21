# Email capture build brief — prepared 2026-11-03

Status: PARTLY BUILT 2026-11-04. Alex directed the capture piece in the HCG chat ("on hcg when people download the free lesson can we have them enter their email or sign up? ... ill put together a email address later but at least we will have a list"). The HCG door is LIVE: the free Progressive Era unit asks for an email on the first download in a browser, saves it to Firestore hcgLeads, and unlocks the rest of the unit in that browser; the admin Email list page (leads.html) dedupes and exports the list. Nothing is sent yet. The sending side below (domain, ESP, CAN-SPAM address) is still undecided, in the order listed at the bottom. Alex explored the idea in the Marketing chat on 2026-11-03 (prompted by Teacher Seller School ads) and asked what the address should be and whether TPSP can sit under Humanities Curriculum Group. This brief consolidates that discussion with the earlier scoping from 2026-10-26 (memory/2026-10-26.md).

## The idea as Alex has it in front of him

Every free asset gets an email door. The Primary Source Sampler becomes a website download instead of TpT-only, the free Progressive Era unit gets a "send me the free unit" door, and TPSP offers a free DBQ starter pack with the DEMO code inside. One list for both sites, tagged by which door the teacher came through. Delivery email first, then a short welcome run built from the existing story bank, then one email a week in the same format, with a plain sales email only when there is something real to sell. No countdown timers, no fake deadlines, no bought lists.

TpT cannot feed this list. TpT shares no buyer emails with sellers, and its guidelines bar requiring personal information to access a purchase. The clean path is the one already built: the pitch pages inside the TpT files route buyers to the websites, where they can sign up voluntarily.

## Verified facts (checked 2026-11-03, ~1:40 PM ET, Porkbun)

- humanitiescurriculumgroup.com — available, $11.81 first year, $11.81 renewal.
- theprimarysourceproject.com — available, $11.81 first year, $11.81 renewal. This settles the open question from the Marketing chat, where the .com registry lookup kept failing and Muse could not confirm it either way.
- theprimarysourceproject.org — available, $7.98 first year on sale, $11.84 renewal.

Nothing was purchased. Registering a domain is spending, which stays Alex's step.

Sender setup from today's chat: hello@humanitiescurriculumgroup.com, sent from the name "Humanities Curriculum Group." TPSP sends ride the same domain with "The Primary Source Project" as the sender name. Stripe accounts and subscriptions stay separate, exactly as Alex set them. Replies forward to his existing private inbox; no public contact address appears on either site.

## From the 2026-10-26 scoping (still the build plan)

- An email service handles sending and unsubscribes. Loops and Brevo were the two named; both had free tiers around 1,000 contacts at scoping time. Re-check current free-tier terms at build time.
- A welcome email can also fire on website account creation through the existing Firebase functions pipeline, since every signup email already sits in Firebase Auth / hcgUsers. That covers site members; the freebie doors cover everyone else.
- Sending needs SPF/DKIM records on the new domain. Muse adds those once the domain exists. Sending marketing mail off the web.app setup is a spam-folder trap, which is why the domain comes first.
- One Privacy Policy paragraph plus an opt-in line at signup. Estimate from October stands: about a day of setup, mostly DNS waiting.

## The one decision today's chat did not surface

CAN-SPAM requires a physical mailing address in every marketing email footer. The October scoping flagged this and noted a PO Box fits Alex's non-identifying rule (no personal name, school, or town in public copy). Alex has never picked the address. Options when he is ready: register a PO Box, or use another business mailing address he controls. Nothing sends until this is settled, so it belongs on the decision list next to the domain, not discovered mid-build.

## Decisions queue for Alex, in order

1. Go or no-go on the email build itself.
2. Register humanitiescurriculumgroup.com ($11.81/yr at Porkbun, checked 2026-11-03). His hands, his card. Optional later: theprimarysourceproject.com at the same price if he wants the matching TPSP address someday.
3. The footer mailing address (PO Box or other).

Everything after those three is Muse's build: ESP setup, SPF/DKIM, the three capture doors, delivery and welcome emails drafted from the story bank for his approval, the Privacy Policy paragraph, and a test send verified before anything goes to a real list.
