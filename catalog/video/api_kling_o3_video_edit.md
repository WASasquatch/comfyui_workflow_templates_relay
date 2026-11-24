# Kling O3: Video Edit

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_o3_video_edit-1.webp" width="360" alt="Kling O3: Video Edit api_kling_o3_video_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_o3_video_edit-2.webp" width="360" alt="Kling O3: Video Edit api_kling_o3_video_edit-2.webp">

> Upload a video and a reference image to edit with Kling O3. Generate a professionally edited video with precise subject editing, scene composition, and native audio-visual synchronization.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_o3_video_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling_o3_video_edit.json)

## Details

| | |
|---|---|
| Name | `api_kling_o3_video_edit` |
| Category | Foundation › Video |
| Media type | image |
| Models | Kling O3 |
| Tags | Video Edit, API, Video |
| Type | API |
| Date | 2026-02-10 |
| Author | ComfyUI |
| Min ComfyUI version | 0.13.0 |
| Usage | 219 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #17 | image | giant_trees_sky_pyramid.png |
| input | `LoadVideo` #25 | video | kling_o3_video_input.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `BatchImagesNode` | 1 | comfy-core |
| `KlingOmniProEditVideoNode` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `Note` | 1 |  |
| `SaveVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note</summary>

```text
Select the Batch Images node, then press Ctrl+B to enable it. Then link the IMAGE output to the reference_images input to enable multiple reference images input.

You can use up to 4 images.
```

</details>
