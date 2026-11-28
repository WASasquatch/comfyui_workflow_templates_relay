# Seedance2.5 1080P: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_seedance2_5_i2v_1080p)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_i2v_1080p-1.webp" width="360" alt="Seedance2.5 1080P: Image to Video api_seedance2_5_i2v_1080p-1.webp">

> Generate cinematic 1080P video clips from a single image using Seedance 2.5, animating the still into a moving scene with synchronized sound, music, and dialogue for clips up to 30 seconds across any aspect ratio. Ideal for breathing life into product shots, extending concept art into motion, and creating engaging social media content from photographs.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_i2v_1080p.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_seedance2_5_i2v_1080p.json)

## Details

| | |
|---|---|
| Name | `api_seedance2_5_i2v_1080p` |
| Category | Foundation › Video |
| Output | video |
| Models | Seedance 2.5 |
| Tags | API, Image to Video |
| Type | API |
| Date | 2026-08-17 |
| Author | ComfyUI |
| Min ComfyUI version | 0.33.2 |
| Usage | 1534 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | cosmoscape.png |
| output | `SaveVideo` #7 | video | api_seedance2_5_i2v_1080p.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ByteDance2ReferenceNodeV2` | 1 |  |
| `LoadImage` | 1 |  |
| `SaveVideo` | 1 |  |
