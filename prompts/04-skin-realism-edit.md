# Prompt 04 — Skin realism (edit pass)

**Type:** image edit · **Input:** the approved crowd version of the profile picture
**Model:** `nano_banana_pro` — it held the framing on the crowd pass, which is why this file
assumes it. Do not run this on `seedream_v4_5` (prompt 03 records why).

Attach only the image being fixed. No character references.

---

## The prompt — paste this

**2275 characters.**

```
Keep this photograph exactly as it is. Same crop, same framing, same face and bone structure, same expression, same hair, same clothes, same jewellery, same cup, same background and the same people in it, same light. Do not redraw her, do not reshape anything, do not move anything, do not change her age or identity.

Change only the surface of her skin, so it reads as a real person photographed on a phone rather than a rendered one.

TEXTURE: real visible pores, densest on her nose, nose bridge and inner cheeks, finer across her forehead, almost none on her eyelids. Faint vellus hair along her jaw, in front of her ears, above her upper lip and at her hairline, catching the sun as a soft pale fuzz. Slight roughness on her shoulders and the tops of her arms.

SPECULAR: break the sheen up. Not one smooth even gloss — small irregular specular highlights on the tip and bridge of her nose, the tops of her cheekbones, her chin and her forehead, with drier matte patches between them. Sweat sits in beads and uneven streaks, never as a uniform glaze.

COLOUR: stop the skin being one flat tone. Warmer red through her nose, nostrils, ears and the apples of her cheeks. Cooler and slightly blue-green under her eyes and at her temples. Yellower across her forehead. Ears and the rims of her nostrils faintly translucent where the sun passes through. Slight blotchy sun flush on her chest and shoulders.

MARKS: a scatter of small sun freckles across her nose, upper cheeks, shoulders and chest — uneven, asymmetric, not a pattern. A few tiny moles and beauty marks. Keep every mark already present. Faint uneven tan on her chest.

CREASES: real crinkle lines radiating from the corner of her squeezed-shut eye, fine lines under her open eye, a genuine crease where her cheek bunches up, a soft nasolabial fold. Small dry flakes on her lower lip. Teeth slightly less uniformly white, very slightly uneven.

Match the photograph's existing grain, noise and softness — the new texture must sit at the same sharpness as the rest of the image, never crisper.

Unretouched, not dirty. She is a healthy 25-year-old in bright sun, not weathered or aged. No added wrinkles beyond the expression she is making. No smoothing, no beauty filter, no airbrushing anywhere in the frame.
```

---

## What actually makes skin read plastic

"Add skin texture" does not fix it. Pores are only one of four failures, and usually not the
loudest. In the crowd version, all four are present:

**1. The sheen is one continuous even gloss.** Real oily skin in hard sun produces *small,
sharp, irregular* speculars — the tip of the nose, the top of a cheekbone — with dry matte
skin between them. A smooth uniform glaze across the whole face is the single strongest
"rendered" cue in the frame, and it is what the `SPECULAR` block exists to break.

**2. The skin is one flat colour.** A real face is several colours at once: red through the
nose, nostrils, ears and cheek apples; blue-green under the eyes and at the temples; yellower
across the forehead. Ears and nostril rims go faintly translucent in strong sun. A single
sampled skin tone stretched over the whole face is a render, not a photograph.

**3. It is unmarked.** She is in harsh summer sun with bare shoulders and chest, and there is
not one freckle, mole or patch of sun mottling on her. Flawless skin over that much exposed
surface is not plausible at this light level.

**4. No vellus hair.** Real skin has fine pale fuzz along the jaw, in front of the ears and
above the lip, and in sun this side-lights and softens every edge. Its absence makes the
silhouette of the face too clean.

The fix for all four is the same principle: **skin is differential, not uniform.** Every block
in the prompt names a region and how it differs from its neighbour. Instructions that apply
one property evenly across the whole face — "more texture", "less smooth" — reproduce the
problem at a different setting.

## Two things that had to be held back

**Age.** Creases and texture push apparent age up. PROJECT-BRIEF §7 wants her unambiguously
mid-20s or older, so that direction is safe — but only to a point, and a weathered 40-year-old
is a different failure. `No added wrinkles beyond the expression she is making` and `healthy
25-year-old in bright sun, not weathered` are the brakes. Keep both.

**Sharpness.** Newly added texture typically renders crisper than the photo it lands in,
which reads as texture pasted onto plastic — worse than the plastic was. The grain-match line
is doing real work; do not cut it.

## Consistency warning — read before accepting freckles

Skin markings are identity, the same as the pendant. If this frame gains freckles across her
nose and shoulders and no other shot has them, the account has two different women in it.

Before accepting the output, decide which it is:

- **Keep the freckles** → they become canon. Record the exact pattern in CHARACTER-BIBLE §2,
  add them to the Element reference set, and carry a freckle line in every future prompt.
- **Reject the freckles** → re-run with the `MARKS` block cut to `keep every mark already
  present` and let the other three blocks do the work. They carry most of the improvement.

Recommended: keep them, but only if you are willing to do the bible and Element update in the
same sitting. Freckles are a strong realism win and a strong consistency liability, and the
liability is the one that bites later.

## What to check on the output

1. **Identity.** Same woman, same bone structure. Texture passes drift faces more than people
   expect — compare at full size against the input.
2. **Age.** Still reads mid-twenties, not older. This is the direction this prompt pushes.
3. **Sheen is broken up**, not evenly reduced. If the whole face went matte, the prompt was
   read as "less shine" and it needs re-running.
4. **Colour varies by region.** Red nose and ears, cooler under-eyes. If the face is still one
   tone with pores on it, nothing important changed.
5. **Texture sharpness matches** the rest of the frame — check her shoulder against the brick
   behind her.
6. **The background is untouched.** The crowd, the shadows and the storefronts must survive.
7. **Not dirty.** Blotchy, greasy or aged is a failure, not a success.
