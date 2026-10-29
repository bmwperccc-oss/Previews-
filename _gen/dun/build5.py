import os
import sys,os,re,json,base64,zipfile
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import build4
from common import *
V=os.path.dirname(os.path.abspath(__file__))+'/..'
def b64s(f): return base64.b64encode(open(f,'rb').read()).decode()
CORE=b64s(V+'/lib/three_core.js');MOD=b64s(V+'/lib/three_mod.js');ENG=open(os.path.dirname(os.path.abspath(__file__))+'/engine.js').read()
IMP='<script type="importmap">{"imports":{"three":"data:text/javascript;base64,%s","three-core":"data:text/javascript;base64,%s"}}</script>'%(MOD,CORE)
LC=open(V+'/lib/liquidchrome.js').read().replace('</script','<\\/script')
FX=open(os.path.dirname(os.path.abspath(__file__))+'/fx.js').read()
EXTRA_CSS='''#cur{position:fixed;left:0;top:0;width:18px;height:18px;margin:-9px 0 0 -9px;border:1.5px solid #fff;border-radius:50%;pointer-events:none;z-index:90;mix-blend-mode:difference;transition:width .25s,height .25s,margin .25s,background .25s}#cur.big{width:56px;height:56px;margin:-28px 0 0 -28px;background:rgba(255,255,255,.9)}body:after{content:"";position:fixed;inset:0;pointer-events:none;z-index:55;opacity:.07;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/></filter><rect width='160' height='160' filter='url(%23n)'/></svg>")}
.lcbg{position:absolute;inset:0;z-index:0;pointer-events:none;opacity:var(--lco,.4)}.lcbg canvas{width:100%;height:100%;display:block}.lc-fallback{background:radial-gradient(60% 60% at 70% 30%,var(--lcc,rgba(47,107,255,.5)),transparent)}
.heroc{z-index:3!important}.glwrap{position:relative}.gl{position:absolute;inset:0;z-index:2;touch-action:pan-y;cursor:grab}.gl:active{cursor:grabbing}.glwrap.ok .fb{display:none}.glwrap.ok:before{display:none}
.hero>*:not(.lcbg):not(.gl):not(.glwrap):not(.reactor),.sky>*:not(.lcbg):not(.gl):not(.mt):not(#fl){position:relative;z-index:1}.hero,.sky{position:relative;overflow:hidden}.hero>.glwrap,.hero>.reactor{z-index:2}'''
CFG={
 'titan':dict(scene=dict(kind='blueprint',accent='#7dd3fc',metal=0x9fb8d6,envTop='#9fcbff',envMid='#1c4a7d',envBot='#06142a'),lc=dict(color='#2b6fff',lco='.35',target='#top',amp=.25)),
 'strengthco':dict(scene=dict(kind='lift',accent='#ffd400',envTop='#eef0f4',envMid='#6b707c',envBot='#0c0d10',exposure=1.2),lc=dict(color='#ffd400',lco='.28',target='.stick',amp=.2)),
 'wboxing':dict(scene=dict(kind='bag',accent='#e0b04a',envTop='#dfe9ff',envMid='#34445e',envBot='#070d17'),lc=dict(color='#e0b04a',lco='.25',target='#top',amp=.22)),
 'queenstowngym':dict(scene=dict(kind='float',accent='#ff7a3d',envTop='#ffffff',envMid='#8ecdf2',envBot='#2a4d73',exposure=1.0),lc=dict(color='#9fd6ff',lco='.32',target='.sky',amp=.2)),
 'coremma':dict(scene=dict(kind='core',accent='#b6ff3b'),lc=dict(color='#b6ff3b',lco='.3',target='#top',amp=.22)),
}
def patch(slug,body,js):
    if slug=='titan':
        body=re.sub(r'(<div class="draw" id="draw">.*?<div class="dim"></div></div>)',r'<div class="glwrap" style="height:clamp(360px,46vw,620px)"><div id="gl" class="gl"></div><div class="fb">\1</div></div>',body,flags=re.S)
    if slug=='strengthco':
        body=body.replace('<div class="stick">','<div class="stick"><div id="lcmount"></div><div id="gl" class="gl" style="z-index:1"></div>',1)
        js=js.replace('cap.textContent=caps[n]}});','cap.textContent=caps[n];window.__lift&&window.__lift(n)}});')
    if slug=='wboxing':
        body=re.sub(r'<div class="bagwrap">(<div id="bag">.*?</div>)(<div class="bh">.*?</div>)</div>',r'<div class="bagwrap glwrap"><div id="gl" class="gl"></div><div class="fb">\1</div>\2</div>',body,flags=re.S)
    if slug=='queenstowngym':
        body=body.replace('<div id="fl"></div>','<div id="fl"></div><div id="gl" class="gl" style="z-index:2"></div>',1)
    if slug=='coremma':
        body=re.sub(r'<div class="reactor" id="rx">(<div class="rg" id="rg">(?:<div class="ring"></div>){4}</div>)</div>',r'<div class="reactor glwrap" id="rx"><div id="gl" class="gl"></div><div class="fb">\1</div></div>',body,flags=re.S)
    return body,js
def build(slug,x,out):
    fonts,css,body,js,theme=build4.FN[x['style']](x)
    body,js=patch(slug,body,js)
    cfg=CFG[slug];lc=cfg['lc']
    css=css+EXTRA_CSS+'.sky.ok #fl{display:none}.stick.ok .bb{visibility:hidden}.stick{position:sticky}'
    h=page(x,fonts,css,body,js,theme)
    tgt=lc['target']
    mount="document.querySelector('%s')"%tgt
    init='''<script>(function(){if(!document.documentElement.classList.contains('js'))return;function go(){try{var t=%s;if(!t)return;var d=document.createElement('div');d.className='lcbg';d.style.setProperty('--lco','%s');t.insertBefore(d,t.firstChild);try{initLiquidChrome(d,{color:'%s',speed:.18,amplitude:%s,frequencyX:3,frequencyY:3,detail:4,roughness:.3,interactive:true,maxDevicePixelRatio:1.15})}catch(e){d.classList.add('lc-fallback')}}catch(e){}}
 var fine=matchMedia('(hover:hover) and (pointer:fine)').matches;if(!fine){var t=%s;if(t){var d=document.createElement('div');d.className='lcbg lc-fallback';d.style.setProperty('--lco','.6');t.insertBefore(d,t.firstChild)}return}
 if(document.readyState==='complete')setTimeout(go,300);else addEventListener('load',function(){setTimeout(go,300)})})();</script>'''%(mount,lc['lco'],lc['color'],lc['amp'],mount)
    scripts='<script>%s</script>%s<script>window.__SCENE=%s</script>%s<script type="module">%s</script><script>%s</script>'%(LC,init,json.dumps(cfg['scene']),IMP,ENG.replace('</script','<\\/script'),FX)
    h=h.replace('</body>',scripts+'</body>')
    d='%s/%s'%(out,slug);os.makedirs(d,exist_ok=True);open(d+'/index.html','w').write(h)
    with zipfile.ZipFile('%s/%s.zip'%(out,slug),'w',zipfile.ZIP_DEFLATED) as z: z.write(d+'/index.html','index.html')
    print(slug,len(h)//1024,'KB')
if __name__=='__main__':
    out=sys.argv[1];os.makedirs(out,exist_ok=True)
    for x in build4.CL:
        if len(sys.argv)<3 or x['slug'] in sys.argv[2:]: build(x['slug'],x,out)
