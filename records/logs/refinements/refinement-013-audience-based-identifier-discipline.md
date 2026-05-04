---
refinement_id: refinement-013-audience-based-identifier-discipline
date: 2026-05-04
date_resolved: 2026-05-04
type: refinement (audience-based model — corrects refinement-012 bypass-message over-translation + adds HL-X justification-framing scope)
status: resolved 2026-05-04 — audience-based identifier discipline locked; refinement-012 bypass-message record-ID rule SUPERSEDED (handoff mode-naming drop preserved); HL-X justification-framing translated; Pre-Alpha-8 fresh test pending as final Pre-Alpha pass
trigger: Pre-Alpha-7 fresh run produced clean artifact body (zero HL-X / engine names / research-XXX / refinement-XXX / decision-XXX / L1-L3 / lane names anywhere in the protocol deliverable). Refinement-012 substantially landed for the artifact. Two operator-facing residuals surfaced; operator correction reframed one of them. (1) Bypass message *"research-010 already locked at High confidence from prior session..."* — refinement-012's CORRECT example wrongly stripped record ID, which is the operator's storage pointer and provides legitimate lookup value when the operator asks "where is this from?" (2) *"Per HL-09 the deviation must be disclosed and the deviation itself is your call."* — HL-X used as adverbial justification framing in operator-facing prose; no lookup affordance for any reader, principle is the value.
relevant_doctrine:
  - CLAUDE.md (Action Override scope language restructured to audience-based; §5 internal-identifier bullet restructured; §7 Internal-Identifier Translation Pass restructured around audience model with Pre-Alpha-7 WRONG/CORRECT pair added and refinement-012 bypass-message CORRECT example corrected)
  - records/logs/refinements/refinement-009-internal-identifier-leakage-in-artifact-output.md (declaration layer — preserved)
  - records/logs/refinements/refinement-010-internal-identifier-translation-enforcement.md (§7 enforcement layer — preserved)
  - records/logs/refinements/refinement-011-action-override-translation-with-refusal-framing.md (Action Override placement + refusal framing + concrete examples — preserved; two-tier closed-loop exception reframed by refinement-013 as audience-based)
  - records/logs/refinements/refinement-012-bypass-message-and-handoff-final-cleanup.md (handoff mode-naming drop preserved; bypass-message record-ID translation rule SUPERSEDED by refinement-013)
  - architecture/operator-observation-loop-v1.md (Pre-Alpha-7 entry references this refinement)
linked_artifacts:
  - records/research/validation/2026-05-04-pre-alpha-7-seed-usage observation.md (Pre-Alpha-7 raw transcript — clean artifact body + refinement-012 over-translation surfaced + HL-X justification-framing new surface)
hl_09_evaluation: PASS — no fabricated grounding. Refinement reframes existing translation discipline; introduces no new grounding claims.
hl_10_evaluation: PASS — addition justified by Pre-Alpha-7 result + operator correction. Refinement-012's bypass-message record-ID translation was an over-translation that stripped legitimate operator value (storage pointer). New HL-X justification-framing surface uncovered. Audience-based model clarifies the principle that refinements 009-012 had been chasing surface-by-surface.
---

# Observation

Refinement-012 was scoped as the final Pre-Alpha refinement. Pre-Alpha-7 fresh run produced **clean artifact body** — every dominant Pre-Alpha-4/5 leak pattern was gone. Refinement-011's four-element bundle + refinement-012's handoff mode-naming drop both landed. Refinement-008's recommendation-closes-the-call held verbatim across the working-set decision surface (fourth consistent observation).

Two operator-facing residuals surfaced. Operator correction reframed one of them and exposed the principle that refinements 009-012 had been chasing surface-by-surface:

**Record IDs and HL-X are not the same class of identifier.**

- **research-XXX** is a *storage pointer* — operators legitimately need it to locate sources in their own system. Stripping it makes the system worse, not safer ("if the user asks where it's from," the record ID tells them).
- **HL-X** has *no lookup affordance for any reader* — it only resolves inside CLAUDE.md. The principle ("reassess before progressing") is the value, not the identifier.

The two surfaces:

1. **Bypass message** — *"research-010 already locked at High confidence from prior session (PMID 41843416, ACSM 2026 Position Stand). No new authoring needed."* Refinement-012 had treated this as a leak (record ID + test methodology terminology). Operator correction: *"shouldnt the id be surfaced though? what if the user asks where its from? i think the only acceptable one is the record id so the user knows where its stored."* **Refinement-012's CORRECT example was an over-translation.**

2. **HL-X justification framing** — *"Per HL-09 the deviation must be disclosed and the deviation itself is your call."* HL-X used adverbially in operator-facing prose, not as the subject of a confirmation question. **New surface refinements 009-012 didn't anticipate.**

# Trigger

