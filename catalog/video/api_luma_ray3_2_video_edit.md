# Luma Ray 3.2: Video Edit

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_luma_ray3_2_video_edit-1.webp" width="360" alt="Luma Ray 3.2: Video Edit api_luma_ray3_2_video_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_luma_ray3_2_video_edit-2.webp" width="360" alt="Luma Ray 3.2: Video Edit api_luma_ray3_2_video_edit-2.webp">

> Edit videos using natural language commands with Luma Ray 3.2, processing one input video and generating an edited output based on your textual instructions.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_luma_ray3_2_video_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_luma_ray3_2_video_edit.json)

## Details

| | |
|---|---|
| Name | `api_luma_ray3_2_video_edit` |
| Category | Foundation › Video |
| Media type | image |
| Models | Luma |
| Tags | API, Video Edit |
| Type | API |
| Date | 2026-06-22 |
| Author | ComfyUI |
| Min ComfyUI version | 0.26.0 |
| Usage | 9 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #3 | video | subway_guitar_busker.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveVideo` | 2 |  |
| `LoadVideo` | 1 |  |
| `LumaRay32ExtendVideoNode` | 1 |  |
| `LumaRay32VideoEditNode` | 1 |  |
| `MarkdownNote` | 1 |  |
| `PreviewAny` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Extend Video</summary>

This section extends videos and needs a `generation_id` from the upstream Luma Ray 3.2 node.

1. By default, `source_generation_id` is wired automatically. To extend from a previous run instead, disconnect that input and paste the `generation_id` shown in **Preview as Text (generation_id)**.
2. Select this section and press **Ctrl+B** to enable it when you want to extend the video.

</details>
