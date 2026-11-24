# Video Edit: Crossfade Merge

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates_purz_crossfade)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_purz_crossfade-1.webp" width="360" alt="Video Edit: Crossfade Merge templates_purz_crossfade-1.webp">

> Smoothly blend two video sequences using a crossfade effect. Input two image sequences and define the transition length and blend mode. Outputs a single, merged video sequence.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_purz_crossfade.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_purz_crossfade.json)

## Details

| | |
|---|---|
| Name | `templates_purz_crossfade` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | None |
| Tags | Video, Video Edit |
| Type | open source |
| Date | 2026-03-19 |
| Author | PurzBeats |
| Min ComfyUI version | 0.0.1 |
| Usage | 6 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `VHS_LoadVideo` #3 | video | crossfade_clip_1.mp4 |
| input | `VHS_LoadVideo` #4 | video | crossfade_clip_2.mp4 |

## Custom nodes required

- [comfyui-videohelpersuite](https://registry.comfy.org/nodes/comfyui-videohelpersuite)
- [comfyui_fill-nodes](https://registry.comfy.org/nodes/comfyui_fill-nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `VHS_LoadVideo` | 2 |  |
| `FL_VideoCrossfade` | 1 |  |
| `MarkdownNote` | 1 |  |
| `VHS_VideoCombine` | 1 |  |
| `VHS_VideoInfo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# FL Video Crossfade

Blends two video image sequences together with a crossfade transition.

## Parameters

| Parameter | Default | Notes |
|---|---|---|
| `images_a` | — | First video sequence (IMAGE input). |
| `images_b` | — | Second video sequence (IMAGE input). |
| `crossfade_frames` | 72 | Number of frames over which the crossfade occurs. |
| `blend_mode` | normal | Blending mode used during the transition. |
| `target_width` | 512 | Output width in pixels. |
| `target_height` | 512 | Output height in pixels. |

> **Note:** `target_width` and `target_height` are determined by the dimensions of `images_a` using the `Video Info` node.

> **Tip:** To add more clips, chain multiple FL Video Crossfade nodes — pass the IMAGE output into `images_a` of the next node and connect a new video to `images_b`.

</details>
