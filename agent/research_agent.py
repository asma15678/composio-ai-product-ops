"""
Evidence-first Composio research agent scaffold.

The live version should connect discover_sources() to Composio's search/browser
tools. It intentionally returns UNKNOWN rather than guessing when evidence is absent.
"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
records=json.loads((ROOT/"data/research_snapshot.json").read_text())["records"]

def discover_sources(app):
    return [
        f"{app['app']} official developer documentation authentication",
        f"{app['app']} official API reference",
        f"{app['app']} official pricing developer access",
        f"{app['app']} official MCP server",
    ]

def run():
    out=[]
    for r in records:
        out.append({**r,"research_queries":discover_sources(r),"run_status":"snapshot"})
    (ROOT/"data/agent_run.json").write_text(json.dumps(out,indent=2))
    print(f"Prepared {len(out)} records.")
if __name__=="__main__":
    run()
