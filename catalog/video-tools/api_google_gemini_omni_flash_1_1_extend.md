# Video Extend: Gemini Omni 1.1 Flash

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_google_gemini_omni_flash_1_1_extend)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_1_extend-1.webp" width="360" alt="Video Extend: Gemini Omni 1.1 Flash api_google_gemini_omni_flash_1_1_extend-1.webp">

> Extend an existing video by up to 10 seconds per step, building stories up to 40 seconds total with Gemini Omni 1.1 Flash. The model analyzes the last 10 seconds of context, keeping characters, motion, and audio coherent as the scene continues from where it left off. Optionally attach reference images to introduce new characters mid-story. Works on uploaded clips and previously generated videos; describe how the scene should continue in plain language. Ideal for longer narratives, scene branching, and iterative storytelling.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_1_extend.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_google_gemini_omni_flash_1_1_extend.json)

## Details

| | |
|---|---|
| Name | `api_google_gemini_omni_flash_1_1_extend` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | Gemini Omni 1.1 Flash |
| Tags | Video Extend |
| Type | API |
| Date | 2026-08-27 |
| Author | ComfyUI |
| Min ComfyUI version | 0.34.2 |
| Usage | 16 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #48 | video | rooster_duel_western.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiVideoOmniV2` | 1 |  |
| `LoadVideo` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |
| `Video Slice` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [rooster_duel_western.mp4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/rooster_duel_western.mp4) — required workflow input (`input/rooster_duel_western.mp4`)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
