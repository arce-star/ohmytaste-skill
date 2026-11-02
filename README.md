# OhMyTaste

[中文说明](README.zh-CN.md)

OhMyTaste is an open-source Agent Skill for **evidence-driven research opportunity discovery**. Given only a broad field or a specific research direction, it investigates real literature, maps what is actually known, identifies unresolved tensions, derives mechanism-level hypotheses, stress-tests them against prior art and counter-evidence, audits feasibility and strategic value, and recommends at most one primary research idea plus one materially different fallback.

Version `0.1.1-alpha.1` focuses on a failure mode observed in real research runs: a model can become good at rejecting weak ideas without becoming good at discovering deeper opportunities. The workflow now forces unresolved questions to feed candidate generation and allows one bounded recovery pass after all obvious candidates fail.

The project does **not** claim expert-level scientific judgment or guaranteed novelty.

## Project Overview

Most idea-generation prompts begin with brainstorming. OhMyTaste begins with evidence. It is intended for early-stage research problem selection when the user has a broad field or a specific subfield but no pre-selected paper list or hypothesis.

Two entry modes are supported:

- **Broad field** — compare several plausible sub-directions, then choose one for deeper investigation.
- **Specific direction** — skip convergence and begin literature grounding immediately.

The workflow produces either a compact research proposal or a justified `NO RECOMMENDATION` verdict.

## Why OhMyTaste

OhMyTaste is designed around these principles:

1. **Evidence before ideas** — inspect real work before proposing hypotheses.
2. **Opportunity discovery before filtering** — search for contradictions, dissociations, hidden assumptions, boundary inversions, measurement failures, underdetermined mechanisms, and newly available interventions or measurements.
3. **Mechanism-driven reasoning** — connect observations, latent causes, interventions, discriminating predictions, and measurements.
4. **Adversarial review** — actively search for work that duplicates, weakens, or falsifies the candidate idea.
5. **Feasibility first** — verify datasets, baselines, compute assumptions, and implementation paths.
6. **Minimal decisive experiment** — prefer the smallest experiment that can change the research decision.
7. **Honest uncertainty** — distinguish epistemic type from evidence strength and access level.
8. **No forced ideas** — return no recommendation when the evidence does not justify one.
9. **Bounded recovery** — when initial ideas fail, use the rejection pattern for one deeper discovery pass rather than endless idea generation.
10. **Separate scientific openness from project strategy** — an open question may still be a poor project because of low expected contribution, competition, cost, or attribution risk.

The workflow avoids numerical self-scoring and multi-agent theater. Decisions are made with explicit evidence and failure reasons.

## Core Workflow

1. **Research Direction Convergence** — narrow a broad field using significance, bottlenecks, enabling conditions, and validation cost.
2. **Literature Grounding and Scope Map** — cover foundational work, recent work, closest methods, negative results, challenges to prevailing conclusions, and the actual regimes demonstrated by each result.
3. **Field Judgment, Tension Map, and Unresolved-Question Ledger** — record what is solved and explicitly track every unresolved question.
4. **Opportunity Discovery and Candidate Formulation** — derive a small candidate set from literature tensions and require a `Discovery Trace` for each serious candidate.
5. **Adversarial Review** — search independently for near-duplicates, counter-evidence, simpler explanations, evaluation artifacts, and contribution collapse.
6. **Residual Opportunity Recovery and Feasibility Audit** — if all initial candidates fail, run exactly one recovery pass using rejection evidence, then audit feasibility.
7. **Final Decision** — report `Scientific Status`, `Project Priority`, and the compatibility decision `ACCEPT`, `REVISE`, `REJECT`, or `NO RECOMMENDATION`.
8. **Research Proposal** — produce Markdown and LaTeX; compile PDF only when XeLaTeX is available and compilation succeeds.

See [`skills/ohmytaste/SKILL.md`](skills/ohmytaste/SKILL.md) for the executable workflow, [`evidence-and-search.md`](skills/ohmytaste/references/evidence-and-search.md) for evidence handling, and [`taste-and-critique.md`](skills/ohmytaste/references/taste-and-critique.md) for research opportunity discovery and critique.

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

Build the packaged archive for the current version:

```bash
VERSION=$(cat VERSION)
python scripts/package_skill.py --output "dist/ohmytaste-v${VERSION}.zip"
```

## Usage Examples

### Broad field

> Use OhMyTaste to investigate trustworthy research opportunities in mechanistic interpretability. I do not have a paper list or a hypothesis. Compare several sub-directions, choose one, and derive a research proposal from evidence.

### Specific direction

> Use OhMyTaste to investigate delayed generalization (grokking). Track unresolved tensions explicitly, convert the strongest one into a hypothesis, search for prior-art collisions, and design the smallest experiment that could separate competing mechanisms.

### Evidence-constrained request

> Investigate retrieval-augmented generation evaluation. If all candidates fail, perform the single residual-opportunity recovery pass. If no defensible idea remains, return `NO RECOMMENDATION`.

## Architecture

```text
ohmytaste-skill/
├── README.md
├── README.zh-CN.md
├── LICENSE
├── CHANGELOG.md
├── VERSION
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
└── .github/workflows/
    ├── ci.yml
    └── release.yml
```

The repository follows the Agent Skills convention: each installable skill is a directory whose name matches the `name` field in its `SKILL.md` frontmatter.

## Limitations

- Scientific novelty cannot be guaranteed. Search coverage, indexing, paywalls, and unpublished work can hide relevant prior art.
- Full-text claims require full-text access. Abstract-only access cannot support claims about detailed experiments, figures, appendices, or derivations.
- Abstract-only similarity may establish strong collision risk without proving complete scientific duplication.
- Research taste is not validated by workflow structure alone. Real-case benchmarking and blinded domain review are still needed.
- Feasibility is conditional on user resources. Missing compute, data access, equipment, or time constraints are recorded as `Unknown`.
- A scientifically open question can still be strategically weak as a project.

## Development

Run repository checks and unit tests:

```bash
python scripts/check_repo.py
python -m unittest discover -s tests -v
```

Build the deterministic ZIP package:

```bash
VERSION=$(cat VERSION)
python scripts/package_skill.py --output "dist/ohmytaste-v${VERSION}.zip"
```

Validate skills CLI discovery from a local checkout:

```bash
npx skills add . --list
```

CI performs repository validation, unit tests, package creation, skills CLI discovery, and a non-interactive installation smoke test. It also attempts to compile the LaTeX proposal template when XeLaTeX is present.

Evaluation cases are documented in [`evals/test-cases.md`](evals/test-cases.md). The current suite contains 12 specification-style cases, including discovery regressions added after real research runs. No expert review is claimed unless a real review is conducted and documented.

## Contribution

Contributions are welcome when they improve evidence quality, opportunity discovery, falsifiability, reproducibility, or evaluation coverage. Workflow changes should include or update an evaluation case showing the behavior being improved.

Avoid adding framework complexity solely for appearance.

## License

MIT License. See [`LICENSE`](LICENSE).
