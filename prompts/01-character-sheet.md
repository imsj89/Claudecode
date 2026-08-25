# Prompt 01 — Character Sheet (Ashmi Gurung)

**Model:** `soul_2` · **Aspect:** 16:9 · **Preset:** photoreal-unretouched · **Composition:** split-screen

Built on the Higgsfield `character-sheet` workflow slot architecture. This is the
foundation artifact — the Reference Element and Soul training set both derive from it,
so it is worth iterating until the face is genuinely right.

---

## The prompt

```
Split-screen character sheet composition, left side a full-body shot of the character standing upright in a neutral straight standing pose facing the camera with both feet flat on the ground and arms relaxed at the sides, full head-to-toe framing with the whole body and both feet visible, right side a tight close-up chest-up portrait of the same character, identical original female character on both sides, single subject only exactly one person with only the character in frame, pure white seamless studio background, professional character sheet presentation, young woman in her mid-twenties of Nepali Himalayan heritage with warm medium-tan skin and a golden-olive undertone, heart-shaped face with a defined tapered jawline and high broad cheekbones, mature adult bone structure and adult facial proportions, straight nose with a slightly low bridge and a rounded tip, full lips with a natural rosy-brown tint and a soft matte finish, dark brown almond eyes with a slight upward outer tilt and a soft epicanthic fold, naturally muted catchlights, no oversized specular glare in the iris, eye color muted rather than glowing, thick straight dark brown eyebrows lightly groomed with natural stray hairs, black-brown hair with a warm undertone, long and thick, straight with a slight natural wave, centre parting, matte natural finish with visible flyaways, visible fine skin texture with natural pores, fine lines, subtle asymmetries and texture irregularities, natural visible makeup with slightly uneven foundation blending rather than flawless coverage, faint natural blush, a small mole below the left jaw, faint freckles across the nose bridge, slight natural sheen rather than a glossy or dewy retouched finish, no digital smoothing, no beauty filter, no AI-airbrushed look, skin completely free of artificial glare, shine or highlight blooms, matte-to-natural complexion, petite slim build approximately five feet two inches tall with a small frame and natural shoulders, wearing an oversized ecru cable-knit sweater over a white cotton tee, straight-leg mid-wash blue jeans, white leather low-top sneakers, a thin gold chain necklace with a small coral-and-turquoise pendant, small gold hoop earrings, a thin gold ring on the right hand, no bag, natural anatomy, high-end but unretouched commercial photography style, soft diffused studio lighting without harsh reflections, cinematic realism, clean white background, 4K quality, sharp focus on skin texture detail, single subject only, exactly one person, only the character in frame, no other people, no duplicate figures, no mannequin, no reflections, no props, no furniture, no background objects, empty seamless studio, left panel standing full-body head-to-toe not cropped not sitting, right panel tight close-up not full body, no babyface, no overly youthful rounded proportions, no beauty filter, no digital smoothing, no airbrushing, no plastic skin, no glossy skin, no text, no watermark, no logos, no frame borders
```

---

## What to check on the output

Judge in this order. The first two are the ones that sink the project.

1. **Heritage read.** Does she read Himalayan/Nepali — or has the model drifted to generic
   North Indian or generic East Asian? This is the known failure mode. Watch the nose bridge,
   the cheekbone width, and the eye fold.
2. **Age read.** Unambiguously mid-twenties? Any babyface drift is a hard fail — regenerate,
   do not proceed.
3. **Skin.** Visible pores and uneven foundation, or airbrushed? If it looks like a beauty
   ad, the realism engine did not take.
4. **Both panels identical.** Same person left and right, not two similar women.
5. **Framing.** Left panel standing, both feet in frame, not cropped or seated.

## Iteration levers

| Problem | Fix |
|---|---|
| Reads too North Indian | Strengthen: `Tibeto-Burman Himalayan features, broad flat cheekbones, low nasal bridge` |
| Reads too East Asian | Add: `South Asian Himalayan, warmer deeper skin tone, larger rounder eyes` |
| Too young | Add: `27 years old, defined mature jawline, longer facial thirds` |
| Too polished | Double the realism clauses; add `slightly tired under-eyes, uneven skin tone` |
| Face differs across panels | Re-emphasise `identical original character, same face on both panels` |

---

## Next steps once approved

1. `show_reference_elements action=create` from the approved image → the Element
2. Generate 15–20 varied shots from the Element (vary angle, expression, distance, light)
3. `show_characters action=train` on that set → the Soul (~10 min)
4. Production: Soul + `soul_2` for stills · Element for video models
