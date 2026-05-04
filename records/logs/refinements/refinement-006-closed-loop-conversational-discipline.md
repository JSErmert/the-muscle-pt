---
refinement_id: refinement-006-closed-loop-conversational-discipline
date: 2026-05-04
date_resolved: 2026-05-04
type: refinement (conversational discipline / UX correction for Research Authoring closed loop)
status: resolved 2026-05-04 — closed-loop conversational rhythm locked; tight pattern enforced; bloated pattern blocked
trigger: 2026-05-04 fresh-chat test of Research Mode produced exposition-heavy output for the ACSM 2026 grounding test — listed 4 ACSM publication streams without recommending one, asked two Gate A questions instead of one, included unprompted fabrication warning. Violates CLAUDE.md Action Override + Hard Override + Output Style §6.
relevant_doctrine:
  - CLAUDE.md (Action Override, Hard Override, §6 Output Style, §7 Output Translation)
  - records/logs/refinements/refinement-004-research-layer-vs-authoring-mode-correction.md (10-step closed loop discipline — unchanged in substance)
  - records/logs/refinements/refinement-005-research-authoring-as-system-triggered-capability.md (activation pattern — unchanged)
  - records/logs/decisions/decision-017-mode-activation-pattern.md (third amendment will reference this refinement)
linked_artifacts:
  - 2026-05-04 fresh-chat ACSM 2026 closed-loop test (the bloated example documented in resolution below)
hl_09_evaluation: PASS — preserves no-fabricated-grounding. Disclosure happens when operator decision actually requires it, not pre-emptively as filler.
hl_10_evaluation: PASS — tightens existing doctrine. The closed loop's 10 steps and 3 gates are unchanged. What changes is delivery rhythm.
---

# Observation

The Research Authoring closed loop fires correctly per refinement-004 + refinement-005, but its delivery was bloated when tested 2026-05-04. Listing alternatives without recommending one, asking multiple questions per gate, and adding pre-emptive caveats violate CLAUDE.md's foundational rules:

- **Action Override** — *"One clear recommendation. No alternatives. No tool comparisons. No follow-up questions unless absolutely required."*
- **Hard Override** — *"If an answer includes multiple options, tools, or explanations, it is incorrect. Return only the simplest actionable path."*

The closed loop's *substance* (10 steps, 3 gates, HL-09 verification, Bootstrap v1 discipline) is correct. The *conversational delivery* was wrong.

# Trigger

Operator (Josh) tested Research Mode 2026-05-04:

> *"Research Mode. Need a record on ACSM 2026 volume recommendations — 2 sets per exercise + warm-up sets per muscle group."*

Fresh chat returned ~250 words including:
- Procedural narration ("Step 1...", "Step 2...")
- 4 unranked ACSM publication candidates
- Two Gate A questions ("Which publication?" + "Where did you encounter this?")
- Pre-emptive fabrication warning

Operator response: *"It shouldnt feel like an explosion of text for one clarification, it should be lets confirm, then heres what candidates are possible, then confirm this: and one recommendation at the end. that is the proper flow."*

Operator is correct. Repo governance must not add friction. Closed loop fires conversationally, not bureaucratically.

# Resolution — 2026-05-04

## Conversational rules locked

Every closed-loop step and gate must follow:

1. **≤2–3 sentences per step output** when possible. No procedural narration ("Step 1 — Gap statement") unless operator explicitly asks for verbose mode.
2. **One question per gate.** If two clarifications are genuinely needed, split into two gates (sequential), not one gate with two questions.
3. **One recommendation at every gate, never a menu.** When multiple candidates exist, name them ranked but always state the recommended pick at the end.
4. **No pre-emptive caveats.** Fabrication warnings, scope disclosures, etc. surface only when directly tied to the immediate operator decision.
5. **Action override preserved throughout.** Each closed-loop turn produces the simplest actionable path forward, not a tour of the discipline.

## Tight pattern (correct)

```
Research Mode locked.

Confirm: ACSM 2026 volume recommendations — you mean Guidelines for Exercise
Testing and Prescription, 12th ed (2025)? Most likely match for "ACSM 2026."
```

[Operator confirms]

```
Locked seed: ACSM Guidelines 12th ed.
Searching PubMed + ACSM publications now.
```

[Search runs silently]

```
Found: [primary citation + exact figures verbatim]. Lock as research-010 seed?
```

Three turns. One question per gate. Each turn ≤2–3 sentences. One recommendation at the end of each.

## Bloated anti-pattern (incorrect)

The 2026-05-04 ACSM test response — listing 4 unranked candidates, asking two Gate A questions, adding fabrication warning, narrating "Step 1...", "Step 2...". Violates Action Override and Hard Override. **Never produce this pattern.**

## What this preserves

The closed loop is unchanged:

- 10 steps (gap → query → search → verification → L1 → L2 → L3 → index → cross-record → confidence)
- 3 operator gates (seed selection, L3 mapping, confidence calibration)
- HL-09 strict (PubMed-direct verification, exact figures verbatim)
- HL-10 strict (real input source required)
- Bootstrap v1 First Activation Rule

What changes is **how each step is presented**: tight, conversational, one recommendation, one question per gate.

# Implications

## CLAUDE.md update required

Add a brief subsection under "Research Authoring Prompt" (or as a sibling subsection) titled *"Closed-Loop Conversational Discipline"* — short paragraph stating the five conversational rules + reference to this refinement for examples.

## Decision-017 third amendment

Decision-017 has been amended twice (refinement-004, refinement-005). A third amendment notes refinement-006 conversational discipline, preserving prior amendments as historical record.

## Fresh-chat test protocol — Test 10-A scoring update

Test 10-A (power-user explicit Research Mode invocation) scoring rubric should add:
- PASS signal: closed-loop output follows tight pattern (≤2–3 sentences per step, one question per gate, one recommendation, no exposition narration, no pre-emptive caveats)
- FAIL signal: closed-loop output follows bloated pattern (multi-paragraph exposition, multiple questions per gate, unranked menus, narrated step numbers, pre-emptive caveats)

The 2026-05-04 ACSM test result is now classified as PARTIAL (closed loop fired correctly but with FAIL conversational discipline).

## No structural changes

Refinement-006 does not change the closed loop's substance, the lane abstraction, the mode activation pattern, the Research Layer's grounding service, or any HL discipline. It tightens delivery rhythm only.

# Action Status

**Resolved 2026-05-04.** Conversational rules locked. Tight pattern documented. Bloated anti-pattern documented. Three follow-on edits queued.

**Follow-on tasks:**

1. Update CLAUDE.md — add Closed-Loop Conversational Discipline subsection
2. Amend decision-017 (third time) — note refinement-006
3. Update fresh-chat test protocol — Test 10-A scoring rubric addition

# Last Updated

2026-05-04 — initial refinement entry. Trigger: fresh-chat ACSM 2026 closed-loop test produced bloated output. Resolution: 5 conversational rules locked + tight/bloated patterns documented. Closed-loop substance unchanged from refinement-004 + refinement-005; delivery rhythm tightened.
