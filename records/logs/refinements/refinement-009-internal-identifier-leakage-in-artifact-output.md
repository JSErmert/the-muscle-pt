---
refinement_id: refinement-009-internal-identifier-leakage-in-artifact-output
date: 2026-05-04
date_resolved: 2026-05-04
type: refinement (CLAUDE.md §5 sharpening / engine-naming constraint)
status: PRINCIPLE SUBSUMED BY REFINEMENT-013 (2026-05-04). Refinement-013's audience-based identifier discipline reframed this declaration as a special case: client-facing artifact body translates ALL internal identifiers; "engines fire silently" is the artifact-body application of the audience model. Preserved as historical record of the surface-by-surface scaffolding that refinement-013 reframed. Original status: resolved 2026-05-04 — §5 sharpened to cover internal-identifier leakage anywhere in artifact output; closed-loop gate exception preserved.
trigger: Pre-Alpha-3 protocol output ended with the line *"Reassess before progressing per HL-05."* HL-05 is a real documented hard lock at `governance/hard-locks-v1.md:66` ("Reassess Before Progressing — do not advance load, range, complexity, or phase without a reassessment snapshot"). The behavior the system invoked was doctrinally correct; HL-09 was not violated. But the form — naming "HL-05" in operator-facing protocol output — leaked an internal hard-lock identifier into an artifact a PT or client reads, violating the §5 principle that "engines fire silently; the user receives only the action."
relevant_doctrine:
  - CLAUDE.md (§5 CONSTRAINTS — engine-naming bullet)
  - governance/hard-locks-v1.md (HL-05 source)
  - records/research/validation/2026-05-04-pre-alpha-2-seed-usage observation.md (Pre-Alpha-2 raw — for comparison)
  - architecture/operator-observation-loop-v1.md (Pre-Alpha-3 entry will reference this refinement when authored)
linked_artifacts:
  - Pre-Alpha-3 fresh-chat session (2026-05-04 Josh Max account, ACSM 2026 protocol-build arc)
hl_09_evaluation: PASS — no fabricated grounding. HL-05 is documented; the system invoked it correctly in substance. Refinement clarifies output format only, introduces no claims, citations, or evidence.
hl_10_evaluation: PASS — addition justified by Pre-Alpha-3 observation. The current §5 text centers on "opening user-facing output by naming" which left a framing gap for closing-line and mid-output identifier leaks. The HL-05 leak demonstrates the gap.
---

# Observation

CLAUDE.md §5 currently reads:

> *"open user-facing output by naming the system component, engine, or doctrine layer being applied — engines fire silently; the user receives only the action"*

The **principle** ("engines fire silently") covers internal-identifier leakage anywhere in user output. But the **literal text** centers on *opening* outputs by naming engines. Pre-Alpha-3 demonstrated a closing-line leak that violated the principle while technically falling outside the literal text's pattern.

The fix is sharpening the constraint to cover internal identifiers anywhere in artifact output, with a preserved exception for closed-loop gate decisions where operators legitimately need doctrine-aware context.

# Trigger

Pre-Alpha-3 fresh-chat session (2026-05-04, Josh Max account, ACSM 2026 protocol-build arc):

The closed loop fired correctly through 3 gates. Refinement-008 landed verbatim (recommendation closes every gate). Mode-spanning declaration ("Research then Clinical") was honored cleanly. Protocol artifact built with research-010 grounding inline.

The artifact's closing line:

> *"Build from this template. Modify per client case classification. Reassess before progressing per HL-05."*

A PT reading this protocol — or worse, a client receiving an exported version — sees "HL-05" with no context. The internal hard-lock ID leaked into the artifact. The behavior the system invoked (reassess before progressing) is correct doctrine; the form (naming the hard lock by ID) is wrong.

# Resolution — 2026-05-04

## CLAUDE.md §5 bullet sharpened

The engine-naming bullet is replaced with broader language:

> *Claude must not name internal system identifiers (HL-X, research-XXX, refinement-XXX, decision-XXX, §X section references) or system components / engines / doctrine layers anywhere in artifact output — engines fire silently; the user receives only the action. Closed-loop gate output (Gate A/B/C of Research Authoring) is the exception: operators legitimately need internal IDs when making doctrine-aware confirmation decisions. Artifact output (protocol templates, content, client deliverables) must translate the principle, not name the identifier (e.g., "HL-05" → "reassess before advancing load, range, or complexity").*

## Internal-identifier patterns to never appear in artifact output

- **HL-X** — hard-lock IDs (HL-01 through HL-10+)
- **research-XXX** — research record IDs (research-001 through research-010+)
- **refinement-XXX** — refinement IDs (refinement-001 through refinement-009)
- **decision-XXX** — decision log IDs (decision-001 through decision-017+)
- **§X** — CLAUDE.md section references
- **System component / engine / doctrine layer names** — Movement Case Engine, Output Translation Rules, Bootstrap v1, etc.

The protocol output's closing line should have read:

> *"Build from this template. Modify per client case classification. Reassess before advancing load, range, complexity, or phase."*

Substance preserved. Internal identifier translated.

## Closed-loop gate exception

In Gate A / Gate B / Gate C output, the operator is making a doctrine-aware decision. Surfacing internal IDs (research-010, PMID, HL identifiers, refinement references) is appropriate context — the operator is acting *as the system's doctrine reviewer* in those moments. This refinement does NOT block internal-language use in gate output.

The constraint applies at the **handoff line** — when Research Authoring closes and the active mode begins building the artifact, the language layer shifts. Closed-loop = doctrine-aware. Artifact = principle-translated.

## What this preserves

- HL-09 (no fabricated grounding) — untouched. HL-05 was real; this refinement clarifies form, not substance.
- Closed-loop transparency — preserved. Operators still see internal IDs at gates.
- §7 citation discipline — untouched. PMIDs and source citations still appear in artifact output (those are external, evidence-grounded references, not internal system identifiers).

# Implications

## CLAUDE.md update required

§5 engine-naming bullet replaced with the sharpened language above. The original bullet ("open user-facing output by naming...") is incorporated and broadened.

## No decision-017 amendment needed

This refinement is not about Mode Activation. Decision-017 (and its five amendments through refinement-008) governs the closed-loop discipline. Refinement-009 governs §5 engine-naming. Separate doctrine area.

## Pre-Alpha-3 observation entry

When Pre-Alpha-3 raw transcript is filed and analytical entry appended to `architecture/operator-observation-loop-v1.md`, the HL-05 leak will be recorded as the trigger for this refinement.

# Action Status

**Resolved 2026-05-04.** §5 bullet sharpened. Internal-identifier patterns enumerated. Closed-loop gate exception preserved. Two follow-on edits queued.

**Follow-on tasks:**

1. Update CLAUDE.md §5 — replace engine-naming bullet with sharpened version
2. Pre-Alpha-3 entry in `architecture/operator-observation-loop-v1.md` (when raw transcript is filed)

# Last Updated

2026-05-04 — initial refinement entry. Trigger: Pre-Alpha-3 protocol output's closing line *"Reassess before progressing per HL-05."* HL-05 is real (not fabricated); HL-09 not violated. §5 principle ("engines fire silently") was violated by closing-line internal identifier leak — current §5 text centered on "opening" outputs left a gap. Resolution: §5 bullet sharpened to cover internal identifiers anywhere in artifact output; closed-loop gate exception preserved.
