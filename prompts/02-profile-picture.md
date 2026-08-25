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

## Expression variants — roll all four, pick one

Direction: **a bad photo of a good moment.** The energy comes from imperfect capture, not a
held pose — scrunched face, eye shut, tongue out, blown highlights, slight motion blur, shot
from too close. Describe the *mechanics* of the face, never the adjective: "playful" gets a
polite smile, "nose scrunched with one eye squeezed shut" gets the actual thing.

Swap the `EXPRESSION` and `LIGHT` blocks in the base prompt for one of these. Everything else
stays identical.

### A — wink + tongue

```
EXPRESSION: caught mid-goof, not posed. Her left eye is squeezed fully shut in an exaggerated wink while the right stays wide open, her nose is scrunched up wrinkling the bridge, her mouth is open in a wide crooked grin with her tongue sticking out over her lower teeth. Cheeks bunched high, laugh lines showing, eyebrows asymmetrical, one raised higher than the other. Genuinely silly, mid-movement, slightly out of control, not seductive and not cute-posed.
LIGHT: harsh direct summer sun from above, blown-out highlights across her forehead and the bridge of her nose, hard shadow under her chin, mild motion blur on her hair and one side of her face from moving while shooting, slightly missed focus, visible sensor noise. Shot too close so the lens distorts her nose and chin slightly.
```

### B — nose scrunch, eyes shut, mid-laugh

```
EXPRESSION: caught mid-laugh with both eyes squeezed shut into crescents, nose scrunched hard, mouth wide open showing teeth, head tipped back and slightly to one side, chin lifted. Cheeks pushed up into her eyes, whole face creased, double chin from the angle, completely unflattering and completely genuine. Not posed, not aware of the camera in this instant.
LIGHT: harsh direct summer sun, badly blown highlights on her cheekbones and forehead, deep shadow in her eye sockets, strong motion blur from laughing while holding the phone, focus slightly behind her face, heavy sensor noise.
```

### C — squished cheek

```
EXPRESSION: her face pressed and squished against her own raised shoulder, one cheek compressed and pushed up distorting that side of her mouth, one eye half closed by the squash, the other eye looking straight into the lens with a conspiratorial grin. Lips pressed sideways and slightly open. Deliberately silly, physically comic, shot far too close.
LIGHT: harsh direct summer sun, uneven and blown on one side of her face, the squashed side falling into hard shadow, strong lens distortion from the extreme closeness, slight motion blur, missed focus, visible noise.
```

### D — unimpressed deadpan

```
EXPRESSION: completely deadpan straight into the lens, eyebrows flat, mouth a closed unimpressed line, dead-eyed, holding the drink up beside her face like evidence. No smile at all. The joke is the total lack of expression, held a beat too long.
LIGHT: harsh direct summer sun from above, blown highlights on her forehead, hard shadows under her brow and chin, slightly overexposed, visible sensor noise, mild lens distortion from the close high angle.
```

---

## Why these work and a pout does not

The reference direction is not "pretty face pulling a face" — it is **an unflattering photo
somebody posted anyway.** Three things carry that and all three are in the prompts above:

1. **Facial mechanics, not adjectives.** `nose scrunched wrinkling the bridge, cheeks bunched
   high, eyebrows asymmetrical` produces an expression. `playful` produces a polite smile.
2. **Asymmetry.** One eye shut, one brow higher, mouth pushed sideways. Symmetrical faces read
   posed; real candids are lopsided.
3. **Capture failure.** Motion blur, missed focus, blown highlights, lens distortion from
   shooting too close. A technically good photo of a silly face still reads as a photoshoot.
   **This is the part most likely to get dropped — keep it.**

---

## Age warning — sharper for these than for the pout

Scrunched, tongue-out, cheeks-bunched expressions read **younger** than neutral ones, and the
high selfie angle compounds it. This is now the highest babyface risk in the project
(PROJECT-BRIEF §7 is a hard guardrail, not a preference).

Keep `Mature adult facial proportions, no babyface` in every variant, and if any output reads
under 25, add `defined mature jawline, longer facial thirds` and re-roll. **D is the safest**
on this axis; **B is the riskiest.**

---

## Do not attach real people's photos as references

Expression direction can come from anywhere, but reference *images* fed to the model must be
Aasmi's own (`ref-1` … `ref-5`). Attaching a real person's photo alongside them blends that
face into hers — breaking identity consistency and importing a real likeness, which
PROJECT-BRIEF §7 prohibits outright.

---

## Drink variants

| Variant | Swap in |
|---|---|
| Boba | `a clear plastic cup of brown sugar boba milk tea with a wide straw and visible tapioca pearls` |
| Slushie | `a bright red frozen slushie in a domed clear cup with a spoon straw` |
| Iced coffee | `a plain plastic iced coffee cup, condensation running down it` |

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
