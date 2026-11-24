# Kling 3.0: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_v3_t2i-1.webp" width="360" alt="Kling 3.0: Text to Image api_kling_v3_t2i-1.webp">

> Generate an image from a text prompt using the Kling 3.0 model. Input your descriptive text to receive a high-quality, prompt-accurate visual output.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_v3_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling_v3_t2i.json)

## Details

| | |
|---|---|
| Name | `api_kling_v3_t2i` |
| Category | Foundation › Image |
| Media type | image |
| Models | Kling, Kling 3.0 |
| Tags | API, Image, Text to Image |
| Type | API |
| Date | 2026-02-10 |
| Author | ComfyUI |
| Min ComfyUI version | 0.13.0 |
| Usage | 14 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #29 | image | api_kling_v3_t2i.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `KlingImageGenerationNode` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
