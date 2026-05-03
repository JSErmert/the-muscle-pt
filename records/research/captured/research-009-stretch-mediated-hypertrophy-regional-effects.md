---
record_id: research-009
slug: stretch-mediated-hypertrophy-regional-effects
status: locked v1 — Medium-High confidence; closed loop complete (Gates A/B/C all passed 2026-05-03)
date_authored: 2026-05-03
date_locked: 2026-05-03
linked_query: query-009-stretch-mediated-hypertrophy
primary_pmid: 40570881
primary_authors: Varovic D, Wolf M, Schoenfeld BJ, Steele J, Grgic J, Mikulic P
primary_journal: International Journal of Sports Medicine
primary_year: 2025
primary_publication_date: December 2025
primary_design: Bayesian systematic review and meta-analysis
primary_sample: 12 studies of young adults
primary_confidence: Medium-High
supplementary_pmids:
  - 39959841 (Wolf et al. 2025 — within-participant RCT, n=30, lengthened partials vs full ROM equivalence)
  - 41247250 (Havers et al. 2025 — within-subject RCT, n=13, pROM initial vs fROM at distal muscle length)
trigger_input: cross-lane reference gap — Exercise-to-Script Lane Spec v1 + content-004 (RDL) both reference stretch-mediated hypertrophy as significantly-informative-eligible without grounded record
gate_status:
  - Gate A (Seed Selection) — passed 2026-05-03 — operator selected Path 1 (Varovic primary + Wolf/Havers supplementary)
  - Gate B (L3 Mapping Review) — passed 2026-05-03 — operator confirmed L3 mapping with micro-refined CC-Y soften option
  - Gate C (Confidence + Cross-Record Promotion) — passed 2026-05-03 — Medium-High confidence locked; downstream edits authorized
---

# RESEARCH-009 — Stretch-Mediated Hypertrophy Regional Effects

This record grounds the "stretch-mediated hypertrophy" reference surfaced by Exercise-to-Script Lane Spec v1 and content-004 (RDL). The closed-loop authoring under corrected Research Authoring Mode (per refinement-004, 2026-05-03) executes here as the first formal application of the corrected discipline.

The honest finding is that the effect is **real but modest, and concentrated at distal muscle portions** — not the dominant hypertrophy driver the lane spec language currently implies.

---

## L1 — Source Capture (Primary)

### Citation

Varovic D, Wolf M, Schoenfeld BJ, Steele J, Grgic J, Mikulic P. **Does Muscle Length Influence Regional Hypertrophy? A Systematic Review and Meta-Analysis.** International Journal of Sports Medicine. December 2025. PMID: 40570881.

URL: https://pubmed.ncbi.nlm.nih.gov/40570881/

### Study Design

Bayesian systematic review and meta-analysis examining whether resistance training at longer muscle lengths produces greater regional hypertrophy compared to training at shorter muscle lengths.

### Sample

Twelve studies of young adults included in the meta-analysis.

### Verified Effect Sizes (verbatim from PubMed direct, exact figures with units)

| Region of muscle length | Standardized Mean Difference (SMD) | 95% Quantile Interval | Exponentiated lnRR |
|---|---|---|---|
| Proximal (25%) | 0.05 | [−0.07, 0.16] | 0.57% |
| Mid-belly (50%) | 0.07 | [−0.02, 0.15] | 1.22% |
| Distal (75%) | 0.09 | [−0.01, 0.19] | 1.88% |

The percentage of posterior distributions falling within regions of practical equivalence was high across all three measured sites — meaning the effect is likely small enough to be practically equivalent across muscle length conditions.

### Disclosed Limitations (from source)

The average difference between "shorter" and "longer" condition muscle lengths in the primary studies was only **~21.8%** — a modest separation. This warrants cautious interpretation: the meta-analysis cannot speak to extreme separations between training conditions; the data describes the effect within typical training-research separations.

---

## L1 — Source Capture (Supplementary Context)

### Wolf et al. 2025 (PMID 39959841)

Wolf M, Korakakis PA, Piñero A, Mohan AE, Hermann T, Augustin F, Sapuppo M, Lin B, Coleman M, Burke R, Nippard J, Swinton PA, Schoenfeld BJ. **Lengthened partial repetitions elicit similar muscular adaptations as full range of motion repetitions during resistance training in trained individuals.** PeerJ. February 12, 2025. PMID: 39959841.

URL: https://pubmed.ncbi.nlm.nih.gov/39959841/

**Design:** Within-participant RCT, n=30 trained individuals, 8-week upper-body program.

**Verified findings:**
- Muscle thickness improvements similar between lengthened partials (LP) and full ROM conditions
- Bayes factors **0.16 to 0.3** = "moderate" support for the **null hypothesis** of equal improvement across interventions
- Authors' conclusion: *"Trainees seeking to maximize muscle size should likely emphasize the stretched position, either by using a full ROM or LPs during upper-body resistance training."*

**Adds to record-009:** direct head-to-head comparison evidence that lengthened partials and full ROM produce similar hypertrophy. Reinforces the meta-analysis finding that practical equivalence is high.

### Havers et al. 2025 (PMID 41247250)

Havers T, Wagner N, Held S, Geisler S, Wiewelhove T. **Partial Range, Full Gains? The Effect of 8 Weeks of Partial Range of Motion Training at Long Muscle Lengths on Elbow Flexor Hypertrophy and Strength in Trained Individuals.** European Journal of Sport Science. November 17, 2025. PMID: 41247250.

