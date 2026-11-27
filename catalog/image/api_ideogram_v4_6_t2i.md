# Ideogram 4.6: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_ideogram_v4_6_t2i)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_v4_6_t2i-1.webp" width="360" alt="Ideogram 4.6: Text to Image api_ideogram_v4_6_t2i-1.webp">

> Generate images from text prompts using Ideogram 4.6, with native 4K output and controls for canvas size, quality level, prompt rewriting, and seed. No file inputs are required and one image is output. Ideal for typography-led posters, packaging and brand graphics, and photographic scenes that need exact colours.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_v4_6_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_ideogram_v4_6_t2i.json)

## Details

| | |
|---|---|
| Name | `api_ideogram_v4_6_t2i` |
| Category | Foundation › Image |
| Output | image |
| Models | Ideogram |
| Tags | API, Text to Image |
| Type | API |
| Date | 2026-11-19 |
| Author | ComfyUI |
| Min ComfyUI version | 0.46.1 |
| Usage | 77 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #2 | image | api_ideogram_v4_6_t2i.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `IdeogramTextToImageApi` | 1 |  |
| `SaveImage` | 1 |  |
