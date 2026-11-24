# HappyHorse 1.1: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_1_i2v-1.webp" width="360" alt="HappyHorse 1.1: Image to Video api_happyhorse1_1_i2v-1.webp">

> Animate a static first frame into a short video with synchronized audio using HappyHorse 1.1, taking 1 input image and producing 1 video output. Ideal for e-commerce product demos, brand marketing content, and short episodic series.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_1_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_happyhorse1_1_i2v.json)

## Details

| | |
|---|---|
| Name | `api_happyhorse1_1_i2v` |
| Category | Foundation › Video |
| Media type | image |
| Models | HappyHorse 1.1 |
| Tags | API, Image to Video |
| Type | API |
| Date | 2026-06-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.26.1 |
| Usage | 11 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #14 | image | girl_lean_on_horse.png |
| output | `SaveVideo` #13 | video | api_happyhorse1_1_i2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `HappyHorseImageToVideoApi` | 1 |  |
| `LoadImage` | 1 |  |
| `SaveVideo` | 1 |  |
