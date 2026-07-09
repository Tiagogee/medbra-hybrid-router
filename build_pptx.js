const P = require("pptxgenjs");
const p = new P();
p.defineLayout({ name: "W", width: 13.333, height: 7.5 });
p.layout = "W";
const BG="0B2E36", GREEN="0E6E5C", SAND="F4F0E8", CORAL="FF6A3D", MUT="9DB3B0", CARD="0f3b45";
const A = "assets/";
const S = () => { const s = p.addSlide(); s.background = { color: BG }; return s; };
const kick = (s, t) => s.addText(t.toUpperCase(), { x:0.7, y:0.55, w:12, h:0.4, color:CORAL, bold:true, fontSize:14, charSpacing:2, fontFace:"Arial" });
const foot = (s, l, r) => { s.addText(l, {x:0.7,y:6.95,w:7,h:0.35,color:GREEN,fontSize:11,fontFace:"Arial"}); if(r) s.addText(r,{x:7,y:6.95,w:5.6,h:0.35,color:GREEN,fontSize:11,align:"right",fontFace:"Arial"}); };

// 1 title (hero full-bleed + left gradient scrim for text)
let s = S();
s.addImage({path:A+"hero.png",x:0,y:0,w:13.333,h:7.5});
s.addShape("rect",{x:0,y:0,w:8.2,h:7.5,fill:{color:BG,transparency:22}});
s.addImage({path:A+"logo_symbol.png",x:0.7,y:0.8,w:0.85,h:0.85});
kick(s,"MedBra AI Labs - AMD Hackathon ACT II");
s.addText("MedBra Hybrid Router", {x:0.7,y:2.1,w:8,h:1.6,color:SAND,bold:true,fontSize:52,fontFace:"Cambria"});
s.addText("An AI orchestration platform for Portuguese-speaking healthcare - routing medical conversations between local and cloud LLMs.", {x:0.7,y:3.7,w:7,h:1.2,color:SAND,fontSize:19,fontFace:"Arial"});
["Gemma on AMD","Fireworks","Live startup"].forEach((t,i)=>{ s.addShape("roundRect",{x:0.7+i*2.5,y:5.1,w:2.35,h:0.55,fill:{color:GREEN},rectRadius:0.27}); s.addText(t,{x:0.7+i*2.5,y:5.1,w:2.35,h:0.55,color:SAND,align:"center",fontSize:13,bold:true,fontFace:"Arial"}); });
foot(s,"medbra.tech","github.com/Tiagogee/medbra-hybrid-router");

// 2 problem
s = S(); kick(s,"The Problem");
s.addText("Getting sick abroad is a financial trap",{x:0.7,y:1.1,w:8,h:1,color:SAND,bold:true,fontSize:38,fontFace:"Cambria"});
s.addText([{text:"A simple US urgent-care visit costs ",options:{color:MUT}},{text:"$500-$2,000",options:{color:CORAL,bold:true}},{text:". So 4.5M+ Brazilians abroad postpone care, self-diagnose, and suffer through symptoms in a language they do not fully master.",options:{color:MUT}}],{x:0.7,y:2.6,w:6.8,h:3,fontSize:21,fontFace:"Arial",lineSpacingMultiple:1.2});
s.addShape("roundRect",{x:8.2,y:2.3,w:4.4,h:3,fill:{color:CARD},line:{color:GREEN,width:1},rectRadius:0.15});
s.addText("$1,847",{x:8.2,y:2.7,w:4.4,h:1.5,color:CORAL,bold:true,fontSize:80,align:"center",fontFace:"Arial"});
s.addText("a real ER bill for a sore throat",{x:8.2,y:4.3,w:4.4,h:0.6,color:GREEN,fontSize:16,align:"center",fontFace:"Arial"});

