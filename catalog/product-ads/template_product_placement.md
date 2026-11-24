# Product Placement

[← Product & Ads](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template_product_placement)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_product_placement-1.webp" width="360" alt="Product Placement template_product_placement-1.webp">

> Swap products into a reference scene while preserving composition and lighting. Generates a final product image and an automatic video prompt for creating polished product videos.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_product_placement.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_product_placement.json)

## Details

| | |
|---|---|
| Name | `template_product_placement` |
| Category | Applied › Product & Ads |
| Output | video |
| Models | Gemini-3.1-Pro, Kling 3.0, Nano Banana 2 |
| Tags | API, Image Edit, Video |
| Type | API |
| Date | 2026-03-30 |
| Author | Julien \| MJM |
| Min ComfyUI version | 0.35.2 |
| Usage | 11 |
| Nodes | 10 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | product_1_product_placement.png |
| input | `LoadImage` #2 | image | product_2_product_placement.png |
| input | `LoadImage` #3 | image | product_3_product_placement.png |
| input | `LoadImage` #5 | image | reference_image_product_placement.png |
| output | `SaveVideo` #10 | video | template_product_placement.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 4 | comfy-core |
| `GeminiNanoBanana2V2` | 1 | comfy-core |
| `GeminiNode` | 1 | comfy-core |
| `KlingVideoNode` | 1 | comfy-core |
| `PreviewAny` | 1 | comfy-core |
| `PreviewImage` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
