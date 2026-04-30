# THE MUSCLE PT — PRIORITIZATION + QUEUE ENGINE v1

## Purpose

This document defines how the system determines:
- what to work on next
- what deserves attention
- what should be delayed
- what should be escalated

The goal is to convert the system from:
- reactive execution
to:
- directed, high-leverage action

---

## Core Principle

Attention is the most limited resource.

The system must decide:
- what matters most
- what can wait
- what must be addressed immediately

---

## 1. OBJECTIVE

The Prioritization + Queue Engine exists to:

- reduce decision fatigue
- allocate attention effectively
- surface the highest-value next action
- ensure important work is not ignored
- ensure low-value work does not dominate

---

## 2. PRIORITY DOMAINS

The system evaluates four primary domains:

### 2.1 Cases
Client-related work

### 2.2 Content
Content production and ideas

### 2.3 Failures
Breakdowns and system errors

### 2.4 Research
Knowledge inputs

---

## 3. CASE PRIORITY ORDER

Cases must be prioritized based on state:

1. Escalated  
2. Failed  
3. Inconclusive  
4. Improving  
5. Active  
6. Validated  
7. Pattern  

---

### Case Priority Logic

Escalated:
- highest urgency
- requires immediate attention

Failed:
- high learning value
- must be analyzed quickly

Inconclusive:
- blocks progression
- requires data collection

Improving:
- maintain direction
- lower urgency

Active:
- normal workflow

Validated:
- stable, minimal attention

Pattern:
- reference only, no immediate action

---

## 4. CONTENT PRIORITY ORDER

Content must be prioritized by signal strength:

1. Repeated real-world insight  
2. Strong single-case insight  
3. Audience demand  
4. Planned content  
5. New idea without validation  

---

### Content Priority Logic

Repeated insight:
- highest leverage
- strong pattern signal

Single-case insight:
- valuable but not yet validated

Audience demand:
- externally driven

Planned content:
- scheduled but replaceable

New ideas:
- lowest priority unless validated

---

## 5. FAILURE PRIORITY ORDER

Failures must be prioritized by impact:

1. Repeated failure  
2. High-cost failure  
3. System-breaking failure  
4. Isolated failure  
5. Low-impact failure  

---

### Failure Priority Logic

Repeated failure:
- indicates system flaw

High-cost failure:
- impacts outcomes significantly

System-breaking failure:
- affects multiple areas

Isolated failure:
- requires analysis but lower urgency

Low-impact failure:
- track but do not prioritize

---

## 6. RESEARCH PRIORITY ORDER

Research must be prioritized by relevance:

1. Directly applicable to active cases  
2. Fills known knowledge gaps  
3. Supports current content  
4. General interest  
5. Future use  

---

### Research Priority Logic

Direct application:
- immediate system value

Knowledge gap:
- resolves uncertainty

Content support:
- improves output quality

General interest:
- low urgency

Future use:
- defer until needed

---

## 7. QUEUE STRUCTURE

The system maintains a dynamic queue:

Top priority items are surfaced first.

Queue categories:

- next_case_action
- next_content_creation
- next_failure_analysis
- next_research_mapping

---

## 8. NEXT ACTION RULE

At any moment, the system must be able to answer:

What is the single most valuable next action?

---

### Selection Rule

Choose the highest item across all domains based on:

- urgency
- impact
- repetition
- system value

---

## 9. ATTENTION ALLOCATION

Time should be distributed based on priority:

High priority:
- immediate focus

Medium priority:
- scheduled

Low priority:
- deferred

---

## 10. ESCALATION INTEGRATION

When an item repeatedly appears at high priority:

- escalate to rule
- escalate to system change
- escalate to architecture update

---

## 11. QUEUE UPDATE RULE

The queue must be updated:

- after each session
- after each content cycle
- after each failure
- after each research mapping

---

## 12. ANTI-FRAGMENTATION RULE

The queue must remain:

- simple
- visible
- actionable

Do not create multiple disconnected queues.

---

## 13. FAILURE MODES

### No Prioritization
Everything treated equally

### Over-Prioritization
Too many high-priority items

### Static Queue
Queue not updated

### Emotional Prioritization
Decisions based on preference instead of system logic

---

## 14. FINAL DEFINITION

The Prioritization + Queue Engine ensures:

- the system always knows what to do next
- attention is directed toward high-value work
- learning is not ignored
- execution remains efficient

---

## SYSTEM SUMMARY

Identify priorities  
Order tasks  
Select highest-value action  
Execute  
Update queue  
Repeat