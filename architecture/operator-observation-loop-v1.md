---
doc_id: operator-observation-loop-v1
version: v1
date: 2026-05-04
type: meta-system architecture
purpose: Establish the operator-observation → pattern detection → doctrine refinement loop as a real architectural commitment. Lock the discipline that prevents observation data from shaping runtime chat behavior. Carry the analytical layer for each observation entry so the raw transcripts stay clean as source material.
relevant_doctrine:
  - CLAUDE.md (§1 lists this doc as a meta-system component)
  - architecture/master-operating-system-governance-bridge-v1.md (sibling)
  - architecture/governing-logic-v1.md (sibling)
linked_artifacts:
  - records/research/validation/2026-05-04-pre-alpha-1-zach-usage observation.md (Pre-Alpha-1 raw source — Zach's chat May 3–4)
hl_09_evaluation: PASS — no fabricated grounding. The loop is structural; it introduces no claims, citations, or evidence to be verified.
hl_10_evaluation: PASS — addition justified by documented current need. Pre-Alpha-1 surfaced both immediately-promotable operator authorizations and patterns to watch. Without this doc, those signals have no structural home and the discipline that governs them is not locked. Thin layer (loop + 5 discipline rules + per-observation analysis); not an expansive automation system.
---

# Operator Observation Loop v1

## Purpose

The Operator Observation Loop captures how the system's actual operators (Zach in production; Josh during build) use the system in practice — and feeds those observations into doctrine refinement *without* contaminating runtime chat behavior.

The loop exists because reported behavior decays and self-report is unreliable. Watching what operators actually do, in real chats, produces signal that retrospective interviews cannot. Live observation catches misalignment at the moment it occurs, before the operator rationalizes around it.

---

## The Loop

Three stages:

1. **Observation.** Raw operator chat transcripts captured as source material under `records/research/validation/`. Lightly cleaned for readability; substance preserved verbatim. One file per session, dated and named.
2. **Pattern detection.** Analytical layer (this doc + future amendments) identifies recurring patterns across observation entries. Single observations stay observations; patterns become candidate doctrine updates only after they repeat.
3. **Doctrine refinement.** Repeated patterns get promoted into `CLAUDE.md` or relevant doctrine docs as actual rules. The promoted rule then governs all future chats. Operators experience this as the system "knowing them" — but the mechanism is doctrine, not log-reading.

**The loop runs between sessions, never within them.**

---

## Discipline (locked)

Five rules govern the loop:

1. **Observation = input. Pattern detection = analysis. Doctrine refinement = output.** Don't conflate the stages.
2. **Single-observation rule.** A pattern visible in only one session is not actionable. Wait for repetition across two or more sessions before promoting to doctrine. **Exception:** an explicit verbal authorization from the operator (a stated rule, not a pattern) is doctrine-eligible immediately without repetition. The single-observation rule applies to *behaviors observed*; not to *rules stated.*
3. **Observer-effect mitigation.** Watch passively. Do not coach operators toward doctrine fit. If operators know they're being watched-and-iterated-on, their usage skews toward what they think the system wants, and signal degrades.
4. **No runtime data ingestion.** Raw observation transcripts are NOT auto-loaded into chats. The loop processes data between sessions. CLAUDE.md surfaces this loop's existence (§1 reference) but does not pull in observation content.
5. **No pre-staging from observations.** The loop's purpose is doctrine refinement, not anticipation. Pre-staging "next likely info" based on observed patterns violates Action Override + Hard Override + the "stop at the next move" rule.

---

## What this loop is NOT

- Not a runtime memory layer. The system does not "remember" prior sessions in chat.
- Not pattern-prediction. It does not pre-stage info the operator is "likely" to ask for.
- Not surveillance dressed as continuity. It does not change the operator's chat behavior; it changes the doctrine that all chats run on.
- Not a replacement for client records. State preservation for specific cases (e.g., "the 26yo case") belongs in client records, not in this loop.

---

## Activation

The loop activates whenever a new observation entry lands:

1. Raw transcript saved at `records/research/validation/YYYY-MM-DD-pre-alpha-N-zach-usage observation.md` (or equivalent operator-named convention).
2. Analytical entry appended to this doc as `## Pre-Alpha-N — Analysis (YYYY-MM-DD)`.
3. Patterns flagged. If the same pattern appears in two or more entries, a candidate doctrine update surfaces in the next refinement cycle.
4. Direct operator authorizations (stated rules) get promoted to doctrine immediately, bypassing pattern repetition.

---

## Pre-Alpha-1 — Analysis (2026-05-04)

**Source:** `records/research/validation/2026-05-04-pre-alpha-1-zach-usage observation.md`
**Window:** Zach's project chat May 3 case-test arc + May 4 morning iterative programming session (7:57 AM – 10:47 AM).
**Repo state during the observed session:** CLAUDE.md updated through refinement-005 (5-mode operator surface, Research Authoring as system-triggered). Refinements 006 and 007 were authored *after* the session and were not in scope for the chat being observed.

### Pattern observations

1. **Mode declaration is mostly skipped — inference works.** Zach opened most cases with the case description directly, no mode declared. The system inferred Clinical correctly every time. Mode declaration may be a doctrine artifact more than an operator habit.
2. **Operator vocabulary ≠ doctrine mode names.** He typed `"programming"` and `"research"` as standalone responses to "Which mode?" — neither is a mode. Cost: two clarification turns at the start of the ACSM thread.
3. **Research Authoring fired correctly when explicitly invoked.** "Research Mode. Need a record on stretch-mediated hypertrophy" → closed loop activated, Gate A presented two ranked seed options, no bloat.
4. **Citation hunger surfaces inline, embedded in programming work.** "Time for breathing ACSM guidelines" / "Wha about PRI" came as casual mid-flow questions during a programming arc. Research Layer (passive grounding) handled it correctly. Validates refinement-005 in observed practice.
5. **ACSM 2026 protocol question collided correctly with HL-09/HL-10.** System classified as inconclusive without a case. Bootstrap v1's First Activation Rule worked.
6. **Iteration depth is high for programming arcs.** The 26yo case spawned 20+ iterative refinements over ~2.5 hours.
7. **Cumulative state preservation worked across the iteration arc.** Every refinement printed the full current protocol, not a diff. Compounding value preserved. Zach explicitly confirmed the desired pattern: *"give me updated exercise everytime i tell you to update."*
8. **Laterality error caught by operator, not system.** System initially specified "sidelying — left side down" for a left-side intercostal strain (wrong; should be left side *up*). Zach caught and corrected. Side-context from earlier case input did not propagate forward into the protocol design step.
9. **"What is X" questions interleave with programming.** "Upper trap function" appeared mid-protocol-build. System pivoted to a clean anatomical answer, then resumed programming on the next turn.
10. **Categorization-for-template questions surface late.** "Is positional breathing mobility or activation?" came after the protocol structure was mostly built. System gave a binary answer to serve template-building.
11. **Typo and casual phrasing tolerated end-to-end.** No friction added.
12. **Carousel deferral message worked.** Correct redirect, no pushback.

### Highest-leverage observations to watch for repetition

These are NOT acted on from a single session. They become candidate doctrine updates if they repeat:

- **Operator vocabulary drift.** "Programming" / "research" used as mode-equivalents. If recurs — consider operator-vocabulary aliases or sharper Mode brief language.
- **Mode declaration skipped.** If consistently skipped and inference always succeeds, mode declarations may be a doctrine-internal mechanism not requiring operator habit.
- **Programming as a Clinical Mode use case.** The current Mode brief frames Clinical around case classification → root cause → intervention. Programming for that case is downstream — but not named explicitly. If "programming" comes up repeatedly as a mode-clarification trigger, the brief should name programming as a Clinical Mode capability.
- **Iterative artifact-refinement as a recognized pattern.** Long programming arcs follow a predictable shape: build structure → organize → split → time → cue → standardize. If recurs, "iteration mode" within Clinical may warrant explicit doctrine.
- **Laterality tracking under iteration.** Watch whether laterality errors surface again across multi-turn arcs. If yes, may need explicit doctrine on side-context preservation.
- **Citation hunger embedded in mode work.** Validates refinement-005's auto-grounding architecture. Watch whether the auto-grounding behavior continues to land cleanly without triggering Research Authoring incorrectly.

### Direct operator authorizations (immediately doctrine-eligible)

These are stated rules from Zach's transcript, not pattern-detected behaviors. Doctrine-eligible without waiting for Pre-Alpha-2 because the single-observation rule applies to behaviors observed, not rules stated.

1. **Full-artifact reprint on iteration.** Verbatim: *"give me updated exercise everytime i tell you to update."* **Promoted 2026-05-04** to CLAUDE.md §6 OUTPUT STYLE as the Iterative Refinement subsection.
2. **PRI breath cadence (4 sec inhale / 6–8 sec exhale, pursed lips).** Real reference framework standard. Citation-style content; lives as recallable Zach knowledge or in a future PRI reference asset. **Not promoted to CLAUDE.md** — wrong doctrine layer.
3. **4–5 cues per exercise.** Looks promotable but was case-specific to the 26yo programming arc. May not generalize across other client cases. **Held** for repetition check in Pre-Alpha-N.

### Disposition

Filed as Pre-Alpha-1. One direct authorization promoted to CLAUDE.md (full-artifact reprint on iteration). Pattern observations and watch items held for repetition check against Pre-Alpha-2.

---

## Future entries

Each subsequent observation appends a section here:

- `## Pre-Alpha-2 — Analysis (YYYY-MM-DD)`
- `## Pre-Alpha-3 — Analysis (YYYY-MM-DD)`
- ...

Each entry follows the same structure: source pointer, window, repo state, pattern observations, watch items, direct operator authorizations, disposition.

When patterns repeat across entries, doctrine updates surface in the next refinement cycle (same mechanism as refinement-001 through refinement-007).

---

## Last Updated

2026-05-04 — initial doc authored. Loop architecture established. Five discipline rules locked. Pre-Alpha-1 analysis filed (12 pattern observations + 6 watch items + 3 direct operator authorizations evaluated). One authorization promoted to CLAUDE.md §6 (full-artifact reprint on iteration); two held (PRI breath cadence as wrong doctrine layer; 4–5 cues per exercise as case-context-dependent, awaiting repetition).
