---
decision_id: decision-008-phase0-update-translation-rules-version-ref
date: 2026-05-01
type: decision
status: closed
relevant_doctrine:
  - CLAUDE.md (Section 7)
  - governance/output-translation-rules-v1.md
phase: M1 Operationalize Plan v1 — Phase 0 fix #4
---

# Decision

Update CLAUDE.md Section 7 reference from "Apply Output Translation Rules v1" to "Apply Output Translation Rules v4."

---

# Context

Phase 0 doctrine integrity audit identified a version-reference mismatch:

- CLAUDE.md Section 7 referenced "Output Translation Rules v1"
- The actual file `governance/output-translation-rules-v1.md` self-identifies as v4 in its title (`# THE MUSCLE PT — OUTPUT TRANSLATION RULES v4`)

The filename retained `v1` for stability (no rename), but the doctrine inside has evolved to v4. CLAUDE.md was reading from a stale version reference.

---

# Reasoning

Per HL-08, version references must match. A reader following the CLAUDE.md reference would expect v1 doctrine and instead encounter v4 — which is a silent doctrine drift hazard.

The fix is one word: change the version number in the reference. No file rename, no doctrine edit.

---

# Resolution

CLAUDE.md Section 7 line updated from "Apply Output Translation Rules v1" to "Apply Output Translation Rules v4."

The file `governance/output-translation-rules-v1.md` keeps its current filename. Future major doctrine evolutions in this file may warrant a filename version bump, but that is not required by Phase 0.

---

# Consequence

CLAUDE.md now cites the correct version of the active Output Translation Rules doctrine. No behavioral change — the doctrine inside the file has been v4 throughout this M1 lock period; only the reference was stale.
