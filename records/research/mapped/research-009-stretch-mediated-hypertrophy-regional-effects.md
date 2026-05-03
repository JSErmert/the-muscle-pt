---
record_id: research-009
slug: stretch-mediated-hypertrophy-regional-effects
mapping_type: L3 system mapping
status: locked v1 — closed loop complete (Gates A/B/C all passed 2026-05-03)
date_authored: 2026-05-03
date_locked: 2026-05-03
companion_file: records/research/captured/research-009-stretch-mediated-hypertrophy-regional-effects.md
primary_pmid: 40570881
linked_query: query-009-stretch-mediated-hypertrophy
gate_status:
  - Gate A — passed 2026-05-03
  - Gate B — passed 2026-05-03 — operator confirmed L3 with micro-refined CC-Y soften option
  - Gate C — passed 2026-05-03 — Medium-High confidence locked; downstream edits authorized
---

# RESEARCH-009 — L3 SYSTEM MAPPING

This file maps research-009 (stretch-mediated hypertrophy regional effects) to the system: Case Engine, Decision Mapping, Rule Candidates, Constraint Candidates, Content Mappings, and Lane Spec implications.

The dominant L3 implication is that **the Exercise-to-Script Lane Spec language requires softening** — the data does not support "this is exactly where stretch-mediated hypertrophy lives" as written. The honest grounding is "modest effect, most pronounced distally, not the dominant hypertrophy driver."

---

## Case Engine Mapping

Research-009 is a **vertical record (mechanism layer)** focused on hypertrophy programming. It does NOT directly modify Clinical Lane case management — Clinical Lane operates on pain / dysfunction / rehab, not on hypertrophy outcomes.

**Indirect Case Engine touchpoints:**

- **Return-to-strength programming after rehab (Clinical → Programming transition).** When a clinical case completes rehab and returns to strength training, exercise selection should default to full ROM; lengthened partials are a valid substitute when full ROM is contraindicated by tissue irritability or joint geometry.
- **Hypermobile populations (research-008 cross-reference).** For hypermobile patients in rehab-to-strength transition, the lengthened position emphasis is *contraindicated* until stability is restored — even though research-009 shows a modest distal hypertrophy advantage in non-hypermobile populations, applying it to hypermobile cases would risk the substrate failure mode research-008 describes.

**Case Engine output:** no new case classifications. Research-009 informs intervention selection at the rehab-to-strength interface but does not introduce a new clinical case category.

---

## Decision Mapping

When the operator is selecting between exercise variants for hypertrophy programming (Exercise-to-Script Lane work, or general programming guidance):

| Decision context | Default | Lengthened-position alternative | When to switch |
|---|---|---|---|
| Trainee can perform full ROM safely | **Full ROM** | Lengthened partials | When full ROM is contraindicated by tissue irritability, joint geometry, or post-rehab status |
| Trainee targets distal regional hypertrophy specifically | Lengthened-position emphasis is a valid bias (modest) | Full ROM still acceptable | Effect is small (SMD 0.10 at 70% muscle length); not a dominant choice |
| Trainee targets strength (1RM) alongside hypertrophy | **Full ROM** (Havers 2025: fROM 28.01% vs pROM 21.59% for 1RM) | Lengthened partials de-prioritized | Strength outcomes favor full ROM |
| Trainee has hypermobility substrate (research-008 positive) | Stability-first; defer hypertrophy emphasis | NOT a substitute pathway — research-008 horizontal modifier overrides | Until stability is restored |

**Decision rule summary:** full ROM is the default. Lengthened partials are a valid alternative, not a superior tool. The effect is modest enough that other programming variables (volume, intensity, frequency, proximity to failure) dominate the hypertrophy outcome.

---

## Rule Candidates

### RC-X (proposed) — Default to Full ROM for Hypertrophy

When programming for hypertrophy in a healthy non-hypermobile trainee, full ROM is the default exercise prescription. Lengthened partials are a substitute pathway when full ROM is contraindicated, not a superior option in steady-state programming.

