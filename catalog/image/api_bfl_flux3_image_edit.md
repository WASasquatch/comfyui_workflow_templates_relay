# FLUX 3 Image: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_bfl_flux3_image_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux3_image_edit-1.webp" width="360" alt="FLUX 3 Image: Image Edit api_bfl_flux3_image_edit-1.webp">

> Edit or combine up to ten reference images from a text instruction with FLUX 3 Image, referring to them in the prompt as image 1, image 2, and so on. One image is output at any of sixteen aspect ratios and up to 4K, with web and image search grounding on by default. Ideal for character-consistent edits, product and object placement, and multi-reference scene compositing.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux3_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bfl_flux3_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_bfl_flux3_image_edit` |
| Category | Foundation › Image |
| Output | image |
| Models | FLUX 3 Image |
| Tags | Image Edit, API |
| Type | API |
| Date | 2026-10-01 |
| Author | ComfyUI |
| Min ComfyUI version | 0.38.2 |
| Usage | 1366 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #4 | image | fashion_model_green_pilot_coat.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Flux3ImageNode` | 1 |  |
| `ImageCompare` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveImageAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [fashion_model_green_pilot_coat.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/fashion_model_green_pilot_coat.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