Pre-Alpha-7 fresh-chat session (2026-05-04, Josh Max account). Same template-builder + 12-week periodization input as Pre-Alpha-4/5/6. System checked project knowledge first, found research-010 already locked, bypassed Research Authoring, presented working-set decision (3 ranked options with refinement-008 closing recommendation — landed verbatim), built protocol after operator picked option A.

**Artifact body**: CLEAN. Zero HL-X, engine names, research-XXX, refinement-XXX, decision-XXX, L1-L3, lane names, contract names anywhere in the protocol artifact. PMID 41843416 cited per §7 Citation Format. Modification Triggers, 12-week periodization, cue stack, split templates — all clean.

**Handoff line**: CLEAN. *"Locked. Building the protocol."* — refinement-012 mode-naming drop landed verbatim.

**Pre-decision operator-facing surfaces — 2 residuals (1 confirmed leak after correction, 1 reclassified)**:

> *"research-010 already locked at High confidence from prior session (PMID 41843416, ACSM 2026 Position Stand). No new authoring needed."*

> *"Per HL-09 the deviation must be disclosed and the deviation itself is your call."*

Operator correction on the first: the record ID is the storage pointer; refinement-012's translation was wrong to strip it. Reread under corrected doctrine: **bypass message is NOT a leak (record ID stays).**

Operator confirmation on the second: HL-X used as adverbial justification framing, no lookup affordance for any reader, principle is the value. **Confirmed leak.**

# Resolution — 2026-05-04

## Audience-based identifier discipline

The audience determines what translates. Identifier types divide by reader value, not by surface.

### Operator-facing surfaces

Includes: closed-loop gates (Gate A / Gate B / Gate C), bypass messages (system found existing record), system status messages, mode-transition messages, and any operator-facing prose where the operator is the reader (not a downstream client).

**KEEP** (operators legitimately need these):
- **research-XXX** — operator's storage pointer (locates the record in their system)
- **PMID** — verifiable external reference
- **Source names** — verifiable (e.g., *"ACSM 2026 Position Stand"*)
- **Gate naming** — *Gate A / Gate B / Gate C* (low semantic load — operators learn quickly)
- **HL-X when it is the SUBJECT of a confirmation question** — e.g., *"Lock under HL-09 strict?"* (the operator is acknowledging the specific hard-lock identification)

**TRANSLATE**:
- **HL-X used adverbially or as justification framing** — *"Per HL-X..."*, *"HL-X applies"*, *"Under HL-X..."*. No lookup affordance for any reader; the principle is the value.
- **refinement-XXX, decision-XXX, §X** — internal-only identifiers, no lookup affordance for operators.
- **Abstract architecture terminology** — engine names (Movement Case Engine), layer names (L1/L2/L3), architecture names (Decision Layer), contract names (Content Output Contract), lane names (Insight Lane / Script Lane / Exercise-to-Script Lane). Unfamiliar without doctrine onboarding.
- **Test methodology terminology** — *Pre-Alpha-N*, *validation session*, *authoring run* → *prior session*

### Client-facing artifact body

Includes: protocol templates, scripts, content delivered to end clients (the PT's clients).

**TRANSLATE everything** to readable principle. PMID + source name remain only as citation per §7 Citation Format.

## Pre-Alpha-7 corrections

**Bypass message — corrected from refinement-012**:

**WRONG (refinement-012 over-translation)**: *"Already grounded by the ACSM 2026 Position Stand from a prior session (PMID 41843416). Building the protocol now."* — strips research-010, which is the operator's storage pointer.

**CORRECT (refinement-013 audience-based)**: *"research-010 already locked from a prior session (PMID 41843416, ACSM 2026 Position Stand). Building the protocol now."* — keeps record ID (storage pointer), keeps PMID + source name (verifiable), translates *"Pre-Alpha sessions"* → *"a prior session"*, drops *"No new authoring needed"* in favor of the action.

**HL-X justification framing — new surface**:

**WRONG**: *"Per HL-09 the deviation must be disclosed and the deviation itself is your call."*

**CORRECT**: *"The deviation must be disclosed; the deviation itself is your call."*

## What this preserves

- Refinement-008 (recommendation closes the call) — unchanged; held verbatim in Pre-Alpha-7 working-set decision
- Refinement-009 (artifact-body identifier prohibition) — substantively unchanged; the audience model clarifies *why* (no value to client reader)
- Refinement-010 (§7 enforcement scan-and-translate) — unchanged
- Refinement-011 (Action Override placement, refusal framing, concrete WRONG/CORRECT examples) — unchanged; two-tier closed-loop exception reframed as audience-based
- Refinement-012 handoff mode-naming drop — preserved (Pre-Alpha-7 handoff *"Locked. Building the protocol."* landed verbatim)
- HL-09 untouched (real references still required when surfaced)
- Closed-loop substance (10 steps, 3 gates, doctrine-aware decision moments) — unchanged

## What this changes

- Refinement-011's two-tier closed-loop exception → reframed as audience-based (operator-facing vs. client-facing, not gate-vs-artifact). Specific HL-X allowance narrows to "subject of confirmation question" only; HL-X used adverbially as justification framing translates.
- Refinement-012's bypass-message CORRECT example → SUPERSEDED. New CORRECT keeps record ID.
- §7 Internal-Identifier Translation Pass restructured around the audience model.
- Action Override scope language refined to distinguish operator-facing from client-facing.

# Implications

## CLAUDE.md updates required

1. **Action Override bullet** — restructure scope language around audience model: client-facing artifact body translates everything; operator-facing surfaces translate HL-X-adverbial, refinement-XXX, decision-XXX, §X, architecture terminology, test methodology — but KEEP record IDs (research-XXX), PMID, source names, Gate A/B/C, HL-X-as-confirmation-subject.
2. **§5 internal-identifier bullet** — restructure to audience model. Cross-reference §7.
3. **§7 Internal-Identifier Translation Pass** — restructure WRONG/CORRECT examples around audience model. Add Pre-Alpha-7 HL-X justification-framing pair. Correct refinement-012's bypass-message CORRECT example. Reframe two-tier closed-loop exception as audience-based.

## Refinement-012 status update

Refinement-012's status note updated to record: handoff mode-naming drop preserved; bypass-message record-ID translation rule SUPERSEDED by refinement-013 (audience-based model — record ID is operator's storage pointer, keep at operator-facing surfaces).

