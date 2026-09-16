# Prompt 04 — Skin texture with the face locked

**Type:** image edit · **Model:** `nano_banana_pro`, image only, no character references.
**Input:** the approved crowd frame with plastic skin, the single correct mole and no extra
lines. Not the over-textured output.

---

## A4 — face locked, texture only (4211 characters)

```
Add photographic micro-detail to her skin. Everything already in this photograph stays exactly as it is, pixel for pixel — the crop, the light, the background, her hair, her clothes, her jewellery and the cup. Only the surface of her skin gains detail.

FACE LOCK — every feature below is already correct in this photograph and stays precisely as it is, unchanged in shape, size, position, proportion and colour:
Oval face, high wide cheekbones, jaw tapering to a small rounded chin. Warm mid-brown skin with a golden olive undertone.
Eyebrows thick, dark and natural, unplucked at the inner ends where the hairs sweep upward, thinning slightly along the tails, a wide gap between them. Her left brow raised high into an arch, her right brow low and straight, angled down toward the temple.
The small dark mole above her raised eyebrow, and the marks on her chest, shoulder and upper arm.
Her open eye light grey with a faint blue cast and a distinct darker ring around the iris, small pupil in the bright sun, almond shaped with a slightly downturned outer corner and a clear upper lid crease. Dark lashes of moderate length, sparse lower lashes, a faint warm sheen on the lid.
Her other eye squeezed fully shut, lashes meeting, the outer corner folding into creases.
Narrow straight nose bridge, bunched and folded across the bridge by her scrunch, tip slightly rounded and lifted, oval nostrils flared, deep creases where the nostrils meet the cheeks.
Wide crooked open grin, pulled higher on her right. Upper lip medium with a defined cupid's bow, lower lip full and rose pink. Straight even upper teeth in a faintly warm white, the two centre teeth slightly larger, tongue low and forward.
Cheeks bunched high and round beneath the open eye, a deep fold running from each nostril past the corner of her mouth.
Small ear close to the head with a thick gold huggie hoop.
Dark brown-black hair pulled back tight into a high ponytail, fine baby hairs at the hairline, loose strands across her temple and cheek.

Work at the millimetre scale only. Her skin stays clear and even in tone, carrying only the marks it already has, and the only creasing anywhere on her face is the folding her expression is already making. Her skin is the smooth young skin of a 25-year-old that simply has visible pores, and her face stays completely smooth-shaven and hairless.

PORE STRUCTURE: give the skin real pores with real anatomy. Each pore is a tiny pit with a soft shadowed centre and a faintly raised rim catching light, not a printed dot. Largest and slightly open across the nose, the sides of the nose and the nose bridge. Smaller and denser on the inner cheeks beside the nose. Fine and shallow across the forehead. Sparse and barely there on the outer cheeks toward the jaw. Pores are confined to those areas alone.

SURFACE TOOTH: between the pores, the faint orange-peel quality of real skin — a barely perceptible roughness in the surface itself, strongest across the forehead and the bridge of the nose. It reads as a fine tooth at the very limit of what the sensor resolves, the way skin looks rather than plastic.

SPECULAR BEHAVIOUR: bring the gloss down to the scale of that surface tooth. Light catches on the raised rims and ridges and stays out of the pits, so every shiny area resolves into hundreds of small, uneven, sharp-edged glints separated by duller skin. The brightest clusters sit on the tip and bridge of her nose, the tops of her cheekbones, her chin and her forehead, and between the clusters the skin is drier and more matte. Sweat sits as individual micro-beads, each with its own pinpoint highlight, gathering in the pores.

SUBSURFACE: light sinks a millimetre or two into the skin before it returns, so the edge between lit and shadowed skin is soft and bleeds warm red rather than turning at a hard line. The rim of her ear and the edges of her nostrils glow faintly where the sun passes through thin tissue.

Match the photograph's own grain, noise and focus. The new detail belongs at the same sharpness as the brickwork behind her — resolved but soft, the way a phone sensor renders skin in bright sun. The result is unretouched, healthy skin on a 25-year-old in hard summer light.
```

### A4-lite — condensed lock (3349 characters)

