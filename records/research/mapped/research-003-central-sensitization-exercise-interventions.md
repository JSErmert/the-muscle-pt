---
record_id: research-003
slug: central-sensitization-exercise-interventions
status: active
date_mapped: 2026-05-01
study_pmid: 39818121
captured_record: records/research/captured/research-003-central-sensitization-exercise-interventions.md
linked_query: query-003
---

# RESEARCH RECORD 003 — System Mapping (L3)

This file holds Layer 3 — how Ibrahim et al. 2025 maps onto The Muscle PT system. Source capture and insight (L1, L2) are held in `records/research/captured/research-003-central-sensitization-exercise-interventions.md`.

---

## Case Engine Mapping

### Classification Implications

A chronic musculoskeletal pain case showing **any of the following central sensitization features** should be classified as the **inflammation-cycle / sensitization-driven case category** (distinct from mechanical-dominant cases per research-001 and from localized single-root neuroinflammation cases per research-002):

- Regional symptom spreading beyond the original injury site (multi-region simultaneous involvement)
- Burning quality during flares (qualitatively distinct from mechanical ache)
- Flare/quiescent cycling pattern with return-to-baseline between flares
- Elevated Central Sensitization Inventory (CSI) score
- Quantitative sensory testing abnormalities (lowered pain thresholds, impaired conditioned pain modulation)
- Disproportion between mechanical findings and symptom severity / spread

### Reassessment Infrastructure — Ibrahim Variables Adapted

Ibrahim measures CS indices via:
- **Central Sensitization Inventory (CSI)** — validated questionnaire, scores 0–100; threshold ≥40 commonly used to flag clinically significant CS
- **Quantitative sensory testing (QST)** — pressure pain thresholds, temporal summation, conditioned pain modulation

Field-usable proxies (when CSI/QST not available):
- **Symptom-quality logging** — burning vs. mechanical ache, ratio over time
- **Region-of-involvement tracking** — number of distinct anatomical regions painful during flares
- **Flare frequency over time** — flares per month, trending up or down
- **Provocation/relief response** — does the case respond to combined-modality interventions (positive signal) or only to passive treatments (warning signal)

CSI in field practice is not a heavy lift — it is a 25-item self-report questionnaire and is the recommended primary CS reassessment marker when feasible. Symptom-quality logging is the next-best when CSI is impractical.

### Cross-Record Sequencing Rules

This record refines the sequencing claims of research-001:

- **If case has no CS features:** research-001 sequencing applies cleanly (thoracic mobility first, chest expansion second, scapular repositioning third) — mobility/stretching-first is appropriate
- **If case has CS features:** research-003 combined-modality framing supersedes — mobility work becomes a *component* of a combined program, not a standalone first phase. Single-modality stretching is shown insufficient for CS reduction at population level
- **If case has both mechanical and CS features (mixed):** address both axes in parallel via a combined program that includes mobility, strengthening, and aerobic components — covers both research-001's sequencing and research-003's effect class

---

## Decision Mapping

### Decision Logic Influence

For chronic musculoskeletal pain cases without red flags:

1. **Screen for central sensitization features first** (CSI ≥40, regional spreading, burning quality, flare cycling). This screen determines which sequencing applies.
2. **CS-positive cases:** prescribe a **combined exercise program** — combined stretching + strengthening (Ibrahim SMD -1.67) or combined stretching + strengthening + aerobic (Ibrahim SMD -1.61). Single-modality approaches are insufficient.
3. **CS-negative cases:** research-001 mechanical sequencing applies; passive mobility / stretching-first staging is appropriate.
4. **All cases:** track CS indices alongside primary outcome measures (CSI re-administered at intervention milestones; symptom-quality logging continuous).
5. **All cases:** maintain escalation triggers active. Red flags (systemic inflammatory disease features, fever, weight loss, night pain unrelated to position, morning stiffness > 1 hour) → escalate, not in scope of conservative trial.

### What This Decision Logic Does NOT Authorize

- Treating every chronic MSK pain case as central-sensitization-driven without screening — over-classification leads to unnecessarily complex programming for mechanical-dominant cases
- Avoiding stretching entirely — stretching as a *component* of a combined program is supported. Only stretching-as-standalone is shown insufficient
- Specifying exact dosing (frequency, intensity, duration) — Ibrahim's network meta-analysis does not specify these at the aggregate level. Practical dosing draws from component RCTs and clinician judgment within evidenced ranges
- Surfacing this citation in default M1 outputs — citations remain off by default per CLAUDE.md Section 7. Surface only when significantly informative or explicitly requested.

---

## Rule Candidates

Drawn from research-003 + linked case + cross-record interactions. Each is a *candidate* — promotion to firing rule requires repeated validation.

- **RC-7.** Chronic MSK pain case + CS features (CSI ≥40, regional spreading, burning quality, flare cycling) → classify as inflammation-cycle / sensitization-driven case category; do not assume mechanical-dominant by default
- **RC-8.** Sensitization-driven case identified → prescribe a **combined-modality exercise program** (combined stretching + strengthening, or combined stretching + strengthening + aerobic). Single-modality approaches are insufficient at the evidence level
- **RC-9.** When research-001 mechanical pattern AND research-003 sensitization features both present → run a combined-modality program that incorporates mobility work as a component, not as a standalone first phase. Don't run mechanical sequencing in isolation when CS features are positive
- **RC-10.** All chronic MSK cases under conservative trial → track CS indices (CSI primary, symptom-quality logging secondary) alongside primary outcome measures. CS reduction is itself a process measure, not just a downstream effect

