from router import HybridRouter
from router.providers import MockProvider

def test_safety_blocks_prescription():
    r = HybridRouter(providers=[MockProvider()])
    out = r.route("que remedio posso tomar para febre?")
    assert out["path"][0].startswith("safety:block")
    assert "consulta" in out["response"]

def test_emergency_escalates_human():
    r = HybridRouter(providers=[MockProvider()])
    out = r.route("estou com dor no peito e falta de ar")
    assert out["escalate_human"] is True

def test_cheap_path_for_price_question():
    r = HybridRouter(providers=[MockProvider()])
    out = r.route("quanto custa a consulta?")
    assert out["total_cost_usd"] == 0.0
    assert out["chosen"] == "mock"

if __name__ == "__main__":
    test_safety_blocks_prescription(); test_emergency_escalates_human(); test_cheap_path_for_price_question()
    print("3/3 PASS")
