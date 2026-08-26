"""Tests for bountywatch. Standard library only: python3 -m unittest discover tests"""

import json
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from bountywatch import state as state_mod
from bountywatch.cli import main
from bountywatch.model import Bounty, from_search_item, parse_amount
from bountywatch.score import (
    CLAIMED, HARDWARE, MIXED, SIM_OK, STALE_CLAIM, UNCLAIMED, UNKNOWN,
    classify, classify_claim, classify_hardware, is_junk, rank,
)

FIXTURE = Path(__file__).parent / "fixtures" / "search_sample.json"
NOW = datetime(2026, 8, 26, 12, 0, 0, tzinfo=timezone.utc)


def load_items():
    with open(FIXTURE, encoding="utf-8") as fh:
        return json.load(fh)["items"]


def bounties():
    return [from_search_item(i) for i in load_items()]


def by_key(ranked):
    return {b.key: b for b in ranked}


class TestParseAmount(unittest.TestCase):
    def test_plain(self):
        self.assertEqual(parse_amount("[Bounty $35000] Welford"), (35000, 35000))

    def test_k_suffix(self):
        self.assertEqual(parse_amount("[Bounty $2.5k] LWT"), (2500, 2500))

    def test_thousands_separator(self):
        self.assertEqual(parse_amount("[Bounty $1,500] sdpa_decode"), (1500, 1500))

    def test_range(self):
        self.assertEqual(parse_amount("[Bounty $500-2500] phi-4"), (500, 2500))

    def test_range_with_en_dash_and_second_dollar(self):
        self.assertEqual(parse_amount("[Bounty $500 – $2.5k] x"), (500, 2500))

    def test_amount_before_word(self):
        self.assertEqual(parse_amount("[$1000 Bounty] GATv2 on PubMed"), (1000, 1000))

    def test_markdown_underscores(self):
        # Search results render the label as [_Bounty_ $1500].
        self.assertEqual(parse_amount("[_Bounty_ $1500] dry-run mode"), (1500, 1500))

    def test_unspecified_amount(self):
        self.assertEqual(parse_amount("[$$ BOUNTY] Add Qwen 1.5"), (None, None))

    def test_no_amount(self):
        self.assertEqual(parse_amount("Fix the flaky test"), (None, None))

    def test_empty(self):
        self.assertEqual(parse_amount(""), (None, None))

    def test_reversed_range_is_normalised(self):
        self.assertEqual(parse_amount("[Bounty $2500-500] x"), (500, 2500))


class TestJunkFilter(unittest.TestCase):
    def test_agent_bait_repo_rejected(self):
        found = [b for b in bounties() if "agent-playground" in b.repo]
        self.assertTrue(found and is_junk(found[0]))

    def test_claim_bookkeeping_rejected(self):
        found = [b for b in bounties() if "rustchain" in b.repo]
        self.assertTrue(found and is_junk(found[0]))

    def test_real_bounty_kept(self):
        real = Bounty(repo="tenstorrent/tt-smi", number=1, title="[Bounty $800] x", url="")
        self.assertFalse(is_junk(real))


class TestHardwareClassification(unittest.TestCase):
    def test_explicit_simulator_wins(self):
        b = Bounty(repo="r", number=1, title="t", url="",
                   body="Validated with ttsim; no hardware required.")
        verdict, evidence = classify_hardware(b)
        self.assertEqual(verdict, SIM_OK)
        self.assertIn("ttsim", evidence)

    def test_chip_name_implies_hardware(self):
        b = Bounty(repo="r", number=1, title="t", url="",
                   body="Benchmark on Wormhole and Blackhole accelerators.")
        self.assertEqual(classify_hardware(b)[0], HARDWARE)

    def test_conflicting_signals_flagged_not_guessed(self):
        b = Bounty(repo="r", number=1, title="t", url="",
                   body="ttsim covers bf16 but device CI is needed for Wormhole fp32.")
        verdict, evidence = classify_hardware(b)
        self.assertEqual(verdict, MIXED)
        self.assertTrue(len(evidence) >= 2)

    def test_silence_is_unknown_not_assumed(self):
        b = Bounty(repo="r", number=1, title="t", url="", body="Refactor the parser.")
        self.assertEqual(classify_hardware(b), (UNKNOWN, ()))


