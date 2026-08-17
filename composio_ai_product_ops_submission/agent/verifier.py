"""
Verification loop.
Sample records across categories and failure modes, then manually compare each
claim with the linked evidence. Do not publish accuracy until the check is complete.
"""
import json, random
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
rows=json.loads((ROOT/"data/research_snapshot.json").read_text())["records"]
random.seed(42)
chosen=[]
for cat in sorted({r["category"] for r in rows}):
    chosen.append(random.choice([r for r in rows if r["category"]==cat]))
remaining=[r for r in rows if r not in chosen]
chosen += random.sample(remaining,10)
print(json.dumps(chosen[:20],indent=2))
print("\nStatus: HUMAN VERIFICATION REQUIRED")
