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

### Verdict — CANDIDATE, not selected

Reviewed 2026-08-25. The right-hand close-up panel of variant A is the **leading
candidate**, saved as Element `ashmi-gurung-face-v1` (run 005) so it survives the session.
**No face has been selected yet** and none should be treated as final until it is.

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
  PROJECT-BRIEF §4 names as the project's core technical risk. Flagged and still **open**
  — it matters because CHARACTER-BIBLE §1 makes the Gurung surname load-bearing on the
  face agreeing with it. Worth resolving while faces are still being chosen; it is far
  cheaper now than after a Soul is trained.


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

**This element preserves a candidate, it does not select one.** Face selection is still
open. If a different candidate wins, create a new element and retire this one.

---

## Run 006 — ten face candidates

**Date:** 2026-08-25 · **Model:** `soul_2` · **Aspect:** 9:16 · **Text-only**

Ten near-neighbours of the run 001 variant A face, for selection. Text-only deliberately:
a reference image would force `enhance_prompt` and strip the realism engine (runs 002–004).
Similarity therefore comes from a tightened written description of the candidate face, with
exactly **one feature perturbed per variant** so the axes stay separable.

| # | Job | Perturbation |
|---|---|---|
| 1 | `195be596-bf84-448e-aef8-761251ca8e92` | baseline |
| 2 | `ebe6e8ec-57bb-4682-8890-34325e6005ab` | lighter complexion |
| 3 | `f4fb78e0-2ffd-48f9-918d-8153b6760a16` | fuller apple cheeks |
| 4 | `77a866c9-4e21-4271-9253-c1ca0224c69a` | larger, more open eyes |
| 5 | `db59a8bb-2817-411c-b2fc-a05124974d71` | lower nasal bridge, stronger epicanthic fold |
| 6 | `662684da-81be-4350-8430-b75a6c76b740` | sharper jaw, more sculpted |
| 7 | `991e42ce-4cb1-47f8-ba0e-b191d6d2d77b` | fuller petal lips (resubmitted; `b1916083` failed) |
| 8 | `d5c476de-3d29-489f-8f41-d6fc7c97f4aa` | deeper, warmer tone |
| 9 | `ca53d038-9646-47f9-97a5-e2aa4ffa6897` | softer, more arched brows |
| 10 | `6adcc63f-debd-4841-a698-9e9278ad4bc1` | rounder, fuller face shape (resubmitted; `cabae37f` failed) |

Variant 5 is the one that tests the PROJECT-BRIEF §4 heritage risk directly.

Two of the twelve submissions failed with no error detail and were resubmitted
unchanged; both succeeded on the retry. Batch submission on `soul_2` is not fully
reliable — always check `failed_count` rather than assuming a submitted batch completes.

**Review notes on the set:**

- **Realism engine: held on all ten.** Matte skin, visible pores, natural asymmetry, no
  gloss. This is the direct payoff of going text-only and confirms the run 002–004
  diagnosis — the reference image, not the prompt, was what broke the grade.
- **Age: passed on all ten.** No babyface drift anywhere.
- **Pendant: rendered correctly on nearly all** — coral centre inside a turquoise ring.
  The identity anchor is reproducible from text alone, which matters for the training set.
- **Heritage: still unresolved across the whole set.** Every variant reads broadly South
  Asian / North Indian. Variant 5, which was built specifically to push Tibeto-Burman
  (lower nasal bridge, stronger epicanthic fold, broader cheekbones), moved the least of
  any perturbation. Prompt-level heritage steering appears weak on `soul_2` at this
  strength. If the Himalayan read matters, it likely needs the stronger levers in
  `prompts/01-character-sheet.md` or a different base model — not another round of the
  same wording.

---

## Run 007 — beauty-forward face candidates

**Date:** 2026-08-25 · **Model:** `soul_2` · **Aspect:** 9:16 · **Text-only**

Run 006 was rejected: the faces were not attractive enough. **Diagnosis: the §5 realism
engine was suppressing beauty.** Clauses like `uneven foundation blending`, `fine lines`,
`texture irregularities` and `unretouched documentary realism` are tuned for authenticity
and actively work against a pretty face. Run 006 also anchored on replicating the run 001
candidate's specific features — deep-set downturned eyes, low heavy brows, lean cheeks —
which read as characterful rather than beautiful.

