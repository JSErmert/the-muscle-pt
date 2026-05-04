---
doc_id: alpha-state-record-v1
version: v1
date: 2026-05-04
type: milestone state record
purpose: Comprehensive state snapshot of THE MUSCLE PT system at Alpha lock. Primary audience is impartial supervision review (ProjectBrainer); secondary audience is structural review (ultrareview) and the founder (Zach) entering the 1-week production testing window. Frames what is locked, what is intentionally deferred, what is unvalidated, and what review should focus on.
relevant_doctrine:
  - CLAUDE.md (interface doctrine — current state)
  - architecture/operator-observation-loop-v1.md (meta-learning architecture; Pre-Alpha-1 through Pre-Alpha-8 entries)
  - architecture/master-operating-system-governance-bridge-v1.md
  - architecture/governing-logic-v1.md
linked_artifacts:
  - records/research/validation/2026-05-04-pre-alpha-1-zach-usage observation.md through 2026-05-04-pre-alpha-8-seed-usage observation.md (8 fresh-chat doctrine-fidelity runs)
  - records/logs/refinements/refinement-001 through refinement-013 (doctrine evolution arc)
  - records/logs/decisions/decision-001 through decision-017 (architectural decisions)
hl_09_evaluation: PASS — no fabricated grounding. Document is a state snapshot with pointers to source artifacts.
hl_10_evaluation: PASS — addition justified by Alpha milestone framing established in Pre-Alpha-6 (*"that should finish of pre-Alpha right? then true Alpha version will be accomplished"*) and the operator's explicit request for a comprehensive review record (Pre-Alpha-8 close: *"create a record for alpha (as current state, a complete review so that it can be accessed during ultrareview ProjectBrainer)"*). One milestone record per state transition; not an expanding meta-layer.
---

# Alpha State Record v1 — THE MUSCLE PT

## Status

**Alpha locked 2026-05-04.** Pre-Alpha refinement cycle target-complete after 8 fresh-chat doctrine-fidelity tests + 6 doctrine refinements (008–013) + 5 closed-loop disciplines (004–008) + audience-based identifier translation discipline (009–013).

The system is at Alpha when:

1. The 5-mode operator surface (Clinical · Insight · Script · Carousel-deferred · Business) is doctrine-locked and behaves consistently under fresh-chat execution
2. Research Layer (M2) is operational with 10 records authored and the Research Authoring closed loop (10 steps, 3 operator gates) working under HL-09 strict
3. The meta-learning loop (Operator Observation Loop) has demonstrated a complete cycle of observation → pattern detection → doctrine refinement → next-chat behavior change across 7 iterations
4. Pre-Alpha-8 fresh-chat run produced a clean artifact deliverable (zero internal-identifier leaks) AND clean operator-facing surfaces (audience-based discipline landed verbatim)

Alpha is **not**:

- Production-validated by founder. Zach's 1-week testing window comes next.
- Carousel Mode complete. Deferred — built during the 1-week testing window → Beta.
- Iteration depth validated. §6 Iterative Refinement (full-artifact reprint discipline) was promoted from Pre-Alpha-1 but has not been exercised under iteration pressure across Pre-Alpha-2 through Pre-Alpha-8 (each ran a single artifact print).
- Budget-realism validated for Zach's account tier. Pre-Alpha runs all happened in Josh's Max account; Pro-tier session-limit behavior under sustained use is unmeasured beyond Pre-Alpha-2's 90% session-limit observation.

## What this document is

A milestone state snapshot for impartial review at the Alpha lock point. Primary audience is the operator's impartial supervision agent (ProjectBrainer). The document orients an outside-the-loop reviewer to:

- What was built and why
- The doctrine evolution arc (how the system reached this state)
- What's locked vs. what's intentionally deferred vs. what's unvalidated
- What review should focus on, and what is explicitly out of scope

CLAUDE.md is the live doctrine. This record is the *frame* for reviewing it. Reviewers should read CLAUDE.md and the cited refinement files directly; this record exists to navigate them.

