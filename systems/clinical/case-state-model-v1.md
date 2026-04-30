# THE MUSCLE PT — CASE STATE MODEL v1

## Purpose

This document defines the state and transition model for client cases within The Muscle PT system.

Its purpose is to make case progression:
- explicit
- repeatable
- auditable
- improvable

This layer adds movement logic to the Movement Case Engine so that client cases are not treated as static records, but as evolving system objects.

---

## Core Principle

A case is not just recorded.

A case moves through defined states over time.

Each state:
- has meaning
- allows certain actions
- restricts other actions
- defines possible next transitions

---

## 1. CASE STATE OBJECTIVE

The Case State Model exists to answer:

- What condition is this case currently in?
- What should happen next?
- What transitions are allowed?
- What evidence is required to move forward?
- When should the system hold, advance, or escalate?

---

## 2. CASE STATES

Every case must be assigned one primary state.

### 2.1 Intake

Definition:
- case has been identified
- initial information is being collected
- no intervention decision has been finalized yet

Meaning:
- system is still gathering context

Allowed actions:
- collect assessment signals
- classify case type
- identify probable root cause

Not allowed:
- promote to reusable pattern
- treat as validated intervention logic

---

### 2.2 Active

Definition:
- case has been classified
- initial intervention path is in progress
- case is being actively worked

Meaning:
- system is testing and observing

Allowed actions:
- apply intervention
- record observations
- reassess response
- modify intervention

Not allowed:
- declare validated success from one good response
- promote to rule

---

### 2.3 Improving

Definition:
- the case is showing positive movement
- expected indicators are trending in the right direction
- the intervention appears directionally correct

Meaning:
- the case is responding, but confirmation is still required

Allowed actions:
- continue intervention
- cautiously progress
- record supporting evidence

Not allowed:
- convert to reusable pattern from one isolated success

---

### 2.4 Inconclusive

Definition:
- evidence is mixed, weak, or incomplete
- current signals are insufficient for strong interpretation

Meaning:
- the system should delay strong conclusions

Allowed actions:
- gather more data
- simplify intervention
- extend observation
- revise classification if needed

Not allowed:
- force premature success or failure labeling
- promote to pattern

---

### 2.5 Failed

Definition:
- intervention did not produce expected improvement
- condition stagnated or worsened
- current logic likely contains an error, mismatch, or missing signal

Meaning:
- the system must learn from breakdown

Allowed actions:
- perform failure analysis
- revise classification
- revise root cause
- regress or escalate
- log refinement signal

Not allowed:
- continue the same logic without re-evaluation

---

### 2.6 Validated

Definition:
- the case has produced repeated, reliable success
- improvement is not a one-time event
- the intervention logic has enough evidence to be trusted for similar cases

Meaning:
- the case has moved beyond directional optimism into confirmed usefulness

Allowed actions:
- document as validated pattern candidate
- compare against similar cases
- reuse cautiously in similar contexts

Not allowed:
- immediately convert into universal rule without broader repetition

---

### 2.7 Pattern

Definition:
- multiple validated cases now support the same intervention logic
- the system recognizes a stable repeatable structure

Meaning:
- the case logic can now inform system-level reuse

Allowed actions:
- create reusable pattern entry
- inform case engine refinement
- inform content generation
- inform decision preferences

Not allowed:
- overgeneralize beyond the conditions that produced the pattern

---

### 2.8 Escalated

Definition:
- the case requires a higher level of attention, uncertainty review, or structural correction
- normal case progression is no longer sufficient

Meaning:
- system confidence is reduced or risk is elevated

Allowed actions:
- deeper review
- revised classification
- revised intervention framework
- higher-priority oversight

Not allowed:
- passive continuation under normal workflow assumptions

---

### 2.9 Closed

Definition:
- the case is no longer actively progressing through the system
- a final outcome has been recorded

Possible reasons:
- resolved
- discharged
- handed off
- paused indefinitely
- archived for learning

Meaning:
- case is historically complete, though still available for analysis

Allowed actions:
- archive
- reference
- pattern comparison
- historical review

Not allowed:
- treat as active without reopening

---

## 3. STATE ORDER

The general lifecycle is:

Intake  
→ Active  
→ Improving or Inconclusive or Failed  
→ Validated  
→ Pattern  
→ Closed  

Escalated may occur from:
- Active
- Improving
- Inconclusive
- Failed

Closed may occur from:
- Validated
- Failed
- Escalated
- Inconclusive
- Improving
when the case is intentionally ended or archived

---

## 4. TRANSITION RULES

A case may only move states when evidence justifies it.

### 4.1 Intake → Active
Requirements:
- sufficient assessment signals collected
- case classified
- probable root cause identified
- initial intervention selected

