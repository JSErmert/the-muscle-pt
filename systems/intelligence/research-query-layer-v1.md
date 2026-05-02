# THE MUSCLE PT — RESEARCH QUERY LAYER v1

## Purpose

Define how the system converts real-world inputs into precise research questions.

This layer ensures:

- research is driven by actual use cases  
- research topics are consistently defined  
- extraction is structured and repeatable  
- the research layer becomes usable, not theoretical  

---

## Core Principle

No research without a question.

No question without a use case.

---

## Objective

Convert:

user input → structured research question → research record

This is the bridge from:

M1 execution → M2 grounding  

---

## System Definition

The Research Query Layer is:

A system that translates real inputs into:

- clear research topics  
- precise research questions  
- structured extraction targets  

---

## Input Sources

All research queries must originate from:

- Golden Run inputs  
- real user prompts  
- repeated failure points  
- recurring system patterns  

No abstract research allowed.

---

## Query Structure

Each research query must include:

---

### 1. Use Case

Define the real scenario.

Example:

- intercostal strain recovery  
- variable pain with unclear cause  
- persistent posterior chain tightness  

---

### 2. Core Question

Define what must be answered.

Examples:

- What is the role of intercostal muscles in breathing and trunk stability?  
- How does restricted breathing affect rib motion and trunk stiffness?  
- When should movement be restored vs avoided in rib injury?  

---

### 3. Mechanism Focus

Define the biological or mechanical process.

Examples:

- rib cage expansion  
- respiratory loading  
- trunk stiffness  
- compensation patterns  

---

### 4. Decision Target

Define what the research must inform.

Examples:

- when to rest vs move  
- when to reintroduce load  
- how to sequence recovery  

---

### 5. Constraints

Define boundaries for interpretation.

Examples:

- do not claim universal causation  
- must distinguish correlation vs causation  
- must remain within study scope  

---

## Query Output Format

Each query must be recorded as:

```text
Use Case:
[real scenario]

Core Question:
[what must be answered]

Mechanism Focus:
[system involved]

Decision Target:
[what decision this informs]

Constraints:
[limits on interpretation]
```

---

## Query Examples

---

### Example 1 — Intercostal Strain

Use Case:
Strained intercostal muscle not improving with rest  

Core Question:
Why does breathing continue to load intercostal injuries?  

Mechanism Focus:
Rib expansion and respiratory mechanics  

Decision Target:
When to reintroduce breathing, movement, and load  

Constraints:
Do not claim all rib pain behaves identically  

---

### Example 2 — Variable Pain

Use Case:
Pain that changes daily with no clear cause  

Core Question:
When should movement be maintained instead of changed?  

Mechanism Focus:
Pain variability and signal stability  

Decision Target:
When to hold vs intervene  

Constraints:
Avoid overgeneralizing pain models  

---

## Integration Points

This layer feeds directly into:

- research record creation  
- system mapping layer  
- decision system refinement  
- content generation  

---

## Failure Conditions

The layer fails if:

- queries are vague  
- queries are not tied to real use cases  
- questions cannot guide research  
- mechanism is undefined  
- decision target is unclear  

---

## Success Condition

The layer succeeds when:

- every research entry begins with a clear query  
- research is directly usable  
- decisions are informed by specific questions  
- no abstract or unused research exists  

---

## Scaling Rule

Add queries only when:

- a new use case appears  
- a failure pattern repeats  
- a decision lacks grounding  

Avoid bulk query creation.

---

## Final Definition

The Research Query Layer converts:

```text
real problems → precise questions → structured research
```

---

## System Summary

Start with reality  
Define the question  
Focus the mechanism  
Target the decision  
Apply constraints  

This is the gateway from:

execution → grounded intelligence
