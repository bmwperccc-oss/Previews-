import sys,json,os,zipfile
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import *
from build3 import hl,BASE,STICKY,mq,contact_html
from eq import *
FOOT='<footer>Concept preview made by Manu. Details taken from the public website.</footer>'
def svcs(x,fmt):
    return ''.join(fmt(i,s) for i,s in enumerate(x['services']))
def hrs(x): return ''.join('<li>%s</li>'%E(h) for h in x['hours'])

# ---------- TITAN: blueprint ----------
def titan(x):
    fonts=font('Mono','fonts2/mono.woff','700')+font('SG','fonts2/sg.woff','300 700')
    css=BASE+'''body{background:#0a2540;color:#dbeafe;font:400 16px/1.6 SG,sans-serif;background-image:linear-gradient(rgba(125,211,252,.10) 1px,transparent 1px),linear-gradient(90deg,rgba(125,211,252,.10) 1px,transparent 1px),linear-gradient(rgba(125,211,252,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(125,211,252,.05) 1px,transparent 1px);background-size:120px 120px,120px 120px,24px 24px,24px 24px}
.m{font:700 12px/1.4 Mono,monospace;letter-spacing:.14em;text-transform:uppercase;color:#7dd3fc}h1,.hd{font-weight:700;letter-spacing:-.04em}
.top{display:flex;justify-content:space-between;padding:56px clamp(18px,4vw,56px) 0}
.hero{display:grid;grid-template-columns:1.1fr 1fr;gap:30px;align-items:center;padding:clamp(30px,6vw,80px) clamp(18px,4vw,56px) 60px;min-height:88vh}
h1{font-size:clamp(46px,8vw,128px);line-height:.92;text-transform:uppercase}h1 em{font-style:normal;color:#7dd3fc}.hero p{max-width:480px;margin:22px 0;font-size:18px;color:#b9d6f2}
.btn{background:#7dd3fc;color:#0a2540;border-radius:2px}.btn:hover{background:#fff}
.draw{position:relative;height:clamp(360px,46vw,620px);color:#7dd3fc}.draw .eq{position:absolute;overflow:visible;will-change:transform}
.draw .g{left:4%;top:2%;width:44%}.draw .k{right:2%;top:10%;width:36%}.draw .d{left:14%;bottom:4%;width:70%}.draw .p{right:0;bottom:30%;width:22%;opacity:.7}
.lab{position:absolute;font:700 11px Mono;letter-spacing:.14em;color:#7dd3fc}.lab:before{content:"";display:inline-block;width:26px;height:1px;background:#7dd3fc;vertical-align:middle;margin-right:8px}
.mq{overflow:hidden;white-space:nowrap;border-block:1px dashed rgba(125,211,252,.5);padding:14px 0}#mqt{display:inline-block}#mqt span{font:700 13px Mono;letter-spacing:.16em;text-transform:uppercase;padding:0 26px;color:#7dd3fc}#mqt span:nth-child(even){color:#fff}.dim{position:absolute;left:14%;right:16%;bottom:-4px;height:1px;background:#7dd3fc;opacity:.6}.dim:before,.dim:after{content:"";position:absolute;top:-6px;width:1px;height:13px;background:#7dd3fc}.dim:after{right:0}
.sec{padding:70px clamp(18px,4vw,56px)}.sec h2{font-size:clamp(34px,6vw,84px);line-height:.95;text-transform:uppercase;margin:8px 0 34px}
.row{display:grid;grid-template-columns:110px 1.1fr 1.6fr;gap:20px;padding:22px 0;border-top:1px dashed rgba(125,211,252,.5);align-items:baseline;transition:background .25s,padding .25s}.row:last-child{border-bottom:1px dashed rgba(125,211,252,.5)}
.row:hover{background:rgba(125,211,252,.08);padding-left:14px}.row h3{font:700 clamp(22px,3vw,40px)/1.05 SG;letter-spacing:-.03em}.row p{color:#b9d6f2}
.tb{margin:0 clamp(18px,4vw,56px) 40px;border:2px solid #7dd3fc;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}.tb>div{padding:18px 20px;border:1px solid rgba(125,211,252,.5)}.tb b{display:block;font:700 22px SG;margin-top:6px;letter-spacing:-.02em}.tb a{text-decoration:underline}
.cta{padding:clamp(60px,9vw,120px) clamp(18px,4vw,56px);text-align:center;border-top:2px solid #7dd3fc}.cta h2{font-size:clamp(42px,8vw,130px);line-height:.92;text-transform:uppercase;font-weight:700;letter-spacing:-.04em}.cta p{margin:18px auto 28px;max-width:460px;color:#b9d6f2}
footer{padding:20px clamp(18px,4vw,56px) 90px;font-size:12px;opacity:.7}#sticky a{background:#7dd3fc;color:#0a2540;border-radius:2px}
@media(max-width:820px){.hero{grid-template-columns:1fr;min-height:0}.row{grid-template-columns:70px 1fr}.row p{grid-column:2}}'''
    rows=svcs(x,lambda i,s:'<div class="row" data-r><span class="m">Fig. %02d</span><h3>%s</h3><p>%s</p></div>'%(i+1,E(s['title']),E(s['desc'])))
    body='''<div class="top m"><span>__NAME__</span><span>Sheet 01 / __SUBURB__</span></div>
<section class="hero" id="top"><div><h1 id="h1">%s</h1><p data-hero>__SUB__</p><a class="btn" data-hero href="__CTA__">__CTALABEL__ %s</a></div>
<div class="draw" id="draw">%s%s%s%s<span class="lab" style="left:6%%;top:0">FIG.01 GLOVE</span><span class="lab" style="right:4%%;top:6%%">FIG.02 KETTLEBELL</span><span class="lab" style="left:16%%;bottom:6%%">FIG.03 DUMBBELL, SCALE 1:1</span><div class="dim"></div></div></section>%s
<section class="sec"><span class="m">Specification</span><h2 class="hd">__SERVTITLE__</h2>%s</section>
<div class="tb" id="end"><div data-r><span class="m">Project</span><b>__NAME__</b></div><div data-r><span class="m">Address</span><b>__ADDRESS__</b></div><div data-r><span class="m">Contact</span><b>%s</b></div></div>
<section class="cta"><h2 class="hd">%s</h2><p data-r>__CLOSESUB__</p><a class="btn" data-r href="__CTA__">__CTALABEL__ %s</a></section>%s%s'''%(hl(x['headline']),ARROW,glove('eq g',2.4),kettle('eq k',2.4),dumbbell('eq d',2.4),plate('eq p',2.4),mq(x['words']),rows,'<br>'.join(contact_lines(x)),hl(x['close']),ARROW,FOOT,STICKY)
    js='''var ps=$$('#draw path,#draw rect,#draw circle');gsap.set(ps,{strokeDasharray:1,strokeDashoffset:1});gsap.to(ps,{strokeDashoffset:0,duration:1.6,ease:'power2.inOut',stagger:.04,delay:.4});
$$('#draw .eq').forEach(function(e,i){gsap.to(e,{y:i%2?10:-10,rotate:i%2?-2:2,duration:3+i*.4,yoyo:true,repeat:-1,ease:'sine.inOut'})});
var dr=$('#draw');addEventListener('pointermove',function(e){var x=(e.clientX/innerWidth-.5),y=(e.clientY/innerHeight-.5);$$('#draw .eq').forEach(function(el,i){gsap.to(el,{x:x*(i+1)*14,duration:.8,overwrite:'auto'})})});'''
    return fonts,css,body,js,'#0a2540'

