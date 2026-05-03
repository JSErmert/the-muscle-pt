---
exercise_id: live-case-retrieval-test-001
date: 2026-05-02
type: validation log
purpose: demonstrate end-to-end M2 retrieval pipeline on a raw first-person case input, producing a grounded plan in practitioner voice; validates the full forward-query → record retrieval → sequencing rules → hard locks → citation surfacing → output translation chain
acceptance_criteria_partially_advanced:
  - "Acceptance Criterion #4 — forward query demonstrably resolvable through index (already satisfied 2026-05-01; re-validated here on a richer multi-mechanism input)"
  - "Acceptance Criterion #8 — clinical decision surfaces a citation that materially shapes the recommendation: PIPELINE-VALIDATED in closed loop. Full satisfaction still requires Phase 2 dual-stream Stream A (Zach making a real clinical decision on a real patient)."
relevant_doctrine:
  - systems/intelligence/research-index-and-traceability-v1.md
  - systems/intelligence/research-query-layer-v1.md
  - systems/intelligence/research-to-system-mapping-v1.md
  - execution/content-output-contract-v1.md (citation format §7)
  - architecture/m2-operationalize-milestone-plan-v1.md
linked_records:
  - research-001 (Wirth 2014, PMID 24835338)
  - research-002 (Lutke Schipholt 2026, PMID 41620319)
  - research-003 (Ibrahim 2025, PMID 39818121)
  - research-004 (Carbone 2015, PMID 24458335)
  - research-005 (García-Juez 2025, PMID 40576779)
  - research-008 (Spanhove 2023, PMID 35609204)
  - research-006 (TMJ — planned, ungrounded; HL-09 disclosure required)
linked_queries:
  - query-001 (founder personal case, v5)
  - query-006 (TMJ, logged-unresolved)
  - query-008 (hypermobility/laxity constitutional substrate, resolved)
linked_artifacts:
  - records/research/validation/2026-05-01-index-query-resolution-exercise.md (precursor; single-record forward/reverse/output pattern validation)
  - records/logs/reviews/monthly/m2-operationalization-closeout.md (closeout document)
  - records/logs/decisions/decision-015-m3-scope-decision.md
  - records/logs/refinements/refinement-002-sed-v1-m3-reordering-question.md
---

# M2 Live Case Retrieval Test — 2026-05-02

This validation exercise confirms the M2 retrieval pipeline operates end-to-end on raw, unstructured, first-person patient input — surfacing the correct records, applying horizontal modifiers and sequencing rules, honoring hard locks, and producing a grounded clinical plan in practitioner voice that does not leak engine names.

The 2026-05-01 exercise validated each query pattern (forward / reverse / output) in isolation on simple inputs. This exercise validates the **full integrated pipeline** on a multi-mechanism input that exercises 7 distinct mechanism layers simultaneously — closer to real Stream A complexity.

---

## Test Design

**Input modality:** Raw first-person conversational description, the way a patient would actually describe their case to a clinician — not pre-structured.

**Expected output:** Clinician-voice plan grounded in M2 records, citations surfaced inline (per CLAUDE.md §7 because the grounding materially shapes the recommendation), no engine/layer names exposed, action override (one plan, no options).

**Voice target:** Zach (practitioner addressing the patient directly, brother-to-brother register).

**Test rationale:** Higher realism than a system-side query format. Validates that the retrieval pipeline can parse mechanism signatures from natural language, not just from explicit problem-statement queries. This is the form Stream A inputs will actually arrive in.

---

## Input — Raw First-Person Case (Founder, Josh)

> "My right side hurts. The right upper trap and neck — tight, sometimes inflamed, especially when I lean forward. Like at my desk hunched over, the whole right top of me feels pulled up tight. Funny thing though — when I drive my Jetta, the bowl seat actually makes the pain go down. I sit forward in it and the neck eases up. I've dislocated my right shoulder blade twice. Right TMJ snapped on me one time and ever since it clicks and I have this weird swallowing-pressure thing on the right. Tweaked my upper back / lower neck once doing some intense breathing work. My whole right side just feels lax — shoulder blade, jaw, the trap area, all loose on the right but not the left. Posterior chain on the right gets inflamed and wraps around in cycles. What do I do?"

---

## Pipeline Trace (system-side, fires silently in production)

### Step 1 — Mechanism Signature Parsing

