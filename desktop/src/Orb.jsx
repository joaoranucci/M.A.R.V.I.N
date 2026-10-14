import React, { useEffect, useRef, useState } from 'react';
import * as THREE from 'three';

const vertex = `varying vec3 vNormal; varying vec3 vPosition; varying vec3 vWorld;
void main(){vNormal=normalize(normalMatrix*normal);vPosition=position;
vec4 mv=modelViewMatrix*vec4(position,1.);vWorld=normalize(-mv.xyz);gl_Position=projectionMatrix*mv;}`;
const fragment = `precision highp float; varying vec3 vNormal; varying vec3 vPosition; varying vec3 vWorld;
uniform float uTime; uniform float uLevel; uniform vec3 uColor;
void main(){
vec3 p=normalize(vPosition); float rim=pow(1.-max(0.,dot(normalize(vNormal),vWorld)),2.9);
float lat=asin(p.y);float lon=atan(p.z,p.x);
float filaments=pow(max(0.,sin(lon*14.+sin(lat*19.+uTime*.22)*2.+lat*13.)),18.);
float ribbons=pow(max(0.,sin(lat*36.+sin(lon*5.+uTime*.17)*2.)),25.);
float flow=filaments*.19+ribbons*.11;
float light=max(0.,dot(normalize(vNormal),normalize(vec3(-.6,1.,1.))));
vec3 base=vec3(.008,.021,.045)+uColor*(flow+rim*1.5+pow(light,22.)*.35);
base+=uColor*uLevel*.1; gl_FragColor=vec4(base,1.);
}`;

