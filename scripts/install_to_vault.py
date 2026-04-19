#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_ROOT = ROOT / "templates" / "vault-root"


def copy_tree(src: Path, dst: Path) -> None:
    if src.exists():
        shutil.copytree(src, dst, dirs_exist_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Install the governance kit templates into a target vault.")
    parser.add_argument("target_vault", help="Path to the target vault")
    parser.add_argument("--with-snapshot", action="store_true", help="Also sync the system snapshot into .dbms-system")
    args = parser.parse_args()

    target = Path(args.target_vault).resolve()
    target.mkdir(parents=True, exist_ok=True)
    copy_tree(TEMPLATE_ROOT, target)

    if args.with_snapshot:
        from sync_system_snapshot import sync_snapshot  # local import
        sync_snapshot(target)

    print(f"INSTALLED_TO_VAULT\t{target}")


if __name__ == "__main__":
    main()
