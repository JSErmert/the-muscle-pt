---
exercise_id: fresh-chat-test-protocol-001
date: 2026-05-02
type: validation protocol (operator-run, fresh Claude.ai web sessions)
purpose: test whether the M2 system's repo documentation alone produces equivalent retrieval, sequencing, and voice behavior in a fresh Claude.ai chat (no session priors, potentially different model) compared to the orchestrated session that authored the records — surfaces the bias delta between session-context-loaded outputs and documentation-only outputs
acceptance_criteria_advanced:
  - "Acceptance Criterion #8 (≥1 clinical decision surfaces a citation that materially shapes the recommendation) — pipeline-side validation extended from 'authoring agent's outputs' to 'any fresh agent reading the documentation'. This is the higher bar."
  - "M2 portability test — the system is portable if a fresh agent reading only the repo produces equivalent system behavior. If not, the gap is a documentation deficit, not an agent deficit, and a refinement signal."
relevant_doctrine:
  - CLAUDE.md (auto-loaded, orients the fresh chat to system layers)
  - systems/intelligence/research-index-and-traceability-v1.md
  - systems/intelligence/research-query-layer-v1.md
  - systems/intelligence/research-layer-bootstrap-v1.md
  - execution/content-output-contract-v1.md
linked_artifacts:
  - records/research/validation/2026-05-02-live-case-retrieval-test.md (v2 — authoring-agent baseline for multi-mechanism case)
  - records/research/validation/2026-05-02-live-case-contrast-test.md (v3 — authoring-agent baseline for negative control)
  - records/research/validation/2026-05-02-live-case-borderline-test.md (v4 — authoring-agent baseline for screen-and-branch)
  - records/logs/reviews/monthly/m2-operationalization-closeout.md
---

# M2 Fresh-Chat Validation Protocol — 2026-05-02

This protocol tests whether the M2 system, as documented in the repo, produces equivalent behavior when read by an unbiased fresh Claude.ai chat — a session with no authoring history, no priors from the build sprint, and potentially a different model.

The 2026-05-02 validation triad (v2 / v3 / v4) was produced by the authoring agent (Opus 4.7, full session context). Those tests validate that **the pipeline can work**. This protocol validates that **the documentation alone makes it work** — the higher bar, and the actual production condition under which Zach (or any other operator) will use the system.

---

## Why This Test Matters

A system that requires its author's session memory to operate correctly is not portable. It is a session capability, not a repo capability. M2 is meant to be a repo capability — Zach should be able to open a fresh Claude.ai chat with the repo loaded, paste a patient case, and get the same quality of plan as the authoring agent produces.

If the fresh chat fails to produce equivalent behavior, the gap is a **documentation deficit**, not an agent deficit. The right response is to fix the documentation, not to tell the operator "you need the authoring agent."

This protocol surfaces those gaps.

---

## What the Fresh Chat Will Have

| Has | Does Not Have |
|---|---|
| All repo files (full read access) | Session memory of authoring sequence |
| CLAUDE.md auto-loaded | Knowledge of just-authored vs. long-standing records |
| Doctrine, records, index, queries, mappings, contracts | Awareness of just-resolved refinements (refinement-002, decision-015) |
| Ability to walk the index, read records, apply rules | Pattern-matching from having written the records |
| Pass criteria, banned phrases, voice contract | Conversational scaffolding from the build session |
| | Same model (likely Sonnet 4.6 web vs. Opus 4.7 authoring) |

**The bias under test is priors-based, not access-based.** The fresh chat has full read access. The question is whether the repo's text alone produces equivalent system behavior.

---

## Model Sequencing — Opus 4.7 Fresh First, Then Sonnet 4.6

The validation triad (v2/v3/v4) was authored on Opus 4.7 with full session priors. The fresh-chat test removes priors. To isolate the prior-bias variable cleanly, **hold the model constant first**.

### Phase 1 — Opus 4.7 Fresh (6 sessions)

Run all 6 sessions on Opus 4.7 fresh first. This isolates the prior-bias variable while holding capability constant:
- Authoring agent: Opus 4.7 + full session priors → known baseline (v2/v3/v4)
- Fresh agent: Opus 4.7 + zero session priors → test condition

Pass/fail on Phase 1 tells you exactly whether the documentation is portable across priors at high capability.

**Decision rule after Phase 1:**
- **All 6 PASS:** documentation is portable. Proceed to Phase 2.
- **Any PARTIAL or FAIL:** documentation gap exists. Fix the doc, re-run Phase 1 sessions that failed. Do NOT proceed to Phase 2 until Phase 1 passes.
- **Any CATASTROPHIC:** halt. The system is not portable. Major doctrine refinement required before continuing.

