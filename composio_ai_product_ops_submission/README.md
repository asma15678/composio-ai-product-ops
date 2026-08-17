# Composio AI Product Ops Intern — Take-Home

## Deliverables
- `output/index.html` — self-explanatory case study
- `data/research_snapshot.json` — 100 structured app records
- `agent/research_agent.py` — evidence-first research-agent scaffold
- `agent/verifier.py` — stratified verification sampler
- `README.md` — run instructions and methodology

## Method
The dataset uses official developer/documentation URLs and conservative classifications.
The key separation is:
1. API existence
2. credential accessibility
3. API breadth
4. MCP status
5. buildability

## Accuracy / honesty
The snapshot is prepared research, not a fabricated claim that 100 live browser sessions
were executed in this environment. The HTML explicitly marks the final human verification
pass as pending. Before submission, run the live agent and manually verify a stratified
sample. Report supported, contradicted and unresolved claims and calculate accuracy only
from resolved claims.

## Run
```bash
python agent/research_agent.py
python agent/verifier.py
```

## Deployment
Deploy `output/index.html` with GitHub Pages, Netlify or Vercel. The page is standalone.
