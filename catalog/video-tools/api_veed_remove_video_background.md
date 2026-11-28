# VEED Remove Video Background: Matte Export

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_veed_remove_video_background)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_veed_remove_video_background-1.webp" width="360" alt="VEED Remove Video Background: Matte Export api_veed_remove_video_background-1.webp">

> Cut the subject out of a video with VEED Remove Video Background: the node segments the foreground in every frame and returns the frames plus an alpha mask, and Join Image with Alpha turns that mask into a transparent PNG sequence ready to composite. Choose standard, fast or green-screen keying; clips up to 60 seconds.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_veed_remove_video_background.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_veed_remove_video_background.json)

## Details

| | |
|---|---|
| Name | `api_veed_remove_video_background` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | VEED |
| Tags | API, Remove Background, Video |
| Type | API |
| Date | 2026-10-22 |
| Author | ComfyUI |
| Min ComfyUI version | 0.43.0 |
| Usage | 23 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #3 | video | swimcap_glass_pop_video.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `JoinImageWithAlpha` | 1 |  |
| `LoadVideo` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
| `VeedRemoveVideoBackgroundNode` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Workflow Guide</summary>

## VEED Remove Video Background: Matte Export — Workflow Guide

## Input Asset
- [swimcap_glass_pop_video.mp4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/swimcap_glass_pop_video.mp4)

## How to Use
1. Load a clip up to 60 seconds.
2. Pick the mode: standard, fast (up to 1080p) or green screen.
3. Run; Join Image with Alpha adds the mask as alpha for the PNG save.

## Limits
- Clips up to 60 seconds per run.
- No resolution setting: 3840x2160 (standard, green screen), 1920x1080 (fast).
- MP4 or WebM flattens the matte; save via Join Image with Alpha.
- green screen uses spill_suppression_strength, not refine_foreground_edges or subject_is_person.

</details>
