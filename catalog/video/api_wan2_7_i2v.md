# Wan2.7: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_wan2_7_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan2_7_i2v-1.webp" width="360" alt="Wan2.7: Image to Video api_wan2_7_i2v-1.webp">

> Upload an image and audio file to generate a video with synchronized sound, using the first and last frames for control.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan2_7_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_wan2_7_i2v.json)

## Details

| | |
|---|---|
| Name | `api_wan2_7_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan2.7 |
| Tags | API, Image to Video, Video |
| Type | API |
| Date | 2026-04-02 |
| Author | ComfyUI |
| Min ComfyUI version | 0.18.4 |
| Usage | 71 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #24 | image | tv_head.png |
| output | `SaveVideo` #32 | video | api_wan2_7_i2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 |  |
| `SaveVideo` | 1 |  |
| `Wan2ImageToVideoApi` | 1 |  |
