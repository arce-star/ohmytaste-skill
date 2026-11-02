# OhMyTaste Evaluations

The evaluations in this directory test workflow behavior, not scientific correctness in the abstract. Each case defines an input, the intended failure mode, and observable pass/fail criteria.

## How to run evaluations

These are currently specification-style evaluations for manual or harness-based execution:

1. Install or load the `ohmytaste` skill.
2. Run each prompt in `test-cases.md` with access to normal literature/web tools.
3. Save the full response, source list, and any generated proposal files.
4. Evaluate only against the stated criteria.
5. Record unresolved cases as unresolved; do not manufacture a pass.

Future automated evaluation may check structural properties, citation provenance, decision outcomes, and whether adversarial search changes the proposal. Human domain review can be added later, but this repository does not claim that such review has already occurred.

## What these evals are intended to catch

- premature brainstorming before literature grounding;
- fabricated research gaps;
- missed near-duplicate prior work;
- collapse between fact and speculation;
- experiments that cannot distinguish mechanisms;
- forced recommendations under weak evidence;
- unverified resource assumptions;
- false claims of full-text paper inspection.
