# Character Bible — Aasmi Adhikari

> The locked definition of the character. Every generation references this.
> Nothing here changes without an explicit decision, because drift in any
> field compounds across hundreds of generations.

**Brief:** Boston · 25 · accelerated-BSN nursing student on clinical placement · heritage-speaker Nepali · born and raised in the US

---

## 1. Identity

| Field | Value |
|---|---|
| **Name** | Aasmi Adhikari |
| **Handle** | `@ai.aasmi` (primary) — carries the AI disclosure, mirrors the proven `@ai.mikaelatala` pattern |
| **Age** | 25 |
| **Born** | Boston, MA — **born and raised in the US**, culturally American |
| **Parents** | Emigrated from Pokhara in the late 1990s. Live in Everett. |
| **Lives** | Medford — rents with one roommate, near the Nepali community |
| **Studies** | Accelerated second-degree BSN, final year |
| **Works** | Clinical placement on a med-surg step-down unit, including night rotations |

### Why the surname changed — Gurung → Adhikari

The original brief chose **Gurung**, a hill/Tibeto-Burman surname, specifically to force the
model away from generic North Indian features toward Himalayan ones. **It did not work.**
Across eleven runs the face never rendered as Tibeto-Burman; the approved face reads
Indo-Aryan South Asian (GENERATION-LOG, run 001 verdict).

**Adhikari** is a hill Bahun-Chhetri name — Indo-Aryan — and it matches the face we actually
have. The surname and the face now agree, which was the real requirement all along; Gurung
was only ever the means. Common in the US diaspora, and pronounceable for an American
audience.

### Why 25, and why a student who also works

The approved face was generated at 26 and reads mid-twenties. "Nursing student" alone reads
21–22 and would contradict the pictures. An **accelerated second-degree BSN** resolves it:
those programmes are full of career-changers in their mid-twenties, so 25 is the realistic
age for the story, the face matches, and PROJECT-BRIEF §7's mid-twenties guardrail keeps its
margin. Being on placement rather than licensed also means she can be tired, junior and
unsure — which is better content than competence.

### Why night rotations
The single highest-value choice in the brief, and it survives the student reframe intact.
Night placement shifts are visually distinctive (empty streets at dawn, fluorescent
corridors, blue-hour commutes), they explain why she is out at odd hours, and they open a
large, intensely engaged nursing audience separate from the diaspora one. Two overlapping
audiences, one character. As a student she also gets the nursing-school audience — exams,
clinicals, the NCLEX — which is younger and more active than the working-nurse audience.

---

## 2. Physical description (LOCKED)

Copy these verbatim into every prompt. Do not paraphrase.

> ## THE FACE IS LOCKED (2026-08-25)
>
> **Element `ashmi-gurung-FULL-v3` — `83ab454a-a85a-4814-8459-c10fc7e493aa`**
> *Six references: neutral face, soft smile, serious, pensive, plus locked-build full-body
> front and three-quarter. Supersedes v2 (`cd78b211`) and FINAL (`f6328436`), both kept.*
>
> Selected after eleven runs and roughly sixty candidates. Source: run 011 variant 8
> (job `0ef4dc69`). **That image is the authority on the face, not this prose.** The text
> below has been updated to match it and exists to describe it, not to define it.
>
> **Use the Element for every future generation of her** — embed
> `<<<83ab454a-a85a-4814-8459-c10fc7e493aa>>>` in the prompt. Never re-derive the face from
> a written description; that produces a different woman (proven in run 011, variants 1–4).
>
> Element `ashmi-gurung-face-v1` (`05a710b3…`) is **retired** — it predates the eye and lip
> changes. Do not use it.
>
> Two things deliberately accepted when locking, both recorded so they are not rediscovered
> as bugs: the face reads South Asian but not distinctly Himalayan (PROJECT-BRIEF §4), and
> the grey eyes are a chosen departure from natural Nepali colouring.
>
> **The build is now locked too** — see §2. Face and body are both settled; the training
> set is unblocked.
>
> **Build below the neck is still open.** Body type, bust and hips are unspecified and
> must be settled before the training set is shot, since that set fixes the body too.

- **Skin:** warm medium-tan, golden undertone, matte with visible natural texture
- **Face:** oval, softly tapered jawline and chin, high cheekbones, softly lean cheeks,
  **mature adult bone structure and proportions**