# ---------- STRENGTH&CO: plate loader ----------
def strengthco(x):
    fonts=font('Anton','fonts2/anton.woff','400')+font('SG','fonts2/sg.woff','300 700')
    css=BASE+'''body{background:#dcd9d2;color:#141414;font:400 16px/1.6 SG,sans-serif}h1,.hd,.big{font-family:Anton,Impact,sans-serif;font-weight:400;text-transform:uppercase}
.top{display:flex;justify-content:space-between;padding:56px clamp(18px,4vw,56px) 0;font-weight:700;letter-spacing:.1em;text-transform:uppercase;font-size:13px}
.hero{padding:clamp(30px,6vw,70px) clamp(18px,4vw,56px) 40px}h1{font-size:clamp(64px,15vw,240px);line-height:.86}h1 em{font-style:normal;background:#ffd400;padding:0 .08em}.hero p{max-width:520px;margin-top:22px;font-size:19px}
.btn{background:#141414;color:#ffd400;margin-top:24px}.btn:hover{background:#ffd400;color:#141414}
.lift{height:360vh;position:relative}.stick{position:sticky;top:0;height:100vh;background:#141414;color:#dcd9d2;display:flex;flex-direction:column;justify-content:center;overflow:hidden}
.kg{position:absolute;left:clamp(18px,4vw,56px);top:84px;font:400 clamp(70px,13vw,200px)/.9 Anton;color:#ffd400}.kg small{font:700 14px SG;letter-spacing:.14em;display:block;color:#dcd9d2}
.hint{position:absolute;right:clamp(18px,4vw,56px);top:96px;font-size:13px;letter-spacing:.14em;text-transform:uppercase;text-align:right;opacity:.7}
.bb{display:flex;align-items:center;justify-content:center;--k:1;margin-top:60px}.bar{height:16px;width:clamp(70px,16vw,240px);background:linear-gradient(#bbb,#777);border-radius:2px}.sleeve{height:28px;width:30px;background:#999}.side{display:flex;align-items:center}
.pl{width:calc(24px*var(--k));height:calc(var(--h)*var(--k));background:var(--c);margin:0 2px;border-radius:5px;transform:scaleY(0);opacity:0;transition:transform .5s cubic-bezier(.2,.9,.2,1.2),opacity .3s}.pl.on{transform:none;opacity:1}
.cap{position:absolute;left:0;right:0;bottom:7vh;text-align:center;font:400 clamp(26px,4vw,56px) Anton;text-transform:uppercase}
.mq{overflow:hidden;white-space:nowrap;background:#ffd400;padding:12px 0}#mqt{display:inline-block}#mqt span{font:400 clamp(24px,3.4vw,44px) Anton;text-transform:uppercase;padding:0 22px}
.sec{padding:70px clamp(18px,4vw,56px)}.sec h2{font-size:clamp(44px,8vw,120px);line-height:.9;margin-bottom:30px}
.card{display:grid;grid-template-columns:90px 1fr;gap:16px;padding:26px 0;border-top:4px solid #141414}.card i{font:400 56px/1 Anton;font-style:normal;color:#b39500}.card h3{font:400 clamp(30px,5vw,64px)/1 Anton;text-transform:uppercase}.card p{max-width:560px;margin-top:6px}
.end{background:#ffd400;padding:clamp(60px,9vw,120px) clamp(18px,4vw,56px)}.end .big{font-size:clamp(54px,12vw,190px);line-height:.86}.end p{max-width:480px;margin:18px 0 8px}.ct{list-style:none;margin-top:26px;font-weight:700}.ct a{text-decoration:underline}
footer{padding:20px clamp(18px,4vw,56px) 90px;font-size:12px}#sticky a{background:#141414;color:#ffd400}
@media(max-width:720px){.bb{--k:.46}.sleeve{width:14px}.pl{width:calc(30px*var(--k)*2)}}'''
    plates=[(25,'#d6322f',340),(20,'#2a5fd0',300),(15,'#f2c500',262),(10,'#2e9b4a',226),(5,'#f4f4f4',176),(2.5,'#222',132)]
    L=''.join('<div class="pl" data-w="%s" style="--c:%s;--h:%dpx"></div>'%(w,c,h) for w,c,h in reversed(plates))
    R=''.join('<div class="pl" data-w="%s" style="--c:%s;--h:%dpx"></div>'%(w,c,h) for w,c,h in plates)
    cards=svcs(x,lambda i,s:'<div class="card" data-r><i>%02d</i><div><h3>%s</h3><p>%s</p></div></div>'%(i+1,E(s['title']),E(s['desc'])))
    body='''<div class="top"><span>__NAME__</span><span>__SUBURB__</span></div>
<section class="hero" id="top"><h1 id="h1">%s</h1><p data-hero>__SUB__</p><a class="btn" data-hero href="__CTA__">__CTALABEL__ %s</a></section>%s
<section class="lift" id="lift"><div class="stick"><div class="kg"><small>On the bar</small><span id="kg">20</span><span style="font-size:.35em"> KG</span></div><div class="hint">Keep scrolling<br>to load the bar</div>
<div class="bb"><div class="side">%s</div><div class="sleeve"></div><div class="bar"></div><div class="sleeve"></div><div class="side">%s</div></div><div class="cap" id="cap">Empty bar. Everyone starts here.</div></div></section>
<section class="sec"><h2 class="hd">__SERVTITLE__</h2>%s</section>
<section class="end" id="end"><div class="big hd">__CLOSE__</div><p data-r>__CLOSESUB__</p><a class="btn" data-r href="__CTA__">__CTALABEL__ %s</a>%s<ul class="ct">%s</ul></section>%s%s'''%(hl(x['headline']),ARROW,mq(x['words']),L,R,cards,ARROW,'',''.join('<li>%s</li>'%c for c in contact_lines(x)+[E(x['address'])]),FOOT,STICKY)
    js='''var pl=$$('#lift .pl'),side=6,kg=$('#kg'),cap=$('#cap'),caps=['Empty bar. Everyone starts here.','Warm-up plates on.','Now we are lifting.','Heavy and honest.','Serious weight.','Almost there.','Fully loaded. Get coached.'];
ScrollTrigger.create({trigger:'#lift',start:'top top',end:'bottom bottom',scrub:true,onUpdate:function(s){var n=Math.min(side,Math.floor(s.progress*(side+1))),tot=20;
$$('#lift .side').forEach(function(sd){var ps=$$('.pl',sd);var order=sd===$$('#lift .side')[0]?ps.slice().reverse():ps;order.forEach(function(p,i){p.classList.toggle('on',i<n)})});
for(var i=0;i<n;i++)tot+=2*parseFloat($$('#lift .side')[1].children[i].dataset.w);kg.textContent=String(tot).replace(/\\.0$/,'');cap.textContent=caps[n]}});'''
    return fonts,css,body,js,'#dcd9d2'