### Phase 2 — Sonnet 4.6 Fresh (6 sessions, only after Phase 1 passes)

Sonnet 4.6 is the default tier on Claude.ai web — likely what Zach will use in production. Phase 2 validates cross-model portability and production-realism after Phase 1 has confirmed documentation portability across priors.

**Decision rule after Phase 2:**
- **All 6 PASS:** system is portable across priors AND across models. Production-ready for Zach handoff.
- **Some PARTIAL or FAIL:** the system is portable at high capability but not at production model tier. Three options: (a) document additional priming guidance for Sonnet operators, (b) require Zach to use Opus 4.7, (c) refine the doctrine for higher-floor accessibility. Decision depends on which elements failed and whether priming repairs them.

### Why this sequence matters

If you run Sonnet 4.6 first and it fails, you can't tell whether the failure is documentation (priors matter) or model capability (Sonnet can't do it). Confounded result.

If you run Opus 4.7 fresh first, a pass cleanly proves documentation portability. A failure cleanly identifies a doc gap that needs fixing before any model variance test makes sense.

---

## Test Design — 3 Cases × 2 Modes = 6 Fresh-Chat Sessions (per phase)

### Two modes per case

| Mode | Operator Input | What it Tests |
|---|---|---|
| **Cold** | Paste the raw patient case only. No system framing. | Does the fresh chat discover the mode activation pattern AND apply the M2 system on its own? Tests CLAUDE.md orientation strength + mode-discovery. |
| **Primed** | Paste the raw patient case + one line: *"Clinical Mode."* | Does the fresh chat activate Clinical Mode correctly and apply the right doctrine? Tests mode activation pattern + doctrine application strength. |

**Note on Primed primer change (2026-05-02):** the original Primed primer was a multi-line instruction. After decision-017 (Mode Activation Pattern) locked, the primer became a single-token mode command. This is cleaner, more production-realistic, and tests the mode activation pattern itself — which is the canonical operator interface to the lane abstraction.

### Three cases (use verbatim from the validation triad)

**Voice note (2026-05-02 update):** the cases below were originally written in patient first-person voice. Production reality is that Zach types in his own clinical-shorthand register — case abstracted to mechanism, period statements, no patient quoting, dives straight in. Voice patterns extracted from the founder conversation archive (`records/system-history/raw/founder-claude-conversation-archive.md`). The underlying case signals are preserved across the rewrite; the v2/v3/v4 authoring-agent baselines remain valid comparison references.

#### Case A — v2 multi-mechanism positive (founder personal case)

> Right-dominant chronic chain. Lax right side — shoulder blade, jaw, upper trap, all loose right side, not left. Two prior right scapular dislocations. Right TMJ snap event, chronic clicking, swallowing-pressure thing on the right. C-T junction tweaked once under heavy breathing. Right upper trap chronic tight, inflamed in flares. Forward lean — desk hunched — the whole right top rides up. Bowl seat in the car forward-leaning, the neck eases up. Posterior chain right side inflammation cycles. What's the chain and what's the play.

#### Case B — v3 negative control (desk worker)

> Desk worker. 38, lifts three days. Overhead press, deadlifts. Six months upper back stiffness, dull ache between the scaps. Last two months tingling down the right arm on overhead pressing — backing off the lifts. Worst after long sitting, eases with warmup. No injury history. Joints stiff, not lax — explicit. Sleep clean. No widespread pain. Walk me through the chain.

#### Case C — v4 borderline (screen-and-branch)

> 32 female runner-lifter. Runs three to four, lifts twice. Four months right neck/shoulder deep ache, not constant but most days. Multi-region morning stiffness — neck, hips, hands — resolves in 20. Good days bad days, doesn't track activity. Pain wakes her on the right side at night. No injury triggered it. One college right shoulder sub, full recovery, asymptomatic until now. Mom is clearly hypermobile — thumb to forearm. She self-reports not bendy. Never been formally tested. How do I screen this and what's conservative in the meantime.

### Total Clinical Mode sessions: 6

- A-Cold, A-Primed
- B-Cold, B-Primed
- C-Cold, C-Primed

**Run each in a separate fresh chat to prevent cross-contamination.**

---

## Mode Activation Validation (5 additional tests)

Tests the full Mode Activation Pattern (decision-017) by activating each non-Clinical mode with a Zach-voice example input. These tests are **lighter-rigor than the Clinical Mode tests** — they validate that mode declaration triggers the right doctrine, voice register, and output structure, not full case-retrieval performance.

