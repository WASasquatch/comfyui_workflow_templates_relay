# Tripo H3.1: Image to Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo3_1_image_to_model-1.webp" width="360" alt="Tripo H3.1: Image to Model api_tripo3_1_image_to_model-1.webp">

> Upload a reference image of your object. Generate a high-detail 3D model with dense geometry and PBR-ready materials.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo3_1_image_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_tripo3_1_image_to_model.json)

## Details

| | |
|---|---|
| Name | `api_tripo3_1_image_to_model` |
| Category | Foundation › 3D Model |
| Media type | image |
| Models | Tripo |
| Tags | 3D, API, Image to 3D |
| Type | API |
| Date | 2026-05-09 |
| Author | ComfyUI |
| Min ComfyUI version | 0.35.1 |
| Usage | 88 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #10 | image | cybernetic_robot.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 | comfy-core |
| `Save3DAdvanced` | 1 |  |
| `TripoConversionNode` | 1 | comfy-core |
| `TripoImageToModelNodeV2` | 1 |  |
| `TripoRetargetNode` | 1 | comfy-core |
| `TripoRigNode` | 1 | comfy-core |
| `TripoTextureNodeV2` | 1 |  |
