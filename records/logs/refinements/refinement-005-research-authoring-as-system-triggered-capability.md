---
refinement_id: refinement-005-research-authoring-as-system-triggered-capability
date: 2026-05-04
date_resolved: 2026-05-04
type: refinement (architectural simplification — operator-facing mode surface)
status: resolved 2026-05-04 — Research Mode retired from operator-facing primary surface; Research Authoring promoted to system-triggered capability with prompt-then-loop discipline; explicit power-user invocation preserved
trigger: 2026-05-04 operator architectural review during Zach handoff preparation. Operator recognized that the 6-mode operator-facing surface (decision-017 + refinement-004) creates confusion for daily-use operators (Zach) — 1 mode is deferred (Carousel), 1 mode is rarely-needed and mostly Josh-side (Research). Operator proposed embedding Research Mode into Clinical Mode; refined recommendation broadens to system-triggered capability available from any active mode when gaps surface.
relevant_doctrine:
  - records/logs/decisions/decision-017-mode-activation-pattern.md (parent decision being amended for the second time)
  - records/logs/refinements/refinement-004-research-layer-vs-authoring-mode-correction.md (parent refinement — established Layer-vs-Authoring separation; this refinement builds on it)
  - records/logs/decisions/decision-016-lane-abstraction-for-content-production.md (lane abstraction — unaffected)
  - CLAUDE.md (Mode Activation table requires another correction)
  - systems/intelligence/research-layer-bootstrap-v1.md (3-layer structure + First Activation Rule — orchestrated by capability, unchanged)
  - systems/intelligence/research-query-layer-v1.md (no abstract research; real input source — unchanged)
linked_artifacts:
  - records/research/queries/query-009-stretch-mediated-hypertrophy.md (cross-mode reference gap — example of capability triggering from Script Lane reference, not Clinical case)
  - records/research/captured/research-009-stretch-mediated-hypertrophy-regional-effects.md (first formal closed-loop execution under refinement-004; under refinement-005 the same closed loop runs inline within whichever mode surfaces the gap)
  - records/research/validation/2026-05-02-fresh-chat-test-protocol.md (Test 10 baseline requires another correction)
hl_09_evaluation: PASS — preserves no-fabricated-grounding discipline. Tightens disclosure discipline by making "operator declined to ground" an explicit path that triggers HL-09 disclosure (e.g., "I'm not grounding that piece from what I have right now") rather than silently ungrounded output. Three-gate operator-in-the-loop discipline preserved; never-auto-fire rule explicit.
hl_10_evaluation: PASS — refinement is operator-facing surface simplification, not capability expansion. The 10-step closed loop is unchanged. The 3 operator gates are unchanged. The Research Layer is unchanged. What changes is the activation pattern (system-triggered prompt vs. operator-declared mode). Documented current need: the Zach handoff requires a clean operator surface; the 6-mode list with one deferred and one rarely-used was creating documented confusion.
---

# Observation

Refinement-004 (2026-05-03) corrected the layer-vs-mode collision in decision-017 by separating the always-on **Research Layer** (passive grounding service) from the **Research Authoring Mode** (active 10-step closed loop with 3 operator gates).

That correction was right architecturally but **leaves a usability problem in the operator-facing mode surface**. The current Mode Activation table presents 6 modes:

1. Clinical Mode
2. Insight Mode
3. Script Mode
4. Carousel Mode (deferred)
5. Research Authoring Mode (rarely-needed by daily-use operators; mostly Josh-side)
6. Business Mode

For Zach's daily-use surface, this means **2 of 6 modes are not for him** — Carousel is deferred, and Research Authoring he basically never uses. A clean operator-facing surface would not include modes the operator doesn't use.

