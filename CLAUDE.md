# Generation defaults

## When the user asks for an image with specific details and instructions

Generate **one single image**. Not two, not a pair to choose from.

| Setting | Value |
|---|---|
| Aspect ratio | `3:4` |
| Resolution | `2k` |
| Quality | `medium` |
| Count | `1` |

**Cost per generation:** 2 credits on `gpt_image_2`, 1.5 on `gpt_image_2_5`.
Preflighted 2026-09-16 with `get_cost: true`.

This replaces the earlier habit of sending two variants at max quality and 4K,
which cost 32 credits a pair on `gpt_image_2_5` sunburst.

## Why these settings

**2K is above what Instagram displays.** A 4:5 feed post renders at 1080 × 1350 and
uploads are downscaled past ~1440px wide. 2K gives roughly 1638 × 2048, so the image is
downsampled on upload either way — which also averages out minor softness.

**Resolution is cheap, quality is expensive.** On `gpt_image_2` at 3:4, 4K/medium is 2.5
credits while 4K/high is 11 — same pixels, 4.4× the price. Quality tier is render effort
(hands, faces, fine texture); resolution is only canvas size.

**Realism does not come from resolution.** Even 4K here is ~8MP, about a third of a real
24MP iPhone file. What made the phone-camera shots convincing was the specified artifacts —
HDR flatness, over-sharpening halos, noise-reduction smear, JPEG edges — not pixel count.

## Deviate only when asked

- More than one image, a different ratio, or higher quality: only on explicit request.
- Several **different** shots (e.g. four camera angles) are separate prompts, not variants —
  use `generate_image_batch`.

## Always

- **Preflight with `get_cost: true`** before any unusual model or setting. It submits nothing.
- **Report credits accurately.** Never quote a cost from memory — costs vary steeply by model,
  quality tier and resolution. A figure preflighted for one model does not transfer to another.

## Note on 3:4 vs 4:5

Instagram's native portrait format is **4:5** (1080 × 1350). `3:4` is slightly taller and will
be cropped or letterboxed a little when posted.

`gpt_image_2` does not support 4:5 and silently coerces it to 3:4, so 3:4 is the correct
setting there. `gpt_image_2_5` **does** support 4:5 natively. Use 3:4 as instructed unless the
user says otherwise.
