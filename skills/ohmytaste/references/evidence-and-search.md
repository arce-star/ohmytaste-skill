# Evidence and Search Protocol

This reference defines how OhMyTaste should search, record, and qualify scientific evidence.

## 1. Search objective

The search is not a bibliography-maximization task. Its purpose is to establish enough local field coverage to answer five questions:

1. What claim is already established, and within what scope?
2. What is the closest prior art to the candidate question or mechanism?
3. What evidence weakens the candidate explanation?
4. What unresolved tension could still support a new scientific question?
5. What information is still missing for a research decision?

Search breadth is useful only when it reduces uncertainty on these questions.

## 2. Query matrix

For a chosen research direction, build queries across several dimensions:

- canonical topic term + mechanism term;
- synonyms and historical terminology;
- target phenomenon + "mechanism", "cause", "explanation", or equivalent field language;
- target phenomenon + "failure", "negative result", "null", "limitation", "counterexample", or equivalent;
- closest method + target phenomenon;
- proposed intervention + target outcome;
- key dataset/benchmark/system + failure mode;
- recent survey/review/open-problem paper for terminology discovery;
- exact or near-exact phrases describing the candidate hypothesis after idea generation;
- terms representing boundary changes: alternate loss, dataset family, scale, architecture, domain, or measurement regime;
- terms for contradictions or dissociations: "inconsistent", "decouple", "dissociate", "fails under", "reversal", "measurement validity", or field equivalents.

Use field-appropriate vocabulary. Search adjacent communities when the same phenomenon may have a different name.

## 3. Source hierarchy

Prefer sources in this order for decisive technical claims:

1. original peer-reviewed paper or authoritative preprint with full text;
2. official proceedings/journal version;
3. author-hosted accepted manuscript or institutional repository;
4. official dataset, benchmark, or code repository documentation;
5. high-quality review or survey for orientation;
6. secondary technical explanation for terminology discovery only.

A secondary source can point to a primary paper. Resolve the primary paper before treating the claim as established whenever practical.

## 4. Access levels

Record one access level per source:

- `full-text` — the relevant body, experiments, figures, appendices, or proofs can be inspected;
- `partial-text` — some body content is available, but relevant sections may be missing;
- `abstract-only` — title/abstract/metadata are available;
- `metadata-only` — bibliographic record only.

Rules:

- `abstract-only` can support claims explicitly present in the abstract.
- It cannot justify claims such as "Figure 4 shows...", "the ablation proves...", or "the appendix derives...".
- `metadata-only` establishes bibliographic existence, not scientific findings.
- If a crucial claim depends on inaccessible full text, mark the claim uncertain and explain the access limit.
- Abstract similarity can establish a serious prior-art risk. It cannot automatically establish that the full scientific contribution is identical when decisive novelty dimensions remain hidden in the body.

## 5. Two-dimensional evidence ledger

Maintain a compact structured ledger. A table is usually sufficient.

| Claim ID | Epistemic Type | Evidence Status | Claim | Source | Access | Location | Effect |
|---|---|---|---|---|---|---|---|
| C1 | FACT | SOURCE_REPORTED | Specific reported result | DOI/arXiv | abstract-only | abstract | supports |
| C2 | FACT | FULL_TEXT_CHECKED | Experimental result checked in paper | DOI/arXiv | full-text | Sec. 4, Fig. 2 | supports |
| C3 | JUDGMENT | SYNTHESIZED | Interpretation across sources | C1, C2 | mixed | synthesis | supports |
| C4 | UNKNOWN | — | Public code availability | repository check pending | — | — | blocks feasibility |

Recommended source fields:

- Title
- Authors
- Venue
- Publication Date
- DOI
- arXiv ID
- Research Problem
- Methodology
- Experimental/Theoretical Evidence
- Limitations
- Access Level
- Relevant Location

Do not invent missing DOI, venue, page, figure, dataset, or repository information.

## 6. Epistemic type

Use these labels consistently:

### FACT

Directly supported by a cited source or verified resource. The wording must stay within what the evidence establishes.

### JUDGMENT

A synthesis or interpretation. It should cite the facts that motivate it and remain revisable.

### HYPOTHESIS

A proposed explanation, mechanism, or prediction to be tested. Do not phrase it as a literature-established fact.

### UNKNOWN

A decision-relevant value that has not been verified: resource access, exact compute, data license, unreported hyperparameter, unpublished negative result, and similar.

## 7. Evidence status

Use a second label for how strongly a claim was checked.

### SOURCE_REPORTED

