import sys,os,json,zipfile,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import build5
from build5 import *
D=os.path.dirname(os.path.abspath(__file__))
N5={x['slug']:x for x in json.load(open(D+'/new5.json'))}
FONTS={'anton':('Anton','fonts2/anton.woff','400'),'bsd':('Anton','fonts/bsd.woff','100 900'),'fraunces':('Anton','fonts2/fraunces.woff','300 900')}
def S(slug,**k):
    b=dict(N5[slug]);b.update(k);return b
CL=[]
def add(**k):
    k.pop('style',None);CL.append(k)
STEPS=[('Say hello','Message the team and tell them what you want to achieve.'),('Come and train','Book a visit or a first session and meet the coaches.'),('Keep going','Build a routine you can stick to, with people who back you.')]
# ---- business configs (facts only from their own public pages)
add(kind='lift',font='anton',bg='#0e0e0f',fg='#ecebe6',ac='#ffd400',on='#0e0e0f',c1='#171718',mut='#bdbcb6',light=False,lc='#ffd400',**N5['strengthco'],
    facts=[('Format','Small-group coaching'),('Block length','8 weeks'),('Where','Christchurch Central')],card=('Coached blocks','Eight weeks.<br>One goal.'),band=('Train. Cook. Eat.',"The members' kitchen runs cooking classes so the food matches the training. Strength is built in the gym and in the kitchen."),steps=STEPS,
    scene=dict(kind='lift',accent='#ffd400',envTop='#eef0f4',envMid='#6b707c',envBot='#0c0d10',exposure=1.2))
add(kind='blueprint',font='bsd',bg='#07101f',fg='#e6f0ff',ac='#7dd3fc',on='#07101f',c1='#0d1a30',mut='#9db4d4',light=False,lc='#2b6fff',layout='b',**N5['titan'],
    facts=[('Disciplines','Muay Thai, kickboxing, MMA, BJJ'),('Where','Sydenham, Christchurch'),('Sessions','Group and private')],card=('Under one roof','Every discipline.<br>One gym.'),band=('Step onto the mats','Message the team to book your first session.'),steps=STEPS,
    scene=dict(kind='blueprint',accent='#7dd3fc',metal=0x9fb8d6,envTop='#9fcbff',envMid='#1c4a7d',envBot='#06142a'))
add(kind='bag',font='anton',bg='#0b0b0d',fg='#f1ede4',ac='#e0b04a',on='#0b0b0d',c1='#17161a',mut='#bfb8a8',light=False,lc='#e0b04a',layout='c',**N5['wboxing'],
    facts=[('Where','Wellington'),('Style','Boxing coaching'),('Level','All levels')],card=('Boxing, properly taught','Hit the bag.<br>Learn the craft.'),band=('Gloves on','Message the gym to ask about the next session.'),steps=STEPS,
    scene=dict(kind='bag',bagTop='WBG',bagSub='BOXING',accent='#e0b04a',envTop='#dfe9ff',envMid='#34445e',envBot='#070d17'))
add(kind='float',font='bsd',bg='#e9f3fa',fg='#10253a',ac='#ff7a3d',on='#ffffff',c1='#ffffff',mut='#4b6378',light=True,lc='#9fd6ff',layout='b',**N5['queenstowngym'],
    facts=[('Where','Queenstown'),('Setting','Alpine town'),('Open to','Locals and visitors')],card=('Train in Queenstown','Lift with a view.<br>Stay strong.'),band=('Come and train','Get in touch to ask about passes and memberships.'),steps=STEPS,
    scene=dict(kind='float',accent='#ff7a3d',envTop='#ffffff',envMid='#8ecdf2',envBot='#2a4d73',exposure=1.0))
add(kind='core',font='anton',bg='#06090a',fg='#e9f5e1',ac='#b6ff3b',on='#06090a',c1='#0f1511',mut='#a9bda0',light=False,lc='#b6ff3b',layout='c',**N5['coremma'],
    facts=[('Where','Hamilton'),('Style','Mixed martial arts'),('Level','All levels')],card=('Fight fit','Build the core.<br>Own the cage.'),band=('Step in','Message the gym to book a first class.'),steps=STEPS,
    scene=dict(kind='core',accent='#b6ff3b'))
