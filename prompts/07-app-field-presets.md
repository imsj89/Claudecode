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

**Anchored to generation 1.** Location, Outfit and Lock hairstyle are byte-identical to 4B —
only Pose, Expression and the ball's position differ. That is what makes the two read as one
shoot rather than two.

| Field | Value |
|---|---|
| 1 Location | free text below (no chip matches) |
| 2 Time of Day | **Night** |
| 3 Pose | **Front-Facing** + **Standing** |
| 4 Expression | **Natural** + **Looking at Camera** |
| 5 Outfit | preset **Athleisure** |
| 7 Format | **9:16**, **4K**, output **4** |

**Location** — shared with 4B
```
Inside a bowling alley at night. Lanes recede to her right with lit pins at the far ends and glowing blue lane numbers above them. A long green illuminated banner runs across the back wall behind her. A metal ball return machine at the left edge of the frame, pale wood flooring underfoot and patterned purple carpet in the lower corner. Overhead score monitors across the top of the frame. Cool blue and purple light across the lanes with the green banner as the only warm accent. The monitors and the banner are far enough away and dim enough that their lettering reads only as blurred coloured glow. Shot on a phone with flash: she is lit brightly and evenly and the alley behind her sits a stop or two darker. Deep depth of field, no portrait mode, sensor noise in the shadows, mild over-sharpening, JPEG artifacts.
```

**Pose** — differs
```
Standing straight and square to the camera, weight even on both feet, shot from about two and a half metres away so she is framed from mid-thigh up and fills roughly three quarters of the frame height. Her right upper arm hangs down close to her side and her forearm is horizontal, so the bowling ball sits level with her chest, well below her chin, held out clear of her body. Her palm is flat underneath the ball taking its weight from below, fingers spread wide across the underside. Her left hand rests on her hip with the fingers forward and the elbow pushed out. Shoulders level, head straight, completely still.
```

**Expression** — differs
```
Calm and neutral, lips together, no smile, eyebrows relaxed, chin level, eyes looking straight down the lens. Natural matte skin with visible pores across her nose and cheeks and only a light sheen on her forehead and cheekbones.
```

**Outfit — custom** — shared with 4B
```
Her long dark brown-black hair is loose and down, centre parted, falling over both shoulders and in front of them, slightly wavy with a few flyaway strands at the crown. Oversized light heather-grey hoodie, dropped shoulders, very long sleeves, the hood lying flat behind her neck, a large kangaroo pocket across the front, the hem sitting at the top of her waistband so a narrow band of midriff shows. Matching light heather-grey sweatpants with a visible drawstring and a small solid red embroidered heart on the right thigh. A band of red and white plaid boxer waistband visible above the sweatpants. Small silver stud earring.
```

**Lock hairstyle** — shared with 4B
```
Long dark brown-black hair worn loose and down, centre parted, falling over both shoulders, slightly wavy, a few flyaway strands at the crown.
```

**Props** — differs only in where the ball sits
```
A plain smooth glossy red-orange bowling ball, its surface uniform and unmarked, held out level with her chest.
```

### Why 4A was re-anchored

An earlier revision pushed 4A toward the original reference photograph — tight bun, two to
three stops of flash falloff, no ball surface spec. That was correct while the stranger's photo
was the target. Once generation 1 became the anchor it stopped being correct: running that
version would have produced a third distinct look instead of a matching pair.

**The rule for any multi-shot set:** the boxes that carry venue, light, wardrobe and hair are
byte-identical across every preset in the set, and only Pose and Expression change. Same
principle as prompt 05. A set drifts the moment a shared box is edited for one shot and not the
others.

**One judgement call left in.** Generation 1 put the ball up beside her head; this keeps the
corrected chest-height geometry, since fixing that height is what you asked for before gen 1
became the anchor. If you would rather match gen 1 exactly, change the Pose box to `her upper
arm raised so the ball sits level with her ear, gripped from the side` and drop the flat-palm
clause.

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

---

## Background swap — matching one generation's set to another (Nano Banana Pro edit)

**Type:** image edit, not a field preset · **Model:** `nano_banana_pro`
**Input:** the generation whose background is wrong. Attach that image only.

When two shots in a set land in visibly different venues, editing the background of one is
cheaper and safer than re-rolling it: a re-roll puts the face back in play, and the face is the
thing this project has spent the most effort locking. Fix the half that is wrong.

**1843 characters.**

```
Keep the woman in this photograph exactly as she is, pixel for pixel: her face, her closed eyes, her downturned head, her hair, her grey hoodie and sweatpants, the plaid waistband, the red heart on her thigh, her hands, the bowling ball she is holding, her position and scale in the frame, and the light falling on her. She is untouched, and she is the only person in the frame. The crop and aspect ratio stay the same.

Rebuild everything behind her as this bowling alley:

Lanes running away to her right, brightly lit, with rows of white-blue pins at the far ends and large pale lane numbers glowing above them in sequence. A long dark green banner runs horizontally across the back wall behind her at about shoulder height, carrying pale soft-focus lettering and a faint speckled starfield texture. Mounted high above the banner, three flat screens: a large purple scoreboard on the left showing a mostly empty scoring grid, a television in the middle playing a music video, and the edge of a third dark screen at the right.

At the left edge of the frame, a dark metal ball return machine with a small control panel. Underfoot, pale honey-coloured wood approach flooring, with dark purple patterned carpet filling the lower left corner.

Deep blue and purple light washing the lanes, the green banner the only warm accent, the ceiling above it dark. The background sits one to two stops darker than she is.

Match her camera exactly: the same eye level, the same lens and perspective, the lanes receding at the angle her stance already implies, her feet meeting the floor where they already do. The new background carries the same grain, noise and softness as the rest of the photograph and stays slightly less sharp than she is.

The music video on the television shows an ordinary crowd scene with indistinct, unrecognisable performers.
```

### How it is built

**Preservation is a positive list, and it comes first.** Every element of her is named as a
thing that *stays*, never as a thing to avoid changing. `Do not change her hair` nominates her
hair for editing; `her hair … she is untouched` does not (BIBLE §5b). The prompt contains no
negation at all — verified before use.

**`She is the only person in the frame`** is doing real work. Background rebuilds are where a
second copy of the subject appears, usually small and further down the lane.

**The camera-match paragraph is the part most often left out.** A rebuilt background that
ignores the original lens sits behind the subject like a backdrop. Tying it to things already
in the frame — `the same eye level`, `the angle her stance already implies`, `her feet meeting
the floor where they already do` — is what makes it read as one photograph. Same
comparative-over-absolute rule as everywhere else.

**Sharpness and grain are specified, and the background is asked to stay *less* sharp than
she is.** A rebuilt background typically renders crisper than the subject it sits behind, which
reads instantly as a composite.

**The television is deliberately unpinned.** Reproducing the exact programme is both hard and
undesirable: the earlier generation rendered a real music video with recognisable artists and
their song credit. `An ordinary crowd scene with indistinct, unrecognisable performers` gets the
screen-glow without putting real people's likenesses into a commercial post — the same call as
the Brand Deal slots and the Thai banner.

**Signage lettering is described, not spelled.** `Pale soft-focus lettering` gets the shape of a
banner without demanding glyphs the model will mangle.

### What to check

1. **Her face is untouched** — compare at full size against the input before anything else.
2. **No second version of her** anywhere down the lanes.
3. **Floor line** — her feet meet the new floor at the same height and angle they did.
4. **Background is softer than she is**, not sharper.
5. **Perspective** — the lanes converge toward a vanishing point consistent with her scale.
6. **Screens** stay glow rather than legible text.

