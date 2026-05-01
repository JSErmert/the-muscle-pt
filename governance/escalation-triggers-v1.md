# THE MUSCLE PT — ESCALATION TRIGGERS v1

## Purpose

This file defines when a recurring issue should be promoted into a higher level of system action.

Escalation prevents the repository from staying static.
It is the mechanism that turns repeated friction into structure.

---

## Core Principle

Do not escalate on first contact.

Escalate when:
- the same issue repeats
- the same uncertainty returns
- the same friction keeps wasting time
- the same pattern appears across multiple contexts

The goal is not more structure.

The goal is better-timed structure.

---

## 1. RULE ESCALATION TRIGGERS

### ET-01 — Repeated Decision Trigger
If the same strategic decision is debated more than once, promote it into a logged rule or preference.

Examples:
- posting frequency
- whether to clear old backlog
- whether to restart an account
- whether to add a new tool

Action:
Move the issue into either:
- `decision-preferences-v1.md`
- `hard-locks-v1.md`

---

### ET-02 — Repeated Waste Trigger
If the same mistake repeatedly consumes time, attention, or momentum, escalate it into a hard lock or workflow constraint.

Examples:
- posting low-value content
- switching tools repeatedly
- losing track of prior choices

Action:
Convert waste into a rule.

---

## 2. SYSTEM ESCALATION TRIGGERS

### ET-03 — Repeated Friction Trigger
If the same operational friction appears across multiple weeks, promote it into a system improvement.

Examples:
- content planning repeatedly breaks down
- cases are recorded inconsistently
- the same session logic must be rebuilt repeatedly

Action:
Update:
- a system artifact
- a workflow section
- a record template

---

### ET-04 — Repeated Pattern Trigger
If the same client issue, audience question, or content insight appears repeatedly, promote it into a reusable system asset.

Examples:
- repeated client case type
- repeated root cause pattern
- repeated audience pain point
- repeated content hook

Action:
Create or update:
- a case type
- a content pillar topic
- a reusable template
- a tracked pattern entry

---

## 3. STRUCTURE ESCALATION TRIGGERS

### ET-05 — Retrieval Failure Trigger
If important information becomes difficult to find more than once, add just enough structure to fix retrieval.

Examples:
- too many mixed content notes in one file
- case records hard to locate
- repeated prompts getting lost

Action:
Add:
- one new file
- one new index
- one new subfolder
Only as much as needed.

---

### ET-06 — Volume Threshold Trigger
If a category accumulates enough real artifacts that one file is no longer practical, split it.

Examples:
- too many active cases
- too many content logs
- too many refinement notes

Action:
Subdivide by:
- status
- time period
- artifact type

Do not subdivide preemptively.

---

## 4. REVIEW ESCALATION TRIGGERS

### ET-07 — Strategy Drift Trigger
If output begins to move away from the mission, identity, or clinical positioning, escalate to review before producing more.

Examples:
- content feels generic
- content no longer reflects the core mission
- decisions begin optimizing for novelty instead of alignment

Action:
Review:
- mission
- positioning
- content system preferences

---

### ET-08 — System Conflict Trigger
If two system artifacts begin guiding behavior in conflicting ways, escalate to architecture review.

Examples:
- content rule conflicts with workflow
- case engine logic conflicts with intervention guidance
- multiple docs define the same thing differently

Action:
Resolve the conflict at the architecture level, not by letting both coexist silently.

---

## 5. ESCALATION LEVELS

### Level 1 — Log
Use when:
- issue appeared once
- not enough evidence yet

Destination:
- `logs/refinement-log.md`

---

### Level 2 — Preference
Use when:
- pattern is emerging
- flexibility still matters

Destination:
- `decision-preferences-v1.md`

---

### Level 3 — Hard Lock
Use when:
- repeated cost is clear
- flexibility is now harmful

Destination:
- `hard-locks-v1.md`

---

### Level 4 — System Revision
Use when:
- issue cannot be solved by a rule alone
- the system itself needs improvement

Destination:
- relevant file in `/systems/` or `/architecture/`

---

## Escalation Questions

Before escalating, ask:

1. Has this happened more than once?
2. Is this causing meaningful repeated cost?
3. Is the problem local, or does it affect multiple parts of the system?
4. Would a rule solve it, or is a system revision needed?
5. What is the smallest useful escalation?

Escalate only to the minimum level required.

---

## Final Definition

Escalation triggers are the self-improvement logic of the repository.

They ensure that:
- repeated waste becomes rules
- repeated friction becomes structure
- repeated patterns become assets
- repeated conflict becomes architecture review

This is how the system improves without becoming overbuilt.
