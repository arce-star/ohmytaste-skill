# Research Taste and Critique Protocol

This reference defines qualitative decision rules for discovering, selecting, and attacking candidate research ideas without pretending that research taste can be reduced to a score.

## 1. What counts as a promising problem

Prefer problems with several of these properties:

- a recurring empirical or theoretical phenomenon lacks a satisfactory mechanism;
- competing explanations make different observable predictions;
- an important benchmark gain may come from a confound or shortcut that can be isolated;
- a recent capability, dataset, measurement, or theoretical tool makes an old question newly testable;
- a method works but its boundary conditions are poorly understood and matter for deployment or scientific interpretation;
- a negative result contradicts a common explanation and can be reconciled by a sharper hypothesis;
- a high-cost assumption can be tested with a much cheaper decisive experiment.

Research value should come from the scientific question and the information gained by the experiment.

## 2. Opportunity discovery primitives

Do not rely mainly on explicit "future work" sections or keyword-empty gaps. Search for structures that can generate a non-obvious scientific question.

### Contradiction

Two credible results resist the same explanation.

Ask:

- Can both findings be true under the claimed mechanism?
- Is one result measured under a different regime that reveals a hidden variable?
- What intervention would force the two explanations to make different predictions?

### Dissociation

Two quantities or processes are routinely treated as equivalent, sequential, or tightly coupled.

Ask whether they can be manipulated independently. A clean dissociation can be more informative than another correlation.

### Hidden assumption

A central conclusion relies on a condition that has not been isolated: loss function, data distribution, normalization, architecture, scale, supervision, initialization, measurement window, or similar.

The opportunity is strongest when changing the assumption makes competing mechanisms predict different outcomes.

### Boundary inversion

A method, mechanism, ranking, or causal effect changes sign or ordering across regimes.

The research question should explain the inversion rather than merely document another benchmark result.

### Measurement failure

A proxy, representation metric, diagnostic, or aggregate score may decouple from the phenomenon it is supposed to measure.

A valuable project can establish where the proxy is valid, where it fails, and what causal conclusion changes after correcting it.

### Mechanism underdetermination

Several explanations fit the same current evidence.

The opportunity is to design a discriminating intervention, not to add another correlational measurement.

### New observability

A new probe, dataset, instrument, theorem, logging interface, or measurement method exposes a state that older work could only infer indirectly.

### New intervention

A recent method makes a previously observational variable directly controllable. This can reopen an old question even when the phenomenon itself is mature.

## 3. Discovery trace

Every serious candidate must make its origin auditable.

Use this chain:

**Evidence A + Evidence B -> tension or unexplained relation -> missing causal distinction -> hypothesis -> discriminating prediction -> minimal decisive experiment.**

A candidate with a polished method but no convincing discovery trace is weak. The trace should show why this question emerges from the literature rather than from generic brainstorming.

## 4. Unresolved-question closure

During field judgment, every statement labeled unresolved must enter a ledger and later receive exactly one status:

- `CANDIDATE` — converted into a testable candidate;
- `KILLED_BY_PRIOR_ART` — direct or sufficiently strong evidence shows that the scientific question is already covered;
- `CURRENTLY_UNTESTABLE` — the question is meaningful but the required observation/intervention is unavailable under current evidence or resources;
- `LOW_VALUE_WITH_REASON` — open enough scientifically, but success would add little understanding or consequence.

Do not allow a report to call a question "truly unresolved" and then silently omit it from candidate generation.

## 5. Weak idea patterns

Treat these as warning signs:

- "apply method A to domain B" with no new mechanism or question;
- swapping an architecture while preserving the same scientific claim;
- claiming a gap because a particular phrase is absent from search results;
- a benchmark improvement whose contribution disappears under stronger tuning of the baseline;
- a hypothesis whose expected result is compatible with every plausible mechanism;
- novelty resting on a tiny implementation difference from the closest paper;
- an expensive full-scale experiment before any cheap falsification attempt;
- an idea requiring private data or equipment that the user has not said they can access;
- a proposal whose scientific claim remains vague even if the headline result succeeds;
- a recovery candidate that merely narrows a rejected idea until no exact keyword match remains.

These patterns can sometimes be repaired, but they require a specific reason the resulting work would teach something new.

## 6. Mechanism test

A mechanism-level candidate should complete this chain:

**Observation -> proposed latent cause -> intervention or perturbation -> discriminating prediction -> measurement.**

Example abstract form:

- Observation: performance changes sharply under condition X.
- Proposed cause: state variable M controls the transition.
- Intervention: manipulate M while holding obvious confounds fixed.
- Prediction: if M is causal, Y changes in direction P; if alternative A is correct, Y stays unchanged or changes differently.
- Measurement: metric Z distinguishes the outcomes.

If the chain cannot be written, the idea is too underspecified for `ACCEPT`.

## 7. Contribution survival test

Assume the proposed experiment succeeds exactly as hoped. Ask:

1. What claim can now be made that the closest prior paper could not make?
2. Is that claim about understanding, causal control, measurement validity, generality, or a consequential boundary condition?
3. Would the result still matter if the headline metric improvement were small or zero?

If the answer depends only on "we got a better number", the idea usually needs revision.

## 8. Closest-work collision test

For the nearest paper, compare at least:

- research question;
- mechanism/hypothesis;
- intervention or decisive evidence;
- data/system and boundary conditions;
- decisive measurement;
- claimed scientific contribution.

Possible outcomes:

- **Same question + same mechanism + similar decisive intervention/evidence + same contribution**: strong `REJECT` signal.
- **Same method + different scientific question**: may survive if the new question is consequential and experimentally distinct.
- **Same question + different mechanism**: potentially valuable if predictions clearly differ.
- **Different terminology + same causal claim**: treat as prior-art collision even when keywords differ.
- **Same broad topic but inaccessible decisive details**: mark collision risk and novelty uncertainty rather than assuming identity.

