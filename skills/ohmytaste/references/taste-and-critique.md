# Research Taste and Critique Protocol

This reference defines qualitative decision rules for selecting and attacking candidate research ideas without pretending that research taste can be reduced to a score.

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

## 2. Weak idea patterns

Treat these as warning signs:

- "apply method A to domain B" with no new mechanism or question;
- swapping an architecture while preserving the same scientific claim;
- claiming a gap because a particular phrase is absent from search results;
- a benchmark improvement whose contribution disappears under stronger tuning of the baseline;
- a hypothesis whose expected result is compatible with every plausible mechanism;
- novelty resting on a tiny implementation difference from the closest paper;
- an expensive full-scale experiment before any cheap falsification attempt;
- an idea requiring private data or equipment that the user has not said they can access;
- a proposal whose scientific claim remains vague even if the headline result succeeds.

These patterns can sometimes be repaired, but they require a specific reason the resulting work would teach something new.

## 3. Mechanism test

A mechanism-level candidate should complete this chain:

**Observation -> proposed latent cause -> intervention or perturbation -> discriminating prediction -> measurement.**

Example abstract form:

- Observation: performance changes sharply under condition X.
- Proposed cause: state variable M controls the transition.
- Intervention: manipulate M while holding obvious confounds fixed.
- Prediction: if M is causal, Y changes in direction P; if alternative A is correct, Y stays unchanged or changes differently.
- Measurement: metric Z distinguishes the outcomes.

If the chain cannot be written, the idea is too underspecified for `ACCEPT`.

## 4. Contribution survival test

Assume the proposed experiment succeeds exactly as hoped. Ask:

1. What claim can now be made that the closest prior paper could not make?
2. Is that claim about understanding, causal control, measurement validity, generality, or a consequential boundary condition?
3. Would the result still matter if the headline metric improvement were small or zero?

If the answer depends only on "we got a better number", the idea usually needs revision.

## 5. Closest-work collision test

For the nearest paper, compare at least:

- research question;
- mechanism/hypothesis;
- intervention or method;
- data/system;
- decisive measurement;
- claimed contribution.

Possible outcomes:

- **Same question + same mechanism + similar intervention**: strong `REJECT` signal.
- **Same method + different scientific question**: may survive if the new question is consequential and experimentally distinct.
- **Same question + different mechanism**: potentially valuable if predictions clearly differ.
- **Different terminology + same causal claim**: treat as prior-art collision even when keywords differ.

## 6. Simpler-explanation test

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

## 7. Minimal decisive experiment

The first experiment should answer one decision question, such as:

- Does the proposed mediator causally affect the phenomenon?
- Does the claimed effect survive a properly tuned baseline?
- Does the effect exist outside the benchmark artifact suspected to create it?
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

## 8. Feasibility gate

A candidate cannot receive unconditional `ACCEPT` when a core dependency is unverified.

Examples of blocking unknowns:

- dataset license or access;
- unavailable baseline code with insufficient paper detail;
- specialized equipment;
- compute beyond the stated user resources;
- evaluation requiring proprietary labels;
- measurement unavailable at the necessary temporal or spatial resolution.

Prefer revising the first experiment to use public and cheap resources when that preserves the causal question.

## 9. Decision gates

Use gates, not scores.

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
- evaluation can be confounded by tuning, leakage, or metric choice.

The revision must be concrete.

### REJECT

Use when any fatal condition remains:

- essentially the same study already exists;
- credible evidence directly contradicts the core hypothesis and no narrower version survives;
- the proposed experiment cannot distinguish the hypothesis from a simpler explanation;
- the contribution reduces to an engineering combination with no durable scientific claim;
- required resources are inaccessible with no meaningful substitute;
- successful results would still add little beyond the closest work.

### NO RECOMMENDATION

Use when all candidates are rejected or when evidence coverage is too weak to make a responsible recommendation.

A useful `NO RECOMMENDATION` response states what was searched, why candidates failed, and what missing evidence could change the decision.