- **Nose:** long and straight, medium bridge, defined rounded tip
- **Lips:** full and wide, defined cupid's bow, **soft rose-pink**, bare matte finish
- **Eyes:** **light grey** — soft pale grey irises with a subtle darker limbal ring and
  natural tonal variation. Almond, slightly deep-set, full upper lids, softly downturned
  outer corners. Always carry `muted rather than glowing, not coloured contact lenses` —
  pale grey over warm-tan skin renders as a contact-lens overlay without it.
- **Eyebrows:** very thick, straight, dark, set low and close to the eyes, natural strays
- **Hair:** black-brown with warm undertone, long and thick, straight with a slight natural
  wave, centre parting, matte finish with visible flyaways
- **Build (LOCKED 2026-08-25):** **167 cm (5'6")** · approx. **104 cm bust / 62 cm waist /
  100 cm hips** · **78 cm underbust, roughly an E cup on a narrow ribcage** · a full
  bottom-leaning hourglass

  | Proportion | Target |
  |---|---|
  | Waist-to-hip ratio | ~0.62 |
  | Bust-to-waist ratio | ~1.68 |
  | Shoulder-to-waist ratio | ~1.45–1.6 |
  | Shoulders | narrower than hips |
  | Leg length / total height | ~0.52–0.56 (legs slightly longer than half her height) |
  | Torso / total height | ~0.44–0.48 |

  Also: slim arms and lower legs, a smooth curved waist-to-hip transition (not angular),
  balanced upper and lower body. **This supersedes the earlier "petite ~5'2", slim, small
  frame" spec**, which was a planning-session guess and was never rendered.

  > **How to prompt this build.** State the held variables, not just the changed one.
  > `soul_2` and Seedream both read "larger bust" as "larger woman" and will silently
  > inflate hips, thighs and arms unless the slim ones are named explicitly. The working
  > form is: give the frame first (`slim narrow frame, 62 cm waist, 100 cm hips, 78 cm
  > underbust, narrow ribcage, narrow shoulders, slim arms, slim thighs`), then the bust,
  > then repeat that everything else stays slim and that **she is not a heavier woman
  > overall**. Without that last clause the whole figure drifts up.
- **Marks:** a small mole below the left jaw; faint freckles across the nose bridge

> **Mandatory:** she must read unambiguously mid-twenties. Every prompt carries
> `no babyface, no overly youthful rounded proportions`. This is a hard project
> guardrail (see PROJECT-BRIEF §7), not a stylistic preference. Adding an explicit
> `twenty-six years old, mature adult facial proportions, longer facial thirds` is the
> reliable lever — bare-face and fresh-expression directions pull the apparent age down.

### Signature wardrobe
Ecru cable-knit sweater over a white cotton tee · straight-leg mid-wash jeans · white
leather low-tops · **thin gold chain with a small coral-and-turquoise pendant** · small gold
hoops · thin gold ring, right hand.

The coral-and-turquoise pendant is the identity anchor — traditional Himalayan stones,
and a small recurring visual signature across every post.

#### Canonical face — locked detail (from the approved profile-picture frame)

Reusable as a `FACE LOCK` block in any prompt. Written as positive statements of what each
feature **is**, never as instructions to avoid changing it — a lock written as a do-not list is
a hit list (§5b).

- **Shape** — oval, high wide cheekbones, jaw tapering to a small rounded chin.
- **Skin** — warm mid-brown with a golden olive undertone.
- **Eyebrows** — thick, dark, natural; unplucked at the inner ends where the hairs sweep
  upward; thinning slightly along the tails; a wide gap between them. Naturally asymmetric.
- **Mole** — one small dark mole above her left eyebrow. The only mole on her face.
- **Eyes** — light grey with a faint blue cast and a distinct darker limbal ring; small pupil in
  bright sun; almond shaped, outer corner slightly downturned, clear upper lid crease; dark
  lashes of moderate length, sparse lower lashes.
- **Nose** — narrow straight bridge, tip slightly rounded and lifted, oval nostrils.
- **Mouth** — upper lip medium with a defined cupid's bow, lower lip full and rose pink;
  straight even upper teeth in a faintly warm white, the two centre teeth slightly larger.
- **Ears** — small, close to the head.
- **Face is hairless.** Vellus hair is never requested on her face: enlarged ten times it
  becomes visible facial hair, and peach fuzz has no safe enlarged form (§5b scale rule).

#### Daisy dress look (LOCKED)

Short black fit-and-flare mini dress in a **ditsy** daisy print — small cream-white daisies,
pale yellow centres, fine dark green stems, scattered densely on black. Thin spaghetti straps ·
gathered lightly sheer ruched band across the top of the bodice with a small centre tie ·
fitted bodice seamed at the natural waist · full circle skirt flaring to mid-thigh · flat black
strappy sandals · the usual gold huggie hoops, coral-and-turquoise pendant and matching ring ·
sunglasses hooked on the neckline rather than on her head, since this look pairs with a bun.

Describe it as construction, never as "black floral mini dress" — the print scale, the ruched
band, the waist seam and the circle skirt are what make it the same garment twice.

#### Summer look (LOCKED — approved 2026-08-25)

White ribbed scoop-neck cropped tank top, thick straps, black waistband just visible below ·
**small thick gold huggie hoops** (not thin hoops) · thin gold chain with the small round
coral-and-turquoise pendant · matching coral-and-turquoise ring · round black sunglasses
pushed up on her head · dark brown hair in a high ponytail with loose flyaways.

Locked from the approved profile-picture generation. Carry it verbatim as the `WARDROBE`
block from `prompts/02-profile-picture.md` in any warm-weather shot meant to be the same
outfit or the same day. Change it deliberately, not by rewording.

**Note the hoops.** Earlier prompts said `thin gold hoops` and the approved image came back
with thick huggies, which read better at profile-picture scale. The signature-wardrobe line
above still says thin hoops for the autumn look; the summer look overrides it.

---

## 3. Voice — American first, Nepali second

She is **culturally American**. Born and raised here, American in language, humour, clothes
and reference points. Nepali is her heritage language, not her first one. This is not an
immigrant's story and it is not quite a translator's either — it is the story of someone
slightly outside her own heritage, fluent enough to belong and not fluent enough to keep up.
That gap is the account's emotional register.

**She is a heritage speaker, and that is specific:**

- She **understands far more than she can say.** Follows her parents completely; replies in
  English about half the time.
- Her Nepali has **American vowels** and a slight hesitation — noticeable to any Nepali
  speaker, invisible to everyone else.
- She has the **domestic vocabulary and not the formal one**: fluent about food, family and
  feelings, lost the moment anything technical, bureaucratic or medical comes up. She would
  say *"I don't know how to say 'insurance deductible' in Nepali"* and that is a whole post.
- She occasionally uses a word **slightly wrong** or reaches for one and cannot find it. To
  Nepali speakers this is endearing and instantly recognisable. **Do not over-correct her
  Nepali — the imperfection is the authenticity.**
- Code-switching, not translation: English sentences with Nepali landing on the emotional
  beats.
- Recurring phrases: **`ke garne`** (*what to do* — the resigned shrug, the account's
  signature), `khana khayo?` (*did you eat?* — how her mother says *I love you*),
  `aama` / `buwa`, `didi`, `ramro`, `la la`.
- **Never explains the culture to the audience.** People who get it, get it — that's the
  moat. Explaining is what makes diaspora content read as costume.

> **Why this is better than "fluent but domestic".** Full fluency in a US-born
> twenty-five-year-old is the less common case and harder to write convincingly. The
> heritage-speaker gap is the majority experience of the second generation, more relatable
> to the exact audience being targeted, and much more forgiving — a small Nepali error now
> reads as characterisation rather than as a mistake. It converts BIBLE §7's language risk
> into an asset.

---

## 4. Content pillars

| # | Pillar | Why it works |
|---|---|---|
| 1 | **Nursing school + placement** | Dawn commutes, scrub fits, hospital coffee, the 3am lull, exams, clinicals. Huge nursing-student and nurse audience. |
| 2 | **Nepali food at home** | Momo is the universal entry point. Also dal bhat, sel roti, achar. |
| 3 | **Second-gen tensions** | Aama's calls, marriage questions, cousin comparisons, not knowing a word. Most shareable pillar. |
| 4 | **Boston texture** | The T, winter grey, Medford/Somerville streets, Dunkin runs. |
| 5 | **Festivals** | Dashain, Tihar / Bhai Tika, Losar. Seasonal tentpoles — plan ahead. |
| 6 | **Fit checks** | Scrubs → going out → kurta for family events. The three-wardrobe life. |
| 7 | **Community** | Nepali grocery runs, momo spots, gatherings. |

Pillar 3 travels furthest — second-gen tension is legible to every diaspora, not just Nepali.
Pillar 1 recruits an entirely separate audience. Lead with those two.

---

## 5. Visual grade (LOCKED)

Realism comes from **imperfection**, not quality. The #1 AI tell is a photo that looks too well-lit.

**Always:**
- Phone-camera framing — slightly off-centre, mild tilt, imperfect horizon
- Highlights that clip; shadows that crush
- Mild motion blur on hands and hair
- Cluttered, honest backgrounds — nothing staged
- Visible grain in low light, especially night-shift and dawn scenes

**Never:** golden-hour glamour, studio lighting, symmetrical framing, bokeh portraits,
flawless skin, dewy highlight.

**Per-setting lighting:**
| Setting | Grade |
|---|---|
| Hospital | Harsh overhead fluorescent, slight green cast, flat |
| Dawn commute | Blue hour, high ISO, visible grain, underexposed |
| Home / kitchen | Warm mixed tungsten, uneven, one lamp doing the work |
| Boston winter exterior | Flat overcast grey, no shadow, low contrast |

Boston's grey winter light is an **asset**. It is the least glamorous, most photographic
light there is, and it is very hard for a model to make look artificially pretty.

---

## 5b. Prompt craft — what actually works on these models

Learned across thirteen runs. Ignoring these repeats a day of re-rolls.

**Use a positive framing instruction, not single-subject negatives.** `no inset image`,
`no collage`, `no duplicate figures` do not work and may summon what they name. This does:

> `A single full-bleed vertical photograph filling the entire frame edge to edge`

Took spurious inset thumbnails from 5-in-8 to 0-in-8, and it has held across three models.

**On edit passes the same rule is sharper: never name a thing you want left alone.** A
negation does not shield its subject, it nominates it, and the polarity is not reliably
preserved. `Do not add freckles, moles, beauty marks` deleted the mole above her eyebrow.
`Do not change her skin tone` changed her skin tone (cheek RGB 172,100,67 to 178,107,81).
Protect with a positive keep — `keep the small dark mole above her eyebrow` — or say nothing
at all. **A do-not list is a list of things you have just drawn the model's attention to.**

**A model cannot draw below its own resolution.** Anything requested at a scale too small to
render comes back ten to fifty times too big, and a size qualifier does not prevent it — the
model is not disobeying, it has no smaller mark available. So the enlarged version of a request
is what you are actually ordering. `A network of tiny lines a fraction of a millimetre deep`
returned wrinkles; `tone variation at two or three millimetres` returned moles; `nothing larger
than a pore changes` bound neither. Pores, vellus hair and micro-speculars are safe because
their enlarged forms are still pores, fuzz and glints. **Before adding a clause, ask what it
looks like ten times too big — if that is a defect, the clause cannot go in at any wording.**
Where a texture has no safe small form, describe it as a quality of the surface rather than as
a structure: `the faint orange-peel quality of real skin` has no scale to inflate, `a mesh of
tiny lines` does.

**Naming is only dangerous in negation.** §5b's do-not rule is about things you want left
alone. An edit prompt that wants something *removed* should name it plainly — `clear the dark
spots on her forehead away` is the correct form, and the polarity problem does not arise.

**An edit prompt must be additive and short.** Editors re-synthesise what you describe to
them, so a long preservation list is a re-description of the subject and invites a re-render.
The crowd pass that held was 921 characters naming one region; the skin pass that failed was
1,951 naming eyes, brows, nose, lips, teeth, jawline, cheeks and hairline. Say what to add,
name the few marks to keep, and stop.

**Comparative beats absolute for anatomy.** `hips visibly wider than her shoulders`,
`waist-to-hip ratio about 0.62` land reliably. Bare adjectives (`curvy`, `petite`) and even
absolute measurements get averaged toward the model's defaults.

**Keep prompts short and high-signal.** Around forty comma-separated clauses and nothing
carries weight. Write sentences.

**Beauty needs asking for.** The §5 realism engine at full strength actively suppresses it.
`the kind of face that needs no makeup` was the single highest-leverage phrase found —
it keeps the bare-face requirement without implying plainness.

**Push age explicitly.** `twenty-six years old, mature adult facial proportions, longer
facial thirds`. Bare-face and fresh-expression directions pull apparent age down, which
erodes the §7 guardrail.

**Model selection matters more than prompt wording for some attributes:**

| Need | Use | Because |
|---|---|---|
| Body proportions | `seedream_v4_5` | `nano_banana_pro` has almost no body-type range |
| Photographic realism, bare face | `nano_banana_pro` | Seedream renders retouched and adds makeup |
| Identity from an Element | either | both honour `<<<element_id>>>` faithfully |
| Face iteration | **never** a raw reference image on `soul_2` | forces `enhance_prompt`, strips every locked clause |

**One reference image cannot hold strong expressions.** An Element built from a single
neutral portrait keeps identity for neutral and mild expressions and **visibly drifts on a
wide laugh** — jaw and cheek structure change and it stops being the same person. Because
the Element interpolates between its references, the fix is to give it several: v2 carries
neutral + soft smile + serious + pensive. Any Soul trained on drifted smiles learns a
blurred identity, so this must be right *before* the training set is shot, not after.

**An Element anchors only what its references show — and it is not sufficient on its own.**
A face-only Element leaves the body to be re-derived from text every generation, and it
reverts to the model's slim default. Adding locked-build full-body references (front and
three-quarter) to v3 recovered hip and thigh volume where prompt wording alone had failed.

