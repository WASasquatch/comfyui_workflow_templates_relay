# Character Turnaround Sheet Generator

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_google_nano_banana_create_turnaround_sheet)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_nano_banana_create_turnaround_sheet-1.webp" width="360" alt="Character Turnaround Sheet Generator api_google_nano_banana_create_turnaround_sheet-1.webp">

> Create orthographic multi-view character turnaround sheet from one reference image, keep consistent character features across front, side and back views, for sci-fi mech and armor character design.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_nano_banana_create_turnaround_sheet.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_google_nano_banana_create_turnaround_sheet.json)

## Details

| | |
|---|---|
| Name | `api_google_nano_banana_create_turnaround_sheet` |
| Category | Foundation › Image |
| Output | image |
| Models | Nano Banana |
| Tags | API, Image Edit |
| Type | API |
| Date | 2026-09-09 |
| Author | ComfyUI |
| Min ComfyUI version | 0.34.0 |
| Usage | 108 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #3 | image | white_mech_front_ortho.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiImage2Node` | 1 |  |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveImageAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [white_mech_front_ortho.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/white_mech_front_ortho.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
