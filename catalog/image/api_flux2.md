# FLUX.2 Pro

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_flux2)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_flux2-1.webp" width="360" alt="FLUX.2 Pro api_flux2-1.webp">

> Generate up to 4MP photorealistic images with multi-reference consistency and professional text rendering.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_flux2.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_flux2.json)

## Details

| | |
|---|---|
| Name | `api_flux2` |
| Category | Foundation › Image |
| Output | image |
| Models | FLUX.2, FLUX |
| Tags | Image Edit, Image, API, Text to Image |
| Type | API |
| Date | 2025-11-26 |
| Author | ComfyUI |
| Min ComfyUI version | 0.21.1 |
| Usage | 44 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #15 | image | api_flux2_input_image_1.png |
| input | `LoadImage` #16 | image | api_flux2_input_image_4.png |
| input | `LoadImage` #18 | image | api_flux2_input_image_3.png |
| input | `LoadImage` #19 | image | api_flux2_input_image_2.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 4 | comfy-core |
| `Flux2ImageNode` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Assets

- [api_flux2_input_image_4.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/api_flux2_input_image_4.png)
- [api_flux2_input_image_1.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/api_flux2_input_image_1.png)
- [api_flux2_input_image_3.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/api_flux2_input_image_3.png)
- [api_flux2_input_image_2.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/api_flux2_input_image_2.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
