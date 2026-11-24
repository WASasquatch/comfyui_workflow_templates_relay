# HeyGen: Video Translate

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_heygen_video_translate)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_video_translate-1.webp" width="360" alt="HeyGen: Video Translate api_heygen_video_translate-1.webp">

> Translate video content into another language with full lip-sync using HeyGen Translate, which automatically transcribes speech, translates it, generates a cloned voice, and re-syncs mouth movements. Takes 1 input video and produces 1 output video. Ideal for localizing talking-head videos, dubbing multilingual presentations, and creating lip-synced content for global audiences.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_video_translate.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_heygen_video_translate.json)

## Details

| | |
|---|---|
| Name | `api_heygen_video_translate` |
| Category | Foundation › Video |
| Output | video |
| Models | HeyGen |
| Tags | API, Lip Sync |
| Type | API |
| Date | 2026-07-21 |
| Author | ComfyUI |
| Min ComfyUI version | 0.28.1 |
| Usage | 11 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #5 | video | heygen_input.mp4 |
| output | `SaveVideo` #6 | video | api_heygen_video_translate.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `HeyGenVideoTranslateNode` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