**The distinction that resolves it:** CHARACTER-BIBLE §5's un-glamorous grade governs
**posted content** — the bad phone photo in a Medford kitchen. The **character sheet** is a
studio reference whose job is to define the face clearly, and there is no reason for it to
be unflattering. Beauty comes from bone structure and feature harmony, not from
airbrushing, so real skin texture and a genuinely attractive face are compatible.

Rewritten toward: model-caliber facial harmony, high sculpted cheekbones, large luminous
almond eyes with an **upward** outer tilt (downturned reads plainer), refined nose, full
lips with a defined cupid's bow, soft flattering key light. Retained: fine visible pores,
subtle natural asymmetry, `no plastic skin`, `no waxy skin`, and the mid-twenties guardrail.

| # | Job | Direction |
|---|---|---|
| 1 | `13273ee8-7191-4a99-8f9c-ae2c177c976a` | balanced |
| 2 | `64cf20cd-f742-4285-aa6c-0e41280c1e39` | Himalayan / Tibeto-Burman |
| 3 | `452540d1-b428-45b1-8407-705b9e111769` | soft romantic |
| 4 | `5f16fac6-6185-4b6b-ad17-927e8980f5f6` | sharp editorial |
| 5 | `2f699a0a-071a-4974-95b6-c1d3bf86a32d` | delicate / fair |
| 6 | `16b2045b-7482-47f2-8e78-437c5912e5a3` | eyes-forward |
| 7 | `b05ba74e-1445-4884-88ff-8517603441fa` | lips + eyes |
| 8 | `30e7617c-f323-4f6e-80a8-fc35fbb80791` | classic symmetrical |
| 9 | `2b47b38c-b0f9-4391-a1f8-6100862e9329` | soft glam |
| 10 | `eb066f73-d80d-4559-ae9a-f03a28f23831` | fresh natural |

### Two defects in the set

**Spurious inset thumbnails on 3, 4, 6, 7 and 10.** A small duplicate figure or a product
shot of the sweater appears in a corner, despite `no inset figure`, `no duplicate figures`
and `single subject only` in the negative tail. This is the same composition failure that
put a doll-sized figure in the middle of the run 001 sheet. **`soul_2` does not reliably
honour single-subject negatives.** Clean: 1, 2, 5, 8, 9. If a defective one is chosen,
re-roll it rather than cropping — the inset signals the composition was unstable.

**Glossier than bible §5 permits.** Deliberate: the anti-gloss clauses were relaxed to let
the beauty lighting work. Fine for face selection, wrong for posted content. Once a face is
chosen, re-derive it under the §5 content grade before shooting the training set, or every
downstream post inherits a beauty-ad finish.

### Plan limit discovered

`max 8 concurrent jobs on ultimate (annual) plan`. Submitting 10 at once silently drops the
overflow — this is what the two unexplained "failures" in run 006 actually were, not model
errors. **Submit in batches of 8 or fewer**, and always check `failed_count`.

---

## Runs 008–009 — no-makeup direction, and two solved problems

**Date:** 2026-08-25 · **Model:** `soul_2` · **Aspect:** 9:16 · **Text-only**

Direction changed to: no makeup, naturally beautiful, fair skin, hazel green eyes.
Run 009 refined toward the preferred candidate (run 008 #8: bare face, fair skin, visible
freckles, thick natural brows, hazel green eyes, fresh expression).

### SOLVED: the inset-thumbnail defect

Negative-listing (`no inset image`, `no thumbnail`, `no collage`) **did not work** and may
have made it worse — naming an object in a negative can summon it. Replacing that with a
**positive framing instruction** fixed it completely:

> `A single full-bleed vertical photograph filling the entire frame edge to edge`

Run 008: 5 of 8 defective. Run 009 with the positive framing: **0 of 8 defective.**
Use the positive form in every future prompt; do not rely on single-subject negatives.

### CONFIRMED: fair skin + hazel green eyes overrides heritage

Run 009 tested this deliberately. Variants 6, 7 and 8 **front-loaded** the heritage terms
into the opening clause — `young Nepali woman of Himalayan Gurung heritage, Tibeto-Burman
facial structure, broad high cheekbones, low nasal bridge, pronounced epicanthic fold` —
the strongest position in the prompt, where tokens carry the most weight.

