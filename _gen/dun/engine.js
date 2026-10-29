import * as THREE from 'three';
const C=window.__SCENE||{};await new Promise(function(r){document.readyState==='complete'?r():addEventListener('load',r)});await new Promise(function(r){window.requestIdleCallback?requestIdleCallback(r,{timeout:1200}):setTimeout(r,300)});const touch=!matchMedia('(hover:hover) and (pointer:fine)').matches;const host=document.getElementById('gl');
if(!host||matchMedia('(prefers-reduced-motion:reduce)').matches)throw new Error('skip');
const renderer=new THREE.WebGLRenderer({antialias:true,alpha:true,powerPreference:'high-performance'});
renderer.setPixelRatio(Math.min(devicePixelRatio,touch?1.25:1.6));renderer.outputColorSpace=THREE.SRGBColorSpace;renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=C.exposure||1.15;
host.appendChild(renderer.domElement);renderer.domElement.style.cssText='width:100%;height:100%;display:block';
const scene=new THREE.Scene(),camera=new THREE.PerspectiveCamera(C.fov||34,1,.1,100);
(function(){const c=document.createElement('canvas');c.width=1024;c.height=512;const g=c.getContext('2d'),gr=g.createLinearGradient(0,0,0,512);gr.addColorStop(0,C.envTop||'#dbe9ff');gr.addColorStop(.55,C.envMid||'#51627f');gr.addColorStop(1,C.envBot||'#0b0f18');g.fillStyle=gr;g.fillRect(0,0,1024,512);g.fillStyle='#fff';[[100,110,220,56],[520,80,280,46],[850,150,150,70],[330,230,120,30]].forEach(function(r){g.fillRect(r[0],r[1],r[2],r[3])});const t=new THREE.CanvasTexture(c);t.mapping=THREE.EquirectangularReflectionMapping;t.colorSpace=THREE.SRGBColorSpace;scene.environment=new THREE.PMREMGenerator(renderer).fromEquirectangular(t).texture})();
const key=new THREE.DirectionalLight(0xffffff,2.2);key.position.set(3,5,6);scene.add(key);
const rim=new THREE.DirectionalLight(new THREE.Color(C.accent||'#7dd3fc'),3);rim.position.set(-5,2,-4);scene.add(rim);scene.add(new THREE.AmbientLight(0xffffff,.35));
const accent=new THREE.Color(C.accent||'#7dd3fc');
const M=function(o){return new THREE.MeshStandardMaterial(o)};
const steel=M({color:C.metal||0xc3cad6,metalness:1,roughness:.26}),dark=M({color:0x16181d,metalness:.85,roughness:.38});

function tex(w,h,fn){const c=document.createElement('canvas');c.width=w;c.height=h;fn(c.getContext('2d'),w,h);const t=new THREE.CanvasTexture(c);t.colorSpace=THREE.SRGBColorSpace;t.anisotropy=4;return t}
const knurl=(function(){const t=tex(64,64,function(g,w,h){g.fillStyle='#808080';g.fillRect(0,0,w,h);g.strokeStyle='#fff';g.lineWidth=3;for(let i=-h;i<w+h;i+=8){g.beginPath();g.moveTo(i,0);g.lineTo(i+h,h);g.stroke();g.beginPath();g.moveTo(i+h,0);g.lineTo(i,h);g.stroke()}});t.colorSpace=THREE.NoColorSpace;t.wrapS=t.wrapT=THREE.RepeatWrapping;t.repeat.set(8,18);return t})();
const steelK=M({color:C.metal||0xc3cad6,metalness:1,roughness:.3,bumpMap:knurl,bumpScale:1.2});
function label(txt,sub,col){return tex(256,256,function(g,w,h){g.clearRect(0,0,w,h);g.fillStyle=col||'#fff';g.textAlign='center';g.font='800 120px Arial,Helvetica,sans-serif';g.fillText(txt,128,sub?126:150);if(sub){g.font='700 54px Arial,Helvetica,sans-serif';g.fillText(sub,128,192)}})}
function decal(t,r){return new THREE.Mesh(new THREE.CircleGeometry(r,48),new THREE.MeshBasicMaterial({map:t,transparent:true,depthWrite:false,toneMapped:false}))}
function hexGeo(r,t){const sh=new THREE.Shape();for(let i=0;i<6;i++){const a=i*Math.PI/3,x=Math.cos(a)*r,y=Math.sin(a)*r;i?sh.lineTo(x,y):sh.moveTo(x,y)}sh.closePath();const g=new THREE.ExtrudeGeometry(sh,{depth:t,bevelEnabled:true,bevelSize:.06,bevelThickness:.06,bevelSegments:4});g.translate(0,0,-t/2);return g}

