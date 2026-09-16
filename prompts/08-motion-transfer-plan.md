# Prompt 08 — Genjutsu motion transfer: plan before generating

## What the reference video is

| | |
|---|---|
| Duration | 15.11 s |
| Format | 720×1280, 9:16, 30 fps |
| Audio | AAC stereo — present, and it matters (see below) |
| Cuts | **None.** One continuous take |
| Camera | Static throughout. No pan, tilt or push |
| Location | One room: pale wall and ceiling, a horizontal band of warm amber lights, dark shelving, a chair |
| Outfit | One: fitted white ribbed tank, slightly cropped, low light-grey sweatpants |
| Hair | Long dark waves, down, small claw clip at the crown |
| Framing | Starts close on head and shoulders, settles to waist-up for the rest |
| Motion | Talking straight to camera with large expressions; both hands come up into her hair around 2.5 s; one hand rises near her face later; head tilts and shoulder movement throughout |

## So: how many images?

**One.** The question assumed a set, but a single unbroken take with a static camera needs a
single character still. Genjutsu drives that one image with the whole clip.

Optionally two or three **extra identity references** alongside it — the closeup, the features
grid, the character sheet. The model takes `image_references` as a list, and the same logic that
made Element v3 hold up should apply: one image defines the shot, the others stabilise the face.
Worth testing as a second run rather than assumed.

## What that one image has to get right

It is not just "a picture of her". Four things decide whether the transfer works:

1. **9:16, matching the driving clip.** A mismatch forces the model to letterbox or crop.
2. **Framing slightly wider than the video's tightest moment.** Waist-up with clear headroom and
   space either side of her shoulders. Her hands come up into her hair at 2.5 s — if the still
   is cropped tight, that motion clips the frame edge and mangles.
3. **Opening posture: standing square to camera, arms relaxed at her sides, facing the lens.**
   The closer the still matches frame 1 of the driving video, the less the model has to warp.
4. **The complete background, in shot.** Genjutsu takes the scene from the image, so whatever
   room she is in has to be fully built in that still — the legacy `motion_control` tool had a
   `scene_control` switch for this, and the Genjutsu model does not expose one.

## Steps

1. **Upload the driving video** and get a `media_id`.
2. **Preflight cost** with `get_cost: true`, image + video attached. This also confirms whether
   15.1 s is within the model's limit — the duration cap is not documented and there is no
   `duration` parameter to clamp it.
3. **Generate the character still** — 4:5 is wrong here, it must be **9:16**. Nano Banana Pro
   with the existing identity references, carrying the canonical face lock and body spec.
4. **Review the still against the four criteria above** before spending video credits. A video
   generation costs many times an image, so the still is the cheap place to iterate.
5. **Run Genjutsu** at 720p first as a proof, then 1080p once the motion reads correctly.

## Decisions needed before step 3

**Setting.** The reference is a bedroom. For her, the on-brand equivalent is her own room in
Medford — which also serves pillar 3, the talking-to-camera second-gen material that BIBLE §4
says travels furthest. Alternative: the hospital break room, which serves pillar 1.

**Outfit.** A white ribbed tank with the established grey sweatpants matches the reference
silhouette almost exactly and is already locked wardrobe, so the motion transfers cleanly and
nothing new needs pinning.

**The audio is the real constraint.** The mouth movements in the reference are speech-shaped.
Transfer them and Aasmi's mouth makes those exact words, which means the finished video only
works over the audio that produced them. If that is a trending sound, reuse is the norm and this
is fine. If it is the original creator speaking her own words, the output would be putting her
speech in Aasmi's mouth — pick a trending audio instead and find a driving clip cut to it.

## Risks

- **15 s is long for motion transfer.** Identity drift accumulates over a take; the face is
  usually least stable at the end. Check the last two seconds first.
- **Hands in hair at 2.5 s** is the hardest moment in the clip. If anything breaks, it breaks
  there.
- **Talking heads expose the face continuously**, unlike the bowling shots where she was turned
  away. This is the most identity-exposed thing attempted so far.
- **Cost.** 15 s at 1080p is likely the most expensive single generation in this project. Run
  720p first.
