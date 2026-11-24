# Image Upscale: Magnific Precise

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_magnific_image_upscale_precise)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_magnific_image_upscale_precise-1.webp" width="360" alt="Image Upscale: Magnific Precise api_magnific_image_upscale_precise-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_magnific_image_upscale_precise-2.webp" width="360" alt="Image Upscale: Magnific Precise api_magnific_image_upscale_precise-2.webp">

> Upload an image to precisely upscale it using the Magnific model, generating a high-resolution version with enhanced detail.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_magnific_image_upscale_precise.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_magnific_image_upscale_precise.json)

## Details

| | |
|---|---|
| Name | `api_magnific_image_upscale_precise` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | Magnific |
| Tags | API, Image Upscale |
| Type | API |
| Date | 2026-02-13 |
| Author | ComfyUI |
| Min ComfyUI version | 0.11.0 |
| Usage | 127 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | young_woman_portrait.png |
| output | `SaveImage` #3 | image | api_magnific_image_upscale_precise.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ImageCompare` | 1 |  |
| `LoadImage` | 1 |  |
| `MagnificImageUpscalerPreciseV2Node` | 1 |  |
| `SaveImage` | 1 |  |
