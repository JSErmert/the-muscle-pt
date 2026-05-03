---
asset_id: affiliate-and-caption-footer-v1
date: 2026-05-02
type: shared assets file (used across multiple lanes)
status: locked v1
parent_decision: decision-016 (Lane Abstraction for Content Production, 2026-05-02)
resolves: refinement-003 (affiliate line specification, 2026-05-02 — N=3 ET-03 escalation)
relevant_doctrine:
  - CLAUDE.md §6 Output Style, §7 Output Translation
  - records/logs/decisions/decision-016-lane-abstraction-for-content-production.md (parent decision; lifts shared elements out of any single lane)
linked_artifacts:
  - records/logs/refinements/refinement-003-affiliate-line-specification.md (resolved by this file)
  - execution/content-output-contract-v1.md (Insight Lane spec — references this file)
  - execution/exercise-to-script-lane-spec-v1.md (Exercise-to-Script Lane spec — references this file)
  - records/content/planned/content-001-why-should-you-care-thoracic-mobility-chronic-neck-pain.md (Insight Lane piece — placeholder updates to reference this file)
  - records/content/planned/content-002-fact-or-fiction-neck-pain-breathing.md (Insight Lane piece — placeholder updates to reference this file)
  - records/content/planned/content-003-soft-sell-12-week-program.md (Insight Lane piece — placeholder updates to reference this file)
---

# SHARED ASSETS — AFFILIATE LINE + CAPTION FOOTER V1

This file holds the social-platform caption footer elements that are shared across multiple lanes (Insight Lane, Exercise-to-Script Lane, and any future lane that publishes to Instagram / similar platforms). Per decision-016, elements used across multiple lanes do NOT live inside any single lane's contract — they live here, referenced by pointer from each lane's spec.

This file resolves refinement-003 (affiliate line specification, ET-03 escalation triggered by N=3 placeholder occurrences in content-001 / content-002 / content-003).

---

## The Shared Assets

### Three-dots separator

```
.
.
.
```

The three-dots separator visually breaks the caption into "above the dots" (the bucket-specific content) and "below the dots" (the standard footer). Used in all Instagram-style captions across lanes.

### Save line

```
Save this for your next [VARIABLE] day
```

The `[VARIABLE]` is **per-lane variable** (see Per-Lane Variation Rules below).

### Like & follow line

```
Like & follow @themusclespt for more
```

Constant across all lanes and all pieces. No variation.

### Affiliate tag line

```
@hd.muscle @thepridefoods @gympin code THEMUSCLEPT
```

Constant across all lanes and all pieces. Updated only when sponsor relationships change (see Update Triggers below).

### Full footer (verbatim)

```
.
.
.
Save this for your next [VARIABLE] day

Like & follow @themusclespt for more

@hd.muscle @thepridefoods @gympin code THEMUSCLEPT
```

---

## Per-Lane Variation Rules

The Save line `[VARIABLE]` differs by lane.

### Exercise-to-Script Lane

`[VARIABLE]` = **body-part day matching the exercise**

Examples:
- Romanian deadlift → "Save this for your next leg day"
- Bench press → "Save this for your next chest day"
- Lat pulldown → "Save this for your next back day"
- Standing calf raise → "Save this for your next calf day" (or "leg day" if the operator prefers consolidating)

The variable is mechanical — derive from the exercise's primary body-part target.

### Insight Lane

`[VARIABLE]` = **bucket-appropriate call-to-action context**

Examples by bucket:
- Bucket 1 (Why Should You Care) → "Save this if you have [the relevant condition the piece addresses]" (e.g., "Save this if you have chronic neck pain")
- Bucket 2 (Scrolling Through My Feed) → "Save this for the next time you see [reaction context]"
- Bucket 3 (Fact or Fiction) → "Save this if you've been told [the myth being addressed]"
- Bucket 5 (Soft Sell) → "Save this if you've been [the audience friction the piece names]"

The variable is content-driven — the operator picks the call-to-action that matches the piece's signal trigger.

### Carousel Lane (deferred)

When Carousel Lane is activated (deferred per decision-016), its variation rule will be added here. Not active.

### Future lanes

Each new lane that publishes to social platforms specifies its own Save line variation rule in its lane spec, AND that rule is summarized here for cross-reference.

---

## Update Triggers

This file changes only when:

| Trigger | Update path |
|---|---|
| **Sponsor change** (new affiliate, dropped affiliate, code change) | Decision/Business Lane → updates the affiliate tag line here → all lanes that reference this file are automatically updated by the next piece they produce |
| **Handle change** (e.g., @themusclespt changes) | Decision/Business Lane → updates the Like & follow line here |
| **Save-line variation rule update for an existing lane** | Lane spec update + this file's Per-Lane Variation Rules section update |
| **New lane added that publishes to social** | New lane spec authored + Per-Lane Variation Rules section here updated to add the new lane's variation rule |

Updates flow through Decision/Business Lane (for sponsor/handle changes — these are business calls) or through lane spec updates (for variation rule changes — these are doctrine calls).

---

## Why This File Exists Separately

Refinement-003 (the recurring placeholder pattern across content-001 / content-002 / content-003) had three resolution options:

1. Specify in Content Output Contract v1 (lock affiliate line into Insight Lane's contract)
2. Explicitly exclude from contract scope (handle per-piece)
3. Per-platform / per-offer asset layer

Decision-016 chose **Option 3 with a refinement** — the assets are shared (not platform-or-offer-only), and they live outside any single lane's contract. This:

- Prevents lane-coupling (Insight Lane and Exercise-to-Script Lane share the affiliate line; neither owns it)
- Makes sponsor / handle updates cheap (one file edit, all lanes inherit)
- Keeps lane specs focused on lane-specific structure
- Acknowledges that affiliate / caption footer is an operational asset, not lane doctrine

---

## Versioning Rule

This is **v1**. Future versions:

- **v1.x** — adding new lane variation rules, updating Save line examples
- **v2** — structural changes to the footer format (e.g., adding a new line, removing the three-dots convention, changing platform conventions)

Updates to the affiliate tag itself (sponsor changes) do NOT trigger a version bump — they are operational updates to a v1 file. The version reflects structure, not content.

---

## Last Updated

2026-05-02 — initial v1 file authored. Refinement-003 resolved via Option 3 (shared assets layer). Affiliate line, caption footer, three-dots separator, Save line per-lane variation rules, Like & follow line, and update triggers all locked. Insight Lane content-001/002/003 placeholder updates now unblocked (decision-016 follow-on task #4). Exercise-to-Script Lane content-004 (RDL) can now fully pass criterion #8 once authored.
