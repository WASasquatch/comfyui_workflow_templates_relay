# Green Screen: Bria

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_bria_video_green_screen)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_video_green_screen-1.webp" width="360" alt="Green Screen: Bria api_bria_video_green_screen-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_video_green_screen-2.webp" width="360" alt="Green Screen: Bria api_bria_video_green_screen-2.webp">

> Upload a video to generate a green screen version with a transparent or solid background.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_video_green_screen.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bria_video_green_screen.json)

## Details

| | |
|---|---|
| Name | `api_bria_video_green_screen` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | BRIA |
| Tags | Remove Background, API |
| Type | API |
| Date | 2026-06-04 |
| Author | ComfyUI |
| Min ComfyUI version | 0.24.1 |
| Usage | 21 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #5 | video | investigator.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `BriaVideoGreenScreen` | 1 |  |
| `LoadVideo` | 1 |  |
| `SaveVideo` | 1 |  |
