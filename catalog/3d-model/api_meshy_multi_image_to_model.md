# Meshy 6: Multi-Image to Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy_multi_image_to_model-1.webp" width="360" alt="Meshy 6: Multi-Image to Model api_meshy_multi_image_to_model-1.webp">

> Create high-quality 3D models from multiple images using Meshy 6. More photos mean better detail capture, accurate proportions, and cleaner mesh structure.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy_multi_image_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_meshy_multi_image_to_model.json)

## Details

| | |
|---|---|
| Name | `api_meshy_multi_image_to_model` |
| Category | Foundation › 3D Model |
| Media type | image |
| Models | Meshy |
| Tags | 3D, API, Image to 3D |
| Type | API |
| Date | 2026-01-19 |
| Author | ComfyUI |
| Min ComfyUI version | 0.33.4 |
| Usage | 28 |
| Nodes | 12 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #8 | image | joker_front.jpg |
| input | `LoadImage` #12 | image | joker_back.jpg |
| input | `LoadImage` #13 | image | joker_side.jpg |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 3 | comfy-core |
| `SaveGLB` | 2 | comfy-core |
| `MarkdownNote` | 1 |  |
| `MeshyAnimateModelNode` | 1 | comfy-core |
| `MeshyMultiImageToModelNode` | 1 |  |
| `MeshyRefineNode` | 1 | comfy-core |
| `MeshyRigModelNode` | 1 | comfy-core |
| `MeshyTextureNode` | 1 | comfy-core |
| `Preview3D` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note</summary>

Output model will be auto-saved to "ComfyUI/output/"

Or you can use the export feature in the preview 3D node to download it.

</details>
