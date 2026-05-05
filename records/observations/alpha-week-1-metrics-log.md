---
doc_id: alpha-week-1-metrics-log
version: v1
date_created: 2026-05-04
window_start: TBD (set when Zach begins)
window_end: TBD (window_start + 7 calendar days)
type: production validation log (Alpha → Beta gate)
purpose: Capture Zach's daily and weekly metrics for the Alpha 1-week production testing window. Three metrics, three thresholds, three failure modes (per architecture/alpha-production-validation-metrics-v1.md). End-of-window joint review against thresholds determines Alpha → Beta promotion.
hl_09_evaluation: PASS — log only; no grounded claims.
hl_10_evaluation: PASS — operator-authorized at Alpha lock.
---

# Alpha Week 1 — Metrics Log

> **Reference**: `architecture/alpha-production-validation-metrics-v1.md` (the framework). `architecture/zach-onboarding-v1.md` (operator reference).

---

## Pre-window preamble (fill in BEFORE window opens)

### Baselines (Zach self-reports pre-system pace, prior 4 weeks)

These are honest estimates, not audited counts. The bar is your own pre-system pace.

| Mode | Pre-system weekly volume |
|---|---|
| Clinical (programs / case interventions / reassessment plans) | TBD |
| Insight (content pieces shipped) | TBD |
| Script (Exercise-to-Script transformations) | TBD |
| Business (decisions documented) | TBD |

**Quality baseline**: of pre-system outputs, roughly what % shipped as-is or with only minor edits? TBD%

**Decision pattern baseline**: of business/clinical decisions you make, roughly what % do you act on without seeking outside verification first? TBD%

### Threshold calibration (Zach + Josh together)

The framework proposes:

- **Output Velocity**: ≥1.5× baseline weekly volume on ≥1 mode used
- **Output Quality Pass Rate**: ≥70% week, ≥50% any day, in (a) shipped as-is + (b) shipped with minor edits
- **Decision Confidence**: ≥60% combined (a) acted-directly + (c) overrode, AND ≥30% (a) alone

Adjust the numbers below if Zach's read of his actual capacity differs:

| Metric | Proposed threshold | Adjusted threshold | Reason for adjustment |
|---|---|---|---|
| Velocity | ≥1.5× baseline on ≥1 mode | TBD | TBD |
| Quality pass rate week | ≥70% | TBD | TBD |
| Quality pass rate daily floor | ≥50% any day | TBD | TBD |
| Confidence (a)+(c) combined | ≥60% | TBD | TBD |
| Confidence (a) alone | ≥30% | TBD | TBD |

### Window-open declaration