Run each in a separate fresh chat. One session per mode.

### Test 7 — Insight Mode

**Input (verbatim):**

> *Insight Mode. Saw a coach today telling people to stretch the upper trap to fix neck pain. That is not the answer. Want a reel.*

**What it tests:**
- Mode acknowledgment
- Activation of Content Output Contract v1 (5 buckets, master framework, voice contract)
- Bucket selection (Bucket 2 Scrolling Through My Feed OR Bucket 3 Fact or Fiction is the likely fit)
- Surfacing of research-008 grounding ("never stretch what's already overworked") with PMID + exact figure citation
- Voice register: signal-driven, brother-to-brother, owns-the-call

**PASS signals:**
- Bucket selected and named
- Master framework applied (Hook → Setup → Mechanism → Tie In → Sign Off)
- research-008 surfaced with PMID 35609204 + exact figure
- Caption format follows Insight Lane convention with shared assets footer

### Test 8 — Script Mode

**Input (verbatim):**

> *Script Mode. RDL today. Give me the full script.*

**What it tests:**
- Mode acknowledgment
- Activation of Exercise-to-Script Lane Spec v1
- 8-section structure applied (Opening Hook → Why → Anatomical Function → Biomechanics → Execution → Programming → Alternatives → Sign Off)
- Locked phrases used verbatim (Opening, Programming, Sign Off)
- Caption template + shared assets footer

**PASS signals:**
- Output substantially matches the canonical RDL worked example in the lane spec
- All 3 locked phrases present verbatim
- Programming convention exact (50% × 8 / 80% × 4 / 6–12 reps / 0–2 RIR)
- Two anatomically-equivalent alternatives named
- Save line: "Save this for your next leg day"

### Test 9 — Carousel Mode

**Input (verbatim):**

> *Carousel Mode. Want to break down the right-dominant chain pattern from yesterday's case into a long carousel.*

**What it tests:**
- Mode acknowledgment
- Recognition that Carousel Mode is deferred (no active doctrine)
- Appropriate redirect to active mode

**PASS signals:**
- Reply substantially matches: *"Carousel Mode is deferred — no active doctrine. Use Insight Mode or Script Mode for now."*
- Optionally suggests which active mode might absorb the work
- Does NOT fabricate carousel doctrine or attempt to produce carousel output

### Test 10 — Research Mode

**Input (verbatim):**

> *Research Mode. Need a record on stretch-mediated hypertrophy. Script lane references it. We don't have grounding yet. Walk me through what we'd need.*

**What it tests:**
- Mode acknowledgment
- Activation of Research Layer doctrine (Bootstrap, Index, Query, Mapping)
- Query Layer v1 discipline (no abstract research; needs real input source)
- HL-09 awareness — does NOT immediately fabricate a record

**PASS signals:**
- Acknowledges the reference gap (Exercise-to-Script Lane Spec mentions stretch-mediated hypertrophy as significantly-informative-eligible)
- Either drafts a query (query-009 or similar following Query Layer v1 format) OR flags that the input source needs to be specified before authoring
- Does NOT invent a PMID or fabricate a research record on the spot
- References Bootstrap v1's First Activation Rule (don't bulk-author records before triggers fire)

### Test 11 — Business Mode

**Input (verbatim):**

> *Business Mode. Thinking about moving the 12-week from rolling enrollment to cohort. What changes.*

**What it tests:**
- Mode acknowledgment
- Activation of Governing Logic v1 + Hard Locks + Prioritization
- Structured tradeoff call
- Out-of-scope discipline (no legal/tax/accounting advice)

**PASS signals:**
- Names the tradeoff dimensions (cash flow timing, operational complexity, audience experience, urgency premium, scaling vs. quality, etc.)
- Surfaces implications without padding
- Action override applied — produces one structured analysis, not a menu
- Hard Locks respected (no fabricated grounding for business claims; no legal/tax/accounting advice)

---

### Total sessions per phase: 11

- 6 Clinical Mode tests (3 cases × Cold + Primed)
- 5 Mode Activation Validation tests (one per non-Clinical mode)

Phase 1 (Opus 4.7 fresh) runs all 11. Phase 2 (Sonnet 4.6 fresh) mirrors after Phase 1 passes.

---

## Comparison Rubric

For each fresh-chat output, score against the authoring-agent baseline from the matched validation log (v2 / v3 / v4):

### Tier 1 — Structural Behavior (binary: matches or doesn't)

