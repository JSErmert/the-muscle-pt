---
record_id: research-004
slug: post-dislocation-scapular-dyskinesis-rehabilitation
status: active
date_mapped: 2026-05-01
study_pmid: 24458335
captured_record: records/research/captured/research-004-post-dislocation-scapular-dyskinesis-rehabilitation.md
linked_query: query-004
---

# RESEARCH RECORD 004 — System Mapping (L3)

This file holds Layer 3 — how Carbone et al. 2015 maps onto The Muscle PT system. Source capture and insight (L1, L2) are held in `records/research/captured/research-004-post-dislocation-scapular-dyskinesis-rehabilitation.md`.

---

## Case Engine Mapping

### Classification Implications

A chronic shoulder/scapular case with **all of the following** should be classified as the **post-dislocation chronic scapular dysfunction case category** (research-004 territory):

- History of one or more dislocation events at the shoulder/scapular region (any anatomical type — AC, glenohumeral, scapulothoracic, or unspecified)
- Chronic post-event state (not acute, not recently reduced)
- Current scapular dyskinesis features (asymmetric scapular position or motion, dyskinetic patterns on observation)
- Functional impairment at the affected shoulder
- No red-flag features (high-frequency recurrent dislocation, severe instability impacting daily life, motor weakness, neural deficits)

This classification is distinct from:
- Mechanical-dominant cases (research-001 — postural-mechanical sequencing applies)
- Localized single-root nerve cases (research-002 — neural tissue management cascade)
- Regional / widespread sensitization cases (research-003 — combined-modality program)

A case can fit multiple categories simultaneously (the linked query-001 case fits all four). Cross-record sequencing addresses this — see Decision Mapping below.

### Reassessment Infrastructure

Carbone supplies reassessment markers at multiple complexity levels:

- **Primary clinical:** Scapular dyskinesis observation (presence/absence by visual screen — lateral scapular slide test, scapular assistance test, scapular dyskinesis test)
- **Quantitative scapular:** SICK Scapula Rating Scale (Carbone reports 7.5 points post-treatment in subset)
- **Functional outcome:** Constant Score; Subjective Shoulder Value (0–100; Carbone reports improvement to 85 points at 12 months)

Field-usable subset (no equipment): **scapular dyskinesis observation + SSV self-report**. These two cover the dominant Carbone outcomes.

### Empirical Anchor for Conservative Trial

Carbone's intervention parameters as a portable trial framework:

- **Duration:** 12-week minimum, with reassessment at 6 weeks and 6 months, full outcome at 12 months
- **Content:** 12 scapular-focused strengthening and stretching exercises (specific prescription requires full-text review)
- **Expected resolution rate:** ~78% scapular dyskinesis resolution at 12 months
- **Functional outcome anchor:** Constant Score / SSV improving toward 85 points

Decision point at 12 months: if scapular dyskinesis has resolved and functional outcomes are tracking toward ~85, continue. If not responding, evaluate for escalation per ET-XX (escalation triggers).

---

## Decision Mapping

### Decision Logic Influence

For chronic post-dislocation cases without red flags:

1. **Open a structured 12-week+ scapular-focused rehabilitation trial** (12 strengthening and stretching exercises per Carbone) before considering surgical referral
2. **Reassess at 6 weeks, 6 months, and 12 months** per Carbone's framework
3. **Track SSV and scapular dyskinesis observation** as primary outcome markers; SICK Scapula Rating Scale if available
4. **Run alongside other applicable record sequencing** when multiple categories apply (e.g., for cases also fitting research-003 CS-positive, run combined-modality program that incorporates the scapular work)
5. **Hold escalation triggers active throughout** — at any point, red-flag features supersede the conservative trial

### What This Decision Logic Does NOT Authorize

- Treating cases without dislocation history as post-dislocation cases — the classification requires dislocation history as the upstream event
- Substituting generic rotator cuff strengthening for scapular-focused work — Carbone's intervention is specifically scapular
- Generalizing to AC vs. glenohumeral vs. scapulothoracic equivalently without acknowledging Carbone's AC-specific population — flag the inference explicitly when the case anatomical type differs from AC (CC-15)
- Surfacing this citation in default M1 outputs — citations remain off by default per CLAUDE.md Section 7. Surface only when significantly informative or explicitly requested.
- Extending the 12-week framework to acute post-event populations — those require different management

---

## Rule Candidates

Drawn from research-004 + linked case + cross-record interactions. Each is a *candidate* — promotion to firing rule requires repeated validation.

- **RC-11.** Chronic post-dislocation case at shoulder/scapular region + scapular dyskinesis features + no red flags → open a structured **12-week scapular-focused rehabilitation trial** (12 exercises, strengthening + stretching) before considering surgical referral. Reassess at 6 weeks, 6 months, 12 months
- **RC-12.** Reassessment expectation at 12 months: ~78% scapular dyskinesis resolution; SSV / Constant Score improvement toward 85 points. Cases substantially below this trajectory at 6-month checkpoint warrant evaluation for escalation
- **RC-13.** Cases with high-frequency recurrent dislocation (multiple events per year), imaging-confirmed structural lesions (large Hill-Sachs, significant Bankart, posterior labral tear), or severe daily-life impact → escalate; do not run extended conservative trial
- **RC-14.** When research-004 post-dislocation case AND research-003 CS features both present → run **combined-modality program that incorporates the scapular-focused work as a component** (per Ibrahim's network meta-analysis evidence + Carbone's specific scapular focus). Don't run scapular-only when CS features are positive

Promotion path: ≥ 2 validated firings without contradiction → formal rule per Bridge §10 Evolution Model.

---

## Constraint Candidates

