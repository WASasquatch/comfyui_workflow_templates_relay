# FLUX 3 Max: Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_flux3_max_t2v-1.webp" width="360" alt="FLUX 3 Max: Text to Video api_flux3_max_t2v-1.webp">

> Generate a video with synchronized audio from a single text prompt with FLUX 3 Max, which reasons about and expands the prompt before rendering. Outputs one clip of 5 to 20 seconds at 720p or 1080p, at any aspect ratio from 9:16 to 21:9, with ambient sound, speech, and effects created alongside the picture and no input files required. Ideal for cinematic concept clips, ad mockups, and social videos that need matching sound design.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_flux3_max_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_flux3_max_t2v.json)

## Details

| | |
|---|---|
| Name | `api_flux3_max_t2v` |
| Category | Foundation › Video |
| Media type | image |
| Models | FLUX 3 Video |
| Tags | API, Text to Video |
| Type | API |
| Date | 2026-10-20 |
| Author | ComfyUI |
| Min ComfyUI version | 0.42.2 |
| Usage | 15 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveVideo` #5 | video | api_flux3_max_t2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Flux3MaxTextToVideoNode` | 1 |  |
| `SaveVideo` | 1 |  |
