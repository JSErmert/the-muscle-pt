---
refinement_id: refinement-003-engine-name-leakage-section-5-rule
date: 2026-05-01
type: refinement
status: closed (rule added; awaiting re-test verification)
relevant_doctrine:
  - CLAUDE.md (Section 5)
  - CLAUDE.md (Section 7)
  - execution/execution-playbook-v1.md (v2)
escalation_path: ET-03 (Repeated Friction Trigger) — pattern repeated across 5 of 7 cold-test outputs
linked_incident: incident-001-cold-test-translation-failures
---

# Observation

The cold test surfaced a translation failure pattern: the model opens user-facing output by naming the engine, doctrine layer, or system component being applied (e.g., *"Use Movement Case Engine"*, *"Use Content Case Flywheel"*, *"Use Governing Logic + Decision Preferences + Hard Locks"*).

Section 7 ("Remove system terminology") and Playbook v2 Founder-Facing Output Rule #1 ("No system language") did not fire on these openings. The model interpreted them as helpful scaffolding — *here's what's about to be applied* — rather than as terminology that should be invisible to the user.

---

# Trigger

5 of 7 cold-test outputs (Tests 1, 2, 3, 5, 7) opened with engine-name announcements. Same pattern, multiple manifestations in a single test run. Per ET-03 (Repeated Friction Trigger), this escalates from incident to refinement — a pattern that warrants a rule sharpening, not just a single-incident correction.

---

# Rule Added

Inserted as a new bullet in CLAUDE.md Section 5 (Constraints):

> *"open user-facing output by naming the system component, engine, or doctrine layer being applied — engines fire silently; the user receives only the action"*

This sits alongside the existing constraints against tool migration, capture modification, second tools, side-tasks, and observation-tracking. It targets the specific failure mode the cold test surfaced.

---

# Why a Section 5 Hard Constraint, Not a Section 7 Soft Checklist

Section 7's "Remove system terminology" is part of a *"before returning any response"* checklist. Soft checklist items rely on the model self-policing during output. The cold test demonstrates this self-policing fails when the model interprets the terminology as helpful prefix rather than as jargon.

Section 5 constraints are hard rules expressed as *"Claude must not"* — same construction as the rules that successfully blocked tool migration, capture modification, and analysis homework in earlier tests. Promoting the rule to Section 5 puts it in the same enforcement layer as those.

---

# Action Status

Rule added. Phase 2 remains paused until the same 7 cold-test prompts pass at 7/7 in a fresh chat with the updated CLAUDE.md.

---

# Generalization for Future M2 Design

The deeper pattern: the model's instinct is to *show its work* by naming the doctrine layer being applied. This instinct is appropriate for an internal audit trail (M3 self-auditing layer) but is wrong for a user-facing surface (M1 interaction layer).

When M3 is authored, this insight should inform the audit-vs-interaction split: engine attribution is welcome in audit output, forbidden in user output. The same answer may need two presentations depending on which layer is being addressed.
