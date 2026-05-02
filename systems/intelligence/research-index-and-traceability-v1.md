# THE MUSCLE PT — RESEARCH INDEX & TRACEABILITY SYSTEM v1

## Purpose

Create a single source of truth that connects:

- research records  
- system decisions  
- content outputs  

This system ensures:

- every decision can be traced back to research  
- every research record is actually used  
- the research layer becomes queryable, not just stored  

---

## Core Principle

If research cannot be found, it cannot be used.

If research is not used, it should not exist.

---

## Objective

Transform the research layer from:

stored records  

into:

connected, queryable system intelligence  

---

## Problem This Solves

Currently:

- research exists as isolated records  
- no lookup mechanism exists  
- no backward traceability exists  
- no connection between decisions and sources  

This prevents:

- validation  
- scaling  
- system trust  

---

## System Definition

The Research Index is:

A structured map that links:

```text
decision → research → source
```

and allows retrieval in both directions.

---

## File Location

```
records/research/index.md
```

---

## Index Structure

Each entry must follow this format:

---

### ENTRY FORMAT

#### Research ID

[unique identifier]

---

#### Topic

[clear topic name]

---

#### Use Cases

- [Test 3 — Intercostal strain recovery]  
- [Test 5 — Variable pain / observation]  

---

#### System Mappings

##### Case Engine Mapping
[how it affects intervention selection]

##### Decision Mapping
[how it influences decision logic]

##### Rule Candidates
- [rule derived from research]

##### Constraint Candidates
- [limitations or conditions]

---

#### Content Mappings

- [carousel topic connections]  
- [reel topics]  
- [education buckets]  

---

#### Source References

- PMID: [number if available]  
- Link: [URL]  
- Title: [study title]  

---

#### Confidence Level

- Low / Medium / High  

---

#### Last Updated

[date]

---

## Query Patterns

The system must support:

---

### Forward Query

```text
problem → research
```

Example:

- intercostal strain → find all related research entries  

---

### Reverse Query

```text
research → system behavior
```

Example:

- study on breathing mechanics → what rules does this affect  

---

### Output Query

```text
output → research
```

Example:

- carousel slide → which research supports this  

---

## Integration Points

This index connects to:

- records/research/mapped/  
- case-state-model  
- decision-preferences  
- content-case-flywheel  

---

## First Required Entries

To activate the system, create:

1. Intercostal strain recovery  
2. Breathing mechanics and rib mobility  
3. Compensation patterns in posterior chain  

---

## Validation Rules

Each entry must:

- reference at least one real source  
- map to at least one system behavior  
- be usable in content generation  
- be traceable to original research  

---

## Failure Conditions

The index fails if:

- entries are missing links to research  
- mappings are vague  
- no connection to system outputs exists  
- topics cannot be queried  

---

## Success Condition

The index is successful when:

- you can answer "why does this work?" instantly  
- you can find research for any output  
- every major decision has traceable grounding  

---

## Scaling Rule

Add entries only when:

- a new use case appears  
- a new decision pattern emerges  
- a new research record is validated  

Avoid bulk creation without usage.

---

## Final Definition

The Research Index converts:

```text
stored knowledge → usable system intelligence
```

by making research:

- connected  
- traceable  
- actionable  

---

## System Summary

Store research  
Map it to behavior  
Index it for retrieval  
Use it consistently  

This is the bridge from:

M2 structure → M2 reality