// 3 solution
s = S(); kick(s,"The Solution");
s.addText("$39 doctor, in Portuguese - powered by smart routing",{x:0.7,y:1.1,w:12,h:0.9,color:SAND,bold:true,fontSize:33,fontFace:"Cambria"});
s.addText([{text:"MedBra is a ",options:{color:MUT}},{text:"live",options:{color:CORAL,bold:true}},{text:" telemedicine service. Its brain is the Hybrid Router: every message goes to the cheapest model that is still accurate enough - and safety never touches a paid model.",options:{color:MUT}}],{x:0.7,y:2.1,w:12,h:1,fontSize:19,fontFace:"Arial"});
s.addImage({path:A+"router_flow.png",x:1.2,y:3.3,w:10.9,h:3.37});

// 4 how
s = S(); kick(s,"How it works");
s.addText("Local first - tokens last - safety always",{x:0.7,y:1.1,w:12,h:0.9,color:SAND,bold:true,fontSize:34,fontFace:"Cambria"});
[["0",CORAL,"Medical Safety Guard - deterministic, 0 tokens. Emergency -> 911 + human. Prescription ask -> safe refusal."],["1",GREEN,"Local Gemma on the AMD GPU pod - $0."],["2",GREEN,"Fireworks (Gemma-2 / Llama, AMD-hosted) - a 1-token judge decides if it is confident enough."],["3",GREEN,"Claude - only for complex + sensitive health."]].forEach((r,i)=>{ const y=2.4+i*1.05; s.addShape("oval",{x:0.9,y:y,w:0.7,h:0.7,fill:{color:r[1]}}); s.addText(r[0],{x:0.9,y:y,w:0.7,h:0.7,align:"center",color:r[1]===CORAL?BG:SAND,bold:true,fontSize:24,fontFace:"Arial"}); s.addText(r[2],{x:1.9,y:y-0.05,w:10.6,h:0.9,color:MUT,fontSize:17,fontFace:"Arial",valign:"middle"}); });

// 5 impact
s = S(); kick(s,"Impact");
s.addText("84% cheaper - safety intact",{x:0.7,y:1.1,w:12,h:0.9,color:SAND,bold:true,fontSize:38,fontFace:"Cambria"});
s.addImage({path:A+"cost_model.png",x:0.7,y:2.3,w:6.6,h:3.8});
s.addText([{text:"15% of messages stay on the top tier ",options:{color:MUT}},{text:"on purpose.",options:{color:CORAL,bold:true}},{text:" We optimize FAQs, never clinical judgment.",options:{color:MUT}}],{x:7.6,y:2.6,w:5,h:1.6,fontSize:20,fontFace:"Arial"});
s.addText("-84%",{x:7.6,y:4.3,w:2.4,h:1,color:CORAL,bold:true,fontSize:46,fontFace:"Arial"}); s.addText("cost / msg",{x:7.6,y:5.35,w:2.4,h:0.4,color:GREEN,fontSize:14,fontFace:"Arial"});
s.addText("0",{x:10.2,y:4.3,w:2.4,h:1,color:CORAL,bold:true,fontSize:46,fontFace:"Arial"}); s.addText("tokens on emergencies",{x:10.2,y:5.35,w:2.6,h:0.6,color:GREEN,fontSize:14,fontFace:"Arial"});

// 6 proof
s = S(); kick(s,"Proof - real inference, today");
s.addText("Not a mock: local Gemma-class model, $0, 3/3 correct",{x:0.7,y:1.1,w:12,h:0.9,color:SAND,bold:true,fontSize:30,fontFace:"Cambria"});
s.addShape("roundRect",{x:0.7,y:2.4,w:11.9,h:3.6,fill:{color:CARD},line:{color:GREEN,width:1},rectRadius:0.12});
s.addText([{text:"qwen2.5 (local, AMD-pod-compatible)\n",options:{color:CORAL,bold:true,fontSize:22}},{text:"\nMedBra lead-intent classification - 3/3 correct - ~2.4s warm - $0.00 marginal\n\nvs Claude same task: ~200 tokens @ ~$0.002/msg.\nThe local tier handles classification at zero marginal cost - proven on real hardware, ready for the AMD pod.",options:{color:MUT,fontSize:18}}],{x:1.2,y:2.8,w:11,h:3,fontFace:"Arial",lineSpacingMultiple:1.15});