Additionally, **Research Authoring is genuinely cross-mode**, not a sibling to Clinical / Insight / Script / Business. Gaps that need authoring surface from inside other modes — research-009 (stretch-mediated hypertrophy) was triggered by a **Script Lane reference**, not by Clinical case work. Embedding Research Authoring solely in Clinical Mode (one operator's first instinct) would lose the cross-mode reality.

# Trigger

2026-05-04 operator architectural review during Zach handoff preparation. After authoring the operator-facing brief for Zach, operator observed that Research Mode appearing in the daily-use mode list created confusion ("Are you telling me research mode isn't required? shouldn't it be removed so that research mode is fully embedded into clinical mode since that is the mode that truly needs it?").

The observation correctly identified the surface-clutter problem. The proposed fix (embed in Clinical) was refined: Research Authoring is a **cross-mode capability**, not a Clinical-specific need. Generalize the embedding rather than narrow it.

# Resolution — 2026-05-04

## Architecture correction

| Concept | Type | Definition | Activation |
|---|---|---|---|
| **Research Layer** | Always-on passive service | Provides grounding citations to other modes when significantly informative per CLAUDE.md §7. | Implicit. No operator action required. *(Unchanged from refinement-004.)* |
| **Research Authoring** | System-triggered capability | Executes the full 10-step closed-loop authoring of new research records: gap → query → PubMed search → verification → 3-layer record → index → cross-record implications. Three operator-in-the-loop confirmation gates preserved. | **Prompt-driven.** When the active mode encounters a grounding gap, system prompts operator: *"Want to ground this with a research record?"* Operator confirms → loop fires inline within the active mode session. Operator declines → active mode continues with HL-09 disclosed ungrounded claim. |
| **Research Mode (explicit, power-user)** | Explicit operator command, preserved | Same closed loop, but invoked proactively rather than reactively. For when Josh wants to add a record before any gap surfaces. | Explicit operator command (preserved as alias). Lives in power-user reference, not Zach's daily mode list. |

The **discipline** of Research Authoring is unchanged from refinement-004. The 10 steps and 3 gates are unchanged. What changes is the **activation pattern**: from "operator declares Research Mode" to "system prompts when gaps surface; operator authorizes; closed loop fires inline."

## Trigger conditions for the system prompt

The system prompts for Research Authoring only when **all** of the following are true:

1. **The active mode encounters a claim that needs grounding** — significantly informative under CLAUDE.md §7, meaning the claim materially shapes the recommendation (not common-knowledge anatomy/kinesiology, not locked-phrase or convention, not heuristic prescription numbers).
2. **No existing record covers it adequately** — either no record exists OR an existing record is insufficient for this specific claim (e.g., research-009 covers stretch-mediated hypertrophy generally but a specific volume claim may need different grounding).
3. **The operator hasn't already declined for this gap in the current session** — once declined, the gap stays declined for the session; operator can re-trigger explicitly later.

The system does **not** prompt when:

- A record exists and adequately grounds the claim → system just surfaces the citation
- The claim is common knowledge per §7
- The claim is part of locked phrasing or convention (lane prescription numbers are heuristic, not cited)
- The operator declined for this gap earlier in the session

## Operator response paths

When the prompt fires:

- **Operator confirms** → 10-step closed loop fires inline within the active mode. 3 gates pause for operator confirmation at seed selection (Gate A), L3 mapping review (Gate B), confidence calibration (Gate C). Once locked, new record propagates to all future modes via the Research Layer.
- **Operator declines** → Active mode continues. The ungrounded claim is disclosed via HL-09 — same pattern as the TMJ referral disclosure in Test 1 (*"I'm not grounding that piece from what I have right now."*).

## Never auto-fires

The system **never** invokes the closed loop without explicit operator authorization. The 3 operator gates exist precisely to preserve operator agency. Auto-firing would:
- Violate the 3-gate discipline
- Risk authoring records the operator doesn't want
- Burn closed-loop cycles on gaps the operator is fine leaving disclosed
- Reduce operator agency

The prompt-then-fire pattern preserves the discipline.

## Power-user explicit invocation preserved

Josh (or any power user) can still invoke Research Authoring proactively by typing **"Research Mode"** explicitly — for cases where the operator wants to add a record before any gap surfaces during active mode work (e.g., closeout flag triggered authoring of research-008; M2 acceleration sprint authored research-001 through 005 + 008 proactively).

This explicit invocation lives in a **power-user reference**, not in Zach's primary mode list.

# Implications

## CLAUDE.md update required (second time)

Mode Activation table reduces to **5 modes + 1 deferred**:

| Mode command | Activates |
|---|---|
| **Clinical Mode** | Movement Case Engine. Research Layer auto-grounds; Research Authoring prompts when gap surfaces. |
| **Insight Mode** | Content Output Contract v1 (5 buckets, master framework). Research Layer auto-grounds; Research Authoring prompts when gap surfaces. |
| **Script Mode** *(alias: Exercise-to-Script Mode)* | Exercise-to-Script Lane Spec v1 + Shared Assets v1. Research Layer auto-grounds; Research Authoring prompts when gap surfaces. |
| **Carousel Mode** | Replies: "deferred — no active doctrine. Use Insight Mode or Script Mode for now." |
| **Business Mode** *(alias: Decision Mode)* | Governing Logic + Hard Locks + Prioritization + Queue Engine. Research Layer auto-grounds; Research Authoring prompts when gap surfaces. |

A **Power-User Reference** subsection added below the table notes the explicit *"Research Mode"* command for proactive authoring (Josh-side).

A **Research Authoring Prompt** subsection added describes the prompt-then-loop trigger conditions and operator response paths.

## Decision-017 amendment required (second time)

Decision-017 was already amended once (2026-05-03 by refinement-004). It now needs a second amendment noting:
- The 6-mode primary surface is reduced to 5 modes + 1 deferred
- Research Authoring is a system-triggered capability, not a primary mode
- Explicit *"Research Mode"* command is preserved as power-user invocation
- 10-step closed loop and 3 operator gates remain unchanged from refinement-004

## Zach's brief simplification

The operator-facing brief Zach receives now lists **4 working modes + 1 deferred**:

| What you're producing | Mode |
|---|---|
| Plan for one person | **Clinical** |
| Content from a real signal | **Insight** |
| Exercise script | **Script** |
| Pricing/packaging/hiring call | **Business** |
| Long-form carousel | *(deferred — pick a different mode)* |

Plus a brief note that the system will prompt to ground new claims when gaps surface, and Zach can confirm or decline.

This is the surface Zach should see in the handoff package.

## Fresh-chat test protocol — Test 10 baseline correction (third time)

Test 10's input is currently:

> *"Research Mode. Need a record on stretch-mediated hypertrophy. Script lane references it. We don't have grounding yet. Walk me through what we'd need."*

Under refinement-005, Test 10 still works as a power-user explicit invocation test (since *"Research Mode"* is preserved for that use case). But the more production-realistic test pattern is now:

**Test 10-A (power-user explicit):** *"Research Mode. Need a record on [topic]."* — tests proactive Josh-side invocation.

**Test 10-B (system-triggered):** Provide a Script Mode or Insight Mode input that contains an ungrounded significantly-informative claim → system should prompt for Research Authoring → operator confirms → closed loop fires inline.

The protocol should add Test 10-B as a separate test of the system-triggered pattern. Test 10-A stays as the explicit-invocation test.

## Query Layer v1 unchanged

Bootstrap v1 First Activation Rule and Query Layer v1's "no abstract research; real input source required" discipline are unchanged. The capability still requires a real input source — what changes is whether that source is operator-declared (explicit Research Mode) or system-detected (gap surfacing during another mode's work).

