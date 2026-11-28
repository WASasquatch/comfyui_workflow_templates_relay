# Gemini Omni 1.2 Flash: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_google_gemini_omni_flash_1_2_r2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_2_r2v-1.webp" width="360" alt="Gemini Omni 1.2 Flash: Reference to Video api_google_gemini_omni_flash_1_2_r2v-1.webp">

> Split a character across two references: image 1 carries the silhouette and armour, image 2 locks the face and detail, and the same identity holds through the whole clip. Gemini Omni Flash renders picture and sound in one pass, so the scene and its audio arrive together.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_2_r2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_google_gemini_omni_flash_1_2_r2v.json)

## Details

| | |
|---|---|
| Name | `api_google_gemini_omni_flash_1_2_r2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Gemini Omni 1.2 Flash |
| Tags | API, Reference to Video |
| Type | API |
| Date | 2026-11-06 |
| Author | ComfyUI |
| Min ComfyUI version | 0.44.1 |
| Usage | 191 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #11 | image | api_google_gemini_omni_flash_1_2_r2v_input_1.png |
| input | `LoadImage` #23 | image | api_google_gemini_omni_flash_1_2_r2v_input_2.png |
| output | `SaveVideo` #4 | video | api_google_gemini_omni_flash_1_2_r2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `GeminiVideoOmniV2` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Assets

- [api_google_gemini_omni_flash_1_2_r2v_input_1.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/api_google_gemini_omni_flash_1_2_r2v_input_1.png) — required workflow input (`input/api_google_gemini_omni_flash_1_2_r2v_input_1.png`)
- [api_google_gemini_omni_flash_1_2_r2v_input_2.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/api_google_gemini_omni_flash_1_2_r2v_input_2.png) — required workflow input (`input/api_google_gemini_omni_flash_1_2_r2v_input_2.png`)

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
