---
refinement_id: refinement-003-affiliate-line-specification
date: 2026-05-02
date_resolved: 2026-05-02
type: refinement (recurring pattern, ET-03 threshold met)
status: resolved 2026-05-02 — via decision-016 + shared assets v1 (Option 3, per-platform / per-offer asset layer with reframe as cross-lane shared assets)
trigger: ET-03 (Escalation Trigger 03 — recurring pattern, N=3)
resolution_artifact: execution/shared-assets/affiliate-and-caption-footer-v1.md
relevant_doctrine:
  - execution/content-output-contract-v1.md (citation discipline, master framework, banned phrases — but does NOT specify affiliate line)
  - architecture/master-operating-system-governance-bridge-v1.md §10 Evolution Model (expansion rule — only expand when repetition is proven)
  - CLAUDE.md §6 Output Style, §7 Output Translation
linked_artifacts:
  - records/content/planned/content-001-why-should-you-care-thoracic-mobility-chronic-neck-pain.md (1st placeholder occurrence)
  - records/content/planned/content-002-fact-or-fiction-neck-pain-breathing.md (2nd placeholder occurrence)
  - records/content/planned/content-003-soft-sell-12-week-program.md (3rd placeholder occurrence — ET-03 threshold met)
  - records/logs/reviews/monthly/m2-operationalization-closeout.md §"Refinement & Incident Signals Captured" (pre-recorded escalation threshold; this refinement is the prescribed action)
---

# Observation

`execution/content-output-contract-v1.md` defines the master framework (Hook → Setup → Mechanism → Tie In → Sign Off), voice contract, banned phrases, citation discipline (PMID + exact figure above the three dots), and 8 overarching pass criteria. **It does not specify the standard affiliate line** — the line that goes alongside or below the caption pointing to whatever Zach is currently directing audience traffic to (program, link in bio, supplement, equipment, etc.).

Three content pieces have now been authored against the contract:

- content-001 (Bucket 1, "Why Should You Care") — placeholder used
- content-002 (Bucket 3, "Fact or Fiction") — placeholder used
- content-003 (Bucket 5, "Soft Sell — 12-Week Program") — placeholder used

In each piece, the affiliate line slot was filled with a `[PLACEHOLDER — standard affiliate line per Content Output Contract v1]` token because the contract does not currently specify what goes there.

# Trigger

**ET-03 (Escalation Trigger 03 — recurring pattern, N=3) is met.**

Per the M2 closeout document (`records/logs/reviews/monthly/m2-operationalization-closeout.md`), the affiliate line gap was logged at N=2 with explicit pre-recorded escalation: "if content-003 produces a third occurrence, escalate to refinement." Content-003 has produced the third occurrence. Refinement entry is therefore now required by doctrine, not optional.

# Open Question

How should the affiliate line be handled?

Three resolution paths:

### Option 1 — Specify in Contract

Add an affiliate line specification to `execution/content-output-contract-v1.md`. The contract gains a section defining:
- The default affiliate line text (or template)
- Where it goes in the post structure (caption, comment, bio, etc.)
- When it varies (per platform, per cohort, per offer cycle)

**Implication:** every future content piece pulls the affiliate line from a single specified source. The contract owns it. Updates to the line happen by editing the contract.

**Cost:** the line becomes part of the doctrine. If Zach changes his affiliate strategy frequently (different programs, different platforms, seasonal offers), the contract requires frequent updates — friction.

### Option 2 — Explicit Exclusion

Add an explicit exclusion clause to the contract: "The affiliate line is not part of the content contract scope. It is set per-piece by Zach at publish time."

**Implication:** content pieces are authored complete-without-affiliate; affiliate is a Zach-controlled publish-time addition. The contract acknowledges its absence rather than ignoring it.

**Cost:** content pieces produced by this system are technically incomplete drafts — they cannot go live without a Zach hand-add. Same friction as today, but at least named in doctrine.

### Option 3 — Per-Platform / Per-Offer Asset Layer

Create a separate small asset file (e.g., `records/content/assets/affiliate-lines.md`) that holds the current affiliate line(s) by platform and offer cycle. Content pieces reference this file. The contract gains a one-line reference to it.

