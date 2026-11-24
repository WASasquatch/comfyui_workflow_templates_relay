# Photo to Blueprint to Model

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_from_photo_2_miniature-1.webp" width="360" alt="Photo to Blueprint to Model api_from_photo_2_miniature-1.webp">

> Transform real building photos into architectural blueprints and then into detailed physical scale models. A complete architectural visualization pipeline from photo to miniature.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_from_photo_2_miniature.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_from_photo_2_miniature.json)

## Details

| | |
|---|---|
| Name | `api_from_photo_2_miniature` |
| Category | Foundation › Image |
| Media type | image |
| Models | Gemini3 Pro Image Preview, Nano Banana Pro, Google |
| Tags | API, Image Edit, Image, 3D |
| Type | API |
| Date | 2025-11-21 |
| Author | ComfyUI |
| Min ComfyUI version | 0.8.0 |
| Usage | 33 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #11 | image | api_from_photo_2_miniature_input_image.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiImage2Node` | 2 |  |
| `SaveImage` | 2 | comfy-core |
| `BatchImagesNode` | 1 |  |
| `LoadImage` | 1 | comfy-core |
