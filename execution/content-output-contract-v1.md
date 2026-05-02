# THE MUSCLE PT — CONTENT OUTPUT CONTRACT v1

## Purpose

This document defines the user-facing contract for content production output. Anything the system generates as content for The Muscle PT must conform to this contract.

The contract enforces:
- voice fidelity (sounds like the founder, not generic AI)
- clinical accuracy without sacrificing accessibility
- verified research grounding (PMID + exact figure, never fabricated)
- format and runtime discipline
- automatic bucket classification

Source: `records/system-history/extracted/2026-05-01-content-output-contract-source.md`

---

## Master Framework

Every reel/script follows this structure:

```text
Hook → Setup → Mechanism → Tie In → Sign Off
```

- **Hook:** ambiguous, < 10 words, creates curiosity
- **Setup:** brief context — *who this is for, what's about to be answered*
- **Mechanism:** anatomy / physiology / clinical reasoning explained simply
- **Tie In:** so-what — practical implication for the audience
- **Sign Off:** bucket-specific (see below)

Runtime: **60–90 seconds**. Non-negotiable.

`TEXT ON SCREEN` brackets included throughout for editor.

---

## Voice Contract

### Required tone
- Direct
- Clinical
- Toddler simple
- Confident, not pushy
- Validates what is true; corrects what is not — never rage bait

### Banned phrases (hard)
- *non-negotiable*
- *game changer*
- *all day long*
- *dial it in*
- *motivational filler* of any kind

If output contains any banned phrase, it has failed the contract. Regenerate.

---

## Caption Contract

- 3 to 5 lines
- **No hashtags**
- **No exclamation marks** on CTA
- Three dots (`...`) separate the lead content from the affiliate line
- Affiliate line at the bottom (standard) — replaced by soft CTA in Soft Sell bucket

### Citation in caption
Verified PMID + exact figure (effect size, percentage, duration of effect, etc.) cited correctly **above the three dots**.

Format:
```text
Study finding: <exact figure with units>
PMID: <number> | <link>
...
<affiliate line or soft CTA>
```

Citations must:
- be verified — never fabricated
- include the exact figure from the study, not paraphrased numerics
- include PMID when available, source link in all cases

---

## Bucket Contract — 5 Buckets

The system must auto-tag inputs to one of five buckets and produce output following that bucket's specific format requirements.

### Bucket 1 — Why Should You Care
- **Trigger pattern:** input phrased as "why should you care about [topic]" or "why does [topic] matter"
- **Format:** master framework (Hook → Setup → Mechanism → Tie In → Sign Off)
- **Sign off:** *"I am the Muscle SPT. And that is why you should care."*
- **Tone:** clinical, hooked on curiosity, ends with conviction

### Bucket 2 — Scrolling Through My Feed
- **Trigger pattern:** founder describes a piece of content they've encountered (someone else's reel, claim, advice) and reacts
- **Format:** master framework, with Tie In addressing the original content directly
- **Tone:** measured, nuanced — validates what's true, corrects what's not. Anatomy and clinical reasoning grounded
- **Required:** offer better alternative with anatomical justification when correcting
- **Sign off:** measured close — no signature line

### Bucket 3 — Random Fun Facts / Science Explained (Fact or Fiction format)
- **Trigger pattern:** input phrased as "fact or fiction. [claim]. fact" or "fact or fiction. [claim]. fiction"
- **Format:** **locked Fact or Fiction format** — Hook → "Fact" or "Fiction" stated clearly → mechanism → research → tie in
- **TEXT ON SCREEN:** "Fact or Fiction?" then "FACT" or "FICTION" reveal
- **Required:** specific research citation with figures (effect size, percentage decrease, duration of effect)
- **Required:** practical application for the audience
- **Sign off:** signature close consistent with science-explained tone

### Bucket 4 — Show and Tell — Biomechanics Masterclass
- **Trigger pattern:** input includes "biomechanics masterclass on [exercise]" or analogous masterclass framing
- **Opening line (locked):** *"Okay class. On today's episode of Zach Teaches You Biomechanics we are going over the [exercise]."*
- **Required content:**
  - Anatomy: primary movers + secondary movers, accurately named
  - Scapular / joint mechanics relevant to the lift
  - Cue language matching founder voice (points of contact, stack maintenance, finger emphasis where relevant)
  - Common compensation pattern identified and addressed
  - Functional outcome — why it matters for posture / daily life / injury prevention
- **Sign off:** masterclass close — connects back to broader programming logic

### Bucket 5 — Soft Sell — Bottom of the Funnel
- **Trigger pattern:** input phrased as "soft sell reel" or contains conversion-oriented framing ("if I had X to do Y")
- **Tone:** direct, confident, value-led — never pushy
- **Format:** value delivery (e.g., 5 actionable items in priority order, each with rationale, not just directive)
- **Tie in:** connects to coaching offer naturally — never forced
- **Sign off (locked):** *"Coaching applications and consultations are open — link in bio"*
- **Caption:** ends with the soft CTA — replaces the standard like-and-follow line

---

## Bucket Auto-Tagging

The system must classify each input to exactly one bucket without being told. Classification is based on:

- Trigger pattern in the input phrasing
- Content type signaled (educational, reactive, science explainer, masterclass, conversion)
- Founder framing (e.g., *"reel —"*, *"reaction reel"*, *"masterclass on"*, *"soft sell reel"*)

When classification is ambiguous, classify to the **most specific** bucket that matches. If still ambiguous, classify to the bucket whose constraints are most restrictive (typically Show and Tell or Fact or Fiction).

---

## Overarching Pass Criteria

Output passes the contract when ALL of the following are true:

1. Sounds like the founder — not generic AI
2. Hits exact runtime — 60 to 90 seconds
3. Cites verified PMID with exact figures — never fabricated
4. Follows caption format precisely — no hashtags, no exclamation, three dots, affiliate line (or soft CTA per bucket)
5. Tags the correct bucket without being told
6. Includes the appropriate sign off for the bucket
7. Maintains clinical accuracy without sacrificing accessibility
8. Avoids every banned phrase

If any one criterion drifts, the output has failed. The drift point is where the next iteration of the system needs to address constraints — log to `records/logs/incidents/` (translation failure) or `records/logs/refinements/` (recurring pattern per ET-03).

---

## Acceptance Test Set

The 5 INPUT COMMANDS in `records/system-history/extracted/2026-05-01-content-output-contract-source.md` are the M2 acceptance test set for the content production workflow. Re-runnable on any change to this contract or the M2 architecture, parallel to how the 7 founder-voice prompts function as the M1 cold test.

Test set covers:
- Input 1: Single Topic to Full Content Package (Bucket 1)
- Input 2: Reaction Reel from Raw Voice Note (Bucket 2)
- Input 3: Fact or Fiction Format (Bucket 3)
- Input 4: Show and Tell Biomechanics Masterclass (Bucket 4)
- Input 5: Soft Sell Conversion Reel (Bucket 5)

---

## Integration Points

- **Section 2 (Content Creation)** in CLAUDE.md references this contract alongside `content-case-flywheel-v1`
- **Section 7 (Output Translation)** specifies citation format as PMID + exact figure
- **`research-to-system-mapping-v1`** must capture PMID + exact figure as required metadata, not optional
- **`research-index-and-traceability-v1`** must support forward and reverse queries from content output back to research records

---

## Final Definition

This contract is the user-facing artifact spec for The Muscle PT content production. It defines what passes and what fails. Drift from this contract is the highest-priority signal for system refinement.
