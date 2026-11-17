#!/usr/bin/env python3
"""Install the `cheat` command without pip or third-party build tooling."""

from __future__ import annotations

import argparse
import os
import shutil
import site
import stat
import sys
from pathlib import Path


def default_bin_dir() -> Path:
    """Return the conventional per-user executable directory for this OS."""
    if os.name == "nt":
        return Path(site.USER_BASE) / "Scripts"
    return Path.home() / ".local" / "bin"


def install(bin_dir: Path, force: bool = False) -> Path:
    source = Path(__file__).resolve().with_name("cheat.py")
    if not source.is_file():
        raise FileNotFoundError(f"Cannot find application file: {source}")

    bin_dir.mkdir(parents=True, exist_ok=True)
    if os.name == "nt":
        target = bin_dir / "cheat.py"
        launcher = bin_dir / "cheat.cmd"
        targets = (target, launcher)
    else:
        target = bin_dir / "cheat"
        targets = (target,)
    if not force and any(path.exists() for path in targets):
        raise FileExistsError(f"{target} already exists. Re-run with --force to replace this installation.")

    shutil.copy2(source, target)
    if os.name == "nt":
        launcher.write_text('@echo off\r\npython "%~dp0cheat.py" %*\r\n', encoding="utf-8")
    else:
        target.chmod(target.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    return bin_dir


def main() -> int:
    parser = argparse.ArgumentParser(description="Install Terminal Cheat Code for the current user.")
    parser.add_argument("--bin-dir", type=Path, default=default_bin_dir(), help="Directory for the cheat command")
    parser.add_argument("--force", action="store_true", help="Replace an existing Terminal Cheat Code installation")
    args = parser.parse_args()
    try:
        bin_dir = install(args.bin_dir, args.force)
    except (FileExistsError, FileNotFoundError, OSError) as error:
        print(f"Installation failed: {error}", file=sys.stderr)
        return 1
    print(f"Installed cheat in {bin_dir}")
    if os.name != "nt":
        print(f'If needed, add it to your PATH: export PATH="{bin_dir}:$PATH"')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
