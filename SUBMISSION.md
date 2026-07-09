# 📤 Submission Pack — MedBra AI Labs

*AMD Developer Hackathon: ACT II · Track 3 (Unicorn) + Gemma-on-AMD · deadline Sat 11 Jul 16:00 UTC*

---

## lablab.ai form — copy/paste answers

**Project Title:** MedBra Hybrid Router — Token-Efficient AI for Portuguese-Speaking Healthcare

**Short Description (≤ ~200 chars):**
An AI orchestration platform that routes medical conversations between local and cloud LLMs — cutting inference cost ~84% while never compromising clinical safety. Live telemedicine, real patients.

**Team Idea (replace the wrong "logistics" one):**
> An AI orchestration platform for Portuguese-speaking healthcare that intelligently routes medical conversations between local and cloud language models, reducing inference cost while maintaining clinical quality and enabling scalable telemedicine for Brazilian communities abroad.

**Long Description:** → use README.md (problem, solution, AMD/Fireworks usage, roadmap)

**Technology tags:** Fireworks AI, Gemma, AMD Developer Cloud, ROCm, Python, Docker, LLM routing, Healthcare, Telemedicine

**Category:** Track 3 — Unicorn (build your startup) · eligible for Gemma-on-AMD ($2,000)

**GitHub:** https://github.com/tiagogee21065/medbra-hybrid-router *(public, MIT, README with run instructions)*

**Demo/App URL:** container — `docker run medbra-router` (or live Bia on WhatsApp, post-Meta unblock)

---

## 🎬 Video script (2 min — record screen + voice, or CEO on camera 20s intro)

**[0:00–0:20] Hook + who we are** *(CEO or voiceover over MedBra reel)*
> "4 million Brazilians live abroad. When they get sick in the US, a simple visit costs up to $2,000 — so they wait, and suffer. MedBra fixes that: a $39 consultation with a Brazilian doctor, in Portuguese. We're already live — real patients, real payments."

**[0:20–0:45] The problem we hit** *(screen: architecture diagram)*
> "But every patient message was hitting a frontier model. Like sending 'how much does it cost?' to a senior physician. Expensive and slow — yet you can NEVER cut corners on safety. So we built a router."

**[0:45–1:20] The solution — live demo** *(terminal: `python demo.py`)*
> "Watch. A price question → handled by the cheapest tier, near-zero cost. A symptom → the router FORCES the top tier; we optimize FAQs, never care. And an emergency? Zero tokens — a deterministic guard sends them to 911 instantly. Local first, tokens last, safety always."

**[1:20–1:45] AMD + Fireworks + the numbers** *(terminal: `python benchmark/cost_model.py`)*
> "Local Gemma runs free on the AMD GPU pod. Fireworks serves our volume tier on AMD hardware. The result: an 84% cut in inference cost — nearly $10,000 a year at scale — with clinical quality intact."

**[1:45–2:00] The vision** *(slide: country modules)*
> "This router is the brain of our AI attendant, Bia. Same core, per-country modules — Portugal, Canada, next. We're not building a demo. We're building an operating system for Portuguese-speaking healthcare. Wherever there's a Brazilian, there's a Brazilian doctor."

---

## 🖼️ Slides (6, MedBra identity — teal #0B2E36 / green #0E6E5C / coral #FF6A3D CTA)

1. **Title** — logo + "MedBra Hybrid Router" + "AI orchestration for Portuguese-speaking healthcare" + Team MedBra AI Labs
2. **Problem** — "$500–$2,000 per visit · 4.5M Brazilians abroad · they wait and suffer" (photo: the $1,847 bill reel frame)
3. **Solution** — the routing diagram (safety → local → fireworks → claude), "Local first · Tokens last · Safety always"
4. **Live demo** — screenshot of `demo.py` output: price(cheap) / symptom(top tier) / emergency(0 tokens)
5. **Impact** — the cost table: 84% cut · ~$10k/yr at scale · "we optimize FAQs, never care" · AMD+Fireworks logos
6. **Vision + traction** — "already live: Stripe, doctors, patients" + country-module roadmap + "Onde tiver um brasileiro, tem um médico brasileiro"

---

## ✅ Pre-submit checklist
- [x] Prototype runs (mock tier, zero keys) · 3/3 tests
- [x] README (repositioned, Aion pitch) · Dockerfile · MIT
- [x] Cost model + benchmark harness
- [ ] `FIREWORKS_API_KEY` + `OLLAMA_HOST` injected → live tiers (optional for demo, strong for judging)
- [ ] GitHub repo public (needs `gh auth login` — CEO, one screen)
- [ ] Video recorded (script above)
- [ ] Slides exported to PDF
- [ ] Form submitted on lablab.ai + Team Idea corrected
