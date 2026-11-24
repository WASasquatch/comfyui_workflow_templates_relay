# Image Upscale: Magnific Creative

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_magnific_image_upscale_creative-1.webp" width="360" alt="Image Upscale: Magnific Creative api_magnific_image_upscale_creative-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_magnific_image_upscale_creative-2.webp" width="360" alt="Image Upscale: Magnific Creative api_magnific_image_upscale_creative-2.webp">

> Upload an image and set the magnification level. Generate an upscaled version of your image with support for up to 16x enlargement.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_magnific_image_upscale_creative.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_magnific_image_upscale_creative.json)

## Details

| | |
|---|---|
| Name | `api_magnific_image_upscale_creative` |
| Category | Foundation › Image Tools |
| Media type | image |
| Models | Magnific |
| Tags | API, Image Upscale |
| Type | API |
| Date | 2026-02-13 |
| Author | ComfyUI |
| Min ComfyUI version | 0.11.0 |
| Usage | 260 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | 1950_new_york.png |
| output | `SaveImage` #3 | image | ComfyUI_00915_.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ImageCompare` | 1 |  |
| `LoadImage` | 1 |  |
| `MagnificImageUpscalerCreativeNode` | 1 |  |
| `SaveImage` | 1 |  |
