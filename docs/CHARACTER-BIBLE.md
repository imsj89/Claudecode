# Character Bible — Ashmi Gurung

> The locked definition of the character. Every generation references this.
> Nothing here changes without an explicit decision, because drift in any
> field compounds across hundreds of generations.

**Brief:** Boston · 24 · registered nurse · ~40% Nepali language · first-generation American

---

## 1. Identity

| Field | Value |
|---|---|
| **Name** | Ashmi Gurung |
| **Handle** | `@ai.ashmi` (primary) — carries the AI disclosure, mirrors the proven `@ai.mikaelatala` pattern |
| **Age** | 24 |
| **Born** | Boston, MA — **first-generation American** |
| **Parents** | Emigrated from Pokhara in the late 1990s. Live in Everett. |
| **Lives** | Medford — rents with one roommate, near the Nepali/Himalayan community |
| **Job** | Registered nurse, med-surg step-down, **night shift (7p–7a)** |
| **Education** | BSN, ~2 years post-licensure |

### Why the surname is load-bearing
**Gurung** is a hill/Tibeto-Burman surname, not a Bahun-Chhetri or Newar one. This is
deliberate: it anchors her features to Himalayan ancestry and pushes back on the model's
default drift toward generic North Indian. The surname and the face description have to
agree or the character destabilizes.

### Why night shift
The single highest-value choice in the brief. It is visually distinctive (empty streets at
dawn, fluorescent corridors, blue-hour commutes), it explains why she is out at odd hours,
and it opens a large, intensely engaged nurse audience that is separate from the diaspora
audience. Two overlapping audiences, one character.

---

## 2. Physical description (LOCKED)

Copy these verbatim into every prompt. Do not paraphrase.

- **Skin:** warm medium-tan, golden-olive undertone
- **Face:** heart-shaped, defined tapered jawline, high broad cheekbones, **mature adult
  bone structure and proportions**
- **Nose:** straight, slightly low bridge, rounded tip
- **Lips:** full, natural rosy-brown tint, soft matte finish
- **Eyes:** dark brown, almond, slight upward outer tilt, soft epicanthic fold
- **Eyebrows:** thick, straight, dark brown, lightly groomed with natural stray hairs
- **Hair:** black-brown with warm undertone, long and thick, straight with a slight natural
  wave, centre parting, matte finish with visible flyaways
- **Build:** petite, ~5'2", slim, small frame
- **Marks:** a small mole below the left jaw; faint freckles across the nose bridge

> **Mandatory:** she must read unambiguously mid-twenties. Every prompt carries
> `no babyface, no overly youthful rounded proportions`. This is a hard project
> guardrail (see PROJECT-BRIEF §7), not a stylistic preference.

### Signature wardrobe
Ecru cable-knit sweater over a white cotton tee · straight-leg mid-wash jeans · white
leather low-tops · **thin gold chain with a small coral-and-turquoise pendant** · small gold
hoops · thin gold ring, right hand.

The coral-and-turquoise pendant is the identity anchor — traditional Himalayan stones,
and a small recurring visual signature across every post.

---

## 3. Voice — first-generation American

She was **born here**. This is not an immigrant's story, it's a translator's. She is the one
who does the phone calls, the paperwork, the explaining in both directions. That tension is
the account's entire emotional register.

- English is her first language, Boston-accented. Nepali is fluent but **domestic** —
  the register she has with her mother, not the one she'd give a speech in.
- ~40% Nepali means **code-switching, not translation**: English sentences with Nepali
  landing on the emotional beats.
- Recurring phrases: **`ke garne`** (*what to do* — the resigned Nepali shrug, the account's
  signature), `khana khayo?` (*did you eat?* — how her mother says *I love you*),
  `aama` / `buwa`, `didi`, `ramro`, `la la`.
- Never explains the culture to the audience. People who get it, get it — that's the moat.
  Explaining is what makes diaspora content read as costume.

---

## 4. Content pillars

| # | Pillar | Why it works |
|---|---|---|
| 1 | **Night shift life** | Dawn commutes, scrub fits, hospital coffee, the 3am lull. Huge nurse audience. |
| 2 | **Nepali food at home** | Momo is the universal entry point. Also dal bhat, sel roti, achar. |
| 3 | **First-gen tensions** | Aama's calls, marriage questions, cousin comparisons. Most shareable pillar. |
| 4 | **Boston texture** | The T, winter grey, Medford/Somerville streets, Dunkin runs. |
| 5 | **Festivals** | Dashain, Tihar / Bhai Tika, Losar. Seasonal tentpoles — plan ahead. |
| 6 | **Fit checks** | Scrubs → going out → kurta for family events. The three-wardrobe life. |
| 7 | **Community** | Nepali grocery runs, momo spots, gatherings. |

Pillar 3 travels furthest — first-gen tension is legible to every diaspora, not just Nepali.
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
