# Grok: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_grok_image_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_image_edit-1.webp" width="360" alt="Grok: Image Edit api_grok_image_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_image_edit-2.webp" width="360" alt="Grok: Image Edit api_grok_image_edit-2.webp">

> Upload an image to edit with the Grok model. Generate a modified version with expressive, cinematic visuals

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_grok_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_grok_image_edit` |
| Category | Foundation › Image |
| Output | image |
| Models | Grok |
| Tags | API, Image Edit |
| Type | API |
| Date | 2026-01-28 |
| Author | ComfyUI |
| Min ComfyUI version | 0.21.1 |
| Usage | 2754 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #6 | image | cyberpunk_robot.png |
| output | `SaveImage` #3 | image | api_grok_image_edit.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GrokImageEditNodeV2` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Input Asset</summary>

## Input Asset

- [cyberpunk_robot.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/cyberpunk_robot.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
