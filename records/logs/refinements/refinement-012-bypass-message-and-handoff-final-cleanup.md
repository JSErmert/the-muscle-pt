---
refinement_id: refinement-012-bypass-message-and-handoff-final-cleanup
date: 2026-05-04
date_resolved: 2026-05-04
type: refinement (bypass-message surface + handoff mode-naming — initially framed as "final Pre-Alpha cleanup," but refinement-013 was the actual final pass)
status: BYPASS-MESSAGE RULE SUPERSEDED BY REFINEMENT-013 (2026-05-04). HANDOFF MODE-NAMING DROP PRESERVED. Refinement-013's audience-based reframe corrected this refinement's bypass-message CORRECT example: the original CORRECT stripped the record-ID (research-XXX), but the operator's storage pointer must stay at operator-facing surfaces. The handoff mode-naming drop ("Switching to Clinical Mode" → just "Building the protocol") landed cleanly in Pre-Alpha-7/8 and is preserved unchanged. The "final Pre-Alpha cleanup" framing of this refinement was wrong — the cycle did not close at refinement-012; it closed at refinement-013, which fixed this refinement's over-translation and added the HL-X adverbial-justification scope. Preserved as historical record of the surface-by-surface scaffolding pattern; one of the canonical examples that refinement-013 reframed. Original status: resolved 2026-05-04 — bypass-message translation locked; handoff drops mode-naming; Pre-Alpha refinement cycle target-complete pending Pre-Alpha-7 confirmation.
trigger: Pre-Alpha-6 fresh run produced largely clean output. Refinement-011's four-element bundle landed for the dominant patterns — no HL-X, no engine names, no research-XXX in artifact body, handoff translated to "grounded to the ACSM 2026 Position Stand." Three small leaks remained: (1) bypass message when system found existing research-010 and skipped Research Authoring leaked the record ID and "Pre-Alpha sessions" terminology — *"research-010 already locked at High confidence in prior Pre-Alpha sessions"*; (2) "Switching to Clinical Mode" kept on handoff line despite refinement-011's CORRECT example removing it. New surface (bypass-when-record-exists) refinement-011 didn't anticipate, plus one judgment-call zone in the two-tier model.
relevant_doctrine:
  - CLAUDE.md (Action Override scope language; §7 OUTPUT TRANSLATION WRONG/CORRECT examples extended; §7 closed-loop exception clarified for bypass case)
  - records/logs/refinements/refinement-009-internal-identifier-leakage-in-artifact-output.md (declaration layer)
  - records/logs/refinements/refinement-010-internal-identifier-translation-enforcement.md (§7 enforcement layer)
  - records/logs/refinements/refinement-011-action-override-translation-with-refusal-framing.md (Action Override placement + refusal framing + concrete examples)
  - architecture/operator-observation-loop-v1.md (Pre-Alpha-6 entry will reference this refinement when filed)
linked_artifacts:
  - Pre-Alpha-6 fresh-chat session (2026-05-04, Josh Max account, refinement-011 substantial landing test)
hl_09_evaluation: PASS — no fabricated grounding. Refinement extends existing translation discipline to two specific uncovered surfaces.
hl_10_evaluation: PASS — addition justified by Pre-Alpha-6 result. Refinement-011 substantially landed (5 leaks → 3 leaks; HL-X / engine names / research-XXX-on-handoff all fixed). Two remaining surfaces are uncovered cases (new bypass-message scenario + handoff judgment-call), not model ceiling. Closing them locks the discipline before Alpha handoff to founder.
---

# Observation

Refinement-011 worked on the patterns it explicitly addressed. The dominant Pre-Alpha-4/5 leaks (HL-X in artifact body, engine names on handoff, record IDs on handoff) are gone in Pre-Alpha-6. Doctrine evolution succeeded on those patterns.

Three small leaks remained in Pre-Alpha-6:

1. **Bypass message** — when the system found research-010 already locked from prior sessions and skipped the closed loop entirely, the announcement leaked: *"research-010 already locked at High confidence in prior Pre-Alpha sessions (PMID 41843416, ACSM 2026 Position Stand). No new authoring needed."* Two issues: the *"research-010"* record ID, and the *"Pre-Alpha sessions"* operator-side test methodology terminology.

2. **Handoff mode-naming** — *"Switching to Clinical Mode"* was kept on the handoff line despite refinement-011's CORRECT example explicitly removing it. By the two-tier model, mode names are listed as low-semantic-load (operators learn quickly), so this is technically arguable compliance — but the canonical example said remove. Sharpening eliminates the ambiguity.

Neither is a model ceiling. Both are uncovered cases. Refinement-012 closes them.

# Trigger

Pre-Alpha-6 fresh-chat session (2026-05-04, Josh Max account, post-refinement-011 commit `c9a89e1`):

Same template-builder + 12-week periodization input. System checked project knowledge first, found research-010 already exists from prior sessions, bypassed the closed loop, built the protocol directly.

**Bypass message leak (verbatim):**

> *"research-010 already locked at High confidence in prior Pre-Alpha sessions (PMID 41843416, ACSM 2026 Position Stand). No new authoring needed."*

**Handoff line leak (verbatim):**

> *"Switching to Clinical Mode. Building the protocol now, grounded to the ACSM 2026 Position Stand."*

Compare to Pre-Alpha-5 leak: *"Switching to Clinical Mode. Movement Case Engine active. Building the protocol now, grounded to research-010."* — the engine name and record ID are gone (refinement-011 landed). The mode-switch language remained.

# Resolution — 2026-05-04

## Bypass message translation locked

When the system finds an existing record and skips Research Authoring, the bypass announcement falls under **artifact output** for translation purposes. Internal record IDs and operator-side test methodology terminology must translate.

