# Seedance2.5: Video Editing

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_video_editing-1.webp" width="360" alt="Seedance2.5: Video Editing api_seedance2_5_video_editing-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_video_editing-2.webp" width="360" alt="Seedance2.5: Video Editing api_seedance2_5_video_editing-2.webp">

> Edit existing video clips with Seedance 2.5 by describing changes in natural language, enabling local object removal, background swaps, scene replacements, and style transfers while preserving the original composition and motion. Feed in 1 video and receive 1 edited video output with temporally consistent results across frames. Ideal for e-commerce background replacement, stylized remakes of footage, and ad re-editing with targeted retouching.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_video_editing.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_seedance2_5_video_editing.json)

## Details

| | |
|---|---|
| Name | `api_seedance2_5_video_editing` |
| Category | Foundation › Video |
| Media type | image |
| Models | Seedance 2.5 |
| Tags | API, Video Edit |
| Type | API |
| Date | 2026-08-07 |
| Author | ComfyUI |
| Min ComfyUI version | 0.33.2 |
| Usage | 695 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #35 | video | kitten_cop.mp4 |
| output | `SaveVideo` #16 | video | api_seedance2_5_video_editing.json |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ByteDance2ReferenceNodeV2` | 1 |  |
| `LoadVideo` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |
| `Video Slice` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

- Change the `task_type` to switch to video editing mode
- It takes the duration and aspect from the input video

</details>
