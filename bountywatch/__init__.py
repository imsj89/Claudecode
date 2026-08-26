"""bountywatch - watch funded open-source bounty boards for claimable work.

Built around one fact about the Tenstorrent bounty program: payout requires
being *assigned* to the issue before submitting a PR. A perfect patch from an
unassigned contributor earns nothing. So the scarce resource is not engineering
skill, it is latency between an issue appearing and someone claiming it.

This package watches for that moment.
"""

__version__ = "0.1.0"
