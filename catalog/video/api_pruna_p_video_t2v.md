# Pruna P-Video 2: Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pruna_p_video_t2v-1.webp" width="360" alt="Pruna P-Video 2: Text to Video api_pruna_p_video_t2v-1.webp">

> Generate videos from a single text prompt with Pruna P-Video-2, producing 1-20 second clips up to 1080p at 48 fps with native audio, including ambience, sound effects, and lip-synced dialogue from an optional last-frame image. Ideal for narrative shorts, motion posters, ad B-roll, and dialogue shots.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pruna_p_video_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_pruna_p_video_t2v.json)

## Details

| | |
|---|---|
| Name | `api_pruna_p_video_t2v` |
| Category | Foundation › Video |
| Media type | image |
| Models | P-Video-2 |
| Tags | API, Text to Video |
| Type | API |
| Date | 2026-09-16 |
| Author | ComfyUI |
| Min ComfyUI version | 0.36.0 |
| Usage | 16 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveVideo` #22 | video | api_pruna_p_video_t2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PrunaTextToVideoNode` | 1 |  |
| `SaveVideo` | 1 |  |