- **CC-15.** Carbone's population is **type III acromioclavicular (AC) dislocation specifically.** Generalization to glenohumeral, scapulothoracic, or other dislocation types is inference, not direct evidence. Flag the inference explicitly when applying to non-AC cases. Research-007 (planned) addresses this gap.
- **CC-16.** Level IV evidence + n=24 → Confidence Medium. Treat the 78.2% resolution rate as "robust evidence of meaningful response" rather than "exact magnitude prediction for any individual case."
- **CC-17.** **Acute reducible dislocation requires immediate medical reduction** — research-004 applies to chronic post-event states only.
- **CC-18.** **High-frequency recurrent dislocation** likely warrants surgical evaluation, not extended conservative trial. The "Level II evidence suggests recurrence is lower with surgical management" finding from older systematic reviews (PMID 15162108) supports this when frequency is high.
- **CC-19.** Specific anatomical lesions (Bankart, large Hill-Sachs, posterior labral tear) may modify rehabilitation expectations downward. Imaging-confirmed lesions should adjust trial expectations or trigger surgical evaluation.
- **CC-20.** Specific exercise prescription details (frequency, intensity, progression) are not provided in Carbone's abstract — defer to full-text review for precise programming. The "12 exercises, scapular focus, 12-week+ duration" framework is the empirical anchor; specific dosing requires clinical judgment within evidenced ranges.

---

## Content Mappings

### Educational Content Buckets (per Content Output Contract v1)

This research grounds content in:

- **Bucket: Educational** — "Post-dislocation rehabilitation works — what the evidence says" / "Why scapular function matters after a shoulder dislocation" / "The 12-week framework for chronic shoulder instability — what to expect"
- **Bucket: Mechanics Breakdown** — Scapular dyskinesis mechanics post-dislocation (simplified anatomy: AC suspension vs. glenohumeral kinematics vs. scapulothoracic gliding; how dislocation alters each)
- **Bucket: Fact or Fiction** — "Once scapular dyskinesis becomes chronic, it can't be reversed" → **FICTION** (Carbone 2015: 78.2% scapular dyskinesis resolution at 12 months in chronic type III AC dislocation patients with structured rehabilitation; AC-specific evidence — disclose population in caption). *Verified against incident-002 standards: Carbone's 78.2% figure directly supports the verdict in the AC-specific population. Generalization caveat must appear in any caption use.*
- **Bucket: Self-Test** — Scapular dyskinesis observation (visual screen of resting scapular position, dynamic scapular motion during arm elevation, scapular assistance test); SSV self-rating
- **Bucket: Recovery Window Framework** — "12 weeks of structured scapular rehabilitation — what the outcomes look like" (with 78% resolution expectation, 6/12 month checkpoints, 85-point functional target)

### Citation Format When Surfaced

Standard format for content captioning:

```
PMID: 24458335 | https://pubmed.ncbi.nlm.nih.gov/24458335/
Structured 12-week scapular rehabilitation resolved scapular dyskinesis in 78.2% of patients (18 of 23) with chronic type III acromioclavicular dislocation at 12-month follow-up; mean Constant Score and Subjective Shoulder Value improved to 85 points (Carbone et al. 2015, n=24, Level IV).
```

For caption use (per Content Output Contract v1), citation lives above the three dots. The AC-specific population must be disclosed when the citation grounds a clinical claim about post-dislocation rehabilitation generally.

---

## Source References

- PMID: 24458335
- Link: https://pubmed.ncbi.nlm.nih.gov/24458335/
- Title: Scapular dyskinesis and SICK syndrome in patients with a chronic type III acromioclavicular dislocation. Results of rehabilitation
- Authors: Carbone S, Postacchini R, Gumina S
- Journal: Knee Surgery, Sports Traumatology, Arthroscopy, 2015
- Verification: PubMed direct (not Google AI)

Exact figures (from abstract):
- Scapular dyskinesis resolved in 18/23 patients (78.2%) at 12 months
- SICK syndrome observed in 4/8 patients with scapular malposition
- SICK Scapula Rating Scale: 7.5 points in 4 patients post-treatment
- Mean Constant Score and Subjective Shoulder Value: improved to 85 points at 12 months
- Sample: 24 enrolled; 23 analyzed at 12-month follow-up; 14 had SICK syndrome at baseline
- Intervention: 12 strengthening and stretching exercises of the scapulae
- Follow-up: 6 weeks, 6 months, 12 months
- Level of Evidence: IV

### Supplementary (context only — not seed grounding)

- PMID 27665529 — McIntyre et al. 2016, Physical Therapy in Sport. Systematic review of conservative rehab for posterior glenohumeral instability (5 studies). Narrative results only; no exact figures in abstract.
- PMID 15162108 — Gibson et al. 2004, Journal of Hand Therapy. Systematic review of nonoperative shoulder instability management. Recommends 3–4 wk immobilization + 12-week rehab framework. No exact outcome figures in abstract; "quantity and quality of evidence were low."

---

## Confidence Level

**Medium.** Drivers: Level IV evidence (case series, not RCT); n=24 (small); AC-specific population. Strengths: verifiable exact figures, direct mechanism match, clear intervention parameters, multi-timepoint follow-up at 12 months.

Promotion to High requires:
- A broader-population supporting record (research-007, planned) with exact figures on glenohumeral / multidirectional / scapulothoracic post-dislocation rehabilitation outcomes
- ≥ 1 dual-stream Phase 2 case demonstrating the rehabilitation-responsiveness pattern with the 12-week framework
- Full-text review detailing exercise prescription and statistical confidence intervals

---

## Last Updated

2026-05-01 — initial mapping authored alongside captured record.
