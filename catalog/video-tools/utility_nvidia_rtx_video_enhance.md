# RTX Video Enhance: HDR

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_nvidia_rtx_video_enhance-1.webp" width="360" alt="RTX Video Enhance: HDR utility_nvidia_rtx_video_enhance-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_nvidia_rtx_video_enhance-2.webp" width="360" alt="RTX Video Enhance: HDR utility_nvidia_rtx_video_enhance-2.webp">

> Upload a video and chain Nvidia's three RTX video nodes in one pass: super resolution upscale, frame generation and SDR-to-HDR conversion, running locally on your Nvidia RTX GPU. Built for VFX artists and professional video creators.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_nvidia_rtx_video_enhance.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_nvidia_rtx_video_enhance.json)

## Details

| | |
|---|---|
| Name | `utility_nvidia_rtx_video_enhance` |
| Category | Foundation › Video Tools |
| Media type | image |
| Models | None |
| Tags | Video Upscale |
| Type | open source |
| Date | 2026-10-13 |
| Author | ComfyUI |
| Min ComfyUI version | 0.40.0 |
| Distributions | cloud |
| Usage | 594 |
| Nodes | 10 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #6 | video | RTX5090_graphics_card.mp4 |

## Custom nodes required

- [comfyui_nvidia_rtx_nodes](https://registry.comfy.org/nodes/comfyui_nvidia_rtx_nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfyMathExpression` | 1 |  |
| `CreateVideo` | 1 | comfy-core |
| `GetVideoComponents` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `PrimitiveInt` | 1 |  |
| `RTXTrueHDR` | 1 |  |
| `RTXVideoFrameGeneration` | 1 |  |
| `RTXVideoSuperResolution` | 1 | comfyui_nvidia_rtx_nodes |
| `SaveImageAdvanced` | 1 |  |
| `SaveVideo` | 1 | comfy-core |