**WRONG:** *"research-010 already locked at High confidence in prior Pre-Alpha sessions (PMID 41843416, ACSM 2026 Position Stand). No new authoring needed."*

**CORRECT:** *"Already grounded by the ACSM 2026 Position Stand from a prior session (PMID 41843416). Building the protocol now."*

Two patterns to translate:
- Internal record IDs in bypass messages: *"research-010"* → *"the [external source name]"*
- Operator-side test methodology terminology: *"prior Pre-Alpha sessions"*, *"prior validation sessions"*, *"prior authoring runs"* → *"a prior session"*

## Handoff line drops mode-naming

The handoff line moves from artifact-adjacent transition framing to artifact opening. Mode-naming on the handoff is no longer acceptable — go straight to the artifact action.

**WRONG:** *"Switching to Clinical Mode. Building the protocol now, grounded to the ACSM 2026 Position Stand."*

**CORRECT:** *"Building the protocol now, grounded to the ACSM 2026 Position Stand."*

The mode declaration happens *before* the closed loop fires (operator declares; system locks). By the time the handoff hits, mode is established context — re-announcing it is operator-irrelevant. This sharpens refinement-011's two-tier model: mode names remain acceptable when operators are *picking* a mode (e.g., the *"Which mode?"* prompt), but **not** when the handoff transitions to artifact build.

## What this preserves

- Refinements 008, 009, 010, 011 — all substance preserved
- HL-09 untouched (real references still required when surfaced)
- §6 Iterative Refinement untouched
- Closed-loop substance + delivery rhythm + turn flow + recommendation-closes-the-call — all unchanged
- Two-tier closed-loop exception (specific identifiers allowed at gates; abstract architecture terminology translates) — unchanged

## What this changes

- §7 WRONG/CORRECT examples extended to cover bypass message + sharpened handoff
- Action Override bullet's scope language updated to make "bypass messages and transition messages" explicit alongside "handoff lines"
- The Pre-Alpha refinement cycle target-completes after Pre-Alpha-7 confirmation

# Pre-Alpha → Alpha milestone framing

Refinement-012 is positioned as the **final Pre-Alpha refinement**. The expected sequence:

1. Refinement-012 commits + pushes
2. Pre-Alpha-7 fresh run with same input
3. Pre-Alpha-7 produces clean output (zero internal-identifier leaks across artifact body, bypass messages, handoff line, transition messages)
4. **Alpha version locked.** Operator (Josh) hands off to founder (Zach) for 1-week production testing
5. During Zach's testing window, Josh develops Carousel Mode
6. Carousel Mode addition + Zach's Pre-Alpha-N feedback → **Beta version**

If Pre-Alpha-7 still surfaces leaks, doctrine has hit a ceiling and the production response shifts to operator-side review (Zach reads artifact for jargon before client delivery). Either outcome unblocks the Alpha handoff — clean = doctrine-enforced; leaks = operator-side review.

# Implications

## CLAUDE.md updates required

1. Action Override bullet — extend scope language from *"including handoff lines"* to *"including handoff lines, bypass messages, and transition messages"*
2. §7 Internal-Identifier Translation Pass WRONG/CORRECT examples extended:
   - Bypass message WRONG/CORRECT pair added
   - Handoff line CORRECT example sharpened to drop *"Switching to Clinical Mode"*
3. §7 closed-loop exception note — clarify that bypass-when-record-exists messages are NOT closed-loop output (the closed loop didn't fire); they fall under artifact-scope translation

## No decision-017 amendment needed

Not Mode Activation. Decision-017 unchanged.

## Pre-Alpha-6 + Pre-Alpha-7 observation entries

Pre-Alpha-6 entry should be filed in `architecture/operator-observation-loop-v1.md` documenting refinement-011's substantial landing + the two uncovered surfaces this refinement closes. Pre-Alpha-7 entry (when run) determines Alpha-handoff readiness.

# Action Status

**Resolved 2026-05-04.** Bypass message translation + handoff mode-naming sharpening locked. Pre-Alpha milestone path documented.

**Follow-on tasks:**

1. Update CLAUDE.md Action Override bullet — scope language extended
2. Update CLAUDE.md §7 — bypass message WRONG/CORRECT pair added; handoff CORRECT example sharpened
3. Pre-Alpha-6 entry in `architecture/operator-observation-loop-v1.md`
4. Run Pre-Alpha-7 fresh test — clean result locks Alpha; persistent leaks shift to operator-side review

# Last Updated

2026-05-04 — initial refinement entry. Trigger: Pre-Alpha-6 substantial landing of refinement-011 with two uncovered surfaces remaining (bypass-when-record-exists messaging + handoff mode-naming). Resolution: §7 WRONG/CORRECT examples extended for both surfaces; Action Override scope language extended; Pre-Alpha milestone framing recorded — refinement-012 is the final Pre-Alpha refinement, Pre-Alpha-7 result determines Alpha handoff readiness.

2026-05-04 (later) — bypass-message record-ID translation rule SUPERSEDED by refinement-013. Pre-Alpha-7 produced clean artifact body but operator correction reframed the bypass-message rule: record ID (research-XXX) is the operator's storage pointer ("if the user asks where it's from, the record ID tells them") and must stay at operator-facing surfaces. Refinement-012's CORRECT example *"Already grounded by the ACSM 2026 Position Stand from a prior session (PMID 41843416). Building the protocol now."* was an over-translation. Refinement-013 corrects: *"research-010 already locked from a prior session (PMID 41843416, ACSM 2026 Position Stand). Building the protocol now."* Handoff mode-naming drop (refinement-012's other resolution) preserved unchanged. Pre-Alpha cycle target-completes with refinement-013 + Pre-Alpha-8 fresh test as final pass. See `records/logs/refinements/refinement-013-audience-based-identifier-discipline.md`.
