# Vidu Q4 Preview: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_vidu_q4_preview_r2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_vidu_q4_preview_r2v-1.webp" width="360" alt="Vidu Q4 Preview: Reference to Video api_vidu_q4_preview_r2v-1.webp">

> Generate expressive videos from two reference images using Vidu Q4 Preview, a flagship model built for vivid character performance, dynamic camera language, and striking visual effects. Ideal for character-driven storytelling, cinematic action sequences, and effect-heavy scenes with explosions, smoke, or particles.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_vidu_q4_preview_r2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_vidu_q4_preview_r2v.json)

## Details

| | |
|---|---|
| Name | `api_vidu_q4_preview_r2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Vidu Q4 |
| Tags | API, Reference to Video |
| Type | API |
| Date | 2026-10-07 |
| Author | ComfyUI |
| Min ComfyUI version | 0.39.2 |
| Usage | 32 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #10 | image | clay_man_smiley_sweater.png |
| input | `LoadImage` #11 | image | yellow_fuzzy_smiley.png |
| output | `SaveVideo` #6 | video | api_vidu_q4_preview_r2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |
| `Vidu4ReferenceVideoNode` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [yellow_fuzzy_smiley.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/yellow_fuzzy_smiley.png)
- [clay_man_smiley_sweater.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/clay_man_smiley_sweater.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
