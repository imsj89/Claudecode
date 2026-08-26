# Prompt 04 — Skin texture (edit pass)

**Type:** image edit · **Model:** `nano_banana_pro`, image only, no character references.
**Input:** the approved crowd frame — the one with plastic skin, the correct mole above her
eyebrow and no extra marks. Not the over-textured output.

---

## A3 — the prompt to run (2874 characters)

```
Add photographic micro-detail to her skin. Everything already in the photograph stays exactly as it is, pixel for pixel — her face, her expression, her colouring, her hair, her clothes, the crop, the light and the background. Keep the small dark mole above her eyebrow on the right of the image, the mark on her chest and the mark on her upper arm.

Work at the millimetre scale only. Two things stay true throughout: her skin stays clear and even in tone, carrying only the marks it already has, and the only creasing anywhere on her face is the soft folding her expression is making in this moment. Her skin is the smooth young skin of a 25-year-old that simply has visible pores.

PORE STRUCTURE: give the skin real pores with real anatomy. Each pore is a tiny pit with a soft shadowed centre and a faintly raised rim catching light, not a printed dot. Largest and slightly open across the nose, the sides of the nose and the nose bridge. Smaller and denser on the inner cheeks beside the nose. Fine and shallow across the forehead. Sparse and barely there on the outer cheeks toward the jaw. Pores are confined to those areas alone.

SURFACE TOOTH: between the pores, the faint orange-peel quality of real skin — a barely perceptible roughness in the surface itself, strongest across the forehead and the bridge of the nose. It reads as a fine tooth at the very limit of what the sensor resolves, the way skin looks rather than plastic.

VELLUS HAIR: fine, short, pale hairs across her cheeks, jawline, temples and in front of her ears, most lying flat against the skin. Where the sun rims her jaw and cheek they light up individually and give the edge of her face a soft translucent halo instead of a hard outline. A tiny dark follicle point where each hair leaves the skin.

SPECULAR BEHAVIOUR: bring the gloss down to the scale of that surface tooth. Light catches on the raised rims and ridges and stays out of the pits, so every shiny area resolves into hundreds of small, uneven, sharp-edged glints separated by duller skin. The brightest clusters sit on the tip and bridge of her nose, the tops of her cheekbones, her chin and her forehead, and between the clusters the skin is drier and more matte. Sweat sits as individual micro-beads, each with its own pinpoint highlight, gathering in the pores.

SUBSURFACE: light sinks a millimetre or two into the skin before it returns, so the edge between lit and shadowed skin is soft and bleeds warm red rather than turning at a hard line. The rim of her ear and the edges of her nostrils glow faintly where the sun passes through thin tissue.

Match the photograph's own grain, noise and focus. The new detail belongs at the same sharpness as the brickwork behind her — resolved but soft, the way a phone sensor renders skin in bright sun. The result is unretouched, healthy skin on a 25-year-old in hard summer light.
```

---

## Why A3 and not A

Version A got the pores, surface texture and specular break-up right, and also produced moles
across her forehead, nose, cheeks, neck, chest and shoulders, plus forehead lines, crow's feet,
under-eye lines, nasolabial creases and neck lines. A3 is A with the two causes removed and a
replacement guard added.

**Removed: `MELANIN GRAIN`.** `Tone variation at two or three millimetres` is what became
moles. Deleted outright — there is no safe wording for it (see the scale rule below).

**Replaced: `MICRO-RELIEF` → `SURFACE TOOTH`.** The old block asked for `a network of tiny
lines`, which became wrinkles. The new one asks for the same roughness as `the faint
orange-peel quality of real skin` — a property of the surface rather than a structure drawn on
it. A quality has no scale to inflate; a line does.

**Removed:** `pores stretch and elongate in the direction the skin is pulled by her expression`
(invited expression lines) and `gathering in pores and micro-creases` (put *creases* in a
prompt that had no business containing the word).

**Added, in place of the old size limit:**

> `her skin stays clear and even in tone, carrying only the marks it already has, and the only
> creasing anywhere on her face is the soft folding her expression is making in this moment`

`Nothing larger than a pore changes` did not bind and has been dropped in favour of this. Note
the form: it states positively what the skin *is*, rather than listing what to avoid. Saying
"no moles, no wrinkles" would name both and risk summoning them (BIBLE §5b); describing clear,
uncreased skin occupies the same space with none of that exposure.

