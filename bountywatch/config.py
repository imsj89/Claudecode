"""Static configuration: in-scope repos, search queries, and junk filters."""

# The 17 repositories named as in-scope by the Tenstorrent Bounty Program
# Terms and Conditions. A contribution only qualifies for payout if it lands
# in one of these AND the issue carries the "bounty" label plus an Exhibit A
# category label.
TENSTORRENT_IN_SCOPE = (
    "tt-metal",
    "tt-mlir",
    "tt-forge",
    "tt-tools-common",
    "tt-smi",
    "tt-topology",
    "luwen",
    "tt-flash",
    "tt-kmd",
    "tt-llk",
    "tt-installer",
    "tt-forge-fe",
    "tt-blacksmith",
    "model-explorer",
    "tt-xla",
    "pytorch2.0_ttnn",
    "tt-lang",
)

TRUSTED_REPOS = frozenset(
    f"tenstorrent/{name}" for name in TENSTORRENT_IN_SCOPE
)

# Search queries run against GitHub's issue search. Tenstorrent tags some
# issues with a `bounty` label and encodes the amount in the title on others,
# so both shapes are needed. Results are de-duplicated by issue URL.
DEFAULT_QUERIES = (
    "org:tenstorrent label:bounty is:issue is:open",
    'org:tenstorrent "Bounty $" in:title is:issue is:open',
)

# Repositories observed serving fake or non-cash "bounties" while polluting
# generic bounty searches. Several appear purpose-built to bait automated
# agents into wasting cycles. Matched as case-insensitive substrings against
# the repo's full name.
JUNK_REPO_MARKERS = (
    "agent-playground",
    "oss-hunter",
    "bountyscout",
    "bounty-scout",
    "rustchain-bounties",
    "devpool-directory",
    "bottube",
)

# Title shapes that indicate bookkeeping noise rather than fundable work.
JUNK_TITLE_MARKERS = (
    "bounty claim:",
    "bounty alert:",
    "bounty post",
    "new opportunities found",
)

# Hardware that must be physically present to validate a change. Tenstorrent
# silicon generations and dev systems.
HARDWARE_MARKERS = (
    "wormhole",
    "blackhole",
    "grayskull",
    "n150",
    "n300",
    "t3k",
    "p300",
    "galaxy",
    "quietbox",
    "loudbox",
    "device ci",
    "on silicon",
    "physical hardware",
    "requires hardware",
)

# Phrases that positively indicate the work can be validated without silicon.
# These are deliberately specific: a passing mention of "simulator" is weak
# evidence, an explicit "does not require hardware" is strong.
SIMULATOR_MARKERS = (
    "ttsim",
    "do not require tenstorrent hardware",
    "does not require tenstorrent hardware",
    "no tenstorrent hardware",
    "without tenstorrent hardware",
    "no hardware required",
    "simulator is sufficient",
    "functional simulator",
)

# Default number of days of inactivity after which an assigned issue is
# treated as a reassignment candidate. The Tenstorrent terms permit
# reassignment when an assignee is "unresponsive for over two (2) weeks".
DEFAULT_STALE_DAYS = 14
