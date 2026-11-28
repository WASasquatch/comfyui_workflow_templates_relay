# FLUX 3 Image: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_bfl_flux3_t2i)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux3_t2i-1.webp" width="360" alt="FLUX 3 Image: Text to Image api_bfl_flux3_t2i-1.webp">

> Generate an image from a text prompt with FLUX 3 Image, which interprets and expands the prompt before generating it, at any of sixteen aspect ratios and up to 4K. Web and image search grounding is on by default and no input files are required. One image is output. Ideal for typography-led posters, layout-driven design work, and fast exploration of visual concepts.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux3_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bfl_flux3_t2i.json)

## Details

| | |
|---|---|
| Name | `api_bfl_flux3_t2i` |
| Category | Foundation › Image |
| Output | image |
| Models | FLUX 3 Image |
| Tags | Text to Image, API |
| Type | API |
| Date | 2026-10-01 |
| Author | ComfyUI |
| Min ComfyUI version | 0.38.2 |
| Usage | 194 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImageAdvanced` #2 | image | api_bfl_flux3_t2i.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Flux3ImageNode` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
