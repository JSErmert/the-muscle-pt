---
exercise_id: live-case-contrast-test-002
date: 2026-05-02
type: validation log (negative control / contrast test)
purpose: confirm M2 retrieval pipeline is signature-driven, not record-availability-driven — that records correctly stay silent when their mechanism signatures are absent and that sequencing logic switches based on substrate detection
acceptance_criteria_advanced:
  - "Pipeline negative-control: records that should NOT fire (research-008, research-004, research-003, research-006) stay silent on a non-hypermobile, non-CS, non-post-dislocation, non-TMJ presentation"
  - "Acceptance Criterion #4 — forward query through index, re-validated on a contrasting mechanism profile"
  - "Acceptance Criterion #8 — pipeline-readiness re-validated for a different case complexity (lower mechanism count, simpler intervention path)"
relevant_doctrine:
  - systems/intelligence/research-index-and-traceability-v1.md
  - systems/intelligence/research-query-layer-v1.md
  - systems/intelligence/research-to-system-mapping-v1.md
  - execution/content-output-contract-v1.md (citation format §7)
  - architecture/m2-operationalize-milestone-plan-v1.md
linked_records_fired:
  - research-001 (Wirth 2014, PMID 24835338) — PRIMARY (thoracic mobility ↔ neck/upper back pain)
  - research-005 (García-Juez 2025, PMID 40576779) — SUPPORTING (mild radicular component)
  - research-002 (Lutke Schipholt 2026, PMID 41620319) — BACKGROUND mechanism only
linked_records_held_silent:
  - research-008 (Spanhove 2023, PMID 35609204) — no laxity substrate
  - research-004 (Carbone 2015, PMID 24458335) — no dislocation history
  - research-003 (Ibrahim 2025, PMID 39818121) — no CS signature
  - research-006 (TMJ — planned) — no TMJ involvement
linked_artifacts:
  - records/research/validation/2026-05-01-index-query-resolution-exercise.md (precursor — single-record forward/reverse/output validation)
  - records/research/validation/2026-05-02-live-case-retrieval-test.md (paired v2 test — multi-mechanism positive case)
  - records/logs/reviews/monthly/m2-operationalization-closeout.md
  - records/logs/decisions/decision-015-m3-scope-decision.md
---

# M2 Live Case Contrast Test — 2026-05-02

This validation exercise is the **negative control** paired with the 2026-05-02 live case retrieval test. The v2 test exercised 7 mechanism signatures simultaneously and validated that the pipeline correctly fires the relevant records and applies the horizontal modifier (research-008) ahead of vertical mechanism layers.

This contrast test runs a **different mechanism profile** — a clearly non-hypermobile, non-CS, non-post-dislocation, non-TMJ desk-worker presentation with primarily thoracic-mechanical and mild radicular components — to confirm that records which should NOT fire correctly stay silent.

**The point of this test:** the pipeline must be signature-driven, not record-availability-driven. A library with 6 active records and 1 horizontal modifier must not fire all 7 on every input. The v2 test alone could not prove this (it presented a case where most records *should* fire). This contrast test does.

---

## Test Design

**Input modality:** Same as v2 — raw first-person conversational description, the way a patient would describe their case to a clinician.

**Voice target:** Same as v2 — Zach (practitioner addressing the patient directly).

**Expected contrast:** Different records fire. Different sequencing applies. Different citation set surfaces. Different escalation criteria. Voice register stays consistent.

**Test rationale:** Validates that the library is *applied selectively*, not *applied wholesale*. This is the critical discipline for Stream A — Zach's caseload will not all look like the founder case, and the system must produce the right plan for the right case, not project the founder case onto every patient.

---

## Input — Raw First-Person Case (synthetic representative — desk worker, non-hypermobile)

