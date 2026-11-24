# Recraft 4.1 flash: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_recraft_v4_1_flash_t2i)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_v4_1_flash_t2i-1.webp" width="360" alt="Recraft 4.1 flash: Text to Image api_recraft_v4_1_flash_t2i-1.webp">

> Generate images from text prompts using Recraft V4.1 Flash, a fast, low-cost model that produces one image output with no file inputs required. Ideal for high-volume generation, rapid iteration, photography and portraits, atmospheric scenes, and quick logo concept exploration.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_v4_1_flash_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_recraft_v4_1_flash_t2i.json)

## Details

| | |
|---|---|
| Name | `api_recraft_v4_1_flash_t2i` |
| Category | Foundation › Image |
| Output | image |
| Models | Recraft |
| Tags | API |
| Type | API |
| Date | 2026-09-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.37.2 |
| Usage | 15 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #5 | image | api_recraft_v4_1_flash_t2i.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `RecraftV4TextToImageNode` | 1 |  |
| `SaveImage` | 1 |  |
