---
exercise_id: live-case-borderline-test-003
date: 2026-05-02
type: validation log (borderline / ambiguous case test — screen-and-branch discipline)
purpose: confirm M2 retrieval pipeline correctly handles sub-threshold signals — that records with partial/ambiguous signature support are screened rather than committed to, and that branching plans handle each screen outcome without re-authoring
acceptance_criteria_advanced:
  - "Pipeline screen-and-branch discipline: records with sub-threshold signature support (research-008, research-003) are surfaced as screening-pivot context rather than as applied-intervention citations"
  - "HL-09 (no fabricated grounding) extended to ungrounded substrate — refusing to apply hypermobility-aware programming without confirmed Beighton screen"
  - "Acceptance Criterion #4 — forward query through index, re-validated on a deliberately ambiguous mechanism profile"
  - "Acceptance Criterion #8 — pipeline-readiness re-validated for borderline cases (the realistic majority of Stream A inputs)"
relevant_doctrine:
  - systems/intelligence/research-index-and-traceability-v1.md
  - systems/intelligence/research-query-layer-v1.md
  - systems/intelligence/research-to-system-mapping-v1.md
  - execution/content-output-contract-v1.md (citation format §7)
  - architecture/m2-operationalize-milestone-plan-v1.md
linked_records_fired:
  - research-001 (Wirth 2014, PMID 24835338) — PRIMARY (mechanical thoracic-cervical, default sequencing)
linked_records_surfaced_as_screening_context:
  - research-008 (Spanhove 2023, PMID 35609204) — screening-pivot context only; would convert to applied if Beighton screen positive
  - research-003 (Ibrahim 2025, PMID 39818121) — screening-pivot context only; would convert to applied if multi-region stiffness/sleep pattern intensifies
linked_records_held_silent:
  - research-005 (García-Juez 2025, PMID 40576779) — no clear radicular component; held in reserve
  - research-004 (Carbone 2015, PMID 24458335) — distant subluxation history with full recovery, not active mechanism
  - research-002 (Lutke Schipholt 2026, PMID 41620319) — background mechanism only
  - research-006 (TMJ — planned) — no TMJ involvement
linked_artifacts:
  - records/research/validation/2026-05-01-index-query-resolution-exercise.md (precursor — single-record forward/reverse/output validation)
  - records/research/validation/2026-05-02-live-case-retrieval-test.md (v2 paired test — multi-mechanism positive case with horizontal modifier applied)
  - records/research/validation/2026-05-02-live-case-contrast-test.md (v3 paired test — negative control, non-hypermobile non-CS desk worker)
  - records/logs/reviews/monthly/m2-operationalization-closeout.md
  - records/logs/decisions/decision-015-m3-scope-decision.md
---

# M2 Live Case Borderline Test — 2026-05-02

This validation exercise is the **borderline / ambiguous case test** — the third in the 2026-05-02 validation triad alongside v2 (multi-mechanism positive case) and v3 (negative control). It tests the hardest retrieval discipline: handling sub-threshold signals where the pipeline must make a judgment call rather than a clean fire/no-fire decision.

The v2 test validated that the pipeline fires the right records on a clear positive case. The v3 test validated that the pipeline holds the right records silent on a clear negative case. **This v4 test validates that the pipeline screens-and-branches when neither positive nor negative is conclusive** — the realistic majority of Stream A inputs.

---

## Why This Test Matters

Real patients rarely arrive with clean v2 or v3 profiles. They arrive with:
- Family history of hypermobility but unclear personal status
- Distant injury history that may or may not be relevant
- Multi-region symptoms that could be mechanical, central, or coincidental
- Sleep disruption that could be positional or pain-amplifying
- Sub-threshold patterns that don't fully meet doctrine triggers

The hard discipline at the borderline is **not over-firing on sub-threshold signals**. A naive retrieval would either:

- **Over-fire:** Apply research-008's horizontal modifier (stability-first, no aggressive trap stretching) on a possibly-non-hypermobile patient because there is *some* hypermobility signal in the input. Result: hypermobility-aware programming applied to a non-hypermobile patient. Wrong direction of intervention.
- **Under-fire:** Ignore the family history + past subluxation entirely and treat as standard mechanical. Result: missed substrate that, if present, would warrant a different framework.

