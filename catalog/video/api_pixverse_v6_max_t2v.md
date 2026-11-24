# PixVerse V6 Max: Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_pixverse_v6_max_t2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pixverse_v6_max_t2v-1.webp" width="360" alt="PixVerse V6 Max: Text to Video api_pixverse_v6_max_t2v-1.webp">

> Generate videos up to 15 seconds at 1080p from a text prompt with PixVerse V6 Max, the higher-fidelity tier of PixVerse V6, with native audio and multi-shot direction in a single generation. No input files required. Ideal for social ads, product concept clips and short-form storytelling.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pixverse_v6_max_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_pixverse_v6_max_t2v.json)

## Details

| | |
|---|---|
| Name | `api_pixverse_v6_max_t2v` |
| Category | Foundation › Video |
| Output | video |
| Models | PixVerse |
| Tags | API, Text to Video |
| Type | API |
| Date | 2026-10-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.42.5 |
| Usage | 17 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveVideo` #3 | video | api_pixverse_v6_max_t2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 1 |  |
| `PixverseV6TextToVideoNode` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# PixVerse V6 Max: Text to Video

Describe the shot and PixVerse V6 Max renders a single clip with optional native audio, from 360p to 1080p and up to 15 seconds, with no input files required.

## Parameters

- `quality` sets the long edge: 360p is 640 px, 540p 1024 px, 720p 1280 px and 1080p 1920 px.
- `multi_clip` lets the model cut the video into several shots instead of one continuous take.
- `negative_prompt` is the only optional text field on V6 Max; the style presets that PixVerse V6 offers are not part of this tier.
- PixVerse records the seed but does not reproduce a run from it.

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
