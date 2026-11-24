# Krea 3: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_krea3_image_edit-1.webp" width="360" alt="Krea 3: Image Edit api_krea3_image_edit-1.webp">

> Perform targeted regional edits on an image with Krea 3, changing only the areas you specify while the rest of the picture stays untouched. One image goes in and one edited image comes out. Ideal for e-commerce product restaging, fashion and portrait relighting, and architectural sketch-to-render work.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_krea3_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_krea3_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_krea3_image_edit` |
| Category | Foundation › Image |
| Media type | image |
| Models | Krea 3 |
| Tags | API, Image Edit |
| Type | API |
| Date | 2026-10-15 |
| Author | ComfyUI |
| Min ComfyUI version | 0.41.1 |
| Usage | 578 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #8 | image | wide_format_digital_render.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Krea3ImageNode` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveImageAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Assets

- [wide_format_digital_render.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/wide_format_digital_render.png)



## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