Both are wrong. The correct behavior is **screen first, commit second** — and the pipeline must produce a plan that handles each possible screen outcome without re-authoring from scratch.

This test validates that behavior.

---

## Test Design

**Input modality:** Same as v2/v3 — raw first-person conversational description.

**Voice target:** Same as v2/v3 — Zach (practitioner addressing patient directly).

**Expected behavior:**
- Sub-threshold signals identified, not collapsed into firm fires
- research-008 surfaced as **screening citation**, not applied citation
- research-003 surfaced as **monitoring citation**, not applied citation
- HL-09 extended to refuse premature application of substrate-grounded programming
- Default mechanical sequencing applied during screening window
- Branching plan presented — one immediate path, multiple conditional outcomes

---

## Input — Raw First-Person Case (synthetic representative — borderline / ambiguous)

> "I'm 32, female, run three or four times a week, lift twice. About four months ago my right neck and shoulder started bothering me — kind of a deep ache, not constant but it shows up most days. Some mornings I'm pretty stiff overall — neck, hips, hands a bit — and it takes 20 minutes of moving to feel normal. Pain has good days and bad days and I can't always tell why. Some nights it wakes me up if I roll onto that side. No injury that triggered this — just gradually showed up. One thing — back in college I subluxed my right shoulder during a fall, popped back in on its own, did some PT, never had problems with it again until maybe now. My mom has really bendy fingers, can put her thumb to her forearm, that kind of thing. I don't think I'm bendy like her but I've never been tested. Should I be worried?"

---

## Pipeline Trace (system-side, fires silently in production)

### Step 1 — Mechanism Signature Parsing with Confidence Flags

| Signal in input | Layer detected | Strength |
|---|---|---|
| "right neck/shoulder deep ache, 4mo gradual" | Mechanical / cervico-scapular | Clear |
| "morning stiffness multi-region (neck, hips, hands), resolves with movement" | **Sub-threshold CS or inflammatory pattern** | Ambiguous |
| "good day / bad day pattern, doesn't always correlate with activity" | **Sub-threshold CS** | Ambiguous |
| "wakes from pain when rolling onto that side" | Mechanical-positional OR sleep-mediated CS amplification | Ambiguous |
| "right shoulder subluxation 10y ago, full recovery, asymptomatic until now" | **Distant post-dislocation history — possibly relevant, not active** | Ambiguous |
| "mother hypermobile (thumb-to-forearm)" | **Family history hypermobility — sub-threshold for substrate** | Ambiguous |
| "self-report not hypermobile, never tested" | **Hypermobility screen needed, not done** | Unknown |

**Critical observation:** 4 of 7 signals are ambiguous. This is the core retrieval challenge — the pipeline must produce a plan that handles the ambiguity rather than collapsing it.

### Step 2 — Forward Query Resolution: Fire / Hold / Screen

| Record | Status | Reasoning |
|---|---|---|
| research-001 (Wirth, PMID 24835338) | **FIRE — primary** | Mechanical right neck/shoulder pattern, 4mo chronic, plausible thoracic-cervical link |
| research-005 (García-Juez, PMID 40576779) | **HOLD** | No clear radicular component yet; revisit if neural signs surface |
| research-003 (Ibrahim, PMID 39818121) | **SCREEN — do not fire RC-7 yet** | CS signals are sub-threshold (multi-region morning stiffness, good/bad day pattern, sleep disruption). Not enough to mandate combined-modality from day one, but enough to monitor and reassess |
| research-008 (Spanhove, PMID 35609204) | **SCREEN — do not fire horizontal modifier yet** | One past subluxation + family history hypermobility ≠ confirmed substrate. Patient self-reports not hypermobile but has never been formally screened. Beighton needed before applying hypermobility-aware programming |
| research-004 (Carbone, PMID 24458335) | **HOLD** | Distant subluxation history with full recovery; not the active mechanism |
| research-002 (Lutke Schipholt, PMID 41620319) | Background only | Not surface-relevant |
| research-006 (TMJ — planned) | **NO** | No TMJ involvement |

