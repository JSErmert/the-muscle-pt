---
decision_id: decision-017
date: 2026-05-02
type: architectural decision (mode activation pattern — operator interface to the lane abstraction)
status: locked
parent_decision: decision-016 (Lane Abstraction for Content Production, 2026-05-02 — the lane abstraction this decision provides operator access to)
relevant_doctrine:
  - CLAUDE.md (full operating envelope — to be updated to surface Mode Activation pattern)
  - records/logs/decisions/decision-016-lane-abstraction-for-content-production.md (parent — defines the lanes; this decision defines how operators activate them)
  - architecture/master-operating-system-governance-bridge-v1.md §10 Evolution Model
linked_artifacts:
  - records/research/validation/2026-05-02-fresh-chat-test-protocol.md (priming pattern simplifies via mode commands)
  - execution/exercise-to-script-lane-spec-v1.md (Script Mode target)
  - execution/content-output-contract-v1.md (Insight Mode target)
  - execution/shared-assets/affiliate-and-caption-footer-v1.md (cross-lane shared, available across all modes that publish to social)
hl_09_evaluation: PASS — no fabricated grounding introduced. Mode activation is an operational interface; it does not change citation discipline, doctrine grounding, or system claims.
hl_10_evaluation: PASS — the addition is justified by documented current need. Lane-inference ambiguity (operator must implicitly signal which lane via context; agent must guess) is a real surfaced gap. Fresh-chat test protocol bias-delta concern (the founder's flagged risk that the docs alone wouldn't produce equivalent behavior) is materially reduced by explicit mode commands. The pattern is a thin layer — one operator-facing command per lane — not an expansive automation system.
trigger: 2026-05-02 — founder asked whether lanes should be activated by operator command (e.g., "Insight Mode", "Script Mode") to make lane-derived functionality navigable. The question surfaced that decision-016's lane abstraction had no operator-accessible interface; the pattern was architectural-only. Decision-017 closes that gap.
---

# DECISION-017 — MODE ACTIVATION PATTERN

This decision establishes how operators activate lanes via explicit mode commands. It is the operator interface to the lane abstraction that decision-016 (2026-05-02) introduced architecturally.

The lane abstraction made the system architecturally portable across work types. The mode activation pattern makes it **operationally accessible** — any operator (Zach, Josh, or any fresh agent reading the documentation) can declare a mode in plain language and the system locks to that lane's doctrine, voice register, citation discipline, and output structure.

---

## Operator-Facing Brief — HOW TO USE MODES

When you start a piece of work, declare the mode. One line. The system locks to that mode's rules until you switch.

### The 6 modes

