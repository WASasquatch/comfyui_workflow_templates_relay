# Replace Background: Bria

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_bria_video_replace_background)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_video_replace_background-1.webp" width="360" alt="Replace Background: Bria api_bria_video_replace_background-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_video_replace_background-2.webp" width="360" alt="Replace Background: Bria api_bria_video_replace_background-2.webp">

> Upload a video and a background image. Detect the main subject and replace the original background with the provided image. Ideal for content creation, virtual production, and background cleanup in video projects.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_video_replace_background.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bria_video_replace_background.json)

## Details

| | |
|---|---|
| Name | `api_bria_video_replace_background` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | BRIA |
| Tags | API, Video Edit, Remove Background |
| Type | API |
| Date | 2026-06-10 |
| Author | ComfyUI |
| Min ComfyUI version | 0.24.1 |
| Usage | 21 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #4 | video | stained_window_vintage_woman.mp4 |
| input | `LoadImage` #8 | image | gothic_hall_light_rays.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `BriaVideoReplaceBackground` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
