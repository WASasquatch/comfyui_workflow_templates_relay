# Seedance2.0: First-Last-Frame to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_seedance2_0_flf2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_flf2v-1.webp" width="360" alt="Seedance2.0: First-Last-Frame to Video api_seedance2_0_flf2v-1.webp">

> Upload the first and last frames of your video. Generate a high-quality video sequence using the Seedance2.0 model.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_flf2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_seedance2_0_flf2v.json)

## Details

| | |
|---|---|
| Name | `api_seedance2_0_flf2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Seedance 2.0 |
| Tags | API, FLF2V, Video |
| Type | API |
| Date | 2026-04-13 |
| Author | ComfyUI |
| Min ComfyUI version | 0.26.2 |
| Usage | 186 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #3 | image | sd_first_frame.png |
| input | `LoadImage` #4 | image | sd_last_frame.png |
| output | `SaveVideo` #2 | video | api_seedance2_0_flf2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `ByteDance2FirstLastFrameNode` | 1 |  |
| `SaveVideo` | 1 |  |
