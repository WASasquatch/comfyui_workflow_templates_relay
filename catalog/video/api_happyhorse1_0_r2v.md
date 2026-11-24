# HappyHorse: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_happyhorse1_0_r2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_0_r2v-1.webp" width="360" alt="HappyHorse: Reference to Video api_happyhorse1_0_r2v-1.webp">

> Generate videos that preserve subject characters from multiple reference images using text prompts. Input up to 9 reference images and a scene description to produce a 3-15 second video output.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_0_r2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_happyhorse1_0_r2v.json)

## Details

| | |
|---|---|
| Name | `api_happyhorse1_0_r2v` |
| Category | Foundation › Video |
| Output | video |
| Models | HappyHorse 1.0 |
| Tags | Reference to Video, API |
| Type | API |
| Date | 2026-04-27 |
| Author | ComfyUI |
| Min ComfyUI version | 0.20.0 |
| Usage | 8 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #14 | image | car_ref.png |
| input | `LoadImage` #18 | image | man_ref.png |
| output | `SaveVideo` #6 | video | api_happyhorse1_0_r2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `HappyHorseReferenceVideoApi` | 1 |  |
| `SaveVideo` | 1 |  |
