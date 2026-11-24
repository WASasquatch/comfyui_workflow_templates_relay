# Seedance 2.5: FLF2V

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_seedance2_5_flf2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_flf2v-1.webp" width="360" alt="Seedance 2.5: FLF2V api_seedance2_5_flf2v-1.webp">

> Generate a smooth video transition between a user-provided start frame and end frame with Seedance 2.5, which automatically interpolates the motion, camera movement, and visual evolution while locking both endpoints. Ideal for shot transitions, storyboard previz, and before-and-after scene showcases like empty-to-packed or day-to-night shifts.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_flf2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_seedance2_5_flf2v.json)

## Details

| | |
|---|---|
| Name | `api_seedance2_5_flf2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Seedance 2.5 |
| Tags | API, FLF2V |
| Type | API |
| Date | 2026-08-07 |
| Author | ComfyUI |
| Min ComfyUI version | 0.31.0 |
| Usage | 157 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #40 | image | pool_end_frame.png |
| input | `LoadImage` #41 | image | pool_start_frame.png |
| output | `SaveVideo` #16 | video | api_seedance2_5_flf2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `ByteDance2FirstLastFrameNode` | 1 |  |
| `SaveVideo` | 1 |  |
