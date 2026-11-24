# Seedance 2.0 Mini: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_mini_r2v-1.webp" width="360" alt="Seedance 2.0 Mini: Reference to Video api_seedance2_0_mini_r2v-1.webp">

> Generate cinematic video from two reference images using Seedance 2.0 Mini, producing a single video output with AI-driven camera motion and consistent character generation. Ideal for storytelling, branded content, and short film creation where shot composition and visual continuity are essential.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_mini_r2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_seedance2_0_mini_r2v.json)

## Details

| | |
|---|---|
| Name | `api_seedance2_0_mini_r2v` |
| Category | Foundation › Video |
| Media type | image |
| Models | Seedance 2.0 |
| Tags | API, Image to Video, Reference to Video |
| Type | API |
| Date | 2026-06-25 |
| Author | ComfyUI |
| Min ComfyUI version | 0.33.2 |
| Usage | 81 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #18 | image | perfume_orange_shot.png |
| input | `LoadImage` #27 | image | asian_model_white_top.png |
| output | `SaveVideo` #20 | video | api_seedance2_0_mini_r2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 | comfy-core |
| `ByteDance2ReferenceNodeV2` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Input Assets</summary>

## Input Assets

- [perfume_orange_shot.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/perfume_orange_shot.png)
- [asian_model_white_top.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/asian_model_white_top.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
