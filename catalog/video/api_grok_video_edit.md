# Grok: Video Edit

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_grok_video_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_video_edit-1.webp" width="360" alt="Grok: Video Edit api_grok_video_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_video_edit-2.webp" width="360" alt="Grok: Video Edit api_grok_video_edit-2.webp">

> Upload a video to edit. Input your desired modifications. Generate an edited video using the Grok API.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_video_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_grok_video_edit.json)

## Details

| | |
|---|---|
| Name | `api_grok_video_edit` |
| Category | Foundation › Video |
| Output | video |
| Models | Grok |
| Tags | API, Video Edit |
| Type | API |
| Date | 2026-01-28 |
| Author | ComfyUI |
| Min ComfyUI version | 0.16.1 |
| Usage | 34 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #8 | video | futuristic_motorcycle.mp4 |
| output | `SaveVideo` #2 | video | api_grok_video_edit.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GrokVideoEditNode` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