| Signal in input | Mechanism layer detected |
|---|---|
| "right side lax — shoulder blade, jaw, trap, all loose on right but not left" | Constitutional asymmetric hyperlaxity |
| "right upper trap tight, inflamed, leaning forward makes it ride up" | Compensatory overactivity (classical hypermobility response) |
| "bowl seat sustained-flexion reduces pain" | External-stability unloads compensator (Wirth-pattern signature) |
| "2 right shoulder blade dislocations" | Post-dislocation scapular involvement |
| "right TMJ snapped, clicks, swallowing-pressure cycle" | TMJ subluxation history |
| "tweaked C-T junction under intense breathing" | Thoracic-cervical junction acute injury, breathing-provoked |
| "posterior chain right inflammation wrapping cycles" | Regional inflammation / sensitization pattern |

7 distinct mechanism signatures parsed from natural language input.

### Step 2 — Forward Query Resolution Through Index

| Record | Surfaced because | Status in plan |
|---|---|---|
| research-008 (Spanhove 2023, PMID 35609204) | Hypermobility horizontal modifier — applied FIRST | Active, governs frame |
| research-003 (Ibrahim 2025, PMID 39818121) | Regional inflammation cycles → CS-suspected; combined-modality sequencing | Active, applied |
| research-005 (García-Juez 2025, PMID 40576779) | Posterior chain neural component; conservative neural mobilization | Active, applied |
| research-001 (Wirth 2014, PMID 24835338) | Sustained-flexion paradoxical relief + thoracic-neck mechanical link | Active, applied |
| research-002 (Lutke Schipholt 2026, PMID 41620319) | Localized neuroinflammation mechanism (background mechanism) | Active, silent in surface output |
| research-004 (Carbone 2015, PMID 24458335) | Post-dislocation scapular dyskinesis | Active, absorbed into stability-first plan |
| research-006 (TMJ) | Right TMJ subluxation + chronic instability | Planned, ungrounded → HL-09 disclosure |

Index resolution depth: ≤ 2 lookups per record (Use Cases section + System Mappings section).

### Step 3 — Sequencing Rules and Hard Locks Applied

- **research-008 horizontal modifier** overrides default vertical sequencing → stability-first, closed-chain proprioceptive, eccentric over end-range, never stretch overactive compensator
- **RC-7 (research-003)** → combined-modality from day one, not mobility-first, given CS-suspected pattern
- **HL-09 (no fabricated grounding)** → TMJ disclosed as ungrounded; referred out
- **Citation surfacing rule (CLAUDE.md §7)** → grounding materially shapes recommendation → citations surface inline with PMID + exact figure
- **Action override (CLAUDE.md Hard Override)** → one plan, no options
- **Output translation (CLAUDE.md §7)** → engine names fire silently; no system terminology in patient-facing output
- **Reassessment markers** → 12-week reassess; connective-tissue workup escalation if right trap dominance and tightness do not drop with stability work

---

## Output — Practitioner Voice (Zach addressing Josh)

> Alright. Listen.
>
> Your right side is lax — shoulder blade, jaw, trap. That's the foundation. Everything else you're describing is downstream of it.
>
> Your right upper trap isn't the problem. It's the solution your body came up with. Your joints on that side can't hold passively, so the trap holds them. That's why it's tight, that's why it's inflamed, that's why leaning forward makes it ride up — it has to work harder to keep you stacked. And that's exactly why the Jetta seat helps. The seat holds you, so the trap doesn't have to. Take the load off the compensator and the pain drops. Makes total sense.
>
> Here's the thing most people get wrong with you: they'd stretch the trap. Don't. You stretch your only available stabilizer and you make it worse. We're going the other direction.
>
> What we do:
>
> **Stability first.** Closed-chain scapular control. Gentle eccentrics. No end-range work, no aggressive trap stretching, no big mobility pushes. You don't need more range — you need control inside the range you already have. This is where most of the work is.
> PMID: 35609204 | https://pubmed.ncbi.nlm.nih.gov/35609204/
> WOSI +325 points at 24 weeks (p = 0.001).
>
> **Combined modality from day one.** Exercise, hands-on, and education together — not exercise alone, not mobility-first. Your posterior chain inflammation cycles are regional sensitization, and single-modality programs flat underperform on that pattern.
> PMID: 39818121 | https://pubmed.ncbi.nlm.nih.gov/39818121/
> SMD −1.67 combined modality.
>
> **Gentle nerve glides.** Not nerve tension. Not end-range stress on the nerve. Glide pattern only.
> PMID: 40576779 | https://pubmed.ncbi.nlm.nih.gov/40576779/
> Pain MD −3.23 / disability SMD −1.57.
>
> **Breathing-coordinated thoracic mobility, light.** Your C-T junction took the acute hit under intense breathing — we don't go anywhere near that pattern. Gentle, paired with breath, no provocation.
> PMID: 24835338 | https://pubmed.ncbi.nlm.nih.gov/24835338/
> r = −0.58 thoracic mobility ↔ neck pain.
>
> **TMJ:** I'm not grounding that piece from what I have right now. Go get a formal TMJ clinical assessment — separate workup, separate clinician.
>
> Reassess at 12 weeks. If the right trap dominance and tightness haven't dropped despite the stability work, we escalate to a connective-tissue workup.

