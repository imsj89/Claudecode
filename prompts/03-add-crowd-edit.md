# Prompt 03 — Add background crowd (edit pass on the approved PFP)

**Type:** image edit · **Input:** the approved profile-picture frame, and nothing else
**Model:** `nano_banana_pro` — a real instruction editor. See the failure analysis below before
using `seedream_v4_5`.

Attach **only the approved image**. Do not attach `ref-1` … `ref-5`: the face is already
correct in the input, and extra references give the model permission to re-render it.

---

## The prompt — paste this

**921 characters.** Short on purpose. See "Why the first version failed".

```
Keep this exact photograph. Same crop, same zoom, same camera distance, same face, same skin, same pose, same clothes, same cup. Her head and shoulders fill the frame exactly as they do now. Do not zoom out, do not widen the shot, do not show more of her body, do not redraw her.

The only change: put people into the empty street behind her.
- On the pavement to her left, mid-distance: a man walking away from the camera, back turned, mid-stride.
- Near the storefronts along the top: two people standing talking, in profile, small.
- On the road: a cyclist passing, seen from behind.

All three are behind her, turned away or in profile, faces indistinct, exactly as soft as the storefronts already are, casting hard shadows in the same direction as the shadows already in the photo. Nobody in front of her, nobody touching the frame edges, nobody looking at the camera. Everything else in the picture stays untouched.
```

**If it still zooms out:** cut to a single addition (the man walking away) and put
`Do not change the framing` as the first line and again as the last line.

---

## Why the first version failed — run `42bd6a0f`, seed 381999

The first attempt at this file used a long preservation list and five placements. On
`seedream_v4_5` it produced a full re-render, not an edit. Against the input frame:

| Changed | What happened |
|---|---|
| **Framing** | Pulled back from a face-filling close-up to a half-body shot. Her face went from roughly 45% of frame height to 15% — fatal for a profile picture, which crops to a circle |
| **Face** | Re-rendered. Smoother, cleaner, reads younger; the sweat sheen and pore texture the original prompt fought for were gone |
| **Sunglasses** | Slid from the crown of her head down to her hairline, different tilt |
| **Earring** | Thick gold huggie became a thinner different hoop |
| **Hair** | High ponytail loosened, more hair falling forward |
| **Pendant** | Smaller, colours shifted |
| **Straw** | Re-angled across her face toward her mouth |
| **Body** | Full midriff and leggings now in frame; bust well under the locked spec |
| **Signage** | Existing storefront sign re-rendered as gibberish — `NOIT SOSG ECNCIOS` |
| **Right edge** | The cropped-pedestrian instruction produced a floating fragment: a hand, a leg and a sneaker with no body attached |

What *did* work: the crowd itself. The man walking away, the cyclist, the woman with the tote,
the pair by the sandwich board and the motion-blurred car all landed with correct scale,
correct perspective and correct shadow direction. The additions were never the problem.

### Two causes

**1. Seedream 4.5 is not an inpainting editor.** Given an input image it does
image-to-image: it re-synthesises the whole frame using the input as a conditioning signal.
There is no mechanism to copy pixels through, so `DO NOT CHANGE` cannot bind anything. Worse,
a long preservation list reads to the model as *a description of things to draw* — which is
exactly why every wardrobe item came back present but reimagined rather than preserved.

**The rule: on an i2i model, naming something to protect it is the same as asking for it to be
redrawn.** Protect by saying less, not more.

**2. The placements did not fit the frame.** Five positions spread across the road, the far
storefronts and both frame edges describe more street than the original crop physically
contains. Asked to fit them all in, the model did the only thing it could and widened the
shot. That one is a prompt error, not a model limitation — the fix is to ask only for what is
already visible behind her.

### What changed in the prompt above

- The preservation list is gone, replaced by one framing lock at the top.
- Five placements down to three, all inside the existing background.
- The cropped frame-edge pedestrian is dropped entirely — it produced the floating fragment
  and it is the placement most likely to pull the crop wider.
- The car is dropped: it needed road that is barely in shot.

## Model choice

`nano_banana_pro` preserves unmasked content far better than Seedream i2i, which is why it was
the recommendation. Seedream was presumably chosen because Unlimited only applies there
(BIBLE §5b). That trade is worth re-examining: an Unlimited re-roll that destroys the framing
is worth less than one credit spent on an editor that holds it.

## What to check on the output

1. **Framing first.** Compare face size against the input before looking at anything else.
   This is the failure mode now.
2. **Her face is untouched.** Any softening, any lost sheen — reject.
3. **Signage.** Existing storefront text must not turn to gibberish. It is the clearest
   evidence the frame was re-rendered rather than edited.
4. **No body fragments.** Every added person needs a plausible complete body, even if partly
   occluded.
5. **Shadows agree** with the existing ground shadows in direction and hardness.
6. **Scale by distance.** People further back are smaller *and higher* in frame.
7. **No resolved background faces.** If one came out sharp, re-run.

## Cost note

At 0.98 credits this is a web-app job. Unlimited applies on Seedream only, and is not reachable
through the MCP connector.
