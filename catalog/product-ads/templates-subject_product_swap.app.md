# Swap Product in Character’s Hand, UGC Style

[← Product & Ads](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-subject_product_swap.app-1.webp" width="360" alt="Swap Product in Character’s Hand, UGC Style templates-subject_product_swap.app-1.webp">

> Upload a photo of a character holding a product and your brands product. Generate an image with the products swapped.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-subject_product_swap.app.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-subject_product_swap.app.json)

## Details

| | |
|---|---|
| Name | `templates-subject_product_swap.app` |
| Category | Applied › Product & Ads |
| Media type | image |
| Models | Gemini3 Pro Image Preview, Google, Nano Banana Pro |
| Tags | API, Image Edit |
| Type | API |
| Date | 2025-12-18 |
| Author | hellorob |
| Min ComfyUI version | 0.8.0 |
| Usage | 15 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #10 | image | subject-girl-holding-skincare-bottle.png |
| input | `LoadImage` #11 | image | product-cleanser.jpeg |

## Subgraphs

- **Batch Images** (3 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 | comfy-core |
| `BatchImagesNode` | 1 |  |
| `GeminiImage2Node` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `ResizeAndPadImage` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
