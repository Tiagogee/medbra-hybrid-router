# MedBra Hybrid Router 🇧🇷🏥

**An AI orchestration platform for Portuguese-speaking healthcare that intelligently routes medical conversations between local and cloud language models — reducing inference cost while preserving clinical safety, enabling scalable telemedicine for Brazilian communities abroad.**

Built by [MedBra](https://medbra.tech) — a *live* telemedicine startup (real patients, real Stripe payments, doctors on screen in <30 min).

*AMD Developer Hackathon: ACT II — Team MedBra AI Labs (Track 3: Unicorn / Gemma on AMD)*

---

## The Problem

4.5M+ Brazilians live abroad. In the US, a simple urgent-care visit costs $500–$2,000 — so they postpone care, self-diagnose, or suffer through symptoms in a language they don't fully master. MedBra sells $39 consultations with Brazilian doctors, in Portuguese, **already live in production** (Stripe → activation → doctor on screen in under 30 minutes).

Our bottleneck: every patient conversation was hitting a frontier LLM. That's like sending every "how much does it cost?" to a senior physician. Expensive, slow, unnecessary — **but you can never economize on safety.**

## The Solution: route by risk and cost, never by hype

```
Patient message
   │
   ├─ 0️⃣  Medical Safety Guard (regex, 0 tokens, 0 ms)
   │      emergency → 911 guidance + human escalation
   │      prescription/diagnosis ask → safe refusal (compliance)
   │
   ├─ 1️⃣  Local Gemma (AMD GPU / Ollama)          $0.00
   ├─ 2️⃣  Fireworks (Gemma-2 / Llama, AMD-hosted)  ~$0.20/1M
   │      └─ 1-token confidence judge: below threshold → escalate
   └─ 3️⃣  Claude (complex + sensitive health)      only when trust runs out
```

**Local first. Tokens last. Safety always.**

## What makes it different

- **Not a demo — a company.** This router is the v2 brain of "Bia", MedBra's WhatsApp attendant, plugged into a live Stripe → n8n → CRM pipeline with real paying patients.
- **Safety tier costs zero tokens.** Emergencies and prescription requests never reach a model at all — deterministic guardrails first (our "Constitution Art. 2").
- **Symptoms force the TOP tier.** Cost optimization inverts when health risk appears: `forced_top_tier=true`. We save on FAQs, never on care.
- **Key-injection architecture.** Set `FIREWORKS_API_KEY` and the Fireworks tier goes live; set `OLLAMA_HOST` and local Gemma joins. No code changes. `MockProvider` keeps everything runnable with zero keys (try it right now).
- **Every hop measured.** Tokens, cost, latency logged per request → feeds our internal Cost-Intelligence matrix (data, not opinion).

## Quickstart (zero keys needed)

```bash
pip install -r requirements.txt
python demo.py                       # 4 real scenarios, mock tier
python tests/test_router.py          # 3/3 safety tests
python benchmark/run_benchmark.py    # per-provider tokens/cost/latency
```

```bash
docker build -t medbra-router . && docker run medbra-router
```

Go live: copy `.env.example` → `.env`, paste keys. Done.

## AMD & Fireworks usage

- **Fireworks AI** hosts our volume tier (Gemma-2-9B, Llama-3.1-8B) on AMD hardware — the cheapest model that still clears the accuracy threshold gets the job.
- **AMD GPU pod / Developer Cloud** runs the $0 local Gemma tier (Ollama-compatible endpoint) for classification and pre-triage.
- Benchmark harness compares local-AMD vs Fireworks vs frontier per task type.

## Roadmap

1. **Now**: router powering Bia's lead triage (intent → price/receita/urgency/support)
2. **Next**: full conversation memory tier + Chatwoot human-loop integration (built)
3. **Then**: country modules — same core, per-country prescription/payment rules (Portugal, Canada...)
4. **Vision**: an operating system for Portuguese-speaking healthcare access, worldwide

## Team

**MedBra AI Labs** — Tiago (founder/CEO) + Axis (AI CTO). Criciúma, Brazil → Orlando, USA → the world.

> *"Onde tiver um brasileiro, tem um médico brasileiro."*
> (Wherever there's a Brazilian, there's a Brazilian doctor.)

MIT License