---

## System architecture at Alpha

### Doctrine layer (CLAUDE.md)

- **Action Override** — top-of-attention rules: one clear recommendation, no alternatives, no follow-up questions unless required, audience-based internal-identifier discipline (refinements 009–013)
- **Hard Override** — multiple options or explanations = invalid; return only the simplest actionable path
- **§1 System Awareness** — system component inventory
- **§2 Role Mapping** — 5-mode operator surface (Clinical, Insight, Script, Carousel-deferred, Business) with mode activation, Research Authoring as system-triggered capability, Closed-Loop Conversational Discipline (refinements 006–008)
- **§3 System History Usage** — source priority (extracted entries → patterns → raw archive); raw archive at git tag `archive/system-history-2026-05-04` (gitignored on main for context budget)
- **§4 Behavior Rules** — real-world signal over invented ideas, simplicity over complexity, behavior adoption over system introduction
- **§5 Constraints** — what Claude must not do (invent without signal, override hard locks, leak internal identifiers without audience awareness, etc.)
- **§6 Output Style** — clear, structured, actionable; Iterative Refinement subsection (full-artifact reprint per Pre-Alpha-1 operator authorization)
- **§7 Output Translation** — Output Translation Rules v4, Internal-Identifier Translation Pass (audience-based), Translation Guardrail (executable + signal-preserving), Citation Format (M2)
- **§8 Failure Handling** — do not guess; classify as inconclusive; request clarification
- **§9–10 System Alignment + Final Definition**

### Core engines (M1)

- **Movement Case Engine v1 (Core)** → Clinical Mode
- **Content Case Flywheel v1 + Content Output Contract v1** → Insight Mode
- **Exercise-to-Script Lane Spec v1 + Shared Assets v1** → Script Mode
- **Carousel Lane** → deferred, no active doctrine (built during Zach 1-week testing → Beta)
- **Governing Logic v1 + Hard Locks + Prioritization + Queue Engine** → Business Mode

### Research layer (M2)

- **Research to System Mapping v1**
- **Research Layer Bootstrap v1** (First Activation Rule, HL-09 strict, HL-10 strict)
- **Research Index & Traceability v1**
- **Research Query Layer v1**
- **10 research records authored** (research-001 through research-010)

### Meta-system (operator behavior layer)

- **Operator Observation Loop v1** — three-stage loop (observation → pattern detection → doctrine refinement) with 5 discipline rules locked. Architecture doc at `architecture/operator-observation-loop-v1.md` carries Pre-Alpha-1 through Pre-Alpha-8 analytical entries inline.
- **Loop boundary**: between sessions only. No runtime memory layer; no pattern-prediction; no pre-staging from observations. Doctrine refinement is the only mechanism by which observation data shapes runtime chat behavior.

### Hard Locks (HL-01 through HL-10+)

Hard Locks live at `governance/hard-locks-v1.md`. The two HLs that surfaced repeatedly during Pre-Alpha:

- **HL-09**: no fabricated grounding. Verified citations only. Strict throughout the 10-step Research Authoring closed loop.
- **HL-05**: reassess before progressing — driver of the canonical Pre-Alpha-3/4/5 leak surface (HL-05 named in artifact body); resolved across refinements 009–013.

---

## Doctrine evolution arc

The doctrine reached Alpha through 13 refinements + 17 decisions. Refinements 008–013 form the Pre-Alpha refinement cycle and were authored in response to fresh-chat doctrine-fidelity tests.

### Refinements 001–007 (foundational)

| ID | Title | Scope |
|---|---|---|
| 001 | M2 research applies to all lanes | Research Layer cross-cuts content lanes |
| 002 | SED v1 / M3 reordering question | Sequencing question for M3 deferred |
| 003 (a) | Affiliate line specification | Shared Assets v1 detail |
| 003 (b) | Engine name leakage §5 rule | Earliest constraint on engine-name leakage in artifact output |
| 004 | Research Layer vs. Authoring Mode correction | Split passive Research Layer (always-on grounding) from system-triggered Research Authoring |
| 005 | Research Authoring as system-triggered capability | Locked the Research Authoring prompt pattern and gate discipline |
| 006 | Closed-loop conversational discipline | Delivery rhythm: ≤2–3 sentences per step, one question per gate, no procedural narration |
| 007 | Closed-loop turn flow — search before Gate A | PubMed/source search runs silently before the first operator gate; pre-search guessing blocked |

