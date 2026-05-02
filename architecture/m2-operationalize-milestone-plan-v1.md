# THE MUSCLE PT — OPERATIONALIZE M2 MILESTONE PLAN v1

## Purpose

Activate the research layer (M2) on top of the validated M1 baseline. Run real signal through every M2 component the system specifies. Produce the records that prove M2's central promise — research-grounded decisions and content production — is operational, not theoretical.

This milestone is authored alongside compressed Phase 2 capture per decision-013 and decision-014. M1 remains in active use; M2 layers on top.

---

## Anti-Goals (binding for the entire milestone)

- No M3 introduction (carousel pipeline, automation, audit) until M2 closes
- No new research-layer doctrine files beyond what's referenced here (Bootstrap v1, Index & Traceability v1, Query Layer v1, Research-to-System-Mapping v1, Content Output Contract v1)
- No bulk research record creation without per-record validation through the Bootstrap process
- No M2 citation surfacing in M1 outputs by default — citations appear only when significantly informative or explicitly requested

If any of the above tempts you mid-milestone: log to `records/logs/refinements/`, do not act.

---

## Acceptance Criteria

M2 is operationalized when ALL of the following are true and verifiable from `records/`:

1. ≥ 5 fully populated research records exist in `records/research/captured/` AND `records/research/mapped/` per the 3-layer Bootstrap structure (metadata + L1 source capture + L2 insight + L3 system mapping)
2. `records/research/index.md` exists per the Research Index & Traceability spec, with ≥ 5 entries linking research → use cases → system mappings
3. ≥ 3 research queries logged per the Research Query Layer format — each tied to a real use case from M1 capture or the founder archive
4. ≥ 1 forward query (problem → research) and ≥ 1 reverse query (research → system behavior) demonstrably resolvable through the index
5. ≥ 1 content piece produced via the Content Output Contract v1 with verified PMID + exact figure citation, passing all 8 overarching pass criteria
6. The 5 INPUT COMMANDS acceptance test set (per `2026-05-01-content-output-contract-source.md`) passes ≥ 4 of 5
7. ≥ 1 clinical decision response in dual-stream testing surfaces a citation that materially shapes the recommendation
8. M2 closeout document at `records/logs/reviews/monthly/m2-operationalization-closeout.md`
9. M3 scope decision logged with explicit HL-09 / HL-10 gate evaluation

Time horizon: 1–2 weeks (compressed, parallel to Phase 2 per decision-013). Hard cap: 4 weeks. If not closed by week 4, the milestone itself becomes the learning signal — escalate as incident.

---

## Phase 0 — Doctrine Integrity (≤ 1 day, blocking)

The M2 doctrine files are now in repo. Verify cross-references resolve:

- `research-layer-bootstrap-v1.md` ✓
- `research-index-and-traceability-v1.md` ✓
- `research-query-layer-v1.md` ✓
- `research-to-system-mapping-v1.md` ✓ (existing)
- `content-output-contract-v1.md` ✓
- CLAUDE.md Section 1 lists all M2 components ✓
- CLAUDE.md Section 2 → Content Creation references the contract ✓
- CLAUDE.md Section 7 specifies M2 citation format (PMID + exact figure) ✓

Path canonicalization confirmed: `records/research/{captured,mapped,archived}/` per architecture-tree-v1.md and Bootstrap v1.

If any reference fails to resolve during use, log as incident immediately.

---

## Phase 1 — First Research Record (≤ 1 day, blocking)

Per Bootstrap v1's First Activation Rule: create one fully populated research record before any scaling.