## research-009 retroactively fits the new pattern

research-009 was authored 2026-05-03 under refinement-004's "Research Authoring Mode = explicit operator command" framing. Under refinement-005, the same authoring would be classified as **system-triggered** — the gap surfaced from Script Lane reference (cross-mode reference gap), and the operator confirmed the closed-loop execution. The record itself is unchanged; only the activation classification updates retroactively.

## Programming-for-Clients lane gap (separate, future)

Refinement-005 does **not** address the previously-flagged Programming-for-Clients lane gap (the "ACSM protocol question without a case" issue). That's a separate refinement candidate at N=1 — wait for ET-03 N=2 occurrence before logging.

# Action Status

**Resolved 2026-05-04.** Research Mode retired from operator-facing primary surface. Research Authoring promoted to system-triggered capability with prompt-then-loop discipline. Explicit *"Research Mode"* command preserved for power-user proactive invocation. CLAUDE.md, decision-017, Zach's brief, fresh-chat test protocol all flagged for update.

**Follow-on tasks** (separate work, sequential):

1. **Update CLAUDE.md** — Mode Activation table reduces to 5 modes + 1 deferred; add Power-User Reference subsection; add Research Authoring Prompt subsection
2. **Amend decision-017 (second time)** — note refinement-005 simplification; preserve refinement-004 amendment as historical record
3. **Update Zach's brief** — 4 working modes + 1 deferred + system-triggered prompt note
4. **Update fresh-chat test protocol** — Test 10-A (power-user explicit) + Test 10-B (system-triggered) split
5. **Re-run fresh-chat Tests 1–6 + Test 10-A + Test 10-B** against fully corrected docs (final architectural validation)

These are sequential follow-ons. Not blocking refinement-005 lock.

# Last Updated

2026-05-04 — initial refinement entry authored. Trigger: 2026-05-04 operator architectural review during Zach handoff preparation. Resolution: Research Mode retired from operator-facing primary surface; Research Authoring promoted to system-triggered prompt-then-loop capability; explicit *"Research Mode"* preserved for power-user proactive invocation. Five follow-on tasks identified. HL-09 / HL-10 evaluations passed. The 10-step closed loop and 3 operator gates from refinement-004 remain unchanged — what changes is the activation pattern, not the discipline.
