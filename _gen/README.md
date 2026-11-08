# Site generator
Build: `python3 _gen/dun/gen.py OUTDIR --json cfg.json` (cfg.json = list of business configs; see PRESETS/SCENES in gen.py and the CL examples).
Needs only python3 (no pip). Each config -> OUTDIR/<slug>/index.html (single file, ~1.8MB with 3D, ~0.2MB when kind=none).
Fields: slug,name,suburb,headline,sub,cta_label,cta_url,words[],serv_title,services[{title,desc}],address,phone,email,close,close_sub,facts[[label,value]x3],card[small,html],band[title,text],kind(lift|blueprint|bag|float|core|rings|tramp|stones|lotus|shoe|ribbon|mirrorball|ballerina|cafe|barber|plumb|none),layout(a|b|c),preset(see PRESETS),font(anton|bsd|fraunces),scene{} overrides.
Test: python3 _gen/dun/shotg.py (needs playwright, expects out_gen/<slug>/index.html).

New: kind=cafe (coffee cup, steam) with preset espresso-latte; see _gen/dun/example_cafe.py. Read _gen/LEARNINGS.md "Rules for the daily batch" before each batch (verify domains resolve before sending).

2026-10-30: kind=shoe rebuilt (proper pointe shoe shape, use with preset black-gold/blush for ballet/dance). See LEARNINGS.md for the stricter contact-source rules (own-site addresses first).

2026-10-31: kind=barber (rotating barber pole, scissors, comb) with preset black-gold (or any); see _gen/dun/example_barber.py. Use for barbers/hair; keep kind=core for electricians/trades.

2026-11-01: kind=plumb (adjustable wrench, brass pipe elbow with spinning valve wheel, dripping water) with any preset; see _gen/dun/example_plumb.py. Use for plumbers, drainlayers, gasfitters, handymen. Electricians stay on kind=core.

2026-11-02: kind=paw (paw print, bone, ball, heart) with any preset; see _gen/dun/example_paw.py. Use for vets, groomers, kennels, pet shops. Added to kind list: lift|blueprint|bag|float|core|rings|tramp|stones|lotus|shoe|ribbon|mirrorball|ballerina|cafe|barber|plumb|paw|none.

2026-11-03: kind=gear (meshing gears with accent hubs, hex bolt, spark plug) with any preset; see _gen/dun/example_gear.py. Use for mechanics, auto repair, engineering, workshops (instead of kind=core). Kind list now: lift|blueprint|bag|float|core|rings|tramp|stones|lotus|shoe|ribbon|mirrorball|ballerina|cafe|barber|plumb|paw|gear|none.

2026-11-04: kind=lotus rebuilt (6 petal layers with gradient, seed pod, stamens, ripples); sample `_gen/dun/example_lotus.py`. Use for spas, yoga, pilates, massage, florists. Kind list unchanged.

2026-11-05: kind=rings polished (wood grain, buckles, stitched straps, chalk dust); sample `_gen/dun/example_rings.py`. Use for gymnastics clubs. Kind list unchanged.

2026-11-06: kind=plumb wrench rebuilt (tapered handle, hooked fixed jaw, serrated sliding jaw, knurled worm); sample `_gen/dun/example_plumb.py`. Kind list unchanged.

2026-11-07: kind=shoe rebuilt (squared platform, seams, pleats, crossed ribbons, pair shifted clear of the card); sample `_gen/dun/example_shoe.py` (uses presets black-gold / blush-pink). Kind list unchanged.

2026-11-08: generator now emits meta description, Open Graph title/description and an accent-coloured inline SVG favicon (initial of the business) on every new page (common.py). No config change needed; published folders were NOT regenerated.
