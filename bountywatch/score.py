"""Filtering and ranking.

The ranking encodes one strategic judgement: an unclaimed issue you can
validate without buying an accelerator is worth far more than a larger bounty
that is already assigned or needs silicon you do not own.
"""

from __future__ import annotations

from .config import (
    HARDWARE_MARKERS,
    JUNK_REPO_MARKERS,
    JUNK_TITLE_MARKERS,
    SIMULATOR_MARKERS,
    TRUSTED_REPOS,
    DEFAULT_STALE_DAYS,
)
from .model import Bounty, parse_amount, utcnow

# Claim states
UNCLAIMED = "unclaimed"
STALE_CLAIM = "stale_claim"
CLAIMED = "claimed"

# Hardware verdicts
SIM_OK = "simulator_ok"
HARDWARE = "hardware_required"
MIXED = "mixed"
UNKNOWN = "unknown"

# Priority bands. Higher sorts first.
P_UNCLAIMED_SIM = 100
P_UNCLAIMED_UNKNOWN = 90
P_UNCLAIMED_HARDWARE = 80
P_STALE_SIM = 60
P_STALE_UNKNOWN = 55
P_STALE_HARDWARE = 50
P_CLAIMED = 10


def is_junk(bounty: Bounty) -> bool:
    """Reject bookkeeping noise and repos that farm bounty searches."""
    repo = bounty.repo.lower()
    if any(marker in repo for marker in JUNK_REPO_MARKERS):
        return True
    title = bounty.title.lower()
    return any(marker in title for marker in JUNK_TITLE_MARKERS)


def classify_hardware(bounty: Bounty) -> tuple[str, tuple[str, ...]]:
    """Guess whether silicon is needed, and show the evidence.

    This is a keyword heuristic, not a judgement -- it returns the matched
    phrases so a human can overrule it. An explicit "does not require
    hardware" outranks an incidental mention of a chip name, because bounties
    routinely name the target architecture while still being simulator-
    testable.
    """
    haystack = f"{bounty.title}\n{bounty.body}".lower()
    sim_hits = tuple(m for m in SIMULATOR_MARKERS if m in haystack)
    hw_hits = tuple(m for m in HARDWARE_MARKERS if m in haystack)

    if sim_hits and hw_hits:
        return MIXED, sim_hits + hw_hits
    if sim_hits:
        return SIM_OK, sim_hits
    if hw_hits:
        return HARDWARE, hw_hits
    return UNKNOWN, ()


def classify_claim(bounty: Bounty, stale_days: int, now=None) -> tuple[str, int | None]:
    """Classify assignment state and idle time.

    The Tenstorrent terms allow an issue to be reassigned when its assignee
    goes quiet for more than two weeks, which makes a long-idle assignment a
    real opening rather than a closed door.
    """
    now = now or utcnow()
    idle_days = None
    if bounty.updated_at:
        idle_days = max(0, (now - bounty.updated_at).days)

    if not bounty.is_claimed:
        return UNCLAIMED, idle_days
    if idle_days is not None and idle_days > stale_days:
        return STALE_CLAIM, idle_days
    return CLAIMED, idle_days


_PRIORITY = {
    (UNCLAIMED, SIM_OK): P_UNCLAIMED_SIM,
    (UNCLAIMED, UNKNOWN): P_UNCLAIMED_UNKNOWN,
    (UNCLAIMED, MIXED): P_UNCLAIMED_UNKNOWN,
    (UNCLAIMED, HARDWARE): P_UNCLAIMED_HARDWARE,
    (STALE_CLAIM, SIM_OK): P_STALE_SIM,
    (STALE_CLAIM, UNKNOWN): P_STALE_UNKNOWN,
    (STALE_CLAIM, MIXED): P_STALE_UNKNOWN,
    (STALE_CLAIM, HARDWARE): P_STALE_HARDWARE,
}


def classify(bounty: Bounty, stale_days: int = DEFAULT_STALE_DAYS, now=None) -> Bounty:
    """Fill in every derived field on a Bounty, in place."""
    bounty.amount_low, bounty.amount_high = parse_amount(bounty.title)
    bounty.hardware, bounty.hardware_evidence = classify_hardware(bounty)
    bounty.claim, bounty.idle_days = classify_claim(bounty, stale_days, now=now)
    bounty.priority = _PRIORITY.get((bounty.claim, bounty.hardware), P_CLAIMED)

    reasons = []
    if bounty.claim == UNCLAIMED:
        reasons.append("unassigned - claimable now")
    elif bounty.claim == STALE_CLAIM:
        reasons.append(
            f"assigned to {', '.join(bounty.assignees)} but idle {bounty.idle_days}d "
            f"(>{stale_days}d: reassignment permitted by program terms)"
        )
    else:
        reasons.append(f"assigned to {', '.join(bounty.assignees)}, active")

    if bounty.hardware == SIM_OK:
        reasons.append("no silicon needed")
    elif bounty.hardware == HARDWARE:
        reasons.append("needs Tenstorrent hardware")
    elif bounty.hardware == MIXED:
        reasons.append("hardware signals conflict - read the issue")

    bounty.reasons = tuple(reasons)
    return bounty


def rank(bounties, stale_days: int = DEFAULT_STALE_DAYS, now=None, trusted_only: bool = True):
    """Filter junk, classify, and sort best-first.

    Sort is by priority band, then by the top of the advertised range, then by
    newest -- a fresh unclaimed issue is the thing worth waking up for.
    """
    out = []
    for bounty in bounties:
        if is_junk(bounty):
            continue
        if trusted_only and bounty.repo not in TRUSTED_REPOS:
            continue
        out.append(classify(bounty, stale_days=stale_days, now=now))

    out.sort(
        key=lambda b: (
            b.priority,
            b.amount_high or 0,
            b.created_at.timestamp() if b.created_at else 0,
        ),
        reverse=True,
    )
    return out
