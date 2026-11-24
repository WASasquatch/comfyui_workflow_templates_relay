# Wan2.6: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_wan2_6_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan2_6_i2v-1.webp" width="360" alt="Wan2.6: Image to Video api_wan2_6_i2v-1.webp">

> Transform images into high-quality videos with enhanced image quality, smoother motion, 1080P resolution support, and natural movement generation for professional results.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan2_6_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_wan2_6_i2v.json)

## Details

| | |
|---|---|
| Name | `api_wan2_6_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan2.6, Wan |
| Tags | Image to Video, Video, API |
| Type | API |
| Date | 2025-12-20 |
| Author | ComfyUI |
| Min ComfyUI version | 0.5.0 |
| Usage | 33 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #42 | image | red_car.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `WanImageToVideoApi` | 1 | comfy-core |
