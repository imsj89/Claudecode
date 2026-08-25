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

### Verdict — APPROVED (variant A, right panel)

**The face is locked.** Reviewed 2026-08-25. The right-hand close-up panel of variant A
is the approved face; it is now Element `ashmi-gurung-face-v1` (see run 005).

Observations on the approved image, for the record:

- **Skin and realism: passed.** Genuine pores, uneven tone, natural asymmetry, matte
  finish, correct hands. The anti-airbrush engine took.
- **Age: passed.** Reads unambiguously mid-twenties, no babyface drift.
- **Pendant: rendered correctly** — coral centre, turquoise outer ring. The identity
  anchor works as specified.
- **Framing: failed, but harmlessly.** The left panel rendered as a tiny inset figure
  rather than a head-to-toe full body, and both close-ups dominate the frame. Only the
  right panel was needed, so this did not block approval — but the split-screen
  composition is not reliable on `soul_2` and should not be trusted for a real turnaround.
- **Heritage: drifted toward generic North Indian.** High nose bridge, no visible
  epicanthic fold, cheekbones not Himalayan-broad. This is the exact failure mode
  PROJECT-BRIEF §4 names as the project's core technical risk. **Accepted by explicit
  decision** — the face was chosen on its merits with the drift flagged. Logged here
  because CHARACTER-BIBLE §1 makes the Gurung surname load-bearing on the face agreeing
  with it, and that tension is now a known, owned trade rather than an accident.


---

## Runs 002–004 — face iteration (all rejected)

Three attempts to modify the approved face: lighter skin, more defined features, eyes as
the strongest feature, petal-shaped lips, fuller cheeks. All rejected; the original face
was kept unchanged. Recorded because the **failure mode is reusable knowledge**.

| Run | Job | Seed | Method | Outcome |
|---|---|---|---|---|
| 002 | `43ff4b1b-fa30-4cae-8a68-933ca21c1f61` | 788911 | text-only, 9:16 | Fresh face, not an edit of the approved one |
| 003 | `a234250d-c485-467a-8d69-c6d34c4810c0` | 796653 | reference image + prompt | Glossy skin, pendant drift, no skin lightening |
| 004 | `aff12fc4-0da8-4554-88a1-c1cb37e6a113` | 263546 | same, `enhance_prompt:false` attempted | Matte recovered, eyes regressed, hair went curly |

### The finding that matters: `enhance_prompt` cannot be disabled on `soul_2`

**Attaching a reference image to `soul_2` forces `enhance_prompt: true`.** The server
discards the submitted prompt and replaces it with its own caption of the reference image.
Run 003's stored prompt reads *"dewy tan skin... warm, healthy glow"* and *"model-like...
symmetrical structure"* — the precise inverse of the locked realism engine in
CHARACTER-BIBLE §5, which is why the skin came back glossy.

Passing `enhance_prompt: false` does not work. The MCP layer rejects it:

```
params.enhance_prompt: requested false → used "omitted"
reason: "Higgsfield Soul 2.0 does not support this parameter"
```

and the completed job still reports `enhance_prompt: true`.

**Consequences for the pipeline:**

1. A text-only `soul_2` call keeps `enhance_prompt: false` and honours the full prompt.
   Run 001 confirms this. Prompt fidelity and identity anchoring are mutually exclusive
   on this path.
2. Do not iterate on a face by feeding back a reference image. Every locked clause —
   realism, heritage, wardrobe, distinguishing marks — is summarised away, differently
   each time, so the same defects recur and re-fixing them costs credits per roll.
3. Identity persistence must come from the native mechanisms (Element, then Soul), not
   from raw reference images. See CHARACTER-BIBLE §6.

Some prompt signal does survive into the caption — run 004's rewrite did pick up "matte",
which cleared the gloss — but it is lossy and non-deterministic. Do not rely on it.

---

## Run 005 — Reference Element (identity lock)

**Date:** 2026-08-25 · **Pipeline step:** 2 of 5 · **Status:** done

The approved right panel of run 001 variant A was cropped (x 1060–2048 of 2048×1152),
uploaded, and registered as a reference element.

| Field | Value |
|---|---|
| Element name | `ashmi-gurung-face-v1` |
| Element ID | `05a710b3-dba8-4f4e-9893-5c75c0cad576` |
| Source media ID | `421c9aaf-e455-40db-ac52-0d39ecdac629` |
| Category | `character` · **Status** `completed` |

Usage: embed `<<<05a710b3-dba8-4f4e-9893-5c75c0cad576>>>` inside the prompt of
`generate_image` / `generate_video`. The backend injects the reference automatically.

**Next:** 15–20 varied shots via the Element (vary angle, expression, distance, light),
then `show_characters action=train` on that set. Body type is still unspecified and must
be settled before the training set is shot — the training set fixes the body as well as
the face.