**It barely moved the result.** All three still read European or Mediterranean. Combined
with run 006 (where clinical heritage wording also failed) and run 007 (where the same
terms *did* work under a warmer skin tone), the conclusion is specific:

> Skin tone and eye colour dominate the perceived-heritage read on `soul_2`. Once fair skin
> and hazel-green eyes are specified, no amount of bone-structure language recovers a
> Himalayan read — not even from the front of the prompt.

This is not a prompt-engineering problem with a remaining fix. It is a genuine either/or:
the fair-and-hazel aesthetic, or a face that reads Nepali. PROJECT-BRIEF §4 stakes the
account's moat on the latter, so this is a strategic decision, not a technical one, and it
should be recorded as such when it is made.

### WATCH: the no-makeup direction reads younger

Bare face + freckles + fresh expression pushes apparent age down. Several run 009 variants
read early-twenties rather than mid-twenties. Still adult, so not a breach — but
PROJECT-BRIEF §7 requires **unambiguous** mid-twenties, and this direction erodes the
margin. Any face chosen from here needs an explicit age push (`27 years old, defined mature
jawline, longer facial thirds`) before it becomes the Element.

**Run 009 jobs:** 1 `9f65b8dc` · 2 `30ee78c3` · 3 `105e5ad7` · 4 `9d05e134` · 5 `52fc5942`
· 6 `917932c2` · 7 `e6571e06` · 8 `89679ddb` (6–8 = heritage front-loaded)

---

## Run 010 — hard beauty push, and a model comparison

**Date:** 2026-08-25 · **Aspect:** 9:16 · Text-only · 1–6 `soul_2`, 7–8 `seedream_v4_5`

Run 009 was still rejected as not attractive enough. **Diagnosis: dilution, plus wording
that actively read as plain.** The prompts had grown to ~40 comma-separated clauses, so no
single attribute carried weight, and three specific phrases were working against beauty:

| Phrase | Reads as |
|---|---|
| `natural untouched eyebrows, softly uneven` | unkempt, not groomed |
| dense freckles across nose *and cheeks* | rustic / girl-next-door |
| flat even lighting | passport photo, no dimension |

**What fixed it:**

1. **Shorter, higher-signal prompts.** Written as sentences rather than a clause pile.
2. **Superlative beauty language up front** — `breathtakingly beautiful`, `stunning
   supermodel-level facial beauty`, `flawless facial harmony and ideal balanced proportions`.
3. **The reframe that carried the most weight:** `the kind of face that needs no makeup`.
   This keeps the bare-face requirement while removing the plainness the earlier phrasing
   implied — "no makeup" had been read as "unremarkable" rather than "needs none".
4. **Groomed but natural brows**, freckles reduced to the nose only, and **flattering light
   with dimension** (subtle shadow under the cheekbones) instead of flat fill.
5. **Explicit age push** — `twenty-six years old, mature adult facial proportions, longer
   facial thirds` — which also repaired the age erosion flagged in run 009.

### Model comparison

`seedream_v4_5` (7, 8) renders more polished and more conventionally striking, but:

- **It ignores `no cosmetics`** — both outputs show defined liner and worked lids.
- **It reads retouched**, closer to a commercial beauty ad than a photograph, which is the
  opposite of the CHARACTER-BIBLE §5 direction for content.
- **Pipeline cost:** Seedream is Element-compatible but **not** Soul-compatible. A face
  chosen here cannot be used for `show_characters action=train`, so the whole identity
  pipeline would have to run through Elements on Element-compatible models, and `soul_2`
  stills would be off the table.

`soul_2` (1–6) stays more photographic and honours the bare-face instruction. **Recommend
staying on `soul_2`** unless the Seedream look is decisively preferred, and if so, decide
the pipeline consequence deliberately rather than by drift.

### Defects

- **4** — nostril/nose anatomy is subtly wrong; re-roll if chosen.
- **5** — an orange lighting cast across the forehead; a lighting artifact, re-roll if chosen.
- **Insets: 0 of 8.** The full-bleed positive framing continues to hold across both models.

**Jobs:** 1 `55f1e28f` · 2 `d7926480` · 3 `0fc28d26` · 4 `0ce92043` · 5 `cb561aeb`
· 6 `5dbf4044` · 7 `a6fe9f4e` (seedream) · 8 `4e0ef522` (seedream)

