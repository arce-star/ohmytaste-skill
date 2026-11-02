---
name: ohmytaste
description: Evidence-first research idea discovery from a broad field or specific research direction. Use when a researcher wants the agent to investigate real literature, identify a defensible unresolved problem, propose a mechanism-driven and falsifiable research idea, adversarially search for prior art and counter-evidence, audit feasibility, and produce a concise research proposal. The skill may explicitly recommend no idea when evidence is insufficient.
license: MIT
compatibility: Requires access to scholarly search or web sources for literature grounding. PDF or full-text access is preferred for claims about detailed experiments, figures, sections, or derivations. XeLaTeX is optional for PDF compilation.
metadata:
  author: arce-star
  version: "0.1.0-alpha.1"
---

# OhMyTaste

Discover a research problem from evidence, then try to kill the resulting idea before recommending it.

## Activation boundary

Use this skill when the user provides either:

- a broad research field and wants the agent to choose a promising sub-direction; or
- a specific research direction and wants a literature-grounded, testable research idea.

Do not require the user to provide an existing idea, paper list, or hypothesis.

Do not use this workflow as a generic literature-summary template, a large brainstorming generator, a citation formatter, or a substitute for an already-defined implementation plan.

## Non-negotiable rules

1. **Evidence before ideas.** Do not generate candidate research ideas until a literature grounding pass has been completed.
2. **No fabricated gaps.** A research gap must survive direct searches for prior solutions, synonyms, adjacent terminology, and counter-evidence.
3. **Mechanism required.** A recommended idea must state a causal or explanatory mechanism and at least one prediction that would differ under a plausible alternative explanation.
4. **Adversarial search is separate.** After generating a candidate, run new searches intended to disprove novelty, mechanism, and contribution.
5. **Feasibility is factual.** Verify that claimed datasets, baselines, repositories, and evaluation resources exist when external access permits. Mark unavailable or user-dependent resources `Unknown`.
6. **Minimal decisive experiment.** The first experiment must be small enough to run early and informative enough to change the decision.
7. **Uncertainty labels are mandatory.** Distinguish `FACT`, `JUDGMENT`, `HYPOTHESIS`, and `UNKNOWN` in internal evidence tracking and in the final proposal where ambiguity matters.
8. **No forced recommendation.** If the evidence does not support a defensible idea, explicitly return `NO RECOMMENDATION` with the blocking reasons.
9. **No expertise theater.** Do not use self-scores, arbitrary weighted rankings, invented reviewer personas, or multi-agent voting as evidence of quality.
10. **No false full-text claims.** Reading an abstract, metadata page, snippet, or secondary summary does not count as reading the paper's full experimental details.

Before research, read:

- `references/evidence-and-search.md` for search coverage, evidence provenance, access-level rules, and the evidence ledger.
- `references/taste-and-critique.md` for research-taste heuristics, contribution tests, adversarial review, and rejection gates.

## Evidence state

Maintain an evidence ledger throughout the run. At minimum, each important source should record:

- title, authors, venue, publication date, DOI and/or arXiv ID when available;
- research problem and methodology;
- experimental or theoretical evidence;
- limitations relevant to the current question;
- access level: `full-text`, `partial-text`, `abstract-only`, or `metadata-only`;
- specific location for decisive claims when available: section, theorem, experiment, figure, table, appendix, or page;
- which claim it supports or challenges.

For every important statement, classify it as:

- `FACT` — directly supported by a source or verified resource;
- `JUDGMENT` — synthesis or interpretation supported by multiple facts;
- `HYPOTHESIS` — proposed explanation or expected result that remains unverified;
- `UNKNOWN` — information required for a decision but not yet established.

## Phase 1 — Research Direction Convergence

If the user provides a specific subfield, record it and continue to Phase 2.

If the user provides a broad field:

1. Identify 3-5 plausible sub-directions using recent literature, surveys, open-problem discussions, benchmark changes, negative results, or new enabling capabilities.
2. For each sub-direction, write a short evidence-backed comparison covering:
   - research significance;
   - unresolved bottleneck;
   - why the bottleneck may be tractable now;
   - validation cost and resource uncertainty;
   - obvious reasons the direction may already be saturated.
3. Choose one sub-direction for deep investigation.
4. Explain the choice in comparative terms and preserve rejected directions only as brief alternatives.

Do not turn this phase into a numerical leaderboard. Use evidence and explicit tradeoffs.

## Phase 2 — Literature Grounding

Build a local map of the selected subfield before proposing an idea.

Cover, when they exist:

- foundational or field-defining work;
- recent representative work;
- the closest known methods or hypotheses;
- negative or null results;
- work that challenges a common explanation or evaluation practice.

Use primary papers for central claims whenever possible. Secondary sources may help discover terminology or papers but cannot replace primary evidence for decisive technical claims.

A paper may influence a detailed technical claim only to the degree allowed by its access level. If only the abstract is available, limit claims to what the abstract establishes and label the access constraint.

Stop expanding the search when new papers mostly repeat already-mapped mechanisms and the candidate neighborhood has been checked under multiple terminology variants. If novelty remains uncertain, keep it uncertain.

## Phase 3 — Field Judgment

Produce a compact field judgment answering:

