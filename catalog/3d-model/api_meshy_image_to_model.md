# Meshy 6: Image to Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy_image_to_model-1.webp" width="360" alt="Meshy 6: Image to Model api_meshy_image_to_model-1.webp">

> Upload an image and generate a 3D model with Meshy 6. Create characters, objects, or mechanical parts with production-quality geometry and clean topology.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy_image_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_meshy_image_to_model.json)

## Details

| | |
|---|---|
| Name | `api_meshy_image_to_model` |
| Category | Foundation › 3D Model |
| Media type | image |
| Models | Meshy |
| Tags | 3D, Image to 3D, API |
| Type | API |
| Date | 2026-01-19 |
| Author | ComfyUI |
| Min ComfyUI version | 0.33.4 |
| Usage | 23 |
| Nodes | 9 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #8 | image | robot-warrior.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveGLB` | 2 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `MeshyAnimateModelNode` | 1 | comfy-core |
| `MeshyImageToModelNode` | 1 |  |
| `MeshyRefineNode` | 1 | comfy-core |
| `MeshyRigModelNode` | 1 | comfy-core |
| `MeshyTextureNode` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note</summary>

Output model will be auto-saved to "ComfyUI/output/"

Or you can use the export feature in the preview 3D node to download it.

</details>
