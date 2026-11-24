# Muse Image 1.0: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meta_muse_image_t2i-1.webp" width="360" alt="Muse Image 1.0: Text to Image api_meta_muse_image_t2i-1.webp">

> Generate images from text prompts using Meta's Muse Image 1.0 model, which follows instructions faithfully, edits with precision, and composes from multiple references. The workflow takes no file inputs and produces 1 image output, with a Save Image Advanced node handling the final render. Ideal for creative concept exploration, rapid visual prototyping, and producing polished marketing or social media imagery.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meta_muse_image_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_meta_muse_image_t2i.json)

## Details

| | |
|---|---|
| Name | `api_meta_muse_image_t2i` |
| Category | Foundation › Image |
| Media type | image |
| Models | Muse Image |
| Tags | API, Text to Image |
| Type | API |
| Date | 2026-09-04 |
| Author | ComfyUI |
| Min ComfyUI version | 0.34.4 |
| Usage | 19 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImageAdvanced` #2 | image | muse_image_1.0.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MetaMuseImageTextToImageApi` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
