# Tripo H3.1: Text to Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_tripo3_1_text_to_model)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo3_1_text_to_model-1.webp" width="360" alt="Tripo H3.1: Text to Model api_tripo3_1_text_to_model-1.webp">

> Generate production-ready 3D hero assets with high-density geometry and PBR materials. Takes text prompts or reference images as input and outputs detailed 3D meshes suitable for close-up renders and game assets.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo3_1_text_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_tripo3_1_text_to_model.json)

## Details

| | |
|---|---|
| Name | `api_tripo3_1_text_to_model` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | Tripo |
| Tags | 3D, API, Text to 3D |
| Type | API |
| Date | 2026-05-09 |
| Author | ComfyUI |
| Min ComfyUI version | 0.35.1 |
| Usage | 11 |
| Nodes | 6 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveGLB` | 1 | comfy-core |
| `TripoConversionNode` | 1 | comfy-core |
| `TripoRetargetNode` | 1 | comfy-core |
| `TripoRigNode` | 1 | comfy-core |
| `TripoTextToModelNodeV2` | 1 |  |
| `TripoTextureNodeV2` | 1 |  |
