# Gemini Omni 1.1 Flash: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_google_gemini_omni_flash_1_1_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_1_i2v-1.webp" width="360" alt="Gemini Omni 1.1 Flash: Image to Video api_google_gemini_omni_flash_1_1_i2v-1.webp">

> Generate videos from text prompts or reference images using Gemini Omni 1.1 Flash, a multimodal model that handles text-to-video, image-to-video, keyframe interpolation, and iterative video editing with natural language. Outputs a single MP4 video with optional audio, supporting aspect ratios, resolutions up to 4K, and scene extension. Ideal for cinematic storytelling, product visualization, and rapid video prototyping.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_1_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_google_gemini_omni_flash_1_1_i2v.json)

## Details

| | |
|---|---|
| Name | `api_google_gemini_omni_flash_1_1_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Gemini Omni 1.1 Flash |
| Tags | API, Image to Video |
| Type | API |
| Date | 2026-08-27 |
| Author | ComfyUI |
| Min ComfyUI version | 0.34.2 |
| Usage | 33 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #11 | image | blue_studio_car.png |
| output | `SaveVideo` #8 | video | api_google_gemini_omni_flash_1_1_i2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiVideoOmniV2` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [blue_studio_car.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/blue_studio_car.png) — required workflow input (`input/blue_studio_car.png`)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
