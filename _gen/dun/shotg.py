import asyncio,sys,os
from playwright.async_api import async_playwright
A=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']
async def one(b,slug,tag,vp,mob,fr):
    c=await b.new_context(viewport=vp,is_mobile=mob,has_touch=mob,device_scale_factor=1)
    pg=await c.new_page();errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)[:120]))
    pg.on('console',lambda m:errs.append(m.text[:120]) if m.type=='error' else None)
    await pg.goto('file://'+os.path.abspath(f'out_gen/{slug}/index.html'));await pg.wait_for_timeout(3500)
    H=await pg.evaluate('document.documentElement.scrollHeight');W=await pg.evaluate('document.documentElement.scrollWidth')
    for i,f in enumerate(fr):
        if f: await pg.evaluate(f'window.scrollTo(0,{int(H*f)})');await pg.wait_for_timeout(2200 if not mob else 700)
        await pg.screenshot(path=f'out_gen/{slug}_{tag}{i}.png')
    await c.close();return slug,tag,H,W,errs[:3]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=A)
        for s in sys.argv[1:]:
            print(await one(b,s,'d',{'width':1440,'height':900},False,(0,.1,.2)))
            print(await one(b,s,'m',{'width':390,'height':844},True,(0,)))
        await b.close()
asyncio.run(main())
