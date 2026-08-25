# AI Influencer Account — Project Brief & Session Handoff

> **Read this first.** It carries the decisions, research, and blockers from the
> planning session so a new session starts warm. Nothing has been built yet.

**Status:** planning complete, blocked on network access. Next step is the
production playbook (see *Open decisions* before writing it).

---

## 1. Strategic decisions (locked)

| Decision | Choice | Why |
|---|---|---|
| **Disclosure** | **Openly AI** | Handle/bio label it as AI. Lower reach ceiling, but no ban risk, brand-safe, and durable. |
| **Niche** | **Culture / aesthetic lifestyle** | Lowest reach per post, strongest moat, best brand-deal appeal. |
| **Monetization** | **Brand deals / sponsorships** | Requires advertiser-safe persona and real engagement, not just view counts. |
| **Character** | **Nepali-American woman** | See §4. |
| **Tooling** | Higgsfield (Soul 2.0 + Soul ID) | See §5. |

---

## 2. ACCESS — use the hosted MCP connector

**Higgsfield has an official hosted MCP server with OAuth. No API keys required.**
This is the primary access path. (An earlier plan to use raw API keys was a
detour — the consumer app does not surface keys where expected. They exist at
`cloud.higgsfield.ai/api-keys` if the MCP route ever fails.)

### Connector setup (done via claude.ai UI, phone-friendly)

1. `claude.ai` → profile icon → **Settings** → **Connectors**
2. **Add custom connector** → URL: `https://mcp.higgsfield.ai/mcp`
3. **Connect** → OAuth with the normal Higgsfield account
4. **Enable the connector in the session** — installing is not enough. A
   connector can show `installState: connected` but `enabledInChat: false`,
   in which case its tools are NOT loaded. This is a common failure.
5. New session → tools appear as `mcp__higgsfield__*`

### Network egress — RESOLVED

The environment's Network access was on **Trusted**, which blocks all Higgsfield
hosts. Set to **Custom** with this list (verified working):

```
higgsfield.ai
platform.higgsfield.ai
cloud.higgsfield.ai
mcp.higgsfield.ai
upload.higgsfield.ai
cdn.higgsfield.ai
d2ol7oe51mr4n9.cloudfront.net
d8j0ntlcm91z4.cloudfront.net
```

The non-obvious entries matter most: the CloudFront hosts are where generated media
actually lands, `upload.higgsfield.ai` is where inputs go, and `cdn.higgsfield.ai` serves
style thumbnails. Without them the MCP tools work but no image can be fetched or uploaded.

Verified: `platform` 405, `mcp` 404, `d2ol7...` serves a full PNG. Real responses from the
destination servers, not tunnel failures. Note these applied to the **running** session —
no restart was needed for the network change.

> **The media CDN hostname is not stable — allowlist both.** Run 001 (2026-08-25) had its
> results served from `d8j0ntlcm91z4.cloudfront.net`, not the `d2ol7...` host verified
> during planning. That host was not on the list, so the images could not be fetched even
> though generation succeeded.
>
> **Telling the two failures apart matters.** A `403` in the response body is the
> destination server answering — the host is reachable. `curl: (56) CONNECT tunnel failed,
> response 403` is the *proxy* refusing before any connection is made — the host is not
> allowlisted. Only the second one is a network-policy problem.
>
> Consequence: a generation can succeed and be visible in the Higgsfield widget while
> being unreadable to the session that made it. That is survivable for approval steps a
> human performs anyway, but it blocks anything that needs to read pixels back.

Leave Environment variables empty — the UI warns they are visible to anyone using the
environment. OAuth via MCP avoids needing them at all.

## 3. Reference account analysis

Three accounts studied. Two distinct strategies.

### `@aikok.png` — 486K followers, 39 posts, 40 following
Bio: *"registered nurse | boston based <3"*. Verified. Link-in-bio funnel.
**Undisclosed** — presents as a real person. Reels-only. Text-overlay hooks baked
into frame one (*"POV: You dated an Asian"*, *"Wait until the end 💀"*). Comment-reply
reels. Mild thirst-trap framing. 76K–112K views.
→ *Not our lane* (undisclosed + subscription funnel), but the **hook-in-thumbnail**
discipline transfers directly.

