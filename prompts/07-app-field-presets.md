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
