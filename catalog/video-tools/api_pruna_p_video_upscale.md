# Video Upscale: Pruna P-Video

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_pruna_p_video_upscale)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pruna_p_video_upscale-1.webp" width="360" alt="Video Upscale: Pruna P-Video api_pruna_p_video_upscale-1.webp">

> Upscale and restore a clip with Pruna P-Video in a single node. Pick a target pixel area from 720p to 4K, optionally raise the frame rate, and let one pass rebuild detail instead of only resampling pixels. Clips already larger than the target are enhanced at their own size. Ideal for finishing low-resolution generations for delivery or social crops.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pruna_p_video_upscale.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_pruna_p_video_upscale.json)

## Details

| | |
|---|---|
| Name | `api_pruna_p_video_upscale` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | Pruna P-Video |
| Tags | API, Upscaling, Video |
| Type | API |
| Date | 2026-11-04 |
| Author | ComfyUI |
| Min ComfyUI version | 0.44.0 |
| Usage | 82 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #1 | video | blue_glow_visors_video.mp4 |
| output | `SaveVideo` #3 | video | api_pruna_p_video_upscale.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadVideo` | 1 |  |
| `MarkdownNote` | 1 |  |
| `PrunaPVideoUpscaleNode` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Video Upscale: Pruna P-Video

**Input Assets**
- [blue_glow_visors_video.mp4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/blue_glow_visors_video.mp4) — required workflow input (`input/blue_glow_visors_video.mp4`)

Upscale and restore a clip in one pass: `Load Video` -> **Pruna P-Video Upscale** -> `Save Video`.

**Parameters**

- `target` - output pixel area: `720p` (0.9 MP), `1080p` (2.1), `2K` (3.7), `4K` (8.3). A larger source keeps its size and is only enhanced. Max length 2400 / 1200 / 600 / 300 frames, about 100 / 50 / 25 / 12.5 s at 24 fps.
- `fps` - `source` keeps the clip rate up to 60; a higher value is interpolated, and output above 30 fps costs twice as much.
- `turbo` - faster pass with softer detail, same price.

Aspect ratio is preserved and rounded to even dimensions. Sources above 10 MP need `target` 2K or 4K; input video is capped at 512 MiB.

</details>
