---
refinement_id: refinement-002-sed-v1-m3-reordering-question
date: 2026-05-01
date_resolved: 2026-05-02
type: refinement
status: resolved (DROP M3 audit; renumber M4 → M3 Automation)
relevant_doctrine:
  - architecture/system-evolution-doctrine-v1.md (referenced but no standalone file exists; staging is documented across CLAUDE.md, milestone plans, and refinement-002 itself)
  - architecture/m2-operationalize-milestone-plan-v1.md §4.2 (M3 Justification Gate — implications below)
linked_artifacts:
  - records/logs/reviews/monthly/m2-operationalization-closeout.md (interim closeout that surfaced the resolution-readiness)
  - records/logs/incidents/incident-002-bucket-3-pre-output-citation-catch.md (evidence that audit-equivalent function is M2-embedded, not M3-staged)
  - records/research/validation/2026-05-01-index-query-resolution-exercise.md (evidence that validation runs during M2 work, not as separate M3 phase)
  - architecture/master-operating-system-governance-bridge-v1.md §10 (Evolution Model — already defines continuous audit-equivalent disciplines)
---

# Observation

System Evolution Doctrine v1 currently stages the milestones as:

- M1 — Decision Layer (interaction)
- M2 — Research-Aware Layer (knowledge grounding)
- M3 — Self-Auditing Layer (validation / trust)
- M4 — Automation Layer (efficiency / scaling)

During M1 review on 2026-05-01, the founder placed automation ("carousel injected temporal saving technological wiring") at M3 — collapsing or reordering the audit layer.

The staging is internally inconsistent until this is resolved.

---

# Trigger

Conversation on 2026-05-01 immediately following the Business Decisions lane addition (decision-002). The founder's framing put automation/tooling at M3, which conflicts with SED v1's M3 = Self-Auditing.

---

# Open Question

Three resolutions to choose from:

1. **Swap:** M3 ↔ M4. Automation comes before audit. Implies audit is a post-automation discipline.
2. **Collapse:** M3 absorbs both audit and automation — audit emerges through automation use rather than as a separate layer.
3. **Drop:** Remove M3 audit as a discrete milestone — it becomes a continuous discipline applied across all layers, not its own staging.

Each has different implications for the M2→M3 gate criteria. The criteria cannot be authored until this is resolved.

---

# Resolution — 2026-05-02

**Decision: DROP M3 audit. Renumber M4 → M3 Automation. SED v1 collapses from 4 layers to 3.**

## New SED v1 Staging

- M1 — Decision Layer (interaction)
- M2 — Research-Aware Layer (knowledge grounding)
- M3 — Automation Layer (efficiency / scaling) [formerly M4]

Audit becomes a **continuous discipline** embedded across all layers, not a discrete milestone.

## Reasoning — Why Drop, Not Swap or Collapse

The M2 acceleration session (2026-05-01) produced concrete evidence that audit-equivalent functions are *not* waiting for a separate M3 stage — they were operating continuously throughout M2 work itself:

1. **incident-002 (pre-output Bucket 3 citation drift caught).** The Content Output Contract v1's citation discipline halted production, surfaced the drift, pivoted the claim, and corrected the upstream L3 mapping — all *during* M2 content production, not as a post-hoc audit step. The audit-equivalent function is *embedded in M2 doctrine*, not deferred to M3.

2. **Index query resolution exercise (`records/research/validation/2026-05-01-index-query-resolution-exercise.md`).** Forward, reverse, and output queries were validated against the populated index *during* M2 work. The validation exercise is structurally an audit operation, but it lived inside M2 — not as a separate M3 phase.

3. **M2 closeout document (`records/logs/reviews/monthly/m2-operationalization-closeout.md`).** The closeout itself audits each M2 component (Bootstrap v1, Index & Traceability v1, Query Layer v1, Content Output Contract v1) against captured records. The audit is a *milestone-end discipline*, not a separate sequential layer. This is consistent with how every M-layer should close out.

4. **Master Operating System Governance Bridge §10 Evolution Model.** Already defines audit-equivalent functions as continuous discipline:
   - §10.2 Expansion Rule (only expand when repetition is proven, friction is consistent, value of structure outweighs cost)
   - §11 Failure Modes (over-governance, over-structuring, system drift) — continuous concerns, not staged ones
   - §4 Escalation Path / Levels — continuous, not staged

5. **Founder framing (the original trigger).** The founder placed automation at M3 because that's how they actually think about the post-M2 layer — efficiency/scaling. The audit-equivalent function does not match this framing because it's *not what the post-M2 stage is for* in operational practice. The audit is woven through every layer's operation.

### Why Not Swap (M3 ↔ M4)?

