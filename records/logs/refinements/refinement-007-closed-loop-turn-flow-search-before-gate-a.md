---
refinement_id: refinement-007-closed-loop-turn-flow-search-before-gate-a
date: 2026-05-04
date_resolved: 2026-05-04
type: refinement (closed-loop turn flow / sequencing correction for Research Authoring)
status: resolved 2026-05-04 — search-before-Gate-A locked; pre-search guessing blocked
trigger: 2026-05-04 fresh-chat test of Research Mode for "ACSM 2026 volume recommendations" surfaced Gate A confirmations BEFORE executing PubMed search. Pre-search guess (ACSM Guidelines 12th ed) was wrong; actual search found ACSM 2026 Position Stand. The closed loop self-corrected mid-flow with an "important correction" — friction the operator should never have seen.
relevant_doctrine:
  - CLAUDE.md (Action Override, Hard Override, §6 Output Style, §7 Output Translation)
  - records/logs/refinements/refinement-004-research-layer-vs-authoring-mode-correction.md (10-step closed loop — substance unchanged)
  - records/logs/refinements/refinement-005-research-authoring-as-system-triggered-capability.md (activation pattern — unchanged)
  - records/logs/refinements/refinement-006-closed-loop-conversational-discipline.md (delivery rhythm — preserved; this refinement adds turn-flow on top)
  - records/logs/decisions/decision-017-mode-activation-pattern.md (fourth amendment will reference this refinement)
linked_artifacts:
  - 2026-05-04 fresh-chat ACSM 2026 pre-search Gate A test (the wrong-path example documented in resolution below)
hl_09_evaluation: PASS — strengthens no-fabricated-grounding. Pre-search guesses are speculative by definition; running the search first means Gate A only ever surfaces real candidates verified against PubMed/source.
hl_10_evaluation: PASS — tightens existing doctrine. The 10 closed-loop steps and 3 gates are unchanged. What changes is *when* Gate A fires within the turn sequence.
---

# Observation

The Research Authoring closed loop has correct substance (refinement-004) and correct delivery rhythm (refinement-006), but its turn-flow sequence was wrong when tested 2026-05-04. The closed loop asked the operator to confirm a candidate seed *before* searching — which forced a guess from training-data plausibility, then required an "important correction" once the actual search ran.

This violates two principles:

- **CLAUDE.md Action Override** — *"One clear recommendation. No alternatives. No tool comparisons."* A pre-search guess is by definition not the recommended pick; it is a guess.
- **HL-09 (no fabricated grounding)** — pre-search candidates surfaced at Gate A are not grounded against PubMed or source. They are training-data plausibility judgments dressed as recommendations.

The 10-step closed loop (refinement-004) and the 5 conversational rules (refinement-006) are unchanged. What changes is the **sequence within a single turn**: search runs first, then Gate A presents verified candidates only.

# Trigger

Operator (Josh) tested Research Mode 2026-05-04:

> *"Research Mode. Need a record on ACSM 2026 volume recommendations — 2 sets per exercise + warm-up sets per muscle group."*

Fresh chat returned:
- Confirmation #1: *"You mean ACSM Guidelines for Exercise Testing and Prescription, 12th ed (2025)?"*
- Operator confirmed.
- Then search ran.
- Then **"Important correction"** — actual source is ACSM 2026 Position Stand, not the Guidelines.
- Closed loop continued from corrected seed.

Two confirmations consumed before any real evidence existed. The pre-search guess was wrong, and the operator had to absorb a mid-flow correction. From the operator's perspective, this is friction that should not exist — the system can search before asking.

Operator response: *"We need to skip directly from the second input (Research Mode. Need...) directly to the CORRECT ACSM's 2026 Position Stand."*

Operator is correct. The closed loop must not surface candidates the system has not yet verified.

# Resolution — 2026-05-04

## Turn-flow rules locked

The closed loop's first turn must follow this sequence:

