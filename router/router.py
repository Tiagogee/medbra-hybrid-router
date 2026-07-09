"""HybridRouter — the core: route each task to the CHEAPEST model that is
still accurate enough. Local-first, tokens-last, safety-always.

Pipeline per message:
  1. MedicalSafetyGuard (regex, 0 tokens) — block/emergency/escalate
  2. Tier-0 classify (cheapest available: local -> fireworks-small -> mock)
  3. 1-token judge: cheap model reports confidence; below threshold -> escalate tier
  4. Escalation ceiling: Claude for complex/sensitive (health = never economized)
Every hop logged: tokens, cost, latency -> benchmark & learning loop.
"""
from __future__ import annotations
import json, time
from dataclasses import asdict
from . import safety
from .providers import BaseProvider, FireworksProvider, LocalGemmaProvider, ClaudeProvider, MockProvider

CLASSIFY_PROMPT = (
    "Classifique a intenção da mensagem de um brasileiro nos EUA falando com a MedBra "
    "(telemedicina em português). Responda APENAS JSON: "
    '{"intent": "preco|como_funciona|receita|urgencia|suporte|outro", "confidence": 0.0-1.0}\n'
    "Mensagem: {msg}"
)

class HybridRouter:
    def __init__(self, providers: list[BaseProvider] | None = None,
                 confidence_threshold: float = 0.80):
        if providers is None:
            providers = [LocalGemmaProvider(), FireworksProvider(), ClaudeProvider(), MockProvider()]
        # cheap -> expensive, only the available ones
        self.tiers = [p for p in providers if p.available()]
        self.threshold = confidence_threshold
        self.log: list[dict] = []

    def route(self, message: str, max_escalations: int = 2) -> dict:
        t0 = time.time()
        # 1) safety first — zero tokens
        s = safety.check(message)
        if s["action"] in ("block", "emergency"):
            out = {"path": [f"safety:{s['action']}"], "response": s["response"],
                   "escalate_human": s["escalate_human"], "total_cost_usd": 0.0,
                   "total_tokens": 0, "latency_ms": (time.time()-t0)*1000}
            self.log.append(out); return out

        force_top = s["action"] == "escalate_model"  # symptoms -> best model, always
        path, cost, tokens = [], 0.0, 0
        tiers = self.tiers[-1:] if force_top and len(self.tiers) > 1 else self.tiers

        for i, p in enumerate(tiers):
            c = p.complete(CLASSIFY_PROMPT.replace("{msg}", message), max_tokens=64)
            cost += c.cost_usd; tokens += c.input_tokens + c.output_tokens
            conf = _extract_confidence(c.text)
            path.append(f"{p.name}({c.model.split('/')[-1]}) conf={conf:.2f} ${c.cost_usd:.6f}")
            if conf >= self.threshold or i >= max_escalations or i == len(tiers) - 1:
                out = {"path": path, "response": c.text, "escalate_human": False,
                       "chosen": p.name, "confidence": conf,
                       "total_cost_usd": round(cost, 6), "total_tokens": tokens,
                       "latency_ms": round((time.time()-t0)*1000, 1),
                       "forced_top_tier": force_top}
                self.log.append(out); return out
        return {"path": path, "response": None, "error": "no providers"}

def _extract_confidence(text: str) -> float:
    try:
        j = json.loads(text[text.index("{"): text.rindex("}") + 1])
        return float(j.get("confidence", 0.5))
    except Exception:
        import re
        m = re.search(r"confidence[\"'=:\s]+([01]\.\d+|\d\.\d+)", text)
        return float(m.group(1)) if m else 0.5
