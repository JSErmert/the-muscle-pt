---
doc_id: clustering-rate-analysis-method-v1
version: v1
date: 2026-05-04
type: analytical methodology (production-rate measurement across doctrine evolution arc)
purpose: Define a defensible, repeatable methodology for estimating production rates and time-saved leverage across The Muscle PT system's doctrine evolution arc — from the archived founder-Claude conversation (M1 build period) through Pre-Alpha 1–8, into Alpha-1 and beyond Beta. Enables relative time-saving pattern analysis from data that already exists, not just future Alpha-1 close. Companion to `architecture/alpha-production-validation-metrics-v1.md` — that doc defines what's measured during Zach's window; this doc defines how rate-and-time-saved is extracted from transcripts (current and future).
relevant_doctrine:
  - architecture/alpha-production-validation-metrics-v1.md (the three-metric framework — Velocity feeds from this analysis)
  - architecture/alpha-state-record-v1.md (Alpha lock state — defines what doctrine state each transcript ran under)
  - CLAUDE.md §3 (raw archive location — gitignored on main; restore via tag for analysis)
linked_artifacts:
  - records/system-history/raw/founder-claude-conversation-archive.md (archive baseline; restore from git tag archive/system-history-2026-05-04)
  - records/research/validation/2026-05-04-pre-alpha-1 through 8 (Pre-Alpha doctrine-fidelity transcripts)
  - records/observations/alpha-week-1-metrics-log.md (Alpha-1 window data destination)
hl_09_evaluation: PASS — methodology only; introduces no grounded claims. Data is observed transcripts.
hl_10_evaluation: PASS — operator authorization 2026-05-04 ("yes please let's draft the methodology doc"). Justified by ProjectBrainer §6 future-potential ceiling (validation that the system actually scales output) + the Alpha→Beta gate's need for objective leverage measurement alongside Zach's self-report.
---

# Clustering Rate Analysis Methodology v1

## Purpose

Estimate Zach's production rate (artifacts per focused-chat-hour) across the entire doctrine evolution arc using DBSCAN-clustered transcript timestamps. Compute time-saved-per-day leverage estimates with bounded confidence intervals. Apply to:

- **Archive baseline** — Zach-only PT-work sections of `founder_chat_og` (M1 build period, vanilla or near-vanilla doctrine)
- **Pre-Alpha 1** — Zach + refinements 001–005 active (May 3–4 case-test arc)
- **Pre-Alpha 2 through 8** — doctrine-fidelity test arc (operator: Josh in Josh's account; useful for doctrine-effect comparison, NOT clean Zach baselining)
- **Alpha-1** — Zach + mature Alpha doctrine (refinements 008–013), 1-week production window
- **Beta-N** — post-Carousel, post-Zach-feedback (future)

The output is a **defensible estimate band** ("between X and Y hours saved per day on the work Zach actually did") with the confounds disclosed, not a single point estimate dressed up as proof.

## Position relative to the metrics framework

`architecture/alpha-production-validation-metrics-v1.md` defines the three primary metrics for Zach's 1-week window: Volume / Quality / Confidence. Volume is measured via daily artifact counts (Zach's self-reporting + cross-checked at end of window).

This methodology **adds a fourth signal** alongside the primary three: a transcript-anchored production-rate analysis that:

- Uses objective transcript data rather than self-report
- Extends across the doctrine evolution arc (not just Alpha-1)
- Produces bounded estimates of leverage gain ratios and time-saved-per-day
- Discloses confounds explicitly so the estimate isn't taken as proof

It is a **secondary signal, not a replacement** for the primary metrics. Volume / Quality / Confidence are still the Alpha → Beta gate. This analysis tells you something different: did the doctrine actually shift production rate over time, and by how much, with what confidence?

---

## The core question

