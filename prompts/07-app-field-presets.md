# Prompt 07 — Field presets for the form-based generator

This app builds its own prompt by concatenating the fields. Rules that follow from that:

1. **One idea per box.** Location = place. Pose = body. Expression = face. Outfit = clothes.
   Repeating content across boxes creates contradictions the model resolves at random.
2. **Capture realism goes in Location**, appended after the scene. There is no camera field, and
   Location is the box treated as scene context.
3. **No face lock, no body spec anywhere.** The app has no field for them, so identity comes
   entirely from the character it has stored. If outputs drift, the fix is that stored
   character — not these boxes.
4. **Format: 4K, not 2K.** Same cost per image in every tool we have measured. Output 4 gives
   choice without wading.
5. **Leave the Brand Deal prop slots empty** until a deal is real. A fabricated product
   placement is a misrepresentation, and it is the same exposure as the disclosure question in
   INSTAGRAM-SETUP §12.

---

## Preset 1 — Hotel room, arrival night (matches what is currently loaded)

| Field | Value |
|---|---|
| 1 Location | chip **Hotel Room** |
| 2 Time of Day | chip **Night** |
| 3 Pose | chip **Candid** + toggle **Sitting** |
| 4 Expression | toggle **Looking Away** |
| 5 Outfit | preset **Cozy** |
| 7 Format | **9:16**, **4K**, output **4** |

**Location — free text**
```
A small mid-range hotel room, unpacked cabin suitcase open on the luggage rack, coat over the desk chair, curtains half drawn on a city window with streetlights and other lit windows behind. Warm bedside lamp on, overhead light off. Shot on an iPhone by a friend, deep depth of field, no portrait mode, slight sensor noise in the shadows, over-sharpening halos, JPEG artifacts, horizon a little tilted.
```

**Pose — free text**
```
Sitting on the end of the bed still half in her outdoor clothes, one shoe off and one still on, leaning forward with her forearms on her knees and her hands loose between them. Shoulders dropped, spine relaxed, mid-exhale at the end of a long travel day.
```

**Expression — free text**
```
Tired but content, a small closed-mouth smile that is not quite for the camera, eyes slightly heavy, eyebrows relaxed, looking off toward the window.
```

**Outfit — custom**
```
Oversized cream knit sweater with the sleeves pushed up over a white cotton tank, straight-leg mid-wash jeans, white socks, one white low-top sneaker still on. Thin gold chain with a small round coral-and-turquoise pendant, small thick gold huggie hoops, matching coral-and-turquoise ring.
```

**Lock hairstyle**
```
Dark brown-black hair in a loose low bun, middle part, flyaway strands at her temples and nape, a few pieces fallen loose around her face.
```

**Props — free text**
```
A half-unpacked cabin suitcase open on the floor, a hospital lanyard badge on the bedside table, a paper cup of tea gone cold.
```

---

## Preset 2 — End of night shift (pillar 1, the differentiated one)

| Field | Value |
|---|---|
| 1 Location | free text below |
| 2 Time of Day | **Morning** |
| 3 Pose | **Wall Lean** + **Standing** |
| 4 Expression | **Looking Away** |
| 5 Outfit | **Casual** |
| 7 Format | 9:16, 4K, output 4 |

**Location**
```
Hospital staff car park just after dawn, rows of parked cars, a low concrete building behind with lit windows, sodium lamps still on against a pale grey sky, damp asphalt. Shot on an iPhone, deep depth of field, no portrait mode, flat overcast light, sensor noise, over-sharpening halos, JPEG artifacts, frame slightly off level.
```

**Pose**
```
Leaning back against the driver's door of her car, weight on one hip, car keys hooked on one finger, the other hand holding a coffee at her side. Not moving, just stopped.
```

**Expression**
```
Blank with tiredness, mouth relaxed and closed, eyes unfocused somewhere past the camera, the specific slackness of someone twelve hours in.
```

**Outfit — custom**
```
Navy scrub top and matching scrub trousers under an open black puffer jacket, white trainers, a hospital ID badge on a lanyard. Thin gold chain with a small round coral-and-turquoise pendant, small gold huggie hoops.
```

**Lock hairstyle**
```
Dark brown-black hair scraped into a low bun that has loosened over the shift, middle part, loose strands stuck to her temples.
```

**Props**
```
A paper coffee cup and car keys.
```

---

## Preset 3 — Boston street, night flash (pillar 4)

| Field | Value |
|---|---|
| 1 Location | free text below |
| 2 Time of Day | **Night** |
| 3 Pose | **Walking** + **Standing** |
| 4 Expression | **Looking at Camera** |
| 5 Outfit | **Streetwear** |
| 7 Format | 9:16, 4K, output 4 |

