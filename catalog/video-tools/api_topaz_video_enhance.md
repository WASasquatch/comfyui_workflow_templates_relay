# Video Upscale: Topaz Astra Fast

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_topaz_video_enhance)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_video_enhance-1.webp" width="360" alt="Video Upscale: Topaz Astra Fast api_topaz_video_enhance-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_video_enhance-2.webp" width="360" alt="Video Upscale: Topaz Astra Fast api_topaz_video_enhance-2.webp">

> Enhance videos with Topaz AI. Supports resolution upscaling using Starlight (Astra) Fast model and frame interpolation with apo-8 model.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_video_enhance.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_topaz_video_enhance.json)

## Details

| | |
|---|---|
| Name | `api_topaz_video_enhance` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | Topaz |
| Tags | API, Video Upscale |
| Type | API |
| Date | 2025-11-25 |
| Author | ComfyUI |
| Min ComfyUI version | 0.20.2 |
| Usage | 79 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #8 | video | api_topaz_video_enhance_input_video.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadVideo` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `TopazVideoEnhanceV2` | 1 |  |