1. **Search executes BEFORE Gate A. Always.** Step 3 (PubMed search) and step 4 (PMID/figure verification) run silently before any operator confirmation is requested.
2. **Gate A presents verified candidates only.** The seed offered to the operator must already be verified — exact citation, PMID, exact figure verbatim. No pre-search guesses, no plausibility-ranked menus from training data.
3. **Single turn from mode declaration to Gate A.** The operator's first message ("Research Mode. Need X") triggers: gap statement → query draft → search → verification → seed presentation. All silent until Gate A.
4. **Pre-search clarification is the exception, not the default.** If the operator's request is genuinely ambiguous in a way that would change the search query itself (not the candidate selection), one clarifying turn is allowed — but only when the search cannot be drafted without it. Default assumption: the search can be drafted from the operator's input.

## Tight pattern (correct turn flow)

```
Operator: "Research Mode. Need a record on ACSM 2026 volume recommendations
— 2 sets per exercise + warm-up sets per muscle group."
```

[System silently: gap → query → PubMed/ACSM search → verification]

```
Research Mode locked.

Found: ACSM 2026 Position Stand on Resistance Training (PMID: <verified>).
States: <exact figure verbatim with units>. Lock as research-XXX seed?
```

[Operator confirms or corrects]

One operator turn → one Gate A turn. The seed presented is real, verified, and ready to lock.

## Bloated anti-pattern (incorrect turn flow)

The 2026-05-04 ACSM test response — asking *"You mean Guidelines 12th ed?"* before searching, then issuing an *"important correction"* once the actual search produced a different source. **Never produce this pattern.**

The failure mode is identifiable: any time Gate A presents a candidate without a PMID and verbatim figure already attached, the search has not run. That is the wrong-path signal.

## What this preserves

The closed loop is unchanged:

- 10 steps (gap → query → search → verification → L1 → L2 → L3 → index → cross-record → confidence)
- 3 operator gates (seed selection, L3 mapping, confidence calibration)
- HL-09 strict, HL-10 strict, Bootstrap v1 First Activation Rule
- Refinement-006 conversational discipline (≤2–3 sentences per step, one question per gate, one recommendation never a menu, no pre-emptive caveats, Action Override preserved)

What changes is **when Gate A fires within the first turn**: after the search, never before.

# Implications

## CLAUDE.md update required

Add a 6th rule to the *Closed-Loop Conversational Discipline* subsection:

> 6. **Search before Gate A.** PubMed/source search runs silently before the first operator gate. Gate A presents only verified candidates (PMID + exact figure). Pre-search guessing is blocked.

## Decision-017 fourth amendment

Decision-017 has been amended three times (refinement-004, refinement-005, refinement-006). A fourth amendment notes refinement-007 turn-flow discipline, preserving prior amendments as historical record.

## Fresh-chat test protocol — Test 10-A scoring update

Test 10-A (power-user explicit Research Mode invocation) scoring rubric should add a turn-flow dimension:

- **PASS signal:** Gate A surfaces with a verified candidate (PMID + exact figure verbatim). One operator turn → one Gate A turn. No mid-flow corrections.
- **FAIL signal:** Gate A surfaces a pre-search guess. Operator confirms a candidate before the system has searched. Mid-flow "correction" required after actual search runs.

The 2026-05-04 ACSM Research Mode test result is now classified as PARTIAL on a third dimension: closed loop fired (refinement-004 PASS) with tight delivery (refinement-006 PASS) but with FAIL turn flow (Gate A before search).

## No structural changes

Refinement-007 does not change the closed loop's substance, the lane abstraction, the mode activation pattern, the Research Layer's grounding service, or any HL discipline. It tightens **first-turn sequencing** only.

# Action Status

**Resolved 2026-05-04.** Turn-flow rules locked. Tight pattern documented. Pre-search Gate A anti-pattern documented. Three follow-on edits queued.

**Follow-on tasks:**

1. Update CLAUDE.md — add 6th rule to Closed-Loop Conversational Discipline (search before Gate A)
2. Amend decision-017 (fourth time) — note refinement-007
3. Update fresh-chat test protocol — Test 10-A turn-flow scoring rubric

# Last Updated

2026-05-04 — initial refinement entry. Trigger: fresh-chat ACSM 2026 Research Mode test surfaced Gate A before search, producing wrong-path pre-search guess and mid-flow correction. Resolution: 4 turn-flow rules locked + tight/bloated patterns documented. Closed-loop substance (refinement-004) and conversational discipline (refinement-006) unchanged; first-turn sequencing tightened.