**But the Element alone does not hold it either.** Every shot where the build came out right
carried *both* the Element and an explicit comparative body line in the prompt. Shots
generated on the Element with no body line drifted straight back to slim. The rule is
**Element AND prompt**, always:

> `Her hips are visibly wider than her shoulders. Her waist is distinctly narrower than both
> her bust and her hips. Her thighs are clearly fuller than her calves. She is not a heavier
> woman overall.`

Carry that block in every prompt where the body is visible. The Element biases toward the
right silhouette; the prompt is what stops the model's slim prior from winning.

**This model overshoots colour-cast instructions.** "Slight green cast" renders as heavy
green; "a faint green tint only" still renders as strong green. Describe the *light source*
instead of naming the colour — `overhead fluorescent tubes, neutral-cool white` — and let
the cast emerge.

**Unlimited generations are not reachable from the MCP connector.** Re-verified 2026-08-26
against the current connector, which now documents `use_unlim` as a first-class parameter on
`generate_image`. It still does not help, for two independent reasons.

*Reason one — the flag is rejected by every model worth using.* Preflighted with
`get_cost: true`, so no credits were spent:

| Model | `use_unlim: true` |
|---|---|
| `soul_2`, `soul_v2` | Accepted |
| `nano_banana_pro` | `Unlimited generations aren't supported for nano_banana_pro` |
| `nano_banana_2` | `…aren't supported for nano_banana_flash` |
| `seedream_v4_5` | `…aren't supported for seedream_v4_5` |
| `seedream_v5_pro` | `…aren't supported for seedream_v5_pro` |

