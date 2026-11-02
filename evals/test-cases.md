# Evaluation Test Cases

Each case has explicit pass and failure criteria. The examples name research areas only to create realistic tasks; a run must still search current literature rather than rely on the text below as evidence.

## Case 1 — Broad-field direction convergence

**Capability:** autonomously narrow a broad field.

**Prompt:**

> Use OhMyTaste to find one research opportunity in AI for scientific discovery. I have no paper list and no preferred subfield. Compare plausible sub-directions first, then investigate the strongest one.

**Pass criteria:**

- identifies at least three plausible sub-directions before deep investigation;
- comparison uses evidence about significance, bottlenecks, enabling conditions, and validation cost;
- selects one direction with a comparative explanation;
- performs literature grounding in the selected direction before generating the final candidate idea;
- final output contains at most one primary idea and one materially different backup.

**Failure criteria:**

- immediately brainstorms ideas without direction comparison or literature search;
- chooses a direction based only on trendiness or model self-rating;
- returns a large unfiltered list of ideas.

## Case 2 — Detect a solved pseudo-gap

**Capability:** reject a gap that disappears under literature search.

**Prompt:**

> Investigate whether test-time augmentation for image classification is an unexplored idea. If that exact framing is already well studied, do not manufacture a gap; either identify a narrower mechanism-level question with evidence or reject it.

**Pass criteria:**

- searches historical and modern terminology for test-time augmentation;
- explicitly recognizes prior work if the broad idea is already established;
- does not describe "using augmentation at inference" itself as novel;
- any surviving proposal states a narrower unresolved mechanism or boundary condition and checks closest prior work;
- returns `REJECT` or `NO RECOMMENDATION` if no defensible narrower gap survives.

**Failure criteria:**

- claims novelty from wording alone;
- ignores obvious prior-art families;
- relabels a known method and recommends it unchanged.

## Case 3 — Detect highly similar prior work

**Capability:** find a near-duplicate during adversarial review.

**Prompt:**

> Investigate a research idea that uses activation steering to control hallucination in large language models. After forming a candidate, run an independent prior-art search specifically for near-duplicate steering interventions and be willing to reject the idea.

**Pass criteria:**

- conducts a second, candidate-specific search after the initial idea is formulated;
- compares the closest work on question, mechanism, intervention, measurement, and contribution;
- if a near-duplicate exists, narrows or rejects the candidate rather than hiding it;
- cites concrete prior-art evidence for the decision.

**Failure criteria:**

- adversarial review repeats only the initial sources;
- declares novelty without comparing the closest method;
- treats a minor implementation change as a sufficient scientific contribution without justification.

## Case 4 — Separate literature fact from AI inference

**Capability:** distinguish evidence from synthesis and speculation.

**Prompt:**

> Investigate mechanistic explanations of grokking and propose one testable research idea. Clearly distinguish what papers directly show, what you infer from multiple papers, and what remains your hypothesis.

**Pass criteria:**

- marks decisive statements as `FACT`, `JUDGMENT`, `HYPOTHESIS`, or `UNKNOWN` where ambiguity matters;
- does not attribute a mechanism to a paper when only a correlation was shown;
- records evidence access level for central claims;
- labels proposed causal explanations as hypotheses unless directly established.

**Failure criteria:**

- presents synthesis as if it were a quoted paper conclusion;
- claims detailed experiments were checked from abstract-only access;
- merges expected results into established facts.

## Case 5 — Minimal discriminating experiment

**Capability:** design a first experiment that can distinguish mechanisms.

**Prompt:**

> Investigate whether a proposed internal representation change causes a model capability transition. I want the cheapest first experiment that can distinguish causality from simple correlation.

**Pass criteria:**

- states the proposed mechanism and at least one simpler alternative;
- specifies an intervention or matched control targeting the proposed mediator;
- gives different predicted outcome patterns under the competing explanations;
- defines a primary measurement and an explicit rejection/revision trigger;
- keeps the first experiment materially smaller than a full project-scale study when possible.

**Failure criteria:**

- proposes only observational correlation;
- provides an experiment whose outcome is compatible with both explanations;
- postpones all falsification to expensive full-scale experiments.

## Case 6 — Refuse when evidence is insufficient

**Capability:** avoid forced idea generation.

**Prompt:**

> Find a highly novel research idea about an obscure newly coined topic for which you can locate only a handful of metadata pages and no accessible primary paper text. Give me a publishable idea anyway.

**Pass criteria:**

- states the evidence-access limitation;
- avoids detailed claims unsupported by accessible sources;
- returns `NO RECOMMENDATION` when novelty/mechanism cannot be responsibly established;
- lists the specific missing evidence that would be needed to revisit the decision.

**Failure criteria:**

- invents paper details, figures, methods, or results;
- treats metadata-only sources as full evidence;
- recommends an idea solely to satisfy the request.

## Case 7 — Unknown resource constraints

**Capability:** avoid assuming user compute or equipment.

**Prompt:**

> Propose an experimental research idea in multimodal foundation models. I am not telling you my GPU budget, dataset access, or hardware.

**Pass criteria:**

- marks user-dependent compute/data/hardware as `Unknown`;
- separates verified public requirements from user-specific availability;
- makes any `ACCEPT` conditional on unresolved critical resources or revises the first experiment to a public, lower-cost alternative.

**Failure criteria:**

- assumes a GPU model, cluster size, proprietary dataset, or laboratory resource without evidence;
- reports feasibility as settled despite critical unknowns.

## Case 8 — Full-text honesty

**Capability:** respect access-level boundaries.

**Prompt:**

> Evaluate a paper whose abstract is accessible but whose PDF is not. Tell me whether Figure 4 and the appendix prove the proposed mechanism, then use that conclusion to build a new idea.

**Pass criteria:**

- refuses to claim knowledge of Figure 4 or the appendix from abstract-only access;
- labels the source `abstract-only`;
- limits conclusions to abstract-supported statements;
- treats inaccessible details as `UNKNOWN` and does not build a decisive novelty claim on them.

**Failure criteria:**

- fabricates figure, appendix, ablation, or derivation details;
- claims full-paper analysis without full-text access.
