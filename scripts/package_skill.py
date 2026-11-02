#!/usr/bin/env python3
"""Create a deterministic standalone ZIP containing the installable OhMyTaste skill."""

from __future__ import annotations

import argparse
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "ohmytaste"
DEFAULT_OUTPUT = ROOT / "dist" / "ohmytaste-v0.1.0-alpha.1.zip"
FIXED_TIME = (2026, 1, 1, 0, 0, 0)


def iter_skill_files(skill_dir: Path):
    for path in sorted(skill_dir.rglob("*")):
        if path.is_file() and "__pycache__" not in path.parts and not path.name.endswith(".pyc"):
            yield path


def build_zip(output: Path, skill_dir: Path = SKILL_DIR) -> Path:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        raise FileNotFoundError(f"Missing required skill file: {skill_md}")

    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        output.unlink()

    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for source in iter_skill_files(skill_dir):
            relative = source.relative_to(skill_dir)
            arcname = Path(skill_dir.name) / relative
            info = zipfile.ZipInfo(str(arcname).replace("\\", "/"), date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, source.read_bytes())

    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    output = build_zip(args.output.resolve())
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