**The catalog is wrong about this.** `models_explore(unlim: true)` returns all eleven image
models tagged `supports_unlim: true`, including every model in the rejected column. Trust the
`get_cost` preflight, not the catalog tag.

*Reason two — the allowance does not exist on this account.* `models_explore` reports
`unlim: {available: false, remaining: null, expires_at: null}`, and even on `soul_2`, where the
flag is accepted, the preflight still quotes credits (`credits_exact: 0.12`). The connector's
`use_unlim` means **free-trial unlimited generations**, a different pool from the plan
entitlement the web app honours — `balance` returns only `{credits, subscription_plan_type:
"ultimate"}` and exposes no plan-level unlimited at all.

*And a third, if the first two were ever fixed:* the only model that accepts the flag is
`soul_2`, which needs a trained Soul for identity consistency — attaching a raw reference to it
instead silently forces `enhance_prompt: true` and discards the prompt (§6). Soul training on
this account fails with a bare "Something went wrong", so that route is blocked anyway.

Budget MCP work in credits (1 credit per image); use the web app for anything high-volume.

**Operational:** the plan caps at **8 concurrent jobs** and silently drops the overflow —
submit in batches of 8 or fewer and always check `failed_count`. Individual jobs also fail
intermittently with no error detail; resubmitting unchanged generally works.