> "I'm 38, desk job, lift maybe three days a week — overhead press, deadlifts, nothing crazy. Past six months my upper back has been getting stiff and there's a dull ache between my shoulder blades that won't go away. Last couple months I'm getting some tingling and light numbness down my right arm when I press overhead — not every rep but enough that I'm starting to back off. It's worst after a long day at the desk or right when I start a session. Once I'm warmed up it eases. I've never dislocated anything, no joint problems, my joints feel pretty stiff actually, not loose. Sleep's fine, no other pain anywhere else. What am I dealing with?"

---

## Pipeline Trace (system-side, fires silently in production)

### Step 1 — Mechanism Signature Parsing

| Signal in input | Layer detected |
|---|---|
| "upper back stiff, dull ache between shoulder blades, 6mo gradual onset" | Thoracic hypomobility / mechanical |
| "worst after prolonged sitting, eases with warmup" | Sustained-flexion-load → mechanical pattern |
| "tingling/numbness down right arm with overhead pressing" | Cervical radicular / neural component, mild |
| "joints feel stiff, never dislocated, no laxity" | **NEGATIVE for hypermobility substrate** |
| "no widespread pain, no other body regions, sleep fine" | **NEGATIVE for central sensitization** |
| "no injury history, no acute event" | **NEGATIVE for post-dislocation pattern** |

**Critical observation:** half the parsed signals are *negative findings* — explicit absences that rule out specific records. This is a mature pipeline behavior. A naive retrieval would only react to positive signals; a disciplined retrieval also reads absences.

### Step 2 — Forward Query Resolution Through Index

| Record | Fires? | Reason |
|---|---|---|
| research-001 (Wirth 2014, PMID 24835338) | **YES — PRIMARY** | Thoracic mobility ↔ neck/upper back; sustained-flexion provocation present |
| research-005 (García-Juez 2025, PMID 40576779) | **YES — supporting** | Mild radicular component → conservative neural mobilization |
| research-002 (Lutke Schipholt 2026, PMID 41620319) | Background only | Mechanism context, not surface citation |
| research-003 (Ibrahim 2025, PMID 39818121) | **NO** | No CS signature — pain is localized, mechanical, exercise-tolerant. RC-7 (CS-screening sequencing) does NOT trigger |
| research-008 (Spanhove 2023, PMID 35609204) | **NO** | No laxity — patient explicitly stiff. Horizontal modifier does NOT apply |
| research-004 (Carbone 2015, PMID 24458335) | **NO** | No dislocation history |
| research-006 (TMJ — planned) | **NO** | No TMJ involvement |

### Step 3 — Sequencing Rules and Hard Locks Applied

