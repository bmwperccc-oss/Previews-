# Learnings (daily improve log)

## Rules for the daily batch
- Before sending, check the domain resolves (e.g. `dig +short MX domain`). 4 of 31 first sends bounced: 2 inferred/typo'd domains (brockfitness.nz, strengthnco.com), 1 wrong gmail address, 1 `info@` group on a PlaySport listing. Never use "inferred" or "listing (inferred)" contact sources; prefer an address copied verbatim from the business's own site.
- Sample size is tiny (31 sent, 0 replies as of 2026-10-29): do not change approach wording on this data yet.
- Available 3D kinds: lift, blueprint, bag, float, core, rings, tramp, stones, lotus, shoe, ribbon, mirrorball, ballerina, cafe, barber (new 2026-10-31), none. Use `kind='cafe'` (preset `espresso-latte`) for cafes/coffee/bakeries.

## 2026-10-29
- Stats: 31 sent, 27 delivered, 0 replies, 4 bounces. No approach/type/style can be ranked yet.
- Improvement (b): new 3D `cafe` kind (coffee cup, saucer, steam, beans) + `espresso-latte` preset; checked desktop 1440x900 and mobile 390x844, no JS errors.
- Fix: generator could not run from a fresh clone (build4 imports missing build3). Added a stub `_gen/dun/build3.py`; gen.py JSON path does not use it.
- Sample config: `_gen/dun/example_cafe.py` (writes cfg.json).

## 2026-10-30
- Stats: 36 sent, 5 bounced, 1 reply (Pulse Pilates: "No thanks", reason not given), 0 interested. Too small to rank anything.
- Bounces by source: own website address copied verbatim 0/8; PlaySport/listing pages 2/~19 (Hybrid gmail, CrossFit Whakatane info@); inferred 2/4 (Brock, Strength&Co typo); Lovetaupo.com operator listing 1/2 (Mancraft hello@ rejected 550 even though copied verbatim). gymkids.co.nz had a temporary delivery delay (Cloudflare timeouts), retrying.
- Improvement (a): rebuilt the `shoe` 3D kind. It was a vase-like lathe tube; it is now a lofted pointe shoe (squared toe-box platform, tapered vamp, V-shaped throat opening, dark lining, drawstring, binding and sole stitch lines). Checked desktop 1440x900 (layouts a and c) and mobile 390x844, no JS errors. Published sites (e.g. dancemasters) were NOT regenerated.

## Rules for the daily batch (added 2026-10-30)
- Contact source ranking: (1) address visible on the business's own website; (2) directory listing only if the domain has a real site AND the address matches it; never use generic info@/hello@ from a third-party listing (Lovetaupo, PlaySport, Age Concern) without a second confirmation (the business's own site or Facebook page). Prefer personal-name addresses.
- Reason for no-thanks replies is not captured; keep the "reply no thanks" line, do not change wording yet.

## 2026-10-31
- Stats: 36 sent, 1 reply (no thanks, Pulse Pilates), 0 interested, 5 hard bounces (+1 temporary delay, gymkids.co.nz). 6 queued. Too small to rank approaches/styles.
- Bounces by source: PlaySport info@ listing 2 (Hybrid gmail, CrossFit Whakatane), inferred/typo domain 2, Lovetaupo listing 1 (Mancraft hello@). Own-website addresses: 0 bounces so far. Rule stands: own-site verbatim addresses first.
- Change today: added kind=barber (striped pole with scrolling stripes, scissors, comb). Verified desktop 1440x900 and mobile 390x844, no JS errors, object fully visible. No existing published folder touched.
- Rule: use kind=barber for barbers/hair; do not reuse kind=core for them. Mancraft (barber, bounced) could be rebuilt as a new slug only if a verified contact is found.

## 2026-11-01
- Stats: 36 sent (+6 sent 2026-11-02 NZ, 8 queued), 1 reply (Pulse Pilates no thanks), 0 interested, 6 bounces (Gym Kids timed out, status 4.4.1, now logged as bounced). Own-website addresses: 0 bounces. Too small to rank anything.
- Change today: added kind=plumb (wrench, pipe elbow + valve wheel, drops). Checked desktop 1440x900 and mobile 390x844, no JS errors, object fully visible. The wrench head is still fairly simple; candidate for a later polish. No published folder touched.
- Rule: use kind=plumb for plumbers/gasfitters/drainlayers; keep kind=core for electricians.

## 2026-11-02
- Stats: 50 rows sent (49 unique recipients; Dunedin Kickboxing duplicated), 2 replies (both "no thanks": Pulse Pilates, approach A + lotus; Tudor House of Flowers, approach G + ribbon, no reason given), 0 interested, 6 bounces (all third-party listing/inferred sources; 14 own-site addresses sent 2026-11-02 so far: 0 bounces, 1 reply). Too small to rank approaches, types, styles or cities.
- Change today: added kind=paw (paw print on a ringed disc, bone, bouncing ball, heart) with `paw` scene in gen.py; sample `_gen/dun/example_paw.py`. Checked desktop 1440x900 and mobile 390x844, no JS errors, object fully visible. No published folder touched.
- Rule: use kind=paw for vets, dog/cat groomers, kennels/daycare, pet shops (Klipped K9 used kind=ribbon; leave as is).

## 2026-11-03
- Stats: 64 rows sent (63 unique), 2 replies (both polite "no thanks": Pulse Pilates A/lotus, Tudor House of Flowers G/ribbon, no reasons given), 0 interested, 6 bounces (all third-party listing or inferred sources). 28 own-site addresses sent 2026-11-02/03: 0 bounces so far, 0 new replies. Too small to rank anything.
- Change today: added kind=gear (two meshing toothed gears with accent hubs, hex bolt, spark plug) with `gear` scene in gen.py; sample `_gen/dun/example_gear.py`. Checked desktop 1440x900 and mobile 390x844, no JS errors, object fully visible on desktop. No published folder touched.
- Rule: use kind=gear for mechanics/auto repair/workshops (four mechanics so far used kind=core; leave those as is).
