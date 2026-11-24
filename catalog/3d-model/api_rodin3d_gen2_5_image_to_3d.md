# Rodin Gen2.5: Image to Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_rodin3d_gen2_5_image_to_3d)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_rodin3d_gen2_5_image_to_3d-1.webp" width="360" alt="Rodin Gen2.5: Image to Model api_rodin3d_gen2_5_image_to_3d-1.webp">

> Upload single or multi-view images to create a 3D model with adjustable quality and enhanced texture

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_rodin3d_gen2_5_image_to_3d.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_rodin3d_gen2_5_image_to_3d.json)

## Details

| | |
|---|---|
| Name | `api_rodin3d_gen2_5_image_to_3d` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | Rodin |
| Tags | 3D, API, Image to 3D |
| Type | API |
| Date | 2026-05-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.22.2 |
| Usage | 27 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | bull_robot.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 |  |
| `Rodin3D_Gen25_Image` | 1 |  |
| `SaveGLB` | 1 |  |
