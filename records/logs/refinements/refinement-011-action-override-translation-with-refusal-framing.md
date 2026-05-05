---
refinement_id: refinement-011-action-override-translation-with-refusal-framing
date: 2026-05-04
date_resolved: 2026-05-04
type: refinement (strongest doctrine attempt — Action Override placement + refusal framing + concrete examples + closed-loop exception tightening)
status: PARTIALLY SUBSUMED BY REFINEMENT-013 (2026-05-04). PRESERVED: Action Override placement of the identifier-translation rule + refusal framing ("if your draft contains these patterns, the response is invalid; do not return it"). REFRAMED: the two-tier closed-loop exception (specific identifiers allowed at gates / abstract architecture terminology translates) was restructured by refinement-013 as audience-based (operator-facing surfaces / client-facing artifact body). CORRECTED: the WRONG/CORRECT examples in this refinement's lineage included the bypass-message translation that refinement-013 superseded. Preserved as historical record of the four-element bundle attempt; the placement and framing landed, the surface-based exception model was reframed by refinement-013. Original status: resolved 2026-05-04 — identifier-translation rule moved to Action Override, refusal framing locked, WRONG/CORRECT examples documented in CLAUDE.md, closed-loop exception tightened to specific identifiers only.
trigger: Pre-Alpha-5 (2026-05-04 fresh run, Josh Max account, post-refinement-010 commit) produced identical 5 internal-identifier leaks to Pre-Alpha-4 — same 2 HL-05 leaks in artifact body + 3 leaks on handoff line. Refinement-010's §7 enforcement subsection ("scan-and-translate before return") was active in CLAUDE.md but did not land in production. Doctrine-not-landing despite explicit declaration AND enforcement framing means we've reached either (a) a placement / framing problem or (b) a model instruction-following ceiling. This refinement is the strongest single attempt to resolve before accepting a model ceiling and shifting to operator-side review.
relevant_doctrine:
  - CLAUDE.md (Action Override section — gets identifier-translation rule; §7 OUTPUT TRANSLATION — restructured with refusal framing + WRONG/CORRECT examples + tightened closed-loop exception; §5 — cross-reference updated)
  - records/logs/refinements/refinement-009-internal-identifier-leakage-in-artifact-output.md (declaration layer)
  - records/logs/refinements/refinement-010-internal-identifier-translation-enforcement.md (§7 enforcement layer)
  - architecture/operator-observation-loop-v1.md (Pre-Alpha-5 entry will reference this refinement when filed)
linked_artifacts:
  - Pre-Alpha-4 fresh-chat session (2026-05-04, original 5-leak observation)
  - Pre-Alpha-5 fresh-chat session (2026-05-04, identical 5-leak recurrence post-refinement-010 commit)
hl_09_evaluation: PASS — no fabricated grounding. Refinement adds enforcement framing only.
hl_10_evaluation: PASS — addition justified by repeated leak pattern. Pre-Alpha-4 surfaced the leaks; refinement-009/010 attempted declaration + enforcement; Pre-Alpha-5 demonstrated both attempts insufficient. This refinement is the strongest single doctrine attempt before accepting a model ceiling.
---

# Observation

Refinements 009 and 010 attempted to prevent internal-identifier leaks in artifact output:

- Refinement-009 added §5 declaration ("must not name internal identifiers")
- Refinement-010 added §7 enforcement ("scan-and-translate before return")

Pre-Alpha-5 fresh run with both active produced identical leaks to Pre-Alpha-4 (same chat input, same output, same 5 internal-identifier leaks). **Doctrine isn't landing.** Three possible causes:

1. **§7 placement too late.** §7 sits near the bottom of CLAUDE.md. Action Override + Hard Override + §6 OUTPUT STYLE are far more attended.
2. **Principle-language framing still too soft.** "Scan and translate" reads as a transformation step, not a refusal.
3. **Model instruction-following ceiling.** Doctrine specificity at this level may exceed what the web model reliably applies.

