# MAI Image 2.6 Flash: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openrouter_mai_image_26_flash_image_edit-1.webp" width="360" alt="MAI Image 2.6 Flash: Image Edit api_openrouter_mai_image_26_flash_image_edit-1.webp">

> Edit images with MAI Image 2.6 Flash, Microsoft's fast image-to-image model that transforms a single input image into a refined output. Ideal for quick retouching, style adjustments, and rapid concept iteration.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openrouter_mai_image_26_flash_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openrouter_mai_image_26_flash_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_openrouter_mai_image_26_flash_image_edit` |
| Category | Foundation › Image |
| Media type | image |
| Models | Mai Image 2.6 |
| Tags | API, Image Edit |
| Type | API |
| Date | 2026-09-10 |
| Author | ComfyUI |
| Min ComfyUI version | 0.35.1 |
| Usage | 10 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #6 | image | clothing_shirt_flat.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `OpenRouterImageNode` | 1 | comfy-core |
| `SaveImageAdvanced` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [clothing_shirt_flat.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/clothing_shirt_flat.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
