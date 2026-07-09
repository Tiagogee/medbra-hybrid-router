"""Medical Safety Guard — Constitution Art.2, non-negotiable.
No AI in this system may diagnose, prescribe, or promise locally-valid
prescriptions. Symptoms -> route to consultation. Emergency -> local services.
"""
import re

BLOCK_PATTERNS = [
    r"\bdiagn[oó]stic", r"\breceit(a|e)\b.*\b(v[aá]lid|local)", r"\bprescri\w+",
    r"\bqual\s+rem[eé]dio\b", r"\bque\s+rem[eé]dio\b", r"\bdosagem\b",
]
EMERGENCY_PATTERNS = [
    r"\bdor no peito\b", r"\bdesmai", r"\bsangramento intenso\b", r"\bfalta de ar\b",
    r"\bconvuls", r"\bavc\b", r"\binfarto\b", r"\bsu[ií]c[ií]d",
]
SYMPTOM_PATTERNS = [r"\bfebre\b", r"\bdor\b", r"\bsintoma", r"\benjoo\b", r"\bt[oô]ntur", r"\bmal[- ]estar\b"]

SAFE_FALLBACK = ("Posso te orientar sobre como funciona a MedBra, mas sintomas precisam "
                 "ser avaliados em consulta. Em caso de emergência, procure o serviço local imediatamente.")
EMERGENCY_MSG = ("⚠️ Isso pode ser uma emergência. Procure o serviço de emergência local AGORA (911 nos EUA). "
                 "A MedBra não substitui atendimento de emergência.")

def check(text: str) -> dict:
    t = text.lower()
    if any(re.search(p, t) for p in EMERGENCY_PATTERNS):
        return {"action": "emergency", "response": EMERGENCY_MSG, "escalate_human": True}
    if any(re.search(p, t) for p in BLOCK_PATTERNS):
        return {"action": "block", "response": SAFE_FALLBACK, "escalate_human": False}
    if any(re.search(p, t) for p in SYMPTOM_PATTERNS):
        return {"action": "escalate_model", "response": None, "escalate_human": False}
    return {"action": "allow", "response": None, "escalate_human": False}
