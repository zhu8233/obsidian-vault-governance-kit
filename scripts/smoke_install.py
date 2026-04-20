#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_ROOT = ROOT / "templates" / "vault-root"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def parse_json(path: Path) -> None:
    with path.open("r", encoding="utf-8") as fh:
        json.load(fh)


def parse_jsonl(path: Path) -> None:
    with path.open("r", encoding="utf-8") as fh:
        for idx, line in enumerate(fh, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                json.loads(line)
            except json.JSONDecodeError as exc:
                fail(f"invalid JSONL at {path} line {idx}: {exc}")


def main() -> None:
    if len(sys.argv) > 1:
        target = Path(sys.argv[1]).resolve()
    else:
        target = ROOT.parent / "obsidian-vault-governance-kit-smoke-vault"

    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True, exist_ok=True)

    shutil.copytree(TEMPLATE_ROOT, target, dirs_exist_ok=True)

    required = [
        target / "RULES.md",
        target / "CLAUDE.md",
        target / "AGENTS.md",
        target / "GEMINI.md",
        target / ".knowledge-registry" / "vault-registry.json",
        target / ".knowledge-registry" / "agent-roster.json",
        target / ".knowledge-registry" / "promotion-queue.json",
        target / ".knowledge-registry" / "change-ledger.jsonl",
        target / "01-Workflow" / "Knowledge-Governance" / "00-Agent-Onboarding.md",
        target / "01-Workflow" / "Knowledge-Governance" / "DBMS" / "index" / "file-index.jsonl",
        target / "01-Workflow" / "Knowledge-Governance" / "DBMS" / "index" / "topic-summary.json",
        target / "01-Workflow" / "Knowledge-Governance" / "DBMS" / "index" / "findings.json",
        target / "01-Workflow" / "Knowledge-Governance" / "DBMS" / "state" / "last-index-run.json",
    ]

    missing = [str(p) for p in required if not p.exists()]
    if missing:
        fail(f"missing files after install: {missing}")

    for json_file in [
        target / ".knowledge-registry" / "vault-registry.json",
        target / ".knowledge-registry" / "agent-roster.json",
        target / ".knowledge-registry" / "promotion-queue.json",
        target / "01-Workflow" / "Knowledge-Governance" / "DBMS" / "index" / "topic-summary.json",
        target / "01-Workflow" / "Knowledge-Governance" / "DBMS" / "index" / "findings.json",
        target / "01-Workflow" / "Knowledge-Governance" / "DBMS" / "state" / "last-index-run.json",
    ]:
        parse_json(json_file)

    parse_jsonl(target / ".knowledge-registry" / "change-ledger.jsonl")
    parse_jsonl(target / "01-Workflow" / "Knowledge-Governance" / "DBMS" / "index" / "file-index.jsonl")

    rules_text = (target / "RULES.md").read_text(encoding="utf-8")
    onboarding_text = (target / "01-Workflow" / "Knowledge-Governance" / "00-Agent-Onboarding.md").read_text(encoding="utf-8")
    if "RULES.md" not in rules_text:
        fail("installed RULES.md does not mention itself")
    if ".knowledge-registry/vault-registry.json" not in onboarding_text:
        fail("onboarding file does not require reading the vault registry")

    print(f"SMOKE_INSTALL_OK\t{target}")


if __name__ == "__main__":
    main()
