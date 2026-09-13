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

## Background swap — take the background from a second image (Nano Banana Pro edit)

**Type:** image edit · **Model:** `nano_banana_pro`
**Attach two images, in this order:** first the shot being fixed, second the shot whose
background is correct. Order is load-bearing — the prompt addresses them by position.

When two shots in a set land in different venues, editing one is cheaper and safer than
re-rolling it: a re-roll puts the face back in play, and the face is what this project has spent
the most effort locking. Fix the half that is wrong.

**1542 characters.**

```
Two images are attached.

The FIRST image is the photograph being edited. The woman in it stays exactly as she is, pixel for pixel: her face, her closed eyes, her downturned head, her hair, her grey hoodie and sweatpants, the plaid waistband, the red heart on her thigh, her hands, the bowling ball she is holding, her position and scale in the frame, and the light falling on her. She is untouched, and she remains the only person in the finished picture. The crop and aspect ratio stay the same.

The SECOND image is a background reference only. Take from it the bowling alley itself, exactly as photographed: the lanes and the angle they run at, the lit pins, the glowing lane numbers, the green banner across the back wall, the screens mounted above it, the ball return machine at the left edge, the pale wood approach flooring, the purple patterned carpet, the deep blue and purple light and the dark ceiling. Reproduce that space as it would look standing empty, and put it behind the woman from the first image.

The one element free to differ is the television. The music video playing on it can show any ordinary crowd scene with indistinct, unrecognisable performers.

Fit the background to her. Keep the first image's eye level, lens and perspective, with the lanes receding at the angle her stance already implies and her feet meeting the floor where they already do. Carry the first image's grain, noise and exposure across the whole frame, keep the background slightly softer than she is, and let it sit one to two stops darker.
```

### The hard part is role separation

Both attached images contain the same woman. Left to itself the model blends them — her pose
drifts toward the second image, or a second copy of her appears down the lane. Three things
prevent it:

**Addressing the images by position, repeatedly.** `The FIRST image is the photograph being
edited` and `The SECOND image is a background reference only`, then every subsequent instruction
names which image it draws from. Vague reference is what produces blending.

**`Reproduce that space as it would look standing empty.`** This is the clause that removes the
woman from the second image, and it is phrased positively — describing the room as empty rather
than instructing the model to exclude her. Naming her to leave her out is the same trap as
naming a mole to preserve it (BIBLE §5b): the negation nominates its subject.

**`She remains the only person in the finished picture.`** A backstop for the same failure,
stated as the desired end state.

### The rest

**`Fit the background to her`** sets the direction of adjustment. Without it the model will
happily reproject her to suit the reference frame, which defeats the point of the edit.

**Camera match is tied to what is already in the first frame** — its eye level, the angle her
stance implies, where her feet already meet the floor — rather than to absolutes. Same
comparative-over-absolute rule as everywhere else in this repo.

**The background stays softer and a stop or two darker than she is.** Rebuilt backgrounds render
crisper than the subject by default, and that reads as a composite immediately.

**The television is deliberately unpinned.** The earlier generation rendered a real music video
with recognisable artists and their song credit. An indistinct crowd scene gets the screen glow
without putting real likenesses into a commercial post — the same call as the Brand Deal slots.

### What to check

1. **Her face is untouched** — compare at full size against the first image before anything else.
2. **No second version of her** anywhere down the lanes. This is the characteristic failure here.
3. **Her pose has not drifted** toward the second image's pose.
4. **Floor line** — her feet meet the new floor at the same height and angle they did.
5. **Background is softer than she is**, not sharper.
6. **Screens** stay glow rather than legible text.

### If it blends anyway

Fall back to describing the background in words with only the first image attached. It is less
accurate but it cannot blend, because there is no second person in the context to blend with.

---

## Preset 5 — Glow bowling, ball raised (a separate night)

