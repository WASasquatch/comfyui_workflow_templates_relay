# Tripo 2.5: Image to Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_tripo_image_to_model)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_image_to_model-1.webp" width="360" alt="Tripo 2.5: Image to Model api_tripo_image_to_model-1.webp">

> Generate professional 3D assets from 2D images using Tripo engine.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_image_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_tripo_image_to_model.json)

## Details

| | |
|---|---|
| Name | `api_tripo_image_to_model` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | Tripo |
| Tags | 3D, Image to 3D, API |
| Type | API |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Min ComfyUI version | 0.36.0 |
| Usage | 16 |
| Nodes | 8 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #36 | image | api_tripo_image_to_model_input_image.jpg |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveGLB` | 2 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `TripoImageToModelNodeV2` | 1 | comfy-core |
| `TripoRetargetNode` | 1 | comfy-core |
| `TripoRigNode` | 1 | comfy-core |
| `TripoTextureNodeV2` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Output file location</summary>

Output model will be auto saved to "ComfyUI/output/"

Or you can use the export function in the preview 3D node to download it.

</details>