**Location**
```
A Boston side street at night, brick sidewalk, a lit storefront and neon sign behind her, parked cars, bare trees, wet pavement reflecting the lights. Shot on an iPhone with direct on-camera flash so she is lit hard and the street behind falls off fast into dark blue. Deep depth of field, no portrait mode, hard flash shadow behind her, sensor noise, over-sharpening halos, JPEG artifacts, frame slightly tilted.
```

**Pose**
```
Caught mid-step on the sidewalk, half turned back toward the camera over one shoulder, hands in her jacket pockets, one foot still lifting.
```

**Expression**
```
Caught off guard and starting to laugh, mouth just opening, eyebrows up, eyes straight into the lens.
```

**Outfit — custom**
```
Black leather bomber over a white ribbed cropped tank, straight-leg dark jeans, white low-top sneakers. Thin gold chain with a small round coral-and-turquoise pendant, small thick gold huggie hoops, matching ring.
```

**Lock hairstyle**
```
Dark brown-black hair loose and slightly windblown, middle part, a few strands across her face.
```

**Props**
```
Leave empty.
```

---

## Preset 4A — Bowling alley, ball raised, straight to camera

**Revised after run 1.** The first version missed on hair, ball height, framing, flash falloff
and legible signage. What changed and why is in the notes below.

| Field | Value |
|---|---|
| 1 Location | free text below (no chip matches) |
| 2 Time of Day | **Night** |
| 3 Pose | **Front-Facing** + **Standing** |
| 4 Expression | **Natural** + **Looking at Camera** |
| 5 Outfit | preset **Athleisure** |
| 7 Format | **9:16**, **4K**, output **4** |

**Location**
```
Inside a bowling alley at night, standing on the approach at the head of a lane. The polished lane recedes behind her with lit pins at the far end and glowing lane numbers above them, a dark ball return unit at the left edge, patterned purple carpet in the foreground. Overhead score monitors and an illuminated banner along the back wall, all of them far enough away and dim enough that their lettering reads only as blurred coloured glow. Shot on a phone with direct on-camera flash: she is lit hard and bright and the flash falls off sharply behind her, so the lanes are two to three stops darker than she is and the corners of the frame go almost black. Deep depth of field, no portrait mode, sensor noise in the shadows, mild over-sharpening, JPEG artifacts.
```

**Pose**
```
Standing straight and square to the camera, weight even on both feet, shot from about three metres away so her whole body from head to below the knees fits in frame and she fills roughly two thirds of the frame height with alley visible around her. Her right upper arm hangs down close to her side and her forearm is horizontal, so the bowling ball sits level with her chest, well below her chin, held out clear of her body. Her palm is flat underneath the ball taking its weight from below, fingers spread wide across the underside. Her left hand rests on her hip with the fingers forward and the elbow pushed out. Shoulders level, head straight, completely still.
```

**Expression**
```
Calm and neutral, lips together, no smile, eyebrows relaxed, chin level, eyes looking straight down the lens.
```

**Outfit — custom**
```
Her hair is scraped back tight and smooth from the hairline into a high rounded bun, her neck and shoulders completely clear, with only a few fine wisps loose at the temples. Oversized light heather-grey hoodie, dropped shoulders, very long sleeves bunched at the wrists, the hem sitting low at the top of her waistband so only a narrow strip of skin shows. Matching light heather-grey sweatpants with a visible drawstring and a small red embroidered heart on one thigh. A narrow band of red and white plaid boxer waistband just visible above the sweatpants. Small silver stud earrings.
```

**Lock hairstyle**
```
Dark brown hair scraped back tight and smooth from the hairline into a high rounded bun at the back of the head, neck and shoulders completely clear of hair, a few fine wisps at the temples.
```

**Props**
```
A bright glossy red-orange bowling ball held out level with her chest, a hard specular highlight on its surface from the flash.
```

### What changed after run 1

**Hair — the worst miss, and the reason for a deliberate rule break.** The Lock hairstyle field
alone did not hold: the output came back with her hair down over her shoulders. Hair is now
stated in **both** Lock hairstyle and at the front of the Outfit box. That violates the
one-idea-per-box rule at the top of this file, and it is intentional — Outfit is the most
reliably honoured descriptive box, and a field that demonstrably fails needs a second carrier.

The wording also changed from naming the bun to describing the **whole head state**: `her neck
and shoulders completely clear`. Asking for a bun leaves loose hair unaddressed, so the model
supplies it; describing what the neck and shoulders look like closes the gap without a negation.

**Ball height — fixed by arm geometry, not by naming a height.** `Chest height` produced a ball
up beside her head. The reliable lever is the joints: `her right upper arm hangs down close to
her side and her forearm is horizontal`. That constrains the height mechanically. `Palm flat
underneath taking its weight from below` fixes the side-grip.

