---
refinement_id: refinement-001-m2-research-applies-to-all-lanes
date: 2026-05-01
type: refinement
status: deferred to M2
relevant_doctrine:
  - systems/intelligence/research-to-system-mapping-v1.md
  - architecture/system-evolution-doctrine-v1.md
  - CLAUDE.md (Section 2)
---

# Observation

The M2 research-grounding layer applies to ALL decision lanes — not only the clinical / Movement Case Engine lane.

Pricing research, scaling research, hiring frameworks, and business strategy literature all flow through the same M2 pipeline as clinical research.

---

# Trigger

During M1 testing on 2026-05-01, Test 3 (RF Fitness pricing model question) returned: *"Inconclusive — not enough signal in the system to set the number."*

The M1 system correctly fell to inconclusive on a Business Decisions question for the same reason it fell to inconclusive on Clinical questions — no mapped research backs the decision.

This confirms that research grounding is not narrowly *clinical-grounding*. It is *evidence-grounding for any decision lane the system can answer*.

---

# Implication for M2 Design

- `records/research/` captures research across all lanes (clinical, business, content)
- M2 trigger: any decision asked → check if mapped research exists → cite, or fail to inconclusive — regardless of lane
- The M1 inconclusive fail-state is the correct precursor to M2 citation. Same pattern, both lanes.

The `research-to-system-mapping-v1` spec already supports this domain-agnostic interpretation: §3.3 (Decision Mapping) is generic and not restricted to clinical literature.

M2 design should not artificially restrict research types to medical/clinical sources.

---

# Action Status

Deferred to M2. M1 lock holds — do not act on this now.

Reopen when System Evolution Doctrine v1 evolves into M2 doctrine and the M2 plan is authored.