The accessible source explicitly reports the claim. This records what the authors state; it does not imply independent verification or field consensus.

### FULL_TEXT_CHECKED

The relevant section, experiment, proof, figure, table, or appendix was inspected directly. This strengthens interpretation of what the paper actually did, but still does not make the result independently replicated.

### INDEPENDENTLY_REPLICATED

An independent paper, benchmark, reproduction, or user-run experiment verifies the important result under materially comparable conditions.

### SYNTHESIZED

The statement is an interpretation across multiple sources. It should normally pair with epistemic type `JUDGMENT`.

Never silently promote `SOURCE_REPORTED` into an established field fact.

## 8. Scope map

For each central result, track the demonstrated scope where relevant:

- task family;
- dataset or system;
- model class;
- loss function;
- training scale;
- experimental regime;
- evaluation protocol;
- intervention type.

When making a field-level statement, ask whether the cited evidence spans the claimed scope. A result demonstrated on one benchmark family or one loss should not be generalized across the field without supporting evidence.

Publication count or paper density may support a `JUDGMENT` that a direction is competitive. It is not sufficient evidence that all consequential research questions are closed.

## 9. Coverage targets

There is no fixed paper count. Coverage is adequate when the search has represented the following roles where they exist:

- foundational work;
- recent representative work;
- closest prior art;
- negative or null evidence;
- a challenge to the dominant explanation, metric, or benchmark assumption;
- at least one boundary-condition or cross-regime source when generality is part of the claim.

A long list that omits closest prior art is inadequate. A shorter set can be sufficient when it tightly covers the mechanism and adversarial neighborhood.

## 10. Stopping rule

Stop a grounding search pass when:

- several query variants converge on the same small cluster of mechanisms and papers;
- newly found papers mostly repeat known claims;
- citation chasing around the closest work produces no materially closer predecessor;
- remaining uncertainty is documented and cannot be resolved with available access.

Continue searching when:

- the candidate uses terminology that differs across communities;
- the closest paper is known only through a secondary source;
- novelty depends on a small wording distinction;
- a contradictory result appears without a reconciled explanation;
- a field-level claim rests on evidence from only one narrow regime;
- recent work may have changed the state of the field.

## 11. Abstract-only collision calibration

When a close paper is available only at abstract level, compare what is explicitly visible along these dimensions:

1. research question;
2. mechanism or explanatory claim;
3. intervention or decisive evidence;
4. scope and boundary conditions;
5. measurement;
6. scientific contribution.

Use one of these outcomes:

- `DIRECT_COLLISION` — the same question, mechanism, decisive intervention/evidence, and contribution are explicit enough to conclude that the candidate is already covered;
- `STRONG_COLLISION_RISK` — the abstract strongly overlaps, but one or more decisive novelty dimensions require full-text checking;
- `RELATED_NOT_DECISIVE` — topic or method overlap exists without enough evidence to conclude contribution identity.

`DIRECT_COLLISION` can justify `REJECT`. `STRONG_COLLISION_RISK` should normally produce `REVISE`, `UNCERTAIN`, or a request for full-text verification unless other independent evidence closes the question.

A similar title, shared dataset, or shared buzzword is never sufficient by itself for `DIRECT_COLLISION`.

## 12. Adversarial search separation

After a candidate idea is written, formulate fresh queries from the candidate itself:

- exact mechanism claim;
- intervention + predicted signature;
- alternative terminology for the same causal relation;
- "failure" or "negative" variants;
- nearest-paper authors + follow-up work;
- citations to and from the nearest paper where available.

This second pass must be capable of changing `ACCEPT` to `REVISE` or `REJECT`.

## 13. Rejection evidence as a new search signal

When a candidate fails, do not discard the failure reason. Record:

- what scientific question was occupied;
- what mechanism was occupied;
- what dimension remained untested or unclear;
- whether the failure exposed a hidden assumption, boundary condition, measurement issue, or mechanism conflict.

If all candidates fail, these records seed the single residual-opportunity recovery pass defined in the main Skill.

## 14. Citation quality in the final proposal

For each important citation, include stable identifiers when available. Prefer DOI and arXiv IDs over fragile search-result URLs.

When possible, attach a short provenance note to decisive claims, such as:

- `full-text, Sec. 5.2, Fig. 3; FULL_TEXT_CHECKED`
- `abstract-only; SOURCE_REPORTED; detailed ablation unavailable`
- `official dataset repository; access verified`

This is especially important when a claim determines novelty, scientific closure, or feasibility.
