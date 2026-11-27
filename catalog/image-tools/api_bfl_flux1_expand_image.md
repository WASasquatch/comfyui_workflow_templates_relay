# Image Outpainting: Flux.1

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_bfl_flux1_expand_image)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux1_expand_image-1.webp" width="360" alt="Image Outpainting: Flux.1 api_bfl_flux1_expand_image-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux1_expand_image-2.webp" width="360" alt="Image Outpainting: Flux.1 api_bfl_flux1_expand_image-2.webp">

> Upload an image to expand its canvas using Flux.1. Generate an outpainted image with extended content.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux1_expand_image.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bfl_flux1_expand_image.json)

## Details

| | |
|---|---|
| Name | `api_bfl_flux1_expand_image` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | FLUX, FLUX.1 |
| Tags | API, Outpainting |
| Type | API |
| Date | 2026-02-09 |
| Author | ComfyUI |
| Min ComfyUI version | 0.3.32 |
| Usage | 30 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #17 | image | man_on_desert.png |
| output | `SaveImage` #5 | image | api_bfl_flux1_expand_image.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `FluxProExpandNode` | 1 | comfy-core |
| `LoadImage` | 1 |  |
| `SaveImage` | 1 | comfy-core |
