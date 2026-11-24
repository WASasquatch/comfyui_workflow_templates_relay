# Vidu Q1: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_vidu_reference_to_video)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_vidu_reference_to_video-1.webp" width="360" alt="Vidu Q1: Reference to Video api_vidu_reference_to_video-1.webp">

> Generate videos with consistent subjects using multiple reference images (up to 7) for character and style continuity across the video sequence.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_vidu_reference_to_video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_vidu_reference_to_video.json)

## Details

| | |
|---|---|
| Name | `api_vidu_reference_to_video` |
| Category | Foundation › Video |
| Output | video |
| Models | Vidu Q1, Vidu |
| Tags | Video, Image to Video, API |
| Type | API |
| Date | 2025-08-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.8.0 |
| Usage | 11 |
| Nodes | 8 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #28 | image | api_vidu_reference_to_video_reference_image_2.jpg |
| input | `LoadImage` #30 | image | api_vidu_reference_to_video_reference_image_1.jpg |
| input | `LoadImage` #45 | image | api_vidu_reference_to_video_reference_image_3.jpg |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 3 | comfy-core |
| `MarkdownNote` | 2 |  |
| `BatchImagesNode` | 1 |  |
| `SaveVideo` | 1 | comfy-core |
| `ViduReferenceVideoNode` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>About Vidu Reference To Video Generation</summary>

You can input multiple reference images simultaneously, such as different perspectives of a character, different scenes, etc., as a reference for the elements in the video, thus ensuring consistency.

</details>

<details><summary>About Reference images</summary>

You can use up to 7 reference images as input.

</details>
