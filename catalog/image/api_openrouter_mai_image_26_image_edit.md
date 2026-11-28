# MAI Image 2.6: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_openrouter_mai_image_26_image_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openrouter_mai_image_26_image_edit-1.webp" width="360" alt="MAI Image 2.6: Image Edit api_openrouter_mai_image_26_image_edit-1.webp">

> Edit images with MAI Image 2.6, Microsoft's flagship model for image editing, combining two reference images into a single refined output. Ideal for multi-reference compositing, product visual restyling, and text-in-image design work.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openrouter_mai_image_26_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openrouter_mai_image_26_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_openrouter_mai_image_26_image_edit` |
| Category | Foundation › Image |
| Output | image |
| Models | Mai Image 2.6 |
| Tags | API, Image Edit |
| Type | API |
| Date | 2026-09-10 |
| Author | ComfyUI |
| Min ComfyUI version | 0.35.1 |
| Usage | 12 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #6 | image | product_bottle_black.png |
| input | `LoadImage` #14 | image | ref_product_earbuds_blue.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 | comfy-core |
| `MarkdownNote` | 1 |  |
| `OpenRouterImageNode` | 1 | comfy-core |
| `SaveImageAdvanced` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Assets

- [product_bottle_black.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/product_bottle_black.png)
- [ref_product_earbuds_blue.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/ref_product_earbuds_blue.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
