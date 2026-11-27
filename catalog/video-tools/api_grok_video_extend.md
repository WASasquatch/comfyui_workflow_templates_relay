# Video Extend: Grok

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_grok_video_extend)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_video_extend-1.webp" width="360" alt="Video Extend: Grok api_grok_video_extend-1.webp">

> Upload a short video and a text prompt describing the next scene. Generate a seamless video extension using Grok extend.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_video_extend.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_grok_video_extend.json)

## Details

| | |
|---|---|
| Name | `api_grok_video_extend` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | Grok |
| Tags | API, Video, Video Extend |
| Type | API |
| Date | 2026-03-24 |
| Author | ComfyUI |
| Min ComfyUI version | 0.18.2 |
| Usage | 16 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #1 | video | deep_space_nexus.mp4 |
| output | `SaveVideo` #3 | video | api_grok_video_extend.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GrokVideoExtendNode` | 1 |  |
| `LoadVideo` | 1 |  |
| `SaveVideo` | 1 |  |