(Note: the two refinement-003 files are a historical naming collision — preserved as-is for traceability.)

### Refinements 008–013 (Pre-Alpha refinement cycle)

| ID | Title | Trigger | Resolution |
|---|---|---|---|
| 008 | Menu discipline — recommendation closes the call | Pre-Alpha-2 working-set bare-menu pattern | Multi-way operator decisions surface ranked options + closing *"Recommend X because Y. Confirm or override."* |
| 009 | Internal-identifier leakage declaration | Pre-Alpha-3 HL-05 leak in artifact closing line | §5 constraint added: engines fire silently; artifact output must translate the principle, not name the identifier |
| 010 | Internal-identifier translation enforcement | Pre-Alpha-4 regression (1 leak → 5 leaks under added periodization complexity) | §7 enforcement subsection: scan-and-translate before return |
| 011 | Action Override translation with refusal framing | Pre-Alpha-5 identical 5-leak recurrence under refinement-010 | Four-element bundle: Action Override placement + refusal framing + concrete WRONG/CORRECT examples + two-tier closed-loop exception (specific identifiers allowed at gates; abstract architecture terminology translates) |
| 012 | Bypass-message + handoff final cleanup | Pre-Alpha-6 substantial landing with two uncovered surfaces (bypass message when record exists; handoff mode-naming) | §7 WRONG/CORRECT extension; Action Override scope language extended; positioned as final Pre-Alpha refinement |
| 013 | Audience-based identifier discipline | Pre-Alpha-7 operator correction surfaced refinement-012 over-translation (record IDs are operator storage pointers) + new HL-X adverbial-justification surface | Identifier discipline divides by reader value, not by surface location. Operator-facing surfaces keep storage pointers + verifiable references; client-facing artifact body translates everything. SUPERSEDES refinement-012 bypass-message rule (handoff mode-naming drop preserved) |

### Decisions

17 architectural decisions span M1 lock through Mode Activation pattern. Most relevant for Alpha review:

- **decision-014** — M2 acceleration with Content Output Contract (parallel-track execution that produced research-001 through 008 + 009)
- **decision-016** — Lane Abstraction for content production (3 lanes: Insight / Script / Carousel-deferred)
- **decision-017** — Mode Activation pattern (5 modes + Research Authoring as system-triggered + 5 amendments mapping to refinements 005, 006, 007, 008)

---

## Pre-Alpha test arc (8 fresh-chat doctrine-fidelity runs)

Each Pre-Alpha test is a fresh-chat run with the same template-builder + 12-week periodization input (Pre-Alpha-2 onward) under the current repo state. Tests run in Josh's Max account (doctrine-fidelity test type) until budget-realism testing begins in Zach's Pro account during Alpha.

