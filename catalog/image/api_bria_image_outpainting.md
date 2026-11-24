# Bria: Image Outpainting

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_image_outpainting-1.webp" width="360" alt="Bria: Image Outpainting api_bria_image_outpainting-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_image_outpainting-2.webp" width="360" alt="Bria: Image Outpainting api_bria_image_outpainting-2.webp">

> A professional Bria-powered outpainting template designed for seamless image extension and edge-aware scene expansion

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_image_outpainting.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bria_image_outpainting.json)

## Details

| | |
|---|---|
| Name | `api_bria_image_outpainting` |
| Category | Foundation › Image |
| Media type | image |
| Models | BRIA |
| Tags | API, Outpainting |
| Type | API |
| Date | 2026-01-20 |
| Author | ComfyUI |
| Min ComfyUI version | 0.10.0 |
| Usage | 19 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #11 | image | baby_otter.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `BriaImageEditNode` | 1 |  |
| `ImagePadForOutpaint` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `PreviewImage` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
