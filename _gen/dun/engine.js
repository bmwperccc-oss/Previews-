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
function size(){const w=host.clientWidth||600,h=host.clientHeight||600;renderer.setSize(w,h,false);camera.aspect=w/h;const f=Math.max(1,.85/(w/h));camera.zoom=1/ (w/h<.9?1.35:1);camera.updateProjectionMatrix()}
new ResizeObserver(size).observe(host);size();
let vis=true;new IntersectionObserver(function(e){vis=e[0].isIntersecting}).observe(host);
const clock=new THREE.Clock();
function loop(){requestAnimationFrame(loop);if(!vis)return;const dt=Math.min(.05,clock.getDelta());T+=dt;
 if(!ticks.noRotate){if(!drag){ry+=vy;vy+=(.0035-vy)*.02;rx+=(0-rx)*.03+vx;vx*=.9}const sc=Math.min(3,scrollY/innerHeight);root.rotation.y=ry+mx*.3+sc*1.4;root.rotation.x=rx+my*.2;root.position.y=sc*1.2;root.scale.setScalar(kind==='lift'?1:Math.max(.55,1-sc*.18))}
 ticks.forEach(function(f){f(T,dt)});renderer.render(scene,camera)}
loop();host.classList.add('ok');host.parentElement.classList.add('ok');