Follow the abstract-only collision calibration in `evidence-and-search.md`.

## 9. Simpler-explanation test

For every candidate, name at least one alternative that requires fewer new assumptions.

Then design a result pattern that separates the explanations. Good first experiments often include:

- intervention vs matched sham control;
- temporal ordering test;
- held-constant confound;
- negative control condition;
- dose-response or perturbation strength sweep;
- cross-dataset or cross-system boundary test when generality is central;
- ablation targeted at the proposed mediator rather than the whole method.

A first experiment that merely reproduces the expected correlation is weak.

## 10. Minimal decisive experiment

The first experiment should answer one decision question, such as:

- Does the proposed mediator causally affect the phenomenon?
- Does the claimed effect survive a properly tuned baseline?
- Does the effect exist outside the benchmark artifact suspected to create it?
- Are two proposed mechanisms causally separable?
- Does the closest prior method already explain the result?

Specify before running:

- smallest realistic dataset/system;
- baseline and control;
- manipulated variable;
- primary measurement;
- predicted pattern under the proposed mechanism;
- predicted pattern under the strongest alternative;
- rejection/revision trigger.

The experiment is decisive when a plausible outcome would actually stop or redirect the project.

## 11. Residual opportunity recovery

If every initial candidate is rejected, run exactly one recovery pass. The goal is to learn from the pattern of rejection rather than to search indefinitely for a surviving keyword niche.

Use the rejection ledger as input. Ask:

1. Which scientific questions were closed, and which causal distinctions were left open?
2. Did several collisions assume the same proxy, benchmark, loss, task family, or regime?
3. Did different prior papers explain the same phenomenon with mechanisms that have never been directly separated?
4. Did a candidate fail because a method was occupied while the underlying mechanism remained unresolved?
5. Did a near-duplicate abstract leave a crucial novelty dimension unknown?
6. Did a failed candidate reveal a stronger contradiction than the original field map contained?

A valid recovery candidate must change the scientific question, mechanism, or decisive distinction. It cannot be a cosmetic reformulation of a rejected candidate.

After generating a recovery candidate, perform a focused adversarial search. If it fails, stop and return `NO RECOMMENDATION`. Do not recursively generate further recovery rounds.

## 12. Feasibility gate

A candidate cannot receive unconditional `ACCEPT` when a core dependency is unverified.

Examples of blocking unknowns:

- dataset license or access;
- unavailable baseline code with insufficient paper detail;
- specialized equipment;
- compute beyond the stated user resources;
- evaluation requiring proprietary labels;
- measurement unavailable at the necessary temporal or spatial resolution.

Prefer revising the first experiment to use public and cheap resources when that preserves the causal question.

## 13. Scientific status

Judge scientific openness separately from project strategy.

### OPEN

The scientific question remains materially unresolved and the current literature does not already support the same contribution.

### PARTIALLY_OPEN

Substantial pieces are solved, but a consequential causal distinction, boundary condition, or measurement question remains unresolved.

### CLOSED

Current evidence supports that essentially the same scientific question, mechanism, decisive evidence, and contribution are already covered.

### UNCERTAIN

Evidence access or search coverage is insufficient to determine openness responsibly.

## 14. Project priority

After scientific status, separately judge whether the project is worth pursuing now.

### PRIORITIZE

The problem is scientifically meaningful, differentiated enough, feasible enough, and has a credible path to a substantive contribution.

### CONDITIONAL

The problem may be worthwhile after a named uncertainty is resolved: full-text novelty check, resource access, baseline reproduction, missing measurement, or similar.

### DEPRIORITIZE

The scientific question may still be open, but current expected contribution, confirmatory character, competition, attribution risk, cost, or likely ceiling makes it a weak project choice.

Do not use competition or predicted future work by another group as evidence that a scientific question is `CLOSED`.

## 15. Workflow decision gates

Keep the compatibility decisions below. They answer whether OhMyTaste should recommend the project under the current evidence, while Scientific Status and Project Priority explain why.

### ACCEPT

All must hold to the level permitted by current evidence:

- a real unresolved question remains after prior-art search;
- the mechanism is explicit;
- at least one discriminating prediction exists;
- the closest work does not already make the same contribution;
- the first experiment is feasible or has explicitly verified prerequisites;
- a negative result would be informative;
- the contribution survives the success thought experiment.

### REVISE

Use when the problem is promising but one of the following is repairable:

- novelty boundary is too close to prior work;
- mechanism is plausible but prediction is not discriminating;
- first experiment is too expensive;
- resource assumptions remain unknown;
- evaluation can be confounded by tuning, leakage, or metric choice;
- abstract-only prior art creates a strong collision risk whose decisive details remain inaccessible.

The revision must be concrete.

### REJECT

Use when any fatal condition remains:

- essentially the same study and scientific contribution already exist;
- credible evidence directly contradicts the core hypothesis and no narrower mechanism survives;
- the proposed experiment cannot distinguish the hypothesis from a simpler explanation;
- the contribution reduces to an engineering combination with no durable scientific claim;
- required resources are inaccessible with no meaningful substitute;
- successful results would still add little beyond the closest work.

### NO RECOMMENDATION

Use when all initial candidates and the one allowed recovery candidate are rejected, or when evidence coverage is too weak to make a responsible recommendation.

A useful `NO RECOMMENDATION` response states:

- the actual scope investigated;
- what was searched;
- why candidates failed;
- what the failure pattern revealed;
- how every unresolved question was closed in the ledger;
- what evidence could reopen the decision.
