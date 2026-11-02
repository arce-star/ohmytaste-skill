---
name: ohmytaste
description: Evidence-first research opportunity discovery from a broad field or specific research direction. Use when a researcher wants the agent to investigate real literature, identify unresolved mechanism-level questions, derive non-obvious research hypotheses from tensions or missing causal distinctions, adversarially search prior art and counter-evidence, audit feasibility and strategic value, and produce a concise research proposal. The skill may explicitly recommend no idea when evidence is insufficient.
license: MIT
compatibility: Requires access to scholarly search or web sources for literature grounding. PDF or full-text access is preferred for claims about detailed experiments, figures, sections, derivations, or novelty boundaries. XeLaTeX is optional for PDF compilation.
metadata:
  author: arce-star
  version: "0.1.1-alpha.1"
---

# OhMyTaste

Discover research opportunities from evidence, derive candidates from unresolved tensions, then try to kill them before recommending them.

## Activation boundary

Use this skill when the user provides either:

- a broad research field and wants the agent to choose a promising sub-direction; or
- a specific research direction and wants a literature-grounded, testable research idea.

Do not require the user to provide an existing idea, paper list, or hypothesis.

Do not use this workflow as a generic literature-summary template, a large brainstorming generator, a citation formatter, or a substitute for an already-defined implementation plan.

## Non-negotiable rules

1. **Evidence before ideas.** Do not generate candidate research ideas until a literature grounding pass has been completed.
2. **Discovery before filtering.** Identify unresolved tensions, hidden assumptions, dissociations, boundary inversions, measurement failures, or newly testable questions before constructing candidate ideas.
3. **No fabricated gaps.** A research gap must survive direct searches for prior solutions, synonyms, adjacent terminology, and counter-evidence.
4. **Unresolved-question closure.** Every question labeled unresolved in field judgment must later be classified as `CANDIDATE`, `KILLED_BY_PRIOR_ART`, `CURRENTLY_UNTESTABLE`, or `LOW_VALUE_WITH_REASON`.
5. **Mechanism required.** A recommended idea must state a causal or explanatory mechanism and at least one prediction that differs under a plausible alternative explanation.
6. **Discovery trace required.** Every serious candidate must show the evidence-to-idea chain that produced it.
7. **Adversarial search is separate.** After generating a candidate, run new searches intended to disprove novelty, mechanism, and contribution.
8. **One recovery pass after rejection.** If all initial candidates fail, perform exactly one residual-opportunity recovery pass using what the failures revealed before returning `NO RECOMMENDATION`.
9. **Feasibility is factual.** Verify that claimed datasets, baselines, repositories, and evaluation resources exist when external access permits. Mark unavailable or user-dependent resources `Unknown`.
10. **Minimal decisive experiment.** The first experiment must be small enough to run early and informative enough to change the decision.
11. **Uncertainty labels are mandatory.** Distinguish epistemic type and evidence status where ambiguity matters.
12. **Abstract-only collision is calibrated.** Abstract-only evidence can establish a strong collision risk, but direct novelty rejection requires that the same research question, mechanism, decisive intervention or evidence, and scientific contribution are all explicit enough to compare.
13. **Scientific openness and project priority are separate.** Competition, low expected paper ceiling, or likely near-term follow-up may lower project priority but do not by themselves close a scientific question.
14. **No forced recommendation.** If the evidence does not support a defensible idea after the recovery pass, explicitly return `NO RECOMMENDATION` with the blocking reasons.
15. **No expertise theater.** Do not use self-scores, arbitrary weighted rankings, invented reviewer personas, or multi-agent voting as evidence of quality.
16. **No false full-text claims.** Reading an abstract, metadata page, snippet, or secondary summary does not count as reading the paper's full experimental details.

Before research, read:

- `references/evidence-and-search.md` for search coverage, evidence provenance, access-level rules, collision calibration, and the evidence ledger.
- `references/taste-and-critique.md` for opportunity discovery primitives, unresolved-question closure, contribution tests, adversarial review, recovery, and decision gates.

## Evidence state

Maintain an evidence ledger throughout the run. At minimum, each important source should record:

