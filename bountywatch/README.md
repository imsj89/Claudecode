# bountywatch

Watches funded open-source bounty boards and tells you the moment something
appears that you can actually claim.

## Why this exists

The Tenstorrent Bounty Program terms contain one clause that determines
everything:

> must be assigned on GitHub to the issue for which you are submitting a pull
> request, and your pull request must be submitted **while you are still
> assigned to the issue**

Payout is gated on *assignment*, not on code quality. A flawless PR from
someone who was never assigned earns **$0**. So the scarce resource is not
engineering skill — it is latency between an issue being posted and someone
claiming it.

A survey on 2026-08-26 found **every open bounty in the Tenstorrent org already
assigned** — org-wide, zero unclaimed. The most tractable one
(`tt-installer#140`, $1,500, explicitly no hardware needed) was posted July 28
and already had two competing PRs. They are not gone because they were hard.
They are gone because someone else was watching.

This tool watches.

## Install

None required. Python 3.9+, standard library only.

```
python3 -m bountywatch --help
```

## Usage

```bash
# First run: everything currently open, ranked
python3 -m bountywatch

# Only four-figure work, with a ready-to-post claim comment
python3 -m bountywatch --min-amount 1000 --claim-template

# Pipe to Slack/Discord from cron
python3 -m bountywatch --webhook "$SLACK_WEBHOOK_URL"

# Offline, against recorded data
python3 -m bountywatch --fixture tests/fixtures/search_sample.json --no-state
```

Set `GITHUB_TOKEN` to lift the search rate limit from 10 to 30 requests per
minute. It works unauthenticated, but will be flaky under load.

Exit codes: `0` alerts found, `1` nothing new, `2` error. The `0`/`1` split is
what makes it useful in cron — you can gate a notification on it.

### Cron

```cron
*/15 * * * * GITHUB_TOKEN=ghp_xxx /usr/bin/python3 -m bountywatch \
  --min-amount 500 --webhook https://hooks.slack.com/services/XXX \
  >> ~/.local/state/bountywatch/log 2>&1
```

Fifteen minutes is a reasonable cadence. The binding constraint is how fast you
can *respond*, not how fast you can detect.

## How it ranks

Claimability first, money second — an $800 issue nobody has taken beats a
$35,000 issue that is already assigned, because only one of them can pay you.

| Band | Meaning |
|---|---|
| `unclaimed` + no hardware needed | Best case. Claim immediately. |
| `unclaimed`, hardware unclear | Read it, then claim. |
| `unclaimed`, needs silicon | Only if you own the hardware. |
| `stale_claim` | Assigned but idle > 14 days. |
| `claimed` | Hidden unless `--all`. |

The `stale_claim` band exists because the terms permit reassignment when an
assignee "becomes unresponsive for over two (2) weeks". That is a legitimate
way into a fully-claimed board — you ask, politely, and the maintainer decides.
`--claim-template` drafts that message; it asks whether work is still active
and offers to stand down, because an idle assignment is the assignee's call
first.

## State

A JSON file (default `~/.local/state/bountywatch/seen.json`) records what has
been reported, so repeat runs stay quiet. It alerts on two events: a **new**
listing, and a **claim-state transition**. The second matters most — an issue
going from `claimed` to `unclaimed` is a bounty being released back into the
pool, which is the single most actionable moment there is.

## Junk filtering

Generic bounty searches are heavily polluted. A search for `"Bounty $" in:title
is:issue is:open` returns ~13,700 results, mostly crypto token claims, scanner
bots filing issues about bounties, and repos offering "$1,000 to calculate the
exact value of PI" that appear built to bait automated agents.

So `--trusted-only` is the **default**: results are restricted to the 17
repositories named in-scope by the program terms. `--include-untrusted` widens
the net; the junk filters still apply.

## Testing

```
python3 -m unittest discover -s tests -v
```

44 tests, no dependencies.

**What is and isn't verified:** all parsing, ranking, junk-filtering, state
and CLI logic is tested against recorded fixtures that mirror real GitHub
payloads. The **live network path is not verified** — it was built in a sandbox
whose proxy hard-scopes `api.github.com`, so `search_issues()` could only be
confirmed to fail *cleanly* (readable error, exit 2, no traceback), not to
succeed. Your first real run is the actual test of that one function.

## Before you rely on this

- The bounty is discretionary. The terms cap Tenstorrent's aggregate liability
  at **$100** and let them suspend payouts at any time. Fine for a $750 fix;
  worth thinking about before sinking weeks into the $35,000 one.
- You warrant that a contribution "is your own work". The terms say nothing
  about AI assistance either way. If that matters to you, ask
  `bounties@tenstorrent.com` — a written answer costs one email.
- Check your employment contract. Eligibility requires you not be bound by
  obligations that prevent participation.
- Exhibit A of the terms defines the payout categories; an issue must carry the
  `bounty` label *and* an Exhibit A category label to qualify.
