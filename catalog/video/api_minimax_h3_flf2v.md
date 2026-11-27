# MiniMax H3: FLF2V

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_minimax_h3_flf2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_flf2v-1.webp" width="360" alt="MiniMax H3: FLF2V api_minimax_h3_flf2v-1.webp">

> Generate a video from a first and last frame using MiniMax H3, producing a smooth animation between the two images. You provide 2 images, and the workflow outputs a single video clip. Ideal for creating seamless transitions in animation, visualizing before-and-after transformations, and generating consistent motion for character or scene sequences.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_flf2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_minimax_h3_flf2v.json)

## Details

| | |
|---|---|
| Name | `api_minimax_h3_flf2v` |
| Category | Foundation › Video |
| Output | video |
| Models | MiniMax H3 |
| Tags | API, FLF2V, Video |
| Type | API |
| Date | 2026-07-30 |
| Author | ComfyUI |
| Min ComfyUI version | 0.30.0 |
| Usage | 70 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #15 | image | angel-warrior-demon-battle-start.png |
| input | `LoadImage` #16 | image | angel-warrior-demon-battle-end.png |
| output | `SaveVideo` #26 | video | api_minimax_h3_flf2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `MinimaxHailuo03FirstLastFrameNode` | 1 |  |
| `SaveVideo` | 1 |  |
