---
refinement_id: refinement-008-menu-discipline-recommendation-closes-the-call
date: 2026-05-04
date_resolved: 2026-05-04
type: refinement (menu discipline / rule 3 sharpening)
status: resolved 2026-05-04 — recommendation-closes-the-call locked; bare menus blocked; appropriate multi-way menus preserved
trigger: Pre-Alpha-2 fresh-chat session (2026-05-04 Zach machine, ACSM 2026 protocol-build arc) surfaced multi-way operator decisions where the system listed candidates with rationale per option but did not state an explicit recommendation. The working-set prescription turn (Keep 1 max-effort / Match ACSM 2-3 sets / Hybrid) is the canonical example. Initial reading of refinement-006 rule 3 ("never a menu") was over-strict — the menus surfaced legitimate multi-way trade-offs that yes/no would have hidden. The actual rule being sought is "recommendation closes the call," not "no menus."
relevant_doctrine:
  - CLAUDE.md (§2 Closed-Loop Conversational Discipline rule 3)
  - records/logs/refinements/refinement-006-closed-loop-conversational-discipline.md (rule being sharpened)
  - records/logs/refinements/refinement-007-closed-loop-turn-flow-search-before-gate-a.md (sibling)
  - records/logs/decisions/decision-017-mode-activation-pattern.md (fifth amendment will reference this refinement)
linked_artifacts:
  - architecture/operator-observation-loop-v1.md (Pre-Alpha-2 entry will reference this refinement when raw transcript is filed)
hl_09_evaluation: PASS — no fabricated grounding. Refinement clarifies output format discipline; introduces no claims, citations, or evidence.
hl_10_evaluation: PASS — addition justified by Pre-Alpha-2 observation. Over-strict reading of "never a menu" produced bad UX (oversimplifying multi-way clinical decisions to yes/no, losing information operators need). Sharpened rule preserves operator agency + system intelligence + cognitive-load-appropriateness for the PT operator surface.
---

# Observation

Refinement-006 rule 3 reads:

> *"One recommendation at every gate, never a menu. When multiple candidates exist, name them ranked but always state the recommended pick."*

Two clauses, partially contradictory:

- *"never a menu"* — strict ban
- *"when multiple candidates exist, rank them and recommend"* — multi-way support

Pre-Alpha-2 surfaced the contradiction. The system encountered legitimate multi-way operator decisions where reducing to yes/no would lose information the operator needs. It surfaced menus correctly. But it failed to close each menu with an explicit recommendation.

The actual discipline being sought is **"recommendation closes the call"** — not *"no menus."*

# Trigger

Pre-Alpha-2 (2026-05-04 Zach machine, ACSM 2026 protocol-build arc):

## Working-set prescription decision — canonical FAIL

After research-010 locked, system surfaced the deviation between operator's protocol spec and ACSM's strength prescription:

> *Working set prescription?*
> *1. Keep 1 max-effort set (your spec, deviates from ACSM)*
> *2. Match ACSM: 2-3 working sets @ ≥80% 1RM*
> *3. 1 max-effort set + 1 back-off set (hybrid)*

Three options. Rationale per option. **No explicit recommendation.** The operator had to choose without the system's call.

## Grounding-path decision — softer FAIL

Earlier in the same chat, after Clinical Mode locked:

> *Grounding path?*
> *1. Build now, disclose ungrounded ACSM claims*
> *2. Research Authoring first, then build*

Two options framed as a real time/quality trade-off. The 2-path framing surfaced the trade-off informatively — yes/no per refinement-005's literal Research Authoring Prompt spec would have hidden the cost of grounding. But the system did not state which path it recommended.

## Operator framing

Josh, after I initially miscounted the violations as "4× menu pattern":

> *"the menus weren't too complex for a PT. They were appropriately rich. The system just didn't take the call within them."*

Operator is correct. The fix is to require the recommendation, not delete the menus.

# Resolution — 2026-05-04

## Rule sharpened

Refinement-006 rule 3 is restated:

> **3. Recommendation closes every gate.** When the choice space is genuinely multi-way and each option carries distinct downstream implications, surface the options ranked — then close with *"Recommend X because Y. Confirm or override."* The recommendation is the last line of the gate output. Bare menus without the closing recommendation are the violation, not menus per se. Yes/no decisions stay yes/no with the recommended path implicit in the asking.
>
> **Scope:** applies to closed-loop gates AND mid-mode multi-way operator decisions in any mode.

## Tight pattern (correct)

Multi-way decision example:

> *Working set prescription?*
>
> *1. Keep 1 max-effort (your spec, deviates from ACSM)*
> *2. Match ACSM: 2-3 working sets @ ≥80% 1RM*
> *3. 1 max-effort + 1 back-off (hybrid)*
>
> *Recommend hybrid — preserves your max-effort intent, satisfies ACSM 2-set floor, fits 1-hour budget. Confirm or override.*

