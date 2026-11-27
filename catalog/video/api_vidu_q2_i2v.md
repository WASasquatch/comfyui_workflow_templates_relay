# Vidu Q2: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_vidu_q2_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_vidu_q2_i2v-1.webp" width="360" alt="Vidu Q2: Image to Video api_vidu_q2_i2v-1.webp">

> Transform static images into dynamic 1080p videos with cinematic camera control, multi-subject consistency

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_vidu_q2_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_vidu_q2_i2v.json)

## Details

| | |
|---|---|
| Name | `api_vidu_q2_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Vidu Q2, Vidu |
| Tags | Image to Video, API |
| Type | API |
| Date | 2026-01-12 |
| Author | ComfyUI |
| Min ComfyUI version | 0.9.0 |
| Usage | 71 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #40 | image | cozy_bear.jpg |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `Vidu2ImageToVideoNode` | 1 | comfy-core |
