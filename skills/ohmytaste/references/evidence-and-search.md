# Evidence and Search Protocol

This reference defines how OhMyTaste should search, record, and qualify scientific evidence.

## 1. Search objective

The search is not a bibliography-maximization task. Its purpose is to establish enough local field coverage to answer four questions:

1. What claim is already established?
2. What is the closest prior art to the candidate question or mechanism?
3. What evidence weakens the candidate explanation?
4. What information is still missing for a research decision?

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
- exact or near-exact phrases describing the candidate hypothesis after idea generation.

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

## 5. Evidence ledger

Maintain a compact structured ledger. A table is usually sufficient.

| Claim ID | Type | Claim | Source | Access | Location | Effect |
|---|---|---|---|---|---|---|
| C1 | FACT | Specific established result | DOI/arXiv | full-text | Sec. 4, Fig. 2 | supports |
| C2 | JUDGMENT | Interpretation across sources | C1, C3 | mixed | synthesis | supports |
| C3 | FACT | Negative/null result | DOI/arXiv | full-text | Table 3 | challenges |
| C4 | UNKNOWN | Public code availability | repository check pending | — | — | blocks feasibility |

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

## 6. Claim discipline

Use these labels consistently:

### FACT

Directly supported by a cited source or verified resource. The wording must stay within what the evidence establishes.

### JUDGMENT

A synthesis or interpretation. It should cite the facts that motivate it and remain revisable.

### HYPOTHESIS

A proposed explanation, mechanism, or prediction to be tested. Do not phrase it as a literature-established fact.

### UNKNOWN

A decision-relevant value that has not been verified: resource access, exact compute, data license, unreported hyperparameter, unpublished negative result, and similar.

## 7. Coverage targets

There is no fixed paper count. Coverage is adequate when the search has represented the following roles where they exist:

- foundational work;
- recent representative work;
- closest prior art;
- negative or null evidence;
- a challenge to the dominant explanation, metric, or benchmark assumption.

A long list that omits closest prior art is inadequate. A shorter set can be sufficient when it tightly covers the mechanism and adversarial neighborhood.

## 8. Stopping rule

Stop a search pass when:

- several query variants converge on the same small cluster of mechanisms and papers;
- newly found papers mostly repeat known claims;
- citation chasing around the closest work produces no materially closer predecessor;
- remaining uncertainty is documented and cannot be resolved with available access.

Continue searching when:

- the candidate uses terminology that differs across communities;
- the closest paper is known only through a secondary source;
- novelty depends on a small wording distinction;
- a contradictory result appears without a reconciled explanation;
- recent work may have changed the state of the field.

## 9. Adversarial search separation

After a candidate idea is written, formulate fresh queries from the candidate itself:

- exact mechanism claim;
- intervention + predicted signature;
- alternative terminology for the same causal relation;
- "failure" or "negative" variants;
- nearest-paper authors + follow-up work;
- citations to and from the nearest paper where available.

This second pass must be capable of changing `ACCEPT` to `REVISE` or `REJECT`.

## 10. Citation quality in the final proposal

For each important citation, include stable identifiers when available. Prefer DOI and arXiv IDs over fragile search-result URLs.

When possible, attach a short provenance note to decisive claims, such as:

- `full-text, Sec. 5.2, Fig. 3`
- `abstract-only; detailed ablation unavailable`
- `official dataset repository; access verified`

This is especially important when a claim determines novelty or feasibility.
