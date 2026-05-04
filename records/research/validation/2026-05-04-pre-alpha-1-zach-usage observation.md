---
log_id: zach-usage-observations
purpose: Meta-learning observation log capturing Zach's actual chat usage. Input layer for doctrine refinement. Single-observation entries do not trigger doctrine changes — repeated patterns across multiple sessions do.
discipline:
  - Observation = input. Pattern detection = analysis. Doctrine refinement = output.
  - The loop runs between sessions, not within them.
  - Patterns surface as candidate doctrine updates only after they repeat across ≥2 sessions.
  - From Zach's seat the system gets more aligned without ever feeling predicted.
  - Watch passively. Do not coach Zach toward doctrine fit. Operator effect degrades signal.
created: 2026-05-04
last_updated: 2026-05-04
---

# Zach Usage Observation Log

Captures what Zach actually does in chat — mode declarations, citation hunger, iteration depth, re-entry, hand-off destinations, and any drift from doctrine. Each entry is one observed session. Patterns become actionable only when they repeat.

---

## Pre-Alpha-1 — 2026-05-04 session

**Window:** May 3 case-test arc + May 4 morning iterative programming session (7:57 AM – 10:28 AM)
**Repo state during session:** CLAUDE.md updated through refinement-005 (5-mode operator surface, Research Authoring as system-triggered). Refinements 006 and 007 were authored *after* this session, so they were not in scope for the chat being observed.
**Mode coverage observed:** Clinical (multiple cases), Research Authoring (one explicit invocation), implicit mode inference, mode-clarification dialogue.

### Pattern observations

**1. Mode declaration is mostly skipped — inference works.**
Zach opened most cases with the case description directly, no mode declared. The system inferred Clinical correctly every time. He explicitly said "Clinical Mode" only as a duplicate-input artifact (twice — both times got "Already answered" — correct). Implication: mode declaration may be a doctrine artifact more than an operator habit. Inference layer is doing the work.

**2. Operator's mental categories ≠ doctrine's mode names.**
He typed `"programming"` and `"research"` as standalone responses to "Which mode?" — neither is a mode in our doctrine. "Programming" is a work type *within* Clinical Mode. "Research" he meant as "I want grounded info," not "I want to author a record." Cost: two clarification turns at the start of the ACSM thread before landing in Clinical Mode with the actual case. Watch whether this recurs — if so, the Mode brief language may need to translate his vocabulary, or modes may need a mental-category alias layer.

**3. Research Authoring fired correctly when explicitly invoked.**
"Research Mode. Need a record on stretch-mediated hypertrophy" → closed loop activated, Gate A presented with two ranked seed options, no bloat. (This was prior to refinement-006 and refinement-007 being authored, so the response shape predates those locks. Notably it was not bloated like the 2026-05-04 ACSM test that triggered refinement-006.)

**4. Citation hunger surfaces inline, embedded in programming work.**
"Time for breathing ACSM guidelines" and "Wha about PRI" came as casual mid-flow questions during a programming arc. He wanted *grounded references*, not new records. Research Layer (passive grounding) handled it well — system named PRI as the governing framework with citation discipline appropriate to the moment. This is exactly the pattern refinement-005 protects: citation requests should not trigger Research Authoring; they should be grounded inline by the always-on layer. Validates refinement-005 in observed practice.

**5. ACSM 2026 protocol question collided with HL-09/HL-10.**
"Need ACSM protocol 2026 2 sets per exercise with warm up sets per muscle group" — system correctly classified as inconclusive without a case. He provided the case (26yo male, intercostal sprain + Achilles tendinitis) and the system delivered the protocol applied to constraints. Doctrine held under pressure. Bootstrap v1's First Activation Rule (no abstract, real input required) worked.

