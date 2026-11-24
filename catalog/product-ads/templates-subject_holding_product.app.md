# Add Product to Character’s Hand, AI UGC

[← Product & Ads](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates-subject_holding_product.app)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-subject_holding_product.app-1.webp" width="360" alt="Add Product to Character’s Hand, AI UGC templates-subject_holding_product.app-1.webp">

> Upload a photo of your character and your product. Generate an image of that character holding the product.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-subject_holding_product.app.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-subject_holding_product.app.json)

## Details

| | |
|---|---|
| Name | `templates-subject_holding_product.app` |
| Category | Applied › Product & Ads |
| Output | image |
| Models | Gemini3 Pro Image Preview, Google, Nano Banana Pro |
| Tags | API, Portrait |
| Type | API |
| Date | 2025-12-18 |
| Author | hellorob |
| Min ComfyUI version | 0.8.0 |
| Usage | 10 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #10 | image | subject-elderly-lady-portrait.png |
| input | `LoadImage` #11 | image | product-toothbrush.png |

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
