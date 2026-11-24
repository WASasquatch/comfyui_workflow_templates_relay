# Kling O3: Image Generation

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_o3_image-1.webp" width="360" alt="Kling O3: Image Generation api_kling_o3_image-1.webp">

> Upload up to 10 reference images to guide the synthesis. Generate a new image using the Kling O3 model based on your provided visual inputs.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_o3_image.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling_o3_image.json)

## Details

| | |
|---|---|
| Name | `api_kling_o3_image` |
| Category | Foundation › Image |
| Media type | image |
| Models | Kling O3 |
| Tags | API, Image Edit, Text to Image |
| Type | API |
| Date | 2026-02-10 |
| Author | ComfyUI |
| Min ComfyUI version | 0.13.0 |
| Usage | 66 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #31 | image | vintage_portrait.png |
| input | `LoadImage` #32 | image | Urban_Fashion.png |
| output | `SaveImage` #29 | image | api_kling_o3_image.json |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 | comfy-core |
| `BatchImagesNode` | 1 | comfy-core |
| `KlingOmniProImageNode` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Assets

- [vintage_portrait.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/vintage_portrait.png)
- [Urban_Fashion.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/Urban_Fashion.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
