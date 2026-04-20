#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import argparse


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
    parser = argparse.ArgumentParser(description="Validate a governed data repository using snapshot + override structure.")
    parser.add_argument("target_vault", help="Path to the governed data vault")
    args = parser.parse_args()
    root = Path(args.target_vault).resolve()

    required = [
        root / "RULES.md",
        root / ".dbms-system" / "RULES.md",
        root / ".dbms-system" / "Interfaces" / "20-Task-Types.md",
        root / ".dbms-system" / "Planning" / "20-Three-Planes.md",
        root / ".dbms-system" / "DBMS" / "00-System-Data-Isolation.md",
        root / ".dbms-system" / "version.json",
        root / "LocalOverrides" / "00-本地覆盖说明.md",
        root / "LocalOverrides" / "compatibility-status.json",
        root / ".knowledge-registry" / "vault-registry.json",
        root / ".knowledge-registry" / "agent-roster.json",
        root / ".knowledge-registry" / "promotion-queue.json",
        root / ".knowledge-registry" / "change-ledger.jsonl",
        root / "01-Workflow" / "Knowledge-Governance" / "DBMS" / "index" / "file-index.jsonl",
        root / "01-Workflow" / "Knowledge-Governance" / "DBMS" / "index" / "topic-summary.json",
        root / "01-Workflow" / "Knowledge-Governance" / "DBMS" / "index" / "findings.json",
        root / "01-Workflow" / "Knowledge-Governance" / "DBMS" / "state" / "last-index-run.json",
    ]

    missing = [str(p) for p in required if not p.exists()]
    if missing:
        fail(f"missing required data repo files: {missing}")

    for p in [
        root / ".dbms-system" / "version.json",
        root / "LocalOverrides" / "compatibility-status.json",
        root / ".knowledge-registry" / "vault-registry.json",
        root / ".knowledge-registry" / "agent-roster.json",
        root / ".knowledge-registry" / "promotion-queue.json",
        root / "01-Workflow" / "Knowledge-Governance" / "DBMS" / "index" / "topic-summary.json",
        root / "01-Workflow" / "Knowledge-Governance" / "DBMS" / "index" / "findings.json",
        root / "01-Workflow" / "Knowledge-Governance" / "DBMS" / "state" / "last-index-run.json",
    ]:
        parse_json(p)

    parse_jsonl(root / ".knowledge-registry" / "change-ledger.jsonl")
    parse_jsonl(root / "01-Workflow" / "Knowledge-Governance" / "DBMS" / "index" / "file-index.jsonl")
    print("VALIDATE_DATA_REPO_OK")


if __name__ == "__main__":
    main()
