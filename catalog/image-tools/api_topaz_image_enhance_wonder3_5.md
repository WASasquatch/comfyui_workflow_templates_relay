# Image Upscale: Topaz Wonder 3.5

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_topaz_image_enhance_wonder3_5)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_image_enhance_wonder3_5-1.webp" width="360" alt="Image Upscale: Topaz Wonder 3.5 api_topaz_image_enhance_wonder3_5-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_image_enhance_wonder3_5-2.webp" width="360" alt="Image Upscale: Topaz Wonder 3.5 api_topaz_image_enhance_wonder3_5-2.webp">

> Upscale and enhance a single image using Topaz's Wonder 3.5 generative model, which adds fine detail, reduces noise, and sharpens text and structured graphics while offering Low, Medium, and High enhancement strengths. The workflow takes 1 input image and produces 1 enhanced output alongside a side-by-side comparison view. Ideal for restoring old or compressed photos, improving product shots and marketing visuals, and preparing low-resolution images for print or large-format display.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_image_enhance_wonder3_5.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_topaz_image_enhance_wonder3_5.json)

## Details

| | |
|---|---|
| Name | `api_topaz_image_enhance_wonder3_5` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | Topaz |
| Tags | API, Image Upscale |
| Type | API |
| Date | 2026-08-04 |
| Author | ComfyUI |
| Min ComfyUI version | 0.30.2 |
| Usage | 126 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #3 | image | wild_run.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ImageCompare` | 1 |  |
| `LoadImage` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
| `TopazImageEnhanceV2` | 1 |  |
