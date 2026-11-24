# Meshy 7: Text to 3D

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy7_text_to_model-1.webp" width="360" alt="Meshy 7: Text to 3D api_meshy7_text_to_model-1.webp">

> Generate production-ready 3D models from a text prompt with Meshy 7, a text-to-3D model that sets a new standard for geometry alignment, faithfully matching the input's proportions, part placement, and surface details. Ideal for concept art turnarounds, character and prop modeling from sketches, and any workflow where preserving the original design's intent is critical.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy7_text_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_meshy7_text_to_model.json)

## Details

| | |
|---|---|
| Name | `api_meshy7_text_to_model` |
| Category | Foundation › 3D Model |
| Media type | image |
| Models | Meshy |
| Tags | API, 3D |
| Type | API |
| Date | 2026-08-24 |
| Author | ComfyUI |
| Min ComfyUI version | 0.33.4 |
| Usage | 19 |
| Nodes | 7 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveGLB` | 2 | comfy-core |
| `MeshyAnimateModelNode` | 1 | comfy-core |
| `MeshyRefineNode` | 1 | comfy-core |
| `MeshyRigModelNode` | 1 | comfy-core |
| `MeshyTextToModelNode` | 1 | comfy-core |
| `MeshyTextureNode` | 1 | comfy-core |