---

## System Self-Check

| Check | Result |
|---|---|
| Raw first-person input parsed to mechanism signatures | PASS — 7 signals → 7 mechanism layers |
| Forward query through index resolves all relevant records | PASS — 6 active records surfaced; 1 planned flagged ungrounded |
| Horizontal modifier (research-008) applied first | PASS — Stability-first frame governs all downstream interventions |
| RC-7 sequencing rule honored | PASS — Combined-modality from day one |
| HL-09 (no fabricated grounding) | PASS — TMJ disclosed as ungrounded; referred out |
| Citation format per CLAUDE.md §7 (PMID + exact figure) | PASS — Inline per claim |
| Engine/layer names fire silently per CLAUDE.md §5 | PASS — No system terminology in patient-facing output |
| Action override per CLAUDE.md Hard Override (one plan, no options) | PASS — Single intervention path |
| Reassessment + escalation criteria present | PASS — 12-week reassess; connective-tissue workup escalation |
| Voice realism (practitioner addressing patient directly) | PASS — Conversational, owns the call, second-person |
| Confidence-aware framing (no overclaiming on Medium-confidence records) | PASS — research-002 mechanism cited silently as background, not surface claim |

---

## Acceptance Criterion Implications

### Acceptance Criterion #4 (forward / reverse query demonstrably resolvable)

Already satisfied 2026-05-01. This exercise re-validates the forward-query mechanism on a richer, multi-mechanism input — strengthening confidence that the index supports the query pattern beyond the simple single-record cases shown in the precursor log.

### Acceptance Criterion #8 (≥1 clinical decision surfaces a citation that materially shapes the recommendation)

**Pipeline-validated.** This exercise demonstrates the system can produce such an output. The exact production-grade test is whether the same pipeline, run on a real Stream A input by Zach, surfaces a citation that materially shapes his recommendation on a real patient.

**Not yet fully satisfied** — this is a closed-loop simulation. Stream A Phase 2 dual-stream still required for full satisfaction. This exercise advances the criterion by removing pipeline-readiness as a possible gating concern.

---

## Refinement Signals

### Signal 1 — Pipeline operates correctly on multi-mechanism inputs

No drift, no orphaned records surfaced, no fabricated grounding emitted. Hard locks fired correctly when the TMJ layer surfaced ungrounded. Horizontal modifier (research-008) correctly took precedence over vertical mechanism sequencing.

### Signal 2 — Voice translation operates correctly

Output reads as practitioner-to-patient prose, not as a system report. Engine names ("Bootstrap v1", "Index", "RC-7", "HL-09") never appear in the patient-facing output. The plan structure (stability first, combined modality, gentle nerve glides, light breathing-coordinated thoracic) emerges from the system but reads as clinical reasoning.

### Signal 3 — Citation surfacing decision was the marginal call

CLAUDE.md §7 says citations surface only when "significantly informative" or explicitly requested. This exercise surfaced 4 inline citations because the grounding materially shaped each recommendation away from the default ("don't stretch the trap" requires explicit mechanistic justification; "combined modality from day one" overrides expected mobility-first sequencing; etc.). This is consistent with §7 but reflects a judgment call worth noting — Phase 2 dual-stream may produce real cases where the grounding is less marginal and citation surfacing should be lighter or heavier.

**No refinement entry needed at this point.** Logged as observation.

### Signal 4 — research-002 cited silently as background mechanism, not surface claim

research-002's localized neuroinflammation mechanism informs the framing but does not surface as a citation in the output. This is appropriate because research-002 is Medium-High confidence (1 of 2 promotion conditions met; full High pending Phase 2 clinical replication) and a single PET/CT N=1 case report — not a population-grounded recommendation for clinical action. The pipeline correctly held it as background mechanism rather than surface claim. Confidence-aware citation surfacing is operating as designed.

---

## Test Disposition

**M2 retrieval pipeline: VALIDATED end-to-end on multi-mechanism real first-person input.**

The pipeline successfully parsed unstructured natural language, mapped 7 mechanism signatures to records via the populated index, applied horizontal modifier precedence and sequencing rules, honored hard locks, surfaced citations consistent with CLAUDE.md §7 discipline, and produced a grounded clinical plan in practitioner voice without leaking engine/layer names.

**Logged as test artifact.** Acceptance criterion #8 still pending Stream A Phase 2 dual-stream for full satisfaction.

---

## Last Updated

2026-05-02 — initial test artifact authored. Pipeline validated end-to-end on founder's raw first-person multi-mechanism case input filtered through Zach's practitioner voice.
