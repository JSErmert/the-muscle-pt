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

## Pre-Alpha-3 — Analysis (2026-05-04)

**Source:** `records/research/validation/2026-05-04-pre-alpha-3-seed-usage observation.md`
**Window:** Single fresh-chat session, Josh Max account (account-tier asymmetry methodology — doctrine-fidelity test, not budget-realism), ACSM 2026 protocol-build arc. Same template-builder input as Pre-Alpha-2. Different mode-declaration pattern: operator pre-declared "Research then Clinical" mode-spanning workflow upfront. Closed loop fired through 3 gates → Mode handoff to Clinical → protocol artifact built. No session-limit hit (Max plan).
**Repo state during the observed session:** CLAUDE.md updated through commit `3f66d83` (refinements 004–008 active, §6 Iterative Refinement subsection, operator observation loop architecture with Pre-Alpha-1 + Pre-Alpha-2 entries, system-history archive surgically removed, Pre-Alpha-2 raw transcript filed). Refinement-009 was authored *after* this session based on the HL-05 leak surfaced in it; it was not in scope for the chat being observed.

### Test type and methodology note

Pre-Alpha-3 was a **doctrine-fidelity test** in Josh's Max account, not a **budget-realism test** in Zach's Pro account. The methodology distinction was established mid-session in Pre-Alpha-2 analysis. Pre-Alpha-3 specifically validates whether refinement-008 (recommendation-closes-the-call) took effect; budget-realism for Zach's daily workflow gets its own future test slot once Zach's rolling window resets.

### Pattern observations

1. **Mode-pick picker pattern recurred — second consistent observation.** "Which mode?" surfaced as a 3-option picker (Clinical/Business/Script + Something else + Skip) — same pattern as Pre-Alpha-2. Two observations now. The doctrine ambiguity (system violation of refinement-006 vs. Claude.ai web UI affordance over a doctrine-compliant ask) remains unresolved. Pattern repetition observed but root cause undetermined.

2. **Operator pre-declared mode-spanning workflow.** Josh typed *"Research then Clinical"* in response to the mode-pick. CLAUDE.md §2 mode-spanning rule explicitly handles this: *"Finish one mode's work first, then switch."* System acknowledged Research first, locked, ran the closed loop, handed off to Clinical cleanly. **New operator pattern not seen in Pre-Alpha-2** (where operator just said "Clinical Mode" and got a downstream grounding-path picker). Pre-declaring the mode-spanning chain skipped the grounding-path picker entirely.

3. **Refinement-007 turn flow PASS with bonus tool-failure handling.** System announced *"Searching ACSM 2026 Position Stand on Resistance Training before Gate A."* Search ran. PMC blocked → system fell back to a secondary source (Applied Performance breakdown of the Position Stand). Verification discipline maintained throughout tool failure: no fabrication, no bail, alternative source surfaced and used. **Robust HL-09 behavior under degraded tool conditions** — new positive observation.

4. **HL-09 multi-source verification.** Gate A explicitly noted *"figures verify across official ACSM, EurekAlert, and PubMed."* Stronger than Pre-Alpha-2's single-source PubMed verification. Citation discipline strengthened in production.

