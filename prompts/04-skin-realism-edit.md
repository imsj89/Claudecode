# Prompt 04 — Skin texture (edit pass, features untouched)

**Type:** image edit · **Input:** the approved crowd version of the profile picture
**Model:** `nano_banana_pro` — it held the framing on the crowd pass. Do not run this on
`seedream_v4_5` (prompt 03 records why).

Attach only the image being fixed. No character references — the face is already correct in
the input, and references invite a re-render.

---

## The prompt — paste this

**1951 characters.**

```
Add real skin micro-texture to this photograph. Nothing else changes.

Her face is correct exactly as it is. Do not alter her bone structure, eyes, eyebrows, nose, lips, teeth, jawline, cheeks, hairline, expression or wink. Do not change her skin tone, her complexion or her age. Do not add freckles, moles, beauty marks, blemishes, tan lines, wrinkles, lines or creases of any kind. Do not remove or move any mark already present. Do not change the crop, framing, hair, clothes, jewellery, cup, background, people or light.

This is a surface pass at pore scale only. Nothing larger than a pore may change.

PORES: real skin pores across her face — largest and most visible on her nose and nose bridge, slightly smaller on her inner cheeks and chin, fine and shallow across her forehead, none on her eyelids or lips. Faint natural unevenness in the skin surface between them, so it is not a smooth plane.

FUZZ: fine pale vellus hair along her jawline, in front of her ears, at her hairline and above her upper lip, catching the sun as a soft light fuzz at the edges of her face.

SHEEN: break up the even gloss. Replace the single smooth highlight with small irregular specular points on the tip and bridge of her nose, the tops of her cheekbones, her chin and her forehead, with slightly drier matte skin between them. Sweat sits in fine uneven beads, never as a uniform glaze.

DEPTH: very subtle tone variation within her existing complexion — a touch warmer through her nose and ears, a touch cooler under her eyes. Barely perceptible. Do not make her look red, blotchy or uneven.

BODY: matching fine skin texture on her shoulders, chest and arms, at the same scale.

Match the photograph's existing grain, noise and softness exactly. The new texture must sit at the same sharpness as the rest of the image, never crisper. Unretouched but clean and healthy — no smoothing, no beauty filter, no airbrushing, and nothing dirty, aged or weathered.
```

---

## The scale rule

`This is a surface pass at pore scale only. Nothing larger than a pore may change.`

That single line is the most important thing in the prompt. Skin-realism instructions
otherwise slide upward in scale on their own — asked for texture, an editor reaches for
freckles, then creases, then a whole reinterpretation of the face. Naming an explicit size
threshold gives it somewhere to stop, and everything above the threshold is then covered by
the do-not list rather than left to judgement.

## What is deliberately excluded, and why

An earlier draft of this file also asked for freckles, moles, tan lines, crow's feet, a
nasolabial fold, lip flaking and less-uniform teeth. All of that is cut. **Those are facial
features, not surface finish.** Her face is locked (BIBLE §2) and this frame is approved; a
pass that adds marks or lines produces a different woman with better skin, which is a worse
outcome than plastic skin on the right woman.

The distinction that decides what belongs in this prompt:

| Belongs — surface finish | Excluded — a facial feature |
|---|---|
| Pores, micro-unevenness | Freckles, moles, beauty marks |
| Vellus hair | Wrinkles, creases, fold lines |
| Specular break-up | Lip texture, teeth shape or colour |
| Subsurface tone variation | Tan lines, blemishes, scarring |

Everything in the left column is how light meets skin. Everything in the right column is part
of what she looks like, and belongs in the bible or nowhere.

## Why pores alone would not have been enough

Three of the four things making the skin read plastic are not texture at all, and all three
are in the left column above:

**1. The sheen is one continuous even gloss.** The loudest cue in the frame, louder than
missing pores. Real oily skin in hard sun gives *small, sharp, irregular* speculars — nose
tip, top of a cheekbone — with drier matte skin between. A smooth uniform glaze across a whole
face is what reads as rendered. This is what `SHEEN` breaks up.

**2. The skin is one flat tone.** A real face is several colours at once. `DEPTH` restores a
little of that, deliberately dialled to *barely perceptible* — pushed harder it stops being
subsurface scattering and starts being a complexion change, which is a feature change.

**3. No vellus hair.** Fine pale fuzz along the jaw and above the lip side-lights in sun and
softens every edge of the face. Its absence makes the silhouette too clean.

Pores fix the fourth. All four are the same underlying principle — **skin is differential, not
uniform** — which is why every block names a region and how it differs from its neighbour.
Anything applied evenly across the whole face just reproduces the problem at a new setting.

## The sharpness trap

Newly added texture usually renders crisper than the photo it lands in, which reads as texture
pasted onto plastic — worse than the plastic was. The grain-match line is load-bearing. If the
output has convincing pores that look sharper than the brick behind her, that is this failure,
not a win.

## What to check on the output

1. **Identity first.** Same woman, same bone structure, same expression. Compare at full size
   against the input before assessing the skin at all — texture passes drift faces more than
   people expect.
2. **No new marks.** No freckle, mole or line that was not in the input. Any of them means the
   pass overshot and should be re-run.
3. **Sheen is broken up**, not evenly reduced. A face that went uniformly matte means the
   prompt was read as "less shine" — re-run.
4. **Texture sharpness matches** the rest of the frame. Check her shoulder against the brick
   behind her.
5. **Complexion unchanged.** If she reads redder or blotchier overall, `DEPTH` overshot — cut
   that block entirely and re-run; the other three carry most of the improvement.
6. **Background untouched.** The crowd, shadows and storefronts must survive.

## If it is still not enough

Do not reach for marks or lines. In order:

1. Cut `DEPTH` and strengthen `SHEEN` — the gloss is almost always the real culprit.
2. Add `pores clearly visible at full resolution, coarse rather than fine` to `PORES`.
3. Run the pass twice, feeding the first output back in. Two gentle passes drift the face far
   less than one aggressive one.
