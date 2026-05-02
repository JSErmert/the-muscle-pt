---
entry_id: 2026-05-01-content-output-contract-source
date: 2026-05-01
classification: source-spec (founder-authored content production contract)
source: pasted into builder session by Josh, originating from Zach (founder)
linked_decisions:
  - decision-014-m2-acceleration-with-content-output-contract
linked_doctrine:
  - execution/content-output-contract-v1.md (derived from this source)
  - architecture/m2-operationalize-milestone-plan-v1.md (uses the 5 INPUT COMMANDS as acceptance test fixtures)
confidence_level: high (founder-authored, explicit and complete)
---

# Source Spec — Content Output Contract + 5 Input Test Fixtures

This is the canonical source-level reference for the Muscle PT content production contract. Saved verbatim per the founder archive convention. The structured doctrine derived from this spec lives at `execution/content-output-contract-v1.md`. The 5 INPUT COMMANDS become M2 acceptance test fixtures.

---

## Verbatim Source

Here are some examples of what to input: Here are 5 input commands for Josh's testing — designed to stress test whether his system can replicate the workflow we have built:

INPUT 1 — Single Topic to Full Content Package

"Reel — Why should you care about training your hamstrings."

Expected output:

- Bucket tagged correctly (Why Should You Care)
- 60 to 90 second runtime script following the master framework — Hook → Setup → Mechanism → Tie In → Sign Off
- Hook is ambiguous, under 10 words, creates curiosity
- Voice matches mine — direct, clinical, toddler simple, no motivational filler, no cringe phrases
- Verified PMID with exact figure cited correctly above the three dots in caption
- Caption is 3 to 5 lines, no hashtags, no exclamation marks on CTA, ends with affiliate line
- Sign off: "I am the Muscle SPT. And that is why you should care."
- TEXT ON SCREEN brackets included for editor

INPUT 2 — Reaction Reel from Raw Voice Note

"Scrolling through my feed reaction reel. Guy is doing a behind the neck press with a barbell saying it's the best shoulder builder. My take — risky for shoulder mechanics in most people unless you have full overhead range, the trade off between perceived benefit and impingement risk is poor for the average lifter, better alternatives exist with same stimulus and lower risk. Talk about anatomy and why."

Expected output:

- Bucket tagged Scrolling Through My Feed
- Measured nuanced tone — not rage bait, validates what is true and corrects what is not
- Anatomy explained accurately (glenohumeral joint mechanics, subacromial space, scapular upward rotation requirements)
- Clinical reasoning for why it is risky — connects to broader shoulder health framework
- Better alternative offered with anatomical justification
- 60 to 90 seconds, full caption, PMID verified

INPUT 3 — Fact or Fiction Format

"Fact or fiction. Static stretching before lifting reduces your strength acutely. Fact."

Expected output:

- Bucket tagged Random Fun Facts or Science Explained
- Locked Fact or Fiction format — Hook → "Fact" or "Fiction" stated clearly → mechanism → research → tie in
- TEXT ON SCREEN reflects the format — "Fact or Fiction?" then "FACT" or "FICTION" reveal
- Specific research citation with figures (effect size, percentage decrease in force production, duration of effect)
- Practical application included
- Caption follows the format

INPUT 4 — Show and Tell Biomechanics Masterclass

"Biomechanics masterclass on the dumbbell row. Talk about anatomical function, primary mover, secondary movers, scapular mechanics, what cues to use, common compensations to avoid, why this exercise is in my programming."

Expected output:

- Opening line — "Okay class. On today's episode of Zach Teaches You Biomechanics we are going over the dumbbell row."
- Bucket tagged Show and Tell — Biomechanics Masterclass
- Anatomy accurate — primary movers (lats, rhomboids, mid traps, posterior delts), secondary movers, scapular retraction and depression mechanics
- Cue language matches mine — points of contact, stack maintenance, pinky and index finger emphasis if relevant
- Common compensation pattern identified and addressed
- Tied to functional outcome — why this matters for posture, daily life, injury prevention
- 60 to 90 seconds, caption follows format

INPUT 5 — Soft Sell Conversion Reel

"Soft sell reel. If I had 12 weeks to transform my body and I could only focus on 5 things, this is what I would do."

Expected output:

- Bucket tagged Soft Sell — Bottom of the Funnel
- Direct confident value-led tone — never pushy
- 5 specific actionable items in priority order — protein, resistance training, sleep, steps, calorie management or similar
- Each item includes a specific rationale not just the directive
- Tie in connects to coaching offer naturally — never forced
- Sign off includes the soft CTA: "Coaching applications and consultations are open — link in bio"
- Caption ends with the soft CTA — replaces standard like and follow line
- 60 to 90 seconds, no hashtags, affiliate line at the bottom

THE OVERARCHING TEST — Does Josh's System Actually Replicate My Voice?

Across all five outputs the test is whether the system produces content that:

1. Sounds like me — not generic AI
2. Hits exact runtime — 60 to 90 seconds
3. Cites verified PMIDs with exact figures — never fabricated
4. Follows my caption format precisely — no hashtags, no exclamation, three dots, affiliate line
5. Tags the correct bucket without me telling it
6. Includes the appropriate sign off based on bucket
7. Maintains clinical accuracy without sacrificing accessibility
8. Avoids every banned phrase — non-negotiable, game changer, all day long, dial it in, motivational filler

If Josh's system can pass these five tests reliably across multiple runs — the workflow is functional. If it drifts on any one of them — that drift point is where the next iteration of the system needs to address constraints.

---

## Classification

- **Type:** founder-authored output contract + acceptance test set
- **Domain:** content production (M1 Content Creation lane + M2 research grounding)
- **Layer impact:** M1 (interaction layer enforces voice/format/banned phrases), M2 (research layer must produce PMID + exact figure citations)
- **Required for:** founder testing of the system in compressed Phase 2 / M2 acceleration

## Interpretation

This source materially expands what M2 is. The earlier framing of M2 as *"research grounding for clinical decisions"* is too narrow. M2 is the engine that powers the content production workflow itself — and research grounding (PMID + exact figures) is necessary infrastructure for that workflow, not an end in itself.

The 5 INPUT COMMANDS define the M2 acceptance test set, parallel to how the 7 founder-voice prompts define the M1 cold test (decision-011, decision-012).

The OVERARCHING TEST defines pass/fail criteria for content production — not just "is the system producing content" but "is the system producing content that replicates Zach's voice while meeting clinical accuracy and citation standards."

## System Mapping

- **Output contract** → `execution/content-output-contract-v1.md` (new doctrine file)
- **5 INPUT COMMANDS** → preserved here as test fixtures; referenced by `architecture/m2-operationalize-milestone-plan-v1.md`
- **Voice contract** → enforced via Output Translation (Section 7) and the new Content Output Contract
- **Citation format (PMID + exact figure above three dots)** → updated in CLAUDE.md Section 7 and the new Content Output Contract
- **Banned phrases** → hard constraint, enforced at content output generation
- **Bucket auto-tagging** → behavior the system must demonstrate; not yet a doctrine file but lives inside the Content Output Contract as a classification rule
