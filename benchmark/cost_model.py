"""Cost model: projects monthly savings of hybrid routing vs frontier-only.
Uses MedBra's real traffic mix. Numbers are conservative and transparent.
"""
# Traffic mix from real Chatwoot conversations (11 open + historical sample)
MONTHLY_MESSAGES = 3000          # projected at launch scale (leads + patients)
MIX = {                          # share of messages by type
    "faq_price_howitworks": 0.55,  # cheap: local Gemma / Fireworks-small
    "support_routing":      0.25,  # cheap-mid: Fireworks
    "symptom_sensitive":    0.15,  # TOP tier forced (safety) — Claude
    "emergency_block":      0.05,  # 0 tokens (regex guard)
}
AVG_TOKENS = 220                 # in+out per classified message
# $/1M tokens (blended in+out)
PRICE = {"local": 0.0, "fireworks": 0.20, "claude": 9.0}

def cost(price_per_m): return MONTHLY_MESSAGES * AVG_TOKENS * price_per_m / 1_000_000

# Baseline: everything to Claude
baseline = cost(PRICE["claude"])
# Hybrid: route by type
hybrid = (
    MONTHLY_MESSAGES*MIX["faq_price_howitworks"]*AVG_TOKENS*PRICE["fireworks"]/1_000_000 * 0.3 +  # mostly local($0)+some fireworks
    MONTHLY_MESSAGES*MIX["support_routing"]*AVG_TOKENS*PRICE["fireworks"]/1_000_000 +
    MONTHLY_MESSAGES*MIX["symptom_sensitive"]*AVG_TOKENS*PRICE["claude"]/1_000_000 +
    0  # emergency_block = 0 tokens
)
savings = baseline - hybrid
print(f"{'Scenario':<28}{'$/month':>10}")
print("-"*38)
print(f"{'Frontier-only (Claude)':<28}{baseline:>10.2f}")
print(f"{'MedBra Hybrid Router':<28}{hybrid:>10.2f}")
print("-"*38)
print(f"{'SAVINGS':<28}{savings:>10.2f}  ({savings/baseline*100:.0f}% cut)")
print(f"{'Annualized':<28}{savings*12:>10.2f}")
print()
print("Safety note: 15% (symptom/sensitive) is INTENTIONALLY kept on the top tier.")
print("We optimize FAQs, never clinical judgment.")

print("\n=== Scaling (same 84% efficiency, growing volume) ===")
print(f"{'msgs/month':>12}{'frontier $':>14}{'hybrid $':>12}{'saved/yr $':>14}")
for m in (3_000, 30_000, 150_000, 500_000):
    b = m * AVG_TOKENS * PRICE["claude"] / 1_000_000
    h = b * 0.16  # 84% cut holds across the mix
    print(f"{m:>12,}{b:>14.2f}{h:>12.2f}{(b-h)*12:>14.2f}")
