# Prompt 02 — Profile picture (Aasmi Adhikari)

**Model:** `seedream_v4_5` · **Aspect:** `1:1` · **Quality:** 4K / basic · **Unlimited:** on
**References:** attach `ref-1` … `ref-5` from the PFP-REFS bundle (up to 14 allowed)

Run this in the Higgsfield web app, where Unlimited is available. If running via MCP instead,
drop the attachments and embed `<<<83ab454a-a85a-4814-8459-c10fc7e493aa>>>` at the start.

**Why 1:1** — Instagram crops the profile picture to a circle from a square. A 9:16 selfie
loses the sides and pushes her face small. Shoot 1:1 and the circle crop keeps her face
filling the frame. If you also want it as a grid post, run a second pass at 4:5.

---

## The prompt — paste this

**2,971 characters.** Default expression is **A (wink + tongue)**; for B, C or D swap the
`EXPRESSION` and `LIGHT` blocks only, keeping every other block intact.

```
Full-bleed square photo, edge to edge.

CAPTURE: iPhone 17 Pro Max front camera, arm's length above her head, angled down. Ultra-wide lens close up, nose and chin slightly enlarged. Deep depth of field, street behind stays semi-sharp, no portrait mode, no background blur. Computational HDR: shadows lifted and flat, highlights clipping on her forehead. Faint over-sharpening halos on jaw and hair. Noise reduction smearing shadow detail, luminance noise in mid-tones. Cool white balance, slight chromatic aberration, JPEG artifacts on high-contrast edges, mild flare, lens smudge in one corner.

SUBJECT: the same woman as the reference images, exact face, bone structure, nose, jawline, eye shape and identity unchanged. 25-year-old Nepali-American woman on a busy sunny summer Boston street, brick sidewalk and storefronts behind. Holding a tall clear cup of iced lemonade with a straw near her chin, condensation on it. White ribbed tank top, thin gold hoops, thin gold chain with a small round pendant, coral orange centre stone in a turquoise ring. Black sunglasses pushed up on her head. Long black-brown hair loose with flyaways, strands stuck to her neck.

BACKGROUND: ordinary strangers behind her, none aware of the camera. One walking past mid-stride, cut off by the frame edge and motion-blurred. Two more at an outdoor cafe table further back, a cyclist passing. All turned away, in profile or cropped, softened by distance and movement, faces indistinct. Parked cars, a trash bin.

EXPRESSION: caught mid-goof, not posed. Left eye squeezed shut in an exaggerated wink, right eye wide open, nose scrunched wrinkling the bridge, mouth open in a wide crooked grin with her tongue out over her lower teeth. Cheeks bunched high, eyebrows asymmetrical, one higher. Genuinely silly, mid-movement, not seductive, not cute-posed.

BODY: 167 cm, slim narrow frame, 62 cm waist, 100 cm hips, 78 cm underbust. Full E cup breasts, clearly full on a narrow ribcage. Narrow shoulders, slim arms. She is not a heavier woman overall.

LIGHT: harsh direct summer sun from above, blown highlights on forehead and nose bridge, hard shadow under her chin, mild motion blur on her hair, focus slightly missed.

FRAMING: face fills most of the frame, roughly centred with slight headroom so a circular crop keeps it whole. Deliberately imperfect: horizon tilted, head off-centre, one shoulder cut by the frame edge. Not symmetrical, not well-composed.

REALISM: unretouched. Visible pores and skin texture, faint sweat sheen on nose and upper lip, uneven skin tone, natural asymmetry, flyaway hairs across her face. Barely-there makeup. No digital smoothing, no beauty filter, no airbrushing, no plastic or waxy skin. Mature adult facial proportions, no babyface, no childlike features.

She is the only person in focus and the only version of her in frame. No duplicate or second copy of her face. No text, no watermark, no phone or device frame, no screen interface, no border.
```

### Handling background people

An empty summer sidewalk in a major city reads staged — emptiness is itself an AI tell. But
background faces are where these models fail hardest, producing melted or duplicated
features that ruin an otherwise good frame.

The `BACKGROUND` block avoids both by making every stranger **turned away, in profile, or
cropped by the frame** and softened by motion and distance. That is also exactly what a real
phone photo does at this depth of field, so the fix costs no realism.

The closing line changed from `One person alone, no other people` to `She is the only person
in focus and the only version of her in frame. No duplicate or second copy of her face.` The
old wording would have cancelled the crowd; the new wording still blocks the real risk, which
is the model rendering a second Aasmi.

### What was cut, and what must never be

Trimmed from the long version: adjective stacking, repeated negatives, and prose connectives.
Nothing load-bearing was removed.

**Never cut these, whatever the character budget:**

1. `Full-bleed square photo, edge to edge` — the positive framing clause. It is the only
   thing that reliably suppresses rendered phone bezels and inset thumbnails; negatives do
   not work (GENERATION-LOG runs 008–009).
2. **The whole BODY block.** The Element biases the silhouette but does not hold it; every
   shot that drifted was one where this block was missing.
3. `Deep depth of field … no portrait mode, no background blur` — the loudest AI tell in a
   selfie.
4. `Mature adult facial proportions, no babyface` — PROJECT-BRIEF §7 hard guardrail, and this
   expression is the highest-risk one in the project.
5. The identity clause naming the reference images.

---

## Why the phone spec is written this way

Naming a camera model does very little on its own — the model has no reliable idea what an
iPhone 17 Pro Max file looks like. **The artifacts do the work**, and they are what separates
a phone photo from a render:

| Artifact | What it kills |
|---|---|
| Deep depth of field, no portrait mode | Creamy background blur is the loudest AI/DSLR tell in a selfie |
| Computational HDR, lifted flat shadows | Renders have dramatic, physically-correct falloff; phones do not |
| Over-sharpening halos | Real phone processing artifact; renders are cleanly sharp |
| Noise reduction smear + residual noise | Renders are either clean or fake-grainy, never both |
| Front-lens distortion at arm's length | Renders keep ideal facial proportions |
| JPEG artifacts, chromatic aberration, lens smudge | Renders have no capture history |
| Tilted horizon, shoulder cut off | Renders are well-composed by default |

If the output still reads AI, **strengthen these before touching anything else.** The failure
is almost always too clean, not wrong content.

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
