# Prompt 03 — Add background crowd (edit pass on the approved PFP)

**Type:** image edit, not generation · **Input:** the approved profile-picture frame
**Model:** `nano_banana_pro` (best instruction-following editor) · fallback `seedream_v4_5` edit
**Aspect:** unchanged — do not let the tool reframe or re-crop

Attach **only the approved image**. Do not attach `ref-1` … `ref-5` on an edit pass: the face
is already correct in the input, and extra references give the model permission to re-render
it.

---

## The prompt — paste this

**2386 characters.**

```
Edit this photograph. Everything already in it stays exactly as it is. The only change is adding people to the street behind her.

DO NOT CHANGE: her face, bone structure, wink, open mouth and tongue, skin texture, sheen, moles and stray brows. Her body, pose, arms and hands. Her white ribbed crop tank, gold huggie hoops, coral-and-turquoise pendant and ring, black sunglasses on her head, ponytail and flyaway strands. The lemonade cup, domed lid, straw, ice, condensation and her grip on it. The crop, tilt, camera angle, exposure, colour grade, noise and grain. The brick sidewalk, road markings, storefronts and signage already present. Do not re-render her, do not move her, do not clean her up.

ADD, in the background only:
- Grey pavement to the left of her, mid-distance: a man in a short-sleeve shirt walking away from the camera, back turned, caught mid-stride.
- Further back on the left, near the sandwich-board sign: two people standing talking, both in profile, small in frame.
- Upper right, in front of the dark glass storefront: a woman walking past in profile, tote bag on her shoulder, head turned away.
- On the road behind: a cyclist seen from behind, and a car passing, motion-blurred.
- Right edge behind her shoulder: one pedestrian cut off by the frame edge, only partly visible.

HOW THEY MUST LOOK: nobody is aware of the camera. Every person turned away, in profile, or cropped. Faces small, indistinct and unresolved, softened by distance and movement. Ordinary summer weekday clothing, muted, nothing bright enough to pull the eye. All of them behind her — none overlapping her face, hair, shoulders, arm or cup, and nobody between her and the camera.

MATCH THE PHOTOGRAPH: same harsh high summer sun, hard-edged shadows on the ground running in the same direction as the shadows already there, blown highlights on their shoulders and heads. Same background softness — exactly as soft as the storefronts already are, never sharper than her face. Correct scale and perspective for a camera held high and angled down: people further back are smaller and higher in the frame, feet planted on the receding ground plane, no one floating. Same white balance, same phone-camera noise, same JPEG artifacts on their edges. They must look like they were in the original frame, not pasted into it.

No second copy of her. No new text, signage, logos or watermark.
```

---

## Why edit instead of re-rolling with the BACKGROUND block

`prompts/02-profile-picture.md` now contains a `BACKGROUND` block, but running it produces a
*new* image — new seed, new face, new outfit drape, new expression. That frame is approved.
Re-rolling to get strangers into it trades a known-good face for a lottery ticket, and face
drift on strong expressions is the most persistent failure in this project (GENERATION-LOG,
Element v2 finding).

An edit pass changes the pixels that need changing and leaves her alone. Keep the
`BACKGROUND` block in prompt 02 for *future* shots; use this file for *this* frame.

## How this prompt is built, and why in that order

An edit prompt is not a generation prompt with "add" in front of it. Three things make it hold:

1. **Preservation before addition.** The `DO NOT CHANGE` list runs first and is long on
   purpose. Editors treat an unmentioned element as fair game — the jewellery, the sweat
   sheen, the tilt and the grain all get quietly "improved" if you don't name them. The
   sheen and the grain matter most: an editor's instinct is to clean a face up, and a
   retouched face is the exact AI tell the original prompt worked hardest to avoid.

2. **Named placements, not a headcount.** `add people to the street` puts them wherever the
   model likes, which is usually straight through her silhouette. Each addition here names a
   region that is currently empty — the grey pavement left of her, the sandwich-board sign,
   the dark storefront upper right, the road, the right frame edge — so the crowd fills real
   space and leaves her outline intact.

3. **Match instructions last.** Added figures fail by being too sharp, too clean, lit from the
   wrong side, or the wrong size for their distance. The `MATCH THE PHOTOGRAPH` block ties
   each of those to something already visible in the frame rather than to an absolute — same
   softness *as the storefronts*, shadows in the same direction *as the existing shadows*.
   Comparative beats absolute here for the same reason it does on her body measurements
   (BIBLE §5b).

**Every stranger is turned away, in profile, or cropped.** Background faces are where these
models fail hardest, and a melted face fifteen feet behind her would ruin the frame more
thoroughly than an empty street ever did. This is also just what a real phone photo does at
this depth of field, so it costs nothing.

## What to check on the output

1. **Her face is untouched.** Compare against the input at full size. Any softening, any
   symmetry correction, any lost sheen — reject and re-run.
2. **Her outline is clear.** Nobody clipping her hair, shoulder, arm or the cup.
3. **Shadows agree.** Added figures cast hard shadows in the same direction as the existing
   ground shadows. Wrong-direction shadows are the giveaway.
4. **Scale by distance.** People further back are smaller *and higher* in the frame. A
   correctly-sized figure standing at the wrong height reads as a cutout.
5. **No resolved background faces.** If one came out sharp and detailed, re-run — do not keep
   it and hope the circle crop hides it.
6. **Grain match.** Added figures should carry the same noise and JPEG edges as the rest. Too
   clean is the most common failure.
7. **Aspect unchanged.** Some editors quietly re-crop. It must still be square.

## If the edit fights you

- **She got re-rendered anyway** → the input is being treated as a reference rather than a
  canvas. Drop every extra attachment and shorten the addition list to two placements.
- **People appear in front of her** → move `nobody between her and the camera` to the top of
  the prompt, immediately after the first line.
- **The whole image got brighter or cleaner** → the model re-graded. Add `do not adjust
  exposure, contrast or saturation anywhere in the frame` to the `DO NOT CHANGE` list.
- **Nothing changed** → the preservation list is smothering the edit. Cut it to the face,
  outfit and cup, and keep the additions.

## Cost note

Editors charge per output like any generation. At 0.98 credits this is a web-app job, where
Unlimited applies (BIBLE §5b — Unlimited is not reachable through the MCP connector).
