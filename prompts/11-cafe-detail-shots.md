# 11 — Café detail shots (pastry case, menu board)

Two independent prompts, so `generate_image_batch` rather than `count: 2`.
Model `gpt_image_2` · 3:4 · 2k · medium · 2 credits each.

- Pastry case — job `6e235a0e-c85c-4c37-9fab-c8bea3ce314b`
- Menu board — job `502545e6-1ecd-42e8-8ed2-9608b68eb461`

No reference media. Both scenes described from the user's own photos.

## The text trick that worked

Both shots are text-heavy, which has broken every previous generation in this project
(the "DO NOT ENTER" sign degraded to garbled lettering over three runs). Two things fixed it:

1. **GPT Image 2**, whose catalog tags are `text-rendering` / `typography`. It spelled all
   six pastry cards and the full three-column menu correctly on the first attempt.
2. **Give the background text permission to be unreadable.** The pastry prompt says
   *"The cards further back are softly out of focus and unreadable."* That removes the
   rendering burden for everything the viewer would not read anyway, and the model spends
   its budget on the six front cards instead of smearing twelve.

Naming the exact card text as a short list of capitalised item names — rather than asking
for "price cards" generically — is what made them legible.

## Branding substitution (menu board)

The source photo is a **George Howell Coffee** menu with that roaster's real prices. The
generated version carries a generic script wordmark ("Roasted Coffee Roasters") instead,
because text drift would otherwise attach invented prices and mangled item names to a named
real business. The layout, palette, column structure and tasting-note styling all carry over.

Prices in both images are invented and match nothing real.
