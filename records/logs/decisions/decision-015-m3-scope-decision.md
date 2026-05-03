---
decision_id: decision-015-m3-scope-decision
date: 2026-05-02
type: decision
status: closed (M3 scope formally evaluated; all candidates DEFER pending Phase 2 evidence)
relevant_doctrine:
  - architecture/m2-operationalize-milestone-plan-v1.md (§4.2 M3 Justification Gate; reclassified per refinement-002)
  - architecture/master-operating-system-governance-bridge-v1.md (HL-09, HL-10, §10 Evolution Model)
  - records/logs/refinements/refinement-002-sed-v1-m3-reordering-question.md (resolved 2026-05-02; M3 = Automation per the renumbered staging)
linked:
  - records/logs/reviews/monthly/m2-operationalization-closeout.md (Section 9 set up this decision)
  - records/logs/decisions/decision-014-m2-acceleration-with-content-output-contract.md (M2 acceleration that produced the evidence base evaluated below)
phase: M2 closeout (acceptance criterion #10)
---

# Decision

**M3 scope: defer all candidates.** No M3-Automation candidate has documented repeated failure justifying it at this point. Per HL-10, additions without documented repeated failure must defer or drop. Each candidate is evaluated below; each currently fails the HL-10 gate.

**M3 stays empty until Phase 2 dual-stream surfaces specific failures that automation would prevent.**

This decision satisfies M2 acceptance criterion #10 ("M3 scope decision logged with explicit HL-09 / HL-10 gate evaluation").

---

# Context

Per the M2 milestone plan §4.2 and the now-resolved refinement-002 (DROP M3 audit; renumber M4 → M3 Automation), the M3 layer is now exclusively about **automation / efficiency / scaling**. Audit-equivalent functions are continuous disciplines embedded across all layers (per refinement-002's resolution).

The candidate list from the original §4.2 (carousel pipeline, scoring, hook generator, golden run, end-to-end validation, automation) has been reclassified:

- **Audit-flavored candidates** (scoring as quality rubric, golden run as manual regression, end-to-end validation as discipline) → continuous disciplines, NOT M3 candidates. They live in Content Output Contract v1, Index & Traceability v1, milestone closeouts, and Bridge §10 Evolution Model.
- **Automation-flavored candidates** (carousel pipeline, hook generator, automated scoring, automated golden run / harness, automated end-to-end validation, generic automation infrastructure) → M3-Automation candidates, evaluated against HL-10 below.

---

# HL-10 Gate Evaluation per Candidate

HL-10: *No addition without documented repeated failure justifying it.* Each candidate must name the documented repeated failure in `records/` that justifies the addition and cite specific incident / refinement / failed-case files. Absence of documented repeated failure → defer or drop.

## Candidate 1 — Carousel Pipeline

- **Documented repeated failure:** **None.**
- **Evidence:** The system has produced 2 content pieces (content-001 Bucket 1 / Why Should You Care; content-002 Bucket 3 / Fact or Fiction). Neither is a carousel. No carousel work has been attempted; no carousel-specific failure has been logged.
- **HL-10 verdict:** **FAILS — DEFER.**
- **Reasoning:** Cannot justify automation for a content type the system has not yet produced manually. Bootstrap v1's First Activation Rule applies in spirit: don't automate before manually validating the production pattern.
- **Revisit trigger:** Phase 2 dual-stream produces ≥ 3 manually-authored carousels showing a repeated failure pattern (e.g., consistent slide-flow drift, citation placement issues, voice inconsistency across slides) that automation would specifically prevent.

## Candidate 2 — Hook Generator

- **Documented repeated failure:** **None.**
- **Evidence:** Hook in content-001 ("Your neck pain might not actually be your neck") and content-002 ("Your neck pain has nothing to do with your breathing") were author-generated and passed criterion 1 (sounds like founder, provisional pending ear-test) and criterion 5 (correct bucket auto-tagging). No hook-specific drift documented in incident-001, incident-002, or any refinement entry.
- **HL-10 verdict:** **FAILS — DEFER.**
- **Reasoning:** Cannot justify automation for a function that has not produced any documented failure. The 2-piece sample is small but the criterion-1 ear-test is the binding constraint, not the hook generation step.
- **Revisit trigger:** ≥ 3 documented occurrences of hook-related criterion failure (banned phrases sneaking in, criterion-5 mis-tagging due to ambiguous hook, sub-10-word constraint violations) in dual-stream Phase 2 production.

## Candidate 3 — Generic Automation Infrastructure

- **Documented repeated failure:** **None.**
- **Evidence:** M2 has been entirely human-driven through this session. No scaling pressure has surfaced — the bottleneck has been authoring depth, not throughput. Per the M2 closeout, internal progress has been substantial without automation.
- **HL-10 verdict:** **FAILS — DEFER.**
- **Reasoning:** Automation infrastructure without a specific failure to address is bulk-creation antipattern at the system-architecture level. Per Bridge §10.2 Expansion Rule: "only expand when (a) repetition is proven (b) friction is consistent (c) value of structure outweighs cost." None of these conditions are met.
- **Revisit trigger:** Phase 2 dual-stream produces sustained throughput friction that manual approach cannot service (e.g., > 5 cases/week with content production demands exceeding founder capacity, or weekly review backlog accumulating).

## Candidate 4 — Automated Scoring System

- **Documented repeated failure:** **None.**
- **Evidence:** The 8 overarching pass criteria in Content Output Contract v1 are already a manual scoring rubric. They have been applied successfully in content-001 and content-002 (both pass with disclosed caveats). incident-002 (the pre-output Bucket 3 catch) demonstrates the manual scoring approach catches drift mid-flow.
- **HL-10 verdict:** **FAILS — DEFER.**
- **Reasoning:** Manual scoring is working. Automating it would not have changed any documented outcome to date. Premature automation locks in current rubric assumptions and reduces the system's ability to refine criteria as Phase 2 produces new patterns.
- **Revisit trigger:** ≥ 5 documented cases where manual rubric application produced inconsistent results across reviewers, OR throughput requirements make manual rubric application untenable.

## Candidate 5 — Automated Golden Run / Regression Harness

- **Documented repeated failure:** **None.**
- **Evidence:** Two manual regression test sets exist and are functioning:
  - **7 founder-voice prompts** (M1 cold test) — went 5/7 → 7/7 after Section 5 engine-name leakage fix (refinement-003); regression test working
  - **5 INPUT COMMANDS** (M2 acceptance test) — 2 of 5 banked manually with citation discipline catching drift (incident-002)
  Both manual regression suites have caught drift and validated fixes. No automation-specific failure surfaced.
- **HL-10 verdict:** **FAILS — DEFER.**
- **Reasoning:** Manual regression is working as designed. The cost of running the manual sets is low (acceptable per current scale). Automating would prematurely lock in current test fixtures, when Phase 2 may produce additional fixtures that should be added incrementally.
- **Revisit trigger:** Regression test set grows beyond ~15 test cases AND running them manually consumes > 1 hour per cycle, OR a documented case where manual regression missed a failure that automated regression would have caught.

## Candidate 6 — Automated End-to-End Validation

- **Documented repeated failure:** **None.**
- **Evidence:** The M2 index validation exercise (`records/research/validation/2026-05-01-index-query-resolution-exercise.md`) and the M2 closeout audit are end-to-end validation running manually. Both have produced useful outputs (forward/reverse/output query patterns confirmed; component-level audits documented).
- **HL-10 verdict:** **FAILS — DEFER.**
- **Reasoning:** Same as Candidate 5 — manual approach is working. End-to-end validation is performed at meaningful intervals (closeouts, refinement events, doctrine updates), not continuously, so automation gain is limited.
- **Revisit trigger:** ≥ 3 milestone closeouts where manual end-to-end audit took > half a day each AND surfaced no novel findings (suggests automation would replace genuinely repetitive manual work).

---

# Aggregate HL-10 Result

**6 of 6 M3-Automation candidates FAIL HL-10 at this point.** None has documented repeated failure justifying it. **DECISION: DEFER ALL.**

This is the disciplined HL-10 outcome. The system has not yet generated the failure-evidence base required to justify automation additions. M3 stays empty until that evidence accumulates.

---

# HL-09 Compliance Check

HL-09: *No fabricated grounding.* This decision satisfies HL-09 because:

1. We are explicitly declining to add automation grounded in nothing-but-anticipation
2. Each candidate's evaluation cites the *absence* of documented failure as the reason for deferral, not a substituted (and potentially fabricated) claim of justification
3. The trigger conditions for revisiting are specific, observable, and grounded in failure types that would be documented per existing incident/refinement protocols
4. The decision itself is documented (this file) with explicit reasoning, satisfying the no-fabricated-grounding standard for governance decisions

---

# Trigger Conditions for Revisiting M3 Candidates

Per HL-10 and this decision, M3 candidates can be revisited when:

1. **Phase 2 dual-stream produces documented repeated failures** of a specific type that a specific automation candidate would prevent. The threshold is the standard refinement threshold per ET-03 (recurring pattern) — typically N=3 occurrences before formal refinement.

2. **Scaling pressure surfaces** — manual capacity becomes insufficient for sustained throughput (e.g., > 5 cases/week, content production demands exceeding founder time, weekly review backlog accumulating).

3. **Doctrine evolution surfaces a specific gap** — e.g., the 5 INPUT COMMANDS test set grows beyond manual capacity, or a regression suite needs CI integration.

4. **A specific incident demonstrates that manual approach failed** where automation would have caught the issue — e.g., a published content piece slips a citation drift past manual review, that an automated rubric scorer would have flagged.

When any trigger fires, the corresponding candidate is re-evaluated against HL-10. Trigger firing is necessary but not sufficient — the documented evidence still must justify the specific candidate.

---

# Implications

## For M2 Acceptance

- **Acceptance criterion #10 satisfied** — M3 scope decision is logged with explicit HL-09 / HL-10 gate evaluation per this document
- M2 progress moves to **8 of 11 acceptance criteria fully satisfied**

## For M3 Layer

- M3 stays operationally empty pending evidence
- The renumbered staging (M1 Decision, M2 Research, M3 Automation per refinement-002) is in effect, with M3 currently uninstantiated
- Audit-equivalent functions remain continuous disciplines per refinement-002

## For Phase 2 Dual-Stream

- Phase 2 should explicitly track whether any of the M3 candidates would have helped — log occurrences as data toward future M3 candidate justification
- The 5 INPUT COMMANDS test, ongoing content production, and case work are all opportunities to surface failures that would justify specific M3 additions
- Per ET-03 threshold: log occurrences; escalate to refinement at N=3; consider M3 candidate re-evaluation thereafter

## For System-Level Governance

- This decision exercises HL-10 at a structural level (the M-layer staging itself), demonstrating the gate works at scale not just at rule-candidate level
- Future structural additions (a hypothetical M4, additional doctrine layers, etc.) face the same HL-10 standard

## For SED v1 Documentation

- The standalone `architecture/system-evolution-doctrine-v1.md` file (still pending per refinement-002 resolution) should incorporate this decision's reasoning about M3 staying empty pending evidence
- The 3-layer staging (M1, M2, M3-Automation) is canonical
- Audit as continuous discipline is canonical

---

# What This Decision Does NOT Do

- **Does not declare automation universally undesirable** — it declares automation un-justified *at this point* given current evidence
- **Does not preclude future M3 additions** — trigger conditions are specified for each candidate
- **Does not replace continuous improvement** — manual processes will continue to be refined per Bridge §10 Evolution Model
- **Does not block Phase 2 dual-stream** — Phase 2 proceeds as designed (per decision-013)
- **Does not retire the M3 candidate list** — the candidates remain on the docket as Phase 2 evidence accumulates
- **Does not authorize new doctrine files** — this decision is logged in records/logs/decisions/; no new doctrine is created. The standalone SED v1 file remains a separate open item per refinement-002

---

# Pending Work (Not Blocked by This Decision)

- Author standalone `architecture/system-evolution-doctrine-v1.md` (open follow-on from refinement-002)
- Update `architecture/m2-operationalize-milestone-plan-v1.md` §4.2 to reflect the reclassification (this decision can be referenced; the milestone plan update is a small documentation cleanup)
- Update M2 closeout document to mark criterion #10 satisfied (small edit)

---

# Consequence

M2 enters its final closure phase with:
- 8 of 11 acceptance criteria fully satisfied
- Remaining gaps are external dependencies on Phase 2 dual-stream (content founder ear-test; ≥1 clinical decision citation surfacing; remaining INPUT COMMANDS) and small documentation tasks
- M3 layer is staged-but-empty, ready to receive evidence-justified additions when Phase 2 surfaces them

The disciplined deferral here is itself a system-validation moment — HL-10 protected the architecture from premature automation that would have locked in untested patterns. Phase 2 is the appropriate evidence-generation window; until then, the manual approach remains in force.

---

# Last Updated

2026-05-02 — initial M3 scope decision authored.
