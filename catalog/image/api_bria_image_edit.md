# Bria: FIBO 2.0 Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_bria_image_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_image_edit-1.webp" width="360" alt="Bria: FIBO 2.0 Image Edit api_bria_image_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_image_edit-2.webp" width="360" alt="Bria: FIBO 2.0 Image Edit api_bria_image_edit-2.webp">

> Edit an image with Bria FIBO 2.0 by describing the change in plain language, with an optional mask to confine it to one region. FIBO 2.0 is one model for both editing and generation, trained on structured VGL captions, so it holds everything you did not ask to change, and it returns that structured prompt so the edit can be rebuilt or refined from JSON.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bria_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_bria_image_edit` |
| Category | Foundation › Image |
| Output | image |
| Models | BRIA |
| Tags | API, Image Edit |
| Type | API |
| Date | 2026-10-21 |
| Author | ComfyUI |
| Min ComfyUI version | 0.42.3 |
| Usage | 78 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #5 | image | sunlit_rooftop_capture.png |
| output | `SaveImage` #8 | image | api_bria_image_edit.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `BriaImageEditNode` | 1 | comfy-core |
| `ImageCompare` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Image Compare is now only available under Nodes 2.0. Open menu-> Nodes 2.0 to enable/disable it

</details>

<details><summary>MarkdownNote</summary>

## Input Asset

- [sunlit_rooftop_capture.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/sunlit_rooftop_capture.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