# ---------- WELLINGTON BOXING: heavy bag ----------
def wboxing(x):
    fonts=font('Fraunces','fonts2/fraunces.woff','300 900')+font('Manrope','fonts/manrope.woff','200 800')
    css=BASE+'''body{background:#0c1a2b;color:#f1ead9;font:400 16px/1.65 Manrope,sans-serif}h1,.hd,.serif{font-family:Fraunces,Georgia,serif;font-weight:700;letter-spacing:-.03em}
.ropes{height:34px;background:linear-gradient(#c62f2f 0 5px,transparent 5px 14px,#f1ead9 14px 19px,transparent 19px 28px,#2f5fc6 28px 33px,transparent 33px)}
.top{display:flex;justify-content:space-between;padding:50px clamp(18px,4vw,60px) 0;font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:#e0b04a}
.hero{display:grid;grid-template-columns:1.2fr .8fr;gap:20px;align-items:start;padding:clamp(30px,5vw,60px) clamp(18px,4vw,60px) 40px;min-height:86vh;overflow:hidden}
h1{font-size:clamp(46px,8.4vw,136px);line-height:.94}h1 em{font-style:italic;color:#e0b04a;font-weight:400}.hero p{max-width:470px;margin:22px 0;font-size:18px;color:#cfc8b6}
.btn{background:#e0b04a;color:#0c1a2b;border-radius:100px}.btn:hover{background:#fff}
.bagwrap{position:relative;height:clamp(420px,62vh,640px);display:flex;justify-content:center;touch-action:none}.bagwrap:before{content:"";position:absolute;top:0;left:10%;right:10%;height:8px;background:#e0b04a;border-radius:4px}
#bag{position:absolute;top:8px;left:50%;width:clamp(110px,14vw,170px);margin-left:calc(clamp(110px,14vw,170px)/-2);transform-origin:50% 0;color:#f1ead9;cursor:grab;user-select:none}#bag svg{width:100%;height:auto;display:block;overflow:visible}#bag:active{cursor:grabbing}
.bh{position:absolute;bottom:0;left:0;right:0;text-align:center;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:#e0b04a}
.sec{padding:70px clamp(18px,4vw,60px)}.sec h2{font-size:clamp(38px,6vw,90px);line-height:.98;margin-bottom:30px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px}.rd{position:relative;padding:34px 26px;background:#10253c;border-radius:6px;overflow:hidden}.rd:before,.rd:after{content:"";position:absolute;left:0;right:0;height:3px;background:#c62f2f;top:12px}.rd:after{top:20px;background:#f1ead9}
.rd i{font:italic 300 15px Fraunces;color:#e0b04a}.rd h3{font:700 28px/1.05 Fraunces;margin:10px 0 8px;letter-spacing:-.02em}.rd p{color:#cfc8b6}
.mq{overflow:hidden;white-space:nowrap;padding:24px 0}#mqt{display:inline-block}#mqt span{font:italic 300 clamp(36px,6vw,80px) Fraunces;padding:0 26px;color:#f1ead9}#mqt span:nth-child(even){color:#e0b04a}
.end{padding:clamp(60px,9vw,120px) clamp(18px,4vw,60px);text-align:center;background:#f1ead9;color:#0c1a2b}.end h2{font-size:clamp(42px,8vw,120px);line-height:.95}.end h2 em{font-style:italic;color:#c62f2f;font-weight:400}.end p{margin:18px auto 26px;max-width:460px}.end .btn{background:#0c1a2b;color:#f1ead9}.ct{list-style:none;margin-top:28px;display:flex;gap:8px 26px;flex-wrap:wrap;justify-content:center}.ct a{text-decoration:underline}
footer{padding:20px clamp(18px,4vw,60px) 90px;font-size:12px;opacity:.7}#sticky a{background:#e0b04a;color:#0c1a2b;border-radius:100px}
@media(max-width:820px){.hero{grid-template-columns:1fr;min-height:0}.bagwrap{height:420px}}'''
    cards=svcs(x,lambda i,s:'<div class="rd" data-r><i>Round %d</i><h3>%s</h3><p>%s</p></div>'%(i+1,E(s['title']),E(s['desc'])))
    body='''<div class="ropes" style="margin-top:30px"></div><div class="top"><span>__NAME__</span><span>__SUBURB__</span></div>
<section class="hero" id="top"><div><h1 id="h1">%s</h1><p data-hero>__SUB__</p><a class="btn" data-hero href="__CTA__">__CTALABEL__ %s</a></div>
<div class="bagwrap"><div id="bag">%s</div><div class="bh">Grab it. Hit it. Drag it.</div></div></section>%s
<section class="sec"><h2 class="hd">__SERVTITLE__</h2><div class="grid">%s</div></section>
<section class="end" id="end"><h2 class="hd">%s</h2><p data-r>__CLOSESUB__</p><a class="btn" data-r href="__CTA__">__CTALABEL__ %s</a><ul class="ct">%s<li>%s</li></ul></section><div class="ropes"></div>%s%s'''%(hl(x['headline'],'hl'),ARROW,bag('bg',2.2),mq(x['words']),cards,hl(x['close']),ARROW,''.join('<li>%s</li>'%c for c in contact_lines(x)),E(x['address']),FOOT,STICKY)
    js='''var bag=$('#bag'),a=0,v=0,drag=false,last=0,lt=0,pivot;
function piv(){var r=bag.getBoundingClientRect();return{x:r.left+r.width/2-Math.sin(a)*0,y:bag.parentNode.getBoundingClientRect().top+8}}
function ang(e){var p=piv();return Math.atan2(e.clientX-p.x,Math.max(40,e.clientY-p.y))}
bag.addEventListener('pointerdown',function(e){drag=true;bag.setPointerCapture(e.pointerId);last=ang(e);lt=performance.now();v=0;e.preventDefault()});
addEventListener('pointermove',function(e){if(!drag)return;var n=ang(e),t=performance.now();v=(n-last)/Math.max(.016,(t-lt)/1000);last=n;lt=t;a=Math.max(-1.2,Math.min(1.2,n))});
addEventListener('pointerup',function(){if(drag){drag=false;v=Math.max(-9,Math.min(9,v))}});
bag.addEventListener('click',function(e){if(Math.abs(v)<.5&&Math.abs(a)<.05)v+=(e.clientX<bag.getBoundingClientRect().left+bag.offsetWidth/2?1:-1)*3.5});
gsap.ticker.add(function(){var dt=Math.min(.033,gsap.ticker.deltaRatio()/60);if(!drag){v+=(-26*Math.sin(a)-1.1*v)*dt;a+=v*dt}bag.style.transform='rotate('+(a*57.3)+'deg)'});
setTimeout(function(){if(Math.abs(a)<.01)v=2.6},1600);'''
    return fonts,css,body,js,'#0c1a2b'

