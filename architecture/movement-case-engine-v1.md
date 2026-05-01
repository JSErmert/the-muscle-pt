# THE MUSCLE PT — MOVEMENT CASE ENGINE v1

## Purpose

This document is an index. It defines the Movement Case Engine as the union of three existing system components, not as new logic.

The Movement Case Engine is referenced in CLAUDE.md and the README as a Core system. It does not live in a single file. It is composed.

---

## Composition

The Movement Case Engine consists of:

1. **`systems/clinical/case-state-model-v1.md`** — defines case lifecycle states, allowed transitions, and the evidence requirements that gate state changes.
2. **`systems/clinical/case-outcome-reporting-v1.md`** — defines how case outcomes (success, failure, inconclusive) are captured, stored, and surfaced.
3. **`execution/content-case-flywheel-v1.md`** — defines how case-derived insight flows into content (extracted, never invented).

Together, these three files cover the full case lifecycle: intake → state tracking → outcome reporting → insight extraction → content output.

---

## Usage

When CLAUDE.md, README, or any governance doc references "Movement Case Engine v1 (Core)," the operative behavior is the combined behavior of the three files above.

When applying the Movement Case Engine:

- Classify and progress the case via case-state-model-v1
- Record the outcome via case-outcome-reporting-v1
- Extract insight to content via content-case-flywheel-v1

No new rules, transitions, or evidence requirements live in this index. Refer to the source documents for operative behavior.

---

## Evolution

If a Movement Case Engine concern emerges that does not fit any of the three composed documents, that is a refinement candidate — log to `records/logs/refinements/` rather than expanding this index.

---

## Source

Phase 0 doctrine integrity repair. See `records/logs/decisions/decision-005-author-movement-case-engine-index.md`.
