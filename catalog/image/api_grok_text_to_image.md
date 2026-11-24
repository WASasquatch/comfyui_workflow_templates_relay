# Grok: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_text_to_image-1.webp" width="360" alt="Grok: Text to Image api_grok_text_to_image-1.webp">

> Input text prompts to generate high-quality images quickly using the Grok model.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_text_to_image.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_grok_text_to_image.json)

## Details

| | |
|---|---|
| Name | `api_grok_text_to_image` |
| Category | Foundation › Image |
| Media type | image |
| Models | Grok |
| Tags | API, Text to Image |
| Type | API |
| Date | 2026-01-28 |
| Author | ComfyUI |
| Min ComfyUI version | 0.16.1 |
| Usage | 122 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #3 | image | api_grok_text_to_image.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GrokImageNode` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
