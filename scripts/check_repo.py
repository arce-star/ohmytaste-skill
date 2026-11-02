#!/usr/bin/env python3
"""Repository and Agent Skill structural checks for OhMyTaste.

This intentionally uses only the Python standard library so contributors can run it
without installing project dependencies. It validates the subset of the Agent Skills
specification that this repository relies on, plus OhMyTaste-specific invariants.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "ohmytaste"
SKILL_FILE = SKILL_DIR / "SKILL.md"
VERSION_FILE = ROOT / "VERSION"
EXPECTED_VERSION = VERSION_FILE.read_text(encoding="utf-8").strip() if VERSION_FILE.is_file() else ""

REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / "README.zh-CN.md",
    ROOT / "LICENSE",
    ROOT / "CHANGELOG.md",
    VERSION_FILE,
    SKILL_FILE,
    SKILL_DIR / "references" / "evidence-and-search.md",
    SKILL_DIR / "references" / "taste-and-critique.md",
    SKILL_DIR / "assets" / "research-proposal.tex",
    ROOT / "scripts" / "package_skill.py",
    ROOT / "evals" / "README.md",
    ROOT / "evals" / "test-cases.md",
    ROOT / ".github" / "workflows" / "ci.yml",
]


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Parse simple top-level scalar YAML fields from SKILL.md."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("SKILL.md must start with YAML frontmatter delimiter '---'")
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration as exc:
        raise ValueError("SKILL.md frontmatter is not closed") from exc

    fields: dict[str, str] = {}
    key_re = re.compile(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$")
    for line in lines[1:end]:
        if not line or line[0].isspace():
            continue
        match = key_re.match(line)
        if not match:
            continue
        key, value = match.groups()
        value = (value or "").strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        fields[key] = value
    return fields, "\n".join(lines[end + 1 :])


def run_checks(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    skill_dir = root / "skills" / "ohmytaste"
    skill_file = skill_dir / "SKILL.md"
    version_file = root / "VERSION"

    for required in [root / p.relative_to(ROOT) for p in REQUIRED_FILES]:
        if not required.is_file():
            errors.append(f"Missing required file: {required.relative_to(root)}")

    expected_version = version_file.read_text(encoding="utf-8").strip() if version_file.is_file() else ""
    if not expected_version:
        errors.append("VERSION must contain a non-empty version")

    if not skill_file.is_file():
        return errors

    text = skill_file.read_text(encoding="utf-8")
    try:
        fields, body = parse_frontmatter(text)
    except ValueError as exc:
        errors.append(str(exc))
        return errors

    name = fields.get("name", "")
    description = fields.get("description", "")
    compatibility = fields.get("compatibility", "")

    if not name:
        errors.append("SKILL.md frontmatter requires name")
    if not description:
        errors.append("SKILL.md frontmatter requires description")
    if name and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append("Skill name must use lowercase letters, digits, and single hyphens")
    if len(name) > 64:
        errors.append("Skill name exceeds 64 characters")
    if len(description) > 1024:
        errors.append("Skill description exceeds 1024 characters")
    if len(compatibility) > 500:
        errors.append("Skill compatibility exceeds 500 characters")
    if name and skill_dir.name != name:
        errors.append(f"Skill directory '{skill_dir.name}' must match name '{name}'")

    if not re.search(r'^#\s+OhMyTaste\s*$', body, re.MULTILINE):
        errors.append("SKILL.md body must contain '# OhMyTaste'")

    for phase in [f"Phase {i}" for i in range(1, 9)]:
        if phase not in body:
            errors.append(f"SKILL.md missing {phase}")

    for required_marker in [
        "Scope Map",
        "Tension Map",
        "Unresolved-Question Ledger",
        "Discovery Trace",
        "Residual Opportunity Recovery",
        "Scientific Status",
        "Project Priority",
        "STRONG_COLLISION_RISK",
    ]:
        if required_marker not in body:
            errors.append(f"SKILL.md missing v0.1.1 discovery invariant: {required_marker}")

    for relative_ref in [
        "references/evidence-and-search.md",
        "references/taste-and-critique.md",
        "assets/research-proposal.tex",
    ]:
        if relative_ref not in text:
            errors.append(f"SKILL.md must reference {relative_ref}")

    if expected_version and f'version: "{expected_version}"' not in text:
        errors.append(f"SKILL.md metadata version must be {expected_version}")

    eval_file = root / "evals" / "test-cases.md"
    if eval_file.is_file():
        eval_text = eval_file.read_text(encoding="utf-8")
        case_count = len(re.findall(r"^## Case \d+", eval_text, flags=re.MULTILINE))
        if case_count < 12:
            errors.append(f"At least 12 eval cases are required; found {case_count}")
        pass_count = len(re.findall(r"^\*\*Pass criteria:\*\*", eval_text, flags=re.MULTILINE))
        fail_count = len(re.findall(r"^\*\*Failure criteria:\*\*", eval_text, flags=re.MULTILINE))
        if pass_count != case_count or fail_count != case_count:
            errors.append("Every eval case must include Pass criteria and Failure criteria")
        for case_title in [
            "Residual opportunity discovery",
            "Unresolved-question closure",
            "Abstract-only collision calibration",
            "Scientific openness versus project priority",
        ]:
            if case_title not in eval_text:
                errors.append(f"evals/test-cases.md missing required v0.1.1 case: {case_title}")

    changelog = root / "CHANGELOG.md"
    if changelog.is_file() and expected_version and expected_version not in changelog.read_text(encoding="utf-8"):
        errors.append(f"CHANGELOG.md must mention version {expected_version}")

    template = skill_dir / "assets" / "research-proposal.tex"
    if template.is_file():
        template_text = template.read_text(encoding="utf-8")
        for section in [
            "Executive Summary",
            "Research Background and Scope",
            "Tension Map and Research Gap",
            "Closest Related Work",
            "Discovery Trace",
            "Proposed Hypothesis",
            "Proposed Method",
            "Experimental Design",
            "Baselines and Metrics",
            "Decisive First Experiment",
            "Expected Contributions",
            "Risks and Alternative Explanations",
            "References",
        ]:
            if f"\\section{{{section}}}" not in template_text:
                errors.append(f"LaTeX template missing section: {section}")
        for command in ["ScientificStatus", "ProjectPriority", "Decision"]:
            if f"\\newcommand{{\\{command}}}" not in template_text:
                errors.append(f"LaTeX template missing decision command: {command}")

    return errors


def main() -> int:
    errors = run_checks()
    if errors:
        print("OhMyTaste repository checks FAILED:")
        for error in errors:
            print(f" - {error}")
        return 1
    print("OhMyTaste repository checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
