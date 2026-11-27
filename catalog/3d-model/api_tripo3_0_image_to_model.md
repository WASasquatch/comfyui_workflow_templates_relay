# Tripo3.0: Image to Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_tripo3_0_image_to_model)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo3_0_image_to_model-1.webp" width="360" alt="Tripo3.0: Image to Model api_tripo3_0_image_to_model-1.webp">

> Transform images or sketches into 3D models with Tripo 3.0's sharp geometry and production-ready PBR textures.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo3_0_image_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_tripo3_0_image_to_model.json)

## Details

| | |
|---|---|
| Name | `api_tripo3_0_image_to_model` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | Tripo |
| Tags | Image to 3D, 3D, API |
| Type | API |
| Date | 2025-12-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.36.0 |
| Usage | 24 |
| Nodes | 11 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | 3d_character_front_view.png |
| input | `LoadImage` #3 | image | 3d_character_back_view.png |
| input | `LoadImage` #4 | image | 3d_character_left_view.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 3 | comfy-core |
| `BatchImagesNode` | 1 | comfy-core |
| `Preview3DAdvanced` | 1 | comfy-core |
| `SaveGLB` | 1 | comfy-core |
| `TripoConversionNode` | 1 | comfy-core |
| `TripoImageToModelNodeV2` | 1 | comfy-core |
| `TripoRetargetNode` | 1 | comfy-core |
| `TripoRigNode` | 1 | comfy-core |
| `TripoTextureNodeV2` | 1 | comfy-core |