URL: https://pubmed.ncbi.nlm.nih.gov/41247250/

**Design:** Within-subject RCT, n=13 trained individuals (small), 8-week unilateral preacher curls, pROM initial (0°–70°) vs fROM (0°–140°).

**Verified findings:**
- Muscle thickness at 50% humeral length: SMD 0.10 (similar between conditions)
- Muscle thickness at 70% humeral length (distal): SMD 0.10, Bayes factor 4.87 (moderate evidence for H1) — pROM initial 7.60% increase vs fROM 4.38% increase
- 1RM: fROM 28.01% vs pROM 21.59% — full ROM slightly favored for strength

**Adds to record-009:** regional measurement at distal muscle length specifically. The 70% humeral length finding is the closest direct support for "stretch-mediated hypertrophy lives at the distal portion" claim — but the absolute effect is small (SMD 0.10), and full ROM produced greater 1RM strength gains.

---

## L2 — Insight Extraction

### What the evidence establishes

1. **The effect of muscle-length emphasis on regional hypertrophy is small.** The strongest available meta-analysis (Varovic 2025, 12 studies) reports SMDs of 0.05 / 0.07 / 0.09 across proximal / mid-belly / distal regions. None exceed Cohen's "small" threshold (SMD ≥ 0.20).

2. **The effect is most pronounced distally.** All three verified candidates (Varovic meta-analysis, Wolf RCT, Havers RCT) point in the same direction — when an effect exists, it manifests at the distal portion of the muscle. Havers 2025 specifically measured 70% humeral length and found SMD 0.10 with moderate evidence (BF 4.87).

3. **Lengthened partials are not superior to full ROM.** Wolf 2025 directly tested this question and found Bayes factors 0.16–0.3 supporting the null. Practical implication: if a trainee can perform full ROM safely, full ROM is the default — lengthened partials are a valid alternative, not a superior tool.

4. **Full ROM may favor strength outcomes.** Havers 2025 1RM data (fROM 28.01% vs pROM 21.59%) suggests full ROM is the safer call when strength is a co-equal goal.

5. **Mechanism plausibility is real but not equivalent to large effects.** Sarcomerogenesis at long muscle lengths and mechanotransduction under stretch are well-described mechanisms. The data say the mechanism translates to a small practical effect, not to dominant hypertrophy driver status.

### What the evidence does NOT establish

1. **That stretch-mediated hypertrophy is "where hypertrophy lives."** The lane spec language is overclaim relative to the evidence. Hypertrophy is driven primarily by volume, intensity, frequency, and proximity to failure — muscle length emphasis is a small modifier, not a foundation.

2. **That distal advantages translate to functional or aesthetic outcomes.** A 1.88% lnRR difference at the distal region is a measurement-level finding, not necessarily a visible-result-level finding. Citation surfacing should not promise visible results from muscle length emphasis alone.

3. **That this generalizes across all muscles, training experience levels, or rep ranges.** Varovic's meta-analysis is "young adults" with the 21.8% length-separation limitation. Untrained populations, older populations, or extreme load ranges are not directly tested.

4. **That extreme stretching positions (beyond typical training ROM) would amplify the effect.** The 21.8% separation limitation matters here — we don't know what would happen at 50%+ separation between conditions, only what happens at typical research separations.

### Confidence rationale

**Medium-High.** Justification:

- **Strong evidence design:** the primary seed is a Bayesian meta-analysis (highest evidence grade for population-level questions). 12 studies. Recent (December 2025).
- **Convergent supporting evidence:** Wolf 2025 RCT (n=30, trained) + Havers 2025 RCT (n=13, trained, regional measurement) point in the same direction as the meta-analysis.
- **Honest effect-size disclosure:** the effects are SMD 0.05–0.10 — small. Confidence should not exceed Medium-High because the effect is modest, not because the evidence is weak.
- **Practical equivalence finding:** Varovic explicitly flags that posterior distributions fell within regions of practical equivalence at high frequency. This is honest acknowledgment that the effect, where present, is small.

**Not High** because the effect is small relative to other hypertrophy drivers; calibrating to High would imply the variable is more important than the data supports.

**Not Medium** because the evidence design is meta-analytic with convergent RCT support. Downgrading to Medium would understate the evidence quality.

**Promotion criteria for High:**
1. A second independent meta-analysis or NMA reports SMDs ≥ 0.20 at any region
2. A large RCT (n > 100) demonstrates practical (not statistical) significance
3. Mechanism studies establish dose-response with extreme separation that translates to clinically meaningful effect

**Promotion criteria for Low:** evidence reversal — meta-analyses showing no effect at all regions.

---

## Cross-Record Positional Note

Research-009 is **not a horizontal modifier** like research-008 (which modifies how interventions apply across other records). Research-009 is a **vertical record** (mechanism layer) that grounds a specific biomechanics claim referenced by the Exercise-to-Script Lane Spec.

Its primary function in the system is to ground citation surfacing in the Exercise-to-Script Lane (and incidentally in any Insight Lane content that references the topic). It does not modify Clinical Lane interventions (the lane operates on pain/dysfunction/rehab, not hypertrophy programming).

---

## Last Updated

2026-05-03 — L1 source capture (primary + supplementary) and L2 insight extraction authored at steps 5–6 of corrected Research Authoring Mode closed loop. Gate A passed (operator selected Path 1). L3 mapping authored at step 7 in companion file (`records/research/mapped/research-009-...md`). Gate B pending.
