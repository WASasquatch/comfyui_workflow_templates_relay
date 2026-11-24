# Image Upscale: Nano Banana Pro

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility_nanobanana_pro_ai_image_fix)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_nanobanana_pro_ai_image_fix-1.webp" width="360" alt="Image Upscale: Nano Banana Pro utility_nanobanana_pro_ai_image_fix-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_nanobanana_pro_ai_image_fix-2.webp" width="360" alt="Image Upscale: Nano Banana Pro utility_nanobanana_pro_ai_image_fix-2.webp">

> Upload an AI-generated image to upscale and enhance details. Generate a 4K output with improved sharpness and coherence using Nano Banana Pro.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_nanobanana_pro_ai_image_fix.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_nanobanana_pro_ai_image_fix.json)

## Details

| | |
|---|---|
| Name | `utility_nanobanana_pro_ai_image_fix` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | Google, Nano Banana Pro |
| Tags | API, Image Upscale |
| Type | API |
| Date | 2026-02-02 |
| Author | ComfyUI |
| Min ComfyUI version | 0.3.71 |
| Usage | 221 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | hovering_figure.png |
| output | `SaveImage` #5 | image | utility_nanobanana_pro_ai_image_fix.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiImage2Node` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
