# Meshy 7.1: Text to Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_meshy7_1_text_to_model)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy7_1_text_to_model-1.webp" width="360" alt="Meshy 7.1: Text to Model api_meshy7_1_text_to_model-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy7_1_text_to_model-2.webp" width="360" alt="Meshy 7.1: Text to Model api_meshy7_1_text_to_model-2.webp">

> Generate detailed 3D models from text prompts using Meshy 7.1, with an optional Ultra 4K geometry mode that captures fine surface detail like stitching, wood grain, and scales as real geometry. Ideal for game asset creation, product visualization, and 3D printing preparation.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy7_1_text_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_meshy7_1_text_to_model.json)

## Details

| | |
|---|---|
| Name | `api_meshy7_1_text_to_model` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | Meshy |
| Tags | API, Text to 3D |
| Type | API |
| Date | 2026-09-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.37.0 |
| Usage | 14 |
| Nodes | 6 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MeshyAnimateModelNode` | 1 | comfy-core |
| `MeshyRefineNode` | 1 | comfy-core |
| `MeshyRigModelNode` | 1 | comfy-core |
| `MeshyTextToModelNode` | 1 | comfy-core |
| `MeshyTextureNode` | 1 | comfy-core |
| `SaveGLB` | 1 |  |
