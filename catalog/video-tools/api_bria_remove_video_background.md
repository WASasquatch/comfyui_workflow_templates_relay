# Remove Background: Bria Solid Color

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_remove_video_background-1.webp" width="360" alt="Remove Background: Bria Solid Color api_bria_remove_video_background-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_remove_video_background-2.webp" width="360" alt="Remove Background: Bria Solid Color api_bria_remove_video_background-2.webp">

> Upload a video to remove its background and replace it with your chosen color. Generate a video with the subject isolated and a new solid background.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_remove_video_background.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bria_remove_video_background.json)

## Details

| | |
|---|---|
| Name | `api_bria_remove_video_background` |
| Category | Foundation › Video Tools |
| Media type | image |
| Models | BRIA |
| Tags | API, Remove Background |
| Type | API |
| Date | 2026-06-04 |
| Author | ComfyUI |
| Min ComfyUI version | 0.14.0 |
| Usage | 35 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #4 | video | spear_warrior.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `BriaRemoveVideoBackground` | 1 |  |
| `LoadVideo` | 1 |  |
| `SaveVideo` | 1 |  |