The closing line takes the call. The operator can confirm or override with full context.

Yes/no decision example (unchanged from refinement-005 spec):

> *Want to ground this with a research record? Closed loop runs in 10 steps with 3 operator gates.*

Yes/no questions stay yes/no. The recommendation is implicit in the asking (the system asking = recommendation to act).

## Bloated anti-pattern (incorrect)

Multi-way decision without closing recommendation:

> *Working set prescription?*
>
> *1. Keep 1 max-effort*
> *2. Match ACSM*
> *3. Hybrid*
>
> *[no recommendation — operator must choose without system's call]*

**Never produce this pattern.** The Pre-Alpha-2 working-set turn is the canonical FAIL example for refinement-008.

## What this rule does NOT cover

Decision-criteria for downstream operator-side use are **not** menus. Example from Pre-Alpha-2's protocol output:

> *HIIT (10 min) — use on neural-light days or when total session time is the constraint.*
> *Moderate (20 min) — use when client has aerobic deficit, recovery-day pairing, or when RT was ≤30 min.*

This is template content describing conditional logic for the operator's downstream client adaptation, not an operator-choice menu requiring a system recommendation. Templates legitimately contain conditional rules. Refinement-008 does not apply here.

## What this preserves

Refinement-006's substance:
- Rule 1 (≤2–3 sentences per step) — unchanged
- Rule 2 (one question per gate) — unchanged
- Rule 4 (no pre-emptive caveats) — unchanged
- Rule 5 (Action Override) — unchanged
- Rule 6 (search before Gate A, refinement-007) — unchanged

What changes is rule 3's framing — the ban shifts from *"menus"* to *"bare menus without the closing recommendation."*

## What this fixes

- System can surface legitimate multi-way trade-offs that yes/no would hide
- Operator agency preserved (recommendation is a recommendation, not a forced choice)
- System still takes the call — the recommendation is the last line; operator overrides if they disagree
- Cognitive load remains PT-appropriate (ranked options + clear recommendation)
- Action Override holds — there is one clear path forward (the recommended one); the menu just makes the trade-off visible

# Implications

## CLAUDE.md update required

§2 Closed-Loop Conversational Discipline rule 3 sharpened per the resolution above. Scope language added: rule applies to closed-loop gates AND mid-mode multi-way operator decisions in any mode (not just closed-loop scope). The bloated anti-pattern list in the same subsection updated: "unranked menus of 4+ candidates" replaced with "bare menus without the closing recommendation."

## Decision-017 fifth amendment

Decision-017 has been amended four times (refinements 004, 005, 006, 007). A fifth amendment notes refinement-008 menu discipline.

## Pre-Alpha-2 entry in operator observation loop

When the Pre-Alpha-2 raw transcript is filed at `records/research/validation/2026-05-04-pre-alpha-2-zach-usage-observation.md`, the analytical layer in `architecture/operator-observation-loop-v1.md` will add a `## Pre-Alpha-2 — Analysis` section. The working-set prescription turn will be cited there as the canonical FAIL example for refinement-008.

## Lesson for the meta-learning loop discipline itself

In the Pre-Alpha-2 chat, I (the agent) initially miscounted the violations as "4× menu pattern across the chat" — overstating the pattern by lumping doctrine-compliant cases (mode-pick under §2 ambiguity behavior; decision-criteria in template content) with genuine violations. Josh pushed back; honest reassessment showed 1 hard violation + 1 soft case + 2 misclassifications.

This is exactly the contamination the single-observation rule is supposed to prevent — manufacturing repetition by lumping unlike instances. **Pattern claims must be specific about what repeated, not summary counts.** Adding this lesson to the loop discipline as guidance for future analytical entries.

# Action Status

**Resolved 2026-05-04.** Rule sharpened. Scope clarified. Tight pattern + bloated anti-pattern documented. Three follow-on edits queued.

**Follow-on tasks:**

1. Update CLAUDE.md — sharpen §2 rule 3, add scope language, update bloated anti-pattern list
2. Amend decision-017 (fifth time) — note refinement-008
3. Pre-Alpha-2 entry in `architecture/operator-observation-loop-v1.md` when raw transcript is filed

# Last Updated

2026-05-04 — initial refinement entry. Trigger: Pre-Alpha-2 working-set prescription turn produced bare-menu pattern. Resolution: rule 3 sharpened from "never a menu" to "recommendation closes every gate." Refinement-006 substance preserved; what changes is rule 3's framing. Lesson on pattern-claim specificity added to meta-learning loop discipline.