| Test | Repo state | Surface tested | Result | Resulting doctrine |
|---|---|---|---|---|
| Pre-Alpha-1 | Through refinement-005 | Zach 26yo case + iterative programming arc (May 3–4) | 12 patterns, 6 watch items, 3 direct authorizations | Full-artifact reprint promoted to §6 Iterative Refinement |
| Pre-Alpha-2 | Through refinement-007 + §6 | Template-builder + ACSM grounding (closed loop full run) | Working-set bare-menu pattern | Refinement-008 (recommendation closes the call) |
| Pre-Alpha-3 | Through refinement-008 | Same template-builder, mode-spanning declaration | HL-05 leak in artifact closing line | Refinement-009 (declaration layer) |
| Pre-Alpha-4 | Through refinement-009 | Same + 12-week periodization added | 5 internal-identifier leaks (regression under complexity) | Refinement-010 (§7 enforcement) |
| Pre-Alpha-5 | Through refinement-010 | Same input | Identical 5-leak recurrence — doctrine not landing | Refinement-011 (four-element bundle) |
| Pre-Alpha-6 | Through refinement-011 | Same input | Substantial landing — 0 HL-X / 0 engine names / 0 research-XXX in artifact body. 2 uncovered surfaces (bypass message + handoff mode-naming) | Refinement-012 (final cleanup) |
| Pre-Alpha-7 | Through refinement-012 | Same input | Clean artifact body. Operator correction surfaced refinement-012 over-translation (record ID is storage pointer) + new HL-X adverbial-justification surface | Refinement-013 (audience-based reframe) |
| Pre-Alpha-8 | Through refinement-013 | Same input | **Clean across all surfaces.** Bypass message + HL-X adverbial framing match refinement-013 CORRECT examples verbatim. Substantive richness increased relative to Pre-Alpha-7. | **Alpha locks** |

The arc demonstrates the operator observation loop functioning: each Pre-Alpha test surfaced a finding; each finding promoted to doctrine; the next test validated the promotion. Refinement scope shrank across iterations as doctrine stabilized.

---

## What's locked at Alpha

### Operator-facing surface

- 5-mode declaration pattern (Clinical, Insight, Script, Carousel-deferred-message, Business) with case-insensitive aliases
- Implicit mode declarations at conversation start (inferred from context if ambiguous)
- Operator switches modes by declaring; system acknowledges and locks
- Mode-spanning workflow recognized: *"Research then Clinical"* / *"first research and then clinical"* (operator-internalized entry pattern from Pre-Alpha-3 onward)

### Research Layer behavior

- Always-on across all modes (passive grounding when significantly informative)
- Research Authoring is system-triggered (never auto-fires; operator authorization at every gate)
- Power-user *"Research Mode"* command preserved for proactive authoring
- 10-step closed loop with 3 operator gates (A: seed selection; B: how-this-applies-to-your-work mapping; C: confidence calibration)
- HL-09 strict throughout (verified citations only; PMID + exact figures verbatim)

### Closed-loop conversational discipline (refinements 006–008)

1. ≤2–3 sentences per step output; no procedural narration
2. One question per gate
3. Recommendation closes every multi-way decision (*"Recommend X because Y. Confirm or override."*) — applies to closed-loop gates AND mid-mode multi-way operator decisions in any mode
4. No pre-emptive caveats — fabrication warnings, scope disclosures surface only when tied to immediate operator decision
5. Action Override preserved throughout
6. Search before Gate A — PubMed/source search runs silently; Gate A presents only verified candidates

### Audience-based identifier discipline (refinements 009–013)

- **Client-facing artifact body** (protocol templates, scripts, content delivered to end clients): translate ALL internal identifiers (HL-X, research-XXX, refinement-XXX, decision-XXX, §X, engine / layer / lane / contract names, test methodology terminology) to readable principle. PMID + source name remain only as citation per §7 Citation Format.
- **Operator-facing surfaces** (gates, bypass messages, system status, mode-transition messages): KEEP storage pointers and verifiable references (research-XXX, PMID, source names, Gate A/B/C naming, HL-X as confirmation-question subject); TRANSLATE HL-X-adverbial / refinement-XXX / decision-XXX / §X / abstract architecture terminology / test methodology terminology.

### Iterative refinement (Pre-Alpha-1)

When the operator iterates on a structured artifact, the system reprints the full updated artifact each turn — not a diff, not a delta summary.

### Hard Locks (HL-01 through HL-10+)

All hard locks at `governance/hard-locks-v1.md` are active and untouched by Alpha doctrine work.

---

## What's deferred (intentional gaps)

1. **Carousel Mode** — `architecture/operator-observation-loop-v1.md` and CLAUDE.md §2 both record this. Status: deferred, no active doctrine. Built when documented repeated need surfaces. Plan: developed by operator (Josh) during Zach's 1-week Alpha testing window; addition + Zach feedback → Beta state record.

