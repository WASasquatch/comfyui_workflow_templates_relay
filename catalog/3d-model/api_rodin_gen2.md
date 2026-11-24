# Rodin: Gen-2 Image to Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_rodin_gen2)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_rodin_gen2-1.webp" width="360" alt="Rodin: Gen-2 Image to Model api_rodin_gen2-1.webp">

> Generate detailed 4X mesh quality 3D models from photos using Rodin Gen2

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_rodin_gen2.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_rodin_gen2.json)

## Details

| | |
|---|---|
| Name | `api_rodin_gen2` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | Rodin |
| Tags | 3D, API, Image to 3D |
| Type | API |
| Date | 2025-09-27 |
| Author | ComfyUI |
| Min ComfyUI version | 0.23.0 |
| Usage | 12 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #82 | image | api_rodin_gen2_input_image.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `BatchImagesNode` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `Rodin3D_Gen2` | 1 | comfy-core |
| `SaveGLB` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Try to provide the following types of images:
- Provide images from multiple angles.
- Images with a solid color background.

This helps to generate a model that better meets the requirements. Of course, thanks to Rodin's excellent product capabilities, the subject in the unprocessed image can also achieve a good model output.  

## Input Asset

- [api_rodin_gen2_input_image.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/api_rodin_gen2_input_image.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
