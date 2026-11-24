# Remove Background: Bria

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_bria_remove_image_background-1.webp" width="360" alt="Remove Background: Bria utility_bria_remove_image_background-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_bria_remove_image_background-2.webp" width="360" alt="Remove Background: Bria utility_bria_remove_image_background-2.webp">

> Upload an image to automatically remove its background using the Bria API. The workflow processes the request asynchronously and returns the edited image with a transparent background.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_bria_remove_image_background.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_bria_remove_image_background.json)

## Details

| | |
|---|---|
| Name | `utility_bria_remove_image_background` |
| Category | Foundation › Image Tools |
| Media type | image |
| Models | BRIA |
| Tags | API, Image, Remove Background |
| Type | API |
| Date | 2026-02-16 |
| Author | ComfyUI |
| Min ComfyUI version | 0.45.4 |
| Usage | 22 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #26 | image | denim_girl_2k.png |
| output | `SaveImage` #27 | image | utility_bria_remove_image_background.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `BriaRemoveImageBackground` | 1 | comfy-core |
| `ImageCompare` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [denim_girl_2k.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/denim_girl_2k.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