5. **Refinement-008 landed verbatim across ALL three gates.** Each gate closed with the recommended-pick + confirm/override pattern:
   - Gate A: *"Lock as research-010 seed? Recommend lock — figures verify across official ACSM, EurekAlert, and PubMed; matches your protocol's 2x/week + ≥80% 1RM + max effort prescription directly. Confirm or override."*
   - Gate B: *"Recommend lock as mapped. Confirm or override."*
   - Gate C: *"Recommend lock at High confidence. Confirm or override."*
   Doctrine over-delivered: Gate A added the closing recommendation pattern even for a yes/no decision (which doesn't strictly require it under refinement-008). Doctrine I authored ~1 hour earlier fired exactly per spec in production.

6. **Cross-record implications richer at Gate B.** Explicitly named research-002 reinforcement and research-009 anchoring. More thorough than Pre-Alpha-2's Gate B mapping. The system's L3 mapping is integrating prior records correctly.

7. **Working-set prescription menu DID NOT FIRE.** The canonical Pre-Alpha-2 FAIL surface (3-option picker without recommendation: Keep 1 / Match ACSM / Hybrid) did not surface in Pre-Alpha-3. System just built the protocol with operator's spec while disclosing the deviation inline (*"This protocol's 1 max-effort + 1 back-off (2 working sets total) sits at the floor of the strength range..."*). **Refinement-008 + operator's pre-declared mode-spanning workflow combined to skip the menu surface entirely.** Major doctrine win.

8. **Mode handoff Research → Clinical clean.** Transition acknowledged explicitly: *"Closed loop complete. Switching to Clinical Mode. Movement Case Engine active. Building protocol now."* §2 mode-spanning rule honored.

9. **§6 Iterative Refinement passively held in artifact form.** Protocol output was a full-artifact print. No iteration arc fired in this session, so the doctrine wasn't actively tested under iteration pressure — but the artifact form is consistent with the doctrine.

10. **Cue Standardization tightened — substantive improvement.** Pre-Alpha-3 cues are shorter, more memorable, more usable for client cueing. Examples:
    - *"Ribs over pelvis. Pelvis over heels."* (vs. Pre-Alpha-2's longer relative-stack cue)
    - *"3 down, pause, drive up."* (vs. Pre-Alpha-2's tempo cue)
    - *"Move with purpose."* (RT) / *"Move with violence."* (power/plyo) — clean register distinction
    Tighter without losing instructional clarity.

11. **HL-09 comprehensive disclosure block softened.** Pre-Alpha-2 had an explicit disclosures section listing what's grounded (research-010) vs. ungrounded (pre-activation, cardio, specificity, postural correction). Pre-Alpha-3 has only the inline volume disclosure. The comprehensive scope disclosure was useful clinical context — its loss is mild but real. Watch whether this trends toward useful tightening or over-tightening.

12. **Cardio neural-overlap cue dropped.** Pre-Alpha-2 had *"Avoid HIIT on max-effort lower days — shared neural/metabolic demand."* Pre-Alpha-3 doesn't. Useful programming guidance lost. Same trend as #11 (artifact terser but loses some clinical nuance).

13. **3-day split simplification — clean but loses override flag.** Pre-Alpha-2 explicitly noted PPL doesn't hit ≥2x/week ACSM minimum, recommended Upper/Lower/Full. Pre-Alpha-3 just notes *"Full-body × 3 (recommended for general pop)"* — cleaner but loses the why.

14. **HL-05 leaked into artifact output — refinement-009 trigger.** Closing line: *"Reassess before progressing per HL-05."* HL-05 is real (`governance/hard-locks-v1.md:66` — "Reassess Before Progressing"). HL-09 NOT violated (no fabrication). §5 principle ("engines fire silently") VIOLATED — internal hard-lock identifier leaked into operator-facing protocol output. Refinement-009 authored same day to sharpen §5: internal identifiers (HL-X, research-XXX, refinement-XXX, decision-XXX, §X) and engine/component names must never appear in artifact output, only in closed-loop gate output. CLAUDE.md §5 bullet replaced with broader language; translation example explicit (*"HL-05" → "reassess before advancing load, range, or complexity"*).

15. **Operator vocabulary consistency.** Josh used *"confirm"* and *"confirm lock"* at gates — clean expected vocabulary, no drift. Different from Pre-Alpha-2 where operator used *"Yes please"* / *"Lock"* — both work, but consistency within a session is observed.

16. **Account-tier asymmetry methodology validated.** Pre-Alpha-3 ran in Josh's Max account. No session-limit hit despite running the same comprehensive protocol output that hit 90% in Pre-Alpha-2 on Zach's Pro account. Confirms the asymmetry is real and substantial. Doctrine-fidelity test ran cleanly; budget-realism test still pending Zach's rolling window reset.

### Highest-leverage observations to watch for repetition

- **Mode-pick picker pattern.** Now 2 consistent observations (Pre-Alpha-2 and Pre-Alpha-3). Doctrine-ambiguous (system vs. UI affordance). Pre-Alpha-4 confirms whether the pattern is reliably the platform UI rendering a doctrine-compliant ask, or whether the system is actually generating menu-style asks that should be tighter. If the latter, refinement candidate.
- **§5 internal-identifier discipline (refinement-009 just locked).** Watch Pre-Alpha-4 for whether artifact output stays clean of HL-X / research-XXX / refinement-XXX / decision-XXX / §X / engine names. The HL-05 pattern shouldn't recur. If it does → doctrine isn't landing despite explicit promotion.
- **Artifact richness vs. terseness trend.** Pre-Alpha-3 lost some explicit disclosures relative to Pre-Alpha-2 (HL-09 disclosure block, cardio neural-overlap cue, 3-day override flag). Watch whether this trends toward useful tightening or over-tightening that loses clinical context. May warrant a §6/§7 doctrine touch on "what to preserve when tightening."
- **§6 Iterative Refinement under iteration pressure.** Still not exercised across multiple sessions. Pre-Alpha-1 had iteration depth (20+ refinements); Pre-Alpha-2 hit session limit before iterating; Pre-Alpha-3 didn't iterate. Watch whether reprint discipline holds under 5+ iteration arcs in a future test.
- **Tool-failure handling under HL-09.** Pre-Alpha-3 demonstrated PMC fallback maintained verification discipline. Watch whether this generalizes to other tool failures (PubMed downtime, search API rate limits, etc.). Positive observation; not yet doctrine-promotable.
- **Bare-menu pattern at non-gate multi-way decisions.** Pre-Alpha-3 didn't surface non-gate multi-way decisions (operator pre-authorized via mode-spanning declaration, skipping the grounding-path and working-set surfaces). Watch Pre-Alpha-4 for arcs that DO surface non-gate multi-way decisions to confirm refinement-008 holds beyond gate output.

### Direct operator authorizations (immediately doctrine-eligible)

1. **Internal leakage prohibition (refinement-009).** Verbatim from operator earlier in the session, regarding HL-05: *"we dont want internal leakage that cant be understood by a PT."* Stated rule. **Promoted 2026-05-04** to refinement-009 + CLAUDE.md §5 sharpening.

### Disposition

Filed as Pre-Alpha-3. One direct authorization promoted to doctrine via refinement-009 (CLAUDE.md §5 sharpened, internal-identifier patterns enumerated, closed-loop gate exception preserved). Pattern observations and watch items held for repetition check against Pre-Alpha-4.

**Net signal from Pre-Alpha-3:**

- **Refinement-008 fully landed in production.** The canonical Pre-Alpha-2 FAIL surface (working-set bare menu) did not appear. Refinement-008 + operator's clearer upfront framing skipped the surface entirely. Doctrine I authored ~2 hours earlier fired exactly per spec.
- **Refinement-007 strengthened in production.** Tool-failure fallback + multi-source verification — robust HL-09 behavior under degraded conditions.
- **Refinement-009 emerged as new finding.** HL-05 leak now resolved via §5 sharpening.
- **Operator observation loop functioning at design capacity.** Two iterations (Pre-Alpha-2 → refinement-008; Pre-Alpha-3 → refinement-009) demonstrating: observation → analysis → doctrine refinement → next-chat behavior change. The loop's value is now demonstrable, not just architectural.

---

## Pre-Alpha-4 — Analysis (2026-05-04)

**Source:** `records/research/validation/2026-05-04-pre-alpha-4-seed-usage observation.md`
**Window:** Single fresh-chat session, Josh Max account (continued doctrine-fidelity test cadence). Same template-builder input as Pre-Alpha-2/3 plus 12-week periodization request added to the operator's input. Closed loop fired through 3 gates → mode handoff to Clinical → protocol artifact built with periodization integrated. No session-limit hit.
**Repo state during the observed session:** CLAUDE.md updated through commit `0179809` (refinements 004–009 active, §6 Iterative Refinement, operator observation loop with Pre-Alpha-1 + Pre-Alpha-2 + Pre-Alpha-3 entries). Refinement-010 was authored *after* this session based on the leak regression surfaced in it; it was not in scope for the chat being observed.

### Pattern observations

1. **Mode-pick picker pattern recurred — third consistent observation.** *"Which mode?"* surfaced as picker again. Three sessions now, same pattern. Doctrine-ambiguous (system vs. Claude.ai web UI affordance) — pattern reliability is now established but root cause still undetermined.

2. **Operator pre-declared mode-spanning workflow — second consistent observation.** Josh typed *"first research and then clinical"* — same operator pattern as Pre-Alpha-3 (*"Research then Clinical"*). Two consistent observations now. **Operator has internalized mode-spanning declaration as preferred entry pattern.** Skipped grounding-path picker entirely both times.

3. **Refinement-007 turn flow PASS** with another tool-fallback observation. System announced *"Searching ACSM 2026 Position Stand on Resistance Training before Gate A."* Search ran. Pulled secondary source ("Move Your Bones breakdown") for verbatim figures. Verification complete.

4. **Tool-failure fallback discipline — second consistent observation.** Pre-Alpha-3 had PMC blocked → Applied Performance fallback. Pre-Alpha-4 had similar pattern (Move Your Bones secondary). HL-09 verification discipline maintained under degraded tool conditions across two sessions. **Now repetition-confirmed.**

5. **HL-09 multi-source verification continued.** *"Figures verify across PubMed, ACSM official, and physiotherapist breakdown."* Consistent with Pre-Alpha-3 multi-source pattern.

6. **Refinement-008 landed verbatim across all 3 gates — second consistent observation.** Each gate closed with *"Recommend X because Y. Confirm or override."* Identical pattern to Pre-Alpha-3. **Refinement-008 is now repetition-confirmed in production.**

7. **Working-set prescription menu DID NOT FIRE — second consistent observation.** Same as Pre-Alpha-3. The canonical Pre-Alpha-2 FAIL surface continues to not appear under the operator's mode-spanning workflow + refinement-008 active. Reliable menu-skip behavior across two sessions.

8. **NEW — ACSM figures expanded.** Pre-Alpha-4 captured richer doctrine extractions than Pre-Alpha-3:
   - Effort: *"Near-failure (~2–3 RIR) sufficient — absolute failure not required"*
   - Power: *"≤24 reps × sets total volume"*
   - Hypertrophy: *"Loads 30%–100% 1RM with sufficient effort"*
   The system's tool-search depth improved between sessions. May be input-driven (operator added periodization request, which prompted deeper grounding scan).

9. **NEW — 12-week periodization handled substantively well.** Operator added *"Periodization weeks 1-4 perfect down the technique / Weeks 5-8 progressive overload weight in reps / Weeks 9-12 increase intensity push limits"* to the input. System integrated as 3-block periodization with explicit RPE / RIR targets, load progression rules, and reassessment markers per block transition. Substance is correct; form failed (see #11).

10. **§6 Iterative Refinement passively held.** Full-artifact reprint. No iteration arc fired this session. Doctrine still not exercised under iteration pressure across Pre-Alpha-2/3/4.

11. **REGRESSION — 5 internal-identifier leaks (refinement-010 trigger).** This is the dominant Pre-Alpha-4 finding:
    - **Handoff line** (3 leaks): *"Switching to Clinical Mode. Movement Case Engine active. Building the protocol now, grounded to research-010."*
    - **Block 2 description** (1 leak): *"HL-05 applies: reassess before advancing — if technique degrades, hold load"*
    - **Section header** (1 leak): *"HL-05 reassessment markers per block transition:"*
    
    Pre-Alpha-3 had 1 leak (closing line only). Pre-Alpha-4 had 5 leaks across artifact body + section headers + handoff line. **Refinement-009's declaration-layer constraint failed to scale with artifact complexity.** Adding 12-week periodization invoked HL-05 doctrine multiple times; the system named the identifier each time. Refinement-010 authored same day to elevate to §7 enforcement layer with pre-return scan-and-translate step.

12. **NEW — Handoff line scope gap surfaced.** Refinement-009 didn't explicitly cover the handoff line (the transition message between closed-loop and artifact build). Pre-Alpha-4 demonstrated the gap — *"Movement Case Engine active. ...grounded to research-010"* leaked because the handoff line wasn't classified as artifact output. Refinement-010 closed the gap by explicitly scoping the handoff line as artifact for translation purposes.

13. **Cue Standardization remained tight** (consistent with Pre-Alpha-3). *"Ribs over hips, hips over heels."* / *"3-1-X-1"* tempo standard / explicit breath control rules. Substantively strong.

14. **Specificity slot logic richer than Pre-Alpha-3.** Pre-Alpha-4 added isometric durations (*"3–5 sets, 20–45 sec"*), Power-set ACSM dosing (*"30–70% 1RM, ≤24 total reps × sets, fast concentric"*) — direct ACSM 2026 power figures embedded. Improvement.

15. **Last line of artifact stayed clean.** *"Reassess every 4 weeks. Reprint the full updated template at each iteration."* No closing-line HL-05 leak this time (unlike Pre-Alpha-3). The leaks shifted location — closing line in Pre-Alpha-3 → mid-artifact + section headers + handoff in Pre-Alpha-4. Same root cause, different surface.

16. **Operator's vocabulary varied across gates** — *"lock"* / *"proceed"* / *"confirm"*. Mixed but all parsed correctly. Different from Pre-Alpha-3's consistent *"confirm"* register.

### Highest-leverage observations to watch for repetition

- **§7 Internal-Identifier Translation Pass (refinement-010 just locked).** Watch Pre-Alpha-5 for clean artifact output. Patterns must NOT recur: HL-X anywhere in artifact, research-XXX anywhere in artifact, engine names on handoff line, mode declarations as artifact framing. If refinement-010 lands, doctrine progression is observation → analysis → enforcement-layer doctrine → next-chat behavior change. If still leaking, even harder enforcement is needed (e.g., output-formatting hooks).
- **Mode-pick picker pattern.** Now 3 consistent observations. Doctrine-ambiguous. If Pre-Alpha-5 confirms a fourth time, pattern reliability is fully established and either (a) we accept the platform UI rendering or (b) we author a doctrine touch around how the mode-pick gets framed.
- **Operator mode-spanning declaration as preferred entry pattern.** Two consistent observations. If recurs, may warrant doctrine recognition as the canonical operator entry pattern for multi-mode work (e.g., explicit example in §2 mode-switching documentation).
- **Tool-failure fallback discipline.** Two consistent observations. Worth promoting to doctrine recognition — *"under tool failure, system surfaces alternative verification source rather than fabricating or bailing"* is now established behavior, not chance. Could be added to refinement-007 as a recognized sub-pattern.
- **§6 Iterative Refinement under iteration pressure.** Still not exercised across Pre-Alpha-2/3/4. Watch Pre-Alpha-5 for whether reprint discipline holds across 5+ refinements in an arc.
- **Declaration-vs-enforcement doctrine pattern.** Refinement-010's meta-learning lesson — *"declaration-layer doctrine doesn't scale with artifact complexity; fix is enforcement-layer, not stricter declaration"* — should be tested against other principle-language constraints in CLAUDE.md. Watch for whether other §5 constraints regress similarly under complexity (factor-watching ban, tool-migration ban, etc.).
- **Artifact richness scaling with input complexity.** Pre-Alpha-4 had richer ACSM figures than Pre-Alpha-3 because the operator's input was richer (added periodization). Watch whether this is a reliable pattern (richer input → richer grounding) or session-specific.

### Direct operator authorizations (immediately doctrine-eligible)

1. **Internal-identifier scan-and-translate enforcement (refinement-010).** Verbatim from operator after seeing the 5 leaks: *"there is still plenty of internal jargon please identify each time something appears that is not pt language ( i still see HL-05...)."* Stated rule. **Promoted 2026-05-04** to refinement-010 + CLAUDE.md §7 OUTPUT TRANSLATION new subsection (Internal-Identifier Translation Pass).

### Disposition

Filed as Pre-Alpha-4. One direct authorization promoted to doctrine via refinement-010 (§7 enforcement layer added; declaration → enforcement transition recorded as meta-learning lesson). Pattern observations and watch items held for repetition check against Pre-Alpha-5.

**Net signal from Pre-Alpha-4:**

- **Refinement-008 repetition-confirmed.** Two consistent observations of clean recommendation-closes-the-call across all 3 gates. Doctrine fully landed.
- **Refinement-007 strengthened with second tool-failure fallback observation.** Repetition-confirmed.
- **Refinement-009 regressed under increased artifact complexity** (1 leak → 5 leaks when periodization was added). Refinement-010 authored to elevate to §7 enforcement layer.
- **Operator observation loop now demonstrating its highest-value pattern** — surfacing doctrine that's strong-enough-for-simple-cases but breaks under complexity. The loop catches this BEFORE it becomes systemic. Each iteration sharpens the doctrine; each next iteration tests the sharpening.
- **Three iterations of refinement now demonstrably driven by the loop:** Pre-Alpha-2 → refinement-008 (menus); Pre-Alpha-3 → refinement-009 (identifier leaks declaration); Pre-Alpha-4 → refinement-010 (identifier leaks enforcement). The loop is the doctrine-evolution engine.

---

## Pre-Alpha-5 — Analysis (2026-05-04)

**Source:** `records/research/validation/2026-05-04-pre-alpha-5-seed-usage observation.md`
**Window:** Single fresh-chat session, Josh Max account, doctrine-fidelity test cadence. Same template-builder + 12-week periodization input as Pre-Alpha-4. Closed loop fired through 3 gates → mode handoff → protocol artifact built. No session-limit hit.
**Repo state during the observed session:** CLAUDE.md updated through commit `cc99c0b` (refinements 004–010 active including refinement-010's §7 Internal-Identifier Translation Pass enforcement subsection, Pre-Alpha-1 through Pre-Alpha-4 entries filed). Refinement-011 was authored *after* this session in response to the doctrine-not-landing failure surfaced in it.

### Critical finding: refinement-010 did not land

Pre-Alpha-5 is a fresh run with refinement-010's §7 enforcement active. It produced **identical output to Pre-Alpha-4** — same operator inputs, same closed-loop responses, same protocol output, same 5 internal-identifier leaks:

- Handoff line: *"Switching to Clinical Mode. Movement Case Engine active. Building the protocol now, grounded to research-010."* (3 leaks)
- Block 2 description: *"HL-05 applies: reassess before advancing — if technique degrades, hold load"* (1 leak)
- Section header: *"HL-05 reassessment markers per block transition:"* (1 leak)

Refinement-010's §7 enforcement subsection ("scan-and-translate before return") was active in CLAUDE.md and did not prevent recurrence under fresh execution. **This is doctrine-not-landing despite explicit declaration AND enforcement framing.**

### Pattern observations

1. **Refinement-010 failure under fresh execution.** Same input + same repo state + new chat → identical leaks. The §7 enforcement subsection did not change behavior. Three possible causes (in order of likelihood): §7 placement too late in CLAUDE.md (Action Override + Hard Override + §6 OUTPUT STYLE are far more attended); principle-language framing still too soft (transformation not refusal); model instruction-following ceiling at this level of doctrine specificity.

2. **L3 / abstract architecture terminology in Gate B output.** Operator (Josh) noticed *"Gate B — L3 system mapping"* and other internal terminology (Case Engine, Decision Layer, Content Output Contract, lane names) within closed-loop gate output. These are doctrine-exempted under refinement-010's closed-loop exception, but unfamiliar to a production operator without doctrine onboarding. **The exception is too broad.** Refinement-011 tightens it to a two-tier model (specific identifiers allowed; abstract architecture terminology translates).

3. **Refinement-007 + refinement-008 + tool-failure fallback all consistently held.** Same gate flow, same multi-source verification, same recommendation-closes-the-call discipline as Pre-Alpha-3 and Pre-Alpha-4. These refinements have now been observed three times without violation. Doctrine-landing reliable for these.

4. **Operator mode-spanning declaration as preferred entry pattern — third consistent observation.** *"first research and then clinical"* — operator continues to use mode-spanning declaration as default entry. Three sessions, three observations.

5. **Mode-pick picker pattern — fourth consistent observation.** *"Which mode?"* surfaced as picker. Pattern is now reliably established. Doctrine-ambiguous between system behavior and Claude.ai web UI affordance.

6. **§6 Iterative Refinement still not exercised under iteration pressure.** Pre-Alpha-5 ran one artifact print, no iteration arc.

### Highest-leverage observations to watch for repetition

- **Pre-Alpha-6 will determine whether refinement-011 lands or whether doctrine has hit a model ceiling.** This is the dominant watch-item. Refinement-011 combines four elements: Action Override placement (most-attended doctrine section), refusal framing replacing transformation framing, concrete WRONG/CORRECT examples with verbatim Pre-Alpha-4/5 leaks, closed-loop exception tightened to two-tier model. If Pre-Alpha-6 fresh run still leaks, the production response shifts to operator-side review (Zach reads artifact for jargon before client delivery), accepting that doctrine has a ceiling and stopping further identifier-translation refinements.
- **Mode-pick picker pattern (4 consistent observations now).** No longer ambiguous in terms of pattern reliability — only ambiguous in root cause (system vs. UI). May warrant explicit doctrine acknowledgment that this is platform-rendered and acceptable.
- **§6 Iterative Refinement under iteration pressure.** Still unexercised. Worth deliberately testing in Pre-Alpha-N+ via an iteration arc.

### Direct operator authorizations (immediately doctrine-eligible)

1. **Strongest single doctrine attempt before accepting model ceiling.** Verbatim from operator after seeing Pre-Alpha-5's identical leaks: *"proceed please so this is fixed."* Combined with the operator's prior framing *"there is still plenty of internal jargon... we dont want internal leakage that cant be understood by a PT."* **Promoted 2026-05-04** to refinement-011 with four-element bundle: Action Override placement + refusal framing + concrete examples + closed-loop exception tightening.

2. **L3 / abstract architecture terminology should translate even within closed-loop gates.** Verbatim observation from operator: *"it says L3 - mapping gateway which is the only thing i noticed."* **Promoted** to refinement-011's two-tier closed-loop exception model (specific identifiers allowed at gates; abstract architecture terminology translates).

### Disposition

Filed as Pre-Alpha-5. Two direct authorizations promoted to doctrine via refinement-011 (Action Override placement, refusal framing, WRONG/CORRECT examples, two-tier closed-loop exception). Pre-Alpha-6 result determines next move — if leaks persist despite refinement-011, accept model ceiling and shift to operator-side review.

**Net signal from Pre-Alpha-5:**

- **Refinements 007, 008, tool-failure fallback** all held under fresh execution. Three observations each — doctrine-landing reliable.
- **Refinement-010 failed under fresh execution.** Same input → same leaks. Doctrine-not-landing despite enforcement framing.
- **Refinement-011 authored as strongest single attempt.** Four-element bundle. If Pre-Alpha-6 still leaks, model ceiling acknowledged and operator-side review becomes the production response.
- **Loop discipline lesson:** doctrine has limits. Adding more text past a point produces diminishing returns. The honest operator observation loop must include "what doctrine cannot fix" as a documented category, not just "what new doctrine prevents."

---

## Future entries

Each subsequent observation appends a section here:

- `## Pre-Alpha-6 — Analysis (YYYY-MM-DD)`
- `## Pre-Alpha-7 — Analysis (YYYY-MM-DD)`
- ...

Each entry follows the same structure: source pointer, window, repo state, pattern observations, watch items, direct operator authorizations, disposition.

When patterns repeat across entries, doctrine updates surface in the next refinement cycle (same mechanism as refinement-001 through refinement-011).

---

## Last Updated

2026-05-04 — initial doc authored. Loop architecture established. Five discipline rules locked. Pre-Alpha-1 analysis filed (12 pattern observations + 6 watch items + 3 direct operator authorizations evaluated). One authorization promoted to CLAUDE.md §6 (full-artifact reprint on iteration); two held (PRI breath cadence as wrong doctrine layer; 4–5 cues per exercise as case-context-dependent, awaiting repetition).
2026-05-04 (later) — Pre-Alpha-2 analysis filed (14 pattern observations + 7 watch items + 2 direct operator authorizations evaluated). One authorization promoted to refinement-008 + CLAUDE.md §2 rule 3 + decision-017 fifth amendment ("recommendation closes every gate"); one meta-learning lesson promoted to loop discipline ("pattern claims must be specific about what repeated, not summary counts"). Net signal: refinements 004–007 + §6 Iterative Refinement landed in production cleanly. Refinement-008 emerged as new finding requiring rule 3 sharpening. Pre-session context-budget overflow and Claude.ai 90% session-limit observed as platform constraints separate from doctrine.
2026-05-04 (still later) — Pre-Alpha-3 analysis filed (16 pattern observations + 6 watch items + 1 direct operator authorization evaluated). Doctrine-fidelity test in Josh Max account; budget-realism test type formally distinguished. One authorization promoted to refinement-009 + CLAUDE.md §5 sharpening (internal-identifier leakage prohibition with closed-loop gate exception). Net signal: refinement-008 fully landed in production verbatim across all 3 gates; the canonical Pre-Alpha-2 working-set FAIL surface did not appear; refinement-007 strengthened with tool-failure fallback discipline. Refinement-009 emerged from HL-05 leak (real hard lock, §5 violation in form not substance). Operator observation loop now demonstrably functional: two iterations (Pre-Alpha-2 → refinement-008; Pre-Alpha-3 → refinement-009) showing observation → analysis → doctrine refinement → next-chat behavior change.
2026-05-04 (latest) — Pre-Alpha-4 analysis filed (16 pattern observations + 7 watch items + 1 direct operator authorization evaluated). Doctrine-fidelity test in Josh Max account with 12-week periodization added to the operator's input. One authorization promoted to refinement-010 + CLAUDE.md §7 OUTPUT TRANSLATION enforcement subsection (Internal-Identifier Translation Pass with pre-return scan-and-translate step + handoff line scope). Net signal: refinements 007 + 008 repetition-confirmed; tool-failure fallback discipline repetition-confirmed. Refinement-009 regressed under increased artifact complexity (1 leak in Pre-Alpha-3 → 5 leaks in Pre-Alpha-4). Refinement-010 elevates declaration-layer constraint to enforcement-layer doctrine. Three loop iterations now demonstrate doctrine evolution: Pre-Alpha-2 → refinement-008 (menus); Pre-Alpha-3 → refinement-009 (identifier-leak declaration); Pre-Alpha-4 → refinement-010 (identifier-leak enforcement). Loop is the doctrine-evolution engine — each iteration sharpens; each next iteration tests the sharpening. Meta-learning lesson recorded: declaration-layer doctrine doesn't scale with artifact complexity; fix is enforcement-layer, not stricter declaration.
2026-05-04 (latest²) — Pre-Alpha-5 analysis filed (6 pattern observations + 3 watch items + 2 direct operator authorizations evaluated). Doctrine-fidelity test, fresh run identical to Pre-Alpha-4 input. Two authorizations promoted to refinement-011 four-element bundle: (a) Action Override placement of identifier-translation refusal rule, (b) refusal framing replacing transformation framing in §7, (c) concrete WRONG/CORRECT examples with verbatim Pre-Alpha-4/5 leaks documented in §7, (d) closed-loop exception tightened to two-tier model (specific identifiers allowed; abstract architecture terminology translates). Net signal: refinements 007 + 008 + tool-failure fallback held under fresh execution (third consistent observation). Refinement-010 FAILED under fresh execution — identical 5 leaks recurred. Doctrine has either a placement / framing problem or a model instruction-following ceiling. Refinement-011 is the strongest single doctrine attempt before accepting the ceiling. Pre-Alpha-6 result determines next move. Loop discipline lesson: doctrine has limits; the honest operator observation loop must include "what doctrine cannot fix" as a category alongside "what new doctrine prevents."