First record must:
- Be based on a real published study with verified PMID
- Follow the full 3-layer structure (metadata + L1 + L2 + L3)
- Map to a real use case (recommended starter domain: rib / breathing mechanics, given its appearance in the cold-test surface and the founder's content archive)
- Be stored at `records/research/captured/research-001-<slug>.md` and mapped at `records/research/mapped/research-001-<slug>.md`

Until this record exists, M2 is not active. M1 outputs continue without citations.

---

## Phase 2 — M2 Capture (Weeks 1–2)

### 2.1 Research Records — Weekly
Per Bootstrap v1, scale by adding one record per new topic that surfaces in:
- M1 case work (Stream A or Stream B)
- Founder archive extraction
- Content production needs

Target: ≥ 5 fully populated records by end of week 2.

Domains drawn from cold-test + content-contract surface area:
- Rib / breathing mechanics
- Hip impingement / overuse running injury
- Knee pain classification (meniscal, PFP, weakness)
- Rotator cuff loading + shoulder impingement
- Static stretching effects on force production (for Fact or Fiction bucket)

### 2.2 Research Index — Continuous
Per Research Index & Traceability v1: as records are created, populate `records/research/index.md` with:
- Research ID, topic, use cases
- System mappings (case engine, decision, rule candidates, constraint candidates)
- Content mappings
- Source references (PMID, link, title)
- Confidence level

Target: ≥ 5 indexed entries by end of week 2.

### 2.3 Research Queries — As Triggered
Per Research Query Layer v1: when a real input surfaces a question that has no research backing, log a query before the research is sought.

Stored at `records/research/queries/query-NNN-<slug>.md` (or inline in the index — TBD by usage).

Target: ≥ 3 queries by end of week 2.

### 2.4 Content Output via Contract — Weekly
Per Content Output Contract v1: produce ≥ 1 content piece per week using the contract, with verified PMID + exact figure citation, passing all 8 overarching criteria.

Target: ≥ 2 content pieces by end of week 2.

### 2.5 Acceptance Test Run — End of Week 2
Run the 5 INPUT COMMANDS from `2026-05-01-content-output-contract-source.md` as a regression suite.

Target: ≥ 4 of 5 pass.

---

## Phase 3 — Reflection & Loop Closure (concurrent)

Weekly review extends from M1 to include M2-specific signals:
- Which research records actually informed decisions or content
- Which queries surfaced gaps the system can't yet answer
- Citation accuracy / fabrication risk (zero tolerance)
- Forward/reverse query resolution time

Output: `records/logs/reviews/weekly/YYYY-WW.md` (extended from M1 weekly review template).

---

## Phase 4 — Closeout & M3 Scope Decision

### 4.1 M2 Closeout Self-Audit

Run each M2 component against captured records:

- **Bootstrap v1:** Does each record follow the 3-layer structure? Any orphaned entries?
- **Index & Traceability v1:** Forward/reverse queries resolvable? Mappings actionable?
- **Query Layer v1:** Each research entry traceable to a real use case query?
- **Content Output Contract v1:** Did the 5 INPUT COMMANDS pass? Where did drift occur?

Findings written to `records/logs/reviews/monthly/m2-operationalization-closeout.md`.

### 4.2 M3 Justification Gate

For every candidate M3 addition (carousel pipeline, scoring, hook generator, golden run, end-to-end validation, automation):

- Name the documented repeated failure in `records/` that justifies it
- Cite specific incident / refinement / failed-case files
- If no documented repeated failure exists, the addition fails HL-10 — defer or drop

Resolution of refinement-002 (M3 reordering question — swap / collapse / drop) is a precondition for any M3 staging decision.

### 4.3 Doctrine Refinement (only if signal demands)

If closeout surfaces ≥ 2 instances of the same M2 doctrine breaking under real use:
- Refinement entry per Bridge §10 Evolution Model
- Bump version of the affected file only

---

## Reporting Surface

The M2-active runtime must answer:

- "What research backs this clinical recommendation?" → resolves via Index forward query
- "Which decisions did this study influence?" → resolves via Index reverse query
- "What's the PMID and exact figure for this claim?" → resolves via record metadata + L1 key_results
- "Has this question already been researched?" → resolves via Query Layer + Index

And must REFUSE correctly:
- Fabricated PMIDs or invented figures → refuse per Bootstrap v1 §Failure Conditions
- Citations without source records → refuse per Index validation rules
- Bulk research generation without use case → refuse per Query Layer §Scaling Rule

---

## Failure Modes To Watch

- Research records created but not indexed → orphaned records, log as incident
- Citations surface in M1 outputs by default → translation drift, log as incident
- PMID + exact figure fabrication → highest-severity incident; halt M2 surfacing immediately
- 5 INPUT COMMANDS pass < 4 of 5 → log per criterion, identify drift, refine before continuing
- Compressed window approaches week 2 with < 5 research records → escalate; either extend window or revise acceptance criteria

---

## Definition of Done

M2 is operationalized when:
- ≥ 5 fully populated and indexed research records exist
- The Content Output Contract test set passes ≥ 4 of 5
- M2 closeout document exists
- M3 scope decision is logged with HL-09 / HL-10 gate evaluation
- refinement-002 (M3 reordering) is resolved

Only then does M3 become a legitimate planning candidate.

---

## SYSTEM SUMMARY

Activate paths.
Create one real record.
Validate structure.
Index and trace.
Query before researching.
Produce content per contract.
Test the 5 inputs.
Decide M3 from evidence.
