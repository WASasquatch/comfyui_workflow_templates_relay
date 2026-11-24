# Nano Banana 2 Lite: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_nano_banana_2_lite_t2i-1.webp" width="360" alt="Nano Banana 2 Lite: Text to Image api_nano_banana_2_lite_t2i-1.webp">

> Generate images from text descriptions using the ultra-fast Gemini 3.1 Flash-Lite Image model, designed for rapid creation and iteration with no file inputs required. This workflow produces one or more generated images based on your text prompt, with support for interleaved text and image inputs. Ideal for quick concept visualization, rapid prototyping, and iterative design exploration.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_nano_banana_2_lite_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_nano_banana_2_lite_t2i.json)

## Details

| | |
|---|---|
| Name | `api_nano_banana_2_lite_t2i` |
| Category | Foundation › Image |
| Media type | image |
| Models | Nano Banana 2 |
| Tags | API, Text to Image |
| Type | API |
| Date | 2026-06-30 |
| Author | ComfyUI |
| Min ComfyUI version | 0.27.0 |
| Usage | 16 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImageAdvanced` #4 | image | api_nano_banana_2_lite_t2i.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiNanoBanana2V2` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
