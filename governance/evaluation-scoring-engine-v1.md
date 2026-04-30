# THE MUSCLE PT — EVALUATION / SCORING ENGINE v1

## Purpose

This document defines how the system evaluates:
- client case outcomes
- intervention effectiveness
- content performance
- research signal strength

The goal is to transform the system from:
- learning from experience
to:
- optimizing decisions based on measured performance

---

## Core Principle

Every output must be evaluated.

Evaluation enables:
- comparison
- prioritization
- refinement
- system improvement

---

## 1. OBJECTIVE

The Evaluation / Scoring Engine exists to:

- measure outcome quality
- assign confidence to decisions
- distinguish strong signals from weak signals
- support prioritization
- guide system refinement

---

## 2. SCORING DOMAINS

The system evaluates four domains:

### 2.1 Case Outcomes
Client progression and intervention results

### 2.2 Interventions
Effectiveness of applied strategies

### 2.3 Content
Performance and impact of output

### 2.4 Research Signals
Strength and reliability of knowledge inputs

---

## 3. SCORING SCALE

All scoring uses a normalized scale:

- 1 = very poor
- 2 = poor
- 3 = moderate
- 4 = strong
- 5 = excellent

Scores must reflect evidence, not opinion.

---

## 4. CASE OUTCOME SCORING

Each case must be evaluated across four dimensions:

### Movement Change
- 1 = no improvement or worse
- 3 = moderate improvement
- 5 = clear and consistent improvement

### Pain Response
- 1 = increased or unstable
- 3 = partially improved
- 5 = consistently improved or resolved

### Control Quality
- 1 = poor or degraded
- 3 = moderate improvement
- 5 = strong, stable control

### Consistency
- 1 = inconsistent results
- 3 = mixed results
- 5 = repeatable and reliable outcomes

---

### Case Score Calculation

Average the four dimensions:

Final Case Score = mean of:
- movement
- pain
- control
- consistency

---

## 5. INTERVENTION EFFECTIVENESS SCORING

Each intervention is evaluated on:

### Fit to Case
- 1 = mismatch
- 3 = partial fit
- 5 = strong alignment

### Outcome Impact
- 1 = no effect
- 3 = moderate effect
- 5 = strong effect

### Repeatability
- 1 = one-off success
- 3 = occasional success
- 5 = consistent across cases

---

### Intervention Score

Average:
- fit
- impact
- repeatability

---

## 6. CONTENT PERFORMANCE SCORING

Each content piece is evaluated on:

### Engagement Quality
- 1 = low interaction
- 3 = average engagement
- 5 = high engagement

### Signal Strength
- 1 = weak or generic idea
- 3 = moderately useful insight
- 5 = strong, clear insight

### Alignment
- 1 = off-mission
- 3 = partially aligned
- 5 = fully aligned with mission

---

### Content Score

Average:
- engagement
- signal strength
- alignment

---

## 7. RESEARCH SIGNAL SCORING

Each research entry is evaluated on:

### Evidence Strength
- 1 = weak or limited
- 3 = moderate
- 5 = strong (meta-analysis, consistent evidence)

### Applicability
- 1 = not relevant to current system
- 3 = somewhat applicable
- 5 = directly applicable

### Consistency with System
- 1 = conflicts with observed outcomes
- 3 = unclear
- 5 = aligns with case data

---

### Research Score

Average:
- evidence strength
- applicability
- consistency

---

## 8. CONFIDENCE LEVELS

Scores map to confidence levels:

- 1–2 → low confidence
- 3 → moderate confidence
- 4–5 → high confidence

---

## 9. SCORE USAGE

Scores must be used to:

### Prioritize
Higher scores receive:
- more attention
- more reuse
- more promotion

---

### Filter
Low scores:
- require reassessment
- should not be promoted

---

### Promote
High scores:
- candidate for pattern
- candidate for rule
- candidate for content reuse

---

## 10. INTEGRATION WITH SYSTEM

### Case State Model

Scores influence transitions:

- high scores → move toward validated
- low scores → move toward failed or inconclusive

---

### Prioritization Engine

Scores affect queue ordering:

- low scores → higher priority for review
- high scores → lower priority for intervention

---

### Content Flywheel

Scores determine:
- which content to double down on
- which content to discard

---

### Research Mapping

Scores determine:
- which research influences decisions
- which research is deprioritized

---

## 11. REFINEMENT RULES

Repeated high scores:
- candidate for pattern creation

Repeated low scores:
- trigger system revision

Mixed scores:
- require additional observation

---

## 12. FAILURE MODES

### No Scoring
System cannot compare outcomes

### Inflated Scoring
All results treated as high quality

### Inconsistent Scoring
Different standards applied across cases

### Ignoring Scores
Scores recorded but not used

---

## 13. SIMPLICITY RULE

The scoring system must remain:

- fast to apply
- consistent
- minimal

Do not:
- overcomplicate scoring formulas
- introduce unnecessary metrics
- slow down execution

---

## 14. FINAL DEFINITION

The Evaluation / Scoring Engine ensures:

- decisions are measurable
- outcomes are comparable
- patterns are validated
- system improvement is data-driven

---

## SYSTEM SUMMARY

Measure outcomes  
Assign scores  
Compare results  
Promote strong signals  
Refine weak signals  
Improve system performance