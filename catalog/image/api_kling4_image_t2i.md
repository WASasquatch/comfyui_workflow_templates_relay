# Kling 4.0: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling4_image_t2i-1.webp" width="360" alt="Kling 4.0: Text to Image api_kling4_image_t2i-1.webp">

> Generate one image or a consistent series from a text prompt with Kling 4.0 Image, up to 8K across ten aspect ratios, optionally steered by reference images addressed in the prompt as @Image1.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling4_image_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling4_image_t2i.json)

## Details

| | |
|---|---|
| Name | `api_kling4_image_t2i` |
| Category | Foundation › Image |
| Media type | image |
| Models | Kling, Kling 4.0 |
| Tags | API, Image, Text to Image |
| Type | API |
| Date | 2026-11-17 |
| Author | ComfyUI |
| Min ComfyUI version | 0.13.0 |
| Usage | 0 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImageAdvanced` #2 | image | Kling4.0_image_t2i_00001_.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Kling4ImageNode` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
