"""Data model and normalisation of GitHub search results."""

from __future__ import annotations

import re
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone

# Matches a dollar figure with optional thousands separators, decimal part and
# a k/K multiplier, optionally as a range ("$500-2500", "$500 - $2.5k").
_AMOUNT = re.compile(
    r"\$\s*(?P<lo>\d[\d,]*(?:\.\d+)?)\s*(?P<lok>[kK])?"
    r"(?:\s*[-‒–—]\s*\$?\s*(?P<hi>\d[\d,]*(?:\.\d+)?)\s*(?P<hik>[kK])?)?"
)


def _to_int(raw: str, k_suffix: str | None) -> int:
    """Convert a matched money string to whole dollars."""
    value = float(raw.replace(",", ""))
    if k_suffix:
        value *= 1000
    return int(round(value))


def parse_amount(title: str) -> tuple[int | None, int | None]:
    """Extract (low, high) USD from a bounty title.

    Returns (None, None) when no figure is present -- titles like
    "[$$ BOUNTY] Add Qwen 1.5" advertise a bounty without naming a number.
    For a single figure, low == high.
    """
    if not title:
        return (None, None)
    match = _AMOUNT.search(title)
    if not match:
        return (None, None)
    low = _to_int(match.group("lo"), match.group("lok"))
    if match.group("hi"):
        high = _to_int(match.group("hi"), match.group("hik"))
        if high < low:
            low, high = high, low
        return (low, high)
    return (low, low)


def _parse_ts(raw: str | None) -> datetime | None:
    if not raw:
        return None
    try:
        return datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        return None


@dataclass
class Bounty:
    """One candidate bounty issue, normalised from the GitHub search API."""

    repo: str
    number: int
    title: str
    url: str
    body: str = ""
    assignees: tuple[str, ...] = ()
    labels: tuple[str, ...] = ()
    created_at: datetime | None = None
    updated_at: datetime | None = None
    comments: int = 0

    # Derived, filled in by score.classify()
    amount_low: int | None = None
    amount_high: int | None = None
    hardware: str = "unknown"
    hardware_evidence: tuple[str, ...] = ()
    claim: str = "unknown"
    idle_days: int | None = None
    priority: int = 0
    reasons: tuple[str, ...] = field(default_factory=tuple)

    @property
    def key(self) -> str:
        """Stable identity across runs."""
        return f"{self.repo}#{self.number}"

    @property
    def is_claimed(self) -> bool:
        return bool(self.assignees)

    def to_dict(self) -> dict:
        data = asdict(self)
        for stamp in ("created_at", "updated_at"):
            value = data.get(stamp)
            data[stamp] = value.isoformat() if value else None
        return data


def from_search_item(item: dict) -> Bounty:
    """Build a Bounty from one GitHub issue-search result item.

    The search API returns the issue's html_url but not its repo name as a
    field, so the repo is recovered from repository_url
    (https://api.github.com/repos/{owner}/{repo}).
    """
    repo_url = item.get("repository_url") or ""
    repo = "/".join(repo_url.rsplit("/", 2)[-2:]) if repo_url else ""

    assignees = tuple(
        a.get("login", "")
        for a in (item.get("assignees") or [])
        if a.get("login")
    )
    # Older payloads carry a singular `assignee` instead of the list.
    if not assignees and item.get("assignee"):
        login = item["assignee"].get("login")
        if login:
            assignees = (login,)

    labels = tuple(
        lbl.get("name", "") if isinstance(lbl, dict) else str(lbl)
        for lbl in (item.get("labels") or [])
    )

    return Bounty(
        repo=repo,
        number=int(item.get("number", 0)),
        title=item.get("title") or "",
        url=item.get("html_url") or "",
        body=item.get("body") or "",
        assignees=assignees,
        labels=labels,
        created_at=_parse_ts(item.get("created_at")),
        updated_at=_parse_ts(item.get("updated_at")),
        comments=int(item.get("comments") or 0),
    )


def utcnow() -> datetime:
    return datetime.now(timezone.utc)
