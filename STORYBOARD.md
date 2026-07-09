# 🎬 Video Storyboard — 2:00 (single take, no improvisation)

Record: screen capture + voiceover. Assets ready in `assets/` and `web/`. Tom: calm, confident, founder.

| # | Time | Screen (what to show) | On-screen text | Narration (read verbatim) | Motion |
|---|---|---|---|---|---|
| 1 | 0:00–0:12 | MedBra reel frame ($1,847 bill) → logo | "MedBra" | "Four million Brazilians live abroad. When they get sick in the US, a simple visit can cost two thousand dollars. So they wait. And they suffer." | slow zoom on bill → cut to logo |
| 2 | 0:12–0:28 | `web/deck.html` slide 3 (solution) | "$39 · Portuguese · live" | "MedBra fixes that: a thirty-nine dollar consultation with a Brazilian doctor, in Portuguese. We're already live — real patients, real payments, a doctor on screen in under thirty minutes." | fade in |
| 3 | 0:28–0:45 | `web/index.html` — type "quanto custa?" click Route | highlight "FAQ → cheapest tier · $0" | "But every message hitting a frontier model is like sending 'how much does it cost' to a senior physician. So we built a router. A price question? Handled by the cheapest tier — near zero cost." | pipeline lights up L→R |
| 4 | 0:45–1:02 | web demo — click "meu filho tem febre" then "dor no peito" | "SYMPTOM → top tier" then "EMERGENCY → 0 tokens" | "A symptom? The router forces the top tier — we optimize FAQs, never care. An emergency? Zero tokens. A deterministic guard sends them straight to 911 and a human." | two quick routes, coral flashes |
| 5 | 1:02–1:20 | `assets/cost_model.png` then `benchmark.png` | "−84% · ~$10k/yr at scale" | "Local Gemma runs free on the AMD GPU pod. Fireworks serves our volume tier on AMD hardware. The result: an eighty-four percent cut in inference cost — nearly ten thousand dollars a year at scale — clinical quality intact." | bar grows, then line climbs |
| 6 | 1:20–1:38 | deck slide 8 (traction) | "Live: Stripe · WhatsApp · Bia" | "This isn't a demo. It's a running company — live payments, official WhatsApp, an AI attendant named Bia. The router is her new brain." | checklist ticks in |
| 7 | 1:38–2:00 | deck slide 10 (vision) + country modules | quote + "model-agnostic" | "Same core, one module per country — Portugal, Canada, next. The patrimony isn't the AI; it's the system that uses any AI best. It survives Claude 6, GPT-6, whatever comes. Wherever there's a Brazilian, there's a Brazilian doctor." | slow fade to logo |

**Tools to record:** OBS / Windows Game Bar (Win+G) / Loom. Resolution 1080p. Keep cursor visible on the web demo.
**Fallback if no time:** run `python demo.py` full-screen terminal and narrate steps 3–5 over it.