## The scale rule this came from

> **A model cannot draw below its own resolution.** A feature requested at a scale too small to
> render is rendered at the smallest scale the model *can* draw — ten to fifty times larger
> than asked. It is not disobeying; it has no smaller mark available.

So the enlarged version of a request is what you are actually ordering:

| Request | Ten times too big | |
|---|---|---|
| Pores | Larger pores | safe |
| Vellus hair | Coarser fuzz | safe |
| Micro-speculars | Larger glints | safe |
| Subsurface bleed | Softer shadow edge | safe |
| `network of tiny lines` | **Wrinkles** | cut |
| `tone variation at 2–3 mm` | **Moles** | cut |

Everything left in A3 sits in the safe half of that table. Before adding any clause, ask what
it looks like ten times too big; if that is a defect, no wording saves it.

## What to check, in order

1. **The mole above her eyebrow is still there**, and it is the only one on her face.
2. **No new lines** on her forehead, beside her eye, under her eye, from nose to mouth, or on
   her neck. Only the folds the expression itself makes.
3. **Skin tone unchanged** — sample a cheek patch against the input if unsure.
4. **Sheen broken up, not enlarged.**
5. **Then** the pores: present, graded by region, and no sharper than the brick behind her.

---

## Other versions in this file

### FIX — corrective pass, for the over-textured output only (1162 characters)

Only for the image that already has good pores plus unwanted moles and lines. It does not apply
to the plastic base.

```
Keep this photograph exactly as it is — the same face, expression, skin tone, hair, clothes, crop, light and background — and keep all of the fine skin texture, pores, fine hairs and small specular glints exactly as they are now. This is a correction to spots and lines only.

First, the dark spots. Keep the single small mole above her eyebrow on the right of the image. Clear the other dark spots away — the ones on her forehead, on her nose, across her cheeks, on her neck, on her chest and along her shoulders and arm — so that skin returns to an even, clear tone while keeping every pore and all of its texture intact.

Second, the lines. Ease out the horizontal lines across her forehead, the lines fanning from the corner of her closed eye, the lines beneath her open eye, the creases running from her nose down to the corners of her mouth, and the lines on her neck. What remains is only the soft natural folding her expression is making in the moment. Her skin reads as the smooth young skin of a 25-year-old that simply has visible pores.

Everything else stays untouched, pixel for pixel, at the same sharpness and grain as the rest of the photograph.
```

This one deliberately names the moles and lines. That is correct and does not contradict
BIBLE §5b: the rule concerns naming things you want **left alone**. Naming something you want
the model to **act on** is how an edit prompt should work — the hazard was only ever in
negation, where polarity is unreliable.

### B — short pass (785 characters)

```
Add fine skin texture to this photograph. Everything else stays exactly as it is, pixel for pixel.

Keep the small dark mole above her eyebrow on the right side of the image. Keep the mark on her chest and the one on her upper arm. Keep her exact skin colour and tone, her face, her expression, her hair, the crop and the background all unchanged.

Add only, at pore scale:
- real visible pores on her nose, cheeks, chin and forehead
- fine pale vellus hair along her jawline, hairline and upper lip
- the wide shiny patches on her forehead, nose and cheekbones broken into small uneven specular points, with drier matte skin between them

Nothing larger than a pore changes. Match the existing grain and sharpness so the new texture sits at the same softness as the rest of the photo.
```

### C — minimal fallback (284 characters)

```
Keep this photograph exactly as it is, pixel for pixel, including the small dark mole above her eyebrow. Add only real skin pores and fine vellus hair to her face and shoulders, and break the wide shiny highlights into small uneven specular points. Nothing larger than a pore changes.
```

---

## Why A added moles and wrinkles

Nothing in A was a negation and nothing named a facial feature, so §5b was not the cause. The
cause is more fundamental:

> **A model cannot draw below its own resolution.** Any feature requested at a scale too small
> to render is rendered at the smallest scale the model *can* draw — typically ten to fifty
> times larger than asked. `Nothing larger than a pore changes` cannot prevent this, because
> the model is not choosing to disobey; it has no smaller mark available.

That makes the enlarged version of a request the thing you are actually ordering. Check each
one before including it:

