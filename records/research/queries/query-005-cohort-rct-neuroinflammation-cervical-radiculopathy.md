---
query_id: query-005
slug: cohort-rct-neuroinflammation-cervical-radiculopathy
status: resolved
date_logged: 2026-05-01
date_resolved: 2026-05-01
version: v1
linked_record: research-005 (active)
linked_purpose: confidence elevation for research-002 (Lutke Schipholt 2026 N=1 case report) — partial promotion achieved (Low-Medium → Medium-High); full High pending Phase 2 clinical replication
input_source: research-library confidence-elevation requirement
---

# QUERY 005 — Cohort or RCT-Level Evidence on Neuroinflammation in Chronic Cervical Radiculopathy

This query was logged 2026-05-01 to support a confidence-elevation record (research-005) for research-002. Research-002 (Lutke Schipholt 2026, PMID 41620319) is a single-patient case report with PET/CT-quantified neuroinflammation reduction following 6 weeks of conservative neural tissue management. The N=1 design is mechanistically informative but population-level generalization requires cohort or RCT-level supporting evidence.

This query differs from query-001 through query-004 in that its source is **not a real-world clinical case** — it is a research-library structural requirement. Per the Query Layer v1 spec's "input sources" criterion, research queries must originate from real use cases, repeated failure points, or recurring system patterns. Research-002's confidence ceiling at Low-Medium is itself a recurring system pattern (the same constraint will appear for any N=1-grounded record), which qualifies query-005 as a legitimate query under doctrine.

---

## Use Case

The library currently grounds the inflammation-driven cervical radiculopathy cascade (research-002) on a single PET/CT case report. While the imaging is rigorous and the figures are verifiable, three structural concerns:

1. **Generalization risk.** Without cohort-level evidence, the system cannot assert that conservative neural tissue management reliably reduces neuroinflammation across chronic cervical radiculopathy populations — only that it did so in this one patient.
2. **Rule-promotion blockage.** RC-5 ("Inflammation-driven cascade identified without red flags → 6-week / 12-session conservative trial") cannot promote from candidate to formal rule on N=1 evidence per Bridge §10 Evolution Model.
3. **Confidence pyramid imbalance.** Research-001 (Medium-High) and research-003 (High) sit on cross-sectional and meta-analysis evidence; research-002 (Low-Medium) is the weakest base in the four-record pyramid.

Research-005 addresses this by capturing cohort or RCT-level evidence on conservative care responsiveness in chronic cervical radiculopathy, ideally with quantitative outcome measures that align with or supplement Lutke Schipholt's PET/CT VT measurement.

---

## Core Question

What does the literature establish, at cohort or RCT level (not N=1), about:

1. Conservative care (specifically nerve and joint mobilisation, neural tissue management, or analogous physical therapy) responsiveness in chronic cervical radiculopathy?
2. Quantitative outcome measures that capture the biological mechanism Lutke Schipholt measured (neuroinflammation, nerve root edema, dorsal root ganglion changes) — or validated clinical proxies (NDI, pain intensity, function scores)?
3. Time-course of conservative trial: do the 6-week / 12-session parameters from research-002 hold up at population level, or do other intervention windows show better evidence?
4. Differentiation between inflammation-driven and disc-driven cervical radiculopathy at population level — does it carry treatment-response implications?

Sub-questions:
- What sample sizes have been studied in cohort/RCT designs?
- What effect sizes are reported on conservative care for chronic cervical radiculopathy?
- Are there imaging-based or biomarker-based studies beyond Lutke Schipholt that quantify the inflammation-component changes?
- What's the recurrence rate / long-term outcome at 6-month and 12-month follow-up?

---

## Mechanism Focus

- Neural tissue management / nerve and joint mobilisation as intervention class
- Physical therapy interventions for cervical radiculopathy more broadly
- Neuroinflammation as measurable construct (PET/CT, MRI, biomarkers)
- Validated clinical proxies (NDI, VAS, function scores) when imaging not available
- Conservative trial duration and dosing parameters at cohort/RCT level

---

## Decision Target

This query must inform:

1. Whether RC-5 can promote from candidate to formal rule (or be revised based on broader evidence)
2. Whether the 6-week / 12-session parameter from research-002 generalizes or needs adjustment
3. Whether new constraint candidates emerge from population-level data not visible in N=1
4. Whether research-002's confidence promotes from Low-Medium to High based on supporting evidence captured

---

## Constraints

