# 13 — Café table still life (cappuccino + Danish)

Model `gpt_image_2` · 3:4 · 2k · medium · 2 credits · job `00234dd8-1d43-4cff-a058-4727aed678d2`
Reference: `a7fbe7e6-910e-4b86-8caf-e3f12c0c8d8b` — a local crop of the finalised café frame.

## Cropping the reference locally

The source frame has her in it, and the request was for the table alone. Rather than
prompt her out — which costs credits and risks the OpenAI filter that refused this image
family four times — the table region was cropped out with PIL and uploaded as the
reference. Free, exact, and it carries the real cup, saucer, Danish, glass and tabletop
with no figure and no skin anywhere in the frame.

First crop at `x > 0.50w` still caught her thigh at the left edge; `x > 0.585w` cleared it.
Worth checking the crop before uploading rather than after a refusal.

GPT Image 2 accepted it without complaint, which confirms the earlier refusals were about
skin in the reference and not about the café scene as such.

---

A cinematic still-life photograph of a cappuccino and a pastry on a cafe table. Re-shoot the exact items in the attached reference from a lower, closer camera.

**CAMERA**
The lens sits just above the tabletop, roughly at the height of the cup's rim, looking across the table rather than down at it. Vertical frame. The cappuccino is the subject, slightly left of centre and closest to the lens; the pastry sits behind it and to the right; the water glass stands further back. Shallow depth of field — the rim of the cup and the latte art are tack sharp, the pastry a little softer, and the window and street beyond dissolve into smooth creamy bokeh.

**THE CAPPUCCINO — copy exactly from the reference**
A wide-mouthed white ceramic cup on a matching white saucer, the handle turned to the left. Warm caramel-brown crema with a white foam rosetta poured into it: a layered leaf of fine fronds narrowing to a stem drawn down the centre. A thin lighter ring of crema around the inside edge. Fine micro-bubbles across the surface.

**THE PASTRY — copy exactly from the reference**
A round cheese Danish on a plain white plate: golden-brown laminated pastry coiled into a thick ring, glossy and blistered, with a pale yellow custard-cheese centre slightly domed and lightly caramelised at its edge. Flaky layers visible along the sides.

**THE GLASS**
A plain clear tumbler of still water standing behind them, the water line catching the light, faint condensation on the outside.

**THE TABLE**
A round table of near-black stained dark wood, softly reflective, the grain just visible where the light rakes across it. The curved edge of the table runs through the lower part of the frame.

**SETTING**
Behind and above, the cafe's floor-to-ceiling window with its pale wooden ledge, and beyond it a wet city street — entirely out of focus, reading only as soft grey, cream and green shapes with gentle highlights where the light catches the wet pavement.

**LIGHT**
Soft, flat, bright overcast daylight from the window at the left and behind, raking low across the table. It skims the foam and the glazed crust of the pastry, draws a bright specular curve along the rim of the cup and down the side of the glass, and leaves the near edge of the table in gentle shadow. Cool daylight against the warm caramel and gold of the coffee and pastry.

**GRADE AND MOOD**
Quiet, warm, unhurried. Rich but natural colour, slightly lifted blacks, a gentle filmic contrast curve, a soft vignette.

**QUALITY**
Shot on a phone in portrait mode: crisp detail in the foam texture, the crema micro-bubbles, the flaking pastry layers and the ceramic glaze, with natural depth-of-field falloff. High dynamic range, fine grain in the shadows. Believable, not an advertisement.

The frame holds only the table and what is standing on it.

---

## Notes

**"The frame holds only the table and what is standing on it"** does the work that
"no people, no hands, no text" would otherwise do, without naming any of them. Same
principle as dropping the mole language in `09`.

**Deliberately letting the background go soft** also disposes of the signage problem.
The "macy's" sign and the street furniture sit outside the focal plane, so there is no
text to render and nothing to drift — the failure mode that broke three earlier runs.

**Drift:** the rosetta has fewer, more symmetrical fronds than the original pour, and the
Danish coils slightly differently. Expected — this is a re-shoot from a new angle, not a crop.
