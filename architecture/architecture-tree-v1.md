# THE MUSCLE PT — ARCHITECTURE TREE v1 (FINAL)

the-muscle-pt/
└── records/
    ├── cases/
    │   ├── active/
    │   ├── successful/
    │   ├── failed/
    │   ├── inconclusive/
    │   ├── validated/
    │   ├── patterns/
    │   └── closed/
    │
    ├── content/
    │   ├── ideas/
    │   ├── planned/
    │   ├── published/
    │   └── performance/
    │
    ├── research/
    │   ├── captured/
    │   ├── mapped/
    │   └── archived/
    │
    ├── system-history/
    │   ├── raw/
    │   ├── extracted/
    │   └── patterns/
    │
    └── logs/
        ├── decisions/
        ├── refinements/
        ├── reviews/
        │   ├── weekly/
        │   └── monthly/
        └── incidents/

## Purpose

This document defines the structure of the records layer in The Muscle PT system.

The goal is to:
- store real-world outputs clearly
- preserve system memory
- support retrieval and reuse
- enable learning and refinement over time

This is where the system becomes operational.

---

## Core Principle

Structure should reflect how the system thinks.

Each folder exists to:
- store a specific type of output
- answer a specific type of question
- support system evolution

---

## ROOT STRUCTURE

the-muscle-pt/  
└── records/  
  ├── cases/  
  ├── content/  
  ├── research/  
  ├── system-history/  
  └── logs/  

---

## 1. CASES

### Purpose

The cases folder stores all client-related work.

This is where:
- client interactions are recorded
- interventions are tracked
- outcomes are classified
- patterns emerge over time

Each subfolder represents a case state.

---

### cases/active/

Stores:
- cases currently being worked
- ongoing client sessions

Meaning:
- intervention is in progress
- no final outcome yet

---

### cases/successful/

Stores:
- cases that produced a good outcome
- improvement observed

Meaning:
- intervention worked
- not yet confirmed as repeatable

---

### cases/failed/

Stores:
- cases where intervention did not work
- negative or no change observed

Meaning:
- system logic needs review
- high-value learning signal

---

### cases/inconclusive/

Stores:
- cases with unclear or mixed results

Meaning:
- insufficient data
- requires further observation

---

### cases/validated/

Stores:
- cases with repeated reliable success

Meaning:
- intervention is trustworthy for similar cases
- stronger than single success

---

### cases/patterns/

Stores:
- confirmed repeatable patterns across multiple validated cases

Meaning:
- system-level reusable logic
- candidate for rules or standard interventions

---

### cases/closed/

Stores:
- completed or archived cases

Meaning:
- no longer active
- preserved for historical reference and analysis

---

## 2. CONTENT

### Purpose

The content folder stores all content-related outputs.

This includes:
- ideas
- planned content
- published content
- performance tracking

---

### content/ideas/

Stores:
- raw content ideas
- insights from cases
- notes for future posts

Meaning:
- unprocessed signal
- early-stage input

---

### content/planned/

Stores:
- scheduled or organized content
- upcoming posts

Meaning:
- ideas that are ready to be executed

---

### content/published/

Stores:
- completed and posted content

Meaning:
- final outputs
- reference for reuse or review

---

### content/performance/

Stores:
- metrics
- engagement summaries
- observations about content success

Meaning:
- feedback signal
- input for refinement

---

## 3. RESEARCH

### Purpose

The research folder stores all knowledge inputs.

This includes:
- raw research
- interpreted insights
- archived references

---

### research/captured/

Stores:
- raw extracted data from sources
- direct study information

Meaning:
- unprocessed research
- source-level information

---

### research/mapped/

Stores:
- research that has been:
  - interpreted
  - mapped to system behavior
  - connected to cases or content

Meaning:
- usable knowledge
- system-integrated research

---

### research/archived/

Stores:
- outdated
- unused
- or low-priority research

Meaning:
- retained for reference
- not actively used

---

## 4. SYSTEM HISTORY

### Purpose

The system-history folder captures the founder’s thinking over time.

This includes:
- verbal input
- conversational reasoning
- evolving ideas
- early-stage system logic

This is where:
- raw thinking is preserved
- structured intelligence is extracted
- patterns in thinking are identified

---

### system-history/raw/

Stores:
- original transcripts
- exported chat conversations
- unmodified verbal or written input

Meaning:
- source-level thinking
- no processing applied

---

### system-history/extracted/

Stores:
- cleaned and structured entries
- classified insights
- interpreted meaning from raw input

Meaning:
- usable system intelligence
- converted from raw thinking

---

### system-history/patterns/

Stores:
- repeated ideas
- recurring decision tendencies
- consistent friction points

Meaning:
- behavioral patterns of the founder
- inputs for system refinement

---

## 5. LOGS

### Purpose

The logs folder stores system memory of change.

This includes:
- decisions
- improvements
- reflections
- failures

Logs ensure:
- nothing important is forgotten
- the system learns over time
- changes are traceable

---

### logs/decisions/

Stores:
- important decisions
- reasoning behind decisions

Examples:
- workflow changes
- strategy shifts
- tool choices

Meaning:
- prevents re-deciding
- preserves intent

---

### logs/refinements/

Stores:
- system improvements
- rule updates
- workflow adjustments

Meaning:
- captures how the system evolves
- connects experience to change

---

### logs/reviews/

Stores:
- periodic reflections

---

#### logs/reviews/weekly/

Stores:
- weekly summaries
- short-term observations
- immediate patterns

Meaning:
- short-term awareness

---

#### logs/reviews/monthly/

Stores:
- broader reflections
- long-term patterns
- strategic adjustments

Meaning:
- long-term insight

---

### logs/incidents/

Stores:
- failures
- breakdowns
- unexpected problems

Examples:
- failed interventions
- system conflicts
- major mistakes

Meaning:
- high-value signals
- triggers for system correction

---

## FINAL DEFINITION

The records layer is the system’s memory.

It stores:
- what happened
- what worked
- what failed
- what changed
- how thinking evolved

It allows the system to:
- learn
- improve
- scale knowledge

---

## SYSTEM SUMMARY

Cases store client reality  
Content stores output  
Research stores knowledge  
System history stores thinking  
Logs store learning  

Together, they form the memory of the system