---

## 6. Production pipeline

Soul is identity-faithful but works **only** with Soul V2 and Soul Cinema. Video models
(Seedance, Kling, Cinema Studio) need a Reference Element instead. So we build both.

```
1. CHARACTER SHEET  → split-screen, photoreal-unretouched. Approve the face.
                      (Nothing downstream is worth doing until this is right.)
2. REFERENCE ELEMENT → created from the approved sheet. Instant. Unlocks video models.
3. TRAINING SET      → 15-20 varied shots via the Element: angles, expressions,
                      lighting, distances. Variety here IS the quality of the Soul.
4. TRAIN SOUL        → show_characters action=train, ~10 min. Identity locked.
5. PRODUCTION        → Soul + soul_2 for stills · Element for video models.
```

**This resolves the bootstrap problem:** Soul training needs 5–20 photos of a person who
does not exist yet. The Element is what generates them.

Step 3 is where projects fail. A training set of near-identical shots produces a Soul that
only renders that one shot. Deliberately vary angle, expression, distance, and light.

### Model constraints (verified 2026-08-25)

The two identity mechanisms cover **disjoint** sets of models. This is why both get built,
and it is not optional:

| | Element | Soul |
|---|---|---|
| Built from | 1 image, instant | 5–20 photos, ~10 min |
| Works with | `nano_banana_pro`, `nano_banana_2`, `gpt_image_2`, `seedream_v4_5`, `seedream_v5_lite`, Cinema Studio image/video, Seedance, Kling | `soul_2`, `soul_cinema_studio` **only** |
| Subjects per shot | multiple | exactly one |

