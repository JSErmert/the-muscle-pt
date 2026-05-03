---
decision_id: decision-016
date: 2026-05-02
type: architectural decision (lane abstraction for content production)
status: locked
relevant_doctrine:
  - CLAUDE.md §2 ROLE MAPPING (existing implicit lane structure — this decision formalizes the subdivision)
  - execution/content-output-contract-v1.md (Insight Lane spec — unchanged by this decision)
  - architecture/master-operating-system-governance-bridge-v1.md §10 Evolution Model
  - architecture/system-evolution-doctrine-v1.md (M-layer staging — orthogonal to lane axis)
linked_artifacts:
  - records/logs/refinements/refinement-003-affiliate-line-specification.md (resolves toward shared assets file via this decision)
  - records/system-history/extracted/2026-05-01-content-output-contract-source.md (5 INPUT COMMANDS — Input 4 reclassification)
  - records/logs/decisions/decision-015-m3-scope-decision.md (Carousel reframe — was M3-Automation candidate; now a Lane)
  - records/logs/reviews/monthly/m2-operationalization-closeout.md (closeout impact)
  - records/content/planned/content-001-why-should-you-care-thoracic-mobility-chronic-neck-pain.md (Insight Lane piece)
  - records/content/planned/content-002-fact-or-fiction-neck-pain-breathing.md (Insight Lane piece)
  - records/content/planned/content-003-soft-sell-12-week-program.md (Insight Lane piece)
hl_09_evaluation: PASS — no fabricated grounding introduced. Decision documents existing implicit structure (CLAUDE.md §2 ROLE MAPPING) and locks a new lane spec (Exercise-to-Script) whose trigger is a documented founder-provided template (RFF prompt 2026-05-02).
hl_10_evaluation: PASS — the lane abstraction is descriptive (captures existing structure made explicit), not expansive. The new Exercise-to-Script Lane spec is the only genuine addition; its trigger is a documented current need (the RFF Exercise Library prompt) representing real founder operational requirements, satisfying the documented-current-need spirit of HL-10.
trigger: 2026-05-02 — founder delivered "REAL FUNCTIONAL FITNESS — EXERCISE LIBRARY TEMPLATE" introducing a structurally distinct content production mode (locked opening/closing phrases, 8-section structure, catalog-driven exercise priority list, batch-filmable workflow, locked affiliate line, locked sign-off) that does not fit the Insight Lane's signal-driven 5-bucket master framework.
---

# DECISION-016 — Lane Abstraction for Content Production

This decision formalizes the lane subdivision under "Content Creation" (CLAUDE.md §2 ROLE MAPPING), introduces the Exercise-to-Script Lane to absorb the founder-provided RFF Exercise Library template, resolves refinement-003 (affiliate line) via a shared assets file, and reframes the Carousel candidate from "M3-Automation candidate" (decision-015) to "deferred Lane awaiting documented repeated need."

The decision was triggered by the 2026-05-02 RFF Exercise Library prompt. The founder identified that folding the prompt into Bucket 4 of the existing Insight Lane contract would collapse two distinct production modes into one contract — an architecturally dangerous move. This decision separates them cleanly.

---

## Operator-Facing Brief — THE LANES — A QUICK READ FOR ZACH

The system organizes around **the kind of work you're doing**. You're in one lane at a time. Pick the one that matches your next move.

### Clinical Lane
**When you're in it:** A patient or client case in front of you.
**What you get:** Classification, root cause, intervention sequencing, reassessment markers — grounded in real research with citations.
**What it produces:** A plan for one specific person.

### Exercise-to-Script Lane
**When you're in it:** Turning an exercise into a teachable, scriptable, filmable structure.
**What you get:** A consistent script template — muscles, function, biomechanics, execution, prescription, alternatives — applied to whatever exercise you're scripting.
**What it produces today:** Filmed RFF reels (the 8-part structure). Your backbone is the 32-exercise priority list.

