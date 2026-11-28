# HY Image 3.5 Preview: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_tencent_hy_image_3_5_preview_image_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tencent_hy_image_3_5_preview_image_edit-1.webp" width="360" alt="HY Image 3.5 Preview: Image Edit api_tencent_hy_image_3_5_preview_image_edit-1.webp">

> Edit images with the HY Image 3.5 Preview model, which deeply understands user intent through optimized text-and-image organization to deliver high-quality results. Takes 1 image input and produces 1 image output. Ideal for portrait editing, commercial posters, and film/TV marketing materials.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tencent_hy_image_3_5_preview_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_tencent_hy_image_3_5_preview_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_tencent_hy_image_3_5_preview_image_edit` |
| Category | Foundation › Image |
| Output | image |
| Models | HY Image 3.5 |
| Tags | API, Image Edit |
| Type | API |
| Date | 2026-09-21 |
| Author | ComfyUI |
| Min ComfyUI version | 0.37.1 |
| Usage | 152 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #5 | image | futuristic_brutalist_motorcycle.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `HunyuanImageEditApi` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveImageAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [futuristic_brutalist_motorcycle.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/futuristic_brutalist_motorcycle.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