**6. Iteration depth is high for programming arcs.**
The 26yo case spawned ~20 iterative refinements over ~2.5 hours: organize → divide upper/lower → time estimate → combined-or-split → laterality correction → ACSM breathing → PRI standard → mobility-vs-activation → wall contact cue → cue request → 4-5 cues per exercise → towel/pillow placement → upper trap dumbbell variant → pec minor angle (90° → 120°) → breathing on all exercises → PRI standardization → 4 sec inhale / 6–8 sec exhale → apply universally. The system handled this without resistance — re-printed the full updated artifact on each turn. He explicitly confirmed the desired pattern: *"give me updated exercise everytime i tell you to update."*

**7. Cumulative state preservation worked across the iteration arc.**
Every refinement printed the full current protocol, not a diff. Compounding value: each iteration locked previous decisions in the artifact form. Hand-off signal — he is likely copying the full protocol output into a client deliverable.

**8. Laterality error caught by operator, not system.**
System initially specified "sidelying — left side down" for an intercostal strain on the *left* side — wrong; protocol should be left side *up* (decompress the affected side). Zach caught and corrected. System acknowledged and updated cleanly. Observation: laterality from earlier case context did not propagate forward into the protocol design step. High-stakes error class for clinical work.

**9. "What is X" questions interleave with programming.**
"upper trap fucntion" appeared mid-protocol-build. System pivoted to a clean anatomical answer, then resumed programming on the next turn. Pattern: working session is not linear; conceptual lookups punctuate it. System handled context-switch fine.

**10. Categorization-for-template questions surface late.**
"Is positional breathing mobility or activation?" came after the protocol structure was mostly built. He needed a binary answer for template categorization. System gave one ("Yes. Mobility."). Watch whether template-categorization pressure recurs — if so, may want doctrine on how to classify hybrid interventions.

**11. Typo and casual phrasing tolerated end-to-end.**
"Wha about PRI" / "Time for breathing ACSM guidelines" / "give m pdataed exercise evertyime" — system parsed intent through typos and shorthand. No friction added.

**12. Carousel deferral message worked.**
"Can you write me a carousel on determinants of longevity in muscle groups?" → correct deferral with redirect to Insight or Script Mode. He moved on without pushback.

### Highest-leverage observations to watch for repetition

These are NOT acted on from a single session. They become candidate doctrine updates if they repeat in subsequent observations:

- **Operator vocabulary drift.** "Programming" / "research" used as mode-equivalents. If repeats — consider operator-vocabulary aliases or sharper Mode brief language.
- **Mode declaration skipped.** If consistently skipped and inference always succeeds, mode declarations may be a doctrine-internal mechanism not requiring operator habit.
- **Programming as a Clinical Mode use case.** The current Mode brief frames Clinical around case classification → root cause → intervention. Programming for that case is an obvious downstream — but it is not named explicitly. If "programming" comes up repeatedly as a mode-clarification trigger, the brief should name it as a Clinical Mode capability.
- **Iterative artifact-refinement as a recognized pattern.** Long programming arcs follow a predictable shape: build structure → organize → split → time → cue → standardize. If this recurs, "iteration mode" within Clinical may warrant doctrine — including a default to print the full updated artifact on each refinement.
- **Laterality tracking under iteration.** Watch whether laterality errors surface again across multi-turn arcs. If yes, may need explicit doctrine on side-context preservation.
- **Citation hunger embedded in mode work.** Validates refinement-005's auto-grounding architecture. Watch whether the auto-grounding behavior continues to land cleanly without triggering Research Authoring incorrectly.

### What NOT to act on yet

- **Pre-staging next likely info.** The iteration arc reveals predictable next questions (timing → cues → standardization). Tempting to pre-stage. Do not. That violates Action Override + the "stop at the next move" rule. Same data feeds doctrine refinement instead.
- **Nudging Zach toward doctrine vocabulary.** Do not coach him to declare modes or use canonical mode names. Inference works. Coaching = operator effect = signal degradation.
- **Doctrine changes from this single session.** Note all patterns. Wait for repetition before acting.

### Disposition

