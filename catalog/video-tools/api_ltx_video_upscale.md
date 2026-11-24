# Upscale: LTX VFX

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ltx_video_upscale-1.webp" width="360" alt="Upscale: LTX VFX api_ltx_video_upscale-1.webp">

> Upscale a finished clip with LTX VFX through the partner API. Pick a target preset such as 1080p and the model rebuilds the frame at the higher resolution instead of stretching the source, so edges, grain and small detail come back sharper. Ideal for finishing a low-resolution take or matching a shot to a higher-resolution timeline.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ltx_video_upscale.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_ltx_video_upscale.json)

## Details

| | |
|---|---|
| Name | `api_ltx_video_upscale` |
| Category | Foundation › Video Tools |
| Media type | image |
| Models | LTX-2.5 |
| Tags | API, Upscale, Video |
| Type | API |
| Date | 2026-11-10 |
| Author | ComfyUI |
| Min ComfyUI version | 0.45.1 |
| Usage | 51 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #3 | video | desert_cave_caravan.mp4 |
| output | `SaveVideo` #4 | video | api_ltx_video_upscale.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadVideo` | 1 |  |
| `LtxApiVideoUpscale` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [desert_cave_caravan.mp4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/desert_cave_caravan.mp4)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