add(slug='swet',kind='float',font='anton',bg='#14110f',fg='#f4efe9',ac='#ff4d2e',on='#ffffff',c1='#1e1a17',mut='#c2b8ad',light=False,lc='#ff4d2e',
    name='SWET',suburb='Wellington',headline='Sweat together.',sub='A fully equipped gym in Kaiwharawhara with group classes, personal training and a free one-week trial.',cta_label='Start free week',cta_url='mailto:admin@swet.co.nz',
    words=['Group classes','Personal training','Open gym','8-Week Challenge','Teen academy'],serv_title='Train your way',
    services=[{'title':'Group classes','desc':'High-energy sessions with people who push you.'},{'title':'Personal training','desc':'One-on-one coaching built around your goals.'},{'title':'Open gym','desc':'A fully equipped floor to train on your own schedule.'},{'title':'8-Week Challenge','desc':'A structured challenge to kick-start your results.'},{'title':'Teen High Performance Academy','desc':'Youth sports coaching for the next generation.'}],
    address='22 Kaiwharawhara Road, Wellington 6035',phone='04 472 4750',email='admin@swet.co.nz',close='Start your free week',close_sub='Message the team to claim a free one-week trial.',
    facts=[('Trial','Free one-week trial'),('Memberships','Weekly, monthly, yearly'),('Where','Kaiwharawhara, Wellington')],card=('New here?','Try it free.<br>For a week.'),band=('SWET Open Games','Challenges and events all year, so there is always a reason to show up.'),steps=STEPS,
    scene=dict(kind='float',accent='#ff4d2e',envTop='#fff2ea',envMid='#6a4a3a',envBot='#100a08',exposure=1.1))
add(slug='strengthfactory',kind='lift',font='bsd',bg='#0d0d0d',fg='#efefef',ac='#ff6a00',on='#0d0d0d',c1='#181818',mut='#b9b9b9',light=False,lc='#ff6a00',
    layout='b',name='Strength Factory',suburb='Wellington',headline='Built for lifters.',sub='A strength gym in Mount Cook for powerlifting, weightlifting and strongperson, with 24/7 member access.',cta_label='Join the gym',cta_url='mailto:strengthfactorywgtn@gmail.com',
    words=['Powerlifting','Weightlifting','Strongperson','24/7 access','Conditioning'],serv_title='The floor',
    services=[{'title':'Powerlifting','desc':'Racks and benches set up for heavy squat, bench and deadlift.'},{'title':'Weightlifting','desc':'Olympic platforms, certified by Weightlifting New Zealand.'},{'title':'Strongperson','desc':'Train the odd-object events with proper kit.'},{'title':'Conditioning','desc':'Conditioning to support your other sports.'},{'title':'24/7 access','desc':'Members train when it suits them, with showers on site.'}],
    address='63C Hopper Street, Mount Cook, Wellington 6011',phone='027 738 1010',email='strengthfactorywgtn@gmail.com',close='Load the bar',close_sub='Message the team about memberships.',
    facts=[('Access','24/7 for members'),('Focus','Strength sports'),('Where','Mount Cook, Wellington')],card=('Memberships','Standard.<br>Student. Annual.'),band=('Always open','Members get 24/7 access, so the bar is ready whenever you are.'),steps=STEPS,
    scene=dict(kind='lift',accent='#ff6a00',envTop='#f4efe8',envMid='#6b6258',envBot='#0c0b0a',exposure=1.2))
add(slug='crossfitwhakatane',kind='blueprint',font='anton',bg='#f4f1ea',fg='#111111',ac='#e4262b',on='#ffffff',c1='#ffffff',mut='#55524c',light=True,lc='#e4262b',
    layout='c',name='CrossFit Whakatane',suburb='Whakatāne',headline='Fitter every week.',sub='Small-group CrossFit classes in Whakatāne, scaled to your ability, with open gym sessions.',cta_label='Book a class',cta_url='mailto:info@crossfitwhakatane.co.nz',
    words=['CrossFit','Small groups','Open gym','All abilities'],serv_title='What you get',
    services=[{'title':'CrossFit classes','desc':'Varied workouts in small groups, adjusted to your ability.'},{'title':'Open gym','desc':'Extra sessions to train on your own.'},{'title':'Unlimited classes','desc':'$45 per week for unlimited classes (GST inclusive).'},{'title':'Single class','desc':'$25 for a single class (GST inclusive).'}],
    address='Whakatāne, Eastern Bay of Plenty',phone='',email='info@crossfitwhakatane.co.nz',close='Book your first class',close_sub='Message the team to get started.',
    facts=[('Unlimited','$45 per week'),('Single class','$25'),('Where','Whakatāne')],card=('Simple pricing','Two prices.<br>No fuss.'),band=('All abilities','Every workout can be scaled, so beginners and veterans train side by side.'),steps=STEPS,
    scene=dict(kind='blueprint',accent='#e4262b',metal=0x5b6573,envTop='#ffffff',envMid='#c9ced6',envBot='#2a2f36',exposure=1.0))
