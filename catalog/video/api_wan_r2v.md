# WAN2.6: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_wan_r2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan_r2v-1.webp" width="360" alt="WAN2.6: Reference to Video api_wan_r2v-1.webp">

> Creating identity-preserved videos with natural movement and cinematic quality.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan_r2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_wan_r2v.json)

## Details

| | |
|---|---|
| Name | `api_wan_r2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan2.6, Wan |
| Tags | API, Character Reference, Video |
| Type | API |
| Date | 2026-01-03 |
| Author | ComfyUI |
| Min ComfyUI version | 0.8.0 |
| Usage | 10 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #34 | video | armored_warrior.mp4 |
| input | `LoadVideo` #35 | video | spear_warrior.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadVideo` | 2 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `WanReferenceVideoApi` | 1 | comfy-core |