| Element | Case A target | Case B target | Case C target |
|---|---|---|---|
| Records that FIRE | research-001, 003, 004, 005, 008 (research-002 silent background) | research-001 (primary), research-005 (supporting); 002 silent | research-001 (primary only) |
| Records held SILENT | (none — research-006 disclosed as ungrounded) | research-008, 003, 004, 006 | research-005 (HOLD), 004, 002, 006 |
| Records in SCREEN state | none | none | research-008 (Beighton), research-003 (multi-region monitoring) |
| Horizontal modifier (research-008) applied? | YES | NO | NO — screened only |
| RC-7 (CS combined-modality) applied? | YES | NO | NO — held in reserve |
| HL-09 disclosure (ungrounded layer) | YES (TMJ referred out) | NO (not needed) | NO (not needed) |
| Plan structure | Single committed plan | Single committed plan | One immediate plan + 3 conditional branches |
| Reassessment horizon | 12 weeks | 6 weeks | 4 weeks (screen-driven) |

### Tier 2 — Citation Discipline (graded)

| Element | Case A target | Case B target | Case C target |
|---|---|---|---|
| Citation count | 4 (research-008, 003, 005, 001) | 2 (research-001, 005) | 1 applied (research-001) + 2 branch-context (research-008, 003) |
| Citation format | PMID + URL + exact figure with units | PMID + URL + exact figure | PMID + URL + exact figure |
| Citation surface mode | Inline per applied claim | Inline per applied claim | Applied + branch-context (conditional pivot evidence) |
| Fabricated PMID or figure | Should be ZERO | Should be ZERO | Should be ZERO |

### Tier 3 — Voice & Translation (graded)

| Element | Required register |
|---|---|
| Voice | Zach: practitioner addressing patient directly, owns-the-call, brother-to-brother register, honest |
| Engine names exposed? | NO — should fire silently (research-008 → "right side is lax", not "applying horizontal modifier") |
| Banned phrases? | NO — no "transform", "unlock", "secret", "they don't want you to know", etc. |
| Factor-watching lists? | NO — no "watch for sleep, stress, etc." |
| Action override? | YES — one plan, no options |

---

## Scoring

### PASS

- Tier 1: ≥ 8 of 9 elements match (record-firing pattern, sequencing rules, hard locks, plan structure)
- Tier 2: Citation count within ±1 of target; format correct; **zero fabricated PMIDs or figures**
- Tier 3: Voice within Zach's register; no engine names exposed; no banned phrases

### PARTIAL

- Tier 1: 5–7 of 9 match (some records misfire or some sequencing wrong)
- Tier 2: Citation count ±2 OR format drift OR ≥ 1 fabricated PMID/figure
- Tier 3: Voice partially Zach's but drifts (e.g., generic-fitness-influencer leak) OR engine names leak

### FAIL

- Tier 1: ≤ 4 of 9 match (system not applied or applied wrong)
- Tier 2: Heavy fabrication (multiple fake PMIDs or figures)
- Tier 3: Voice not Zach's at all OR system terminology in patient-facing output

### Catastrophic Failure (separate flag)

- Fresh chat ignores the M2 layer entirely and produces generic-internet-PT advice
- Fresh chat fabricates PMIDs that don't match the repo's records
- Fresh chat applies hypermobility-aware programming to Case B (desk worker, no laxity) — false positive
- Fresh chat applies generic mechanical programming to Case A (founder, lax substrate) — false negative on horizontal modifier

---

## Capture Template

For each of the 6 sessions, capture in a new validation log file at `records/research/validation/2026-05-XX-fresh-chat-test-results-[case]-[mode].md`:

```markdown
---
exercise_id: fresh-chat-test-[A|B|C]-[cold|primed]
date: [YYYY-MM-DD]
fresh_chat_model: [Sonnet 4.6 / Opus 4.7 / etc.]
mode: [cold | primed]
case: [A | B | C]
---

# Fresh Chat Test — Case [X] [Mode]

## Input
[verbatim case text from protocol]

## Operator framing (primed only)
[the priming line, if used]

## Fresh chat output (verbatim)
[paste the entire response]

## Tier 1 scoring
[checklist against the rubric — which elements matched, which didn't]

## Tier 2 scoring
[citation count, format, fabrication check]

## Tier 3 scoring
[voice, engine name leakage, banned phrases]

## Aggregate score
[PASS | PARTIAL | FAIL | CATASTROPHIC]

## Refinement signals surfaced
[any documentation gaps revealed by this session]

## Last Updated
[YYYY-MM-DD]
```

---

## What to Do on Each Outcome

### If PASS across all 6 sessions

