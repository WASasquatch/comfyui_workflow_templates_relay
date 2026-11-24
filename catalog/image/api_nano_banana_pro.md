# Nano Banana Pro

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_nano_banana_pro)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_nano_banana_pro-1.webp" width="360" alt="Nano Banana Pro api_nano_banana_pro-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_nano_banana_pro-2.webp" width="360" alt="Nano Banana Pro api_nano_banana_pro-2.webp">

> Nano-banana Pro (Gemini 3.0 Pro Image) - Studio-quality 4K image generation and editing with enhanced text rendering and character consistency.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_nano_banana_pro.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_nano_banana_pro.json)

## Details

| | |
|---|---|
| Name | `api_nano_banana_pro` |
| Category | Foundation › Image |
| Output | image |
| Models | Gemini3 Pro Image Preview, Google, Nano Banana Pro |
| Tags | API, Image, Image Edit |
| Type | API |
| Date | 2025-11-21 |
| Author | ComfyUI |
| Min ComfyUI version | 0.8.0 |
| Usage | 3465 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #11 | image | api_nano_banana_pro_input_image_1.png |
| input | `LoadImage` #12 | image | api_nano_banana_pro_input_image_2.png |
| output | `SaveImage` #30 | image | api_nano_banana_pro.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 | comfy-core |
| `BatchImagesNode` | 1 | comfy-core |
| `GeminiImage2Node` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
