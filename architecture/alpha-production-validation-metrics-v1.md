---
doc_id: alpha-production-validation-metrics-v1
version: v1
date: 2026-05-04
type: validation framework (Alpha → Beta transition gate)
purpose: Define what "production-validated" means in measurable terms so Zach's 1-week testing window produces interpretable data instead of impressionistic feedback. Three metrics, each catching a different failure mode (volume / quality / confidence). Per ProjectBrainer review §6 — the single largest unmeasured Alpha→Beta variable.
relevant_doctrine:
  - architecture/alpha-state-record-v1.md (Alpha lock conditions)
  - architecture/alpha-projectbrainer-review-v1.md (§6 future-potential ceiling — defines the metric requirement)
  - architecture/operator-observation-loop-v1.md (Alpha-N entries will record metric data)
linked_artifacts:
  - records/observations/alpha-week-1-metrics-log.md (to be created at window open)
hl_09_evaluation: PASS — no fabricated grounding. Framework defines measurement; introduces no claims about expected results.
hl_10_evaluation: PASS — operator authorization (2026-05-04: *"yes please"* on item 2 of the pre-Zach-window must-resolve list). ProjectBrainer review §6 surfaced this as the dominant strategic gap.
---

# Alpha Production Validation Metrics v1

## Why this document exists