| Request | What it becomes when scaled up | Verdict |
|---|---|---|
| Pores | Slightly larger pores | Safe — still pores |
| Vellus hair | Slightly coarser fuzz | Safe |
| Micro-speculars | Slightly larger glints | Safe |
| **`network of tiny lines`** | **Wrinkles** | Cut |
| **`tone variation at two or three millimetres`** | **Moles and freckles** | Cut |

`MICRO-RELIEF` and `MELANIN GRAIN` were the two failures, and both were predictable from that
table. They are the exact blocks A2 removes.

Two smaller contributors, also cut in A2: `pores stretch and elongate in the direction the skin
is pulled by her expression` invited expression lines, and `gathering in pores and
micro-creases` put the word *creases* in a prompt that had no business containing it.

**The replacement for micro-relief** is `SURFACE TOOTH` — the same roughness described as an
orange-peel *quality of the surface* rather than as a mesh of lines. A quality has no scale to
inflate; a line does.

### The rule, stated for reuse

Before adding any clause to a texture prompt, ask what it looks like ten times too big. If the
answer is a defect, the clause cannot go in at any wording — the size qualifier will not save
it. Only request features whose enlarged form is still the thing you wanted.

## Why the first attempt changed the wrong things

The first version of this file ran 1,951 characters with a long `do not` list. It produced a
re-render, not a texture pass. Measured against the input:

| Changed | Detail |
|---|---|
| **The mole above her eyebrow** | Removed entirely |
| **Skin tone** | Cheek patch moved from RGB 172,100,67 to 178,107,81 — lighter, and the blue channel up 14, so less saturated. Visibly more yellow-gold |
| **Eyebrows** | Noticeably thicker, bushier, re-arched |
| **Eye** | Shape altered, iris lighter |
| **Sheen** | *Increased.* Broad gloss patches on the forehead and cheek got larger, the opposite of what was asked |
| **Creases** | Under-eye and nasolabial lines deepened, despite being explicitly forbidden |
| **Earring** | Re-rendered at a different thickness |
| **Background** | The walking man's clothing, the storefront group and the cyclist all shifted |

### The cause: negations name their subject

`Do not add freckles, moles, beauty marks` is what removed the mole. `Do not change her skin
tone, her complexion` is what changed the skin tone. Naming something in a negative puts it in
the model's attention as a thing to act on, and the polarity is not reliably preserved — an
instruction mentioning moles gets applied *to* the moles.

This is the same finding already recorded in BIBLE §5b for rendered phone bezels, where
`no inset image` produced inset images and only a positive full-bleed clause fixed it. The
rule generalises further than it was written:

> **Never name a thing you want left alone.** Protect it with a positive keep — `keep the small
> dark mole above her eyebrow` — or do not mention it at all. A do-not list is a list of things
> you have just drawn the model's attention to.

The second cause is length. 1,951 characters describing eyes, brows, nose, lips, teeth,
jawline, cheeks and hairline is a re-description of her face, and an editor re-synthesises what
you describe to it. The crowd pass that worked (prompt 03) was 921 characters and named one
region. This prompt is 785 and names three additions.

### What changed in the prompt above

- The entire `do not` list is gone.
- The mole, the chest mark and the arm mark are protected by **positive keeps** that name them
  as things to preserve.
- `DEPTH` is deleted. It was the block that moved the skin tone, and the other three carry the
  improvement without touching colour.
- No facial feature is named anywhere. Pores, fuzz and speculars are surfaces, not features.

## What to check on the output

Check these in order and stop at the first failure — each one means re-run, not adjust.

1. **The mole above her eyebrow is still there.** This is the fastest tell that the pass
   overstepped.
2. **Skin tone unchanged.** Sample a cheek patch against the input if unsure; more than a few
   RGB points of drift means it re-rendered.
3. **Eyebrows unchanged** in thickness and shape.
4. **Sheen is broken up, not bigger.** Larger gloss patches mean it read `shiny` as an
   instruction to add shine.
5. **No new lines** under the eye or beside the nose.
6. **Background people unchanged** — same clothing, same positions.
7. **Then, finally:** are there pores, and do they sit at the same sharpness as the brick
   behind her?

## If it still overshoots

Use the minimal fallback. If that also moves things, cut it to a single addition —
`Keep this photograph exactly as it is, pixel for pixel. Add only real skin pores to her face.`
— and run the fuzz and specular passes as separate rounds, feeding each output into the next.
Three tiny passes drift the face far less than one that tries to do everything.
