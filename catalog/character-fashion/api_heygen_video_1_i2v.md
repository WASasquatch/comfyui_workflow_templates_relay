# HeyGen Video 1.0: Image to Video

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_heygen_video_1_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_video_1_i2v-1.webp" width="360" alt="HeyGen Video 1.0: Image to Video api_heygen_video_1_i2v-1.webp">

> Generate a 5-15 second clip with synchronized dialogue and sound from a single image using HeyGen Video 1.0, which starts on that exact frame and keeps the image's aspect ratio, at 480p or 768p. The prompt drives both the action and the spoken line, and one video is output. Ideal for giving a portrait or product photo a voice, producing talking-head clips without a shoot, and bringing stills to life.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_video_1_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_heygen_video_1_i2v.json)

## Details

| | |
|---|---|
| Name | `api_heygen_video_1_i2v` |
| Category | Applied › Character & Fashion |
| Output | video |
| Models | HeyGen |
| Tags | API, Image to Video |
| Type | API |
| Date | 2026-09-30 |
| Author | ComfyUI |
| Min ComfyUI version | 0.38.1 |
| Usage | 168 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #5 | image | model_red_curls_ring.png |
| output | `SaveVideo` #3 | video | api_heygen_video_1_i2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `HeyGenImageToVideoNode` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Assets

- [model_red_curls_ring.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/model_red_curls_ring.png)

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
