---
refinement_id: refinement-004-research-layer-vs-authoring-mode-correction
date: 2026-05-03
date_resolved: 2026-05-03
type: refinement (architectural correction to decision-017)
status: resolved 2026-05-03 — Research Layer / Authoring Mode separation locked + full closed-loop authoring discipline established
trigger: fresh-chat test results 2026-05-03 — Tests 1–6 (Clinical Mode) failed to surface Research Layer citations across all six sessions despite CLAUDE.md saying "Clinical Mode | Movement Case Engine + Research Layer (for citations)"; Test 10 (Research Mode) stopped at query draft instead of executing the full closed loop. Both failures trace to the same architectural confusion in decision-017 — Research framed as a Mode without distinguishing the passive grounding service from the active authoring discipline.
relevant_doctrine:
  - records/logs/decisions/decision-017-mode-activation-pattern.md (parent decision being corrected)
  - records/logs/decisions/decision-016-lane-abstraction-for-content-production.md (lane abstraction — unaffected)
  - CLAUDE.md (Mode Activation table requires correction)
  - systems/intelligence/research-layer-bootstrap-v1.md (3-layer structure + First Activation Rule — orchestrated by Authoring Mode)
  - systems/intelligence/research-index-and-traceability-v1.md (index discipline)
  - systems/intelligence/research-query-layer-v1.md (no abstract research; real input source required)
  - systems/intelligence/research-to-system-mapping-v1.md (L3 mapping discipline)
linked_artifacts:
  - records/research/validation/2026-05-02-fresh-chat-test-protocol.md (Test 10 baseline requires correction)
  - Tests 1–6 fresh-chat results 2026-05-03 (Clinical Mode citation surfacing failure across all six sessions)
  - Test 10 fresh-chat results 2026-05-03 (Research Mode stopped at query draft)
  - records/research/queries/query-009 (placeholder — to be authored as the first execution of corrected Research Authoring Mode for stretch-mediated hypertrophy)
hl_09_evaluation: PASS — refinement preserves no-fabricated-grounding discipline; the closed loop explicitly mandates PubMed-direct verification at step 4, exact-figure extraction at step 5, and confidence calibration at step 10. Tightens HL-09 enforcement, does not loosen it.
hl_10_evaluation: PASS — refinement is correction of an architectural confusion surfaced by documented test failures (six Clinical Mode sessions + Test 10). Documented current need. The closed-loop authoring discipline formalizes what was already done manually for research-001 through 005 + 008; making the implicit explicit is the spirit of HL-10, not an expansive addition.
---

# Observation

Decision-017 (Mode Activation Pattern, 2026-05-02) defined six modes including "Research Mode" that activates "Research Layer (Bootstrap, Index, Query, Mapping)." This framing conflates two architecturally distinct things:

1. **Research as a passive grounding service** — citations surface across other modes when significantly informative (CLAUDE.md §7). No mode declaration required to access. This is *the layer doing its grounding job*.

2. **Research as an active authoring discipline** — explicit operator-invoked work to add new records to the layer. Includes PubMed search, PMID verification, 3-layer record authoring, indexing, cross-record implications. This is *the layer being expanded*.

Decision-017's "Research Mode" verb only addresses #2 (authoring), but the Mode Activation table mentions Research Layer alongside Clinical Mode (implying #1). The conflation is real and produced two specific failures in the 2026-05-03 fresh-chat test set.

# Trigger — Two Documented Failures

## Failure 1 — Research Layer citations did not fire in Clinical Mode (Tests 1–6)

Across **all six Clinical Mode test sessions** (Cold and Primed × three cases), no PMIDs surfaced. Despite the Mode Activation table specifying "Clinical Mode | Movement Case Engine + Research Layer (for citations)," the citations did not surface.

| Test | Case | Expected citation | Surfaced? |
|---|---|---|---|
| 1, 2 | Case A (founder, laxity substrate) | research-008 (PMID 35609204) for "stop stretching the right upper trap"; research-006 disclosed as ungrounded for TMJ | NO |
| 3, 4 | Case B (desk worker, mechanical) | research-001 (PMID 24835338) for thoracic-cervical chain; research-005 (PMID 40576779) for neural mobilization | NO |
| 5, 6 | Case C (borderline screen-and-branch) | research-008 + research-003 as branch-context citations | NO |

The clinical reasoning was correct in all six sessions — the chain was identified, the right intervention staged, the right cautions applied. **What was missing was research grounding.** Recommendations that materially deviate from default (e.g., "stop stretching the trap" — which contradicts standard practice) require explicit research grounding per CLAUDE.md §7. The fresh chat reasoned its way to the right answer without surfacing the layer that grounds it.