# ---------- QUEENSTOWN: alpine + floating weights ----------
def queenstown(x):
    fonts=font('BSD','fonts/bsd.woff','100 900')+font('Manrope','fonts/manrope.woff','200 800')
    css=BASE+'''body{background:#eef6fb;color:#0b2545;font:400 17px/1.65 Manrope,sans-serif}h1,.hd{font-family:BSD,Impact,sans-serif;font-weight:800;text-transform:uppercase;letter-spacing:-.01em}
.sky{position:relative;min-height:100vh;background:linear-gradient(180deg,#8ecdf2 0%,#cfe9f8 55%,#eef6fb 100%);overflow:hidden}
.top{position:relative;z-index:3;display:flex;justify-content:space-between;padding:56px clamp(18px,4vw,60px) 0;font-weight:700;letter-spacing:.12em;text-transform:uppercase;font-size:13px}
.heroc{position:relative;z-index:3;padding:clamp(30px,6vw,80px) clamp(18px,4vw,60px) 0;max-width:980px}h1{font-size:clamp(60px,12vw,200px);line-height:.86}h1 em{font-style:normal;color:#ff7a3d}.heroc p{max-width:480px;margin:20px 0;font-size:19px}
.btn{background:#0b2545;color:#fff;border-radius:100px}.btn:hover{background:#ff7a3d}
#fl{position:absolute;inset:0;z-index:2;pointer-events:none}#fl .it{position:absolute;left:0;top:0;color:#0b2545;opacity:.4;will-change:transform}
.mt{position:absolute;left:0;right:0;bottom:-2px;z-index:1}.mt svg{display:block;width:100%;height:auto}
.fac{padding:70px clamp(18px,4vw,60px)}.fac h2{font-size:clamp(44px,8vw,120px);line-height:.9;margin-bottom:28px}.chips{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px}
.ch{background:#fff;border-radius:22px;padding:26px;box-shadow:0 10px 30px rgba(11,37,69,.08);transition:transform .3s}.ch:hover{transform:translateY(-6px)}.ch h3{font:800 28px/1 BSD;text-transform:uppercase;margin-bottom:6px}.ch p{color:#40597a}.ch svg{width:54px;height:auto;color:#ff7a3d;margin-bottom:12px}
.hrs{margin:10px clamp(18px,4vw,60px) 60px;background:#0b2545;color:#fff;border-radius:28px;padding:clamp(30px,5vw,60px);display:flex;gap:20px;flex-wrap:wrap;justify-content:space-between;align-items:center}.hrs .t{font:800 clamp(60px,12vw,180px)/.9 BSD}.hrs .t span{color:#ff7a3d}.hrs small{display:block;letter-spacing:.14em;text-transform:uppercase;font-weight:700;color:#8ecdf2}
.mq{overflow:hidden;white-space:nowrap;padding:0 0 30px}#mqt{display:inline-block}#mqt span{font:800 clamp(28px,4vw,52px) BSD;text-transform:uppercase;padding:0 22px;color:#8ecdf2}
.end{padding:clamp(60px,9vw,120px) clamp(18px,4vw,60px);background:linear-gradient(180deg,#eef6fb,#8ecdf2);text-align:center}.end h2{font-size:clamp(46px,9vw,150px);line-height:.88}.end p{margin:16px auto 26px;max-width:440px}.ct{list-style:none;margin-top:28px;display:flex;gap:8px 26px;flex-wrap:wrap;justify-content:center;font-weight:600}.ct a{text-decoration:underline}
footer{padding:20px clamp(18px,4vw,60px) 90px;font-size:12px;opacity:.7}#sticky a{background:#ff7a3d;color:#fff;border-radius:100px}'''
    ic=[dumbbell('',2.6),kettle('',2.6),plate('',2.6),dumbbell('',2.6),kettle('',2.6),plate('',2.6),dumbbell('',2.6)]
    chips=svcs(x,lambda i,s:'<div class="ch" data-r>%s<h3>%s</h3><p>%s</p></div>'%(ic[i%7],E(s['title']),E(s['desc'])))
    mt='<svg viewBox="0 0 1440 360" preserveAspectRatio="none"><path id="m1" fill="#b9dcf0" d="M0 260L140 150L230 220L380 90L520 230L650 140L800 250L960 110L1100 230L1250 150L1440 250V360H0Z"/><path id="m2" fill="#6fa7cf" d="M0 300L180 210L300 270L470 170L620 280L780 200L930 290L1100 190L1260 280L1440 220V360H0Z"/><path id="m3" fill="#eef6fb" d="M0 335L200 290L360 325L560 280L760 330L960 285L1180 330L1440 295V360H0Z"/></svg>'
    body='''<section class="sky" id="top"><div class="top"><span>__NAME__</span><span>__SUBURB__</span></div><div id="fl"></div><div class="heroc"><h1 id="h1">%s</h1><p data-hero>__SUB__</p><a class="btn" data-hero href="__CTA__">__CTALABEL__ %s</a></div><div class="mt" id="mt">%s</div></section>%s
<section class="fac"><h2 class="hd">__SERVTITLE__</h2><div class="chips">%s</div></section>
<div class="hrs" data-r><div><small>Open every day</small><div class="t">6<span>:</span>00 &ndash; 21<span>:</span>00</div></div><div><small>Where</small><b>__ADDRESS__</b></div></div>
<section class="end" id="end"><h2 class="hd">%s</h2><p data-r>__CLOSESUB__</p><a class="btn" data-r href="__CTA__">__CTALABEL__ %s</a><ul class="ct">%s</ul></section>%s%s'''%(hl(x['headline']),ARROW,mt,mq(x['words']),chips,hl(x['close']),ARROW,''.join('<li>%s</li>'%c for c in contact_lines(x)),FOOT,STICKY)
    dumb=dumbbell('',3).replace('<svg ','<svg width="110" ');kt=kettle('',3).replace('<svg ','<svg width="60" ');pl=plate('',3).replace('<svg ','<svg width="64" ')
    js='''var fl=$('#fl'),sky=$('.sky'),H=sky.offsetHeight,W=sky.offsetWidth,mx=-999,my=-999,items=[],tp=[%s,%s,%s];
for(var i=0;i<12;i++){var d=document.createElement('div');d.className='it';d.innerHTML=tp[i%%3];fl.appendChild(d);items.push({el:d,x:Math.random()*W,y:Math.random()*H*.75,vx:(Math.random()-.5)*.3,vy:(Math.random()-.5)*.3,r:Math.random()*360,vr:(Math.random()-.5)*.4,ph:Math.random()*6})}
sky.addEventListener('pointermove',function(e){var r=sky.getBoundingClientRect();mx=e.clientX-r.left;my=e.clientY-r.top});sky.addEventListener('pointerleave',function(){mx=my=-999});
addEventListener('resize',function(){H=sky.offsetHeight;W=sky.offsetWidth});
gsap.ticker.add(function(t){items.forEach(function(o){var dx=o.x-mx,dy=o.y-my,d=Math.sqrt(dx*dx+dy*dy)+1;if(d<190){var f=(190-d)/190*1.4;o.vx+=dx/d*f;o.vy+=dy/d*f}o.vx*=.97;o.vy*=.97;o.x+=o.vx+Math.sin(t+o.ph)*.25;o.y+=o.vy+Math.cos(t*.8+o.ph)*.2;o.r+=o.vr+o.vx;if(o.x<-120)o.x=W+60;if(o.x>W+120)o.x=-60;if(o.y<-100)o.y=H*.8;if(o.y>H*.85)o.y=-60;o.el.style.transform='translate3d('+o.x+'px,'+o.y+'px,0) rotate('+o.r+'deg)'})});
gsap.to('#m1',{y:-40,ease:'none',scrollTrigger:{trigger:'.sky',start:'top top',end:'bottom top',scrub:true}});gsap.to('#m2',{y:-18,ease:'none',scrollTrigger:{trigger:'.sky',start:'top top',end:'bottom top',scrub:true}});'''%(json.dumps(dumb),json.dumps(kt),json.dumps(pl))
    return fonts,css,body,js,'#8ecdf2'

