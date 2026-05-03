---
exercise_id: index-validation-001
date: 2026-05-01
type: validation log
purpose: demonstrate that records/research/index.md supports forward, reverse, and output queries per Research Index & Traceability v1
acceptance_criteria_satisfied:
  - "≥ 1 forward query (problem → research) demonstrably resolvable through the index"
  - "≥ 1 reverse query (research → system behavior) demonstrably resolvable through the index"
relevant_doctrine:
  - systems/intelligence/research-index-and-traceability-v1.md
  - systems/intelligence/research-query-layer-v1.md
  - architecture/m2-operationalize-milestone-plan-v1.md (Acceptance Criterion #4)
---

# M2 Index Query Resolution Exercise — 2026-05-01

This is a one-shot validation exercise to confirm that `records/research/index.md` supports the three query patterns defined in `research-index-and-traceability-v1.md`:

- **Forward query:** problem → research
- **Reverse query:** research → system behavior
- **Output query:** output → research

Per the M2 milestone plan, Acceptance Criterion #4 requires *both* a forward and reverse query "demonstrably resolvable through the index." This log demonstrates each on the seed records (research-001 and research-002) authored on this same date.

---

## Exercise 1 — Forward Query (problem → research)

### Real-World Problem

> *"A clinician (Zach) is presented with a chronic neck pain client whose symptoms flare in the car on long drives. Sitting in a bowl-shaped car seat reproducibly triggers a posterior chain pain wrap. The client reports that arm-behind-back retraction with a lean-back squeeze relieves it. What does the system know about this pattern?"*

This is a synthetic but realistic Stream A scenario — a client presentation that matches the linked case underlying query-001.

### Index Resolution Path

1. **Open `records/research/index.md`.**
2. **Pattern match against Use Cases sections.** The query terms "chronic neck pain", "sustained-flexion provocation", "extension-retraction relief" map directly to the Use Cases of:
   - **research-001** — listed Use Case: query-001 (chronic right-dominant thoracic + cervicothoracic + posterior chain dysfunction; bowl-shaped car seat provocation; arm-behind-back retraction relief).
3. **Read research-001's System Mappings section.** Index entry surfaces:
   - Case Engine Mapping (classify as single co-dysfunction; reassessment markers NDI + thoracic flexion ROM + chest expansion)
   - Decision Mapping (sequencing bias: thoracic extension first, then chest expansion, then scapular repositioning)
   - Rule Candidates RC-1, RC-2, RC-3
   - Constraint Candidates CC-1, CC-2, CC-3
   - Content buckets (Educational, Fact or Fiction, Mechanics Breakdown, Self-Test)
4. **Verify source backing.** Index entry surfaces verified PMID 24835338 (Wirth 2014, Manual Therapy) with exact figures: thoracic flexion ↔ MVV r = 0.45, chest expansion ↔ MVV r = 0.42, Pemax ↔ NDI r = -0.58, Pimax ↔ NDI r = -0.46.
5. **Drill into full record if needed.** File pointers in the index entry navigate to:
   - `captured/research-001-...md` for L1 source + L2 insight
   - `mapped/research-001-...md` for L3 system mapping detail
   - `queries/query-001-...md` for the originating real input

### Output

Forward query resolves in a single page lookup. The clinician receives:
- Pattern recognition (this is the Wirth pattern)
- Sequencing bias for intervention
- Field-usable reassessment markers
- Verified source grounding for any clinical claim made

### Verdict

**PASS.** Forward query (problem → research) is demonstrably resolvable through the index. Resolution depth: single page; supporting detail one file pointer away.

---

## Exercise 2 — Reverse Query (research → system behavior)

### Subject

**research-002** — Lutke Schipholt et al. 2026, *Musculoskeletal Science and Practice*. PMID 41620319. PET/CT-quantified neuroinflammation reduction with 6 weeks / 12 sessions of nerve and joint mobilisation in chronic cervical radiculopathy.

### Reverse Question

> *"Given this study, what system behaviors does it influence? What rules, constraints, decisions, and content does it ground?"*

This is the canonical reverse query pattern from `research-index-and-traceability-v1.md`.

### Index Resolution Path

1. **Open `records/research/index.md`.**
2. **Locate research-002 in Active Records.** Direct anchor lookup — index is organized by record ID.
3. **Enumerate the System Mappings section.** Index surfaces the complete behavior set this record grounds:

#### Case Engine Behaviors

- **Classification rule:** Cases with cyclical nerve-quality symptoms during inflammation flares + soft-tissue marker change + no red-flag features → classify as inflammation-driven nerve compression cascade (distinct from disc-driven radiculopathy).
- **Reassessment proxies (field-usable):** palpable soft-tissue marker change, symptom-quality logging (nerve vs. mechanical), provocation/relief response, NDI (shared with research-001).

#### Decision Logic Behaviors

- **Open structured 6-week / 12-session conservative trial** (nerve and joint mobilisation) before escalation
- **Run research-001 sequencing in parallel** when both axes positive — not sequentially
- **Maintain symptom-quality logging** alongside NDI throughout trial
- **Hold escalation trigger active** — red flags supersede trial at any point

#### Rule Candidates Grounded by research-002

- **RC-4** — Chronic cervical pain + cyclical nerve-quality symptoms + no red flags → screen for inflammation-driven cascade; do not assume disc-driven by default
- **RC-5** — Inflammation-driven cascade identified without red flags → 6-week / 12-session conservative trial before escalation
- **RC-6** — Both research-001 mechanical pattern AND research-002 inflammation cascade present → run sequencing on both axes in parallel

#### Constraint Candidates Grounded by research-002

- **CC-4** — N=1 case report; do not generalize without confirming case fits cascade pattern (research-005 planned)
- **CC-5** — Red-flag features supersede conservative trial — escalate immediately
- **CC-6** — Inflammation-driven cascade is mechanistically distinct from disc-driven radiculopathy
- **CC-7** — 6-week / 12-session is empirical anchor, not magic dose
- **CC-8** — Field-usable reassessment markers are clinical proxies, not equivalent to PET/CT VT in evidentiary weight

#### Content Buckets Grounded by research-002

- Educational ("Why your nerve pain isn't always your discs")
- Mechanics Breakdown (how inflammation drives nerve symptoms; now measurable)
- Fact or Fiction ("If you have nerve pain, you need an MRI / surgery" — fiction-leaning when red flags absent)
- Self-Test (cyclical inflammation-driven vs. constant disc-driven)
- Recovery Window Framework ("The 6-week / 12-session conservative trial — what it is, when it is appropriate, when it is not")

#### Source Grounding Verified

- PMID 41620319 — exact figures resolvable directly from index entry (VT 12.96 → 6.21 neuroforamen; VT 6.43 → 5.38 spinal cord; 12 sessions / 6 weeks; maintained at 6 months)
- Confidence ceiling: Low-Medium (N=1 case report)
- Confidence promotion path: research-005 (planned) + ≥ 1 dual-stream Phase 2 case demonstrating the pattern

### Verdict

**PASS.** Reverse query (research → system behavior) is demonstrably resolvable through the index. Resolution depth: single index entry surfaces every rule, constraint, decision logic point, and content bucket the record grounds. Each behavior is traceable to a specific exact figure in the source record (e.g., RC-5's "6-week / 12-session" anchor maps directly to the study's "12 sessions of nerve and joint mobilisation" intervention specification).

---

## Exercise 3 — Output Query (output → research)

### Bonus demonstration. Not required by Acceptance Criterion #4, included to validate the third query pattern in the same exercise.

### Hypothetical Output

> *Fact or Fiction caption draft: "Your neck and your breathing live in the same system. Restrict one and the other compensates."*

### Index Resolution Path

1. **Open `records/research/index.md`.**
2. **Scan Content Mappings sections across all Active Records.** The "Fact or Fiction" bucket is matched in:
   - **research-001** — bucket entry: "Your neck pain has nothing to do with your breathing" (FICTION; Wirth figures support the verdict directly)
3. **Read source grounding.** PMID 24835338, exact figures r = 0.42 chest expansion ↔ MVV; r = -0.58 Pemax ↔ NDI; r = -0.46 Pimax ↔ NDI.
4. **Citation contract satisfied:** caption can carry verified PMID + exact figure above the three dots per Content Output Contract v1.

*Note: this example was updated 2026-05-01 to reflect research-001's corrected L3 mapping. The original example resolved to a "Stretching your neck fixes neck pain" mapping that was caught and corrected during content-002 production — the citation discipline at content-output time forced the mapping correction. See incident-002 for the full pre-output drift catch.*

### Verdict

**PASS.** Output query (output → research) is demonstrably resolvable. The Content Mappings sections in the index act as the lookup table from output bucket back to grounding research.

---

## Aggregate Findings

| Query Pattern | Required by Acceptance Criterion #4 | Result |
|---|---|---|
| Forward (problem → research) | Yes | **PASS** |
| Reverse (research → system behavior) | Yes | **PASS** |
| Output (output → research) | No (bonus) | **PASS** |

### Observations

1. **Index design holds.** A single page lookup resolves any of the three query patterns without requiring drill-down into captured/ or mapped/ files. File pointers exist for deeper retrieval but are not required for the typical query.
2. **Co-location of source figures + system mapping is load-bearing.** Each behavior in the index entry sits next to its grounding figures. This is what makes claims like "open a 6-week / 12-session trial" *traceable in one glance* rather than a multi-file dig.
3. **Confidence levels surface naturally.** Both records carry their confidence ceilings in the index, and the planned-record system (research-005 to elevate research-002) makes the gap explicit rather than hidden.
4. **The Wirth + Lutke Schipholt pairing is more than additive.** RC-6 (run mechanical and inflammation axes in parallel) only emerged because both records were authored together. This validates the M2 doctrine choice to author records when use cases demand them, not in bulk — the pairing only became visible because the same case (query-001 → query-002) drove both.

### What Did Not Pass

Nothing failed. One soft observation worth flagging:

- The index does not yet support **negative queries** ("what does the system explicitly NOT claim about X?"). Constraint Candidates approximate this but require knowing which record to look in. A future enhancement (probably post-M2) might add a top-level "Out of Scope" or "Constraint Index" lookup table. **Logged as an observation, not a refinement** — does not block M2 closeout.

---

## Acceptance Criterion Update

Per `architecture/m2-operationalize-milestone-plan-v1.md`:

- **Criterion #4** — *"≥ 1 forward query (problem → research) and ≥ 1 reverse query (research → system behavior) demonstrably resolvable through the index"* → **SATISFIED** by this exercise.

---

## Last Updated

2026-05-01 — initial validation exercise authored.
