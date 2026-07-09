"""Model providers — swap-in architecture. Set env keys and everything works.
FIREWORKS_API_KEY=  -> FireworksProvider goes live
OLLAMA_HOST=        -> LocalGemmaProvider (AMD GPU / RTX local)
ANTHROPIC_API_KEY=  -> ClaudeProvider (escalation tier)
No keys? MockProvider keeps the whole pipeline runnable/demoable.
"""
from __future__ import annotations
import os, time, json
from dataclasses import dataclass, field

@dataclass
class Completion:
    text: str
    provider: str
    model: str
    input_tokens: int
    output_tokens: int
    latency_ms: float
    cost_usd: float
    confidence: float = 1.0  # provider self-reported (1-token judge)

# $/1M tokens (input, output) — update from provider pricing pages
PRICING = {
    "fireworks/gemma-2-9b-it":        (0.20, 0.20),
    "fireworks/llama-v3p1-8b":        (0.20, 0.20),
    "fireworks/llama-v3p1-70b":       (0.90, 0.90),
    "local/gemma":                    (0.0, 0.0),
    "anthropic/claude-sonnet":        (3.00, 15.00),
    "mock/tiny":                      (0.0, 0.0),
}

def _cost(model: str, tin: int, tout: int) -> float:
    pin, pout = PRICING.get(model, (1.0, 1.0))
    return (tin * pin + tout * pout) / 1_000_000

class BaseProvider:
    name = "base"
    model = "base/none"
    def available(self) -> bool: return False
    def complete(self, prompt: str, max_tokens: int = 256) -> Completion: raise NotImplementedError

class FireworksProvider(BaseProvider):
    """https://api.fireworks.ai — AMD-hosted models. Just set FIREWORKS_API_KEY."""
    name = "fireworks"
    def __init__(self, model: str = "accounts/fireworks/models/gemma2-9b-it"):
        self.key = os.getenv("FIREWORKS_API_KEY", "")
        self.model = f"fireworks/{model.split('/')[-1]}"
        self._endpoint = "https://api.fireworks.ai/inference/v1/chat/completions"
        self._raw_model = model
    def available(self) -> bool: return bool(self.key)
    def complete(self, prompt: str, max_tokens: int = 256) -> Completion:
        import requests
        t0 = time.time()
        r = requests.post(self._endpoint, timeout=60,
            headers={"Authorization": f"Bearer {self.key}"},
            json={"model": self._raw_model, "max_tokens": max_tokens,
                  "messages": [{"role": "user", "content": prompt}]})
        r.raise_for_status()
        d = r.json()
        usage = d.get("usage", {})
        tin, tout = usage.get("prompt_tokens", 0), usage.get("completion_tokens", 0)
        return Completion(d["choices"][0]["message"]["content"], self.name, self.model,
                          tin, tout, (time.time()-t0)*1000, _cost(self.model, tin, tout))

class LocalGemmaProvider(BaseProvider):
    """Ollama-compatible local inference (AMD GPU pod or RTX). Cost: $0."""
    name = "local-gemma"
    model = "local/gemma"
    def __init__(self, host: str | None = None, model: str = "gemma2:9b"):
        self.host = host or os.getenv("OLLAMA_HOST", "")
        self._m = model
    def available(self) -> bool: return bool(self.host)
    def complete(self, prompt: str, max_tokens: int = 256) -> Completion:
        import requests
        t0 = time.time()
        r = requests.post(f"{self.host}/api/generate", timeout=120,
                          json={"model": self._m, "prompt": prompt, "stream": False,
                                "options": {"num_predict": max_tokens}})
        r.raise_for_status()
        d = r.json()
        tin, tout = d.get("prompt_eval_count", 0), d.get("eval_count", 0)
        return Completion(d.get("response", ""), self.name, self.model,
                          tin, tout, (time.time()-t0)*1000, 0.0)

class ClaudeProvider(BaseProvider):
    """Escalation tier: complex reasoning + sensitive health conversations."""
    name = "claude"
    model = "anthropic/claude-sonnet"
    def __init__(self):
        self.key = os.getenv("ANTHROPIC_API_KEY", "")
    def available(self) -> bool: return bool(self.key)
    def complete(self, prompt: str, max_tokens: int = 512) -> Completion:
        import requests
        t0 = time.time()
        r = requests.post("https://api.anthropic.com/v1/messages", timeout=90,
            headers={"x-api-key": self.key, "anthropic-version": "2023-06-01"},
            json={"model": "claude-sonnet-4-5", "max_tokens": max_tokens,
                  "messages": [{"role": "user", "content": prompt}]})
        r.raise_for_status()
        d = r.json()
        u = d.get("usage", {})
        tin, tout = u.get("input_tokens", 0), u.get("output_tokens", 0)
        return Completion(d["content"][0]["text"], self.name, self.model,
                          tin, tout, (time.time()-t0)*1000, _cost(self.model, tin, tout))

class MockProvider(BaseProvider):
    """Keeps the pipeline demoable with zero keys (CI, offline, judges)."""
    name = "mock"
    model = "mock/tiny"
    def __init__(self, canned: dict | None = None):
        self.canned = canned or {}
    def available(self) -> bool: return True
    def complete(self, prompt: str, max_tokens: int = 256) -> Completion:
        time.sleep(0.02)
        for k, v in self.canned.items():
            if k.lower() in prompt.lower():
                return Completion(v, self.name, self.model, len(prompt)//4, len(v)//4, 20.0, 0.0)
        return Completion("MOCK: intent=info_preco confidence=0.93", self.name, self.model,
                          len(prompt)//4, 12, 20.0, 0.0)