- title, authors, venue, publication date, DOI and/or arXiv ID when available;
- research problem and methodology;
- experimental or theoretical evidence;
- limitations relevant to the current question;
- access level: `full-text`, `partial-text`, `abstract-only`, or `metadata-only`;
- specific location for decisive claims when available: section, theorem, experiment, figure, table, appendix, or page;
- which claim it supports or challenges.

Track two distinct dimensions for important claims.

### Epistemic type

- `FACT` — directly supported by a source or verified resource;
- `JUDGMENT` — synthesis or interpretation supported by multiple facts;
- `HYPOTHESIS` — proposed explanation or expected result that remains unverified;
- `UNKNOWN` — information required for a decision but not yet established.

### Evidence status

- `SOURCE_REPORTED` — the source explicitly reports the claim, but it has not been independently checked beyond the accessible source material;
- `FULL_TEXT_CHECKED` — the relevant full-text section, experiment, proof, table, figure, or appendix was inspected;
- `INDEPENDENTLY_REPLICATED` — an independent source or reproduction verifies the important result;
- `SYNTHESIZED` — the statement is an interpretation across sources rather than a single-source result.

Do not silently upgrade `SOURCE_REPORTED` into a field-level established fact.

## Phase 1 — Research Direction Convergence

If the user provides a specific subfield, record the requested scope and continue to Phase 2.

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

## Phase 2 — Literature Grounding and Scope Map

Build a local map of the selected subfield before proposing an idea.

Cover, when they exist:

- foundational or field-defining work;
- recent representative work;
- the closest known methods or hypotheses;
- negative or null results;
- work that challenges a common explanation or evaluation practice;
- boundary-condition studies where results reverse, disappear, or decouple.

Also record a **Scope Map**:

- what task families, datasets, model classes, loss functions, scales, experimental systems, and evaluation regimes were actually covered;
- what adjacent regimes were not checked;
- which conclusions appear broad and which are demonstrated only in a narrow setting.

Paper density or publication count may indicate competition, but cannot by itself establish structural saturation.

Use primary papers for central claims whenever possible. Secondary sources may help discover terminology or papers but cannot replace primary evidence for decisive technical claims.

A paper may influence a detailed technical claim only to the degree allowed by its access level. If only the abstract is available, limit claims to what the abstract establishes and label the access constraint.

Stop expanding a grounding pass when new papers mostly repeat already-mapped mechanisms and the candidate neighborhood has been checked under multiple terminology variants. If novelty remains uncertain, keep it uncertain.

## Phase 3 — Field Judgment, Tension Map, and Unresolved-Question Ledger

Produce a compact field judgment answering:

1. What has the field genuinely solved, at what evidence level, and within what scope?
2. Which observed behaviors, mechanisms, assumptions, or boundary conditions remain insufficiently explained?
3. Which methods improve a metric while leaving the underlying bottleneck unresolved?
4. Why have existing approaches failed to settle the question?
5. What recent evidence, dataset, method, instrumentation, or theoretical result changes the feasibility of studying it now?

Then build a **Tension Map**. Search explicitly for:

- two credible results that current explanations do not reconcile cleanly;
- two variables or processes commonly treated as equivalent that may dissociate;
- conclusions that depend on an assumption never isolated experimentally;
- results that reverse across dataset, loss, scale, architecture, or evaluation regime;
- a proxy or measurement that may decouple from the target mechanism;
- several plausible mechanisms that explain the same observed evidence;
- a new measurement or intervention that makes an old hidden variable observable or controllable.

Create an **Unresolved-Question Ledger**. Every question called unresolved must later end in exactly one state:

- `CANDIDATE`;
- `KILLED_BY_PRIOR_ART`;
- `CURRENTLY_UNTESTABLE`;
- `LOW_VALUE_WITH_REASON`.

A valid gap is a specific unresolved relation between evidence and explanation. Absence of a paper with exactly the desired title is not a gap.

Do not proceed to `NO RECOMMENDATION` from Phase 3 solely because obvious gaps disappear. First convert the strongest remaining tensions into candidate hypotheses in Phase 4.

## Phase 4 — Opportunity Discovery and Candidate Formulation

