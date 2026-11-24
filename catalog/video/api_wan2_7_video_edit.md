# Wan2.7: Video Edit

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan2_7_video_edit-1.webp" width="360" alt="Wan2.7: Video Edit api_wan2_7_video_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan2_7_video_edit-2.webp" width="360" alt="Wan2.7: Video Edit api_wan2_7_video_edit-2.webp">

> Upload a video and corresponding images to edit and replace characters or scenes using the Wan2.7 model.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan2_7_video_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_wan2_7_video_edit.json)

## Details

| | |
|---|---|
| Name | `api_wan2_7_video_edit` |
| Category | Foundation › Video |
| Media type | image |
| Models | Wan2.7 |
| Tags | API, Video, Video Edit |
| Type | API |
| Date | 2026-04-02 |
| Author | ComfyUI |
| Min ComfyUI version | 0.18.4 |
| Usage | 64 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #1 | video | play_chess.mp4 |
| input | `LoadImage` #2 | image | old_bear.png |
| input | `LoadImage` #3 | image | funny_dog.png |
| output | `SaveVideo` #5 | video | api_wan2_7_video_edit.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `LoadVideo` | 1 |  |
| `SaveVideo` | 1 |  |
| `Wan2VideoEditApi` | 1 |  |
