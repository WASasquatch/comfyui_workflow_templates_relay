# HeyGen Video 1.0: Text to Video

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_heygen_video_1_t2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_video_1_t2v-1.webp" width="360" alt="HeyGen Video 1.0: Text to Video api_heygen_video_1_t2v-1.webp">

> Generate a 5-15 second clip with synchronized dialogue and sound from a text prompt using HeyGen Video 1.0, at 480p or 768p in any of six aspect ratios, with no input files required. One video is output. Ideal for UGC-style talking clips, product explainers, and short social ads where the spoken line and the ambience have to match the scene.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_video_1_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_heygen_video_1_t2v.json)

## Details

| | |
|---|---|
| Name | `api_heygen_video_1_t2v` |
| Category | Applied › Character & Fashion |
| Output | video |
| Models | HeyGen |
| Tags | API, Text to Video |
| Type | API |
| Date | 2026-09-30 |
| Author | ComfyUI |
| Min ComfyUI version | 0.38.1 |
| Usage | 17 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveVideo` #3 | video | api_heygen_video_1_t2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `HeyGenReferenceToVideoNode` | 1 |  |
| `SaveVideo` | 1 |  |