const rubTex=tex(256,256,function(g,w,h){g.fillStyle='#808080';g.fillRect(0,0,w,h);for(let i=0;i<5000;i++){g.fillStyle='rgba('+(Math.random()>.5?'255,255,255':'0,0,0')+',.10)';g.fillRect(Math.random()*w,Math.random()*h,2,2)}});rubTex.colorSpace=THREE.NoColorSpace;rubTex.wrapS=rubTex.wrapT=THREE.RepeatWrapping;
function plateGrp(r,t,col,txt,tc){const g=new THREE.Group();g.add(new THREE.Mesh(plateGeo(r,t),M({color:0x141416,roughness:.78,metalness:.15,bumpMap:rubTex,bumpScale:.6})));
const cm=M({color:col,roughness:.3,metalness:.25}),sm=M({color:0xd5dae3,metalness:1,roughness:.22});
const rim=new THREE.Mesh(new THREE.TorusGeometry(r-.01,.045,14,120),cm);g.add(rim);
[1,-1].forEach(function(f){const z=f*(t/2+.044);
const ring=new THREE.Mesh(new THREE.RingGeometry(r*.8,r*.95,120),cm);ring.position.z=z;if(f<0)ring.rotation.y=Math.PI;g.add(ring);
const gr=new THREE.Mesh(new THREE.RingGeometry(r*.5,r*.525,100),sm);gr.position.z=z;if(f<0)gr.rotation.y=Math.PI;g.add(gr);
const gr2=new THREE.Mesh(new THREE.RingGeometry(r*.66,r*.675,100),sm);gr2.position.z=z;if(f<0)gr2.rotation.y=Math.PI;g.add(gr2);
const hub=new THREE.Mesh(new THREE.RingGeometry(.2,.5,64),sm);hub.position.z=z;if(f<0)hub.rotation.y=Math.PI;g.add(hub);
for(let i=0;i<8;i++){const a=i/8*Math.PI*2,b=new THREE.Mesh(new THREE.CylinderGeometry(.03,.03,.02,12),sm);b.rotation.x=Math.PI/2;b.position.set(Math.cos(a)*.37,Math.sin(a)*.37,z+f*.008);g.add(b)}
const d=decal(label(txt,'KG',tc||'#fff'),r*.27);d.position.set(0,r*.64,z+f*.004);if(f<0)d.rotation.y=Math.PI;g.add(d);
const d2=decal(label(txt,'KG',tc||'#fff'),r*.27);d2.position.set(0,-r*.64,z+f*.004);if(f<0)d2.rotation.y=Math.PI;g.add(d2)});
const th=new THREE.Mesh(new THREE.TorusGeometry(.2,.03,10,40),sm);g.add(th);return g}
function cyl(a,b,h,m,s){return new THREE.Mesh(new THREE.CylinderGeometry(a,b,h,s||48),m)}
function rotZ(m){m.rotation.z=Math.PI/2;return m}
function dumbbell(m,m2){const g=new THREE.Group();g.add(rotZ(cyl(.15,.15,2.5,steelK,32)));[-1,1].forEach(function(s){[[.74,.42,1.08],[.6,.36,1.52]].forEach(function(q){const a=new THREE.Mesh(hexGeo(q[0],q[1]),m);a.rotation.y=Math.PI/2;a.position.x=s*q[2];g.add(a)});const c=rotZ(cyl(.22,.22,.16,steel,32));c.position.x=s*1.82;g.add(c);const d=decal(label('12','KG','#fff'),.34);d.rotation.y=s>0?Math.PI/2:-Math.PI/2;d.position.x=s*1.92;g.add(d)});return g}
function kettle(m){const g=new THREE.Group(),b=new THREE.Mesh(new THREE.SphereGeometry(1,64,40),m);b.scale.set(1,.92,1);b.position.y=-.1;g.add(b);const base=cyl(.64,.72,.2,m,48);base.position.y=-.98;g.add(base);const h=new THREE.Mesh(new THREE.TorusGeometry(.64,.14,24,64,Math.PI),m);h.position.y=.7;g.add(h);[-1,1].forEach(function(s){const n=cyl(.15,.17,.3,m,24);n.position.set(s*.64,.6,0);g.add(n)});const d=decal(label('16','KG','#fff'),.34);d.position.set(0,-.15,.992);g.add(d);const d2=decal(label('16','KG','#fff'),.34);d2.rotation.y=Math.PI;d2.position.set(0,-.15,-.992);g.add(d2);return g}
function plateGeo(r,t){const s=new THREE.Shape();s.absarc(0,0,r,0,Math.PI*2,false);const h=new THREE.Path();h.absarc(0,0,.2,0,Math.PI*2,true);s.holes.push(h);const g=new THREE.ExtrudeGeometry(s,{depth:t,bevelEnabled:true,bevelSize:.04,bevelThickness:.04,bevelSegments:3,curveSegments:56});g.translate(0,0,-t/2);return g}
function glove(m,m2){const g=new THREE.Group(),b=new THREE.Mesh(new THREE.SphereGeometry(1,64,40),m);b.scale.set(1,1.12,.95);g.add(b);const t=new THREE.Mesh(new THREE.SphereGeometry(.42,40,28),m);t.position.set(-.78,-.1,.35);t.scale.set(.9,1.25,.9);t.rotation.z=.5;g.add(t);const c=cyl(.62,.7,.8,m2,48);c.position.y=-1.3;g.add(c);const wm=M({color:0xf4f4f4,roughness:.4});const r=new THREE.Mesh(new THREE.TorusGeometry(.66,.07,14,56),wm);r.rotation.x=Math.PI/2;r.position.y=-.98;g.add(r);const r2=new THREE.Mesh(new THREE.TorusGeometry(.66,.05,14,56),wm);r2.rotation.x=Math.PI/2;r2.position.y=-1.55;g.add(r2);for(let i=0;i<4;i++){const l=new THREE.Mesh(new THREE.BoxGeometry(.5,.05,.05),wm);l.position.set(0,-1.12-i*.1,.69);g.add(l)}const d=decal(label('PRO',null,'#fff'),.38);d.position.set(0,.05,.935);g.add(d);return g}
function blue(g){const fill=new THREE.MeshBasicMaterial({color:0x123f70,transparent:true,opacity:.35,depthWrite:false}),line=new THREE.LineBasicMaterial({color:accent,transparent:true,opacity:.95});const meshes=[];g.traverse(function(o){if(o.isMesh)meshes.push(o)});meshes.forEach(function(o){const e=new THREE.LineSegments(new THREE.EdgesGeometry(o.geometry,1),line);o.add(e);o.material=fill});return g}
const root=new THREE.Group();scene.add(root);
let ry=0,rx=0,vy=.004,vx=0,drag=false,lx=0,ly=0,mx=0,my=0;
host.addEventListener('pointerdown',function(e){drag=true;lx=e.clientX;ly=e.clientY;try{host.setPointerCapture(e.pointerId)}catch(_){}});
host.addEventListener('pointermove',function(e){if(!drag)return;vy=(e.clientX-lx)*.007;vx=(e.clientY-ly)*.004;lx=e.clientX;ly=e.clientY;ry+=vy;rx+=vx});
['pointerup','pointercancel'].forEach(function(n){host.addEventListener(n,function(){drag=false})});
addEventListener('pointermove',function(e){mx=e.clientX/innerWidth-.5;my=e.clientY/innerHeight-.5});
const ticks=[];let T=0;
function enter(o,x,y,z,delay){const to={x:x,y:y,z:z};o.position.set(x+(Math.random()>.5?1:-1)*14,y+(Math.random()-.5)*8,z-6);o.scale.setScalar(.001);gsap.to(o.position,{x:to.x,y:to.y,z:to.z,duration:1.8,delay:delay,ease:'expo.out'});gsap.to(o.scale,{x:1,y:1,z:1,duration:1.4,delay:delay,ease:'back.out(1.6)'});gsap.from(o.rotation,{x:'+=6',y:'+=8',duration:2,delay:delay,ease:'expo.out'})}
const kind=C.kind;
if(kind==='blueprint'){
  const d=blue(dumbbell(steel,steel)),k=blue(kettle(steel)),g=blue(glove(steel,steel));const p=new THREE.Mesh(plateGeo(1.3,.3),steel);blue(p);
  root.add(d,k,g,p);enter(d,0,-1.3,0,.2);d.scale.setScalar(1);enter(k,-2.4,1.5,-1,.5);enter(g,2.4,1.3,-.5,.8);enter(p,2.0,-1.7,.2,1.1);
  d.userData.base=1.15;ticks.push(function(t){d.rotation.y=t*.4;d.rotation.x=Math.sin(t*.6)*.25;k.rotation.y=-t*.5;g.rotation.y=t*.45;g.rotation.z=Math.sin(t)*.2;p.rotation.x=t*.35;p.rotation.y=Math.sin(t*.5)*.6});camera.position.set(0,0,12.5);
}
if(kind==='lift'){
  const bar=cyl(.07,.07,9.4,steelK,24);rotZ(bar);root.add(bar);
  const sp=[[1.5,.36,0xd6322f,.6],[1.5,.32,0x2a5fd0,.4],[1.5,.28,0xf2c500,.3],[1.5,.24,0x2e9b4a,.3],[1.0,.2,0xf2f2f2,.2],[.8,.16,0x222222,.15]];
  const plates=[];[-1,1].forEach(function(s){let x=0;sp.forEach(function(q,i){const m=plateGrp(q[0],q[1],q[2],['25','20','15','10','5','2.5'][i],i===4?'#222':'#fff');m.rotation.y=Math.PI/2;x+=q[1]/2+.04;m.userData={tx:s*(1.5+x),s:s,t:0,i:i};x+=q[1]/2;m.position.set(s*14,0,0);m.visible=false;root.add(m);plates.push(m)})});
  [-1,1].forEach(function(s){const sl=rotZ(cyl(.13,.13,3.4,steel,24));sl.position.x=s*3.2;root.add(sl);const col=rotZ(cyl(.22,.22,.24,steel,32));col.position.x=s*1.3;root.add(col);const cb=rotZ(cyl(.23,.23,.06,dark,32));cb.position.x=s*1.3+s*.08;root.add(cb);const sc=cyl(.045,.045,.12,steel,12);sc.position.set(s*1.3,.22,0);root.add(sc)});
  root.rotation.y=.5;ry=.5;vy=0;camera.position.set(0,1.6,11);camera.lookAt(0,0,0);
  window.__lift=function(n){plates.forEach(function(m){const on=m.userData.i<n;if(on&&m.userData.t!==1){m.userData.t=1;m.visible=true;gsap.fromTo(m.position,{x:m.userData.s*12,y:3},{x:m.userData.tx,y:0,duration:1.1,ease:'power3.out'});gsap.fromTo(m.rotation,{x:6},{x:0,duration:1.1,ease:'power3.out'})}if(!on&&m.userData.t===1){m.userData.t=0;gsap.to(m.position,{x:m.userData.s*12,y:3,duration:.6,ease:'power2.in',onComplete:function(){m.visible=false}})}})};
  ticks.push(function(t){root.position.y=Math.sin(t*.8)*.08});
}
if(kind==='bag'){
  const red=new THREE.MeshPhysicalMaterial({color:0xc62f2f,roughness:.32,metalness:.1,clearcoat:1,clearcoatRoughness:.15}),leather=M({color:0x3a2a22,roughness:.55,metalness:.05});
  const pivot=new THREE.Group();pivot.position.set(0,3.6,0);root.add(pivot);
  const bagm=new THREE.Mesh(new THREE.CapsuleGeometry(.85,2.5,16,40),M({color:0x7a1f1f,roughness:.45,metalness:.1}));bagm.position.y=-2.7;pivot.add(bagm);
  const bl=new THREE.Mesh(new THREE.CylinderGeometry(.87,.87,1.5,48,1,true,-.8,1.6),new THREE.MeshBasicMaterial({map:label(C.bagTop||'BOX',C.bagSub||'GYM','#fff'),transparent:true,depthWrite:false,toneMapped:false}));bl.position.y=-2.7;pivot.add(bl);[-1.6,-2.7,-3.8].forEach(function(y){const s=new THREE.Mesh(new THREE.TorusGeometry(.86,.05,10,48),leather);s.rotation.x=Math.PI/2;s.position.y=y;pivot.add(s)});
  [0,1,2,3].forEach(function(i){const a=i*Math.PI/2,ch=cyl(.025,.025,1.5,steel,8);ch.position.set(Math.cos(a)*.38,-.55,Math.sin(a)*.38);ch.lookAt(0,-1.3,0);ch.rotateX(Math.PI/2);pivot.add(ch)});
  const beam=cyl(.12,.12,3.4,steel,24);rotZ(beam);beam.position.set(0,3.65,0);root.add(beam);
  const g1=glove(red,leather),g2=glove(red,leather);g1.scale.setScalar(.55);g2.scale.setScalar(.55);g1.position.set(-2.5,-1.4,.6);g2.position.set(2.5,-1.9,.8);g1.rotation.z=-.6;g2.rotation.z=.6;root.add(g1,g2);
  camera.position.set(0,.2,14.5);root.position.y=-.4;vy=0;
  let ax=0,az=0,vax=0,vaz=0,grab=false,gx=0,last={x:0,y:0,t:0};const ray=new THREE.Raycaster(),ndc=new THREE.Vector2();
  function hit(e){const r=renderer.domElement.getBoundingClientRect();ndc.set((e.clientX-r.left)/r.width*2-1,-((e.clientY-r.top)/r.height)*2+1);ray.setFromCamera(ndc,camera);return ray.intersectObject(bagm).length>0}
  host.addEventListener('pointerdown',function(e){if(hit(e)){grab=true;drag=false;gx=e.clientX;host.setPointerCapture(e.pointerId)}});
  host.addEventListener('pointermove',function(e){const t=performance.now(),dx=e.clientX-last.x,dt=Math.max(8,t-last.t);if(grab){const r=renderer.domElement.getBoundingClientRect();const nz=Math.max(-.9,Math.min(.9,-(e.clientX-gx)/r.width*3));vaz=(nz-az)*10;az=nz}else if(hit(e)&&Math.abs(dx)/dt>.5){vaz+=-dx/dt*1.1}last={x:e.clientX,y:e.clientY,t:t}});
  const rel=function(){grab=false};host.addEventListener('pointerup',rel);host.addEventListener('pointercancel',rel);
  host.addEventListener('click',function(e){if(hit(e)&&Math.abs(vaz)<.3)vaz+=(Math.random()>.5?1:-1)*4});
  enter(g1,-2.5,-1.4,.6,.5);enter(g2,2.5,-1.9,.8,.8);pivot.rotation.z=.5;
  ticks.push(function(t,dt){if(!grab){vaz+=(-18*Math.sin(az)-1.0*vaz)*dt;az+=vaz*dt}vax+=(-18*Math.sin(ax)-1.0*vax)*dt;ax+=vax*dt;pivot.rotation.z=az;pivot.rotation.x=ax;g1.position.y=-1.4+Math.sin(t*1.1)*.15;g2.position.y=-1.9+Math.sin(t*1.3+1)*.15;g1.rotation.y=mx*1.2;g2.rotation.y=mx*1.2});
  ticks.noRotate=true;
}
if(kind==='float'){
  const objs=[],mats=[M({color:0xe8eef6,metalness:1,roughness:.22}),M({color:0xaed0ec,metalness:.9,roughness:.3}),M({color:0xff7a3d,metalness:.5,roughness:.35})];
  for(let i=0;i<15;i++){const t=i%3,m=mats[i%3];let o=t===0?dumbbell(m,steel):t===1?kettle(m):new THREE.Mesh(plateGeo(1.1,.28),m);o.userData={vx:(Math.random()-.5)*.01,vy:(Math.random()-.5)*.01,rx:(Math.random()-.5)*.012,ry:(Math.random()-.5)*.012,s:.5+Math.random()*.35};root.add(o);const x=(Math.random()-.5)*20,y=(Math.random()-.5)*9,z=-3+Math.random()*4;enter(o,x,y,z,.15+i*.07);o.scale.setScalar(.001);gsap.to(o.scale,{x:o.userData.s,y:o.userData.s,z:o.userData.s,duration:1.4,delay:.15+i*.07,ease:'back.out(1.6)',overwrite:true});objs.push(o)}
  camera.position.set(0,0,12);vy=0;const pt=new THREE.Vector3();ticks.noRotate=true;let burst=0;host.addEventListener('pointerdown',function(){burst=1});
  ticks.push(function(t){const v=new THREE.Vector3(mx*2,-my*2,.5).unproject(camera).sub(camera.position).normalize();const d=-camera.position.z/v.z;pt.copy(camera.position).add(v.multiplyScalar(d));objs.forEach(function(o){const u=o.userData,dx=o.position.x-pt.x,dy=o.position.y-pt.y,dist=Math.hypot(dx,dy)+.01;if(dist<3.2){const f=(3.2-dist)/3.2*(.07+burst*.2);u.vx+=dx/dist*f;u.vy+=dy/dist*f;u.rx+=dy/dist*f*.4;u.ry+=dx/dist*f*.4}u.vx*=.985;u.vy*=.985;o.position.x+=u.vx;o.position.y+=u.vy+Math.sin(t+o.position.x)*.0025;o.rotation.x+=u.rx;o.rotation.y+=u.ry;u.rx*=.99;u.ry*=.99;if(o.position.x>11)o.position.x=-11;if(o.position.x<-11)o.position.x=11;if(o.position.y>5.5)o.position.y=-5.5;if(o.position.y<-5.5)o.position.y=5.5});burst*=.9});
}
if(kind==='core'){
  const ico=new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.IcosahedronGeometry(1.9,1)),new THREE.LineBasicMaterial({color:accent,transparent:true,opacity:.85}));root.add(ico);
  const core=new THREE.Mesh(new THREE.SphereGeometry(.75,48,32),new THREE.MeshBasicMaterial({color:0xeaffc0}));root.add(core);
  const gc=document.createElement('canvas');gc.width=gc.height=256;const gg=gc.getContext('2d'),gr=gg.createRadialGradient(128,128,0,128,128,128);gr.addColorStop(0,'rgba(200,255,90,1)');gr.addColorStop(.4,'rgba(182,255,59,.45)');gr.addColorStop(1,'rgba(182,255,59,0)');gg.fillStyle=gr;gg.fillRect(0,0,256,256);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:new THREE.CanvasTexture(gc),blending:THREE.AdditiveBlending,transparent:true,depthWrite:false}));glow.scale.setScalar(7);root.add(glow);
  const rings=[0,1,2].map(function(i){const r=new THREE.Mesh(new THREE.TorusGeometry(2.5+i*.45,.03,12,160),new THREE.MeshBasicMaterial({color:accent,transparent:true,opacity:.85-i*.2}));r.rotation.set(i*1.0,i*.6,0);root.add(r);return r});
  const N=500,pos=new Float32Array(N*3);for(let i=0;i<N;i++){const r=3.2+Math.random()*2.2,a=Math.random()*6.283,b=(Math.random()-.5)*2.4;pos[i*3]=Math.cos(a)*r;pos[i*3+1]=b*r*.5;pos[i*3+2]=Math.sin(a)*r}
  const pg=new THREE.BufferGeometry();pg.setAttribute('position',new THREE.BufferAttribute(pos,3));const pts=new THREE.Points(pg,new THREE.PointsMaterial({color:accent,size:.05,transparent:true,opacity:.8,depthWrite:false}));root.add(pts);
  root.scale.setScalar(.001);gsap.to(root.scale,{x:1,y:1,z:1,duration:1.8,ease:'expo.out'});camera.position.set(0,0,10.5);
  ticks.push(function(t){ico.rotation.y=t*.3;ico.rotation.x=t*.17;rings[0].rotation.z=t*.6;rings[1].rotation.x=t*.5;rings[2].rotation.y=t*.7;pts.rotation.y=t*.12;const s=1+Math.sin(t*2.4)*.07;core.scale.setScalar(s);glow.scale.setScalar(6.4+Math.sin(t*2.4)*.7)});
}
/* ---- themed kinds for non-gym businesses ---- */
function G(){const g=new THREE.Group();root.add(g);g.scale.setScalar(.001);gsap.to(g.scale,{x:1,y:1,z:1,duration:1.6,ease:'expo.out'});return g}
function dbl(o){o.side=THREE.DoubleSide;return o}
function ribbon(w,n,fn,mat){const geo=new THREE.BufferGeometry(),pos=new Float32Array(n*6),idx=[];for(let i=0;i<n-1;i++){const a=i*2;idx.push(a,a+1,a+2,a+1,a+3,a+2)}geo.setIndex(idx);geo.setAttribute('position',new THREE.BufferAttribute(pos,3));const m=new THREE.Mesh(geo,mat);m.frustumCulled=false;const a=new THREE.Vector3(),b=new THREE.Vector3(),tg=new THREE.Vector3(),sd=new THREE.Vector3(),Z=new THREE.Vector3(0,0,1);
 m.userData.upd=function(t){const p=geo.attributes.position;for(let i=0;i<n;i++){const u=i/(n-1);fn(u,t,a);fn(Math.min(1,u+.012),t,b);tg.subVectors(b,a);if(tg.lengthSq()<1e-9)tg.set(0,1,0);sd.crossVectors(tg,Z);if(sd.lengthSq()<1e-9)sd.set(1,0,0);sd.normalize().multiplyScalar(w*.5*(1-u*.35));p.setXYZ(i*2,a.x+sd.x,a.y+sd.y,a.z+sd.z);p.setXYZ(i*2+1,a.x-sd.x,a.y-sd.y,a.z-sd.z)}p.needsUpdate=true;geo.computeVertexNormals()};m.userData.upd(0);return m}
