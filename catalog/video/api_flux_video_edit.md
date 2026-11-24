# Flux Video Edit

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_flux_video_edit-1.webp" width="360" alt="Flux Video Edit api_flux_video_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_flux_video_edit-2.webp" width="360" alt="Flux Video Edit api_flux_video_edit-2.webp">

> Edit and transform images with FLUX using simple text prompts. Change characters, objects, backgrounds, styles, or entire scenes while preserving the key details and overall consistency of the original image.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_flux_video_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_flux_video_edit.json)

## Details

| | |
|---|---|
| Name | `api_flux_video_edit` |
| Category | Foundation › Video |
| Media type | image |
| Models | FLUX |
| Tags | API, Video Edit |
| Type | API |
| Date | 2026-09-14 |
| Author | ComfyUI |
| Min ComfyUI version | 0.36.0 |
| Usage | 38 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #2 | video | subway_musician.mp4 |
| output | `SaveVideo` #6 | video | api_flux_video_edit.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `FluxVideoEditNode` | 1 |  |
| `LoadVideo` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [subway_musician.mp4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/subway_musician.mp4)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
