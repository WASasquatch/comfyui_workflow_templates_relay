# MAGI-2: Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_magi2_t2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_magi2_t2v-1.webp" width="360" alt="MAGI-2: Text to Video api_magi2_t2v-1.webp">

> Generate a 1080p video of 4 to 30 seconds with native audio from a text prompt using MAGI-2, Sand.ai's 480B video model. Strong instruction following, complex composition and long-shot stability, with dialogue, foley and score generated in the same pass.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_magi2_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_magi2_t2v.json)

## Details

| | |
|---|---|
| Name | `api_magi2_t2v` |
| Category | Foundation › Video |
| Output | video |
| Models | MAGI-2 |
| Tags | API, Text to Video |
| Type | API |
| Date | 2026-11-28 |
| Author | ComfyUI |
| Min ComfyUI version | 0.46.4 |
| Usage | 0 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveVideo` #2 | video | api_magi2_t2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Magi2TextToVideoApi` | 1 |  |
| `SaveVideo` | 1 |  |
