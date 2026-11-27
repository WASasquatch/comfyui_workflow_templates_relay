# LTX-2.5 (Pro): Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_ltx2_5_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ltx2_5_i2v-1.webp" width="360" alt="LTX-2.5 (Pro): Image to Video api_ltx2_5_i2v-1.webp">

> Generate video from a single image using LTX-2.5's fast distilled model, delivering cinematic multi-shot sequences with consistent characters, lighting, and style across cuts. The workflow outputs a video file with native multishot support and automatic duration prediction. Ideal for rapid storyboarding, social media content creation, and pre-visualization in commercial production pipelines.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ltx2_5_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_ltx2_5_i2v.json)

## Details

| | |
|---|---|
| Name | `api_ltx2_5_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | LTX-2.5 |
| Tags | API, Image to Video |
| Type | API |
| Date | 2026-08-11 |
| Author | ComfyUI |
| Min ComfyUI version | 0.32.0 |
| Usage | 29 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #4 | image | space_battle.png |
| output | `SaveVideo` #2 | video | api_ltx2_5_i2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 |  |
| `LtxApi25ImageToVideo` | 1 |  |
| `SaveVideo` | 1 |  |
