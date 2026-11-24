# FLUX 3 Video: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux3_i2v-1.webp" width="360" alt="FLUX 3 Video: Image to Video api_bfl_flux3_i2v-1.webp">

> Generate full videos from a single text prompt using FLUX 3, which automatically expands your description into a cohesive scene with synchronized audio, motion, and physics. Outputs one 720p, 24fps MP4 video (5-20 seconds) with support for multi-shot structures and aspect ratios from 9:16 to 21:9. Ideal for product photography, filmic ad campaigns, and dynamic motion graphics.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux3_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bfl_flux3_i2v.json)

## Details

| | |
|---|---|
| Name | `api_bfl_flux3_i2v` |
| Category | Foundation › Video |
| Media type | image |
| Models | FLUX 3 Video |
| Tags | API, Image to Video |
| Type | API |
| Date | 2026-08-04 |
| Author | ComfyUI |
| Min ComfyUI version | 0.30.2 |
| Usage | 21 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #423 | image | space_caravan.png |
| output | `SaveVideo` #422 | video | api_bfl_flux3_i2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Flux3ImageToVideoNode` | 1 |  |
| `LoadImage` | 1 |  |
| `SaveVideo` | 1 |  |