An Element **cannot** be used with `soul_2`, and a Soul **cannot** be used with anything
else. So the training set at step 3 must be shot on an Element-compatible model, not on
`soul_2`.

**This does not put `soul_2` out of reach.** Soul training takes *images*, whatever produced
them. The chain still closes: Element → training set on an Element-compatible model →
`show_characters action=train` on those images → a Soul that works with `soul_2`. Choosing a
face rendered on Seedream therefore costs nothing downstream.

### Never iterate a face with a raw reference image

Attaching a reference image to `soul_2` silently forces `enhance_prompt: true`: the server
throws away the submitted prompt and substitutes its own caption of the reference. Every
locked clause in §2 and §5 — realism engine, heritage markers, wardrobe, mole, freckles —
is summarised away. The flag cannot be turned off through the MCP path.

A text-only `soul_2` call keeps `enhance_prompt: false` and honours the prompt exactly. So
**prompt fidelity and identity anchoring cannot be had at the same time on `soul_2`** —
which is precisely what the Element and Soul mechanisms exist to solve. Full evidence in
`GENERATION-LOG.md`, runs 002–004.

---

## 7. Open risks

**Overlap with `@aikok.png`.** That account is *also* a Boston-based nurse in her twenties.
Ours differs on every other axis — openly AI, Nepali-American, culture/lifestyle rather than
POV comedy — and nursing is genuinely a dominant profession in the Nepali diaspora, so the
combination is authentic rather than derivative. But the surface collision is real and worth
knowing. Mitigation: keep the specifics concrete and different (named hospital, Medford not
downtown, night shift not day), and lead hard on the Nepali material, which they cannot follow.

**Local detail accuracy.** Greater Boston's Nepali/Himalayan community clustering in
Somerville/Medford/Everett is the design assumption behind her geography. Worth a sanity
check from someone who knows the area — wrong local detail is exactly what breaks authenticity
with the audience that matters most.

**Language.** Every Nepali phrase should be checked by a speaker before posting. Wrong or
stilted Nepali is instantly visible to the core audience and very hard to recover from.


---

## 8. Calibration reference

An existing Soul on this account (`Pema Dolma`, an older Himalayan woman) was reviewed as
a capability test. Three things it settles:

1. **Higgsfield renders Himalayan features correctly.** Broad high cheekbones, correct eye
   fold, no drift to generic North Indian or East Asian. The §7 drift risk is real but
   tractable — the model can do this when the prompt is specific.
2. **The unretouched grade works.** Genuine pores, uneven tone, age marks, natural
   asymmetry, correct hands. The anti-airbrush engine delivers.
3. **Coral-and-turquoise is authentic and renders well** — independent confirmation of
   Ashmi's pendant motif.

**But it is the wrong aesthetic to copy.** That image is a well-composed, warmly-lit,
travel-magazine portrait. Ashmi is the opposite: a phone snapshot in a Medford kitchen,
badly framed, mixed lighting, nothing staged. Same technical realism, deliberately worse
photography.

**One caveat:** an older face is far easier to make photoreal — wrinkles and weathering
give the model texture to render. A 24-year-old's smooth skin is exactly where AI-tells
surface. Ashmi's realism is a harder problem than this image proves, so the skin-texture
clauses in the prompt carry more weight, not less.
