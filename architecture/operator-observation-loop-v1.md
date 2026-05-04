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

## Pre-Alpha-2 — Analysis (2026-05-04)

**Source:** `records/research/validation/2026-05-04-pre-alpha-2-seed-usage observation.md`
**Window:** Single fresh-chat session, Zach machine, ACSM 2026 protocol-build arc. Operator (Josh acting as Zach) ran a comprehensive training-protocol-template input through Clinical Mode → triggered system Research Authoring prompt → ran the full 10-step closed loop with 3 gates → received full protocol output. Session hit Claude.ai web 90% limit after the protocol artifact landed.
**Repo state during the observed session:** CLAUDE.md updated through commit `4d37713` (refinements 004–007 active, §6 Iterative Refinement subsection, operator observation loop architecture established, system-history archive surgically removed for context budget). Refinement-008 was authored *after* this session based on the patterns surfaced in it; it was not in scope for the chat being observed.

### Pre-session context-budget observation

Before any input could be tested, the bare load of CLAUDE.md + project repo into Claude.ai web exceeded the context window by 637k tokens. Diagnosed as the 1.87MB founder-Claude conversation archive at `records/system-history/raw/founder-claude-conversation-archive.md` (~470k tokens alone). Resolved via surgical fix: tag-archived the directory at `archive/system-history-2026-05-04`, gitignored the single oversized file, restored extracted/patterns/raw-README to preserve doctrine roles. CLAUDE.md §3 updated to point at the archive tag. After the fix, bare load fit within budget.

**Operationally significant observation, not a doctrine failure** — but it reveals an architectural gap: the repo had no enforced *auto-load vs. discoverable* boundary. Adding everything as if context were infinite is a real failure mode. Worth a future doctrine touch on what belongs in active project knowledge vs. what stays in archive-tag-accessible state.

### Pattern observations

1. **Mode-pick under ambiguity worked per CLAUDE.md §2.** Operator's input ("comprehensive training protocol template for future client work") didn't fit any single mode cleanly. System asked *"Which mode?"* — exactly the §2 default behavior. The Claude.ai UI rendered the ask as a 3-option picker (Clinical/Business/Script + Something else + Skip). Doctrine ambiguity: whether the picker rendering is a system violation of refinement-006 or a platform UI affordance over a doctrine-compliant ask. Held as ambiguous.
2. **Clinical Mode locked correctly** with the canonical *"Clinical Mode locked. Movement Case Engine active."* phrasing per refinement-005 spec.
3. **Refinement-005 system-triggered Research Authoring fired correctly.** When the operator's input contained the significantly-informative claim *"based on ACSM updated guidelines,"* the system surfaced a grounding decision rather than building ungrounded. Did NOT auto-fire the closed loop. Operator-authorized. Validates refinement-005's narrow-trigger discipline.
4. **Grounding-path framing — soft refinement-008 case.** System offered a 2-path picker (Build now + disclose ungrounded vs. Research Authoring first). The 2-path framing surfaced a real time/quality trade-off that yes/no per refinement-005's literal spec would have hidden. But no closing recommendation. Soft FAIL on rule 3 as later sharpened by refinement-008.
5. **Refinement-007 turn flow — exemplary execution.** After grounding-path selection, system announced *"Searching ACSM 2026 Position Stand on Resistance Training before Gate A."* Search ran silently. PubMed abstract fetched. Verified. Gate A presented with PMID 41843416, full citation (Currier BS et al., *Med Sci Sports Exerc.* 2026 Apr 1;58(4):851-872), and exact figures verbatim across 5 categories (strength, hypertrophy, power, non-impact variables, synthesis base of 137 systematic reviews / >30,000 participants). Single turn from grounding-path selection to verified Gate A. Pre-search guessing → blocked. Refinement-007 landed in production.
6. **HL-09 strict throughout the closed loop.** PubMed-direct verification. Exact figures verbatim. PMID present. Source link present. No fabrication.
7. **Gate B L3 mapping caught a real deviation.** The cross-record implication item (item 4 of the L3 mapping) flagged the discrepancy between operator's protocol spec ("1 max effort + 2 warm-ups") and ACSM's strength prescription ("2-3 working sets at ≥80% 1RM"). High-leverage system behavior — exactly what L3 mapping should do.
8. **Gate C confidence calibration appropriate.** HIGH confidence given umbrella review evidence base + verified PMID + recognized authorities. Caveats were decision-relevant scope limits (abstract-level capture, healthy adults, cardio out-of-scope) — not pre-emptive caveating. Refinement-006 rule 4 held.
9. **Research-010 lock + Mode handoff clean.** Research Mode → Clinical Mode transition acknowledged explicitly (*"research-010 locked. Research Mode closing. Returning to Clinical Mode."*).
10. **Working-set prescription turn — canonical refinement-008 FAIL.** Three-option picker (Keep 1 max-effort / Match ACSM 2-3 sets / Hybrid + Something else + Skip) with rationale per option, no closing recommendation. Operator had to choose without the system's call. This is the canonical FAIL example documented in refinement-008.
11. **§6 Iterative Refinement landed in production.** Protocol output opened with *"Reprinting full artifact per §6 Iterative Refinement."* Explicit reference to doctrine authored ~1 hour earlier. Validates the doctrine-promotion → next-chat-behavior pipeline of the meta-learning loop.
12. **Protocol output substantively strong.** Comprehensive 60-min template with time architecture, RT prescription grounded against research-010 with verified figures inline, pre-activation block (postural targeting logic), 5 standardized cues, 2/3/4/5-day splits, cardio selection rule, specificity block logic, build notes for client modification. Volume threshold flag honest (2-set protocol below hypertrophy threshold given 2x/week frequency). 3-day PPL → Upper/Lower/Full override caught the ACSM ≥2x/week non-compliance. HL-09 disclosures surgical (out-of-scope portions explicitly flagged).
13. **Cardio Selection Rule is template content, not a menu.** Conditional logic for downstream operator-side use ("HIIT — use on neural-light days. Moderate — use when client has aerobic deficit") is template content describing rules for client adaptation, not an operator-choice menu requiring a system recommendation. Refinement-008 scope language excludes this case correctly.
14. **Claude.ai web 90% session-limit hit after one comprehensive output.** Long-form artifact deliverables eat session budget fast. Operationally significant for iteration arcs (Pre-Alpha-1 had 20+ refinements over 2.5 hours; Pre-Alpha-2 hit 90% after the first artifact print). Platform constraint, not doctrine issue.