**Framing — fixed with a distance and a fraction.** `Framed from mid-shin up` was ignored. `Shot
from about three metres away … she fills roughly two thirds of the frame height` gives two
concrete quantities instead of a crop name the app has no field for.

**Flash falloff — fixed with stops.** The output was evenly lit with a well-exposed background,
which killed the flash look. `Two to three stops darker than she is` is a measurable
instruction; `falls off fast` is a vibe.

**Legible signage — fixed by distance and dimness.** The output rendered `BOOK YOUR PARTY`, a
real song credit and a venue name. Beyond looking wrong, fabricated third-party brand and
artist content in a commercial post is the same exposure as the Brand Deal slots. The fix is
positive: the signage is `far enough away and dim enough that their lettering reads only as
blurred coloured glow`, rather than asking for no text.

**Midriff.** The output showed a wide band of skin and a very prominent waistband. `The hem
sitting low at the top of her waistband so only a narrow strip of skin shows` pins it.

---

## Preset 4B — Bowling alley, ball low, eyes closed

Same alley, same outfit, different frame. Everything except Outfit changes from 4A.

| Field | Value |
|---|---|
| 1 Location | free text below |
| 2 Time of Day | **Night** |
| 3 Pose | **Candid** + **Standing** |
| 4 Expression | **Natural** + **Looking Away** |
| 5 Outfit | preset **Athleisure** |
| 7 Format | **9:16**, **4K**, output **4** |

**Location**
```
Inside a bowling alley at night, standing at the head of a lane. Lanes recede behind her with lit pins at the far ends and glowing lane numbers above them. A bright green LED strip runs along the top of the back wall with large illuminated green display lettering below it, and overhead score monitors across the top of the frame. A rack of multicoloured bowling balls at the lower left edge. Dark blue and green neon wash, magenta light spilling across the floor in the foreground. Shot on a phone with flash so she is lit brightly and the alley behind falls away into dark blue and green. Deep depth of field, no portrait mode, sensor noise in the shadows, mild over-sharpening, JPEG artifacts.
```

**Pose**
```
Standing close to the camera and filling the frame from mid-thigh up, angled very slightly to one side. Both arms are down in front of her: her right arm curls around a bowling ball held low against her stomach at waist height, fingers wrapped underneath it. Her left hand rests low on her own hip at the waistband, fingers relaxed. Shoulders soft and slightly rounded, head tipped down and turned a little to one side.
```

**Expression**
```
Eyes fully closed, head tipped down and slightly away, lips pushed forward into a soft pout. Calm and dreamy, chin tucked, eyebrows relaxed, unaware of the camera. Dewy skin with bright wet-looking highlights on her cheekbones, nose, chin and brow bones, visible pores across her nose and cheeks.
```

**Outfit — custom**
```
Oversized light heather-grey hoodie, dropped shoulders, very long sleeves, the hood bunched loosely at the back of her neck, a large kangaroo pocket across the front, hanging long enough to cover her waist. Matching light heather-grey sweatpants with a visible drawstring and a small red embroidered heart motif on the right thigh. The red and white plaid waistband of boxer shorts showing at her hip. A small silver stud earring.
```

**Lock hairstyle**
```
Dark brown hair, centre parting, pulled up into a small messy high bun with loose wispy strands escaping around her face, at her temples and down the back of her neck.
```

**Props**
```
A bright glossy red-orange bowling ball held low against her stomach, and a rack of multicoloured bowling balls at the edge of the frame.
```

### What changed from 4A, and why

| | 4A | 4B |
|---|---|---|
| Ball | Raised at chest height, palm flat underneath, fingers spread | Held low against her stomach, arm curled round it |
| Free hand | On her hip, elbow out | Low on her hip at the waistband, arm down |
| Eyes | Straight down the lens | Fully closed |
| Head | Level and square | Tipped down and turned aside |
| Hair | Tight smooth bun | Small messy bun, strands escaping |
| Midriff | Sliver visible | Covered — the hoodie hangs longer |
| Framing | Mid-shin up | Mid-thigh up, closer |
| Background | Blue neon | Green LED wall and lettering, magenta floor spill |

**The framing change lives in the Pose box.** The app has no zoom or shot-size control, so
`close to the camera and filling the frame from mid-thigh up` is the only place to ask for it.

**The dewy skin lives in the Expression box.** There is no skin field either. Expression is the
closest lane, being the only face-facing box, so the sheen and pore clauses ride there.

**Closed eyes are the risk.** These models drift toward open eyes because almost all their
training portraits have them. If they come back open, strengthen to `both eyelids fully closed,
lashes resting on her cheeks` before changing anything else.

**Wall lettering is described, not spelled.** The reference shows readable words on the green
displays. Asking for specific words produces mangled glyphs, so the box asks for `large
illuminated green display lettering` and leaves the content to the model.