The system's stated objective is leverage — scaling Zach's expertise, not replacing it. "Time saved per day" is one of three axes that have to validate (Volume), alongside Quality (output is Zach's, not generic-Claude) and Confidence (Zach trusts the output enough to actually use the time saved).

**Specifically what this methodology answers:**

For a defined unit of work (an artifact unit), how many of those units does Zach produce per focused-chat-hour, in each doctrine state? And given those rates, how much time per day does the current doctrine state save Zach relative to the baseline state, on the work he actually did?

**What this methodology cannot answer:**

- Counterfactual certainty (Zach can't run the same week twice with/without the system)
- Quality-at-constant-time (handled by Quality Pass Rate, separately)
- Trust earned (handled by Decision Confidence, separately)
- Doctrine attribution (which specific refinements drove the rate change)

These limits are not workarounds; they are the honest envelope of what a transcript-rate analysis can defensibly conclude.

---

## Methodology — four stages

### Stage 1: Artifact unit definition

Every transcript section is parsed against the same artifact unit list:

| Mode | Unit definition |
|---|---|
| Clinical | One programmed protocol (regardless of iterations), one full case classification, one reassessment plan, one intervention design |
| Insight | One content piece drafted to publish-ready (regardless of iterations) |
| Script | One Exercise-to-Script transformation (8-section structure complete) |
| Business | One decision documented (with rationale, not just a yes/no) |
| Research grounding | One verified research record authored (gates A/B/C complete) — counted separately as a research unit |

**Iteration rule (critical):** an artifact iterated 20 times = 1 unit, not 20. The cumulative deliverable is what counts. Refinements are part of producing the unit, not separate units. This rule preserves the §6 Iterative Refinement value (compounding artifact, not delta diffs).

**Sub-artifact rule:** if a single output produces multiple distinct deliverables (e.g., a programming arc that produces both a strength program AND a separate cardio plan), each distinct deliverable counts as its own unit if they could be shipped independently to a client.

**Discarded artifacts:** if Zach (or the operator-acting-as-Zach) explicitly discards an in-progress artifact and starts over, the discarded one is logged but does NOT count as a delivered unit. This prevents inflating production rate via abandoned work.

**Counting protocol:**
- For Alpha-1 and going forward: Zach categorizes outputs in real time per the metrics log (already specced)
- For historical transcripts (archive, Pre-Alpha 1–8): manual tagging pass — read transcript, identify discrete deliverable artifacts, tabulate
- Pattern-based extraction (auto-detect "deliverable headers" via markdown structure) is acceptable as a Beta+ scaling approach but **not** for v1 — too noisy for primary methodology

### Stage 2: Timestamp extraction + DBSCAN clustering

**Timestamp parsing:**
- Each transcript message is associated with its timestamp (from inline timestamps in the transcript, e.g., "3:11 PM" / "3:14 PM" / "3:39 PM"; or from Claude.ai export metadata if available)
- For the founder archive specifically: timestamps may need manual extraction in some sections; gracefully degrade if unavailable for a given section
- Output: ordered array `[t_1, t_2, ..., t_N]` of message timestamps for each section under analysis

**DBSCAN clustering:**

Why DBSCAN over gap-threshold:
- Within-block thinking pauses (a 12-min pause inside a deep-work block) shouldn't end the block; DBSCAN with `eps = 15-20 min` and `min_samples = 2` handles natural variance
- Outlier messages (single 3am message between two day-long gaps) get classified as noise rather than starting a spurious block
- No hand-tuning the threshold — `eps` is principled and consistent across transcripts

Parameters for v1:
- `eps = 15 minutes` (default; tune via gap-distribution histogram per transcript)
- `min_samples = 2` (a lone message isn't a "block")
- Distance metric: absolute time difference (1D)

Output per transcript section:
- List of work blocks: `[(block_start_t, block_end_t, message_count), ...]`
- Noise points (lone messages) tabulated separately

**Block duration:**
- Block duration = `block_end_t − block_start_t`
- Total focused-chat-time for section = sum of block durations
- Wall-clock time for section = `last_t − first_t` (for comparison only)
- **Density indicator** = total focused-chat-time / wall-clock-time. A low density (< 30%) means the section had long breaks between work — important context.

**Per-section secondary metrics** (fall out of the same clustering for free):
- Block count (how many distinct work sessions)
- Average block length (focus duration)
- Block density (focused-time / wall-time) — sanity check on whether the section was concentrated work or scattered

### Stage 3: Rate calculation

**Rate per section:**
- `rate_focused = artifact_units / total_focused_chat_hours`
- `rate_walltime = artifact_units / wall_clock_hours` (reported alongside for reference)

**Why both:**
- `rate_focused` is the load-bearing measurement for cross-transcript comparison (apples-to-apples on actual work time)
- `rate_walltime` reveals whether a session was concentrated or spread out (interpretation context)

**Aggregating across sections:**
- For each transcript (archive, Pre-Alpha-1, Alpha-1, etc.), sum artifact units across all sections; sum focused-chat-hours across all sections; compute weighted rate
- Report per-mode rates separately when artifact volume per mode is sufficient (≥3 units per mode); aggregate to "all modes" rate when per-mode samples are too small

**Confidence bounds:**
- Use bootstrap resampling (1000 iterations) on the artifact-counts to produce a 90% confidence interval for each rate
- For small samples (< 5 units), report raw count alongside rate and acknowledge wide bounds explicitly
- Don't pretend precision the data doesn't support

### Stage 4: Time-saved estimation

**Multiplier:**
- `multiplier = rate_target / rate_baseline` (e.g., `Alpha-1 rate / archive baseline rate`)
- Multiplier > 1 = doctrine state produces more units per focused hour than baseline
- Multiplier ≈ 1 = no rate change
- Multiplier < 1 = doctrine state slows production (red flag)

**Time saved per day estimate:**

Given Zach produced `N` artifacts during a measurement window of `D` days:

- Time at Alpha rate to produce N artifacts: `N / rate_alpha` hours
- Time at baseline rate to produce same N artifacts: `N / rate_baseline` hours
- **Time saved over the window**: `(N/rate_baseline) − (N/rate_alpha)` hours
- **Time saved per day**: `[(N/rate_baseline) − (N/rate_alpha)] / D` hours/day

The output is reported as a band, not a point: take the bootstrap 90% CIs from Stage 3 and propagate through to time-saved.

**Reportable form:**

> *"Over the Alpha-1 window, Zach produced X artifacts in Y focused-chat-hours, an estimated rate of Z artifacts/hour. Compared to the archive baseline rate of W artifacts/hour, this represents a time-saving estimate of [LOW] to [HIGH] hours per day (90% CI), on the work he actually did. Confounds disclosed: [list]."*

Single point estimates are not the reportable form. Bands are.

---

## Data sources

| Source | Access | What it represents | Comparison value |
|---|---|---|---|
| `records/system-history/raw/founder-claude-conversation-archive.md` (1.87MB, restored from git tag `archive/system-history-2026-05-04`) | Local restore: `git checkout archive/system-history-2026-05-04 -- records/system-history/raw/founder-claude-conversation-archive.md`. Per CLAUDE.md §3, do NOT re-commit. | Archive baseline; Zach-only PT-work sections = closest to "vanilla / minimal-doctrine" baseline | Primary baseline for time-saved estimates |
| `records/research/validation/2026-05-04-pre-alpha-1-zach-usage observation.md` | Tracked | Zach + refinements 001–005 (M1 doctrine, Pre-Alpha-1 case-test arc) | Intermediate doctrine state — useful for showing the doctrine arc's effect |
| `records/research/validation/2026-05-04-pre-alpha-2 through 8` | Tracked | Doctrine-fidelity tests in Josh's account simulating Zach. Same template-builder input variations. | **Operator-confounded.** Useful for doctrine-effect-on-Josh-as-tester comparison; NOT clean Zach baseline. Use carefully. |
| `records/observations/alpha-week-1-metrics-log.md` (when window closes) | Tracked | Zach + mature Alpha doctrine (refinements 008–013) + 1-week production work | **Primary cross-comparison target** with archive baseline |
| Future Beta-N transcripts | Tracked when filed | Zach + Carousel Mode + Zach-feedback-integrated doctrine | Beta-cycle comparison |

**Operator-confound disclosure:** Pre-Alpha 2 through 8 were run by Josh in Josh's Max account, simulating Zach's input. Rate measurements from these are NOT directly comparable to Zach's transcripts because:
- Different operator typing speed and chat patterns
- Different session-budget constraints (Max vs. Pro)
- Different familiarity with the system being tested

These transcripts can be used to measure **doctrine effect at constant operator** (Josh): how did the doctrine's effect on Josh's production rate evolve across refinements 008–013? That's a useful secondary measurement. But they are NOT input to Zach's time-saved baseline.

---

## Confounds and mitigations

The methodology has to disclose confounds, not hide them.

### Confound 1 — Operator improvement over time

Zach in 2024–2025 (founder archive era) was a different practitioner than Zach in 2026. He's improved at his craft AND at using Claude. Some of any rate gain is HIM improving, not the system.

**Mitigation:**
- Disclose this in every report; don't claim system-only attribution
- Where possible, look for non-doctrine-related changes in Zach's pace (e.g., did he get faster typing? did his clinical reasoning evolve in ways unrelated to the system?)
- Bound the confound: "estimated multiplier X is doctrine + operator improvement combined; doctrine-specific effect is at most X and at least 1.0"

### Confound 2 — Different work types across sections

Founder archive Zach-only sections were exploratory/discussion-heavy. Alpha-1 will be production-heavy. Discussion produces fewer artifacts per hour than production work, biasing baseline rate downward and inflating multiplier.

**Mitigation:**
- Tag each section by work type (production vs. exploration) when manually counting artifact units
- Compute rates within work-type categories; don't compare exploration-rate to production-rate across transcripts
- Where insufficient production-type data exists in the archive, narrow the baseline to the production-type subset and acknowledge sample size

### Confound 3 — Unit definition drift

If "artifact unit" is defined differently across transcripts (because of doctrine differences in what counts as a deliverable), comparisons are noise.

**Mitigation:**
- Use a single artifact unit list across all transcripts (the table in Stage 1)
- Document edge cases inline when counting
- A unit is a unit even if doctrine state changes its production process

### Confound 4 — Counterfactual gap

Zach can't run the same week twice with/without the system. Baseline measurements are necessarily different work in different weeks.

**Mitigation:**
- Acknowledge the counterfactual gap explicitly in every report
- Use multiple baseline sections (different weeks/topics from archive) to bound the variance, not just one section
- Treat the multiplier as "central estimate ± archive baseline variance" not "true value"

### Confound 5 — Quality at constant time

A 4× rate multiplier is meaningless if quality drops 50%. Time saved is illusory.

**Mitigation:**
- Quality Pass Rate is measured separately in the metrics framework
- Time-saved estimates are NOT reported in isolation; always alongside Quality Pass Rate
- A time-saved estimate from a Quality-failing window is reported as "rate X, but Quality failed; time-saved is invalid"

### Confound 6 — Account-tier asymmetry

Zach in Pro account hits session limits sooner than Josh in Max. If the limit binds during Alpha-1, observed rate is artificially low because the session ended before more output could be produced.

**Mitigation:**
- Pre-Alpha-9 budget test (already in pre-window dependency list) determines if the limit binds
- If limit binds during Alpha-1, exclude limit-truncated sections from rate analysis OR report rate-up-to-limit as a lower bound
- Beta cycle should resolve account-tier asymmetry as a structural concern

### Confound 7 — Single-shot vs iteration-arc chat (surfaced 2026-05-04 by parser validation)

The methodology measures **operator engagement time**, not model production time. Inter-message gaps reflect operator typing and thinking; model latency between request and response is invisible to the timestamps because timestamps mark message-send events, not response-completion.

For **iteration-arc chat** (Pre-Alpha-1 style: 23 messages over a 1.4-hour focused block, lots of back-and-forth refinement), focused-time is meaningful — it captures when the operator was actively engaged with the system.

For **single-shot chat** (Pre-Alpha-2/3/4/5/6/7/8 style: one comprehensive request → one comprehensive response → maybe one decision), focused-time is **artificially low**. The system did substantial production work during model-latency periods that the timestamps don't see. Pre-Alpha-8 parsed 2 timestamps spanning 1 minute, but the actual Alpha-locking artifact was produced in that minute's worth of operator engagement. Rate computation on single-shot transcripts produces misleadingly high rates because units / focused-hours has a tiny denominator.

**Mitigation:**
- Tag each transcript section in the YAML tag file with `chat_style: iteration-arc | single-shot | mixed`
- For single-shot sections, do NOT report rate-per-focused-hour as a comparable metric — report instead as "1 unit produced in the request-response exchange"
- Iteration-arc transcripts are the apples-to-apples comparison set for rate measurement
- Alpha-1 should be predominantly iteration-arc (Zach refining programs, iterating on content); confirm at end-of-window before applying full pipeline

### Confound 8 — Minute-precision timestamp deduplication (parser v1 limitation)

The current parser deduplicates consecutive identical timestamps to avoid noise (e.g., the same timestamp written twice in adjacent text). This drops legitimate same-minute messages when the operator sends multiple requests in the same minute.

**Mitigation (v1):** acknowledge that message counts and block-message-counts are lower bounds. For artifact-rate calculations this rarely matters because units are coarser than minutes. For high-frequency exchange analysis (e.g., > 5 messages per minute sustained), the parser would need second-level timestamps from Claude.ai export metadata.

**Future fix (v1.1+):** if Claude.ai web export provides second-level or millisecond timestamps, switch to those; otherwise accept minute-precision as the floor.

---

## Output format — the report structure

For each transcript-pair comparison, produce a section like:

```markdown
## [Source] vs [Comparison] — Rate analysis

### Inputs

- Source transcript: [path], [doctrine state], [date range], [operator]
- Comparison transcript: [path], [doctrine state], [date range], [operator]
- Artifact unit definitions: see Methodology Stage 1

### Stage 2 — Clustering

| Transcript | Total messages | Wall-clock hours | Focused-chat-hours | Block count | Avg block length | Block density |
|---|---|---|---|---|---|---|
| [Source] | N | X | Y | Z | A | Y/X |
| [Comparison] | N | X | Y | Z | A | Y/X |

### Stage 3 — Rate

| Transcript | Artifact units | Rate (units/focused-hour) | 90% CI |
|---|---|---|---|
| [Source] | N | r | [low, high] |
| [Comparison] | N | r | [low, high] |

### Stage 4 — Time saved estimate

- Multiplier: r_comparison / r_source = M (90% CI: [low, high])
- Reference work volume (e.g., Alpha-1 artifact production): N units
- Time at source rate to produce N: N/r_source = T_source hours
- Time at comparison rate to produce N: N/r_comparison = T_comparison hours
- Time saved over comparison period: T_source − T_comparison = T_saved hours
- Time saved per day (over D days): T_saved / D hours/day, 90% CI [low, high]

### Confounds disclosed

[Numbered list of which confounds apply, with mitigation status]

### Interpretation

[1–2 paragraphs of honest read]
```

---

## Implementation notes (for v1.1 — the actual analysis pass)

**Language**: Python (pandas + scikit-learn). Lightweight; no heavy dependencies.

**High-level structure:**

```python
# pseudocode

def parse_transcript(path) -> list[Message]:
    # extract (timestamp, author, content) tuples from markdown
    # handle Claude.ai timestamp formats ("3:11 PM", etc.)
    # gracefully degrade if timestamps missing
    pass

def cluster_blocks(messages, eps_minutes=15, min_samples=2) -> list[Block]:
    # DBSCAN on 1D timestamp array
    # return list of (start_t, end_t, message_count) tuples
    pass

def count_artifacts(transcript_path, manual_tag_file) -> dict[mode, int]:
    # apply manual artifact tags from companion .yaml/.json file
    # return per-mode counts
    pass

def compute_rate(artifacts, focused_hours) -> Rate:
    # bootstrap 90% CI
    pass

def time_saved_estimate(rate_baseline, rate_target, artifact_volume_target, days) -> TimeSaved:
    # propagate confidence intervals
    pass
```

**Manual tag file format** (companion to each transcript):

```yaml
# transcript: records/research/validation/2026-05-04-pre-alpha-1-zach-usage observation.md
# tagged by: Josh
# tag date: 2026-05-XX

artifacts:
  - section_start: "May 3 morning"
    section_end: "May 3 morning"
    mode: clinical
    unit: 1  # one case classification (left intercostal strain)
    notes: "26yo case, single classification turn"
  - section_start: "May 4 7:57 AM"
    section_end: "May 4 10:47 AM"
    mode: clinical
    unit: 1  # one programmed protocol with 20+ iterations
    notes: "iteration arc; cumulative artifact = 1 unit per iteration rule"
  # ...
```

The script + tag-file pair is the deliverable. The script is reusable across all transcripts; the tag-files are per-transcript manual annotation.

**Implementation cost estimate:**
- Initial script + tagging schema: ~3 hours
- First transcript pass (one of the Pre-Alpha files as proof-of-concept): ~1 hour
- Full archive baseline tagging: ~3–5 hours (depends on size of Zach-only PT sections)
- Pre-Alpha 1 + 8 tagging: ~1 hour each
- Alpha-1 tagging (when window closes): ~1 hour with Zach assist

**v1.1 scope:** ship the script + tag-schema + one proof-of-concept transcript analysis. Full baseline + cross-transcript comparison comes after Alpha-1 closes.

---

## Workflow — when to run, how often

**Pre-Alpha (now → window opens):**
- Pre-author the script and tag-schema (low-priority background work; doesn't block window)
- DO NOT run rate analysis on Alpha-1 data during the window (avoid Zach performing-for-the-measurement)

**At Alpha-1 window close:**
- Tag Alpha-1 transcripts (Zach assist for ambiguous unit decisions)
- Restore the archive locally; tag Zach-only PT sections
- Tag Pre-Alpha-1 (already tracked)
- Run the full pipeline: archive baseline rate + Pre-Alpha-1 rate + Alpha-1 rate
- Produce time-saved estimate band with confounds disclosed
- Report alongside the three primary metrics in the Alpha → Beta gate review

**Pre-Alpha 2–8 analysis (optional, secondary):**
- Useful for measuring doctrine-effect-at-constant-operator (Josh) across refinements 008–013
- NOT input to Zach's time-saved baseline (operator-confounded)
- Can be tagged + analyzed at any time as a doctrine-evolution sanity check

**Beta-N (future):**
- Same methodology, Beta doctrine state, Zach as operator
- Comparison: Alpha-1 rate vs. Beta-N rate = effect of Carousel + Zach-feedback integration

**Re-run triggers:**
- New doctrine state stabilizes (lock event)
- Operator change (e.g., second operator joins)
- Significant doctrine refinement (e.g., compaction pass that might shift the rate)

---

## Limitations — what this can NEVER measure

Honest framing — even with rigorous methodology, this analysis cannot:

1. **Prove causal attribution to specific doctrine pieces.** Multipliers measure aggregate doctrine-state effect. Whether refinement-008 vs. refinement-013 specifically drove the rate change is opaque. Doctrine-specific attribution requires controlled A/B tests this methodology doesn't support.

2. **Isolate operator improvement from system improvement.** Confound 1 is structural; cannot fully resolve.

3. **Measure leverage on work Zach didn't do.** If Zach's window doesn't include Insight Mode work, this analysis says nothing about Insight Mode time savings.

4. **Predict steady-state rates.** A 1-week window may show novelty-adoption effects (Zach trying new patterns enthusiastically) that decay over months.

5. **Capture quality-at-constant-time.** Volume rate alone is incomplete; Quality Pass Rate is required to interpret time-saved.

6. **Substitute for Decision Confidence.** A high time-saved estimate from a low-Confidence window means Zach isn't actually using the saved time — leverage isn't realized.

The methodology produces **defensible estimates with stated bounds for one axis of leverage measurement**. It is sufficient evidence to inform Beta scoping. It is NOT sufficient evidence to make claims about absolute productivity gain.

---

## Pointer back

- **Operator**: Josh
- **Founder**: Zach
- **Date**: 2026-05-04
- **Status**: methodology v1 authored. Implementation script + tag-schema pending (low-priority, pre-window background work).

The companion implementation will live at `scripts/clustering_rate_analysis.py` (when authored) with per-transcript tag files at `records/observations/rate-analysis-tags/<transcript-name>.yaml`. End-of-Alpha-1 review uses this methodology to produce the time-saved estimate alongside the three primary metrics from `architecture/alpha-production-validation-metrics-v1.md`.

---

## Last Updated

2026-05-04 — initial methodology authored at Alpha lock. Four-stage analytical pipeline (artifact unit definition / DBSCAN clustering / rate calculation / time-saved estimation). DBSCAN with `eps=15min`, `min_samples=2` chosen over gap-threshold for robustness against within-block thinking pauses + outlier message handling. Six confounds disclosed (operator improvement, work-type drift, unit definition drift, counterfactual gap, quality at constant time, account-tier asymmetry) with mitigations specified. Reportable output is a confidence band, not a point estimate. Operator-confound on Pre-Alpha 2–8 (Josh acting as Zach in Josh's account) flagged — useful for doctrine-effect-at-constant-operator measurement, NOT clean Zach baselining. Implementation deferred to v1.1 as low-priority pre-window background work; full pipeline runs at Alpha-1 close.
