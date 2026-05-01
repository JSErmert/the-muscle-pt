---
decision_id: decision-007-phase0-author-movement-case-engine-index
date: 2026-05-01
type: decision
status: closed
relevant_doctrine:
  - architecture/movement-case-engine-v1.md
  - systems/clinical/case-state-model-v1.md
  - systems/clinical/case-outcome-reporting-v1.md
  - execution/content-case-flywheel-v1.md
  - CLAUDE.md (Section 1)
phase: M1 Operationalize Plan v1 — Phase 0 fix #3
---

# Decision

Author `architecture/movement-case-engine-v1.md` as a 1-page index document. The file is referenced by README and CLAUDE.md as a Core system but did not exist.

---

# Context

Phase 0 doctrine integrity audit identified that `movement-case-engine-v1.md` was named in CLAUDE.md Section 1 (System Awareness) and the README as a Core system component, but no file existed. The operative behavior of the Movement Case Engine was distributed across three other files without a unifying index.

---

# Reasoning

Per HL-08, references to non-existent doctrine files must be repaired. The M1 Operationalize Plan specified the recommended fix: "Author a 1-page index doc that defines the Movement Case Engine as the union of case-state-model + case-outcome-reporting + content-case-flywheel (no new logic, just naming)."

This avoids inventing new doctrine. The Movement Case Engine is composed, not authored.

---

# Resolution

`architecture/movement-case-engine-v1.md` created as a 1-page index. It defines the Movement Case Engine as the union of:

1. `systems/clinical/case-state-model-v1.md` — case lifecycle states and transitions
2. `systems/clinical/case-outcome-reporting-v1.md` — outcome capture and storage
3. `execution/content-case-flywheel-v1.md` — case-derived insight to content

The index contains no new transitions, evidence requirements, or content rules. All operative behavior remains in the source files.

---

# Consequence

CLAUDE.md and README references to "Movement Case Engine v1 (Core)" now resolve to a real file. Future readers can find the engine via a single index rather than reverse-engineering it from three distributed sources.

If a Movement Case Engine concern emerges that does not fit any of the three composed documents, that is a refinement candidate per the index doc's Evolution section.
