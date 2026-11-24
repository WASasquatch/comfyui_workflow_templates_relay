# MiniMax H3: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_r2v-1.webp" width="360" alt="MiniMax H3: Reference to Video api_minimax_h3_r2v-1.webp">

> Generate video from a reference image or set of multimodal inputs using MiniMax H3, which interprets text, images, video, and audio together to produce coherent 5–15 second clips with native stereo audio. Input up to 2 images for first/last frame control, or up to 9 images, 3 video clips, and 3 audio clips in Omni Reference mode, and output a single video in your chosen aspect ratio. Ideal for commercial content creation, character-driven storytelling, and rapid visual concept validation.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_r2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_minimax_h3_r2v.json)

## Details

| | |
|---|---|
| Name | `api_minimax_h3_r2v` |
| Category | Foundation › Video |
| Media type | image |
| Models | MiniMax H3 |
| Tags | API, Reference to Video, Image to Video |
| Type | API |
| Date | 2026-07-30 |
| Author | ComfyUI |
| Min ComfyUI version | 0.30.0 |
| Usage | 139 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | 9panel_storyboard_golden_hour_clay_court.png |
| output | `SaveVideo` #3 | video | api_minimax_h3_r2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 |  |
| `MinimaxHailuo03ReferenceNode` | 1 |  |
| `SaveVideo` | 1 |  |