Promotion path: ≥ 2 validated firings without contradiction → formal rule per Bridge §10 Evolution Model.

---

## Constraint Candidates

- **CC-9.** Ibrahim measures CS *indices* (CSI questionnaire, QST measures) — not directly burning quality, regional spreading patterns, or flare frequency. CSI is a validated proxy but not a direct measurement of these features. Treat CSI scores as proxies, not literal disease markers.
- **CC-10.** Findings apply to chronic MSK pain. **Acute, post-surgical, post-traumatic acute, and systemic inflammatory disease populations are out of scope.** Red flags supersede.
- **CC-11.** Single-modality stretching being shown insufficient for CS reduction does NOT mean stretching is harmful — it means stretching as a *standalone intervention* is insufficient for CS-dominant cases. Stretching as a *component* of a combined program is supported.
- **CC-12.** Specific dosing (frequency, intensity, duration, session count) is not established at the network meta-analysis level — these vary across the 89 component RCTs. Practical dosing must draw from component RCTs and clinical judgment within evidenced ranges.
- **CC-13.** Network meta-analyses inherit the methodological quality of their component RCTs. SMD point estimates' clinical confidence depends on risk-of-bias of underlying trials. The very large effect sizes (SMD -1.67, -1.61) should be interpreted as "robust evidence of meaningful effect" rather than "exact magnitude prediction for any individual case."
- **CC-14.** CS-positive classification is not a permanent label. CS modulation is dynamic — sensitization can decrease with appropriate intervention. Re-screen CSI at intervention milestones; reclassify if features resolve.

---

## Content Mappings

### Educational Content Buckets (per Content Output Contract v1)

This research grounds content in:

- **Bucket: Educational** — "Why your chronic pain might be sensitization, not damage" / "Why combined exercise programs beat any single approach for chronic pain" / "Your nervous system's pain volume can be turned down — the science"
- **Bucket: Mechanics Breakdown** — How central sensitization produces regional pain spreading and flare cycling (the dorsal horn explanation, simplified)
- **Bucket: Fact or Fiction** — "Exercise can't help chronic pain when you're already too sensitized" → **FICTION** (Ibrahim 2025: SMD -0.81 overall, SMD -1.67 with combined stretching + strengthening, in populations specifically with central sensitization features). *Verified: Ibrahim's figures directly support this verdict.*
- **Bucket: Self-Test** — Symptom-quality logging (burning vs. mechanical ratio); regional involvement tracking; CSI questionnaire as a structured self-screen
- **Bucket: Recovery Window Framework** — "Why a single 'fix' rarely works for chronic pain — the combined program logic"

### Citation Format When Surfaced

Standard format for content captioning:

```
PMID: 39818121 | https://pubmed.ncbi.nlm.nih.gov/39818121/
Combined exercise programs reduce central sensitization indices in chronic musculoskeletal pain by SMD -1.67 (95% CrI -2.41 to -0.97), a very large effect — pooled across 89 randomized trials (Ibrahim et al. 2025).
```

For caption use (per Content Output Contract v1), citation lives above the three dots.

---

## Source References

- PMID: 39818121
- Link: https://pubmed.ncbi.nlm.nih.gov/39818121/
- Title: Comparative effectiveness of various exercise interventions on central sensitisation indices: A systematic review and network meta-analysis
- Authors: Ibrahim AAE, McWilliams DF, Smith SL, Chaplin WJ, Salimian M, Georgopoulos V, Kouraki A, Walsh DA
- Journal: Annals of Physical and Rehabilitation Medicine, 2025
- Verification: PubMed direct (not Google AI)

Exact figures (from abstract):
- Any exercise vs. baseline: SMD -0.81 (95% CI -0.93 to -0.70)
- Combined stretching + strengthening: SMD -1.67 (95% CrI -2.41 to -0.97)
- Strengthening + stretching + aerobic: SMD -1.61 (95% CrI -2.74 to -0.56)
- 89 RCTs in network meta-analysis (164 total RCTs; 249 eligible studies identified)

### Supplementary (context only — not seed grounding)

- PMID 38662515 — Chen et al. 2024, European Journal of Pain. Earlier meta-analysis on exercise effects on CS outcomes. Limited exact figures in abstract; superseded for seed purposes by the 2025 network meta-analysis but useful as supporting context.
- PMID 36963161 — Verbrugghe et al. 2023, Brazilian Journal of Physical Therapy. Single RCT (n=51) on high-intensity training for CS in chronic LBP at 6-month follow-up. Mean difference CSI 7.9 (95% CI 2.1, 12.7) favoring high-CSI subgroup. Useful as a specific component-RCT example demonstrating CS reduction with structured exercise.

---

## Confidence Level

**High.** Drivers: network meta-analysis (highest evidence level for comparative effectiveness); 89 RCTs in the network; tight confidence intervals on the overall effect; combined-modality SMDs in large-effect territory with lower bounds still in meaningful-effect territory; recent (2025); direct construct match between Ibrahim's CS indices and the case mechanism.

This is the strongest evidence base of any record authored to date and serves as a reference standard for the inflammation/sensitization layer of the system.

---

## Last Updated

2026-05-01 — initial mapping authored alongside captured record.
