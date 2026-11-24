# HappyHorse: Video Edit

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_0_video_edit-1.webp" width="360" alt="HappyHorse: Video Edit api_happyhorse1_0_video_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_0_video_edit-2.webp" width="360" alt="HappyHorse: Video Edit api_happyhorse1_0_video_edit-2.webp">

> Edit a video using text instructions and optional reference images for style transfer or local replacement. Takes a video and up to 5 reference images as input, outputs an edited video.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_0_video_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_happyhorse1_0_video_edit.json)

## Details

| | |
|---|---|
| Name | `api_happyhorse1_0_video_edit` |
| Category | Foundation › Video |
| Media type | image |
| Models | HappyHorse 1.0 |
| Tags | Video Edit, API |
| Type | API |
| Date | 2026-04-27 |
| Author | ComfyUI |
| Min ComfyUI version | 0.20.0 |
| Usage | 24 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #14 | image | urban_man.png |
| input | `LoadVideo` #16 | video | woman_by_tram.mp4 |
| output | `SaveVideo` #6 | video | api_happyhorse1_0_video_edit.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `HappyHorseVideoEditApi` | 1 |  |
| `LoadImage` | 1 |  |
| `LoadVideo` | 1 |  |
| `SaveVideo` | 1 |  |
