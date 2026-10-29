import base64,html,json,re,os
E=html.escape
V=os.path.dirname(os.path.abspath(__file__))+'/..'
def b64(f): return base64.b64encode(open(f,'rb').read()).decode()
def font(name,file,weight='100 900'):
    return '@font-face{font-family:"%s";src:url(data:font/woff;base64,%s) format("woff");font-weight:%s;font-display:swap}'%(name,b64(V+'/'+file),weight)
def libs():
    r=lambda f:open(V+'/lib/'+f).read().replace('</script','<\\/script')
    return ''.join('<script>%s</script>'%r(f) for f in ('lenis.min.js','gsap.min.js','ScrollTrigger.min.js','SplitText.min.js'))
ARROW='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" width="18" height="18"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
def contact_lines(x):
    out=[]
    if x.get('phone'): out.append('<a href="tel:%s">%s</a>'%(re.sub(r'[^0-9+]','',x['phone']),E(x['phone'])))
    if x.get('email'): out.append('<a href="mailto:%s">%s</a>'%(E(x['email']),E(x['email'])))
    return out
HEAD='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="robots" content="noindex"><meta name="theme-color" content="__THEME__"><title>__NAME__ | Website concept</title>
<script>(function(){var d=document.documentElement;if(!matchMedia('(prefers-reduced-motion:reduce)').matches)d.classList.add('js')})();</script><style>__FONTS__
*{box-sizing:border-box;margin:0;padding:0}html.lenis,html.lenis body{height:auto}.lenis.lenis-smooth{scroll-behavior:auto!important}.lenis.lenis-stopped{overflow:hidden}
body{-webkit-font-smoothing:antialiased;overflow-x:hidden}a{color:inherit;text-decoration:none}img{display:block;max-width:100%}
.concept{position:fixed;z-index:80;top:0;left:0;right:0;text-align:center;font:700 12px/1 system-ui,sans-serif;letter-spacing:.06em;padding:9px 12px;background:#fff;color:#111}
:focus-visible{outline:3px solid currentColor;outline-offset:3px}
__CSS__
@media(prefers-reduced-motion:reduce){*{scroll-behavior:auto!important}}</style></head><body>
<div class="concept">Concept preview only. Not live and not affiliated.</div>
__BODY__
__LIBS__
<script>
(function(){var root=document.documentElement,$=function(s,c){return(c||document).querySelector(s)},$$=function(s,c){return Array.prototype.slice.call((c||document).querySelectorAll(s))};
var animated=root.classList.contains('js')&&window.gsap&&window.ScrollTrigger&&window.SplitText&&window.Lenis;if(!animated)root.classList.remove('js');
var sticky=$('#sticky'),hero=$('#top'),fin=$('#end');
if(sticky&&'IntersectionObserver' in window){var hi=true,fi=false,sy=function(){var on=!hi&&!fi;sticky.classList.toggle('on',on);var a=$('a',sticky);if(a)a.tabIndex=on?0:-1};
new IntersectionObserver(function(e){hi=e[0].isIntersecting;sy()},{threshold:.05}).observe(hero);new IntersectionObserver(function(e){fi=e[0].isIntersecting;sy()},{threshold:.15}).observe(fin)}
if(!animated)return;
gsap.registerPlugin(ScrollTrigger,SplitText);var lenis=new Lenis({lerp:.1});lenis.on('scroll',ScrollTrigger.update);gsap.ticker.add(function(t){lenis.raf(t*1000)});gsap.ticker.lagSmoothing(0);
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href^="#"]');if(!a)return;var h=a.getAttribute('href');var t=h==='#top'?0:$(h);if(t!==null&&t!==undefined){e.preventDefault();lenis.scrollTo(t,{duration:1.4,offset:-20})}});
var sp=SplitText.create('#h1',{type:'lines,words',mask:'lines'});gsap.set('[data-hero]',{y:20});
gsap.timeline({delay:.15}).from(sp.words,{yPercent:115,rotate:3,duration:1.1,ease:'expo.out',stagger:.07}).to('[data-hero]',{opacity:1,y:0,duration:.9,ease:'power3.out',stagger:.12},'-=.7');
gsap.utils.toArray('[data-r]').forEach(function(el){gsap.to(el,{opacity:1,y:0,duration:1,ease:'power3.out',scrollTrigger:{trigger:el,start:'top 90%',once:true}})});
$$('h2.hd').forEach(function(h){SplitText.create(h,{type:'lines',mask:'lines',autoSplit:true,onSplit:function(s){return gsap.from(s.lines,{yPercent:105,duration:1,ease:'expo.out',stagger:.08,scrollTrigger:{trigger:h,start:'top 90%',once:true}})}})});
var mq=$('#mqt');if(mq){var mx=0,dir=-1,half=function(){return mq.scrollWidth/2};var hw=half();addEventListener('resize',function(){hw=half()});
gsap.ticker.add(function(){var v=lenis.velocity||0;if(v)dir=v>0?-1:1;mx+=dir*(.8+Math.min(Math.abs(v)*.5,28));if(hw>0)mx=((mx%hw)-hw)%hw;mq.style.transform='translate3d('+mx+'px,0,0)'})}
__JS__
addEventListener('load',function(){ScrollTrigger.refresh()});
})();
</script></body></html>'''
def page(x,fonts,css,body,js,theme):
    t=HEAD
    for k,v in (('__FONTS__',fonts),('__CSS__',css),('__BODY__',body),('__JS__',js),('__LIBS__',libs()),('__THEME__',theme)):
        t=t.replace(k,v)
    reps={'__NAME__':E(x['name']),'__SUBURB__':E(x['suburb']),'__HEADLINE__':E(x['headline']),'__SUB__':E(x['sub']),'__CTA__':E(x['cta_url']),'__CTALABEL__':E(x['cta_label']),
          '__CLOSE__':E(x['close']),'__CLOSESUB__':E(x.get('close_sub','')),'__GIANT__':E(x.get('giant',x['name'].split()[0])),'__WORDS__':json.dumps(x['words']),
          '__ADDRESS__':E(x.get('address','')),'__SERVTITLE__':E(x.get('serv_title','What we do'))}
    for k in sorted(reps,key=len,reverse=True): t=t.replace(k,reps[k])
    return t
