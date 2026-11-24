# Ideogram 4.5: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_v4_5_t2i-1.webp" width="360" alt="Ideogram 4.5: Text to Image api_ideogram_v4_5_t2i-1.webp">

> Generate images from text prompts using Ideogram 4.5, with controls for canvas size, quality level, automatic prompt rewriting, and seed. No file inputs are required and one image is output. Ideal for typography-led posters, layout-driven design work, marketing visuals, and fast exploration of visual concepts.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_v4_5_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_ideogram_v4_5_t2i.json)

## Details

| | |
|---|---|
| Name | `api_ideogram_v4_5_t2i` |
| Category | Foundation › Image |
| Media type | image |
| Models | Ideogram |
| Tags | Text to Image, API |
| Type | API |
| Date | 2026-09-30 |
| Author | ComfyUI |
| Min ComfyUI version | 0.38.1 |
| Usage | 32 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImageAdvanced` #5 | image | api_ideogram_v4_5_t2i.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `IdeogramTextToImageApi` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
