# Muse Image 1.0: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meta_muse_image_image_edit-1.webp" width="360" alt="Muse Image 1.0: Image Edit api_meta_muse_image_image_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meta_muse_image_image_edit-2.webp" width="360" alt="Muse Image 1.0: Image Edit api_meta_muse_image_image_edit-2.webp">

> Edit an image with precision using Muse Image 1.0, following natural language instructions to alter specific elements while preserving the rest of the scene. Takes 2 input images and produces 1 edited output image. Ideal for product photography touch-ups, creative style transfers, and iterative visual refinement.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meta_muse_image_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_meta_muse_image_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_meta_muse_image_image_edit` |
| Category | Foundation › Image |
| Media type | image |
| Models | Muse Image |
| Tags | API, Image Edit |
| Type | API |
| Date | 2026-09-04 |
| Author | ComfyUI |
| Min ComfyUI version | 0.34.4 |
| Usage | 21 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #4 | image | deep_blue_whale_swim_scene.png |
| input | `LoadImage` #5 | image | desert_red_modern_house.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `MarkdownNote` | 1 |  |
| `MetaMuseImageEditApi` | 1 |  |
| `SaveImageAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Assets

- [deep_blue_whale_swim_scene.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/deep_blue_whale_swim_scene.png)
- [desert_red_modern_house.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/desert_red_modern_house.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
