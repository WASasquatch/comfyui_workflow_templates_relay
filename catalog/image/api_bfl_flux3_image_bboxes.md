# FLUX 3 Image: Bounding Box Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_bfl_flux3_image_bboxes)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux3_image_bboxes-1.webp" width="360" alt="FLUX 3 Image: Bounding Box Edit api_bfl_flux3_image_bboxes-1.webp">

> Place objects and text where you want them with FLUX 3 Image by feeding boxes from the Create Bounding Boxes node into the prompt, so each box carries its own description and copy into the render. Boxes are relative to the canvas, so set the output to the same aspect ratio. One image is output, up to 4K. Ideal for poster and layout composition, placing headlines and captions, and controlling where subjects sit in the frame.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux3_image_bboxes.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bfl_flux3_image_bboxes.json)

## Details

| | |
|---|---|
| Name | `api_bfl_flux3_image_bboxes` |
| Category | Foundation › Image |
| Output | image |
| Models | FLUX 3 Image |
| Tags | Image Edit, API |
| Type | API |
| Date | 2026-10-01 |
| Author | ComfyUI |
| Min ComfyUI version | 0.38.2 |
| Usage | 53 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | giant_flamingo_balloon_ship_harbor.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CreateBoundingBoxes` | 1 |  |
| `Flux3ImageNode` | 1 |  |
| `ImageCompare` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `PreviewAny` | 1 |  |
| `SaveImageAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [giant_flamingo_balloon_ship_harbor.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/giant_flamingo_balloon_ship_harbor.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
