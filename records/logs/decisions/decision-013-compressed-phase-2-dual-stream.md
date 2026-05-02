---
decision_id: decision-013-compressed-phase-2-dual-stream
date: 2026-05-01
type: decision
status: open (Phase 2 in progress)
relevant_doctrine:
  - architecture/system-evolution-doctrine-v1.md
  - governance/hard-locks-v1.md (HL-10)
  - execution/execution-playbook-v1.md (v2)
linked:
  - decision-012-m1-cold-test-passed
phase: M1 Operationalize Plan v1 — Phase 2 (operational capture), compressed
---

# Decision

Compress Phase 2 from the original 4–6 week horizon to **1–2 weeks**. Run two parallel evidence streams to compensate for the reduced window. Substitute HL-10's *"≥ 2 documented repeated failures in records/"* gate with three pre-existing evidence sources.

This is a deliberate, logged trade-off — not a quiet violation of the M1 Plan.

---

# Context

The M1 Plan's 4–6 week Phase 2 horizon is tied to the 7-day content performance lag and the need for ≥ 2 occurrences to identify repeated patterns with statistical confidence.

The founder (builder, Josh) is choosing to compress to 1–2 weeks because:
- Operational momentum matters more than statistical purity at this stage
- The transcript already contains detailed M2 architecture (#21, #23, #26) ready to port
- Years of operational signal already exist in the founder archive
- The cold-test cycle has already produced one real incident → refinement loop (incident-001 → refinement-003)

Without compensating measures, this would violate HL-10. Compensating measures below.

---

# Two-Stream Capture Design

**Stream A — Zach's natural use:**
- Zach uses the Claude.ai project normally with no logging burden
- Chats persist in his Claude.ai history
- Cadence: exports at end of week (1–2 total exports over the compressed window)
- Transfer method: per-chat export via ⋮ menu → Download → sent to Josh
- Storage location: `records/system-history/raw/`
- File naming: `zach-chat-export-2026-WW-NN.md` where WW is ISO week and NN is sequence

**Stream B — Josh's archive-driven parallel:**
- Josh runs sessions in his own Claude.ai (separate project to keep streams clean)
- Prompts pulled from `records/system-history/raw/founder-claude-conversation-archive.md` material
- Logs directly into records as he goes (no post-hoc processing required)
- Generates `records/cases/`, `records/content/`, `records/research/`, and `records/system-history/extracted/` entries in real time

**Trade-off acknowledgment:**

| | Stream A (Zach) | Stream B (Josh) |
|---|---|---|
| Volume | Lower | Higher |
| Authority | Real operational signal | Archive-derived |
| Logging friction | Post-hoc processing | Direct log-as-you-go |
| Evidence type | Novel | Re-extracted |

Combined: ~2x record volume with two complementary evidence types.

---

# Substitute Evidence for HL-10

Instead of the literal *"≥ 2 documented repeated failures in records/"* gate, accept evidence from:

1. **`records/system-history/raw/founder-claude-conversation-archive.md`** — 18,608 lines of operational signal documenting the founder's reasoning, decisions, and friction across years. This is the same evidence layer the original system was built from.
2. **`incident-001` + `refinement-003`** — already-logged proof that the system can fail, surface the failure, and self-correct on its own surface. This satisfies the *spirit* of HL-10's "documented repeated failure" requirement (the cold test demonstrated a 5-of-7 pattern, not a single anomaly).
3. **Transcript MDs #21, #23, #26** — M2 architecture authored against the same use case during the original system design; not theoretical, but operationally grounded by the founder.

Together these substitute for fresh repeated-failure evidence within `records/`.

---

# Compressed Phase 2 Acceptance Criteria

| Criterion (M1 Plan §Acceptance) | Original | Compressed | Justification |
|---|---|---|---|
| Cases captured | ≥ 8 | ≥ 3 | Tests capture workflow under load |
| Content with 7-day perf | ≥ 8 | ≥ 3 (whatever window available) | Acknowledges 1-2 weeks won't yield full 7-day perf on most pieces |
| Research entries fully mapped | ≥ 3 | ≥ 1 | Proves M2 pipeline end-to-end |
| Founder-archive extractions | ≥ 4 | ≥ 1–2 (one per week) | Maintains Stream B baseline |
| Weekly reviews | ≥ 4 | 1–2 | One per week |
| Monthly review | ≥ 1 | Optional | Window may not justify |
| Decision + refinement | ≥ 1 each | Already satisfied | decision-001 through decision-012, refinement-001 through refinement-003 |
| Closeout document | required | required | Still mandatory |
| M2 scope decision with HL-09/HL-10 gate | required | required (with substitute evidence above) | Still mandatory |

Full flywheel cycle traceability still required: ≥ 1 case → insight → content → audience → feedback → logged decision/refinement.

---

# What Is Given Up

- Statistical confidence on repeated-pattern identification
- Content performance validation past one week
- A robust monthly review window
- Strict letter of HL-10 (the spirit is preserved via substitute evidence)

# What Is Preserved

- Capture workflow tested under real load
- Records tree exercised end-to-end
- Translation failures still caught and logged
- M2 plan grounded in rich existing evidence rather than thin new evidence
- Two-stream variation provides cross-validation Stream-A-only would lack

---

# Stream A Processing Protocol

When Zach's weekly export arrives:

1. Save to `records/system-history/raw/zach-chat-export-2026-WW-NN.md` verbatim
2. Read through and extract:
   - **Case events** → format per `case-state-model-v1` and `case-outcome-reporting-v1` → `records/cases/active/case-NNN-<slug>.md`
   - **Insights** → format per `system-history-extraction-format-v1` → `records/system-history/extracted/`
   - **Translation failures** → `records/logs/incidents/`
   - **Recurring patterns (≥ 2x)** → `records/logs/refinements/` per ET-03
3. Log a weekly review to `records/logs/reviews/weekly/2026-WW.md` per Playbook v2 §6
4. Note any direct quotes that should land in patterns (`records/system-history/patterns/`) for future reference

---

# Resolution

- Compressed Phase 2 begins immediately upon Zach receiving the project access
- Stream B (Josh's archive-driven sessions) can begin in parallel without waiting on Zach
- Phase 4 closeout writes to `records/logs/reviews/monthly/m1-operationalization-closeout.md` as planned
- The M2 scope decision at Phase 4 must explicitly cite which substitute evidence sources justify each M2 candidate

---

# Consequence

Phase 2 produces records faster than the original plan would have, with the trade-offs above logged transparently. M2 plan can begin authoring as soon as compressed Phase 2 closes, using transcript MDs as foundation and substitute evidence as justification.

If the compression turns out to under-produce evidence, that itself is the learning signal — log as incident, extend the window or revise the substitute-evidence policy.
