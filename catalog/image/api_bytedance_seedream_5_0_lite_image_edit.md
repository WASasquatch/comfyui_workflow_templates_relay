# Seedream 5.0 Lite: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream_5_0_lite_image_edit-1.webp" width="360" alt="Seedream 5.0 Lite: Image Edit api_bytedance_seedream_5_0_lite_image_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream_5_0_lite_image_edit-2.webp" width="360" alt="Seedream 5.0 Lite: Image Edit api_bytedance_seedream_5_0_lite_image_edit-2.webp">

> Upload an image and a text prompt to edit it. Generate a modified image where the details align with your instructions.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream_5_0_lite_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bytedance_seedream_5_0_lite_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_bytedance_seedream_5_0_lite_image_edit` |
| Category | Foundation › Image |
| Media type | image |
| Models | Seedream 5.0 |
| Tags | API, Image Edit |
| Type | API |
| Date | 2026-02-24 |
| Author | ComfyUI |
| Min ComfyUI version | 0.33.3 |
| Usage | 621 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #29 | image | man_with_old_computers.png |
| input | `LoadImage` #32 | image | inflated_character.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 | comfy-core |
| `ByteDanceSeedreamNodeV3` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveImageAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Assets

- [man_with_old_computers.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/man_with_old_computers.png)
- [inflated_character.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/inflated_character.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
