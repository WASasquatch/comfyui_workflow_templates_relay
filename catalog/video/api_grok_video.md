# Grok: Video generation

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_grok_video)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_video-1.webp" width="360" alt="Grok: Video generation api_grok_video-1.webp">

> Input text prompts or an initial image frame to generate up to 15-second videos with synchronized audio using the Grok model.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_grok_video.json)

## Details

| | |
|---|---|
| Name | `api_grok_video` |
| Category | Foundation › Video |
| Output | video |
| Models | Grok |
| Tags | Video, Image to Video, Text to Video, API |
| Type | API |
| Date | 2026-01-28 |
| Author | ComfyUI |
| Min ComfyUI version | 0.16.1 |
| Usage | 292 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #3 | image | sci-fi_mech.png |
| output | `SaveVideo` #2 | video | api_grok_video.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GrokVideoNode` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
