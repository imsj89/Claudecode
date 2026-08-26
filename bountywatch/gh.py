"""Minimal GitHub issue-search client built on the standard library.

Deliberately dependency-free so the watcher can be dropped into a cron job
without an install step.
"""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request

SEARCH_URL = "https://api.github.com/search/issues"
USER_AGENT = "bountywatch/0.1 (+https://github.com/)"
PER_PAGE = 50


class RateLimited(RuntimeError):
    """Raised when GitHub refuses the request for rate-limit reasons."""

    def __init__(self, message: str, reset_at: int | None = None):
        super().__init__(message)
        self.reset_at = reset_at


class SearchError(RuntimeError):
    pass


def _request(url: str, token: str | None, timeout: int) -> tuple[dict, dict]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": USER_AGENT,
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
            return payload, dict(resp.headers)
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:400]
        reset = exc.headers.get("X-RateLimit-Reset") if exc.headers else None
        remaining = exc.headers.get("X-RateLimit-Remaining") if exc.headers else None
        if exc.code in (403, 429) and remaining == "0":
            raise RateLimited(
                f"GitHub rate limit exhausted: {detail}",
                reset_at=int(reset) if reset and reset.isdigit() else None,
            ) from exc
        raise SearchError(f"HTTP {exc.code} from GitHub search: {detail}") from exc
    except urllib.error.URLError as exc:
        raise SearchError(f"network error contacting GitHub: {exc.reason}") from exc


def search_issues(
    query: str,
    token: str | None = None,
    max_pages: int = 3,
    timeout: int = 20,
    pause: float = 2.0,
) -> list[dict]:
    """Run one issue search, following pagination up to max_pages.

    Unauthenticated search allows only 10 requests/minute, so pages are spaced
    out by `pause` seconds. Supplying a token raises the ceiling to 30/minute
    and is strongly recommended.
    """
    items: list[dict] = []
    for page in range(1, max_pages + 1):
        params = urllib.parse.urlencode(
            {
                "q": query,
                "per_page": PER_PAGE,
                "page": page,
                "sort": "created",
                "order": "desc",
            }
        )
        payload, _ = _request(f"{SEARCH_URL}?{params}", token, timeout)
        batch = payload.get("items") or []
        items.extend(batch)
        if len(batch) < PER_PAGE:
            break
        if page < max_pages:
            time.sleep(pause)
    return items


def token_from_env() -> str | None:
    for name in ("GITHUB_TOKEN", "GH_TOKEN", "BOUNTYWATCH_TOKEN"):
        value = os.environ.get(name)
        if value:
            return value
    return None
