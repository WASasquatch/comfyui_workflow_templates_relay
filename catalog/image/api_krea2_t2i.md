# Krea2: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_krea2_t2i-1.webp" width="360" alt="Krea2: Text to Image api_krea2_t2i-1.webp">

> Input a text prompt describing your desired scene. Generate four aesthetic, high-quality images that interpret your prompt with creative variety.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_krea2_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_krea2_t2i.json)

## Details

| | |
|---|---|
| Name | `api_krea2_t2i` |
| Category | Foundation › Image |
| Media type | image |
| Models | Krea 2 |
| Tags | API, Text to Image |
| Type | API |
| Date | 2026-05-27 |
| Author | ComfyUI |
| Min ComfyUI version | 0.24.1 |
| Usage | 72 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #2 | image | api_krea2_t2i.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Krea2ImageNode` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