## No decision-017 amendment needed

Not Mode Activation. Decision-017 unchanged.

## Pre-Alpha-7 entry in operator-observation-loop-v1

Pre-Alpha-7 entry filed concurrently with this refinement. Tracks: refinement-012 substantial landing for artifact deliverable; refinement-012 bypass-message over-translation surfaced via operator correction; HL-X justification-framing new surface closed; Pre-Alpha-8 scoped as final Pre-Alpha pass.

## Pre-Alpha-8 milestone path

Pre-Alpha-8 = final Pre-Alpha pass per operator authorization (*"this will be the last pre-alpha pass"*). Fresh-chat run with same input under refinement-013 doctrine. Expected output:

- Artifact body: clean (refinements 009/010/011/012/013 cumulative discipline)
- Handoff line: clean (refinement-012 mode-naming drop preserved)
- Bypass message: keeps research-XXX storage pointer; *"prior session"* terminology; drops *"No new authoring needed"*
- Justification framing: principle-language not HL-X

If clean → **Alpha locks**. Handoff to founder Zach for 1-week production testing while operator develops Carousel Mode → Beta version.

If leaks persist on the residual surface → model ceiling acknowledged; operator-side review for that surface only.

# Loop discipline lesson

When a refinement adds friction (over-translation that strips legitimate operator value), the underlying rule may need reframing rather than extension. Refinements 009-012 had been chasing surface-by-surface rules (artifact body → handoff line → bypass message). Refinement-013's audience-based reframe is what the principle should have been from the start: identifier discipline divides by **reader value**, not by **surface location**.

Future identifier-discipline questions resolve against audience, not surface.

# Action Status

**Resolved 2026-05-04.** Audience-based identifier discipline locked. Refinement-012 bypass-message rule SUPERSEDED (handoff mode-naming drop preserved). HL-X justification-framing scope added. Pre-Alpha cycle concludes with Pre-Alpha-8 fresh test as final pass.

**Follow-on tasks:**

1. Update CLAUDE.md Action Override — audience-based scope language
2. Update CLAUDE.md §5 — audience-based bullet
3. Update CLAUDE.md §7 — restructure WRONG/CORRECT examples around audience model; add Pre-Alpha-7 HL-X justification-framing pair; correct refinement-012 bypass-message CORRECT example; reframe closed-loop exception as audience-based
4. Update refinement-012 status note — bypass-message record-ID rule SUPERSEDED; handoff mode-naming drop preserved
5. Pre-Alpha-7 entry in `architecture/operator-observation-loop-v1.md`
6. Run Pre-Alpha-8 fresh test — clean result locks Alpha; persistent residual leaks shift to operator-side review for that surface

# Last Updated

2026-05-04 — initial refinement entry. Trigger: Pre-Alpha-7 produced clean artifact body but operator correction surfaced refinement-012 over-translation (bypass-message stripped record ID, which is the operator's storage pointer) plus new HL-X justification-framing surface. Resolution: audience-based identifier discipline replaces surface-based model. Operator-facing surfaces keep record IDs / PMID / source names / Gate naming / HL-X-as-confirmation-subject; translate HL-X-adverbial / refinement-XXX / decision-XXX / §X / architecture terminology / test methodology. Client-facing artifact body translates everything. Pre-Alpha-8 fresh test = final Pre-Alpha pass; result determines Alpha lock.
