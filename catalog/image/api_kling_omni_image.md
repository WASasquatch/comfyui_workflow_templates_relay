# Kling O1: Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_kling_omni_image)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_omni_image-1.webp" width="360" alt="Kling O1: Image api_kling_omni_image-1.webp">

> Generate high-quality images from text prompts using Kling O1, with support for up to 10 reference images to guide style and content. Features flexible aspect ratios and 1K/2K resolution options.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_omni_image.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling_omni_image.json)

## Details

| | |
|---|---|
| Name | `api_kling_omni_image` |
| Category | Foundation › Image |
| Output | image |
| Models | Kling O1 |
| Tags | API, Character Reference, Text to Image |
| Type | API |
| Date | 2026-01-05 |
| Author | ComfyUI |
| Min ComfyUI version | 0.4.0 |
| Usage | 13 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #5 | image | api_kling_omni_image.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `KlingOmniProImageNode` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
