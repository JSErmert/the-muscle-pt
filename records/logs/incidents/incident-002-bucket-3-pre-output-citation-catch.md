---
incident_id: incident-002
date: 2026-05-01
type: pre-output drift caught (Bucket 3 citation discipline)
severity: Low (caught before any output published; no client / audience exposure)
detection_layer: Content Output Contract v1, Bucket 3 — Random Fun Facts / Science Explained (locked Fact or Fiction format)
linked_files:
  - execution/content-output-contract-v1.md
  - records/research/captured/research-001-thoracic-chest-mobility-chronic-neck-pain.md
  - records/research/mapped/research-001-thoracic-chest-mobility-chronic-neck-pain.md
  - records/research/index.md
  - records/research/validation/2026-05-01-index-query-resolution-exercise.md
  - records/content/planned/content-002-fact-or-fiction-neck-pain-breathing.md
preceded_by: incident-001 (cold-test translation failures, 5 of 7 outputs leaked engine names)
status: resolved (pivot completed, L3 mapping corrected, validation log updated, content-002 produced with corrected grounding)
---

# INCIDENT 002 — Pre-Output Bucket 3 Citation Drift Caught

A planned content piece (content-002, Bucket 3 — Fact or Fiction) failed the Bucket 3 citation-discipline check during production. The original trigger-phrase candidate's verdict could not be supported by direct research grounding. The system halted production, surfaced the finding, pivoted the claim, and corrected the upstream L3 mapping that had produced the unsupported pre-map.

This incident documents the **pre-output catch as a system-validation event** — the citation discipline did its job and prevented drift from reaching the audience.

---

## What Happened

### Original Plan

Following research-001's L3 Content Mappings, content-002 was scheduled to produce a Bucket 3 (Fact or Fiction) reel on:

> *"Fact or fiction. Stretching your neck fixes neck pain. Fiction."*

This trigger phrase was derived from research-001's L3 entry at the time:

> **Bucket: Fact or Fiction** — "Stretching your neck fixes neck pain" (fiction-leaning given Wirth's thoracic + respiratory findings)

The "(fiction-leaning)" hedge had already been a soft signal in the L3 mapping that the verdict was not fully grounded.

### Detection

Per Content Output Contract v1, Bucket 3 requires:

> Required: specific research citation with figures (effect size, percentage decrease in force production, duration of effect)

Producing the verdict required research that *directly supports* the claim "stretching alone is insufficient for chronic neck pain." A PubMed search was run before drafting:

- `stretching exercise alone chronic neck pain effectiveness systematic review`
- `neck stretching versus combined exercise chronic neck pain RCT`

Findings (verified PubMed search results):

| PMID | Author/Year | Finding |
|---|---|---|
| 25780258 | Tunwattanapong et al. | A 4-week neck and shoulder stretching program decreased neck/shoulder pain and improved function in office workers with chronic neck pain |
| 17351694 | Ylinen et al. | "Both stretching exercise and manual therapy considerably decreased neck pain and disability in women with non-specific neck pain" |
| 18586810 | Häkkinen et al. | One-year follow-up: no significant difference in improvement between strength training + stretching vs. stretching alone — both probably as effective |
| 30135909 | de Campos et al. | Strengthening preferred over stretching alone in office workers, but stretching still effective |
| Systematic review aggregate | — | "5 of 6 studies reported significant improvement in pain or decrease in pain prevalence" with stretching programs |

**Conclusion:** the literature supports stretching as effective for chronic neck pain (closer to fact than fiction). The "fiction" verdict on "stretching your neck fixes neck pain" is not directly supportable by current evidence. Producing the originally planned reel would have been a citation-contract violation.

### Root Cause of the Pre-Map Error

When research-001's L3 was authored on the same date (2026-05-01), the Fact-or-Fiction entry was an **interpretive leap** beyond Wirth's actual scope. Wirth (PMID 24835338) studied correlations between thoracic mobility, chest expansion, respiratory function, and chronic neck pain — *not* stretching as an intervention. The pre-map inferred that because thoracic and respiratory factors are upstream, treating only the neck (including via stretching) must be insufficient. That inference is not what Wirth measured.

The "(fiction-leaning)" hedge was the L3 author's tell that the mapping was not fully grounded. The Bucket 3 contract's strict citation requirement caught the gap that the hedge had only partially flagged.

---

## Action Taken

1. **Halted content-002 production** under the original trigger phrase
2. **Surfaced the finding to the user** with the alternative pivot proposal
3. **User confirmed** the pivot to a Wirth-directly-supported claim
4. **Pivoted content-002** to "Your neck pain has nothing to do with your breathing" → FICTION, supported by three direct Wirth figures (r = 0.42, r = -0.58, r = -0.46)
5. **Corrected research-001's L3 Fact-or-Fiction mapping** in `records/research/mapped/research-001-thoracic-chest-mobility-chronic-neck-pain.md` to remove the unsupported claim and replace with the Wirth-supported one
6. **Updated `records/research/index.md`** Content Mappings + research-001 Last Updated + top-level Last Updated
7. **Updated `records/research/validation/2026-05-01-index-query-resolution-exercise.md`** Output Query example to reflect the corrected L3 mapping
8. **Authored content-002** with corrected grounding, all 8 pass criteria PASS-state achieved
9. **Logged this incident** for M2 closeout audit reference

---

## System Behavior — Working as Designed

This incident is a **success of the citation discipline**, not a failure. The system caught a pre-output drift event before any audience exposure. The chain of catches:

1. The L3 author hedged with "(fiction-leaning)" — soft warning
2. The Bucket 3 contract demanded direct figure-backed support — hard gate
3. The PubMed verification step revealed the verdict was not groundable
4. The system halted, escalated, and corrected upstream

This is what HL-09 (no fabricated grounding) and the citation contract are *for*. The cost of the catch was a few minutes of search and a draft pivot. The cost of *not catching* would have been a published reel that misrepresented the science to Zach's audience.

---

## Refinement Signal — Should L3 Content Mappings Require Direct-Citation Justification at Authoring Time?

**Open question for refinement consideration.** This is one occurrence — log as observation. If recurs in future L3 authoring (research-003, research-004, research-005), escalate to a refinement entry per Bridge §10 Evolution Model.

Candidate refinement (if it recurs):

> When authoring L3 Content Mappings, each Bucket entry must include a one-line justification of *which exact figures from the captured study support this content claim*. Hedged tags like "(fiction-leaning)" are not sufficient. If no exact figures support the verdict directly, the bucket entry should not be authored — wait for a future research record that does support it directly, or reframe the claim until it can be grounded.

This would tighten the upstream L3 authoring discipline so the catch happens at L3 authoring time, not at content-output time. Both layers catching is good (defense in depth); the goal is to minimize how often content-output time has to do the upstream's job.

---

## Related Observations

- **Affiliate line gap recurrence:** content-001 and content-002 both used the same `[Standard affiliate line — placeholder, to be supplied by founder]` because the Content Output Contract does not specify the affiliate line. This is now N=2 occurrences. If recurs in content-003, escalate to a refinement entry per ET-03 (recurring pattern). Tracked separately, not in scope of this incident.

---

## Severity and Closure

**Severity: Low.** Caught pre-output. No audience exposure. No published drift. System worked as designed. Documentation cost (this incident, three file edits, one validation log update) is small relative to the value of the catch.

**Closed: 2026-05-01.** Pivot complete; mappings corrected; content-002 produced; M2 audit trail established.

---

## Last Updated

2026-05-01 — incident authored at time of catch and pivot.