Same prompt with the face lock cut to the features that have actually drifted in past runs.
Use this if A4 moves anything, since length is itself a drift risk.

```
Add photographic micro-detail to her skin. Everything already in this photograph stays exactly as it is, pixel for pixel — the crop, the light, the background, her hair, her clothes, her jewellery and the cup. Only the surface of her skin gains detail.

FACE LOCK — these are already correct in this photograph and stay precisely as they are, unchanged in shape, size, position, proportion and colour:
Her eyebrows: thick, dark, natural, unplucked at the inner ends, thinning along the tails, a wide gap between them, the left raised into a high arch and the right low and straight. The small dark mole above her raised eyebrow. Her open eye: light grey with a faint blue cast and a distinct darker ring around the iris, almond shaped, outer corner slightly downturned, clear upper lid crease, dark lashes of moderate length. Her narrow straight nose bridge, bunched by the scrunch, tip slightly rounded and lifted. Her upper lip with its defined cupid's bow, her full rose-pink lower lip, her straight even upper teeth in a faintly warm white. Her warm mid-brown skin with its golden olive undertone. The marks on her chest, shoulder and upper arm.

Work at the millimetre scale only. Her skin stays clear and even in tone, carrying only the marks it already has, and the only creasing anywhere on her face is the folding her expression is already making. Her skin is the smooth young skin of a 25-year-old that simply has visible pores, and her face stays completely smooth-shaven and hairless.

PORE STRUCTURE: give the skin real pores with real anatomy. Each pore is a tiny pit with a soft shadowed centre and a faintly raised rim catching light, not a printed dot. Largest and slightly open across the nose, the sides of the nose and the nose bridge. Smaller and denser on the inner cheeks beside the nose. Fine and shallow across the forehead. Sparse and barely there on the outer cheeks toward the jaw. Pores are confined to those areas alone.

SURFACE TOOTH: between the pores, the faint orange-peel quality of real skin — a barely perceptible roughness in the surface itself, strongest across the forehead and the bridge of the nose. It reads as a fine tooth at the very limit of what the sensor resolves, the way skin looks rather than plastic.

SPECULAR BEHAVIOUR: bring the gloss down to the scale of that surface tooth. Light catches on the raised rims and ridges and stays out of the pits, so every shiny area resolves into hundreds of small, uneven, sharp-edged glints separated by duller skin. The brightest clusters sit on the tip and bridge of her nose, the tops of her cheekbones, her chin and her forehead, and between the clusters the skin is drier and more matte. Sweat sits as individual micro-beads, each with its own pinpoint highlight, gathering in the pores.

SUBSURFACE: light sinks a millimetre or two into the skin before it returns, so the edge between lit and shadowed skin is soft and bleeds warm red rather than turning at a hard line. The rim of her ear and the edges of her nostrils glow faintly where the sun passes through thin tissue.

Match the photograph's own grain, noise and focus. The new detail belongs at the same sharpness as the brickwork behind her — resolved but soft, the way a phone sensor renders skin in bright sun. The result is unretouched, healthy skin on a 25-year-old in hard summer light.
```

---

## The face lock

Every clause is a **positive statement of what the feature already is**, never an instruction
to avoid changing it. That distinction is the whole rule from BIBLE §5b: `her eyebrows are
thick, dark and natural, unplucked at the inner ends` protects them, while `do not change her
eyebrows` nominates them for editing. A lock written as a do-not list is a hit list.

The lock is derived from the approved frame itself, not from the bible's general description,
because it has to match *this* image down to the raised-versus-low brow and the direction the
brow hairs sweep. It is now also recorded in CHARACTER-BIBLE §2 as the canonical face, so
future prompts can reuse it rather than re-deriving it from a screenshot.

**A4-lite exists because the lock is long.** Past failures came from re-description: a prompt
that says enough about a face invites the model to rebuild it. A4 is 4,219 characters and most
of that is describing her face, which is exactly the shape of a prompt that has re-rendered
before — on Seedream it certainly would. Nano Banana Pro held framing and identity on the crowd
pass, so it is worth trying at full length first, but drop to A4-lite at the first sign of
drift, and to FIX or C below if that also moves things.