---

## Run 011 — grey eyes + pinker lips, and the identity problem is SOLVED

**Date:** 2026-08-25 · **Aspect:** 9:16 · 1–4 `soul_2` text-only, 5–6 Element on
`nano_banana_pro`, 7–8 Element on `seedream_v4_5`

Requested changes to the run 001 candidate face: **light grey eyes, pinker lips.**
Everything else held.

### Correction to the run 002–004 conclusion

Earlier this session the log recorded that *"prompt fidelity and identity anchoring cannot
be had at the same time on `soul_2`."* That was correct **only for raw reference images on
`soul_2`**, and stating it as a general rule was too broad. This run tested the Element
path properly and it works:

> **Embedding `<<<element_id>>>` in the prompt preserves the face faithfully AND honours the
> full prompt. No `enhance_prompt` rewrite occurs.**

Variants 5–8 hold her bone structure, nose, lip shape, hair, the coral-and-turquoise
pendant and the sweater collar, while applying both requested changes. Variants 1–4,
text-only on `soul_2`, produced the right *family* of face but plainly a different woman —
confirming that a written description cannot substitute for identity injection.

**This is the mechanism to use for all future face iteration.** Do not iterate faces with
text descriptions, and never with a raw reference image on `soul_2`.

### Consequence for the pipeline

The Element path runs on Element-compatible models only, so `soul_2` cannot be used for
iterating this face. That is not a blocker — CHARACTER-BIBLE §6 already routes the training
set through the Element — but it does mean the **face-selection and refinement stage now
lives on `nano_banana_pro` / `seedream_v4_5`**, and only the final trained Soul returns to
`soul_2`.

### Observations

- **5 and 6** (`nano_banana_pro`) are the most photographic and the closest to her. Note the
  server reports these as `nano_banana_2` — the request was routed to a sibling model.
- **7 and 8** (`seedream_v4_5`) hold identity equally well but run warmer, more saturated
  and glossier, consistent with the run 010 finding.
- **Grey eyes read as coloured contacts on several**, most visibly 2, 3 and 4: pale grey
  against deep warm-tan skin is a high-contrast combination the model renders as an overlay.
  5 is the most convincing. If grey is kept, the anti-contact-lens clause needs strengthening,
  or a warmer grey-hazel would sit more naturally on this complexion.
- **4 overshot the lip change** — reads as applied red lipstick rather than a natural pinker
  lip, which also breaks the no-makeup direction.
- Insets: 0 of 8. Full-bleed framing still holding across three models.

**Jobs:** 1 `563ec34e` · 2 `4b0dfb1b` · 3 `bed3a02c` · 4 `1999e137` · 5 `920b1c12`
· 6 `0b346b71` · 7 `d28972b5` · 8 `0ef4dc69`


---

## FACE LOCKED — 2026-08-25

**Element `ashmi-gurung-FINAL` — `f6328436-b87a-41b1-87c0-809fc0f72cb8`**

Selected: **run 011 variant 8** (job `0ef4dc69-eb73-44dd-b00b-b7c4c75b4e45`), Element-guided
on `seedream_v4_5`. Source media `96523ded-d081-465f-a8b8-1f01e8ec90d9`.

Eleven runs, ~60 candidates. The path that worked, in order:

1. **Run 001** produced the base face text-only, and it survived every later comparison —
   the user returned to it three separate times after exploring other directions.
2. **Runs 002–004** failed trying to edit it with a raw reference image on `soul_2`.
3. **Runs 006–010** explored alternatives (near-neighbours, beauty-forward, no-makeup,
   fair/hazel). All rejected, but they produced the prompt-craft findings — dilution,
   the plainness phrases, the full-bleed framing fix.
4. **Run 011** applied the final edits through the **Element**, which preserved identity and
   honoured the prompt at the same time. That was the mechanism the whole session needed.

### Accepted departures from the original brief

Recorded so a later session does not "fix" them:

| Field | Bible original | Locked | Status |
|---|---|---|---|
| Eyes | dark brown | **light grey** | chosen |
| Lips | rosy-brown | **soft rose-pink** | chosen |
| Heritage read | Himalayan/Tibeto-Burman | reads South Asian, not distinctly Himalayan | known, accepted |

