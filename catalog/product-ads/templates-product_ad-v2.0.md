# Swap Product Into a Reference AD

[← Product & Ads](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-product_ad-v2.0-1.webp" width="360" alt="Swap Product Into a Reference AD templates-product_ad-v2.0-1.webp">

> Create static ads for your product in the style of a reference advertisement

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-product_ad-v2.0.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-product_ad-v2.0.json)

## Details

| | |
|---|---|
| Name | `templates-product_ad-v2.0` |
| Category | Applied › Product & Ads |
| Media type | image |
| Models | Gemini3 Pro Image Preview, Nano Banana Pro, Google, ByteDance, Seedance |
| Tags | API, Style Reference |
| Type | API |
| Date | 2025-12-03 |
| Author | hellorob |
| Min ComfyUI version | 0.8.0 |
| Usage | 20 |
| Nodes | 10 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | reference_ad.png |
| input | `LoadImage` #2 | image | comfy_gpu.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 | comfy-core |
| `PrimitiveStringMultiline` | 2 | comfy-core |
| `GeminiImage2Node` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `ImageBatch` | 1 | comfy-core |
| `RegexReplace` | 1 | comfy-core |
| `ResizeAndPadImage` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
