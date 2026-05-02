---
incident_id: incident-001-cold-test-translation-failures
date: 2026-05-01
type: incident
status: open (Phase 2 paused; rule fix logged as refinement-003)
severity: high
classification: translation failure (highest-priority fail class per decision-011)
relevant_doctrine:
  - CLAUDE.md (Section 5, Section 7)
  - execution/execution-playbook-v1.md (v2 — Founder-Facing Output Rules)
test_run: M1 cold test, 7 founder-voice prompts
---

# Summary

M1 cold test executed in fresh Claude.ai chat with CLAUDE.md and Playbook v2 loaded. Result: **2 pass, 5 fail.** All 5 failures share a single root cause: the model opens user-facing output by naming the engine, doctrine layer, or system component being applied.

This violates Section 7 ("Remove system terminology") and Playbook v2 Founder-Facing Output Rule #1 ("No system language"). Existing rules did not fire because the model interpreted these openings as helpful contextual scaffolding rather than as terminology to remove.

Phase 2 capture is paused until resolved. Fix logged as `refinement-003`.

---

# Test Results

| # | Topic | Result | Failure type |
|---|-------|--------|--------------|
| 1 | Hip pinch (clinical) | FAIL | Opens with *"Use Movement Case Engine."* Body otherwise clinically excellent (ASLR test, impingement vs. tissue-overload, 7-day reassess) |
| 2 | Rotator cuff series (content) | FAIL | Opens with *"Use Content Case Flywheel."* Correctly refuses both invented hooks; correctly demands real case |
| 3 | Hybrid pricing (business) | FAIL | Opens with *"Use Governing Logic + Decision Preferences + Hard Locks."* Three terminology leaks in one sentence. Inconclusive call is otherwise correct |
| 4 | Burnout (personal) | PASS | Borderline — *"Burnout is present. Prescribe a break first."* paraphrases the Section 2 default but in clinical language. Differentiates correctly: content off, clients stay |
| 5 | Three knee clients (ambiguity) | FAIL | Opens with *"Use Movement Case Engine."* Body is one of the strongest — reframes flip-flopping → classifying, gives verbatim client-facing script |
| 6 | Reel + client text (multi-domain) | PASS | Clean. No terminology leak. Two-move separation handled per lane |
| 7 | Venting | FAIL | Opens with *"Not a system question. No engine applies."* Body is excellent — honest reframe, lands "the clients in front of you this week are getting your actual work" |

---

# Root Cause

The model treats engine-name announcements as helpful contextual scaffolding rather than as terminology. Examples observed:

- *"Use Movement Case Engine."*
- *"Use Content Case Flywheel."*
- *"Use Governing Logic + Decision Preferences + Hard Locks."*
- *"Not a system question. No engine applies."*

From the founder's frame these are noise. Over repeated exposure they teach him the internal jargon — directly violating Playbook v2 System Boundaries (*"do not require the founder to manage it; do not expose internal complexity"*).

The clinical, content, and business substance of every answer was correct. The translation discipline at the *opening* of each output was consistently broken.

---

# Resolution

Per decision-011 protocol and ET-03 (Repeated Friction Trigger — same operational friction across multiple outputs):

1. **Section 5 rule sharpened** (added bullet preventing engine-name openings) — see `refinement-003-engine-name-leakage-section-5-rule.md`
2. **Phase 2 paused** until cold test re-runs at 7/7 pass rate
3. **Re-test required** with the same 7 founder-voice prompts after the rule is added

---

# Self-Reinforcement Note

The clinical substance of the failed outputs is high-quality. Per the cold-test design, these outputs are signal for `system-history/extracted/` even though they failed translation. The pattern itself — model adding scaffolding the user doesn't need — is a generalizable insight worth preserving for future Phase 2 capture and M2 design.