Same outfit, **different venue and different light**. This does not belong to the 4A/4B set:
that pair is flash-lit in a blue-and-green alley, this is ambient neon in a magenta glow-bowl.
Treat it as its own post rather than trying to match it to generation 1.

| Field | Value |
|---|---|
| 1 Location | free text below |
| 2 Time of Day | **Night** |
| 3 Pose | **Hip Pop** + **Standing** |
| 4 Expression | **Natural** + **Looking Away** |
| 5 Outfit | **Athleisure** — unchanged from 4A/4B |
| 7 Format | **9:16**, **4K**, output **4** |

**Location** — changed
```
Inside a neon glow-bowling alley at night, standing out on the pale wood lane approach. Lanes run away on both sides of her, their surfaces wet-looking and streaked with reflected magenta and blue. Large LED video walls span the back wall above the pin decks showing rippling liquid patterns in hot pink and electric blue, an illuminated venue logo glowing at the centre, pale lane numbers along the top. A white cylindrical pillar at the left. The ceiling washed deep violet. Lit only by the venue's own neon, with no flash and no camera light: a heavy magenta and blue cast falls across her grey clothes and the floor, deep shadow fills everywhere the neon does not reach, and the brightest things in the frame are the screens and the lanes rather than her. Shot on a phone in low light, with visible grain and colour noise, slightly soft focus, muddy shadows, deep depth of field, no portrait mode.
```

**Pose** — changed
```
Standing out on the lane approach, her whole body in frame from head to shoes, shot from about six metres away so she occupies roughly half the frame height with a wide expanse of glowing lanes and floor around her. Her right arm is raised high and almost straight above her head, the bowling ball balanced up on her open palm and fingertips. Her left hand rests on her hip at the waistband, elbow out. Her weight is on one leg with the other relaxed and turned slightly inward, hips tipped to one side, her right shoulder pulled up by the reach and her left shoulder dropped.
```

**Expression** — changed
```
Head tipped down and turned away from the raised ball, chin toward her shoulder, eyes lowered almost closed, a small closed-mouth private smile. Quiet and pleased with herself, unhurried, completely unaware of the camera.
```

**Lock hairstyle** — optional, see below
```
Dark brown-black hair scraped back and twisted into a small high topknot bun, a few loose strands escaping at her nape and temples.
```

### The mood is the ambient light, and that is the whole change

Every other preset in this file specifies **flash**. This one specifies its absence, and that
single difference produces most of the look:

- **She is not the brightest thing in the frame.** Flash makes the subject brightest and drops
  the room away; ambient neon does the opposite. `The brightest things in the frame are the
  screens and the lanes rather than her` is the clause that inverts it.
- **The colour cast lands on her.** Under flash her grey hoodie stays grey. Under neon it takes
  magenta and blue, which is what ties her into the room.
- **Low light brings its own artifacts** — grain, colour noise, soft focus, muddy shadows. These
  replace the flash artifacts, they do not stack with them.

**Distance carries the mood as much as the light.** At roughly half the frame height with lanes
running away on both sides, the room is the subject and she is a figure in it. Shot close, the
same pose is just a person holding a ball.

### On the hair

The reference has it up in a topknot; the 4A/4B set settled on hair down. Since this is a
separate night at a separate venue, either works — the Lock hairstyle box above gives the
topknot. Leave the box on the loose-hair text instead if you would rather her hair stay
constant across every post regardless of venue.

### What to check

1. **The arm.** A raised arm with a heavy ball balanced on an open palm is the failure point.
   Check the wrist angle, the finger count, and whether the ball reads as resting rather than
   glued.
2. **She is not flash-lit.** If she comes out bright against a dark room, the ambient clause
   lost — strengthen `lit only by the venue's own neon` and move it to the front of the box.
3. **Colour cast on her clothes.** Grey clothes that stayed neutral grey mean the light did not
   land.
4. **Scale** — roughly half the frame height, lanes visible both sides.
5. **Shoes and feet.** Full-length framing puts them in play for the first time in this set.

