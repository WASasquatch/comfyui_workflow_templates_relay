# Nano Banana 2: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_google_nano_banana2_text_to_image)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_nano_banana2_text_to_image-1.webp" width="360" alt="Nano Banana 2: Text to Image api_google_nano_banana2_text_to_image-1.webp">

> Generate images from text prompts using the Nano Banana 2 model, producing one image output with no file inputs required. Ideal for rapid prototyping, concept art generation, and creative exploration.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_nano_banana2_text_to_image.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_google_nano_banana2_text_to_image.json)

## Details

| | |
|---|---|
| Name | `api_google_nano_banana2_text_to_image` |
| Category | Foundation › Image |
| Output | image |
| Models | Nano Banana 2 |
| Tags | API, Text to Image |
| Type | API |
| Date | 2026-06-16 |
| Author | ComfyUI |
| Min ComfyUI version | 0.20.3 |
| Usage | 129 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #9 | image | api_google_nano_banana2_text_to_image.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiNanoBanana2V2` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
