# Changelog

All notable changes to OhMyTaste are documented here.

## [0.1.1-alpha.1] - 2026-11-03

### Changed

- Added a mandatory Scope Map, Tension Map, Unresolved-Question Ledger, and Discovery Trace so field judgment must feed candidate generation.
- Added one bounded Residual Opportunity Recovery pass when all initial candidates fail, using rejection evidence to search for deeper unresolved mechanisms rather than keyword-empty niches.
- Added explicit opportunity-discovery primitives: contradiction, dissociation, hidden assumption, boundary inversion, measurement failure, mechanism underdetermination, new observability, and new intervention.
- Split evidence handling into epistemic type (`FACT`, `JUDGMENT`, `HYPOTHESIS`, `UNKNOWN`) and evidence status (`SOURCE_REPORTED`, `FULL_TEXT_CHECKED`, `INDEPENDENTLY_REPLICATED`, `SYNTHESIZED`).
- Calibrated abstract-only prior-art collisions with `DIRECT_COLLISION`, `STRONG_COLLISION_RISK`, and `RELATED_NOT_DECISIVE` instead of treating topic similarity as automatic novelty closure.
- Separated `Scientific Status` (`OPEN`, `PARTIALLY_OPEN`, `CLOSED`, `UNCERTAIN`) from `Project Priority` (`PRIORITIZE`, `CONDITIONAL`, `DEPRIORITIZE`) while retaining the compatibility workflow decisions `ACCEPT`, `REVISE`, `REJECT`, and `NO RECOMMENDATION`.
- Updated the LaTeX proposal template to include scope, tension map, discovery trace, evidence/collision status, and the two-axis final decision.
- Expanded evaluation coverage from 8 to 12 cases with regression tests for residual opportunity discovery, unresolved-question closure, abstract-only collision calibration, and scientific openness versus project priority.

### Motivation

This release addresses a failure mode observed in real OhMyTaste runs: the workflow could identify a genuinely unresolved mechanism-level tension during field judgment, then omit it from candidate generation and terminate after rejecting easier candidates. The new workflow treats candidate rejection as evidence for one final discovery pass while preserving a hard stopping rule.

### Release status

Alpha. These changes improve the structure of research opportunity discovery but do not establish expert-level research taste. Quality still requires validation against real research cases and blinded domain-expert evaluation.

## [0.1.0-alpha.1] - 2026-11-03

### Added

- Initial `ohmytaste` Agent Skill with an eight-phase evidence-first research idea discovery workflow.
- Explicit evidence ledger and claim labeling for facts, judgments, hypotheses, and unknowns.
- Literature search protocol covering seminal work, recent work, closest prior art, negative results, and counter-evidence.
- Adversarial novelty review and feasibility audit with `ACCEPT`, `REVISE`, and `REJECT` outcomes.
- Markdown/LaTeX proposal output contract and XeLaTeX-compatible proposal template.
- Six required evaluation scenarios with explicit pass/fail criteria, plus two additional stress cases.
- Repository validator, deterministic skill ZIP packager, unit tests, and GitHub Actions CI.
- English and Simplified Chinese documentation.

### Release status

Alpha. The workflow is intended for iterative validation on real research cases. No claim of expert-level research judgment is made.
