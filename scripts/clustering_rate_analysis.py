#!/usr/bin/env python3
"""
clustering_rate_analysis.py — DBSCAN-clustered transcript analysis for The Muscle PT system

Implements the methodology in architecture/clustering-rate-analysis-method-v1.md.

Pipeline:
  1. Parse transcript timestamps (inline H:MM AM/PM markers in the markdown)
  2. Cluster timestamps via 1D DBSCAN (eps=15min default, min_samples=2)
  3. Compute rate (artifact_units / focused_chat_hours) with bootstrap 90% CI
  4. (compare command) Produce multiplier + time-saved estimate band

Usage:
  Validate parser on a transcript (no tags needed):
    python scripts/clustering_rate_analysis.py validate-parser <transcript_path>

  Analyze one transcript (requires tag file):
    python scripts/clustering_rate_analysis.py analyze <transcript_path> <tag_file>

  Compare baseline vs target:
    python scripts/clustering_rate_analysis.py compare <baseline_transcript> <baseline_tags> <target_transcript> <target_tags>

Outputs markdown to stdout. Pipe to a file or paste into the Alpha-1 analytical entry.
"""

from __future__ import annotations

import argparse
import random
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

try:
    import yaml
except ImportError:
    print("error: PyYAML required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


# --- Timestamp parsing ---------------------------------------------------------
# Pre-Alpha 1-8 transcripts use "H:MM AM/PM" inline markers in the markdown body.
# Founder archive may use additional formats; extend the patterns list as needed.

TIME_PATTERNS = [
    # Pre-Alpha 1-8 timestamps are often run together with adjacent text
    # (e.g. "breathing.7:57 AMClaude responded:"), so no trailing \b.
    # Leading constraint: digit must be preceded by a non-digit to avoid matching
    # part of a longer number sequence.
    re.compile(r"(?<!\d)(\d{1,2}):(\d{2})\s*(AM|PM)", re.IGNORECASE),
]


def parse_transcript(transcript_path: Path, base_date: Optional[str] = None) -> list[datetime]:
    """
    Extract message timestamps from a transcript markdown file.

    Returns a sorted list of datetime objects, one per timestamped message.
    Day rollover is handled by detecting decreases in time-of-day.

    base_date: anchor date (YYYY-MM-DD). If None, infers from filename pattern.
    """
    text = transcript_path.read_text(encoding="utf-8")

    if base_date is None:
        m = re.search(r"(\d{4}-\d{2}-\d{2})", transcript_path.name)
        base_date = m.group(1) if m else datetime.now().strftime("%Y-%m-%d")

    base = datetime.strptime(base_date, "%Y-%m-%d")

    timestamps: list[datetime] = []
    last_dt: Optional[datetime] = None

    for pattern in TIME_PATTERNS:
        for match in pattern.finditer(text):
            hour = int(match.group(1))
            minute = int(match.group(2))
            ampm = match.group(3).upper()

            if ampm == "PM" and hour != 12:
                hour += 12
            elif ampm == "AM" and hour == 12:
                hour = 0

            dt = base.replace(hour=hour, minute=minute, second=0, microsecond=0)

            if last_dt is not None and dt < last_dt:
                dt += timedelta(days=1)
                base = dt.replace(hour=0, minute=0)

            if last_dt is not None and dt == last_dt:
                continue

            timestamps.append(dt)
            last_dt = dt

    return timestamps


# --- DBSCAN clustering (1D) ----------------------------------------------------

@dataclass
class WorkBlock:
    start: datetime
    end: datetime
    message_count: int

    @property
    def duration_minutes(self) -> float:
        return (self.end - self.start).total_seconds() / 60.0


def cluster_blocks(timestamps: list[datetime], eps_minutes: float = 15.0, min_samples: int = 2) -> list[WorkBlock]:
    """
    1D DBSCAN clustering on timestamps with eps in minutes.

    For sorted 1D temporal data, DBSCAN with eps=t and min_samples=k reduces to:
    walk through, group messages where each consecutive gap <= eps, drop clusters smaller than k.
    Lone messages (gap > eps on both sides) become noise points and are excluded.
    """
    if not timestamps:
        return []

    blocks: list[WorkBlock] = []
    block_start = timestamps[0]
    block_end = timestamps[0]
    block_count = 1

    for i in range(1, len(timestamps)):
        gap = (timestamps[i] - timestamps[i - 1]).total_seconds() / 60.0

        if gap <= eps_minutes:
            block_end = timestamps[i]
            block_count += 1
        else:
            if block_count >= min_samples:
                blocks.append(WorkBlock(block_start, block_end, block_count))
            block_start = timestamps[i]
            block_end = timestamps[i]
            block_count = 1

    if block_count >= min_samples:
        blocks.append(WorkBlock(block_start, block_end, block_count))

    return blocks


# --- Tag file loading ----------------------------------------------------------

def load_tags(tag_path: Path) -> dict:
    """Load YAML artifact-unit tag file. See _schema.yaml for the format."""
    return yaml.safe_load(tag_path.read_text(encoding="utf-8"))


# --- Rate computation ----------------------------------------------------------

@dataclass
class RateResult:
    artifact_units: int
    focused_minutes: float
    walltime_minutes: float
    block_count: int

    @property
    def focused_hours(self) -> float:
        return self.focused_minutes / 60.0

    @property
    def walltime_hours(self) -> float:
        return self.walltime_minutes / 60.0

    @property
    def rate_focused(self) -> float:
        return self.artifact_units / self.focused_hours if self.focused_hours > 0 else 0.0

    @property
    def rate_walltime(self) -> float:
        return self.artifact_units / self.walltime_hours if self.walltime_hours > 0 else 0.0

    @property
    def avg_block_minutes(self) -> float:
        return self.focused_minutes / self.block_count if self.block_count else 0.0

    @property
    def density(self) -> float:
        return self.focused_minutes / self.walltime_minutes if self.walltime_minutes > 0 else 0.0


def compute_rate(timestamps: list[datetime], blocks: list[WorkBlock], tags: dict) -> RateResult:
    if not timestamps or not blocks:
        return RateResult(0, 0.0, 0.0, 0)

    units = sum(int(item.get("unit", 0)) for item in tags.get("artifacts", []))
    focused_min = sum(b.duration_minutes for b in blocks)
    walltime_min = (timestamps[-1] - timestamps[0]).total_seconds() / 60.0

    return RateResult(
        artifact_units=units,
        focused_minutes=focused_min,
        walltime_minutes=walltime_min,
        block_count=len(blocks),
    )


# --- Bootstrap CI --------------------------------------------------------------

def bootstrap_rate_ci(units: int, focused_hours: float, n_iter: int = 1000, ci_pct: float = 90.0,
                      seed: Optional[int] = 42) -> tuple[float, float]:
    """
    Bootstrap a CI on the rate by resampling artifact-presence with replacement.

    For small samples (units < 5) bounds are wide — that's the honest report.
    For production statistical rigor, prefer scipy.stats.bootstrap.
    """
    if units == 0 or focused_hours == 0:
        return (0.0, 0.0)

    rng = random.Random(seed)
    rates = []
    for _ in range(n_iter):
        # Bernoulli-style resample of unit presence
        resampled_units = sum(1 for _ in range(units) if rng.random() < 0.5) * 2
        rates.append(resampled_units / focused_hours)

    rates.sort()
    alpha = (1 - ci_pct / 100.0) / 2.0
    low_idx = int(len(rates) * alpha)
    high_idx = int(len(rates) * (1 - alpha)) - 1
    return (rates[low_idx], rates[high_idx])


# --- Reporting -----------------------------------------------------------------

def render_validation(transcript_path: Path, timestamps: list[datetime], blocks: list[WorkBlock]) -> str:
    lines = [f"# Parser validation — {transcript_path.name}", ""]
    lines.append(f"**Messages with parsed timestamps**: {len(timestamps)}")
    if timestamps:
        lines.append(f"**First timestamp**: {timestamps[0].isoformat()}")
        lines.append(f"**Last timestamp**: {timestamps[-1].isoformat()}")
        wall_min = (timestamps[-1] - timestamps[0]).total_seconds() / 60.0
        lines.append(f"**Wall-clock span**: {wall_min:.1f} min")
    focused_min = sum(b.duration_minutes for b in blocks)
    lines.append("")
    lines.append(f"**Work blocks (eps=15min, min_samples=2)**: {len(blocks)}")
    lines.append(f"**Total focused-chat-time**: {focused_min:.1f} min ({focused_min/60:.2f} hours)")
    lines.append("")
    lines.append("| # | Start | End | Duration (min) | Messages |")
    lines.append("|---|---|---|---|---|")
    for i, b in enumerate(blocks, 1):
        lines.append(f"| {i} | {b.start.isoformat()} | {b.end.isoformat()} | {b.duration_minutes:.1f} | {b.message_count} |")
    return "\n".join(lines) + "\n"


def render_analysis(transcript_path: Path, tags: dict, timestamps: list[datetime],
                    blocks: list[WorkBlock], rate: RateResult, ci: tuple[float, float]) -> str:
    operator = tags.get("operator", "unknown")
    doctrine = tags.get("doctrine_state", "unknown")
    work_type = tags.get("work_type", "unknown")

    lines = [
        f"# Analysis — {transcript_path.name}",
        "",
        f"**Operator**: {operator}  ",
        f"**Doctrine state**: {doctrine}  ",
        f"**Work type**: {work_type}",
        "",
        "## Clustering",
        "",
        f"- Messages parsed: **{len(timestamps)}**",
        f"- Wall-clock span: **{rate.walltime_minutes:.1f} min** ({rate.walltime_hours:.2f} hours)",
        f"- Focused chat time (sum of blocks): **{rate.focused_minutes:.1f} min** ({rate.focused_hours:.2f} hours)",
        f"- Block density (focused/wall): **{rate.density:.1%}**",
        f"- Block count: **{rate.block_count}** (avg {rate.avg_block_minutes:.1f} min/block)",
        "",
        "## Rate",
        "",
        f"- Artifact units (from tags): **{rate.artifact_units}**",
        f"- **Rate (focused-chat-hours)**: {rate.rate_focused:.3f} units/hour, 90% CI [{ci[0]:.3f}, {ci[1]:.3f}]",
        f"- Rate (wall-clock-hours, reference only): {rate.rate_walltime:.3f} units/hour",
        "",
    ]

    notes = tags.get("notes")
    if notes:
        lines.extend(["## Notes", "", str(notes).strip(), ""])

    return "\n".join(lines) + "\n"


def render_comparison(baseline_path: Path, target_path: Path,
                      baseline_rate: RateResult, baseline_ci: tuple[float, float],
                      target_rate: RateResult, target_ci: tuple[float, float],
                      target_window_days: int = 7) -> str:
    """Produce comparison report with multiplier + time-saved band."""
    lines = [
        f"# Comparison — {baseline_path.name} (baseline) vs {target_path.name} (target)",
        "",
        "## Rates",
        "",
        "| Transcript | Units | Focused hours | Rate (units/hour) | 90% CI |",
        "|---|---|---|---|---|",
        f"| Baseline ({baseline_path.name}) | {baseline_rate.artifact_units} | {baseline_rate.focused_hours:.2f} | {baseline_rate.rate_focused:.3f} | [{baseline_ci[0]:.3f}, {baseline_ci[1]:.3f}] |",
        f"| Target ({target_path.name}) | {target_rate.artifact_units} | {target_rate.focused_hours:.2f} | {target_rate.rate_focused:.3f} | [{target_ci[0]:.3f}, {target_ci[1]:.3f}] |",
        "",
    ]

    if baseline_rate.rate_focused > 0 and target_rate.rate_focused > 0:
        # Central multiplier
        multiplier = target_rate.rate_focused / baseline_rate.rate_focused
        # CI propagation: low_target / high_baseline → multiplier_low; high_target / low_baseline → multiplier_high
        mult_low = target_ci[0] / baseline_ci[1] if baseline_ci[1] > 0 else 0
        mult_high = target_ci[1] / baseline_ci[0] if baseline_ci[0] > 0 else float("inf")

        lines.extend([
            "## Multiplier",
            "",
            f"- Central: **{multiplier:.2f}×**",
            f"- 90% CI (propagated): [{mult_low:.2f}, {mult_high:.2f}]×",
            "",
        ])

        # Time-saved estimate
        N = target_rate.artifact_units
        if N > 0:
            time_at_baseline = N / baseline_rate.rate_focused
            time_at_target = N / target_rate.rate_focused
            saved = time_at_baseline - time_at_target
            saved_per_day = saved / target_window_days

            saved_per_day_low = (N / baseline_ci[1] - N / target_ci[1]) / target_window_days if baseline_ci[1] > 0 else 0
            saved_per_day_high = (N / baseline_ci[0] - N / target_ci[0]) / target_window_days if baseline_ci[0] > 0 else 0

            lines.extend([
                "## Time saved estimate",
                "",
                f"- Target produced **{N} artifact units** in **{target_rate.focused_hours:.2f} focused-chat-hours**",
                f"- At baseline rate, same volume would take: **{time_at_baseline:.2f} hours**",
                f"- Time saved over the window: **{saved:.2f} hours**",
                f"- **Time saved per day** ({target_window_days}-day window): **{saved_per_day:.2f} hours/day**",
                f"- 90% CI: [{saved_per_day_low:.2f}, {saved_per_day_high:.2f}] hours/day",
                "",
            ])

    lines.extend([
        "## Confounds disclosed",
        "",
        "1. Counterfactual gap — different work in different weeks",
        "2. Operator improvement — operator skill change is confounded with system effect",
        "3. Work-type drift — verify both transcripts are tagged the same work type (production vs exploration)",
        "4. Quality at constant time — rate alone is incomplete; report alongside Quality Pass Rate",
        "5. Account-tier asymmetry — if Pro budget bound during target window, rate is artificially low",
        "",
        "See `architecture/clustering-rate-analysis-method-v1.md` for the full confound list and mitigations.",
        "",
    ])

    return "\n".join(lines) + "\n"


# --- Entry point ---------------------------------------------------------------

def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1] if __doc__ else "")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_v = sub.add_parser("validate-parser", help="Parse a transcript and report block structure (no tags needed)")
    p_v.add_argument("transcript", type=Path)
    p_v.add_argument("--base-date", type=str, default=None)
    p_v.add_argument("--eps-minutes", type=float, default=15.0)
    p_v.add_argument("--min-samples", type=int, default=2)

    p_a = sub.add_parser("analyze", help="Analyze a single transcript with its tag file")
    p_a.add_argument("transcript", type=Path)
    p_a.add_argument("tags", type=Path)
    p_a.add_argument("--base-date", type=str, default=None)
    p_a.add_argument("--eps-minutes", type=float, default=15.0)
    p_a.add_argument("--min-samples", type=int, default=2)

    p_c = sub.add_parser("compare", help="Compare baseline vs target")
    p_c.add_argument("baseline_transcript", type=Path)
    p_c.add_argument("baseline_tags", type=Path)
    p_c.add_argument("target_transcript", type=Path)
    p_c.add_argument("target_tags", type=Path)
    p_c.add_argument("--target-days", type=int, default=7,
                     help="Number of days the target window spans (default 7)")
    p_c.add_argument("--eps-minutes", type=float, default=15.0)
    p_c.add_argument("--min-samples", type=int, default=2)

    args = parser.parse_args(argv)

    if args.cmd == "validate-parser":
        ts = parse_transcript(args.transcript, args.base_date)
        blocks = cluster_blocks(ts, args.eps_minutes, args.min_samples)
        sys.stdout.write(render_validation(args.transcript, ts, blocks))
        return 0

    if args.cmd == "analyze":
        ts = parse_transcript(args.transcript, args.base_date)
        blocks = cluster_blocks(ts, args.eps_minutes, args.min_samples)
        tags = load_tags(args.tags)
        rate = compute_rate(ts, blocks, tags)
        ci = bootstrap_rate_ci(rate.artifact_units, rate.focused_hours)
        sys.stdout.write(render_analysis(args.transcript, tags, ts, blocks, rate, ci))
        return 0

    if args.cmd == "compare":
        b_ts = parse_transcript(args.baseline_transcript)
        b_blocks = cluster_blocks(b_ts, args.eps_minutes, args.min_samples)
        b_tags = load_tags(args.baseline_tags)
        b_rate = compute_rate(b_ts, b_blocks, b_tags)
        b_ci = bootstrap_rate_ci(b_rate.artifact_units, b_rate.focused_hours)

        t_ts = parse_transcript(args.target_transcript)
        t_blocks = cluster_blocks(t_ts, args.eps_minutes, args.min_samples)
        t_tags = load_tags(args.target_tags)
        t_rate = compute_rate(t_ts, t_blocks, t_tags)
        t_ci = bootstrap_rate_ci(t_rate.artifact_units, t_rate.focused_hours)

        sys.stdout.write(render_comparison(
            args.baseline_transcript, args.target_transcript,
            b_rate, b_ci, t_rate, t_ci, args.target_days,
        ))
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