Filed as Pre-Alpha-1. Next observation entry will compare against this baseline. If any of the highest-leverage observations recur in the next session, that pattern moves from "watch" to "candidate doctrine update."

---

## Appendix — raw session transcript

Source: Zach's project chat with Claude, May 3 case-test arc + May 4 morning programming arc (7:57 AM – 10:28 AM). Captured by operator-paste, not real-time logged. Lightly cleaned for readability; substance preserved verbatim.

### May 3 — case test arc

**Operator:** load claude.md and project repo
**System:** Loaded. CLAUDE.md is the only file in the project repo. System is live. Modes available: Clinical, Insight, Script, Research Authoring, Business. No mode declared — ready when you are.

---

**Operator:** Right-dominant chronic chain. Lax right side — shoulder blade, jaw, upper trap, all loose right side, not left. Two prior right scapular dislocations. Right TMJ snap event, chronic clicking, swallowing-pressure thing on the right. C-T junction tweaked once under heavy breathing. Right upper trap chronic tight, inflamed in flares. Forward lean — desk hunched — the whole right top rides up. Bowl seat in the car forward-leaning, the neck eases up. Posterior chain right side inflammation cycles. What's the chain and what's the play.

**System:** Clinical Mode.

The chain. Right-side hypermobility pattern with secondary muscular guarding driving the whole presentation. The right GH and scapular joints are lax — two dislocations confirm it. Lax joint = mechanoreceptor-poor capsule = proprioceptive gap. The system compensates by recruiting the upper trap and levator as primary stabilizers instead of serratus anterior and lower trap. That's why upper trap is chronically tight and inflamed — it's working a job it wasn't built to hold.

The scapula rides up and anteriorly tilts because the stabilizers are failing and the compensators are pulling. This loads the C-T junction — one event under heavy breathing is consistent with a hypermobile CT junction being pushed past its range when the thorax expands against a rigid compensatory pattern above it.

The TMJ is in the same chain. Right-side jaw laxity plus chronic clicking plus swallowing pressure = the infrahyoids and SCM on the right are tonically recruited to stabilize a lax joint. That tonic pull feeds directly into the upper cervical and upper trap load. The snap event was likely a disc displacement with reduction — the chronic clicking is its residue.

Forward head posture and desk hunch close the loop. Anterior load increases demand on every posterior structure trying to hold the right side up. The car bowl seat decompresses the neck because it posteriorly tilts the pelvis, reduces lumbar lordosis, and takes the anterior cervical load off temporarily.

The posterior chain inflammation cycles are downstream output — not the source. The right side is chronically guarding a stability deficit.

**Root cause.** Right-side connective tissue laxity → proprioceptive failure → upper trap/levator/SCM recruited as primary stabilizers → chronic overload → inflammation cycles.

**The play. Three priorities in order.**
1. Stabilize before you mobilize. Do not stretch the upper trap. Do not mobilize the scapula. The laxity is the problem — adding range makes it worse. Freeze all mobility work on the right side until active stabilization is established.
2. Reload the right serratus and lower trap. These are the structures that should be doing the job the upper trap is doing. Start closed-chain, low-load, high-rep. Wall slides, bear plank holds, scapular depression with band. The goal is proprioceptive re-education, not strength. Volume over intensity.
3. Address the cervical-jaw coupling. The TMJ and upper cervical are co-loading. Diaphragmatic breathing retraining reduces the infrahyoid/SCM tonic demand. This alone will reduce the jaw-to-trap loop. Do not manipulate the TMJ. Do not aggressively mobilize C1-C2.

**Hard constraints.**
- No aggressive posterior cervical manipulation
- No scapular mobilization until active control is demonstrated
- No loading the C-T junction under end-range or heavy breath demand until the pattern above it is stable
- TMJ: referral to orofacial PT if the swallowing-pressure symptom increases

