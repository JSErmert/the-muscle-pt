# THE MUSCLE PT — CASE OUTCOME REPORTING v1

## Purpose

This document defines how client outcomes are captured, classified, versioned, stored, and learned from.

The goal is to ensure that:
- successful plans become reusable patterns
- failed plans become refinement signals
- the system improves over time through structured feedback

---

## Core Principle

Every case outcome must teach the system something.

Do not store outcomes passively.

All outcomes must be:
- classified
- structured
- usable for future decisions

---

## 1. OUTCOME TYPES

Every case must be assigned one of three outcome types:

### Successful
- intervention produced expected improvement
- movement, pain, or control improved as intended
- outcome aligns with prediction

### Failed
- intervention did not produce expected improvement
- condition worsened or stagnated
- incorrect assumption or mapping likely occurred

### Inconclusive
- insufficient data
- mixed signals
- requires additional observation

---

## 2. CASE RECORD STRUCTURE

Each case outcome must include:

### Metadata
- case_id
- client_id (or anonymized reference)
- date_recorded
- recorded_by
- system_version
- intervention_version

### Case Definition
- case_type
- root_cause
- severity
- initial_conditions

### Intervention
- intervention_applied
- progression_stage
- constraints_applied

### Outcome Classification
- outcome_type (successful, failed, or inconclusive)

### Observations
- movement_change
- pain_change
- control_change
- adherence_notes

### Outcome Analysis
- what_worked
- what_did_not_work
- why_this_result_occurred

### Next Step
- reinforce
- modify
- regress
- escalate
- observe further

---

## 3. SUCCESS RECORDING

For successful cases:

Capture:
- why it worked
- what signals predicted success
- whether this pattern has appeared before
- whether this can be reused

A successful case should only become a reusable pattern when:
- it has occurred multiple times
- outcomes are consistent
- context is understood

---

## 4. FAILURE RECORDING

For failed cases:

Capture:
- where the breakdown occurred
- whether failure was due to:
  - incorrect classification
  - incorrect root cause
  - incorrect intervention
  - execution failure
  - insufficient data

Failure categories:
- classification error
- root cause error
- intervention mismatch
- progression error
- adherence failure
- unknown

Do not treat failure as noise.

Treat failure as high-value signal for system refinement.

---

## 5. INCONCLUSIVE RECORDING

For inconclusive cases:

Capture:
- what is unclear
- what data is missing
- what must be tested next

Do not force classification prematurely.

Allow the system to gather more evidence.

---

## 6. STORAGE STRUCTURE

All case outcomes must be stored in:

records/cases/

Structure:
- active
- successful
- failed
- closed
- templates

---

## 7. VERSIONING

Every case must include:
- system_version
- intervention_version
- date_recorded

Versioning allows the system to:
- track what logic was used
- identify when improvements occurred
- trace failures back to system state

---

## 8. REFINEMENT INTEGRATION

After recording a case outcome, evaluate:
- is this a repeated pattern
- is this a new pattern
- is this a failure worth escalation

Escalation paths:
- repeated success becomes candidate pattern
- repeated failure triggers system revision
- repeated decision becomes rule update

---

## 9. LOG INTEGRATION

Important learnings must be recorded in:

logs/refinement-log.md

Each log entry should include:
- case_id reference
- summary of learning
- proposed change
- decision outcome

---

## 10. SYSTEM LEARNING LOOP

Case leads to outcome  
Outcome leads to classification  
Classification leads to analysis  
Analysis leads to pattern detection  
Pattern detection leads to rule or system update  
System update improves future cases

---

## 11. AUDIT AND TRACEABILITY

Every stored case must allow:
- reconstruction of decision
- verification of intervention
- understanding of outcome
- traceability to system version

Audit questions:
- was the case classified correctly
- was the root cause reasonable
- was the intervention appropriate
- was the outcome interpreted correctly
- what should change next time

---

## 12. FAILURE MODES

Passive storage:
- storing cases without analysis

Premature pattern creation:
- turning single successes into rules

Ignoring failures:
- not capturing breakdowns

No versioning:
- losing context of decisions over time

---

## 13. FINAL DEFINITION

This layer ensures that:
- good outcomes are reused
- bad outcomes are learned from
- decisions improve over time
- the system becomes more accurate with use

---

## SYSTEM SUMMARY

Record outcomes  
Classify them  
Analyze results  
Extract patterns  
Update system  
Improve future decisions