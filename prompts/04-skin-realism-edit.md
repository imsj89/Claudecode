# Prompt 04 — Skin texture (edit pass, additive only)

**Type:** image edit · **Input:** the approved crowd version of the profile picture
**Model:** `nano_banana_pro`. Attach only the image being fixed, no character references.

---

## The prompt — paste this

**785 characters.**

```
Add fine skin texture to this photograph. Everything else stays exactly as it is, pixel for pixel.

Keep the small dark mole above her eyebrow on the right side of the image. Keep the mark on her chest and the one on her upper arm. Keep her exact skin colour and tone, her face, her expression, her hair, the crop and the background all unchanged.

Add only, at pore scale:
- real visible pores on her nose, cheeks, chin and forehead
- fine pale vellus hair along her jawline, hairline and upper lip
- the wide shiny patches on her forehead, nose and cheekbones broken into small uneven specular points, with drier matte skin between them

Nothing larger than a pore changes. Match the existing grain and sharpness so the new texture sits at the same softness as the rest of the photo.
```

### Minimal fallback — 284 characters

If the version above still moves anything, use this instead. Shorter is safer on an editor.

```
Keep this photograph exactly as it is, pixel for pixel, including the small dark mole above her eyebrow. Add only real skin pores and fine vellus hair to her face and shoulders, and break the wide shiny highlights into small uneven specular points. Nothing larger than a pore changes.
```

---

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