**Diagnosis:** the fresh chat read "Research" as a sibling mode and treated Clinical Mode as research-disconnected. The "+ Research Layer (for citations)" line in the Mode Activation table did not override this reading — likely because "Research" appears as its own mode in the same table.

## Failure 2 — Research Mode stopped at query draft (Test 10)

Test 10 input: *"Research Mode. Need a record on stretch-mediated hypertrophy. Script lane references it. We don't have grounding yet. Walk me through what we'd need."*

The fresh chat produced exemplary discipline at the wrong scope:
- Drafted query-009 in proper Query Layer v1 format
- Named candidate seed papers (Maeo et al., Kassiano et al., Schoenfeld) without fabricating PMIDs
- Followed Bootstrap v1 First Activation Rule
- Specified what input source is needed before authoring
- Refused to proceed without operator-supplied seed paper

This was *correct discipline at the wrong scope*. It stopped at step 2 of the 10-step closed loop because the docs framed Research Mode as a "consult Bootstrap/Index/Query/Mapping" pattern rather than as an "execute the full authoring loop end-to-end" pattern.

**The full closed loop is what was done manually for research-001 through 005 + 008.** The fresh chat had no path to execute it because the docs didn't specify the loop existed.

# Resolution — 2026-05-03

Both failures resolve through one architectural correction.

## Architecture correction

| Concept | Type | Definition | Activation |
|---|---|---|---|
| **Research Layer** | Always-on passive service | Provides grounding citations to other modes when significantly informative per CLAUDE.md §7. | Implicit. No mode declaration required. Active across Clinical, Insight, Script, and Business modes (and any future grounding-relevant lane). |
| **Research Authoring Mode** | Operator-invoked active discipline | Executes the full 10-step closed-loop authoring of new research records: gap → query → PubMed search → verification → 3-layer record → index → cross-record implications. | Explicit operator command: "Research Authoring Mode" (or alias "Research Mode"). Invokes the closed loop with three operator-in-the-loop confirmation gates. |

## The Closed Loop — 10 Steps

What was done manually for research-001 through 005 + 008 is now formalized as the canonical Research Authoring Mode execution:

| Step | Action | Discipline | Gate? |
|---|---|---|---|
| 1 | **Gap identification** — surface need from real input (case, lane reference, closeout flag, recurring system pattern) | Query Layer v1 — no abstract research; real input source required | — |
| 2 | **Query draft** — log to `records/research/queries/` in Query Layer v1 format with use case, core question, mechanism focus, decision target, constraints | Query Layer v1 format | — |
| 3 | **PubMed search** — execute web search / PubMed-direct query for candidate seed papers | No fabrication; PubMed-direct only | — |
| 4 | **PMID + figure verification** — pull candidate paper(s) from PubMed; verify PMID, abstract, study design, sample, exact figures with units | HL-09 strict; figures verbatim, never paraphrased | **Gate A** — operator selects among multiple candidates |
| 5 | **L1 source capture** — author `records/research/captured/research-NNN-...md` with metadata, source reference, abstract excerpt, study design, verified figures | Bootstrap v1 metadata + L1 structure | — |
| 6 | **L2 insight extraction** — within the same captured file, extract what the source actually establishes (effect sizes, confidence, scope, limitations, what it does NOT establish) | Bootstrap v1 L2 discipline | — |
| 7 | **L3 system mapping** — author `records/research/mapped/research-NNN-...md` with Case Engine mapping, Decision mapping, Rule Candidates, Constraint Candidates, Content Mappings | Research-to-System Mapping v1 | **Gate B** — operator confirms cross-record interactions, rule candidates, constraint candidates land correctly for the domain |
| 8 | **Index entry** — update `records/research/index.md` with full entry: use cases, system mappings, source reference, confidence, file pointers | Index & Traceability v1 — forward / reverse / output query patterns supported | — |
| 9 | **Cross-record implications** — identify promotions, sequencing refinements, horizontal modifier effects (e.g., research-008 modifies research-001/003/004/005; research-005 partially promoted research-002) | Cross-record interaction discipline | — |
| 10 | **Confidence calibration** — assign initial confidence (Low / Medium / Medium-High / High) with promotion criteria locked | Bootstrap v1 confidence rating discipline | **Gate C** — operator confirms calibration before lock |

## Operator-in-the-Loop Gates — 3 Gates

The closed loop fires end-to-end with three natural confirmation pauses:

