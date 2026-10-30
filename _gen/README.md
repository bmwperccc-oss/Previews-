# Site generator
Build: `python3 _gen/dun/gen.py OUTDIR --json cfg.json` (cfg.json = list of business configs; see PRESETS/SCENES in gen.py and the CL examples).
Needs only python3 (no pip). Each config -> OUTDIR/<slug>/index.html (single file, ~1.8MB with 3D, ~0.2MB when kind=none).
Fields: slug,name,suburb,headline,sub,cta_label,cta_url,words[],serv_title,services[{title,desc}],address,phone,email,close,close_sub,facts[[label,value]x3],card[small,html],band[title,text],kind(lift|blueprint|bag|float|core|rings|tramp|stones|lotus|shoe|ribbon|mirrorball|ballerina|cafe|none),layout(a|b|c),preset(see PRESETS),font(anton|bsd|fraunces),scene{} overrides.
Test: python3 _gen/dun/shotg.py (needs playwright, expects out_gen/<slug>/index.html).

New: kind=cafe (coffee cup, steam) with preset espresso-latte; see _gen/dun/example_cafe.py. Read _gen/LEARNINGS.md "Rules for the daily batch" before each batch (verify domains resolve before sending).

2026-10-30: kind=shoe rebuilt (proper pointe shoe shape, use with preset black-gold/blush for ballet/dance). See LEARNINGS.md for the stricter contact-source rules (own-site addresses first).
