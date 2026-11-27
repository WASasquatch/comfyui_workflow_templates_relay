# Kling 3.0: Video Generation

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_kling_v3_video)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_v3_video-1.webp" width="360" alt="Kling 3.0: Video Generation api_kling_v3_video-1.webp">

> Input text or image prompts to generate 15-second video sequences with multi-shot compositions, complex camera movements, and consistent subjects.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_v3_video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling_v3_video.json)

## Details

| | |
|---|---|
| Name | `api_kling_v3_video` |
| Category | Foundation › Video |
| Output | video |
| Models | Kling 3.0 |
| Tags | API, Image to Video, Video |
| Type | API |
| Date | 2026-02-10 |
| Author | ComfyUI |
| Min ComfyUI version | 0.13.0 |
| Usage | 203 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | boxing.png |
| output | `SaveVideo` #2 | video | api_kling_v3_video.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `KlingVideoNode` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
