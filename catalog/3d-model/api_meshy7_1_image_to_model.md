# Meshy 7.1: Image to 3D

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_meshy7_1_image_to_model)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy7_1_image_to_model-1.webp" width="360" alt="Meshy 7.1: Image to 3D api_meshy7_1_image_to_model-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy7_1_image_to_model-2.webp" width="360" alt="Meshy 7.1: Image to 3D api_meshy7_1_image_to_model-2.webp">

> Generate a 3D model from a single image using Meshy 7.1's Ultra 4K geometry mode, which produces 4096³ meshes so fine surface detail like stitching, wood grain, and scales becomes real geometry rather than texture. Takes one input image. Ideal for high-fidelity asset creation, detailed prop modeling, and product visualization.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy7_1_image_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_meshy7_1_image_to_model.json)

## Details

| | |
|---|---|
| Name | `api_meshy7_1_image_to_model` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | Meshy |
| Tags | API, Image to 3D |
| Type | API |
| Date | 2026-09-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.37.0 |
| Usage | 102 |
| Nodes | 8 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #8 | image | clay_heart_girl.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `MeshyAnimateModelNode` | 1 | comfy-core |
| `MeshyImageToModelNode` | 1 | comfy-core |
| `MeshyRefineNode` | 1 | comfy-core |
| `MeshyRigModelNode` | 1 | comfy-core |
| `MeshyTextureNode` | 1 | comfy-core |
| `Save3DAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Input Image</summary>

**Input Assets**
- [clay_heart_girl.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/clay_heart_girl.png)

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
