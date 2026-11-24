# Image Upscale: Nano Banana Pro Illustration

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility_nanobanana_pro_illustration_upscale)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_nanobanana_pro_illustration_upscale-1.webp" width="360" alt="Image Upscale: Nano Banana Pro Illustration utility_nanobanana_pro_illustration_upscale-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_nanobanana_pro_illustration_upscale-2.webp" width="360" alt="Image Upscale: Nano Banana Pro Illustration utility_nanobanana_pro_illustration_upscale-2.webp">

> Upload a stylized art or illustration. Generate a creatively upscaled 4K image with enhanced detail using the Nano Banana Pro model, ideal for marketing or gaming assets.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_nanobanana_pro_illustration_upscale.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_nanobanana_pro_illustration_upscale.json)

## Details

| | |
|---|---|
| Name | `utility_nanobanana_pro_illustration_upscale` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | Gemini3 Pro Image Preview, Google, Nano Banana Pro |
| Tags | API, Image Upscale |
| Type | API |
| Date | 2026-02-02 |
| Author | ComfyUI |
| Min ComfyUI version | 0.3.71 |
| Usage | 33 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | downhill_run.jpg |
| output | `SaveImage` #5 | image | utility_nanobanana_pro_illustration_upscale.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiImage2Node` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