## Facial hair removed — and it was the right call

The `VELLUS HAIR` block is gone. It was doing real work — fine pale fuzz lit at the jaw turns a
hard facial silhouette into a soft translucent edge, and its absence is the one realism cost of
this version.

But it was also the most dangerous block left in the prompt, by the scale rule this file
already documents: **vellus hair rendered ten times too large is visible facial hair.** Peach
fuzz has no safe enlarged form on a woman's face — it becomes a moustache or sideburns. It sits
in the same column as `network of tiny lines` and `tone variation at 2–3 mm`, and it should
have been cut alongside them.

In its place the guard paragraph now carries `her face stays completely smooth-shaven and
hairless` — positive form, describing the state rather than forbidding the feature.

Expect the edge of her face to stay slightly crisper than a real photograph would be. That is
the accepted trade. If it bothers you later, the fix is a separate low-strength pass for edge
softness alone, never a return of the fuzz block.

## What each texture block does

**PORE STRUCTURE** — a pore is a *pit*: shadowed centre, faintly raised rim catching light.
Rendered "pores" are printed dots of darker tone, which read as noise laid over plastic rather
than holes in a surface. Density is graded by region because uniform pore density is its own
tell.

**SURFACE TOOTH** — the orange-peel quality between the pores. This replaced a block asking for
`a network of tiny lines`, which came back as wrinkles. A quality of the surface has no scale
to inflate; a structure drawn on it does.

**SPECULAR BEHAVIOUR** — the loudest cue of all, and it depends on the surface tooth existing
first. Light sits on raised rims and stays out of pits, so a shiny cheek becomes hundreds of
small uneven glints rather than one gloss.

**SUBSURFACE** — renders terminate light at the surface, which is why rendered faces look like
painted objects. Real skin is translucent for a millimetre or two, so the shadow edge is soft
and bleeds warm red.

## What to check, in order

1. **Eyebrows unchanged** — thickness, arch, the gap, the raised/low asymmetry. This is what
   drifted first last time.
2. **The mole above her raised brow is present**, and it is the only one on her face.
3. **No hair anywhere on her face.**
4. **No new lines** on her forehead, beside or under her eye, from nose to mouth, or on her
   neck — only the folds her expression is already making.
5. **Skin tone unchanged** — sample a cheek patch against the input if unsure.
6. **Eye colour and shape unchanged**, iris still light grey with the darker ring.
7. **Sheen broken up, not enlarged.**
8. **Then** the pores: present, graded by region, no sharper than the brick behind her.

---

## Other versions in this file

### FIX — corrective pass, for the over-textured output only (1162 characters)

```
Keep this photograph exactly as it is — the same face, expression, skin tone, hair, clothes, crop, light and background — and keep all of the fine skin texture, pores, fine hairs and small specular glints exactly as they are now. This is a correction to spots and lines only.

First, the dark spots. Keep the single small mole above her eyebrow on the right of the image. Clear the other dark spots away — the ones on her forehead, on her nose, across her cheeks, on her neck, on her chest and along her shoulders and arm — so that skin returns to an even, clear tone while keeping every pore and all of its texture intact.

Second, the lines. Ease out the horizontal lines across her forehead, the lines fanning from the corner of her closed eye, the lines beneath her open eye, the creases running from her nose down to the corners of her mouth, and the lines on her neck. What remains is only the soft natural folding her expression is making in the moment. Her skin reads as the smooth young skin of a 25-year-old that simply has visible pores.

Everything else stays untouched, pixel for pixel, at the same sharpness and grain as the rest of the photograph.
```

This one deliberately names the moles and lines it wants gone. Correct here: §5b concerns
naming things you want **left alone**. Naming something you want the model to **act on** is how
an edit prompt should work.

### C — minimal fallback (284 characters)

```
Keep this photograph exactly as it is, pixel for pixel, including the small dark mole above her eyebrow. Add only real skin pores and fine vellus hair to her face and shoulders, and break the wide shiny highlights into small uneven specular points. Nothing larger than a pore changes.
```

---

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