2. **Carousel Lane (content)** — distinct from Carousel Mode but coupled. Same deferral rationale (no documented repeated need yet). CLAUDE.md §2 surfaces this.

3. **§6 Iterative Refinement under iteration pressure** — substance is correct (full-artifact reprint each turn) and operator-authorized in Pre-Alpha-1 transcript. Not exercised across Pre-Alpha-2 through Pre-Alpha-8 (each ran one artifact print). Validation deferred to an Alpha-N or Beta-N iteration arc.

4. **Specific HL-X allowances at gates** — refinement-013's audience model narrowed HL-X allowance to "subject of confirmation question" only. The narrower scope hasn't been exercised in production yet because no closed-loop gate during Pre-Alpha-8 surfaced an HL-X-as-subject confirmation. Watch in Alpha.

5. **Account-tier asymmetry methodology** — formally distinguished doctrine-fidelity tests (Josh Max) from budget-realism tests (Zach Pro). Pre-Alpha runs were doctrine-fidelity in Josh's account. Zach's 1-week testing window provides the budget-realism data.

---

## Open watch items (carried to Alpha-N)

These are items the operator observation loop tracks across sessions. None are blockers for Alpha; all are worth surfacing in Alpha-N or Beta-N as relevant.

1. **Mode-pick picker pattern.** Four consistent observations in Pre-Alpha-2/3/4/5 showed *"Which mode?"* rendering as a 3-option picker on Claude.ai web. Doctrine-ambiguous between system menu generation (would violate refinement-006 delivery rhythm) and platform UI affordance over a doctrine-compliant ask. Pattern reliability fully established; root cause undetermined. Alpha-N can confirm by inspecting whether the same pattern appears on Zach's instance — if yes, it's platform UI; if not, doctrine refinement candidate.

2. **§6 Iterative Refinement under iteration pressure.** Unexercised across all Pre-Alpha tests. Watch when an iteration arc fires (5+ refinements on a single artifact).

3. **Substantive output richness scaling with input complexity.** Pre-Alpha-4 had richer ACSM figure extraction than Pre-Alpha-3 because the operator added periodization. Pre-Alpha-8 had richer pre-activation drills + DEVIATION DISCLOSURE block + per-phase tempo than Pre-Alpha-7 with identical input. Two patterns: (a) richer input → richer grounding; (b) doctrine maturation → richer artifact at constant input. Watch whether (b) holds in Alpha-N.

4. **Tool-failure fallback discipline.** Pre-Alpha-3 (PMC blocked → Applied Performance fallback) and Pre-Alpha-4 (Move Your Bones secondary). Two consistent observations of HL-09 verification maintained under degraded tool conditions. Worth promoting to refinement-007 as a recognized sub-pattern if a third observation surfaces in Alpha.

5. **Operator vocabulary drift (Pre-Alpha-1 watch).** Zach typed *"programming"* and *"research"* as standalone responses to *"Which mode?"* in Pre-Alpha-1. Cost: two clarification turns. Alpha-N is the first opportunity to see whether this recurs in Zach's actual production work or whether the picker (now reliably observed) absorbs the vocabulary drift.

6. **Bypass-when-record-exists pattern.** Now three consistent observations (Pre-Alpha-6, 7, 8). Refinement-013 messaging cleanup landed. Watch whether the bypass behavior continues to be appropriate (skipping closed loop when record is sufficient) vs. inappropriate (skipping when a record SHOULD have been re-authored — none observed yet).

7. **Pre-session context-budget overflow** (Pre-Alpha-2 finding). Resolved via tag-archive + gitignore + surgical fix. Architectural takeaway recorded as *"adding everything as if context were infinite is a real failure mode"* — worth a future doctrine touch on what belongs in active project knowledge vs. archive-tag-accessible state.

