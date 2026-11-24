# Video Extend: Gemini Omni 1.2 Flash

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_2_extend-1.webp" width="360" alt="Video Extend: Gemini Omni 1.2 Flash api_google_gemini_omni_flash_1_2_extend-1.webp">

> Continue a finished clip instead of re-shooting it: the model reads the last frames and keeps the same subject, framing and audio running for the next stretch. A 5-second input becomes a 10-second output without a visible seam.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_2_extend.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_google_gemini_omni_flash_1_2_extend.json)

## Details

| | |
|---|---|
| Name | `api_google_gemini_omni_flash_1_2_extend` |
| Category | Foundation › Video Tools |
| Media type | image |
| Models | Gemini Omni 1.2 Flash |
| Tags | API, Video Extend |
| Type | API |
| Date | 2026-11-06 |
| Author | ComfyUI |
| Min ComfyUI version | 0.44.1 |
| Usage | 28 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #24 | video | api_google_gemini_omni_flash_1_2_extend_input.mp4 |
| output | `SaveVideo` #4 | video | api_google_gemini_omni_flash_1_2_extend.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiVideoOmniV2` | 1 |  |
| `LoadVideo` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [api_google_gemini_omni_flash_1_2_extend_input.mp4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/api_google_gemini_omni_flash_1_2_extend_input.mp4) — required workflow input (`input/api_google_gemini_omni_flash_1_2_extend_input.mp4`)

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