1. What has the field genuinely solved?
2. Which observed behaviors, mechanisms, assumptions, or boundary conditions remain insufficiently explained?
3. Which methods improve a metric while leaving the underlying bottleneck unresolved?
4. Why have existing approaches failed to settle the question?
5. What recent evidence, dataset, method, instrumentation, or theoretical result changes the feasibility of studying it now?

A valid gap is a specific unresolved relation between evidence and explanation. Absence of a paper with exactly the desired title is not a gap.

If the apparent gap disappears during this phase, discard it and continue searching. If no defensible gap remains, proceed to `NO RECOMMENDATION`.

## Phase 4 — Idea Generation

Generate a small candidate set, normally 1-3 ideas.

Each candidate must contain:

- **Research Problem**
- **Motivation**
- **Research Gap**
- **Supporting Evidence**
- **Proposed Hypothesis**
- **Underlying Mechanism**
- **Proposed Method**
- **Expected Contribution**
- **Experimental Design**

The mechanism must produce at least one discriminating prediction. State what result would weaken or falsify the hypothesis.

Prefer ideas that change understanding, measurement, intervention, or a consequential boundary condition. Penalize ideas whose main novelty is merely combining two existing methods without a new mechanism or question.

## Phase 5 — Adversarial Review

For each candidate, start an independent reverse search. Do not rely only on the papers collected while constructing the idea.

Attempt to falsify the candidate on all seven axes:

1. **Prior-art collision** — search the hypothesis, mechanism, intervention, and expected signature using synonyms and adjacent terminology.
2. **Missed related work** — inspect references/citations of the closest papers and recent follow-ups when available.
3. **Combination test** — ask whether the method is a straightforward composition whose scientific contribution survives only as engineering.
4. **Counter-evidence** — search for null results, contradictory measurements, failure reports, or theory that rules out the mechanism.
5. **Simpler explanation** — identify at least one simpler mechanism and an experiment that separates it from the proposed mechanism.
6. **Evaluation integrity** — check for leakage, metric artifacts, dataset shortcuts, tuning asymmetry, or unfair baselines.
7. **Contribution survival** — assume the main experiment succeeds; ask what scientific claim remains that the closest prior work could not already make.

Record concrete evidence for each major attack. Generic strengths/weaknesses are insufficient.

## Phase 6 — Feasibility Audit

Verify, or mark `Unknown`:

- whether the proposed datasets or experimental systems exist;
- whether public access is available;
- whether closest baselines have code, sufficient implementation detail, or reproducible substitutes;
- whether private data, specialized equipment, licensing, or human-subject approvals are required;
- compute, memory, storage, runtime, and repeated-run requirements when estimable;
- an implementable path from input data to the decisive measurement;
- whether the proposed experiment actually distinguishes the core hypothesis from alternatives.

Never infer the user's GPU, cluster, laboratory equipment, budget, or data access from silence.

If feasibility depends on an unknown resource, keep the idea conditional or revise the first experiment to remove that dependency.

## Phase 7 — Final Decision

Assign each surviving candidate exactly one decision:

- `ACCEPT` — evidence supports novelty enough for the current search coverage, the mechanism is testable, the decisive experiment is feasible, and the contribution survives adversarial review.
- `REVISE` — the core question remains promising but novelty, mechanism, experimental discrimination, or feasibility requires a concrete modification.
- `REJECT` — a fatal prior-art collision, counter-evidence, non-discriminating experiment, infeasible dependency, or contribution collapse remains.

Default output policy:

- recommend one primary idea;
- optionally include one backup only when it is materially different in scientific question or mechanism;
- if none survive, return `NO RECOMMENDATION` and list the decisive reasons.

Do not hide rejected candidates when their failure teaches something important about the field; summarize the failure briefly.

## Phase 8 — Research Proposal

For the final accepted or revised idea, produce a concise Markdown proposal with these sections:

1. Executive Summary
2. Research Background
3. Research Gap
4. Closest Related Work
5. Proposed Hypothesis
6. Proposed Method
7. Experimental Design
8. Baselines and Metrics
9. Decisive First Experiment
10. Expected Contributions
11. Risks and Alternative Explanations
12. References

Also produce a LaTeX version. Use `assets/research-proposal.tex` as the structural template when useful.

If file creation is available, save both `.md` and `.tex`. If XeLaTeX is available, attempt compilation and report a PDF only after the compiler exits successfully and the file exists. If the compiler is absent or compilation fails, report the exact limitation and keep the Markdown/LaTeX deliverables.

The proposal must include:

- the final decision (`ACCEPT` or `REVISE`);
- evidence-access caveats that materially affect confidence;
- the strongest prior-art threat;
- the strongest alternative explanation;
- the result of the minimal decisive experiment that would trigger rejection or major revision;
- resource assumptions, with missing ones marked `Unknown`.

## Completion checklist

Before returning a recommendation, verify:

- literature grounding preceded idea generation;
- closest prior art was searched independently after idea generation;
- decisive technical claims are tied to appropriate source access levels;
- the gap is specific and supported by evidence;
- the mechanism yields a discriminating prediction;
- a simpler explanation was considered;
- the first experiment can change the decision;
- resources are verified or marked `Unknown`;
- the final status is `ACCEPT`, `REVISE`, `REJECT`, or `NO RECOMMENDATION`;
- uncertainty is stated plainly and no expert-review claim is invented.
