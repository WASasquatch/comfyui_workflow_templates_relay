# HY 3D: Image to Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_hunyuan3d_image_to_model-1.webp" width="360" alt="HY 3D: Image to Model api_hunyuan3d_image_to_model-1.webp">

> Upload an image to generate a 3D model with geometry and PBR textures.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_hunyuan3d_image_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_hunyuan3d_image_to_model.json)

## Details

| | |
|---|---|
| Name | `api_hunyuan3d_image_to_model` |
| Category | Foundation › 3D Model |
| Media type | image |
| Models | Hunyuan3D |
| Tags | 3D, API, Image to 3D |
| Type | API |
| Date | 2026-05-21 |
| Author | ComfyUI |
| Min ComfyUI version | 0.23.0 |
| Usage | 53 |
| Nodes | 10 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | pink_robot_front.png |
| input | `LoadImage` #10 | image | pink_robot_back.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveImage` | 4 | comfy-core |
| `LoadImage` | 2 | comfy-core |
| `SaveGLB` | 2 | comfy-core |
| `MarkdownNote` | 1 |  |
| `TencentImageToModelNode` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Assets

- [pink_robot_front.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/pink_robot_front.png)
- [pink_robot_back.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/pink_robot_back.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
