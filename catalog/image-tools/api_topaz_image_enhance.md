# Image Upscale: Topaz Reimagine

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_topaz_image_enhance)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_image_enhance-1.webp" width="360" alt="Image Upscale: Topaz Reimagine api_topaz_image_enhance-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_image_enhance-2.webp" width="360" alt="Image Upscale: Topaz Reimagine api_topaz_image_enhance-2.webp">

> Professional image enhancement using Topaz's Reimagine model with face enhancement and detail restoration.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_image_enhance.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_topaz_image_enhance.json)

## Details

| | |
|---|---|
| Name | `api_topaz_image_enhance` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | Reimagine, Topaz |
| Tags | API, Image Upscale |
| Type | API |
| Date | 2025-11-25 |
| Author | ComfyUI |
| Min ComfyUI version | 0.30.2 |
| Usage | 26 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | api_topaz_image_enhance_input_image.webp |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GetImageSize` | 1 |  |
| `ImageCompare` | 1 |  |
| `LoadImage` | 1 |  |
| `ResizeImageMaskNode` | 1 |  |
| `SaveImage` | 1 |  |
| `TopazImageEnhanceV2` | 1 |  |
