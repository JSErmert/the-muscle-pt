---
record_id: research-001
slug: thoracic-chest-mobility-chronic-neck-pain
status: active
date_mapped: 2026-05-01
study_pmid: 24835338
captured_record: records/research/captured/research-001-thoracic-chest-mobility-chronic-neck-pain.md
linked_query: query-001
---

# RESEARCH RECORD 001 — System Mapping (L3)

This file holds Layer 3 — how Wirth 2014 maps onto The Muscle PT system. Source capture and insight (L1, L2) are held in `records/research/captured/research-001-thoracic-chest-mobility-chronic-neck-pain.md`.

---

## Case Engine Mapping

### Classification Implications

When a case presents with chronic non-specific neck pain AND any of the following:
- Restricted thoracic flexion mobility
- Reduced chest expansion
- Reduced respiratory pressure generation
- Forward-head / kyphotic-thoracic posture
- Symptom flare on sustained thoracic flexion (seated forward lean, bowl-shaped seating)
- Symptom relief on thoracic extension + scapular retraction

…the case engine should treat the cervical complaint and the thoracic/respiratory pattern as a single mechanical system, not two separate problems.

### Reassessment Infrastructure

Wirth supplies a measurable variable set that can serve as reassessment markers for chronic neck pain cases:

- Neck Disability Index (NDI) — primary disability measure
- Thoracic flexion ROM — primary mobility measure
- Chest expansion (cm differential, full inspiration vs. expiration) — primary respiratory mechanic measure
- Pemax / Pimax — respiratory pressure generation (advanced; requires equipment)
- MVV — maximum voluntary ventilation (advanced; requires equipment)

Subset usable in field without equipment: **NDI + thoracic flexion ROM + chest expansion**. These three alone cover the dominant Wirth correlations.

### Provocation / Relief Test (clinical)

Reproducible provocation/relief pair drawn from linked case:
- Sustained seated thoracic flexion + scapular protraction (≥15 minutes) → reproduces or amplifies pain
- Thoracic extension + scapular retraction (1–2 minutes) → reduces pain

This pair can serve as a fast in-clinic mechanical screen for cases that fit the Wirth pattern.

---

## Decision Mapping

### Decision Logic Influence

For chronic neck pain cases fitting the Wirth pattern, intervention sequencing should prioritize:

1. **Restore thoracic extension mobility** before loading the cervical spine
2. **Restore chest expansion / respiratory mechanics** before progressing strength work
3. **Reposition scapulae (retraction capacity)** before loading shoulder or upper-back chains

This is a sequencing claim, not a universal protocol. It applies to cases that match the mechanical signature Wirth measured.

### What This Decision Logic Does NOT Authorize

- Treating every chronic neck pain case as a thoracic mobility case — Wirth's sample is non-specific CNP; specific pathologies (radiculopathy, post-surgical, post-traumatic acute) are out of scope
- Surfacing this citation in default M1 outputs — citations remain off by default per CLAUDE.md Section 7. Surface only when significantly informative or explicitly requested.

---

## Rule Candidates

Drawn from Wirth + linked case. Each is a *candidate* — promotion to firing rule requires repeated validation across additional cases.

- **RC-1.** Chronic neck pain + restricted thoracic flexion mobility → assess chest expansion and respiratory mechanics before progressing cervical loading
- **RC-2.** Sustained seated forward-flexion provocation pattern → screen for the Wirth pattern (thoracic + chest + cervical co-dysfunction)
- **RC-3.** Pain relief with thoracic extension + scapular retraction → bias intervention toward extension-restoration sequencing

Promotion path: each rule fires informally during dual-stream Phase 2 capture. After ≥ 2 validated firings without contradiction, promote to formal rule per Bridge §10 Evolution Model.

---

## Constraint Candidates

- **CC-1.** Wirth findings do not extend to specific cervical pathologies (radiculopathy, herniation, post-dislocation instability). Cases with neural compression signs, dislocation history, or structural pathology require separate research grounding (see related_records_planned in captured file).
- **CC-2.** Correlation ≠ causation. Wirth does not prove that restoring thoracic mobility resolves neck pain — only that they co-vary. Treat sequencing claims as bias, not protocol.
- **CC-3.** Non-specific CNP only. Acute injury, post-surgical, and pediatric populations are out of scope.

---

## Content Mappings

### Educational Content Buckets (per Content Output Contract v1)

This research grounds content in:

- **Bucket: Educational** — "Chronic neck pain isn't always a neck problem" / "Why your neck pain might live in your ribs and breathing"
- **Bucket: Fact or Fiction** — "Your neck pain has nothing to do with your breathing" (**FICTION** — Wirth's r = 0.42 chest expansion ↔ MVV; r = -0.58 Pemax ↔ NDI; r = -0.46 Pimax ↔ NDI directly support the verdict). *Note: previous entry mapped a "Stretching your neck fixes neck pain" claim as fiction-leaning; this was an interpretive leap beyond Wirth's actual scope. Corrected per incident-002.*
- **Bucket: Mechanics Breakdown** — Thoracic flexion ROM and chest expansion as upstream variables in chronic neck pain
- **Bucket: Self-Test** — Provocation / relief pair as an at-home screen ("if X position flares it and Y position calms it, your case fits a known pattern")

### Citation Format When Surfaced

```
PMID: 24835338 | https://pubmed.ncbi.nlm.nih.gov/24835338/
Thoracic flexion mobility correlates with respiratory capacity at r = 0.45; chest expansion at r = 0.42 (Wirth 2014, chronic non-specific neck pain).
```

For caption use (per Content Output Contract v1), citation lives above the three dots.

---

## Source References

- PMID: 24835338
- Link: https://pubmed.ncbi.nlm.nih.gov/24835338/
- Title: The relation between thoracic spine mobility, chest expansion, respiratory function, and chronic non-specific neck pain
- Authors: Wirth B, Amstalden M, Perk M, Boutellier U, Humphreys BK
- Journal: Manual Therapy, 2014
- Verification: PubMed direct (not Google AI)

---

## Confidence Level

Medium-High. Same as captured record. Upgrades to High after full-text review and ≥ 1 additional supporting record (research-005 or later).

---

## Last Updated

2026-05-01 — initial mapping authored. Same-date correction: Fact-or-Fiction content mapping replaced per incident-002 (original claim "Stretching your neck fixes neck pain" was not Wirth-supportable; PubMed search showed literature supports stretching as effective for chronic neck pain). New entry "Your neck pain has nothing to do with your breathing" → FICTION uses Wirth's correlation figures directly.
