# Gemini Omni 1.2 Flash: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_google_gemini_omni_flash_1_2_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_2_i2v-1.webp" width="360" alt="Gemini Omni 1.2 Flash: Image to Video api_google_gemini_omni_flash_1_2_i2v-1.webp">

> Animate a still: the image becomes the first frame and the prompt carries the motion, camera and sound. Gemini Omni Flash renders picture and audio in one pass, so ambience and voices arrive with the clip.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_2_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_google_gemini_omni_flash_1_2_i2v.json)

## Details

| | |
|---|---|
| Name | `api_google_gemini_omni_flash_1_2_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Gemini Omni 1.2 Flash |
| Tags | API, Image to Video |
| Type | API |
| Date | 2026-11-06 |
| Author | ComfyUI |
| Min ComfyUI version | 0.44.1 |
| Usage | 345 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #11 | image | api_google_gemini_omni_flash_1_2_i2v_input.png |
| output | `SaveVideo` #4 | video | api_google_gemini_omni_flash_1_2_i2v.mp4 |

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

- [api_google_gemini_omni_flash_1_2_i2v_input.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/api_google_gemini_omni_flash_1_2_i2v_input.png) — required workflow input (`input/api_google_gemini_omni_flash_1_2_i2v_input.png`)

Gemini Omni Flash renders picture and sound in one pass, so the ambience and voices arrive with the clip. The still is the first frame; the prompt refers to it as `@Image1`.

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
