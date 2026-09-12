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

**Revised to match generation 1.** Gen 1 is now the consistency anchor for the set: the venue,
light, skin and outfit fit all follow it, and only the pose and expression differ. Six boxes
changed; the chips did not.

| Field | Value |
|---|---|
| 1 Location | free text below |
| 2 Time of Day | **Night** |
| 3 Pose | **Candid** + **Standing** |
| 4 Expression | **Natural** + **Looking Away** |
| 5 Outfit | preset **Athleisure** |
| 7 Format | **9:16**, **4K**, output **4** |

**Location** — changed
```
Inside a bowling alley at night. Lanes recede to her right with lit pins at the far ends and glowing blue lane numbers above them. A long green illuminated banner runs across the back wall behind her. A metal ball return machine at the left edge of the frame, pale wood flooring underfoot and patterned purple carpet in the lower corner. Overhead score monitors across the top of the frame. Cool blue and purple light across the lanes with the green banner as the only warm accent. The monitors and the banner are far enough away and dim enough that their lettering reads only as blurred coloured glow. Shot on a phone with flash: she is lit brightly and evenly and the alley behind her sits a stop or two darker. Deep depth of field, no portrait mode, sensor noise in the shadows, mild over-sharpening, JPEG artifacts.
```

**Pose** — changed (framing only)
```
Standing angled very slightly to one side, shot from about two and a half metres away so she is framed from mid-thigh up and fills roughly three quarters of the frame height. Both arms are down in front of her: her right arm curls around a bowling ball held low against her stomach at waist height, fingers wrapped underneath it. Her left hand rests low on her own hip at the waistband, fingers relaxed. Shoulders soft and slightly rounded, head tipped down and turned a little to one side.
```

**Expression** — changed (skin only)
```
Eyes fully closed, head tipped down and slightly away, lips pushed forward into a soft pout. Calm and dreamy, chin tucked, eyebrows relaxed, unaware of the camera. Natural matte skin with visible pores across her nose and cheeks and only a light sheen on her forehead and cheekbones.
```

**Outfit — custom** — changed
```
Her long dark brown-black hair is loose and down, centre parted, falling over both shoulders and in front of them, slightly wavy with a few flyaway strands at the crown. Oversized light heather-grey hoodie, dropped shoulders, very long sleeves, the hood lying flat behind her neck, a large kangaroo pocket across the front, the hem sitting at the top of her waistband so a narrow band of midriff shows. Matching light heather-grey sweatpants with a visible drawstring and a small solid red embroidered heart on the right thigh. A band of red and white plaid boxer waistband visible above the sweatpants. Small silver stud earring.
```

**Lock hairstyle** — changed
```
Long dark brown-black hair worn loose and down, centre parted, falling over both shoulders, slightly wavy, a few flyaway strands at the crown.
```

**Props** — changed
```
A plain smooth glossy red-orange bowling ball, its surface uniform and unmarked, held low against her stomach.
```

### What changed after generation 2, and why

Gen 2 diverged from gen 1 on six axes. Three of them were caused by this file describing the
*original* reference photo instead of matching the first generation.

| | Gen 1 | Gen 2 | Cause |
|---|---|---|---|
| Mood | Cool blue, green banner accent | Dark, green and magenta neon | 4B Location asked for exactly that |
| Skin | Natural, light sheen | Dewy, wet-looking speculars | 4B Expression asked for `dewy … wet-looking` |
| Framing | Alley visible around her | Noticeably tighter | 4B Pose asked for `close to the camera` |
| Hoodie | Hem at waistband, midriff band | Hangs long, midriff covered | 4B Outfit said `long enough to cover her waist` |
| Ball | Plain and smooth | Marbled, serial and number printed on it | Nothing specified it |
| Venue | Ball return machine, blue lanes | Ball rack, PINZ neon | Different furniture named |

**The hair instruction is reversed on purpose.** The previous revision pushed hard for a tight
bun, because the original photo has one. Both generations came back with hair down anyway, and
gen 1 is now the anchor — so this preset asks for hair **down** to match it. Consistency across
her own posts is worth more than fidelity to a stranger's photograph, and fighting the model
for a bun costs re-rolls on a detail that no longer matters.

**Flash strength is softer here than in revised 4A.** 4A asks for two to three stops of falloff;
this asks for one or two, because that is what gen 1 actually looks like. If the pair is meant
to sit side by side in a grid, 4A should be brought down to match rather than 4B pushed up.

**The ball needed specifying at all.** Left unstated, the model added a marbled finish, a serial
number and a lane number. `Plain … uniform and unmarked` is now explicit, phrased as what the
surface *is* rather than as a list of things to leave off.

**Legible screen text is still unfixed in the outputs.** Both generations rendered readable
signage. The blur clause now present in both Location boxes is the second attempt; if it still
comes through, the next lever is moving the screens out of frame entirely rather than
strengthening the wording.

