# FLUX 3 Video: Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_bfl_flux3_t2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux3_t2v-1.webp" width="360" alt="FLUX 3 Video: Text to Video api_bfl_flux3_t2v-1.webp">

> Generate full videos from a single text prompt with FLUX 3, which expands natural language into complete scenes with synchronized audio, no reference images or complex settings needed. Outputs 1 video in 720p at 24fps, 5 to 20 seconds long, supporting any aspect ratio from 9:16 to 21:9 with built-in sound design. Ideal for quick social media clips, ad mockups, and concept films requiring realistic motion and cinematic style.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux3_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bfl_flux3_t2v.json)

## Details

| | |
|---|---|
| Name | `api_bfl_flux3_t2v` |
| Category | Foundation › Video |
| Output | video |
| Models | FLUX 3 Video |
| Tags | API, Text to Video |
| Type | API |
| Date | 2026-08-04 |
| Author | ComfyUI |
| Min ComfyUI version | 0.30.2 |
| Usage | 39 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveVideo` #6 | video | api_bfl_flux3_t2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Flux3TextToVideoNode` | 1 |  |
| `SaveVideo` | 1 |  |
