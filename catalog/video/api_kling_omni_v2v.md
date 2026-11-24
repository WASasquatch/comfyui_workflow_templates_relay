# Kling O1: Video to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_omni_v2v-1.webp" width="360" alt="Kling O1: Video to Video api_kling_omni_v2v-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_omni_v2v-2.webp" width="360" alt="Kling O1: Video to Video api_kling_omni_v2v-2.webp">

> Transform videos with Kling O1. Edit video content, change styles, or replace characters using text prompts and reference images.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_omni_v2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling_omni_v2v.json)

## Details

| | |
|---|---|
| Name | `api_kling_omni_v2v` |
| Category | Foundation › Video |
| Media type | image |
| Models | Kling O1 |
| Tags | API, Character Reference, Video |
| Type | API |
| Date | 2026-01-10 |
| Author | ComfyUI |
| Min ComfyUI version | 0.8.0 |
| Usage | 32 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #3 | image | blue_shirt_rabbit.jpg |
| input | `LoadVideo` #7 | video | dancing_women.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `BatchImagesNode` | 1 | comfy-core |
| `KlingOmniProVideoToVideoNode` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note</summary>

Select `Batch Images` and Ctrl-B to enable it

</details>
