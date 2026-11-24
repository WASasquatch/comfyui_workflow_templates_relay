# Kling O3: Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_o3_t2v-1.webp" width="360" alt="Kling O3: Text to Video api_kling_o3_t2v-1.webp">

> Upload text, audio, or images to generate a 15-second video with synchronized audio, character consistency, and storyboard control.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_o3_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling_o3_t2v.json)

## Details

| | |
|---|---|
| Name | `api_kling_o3_t2v` |
| Category | Foundation › Video |
| Media type | image |
| Models | Kling O3 |
| Tags | API, Text to Video |
| Type | API |
| Date | 2026-02-10 |
| Author | ComfyUI |
| Min ComfyUI version | 0.13.0 |
| Usage | 25 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveVideo` #14 | video | api_kling_o3_t2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `KlingOmniProTextToVideoNode` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