### Insight Lane
**When you're in it:** Real-world signal — something you saw in clinic, something a client said, something in someone else's reel that hit wrong.
**What you get:** A bucket, a hook, a master framework, voice register, citation discipline.
**What it produces:** Reels — Why Should You Care, Scrolling Through My Feed, Fact or Fiction, Soft Sell.
*(Note: exercise demos used to live here under Bucket 4. They've moved to Exercise-to-Script Lane.)*

### Carousel Lane
**Status:** Deferred. No active doctrine. We build this when there's a documented repeated need — not before.

### Research Lane
**When you're in it:** A real question needs a grounded record.
**Your role:** Mostly flagging questions and providing real case input. Josh authors the records.
**What it produces:** The evidence the other lanes cite. The thing that stops fabricated grounding from sneaking in.

### Decision / Business Lane
**When you're in it:** A real call on pricing, packaging, hiring, scaling, partnerships.
**What you get:** A structured tradeoff call with the hard limits respected.
**Out of scope:** Legal, tax, accounting.

### How to know which lane you're in

Ask one question: **what am I producing in the next 30 minutes?**

- A plan for one person → **Clinical**
- An exercise scripted into reel/video form → **Exercise-to-Script**
- Content from something I noticed → **Insight**
- A grounded research record → **Research**
- A pricing or packaging call → **Business**

When two answers fit, pick the dominant one and finish that work first.

### Why the separation matters

Each lane has different rules. Exercise-to-Script is catalog-driven (a priority list of exercises). Insight is signal-driven (a real-world observation). Mixing them collapses both — you'd produce generic exercise content with no real insight, and reactive content with no consistent structure. Keep them separate; you keep them strong.

---

## Architectural Context

### The two axes of the system

| Axis | What it represents | Examples |
|---|---|---|
| **M-layer (maturity axis)** | How mature/operationalized the system is | M1 Decision Layer, M2 Research Layer, M3 Automation Layer (per refinement-002 resolution 2026-05-02) |
| **Lane (work-type axis)** | What kind of work the operator is doing | Clinical, Exercise-to-Script, Insight, Carousel (deferred), Research, Decision/Business |

The two axes are **orthogonal**. A lane can mature across M-layers; an M-layer contains multiple lanes. They are not interchangeable.

### Why this decision was needed now

The 2026-05-02 RFF Exercise Library prompt introduced a structurally distinct content production mode with:

- **Locked opening/closing phrases** (different from Insight Lane voice contract)
- **8-section structure** (different from Insight Lane's 5-section master framework Hook → Setup → Mechanism → Tie In → Sign Off)
- **Catalog-driven production** (32-exercise priority list — different from Insight Lane's signal-driven production rule)
- **Batch-filmable workflow** (different from Insight Lane's one-piece-per-signal cadence)
- **Locked affiliate line** specification (`@hd.muscle @thepridefoods @gympin code THEMUSCLEPT`)

Folding this into Bucket 4 of the Insight Lane contract would have created:

1. **Master framework conflict** — Bucket 4 sometimes 5 sections, sometimes 8
2. **Production-rule conflict** — Insight Lane's "extract real insight from real-world signal" diluted by "produce 32 exercises in priority order"
3. **Voice-contract conflict** — locked phrases vs. signal-shaped openings
4. **Operator-mode ambiguity** — operator has to implicitly infer which sub-mode they're in

The founder explicitly flagged the collapse risk as architecturally dangerous. This decision codifies the lane separation that prevents the collapse.

---

## The Decision

### Lane abstraction is locked

CLAUDE.md §2 ROLE MAPPING already implicitly contains lanes (Client Work, Content Creation, Decision Making, Business Decisions, Prioritization). This decision formalizes the subdivision **within Content Creation**:

- Content Creation lane → subdivided into **Insight Lane** + **Exercise-to-Script Lane** + **Carousel Lane (deferred)**

And names the full lane catalog explicitly:

| Lane | Work | Status |
|---|---|---|
| Clinical Lane | Patient/client case management | Active (M1 Movement Case Engine) |
| Exercise-to-Script Lane | Exercise → script transformation | **NEW — locked by this decision** |
| Insight Lane | Signal-driven content extraction | Active (M2 Content Output Contract v1) |
| Carousel Lane | Long-form visual decomposition | Deferred — no active doctrine |
| Research Lane | Question → grounded record authoring | Active (M2 Research Layer) |
| Decision/Business Lane | Tradeoff calls (pricing, packaging, hiring, etc.) | Active (M1 Governing Logic) |

### Lane operator rule (one lane at a time)

The operator is in one lane at a time. Lane selection is the first move when starting work. The "what am I producing in the next 30 minutes?" question is the lane filter.

### Each lane has its own contract / spec

| Lane | Contract / spec location |
|---|---|
| Clinical Lane | `systems/intelligence/movement-case-engine-v1.md` (and related Case Engine doctrine) |
| Exercise-to-Script Lane | `execution/exercise-to-script-lane-spec-v1.md` — **TO BE AUTHORED** as follow-on to this decision |
| Insight Lane | `execution/content-output-contract-v1.md` — **unchanged** |
| Carousel Lane | None — deferred until trigger |
| Research Lane | `systems/intelligence/research-layer-bootstrap-v1.md` + `research-index-and-traceability-v1.md` + `research-query-layer-v1.md` + `research-to-system-mapping-v1.md` |
| Decision/Business Lane | `systems/governance/governing-logic-v1.md` (and related governance doctrine) |

### Shared assets are lifted out of any single lane

Elements used across multiple lanes do NOT live inside any single lane's contract. They live in a shared assets layer:

- **Affiliate line** (`@hd.muscle @thepridefoods @gympin code THEMUSCLEPT`) and standard captioning footer (`Save this for your next [X] day` / `Like & follow @themusclespt for more`) — shared across all lanes that publish to social
- **Voice register / banned phrases / engine-name silence** — already in CLAUDE.md §5–§7 as system-wide rules
- **Citation format** (PMID + URL + exact figure) — already in CLAUDE.md §7 as a system-wide rule

The shared assets file location: `execution/shared-assets/` — **TO BE CREATED** with `affiliate-and-caption-footer-v1.md` as the first asset.

---

## Implications

### Refinement-003 (affiliate line specification) — RESOLVED via Option 1 with shared-assets twist

The affiliate line gets specified, but NOT inside the Insight Lane's `content-output-contract-v1.md`. It's lifted to `execution/shared-assets/affiliate-and-caption-footer-v1.md` and referenced by all lanes that publish to social.

content-001, content-002, content-003 placeholders update to reference this shared assets file.

Refinement-003 status: **resolved by decision-016. Update refinement-003 doc to reflect resolution.**

### Carousel reframe (decision-015)

Decision-015 evaluated Carousel as an M3-Automation candidate against HL-10 and DEFERRED. Decision-016 reframes Carousel as a **Lane**, not an automation candidate. The defer status remains, but the trigger changes:

- **Old (decision-015):** Carousel returns when documented repeated failure justifies automation infrastructure
- **New (this decision):** Carousel returns when documented repeated need justifies a Carousel Lane spec — i.e., when there's a real, recurring use case for long-form visual decomposition that the existing lanes can't absorb

The HL-10 evaluation for Carousel as a Lane will be made when the trigger fires.

### Input 4 of the 5 INPUT COMMANDS — RECLASSIFIED

Per `records/system-history/extracted/2026-05-01-content-output-contract-source.md`, Input 4 was "Show and Tell Biomechanics Masterclass (dumbbell row)" — previously categorized as Bucket 4 of the Insight Lane.

**Reclassification:** Input 4 is **Exercise-to-Script Lane** content. The dumbbell row example becomes a candidate exercise from the 32-exercise priority list (or substituted for one already on the list).

Acceptance Criterion #7 (≥4 of 5 INPUT COMMANDS) requirement adjusts:

| Input | Original lane (before this decision) | New lane | Status |
|---|---|---|---|
| 1 (Hamstrings → Bucket 1) | Insight Lane | Insight Lane | Banked via content-001 |
| 2 (Voice note → Bucket 2) | Insight Lane | Insight Lane | Pending external (Zach voice note) |
| 3 (Static stretching → Bucket 3) | Insight Lane | Insight Lane | Banked via content-002 |
| 4 (Dumbbell row → Bucket 4) | Insight Lane Bucket 4 | **Exercise-to-Script Lane** | Now solo-producible against the RFF spec — could bank as content-004 |
| 5 (12-week program → Bucket 5) | Insight Lane | Insight Lane | Banked structurally via content-003 |

3 of 5 INPUT COMMANDS banked structurally; Input 4 now unblocked for solo production via the new Exercise-to-Script Lane spec; Input 2 still external (Zach voice note required).

### CLAUDE.md §2 ROLE MAPPING — UPDATE REQUIRED

CLAUDE.md §2 currently says:

> ### Content Creation
> Use:
> - Content Case Flywheel (when to produce)
> - Content Output Contract v1 (what to produce — voice, format, buckets, citations)

This needs updating to surface the lane subdivision:

> ### Content Creation
> Three lanes — pick the one that matches what you're producing.
>
> **Insight Lane** — signal-driven content from real-world observation. Use:
> - Content Case Flywheel (when to produce)
> - Content Output Contract v1 (what to produce — voice, format, 5 buckets, citations)
>
> **Exercise-to-Script Lane** — exercise → teachable script transformation. Use:
> - Exercise-to-Script Lane Spec v1 (8-section structure, locked phrases, 32-exercise priority list)
> - Shared Assets v1 (affiliate line, caption footer)
>
> **Carousel Lane** — deferred. No active doctrine.

The CLAUDE.md update is a follow-on task, not part of this decision file.

### M2 Closeout impact

Acceptance Criterion #7 status updates from "2 of 5 banked + 1 structurally banked = 3 of 5" to **"3 of 5 banked + Input 4 now unblocked = 4 of 5 reachable solo"** once Exercise-to-Script Lane spec is authored. This is a meaningful M2 progress shift.

The M2 closeout document should reflect this. Follow-on task.

### M-layer staging unchanged

The lane abstraction is orthogonal to the M-layer staging. Decision-016 does NOT alter SED v1's 3-layer staging (M1 Decision, M2 Research, M3 Automation per refinement-002 resolution). M3 still stays empty per decision-015. The lane abstraction is a separate axis.

---

## Follow-on Tasks (separate work, not part of this decision)

1. **Author `execution/exercise-to-script-lane-spec-v1.md`** — capture the 8-section structure, locked phrases, 32-exercise priority list, batch-filming workflow, and worked example (Romanian Deadlift script). The RFF prompt is the source material; this lane spec is its formalization.
2. **Create `execution/shared-assets/affiliate-and-caption-footer-v1.md`** — capture the affiliate line, caption footer template, and per-lane variation rules.
3. **Update refinement-003** — mark resolved by decision-016 with shared-assets resolution path.
4. **Update content-001, content-002, content-003** — replace affiliate placeholders with reference to shared assets file.
5. **Author content-004** — Bucket 4 → Exercise-to-Script Lane, RDL or other priority-list exercise. Banks Input 4 of the 5 INPUT COMMANDS.
6. **Update CLAUDE.md §2** — surface the Content Creation lane subdivision.
7. **Update M2 closeout** — reflect criterion #7 progress (3 banked + Input 4 unblocked = 4 reachable solo).
8. **Update decision-015** — note that Carousel candidate has been reframed from automation candidate to deferred Lane.

These are sequential or parallel follow-ons. Not blocking decision-016 lock.

---

## HL-09 / HL-10 Gate Evaluation

### HL-09 (no fabricated grounding) — PASS

Decision-016 documents existing implicit structure (CLAUDE.md §2 ROLE MAPPING) and locks a new lane spec whose trigger is a documented founder-provided template (RFF prompt 2026-05-02). No fabricated grounding introduced. The Exercise-to-Script Lane spec, when authored, must follow standard grounding discipline (any biomechanical claims grounded; any prescription numbers grounded or marked as Zach's clinical/experiential heuristic).

### HL-10 (no addition without documented repeated failure / current need) — PASS

The lane abstraction itself is **descriptive, not expansive** — it captures structure that already exists implicitly in CLAUDE.md §2. Making implicit structure explicit is not an HL-10 addition; it's a clarification.

The Exercise-to-Script Lane spec **is** an addition. Its HL-10 justification:
- The RFF Exercise Library prompt represents a documented founder-provided current operational need
- The structural collision risk if folded into Bucket 4 represents a documented architectural failure mode that this decision prevents
- This is documented current need, not speculative future need — the strict spirit of HL-10 is satisfied

Carousel Lane stays deferred. Its HL-10 evaluation will be made when its trigger fires (documented repeated need for long-form visual decomposition).

---

## Decision Lock

**Decision-016 locked 2026-05-02.**

Lane abstraction formalized. Exercise-to-Script Lane introduced. Refinement-003 resolved via shared assets file. Carousel reframed from automation candidate to deferred Lane. Input 4 of the 5 INPUT COMMANDS reclassified to Exercise-to-Script Lane and unblocked for solo production. M2 progress meaningfully advanced.

The operator-facing brief embedded above is the canonical Zach-facing summary.

---

## Last Updated

2026-05-02 — initial decision authored. Lane abstraction locked. Operator-facing brief embedded. Eight follow-on tasks identified. HL-09 / HL-10 gates evaluated and passed.
