# Tripo P1: Image to Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_p1_image_to_model-1.webp" width="360" alt="Tripo P1: Image to Model api_tripo_p1_image_to_model-1.webp">

> Upload a reference image of your subject. Generate a game-ready 3D model with clean topology and optimized polygon budgets

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_p1_image_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_tripo_p1_image_to_model.json)

## Details

| | |
|---|---|
| Name | `api_tripo_p1_image_to_model` |
| Category | Foundation › 3D Model |
| Media type | image |
| Models | Tripo P1 |
| Tags | 3D, API, Image to 3D |
| Type | API |
| Date | 2026-05-28 |
| Author | ComfyUI |
| Min ComfyUI version | 0.35.1 |
| Usage | 14 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #45 | image | knight_with_sword.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 | comfy-core |
| `SaveGLB` | 1 | comfy-core |
| `TripoConversionNode` | 1 | comfy-core |
| `TripoP1ImageToModelNode` | 1 | comfy-core |
| `TripoRetargetNode` | 1 | comfy-core |
| `TripoRigNode` | 1 | comfy-core |
| `TripoTextureNodeV2` | 1 |  |