add(slug='peachboxing',kind='bag',font='fraunces',bg='#fff1ea',fg='#2a1410',ac='#ff5d7a',on='#ffffff',c1='#ffffff',mut='#7a5a52',light=True,lc='#ff9aa9',
    layout='b',name='Peach Boxing',suburb='Henderson Valley, West Auckland',headline='Fight for it.',sub='Boxing classes and Women\'s Boxfit in Henderson Valley, plus fight nights and youth and workplace sessions.',cta_label='Join a class',cta_url='mailto:alina@peachboxing.co.nz',
    words=['Boxing classes',"Women's Boxfit",'Fight nights','Youth sessions'],serv_title='Classes and more',
    services=[{'title':'Boxing classes','desc':'Learn to box in a supportive, high-energy room.'},{'title':"Women's Boxfit",'desc':'A boxing fitness class, with a concession card available.'},{'title':'Fight nights','desc':'Events where the gym shows what it can do.'},{'title':'Schools and workplaces','desc':'Speaking and training sessions for schools, youth programmes and workplaces.'}],
    address='Henderson Valley, West Auckland',phone='021 202 7584',email='alina@peachboxing.co.nz',close='Gloves on',close_sub='Message the gym to join a class.',
    facts=[('Classes','Boxing and Boxfit'),('Where','Henderson Valley'),('Events','Fight nights')],card=('Come as you are','Boxing for<br>everyone.'),band=('Fight nights','Come and cheer, or get in the ring yourself.'),steps=STEPS,
    scene=dict(kind='bag',bagTop='PEACH',bagSub='BOXING',accent='#ff5d7a',envTop='#fff0ee',envMid='#c98f8f',envBot='#3a1a1f',exposure=1.15))

LAYCSS="""@media(min-width:861px){
.lb .hero .in{grid-template-columns:1fr;gap:20px}.lb .hero .in>div:first-child{max-width:52%}.lb h1{font-size:clamp(50px,7.6vw,124px)}.lb .glbox{left:44%;right:0;width:56%;top:60px}.lb .next{max-width:none;background:none;border:0;backdrop-filter:none;padding:0;justify-self:start}.lb .next h3,.lb .next small{display:none}.lb .next ul{display:flex;gap:34px;margin:0}.lb .next li{border:0;flex-direction:column;align-items:flex-start;padding:0}.lb .next li span{text-align:left;color:var(--w);font-weight:700}
.lb .grid{grid-template-columns:1fr;gap:0}.lb .card{flex-direction:row;align-items:center;min-height:0;padding:26px 8px;border-radius:0;border-width:0 0 1px 0;background:transparent}.lb .card>div{display:flex;align-items:center;gap:30px;flex:1}.lb .card h3{margin:0;font-size:clamp(30px,4.6vw,66px);flex:1;transition:padding .3s,color .3s}.lb .card p{flex:1;max-width:420px}.lb .card:hover h3{color:var(--y);padding-left:18px}.lb .card i{width:70px}
.lb .steps{grid-template-columns:1fr}.lb .step{display:grid;grid-template-columns:140px 1fr 1.3fr;align-items:center;border-right:0;border-bottom:1px solid var(--bd);margin:0;padding:22px 0}.lb .step b{font-size:64px}
.lc .hero{background:linear-gradient(90deg,var(--y) 0 50%,transparent 50%)}.lc .hero .in{grid-template-columns:1fr}.lc .hero .in>div:first-child{max-width:46%;color:var(--on)}.lc h1 em{background:var(--on);color:var(--y)}.lc .hero p{color:inherit;opacity:.8}.lc .hero .btn{background:var(--on);color:var(--y)}.lc .hero .btn.o{background:transparent;color:var(--on);border-color:var(--on)}
.lc .glbox{left:50%;right:0;width:50%}.lc .next{position:absolute;right:clamp(16px,4vw,48px);bottom:110px}.lc .mq{background:var(--on);color:var(--y)}
.lc .grid{grid-template-columns:repeat(2,1fr);gap:0}.lc .card{border-radius:0;min-height:210px;border-width:0 1px 1px 0}.lc .steps{grid-template-columns:1fr}.lc .step{display:grid;grid-template-columns:150px 1fr 1.2fr;align-items:center;border-right:0;border-bottom:1px solid var(--bd);margin:0;padding:22px 0}.lc .step b{font-size:70px}.lc .sec h2{max-width:none}}
"""