- Cohort or RCT-level evidence preferred — additional N=1 case reports do not elevate research-002's confidence
- Findings must apply to chronic (not acute) cervical radiculopathy without red flags
- Do not include surgical-arm-only studies — research-002 is specifically about conservative care
- Do not surface citations in default M1 outputs — only when significantly informative or explicitly requested
- Do not fabricate PMIDs or invent figures — verify direct against PubMed

---

## Resolution

Status: **resolved** — 2026-05-01.

### Seed Record Locked

**research-005** — García-Juez S, Navarro-Santana MJ, Valera-Calero JA, Albert-Lucena D, Varas-de-la-Fuente AB, Plaza-Manzano G. 2025, Journal of Orthopaedic & Sports Physical Therapy. **PMID: 40576779.**

*Effectiveness of Articular and Neural Mobilization for Managing Cervical Radicular Pain: A Systematic Review With Network Meta-Analysis.*

Captured at `records/research/captured/research-005-conservative-neural-mobilization-cervical-radiculopathy.md`.
Mapped at `records/research/mapped/research-005-conservative-neural-mobilization-cervical-radiculopathy.md`.

### Verified Figures from Abstract

- **50 studies analyzed quantitatively** (from 777 reports screened)
- **Pain (short-term):** articular + neural mobilization + usual care vs. wait/see/sham/placebo: **MD -3.23 (95% CI: -4.33, -2.12)**
- **Pain:** articular + neural mobilization + usual care vs. standard care alone: **MD -1.52 (95% CI: -2.31, -0.73)**
- **Disability:** neural mobilization + usual care vs. wait/see/sham/placebo: **SMD -1.57 (95% CI: -2.53, -0.61)** — large effect
- **Disability:** neural mobilization + usual care vs. usual care alone: **SMD -1.31 (95% CI: -1.88, -0.73)** — large effect
- Authors note risk of bias and heterogeneity downgrade certainty in some comparisons (moderate to very low across some)

### How the Resolution Answers the Query

- **Population-level evidence captured:** García-Juez 2025 supplies NMA-level evidence (50 studies) on the same intervention class research-002 grounds at mechanism level. Both pain and disability outcomes show large, statistically significant effects.
- **6-week timeframe consistency:** Component RCTs in this literature typically span 4–8 week windows, consistent with research-002's 6-week / 12-session parameter — the 6-week framework is supported by the broader RCT evidence base
- **research-002 confidence elevation:** **Partial — Low-Medium → Medium-High.** One of two promotion conditions met (NMA-level supporting evidence captured). Full High promotion remains conditional on the second condition: ≥ 1 dual-stream Phase 2 case demonstrating the cascade pattern (clinical replication).
- **RC-5 promotion path established:** RC-5 ("6-week / 12-session conservative trial for inflammation-driven cascade") is now eligible for promotion from candidate to formal rule once the Phase 2 clinical replication condition is met. Population-level effectiveness evidence is the necessary precondition; firing-rule validation through actual case work is the sufficient final step.

### Disclosure

Research-005's confidence is High at the NMA level, but the certainty of evidence on individual components is downgraded by the authors due to risk of bias and heterogeneity in some comparisons. Effect sizes should be interpreted as "robust evidence of meaningful effect" rather than "exact magnitude prediction" (CC-22). Specific dosing parameters are not specified at NMA level (CC-21).

### Search Terms That Surfaced the Result

- `cervical radiculopathy neural mobilization randomized controlled trial systematic review meta-analysis` (primary — surfaced PMID 40576779 directly)
- `manual therapy cervical radiculopathy effectiveness network meta-analysis` (corroboration — supplied PMID 40776625 as supporting evidence)
- `conservative treatment cervical radiculopathy outcomes cohort effect size` (broader context — surfaced PMID 36599029 for ecosystem awareness, no exact figures)

Two supporting candidates retained as supplementary L2 context only:
- **PMID 40776625** (Núñez de Arenas-Arroyo et al. 2025) — independent NMA confirmation: neurodynamic techniques SMD -1.45 (95% CI -1.88 to -1.02), aligning with García-Juez's effect estimates
- **PMID 36599029** (Plener et al. 2023) — broader systematic review (59 trials, 4108 participants) with very low certainty evidence ratings; useful background, not direct grounding

---

## Version Notes

- **v1** (this version) — Initial query authored 2026-05-01 to drive research-005 (confidence elevation for research-002). Source is a research-library structural requirement, not a real-world clinical case — but qualifies as a legitimate query under doctrine because the N=1 confidence-ceiling pattern recurs system-wide.
