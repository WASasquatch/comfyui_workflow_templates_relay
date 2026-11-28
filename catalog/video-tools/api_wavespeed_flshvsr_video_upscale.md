# Video Upscale: WaveSpeed FlashVSR

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_wavespeed_flshvsr_video_upscale)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wavespeed_flshvsr_video_upscale-1.webp" width="360" alt="Video Upscale: WaveSpeed FlashVSR api_wavespeed_flshvsr_video_upscale-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wavespeed_flshvsr_video_upscale-2.webp" width="360" alt="Video Upscale: WaveSpeed FlashVSR api_wavespeed_flshvsr_video_upscale-2.webp">

> Upload a video to upscale it to 720p, 1080p, 2K, or 4K. The workflow enhances detail, reduces artifacts, and ensures consistent motion for a high-quality, natural-looking output.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wavespeed_flshvsr_video_upscale.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_wavespeed_flshvsr_video_upscale.json)

## Details

| | |
|---|---|
| Name | `api_wavespeed_flshvsr_video_upscale` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | FlashVSR, WaveSpeed |
| Tags | API, Video Upscale |
| Type | API |
| Date | 2026-01-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.11.0 |
| Usage | 50 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #4 | video | lighter.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadVideo` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `WavespeedFlashVSRNode` | 1 | comfy-core |
