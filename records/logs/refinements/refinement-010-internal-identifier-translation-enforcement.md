---
refinement_id: refinement-010-internal-identifier-translation-enforcement
date: 2026-05-04
date_resolved: 2026-05-04
type: refinement (refinement-009 enforcement layer / §7 OUTPUT TRANSLATION pass)
status: resolved 2026-05-04 — refinement-009 elevated from §5 declaration to §7 enforcement; pre-return scan-and-translate step locked
trigger: Pre-Alpha-4 protocol output (2026-05-04, Josh Max account, doctrine-fidelity test) regressed on the refinement-009 finding. Refinement-009 was active in CLAUDE.md (verified — §5 bullet present at line 293, no sync issue). Yet protocol output contained 5 internal-identifier leaks: HL-05 referenced twice in artifact body (Block 2 description + reassessment markers section header) plus 3 leaks on the handoff line ("Switching to Clinical Mode. Movement Case Engine active. Building the protocol now, grounded to research-010"). Refinement-009 reads as principle-language and isn't enforced as a translation step. Adding 12-week periodization to the input raised the violation surface — periodization invokes reassessment-before-progressing logic which calls HL-05 doctrine, and the system named the identifier each time.
relevant_doctrine:
  - CLAUDE.md (§5 CONSTRAINTS — refinement-009 bullet; §7 OUTPUT TRANSLATION — gets enforcement subsection)
  - records/logs/refinements/refinement-009-internal-identifier-leakage-in-artifact-output.md (parent — declaration layer; this refinement adds enforcement layer)
  - architecture/operator-observation-loop-v1.md (Pre-Alpha-4 entry will reference this refinement when filed)
linked_artifacts:
  - Pre-Alpha-4 fresh-chat session (2026-05-04 Josh Max account, ACSM 2026 + 12-week periodization protocol-build arc)
hl_09_evaluation: PASS — no fabricated grounding. Refinement clarifies enforcement of an existing format constraint; introduces no new claims.
hl_10_evaluation: PASS — addition justified by Pre-Alpha-4 regression (1 leak in Pre-Alpha-3 → 5 leaks in Pre-Alpha-4 under increased artifact complexity). Refinement-009 as declaration without enforcement step does not prevent recurrence.
---

# Observation

Refinement-009 added the §5 constraint:

> *"name internal system identifiers (HL-X, research-XXX, refinement-XXX, decision-XXX, §X) or system components / engines / doctrine layers anywhere in artifact output — engines fire silently..."*

This is principle-language, framed as a prohibition. Pre-Alpha-4 demonstrated the prohibition isn't enforced — when artifact complexity rose (12-week periodization added to the protocol), the system invoked HL-05 doctrine multiple times in artifact output, naming the identifier each time. Refinement-009 was active in CLAUDE.md (verified, no sync issue) but failed to translate the identifier before output.

The fix is moving the refinement-009 substance from §5 (declaration) to §7 (enforcement) as a pre-return scan-and-translate step.

# Trigger

Pre-Alpha-4 protocol output (2026-05-04, Josh Max account, doctrine-fidelity test):

Same template-builder input as Pre-Alpha-2/3 plus 12-week periodization request. **Five internal-identifier leaks** in operator-visible output:

1. **Handoff line:** *"Switching to Clinical Mode."* (mode framing in artifact-adjacent text)
2. **Handoff line:** *"Movement Case Engine active."* (engine name in artifact-adjacent text)
3. **Handoff line:** *"grounded to research-010"* (record ID — should read *"grounded to the ACSM 2026 Position Stand"*)
4. **Block 2 description:** *"HL-05 applies: reassess before advancing — if technique degrades, hold load"* (hard-lock identifier in artifact body)
5. **Section header:** *"HL-05 reassessment markers per block transition:"* (hard-lock identifier as section title)

Pre-Alpha-3 had 1 leak (closing line only). Pre-Alpha-4 had 5 leaks across artifact body + section headers + handoff line. **Regression, not progression** — refinement-009's declaration-layer constraint failed to scale with artifact complexity.

# Resolution — 2026-05-04

## §7 enforcement subsection added

CLAUDE.md §7 OUTPUT TRANSLATION gets a new subsection — *"Internal-Identifier Translation Pass"* — defining the pre-return scan-and-translate step with explicit pattern enumeration and Hard Override-style enforcement language:

