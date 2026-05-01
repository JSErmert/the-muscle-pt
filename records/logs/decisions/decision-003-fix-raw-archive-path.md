---
decision_id: decision-003-fix-raw-archive-path
date: 2026-04-30
type: decision
status: closed
relevant_doctrine:
  - CLAUDE.md (Section 3)
commit: 9b90963
---

# Decision

Fix the raw archive path reference in CLAUDE.md Section 3 from `records/system-history/raw/` to `records/raw/`.

---

# Context

A repository audit on 2026-04-30 found that CLAUDE.md Section 3 referenced the raw archive at `records/system-history/raw/`, but the actual file system path is `records/raw/` (one directory level shallower).

The audit caught this as part of broader CLAUDE.md reference verification. All other system-component references resolved correctly; only the raw archive path was off.

---

# Reasoning

This is a doctrine integrity repair — same class of fix as the M1 Plan's Phase 0 issues. Per HL-08, silent edits to core artifacts are not permitted; the repair gets a logged decision.

CLAUDE.md is the governance-layer surface; broken path references degrade the system's ability to source structured outputs from the raw archive when needed.

---

# Resolution

Edit Section 3 — Raw Archive Location — to point at `records/raw/`.

This was committed alongside an experimental clinical-citation rule that was later reverted (see decision-001). The path fix itself was not reverted because the original path reference was a genuine bug, not a premature M2 feature.

---

# Consequence

CLAUDE.md Section 3 now resolves correctly. No downstream impact — the path was never being followed by code; the fix is for human and model readability when sourcing the raw archive.

Note: The architecture and research specs reference at least three different storage paths for research records (`research/captured/`, `research/mapped/`, `/research/records/`, and the actual `records/research/`). This is the same class of bug. See refinement-001 for related M2 implications.
