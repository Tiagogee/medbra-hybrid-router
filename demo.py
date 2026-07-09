"""Demo CLI — runs with ZERO keys (mock tier) or live keys when injected.
$ python demo.py "quanto custa a consulta?"
"""
import sys, json
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from router import HybridRouter
from router.providers import MockProvider

msgs = sys.argv[1:] or [
    "quanto custa a consulta?",
    "meu filho esta com febre alta, o que eu faco?",
    "estou com dor no peito e falta de ar",
    "que remedio posso tomar para dor de cabeca?",
]
r = HybridRouter()
print(f"tiers ativos: {[p.name for p in r.tiers]}\n" + "=" * 60)
for m in msgs:
    out = r.route(m)
    print(f"\n>> {m}")
    print(json.dumps(out, indent=2, ensure_ascii=False))
