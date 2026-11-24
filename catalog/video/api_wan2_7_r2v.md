# Wan2.7: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_wan2_7_r2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan2_7_r2v-1.webp" width="360" alt="Wan2.7: Reference to Video api_wan2_7_r2v-1.webp">

> Upload a reference video and character image to generate a video with consistent character features.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan2_7_r2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_wan2_7_r2v.json)

## Details

| | |
|---|---|
| Name | `api_wan2_7_r2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan2.7 |
| Tags | API, Video, Reference to Video |
| Type | API |
| Date | 2026-04-02 |
| Author | ComfyUI |
| Min ComfyUI version | 0.18.4 |
| Usage | 18 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #4 | image | steampunk_woman_underwater.png |
| input | `LoadImage` #5 | image | x_robot.png |
| output | `SaveVideo` #7 | video | api_wan2_7_r2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `SaveVideo` | 1 |  |
| `Wan2ReferenceVideoApi` | 1 |  |
