# Generation Log

> One entry per generation run. Records what was submitted, with which seed, so any
> approved image can be reproduced or re-rolled without reconstructing the prompt.
> Media itself is gitignored — it lives in the Higgsfield workspace.

---

## Run 001 — Character sheet (Ashmi Gurung)

**Date:** 2026-08-25 · **Prompt:** `prompts/01-character-sheet.md` (verbatim, unmodified)
**Pipeline step:** 1 of 5 (CHARACTER-BIBLE §6) · **Status:** awaiting face approval

| Setting | Value |
|---|---|
| Model | `soul_2` (`text2image_soul_v2`) |
| Aspect / output | 16:9 → 2048×1152 |
| Style | `General` (`3db34ab5-3439-4317-9e03-08dc30852e69`), default strength |
| Quality | `1080p` (server default for the model) |
| Prompt enhance | off — the prompt is hand-built to the slot architecture and must not be rewritten |
| Variants | 2, same prompt and settings, different seed |

| Variant | Job ID | Seed |
|---|---|---|
| A | `198436c4-3b28-4b79-a930-d836c607612b` | 391970 |
| B | `c5d379f3-ed27-4429-88c7-bb1cf8df8674` | 138621 |

**Note on `enhance_prompt`.** It came back `false`, which is what we want. The prompt is
assembled to the `character-sheet` slot architecture and its ordering is load-bearing —
composition and identity tokens are first because early tokens carry more weight. If a
future run shows `enhance_prompt: true`, the model rewrote the prompt and the result is
not a faithful test of the bible.

### Verification status — NOT yet graded

The five checks in `prompts/01-character-sheet.md` (heritage read, age read, skin,
panel consistency, framing) require **human review of the pixels** and have not been
performed. The session that generated these could not fetch the image bytes; see the
egress note in PROJECT-BRIEF §2. Checks 1 and 2 are hard-fail gates — nothing downstream
should be built until someone has actually looked.

Record the verdict here when reviewed, then proceed to the Reference Element
(CHARACTER-BIBLE §6, step 2) or re-roll using the iteration levers in the prompt file.