class TestClaimClassification(unittest.TestCase):
    def test_unassigned(self):
        b = Bounty(repo="r", number=1, title="t", url="",
                   updated_at=datetime(2026, 8, 25, tzinfo=timezone.utc))
        self.assertEqual(classify_claim(b, 14, now=NOW)[0], UNCLAIMED)

    def test_fresh_claim(self):
        b = Bounty(repo="r", number=1, title="t", url="", assignees=("a",),
                   updated_at=datetime(2026, 8, 25, tzinfo=timezone.utc))
        self.assertEqual(classify_claim(b, 14, now=NOW)[0], CLAIMED)

    def test_idle_claim_becomes_reassignment_candidate(self):
        b = Bounty(repo="r", number=1, title="t", url="", assignees=("a",),
                   updated_at=datetime(2026, 5, 1, tzinfo=timezone.utc))
        verdict, idle = classify_claim(b, 14, now=NOW)
        self.assertEqual(verdict, STALE_CLAIM)
        self.assertGreater(idle, 100)

    def test_boundary_is_strictly_greater(self):
        # Terms say "over two (2) weeks", so exactly 14 days is not yet stale.
        exactly_14 = datetime(2026, 8, 12, 12, 0, tzinfo=timezone.utc)
        b = Bounty(repo="r", number=1, title="t", url="", assignees=("a",),
                   updated_at=exactly_14)
        self.assertEqual(classify_claim(b, 14, now=NOW)[0], CLAIMED)

    def test_missing_timestamp_does_not_crash(self):
        b = Bounty(repo="r", number=1, title="t", url="", assignees=("a",))
        self.assertEqual(classify_claim(b, 14, now=NOW), (CLAIMED, None))


class TestRanking(unittest.TestCase):
    def setUp(self):
        self.ranked = rank(bounties(), now=NOW)
        self.keys = [b.key for b in self.ranked]

    def test_junk_and_out_of_scope_removed(self):
        self.assertNotIn("xevrion-v2/agent-playground#4", self.keys)
        self.assertNotIn("Scottcjn/rustchain-bounties#16622", self.keys)
        # tt-buda-demos is real but not in the program's in-scope repo list.
        self.assertNotIn("tenstorrent/tt-buda-demos#20", self.keys)

    def test_unclaimed_no_hardware_ranks_first(self):
        self.assertEqual(self.keys[0], "tenstorrent/tt-smi#91")

    def test_unclaimed_beats_bigger_claimed_bounty(self):
        smi = self.keys.index("tenstorrent/tt-smi#91")
        welford = self.keys.index("tenstorrent/tt-metal#54016")
        self.assertLess(smi, welford, "$800 open should outrank $35k taken")

    def test_stale_claim_outranks_fresh_claim(self):
        stale = self.keys.index("tenstorrent/tt-metal#32140")
        fresh = self.keys.index("tenstorrent/tt-metal#52037")
        self.assertLess(stale, fresh)

    def test_stale_reason_cites_terms(self):
        entry = by_key(self.ranked)["tenstorrent/tt-metal#32140"]
        self.assertEqual(entry.claim, STALE_CLAIM)
        self.assertTrue(any("reassignment" in r for r in entry.reasons))

    def test_untrusted_repos_admitted_on_request(self):
        keys = [b.key for b in rank(bounties(), now=NOW, trusted_only=False)]
        self.assertIn("tenstorrent/tt-buda-demos#20", keys)
        # Junk stays out even then.
        self.assertNotIn("xevrion-v2/agent-playground#4", keys)

    def test_range_amount_preserved(self):
        entry = by_key(self.ranked)["tenstorrent/tt-metal#19418"]
        self.assertEqual((entry.amount_low, entry.amount_high), (500, 2500))