### `@graciebooom` — 495K followers, **5 posts**, 12 following
Recurring family cast (mom, dad, sister). One repeatable bit (*"Dad guesses the
clap"*) reshot as variants. 182K–**2.6M** views.
→ Key lesson: **495K followers off 5 posts.** Format repetition beats volume.
Multi-character consistency is the hard build; we're avoiding it initially.

### `@ai.mikaelatala` — 338K followers, 124 posts, 0 following
Bio: *"Philippines' first AI muse. Hyper-real. Heartfelt. Human-inspired."*
**Openly AI** — flagged in handle AND bio. `SKINITA STUDIO` watermark. Everyday
street scenes, consistent desaturated grade. 102K–136K views.
→ **This is our model.** Proves openly-AI works at scale. Note the view ceiling is
lower than the undisclosed accounts — that is the honest trade.

### Cross-cutting patterns
- Reels-dominant; the Reels tab is the default view on all three.
- The thumbnail **is** the hook — text overlay in frame one.
- Low following counts (0/12/40) — reads as creator, not engagement-farmer.
- Cultural specificity is the differentiator, not attractiveness.
- Serialized repeatable formats >> one-off posts.

---

## 4. The character: Nepali-American

**Why this is strong:** the US South Asian diaspora content space is overwhelmingly
Indian. Nepali specifically is close to unserved despite real diaspora hubs —
Jackson Heights NY, Irving/Fort Worth TX, Boston, Baltimore, Columbus/Akron OH,
Denver, Portland OR. Specificity is the moat, and this is about as specific as it gets.

**Brand-deal categories that map cleanly:** diaspora fintech/remittance (Remitly,
Wise), South Asian beauty, food and grocery brands, travel, telecom.

**The core technical risk:** image models default Nepali features toward generic
South Asian or generic East Asian. Nepali faces span Indo-Aryan and Tibeto-Burman
ancestry, and the models flatten this. **Getting the Soul ID training set right is
the single highest-leverage task in the project** — everything downstream inherits it.

---

## 5. Higgsfield API — verified capabilities

Confirmed against the official SDK (`higgsfield-ai/higgsfield-js`). Note: a
secondary source claiming "the API is not yet open" is **stale and wrong**.

| Need | Endpoint / method |
|---|---|
| Train character identity | `createSoulId()` / `listSoulIds()` |
| Reference identity in a generation | `custom_reference_id` param |
| Stills (Soul 2.0) | `/v1/text2image/soul` |
| Style presets | `getSoulStyles()` |
| Image → video | `/v1/image2video/dop` (incl. TURBO) |
| Lipsync / talking | `/v1/speak/higgsfield` |
| Camera motion presets | `getMotions()` |

**Auth:** OAuth via the hosted MCP connector (preferred), or `Authorization: Key ${HF_API_KEY_ID}:${HF_API_SECRET}` for direct API use.
**Base URL:** `https://platform.higgsfield.ai`
**Pattern:** async — submit to a model endpoint, then poll or use a webhook.

Soul ID trains from ~5 photos minimum (20+ recommended) and persists as a reusable
reference across Soul 2.0, Cinema Studio, and video models. This is the mechanism
that solves character consistency.

---

## 6. Open decisions (resolve before writing the playbook)

- [ ] **Which US city?** Drives every location, background, and cultural detail.
- [ ] **Age and occupation.** Must read unambiguously mid-20s+ (see §7).
- [ ] **Nepali language use** — none / sprinkled phrases / code-switching.
- [ ] **Handle and display name** — must carry the AI disclosure.
- [ ] **Watermark?** `@ai.mikaelatala` uses one; it doubles as studio branding.
- [ ] **First-generation or immigrated?** Changes the whole content voice.

---

## 7. Guardrails (non-negotiable)

- **Character must read unambiguously mid-20s or older.** Youthful-looking
  synthetic personas are a hard line, the fastest route to permanent ban, and
  would destroy the brand-deal endgame.
- **No real person's likeness.** Training data must not reproduce an identifiable
  individual.
- **AI status disclosed** in handle and bio — this is the chosen lane; don't drift.
- **FTC disclosure** on every sponsored post.
- Cultural specificity should read as authentic, not as costume.

---

## 8. Build order (next session)

1. Confirm `mcp__higgsfield__*` tools are loaded and network access works (§2).
2. Resolve §6 decisions.
3. Character bible — locked physical description, wardrobe, world.
4. **Soul ID training set spec** — the highest-leverage artifact (§4).
5. Locked style/grade prompt block for visual consistency.
6. Shot-list library + hook/caption banks.
7. Posting cadence and the first 30 days.
8. Brand-deal positioning and media kit.

**Progress.** Steps 1–3 are done: MCP tools and egress verified (§2), the §6 decisions
resolved, and the bible written (`docs/CHARACTER-BIBLE.md`). Step 4 is under way — the
character sheet that seeds the training set has been generated (`prompts/01-character-sheet.md`,
run 001 in `docs/GENERATION-LOG.md`).

**The sheet is generated but not approved.** The heritage and age reads are hard-fail
gates and need human eyes before the Reference Element is created — nothing downstream
should be built on an unreviewed face.
