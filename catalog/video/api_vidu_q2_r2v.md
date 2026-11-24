# Vidu Q2: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_vidu_q2_r2v-1.webp" width="360" alt="Vidu Q2: Reference to Video api_vidu_q2_r2v-1.webp">

> Generate videos with reference-based consistency for up to 3 subjects, maintaining character and style continuity across the video sequence with cinematic camera movements.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_vidu_q2_r2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_vidu_q2_r2v.json)

## Details

| | |
|---|---|
| Name | `api_vidu_q2_r2v` |
| Category | Foundation › Video |
| Media type | image |
| Models | Vidu Q2, Vidu |
| Tags | Character Reference, Image to Video, API |
| Type | API |
| Date | 2026-01-12 |
| Author | ComfyUI |
| Min ComfyUI version | 0.9.0 |
| Usage | 24 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #40 | image | api_vidu_q2_r2v_red_haired_girl.jpg |
| input | `LoadImage` #42 | image | vintage_robot.jpg |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `Vidu2ReferenceVideoNode` | 1 | comfy-core |
