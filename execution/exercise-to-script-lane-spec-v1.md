---
spec_id: exercise-to-script-lane-spec-v1
date: 2026-05-02
type: lane spec (Content Creation → Exercise-to-Script Lane)
status: locked v1
parent_decision: decision-016 (Lane Abstraction for Content Production, 2026-05-02)
trigger_artifact: founder-provided "REAL FUNCTIONAL FITNESS — EXERCISE LIBRARY TEMPLATE" prompt 2026-05-02
relevant_doctrine:
  - CLAUDE.md (full operating envelope — voice rules, output translation, banned phrases, citation discipline)
  - execution/content-output-contract-v1.md (Insight Lane spec — sibling lane, this spec follows analogous structural rigor)
  - execution/shared-assets/affiliate-and-caption-footer-v1.md (referenced for affiliate + caption footer; TO BE AUTHORED as decision-016 follow-on #2)
  - architecture/master-operating-system-governance-bridge-v1.md §10 Evolution Model
linked_artifacts:
  - records/logs/decisions/decision-016-lane-abstraction-for-content-production.md (parent decision)
  - records/logs/refinements/refinement-003-affiliate-line-specification.md (resolution path: shared assets file)
  - records/system-history/extracted/2026-05-01-content-output-contract-source.md (5 INPUT COMMANDS — Input 4 reclassified to this lane)
hl_09_position: PASS — biomechanics claims grounded in standard anatomy/kinesiology common knowledge; specific research figures surface only when significantly informative; prescription numbers (50%/80%/6-12 reps/0-2 RIR) marked as Zach's clinical heuristic, not as research-citation-grounded.
hl_10_position: PASS — lane is the formalization of a documented founder-provided template. The 32-exercise priority list bounds the lane's scope; additions beyond require documented current need (per HL-10).
---

# EXERCISE-TO-SCRIPT LANE SPEC V1

This is the formal lane specification for Exercise-to-Script work — the transformation of an exercise (movement, equipment, technique) into a teachable, scriptable, filmable structure. The lane was introduced by decision-016 (2026-05-02) as a sibling to the Insight Lane (Content Output Contract v1) and the deferred Carousel Lane.

The source material is the founder-provided "REAL FUNCTIONAL FITNESS — EXERCISE LIBRARY TEMPLATE" prompt 2026-05-02. This spec formalizes that template as doctrine.

---

## Lane Identity

### Scope

| In scope | Out of scope |
|---|---|
| Educational exercise reels (filmed) | Client-specific written programs (different lane — provisionally a future "Programming-for-Clients Lane") |
| Exercise library catalog reels | Patient-specific clinical interventions (Clinical Lane / Movement Case Engine) |
| Biomechanics + anatomy + execution + prescription + alternatives for one exercise per piece | Periodization / mesocycle structure (different work — Decision/Business Lane or future lane) |
| The 32-exercise priority list as the backbone | Reactive content from real-world signal (Insight Lane) |
| Batch filming workflow with voiceover-later production | Long-form visual decomposition (Carousel Lane — deferred) |

### When the operator is in this lane

The lane filter from the operator-facing brief: *what am I producing in the next 30 minutes?* If the answer is **"an exercise scripted into reel/video form"**, the operator is in this lane.

If the answer involves both an exercise AND a real-world signal trigger (e.g., "I want to react to a video of someone doing this exercise wrong"), Insight Lane Bucket 2 (Scrolling Through My Feed) takes precedence. Exercise-to-Script Lane is for the educational-library-catalog mode, not the reactive mode.

### One exercise per piece

This lane produces **one exercise per piece**. Multi-exercise content (e.g., a full workout, a circuit, a superset) belongs in a different lane (Insight Lane or future workout-content lane), not this one. The 8-part structure is calibrated to a single movement.

---

## Locked Phrases

These phrases are **invariant across every piece**. Operator does not edit them.

### Locked opening (5 seconds)

> "On today's episode of Real Functional Fitness, I teach you how to perform the [exercise name]."

### Locked closing / sign-off (5 seconds)

> "That is the [exercise name]. I am the Muscle PT. I will see you in the next one."

### Programming locked phrasing (10 seconds)

> "Two warm-up sets. Fifty percent for eight reps. Eighty percent for four reps. Then one working set in the 6 to 12 rep range taken close to failure — 0 to 2 reps in reserve."

These three locked phrases are the lane's voice anchors. Reels that omit or edit them fail criterion #1 of the lane's pass criteria.

---

## The 8-Part Structure

Total runtime: **75 to 90 seconds**.

| # | Section | Duration | Purpose |
|---|---|---|---|
| 1 | **Opening Hook** | 5 sec | Locked opening phrase + on-screen text [exercise name] |
| 2 | **Why This Exercise Matters** | 10–15 sec | Muscle groups + role in real-world function/ADLs. Connect gym movement to a life outcome. |
| 3 | **Anatomical Function** | 10–15 sec | Primary mover + what it actually does. Origin / insertion / line of action — communicated in toddler-clear language. |
| 4 | **Biomechanics and Resistance Profile** | 10–15 sec | Where in the range of motion the load is highest. Ascending or descending resistance profile. Where the stretch is. Where the contraction is. |
| 5 | **Execution and Cues** | 15–20 sec | Setup + 2–3 specific cues that make the movement work + 1–2 common compensations to avoid. |
| 6 | **Programming** | 10 sec | Locked programming phrasing (above). |
| 7 | **Alternatives** | 10 sec | "If you do not have access to this equipment or this movement does not feel right for your body — here are two alternatives that train the same anatomical function." Then name two anatomically equivalent substitutions. |
| 8 | **Sign Off** | 5 sec | Locked closing phrase. |

**Total:** 75–90 seconds across the 8 sections.

---

## Voice Contract

| Voice trait | Required register |
|---|---|
| Owns the call | Yes — Zach speaks as the authority teaching the movement, not as one option among many |
| Toddler-clear without being condescending | Yes — anatomical concepts (origin, insertion, line of action, biarticular, etc.) explained in plain language a non-clinician can follow |
| Brother-to-brother / coach-to-trainee register | Yes — direct address ("you", "your"), not impersonal third-person |
| Honest, no hype | Yes — "this protects your back for decades" is OK if grounded in mechanics; "transform your body" is banned |
| No banned phrases | Per CLAUDE.md and Insight Lane voice contract — no "transform", "unlock", "secret", "they don't want you to know", "discover", false-scarcity language |
| No engine names | Per CLAUDE.md §5 — no "research-008", "horizontal modifier", "RC-7", "lane spec", etc. in user-facing output |
| No factor-watching lists | Per CLAUDE.md §5 — no "watch for sleep, stress, hydration, etc." |
| Action override | Per CLAUDE.md Hard Override — one prescription, one set of cues, one set of alternatives. No "you could try X or Y or Z" |

---

## Programming Prescription Convention

**Locked structure for Section 6:**

- Warm-up Set 1 — 50% of working weight × 8 reps
- Warm-up Set 2 — 80% of working weight × 4 reps
- Working Set — 6 to 12 reps taken close to failure (0–2 RIR)

**Why locked:** the prescription is part of the lane's identity. Every Exercise-to-Script piece teaches the same set/rep/RIR convention so the audience develops a consistent training framework across the entire library. Variation undermines the library's coherence.

**HL-09 grounding note:** the prescription numbers are Zach's clinical/experiential heuristic, broadly aligned with hypertrophy and minimum-effective-dose literature but not surfaced as a per-piece research citation. The convention is treated as the lane's standard, not as a research-derived figure requiring PMID grounding.

---

## Alternatives Convention

**Locked structure for Section 7:**

> "If you do not have access to this equipment or this movement does not feel right for your body — here are two alternatives that train the same anatomical function."

Then **name two alternatives**, each with a one-line reason for why it substitutes (different stability demand, different equipment requirement, different load distribution, etc.).

**Selection rule:** alternatives must train the **same primary anatomical function** as the main exercise. A Romanian deadlift alternative cannot be a leg curl (different muscle action) — it can be a dumbbell RDL or single-leg RDL (same hip-hinge function with different stability/load demands).

---

## Caption Template (Instagram)

```
[Exercise name]

Primary movers — [list the muscles]
Function — [what these muscles do in real life]
Resistance profile — [ascending or descending]
Stretch position — [where in the range]

Programming — 2 warm-up sets at 50 percent for 8 reps and 80 percent for 4 reps. 1 working set in the 6 to 12 rep range taken close to failure (0 to 2 RIR).

Alternatives — [Exercise 1] / [Exercise 2]
.
.
.
[Caption footer per shared assets v1]
```

The three-dots separator and the caption footer (Save / Like & follow / affiliate tag) live in `execution/shared-assets/affiliate-and-caption-footer-v1.md` and are referenced here by pointer, not duplicated.

The "Save this for your next [body part] day" line is bucket-variable in the Insight Lane but lane-fixed in this lane (always references the relevant body part for the exercise — leg day, chest day, back day, etc.).

---

## YouTube Clip Description Template

For long-form / educational platform output:

```
HOW TO PERFORM THE [EXERCISE NAME]
Real Functional Fitness Exercise Library

WHY THIS EXERCISE MATTERS
[2–3 sentences on the muscles trained and their role in function and ADLs]

ANATOMICAL FUNCTION
Primary mover — [muscle and its action]
Secondary movers — [list]
Stabilizers — [list]

BIOMECHANICS
Resistance profile — [ascending/descending]
Peak tension — [where in the range]
Stretch position — [where the muscle is loaded longest]

EXECUTION
Setup — [exact positioning]
Cues — [list 2–3 key cues]
Common mistakes — [list 1–2 to avoid]

PROGRAMMING
Warm-up Set 1 — 50% of working weight for 8 reps
Warm-up Set 2 — 80% of working weight for 4 reps
Working Set — 6 to 12 reps taken close to failure (0–2 RIR)

ALTERNATIVES
1. [Exercise name] — [why it substitutes]
2. [Exercise name] — [why it substitutes]

THE RFF METHOD
Train. Stack. Recover.

Coaching applications open at themusclept.com
```

The "Train. Stack. Recover." method line and the "Real Functional Fitness" series brand are **lane-specific brand elements**. They live in this spec, not in shared assets, because they are exclusive to this lane's output.

---

## Worked Example — Romanian Deadlift

This example was provided in the founder's source prompt and is preserved verbatim as the canonical reference piece for the lane.

### Opening
> "On today's episode of Real Functional Fitness, I teach you how to perform the Romanian deadlift."
> [TEXT ON SCREEN — Romanian Deadlift]

### Why This Exercise Matters
> "Your hamstrings, glutes, and erector spinae are the muscles you use every time you bend over to pick something up off the ground. Every grocery bag, every child, every box. If these muscles are weak — your lower back takes the load. The Romanian deadlift loads them through their longest range under maximum tension. Master this and you protect your back for decades."

### Anatomical Function
> "The hamstrings are biarticular — they cross both the knee and the hip. The Romanian deadlift loads them through hip flexion with the knees relatively fixed. The biceps femoris long head, semitendinosus, and semimembranosus all elongate as your hips travel back. The glutes act as the primary hip extensor on the way up. Erector spinae and multifidus isometrically brace the spine throughout."

### Biomechanics
> "This is a descending resistance profile movement. The mechanical demand on the hamstrings is greatest at the bottom — when the muscle is most lengthened and the moment arm at the hip is greatest. This is exactly where stretch mediated hypertrophy lives."

### Execution and Cues
> "Set up with a hip-width stance. Grip the bar slightly outside your legs. Exhale and stack — ribcage over pelvis, neutral spine. Push your hips back as you lower the bar — knees stay relatively fixed. Feel the stretch in your hamstrings. Drive your hips forward to return to standing. Two cues — push the floor away with your hips, not your back. And keep the bar pulled into your body the entire descent."

### Programming
> "Two warm-up sets. 50 percent for 8 reps. 80 percent for 4 reps. Then one working set in the 6 to 12 rep range taken close to failure — 0 to 2 reps in reserve."

### Alternatives
> "If you do not have a barbell or this loads your lower back too aggressively — try the dumbbell Romanian deadlift or the single-leg Romanian deadlift. Both train the same anatomical function with different stability demands."

### Sign Off
> "That is the Romanian deadlift. I am the Muscle PT. I will see you in the next one."

### Sample Caption

```
The Romanian Deadlift

Primary movers — hamstrings, glutes, erector spinae
Function — loads the muscles you use every time you bend to pick something up
Resistance profile — descending
Stretch position — bottom, hips back, hamstrings fully lengthened

Programming — 2 warm-up sets at 50 percent for 8 reps and 80 percent for 4 reps. 1 working set in the 6 to 12 rep range taken close to failure (0 to 2 RIR).

Alternatives — Dumbbell RDL / Single-leg RDL
.
.
.
Save this for your next leg day

Like & follow @themusclespt for more

@hd.muscle @thepridefoods @gympin code THEMUSCLEPT
```

This worked example is the canonical reference for pass-criteria evaluation. Future Exercise-to-Script pieces are graded against the structural and voice fidelity demonstrated here.

---

## 32-Exercise Priority List (Lane Backbone)

The 32 exercises below are the **lane backbone** — the bounded scope of the library. Pieces are produced in priority order unless documented current need justifies reordering.

### Lower body — knee dominant
1. Pendulum squat
2. Hack squat
3. Bulgarian split squat
4. Leg extension
5. Leg press

### Lower body — hip dominant
6. Romanian deadlift *(worked example above)*
7. Stiff leg deadlift
8. 45 degree back extension
9. Lying leg curl
10. Single leg RDL

### Upper body — push horizontal
11. Flat machine chest press
12. Cable chest fly
13. Incline dumbbell press
14. Pec deck

### Upper body — push vertical
15. Seated dumbbell shoulder press
16. Machine shoulder press
17. Lateral raise (cable and dumbbell)

### Upper body — pull horizontal
18. Machine row
19. Cable row
20. Chest supported dumbbell row

### Upper body — pull vertical
21. Lat pulldown
22. Pullup or assisted pullup
23. Straight arm pulldown

### Arms
24. Cable bicep curl
25. Incline dumbbell curl
26. Overhead tricep extension
27. Cable tricep pushdown

### Core
28. Cable wood chopper
29. Hanging leg raise
30. Plank progressions

### Calves
31. Standing calf raise
32. Seated calf raise

**HL-10 boundary on the list:** additions beyond these 32 exercises require **documented current need** (per HL-10 — operator request, observed audience demand, clinical relevance, or sponsor/equipment partnership). The list is not closed — it is bounded with an additions discipline.

---

## Filming Workflow

Production discipline (lives within this lane spec because it shapes what the operator does, not just what the script contains):

1. **Batch filming sessions** — 5 to 8 exercises per gym session
2. **Constants per session** — same shirt, same lighting, same setup
3. **Capture order** — all demo footage first, multiple angles per exercise; voiceover scripted/recorded later in a controlled environment
4. **Why this separation** — separates the visual capture from the performance, lets a month of content batch in two sessions, keeps audio quality consistent across the entire library

This workflow is the **Filming Mode** sub-mode within Exercise-to-Script Lane (per founder framing 2026-05-02 — "filming is the final extension, not the lane itself"). Future output channels within the lane (e.g., written program documents, app-based programming) would have different production workflows. Filming Mode is one such workflow, locked here as the v1 production convention.

---

## 8 Overarching Pass Criteria

Sibling rigor to the Insight Lane's 8 overarching pass criteria. Every Exercise-to-Script piece is graded against these:

| # | Criterion | What it tests |
|---|---|---|
| 1 | **Locked phrases verbatim** | Opening + closing + programming locked phrasings used exactly. Edits to these phrases fail this criterion. |
| 2 | **Why This Exercise Matters connects to ADLs** | Section 2 names the muscles AND ties them to a real-life function (groceries, kids, falls, posture, etc.). Generic "builds your hamstrings" without ADL connection fails. |
| 3 | **Anatomical Function in toddler-clear language** | Section 3 explains origin / insertion / line of action without medical jargon overwhelm. A non-clinician can follow it. |
| 4 | **Biomechanics correctly identified** | Section 4 names the resistance profile (ascending or descending), the peak tension location, and the stretch position. All three present. |
| 5 | **Execution complete** | Section 5 contains setup + 2–3 specific cues + 1–2 common compensations. Missing any element fails. |
| 6 | **Programming prescription verbatim** | Section 6 uses the locked programming phrasing exactly (50% × 8 / 80% × 4 / 6–12 reps / 0–2 RIR). |
| 7 | **Alternatives anatomically equivalent** | Section 7 names two alternatives that train the same primary anatomical function as the main exercise. |
| 8 | **Caption follows lane template + shared assets reference** | Caption uses the lane template structure, references shared assets file for footer (affiliate + Like & follow + Save line), and the Save line names the relevant body-part day. |

Aggregate pass requires **all 8 criteria met**. Provisional or placeholder elements (e.g., affiliate line awaiting shared assets file authoring) follow the same pattern as Insight Lane pieces — provisional pass with caveat documented.

---

## Citation Discipline (Lane-Specific)

Per CLAUDE.md §7, citations surface only when significantly informative or explicitly requested.

For Exercise-to-Script Lane:

- **Default: no inline citations.** Anatomy, kinesiology, and biomechanics claims rely on standard exercise-science common knowledge and are not surfaced with PMIDs per piece.
- **Exception 1: significantly informative claims.** If a biomechanics claim relies on specific research that materially shapes the recommendation (e.g., stretch-mediated hypertrophy specifics), the citation may surface either inline (per Insight Lane convention) or in the YouTube description's "WHY THIS EXERCISE MATTERS" section.
- **Exception 2: explicit request.** If the audience or platform requires citations, they surface.
- **Prescription numbers (50% / 80% / 6–12 reps / 0–2 RIR):** treated as Zach's clinical/experiential heuristic. Loosely aligned with hypertrophy + minimum-effective-dose literature but not per-piece-cited. Marked here in the spec as heuristic for traceability; not surfaced per piece.

This is **lighter-grounding than the Insight Lane**, consistent with the lane's purpose (teaching the movement, not surfacing the literature).

---

## Cross-Lane Interactions

| Other lane | How it interacts with Exercise-to-Script |
|---|---|
| **Clinical Lane** | A clinical case may surface a need for a hypermobility-aware substitute (e.g., research-008 implies certain RDL variations are inappropriate for hypermobile patients). The Alternatives section of the relevant Exercise-to-Script piece can include the clinically-aware substitute as one of its two alternatives. The clinical reasoning lives in Clinical Lane; the alternative naming lives here. |
| **Insight Lane** | An Insight Lane piece may mention an exercise that is then expanded into a full Exercise-to-Script piece. The Insight Lane piece is reactive/signal-driven; the Exercise-to-Script piece is library/catalog-driven. Same exercise, different production logic. Pieces do not cross-reference each other publicly; the cross-reference lives in the system, not in the audience-facing output. |
| **Carousel Lane** | When Carousel Lane is activated (deferred), an Exercise-to-Script piece's anatomical and biomechanical content could feed a long-form carousel decomposition. Not active. |
| **Research Lane** | Significantly-informative biomechanics claims surface citations from Research Lane records when the citation discipline rules apply. Default is no citation. |
| **Decision/Business Lane** | Pricing, packaging, or sponsor decisions affecting the lane (e.g., new sponsor → new affiliate line → shared assets file update) flow through Decision/Business Lane and update the shared assets, not this spec directly. |

---

## HL-09 / HL-10 Discipline Within the Lane

### HL-09 (no fabricated grounding)

Within Exercise-to-Script Lane:

- **Anatomical claims** must be correct (biceps femoris long head crosses hip and knee; this is fact, not opinion). Errors here violate HL-09 even without citation surfacing.
- **Biomechanics claims** must be mechanically defensible. "Descending resistance profile" must match the actual moment-arm reality of the exercise.
- **Prescription numbers** are Zach's heuristic — marked here as such, not as research-derived. The spec's transparency about this is the HL-09 protection.
- **Citations**, when surfaced, must follow CLAUDE.md §7 (PMID + URL + exact figure with units). Fabricated PMIDs or paraphrased numerics fail HL-09.

### HL-10 (no addition without documented current need)

Within Exercise-to-Script Lane:

- **The 32-exercise priority list is the lane's bounded scope.** Additions require documented current need.
- **The 8-part structure is locked at v1.** Structural changes require a new version (v2) with documented justification.
- **Locked phrases are locked.** Edits to "On today's episode of Real Functional Fitness…" or the closing or the programming phrasing require a new version.
- **The shared assets file changes** (affiliate line, footer) flow through Decision/Business Lane updates and don't require this spec's update.

---

## Versioning Rule

This is **v1**. Future versions:

- **v1.x** — minor refinements (e.g., adjusting timing per section based on actual filmed pieces; clarifying ambiguous criteria) that do not change locked phrases, the 8-part structure, or prescription convention
- **v2** — structural changes (new sections, locked phrase edits, prescription convention updates) require documented current need and a new version file

Versioning is per the Bridge §10 Evolution Model — expansion only when repetition is proven, friction is consistent, and value of structure outweighs cost.

---

## Last Updated

2026-05-02 — initial v1 spec authored. Lane formalized from founder-provided RFF Exercise Library template prompt 2026-05-02. 8-part structure, locked phrases, prescription convention, alternatives convention, caption + YouTube templates, RDL worked example, 32-exercise priority list, filming workflow, 8 pass criteria, citation discipline, cross-lane interactions, and HL-09/HL-10 discipline all locked. Awaiting shared assets file authoring (decision-016 follow-on #2) before content-004 (first lane piece, candidate exercise: Romanian deadlift via worked example) can fully pass criterion #8.