### Highest-leverage observations to watch for repetition

- **Bare-menu pattern (refinement-008 candidate).** Pre-Alpha-2 had 1 hard violation (working-set turn) + 1 soft case (grounding-path turn) + 1 doctrine-ambiguous case (mode-pick). Refinement-008 was authored on the basis of this single observation because the operator's verbal pushback (*"the recommendation is what was missing as the last option"*) constituted a stated rule — doctrine-eligible without repetition per the single-observation rule's exception. Pre-Alpha-3 confirms whether refinement-008 took effect.
- **Decision-criteria-vs-menu distinction.** Refinement-008 scope explicitly excludes template content with conditional logic. Watch whether the system continues providing decision-criteria appropriately without confusing it for operator-choice menus.
- **Laterality preservation under iteration (Pre-Alpha-1 watch).** Pre-Alpha-2 didn't exercise laterality much (template-builder context, not case-iteration context). Still pending repetition check.
- **Operator vocabulary drift (Pre-Alpha-1 watch).** Pre-Alpha-2 didn't exercise this — operator declared mode explicitly when asked rather than typing alternative vocabulary. Still pending.
- **Mode declaration skipped (Pre-Alpha-1 watch).** Pre-Alpha-2 had operator declare Clinical Mode explicitly via picker selection. Different pattern than Pre-Alpha-1's skip-then-infer. Watch for whether explicit declaration becomes the default once operators learn the picker exists.
- **Iterative artifact-refinement (Pre-Alpha-1 watch).** Pre-Alpha-2 didn't iterate on the protocol output (90% session-limit hit prevented iteration). Still pending repetition check across iteration arcs.
- **Session-limit constraint on iteration headroom.** New observation. Whether this becomes a recurring constraint depends on operator workflow — if Zach's typical sessions deliver one artifact per chat, the 90% limit may not bind. If he iterates extensively, it will. Watch.

### Direct operator authorizations (immediately doctrine-eligible)

1. **Recommendation closes the call (refinement-008).** Verbatim from operator: *"the menus weren't too complex for a PT. They were appropriately rich. The system just didn't take the call within them."* And: *"yes the recommendation is what was missing as the last option, brilliant."* **Promoted 2026-05-04** to CLAUDE.md §2 rule 3 + refinement-008 doctrine entry + decision-017 fifth amendment.
2. **Pattern claims must be specific (meta-learning loop discipline).** Surfaced when operator pushed back on agent's overcounting of "4× menu pattern" (honest count: 1 hard + 1 soft + 2 misclassifications). **Promoted** to refinement-008 implications section as a meta-learning loop discipline lesson — pattern claims must specify what repeated, not summary counts. Lumping doctrine-compliant cases with genuine violations contaminates pattern detection.

### Disposition

Filed as Pre-Alpha-2. One direct authorization promoted to doctrine via refinement-008 (CLAUDE.md + decision-017 + new refinement entry). One meta-learning lesson recorded into the loop discipline. Pattern observations and watch items held for repetition check against Pre-Alpha-3.

**Net signal from Pre-Alpha-2:** the closed-loop substance + delivery rhythm + turn-flow disciplines (refinements 004–007) all landed in production cleanly. The §6 Iterative Refinement doctrine landed immediately in the next-chat. Refinement-008 emerged as a real new finding requiring rule 3 sharpening. Operator observation loop functioning as designed: observation → analysis → doctrine refinement → next-chat behavior change.

---

## Future entries

Each subsequent observation appends a section here:

- `## Pre-Alpha-3 — Analysis (YYYY-MM-DD)`
- `## Pre-Alpha-4 — Analysis (YYYY-MM-DD)`
- ...

Each entry follows the same structure: source pointer, window, repo state, pattern observations, watch items, direct operator authorizations, disposition.

When patterns repeat across entries, doctrine updates surface in the next refinement cycle (same mechanism as refinement-001 through refinement-008).

---

## Last Updated

2026-05-04 — initial doc authored. Loop architecture established. Five discipline rules locked. Pre-Alpha-1 analysis filed (12 pattern observations + 6 watch items + 3 direct operator authorizations evaluated). One authorization promoted to CLAUDE.md §6 (full-artifact reprint on iteration); two held (PRI breath cadence as wrong doctrine layer; 4–5 cues per exercise as case-context-dependent, awaiting repetition).
2026-05-04 (later) — Pre-Alpha-2 analysis filed (14 pattern observations + 7 watch items + 2 direct operator authorizations evaluated). One authorization promoted to refinement-008 + CLAUDE.md §2 rule 3 + decision-017 fifth amendment ("recommendation closes every gate"); one meta-learning lesson promoted to loop discipline ("pattern claims must be specific about what repeated, not summary counts"). Net signal: refinements 004–007 + §6 Iterative Refinement landed in production cleanly. Refinement-008 emerged as new finding requiring rule 3 sharpening. Pre-session context-budget overflow and Claude.ai 90% session-limit observed as platform constraints separate from doctrine.
