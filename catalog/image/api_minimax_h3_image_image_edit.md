# MiniMax-H3-Image: Image Edit (API)

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_image_image_edit-1.webp" width="360" alt="MiniMax-H3-Image: Image Edit (API) api_minimax_h3_image_image_edit-1.webp">

> Edit a picture by describing the change, with MiniMax-H3-Image through the partner API. The source is read as <Picture 1> and only what the instruction asks for is rewritten, so props, clothing or set pieces can be swapped without losing the rest of the frame. Ideal for adding or removing a subject, restyling a material or reshaping a composition from a finished render.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_image_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_minimax_h3_image_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_minimax_h3_image_image_edit` |
| Category | Foundation › Image |
| Media type | image |
| Models | MiniMax H3 Image |
| Tags | API, Image, Image Edit |
| Type | API |
| Date | 2026-11-10 |
| Author | ComfyUI |
| Min ComfyUI version | 0.45.1 |
| Usage | 133 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | surreal_rendering_modern.png |
| output | `SaveImage` #4 | image | api_minimax_h3_image_image_edit.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `MinimaxH3ImageNode` | 1 |  |
| `SaveImage` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [surreal_rendering_modern.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/surreal_rendering_modern.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
