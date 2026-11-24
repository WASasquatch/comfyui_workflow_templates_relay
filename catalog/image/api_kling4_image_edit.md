# Kling 4.0: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling4_image_edit-1.webp" width="360" alt="Kling 4.0: Image Edit api_kling4_image_edit-1.webp">

> Restyle one reference portrait with Kling 4.0 Image: keep the same face and framing, then change the hair, the makeup, the outfit or the whole look from a text prompt. Add up to ten reference images and address them as @Image1 onwards.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling4_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling4_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_kling4_image_edit` |
| Category | Foundation › Image |
| Media type | image |
| Models | Kling, Kling 4.0 |
| Tags | API, Image, Image Edit |
| Type | API |
| Date | 2026-11-17 |
| Author | ComfyUI |
| Min ComfyUI version | 0.13.0 |
| Usage | 0 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | kling4_image_edit_portrait.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Kling4ImageNode` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveImageAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Assets

- [kling4_image_edit_portrait.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/kling4_image_edit_portrait.png)

Keep this reference face in the LoadImage node and change only the clothing, hair or makeup in the prompt. The node passes it in as `@Image1`.

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
