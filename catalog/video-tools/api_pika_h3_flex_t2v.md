# Pika H3 Flex: Text to Video (API)

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_pika_h3_flex_t2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pika_h3_flex_t2v-1.webp" width="360" alt="Pika H3 Flex: Text to Video (API) api_pika_h3_flex_t2v-1.webp">

> Generate a clip with synchronized audio from a text prompt with Pika H3 Flex through the partner API, no weights to download. One node covers text to video, image to video and first-last-frame by connecting the optional frame inputs, with 480p to 4K output and 5 to 15 second durations. Ideal for prompt exploration on MiniMax H3 when a local install is not available.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pika_h3_flex_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_pika_h3_flex_t2v.json)

## Details

| | |
|---|---|
| Name | `api_pika_h3_flex_t2v` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | Pika H3 Flex, MiniMax H3 |
| Tags | API, Text to Video, Video |
| Type | API |
| Date | 2026-11-04 |
| Author | ComfyUI |
| Min ComfyUI version | 0.44.1 |
| Usage | 13 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveVideo` #2 | video | api_pika_h3_flex_t2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 1 |  |
| `PikaH3FlexVideoNode` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Pika H3 Flex: Text to Video (API)

**Input Assets**
- none — this template starts from text.

**Pika H3 Flex through the partner API.** The same MiniMax H3 base the local Flex templates use, without downloading weights: write a prompt and get a finished clip with synchronized audio.

---

### What this graph does

1. **Pika H3 Flex Video**: one node takes the prompt and the render settings. `first_frame` and `last_frame` are optional image inputs.
2. **Save Video**: writes `api_pika_h3_flex_t2v.mp4`.

### Prompt format

Use the MiniMax H3 text mode structure, so picture and sound come from one description:

```text
integrated_multimodal_description: [Shot 1] Live-action, cinematic, ... The camera tracks low alongside the board at fast speed ...

overall_soundscape: ...

non_diegetic_music: ...
```

- `integrated_multimodal_description` holds the timeline, the camera vocabulary and any dialogue in `<d>[English] ...</d>`.
- `overall_soundscape` covers wind, impacts and other diegetic sound, `non_diegetic_music` the audience-only score, `N/A` when there is none.
- Keep every described event inside the requested duration.

### Parameters

| Widget | What it does |
|---|---|
| `prompt` | The structured H3 prompt. |
| `resolution` | `480p` to `4k`; `1080p` and above render at 768p and upscale once. |
| `aspect_ratio` | `auto` follows the first connected frame, otherwise the prompt. |
| `duration` | 5 to 15 seconds; 5 s gives 124 frames, about 5.17 s. |
| `rewrite_prompt` | Let the model expand the prompt. Off keeps seeds reproducible and leaves the structured prompt untouched. |
| `seed` | Same seed gives similar, not identical, clips. |

### Measured on this graph

The kite-surfer prompt rendered 1344 x 768, 124 frames, 5.17 s at 24 fps, with generated audio matching the splash.

### Gotchas

- Audio is generated with the picture, so the clip is cut-ready.
- The same seed at a different resolution gives a different video.
- Connect only `first_frame` for image to video, both frames for first-last-frame, neither for text to video.

</details>
