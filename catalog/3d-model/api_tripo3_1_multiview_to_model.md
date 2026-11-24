# Tripo H3.1: Multiview to Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_tripo3_1_multiview_to_model)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo3_1_multiview_to_model-1.webp" width="360" alt="Tripo H3.1: Multiview to Model api_tripo3_1_multiview_to_model-1.webp">

> Upload multiview images of your object. Generate a high-detail 3D model with dense geometry and PBR-ready materials.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo3_1_multiview_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_tripo3_1_multiview_to_model.json)

## Details

| | |
|---|---|
| Name | `api_tripo3_1_multiview_to_model` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | Tripo |
| Tags | API, 3D, Image to 3D |
| Type | API |
| Date | 2026-05-09 |
| Author | ComfyUI |
| Min ComfyUI version | 0.35.1 |
| Usage | 73 |
| Nodes | 9 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #44 | image | castle_front_view.png |
| input | `LoadImage` #45 | image | castle_side_view.png |
| input | `LoadImage` #46 | image | castle_back_view.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 3 | comfy-core |
| `SaveGLB` | 1 | comfy-core |
| `TripoConversionNode` | 1 | comfy-core |
| `TripoMultiviewToModelNode` | 1 | comfy-core |
| `TripoRetargetNode` | 1 | comfy-core |
| `TripoRigNode` | 1 | comfy-core |
| `TripoTextureNodeV2` | 1 |  |
