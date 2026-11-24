# Mai Image 2.6 Flash: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openrouter_mai_image_26_flash-1.webp" width="360" alt="Mai Image 2.6 Flash: Text to Image api_openrouter_mai_image_26_flash-1.webp">

> Generate images from text prompts with Microsoft's MAI Image 2.6 Flash, a fast, cost-efficient model that emphasizes low latency and high throughput for rapid visual ideation. The workflow takes a single text prompt and produces one image output. Ideal for concept sketches, marketing mockups, and batch asset drafts where speed matters more than final polish.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openrouter_mai_image_26_flash.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openrouter_mai_image_26_flash.json)

## Details

| | |
|---|---|
| Name | `api_openrouter_mai_image_26_flash` |
| Category | Foundation › Image |
| Media type | image |
| Models | Mai Image 2.6 |
| Tags | API, Text to Image |
| Type | API |
| Date | 2026-09-09 |
| Author | ComfyUI |
| Min ComfyUI version | 0.35.1 |
| Usage | 49 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImageAdvanced` #3 | image | api_openrouter_mai_image_26_flash.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `OpenRouterImageNode` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
