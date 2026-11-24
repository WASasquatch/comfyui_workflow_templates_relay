# LTX-2.5 (Pro): FLF2V

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_ltx2_5_flf2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ltx2_5_flf2v-1.webp" width="360" alt="LTX-2.5 (Pro): FLF2V api_ltx2_5_flf2v-1.webp">

> Generate a video from two reference images using LTX-2.5, blending the content of both frames into a single animated sequence. Ideal for creating transition shots, morphing between two subjects or scenes, and building multi-shot narratives from still references.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ltx2_5_flf2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_ltx2_5_flf2v.json)

## Details

| | |
|---|---|
| Name | `api_ltx2_5_flf2v` |
| Category | Foundation › Video |
| Output | video |
| Models | LTX-2.5 |
| Tags | API, FLF2V |
| Type | API |
| Date | 2026-08-11 |
| Author | ComfyUI |
| Min ComfyUI version | 0.32.0 |
| Usage | 21 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #4 | image | porsche_car_01.png |
| input | `LoadImage` #5 | image | porsche_car_02.png |
| output | `SaveVideo` #2 | video | api_ltx2_5_flf2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `LtxApi25ImageToVideo` | 1 |  |
| `SaveVideo` | 1 |  |
