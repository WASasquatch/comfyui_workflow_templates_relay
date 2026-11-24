# Gemini Omni 1.1 Flash: Video Edit

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_1_edit-1.webp" width="360" alt="Gemini Omni 1.1 Flash: Video Edit api_google_gemini_omni_flash_1_1_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_1_edit-2.webp" width="360" alt="Gemini Omni 1.1 Flash: Video Edit api_google_gemini_omni_flash_1_1_edit-2.webp">

> Edit videos through natural language conversation with Gemini Omni 1.1 Flash. Upload a clip (10 seconds or less) and describe the change: swap backgrounds, restyle scenes, add or remove elements, and the model applies the edit while preserving everything you did not mention. Add \"Keep everything else the same\" for maximum consistency; simple prompts work best. Outputs video with native audio at 16:9 or 9:16, with 1080p/4K output available. Ideal for remixes, style changes, and iterative refinement without re-generating from scratch.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_1_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_google_gemini_omni_flash_1_1_edit.json)

## Details

| | |
|---|---|
| Name | `api_google_gemini_omni_flash_1_1_edit` |
| Category | Foundation › Video |
| Media type | image |
| Models | Gemini Omni 1.1 Flash |
| Tags | API, Video Edit |
| Type | API |
| Date | 2026-08-27 |
| Author | ComfyUI |
| Min ComfyUI version | 0.34.2 |
| Usage | 213 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #14 | video | hooded_wanderer_planet_bridge.mp4 |
| output | `SaveVideo` #8 | video | api_google_gemini_omni_flash_1_1_edit.mp4 |

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

- [hooded_wanderer_planet_bridge.mp4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/hooded_wanderer_planet_bridge.mp4) — required workflow input (`input/hooded_wanderer_planet_bridge.mp4`)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