PRESETS={
 'charcoal-yellow':dict(bg='#0e0e0f',fg='#ecebe6',ac='#ffd400',on='#0e0e0f',c1='#171718',mut='#bdbcb6',light=False,lc='#ffd400'),
 'navy-sky':dict(bg='#07101f',fg='#e6f0ff',ac='#7dd3fc',on='#07101f',c1='#0d1a30',mut='#9db4d4',light=False,lc='#2b6fff'),
 'black-gold':dict(bg='#0b0b0d',fg='#f1ede4',ac='#e0b04a',on='#0b0b0d',c1='#17161a',mut='#bfb8a8',light=False,lc='#e0b04a'),
 'ice-orange':dict(bg='#e9f3fa',fg='#10253a',ac='#ff7a3d',on='#ffffff',c1='#ffffff',mut='#4b6378',light=True,lc='#9fd6ff'),
 'void-green':dict(bg='#06090a',fg='#e9f5e1',ac='#b6ff3b',on='#06090a',c1='#0f1511',mut='#a9bda0',light=False,lc='#b6ff3b'),
 'warm-red':dict(bg='#14110f',fg='#f4efe9',ac='#ff4d2e',on='#ffffff',c1='#1e1a17',mut='#c2b8ad',light=False,lc='#ff4d2e'),
 'cream-red':dict(bg='#f4f1ea',fg='#111111',ac='#e4262b',on='#ffffff',c1='#ffffff',mut='#55524c',light=True,lc='#e4262b'),
 'blush-pink':dict(bg='#fff1ea',fg='#2a1410',ac='#ff5d7a',on='#ffffff',c1='#ffffff',mut='#7a5a52',light=True,lc='#ff9aa9'),
 'forest-lime':dict(bg='#0c1a14',fg='#eaf5ec',ac='#c6f24a',on='#0c1a14',c1='#13261d',mut='#a7bfae',light=False,lc='#3fbf7a'),
 'violet-hot':dict(bg='#100a1c',fg='#f1eaff',ac='#ff3df0',on='#100a1c',c1='#1a1230',mut='#b9a8d9',light=False,lc='#8a4dff'),
 'espresso-latte':dict(bg='#17100b',fg='#f6ece0',ac='#d99a5b',on='#17100b',c1='#241812',mut='#c4b09c',light=False,lc='#d99a5b'),
 'sand-teal':dict(bg='#f3ece0',fg='#16302f',ac='#0f8b8d',on='#ffffff',c1='#ffffff',mut='#5d6d68',light=True,lc='#7fd0cf'),
}
SCENES={
 'lift':dict(kind='lift',envTop='#eef0f4',envMid='#6b707c',envBot='#0c0d10',exposure=1.2),
 'blueprint':dict(kind='blueprint',metal=0x9fb8d6,envTop='#9fcbff',envMid='#1c4a7d',envBot='#06142a'),
 'bag':dict(kind='bag',bagTop='GYM',bagSub='BOXING',envTop='#dfe9ff',envMid='#34445e',envBot='#070d17'),
 'float':dict(kind='float',envTop='#ffffff',envMid='#8ecdf2',envBot='#2a4d73',exposure=1.0),
 'core':dict(kind='core'),
 'none':dict(kind='none'),
 'rings':dict(kind='rings',envTop='#e8f2ff',envMid='#3b5f8f',envBot='#08152b',exposure=1.1),
 'tramp':dict(kind='tramp',envTop='#ffffff',envMid='#c9ced6',envBot='#3a3f48',exposure=1.0),
 'stones':dict(kind='stones',envTop='#e9f7ee',envMid='#4c7a63',envBot='#0b1d16',exposure=1.0),
 'lotus':dict(kind='lotus',envTop='#ffffff',envMid='#a8d5e8',envBot='#2c5a6b',exposure=1.1),
 'shoe':dict(kind='shoe',envTop='#fff4dd',envMid='#8a6a3a',envBot='#0e0a05',exposure=1.15),
 'ribbon':dict(kind='ribbon',envTop='#f1e4ff',envMid='#5a3b8f',envBot='#0b0716',exposure=1.1),
 'mirrorball':dict(kind='mirrorball',envTop='#ffffff',envMid='#d79bb0',envBot='#3a1a28',exposure=1.2),
 'cafe':dict(kind='cafe',envTop='#fff3e0',envMid='#9a6a43',envBot='#1a0e07',exposure=1.15),
 'ballerina':dict(kind='ballerina',envTop='#ffffff',envMid='#9fcfcc',envBot='#244a49',exposure=1.1),
}
def from_json(d):
    x=dict(PRESETS[d.get('preset','charcoal-yellow')]);x.update(d)
    sc=dict(SCENES[x['kind']]);sc.update(x.get('scene',{}));sc['accent']=x['ac'];x['scene']=sc
    x.setdefault('font','anton');x.setdefault('steps',STEPS);x.setdefault('layout','a')
    return x