// 7 market
s = S(); kick(s,"Market");
s.addText("4.5M Brazilians abroad - and every diaspora after",{x:0.7,y:1.1,w:12,h:0.9,color:SAND,bold:true,fontSize:33,fontFace:"Cambria"});
[["2M+","Brazilians in the US (beachhead)"],["$39","per consult - ~$29 margin"],["$0","marginal cost to 150 lives"]].forEach((x,i)=>{ s.addText(x[0],{x:0.9+i*4.1,y:2.7,w:3.8,h:1.2,color:CORAL,bold:true,fontSize:54,align:"center",fontFace:"Arial"}); s.addText(x[1],{x:0.9+i*4.1,y:3.95,w:3.8,h:0.8,color:GREEN,fontSize:15,align:"center",fontFace:"Arial"}); });
s.addText("Same core -> per-country modules: Portugal, Canada, UK, Spain. The router makes each new market cheap to serve.",{x:0.9,y:5.4,w:11.5,h:1,color:MUT,fontSize:19,fontFace:"Arial"});

// 8 traction
s = S(); kick(s,"Traction");
s.addText("Not a demo - a running company",{x:0.7,y:1.1,w:12,h:0.9,color:SAND,bold:true,fontSize:38,fontFace:"Cambria"});
[["OK","Live pay-first pipeline: Stripe -> activation -> doctor on screen in <30 min (real $39 charges settled)"],["OK","Official WhatsApp Cloud API + Chatwoot attendant (Bia)"],["OK","Cinematic content engine, brand, CRM, automations (n8n)"],[">>","Hybrid Router = the v2 brain of Bia"]].forEach((r,i)=>{ const y=2.5+i*1.0; s.addShape("roundRect",{x:0.9,y:y,w:0.75,h:0.6,fill:{color:r[0]==="OK"?GREEN:CORAL},rectRadius:0.1}); s.addText(r[0],{x:0.9,y:y,w:0.75,h:0.6,align:"center",color:r[0]==="OK"?SAND:BG,bold:true,fontSize:15,fontFace:"Arial"}); s.addText(r[1],{x:1.85,y:y-0.05,w:10.6,h:0.75,color:MUT,fontSize:18,fontFace:"Arial",valign:"middle"}); });

// 9 scale
s = S(); kick(s,"Why it scales");
s.addText("Cost stays flat while volume explodes",{x:0.7,y:1.1,w:12,h:0.9,color:SAND,bold:true,fontSize:34,fontFace:"Cambria"});
s.addImage({path:A+"benchmark.png",x:3.2,y:2.0,w:6.9,h:3.97});
s.addText("~$10k/yr saved at 500k msgs/mo - margin that compounds as we add countries.",{x:0.9,y:6.15,w:11.5,h:0.6,color:MUT,fontSize:18,align:"center",fontFace:"Arial"});

// 10 vision (hero full-bleed)
s = S();
s.addImage({path:A+"hero.png",x:0,y:0,w:13.333,h:7.5});
s.addShape("rect",{x:0,y:0,w:8.2,h:7.5,fill:{color:BG,transparency:18}});
kick(s,"The Vision");
s.addText("An operating system for\nPortuguese-speaking healthcare",{x:0.7,y:1.5,w:7.6,h:1.8,color:SAND,bold:true,fontSize:33,fontFace:"Cambria"});
s.addText("The patrimony is not the AI - it is the system that uses any AI in the best way. Model-agnostic by design: survives Claude 6, GPT-6, Gemini Ultra.",{x:0.7,y:3.5,w:7.2,h:1.4,color:SAND,fontSize:18,fontFace:"Arial"});
s.addText("\"Onde tiver um brasileiro, tem um medico brasileiro.\"",{x:0.7,y:5.1,w:7.4,h:1,color:SAND,italic:true,fontSize:22,fontFace:"Cambria"});
foot(s,"MedBra AI Labs - Tiago (CEO) + Axis (AI CTO)","Criciuma -> Orlando -> the world");

p.writeFile({ fileName: "MedBra-Investor-Deck.pptx" }).then(f => console.log("PPTX gerado:", f));