- **Without research-008 horizontal modifier:** default vertical sequencing applies → mobility-first (Wirth pattern) is allowed, NOT overridden
- **Without RC-7 firing:** combined-modality from day one is NOT mandated — staged mobility-first → neural glides → strength reintegration is the appropriate sequencing
- **HL-09 (no fabricated grounding):** all surfaced claims grounded; no ungrounded layer to disclose; no referral required
- **Citation surfacing rule (CLAUDE.md §7):** research-001 grounding materially shapes the call (mobility-first when most clinicians would attack the symptomatic neck); research-005 grounding shapes the neural piece. Both surface inline.
- **Action override (CLAUDE.md Hard Override):** one plan, no options
- **Output translation (CLAUDE.md §7):** engine names fire silently; no system terminology in patient-facing output
- **Reassessment markers:** 6-week reassess (shorter horizon than v2's 12 weeks because the case is simpler — straightforward mechanical with mild neural, no constitutional substrate or CS overlay)

---

## Output — Practitioner Voice (Zach addressing patient)

> Yeah, I know what this is. Pretty common pattern.
>
> Your upper back is stiff. Sitting all day locks the thoracic spine into flexion, and your neck and shoulders end up doing thoracic-spine work they're not built for. The arm tingling under overhead pressing is the downstream tax — when the upper back can't extend, the cervical spine compensates, the nerve gets a little crowded, and you feel it down the arm. It's a chain problem, not a neck problem.
>
> Good news — you don't have anything structurally wrong. Joints stiff, not loose. No injury. No widespread stuff. This is mechanical and it responds well.
>
> Plan, in this order:
>
> **Thoracic mobility first.** Open up extension. Quadruped extension-rotation, foam roller extensions, wall slides. Daily, short. This is the unlock — get the thoracic spine doing its job and the neck stops compensating.
> PMID: 24835338 | https://pubmed.ncbi.nlm.nih.gov/24835338/
> r = −0.58 thoracic mobility ↔ neck pain.
>
> **Then nerve glides for the right arm.** Gentle median-nerve sliders, not tensioners. Get the nerve moving cleanly through the brachial plexus and out — no end-range stretch.
> PMID: 40576779 | https://pubmed.ncbi.nlm.nih.gov/40576779/
> Pain MD −3.23 / disability SMD −1.57.
>
> **Then back to lifting, modified.** Pull overhead pressing for the next 4 weeks. Replace it with landmine press or incline DB press — same pattern, less cervical compression. Keep deadlifts in if they're symptom-free. After 4 weeks, retest overhead with light loads and progress only if the tingling stays away.
>
> Reassess at 6 weeks. If the upper back stiffness hasn't dropped and the arm symptoms are still showing up, we add hands-on work and look harder at the cervical spine.

---

## Contrast Self-Check (v2 founder case vs. v3 desk-worker case)

| Element | v2 (founder, multi-mechanism) | v3 (desk worker, mechanical+neural) | Pipeline correct? |
|---|---|---|---|
| research-008 fires | YES (lax substrate present) | NO (stiff, never dislocated) | ✓ Horizontal modifier applies only when substrate present |
| research-004 fires | YES (2 dislocations) | NO (no dislocation) | ✓ Vertical record fires only when signature present |
| research-003 fires | YES (regional inflammation cycles) | NO (localized, exercise-tolerant) | ✓ CS sequencing rule fires only on CS pattern |
| research-006 (TMJ) flagged | YES (snap event, clicks) | NO (no TMJ) | ✓ HL-09 disclosure only when ungrounded layer is relevant |
| Sequencing | Stability-first, never stretch compensator, combined-modality day one | Mobility-first, staged progression, return-to-lifting modification | ✓ Different mechanism → different sequencing |
| Ungrounded layer disclosed | YES (TMJ referred out) | NO (none required) | ✓ HL-09 fires only when needed |
| Citations surfaced | 4 (research-008, 003, 005, 001) | 2 (research-001, 005) | ✓ Confidence-aware surfacing varies with case |
| Reassessment horizon | 12 weeks (constitutional + CS overlay) | 6 weeks (clean mechanical) | ✓ Reassessment scaled to case complexity |
| Escalation pathway | Connective-tissue workup | Hands-on + deeper cervical workup | ✓ Escalation matches mechanism profile |
| Voice register | Zach practitioner voice | Zach practitioner voice | ✓ Voice consistent across cases |

---

## System Self-Check

| Check | Result |
|---|---|
| Negative findings (absences) parsed correctly | PASS — 3 explicit absences ruled out 4 records |
| Records that should NOT fire stayed silent | PASS — research-008, 004, 003, 006 all silent |
| Records that SHOULD fire surfaced | PASS — research-001 primary, research-005 supporting |
| research-002 held as background mechanism only | PASS — not surfaced as surface citation |
| Sequencing logic switched based on substrate detection | PASS — mobility-first allowed (no horizontal modifier override; no RC-7 trigger) |
| HL-09 fired only when needed | PASS — no ungrounded disclosure on a fully-grounded case |
| Citation surfacing matched material decision impact | PASS — 2 citations on a simpler case vs. 4 on a complex one |
| No false positives | PASS — pipeline did not over-apply the most recently authored record (research-008) |
| No false negatives | PASS — applicable records surfaced |
| Voice translation consistent across cases | PASS — same Zach register, different content |
| Action override (one plan, no options) | PASS — single staged plan |
| Engine/layer names silent in output | PASS — no system terminology in patient-facing output |
| Reassessment + escalation criteria scaled to case | PASS — 6-week vs. 12-week horizon appropriate to complexity |

---

## Refinement Signals

### Signal 1 — Negative-finding parsing operates correctly

The pipeline correctly read explicit absences ("never dislocated", "joints feel stiff not loose", "no widespread pain") as ruling-out signals, not just as missing-information signals. This is a mature pipeline behavior — a less disciplined retrieval would default to firing all available records on any input that mentions related anatomy.

### Signal 2 — Sequencing logic is correctly conditional, not hardcoded

In v2, stability-first sequencing was governed by research-008's horizontal modifier. In v3, with no horizontal modifier active, mobility-first sequencing emerged from research-001's default sequencing bias. The pipeline did not apply v2's stability-first rule by default to v3 — sequencing was case-conditional.

### Signal 3 — Reassessment and escalation horizons scale with case complexity

12 weeks for a multi-mechanism case with constitutional substrate and CS overlay; 6 weeks for a clean mechanical-with-mild-neural case. The pipeline produces appropriate horizons rather than a fixed reassessment schedule — consistent with how a practitioner would actually scale follow-up.

### Signal 4 — Confidence-aware citation surfacing varies appropriately

v2 surfaced 4 citations because 4 records each materially shaped a distinct intervention call. v3 surfaced 2 citations because only 2 records materially shaped the plan. Citation density correlated with mechanism complexity, not with intent to demonstrate the library.

### Signal 5 — Voice register is independent of mechanism profile

Same Zach voice across both cases despite very different content, sequencing, and citation density. This validates the voice translation step is a final-stage transformation, not a content-determined behavior.

**No refinement entries triggered by this exercise.** All signals are confirmations of existing pipeline behavior, not surfaced gaps.

---

## Acceptance Criterion Implications

### Acceptance Criterion #4 (forward query demonstrably resolvable through index)

Re-validated on a contrasting mechanism profile. Forward query mechanism works for *both* multi-mechanism cases (v2) and simpler mechanical-plus-neural cases (v3) — and produces appropriately different record sets.

### Acceptance Criterion #8 (≥1 clinical decision surfaces a citation that materially shapes the recommendation)

Pipeline-readiness re-validated. The system produces materially-shaping citations on cases of varying complexity. Stream A Phase 2 dual-stream still required for full satisfaction (Zach making a real call on a real patient), but pipeline behavior is now validated across two distinct mechanism profiles.

### Negative-Control Discipline (informally tracked)

This exercise establishes the negative-control discipline as part of the validation regime: any future research record added to the library should pass *both* a positive-case test (the case it was authored for) AND a negative-case test (a case where it should NOT fire). This protects against record-availability-driven retrieval — the failure mode where library expansion silently degrades retrieval precision.

**Logged as observation.** Could become a formal Bootstrap v1 amendment if a future record fails its negative-control test. Not a refinement at this point.

---

## Test Disposition

**M2 retrieval pipeline: VALIDATED on negative control.**

The pipeline correctly distinguishes between cases that warrant horizontal modifier application and cases that do not. It correctly suppresses records with absent signatures while surfacing records with present signatures. It correctly scales sequencing, citation density, and reassessment horizons to case complexity.

Combined with the v2 multi-mechanism test, the pipeline is now validated across:
- High-complexity multi-mechanism input with horizontal modifier (v2)
- Lower-complexity mechanical-plus-neural input without horizontal modifier (v3)

This establishes the pipeline operates correctly across mechanism-count diversity, substrate presence/absence, and CS pattern presence/absence.

**Logged as test artifact.** Acceptance criterion #8 still pending Stream A Phase 2 dual-stream for full satisfaction.

---

## Last Updated

2026-05-02 — initial contrast-test artifact authored. Pipeline validated as signature-driven (not record-availability-driven) on a deliberately non-hypermobile, non-CS, non-post-dislocation, non-TMJ desk-worker presentation.
