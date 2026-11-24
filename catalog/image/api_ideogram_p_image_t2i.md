# Ideogram P-Image: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_p_image_t2i-1.webp" width="360" alt="Ideogram P-Image: Text to Image api_ideogram_p_image_t2i-1.webp">

> Generate images from text descriptions using Ideogram's fast P-Image model, which delivers quality comparable to leading image models at significantly lower cost and latency. One text prompt is accepted and one image is output, with controls for quality level and resolution. Ideal for rapid iteration in design workflows, high-volume content production, and cost-sensitive A/B testing of visual concepts.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_p_image_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_ideogram_p_image_t2i.json)

## Details

| | |
|---|---|
| Name | `api_ideogram_p_image_t2i` |
| Category | Foundation › Image |
| Media type | image |
| Models | Ideogram |
| Tags | API, Text to Image |
| Type | API |
| Date | 2026-07-30 |
| Author | ComfyUI |
| Min ComfyUI version | 0.29.2 |
| Usage | 15 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImageAdvanced` #13 | image | api_ideogram_p_image_t2i.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `BuildJsonPromptIdeogram` | 1 |  |
| `CreateBoundingBoxes` | 1 |  |
| `IdeogramPImage` | 1 |  |
| `PreviewAny` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