8. **Session-limit constraint on iteration headroom** (Pre-Alpha-2 finding). Pre-Alpha-2 hit Claude.ai web 90% session-limit after one comprehensive output on Zach's Pro account; Pre-Alpha-3 through 8 ran clean on Josh's Max. If Zach's typical session = one artifact, the limit may not bind; if he iterates, it will. Direct Alpha-N data point.

---

## Review focus questions

These are the questions the operator wants impartial supervision (ProjectBrainer) to answer at Alpha. Order is approximately by leverage.

1. **Audience-based discipline coherence.** Does the audience-based identifier model (refinement-013) introduce any internal contradictions with refinements 009–012, or does it cleanly subsume them? Are there places in CLAUDE.md (Action Override, §5, §7) where the discipline is stated in conflicting terms across sections?

2. **Refinement chain accumulation.** Refinements 009 → 010 → 011 → 012 → 013 are a chain on a single concern (internal-identifier discipline). Is anything in refinements 009–012 now redundant given refinement-013's audience model? Should any be marked as fully superseded vs. partially preserved (refinement-012 currently has the latter)?

3. **Closed-loop discipline at production**. Are refinements 006–008 (closed-loop conversational discipline) over- or under-specified for production use by an operator (Zach) who has not been through the build? What's the smallest set of rules that produces the observed behavior?

4. **CLAUDE.md complexity vs. handoff readiness.** Does CLAUDE.md surface the right complexity for production handoff to a founder who isn't deep in the build? Specifically: is the §2 Closed-Loop Conversational Discipline section (lines ~116–141) appropriate weight, or is it doctrine inflation that should compact?

5. **Meta-learning loop scope.** Does `architecture/operator-observation-loop-v1.md` over-claim what doctrine refinement can do? Refinement-011 explicitly framed a model-ceiling possibility; Pre-Alpha-6 came back as "uncovered cases, not ceiling." Is the loop's framing of doctrine limits honest, or does the architecture document drift toward doctrine-can-fix-everything?

6. **Section consistency across CLAUDE.md.** Action Override + Hard Override + §5 + §7 + §6 Iterative Refinement should all read as one coherent doctrine, not as a sediment of overlapping rules. Where do they overlap, and where could compaction tighten without losing signal?

7. **Pruning candidates.** Are there doctrine sections, refinements, or decisions that the system no longer needs but haven't been pruned? (Particular candidates: the duplicate refinement-003 files; any closed-loop language now subsumed by refinement-013's audience model; any reference patterns that pre-date the audience model.)

8. **What's missing for Alpha→Beta transition.** Given Zach's 1-week testing comes next, what's missing from Alpha that would meaningfully reduce production friction? Specifically: is anything documented in this record actually a Beta dependency masquerading as deferred?

---

## What review should NOT focus on

- **Carousel Mode** — intentionally deferred. Built during Zach's 1-week testing window. Reviewer flagging this as a gap would mean missing the deferral framing.
- **§6 Iterative Refinement substance** — operator-authorized in Pre-Alpha-1; substance is correct; only validation under iteration pressure is unfinished. Reviewer should not propose changes to the substance; only flag validation gaps.
- **Research records 001–010 substance** — HL-09 strict was applied at authoring; PMIDs verified; figures verbatim. Re-validation of research records is out of scope for Alpha review (would require domain expertise outside the system).
- **Pre-session context-budget overflow handling** — resolved via archive tag + gitignore + surgical fix in Pre-Alpha-2. Documented in the operator observation loop. Not a current state issue.
- **Hard Locks substance** — HL-01 through HL-10+ at `governance/hard-locks-v1.md`. Substance is unchanged through Alpha; only the discipline around naming HL-X identifiers in artifact output evolved (refinements 009–013). Reviewer should not propose hard-lock content changes.
- **Doctrine artifacts pre-dating M2 acceleration** — decision-014 onward is the current architectural epoch. Pre-decision-014 records are historical and should not be flagged for revision.
- **Beta-tier features** — Carousel Mode + post-Zach-feedback refinements explicitly belong to Beta. Alpha review should not anticipate or pre-author Beta doctrine.

