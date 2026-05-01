---
decision_id: decision-002-add-business-decisions-lane
date: 2026-05-01
type: decision
status: closed
relevant_doctrine:
  - CLAUDE.md (Section 2)
commit: 0a474dd
---

# Decision

Add a `### Business Decisions` lane to CLAUDE.md Section 2, alongside Client Work, Content Creation, Decision Making, and Prioritization.

---

# Context

During M1 founder-style stress testing on 2026-05-01, Test 3 (RF Fitness pricing model question) returned: *"Out of scope. The Muscle PT system covers client work, content, and governance — not pricing strategy."*

The system flagged its own boundary cleanly, but the boundary was wrong: the founder needs pricing, packaging, hiring, scaling, and partnership decisions handled inside the system, not deferred outside it. The existing `Decision Making` lane was being interpreted as internal-system-decisions only, not business decisions.

---

# Reasoning

This is M1 lane completion, not M2 expansion. The founder operates a coaching/PT business; pricing and scaling are core daily decisions, not adjacent ones. Refusing them as out-of-scope leaves a major decision surface uncovered.

The new lane uses the same governance components (Governing Logic, Decision Preferences, Hard Locks, Prioritization Queue) but is scoped explicitly to business operations. An `Out of scope` list (legal, tax, accounting) preserves the discipline of the system flagging boundaries that genuinely need outside experts.

---

# Resolution

Inserted into Section 2 between `Decision Making` and `Prioritization`:

```
### Business Decisions

Use:
- Governing Logic
- Decision Preferences
- Hard Locks
- Prioritization + Queue Engine

Focus:
- pricing
- packaging
- hiring
- scaling
- partnerships / equity

Out of scope:
- legal
- tax
- accounting
```

---

# Consequence

Re-running Test 3 produced an engaged inconclusive output ("price RF Fitness at the level your current group clients would already pay") instead of an out-of-scope refusal. Confirmed lane derivation works.

This change is M1, not M2 — the lane addition completes M1 scope; it does not introduce research grounding or any other M2 capability.