The system is portable. Documentation is sufficient. Acceptance Criterion #8 pipeline-side is now documentation-validated, not just authoring-agent-validated. Phase 2 Stream A can proceed knowing Zach's fresh chats will produce equivalent behavior.

**Action:** log the result in the M2 closeout. No refinement entries needed.

### If PARTIAL on some sessions

Specific documentation gaps exist. The fresh chat got most of it but missed elements that would be obvious to the authoring agent because of priors.

**Action:** for each partial session, identify which Tier 1/2/3 elements failed. Each failed element is a refinement signal. If N=2+ sessions fail the same element, escalate to a refinement entry. Common likely gaps:
- The SCREEN state isn't documented (Case C borderline)
- The horizontal modifier precedence isn't surfaced clearly enough in research-008
- The citation surfacing rule (CLAUDE.md §7) is too vague on when to surface vs. suppress
- The voice contract examples are insufficient

### If FAIL on some sessions

Major documentation gaps. The system isn't being applied at all or is being applied wrong.

**Action:** stop testing, fix the documentation, re-run. Specifically:
- If Cold mode fails but Primed passes: CLAUDE.md orientation is too weak. Strengthen it.
- If both fail: the underlying doctrine files are unclear. Identify which file should have made this obvious; refine it.
- Each FAIL = a refinement entry, not a session note.

### If CATASTROPHIC on any session

The system is not portable in its current state. This is a hard finding.

**Action:** halt Phase 2 Stream A planning until the catastrophic failure mode is documented and fixed. The handoff to Zach is unsafe until the system is portable.

---

## Operator Instructions for Running the Test

1. Open Claude.ai web in a new browser tab. Make sure the repo is connected (or paste relevant files manually if not).
2. Start a fresh chat. Confirm no prior conversation context is present.
3. **For Cold mode:** paste only the case text. Do not add framing.
4. **For Primed mode:** paste the case text, followed by the priming line: *"Use the M2 research layer. Walk the research index and surface relevant records with PMID + exact figure citations per the Content Output Contract. Speak in Zach's voice."*
5. Capture the entire response verbatim into a new validation log file (template above).
6. Score against the rubric.
7. Move to the next case in a new fresh chat.
8. After all 6 sessions, review aggregate findings. Author refinement entries for any N=2+ failed elements.

**Important:** do not run multiple cases in the same chat. Cross-contamination defeats the test. Each session is one case, one mode, one fresh chat.

**Equally important:** do not edit fresh chat output before capturing. Verbatim only. The point is to surface what the fresh chat actually produces, not what we want it to produce.

---

## Test Disposition

**Protocol authored 2026-05-02. Awaiting operator-run sessions.**

This protocol does not generate validation results — those are produced by the operator running fresh Claude.ai chats and capturing outputs. The protocol's purpose is to make the test reproducible, calibrated, and comparable against the authoring-agent baselines.

When all 6 sessions are run and captured, aggregate the findings into a single closeout-style document at `records/research/validation/2026-05-XX-fresh-chat-test-aggregate.md` with overall pass/partial/fail summary and refinement signals.

---

## Last Updated

2026-05-02 — initial protocol authored. Six-session test design (3 cases × 2 modes) with verbatim inputs, comparison rubric, scoring tiers, capture template, and operator instructions. Awaiting operator-run results to validate M2 portability.
2026-05-02 (later) — added Phase 1 (Opus 4.7 fresh) / Phase 2 (Sonnet 4.6 fresh) sequencing rule. Phase 1 holds model constant to isolate prior-bias variable cleanly; Phase 2 validates cross-model portability only after Phase 1 passes.
2026-05-02 (later still) — Primed primer simplified to single-token mode commands per decision-017 (Mode Activation Pattern). Added 5 Mode Activation Validation tests in Zach's voice (Insight, Script, Carousel, Research, Business) to validate the full mode pattern. Total per phase: 11 sessions (6 Clinical Mode rigorous + 5 mode-activation light). Cold-mode tests now also test mode-discovery from CLAUDE.md alone. Up to 22 sessions if both phases run.
2026-05-02 (final) — Case A/B/C inputs rewritten in Zach's actual voice after voice extraction from `records/system-history/raw/founder-claude-conversation-archive.md`. Production reality: Zach types in clinical-shorthand register (case abstracted to mechanism, period statements, no patient quoting, dives straight in), not in patient first-person voice. Case signals are preserved across the rewrite; the v2/v3/v4 authoring-agent baselines remain valid comparison references. Mode Activation tests (7-11) sharpened to match same register.