Pre-Alpha tests validated doctrine-fidelity (does the system follow CLAUDE.md instructions under fresh-chat execution?). They did not validate production-readiness (does the system actually scale Zach's professional output?). Without explicit success criteria, Zach's 1-week window produces impressionistic feedback — which is not a basis for the Alpha → Beta promotion decision.

This document defines the three metrics, the threshold for each, the measurement protocol, and what the metrics cannot catch.

---

## The three failure modes

A doctrine-engineered LLM system that scales a professional's output can fail in three independent ways:

1. **Volume failure** — the system slows the operator down. Doctrine costs more time than it saves. The closed-loop discipline, the gate confirmations, the audience-translation pass — each adds friction. If the friction outweighs the throughput gain, the system is anti-leverage.
2. **Quality failure** — the system's output isn't the operator's. Substance is generic-Claude wearing The Muscle PT's voice. The output reads acceptably but doesn't reflect the operator's clinical judgment, content instinct, or business intuition. If the operator has to rewrite to make outputs *his*, the system isn't an extension of his expertise — it's a stylistic veneer.
3. **Confidence failure** — the operator doesn't trust the output. He uses the system, but verifies everything independently before delivering. This defeats the leverage entirely: doing the work AND reviewing the system's work is more effort than just doing the work.

A system can produce lots of fast output the operator doesn't trust. A system can produce slow trustworthy output that doesn't scale time. A system can produce trustworthy fast output that's generic. The three metrics catch each failure mode separately.

---

## Metric 1 — Output Velocity

**Definition.** Volume of deliverable artifacts produced per day, across the 5 modes the system supports.

**Measurement.** Daily count, segmented by mode:

- **Clinical Mode**: number of clinical programs / case interventions / reassessment plans designed end-to-end
- **Insight Mode**: number of Insight content pieces shipped (drafted to publish-ready)
- **Script Mode**: number of Exercise-to-Script transformations completed
- **Business Mode**: number of business decisions documented (pricing, packaging, partnership, scaling)
- **Carousel** (deferred): not measured during Alpha window unless Carousel Mode is in scope

Daily totals roll up to a weekly velocity figure across all modes used.

**Baseline.** Set BEFORE the window opens. Zach self-reports his typical weekly volume across the same categories from the prior 4 weeks (without the system). Document the baseline in `records/observations/alpha-week-1-metrics-log.md` at window open. Baselines are honest estimates, not audited counts — the bar is Zach's own pre-system pace.

**Threshold.** ≥ 1.5× baseline weekly volume on at least one mode actually used during the window. The 1.5× threshold says: the system has to deliver enough leverage to justify the friction of using it. Less than 1.5× and the operator is better off doing it manually.

**Failure read.** Velocity below threshold = volume failure. Doctrine friction > throughput gain. Implication: the doctrine is over-specified relative to its leverage; compaction (deferred Tier-1 work) becomes load-bearing for Beta.

**What invalidates this metric:**

- Pro-account session-limit hits during the window. If budget binds before deliverables finish, velocity is artificially low for tier reasons, not doctrine reasons. Pre-Alpha-9 budget test (item 1 of the pre-window list) is the precondition that lets velocity readings be interpretable.
- Mode-coverage skew. If Zach only uses Clinical Mode all week, velocity on Clinical may pass threshold while the other modes' doctrine remains unvalidated. The metric reads as "Clinical Mode validates production velocity"; it does not read as "5-mode surface validates production velocity."

---

## Metric 2 — Output Quality Pass Rate

**Definition.** Percentage of system outputs Zach delivers (to clients, to social, to operations) without major rewrite.

**Measurement.** For every system output Zach uses, he categorizes the outcome at delivery time:

- **(a) Shipped as-is** — output went out exactly as the system produced it
- **(b) Shipped with minor edits** — small adjustments (a sentence changed, a parameter swapped) but the substance is the system's
- **(c) Major rewrite** — Zach kept the structure or some content but rewrote substantively
- **(d) Discarded** — output rejected; Zach started over manually

Daily logging: per output, one category. Categories (a) and (b) count toward the pass rate; (c) and (d) count against.

**Threshold.** ≥ 70% of outputs in (a) or (b) across the week, AND no day below 50%.

The week-level ≥70% says: the system's substance is reliably Zach's. The daily ≥50% guardrail catches the case where the week passes on average but one mode (e.g., Insight) is consistently failing — which the rolled-up weekly number would hide.

**Failure read.** Pass rate below threshold = quality failure. The system's output isn't Zach's expertise — it's generic Claude output dressed in The Muscle PT language. Implication: the doctrine constrains form but not substance; either the Research Layer needs deeper grounding, the engine specs need more substantive content rules, or the system isn't the right leverage for the failing mode.

**What invalidates this metric:**

- Quality bar drift. Zach rates his own output; the bar is implicitly defined by his standards. If he drifts toward "it's good if I shipped it" the pass rate rises artificially. Mitigation: at week end, Zach reads back through the (a) and (b) outputs and re-rates honestly. Anything he wouldn't ship today gets re-categorized.
- Sample size. If only 5 outputs land during the week, percentage is noisy. Floor: report as raw counts as well as percentages when total is below 10.

---

## Metric 3 — Decision Confidence

**Definition.** Percentage of clinical and business decisions where Zach acted on the system's recommendation without seeking outside verification.

**Measurement.** For every decision the system surfaces a recommendation on (whether through closed-loop gates, refinement-008 mid-mode multi-way decisions, or any other mode), Zach logs:

- **(a) Acted on recommendation directly** — confirmed and moved on; no outside verification before acting
- **(b) Acted after independent verification** — confirmed but verified independently first (re-ran the analysis, looked up the source, asked someone, checked his clinical training)
- **(c) Overrode** — chose a different path

Categories (a) and (c) both count toward the confidence metric. (a) is "trusted the system enough to act"; (c) is "trusted his own judgment enough to override clean." Only (b) counts against — that's the leverage-defeating pattern of doing the work AND reviewing the system's work.

**Threshold.** ≥ 60% (a) + (c) combined, AND ≥ 30% (a) alone.

The combined ≥60% says: the system isn't slowing decisions down with verification overhead. The (a)-alone ≥30% says: the operator is actually trusting the system's recommendations on at least a third of decisions, not just overriding them all.

**Failure read.** Confidence below threshold = trust failure. The operator uses the system but doesn't trust it; the leverage is theoretical. Implication: HL-09 strict has earned reliability on grounded claims, but the system's *judgment* (when to invoke a hard lock, which option to recommend in a multi-way decision, when to defer) hasn't earned operational trust. Watch the (b) bucket for patterns — what specifically is Zach verifying? That's the layer the system hasn't earned trust on.

**What invalidates this metric:**

- Decision selection bias. If Zach only invokes the system on low-stakes decisions, confidence reads high for trivial reasons. Mitigation: at week end, retrospectively flag any high-stakes decisions made WITHOUT consulting the system. If those count materially, the system isn't being load-tested at the actual confidence bar.
- The operator-as-builder dynamic. Josh built the doctrine; he knows where it's weak. Zach hasn't been through the build; he won't know which recommendations the doctrine covers vs. which are model-default. (b) may be inflated early in the week as Zach learns the doctrine's reliable surfaces. Recommend: report metric segmented by week-half (days 1–3 vs. 4–7) to detect learning curve vs. persistent friction.

---

## Threshold logic — what passes Alpha → Beta

| Metric | Threshold | Interpretation |
|---|---|---|
| Velocity | ≥1.5× baseline on ≥1 mode used | System delivers leverage on at least one mode |
| Quality pass rate | ≥70% week, ≥50% any day | System's substance is Zach's |
| Decision confidence | ≥60% (a)+(c), ≥30% (a) alone | System has earned operational trust |

**All three pass:** Alpha is production-validated. Beta scoping (Carousel Mode, mode-coverage expansion, doctrine compaction) proceeds with confidence.

**Two pass, one fails:** the failing metric defines the Beta scope. Don't ship Beta features until the underlying gap is addressed.

**One or zero pass:** Alpha is doctrine-fidelity-only. The system isn't load-bearing for production. Either narrow the scope (system covers fewer modes but works on those), or fundamentally rework the failing axis.

**Special case — Pro-account budget binds before week ends:** velocity reads are invalid; quality and confidence are still readable. Make Velocity reading conditional: "valid IF account budget did not bind."

---

## Measurement protocol

**Logging file.** Create `records/observations/alpha-week-1-metrics-log.md` at window open. Daily entries with a single table per day per mode used. End of week: weekly rollup table + interpretive paragraph from Zach + any qualitative observations he wants captured.

**Logging cost ceiling.** Total logging time ≤10 minutes per day. If logging takes longer, the protocol itself becomes anti-leverage. The point is operational measurement, not academic data collection.

**Baseline-setting timing.** Before window opens: Zach writes pre-system baselines (volume, typical quality categories he experiences with manual production, decision-making patterns). Captured in the log file's preamble. No baselines, no validation framework — the metrics need a reference.

**Window definition.** "1 week" = 7 calendar days from the operator-declared start. Stop the clock for non-business days only if Zach typically takes them off pre-system (otherwise the comparison is uneven).

**End-of-window read.** Zach (operator) and Josh (system architect) review the log together. Each metric: pass/fail vs. threshold, with the noted invalidation conditions checked. Interpretive notes go into the Alpha-N analytical entry in `architecture/operator-observation-loop-v1.md`.

---

## What these metrics cannot catch

Honest framing — these three metrics validate production-leverage but do NOT validate:

1. **Doctrine load-bearing-vs-decorative.** If all three metrics pass, that's evidence the system as a whole works. It is NOT evidence that any specific part of the doctrine (refinement-008's recommendation discipline, refinement-013's audience model, the closed-loop discipline rules) is load-bearing. Beta compaction work still needs separate validation.
2. **Mode coverage.** If Zach uses Clinical Mode all week and ignores the others, three metrics pass for Clinical only. Insight, Script, Business remain doctrine-locked but production-untested. Alpha-N entries should explicitly track mode coverage and flag unused modes as still-unvalidated.
3. **Time-horizon failures.** A week is short. Some failure modes only surface over months — operator burnout from doctrine friction, drift in output style, accumulated correction debt. Alpha 1-week passes are necessary, not sufficient, for Beta promotion.
4. **Bespoke-vs-transferable.** The metrics validate the system on Zach. They say nothing about whether the doctrine pattern transfers to a hypothetical second operator. ProjectBrainer §6 flagged this as the largest strategic question; it requires a separate test (a second-operator hypothetical or pilot) outside Zach's window.
5. **Operator-affordance gaps.** If the mode-spanning prefix pattern is only known to Josh, Zach may underuse the system in week 1 because he doesn't know its full surface. Velocity reads low, but the cause is onboarding gap, not system gap. Mitigation: 30-min Zach onboarding (item 4 of pre-window list) closes this before measurement starts.
6. **The actual business question.** Output velocity, quality, and confidence are necessary conditions for the system having business value. They are not sufficient. Whether the system actually moves Zach's revenue, client outcomes, or work satisfaction is a quarter-scale measurement, not a week-scale one.

---

## Calibration before the window opens

The thresholds (1.5× / 70% / 60%) are starting points, not received truth. Before the window opens, Zach and Josh review the proposed thresholds and adjust based on:

- Zach's read of what 1.5× would actually require him to ship
- Whether the Quality pass rate threshold is too tight or too loose given his actual quality bar
- Whether the Decision confidence (a)-alone ≥30% threshold is realistic given Zach's relationship to outside verification

The recalibrated thresholds get committed to this doc as v1.1 before window open. After week 1, threshold revision based on data is allowed (Beta cycle) — but only with explicit reasoning recorded.

---

## Pointer back

- **Operator**: Josh
- **Founder**: Zach
- **Date**: 2026-05-04
- **Status**: v1 draft pending Zach calibration. Window-open dependency: thresholds confirmed + log file initialized + baselines recorded.

Once thresholds are calibrated and items 1, 3, 4 of the pre-window list complete, Alpha window opens. End-of-window review against this framework is the gate to Beta.

---

## Last Updated

2026-05-04 — initial validation framework authored. Three metrics (Output Velocity / Output Quality Pass Rate / Decision Confidence) target three independent failure modes (volume / quality / confidence). Thresholds proposed (≥1.5× baseline / ≥70% pass rate / ≥60% combined trust + ≥30% direct-action). Measurement protocol specified (≤10 min/day logging cost, baseline-setting before window, end-of-window joint review). Six explicit limitations recorded: load-bearing-vs-decorative gap, mode coverage gap, time-horizon limit, bespoke-vs-transferable gap, operator-affordance dependency, business-question scope. Pending Zach calibration of thresholds before window opens.