**Grounding:** Wolf 2025 (PMID 39959841) directly tested LP vs fROM and found Bayes factors 0.16–0.3 supporting null. Varovic 2025 (PMID 40570881) found regional SMDs of 0.05–0.09 — none exceed small-effect threshold.

**Status:** candidate. Promotion to formal RC requires: (a) Phase 2 case demonstrating decision-relevance OR (b) operator-confirmed adoption.

### RC-Y (proposed) — Calibrated Citation Surfacing for Modest-Effect Findings

When a research record's primary effect size is small (SMD < 0.20 across regions), citation surfacing in lane content must reflect the modest nature of the effect — not affirmative overclaim. Honest framing: "research suggests a modest [X] effect, most pronounced [where applicable]" rather than "research proves [X]."

**Grounding:** research-009's effect sizes (SMD 0.05–0.09 in meta-analysis) require this discipline. Any future small-effect record will face the same surfacing question.

**Status:** candidate. Likely generalizable beyond research-009. Promotion requires N=2 small-effect records benefiting from the same discipline.

---

## Constraint Candidates

### CC-X (proposed) — Modest-Effect Citation Discipline

Stretch-mediated hypertrophy effect sizes (Varovic 2025 SMDs 0.05–0.09) are small. Citation surfacing must:
- State the SMD with units verbatim (per CLAUDE.md §7)
- Disclose the practical-equivalence finding when relevant
- NOT generalize to "lengthened-position is the secret to muscle growth" or similar overclaim
- Frame the effect as a regional modifier at the distal portion, not as a dominant driver

### CC-Y (proposed) — Lane Spec Language Softening Requirement [LOCKED 2026-05-03]

The Exercise-to-Script Lane Spec v1's RDL worked example previously read: *"This is exactly where stretch mediated hypertrophy lives."*

This language was overclaim relative to research-009. **Operator-locked replacement (Gate B, 2026-05-03):**

> *"This is the lengthened position. The modest stretch-mediated hypertrophy effect concentrates here."*

Two period statements. Anatomy named first; effect characterization second with "modest" baked into the noun phrase. Matches Zach's coach-voice rhythm in the worked example.

Lane spec edit + content-004 edit triggered post-Gate C.

### CC-Z (proposed) — Hypermobility Override

In hypermobile cases (research-008 positive), the lengthened-position advantage of research-009 is **not applicable** — substrate stability requirements override hypertrophy-optimization choices. The horizontal modifier wins.

---

## Content Mappings

### Insight Lane — Bucket 1 (Why Should You Care)

Candidate: *"Why ROM matters in your training."* — full grounding from research-009 with honest acknowledgment of modest effect. Could also reference Schoenfeld physiology review (PMC10587333) for mechanism context if needed. Strong educational angle: "the effect is small, so don't sacrifice load or volume to chase lengthened partials."

### Insight Lane — Bucket 3 (Fact or Fiction)

Strong candidate: *"Stretching the lengthened position is the secret to muscle growth."* → **FICTION-LEANING.** Grounded by Varovic SMDs 0.05–0.09 and Wolf Bayes factors 0.16–0.3 supporting null. Verdict not "FICTION" outright because the effect is *real*, just small. Honest verdict: *"Mostly fiction — the effect is real but small. Volume and intensity are the bigger drivers."*

### Exercise-to-Script Lane — YouTube Description Citation Surfacing

When relevant exercises (RDL, stiff-leg deadlift, lying leg curl, incline DB press, cable fly, and other lengthened-position-loaded exercises) surface this in their YouTube clip descriptions, the canonical citation format is:

```
[Surfacing context, e.g. "Why this exercise emphasizes the stretched position:"]

PMID: 40570881 | https://pubmed.ncbi.nlm.nih.gov/40570881/
SMD 0.09 distal regional hypertrophy advantage [95% QI: −0.01, 0.19] in resistance-trained young adults; effect is modest and most pronounced at the distal portion of the muscle.
```

The figure is exact, the units are correct, the framing is honest about effect size.

### Exercise-to-Script Lane — Reel Script Default

