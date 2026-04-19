#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
from pathlib import Path
import subprocess
import argparse
from datetime import datetime, timezone


ROOT = Path(__file__).resolve().parent.parent
CORE = ROOT / "core"


def repo_head() -> str | None:
    try:
        return subprocess.check_output(
            ["git", "-C", str(ROOT), "rev-parse", "HEAD"],
            text=True,
        ).strip()
    except Exception:
        return None


def latest_tag() -> str | None:
    try:
        return subprocess.check_output(
            ["git", "-C", str(ROOT), "describe", "--tags", "--abbrev=0"],
            text=True,
        ).strip()
    except Exception:
        return None


def repo_dirty() -> bool:
    try:
        output = subprocess.check_output(
            ["git", "-C", str(ROOT), "status", "--porcelain"],
            text=True,
        )
        return bool(output.strip())
    except Exception:
        return False


def sync_snapshot(target_vault: Path) -> Path:
    snapshot = target_vault / ".dbms-system"
    snapshot.mkdir(parents=True, exist_ok=True)

    # Clear known snapshot subtrees before replacing.
    for rel in ["Interfaces", "Planning", "DBMS", "RULES.md", "00-Agent-Onboarding.md", "skills-manifest.md"]:
        path = snapshot / rel
        if path.is_dir():
            shutil.rmtree(path)
        elif path.exists():
            path.unlink()

    shutil.copy2(CORE / "RULES.md", snapshot / "RULES.md")
    shutil.copy2(CORE / "00-Agent-Onboarding.md", snapshot / "00-Agent-Onboarding.md")
    shutil.copy2(CORE / "skills-manifest.md", snapshot / "skills-manifest.md")
    shutil.copytree(CORE / "Interfaces", snapshot / "Interfaces", dirs_exist_ok=True)
    shutil.copytree(CORE / "Planning", snapshot / "Planning", dirs_exist_ok=True)
    shutil.copytree(CORE / "DBMS", snapshot / "DBMS", dirs_exist_ok=True)

    version = {
        "system_repo": "obsidian-vault-governance-kit",
        "release_tag": latest_tag(),
        "source_commit": repo_head(),
        "source_dirty": repo_dirty(),
        "synced_at": datetime.now(timezone.utc).isoformat(),
    }
    (snapshot / "version.json").write_text(json.dumps(version, ensure_ascii=False, indent=2), encoding="utf-8")
    return snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync the system snapshot into a target data vault.")
    parser.add_argument("target_vault", help="Path to the governed data vault")
    args = parser.parse_args()
    snapshot = sync_snapshot(Path(args.target_vault).resolve())
    print(f"SNAPSHOT_SYNCED\t{snapshot}")


if __name__ == "__main__":
    main()
