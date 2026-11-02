# OhMyTaste

[中文说明](README.zh-CN.md)

OhMyTaste is an open-source Agent Skill for **research idea discovery grounded in real literature**. Given only a research direction, it investigates the field, identifies a defensible unresolved problem, proposes a mechanism-driven hypothesis, stress-tests it against prior work and counter-evidence, audits feasibility, and returns at most one primary research idea plus one materially different fallback.

The first alpha release focuses on a rigorous, reproducible, and adversarial workflow. It does **not** claim expert-level scientific judgment or guaranteed novelty.

## Project Overview

Most idea-generation prompts start from brainstorming. OhMyTaste starts from evidence. Its intended use is early-stage research problem selection when the user has a broad field or a specific subfield but no pre-selected paper list or hypothesis.

The skill supports two entry modes:

- **Broad field** — compare several plausible sub-directions, then choose one for deeper investigation.
- **Specific direction** — skip convergence and begin literature grounding immediately.

The output is a compact research proposal with explicit evidence provenance, uncertainty labels, adversarial review, feasibility constraints, and a minimal decisive experiment.

## Why OhMyTaste

OhMyTaste is designed around eight principles:

1. **Evidence before ideas** — search and inspect real work before proposing hypotheses.
2. **Research taste** — prioritize consequential unresolved questions over fashionable combinations.
3. **Mechanism-driven reasoning** — connect observations, mechanisms, interventions, and predictions.
4. **Adversarial review** — actively search for work that duplicates, weakens, or falsifies the candidate idea.
5. **Feasibility first** — verify datasets, baselines, compute assumptions, and implementation paths.
6. **Minimal decisive experiment** — prefer the smallest experiment that separates competing explanations.
7. **Honest uncertainty** — label facts, literature-supported judgments, hypotheses, and unknowns separately.
8. **No forced ideas** — return no recommendation when the evidence does not justify one.

The workflow avoids numerical self-scoring and multi-agent theater. Decisions are made with evidence gates and explicit failure reasons.

## Core Workflow

1. **Research Direction Convergence** — narrow a broad field using research value, bottlenecks, enabling conditions, and validation cost.
2. **Literature Grounding** — cover seminal work, recent representative papers, closest methods, negative results, and challenges to prevailing conclusions.
3. **Field Judgment** — determine what is actually solved, what remains mechanistically unclear, and why prior work has not resolved it.
4. **Idea Generation** — construct a small number of hypotheses tied to evidence and a concrete mechanism.
5. **Adversarial Review** — run independent searches for near-duplicates, counter-evidence, simpler explanations, leakage, weak baselines, and contribution collapse.
6. **Feasibility Audit** — verify data, baselines, resources, implementation path, and whether the experiment distinguishes hypotheses.
7. **Final Decision** — mark each candidate `ACCEPT`, `REVISE`, or `REJECT`; recommend at most one primary idea and one substantially different fallback.
8. **Research Proposal** — produce Markdown and LaTeX; compile PDF only when XeLaTeX is actually available and compilation succeeds.

See [`skills/ohmytaste/SKILL.md`](skills/ohmytaste/SKILL.md) for the executable workflow, [`evidence-and-search.md`](skills/ohmytaste/references/evidence-and-search.md) for evidence handling, and [`taste-and-critique.md`](skills/ohmytaste/references/taste-and-critique.md) for research judgment and rejection criteria.

## Installation

The current skills CLI requires Node.js 22.20 or later.

List the skill without installing:

```bash
npx skills add arce-star/ohmytaste-skill --list
```

Install OhMyTaste:

```bash
npx skills add arce-star/ohmytaste-skill --skill ohmytaste
```

Install globally for a specific supported agent, for example Codex:

```bash
npx skills add arce-star/ohmytaste-skill --skill ohmytaste -g -a codex -y
```

A packaged archive can also be built locally:

```bash
python scripts/package_skill.py --output dist/ohmytaste-v0.1.0-alpha.1.zip
```

## Usage Examples

### Broad field

> Use OhMyTaste to investigate trustworthy research opportunities in mechanistic interpretability. I do not have a paper list or a hypothesis. First compare several sub-directions, then select one and produce a defensible proposal.

### Specific direction

> Use OhMyTaste to investigate delayed generalization (grokking) in neural networks. Find a research question that is still genuinely open, adversarially check for prior work, and design the smallest experiment that could falsify the hypothesis.

### Evidence-constrained request

> Investigate retrieval-augmented generation evaluation. If the literature does not support a credible new mechanism-level idea, explicitly return no recommendation.

## Architecture

```text
ohmytaste-skill/
├── README.md
├── README.zh-CN.md
├── LICENSE
├── CHANGELOG.md
├── skills/
│   └── ohmytaste/
│       ├── SKILL.md
│       ├── references/
│       │   ├── evidence-and-search.md
│       │   └── taste-and-critique.md
│       └── assets/
│           └── research-proposal.tex
├── scripts/
│   ├── check_repo.py
│   └── package_skill.py
├── evals/
│   ├── README.md
│   └── test-cases.md
├── tests/
│   ├── test_check_repo.py
│   └── test_package_skill.py
└── .github/workflows/ci.yml
```

The repository follows the Agent Skills convention: each installable skill is a directory whose name matches the `name` field in its `SKILL.md` frontmatter. Supporting references and assets live inside that skill directory so packaging remains self-contained.

## Limitations

- Scientific novelty cannot be guaranteed. Search coverage, indexing, paywalls, and recent unpublished work can hide relevant prior art.
- Full-text claims require full-text access. Abstract-only access must be labeled and cannot support claims about detailed experiments, figures, or derivations.
- The skill cannot replace domain experts, laboratory judgment, safety review, or formal peer review.
- Feasibility is conditional on user resources. Missing compute, data access, equipment, or time constraints are recorded as `Unknown`.
- A proposal can still fail after implementation. The workflow is explicitly designed to make early failure informative and cheap.

## Development

Run repository checks and unit tests:

```bash
python scripts/check_repo.py
python -m unittest discover -s tests -v
```

Build the deterministic ZIP package:

```bash
python scripts/package_skill.py --output dist/ohmytaste-v0.1.0-alpha.1.zip
```

Validate skills CLI discovery from a local checkout:

```bash
npx skills add . --list
```

CI performs repository validation, unit tests, package creation, skills CLI discovery, and a non-interactive installation smoke test. It also attempts to compile the LaTeX proposal template when XeLaTeX is present; absence of XeLaTeX is reported as a skipped optional check.

Evaluation cases are documented in [`evals/test-cases.md`](evals/test-cases.md). They specify explicit pass and failure criteria. No expert review is claimed unless a real review is later conducted and documented.

## Contribution

Contributions are welcome when they improve evidence quality, falsifiability, reproducibility, or evaluation coverage. Please keep changes testable and avoid adding framework complexity solely for appearance.

For workflow changes, include or update an evaluation case showing the behavior being improved. For search or evidence rules, state which failure mode the rule addresses.

## License

MIT License. See [`LICENSE`](LICENSE).
