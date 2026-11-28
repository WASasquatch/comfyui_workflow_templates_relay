# Magnific: Style Reference

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_magnific_image_style_transfer)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_magnific_image_style_transfer-1.webp" width="360" alt="Magnific: Style Reference api_magnific_image_style_transfer-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_magnific_image_style_transfer-2.webp" width="360" alt="Magnific: Style Reference api_magnific_image_style_transfer-2.webp">

> Upload a target image and a style reference image. Generate a new image that merges the artistic style of the reference with the structure of your target.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_magnific_image_style_transfer.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_magnific_image_style_transfer.json)

## Details

| | |
|---|---|
| Name | `api_magnific_image_style_transfer` |
| Category | Foundation › Image |
| Output | image |
| Models | Magnific |
| Tags | API, Style Reference |
| Type | API |
| Date | 2026-01-26 |
| Author | ComfyUI |
| Min ComfyUI version | 0.11.0 |
| Usage | 15 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #11 | image | girl_riding_unicorn.png |
| input | `LoadImage` #13 | image | magnific_style_reference.png |
| output | `SaveImage` #14 | image | api_magnific_image_style_transfer.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 | comfy-core |
| `MagnificImageStyleTransferNode` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