| Mode command | When you use it |
|---|---|
| **Clinical Mode** | A patient or client case in front of you. |
| **Insight Mode** | Content sparked by real-world signal — something you saw, said, or reacted to. |
| **Script Mode** *(or Exercise-to-Script Mode)* | Turning an exercise into a scriptable, filmable structure. |
| **Carousel Mode** | Long-form visual decomposition. *(Currently deferred — system will tell you so.)* |
| **Research Mode** | Authoring or extending a research record. *(Mostly Josh's mode.)* |
| **Business Mode** *(or Decision Mode)* | Pricing, packaging, hiring, scaling, partnerships. |

### How to declare a mode

Any of these work — system reads them all:

> *"Insight Mode."*
> *"Switch to Script Mode."*
> *"I'm in Clinical Mode."*
> *"Business Mode — pricing for the new program."*

### What happens when you declare

The system locks to that mode's:
- Doctrine (which spec / contract / engine governs the output)
- Voice register (appropriate to the mode)
- Citation discipline (heavy / light / none per mode)
- Output structure (5 buckets vs. 8 sections vs. clinical plan vs. tradeoff brief, etc.)

### What if you don't declare a mode

System infers from context (current behavior preserved). If unclear, system asks one question: *"Which mode are you in?"*

### How to switch modes mid-conversation

Just declare the new mode. System acknowledges the switch and locks to the new mode.

> *"Done with the case. Switch to Insight Mode — I want to make a reel about what just happened."*

### What if your work spans two modes

Finish one mode's work first, then switch. The system signals when it sees a mode-spanning request and asks which to do first.

---

## Architectural Context

### The lane / mode duality

Two complementary concepts, introduced by sibling decisions:

| Concept | Decision | Role |
|---|---|---|
| **Lane** | decision-016 | Architectural noun — the work-type axis. Names the kind of work and its governing doctrine. |
| **Mode** | decision-017 *(this decision)* | Operator command verb — how the operator opens the door to a lane and locks the system to it. |

Lanes describe the system structure. Modes describe how the operator accesses them. They coexist; neither replaces the other.

### Why mode activation is needed now

Decision-016 introduced lanes architecturally but left lane selection implicit — the operator's context implies the lane; the agent infers which doctrine to apply. This works when the agent has full session context (as during the 2026-05-02 authoring sprint) but creates real risks otherwise:

1. **Fresh-chat bias delta.** The founder explicitly flagged this concern when designing the fresh-chat test protocol — a fresh Claude.ai chat without session priors must "discover" the lane from documentation. Inference is harder; failures are more likely.
2. **Lane-inference errors.** Agent can guess wrong, especially at borderline (e.g., a clinical case the operator wants to make content about). Wrong-lane application produces wrong-doctrine outputs.
3. **Operator overhead.** The lane abstraction was invisible to the operator without a command interface. The operator's mental model (filming day vs. clinical day vs. content-from-something-I-saw day) had no system-side hook.
4. **Doctrine-portability test.** The fresh-chat protocol's Cold/Primed structure tests whether documentation alone is sufficient. Adding mode commands makes Primed-mode tests cleaner and Cold-mode tests more rigorous (Cold tests now explicitly test whether the docs surface the mode commands without operator help).

### What this is not

Mode activation is **not** an automation pattern. It does not:
- Generate content automatically
- Fire triggers without operator request
- Replace the lane spec — the spec still owns the doctrine; mode activation is a thin command layer

This is an **interface addition**, not a capability expansion. HL-10 passes because the addition is thin and the need is documented.

---

## The Decision

### Mode commands lock to lane doctrine

| Mode command | Primary alias(es) | Activates |
|---|---|---|
| **Clinical Mode** | "Clinical Lane" | Movement Case Engine v1 + Research Layer doctrine for citations + Clinical voice register |
| **Insight Mode** | "Insight Lane" | Content Output Contract v1 (5 buckets, master framework, voice contract, citation discipline) + Shared Assets v1 (caption footer) |
| **Script Mode** | "Exercise-to-Script Mode", "Exercise-to-Script Lane" | Exercise-to-Script Lane Spec v1 (8-section structure, locked phrases, 32-exercise priority list) + Shared Assets v1 (caption footer) |
| **Carousel Mode** | "Carousel Lane" | No active doctrine. System replies: "Carousel Mode is deferred — no active doctrine. Use Insight Mode or Script Mode for now." |
| **Research Mode** | "Research Lane" | Research Layer doctrine: Bootstrap v1 + Index & Traceability v1 + Query Layer v1 + Research-to-System Mapping v1 |
| **Business Mode** | "Decision Mode", "Business Lane" | Governing Logic v1 + Hard Locks + Prioritization + Queue Engine. Out of scope: legal, tax, accounting (per CLAUDE.md §2). |

### Default behavior (no mode declared)

Current inference behavior preserved. Agent reads context, applies the most plausible lane's doctrine, and discloses inference if non-obvious. If genuinely ambiguous, agent asks: *"Which mode are you in?"* before proceeding.

### Mode switching

Operator can switch modes any time by declaring a new mode. Agent acknowledges the switch verbally and locks to the new mode's doctrine. Previous mode's work is preserved (the conversation history retains it); the active mode is the most-recently-declared one.

### Mode-spanning requests

When a request requires work in two modes (e.g., "I have a hypermobility patient I want to make content about"), agent:

1. Identifies the mode-spanning structure
2. Names the two modes involved
3. Asks the operator which to do first
4. Completes the first mode's work, signals the transition, then picks up the second on operator confirmation

This protects mode integrity. Mode-spanning is acknowledged; mode-mixing is not.

### Aliases are case-insensitive

"Insight Mode", "insight mode", "INSIGHT MODE", "Insight Lane", "insight lane" all activate the same mode. Operator does not need to remember exact capitalization or primary-vs-alias distinction.

### Mode declaration may be implicit at conversation start

If a fresh chat opens with a clinical case and no mode declaration, agent infers Clinical Mode. If the operator's first message contains both case material AND a mode command, the explicit mode wins.

---

## Implications

### Fresh-chat test protocol — UPDATE REQUIRED

The fresh-chat protocol's Primed mode currently uses:

> *"Use the M2 research layer. Walk the research index and surface relevant records with PMID + exact figure citations per the Content Output Contract. Speak in Zach's voice."*

This becomes:

> *"Clinical Mode."*

Single-token priming. Cleaner test, more production-realistic, easier to reproduce. The protocol should be updated as a follow-on task.

The Cold-mode tests gain new diagnostic value: they now also test whether a fresh chat reading CLAUDE.md alone discovers the mode command syntax and applies it. If the agent independently infers the right mode without command help, that's a stronger PASS than current Cold mode achieves.

### CLAUDE.md — UPDATE REQUIRED

CLAUDE.md needs a new "Mode Activation" subsection added to §2 ROLE MAPPING (or a new §2.5 if cleaner). The subsection surfaces:

- The 6 mode commands and their primary aliases
- Default behavior when no mode declared
- Mode switching syntax
- Mode-spanning request handling

This is decision-017's primary doctrine update. Follow-on task.

### Content authoring workflow — slightly cleaner

Future content pieces (content-005 onward) can declare mode in their frontmatter or in the operator's authoring prompt. This makes the lane assignment explicit at authoring time rather than inferred from the slug.

### Acceptance Criterion #8 (≥1 clinical decision surfaces a citation that materially shapes the recommendation) — pipeline-side strengthens

The fresh-chat test protocol becomes more rigorous (Cold tests have higher discriminative power). Pipeline-side criterion #8 satisfaction is strengthened by a tighter test methodology. Clinical-side still pending Stream A.

### Decision-016 (lane abstraction) — unchanged but completed

Decision-016 defined the lanes architecturally. Decision-017 makes them operationally accessible. Together, lanes + modes are now a complete architectural unit. Decision-016 itself does not need amendment; decision-017 sits as its operational sibling.

### Decision-015 (M3 scope decision) — minor amendment

Decision-015 evaluated Carousel as an M3-Automation candidate. Decision-016 reframed Carousel as a deferred Lane. Decision-017 now provides Carousel Mode as the operator-facing reply ("deferred — no active doctrine"). Decision-015 should note both reframes (Carousel as Lane per decision-016, Carousel Mode operator response per decision-017) in a small amendment. Follow-on task.

### M2 closeout — minor amendment

M2 closeout document should reflect:
- 4 of 5 INPUT COMMANDS banked (criterion #7 structurally satisfied per content-004)
- Lane abstraction (decision-016) and Mode Activation pattern (decision-017) as additional architectural commitments completed during the M2 acceleration window
- Refinement-003 resolved
- Pipeline-readiness for criterion #8 strengthened by mode activation

Follow-on task.

---

## HL-09 / HL-10 Gate Evaluation

### HL-09 (no fabricated grounding) — PASS

Decision-017 introduces no claims, citations, or evidence. The pattern is operational interface. No HL-09 surface.

### HL-10 (no addition without documented repeated failure / current need) — PASS

The addition is justified by documented current need:

1. **Documented bias delta concern.** The founder explicitly raised this when designing the fresh-chat test protocol 2026-05-02. The concern was specific: documentation alone may not produce equivalent system behavior in fresh chats without session priors.
2. **Documented lane-inference ambiguity.** Decision-016 introduced lanes but left lane selection implicit. The implicit-only design has a documented failure mode (wrong-lane application produces wrong-doctrine outputs at borderline cases).
3. **Documented doctrine-portability test.** The fresh-chat protocol exists specifically to test portability. Mode activation makes the test more rigorous and the production pattern more reliable.

The addition is **thin** — one operator-facing command per lane, one operator-facing default behavior, one operator-facing switch syntax. Not an expansive automation pattern. Passes both the spirit and the letter of HL-10.

---

## Follow-on Tasks (separate work, not part of this decision)

1. **Update CLAUDE.md §2** — add Mode Activation subsection surfacing the 6 mode commands, default behavior, switching syntax, mode-spanning handling.
2. **Update fresh-chat test protocol** — replace the multi-line Primed-mode primer with single-token mode commands. Update test design notes and rubric to reflect that Cold mode now also tests mode-discovery.
3. **Update M2 closeout** — reflect criterion #7 structural pass, decision-016 + decision-017 architectural commitments, refinement-003 resolution.
4. **Update decision-015** — small amendment noting Carousel Lane reframe (decision-016) and Carousel Mode operator response (decision-017).
5. **(Optional, downstream)** — author a brief Zach-facing user guide combining the lane brief (from decision-016) and the mode commands (from decision-017) into a single quick-read reference. Could ride along with the Zach handoff package.

These are sequential or parallel follow-ons. Not blocking decision-017 lock.

---

## Decision Lock

**Decision-017 locked 2026-05-02.**

Mode activation pattern formalized. Six mode commands locked. Default behavior preserved. Switching and mode-spanning rules established. Fresh-chat test protocol simplification path identified. CLAUDE.md update path identified. M2 closeout / decision-015 amendment paths identified.

Together with decision-016 (Lane Abstraction), the lane + mode architecture is complete: lanes describe the work-type structure of the system; modes describe how operators access them.

---

## Last Updated

2026-05-02 — initial decision authored. Mode Activation pattern locked as the operator interface to decision-016's lane abstraction. Six mode commands defined with aliases, default behavior, switching syntax, and mode-spanning rules. HL-09 / HL-10 gates evaluated and passed. Five follow-on tasks identified.
