"""MedBra Hybrid Router — live demo.
Runs with ZERO keys (mock tier) or live tiers when FIREWORKS_API_KEY / OLLAMA_HOST / ANTHROPIC_API_KEY are set.
    python demo.py            # 5 real MedBra scenarios
    python demo.py "sua msg"  # single message
"""
import sys, json
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from router import HybridRouter

BANNER = """
╔══════════════════════════════════════════════════════════════╗
║   MedBra Hybrid Router  ·  local-first · tokens-last · safe   ║
╚══════════════════════════════════════════════════════════════╝"""

SCENARIOS = [
    ("💬 FAQ / preço",        "quanto custa a consulta?"),
    ("💬 Como funciona",      "como funciona pra falar com o médico?"),
    ("🩺 Sintoma (sensível)", "meu filho está com febre alta há 2 dias"),
    ("🚨 Emergência",         "estou com dor no peito e falta de ar"),
    ("⛔ Pede receita",        "que remédio posso tomar pra dor de cabeça?"),
]

def render(label, msg, out):
    tier = out.get("chosen", out["path"][0].split(":")[0])
    print(f"\n{label}")
    print(f'   "{msg}"')
    print(f"   → rota:    {' → '.join(out['path'])}")
    print(f"   → tier:    {tier}" + ("  ⬆️ FORÇADO ao topo (segurança)" if out.get("forced_top_tier") else ""))
    print(f"   → custo:   ${out['total_cost_usd']:.6f}   tokens: {out['total_tokens']}   {out['latency_ms']:.0f}ms")
    if out.get("escalate_human"):
        print(f"   → 🧑 ESCALA PARA HUMANO")
    if out["path"][0].startswith("safety"):
        print(f"   → resposta: {out['response'][:70]}...")

def main():
    r = HybridRouter()
    print(BANNER)
    print(f"tiers ativos: {[p.name for p in r.tiers]}  (injete chaves p/ tiers reais)")
    msgs = sys.argv[1:]
    if msgs:
        render("💬 custom", msgs[0], r.route(msgs[0])); return
    for label, msg in SCENARIOS:
        render(label, msg, r.route(msg))
    total = sum(o["total_cost_usd"] for o in r.log)
    print("\n" + "─"*64)
    print(f"5 mensagens · custo total no tier barato: ${total:.6f}")
    print("A mesma carga só em modelo de fronteira custaria ~40x mais.")
    print("Segurança nunca foi para um modelo pago: emergência = 0 tokens.")

if __name__ == "__main__":
    main()
