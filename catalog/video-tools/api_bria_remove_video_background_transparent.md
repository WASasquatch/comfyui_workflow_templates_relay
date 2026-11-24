# Remove Background: Bria Transparent

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_remove_video_background_transparent-1.webp" width="360" alt="Remove Background: Bria Transparent api_bria_remove_video_background_transparent-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_remove_video_background_transparent-2.webp" width="360" alt="Remove Background: Bria Transparent api_bria_remove_video_background_transparent-2.webp">

> Upload a video and generate its frames with a transparent background, outputting image and mask sequences along with a WebM video supporting an alpha channel.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_remove_video_background_transparent.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bria_remove_video_background_transparent.json)

## Details

| | |
|---|---|
| Name | `api_bria_remove_video_background_transparent` |
| Category | Foundation › Video Tools |
| Media type | image |
| Models | BRIA |
| Tags | API, Remove Background |
| Type | API |
| Date | 2026-06-04 |
| Author | ComfyUI |
| Min ComfyUI version | 0.24.1 |
| Usage | 35 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #5 | video | ad_video_demo.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `BriaTransparentVideoBackground` | 1 |  |
| `GetVideoComponents` | 1 |  |
| `JoinImageWithAlpha` | 1 |  |
| `LoadVideo` | 1 |  |
| `SaveWEBM` | 1 |  |
