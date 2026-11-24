# Remove Background: Bria Local

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility-bria_remove_video_background)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-bria_remove_video_background-1.webp" width="360" alt="Remove Background: Bria Local utility-bria_remove_video_background-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-bria_remove_video_background-2.webp" width="360" alt="Remove Background: Bria Local utility-bria_remove_video_background-2.webp">

> Upload a video to remove the background. Generate a new video with a transparent or solid color background.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-bria_remove_video_background.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility-bria_remove_video_background.json)

## Details

| | |
|---|---|
| Name | `utility-bria_remove_video_background` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | BRIA |
| Tags | API, Remove Background |
| Type | API |
| Date | 2026-02-16 |
| Author | ComfyUI |
| Min ComfyUI version | 0.14.0 |
| Usage | 9 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #123 | video | prince_and_phoenix.mp4 |
| output | `SaveVideo` #124 | video | utility-bria_remove_video_background.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `BriaRemoveVideoBackground` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