The heritage point still carries the PROJECT-BRIEF §4 consequence — the Gurung surname and
the Nepali content voice now rest on a face that does not visibly signal Himalayan ancestry.
Accepted deliberately, after being flagged before selection.

### Corrections to earlier entries in this log

- **Runs 002–004 conclusion was too broad.** "Prompt fidelity and identity anchoring cannot
  be had at the same time" is true only of raw reference images on `soul_2`. The Element path
  does both. See run 011.
- **Run 010's Seedream warning was overstated.** Choosing a Seedream-rendered face does *not*
  take `soul_2` off the table. Soul training consumes images regardless of which model made
  them, so the chain Element → training set → Soul → `soul_2` still closes.

### Next

1. **Settle body type, bust and hips** — blocks everything below.
2. Generate 15–20 varied shots via `<<<f6328436-b87a-41b1-87c0-809fc0f72cb8>>>`, deliberately
   varying angle, expression, distance and light (CHARACTER-BIBLE §6 step 3 is where projects
   fail).
3. **Re-derive under the §5 content grade before shooting that set.** The locked face was
   selected under flattering beauty light; the posted-content grade is the opposite. If the
   training set inherits the beauty-ad finish, every post does.
4. `show_characters action=train` → Soul → production on `soul_2`.

---

## Runs 012–013 — body type selection

**Date:** 2026-08-25 · **Aspect:** 9:16 · Element `f6328436-b87a-41b1-87c0-809fc0f72cb8`

Six builds per run, identical pose, wardrobe, framing and lighting so build is the only
variable. Fitted athletic wear rather than swimwear — it reads proportions just as clearly
and keeps the sheet advertiser-safe per PROJECT-BRIEF §1 and §3.

### The Element works for full-body, not just close-ups

Her face carried onto full-length shots across all twelve images. This is what the training
set depends on, and it is now demonstrated rather than assumed.

### `nano_banana_pro` has almost no body-type range (run 012)

Six builds spanning petite-slim 5'2" to full-hourglass 5'5" to tall-lean 5'8" came back
nearly identical. The model has a strong prior toward slim-model proportions and flattened
the build language into it — the same failure mode as the heritage terms in runs 006/009:
**descriptive attributes lose to model defaults.**

### `seedream_v4_5` has wide body-type range (run 013)

The same experiment on Seedream produced a genuine spread from restrained to very full.
Two things changed together, so both are worth carrying forward:

1. **The model.** Seedream is the one to use for anything where body proportions matter.
2. **Comparative rather than absolute language.** `hips visibly wider than her shoulders`,
   `waist distinctly narrower than both her bust and her hips`, `waist-to-hip ratio around
   0.7` — relative statements survive where adjectives get averaged away. This is the same
   lesson as run 010's dilution finding, applied to anatomy.

### Note on the reference images

Body direction was requested by pointing at screenshots of a real, identifiable person's
Instagram with the ask to reproduce her exact proportions. **Declined** — PROJECT-BRIEF §7
prohibits reproducing an identifiable individual's likeness, and a persona traceable to a
real person is precisely the risk the brand-deal strategy cannot carry. Replaced with named
generic archetypes chosen from a comparison sheet, which reached the same destination
without cloning anyone.

**Run 012 jobs (nano):** 1 `c3ed792c` · 2 `af145c28` · 3 `da6dba5f` · 4 `00dd7961`
· 5 `7bf44ac3` · 6 `48ffa4e3`
**Run 013 jobs (seedream):** 1 `87bec4de` · 2 `b3a3eb2b` · 3 `34f83ab1` · 4 `cd388c29`
· 5 `743b8548` · 6 `001e0268`

**Status: awaiting build selection.** Nothing written to CHARACTER-BIBLE §2 until chosen.

---

## BUILD LOCKED — 2026-08-25

**167 cm · 95 cm bust / 62 cm waist / 100 cm hips · full bottom-leaning hourglass**
Waist-to-hip ~0.62 · bust-to-waist ~1.5 · shoulders narrower than hips · legs slightly
longer than half total height. Written into CHARACTER-BIBLE §2.

Selected as "A" from an escalation ladder, then verified across five angles — front,
three-quarter, profile, signature sweater-and-jeans fit, and jeans at three-quarter. The
silhouette and the locked face both held in all five, which is the check that matters
before a training set.