function sparkTex(){const c=document.createElement('canvas');c.width=c.height=128;const g=c.getContext('2d'),gr=g.createRadialGradient(64,64,0,64,64,64);gr.addColorStop(0,'rgba(255,255,255,1)');gr.addColorStop(.3,'rgba(255,255,255,.35)');gr.addColorStop(1,'rgba(255,255,255,0)');g.fillStyle=gr;g.fillRect(0,0,128,128);return new THREE.CanvasTexture(c)}
function dust(n,rad,col,size){const pos=new Float32Array(n*3);for(let i=0;i<n;i++){const r=rad*(.4+Math.random()*.7),a=Math.random()*6.283,b=(Math.random()-.5)*rad*1.3;pos[i*3]=Math.cos(a)*r;pos[i*3+1]=b;pos[i*3+2]=Math.sin(a)*r}const g=new THREE.BufferGeometry();g.setAttribute('position',new THREE.BufferAttribute(pos,3));return new THREE.Points(g,new THREE.PointsMaterial({color:col,size:size||.06,transparent:true,opacity:.8,depthWrite:false,map:sparkTex(),blending:THREE.AdditiveBlending}))}
const hsl=function(h,s,l){return new THREE.Color().setHSL(((h%1)+1)%1,s,l)};
function hueOf(c){const o={};c.getHSL(o);return o.h}