Generate a small candidate set, normally 1-3 ideas, directly from the strongest entries in the Tension Map and Unresolved-Question Ledger.

Prefer these opportunity-discovery primitives:

- **Contradiction** — two credible results resist a common explanation;
- **Dissociation** — two quantities or processes assumed to move together may be causally separable;
- **Hidden assumption** — an important conclusion depends on a condition never isolated;
- **Boundary inversion** — a result changes sign, ranking, or mechanism across regimes;
- **Measurement failure** — a proxy is treated as the mechanism but may detach from it;
- **Mechanism underdetermination** — multiple mechanisms fit the current evidence;
- **New observability** — a new tool makes a previously hidden state measurable;
- **New intervention** — a new method makes a previously correlational variable directly manipulable.

Each serious candidate must include:

- **Research Problem**
- **Motivation**
- **Research Gap**
- **Supporting Evidence**
- **Proposed Hypothesis**
- **Underlying Mechanism**
- **Proposed Method**
- **Expected Contribution**
- **Experimental Design**
- **Discovery Trace**

The **Discovery Trace** must use this structure:

`Evidence A + Evidence B -> tension or unexplained relation -> missing causal distinction -> hypothesis -> discriminating prediction -> minimal decisive experiment`.

The mechanism must produce at least one discriminating prediction. State what result would weaken or falsify the hypothesis.

Prefer ideas that change understanding, measurement, intervention, or a consequential boundary condition. Penalize ideas whose main novelty is merely combining two existing methods without a new mechanism or question.

Before moving on, check the Unresolved-Question Ledger: every unresolved question from Phase 3 must now either map to a candidate or carry a reason it is untestable or low-value.

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

For the closest prior work, compare explicitly:

- research question;
- mechanism;
- intervention or decisive evidence;
- scope and boundary conditions;
- measurement;
- scientific contribution.

If the closest source is abstract-only, use `STRONG_COLLISION_RISK` when similarity is high but decisive novelty dimensions remain unavailable. Direct `REJECT` from abstract-only evidence requires sufficiently explicit overlap in research question, mechanism, decisive intervention/evidence, and contribution.

Record concrete evidence for each major attack. Generic strengths/weaknesses are insufficient.

## Phase 6 — Residual Opportunity Recovery and Feasibility Audit

### Residual Opportunity Recovery

If at least one candidate survives adversarial review, skip directly to the feasibility audit below.

If all initial candidates fail, perform **exactly one** recovery pass before `NO RECOMMENDATION`.

Use the rejection record as new evidence. Ask:

1. What did all the collisions have in common?
2. Which unresolved question survived even though the obvious implementation was occupied?
3. Did two rejected candidates fail for different explanations of the same phenomenon?
4. Did prior art close a method while leaving a causal distinction open?
5. Did abstract-only collisions leave an unresolved novelty boundary that requires full-text checking?
6. Did rejection expose a cross-regime contradiction, measurement failure, or hidden assumption?

A recovery candidate must have a new scientific question or mechanism. Renaming the rejected method, shrinking the scope arbitrarily, or searching for a keyword-empty corner is invalid.

After this single recovery pass, run a focused adversarial search on any recovery candidate. If it also fails, return `NO RECOMMENDATION`; do not recurse indefinitely.

### Feasibility Audit

For every surviving initial or recovery candidate, verify, or mark `Unknown`:

- whether the proposed datasets or experimental systems exist;
- whether public access is available;
- whether closest baselines have code, sufficient implementation detail, or reproducible substitutes;
- whether private data, specialized equipment, licensing, or human-subject approvals are required;
- compute, memory, storage, runtime, and repeated-run requirements when estimable;
- an implementable path from input data to the decisive measurement;
- whether the proposed experiment actually distinguishes the core hypothesis from alternatives.

Never infer the user's GPU, cluster, laboratory equipment, budget, or data access from silence.

If feasibility depends on an unknown resource, keep the idea conditional or revise the first experiment to remove that dependency.

## Phase 7 — Final Decision: Scientific Status and Project Priority

For each surviving or rejected candidate, record three outputs.

### A. Scientific Status

