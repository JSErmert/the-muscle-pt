# ProjectBrainer — Alpha Review of THE MUSCLE PT

  **Date:** 2026-05-04
  **Author:** ProjectBrainer (impartial supervision agent — Claude reviewing
  Claude; caveat per the brief)
  **Operator:** Josh
  **Founder:** Zach
  **Scope:** Alpha state record v1 + brief v1 + CLAUDE.md + refinement-013 +
  refinement-008 + Pre-Alpha-2 raw + Pre-Alpha-8 raw.
  Operator-observation-loop-v1 was sampled but not read in full (file
  exceeded a single-read budget). Where I rely on the loop's claims I cite
  the Alpha record's framing of them and verify against the raw Pre-Alpha
  transcripts I did read.

  ---

  ## TL;DR — committed call, no split-the-difference

  1. **Refinement-013 is the right doctrine and Pre-Alpha-8 validates it on
  the surfaces tested.** The audience-based reframe is what the principle
  should have been from the start, and the operator's own loop-discipline
  lesson on this is correctly stated.
  2. **The "Alpha-ready, 5-mode operator surface validated under fresh-chat
  execution" claim overreaches the data.** What was actually validated under
  fresh-chat conditions is Clinical Mode + the Research Authoring closed
  loop's bypass branch (when a record is already locked). Insight Mode,
  Script Mode, and Business Mode have **zero fresh-chat test data**. The
  Research Authoring closed loop's *live* branch (when a record is being
  authored from scratch) has been validated **once** — Pre-Alpha-2 — on a Pro
   account that hit 90% session-limit and was not retested.
  3. **Pre-Alpha-2 and Pre-Alpha-8 are not the same test.** Pre-Alpha-2 had
  no mode pre-declaration, no periodization, and ran Research Authoring live.
   Pre-Alpha-8 had `"Research mode, then Clinical mode:"` as an operator
  pre-declaration AND added a 12-week periodization clause AND bypassed
  Research Authoring entirely (research-010 was already locked). The
  narrative "doctrine evolution arc 008→013 cumulatively succeeded on the
  same input" rests on a comparison the data does not support. The arc *did*
  succeed on the artifact-translation surface; the comparison framing
  inflates it.
  4. **CLAUDE.md is doctrine-inflated.** The audience-based identifier
  taxonomy appears in three places (Action Override line 24, §5 line 294, §7
  lines 333–406) in three slightly different phrasings. That is three sources
   of truth for one rule. This is the highest-leverage pruning candidate.
  5. **Refinement-012's status note is wrong by your own doctrine.**
  Refinement-013 explicitly SUPERSEDES refinement-012's bypass-message rule.
  Refinement-012's own header should reflect
  "BYPASS-MESSAGE-RULE-SUPERSEDED-by-013; HANDOFF-DROP-PRESERVED." Right now
  it reads as fully active. Refinements 009-011 are *substantively* preserved
   but should be marked "principle-subsumed-by-013,
  mechanics-preserved-as-historical-record" so a future reader doesn't
  mistake the chain for live doctrine.
  6. **The biggest Alpha→Beta risk is one you've already flagged but haven't
  sized: budget realism on Zach's Pro account.** Pre-Alpha-2's 90%
  session-limit hit after a single comprehensive output is not a watch item;
  it's a structural finding. CLAUDE.md is ~485 lines plus the rest of the
  project knowledge. If Zach's typical session = one comprehensive output,
  Pro may bind before Alpha is meaningfully tested in production. This
  deserves a dedicated test before Zach's 1-week window opens, not after.
  7. **Carousel Mode deferral is operator-avoidance dressed as need-driven
  deferral.** The brief admits this is a possibility; I'm taking the call.
  Carousel is the highest-leverage Insight format on social. "No documented
  repeated need" is true because the system has been operator-tested, not
  founder-used. The deferral defers a doctrine surface you don't yet know how
   to constrain.

  The honest read: **doctrine-fidelity Alpha is genuinely achieved on the
  surfaces tested. Production-readiness Alpha is not.** Whether your lock
  decision is appropriate depends on which one "Alpha" was meant to mean. The
   Alpha state record's `Alpha is not:` list (lines 33–38) already concedes
  most of this — but the lock decision and the framing in the rest of the
  document treat doctrine-fidelity Alpha as the lock condition. That gap is
  the operator narrative outpacing the data.

  ---

  ## 1. Project maturity — actual vs. narrative

  **Narrative position (per Alpha state record):** Pre-Alpha cycle
  target-complete; 5-mode operator surface doctrine-locked; meta-learning
  loop demonstrated complete cycles across 7 iterations; Alpha locks for
  handoff to founder.

  **Actual position, calibrated against the raw transcripts:**

  | Surface | Validation status | Evidence |
  |---|---|---|
  | Clinical Mode artifact body (template-builder input) | Validated |
  Pre-Alpha-3→8, all clean by Pre-Alpha-8 |
  | Research Authoring closed-loop *bypass* branch | Validated (3
  observations) | Pre-Alpha-6, 7, 8 with research-010 pre-locked |
  | Research Authoring closed-loop *live* branch | Validated **once**, on a
  session-limit-binding account | Pre-Alpha-2 only; PMID 41843416 was
  authored there |
  | Recommendation-closes-the-call (refinement-008) | Validated
  (Pre-Alpha-3→8) | Working-set decision held verbatim across 6 tests |
  | Audience-based identifier discipline (refinement-013) | Validated
  **once** | Pre-Alpha-8 only — the rest of the chain validated 009–012,
  which 013 reframed |
  | §6 Iterative Refinement (full-artifact reprint under iteration pressure)
  | **Unvalidated** | Pre-Alpha-1 authorized the rule; no Pre-Alpha test ran
  an iteration arc |
  | Insight Mode | **Untested under fresh execution** | No Pre-Alpha record |
  | Script Mode | **Untested under fresh execution** | No Pre-Alpha record |
  | Business Mode | **Untested under fresh execution** | No Pre-Alpha record
  |
  | Carousel Mode | Deferred (intentional) | No doctrine to test |
  | Budget realism on Pro account | **Validated negatively, not retested** |
  Pre-Alpha-2 hit 90% session-limit |
  | Different-input class on Clinical Mode | **Untested** | All Pre-Alpha-2→8
   ran the same template-builder; case-classification, intervention-design,
  programming-for-individual-clients are core Clinical Mode surfaces and none
   have fresh-chat data |

  **Calibrated position:** This is a doctrine-fidelity Alpha for *one mode on
   one input class on one account tier*. That is a real achievement — the
  doctrine demonstrably constrains a fresh Claude instance to produce
  consistent professional-grade output on the surface tested. It is also a
  narrower validation surface than the doctrine-lock framing implies.

  **On the operator narrative:** The Alpha state record's `What's locked at
  Alpha` list (lines 158–196) lists the 5-mode operator surface as locked.
  *Doctrine* for the 5-mode surface is locked — i.e., the doctrine documents
  specify what each mode does. *Behavior* of the 5-mode surface under
  fresh-chat execution is not validated; only Clinical Mode behavior is.
  Recommend the §1 of the Alpha state record distinguish "doctrine-locked"
  from "validated under fresh execution" as orthogonal claims, not a single
  bundle.

  ---

  ## 2. Findings against the 8 review focus questions

  ### 2.1 — Audience-based discipline coherence

  **Q (Alpha state record §6.1):** Does the audience-based identifier model
  (refinement-013) introduce internal contradictions with refinements
  009–012, or does it cleanly subsume them?

  **Finding:** Cleanly subsumes the *principle*. Does NOT cleanly subsume the
   *doctrine surface presentation* — the audience taxonomy is restated in
  three different phrasings in CLAUDE.md (Action Override line 24, §5 line
  294, §7 lines 333–406) and again in five different refinement files (009,
  010, 011, 012, 013). The principle is consistent across all six surfaces;
  the wording is not. Three minor inconsistencies I noticed:

  - Action Override line 24 calls them "client-facing artifact body" vs.
  "operator-facing surfaces"; §5 uses the same wording; §7 uses
  "Client-facing artifact body" + "Operator-facing surfaces" as section
  headers (cosmetically same, structurally different).
  - The HL-X-as-confirmation-question allowance is stated as "subject of a
  confirmation question" in §7 line 361 and Action Override line 24, but as
  "the subject of a confirmation question" in refinement-013 line 71.
  Functionally identical; not a contradiction; a future reader will read this
   as three rules and ask which is canonical.
  - The list of what translates in operator-facing surfaces is stated
  identically in three places — which means a doctrine update has to be made
  in three places. Drift risk is real over Beta+.

  **Recommendation:** Single source of truth in §7. Action Override and §5
  reduce to one sentence each + pointer. Saves ~15 lines of CLAUDE.md and
  removes drift risk.

  ### 2.2 — Refinement chain accumulation

  **Q (Alpha state record §6.2):** Is anything in refinements 009–012
  redundant given refinement-013?

  **Finding:** Yes, more aggressively than the operator's framing admits.

  - **Refinement-009** (declaration that internal-identifier leakage is
  wrong): subsumed by 013. The principle "audience determines what
  translates" makes 009's "engines fire silently" framing a special case
  (client-facing artifact body translates everything).
  - **Refinement-010** (§7 enforcement scan-and-translate): the
  scan-and-translate *mechanism* is preserved; the *rules* it enforces are
  the audience-based ones from 013. 010's content is now scaffolding around
  013's rule.
  - **Refinement-011** (Action Override placement + refusal framing +
  WRONG/CORRECT examples + two-tier closed-loop exception): refinement-013
  explicitly reframes the two-tier exception as audience-based. The Action
  Override placement and refusal framing are still correct; the WRONG/CORRECT
   examples have been corrected by 013 (the bypass-message CORRECT was wrong
  in 011's lineage).
  - **Refinement-012** (bypass-message + handoff cleanup): 013 SUPERSEDES the
   bypass-message rule. The handoff mode-naming drop is preserved.
  Refinement-012 is currently in a half-superseded state — its file's status
  header (line 6, the `status:` field) does NOT reflect that the
  bypass-message CORRECT example is wrong.

  **Recommendation:**
  - Mark 009, 010, 011 with a header note: "Principle subsumed by
  refinement-013 audience-based discipline. Preserved as historical record of
   the surface-by-surface scaffolding that refinement-013 reframed."
  - Mark 012 with a header note: "Bypass-message rule SUPERSEDED by
  refinement-013. Handoff mode-naming drop preserved." Update the `status:`
  field accordingly.
  - Don't delete the files. The chain *is* the meta-learning loop's training
  data; deleting it removes the evidence that scaffolding was the path. But
  mark the supersession explicitly so a future reader doesn't read 011's
  WRONG/CORRECT examples as authoritative.

  **Operator-bias correction:** The brief admits the contrarian read that
  009–012 are dead doctrine retained out of sunk-cost. My read: not dead;
  demoted. The chain has training-data value for the loop discipline itself.
  Sunk-cost preservation would be claiming they're still load-bearing.
  Demoting them with explicit supersession captures the actual epistemic
  state.

  ### 2.3 — Closed-loop discipline at production

  **Q (Alpha state record §6.3):** Are refinements 006–008 over- or
  under-specified for production use by an operator who has not been through
  the build?

  **Finding:** Over-specified for daily use, appropriately specified for
  Research Authoring.

  The discipline (≤2-3 sentences per step, one question per gate,
  recommendation closes the call, no pre-emptive caveats, Action Override
  preserved, search before Gate A) was authored against Research Authoring
  sessions. Pre-Alpha-2's working-set turn was the canonical FAIL example —
  and that turn was inside Research Authoring. The validation surface for
  refinements 006–008 is *Research Authoring rhythm*.

  The doctrine then extends rule 3 (recommendation closes the call) to
  "mid-mode multi-way operator decisions in any mode" (CLAUDE.md line 122).
  That extension has not been tested. Pre-Alpha-2→8 only exercised the rule
  inside Research Authoring or its bypass.

  The risk for Zach: rule 1 (≤2-3 sentences per step) and rule 4 (no
  pre-emptive caveats) are tight constraints. Real clinical reasoning may
  legitimately require more than 2-3 sentences per step (a complex case
  classification doesn't compress; the discipline says it should). The
  discipline's correctness against Research Authoring rhythm doesn't transfer
   cleanly to clinical reasoning rhythm.

  **Recommendation:**
  - Scope rule 1 (≤2-3 sentences per step) explicitly to closed-loop steps
  and gate questions, NOT to Clinical Mode case reasoning.
  - Test rule 3's extension to mid-mode decisions during Zach's window. If
  clinical case work surfaces multi-way decisions where Zach wants the system
   to *not* take the call (because the call belongs to him as the clinician),
   the rule needs an exception.

  The smallest set that produces the observed Pre-Alpha behavior is probably
  rule 3 + rule 6 (search before Gate A) + Action Override. Rules 1, 2, 4, 5
  are correctness conditions for the rhythm but not behavior-shaping rules in
   the way 3 and 6 are.

  ### 2.4 — CLAUDE.md complexity vs. handoff readiness

  **Q (Alpha state record §6.4):** Is §2 Closed-Loop Conversational
  Discipline section appropriate weight, or is it doctrine inflation?

  **Finding:** Inflation.

  §2's Closed-Loop Conversational Discipline subsection (CLAUDE.md lines
  116–141) is ~26 lines. The substantive rules are 6 short principles. The
  rest is tight-pattern + bloated-anti-pattern + scope notes +
  cross-references. That's onboarding material, not run-time doctrine. The
  fresh-chat instance reads it once at session start; the operator reads it
  never (he wrote it).

  Compounding this, the Mode Activation table (lines 81–94), the Research
  Authoring Prompt subsection (lines 96–108), and the Power-User Reference
  subsection (lines 110–114) are all also onboarding-shaped. The actual
  *behavior-shaping* content of §2 is the table + the closed-loop rules. The
  rest is "here's how this works" — appropriate in architecture
  documentation, expensive in run-time doctrine that consumes context budget
  on every session.

  **Recommendation for handoff readiness:**
  - Compact CLAUDE.md to ~250 lines preserving: Action Override (1 sentence +
   pointer to §7), Hard Override, Core Principle, §1 System Awareness (table
  only), §2 Mode Activation table + ≤6 closed-loop rules without examples, §4
   Behavior Rules, §5 Constraints (compact), §7 Output Translation (full —
  this is the load-bearing section), §8 Failure Handling, §9–10.
  - Move tight-pattern + bloated-anti-pattern examples + WRONG/CORRECT pairs
  to a new file `architecture/claudemd-doctrine-companion.md` referenced from
   CLAUDE.md by pointer. The doctrine companion lives in project knowledge;
  the run-time CLAUDE.md is half the size.
  - This is non-trivial work but it is the single highest-leverage
  handoff-readiness move. CLAUDE.md size compounds with Carousel Mode
  addition during Beta.

  ### 2.5 — Meta-learning loop scope

  **Q (Alpha state record §6.5):** Does the operator-observation-loop
  architecture over-claim what doctrine refinement can do?

  **Finding:** The loop's framing is mostly honest. Two specific drift risks:

  - **Self-sealing risk** (already flagged in the brief): the loop catches
  what the operator notices. Refinements 009→013 are evidence the loop *can*
  catch operator-noticed surfaces. They are not evidence the loop catches
  non-noticed surfaces. The architecture document's loop-completeness claims
  (per the Alpha record's framing of "demonstrated a complete cycle of
  observation → pattern detection → doctrine refinement → next-chat behavior
  change across 7 iterations") describe what happened on the noticed-surface
  side. Recommend the architecture doc add an explicit limitation: "the loop
  has no mechanism for unnoticed failures."
  - **Doctrine-can-fix-everything drift** (refinement-011 explicitly framed a
   "model ceiling" possibility that didn't fire): refinement-011 said *"if
  Pre-Alpha-6 still leaks → model ceiling acknowledged."* Pre-Alpha-6 was
  clean on the original surface but had two new uncovered surfaces. The
  operator records this as "ceiling framing was premature." The contrarian
  read: the ceiling framing was right, *and* refinements 012/013 were the
  correct doctrine moves anyway. These are not exclusive. The honest framing
  is "Pre-Alpha-6 closed the original surface (which 011 had targeted); two
  new surfaces opened that were not predicted; doctrine extension was
  warranted because the new surfaces had legitimate principle-level
  resolutions." That is *not* "ceiling framing was premature" — it is "the
  surface count was undercounted, and the ceiling test was on a different
  surface than the one that surfaced."

  **Recommendation:** The loop architecture doc should distinguish
  "surface-resolved" from "ceiling-tested." Refinements 011 and 013 each
  resolved a surface; neither tested the ceiling because the test conditions
  for "ceiling reached" require the *same* surface to recur after a
  refinement — and Pre-Alpha-6 didn't have that condition (new surfaces, not
  the old ones). The "ceiling framing was premature" line in the loop's
  narrative is doctrine optimism: it reads "we didn't hit the ceiling"
  instead of "we didn't run the ceiling test."

  ### 2.6 — Section consistency across CLAUDE.md

  **Q (Alpha state record §6.6):** Where do Action Override + Hard Override +
   §5 + §7 + §6 Iterative Refinement overlap, and where could compaction
  tighten?

  **Finding:** Six concrete overlaps:

  1. **Audience-based identifier discipline** appears in Action Override
  (line 24), §5 (line 294), §7 (lines 333–406). Three sources of truth.
  *Highest-leverage compaction.*
  2. **"Simplicity" / "no alternatives" / "one clear path"** — Action
  Override (lines 19–23), Hard Override (lines 32–33), §6 (lines 305–311), §7
   (lines 322–331), Translation Guardrail (lines 410–418). Five touches of
  the same principle. The Translation Guardrail is the most rigorous
  formulation ("executable + signal-preserving") and should be the canonical
  statement; the others compact to pointers.
  3. **"Real-world signal over invented ideas"** — §4 (line 273), §5 first
  bullet (line 285), §7 Translation Guardrail (line 414). Three touches.
  4. **HL-09 / verified citations** — §7 Citation Format (lines 422–440), §5
  (implicit via "invent content without signal"), Action Override
  (audience-based discipline references it). The Citation Format is the
  canonical statement; the others should pointer-reference.
  5. **Closed-loop discipline location** — §2 contains the rules (lines
  116–141); the Mode Activation table (lines 81–94) references it;
  refinements 006/007/008 are footnoted. The §2 location is appropriate; the
  cross-reference density is fine. Not a compaction candidate.
  6. **Mode-spanning request handling** — §2 Defaults (line 92) says
  "complete one mode's work first, signal the transition, then pick up the
  second on operator confirmation." This rule has been
  **operator-internalized as the `"Research mode, then Clinical mode:"`
  prefix pattern** (Pre-Alpha-3 onward through Pre-Alpha-8). The doctrine
  doesn't surface this as a recognized pattern; the operator does. Worth
  promoting to doctrine in §2: "operator may pre-declare mode-spanning
  workflow with `"Mode A, then Mode B:"` prefix; system locks A first,
  signals transition, locks B on completion." This codifies what the system
  already does and gives Zach an affordance Josh has internalized.

  **Recommendation:** Compact CLAUDE.md by collapsing 1–4 onto canonical
  sources of truth. Promote the mode-spanning prefix pattern in 6 to
  doctrine.

  ### 2.7 — Pruning candidates

  Concrete list, by file:

  | Item | File / location | Action |
  |---|---|---|
  | Audience taxonomy duplication (3x) | CLAUDE.md Action Override line 24,
  §5 line 294, §7 lines 333–406 | Single source of truth in §7; compact
  others to pointers. ~15 lines saved. |
  | Tight-pattern / bloated-anti-pattern examples | CLAUDE.md §2 lines
  127–141 | Move to `architecture/claudemd-doctrine-companion.md`. ~15 lines
  saved. |
  | WRONG/CORRECT examples in §7 | CLAUDE.md §7 lines 369–406 | Move to
  companion doc; keep one canonical pair in §7. ~30 lines saved. |
  | Refinement-009, 010, 011 status | their `status:` fields | Mark
  "Principle subsumed by refinement-013, mechanics preserved as historical
  record" |
  | Refinement-012 status | its `status:` field | Mark "Bypass-message rule
  SUPERSEDED by 013; handoff mode-naming drop preserved" |
  | Duplicate refinement-003 files |
  refinement-003-engine-name-leakage-section-5-rule.md AND
  refinement-003-affiliate-line-specification.md | Reissue one as
  refinement-014 (or rename to 003a/003b with explicit cross-reference); the
  duplicate naming is a real archeological hazard for a future reader |
  | §6 Iterative Refinement rule | CLAUDE.md lines 312–316 | Either
  acknowledge "operator-authorized but unvalidated under iteration pressure"
  inline, or move the rule to architecture/observations until validated.
  Don't ship a doctrine rule as live when it has zero fresh-chat validation.
  |
  | Refinement-007 (search before Gate A) |
  records/logs/refinements/refinement-007-... | NOT a pruning candidate. The
  search-before-Gate-A rule is a substantive tight-pattern lock, distinct
  from refinement-008's menu discipline. Both are needed. (I checked this
  carefully — refinement-008 explicitly preserves rule 6 from
  refinement-006/007.) |

  ### 2.8 — What's missing for Alpha→Beta

  **Highest-leverage missing items, ranked:**

  1. **Budget-realism test on Zach's Pro account before the 1-week window
  opens.** Pre-Alpha-2's 90% session-limit hit was on a different doctrine
  state (through refinement-007). Re-run the same template-builder input on
  Pre-Alpha-8 doctrine on Zach's Pro account. If the limit binds before
  completion, you have a Beta-blocker that masquerades as deferred. If it
  doesn't bind, the watch item closes. Either way, you need this datum before
   Zach starts. Cost: one fresh-chat session + one 70k-token output cycle on
  Pro. Value: the entire 1-week window's signal quality depends on knowing
  whether Zach is operating under budget pressure.

  2. **One Insight Mode fresh-chat test and one Script Mode fresh-chat test
  under doctrine-fidelity conditions.** Same operator, same Max account,
  fresh chat, real input that exercises each mode end-to-end. These are
  claimed to be doctrine-locked; doctrine-locked without behavior-validation
  is not the same epistemic state as Clinical Mode is in. Two tests; ~3 hours
   of operator time; closes the largest validation gap.

  3. **One iteration-arc test of §6 Iterative Refinement.** Pre-Alpha-1
  authorized the rule; no Pre-Alpha test ran more than one artifact print.
  Run a 5-iteration arc on a single artifact (template-builder, then 5
  modifications). Validates whether the full-artifact reprint discipline
  holds under iteration pressure. ~2 hours of operator time.

  4. **Carousel Mode is a Beta dependency masquerading as deferred.** The
  deferral framing is "no documented repeated need." That framing is
  structurally biased — the system has only been operator-tested on a
  template-builder input. *Of course* there is no documented repeated need
  for Carousel: the validation surface didn't include Insight content
  production. Carousel is the highest-leverage social format. Recommend
  either (a) admit Carousel is Beta-blocking and author at least a Carousel
  Lane spec before Zach starts, or (b) explicitly exclude social Carousel
  content from Zach's 1-week window so the deferral doesn't quietly become a
  production gap. Halfway is the worst position.

  5. **Operator vocabulary discovery test for Zach.** Pre-Alpha-1 already
  showed Zach's "programming" / "research" vocabulary cost two clarification
  turns. Has Zach been briefed on the mode-declaration patterns? If not, his
  first session will surface vocabulary drift you've already observed once.
  Recommend: 30-minute Zach onboarding on the mode commands + the
  mode-spanning prefix pattern + the closed-loop rhythm. If "Zach handles his
   account on his own" is the framing, the vocabulary drift will land as
  friction in the 1-week window.

  ---

  ## 3. Meta-realizations the operator can't see from inside

  ### 3.1 — Pre-Alpha-2 and Pre-Alpha-8 are not the same test

  This is the highest-leverage meta-realization in the review.

  The Alpha state record's Pre-Alpha test arc table (lines 142–152) frames
  Pre-Alpha-2 onward as "the same template-builder + 12-week periodization
  input." Reading the raw transcripts:

  - **Pre-Alpha-2 input** (from the raw transcript I read): no `"Research
  mode, then Clinical mode:"` prefix; no periodization clause; ended at
  "based on ACSM updated guidelines. Provide a 2-day, 3-day, 4-day, 5-day
  split structure as the guiding templates that I can build and modify
  details upon and utilize to make specific to future client needs. Also
  standardize cues accordingly, points of contact, maintaining a relative
  stack, proper breath control, tempo if applicable, that can be applied
  across all modalities." Mode declaration was operator-prompted ("Which
  mode?").
  - **Pre-Alpha-8 input** (from the raw transcript I read): begins with
  `"Research mode, then Clinical mode:"`; ends with "Periodization weeks 1-4
  perfect down the technique. Weeks 5-8 progressive overload weight in reps.
  Weeks 9-12 increase intensity push limits." Mode declaration was operator
  pre-declared as a mode-spanning workflow.

  Three structural differences:

  1. **Mode declaration:** Pre-Alpha-2 had no pre-declaration, surfaced the
  picker pattern, required clarification. Pre-Alpha-8 had pre-declaration, no
   picker.
  2. **Research Authoring branch:** Pre-Alpha-2 ran the *live* branch (search
   → Gate A → Gate B → Gate C → lock). Pre-Alpha-8 ran the *bypass* branch
  ("research-010 already locked from a prior session"). These are different
  code paths in the doctrine.
  3. **Input complexity:** Pre-Alpha-8 added periodization (which appears as
  an additional Block 3 PERIODIZATION — 12-WEEK ARC table in the artifact).
  Pre-Alpha-2 did not have this output.

  The "doctrine evolution arc 008→013 cumulatively succeeded under fresh
  execution on the same input" is therefore an over-claim. What is true: the
  doctrine evolved across the surfaces that were exposed by the changing
  tests. What is not true: the doctrine "cumulatively succeeded" on a
  controlled input. The variable that changed across Pre-Alpha-2→8 is not
  just doctrine state; it is also test conditions.

  **Implication for the loop's epistemic claim:** the loop's "validate that
  the update took effect" mechanism (Alpha state record line 154) requires
  the next test to surface the same condition the previous test surfaced.
  Pre-Alpha-3→4→5 did this on the artifact-translation surface (same
  complexity, same leak class, doctrine landing). Pre-Alpha-7→8 did NOT do
  this on the bypass-message surface, because Pre-Alpha-8 added periodization
   and pre-declared mode-spanning. The "Pre-Alpha-8 = clean" datum is real
  but the test conditions changed enough that Pre-Alpha-7 → Pre-Alpha-8 is
  not a clean A/B for refinement-013 alone.

  This doesn't invalidate refinement-013. It does mean the validation surface
   is "refinement-013 + mode-pre-declaration + periodization complexity," not
   "refinement-013 in isolation."

  ### 3.2 — The Research Authoring closed loop has been validated *live*
  exactly once

  Pre-Alpha-2 was the only fresh-chat test that exercised the closed loop's
  live branch (search → Gate A → Gate B → Gate C → lock). That test:

  - Was on Zach's Pro account, doctrine state through refinement-007 (i.e.,
  before refinements 008, 009, 010, 011, 012, 013 existed)
  - Hit 90% session-limit
  - Surfaced the working-set bare-menu pattern that became refinement-008
  - Was not retested under any subsequent doctrine state (because
  research-010 was now locked in project knowledge)

  Pre-Alpha-3→8 all ran the *bypass* branch. The closed loop's live tight
  pattern (CLAUDE.md lines 127–135 — "[System silently: gap → query →
  PubMed/source search → verification] → System: Research Mode locked. Found:
   ... Lock as research-XXX seed?") has been validated **once**, in a state
  of doctrine that is no longer current.

  **Implication:** The doctrine refinements 008, 009, 010, 011, 012, 013 have
   not been validated against the live closed loop. They have been validated
  against the bypass branch + the artifact body. If Zach asks for grounding
  on a topic NOT covered by research-001→010, the closed loop fires live, and
   the live branch is running on un-revalidated doctrine.

  This is a meaningful validation gap. The Alpha state record does not flag
  it. The brief does not flag it. Recommend: one Pre-Alpha-9 or Alpha-1
  fresh-chat test that triggers the live closed loop on a topic outside the
  existing research records. Zach's first novel grounding request is
  otherwise the live test.

  ### 3.3 — The validation surface is one-mode-one-input-class. The doctrine
  surface is five-modes-many-inputs.

  This compounds with 3.2. The doctrine specifies five modes; the validation
  has tested one. The doctrine specifies many input classes for Clinical Mode
   (case classification, root cause, intervention logic, reassessment per
  CLAUDE.md lines 152–155); the validation has tested one (template-builder).
   The ratio of validated surface to doctrinal surface is ~1:20.

  The Alpha state record's `Alpha is not:` list (lines 33–38) concedes some
  of this ("Iteration depth validated"; "Budget-realism validated for Zach's
  account tier"). It does not concede the mode-coverage gap or the
  input-class gap within Clinical Mode.

  **Implication:** the more accurate framing is "Alpha doctrine is locked;
  Alpha validation is partial." This is not a blocker for handoff — Zach's
  1-week window is the validation phase. But it should be the framing, so
  that what Zach surfaces is read as *first-time validation data*, not
  *regression*.

  ### 3.4 — The bypass-message has only ever been observed in the
  operator-authoring sequence; Zach's experience may not match

  The bypass-message-when-record-exists pattern has three observations
  (Pre-Alpha-6, 7, 8). All three are in the *same fresh-chat structure*:
  operator opens chat, project knowledge contains research-010, operator runs
   the template-builder request, system finds research-010, bypasses Research
   Authoring, builds protocol.

  Zach starts cold. His project knowledge is the same repo, but his behavior
  is different. Will Zach trigger Research Authoring on a topic that *isn't*
  in research-001→010? Likely yes — he's a practicing PT with clinical input
  outside RT prescription. So Zach's first novel-topic Clinical request will
  run the live closed loop, not the bypass. That's the test that's been run
  once (Pre-Alpha-2) on doctrine state through refinement-007.

  **Implication:** the bypass-message validation (Pre-Alpha-6, 7, 8) is
  over-fit to operator behavior. It is the dominant Pre-Alpha datapoint and
  it is the path Zach is least likely to take in his first sessions. The
  brief flags "operator-internalized affordances that won't transfer" — this
  is the most concrete instance.

  ### 3.5 — The doctrine-as-coping read has one specific signal

  The brief itself raises this: "when the operator hits ambiguity, the
  response has often been 'author a refinement.'" My read of the data:

  - Refinement-008: substantive new rule (recommendation closes the call).
  Fired on a real bare-menu observation. Genuine doctrine extension.
  - Refinement-009: declaration that internal-identifier leakage is wrong.
  Fired on Pre-Alpha-3's HL-05 leak. Genuine.
  - Refinement-010: §7 enforcement scan-and-translate. Fired because
  refinement-009's declaration didn't reduce leak count under added
  complexity. Reasonable extension.
  - Refinement-011: Action Override placement + refusal framing. Fired
  because refinement-010 didn't reduce identical leak count. The four-element
   bundle (Action Override placement + refusal framing + concrete
  WRONG/CORRECT + closed-loop exception) was reasonable but reads as "throw
  everything at it."
  - Refinement-012: bypass-message + handoff cleanup. Fired on uncovered
  surfaces, not regressions on the original surface. Two separate surfaces
  bundled into one refinement.
  - Refinement-013: audience-based reframe. Fired on operator correction of
  refinement-012's bypass-message rule. Reframed 009-012 to a unifying
  principle.

  Refinements 011 and 012 are the most defensible doctrine-as-coping
  candidates:

  - **011's four-element bundle**: this is what diminishing returns looks
  like on a single concern. The previous refinement didn't land; throw four
  more elements at it. That's not a clean doctrine move; it is "I don't know
  which of these is load-bearing, so I'll do all four."
  - **012's bypass-message rule was wrong by the operator's own subsequent
  doctrine**. It was authored, landed in CLAUDE.md, was tested in
  Pre-Alpha-7, surfaced as over-translation via operator correction, was
  superseded by 013. That's a one-test cycle of authoring a wrong rule. Not
  catastrophic (the loop caught it within one cycle), but it is
  doctrine-as-coping on the way through.

  **My honest read:** 008 is genuine doctrine maturation. 009 is genuine. 010
   is reasonable. 011 starts to look like coping. 012 was a wrong rule
  authored under coping pressure (the cycle was supposed to be ending, the
  operator authored 012 framed as "final cleanup"). 013 is the actual
  doctrine and probably should have been the rule from refinement-009 onward.

  **The contrarian read the operator may not want:** the right move at
  refinement-011 was probably "stop, run Pre-Alpha-6, see what Pre-Alpha-6
  surfaces, decide based on data." Instead, refinement-011 explicitly framed
  a model-ceiling possibility, Pre-Alpha-6 came back clean on the original
  surface, the cycle continued. That's a structurally healthy pattern (one
  more cycle to verify) up to a point. The point at which it became coping
  was 012 — a refinement authored as "final cleanup" that had to be reframed
  by 013. By 012, the loop had four observations confirming refinement-011
  landed; the right call was probably "lock Alpha now, surface bypass-message
   + handoff in Alpha-N as observation tasks, don't author 012."

  This is one possible read; the other is "012 + 013 are the loop functioning
   correctly, catching surfaces and reframing the principle." Both are
  consistent with the data. I'm flagging that the first read is at least as
  well-supported as the second. The operator's narrative is the second; the
  brief admits the first as possible; I'm taking the call that the first is
  the more honest framing. Don't split the difference.

  ### 3.6 — CLAUDE.md is its own future risk

  CLAUDE.md is ~485 lines as of Alpha. The audience taxonomy appears 3x.
  Tight-pattern + bloated-anti-pattern examples are in §2 and §7. The
  Carousel Mode addition during Beta will add another section. By the time
  Beta locks, CLAUDE.md is plausibly 600+ lines. The Pre-Alpha-2
  session-limit hit was on a doctrine state ~360 lines (through
  refinement-007) on Pro. Doctrine inflation is a Beta blocker before it is a
   Beta cleanup task.

  The compaction described in §2.4 + §2.6 + §2.7 is the highest-leverage
  pre-Beta work the operator can do. ~60 lines saved without behavioral
  degradation. Tested by hypothetical: if the Pre-Alpha-8 fresh-chat run had
  been on the compacted CLAUDE.md instead of the current one, would the
  doctrine have landed? The answer depends on whether the
  audience-taxonomy-3x is *behavior-shaping* through repetition or
  *just-in-case redundancy*. If the latter (most likely), the compaction is
  safe. If the former, the compaction needs validation. Either way, you can't
   know without running it.

  ---

  ## 4. Pruning candidates — single consolidated list

  Repeated from §2.7 with priorities; this is the pre-Beta cleanup list:

  **Tier 1 (high leverage, low risk):**
  - CLAUDE.md audience-taxonomy duplication → single source of truth in §7.
  Saves ~15 lines, removes drift risk.
  - Refinement-012 status note → mark bypass-message-rule SUPERSEDED,
  handoff-drop PRESERVED.
  - Duplicate refinement-003 files → reissue one as refinement-014 OR rename
  with explicit a/b discriminator.
  - §6 Iterative Refinement rule → either acknowledge unvalidated state
  inline OR move to architecture/observations.

  **Tier 2 (medium leverage, requires validation):**
  - CLAUDE.md tight-pattern / WRONG-CORRECT examples → move to companion doc.
   Saves ~45 lines. Requires one fresh-chat test of the compacted doctrine to
   confirm doctrine still lands.
  - Refinements 009, 010, 011 status notes → mark "Principle subsumed by
  refinement-013, mechanics preserved."
  - §1 System Awareness inventory → may overlap with
  `architecture/architecture-tree-v1.md`. Worth a separate audit pass.

  **Tier 3 (cosmetic / archaeological):**
  - Refinement-002 (SED v1 / M3 reordering question) — was the question
  resolved by decision-015 (M3 scope decision)? If yes, mark refinement-002
  closed with cross-reference. If no, it is an open architectural question
  that should not sit in `records/logs/refinements/`.
  - README files in `records/logs/refinements/` and `records/logs/decisions/`
   — verify they reflect current state through refinement-013 and
  decision-017.

  ---

  ## 5. Risk surface for Alpha → Beta

  **Tier 1 — must-resolve before Zach's window:**

  1. **Pro-account budget realism.** Re-run Pre-Alpha-8 input on Zach's Pro
  account before the 1-week window opens. Cost: one session. Value: the
  entire 1-week window's signal quality.
  2. **Carousel Mode disposition.** Either author a minimal Lane spec now, or
   explicitly scope-exclude social Carousel content from Zach's window.
  Halfway is worst.
  3. **Zach onboarding on mode-declaration vocabulary.** Even 30 minutes
  closes the Pre-Alpha-1 vocabulary-drift gap.

  **Tier 2 — likely to surface in the window:**

  4. **Closed-loop discipline rule 1 (≤2-3 sentences per step) against real
  clinical reasoning.** May force compression on cases that legitimately need
   more. Watch for Zach pushing back on terseness.
  5. **The mode-spanning prefix pattern** (`"Research mode, then Clinical
  mode:"`). Zach has not seen this. Recommend the system surface this pattern
   when Zach asks an ambiguous mode-spanning question, instead of the picker.
  6. **Bypass-message + research-XXX storage pointer presentation.**
  "research-010 already locked from a prior session" assumes Zach reads
  "research-010" as a storage pointer. He may read it as system jargon. Watch
   for friction.

  **Tier 3 — lower priority but worth tracking:**

  7. **Insight / Script / Business Mode first-touch.** Each mode's first
  fresh-chat instance is unvalidated territory. The loop architecture should
  have a checklist for first-mode-touch observations.
  8. **§6 Iterative Refinement first iteration arc.** Substance is correct
  (full-artifact reprint each turn); behavior is unvalidated. Watch for Zach
  iterating and the system reverting to delta-summary.
  9. **HL-X-as-confirmation-question allowance** (refinement-013, narrowed
  scope). No Pre-Alpha test surfaced an HL-X-as-subject confirmation. Watch
  for first instance.

  **Risks the operator has discounted (per the brief, that I confirm):**

  - Doctrine inflation as a Beta blocker. The brief flags it; Zach's Pro
  budget makes it material, not aesthetic.
  - Single-test-input bias. Confirmed; meta-realization §3.3.
  - Operator-tester rather than founder-tester perspective. Confirmed;
  meta-realizations §3.4.

  **Risks the operator has discounted that the brief does NOT flag:**

  - Pre-Alpha-2 vs Pre-Alpha-8 input non-equivalence (meta-realization §3.1).
  - Live closed loop validated once on outdated doctrine state
  (meta-realization §3.2).
  - Refinement-012 was a wrong rule on the way through; the loop caught it
  but the catch consumed a test cycle (meta-realization §3.5).

  ---

  ## 6. Future-potential ceiling — realistic 10x unlocks vs.
  operator-aesthetic complexity

  **What's load-bearing for 10x:**

  1. **Validation that the system actually scales Zach's output.** Hours
  saved per week, clients served per week, content shipped per week. If
  Zach's 1-week window produces (a) more output than baseline at (b) equal or
   better quality, the system has demonstrated load-bearing value. If it
  doesn't, the doctrine is optimized for the wrong objective. This is the
  single most important Beta datum and the brief does not surface it as a
  metric.

  2. **The doctrine-engineering pattern transferring across operators.** If
  you can build doctrine-on-Claude that constrains output for one PT
  operator, can you build it for a second PT operator without rebuilding from
   scratch? If yes, the doctrine pattern is productizable; this becomes a B2B
   doctrine-engineering capability. If no, this is bespoke to Zach. The
  honest test is: take the Pre-Alpha-8 doctrine state, change Zach's name to
  a hypothetical second operator, and ask what would need to change. If the
  answer is "everything in the operator-internalized affordances"
  (mode-spanning prefix, vocabulary, etc.), the doctrine is bespoke. If the
  answer is "swap research records and HL list," it's a transferable
  substrate.

  3. **The operator-observation loop as a doctrine-management category.** The
   loop is the unique asset here. Most LLM-tooling projects do prompt
  engineering; this is doctrine engineering with an explicit refinement loop.
   Productizable as: "operators define behavior; system refines doctrine
  between sessions through observation, not in real-time." This is closer to
  MDM (master data management) for behavior than to typical LLM tooling. The
  MIS resonance is real — and unusual.

  **What's operator-aesthetic complexity:**

  1. The audience-taxonomy 3x duplication. The system would behave the same
  with a single source of truth.
  2. The refinement-009/010/011/012 chain preserved as live doctrine when 013
   is the actual rule.
  3. The §6 Iterative Refinement rule shipped as live before validation.
  4. The inventory-style §1 System Awareness when an architecture tree
  already exists in `architecture/architecture-tree-v1.md`.

  **Realistic 10x:**

  - NOT adding Carousel Mode in Beta. If Carousel adds doctrine surface
  without proportionate output value, it's complexity-for-complexity.
  - IS validating the doctrine-engineering pattern is transferable. One
  additional operator (hypothetical or real) is a 10x signal.
  - IS measuring Zach's actual output uplift in the 1-week window. The Alpha
  state record asks "Alpha is not production-validated by founder. Zach's
  1-week testing window comes next." Define what "production-validated" means
   *in measurable terms* before the window opens, not after.

  **Career-leverage angle (per my user_role memory — operator is an MIS+CS
  Honors graduate):** doctrine-engineering for LLM-driven business systems is
   unusually well-aligned with the MIS+CS credential pair. MIS resonates with
   master data / governance / contract-driven behavior; CS Honors resonates
  with the engine-depth and deterministic-output-contract framing. This
  project, if generalized away from Zach-the-PT, is a portfolio piece for B2B
   AI doctrine engineering. The bespoke-to-Zach version is a one-off favor.
  The transferable-pattern version is a productizable capability. Right now,
  this project has not been forced to distinguish which it is. Beta is the
  moment to force that distinction.

  ---

  ## 7. What I deferred from this review

  In the spirit of the brief's "honest evaluation" framing:

  - **Operator-observation-loop-v1.md** — read partially; could not fit in a
  single read budget. My evaluation of the loop's framing (§2.5) relies on
  the Alpha state record's representation of the loop and the raw Pre-Alpha
  transcripts. If the loop architecture file contains framing claims that
  contradict the Alpha state record, my finding may need revision.
  - **Refinements 009, 010, 011, 012 individual files** — I read 008 + 013
  directly and inferred 009–012 from the cross-references in CLAUDE.md, the
  Alpha state record, the brief, and refinement-013's disposition of them. My
   recommendation to mark them subsumed/superseded is consistent with what
  those documents say about each other; if a primary read of 009–012 surfaces
   something inconsistent, the recommendation may need revision.
  - **The 10 research records (research-001→010)** — out of scope per the
  brief; I respected that. HL-09 fabrication-free is asserted; I have not
  audited.
  - **Hard Locks substance (HL-01→HL-10+)** — out of scope per the brief; I
  respected that.
  - **Decision logs (decision-001→017)** — sampled via cross-reference but
  not read in primary form. My claims about decision-014 (M2 acceleration)
  and decision-017 (Mode Activation) are inferred from CLAUDE.md and the
  Alpha state record's representations; if a primary read surfaces
  inconsistencies, revision needed.
  - **Validation transcripts Pre-Alpha-3, 4, 5, 6, 7** — read only
  Pre-Alpha-2 and Pre-Alpha-8. The "5 internal-identifier leaks under added
  complexity" claim about Pre-Alpha-4 (Alpha state record line 148) is taken
  on the operator's reporting; I did not verify by reading the raw
  transcript. My meta-realization §3.1 (Pre-Alpha-2 vs Pre-Alpha-8
  non-equivalence) is verified directly.

  If any of these deferred reads change the calls in this review, surface
  back and I'll revise.

  ---

  ## 8. Closing — pointer back to the operator

  You asked: *"Bias toward saying the uncomfortable thing. Don't split the
  difference."*

  The uncomfortable things, in priority order:

  1. The Alpha lock is a doctrine-fidelity Alpha on a narrow validation
  surface, not a 5-mode-validated Alpha. The lock decision is defensible *if*
   "Alpha" means "doctrine target-complete, ready for first-time validation
  in production." The lock decision is over-stated *if* "Alpha" means
  "behavior validated across the 5-mode operator surface."
  2. CLAUDE.md is doctrine-inflated. The single highest-leverage move before
  Zach's window is compacting the audience taxonomy to one source of truth
  and moving examples to a companion doc.
  3. Refinements 011 and 012 are doctrine-as-coping candidates by the
  contrarian read. Refinement-013 is the doctrine that should have been from
  009 onward. Sunk-cost preservation is a real signal in the chain's status
  notes.
  4. Carousel Mode deferral is operator-avoidance dressed as need-driven
  deferral.
  5. Pro-account budget realism is the largest unmeasured Beta blocker. One
  pre-Zach-window test closes it.
  6. The "doctrine evolution arc 008→013 cumulatively succeeded under fresh
  execution on the same input" framing is an over-claim. The data supports
  "the doctrine evolved across the surfaces the changing tests exposed." Both
   are true; only the second is honest.

  The thing that is more settled than your cautious framing implies:
  **refinement-013's audience-based discipline is genuinely good doctrine.**
  The reframe captures what the principle should have been from the start,
  and Pre-Alpha-8 — caveats above notwithstanding — is real validation that
  the principle lands under fresh execution. The operator-observation loop,
  applied to its own scaffolding chain, produced a clean reframe. That is the
   loop functioning as designed. Don't undersell it.

  The thing that is less settled than the cautious framing implies: **the
  5-mode operator surface is doctrine-locked but not behavior-locked.**
  Zach's 1-week window is the first 4-mode validation. Treat it that way, not
   as production-readiness verification.

  — ProjectBrainer
  2026-05-04

  Review delivered as a single copyable markdown block per the standing
  format rule. Headline: doctrine-fidelity Alpha is real on the surfaces
  tested, but the "5-mode operator surface validated" framing overreaches the
   data; CLAUDE.md is inflated (audience taxonomy 3x); refinements 009–012
  should be marked subsumed/superseded; the largest unmeasured Alpha→Beta
  risk is Pro-account budget realism on Zach's tier; Carousel Mode deferral
  is structural avoidance. Findings are committed (no split-the-difference)
  and tagged with file:line references where the operator can act on them. I
  deferred reads on operator-observation-loop-v1.md (token budget) and
  refinements 009–012 individually (inferred from cross-references) — flagged
   in §7 so revisions are possible if those reads contradict.

✻ Baked for 9m 40s

※ recap: Goal: deliver an impartial ProjectBrainer review of The Muscle PT at
   Alpha lock before ultrareview and Zach's 1-week test. The review is
  delivered as a single markdown block; next action is your read and any
  revision requests. (disable recaps in /config)