- **Start date**: TBD
- **End date** (start + 7 calendar days): TBD
- **Account tier**: Pro (Zach's account)
- **Repo state at window open**: <git commit SHA>
- **Pre-Alpha-9 budget test result**: TBD (must complete before window opens; result determines whether Velocity is interpretable)
- **Onboarding completed**: ☐ Zach has read `architecture/zach-onboarding-v1.md`

---

## Daily entries

Copy the template below for each day. Daily logging cost ceiling: ≤10 minutes total.

### Day N — YYYY-MM-DD

#### Outputs produced

For each thing you produced with the system today:

| # | Mode | What it was (1 line) | Quality category | Decision confidence (if rec surfaced) |
|---|---|---|---|---|
| 1 | _e.g. Clinical_ | _e.g. ACL rehab program for 26F_ | _(a/b/c/d)_ | _(a/b/c) or N/A_ |

Quality categories:
- **(a)** Shipped as-is
- **(b)** Shipped with minor edits
- **(c)** Major rewrite
- **(d)** Discarded

Decision confidence categories:
- **(a)** Acted directly on system recommendation
- **(b)** Acted after independent verification
- **(c)** Overrode system recommendation

#### Daily one-liner

> Did the system feel like leverage today, or friction? (One sentence.)

_TBD_

#### Flags raised today (if any)

| Category | Description |
|---|---|
| _Leak / Live closed loop / Iteration arc / Vocabulary drift / Budget binding / Generic output / Trust friction_ | _One line_ |

---

## End-of-window rollup (fill in at window close)

### Volume read

| Mode | Pre-system baseline (weekly) | Window total (7 days) | Multiplier |
|---|---|---|---|
| Clinical | TBD | TBD | TBD |
| Insight | TBD | TBD | TBD |
| Script | TBD | TBD | TBD |
| Business | TBD | TBD | TBD |

**Velocity threshold check**: ≥1.5× baseline on at least one mode used? **TBD (PASS / FAIL)**

**Invalidation check**: did Pro-account budget bind during the window? **TBD (Yes / No)**. If yes, Velocity reading is invalidated.

### Quality read

| Total outputs | (a) as-is | (b) minor edits | (c) major rewrite | (d) discarded | Pass rate (a+b)/total |
|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD% |

**Daily floor check**: was any single day below 50%? **TBD (Yes / No)**. If yes, even if weekly passes, flag the day(s) that failed.

**Quality threshold check**: ≥70% week + ≥50% every day? **TBD (PASS / FAIL)**

**Bar-drift retrospective**: read back through (a) and (b) outputs at week end. Anything you wouldn't ship today? Re-categorize honestly. Updated pass rate after re-rate: TBD%.

### Confidence read

| Total system recommendations | (a) acted directly | (b) acted after verification | (c) overrode | (a)+(c) combined | (a) alone |
|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD% | TBD% |

**Confidence threshold check**: ≥60% (a)+(c) AND ≥30% (a) alone? **TBD (PASS / FAIL)**

**Selection-bias retrospective**: any high-stakes decisions made WITHOUT consulting the system? List them. If material, the system isn't being load-tested at the actual confidence bar.

**Week-half segmentation** (learning curve check):

| Half | (a) % | (b) % | (c) % |
|---|---|---|---|
| Days 1–3 | TBD | TBD | TBD |
| Days 4–7 | TBD | TBD | TBD |

If (b) drops materially across halves, the learning curve is closing the trust gap. If (b) stays high, the friction is persistent.

---

## Threshold summary

| Metric | Threshold | Result | Pass / Fail |
|---|---|---|---|
| Velocity | TBD | TBD | TBD |
| Quality pass rate (week) | TBD | TBD | TBD |
| Quality daily floor | TBD | TBD | TBD |
| Confidence combined | TBD | TBD | TBD |
| Confidence direct | TBD | TBD | TBD |

**Overall Alpha → Beta gate read**:

- **All metrics pass** → Alpha is production-validated. Beta scoping (Carousel Mode, mode-coverage expansion, doctrine compaction) proceeds with confidence.
- **Two pass, one fails** → the failing metric defines Beta scope. Don't ship Beta features until the underlying gap is addressed.
- **One or zero pass** → Alpha is doctrine-fidelity-only. Either narrow scope or fundamentally rework the failing axis.

**This window's read**: TBD

---

## Qualitative observations from Zach

(Free-form. What surprised you? What worked better than expected? What didn't? What made you cringe? What made you say "the system gets it"?)

_TBD_

---

## Mode coverage in this window

Track which modes Zach actually used. Modes not used in week 1 remain doctrine-locked but production-untested.

| Mode | Used? | Outputs produced | Validation status after this window |
|---|---|---|---|
| Clinical | TBD | TBD | TBD (validated / partial / untested) |
| Insight | TBD | TBD | TBD |
| Script | TBD | TBD | TBD |
| Business | TBD | TBD | TBD |
| Carousel | OUT OF SCOPE | N/A | Deferred to Beta |

---

## Watch items surfaced (for Alpha-N analytical entry)

Items observed during the window that should be carried into the operator observation loop:

| # | Observation | Mode | Severity (low / medium / high) |
|---|---|---|---|
| 1 | TBD | TBD | TBD |

---

## Joint review notes (Zach + Josh, end of window)

(Captured during end-of-window joint review meeting.)

_TBD_

---

## Disposition

After end-of-window joint review, file the analytical summary in `architecture/operator-observation-loop-v1.md` under the Alpha-1 entry. Reference this log file as the source. If thresholds need revision based on data, propose Beta-cycle threshold updates with explicit reasoning.

---

## Last Updated

2026-05-04 — template created at Alpha lock; pending baseline + threshold + start-date fill-in before window opens.
