# The Modern America cover notes

Built 2026-10-22, following the construction of the Civil Rights cover (cover-civil-rights.html): navy background, cream wordmark, rust rule, one period photograph, contents lines, Knoweth footer. Source file: cover-modern-america.html. Outputs: modern-america-cover.png (1632 x 2112) and modern-america-cover.pdf (printable, US Letter).

## Photograph

- Title: President George H. W. Bush signing the Americans with Disabilities Act on the South Lawn of the White House, July 26, 1990
- What it actually is: The ADA signing ceremony on the White House South Lawn. President Bush sits at the signing desk at center, pen in hand; seated to his left is Evan Kemp, chairman of the Equal Employment Opportunity Commission, and to his right Justin Dart, the disability rights leader, in his cowboy hat; the Reverend Harold Wilke and Sandra Parrino of the National Council on Disability stand behind. The same photograph ships in the unit itself, in Lesson 3 (assets/ada-signing.jpg; the lesson's deck crops ada-port.jpg, ada-wide.jpg, and bush-port.jpg derive from it), where the lesson's SOURCES.md carries its full record.
- Creator: George Bush Presidential Library and Museum photograph (National Archives photo P14777-18, as described on the National Archives Prologue blog for the same signing photograph)
- Date: July 26, 1990
- Repository: George Bush Presidential Library and Museum, via the National Archives
- Identifiers: National Archives photo P14777-18
- Public domain basis: A work of the United States federal government, a White House photograph held by the George Bush Presidential Library, public domain as a federal work. Lesson 3's SOURCES.md records the same basis.
- Honest caveat, carried from Lesson 3's build record: during the unit build, direct fetches of the two Wikimedia Commons file pages for the ADA signing and Gulf War photographs returned HTTP 403 and were not retried; the public-domain basis rests on the photograph's status as a federal work, the Commons category listings, and the National Archives' own description of this signing photograph (photo P14777-18), not on a line-by-line read of the Commons file page. The cover relies on the same basis the unit itself ships.
- The copy held locally is covers/modern-america-ada-signing-1990.jpg (1920 x 1530), the unit's own shipped copy of the photograph, taken from Lesson 3's img/. The cover HTML renders from it directly; at 1920 px wide it prints cleanly at the cover frame's size, so no separate downscaled render copy was needed. The cover frame crop (object-fit: cover, object-position center 32%) holds the president at the desk with Kemp and Dart seated beside him; visually checked.

## Previews

- preview-ma-1.html: the full plate, one row per lesson, in the pilot's plate-overview construction. Output ma-preview-1.png (1800 x 1350).
- preview-ma-2.html: real document pages, Lesson 1 activity page 1 and Lesson 4 reading page 1, rendered from the built PDFs at 130 dpi into covers/pages/ (ma-l1-activity-p1-1.png, ma-l4-reading-p1-1.png). Output ma-preview-2.png.
- preview-ma-3.html: unit test page 1 and the teacher answer key page (page 9, the first key page, with the blueprint tags printed as "(Blueprint N)" after each answer) from the same renders (ma-test-p1-1.png, ma-test-p9-9.png). Output ma-preview-3.png.

The cover and preview PNGs are copied to site/public/assets/ (as modern-america-cover.png and modern-america-preview-1/2/3.png) for the unit page and course page. The cover PDF stays in covers/ only: Modern America is an All-Access unit, so none of its PDFs, the cover included, are posted to the site as downloads.
