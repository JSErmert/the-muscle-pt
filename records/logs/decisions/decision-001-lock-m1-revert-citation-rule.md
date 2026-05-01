---
decision_id: decision-001-lock-m1-revert-citation-rule
date: 2026-04-30
type: decision
status: closed
relevant_doctrine:
  - architecture/system-evolution-doctrine-v1.md
  - CLAUDE.md (Section 5)
commit: 1e2053b
tag: m1-baseline
---

# Decision

Lock CLAUDE.md as the validated M1 baseline. Revert the clinical-citation hard-lock that had been added to Section 5.

---

# Context

A Section 5 constraint had been added requiring clinical recommendations to cite *exact source, line, and link from the research mapping system*; if no verified source existed, the rule directed the model to classify as inconclusive per Section 8.

In testing, the rule did not fire as intended. The research library (`records/research/`) was empty, but the model continued producing clinical recommendations from training rather than failing through to the inconclusive output. Worse, the rule pulled M2-layer behavior (research grounding) into M1, which violates the staged evolution discipline.

---

# Reasoning

System Evolution Doctrine v1 is explicit about the failure mode this triggered:

> **Failure Modes to Avoid — Overloading Early Layers:** Forcing research, audit, or automation into M1 outputs.

The citation rule was an M2 capability inserted into M1 with no M2 infrastructure to back it. SED v1's M1 specifies *"no citations"* and M2 specifies *"citations appear only when explicitly requested"* — both contradicted the rule we had introduced.

---

# Resolution

- Revert the citation hard-lock from Section 5
- Keep the path fix from the same commit (`records/system-history/raw/` → `records/raw/`) — that was a real bug, see decision-003
- Tag commit as `m1-baseline` on the remote
- Defer all research-grounding work to the M2 plan

---

# Consequence

M1 is locked. Future clinical answers will be M1-style (decisive, no citations) until M2 is authored on top of populated research records. The decision to skip the citation rule is captured here so future readers understand why the commit history shows the rule briefly existing before being removed.
