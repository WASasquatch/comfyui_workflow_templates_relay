# MiniMax-H3-Image: Text to Image (API)

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_minimax_h3_image_t2i)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_image_t2i-1.webp" width="360" alt="MiniMax-H3-Image: Text to Image (API) api_minimax_h3_image_t2i-1.webp">

> Generate an image from a text prompt with MiniMax-H3-Image through the partner API. One checkpoint covers text-to-image and image editing, generation is distilled to 6 steps with no CFG and returns about 16 MP natively. Ideal for poster, packaging and editorial concepts that need legible text and dense detail.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_image_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_minimax_h3_image_t2i.json)

## Details

| | |
|---|---|
| Name | `api_minimax_h3_image_t2i` |
| Category | Foundation › Image |
| Output | image |
| Models | MiniMax H3 Image |
| Tags | API, Text to Image |
| Type | API |
| Date | 2026-11-10 |
| Author | ComfyUI |
| Min ComfyUI version | 0.45.1 |
| Usage | 143 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #2 | image | api_minimax_h3_image_t2i.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MinimaxH3ImageNode` | 1 |  |
| `SaveImage` | 1 |  |
