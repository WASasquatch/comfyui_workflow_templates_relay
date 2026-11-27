# Video Upscale: ByteDance vCube

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_bytedance_vcube_video_enhance)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_vcube_video_enhance-1.webp" width="360" alt="Video Upscale: ByteDance vCube api_bytedance_vcube_video_enhance-1.webp">

> Enhance video quality with ByteDance vCube, an AI-driven tool that upscales and restores footage through shot-adaptive processing, fixing compression artifacts and color distortion while preserving original texture. Ideal for improving UGC clips, refining AIGC content, and restoring classic films with vibrant, clear results.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_vcube_video_enhance.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bytedance_vcube_video_enhance.json)

## Details

| | |
|---|---|
| Name | `api_bytedance_vcube_video_enhance` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | ByteDance |
| Tags | API, Video Upscale |
| Type | API |
| Date | 2026-08-24 |
| Author | ComfyUI |
| Min ComfyUI version | 0.33.4 |
| Usage | 46 |
| Nodes | 12 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #3 | video | chill_capybara_dance_pose.mp4 |

## Subgraphs

- **Video Stitch** (8 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfyMathExpression` | 2 | comfy-core |
| `GetVideoComponents` | 2 | comfy-core |
| `SaveVideo` | 2 | comfy-core |
| `ByteDanceVideoEnhanceNode` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `ImageStitch` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `ResizeImageMaskNode` | 1 | comfy-core |
