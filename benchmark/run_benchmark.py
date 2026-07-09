"""Benchmark: same tasks -> every available provider. Outputs tokens/cost/latency table.
Feeds the MedBra Cost-Intelligence matrix with DATA instead of opinion."""
import json, statistics, sys
sys.path.insert(0, "..") if "benchmark" in __file__ else None
from router.providers import FireworksProvider, LocalGemmaProvider, ClaudeProvider, MockProvider

TASKS = [json.loads(l) for l in open(__file__.replace("run_benchmark.py", "tasks.jsonl"), encoding="utf-8")]

def run():
    provs = [p for p in (LocalGemmaProvider(), FireworksProvider(), ClaudeProvider(), MockProvider()) if p.available()]
    print(f"{'provider':<14}{'ok':<5}{'avg_ms':<9}{'tokens':<8}{'cost_usd':<10}")
    for p in provs:
        lat, tok, cost, ok = [], 0, 0.0, 0
        for t in TASKS:
            try:
                c = p.complete(t["prompt"], max_tokens=64)
                lat.append(c.latency_ms); tok += c.input_tokens + c.output_tokens; cost += c.cost_usd
                if t.get("expect", "") in c.text.lower(): ok += 1
            except Exception:
                pass
        print(f"{p.name:<14}{ok}/{len(TASKS):<4}{statistics.mean(lat) if lat else 0:<9.0f}{tok:<8}{cost:<10.6f}")

if __name__ == "__main__":
    run()
