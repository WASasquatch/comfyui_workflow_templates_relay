# PixVerse 6.0: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_pixverse6_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pixverse6_i2v-1.webp" width="360" alt="PixVerse 6.0: Image to Video api_pixverse6_i2v-1.webp">

> Turn a still image into a moving video clip with PixVerse V6, generating up to 15 seconds of footage at resolutions from 360p to 1080p. Supports multiple aspect ratios, integrated audio generation, and multi-shot direction for cohesive narrative flow. Ideal for social media ads, product demonstrations, and short-form storytelling.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pixverse6_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_pixverse6_i2v.json)

## Details

| | |
|---|---|
| Name | `api_pixverse6_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | PixVerse |
| Tags | API, Image to Video |
| Type | API |
| Date | 2026-08-30 |
| Author | ComfyUI |
| Min ComfyUI version | 0.34.0 |
| Usage | 36 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #19 | image | sunny_pink_high_tops.png |
| output | `SaveVideo` #14 | video | api_pixverse6_i2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `PixverseV6ImageToVideoNode` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Input Asset</summary>

## Input Asset

- [sunny_pink_high_tops.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/sunny_pink_high_tops.png) — required workflow input

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
