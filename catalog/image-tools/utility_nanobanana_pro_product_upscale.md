# Image Upscale: Nano Banana Pro Product

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility_nanobanana_pro_product_upscale)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_nanobanana_pro_product_upscale-1.webp" width="360" alt="Image Upscale: Nano Banana Pro Product utility_nanobanana_pro_product_upscale-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_nanobanana_pro_product_upscale-2.webp" width="360" alt="Image Upscale: Nano Banana Pro Product utility_nanobanana_pro_product_upscale-2.webp">

> Upload a product image to enhance its detail and sharpness. Generate an upscaled, high-quality output with improved typography and realistic coherence using the Nano Banana Pro model.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_nanobanana_pro_product_upscale.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_nanobanana_pro_product_upscale.json)

## Details

| | |
|---|---|
| Name | `utility_nanobanana_pro_product_upscale` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | Nano Banana Pro |
| Tags | API, Image Upscale |
| Type | API |
| Date | 2026-02-02 |
| Author | ComfyUI |
| Min ComfyUI version | 0.3.71 |
| Usage | 63 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | orange_beauty_trio.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiImage2Node` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