if(kind==='rings'){
  const g=G();g.position.y=.3;camera.position.set(0,0,15.5);
  const wood=M({color:C.wood||0xe9e2d3,roughness:.42,metalness:.05}),strap=M({color:accent,roughness:.65});
  const bar=rotZ(cyl(.09,.09,6.2,steelK,24));bar.position.y=3.7;g.add(bar);
  [-1,1].forEach(function(s){const c=rotZ(cyl(.16,.16,.3,steel,24));c.position.set(s*3.1,3.7,0);g.add(c)});
  const pend=[];
  [-1,1].forEach(function(s,i){const p=new THREE.Group();p.position.set(s*1.55,3.7,0);g.add(p);
    const st=new THREE.Mesh(new THREE.BoxGeometry(.2,3.3,.035),strap);st.position.y=-1.65;p.add(st);
    [-1,1].forEach(function(f){const st2=new THREE.Mesh(new THREE.BoxGeometry(.2,3.3,.01),M({color:0x111111,roughness:.9}));st2.position.set(0,-1.65,f*.02);p.add(st2)});
    const bk=new THREE.Mesh(new THREE.BoxGeometry(.34,.26,.12),steel);bk.position.y=-3.3;p.add(bk);
    const r=new THREE.Mesh(new THREE.TorusGeometry(.98,.1,28,100),wood);r.position.y=-4.38;p.add(r);
    const r2=new THREE.Mesh(new THREE.TorusGeometry(.98,.103,6,100,Math.PI*.35),M({color:accent,roughness:.5}));r2.position.y=-4.38;r2.rotation.z=Math.PI*.15;p.add(r2);
    pend.push(p)});
  const ch=dust(260,3.4,0xffffff,.05);ch.position.y=-1.2;g.add(ch);
  ticks.push(function(t){pend.forEach(function(p,i){p.rotation.z=Math.sin(t*1.1+i*1.7)*.13;p.rotation.x=Math.cos(t*.85+i)*.07});ch.rotation.y=t*.05;ch.position.y=-1.2+Math.sin(t*.6)*.15});
}
if(kind==='tramp'){
  const g=G();camera.position.set(0,.4,11.5);const tilt=new THREE.Group();tilt.rotation.x=.42;g.add(tilt);
  const fr=new THREE.Mesh(new THREE.TorusGeometry(2.6,.15,18,110),M({color:accent,metalness:.5,roughness:.3}));fr.rotation.x=Math.PI/2;tilt.add(fr);
  const mt=tex(512,512,function(c,w,h){c.fillStyle='#16213a';c.fillRect(0,0,w,h);c.strokeStyle='rgba(255,255,255,.18)';c.lineWidth=2;for(let i=-20;i<40;i++){c.beginPath();c.moveTo(i*26,0);c.lineTo(i*26+h,h);c.stroke();c.beginPath();c.moveTo(i*26+h,0);c.lineTo(i*26,h);c.stroke()}c.strokeStyle=C.accent||'#fff';c.lineWidth=10;c.beginPath();c.arc(256,256,92,0,6.283);c.stroke()});
  const mat=new THREE.Mesh(new THREE.CircleGeometry(2.46,72),M({map:mt,roughness:.85,side:THREE.DoubleSide}));mat.rotation.x=-Math.PI/2;mat.position.y=-.06;tilt.add(mat);
  for(let i=0;i<44;i++){const a=i/44*Math.PI*2,sp=cyl(.02,.02,.26,steel,6);sp.position.set(Math.cos(a)*2.53,-.06,Math.sin(a)*2.53);sp.rotation.z=Math.cos(a)*.7;sp.rotation.x=-Math.sin(a)*.7;tilt.add(sp)}
  [0,1,2,3].forEach(function(i){const a=i*Math.PI/2+Math.PI/4,lg=cyl(.07,.07,1.9,steel,12);lg.position.set(Math.cos(a)*2.9,-.95,Math.sin(a)*2.9);lg.rotation.z=Math.cos(a)*.35;lg.rotation.x=-Math.sin(a)*.35;tilt.add(lg)});
  const ball=new THREE.Mesh(new THREE.SphereGeometry(.55,48,32),M({color:0xfff2d0,roughness:.3,metalness:.1,emissive:accent,emissiveIntensity:.25}));tilt.add(ball);
  const sh=new THREE.Mesh(new THREE.CircleGeometry(.5,32),new THREE.MeshBasicMaterial({color:0x000000,transparent:true,opacity:.35,depthWrite:false}));sh.rotation.x=-Math.PI/2;sh.position.y=-.04;tilt.add(sh);
  ticks.push(function(t){const u=Math.abs(Math.sin(t*2.1)),h=u*3;ball.position.y=.55+h;const sq=h<.15?.8+h*1.3:1;ball.scale.set(1/Math.sqrt(sq),sq,1/Math.sqrt(sq));mat.position.y=-.06-(1-u)*.1*(h<.2?1:0);sh.scale.setScalar(1-u*.5);sh.material.opacity=.4-u*.25});
}
if(kind==='stones'){
  const g=G();g.position.y=-.3;camera.position.set(0,.3,11.5);
  const pal=C.stones||[0x6d6f73,0x8d8f91,0x585a5e,0xa3a39d,0x4a4c50,0x9a9c9f];
  const R=[1.45,1.15,.92,.7,.5,.34],H=[.5,.46,.42,.4,.38,.36];let y=0;const st=[];
  for(let i=0;i<R.length;i++){const geo=new THREE.SphereGeometry(1,64,40),p=geo.attributes.position;for(let k=0;k<p.count;k++){const x=p.getX(k),yy=p.getY(k),z=p.getZ(k),n=1+.05*Math.sin(x*3+i)+.04*Math.sin(z*4+yy*2+i*2);p.setXYZ(k,x*n,yy*n,z*n)}geo.computeVertexNormals();
    const m=new THREE.Mesh(geo,M({color:pal[i%pal.length],roughness:.55,metalness:.05,bumpMap:rubTex,bumpScale:.8}));m.scale.set(R[i],H[i]*R[i]*1.05,R[i]*.92);y+=H[i]*R[i]*.95*(i?1:.35);m.position.set((Math.random()-.5)*.1,y,0);m.rotation.y=Math.random()*6;g.add(m);y+=H[i]*R[i]*.7;st.push(m)}
  const wat=[0,1,2].map(function(i){const r=new THREE.Mesh(new THREE.RingGeometry(1.8,1.86,120),new THREE.MeshBasicMaterial({color:accent,transparent:true,opacity:.7,side:THREE.DoubleSide,depthWrite:false}));r.rotation.x=-Math.PI/2;r.position.y=-.02;g.add(r);return r});
  const pool=new THREE.Mesh(new THREE.CircleGeometry(3.2,80),M({color:C.pool||0x0f3d3a,roughness:.2,metalness:.6,transparent:true,opacity:.85}));pool.rotation.x=-Math.PI/2;pool.position.y=-.03;g.add(pool);
  const fl=dust(160,3,accent,.07);fl.position.y=2;g.add(fl);g.position.y=-2.2;
  ticks.push(function(t){wat.forEach(function(r,i){const u=((t*.28)+i/3)%1;r.scale.setScalar(.7+u*1.6);r.material.opacity=(1-u)*.6});st.forEach(function(m,i){m.position.x=Math.sin(t*.7+i)*.02*i});fl.rotation.y=t*.1;fl.position.y=2+Math.sin(t*.5)*.2});
}
if(kind==='lotus'){
  const g=G();camera.position.set(0,2.2,11);g.rotation.x=.35;
  const base=hueOf(accent),pets=[];
  const layers=[[8,2.0,.32,1.55,.4],[8,1.75,.62,1.25,.5],[6,1.45,.95,.95,.58],[5,1.0,1.25,.62,.72]];
  layers.forEach(function(L,li){for(let i=0;i<L[0];i++){const piv=new THREE.Group();piv.rotation.y=i/L[0]*Math.PI*2+li*.4;g.add(piv);
    const sh=new THREE.Shape();sh.moveTo(0,0);sh.bezierCurveTo(.42,.35,.5,1.1,0,L[1]);sh.bezierCurveTo(-.5,1.1,-.42,.35,0,0);
    const geo=new THREE.ShapeGeometry(sh,24),p=geo.attributes.position;for(let k=0;k<p.count;k++){const x=p.getX(k),yy=p.getY(k);p.setZ(k,-x*x*.5*(1+yy*.2))}geo.computeVertexNormals();
    const m=new THREE.Mesh(geo,new THREE.MeshPhysicalMaterial({color:hsl(base,.85,.5+li*.06),roughness:.35,metalness:0,side:THREE.DoubleSide,emissive:hsl(base,.8,.3),emissiveIntensity:.35+li*.05,clearcoat:.6}));
    m.scale.set(L[3],1,1);m.position.set(0,0,.25+li*.0);piv.add(m);const tilt=new THREE.Group();tilt.position.set(0,L[2]*.4,.15);piv.remove(m);m.position.set(0,0,0);tilt.add(m);piv.add(tilt);tilt.rotation.x=L[4];tilt.userData={b:L[4],i:i,li:li};pets.push(tilt)}});
  const cen=new THREE.Mesh(new THREE.SphereGeometry(.34,32,24),M({color:0xffd34d,roughness:.4,emissive:0xffa400,emissiveIntensity:.5}));cen.position.y=.9;g.add(cen);
  for(let i=0;i<24;i++){const a=i/24*6.283,s=new THREE.Mesh(new THREE.SphereGeometry(.05,10,8),M({color:0xffe27a,emissive:0xffb000,emissiveIntensity:.8}));s.position.set(Math.cos(a)*.34,.95+Math.sin(i*2)*.05,Math.sin(a)*.34);g.add(s)}
  const pad=new THREE.Mesh(new THREE.CircleGeometry(2.6,70),M({color:C.pool||0x1d5b3a,roughness:.5,side:THREE.DoubleSide}));pad.rotation.x=-Math.PI/2;pad.position.y=-.1;g.add(pad);
  const fl=dust(140,3.2,accent,.07);fl.position.y=1.8;g.add(fl);g.position.y=2.3;g.scale.setScalar(.8);camera.position.set(0,3.2,11);
  ticks.push(function(t){pets.forEach(function(p){p.rotation.x=p.userData.b+Math.sin(t*.8+p.userData.li*.7)*.09});g.rotation.y=t*.1;fl.rotation.y=-t*.12});
}
if(kind==='shoe'){
  const g=G();g.position.y=-.2;camera.position.set(0,.4,13);
  const sat=new THREE.MeshPhysicalMaterial({color:hsl(.97,.55,.8),roughness:.28,metalness:.05,clearcoat:.8,clearcoatRoughness:.2,sheen:1,sheenColor:new THREE.Color(0xffffff),side:THREE.DoubleSide});
  const prof=[[0,0],[.3,0],[.38,.04],[.55,.3],[.66,.7],[.64,1.1],[.55,1.5],[.47,1.95],[.45,2.4],[.47,2.7]].map(function(a){return new THREE.Vector2(a[0],a[1])});
  function shoe(){const s=new THREE.Group(),l=new THREE.Mesh(new THREE.LatheGeometry(prof,64),sat);l.scale.set(.85,1,1.2);s.add(l);
    const inner=new THREE.Mesh(new THREE.CircleGeometry(.43,40),M({color:0x2a1a1f,roughness:.9}));inner.rotation.x=-Math.PI/2;inner.position.y=2.62;inner.scale.set(.85,1.2,1);s.add(inner);
    const tip=new THREE.Mesh(new THREE.CylinderGeometry(.3,.3,.03,40),M({color:hsl(hueOf(accent),.4,.55),roughness:.7}));tip.position.y=.01;tip.scale.set(.85,1,1.2);s.add(tip);
    const draw=new THREE.Mesh(new THREE.TorusGeometry(.48,.018,8,64),M({color:0xffffff,roughness:.4}));draw.rotation.x=Math.PI/2;draw.position.y=2.55;draw.scale.set(.85,1.2,1);s.add(draw);
    const stitch=new THREE.Mesh(new THREE.TorusGeometry(.62,.012,6,64),M({color:0xffffff,roughness:.5}));stitch.rotation.x=Math.PI/2;stitch.position.y=1.0;stitch.scale.set(.85,1.2,1);s.add(stitch);
    return s}
  const a=shoe(),b=shoe();a.position.set(-1.0,-2.2,0);b.position.set(1.0,-2.2,.3);a.rotation.set(.1,0,.12);b.rotation.set(-.08,0,-.14);g.add(a);g.add(b);
  const rm=dbl(new THREE.MeshStandardMaterial({color:hsl(.97,.6,.72),roughness:.25,metalness:.1,emissive:hsl(.97,.6,.3),emissiveIntensity:.2}));
  [[a,-1],[b,1]].forEach(function(q,k){for(let j=0;j<2;j++){const r=ribbon(.2,60,function(u,t,o){const ph=j*Math.PI+k;const ang=u*7+ph+t*.25;const rr=.5+u*.25;o.set(q[0].position.x+Math.cos(ang)*rr*(1-u*.2)+u*q[1]*1.1*Math.sin(t*.9+u*4+k),q[0].position.y+2.6-u*u*.5+Math.sin(u*9+t*1.6+ph)*.2*u+u*1.1,Math.sin(ang)*rr*1.2+Math.sin(u*5+t+ph)*.35*u)},rm);g.add(r);q.push(r)}});
  const sp=dust(120,3.6,accent,.07);g.add(sp);
  ticks.push(function(t){const rr=[];g.children.forEach(function(c){if(c.userData&&c.userData.upd)c.userData.upd(t)});a.rotation.y=t*.5;b.rotation.y=-t*.45;a.position.y=-2.2+Math.sin(t*1.2)*.12;b.position.y=-2.2+Math.sin(t*1.2+1.5)*.12;sp.rotation.y=t*.08});
}
if(kind==='ribbon'){
  const g=G();camera.position.set(0,0,12);const base=hueOf(accent),N=6;
  for(let k=0;k<N;k++){const m=dbl(new THREE.MeshStandardMaterial({color:hsl(base+k*.07,.7,.58),roughness:.3,metalness:.15,emissive:hsl(base+k*.07,.7,.3),emissiveIntensity:.3}));
    const r=ribbon(.55,90,function(u,t,o){const a=u*6.2+t*.55+k*Math.PI*2/N,rad=3.3*(1-u*.82)+Math.sin(u*8+t+k)*.25,yy=(u-.5)*5.2+Math.sin(t*.8+k)*.3;o.set(Math.cos(a)*rad,yy,Math.sin(a)*rad)},m);g.add(r)}
  const core=new THREE.Mesh(new THREE.SphereGeometry(.32,32,24),new THREE.MeshBasicMaterial({color:0xffffff}));core.position.y=-.4;g.add(core);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:sparkTex(),color:accent,blending:THREE.AdditiveBlending,transparent:true,depthWrite:false}));glow.scale.setScalar(4);glow.position.y=-.4;g.add(glow);
  const sp=dust(200,3.6,accent,.06);g.add(sp);
  ticks.push(function(t){g.children.forEach(function(c){if(c.userData&&c.userData.upd)c.userData.upd(t)});glow.scale.setScalar(3.6+Math.sin(t*2)*.5);sp.rotation.y=t*.1});
}
if(kind==='mirrorball'){
  const g=G();camera.position.set(0,0,12);
  const ball=new THREE.Mesh(new THREE.IcosahedronGeometry(1.9,3),new THREE.MeshStandardMaterial({color:0xdfe3ea,metalness:1,roughness:.07,flatShading:true}));g.add(ball);
  const cap=cyl(.1,.1,2.4,steel,12);cap.position.y=3.0;g.add(cap);const hk=new THREE.Mesh(new THREE.TorusGeometry(.18,.04,10,24),steel);hk.position.y=4.3;g.add(hk);
  const spots=[];for(let i=0;i<26;i++){const s=new THREE.Sprite(new THREE.SpriteMaterial({map:sparkTex(),color:hsl(hueOf(accent)+i*.03,.8,.65),blending:THREE.AdditiveBlending,transparent:true,depthWrite:false}));s.scale.setScalar(.5+Math.random()*.7);s.userData={a:Math.random()*6.28,r:3+Math.random()*1.8,y:(Math.random()-.5)*5,sp:.2+Math.random()*.4};g.add(s);spots.push(s)}
  const beams=[-1,1].map(function(s){const c=new THREE.Mesh(new THREE.ConeGeometry(1.5,5.5,32,1,true),new THREE.MeshBasicMaterial({color:accent,transparent:true,opacity:.1,blending:THREE.AdditiveBlending,depthWrite:false,side:THREE.DoubleSide}));c.position.set(s*3.6,2.4,0);c.rotation.z=s*.9+Math.PI;g.add(c);return c});
  g.position.y=-.4;
  ticks.push(function(t){ball.rotation.y=t*.45;spots.forEach(function(s){const u=s.userData,a=u.a+t*u.sp;s.position.set(Math.cos(a)*u.r,u.y+Math.sin(t+u.a)*.3,Math.sin(a)*u.r);s.material.opacity=.5+.5*Math.sin(t*2+u.a)});beams.forEach(function(b,i){b.material.opacity=.07+.05*Math.sin(t*1.6+i*2)})});
}
if(kind==='ballerina'){
  const g=G();camera.position.set(0,.2,12);
  const por=M({color:0xf4ebe6,roughness:.4,metalness:.05}),tutu=new THREE.MeshPhysicalMaterial({color:hsl(hueOf(accent),.35,.9),roughness:.55,transparent:true,opacity:.88,side:THREE.DoubleSide,sheen:1,sheenColor:accent}),ac=M({color:accent,roughness:.35,metalness:.4});
  const fig=new THREE.Group();g.add(fig);
  const skirts=[[1.75,-.45,1],[1.45,-.25,.82],[1.15,-.1,.64]];const sk=[];
  skirts.forEach(function(q,i){const pr=[[.22,.3],[.5,.12],[q[0]*.62,q[1]*.4],[q[0],q[1]]].map(function(a){return new THREE.Vector2(a[0],a[1])});const m=new THREE.Mesh(new THREE.LatheGeometry(pr,64),tutu);m.position.y=-.1-i*.02;m.rotation.y=i;fig.add(m);sk.push(m)});
  const waist=new THREE.Mesh(new THREE.TorusGeometry(.24,.05,12,40),ac);waist.rotation.x=Math.PI/2;waist.position.y=.3;fig.add(waist);
  const tor=new THREE.Mesh(new THREE.CylinderGeometry(.26,.32,.8,32),por);tor.position.y=.72;fig.add(tor);
  const bodice=new THREE.Mesh(new THREE.CylinderGeometry(.27,.33,.4,32,1,true,0,6.283),ac);bodice.position.y=.5;fig.add(bodice);
  const neck=cyl(.09,.11,.22,por,16);neck.position.y=1.2;fig.add(neck);
  const head=new THREE.Mesh(new THREE.SphereGeometry(.24,32,24),por);head.position.y=1.5;fig.add(head);
  const bun=new THREE.Mesh(new THREE.SphereGeometry(.11,20,16),M({color:0x2b1f24,roughness:.6}));bun.position.set(0,1.66,-.18);fig.add(bun);
  [-1,1].forEach(function(s){const arm=new THREE.Group();arm.position.set(s*.28,1.0,0);const u=cyl(.065,.05,1.15,por,12);u.position.y=.55;arm.add(u);arm.rotation.z=s*-.42;arm.rotation.x=-.05;fig.add(arm);
    const leg=cyl(.13,.07,1.9,por,16);leg.position.set(s*.13,-1.25,0);leg.rotation.z=s*.07;fig.add(leg);
    const toe=new THREE.Mesh(new THREE.SphereGeometry(.09,16,12),ac);toe.position.set(s*.2,-2.25,.02);fig.add(toe)});
  const plat=cyl(1.1,1.2,.22,M({color:C.pool||0x2a2230,roughness:.35,metalness:.5}),64);plat.position.y=-2.4;g.add(plat);
  const ringp=new THREE.Mesh(new THREE.TorusGeometry(1.15,.04,10,80),ac);ringp.rotation.x=Math.PI/2;ringp.position.y=-2.28;g.add(ringp);
  const sp=dust(140,3.4,accent,.06);g.add(sp);g.position.y=.1;
  ticks.push(function(t){fig.rotation.y=t*2.2;sk.forEach(function(m,i){m.scale.set(1+Math.sin(t*3+i)*.025,1,1+Math.sin(t*3+i)*.025)});sp.rotation.y=-t*.1});
}

