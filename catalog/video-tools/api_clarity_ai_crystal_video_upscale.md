# Clarity AI: Crystal Video Upscaler

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_clarity_ai_crystal_video_upscale)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_clarity_ai_crystal_video_upscale-1.webp" width="360" alt="Clarity AI: Crystal Video Upscaler api_clarity_ai_crystal_video_upscale-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_clarity_ai_crystal_video_upscale-2.webp" width="360" alt="Clarity AI: Crystal Video Upscaler api_clarity_ai_crystal_video_upscale-2.webp">

> Upscale a video with Clarity AI's Crystal model, running through the Fal proxy: one video in, one upscaled video out. Set scale_factor to multiply the frame size, and the output keeps the source resolution, frame count and audio track. The result is capped at 9 megapixels per frame and 360 megapixel-seconds per clip, so long or oversized clips come back upscaled by less than the factor you asked for. Ideal for restoring generated clips, preparing footage for large screens, and sharpening soft AI video.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_clarity_ai_crystal_video_upscale.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_clarity_ai_crystal_video_upscale.json)

## Details

| | |
|---|---|
| Name | `api_clarity_ai_crystal_video_upscale` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | Crystal Upscaler |
| Tags | API, Video Upscale |
| Type | API |
| Date | 2026-10-19 |
| Author | ComfyUI |
| Min ComfyUI version | 0.42.2 |
| Usage | 65 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #1 | video | desert_highway_encounter.mp4 |
| output | `SaveVideo` #3 | video | api_clarity_ai_crystal_video_upscale.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ClarityCrystalVideoUpscaleNode` | 1 |  |
| `LoadVideo` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Clarity AI Crystal Video Upscaler

Upscale a video with Clarity AI's Crystal model, running through the Fal proxy.

### How to use

1. Sign in with your ComfyUI account before queueing: this node runs on Comfy's servers.
2. Load a video in **Load Video**. Any resolution and length works.
3. Set `scale_factor` to multiply width and height. 2.0 doubles both dimensions.
4. Queue the prompt, then preview or save the result.

### Limits

The output is capped at **9 megapixels per frame** and **360 megapixel-seconds per clip**, so very large frames or long clips are upscaled by less than the factor you asked for. Resolution, frame count, and the audio track are preserved.

</details>