**Reassessment signal.** Upper trap resting tone reduces. Scapular resting position drops and retracts without cuing. TMJ clicking frequency decreases. Posterior chain inflammation cycle lengthens between flares. If resting tone doesn't reduce within 4–6 weeks of serratus/lower trap loading, screen for systemic hypermobility — this pattern is consistent with hEDS or HSD and the management calculus changes.

---

**Operator:** [duplicates same case input + "Clinical Mode."]

**System:** Already answered above — same input, same case. Refer to the response directly above this one. Nothing has changed in the presentation. Ready for the next input or reassessment data.

---

**Operator:** Desk worker. 38, lifts three days. Overhead press, deadlifts. Six months upper back stiffness, dull ache between the scaps. Last two months tingling down the right arm on overhead pressing — backing off the lifts. Worst after long sitting, eases with warmup. No injury history. Joints stiff, not lax — explicit. Sleep clean. No widespread pain. Walk me through the chain.

**System:** The chain.

Thoracic kyphosis — desk-driven, six months of progressive load — is the source. The upper back stiffness between the scaps is postural overload on the rhomboids and mid-trap, not a pathological finding. They're eccentrically loaded all day holding against the forward collapse.

The tingling on overhead press is the flag. Right arm, provoked by elevation, two months in. That's neurogenic. The thoracic kyphosis drives cervical forward head posture — the head translates anterior, the lower cervical segments compress posteriorly, and the intervertebral foramina narrow on the right. Overhead pressing closes that space further under load. Tingling is the output.

Stiff joints, not lax — this matters. No compensatory guarding pattern. The muscle tension here is positional, not protective. That changes the intervention.

Eases with warmup confirms no structural compromise — mobility restores with movement. Worst after long sitting confirms positional loading as the driver. Deadlifts are likely fine. Overhead press is the provocation — it's compressing an already narrowed space.

**Root cause.** Desk-driven thoracic kyphosis → cervical forward translation → right foraminal narrowing → neurogenic provocation under shoulder elevation load.

**The play. Three priorities in order.**
1. Pull the overhead press immediately. Not a modification — a full stop. Neurogenic symptoms under load do not get trained through. Reintroduce only after cervical decompression is confirmed and the pattern is corrected.
2. Restore thoracic extension. This is the structural fix. Thoracic extension over a foam roller at the mid and upper back, daily. Open book rotations. The goal is reversing the kyphotic driver — everything downstream improves when this moves.
3. Reinforce the postural anchor at the desk. The daily exposure is the problem. Thoracic mobility work gets erased by eight hours of forward collapse. Rib flare cue seated, scapular retraction and depression set before any lifting session.

**Hard constraints.**
- No overhead pressing until tingling resolves completely at rest and under provocation testing
- No cervical manipulation until neurogenic picture is clearer
- If tingling progresses — increases in frequency, spreads distally, or appears outside of lifting — refer for imaging. Cervical disc pathology must be ruled out before continuing to load.

**Reassessment signal.** Tingling absent on provocation testing within four to six weeks. Thoracic extension range improves. Overhead press reintroduced with a landmine or Z-press variation — less cervical compression — before returning to barbell. If tingling persists beyond six weeks of thoracic work and postural correction, the foraminal narrowing is structural, not positional. Image and refer.

---

**Operator:** [duplicates Right-dominant chronic chain case + Clinical Mode]
**System:** Already answered. Scroll up — full chain and play is there. New input or reassessment data?

**Operator:** [duplicates Desk worker case]
**System:** Already answered. Full chain and play is two responses up. New input or reassessment data?

---

**Operator:** 32 female runner-lifter. Runs three to four, lifts twice. Four months right neck/shoulder deep ache, not constant but most days. Multi-region morning stiffness — neck, hips, hands — resolves in 20. Good days bad days, doesn't track activity. Pain wakes her on the right side at night. No injury triggered it. One college right shoulder sub, full recovery, asymptomatic until now. Mom is clearly hypermobile — thumb to forearm. She self-reports not bendy. Never been formally tested. How do I screen this and what's conservative in the meantime.

