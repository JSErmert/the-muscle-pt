---
decision_id: decision-009-phase1-records-tree-and-archive-relocation
date: 2026-05-01
type: decision
status: closed
relevant_doctrine:
  - architecture/architecture-tree-v1.md
  - CLAUDE.md (Section 3)
phase: M1 Operationalize Plan v1 — Phase 1 (records tree standup)
supersedes: decision-003-fix-raw-archive-path
---

# Decision

Stand up the full `records/` tree per `architecture-tree-v1.md`. Relocate the founder conversation archive from `records/raw/` to `records/system-history/raw/`. Update CLAUDE.md Section 3 to point at the spec-correct path.

This supersedes **decision-003**.

---

# Context

`architecture-tree-v1.md` defines the records layer as:

```
records/
  cases/{active,successful,failed,inconclusive,validated,patterns,closed}/
  content/{ideas,planned,published,performance}/
  research/{captured,mapped,archived}/
  system-history/{raw,extracted,patterns}/
  logs/{decisions,refinements,incidents}/
  logs/reviews/{weekly,monthly}/
```

The repo previously had only a partial tree, and the founder archive sat at `records/raw/founder-claude-conversation-archive.md` — outside the spec. Decision-003 had updated CLAUDE.md to point at this incorrect path, treating CLAUDE.md as the thing to fix rather than the file location.

That was the wrong fix.

---

# Reasoning

`architecture-tree-v1.md` is the authoritative source for records layout. When CLAUDE.md and the filesystem disagree, the architecture spec is the arbiter — not whichever surface happens to be easier to edit.

The Phase 1 standup is the right time to correct this:

- All terminal folders required by the spec now exist
- The founder archive moves to its spec-correct location: `records/system-history/raw/`
- CLAUDE.md Section 3 reverts to the spec-correct path: `records/system-history/raw/`
- Each terminal folder receives a one-paragraph README sourced from `architecture-tree-v1.md`

---

# Resolution

Actions taken:

1. Created missing directory structure under `records/` per architecture-tree-v1.md
2. `git mv records/raw/founder-claude-conversation-archive.md records/system-history/raw/`
3. Removed the now-empty `records/raw/`
4. Reverted CLAUDE.md Section 3: `records/raw/` → `records/system-history/raw/`
5. Wrote 19 README.md files (one per terminal folder lacking one), each ≤1 paragraph copied from `architecture-tree-v1.md`

---

# Consequence

`records/` tree is now spec-compliant. Phase 1 of the M1 Operationalize Plan closes.

**On decision-003:** the prior decision is superseded but not deleted. It remains in the log as a record of the misjudgment so future readers see the trail. Decision-003's status field is unchanged (still "closed"); this decision's `supersedes` field carries the linkage.

The lesson logged for future reference: when CLAUDE.md and the filesystem disagree, check `architecture-tree-v1.md` before deciding which surface to "fix."

Phase 2 (operational capture) is next.