---

### 4.2 Active → Improving
Requirements:
- directional positive change observed
- movement, pain, control, or tolerance improves
- signals align with the intervention hypothesis

---

### 4.3 Active → Inconclusive
Requirements:
- mixed response
- weak or conflicting signals
- insufficient evidence to declare success or failure

---

### 4.4 Active → Failed
Requirements:
- no meaningful progress
- worsening condition
- clear mismatch between logic and outcome

---

### 4.5 Improving → Validated
Requirements:
- repeated positive outcomes
- sufficient confidence in intervention logic
- success not dependent on one isolated session

---

### 4.6 Improving → Inconclusive
Requirements:
- initial progress becomes unclear
- evidence weakens
- new signals complicate interpretation

---

### 4.7 Improving → Failed
Requirements:
- regression occurs
- progression logic proves incorrect
- success signal was misleading

---

### 4.8 Inconclusive → Active
Requirements:
- enough new data collected
- revised intervention is ready for active testing

---

### 4.9 Inconclusive → Failed
Requirements:
- new evidence reveals clear mismatch
- previous ambiguity resolves negatively

---

### 4.10 Failed → Active
Requirements:
- revised classification or revised intervention exists
- case is being re-run under new logic

---

### 4.11 Validated → Pattern
Requirements:
- multiple validated cases support the same logic
- repeatability is confirmed across similar contexts

---

### 4.12 Any State → Escalated
Requirements:
- risk, uncertainty, or breakdown exceeds normal progression logic
- case requires higher-level review

---

### 4.13 Any Non-Active State → Closed
Requirements:
- case has reached a practical endpoint
- learning has been captured
- no further active progression is occurring

---

## 5. STATE BEHAVIOR RULES

### Intake
Bias:
- gather clarity

### Active
Bias:
- test carefully

### Improving
Bias:
- continue with caution

### Inconclusive
Bias:
- delay certainty

### Failed
Bias:
- analyze and revise

### Validated
Bias:
- trust locally, not universally

### Pattern
Bias:
- reuse with boundaries

### Escalated
Bias:
- increase scrutiny

### Closed
Bias:
- preserve for learning

---

## 6. EVIDENCE REQUIREMENTS

State transitions must be supported by evidence.

Valid evidence may include:
- movement quality changes
- pain changes
- control changes
- tolerance changes
- adherence signals
- repeated session outcomes

Weak evidence should not trigger major state promotion.

One positive session does not justify:
- Validated
- Pattern

One failed moment does not always justify:
- Failed
- Escalated

The system must prefer repeated evidence over isolated events.

---

## 7. VERSIONING

Every case state record must include:
- case_id
- state
- date_entered
- recorded_by
- system_version
- intervention_version

Purpose:
- trace what logic was active when the case moved
- enable audit and future comparison
- support refinement based on versioned history

---

## 8. LEARNING INTEGRATION

Case states drive system learning.

### Improving and Validated
Feed:
- successful intervention logic
- content ideas
- potential reusable patterns

### Failed
Feeds:
- refinement needs
- anti-pattern detection
- system correction

### Inconclusive
Feeds:
- uncertainty awareness
- missing signal detection
- future assessment improvements

### Pattern
Feeds:
- system reuse
- case engine refinement
- content authority
- decision preference updates

---

## 9. STORAGE STRUCTURE

Case state records should be stored under:

records/cases/

Recommended organization:
- active/
- successful/
- failed/
- closed/
- patterns/
- templates/

A case may move folders only when state transition is formally recorded.

---

## 10. AUDIT QUESTIONS

For any case, the system should be able to answer:

- What state is this case currently in?
- Why is it in that state?
- What evidence justified the last transition?
- What are the allowed next moves?
- What system version was active at the time?
- Has this logic succeeded before?
- Should this case influence future rules or patterns?

---

## 11. FAILURE MODES

### State Drift
A case changes in practice but not in records.

### Premature Promotion
A case is promoted to Validated or Pattern too early.

### Frozen Ambiguity
A case remains Inconclusive without active effort to gather more evidence.

### Passive Failure
A Failed case is stored but not analyzed.

### Untracked Re-entry
A Failed or Closed case is resumed without formal state transition back to Active.

---

## 12. FINAL DEFINITION

The Case State Model gives the Movement Case Engine movement logic.

It ensures that:
- cases are not static
- transitions are evidence-based
- learning is tied to progression
- successful logic is promoted carefully
- failures improve the system
- repeatable patterns emerge through validated use

---

## SYSTEM SUMMARY

A case enters  
A case is worked  
A case moves through states  
Each transition is evidence-based  
Each outcome teaches the system  
The system improves through structured case movement