export default function Orb({ phase = 'idle', audio = {input:0,output:0}, small = false }) {
  const host = useRef(null), live = useRef({phase,audio});
  const [fallback,setFallback] = useState(false);
  live.current = {phase,audio};
  useEffect(() => {
    let renderer, frame, ro;
    const parent=host.current;
    try {
      renderer=new THREE.WebGLRenderer({alpha:true,antialias:true,powerPreference:'low-power'});
      renderer.setPixelRatio(Math.min(window.devicePixelRatio,1.6));
      renderer.setClearColor(0x000000,0);
      parent.appendChild(renderer.domElement);
      renderer.domElement.setAttribute('aria-label','Núcleo tridimensional do MARVIN');
      const scene=new THREE.Scene();
      const camera=new THREE.PerspectiveCamera(37,1,.1,100);
      camera.position.set(0,.13,6.3);
      const root=new THREE.Group(); scene.add(root);
      const uniforms={uTime:{value:0},uLevel:{value:0},uColor:{value:new THREE.Color('#198fff')}};
      const material=new THREE.ShaderMaterial({vertexShader:vertex,fragmentShader:fragment,uniforms});
      const sphere=new THREE.Mesh(new THREE.SphereGeometry(1.17,80,64),material);root.add(sphere);
      const wireMat=new THREE.MeshBasicMaterial({color:0x258eff,wireframe:true,transparent:true,opacity:.055});
      const cage=new THREE.Mesh(new THREE.IcosahedronGeometry(1.185,3),wireMat);root.add(cage);
      const glowMat=new THREE.ShaderMaterial({vertexShader:vertex,fragmentShader:`varying vec3 vNormal;varying vec3 vWorld;uniform vec3 uColor;
      void main(){float a=pow(1.-abs(dot(normalize(vNormal),normalize(vWorld))),3.5);gl_FragColor=vec4(uColor,a*.16);}`,
        uniforms:{uColor:uniforms.uColor},transparent:true,blending:THREE.AdditiveBlending,depthWrite:false,side:THREE.BackSide});
      root.add(new THREE.Mesh(new THREE.SphereGeometry(1.28,48,32),glowMat));
      const rings=[];
      for(let i=0;i<4;i++){
        const ring=new THREE.Mesh(new THREE.TorusGeometry(1.35+i*.12,.0045,6,160),
          new THREE.MeshBasicMaterial({color:0x299eff,transparent:true,opacity:i===0?.75:.22,blending:THREE.AdditiveBlending}));
        ring.rotation.set(Math.PI/2+.19+i*.21,.18+i*.19,i*.6);root.add(ring);rings.push(ring);
      }
      const points=[];
      for(let i=0;i<480;i++){
        const a=i*2.399963,b=Math.acos(1-2*(i+.5)/480),r=1.45+(i%7)*.045;
        points.push(r*Math.sin(b)*Math.cos(a),r*Math.cos(b)*.8,r*Math.sin(b)*Math.sin(a));
      }
      const particleGeo=new THREE.BufferGeometry();particleGeo.setAttribute('position',new THREE.Float32BufferAttribute(points,3));
      const particleMat=new THREE.PointsMaterial({color:0x74c6ff,size:.016,transparent:true,opacity:.6,blending:THREE.AdditiveBlending,depthWrite:false});
      const particles=new THREE.Points(particleGeo,particleMat);root.add(particles);
      const pulseRings=[];
      for(let i=0;i<3;i++){
        const ring=new THREE.Mesh(new THREE.TorusGeometry(1.55,.005,4,160),new THREE.MeshBasicMaterial({color:0x5abfff,transparent:true,opacity:0,blending:THREE.AdditiveBlending}));
        scene.add(ring);pulseRings.push(ring);
      }
      const resize=()=>{const w=parent.clientWidth||500,h=parent.clientHeight||500;renderer.setSize(w,h);camera.aspect=w/h;camera.updateProjectionMatrix();};
      ro=new ResizeObserver(resize);ro.observe(parent);resize();
      const reduce=window.matchMedia('(prefers-reduced-motion: reduce)');
      const started=performance.now();let level=0;
      const render=()=>{
        frame=requestAnimationFrame(render);
        if(document.hidden)return;
        const t=(performance.now()-started)/1000,{phase,audio}=live.current;
        const input=phase==='listening'?audio.input||0:phase==='speaking'?audio.output||0:0;
        level+=(input-level)*.3;
        const color=new THREE.Color(phase==='approval'?'#f5b861':phase==='listening'?'#4ee0d3':'#2c9cff');
        uniforms.uColor.value.lerp(color,.06);uniforms.uTime.value=reduce.matches?0:t;uniforms.uLevel.value=level;
        sphere.rotation.y=reduce.matches?0:t*.045;cage.rotation.y=-sphere.rotation.y*.5;
        particles.rotation.y=reduce.matches?0:t*(phase==='thinking'?.28:.035);
        particles.rotation.z=reduce.matches?0:Math.sin(t*.1)*.12;
        particleMat.opacity=phase==='thinking'?.9:.36;
        const scale=1+level*.1;root.scale.setScalar(scale);
        rings.forEach((ring,i)=>{ring.material.color.copy(uniforms.uColor.value);ring.rotation.z=reduce.matches?i*.5:t*(i%2?-.06:.08)+i*.5;ring.material.opacity=(i===0?.65:.15)+level*.25;});
        pulseRings.forEach((ring,i)=>{const p=((reduce.matches?0:t*.38)+i/3)%1;ring.scale.setScalar(1+p*.5+level*.16);ring.material.opacity=(1-p)*level*.55;ring.material.color.copy(uniforms.uColor.value);});
        renderer.render(scene,camera);
      };render();
      return ()=>{cancelAnimationFrame(frame);ro.disconnect();scene.traverse(o=>{o.geometry?.dispose();if(o.material){[].concat(o.material).forEach(m=>m.dispose());}});renderer.dispose();renderer.domElement.remove();};
    } catch(error) {renderer?.dispose();setFallback(true);}
  },[]);
  return <div className={`orb-render ${small?'small':''}`} ref={host}>{fallback&&<div className={`orb-fallback ${phase}`}><span/></div>}</div>;
}
