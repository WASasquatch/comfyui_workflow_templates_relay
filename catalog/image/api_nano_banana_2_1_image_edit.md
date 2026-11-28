# Nano Banana 2.1: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_nano_banana_2_1_image_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_nano_banana_2_1_image_edit-1.webp" width="360" alt="Nano Banana 2.1: Image Edit api_nano_banana_2_1_image_edit-1.webp">

> Edit images with natural language and mask-based local edits powered by Nano Banana 2.1, taking one input image and returning one edited result alongside a side-by-side comparison view. Ideal for brand marketing posters, e-commerce product shots, and multi-round retouching where subjects and text must stay consistent.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_nano_banana_2_1_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_nano_banana_2_1_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_nano_banana_2_1_image_edit` |
| Category | Foundation › Image |
| Output | image |
| Models | Nano Banana |
| Tags | Image Edit, Image, API |
| Type | API |
| Date | 2026-10-06 |
| Author | ComfyUI |
| Min ComfyUI version | 0.39.1 |
| Usage | 2429 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #6 | image | silver_frame_profile.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiNanoBanana2V2` | 1 |  |
| `ImageCompare` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveImageAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [silver_frame_profile.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/silver_frame_profile.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
