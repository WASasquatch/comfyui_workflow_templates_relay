# MiniMax H3: Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_minimax_h3_t2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_t2v-1.webp" width="360" alt="MiniMax H3: Text to Video api_minimax_h3_t2v-1.webp">

> Generate video directly from text using the MiniMax H3 model, producing a 5-15 second clip with native stereo audio. Ideal for rapid concept visualization, short-form social media content, and pre-visualization for film or advertising projects.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_minimax_h3_t2v.json)

## Details

| | |
|---|---|
| Name | `api_minimax_h3_t2v` |
| Category | Foundation › Video |
| Output | video |
| Models | MiniMax H3 |
| Tags | Text to Video, API, Video |
| Type | API |
| Date | 2026-07-30 |
| Author | ComfyUI |
| Min ComfyUI version | 0.30.0 |
| Usage | 13 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveVideo` #8 | video | api_minimax_h3_t2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MinimaxHailuo03TextToVideoNode` | 1 |  |
| `SaveVideo` | 1 |  |