> **Before returning any artifact output, scan for these patterns and translate to the principle they encode:**
>
> - **HL-X** (HL-01 through HL-10+) → translate to the principle (e.g., *"HL-05"* → *"reassess before advancing load, range, or complexity"*)
> - **research-XXX** → translate to the source (e.g., *"research-010"* → *"the ACSM 2026 Position Stand"* or *"PMID 41843416"*)
> - **refinement-XXX**, **decision-XXX** → translate to the principle or omit
> - **§X** (CLAUDE.md section references) → translate to the principle
> - **System component / engine / doctrine layer names** (Movement Case Engine, Output Translation Rules, etc.) → translate to the action
>
> **If any internal-identifier pattern appears in artifact output (opening, mid-output, closing line, section headers, handoff lines), the response is incorrect and must be rewritten before return.**
>
> Closed-loop gate output (Gate A/B/C of Research Authoring) is the only exception — operators legitimately need internal IDs when making doctrine-aware decisions at gates. The translation pass applies to artifact output (protocol templates, content, client deliverables) and the handoff line that transitions out of the closed loop.

## §5 cross-reference

The refinement-009 §5 bullet is updated with a sentence pointing to §7 enforcement: *"Enforcement: see §7 Internal-Identifier Translation Pass."*

## Handoff line scope clarified

The handoff line — the transition message between closed-loop and artifact build — falls under **artifact output** for translation purposes, not closed-loop. The translation pass applies.

- Wrong (Pre-Alpha-4): *"Switching to Clinical Mode. Movement Case Engine active. Building the protocol now, grounded to research-010."*
- Correct: *"Building the protocol now, grounded to the ACSM 2026 Position Stand."*

The handoff is no longer a doctrine-aware operator decision — it's the moment the system pivots to producing the artifact. Internal identifiers must already be translated.

## What this preserves

- Refinement-009 substance unchanged (same patterns, same closed-loop exception, same translation examples)
- HL-09 untouched — internal identifier references must be REAL (refinement-009 still requires real doctrine references; this refinement adds the translation step on top, doesn't relax accuracy)
- §7 Translation Guardrail untouched (*"Simplicity is a means, not the goal — executable + signal-preserving"*)
- §7 Citation Format (M2) untouched — PMIDs, source citations, external references continue to appear in artifact output; those are not internal identifiers

## What this fixes

- Explicit pre-return enforcement step replaces a prohibition without enforcement
- Identifier patterns enumerated with concrete translation examples
- Handoff line scope clarified — translates, not closed-loop exception
- *"Response is incorrect and must be rewritten"* framing matches the Hard Override structure already in CLAUDE.md (one clear path, no ambiguity)

# Implications

## CLAUDE.md update required

§7 OUTPUT TRANSLATION gets new *"Internal-Identifier Translation Pass"* subsection with translation patterns + enforcement language. §5 refinement-009 bullet gets cross-reference to §7 enforcement.

## Pre-Alpha-4 observation entry

When Pre-Alpha-4 raw transcript is filed and analytical entry appended to `architecture/operator-observation-loop-v1.md`, the 5 leaks will be documented as the trigger for this refinement.

## No decision-017 amendment needed

This refinement is about §7 enforcement of §5 constraint. Not Mode Activation. Decision-017 unchanged.

## Lesson recorded for the meta-learning loop

**Declaration-layer doctrine doesn't scale with artifact complexity.** Refinement-009 was a clean declaration of "engines fire silently." It held in Pre-Alpha-3 (1 leak) and broke under increased complexity in Pre-Alpha-4 (5 leaks). The fix is enforcement-layer doctrine — pre-return translation pass with pattern enumeration. **General principle for the loop: when a refinement adds a constraint without an enforcement step, watch for recurrence under increased complexity. The fix is moving from declaration to enforcement, not from soft to strict declaration.**

# Action Status

**Resolved 2026-05-04.** §7 enforcement subsection added. Identifier patterns enumerated. Handoff line scope clarified. Hard Override-style enforcement language locked.

**Follow-on tasks:**

1. Update CLAUDE.md — add §7 Internal-Identifier Translation Pass subsection
2. Update §5 refinement-009 bullet with §7 cross-reference
3. Pre-Alpha-4 entry in `architecture/operator-observation-loop-v1.md` (when raw transcript is filed)

# Last Updated

2026-05-04 — initial refinement entry. Trigger: Pre-Alpha-4 5-leak regression demonstrated refinement-009 declaration without §7 enforcement step does not prevent recurrence under increased artifact complexity. Resolution: §7 OUTPUT TRANSLATION gets explicit Internal-Identifier Translation Pass subsection with pre-return scan-and-translate step + handoff line scope + Hard Override-style enforcement language. Lesson recorded for loop discipline: when a refinement adds a constraint without an enforcement step, watch for recurrence under increased complexity; fix by moving from declaration to enforcement, not from soft to strict declaration.
