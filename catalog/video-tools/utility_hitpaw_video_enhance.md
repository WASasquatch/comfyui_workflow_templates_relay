# Video Upscale: HitPaw

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_hitpaw_video_enhance-1.webp" width="360" alt="Video Upscale: HitPaw utility_hitpaw_video_enhance-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_hitpaw_video_enhance-2.webp" width="360" alt="Video Upscale: HitPaw utility_hitpaw_video_enhance-2.webp">

> Upload a video to enhance and upscale. Generate a restored output with improved clarity, temporal stability, and optional portrait enhancement.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_hitpaw_video_enhance.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_hitpaw_video_enhance.json)

## Details

| | |
|---|---|
| Name | `utility_hitpaw_video_enhance` |
| Category | Foundation › Video Tools |
| Media type | image |
| Models | HitPaw |
| Tags | Video Upscale, API |
| Type | API |
| Date | 2026-02-02 |
| Author | ComfyUI |
| Min ComfyUI version | 0.12.0 |
| Usage | 21 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #12 | video | dad_carry_daughter.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `HitPawVideoEnhance` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
