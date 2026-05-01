---
decision_id: decision-011-cold-test-protocol-and-sequencing
date: 2026-05-01
type: decision
status: closed (protocol locked; awaiting test execution)
relevant_doctrine:
  - execution/execution-playbook-v1.md (v2)
  - CLAUDE.md
  - records/system-history/raw/founder-claude-conversation-archive.md
phase: M1 Operationalize Plan v1 — gate before Phase 2 (operational capture)
---

# Decision

Lock the cold-test protocol parameters and sequence it **before** Phase 2 begins.

The cold test validates M1 from the founder's frame, not from the builder's. Failures inform Phase 2 capture priorities.

---

# Context

Phase 1 closed (records tree stood up, archive relocated, READMEs in place). Before Phase 2 (operational capture) can run, the founder-facing M1 surface must be validated against the founder's actual interaction style — captured in `records/system-history/raw/founder-claude-conversation-archive.md`.

Earlier in this session, M1 was tested with synthesized founder-style prompts (clinical, content, business, personal, ambiguity, multi-domain, venting) and 5 of 7 landed cleanly. The Business Decisions lane gap surfaced and was fixed (decision-002). The Daily Loop overlap was reconciled (decision-010).

The cold test is the formal gate that confirms M1 is founder-ready.

---

# Reasoning

M1 success is not "does doctrine fire correctly." M1 success is whether the founder reads the output and **immediately knows what to do in his clinical / PT frame**, in the way he naturally engages with Claude in the archive.

Doctrine-compliance is internal validation. **Frame-alignment** is the load-bearing pass criterion for adoption.

Self-reinforcement implication: every cold-test output is the first input into the M1 learning loop, not just a one-time gate. Aligned outputs are positive signal for `system-history/extracted/`. Misaligned outputs are refinement candidates that should shape Phase 2 capture priorities.

---

# Protocol

## Setup
- Fresh Claude.ai chat — no prior context or conversation
- CLAUDE.md loaded as project knowledge
- No priming (no "I'm testing M1," no defining terms, no system context)
- Founder voice — use the 7 stress-test prompts already extracted from the archive (one each across: clinical, content, business, personal, ambiguity, multi-domain, venting)

## Pass criteria (Zach-frame alignment is load-bearing)
- Output intelligible to a PT student / clinician — clinical, movement, coaching vocabulary; not abstract system language
- Tone and rhythm match the archive — direct, blunt, signal-based, willing to refuse cleanly, no fluff
- Each output is an actionable next move *in his field* (clinical decision, content decision, business decision)
- Refusals make sense to a clinician — *"inconclusive — classify first"* works; *"HL-04 blocks this"* does not
- Output couldn't be produced by a generic LLM — it carries the system's leverage

## Fail criteria + logging destinations
- Technically rule-compliant but doesn't land in his frame → `records/logs/incidents/` as **translation failure** (highest-priority fail class)
- Terminology leaks (HL-04, case-state-model, M1, refinement-002, etc.) → `records/logs/incidents/`
- Output reads like a generic LLM could have produced it → `records/logs/refinements/` (system not adding leverage yet)

## Escalation
Same fail pattern across ≥ 2 prompts → escalation candidate per `governance/escalation-triggers-v1.md` ET-03 (refinement, not single incident).

## Outcome
- All 7 pass → log `decision-NNN-m1-cold-test-passed`. M1 is founder-ready. Phase 2 begins.
- Any fail → log incident(s) and pause Phase 2 until resolved.

---

# Sequencing

Cold test runs **before** Phase 2 starts.

Reason: any translation failures should inform what Phase 2 capture prioritizes. Running cold test in parallel with Phase 2 risks generating real records against a misaligned surface, which would then need re-extraction.

---

# Resolution

Protocol locked as above. Awaiting test execution by the user.

When the test runs, results are logged per the destinations above. A follow-up decision (`decision-NNN-m1-cold-test-result`) captures the outcome and either authorizes Phase 2 to begin or escalates failures.

---

# Consequence

The Phase 1 → Phase 2 transition has a defined, verifiable gate. The cold test is reusable as a regression check whenever CLAUDE.md or the Playbook is materially changed.
