"""Run-to-run memory, so the watcher alerts on change rather than on existence."""

from __future__ import annotations

import json
import os
from pathlib import Path


def default_state_path() -> Path:
    base = os.environ.get("XDG_STATE_HOME") or os.path.expanduser("~/.local/state")
    return Path(base) / "bountywatch" / "seen.json"


def load(path: Path) -> dict:
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
            return data if isinstance(data, dict) else {}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save(path: Path, state: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=2, sort_keys=True)
    os.replace(tmp, path)


def diff(bounties, state: dict) -> tuple[list, dict]:
    """Return the bounties worth alerting on, plus the state to persist.

    Something is alert-worthy when it is newly seen, or when its claim state
    has moved. The second case is the valuable one: an issue going from
    `claimed` to `unclaimed` is a bounty being released back into the pool,
    which is exactly the moment worth acting on.
    """
    alerts = []
    next_state = dict(state)

    for bounty in bounties:
        previous = state.get(bounty.key)
        record = {
            "claim": bounty.claim,
            "priority": bounty.priority,
            "title": bounty.title,
            "url": bounty.url,
            "amount_high": bounty.amount_high,
        }

        if previous is None:
            bounty.reasons = ("NEW listing",) + bounty.reasons
            alerts.append(bounty)
        elif previous.get("claim") != bounty.claim:
            bounty.reasons = (
                f"claim state changed: {previous.get('claim')} -> {bounty.claim}",
            ) + bounty.reasons
            alerts.append(bounty)

        next_state[bounty.key] = record

    return alerts, next_state