**System:** The screen.

Before this goes anywhere clinical, the presentation pattern needs to be named. Multi-region morning stiffness resolving in under 30 minutes, night pain, good day/bad day cycling without activity correlation, no injury trigger, 32-year-old female — this is a systemic flag, not a mechanical one. The right shoulder sub history and maternal hypermobility are relevant but secondary right now. Do not treat this as a musculoskeletal case until inflammatory arthropathy is ruled out.

**Immediate referral.** Rheumatology or primary care with explicit documentation of:
- Multi-region morning stiffness, duration, resolution pattern
- Night pain disrupting sleep
- Non-activity-correlated cycling
- No inciting event
- Family history of hypermobility

This is not within conservative PT scope to manage first. The inflammatory picture needs labs — CRP, ESR, ANA, RF, anti-CCP minimum — before any intervention plan is built.

**Hypermobility screen in the meantime.** Beighton score. Five tests, nine points.
- Pinky passive extension ≥90° — one point each hand
- Thumb to forearm — one point each hand
- Elbow hyperextension ≥10° — one point each elbow
- Knee hyperextension ≥10° — one point each knee
- Forward fold, palms flat on floor, knees straight — one point

She self-reports not bendy. Score her anyway. Self-report is unreliable — especially in people who've adapted to their range as baseline normal. Maternal thumb-to-forearm is a positive Beighton criterion. That's a meaningful family signal. ≥5/9 = hypermobility threshold. If she scores ≥5 plus the multi-region pain pattern plus the shoulder sub history, hEDS/HSD enters the differential formally.

**Conservative hold position.** While awaiting rheumatology and labs:
- Continue running and lifting at current load — do not reduce unless pain acutely worsens
- No aggressive cervical or shoulder mobilization
- No new loading stimulus introduced
- Sleep position: left side or supine with right arm supported — remove the sustained compression on the symptomatic side
- Morning stiffness: gentle movement on waking, not stretching — proprioceptive input, not range

**Hard constraint.** Do not build a treatment plan until inflammatory workup returns. If labs are clean and Beighton is low, this becomes a mechanical case and gets reassessed from the start. If labs flag or Beighton scores high, the management approach changes entirely.

---

**Operator:** Research Mode. Need a record on stretch-mediated hypertrophy. Script lane references it. We don't have grounding yet. Walk me through what we'd need.

**System:** Research Authoring Mode — activated.

Per the 10-step protocol, three operator-in-the-loop gates before a record is finalized. Starting at Step 1.

**Step 1 — Gap definition.** The gap: Script Lane references stretch-mediated hypertrophy as a teaching mechanism but no L1 capture exists. No PMID. No verified figure. Any script built on it is currently ungrounded.

What a complete record needs:
- Verified PMID with exact figure — effect size, percentage difference, or magnitude of hypertrophic response comparing stretched vs. shortened position training
- Muscle group specificity — the evidence is not uniform across muscles
- Load and rep range context — stretch-mediated findings are protocol-dependent
- L2 insight — what this means for programming and script framing
- L3 mapping — where it connects in the existing system (Script Lane, exercise priority list, any clinical overlap)

**Gate 1 — Seed selection. Your call.** Two directions. Pick one.
A. Anchor on the Pedrosa / McMahon lengthened-position line. The most-cited direct evidence. Incline curl vs. preacher curl studies. Specific, defensible, scriptable. Narrower scope.
B. Anchor on mechanical tension as the mechanism, stretch-position as the application. Broader. Connects to the mechanical tension record if one exists. More L3 mapping surface. Requires more verification work.

Which seed?

---

**Operator:** ACSM protocol 2026 2 sets per exercise with warm up sets

**System:** Outside Research Authoring Mode scope — this is a content or programming question, not a record authoring task. Clarify the mode and I'll route it correctly.