Swap would put audit AFTER automation. This is mechanically wrong — automation amplifies whatever is in the system. Automating before validating means automating drift. But also: *the system is already producing audit-equivalent output continuously through M2*. The function isn't waiting for M4 — it's already happening. Swap doesn't match observed behavior.

### Why Not Collapse (M3 + M4)?

Collapse would imply audit is a function of automation infrastructure (e.g., automated regression testing, golden run validation). This has some merit — automated validation IS valuable. But it would mean M2 is operationally complete *without* validation infrastructure, contradicting what the M2 closeout just demonstrated (closeout audit). It also creates an enormous, ill-defined combined layer. Collapse fails the clarity test.

### Why Drop Works

Drop matches observed behavior:
- Audit-equivalent functions ARE running continuously
- They're embedded in M2 doctrine (Content Output Contract v1's citation discipline; Index & Traceability v1's validation)
- They run at milestone close (closeout documents)
- They run through the Bridge §10 Evolution Model continuously
- The M-layer staging becomes 3 layers (cleaner) without losing any function

Drop also aligns with the founder's automation-at-M3 framing without forcing the founder to adopt an audit-stage mental model that doesn't match how the system actually operates.

## Implications for M2 Milestone Plan §4.2 (M3 Justification Gate)

The original §4.2 listed candidates: *carousel pipeline, scoring, hook generator, golden run, end-to-end validation, automation*.

Under the renumbered model, this list needs reclassification:

| Original candidate | New classification |
|---|---|
| Carousel pipeline | **M3-Automation candidate** — evaluate against HL-10 |
| Scoring | **Audit-equivalent → continuous discipline** when used as quality rubric; **M3-Automation candidate** when implemented as automated scoring system |
| Hook generator | **M3-Automation candidate** — evaluate against HL-10 |
| Golden run | **Audit-equivalent → continuous discipline** when used as manual regression test; **M3-Automation candidate** when implemented as automated harness |
| End-to-end validation | **Audit-equivalent → continuous discipline** for the validation function itself; **M3-Automation candidate** when implemented as automated infrastructure |
| Automation | **M3-Automation candidate** — evaluate against HL-10 |

Audit-flavored functions (scoring as rubric, golden run as manual regression, end-to-end validation as discipline) are now embedded in:
- **Content Output Contract v1** — citation discipline, banned phrases, 8 overarching pass criteria, drift catch
- **Index & Traceability v1** — forward/reverse/output query validation
- **Bootstrap v1** — 3-layer structure compliance, First Activation Rule
- **Master Operating System Governance Bridge §10** — Evolution Model, expansion discipline
- **Milestone closeout documents** — component audits at milestone end

Automation-flavored candidates (carousel pipeline, hook generator, automation infrastructure) become M3-Automation candidates, evaluated against HL-10 (documented repeated failure justifying the addition).

## Implications for M3 Scope Decision (Acceptance Criterion #10)

Refinement-002 was the gating precondition for the M3 scope decision. With this resolution:

1. The M3 scope decision can now proceed
2. M3 candidates are reclassified per the table above
3. Audit-equivalent candidates are out of scope for the M3 scope decision (they live as continuous disciplines)
4. Automation-flavored candidates remain in scope, evaluated against HL-10
5. Per the M2 closeout's preliminary HL-10 evaluation, **most automation-flavored candidates currently fail HL-10** (no documented repeated failure justifying them)
6. Likely M3 scope decision outcome: defer all automation candidates pending Phase 2 dual-stream evidence of repeated failures justifying specific automation additions

## Implications for Standalone SED v1 Doctrine File

The resolution surfaced that **no standalone `architecture/system-evolution-doctrine-v1.md` file exists** in the repo, despite refinement-002 (and likely other artifacts) referencing it. The staging has been described in:
- This refinement (informal)
- M2 milestone plan (operational)
- CLAUDE.md Section 1 (M2 layer reference only)

Action required: a formal SED v1 file should be authored documenting the now-3-layer staging (M1 Decision, M2 Research, M3 Automation) plus the continuous audit discipline pattern. **This is a separate task from this resolution.** Logged here as an open documentation item; should be authored before M3 scope decision is finalized so the staging it operates against is canonical.

## Action Status

**Resolved 2026-05-02.** Decision: DROP M3 audit; renumber M4 → M3 Automation; audit becomes continuous discipline.

Open follow-on items (separate tasks, not blocking this resolution):
1. Author standalone `architecture/system-evolution-doctrine-v1.md` reflecting the 3-layer staging
2. Update `architecture/m2-operationalize-milestone-plan-v1.md` §4.2 to reclassify M3 candidates per the table above
3. Make the M3 scope decision (acceptance criterion #10) — now unblocked

## Last Updated

2026-05-02 — refinement resolved. DROP M3 audit; renumber M4 → M3 Automation; audit-equivalent functions documented as continuous disciplines embedded across all layers.
