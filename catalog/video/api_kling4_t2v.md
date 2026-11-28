# Kling 4.0: Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_kling4_t2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling4_t2v-1.webp" width="360" alt="Kling 4.0: Text to Video api_kling4_t2v-1.webp">

> Generate a ten-second cinematic clip from text alone with Kling 4.0, holding one single continuous shot through a full high-speed chase while also producing native stereo audio. Ideal for short-form spectacle, concept pitches, and motion references where a single unbroken take carries the idea.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling4_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling4_t2v.json)

## Details

| | |
|---|---|
| Name | `api_kling4_t2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Kling 4.0 |
| Tags | API, Text to Video |
| Type | API |
| Date | 2026-10-27 |
| Author | ComfyUI |
| Min ComfyUI version | 0.43.0 |
| Usage | 15 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveVideo` #2 | video | api_kling4_t2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Kling4TextToVideoNode` | 1 |  |
| `SaveVideo` | 1 |  |
