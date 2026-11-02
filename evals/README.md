# OhMyTaste Evaluations

The evaluations in this directory test workflow behavior, not scientific correctness in the abstract. Each case defines an input, the intended failure mode, and observable pass/fail criteria.

## How to run evaluations

These are currently specification-style evaluations for manual or harness-based execution:

1. Install or load the `ohmytaste` skill.
2. Run each prompt in `test-cases.md` with access to normal literature/web tools.
3. Save the full response, source list, evidence ledger, unresolved-question ledger, and any generated proposal files.
4. Evaluate only against the stated criteria.
5. Record unresolved cases as unresolved; do not manufacture a pass.

Future automated evaluation may check structural properties, citation provenance, decision outcomes, whether adversarial search changes the proposal, and whether rejected ideas generate useful residual-opportunity discovery. Human domain review can be added later, but this repository does not claim that such review has already occurred.

## What these evals are intended to catch

- premature brainstorming before literature grounding;
- fabricated research gaps;
- missed near-duplicate prior work;
- collapse between fact and speculation;
- experiments that cannot distinguish mechanisms;
- forced recommendations under weak evidence;
- unverified resource assumptions;
- false claims of full-text paper inspection;
- stopping immediately after obvious candidates are rejected;
- field judgments that identify unresolved questions and then silently drop them;
- over-rejecting novelty from abstract-only prior art;
- conflating scientific openness with competition, attribution risk, or expected publication ceiling.

## Current evaluation set

Cases 1-8 cover the original evidence, critique, feasibility, and honesty requirements. Cases 9-12 are v0.1.1 discovery regressions added after real research runs showed that the workflow could become overly conservative: it could correctly reject weak ideas while failing to convert its own strongest unresolved field judgment into a candidate hypothesis.
