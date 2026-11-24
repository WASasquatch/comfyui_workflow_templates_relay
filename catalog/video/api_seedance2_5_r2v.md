# Seedance 2.5: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_seedance2_5_r2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_r2v-1.webp" width="360" alt="Seedance 2.5: Reference to Video api_seedance2_5_r2v-1.webp">

> Generate reference-driven videos with Seedance 2.5 by supplying up to 20 images, 6 video clips, and 6 audio clips to control character consistency, visual style, and motion rhythm in a single 4–30 second output with synchronized sound and lip-synced dialogue. Ideal for e-commerce product showcases, brand advertising, and character-driven short series.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_r2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_seedance2_5_r2v.json)

## Details

| | |
|---|---|
| Name | `api_seedance2_5_r2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Seedance 2.5 |
| Tags | API, Reference to Video |
| Type | API |
| Date | 2026-08-07 |
| Author | ComfyUI |
| Min ComfyUI version | 0.33.2 |
| Usage | 2408 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #12 | image | medusa_poster.png |
| output | `SaveVideo` #16 | video | api_seedance2_5_r2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ByteDance2ReferenceNodeV2` | 1 |  |
| `LoadImage` | 1 |  |
| `SaveVideo` | 1 |  |
