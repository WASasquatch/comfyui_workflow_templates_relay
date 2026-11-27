# Runway Aleph2: Video Edit

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_runway_aleph2_video_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_runway_aleph2_video_edit-1.webp" width="360" alt="Runway Aleph2: Video Edit api_runway_aleph2_video_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_runway_aleph2_video_edit-2.webp" width="360" alt="Runway Aleph2: Video Edit api_runway_aleph2_video_edit-2.webp">

> Generate a single edited video that preserves original motion and timing while applying your chosen changes. Ideal for portrait and product relighting, consistent lighting across photo sets, and e-commerce apparel presentation.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_runway_aleph2_video_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_runway_aleph2_video_edit.json)

## Details

| | |
|---|---|
| Name | `api_runway_aleph2_video_edit` |
| Category | Foundation › Video |
| Output | video |
| Models | Runway |
| Tags | API, Video Edit |
| Type | API |
| Date | 2026-06-15 |
| Author | ComfyUI |
| Min ComfyUI version | 0.25.0 |
| Usage | 33 |
| Nodes | 8 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #3 | image | example.png |
| input | `LoadVideo` #4 | video | sunset_city_skateboarder.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `RunwayAleph2KeyframeNode` | 1 | comfy-core |
| `RunwayAleph2PromptImageNode` | 1 | comfy-core |
| `RunwayAleph2VideoToVideoNode` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Runway Aleph 2 is Runway's flagship **in-context video editing** model. It edits footage you already have while **preserving the original motion and timing** — no reshoots, no frame-by-frame retouching.

Typical uses:
- **Restyle**: dark anime look, seasonal or lighting changes
- **Change elements**: product color, hairstyle, clothing, add/remove objects
- **Reframe**: tighter shot on a subject at the same moment
- **Multi-shot edits**: apply a change across relevant cuts in one clip

> Only changes what you ask for; background, lighting, and untouched details stay as they were.

## Basic workflow (text prompt only)

1. **Load Video** — source clip (2–30 seconds, ≤30 fps)
2. **Runway Aleph2 Video to Video** — English prompt describing the edit (1–1000 characters)
3. **Save Video** — write the result

Requires a logged-in ComfyUI `comfy.org` API account (Partner node).

## Optional: timed guidance images (per-moment / per-frame)

Besides text, you can attach up to **5** reference images at specific moments on the timeline. Use **one or the other** — do not connect both `keyframes` and `prompt_images`:

### Keyframes — anchored to the **input (source) video**

`Runway Aleph2 Keyframe` → main node `keyframes`

Place a guidance image at a point on the **original** timeline so the edit near that frame follows that look (edit one frame, carry through the clip).

**Timing modes:**
| Mode | Meaning | Example |
|------|---------|--------|
| **Absolute time (seconds)** | Seconds from the start | `2.5` = at 2.5s |
| **Fraction of duration (0.0–1.0)** | Fraction of clip length | `0.5` = midpoint |

### Prompt images — anchored to the **output (result) video**

`Runway Aleph2 Prompt Image` → main node `prompt_images`

Specify what the **generated** video should look like at a moment on the **output** timeline (useful to lock in a look at one frame before generating the full clip).

**Position modes:** same two options as above, but relative to the **output** video.

### Chaining multiple guidance images

Feed the previous node's `keyframes` or `prompt_images` output into the optional input of the next node of the same type. Chain up to 5 images.

## Main node parameters

| Parameter | Description |
|-----------|-------------|
| **prompt** | English description of the desired change |
| **seed** | Random seed; `randomize` gives a new value each run |
| **public_figure_threshold** | Public-figure moderation: `low` is less strict, `auto` is default |

## Limits

- Video **2–30 seconds**, frame rate **≤ 30 fps**; output resolution matches input
- **Keyframes OR prompt images** — not both at once
- At most **5** guidance images per type; absolute seconds must not exceed video duration

</details>
