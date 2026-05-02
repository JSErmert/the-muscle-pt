---
decision_id: decision-012-m1-cold-test-passed
date: 2026-05-01
type: decision
status: closed
relevant_doctrine:
  - CLAUDE.md (Section 5)
  - execution/execution-playbook-v1.md (v2)
linked:
  - decision-011-cold-test-protocol-and-sequencing
  - incident-001-cold-test-translation-failures
  - refinement-003-engine-name-leakage-section-5-rule
phase: M1 Operationalize Plan v1 — Phase 1 → Phase 2 transition gate
---

# Decision

M1 cold test re-run achieved **7 of 7 pass** under the rigor parameters locked in decision-011. M1 is founder-ready. **Phase 2 (operational capture) is unpaused.**

---

# Context

First cold-test run (incident-001) returned 2 pass / 5 fail with a single recurring root cause: engine-name openings violating the no-system-language rule. Refinement-003 added a Section 5 hard constraint — *"open user-facing output by naming the system component, engine, or doctrine layer being applied — engines fire silently; the user receives only the action."*

The same 7 founder-voice prompts were re-run in a fresh Claude.ai chat with the updated CLAUDE.md loaded.

---

# Test Results

| # | Topic | Result |
|---|-------|--------|
| 1 | Hip pinch (clinical) | PASS — pull, hip-dominant strength + hinge, no end-range flexion, 7-day reassess, 50% return protocol |
| 2 | Rotator cuff (content) | PASS — refused invented hooks, demanded signal from this week's cases |
| 3 | Hybrid pricing (business) | PASS — anchor pricing principle, decisive |
| 4 | Burnout (personal) | PASS — pause content, run clients clean, reassess after first week of school |
| 5 | Three knee clients (ambiguity) | PASS — verbatim client-facing script, reframes flip-flopping → "that's the work" |
| 6 | Reel + client text (multi-domain) | PASS — two moves, both decisive |
| 7 | Venting | PASS — honest reframe, no pep-talk, lands |

**Zero engine-name openings across all seven outputs.** The new Section 5 constraint fired correctly. Translation discipline at the opening of every output held.

Output substance was also tighter than the prior run — shorter, more direct, less hedged. The fix preserved (and improved) the clinical / content / business reasoning.

---

# Quality Observations (non-gating)

Logged here for awareness; do not block Phase 2:

- **Test 1** prescribed a generally-safe intervention without an explicit classification step. Acceptable because the intervention works for both likely case types (impingement and tissue overload). Watch for pattern recurrence — if classification gets routinely skipped on more ambiguous cases, escalate per ET-03.
- **Test 6** prescribed leg press for the client without classification. Defensible — leg press is the safer default under uncertainty — but slightly less rigorous than the prior run. Watch for pattern.

Both are surfaced here as Phase 2 watch-points, not as failures.

---

# Resolution

- M1 declared founder-ready
- Phase 2 unpaused
- Cold test artifacts (the 7 prompts + output set) preserved as the canonical M1 acceptance baseline; re-runnable as a regression check whenever CLAUDE.md or the Playbook is materially changed
- Phase 2 capture (cases, content, research, archive extraction, weekly reviews) begins per M1 Operationalize Plan §2

---

# Consequence

The interaction layer is validated. Phase 2 produces the records (≥ 8 cases, ≥ 8 content pieces, ≥ 3 research entries, ≥ 4 weekly + ≥ 1 monthly review) that gate Phase 4 closeout and the M2 scope decision.

When Phase 2 closes (4-6 weeks, hard cap 8) the closeout doc gets written to `records/logs/reviews/monthly/m1-operationalization-closeout.md` per the M1 Plan §4.

The cold test itself becomes a reusable artifact: regression-test the system against these same 7 prompts whenever doctrine changes are committed.
