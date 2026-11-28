# Vidu Q2: FLF2V

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_vidu_q2_flf2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_vidu_q2_flf2v-1.webp" width="360" alt="Vidu Q2: FLF2V api_vidu_q2_flf2v-1.webp">

> Create smooth video transitions between start and end frames with cinematic camera movements, multi-subject consistency.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_vidu_q2_flf2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_vidu_q2_flf2v.json)

## Details

| | |
|---|---|
| Name | `api_vidu_q2_flf2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Vidu Q2 |
| Tags | FLF2V, Video, API |
| Type | API |
| Date | 2026-01-12 |
| Author | ComfyUI |
| Min ComfyUI version | 0.9.0 |
| Usage | 23 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #40 | image | nun_in_church-1.png |
| input | `LoadImage` #42 | image | nun_in_church-2.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `Vidu2StartEndToVideoNode` | 1 | comfy-core |
