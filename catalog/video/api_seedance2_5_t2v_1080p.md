# Seedance2.5 1080P: Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_seedance2_5_t2v_1080p)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_t2v_1080p-1.webp" width="360" alt="Seedance2.5 1080P: Text to Video api_seedance2_5_t2v_1080p-1.webp">

> Generate cinematic 1080P video clips from text descriptions using Seedance 2.5, supporting clips up to 30 seconds with synchronized sound, music, and dialogue across any aspect ratio. Ideal for short comedy scenes, product showcases, and creative storytelling.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_t2v_1080p.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_seedance2_5_t2v_1080p.json)

## Details

| | |
|---|---|
| Name | `api_seedance2_5_t2v_1080p` |
| Category | Foundation › Video |
| Output | video |
| Models | Seedance 2.5 |
| Tags | API, Text to Video |
| Type | API |
| Date | 2026-08-17 |
| Author | ComfyUI |
| Min ComfyUI version | 0.31.0 |
| Usage | 30 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveVideo` #10 | video | api_seedance2_5_t2v_1080p.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ByteDance2TextToVideoNode` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