# ---------- CORE MMA: reactor ----------
def coremma(x):
    fonts=font('SG','fonts2/sg.woff','300 700')+font('Mono','fonts2/mono.woff','700')
    css=BASE+'''body{background:#05070a;color:#e9f2e0;font:400 16px/1.6 SG,sans-serif}h1,.hd{font-weight:700;letter-spacing:-.045em}.m{font:700 12px Mono;letter-spacing:.16em;text-transform:uppercase;color:#b6ff3b}
.top{display:flex;justify-content:space-between;padding:56px clamp(18px,4vw,56px) 0}
.hero{display:grid;grid-template-columns:1.1fr .9fr;gap:20px;align-items:center;padding:clamp(20px,4vw,50px) clamp(18px,4vw,56px) 50px;min-height:90vh}h1{font-size:clamp(54px,10vw,170px);line-height:.88;text-transform:uppercase}h1 em{font-style:normal;color:#b6ff3b;text-shadow:0 0 40px rgba(182,255,59,.45)}.hero p{max-width:470px;margin:22px 0;font-size:18px;color:#b9c7ad}
.btn{background:#b6ff3b;color:#05070a;clip-path:polygon(12px 0,calc(100% - 12px) 0,100% 12px,100% calc(100% - 12px),calc(100% - 12px) 100%,12px 100%,0 calc(100% - 12px),0 12px);padding:17px 32px}.btn:hover{background:#fff}
.reactor{position:relative;aspect-ratio:1;max-width:560px;margin:auto;width:100%;perspective:900px}.rg{position:absolute;inset:0;transform-style:preserve-3d;transition:transform .15s}
.ring{position:absolute;inset:0;border:2px solid rgba(182,255,59,.7);border-radius:50%;box-shadow:0 0 30px rgba(182,255,59,.25),inset 0 0 30px rgba(182,255,59,.12)}.ring:nth-child(2){inset:12%;border-style:dashed;border-color:rgba(182,255,59,.5)}.ring:nth-child(3){inset:26%;border-width:6px;border-color:rgba(182,255,59,.9)}
.ring:nth-child(4){inset:42%;background:radial-gradient(circle,#eaffc0,#b6ff3b 45%,rgba(182,255,59,0) 72%);border:0;box-shadow:0 0 90px 20px rgba(182,255,59,.55)}
.ring:nth-child(1){animation:sp 24s linear infinite}.ring:nth-child(2){animation:sp 16s linear infinite reverse}.ring:nth-child(3){animation:sp 10s linear infinite}.ring:nth-child(4){animation:pu 2.4s ease-in-out infinite}@keyframes sp{to{transform:rotate(360deg)}}@keyframes pu{50%{transform:scale(1.18)}}
.mq{overflow:hidden;white-space:nowrap;border-block:1px solid #1b2a12;padding:14px 0}#mqt{display:inline-block}#mqt span{font:700 clamp(22px,3vw,38px) SG;letter-spacing:-.03em;text-transform:uppercase;padding:0 26px;color:#b6ff3b}#mqt span:nth-child(even){color:#e9f2e0}
.sec{padding:70px clamp(18px,4vw,56px)}.sec h2{font-size:clamp(38px,7vw,100px);line-height:.92;text-transform:uppercase;margin:8px 0 34px}
.hx{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px}.hc{position:relative;background:#0d130a;padding:34px 28px;clip-path:polygon(24px 0,calc(100% - 24px) 0,100% 24px,100% calc(100% - 24px),calc(100% - 24px) 100%,24px 100%,0 calc(100% - 24px),0 24px);border:1px solid #2a3d19;transition:background .3s,transform .3s}.hc:hover{background:#16230d;transform:translateY(-6px)}.hc i{font:700 13px Mono;font-style:normal;color:#b6ff3b}.hc h3{font:700 28px/1.05 SG;letter-spacing:-.03em;margin:12px 0 8px}.hc p{color:#b9c7ad}
.end{padding:clamp(60px,9vw,120px) clamp(18px,4vw,56px);text-align:center;border-top:1px solid #1b2a12}.end h2{font-size:clamp(46px,9vw,150px);line-height:.88;text-transform:uppercase}.end p{margin:16px auto 26px;max-width:440px;color:#b9c7ad}.ct{list-style:none;margin-top:28px;display:flex;gap:8px 26px;flex-wrap:wrap;justify-content:center}.ct a{text-decoration:underline}
footer{padding:20px clamp(18px,4vw,56px) 90px;font-size:12px;opacity:.6}#sticky a{background:#b6ff3b;color:#05070a}
@media(max-width:820px){.hero{grid-template-columns:1fr;min-height:0}.reactor{max-width:360px}}'''
    cards=svcs(x,lambda i,s:'<div class="hc" data-r><i>0%d</i><h3>%s</h3><p>%s</p></div>'%(i+1,E(s['title']),E(s['desc'])))
    body='''<div class="top m"><span>__NAME__</span><span>__SUBURB__</span></div>
<section class="hero" id="top"><div><h1 id="h1">%s</h1><p data-hero>__SUB__</p><a class="btn" data-hero href="__CTA__">__CTALABEL__ %s</a></div><div class="reactor" id="rx"><div class="rg" id="rg"><div class="ring"></div><div class="ring"></div><div class="ring"></div><div class="ring"></div></div></div></section>%s
<section class="sec"><span class="m">What you get</span><h2 class="hd">__SERVTITLE__</h2><div class="hx">%s</div></section>
<section class="end" id="end"><h2 class="hd">%s</h2><p data-r>__CLOSESUB__</p><a class="btn" data-r href="__CTA__">__CTALABEL__ %s</a><ul class="ct">%s<li>%s</li></ul></section>%s%s'''%(hl(x['headline']),ARROW,mq(x['words']),cards,hl(x['close']),ARROW,''.join('<li>%s</li>'%c for c in contact_lines(x)),E(x['address']),FOOT,STICKY)
    js='''var rg=$('#rg'),rx=$('#rx');addEventListener('pointermove',function(e){var r=rx.getBoundingClientRect(),cx=r.left+r.width/2,cy=r.top+r.height/2;var dx=(e.clientX-cx)/innerWidth,dy=(e.clientY-cy)/innerHeight;rg.style.transform='rotateY('+(dx*50)+'deg) rotateX('+(-dy*50)+'deg)'});
gsap.from('.ring',{scale:.2,opacity:0,duration:1.4,ease:'expo.out',stagger:.12});
$$('.hc').forEach(function(c){c.addEventListener('pointermove',function(e){var r=c.getBoundingClientRect();c.style.background='radial-gradient(260px circle at '+(e.clientX-r.left)+'px '+(e.clientY-r.top)+'px,#1f3310,#0d130a 70%)'});c.addEventListener('pointerleave',function(){c.style.background=''})});'''
    return fonts,css,body,js,'#05070a'

CL=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'new5.json')))
FN={'titan':titan,'strengthco':strengthco,'wboxing':wboxing,'queenstown':queenstown,'coremma':coremma}
if __name__=='__main__':
    out=sys.argv[1]; os.makedirs(out,exist_ok=True)
    for x in CL:
        fonts,css,body,js,theme=FN[x['style']](x)
        h=page(x,fonts,css,body,js,theme)
        d='%s/%s'%(out,x['slug']); os.makedirs(d,exist_ok=True); open(d+'/index.html','w').write(h)
        with zipfile.ZipFile('%s/%s.zip'%(out,x['slug']),'w',zipfile.ZIP_DEFLATED) as z: z.write(d+'/index.html','index.html')
        print(x['slug'],len(h)//1024,'KB')