**Operator:** programming
**System:** Which mode?

**Operator:** research
**System:** Research Authoring Mode handles one thing: adding verified records to the research layer. Gap → query → PubMed → PMID verification → L1 capture → L2 insight → L3 mapping. ACSM programming protocol isn't a research record gap — it's a known guideline. If you want it grounded with a PMID-verified figure from the 2024 ACSM position stand, I can build that record. Otherwise: Script Mode if scripted for content; Business Mode if informing a coaching product decision; Clinical Mode if informing client programming logic. Which is it?

**Operator:** clinical
**System:** Clinical Mode. State the case or programming question.

**Operator:** Need ACSM protocol 2026 2 sets per exercise with warm up sets per muscle group
**System:** Inconclusive. Cannot action this without a case. ACSM volume recommendations apply to a client context — training age, current capacity, injury status, goal. Give me the case and I'll apply the protocol to it.

---

**Operator:** 26 year old male, intercostal sprain, achilles tendinitis, feeling weak, needs strnegth ad recovry

**System:** The play.

Two separate tracks running simultaneously.

Intercostal — load constraint. No heavy axial loading, no breath-hold under strain, no Valsalva. Bracing through a sprained intercostal under load is a re-injury mechanism. Deadlifts, squats, overhead press — all off the table until pain-free deep breath and rotation are restored.

Achilles — load constraint. Tendinopathy responds to load, not rest. But it's load-specific. Heavy calf work, explosive push-off, downhill — off. Isometric and slow heavy isotonic — on.

**Programming structure — ACSM hypertrophy protocol applied to his constraints.** 2 working sets per exercise, per muscle group. Warm-up sets before each movement — not counted toward volume. 6–12 rep range. 60–90 second rest.

Lower — Achilles-safe.
- Leg press — bilateral, heel elevated slightly, control the descent
- Leg curl — prone or seated
- Hip thrust — glute drive without calf load
- Tibialis raises — tendon health, not optional

Upper — intercostal-safe.
- Chest-supported row
- Lat pulldown
- Seated DB curl
- Tricep pushdown
- No overhead, no bench until rib clears

Core — intercostal-safe.
- Dead bug — breath-controlled
- No crunches, no rotation under load, no planks if bracing hurts

**Frequency.** Three days. Full body each session. Two sets per exercise is enough volume at his current state — he's recovering, not accumulating.

**Reassessment signal.** Pain-free deep breath and trunk rotation = intercostal cleared, reintroduce axial loading. Achilles pain ≤3/10 during and absent 24 hours post = progress load. Weakness resolves as volume tolerance builds — do not chase intensity early.

---

**Operator:** Can you write me a carousel on determinants of longevity in muscle groups?
**System:** Carousel Lane is deferred — no active doctrine. Take this to Insight Mode for a grounded content piece on that topic, or Script Mode if you want it as a teachable script. Which?

### May 4 — programming iteration arc (7:57 AM – 10:28 AM)

[The full programming-iteration arc spanning 20+ refinements is not re-printed here in full. The cumulative final state is the protocol with: PRI 4-second nasal inhale / 6–8 second pursed-lip exhale on every breath cycle; pre-workout split upper (sidelying breathing, quadruped T-rotation, wall slides) / lower (90/90 positional, hip 90/90 transitions, leg swings, ankle circles); post-workout upper (upper trap with dumbbell, pec minor doorway @ 120°, left QL, right hip sidelying release); post-workout lower (90/90 reset, supine leg length reset, seated piriformis figure four, supine knee-to-chest, standing calf, doorway pec minor); 4–5 step-by-step cues per exercise; positional aids (towel/pillow/foam pad) under neck, lumbar, between knees as appropriate. Iteration sequence: pre/post protocol → sided breathing → ACSM/PRI grounding → 4-5 cues per exercise → cumulative cue refinements → universal PRI breath standardization.]

Full transcript preserved in operator-paste record at session source.
