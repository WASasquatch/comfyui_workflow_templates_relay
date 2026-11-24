# HappyHorse: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_happyhorse1_0_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_0_i2v-1.webp" width="360" alt="HappyHorse: Image to Video api_happyhorse1_0_i2v-1.webp">

> Generate high-quality, fluid videos from images using HappyHorse-1.0-I2V with realistic dynamic rendering and accurate text and image semantic comprehension.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_0_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_happyhorse1_0_i2v.json)

## Details

| | |
|---|---|
| Name | `api_happyhorse1_0_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | HappyHorse 1.0 |
| Tags | API, Image to Video |
| Type | API |
| Date | 2026-04-27 |
| Author | ComfyUI |
| Min ComfyUI version | 0.20.0 |
| Usage | 20 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #14 | image | pink_city_horse.png |
| output | `SaveVideo` #6 | video | api_happyhorse1_0_i2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `HappyHorseImageToVideoApi` | 1 |  |
| `LoadImage` | 1 |  |
| `SaveVideo` | 1 |  |
