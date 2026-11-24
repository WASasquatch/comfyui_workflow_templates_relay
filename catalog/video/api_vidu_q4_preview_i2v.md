# Vidu Q4 Preview: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_vidu_q4_preview_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_vidu_q4_preview_i2v-1.webp" width="360" alt="Vidu Q4 Preview: Image to Video api_vidu_q4_preview_i2v-1.webp">

> Generate cinematic videos from a single still image using Vidu Q4 Preview, an expressive flagship model built for lifelike character acting, dramatic camera movement, and striking visual effects. Submit 1 image and receive 1 finished video, with support for up to 15 reference images, 3 reference audio clips, and 2K or 4K output. Ideal for short films, marketing content, and social media storytelling.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_vidu_q4_preview_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_vidu_q4_preview_i2v.json)

## Details

| | |
|---|---|
| Name | `api_vidu_q4_preview_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Vidu Q4 |
| Tags | API, Image to Video |
| Type | API |
| Date | 2026-10-07 |
| Author | ComfyUI |
| Min ComfyUI version | 0.39.2 |
| Usage | 28 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #5 | image | model_turquoise_yellow_outfit.png |
| output | `SaveVideo` #6 | video | api_vidu_q4_preview_i2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |
| `Vidu4ImageToVideoNode` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [model_turquoise_yellow_outfit.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/model_turquoise_yellow_outfit.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
