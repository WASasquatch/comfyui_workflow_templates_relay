# Seedance2.0 4K: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_seedance2_0_r2v_4k)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_r2v_4k-1.webp" width="360" alt="Seedance2.0 4K: Reference to Video api_seedance2_0_r2v_4k-1.webp">

> Generate a reference-based video from a single input image using Seedance 2.0, producing native 4K output with 10-bit color depth and clean fine detail retention. The workflow takes 1 image and outputs 1 video. Ideal for high-resolution motion graphics, cinematic VFX shots requiring downstream grading, and professional video production where 4K finishing is essential.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_r2v_4k.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_seedance2_0_r2v_4k.json)

## Details

| | |
|---|---|
| Name | `api_seedance2_0_r2v_4k` |
| Category | Foundation › Video |
| Output | video |
| Models | Seedance 2.0 |
| Tags | API, Image to Video, Reference to Video |
| Type | API |
| Date | 2026-06-30 |
| Author | ComfyUI |
| Min ComfyUI version | 0.33.2 |
| Usage | 20 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #3 | image | green_rider.png |
| output | `SaveVideo` #4 | video | api_seedance2_0_r2v_4k.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ByteDance2ReferenceNodeV2` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [green_rider.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/green_rider.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
