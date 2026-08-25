# Prompt 02 — Profile picture (Aasmi Adhikari)

**Model:** `seedream_v4_5` · **Aspect:** `1:1` · **Quality:** 4K / basic · **Unlimited:** on
**References:** attach `ref-1` … `ref-5` from the PFP-REFS bundle (up to 14 allowed)

Run this in the Higgsfield web app, where Unlimited is available. If running via MCP instead,
drop the attachments and embed `<<<83ab454a-a85a-4814-8459-c10fc7e493aa>>>` at the start.

**Why 1:1** — Instagram crops the profile picture to a circle from a square. A 9:16 selfie
loses the sides and pushes her face small. Shoot 1:1 and the circle crop keeps her face
filling the frame. If you also want it as a grid post, run a second pass at 4:5.

---

## The prompt

```
A single full-bleed square photograph filling the entire frame edge to edge. Candid phone selfie held high above her head and angled down, arm's-length, slight tilt, casually framed. Close-up head-and-shoulders shot of the same woman as in the reference images, keeping her exact face, bone structure, nose, jawline, eye shape and identity completely unchanged. A 25-year-old Nepali-American woman on a sunny summer street in Boston, brick sidewalk and blurred storefronts behind her. She holds a tall clear plastic cup of iced lemonade with a straw up near her chin, condensation on the cup. Wearing a simple white ribbed tank top and thin gold hoops, a thin gold chain with a small round pendant with a coral orange centre stone inside a turquoise ring. Black sunglasses pushed up onto the top of her head, holding her hair back. Long black-brown hair loose with flyaways, a few strands stuck to her neck in the heat. EXPRESSION: a playful exaggerated pout, lips pushed forward, eyebrows slightly raised, eyes looking straight up into the lens, deliberately silly rather than seductive. Her face fills most of the frame, centred, with a little headroom, framed so a circular crop keeps her whole face. LIGHT: bright direct summer sunlight from above and slightly behind the phone, hard-edged shadows under her chin and nose, a few blown-out highlights on her forehead and cheekbones, warm and slightly overexposed, visible sensor noise in the shadows. Real phone-camera look with mild lens distortion from the close high angle. Unretouched: visible skin texture and pores, a faint sheen of sweat, uneven skin tone, natural asymmetry, no makeup or barely-there makeup, no digital smoothing, no beauty filter, no airbrushing, no plastic skin. Mature adult facial proportions, no babyface. One person alone, sharp focus on her face, no text, no watermark, no phone or device frame visible, no screen interface, no border.
```

---

## Variants worth rolling

Change one clause, keep everything else identical:

| Variant | Swap in |
|---|---|
| Boba | `a clear plastic cup of brown sugar boba milk tea with a wide straw and visible tapioca pearls` |
| Slushie | `a bright red frozen slushie in a domed clear cup with a spoon straw` |
| Iced coffee | `a plastic Dunkin iced coffee cup, condensation running down it` |
| Softer expression | `a small closed-mouth smirk with her tongue slightly out at one corner, amused rather than posed` |
| Shade | `standing in shade with bright sun behind her, face evenly lit, hard sunlight blowing out the street behind` |

**Dunkin note:** it is on-brand for Boston (BIBLE §4) but brand logos render badly and put
someone else's trademark in your profile picture. Prefer a plain cup.

---

## What to check on the output

1. **Circle-crop test.** Crop it to a circle before deciding. Plenty of good squares lose the
   chin or the top of the head once Instagram rounds them off.
2. **Identity.** Same woman as `ref-1`. Nose bridge, jawline, eye shape.
3. **Age.** Reads mid-twenties. A pout plus a high angle plus summer light is the most
   babyface-prone combination we have shot — this is the one to watch (PROJECT-BRIEF §7).
4. **Skin.** Visible pores and sheen, not airbrushed. Bright sun tempts the model toward a
   beauty-ad finish.
5. **Hands.** One hand holds the cup and the other holds the phone off-frame. Check finger
   count on the cup hand.
6. **Sunglasses.** On top of her head, not over her eyes — the eyes are the identity.

---

## Notes

- **The pout is the risk.** An exaggerated pout drifts toward both babyface and thirst-trap.
  The prompt says `deliberately silly rather than seductive` for that reason; keep that clause.
- **Expression references matter here.** `ref-2` … `ref-4` give the Element expression range;
  without them a strong expression drifts the face (GENERATION-LOG, Element v2 finding).
- This is deliberately warmer and sunnier than the §5 content grade. A profile picture is one
  image a person chose of themselves, so a nice photo is in character. **Do not** carry this
  brightness into feed posts.
