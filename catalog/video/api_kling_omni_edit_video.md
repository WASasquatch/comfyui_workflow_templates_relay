# Kling O1: Video Edit

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_kling_omni_edit_video)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_omni_edit_video-1.webp" width="360" alt="Kling O1: Video Edit api_kling_omni_edit_video-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_omni_edit_video-2.webp" width="360" alt="Kling O1: Video Edit api_kling_omni_edit_video-2.webp">

> Edit videos with natural language commands, featuring video reference mode for quick generation of high-quality style transfers, element additions, and background modifications.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_omni_edit_video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling_omni_edit_video.json)

## Details

| | |
|---|---|
| Name | `api_kling_omni_edit_video` |
| Category | Foundation › Video |
| Output | video |
| Models | Kling |
| Tags | Video, API, Video Edit, Text to Video, Image to Video |
| Type | API |
| Date | 2025-12-02 |
| Author | ComfyUI |
| Min ComfyUI version | 0.14.0 |
| Usage | 47 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #23 | video | api_kling_omni_edit_video_input_video.mp4 |
| input | `LoadImage` #24 | image | api_kling_omni_edit_video_input_image.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `BatchImagesNode` | 1 |  |
| `KlingOmniProEditVideoNode` | 1 |  |
| `LoadImage` | 1 | comfy-core |
| `LoadVideo` | 1 |  |
| `Note` | 1 |  |
| `SaveVideo` | 1 | comfy-core |
| `Video Slice` | 1 |  |

## Notes embedded in the workflow

<details><summary>Reference Image Limit</summary>

```text
You can use up to 7 reference images if you only use image input.

When you provide video input, you can only use up to 4 reference images.
```

</details>
