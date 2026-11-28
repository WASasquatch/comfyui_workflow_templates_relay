# Product Ad Cinematic Sequence Generator

[← Product & Ads](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template_sferro21_product_ad.app)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_sferro21_product_ad.app-1.webp" width="360" alt="Product Ad Cinematic Sequence Generator template_sferro21_product_ad.app-1.webp">

> Upload a product image and a cinematic style reference. Generate a sequence of stylized product advertisements with consistent composition and lighting.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_sferro21_product_ad.app.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_sferro21_product_ad.app.json)

## Details

| | |
|---|---|
| Name | `template_sferro21_product_ad.app` |
| Category | Applied › Product & Ads |
| Output | image |
| Models | Nano Banana Pro |
| Tags | API, Image Edit, Style Transfer |
| Type | API |
| Date | 2026-03-16 |
| Author | sferro21 |
| Min ComfyUI version | 0.8.0 |
| Usage | 37 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | golf_ball_in_crocodile_mouth.png |
| input | `LoadImage` #2 | image | comfy_hat.png |
| output | `SaveImage` #5 | image | template_sferro21_product_ad.app.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 | comfy-core |
| `BatchImagesNode` | 1 | comfy-core |
| `GeminiImage2Node` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