- `OPEN` — the scientific question remains materially unresolved under current evidence.
- `PARTIALLY_OPEN` — an unresolved component remains, but substantial parts are already explained or occupied.
- `CLOSED` — current evidence supports that essentially the same scientific question and contribution are already resolved.
- `UNCERTAIN` — evidence access or coverage is insufficient to determine openness responsibly.

### B. Project Priority

- `PRIORITIZE` — strong scientific value, meaningful differentiation, and a credible first experiment justify near-term work.
- `CONDITIONAL` — worth revisiting if named evidence, resource, or novelty uncertainty is resolved.
- `DEPRIORITIZE` — scientifically open or partially open, but current expected contribution, competition, cost, attribution risk, or confirmatory character makes it a weak project choice.

Competition, likely follow-up by another group, or low expected venue ceiling may justify `DEPRIORITIZE`; they do not by themselves justify `CLOSED`.

### C. Workflow Decision

Keep the compatibility decision:

- `ACCEPT` — evidence supports novelty enough for the current search coverage, the mechanism is testable, the decisive experiment is feasible, and the contribution survives adversarial review.
- `REVISE` — the core question remains promising but novelty, mechanism, experimental discrimination, feasibility, or scope requires a concrete modification.
- `REJECT` — a fatal prior-art collision, counter-evidence, non-discriminating experiment, infeasible dependency, or contribution collapse remains.
- `NO RECOMMENDATION` — no candidate remains worth recommending after the one allowed recovery pass, or evidence coverage is too weak to make a responsible recommendation.

Default output policy:

- recommend one primary idea;
- optionally include one backup only when it is materially different in scientific question or mechanism;
- if none survive, return `NO RECOMMENDATION` and list the decisive reasons plus what the rejection process revealed about remaining open questions.

Do not hide rejected candidates when their failure teaches something important about the field; summarize the failure briefly.

## Phase 8 — Research Proposal

For the final accepted or revised idea, produce a concise Markdown proposal with these sections:

1. Executive Summary
2. Research Background and Scope
3. Tension Map and Research Gap
4. Closest Related Work
5. Discovery Trace
6. Proposed Hypothesis
7. Proposed Method
8. Experimental Design
9. Baselines and Metrics
10. Decisive First Experiment
11. Expected Contributions
12. Risks and Alternative Explanations
13. References

Also produce a LaTeX version. Use `assets/research-proposal.tex` as the structural template when useful.

If file creation is available, save both `.md` and `.tex`. If XeLaTeX is available, attempt compilation and report a PDF only after the compiler exits successfully and the file exists. If the compiler is absent or compilation fails, report the exact limitation and keep the Markdown/LaTeX deliverables.

The proposal must include:

- `Scientific Status`;
- `Project Priority`;
- the workflow decision (`ACCEPT` or `REVISE`);
- evidence-access caveats that materially affect confidence;
- the strongest prior-art threat;
- the strongest alternative explanation;
- the result pattern of the minimal decisive experiment that would trigger rejection or major revision;
- resource assumptions, with missing ones marked `Unknown`.

For `NO RECOMMENDATION`, produce a compact verdict instead of forcing a proposal. Include scope, strongest rejected candidates, unresolved-question closure, the recovery-pass result, and concrete evidence that could reopen the decision.

## Completion checklist

Before returning a recommendation or `NO RECOMMENDATION`, verify:

- literature grounding preceded idea generation;
- a Scope Map was recorded;
- a Tension Map was built before candidate generation;
- every unresolved question received a closure state;
- every serious candidate contains a Discovery Trace;
- closest prior art was searched independently after idea generation;
- abstract-only collisions were calibrated rather than automatically treated as definitive novelty closure;
- decisive technical claims are tied to appropriate source access levels and evidence status;
- the gap is specific and supported by evidence;
- the mechanism yields a discriminating prediction;
- a simpler explanation was considered;
- the first experiment can change the decision;
- if all initial candidates failed, exactly one residual-opportunity recovery pass was performed;
- resources are verified or marked `Unknown`;
- Scientific Status and Project Priority are reported separately;
- the final workflow status is `ACCEPT`, `REVISE`, `REJECT`, or `NO RECOMMENDATION`;
- uncertainty is stated plainly and no expert-review claim is invented.
