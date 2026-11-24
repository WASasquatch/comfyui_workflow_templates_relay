# Seedream 4.0: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream4-1.webp" width="360" alt="Seedream 4.0: Image Edit api_bytedance_seedream4-1.webp">

> Multi-modal AI model for text-to-image and image editing. Generate 2K images in under 2 seconds with natural language control.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream4.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bytedance_seedream4.json)

## Details

| | |
|---|---|
| Name | `api_bytedance_seedream4` |
| Category | Foundation › Image |
| Media type | image |
| Models | ByteDance, Seedream 4.0 |
| Tags | API, Image, Image Edit, Text to Image |
| Type | API |
| Date | 2025-09-11 |
| Author | ComfyUI |
| Min ComfyUI version | 0.33.3 |
| Usage | 974 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #11 | image | comfyui_logo.png |
| output | `SaveImage` #12 | image | api_bytedance_seedream4.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ByteDanceSeedreamNodeV3` | 1 |  |
| `ImageCompare` | 1 |  |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [comfyui_logo.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/comfyui_logo.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
