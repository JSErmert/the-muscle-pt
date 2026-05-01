---
decision_id: decision-010-fold-daily-loop-into-execution-playbook-v2
date: 2026-05-01
type: decision
status: closed
relevant_doctrine:
  - execution/execution-playbook-v1.md (now internally v2)
  - governance/decision-preferences-v1.md (DP-09, DP-11, DP-12)
phase: M1 Operationalize Plan v1 — Phase 1 follow-on (pre-Phase 2 reconciliation)
---

# Decision

Fold the Founder Daily Operating Loop v1 (drafted earlier in session, not yet committed as a separate file) into `execution/execution-playbook-v1.md`. Bump the playbook's internal version to **v2**.

The Daily Loop does not become a standalone doctrine file. The Playbook is the canonical execution surface.

---

# Context

The Daily Loop and the existing Playbook v1 had substantial overlap, including direct duplicates:

- Both prescribed End-of-Day signal capture (one insight + one pattern + one notable case)
- Both prescribed weekly review cadence
- Both covered content workflow with similar structure

The Loop also added behavioral content the Playbook did not have:

- Morning Priority Activation with strict output format
- Founder-Facing Output Rules (no system language, one action, minimal explanation, no overload)
- "What the System Replaces" before/after value statement
- "What Success Feels Like" qualitative markers
- Explicit Failure Indicators with incident-logging triggers
- System Boundaries (broader "must NOT" list)

Two doctrine surfaces saying the same thing in different depths is the same drift class as:
- decision-001 (premature M2 citation rule)
- decision-004 (redundant tool-introduction prohibition in output-translation-rules-v1)

---

# Reasoning

DP-09 (Prefer Fewer Tools Used Well), DP-11 (Prefer Compression Over Expansion), and DP-12 (Prefer System Reuse Over One-Off Solutions) all point to a single execution surface, not two.

Combined, the Loop and Playbook v1 are tighter than either alone. The Playbook keeps its governance framing. The Loop's behavioral specificity, output rules, and failure-mode discipline get folded in.

Filename stays `execution-playbook-v1.md` (matches the convention used by `output-translation-rules-v1.md`, which is internally v4). Internal title is now `EXECUTION PLAYBOOK v2`.

---

# Resolution

`execution/execution-playbook-v1.md` rewritten as Execution Playbook v2 with the following structure:

1. Morning — Priority Activation (Loop addition)
2. During Work — Signal Capture (Loop classification + Playbook v1 §1 Sessions)
3. Real-Time Execution — Action Guidance (Loop rules + Playbook v1 §4 + §7)
4. End of Day — Signal Compression (deduplicated, with explicit storage path + format reference)
5. Content Extraction (Playbook v1 §2 + Loop's stricter Case→Insight→Content rule)
6. Weekly Review — Direction Control (Playbook v1 §3 + Loop's ≥2x triggers + 4-domain health scoring)
7. Priority Rule — When Unsure (Playbook v1 §5)
8. Failure Rule — When Unclear (Playbook v1 §6)
+ Founder-Facing Output Rules (Loop)
+ What the System Replaces (Loop)
+ What Success Feels Like (Loop)
+ System Boundaries (Loop, broader)
+ Failure Indicators (Loop, with incident-logging triggers)
+ Definition of Success (Loop)
+ One-Line System Identity (Loop)
+ System Summary (Playbook v1, extended)

The standalone Daily Loop document is not committed. Its content lives in v2.

---

# Consequence

A single execution surface for the founder. Phase 2 capture references only `execution-playbook-v1.md` (v2 internally). Future founder-facing behavioral additions extend this file rather than spawning parallel docs.

CLAUDE.md does not currently version-reference this file; no CLAUDE.md update needed.

The cold test (decision-011) measures the founder-facing surface — which is now this Playbook v2.
