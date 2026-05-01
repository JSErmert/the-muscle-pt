---
decision_id: decision-004-dedupe-output-translation-rules
date: 2026-05-01
type: decision
status: closed
relevant_doctrine:
  - governance/output-translation-rules-v1.md
  - CLAUDE.md (Section 5)
commit: f26cac0
---

# Decision

Remove the line *"Never introduce new tools, files, or systems unless the user explicitly asks for them"* from `governance/output-translation-rules-v1.md` (Rule 2 — Improve, Don't Replace).

---

# Context

The line existed in `output-translation-rules-v1.md` as a soft "before returning any response" guideline. CLAUDE.md Section 5 (Constraints) had grown a stronger, more specific set of hard constraints during M1 refinement:

- *"propose tool migration when the user already has a working capture or storage method"*
- *"introduce a second tool when the user's existing tool can hold the new behavior (separate list, label, or section)"*
- *"modify the user's capture step — preserve capture unchanged"*
- *"bolt analysis, classification, or logging tasks onto a recommendation"*

The single line in `output-translation-rules-v1` had become redundant with — and weaker than — the hard-constraint version in CLAUDE.md.

---

# Reasoning

Two doctrine surfaces saying the same thing in different strengths is a drift risk: the model may interpret the soft line as the operative rule and ignore the harder Section 5 constraints. Dedupe consolidates authority in one place.

CLAUDE.md is the operating layer per the System Evolution Doctrine M1 spec. Constraints belong there, not in supporting governance docs that say the same thing more loosely.

---

# Resolution

Delete the redundant line from `output-translation-rules-v1.md` Rule 2. Leave the rest of Rule 2 intact ("Keep what the user is already doing. Make it easier, not different.").

CLAUDE.md Section 5 is now the single source of truth for tool-introduction prohibitions.

---

# Consequence

No behavioral change expected; the rule is still enforced — through CLAUDE.md instead of two surfaces. Future changes to tool-introduction discipline should be made in CLAUDE.md Section 5 only.
