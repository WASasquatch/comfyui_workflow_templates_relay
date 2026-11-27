# Grok: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_grok_reference_to_video)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_reference_to_video-1.webp" width="360" alt="Grok: Reference to Video api_grok_reference_to_video-1.webp">

> Upload a reference image and generate a video using the Grok API, supporting up to 6 reference images for enhanced consistency.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_reference_to_video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_grok_reference_to_video.json)

## Details

| | |
|---|---|
| Name | `api_grok_reference_to_video` |
| Category | Foundation › Video |
| Output | video |
| Models | Grok |
| Tags | API, Character Reference, Video |
| Type | API |
| Date | 2026-03-24 |
| Author | ComfyUI |
| Min ComfyUI version | 0.18.2 |
| Usage | 212 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #5 | image | quiet_girl.png |
| input | `LoadImage` #6 | image | phone.png |
| output | `SaveVideo` #4 | video | api_grok_reference_to_video.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `GrokVideoReferenceNode` | 1 |  |
| `SaveVideo` | 1 |  |