This refinement is the strongest single doctrine attempt — combining placement, framing, examples, and exception tightening. If it still doesn't land in Pre-Alpha-6, the response shifts to operator-side review (Zach reviews artifact for jargon before client delivery), accepting that doctrine has a ceiling.

# Trigger

Pre-Alpha-5 fresh-chat session (2026-05-04, Josh Max account, post-refinement-010 commit `758b3d1`) produced identical output to Pre-Alpha-4:

- **Handoff line** (3 leaks): *"Switching to Clinical Mode. Movement Case Engine active. Building the protocol now, grounded to research-010."*
- **Block 2 description**: *"HL-05 applies: reassess before advancing — if technique degrades, hold load"*
- **Section header**: *"HL-05 reassessment markers per block transition:"*

Same 5 leaks. Refinement-010's §7 enforcement subsection failed to prevent recurrence.

Josh additionally observed *"L3 — mapping gateway"* in Gate B output (*"Gate B — L3 system mapping"*). L3 is internal Bootstrap v1 layer terminology. Currently doctrine-exempted under refinement-010's closed-loop exception, but unfamiliar to a production operator (Zach) without doctrine onboarding. The exception is too broad.

# Resolution — 2026-05-04

Four-element bundle: placement + framing + examples + exception tightening.

## 1. Identifier-translation rule moved to Action Override

CLAUDE.md Action Override section adds a new bullet:

> *No internal system identifiers in artifact output. If your draft response contains HL-X, research-XXX, refinement-XXX, decision-XXX, §X, or system component / engine / doctrine layer names anywhere in artifact output (protocol templates, content, client deliverables, including handoff lines), the response is invalid. Do not return it. Rewrite with internal identifiers translated to operator-readable language. See §7 Internal-Identifier Translation Pass for WRONG/CORRECT examples.*

Action Override is the most-attended doctrine section. Placement at this level operates equivalent to "no menus, no follow-up questions" — top-of-attention rules.

## 2. Refusal framing replaces transformation framing

Old (§7, refinement-010): *"Before returning any artifact output, scan for these patterns and translate to the principle they encode."*

New (§7, refinement-011): *"If your draft response contains these patterns in artifact output, the response is invalid. Do not return it. Rewrite from scratch with internal identifiers translated to operator-readable language."*

Refusals are followed more reliably than instructed transformations. The framing aligns with Hard Override structure already in CLAUDE.md ("If an answer includes multiple options, tools, or explanations, it is incorrect").

## 3. Concrete WRONG/CORRECT examples in CLAUDE.md §7

Models follow concrete examples more reliably than abstract principles. The actual Pre-Alpha-4/5 leaks become the documented FAIL examples with verbatim corrected versions:

> **WRONG:** *"HL-05 applies: reassess before advancing — if technique degrades, hold load"*
> **CORRECT:** *"Reassess before advancing — if technique degrades, hold load"*
>
> **WRONG:** *"HL-05 reassessment markers per block transition:"*
> **CORRECT:** *"Reassessment markers per block transition:"*
>
> **WRONG:** *"Switching to Clinical Mode. Movement Case Engine active. Building the protocol now, grounded to research-010."*
> **CORRECT:** *"Building the protocol now, grounded to the ACSM 2026 Position Stand."*

These exact strings appear in CLAUDE.md §7 as the canonical translation reference.

## 4. Closed-loop exception tightened — two-tier model

Refinement-010's closed-loop exception treated all gate output as exempt. Refinement-011 splits the exception into two tiers:

**Allowed at gates (operators legitimately need these for doctrine-aware confirmation):**
- Specific record identifiers operators are confirming: *research-XXX*, *PMID-X*
- Hard-lock identifiers when operator is confirming a specific compliance decision: *HL-X*
- Gate naming itself: *Gate A / Gate B / Gate C* (low semantic load, operator learns quickly)