**New retrieval state introduced in this test: SCREEN.** Distinct from FIRE, HOLD, and NO. The SCREEN state is for records whose sub-threshold signature support warrants a formal screen before they can be either applied or dismissed. Records in SCREEN state surface as **screening-pivot context** in the patient-facing output, not as applied intervention citations.

### Step 3 — Sequencing Rules and Hard Locks Applied

- **Default vertical sequencing applies** (research-001 mobility-first) because no horizontal modifier is confirmed and no RC-7 trigger has fired
- **Premature application of research-008's horizontal modifier is blocked by HL-09** — research-008's evidence base is for *confirmed* hEDS/HSD patients, not for screening-positive presentations. Applying hypermobility-aware programming on incomplete grounding violates the no-fabricated-grounding hard lock
- **Premature application of RC-7 is blocked by the same logic** — combined-modality from day one is grounded for confirmed CS pattern, not for sub-threshold multi-region stiffness
- **Conservative interim plan emerges** — what's mechanically grounded NOW, while screening pending
- **Branching plan structure** — one immediate path with three conditional outcomes from screen results
- **Citation surfacing rule (CLAUDE.md §7)** — research-001 surfaces as applied citation; research-008 and research-003 surface as **branch-context citations** (the conditional pivot evidence), a novel surfacing pattern beyond v2/v3
- **Reassessment horizon scaled to screening window** — 4 weeks (faster than v3's 6 weeks because the screen output drives plan locking)
- **Honest disclosure of uncertainty** — patient explicitly told the plan is conditional on screening, not committed

---

## Output — Practitioner Voice (Zach addressing patient)

> Honest answer: probably not worried, but we need to screen a couple things before I lock the plan.
>
> Here's what's going on. Four months of right neck/shoulder ache, gradual onset, no injury. That's almost always a mechanical pattern — the upper back gets stiff, the shoulder blade stops moving cleanly, the neck and trap pick up the slack, and you get a deep ache on one side. Treatable, responsive, nothing structural.
>
> Two things I want to check before I commit to a plan, though. Both because the answer changes the plan.
>
> **First — hypermobility screen.** You subluxed that shoulder once in college and your mom is clearly hypermobile. You self-report you're not, but you've never been tested. We need a Beighton score before I program this. If you screen positive, the plan changes — stability-first, no aggressive stretching of the right trap, different progression. If you screen negative, we go standard. Five minutes to do, I'll walk you through it next session.
>
> **Second — the morning stiffness in your hips and hands.** That, plus the good day / bad day pattern, plus pain waking you up — those can be normal mechanical noise, or they can be early signs of something more central. I want to track this for four weeks. If the multi-region stiffness gets more consistent or the sleep disruption increases, we change the plan.
>
> **In the meantime — start here, conservative:**
>
> **Thoracic mobility.** Quadruped extension-rotation, foam roller, wall slides. Daily, short.
> PMID: 24835338 | https://pubmed.ncbi.nlm.nih.gov/24835338/
> r = −0.58 thoracic mobility ↔ neck pain.
>
> **Scapular control work.** Light, controlled, no end-range stuff yet. We hold off on aggressive trap stretching until the hypermobility screen comes back.
>
> **Keep running and lifting** as long as it's not flaring the neck. If overhead pressing or any specific movement triggers it, pull it for now.
>
> Reassess at 4 weeks with the screen results in hand. Plan goes one of three directions:
>
> 1. Screen negative + multi-region stuff resolves → standard mobility-first progression, we're done.
> 2. Screen positive → pivot to hypermobility-aware programming. Different framework, I'll walk you through it.
>    PMID: 35609204 | https://pubmed.ncbi.nlm.nih.gov/35609204/
>    WOSI +325 points at 24 weeks (p = 0.001) — for context on the rehab framework if we go this direction.
> 3. Multi-region stiffness intensifies or sleep disruption worsens → we add hands-on work and combined-modality from there.
>    PMID: 39818121 | https://pubmed.ncbi.nlm.nih.gov/39818121/
>    SMD −1.67 combined modality — for context on why the plan would change.
>
> So: not worried right now. Two screens, four weeks, then we lock the plan.

---

## System Self-Check — Borderline-Specific Discipline

| Check | Result |
|---|---|
| Sub-threshold signals identified rather than over-fired | PASS — 4 ambiguous signals flagged, not collapsed into firm fires |
| HL-09 prevented premature application of research-008 horizontal modifier | PASS — screening invoked instead of intervention |
| RC-7 (CS combined-modality) held in reserve, not applied prophylactically | PASS — monitoring path applied instead |
| Default vertical sequencing applied while screening pending | PASS — research-001 mobility-first, conservative |
| Branching plan presented (3 outcomes from screen) | PASS — plan handles each screen result without re-authoring |
| Citation surfacing pattern adapted to ambiguity | PASS — research-008 surfaced as *screening-pivot context*, not as *applied intervention*; novel surfacing pattern |
| Reassessment horizon scaled to screening timeline | PASS — 4 weeks (vs. v3's 6 weeks and v2's 12 weeks) |
| Engine names silent in output | PASS |
| Action override (one plan, no options at the immediate-action level) | PASS — the immediate plan is one path; the branches fire only on screen results |
| Honest disclosure of uncertainty | PASS — "we need to screen before I lock the plan" stated openly |

---

## Cross-Test Discipline Comparison

| Element | v2 (founder, multi-mech) | v3 (desk worker, mechanical+neural) | v4 (borderline, ambiguous) |
|---|---|---|---|
| Pipeline mode | Confirm-and-apply | Confirm-and-apply (different records) | **Screen-and-branch** |
| research-008 application | Applied as horizontal modifier | Held silent (substrate absent) | **Screened, not applied yet** |
| RC-7 application | Applied (CS confirmed) | Held silent (CS absent) | **Held in reserve, monitored** |
| Citation surfacing | Inline per applied claim (4 citations) | Inline per applied claim (2 citations) | **Inline per applied claim (1) + branch-context citations (2)** |
| Reassessment horizon | 12 weeks | 6 weeks | **4 weeks** (screen-driven) |
| Plan structure | Single committed plan | Single committed plan | **One immediate plan + 3 branches conditional on screen results** |
| HL-09 disclosure pattern | TMJ referred out (ungrounded layer present) | None needed (all grounded) | **Screening as HL-09 discipline** (refusing to ground intervention without confirmed substrate) |
| Voice register | Zach practitioner voice | Zach practitioner voice | Zach practitioner voice — same register, more openly conditional language |

---

## Refinement Signals

### Signal 1 — Pipeline introduces a fourth retrieval state: SCREEN

Beyond FIRE / HOLD / NO, the borderline case surfaced a SCREEN state for records whose signature support is sub-threshold. SCREEN-state records produce **branch-context citations** rather than applied-intervention citations. This is a novel pipeline behavior that emerged from the test rather than from existing doctrine.

**Refinement candidate (logged but not authored):** Bootstrap v1 or Index & Traceability v1 may benefit from formalizing the SCREEN state and the branch-context citation surfacing pattern. **N=1 occurrence so far.** If a second borderline test or real Stream A case demonstrates the same pattern, escalate to formal refinement.

### Signal 2 — HL-09 extends naturally to ungrounded substrate

HL-09 originally framed as "no fabricated grounding" — meaning don't cite figures or claims unsupported by the source. This test extended HL-09 to a related but distinct discipline: **don't apply substrate-grounded programming without confirmed substrate.** Research-008's evidence applies to confirmed hEDS/HSD patients, and applying its programming on a screening-positive (not confirmed) patient would be a softer form of grounding fabrication.

**Refinement candidate (logged but not authored):** HL-09 may benefit from explicit extension to "no application of substrate-grounded programming without confirmed substrate." **N=1 occurrence so far.** Monitor for recurrence.

### Signal 3 — Branch-context citation pattern is a third citation-surfacing mode

v2 surfaced citations for applied claims. v3 surfaced citations sparingly because fewer claims needed grounding. v4 surfaced citations for **conditional pivot evidence** — citations attached not to "what we are doing" but to "what would change what we do." This is a third citation-surfacing pattern.

**No refinement entry needed at this point.** Logged as observation. The CLAUDE.md §7 citation rule ("when significantly informative or explicitly requested") accommodates this pattern naturally — branch-context citations are significantly informative because they tell the patient what would change the plan and why.

### Signal 4 — Reassessment horizons scale with case-locking-readiness, not just complexity

v2: 12 weeks (multi-mechanism, constitutional + CS, slow trajectory expected). v3: 6 weeks (clean mechanical, fast trajectory expected). v4: 4 weeks (screen-driven — horizon set by *when the plan can be locked*, not by symptom-trajectory expectation).

This is a novel reassessment-horizon principle that emerged from the test: when a plan is conditional on a screen, the reassessment is timed to the screen, not to the symptom trajectory. Logged as observation.

### Signal 5 — "Should I be worried?" is a different framing question than v2/v3 inputs

v2 ended with "What do I do?" (action request). v3 ended with "What am I dealing with?" (diagnosis request). v4 ended with "Should I be worried?" (anxiety-management request). The output appropriately matched the framing — leading with reassurance ("probably not worried") before structure. This validates that the voice translation step reads framing, not just content.

**No refinement entry needed.** Working as designed.

---

## Acceptance Criterion Implications

### Acceptance Criterion #4 (forward query demonstrably resolvable through index)

Re-validated on a deliberately ambiguous mechanism profile. Forward query mechanism works for *both* clear positive cases (v2), clear negative cases (v3), and ambiguous-mixed cases (v4).

### Acceptance Criterion #8 (≥1 clinical decision surfaces a citation that materially shapes the recommendation)

Pipeline-readiness re-validated for the realistic majority of Stream A inputs. Real patients rarely arrive as clean v2 or v3 profiles — most arrive as v4-style borderlines. The pipeline producing screen-and-branch plans on borderlines is more important for criterion #8 satisfaction than producing clean v2-style plans on rare clear cases.

### Negative-Control + Borderline Discipline as Validation Regime

Combined with the v3 negative-control test, this v4 test establishes a **three-mode validation regime** for any future research record added to the library:

1. **Positive case** — record fires, programming applies (the case it was authored for)
2. **Negative case** — record stays silent, programming does not apply (a case where it should NOT fire)
3. **Borderline case** — record surfaces in SCREEN state, programming is conditional on confirmation (a case where the record is plausible but not confirmed)

A record passing all three is more robust than a record passing only the positive case. **Logged as observation — not yet a doctrine refinement.** Could become a formal Bootstrap v1 amendment if the regime proves valuable across a sustained validation window.

---

## Test Disposition

**M2 retrieval pipeline: VALIDATED on borderline-ambiguity discipline.**

The hard discipline tested here is *not over-firing on sub-threshold signals*. The pipeline correctly:
- Identified 4 ambiguous signals and held them as ambiguous rather than collapsing them
- Refused to apply research-008's horizontal modifier without confirmed substrate (HL-09 extended)
- Refused to apply RC-7's combined-modality mandate without confirmed CS pattern
- Surfaced research-008 and research-003 as branch-context citations rather than applied citations
- Produced a one-immediate-plan + three-branch-outcomes structure that handles each screen result without re-authoring
- Disclosed uncertainty honestly to the patient ("we need to screen before I lock the plan")
- Scaled reassessment horizon (4 weeks) to screen-locking timeline rather than symptom trajectory

Combined with v2 (multi-mechanism positive case) and v3 (negative control), the pipeline is now validated across:
- Multi-mechanism inputs with horizontal modifier active (v2)
- Single-mechanism inputs without horizontal modifier (v3)
- Sub-threshold mixed inputs requiring screen-and-branch (v4)

This three-mode validation regime is the production-realistic distribution Stream A will produce. Stream A v4-style cases are the majority; the pipeline is now validated for that majority.

**Logged as test artifact.** Acceptance criterion #8 still pending Stream A Phase 2 dual-stream for full satisfaction (Zach making a real call on a real patient).

---

## Last Updated

2026-05-02 — initial borderline-test artifact authored. Pipeline validated as screen-and-branch capable on a deliberately ambiguous 32yo runner/lifter case with sub-threshold hypermobility and CS signals. Three-mode validation triad (v2 multi-mechanism / v3 negative control / v4 borderline) now complete.
