# Tripo: Multiview to Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_multiview_to_model-1.webp" width="360" alt="Tripo: Multiview to Model api_tripo_multiview_to_model-1.webp">

> Build 3D models from multiple angles with Tripo's advanced scanner.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_multiview_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_tripo_multiview_to_model.json)

## Details

| | |
|---|---|
| Name | `api_tripo_multiview_to_model` |
| Category | Foundation › 3D Model |
| Media type | image |
| Models | Tripo |
| Tags | Image to 3D, 3D, API |
| Type | API |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Min ComfyUI version | 0.35.1 |
| Usage | 28 |
| Nodes | 9 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #7 | image | api_tripo_multiview_to_model_front_image.jpg |
| input | `LoadImage` #8 | image | api_tripo_multiview_to_model_back_image.jpg |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 | comfy-core |
| `SaveGLB` | 2 | comfy-core |
| `TripoConversionNode` | 1 | comfy-core |
| `TripoMultiviewToModelNode` | 1 | comfy-core |
| `TripoRetargetNode` | 1 | comfy-core |
| `TripoRigNode` | 1 | comfy-core |
| `TripoTextureNode` | 1 | comfy-core |
