# Learnings (daily improve log)

## Rules for the daily batch
- Before sending, check the domain resolves (e.g. `dig +short MX domain`). 4 of 31 first sends bounced: 2 inferred/typo'd domains (brockfitness.nz, strengthnco.com), 1 wrong gmail address, 1 `info@` group on a PlaySport listing. Never use "inferred" or "listing (inferred)" contact sources; prefer an address copied verbatim from the business's own site.
- Sample size is tiny (31 sent, 0 replies as of 2026-10-29): do not change approach wording on this data yet.
- Available 3D kinds: lift, blueprint, bag, float, core, rings, tramp, stones, lotus, shoe, ribbon, mirrorball, ballerina, cafe (new), none. Use `kind='cafe'` (preset `espresso-latte`) for cafes/coffee/bakeries.

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