def css_for(x):
    L=x['light'];bd='rgba(0,0,0,.12)' if L else 'rgba(255,255,255,.14)'
    disp="font-family:Anton,Impact,sans-serif;font-weight:400;text-transform:uppercase" if x['font']!='fraunces' else "font-family:Anton,Georgia,serif;font-weight:700;text-transform:none;letter-spacing:-.02em"
    return '''
:root{--k:%(bg)s;--w:%(fg)s;--y:%(ac)s;--on:%(on)s;--c1:%(c1)s;--mut:%(mut)s;--bd:%(bd)s}
body{background:var(--k);color:var(--w);font:400 17px/1.6 SG,sans-serif}
h1,h2,h3,.big,.kg,.logo,.pg li,.step b,.mq span{%(disp)s}
.nav{position:fixed;top:34px;left:0;right:0;z-index:60;display:flex;justify-content:space-between;align-items:center;padding:14px clamp(16px,4vw,48px);background:linear-gradient(var(--k),transparent);backdrop-filter:blur(6px)}
.logo{font-size:24px;letter-spacing:.03em}.nav nav{display:flex;gap:28px;font:700 12px SG;letter-spacing:.14em;text-transform:uppercase}.nav nav a{opacity:.7}.nav nav a:hover{opacity:1;color:var(--y)}
.btn{display:inline-flex;align-items:center;gap:10px;background:var(--y);color:var(--on);font:700 13px SG;letter-spacing:.12em;text-transform:uppercase;padding:17px 26px;border-radius:999px;transition:transform .25s}.btn:hover{transform:translateY(-2px)}
.btn.o{background:transparent;color:var(--w);border:1.5px solid var(--bd)}.btn.o:hover{border-color:var(--y);color:var(--y)}
.hero{position:relative;min-height:100svh;display:grid;align-content:end;padding:130px clamp(16px,4vw,48px) 30px;overflow:hidden}
.hero .in{position:relative;z-index:3;display:grid;grid-template-columns:1.5fr 1fr;gap:30px;align-items:end}
h1{font-size:clamp(54px,9vw,150px);line-height:.9}h1 em{font-style:normal;color:var(--on);background:var(--y);padding:0 .1em;display:inline-block;transform:rotate(-1.5deg)}
.hero p{max-width:480px;margin:24px 0 28px;font-size:19px;color:var(--mut)}.row{display:flex;gap:12px;flex-wrap:wrap}
.next{background:color-mix(in srgb,var(--c1) 70%%,transparent);border:1px solid var(--bd);backdrop-filter:blur(14px);border-radius:22px;padding:26px;max-width:360px;justify-self:end}
.next small{font:700 11px SG;letter-spacing:.18em;text-transform:uppercase;color:var(--y)}.next h3{font-size:40px;line-height:1;margin:10px 0 8px}.next ul{list-style:none;margin-top:14px;font-size:15px}.next li{display:flex;justify-content:space-between;gap:12px;padding:10px 0;border-top:1px solid var(--bd)}.next li span{color:var(--mut);text-align:right}
.hero>.glbox{position:absolute!important;right:0;top:70px;bottom:90px;width:56%%;z-index:2}.glbox .gl{position:absolute;inset:0}.hero>#heromount{position:absolute!important;inset:0;z-index:0}
.mq{position:relative;z-index:3;overflow:hidden;white-space:nowrap;background:var(--y);color:var(--on);padding:12px 0;margin-top:40px;transform:rotate(-1deg) scale(1.02)}#mqt{display:inline-block}#mqt span{font-size:clamp(22px,3vw,40px);padding:0 22px}
.lift{height:420vh;position:relative}.stick{position:sticky;top:0;height:100svh;overflow:hidden;display:grid;grid-template-columns:minmax(280px,.9fr) 1.4fr;align-items:center;gap:20px;padding:0 clamp(16px,4vw,48px)}
.sl{position:relative;z-index:2;padding-top:60px}.sl small{font:700 12px SG;letter-spacing:.18em;text-transform:uppercase;color:var(--y)}
.kg{font-size:clamp(90px,12vw,190px);line-height:.9;margin:8px 0 18px}.kg i{font-style:normal;font-size:.3em;color:var(--mut);margin-left:8px}
.pg{list-style:none}.pg li{display:flex;gap:16px;align-items:baseline;padding:13px 0;border-top:1px solid var(--bd);font-size:clamp(22px,2.6vw,36px);color:var(--mut);opacity:.5;transition:all .4s}.pg li span{font:700 12px SG;letter-spacing:.12em}.pg li.on{color:var(--w);opacity:1;padding-left:12px}.pg li.on span{color:var(--y)}
.stick .gl{position:relative;z-index:2;height:min(78vh,720px);width:100%%;touch-action:pan-y;cursor:grab}
.fb{display:none;position:relative;z-index:2;align-items:center;justify-content:center;gap:6px}.lp{width:20px;border-radius:5px;background:var(--c);height:var(--h);transform:scaleY(0);transition:transform .5s cubic-bezier(.2,.9,.2,1.2)}.lp.on{transform:none}.stick.ok .fb{display:none!important}
.hint{position:absolute;bottom:84px;left:50%%;transform:translateX(-50%%);z-index:3;font:700 11px SG;letter-spacing:.2em;text-transform:uppercase;color:var(--mut);white-space:nowrap}
.sec{padding:clamp(80px,11vw,150px) clamp(16px,4vw,48px)}.sec h2{font-size:clamp(48px,8vw,130px);line-height:.9;max-width:14ch}.sec .lead{max-width:520px;color:var(--mut);margin:20px 0 50px}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.card{position:relative;background:var(--c1);border:1px solid var(--bd);border-radius:20px;padding:30px;min-height:250px;display:flex;flex-direction:column;justify-content:space-between;overflow:hidden;transition:border-color .3s}.card:hover{border-color:var(--y)}
.card i{font:700 14px SG;font-style:normal;color:var(--y);letter-spacing:.1em}.card h3{font-size:clamp(28px,3.2vw,46px);line-height:1;margin:40px 0 10px}.card p{color:var(--mut);font-size:16px}
.steps{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--bd)}.step{padding:34px 28px 10px 0;border-right:1px solid var(--bd);margin-right:28px}.step:last-child{border:0}.step b{font-size:84px;line-height:1;color:var(--y);display:block}.step h3{font-size:30px;margin:6px 0}.step p{color:var(--mut)}
.kit{margin:0 clamp(16px,4vw,48px);border-radius:28px;background:var(--y);color:var(--on);padding:clamp(36px,6vw,90px);display:grid;grid-template-columns:1.2fr 1fr;gap:30px;align-items:center}.kit h2{font-size:clamp(42px,6.2vw,96px);line-height:.92}.kit p{font-size:19px;max-width:420px}
.end{padding:clamp(80px,12vw,170px) clamp(16px,4vw,48px) 60px}.end .big{font-size:clamp(56px,13vw,220px);line-height:.86}.end p{max-width:480px;margin:22px 0 28px;color:var(--mut)}
.ct{display:flex;gap:30px;flex-wrap:wrap;margin-top:50px;padding-top:26px;border-top:1px solid var(--bd);font-weight:700}.ct a{color:var(--y)}.ct small{display:block;color:var(--mut);font:700 11px SG;letter-spacing:.16em;text-transform:uppercase}
footer{padding:20px clamp(16px,4vw,48px) 100px;font-size:12px;color:var(--mut)}
#sticky{position:fixed;left:50%%;width:min(340px,calc(100%% - 24px));margin-left:calc(min(340px,calc(100%% - 24px))/-2);bottom:12px;z-index:50;transform:translateY(140%%);transition:transform .4s}#sticky.on{transform:none}#sticky a{display:flex;justify-content:center;padding:16px;border-radius:999px;background:var(--y);color:var(--on);font:700 13px SG;letter-spacing:.12em;text-transform:uppercase;box-shadow:0 10px 30px rgba(0,0,0,.35)}
[data-hero],[data-r]{opacity:0}html:not(.js) [data-hero],html:not(.js) [data-r]{opacity:1}
@media(max-width:860px){.nav nav{display:none}.hero .in,.stick,.kit{grid-template-columns:1fr}.next{justify-self:start}.grid,.steps{grid-template-columns:1fr}.step{border-right:0;border-bottom:1px solid var(--bd);margin:0}
.glbox{display:none}.gl{display:none}.stick{align-content:center}.fb,.stick.ok .fb{display:flex!important;height:150px}.lift{height:380vh}.sl{padding-top:70px}.kg{font-size:90px}.pg li{padding:9px 0;font-size:22px}}
'''%dict(x,bd=bd,disp=disp)
def build_one(x,out):
    f=FONTS[x['font']]
    fonts=font('Anton',f[1],f[2])+font('SG','fonts2/sg.woff','300 700')
    progs=x['services'];kind=x['kind']
    cards=''.join('<div class="card" data-r><i>%02d</i><div><h3>%s</h3><p>%s</p></div></div>'%(i+1,E(s['title']),E(s['desc'])) for i,s in enumerate(progs))
    n=len(progs)+1
    cards+='<div class="card" data-r style="background:var(--y);color:var(--on)"><i style="color:var(--on)">%02d</i><div><h3>Start here</h3><p style="color:inherit;opacity:.85">Not sure where to begin? Message the team and they will point you the right way.</p><a class="btn" style="background:var(--on);color:var(--y);margin-top:18px" href="__CTA__">Get in touch</a></div></div>'%n
    facts=''.join('<li>%s<span>%s</span></li>'%(E(a),E(b)) for a,b in x['facts'])
    steps=''.join('<div class="step" data-r><b>%02d</b><h3>%s</h3><p>%s</p></div>'%(i+1,E(a),E(b)) for i,(a,b) in enumerate(x['steps']))
    hl=x['headline'];parts=hl.split(' ');hh=' '.join(parts[:-1])+' <em>'+parts[-1]+'</em>' if len(parts)>1 else '<em>'+hl+'</em>'
    plates=[(25,'#d6322f',230),(20,'#2a5fd0',200),(15,'#f2c500',172),(10,'#2e9b4a',146),(5,'#f4f4f4',116),(2.5,'#222',88)]
    fb=''.join('<div class="lp" style="--c:%s;--h:%dpx"></div>'%(c,h) for w,c,h in plates)
    pg=''.join('<li><span>%02d</span>%s</li>'%(i+1,E(s['title'])) for i,s in enumerate(progs[:6]))
    nav='<header class="nav"><a class="logo" href="#top">%s</a><nav><a href="#prog">%s</a><a href="#how">How it works</a><a href="#kitchen">More</a><a href="#end">Contact</a></nav><a class="btn" href="__CTA__">__CTALABEL__</a></header>'%(E(x['name']),E(x['serv_title']))
    right='<div class="glbox"><div id="gl" class="gl"></div></div>' if kind not in ('lift','none') else ''
    nextcard='<aside class="next" data-hero><small>%s</small><h3>%s</h3><ul>%s</ul></aside>'%(E(x['card'][0]),x['card'][1],facts)
    hero='<section class="hero" id="top"><div id="heromount"></div>%s<div class="in"><div><h1 id="h1">%s</h1><p data-hero>__SUB__</p><div class="row" data-hero><a class="btn" href="__CTA__">__CTALABEL__ %s</a><a class="btn o" href="#prog">See more</a></div></div>%s</div><div class="mq"><div id="mqt"></div></div></section>'%(right,hh,ARROW,nextcard)
    loader=''
    if kind=='lift':
        loader='<section class="lift" id="lift"><div class="stick" id="stick"><div id="lcmount" style="position:absolute;inset:0;z-index:0"></div><div class="sl"><small>Build your block</small><div class="kg"><span id="kg">20</span><i>KG</i></div><ul class="pg" id="pg">%s</ul></div><div id="gl" class="gl"></div><div class="fb"><div style="display:flex;gap:6px;align-items:center">%s</div></div><div class="hint">Scroll to load the bar &middot; drag to spin it</div></div></section>'%(pg,fb)
    body=nav+hero+loader+'''<section class="sec" id="prog"><h2 class="hd">__SERVTITLE__</h2><div class="grid" style="margin-top:50px">'''+cards+'''</div></section>
<section class="sec" id="how" style="padding-top:0"><h2 class="hd">How it works</h2><div class="steps" style="margin-top:50px">'''+steps+'''</div></section>
<section class="kit" id="kitchen"><div><h2 class="hd">'''+E(x['band'][0])+'''</h2></div><div data-r><p>'''+E(x['band'][1])+'''</p></div></section>
<section class="end" id="end"><div class="big hd">__CLOSE__</div><p data-r>__CLOSESUB__</p><a class="btn" data-r href="__CTA__">__CTALABEL__ '''+ARROW+'''</a><div class="ct" data-r><div><small>Visit</small>__ADDRESS__</div>'''+('<div><small>Call</small><a href="tel:%s">%s</a></div>'%(re.sub(r'[^0-9+]','',x['phone']),E(x['phone'])) if x.get('phone') else '')+'''<div><small>Email</small><a href="mailto:'''+E(x['email'])+'">'+E(x['email'])+'''</a></div></div></section>
<footer>Concept preview built by Manu. Not live and not affiliated with '''+E(x['name'])+'''.</footer><div id="sticky"><a href="__CTA__">__CTALABEL__</a></div>'''
    js="document.getElementById('mqt').innerHTML=__WORDS__.concat(__WORDS__,__WORDS__,__WORDS__).map(function(w){return '<span>'+w+' &#9679;</span>'}).join('');"
    if kind=='lift':
        js+='''var pgl=$$('#pg li'),lp=$$('.lp'),kgv=$('#kg'),W=[25,20,15,10,5,2.5];
ScrollTrigger.create({trigger:'#lift',start:'top top',end:'bottom bottom',scrub:true,onUpdate:function(s){var n=Math.min(6,Math.floor(s.progress*7)),t=20;for(var i=0;i<n;i++)t+=W[i]*2;kgv.textContent=t;pgl.forEach(function(l,i){l.classList.toggle('on',i<n&&i===n-1)});lp.forEach(function(p,i){p.classList.toggle('on',i<n)});window.__lift&&window.__lift(n)}});'''
    js+="gsap.from('.nav',{y:-40,opacity:0,duration:1,ease:'power3.out',delay:.3});"
    css=css_for(x)+LAYCSS+EXTRA_CSS.replace('.heroc{z-index:3!important}','')+'.lcbg{position:absolute;inset:0}'
    t=page(x,fonts,css,body,js,x['bg']).replace('<body>','<body class="l%s">'%x.get('layout','a'),1)
    c=x['lc']
    lcs='''<script>(function(){function mk(sel,col,lco,amp){var t=document.querySelector(sel);if(!t)return;var d=document.createElement('div');d.className='lcbg';d.style.opacity=lco;t.insertBefore(d,t.firstChild);try{initLiquidChrome(d,{color:col,speed:.14,amplitude:amp,frequencyX:3,frequencyY:3,detail:4,roughness:.3,interactive:true,maxDevicePixelRatio:1.1})}catch(e){}}
var fine=matchMedia('(hover:hover) and (pointer:fine)').matches;function go(){mk('#heromount','%s',%s,.22);mk('#lcmount','%s',.2,.2)}
if(!fine){['#heromount','#lcmount'].forEach(function(s){var t=document.querySelector(s);if(t)t.style.background='radial-gradient(60%% 60%% at 75%% 25%%,%s55,transparent)'});return}
if(document.readyState==='complete')setTimeout(go,300);else addEventListener('load',function(){setTimeout(go,300)})})();</script>'''%(c,'.18' if x['light'] else '.32',c,c)
    scripts=('<script>%s</script>%s<script>window.__SCENE=%s</script>%s<script type="module">%s</script><script>%s</script>'%(LC,lcs,json.dumps(x['scene']),IMP,ENG.replace('</script','<\\/script'),FX)) if kind!='none' else '<script>%s</script>%s<script>%s</script>'%(LC,lcs,FX)
    t=t.replace('</body>',scripts+'</body>')
    d=out+'/'+x['slug'];os.makedirs(d,exist_ok=True);open(d+'/index.html','w').write(t)
    print(x['slug'],len(t)//1024,'KB')
if __name__=='__main__':
    out=sys.argv[1];only=sys.argv[2:]
    if only and only[0]=='--json':
        for d in json.load(open(only[1])): build_one(from_json(d),out)
        sys.exit(0)
    for x in CL:
        if not only or x['slug'] in only: build_one(x,out)