**Implication:** affiliate line lives outside the contract but inside the system. Content pieces still pull from a single source. Updates happen in one small file rather than in the doctrine.

**Cost:** introduces a new asset class, but small and well-bounded. Closest match to how Zach actually operates (lines change per cohort, per platform, per active offer).

# Decision Target

This refinement requires **Zach's input** to resolve, because all three options depend on:
- Whether Zach has a stable affiliate line or whether it varies frequently
- Whether the line varies by platform (IG vs TikTok vs YouTube)
- Whether it varies by offer cycle (cohort-based program with rolling enrollment cycles)

Without Zach's input, picking any option is fabrication.

# Resolution — 2026-05-02

**Resolved via decision-016 + shared assets v1.**

Option 3 (per-platform / per-offer asset layer) was confirmed as the resolution path, with one architectural reframe: the asset is **not** per-platform / per-offer specifically — it is **cross-lane shared**. The same affiliate line and caption footer apply across Insight Lane, Exercise-to-Script Lane, and any future lane that publishes to social platforms. The asset is a system-wide shared element, not a per-platform variant.

The trigger artifact for the resolution was the founder-provided RFF Exercise Library prompt (2026-05-02), which included the standard affiliate line verbatim:

`@hd.muscle @thepridefoods @gympin code THEMUSCLEPT`

Decision-016 (Lane Abstraction for Content Production) authored 2026-05-02 lifted the affiliate line and caption footer out of any single lane's contract and into a shared assets layer at `execution/shared-assets/affiliate-and-caption-footer-v1.md`. The shared assets file was authored 2026-05-02 and is the canonical specification.

**Why the cross-lane reframe (not strict Option 3):** the per-platform / per-offer framing implied platform-specific or offer-cycle-specific variation. In practice, the affiliate line is constant; what varies per-lane is the Save line. The shared assets file captures both — affiliate line as constant, Save line variation rule as per-lane. This is a more accurate match to how the assets actually behave.

**Per-lane Save line variation rules** (locked in `execution/shared-assets/affiliate-and-caption-footer-v1.md`):
- Exercise-to-Script Lane → "Save this for your next [body part] day"
- Insight Lane → "Save this if [bucket-appropriate call-to-action context]" (varies per piece based on signal trigger)
- Carousel Lane → deferred (added when lane activates)

# Implications While Open

- content-001, content-002, content-003 remain at placeholder for the affiliate line until this refinement resolves
- Acceptance Criterion #6 (≥1 content piece passes all 8 criteria fully) cannot fully close on the affiliate-line dimension until this refinement resolves
- Future content pieces (content-004 onward) will continue to use the placeholder pattern until resolution
- The placeholder pattern is now **expected and tracked**, not a recurring gap — N≥4 occurrences should NOT trigger a new refinement; this refinement absorbs all subsequent occurrences until resolved
- The placeholder pattern does NOT block Phase 2 dual-stream Stream A start; it blocks live publication only

# Action Status

**Resolved 2026-05-02.** Affiliate line specified at `execution/shared-assets/affiliate-and-caption-footer-v1.md` as `@hd.muscle @thepridefoods @gympin code THEMUSCLEPT`. Caption footer + per-lane Save line variation rules also locked in the shared assets file.

The Zach handoff package no longer includes affiliate line specification (this is now resolved). Two Zach-input items remain in the handoff:
1. Voice note for Input 2 (Bucket 2 reaction reel — Insight Lane)
2. Exercise selection for Input 4 — REMOVED FROM HANDOFF: per decision-016, Input 4 reclassified to Exercise-to-Script Lane and is now solo-producible against the lane spec; no Zach input required to unblock

**Updated handoff package (post-decision-016):** only Input 2 (voice note) requires Zach input. Inputs 4 and refinement-003 are both resolved internally.

# Last Updated

2026-05-02 — initial refinement entry authored. ET-03 threshold met via content-003 third placeholder occurrence. Three resolution options laid out; provisional preference noted.
2026-05-02 (later) — resolved via decision-016 + shared assets v1. Resolution path: shared assets file (cross-lane reframe of Option 3). Affiliate line locked. Per-lane Save line variation rules locked. Zach handoff package reduced to 1 item (Input 2 voice note only).
