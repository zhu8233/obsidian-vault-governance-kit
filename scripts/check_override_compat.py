#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Check local override compatibility against the system snapshot.")
    parser.add_argument("target_vault", help="Path to the governed data vault")
    args = parser.parse_args()

    root = Path(args.target_vault).resolve()
    version_file = root / ".dbms-system" / "version.json"
    compat_file = root / "LocalOverrides" / "compatibility-status.json"

    if not version_file.exists():
        raise SystemExit("FAIL: missing .dbms-system/version.json")
    if not compat_file.exists():
        raise SystemExit("FAIL: missing LocalOverrides/compatibility-status.json")

    version = json.loads(version_file.read_text(encoding="utf-8"))
    compat = json.loads(compat_file.read_text(encoding="utf-8"))

    result = {
        "snapshot_tag": version.get("release_tag"),
        "override_tag": compat.get("system_tag"),
        "status": "compatible" if version.get("release_tag") == compat.get("system_tag") else "review-needed",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