- **Gate A — Seed Candidate Selection (after step 4).** When PubMed returns multiple plausible seed papers, the agent surfaces the candidates with their effect sizes / sample sizes / study designs / confidence levels and asks the operator which to lock. Protects against picking a weaker source when a stronger one exists.
- **Gate B — L3 Mapping Review (after step 7).** L3 mapping is domain-specific judgment work — Case Engine integration, Rule Candidates, Constraint Candidates, Content Mappings. The agent surfaces the draft mapping and asks the operator to confirm the cross-record interactions and clinical/practical applicability.
- **Gate C — Confidence + Cross-Record Promotion Review (after step 10).** Initial confidence assignment and any cross-record promotions are surfaced for operator review before the index entry locks. Protects against overclaiming and against missing cross-record implications.

Between gates, the agent runs the closed loop autonomously. Gates exist to anchor the operator's judgment at the points where it most matters; they do not require the operator to babysit every step.

## What this preserves

- **HL-09 strict.** Steps 3, 4, 5 enforce PubMed-direct verification. No PMID is cited without verification. Figures are extracted verbatim with units.
- **HL-10 strict.** Step 1 requires real input source (case, lane reference, closeout flag, recurring pattern). No abstract research, no bulk authoring, no records without trigger.
- **Bootstrap v1 First Activation Rule.** Records get authored only when triggers fire; closed loop honors this at step 1.
- **Operator authority.** Three gates ensure operator judgment lands at the highest-leverage points without requiring continuous involvement.

# Implications

## CLAUDE.md update required

Mode Activation table (added 2026-05-02 by decision-017) requires three corrections:

1. **Clinical Mode row:** remove "+ Research Layer (for citations)" — the layer is implicit, always-on across other modes. Adding it to the table created the conflation that caused the Tests 1–6 citation surfacing failure.
2. **Research Mode row:** rename to "Research Authoring Mode" with alias "Research Mode" preserved for backward compatibility. Update the activates column to: "Research Authoring closed loop — gap → query → PubMed search → verification → 3-layer record → index → cross-record implications. Three operator-in-the-loop gates."
3. **New brief note above the table:** "The Research Layer is always-on and grounds other modes' outputs with citations when significantly informative per CLAUDE.md §7. No mode declaration required to access. Research Authoring Mode is for adding records to the layer."

## Decision-017 amendment required

Decision-017's "Mode commands lock to lane doctrine" table requires the same correction. A small amendment section at the bottom of decision-017 should note the architectural correction and reference this refinement.

## Fresh-chat test protocol update required

Test 10 baseline correction: the test currently expects "drafts query OR flags input source needed before authoring." The corrected expectation is the full 10-step closed loop with three operator gates. Operator running Test 10 against corrected docs should see the agent draft query-009, run PubMed search, surface seed candidates at Gate A, and pause for operator selection.

The protocol's Phase 1 (Opus 4.7 fresh) results from 2026-05-03 should be re-run for Tests 1–6 (Clinical Mode citation surfacing should now fire) and Test 10 (closed loop should now execute) after the docs are corrected. Tests 7, 8, 9, 11 results stand — they were not affected by the layer/mode confusion.

## Bootstrap v1 — no structural change required

Bootstrap v1's 3-layer structure and First Activation Rule are unchanged. The closed loop orchestrates these existing disciplines into a single coherent execution flow with PubMed integration; it does not modify Bootstrap v1 itself.

## query-009 status

query-009 (stretch-mediated hypertrophy) was drafted at conceptual level by the Test 10 fresh chat output. The corrected Research Authoring Mode would execute steps 3–10 as the next move once query-009 is formally logged. This becomes the **first execution of corrected Research Authoring Mode** — both validates the closed loop AND fills the lane reference gap.

# Action Status

**Resolved 2026-05-03.** Architecture correction locked: Research Layer (passive, always-on) vs. Research Authoring Mode (active, full closed loop with 3 gates) cleanly separated. Closed loop's 10 steps formalized from the manual authoring of research-001 through 005 + 008.

**Follow-on tasks** (separate work, not blocking this resolution):

1. Update CLAUDE.md Mode Activation table per Implications section above
2. Amend decision-017 with reference to this refinement
3. Update fresh-chat test protocol — Test 10 baseline correction; flag Tests 1–6 for re-run after CLAUDE.md correction
4. Author query-009 (stretch-mediated hypertrophy) as the first formal execution of corrected Research Authoring Mode
5. Re-run fresh-chat Tests 1–6 and Test 10 against corrected docs to validate the architectural fix

# Last Updated

2026-05-03 — initial refinement entry authored. Trigger: 2026-05-03 fresh-chat test results showing Research Layer citation surfacing failure across Clinical Mode (Tests 1–6) and Research Mode stopping at query draft (Test 10). Resolution: separated Research Layer (passive grounding) from Research Authoring Mode (active full closed loop with 10 steps + 3 operator gates). HL-09 / HL-10 evaluations passed. Five follow-on tasks identified. The closed loop formalizes what was done manually for research-001 through 005 + 008.