---

## File index for reviewers

### Read first

1. `CLAUDE.md` — current interface doctrine, top to bottom
2. `architecture/operator-observation-loop-v1.md` — meta-learning architecture + Pre-Alpha-1 through Pre-Alpha-8 analytical entries inline
3. This record (`architecture/alpha-state-record-v1.md`) — Alpha frame

### Read second (doctrine evolution)

4. `records/logs/refinements/refinement-008-menu-discipline-recommendation-closes-the-call.md`
5. `records/logs/refinements/refinement-009-internal-identifier-leakage-in-artifact-output.md`
6. `records/logs/refinements/refinement-010-internal-identifier-translation-enforcement.md`
7. `records/logs/refinements/refinement-011-action-override-translation-with-refusal-framing.md`
8. `records/logs/refinements/refinement-012-bypass-message-and-handoff-final-cleanup.md`
9. `records/logs/refinements/refinement-013-audience-based-identifier-discipline.md`

### Read third (foundational)

10. `records/logs/decisions/decision-017-mode-activation-pattern.md` (5-amendment chain, including the 5 closed-loop discipline refinements)
11. `records/logs/refinements/refinement-004-research-layer-vs-authoring-mode-correction.md`
12. `records/logs/refinements/refinement-005-research-authoring-as-system-triggered-capability.md`
13. `records/logs/refinements/refinement-006-closed-loop-conversational-discipline.md`
14. `records/logs/refinements/refinement-007-closed-loop-turn-flow-search-before-gate-a.md`

### Raw observation data (substantiation)

15. `records/research/validation/2026-05-04-pre-alpha-1-zach-usage observation.md` through `2026-05-04-pre-alpha-8-seed-usage observation.md` — 8 fresh-chat raw transcripts

### Engine docs

16. `execution/movement-case-engine-v1.md` (Clinical Mode)
17. `execution/content-output-contract-v1.md` (Insight Mode)
18. `execution/exercise-to-script-lane-spec-v1.md` (Script Mode)
19. `governance/hard-locks-v1.md` (HL-01 through HL-10+)

### Architecture siblings

20. `architecture/master-operating-system-governance-bridge-v1.md`
21. `architecture/governing-logic-v1.md`

---

## Alpha → Beta milestone path

1. **Alpha lock (now, 2026-05-04)** — this record committed; Zach handoff begins
2. **Zach 1-week production testing** — Alpha-N entries appended to `architecture/operator-observation-loop-v1.md` as observations land
3. **Carousel Mode development (in parallel during Zach testing)** — operator (Josh) authors Carousel Lane spec + Carousel Mode doctrine
4. **Beta state record** — at completion of Zach feedback integration + Carousel Mode lock. Filed at `architecture/beta-state-record-v1.md`. Same structure as this record.

---

## Reviewer pointer back

The operator (Josh) authored this Alpha record on 2026-05-04 immediately after Pre-Alpha-8 produced clean output across all surfaces refinements 008–013 targeted. Review feedback should be returned in whatever format ProjectBrainer's standard output produces. Findings that propose doctrine changes will be evaluated against the operator observation loop's discipline (single-observation rule with stated-rule exception); findings that propose pruning will be evaluated against signal-preservation guardrails (executable + signal-preserving, not just simpler).

If this record itself needs structural revision before review, the operator should flag back before ProjectBrainer is engaged.

---

## Last Updated

2026-05-04 — initial Alpha state record authored. Pre-Alpha-8 fresh-chat run produced clean output across all surfaces refinements 008–013 targeted; refinement-013 audience-based identifier discipline landed verbatim under fresh execution; Pre-Alpha refinement cycle target-complete. Doctrine evolution arc 008 → 009 → 010 → 011 → 012 → 013 cumulatively succeeded; each refinement scope shrank as doctrine stabilized; substantive output richness increased rather than degraded across the arc. Alpha locks for handoff to founder Zach for 1-week production testing while operator develops Carousel Mode in parallel → Beta state record at completion.
