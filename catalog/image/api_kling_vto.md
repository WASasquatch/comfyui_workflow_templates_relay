# Kling: Virtual Try On

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_kling_vto)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_vto-1.webp" width="360" alt="Kling: Virtual Try On api_kling_vto-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_vto-2.webp" width="360" alt="Kling: Virtual Try On api_kling_vto-2.webp">

> Dress a virtual model in any garment by combining a clothing image with a person photo, generating a realistic try-on result alongside a side-by-side comparison view. It accepts flat-lay, mannequin, or on-model clothing shots while preserving the model's face and pose. Ideal for fashion e-commerce previews, styling mockups, and virtual fitting experiences.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_vto.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling_vto.json)

## Details

| | |
|---|---|
| Name | `api_kling_vto` |
| Category | Foundation › Image |
| Output | image |
| Models | Kling |
| Tags | Virtual Try-On |
| Type | API |
| Date | 2026-10-07 |
| Author | ComfyUI |
| Min ComfyUI version | 0.39.2 |
| Usage | 19 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | model_colorful_outfit.png |
| input | `LoadImage` #3 | image | green_floral_dress.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `ImageCompare` | 1 |  |
| `KlingTryOnNode` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveImageAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Assets

- [model_colorful_outfit.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/model_colorful_outfit.png)
- [green_floral_dress.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/green_floral_dress.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
