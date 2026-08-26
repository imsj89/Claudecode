"""Command line entry point."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import gh, notify, state as state_mod
from .config import DEFAULT_QUERIES, DEFAULT_STALE_DAYS
from .model import from_search_item
from .score import CLAIMED, rank


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="bountywatch",
        description=(
            "Watch funded bounty boards for issues you can actually claim. "
            "Payout on the Tenstorrent program requires being assigned to the "
            "issue before you open a PR, so this ranks by claimability first "
            "and dollar amount second."
        ),
    )
    parser.add_argument(
        "--query", action="append", default=None,
        help="Override the default searches. Repeatable.",
    )
    parser.add_argument(
        "--fixture", type=Path, default=None,
        help="Read search results from a JSON file instead of the network. "
             "Accepts a list of items or a {'items': [...]} payload.",
    )
    parser.add_argument(
        "--state", type=Path, default=None,
        help=f"State file path (default: {state_mod.default_state_path()}).",
    )
    parser.add_argument(
        "--stale-days", type=int, default=DEFAULT_STALE_DAYS,
        help="Idle days before an assigned issue counts as reassignable.",
    )
    parser.add_argument(
        "--min-amount", type=int, default=0,
        help="Hide bounties advertised below this dollar figure.",
    )
    parser.add_argument(
        "--include-untrusted", action="store_true",
        help="Also report repos outside the program's in-scope list. Generic "
             "bounty searches are heavily polluted, so this is off by default.",
    )
    parser.add_argument(
        "--all", action="store_true",
        help="Show every match, including actively-claimed issues.",
    )
    parser.add_argument(
        "--json", action="store_true", help="Emit JSON instead of text.",
    )
    parser.add_argument(
        "--claim-template", action="store_true",
        help="Also print a ready-to-post claim comment for each alert. "
             "You post it yourself, under your own name.",
    )
    parser.add_argument(
        "--webhook", default=None, help="POST alerts to this Slack/Discord URL.",
    )
    parser.add_argument(
        "--no-state", action="store_true",
        help="Report everything and do not read or write the state file.",
    )
    parser.add_argument(
        "--max-pages", type=int, default=3, help="Search pages per query.",
    )
    return parser


def load_fixture(path: Path) -> list[dict]:
    with open(path, "r", encoding="utf-8") as fh:
        payload = json.load(fh)
    if isinstance(payload, dict):
        return payload.get("items") or []
    return payload


def collect(args) -> list[dict]:
    if args.fixture:
        return load_fixture(args.fixture)

    token = gh.token_from_env()
    if not token:
        print(
            "warning: no GITHUB_TOKEN set - unauthenticated search is capped at "
            "10 requests/minute and may fail under load",
            file=sys.stderr,
        )

    raw: list[dict] = []
    seen_urls = set()
    for query in (args.query or list(DEFAULT_QUERIES)):
        items = gh.search_issues(query, token=token, max_pages=args.max_pages)
        for item in items:
            url = item.get("html_url")
            if url and url not in seen_urls:
                seen_urls.add(url)
                raw.append(item)
    return raw


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)

    try:
        raw = collect(args)
    except gh.RateLimited as exc:
        print(f"rate limited: {exc}", file=sys.stderr)
        return 2
    except gh.SearchError as exc:
        print(f"search failed: {exc}", file=sys.stderr)
        return 2
    except (OSError, json.JSONDecodeError) as exc:
        print(f"could not read fixture: {exc}", file=sys.stderr)
        return 2

    bounties = rank(
        (from_search_item(item) for item in raw),
        stale_days=args.stale_days,
        trusted_only=not args.include_untrusted,
    )

    if args.min_amount:
        bounties = [
            b for b in bounties
            if b.amount_high is not None and b.amount_high >= args.min_amount
        ]
    if not args.all:
        bounties = [b for b in bounties if b.claim != CLAIMED]

    if args.no_state:
        alerts = bounties
    else:
        path = args.state or state_mod.default_state_path()
        previous = state_mod.load(path)
        alerts, next_state = state_mod.diff(bounties, previous)
        state_mod.save(path, next_state)

    if args.json:
        print(notify.render_json(alerts))
    else:
        print(notify.render_text(alerts, show_all=args.all))
        if args.claim_template:
            for bounty in alerts:
                print()
                print(notify.render_claim(bounty))

    if args.webhook and alerts:
        if not notify.post_webhook(args.webhook, alerts):
            print("warning: webhook delivery failed", file=sys.stderr)

    return 0 if alerts else 1
