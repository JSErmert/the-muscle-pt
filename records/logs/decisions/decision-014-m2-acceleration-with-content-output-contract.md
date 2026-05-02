---
decision_id: decision-014-m2-acceleration-with-content-output-contract
date: 2026-05-01
type: decision
status: open (M2 in progress)
relevant_doctrine:
  - architecture/system-evolution-doctrine-v1.md
  - architecture/m2-operationalize-milestone-plan-v1.md
  - execution/content-output-contract-v1.md
  - systems/intelligence/research-layer-bootstrap-v1.md
  - systems/intelligence/research-index-and-traceability-v1.md
  - systems/intelligence/research-query-layer-v1.md
  - CLAUDE.md (Sections 1, 2, 7)
linked:
  - decision-013-compressed-phase-2-dual-stream
  - decision-001-lock-m1-revert-citation-rule (superseded — M2 conditions now met)
phase: M2 acceleration (parallel to compressed Phase 2)
---

# Decision

Accelerate M2 introduction. Bring the research layer online during the compressed Phase 2 window rather than after Phase 2 closes.

This is a strategic reversal of the conservative staging applied earlier in this session. The conditions that justified delay no longer apply.

---

# Why the Reversal Is Justified

When the citation hard-lock was reverted (decision-001), the conditions were:
- M1 was not yet validated
- No substitute evidence for HL-10 existed in `records/`
- M2 was attempted as a single rule patch with no architecture
- Research records were empty
- The rule failed to fire as intended

The conditions now are different:
- **M1 is validated** — cold test passed 7/7 (decision-012)
- **Substitute evidence is locked** (decision-013): founder archive, cold-test failure-correction loop, transcript MDs
- **M2 architecture is in repo** — Bootstrap v1, Index & Traceability v1, Query Layer v1, Research-to-System-Mapping v1, Content Output Contract v1 ported and reconciled with CLAUDE.md
- **Testing scenario explicitly requires M2** — Zach is a clinician; uncited clinical advice is degraded operating mode for him

Pulling M2 in now isn't a violation of the M1 lock. It's the lock's purpose being fulfilled. M1 was meant to validate the interaction layer so M2 could be added with confidence.

---

# Triggering Source

A founder-authored content output contract (saved verbatim at `records/system-history/extracted/2026-05-01-content-output-contract-source.md`) materially expanded the M2 scope. The earlier framing of M2 as *"research grounding for clinical decisions"* was too narrow.

M2 is the engine that powers the content production workflow. Research grounding (PMID + exact figures) is necessary infrastructure. The output contract defines the actual user-facing artifact spec.

---

# Resolution

Actions taken in this session:

1. **Saved source spec** verbatim to `records/system-history/extracted/2026-05-01-content-output-contract-source.md` per `system-history-extraction-format-v1`
2. **Authored `execution/content-output-contract-v1.md`** — codifies voice contract, format contract, caption contract, citation contract (PMID + exact figure above three dots), 5-bucket auto-tagging, 8 overarching pass criteria
3. **Ported transcript MDs** from `ChatGPT-AI Impact and Transformation.md`:
   - #21 Research Layer Bootstrap v1 → `systems/intelligence/research-layer-bootstrap-v1.md`
   - #23 Research Index & Traceability System v1 → `systems/intelligence/research-index-and-traceability-v1.md`
   - #26 Research Query Layer v1 → `systems/intelligence/research-query-layer-v1.md`
4. **Updated CLAUDE.md:**
   - Section 1 now lists Content Output Contract v1 alongside core systems and adds a Research layer (M2) sub-list
   - Section 2 → Content Creation references both the flywheel (when) and the output contract (what)
   - Section 7 now specifies the M2 citation format (PMID + exact figure) with default behavior — citations surface only when significantly informative or explicitly requested; M1 outputs remain citation-free by default
5. **Authored `architecture/m2-operationalize-milestone-plan-v1.md`** — Phases 0–4, compressed to 1–2 weeks parallel to Phase 2, with acceptance criteria scaled appropriately and tied to substitute evidence per decision-013

---

# What This Does NOT Do

- Does not retire M1 — M1 remains in active use; M2 layers on top
- Does not introduce M3 — explicitly deferred per M2 plan Anti-Goals
- Does not surface citations in default M1 output — only when significantly informative or explicitly requested
- Does not bulk-populate research records — Bootstrap v1's "one fully populated record before scaling" rule still binds

---

# Pending Work

- Phase 1 of M2 plan (the first fully populated research record) has not yet been authored. This is the next blocking step. Recommended starter: rib / breathing mechanics (high overlap with cold test surface area and content archive)
- The 5 INPUT COMMANDS acceptance test set has not yet been run against the system — this is part of Phase 2 capture
- refinement-002 (SED v1 M3 reordering question — swap / collapse / drop) remains open and must resolve before the M3 scope decision at M2 closeout

---

# Consequence

The dual-stream compressed Phase 2 (per decision-013) now runs against the M1 + M2 stack. Stream A (Zach) gets research grounding when relevant; Stream B (Josh's archive-driven sessions) generates research records as it goes.

M2 closeout produces the artifact set that gates M3 scope evaluation. M2 takes 1–2 weeks (hard cap 4) to operationalize. If the compressed window under-produces evidence, that is itself the learning signal — log as incident, extend window or revise acceptance criteria.
