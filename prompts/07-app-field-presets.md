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
Inside a bowling alley at night, standing on the approach at the head of a lane. The polished wood lane recedes behind her to the right with lit pins at the far end and glowing blue lane numbers above them. Overhead score monitors run along the top of the frame, one of them playing a music video. A long green illuminated advertising banner along the back wall. Dark ceiling, deep blue and purple neon wash over the walls, a dark ball return unit at the left edge, patterned purple carpet in the foreground. Shot on a phone with direct on-camera flash so she is lit hard and bright and the alley behind falls off fast into dark blue. Deep depth of field, no portrait mode, sensor noise in the shadows, mild over-sharpening, JPEG artifacts.
```

**Pose**
```
Standing straight and square to the camera, weight even on both feet. Her right arm is held out from her body with a bowling ball balanced up at chest height, palm flat underneath it and fingers spread wide, elbow bent. Her left hand rests on her hip, fingers forward, elbow pushed out. Shoulders level, head straight, completely still.
```

**Expression**
```
Calm and neutral, lips together, no smile, eyebrows relaxed, chin level, eyes looking straight down the lens.
```

**Outfit — custom**
```
Oversized light heather-grey hoodie, dropped shoulders, very long sleeves bunched at the wrists, hem sitting high enough to show a sliver of bare midriff. Matching light heather-grey sweatpants with a visible drawstring and a small red embroidered heart motif on the left thigh. The red and white plaid waistband of boxer shorts showing above the sweatpants. Small silver stud earrings.
```

**Lock hairstyle**
```
Dark brown hair, centre parting, pulled back tight and smooth into a high rounded bun at the back of the head, a few fine wispy strands loose at the temples.
```

**Props**
```
A bright glossy red-orange bowling ball held up in her right hand, a hard specular highlight on its surface from the flash.
```

### Notes on this one

**The signage is described, not transcribed.** The reference has Thai text on the back-wall
banner. Foreign-script text is where these models produce garbage, and reproducing a real
brand's advertisement serves no purpose, so it is specified as `a long green illuminated
advertising banner` and left at that. Same reasoning as leaving the Brand Deal slots empty.

**Aspect mismatch.** The reference is roughly 3:4; the app offers only 9:16 or 16:9. At 9:16 she
will sit smaller in a taller frame with extra floor and ceiling. Shoot 9:16 and crop to 4:5,
rather than trying to fight the framing in the pose box.

**The hand is the hard part.** Fingers spread flat under a sphere fails more often than
anything else in this frame. Check it at full size on every output before picking one.

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

