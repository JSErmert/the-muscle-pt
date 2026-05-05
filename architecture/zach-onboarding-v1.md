---
doc_id: zach-onboarding-v1
version: v1
date: 2026-05-04
type: operator handoff (Alpha → founder production testing)
purpose: Get Zach productive on the system in ~30 minutes. Cover what he needs to actually use the system during the 1-week production testing window. Closes the operator-affordance dependency the metrics framework explicitly flags.
audience: Zach (founder, practicing PT, has not been involved in the doctrine build)
relevant_doctrine:
  - CLAUDE.md (the live interface doctrine — Zach doesn't need to read this)
  - architecture/alpha-state-record-v1.md (what's locked at Alpha)
  - architecture/alpha-production-validation-metrics-v1.md (the three metrics being measured)
hl_09_evaluation: PASS — operator reference document; no grounded claims requiring citation.
hl_10_evaluation: PASS — addition justified by ProjectBrainer review §2.8 + metrics framework's explicit operator-affordance dependency.
---

# Zach Onboarding — The Muscle PT System (Alpha)

This is your 30-minute reference for using The Muscle PT system during the 1-week production testing window. Read it once, keep it open while you work, ask Josh anything that's unclear.

## What this is (60 seconds)

The Muscle PT system is a doctrine layer that constrains a Claude.ai web instance to produce consistent professional output for your practice. You declare what you're working on (a "mode"); the system locks to the doctrine for that mode and produces output in your voice with your standards. Research-grounded claims come with verified citations. Internal mechanics stay invisible to you and to your clients.

The system is at **Alpha** — doctrine target-complete on the surfaces tested, ready for production validation. Your week is the first time the system runs against real client work, real content production, real business decisions. Three metrics will measure whether it's actually load-bearing for your practice (see `architecture/alpha-production-validation-metrics-v1.md` — Josh will walk you through these).

---

## Step 1 — How to declare a mode (most important)

Five modes. Declare in plain language at the start of a chat (or any time you switch):

| Mode | Use it for |
|---|---|
| **Clinical Mode** | Case classification, root cause, intervention design, programming for individual clients, reassessment plans |
| **Insight Mode** | Signal-driven content from real-world observation. The 5-bucket Insight Lane format. |
| **Script Mode** | Exercise-to-Script transformations (one exercise → teachable script using the locked 8-section structure). Alias: *Exercise-to-Script Mode.* |
| **Business Mode** | Pricing, packaging, hiring, scaling, partnerships. Alias: *Decision Mode.* |
| **Carousel Mode** | OUT OF SCOPE FOR THIS WEEK. Deferred to Beta. If you declare it, the system will tell you to use Insight Mode or Script Mode instead. |

**To declare**: just type *"Clinical Mode"* (or any other mode name) at the start of your message. Capitalization doesn't matter. You can also just describe what you're working on and the system will infer — but explicit declaration is faster and avoids the *"Which mode?"* picker.

**To switch mid-chat**: declare the new mode. The system locks to the new doctrine on the next turn.

---

## Step 2 — The mode-spanning prefix (use it constantly)

When your work spans two modes — for example, you need a research record grounded first and then a clinical protocol built on it — pre-declare both with this prefix:

> *"Research mode, then Clinical mode: <your request>"*

The system locks Research Authoring first, runs that to completion, signals the transition, then locks Clinical Mode and continues. **This skips the *"Which mode?"* picker AND the in-flow grounding-path question** — saves you turns.

This pattern was internalized by Josh during the build; it's now codified in CLAUDE.md §2. Use it whenever your work crosses mode boundaries.

---

## Step 3 — What you'll see when Research Authoring fires

Research Authoring is the system's way of grounding a claim with a verified citation. Two paths:

### Path A — Bypass (record already exists)

If you ask about a topic the system has already authored a research record for (one of research-001 through 010), it'll bypass the closed loop and just use the record. You'll see something like:

> *"research-010 already locked from a prior session (PMID 41843416, ACSM 2026 Position Stand)."*

**This is normal. Not jargon.** *"research-010"* is the storage pointer — it tells you which file in our system holds the source. PMID is the verifiable external reference. *"From a prior session"* means Josh authored this record before you started. Just keep going.

### Path B — Live closed loop (new topic needs grounding)

If the topic is new, the system fires a 10-step closed loop with three operator gates (Gate A, B, C). You'll see:

1. *"Research Mode locked. Searching <source>..."*
2. *"Found: <source name> (PMID: <number>). States: <exact figure>. Lock as research-XXX seed?"* — this is **Gate A**. You confirm or override.
3. **Gate B** asks how the record applies to your work; you confirm or override the proposed mapping.
4. **Gate C** asks for confidence calibration; you confirm or override the proposed level.
5. Record locked; system continues with your original request.

Each gate closes with *"Recommend X because Y. Confirm or override."* — you can just say *"Confirm"* or override with your reasoning.

**Important**: refinements 008–013 have been tested heavily on Path A but only once on Path B (back when the doctrine was different). Your first novel-topic grounding request is the first live test of the closed loop on current doctrine. **Flag back to Josh if anything in the gate sequence feels off — wrong source, weird phrasing, recommendation that doesn't match the substance.**

---

## Step 4 — What you'll see in artifact output (and what counts as a leak)

The system has been engineered to keep internal jargon out of your client-facing output. If you're producing:

- A **protocol template** (Clinical Mode)
- An **Insight content piece** or **Exercise script** (Insight or Script Mode)
- A **client deliverable** of any kind

Then the artifact body should NEVER contain:

- HL-X (HL-01 through HL-10+ — internal hard-lock identifiers)
- research-XXX, refinement-XXX, decision-XXX (record IDs)
- §X (CLAUDE.md section references)
- Engine names (Movement Case Engine, Content Output Contract, etc.)
- L1/L2/L3 (internal layer terminology)
- "Pre-Alpha", "validation session", "authoring run" (test methodology terminology)

**If you see any of these in a protocol template or content artifact, that's a leak.** Flag it. Translation discipline failed.

What's OK in operator-facing surfaces (gates, bypass messages, system status — things only YOU see, not your clients):

- research-XXX (storage pointer)
- PMID (verifiable reference)
- Source names (e.g., "ACSM 2026 Position Stand")
- Gate A / Gate B / Gate C
- HL-X when the system asks you to confirm a hard-lock decision (e.g., *"Lock under HL-09 strict?"*) — that's the identifier as the SUBJECT of a confirmation question; it's allowed because you might want to know which compliance rule you're acknowledging

What's NOT OK in operator-facing surfaces:

- HL-X used adverbially in prose (*"Per HL-09 the deviation must be disclosed"* should be *"The deviation must be disclosed"*)
- Engine names, layer names, contract names, lane names
- Anything in the "test methodology" category

If you see these, that's also a leak — flag it.

---

## Step 5 — Iterating on an artifact

When you tell the system to update an artifact (protocol, script, plan, programming sequence), it should reprint the **full updated artifact** each turn — not a diff, not a delta summary.

This is operator-authorized doctrine from your own May 4 session: *"give me updated exercise everytime i tell you to update."*

**Watch for the system reverting to delta-summary under iteration pressure.** This rule was authorized but has not been tested across a 5+ refinement arc. If you iterate substantially on one artifact and the system starts giving you "here's what changed" instead of the full artifact — flag it.

---

## Step 6 — The metrics log

Open `records/observations/alpha-week-1-metrics-log.md` (Josh will create the template). Three things to log:

### Daily (≤10 min total)

For each thing you produce with the system:

1. **What it was** — Clinical program / Insight piece / Script / Business decision
2. **Quality category** — (a) shipped as-is, (b) shipped with minor edits, (c) major rewrite, (d) discarded
3. **Decision confidence** (if the system surfaced a recommendation) — (a) acted directly, (b) acted after independent verification, (c) overrode

### Daily (one line)

Did the system feel like leverage today, or friction? One sentence.

### End of week

Joint review with Josh against the three metrics (Velocity, Quality, Confidence). The thresholds are pass/fail criteria for Alpha → Beta promotion.

**Logging cost ceiling**: 10 minutes/day max. If logging takes longer than this, the protocol itself is becoming anti-leverage — tell Josh, we'll simplify.

---

## Step 7 — What to flag back to Josh during the window

Anything in these categories goes to Josh (Slack, text, whatever's fastest):

1. **Leaks** — internal jargon (HL-X, engine names, etc.) appearing in artifact output that shouldn't be there per Step 4
2. **Live closed loop weirdness** — anything off in Gate A/B/C sequence on a NEW topic (refinements 008–013 untested against live branch on current doctrine)
3. **Iteration arc breakdowns** — if you iterate on an artifact and the system starts giving you diffs instead of full reprints
4. **Vocabulary drift** — if the *"Which mode?"* prompt confuses you or you find yourself typing words like *"programming"* / *"research"* as standalone responses (Pre-Alpha-1 surfaced this; we want to see if it recurs)
5. **Pro-account budget binding** — if your session hits a context limit before you finish a deliverable. This is a real Alpha→Beta risk; we need to know if and when it happens.
6. **Outputs that feel "generic"** — outputs that pass the form check but don't reflect your clinical judgment, content instinct, or business intuition. This is the Quality failure mode the metrics catch — but your subjective read matters.
7. **Trust friction** — recommendations the system surfaces that you DON'T trust. Specifically: what made you not trust it? That's the data we need to find which doctrine layer hasn't earned operational confidence.

You don't need to write essays — a one-line flag with a screenshot or copy-paste is enough. Josh will integrate.

---

## Step 8 — What's OUT of scope this week

- **Carousel content** (long-form visual decomposition for Instagram/social). Carousel Mode is deferred to Beta. If you have Carousel content to ship this week, do it manually — don't try to use the system for it. Don't let an unscoped feature become a production gap mid-window.
- **Doctrine changes** (CLAUDE.md edits, new refinements). Observe and flag; doctrine evolution happens between sessions, not during. The whole Alpha test is whether the *current* doctrine works in production — changing it mid-test invalidates the data.
- **New research records** (research-011+). If you NEED to ground a novel topic, fire the live closed loop (it'll author the record). But don't pre-author records "just in case" during the window — let actual gaps surface them.

---

## Step 9 — Quick reference card (keep this open)

**Mode declarations**: just type the name. Capitalization optional.

**Mode-spanning**: prefix with *"Mode A, then Mode B: <request>"*

**Closed-loop confirmation**: *"Confirm"* (or override with reasoning) at each gate.

**Iteration**: tell it to update; expect full artifact reprint.

**Leak flag**: screenshot + one line to Josh.

**Daily logging**: ≤10 min, three categories per output.

**Out of scope**: Carousel.

---

## The honest framing

You're testing whether the system actually scales your output, not whether the doctrine is theoretically correct. Three things can fail:

1. **Volume failure** — system slows you down (doctrine costs more time than it saves)
2. **Quality failure** — system's output isn't yours (you have to rewrite to make it sound like you)
3. **Confidence failure** — you don't trust the output (you verify everything before shipping, defeating the leverage)

Each can fail independently. The metrics catch each separately. Your job during the week is to use the system the way you'd actually use a tool — not to baby it, not to find ways to make it work, just use it. The data tells us where the system is load-bearing and where it isn't.

If at the end of the week one or more metrics fail, that's not a failure of the work — that's the data we need to scope Beta correctly. The honest read is more valuable than a passing read.

---

## Pointer back

- **Operator** (system architect): Josh
- **Founder** (you): Zach
- **Window**: 1 week from declared start
- **Repo**: `https://github.com/JSErmert/the-muscle-pt`

For anything not covered here, ask Josh. The doctrine evolves between sessions through the operator observation loop — your week's data is the input to whatever evolves next.

Welcome to Alpha. Use the tool, log honestly, flag leaks, override the system whenever your judgment says to. The system's job is to amplify your expertise, not replace it.

---

## Last Updated

2026-05-04 — initial onboarding doc authored at Alpha lock. Covers mode declarations, mode-spanning prefix, closed-loop discipline (bypass + live branches), audience-based identifier translation (what's a leak vs. what's intentional), iteration discipline, metrics log usage, what to flag back, what's out of scope. Closes operator-affordance dependency that the metrics framework explicitly flags.
