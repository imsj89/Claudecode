"""Rendering and delivery of alerts."""

from __future__ import annotations

import json
import urllib.error
import urllib.request

from .score import STALE_CLAIM, UNCLAIMED

_BADGE = {
    UNCLAIMED: "OPEN ",
    STALE_CLAIM: "STALE",
}


def money(bounty) -> str:
    if bounty.amount_low is None:
        return "$?"
    if bounty.amount_high != bounty.amount_low:
        return f"${bounty.amount_low:,}-${bounty.amount_high:,}"
    return f"${bounty.amount_low:,}"


def render_text(bounties, show_all: bool = False) -> str:
    if not bounties:
        return "No bounties matched."

    lines = []
    for bounty in bounties:
        badge = _BADGE.get(bounty.claim, "taken")
        lines.append(f"[{badge}] {money(bounty):>16}  {bounty.repo}#{bounty.number}")
        lines.append(f"          {bounty.title}")
        lines.append(f"          {bounty.url}")
        for reason in bounty.reasons:
            lines.append(f"            - {reason}")
        if bounty.hardware_evidence and show_all:
            joined = ", ".join(bounty.hardware_evidence[:6])
            lines.append(f"            - matched: {joined}")
        lines.append("")
    return "\n".join(lines).rstrip()


def render_json(bounties) -> str:
    return json.dumps([b.to_dict() for b in bounties], indent=2, default=str)


def post_webhook(url: str, bounties, timeout: int = 15) -> bool:
    """POST a Slack/Discord-compatible payload. Returns True on 2xx."""
    if not bounties:
        return True
    summary = render_text(bounties)
    body = json.dumps({"text": f"bountywatch: {len(bounties)} alert(s)\n\n{summary}"})
    req = urllib.request.Request(
        url,
        data=body.encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": "bountywatch/0.1"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return 200 <= resp.status < 300
    except (urllib.error.HTTPError, urllib.error.URLError):
        return False


_CLAIM_OPEN = """\
Hi - I'd like to pick this one up. Could you assign it to me?

Plan of attack:
  1. <one line on the approach>
  2. <how you will validate it>

I'll open a PR while assigned, per the bounty program terms. If you'd rather
hold it for someone else, no problem - just say so and I'll drop it.\
"""

_CLAIM_STALE = """\
Hi @{assignee} / maintainers - is this still being worked on? The issue has
been idle for {idle} days.

If it's still active I'll stay clear. If it's been dropped, I'd be glad to
take it over - happy to be assigned and open a PR.\
"""


def render_claim(bounty) -> str:
    """A ready-to-post claim comment for the user to send under their own name.

    Kept deliberately plain and honest: it makes no promises about timelines
    and explicitly offers to stand down. The stale variant asks rather than
    assumes, because an idle assignment is the assignee's call first and the
    maintainer's second.
    """
    header = f"--- draft comment for {bounty.repo}#{bounty.number} ---\n{bounty.url}\n"
    if bounty.claim == STALE_CLAIM and bounty.assignees:
        body = _CLAIM_STALE.format(
            assignee=bounty.assignees[0], idle=bounty.idle_days,
        )
    else:
        body = _CLAIM_OPEN
    return f"{header}\n{body}\n"