Default: **NO citation surfaced in the reel script.** The effect is too modest to qualify as "significantly informative" under CLAUDE.md §7 for the audio reel format. Surface only if Zach explicitly elects to elevate the claim.

### Carousel Lane (deferred)

If/when activated: research-009 supports a carousel breakdown of "How muscle length affects hypertrophy" — modest-effect story, regional patterning, decision implications. Deferred per decision-016.

---

## Cross-Record Implications

### Lane Spec language requires softening

`execution/exercise-to-script-lane-spec-v1.md` references stretch-mediated hypertrophy in the RDL worked example. The line *"This is exactly where stretch mediated hypertrophy lives"* is overclaim per research-009.

**Required action:** at Gate B, operator selects soften-option A / B / C (per CC-Y above). Lane spec edit follows.

### Content-004 (RDL) requires soften update

`records/content/planned/content-004-rff-romanian-deadlift.md` Section 4 (Biomechanics) reads: *"This is exactly where stretch mediated hypertrophy lives."* Same language as the lane spec worked example.

**Required action:** content-004 Section 4 updates same direction as lane spec. Triggered after Gate B.

### research-001 / research-002 / research-003 / research-004 / research-005 / research-008

No direct cross-record implications. Research-009's mechanism layer (hypertrophy programming) does not overlap with the clinical/rehabilitation focus of the other records.

### Confidence promotion potential for other records

None triggered by research-009. The record stands as Medium-High; no promotion implications upstream.

### Future records this might inform

If a future research record is authored on:
- Eccentric-specific hypertrophy
- Volume / intensity / proximity-to-failure as primary hypertrophy drivers
- Periodization for hypertrophy

…research-009 should be cross-referenced as the regional-modifier record that contextualizes those primary-driver records.

---

## Lane Spec Implications (specific edits required)

The Exercise-to-Script Lane Spec v1 (`execution/exercise-to-script-lane-spec-v1.md`) requires three changes triggered by research-009:

1. **RDL worked example, Section 4 (Biomechanics):** soften the stretch-mediated hypertrophy line per CC-Y operator selection (option A / B / C).
2. **Citation Discipline section:** add explicit reference to research-009 as the canonical source when surfacing stretch-mediated hypertrophy in YouTube descriptions. Provide the canonical citation format from Content Mappings above.
3. **8 Overarching Pass Criteria, criterion #4 (Biomechanics correctly identified):** add a note that biomechanics claims with small underlying effect sizes (per the relevant research record) must be framed as modest, not affirmative.

These edits are downstream of Gate B operator confirmation. They do NOT happen until research-009 locks at Gate C.

---

## Gate B — L3 Mapping Review (operator)

The L3 mapping above is drafted. Gate B asks the operator to confirm three things before proceeding to Gate C:

1. **Case Engine Mapping** — does the rehab-to-strength transition framing land correctly? Should hypermobile-population override be more prominent?

2. **Rule Candidates and Constraint Candidates** — are RC-X (Default to Full ROM), RC-Y (Calibrated Citation Surfacing), CC-X (Modest-Effect Citation Discipline), CC-Y (Lane Spec Language Softening), CC-Z (Hypermobility Override) all aligned with the system's operating philosophy? Any missing? Any to remove?

3. **Lane Spec Soften Option** — operator selection among CC-Y options A / B / C (or a fourth option of operator's choosing) for the lane spec language correction. This selection unlocks the Gate C confidence + cross-record promotion review.

Operator confirmation at Gate B unlocks steps 8–10 (index entry + cross-record implications + confidence calibration) and Gate C.

---

## Last Updated

2026-05-03 — L3 system mapping authored at step 7 of corrected Research Authoring Mode closed loop. Case Engine mapping, Decision Mapping, Rule Candidates (RC-X, RC-Y), Constraint Candidates (CC-X, CC-Y, CC-Z), Content Mappings (Insight Lane Buckets 1 + 3, Exercise-to-Script Lane YouTube descriptions + reel default), Cross-Record Implications, and Lane Spec Implications all drafted. Gate B pending operator confirmation.
