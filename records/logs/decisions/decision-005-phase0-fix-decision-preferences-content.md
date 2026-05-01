---
decision_id: decision-005-phase0-fix-decision-preferences-content
date: 2026-05-01
type: decision
status: closed
relevant_doctrine:
  - governance/decision-preferences-v1.md
  - architecture/master-operating-system-governance-bridge-v1.md
phase: M1 Operationalize Plan v1 — Phase 0 fix #1
---

# Decision

Replace the contents of `governance/decision-preferences-v1.md` with the actual Decision Preferences doctrine. The file previously contained the Master Operating System Governance Bridge content (mislabeled duplicate).

---

# Context

Phase 0 doctrine integrity audit identified that `decision-preferences-v1.md` was a mislabeled file: it contained the Governance Bridge content, which is properly stored in `architecture/master-operating-system-governance-bridge-v1.md`. The actual Decision Preferences doctrine (referenced by Bridge §3 and Governing Logic §5 as the layer between Hard Locks and Execution Judgment) was missing.

---

# Reasoning

Per HL-08, doctrine integrity must be repaired before operationalization. Two doctrine surfaces holding the same content (Bridge content in two places, Decision Preferences absent) creates drift risk and breaks reference resolution.

The corrected content was ported from the source ChatGPT transcript that produced the original system architecture. It defines DP-01 through DP-13 across content, client system, tool/workflow, and repo design preferences, plus a decision filter and a preference-promotion rule.

---

# Resolution

`governance/decision-preferences-v1.md` rewritten with the proper Decision Preferences v1 doctrine.

The Bridge content remains intact in `architecture/master-operating-system-governance-bridge-v1.md` (no change to that file).

---

# Consequence

Decision Preferences is now correctly resolvable from CLAUDE.md Section 2 (Decision Making, Business Decisions) and from cross-references in the Bridge and Governing Logic. The bias layer (DP-01..DP-13) is now operational doctrine, not aspirational.
