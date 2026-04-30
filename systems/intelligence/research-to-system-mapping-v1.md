# THE MUSCLE PT — RESEARCH TO SYSTEM MAPPING v1 (FIXED)

## Purpose

This document defines how research is:
- sourced from published literature
- extracted into structured text
- interpreted into actionable insight
- mapped into system behavior

The goal is to transform research from static reference into:
- decision logic
- client system input
- content generation
- auditable, traceable artifacts

---

## Core Principle

Research is not stored to be cited  
Research is stored to be used  

Every research artifact must support:
- decision-making
- system behavior
- traceability
- reproducibility

---

## 1. RESEARCH LAYER STRUCTURE

Each research entry must pass through 3 layers:

### Layer 1 — Source Capture
What the study says

### Layer 2 — Insight Extraction
What the study means

### Layer 3 — System Mapping
What the system does with it

---

## 2. RESEARCH RECORD FORMAT

Each research entry must follow this structure:

### Metadata

- research_id
- title
- authors
- year
- journal
- PMID
- source_link
- date_extracted
- extracted_by

---

### Layer 1 — Source Extraction

Direct extraction from source.

Rules:
- must be derived directly from the published study
- no paraphrasing of numerical data
- no invented claims
- preserve exact meaning of results

Structure:

- study_design
- population
- intervention
- comparison
- outcomes
- key_results (exact values when applicable)

---

### Layer 2 — Insight Interpretation

Convert extracted findings into usable understanding.

Rules:
- must remain faithful to the source
- no exaggeration
- no speculative claims
- may simplify language but not distort meaning

Structure:

- core_takeaway
- practical_meaning
- limitations
- confidence_level

---

### Layer 3 — System Mapping

Translate insight into system behavior.

Rules:
- must map to at least one system domain
- must be actionable
- must be reusable

Structure:

- content_mapping
- case_engine_mapping
- decision_mapping
- rule_candidate
- constraint_candidate

---

## 3. SYSTEM MAPPING DEFINITIONS

### 3.1 Content Mapping

Defines how research becomes content.

Example fields:
- topic
- hook angle
- myth to challenge
- simplified explanation
- audience relevance

---

### 3.2 Case Engine Mapping

Defines how research informs client decisions.

Example fields:
- case type relevance
- root cause implications
- intervention guidance
- progression constraints

---

### 3.3 Decision Mapping

Defines how research affects system decisions.

Example fields:
- preference update
- workflow adjustment
- strategy alignment

---

### 3.4 Rule Candidate

If repeated across multiple sources:
- candidate for decision preference
- candidate for hard lock

---

### 3.5 Constraint Candidate

Defines boundaries:
- what not to do
- when not to escalate
- when to limit progression

---

## 4. TRACEABILITY REQUIREMENTS

Every research record must be:

- linked to a valid source
- reproducible from original study
- timestamped
- attributable

Required fields:

- PMID (if applicable)
- source_link
- date_extracted
- extracted_by

---

## 5. EXTRACTION PROCESS

Step 1 — Identify Source  
- locate published study  
- verify legitimacy  

Step 2 — Extract Data  
- capture study structure  
- record exact results  
- avoid interpretation at this stage  

Step 3 — Interpret Insight  
- convert findings into practical meaning  
- identify real-world relevance  

Step 4 — Map to System  
- define how this affects:
  - content
  - client decisions
  - system rules  

Step 5 — Store Record  
- save in research layer  
- maintain consistent format  

---

## 6. STORAGE STRUCTURE

All research records should be stored in:

/research/records/

File naming convention:

research-entry-[research_id].md

---

## 7. OVERSIGHT AND AUDIT

Each research record must support:

- verification of source accuracy
- review of interpretation
- traceability of system decisions back to research

Audit questions:

- Can the claim be traced to the study?
- Is the interpretation faithful?
- Does the mapping align with the system?
- Is the usage appropriate?

---

## 8. INTEGRATION WITH SYSTEM

### Content System

Research informs:
- educational content
- myth busting
- authority building

---

### Movement Case Engine

Research informs:
- intervention selection
- progression logic
- case handling

---

### Decision System

Research informs:
- preferences
- rules
- constraints

---

## 9. USAGE RULES

- do not cite without source
- do not interpret without extraction
- do not map without understanding
- do not create rules from a single study

---

## 10. FAILURE MODES

### Misinterpretation
- exaggerating findings
- removing context

### Overgeneralization
- applying narrow studies broadly

### Premature Rule Creation
- turning single findings into system rules

### Citation Without Use
- storing research but not mapping it to system behavior

---

## 11. FINAL DEFINITION

This layer transforms research into:

- usable knowledge
- system input
- traceable decisions
- scalable insight

---

## SYSTEM SUMMARY

Source → Extract → Interpret → Map → Apply → Audit