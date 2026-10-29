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
