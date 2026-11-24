# Tripo P1: Multiview to Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_tripo_p1_mv_to_model)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_p1_mv_to_model-1.webp" width="360" alt="Tripo P1: Multiview to Model api_tripo_p1_mv_to_model-1.webp">

> Upload an image or multi-view references to generate a clean low-poly 3D model with controlled polygon count and organized topology, ready for export to game engines.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_p1_mv_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_tripo_p1_mv_to_model.json)

## Details

| | |
|---|---|
| Name | `api_tripo_p1_mv_to_model` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | Tripo P1 |
| Tags | 3D, API, Image to 3D |
| Type | API |
| Date | 2026-05-28 |
| Author | ComfyUI |
| Min ComfyUI version | 0.35.1 |
| Usage | 12 |
| Nodes | 9 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #45 | image | wooden_doll.png |
| input | `LoadImage` #47 | image | wooden_doll_left.png |
| input | `LoadImage` #48 | image | wooden_doll_back.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 3 |  |
| `SaveGLB` | 1 | comfy-core |
| `TripoConversionNode` | 1 | comfy-core |
| `TripoP1MultiviewToModelNode` | 1 |  |
| `TripoRetargetNode` | 1 | comfy-core |
| `TripoRigNode` | 1 | comfy-core |
| `TripoTextureNodeV2` | 1 |  |
