# Prompt 04 — Skin texture (edit pass, additive only)

**Type:** image edit · **Input:** the approved crowd version of the profile picture
**Model:** `nano_banana_pro`. Attach only the image being fixed, no character references.

Three versions, longest first. **Start with A**; drop to a shorter one only if it moves
something it should not. No version contains the words "do not", and no version names a facial
feature (BIBLE §5b).

---

## A — detailed micro-level pass (2942 characters)

```
Add photographic micro-detail to her skin. Everything already in the photograph stays exactly as it is, pixel for pixel — her face, her expression, her colouring, her hair, her clothes, the crop, the light and the background. Keep the small dark mole above her eyebrow on the right of the image, the mark on her chest and the mark on her upper arm.

Work at the millimetre scale only. Nothing larger than a pore changes.

PORE STRUCTURE: give the skin real pores with real anatomy. Each pore is a tiny pit with a soft shadowed centre and a faintly raised rim catching light, not a printed dot. Largest and slightly open across the nose, the sides of the nose and the nose bridge. Smaller and denser on the inner cheeks beside the nose. Fine and shallow across the forehead. Sparse and barely there on the outer cheeks toward the jaw. Pores are confined to those areas alone. They stretch and elongate slightly in the direction the skin is pulled by her expression.

MICRO-RELIEF: between the pores, the faint criss-cross network of tiny lines that covers all real skin — a shallow irregular mesh of diamonds and triangles, a fraction of a millimetre deep. Strongest across the forehead and the bridge of the nose. It reads as a very fine tooth in the surface, at the limit of what the sensor resolves.

VELLUS HAIR: fine, short, pale hairs across her cheeks, jawline, temples and in front of her ears, most lying flat against the skin. Where the sun rims her jaw and cheek they light up individually and give the edge of her face a soft translucent halo instead of a hard outline. A tiny dark follicle point where each hair leaves the skin.

SPECULAR BEHAVIOUR: bring the gloss down to the scale of the micro-relief. Light catches on the raised rims and ridges and stays out of the pits, so every shiny area resolves into hundreds of small, uneven, sharp-edged glints separated by duller skin. The brightest clusters sit on the tip and bridge of her nose, the tops of her cheekbones, her chin and her forehead, and between the clusters the skin is drier and more matte. Sweat sits as individual micro-beads, each with its own pinpoint highlight, gathering in pores and micro-creases.

SUBSURFACE: light sinks a millimetre or two into the skin before it returns, so the edge between lit and shadowed skin is soft and bleeds warm red rather than turning at a hard line. The rim of her ear and the edges of her nostrils glow faintly where the sun passes through thin tissue.

MELANIN GRAIN: within her existing skin colour, faint variation at a scale of two or three millimetres, so every patch of skin varies very slightly in tone. Far too fine to read as blotchiness.

Match the photograph's own grain, noise and focus. The new detail belongs at the same sharpness as the brickwork behind her — resolved but soft, the way a phone sensor renders skin in bright sun. The result is unretouched, healthy skin on a 25-year-old in hard summer light.
```

---

## B — short pass (785 characters)

```
Add fine skin texture to this photograph. Everything else stays exactly as it is, pixel for pixel.

Keep the small dark mole above her eyebrow on the right side of the image. Keep the mark on her chest and the one on her upper arm. Keep her exact skin colour and tone, her face, her expression, her hair, the crop and the background all unchanged.

Add only, at pore scale:
- real visible pores on her nose, cheeks, chin and forehead
- fine pale vellus hair along her jawline, hairline and upper lip
- the wide shiny patches on her forehead, nose and cheekbones broken into small uneven specular points, with drier matte skin between them

Nothing larger than a pore changes. Match the existing grain and sharpness so the new texture sits at the same softness as the rest of the photo.
```

---

## C — minimal fallback (284 characters)

```
Keep this photograph exactly as it is, pixel for pixel, including the small dark mole above her eyebrow. Add only real skin pores and fine vellus hair to her face and shoulders, and break the wide shiny highlights into small uneven specular points. Nothing larger than a pore changes.
```

---

## What each block in A is doing

Skin does not read as plastic because it lacks pores. It reads as plastic because it is a
**smooth surface with one gloss on it**, and a surface has no anatomy. Each block restores one
piece of that anatomy at the millimetre scale.

**PORE STRUCTURE** — the detail that matters is that a pore is a *pit*: a shadowed centre with
a faintly raised rim catching light. Rendered "pores" are usually printed dots of a darker
tone, which at any real resolution read as noise laid over plastic rather than holes in a
surface. Density is graded by region — open on the nose, fine on the forehead, sparse near the
jaw — because uniform pore density is its own tell.

**MICRO-RELIEF** — the piece almost every skin prompt omits. Real skin carries a shallow
criss-cross mesh of tiny lines, a fraction of a millimetre deep, in irregular diamonds and
triangles. It is what makes skin look like skin instead of matte plastic, and it is also the
structure the speculars need in order to break up. Pores without micro-relief still read
synthetic.

**VELLUS HAIR** — fine pale hairs, lit individually where the sun rims her jaw, turning the
silhouette of her face into a soft translucent halo instead of a hard cut. A hard facial edge
is a strong render cue and this is the only thing that softens it.

**SPECULAR BEHAVIOUR** — the loudest cue of all, and it depends on MICRO-RELIEF existing first.
Light sits on raised rims and stays out of the pits, so a shiny cheek is not one gloss but
hundreds of small uneven glints with duller skin between. Sweat as individual micro-beads, each
with its own pinpoint highlight, rather than a glaze.

**SUBSURFACE** — skin is translucent for a millimetre or two, so the boundary between lit and
shadowed skin is soft and bleeds warm red instead of turning at a hard line. Ear rims and
nostril edges glow where sun passes through thin tissue. Renders terminate light at the
surface, which is why rendered faces look like painted objects.

**MELANIN GRAIN** — tone variation at two or three millimetres, bounded inside her existing
colour and dialled far below anything that could read as blotchiness. The previous attempt's
colour block is what shifted her skin tone, so this one is deliberately timid.

## The scale rule

`Work at the millimetre scale only. Nothing larger than a pore changes.`

Skin instructions slide upward in scale on their own — asked for texture, an editor reaches for
freckles, then creases, then a fresh interpretation of the face. An explicit size threshold
gives it somewhere to stop, and it does safely what a do-not list cannot do at all.

## A is longer than the version that failed. Why that is still right

The failed attempt was 1,951 characters; A is 2942. Length was the *second* cause of that
failure, not the first. The first was that it named eyes, brows, nose, lips, teeth, jawline,
cheeks and hairline inside negations — which both re-described her face and inverted on the
marks it was meant to protect.

A names no facial feature and contains no negation; every character of it describes a surface
property, which is the thing being changed. That is a different kind of length from a
re-description of her face. It is still length, though, so if A drifts anything, go to B, then C.

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