class TestFromSearchItem(unittest.TestCase):
    def test_repo_recovered_from_repository_url(self):
        b = from_search_item(load_items()[0])
        self.assertEqual(b.repo, "tenstorrent/tt-smi")

    def test_singular_assignee_field_supported(self):
        b = from_search_item({
            "repository_url": "https://api.github.com/repos/o/r",
            "number": 1, "title": "t", "html_url": "u",
            "assignee": {"login": "solo"}, "assignees": [],
        })
        self.assertEqual(b.assignees, ("solo",))

    def test_missing_fields_tolerated(self):
        b = from_search_item({})
        self.assertEqual(b.repo, "")
        self.assertEqual(b.assignees, ())
        self.assertIsNone(b.created_at)


class TestState(unittest.TestCase):
    def test_first_run_alerts_everything_then_goes_quiet(self):
        ranked = rank(bounties(), now=NOW)
        alerts, next_state = state_mod.diff(ranked, {})
        self.assertEqual(len(alerts), len(ranked))
        self.assertTrue(any("NEW listing" in r for r in alerts[0].reasons))

        again = rank(bounties(), now=NOW)
        alerts2, _ = state_mod.diff(again, next_state)
        self.assertEqual(alerts2, [])

    def test_release_of_a_claim_alerts(self):
        ranked = rank(bounties(), now=NOW)
        _, saved = state_mod.diff(ranked, {})

        freed = bounties()
        for b in freed:
            if b.key == "tenstorrent/tt-metal#54016":
                b.assignees = ()
        alerts, _ = state_mod.diff(rank(freed, now=NOW), saved)
        keys = [a.key for a in alerts]
        self.assertEqual(keys, ["tenstorrent/tt-metal#54016"])
        self.assertTrue(any("claim state changed" in r for r in alerts[0].reasons))

    def test_roundtrip_persists(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "nested" / "seen.json"
            state_mod.save(path, {"a/b#1": {"claim": "unclaimed"}})
            self.assertEqual(state_mod.load(path)["a/b#1"]["claim"], "unclaimed")

    def test_corrupt_state_file_is_survivable(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "seen.json"
            path.write_text("{not json", encoding="utf-8")
            self.assertEqual(state_mod.load(path), {})


class TestCli(unittest.TestCase):
    def test_offline_run_reports_and_exits_zero(self):
        with tempfile.TemporaryDirectory() as tmp:
            code = main([
                "--fixture", str(FIXTURE),
                "--state", str(Path(tmp) / "s.json"),
                "--json",
            ])
            self.assertEqual(code, 0)

    def test_second_run_finds_nothing_new(self):
        with tempfile.TemporaryDirectory() as tmp:
            statefile = str(Path(tmp) / "s.json")
            main(["--fixture", str(FIXTURE), "--state", statefile])
            code = main(["--fixture", str(FIXTURE), "--state", statefile])
            self.assertEqual(code, 1, "no new alerts should exit 1")

    def test_min_amount_filter(self):
        with tempfile.TemporaryDirectory() as tmp:
            code = main([
                "--fixture", str(FIXTURE), "--no-state",
                "--min-amount", "100000", "--json",
            ])
            self.assertEqual(code, 1)

    def test_missing_fixture_is_a_clean_error(self):
        self.assertEqual(main(["--fixture", "/nope/missing.json", "--no-state"]), 2)


if __name__ == "__main__":
    unittest.main()


class TestClaimTemplate(unittest.TestCase):
    def setUp(self):
        from bountywatch import notify
        self.notify = notify
        self.ranked = by_key(rank(bounties(), now=NOW))

    def test_open_bounty_gets_offer_to_stand_down(self):
        text = self.notify.render_claim(self.ranked["tenstorrent/tt-smi#91"])
        self.assertIn("assign it to me", text)
        self.assertIn("I'll drop it", text)

    def test_stale_bounty_asks_the_assignee_first(self):
        entry = self.ranked["tenstorrent/tt-metal#32140"]
        text = self.notify.render_claim(entry)
        self.assertIn("@velonica0", text)
        self.assertIn(f"{entry.idle_days} days", text)
        self.assertIn("still being worked on", text)

    def test_stale_template_never_assumes_abandonment(self):
        text = self.notify.render_claim(self.ranked["tenstorrent/tt-metal#40494"])
        self.assertIn("If it's still active I'll stay clear", text)