### How the spec was arrived at

1. A ratio table was supplied (84–87 / 60–63 / 89–94 at 167 cm, WHR 0.66–0.71). Rendered
   faithfully — but **that spec is a slim hourglass**, around a US 2–4, and read leaner than
   the "fuller bust, curvy waist, fuller hips" direction given moments earlier. Ratios and
   absolute circumference do different jobs: 0.67 WHR is genuinely curvy *as a ratio* while
   the circumferences stay small. Flagged rather than silently resolved.
2. The follow-up — "bust ×2, hips ×1.5" — is not renderable taken literally: 85 × 2 = 170 cm
   bust on a 167 cm frame is roughly her own height. Rather than guess, an escalation ladder
   was generated with explicit numbers at each rung (A 95/62/100, B 102/62/105,
   C 109/61/106, where C doubles the bust-to-waist *difference*). A was chosen.

**Lesson worth keeping:** when a numeric instruction is impossible or ambiguous, render a
labelled ladder rather than picking an interpretation silently. It resolved in one round
what a clarifying question would have taken several messages to settle.

### Anatomical-stability note

A was also the right call on durability. Past roughly B, the waist-to-bust contrast exceeds
what stays stable across many generations — expect ribcage and shoulder-line drift as pose
varies, and worse in video. The training set locks whatever is chosen into every future
image, so stability compounds.

**Jobs:** front `b5c73111` · three-quarter `1f9ecf8e` · profile `5e05599a` ·
signature fit `531c8fad` · jeans 3/4 `1e0f9da5`
Ladder: A `b5c73111` · B `37f89c31` · C `5c42e5bd` · B 3/4 `7d7c0be4`

---

## Both gates are now clear

Face and build are locked. CHARACTER-BIBLE §6 step 3 is unblocked.

**Before shooting the training set, re-derive under the §5 content grade.** Every image so
far was made under flat or flattering studio light. The posted-content grade is the
opposite — harsh hospital fluorescent, blue-hour grain, uneven kitchen tungsten, flat Boston
overcast. A training set shot in studio light produces a Soul that renders studio light,
and every post inherits a beauty-ad finish, which is the exact AI tell §5 exists to prevent.

Then: 15–20 varied shots via the Element (vary angle, expression, distance, light) →
`show_characters action=train` → Soul → production on `soul_2`.

---

## BUILD SPEC AMENDED — E cup

**Final: 167 cm · 104 cm bust / 62 cm waist / 100 cm hips · 78 cm underbust (~E cup)**

Verified across front, three-quarter, profile, signature sweater-and-jeans, and jeans at
three-quarter. Silhouette and face both held in all five.

### The instruction that actually worked

"Enlarge the bust by 2×" was first read as circumference — 95 → 190 cm, not renderable on a
167 cm frame. Laddering by circumference (105 / 115 / 125) also failed, for a second reason:
**the model treats a larger bust as a larger woman** and inflated hips, thighs and arms even
though those numbers were held constant in the prompt.

The clarification — double the **cup volume**, not the circumference — is the correct
anatomical reading, and it only rendered properly once the prompt **named the held
variables**:

> give the slim frame first (waist, hips, underbust, ribcage, shoulders, arms, thighs), then
> the bust, then restate that everything else stays slim and that **she is not a heavier
> woman overall**

That last clause is what stops the whole-figure drift. Generalises: on these models,
isolating one attribute requires explicitly pinning the ones that must not move.

### Also learned

- **The model stops tracking numbers past a ceiling.** 115 and 125 cm bust rendered nearly
  identically, and 125 ignored its stated ratio. Past roughly 115 the model returns its own
  maximum rather than the request — more circumference will not go further.
- **Front-on framing hides bust volume.** A fitted tank flattens it; three-quarter and
  profile are the honest reads. Judge chest specs off those angles.
- **Under her signature oversized cable-knit the bust spec is nearly invisible.** Since
  pillars 1 and 4 put her in scrubs and winter layers for most posts, this spec will only
  visibly affect a minority of output.

**Jobs:** front `c581d077` · three-quarter `6f69337a` · profile `82cc9fab` ·
signature fit `f8ece926` · jeans 3/4 `8310be59`
Rejected: G cup `af219354` / `be37b482` / `a6516624` / `c67bcef1`