if(kind==='cafe'){
  const g=G();camera.position.set(0,1.2,13);g.rotation.x=.28;
  const cer=new THREE.MeshPhysicalMaterial({color:0xf6efe6,roughness:.18,metalness:0,clearcoat:1,clearcoatRoughness:.08});
  const cup=[[0,0],[.55,0],[.8,.05],[1.35,.9],[1.62,1.9],[1.68,2.1]].map(function(a){return new THREE.Vector2(a[0],a[1])});
  const body=new THREE.Mesh(new THREE.LatheGeometry(cup,72),cer);body.position.y=-.5;g.add(body);
  const inner=new THREE.Mesh(new THREE.CylinderGeometry(1.5,1.5,.02,64),M({color:0x3a2012,roughness:.25,metalness:.1,emissive:0x1a0c05,emissiveIntensity:.4}));inner.position.y=1.38;g.add(inner);
  const lip=new THREE.Mesh(new THREE.TorusGeometry(1.65,.05,14,72),cer);lip.rotation.x=Math.PI/2;lip.position.y=1.6;g.add(lip);
  const crema=new THREE.Mesh(new THREE.TorusGeometry(.9,.06,10,60),M({color:0xc58a4c,roughness:.5}));crema.rotation.x=Math.PI/2;crema.position.y=1.4;g.add(crema);
  const heart=new THREE.Mesh(new THREE.TorusGeometry(.42,.05,10,40),M({color:0xf1dcc0,roughness:.5}));heart.rotation.x=Math.PI/2;heart.position.y=1.41;heart.scale.set(1,1.3,1);g.add(heart);
  const hd=new THREE.Mesh(new THREE.TorusGeometry(.62,.17,20,60,Math.PI*1.25),cer);hd.position.set(1.62,.55,0);hd.rotation.z=-Math.PI*.62;g.add(hd);
  const band=new THREE.Mesh(new THREE.TorusGeometry(1.5,.06,12,72),M({color:accent,roughness:.35,metalness:.3}));band.rotation.x=Math.PI/2;band.position.y=.05;band.scale.set(1,1,1);g.add(band);
  const sau=new THREE.Mesh(new THREE.LatheGeometry([[0,0],[1.4,0],[2.4,.12],[3.0,.4],[3.08,.46]].map(function(a){return new THREE.Vector2(a[0],a[1])}),72),cer);sau.position.y=-.65;g.add(sau);
  const sr=new THREE.Mesh(new THREE.TorusGeometry(2.6,.05,10,80),M({color:accent,roughness:.35,metalness:.3}));sr.rotation.x=Math.PI/2;sr.position.y=-.47;g.add(sr);
  const spoon=new THREE.Group();const bowl=new THREE.Mesh(new THREE.SphereGeometry(.28,24,16),steel);bowl.scale.set(1,.35,1.4);spoon.add(bowl);const sh=rotZ(cyl(.05,.07,1.8,steel,12));sh.position.x=1.0;spoon.add(sh);spoon.position.set(1.0,-.38,1.9);spoon.rotation.y=-.5;g.add(spoon);
  const beanM=M({color:0x4a2a16,roughness:.45,metalness:.1});const beans=[];
  for(let i=0;i<9;i++){const b=new THREE.Mesh(new THREE.SphereGeometry(.2,20,14),beanM);b.scale.set(1,.62,.75);const a=i/9*Math.PI*2+.3,r=3.6+Math.sin(i*2.3)*.5;b.position.set(Math.cos(a)*r,-.42+Math.sin(i)*.1,Math.sin(a)*r*.8);b.rotation.set(i,i*1.7,i*.6);const sl=new THREE.Mesh(new THREE.BoxGeometry(.34,.015,.03),M({color:0x1c0f07}));sl.position.set(0,.125,0);b.add(sl);g.add(b);beans.push(b)}
  const stm=dbl(new THREE.MeshBasicMaterial({color:0xffffff,transparent:true,opacity:.22,depthWrite:false}));
  for(let k=0;k<3;k++){const r=ribbon(.38,70,function(u,t,o){const w=Math.sin(u*6+t*1.3+k*2.1)*.32*u;o.set(-.5+k*.5+w,1.5+u*2.9,Math.sin(u*5+t+k)*.28*u)},stm);g.add(r)}
  const sp=dust(90,3.2,accent,.05);sp.position.y=1.5;g.add(sp);g.position.y=-.2;g.scale.setScalar(.82);
  ticks.push(function(t){g.children.forEach(function(c){if(c.userData&&c.userData.upd)c.userData.upd(t)});g.rotation.y=Math.sin(t*.35)*.5;beans.forEach(function(b,i){b.rotation.y+=.004;b.position.y=-.42+Math.sin(t*.9+i)*.03});sp.rotation.y=t*.06});
}

function size(){const w=host.clientWidth||600,h=host.clientHeight||600;renderer.setSize(w,h,false);camera.aspect=w/h;const f=Math.max(1,.85/(w/h));camera.zoom=1/ (w/h<.9?1.35:1);camera.updateProjectionMatrix()}
new ResizeObserver(size).observe(host);size();
let vis=true;new IntersectionObserver(function(e){vis=e[0].isIntersecting}).observe(host);
const clock=new THREE.Clock();
function loop(){requestAnimationFrame(loop);if(!vis)return;const dt=Math.min(.05,clock.getDelta());T+=dt;
 if(!ticks.noRotate){if(!drag){ry+=vy;vy+=(.0035-vy)*.02;rx+=(0-rx)*.03+vx;vx*=.9}const sc=Math.min(3,scrollY/innerHeight);root.rotation.y=ry+mx*.3+sc*1.4;root.rotation.x=rx+my*.2;root.position.y=sc*1.2;root.scale.setScalar(kind==='lift'?1:Math.max(.55,1-sc*.18))}
 ticks.forEach(function(f){f(T,dt)});renderer.render(scene,camera)}
loop();host.classList.add('ok');host.parentElement.classList.add('ok');
