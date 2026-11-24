# Wan3.0: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_wan3_0_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan3_0_i2v-1.webp" width="360" alt="Wan3.0: Image to Video api_wan3_0_i2v-1.webp">

> Create up to 30 seconds of high-fidelity video from a single image using Wan 3.0, which supports text, image, audio, and document inputs for versatile scene generation. Produces authentic, realistic footage with unique facial details and believable motion in one pass. Ideal for cinematic storytelling, product visualization, and documentary-style scene recreation.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan3_0_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_wan3_0_i2v.json)

## Details

| | |
|---|---|
| Name | `api_wan3_0_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan3.0 |
| Tags | API, Image to Video |
| Type | API |
| Date | 2026-08-24 |
| Author | ComfyUI |
| Min ComfyUI version | 0.33.4 |
| Usage | 4600 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #6 | image | beetle_rider.png |
| output | `SaveVideo` #8 | video | api_wan3_0_i2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 | comfy-core |
| `Wan3ImageToVideoApi` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Input Asset</summary>

**Input Asset** 

- [beetle_rider.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/beetle_rider.png) — required workflow input (`input/beetle_rider.png`)

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