**Translate at gates (abstract architecture terminology — unfamiliar without doctrine onboarding):**
- Layer names: *L1 / L2 / L3* → *"L3 system mapping"* becomes *"How this record applies to your work"*
- Engine names: *Case Engine* → *"Clinical practice"*; *Movement Case Engine* → *"Clinical practice engine"*
- Architecture names: *Decision Layer* → *"Decision-making"*
- Contract names: *Content Output Contract* → *"Content production rules"*
- Lane names: *Insight Lane* / *Script Lane* / *Exercise-to-Script Lane* → *"Insight content"* / *"Exercise scripts"* / etc.

Gate B output that previously read *"Case Engine — Default RT prescription..."* now reads *"Clinical practice — Default RT prescription..."* etc.

## What this preserves

- HL-09 untouched — internal identifier references must still be REAL
- Refinement-008 untouched — recommendation closes every gate
- Refinement-007 untouched — search before Gate A turn flow
- §6 Iterative Refinement untouched — full-artifact reprint on iteration
- Closed-loop substance — 10 steps, 3 gates, doctrine-aware decision moments preserved

## What this changes

Internal-identifier discipline now operates at three layers:
- Action Override (top-of-attention refusal rule)
- §5 (constraint declaration)
- §7 (refusal framing + concrete examples + tightened exception)

# Honest framing — model ceiling possibility

If Pre-Alpha-6 fresh run still leaks despite this four-element bundle, the doctrine has hit a model instruction-following ceiling. Adding more doctrine past that point produces diminishing returns. The production response then becomes:

- **Operator-side review:** Zach reads artifact output for internal identifiers before client delivery, replacing them as a final manual pass
- **Workflow integration:** the manual review becomes an explicit step in the production workflow, not a doctrine reliance
- **Doctrine pause:** stop adding identifier-translation refinements; document the ceiling

This refinement is one strong attempt, not an infinite escalation. Pre-Alpha-6 result determines next move.

# Implications

## CLAUDE.md updates required

1. Action Override section — add new bullet with refusal framing
2. §7 OUTPUT TRANSLATION — restructure Internal-Identifier Translation Pass with refusal framing, concrete WRONG/CORRECT examples, tightened closed-loop exception
3. §5 refinement-009 bullet — cross-reference updated to point to Action Override + §7

## No decision-017 amendment needed

Not Mode Activation. Decision-017 unchanged.

## Pre-Alpha-5 + Pre-Alpha-6 observation entries

Pre-Alpha-5 entry should be filed in `architecture/operator-observation-loop-v1.md` documenting the doctrine-not-landing failure that triggered this refinement. Pre-Alpha-6 entry (when run) determines whether refinement-011 landed or whether we hit the model ceiling.

# Action Status

**Resolved 2026-05-04.** Four-element bundle locked: Action Override placement + refusal framing + concrete examples + closed-loop exception tightening. Honest model-ceiling framing recorded for next-iteration decision.

**Follow-on tasks:**

1. Update CLAUDE.md Action Override — add identifier-translation refusal rule
2. Update CLAUDE.md §7 — restructure Internal-Identifier Translation Pass with refusal framing + WRONG/CORRECT examples + two-tier closed-loop exception
3. Update §5 cross-reference if needed
4. Pre-Alpha-5 entry in `architecture/operator-observation-loop-v1.md`
5. Run Pre-Alpha-6 fresh test — if leaks persist, shift to operator-side review

# Last Updated

2026-05-04 — initial refinement entry. Trigger: Pre-Alpha-5 fresh run produced identical 5 leaks to Pre-Alpha-4 despite refinement-010 §7 enforcement active. Resolution: four-element bundle (Action Override placement + refusal framing + concrete WRONG/CORRECT examples + closed-loop exception tightened to two-tier model). Honest model-ceiling framing recorded — if Pre-Alpha-6 still leaks, doctrine has hit a model capability ceiling and the production response shifts to operator-side review rather than additional doctrine.
